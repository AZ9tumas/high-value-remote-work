# Stygian Drop: concept, faithful refinement

*By claude, 5 October 2026. Idea work on design doc v0.2 (`source/STYGIAN_DROP.md`). No code, Blender or Studio.*

*Citations: OGE is `research_notes/Roblox scripter income strategies/own_games_economics.md` and PEP is `platform_economics_payouts.md` in the same folder. "(OGE 4)" means section 4.*

## 0. What stays

Every item in the Decided column of section 11 stays as written:

- First person, through the graft viewmodel.
- 1 to 4 players, co-op, solo viable.
- The lift is the refuge. Nothing enters it while its doors are closed.
- No weapons. You survive by watching and moving.
- Stops are procedural situations on authored kits. Key floors are hand-built.
- The descent starts plausible. Nobody says "hell" early.
- A checkpoint floor ends each band.

Section 13's money rules stay too. Everything below works inside them.

## 1. Hook and pitch

**Hook:** The lift is safe. The four seconds its doors take to close are not.

**Pitch:** Stygian Drop is first-person co-op horror for 1 to 4 players: a vehicle lift takes your crew down through a car park that goes too deep, one stop at a time, and at each stop you step out, do one thing with your hands, and get back before something notices. The lift is your only refuge, but its doors are real machinery that close slowly and reopen for anything in the beam: a friend, the nose of a car, or something you cannot see. You never fight back; you learn what each thing wants, decide who holds the doors, and keep following the person who went down before you.

**Thumbnail:** the doors half shut, one red segment glowing on the door edge at knee height, nothing in the doorway. It shows the real game, which play-through rate rewards (OGE 4).

## 2. The signature mechanic: the Close

**Every stop ends at a real lift door that takes four seconds to shut, reopens for anything in its beam, and can only be forced by a hand held on the panel.** Reaching the lift is half the escape. The close is the other half.

- **Slow.** About 3 seconds to open and 4 to close, the targets Lift 04 was built to (`elevator_blender_prompt.md` 5.2). Nothing makes them faster.
- **The beam.** Anything in the doorway trips the light curtain and the doors reopen: a player, a dropped crate, a bumper, an arm. A strip on the door edge glows red where the beam is broken. Players learn it the first time they walk through and see their own height light up.
- **The nudge.** On the third reopen in one close (beam or OPEN button), a buzzer sounds and the doors close at half speed, whatever is in the beam. They push players in and threats out. Everyone learns to dread that buzzer, and to be glad of it.
- **The hands.** OPEN and CLOSE sit on the panel beside the doors. Each press is a reach of the graft hand, so whoever closes the doors is the person nearest the floor.
- **The empty car.** When everyone is out, the doors shut after a few seconds and the lift waits, dark. The landing call button brings them back, slowly, with your hand on the wall and your back to the floor. On a Dark stop that button is dead until someone fixes the breaker.
- **The fire key.** A rare find, never sold. Turn it, then hold CLOSE for the full four seconds and the beam is ignored. Let go and the doors reopen. You face the panel, hand committed, back to whatever you are shutting out.

**Why it is ours.** Roblox elevator games close their doors on a timer, and as far as I know no Roblox horror game makes the exit door a machine you have to manage (unverified). Most horror games end the escape at the safe room. Here the safe room has a slow, honest door, so the scariest place in the game is the line in front of it.

**What it gives co-op.** One verb everyone understands without chat, which matters now that chat needs an age check (OGE 4). Stand in the beam to hold the doors for a friend. Shout "close it" or "wait". Solo, the Close is you, the panel and whatever followed you. Every "hold the door!" is a clip, and Roblox's Moments now launch players straight from short gameplay videos (OGE 4).

**What it fixes.** v0.2 calls door timing a hypothesis. A bare wait can go flat. The Close gives the wait three inputs (beam, nudge, key) and a decision made with friends, so the M1 feel check tests something stronger than a timer. Keep the big car: its depth puts the back wall out of the Passenger's reach (section 4).

**The cars obey the same rule.** A car is a big object in the beam. Getting one into the lift means getting all of it past the line.

## 3. Run structure and loops

### The run

