# Stygian Drop: design critique of v0.2

By claude, 5 October 2026. Reviews `source/STYGIAN_DROP.md` v0.2. Numbers cite their file in `research_notes/Roblox scripter income strategies/`. Claims from memory are marked (unverified).

## Verdict

The mood is right and the assets are rare: a finished hands rig, real coupled doors, 19 drivable cars. But the loop has a leave and a return, no clock and no prices, so careful play is safe and dull. US$3,000 a month needs about 300 to 600 average CCU at co-op survival rates of $5 to $10 per CCU-month (own_games_economics.md §1, §2). Only retention gets there. Four changes do most of the work: a clock on every stop, the doorway as a decision, progress banked when the doors close, and a first three minutes rebuilt for Roblox.

## 1. Fantasy, loop and decisions

**Core fantasy, as implied:** you leave the only safe room on purpose, do one small job with your hands in a place that should not exist, and make it back before something notices.

**Core loop, as implied:** descend, the doors open, step out for a required or optional reason, get back in, watch the doors close, recover on the way down.

**Is the fun clear?** The feeling is; the fun is not. Structurally this is a micro-extraction loop, like Lethal Company or R.E.P.O. (unverified): leave a safe vehicle, take what you can, get back. The doc has the leave and the return but not the take. Staying out costs nothing and loot is worth little, so "I could go back now, but..." has no price on either side.

**Where the decisions are:** greed (one more thing past the ramp), reading a threat (torch off for the Attendant) and the hands (committing to a timed action). Greed is unpriced, threats appear only on some stops, and hand actions are rare. Between them, the verb is walking.

## 2. Seven weaknesses, with fixes

### W1. No clock and no counterplay

**Risk.** Nothing defines "notices". The torch is generous, the lift waits and threats are optional rolls, so the best strategy is to creep. Door timing only bites when something can reach the doorway inside the close time (the brief targets 3.5 to 5 s, `source/elevator_blender_prompt.md` §5). The M1 test has no threat, so it measures novelty, not the mechanic. And with no weapons and no tools, knowledge has nothing to act through.

**Fix.**

- **The floor wakes up.** Three stages per stop: quiet, stirring, awake. Time outside, light, carried noise and cancelled hand actions raise it. Each threat has one behaviour per stage, and at "awake" it heads for the lift, so every return has a threat in it. Threat-free stops lose their lights instead. Players read the stage from the world (the ventilation stops, then emergency lighting), not a UI bar.
- **The gap is the timer.** A person fits through a gap that a crate does not, and players learn where that point is. Decide per threat whether it trips the light curtain. The one that does is your scariest.
- **Test it properly.** Run M1 twice: as written, and with something harmless moving far off as the doors close. If players behave the same, timing alone is not the hook.
- **Tools bend a rule, never kill.** Flares pull the Attendant. Thrown bolts splash to pull the Leak. Chalk stencils mark cars checked for the Occupant. A parked car's headlights watch Headlights for you, but only with its loud engine running. Found on floors, never sold.

### W2. The first minutes are built for Steam, not Roblox

**Risk.** The first stop is a 3 to 5 minute slow burn, and ranking penalises exits in the first 60 to 180 seconds (own_games_economics.md §4). It is solo, but friends arrive together, and co-play days are ranked too. Checkpoints 20 to 30 minutes apart let one wipe erase a session. On phones, dark scenes are hard to read and low settings can drop shadows (unverified).

**Fix.**

- **Cold open in the moving car,** party included. By second 20, something is off: the display reads P3, but the car keeps sinking a beat before it levels. Doors open by second 40, the note is visible from the doorway, and the car light lands by minute 2. Same slow burn, half the clock, no scare.
- **Bands of 6 stops,** about 12 to 15 minutes, each ending at its checkpoint. Two make a 30-minute session; sessions of 19+ minutes go with double-digit D1 (own_games_economics.md §1).
- **Mobile:** one context button, hold-to-act on a big ring, a "glance back" button that turns the head 180 degrees, and brightness calibration at first launch. Compute stealth on the server from simple geometry, never from what a client renders.

### W3. Ten parking stops will look the same by stop four

**Risk.** Purposes are fetch tasks, and layout rolls change corridors, not decisions. Four threats across 40 stops run thin.

**Fix.**

