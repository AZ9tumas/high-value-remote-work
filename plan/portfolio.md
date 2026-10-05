# Portfolio spec: one offer, one case study

C-006 · claude · 5 Oct 2026. Draft for owner review; nothing has been posted or sent. The for-hire kit in [`outreach/`](outreach/) builds on it.

**Evidence caveat.** Every fact about the owner's work comes from the game repo's README, copied to [`games/stygian-drop/source/README.md`](../games/stygian-drop/source/README.md). That repo is not in this checkout, so nothing here proves the code exists or works, and the README mixes eras (sprint is both installed and not installed). Such claims are marked **owner to confirm** and stay out of public text until confirmed and showable.

## 1. The offer

### Recommended: one moving system, replicated once

Codex's default is a save, duplication or validation fix, but [the brief](codex_income_execution.md) prefers a specialty with stronger evidence. The owner's strongest evidence is a before/after claim backed by an analysis: a scissor-gate sweep costs "one attribute batch plus a bounded collider update, not 289 weld poses per Heartbeat" (README; owner to confirm). A buyer can check that kind of result. Studios and experienced scripters also list optimization and debugging ([freelance note §3](../research_notes/Roblox%20scripter%20income%20strategies/freelance_commission_market.md), [studio note §3](../research_notes/Roblox%20scripter%20income%20strategies/studio_jobs_contracts.md); search summaries).

| Field | Spec |
|---|---|
| Problem | A door, gate, lift, platform or rig moves on the server every frame, costing bandwidth and server time, and stutters on clients |
| Outcome | The server keeps authority over state and collision but replicates each move once (attributes plus a server-clock start time). Clients animate locally; late joiners rebuild the pose |
| Environment | The client's current engine and framework; PC plus one phone; StreamingEnabled as the place uses it |
| Acceptance check | One written scenario (players, cycles, device), run before and after. (1) Network and server-time cost (for example `Stats.DataSendKbps`, `Stats.HeartbeatTimeMs`) meets the targets set in discovery. (2) Parity checklist: timing within tolerance, collisions match, a late joiner sees the live pose, no new remote trusts the client |
| Access | A test copy (Team Create on a copy, or an .rbxl) and the system's scripts. No live game, account, group role or production data |
| Exclusions | Other systems, art or rig changes, new features, publishing to live, any security guarantee |
| Hours | 6 to 12 after discovery (estimate; log actuals) |
| Revisions | One round against the check. A changed check is a new quote |
| Delivery | A calendar date in each quote; default 5 working days after deposit and access |
| Support | 7 days after acceptance, defects against the check only |

**Discovery (separate, capped at 3 h, paid upfront):** reproduce, measure the baseline, set targets, quote a fixed price. If the system is not the cause, the report says so and the job ends.

**Price, a hypothesis to test:** discovery $150; fix $600, 50% deposit. Basis: [`PLAN.md`](../PLAN.md) uses $500 to $1,500 per scoped system, from vendor hiring guides (Memvers, Game-Ace) that are unverified search summaries; a freelance Luau listing pays $40 to $60/h (Sawhorse, date unverified) ([freelance note §2](../research_notes/Roblox%20scripter%20income%20strategies/freelance_commission_market.md), [studio note §2](../research_notes/Roblox%20scripter%20income%20strategies/studio_jobs_contracts.md)). $600 over 6 to 12 h is $50 to $100/h before selling time.

**Demand risk:** buyers ask for data and combat work more often than optimization (freelance note §3). If replies come but nothing gets scoped, ask why; A1 is the one change to consider.

### Alternates

