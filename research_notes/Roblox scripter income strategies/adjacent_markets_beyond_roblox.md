# Adjacent Markets Beyond Roblox for an Expert Lua/Luau Scripter (2025–2026 scan)

*Method note (researched Oct 5, 2026):* This session's egress proxy blocked full-page fetching for almost every domain, including forum.cfx.re, gmodstore.com, tubefilter.com, prismnews.com, hypergridbusiness.com and gameserverkings.com. Most findings below therefore come from search-engine summaries of the cited pages, not from reading the pages in full. Items marked **(secondary)** come from SEO or aggregator guides rather than from the platform itself or reputable press. Items marked **[OLDER]** predate 2025. All ramp-up times are my own estimates, not sourced data. Spot-check the numbers that drive decisions before relying on them.

## Q1. FiveM/RedM (Cfx.re, owned by Rockstar/Take-Two): script market, prices, seller earnings, commission rates, and 2024–2026 policy

### Takeaway
FiveM is the closest skill match for a Luau scripter. Its scripts are Lua and it uses the same client/server event model as Roblox. It also has a large and growing audience: a Steam record of 221K concurrent players in May 2026. A seller can earn in two ways:
- **Selling scripts on Tebex stores.** Scripts usually cost about €12–€46, and Tebex takes about 22–23% in fees.
- **Custom commissions.** These usually pay about $30–$80/hr.

Since January 12, 2026, Rockstar's Creator Platform License Agreement (CPLA) governs everything. It makes Tebex the only legal payment route and was revised again on Sept 10, 2026. Rockstar also runs the official Cfx Marketplace, which only accepts creators who apply and are approved, and it has not disclosed the marketplace's revenue split.

