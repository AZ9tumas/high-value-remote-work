# Stygian Drop

> Working title. The elevator is **Vehicle Lift 04**, "Car 04" on its control panel. Version 0.1 of this
> document (the horde-in-the-elevator arena, the Manifest, Charon's Landing) is retired; it is in git
> history if anything needs rescuing.

A first-person co-op horror game on Roblox for 1 to 4 players. A goods lift takes you down beneath a
building, one stop at a time. At each stop you step out into a place you should not be, do what you
came for, and get back before something notices. The lift always comes back for you. That is the
part you should worry about.

---

## Contents

1. [Pitch](#1-pitch)
2. [What we have](#2-what-we-have)
3. [The lift](#3-the-lift)
4. [Why you leave the lift](#4-why-you-leave-the-lift)
5. [The stop: core loop](#5-the-stop-core-loop)
6. [Hands and items](#6-hands-and-items)
7. [Floors](#7-floors)
8. [Threats](#8-threats)
9. [The descent](#9-the-descent)
10. [The first stop](#10-the-first-stop)
11. [Decided, and still to prove](#11-decided-and-still-to-prove)
12. [Technical notes](#12-technical-notes)
13. [Monetization rules](#13-monetization-rules)
14. [Milestones and gates](#14-milestones-and-gates)
15. [Open questions](#15-open-questions)

---

## 1. Pitch

The Roblox elevator format is proven: players recognise it on sight. Most elevator games are about
the rooms. This one is about the relationship between you, the lift, and whatever is outside it.

A lift is a strange refuge. It is enclosed and familiar, but you do not control where it takes you.
You escape a floor by getting in, then you are trapped while it moves.

> I want the doors to close because of what is outside. I do not want them to open, because I do not
> know what comes next.

That feeling is the identity of the game.

### What each influence contributes

We borrow what these games make the player feel, not their recognisable features.

| Influence | The experience we want from it |
| --- | --- |
| FNAF | Watch something, understand its behaviour, decide under pressure |
| The Backrooms | A place that is recognisable but wrong in scale, layout or purpose. You feel out of place before anything attacks |
| DOORS | Knowledge carried forward through an uncertain sequence. Players get better at recognising danger |
| Outlast | Committing to a vulnerable position, then surviving by moving, hiding and knowing too little |
| Poppy Playtime | Physical machinery that makes a place feel purposeful, with a few large encounters as peaks |

The rule that holds them together: **threats have understandable behaviour; the place stays a
mystery.** Players learn how to survive something without learning what it is.

---

## 2. What we have

| Asset | State | Role in this design |
| --- | --- | --- |
| First-person viewmodel (Ferryman's grafts: ash-gray synthetic arms, black leather gloves) | Finished, in Studio | Every interaction is seen through these hands. The single strongest asset |
| Vehicle Lift 04 | Built in Blender: center-opening telescoping car and landing doors, coupler, interlock, light curtain, motion profile, `LiftCycle` verified | The refuge, the save point, the only constant |
| Item and interaction setup | Working prototype | The basis for tasks (section 6) |
| Hoist cage, staging hall, rust and sodium art | Retired | Do not reuse the look. Runtime code (`ElevatorService`, `Elevator.luau`) is reusable |

---

## 3. The lift

### What it means

The lift is **comforting without being trustworthy**. It keeps working. It keeps taking you down.
Whether that is helping you is the question the game never answers directly.

Chosen direction: the lift **appears to be looking after you, for reasons you do not understand**,
expressed very subtly. It never speaks and never has a face. Examples of the register:

- The doors wait a beat longer than they should when a player is still running back.
- Something you left behind on a floor is in the car when the doors open at the next stop.
- The floor display shows a level that is not on the panel, once, then corrects itself.
- The panel light for the button you are about to press is already on.

These are rare. Used often, they turn the refuge into another dangerous room.

### Consistency rules (so players get attached)

- Same car every run: the same lighting, the same hum, the same chime, the same panel, the same
  protection pads. Players should know it well enough to notice a change.
- The lift is **never** the source of a jump scare. Nothing spawns inside it while the doors are shut.
- Players can leave objects in the car and they stay there for the run. The car becomes theirs.
- Changes inside the car are small, rare and remembered: a pad unhooked, a tube a different colour,
  a second capacity plate. One per several stops at most.

### The doors are real

The doors behave like real equipment because that is where the tension lives, and they are already
built that way:

- Opening takes a few seconds and closing takes longer. You cannot slam them.
- Anything in the doorway trips the light curtain and the doors reopen. After repeated trips they
  close slowly with a buzzer.
- Landing doors only open while the car is at that floor. If the car leaves, the landing doors are a
  wall.

Whether door timing is strong enough to carry the game is **a hypothesis, not a pillar**. The first
stop (section 10) is where it gets tested.

---

## 4. Why you leave the lift

"Do tasks while entities chase you" describes activity, not desire. The player needs an answer to
"why am I going deeper?" beyond "that is where the next level is". The design uses three layers:

1. **A reason to keep descending.** Someone went down before you, and they left things for you to
   find: notes, tapes, parking tickets with times written on them, a coat in a car. You are following
   them. Where they were going, and whether you want to get there, is the long mystery. The story is
   not decided (section 15); the structure is.
2. **A modest requirement at some stops, not all.** Some stops will not let the lift continue until
   something is done: power restored to the landing, a barrier raised, a key retrieved. Other stops
   ask nothing. The lift simply opens, and leaving the car is a choice.
3. **Optional reasons to go further.** Supplies (light, batteries, tools, a better torch), knowledge
   (a note that explains a threat, a map of a floor you will see again), and things that change the
   lift (a fuse that lets you choose between two stops). The best moments are "I could go back now,
   but I can see something useful past that ramp."

The layer-3 choice is where most of the horror should come from, more than locked exits.

Retired as a universal rule: **the fare.** "Pay the ferryman at the parking machine" remains a good
idea for particular stops, or for a landmark floor. Making every stop a payment errand would be
repetitive.

---

## 5. The stop: core loop

### The run

```
Descend  ->  Doors open  ->  The stop  ->  Back in the lift  ->  Doors close  ->  Descend
   ^                                                                               |
   +------------------------- supplies, damage, knowledge ---------------------------+
```

Each stop asks you to leave something familiar, understand a small part of an unfamiliar place, and
come back with the consequences: supplies, damage, knowledge, or something you wish you had not
brought back.

### The rhythm of a stop

**Explore, notice, understand, commit, escape, recover.**

Not every stop needs every step, and "escape" need not be a chase. A quiet stop that only teaches you
to look at something is a good stop. Recovery happens in the lift during descent: count what you
found, talk, check each other's light.

### Session shape

- A run is a sequence of stops to a **checkpoint floor** (section 9). Target 20 to 30 minutes between
  checkpoints.
- Death is per player. A downed player can be recovered by teammates who reach them. If everyone is
  down, the run ends at the last checkpoint reached.

---

## 6. Hands and items

The viewmodel matters because of **what your hands commit you to doing**.

### The design question for every interaction

> What does doing this stop me from watching or doing for a moment?

Interactions that briefly make you vulnerable:

- Lifting a car bonnet: it blocks your view of the garage.
- Reaching into an electrical cabinet: both hands inside, and footsteps behind you.
- Carrying something bulky: it hides the floor in front of you, and you must set it down to open a door.
- Turning a valve or cranking a barrier: slow, noisy, and you cannot turn around mid-turn.
- Inspecting a machine with the torch: the corridor beyond it goes dark.

These are timed actions played through the hands, cancellable at a cost (dropping what you carry,
restarting the crank). They are where the viewmodel becomes part of the horror.

### Inventory

A small, simple inventory stays, because a restrictive one would be awkward, especially solo.
**Not** adopted: "two hands, no inventory". What is kept from that idea: **bulky items** are carried in
both hands, cannot be stored, and are the thing a task is usually about. Small items (batteries, keys,
notes) go in the inventory.

### Tools and light

- The torch is the main tool. Battery is a real resource but generous at first.
- No weapons. Threats are survived by watching, hiding, moving and using the environment, not killed.
  (This is a direct reversal of v0.1 and is deliberate.)

---

## 7. Floors

### Principle

**Change the situation, not just the corridors.** A huge garage with randomised cars becomes
repetitive if every visit is "find the fuse, return". A smaller space feels new when its conditions
change:

- The objective is visible but the route to it is exposed.
- The route is familiar but the lights are out.
- The thing you need makes noise when carried.
- The threat reacts to movement this time, so the same open space has to be crossed differently.

### How a stop is made

A stop is assembled from four rolls on top of an authored floor kit:

| Layer | Examples |
| --- | --- |
| **Layout** | Modular pieces on a grid: ramps, bays, columns, service corridors, stairwells, plant rooms |
| **Purpose** | Nothing required; restore power; raise the barrier; retrieve an item; find the person's next note |
| **Condition** | Lights out; flooding; alarms sounding; one exit only; the lift will only wait so long |
| **Threat** | None, or one threat type from those the band allows (section 8) |

Plus **dressing** that sets the baseline: parked cars, drains, pipes, ventilation noise, signage,
oil stains, puddles.

### Authored floors

Some floors are always hand-built and always in the same place in the descent: the first stop,
each checkpoint floor, and the major reveals. The descent should be remembered as a sequence of
experiences, not a count of levels.

### The baseline rule

Every floor type first appears **quietly**, long enough to feel ordinary. Wrongness only works against
a baseline the player built themselves.

---

## 8. Threats

### Rules

- **Few, and understandable.** Each threat has behaviour a player can learn: what it responds to, what
  it ignores, where it goes. Learning it is the skill the game rewards.
- **Unexplained.** Knowing how to survive something never tells you what it is.
- **One at a time,** mostly. At most one active threat per stop in the early bands. Scarcity is scarier
  and much cheaper to build.
- **Readable.** A shape, a sound or a light tells you one is near before it matters.
- **They respect the lift.** Nothing enters the car while its doors are closed. Whether something
  follows you through open doors is a threat's defining trait, and the most frightening one to learn.

### Starting roster (concepts only, to prototype)

| Name (working) | Behaviour | What it teaches |
| --- | --- | --- |
| **The Attendant** | Walks the floor on a patrol between pay stations. Follows light, not sound. Turn your torch off and stand still | Observation (FNAF) |
| **Headlights** | A parked car that is not always parked. Moves only when no one is looking at it | Watching, and splitting a team's attention |
| **The Leak** | Something in the flooded bays. Follows splashing. Walk slowly, or stay on the dry ramps | Movement discipline |
| **The Occupant** | Hides in cars. You find it by what is different about a car you already walked past | Comparing the world against your own memory |

One of these is a **peak encounter** per band (Poppy Playtime's role): a larger, scripted set piece on a
checkpoint floor.

---

## 9. The descent

### Do not say "hell" early

The first basement plausibly belongs under a building. The descent is increasingly impossible
infrastructure, and players should wonder how any of it fits beneath the building before anyone
names it. The "Stygian" in the title is the only early hint.

### Bands

| Band | Stops (approx.) | Feels like | New idea it introduces |
| --- | --- | --- | --- |
| **Parking** | 1 to 10 | An ordinary multi-storey basement, then one level too many | Stepping out, the lift as refuge, the first threat |
| **Service** | 11 to 20 | Plant rooms, loading docks, laundries, corridors that go on too long | Timed actions, carrying things, noise |
| **Offices** | 21 to 30 | Backrooms: mono-yellow walls, damp carpet, drop ceilings, the hum | Getting lost, maps and landmarks |
| **Underneath** | 31 onward | Infrastructure that should not exist: flooded car parks, lifts inside lifts | Not decided. The reveal |

Each band ends in an authored **checkpoint floor** with a peak encounter. Reaching one saves the run.

---

## 10. The first stop

The introduction for new players, and the first thing to build. Solo, hand-authored, about 3 to 5
minutes, no threat that can hurt you.

1. **In the lift, alone.** The display counts down P1, P2, P3. The hum, the chime. Hands visible. The
   player can press buttons; only one does anything.
2. **Doors open onto an ordinary garage.** It is lit, mostly. Concrete, drainage, pipes, ventilation,
   a few parked cars at odd angles, one with dust on it. Let it feel like a garage for a while.
   No flicker, no scare.
3. **One clear reason to step out.** The lift will not go further: the landing's call panel is dead.
   A breaker cabinet across the level has a tripped switch. A note on a car windscreen, in the person's
   handwriting, points the way.
4. **One small interaction.** Open the cabinet (both hands in, the view narrowed), reset the breaker.
   Somewhere behind you, a single car's interior light comes on.
5. **The walk back.** The player passes the car. They remember it being dark. Nothing happens.
6. **The lift.** The doors are open. The player steps in and presses close. The doors take their
   time. The player watches the garage while they close.
7. **Descend.** Nothing is confirmed.

The player enters the next floor already watching more carefully. That is the whole job of the intro.

### What the first stop tests

- Does standing in the lift, waiting for the doors to close, feel tense? (Door timing hypothesis.)
- Do players notice the car light without being told?
- Do they want to press the close button, or do they keep looking at the garage?

---

## 11. Decided, and still to prove

| Decided | Still a hypothesis, test before building on it |
| --- | --- |
| First person, the graft viewmodel | Door timing as a core source of tension |
| 1 to 4 players, co-op, solo viable | The lift "looking after you" reads as intended and not as a bug |
| The lift is the refuge; nothing enters it while closed | Bulky items as the centre of most tasks |
| No weapons; survive by observation and movement | Which threats are fun, from section 8 |
| Stops are procedural situations on authored kits; key floors hand-built | How much procedural variety a stop needs to stay fresh |
| The descent starts plausible; "hell" is never announced early | The long story (section 15) |
| Checkpoint floors per band | Run length and death rules in co-op |

---

## 12. Technical notes

- **Strictly first person.** The graft viewmodel (four skinned meshes, 39 bones, independent arm and
  glove skins) is installed in Studio and the Rojo project. Guide: `output/viewmodel/full/README.md`.
  Interactions are authored as viewmodel clips, as the gate open and close clips already are.
- **The lift in Roblox.** `ElevatorService` and `Elevator.luau` already provide the root, prismatic
  travel, floor markers, promises and signals. The new doors need a rig module driven by the recorded
  motion profile in `output/lift/lift_meta.json`, with the same "replicate once, animate on clients"
  approach the scissor gate uses. The car stays one model for the whole run; floors stream in and out
  below it.
- **Floors** are built from modular kits on a fixed grid, streamed in when the lift arrives and
  removed after it leaves. StreamingEnabled on.
- **Server authority.** Threat behaviour, item state, door state and progress live on the server.
  Clients send intent.
- **Deterministic seeds per run** for reproducible floors and bugs.
- **Analytics from day one:** stops reached, where players die, which threats kill them, how long they
  stay out of the lift, how often they turn back from an optional item, session length, D1 return.

---

## 13. Monetization rules

Details wait until the first stop is fun. The rules carry over from v0.1:

- **Never sell immunity to the core tension.** Nothing that makes threats harmless or the lift faster.
- **Everything purchasable is also earnable,** except cosmetics.
- **No paid random items in v1** (full odds disclosure is required and is work we do not need yet).
- Likely products: revives, cosmetics for the hands (glove and arm skins; the viewmodel already has
  separate skin slots), and **personal objects that live in the lift** for the run, which feeds the
  attachment in section 3.

---

## 14. Milestones and gates

### M1: The first stop (target about 40 hours)

The lift car in Studio with working doors. The authored first garage. The breaker interaction through
the hands. The car interior light. No other threats, no procedural floors.
**Goal: find out whether leaving and returning to the lift feels like something.**

### M2: One procedural band (about 120 hours)

The parking kit, the stop assembler (layout, purpose, condition, threat), two threats from section 8,
the torch and inventory, co-op for up to 4, one checkpoint floor.

### M3: Presentable (about 120 hours)

The service band, remaining threats, audio, lighting and art passes, the note trail.

### M4: Ship (about 80 hours)

Progression, monetization, analytics, soft launch.

### Gates

| Gate | When | Threshold | If failed |
| --- | --- | --- | --- |
| **Feel check** | After M1 | 5 outside players, unprompted, say something about the car light or the doors | Rework the stop. Do not start procedural generation |
| **Fun check** | After M2 | 5 outside players voluntarily start a second run | Rework the loop or stop |
| **Retention** | Soft launch | D1 above 25%, median session above 12 minutes | One tuning pass; if still below 20%, stop |
| **Traction** | 2 weeks after launch | Sustained CCU above 30 | Stop |

---

## 15. Open questions

- **The long story.** Who went down before you, and why are you following them? What is at the
  bottom? Decide the shape before M3; the first stop only needs one handwritten note.
- **Title.** *Stygian Drop* hints at the underworld, which section 9 wants to keep quiet. A plain
  public title ("Car 04", "Lift", "Sublevel") with the underworld as a late reveal may serve better.
- **How far does the lift's care go?** Could it ever refuse to open for a threat? Could it ever leave
  without someone? Each of those is powerful once and ruinous if frequent.
- **Co-op and the doors.** Holding the doors for a teammate is a natural co-op moment. Should the lift
  wait for everyone, or leave on a timer at some stops?
- **Car size.** Lift 04 was sized as a combat arena. For 1 to 4 players without a horde, a smaller car
  might feel more intimate. Keep it large for now: an oversized empty lift is its own kind of wrong.

---

*Design document, v0.2, 19 September 2026. Replaces the arena design. Nothing here survives contact
with the first playtest, and that is the point.*
