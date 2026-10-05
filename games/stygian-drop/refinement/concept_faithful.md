# Stygian Drop: concept, faithful refinement

*By claude, 5 October 2026. Idea work on design doc v0.2 (`source/STYGIAN_DROP.md`).*

*Citations: OGE is `research_notes/Roblox scripter income strategies/own_games_economics.md`, PEP is `platform_economics_payouts.md` in the same folder. "(OGE 4)" means section 4.*

## 0. What stays

All seven Decided items in section 11 stay as written: first person with the graft viewmodel; 1 to 4 co-op, solo viable; the lift is the refuge and nothing enters it while closed; no weapons; procedural situations on authored kits, key floors hand-built; a plausible start, no early "hell"; checkpoint floors per band. Section 13's money rules stay too.

## 1. Hook and pitch

**Hook:** The lift is safe. The four seconds its doors take to close are not.

**Pitch:** Stygian Drop is first-person co-op horror for 1 to 4 players: a vehicle lift takes your crew down through a car park that goes too deep, and at each stop you step out, do one thing with your hands, and get back before something notices. The lift is your only refuge, but its doors are real machinery that close slowly and reopen for anything in the beam: a friend, the nose of a car, or something you cannot see. You never fight; you learn what each thing wants, decide who holds the doors, and follow the person who went down before you.

## 2. The signature mechanic: the Close

**Every stop ends at a real lift door that takes four seconds to shut, reopens for anything in its beam, and can only be forced by a hand held on the panel.** Reaching the lift is half the escape. The close is the other half.

- **Slow.** About 3 seconds to open and 4 to close, the targets Lift 04 was built to (`elevator_blender_prompt.md` 5.2).
- **The beam.** Anything in the doorway reopens them: a player, a dropped crate, a bumper, an arm. A red strip on the door edge shows where the beam is broken.
- **The nudge.** On the third reopen in one close, a buzzer sounds and the doors close at half speed, whatever is in the beam. They push players in and threats out.
- **The hands.** OPEN and CLOSE sit beside the doors. Each press is a reach of the graft hand, so whoever closes them stands nearest the floor.
- **The empty lift.** When everyone is out, the doors shut and the lift waits, dark. The landing call button brings them back slowly, your back to the floor. On a Power stop it is dead until the breaker is fixed.
- **The fire key.** A rare find, never sold. Turn it and hold CLOSE for the full four seconds: the beam is ignored. Let go and the doors reopen. You face the panel, back to whatever you are shutting out.

**Why it is ours.** Roblox elevator games close their doors on a timer, and I know of no Roblox horror game that makes the exit door a machine you have to manage (unverified). Here the safe room has a slow, honest door, so the scariest place in the game is the line in front of it.

**Co-op and clips.** Holding the doors needs no chat, which now requires an age check (OGE 4): you stand in the beam for a friend. Every "hold the door!" is a clip, and Roblox's Moments now launch players straight from short videos (OGE 4).

**What it fixes.** v0.2 calls door timing a hypothesis. A bare wait can go flat; a contested doorway does not. Keep the oversized lift car: its depth keeps the back wall out of the Passenger's reach.

## 3. Run structure and loops

### The run

One run is one band: nine stops and a checkpoint, about 27 minutes. GameAnalytics ties 19+ minute sessions to double-digit D1 (OGE 1), and two runs about fill the 60 daily minutes that discovery counts (OGE 4).

| Segment | Length |
|---|---|
| P1: board the lift | 45 s |
| Stop 1, P3: authored and quiet (section 5) | 2 min |
| Stops 2 to 9: procedural, about 2.5 min each with the descent | 20 min |
| Stop 10, **Long Stay**: checkpoint and peak | 4 min |

**Long Stay** is a vast level whose call panel reads VEHICLES ONLY. The crew hotwires the person's car (both hands under the dash) and drives it to the lift while every parked car creeps when unwatched. Park it fully inside, or the bumper holds the doors open. The game's best clip, and the only place you drive.

### The stop, moment to moment

1. **Read the landing:** level on the display, side on the hall lantern, purpose on the call panel.
2. **Step out,** torch on or off, maybe leaving a doorman in the lift.
3. **Commit your hands:** a 2 to 6 second task that blocks your view or your torch.
4. **Greed:** one optional thing is always in sight.
5. **Get back. The Close.**
6. **Descend,** 20 to 30 seconds: count, swap batteries, spot what changed in the lift.

### What changes from stop to stop

