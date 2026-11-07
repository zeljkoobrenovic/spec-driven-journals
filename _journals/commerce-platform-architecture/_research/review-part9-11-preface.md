# Editorial review — Parts IX, X, XI and preface pages

Reviewer pass of 2026-11-07 per `_research/REVIEWER-BRIEF.md`. Word counts are body words before `## Sources and Evidence` (brief's awk measure), before → after.

## 37-journey-consumer-order (6,661 → see table at end)

- Timetoread 27 → 29.
- Warehouse and carrier times aligned with chapters 15/16 (owners): last wave 21:00 and PostNL collection 22:30 replace the assumed 20:30 collection; first wave 06:30 (was 07:30); manifest 18:30; out for delivery 07:50 and delivered 11:20 (were 08:40 / 10:52). Resolution: chapter 15's ledger line (warehouse owner) wins over the journey's own "20:30" ledger line.
- Socks net corrected to €29.75 for two pairs (2 × €14.88 summed to €194.22, not the ledger's €194.21).
- Order creation aligned with chapter 11's ledger line: order created with payment *pending*, marked paid by the fetched webhook status; the "webhook never arrives" failure adjusted accordingly.
- Consistency item 2: the Three-Status Order's mechanism now matches chapter 13 (split two-line order collapsed to "fulfilled", ERP waiting for "order complete"), replacing "one message lost" and "daily batch failed".
- Item 1 checked: revenue at delivery (IFRS 15); invoice on dispatch. Item 4 checked: D2C via OMS from 13 October 2027.
- Consistency item 15 (coordinator ruling): Duiven evening timings aligned (last wave 21:00, PostNL 22:30); `[editor-review]` ledger line appended.

## 38-journey-return-and-exchange (7,073 → 6,497)

- Over 7,000: trimmed by cutting restated material (lead, commercetools/Zalando/Loop asides, Odoo quote repeated from Journey 1, refund-timing detail, store-return closing, handoff-table commentary, Double Refund fix restated) and dropped the now-orphaned sources (Zalando, Loop, Coresight, NRF 2024, einvoice.belgium.be). Timetoread 22 → 28.
- WHY IT MATTERS conflated parcels with items ("one for every four items"); rewritten to two sentences before the author's callout removal (moot now).
- Belgian credit note: removed "under the 2026 mandate" (consistency items 5/17 hedge); now "would travel through Peppol like the invoice".
- Checked against ledger: R-20270419-1, 20:40 request, 20 April drop-off, 22 April 10:15 grading, 13:00 wave, delivery 23 April, credit note €164.46 + €34.54, Double Refund (212 / €19,400), Stacking Bug refunds (190 / ~€3,000), 61/27/9/3 dispositions. All agree.

## 39-journey-wholesale-order (6,826 → 6,796)

- ASN Chargeback mechanism aligned with chapter 22 (owner; Part V `[editor-review]` line): the ERP generated the DESADV at release, before packing, with pallet numbers from an ERP number range, while the WMS printed its own labels at pack time; nine Q3 deliveries deducted from an October 2026 remittance. Replaced the "one product group per pallet / revised guideline" version in the prose, the January table, the step table and Figure 3. The Pulled Rug now points at the unowned supplier conditions rather than an unsourced guideline revision.
- Belgian mandate: replaced "a foreign supplier … is not itself obliged" and the meta sentence about "a question for a reviewer" with the item 5/17 hedge.
- Ardennes Trail Co. variant (item 12): left as the Part III reviewer set it (Namur, 40 jackets, €3,800, 21/23 April, due 23 May); matches chapter 14.
- American spelling (center, offenses, mechanized); timetoread 27 → 29.
- Checked: ORDERS 09:12 6 April, 240 units/18 SKUs, €19,860 + €4,170.60 = €24,030.60, three pallets, DESADV 8 April, delivery and INVOIC 9 April, due 9 May; credit limit €450,000/€188,000 open; 12 moss M → 23 available; wholesale revenue at delivery (item 1); EDI via OMS from 8 December 2027 (item 4).

## 40-journey-peak-day (5,936, unchanged within ±30)

- Duiven cut-off aligned with item 15: the last wave is normally released at 21:00 for PostNL's 22:30 collection (was "released after the 22:00 cut-off"); the 22:00 row now reads as the storefront's promise expiring, with Daniel's extra 23:00 collection.
- Removed a contradiction: the closing paragraph said the ERP's "hourly order import still runs during the evening in 2027" while the capacity table (and W5) put the ERP on a daily overnight batch; also removed "that is the next journey" (there is none).
- Checked against the ledger: daily and hourly figures (sum 31,000; Friday 11,500; 20–21h 2,300), queue 500/2,500/4,400, call times 19:50/20:20/20:35/20:50/21:05/21:30/22:40/00:00/02:30, 760 canceled (900 units) + 360 delayed (440 units), €96,000 breakdown (sums), 790/550 split, 160/140 marketplace orders and one bol strike, ten-unit buffer, 2027 plan figures (60/80/120/150/200/300, 15 October go/no-go, freeze 15 November–5 December, eight rungs, 08:00 Saturday report). Item 9: the Stacking Bug is only linked, not quantified. All agree.

## part-9-intro (1,956 → 1,544)

- Trimmed toward the 1,500-word part-intro cap by cutting restatements of the journeys' own numbers (the chapter summaries had repeated each journey's full scenario), shortening KEY POINTS and the "how to read" paragraph.
- Failure patterns cut from four to three (dropped The Message in a Bottle, which KEY POINT 3 already carries).
- ASN Chargeback summary aligned with chapter 22's mechanism (ERP wrote the DESADV before packing); "despatch advice" defined on first use. Timetoread 5 → 7.

## part-10-intro (1,813 → ~1,530)

- Trimmed toward 1,500 by cutting the chapter summaries' repetition of each chapter's case figures; failure patterns cut from four to three (dropped The Lynchpin).
- Item 16: "five of its 34 integrations had no owner" made dated: thirteen without a named owner in January 2027, five still unowned in April.
- Item 13: the composable rebuild is now attributed to the consultancy. Timetoread 5 → 7.

## 41-build-buy-or-assemble (6,397 → ~6,470 after the pitch rewrite; WHY IT MATTERS removed by the coordinator's script)

- Consistency item 13 (ruling 13a): the composable rebuild (~€3.2M, 18 months) is now the outside consultancy's pitch; the agency's pitch is the headless storefront rebuild on the current platform (~€240,000, nine months, linked to chapter 32); the enterprise suite is an option Noor costed herself, not an ERP-partner pitch. The TCO table intro, its suite retainer cell and the W4 decision record's context follow. `[editor-review]` ledger line appended.
- Timetoread 26 → 28.

## 42-replatforming-and-migration (6,302 → ~6,230; only the coordinator's callout removal changed the count)

- Marketplace seam row said OMS order numbers "continue the connector's family with an OMS prefix"; aligned with chapter 13's W2 line (one family continuing the platform's sequence, channel id kept as a reference).
- Checked against the ledger and item 4: 1,900 conflicting variants, DE storefront first PIM consumer in August, NL/BE and connector in September, shadow August, parallel run 1–14 September (1.4%), marketplace 15 September, D2C 13 October, freeze 15 November–5 December, wholesale 8 December, retirement January 2028, 14 of 34 integrations re-pointed, 2026 orders imported as history. All agree.