A run is one band: nine stops and a checkpoint, about 27 minutes. That sits in the 19+ minute sessions GameAnalytics ties to double-digit D1 (OGE 1). Two runs about fill the 60 minutes per player per day that discovery counts (OGE 4).

| Segment | Length |
|---|---|
| P1: the lift arrives, the crew gets in, the doors close | 45 s |
| Stop 1, P3: authored and quiet (section 5) | 2 min |
| Stops 2 to 9: procedural, about 2.5 minutes each with the descent | 20 min |
| Stop 10, **Long Stay**: checkpoint and peak | 4 min |

**Long Stay** is a vast long-stay level whose call panel reads VEHICLES ONLY. The crew finds the person's car, hotwires it with both hands under the dash, and drives it to the lift while every parked car on the level creeps whenever nobody is looking at it. Then they must park it fully inside, or the bumper holds the doors open. The car rides down with you. It is the best clip in the game, and the only place you drive.

### The stop, moment to moment

1. **Read the landing.** The display gives the level. The hall lantern gives the side. As the doors part, the landing call panel says what the stop wants.
2. **Step out.** Torch on or off. All together, or leave a doorman in the car.
3. **Commit your hands.** Every task is a 2 to 6 second hand action that blocks your view or your torch: a breaker cabinet, a glove box, a pay station, a crate in both arms.
4. **Greed.** One optional thing is always in sight: a glove box ajar, batteries past the ramp, a ticket on a pillar.
5. **Get back. The Close.**
6. **Descend** for 20 to 30 seconds. Count, swap batteries, read what you found, look for what changed in the car.

### What changes from stop to stop

| Roll | How players read it | Launch options |
|---|---|---|
| Purpose | The landing call panel | **Lit:** nothing needed; leaving is a choice. **Dark:** find the breaker. **Key:** a key is in a pay station or a car. **Fare:** feed the pay station the ticket found on this level. **Load:** carry something bulky aboard, two hands, no torch |
| Condition | Landing lights and the display | **Dark:** the landing is unlit. **Timed:** the display counts down and at zero the lift goes, whoever is outside. **Alarm:** a siren drowns the sounds that warn you. **Rear:** the other doors open |
| Threat | Signs you learn | None, or one from the band |

After launch, add the **Offer**: sometimes two buttons light on the way down, a short way or a richer one.

Bulky items become one purpose in five, not the centre of every task. Carrying alone is dull solo, and the hands commit you in every task anyway.

### Death and the crew

- **Downed:** you fall and crawl. A teammate revives you with both hands for 4 seconds, facing you, back to everything else.
- **Left behind:** if the lift goes without you, you watch the crew through the CCTV dome in the car's corner. At the next stop anyone can spend a **token** at the panel, and you are standing on the landing when the doors open.
- **Solo:** downed ends the run, unless you spend a token and wake on the car floor as the doors open at the next stop.
- **Everyone down:** back to P1. Checkpoints are kept. A crew can start from any checkpoint one member has reached, so veterans can bring friends deep.

The lift only goes when someone inside closes the doors, except on Timed stops, which say so. That answers v0.2's open question: the lift waits for everyone. The threats do not.

### Between runs

- **Ticket book.** The person's parking tickets, about 30 per band, some only on rare stops.
- **Field notes.** Each threat's page, in the person's handwriting, fills in as you see it, survive it and master it.
- **Your car.** Bring one personal object per run (a radio, a thermos, a desk fan). It rides in the lift and your crew sees it. Your deepest level is scratched by the panel as tally marks.
- **Hands.** Glove and arm skins, some earned by feats: a band without the torch, ten clean closes.
- **The Daily Drop.** One shared seed a day for every crew, with a depth board and a token streak. Seeded floors are already planned (v0.2 section 12), so it is cheap, and it feeds the D2 to D7 play days that ranking counts (OGE 4).
- **Updates:** a layout or a threat every two weeks, a band every two months. Updates bring Roblox's "explore" spike of new players (OGE 4).

## 4. Threats

At most one per stop, never inside the car, never killed. One humanoid rig in three costumes, plus the cars and a water shape. Pace scales with crew size.