| Roll | Read from | Launch options |
|---|---|---|
| Purpose | The landing call panel | **Lit:** nothing needed. **Power:** fix the breaker. **Key:** in a pay station or a car. **Fare:** pay with a ticket found here. **Load:** carry something bulky aboard |
| Condition | Landing lights, the display | **Dark:** unlit landing. **Timed:** a countdown, then the lift goes, whoever is outside. **Alarm:** a siren hides the warning sounds. **Rear:** the other doors open |
| Threat | Signs you learn | None, or one from the band |

Bulky items are one purpose in five, not the centre.

### Death and the crew

- **Downed:** you crawl until a teammate revives you: both hands, 4 seconds, back to everything else.
- **Left behind:** if the lift goes without you, you watch through its CCTV dome until someone spends a **token** at the next stop's panel. Then you are waiting on the landing when the doors open.
- **Solo:** downed ends the run, unless you spend a token.
- **Everyone down:** back to P1, checkpoints kept. A crew can start from any member's checkpoint, so veterans can bring friends deep.

The lift leaves only when someone inside closes the doors, or on Timed stops. It waits for everyone. The threats do not.

### Between runs

- **Ticket book:** the person's parking tickets, about 30 per band.
- **Field notes:** a page per threat in the person's handwriting, filled in as you survive it.
- **Your lift:** one personal object rides along each run, and your best depth is tally-marked by the panel.
- **The Daily Drop:** one shared seed a day, a depth board, a token streak. Seeds are already planned (v0.2 section 12), and it feeds the D2 to D7 play days that ranking counts (OGE 4).

## 4. Threats

At most one per stop, never inside the lift, never killed. One humanoid rig in three costumes, plus the cars and a water shape. Pace scales with crew size.

| Threat | Behaviour | Counterplay | The clip |
|---|---|---|---|
| **The Passenger** (new) | Waits facing a wall, then follows the last player back at walking pace. It never crosses the sill: it stands in the beam and reaches one arm in | Come back early and together. Otherwise wait out the nudge at the back wall, or use a fire key within its reach | The crew pressed to the back pads as the buzzer sounds and the doors close on its arm |
| **Headlights** (refined) | One parked car with its lights on. It creeps toward the nearest player, a bay at a time, whenever nobody is looking | One watches, one works. Solo, work in bursts and look back | "It was a bay closer every time I turned round." Then the lights fill the screen |
| **The Attendant** (refined) | Walks between pay stations. Goes toward light: torches, dome lights, a lift held open | Torch off, stand still. Never hold the doors longer than you must | Torches off, everyone frozen, and it walks between you close enough to touch |
| **The Occupant** (refined) | Moves between parked cars when no one is near. Its car has one small change: window down, seat back, dome light on. Open that car and you are down | Remember the cars. Check one before you reach into its glove box | He opens the door for a battery and it is in the back seat |
| **The Leak** (kept) | Something under the water in flooded bays. Goes to the latest splash; sprinting splashes | Walk, cross on car roofs, or throw a battery to splash elsewhere | The crew hopping roof to roof as a ripple circles below |

Launch with the first four. The Leak comes with flooding in the Service band.

## 5. The first 3 minutes

A first run skips the public lobby: only you and your friends.

| Time | Beat |
|---|---|
| 0:00 | Fade in on the P1 landing. Car 04 arrives: the chime, then car and landing doors telescope open together. The best thing the game owns is the first thing you see. No title screen |
| 0:10 | Walk in. Crossing the doorway lights the edge strip red at your height. The hand reaches the panel: P3, CLOSE |
| 0:25 | Descent. The hum, P2, P3. A big, empty lift and a plate: RATED LOAD 1 VEHICLE |
| 0:45 | The doors open on an ordinary, lit car park. A windscreen note: "Breaker by the ramp. Walk." You step out and the doors close behind you, as lift doors do. The call button is dead |
| 1:00 | The walk: concrete, drains, cars at odd angles, one dusty. Nothing happens. This is v0.2's quiet, cut to 40 seconds |
| 1:40 | The breaker: both hands in the cabinet, the view narrowed to the switch. Behind you, a car's dome light clicks on. The call button lights |
| 2:05 | The walk back past the lit car. A coat on the passenger seat. Nothing happens |
| 2:25 | Call the lift, step in, CLOSE. Halfway, the doors reopen. One red segment on the strip, at knee height. Nobody is there. Again. On the third try the buzzer sounds and the doors nudge shut on whatever is standing there |
| 2:55 | Descent to P4. Nothing is confirmed |