- **Players pick the next stop.** Two buttons light, and their halos hint at the condition: flickering means lights out, buzzing means alarms. Choosing your risk is agency without weapons.
- **Situation cards.** 20 to 30 authored stops that twist a known rule: the Attendant with every light on, the objective across an open deck, the **rear** doors opening instead of the front (already rigged, `source/README.md`).
- **It is a vehicle lift. Use the cars.** Some stops ask you to drive a vintage car onto the lift, such as the person's own car with the next note in the glovebox: headlights in the dark, an engine that wakes the floor. I know of no elevator game that does this (unverified), and the systems exist.
- **Revisits.** A known floor comes back changed, so the baseline rule (section 7) pays off across runs.

### W4. Nothing persists between runs

**Risk.** Progression is one word in M4. Median D7 is 1.6% (own_games_economics.md §1), and a game whose only saved state is a checkpoint will sit below it.

**Fix.** One rule: **when the doors close, it is yours.** Notes, trophies and fares in the car at departure are banked, even if the run later wipes. Every close becomes a save, and greed gets its price. Structure in section 4.

### W5. Death and solo are unsolved

**Risk.** A downed player whose team moves on waits up to 30 minutes. Solo players cannot be revived or split attention, and Headlights is near impossible while your hands are in a cabinet.

**Fix.**

- **Downed means a 45 s bleed-out.** A teammate can carry you as a bulky item: both hands, no torch.
- **The fare returns as the revive.** If you are left behind and anyone spends a fare (an old coin), you are standing in the car when the doors open at the next stop: the doc's own care example (section 3), applied to people. One per player per band. Found, granted daily, and sold, which section 13 allows because it is earnable. Evade and Dead Rails both sell revives (own_games_economics.md §3, §6).
- **Spectators** ping one thing every 20 s.
- **Solo:** the lift always waits, one free fare per band, and Headlights moves only while your hands block your view. Section 6's design question becomes the solo rule.

### W6. The co-op rules are undefined, so griefing is easy

**Risk.** "Should the lift wait for everyone?" is still open (section 15). One player can close the doors on others, stand in the light curtain, drop a crate in the doorway or go AFK outside.

**Fix.**

- **Closing is not leaving.** Anyone can close the doors. The car leaves only when every standing player is inside, or when everyone inside holds the floor button together for 3 seconds. Leaving someone is a choice the whole car makes. A lift that leaves on its own is an authored beat, once per run at most.
- **Nudging caps door griefing,** and it is already built. 60 s idle outside counts as left behind.
- **Party first:** friends and cheap private servers; public lobbies second.
- **Stencils, not free drawing.** Roblox restricts free-form creation to players over 16 (platform_economics_payouts.md §6).

### W7. The mystery has no delivery plan

**Risk.** Random care moments will read as lag, as the doc fears. Notes get skipped. The story is undecided, so clues cannot agree, and theory videos need clues that agree.

**Fix.**

- **A care director, not dice.** Each beat answers something a player just did (you ran back, so the doors waited), fires only when that player is looking, never repeats in a session, and comes at most once per 10 minutes, rarer later.
- **The service log.** The faded inspection card on the panel fills in after each run: "Door dwell exceeded rating by 1.8 s. Cause not found." It confirms intent without explaining it, and it is a collection.
- **Write the truth now,** one private page before M2, so every clue agrees.
- **Story in objects.** Fragments under 15 words: tickets whose times run backwards, the person's car on every checkpoint floor, more wrong each time. One reveal per checkpoint. Each band ships as an update, and updates bring a spike of recommended players (own_games_economics.md §4). The mystery is the content calendar.

## 3. Protect these

1. **The refuge rule.** Nothing enters while the doors are shut, and the car is the same every run. Trusting it is what makes leaving a choice. Never break it, even for a reveal.
2. **Understandable threats, mysterious place.** Skill brings players back; mystery makes them talk. Rules are also cheaper to build than clever AI.
3. **The hands question.** It turns the finished viewmodel into gameplay, where most Roblox interactions are a prompt and a progress bar. One or two per stop keeps it special.
4. **Real doors.** Coupled doors, a light curtain and nudging are physical, readable and full of co-op uses. Add no magic beyond the rare care beat.
5. **Discipline.** One threat per stop, quiet baselines, gates, analytics from day one, no paid random items. Scarier, cheaper for one developer, and clean for a 16+ launch.

## 4. Retention and meta-progression

| When | What brings them back |
|---|---|
| Second run, today | The end screen shows what was banked, one new log line, and the button you did not press. "Ride again" keeps the party, with no lobby walk. |
| D1 | The **Daily Drop**: one seed for everyone (section 12 already has seeds), one modifier, a depth board. The first run of the day grants a fare. A log entry with a blank you fill by surviving that threat again. |
| D7 | Checkpoints become start floors. Weekly updates: a situation card, a threat variant, a note. A Saturday "Deep Shift" event, since play peaks on Saturdays (own_games_economics.md §4). |

