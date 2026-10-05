# Market lens: Stygian Drop

Market and audience analysis of design doc v0.2 (`source/STYGIAN_DROP.md`). Idea only. 5 October 2026.

**Sources.** [OGE] = `own_games_economics.md`, [PEP] = `platform_economics_payouts.md`, both in `research_notes/Roblox scripter income strategies/`. Other games are from memory. Numbers and recent events I could not check are marked (unverified).

**In short:** the right loop, with the wrong intro and title, and no return engine yet.

---

## 1. Comparables

| Game | Hook and loop | Why it spread | Money | Take / avoid |
|---|---|---|---|---|
| **DOORS** (2022) | 100 numbered hotel rooms. Scan, loot, survive entities whose tells you learn | Screaming YouTube runs. Named, drawable entities (Rush, Seek, Figure) | Knobs currency, Robux revives | Take: learnable tells, revives. Avoid: its rooms, names and UI |
| **Pressure, Grace** | DOORS-style room runs: deeper into a sea-floor facility, or entities that each demand one exact reaction | Sold as "the next DOORS". Skill clips | Currency, items, cosmetics | That lane is taken twice. Take: depth as progress, one-rule threats. Avoid: being the third |
| **Regretevator** | An elevator stops at strange floors with odd characters. Half horror, half comedy | Meme characters (Gnarpy) fed fan art | Cosmetics, passes | Take: characters people draw. Avoid: whimsy, random floors |
| **The Normal Elevator** and kin | Ride. Doors open on a random scenario. Survive, ride again | A decade-old format kids know on sight | Passes such as pick-a-floor | Take: "elevator" reads instantly. Avoid: "The ___ Elevator" names, doors-plus-monster thumbnails |
| **Piggy** (2020), **The Mimic** | Chapters. Find items, escape a killer, survive big authored scares | YouTube reactions. A face kids know | Skins, traps, passes | Take: a recognisable threat sells icons and skins. Avoid: kid tone, a chapter treadmill one person cannot feed |
| **Apeirophobia** | Backrooms levels: navigate, solve, escape | Rode the Backrooms wave | Passes | Take: one Backrooms band at most. Avoid: yellow wallpaper up front, mazes on phones |
| **99 Nights in the Forest** (2025) | Survive 99 nights. Gather by day, keep the fire lit, hold off a stalker with light | Friend groups. 14.15M CCU record [OGE §3] | Classes for premium currency | Take: progression friends return to daily. Avoid: thinking its scale came from fear |
| **Dead Rails** (2025) | Ride a train to the end of the line. Stop, scavenge, get back aboard | Featured by Roblox [OGE §3]. Challenge videos | Bonds for revives and classes [OGE §3] | Closest structure: moving refuge, stops, return; about 18-minute sessions [OGE §3]. Avoid: horde combat (v0.1) |
| **Forsaken** | Asymmetric killer vs survivors, with Roblox legacy characters | Lore, fan art, edits | Characters, skins | Take: names and lore fuel fan content. Avoid: PvP |
| **Lethal Company, R.E.P.O., The Exit 8** (Steam) | Leave the ship, scavenge, return before it leaves. Carry fragile loot. Spot what changed | Proximity-voice clips. Cloned on Roblox within weeks [OGE §3] | Paid PC games | Stygian Drop's real loop, known to older players. Take: the leave timer, carry tension, voice. Avoid: looking like one more clone |

Money column, and Pressure, Grace and stalker details: from memory (unverified).

### Saturation, honestly

- Co-op horror is one of Roblox's fastest-moving genres [OGE §3], and crowded. This concept sits where three busy lanes meet: elevator, DOORS-style and Backrooms.
- Players will call it "DOORS in a car park". Fine, if the tile shows what nobody owns: racing friends back to slow, real doors.
- The near-duplicate filter judges metadata and place files [OGE §3]. Original code is safe. A generic "Elevator" title and thumbnail is not.
- Hits get cloned within weeks [OGE §3]. The moat: the door rig, the hands, the cars, the lore.

---

## 2. The player

**Core: 16 to 24, friend groups of 2 to 4, voice on, US, UK and EU, phone and PC. Later: 9 to 15.**

