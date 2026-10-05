# Task Prompt: The Lift (Blender), a new theme, built for real

You have Blender MCP access and can run background Blender from the shell. Build **one elevator** in
Blender, to a high standard, for the Roblox game Stygian Drop. The elevator is the game's arena: the
players fight inside it while it descends. This task is the elevator and nothing else. No hall, no
lobby, no parking level, no Roblox Studio work.

The user's own words:

> I want to change themes and restart. As of now only the viewmodel is good, perfect actually. I want
> a backrooms mix (and something like basement parking stuff) + a theme that matches the vibe, a place
> where the kind of viewmodel (arms) we have seems to fit in. The mineshaft was a completely wrong
> approach. I am expecting things to be of high quality, like doors closing (you can explore the idea
> of having modern doors) and I am expecting proper functionality there, just as how doors would close
> in real life.

Work at full effort. The user judges the result by what exists in the scene and by the renders and
the door animation, not by plans. Build the whole elevator, then refine it. Do not stop to ask
questions (section 9 lists the only reasons to stop).

---

## 1. What went wrong before, so you do not repeat it

- The previous art direction (rusted riveted steel, sodium light, mine shafts, scissor-gate hoist
  cages, an underworld ferry dock) is **rejected**. The user rated the staging hall 0 out of 10. Do not
  reuse its look, its materials, its kit, or its hoist cage. Do not open `doors_elevator.blend` or
  `staging_hall.blend` for reference beyond checking a number.
- Nothing there was wrong technically. It was wrong in **mood**: warm, rusty, busy and theatrical.
  The new world is the opposite: quiet, flat, fluorescent, institutional, too clean in some places and
  quietly wrong in others.
- Doors were previously a scissor gate animated as a lattice. This time the doors are the centrepiece:
  modern, powered, coupled car and landing doors that move the way real ones do (section 5).

## 2. The one thing that is already right: the viewmodel

Every design decision must make these arms look at home. Look at them before you start:
`output/viewmodel/full/renders/GraftViewmodel_FirstPerson.png`, `..._Anatomy.png`, `..._Grip.png`,
and read `output/viewmodel/VIEWMODEL_BRIEF.md`.

- **Ferryman's grafts**: human arms rebuilt in ash-gray synthetic dermis, paired recessed tendon
  channels, subtle elbow compression folds, a thin bronze bonded repair seam.
- Near-black supple leather gloves, charcoal stitching.
- The feeling is clinical, maintained, anonymous, quietly unnatural. A crew member of something
  institutional that has been running on its own for a long time.

What that implies for the elevator: brushed and satin metals, enamel paint, matte polymers, rubber,
fluorescent light, cold neutral greys against sick yellows, a single restrained warm accent (brass or
bronze) that rhymes with the repair seam. No gore, no rust-horror, no neon, no sci-fi panels.

## 3. The theme: sub-level parking meets the backrooms

**World idea (for context only, do not build it):** an underground car park beneath a building that
no one remembers. The levels go down past where they should stop: P1, P2, P3, and then numbers that
do not make sense. The deeper levels drift from parking concrete into backrooms interiors: mono-yellow
walls, damp carpet, drop ceilings, humming fluorescent tubes, fire doors to nowhere. The only way
between them is one large vehicle lift. The lift still works perfectly. That is the unsettling part.

**The elevator:** a large, modern-ish (1990s to 2000s institutional, well maintained, slightly worn)
**vehicle and goods lift** of the kind found in hospital basements and multi-storey car parks, big
enough to carry vans. It is the arena, so it must be large, and a vehicle lift is the honest reason
for a car that size.

Mood words: liminal, humming, overlit-underlit, clean-but-wrong, empty, patient, municipal.

Ideas to use, adapt or improve (you decide, and record why in the design record):

- **Stainless center-opening telescoping doors**, satin brushed, with a black rubber safety edge and a
  full-height light curtain on the car door edge. Panels big enough to feel like machinery.
- **Car interior**: enamel-painted steel wall panels in an institutional beige or pale mustard, with
  stainless bumper rails and a heavy rubber floor (stud or coin pattern) or steel checker plate worn
  bright in the traffic lanes. Grey quilted **protection pads** hung on stainless pad buttons on one or
  two walls, the way real service lifts carry them: soft, grey, slightly sagging, instantly liminal.
