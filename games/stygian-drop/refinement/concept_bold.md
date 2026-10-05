# Bold pass: three variants and a pick

*Idea work only, 5 October 2026. Working titles. "The lift" is Vehicle Lift 04; "cars" are the 19 vintage cars.*

Sources: **[econ]** `research_notes/Roblox scripter income strategies/own_games_economics.md`; **[pay]** `research_notes/Roblox scripter income strategies/platform_economics_payouts.md`; **[v0.2]** `source/STYGIAN_DROP.md`; **[brief]** `source/elevator_blender_prompt.md`. Unsourced claims about other games are marked (unverified).

## In short

- **Pick: Long Stay.** Co-op for 1 to 4. Ride the lift down, find an abandoned car worth taking, get it running with your hands, drive it into the lift, then choose: deeper or up. Your finds fill a row of bays the whole server can see.
- It keeps v0.2's core and adds a reason to leave the lift, a job for the cars, and a collection that brings players back. About 200 more hours than v0.2; ships in 3 to 3.5 months.

## What v0.2 leaves on the table

- **The lift was built to carry cars and never carries one.** The 19 drivable cars are dressing.
- **"Why leave the lift?" gets errands:** activity, not desire, as v0.2 admits [v0.2 §4].
- **The opening is slow.** 3 to 5 minutes whose one event is a car light [v0.2 §10]. Discovery penalises exits in the first 60 to 180 seconds [econ §4].
- **No meta loop.** M4 says "progression" with no design [v0.2 §14], while ranking counts play days across 28 days [econ §4].

## 1. Three variants

### A. Long Stay: co-op extraction and car collecting

- **Hook:** Every car down here was left by someone who never came back. Start one. Get it in the lift.
- **Core loop:** Lift down one stop → find a car worth taking → get it running by hand → drive it into the lift → deeper or up → restore, show or sell → go deeper.
- **Signature mechanic:** *The start-up.* Cars are dead until you fix them: the key from the booth, a jump pack under a raised bonnet, a jerry can, the choke, the crank. Every crank is loud. Then the doors: a bumper in the light curtain reopens them.
- **Why it spreads:** Roles for friends: one cranks, one watches, one waves the car in, one holds the doors. Invited friends count as intentional co-play, a ranking signal [econ §4]. Every run makes a clip ("it won't start", "the bumper is in the doors"), and Moments turn clips into direct launches [econ §4]. Solo works, so it survives low CCU.
- **Precedent:** Dead Rails, a co-op train journey (unverified) with about 18-minute sessions and paid revives [econ §3].
- **Session:** Runs of 15 to 25 minutes, two or three per session.
- **Monetization:** Car and hand cosmetics, bays, one revive per run, private servers (section 2).
- **Scope:** About 550 to 600 hours, plus $3k to $6k of contracted art.
- **Biggest risk:** A car is armour. If players can drive anywhere, the horror dies. So cars start dead, are loud and lit, and you drive only the last minute of a stop.

### B. Last Car Down: competitive elimination race

- **Hook:** Eight cars race down. The lift holds three.
- **Core loop:** Race down a spiral section to the lift. The first three cars fully inside ride down. The rest are left as the lights go out, hunted for 60 seconds. Reach the stairwell and you start the next round at the back; get caught and you are out. Last driver wins.
- **Signature mechanic:** The finish line can be held. A bumper in the light curtain keeps the doors open, so the leader can block to save a friend while everyone waits in the dark.
- **Why it spreads:** Photo finishes at the doors, betrayals, an instantly readable thumbnail. Knocked-out players return as parked cars that move when unwatched, so nobody sits idle.
- **Session:** Rounds of 2 to 3 minutes, matches of about 12.
- **Monetization:** Car skins, horns, emotes, a season pass. Equal stats.
- **Scope:** About 400 to 450 hours (round flow, AI drivers to fill servers, anti-cheat), plus $2k to $4k of art.
- **Biggest risk:** It needs a crowd, which solo developers are told to avoid [econ §7]. PvP on client-owned car physics invites exploiters, a known burnout cause [econ §9]. The hands shrink to the wheel and most of the horror goes.

### C. Landing Calls: night-shift doorman horror

- **Hook:** You run the lift on the night shift. Someone waits at every landing. Not all of them should come up.
- **Core loop:** A call lights the panel → ride to the landing → check before opening: the camera, the ticket pushed through the slot, their car, the level's posted rules → open, or leave them → survive the shift.
- **Signature mechanic:** The doors are your decision. Let the wrong one in and it rides with you.
- **Why it spreads:** Impostor reveals suit streamers; doorman-checking games have gone viral on PC (unverified).
- **Session:** Shifts of 10 to 12 minutes. Five story nights, then an endless shift.
- **Monetization:** Weak: cosmetics, extra nights.
- **Scope:** About 250 to 300 hours, plus $1.5k to $3k of art. Cars arrive with visitors; sometimes you drive one in.
- **Biggest risk:** Finite content and little co-play. A fast hit or nothing.