| Factor | Fact | So |
|---|---|---|
| Publishing | New games reach 16+ only. Reaching under-16s takes an ID check, 2FA, a subscription or refundable fee, and 250 highly engaged age-checked plays within 60 days [PEP §6] | Launch to 16+. That launch is the under-16 test |
| Maturity | Select (9 to 15) sees up to Moderate. Restricted is 18+ only and blocked in some countries [PEP §6] | Cap fear at Moderate. No gore. Never Restricted |
| DevEx | Age-verified US adults' purchases pay $0.0054 per Earned Robux, 42% over $0.0038. Any R6 option disqualifies [PEP §1] | Lock R15 now. The bonus needs adult buyers, not an 18+ game |
| Spend | US adults spend about 50% more than under-18s [OGE §4]. Younger players' spend per hour fell in Q2 2026 [PEP §6] | Older players pay more and have patience for watch-and-learn horror |
| Chat | Chat needs an age check since January 2026 [OGE §4] | Many strangers cannot talk. Build pings: "hold the doors", "look at it" |
| Owner | PROFILE.md is blank. From 1 Nov 2026, non-US creators face up to 30% withholding on US-source DevEx, which can cancel the 18+ bonus [PEP §7] | Fill in the profile first |

**Group size.** Co-play days are a ranked signal [OGE §4]. But most Home traffic arrives alone, so a public lift must fill and leave within about 30 seconds.

**Device.** Phones are probably most players (unverified). DOORS showed first-person horror works there, given big hold buttons, a brightness check, threats lit in dark rooms and fast loads. Gamepad is bound already; test "keep looking at it" on a stick.

**Session.** 20 to 40 minutes, longer at weekends (Saturday peak [OGE §4]). Sessions of 19+ minutes get double-digit D1 [OGE §1]. But 20 to 30 minutes before a first save is too much for a new player to risk: put their first checkpoint near minute 10.

---

## 3. Discovery fit

| Signal [OGE §4] | Fit | Why |
|---|---|---|
| Play-through (the click) | Mixed | "Elevator" reads on sight. A faceless lift and dark art do not, on a phone grid |
| First-play bounce (exits in 60 to 180 s) | **Hurts as written** | Section 10 is a 3 to 5 minute solo walk with "no flicker, no scare" |
| Play days and playtime over 28 days | Mixed | Two checkpoints fill the 60-minute daily cap. No daily reason to return yet |
| Co-play | Good | Holding doors for friends is natural. Needs invites and cheap private servers |
| Spend | Weak early | Nothing to buy in session one. A revive at death is Roblox's own example [OGE §6] |
| Near-duplicate | Low in code, high in metadata | See section 1 |

Elevator players expect a new floor every minute or two, so keep early stops to 1 to 3 minutes. A quiet stop can be 30 seconds.

### What the first 3 minutes must do

| Time | Beat |
|---|---|
| 0:00 to 0:20 | Spawn in the lift with your party or a filled public car. No menu first |
| 0:20 to 0:50 | Hum, chime, hands. The display shows a level not on the panel, then corrects |
| 0:50 to 1:30 | Doors open. The goal is clear in 10 seconds: dead call panel, breaker sign, a note on a windscreen |
| 1:30 to 2:15 | Hands in the cabinet, view narrowed. A car's interior light comes on behind you |
| 2:15 to 3:00 | Back past the lit car. The doors take their time. As they close, its headlights come on, aimed at you |

Rules: one confirmed, unexplained sign that something noticed you. Never 30 seconds without a goal. Parties play the intro together; returning players skip it.

### Calibrate the gates

- **D1 above 25%** beats the top-10% line in Roblox's example (18.73%); the median is 10.3% [OGE §1]. Pass above the similar-games median in Creator Analytics (about 12% [OGE §7]).
- **CCU above 30** only proves survival: about $150 to $300 a month. $3,000 needs about 300 to 600 average CCU at $5 to $10 per CCU-month [OGE §1, §2].
- **After M1**, buy 5,000 to 20,000 plays for $50 to $150 and read bounce and D1 [OGE §5]. Five testers cannot measure bounce.
- **At launch**, nominate for Standout Games, Roblox's hand-picked sort for novel games [OGE §3].

---

## 4. The click

**"Stygian Drop" does not work as the public title.**

