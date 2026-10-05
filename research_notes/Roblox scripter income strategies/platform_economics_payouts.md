# Roblox Platform Economics & Creator Payouts (state as of 5 October 2026)

*How the sources were gathered (important for weighing them):* The research environment's egress proxy blocked create.roblox.com, devforum.roblox.com, en.help.roblox.com, about/corp/ir.roblox.com, sec.gov and almost all press sites. **Official Creator Hub documentation was therefore read directly from Roblox's own open-source docs repository, `github.com/Roblox/creator-docs`, which is the source of create.roblox.com/docs (repo HEAD commit dated 2026-10-02).** Each docs citation below gives that file's last-change date from the git history. Financial-filing and press figures come from **search-engine extracts** of the cited pages; I could not open those pages directly. Treat them as "reported" and check the exact wording before publishing. The web-search budget ran out partway through, so lawsuits, Robux retail prices and some statistics are listed as gaps.

---

## 1. Developer Exchange (DevEx): rate(s), rate history, threshold, eligibility, cadence, processor, methods, tax forms

### Takeaway
As of October 2026 there are **three DevEx rates**:
- **Standard:** US$0.0038 per Earned Robux, for Robux earned from 5 Sep 2025 10am PT onward. This was an 8.5% rise from $0.0035.
- **Legacy:** $0.0035, for balances earned before that cutoff. These must be cashed out first.
- **US 18+ rate:** $0.0054, live since 8 Jun 2026. It applies only to dev products, passes, subscriptions and private servers bought by **age-verified 18+ US players** in **R15-compliant games**.

Cash-out rules: minimum 30,000 Earned Robux; age 13+; verified email; a W-9 or W-8 on file; at most **one completed cash-out per calendar month**; paid through **Tipalti**.

From **1 Nov 2026**, DevEx payments are reclassified as **royalties**. For non-US creators this means 0–30% US withholding on the portion of earnings that comes from US players.

