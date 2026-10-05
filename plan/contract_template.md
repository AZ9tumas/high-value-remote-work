# Contract and payment terms template

**Template, not legal advice. Have it reviewed for your country before relying on it.**

Claude, 5 October 2026, for task C-008. A draft for the owner's review. Everything in [BRACKETS] is yours to fill in or choose.

## How to use

- **Full template (part 1):** systems, retainers and any job above [SMALL JOB LIMIT] USD. Attach the spec (Schedule A).
- **One-page version (part 2):** one fix or a small script.
- Fill in every placeholder and delete the options you don't use. Keep your hour estimate private and use it to track your effective rate (`plan/codex_income_execution.md`).
- Name a real person or company as the client. A Roblox group is a platform feature, not a party that can sign.
- If a studio sends its own contract, check it for the same points: deposit, handover after payment, IP on payment, your own tools, portfolio rights, liability cap.
- **Fill in copies outside this repo.** Never commit signed contracts, client names or payment details here.
- **These depend on the country, so get local advice on:** contracts with anyone under 18, on either side; e-signatures and how an IP transfer must be signed; late fees and non-refundable deposits; limits on liability; VAT, GST and tax withholding; data protection if you touch player data; where disputes can be heard.

## 1. Full template

### Development agreement

Date: [DATE] · Project: [PROJECT NAME]

**1. Parties.**
Contractor: [CONTRACTOR], [COUNTRY], [EMAIL], Roblox user ID [ROBLOX ID].
Client: [CLIENT], [COUNTRY], [EMAIL], Roblox user ID [ROBLOX ID], group ID [GROUP ID].
Each party confirms it is 18 or older and able to sign. If the client is under 18, a parent or legal guardian also signs and takes on the client's duties.

**2. Independent contractor.** The contractor is an independent contractor, not an employee, partner or agent of the client. It decides how and when to do the work and uses its own equipment. It may work for others, subject to clause 14. Subcontractors need the client's written consent.

**3. Scope.** The work, deliverables and acceptance checks are in the spec (Schedule A). An acceptance check is a specific, testable result, such as "data saves and reloads after a server shutdown in the test place". Anything not in the spec is excluded. Unless the spec says otherwise, that includes art, building, animation and sound; problems outside the spec; third-party code, plugins and services; publishing, store and ad setup; changes to the live game or live player data. The contractor will not do work that breaks Roblox's Terms of Use or Community Standards. If the spec and these terms conflict, these terms apply unless the spec names the clause it changes.

**4. Price and milestones.**
- Fixed price: [PRICE] USD for the spec, including the revisions in clause 6 and the support in clause 11.
- Deposit: [DEPOSIT %] of the price, due before work starts and counted toward the price. Work starts when the deposit has cleared and the client has given the access in Schedule A.
- Milestones: as in Schedule A. The contractor invoices each milestone when it is accepted, and starts the next one after it is paid.
- Discovery, for unclear scope: a separate milestone of up to [DISCOVERY HOURS] hours for [DISCOVERY FEE] USD, paid before it starts. It delivers written findings, a fix plan and a fixed quote for the rest. The fee is due even if the cause is not found within the cap. The cap rises only with written approval. The client may stop after discovery. If it goes ahead, the quote becomes the price in an updated Schedule A. [Option: the fee counts toward that price.]

**5. Changes.** Change requests must be in writing. The contractor replies with the cost and the effect on dates. Change work starts only after both agree in writing. Agreed changes are added to the spec and billed at [HOURLY RATE] USD per hour or at an agreed fixed price.

**6. Revisions.** Each milestone includes [REVISION ROUNDS] rounds of revisions. A revision adjusts delivered work within the spec, such as tuning values. Fixing a failed acceptance check is not a revision and costs nothing extra. New features are change requests. Extra rounds are billed at [HOURLY RATE].

**7. Timeline and client delays.** Target dates are in Schedule A and run from the start date. They move day for day with any client delay, such as late payment, access, feedback, assets or decisions. If the client does not respond for [SILENCE DAYS] days, the contractor may pause and invoice work done on the current milestone at [HOURLY RATE], up to that milestone's price. If there is still no response [SILENCE DAYS] days after a written reminder, the client is treated as having cancelled under clause 19. The contractor warns the client promptly if a date will slip, with a new date.

