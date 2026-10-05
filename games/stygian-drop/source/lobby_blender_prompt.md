# Task Prompt: The Staging Hall (Blender), v2: build the whole arena

You have Blender MCP access. Build, in Blender only, the **complete arena** where six players arrive by hoist cage, gear up, and board a gigantic central elevator. It will ship on Roblox later, so every decision has to survive that move. You are not touching Roblox Studio in this task.

The user's own words:

> Reuse this elevator, and the idea here is 6 of these will allow 6 players to come together into one arena, that arena will have another different (and gigantic) elevator in the middle with areas outside the elevator for armoring up and getting weapons. A lot to consider here, I was thinking of a circular design with the elevator in the middle but this can get way better than that I believe.

Treat "circle with the elevator in the middle" as the baseline to beat, not the answer.

---

## 0. Why this is v2, read this first

A first run of this task has already happened. It stopped after Stage 1 with a file that links one hoist cage, a 5-stud proxy, a design record, and four questions. The user saw a single cage in a rock shaft and was, in their words, disappointed: **they expected the entire arena.** That was a fault in the v1 prompt, which told the agent to stop and wait after understanding and again after concepts.

This prompt removes those stops. The deliverable is **the whole arena, built, lit, and rendered**, not a plan, a question list, or one piece of it. Do not end your session with questions for the user unless you are genuinely blocked (section 6). Where something is ambiguous, pick the strongest option, write down why in the design record, and keep building.

### What already exists (do not redo it)

On branch `lobby/staging-hall` (pushed, last commit `8c53aeb`):

- `assets/blender/staging_hall.blend`: links Hoist No.2 from `//doors_elevator.blend` by relative path, plus a 5-stud character proxy. Verified to open clean.
- `output/lobby/scripts/00_setup_file.py`: rebuilds that file from scratch.
- `output/lobby/LOBBY_DESIGN.md`: the interpretation, the conflict table against `STYGIAN_DROP.md`, and **measured facts about the hoist** (dimensions, gate face, shaft sizes, triangle counts). Read it fully and trust its numbers; they were measured from the .blend.

Check out the branch, pull, confirm you are at or after `8c53aeb`, and build on it.

---

## 1. Read before building

In the repo at `/Users/az9umas/Desktop/Stygian`:

| File | Why |
| --- | --- |
| `output/lobby/LOBBY_DESIGN.md` | Stage 1 output. Your starting point. |
| `STYGIAN_DROP.md` | Design doc. Sections 4 (Acheron Express), 9 (lobby), 11 (technical). |
| `output/NOTES.md` | Scale, texture, collision and importer decisions with reasons. |
| `output/roblox/HOIST_README.md` | How the hoist moves and what a floor needs. |
| `roblox_material_pipeline_prompt.md` | Roblox mesh and texture specs, bake rules, naming. Sections 1 and 2 apply. |
| `src/ReplicatedStorage/Configs/ElevatorConfig.luau`, `src/ServerScriptService/Modules/Elevator.luau` | What the runtime expects from an elevator model. |

Do not spend long here. Stage 1 already digested these; skim for anything LOBBY_DESIGN.md does not cover and move on to building.

---

## 2. Decisions already made (do not reopen them)

These answer the four open questions in LOBBY_DESIGN.md section 4. The user can override them later; until then, build to them.

1. **One party of up to six, on a six-player server.** The hall is that party's staging area, not a public lobby.
2. **The Express physically leaves.** It seals, then drops out of the hall into its own shaft, 40 to 60 studs down to a sealed station where the run's floors are faked. Model the hall, the pit, and enough shaft below the hall floor to sell the drop (a stub that fades to black). The station below is out of scope.
3. **Gear-up is per-player loadout selection at shared stations.** Physical racks and stands where a player picks a weapon and an armour class from their unlocks. Shared stations with several slots so six players never queue; respect the 7-stud ProximityPrompt spacing. Armour and weapons are distinct places with distinct silhouettes.
4. **Players spawn inside their hoist cage at the top of its shaft, in the dark, and ride down.** The gate opening on the hall is the first frame. No surface hub. The Ledger (leaderboard wall) and the Ferryman (shop) live in this hall.
5. **Six hoists stay six**, including for small parties. Unused cages park at the top, dark. A physical crew board reads the party state (for example `CREW 2 OF 6`).
6. **The six shaft surrounds are a new, lighter reusable piece.** The existing mine rock surround is 85,600 tris per shaft (924,660 for six hoists); do not use it in the hall. The linked cage itself (68,510 tris) stays as is.