### Side by side

| | A. Long Stay | B. Last Car Down | C. Landing Calls |
|---|---|---|---|
| Players | 1 to 4, co-op | 6 to 8, competitive | 1 to 2 |
| Driving | The getaway | Everything | Rare |
| Structure | Runs plus a lasting collection | Rounds | Story nights |
| DevEx per average CCU per month (my estimate) | $6 to $12 | $3 to $6 | $1 to $3 |
| Average CCU for $3k a month [econ §2] | 250 to 500 | 500 to 1,000 | 1,000 to 3,000 |
| Build, full time | 3 to 3.5 months | About 2.5 months | About 1.5 months |

Estimates use [econ §1]'s bands: $5 to $10 for co-op survival with progression, $9 to $12 at platform average, under $2 for hangouts and very young audiences.

## 2. The pick: Long Stay

A real car-park sign with a second meaning. Check the name is free.

### The first 3 minutes

A first-time player skips the hub and loads straight into the lift, alone or with friends.

1. **0:00** Inside the lift, doors shut. The hum. Only P1 is lit.
2. **0:10** Press P1. The doors open on an ordinary, lit car park. A note on the call panel: *"Keys are in the booth. Don't use the horn. M."*
3. **0:40** The booth's key board holds bay tags. Match one to the bay number beside the car under a dust sheet.
4. **1:05** Pull off the sheet. Turn the key. The starter grinds, slows and dies.
5. **1:20** Fetch the jump pack from the fire point. Raise the bonnet (the level vanishes behind it) and clamp the leads with both hands.
6. **1:45** Behind the bonnet, the far row of tubes goes out. Then the next.
7. **1:55** Bonnet down. Something stands where the light ends. It does not come closer.
8. **2:05** Crank. Crank. It catches and the headlights come on. The figure turns toward them.
9. **2:20** Drive into the lift. Stop short and the bumper trips the light curtain: the doors start, then reopen. Pull forward. The doors take four seconds [brief §5.2]. Through the gap, the figure walks toward the headlights.
10. **2:45** The panel offers UP and P2. A note on the seat: *"Take it up. The deeper ones are better."*
11. **3:00** The doors open on Level 0, the hub. The coupe rolls into your first bay beside other players' rows. Ledger: 1 of 19.

Nothing can hurt them yet, as v0.2 requires, but they get a chase, a near miss and a prize.

### The run

- **Load out:** three tools each; bulky ones (jerry can, jump pack) take both hands.
- **Each stop** uses v0.2's rolls: layout, purpose, condition, threat [v0.2 §7]. The purpose is always one question: is any car here worth it? 4 to 8 parked cars. Most are locked, wrecked or worthless; one or two are good; one may be occupied.
- **Posted rules** hang at every landing: "ENGINES OFF ON THIS LEVEL", "HEADLIGHTS ON", "NO REVERSING". Reading them is the knowledge skill. Rules are data, so variety is cheap.
- **The lift is rated for three cars** (tune to real sizes). A second plate says four. It is right once.
- **Up** banks everything aboard. **Down** means rarer cars and worse threats. If the whole party goes down, the cars aboard are lost; they may turn up deeper, marked *Repossessed*.
- **Lift care, rare:** the doors wait a beat for a runner. A car you abandoned two stops ago is parked inside when the doors open.
- **Ramps only connect half-levels.** Below that, every ramp loops back. Only the lift goes down.
- **Checkpoint floors** end each band (P10, P20) with a peak encounter. Clear one to start from there.

### Threats

Few, readable, unexplained, and they respect the closed lift [v0.2 §8].

| Threat | Behaviour | Teaches |
|---|---|---|
| **The Attendant** (v0.2) | Patrols between pay stations. Follows light, so headlights draw it | Drive dark, or drive fast |
| **The Warden** (new) | Enforces the posted rules; break one and you hear its ticket printer. Clamps any car left alone | Read the signs |
| **The Occupant** (v0.2) | Hides in a car. Tells: a clean bonnet in a dusty row, a fogged windscreen, a warm engine. Start it and the doors lock until a teammate opens one | Compare before you commit |
| **The Tow** (new, peak) | On checkpoint floors, a driverless tow truck hooks the last car at the doors. One player unhooks it by hand | Teamwork at the doors |

The Leak (flooded bays, follows splashing) comes in the first update.

### The meta loop

