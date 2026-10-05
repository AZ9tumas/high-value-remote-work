# Contract and payment terms template

**Template, not legal advice. Have it reviewed for your country before relying on it.**

Claude, 5 October 2026, for task C-008. A draft for the owner's review. Everything in [BRACKETS] is yours to fill in or choose.

## How to use

- **Full template (part 1):** systems, retainers and any job above [SMALL JOB LIMIT] USD. Attach the spec (Schedule A).
- **One-page version (part 2):** one fix or a small script.
- Fill in every placeholder and delete unused options. Keep your hour estimate private and use it to track your effective rate (`plan/codex_income_execution.md`).
- Name a real person or company as the client. A Roblox group is a platform feature, not a party that can sign.
- If a studio sends its own contract, check it for the same points: deposit, handover after payment, IP on payment, your own tools, portfolio rights, liability cap.
- **Fill in copies outside this repo.** Never commit signed contracts, client names or payment details here.
- **These depend on the country, so get local advice on them:**
  - contracts with anyone under 18, on either side;
  - e-signatures, and how an IP transfer must be signed;
  - late fees, non-refundable deposits and liability limits;
  - VAT, GST and tax withholding;
  - data protection, if you touch player data;
  - where disputes can be heard.

## 1. Full template

### Development agreement

Date: [DATE] · Project: [PROJECT NAME]

**1. Parties.**
Contractor: [CONTRACTOR], [COUNTRY], [EMAIL], Roblox ID [ROBLOX ID].
Client: [CLIENT], [COUNTRY], [EMAIL], Roblox ID [ROBLOX ID], group ID [GROUP ID].
Both parties are 18 or older. If the client is not, a parent or guardian also signs and takes on the client's duties.

**2. Independent contractor.** The contractor is independent, not the client's employee, partner or agent. It chooses how and when to work, uses its own equipment and may work for others. Subcontractors need the client's written consent.

**3. Scope.** The deliverables and acceptance checks are in the spec (Schedule A). An acceptance check is a testable result, such as "data reloads after a server shutdown". Anything else is excluded, such as art, animation, sound, third-party code, publishing, and changes to the live game or live data, unless the spec lists it. The contractor will not break Roblox's Terms of Use. These terms override the spec unless it names the clause it changes.

**4. Price and milestones.**
- Fixed price: [PRICE] USD, including clause 5 revisions and clause 10 support.
- Deposit: [DEPOSIT %] of the price, paid before work starts and counted toward it. Work starts once it clears and the Schedule A access is in place.
- Each milestone is invoiced on acceptance. The next starts after payment.
- Discovery, for unclear scope: up to [DISCOVERY HOURS] hours for [DISCOVERY FEE] USD, paid first. It delivers findings, a fix plan and a fixed quote, and the fee is due even if the cause is not found. The cap rises only with written approval. The client may then stop, or adopt the quote in an updated Schedule A [with the fee counted toward it].

**5. Changes and revisions.** Change requests must be in writing. The contractor quotes the cost and new dates, and starts only after written agreement. Changes are billed at [HOURLY RATE] USD per hour or an agreed fixed price. Each milestone includes [REVISION ROUNDS] revision rounds within the spec; extra rounds are billed hourly. Fixing a failed acceptance check is free and not a revision. New features are change requests.

**6. Timeline and client delays.** Schedule A dates move day for day with client delays in payment, access, feedback, assets or decisions. If the client is silent for [SILENCE DAYS] days, the contractor may pause and invoice current-milestone work at [HOURLY RATE], up to its price. Silence for [SILENCE DAYS] more days after a written reminder counts as cancelling (clause 17). The contractor warns early of any slip.

**7. Delivery and acceptance.** Each milestone comes with a delivery note, test steps, a demo and the result of each acceptance check. Within [ACCEPTANCE DAYS] days, the client accepts or lists failed checks with steps to reproduce. The contractor fixes them, with a new window for those items only. Silence after the window, or use in a game open to players, means accepted. Issues outside the acceptance checks are change requests, not grounds to reject.

