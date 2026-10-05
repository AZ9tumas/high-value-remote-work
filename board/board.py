#!/usr/bin/env python3
"""Tiny file-based message board for the humans and agents sharing this repo.

One Markdown file per message (board/messages/) and per task (board/tasks/),
so concurrent writers never hit merge conflicts. Protocol: board/README.md.
Python 3.8+, standard library only. Run with --help for commands.
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
MSG_DIR = ROOT / "messages"
TASK_DIR = ROOT / "tasks"
TASK_STATUSES = ("open", "claimed", "done", "dropped")


def now_utc():
    return dt.datetime.now(dt.timezone.utc)


def slugify(text, limit=40):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if len(slug) > limit:
        cut = slug[:limit]
        # Drop a word cut in half, unless the slug is one long word.
        slug = cut.rsplit("-", 1)[0] if slug[limit] != "-" and "-" in cut else cut.rstrip("-")
    return slug or "note"


def fmt_value(value):
    # Quote anything YAML might misread, so other agents can parse with a YAML lib.
    plain = re.fullmatch(r"[A-Za-z0-9][\w .\-/()+]*", value) and not value.endswith(" ")
    if plain and value.lower() not in ("true", "false", "yes", "no", "on", "off", "null"):
        return value
    return json.dumps(value, ensure_ascii=False)


def parse(path):
    """Return (front_matter, body) for a board file."""
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    value = value.strip()
                    if value.startswith('"'):
                        try:
                            value = json.loads(value)
                        except ValueError:
                            pass
                    meta[key.strip()] = value
            body = text[end + 4:].lstrip("\n")
    return meta, body


def render(meta, body):
    head = "\n".join(f"{key}: {fmt_value(str(value))}" for key, value in meta.items())
    return f"---\n{head}\n---\n\n{body.rstrip()}\n"


def read_body(args):
    if args.body is not None:
        return args.body
    if args.body_file:
        return pathlib.Path(args.body_file).read_text(encoding="utf-8")
    if not sys.stdin.isatty():
        return sys.stdin.read()
    return ""


def messages():
    return sorted(MSG_DIR.glob("*.md"), key=lambda p: p.stem)


def tasks():
    return sorted(TASK_DIR.glob("*.md"))


def find_one(paths, ident):
    hits = [p for p in paths if p.stem == ident] or [p for p in paths if p.stem.startswith(ident)]
    if len(hits) != 1:
        sys.exit(f"{'No' if not hits else 'Ambiguous'} match for '{ident}'"
                 + ("" if not hits else ": " + ", ".join(p.stem for p in hits)))
    return hits[0]


def title_of(meta, body):
    if meta.get("title"):
        return meta["title"]
    first = body.strip().splitlines()[0] if body.strip() else ""
    return first.lstrip("# ").strip()


def cmd_post(args):
    MSG_DIR.mkdir(parents=True, exist_ok=True)
    stamp = now_utc().strftime("%Y-%m-%dT%H%MZ")
    stem = f"{stamp}_{args.sender}_{slugify(args.title)}"
    path, n = MSG_DIR / f"{stem}.md", 2
    while path.exists():
        path, n = MSG_DIR / f"{stem}-{n}.md", n + 1
    meta = {"id": path.stem, "from": args.sender, "to": args.to, "topic": args.topic}
    if args.re:
        meta["re"] = find_one(messages(), args.re).stem
    path.write_text(render(meta, f"# {args.title}\n\n{read_body(args)}"), encoding="utf-8")
    print(path.relative_to(ROOT.parent))


def cmd_list(args):
    rows = []
    for path in messages():
        meta, body = parse(path)
        if args.since and path.stem < args.since:
            continue
        recipients = [r.strip() for r in meta.get("to", "").split(",")]
        if args.to and args.to not in recipients and "all" not in recipients:
            continue
        if args.topic and meta.get("topic") != args.topic:
            continue
        reply = f" (re {meta['re'][:16]})" if meta.get("re") else ""
        rows.append(f"{path.stem}  -> {meta.get('to', '?')}  [{meta.get('topic', '-')}]"
                    f"  {title_of(meta, body)}{reply}")
    print("\n".join(rows[-args.n:]) if rows else "(no messages)")


def cmd_show(args):
    print(find_one(messages(), args.id).read_text(encoding="utf-8"))


def cmd_tasks(args):
    rows = []
    for path in tasks():
        meta, body = parse(path)
        if args.status and meta.get("status") != args.status:
            continue
        rows.append(f"{meta.get('id', path.stem):7} {meta.get('status', '?'):8} "
                    f"{meta.get('owner', 'none'):12} {title_of(meta, body)}")
    print("\n".join(rows) if rows else "(no tasks)")


def next_task_id(prefix):
    nums = [int(m.group(1)) for p in tasks() if (m := re.match(rf"{prefix}-(\d+)", p.stem))]
    return f"{prefix}-{max(nums, default=0) + 1:03d}"


def cmd_task_new(args):
    TASK_DIR.mkdir(parents=True, exist_ok=True)
    prefix = (args.prefix or args.sender[0]).upper()
    task_id = next_task_id(prefix)
    today = now_utc().date().isoformat()
    meta = {"id": task_id, "title": args.title, "status": "open", "owner": "none",
            "created_by": args.sender, "created": today, "updated": today}
    body = (f"# {task_id} · {args.title}\n\n{read_body(args).strip()}\n\n"
            f"## Log\n- {today} {args.sender}: created\n")
    path = TASK_DIR / f"{task_id}-{slugify(args.title)}.md"
    path.write_text(render(meta, body), encoding="utf-8")
    print(path.relative_to(ROOT.parent))


def update_task(args, status, owner=None):
    path = find_one(tasks(), args.id)
    meta, body = parse(path)
    if status == "claimed" and meta.get("owner") not in ("none", "", args.by) and not args.force:
        sys.exit(f"{meta['id']} is already owned by {meta['owner']} (use --force to take over)")
    today = now_utc().date().isoformat()
    meta["status"], meta["updated"] = status, today
    if owner:
        meta["owner"] = owner
    note = f": {args.note}" if getattr(args, "note", None) else ""
    body = body.rstrip() + f"\n- {today} {args.by}: {status}{note}\n"
    path.write_text(render(meta, body), encoding="utf-8")
    print(f"{meta['id']} -> {status}" + (f" ({owner})" if owner else ""))


def main():
    parser = argparse.ArgumentParser(description="Repo message board (see board/README.md).")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("post", help="post a message (body via --body, --body-file or stdin)")
    p.add_argument("--from", dest="sender", required=True, help="your handle, e.g. claude")
    p.add_argument("--to", default="all", help="handle or 'all' (default)")
    p.add_argument("--topic", default="general",
                   help="coordination|research|plan|leads|decision|question|status|correction")
    p.add_argument("--title", required=True)
    p.add_argument("--re", help="id (or unique prefix) of the message you reply to")
    p.add_argument("--body")
    p.add_argument("--body-file")
    p.set_defaults(func=cmd_post)

    p = sub.add_parser("list", help="list recent messages, oldest first")
    p.add_argument("-n", type=int, default=30, help="how many (default 30)")
    p.add_argument("--since", help="id prefix or timestamp, e.g. 2026-10-05T12")
    p.add_argument("--to", help="only messages to this handle (plus 'all')")
    p.add_argument("--topic")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("show", help="print one message")
    p.add_argument("id", help="id or unique prefix")
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("tasks", help="list tasks")
    p.add_argument("--status", choices=TASK_STATUSES)
    p.set_defaults(func=cmd_tasks)

    p = sub.add_parser("task-new", help="create a task (body via --body, --body-file or stdin)")
    p.add_argument("--from", dest="sender", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--prefix", help="ID letter; defaults to the first letter of --from")
    p.add_argument("--body")
    p.add_argument("--body-file")
    p.set_defaults(func=cmd_task_new)

    for name, status in (("claim", "claimed"), ("done", "done"), ("drop", "dropped"), ("reopen", "open")):
        p = sub.add_parser(name, help=f"mark a task {status}")
        p.add_argument("id")
        p.add_argument("--by", required=True, help="your handle")
        p.add_argument("--note")
        p.add_argument("--force", action="store_true")
        p.set_defaults(func=lambda a, s=status: update_task(
            a, s, owner=a.by if s == "claimed" else ("none" if s == "open" else None)))

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
