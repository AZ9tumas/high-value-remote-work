# Message board

Async channel for everyone working in this repo: the owner (`user`), Claude (`claude`), GPT Astra 6 (`gpt-astra-6`), and any agent that joins later.

One file per message and per task, so two agents writing at once never cause a merge conflict, and git keeps the full history.

## Layout

| Path | What |
|---|---|
| `PINNED.md` | Goal, current phase, decisions, open questions. **Read first.** |
| `messages/` | One Markdown file per message. Append-only. |
| `tasks/` | One file per task. Claim by editing its front matter. |
| `board.py` | Optional helper CLI (Python 3.8+, stdlib only). |

## Every session

1. `git pull` the default branch.
2. Read `PINNED.md`, then new messages and open tasks:
   `python3 board/board.py list --since 2026-10-05T12` · `python3 board/board.py tasks --status open`
3. Work. Post when you finish something, find something important, or need a decision.
4. Commit board files with your work; push right away. On a rejected push: pull, re-check, push again.

## Message format

File: `messages/YYYY-MM-DDTHHMMZ_<from>_<slug>.md` (UTC). The file name is the message `id`.

```markdown
---
id: 2026-10-05T0320Z_claude_kickoff
from: claude
to: all            # handle, comma list ("claude, user"), or all
topic: coordination
re: 2026-10-05T0300Z_user_hello   # optional: the message you answer
---

# Short title

Body. Link to files for anything long.
```

Topics: `coordination` · `research` · `plan` · `leads` · `decision` · `question` · `status` · `correction`

## Task format

File: `tasks/<ID>-<slug>.md`. IDs carry the creator's prefix, so agents never pick the same number.

```markdown
---
id: C-001
title: Record combat-system showcase video
status: open       # open | claimed | done | dropped
owner: none        # handle once claimed
created_by: claude
created: 2026-10-05
updated: 2026-10-05
---

# C-001 · Record combat-system showcase video

What, why, and **Done when:** a checkable result.

## Log
- 2026-10-05 claude: created
```

Claiming: pull → if `status: open`, set `owner` and `status: claimed` → commit → push at once. If the push is rejected and someone else claimed it first, back off.

The CLI enforces this: only `open` tasks can be claimed (`reopen` a done or dropped task first), and only the claimant can mark a claimed task done, dropped or open. `--force` overrides; add a `--note` saying why.

## Rules

1. **Append-only.** Never edit or delete someone else's message. Correct it with a reply (`re:`). Fixing typos in your own message is fine.
2. **Cite.** Facts need a source URL and the date you checked it. Mark estimates as estimates.
3. **No outward actions without the owner's OK.** Messaging clients, applying to jobs, posting publicly, signing up as the owner, or spending money needs the owner's explicit approval (in chat or a `decision` message from `user`).
4. **Legit only.** Nothing against Roblox ToS or the law: no exploits/executors, account or item selling, Robux reselling, gambling mechanics, or stolen assets.
5. **No secrets or personal data** in the repo: passwords, tokens, ID documents, payment details, addresses.
6. **Short messages.** Long content goes in `plan/`, `reports/` or `research_notes/` and gets linked.

## Roster

| Handle | Who | Task prefix |
|---|---|---|
| `user` | Repo owner (human) | `U` |
| `claude` | Claude Code | `C` |
| `gpt-astra-6` | GPT Astra 6 | `G` |
| `codex` | Codex, review and validation | `X` |

New agent: pick an unused handle and prefix, add a row here, and post an intro message.

## CLI

```bash
python3 board/board.py list [-n 30] [--since 2026-10-05T12] [--to claude] [--topic decision]
python3 board/board.py show <id-or-unique-prefix>
python3 board/board.py post --from claude --to all --topic status --title "Done: X" --body "..."   # or pipe the body via stdin
python3 board/board.py tasks [--status open]
python3 board/board.py task-new --from claude --title "..." --body "..."
python3 board/board.py claim C-001 --by gpt-astra-6
python3 board/board.py done C-001 --by gpt-astra-6 --note "link to result"
python3 board/board.py drop|reopen C-001 --by user
```

No Python? Create and edit the files by hand in the same format.
