#!/usr/bin/env python3
"""Codex review, 2026-10-05: diagnostic expectations, not the repository test suite.

Run from any directory with Python 3.8+. Real board files are never modified.
Exit 1 means at least one documented workflow expectation is unmet.
"""
import contextlib
import importlib.util
import io
import json
import pathlib
import tempfile
import types


def main():
    repo = pathlib.Path(__file__).resolve().parents[2]
    spec = importlib.util.spec_from_file_location("reviewed_board", repo / "board/board.py")
    board = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(board)
    results = []

    def check(name, passed, observed):
        results.append({"check": name, "passed": passed, "observed": observed})

    with tempfile.TemporaryDirectory(prefix="board-review-") as temp:
        board.ROOT = pathlib.Path(temp) / "board"
        board.MSG_DIR = board.ROOT / "messages"
        board.TASK_DIR = board.ROOT / "tasks"
        board.TASK_DIR.mkdir(parents=True)
        task = board.TASK_DIR / "T-001-test.md"
        meta = {"id": "T-001", "title": "Test", "status": "claimed", "owner": "alice"}
        args = types.SimpleNamespace(id="T-001", by="bob", force=False, note=None)

        task.write_text(board.render(meta, "# Test"), encoding="utf-8")
        rejected = False
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                board.update_task(args, "done")
        except SystemExit:
            rejected = True
        actual = board.parse(task)[0]
        check("reject non-owner completion without force",
              rejected and actual.get("status") == "claimed", actual)

        # Independent fixture: the previous check need not fail for this to run.
        meta["status"] = "done"
        task.write_text(board.render(meta, "# Test"), encoding="utf-8")
        args.by = "alice"
        rejected = False
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                board.update_task(args, "claimed", owner="alice")
        except SystemExit:
            rejected = True
        actual = board.parse(task)[0]
        check("require reopen before claiming a completed task",
              rejected and actual.get("status") == "done", actual)

        task.write_text(
            "---\nid: T-001\nstatus: open       # open | claimed | done | dropped\n"
            "owner: none\n---\n\n# Test\n", encoding="utf-8")
        status = board.parse(task)[0].get("status")
        check("parse documented inline status comment", status == "open", status)

        args = types.SimpleNamespace(sender="codex", title="Roundtrip", to="user",
                                     topic="status", re=None, body="Smoke test body",
                                     body_file=None)
        with contextlib.redirect_stdout(io.StringIO()):
            board.cmd_post(args)
        actual, body = board.parse(next(board.MSG_DIR.glob("*.md")))
        check("message post/parse round trip",
              actual.get("from") == "codex" and "Smoke test body" in body, actual)

    print(json.dumps(results, indent=2))
    return 0 if all(row["passed"] for row in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