## 43-commerce-scaling-stages (6,767 → ~6,700; only the callout removal changed the count)

- Internal contradiction fixed: the "Path, Priced" section said "three of the ten incidents descend from" the Growing era while the scene (and the ledger) says eight; now "eight …; the clearest are …".
- "The 2026 incidents cost" included the January 2027 Double Refund; now "incidents of 2026 and January 2027" (total €137,800 ≈ €138,000 checks).
- American spelling (centerpiece, ERP-centered); timetoread 24 → 29.
- Checked: April 2027 stage map, thirteen systems, eight of ten incidents, stage-4 signals deferred to 2029, ledger stage table, store and system dates. Agree.

## 44-organizing-commerce-engineering (6,515 → ~6,430)

- Item 16: dates made explicit. The January 2027 inventory had 13 of 34 integrations without a named owner; the ownership-map tallies are labeled "as it stood in April 2027" (5 still unowned); the "Before (January 2027)" paragraph now says thirteen; Figure 1 label and caption, and the scale-stage judgement ("the thirteen … of January 2027"), follow.
- The Deprecated Endpoint scene aligned with chapter 26's ledger line: 8 February 2027 (Noor's sixth week, not second), discovered via a bol seller-support escalation (not "a wholesale colleague").
- App governance target aligned with item 10 / chapter 31: 34 apps by July 2027, none unused, none writing stock (was "32 apps … illustrative target").
- Timetoread 24 → 28.

