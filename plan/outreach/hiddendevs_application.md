# HiddenDevs Luau Scripter application (draft)

C-004 · claude · 5 Oct 2026. Draft only: apply only with the owner's OK. The requirements in [`../portfolio.md` §5](../portfolio.md) are search summaries of hiddendevs.com bulletins 2 to 4 (checked 5 Oct 2026; the site is blocked here). Read the live bulletins before applying.

## Checklist

- [ ] One script of 200 to 1,000 lines, not counting blank or comment lines. Counted: [COUNT].
- [ ] At least 80% Luau.
- [ ] Written by the owner alone. No team code, no modules pasted together, **no AI-generated or AI-edited lines** (HiddenDevs: "very strictly prohibited"; roles can also be revoked later for unoriginal work).
- [ ] Real intermediate techniques (for example CFrame math, physics, metatables or typed OOP, a client/server split). No filler or repeated blocks.
- [ ] A direct GitHub **file** link (`.../blob/main/src/.../File.luau`), not a repo link or a paste.
- [ ] A working demo in a Roblox place the owner's account owns, or whose description credits the owner.
- [ ] A short demo video (optional; helps the reviewer).
- [ ] The owner can explain every line.
- [ ] 2-step verification on. Never "verify" through a third-party server or link (a documented scam).

## Application text

Edit it to match the file actually submitted. Keep only what the file does.

> **Role:** Luau Scripter
> **Code:** [DIRECT GITHUB FILE LINK]
> **Demo place:** [PLACE LINK] · **Video:** [VIDEO LINK]
>
> This module animates a [N]-piece scissor gate on every client from four attributes the server writes once per sweep: start pose, end pose, start time and duration. Each client works out progress from the shared server clock and poses the pieces through `Motor6D.Transform`, which does not replicate. So a sweep costs one attribute update, not a pose per piece per frame. A player who joins mid-sweep rebuilds the same pose from the same attributes. The server keeps authority over the gate's state and moves only a collision slab.
>
> Techniques: [ONLY WHAT THE FILE DOES, e.g. CFrame math for the scissor linkage, a typed state machine, attribute signals, cleanup on stream-out]. Tests: [N] Jest Roblox specs, run in CI: [CI LINK].
>
> I am the sole developer of this code and wrote it without AI tools. [HANDLE], [YEARS] years of Luau.

If the last line is not fully true, do not apply with this file.

## After applying

Review takes up to 72 hours. If there is no answer by then, open an application ticket (`/ticket`). Record the result on the board.
