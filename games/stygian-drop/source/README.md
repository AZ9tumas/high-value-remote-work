# Stygian Drop

Roblox game built with [Rojo](https://rojo.space) 7.7.0 + [Wally](https://wally.run) + [Knit](https://sleitnick.github.io/Knit/).
Vehicle Lift 04 and the expanded P3 basement are now installed in Studio with the existing OOP/Knit setup.
See [the integration guide](output/studio/README.md) for the playable place, object APIs, reusable sections,
lighting and verification. The original mine hoist remains supported and is preserved in ServerStorage.

## Setup

```sh
./scripts/setup.sh
```

Runs `rokit install` (toolchain pinned in `rokit.toml`), `wally install` (packages pinned in
`wally.lock`), regenerates `sourcemap.json`, and re-exports package types. Re-run after every
`wally install`.

Day-to-day: open the place in Studio, run `rojo serve`, connect the Rojo plugin. Format with
`stylua src/`, lint with `selene src/`. `./scripts/check.sh` is the full quality gate (format,
lint, strict `luau-lsp` analysis).

Without the Rojo plugin (for example from an automated session) `tools/inject_tree.py` builds the
tree and pushes it into the open place over a local HTTP server; see the header of that file.

## Layout

```
src/
  ReplicatedFirst/      Bootstrap.client (loading screen up before anything replicates)
  ReplicatedStorage/    Configs/ (ElevatorConfig), Assets/ (preloaded on join)   + Packages/ (wally)
  ServerScriptService/  Runtime.server, ProfileTemplate, Services/, Modules/     + ServerPackages/
  StarterPlayer/        StarterPlayerScripts/Runtime.client, Controllers/
output/roblox/          Blender -> Roblox pipeline: bake tools, wiring script, rig metadata
```

Knit everywhere: server **Services** in `src/ServerScriptService/Services/`, client **Controllers**
in `src/StarterPlayer/StarterPlayerScripts/Controllers/`. The `Runtime.*` scripts auto-load every
module in those folders; drop a module in and it runs.

Movement: hold **Shift** (gamepad L3, or the touch button) to sprint. `SprintService` owns the
authoritative speeds, `SprintController` the input, and `Configs/MovementConfig` every number.
Walking shows no arms at all: the viewmodel rests below the frame. Sprinting raises it into a
procedural athlete's pump (`StygianViewmodelKit/RunCycle`, same bone space as the Blender clips)
and adds head bob, sway, roll, a forward lean and a wider FOV, all locked to real ground speed.

Driving: the 19 vintage cars in `Workspace.VintageCars` (tagged `VintageCar`) are drivable. Walk
to the driver's door (right-hand side) and press **E** (gamepad X, or tap the prompt).

- **W/S** or the stick drive and brake (holding S at a stop reverses), and **A/D** steer.
- **Shift** is the handbrake, **V** switches between the seat view and a chase view, and **Jump**
  gets out beside the car.

Motion comes from body movers, not tyre friction. A planar LinearVelocity (no control along the
road normal) and a yaw-only AlignOrientation are set each physics step by a per-wheel model in
`Vehicle/Drivetrain`: ground contact, load transfer, grip and friction circle, rear-wheel drive,
four-wheel brakes, Ackermann steering, understeer and handbrake slides.

- `VehicleService` (with `Modules/Vehicle`) owns seats, network ownership, lamps and parking.
- `VehicleController` runs the model on the driver's client and handles both views.
- `Configs/VehicleConfig` holds every number.

Saved cars stay anchored and parked. Details: `output/vintage_cars/README.md`.

Studio-only verification tooling (inert in live games): `ServerStorage/AgentTools`,
`ServerStorage/AgentScenarios`, `ServerScriptService/AgentBridge.server` and
`StarterPlayerScripts/AgentProbe`. They run playtest scenarios that return one bounded server and
client report, including a check that Studio is running the code on disk
(`scripts/agent_manifest.py`). Workflow: `.claude/skills/studio-verify/SKILL.md`.

## Join flow

```
player joins ──┬─ client: loading screen (ReplicatedFirst) → preload → ClientReady
               └─ server: ProfileStore session (PlayerDataService)
both done ───── LoadingService marks the player loaded
                ├─ client gets LoadingComplete → screen fades → GameStarted
                └─ server fires PlayerLoaded → CharacterService spawns the character
```

- `Players.CharacterAutoLoads` is off: no character exists until loading completes. Respawns are
  manual (`Players.RespawnTime` is the delay).
- Gameplay services gate on `LoadingService:ObservePlayerLoaded(cb)` (replays already-loaded
  players, so it can never miss one). Controllers gate on `LoadingController:ObserveGameStarted`.
- `PlayerDataService` owns one session-locked ProfileStore profile per player. Studio playtests use
  the in-memory Mock store and never touch live data.

## Elevators

The current place uses `workspace.VehicleLift04`, key `"1"`, with `P2` and `P3` landings.
`lift:Open({ entrance = "Rear" })` selects its rear entrance; `lift:Close()` closes both faces.
Vehicle Lift 04 never permits forced opening during travel or travel with doors open.
The examples below describe the retained legacy hoist. See the integration guide above for the new rig.

`ElevatorService` finds every model tagged `Elevator` (CollectionService) and builds an `Elevator`
object (`src/ServerScriptService/Modules/Elevator.luau`) for it, keyed by the model's
`ElevatorKey` attribute (`"1"`, `"2"`, ...).

```lua
local ElevatorService = Knit.GetService("ElevatorService")
local lift = ElevatorService:FetchElevator(workspace.HoistCage_No2_Mesh)   -- or FetchElevator("1")

lift:Close():andThen(function()
    return lift:MoveToFloor("Lower level")           -- index, name or marker Part
end)
lift:Descend({ closeGate = true })                   -- close first, then one floor down
lift:Ascend()                                        -- rejects while the gate is open
lift:Open({ force = true })                          -- gate moves even mid-trip
lift:Stop()                                          -- emergency hold
lift.FloorReached:Connect(function(index, name) end)
```

Every action returns a Promise and never yields the caller. Floors are marker Parts in the model's
`Floors` folder (Y = stop height, Name = label). Speeds are attributes on the model (`Speed`,
`RampTime`, `GateTime`, `GateColliderRate`, `LeverTilt`, `LeverTime`), read live. Nothing runs per
frame while a cage is idle. See `output/roblox/HOIST_README.md` for the physical model and how to
add floors.

The scissor gate is server-authoritative but client-animated. A sweep replicates once, as four
attributes on the model (`GateFrom`, `GateTo`, `GateStart`, `GateDuration`; see
`ReplicatedStorage/Elevator/GateMotion`), and `ElevatorController` on every client derives the
progress from the server clock and poses the 288 pieces through `Motor6D.Transform`, which never
replicates. The server moves only the collision slab, at `GateColliderRate` per second. Late
joiners rebuild the pose from the same attributes. The rig numbers live in
`ReplicatedStorage/Elevator/Rigs/`, generated by `output/roblox/make_hoist_script.py`.

## Scale notes

- Data: ProfileStore session locks (one writer per player, ever), batched saves, Mock in Studio.
- Join: both halves of loading are asynchronous and per-player state is a flat table cleared on
  leave; a client that never reports ready is kicked after 180 s.
- Remotes: clients only ever fire `ClientReady` (at-most-once) and read-only elevator queries; all
  elevator control is server-side.
- Elevators: no idle per-frame work, one Heartbeat connection per moving cage, and a gate sweep
  costs the network one attribute batch plus a bounded collider update, not 289 weld poses per
  Heartbeat (`output/performance/gate-close-analysis-2026-09-18.md`).

## First-person viewmodel

The complete Ferryman's graft arms and black leather gloves are in
`assets/blender/viewmodel.blend`, with the native model and skin/pose modules under
`src/ReplicatedStorage/Assets/StygianViewmodelKit`. The standalone `Viewmodel.client.luau`
mounts one camera rig after character spawn, locks first person, and handles respawns.
The uploaded assets are installed in the open Studio place: press Play; **E** on the scissor
gate plays the Blender-authored reach/grip/release for opening or closing it. The arms stay
steady during movement; no walk/run animation or Shift sprint is installed. **G** toggles
grip and **H** toggles inspection. See the [asset guide](output/viewmodel/full/README.md)
for files, rig structure, independent skins, budgets, tests and a saved playable place.