## 45-ai-and-agentic-commerce (7,500 → ~6,500)

- Over 7,000: trimmed by cutting duplicated vendor lists (the "one layer down" paragraph, admin-agent roll call, Amazon Auto-Buy and Perplexity details, the Amazon row of the status table, the Visa/Mastercard counts), restated framing (lead's second paragraph, the "builds on" list, the W8 list repeated after the agent test, the Klarna depends-on bullet) and long quotes (SCA exemptions, CERRE, AI Act omnibus detail). Evidence, the agent test, the protocol timeline, the readiness table, the posture table and the scale-stage table are kept. Timetoread 24 → 28.
- Agent-test table: "the copy said yes until about 21:40" contradicted Journey 4 (storefronts zeroed about 20:30, marketplaces about 21:35); fixed. "Three-Status Order was three weeks away" → two weeks (7–14 December).
- W8 table: AI disclosure "delivered by August 2026" by the Buy team, which did not exist until April 2027; now April 2027, with Article 50 applying since 2 August 2026.
- Hand-off now goes to [[part-11]] only (was part-11 and case-shopify). American spelling (US-centered).

## part-11-intro (1,152 → ~1,090; within the 1,500 cap)

- Item 13: the composable rebuild is attributed to "an outside consultancy". No other change needed; opener, chapter list and hand-off correct.

## 46-case-shopify (7,036 → ~6,960 after callout removal; under 7,000, not trimmed)

- Checked format (Where the Evidence Stops before What to Take Away; eight labeled inferences; hand-off to case-amazon) and Kestrel & Pine references (41 apps in January 2027, Deprecated Endpoint, W5/W8). No edits. Timetoread 27 left (expected ~30; small).

## 47-case-amazon (6,508 → ~6,450)

- The ledger's "about 40% of German marketplace units" shipped by a marketplace program had been narrowed to "units sold on Amazon in Germany … shipped by Amazon's program"; restored to the ledger's scope (two places).

## 48-case-zalando (6,492 → ~6,430)

- Checked; no edits needed (Deprecated Endpoint, stock chain and W1/W5/W7 references agree with the ledger).

## 49-case-composable-movement (5,497 → ~5,440)

- Item 13a: "Noor Visser's February 2027 composable pitch" (Noor did not pitch) → "the composable rebuild an outside consultancy pitched to Noor Visser in February 2027 (about €3.2 million over three years)", linked to build-buy-or-assemble.
- Item 6 checked: April ("500+", $100B) and July ("600+", $110B) commercetools figures are cited separately.

## meet-kestrel-and-pine (5,233 → ~5,260)

- Eva's promise made explicit: promised Wednesday, delivered Thursday, a day late because the last wave leaves at 21:00 (matches chapters 01, 15, 16 and item 15).
- American spelling (distribution center, twice); timetoread 15 → 22. Ten incidents, Waypoint table and recurring examples checked against the ledger.

## domain-coverage (5,597 → ~5,530)

- Added the hand-off "Continue with [[toolkit]]" (it listed toolkit, glossary and bibliography without handing off). Timetoread 16 → 24.
- Open issue for the author: the page names the Productscape models and lists their file paths and `_research/productscape-digest.md` in Sources and Evidence. The style guide allows the models as research maps "for the Domain Coverage page only"; the reviewer brief says no citation of a Productscape file. Left as is; the author should decide whether local file paths belong in a published Sources list.

## Spot checks (WebFetch, 2026-11-07)

- Baymard cart abandonment 70.22%, 50 studies, updated 28 October 2026 (journey 37): confirmed.
- Mollie webhooks: 10 attempts over about 26 hours; payload carries only the id, not the status (journey 37): confirmed.

## Final body word counts (before → after; "before" is the count at the start of this pass, before the coordinator removed WHY IT MATTERS)

| Page | Before | After |
| --- | --- | --- |
| part-9-intro | 1,956 | 1,544 |
| 37-journey-consumer-order | 6,661 | 6,666 |
| 38-journey-return-and-exchange | 7,073 | 6,494 |
| 39-journey-wholesale-order | 6,826 | 6,796 |
| 40-journey-peak-day | 5,936 | 5,880 |
| part-10-intro | 1,813 | 1,538 |
| 41-build-buy-or-assemble | 6,478 | 6,483 |
| 42-replatforming-and-migration | 6,302 | 6,225 |
| 43-commerce-scaling-stages | 6,767 | 6,663 |
| 44-organizing-commerce-engineering | 6,515 | 6,442 |
| 45-ai-and-agentic-commerce | 7,500 | 6,498 |
| part-11-intro | 1,152 | 1,089 |
| 46-case-shopify | 7,036 | 6,957 |
| 47-case-amazon | 6,508 | 6,402 |
| 48-case-zalando | 6,492 | 6,384 |
| 49-case-composable-movement | 5,497 | 5,396 |
| meet-kestrel-and-pine | 5,233 | 5,117 |
| domain-coverage | 5,597 | 5,530 |

Build: passes. Render check (18 pages above): all OK.

## Open issues for other parts / the author

- Item 8 (invoice per shipment vs per order) is still OPEN; journey 37's requirements table says "one invoice per shipment". Follow chapter 14's ruling when made.
- Ledger lines superseded by this pass (journey-consumer-order "20:30", journey-wholesale-order ASN mechanism, build-buy-or-assemble pitch attribution) are recorded in one `[editor-review]` line rather than edited.
- Chapter 28's ledger line still says revenue "recognized at shipment" (item 1 says delivery); not in this scope.
- 45: some Sources entries now support claims trimmed from the body (Amazon Auto-Buy, Perplexity, Shopware/Salesforce agent dates); harmless, but the bibliography pass may prune them.
- domain-coverage: Productscape file paths in Sources (see above).
- Spot checks beyond Baymard and Mollie were not run for the cases; their dated figures were checked against the research briefs only.

## where-commerce-platforms-go-wrong (9,403 → 6,481)

- Item 13a: the Giant's Boots paragraph said there were three pitches ("a consultancy's … and the ERP partner's suite, and the agency's proposal … declined all three"). It now has two pitches, the consultancy's composable rebuild (about €3.2M) and the agency's €240,000 headless storefront rebuild, and says she declined both.
- Trimmed from over 7,000 words to 6,481. The cuts removed repetition between the warning-sign table and "What it looks like", shortened "Why it happens" and the remedy lines, kept 3–4 links in "Where this book helps", and shortened the closing sections. All sixteen sections, their quotes, every dated public example and every Kestrel & Pine figure are kept. One cross-reference sentence under The Message in a Bottle was removed; it had no figures. Timetoread 38 → 28.
- Render check: OK.
