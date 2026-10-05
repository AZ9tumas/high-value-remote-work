# Stygian Drop: refined concept (v0.3 proposal)

> **Codex review, 5 October 2026:** Original proposal preserved below. Read the [review and smaller experiment](refinement/codex_review_and_experiment.md) before adopting its gates. The 12%/18.7% retention figures are illustrative examples; the stated tester counts do not match the group-replay gate; and unanimous agreement among occupants does not prevent one occupant from abandoning everyone outside. The new document proposes corrections without approving a build or ad spend.

*Merge of the four idea passes, 5 October 2026. Idea only. [OGE] and [PEP] are `own_games_economics.md` and `platform_economics_payouts.md` in `research_notes/Roblox scripter income strategies/`. [Brief] is `source/elevator_blender_prompt.md`. [PLAN] is `PLAN.md`.*

## 1. Verdict

**Recommend v0.3, "the Close":** v0.2's on-foot stops and refuge rules, with the slow real doors as the core, a clock on every stop, and progress banked each time the doors shut.
**Hook:** The lift is safe. The four seconds its doors take to close are not.
**Why it is good:** it turns the rarest thing already built, real doors with a light curtain, into a mechanic no Roblox elevator game has (unverified). Every return can become a clip, friends need no chat, and it ships in about 260 hours.

## 2. Scorecard

1 is poor, 5 is strong. Long Stay is the bold pass's pick.

| | v0.2 | Faithful | Long Stay | **v0.3** |
|---|---|---|---|---|
| Click appeal | 2: "Drop" reads as a dropper | 3: same title, strong door image | 3: a car in a lift is new | **4**: genre word, headlights icon |
| First 3 minutes | 2: quiet 3 to 5 min [OGE §4] | 4: beam trip by 2:30 | 4: chase and prize; busy | **4**: goal in 10 s, sign by 3:00 |
| Retention D1/D7 | 1: nothing persists | 3: Daily Drop, notes | 4: 100+ entry car Ledger | **4**: Daily Drop, banking, trophies; unproven |
| Friend play | 3: rules undefined | 4: stand in the beam | 4: roles, but one drives | **5**: Hold, Watch, Operator, the vote |
| Clip-ability | 3: subtle by design | 4: arm in the doors | 4: "it won't start" | **5**: last one in, headlights in the gap |
| Monetization fit | 2: nothing to buy early | 4: capped revives, skins | 4: big store; speed-ups off-tone | **4**: fare at death, skins, lift objects |
| Solo scope | 3: 360 h, two bands | 4: 220 h, likely low | 1: 550 to 600 h, $3k to $6k art | **4**: about 260 h, one band |
| Asset reuse | 3: cars as dressing | 4: doors central | 5: the lift carries cars | **4**: doors, rear face, hands, P3, cars |
| Originality, near-duplicate risk | 2: three crowded lanes at once | 3: the Close is new (unverified) | 4: car-recovery horror (unverified) | **3**: crowded lane; the Close is ours (unverified) |
| **Total** | 21 | 33 | 33 | **37** |

Scope binds at 10 to 15 h/week [PLAN], so Long Stay loses despite the tie.

**Signal.** All four passes, independently: the first stop is too slow for the 60 to 180 s bounce window [OGE §4]; a car belongs in the lift; a daily shared target; revives first; R15 and a 16+ launch; one band at launch. Three: the doors as the identity; a lower D1 gate with an ad test.

**Conflicts, ruled**

| Conflict | Ruling and reason |
|---|---|
| On-foot stops, or car recovery (bold) | On foot; the car is the peak. Long Stay costs a year of the owner's hours, and a drivable car is a second refuge |
| Bands of 27 min (faithful), or 10 to 15 (market, critique) | About 16 min, banked at every close, so a wipe never erases a session |
| Anyone leaves (faithful), betrayal (market), or a vote (critique) | The vote; timed stops leave alone. No griefing, and "left behind" survives |
| Threats that hear voice (market); a chase view (bold) | Neither. One punishes voice users; the other breaks first person |
| Posted rules, the Warden, the hub, restore timers, the Tow (bold) | Cut. Signs give away the rule v0.2 wants learned by watching; the lift is home; timers fight horror pacing; mass Headlights is a cheaper peak |