| Threat | Behaviour | Counterplay | The clip |
|---|---|---|---|
| **The Passenger** (new) | Waits on the floor, facing a wall. When the crew heads back, it follows the last player at walking pace. It never crosses the sill: it stands in the beam and reaches one arm in | Come back early and together, and the doors shut before it arrives. If not, wait out the nudge at the back of the car, or use a fire key within its reach | The crew pressed against the back pads while the buzzer sounds and the doors close on its reaching arm |
| **Headlights** (refined) | One parked car with its lights on. It creeps toward the nearest player, a bay at a time, whenever nobody is looking at it | One player watches, one works. Solo, work in short bursts and look back | "It was a bay closer every time I turned round." Then the lights fill the screen |
| **The Attendant** (refined) | Walks between pay stations. Goes toward light: torches, dome lights, and a lift held open, which spills light across the floor | Torch off, stand still. Never hold the doors longer than you must | Torches off, everyone frozen, and it walks between you close enough to touch |
| **The Occupant** (refined) | Moves between parked cars when no one is near. Its car has one small change: a window down, a seat back, the dome light on. Open that car and you are down | Remember the cars. Check one against your last look before you reach into its glove box | He opens the door for a battery and it is sitting in the back seat |
| **The Leak** (kept, Service band) | Something under the water in flooded bays. It goes to the latest splash, and sprinting splashes | Walk, cross on car roofs and dry ramps, or throw a battery to splash elsewhere | The crew hopping roof to roof while a ripple circles below |

Launch with the first four. The Leak arrives with flooding in the Service band.

## 5. The first 3 minutes

A first run skips the public lobby. It starts on its own server, with only you and any friends you brought.

| Time | Beat |
|---|---|
| 0:00 | The loading screen fades in on the P1 landing. Car 04 arrives: the chime, then car and landing doors telescope open together. The best thing the game owns is the first thing you see. No title screen |
| 0:10 | Walk in. Crossing the doorway lights the edge strip red at your height. The hand reaches the panel: P3, CLOSE. The doors take their time |
| 0:25 | Descent. The hum, P2, P3. A big, clean, empty car, and a plate: RATED LOAD 1 VEHICLE |
| 0:45 | The doors open on an ordinary, lit car park. A note on the nearest windscreen: "Breaker by the ramp. Walk." You step out, and the empty car's doors close behind you, as lift doors do. The call button beside them is dead. The goal is clear |
| 1:00 | The walk: concrete, drains, fans, cars at odd angles, one dusty. Nothing happens. This is v0.2's quiet, cut to 40 seconds |
| 1:40 | The breaker. Cabinet open, both hands in, the view narrowed to the switch. Behind you, a car's dome light clicks on. Across the level, the call button lights |
| 2:05 | The walk back, past the lit car. A coat on the passenger seat. Nothing happens |
| 2:25 | Call the lift. The doors take three seconds to open. Step in, press CLOSE. Halfway, they reopen. One red segment on the strip, at knee height. Nobody is there. Again. On the third try the buzzer sounds and the doors nudge shut on whatever is standing there |
| 2:55 | Descent to P4. Nothing is confirmed |

Stop 2 is seeded with the Passenger, the first thing that can hurt you. It teaches the one big rule: get back, then get the doors shut.

**The tension, resolved.** Roblox now scores first-play bounce, meaning exits in about the first 60 to 180 seconds (OGE 4). v0.2 wants a quiet first stop of 3 to 5 minutes. Both survive because **the floor stays quiet and the doorway does not.** Nothing on the floor flickers, jumps or hurts you, so the player still builds the baseline. The first minute is carried by the lift itself: the doors, the descent, a goal and a reason to get back. The hook lands at about 2:40, from the one thing the player already trusts. The doors reopen for something they cannot see. It is not a jump scare, and nothing comes from inside the car. The dome light is a free lesson too: later, it is how the Occupant gives itself away.

## 6. The long mystery

**Lore is something you hold.** Every clue is an object you turn over in the graft hands (the inspect clip exists), with one handwritten line at most. No voice-over, no cutscenes, no menu of logs.