**Meta-progression:** three tracks and one currency. Nothing sold makes a threat harmless or the lift faster.

| Track | Earned by | Gives | Sold? |
|---|---|---|---|
| Depth | Reaching checkpoints | Start floors; tools found deeper | No |
| The Log | Surviving threats, banking notes, care beats | How to survive each threat, never what it is; glove details for full pages | No |
| The Car | Carrying trophies out (a coat, a sign, a stopped clock) | Permanent objects in your spot in the car: one hook and one shelf per player | Trophies no; extra objects and hand skins yes |
| Fares | Floors, first daily run, banked trophies | Revives (capped), cosmetics | Yes, and always earnable |

Trophies are bulky, so the best ones cost real nerve. Your spot becomes a record of what you dared, friends see it, and the oversized car slowly fills. A party starts from the deepest checkpoint everyone has, and a veteran riding with a newer friend earns a fare, so your best players recruit. With payer conversion near 3.80% (own_games_economics.md §1), keep the paid layer cheap and repeatable; spend days are ranked too (§4). Add a season track only once D7 is stable (§6).

**Recalibrate the gate.** D1 above 25% beats Roblox's illustrative top-10% figure of 18.73% (median 12.11%, own_games_economics.md §1). Keep 25% as the hope, stop below the similar-games median in Creator Analytics, and add D7 above 3%, about double the 1.6% median.

## 5. Co-op

### Moment 1: The Hold

At a "lift will only wait so long" stop, the doors start closing when dwell ends. A player inside can hold Door Open, which keeps the hall lantern lit, but after about 10 seconds the lift starts nudging. The runner returns with a crate in both hands: no torch, low view. The holder sees what is behind the runner; the runner does not. The call is "keep coming" or "drop it", and the gap enforces it. A dark lantern says "drop it" without a word.

### Moment 2: The Watch

Headlights moves only when no one is looking, and the job needs both hands in a cabinet. One player watches, one works. With four, deal two cars: two watchers, a worker, a carrier. Hold the ping key on a car and teammates see an eye on it. When the eye drops, someone must pick it up. The panic is two watchers turning at the same sound.

### Moment 3: The Operator

Dealt only with two or more players. The landing's call panel is dead, so one player stays in the car and runs the doors. The operator sees the landing; the team sees the floor. Opening for friends with something behind them opens the doors for it too, for about 3 s to open and 4 s to close. Without voice, the operator rings the arrival chime: once for "come", twice for "stay away". The chime is loud and wakes the floor. Talking has a price.

These are your clips. Roblox's Moments are short videos that launch straight into the game (own_games_economics.md §4), and a crate left in a closing gap is a perfect one.

### Proximity voice under 2026 rules

Chat has needed an age check worldwide since January 2026, and only 51% of global DAU (65% in the US) had one by the end of Q1 (own_games_economics.md §4). New games launch to an age-checked 16+ audience (platform_economics_payouts.md §6). Voice also needs 13+, a check and an opt-in, and parents can switch it off (unverified). Expect mixed lobbies. **Support it, never require it.**

- Let the lift shape the sound: clear in the closed car, muffled through closing doors, proximity on the floor. A door cutting off a friend mid-word is the best sound in the game.
- Every co-op mechanic must work with pings, stencils, the lantern and the chime.
- Threats ignore microphones at launch, or the players who can talk are punished. Try it later as an opt-in private-server mode.
- Upside: US players over 18 spend about 50% more (own_games_economics.md §4), and the US 18+ DevEx rate needs R15 characters for all playtime (§1). Keep teammates R15.

## 6. Pillars

Stygian Drop is co-op horror about leaving the only safe room on purpose. **The car is home:** Vehicle Lift 04 is the same every run, nothing reaches you inside while the doors are shut, and what you carry in is yours. **The doorway is the decision:** every stop ends at a door that takes real seconds to close, and the team decides who and what makes it through the gap. **Learn the rule, never the reason:** each threat obeys one readable rule, and nothing explains what it is. **Your hands are the risk:** every useful action costs your view, your light or your speed, so friends cover for you. **One more stop:** something worth having always sits just past safe, and how far you stray is the game.

The doorway pillar survives even if the timing hypothesis fails: holding, dropping and leaving are still decisions.

**Sources:** `source/STYGIAN_DROP.md` (v0.2), `source/README.md`, `source/elevator_blender_prompt.md`, `own_games_economics.md` (§1 to §4, §6), `platform_economics_payouts.md` (§6).