## 3. The concept (v0.3 proposal)

### Pitch

First-person co-op horror for 1 to 4. A vehicle lift takes your crew down through a car park that goes too deep. At each stop you step out, do one job with your hands, and get back before the floor wakes up. Its doors take four seconds to close and reopen for anything in the beam. You never fight. You decide who holds the doors.

### Public title

**Don't Miss the Elevator** (market's pick): genre word, loop and stakes. Alternatives: **Make It Back** (best thumbnail text, no genre word) and **Sublevel** (ownable, weak in search). Check all three in Roblox search (unverified). No "Doors" (too close to DOORS), "Backrooms" or "The [adjective] Elevator". "Stygian" moves to the maker's plate and names the bottom. Icon: headlights in the closing gap. Thumbnails: MAKE IT BACK, HOLD THE DOORS, DON'T LOOK AWAY; two or more lift play-through about 8.5% [OGE §4].

### Pillars

1. **The lift is home.** Nothing reaches you while the doors are shut.
2. **The doorway is the decision.** Who and what makes it through is the crew's call.
3. **Learn the rule, never the reason.**
4. **Your hands are the risk.** Every useful action costs view, light or speed.
5. **One more stop.** Something good sits just past safe, and the floor is waking.

### Signature mechanic: the Close

- **Slow:** about 3 s to open, 4 to close, 4 to 6 s dwell [Brief §5.2].
- **The beam:** anything in the doorway reopens them; a red edge strip shows where. The gap stops fitting a crate before it stops fitting a person.
- **The nudge:** on the third reopen, a buzzer and half speed that push players in and threats out.
- **The hands:** whoever presses CLOSE stands nearest the floor.
- **The empty lift:** with everyone out, the doors shut and the car waits, dark. Calling it back puts your back to the floor.
- **Leaving:** only when every standing player is inside, or everyone inside holds the button for 3 s. Timed stops leave alone.
- **Banking:** when the doors meet, everything inside is yours for good.
- **The fire key:** rare, never sold. Hold CLOSE for 4 s to ignore the beam.
- **The clock:** each stop goes quiet, stirring, awake, pushed by time, light, noise and cancelled hand actions. The far tubes die first. At awake the threat heads for the lift; an empty stop goes dark toward you.

### Run structure

| Segment | Minutes |
|---|---|
| P1 landing; a public lift leaves at 4 players or 30 s | 0.5 |
| Six stops, 0.5 to 2.5 min out each, plus a 25 s descent | 10 to 13 |
| Long Stay, the checkpoint and peak | 3 to 4 |
| End screen: banked items, a new Log line, "Ride again" | 0.5 |
| **One run** | **about 16** |

Two runs make a 30-minute session; 19+ minute sessions go with double-digit D1 [OGE §1]. After each stop two floor buttons light; their halos hint at the next condition. Stops are 6 authored layouts on the P3 kit, mirrored to 12, rolling purpose (none, power, key, ticket, load), condition (dark, timed, alarm, rear doors) and threat. Below Long Stay the car park keeps going, harder, for the depth board.

**Death:** 45 s to be revived (4 s, both hands), then the lift's CCTV until a fare calls you back. Solo gets one free fare per band. A wipe returns you to the last checkpoint, banked items kept. Deaths show 2 s of third person first.

### The first 3 minutes