- **Tickets.** The person's parking tickets. Each is stamped with its level and the same time on every floor: 23:58.
- **Their car.** Same model and plate on most floors, a little different each time: the coat on the seat, then gone; one glove on the dash; keys in the ignition. At Long Stay it is the car you drive into the lift.
- **Field notes** in their hand: "It doesn't hear. It sees light." "It only wants a lift."
- **The inspection certificate** in the car. One more line becomes readable for each band cleared. Late on, players can match its signature to the tickets.
- **The care.** At most once a band, never explained: the doors wait a beat for the last runner, something you dropped is in the car at the next stop, the button you reach for is already lit. The edge strip makes these read as choices, not bugs: when the doors wait, nothing shows in the beam.

**What is at the bottom.** The lift's machine room. A chair faces a wall of small monitors, one per landing. On one, a new crew is stepping into Car 04 at P1. The person you followed is in the chair, hands on the controls, and their arms are ash gray like yours. They have been driving your lift the whole way down: every door that waited, every light already on. The note on the desk says "Your shift." You sit. There is one button, HOLD. On the monitor, someone is running for the doors.

**Why players will talk.** It pays off the doc's opening ("The lift always comes back for you. That is the part you should worry about."). It explains every kindness in hindsight. It turns the grafts from a skin into a uniform: you were never following them, you were being delivered. It answers who, not what, so the place stays a mystery. Later, an **Operator mode** could seat players who reach the bottom in the chair during strangers' runs, with only kind, rate-limited actions. Then "is the lift looking after me, or is that a person?" has a real answer.

## 7. Monetization

Section 13's rules hold. No immunity for sale. Everything buyable is earnable, except cosmetics. No paid random items.

- **Tokens, the revive.** Call back a crewmate, or yourself when solo. Earned from the Daily Drop streak, band clears and rare glove-box finds. Sold in packs of 1, 5 and 12. Capped at one call-back per player per band. Revives are a standard Roblox consumable: Roblox's own guidance uses Evade's, and Dead Rails sells Bonds for them (OGE 6).
- **Hands.** Glove and arm skins, sold directly, mixed across the viewmodel's separate slots. In first person your hands are the only part of you that you ever see. They are the avatar.
- **Lift objects.** Things that ride in your car for the run. Comfort only, no stats.
- **Private servers** for friend crews, at a 70% share (PEP 2). Co-play days also feed discovery (OGE 4).
- **Later, once D7 holds:** a monthly free and premium cosmetic track tied to stops survived (OGE 6).
- **Never sold:** fire keys, faster doors, anything that calms a threat.
- **R15 only, from day one.** It qualifies spend by age-verified US adults for the $0.0054 DevEx rate, 42% above the standard $0.0038 (PEP 1). US players over 18 spend about 50% more (OGE 4), and horror skews older. A new game also reaches only 16+ players until it passes the 250-play evaluation for younger tiers (PEP 6). Build for that audience.

The target in numbers: $3,000 a month is about 789,000 Earned Robux at the standard rate (PEP 4), or about 300 to 600 average CCU at the $5 to $10 per CCU-month band for a competently monetized co-op survival game (OGE 1).

## 8. Cut to ship sooner

- **One band at launch:** Parking, ending at Long Stay. Service is the first big update. Offices and Underneath come later.
- **No grid generator.** Six authored layouts from the P3 kit, mirrored to twelve. The situation rolls do the work.
- **Four threats** from one rig plus the cars.
- **Six hand clips:** press, cabinet, glove box, carry, revive, inspect.
- **Revive in place.** Carrying bodies can wait.
- **Text on tickets only.** No voice, tapes or cutscenes.
- **The lobby is a P1 landing.** No hall.
- **Driving on Long Stay only, seat view only.** The chase view breaks first person. Threat cars slide on rails, not the drivetrain.
- **A small store:** tokens, six skins, six lift objects, private servers.
- **Operator mode** waits until players actually reach the bottom.

My estimate: about 220 hours to launch instead of v0.2's 360. After M2, spend about $100 on Ads Manager's Maximize Plays to read bounce and D1 on 5,000 to 14,000 plays (OGE 5).

One gate needs fixing. The soft-launch bar of D1 above 25% is higher than Roblox's own top-10% example, 18.73% (OGE 1). Pass at 15%. Stop below 10%.
