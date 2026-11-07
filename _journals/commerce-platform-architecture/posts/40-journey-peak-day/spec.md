---
status: accepted
revised: 2026-11-07
---

# Spec: Journey 4: Black Friday, Hour by Hour

## Intent

Tell Kestrel & Pine's Black Friday week of 2026 as a journey through the same chain the earlier journeys crossed, hour by hour, with what each system did and what each person saw and did, in the order they saw it; then lay out the 2027 plan built from it: the forecast, the capacity table per link, the rebuilt order path through the OMS, the availability service, the eight switches with owners and triggers, the runbook, the rehearsal and the morning-after reconciliation. The reader should finish knowing that the evening was lost in the afternoon by a queue nobody could see, that the sell-out took two hours to reach the channels by design, and that most of the fix is visibility and switches rather than new systems. The chapter applies the ideas of [[peak-load-and-reliability]]; it does not re-teach them.

## Audience

Newcomers to commerce architecture, in particular the engineer or product manager who will be asked to "make sure Black Friday does not happen again" and needs to see what a peak looks like from inside the chain, and the operations or ecommerce lead who will own a row of the runbook. Assumes the vocabulary of the earlier journeys; redefines WMS, ERP, iPaaS, OMS, rate limit, wave, idempotency key, dead-letter queue, stock event, available-to-promise and degradation ladder briefly on first use.

## Success criteria

- [x] The hour-by-hour table and the week table reproduce the ledger's canonical figures (31,000 orders in the week; 2,300 in the peak hour, 38 a minute, 41x traffic; sell-out at 19:40; up to two hours of lag; the four-hour backlog; 1,340 units; 1,120 orders; about €96,000) and label every other figure as illustrative.
- [x] The timeline agrees with the sibling chapters: the order flow throttled by the WMS vendor's rate limit at about seven orders a minute, four hours behind by 21:00, orders placed at 20:00 in the WMS after midnight, roughly 8,000 missed next-day deliveries; the ERP-to-platform push at about 20:30 and the marketplaces at zero at about 21:35; the 790/550 unit split and the 160 marketplace orders with bol's strike; the 20% outerwear promotion at €159.20; the December ten-unit connector buffer.
- [x] Contains a sequence diagram of the 19:40–21:35 window and a flowchart of the 2027 chain, each with a caption that states the point.
- [x] The 2027 plan is consistent with the ledger's cutover dates (marketplace orders through the OMS 15 September, D2C 13 October, freeze 15 November–5 December, wholesale 8 December), the W1 buffers (3 and 1 units), the May 2027 promise service and the June 2027 API-budget analysis.
- [x] The switch table gives eight switches with owner, trigger and effect and names what is never switched off; the runbook has roles, dashboard, cadence, communication and the morning-after reconciliation; the rehearsal section records what the load tests and the game day found.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; the three take-away tiers are present; no "Across Scale Stages" section (a JOURNEYS chapter).
- [x] Length within 4,500–6,000 words including tables.

## Non-goals

- The concepts (peak profiles, capacity planning, backpressure, waiting rooms, degradation, observability, SLOs, the four postures, the scale-stage table) and the public evidence behind them — [[peak-load-and-reliability]].
- Why the copied stock number was the wrong number and how available-to-promise is computed — [[inventory-and-availability]].
- The promotion settings and the stacking bug of the same week — [[commerce-promotions]].
- Waves, cut-offs and warehouse staffing — [[warehouse-and-fulfillment]]; the promise service — [[shipping-and-delivery]].
- The API-budget analysis in detail — [[multi-tenancy-and-isolation]]; the OMS cutover sequence — [[replatforming-and-migration]].
- Marketplace cancellation standards and the strike — [[marketplaces-and-channel-integration]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The daily shape of the week (2,100 / 2,300 / 2,700 / 3,900 / 11,500 / 3,900 / 4,600) and the Friday hourly shape are this chapter's illustrations, appended to the ledger; if another chapter needs a different Friday total, the ledger line should be revised rather than contradicted.
- The cost breakdown of the €96,000 (margin €65,700, vouchers €16,800, penalties €6,500, support and shipping €7,000) is illustrative; a finance-minded reviewer may prefer the lost margin computed on the promotion price excluding VAT, which is what the roughly €73 per unit assumes.
- The 2027 game-day results are written as if the rehearsal has happened by the book's November 2027 vantage; the ledger records them as plan.

## Decision log

- **2026-11-07** — Told the evening in the order the people discovered it (warehouse at 19:50, operations at 20:20, ecommerce at 20:35, integration at 20:50) rather than in the order the problems began (13:00), so the reader feels the absence of a gauge; the "could and could not do" table then maps each gap to a 2027 switch.
- **2026-11-07** — Reconstructed the queue from the ledger's two fixed points (four hours behind at 21:00; 20:00 orders in the WMS after midnight) with a throughput of about seven a minute, which the multi-tenancy chapter's June 2027 analysis also gives, rather than inventing a faster flow that fails earlier.
- **2026-11-07** — Placed the OMS cutover before the peak, following the ledger's replatforming line (D2C orders through the OMS from 13 October), and used the load tests and the game day to justify it; an earlier draft scheduled the cutover after the peak and was corrected.
- **2026-11-07** — Kept the 2027 plan's figures (60 and 80 orders a minute, 120 on the OMS-to-WMS link, buffers of 3, 1 and 25 units, the 08:00 Saturday report) as the plan's own commitments and appended them to the ledger so the chapters on scaling stages and organizing engineering can reuse them.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` and [[meet-kestrel-and-pine]] — the canonical peak figures, Waypoint, cutover dates, buffers and the API-budget analysis.
  - [[peak-load-and-reliability]] — the concepts applied here.
  - [[inventory-and-availability]], [[warehouse-and-fulfillment]], [[marketplaces-and-channel-integration]], [[multi-tenancy-and-isolation]], [[commerce-promotions]], [[shipping-and-delivery]], [[replatforming-and-migration]] — sibling reconstructions this journey must agree with.
  - `_research/brief-platform-engineering-scale.md` (Part 5), `_research/brief-shopify.md` (Part 6), `_research/brief-integration-and-data.md` (Part 2).
- **External**
  - Shopify Engineering, *How we prepare Shopify for BFCM* (2025) — the 150% forecast convention and Game Days.
  - Zalando Engineering, *How Zalando prepares for Cyber Week* (2020) — test orders that fulfillment skips; the Situation Room.
  - AWS, *Exponential backoff and jitter* (2015) — the thundering-herd finding in the October load test.
  - AWS Builders' Library (2019), Amazon SQS documentation (n.d.), Google SRE book (2017), Hodgson (2017), Cloudflare (2021), Stripe rate-limit documentation (n.d.) — as cited in the article.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: cut-off aligned with item 15, ERP batch contradiction removed. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