### Cited Findings
**Scale and ownership**
- Rockstar launched the Cfx Marketplace "following the 2023 acquisition of Cfx.re" (reported Jan 2026). — [Respawn/Outlook India](https://respawn.outlookindia.com/gaming/gaming-news/rockstar-games-launches-official-mod-marketplace-fivem-redm)
- FiveM's Steam app reached a record 221,298 concurrent users on May 3, 2026. A later sample showed about 180.7K playing, with a 24-hour peak of about 190K (2026). — [SteamDB charts](https://steamdb.info/app/2676230/charts/); [playerstats.gg](https://playerstats.gg/game/fivem/)
- FiveM broke its own Steam record at 200,000 concurrent players, which press framed as happening "ahead of GTA 6" (2026). — [GamesRadar](https://www.gamesradar.com/games/grand-theft-auto/ahead-of-gta-6-rockstar-owned-gta-5-rp-mega-mod-fivem-breaks-its-own-steam-record-with-200-000-concurrent-players/)

**Policy changes (2025–2026)**
- On Dec 22, 2025, Cfx.re announced a new CPLA effective Jan 12, 2026. Creators must accept it to keep participating fully. — [GameServerKings KB](https://www.gameserverkings.com/knowledge-base/fivem/server-monetisation/) (secondary); [CPLA PDF, Jan 12 2026](https://static.cfx.re/platform-license-agreement-12-jan-2026.pdf); [Cfx forum announcement](https://forum.cfx.re/t/updates-to-the-creator-platform-license-agreement/5371920)
- The CPLA was revised again on Sept 10, 2026; this is the current version at fivem.net/terms. I found no changelog for this revision. — [fivem.net/terms](https://fivem.net/terms); [CPLA PDF, Sept 10 2026](https://static.cfx.re/platform-license-agreement-10-sept-2026.pdf)
- The Rockstar ToS, Community Guidelines and the CPLA together form a binding agreement with Rockstar Games, Inc. and Take-Two. That agreement covers "FiveM" and "RedM" (Sept 2026 version). — [fivem.net/terms](https://fivem.net/terms)
- The CPLA says: "Tebex is the authorized monetization partner for the Cfx Platform, and the use of any other platform or payment provider is prohibited." In practice, taking payment through PayPal, Patreon, Ko-fi or your own card form is a violation (2026). — [CPLA Sept 2026](https://static.cfx.re/platform-license-agreement-10-sept-2026.pdf); [GameServerKings](https://www.gameserverkings.com/knowledge-base/fivem/server-monetisation/)
- The rules prohibit or restrict (2026, secondary summary of the CPLA):
  - selling in-game currency for real money
  - real-money gambling or cash-out
  - chance-based purchases
  - Rockstar-created content
  - crypto and NFTs
  - third-party resale
  - real-world IP
  - "undefined benefits"

  — [GameServerKings](https://www.gameserverkings.com/knowledge-base/fivem/server-monetisation/)
- The January 2026 CPLA revised the IP provisions, the content-usage rules, and the responsibilities creators take on when they distribute paid or free resources. — [GoodLeafDev](https://goodleafdev.com/blog/fivem-creator-license-agreement-update) (secondary)
- **Cfx Marketplace** is Rockstar's official, curated store for FiveM/RedM content: props, vehicles, maps and scripts. Details at launch (Jan 2026):
  - It launched Jan 12–14, 2026 with about 15–16 hand-picked creators, plus 6 more "coming soon".
  - Other sellers must apply and be approved.
  - Premium items cost around $129.99, bundles go up to about $389.99–$467.99, and some items are $23.99/month subscriptions.

  — [Game Developer](https://www.gamedeveloper.com/business/rockstar-launches-an-official-mod-marketplace); [Wccftech](https://wccftech.com/rockstar-launches-cfx-marketplace-official-modding-store-fivem-redm/); [Kotaku](https://kotaku.com/gta-cfx-marketplace-mods-online-rdr2-2000659824); [TechRadar](https://www.techradar.com/gaming/rockstar-has-launched-its-own-mod-marketplace-ahead-of-the-launch-of-grand-theft-auto-6)
- Nobody has disclosed the Cfx Marketplace revenue split. Kotaku says it is unclear what cut Take-Two takes. — [Kotaku](https://kotaku.com/gta-cfx-marketplace-mods-online-rdr2-2000659824); **conflicting/unverified:** one outlet claims "all profits are collected only by its creators" — [GamerUrge](https://gamerurge.com/gta-online-paid-mod-marketplace)
- Cfx.re supports selling escrowed (code-protected) assets, distributed through Tebex. — [PlayDeck guide](https://www.playdeck.co/guides/tebex-fees-escrow-selling-scripts/) (2026, secondary)

**Fees**
- Tebex charges FiveM sales a 15% platform fee, against its standard 5%. Payment-gateway fees add roughly 7–8% more, so total fees are about 22–23% and a $30 script nets about $23 (2026). — [PlayDeck](https://www.playdeck.co/guides/tebex-fees-escrow-selling-scripts/), [FiveMX](https://fivemx.com/blog/tebex-alternatives-fivem-2026) (secondary); Tebex's own explainer: [Tebex Platform Fee Explained](https://docs.tebex.io/creators/pricing-overview/tebex-fees-and-billing-overview/tebex-platform-fee-explained); a long-running community complaint thread: [Cfx forum "Tebex and its 15% gateway fees for FiveM"](https://forum.cfx.re/t/tebex-and-its-15-gateway-fees-for-fivem/4838828) **[OLDER — thread date not visible, likely pre-2025]**

**Script prices** (Tebex store pages, retrieved Oct 2026)
- QBCore/ESX script prices:
  - phone €46
  - housing €28
  - mechanic €33
  - job scripts €19–€23
  - multicharacter €17
  - HUD €20
  - shop scripts €12.10–€32.67
  - drug-lab and restaurant scripts $15–$20

  — [CanX Tebex](https://canx.tebex.io/), [JPResources Tebex](https://jpresources.tebex.io/category/qbcore), [F4 Studio Tebex](https://f4studio.tebex.io/)
- Stores market their scripts as compatible with QBCore, ESX and Qbox. — [F4 Studio Tebex](https://f4studio.tebex.io/)

**Commission rates**
- Fiverr FiveM gigs start at $5–$10 at the low end. Freelance FiveM developers typically charge $30–$80/hr, and some list $35/hr (Sept 2026). — [Fiverr: hire FiveM developers](https://www.fiverr.com/hire/fivem); [Fiverr $5 gig example](https://www.fiverr.com/sevres986/make-fivem-scripts-for-you); [Guru FiveM freelancers](https://www.guru.com/m/hire/freelancers/fivem/)
- Buyer budgets: servers earning $10K+/month typically get 60–80% of their revenue from Tebex VIP subscriptions and also sell scripts (2026). Smaller engaged communities bring in about $100–$500/month. — [FiveMX monetization guide](https://fivemx.com/blog/complete-guide-fivem-server-monetization) (secondary)

### Inferences
- **Skill transfer is near-total.** FiveM gigs are explicitly "FiveM scripts in Lua" ([Fiverr](https://www.fiverr.com/sevres986/make-fivem-scripts-for-you)). FiveM's client/server event model maps directly onto Roblox RemoteEvents. In-game web UIs (NUI) are HTML/JS, so roblox-ts and TypeScript experience is a bonus. A Luau expert would mainly need to learn framework conventions (QBCore/ESX/Qbox), the common libraries, and the SQL persistence pattern. I estimate 2–6 weeks to become competitive.
- **Fastest cash is commissions.** At $30–$80/hr, 10 hrs/week is about $1.2K–$3.2K/month. This is a scenario, not observed data.
- **Script sales are slower but compound.** A €25 script nets about €19 after Tebex fees, so about 150 sales/month would be about €2.9K/month (scenario). Script-sales income depends on reputation, Discord marketing and escrow protection.
- **Platform risk is high.** Rockstar controls the platform and revised the CPLA twice in 2026. The official marketplace is gated and its split undisclosed. The GTA VI launch could shift where roleplay players go.

### Gaps
- I found no reliable public data on individual Tebex script sellers' earnings: no disclosures and no surveys.
- I could not see what changed in the Sept 10, 2026 CPLA. I found no specific 2024 Cfx.re policy changes; the forum was blocked.
- The Cfx Marketplace revenue split and whether it will open broadly to more creators are both unknown.
- The $30–$80/hr range comes from a search summary of Fiverr's hire page; I could not check it on the page itself.

## Q2. Garry's Mod (GModStore), WoW addons, Defold, LÖVE2D, Playdate: meaningful income in 2025–2026?

### Takeaway
Mostly no.
- **GMod** is the only one with a working market for Lua scripts (GModStore). It is a mature niche where sellers anecdotally earn $100 to $1,000+/month. Its successor, s&box, now has a real creator fund of $1M/year, but s&box is not Lua.
- **WoW addons** earn donation-scale money (WeakAuras gets about $500/month on Patreon), and Blizzard's Midnight API limits gutted the combat-addon niche.
- **Playdate** paid about $1.04M to all of its developers combined in two years.
- **LÖVE and Defold** have no creator payout channel at all; the only way to earn is to ship your own game.

### Cited Findings
**Garry's Mod, GModStore and s&box**
- GModStore reportedly takes a 20% cut, so creators keep 80%. — search summary attributing this to [GModStore developer help](https://www.gmodstore.com/help/developers). **UNVERIFIED:** the page was blocked and a second search could not confirm the figure.
- Anecdotally, smaller GModStore creators earn about $100/month and larger ones $1,000+/month (undated). — [GModStore community thread "Who has made gmod a career?"](https://www.gmodstore.com/community/posts/A-E1J2jTQeCNqU3H75kKDQ)
- Facepunch's s&box Play Fund had paid out more than $500,000 to game makers as of April 2026. The fund is paid for out of Garry's Mod profits. — [PC Gamer](https://www.pcgamer.com/games/rpg/we-dont-have-to-fire-1000-people-to-keep-it-working-facepunch-studios-says-paying-s-and-box-game-developers-is-sustainable-with-usd500-000-paid-out-to-date/)
- s&box's Steam launch day (2026):
  - It grossed just over $1M, with $574K profit.
  - Facepunch then raised the Play Fund to $1M/year, paid out to the most popular games and maps.
  - Developers can export their games to Steam, and Facepunch takes no cut.

  — [Yahoo Tech / PC Gamer](https://tech.yahoo.com/gaming/articles/box-makes-nearly-1-million-204915433.html); [80.lv](https://80.lv/articles/s-box-to-launch-on-steam-with-sustainable-payout-for-devs)

**World of Warcraft addons**
- For Midnight, Blizzard moved real-time combat data into "secret values" and is blocking third-party addons that act as computational combat helpers (Nov 3, 2025). — [Blizzard Watch](https://blizzardwatch.com/2025/11/03/heck-happening-wow-addons-midnight/); [The Escapist](https://www.escapistmagazine.com/world-of-warcraft-midnight-addon/)
- WeakAuras said it would not continue development in Midnight, and Shadowed Unit Frames paused updates (2025). — [Blizzard EU forums](https://eu.forums.blizzard.com/en/wow/t/add-on-devs-refused-to-continue-in-the-midnight-era-due-to-restrictions-imposed-by-blizz/602690)
- WeakAuras' Patreon brings in about $500/month, plus some CurseForge and Wago income. The team called this "not a very significant amount of money for any of us" (late 2025). — [WeakAuras Patreon post](https://www.patreon.com/posts/weakauras-x-140349416)
- Blizzard later relaxed some of the Midnight addon limits (exact date not confirmed). — [Icy Veins](https://www.icy-veins.com/wow/news/weakauras-responds-to-addon-limitation-loosening-in-midnight/)

**Playdate**
- From Catalog's launch in March 2023 through April 2025, it sold 289,305 games and paid developers $1,043,186. Panic added 262 hand-picked titles over that period. — [Game Developer](https://www.gamedeveloper.com/business/panic-has-paid-out-over-1-million-to-playdate-developers-on-catalog) (Apr 2025)
- **[OLDER]** As of 2024, Catalog had sold 150K+ games and developers had earned $544,290 after taxes, processing fees and Panic's 25% cut. — [Engadget](https://www.engadget.com/playdate-developers-have-made-more-than-500k-in-catalog-sales-120034296.html); [VGC](https://www.videogameschronicle.com/news/playdates-catalog-has-sold-150000-games-earning-developers-more-than-544000/)

**LÖVE2D and Defold**
- Balatro, built with the Lua-based LÖVE framework, sold 5M copies by Jan 21, 2025; it released on Feb 20, 2024. — [Game Developer](https://www.gamedeveloper.com/business/balatro-sells-5-million-copies-after-end-of-year-spike); [GameFromScratch](https://gamefromscratch.com/balatro-made-with-love-love2d-that-is/)
- For Defold, I found no creator marketplace, payout program or income data in 2025–2026 sources (see Gaps).

### Inferences
- **Playdate is tiny.** About $1.04M across roughly 262 titles averages about $4K per title over its lifetime, and about $3.61 net per sale. That is hobby money, not a channel.
- **LÖVE, Defold and Playdate are "ship your own game" bets.** Their outcomes depend on a hit (Balatro is an outlier), so they are not a dependable secondary income for a services-oriented scripter.
- **GMod uses Lua (GLua),** so the ramp-up would be fast (about 1–3 weeks). However, the market is small and aging, and Facepunch's investment has moved to s&box. s&box scripting is generally understood to be C#, but I did not verify that in this session. That makes s&box a new-language bet whose upside is capped by a $1M/year fund shared across all creators.
- **WoW addons are not an income channel.** Even a flagship addon makes about $500/month in donations, and Midnight shrank the space.

### Gaps
- I could not verify GModStore's fee, its total payouts to creators, or any 2025–2026 market-size data.
- I found no income data for typical (non-flagship) WoW addon authors on CurseForge or Patreon.
- I found no Defold or LÖVE freelance or job-market rate data, and no Playdate payout figures after April 2025.

## Q3. Other UGC platforms with creator payouts: Fortnite UEFN/Verse, Minecraft Marketplace/Bedrock, Rec Room, CurseForge/Overwolf, Hytale (2025–2026)

### Takeaway
- **Fortnite** is the only one with Roblox-scale money. Epic paid creators about $352M in 2024 and an estimated about $370M in 2025, and cumulative UEFN payouts passed $1B by June 2026. Since late 2025, in-island purchases pay creators 100% of the V-Bucks value through 2026. However, it means learning Verse and Unreal, and earnings are highly concentrated among the top creators.
- **Minecraft Marketplace** has paid creators more than $500M in total and keeps 30% of sales, but only about 300 approved partner organisations can sell there. Bedrock add-ons are scripted in JavaScript/TypeScript, which suits a roblox-ts user.
- **Rec Room** shut down on June 1, 2026.
- **CurseForge** rewards average about $600 per author over the program's lifetime.
- **Hytale** (Java, in early access since Jan 13, 2026) is promising but early. It takes 0% commission for two years, and mods are growing fast.

### Cited Findings
**Fortnite UEFN/Verse**
- **[OLDER, data year 2024]** Epic paid $352M to creators in 2024. — [Esports Insider](https://esportsinsider.com/2025/01/fortnite-352m-creator-revenue-payments-maps) (Jan 2025)
- Naavik estimates about $370M in engagement payouts in 2025, the midpoint of a $350–$390M range. — [Tech-Insider summarizing Naavik](https://tech-insider.org/ca/fortnite-creator-economy-1-billion-2026/) (2026; estimate, secondary)
- Epic announced at Unreal Fest Chicago on June 17, 2026 that UEFN creator payouts had passed $1B since the tool launched in 2023. At the same event:
  - Creator islands made up 47% of Fortnite playtime, up from 38% a year earlier. Tech-Insider instead says "~35%".
  - More than 3K islands now earn more from in-island transactions than from engagement payouts.

  — [PocketGamer.biz](https://www.pocketgamer.biz/unreal-engine-for-fortnite-creator-payouts-surpass-1bn/); [Tubefilter](https://www.tubefilter.com/2026/06/17/epic-games-unreal-editor-for-fortnite-creator-payouts/); [Respawn/Outlook India](https://respawn.outlookindia.com/gaming/gaming-news/epics-uefn-payouts-reached-1-billion-since-launch)
- The engagement pool is 40% of Fortnite's net revenue from the Item Shop and most real-money purchases. — [Respawn/Outlook India](https://respawn.outlookindia.com/gaming/gaming-news/epics-uefn-payouts-reached-1-billion-since-launch) (June 2026); [Fortnite Platform & Economy](https://www.fortnite.com/developer/platform-and-economy)
- **In-island transactions** were announced in Sept 2025, previewed, then rolled out. The revenue share works like this:
  - Through the end of 2026, creators get 100% of the V-Bucks value of a sale, which reports equate to about 74% of the net sale.
  - From 2027, they get 50% of the V-Bucks value, about 37% of the net sale.
  - **Sources disagree on the cutoff date:** Dec 31, 2026 or Jan 31, 2027.

  — [Fortnite.com news](https://www.fortnite.com/news/tools-for-in-island-transactions-now-available-to-fortnite-developers?lang=en-US); [Esports Insider](https://esportsinsider.com/2025/09/fortnite-developers-sell-in-game-items-update) (Sept 2025); [GameSpot](https://www.gamespot.com/articles/fortnite-now-lets-creators-publish-islands-with-in-game-transactions/1100-6537294/); [PocketGamer.biz](https://www.pocketgamer.biz/epic-games-is-previewing-in-island-transaction-tools-for-fortnite-creators/)
- Earnings are concentrated: 58 creators earned more than $1M in 2024, and seven individuals earned more than $10M (period unclear in the search summary). — [Naavik, "The New Fortnite Creative Millionaires"](https://naavik.co/digest/fortnite-creative-millionaires/)

**Minecraft Marketplace and Bedrock**
- Partner program terms (2026 guide; secondary, not confirmed against Microsoft):
  - Marketplace creators have earned more than $500M in total.
  - About 300 partner organisations publish content.
  - Partners keep 70% of each sale.
  - Microsoft pays quarterly through Partner Center, with a $200 minimum.
  - Joining requires an application with a portfolio and business information.

  — [Generalist Programmer partner guide](https://generalistprogrammer.com/tutorials/how-to-become-minecraft-marketplace-partner-guide)
- **[OLDER]** An earlier reported milestone put creator payouts at $350M (date not shown). — [Screen Rant](https://screenrant.com/minecraft-marketplace-350-million-profit-modders/)
- The Bedrock Script API runs JavaScript in behavior packs, and Microsoft documents a TypeScript workflow. Bedrock Dedicated Server adds more powerful JavaScript APIs, including ones for connecting to external services (current docs). — [Microsoft Learn: Scripting with TypeScript](https://learn.microsoft.com/en-us/minecraft/creator/documents/scripting/next-steps?view=minecraft-bedrock-stable); [Microsoft Learn: BDS scripting](https://learn.microsoft.com/en-us/minecraft/creator/documents/bedrockserver/scripting?view=minecraft-bedrock-stable)
- Minecraft announced its first affiliate program, run through impact.com, in late Aug 2026. It pays commission for promoting Minecraft, not for development work. — [MediaPost](https://www.mediapost.com/publications/article/415461/minecraft-taps-creator-partnership-platform-to-pow.html?edition=142773)

**Rec Room (closed)**
- Rec Room creators earned more than $1M in a single quarter for the first time (Sept 24, 2025). More than 2,500 creators had been paid, and 17 had earned more than $100K over their lifetime. — [Rec Room blog](https://blog.recroom.com/posts/2025/9/24/a-1m-quarter-for-rr-creators)
- Rec Room kept only about 30¢ of every dollar spent on UGC items, against about 70¢ on its own items (Aug 28, 2025). — [Rec Room blog: Finances and UGC revenue](https://blog.recroom.com/posts/2025/8/28/rec-room-finances-and-ugc-revenue)
- Rec Room cut 16% of staff in March 2025 and about half of its staff in August 2025. — [TechPowerUp](https://www.techpowerup.com/340360/rec-room-dev-lays-off-roughly-half-of-staff-and-narrows-scope-of-free-to-play-ugc-game)
- It announced its shutdown in March 2026 and closed on June 1, 2026. — [Hypergrid Business](https://www.hypergridbusiness.com/2026/03/rec-room-shuts-down-after-decade-and-150-million-players/); [IBTimes UK](https://www.ibtimes.co.uk/rec-room-shuts-down-ai-costs-overwhelm-revenue-1789414)

**CurseForge / Overwolf rewards**
- CurseForge says it has paid $20.4M to 33,686 authors (current page, figure undated). — [CurseForge for Mod Authors](https://authors.curseforge.com/welcome/)
- The rewards program pays $0.05 per point from a pool based on downloads, splits revenue 70/30 in creators' favour, and pays out through PayPal or gift cards (2026). — [Gemlist](https://www.gemlist.io/blog/how-much-does-curseforge-pay-mod-creators) (secondary)
- Payouts now go through Tremendous, which offers gift cards, prepaid cards, bank transfer or charity (date not shown). — [CurseForge blog](https://blog.curseforge.com/introducing-tremendous-a-game-changing-payout-solution-for-curseforge-authors/)

**Hytale**
- Hytale entered Early Access on Jan 13, 2026 with an official CurseForge partnership. More than 500 mods appeared within 48 hours and more than 3,500 within a month. — [HytaleCharts](https://hytalecharts.com/news/hytale-modding-curseforge-partnership-creator-guide) (2026; secondary)
- Hytale mods have passed 20M downloads, with more than 5,000 mods created. Hypixel and CurseForge are running a $100K modding contest with 65 winners; first place in each category gets $10K (2026). — [PocketGamer.biz](https://www.pocketgamer.biz/hypixel-studios-and-curseforge-launch-100000-modding-contest-for-hytale-creators/); [GameSpot](https://www.gamespot.com/articles/hytale-announces-modding-contest-with-100k-prize-pool-on-offer/1100-6538548/)
- The deepest kind of Hytale mod, the server plugin, is written in Java and packaged as a .jar against the server API (2026). — [WabbaNode](https://wabbanode.com/blog/hytale/how-does-hytale-modding-work); [Apex Hosting](https://apexminecrafthosting.com/guides/hytale/how-to-install-hytale-server-mods-plugins-assets/)
- Hytale takes 0% commission on mods and servers for at least the first two years. Approved creators get creator codes that earn 5% of checkout spend, rising to 7% later. — [hytale.game interview with Simon](https://hytale.game/en/exclusive-simon-hytale-owner-unveils-early-access-pricing-monetization-modding-and-lore/) (fan site, secondary)
- Mods in the in-game browser are free to install; Hytale's owner says the browser should be "a library, not a mall" (2026). — [Simon on X](https://x.com/Simon_Hypixel/status/2050604074932871343); [hytale.game](https://hytale.game/en/hytale-simon-hypixel-reveals-a-revolutionary-library-first-vision-for-mod-monetization/)

### Inferences
- **Fortnite:** the 2025 pool works out to about $30M/month, but it is top-heavy. Ramp-up is the slowest of the options: a new language (Verse) plus the Unreal editor and level-design workflow, probably 2–4+ months to ship competitive work. For a scripter, contract Verse work for established UEFN studios is probably more realistic than self-published island payouts. I found no rate data to confirm that.
- **Minecraft:** individuals effectively cannot sell on the Marketplace without partner status. The realistic route is contracting for partner studios, or getting into the partner program through a studio. Ramp-up is fast for a roblox-ts user because the language is JS/TS.
- **CurseForge:** $20.4M across 33,686 authors is about $606 per author over the program's lifetime on average. The median is surely lower, so this is pocket money, not a channel.
- **Hytale:** Speculative upside thanks to the 0% commission window, a growing install base and an official CurseForge pipeline. The downsides: it requires Java, it is in early access, and the free-mod "library" model means income would come from servers, creator codes, contests or commissions rather than mod sales.
- **Rec Room:** eliminated.

### Gaps
- I found no public rates for freelance Verse/UEFN contractors or for Minecraft partner-studio contractors.
- I found no data on what a typical (median) Fortnite creator earns, and could not verify the period behind Naavik's figures.
- I could not confirm the Minecraft "$500M" and "about 300 partners" figures from a Microsoft primary source.
- I could not confirm Hytale's specific mechanisms for creators to earn money (for example, paid plugins or server stores) beyond creator codes. The 0% commission claim comes from a fan-site interview.

## Q4. General freelance pivot (game backends, Discord bots, automation, TypeScript/web): Upwork/Fiverr rates

### Takeaway
Demand is broad but crowded, and the low end is price-compressed:
- Upwork Lua freelancers list $10–$75/hr.
- Upwork TypeScript freelancers sit around a median of about $30/hr (range $11–$42); experienced US-based developers charge $150+/hr.
- Bot and chatbot developers charge about $30–$61/hr.
- Discord-bot projects range from $300 to $12K+.

A Luau expert with roblox-ts experience can credibly bid on TypeScript, Node and Discord-bot work within weeks. They would need a portfolio outside Roblox and would face more competition than in game-specific niches.

### Cited Findings
- On Upwork, Lua freelancers list rates of $10, $20, $30 and $75/hr. Typical focused Lua projects run $500–$1,500 (Sept 2026). — [Upwork: Lua developers](https://www.upwork.com/hire/lua-developers/)
- US employment listings for Lua developers advertise about $55–$57/hr; these are jobs, not freelance gigs (Aug 2026). — [ZipRecruiter](https://www.ziprecruiter.com/Jobs/Lua-Developer)
- TypeScript rates (2026; figures via search summary):
  - On Upwork, TypeScript freelancers charge $11–$42/hr, with a median of $30.
  - Individual Upwork listings run $20–$50/hr.
  - US-based developers range from $30/hr for juniors to $150+/hr for the most experienced.

  — [Upwork: TypeScript developers](https://www.upwork.com/hire/typescript-developers/) (Oct 2026); [goLance JS rate guide](https://golance.com/hiring/best-freelance-javascript-developers-hourly-rate)
- Upwork's fees are reported as 10% for freelancers and 5% for clients (2026). — [GigRadar](https://gigradar.io/blog/upwork-hourly-rate) (secondary; check against Upwork's current fee schedule)
- Chatbot and bot developers on Upwork generally cost $30–$61/hr (Oct 2026). — [Upwork: chatbot developer cost](https://www.upwork.com/hire/chatbot-developers/cost/); [Upwork: bot developers](https://www.upwork.com/hire/bot-developers/)
- Discord-bot developers can be hired from about $10/hr on Upwork and Fiverr. Projects range from $300 for a simple command bot to $12,000+ for a custom bot with integrations, dashboards and production monitoring (Sept 2026). — [Arc.dev: Discord bot developers](https://arc.dev/hire-developers/discord-bot)
- Upwork runs a dedicated Discord-bot-developer category (Sept 2026). — [Upwork: Discord bot developers](https://www.upwork.com/hire/discord-bot-developers/)

### Inferences
- Several Roblox skills carry over (inference):
  - roblox-ts gives TypeScript fluency.
  - Writing Roblox networking and persistence code maps onto game backends: matchmaking, leaderboards, webhooks, Discord/Roblox Open Cloud integrations.
  - Many Roblox studios want Discord bots for their communities, so existing Roblox clients are a warm lead.
- A new Upwork profile with no off-Roblox reviews would likely have to start around $25–$45/hr and raise rates as reviews build. This is a scenario, not sourced.
- Lua-specific Upwork demand is thin and mixed (embedded, game modding, Neovim and so on). The larger market is TypeScript/Node.

### Gaps
- I found no Fiverr rate data specific to Discord bots or game backends, and no 2025–2026 job-volume or demand counts for these categories.
- I found no rate data specifically for "game backend developer" freelancers.
- I could not verify the current Upwork fee structure; it has changed over time.

## Q5. Which channel offers the best ratio of earning potential to ramp-up time for an expert Luau scripter?

### Takeaway
**FiveM/RedM is the best secondary channel.** The language switch is minimal (Lua), the client/server model is Roblox-like, and the audience is large and active (Steam record of 221K concurrent players, May 2026). Commissions pay quickly at $30–$80/hr, and selling scripts adds a slower, compounding stream (€12–€46 per script, about 77% net after Tebex fees). The main risk is Rockstar's control: the CPLA was revised twice in 2026, and the official marketplace is curated with an undisclosed split.

**Runner-up: TypeScript, Node and Discord-bot freelancing.** It builds on roblox-ts, has a larger total market and less platform risk, but competition is heavier and the low end is price-compressed.

**Not recommended as a secondary channel:**
- Fortnite UEFN has the biggest money pool but the slowest ramp-up and extreme concentration among top creators.
- Hytale is a speculative early-access bet that requires Java.
- GMod, WoW addons, Playdate, LÖVE and Defold produce hobby-level income.
- Rec Room is closed.

### Cited Findings
These are the key comparative data points; full citations are in Q1–Q4.
- FiveM: Steam concurrent-player record of 221,298 on May 3, 2026. — [SteamDB](https://steamdb.info/app/2676230/charts/)
- FiveM: about 22–23% total Tebex fees, and Tebex is the only permitted payment route under the 2026 CPLA. — [PlayDeck](https://www.playdeck.co/guides/tebex-fees-escrow-selling-scripts/); [CPLA](https://static.cfx.re/platform-license-agreement-10-sept-2026.pdf)
- FiveM: commissions at $30–$80/hr. — [Fiverr](https://www.fiverr.com/hire/fivem)
- TypeScript on Upwork: median about $30/hr. — [Upwork](https://www.upwork.com/hire/typescript-developers/)
- Bot developers on Upwork: $30–$61/hr. — [Upwork](https://www.upwork.com/hire/chatbot-developers/cost/)
- Fortnite: about $370M in creator payouts in 2025 (estimate) and $1B+ cumulative by June 2026. — [Tech-Insider/Naavik](https://tech-insider.org/ca/fortnite-creator-economy-1-billion-2026/); [PocketGamer.biz](https://www.pocketgamer.biz/unreal-engine-for-fortnite-creator-payouts-surpass-1bn/)
- Rec Room: closed June 1, 2026. — [Hypergrid Business](https://www.hypergridbusiness.com/2026/03/rec-room-shuts-down-after-decade-and-150-million-players/)
- Playdate: about $1.04M paid to all developers through April 2025. — [Game Developer](https://www.gamedeveloper.com/business/panic-has-paid-out-over-1-million-to-playdate-developers-on-catalog)
- WeakAuras: about $500/month on Patreon. — [Patreon](https://www.patreon.com/posts/weakauras-x-140349416)

### Inferences
**Ranking table.** Ramp-up times and ranks are my estimates; the money signals are sourced above.

| Rank | Channel | Language gap from Luau | Est. ramp-up | 2025–26 money signal (sourced) | Main risk |
|---|---|---|---|---|---|
| 1 | FiveM/RedM commissions → Tebex script store | Minimal (Lua; HTML/JS for UI) | 2–6 wks | $30–$80/hr commissions; €12–€46 scripts, about 22–23% fees; 221K concurrent-player record | Rockstar policy control (CPLA revised Jan and Sept 2026); gated official marketplace; GTA VI disruption |
| 2 | TS/Node/Discord-bot and game-backend freelancing | Low (roblox-ts → TS) | 2–6 wks (portfolio) | TS median about $30/hr on Upwork; bots $30–$61/hr; projects $300–$12K+ | Crowded; low-end price pressure; Upwork fees |
| 3 | Minecraft Bedrock add-ons (contracting for Marketplace partners) | Low (JS/TS) | 3–8 wks | More than $500M paid to partners in total, 70/30 split (secondary) | Partner gating; no contractor rate data |
| 4 | Fortnite UEFN/Verse | High (Verse + Unreal) | 2–4+ months | About $370M (est.) in 2025; in-island purchases pay 100% of V-Bucks value through 2026 | Extreme concentration; discovery; share drops in 2027 |
| 5 | Hytale (Java plugins) | High (Java) | 1–3 months | 0% commission for 2 years; 20M+ mod downloads; $100K contest | Early access; free-mod model; monetization still forming |
| 6 | GMod/GModStore | Minimal (GLua) | 1–3 wks | Anecdotal $100–$1K+/month | Aging, small niche; Facepunch's focus has moved to s&box |
| 7 | WoW addons, CurseForge rewards, Playdate, LÖVE, Defold | Minimal (Lua) | n/a | Donation- or hit-scale income (WeakAuras about $500/month; CurseForge about $606 per author lifetime) | Not a dependable income stream |
| — | Rec Room | — | — | Shut down June 1, 2026 | Eliminated |

- **Suggested sequencing for the plan (inference):** start with FiveM commissions for immediate cash and to learn which frameworks buyers use. Package the reusable pieces into 1–3 Tebex scripts with escrow, and later apply to the Cfx Marketplace. Use TS and Discord-bot freelancing as a lower-risk fallback that also serves existing Roblox clients.

### Gaps
- No source compares ramp-up times across these platforms; every ramp-up figure above is an estimate.
- I found no data on typical (median) earnings for FiveM script sellers, UEFN Verse contractors or Minecraft partner-studio contractors. Those numbers would change the ranking between FiveM, Fortnite and Minecraft.
- I could not quantify how GTA VI's launch will affect FiveM's player base or the market for scripts.