- **Ceiling**: a suspended ceiling of perforated metal or diffuser panels with fluorescent troffers,
  one tube a slightly different colour temperature from the others; a ventilation fan grille; a
  top-of-car emergency hatch outline (the doc's "entry point for aerial enemies").
- **Car operating panel (COP)**: brushed stainless, round mushroom buttons with a thin ring halo,
  engraved labels (P1, P2, P3, P4, and a few blank buttons), door open and close buttons, alarm,
  emergency phone grille, key switches (independent service, fire service), inspection certificate
  frame with an unreadable faded card. A second, lower accessible COP on the opposite wall.
- **Position indicator** above the car door: a dot-matrix or segmented display. Design it to show
  level names like `P3` and also to carry the game's Manifest readout later. A mechanical dial
  indicator would be a period-correct alternative: pick one and justify it.
- **Signage and markings**: capacity plate ("RATED LOAD" in kg and an invented maximum number of
  vehicles), a "NO SMOKING" pictogram plate, yellow and black hazard stripe on the car sill edge and
  fascia, a painted floor stencil. All text and logos invented. No real brands, no real manufacturer
  names, no real regulation numbers.
- **The game requirements in theme** (from `STYGIAN_DROP.md` section 4, still binding): 6 players and
  30 or more enemies without the melee becoming a pile; front and rear door faces (a through car);
  a central obstruction so no one sees the whole car at once; a raised position worth fighting for;
  a grated or openable ceiling; emergency lighting. Express these in theme, for example: an abandoned
  hatchback or a pallet cage strapped down in the car as the obstruction, a raised loading platform or
  vehicle ramp along one wall as the high ground, battery emergency fittings that switch on in a
  blackout. The obstruction and high ground are props inside the car, separate objects, removable.
- **Wrongness, used sparingly**: one control panel button that has no label, a second capacity plate
  with a different number, the protection pads hanging in a place a person could stand behind, a
  bronze fitting that does not belong. Two or three details, not a haunted house.

If you have a better idea for the elevator that still satisfies sections 2 and 3, argue it in the
design record in a paragraph and build it. Do not produce a concept menu for the user to choose from.

## 4. Scale and size (decide, measure, record)

Author at **1 Blender unit = 1 stud**. Roblox characters are about 5 studs tall and this game is
strictly first person, 70 degree vertical FOV, camera about 4.6 studs above the floor.

- Size everything a hand touches **to the player's body**, treating the player as an adult: call and
  car buttons centred about 3.0 to 3.5 studs up, handrails and bumper rails about 2.6 to 2.9 studs,
  door opening height at least 8 studs so the doorway reads as a vehicle entrance and not a cupboard.
  Check each against the viewmodel in a first-person render. Record the final numbers.
- The car interior is large because it is the arena. Target roughly 30 to 44 studs wide and 36 to 48
  studs deep, clear height 12 to 16 studs. Justify the final numbers against 36 bodies (6 players,
  30 enemies) at about 40 square studs each plus the obstruction and the high ground, and against how
  a real truck lift is proportioned. It must not feel like a warehouse with a door.
- Door openings: wide enough that 3 or 4 players pass abreast. That points to 12 to 18 studs wide.
  Choose the door configuration to suit (section 5).

## 5. The doors: the heart of this task

Model and rig the doors as a real modern elevator door system, then prove it moves like one. Research
real center-opening elevator door equipment if you need to; do not invent a simplified version.

### 5.1 What must exist, as separate objects with clean pivots

On **each** entrance (front and rear), two door sets:

1. **Car doors** (ride with the car): center-opening, telescoping. Two-speed (four panels) at minimum;
   three-speed (six panels) if the opening is wide enough that two-speed panels would be unreasonably
   broad. Each panel on its own hanger with top rollers on a header track, up-thrust rollers, and
   guide shoes (gibs) running in a grooved car sill. A door operator on the car top: motor, gearbox or
   belt drive, operator arm or belt clamps, and the relating mechanism (cables over pulleys, or a
   belt) that makes the fast and slow panels move in the correct ratio. A **door coupler (vane or
   clutch)** mounted on the car door. The safety edge and light curtain on the leading edges.
2. **Landing doors** (stay at the floor): the same panel configuration, on their own header track and
   landing sill, with an entrance frame (jambs, head), a **door interlock**, pickup rollers the car
   door coupler engages, and a **self-closing device** (a closer weight in a tube, or a spring closer).
   Landing doors never move by themselves except to self-close. They open only when the car is in the
   landing zone and the coupler has engaged their rollers.

Also on each entrance: car door and landing door sills with a realistic running gap between them,
a car apron (toe guard) below the car sill, and a landing fascia.

### 5.2 How they must move

Build it as a real rig, not keyframed panels:

- One custom property per entrance on the car, `door_command` (0 closed, 1 open), drives a door
  operator value through a **motion profile**: jerk-limited acceleration, cruise, deceleration, a slow
  final "checking" approach into the fully open and fully closed positions. Every panel is driven from
  that one operator value through **drivers**, with the telescoping ratios exact (two-speed 1:2,
  three-speed 1:2:3 of travel). No panel is keyed by hand.
- The landing doors follow the car doors **only through the coupler**: a driver that checks the car's
  height against that landing and engages only inside the landing zone (a few studs). Outside the
  zone the landing doors stay locked shut. If the car doors close while the landing doors are open,
  the landing doors close with them; if the coupler releases early, the closer brings them home.
- Timing in the spirit of real equipment for a door this wide: opening about 2.5 to 3.5 seconds,
  closing slower than opening (about 3.5 to 5 seconds), dwell open about 4 to 6 seconds. Closing is
  gentle because real closing force and kinetic energy are limited. Record the final curve.
- **Reopen on obstruction**: while closing, a light-curtain trip reverses the doors to fully open
  without a hard snap (decelerate, then reverse).
- **Nudging**: after repeated obstructions, the doors close at reduced speed with a buzzer cue
  (record the cue as a named event, no audio needed).
- The car may not move while any door on it is unlocked; the landing interlock releases only with the
  car in the zone. Put this in the rig as a readable state, even if Blender cannot enforce it.
- Constant clearances: panel to panel, panel to frame and panel to sill gaps stay constant through the
  whole stroke. Nothing interpenetrates at any frame.

### 5.3 Prove it

- A **test shaft segment** with just enough to exercise the doors: two landing entrances one floor
  apart (front face on one, front and rear on the other), guide rails, the car sling and roller guides,
  a counterweight glimpse, and a car that travels between them. This is a test rig for the elevator,
  not an environment: plain dark shaft walls, no parking level, no hall.
- An action, `LiftCycle`, about 30 to 45 seconds: arrive at a landing with a proper leveling approach,
  couple, open, dwell, start closing, obstruct, reopen, dwell, close, lock, depart, travel one floor,
  arrive, open the rear face. Drive it by animating only the custom properties, never the panels.
- A **verification script** that steps through every frame of `LiftCycle` and reports: panel ratio
  error, minimum and maximum gap per panel pair, any mesh intersection between moving and static door
  parts (BVH overlap), landing doors ever open without the car in the zone, car moving with a door
  unlocked. It must pass with zero violations before you call the doors done.
- Renders of the cycle (section 7).

## 6. The rest of the elevator, to the same standard

- **Car structure**: platform, sling (crosshead, stiles, safety plank), roller guides on T rails,
  car top with the door operators, a balustrade, the car top inspection station, the fan, and the
  emergency hatch. The player never sees most of this from inside, but aerial enemies come through the
  ceiling, so the car top must hold up in a render from above.
- **Interior**: walls, pads, rails, floor, ceiling, lights, both COPs, the position indicator, signage,
  the emergency lighting fittings, the obstruction prop, the high ground. Real bevels and radii on
  everything a hand would touch. Screws and pad buttons as real geometry where they catch light.
- **Materials**: physically based and restrained. Brushed stainless with directional anisotropy read
  through roughness streaks; enamel with fine orange peel and chipped edges at impact heights; worn
  rubber; fluorescent diffusers with a faint yellowed tint; quilted pad fabric with stitching; one
  bronze accent. Wear goes where people and vehicles actually touch: sill grooves, bumper rails, the
  area around the COP, the lower door panels.
- **Lighting of the car itself**: the troffers are the key. Emergency fittings as a switchable
  collection. The car must look right lit only by its own fittings, in black surroundings.

## 7. Renders you must produce and look at

Real renders from placed cameras, compressed JPG, in `output/lift/renders/`. EEVEE for review, Cycles
with denoising for heroes. No gizmos, grid, overlays or light icons. Every interior view is first
person at 4.6 studs, 70 degree vertical FOV, with the viewmodel's scale in mind (link or append the
viewmodel from `assets/blender/viewmodel.blend` for at least two renders, hands at rest and one hand
reaching for the COP).