- Many younger players will not know "Stygian". Adults who do read "underworld", which section 9 wants hidden.
- "Drop" suggests a dropper obby or a loot drop. Mismatched metadata is a listed penalty [OGE §4].
- No genre word. US players say "elevator". "Lift" reads British; "Car 04" reads as a driving game.

Keep "Stygian" for the reveal: the deepest band's name, or a word the display shows once.

| Title | For | Against |
|---|---|---|
| **Don't Miss the Elevator** (pick) | States the loop and the stakes. Genre word. Any age | Instruction titles are common |
| **Freight Elevator** | Plain, true to Lift 04 | No danger implied |
| **Make It Back** | The core feeling. Strong thumbnail text | No genre word |
| **Lower Levels** | Real car-park signage. Room to descend | No horror cue |
| **Sublevel** (the doc's own) | Short, ownable, quietly wrong | Weak in search, vague to kids |

Search Roblox for each before choosing; I could not.

**Icon**, readable at phone size:

1. **Headlights in the gap** (lead). From inside the car, doors almost shut, two round headlights in the slit. They read as eyes: a face with no explanation.
2. **The button.** A grey gloved hand presses a lit button under a display showing an impossible level.
3. **The Attendant.** A uniformed silhouette in the closing gap, cap shadow for a face. Unexplained is fine. Undrawable is not.

**Thumbnails** (16:9). Ship at least 2 so personalisation runs; it averaged +8.5% play-through in Roblox's tests [OGE §4].

1. **MAKE IT BACK.** Sprinting toward the lit lift as the doors close, a teammate's arm in the doorway, headlights behind.
2. **HOLD THE DOORS.** Three R15 avatars in the car yell at a fourth running in. Shows co-op, and that this is Roblox.
3. **DON'T LOOK AWAY.** Torches on one parked car while a player turns away.

One bright subject on dark. No monster close-ups. No yellow wallpaper: lead with the car park.

**One-line pitch:** "Co-op elevator horror. Step out, do the job, and make it back before the doors close."

---

## 5. Clips

| Moment | Why it gets shared | Engineer more |
|---|---|---|
| Last one in | A five-second cliffhanger: did they make it? | At some stops the lift leaves on a timer. A body in the doorway holds it until the buzzer forces it shut |
| Left behind | Betrayal is a TikTok staple | Let a player press close on a friend, who can survive until the lift returns |
| Don't look away (Headlights) | Voice chaos over who is watching | Pair it with a two-handed task that turns someone around |
| Lights off (The Attendant) | Whispering in the dark as it passes | Made for spatial voice. If the audio API can read voice loudness (unverified), let it hear you |
| Spot the change (The Occupant) | "What's different?" pulls comments, as The Exit 8 does | Changes visible in a screenshot. Reward players who call them |
| The car in the lift | An image no other horror game has | One peak per band: drive a vintage car into Vehicle Lift 04 as the doors close |
| An impossible floor on the display | Theory videos and wiki pages | Numbered notes, consistent names, hidden stops |

Also:

- **Make deaths watchable.** Two seconds of third person showing what got you, then spectate. A first-person death shows nothing.
- **Put the stop number in every shot.** Depth is the brag: "we reached P23".
- **Moments**, Roblox's short clips that launch straight into a game, are live in the US [OGE §4]. Clips now feed on-platform discovery too.

---

## 6. Verdict

1. **Rebuild the first 3 minutes for the bounce window.** Section 10 is built to be slow; show a goal within seconds and one confirmed sign of a threat before 3:00.
2. **Make "make it back before the doors close" the public identity.** Use a plain "elevator" title (Don't Miss the Elevator), the headlights icon and door-race thumbnails, and save "Stygian" for the reveal.
3. **Build the return engine before launch.** Add a daily seeded descent with a depth board, a notes log, badges and bands shipped as updates [OGE §4], plus fair early spend: revives at death, lift objects, hand skins that also show on the avatar.
4. **Build for 16+ friend groups first.** Lock R15 for the US 18+ rate, cap fear at Moderate, add pings, and open to 9 to 15 after the 250-play evaluation.
5. **Engineer the shareable moments.** Let the lift sometimes leave so someone must choose to hold the doors, make deaths watchable, and give each band a car-into-the-lift peak.