**8. Delivery and acceptance.** For each milestone, the contractor sends a delivery note: what was done, how to test it, a demo (video, screen share or playtest) and the result of each acceptance check. The client has [ACCEPTANCE DAYS] days to test against the acceptance checks. It then accepts, or lists the failed checks with steps to reproduce. The contractor fixes them and redelivers, with a new window for the fixed items only. A milestone is deemed accepted if the client does not reply in time, or uses the work in a game open to players. Issues outside the acceptance checks are change requests, not grounds to reject.

**9. Roblox delivery.**
- The contractor works in [a test place or copy owned by the client / a place or repository owned by the contractor]. It does not edit or publish the live game unless the spec says so and the client approves each publish in writing.
- The client keeps full ownership and control of its games, groups, accounts, assets and data. Nothing in this agreement transfers a game, group, account or asset between the parties.
- Before full payment, the contractor shows the work by video, live demo or playtest. Source code, place files, model files and packages are handed over only after the full price has cleared, as [a Rojo repository / an .rbxl or .rbxm file / a package in the client's group].
- If the work is built inside a client-owned place, for example in Team Create, the client can see it before payment. Clause 12 still applies: unpaid work may not be used in a game open to players.
- Assets the game needs, such as images, meshes, audio and animations, are uploaded under the client's account or group. The client uploads them, or the contractor does through a group role limited to that task.
- The client keeps backups of its game and data. Changes that affect saved player data are tested on test data first.

**10. Access and security.**
- Neither party will ask for or share passwords, cookies (including .ROBLOSECURITY), 2-step verification codes or recovery codes.
- Access is given only through roles, at the lowest level that works: Team Create on the test place, a group role with edit access to the test experience only, or repository access. There is no access to group funds, payouts, roles, secrets, API key management or live publishing unless the spec requires it. Any Open Cloud API key is created by the client with the narrowest permissions and an expiry date.
- Neither party will ask the other to paste code into browser developer tools, log in through a link sent in a message, or run unknown programs or plugins.
- Both parties keep 2-step verification on for their Roblox, email and repository accounts. Each reports a suspected compromise to the other at once, and the affected access is paused.
- The client removes the contractor's access at final handover or termination. After the support window, the contractor deletes the client's confidential material, except records it must keep and the materials in clause 13.

**11. Warranty and support.** For [SUPPORT DAYS] days after final acceptance, the contractor fixes at no charge any defect where the delivered work fails an acceptance check in the environment in Schedule A. The client reports defects in writing with steps to reproduce. The contractor responds within [RESPONSE DAYS] business days. Not covered: changes by others, third-party code, Roblox engine, API or policy changes after delivery, use outside the spec, and new features. No system is exploit-proof. The contractor follows the agreed checks and good practice, but does not guarantee that exploits, cheating or data loss cannot happen. Apart from this clause, the work is provided as is, as far as the law allows.

**12. Intellectual property.**
- Until the full price is paid, the contractor owns the deliverables. The client may use them only for testing, not in a game open to players. If the client uses unpaid work in a game open to players, the whole price is due at once.
- On full payment, the contractor assigns to the client all rights in the deliverables made for this project, except Contractor Tools.
- Contractor Tools are code, libraries, frameworks, plugins and know-how the contractor made before or outside this project. The contractor keeps them. The client gets a non-exclusive, perpetual, worldwide, royalty-free licence to use, copy and modify them as part of the deliverables in its games. The licence passes with a game if the client transfers it. The client may not sell or publish Contractor Tools as a standalone product.
- Third-party code listed in Schedule A stays under its own licence, which the client must follow.

**13. Portfolio and credit.** After the work is publicly released [or [PORTFOLIO MONTHS] months after final payment, if sooner], the contractor may show the non-confidential work in its portfolio, case studies and job applications: short videos, screenshots, a description of its role and short code excerpts. It will not show unreleased content, security details, player data or non-public figures. The client grants a non-exclusive licence for these uses. An NDA or the spec can limit or remove this right. [Option: the client credits the contractor as "[CREDIT LINE]" wherever the game lists credits.]

**14. Confidentiality.** Each party keeps the other's non-public information confidential and uses it only for this project. This includes unreleased content, code, data, revenue, player data, access details and the contractor's tools and prices. It does not cover information that is public through no fault of the receiver, that the receiver already had or develops independently, or that the law requires it to disclose, with notice where allowed. Security weaknesses found during the work are reported only to the client. These duties last [CONFIDENTIALITY YEARS] years after this agreement ends, and with no end date for player data and access details. A separate NDA signed by both parties wins where it differs.

**15. Liability.** Each party's total liability under this agreement is capped at the fees the client has paid under it [in the 12 months before the claim]. Neither party is liable for indirect or consequential loss, including lost revenue, Robux, players, data or goodwill. The contractor does not guarantee revenue, CCU, visits, retention, discovery or moderation outcomes. These limits do not apply to the client's duty to pay, to fraud, or to anything the law does not allow to be limited.

**16. Payment.** Invoices are in USD and due [PAYMENT DAYS] days after the invoice date. Accepted methods: [METHODS]. Payments come from the client's own account or the company named in clause 1. [FEE PAYER] pays transfer, processing and currency conversion fees. A payment counts as made when cleared funds reach the contractor. A reversed or charged-back payment counts as unpaid. The client will raise any problem under clause 22 before opening a dispute with a payment provider.

**17. Robux (only if Schedule A accepts Robux).** The Robux price is the USD price divided by the standard DevEx rate on [QUOTE DATE] ([DEVEX RATE] USD per Robux), rounded up, plus [MARGIN %]. It is paid only by a one-time group payout from a group the client controls, to the contractor's Roblox account in clause 1. Passes, items, gift cards and other routes are not accepted. A Robux payment counts as paid only when the Robux are available in the contractor's balance, not pending. The client confirms that the Robux are the group's bona fide earnings and that the payout follows Roblox's rules. If Roblox restricts or reverses a payout, or holds it for more than [HOLD DAYS] days, the client pays the same amount in USD within [PAYMENT DAYS] days. Refunds of Robux payments are made in USD at the quoted rate.

**18. Late payment.** If a payment is late, the contractor may pause work and withhold deliverables until it is paid, and dates move to match. Late amounts carry [LATE FEE], where the law allows. If a payment is more than [LATE DAYS] days late, the contractor may end the agreement, and the cancellation terms in clause 19 apply. Unpaid work stays the contractor's.

**19. Termination and kill fee.**
- The client may cancel at any time by written notice. It then pays for accepted milestones, plus work done on the current milestone at [HOURLY RATE] up to that milestone's price, plus a kill fee of [KILL FEE %] of the price of milestones not yet started. The contractor keeps the deposit and counts it toward these amounts. The same applies if the contractor ends the agreement under clause 7 or 18, or for the client's serious breach.
- Either party may end the agreement for a serious breach that the other does not fix within [CURE DAYS] days of written notice. The contractor may also withdraw with [NOTICE DAYS] days' written notice. If the contractor withdraws, or the client ends the agreement for the contractor's breach, the client pays only for accepted milestones, and the contractor refunds payments for work not delivered, including the unused deposit.
- On ending, the contractor hands over the work that has been paid for, and access is removed under clause 10. Clauses 12 to 18, 20, 22 and 23 continue.

**20. Taxes.** Each party is responsible for its own taxes, registrations and filings. Prices exclude VAT, GST and sales tax, which are added where they apply. If the client must withhold tax from a payment, it tells the contractor before paying and gives proof of the amount withheld. [Option: the client adds the withheld amount so the contractor receives the full invoice.]

**21. Retainer (optional).** [RETAINER FEE] USD a month, paid in advance by day [DUE DAY] of each month, for up to [RETAINER HOURS] hours of the work in Schedule A. Unused hours [expire / roll over for one month]. Extra hours need written approval and are billed at [HOURLY RATE]. The contractor responds to requests within [RESPONSE DAYS] business days. The minimum term is [MINIMUM MONTHS] months; after that, either party may end the retainer with [NOTICE DAYS] days' written notice. Each task is accepted under clause 8, and its code is handed over once that month's fee and any extra hours are paid.

**22. Disputes and governing law.** The parties first try to settle any dispute in good faith for [TALK DAYS] days after written notice. If that fails, the dispute goes to [FORUM]. This agreement is governed by the law of [JURISDICTION]. Either party may seek urgent relief to protect its confidential information or intellectual property.

**23. General.** This agreement, Schedule A and any NDA are the whole agreement. Changes must be agreed in writing. Email, and messages in [CHANNEL] that both parties can keep, count as writing. Neither party may transfer this agreement without the other's written consent. If a clause is unenforceable, the rest still applies. Neither party is responsible for delays caused by events outside its reasonable control, such as Roblox outages. E-signatures and signed copies count as originals.

**Signatures**

| | Contractor | Client | Parent or guardian (client under 18) |
|---|---|---|---|
| Name | | | |
| Title, if a company | | | |
| Signature or e-signature | | | |
| Date | | | |

### Schedule A: spec

| Field | Entry |
|---|---|
| Game and place | [GAME NAME], place ID [PLACE ID] |
| Problem or goal | [FAILING BEHAVIOR or FEATURE] |
| Supported environment | [DEVICES, PLACE, SERVER OR CLIENT] |
| Deliverables | [LIST] |
| Acceptance checks | One per line: [STARTING STATE], [ACTION], [EXPECTED RESULT] |
| Extra exclusions | [LIST] |
| Work location | [TEST PLACE OR COPY OWNED BY CLIENT / CONTRACTOR'S PLACE OR REPOSITORY] |
| Access needed | [TEAM CREATE ON PLACE / EDIT ROLE ON TEST EXPERIENCE / REPOSITORY ROLE] |
| Handover format | [ROJO REPOSITORY / .RBXL OR .RBXM FILE / PACKAGE] |
| Contractor Tools and third-party code | [LIST, WITH LICENCES] |
| Revisions · acceptance · support | [REVISION ROUNDS] rounds · [ACCEPTANCE DAYS] days · [SUPPORT DAYS] days |
| Robux accepted | [NO / YES, UNDER CLAUSE 17] |

Milestones other than discovery add up to the price. The deposit counts toward it.

| Milestone | Deliverable | Acceptance checks | USD | Due |
|---|---|---|---|---|
| Discovery (optional) | Findings, fix plan, quote | Capped at [DISCOVERY HOURS] hours | [DISCOVERY FEE], paid first | [DATE] |
| Deposit | Start of work | | [AMOUNT] | Before start |
| M1 | [DELIVERABLE] | [CHECKS] | [AMOUNT] | [DATE] |
| Final | [DELIVERABLE]; handover after full payment | [CHECKS] | [AMOUNT] | [DATE] |

## 2. One-page version for small jobs

### Small job agreement

For jobs up to [SMALL JOB LIMIT] USD. [CONTRACTOR] ("I") and [CLIENT] ("you"), Roblox user IDs [ROBLOX ID] and [ROBLOX ID], agree on [DATE]:

1. **Job.** [TASK] in [GAME OR PLACE]. Done when: [ACCEPTANCE CHECKS]. Anything else is extra and quoted separately.
2. **Price.** [PRICE] USD, fixed. [DEPOSIT %] before I start, the rest before handover. Method: [METHOD]. [FEE PAYER] pays the fees. Paid means cleared funds in my account. A reversed payment counts as unpaid.
3. **Robux, only if agreed.** [ROBUX PRICE] Robux (the USD price divided by [DEVEX RATE]), by one-time group payout. They count as paid only when available, not pending.
4. **Handover.** I work in a test copy or my own place and show results by video or playtest. I hand over the code as [FORMAT] only after full payment. You keep your game, group and assets; nothing is transferred between us. Assets go under your account or group.
5. **Access.** We never share passwords, cookies (including .ROBLOSECURITY) or 2-step codes. I get Team Create or a limited role on the test place only. You remove my access when we finish.
6. **Checks.** You have [ACCEPTANCE DAYS] days to test against the checks. No reply, or live use, means accepted. [REVISION ROUNDS] revision round(s) included. Fixing a failed check is free.
7. **Support.** For [SUPPORT DAYS] days after acceptance, I fix failed checks for free. I don't guarantee revenue, CCU or retention, or that exploits are impossible.
8. **Rights.** On full payment, you own the code made for this job. I keep my existing tools and give you a non-exclusive, permanent licence to use them in your games. After release, I may show non-confidential parts in my portfolio, unless we sign an NDA.
9. **Confidentiality.** We each keep the other's non-public information private.
10. **Liability.** Each side's liability is capped at the fees paid. Neither is liable for lost revenue, Robux, players or data.
11. **Cancelling.** If you cancel after I start, you pay for work done at [HOURLY RATE], at least [MINIMUM FEE] USD, and I refund any prepayment above that. If I can't finish, I refund what you paid for undelivered work.
12. **Late payment.** I may pause and keep the work until paid. Late fee: [LATE FEE], where the law allows.
13. **Taxes.** Each of us pays our own taxes.
14. **Disputes.** We talk first for [TALK DAYS] days, then [FORUM]. Governing law: [JURISDICTION].
15. **Age.** We are both 18 or older, or your parent or guardian also signs.

Signed or e-signed: [CONTRACTOR], [DATE] · [CLIENT], [DATE] · Parent or guardian, if needed: [NAME], [DATE]

## 3. Before you start

- [ ] **Client checked.** The Roblox account and group are real and match the game. The person owns it or has a role that shows authority. Contact details match across channels.
- [ ] **Age.** The client is 18 or older, or a parent or guardian will sign. The rules differ by country.
- [ ] **Spec agreed:** deliverables, acceptance checks, exclusions, milestones and dates.
- [ ] **Agreement signed** or e-signed by both sides.
- [ ] **Deposit or discovery fee cleared** in your own account. A screenshot is not payment. Robux count only when available, not pending.
- [ ] **Payment method checked.** You have read its current terms for your country: fees, conversion, disputes and chargebacks, whether services and digital goods are covered, and what proof of delivery it needs.
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
| "Transfer the group, game or assets first; payment within 14 days." | Never transfer anything. Code goes over only after cleared payment (clause 9). |
| "Paste this into your browser's developer tools" to verify or get access. | Never. It is used to steal session cookies. End the chat. |
| A login link, a "verify" step on a Discord server, or a "moderator" who contacts you first. | Log in only at roblox.com, typed or bookmarked. Copies of the login page can get past 2-step verification. |
| Asks for your password, cookie or 2-step code, or offers theirs. | Refuse. Use Team Create or group roles (clause 10). Compromised groups have had all their funds paid out. |
| Robux "sent" but pending or held, or from a group whose payouts are restricted. | Count Robux only when available (clause 17). Group payouts now arrive as Pending Robux, and extra holds of up to 10 days are reported. |
| Revenue share only, or "I'll pay you when the game earns". | Revenue share only on top of guaranteed USD. Talent Hub users call percentage pay "unreliable and easy to scam through" (note section 2). |
| A job post that looks too good, or a new account with no history. | Check the client and the game before replying. Talent Hub users report scam posts (note section 1). |
| "Pay on completion" with no deposit, or a large unpaid "test task". | Deposit or paid discovery first; offer a small paid test instead. *General caution: the note found no source on free-test scams.* |
| A payment screenshot, a payment from someone else's account, or a push for a payment type chosen to skip fees. | Wait for cleared funds from the client's own account, by an agreed method. Rely on no provider protection you have not checked. *General caution.* |
| A request to install their plugin, model or program. | Read plugin and model code before use. Never run unknown programs. *General caution.* |

## 5. Choices for the owner

The suggestions are my judgment, not market data. The research found no source on deposit sizes (note section 4, gaps).

| Choice | Suggested start |
|---|---|
| Deposit | 50% for new clients; 100% upfront under [SMALL JOB LIMIT] |
| Acceptance window | 5 business days |
| Revision rounds | 2 per milestone |
| Support window | 14 days |
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
- Group payouts count as Earned Robux only if the group's funds are bona fide earnings. Cash-out needs 30,000 Earned Robux and is limited to one per calendar month ([DevEx doc][devex]). A small Robux job can take weeks or months to become cash.
- From 1 Nov 2026, DevEx payments are treated as royalties, and US withholding may apply depending on your tax status ([tax doc][tax]; `PLAN.md`). Robux priced at the DevEx rate can then pay less than the same USD price, which is why clause 17 has a margin.

**Payment providers.** This file makes no claim about any provider's buyer or seller protection ([Codex review][review], finding 7). Check the current terms for your country before you name a method.

[note]: ../research_notes/Roblox%20scripter%20income%20strategies/freelance_commission_market.md
[devex]: https://github.com/Roblox/creator-docs/blob/9f840b170b3e472c705e035126b45e3e050daed2/content/en-us/production/monetization/developer-exchange.md
[groups]: https://github.com/Roblox/creator-docs/blob/9f840b170b3e472c705e035126b45e3e050daed2/content/en-us/projects/groups.md
[tax]: https://github.com/Roblox/creator-docs/blob/9f840b170b3e472c705e035126b45e3e050daed2/content/en-us/production/monetization/tax-information.md
[review]: ../reports/Codex%20review%202026-10-05.md