1. Standing on a landing, doors closed, car arriving (position indicator changing).
2. The same view, doors mid-open, both car and landing panels visibly telescoping.
3. Inside the car, looking out through fully open front doors.
4. Inside the car from the back corner, whole interior, obstruction and high ground readable.
5. The COP close up with the viewmodel hand reaching for a button.
6. The door operator and coupler on the car top, lit for inspection.
7. Emergency lighting only, inside the car.
8. A cutaway or section of one entrance showing car doors, landing doors, sills, running gap,
   hangers, coupler and interlock, like a manufacturer's drawing.
9. An EEVEE animation of `LiftCycle` from render 2's camera, saved as MP4, plus a contact sheet of
   12 evenly spaced frames.

Open every image and critique it before moving on. Ask: **would someone who has stood in a basement
car park at 3 a.m. recognise this lift, and feel slightly uneasy in it?** If not, fix the scene.

## 8. Roblox-ready hand-off (files only, no Studio, no uploads)

- Scene structure: collections `Lift_Car` (moves), `Lift_CarDoors_Front`, `Lift_CarDoors_Rear`,
  `Lift_LandingDoors_*`, `Lift_Props` (obstruction, high ground), `Lift_TestShaft`, `Lift_Lights`,
  `Lift_Lights_Emergency`, `Colliders`, `Cameras`. Moving parts separated from static. Every panel's
  origin at its hanger centre, travel axis recorded.
