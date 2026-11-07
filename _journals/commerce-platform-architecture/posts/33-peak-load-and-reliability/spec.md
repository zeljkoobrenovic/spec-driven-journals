---
status: accepted
revised: 2026-11-07
---

# Spec: Black Friday Every Year: Peak Load, Resilience and Recovery

## Intent

Teach a reader new to commerce architecture how a peak day breaks a commerce chain and how to prepare for it: why a hosted platform's peak is not the merchant's peak (multi-tenant smoothing versus a single merchant's 40x spike), why the integrations rather than the storefront are the bottleneck, how to size and test the whole chain in one unit (orders per minute), how queues, backpressure, caching, waiting rooms and a written switch-off order protect the money path, how to observe the day in business units and staff a situation room, and why recovery after a peak is reconciliation. The chapter owns the peak plan, graceful degradation, backpressure and the load test; it summarizes Kestrel & Pine's 2026 peak and 2027 plan and leaves the hour-by-hour narrative and the full runbook to [[journey-peak-day]].

## Audience

Newcomers to commerce architecture. The engineer or engineering lead who inherits a working but untested integration landscape (Noor Visser's position) benefits most; the ecommerce manager who owns the promotion calendar and the operations lead who owns the warehouse's peak roster should be able to read it and recognize their part of the plan. Assumes no prior knowledge of WMS, ERP, PSP, iPaaS, CDN, rate limits, queues, idempotency, dead-letter queues, feature switches or SLOs; each is defined on first use.

## Success criteria

- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym (WMS, ERP, PSP, iPaaS, CDN, ATP, OMS, SLO, 3PL) is expanded on first use.
- [x] The business problem comes first (31,000 orders, €96,000, 1,120 broken promises) and every mechanism is tied to a business consequence.
- [x] The chapter states and evidences the central claim that a platform's peak-to-average ratio is about two while the merchant's was about seventy, using Shopify's 2025 figures with their caveats and the ledger's figures.
- [x] Dated public evidence with definitions: Shopify BFCM 2023–2025 (sales per minute, edge and app-server requests, unaudited), Shopify readiness 2023 and 2025, Zalando 2019 and 2020, Alibaba 2020, Adobe 2024, the 2018 Shopify changelog and the 2018 Prime Day account, each with its age flagged where older than three years.
- [x] Contains a requirements table per flow, a trade-off table of four postures, the "Across Scale Stages: When It Fits and When It Limits" table with a judgement, two mermaid diagrams (the 2026 chain with capacities; the degradation ladder), a "When it goes wrong" table, the three take-away tiers, Questions to Ask and grouped Sources.
- [x] Kestrel & Pine figures match the ledger and the sibling chapters: 31,000 orders, 2,300 in the peak hour, 41x traffic, 19:40 sell-out, two-hour lag, four-hour backlog, 1,340 units, 1,120 orders, €96,000; the order flow throttled by the WMS vendor's rate limit at about seven orders a minute; the 2027 plan consistent with the OMS cutover dates and the 15 November–5 December freeze in the ledger.
- [x] Length at or under about 6,500 words including tables.

## Non-goals

- The hour-by-hour narrative of 23–29 November 2026, the switch table with owners and triggers, the runbook and the rehearsal — [[journey-peak-day]].
- Available-to-promise, reservations, buffers and the availability service — [[inventory-and-availability]].
- Rate limits as a tenancy tool, the API-budget analysis and pods — [[multi-tenancy-and-isolation]].
- Idempotency keys, outbox, dead-letter mechanics, retries with jitter and the reconciliation card — [[events-consistency-and-reconciliation]].
- Waves, cut-offs and warehouse capacity — [[warehouse-and-fulfillment]]; the computed delivery promise — [[shipping-and-delivery]].
- Storefront caching and edge delivery in depth — [[storefront-architecture]]; checkout's internal protection and payment flows — [[cart-and-checkout]], [[commerce-payments]].
- Card testing and bot traffic at peak — [[commerce-security]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The chapter cites Shopify's 2018 changelog for decoupling payment from order creation and notes that the present-day checkout throttle is undocumented; if Shopify publishes a first-party description, the paragraph should be updated and dated.
- The degradation ladder's order is the author's judgement; a reviewer may want a marketplace-first seller's variant shown explicitly rather than only in the take-aways.
- Sibling chapters give two illustrative splits of the oversell (about 790/550 units storefront/marketplace in `inventory-and-availability`; about 160 marketplace orders in `marketplaces-and-channel-integration`); they are not contradictory but a reviewer should check that no chapter implies units per order from them.

## Decision log

- **2026-11-07** — Framed the chapter around "the platform's peak is not the merchant's peak" rather than around platform scaling, because the reader is a merchant-side newcomer and the contract's evidence (Shopify's 4:1 edge ratio and 2x peak-to-average) supports it; platform-owner practices are marked as belonging to the fourth posture and the Group stage.
- **2026-11-07** — Chose orders per minute as the single unit throughout (tables, SLOs, dashboard, forecast), following the brief's observation that every large operator reports its peak in a business unit, and rejected requests per second because the merchant's bottleneck links (WMS, ERP, carriers) cannot be measured in it.
- **2026-11-07** — Summarized Kestrel & Pine's 2026 evening in one section and moved the timeline, the sequence diagram, the switch table and the runbook to Journey 4, so the two chapters do not duplicate; this chapter keeps the ideas and the plan's spine.
- **2026-11-07** — Cut the chapter from about 7,900 to about 6,600 words by collapsing the four postures into one paragraph plus a table, replacing the golden-signals table with prose and removing a separate "public record, dated" list that duplicated inline citations.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]], `_research/scenario-ledger.md` — the 2026 peak figures, the Waypoint decisions, the 2027 cutover dates and the freeze.
  - [[journey-peak-day]] — the hour-by-hour narrative and the full 2027 plan this chapter summarizes.
  - [[inventory-and-availability]], [[warehouse-and-fulfillment]], [[marketplaces-and-channel-integration]], [[multi-tenancy-and-isolation]] — the sibling reconstructions of the oversell and the queue that this chapter must agree with.
  - `_research/brief-platform-engineering-scale.md` (Part 5), `_research/brief-shopify.md` (Part 6), `_research/brief-integration-and-data.md` (Part 2) — the verified evidence base.
- **External**
  - Shopify, BFCM 2023–2025 news and press releases — peak figures with definitions and caveats.
  - Shopify Engineering, *How we prepare Shopify for BFCM* (2025) and *Scale and performance testing* (2023) — the readiness program.
  - Zalando Engineering, *End-to-end load testing* (2019) and *How Zalando prepares for Cyber Week* (2020) — production load tests, test orders, the Situation Room.
  - AWS Builders' Library, *Using load shedding to avoid overload* (2019) — goodput and backpressure.
  - Pete Hodgson, *Feature Toggles* (2017) — ops toggles.
  - Cloudflare (2021), Queue-it (n.d.) — waiting rooms.
  - CNBC, *Amazon Prime Day 2018* (2018) — degradation under fire.
  - Google SRE book (2017) — SLOs and the four golden signals.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: aligned the availability-service fallback with the ledger (ten-unit marketplace buffer), relabeled the 8,000-order figure as a ledger figure, removed the invented predecessor, expanded SRE, SLA, OMS, D2C, EDI, timetoread. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: ledger-as-document reference rephrased. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