---

## 3. What "the entire arena" means: definition of done

At the end of your session, `staging_hall.blend` must contain all of this, assembled in place at true scale, and the renders in section 3.2 must show it. If any line is missing, you are not done.

### 3.1 In the scene

- **The hall itself:** floor, walls, ceiling or overhead structure, edges that fall to black. Not a floating slab on an infinite grid.
- **All six arrival hoists**, each with its linked cage, its new shaft surround integrated into the hall architecture, a landing sill, and the shaft visibly continuing up into darkness above the hall.
- **The Acheron Express, fully modelled**, not a box proxy: car structure, caged see-through walls, front and rear door faces with a door mechanism that reads at this scale, mezzanine or raised position inside, central obstruction, grated ceiling, Manifest split-flap board above the front doors, floor dial, emergency light fixtures. Moving parts separated from static per the `_Export` / `_ExportMoving` convention, with clean pivots and recorded travel.
- **The Express shaft and pit:** the opening in the hall floor, a safe sill and edge treatment, the headgear or overhead structure the car hangs from, and the shaft stub below.
- **Gear-up stations:** armour stands and weapon racks, placed and modelled to a readable level, with every prompt point marked.
- **The Ledger** wall and **the Ferryman** shop counter or booth.
- **The crew and countdown board**, readable from every arrival cage.
- **Lighting:** sodium keys, practical fixtures, emergency red as a switchable collection, absolute black beyond the edges.
- **Materials** on everything visible. Reuse the uploaded cage PBR sets and the `DiamondPlate_WornSteel` MaterialVariant wherever they fit.
- **Set dressing** that makes it a place: cables, pipes, signage (invented, no real brands), puddles, the dustbin prop from `assets/props/dustbin/` linked where it fits.
- **Colliders** as simple named volumes in their own collection.
- **Six character proxies** in the review renders, one per arrival cage, plus a group at the Express doors.

### 3.2 Renders you must produce and look at

Real renders from placed cameras, not viewport screenshots. No overlays, grid, gizmos, light icons or camera wireframes in any deliverable image. EEVEE for review passes, Cycles with denoising for final heroes. Save as compressed JPG in `output/lobby/renders/` (committed).

1. Top-down orthographic plan of the whole arena with zones labelled.
2. Wide establishing shot showing the entire hall, all six shafts and the Express in one frame.
3. First frame from inside each of the six cages as the gate opens (six images; they should look fair and near-identical in what they offer).
4. Gear-up area at player eye height with proxies using it.
5. The party at the Express doors.
6. Inside the Express looking out through the open doors into the hall.
7. Emergency red variant of the establishing shot.
8. The Express mid-drop, roof half below the hall floor.

Open every render and critique it before moving on. Ask of each one: **if the user saw only this image, would they say "that is the arena"?** If not, fix the scene, not the caption.

### 3.3 Hand-off files, still no uploads

- Meshes exported per piece (FBX and GLB, studs, transforms applied) to `output/lobby/meshes/`.
- `output/lobby/layout_meta.json` in the style of `output/roblox/scene_meta.json`: placements, pivots, door axes and travel, floor marker heights, prompt points, spawn and arrival points, lights, all in studs and Roblox axes.
- A list of new textures needing upload and which existing IDs are reused.
- A short note on what an `ElevatorRigs` module for the Express would need.
- `LOBBY_DESIGN.md` updated with the chosen layout, reasoning, rejected concepts, and every number below.

---

## 4. How to work

### 4.1 Breadth first, always a whole arena

The v1 run failed by going deep on one cage. Do the opposite.