- Meshes per piece to `output/lift/meshes/` as FBX and GLB, 1 unit = 1 stud, transforms applied.
  Hard cap 20,000 triangles per mesh; aim under 10,000; report every piece.
- Roblox takes **one material per MeshPart**. Either split multi-material pieces by material at
  export, or give unique props UVs and a baked SurfaceAppearance set. Tiling surfaces (wall enamel,
  floor, ceiling) use tileable PBR maps meant for MaterialVariants (`StudsPerTile` recorded; they tile
  from face centres). Unique props get 1024 baked maps: ColorMap sRGB, NormalMap OpenGL tangent,
  RoughnessMap, MetalnessMap. Non-colour maps are 8-bit RGB with **no alpha channel**. No text or
  symbols baked into maps that could be misread by moderation: signs and displays are separate meshes
  whose text becomes SurfaceGui labels in Roblox.
- `output/lift/lift_meta.json`: in studs and Roblox axes (Roblox x, y, z = Blender x, z, -y): every
  piece and its pivot; per entrance, per panel: closed and open positions, travel, speed ratio, track;
  the door motion profile sampled at 30 Hz for open, close, reopen and nudge; dwell; landing zone
  height; coupler engagement window; the car's `CageRoot` equivalent, a prismatic anchor point with
  its axis, floor marker heights; COP button positions and labels; indicator, lights (type, colour,
  range, brightness, shadow) and colliders. The existing runtime (`src/ServerScriptService/Modules/Elevator.luau`
  and `src/ReplicatedStorage/Elevator/GateMotion`) drives a scissor gate today; write a short note on
  what an `ElevatorRigs` module for these doors would need, without editing `src/`.
- A list of new textures that would need uploading, with sizes.

## 9. How to work

### 9.1 Order

1. Read the files in section 10 (briefly), look at the viewmodel renders, write the design record's
   first section (concept, why it fits the arms, final dimensions with reasons).
