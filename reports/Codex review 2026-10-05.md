# Review of Claude's work

Codex, 5 October 2026. Reviewed repository commit `08a63442d687a91229e279bfd2dea84c1f6b7d19`. This is a review of the delivered research and design documents, not a blinded concept study or an audit of the separate game's implementation.

## Verdict

**Keep the strategy and the door mechanic. Replace the certainty, the spending assumptions, and the experiment design.**

The strongest recommendation is to pursue paid Roblox engineering work while treating an original game as a limited experiment. Stygian Drop's strongest idea is a familiar safe place whose slow doors turn returning to safety into a decision. Neither a reliable income pipeline nor player demand has yet been demonstrated.

The repository contains substantial research: six income research tracks, a synthesis report and plan, four game concept passes, a merged proposal, imported game documentation, and a Python message board. At the reviewed commit, the Markdown/Python files outside the imported `source/` folder contain approximately **64,980 whitespace-delimited words**. That measures volume, not accuracy or value. The outreach kit, qualified lead list, portfolio proof package, and interview pack are still open tasks. There is no Luau source, playable build, recruitment conversion data, or game analytics here.

I cannot verify the reported approximately $100 spend or which model produced each part without billing/session records. The output is useful desk research, but the next paid work should produce evidence or a usable deliverable rather than another broad research pass. The copied game README describes assets in another repository; their existence, quality, and claimed verification are not established by this checkout.

## Findings, in order of consequence

### 1. Correct the DevEx instructions before acting on them

**High priority.** [PLAN.md](../PLAN.md), the [pinned board](../board/PINNED.md), and [C-002](../board/tasks/C-002-owner-devex-tax-steps-before-15-and-31.md) direct the owner to put tax forms in the DevEx portal, state withholding categorically, and imply requesting by 15 October secures current terms.

Roblox's current [tax documentation][tax], read directly during this review, says:

- 15 October is a **recommended request deadline**, not a guarantee. Tax treatment depends on **payout date**, not submission date. Requests processed on or after 1 November may receive royalty treatment even if submitted earlier.
- Review the **Taxes page in Creator Hub**. It becomes the system of record for forms and treaty claims. Tipalti continues disbursements. An existing valid W-9 may migrate automatically and show **Validated**, requiring no further action.
- Non-US individuals use W-8BEN; entities use W-8BEN-E. Claim treaty benefits only when applicable. Country, tax residence, and entity status are still unknown here.
- For non-US creators without valid information, 24% backup withholding **may** apply to the full payout. With valid information, the documented 0–30% withholding concerns US-player-related earnings and eligibility for treaty benefits.

The dates themselves were verified. The problem is the compressed instructions. Confirm the account's actual status; do not submit duplicate forms or assume everyone needs the same treaty claim.

### 2. The retention gates turn an example into a market benchmark

**High priority.** [REFINED_CONCEPT.md sections 4–5](../games/stygian-drop/REFINED_CONCEPT.md) treats 12% D1 as the similar-game median and 18.7% as a top-decile threshold, then uses these to recalibrate launch decisions.

The actual [analytics documentation][analytics] introduces 12.11%–18.73% with **“For example, if you see…”**. These are illustrative numbers, not a universal benchmark or a measurement of Stygian Drop's peers. The figures are in the analytics-dashboard document; the cited retention page explains cohorts but does not establish those percentiles. The raw research already calls them illustrative; that qualification was lost in the final recommendation.

Keep a provisional target if useful, but label it a hypothesis. Compare the actual game with its actual displayed peer group when available. Report acquisition source, new-player counts, device mix, build version, and matured D1/D7 cohorts. Paid-player retention cannot stand in for Recommended for You retention. A small sample near a threshold is inconclusive, not a reason to greenlight a large build.

### 3. Revenue and completion dates are scenarios, not forecasts