1. **Concepts, fast, no approval stop.** Sketch at least three genuinely different layouts as quick top-down plans with rough massing (one may be the circle). Candidates to consider, not a menu: hexagonal ring with shafts in the walls; sunken amphitheatre with arrival high and the Express at the bottom; split level with arrival above and staging below; spoke plan with a bay per hoist; an asymmetric pit-head where all six hoists hang from one colossal headframe. Score them against section 5, pick the winner yourself, record the scoring and the rejected ones in LOBBY_DESIGN.md, commit, and go straight on. Budget: a small fraction of the session, not most of it.
2. **Full blockout of the entire arena.** Every item in 3.1 present as grey massing at true scale in one pass: hall, six shafts with linked cages, Express massing with door-open poses, pit, stations, Ledger, Ferryman, boards, proxies. Render the plan, the establishing shot and the six first frames. Fix layout problems now, when they are cheap. Commit.
3. **Model the Express for real.**
4. **Replace hall blockout with the modular kit** (wall panel, corner, pillar, floor tile, ceiling section, trim, light fixture, door frame, plus the shaft surround and whatever the layout needs), snapping to a consistent grid.
5. **Stations, Ledger, Ferryman, boards, dressing.**
6. **Materials, then lighting.**
7. **Final renders (3.2) and hand-off (3.3).**

**After step 2, every commit contains a complete arena** at whatever fidelity has been reached. If the session is running long, keep the whole arena consistent and lower the polish, rather than finishing one corner beautifully and leaving the rest grey. Never end on a partial arena.

### 4.2 Keep going without check-ins

- Do not stop to ask for approval between steps. Record decisions and move on.
- Post short progress notes as you go (what changed, a render path, the commit hash), then continue immediately in the same turn.
- The only reasons to stop and wait are in section 6.

### 4.3 Scripted and re-runnable

- Python under `output/lobby/scripts/`, numbered in build order (`00_setup_file.py` exists). Key dimensions as named constants at the top: shaft count, hall radius or bay spacing, hall height, Express interior size, pit size, station spacing, drop depth.
- The user must be able to change a constant and rebuild the arena. Hand-placed tweaks that no script can reproduce are not allowed.

---

## 5. Design criteria (use for concept scoring and self-review)

1. **The first frame.** The Express dominates what a player sees when their gate opens.
2. **Fairness.** No cage is meaningfully closer to armour, weapons, or the boarding doors. Report walk distance per cage in studs and seconds (16 studs/s).
3. **Flow.** Arrive, armour, weapons, board. Six players at once, no queues, no awkward crossings. Prompts at least 7 studs apart.
4. **Convergence.** Players see each other arrive and naturally end up together at the doors.
5. **Density.** Empty floor space reads as amateur. Keep walks short; cut area you cannot justify.
6. **Spectacle.** Crew state and countdown readable from anywhere, physically. The departure of the Express is a moment.
7. **Scale contrast.** The hoist cage is 8 studs across. The Express is a different class of machine: it must hold 6 players and 30+ mobs without the melee becoming a pile, so expect an interior somewhere around 40 to 60 studs across. Justify the final number. It should dwarf the cages without swallowing the hall.
8. **Theme.** Rusted steel, riveted plate, sodium light, standing water, black beyond the edges. Mine pit-head meets underworld ferry dock. The hoist sets the material language.
9. **Roblox cost.** StreamingEnabled on. Track total triangles, part count, and shadow-casting lights. Six cages are 411k tris already; the rest of the hall should be budgeted around that and reported.

---

## 6. When you are allowed to stop and wait

Only these:

- A git push fails and you cannot fix it.
- `staging_hall.blend` approaches 50 MB (see 7.2).
- Blender crashes in a way you cannot recover from after reopening the last saved file.
- A decision in section 2 turns out to be physically impossible, with evidence.

Anything else, decide, document, and continue.

---

## 7. Hard constraints

### 7.1 Reuse, do not remodel

- Link the hoist cage from `doors_elevator.blend` (relative path). Never save or edit `doors_elevator.blend`.
- Reuse existing texture sets by ID (`output/roblox/uploaded_ids.json`) wherever they fit. Every new texture is a future upload and a moderation risk.
- Leave the user's untracked `assets/blender/lobby.blend` alone.

### 7.2 Saving and version control (crucial, do not skip)

Losing work is the one outcome the user will not accept. Blender has crashed mid-bake on this project before.

**Save the .blend constantly.**