2. Block out the whole elevator at true scale in one pass: car, both entrances, all door panels as
   boxes, test shaft, props. First-person renders from inside and from a landing. Fix proportions now.
3. Build and rig the door system (section 5) and pass the verification script. This comes before
   interior detail because it constrains the frame, header and sill geometry.
4. Car structure and car top.
5. Interior, props, signage.
6. Materials, then lighting.
7. Renders (section 7), hand-off (section 8).

### 9.2 Rules

- Everything scripted and re-runnable, under `output/lift/scripts/`, numbered in build order, key
  dimensions as named constants at the top (car width, depth, height, door width, height, panel
  count, travel ratios, timings, landing spacing). Change a constant and rebuild. No unreproducible
  hand edits.
- Work file: `assets/blender/lift.blend`. Link the viewmodel for renders (relative path), never edit
  `viewmodel.blend`. Do not modify `doors_elevator.blend`, `staging_hall.blend` or `lobby.blend`.
- Save constantly (`bpy.ops.wm.save_mainfile(compress=True)`), always before a render, bake, boolean
  apply or any script you have not run before. Confirm the file time changed from the shell.
- Git: work on a new branch `lift/vehicle-lift` from `main`. Commit and push after the blockout,
  after the doors pass verification, after each major stage, and before long renders. Stage explicit
  paths only; never `git add -A`, never commit `.DS_Store` or `.blend1`, never force-push or rewrite
  history. Keep the .blend under 50 MB (split kit pieces into linked files if needed).
- Stop and wait only if: a push fails and you cannot fix it; the .blend nears 50 MB and splitting does
  not solve it; Blender crashes unrecoverably; or a requirement is physically impossible, with evidence.
  Everything else: decide, record the reason, keep building.
- Documentation: `output/lift/LIFT_DESIGN.md` (concept, dimensions, door system, verification
  results, triangle budgets, compromises) and a dated entry in `output/NOTES.md`. **No em dashes** in
  anything you write.

### 9.3 Blender quirks on this machine (Blender 5.1, Apple Metal GPU)

- `execute_blender_code` must set `result` to a dict. MCP requests time out around 40 seconds: run
  heavy work (Cycles, bakes, long verification) in background Blender from the shell with `--python`,
  and never save the .blend from a background process while the interactive session has it open.
- Start interactive renders with `bpy.ops.render.render('INVOKE_DEFAULT', write_still=True)` and poll
  for the file.
- The area screenshot tool needs `size_limit_in_bytes` around 300000; prefer real renders.
- Principled node type is `ShaderNodeBsdfPrincipled`; `ShaderNodeMix` sockets by identifier
  (`Factor_Float`, `A_Color`, `B_Color`, `Result_Color`); `mesh.use_auto_smooth` is gone.
- After a file reload `bpy.context` has no active object: build with bmesh and the data API, or use
  `temp_override`.
- A light inside a glass or diffuser mesh lights nothing with caustics off: set `visible_shadow = False`
  on the diffuser.
- Drivers that read another object's transform need that object as a driver variable target, not a
  Python expression over `bpy.data`, or they will not update in background renders.

## 10. Read first (skim, do not dwell)

| File | Why |
| --- | --- |
| `output/viewmodel/VIEWMODEL_BRIEF.md` and `output/viewmodel/full/README.md` | The arms this world must suit, and the camera setup |
| `STYGIAN_DROP.md` sections 4 and 11 | Arena requirements and technical constraints (first person, streaming, enemy cap) |
| `roblox_material_pipeline_prompt.md` sections 1 and 2 | SurfaceAppearance vs MaterialVariant, map conventions, alpha rules |
| `output/NOTES.md` | Importer, collision and upload lessons (read for the Roblox facts, ignore the old art direction) |
| `src/ServerScriptService/Modules/Elevator.luau` | What the runtime expects: a root, a prismatic anchor, floor markers, a door rig module |

## 11. Final report

End with one short report: the concept in two or three sentences and why it fits the arms; the final
dimensions; the door configuration, timings and verification result (zero violations, with the
numbers); triangle totals and the largest piece; texture list; the render paths, with the door cycle
MP4 first; compromises with reasons; the last pushed commit hash.