**High priority.** The report's roughly 330 CCU calculation divides platform-wide payouts by platform-wide engagement. The research itself notes avatar-item income, payout lag, skew, and unaudited anecdotes. That is useful context but cannot estimate this unbuilt horror game's revenue. The Q2 financial source was blocked during this review, so I verified the arithmetic conditional on the supplied inputs, not those financial facts.

Sensitivity illustration, **not observed Stygian Drop rates**:

| Assumed monthly gross DevEx per sustained average CCU | Average CCU for $3,000 gross/month |
|---|---:|
| $1 | 3,000 |
| $3 | 1,000 |
| $6 | 500 |
| $10 | 300 |

Use measured Earned Robux, eligible exchange rates, refunds, revenue splits, ads, contractors, fees, and taxes when they exist. A CCU target or 100-DAU program eligibility threshold is not a business viability test.

The income plan likewise treats an unspecified amount of availability as full time, quotes gross revenue as the goal, and schedules a first $3,000 month without owner-specific demand evidence. Job salary bands establish that some roles paid those amounts, not that this owner qualifies or that the roles remain open. The research acknowledges stale posts and vendor-provided rate guides. I could not recheck current job pages because the network proxy blocked them.

**Correction:** use the [income execution brief](../plan/codex_income_execution.md). Track collected cash and total working hours. Treat January 2027 as an ambition, not a forecast. Do not automatically pivot to FiveM just because an untested offer fails.

### 4. The game test cannot support its stated decision as written

**High priority.** M1 specifies six players, consisting of two groups and two solos, but requires two of **three** groups to replay. At two players per group, the described sample contains only two groups. It also combines prototype construction, mobile controls, a threat, a clock, revive behavior, several stops, and an ad experiment into an unsupported 45-hour estimate.

The $100 / 5,000–14,000 plays estimate combines different campaign objectives. Plays are not necessarily unique new people. A cheap-play campaign may optimize for a different audience from the intended co-op horror audience. The original ad announcement was blocked during this review; no cost-per-acquired-new-player forecast is verified.

Further, turning the Passenger off changes the presence of a threat. It does not isolate the effect of door timing. Similar behavior in that comparison could reflect scripted timing, lack of danger, or a weak threat. It is not a clean test of whether slow doors matter.

**Correction:** [the revised experiment](../games/stygian-drop/refinement/codex_review_and_experiment.md) defines a smaller test, consistent participant counts, competing explanations, and a no-spend first gate. No game development or advertising was performed in this review.

### 5. “No griefing” is not supported by the departure rule

**High priority for design.** The rule allows departure when everyone **inside** holds the button. If one player is inside and the rest are outside, that one player satisfies the rule alone. Conversely, unanimity among occupants lets one uncooperative occupant veto departure. Nudging the doors does not solve either voting problem.

The merged proposal also needs rules for disconnects, downed players, obstructing crates, a threat already inside an open lift, and what damage the Passenger can inflict before a nudge pushes it away. These are design gaps, not reproduced implementation bugs. The core hook needs a credible, readable consequence; repeated automatic rescues could turn the return into a waiting sequence.

Test in invite-only parties first. Specify a bounded, visibly signaled departure rule before claiming public matchmaking is ready. Keep paid revives out of the first experiment so payment does not mask frustration with death or waiting.

### 6. Ads can assist discovery without supplying ranking engagement

**Medium priority.** The report says ads test a prototype “rather than grow it.” Roblox's [discovery documentation][discovery] explicitly distinguishes **retrieval** from **ranking**. Ads and other sources can accelerate consideration for organic discovery and bring revenue; the ranking stage uses the behavior of users acquired through Recommended for You.

The accurate instruction is to separate acquisition cohorts and judge each by its purpose. Do not claim paid plays have no discovery effect, or promise they will produce organic distribution. Roblox also says benchmark comparisons themselves are not algorithm inputs.

### 7. Some commercial and design claims outrun their evidence

**Medium priority.** The report dismisses entire side-income categories as unable to reach $3,000 despite lacking representative earnings data. A small sponsor count or a third-party YouTube estimate cannot establish such a ceiling. “Lower priority for this goal” is defensible; “cannot reach” is not established.

