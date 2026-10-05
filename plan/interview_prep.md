# Interview prep pack: Roblox studio roles

Task C-007 · claude · 5 Oct 2026. For the 60 to 90 minute live technical interview that studios like Uplift run [R1]. API facts were checked on 5 Oct 2026 against Roblox creator-docs commit `9f840b170b3e472c705e035126b45e3e050daed2` and the Luau docs. Tags like [C1] point to the sources at the end. Limits change, so re-check any number before you quote it.

**Answer shape (about 2 minutes):** what it is, how it works, the trade-off, one example from your own work.

## 1. Likely questions

### Networking and server authority

**1. RemoteEvent, UnreliableRemoteEvent or RemoteFunction?**
- RemoteEvent: one-way, reliable, ordered per client and direction, even across instances [C1].
- UnreliableRemoteEvent: no delivery or order guarantee. Drops payloads over 1,000 bytes and sends over the rate limit. Good for high-rate cosmetic state with a sequence number [C1].
- RemoteFunction: client to server only. Each client gets about 500 sends per second per remote event type, shared by all instances [C1].
- Pitfall: server code that waits on InvokeClient. The client can error, leave or never answer [C1].

**2. What survives a trip over a remote?**
- Non-string keys become strings. Avoid mixed or holey tables. Metatables are dropped, functions arrive as nil, tables arrive as copies [C1].
- Instances the receiver cannot see arrive as nil [C1]. Send plain ids and numbers; rebuild objects on the other side.
- Pitfall: sending an object and expecting its methods on the server.

**3. Network ownership: how does it work, what does it cost?**
- The server always owns anchored parts. Unanchored parts near a character go to that client automatically. Override with SetNetworkOwner from the server [C2].
- An owner has full physics authority: teleport, fly, fling, NaN CFrames, skipped Touched events [C2].
- Vehicles: give the driver ownership for feel, then check outcomes on the server. Roblox's server authority model (beta, per its security docs) keeps objects server-owned with client prediction and rollback [C2][C3].
- Pitfall: SetNetworkOwner(nil) everywhere. The docs warn of jittery physics [C2].

**4. How do clients show timed server state (doors, rounds, cooldowns)?**
- Replicate start time and duration once, as attributes. Clients compute progress from workspace:GetServerTimeNow(), which is smoothed and monotonic [C4].
- Property changes and remote events can arrive in either order. Same-type changes, such as two attribute changes, generally arrive in order [C4].
- Client-only posing: Motor6D.Transform is not replicated and is applied in a batch before physics [C5].
- Pitfall: tick() or os.time() on clients (local device clocks), or GetServerTimeNow for reward timers (not secure) [C3][C4].

### Data and session locking