| Time | Beat |
|---|---|
| 0:00 | P1 landing, party included, no menu. Car 04 arrives; both door sets telescope open |
| 0:10 | Walk in; the edge strip flicks red at your height. Only P3 lights |
| 0:20 | Descent. The display shows a level not on the panel, once |
| 0:40 | A lit, ordinary car park. A note readable from the doorway: "Breaker by the ramp. Walk." The doors close behind you; the call button is dead |
| 0:50 | The walk. Nothing happens |
| 1:30 | Both hands in the breaker cabinet, view narrowed. Behind you, a dome light clicks on |
| 1:55 | Back past the lit car. A coat on the seat |
| 2:15 | In, CLOSE. Halfway, the doors reopen: one red segment at knee height. Nobody there. Again |
| 2:45 | Third time: buzzer, nudge. In the last hand-width of gap, the lit car's headlights come on |
| 3:00 | Shut. "Banked: 1 ticket." Stop 2 has the Passenger |

Nothing can hurt you yet (v0.2's rule). Returning players skip it.

### Threats

One per stop at most, never inside a closed lift, never killed. One humanoid rig in three costumes.

| Threat | Behaviour | Counterplay | The clip |
|---|---|---|---|
| **The Passenger** | Once the floor wakes, follows the last player back. Never crosses the sill: stands in the beam, reaches in | Return early, together; back wall; fire key | The crew on the back pads as the doors close on its arm |
| **Headlights** | A parked car that creeps a bay whenever nobody looks; rolls in through open doors if you look away | One watches, one works. Solo, it moves only while your hands block your view | Four players staring through the closing gap |
| **The Attendant** | Walks between pay stations toward light, including a lift held open | Torch off, stand still, throw a flare | Torches off, all frozen, it walks between you |
| **The Occupant** | Hides in one car marked by one change. Open it and you are down | Remember the cars; chalk the checked ones | He reaches in for a battery; it is in the back seat |

**Peak, Long Stay:** the panel reads VEHICLES ONLY. Hotwire the person's car and drive it in while every parked car is a Headlights. Stop short and the bumper holds the doors open.

**Tools,** found and never sold: torch, chalk (pings, stencils only [PEP §6]), flares, the fire key. The Leak waits for the Service update, with its flooded bays.

### Meta progression, and tomorrow

- **Depth:** checkpoints become start floors. Crews start from the deepest one all members share, so newcomers get the intro; veterans earn a fare for bringing them.
- **The Log:** surviving a threat fills its page: how to survive it, never what it is.
- **Trophies:** bulky finds carried back in both hands hang on your hook in the lift for good, where your crew sees them.
- **Fares:** one currency, from stops, clears and the first run of the day.

**Why come back tomorrow:** the **Daily Drop**: one seed for everyone, a depth board, and one named lost item on a stated level ("A stopped clock. P11. Today only."). A streak pays fares. A new situation card each week. Saturdays, when play peaks [OGE §4]: Deep Shift, every level dark, trophies doubled.

### Co-op moments

- **The Hold:** on timed stops one holds OPEN for a runner with a crate, and sees what follows them.
- **The Watch:** one keeps eyes on Headlights while another works.
- **The Operator:** a dead landing panel means one stays to run the doors. The chime (once "come", twice "stay away") needs no voice, and wakes the floor.
- **The Vote and the Call-back:** leaving a friend takes everyone inside; a fare brings them back, standing in the car when the doors next open.

Voice is optional, muffled by closing doors. Chat needs an age check [OGE §4], so all of it works with pings.

### Mystery, and the bottom

Lore is held in the hands, one line at most. Tickets are stamped 23:58 on every level. The person's car turns up more wrong each time. Their field notes explain survival, never cause. The inspection card by the panel gains a line per run: "Door dwell exceeded rating by 1.8 s. Cause not found." The care stays rare: it answers what a player just did, while they look, once a band at most. One reveal per checkpoint; each band ships as an update.

**At the bottom, "Stygian":** the machine room. Monitors show every landing; on one, a new crew boards at P1. In the chair is the person you followed, arms ash gray like yours. They drove your lift: every door that waited, every light already on. The note says "Your shift." One button: HOLD. Someone runs for the doors. It explains every kindness, makes the grafts a uniform, and answers who, never what.

### Monetization

Section 13 holds: no immunity, no paid random items.

- **Fares**, the ferryman's coins, are the revive, Roblox's own example consumable [OGE §6]. One calls back a crewmate, or yourself solo. Earned and sold, offered at death, one per player per band.
- **Hand skins** in the viewmodel's slots, and **lift objects** for your hook. No stats.
- **Private servers:** 70% share [PEP §2]; co-play feeds ranking [OGE §4]. Set the price once; changing it cancels subscriptions [OGE §6].
- **Later:** a season track once D7 holds [OGE §6]. **Never sold:** fire keys, tools, trophies, Log pages, depth.

### Audience and rating

16 to 24 friend groups first. New games reach 16+ only; the under-16 evaluation (ID, 2FA, a refundable fee, 250 highly engaged age-checked plays in 60 days) opens ages 9 to 15 [PEP §6]. Moderate at most, never Restricted. R15-only for the US 18+ rate, 42% more on adult US spend [PEP §1], though withholding can cancel it for a non-US owner without a treaty [PEP §7]. Mobile: one context button, a hold ring, glance-back, a brightness check.

## 4. What changes from v0.2, and why

| v0.2 | v0.3 | Why |
|---|---|---|
| Door timing is a hypothesis; no clock | The Close, contested; the floor wakes up | A bare wait goes flat, and creeping was safe |
| 3 to 5 min quiet intro | 3 min, a sign by 3:00 | Bounce counts exits at 60 to 180 s [OGE §4] |
| 20 to 30 min between saves | 16 min runs; every close banks | A wipe must not erase a session |
| No progression yet | Depth, Log, trophies, fares, Daily Drop | Median D7 is 1.6% [OGE §1]; ranking reads play days to D28 [OGE §4] |
| Who the lift waits for is open | It waits; leaving takes a vote | Stops griefing |
| The fare retired | The fare is the revive currency | Earnable, sellable, on theme |
| Four threat ideas; cars as dressing | Passenger added, Leak deferred; cars as threats and the peak | Something must reach the doorway; the lift was built for a car |
| Four bands, grid generator | One band, authored layouts | Scope; updates bring explore spikes [OGE §4] |
| "Stygian Drop" | Don't Miss the Elevator | "Drop" reads as dropper; Stygian spoils the reveal |
| Story undecided | Truth written; "Your shift" | Clues must agree for theory videos |
| D1 25%, CCU 30 | Recalibrated in section 5 | 25% beats Roblox's top-10% line, 18.73% [OGE §1] |

**What stays:** first person and the grafts; 1 to 4 co-op, solo viable; the refuge rule; no weapons; authored kits; no early "hell"; checkpoints; few readable threats; the hands question; the baseline rule; rare care; the big car; section 13; analytics and seeds.

## 5. The cheapest test: M1, "The Close"

**About 45 hours, at up to 10 h/week in October and November [PLAN].**

- **Built:** door feedback on the existing rig (edge strip, landing call, the dark empty car); the authored first stop; stops 2 and 3 on the P3 kit (a key; a timed stop with a crate); the Passenger; the clock; downed and revive; basic mobile controls; an end card; analytics.
- **Cut:** the stop assembler, other threats, meta, store, Daily Drop, public lifts, Long Stay, the two buttons.
- **How:** six moderated outside players (two groups, two solos), then about $100 of ads for 5,000 to 14,000 plays [OGE §5], which do not affect ranking [OGE §4]. It needs the owner's OK to spend and an age-checked account [PEP §6].

| Measure | Pass | Fail |
|---|---|---|
| Testers who mention the doors or the doorway, unprompted | 4 of 6 | 2 or fewer |
| Groups who ride again unasked | 2 of 3 | none |
| Ad players still in at 3:00 | 60%+ | under 40% |
| Median session | 7+ min | under 4 min |
| Press "Ride again" | 25%+ | under 10% |

Between the lines: one 10-hour fix and a retest. Fail: the hours go to other prototypes [PLAN]. The 3:00 and replay bars are mine; no public bounce benchmark exists [OGE §4]. Record D1 without gating on it. Run some tests with the Passenger off: if players act the same, the doors alone are not the hook (critique).

**Later gates**

| Gate | Pass | Stop |
|---|---|---|
| M2 ads: D1 | 12%+, the similar-games median and PLAN's bar; 18.7% is top 10% [OGE §1] | under 10% after one fix |
| M2 ads: median session | 15+ min; 19+ min sessions get double-digit D1 [OGE §1] | under 10 min |
| Soft launch: D7 | 3%+, twice the median [OGE §1] | under 1.6% |
| 4 weeks live | 30+ average CCU: survival, not a business. $3,000 a month needs 300 to 600 [OGE §1, §2] | under 30 after the first big update |

Move contract hours to the game only after two DevEx cycles of cash [PLAN].

## 6. Scope and timeline

| Milestone | Hours | When | Contents |
|---|---|---|---|
| M1 The Close | 45 | Oct to Nov 2026 | As above |
| M2 One band | 120 | Feb to Apr 2027, 12 h/week, after the contract floor [PLAN] | Stop rolls, Headlights, Attendant, two buttons, banking, Log, trophies, fares, Long Stay, Daily Drop, public lift. $150 of ads; the D1 gate |
| M3 Launch | 95 | May to Jun 2027 | Occupant, store, mobile, audio and light, ticket trail, care beats, icon and thumbnails, soft launch, Standout Games nomination [OGE §3] |
| Updates | 10 h/week | Jul 2027 on | A situation card a week; the Service band and the Leak first |

**Total:** about 260 hours (faithful pass 220, v0.2 360, Long Stay 550 to 600, a year at 12 h/week). Art for the icon, thumbnails and sound: about $500 to $1,500, as the lift, hands and cars exist; a polished launch runs $2k to $8k [OGE §7]. Launch lands near month 9, so M1 and M2 are two of the plan's 3 to 4 prototype tests [PLAN].

**Cut if late, in order:** the Occupant; the endless levels; lift objects; care rules (keep three scripted beats); trophy variants. **Never cut:** the Close, the clock, the Passenger, the first 3 minutes, banking, the Daily Drop, analytics, R15.

## 7. Decisions for the owner

1. **Core: the Close, or Long Stay's car recovery?** The Close. Long Stay collects better but costs over twice the hours.
2. **Run M1 now, with these gates and about $100 of ads?** Yes. Hold M2 until the contract floor.
3. **Public title "Don't Miss the Elevator", with Stygian kept for the bottom?** Yes, after a Roblox search check.
4. **The lift waits for everyone, leaving takes a vote, and only timed stops leave alone?** Yes.
5. **Approve the ending, "Your shift", now?** Yes, on one private page before M2, so every clue agrees.

## 8. Credits

| From | Ideas |
|---|---|
| v0.2 (owner) | Refuge rule, care, hands question, threat rules and the four original threats, bands, section 13 |
| Market lens | Plain title, Stygian for the bottom, icon, thumbnails, 3-minute rules, watchable deaths, audience, ad sizing, gates |
| Design critique | The clock, banking, two buttons, fare as revive, the vote, Hold, Watch, Operator, care rules, service log, trophies, Deep Shift, D7 gate, pillars |
| Faithful pass | The Close, fire key, hook line, Passenger, first 3 minutes, Long Stay peak, lore you hold, the ending, authored layouts |
| Bold pass | Desire over errands, the daily named find, a car in the lift, Saturday Blackout |
| This merge | Endless levels, Stygian on the maker's plate, scorecard, M1 bars, timeline |