**8. Roblox delivery.**
- The contractor works in [a test place or copy owned by the client / its own place or repository]. It changes the live game only if the spec says so, with written approval for each live publish.
- The client keeps ownership and control of its games, groups, accounts, assets and data. Nothing here transfers any of them between the parties.
- Before full payment, the contractor shows the work by video, demo or playtest. Code, place files, models and packages are handed over only after full payment clears. Format: [Rojo repository / .rbxl or .rbxm file / package in the client's group].
- Work inside a client-owned place, such as in Team Create, is visible before payment. Clause 11 still applies.
- Assets such as images, meshes, audio and animations go under the client's account or group.
- The client keeps backups. Player-data changes are tested on test data first.

**9. Access and security.**
- Neither party asks for or shares passwords, cookies (including .ROBLOSECURITY), 2-step verification codes or recovery codes.
- Access is by role, at the lowest level that works: Team Create on the test place, edit access to the test experience only, or repository access. There is no access to group funds, payouts, roles, secrets or live publishing unless the spec requires it. Any API key is created by the client, narrowly scoped and set to expire.
- Neither party asks the other to paste code into browser developer tools, use a login link sent in a message, or run unknown programs or plugins.
- Both keep 2-step verification on and report a suspected compromise at once.
- The client removes access at the end. After the support window, the contractor deletes the client's confidential material, except required records and clause 12 materials.

**10. Warranty and support.** For [SUPPORT DAYS] days after final acceptance, the contractor fixes for free any failed acceptance check in the Schedule A environment. The client reports it in writing with steps to reproduce, and the contractor responds within [RESPONSE DAYS] business days. Not covered: others' changes, third-party code, later Roblox changes and new features. No system is exploit-proof; the contractor does not guarantee against exploits or data loss. Otherwise the work is provided as is, as far as the law allows.

**11. Intellectual property.**
- Until full payment, the contractor owns the deliverables, and the client may use them only for testing. Using unpaid work in a game open to players makes the whole price due at once.
- On full payment, the contractor assigns to the client all rights in the deliverables made for this project, except Contractor Tools.
- Contractor Tools are code, libraries, plugins and know-how the contractor made before or outside this project. It keeps them and grants the client a non-exclusive, perpetual, worldwide, royalty-free licence to use and modify them as part of the deliverables. The licence passes with the game if it is sold. Contractor Tools may not be resold on their own.
- Third-party code listed in Schedule A keeps its own licence.

**12. Portfolio and credit.** After public release [or [PORTFOLIO MONTHS] months after final payment, if sooner], the contractor may show the non-confidential work in its portfolio and applications: short videos, screenshots, its role and short code excerpts. The client grants a non-exclusive licence for this. Unreleased content, security details, player data and non-public figures stay private. An NDA or the spec can limit this right. [Option: the game's credits list the contractor as "[CREDIT LINE]".]

**13. Confidentiality.** Each party keeps the other's non-public information confidential and uses it only for this project. That includes unreleased content, code, revenue, player data and access details. It excludes information that becomes public through no fault of the receiver, that the receiver already had or builds independently, or that the law requires it to disclose. Security weaknesses go only to the client. This lasts [CONFIDENTIALITY YEARS] years after the end, and indefinitely for player data and access details. A signed NDA prevails.

**14. Liability.** Each party's total liability is capped at the fees paid under this agreement [in the 12 months before the claim]. Neither is liable for indirect loss, such as lost revenue, Robux, players or data. The contractor does not guarantee revenue, CCU, retention, discovery or moderation outcomes. These limits do not cover the duty to pay, fraud, or anything the law does not allow to be limited.

**15. Payment and late payment.** Invoices are in USD, due within [PAYMENT DAYS] days, and paid by [METHODS] from the client's own account or the company in clause 1. [FEE PAYER] pays transfer, processing and conversion fees. Payment counts when cleared funds arrive. A reversed or charged-back payment counts as unpaid. The client raises problems under clause 20 before any payment dispute. If payment is late, the contractor may pause and withhold deliverables, and dates move. Late amounts carry [LATE FEE] where the law allows. After [LATE DAYS] days late, the contractor may end the agreement under clause 17.

**16. Robux (only if Schedule A accepts them).** The Robux price is the USD price divided by the standard DevEx rate on [QUOTE DATE] ([DEVEX RATE] USD per Robux), rounded up, plus [MARGIN %, or 0%]. It is paid only by one-time group payout from a group the client controls. Robux count as paid only when available, not pending. The client confirms they are the group's bona fide earnings, paid out under Roblox's rules. If Roblox restricts or reverses a payout, or holds it over [HOLD DAYS] days, the client pays in USD within [PAYMENT DAYS] days. Refunds are in USD at the quoted rate.

**17. Termination and kill fee.**
- The client may cancel in writing at any time. It then pays for accepted milestones, for current-milestone work at [HOURLY RATE] up to its price, and a kill fee of [KILL FEE %] of unstarted milestones. The deposit is kept and counted toward this. The same applies when the contractor ends the agreement under clause 6 or 15, or for the client's serious breach.
- Either party may end it for a serious breach not fixed within [CURE DAYS] days of written notice. The contractor may also withdraw on [NOTICE DAYS] days' notice. If the contractor withdraws, or the client ends it for the contractor's breach, the client pays only for accepted milestones and gets the rest back, including any unused deposit.
- On ending, paid work is handed over and access is removed. Clauses 11 to 16, 18, 20 and 21 continue.

**18. Taxes.** Each party handles its own taxes. Prices exclude VAT, GST and sales tax, which are added where they apply. If the client must withhold tax, it says so before paying and gives proof. [Option: it adds the withheld amount so the contractor receives the full invoice.]

**19. Retainer (optional).** [RETAINER FEE] USD a month, paid in advance by day [DUE DAY], buys up to [RETAINER HOURS] hours of Schedule A work. Unused hours [expire / roll over one month]. Approved extra hours cost [HOURLY RATE]. Responses come within [RESPONSE DAYS] business days. After [MINIMUM MONTHS] months, either party may end it on [NOTICE DAYS] days' written notice. Tasks are accepted under clause 7. Code is handed over once its month is paid.

**20. Disputes and governing law.** The parties first try in good faith to settle a dispute for [TALK DAYS] days after written notice, then take it to [FORUM]. The law of [JURISDICTION] governs this agreement. Either party may seek urgent relief to protect confidential information or IP.

**21. General.** This agreement, Schedule A and any NDA are the whole agreement. Changes need written agreement; email and [CHANNEL] messages count. Neither party may transfer it without the other's written consent. An unenforceable clause leaves the rest intact. Neither party is liable for delays beyond its control, such as Roblox outages. E-signatures and copies count as originals.

**Signatures**

| | Contractor | Client | Parent or guardian, if needed |
|---|---|---|---|
| Name and title | | | |
| Signature or e-signature | | | |
| Date | | | |

### Schedule A: spec

| Field | Entry |
|---|---|
| Game and place | [GAME NAME], place ID [PLACE ID] |
| Problem or goal | [FAILING BEHAVIOR or FEATURE] |
| Environment | [DEVICES, SERVER OR CLIENT] |
| Deliverables and checks | [DELIVERABLE]: [STARTING STATE], [ACTION], [EXPECTED RESULT] |
| Extra exclusions | [LIST] |
| Work location and access | [TEST PLACE OR REPOSITORY]; [ROLE] |
| Handover format | [ROJO REPOSITORY / .RBXL OR .RBXM FILE / PACKAGE] |
| Contractor Tools; third-party code | [LIST, WITH LICENCES] |
| Revisions · acceptance · support | [REVISION ROUNDS] rounds · [ACCEPTANCE DAYS] days · [SUPPORT DAYS] days |
| Robux accepted | [NO / YES] |

Milestones other than discovery add up to the price, deposit included.

| Milestone | Deliverable and checks | USD | Due |
|---|---|---|---|
| Discovery (optional) | Findings, fix plan, quote; up to [DISCOVERY HOURS] hours | [DISCOVERY FEE], paid first | [DATE] |
| Deposit | | [AMOUNT] | Before start |
| M1 | [DELIVERABLE]; [CHECKS] | [AMOUNT] | [DATE] |
| Final | [DELIVERABLE]; [CHECKS]; handover after full payment | [AMOUNT] | [DATE] |

## 2. One-page version for small jobs

### Small job agreement

[CONTRACTOR] ("I") and [CLIENT] ("you"), Roblox IDs [ROBLOX ID] and [ROBLOX ID], agree on [DATE]:

1. **Job.** [TASK] in [GAME OR PLACE]. Done when: [ACCEPTANCE CHECKS]. Anything else is quoted separately.
2. **Price.** [PRICE] USD, fixed: [DEPOSIT %] before I start, the rest before handover, by [METHOD]. [FEE PAYER] pays the fees. Paid means cleared funds in my account; a reversed payment counts as unpaid.
3. **Robux, only if agreed.** [ROBUX PRICE] Robux (the USD price divided by [DEVEX RATE]) by one-time group payout, counted as paid only when available, not pending.
4. **Handover.** I work in a test copy or my own place and show results by video or playtest. The code ([FORMAT]) comes only after full payment. You keep your game, group and assets; nothing is transferred between us. Assets go under your account or group.
5. **Access.** We never share passwords, cookies (including .ROBLOSECURITY) or 2-step codes. I get Team Create or a limited role on the test place only, removed when we finish.
6. **Checks.** You have [ACCEPTANCE DAYS] days to test. Silence or live use means accepted. [REVISION ROUNDS] revision round(s) included. Fixing a failed check is free.
7. **Support.** For [SUPPORT DAYS] days after acceptance, I fix failed checks for free. No guarantee of revenue, CCU or retention, or that exploits are impossible.
8. **Rights.** On full payment, you own the code made for this job. I keep my existing tools and license them to you for your games, non-exclusively and permanently. After release, I may show non-confidential parts in my portfolio unless we sign an NDA.
9. **Confidentiality.** We each keep the other's non-public information private.
10. **Liability.** Capped at the fees paid. Neither side is liable for lost revenue, Robux, players or data.
11. **Cancelling.** If you cancel after I start, you pay for work done at [HOURLY RATE], at least [MINIMUM FEE] USD; I refund any prepayment above that. If I can't finish, I refund payment for undelivered work.
12. **Late payment.** I may pause and keep the work until paid. Late fee: [LATE FEE], where the law allows.
13. **Taxes.** Each of us pays our own taxes.
14. **Disputes.** We talk first for [TALK DAYS] days, then [FORUM]. Governing law: [JURISDICTION].
15. **Age.** We are both 18 or older, or your parent or guardian also signs.

Signed or e-signed: [CONTRACTOR] [DATE] · [CLIENT] [DATE] · [GUARDIAN, IF NEEDED] [DATE]

## 3. Before you start

- [ ] **Client checked.** The Roblox account and group are real and match the game. The person owns it or has a role that shows authority. Contact details match across channels.
- [ ] **Age.** The client is 18 or older, or a parent or guardian will sign. The rules differ by country.
- [ ] **Spec agreed:** deliverables, acceptance checks, exclusions, milestones and dates.
- [ ] **Agreement signed** or e-signed by both sides.
- [ ] **Deposit or discovery fee cleared** in your own account. A screenshot is not payment. Robux count only when available, not pending.
- [ ] **Payment method checked.** You have read its current terms for your country: fees, disputes and chargebacks, cover for services and digital goods, and proof of delivery.
- [ ] **Test copy, not the live game.** Place copying is off before private assets go in ([Roblox groups doc][groups], checked 5 Oct 2026).
- [ ] **Least-privilege access.** Team Create on the test place, or edit access to the test experience only. Not a group-wide edit role: it reaches every group game and the Data Stores Manager ([groups doc][groups]). No funds, payout, role, secrets or API key permissions.
- [ ] **No credentials shared** either way: no passwords, cookies, .ROBLOSECURITY, 2-step or recovery codes.
- [ ] **2-step verification on** for your Roblox, email, GitHub and payment accounts.
- [ ] **Backups.** The client has a backup of the live place and data. Data changes are tested on test data.
- [ ] **Records kept outside this repo:** agreement, spec, messages, invoices, delivery notes, demo videos and commits. They are your proof of delivery.
- [ ] **Dates tracked.** Acceptance windows and invoice due dates are in your calendar. Unpaid invoices are pipeline, not income (`PLAN.md`).

## 4. Scam red flags

Source: [research note][note] section 4 unless marked, researched 5 Oct 2026. Its DevForum items are search summaries, so treat them as lower confidence.

| Red flag | Defence |
|---|---|
| "Transfer the group, game or assets first; payment within 14 days." | Never transfer anything. Code goes over only after cleared payment (clause 8). |
| "Paste this into your browser's developer tools" to verify or get access. | Never. It is used to steal session cookies. End the chat. |
| A login link, a "verify" step on a Discord server, or a "moderator" who contacts you first. | Log in only at roblox.com, typed or bookmarked. Copies of the login page can get past 2-step verification. |
| Asks for your password, cookie or 2-step code, or offers theirs. | Refuse. Use Team Create or group roles (clause 9). Compromised groups have had all their funds paid out. |
| Robux "sent" but pending or held, or from a group whose payouts are restricted. | Count Robux only when available (clause 16). Group payouts now arrive as Pending Robux, and extra holds of up to 10 days are reported. |
| Revenue share only, or "I'll pay you when the game earns". | Revenue share only on top of guaranteed USD. Talent Hub users call percentage pay "unreliable and easy to scam through" (note section 2). |
| A job post that looks too good, or a new account with no history. | Check the client and the game before replying. Talent Hub users report scam posts (note section 1). |
| "Pay on completion" with no deposit, or a large unpaid "test task". | Deposit or paid discovery first; offer a small paid test instead. *General caution: the note found no source on free-test scams.* |
| A payment screenshot, a payment from someone else's account, or a push for a payment type chosen to skip fees. | Wait for cleared funds from the client's own account, by an agreed method. Rely on no provider protection you have not checked. *General caution.* |
| A request to install their plugin, model or program. | Read plugin and model code before use. Never run unknown programs. *General caution.* |

## 5. Choices for the owner

The suggestions are my judgment, not market data. The research found no source on deposit sizes (note section 4, gaps).

| Choice | Suggested start |
|---|---|
| Deposit | Discovery and jobs under [SMALL JOB LIMIT, e.g. $200]: 100% upfront. Otherwise as the rate card (`plan/outreach/rate_card.md`): under $1,000, 50% deposit and 50% on acceptance; $1,000 or more, 40% / 30% at a demo / 30% on acceptance |
| Acceptance window | 5 business days (matches the rate card) |
| Revision rounds | 1 for the small fixed offers in `plan/portfolio.md`; 2 per milestone for larger systems |
| Support window | 7 days for the small fixed offers; 14 days for larger systems |
| Kill fee | 25% of milestones not yet started |
| Invoice terms and late fee | Due in 7 days; late fee only as local advice allows |
| Discovery | A few hours, fixed fee, paid first |
| Change rate | The hourly rate on your rate card (task C-004) |
| Robux | USD only by default. If accepted, add a margin for delay, fees and withholding |
| Portfolio | After release, or 6 months after final payment |
| Clients under 18 | Guardian co-signs, or adults only |
| Payment methods and fees | Methods you can receive in your country; client pays sending fees |
| Law and forum | Your own country, after local advice |

## 6. Notes

**Robux figures**, checked 5 Oct 2026 in Roblox's docs:
- Standard DevEx rate: $0.0038 per Earned Robux. So $1 ≈ 263 Robux, and $500 = 131,579 Robux after rounding up ([DevEx doc][devex]).
- Group payouts count as Earned Robux only if the group's funds are bona fide earnings. Cash-out needs 30,000 Earned Robux, with one completed cash-out per calendar month ([DevEx doc][devex]). A small Robux job can take weeks or months to become cash.
- From 1 Nov 2026, DevEx payments are treated as royalties, and US withholding may apply depending on your tax status ([tax doc][tax]; `PLAN.md`). Robux priced at the DevEx rate can then pay less than the same USD price, which is why clause 16 has a margin.

**Payment providers.** This file makes no claim about any provider's buyer or seller protection ([Codex review][review], finding 7). Check the current terms for your country before you name a method.

[note]: ../research_notes/Roblox%20scripter%20income%20strategies/freelance_commission_market.md
[devex]: https://github.com/Roblox/creator-docs/blob/9f840b170b3e472c705e035126b45e3e050daed2/content/en-us/production/monetization/developer-exchange.md
[groups]: https://github.com/Roblox/creator-docs/blob/9f840b170b3e472c705e035126b45e3e050daed2/content/en-us/projects/groups.md
[tax]: https://github.com/Roblox/creator-docs/blob/9f840b170b3e472c705e035126b45e3e050daed2/content/en-us/production/monetization/tax-information.md
[review]: ../reports/Codex%20review%202026-10-05.md