### Cited Findings
**Rates and rate history**
- "The standard exchange rate for the DevEx program is `0.0038` per 1 Earned Robux, which comes out to $114 USD for 30,000 Earned Robux." — [Roblox Creator Docs: Developer Exchange (upd. 2026-07-07)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md) (canonical page: create.roblox.com/docs/production/monetization/developer-exchange)
- Legacy rate: "Before September 5, 2025 at 10am PT, the standard exchange rate was `0.0035`… those balances will cash out at the `0.0035` exchange rate." — [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md)
- Cash-out order: "You can only cash out your Earned Robux at the old exchange rate before you can cash out any Earned Robux at the current exchange rate. This includes one-time payouts from groups." Spending Robux on the platform does **not** clear the old-rate balance first. — [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md)
- Roblox's FY2025 10-K describes the change as "an 8.5% increase in fiat currency exchange rates for earned Robux effective September 5, 2025" (reported via search extract). — [Roblox 10-K FY2025 (SEC)](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm)
- **US 18+ rate.** "Roblox offers a higher exchange rate of `0.0054` for certain Earned Robux in eligible games from purchases of developer products, passes, subscriptions, and private servers from U.S. players who have verified their age as at least 18 years old through facial age estimation or government ID." Effective date: "June 8, 2026." — [Creator Docs: U.S. 18+ exchange rate (upd. 2026-08-25)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/18-plus-devex-rate.md) and [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md)
  - The docs page was added on 2026-05-29 ([file history](https://github.com/Roblox/creator-docs/commits/main/content/en-us/production/monetization/18-plus-devex-rate.md)).
  - Press and secondary sites say it was announced in **April 2026** as "Earn 42% More on Spend from 18+ US Players". — [DevForum announcement (title via search)](https://devforum.roblox.com/t/introducing-the-us-18-devex-rate-earn-42-more-on-spend-from-18-us-players/4607091); [NetInfluencer](https://www.netinfluencer.com/roblox-to-raise-developer-exchange-rate-for-games-aimed-at-18-plus-players-as-adult-cohort-surges/)
  - A secondary summary (unverified) says Roblox justified it by noting that its US 18–34 user base grew 50% YoY and that this group monetizes about 50% higher than under-18s. — [devex.gg (via search extract)](https://devex.gg/18-plus-devex-rate)
- **Which games qualify for the 18+ rate:**
  - Player characters must spend "**100% of active playtime**" as one of:
    - R15 platform avatars (standard or advanced rig);
    - custom human-form characters with 15+ parts **or** 15+ joints, ≥2 torso parts and full bipedal articulation;
    - custom non-human characters.
  - Animation packs must be R15. Any R6 option (spawning as or swapping to R6) makes the game ineligible.
  - Games with no visible player character (e.g., top-down strategy) count as "non-human form". NPCs are not evaluated.
  - Roblox runs ongoing background compliance checks; a failed check removes eligibility until fixed.
  - Group games: one-time payouts and recurring splits respect the 18+ rate. "Both your one-time payouts and DevEx requests prioritize the U.S. 18+ DevEx rate."
  - Source: [Creator Docs: U.S. 18+ rate](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/18-plus-devex-rate.md)
- **Older history (pre-2025, community-documented only — may be inaccurate):** $0.0025 at DevEx launch (1 Oct 2013) → $0.0035 (1 Mar 2017) → $0.0038 (5 Sep 2025) → $0.0054 US 18+ tier (8 Jun 2026). — [supertj/devex-rates (GitHub, third-party)](https://github.com/supertj/devex-rates)

**Threshold and eligibility**
- Requirements:
  - "Be at least 13 years old"
  - "Have a minimum of 30,000 Earned Robux in your account"
  - "Have a Roblox-verified email address"
  - "Have a valid DevEx portal account"
  - "Have either an IRS form W-9 (for U.S. taxpayers) or W-8 (for non-U.S. taxpayers) on file"
  - Full compliance with the Terms of Use and Community Standards; non-compliance "may result in suspension from the DevEx program."
  - Source: [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md)
- **Premium:** not in the official requirement list. A secondary source says the Premium requirement was dropped in early 2022 (a pre-2025 claim, unverified here). — [ExitLag blog (via search extract)](https://www.exitlag.com/blog/devex-roblox/)
- **What counts as Earned Robux:**
  - In-game sales: dev products, passes, subscriptions.
  - Fees from in-game purchases of Marketplace items.
  - Fees from Robux Transfers through the Transfer API.
  - Paid private servers; paid access bought in Robux; Roblox Plus incentives; "publishing ads within a game".
  - Creator Store paid models and plugins; Marketplace avatar items.
  - Creator Rewards.
  - Source: [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md)
- **What does NOT count:**
  - Directly purchased Robux, and monthly subscription Robux grants.
  - Trading or resale of items.
  - Robux received from transfers; gift-card redemptions.
  - "Passes sold for template games with no legitimate user visits".
  - Moderated, violating content.
  - "Roblox maintains the exclusive right to decide if any Robux qualifies." — [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md)
- **Name and ID:** you must use your legal name only. If a request is rejected for a name mismatch, the parties involved "will likely need to follow the ID verification process." Past approvals do not guarantee future ones. — [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md)

**Process, cadence and timing**
- Submit via Creator Hub → Finances → **Cash Out**. The Robux are removed when you submit and refunded if the request is rejected. Requests cannot be cancelled. — [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md)
- First-time cash-out: Roblox emails an invite to the Tipalti DevEx Portal. Payment method and tax form must be completed "within one week", otherwise the request is auto-declined and refunded. — [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md)
- Processing estimates: about **10 business days** for first-time participants and about **5 business days** for returning ones. There is no processing on weekends or holidays, and bank transit time is extra. — [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md)
- **Frequency:** "You can have a completed DevEx request once per calendar month." — [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md)
- The Earned Robux balance on the dashboard is an estimate with "up to a 24 hour delay." — [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md)

**Processor, payment methods, fees, countries**
- Tipalti offers PayPal, ACH, eCheck, wire and check; what is available "depend[s] on where you live" (see Tipalti's country coverage list). — [Creator Docs: DevEx Portal (upd. 2026-07-15)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/devex-portal.md)
- Transit times: ACH 3–5, eCheck 3–5, PayPal 2–3, wire 1–5, check 7–14 business days. — [Creator Docs: DevEx Portal](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/devex-portal.md)
- Fees: "Tipalti charges a transaction fee that is deducted from your DevEx payout," which varies by payment method. Converting to local currency adds an FX fee of **1.9% to 3%**. — [Creator Docs: DevEx Portal](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/devex-portal.md)
- Bank account names must match the DevEx Portal name. DevEx is "available for individuals and companies"; the payment method and tax form must match whichever entity is cashing out. — [Creator Docs: DevEx Portal](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/devex-portal.md)

**Tax forms and withholding (major change on 1 Nov 2026)**
- "Beginning **November 1, 2026**, DevEx payments will be classified as royalties under the updated Terms of Use." — [Creator Docs: DevEx tax information (added and updated 2026-07-15)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/tax-information.md)
- Key dates:
  - 15 Jul 2026: Creator Hub **Taxes** page opens.
  - **15 Oct 2026**: "Recommended deadline to request a DevEx payout before the Terms of Use update."
  - **31 Oct 2026**: last day of the current terms. Tax info on file by then sets the withholding rate.
  - **1 Nov 2026**: royalties regime starts. Withholding is set by the *payout* date, not the submission date.
  - Source: [Creator Docs: tax information](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/tax-information.md)
- US creators: no withholding with a valid W-9. **24% backup withholding** applies if the TIN is invalid or missing, or after an IRS B-Notice. — [Creator Docs: tax information](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/tax-information.md)
- Non-US creators (W-8BEN for individuals, W-8BEN-E for entities): **0%–30% US withholding** on "DevEx payments related to sales to U.S. players, depending on your country of residence and whether you successfully claim a tax treaty." Without valid tax info by 31 Oct 2026, **24% backup withholding may apply to the full payout**. — [Creator Docs: tax information](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/tax-information.md)
- Year-end forms:
  - US creators: 1099-NEC for payments before 1 Nov 2026, 1099-MISC (royalties, Box 2) after.
  - Non-US creators: Form 1042-S.
  - Under the pre-change rules, US persons got a 1099-NEC if prior-year cash earnings exceeded **$2,000**, and "Non-U.S. persons generally will **not** receive an annual tax form."
  - Source: [Creator Docs: tax information](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/tax-information.md); [Creator Docs: DevEx Portal](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/devex-portal.md)
- **Coming payout channel (announced at RDC 2026):** "Roblox Wallet" will give eligible **US** independent creators **aged 18+** their earnings in real currency with automatic payments **every business day**, "launching later in 2026" (via search extracts). — [Roblox IR: RDC 2026 release](https://ir.roblox.com/news/news-details/2026/Roblox-Unveils-New-Ways-to-Play-Build-and-Grow-at-the-Roblox-Developers-Conference-RDC/default.aspx); [PocketGamer.biz](https://www.pocketgamer.biz/roblox-unveils-new-play-creation-and-monetisation-tools-at-rdc-2026/)

### Inferences
- A creator starting now has no legacy balance, so **$0.0038 is the floor rate**. Any spend from age-verified US adults on passes, dev products, subscriptions or private servers in an R15-compliant game earns 42% more (0.0054/0.0038 = 1.42).
- Making the game R15-only is a cheap design choice that should be made before launch. For a Luau scripter, custom rigs need ≥15 parts or joints.
- Because only one cash-out per calendar month is allowed, plus roughly 5–10 business days of processing and 1–14 days of transit, **cash lags earnings by about 2–6 weeks** even for sales with a ~5-day hold. For programs with 30–60-day holds (Section 2) the lag is longer.
- Non-US creators who want to be paid under the pre-royalty regime had to request by about 15 Oct 2026 (10 days after this note). After that, they need a valid W-8 with a TIN and a treaty claim filed in Creator Hub by **31 Oct 2026** to avoid 24% backup withholding on the whole payout.
- Payouts lose a small extra slice to Tipalti fees (a fixed per-payout fee by method) and to the 1.9–3% FX fee if paid in local currency. Receiving USD and converting elsewhere may be cheaper, depending on the country.

### Gaps
- The DevEx Terms of Use (help center, blocked) could not be read. This covers the full eligibility list, sanctioned or excluded countries, any per-request maximums, and the exact contractor language.
- The date the minimum was lowered to 30,000 Robux (believed to be pre-2025) could not be confirmed.
- The relative cash-out order of legacy vs US 18+ Robux is not stated in one place. The docs say legacy cashes out first and that 18+ is "prioritized"; the most likely order is legacy → 18+ → standard (inference).
- Tipalti's per-method fee amounts and Roblox Wallet details (fees, launch date, whether it replaces the monthly limit) were not available.
- The RDC 2025 tie-in to the 5 Sep 2025 rate change is plausible from the timing but was not verified this session.

---

## 2. Platform fees by product, and hold ("pending"/escrow) periods

### Takeaway
- In-game items (passes, developer products, Robux subscriptions, private servers) pay the creator **70% of the Robux price**.
- Avatar items pay the creator **30%**. In-game sales add a **40% affiliate fee to the game owner**. Marketplace-only sales can rise to 70% under progressive pricing.
- **Creator Store** paid models and plugins pay **100% of net USD** (only taxes and payment processing are deducted).
- Local-currency products have their own splits: paid access pays 50/60/70% by price tier; local-currency subscriptions pay 70% in month 1 and 100% from month 2, converted to Robux at $0.01 per Robux.
- Holds run from about **5 days** (passes and dev products) to **30 days** (avatar items, local-currency subscriptions, Creator Store) and **60 days** (Creator Rewards, Roblox Plus incentives, local-currency paid access).

### Cited Findings
- **Passes and developer products: 70%.** Roblox's own worked example: a non-subscriber buys a 100-Robux item → creator earns 70 → "Effective revenue share 70%". If a Roblox Plus subscriber pays 90 or 80 Robux, Roblox covers the 10–20% discount, so the creator still gets 70. That is an effective 78% or 88% of what the user actually paid. — [Creator Docs: Roblox Plus (upd. 2026-07-14)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/roblox-plus.md)
- Pass prices can be set from 1 Robux to 1 billion Robux. — [Creator Docs: Passes (upd. 2026-09-23)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/passes.md)
- **Private servers: 70%,** charged as a monthly Robux fee. Roblox's example: "70% revenue share on a 100 Robux server price." — [Creator Docs: Roblox Plus](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/roblox-plus.md); [Creator Docs: Monetization overview (upd. 2026-09-30)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/index.md)
- **Hold for passes and dev products:** "approximately 5 days" (stated in the subscriptions doc, which says Robux subscriptions follow "the same hold period as passes and developer products"). — [Creator Docs: Subscriptions (upd. 2026-07-07)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/subscriptions.md)
- **Subscriptions:** — [Creator Docs: Subscriptions](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/subscriptions.md)
  - *Priced in Robux*:
    - Minimum 49 Robux; available to all creators, on all platforms, in all countries.
    - Regional pricing on by default.
    - "70% of the subscription value every month", with a ~5-day hold.
  - *Priced in local currency*:
    - Prices fixed at $2.99 / $4.99 / $7.99 / $9.99 / $14.99.
    - Requires an account verified by ID or phone; available on Web, App Store and Google Play only.
    - **Not available** in Argentina, China, Colombia, India, Indonesia, Japan, Russia, Taiwan, Türkiye, UAE, Ukraine or Vietnam.
    - "You earn Robux at a rate of US $0.01 to 1 Robux according to the base platform price you selected, after platform fees". The creator gets **70% in month 1 and 100% from month 2** (e.g., a $5 subscription pays 350 Robux, then 500 Robux a month).
    - **30-day hold**; a refund inside the hold cancels the payout. Subscriptions cannot be cross-sold and do not earn affiliate fees.
- **Paid access in Robux:** price 25–1,000 Robux; "held in escrow for up to 7 days"; no refunds. — [Creator Docs: Paid access in Robux (upd. 2026-07-07)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/paid-access-robux.md)
- **Paid access in local currency:** — [Creator Docs: Paid access local currency (upd. 2026-07-21)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/paid-access-local-currency.md)
  - Revenue share depends on price tier: **$9.99 → 50%, $29.99 → 60%, $49.99 → 70%**, minus taxes and VAT.
  - Escrow is a "minimum of 60 days", with payouts "once a month" via Tipalti. Tipalti onboarding takes 5–8 business days.
  - Not purchasable by users in Argentina, China, Colombia, India, Indonesia, Russia, Taiwan, Turkey, UAE, Ukraine or Vietnam.
  - If many users report the game as broken, it may be quarantined and escrowed earnings refunded.
- **Avatar items (UGC):** — [Creator Docs: Marketplace fees & commissions (upd. 2026-09-03)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/marketplace/marketplace-fees-and-commissions.md)
  - Marketplace sale: the creator gets **30%**.
  - In-game sale: creator 30% / **game owner (affiliate) 40%** / Roblox 30%.
  - **Progressive revenue share** applies to Marketplace purchases only, based on price ÷ price floor: 1× → 30%, 1.3× → 37%, 1.5× → 41%, 2× → 50%, 2.5× → 57%, 3× → 62%, 3.5× → 65%, 4× → 67%, 5× → 69%, ≥6× → 70%. In-game purchases get the base 30%.
  - **30-day escrow**.
  - Resale of community Limiteds: reseller 50% / original creator 10% / seller-affiliate 10% / Roblox 30%. Only Roblox Plus or Premium members can resell.
- **Creator Store (models and plugins):**
  - Sold in **USD**. The creator earns "100% of net proceeds on transactions, bypassing platform fees and DevEx rates"; only taxes and payment-processing fees are deducted.
  - Price limits: plugins $4.99–$249.99; models $2.99–$49.99.
  - **30-day escrow**, then paid to a Stripe account.
  - Seller requirements: age check or government ID; age 18+ (or 13–17 with parental consent); 2FA; residence in a Stripe-supported country; **not available in Brazil, China, India or Russia**; individual accounts only (no groups).
  - Source: [Creator Docs: Creator Store (upd. 2026-10-02)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/creator-store.md); [Creator Docs: Monetization overview](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/index.md)
- **Robux transfers:** when a Plus subscriber sends Robux inside your game, "your game earns **10%** of the Robux sent and the recipient receives the remaining **90%**." Transfers must be 10–500 Robux. The game's cut is DevEx-eligible and Roblox takes no fee; the recipient's Robux are not DevEx-eligible. — [Creator Docs: Robux transfers (added 2026-05-04)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/robux-transfers.md); [Creator Docs: Roblox Plus](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/roblox-plus.md)
- **Other holds:**
  - Creator Rewards: paid "in 'Earned Robux' with a 60-day holding period". — [Creator Docs: Creator Rewards (upd. 2026-09-30)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-rewards.md)
  - Roblox Plus sign-up incentives: "subject to a 60-day holding period". — [Creator Docs: Roblox Plus](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/roblox-plus.md)
  - Immersive ads: paid "on the 25th of the following month". — [Creator Docs: Immersive ads (upd. 2026-07-30)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/immersive-ads.md)

### Inferences
- **Real "platform cut" against player dollars.** At the standard rate the creator's cash per Robux a player spends is 0.7 × $0.0038 = **$0.00266**. At the US 18+ rate it is 0.7 × $0.0054 = **$0.00378**.
  - If players pay about $0.01 per Robux (the rate Roblox uses for local-currency subscriptions), the creator keeps **~26.6%** of player dollars (standard) or **~37.8%** (US 18+).
  - At an illustrative retail price of $0.0125 per Robux, the creator keeps **~21.3%** or **~30.2%**.
  - The rest goes to app stores and payment processors, Roblox's 30% Robux cut, and the gap between the DevEx rate and the Robux retail price.
- In cash terms, local-currency subscriptions convert at $0.01 per Robux and then DevEx at $0.0038. So a $1 subscription price yields $0.266 in month 1 and **$0.38** from month 2 onward. This is one of the better recurring yields on the platform.
- The Creator Store is the only channel with near-100% pass-through. It is a B2B market of other developers and has price ceilings ($249.99 plugins, $49.99 models). For a strong Luau scripter, paid plugins and scripted models are a real channel that is not tied to DevEx.
- An experience that sells avatar items in-game earns a 40% affiliate fee on catalog items it did not make. This fee counts as Earned Robux.

### Gaps
- The revenue share for **paid access in Robux** is not stated in the docs read; 70% is likely but unverified.
- A primary statement of the passes/dev-products hold outside the subscriptions doc (e.g., the help center's "pending Robux" article) was not accessible.
- Stripe payment-processing fee rates for the Creator Store were not found.

---

## 3. Creator payout programs: Creator Rewards (which replaced Premium Payouts), Roblox Plus incentives, ads, commerce, paid access, pricing tools, Robux price changes

### Takeaway
- **Engagement-Based (Premium) Payouts and the Creator Affiliate program ended on 24 Jul 2025.** They were replaced by **Creator Rewards**:
  - **5 Robux per Active Spender per day**. The game must be one of that user's first three experiences of the day, played for 10+ minutes; an Active Spender has spent ≥$9.99 in the last 60 days.
  - **Audience Expansion: 35% revenue share on the first $100** a new or reactivated user spends anywhere on Roblox in their first 60 days. This requires an ID-verified creator and a game with 100+ average DAU.
  - The formula has not changed since launch (git history through 2026-09-30).
- **Roblox Plus** (available to users from 30 Apr 2026, per the docs) adds Roblox-subsidized discounts, a bounty of up to 750 Robux per subscriber you sign up, private-server compensation, and a 10% cut of in-game Robux transfers.
- Other channels: rewarded video and immersive ads (13+, ID-verified, 2FA, 2,000+ monthly visitors); Shopify commerce (US buyers only); and pricing tools (price optimization, regional pricing, and "Managed pricing" since June 2026).

### Cited Findings
**Creator Rewards**
- The **Daily Engagement Reward** "pays Creators 5 Robux for each user who spends at least 10 minutes in their experience over the course of the day." The experience must be among "the first three experiences that the user visits that day". Users must be Active Spenders, "meaning they must have spent at least $9.99 in the past 60 days". Active Spenders must also have been active on Roblox for 60+ days and not be new or reactivated users. — [Creator Docs: Creator Rewards](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-rewards.md)
- "Qualifying Purchases" are purchases of Robux, Roblox Premium, or UGC subscriptions. — [Creator Docs: Creator Rewards](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-rewards.md)
- **Audience Expansion:** "the Creator earns a 35% revenue share on their first $100 of Qualifying Purchases anywhere on the platform during their first 60 days" for **New Users** or **Reactivated Users** (lapsed for 60+ consecutive days). — [Creator Docs: Creator Rewards](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-rewards.md)
  - Attribution comes from a Share Link, a direct link, or a search for the exact experience name, with 10+ minutes played that day. In every case "the experience maintains an average of 100+ DAU for 60 days after the joining or rejoining date."
  - Users arriving through Roblox promotional campaigns and duplicate or alt accounts are excluded.
- **Eligibility:** all creators earn Daily Engagement automatically from 24 Jul 2025. Audience Expansion requires "an ID-verified account in good standing and a valid DevEx account". For group-owned games, a member with group-revenue permission must meet this. Paid-access games are eligible. — [Creator Docs: Creator Rewards](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-rewards.md)
- **Anti-abuse:** bots, automation, teleport manipulation, alt-account farming, impersonation and high chargeback rates can lead to forfeited rewards, removal from the program or account termination. — [Creator Docs: Creator Rewards](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-rewards.md)
- **What it replaced:** "Engagement Based Payouts and Creator Affiliate programs have been discontinued and replaced with Creator Rewards." Engagement-Based Payouts were deprecated "Effective July 24, 2025". — [Creator Docs: Creator Rewards](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-rewards.md); [Creator Docs: Engagement-based payouts](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/engagement-based-payouts.md)
  - Secondary sources date the announcement to **24 Jun 2025** and the go-live to 24–25 Jul 2025. — [DevForum: Introducing Creator Rewards (title via search)](https://devforum.roblox.com/t/introducing-creator-rewards-earn-more-by-growing-the-community/3777628); [DevForum: Creator Rewards is Live (title via search)](https://devforum.roblox.com/t/creator-rewards-is-live/3838257); [Roblox Wiki (fandom, via search extract)](https://roblox.fandom.com/wiki/Creator_Rewards)
- **No formula changes since launch.** The doc's git history shows the 5 Robux / 35% / $100 / 60-day / 100-DAU terms unchanged from 2025-07-24 to 2026-09-30. The only edits are wording, group eligibility (added 2025-09-03) and dashboard benchmarks (2026-04-01). — [creator-rewards.md commit history](https://github.com/Roblox/creator-docs/commits/main/content/en-us/creator-rewards.md)
- Roblox's FY2025 10-K lists "the Creator Rewards Program launched in July 2025" as a driver of higher developer exchange fees (via search extract). — [Roblox 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm)

**Roblox Plus (new consumer subscription; creator incentives)**
- "Roblox Plus will become available to users starting on April 30, 2026" (from the first version of the doc, added 2026-04-10). — [roblox-plus.md history](https://github.com/Roblox/creator-docs/commits/main/content/en-us/production/monetization/roblox-plus.md)
- Creator earnings from Plus: — [Creator Docs: Roblox Plus](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/roblox-plus.md)
  - **Discounts:** subscribers get 10% off, rising to 20% from month 3. The discount is "covered by Roblox so that your earnings per purchase are not reduced". It applies to dev products, passes, developer subscriptions, paid-access games and avatar items.
  - **Sign-up bounty:** "250 Robux per month for their first three consecutive months, with up to 750 Robux for every newly acquired subscriber". This only counts sign-ups made through your game via `PromptRobloxSubscriptionPurchase`, and only once the subscription is paid (free trials excluded).
  - **Private servers:** "up to 100 Robux per subscriber" when the subscriber spends 60+ cumulative minutes over 30 days in a paid private server they created in your game, ranked among their top five such servers.
  - **Transfers:** 10% of in-game Robux transfers.
  - All of these earnings have a 60-day hold.
- Hard-coded prices will show Plus users the wrong price. Use `GetProductInfoAsync` or `GetDeveloperProductsAsync` to display the discounted price. — [Creator Docs: Roblox Plus](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/roblox-plus.md)

**Ads**
- **Rewarded video ads** (doc added 2025-07-15): — [Creator Docs: Rewarded video ads (upd. 2026-07-30)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/promotion/rewarded-video-ads.md)
  - Requirements: publisher 13+, account in good standing, 2FA and ID verification. The game must be public, unrestricted and have no free-form user creation, with an approved maturity questionnaire and "at least 2 thousand unique visitors per month".
  - Earnings = EPM (earnings per 1,000 impressions) × impressions.
  - Rewards must be **developer products** (not Robux); Roblox recommends rewards worth 3–10 Robux. You can exclude users who are likely to spend from seeing ads.
- **Immersive ads** (image, video, portal): — [Creator Docs: Immersive ads](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/immersive-ads.md)
  - Publishers earn per impression, per 15-second view or per teleport. Payouts arrive on the 25th of the following month.
  - Requirements: game public; owner 13+; ID-verified with 2FA (persistent); approved maturity questionnaire; **2,000 unique visitors per month**.
  - Roblox is not obliged to serve ads.

**Commerce (physical goods via Shopify)**
- Creator requirements: **18+**, ID- and email-verified, and the Shopify store's account holder (or authorized by them). — [Creator Docs: Commerce products (doc added 2025-05-15; upd. 2026-07-07)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/commerce-products.md)
- "At this time, only US-based users can purchase commerce products." Buyers must be 13+, or **18+ in Texas**. — [Creator Docs: Commerce products](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/commerce-products.md)
- Bundling a digital item with a physical product requires either:
  - a game averaging >100,000 DAU and >1,000,000 Robux monthly earnings over 90 days, or
  - a written agreement for at least **$50,000 a year in ad spend**.
  - Source: [Creator Docs: Commerce products](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/commerce-products.md)

**Pricing tools**
- **Price optimization** (doc since 2024-10-07; upd. 2026-07-07): a price test of about 3 weeks shows test prices to 98% of users and original prices to 2%, then reports the "approximate revenue impact". — [Creator Docs: Price optimization](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/price-optimization.md)
- **Regional pricing** (doc since 2025-04-21): Roblox sets per-region prices based on purchasing power, FX and local spending. These "will never be discounted by more than 70% of your default price, and they will never exceed the default price". — [Creator Docs: Regional pricing](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/regional-pricing.md)
- **Managed pricing** (doc added 2026-06-15) combines regional pricing and price optimization in one opt-in system. — [Creator Docs: Managed pricing](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/managed-pricing.md)
- Regional pricing does not change the avatar-item revenue-share percentage. — [Creator Docs: Marketplace fees](https://github.com/Roblox/creator-docs/blob/main/content/en-us/marketplace/marketplace-fees-and-commissions.md)

**Robux purchase prices**
- The 10-K and Q1 2026 materials cite "**differential Robux pricing launched in November 2024**" as raising developer exchange fees by increasing the supply of Robux available to creators (via search extract). — [Roblox 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm); [Q1 2026 shareholder letter (SEC 8-K)](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026028882/ex991-q12026earningsshar.htm)
- Roblox Plus discounts of 10–20% are subsidized by Roblox, so creators lose nothing on them (see above).

### Inferences
- **Creator Rewards is small per user and pays off at scale.**
  - Each qualifying Active-Spender day = 5 Robux ≈ **$0.019**.
  - 1,000 qualifying Active Spenders a day ≈ 150,000 Robux per 30 days ≈ **$570 a month** (standard rate).
  - Reaching $3,000 a month from Daily Engagement alone would need ~157,895 qualifying user-days a month, or **~5,263 qualifying Active Spenders every day**. For most games it is a supplement, not the base.
- Audience Expansion pays out at most 35% × $100 of a recruited user's spending. It rewards off-platform marketing (Share Links, social channels), but only once the game holds 100+ average DAU for 60 days.
- A Plus sign-up is worth at most 750 Robux ≈ **$2.85**, and the private-server payment at most 100 Robux ≈ $0.38 per subscriber per month. These are small next to direct in-game sales.
- Commerce is US-only and its bundling bar is very high, so it is not realistic for an indie target of $3,000 a month.
- Ads need 2,000+ monthly unique visitors plus ID verification and 2FA. EPMs are not published, so ad income cannot be estimated from public sources.

### Gaps
- Roblox has published nothing on what share of a typical game's earnings Creator Rewards makes up, or on how Audience-Expansion dollars convert to Robux.
- No rewarded-video EPM or immersive-ad CPM benchmarks were found.
- The revenue split for commerce (Shopify) sales was not found.
- 2025–2026 Robux retail price points per platform were not obtainable after the search budget ran out. This covers the size of the web/gift-card vs mobile "differential pricing" and any bonus-Robux changes.
- Roblox Plus's consumer price was not found.

---

## 4. Worked math for netting US$3,000/month, plus group revenue splitting

### Takeaway
At the standard $0.0038 rate, **$3,000 = 789,474 Earned Robux a month** (≈26,300 a day). If all of it came from items paying 70%, that means **≈1.13M Robux of player spend a month**, which is roughly **US$11k–14k of player spending**.

Earned Robux needed to net $3,000 under different scenarios:

| Scenario | Earned Robux / month |
|---|---|
| All spend qualifies for the US 18+ rate | 555,556 |
| 25% of spend qualifies for the 18+ rate | 714,286 |
| Non-US creator, 30% withholding on a 50% US-source share | 928,793 (≈957,518 with a 3% FX fee) |
| Backup withholding at 24% on the full payout | ~1.04M |

Group games can split revenue to collaborators by percentage, both recurring and one-time. Those Robux are DevEx-eligible if they are bona fide earnings.

### Cited Findings
- Rates: standard 0.0038, legacy 0.0035, US 18+ 0.0054; DevEx minimum 30,000 Robux ($114 at the standard rate). — [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md); [Creator Docs: U.S. 18+ rate](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/18-plus-devex-rate.md)
- Revenue shares used below:
  - 70% for passes, dev products and private servers — [Creator Docs: Roblox Plus](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/roblox-plus.md)
  - 30% / 40% for avatar items and the in-game affiliate fee — [Creator Docs: Marketplace fees](https://github.com/Roblox/creator-docs/blob/main/content/en-us/marketplace/marketplace-fees-and-commissions.md)
  - Local-currency subscriptions at US$0.01 = 1 Robux — [Creator Docs: Subscriptions](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/subscriptions.md)
- Withholding and fees used below:
  - Non-US withholding 0–30% on the US-source share; 24% backup withholding — [Creator Docs: tax information](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/tax-information.md)
  - FX fee 1.9–3% — [Creator Docs: DevEx Portal](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/devex-portal.md)
- **Group payouts:** — [Creator Docs: Groups (upd. 2026-09-30)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/projects/groups.md)
  - Owners or members with Group Revenue permission can send **one-time payouts** in batches (including by CSV of userId/payoutInRobux), with 2FA and eligibility checks.
  - They can also set **recurring percentage payouts** per game and group-wide. Roblox's example: a game split 40/30/10, with the 20% remainder passing through the group split and then into the group balance.
  - "Some groups may not have this page unlocked initially… such as the age of the group or insufficient funds."
  - "Payouts cannot be shared across group members for games that charge for paid access in local currency."
  - Private-server subscription splits stay locked at the percentages in force at purchase time.
- "Group payouts count as Earned Robux if the group funds are composed of bona fide earnings." Group funds earned against the rules do not count. — [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md)
- Legacy-rate Robux, including Robux from group one-time payouts, must be cashed out before current-rate Robux. Group splits and one-time payouts carry the US 18+ rate through to recipients. — [Creator Docs: DevEx](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/developer-exchange.md); [Creator Docs: U.S. 18+ rate](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/18-plus-devex-rate.md)

### Inferences (calculations; inputs cited above)
- **Earned Robux needed for US$3,000 net of DevEx** (before Tipalti fees, FX and withholding):
  - Standard $0.0038 → **789,474 Robux/month** (≈26,316 a day; ≈9.47M a year for $36,000).
  - US 18+ $0.0054 → **555,556**.
  - Legacy $0.0035 → 857,143 (only relevant to holders of pre-Sept-2025 balances).
  - Blends:
    - 10% at the 18+ rate → effective $0.00396 → 757,576 Robux.
    - 25% → $0.00420 → 714,286 Robux.
    - 50% → $0.00460 → 652,174 Robux.
- **Gross player spend (in Robux) to reach 789,474 Earned Robux:**
  - Passes, dev products, private servers and Robux subscriptions at 70% → **1,127,820 Robux**.
  - Avatar items at the base 30% → 2,631,579.
  - Avatar items sold in-game as the affiliate (40%) → 1,973,684.
  - Robux transfers (10% cut) → 7.9M (not a realistic primary source).
  - If all spend qualified for the 18+ rate at 70% → 793,651 Robux of player spend.
- **Gross player spend in US$** (depends on what players actually paid per Robux, which is not verified):
  - At $0.01 per Robux (Roblox's own subscription conversion) → **≈$11,278 a month**.
  - At an illustrative $0.0125 per Robux → **≈$14,098 a month**.
  - Rule of thumb: the creator nets **~21–27% of player dollars** at the standard rate and **~30–38%** on qualifying US 18+ spend.
- **Non-US withholding buffer** after 1 Nov 2026, with a valid W-8 (withholding rate w applied to US-source share s). Gross DevEx needed to net $3,000:

  | w | s | Gross DevEx | Earned Robux (standard rate) |
  |---|---|---|---|
  | 10% | 50% | $3,158 | 831,025 |
  | 15% | 50% | $3,243 | 853,485 |
  | 30% | 25% | $3,243 | 853,485 |
  | 30% | 50% | $3,529 | 928,793 |
  | 30% | 75% | $3,871 | 1,018,676 |
  | 30% on 50% US share, plus 3% FX fee | — | $3,639 | 957,518 |
  | 24% backup withholding on the full payout | — | $3,947 | 1,038,781 |

  US creators with a valid W-9 face no withholding (income tax is still owed).
- **Mixed example:** 700k Robux from passes and dev products + 60k from Creator Rewards (≈400 qualifying Active Spenders a day) + 30k from Plus incentives and transfers = 790k ≈ $3,002 at the standard rate.
- **Timing:** Creator Rewards and Plus incentives clear after 60 days, so in month one only the ~5-day-hold sales are cashable. Budget a 2–3 month ramp before a stable $3k cash-out.
- **Collaborators:** a contributor paid through group splits receives Earned Robux in their own account and cashes out under their own DevEx eligibility (13+, 30k minimum, tax form). Each participant needs 30,000+ Robux to cash out. A small share (e.g., 10% of a modest game) may sit below the minimum for months.

### Gaps
- Real 2026 Robux retail prices, which are needed to turn Robux spend into player-dollar spend precisely.
- Tipalti's per-payout fee for each method.
- Whether a minimum group age or balance applies before payouts unlock (the docs give no numbers).

---

## 5. Official creator-earnings statistics (DevEx totals, distribution, "developer exchange fees")

### Takeaway
Roblox's **"developer exchange fees"** (DevEx cash paid to creators) grew from **$922.8M in 2024** to **$1.503B in 2025** (+63%).

The quarterly path then peaked and fell back:
- 2025: Q1 $281.6M, Q2 $316.4M, Q3 $427.9M, Q4 ≈$477M (implied).
- 2026: Q1 **$423M**, Q2 **$363M** (+15% YoY). H1 2026 total ≈ $786M.

RDC 2026 figures as reported in the press: creators earned about **$1.7B over the 12 months to 30 Jun 2026**. The distribution is extremely top-heavy:
- top 10 averaged $65.7M;
- top 100 averaged $10.8M;
- top 1,000 averaged ~$1.3–1.4M (sources conflict);
- the **median of 42,000+ DevEx participants was ~$1,500**;
- more than $5B has been paid out since 2013.

### Cited Findings
- FY2025 developer exchange fees **$1,503,106 thousand** vs **$922,821 thousand** in FY2024 (+63%). The 10-K attributes this to bookings growth, "differential Robux pricing launched in November 2024, the Creator Rewards Program launched in July 2025, and an 8.5% increase in fiat currency exchange rates for earned Robux effective September 5, 2025" (via search extract). — [Roblox 10-K FY2025 (SEC)](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm)
- 2025 quarters: Q1 $281.6M (+39% YoY), Q2 $316.4M (+52%), Q3 $427.9M (+85%) (via search extract). — [Roblox 10-Q Q3 2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000327/rblx-20250930.htm); [Roblox 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm)
- Q1 2026 developer exchange fees **$423M**, +50% vs $282M (via search extract). — [Roblox Q1 2026 shareholder letter (SEC 8-K)](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026028882/ex991-q12026earningsshar.htm); [Investing.com Q1 2026 slides](https://www.investing.com/news/company-news/roblox-q1-2026-slides-strong-growth-amid-safetydriven-headwinds-93CH-4651643)
- Q2 2026 developer exchange fees **$363M**, +15% vs $316M, "a decline from the $477 million peak in Q4 2025" (via search extract). — [Roblox Q2 2026 earnings release (SEC 8-K)](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm); [Roblox 10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051082/rblx-20260630.htm); [Investing.com Q2 2026 slides](https://www.investing.com/news/company-news/roblox-q2-2026-slides-bookings-growth-slows-to-8-amid-user-decline-93CH-4826401)
- Q2 2026 platform context (via search extract): — [Investing.com](https://www.investing.com/news/company-news/roblox-q2-2026-slides-bookings-growth-slows-to-8-amid-user-decline-93CH-4826401); [Music Ally](https://musically.com/2026/07/31/roblox-ended-q2-2026-with-123-million-daily-active-users/); [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/roblox-cuts-2026-guidance-age-123523142.html)
  - Revenue $1.5B (+36%); bookings growth **8%**, at the low end of guidance.
  - DAU **123M** (+10% YoY), down from a **152M peak in Q3 2025**.
  - Average monthly unique payers 27.0M, down from 36.7M in Q4 2025. Average bookings per monthly unique payer **$19.25**, down from more than $23.
  - FY2026 bookings guidance cut to **$7.33–7.60B** from $8.28–8.55B.
- **RDC 2026 creator-earnings figures** (via search extracts of press coverage):
  - Approximately **$1.7B** in DevEx over the 12 months to 30 Jun 2026, "up around 50% year over year".
  - Top 10 creators averaged **$65.7M**; top 100 averaged **$10.8M**; top 1,000 averaged **$1.4M**.
  - "More than 42,000 creators participate in DevEx" with a **median of ≈$1,500** over the same 12 months.
  - Source: [TweakTown](https://www.tweaktown.com/news/113585/robloxs-top-10-creators-averaged-dollars65-7-million-each-while-the-median-made-dollars1500-and-roblox-everywhere-is-the-fix/index.html); [IBTimes UK](https://www.ibtimes.co.uk/roblox-top-creators-devex-payouts-2026-1819403); [VGTimes](https://vgtimes.com/news/167465-roblox-reveals-creator-earnings-range-from-1500-median-to-65.7-million-average.html)
  - **Conflicting figure:** other secondary analyses give the top-1,000 average as **$1.3M**. — [ShaneTheGamer analysis](https://www.shanethegamer.com/research/roblox-creator-economy-analysis/); [Panstag (Sep 2026)](https://www.panstag.com/2026/09/roblox-creator-economy-earnings.html)
- "Creators have earned more than $5bn through DevEx since 2013" (RDC 2026, via search extract). — [PocketGamer.biz](https://www.pocketgamer.biz/roblox-unveils-new-play-creation-and-monetisation-tools-at-rdc-2026/); [Roblox IR RDC 2026 release](https://ir.roblox.com/news/news-details/2026/Roblox-Unveils-New-Ways-to-Play-Build-and-Grow-at-the-Roblox-Developers-Conference-RDC/default.aspx)
- **Speculative third-party projection, likely outdated:** "$1.8–2.0B" in 2026 payouts, based on revenue guidance of $6.02–6.29B. This predates the July 2026 guidance cut. — [ShaneTheGamer / Panstag (via search extract)](https://www.shanethegamer.com/research/roblox-creator-economy-analysis/)

### Inferences
- Q4 2025's implied ≈$477.2M = $1,503.1M − ($281.6M + $316.4M + $427.9M).
- The payout pool shrank **~24% from Q4 2025 to Q2 2026** ($477M → $363M) and ~14% from Q1 to Q2 2026. Q4 is seasonally strong, but the decline lines up with the age-check-driven fall in DAU and bookings (Section 6). Creators entering in late 2026 face a smaller per-quarter pool than at the late-2025 peak.
- If the $1.7B is "+~50% YoY", the 12 months to June 2025 come to about $1.13B, which is consistent with FY2025's $1.5B.
- **$36,000 a year is about 24× the median DevEx participant (~$1,500).** That is far above typical, but well below the top-1,000 average ($1.3–1.4M). The rank needed for $36k is unknown.

### Gaps
- No official count of creators earning more than $10k, $100k or $1M a year (for 2024, 2025 or 2026) could be retrieved. The Economic Impact Report and the RDC 2025/2026 pages were blocked and the search budget was used up.
- The FY2023 DevEx total, 2025 bookings, and the exact RDC 2026 date and wording were not verified.

---

## 6. 2025–2026 policy and regulatory changes affecting earnings (age checks, maturity labels, publishing and ID requirements, paid random items, country blocks, lawsuits) and their observed effect

### Takeaway
2026 reshaped Roblox around **verified age**:
- **Age checks** have been mandatory for chat since January 2026.
- **Roblox Kids (5–8) / Roblox Select (9–15) / Roblox (16+)** account tiers were announced 13 Apr 2026 and went global in June 2026.
- **Every creator now needs an age check to publish**. Reaching under-16s additionally requires ID or face verification, 2FA, a 2-month Plus/Premium subscription or a refundable fee, and passing an evaluation of **250 highly-engaged age-checked plays within 60 days**.
- Experiences without maturity info have restricted playability; Restricted (18+) games are blocked in Korea, Saudi Arabia, Türkiye and similar markets; paid random items must be gated per user with PolicyService.

Observed effect: Q2 2026 per-hour monetization fell, especially among younger US and Canadian users. Roblox cut FY2026 bookings guidance by about $0.9B, and quarterly DevEx payouts fell from $477M (Q4 2025) to $363M (Q2 2026).

### Cited Findings
**Age-based accounts and publishing requirements**
- Roblox "implemented mandatory age checks in January for all users who want to access chats". Kids/Select accounts were announced 13 Apr 2026 (via search extract). — [TechCrunch, 2026-04-13](https://techcrunch.com/2026/04/13/roblox-introduces-kids-and-select-accounts-for-age-appropriate-access-to-games-and-chat/)
- The accounts became "Now Globally Available" in June 2026. A secondary site gives **16 Jun 2026**. — [Roblox Newsroom (June 2026, title via search)](https://about.roblox.com/newsroom/2026/06/age-based-roblox-kids-and-select-accounts-now-globally-available); [BloxGuides (secondary)](https://bloxguidesgg.com/blog/roblox-kids-select-accounts-global-launch-june-16-2026)
- **Tier rules:** — [Creator Docs: Roblox Kids and Select (added 2026-05-19; upd. 2026-09-12)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/publishing/kids-and-select.md)
  - Kids sees Minimal and Mild content; Select sees Minimal, Mild and Moderate; Roblox (16+) sees all rated content except Restricted.
  - A self-declared age only sets a temporary tier until the user completes an age check.
- **Publishing to 16+ (the minimum):** account in good standing and at least 2 days old; **age verification** by facial age estimation or government ID; completed Maturity & Compliance Questionnaire. — [Creator Docs: Roblox Kids and Select](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/publishing/kids-and-select.md)
- **Publishing to under-16s:** — [Creator Docs: Roblox Kids and Select](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/publishing/kids-and-select.md); [Creator Docs: Publish games and places (upd. 2026-09-24)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/publishing/publish-games-and-places.md)
  - Verification: facial age estimation if under 18, **government ID if 18+**; plus 2FA.
  - A fee or subscription: an active Plus or Premium subscription held for 2 consecutive months, **or** a refundable **1,000-Robux publishing fee**. It is refunded if the game keeps 25 highly engaged players for 60 days without moderation.
  - An evaluation: a trial with age-checked 16+ users, bot and spend analysis, a safety review, and a threshold of **250 unique plays by highly engaged age-checked users within 60 days**.
  - Optional **expedited review**: a refundable **50,000-Robux** fee, refundable after 90 days if the game keeps 25 highly engaged players.
- **Maturity labels:** — [Creator Docs: Content maturity (upd. 2026-09-26)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/promotion/content-maturity.md)
  - "If an experience does not have accurate or all content maturity information, Roblox restricts the playability of the experience on the platform for all players."
  - Restricted games are only for age-verified users 18+ and "are unplayable for players who created their accounts or are located in certain countries or regions, such as Korea, Saudi Arabia, and Türkiye".
  - Roblox "restricts free-form user creation and social hangouts to players over 16."
- **ID or age verification required for specific monetization:** — [Creator Docs: Rewarded video ads](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/promotion/rewarded-video-ads.md); [Creator Docs: Immersive ads](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/immersive-ads.md); [Creator Docs: Creator Rewards](https://github.com/Roblox/creator-docs/blob/main/content/en-us/creator-rewards.md); [Creator Docs: Creator Store](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/creator-store.md); [Creator Docs: Commerce](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/commerce-products.md); [Creator Docs: Subscriptions](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/subscriptions.md)
  - Ads (rewarded and immersive): ID verification + 2FA.
  - Creator Rewards Audience Expansion: ID-verified account.
  - Creator Store selling: age check or ID.
  - Commerce: 18+ and ID-verified.
  - Local-currency subscriptions: ID or phone verification.
- **Paid random items:**
  - Odds must be disclosed as percentages summing to 100%, including for indirect purchases with currency bought using Robux.
  - When `PolicyService:GetPolicyInfoForPlayerAsync()` returns `ArePaidRandomItemsRestricted = true`, the user "cannot interact with paid random item generators". Creators must apply one of the prescribed alternatives, e.g., offering the item for direct purchase.
  - Source: [Creator Docs: Paid random items (upd. 2026-07-07)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/paid-random-items.md); [Creator Docs: Monetization overview](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/index.md)

**Country-level restrictions**
- Region-restricted games are "neither discoverable nor playable by users in that country", while other regions are unaffected. — [Creator Docs: Regional content availability](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/promotion/regional-content-availability.md)
- Monetization products are also unavailable by country (see Section 2): local-currency subscriptions and paid access exclude Argentina, China, Colombia, India, Indonesia, Russia, Taiwan, Türkiye, UAE, Ukraine and Vietnam (plus Japan for subscriptions). Creator Store selling excludes Brazil, China, India and Russia. — [Creator Docs: Subscriptions](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/subscriptions.md); [Creator Docs: Paid access local currency](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/paid-access-local-currency.md); [Creator Docs: Creator Store](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/creator-store.md)
- **Russia** blocked Roblox on **3 Dec 2025**. — [Tom's Guide](https://www.tomsguide.com/computing/online-security/russia-blocks-roblox-and-demand-for-vpns-skyrockets); [VOI](https://voi.id/en/technology/546018)
  - Aggregator sites claim the block was **lifted in June 2026** after Roblox agreed to age-gate access. This is unverified and from a low-reliability aggregator. — [rblxdb](https://rblxdb.com/guides/is-roblox-getting-banned)
- **Iraq** banned Roblox on **21 Oct 2025**, and **Indonesia** blocked users under 16 from **28 Mar 2026** (aggregator claims via search extract). — [rblxdb](https://rblxdb.com/guides/is-roblox-getting-banned); [BearVPN](https://bearvpn.com/blog/where-is-roblox-banned/)
- A social-media list of full bans (China, Iran, North Korea, Türkiye, Algeria, Egypt, Oman, Palestine, Russia, Iraq, Qatar) is low reliability. — [X post (low reliability)](https://x.com/imcyrian/status/2040740990290714863?lang=en)

**Observed effect on creator revenue**
- Q2 2026: "The bookings shortfall reflects a decline in per hour monetization most notably with younger cohorts in the U.S. and Canada." The search extract also attributes it to "a greater than expected shift of approximately one-third of age-checked DAUs" (sentence truncated in the extract). — [Investing.com Q2 2026 call transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-roblox-q2-2026-beats-eps-but-shares-sink-on-bookings-93CH-4826338); [Yahoo Finance: "Roblox cuts 2026 guidance after age-verification slowdown"](https://finance.yahoo.com/markets/stocks/articles/roblox-cuts-2026-guidance-age-123523142.html)
- FY2026 bookings guidance fell by about $900M, and Roblox warned of a further sequential DAU decline. DevEx fees fell from $477M (Q4 2025) → $423M (Q1 2026) → $363M (Q2 2026) (via search extract). — [Investing.com Q2 2026 slides](https://www.investing.com/news/company-news/roblox-q2-2026-slides-bookings-growth-slows-to-8-amid-user-decline-93CH-4826401)
- Roblox's own response points creators toward adults: the US 18+ DevEx rate ties extra pay to adult US spend (Section 1). — [Creator Docs: U.S. 18+ rate](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/18-plus-devex-rate.md)

### Inferences
- **Launches now start with an age-checked 16+ audience.** Reaching the large under-16 audience requires passing the 250-highly-engaged-plays evaluation (or paying the refundable 50k-Robux expedited fee).
- For a new indie title, the fastest money is likely **16+/18+ design**: older-skewing genres, an R15-only rig for the 18+ rate, and no reliance on paid random items or social-hangout mechanics.
- Any loot-box-style monetization must be wrapped in `PolicyService` checks, with a direct-purchase alternative for restricted users. This is extra engineering (well suited to a strong scripter) and can lower conversion in affected regions.
- **Country risk:** sudden blocks (Russia, Iraq, Indonesia's under-16 rule) can remove players and payers overnight. Payment-feature exclusions (local-currency subscriptions and paid access in about 11–12 countries) limit those tools there. Robux-priced products are the most globally available.

### Gaps
- **Lawsuits and regulatory actions** (US state attorneys-general suits, multi-district litigation, Brazil's child-protection law affecting loot boxes, Australia/EU/UK rules) **could not be verified**: the web-search budget ran out before these queries. Background knowledge (pre-2026, unverified here) suggests 2025 suits by the Louisiana, Kentucky and Texas AGs and a Florida investigation. The report writer should verify status and any monetization impact before use.
- Whether Russia's block was actually lifted (and on what terms), and whether Türkiye, Qatar or other blocks still stand as of Oct 2026, are unconfirmed.
- No quantified per-creator effect of the age checks (e.g., a median game's revenue change) was found. Only platform-level metrics are available.

---

## 7. Tax and legal basics for non-US creators receiving DevEx (general, not country-specific)

### Takeaway
- Non-US creators file **Form W-8BEN** (individuals) or **W-8BEN-E** (entities) and may claim a **US tax-treaty rate**. This requires a TIN, and the country of citizenship (or incorporation) must match the country of the permanent residence address.
- Until 31 Oct 2026, non-US creators generally received no US tax form (the payments were service-type).
- From **1 Nov 2026**, DevEx payouts are **royalties**. Roblox withholds **0–30% US tax on the US-source portion** (purchases by US players), issues **Form 1042-S**, and applies **24% backup withholding** if tax info is missing or invalid.
- Income remains taxable under the creator's home-country rules; withholding is a prepayment of tax, not a fee.

### Cited Findings
- Non-US persons must use W-8BEN or W-8BEN-E, which "certify your foreign tax status and may allow you to claim a reduced U.S. withholding tax rate under an applicable tax treaty". — [Creator Docs: tax information](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/tax-information.md)
- A treaty claim needs a valid, complete W-8 that includes a TIN (US or foreign) and lists a country of citizenship or incorporation matching the permanent residence address. Supporting documents (ID or passport, business registration, proof of TIN or residency) may be requested. — [Creator Docs: tax information](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/tax-information.md)
- "U.S.-source income… For DevEx, this generally maps to the portion of your earnings related to purchases made by U.S. players." Withholding "may apply only to the U.S.-source portion of your earnings instead of your entire payment." — [Creator Docs: tax information](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/tax-information.md)
- "**Withholding taxes are not fees.** They are income taxes deducted from your payout and remitted to the IRS on your behalf." Withholding details and Form 1042-S are available on the Creator Hub Taxes page. "Roblox does not provide tax advice." — [Creator Docs: tax information](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/tax-information.md)
- Under the pre-1 Nov 2026 regime, "Non-U.S. persons generally will **not** receive an annual tax form from Roblox". US persons received **1099-NEC** (nonemployee compensation, i.e., payment for services) when payments exceeded $2,000. — [Creator Docs: DevEx Portal](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/devex-portal.md); [Creator Docs: tax information](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/tax-information.md)
- After 1 Nov 2026 the IRS treatment changes: "As of November 1, 2026, DevEx payments are treated as royalties for U.S. federal income tax purposes" ("compensation for the use of intellectual property"). — [Creator Docs: tax information](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/tax-information.md)
- DevEx is available to companies as well as individuals; the entity's payment method and tax form must match. — [Creator Docs: DevEx Portal](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/devex-portal.md)
- Separate payment rails carry their own tax onboarding: Creator Store sales (USD via **Stripe**, which collects TIN details) and local-currency paid access (via a separate **Tipalti** tax and banking setup). — [Creator Docs: Creator Store](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/creator-store.md); [Creator Docs: Paid access local currency](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/monetization/paid-access-local-currency.md)

### Inferences
- **Pre-Nov 2026 status.** The 1099-NEC (US) and the "no form" practice for non-US persons both point to DevEx having been treated as **payment for independent services**, not employment. Creators have been self-employed or independent contractors under their home-country rules and responsible for their own income tax and social contributions.
- **Post-Nov 2026 status.** The royalty classification brings US-source withholding for non-US creators. Its size depends on (a) whether the creator's country has a US treaty with a reduced royalty rate (0–30%) and (b) the share of their game's revenue from US players. A game aimed at US adults (to capture the 18+ rate) maximizes that share. So the **18+ uplift and the withholding exposure rise together** for non-treaty-country creators.
  - At 30% withholding, an 18+ Robux nets 0.0054 × 0.7 = **$0.00378**. That is still 42% more than a withheld standard-rate US Robux (0.0038 × 0.7 = $0.00266).
  - But it is roughly the same as, and slightly *less* than, an un-withheld standard Robux from a non-US player ($0.0038).
  - So for a creator from a 30%/no-treaty country, the 18+ rate roughly cancels the US withholding rather than adding to income.
- Whether US withholding can be credited against home-country tax depends on local law (foreign tax credit and treaty relief). Creators should keep the 1042-S and get local professional advice.
- Creators who operate through a company file a W-8BEN-E, and the entity's treaty position then applies. This can change the effective rate, so it is worth discussing with an advisor before scaling past the $3k/month level.
- **General compliance checklist (inference, country-agnostic):**
  - register for income tax or self-employment locally as required;
  - keep records of monthly DevEx and Creator Store or Stripe payouts;
  - track FX conversion (Tipalti's 1.9–3% fee, or a bank's rate);
  - check whether local VAT/GST rules treat royalty or service income from a US company as reverse-charge or exempt;
  - file the treaty claim before 31 Oct 2026.

### Gaps
- The DevEx Terms of Use text (blocked) could not be checked for explicit "independent contractor" language, governing law, or creator-side tax indemnities.
- Country-by-country treaty royalty rates were not compiled: the user's country is unknown and the IRS treaty pages were blocked. The report writer should use the IRS "United States Income Tax Treaties A–Z" list referenced in the docs.
- Whether Creator Store (Stripe) USD income is also reclassified or subject to withholding after 1 Nov 2026 is not addressed in the docs read.
