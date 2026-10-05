# Stygian Drop: review and smaller experiment

Codex, 5 October 2026. Idea work only. I read v0.3 before completing this review, so this is **not** the blinded independent pass requested in C-001. The owner's v0.2 and Claude's proposals remain unchanged. No game has been built or playtested here.

## Recommendation

Keep **Stygian Drop** as the working title. Use **“The lift is safe. Getting everyone back inside is not.”** as the test pitch. Test the Close before committing to a new title, an ending, daily progression, or a launch date.

The valuable idea is not technically elaborate doors alone. It is a decision a player can read: **bank what we have now, or help someone bring one more thing back?** The machinery makes that decision visible and gives it a physical cost. It succeeds if players voluntarily take that risk again after they understand it.

Protect the lift's safety when sealed, understandable threat behavior, vulnerable hands, and quiet contrast. Avoid making every stop an automatic chase. If all returns have the same mandatory timer and automatic nudge rescue, the player learns a schedule instead of weighing a risk.

## What to keep and what to defer

Keep one readable threat, a useful optional object, a short task that occupies the hands, clear door feedback, a way to help a partner, and a fair failure/retry. Use the existing lift only after checking it in the actual game repository.

Defer Daily Drop, streaks, a season track, persistent trophies, a store, paid revives, public matchmaking, multiple threats, driving encounters, an endless mode, and the final reveal. These may belong in a later game. They cannot rescue an unproven core interaction, and adding them makes the first experiment harder to interpret.

The scorecard scores and 260-hour schedule are design judgments. Establish integration cost in the real project before estimating. The separate README contains mixed-era descriptions, including both an installed sprint system and a statement that sprint is not installed; documentation alone cannot establish current behavior.

## Define a coherent test before building

For an invite-only prototype, use one floor with one return decision and a deterministic threat. Let players learn the rule, then offer a voluntary second attempt with a different object position or timing. The player should understand why leaving the lift is useful within the first minute. That is a design target, not a sourced industry threshold.

The prototype needs an unambiguous answer to each case:

| Case | Proposed behavior to test |
|---|---|
| Everyone standing is back inside | Anyone may request close; show the committed departure clearly |
| Someone is outside | Do not treat one occupant's vote as team consent. Use a visibly announced last-call countdown with a bounded hold extension |
| Repeated obstruction | A blocker cannot reset last-call time forever. Clearly show what will happen to people and objects when the hold expires |
| Player is downed | A teammate can make a legible rescue attempt; otherwise the player can rejoin the next attempt without buying anything |
| Disconnect or AFK player | Cannot freeze departure or require a paid revive to restore the party. Define the boundary before testing |
| Threat reaches the doorway | Specify reachable damage, warning, counterplay, and what the nudge does. Do not invent those rules during a test |
| Threat or car crosses into the lift | Explicitly resolve it before declaring the lift sealed and safe; never trap an unexplained active threat inside the promised refuge |
| No players remain alive | Free, prompt restart; no long spectator wait |
| Object crosses the banking boundary twice | It counts once per attempt. Closing the doors is not an unlimited reward source |

The exact timing is tunable. Public-lobby anti-griefing needs its own later validation; this table is not a claim that it is solved.

## Experiment A: comprehension and voluntary risk

**Proposed sample: eight new participants, comprising three pairs and two solos.** Each person participates once in the first-exposure sample. This is qualitative testing, not a market-size or retention estimate. Device coverage must include the intended mobile interaction before recruiting paid traffic.

Use the same instructions and build for each session. Do not tell participants that the doors are the intended hook. Ask afterward what they thought the rule was, why they returned when they did, what felt unfair, and whether they want another attempt. Obtain appropriate consent for any recording; anonymous written observations are sufficient.

Record:

- Whether they understood the objective, door warning, and cause of failure without coaching.
- Whether they chose between saving an object and helping a teammate, rather than merely waiting for an animation.
- Whether each pair voluntarily starts another attempt when genuinely free to stop.
- Whether the solos have an actual decision rather than the co-op task with one role missing.
- Doorway hesitation, failed inputs, obstruction, disconnections, frustration, and reported unfair deaths.

Working continuation signals: at least two of the three pairs voluntarily retry; a majority can accurately explain the risk; and no repeated blocker makes the task impossible on the supported device. These are **proposed internal criteria**, not industry benchmarks. One success in a friendly group is insufficient. Record disagreements and confusion alongside positive quotes.

If the test mainly finds control or comprehension problems, fix those and repeat with fresh participants. If players understand the rules but find no reason to risk another return, redesign the reward/decision before adding progression. Limit repair work to a separately agreed time cap.

## Experiment B: does the door decision add value?

Only after comprehension is reliable, compare the current slow-close version with a shorter, predictable-close version. Keep the threat, objective, reward, and other timings as comparable as possible. Counterbalance order across groups and record order, because surprise cannot be restored for a second playthrough.

Measure decisions and voluntary replay, not just screams, session length, or whether someone mentions the doors. If the slow-close version is only more confusing or longer, realism is not earning its cost. This is exploratory evidence; a small crossover test cannot establish statistical superiority or commercial demand.

Turning the Passenger off can separately test whether the threat creates any pressure, but it does not isolate door timing. Do not draw the original proposal's causal conclusion from that comparison alone.

## Paid testing comes later

An owner-approved ad test needs a stable build, verified funnel events, an acquisition objective, a hard spending cap, and a minimum sample/time plan written before it starts. No universal cost-per-play or promised number of new users is available here.

Count unique new players separately from visits and replays. Track acquisition source, build, device, party size, successful load, first objective, first return, death, completion, and voluntary restart. Keep full incoming-player denominators, with loading failures and early exits visible. Do not drop bounces to improve reported retention. Do not pool invited testers, ad players, and Recommended for You players as one comparable cohort.

For each daily new-player cohort, report D1 only after the following day and D7 only after the relevant seventh day, following [Roblox's cohort definitions](https://github.com/Roblox/creator-docs/blob/9f840b170b3e472c705e035126b45e3e050daed2/content/en-us/production/analytics/retention.md). Report the numerator and denominator, not just a percentage. Account for repeated players and correlation within parties when interpreting uncertainty.

The often-quoted **12.11% and 18.73% are illustrative** in the [analytics documentation](https://github.com/Roblox/creator-docs/blob/9f840b170b3e472c705e035126b45e3e050daed2/content/en-us/production/analytics/analytics-dashboard.md#benchmarking). Use the actual game's relevant comparison group when available and provisional internal goals otherwise. Do not treat a narrowly passed threshold as proof of profitability.

Ads can assist discovery consideration; ranking engagement comes from Recommended for You users, per [Roblox's discovery documentation](https://github.com/Roblox/creator-docs/blob/9f840b170b3e472c705e035126b45e3e050daed2/content/en-us/discovery.md). Segment those cohorts instead of saying ads either guarantee growth or cannot grow a game.

## Next decision

The next justified commitment is a small, owner-approved core test after inspecting the actual project. Continue only if the core earns voluntary replay and the owner can afford the time without delaying the income objective. Do not approve the store, public launch, long-term content schedule, or ending as a package with that experiment.
