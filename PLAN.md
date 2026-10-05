# Plan: US$3,000/month

Plan v1.1, 5 Oct 2026. Based on `reports/Roblox scripter income strategies.md`, revised after the [Codex review](reports/Codex%20review%202026-10-05.md) (claims checked against Roblox's docs). **Awaiting the owner's review.**

**In one line:** sell one well-scoped Roblox engineering offer for dollars, prove it with collected cash, then build a contracted floor and test games on the side with a time limit.

**Read the numbers as scenarios.** Targets and dates below are things to test, not forecasts. Nothing here has been proven for this owner yet.

## Urgent: DevEx tax change

Source: Roblox [tax information](https://github.com/Roblox/creator-docs/blob/9f840b170b3e472c705e035126b45e3e050daed2/content/en-us/production/monetization/tax-information.md) doc, checked 5 Oct 2026.

| When | What to do | Who |
|---|---|---|
| **Now** | Open **Creator Hub → Finances → Taxes** and read your status. A valid W-9 already in Tipalti migrates on its own and shows **Validated** (no action). Otherwise submit there: W-9 (US person), W-8BEN (non-US individual) or W-8BEN-E (non-US entity). Claim a treaty rate only if you qualify. Payouts still go through Tipalti | Owner |
| **15 Oct 2026** | Roblox's *recommended* last day to request a DevEx payout under current terms. Not a guarantee: the **payout date** decides, so a payout on or after 1 Nov may be taxed as a royalty | Owner |
| **31 Oct 2026** | Last day for tax info to count for the first royalty payouts. Without valid info, 24% backup withholding **may** apply to the whole payout | Owner |
| 1 Nov 2026 | DevEx becomes royalties. Non-US creators with valid info: 0 to 30% on earnings from US-player sales, by country and treaty | Info |

## Rules of thumb

- **Quote in USD.** If a client insists on Robux: about 263 Robux = $1 (DevEx $0.0038/Robux). Robux pay keeps about 30% of what the client spent.
- **Fixed price per scoped outcome**, with written acceptance checks, a deposit and milestones. Keep files until paid. Check PayPal's current Seller Protection terms for your country before relying on them; keep proof of delivery.
- **Count collected cash, not invoices.** Effective rate = collected USD ÷ all hours, including scoping, calls, revisions and selling.
- **$3,000 gross is not take-home.** Payment fees, expenses and income tax come off. Decide which one the goal means (`PROFILE.md`).
- **Capacity math:** gross = hours/week × 4.33 × billable share × realized rate. Example: 30 h × 4.33 × 60% × $50 = $3,900. At 20 h and 50%, the same rate gives $2,167.
- **Revenue share only on top of** guaranteed pay. 10% of a game making 500k Robux/month is about $190.
- **No single client** (other than an employer) above 50% of income.

## Stage 1 · Ten days to evidence (5 to 18 Oct)

Follows the [Codex execution brief](plan/codex_income_execution.md). Pause broad research during this sprint.

- [ ] Fill in `PROFILE.md`: country and tax residence, 18+, weekly hours, runway, shippable work, gross or take-home
- [ ] Tax steps above; ID-verify the Roblox account; 2-step verification on
- [ ] **One offer** in your strongest proven area. Only offer what you can show. Drafted in `plan/portfolio.md`: recommended "one moving system, replicated once"; alternates are a save/duplication/validation fix and a vehicle handling pass. Pick one
- [ ] **One case study** from work you may publish: problem, your role (name any AI help), before/after, short demo, one test. Template and 3 candidates from your game: `plan/portfolio.md` §2. Build new demos only if nothing shippable can be shown
- [ ] Up to 10 **qualified** leads: current opening or clear need, real organization, eligible geography, source URL checked on a stated date. 10 candidates in `plan/leads.md`, none verified live yet: open each link to confirm
- [ ] HiddenDevs "Luau Scripter" application and a DevForum for-hire thread, sent only with the owner's OK. Drafts and rate card: `plan/outreach/`. HiddenDevs refuses AI-written code; DevForum posting needs an age-verified 18+ account (search summaries, 5 Oct 2026)
- [ ] Set your contract defaults: `plan/contract_template.md` (not legal advice)
- [ ] Before the first interview: `plan/interview_prep.md` (5 sessions)

**Exit:** proof and offer reviewable; qualified leads listed. If there are no qualified leads, fix eligibility or the channel before making more portfolio assets.

## Stage 2 · Cash engine (weeks 3 to 9, to early Dec)

- Fixed USD quotes, roughly $500 to $1,500 per scoped system (vendor price guides, unverified). Reply to leads within hours.
- 8 to 12 applications to studios with **currently open** roles, starting from `plan/leads.md` (best first: Twin Atlas, Voldex, Roblox's Technical Developer Specialist contract). Check each role's country rules against `PROFILE.md`.
- Rehearse a 60 to 90 minute live technical interview.

**Targets to test:** first paid job by week 3; $1,000 collected by week 4; $2,000 in month 2; two interview processes by week 6.

**If it stalls, find the failing step and change one thing:**

| Symptom | Next move |
|---|---|
| Leads but no replies | Check fit, delivery and the pitch. A small batch is weak evidence |
| Replies but no scoped work | Ask what is missing: proof, availability, trust, price or relevance |
| Proposals but no yes | Compare scope, terms and alternatives. Do not cut price by reflex |
| Paid work, poor effective rate | Tighten scope and acceptance checks before taking more |
| Approved but unpaid | Pipeline, not income. Track due dates |

Consider FiveM, TypeScript or bot work only after the Roblox offer has been tested and adjusted, not after one failed batch.

## Stage 3 · Contracted floor (months 3 to 6, Dec to Mar)

- Accept a contract at **$3,000+/month or $30+/hour**, or turn the best clients into 2 to 3 monthly retainers (live-ops, optimization, security audits).

**Ambition, not forecast:** a first $3,000 collected month around January 2027; $3,000+ contracted or recurring by month 6.
**Fallback:** no offer by month 4, so build the floor from retainers plus commissions, then TypeScript or Discord-bot work; kids' coding instruction only as a last resort.

## Stage 4 · Upside (months 4 to 12, 10 to 15 h/week)

- **3 to 4 different prototypes**, each 2 to 4 weeks: a proven loop with a twist, 16+ audience, R15-only, server-authoritative, policy-checked monetization. Two milestones of one game count as one bet.
- **Stygian Drop** goes first, as a small **no-spend** test: Experiment A in `games/stygian-drop/REFINED_CONCEPT.md` section 5 (invite-only, 8 new players). Time-box it, and re-estimate only after inspecting the real game repo. It can run at up to 10 h/week during stages 1 and 2. Hold anything bigger until the floor is in place.
- **Paid tests later**, and only with the owner's OK: a stable build, verified funnel events, a hard spending cap and a written sample plan. Count unique new players, not plays. Ads can speed up discovery consideration, but ranking uses the engagement of players who came from Recommended for You.
- One Creator Store plugin, or a kit sold off-platform where Stripe is not available.

**Targets:** voluntary replay in invite tests first. Then, once a game has 100+ daily users, compare day-one retention with **its own peer benchmark in Creator Hub**. Roblox's 12.11% and 18.73% figures are an example in its docs, not a benchmark. Keep 12% only as a provisional internal goal. Report numerators and denominators per cohort and source.
**Fallback:** four prototypes without voluntary replay or peer-level retention, so stop the game track and move the hours to products and retainers, or join a funded team.

## Checkpoint (month 9+)

Scale a game only when organic players perform and ads earn back their cost (up to 4% of earnings on ads). Move contract hours to a game only in proportion to the cash it paid in **two consecutive DevEx cycles**.

## Weekly scoreboard

Empty means unknown, not zero. Keep client details out of this public repo.

| Week of | Qualified leads | Sent (owner OK) | Replies | Proposals | Paid starts | Collected USD | Unpaid USD | Delivery h | Total business h |
|---|---|---|---|---|---|---|---|---|---|
| 5 Oct | | | | | | | | | |
| 12 Oct | | | | | | | | | |
| 19 Oct | | | | | | | | | |
| 26 Oct | | | | | | | | | |