**5. Walk me through a safe player-data lifecycle.**
- One key per player, such as `User_{UserId}`, under the 4 MB per key limit. Load once, keep it in memory [C6][C7].
- Save on an interval (Roblox's sample: 180 s; the docs advise a random first offset), on leave, at purchases and in BindToClose, which gets 30 seconds [C6][C8].
- On a failed load, play with defaults but mark the data so it never saves, and block purchases [C6].
- Pitfall: saving defaults over the real save after a load error.

**6. What is session locking, and why?**
- Two servers holding the same data means one saves stale data: lost progress or duplicated items. Fast rejoins, teleports and slow saves cause it [C6].
- A lock id is written inside the same UpdateAsync that reads the key. Other servers wait. The lock expires unless autosave refreshes it [C6].
- ProfileStore does this. StartSessionAsync asks the old server for a final save first. `Steal` bypasses locks: debug only [T2].
- Pitfall: assuming the PlayerRemoving save always lands before the next server loads [C6].

**7. SetAsync, UpdateAsync and retries.**
- UpdateAsync reads the latest value and reruns your callback if another server wrote first. The callback must not yield; return nil to cancel. It uses read and write budget [C7].
- SetAsync overwrites blindly. Fine for new keys [C7].
- Retry with pcall and capped exponential backoff with jitter, in order per key. A "failed" write may have landed: verify with GetAsync and UseCache = false (the default cache is 4 s) [C6][C7].
- Pitfall: parallel retries that let an old write land after a newer one [C6].

**8. Schema changes, restores and limits.**
- Store a schema version and migrate on load. ProfileStore's Reconcile fills new template keys [T2].
- The first write per key in each UTC hour becomes a version, kept 30 days after it is overwritten. Restore with ListVersionsAsync and GetVersionAsync. Snapshot before releases that change data logic [C7].
- Per key: 4 MB/min of writes, 25 MB/min of reads. Request budgets scale with players; check GetRequestBudgetForRequestType [C7].
- Pitfall: changing the data shape without a version field.

### Performance

**9. A live server lags. How do you find the cause?**
- Developer Console (F9): Server Jobs, Heartbeat, Steps Per Sec. Server heartbeat caps at 60, so frames over 16.67 ms matter [C9].
- MicroProfiler (Ctrl+Alt+F6) on server or client, with debug.profilebegin/profileend labels. Script Profiler for per-function CPU. Performance dashboard for trends [C9].
- Pitfall: optimizing before measuring, or on the wrong side.

**10. Find and fix a memory leak.**
- Take Luau heap snapshots over time and compare them [C9].
- Usual causes: connections never disconnected, per-player tables kept after leave, references to destroyed instances.
- Destroy() disconnects connections and locks Parent; then nil your references [C10]. Workspace.PlayerCharacterDestroyBehavior can destroy old characters and leaving Player objects [C4].
- Pitfall: setting Parent to nil when you meant Destroy().

**11. Many moving things: cut CPU and bandwidth.**
- Replicate state changes, not frames, and animate on clients (your gate story) [C5].
- Instance streaming limits what reaches each client. Client code must tolerate parts streaming in and out [C11].
- Parallel Luau with Actors (no instance writes or require in parallel phases). `--!native` for numeric server code. Measure first [C12].
- Pitfall: Heartbeat loops running while nothing moves.

### Luau language and typing

**12. What does strict mode buy you, and where does it stop?**
- Modes: `--!nocheck`, `--!nonstrict` (default), `--!strict` [L1].
- Types are checked before runtime only. Remote data still needs runtime checks: typeof, ranges, math.isfinite [C22][T1].
- Run `luau-lsp analyze` in CI [T6].
- Pitfall: casting remote arguments with `::` and calling that validation.

**13. Type an OOP class. Which Luau features do you use?**
- A data type, then `export type Account = typeof(setmetatable({} :: AccountData, Account))`, then annotate `self` [L1].
- Fields on the object, methods on the metatable. table.create for known sizes. Avoid getfenv, setfenv and loadstring: they deoptimize [L2].
- Know compound assignment, continue, if-then-else expressions, string interpolation, generalized iteration and `//` [L2].
- Pitfall: leaving `self` inferred, so methods disagree on the type [L1].

**14. task library, deferred events, Promises.**
- task.spawn runs now, task.defer at the end of the current resumption cycle, task.delay later; task.cancel stops a thread. wait, spawn and delay are deprecated [C13].
- Deferred signals run handlers at resumption points. Roblox recommends them, and the default will switch to them [C13].
- Promises: chainable, cancellable async instead of hidden yields [T7].
- Pitfall: code that expects a handler to run the instant an event fires.

### Architecture and tooling

**15. Your Rojo and Git workflow.**
- Files are the source of truth: `rojo serve` plus the Studio plugin. Rokit pins tool versions [C14].
- `rojo sourcemap` feeds luau-lsp [T6]. Branches, pull requests and review. CI runs your check script: format, selene, `luau-lsp analyze` [C14][T6].
- Studio Script Sync syncs scripts only. Rojo fits when the whole project should live in files [C14].
- Pitfall: editing the same scripts in Studio and on disk with no clear source of truth.

**16. Wally dependencies.**
- wally.toml has [dependencies], [server-dependencies] and [dev-dependencies]. Realms are shared and server. wally.lock pins versions; use `wally install --locked` in CI [T3].
- Server-realm packages are for code that should not replicate [T3]. Replicated modules can be decompiled [C24].
- Pitfall: server-only logic in shared packages.

**17. roblox-ts: when, and at what cost?**
- A TypeScript-to-Luau compiler (npm `roblox-ts`, CLI `rbxtsc`). Its README lists live games such as BedWars [T4].
- Gains: TypeScript types, editor tooling, a familiar language. Costs: a build step, debugging emitted Luau, typings for Luau packages, team skills.
- Pitfall: thinking compile-time types remove runtime checks on remote data [T1].

**18. How do you test Roblox code?**
- Pure logic in ModuleScripts with injected dependencies. Jest Lua (runs inside Roblox) or TestEZ [T5].
- Data tests run on ProfileStore.Mock, never live keys [T2].
- CI: Open Cloud Luau Execution runs a script against a place version. No physics, no auto-running scripts, nothing persisted, up to 5 minutes. It can still reach DataStores [C15].
- Studio network simulation (latency, jitter, packet loss) for netcode [C9].
- Pitfall: tests that write to real DataStores.

**19. Your game uses Knit. Would you use it again?**
- Knit is archived. Its author cites weak typing and intellisense. It served two roles: service structure and a networking bridge [T1].
- ModuleScripts cover structure. A thin wrapper over RemoteEvents with runtime checks covers networking [T1].
- Pitfall: defending a framework without naming its costs.

### Monetization and live-ops

**20. Implement ProcessReceipt and make it idempotent.**
- Set it once, in one server Script, for all developer products, including Store-tab purchases made outside the game [C16].
- It runs when a purchase completes and when the buyer joins with unresolved receipts. No timed retries. It can run on two servers at once, and PurchaseGranted can still fail to record [C16].
- Flow: wait for session-locked data (stop if the player leaves). If the PurchaseId is recorded and saved, return PurchaseGranted. Otherwise grant, record the PurchaseId, save. Return PurchaseGranted only after the save succeeds, else NotProcessedYet [C6].
- Pitfall: granting on PromptProductPurchaseFinished. It can be spoofed [C16][C22].

**21. Passes, products and policy.**
- UserOwnsGamePassAsync is cached; PromptGamePassPurchaseFinished refreshes it [C16].
- Paid random items: show every outcome with numeric odds totalling 100%. Check PolicyService:GetPolicyInfoForPlayerAsync (ArePaidRandomItemsRestricted, IsPaidItemTradingAllowed) [C17].
- Pitfall: a paid random reward with no odds or policy check.

**22. Live config and A/B tests.**
- ConfigService (server only) returns a ConfigSnapshot. Snapshots do not auto-update: call Refresh on UpdateAvailable at safe points, such as between rounds [C18].
- Publish now (about 15 s to 1 min) or over 15 minutes. History can restore. GetConfigForPlayerAsync applies targeting [C18].
- Experiments test config values: up to two variants plus control, for 14 to 60 days. Measure with AnalyticsService (LogEconomyEvent, LogFunnelStepEvent, LogCustomEvent) [C18].
- Pitfall: no code default when GetConfigAsync throws on a first load [C18].

### Security against exploiters

**23. What can an exploiter do? Secure a remote.**
- They fire any remote with any arguments (except the Player argument), decompile replicated LocalScripts and ModuleScripts, own their character, and fire ProximityPrompt and ClickDetector events from any range [C22].
- Validate in layers: permission and context; type and structure (typeof, IsDescendantOf, string length, utf8.len); values (ranges, math.isfinite); then a per-player token bucket, cleared on leave [C22].
- The server is a gatekeeper, not a relay [C22].
- Pitfall: NaN passes `typeof(x) == "number"` and fails every comparison [C22].

**24. Speed or teleport cheats: detect and respond.**
- Check distance over time with latency tolerance. Project to XZ. Use leaky-bucket accumulators. Exempt real teleports [C2].
- Respond quietly first: rubber-band to the last valid position. Build a suspicion score from several heuristics, delay visible action, and use the Ban API for repeat offenders [C23].
- Honeypot remotes that no real client fires are a strong signal [C23].
- Pitfall: kicking on one signal. Laggy players will trip it.

**25. What leaks to clients?**
- Anything replicated, including unreleased content. Clients can teleport to any place in the universe unless access is "Secure within universe only" [C24].
- Keep server code in ServerScriptService or ServerStorage, never in shared modules. Keys go in the secrets store [C24].
- Toolbox models can hide backdoors. Inspect them; Capabilities sandboxing is in beta [C24].
- Pitfall: kicking from a test place after join. The content has already replicated [C24].

## 2. System design prompts (rehearse out loud)

Cover requirements, server authority, data and failure modes, scale and testing. Take 15 to 20 minutes each.

**A. Item trading that cannot duplicate.**
- Same-server trades first. Both profiles are session-locked on this server [C6][T2].
- Server state machine: open, both ready, countdown, commit. Any change resets ready. Rate-limit, and validate every offer against server inventory [C22].
- Items carry unique ids (HttpService:GenerateGUID) [C25]. Commit with no yield between remove and add. Write the trade id into both profiles, then save both. Writes are not atomic across keys, so the trade id makes a replay detectable [C6].
- Cross-server gifts: ProfileStore MessageAsync (UpdateAsync-backed), not MessagingService, which is best effort [T2][C19].
- Follow-ups: one save fails; now what? How do you find dupes already in the economy? How would a cross-server auction work (MemoryStore sorted map) [C20]?

**B. Cross-server timed event.**
- Put the start time in config so every server agrees without messages. Clients count down with GetServerTimeNow [C18][C4].
- MessagingService for live news: usually 1 to 2 s, best effort, 1 kB messages. Treat it as a hint; servers also poll [C19].
- Global counter: MemoryStore hash map with sharded keys and UpdateAsync. Each key allows about 5,000 write units a minute [C20].
- Memory stores are not durable. Use short expirations; the quota is 64 KB + 1.2 KB per user. Final results go to DataStores [C20].
- Rewards are keyed by event id in the player's profile, so server hops cannot double-claim.
- Follow-ups: a server misses the start message? How do you avoid a hot key? A player hops servers mid-event?

**C. Round-based game server.**
- One server module owns the phases: waiting, intermission, loading, playing, results, cleanup. Phase and end time replicate as attributes [C4].
- CharacterAutoLoads off; spawn with LoadCharacterAsync [C21]. Mid-round joiners spectate. Leavers trigger a win check.
- All round objects live under one container and are destroyed at cleanup [C10].
- Rewards are granted at results, idempotent per round id, and saved through the profile.
- Matchmaking: TeleportAsync with TeleportOptions.ShouldReserveServer (ReserveServer is deprecated). Retry, and handle TeleportInitFailed [C21].
- Follow-ups: the round loop errors halfway? Twenty maps without memory growth? How do you test it?

**D. Live-ops config system.**
- Experience Configs hold flags, tunables and timed content. Every key has a code default [C18].
- Validate types and ranges before use. Send clients only what they need.
- Apply updates at safe points (UpdateAvailable, then Refresh). Roll out over 15 minutes; roll back from History [C18].
- Targeting and experiments for A/B. Log the config value with analytics events [C18].
- Without Configs: one DataStore key plus a MessagingService nudge, and polling with jitter [C6][C19].
- Follow-ups: a bad value starts crashing servers? Give 10% of players a new price and measure it? Config fails at server start?

**E. Server-authoritative combat hits.**
- The client plays animation and effects at once, then sends intent: weapon id, origin, direction [C22].
- Server checks: alive, equipped, cooldown and ammo tracked on the server, rate limit, finite numbers [C22].
- Server hit test (Raycast, Spherecast, Shapecast or GetPartBoundsInBox), or verify the client's claim: origin near the character, hit near the target, no static geometry between [C25][C22].
- Damage comes from server weapon stats only [C23]. Rewind targets a little, using Player:GetNetworkPing() with a cap [C21].
- Follow-ups: how much rewind is fair to the victim? Projectiles versus hitscan? An aimbot that sends only valid shots?

## 3. Your stories (owner to confirm each)

Built from `games/stygian-drop/source/README.md` [O1], the README of your own game repo. Nothing here proves the code exists. Confirm every line and add real results. Never invent metrics.

1. **Load-gated join (data reliability).** S: gameplay could start before data or assets loaded. T: make joining deterministic. A: CharacterAutoLoads is off. A ReplicatedFirst loading screen preloads while the server opens a session-locked ProfileStore profile. The player counts as loaded only when both finish. Services gate on ObservePlayerLoaded, which replays already-loaded players. Clients that never report ready are kicked after 180 s. Studio uses the Mock store. R: owner to add.
2. **Gate replication (networking, performance).** S: a scissor gate of 288 pieces. A: the server replicates each sweep once, as four attributes. Clients derive progress from the server clock and pose the pieces through Motor6D.Transform. The server moves only a collision slab. Late joiners rebuild from the attributes. R: one attribute batch plus a bounded collider update, not 289 weld poses per Heartbeat (your 18 Sep 2026 analysis).
3. **Elevator API (API design, safety).** A: objects are built from CollectionService tags. Every action returns a Promise and never yields the caller. Interlocks: Ascend rejects while the gate is open. No per-frame work while idle. Clients get read-only queries. R: owner to add.
4. **Vehicle drivetrain (physics, ownership).** A: a per-wheel model (contact, load transfer, friction circle, Ackermann steering) drives a planar LinearVelocity and a yaw-only AlignOrientation on the driver's client. VehicleService owns seats and network ownership. Be ready for: what does the server check, given the driver owns the car [C2]?
5. **Toolchain (team readiness).** A: Rojo 7.7.0, Wally, Rokit-pinned tools, one check script (format, selene, strict luau-lsp) and Studio-only scenario tests that confirm Studio runs the code on disk. R: owner to add.
6. **Client work (placeholder).** Project, permission to mention it, your role, the problem, results with numbers (CCU, visits, bugs fixed), link.

## 4. Five-session prep plan (60 minutes each)

1. **Networking and security.** Read [C1][C2][C22]. Answer questions 1 to 4 and 23 to 25 aloud, 2 minutes each, recorded. Note the gaps.
2. **Data and money.** From memory, in strict Luau, write a session-locked save flow and a ProcessReceipt handler (30 min). Compare them with Roblox's sample [C6]. Answer 5 to 8 and 20 to 22 aloud.
3. **Luau, performance, tooling.** Write a typed token bucket with tests (25 min). Profile one hot path in your game with the MicroProfiler (15 min). Answer 9 to 19 quickly.
4. **System design.** Prompts A and E aloud, 20 minutes each, then their follow-ups. Sketch on paper.
5. **Mock interview.** A friend, or an AI agent if you prefer, plays interviewer. 15 min: explain the gate replication or the join flow aloud, with a diagram. 20 min: random questions from part 1. 20 min: one unseen prompt (B, C or D). 5 min: feedback. Record it and redo the two weakest answers.

Before each real interview, check the job post's stack (Rojo, roblox-ts) and re-check any limit you plan to quote.

## Sources

All checked 5 Oct 2026.

**Roblox creator-docs**, github.com/Roblox/creator-docs commit `9f840b170b3e472c705e035126b45e3e050daed2`. Paths under `content/en-us/`:
- [C1] `scripting/events/remote.md`; `reference/engine/classes/RemoteEvent.yaml`, `UnreliableRemoteEvent.yaml`
- [C2] `physics/network-ownership.md`; `scripting/security/network-ownership.md`
- [C3] `projects/server-authority/index.md`
- [C4] `reference/engine/classes/Workspace.yaml`; `scripting/attributes.md`
- [C5] `reference/engine/classes/Motor6D.yaml`
- [C6] `cloud-services/data-stores/best-practices.md`, `player-data-purchasing.md`
- [C7] `cloud-services/data-stores/index.md`, `error-codes-and-limits.md`, `versioning-listing-and-caching.md`; `reference/engine/classes/GlobalDataStore.yaml`
- [C8] `reference/engine/classes/DataModel.yaml`
- [C9] `performance-optimization/identify.md`, `performance-optimization/microprofiler/index.md`; `studio/developer-console.md`
- [C10] `reference/engine/classes/Instance.yaml`
- [C11] `workspace/streaming/index.md`
- [C12] `scripting/multithreading.md`; `luau/native-code-gen.md`
- [C13] `scripting/events/deferred.md`; `reference/engine/libraries/task.yaml`; `reference/engine/globals/RobloxGlobals.yaml`
- [C14] `projects/external-tools.md`; `scripting/sync.md`
- [C15] `reference/cloud/openapi.json` (LuauExecutionSessionTask)
- [C16] `reference/engine/classes/MarketplaceService.yaml`; `production/monetization/developer-products.md`
- [C17] `production/monetization/paid-random-items.md`
- [C18] `production/configs.md`, `production/experiments.md`; `reference/engine/classes/AnalyticsService.yaml`
- [C19] `reference/engine/classes/MessagingService.yaml`
- [C20] `cloud-services/memory-stores/index.md`
- [C21] `projects/teleport.md`; `reference/engine/classes/TeleportService.yaml`, `Players.yaml`, `Player.yaml`
- [C22] `scripting/security/security-tactics.md`, `client-server-boundary.md`
- [C23] `scripting/security/server-side-detection.md`, `defensive-design.md`
- [C24] `scripting/security/access-control.md`, `third-party-vulnerabilities.md`; `cloud-services/secrets.md`
- [C25] `reference/engine/classes/WorldRoot.yaml`, `HttpService.yaml`

**Luau docs**, github.com/luau-lang/site commit `a60a62708901b1b7774518e2af9719e9efe678e0`. Paths under `src/content/docs/`:
- [L1] `types/overview.md`, `types/object-oriented-programs.md`
- [L2] `getting-started/syntax.md`, `guides/performance.md`

**Third-party tools** (GitHub, at the commit shown):
- [T1] Sleitnick/Knit `README.md`, `ARCHIVAL.md` @ `bb1ecf3dea69ca89147b9abe802a8c14399cb5e5`
- [T2] MadStudioRoblox/ProfileStore `docs/api.md` @ `45c9847cbcf1fc260369c50eb335aba7c35aecdd`
- [T3] UpliftGames/wally `README.md` @ `4a9d53ea9d8cddf2065bdf177f8d3e7c75babc9d`
- [T4] roblox-ts/roblox-ts `README.md`, `package.json` @ `68648b0c633ef1016009aec7521b528f648ba656`
- [T5] jsdotlua/jest-lua `README.md` @ `a5d089ab06021a931f9bb3df9cbc7b5154da8a7b`; Roblox/testez `README.md` @ `26a5247631279154c74425b94583c189b8447d0f`
- [T6] JohnnyMorganz/luau-lsp `README.md` @ `9024d56b36e03df195a18df6207358ab9c3bd269`; rojo-rbx/rojo `src/cli/sourcemap.rs` @ `95262a02e96aabd02ff455142cb1414d55be0dd8`
- [T7] evaera/roblox-lua-promise `README.md` @ `031d429c82ee458a849e79fa523523bd349d7695`

**This repo:**
- [R1] `research_notes/Roblox scripter income strategies/studio_jobs_contracts.md`, section 3 (from search excerpts, not re-checked here)
- [O1] `games/stygian-drop/source/README.md` (copy of your game's README; the code is in a separate repo; owner to confirm)