Stop 2 is seeded with the Passenger, the first thing that can hurt you, to teach the rule that matters: get back, then get the doors shut.

**The tension, resolved.** Roblox now ranks games partly on first-play bounce, exits in about the first 60 to 180 seconds (OGE 4). v0.2 wants a quiet first stop. Both survive because **the floor stays quiet and the doorway does not.** Nothing on the floor flickers, jumps or hurts you, so the baseline gets built, and the lift carries the first minute. The hook lands at about 2:40 and is no jump scare: the one thing the player trusts reopens for something they cannot see. The dome light is a free lesson too: later, it marks the Occupant.

## 6. The long mystery

**Lore is something you hold.** Every clue is an object turned over in the graft hands, with one handwritten line at most. No voice-over, cutscenes or log menus.

- **Tickets:** the person's parking tickets, stamped with each level and the same time on every floor, 23:58.
- **Their car:** same plate on most floors, a little different each time (the coat gone, one glove on the dash, keys in the ignition). At Long Stay you drive it into the lift.
- **Field notes** in their hand: "It doesn't hear. It sees light." "It only wants a lift."
- **The inspection certificate** in the lift: one more line readable per band cleared. Late on, its signature matches the tickets.
- **The care,** at most once a band, never explained: the doors wait for the last runner, a dropped item is in the lift at the next stop, the button you reach for is already lit. The edge strip makes these read as choices, not bugs: when the doors wait, nothing shows in the beam.

**What is at the bottom.** The lift's machine room. A chair faces a wall of small monitors, one per landing; on one, a new crew is stepping into Car 04 at P1. The person you followed is in the chair, hands on the controls, arms ash gray like yours. They have been driving your lift the whole way down: every door that waited, every light already on. The note on the desk says "Your shift." You sit. There is one button, HOLD. On the monitor, someone is running for the doors.

**Why players will talk.** It pays off the doc's opening: "The lift always comes back for you. That is the part you should worry about." It explains every kindness in hindsight. It turns the grafts from a skin into a uniform: you were not following them, you were being delivered. It answers who, not what, so the place stays a mystery.

## 7. Monetization

Section 13 holds: no immunity for sale, everything buyable is earnable except cosmetics, no paid random items.

- **Tokens (the revive).** Call back a crewmate, or yourself solo. Earned from the Daily Drop streak, band clears and rare finds; sold in packs of 1, 5 and 12; capped at one call-back per player per band. Roblox's guidance cites Evade's revives, and Dead Rails sells Bonds for them (OGE 6).
- **Hands.** Glove and arm skins, sold or earned by feats, mixed across the viewmodel's separate slots. In first person your hands are all you see of yourself. They are the avatar.
- **Lift objects.** Things that ride in the lift for the run. Comfort only, no stats.
- **Private servers** for friend crews: a 70% share (PEP 2), and co-play days feed discovery (OGE 4).
- **Never sold:** fire keys, faster doors, anything that calms a threat.
- **R15 only, from day one.** It qualifies age-verified US adult spend for the $0.0054 DevEx rate, 42% above standard (PEP 1). US over-18s spend about 50% more (OGE 4), and new games reach only 16+ players until they pass a 250-play evaluation (PEP 6). Horror suits that audience.

The target: $3,000 a month is about 789,000 Earned Robux at the standard rate (PEP 4), or roughly 300 to 600 average CCU at $5 to $10 per CCU-month, the band for competent co-op survival games (OGE 1).

## 8. Cut to ship sooner

- **One band at launch,** Parking to Long Stay. Service is the first big update and an "explore" spike (OGE 4); Offices and Underneath later.
- **No grid generator.** Six authored layouts from the P3 kit, mirrored to twelve. The situation rolls do the work.
- **Six hand clips:** press, cabinet, glove box, carry, revive, inspect.
- **The lobby is a P1 landing.** No hall.
- **Drive on Long Stay only, in seat view.** The chase view breaks first person. Threat cars slide on rails, not the drivetrain.
- **A small store:** tokens, six skins, six lift objects, private servers. A season track waits until D7 holds.

My estimate: about 220 hours to launch, not v0.2's 360. After M2, about $100 of Ads Manager buys roughly 5,000 to 14,000 plays to read bounce and D1 (OGE 5).

Fix one gate: D1 above 25% beats even Roblox's own top-10% example, 18.73% (OGE 1). Pass at 15%, stop below 10%.
