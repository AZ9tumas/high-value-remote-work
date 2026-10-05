# Economics & Strategy of Building and Monetizing Your Own Roblox Games (solo / small-team scripter, 2025–2026)

*How these notes were made (research date 2026-10-05):* WebFetch was blocked by the egress proxy for most domains (sec.gov, devforum.roblox.com, about.roblox.com, Wikipedia, RoMonitor, Rolimons, Naavik, trade press). So most web facts below come from **search-engine result summaries**, not full-page reads, and the report writer should treat them as "reported." The exception is **Roblox's official Creator Hub documentation**, which I read directly from the official `Roblox/creator-docs` GitHub repo (snapshot commit dated 2026-10-02). Those citations point to GitHub file URLs, which mirror `create.roblox.com/docs/...`.
*Labels:* **[OFFICIAL]** = Roblox docs or financial filings. **[PRESS]** = news reporting. **[3P-EST]** = third-party estimate or model, unaudited. **[ANECDOTE]** = a developer's self-report. **(s.s.)** = attribution taken from a search summary, not verified on the page.

---

## 1. Revenue benchmarks: how CCU / DAU / visits / playtime translate into revenue

### Takeaway
At platform-average monetization, one *average* concurrent user (CCU) held for a month is worth about **$9–$12 of DevEx**. That comes from two independent estimates that agree: a top-down figure from Roblox's Q2 2026 financials and a developer rule of thumb. Individual games vary from **under $0.50 to about $15+ per average-CCU-month** depending on genre, audience age and how deep the monetization goes. Payer conversion is low single digits, and spend is heavily concentrated in a few payers and a few games.