- **Level 0** is the shared hub. Each player has a row of bays where every car they bring up parks, condition and finish on show.
- **The Ledger** logs 19 models in four conditions (Wreck, Dusty, Clean, Mint), plus rare finishes found by depth: Lit, Flooded, Ashen (grey with a bronze seam, like your arms), Repossessed. Over a hundred entries from cars that already exist. Finishes are found, never sold.
- **Restore** a car over real hours, or **sell** it through the slot in the Buyer's booth for fares. Nobody has seen the Buyer. Fares buy tools, bays and key cards for deeper starts.
- **Glovebox notes** carry the trail of whoever went down before you [v0.2 §4].
- **Products:** paints, plates, wheels, glove and arm skins [v0.2 §13], extra bays, a 2x fares pass, one revive per run, restoration speed-ups, private servers, and later a season pass once D7 holds [econ §6]. Nothing changes a threat or the lift. No paid random items.

### Why come back tomorrow

- Your restorations finished overnight.
- **Lost and Found:** each day one named car and finish is reported on a stated level, the same for everyone.
- A first-run bonus and a streak.
- **Saturday Blackout:** every level dark, finishes twice as common. Traffic usually peaks on Saturday [econ §4].
- An unfinished Ledger row, and the next glovebox note.

## 3. The three questions

### The cars, and the spiral

Use them as the payoff, not the medium. A whole game of driving down a spiral (variant B) makes the car a second refuge, removes any reason to take the lift, and repeats one corner for twenty minutes. In Long Stay the lift takes you down and you drive yourself back. The spiral becomes a set piece: the lift lands you at the top of one, the find is two half-levels below, and you drive it back up with something behind you. That is the game's best clip, and the chase view already exists.

Tech: cars ride anchored while the lift moves, as saved cars already park. The choke, crank and push-starts are server states on top of the drivetrain, not new physics.

### A broad 9+/13+ audience or US 18+

- New games launch to an age-checked 16+ audience. Reaching under-16s takes verification, 2FA, a subscription or a refundable 1,000-Robux fee, and 250 highly engaged age-checked plays within 60 days [pay §6].
- The US 18+ rate is $0.0054 against $0.0038 (42% more), only on purchases by age-verified US adults in R15-compliant games [pay §1]. If 25% of spend qualifies, $3k needs 714,286 Earned Robux instead of 789,474 [pay §4]: about 10% less, not a new business.
- US adults spend about 50% more than under-18s [econ §4].

**Decision:** R15-only from day one. It is free, and any R6 option disqualifies the game [pay §1]. Write for 13+ taste: bloodless and scary, aiming at Moderate (my reading of the questionnaire; confirm it). Launch to 16+, then pass the under-16 evaluation so the 9 to 15 Select tier, which sees up to Moderate, can find it [pay §6]. Avoid Restricted: 18+ only, and unplayable in places like Korea, Saudi Arabia and Türkiye [pay §6]. Co-op runs on pings ("car here", "key", "it's coming", "close the doors"), so players without chat can still play together.

### Shipping in 3 to 4 months

Several 2025 hits went from creation to virality in about 1 to 3 months [econ §7]. Three months works here only because the lift, the basement, the cars, the hands and the data layer already exist. About 550 to 600 new hours:

| Month | Build | Gate |
|---|---|---|
| 1 | Authored first stop, one generated stop, the start-up, cars in the lift, the Attendant | Feel check [v0.2 §14]: 5 outside players mention the start-up or the doors unprompted |
| 2 | Stop assembler, Warden, Occupant, Level 0 bays, Ledger, fares | Fun check: 5 outside players start a second run |
| 3 | Checkpoint floor and the Tow, products, UI art, icon and thumbnails, analytics; $50 to $150 of ads for 5k to 20k test plays [econ §5] | Soft launch |

If late, cut restoration, the second band and the Occupant; ship the Parking band with 12 cars. Then update weekly (a car, a finish, a rule set), with the backrooms band as the first big update, since updates trigger "explore" spikes [econ §4]. Art fits the $2k to $8k range for a polished launch [econ §7].

## 4. Does it beat v0.2?

Yes, for a game meant to earn $3,000 a month.

- **It answers v0.2's open problem.** You leave the lift because you want that car, not because a breaker tripped.
- **It uses everything built.** The vehicle lift finally carries vehicles. The door-timing hypothesis [v0.2 §11] no longer carries the game alone: the doors matter because a car must fit through them.
- **It retains and earns.** A visible collection, overnight restorations and a daily shared find feed the play-day signals [econ §4]. At $6 to $12 per average CCU, $3k needs 250 to 500 average CCU [econ §2], about 8,000 to 16,000 DAU at 45 minutes a day (formula in [econ §1]).
- **It spreads.** Every run makes a clip and the roles pull friends in. Original in name, art and loop, it avoids the near-duplicate filter and can be nominated for Standout Games [econ §3].
- **It keeps the soul:** first person, the grafts, the lift as an untrustworthy refuge, no weapons, learnable threats, an unexplained place, bands and checkpoints.

v0.2 is better at purer atmosphere, a smaller build (360 hours, M1 to M4 [v0.2 §14]) and lower physics risk. If the month-1 feel check fails on the start-up, fall back to v0.2's on-foot stops and keep the car collection as the meta. That still beats v0.2.