- `bpy.ops.wm.save_mainfile(compress=True)` after every meaningful change, and always before a render, bake, heavy boolean or modifier apply, or any script you have not run before.
- After saving, confirm from Bash that the file's modified time changed.
- Keep library paths relative.

**Commit and push to GitHub as you go.**

- Work on the existing `lobby/staging-hall` branch. Do not commit to `main`.
- Commit **and push** at minimum: after the concept pick; after the full blockout; after each major piece (Express, kit, stations, materials, lighting); before any long render or bake; and roughly every 30 minutes regardless (`WIP: ...` if half done).
- Save the .blend before staging it.
- After every push, confirm `git status` shows the branch up to date with `origin`. If a push fails, stop and tell the user immediately.

**Stage only your own files.**

- The working tree has uncommitted changes that belong to the user (`.DS_Store` files, `assets/blender/dustbin.blend`, `lobby.blend`). Never stage, commit, stash, reset, or discard them.
- Never `git add -A`, `git add .`, or `git commit -a`. Explicit paths only; read `git status` before every commit.
- Never force-push, rebase, amend pushed commits, or rewrite history.

**Keep the repo pushable.**

- No Git LFS. GitHub rejects files over 100 MB and warns over 50 MB. Check the .blend size before each commit. If it nears 50 MB, split kit pieces into their own linked .blend files under `assets/blender/staging_hall_kit/` and continue; only stop if that does not solve it.
- `output/lobby/meshes/` and `output/lobby/previews/` are gitignored (add them if not already). Commit the .blend files, scripts, `layout_meta.json`, docs, and `output/lobby/renders/*.jpg`.
- Never commit `.blend1` backups.

### 7.3 The Express must be riggable later

- Car (moves), shaft and hall (static), doors (their own moving pieces) separated, following `moving_parts_blender.py` pivot discipline.
- Door mechanism animatable with simple constraints or CFrame tweens; record axes and travel.
- Mount points for the Manifest board, floor dial, emergency lights, ceiling grate entry.
- The runtime needs a `CageRoot`, a `ShaftAnchor` with a prismatic axis, and a `Floors` folder of markers; plan the Express's equivalents and record them in `layout_meta.json`.
- Players left behind cannot fall into the pit when the car is gone: plan the edge (gates, rising barrier, or a closing floor).

### 7.4 Roblox specs (verify against current Creator Hub docs)

- Export at 1 Blender unit = 1 stud, transforms applied, FBX plus GLB.
- 20,000 tris hard cap per MeshPart, aim under 10,000. Report tris per piece.
- Modular kit, never the room as one mesh.
- Tiling surfaces use MaterialVariant. Diamond plate is `StudsPerTile = 4` and tiles from face centres, so size floor parts to 4, 12, 20, 28 studs. Unique props use SurfaceAppearance at 1024.
- Single-sided planes do not render backfaces on Roblox; plan collision as separate simple volumes.
- Budget shadow-casting lights for Future lighting.

### 7.5 Blender quirks on this machine (Blender 5.1, Metal GPU)

- The area screenshot tool needs `size_limit_in_bytes` around 300000.
- `execute_blender_code` must set `result` to a dict.
- Operators that need a window context fail right after a file reload; use the data API or bmesh, or a `temp_override`.
- Principled node is `ShaderNodeBsdfPrincipled`; `mesh.use_auto_smooth` is gone in 5.x.
- Start long renders with `INVOKE_DEFAULT` and poll for the file from Bash.
- A light inside a glass bulb needs `visible_shadow = False` on the bulb mesh.

### 7.6 Off limits

- No Roblox uploads and no Roblox Studio work.
- Do not modify anything under `src/`.
- Do not overwrite existing exports in `output/roblox/`.
- No em dashes in any documentation you write.

---

## 8. Final report

When the definition of done in section 3 is met, end with one short report:

- The chosen layout in two or three sentences and why it beat the circle.
- The eight render types from 3.2, as file paths, establishing shot first.
- Key numbers: hall footprint, Express interior, walk distance range across cages, total tris, shadow-casting light count, .blend size.
- Compromises, with reasons.
- The final pushed commit hash.

If you are ever unsure whether it is time to save and commit, it is.