The categorical statement that PayPal Goods and Services protects buyers but not sellers is also insufficiently supported by the cited consumer explainer. Check the applicable country's current Seller Protection terms, transaction eligibility, and proof-of-delivery requirements before promising protection or its absence. The legal policy page was blocked here, so I am flagging the claim as unverified rather than substituting a jurisdiction-specific conclusion.

The game scorecard is subjective. Four passes referencing the same research are not four independent market validations. A mechanic being absent from all Roblox elevator games, a title being available, and players liking the proposed ending remain unverified. The 260-hour total is arithmetic over estimates, not a delivery commitment. Reusing M1 and M2 of one idea does not provide two independent concept bets for the income plan's prototype-diversification target.

### 8. The board works for basic use but does not enforce its protocol

**Lower priority.** I exercised `board/board.py` against temporary files, without changing real tasks during the probe:

| Check | Result |
|---|---|
| Post a message and parse it back | Passed |
| Reject non-owner completion of a claimed task without `--force` | Failed: Bob could mark Alice's task done |
| Require `reopen` before claiming an already completed task | Failed: the owner could claim it directly |
| Parse the inline-comment status format shown in the README | Failed: the comment became part of the status |

The existing message list and nine open tasks read successfully. `cmd_post` and task-ID allocation also use check-then-write rather than exclusive creation, so their claimed collision safety is not enforced for concurrent local writers; this race was identified by inspection, not exercised. Git conflict handling cannot prevent two local processes from overwriting before a commit.

These are workflow integrity gaps, not evidence of a remote exploit. Reproduction is in [board_probe.py](../reviews/2026-10-05/board_probe.py). Its nonzero exit intentionally reports the three unmet expectations. I preserved the existing tool under the repository's instruction not to rewrite other agents' work. A focused tool-maintenance change can address these; it should not delay income validation.

## What is already good

- Raw notes often distinguish official sources, search excerpts, vendor estimates, and unknowns. Preserve those distinctions in short recommendations too.
- Dollar contracts, scoped deliverables, deposits/milestones, and guaranteed pay before revenue share form a reasonable starting strategy.
- Keeping original game documents intact and treating v0.3 as a proposal preserves the owner's choices.
- The refuge rule, readable threats, hands-based vulnerability, no required voice chat, and a small prototype are useful design constraints.
- No outside applications, purchases, or public posts are required to prepare the next useful deliverable.

## Validation and limits

Eight official Roblox documents were downloaded over verified HTTPS and matched byte-for-byte to creator-docs commit `9f840b170b3e472c705e035126b45e3e050daed2`. This directly supports the checked policy, analytics, and discovery findings. [source_checks.json](../reviews/2026-10-05/source_checks.json) records URLs, hashes, successful retrievals, and failures. A successful download is not a claim that every line of the original research was fact-checked.

Direct checks of the ad announcement, PayPal policy, three job pages, SEC financial release, and GameAnalytics report were blocked by the network proxy. Their claims remain unverified in this review, not disproved. The game's source repository, Studio build, assets, tests, player data, owner profile, and billing records were unavailable.

Original research and imported game documents are preserved. New work is a review, a practical income brief, a game experiment specification, and reproducible audit evidence. Entry-point addenda link the corrections; no owner design decision, application, purchase, tax action, or publication is implied.

[tax]: https://github.com/Roblox/creator-docs/blob/9f840b170b3e472c705e035126b45e3e050daed2/content/en-us/production/monetization/tax-information.md
[analytics]: https://github.com/Roblox/creator-docs/blob/9f840b170b3e472c705e035126b45e3e050daed2/content/en-us/production/analytics/analytics-dashboard.md
[discovery]: https://github.com/Roblox/creator-docs/blob/9f840b170b3e472c705e035126b45e3e050daed2/content/en-us/discovery.md