### Cited Findings
**Platform-level (official):**
- **Q2 2026** (quarter ended 2026-06-30) [OFFICIAL]:
  - Revenue rose 36% YoY to $1.5B. Bookings rose 8% to $1.6B, at the low end of guidance.
  - DAU rose 10% YoY to **123M**. Hours rose 5% to **29B**.
  - Developer Exchange (DevEx) fees rose 15% YoY to **$363M**. Roblox credits part of that to the creator-earnings increase it announced on 2025-09-05.
  - Management said monetization measured as bookings per hour came in below forecast, "particularly with under-13 cohorts."
  - Sources: [Roblox Q2 2026 8-K exhibit 99.1](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm); [Q2 2026 Shareholder Letter](https://s27.q4cdn.com/984876518/files/doc_financials/2026/q2/Roblox-Q2-2026-Earnings-Shareholder-Letter.pdf); [Investing.com Q2 2026 call transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-roblox-q2-2026-beats-eps-but-shares-sink-on-bookings-93CH-4826338); [Investing.com Q2 2026 slides](https://www.investing.com/news/company-news/roblox-q2-2026-slides-bookings-growth-slows-to-8-amid-user-decline-93CH-4826401).
- **Q1 2026** [OFFICIAL]:
  - Revenue rose 39% to $1.4B. Bookings rose 43% to $1.7B.
  - DAU rose 35% YoY to 132M. Hours rose 43% to 31B.
  - Monthly unique payers rose 52% to 31M.
  - Sources: [Roblox Q1 2026 8-K](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026028882/ex991-q12026earningsshar.htm); [Motley Fool Q1 2026 transcript](https://www.fool.com/earnings/call-transcripts/2026/04/30/roblox-rblx-q1-2026-earnings-call-transcript/).
- **FY2025** [OFFICIAL]: revenue was $4.9B (+36%) and bookings $6.8B (+55%). In Q4 2025, bookings were up 63% YoY and DAU up 69% YoY. About 60M DAU were added between Q4 2024 and Q4 2025. Sources: [Q4 2025 shareholder letter (8-K)](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000009/ex991-q42025shareholder.htm); [PDF](https://s27.q4cdn.com/984876518/files/doc_financials/2025/q4/Q4-2025-Shareholder-Letter.pdf).
- **Q3 2025** DevEx fees were $427.9M, up 85% YoY [OFFICIAL]. Source: [Roblox Q3 2025 8-K](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000326/ex991-q32025shareholderl.htm).
- **Annual creator payouts** [OFFICIAL via PRESS]:
  - Creators earned about **$1.7B through DevEx in the 12 months ending 2026-06-30**, roughly +50% YoY. This was announced at RDC in September 2026. Sources: [TweakTown](https://www.tweaktown.com/news/113585/robloxs-top-10-creators-averaged-dollars65-7-million-each-while-the-median-made-dollars1500-and-roblox-everywhere-is-the-fix/index.html); [Dexerto](https://www.dexerto.com/roblox/robloxs-top-creators-average-65-7-million-a-year-but-most-make-far-less-3408675/).
  - Roblox paid creators about $1.5B in calendar 2025. Source: [Tubefilter, 2026-09-03](https://www.tubefilter.com/2026/09/03/roblox-creator-earnings-2025-usa-gdp-game-item-sales/).
- **DevEx rate and what counts as Earned Robux** [OFFICIAL]:
  - The standard rate is **$0.0038 per Earned Robux for Robux earned on or after 2025-09-05**. The previous rate was $0.0035.
  - That works out to $114 per 30,000 Robux, and **30,000 Earned Robux is the minimum to cash out**.
  - Earned Robux covers passes, developer products, subscriptions, Robux Transfer fees, paid private servers, paid access priced in Robux, Roblox Plus incentives, in-game ad publishing, and **Creator Rewards**.
  - Roblox "maintains the exclusive right to decide if any Robux qualifies as Earned Robux."
  - Source: [Creator docs: Developer Exchange](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md).
- **U.S. 18+ DevEx rate of $0.0054**, effective **2026-06-08** [OFFICIAL]:
  - It applies to developer products, passes, subscriptions and private servers bought by U.S. players who have age-verified as 18+.
  - Only eligible games qualify. Player characters must be articulated humanoid (R15-type) for 100% of active playtime, and any R6 option disqualifies the game.
  - Source: [Creator docs: U.S. 18+ exchange rate](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/18-plus-devex-rate.md).
- **Marketplace fee:**
  - [3P (s.s.)] Roblox keeps a 30% marketplace fee on in-game sales, so the developer gets 70% of the Robux price. The same explainer puts the developer's "effective" share of player spend at about 25–35% once DevEx and Creator Rewards are combined, versus the ~22.7% DevEx/bookings ratio I derive in Inferences below. Source: [rolearn.dev revenue-share explainer](https://rolearn.dev/insights/roblox-developer-revenue-share-2026/).
  - [OFFICIAL] This is consistent with the subscriptions doc, which says Robux-priced subscriptions earn "70% of the subscription value every month." Source: [Creator docs: Subscriptions](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/subscriptions.md).

**Game-level benchmarks:**
- **GameAnalytics 2026 Roblox Benchmark Report** [3P, large sample]:
  - Sample: 500+ Roblox titles with ≥1M MAU between 2025-08-01 and 2026-07-31; 4.76B sessions.
  - **Payer conversion: 3.80%.**
  - **ARPPU: median $0.70; top 10% $2.33; top 5% $4.80; top 1% $55.31.**
  - **Retention: median D1 10.3%, D7 1.6%, D30 0.5%.**
  - The summaries don't say whether conversion and ARPPU are per day or per period. GameAnalytics usually reports daily figures.
  - Sources: [GameAnalytics 2026 report](https://www.gameanalytics.com/reports/2026-roblox-report); [Mellow / gamedevreports summary](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox).
- **GameAnalytics 2025 Roblox Benchmark Report** (data Jan 2023–Jul 2025) [3P]:
  - **Median D1 retention by average session length:**
    - 0–3 minute sessions: 4.31%.
    - 4–6 minute sessions: about 6%, and 11–13% for higher performers.
    - 19+ minute sessions: double-digit D1 and about 2 sessions per day.
  - **ARPPU:**
    - 13–18 minute sessions: median just over $1.20, with the best games above $6.
    - 25+ minute sessions: the best games drive $10+ per payer.
  - Source: [GameAnalytics 2025 report](https://www.gameanalytics.com/reports/2025-roblox-report).
- **Roblox's own benchmark example** [OFFICIAL, illustrative]: "10% of games with similar players have a Day 1 Retention of 18.73% or higher" and "50% … 12.11% or lower." Roblox now overlays benchmarks from similar games, falling back to genre benchmarks, in Creator Analytics. Source: [Creator docs: Analytics – retention/overview](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/analytics/retention.md).
- **How Roblox defines conversion** [OFFICIAL]: Roblox treats conversion rate as "one of the most important metrics." It also notes that "a high ARPPU and low ARPDAU suggest revenue comes from a limited user subset." Source: [Creator docs: Analytics – monetization](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/analytics/monetization.md).

**Case studies and rules of thumb:**
- [ANECDOTE (s.s.)] A developer who worked on games totaling 210M visits gives this rule of thumb: **daily Robux income ≈ 100 × CCU**, so 1k CCU earns about 100k Robux per day. He adds that this "highly depends on monetization, game genre, demographic." Source: as relayed by [RoWatcher, "The Roblox Income Ladder"](https://rowatcher.com/news/the-roblox-income-ladder-what-developers-really-earn).
- [ANECDOTE (s.s.)] A DevForum-cited **500–1,000 CCU game with poor monetization made only 1,000–1,250 Robux per day**. Source: [RoWatcher](https://rowatcher.com/news/the-roblox-income-ladder-what-developers-really-earn).
- [3P-EST (s.s.)] A "decently-monetized 100 CCU game" makes about 50k–150k Robux a year (about $190–$570). Source: [RoWatcher](https://rowatcher.com/news/the-roblox-income-ladder-what-developers-really-earn).
  - **This conflicts with the 100× rule**, which would imply about 3.65M Robux a year at 100 CCU.
- [3P-EST] Games around **2,000–3,000 CCU can reach about $10,000 a month "when monetization works."** Source: [StealWhatWorks blog](https://stealwhatworks.com/blogs/news/roblox-games-over-10k-month-now).
- [3P-EST] **Fisch** made an estimated **$3–6M in Q1 2026 at about 110,000 average CCU** (about 4B lifetime visits). Source: [RoWatcher, highest-earning games 2026](https://rowatcher.com/news/the-10-highest-earning-roblox-games-in-2026-and-what-they-mean-for-the-platform).
- [3P-EST] **Dress to Impress** made an estimated $2–5M per quarter in Q1 2026, mostly from cosmetics and seasonal passes. Source: [RoWatcher](https://rowatcher.com/news/the-10-highest-earning-roblox-games-in-2026-and-what-they-mean-for-the-platform).
- [PRESS] **Blue Lock: Rivals** (released June 2024) at times had over 1M concurrent players and generated "$5 million/month in in-game purchases" before DoBig Studios bought it for $3M. Source: [Tubefilter, 2025-07-14](https://www.tubefilter.com/2025/07/14/indie-game-creators-are-making-millions-selling-their-roblox-worlds/).
- [PRESS] **Grow a Garden** earned **$12M in May 2025** from virtual item sales. Some estimates put the owners at about $20M a month at the peak. Source: [Calcalist](https://www.calcalistech.com/ctechnews/article/dj4lxef8r).
  - [3P-EST] Lifetime revenue was estimated at $286.8M as of September 2026. Source: [profitable.app](https://profitable.app/roblox/games/grow-a-garden).
- [PRESS/EST (s.s.)] **Steal a Brainrot** earned an estimated ~US$64M in real-money in-game purchases between its May 2025 launch and about March 2026. Source: [The Star (Bloomberg syndication), 2026-03-25](https://www.thestar.com.my/tech/tech-news/2026/03/25/robloxs-hit-game-steal-a-brainrot-battles-its-many-imitators).

### Inferences
- **Top-down calibration from Q2 2026 official numbers:**
  - DevEx ÷ hours = $363M ÷ 29B ≈ **$0.0125 per engagement-hour**.
  - One average CCU equals about 730 player-hours a month, so that is **≈ $9 of DevEx per average-CCU-month**.
  - Bookings ÷ hours ≈ $0.055 per hour, and DevEx ≈ 22.7% of bookings. That is roughly the platform-wide share of each player dollar that reaches creators.
  - Caveat: DevEx also pays UGC/avatar-item creators and Creator Rewards, and it lags earnings. Game-only figures are somewhat lower, and the median game sits well below the mean because spend is skewed.
- **Bottom-up check:** 100 Robux/CCU/day ≈ 3,040 Robux/CCU/month ≈ **$11.6 at $0.0038**. This matches the top-down figure, which suggests the "100×" rule describes an average-to-good monetizer, not a typical small game.
- **Implied range from the case studies:**

  | Game / case | Implied DevEx per average-CCU-month |
  |---|---|
  | Fisch (3P estimate) | about $9–$18 |
  | Steal a Brainrot (assuming ~1M average CCU) | about $6 |
  | Poorly monetized DevForum anecdote | about $0.11–$0.29 |

- **Working planning band:**
  - $1–$15 per average-CCU-month overall.
  - About **$5–$10 for a competently monetized progression, simulator, tycoon or co-op survival game**.
  - Under $2 for hangout, obby or very-young-audience games.
  - The ×10–×100 spread between good and bad monetization at the same CCU is the single biggest lever.
- **Converting DAU to CCU:** average CCU ≈ DAU × average minutes per DAU ÷ 1,440. For example, 10,000 DAU × 30 minutes ≈ 208 average CCU. Across the platform in Q2 2026, 29B hours ÷ 91 days ≈ 319M hours a day, which is about 13.3M average concurrent users and about 2.6 hours per DAU per day, spread across all experiences.
- Visits measure session starts, not hours, so they are a poor proxy for revenue. Use CCU-hours or DAU × playtime instead.

### Gaps
- No official Roblox figure for revenue per CCU, or for ARPDAU by genre.
- The RoMonitor Stats and Rolimons revenue-estimate pages couldn't be fetched (egress blocked), and their methods aren't public.
- I couldn't confirm whether GameAnalytics' 3.80% conversion and $0.70 ARPPU are daily or period figures.
- The DevForum posts behind the anecdotes couldn't be read directly. RoWatcher, StealWhatWorks and profitable.app numbers are unaudited.
- I couldn't verify the current Robux retail price per USD, so the player-dollar share is derived only from the DevEx/bookings ratio.

---

## 2. What average CCU nets ~US$3,000/month, and how common is that?

### Takeaway
A reasonably monetized game needs roughly **250–1,000 *sustained average* CCU** to make about $3k a month in DevEx. That is about **6,000–30,000 DAU**, depending on playtime. A weakly monetized game may need 3,000+ CCU. Hitting $36k a year probably puts a creator around the **top few thousand of the ~42,000 DevEx participants**, far above the official **~$1,500 median**.

### Cited Findings
- **RDC 2026** (published around 2026-09-11 to 09-13; covers the 12 months ending 2026-06-30) [OFFICIAL via PRESS]:
  - **More than 42,000 creators participate in DevEx.**
  - **The median DevEx creator received about $1,500 for the year.**
  - The **top 1,000 averaged $1.4M**, the **top 100 averaged $10.8M**, and the **top 10 averaged $65.7M**, up from $33.9M in the previous report.
  - Sources: [TweakTown](https://www.tweaktown.com/news/113585/robloxs-top-10-creators-averaged-dollars65-7-million-each-while-the-median-made-dollars1500-and-roblox-everywhere-is-the-fix/index.html); [Dexerto](https://www.dexerto.com/roblox/robloxs-top-creators-average-65-7-million-a-year-but-most-make-far-less-3408675/); [TechSpot](https://www.techspot.com/news/113855-roblox-top-creators-making-65-million-year-while.html).
- The previous report had the top 1,000 creators averaging $1.3M in 2025. Source: [GamesHub](https://www.gameshub.com/news/article/roblox-creator-earnings-2025-report-millionaire-developers-2856170/).
- **Official thresholds that hint at what Roblox counts as a "real" game:**
  - Creator Rewards **Audience Expansion pays only if the experience "maintains an average of 100+ DAU for 60 days."** Source: [Creator docs: Creator Rewards](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-rewards.md).
  - Rewarded video ads need a public game with **at least 2,000 unique visitors a month**. Source: [Creator docs: Rewarded video ads](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/promotion/rewarded-video-ads.md).
  - Price optimization generally needs **about 60,000 transactions in the previous 30 days**, so small games can't use it. Source: [Creator docs: Price optimization](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/price-optimization.md).
  - The Brand Developer Directory requires at least one game with **4M+ MAU and a 65% like score**. Source: [Creator docs](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-programs/brand-developer-directory.md).
- **Concentration** [3P (s.s.)]: a live tracker following 2,705 games reported about **61% of concurrent players in the top 100 games**. The search summary didn't make clear whether the tracker was [rblxdb](https://rblxdb.com/roblox-player-count) or [rtrack.live](https://rtrack.live/insights/Live/Concurrent).
- **Retention base rates** [3P]: even among GameAnalytics' already-successful sample (≥1M MAU), the median game keeps only 0.5% of new users at D30. Source: [GameAnalytics 2026](https://www.gameanalytics.com/reports/2026-roblox-report).

### Inferences
- **Average CCU needed for $3,000 a month of DevEx (gross, before contractors, ads and tax):**

  | DevEx per average-CCU-month | Typical case | Average CCU needed |
  |---|---|---|
  | $12 | strong monetization | ≈ 250 |
  | $9 | platform average | ≈ 330 |
  | $6 | — | ≈ 500 |
  | $3 | mediocre | ≈ 1,000 |
  | $1 | hangout / young audience | ≈ 3,000 |

  - At 30 minutes of average daily playtime, 330 average CCU ≈ 16,000 DAU. At 60 minutes it's ≈ 8,000 DAU.
  - Creator Rewards could add about 10–35% on top; see the calculation in section 6.
- **Rough rank estimate:**
  - The top 1,000 creators took about $1.4B of the $1.7B (about 82%).
  - The remaining ~41,000 participants shared about $0.3B, an average of roughly $7k each against a $1.5k median.
  - $36k a year is about 5× that average, which plausibly places a creator around **rank 2,000–4,000 (top ~5–10% of DevEx participants)**. This is very uncertain.
  - The ~42k DevEx participants are themselves a small, self-selected group that cleared the 30,000-Robux minimum.
  - DevEx participants also include UGC/avatar-item creators, so the share of *game* developers at this level could differ.
- The top-10 average roughly doubled while the median stayed around $1.5k. Breakout hits drive aggregate growth, but that growth doesn't reach typical creators.

### Gaps
- **No reliable public distribution of experiences by CCU** (how many reach 100, 500 or 1,000+ CCU). A "~7 million active experiences (Q3 2025)" figure appeared in a search summary with no verifiable source.
- The RoMonitor, Rolimons and Rotrends lists that could support counts weren't accessible.
- No official histogram of DevEx earnings, only the median and top-N averages.

---

## 3. 2025–2026 genre and trend landscape; breakout hits; the fast-follow strategy and where inspiration ends and infringement begins

### Takeaway
The 2025 mega-hits (Grow a Garden, Steal a Brainrot, 99 Nights in the Forest, Dead Rails) were built by tiny teams in weeks to a few months. They shared a few traits:
- simple collect / grow / steal / survive loops
- strong social or competitive interplay
- meme or collectible content
- very frequent content drops and scheduled "events"

Fast-following is the dominant industry behavior and clones appear within days to weeks. But Roblox now officially deprioritizes near-duplicate games in recommendations, and hit owners are filing lawsuits. Mechanics and ideas are free to borrow; specific expression (names, art, models, code, UI, thumbnails, place files) is not.

### Cited Findings
**Breakout hits:**
- **Grow a Garden** [PRESS]:
  - Launched March 2025 by a teen creator and earned $12M in May 2025. The original creator is estimated to still own about half the game. Source: [Calcalist](https://www.calcalistech.com/ctechnews/article/dj4lxef8r).
  - Reached nearly 22M CCU in July 2025. Source: [Game Developer](https://www.gamedeveloper.com/business/roblox-s-grow-a-garden-had-nearly-22-million-concurrent-users-in-july).
  - Its all-time peak of 22,346,725 CCU was later passed by Steal a Brainrot. Source: [RTC on X](https://x.com/Roblox_RTC/status/1966948186653863995).
- **Steal a Brainrot** [PRESS]:
  - Developed by SpyderSammy, owned by **DoBig Studios**, launched **2025-05-16**. It averaged about 1M CCU in September 2025. Source: [Wikipedia: Steal a Brainrot](https://en.wikipedia.org/wiki/Steal_a_Brainrot).
  - Holds the Guinness record of **25,868,678 concurrent players on 2025-10-11**. Sources: [Guinness World Records](https://www.guinnessworldrecords.com/world-records/503322-most-concurrent-players-for-a-videogame-made-in-roblox); [PocketGamer.biz](https://www.pocketgamer.biz/robloxs-steal-a-brainrot-becomes-first-game-to-surpass-25m-concurrent-players/).
  - Design: a tycoon base fused with steal-and-defend PvP and a meme aesthetic. Source: [Beebom](https://beebom.com/robloxs-steal-a-brainrot-delivered-a-2025-masterclass-in-player-engagement-and-gave-uefn-a-second-wind/).
- **The "admin abuse" event war** [PRESS]: Grow a Garden and Steal a Brainrot scheduled competing live events against each other. That rivalry helped set a Roblox platform record of about 47M concurrent players in August 2025. Source: [Tubefilter, 2025-08-25](https://www.tubefilter.com/2025/08/25/roblox-grow-garden-steal-brainrot-admin-war-record/).
- **99 Nights in the Forest** [PRESS / wiki]:
  - Created **2025-03-04** by Grandma's Favourite Games. It's a co-op survival-horror game with a CCU record of 14,153,173. Sources: [Roblox Fandom wiki](https://roblox.fandom.com/wiki/Grandma's_Favourite_Games/99_Nights_in_the_Forest); [games.gg](https://games.gg/news/99-nights-forest-14-million-roblox/).
  - 20th Century Studios has acquired the theatrical film rights. Source: [TheWrap](https://www.thewrap.com/creative-content/movies/20th-century-studios-roblox-game-99-nights-in-the-forest/).
- **Dead Rails (RCM Games)** [PRESS / blog]:
  - Created **2025-01-01** and featured by Roblox's official channels in late February 2025.
  - Average session is about 18 minutes.
  - It monetizes "Bonds" used for revives and class unlocks.
  - Sources: [Max Power Gaming](https://www.maxpowergaming.co/post/how-dead-rails-became-hottest-roblox-game); [games.gg](https://games.gg/news/dead-rails-roblox-zombie-game/); [Fandom](https://roblox.fandom.com/wiki/RCM_Games/Dead_Rails).
- **Blue Lock: Rivals** [PRESS]: built by an anonymous 19-year-old **in about 3 months** (released June 2024). It at times drew over 1M CCU and was sold to DoBig for $3M. Source: [Tubefilter](https://www.tubefilter.com/2025/07/14/indie-game-creators-are-making-millions-selling-their-roblox-worlds/).
- **Fisch** [3P-EST]: about 110k average CCU and about 4B visits in Q1 2026. RoWatcher frames it as proof that "the top tier is not permanently locked." Source: [RoWatcher](https://rowatcher.com/news/the-10-highest-earning-roblox-games-in-2026-and-what-they-mean-for-the-platform).

**Genre waves:**
- [3P (s.s.)] Fastest-moving categories in 2024–25:
  - steal-and-defend tycoons
  - idle-grow simulators
  - co-op horror (Doors, Forsaken, 99 Nights)
  - anime fighters (Type Soul, Blade Ball)
  - fashion and social (Dress to Impress)
  - mobile-first shooters (Rivals)
  - Source: [Game-Ace blog](https://game-ace.com/blog/roblox-trends-in-gaming/).
- [PRESS (s.s.)] The "Italian brainrot" meme wave came out of TikTok and Instagram in early 2025. Source: [MarketScreener](https://www.marketscreener.com/news/how-roblox-brainrot-games-are-taking-over-ce7d5fd8d98bf62c).

**2026 (low confidence):**
- [3P listicles] Murder Mystery 2 was reported as the top game by CCU in July 2026 (about 545.9K). A "Grow a Garden 2" released June 2026 was reported at about 454K CCU. 99 Nights was called 2026's leading horror game at 400–450K CCU. Sources: [StudioKrew, July 2026](https://studiokrew.com/blog/top-roblox-games-july-2026/); [games.gg 2026](https://games.gg/news/best-roblox-games-2026/).
- **Unverified.** No reliable press confirms a 2026-born mega-hit on the scale of Steal a Brainrot or Grow a Garden.

**Fast-follow and clones:**
- [PRESS] Roblox developers clone viral Steam and indie hits within days to weeks, often near one-to-one including the UI, and some clones outperform the originals with younger players. Sources: [Windows Central](https://www.windowscentral.com/gaming/how-roblox-theft-is-becoming-a-big-problem); [PC Gamer, on the Peak developers](https://www.pcgamer.com/games/action/peak-dev-would-rather-you-pirate-peak-than-play-a-microtransaction-roblox-slop-ripoff/); [GamesRadar](https://www.gamesradar.com/games/simulation/the-robloxification-of-steam-creator-of-viral-game-apologizes-after-slop-rip-offs-flood-valves-store/); [Plagiarism Today, 2026-09-17](https://www.plagiarismtoday.com/2026/09/17/the-attack-of-the-roblox-clones/).
- [PRESS] Hit owners are litigating. **Since November 2025, Steal a Brainrot developers Spyder Games and Speedy Simulator Gaming have filed at least four lawsuits** against alleged imposters, including a website hosting 12 near-identical copies. Sources: [Bloomberg, 2026-03-24](https://www.bloomberg.com/news/articles/2026-03-24/roblox-s-hit-game-steal-a-brainrot-battles-its-many-imitators); [The Star](https://www.thestar.com.my/tech/tech-news/2026/03/25/robloxs-hit-game-steal-a-brainrot-battles-its-many-imitators).
- [ANECDOTE] A 2026 DevForum thread is titled "Someone copied my game 1:1 turned it into ai slop and is getting more players." Source: [DevForum](https://devforum.roblox.com/t/someone-copied-my-game-11-turned-it-into-ai-slop-and-is-getting-more-players/4840355).

**Roblox's rules:**
- [OFFICIAL] Roblox's discovery documentation says:
  - **"Non-unique games — Games with metadata and place files that closely resemble existing games on Roblox are no longer prioritized for recommendations and might rank lower in search results."**
  - Creators should "Avoid publishing content with repetitive titles and images that have been previously published."
  - Source: [Creator docs: Discovery](https://github.com/Roblox/creator-docs/blob/main/content/en-us/discovery.md).
- [OFFICIAL] Roblox's IP policy:
  - "Copyright does not protect facts or ideas, but it may protect the specific expression of a fact or idea."
  - Crediting the original creator is not a defense.
  - Roblox suspends or terminates repeat or egregious infringers.
  - Knowingly false DMCA notices create liability under §512(f).
  - Source: [Creator docs: IP guidelines](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/publishing/ip-guidelines.md).
- [OFFICIAL] **Rights Manager** (announced April 2024) is the tool IP owners use to file removal requests. Creators have complained that it's abused with false claims to take down original games. Source: [DevForum: Introducing Rights Manager](https://devforum.roblox.com/t/introducing-rights-manager/2880717).
- [OFFICIAL] **Licensed IP route:**
  - Creators can request a "Full game" or "In-game sales" license from the Licenses catalog, under a revenue share the rights holder sets.
  - Rights holders can also send offers to games that Roblox detects "making prominent use of a registered IP," and ignoring such an offer can lead to an infringement claim.
  - Sources: [Creator docs: IP licensing for creators](https://github.com/Roblox/creator-docs/blob/main/content/en-us/ip-licensing/creators.md); [Tubefilter, 2025-07-15](https://www.tubefilter.com/2025/07/15/roblox-ip-platform-netflix-blue-lock-creator-revenue-share-transformative-works/amp/).
- [OFFICIAL] **Standout Games** is a daily, hand-curated Home sort for *novel* games: unique mechanics, distinctive visuals, or an underrepresented genre. Developers can nominate their own game through a survey. Source: [Creator docs: Standout Games](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-programs/standout-games.md).

### Inferences
- **What the 2025 hits had in common:**
  - one-sentence core loops, such as plant → wait → sell, or buy → defend → steal
  - social conflict or cooperation
  - collectible or meme content that is cheap to produce in volume
  - scheduled, hyped live events
  - very fast update cadence
  - builds measured in weeks to about 3 months
  - These favor a fast, systems-strong scripter: economy, data persistence, server authority and anti-exploit work are the hard parts. Art can stay simple.
- **Trend windows are short.** Steal a Brainrot went from launch (May 16) to record (September) in about 4 months, and clones flooded in within weeks. The value of a pure fast-follow decays quickly.
  - The safer play is a **"genre-follow with a distinct twist."** Keep the genre's core loop but change the theme, the social mechanic, or the progression layer.
  - Avoid a near-copy, which now risks discovery deprioritization, DMCA takedowns, and lawsuits from well-funded owners like DoBig and Spyder Games.
- **Practical line:**
  - **OK to reuse:** genre conventions and mechanics, such as stealing from bases, growing plants, or surviving nights.
  - **Not OK to copy:** names or confusingly similar branding, logos, thumbnails, models and meshes, UI layouts and art, audio, place files, and code.
  - Ripping Steam or indie games one-to-one creates reputational and legal exposure, and Roblox's non-unique filter counts against it too.
- For older audiences, licensed IP through License Manager is a legitimate route to known IP, but the rights holder sets the revenue share and approval is discretionary.

### Gaps
- No reliable press confirming 2026-born breakouts, or why they worked. 2026 names come from low-quality listicles.
- No primary data on **The Strongest Battlegrounds** revenue or design drivers. The only DTI figures are third-party estimates.
- The Naavik article ["Predicting the Next Big Hits on Roblox"](https://naavik.co/digest/predicting-the-next-big-hits-on-roblox/) couldn't be read (blocked).
- No data on how many clones Roblox removes or how outcomes of non-unique-game deprioritization are measured.

---

## 4. Discovery in 2025–2026: how recommendations work, which metrics matter, and the impact of age-gating

### Takeaway
"Recommended For You" (RFY) on Home works in two stages:
1. **Retrieval:** a game gets considered once a handful of plays come in from any source.
2. **Ranking:** a personalized ranking tests the game daily on small cohorts and **only counts users who arrived organically through RFY**.

Since **June 2026**, ranking uses play-through rate, first-play bounce, play days and playtime across D1, D2–7 and D8–28 (a 28-day window, up from 7), plus co-play and spend. The old single "qualified play-through rate" was removed.

Mandatory age checks for chat (worldwide from January 2026) cut DAU from about 152M to 123M. They also shifted spending power toward verified older users, which Roblox now explicitly rewards with an 18+ DevEx premium.

### Cited Findings
- **June 2026 overhaul** [OFFICIAL]:
  - Roblox published "Optimizing Discovery: How Great Games Reach Millions of Players" and a DevForum post, "Recommended For You Algorithm Improvements That Better Value Long-Term Retention."
  - **QPTR was removed.** Play-through rate and first-play bounce rate were added. The old metric's components were split into separate play-through, session-quality and spend signals.
  - **The evaluation window grew from 7 to 28 days.**
  - Sources: [Roblox Newsroom (June 2026)](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox); [DevForum announcement](https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575); [Endsights summary](https://endsights.com/roblox-optimizing-discovery-how-great-games-reach-millions-of-players-on-roblox); [Zehn Studio summary](https://zehn-studio26.com/news/recommended-for-you-retention-update/).
- **Current ranked signals** [OFFICIAL]:
  - **Most important:**
    - play-through rate
    - **first-play bounce rate** (negative: early exits within about 60–180 seconds)
    - **play days per user** (D1, D2–D7, D8–D28)
    - **playtime per user** (capped at **60 minutes per user, per game, per day**)
  - **Important:**
    - intentional co-play days (friends via invites or private servers)
    - qualified play sessions
    - **spend days per user**
    - **Robux spent per user**
  - Source: [Creator docs: Discovery](https://github.com/Roblox/creator-docs/blob/main/content/en-us/discovery.md).
- **Two-stage system** [OFFICIAL]:
  - Retrieval can be triggered when "games that have even a small number of people playing" signal worth.
  - **"Roblox doesn't count the engagement, monetization, or retention of users first acquired from ads, curation, friends, search, social media, or any other source in the ranking stage."**
  - Source: [Creator docs: Discovery](https://github.com/Roblox/creator-docs/blob/main/content/en-us/discovery.md).
- **Discovery FAQ** [OFFICIAL]:
  - Retrieval needs "only a very low minimum number of plays from any source."
  - "The algorithm tests your game daily, and if it sees improving performance, it increases impressions."
  - New games don't have to wait 28 days. Signals are staged: D1 first, then D2–7, then D8–28.
  - About 100 games are shown on each user's Home page.
  - Genre is "not an explicit ranking factor," and finite or story games are not penalized.
  - Weekly seasonality "usually peaks on a Saturday."
  - Competitors' improvements can cancel out your own gains.
  - Play-through rate temporarily drops as impressions scale up.
  - Advice: "If retention is low, focus on core gameplay first. Once retention is strong, improving monetization can help you increase your Home impressions."
  - Source: [Creator docs: Discovery FAQ](https://github.com/Roblox/creator-docs/blob/main/content/en-us/discovery-faq.md).
- **Explore and expand** [OFFICIAL]: content updates often produce a spike of RFY users ("explore"). If that cohort engages and monetizes well, Roblox recommends the game to more similar cohorts ("expand"). Source: [Creator docs: Discovery](https://github.com/Roblox/creator-docs/blob/main/content/en-us/discovery.md).
- **Visibility penalties** [OFFICIAL]:
  - "Leading with giveaways" or other monetary implications. Roblox's example is a game titled "Robux! Play now!"
  - Mismatched metadata and content.
  - Non-unique games.
  - Creator Dashboard shows a daily quality banner.
  - Source: [Creator docs: Discovery](https://github.com/Roblox/creator-docs/blob/main/content/en-us/discovery.md).
- **Other discovery surfaces** [OFFICIAL]: Continue Playing, Friends, Sponsored, Curated sorts, Standout Games, semantic search, Discover/Charts, Experience Events (up to 5 promo thumbnails), and experience notifications. Source: [Creator docs: Discovery](https://github.com/Roblox/creator-docs/blob/main/content/en-us/discovery.md).
- **Charts:**
  - [OFFICIAL] "Top Playing Now," a real-time CCU sort, was added in April 2025. Source: [DevForum](https://devforum.roblox.com/t/introducing-top-playing-now-on-charts/3529809).
  - [wiki] Charts has about 29 sorts, including Up-and-Coming. Source: [Roblox Fandom: Charts](https://roblox.fandom.com/wiki/Charts).
- **Thumbnail personalization** (needs 2+ active thumbnails) [OFFICIAL]: in testing, games saw an **average +8.5%** in qualified play-through rate, and some saw +50%. Source: [Creator docs: Thumbnails](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/publishing/thumbnails.md).
- **RDC 2026** (2026-09-11) [OFFICIAL via PRESS]:
  - **"Moments":** short gameplay videos that launch straight into the game. Fully available in the U.S.; video on experience detail pages comes later.
  - **"Roblox Everywhere":** standalone apps for mobile, PC and console, plus Chrome launch by the end of 2026.
  - Sources: [PocketGamer.biz](https://www.pocketgamer.biz/roblox-unveils-new-play-creation-and-monetisation-tools-at-rdc-2026/); [Inven Global](https://www.invenglobal.com/articles/25918/roblox-unveils-expansions-to-play-creation-and-monetization-at-rdc).
- **Age checks** [OFFICIAL / PRESS]:
  - Rolled out for chat starting December 2025 in Australia, New Zealand and the Netherlands, then **mandatory worldwide in January 2026**.
  - Uses facial age estimation from a video selfie.
  - Brackets are roughly under 9, 9–12, 13–15, 16–17, 18–20 and 21+.
  - Sources: [Roblox IR](https://ir.roblox.com/news/news-details/2026/Roblox-Requires-Users-Worldwide-to-Age-Check-to-Access-Chat/default.aspx); [Biometric Update](https://www.biometricupdate.com/202511/roblox-to-make-age-assurance-for-chat-mandatory-as-of-january-2026); [GameSpot](https://www.gamespot.com/articles/roblox-has-added-facial-age-verification-with-very-mixed-results/1100-6537378/).
- **Age-check impact** [OFFICIAL via PRESS]:
  - **DAU fell from about 152M (Q3 2025) to 144M (Q4 2025), 132M (Q1 2026) and 123M (Q2 2026).**
  - The CEO cited "greater-than-expected headwinds" that slowed new-user acquisition and restricted communication for users who hadn't age-checked.
  - By the end of Q1, 51% of global DAU (65% in the U.S.) had age-checked.
  - The 18–34 cohort grew more than 50%.
  - **U.S. users over 18 spend about 50% more than under-18 users.**
  - FY2026 bookings growth guidance was cut from 22–26% to **8–12%**.
  - Sources: [Respawn/Outlook](https://respawn.outlookindia.com/gaming/gaming-news/roblox-bets-on-safety-and-adults-over-user-volume); [Tech-Insider](https://tech-insider.org/roblox-age-verification-2026/); [Seeking Alpha](https://seekingalpha.com/news/4583513-roblox-forecasts-2026-revenue-growth-of-20-percentminus-25-percent-as-safety-changes-drive); [Motley Fool Q1 2026 transcript](https://www.fool.com/earnings/call-transcripts/2026/04/30/roblox-rblx-q1-2026-earnings-call-transcript/).
- **Content maturity labels** [OFFICIAL]:
  - Labels drive Home and Charts recommendations by age group.
  - Games without the maturity questionnaire have restricted playability.
  - "Restricted" games are open only to age-verified 18+ users and can't be played in some countries, including Korea, Saudi Arabia and Türkiye.
  - Games whose primary theme is a sensitive issue are 16+, and they're only recommended to age-verified users.
  - Source: [Creator docs: Content maturity](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/promotion/content-maturity.md).

### Inferences
- **Metric priorities for a new game:**
  - **Play-through rate:** icon, thumbnail and title must match what's in the game.
  - **First-play bounce:** the first 60–180 seconds must deliver the core fantasy with no friction.
  - **D2–7 and D8–28 play days:** daily rewards, streaks, timed events, collection goals.
  - **Co-play:** party and invite systems, private servers.
  - **Spend days and Robux spent:** monetization should start early but stay non-hostile.
- Ads, YouTube, TikTok, friends and search traffic **can trigger retrieval but can't buy ranking**. The organic RFY cohort has to perform. That makes external traffic a test and ignition tool, not a substitute for retention.
- The 28-day window should favor games with long-tail retention, such as progression, collection and social games, over short fads with strong D0 but weak D8–28.
  - For a small team, that means building at least 2–4 weeks of goals and an update calendar *before* pushing traffic.
- Age-gating moves value toward verified 13+ and 18+ audiences: higher spend, the 18+ DevEx rate, and Roblox's stated growth in the 18–34 cohort. It may also hurt chat-heavy social or hangout designs that relied on unverified kids chatting. **This is an inference, not directly sourced.**
- Daily testing, plus "explore" spikes after updates, makes **regular content updates part of the discovery engine itself**, not just a retention tool.

### Gaps
- No public numbers on the share of impressions given to new games, or on typical play-through or bounce thresholds.
- The Up-and-Coming sort's criteria aren't documented. One source reported a developer complaint that it lists games with 10K–200K+ CCU, but I couldn't attribute it.
- No genre-level data on how age checks affected engagement or revenue.

---

## 5. Paid user acquisition: Roblox Ads Manager and influencer / YouTube / TikTok marketing

### Takeaway
Roblox's official cost-per-play benchmarks (November 2025) are about **$0.007–$0.019 per play**, so $100 buys roughly 5,000–14,000 plays. That makes ads an excellent **testing and ignition tool**. But ad-acquired users don't count toward RFY ranking, and profitability depends on how much each acquired play spends. Roblox's own 2026 data says about two-thirds of games reinvesting up to 4% of earnings reached ROAS above 100%. Influencer pricing data is mostly unverified third-party rate cards.

### Cited Findings
- **Official benchmarks, as of 2025-11-11** [OFFICIAL]:

  | Objective | Average cost per play |
  |---|---|
  | Maximize Plays | $0.0073 |
  | Drive Retention | $0.0113 |
  | Reactivate Users | $0.011 |
  | Acquire New Users | $0.0187 |

  - Home and Search campaigns were combined, and the classic campaign flow was retired.
  - Source: [DevForum: Ads Manager Updates – Home + Search Combined, New Benchmarks](https://devforum.roblox.com/t/ads-manager-updates-home-search-combined-new-benchmarks-and-sunsetting-the-classic-flow/4084863).
- **Acquire New Users objective** [OFFICIAL]: added in August 2025. It targets users who haven't visited your experience before, or not in the last 180 days. Source: [DevForum: Acquire New Users, Continuous Campaigns](https://devforum.roblox.com/t/ads-manager-updates-acquire-new-users-continuous-campaigns-and-more/3862159).
- [OFFICIAL (s.s.)] Roblox said the cost to get a player into a game was "over 71% cheaper," at under $0.01 per play, and that "Maximize Plays" is meant to help smaller creators launch new games. Source: [DevForum Ads Manager announcements](https://devforum.roblox.com/t/ads-manager-updates-acquire-new-users-continuous-campaigns-and-more/3862159).
- [OFFICIAL (s.s.)] At **RDC 2026**, Roblox said **over 1,200 games launched "Earnings" campaigns**, and **nearly two in three games that reinvested up to 4% of their earnings achieved ROAS above 100%**. It also added ROAS reporting and incrementality measurement. Source: [DevForum: Ads Manager RDC Recap – Earnings, ROAS Reporting & Incrementality](https://devforum.roblox.com/t/ads-manager-rdc-recap-earnings-roas-reporting-incrementality/4909790).
- [ANECDOTE] A July 2025 thread claimed the new Ads Manager was delivering "significantly worse results (x30 times worse)." Source: [DevForum](https://devforum.roblox.com/t/urgent-new-ads-manager-is-delivering-significantly-worse-results-x30-times-worse/3801409).
- **How Ads Manager works** [OFFICIAL]:
  - **Auction:** a second-price auction, where the winner pays the second-highest bid plus $0.01, using an adjusted eCPM.
  - **Search ads:**
    - also weigh how relevant the game is to the search query
    - reach only users aged 13+
    - can't be targeted
  - **Placement and creatives:**
    - campaigns run on both Home and Search
    - up to 10 16:9 thumbnails per campaign, with optional AI-generated variants
  - **Budget and payment:**
    - daily budgets
    - pay by card (18+), or convert Robux to ad credits (13+; irreversible; minimum 1 credit)
  - Sources: [Creator docs: Ads Manager](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/promotion/ads-manager.md); [Creator docs: Search ads](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/promotion/search-ads.md).
- **Third-party cost claims:**
  - [3P] Cost per visit runs about 4–12 Robux in 2026. Break-even example: a 2% payer rate × 80 Robux ARPPU yields only 1.6 Robux per visit, and "most developers running Roblox ads are losing money." Source: [RoWatcher, "Break-even math"](https://rowatcher.com/news/roblox-ads-in-2026-the-break-even-math-small-devs-ignore).
  - [3P] Sponsored experiences cost $0.10–$0.50 per click, with an average cost per play of $0.45 across 850+ promoted games. Sources: [Bloxg benchmarks](https://bloxg.com/statistics/roblox-advertising-benchmarks); [Bloxg ads guide](https://bloxg.com/guides/roblox-ads-guide).
  - **These conflict with Roblox's official benchmarks by about 20–60×.** They are likely older or use different definitions.
- **Influencer rates** [3P-EST, unverified]:

  | Channel size | Price per video |
  |---|---|
  | 1K–10K subscribers | $20–100 |
  | 10K–50K | $100–300 |
  | 50K–200K | $300–1,000 |
  | 200K–1M | $1,000–5,000 |
  | 1M+ | $5,000–25,000+ |

  - CPM deals run about $5–20 per 1,000 views.
  - Roblox YouTube channels themselves earn low RPMs ($0.50–2.00) because their audiences are young.
  - Sources: [Bloxg influencer guide](https://bloxg.com/guides/roblox-influencer-guide); [Hypertube](https://hypertube.io/blog/how-much-do-roblox-youtubers-really-make-2026-data).
- **Creator Rewards for influencers** [OFFICIAL]: members of Roblox's **Video Stars** program can earn Daily Engagement and Audience Expansion rewards. **Share Links** track off-platform acquisition. Source: [Creator docs: Creator Rewards](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-rewards.md).
- **Brand-deal rules** [OFFICIAL via PRESS]:
  - From **2026-05-04**, brand integrations must be registered and their assets moderated.
  - From **January 2027**, Roblox takes a revenue share on creator-negotiated brand deals. The percentage hadn't been disclosed when reported.
  - Some brand categories and rewarded formats are barred for users under 13.
  - Sources: [PocketGamer.biz](https://www.pocketgamer.biz/roblox-to-take-cut-of-in-game-brand-deals-from-2027-under-new-advertising-rules/); [Kidscreen](https://kidscreen.com/2026/03/23/roblox-plans-to-start-taking-a-cut-on-brand-deals/); [NetInfluencer](https://www.netinfluencer.com/roblox-to-take-cut-of-creator-brand-deal-revenue-starting-2027/).

### Inferences
- **Break-even on DevEx alone, at $0.0038 per Robux:**
  - A $0.0073 "Maximize Plays" play has to return about 1.9 Earned Robux, which is about **2.7 Robux of player spend** after the 30% fee.
  - A $0.0187 "Acquire New Users" player has to return about 4.9 Earned Robux, or about **7 Robux of spend**.
  - A game with 3–4% conversion and roughly 100+ Robux spend per payer within the attribution window can clear that bar. Weakly monetized games can't.
  - Creator Rewards and lifetime value beyond the window add upside.
- **Best use for a solo developer: cheap, statistically useful prototype tests.**
  - Spend about $50–$150 per prototype to get 5,000–20,000 plays and read play-through rate, first-play bounce, D1 and session length against benchmarks.
  - Use the same tool to ignite retrieval for a launch or a big update.
  - Scale spend only when Roblox's ROAS reporting shows more than 100%.
  - **These budgets are an inference from the official cost-per-play figures.**
- **Influencers / TikTok:**
  - These bring first plays, social proof and possibly Creator Rewards Audience Expansion income (35% of new or reactivated users' first $100 of spend). The game must keep 100+ DAU and the users must be new or lapsed for 60+ days.
  - That traffic doesn't feed RFY ranking, so it only pays off if the organic cohort metrics are already good.

### Gaps
- No official CPM or CPC for Sponsored ads, and no verified small-developer ROI case studies with dollar figures.
- No sourced data on TikTok marketing costs or outcomes for Roblox games.
- The influencer rate cards are unverified third-party content.

---

## 6. Monetization design: game passes vs developer products vs subscriptions vs rewarded video vs private servers; price points; live-ops; Creator Rewards

### Takeaway
Most revenue still comes from **passes (durables) and developer products (consumables)**, at 70% of the Robux price. The current toolkit layers several streams on top:
- subscriptions, priced in Robux or local currency (local-currency subs pay 70% in month one, then 100%)
- private servers
- **Creator Rewards**: 5 Robux per qualifying "Active Spender" day, plus 35% of new or reactivated users' first $100 of spend
- **Roblox Plus** incentives
- small ad income
- the **U.S. 18+ DevEx premium**

Managed pricing (regional pricing and price tests) is on by default for new items, but price tests need about 60k transactions a month. Paid random items require exact odds disclosure and must respect a policy API.

### Cited Findings
- **Pass price range** [OFFICIAL]: a pass can be priced from 1 Robux up to 1 billion Robux. Source: [Creator docs: Passes](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/passes.md).
- **Subscriptions** [OFFICIAL]:
  - **Pricing:**
    - auto-renewing
    - priced in Robux (minimum 49 Robux, regional pricing forced on) or in local currency (5 price tiers)
    - Robux prices can change only once every 60 days, with 30 days' notice for increases
  - **What you earn:**
    - **Local-currency subscriptions pay 70% in the first month and 100% from the second month on**, at $0.01 = 1 Robux. For example, a $5 subscription earns 350 Robux, then 500 Robux a month.
    - Robux-priced subscriptions pay 70% every month.
  - **Holds:**
    - local-currency earnings are held 30 days
    - Robux earnings are held about 5 days, the same as passes and developer products
  - **Constraint:** mutually exclusive tiers (Bronze/Silver/Gold) aren't supported.
  - Source: [Creator docs: Subscriptions](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/subscriptions.md).
- **Private servers** [OFFICIAL]: **changing the price cancels all active private-server subscriptions.** Source: [Creator docs: Private servers](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/private-servers.md).
- **Paid access in local currency** [OFFICIAL]:
  - The revenue share is **50%, 60% or 70% at $9.99, $29.99 or $49.99**.
  - Earnings are held in escrow at least 60 days.
  - Games that many players report as broken can be quarantined, with escrowed earnings refunded.
  - Sources: [Creator docs: Paid access (local currency)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/paid-access-local-currency.md); [Game Developer](https://www.gamedeveloper.com/business/roblox-rolls-out-higher-rev-share-plan-for-devs-making-premium-games).
- **Creator Rewards** [OFFICIAL]: this replaced Engagement-Based (Premium) Payouts and the Creator Affiliate program, effective **2025-07-24**.
  - **Daily Engagement:** **5 Robux per user per day**, if your experience is one of the first three that user plays that day for **10+ minutes** and the user is an **"Active Spender."** An Active Spender has made at least **$9.99** of qualifying purchases (Robux, Premium, UGC subscriptions) in the past 60 days and isn't a new or reactivated user.
  - **Audience Expansion:** **35% revenue share on the first $100 of qualifying purchases**, during the first 60 days, from New or Reactivated users (lapsed 60+ days) attributed to your experience.
    - Users can arrive via Share Links or as their first session that day.
    - The experience must keep **100+ average DAU for 60 days**.
  - Sources: [Creator docs: Creator Rewards](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-rewards.md); [Engagement-based payouts (deprecated)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/engagement-based-payouts.md); [Creator Affiliate (deprecated)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-programs/creator-affiliate.md).
- **Roblox Plus** (per the docs snapshot of 2026-10-02; launch date not verified) [OFFICIAL]:
  - Subscribers get 10%, then 20%, off eligible purchases. **Roblox subsidizes the discount, so developer earnings per sale are unchanged.**
  - Developers earn **250 Robux a month for 3 months (up to 750 Robux) per Plus subscriber recruited in-game** through `PromptRobloxSubscriptionPurchase`. These earnings have a 60-day hold.
  - Developers earn **up to 100 Robux per subscriber who spends 60+ minutes a month** in the game's paid private servers. Subscribers get those servers free.
  - Developers earn 10% of in-game Robux transfers made by Plus subscribers.
  - Hard-coded prices show the wrong amount to Plus subscribers, so prices should be displayed dynamically.
  - Source: [Creator docs: Roblox Plus](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/roblox-plus.md).
- **Rewarded video ads** [OFFICIAL]:
  - **Eligibility:** the creator must be 13+ and ID-verified, and the game must be public with **at least 2,000 unique visitors a month** and a completed Maturity & Compliance questionnaire.
  - **Earnings:** EPM (earnings per 1,000 impressions) × impressions.
  - **Tools:** a Creator Hub calculator estimates earnings, and Experiments can roll a placement out to a percentage of users.
  - Source: [Creator docs: Rewarded video ads](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/promotion/rewarded-video-ads.md).
  - Roblox opened rewarded video to more creators in mid-2025 and to "all ads eligible creators" later. Sources: [DevForum: More Creators Can Now Use Rewarded Video Ads](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678); [DevForum: Rewarded Video ads are now available to all ads eligible creators](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278?page=3).
  - [OFFICIAL (s.s.)] Roblox said that in the first months, rewarded video could make up to 3% of earnings, with a long-term goal of most creators growing revenue 5–10% through ads products. Completion rates of 90%+ and "Minimal" maturity ratings attract higher EPMs. Source: [DevForum: Ads for Creators – RDC Recap (September 2025)](https://devforum.roblox.com/t/ads-for-creators-rdc-recap-and-what%E2%80%99s-next/3929106).
  - [ANECDOTE (s.s.)] Reported EPMs are inconsistent: about $1.59 per 1,000 views, about 122 Robux per 1,000 impressions, and "1 Robux per impression" in some cases. Source: same DevForum threads.
- **Immersive ads (image and portal)** [OFFICIAL]: publishers earn per qualifying image impression or successful teleport, paid on the 25th of the following month, and fraud gets clawed back. Source: [Creator docs: Immersive ads](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/immersive-ads.md).
- **Managed pricing** [OFFICIAL]:
  - **Regional pricing** stays between **30% and 100% of the default price**.
  - **Price optimization** needs about **60,000 transactions in 30 days**, runs tests at least every 90 days, and only applies prices that produce positive incremental revenue.
  - **New games and new items are enrolled by default.**
  - Subscriptions, private servers and developer servers are regionalized automatically.
  - Hard-coded prices block testing.
  - Sources: [Managed pricing](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/managed-pricing.md); [Price optimization](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/price-optimization.md); [Regional pricing](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/regional-pricing.md).
- **Compliance for paid random items** [OFFICIAL]:
  - Any paid random item must disclose all outcomes and exact odds summing to 100%. This includes items bought indirectly through Robux-bought currency, keys or spins.
  - Odds boosters, such as a "lucky potion," must state their numerical effect.
  - Games must honor `ArePaidRandomItemsRestricted`: hide or block paid random items for restricted users, and don't let them trade the outcomes.
  - Free random rewards don't need disclosure.
  - Source: [Creator docs: Paid random items](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/paid-random-items.md).
- **Design guidance** [OFFICIAL]:
  - Item types: durable items (such as skins) and consumables (such as boosts).
  - Explain consumables in context. Roblox's example is the "Revives" in *Evade*.
  - Season passes with free and premium tracks tied to the core loop and spaced relative to average session length.
  - Bundles, VIP memberships, and subscription currency packs.
  - Source: [Creator docs: Monetization foundations](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/monetization-foundations.md).
- **Monetization and discovery** [OFFICIAL]: spend days and Robux spent per user feed RFY ranking. Roblox's advice: "Once retention is strong, improving monetization can help you increase your Home impressions." Sources: [Discovery FAQ](https://github.com/Roblox/creator-docs/blob/main/content/en-us/discovery-faq.md); [Discovery](https://github.com/Roblox/creator-docs/blob/main/content/en-us/discovery.md).
- **Live-ops example** [PRESS]: Dead Rails sells "Bonds" for revives and class unlocks. Source: [Max Power Gaming](https://www.maxpowergaming.co/post/how-dead-rails-became-hottest-roblox-game). The Grow a Garden / Steal a Brainrot scheduled live-event war drove record CCU. Source: [Tubefilter](https://www.tubefilter.com/2025/08/25/roblox-grow-garden-steal-brainrot-admin-war-record/).
- **Roblox Wallet** [OFFICIAL via PRESS]: lets creators manage and transfer real-currency earnings. It rolls out in late 2026 to U.S. creators aged 18+, then globally in 2027. Source: [PocketGamer.biz (RDC 2026)](https://www.pocketgamer.biz/roblox-unveils-new-play-creation-and-monetisation-tools-at-rdc-2026/).

### Inferences
- **Creator Rewards scale (assumption-heavy):**
  - Per 1,000 DAU, if q% qualify (Active Spender, game in their first three of the day, 10+ minutes), the payout is 1,000 × q × 5 Robux × 30 days × $0.0038.
  - **That's about $57 a month per 1,000 DAU at q = 10%**, or about $114 at 20%.
  - A game with 10,000 DAU (around the $3k/month scale) could earn about **$285–$1,140 a month** from Daily Engagement alone at q = 5–20%. That's material: about 10–35% on top of purchase revenue.
  - q is unknown. One weak proxy: 31M monthly unique payers against 132M DAU in Q1 2026.
- **Recommended mix** for a $3k/month target:
  - 2–4 durable passes (VIP, 2× currency, cosmetic or utility)
  - a laddered set of consumables (boosts, revives, currency packs)
  - a starter or value bundle
  - optionally one Robux-priced subscription that bundles daily currency and perks, which suits retention-led games
  - a free/premium season pass once the game has stable D7
  - always dynamic prices, so managed pricing and Roblox Plus display correctly
  - **Avoid paid gacha** unless odds disclosure and the policy-API gating are implemented perfectly.
  - This mix is synthesized from the official guidance above.
- **Ads are a minor stream for small games.** The 2,000-visitor threshold is easy to reach, but Roblox itself projects only about 3%, then 5–10%, of earnings. Use them only where they don't hurt retention signals.
- **Update cadence:** "explore" spikes after updates, daily testing, and the 28-day retention window all argue for weekly content drops or timed events while a game is growing. That cadence also fits the event-driven playbook of the 2025 hits.
- **Robux vs local-currency subscriptions:** at the same price, a local-currency subscription earns more than a Robux one from month two (100% vs 70%), but it can't be repriced and has a 30-day hold.

### Gaps
- No sourced data on revenue split by product type (passes vs products vs subscriptions vs private servers), or on subscription adoption rates.
- No reliable price-point benchmarks (for example, typical prices of best-selling passes and products by genre).
- No data on what share of DevEx Creator Rewards makes up, or on the typical share of a game's DAU that qualifies as Active Spenders.
- Rewarded-video EPMs are only anecdotal.

---

## 7. Costs and team: outsourcing, costs, timelines, "prototype fast and test many"

### Takeaway
A strong Luau scripter can own every system and outsource art, which is what the 2025 hit pattern rewards. Third-party rate cards suggest a lean prototype costs **a few hundred dollars** and a polished launch **low thousands**. Several 2025 hits went from creation to virality in **about 1–3 months**. Roblox's AI creation tools and its cheap per-play ads make a **portfolio of fast prototypes, measured against benchmarks**, cheaper than ever.

### Cited Findings
- [3P] Builder pricing: **$25–$150** for small builds, **$150–$500** for multi-zone hubs, **$500–$2,000** for full game worlds, and **$2,000+** for established premium builders. Source: [Bloxg building marketplace](https://bloxg.com/marketplace/services/building).
- [3P / DevForum (s.s.)] GUI commissions run about **$20–60 per design** (about 1.6k–4.8k Robux). Source: [DevForum: "How to be more firm with commission prices?"](https://devforum.roblox.com/t/how-to-be-more-firm-with-commission-prices/3143832).
  - The same summary contained an inconsistent Robux-to-USD conversion that I ignored.
- [DevForum, 2020, dated] Example of a larger UI job: a $1,500 vector UI commission. Source: [DevForum](https://devforum.roblox.com/t/vector-artist-needed-ui-design-commission-1500-usd/865084).
- [3P] Freelance Roblox developers cost about **€20 to €130+ per hour**. Source: [Game-Ace cost article](https://game-ace.com/blog/how-much-does-it-cost-to-make-a-roblox-game/).
- **Timelines from the 2025 hits** [PRESS / wiki]:
  - Blue Lock: Rivals was built in **about 3 months** by a solo 19-year-old. Source: [Tubefilter](https://www.tubefilter.com/2025/07/14/indie-game-creators-are-making-millions-selling-their-roblox-worlds/).
  - Dead Rails was created 2025-01-01 and featured by Roblox in late February 2025. Source: [Max Power Gaming](https://www.maxpowergaming.co/post/how-dead-rails-became-hottest-roblox-game).
  - 99 Nights was created 2025-03-04. Source: [Fandom](https://roblox.fandom.com/wiki/Grandma's_Favourite_Games/99_Nights_in_the_Forest).
  - Grow a Garden launched March 2025 and earned $12M by May 2025. Source: [Calcalist](https://www.calcalistech.com/ctechnews/article/dj4lxef8r).
  - Steal a Brainrot launched 2025-05-16 and set its record in September/October 2025. Source: [Wikipedia](https://en.wikipedia.org/wiki/Steal_a_Brainrot).
- [PRESS] A game that would take a year on PC "can be cloned and reimagined on Roblox in a matter of weeks." Source: [Windows Central](https://www.windowscentral.com/gaming/how-roblox-theft-is-becoming-a-big-problem).
- **Roblox AI tools, RDC 2026** [OFFICIAL via PRESS]:
  - The prompt-based **Build** tool has been used to publish about **9,000 games**, and **71%** of those creators had never used Studio.
  - **Scene Generator** (scenes from prompts and reference images) and **NPCs that playtest** are due by the end of 2026.
  - Sources: [PocketGamer.biz](https://www.pocketgamer.biz/roblox-unveils-new-play-creation-and-monetisation-tools-at-rdc-2026/); [Inven Global](https://www.invenglobal.com/articles/25918/roblox-unveils-expansions-to-play-creation-and-monetization-at-rdc).
- **Roblox Incubator** [OFFICIAL]: a **six-month, milestone-driven** program with **up to 40 teams per cohort**, for "small, experienced teams who have a strong prototype or plan to build one." Applications were closed as of the docs snapshot. Source: [Creator docs: Roblox Incubator](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-programs/incubator.md).
- **Built-in testing tools** [OFFICIAL]: Experiments can roll changes out to a percentage of users, and Ads Manager's "Maximize Plays" delivers plays for under $0.01 each. Sources: [Creator docs: Rewarded video ads (Experiments)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/promotion/rewarded-video-ads.md); [DevForum Ads benchmarks](https://devforum.roblox.com/t/ads-manager-updates-home-search-combined-new-benchmarks-and-sunsetting-the-classic-flow/4084863).
- [3P] Solo-developer advice: avoid ideas that "need algorithmic luck, a large starting crowd, expensive content volume, or someone else's IP." Source: [CreatorXP](https://creatorxp.gg/guides/roblox-game-ideas-to-avoid).

### Inferences
- **Typical outsourcing for a solo scripter, with budgets from the third-party ranges above** (estimates, not sourced totals):
  - icon and 3–5 thumbnails, the highest-ROI art spend because they drive play-through rate and personalization
  - a modest map or build
  - UI kit and skin
  - a few animations and VFX
  - **Per prototype: ≈ $300–$1,500 plus about $50–$150 of ads for a metrics read.**
  - **Per polished launch: ≈ $2k–$8k.**
- **"Test many" loop, achievable at 2–4 weeks per prototype for a fast scripter:**
  1. Build a vertical slice of a trend-adjacent loop with a twist.
  2. Buy 5k–20k plays.
  3. Check first-play bounce, D1 (aim above the similar-games median, which in Roblox's example is about 12%) and session length.
  4. Kill or iterate.
  5. Double down only on prototypes with strong organic RFY cohorts.
- **Timeline expectation:** the hits show 1–3 month builds are enough to catch a wave. Reaching about $3k a month sustainably, though, probably takes several attempts. This is an inference; no base-rate data was found.

### Gaps
- No reliable 2025–2026 survey of Roblox contractor rates. Animator, VFX and modeler rates weren't found.
- No data on portfolio hit rates (what share of prototypes reach 100, 500 or 1,000 CCU).
- No verified figures for AI-tool cost savings.

---

## 8. Alternative ownership models: revenue share, publishers and investors, buying and selling ("flipping") games

### Takeaway
A real M&A market has grown since Roblox eased ownership transfers (reported as a December 2024 policy change).
- **Top-end deals:** studios such as **DoBig Studios** and **Voldex** buy breakout games for millions. Seven of the 15 top-earning games had been bought from their creators by mid-2025, and the published prices are often only a few months of revenue.
- **Smaller games:** these trade on escrow marketplaces (RoMarket, RoFlag) at third-party "rule-of-thumb" multiples of roughly **1–14 months of revenue**.

Roblox group payouts are the native rail for revenue-sharing with builders and partners. Licensed IP, brand work (with a Roblox revenue share from 2027) and Roblox's Incubator are adjacent paths. Publisher deal terms aren't public.

### Cited Findings
- [PRESS] **Tubefilter, 2025-07-14:**
  - "In the last six months, midsize game development companies focused on the platform, like DoBig Studios and Voldex, have been acquiring top-performing games from independent (and often anonymous) developers for millions of dollars apiece."
  - **Blue Lock: Rivals sold to DoBig for $3M** while generating about $5M a month in in-game purchases.
  - The article states that "Grow a Garden sold to DoBig in May." **This conflicts with** Calcalist's report that the original creator still owns about half of Grow a Garden. Source: [Calcalist](https://www.calcalistech.com/ctechnews/article/dj4lxef8r).
  - Source: [Tubefilter](https://www.tubefilter.com/2025/07/14/indie-game-creators-are-making-millions-selling-their-roblox-worlds/).
- [PRESS (s.s.)] By mid-2025, **seven of the fifteen highest-earning Roblox games had been bought from their original creators**. The buying spree followed a Roblox policy change "last December" (December 2024) that made ownership transfers easier. Source: [Music Ally, 2025-07-14 (Bloomberg-sourced)](https://musically.com/2025/07/14/popular-roblox-games-are-being-acquired-for-millions-of-dollars/).
- **Brookhaven RP sold to Voldex** in February 2025 [PRESS]:
  - Funded by Raine Partners and Shamrock Capital.
  - Brookhaven had about 60B visits and over 120M monthly active players.
  - Voldex assigned at least 15 developers, and the creator stayed on through the transition.
  - The deal was reportedly bigger than Embracer's Bloxburg acquisition, which was reported at about $100M.
  - Sources: [Variety](https://variety.com/2025/gaming/news/roblox-brookhaven-game-acquired-voldex-1236295120/); [Bloomberg Law](https://news.bloomberglaw.com/private-equity/robloxs-brookhaven-rp-video-game-is-sold-by-mystery-creator); [PocketGamer.biz](https://www.pocketgamer.biz/voldex-acquires-hit-roblox-game-brookhaven/); [Music Ally](https://musically.com/2025/07/14/popular-roblox-games-are-being-acquired-for-millions-of-dollars/).
- [PRESS] Consolidation among brand-focused Roblox studios (Super League / Supersocial). Source: [Tubefilter, 2025-05-01](https://www.tubefilter.com/2025/05/01/roblox-consolidation-super-league-supersocial/).
- [PRESS, dated 2022] **Gamefam** raised a $25M Series A led by Konvoy (2022). It runs 30+ games and has partnered with Mattel, Disney, Sony and others. Source: [Game Developer](https://www.gamedeveloper.com/business/gamefam-nets-25-million-to-create-even-more-roblox-games).
- **Valuation rules of thumb** [3P (s.s.); exact split of claims between RoMarket and RoValuate unverified]:
  - Valuations "typically range from 1–12 months of revenue, depending on how stable the player base looks."
  - Genre multiples of monthly revenue:

    | Genre | Multiple of monthly revenue |
    |---|---|
    | Roleplay | about 14× |
    | Tycoon | about 12× |
    | Simulator | about 10× |
    | Fighting / other | about 8× |
    | Obby | about 6× |

  - Bloxburg reportedly sold for about 2.5× annual revenue. "Most mid-tier games (under $20K/year) settle at 1.2–1.5×." Anything above 3× is rare.
  - Sources: [RoMarket: How much do Roblox games sell for](https://romarket.app/guides/how-much-do-roblox-games-sell-for); [RoValuate: How to value a Roblox game](https://rovaluate.com/blog-how-to-value-roblox-game.html).
- **Marketplaces** [3P]:
  - **RoMarket:** free listing, **Escrow.com** payouts, "official ownership transfer," and seller fees of **5% up to $5k, 4% for $5k–$50k, and 3% above $50k**. Sources: [RoMarket sell page](https://romarket.app/sell); [RoMarket: How to sell a Roblox game](https://romarket.app/guides/how-to-sell-a-roblox-game).
  - **RoFlag:** a buyer network and acquisitions listing. Source: [RoFlag](https://roflag.com/).
  - **Gameflip:** Roblox game listings. Source: [Gameflip](https://gameflip.com/en/shop/game/roblox).
  - RoMarket publishes a ToS explainer: [RoMarket: Can you buy & sell Roblox games?](https://romarket.app/guides/can-you-buy-and-sell-roblox-games). I didn't read it.
- **Native revenue-share mechanism** [OFFICIAL]: groups support **"one-time payouts and recurring revenue splits"**, and these respect the 18+ DevEx rate. Source: [Creator docs: U.S. 18+ exchange rate – Group payouts](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/18-plus-devex-rate.md).
  - A DevForum thread on how to split revenue with a partner shows there's no standard split. Source: [DevForum](https://devforum.roblox.com/t/need-help-figuring-out-how-to-split-revenue-from-my-game-with-my-partner/1018378).
- **DoBig Studios** [3P (s.s.)]: described as a private development, publishing, analytics and acquisition company, with partnership structures "limited" in public detail. Source: [Crunchbase](https://www.crunchbase.com/organization/do-big-studios).
- **Other routes** [OFFICIAL]:
  - Licensed IP through License Manager, with rights-holder-set revenue share. Source: [IP licensing for creators](https://github.com/Roblox/creator-docs/blob/main/content/en-us/ip-licensing/creators.md).
  - The Brand Developer Directory / Partner Program, which requires a 4M+ MAU game. Source: [docs](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-programs/brand-developer-directory.md).
  - Roblox Incubator. Source: [docs](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-programs/incubator.md).
  - Roblox's cut of brand deals from January 2027. Source: [PocketGamer.biz](https://www.pocketgamer.biz/roblox-to-take-cut-of-in-game-brand-deals-from-2027-under-new-advertising-rules/).

### Inferences
- **Blue Lock: Rivals price vs revenue:** if the "$5M/month in in-game purchases" is gross player spend, developer-net was about $1.1M a month (applying the ~22.7% DevEx/bookings ratio). The $3M price is then about **2–3 months of net revenue**.
  - Buyers price in steep fad decay. Selling a breakout early transfers that risk and converts a volatile stream into cash.
  - A creator with a hot game should model decay before rejecting an offer.
- **A game netting a stable $3k a month** would, at the third-party multiples, plausibly fetch about **$18k–$54k**: 6–14 months, or 1.2–1.5× annual. That only holds if revenue is stable; buyers discount declining or exploit-ridden games.
- **Flipping as a strategy** (build, grow to a few hundred CCU, sell) is plausible for a fast scripter, but the evidence is thin and comes only from vendor marketing.
  - Risks: platform discretion over transfers, Earned Robux and DevEx; escrow and counterparty risk; IP-clean asset provenance needed for due diligence; post-sale decline disputes.
- **Revenue-share partnerships** (with builders, artists or YouTubers): use a Roblox group with recurring percentage payouts, so splits are automatic and auditable. Put vesting and exit terms in writing off-platform. This is an inference; no standard terms were found.

### Gaps
- No public DoBig or Voldex term sheets, publisher revenue splits or advance sizes.
- No verified list of deal multiples. RoMarket and RoValuate figures are vendor models, and Rolimons/RoMonitor data couldn't be accessed.
- I didn't verify Roblox's own policy text on off-platform sales of games or groups. The December 2024 transfer-policy change is press-reported only.
- No evidence on investor funds currently backing *small* Roblox teams in 2025–2026. The Gamefam raise is from 2022.

---

## 9. Success odds and risks

### Takeaway
Outcomes are extremely skewed. The median DevEx participant earns about **$1,500 a year**, while the top 1,000 average $1.4M, and even successful games keep only about 0.5% of new users at D30. The main risks:
- **trend decay and copycats**, including litigation and Roblox's non-unique filter cutting both ways
- **exploiters and burnout**
- **platform dependency**: 2026's age-check-driven DAU decline and bookings guidance cut, algorithm overhauls, discretion over Earned Robux, and new fees on brand deals
- moderation and IP-claim risk, including false claims

### Cited Findings
- **Distribution** [OFFICIAL via PRESS]: about $1,500 median versus $1.4M average for the top 1,000 and $65.7M for the top 10, among more than 42,000 DevEx participants (12 months to 2026-06-30). Source: [TweakTown](https://www.tweaktown.com/news/113585/robloxs-top-10-creators-averaged-dollars65-7-million-each-while-the-median-made-dollars1500-and-roblox-everywhere-is-the-fix/index.html).
- **Retention base rates** [3P]: median D1 10.3%, D7 1.6%, D30 0.5%, even among games with ≥1M MAU. Source: [GameAnalytics 2026](https://www.gameanalytics.com/reports/2026-roblox-report).
- **Exploiters and burnout:**
  - [PRESS, undated] Developers of competitive games say they're "burning out in their fight against hackers," and some no longer want to build such games. Source: [PCGamesN](https://www.pcgamesn.com/roblox/developers-burning-out-hackers).
  - [ANECDOTE] "with every new update comes a new exploit." Source: [DevForum: Are exploiters still a problem in 2025?](https://devforum.roblox.com/t/are-exploiters-still-a-problem-in-2025/3819994).
- **Copycats:**
  - [PRESS] Clones flood hits within weeks. Sources: [Windows Central](https://www.windowscentral.com/gaming/how-roblox-theft-is-becoming-a-big-problem); [Plagiarism Today](https://www.plagiarismtoday.com/2026/09/17/the-attack-of-the-roblox-clones/).
  - [PRESS] Even Steal a Brainrot's owners resorted to lawsuits. Source: [Bloomberg](https://www.bloomberg.com/news/articles/2026-03-24/roblox-s-hit-game-steal-a-brainrot-battles-its-many-imitators).
  - [3P] A solo developer has little protection against a funded team fast-following and improving the mechanic. Source: [ProGameGuides (s.s.)](https://progameguides.com/roblox/5-things-roblox-developers-need-to-do/).
- **False IP claims** [ANECDOTE]: Rights Manager has reportedly been abused to take down original games while the copiers stayed up. Source: [DevForum: Introducing Rights Manager](https://devforum.roblox.com/t/introducing-rights-manager/2880717).
- **Platform dependency** [OFFICIAL]:
  - DAU went from about 152M to 123M between Q3 2025 and Q2 2026.
  - FY2026 bookings growth guidance was cut to 8–12%.
  - Q2 2026 bookings per hour came in below forecast, especially among under-13s.
  - Sources: [Respawn](https://respawn.outlookindia.com/gaming/gaming-news/roblox-bets-on-safety-and-adults-over-user-volume); [Seeking Alpha](https://seekingalpha.com/news/4583513-roblox-forecasts-2026-revenue-growth-of-20-percentminus-25-percent-as-safety-changes-drive); [Investing.com Q2 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-roblox-q2-2026-beats-eps-but-shares-sink-on-bookings-93CH-4826338).
- **DevEx discretion** [OFFICIAL]:
  - Roblox "maintains the exclusive right to decide if any Robux qualifies as Earned Robux."
  - Moderated violative content doesn't earn.
  - "Previous DevEx request approvals are not guarantees."
  - Source: [Creator docs: Developer Exchange](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md).
- **Policy and moderation risk** [OFFICIAL]:
  - A missing or inaccurate maturity questionnaire restricts playability. Source: [Content maturity](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/promotion/content-maturity.md).
  - Broken paid-access games can be quarantined, with escrowed earnings refunded. Source: [Paid access](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/paid-access-local-currency.md).
  - Violating ad eligibility rules can bring suspension or loss of ad payouts. Source: [Rewarded video ads](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/promotion/rewarded-video-ads.md).
- **Algorithm changes:**
  - [OFFICIAL] The June 2026 overhaul removed QPTR and extended the window to 28 days. Source: [DevForum](https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575).
  - [3P] The late-2025 shift from click-based to stay-and-return-based recommendations was summarized by [RoWatcher (s.s.)](https://rowatcher.com/news/one-year-on-the-charts-what-really-happens-after-a-roblox-game-goes-viral).
- **Fee and terms changes** [OFFICIAL via PRESS]: Roblox takes a share of brand deals from January 2027. Source: [Kidscreen](https://kidscreen.com/2026/03/23/roblox-plans-to-start-taking-a-cut-on-brand-deals/).
- **Upside levers on the platform side** [OFFICIAL via PRESS]:
  - The DevEx rate rose to $0.0038 on 2025-09-05. Source: [DevEx docs](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md).
  - The 18+ rate of $0.0054 started 2026-06-08. Source: [18+ docs](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/18-plus-devex-rate.md).
  - Roblox Everywhere standalone apps, Chrome launch and Moments were announced at RDC 2026. Source: [PocketGamer.biz](https://www.pocketgamer.biz/roblox-unveils-new-play-creation-and-monetisation-tools-at-rdc-2026/).

### Inferences
- **Survivorship bias is severe.** Every famous 2025 case was a top-0.01% outcome. Plan around median-to-good outcomes: several prototypes, most failing benchmark gates, and one or two reaching a few hundred CCU.
- **Main risk controls for a fast scripter:**
  - server-authoritative design, rate-limited remotes and anti-exploit work from day one
  - an IP-clean asset pipeline: own or commissioned assets with written transfer of rights, which also preserves resale value
  - a content and event calendar to fight decay
  - avoid near-clones
  - keep a parallel income stream, such as commissions or contract scripting, until a game holds roughly 300+ CCU for 4+ weeks
- **Platform-concentration risk:** 100% of revenue depends on Roblox's algorithm, policy and DevEx terms.
  - Partial hedges: building for 13+ and 18+ audiences, which spend more, are less exposed to under-13 monetization weakness and may qualify for the 18+ DevEx rate; plus an early exit through sale.
- **Burnout risk comes from live ops**: weekly updates, exploit firefighting and community moderation. Budget for community moderators or a partner once a game earns money.

### Gaps
- **No base-rate data** on the share of new games that ever reach 100, 500 or 1,000 CCU, or on the average number of attempts before a creator's first $1k/month game.
- No systematic postmortem dataset for small games. The DevForum, Reddit and YouTube postmortems couldn't be fetched.
- No data on how often DevEx requests are rejected or Earned Robux is clawed back.