| | A1: one save, duplication or validation bug (Codex's default) | A2: handling pass for one vehicle |
|---|---|---|
| Choose if | The owner has fixed such bugs and can show one | The cars look good on video |
| Evidence (owner to confirm) | Session-locked ProfileStore, Mock store, gameplay gated on load | 19 cars on body movers: per-wheel grip, load transfer, Ackermann steering |
| Problem | One reproducible failure: lost or rolled-back data, duplicated items, or a remote that trusts the client | One car type flips, slides or jitters, or fails under latency |
| Acceptance check | A written reproduction fails before and passes after; a regression check covers it; handover note | Agreed test-course numbers (top speed, braking distance, turning circle, no rollover at stated speeds) on PC and touch |
| Access | Test copy with Mock or test DataStores | Test copy, the car and its scripts |
| Exclusions | Other bugs, migrating live profiles, production access, security guarantee | New models or art, other vehicles, a new chassis |
| Hours (estimate) | 4 to 10 | 8 to 16 |
| Discovery | 3 h cap, $150: reproduce, or report "could not reproduce" | 3 h cap, $150: build the course, record a baseline |
| Fix price (hypothesis) | $500 | $750 |

Environment, revisions, delivery, support and price sources as above.

## 2. Case study

### Template (one page)

1. **Title:** the outcome, in plain words.
2. **Problem:** what was wrong and how it showed.
3. **Role:** what the owner did. Name other contributors, libraries (ProfileStore, Knit), bought assets and AI tools.
4. **Before/after:** one scenario, measured twice, with method and date.
5. **Demo, 30 to 90 s:** title card (5 s); the before, with a stats overlay (15 s); the after, same overlay (20 s); an edge case such as a late joiner (15 s); key code and the test passing (10 s); end card with offer and link (5 s).
6. **One meaningful test** that proves the main claim, and how to run it.
7. **Results:** measured numbers only; otherwise "not measured".

### Candidates (all owner to confirm)

| | Case study | Evidence the owner must pull |
|---|---|---|
| 1 (lead) | **Scissor gate: replicate once, animate on clients.** Four attributes per sweep; each client poses 288 pieces through `Motor6D.Transform`; the server moves only a collision slab | `output/performance/gate-close-analysis-2026-09-18.md`: numbers, scenario, tool, date, and whether measured or counted. The commits that made the change. A recording of old and new in one scenario. A test that a late joiner's pose matches the live pose |
| 2 | **Join flow on session-locked data.** Gameplay waits for preload and the ProfileStore session; clients that never report ready are kicked at 180 s | An `AgentScenarios` playtest report of join, leave and rejoin with data intact (Mock store). A two-server session-lock test. ProfileStore credited |
| 3 | **Per-wheel driving model** on body movers | Test-course numbers and a recording, also with Studio's replication lag on. Proof the car models may be shown |

### Pre-launch secrecy

To keep Stygian Drop quiet, extract one module into a public Rojo repo: a **"replicate once, animate on clients" gate kit** built from plain parts, with no game art, names or story. The hoist's look is already retired from the design ([v0.2 §2](../games/stygian-drop/source/STYGIAN_DROP.md)), so a plain-parts kit reveals little about the game. If the owner wrote the client module alone, it can double as the HiddenDevs script (section 5).

## 3. Fallback demo (only if nothing can be shown)

One demo place: the gate kit, rebuilt from scratch, beside a naive server-posed gate. Set a time cap first (suggest 8 h). Pass checks:

1. Three clients in a local server test: progress at the same server time agrees within tolerance.
2. A client joining mid-sweep shows the live pose.
3. No player passes the closed gate; the collider follows the sweep.
4. Server `Stats.DataSendKbps` logged for both gates over the same 10 sweeps; published numbers come from that log.
5. CI passes: StyLua, selene, strict `luau-lsp analyze`, tests.
6. A 30 to 90 s video per the shot list.

If the owner picks A1: a session-locked inventory with a trade that cannot duplicate items, on the Mock store, checked by a two-server reproduction.

## 4. Public repo layout

```
gate-kit/
  default.project.json   Rojo: the package
  demo.project.json      Rojo: the demo place
  rokit.toml             pinned rojo, wally, selene, stylua, luau-lsp
  wally.toml             dev deps: roblox/jest, roblox/jest-globals
  .luaurc                languageMode "strict"
  selene.toml  stylua.toml
  src/Server  src/Client  src/Shared  src/__tests__/*.spec.luau
  demo/  .github/workflows/ci.yml  README.md  LICENSE
```

- **Tests: Jest Roblox**, https://github.com/Roblox/jest-roblox. Roblox's official Jest port: changelog version 3.20.1 (30 Aug 2026), commits to 2 Oct 2026, on Wally as `roblox/jest`. Runs in Studio, or in CI through Open Cloud Luau Execution (OCALE). Avoid TestEZ (last commit 30 Jan 2023) and the jsdotlua/jest-lua fork (last release 23 Dec 2024). Checked with git, 5 Oct 2026.
- **CI (GitHub Actions):** job 1, every push: `CompeyDev/setup-rokit`, then `stylua --check`, `selene`, and `luau-lsp analyze` with a Rojo sourcemap. Job 2: Jest specs in a private test place through OCALE, key and IDs as repo secrets, like Roblox's [`ocale.yml`](https://github.com/Roblox/jest-roblox/blob/master/.github/workflows/ocale.yml). If job 2 is slow to set up, run Jest in Studio and ship job 1 first.
- **README:** video link first, then purpose, install, a short usage example, how it works, before/after numbers with method and date, credits, license.

## 5. HiddenDevs "Luau Scripter" requirements

From the [freelance note §1](../research_notes/Roblox%20scripter%20income%20strategies/freelance_commission_market.md) (search summaries of hiddendevs.com bulletins 2 to 4; the site is blocked here), rechecked by search on 5 Oct 2026:

- At least 200 lines of Luau in one script, not counting blank or comment lines; at least 80% Luau.
- A direct GitHub link to the file. Repository links and pastes are refused.
- "Sophisticated" intermediate code with a working demo in a Roblox place. Suggested: CFrame math, physics, metatables, open-source libraries.
- Avoid repetition, filler, modules pasted into one file, and 1,000+ lines.
- Sole developer, specifically credited. Team work in that genre is refused.
- **AI-generated or AI-modified code is "very strictly prohibited"**; roles can be revoked later. The game README mentions agent tooling, so submit only a file the owner wrote without AI help.
- Review takes up to 72 hours; then open a ticket.
- The place must be owned by you or credit you in its description (this may belong to another role; comply anyway).
