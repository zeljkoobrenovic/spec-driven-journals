---
status: accepted
revised: 2026-11-07
---

# Spec: Getting It There: Carriers, Labels, Tracking and the Delivery Promise

## Intent

Answer contract 16 of PLAN.md for a reader new to commerce architecture: how are carriers chosen, labels produced and tracking shown, and how do you make a delivery promise you can keep? The chapter defines the shipping vocabulary (carrier, service, label, manifest, tracking event, pickup point, cut-off, lane, EDD, rate shopping, multi-carrier platform), shows the three moments shipping touches an order (promise at checkout, label at packing, tracking after collection) and makes three arguments: a normalizing layer between the merchant's systems and every carrier is not optional from the second carrier onward; the order's shipping status must be derived from a small normalized event vocabulary that every consumer reads; and the delivery promise must be computed from the warehouse's cut-off and backlog, the stock location, lane transit and a margin for the tail rather than written into the page. It covers delivery options, cross-border customs and IOSS briefly, shipping cost as a lever, the four integration choices and the four promise approaches with trade-offs, and the exceptions (lost, damaged, undeliverable, retired API versions, missed manifests). After reading, Noor Visser's stand-in can answer Milan's request for a delivery date on every storefront with a specification rather than a sentence.

## Audience

Readers new to commerce architecture. The engineer or architect who must connect a warehouse or platform to carriers, or specify a delivery-promise component, benefits most; e-commerce managers who own the storefront's promise text and operations leaders who own carrier contracts benefit next. Assumes general software literacy; defines every shipping term, idempotency, webhook, lane and IOSS on first use.

## Success criteria

- [x] Opens with the exact callouts in order (IN THIS CHAPTER, YOU WILL; three KEY POINTS; WHY THE BUSINESS CARES; WHY ARCHITECTS SHOULD CARE; FAILURE PATTERNS with The Pulled Rug, The Message in a Bottle and The First Snowfall), then the lead and the "Where we are in the order's journey" paragraph placing the chapter between the label on 14 April and the delivery on 15 April.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] A vocabulary table, a requirements table (freshness, consistency, speed, availability) for the six shipping flows, a normalized-event table, two trade-off tables (who talks to the carriers; how the promise is made) and the "Across Scale Stages: When It Fits and When It Limits" table with Starting, Growing, Omnichannel and Group.
- [x] Two mermaid diagrams with captions: the shipping layer around the three moments, and the inputs of a computed promise.
- [x] Kestrel & Pine worked examples with ledger numbers: the four carriers, the static "ordered before 22:00" promise, Eva's parcel (label 14 April, PostNL, delivered 15 April), the Black Friday four-hour queue, the €75 free-shipping threshold and €92 average order, the 40% marketplace-fulfilled German units, and Waypoint W8 explained without change; the 21:00 last wave and 22:30 collection reused from chapter 15.
- [x] Every company-specific claim carries a source and a year: PostNL V4 (2025 rollout), DHL Parcel DE v2 (2.2.0, October 2026; Kleinpaket January 2025; 17:45 close-out), bpost v5 (April 2023), EasyPost statuses, Shopify's five states, PostNL's 97% KPI (2024 report), the ACM letter figures (2025, 2026), Amazon SPEEDY (2025), the conformal-forecasting paper (2025), Directive 2011/83/EU Articles 13(2), 18 and 20, EU customs and IOSS pages; marketing counts and vendor A/B tests are labeled as such; illustrative times and costs are labeled assumptions.
- [x] "When It Goes Wrong" covers retired API versions, duplicate labels, missed manifests, lost or duplicated scans, missing tracking numbers, the promise at peak, undeliverable or lost parcels and marketplace-fulfilled tracking, each with detection and recovery.
- [x] "What to Take Away" has the three tiers; "Questions to Ask" has 10 questions; the closing paragraph hands off to [[stores-and-omnichannel]]; Sources and Evidence is grouped and ends with the fictional-merchant line.
- [x] Article under 6,500 words including tables.

## Non-goals

- Warehouse steps, the fulfillment order, waves, capacity and the wave schedule as such — [[warehouse-and-fulfillment]]; this chapter reads cut-off and backlog as inputs only.
- Checkout orchestration and how delivery options are rendered and priced in the cart — [[cart-and-checkout]].
- Transactional notifications, the order status page and WISMO handling — [[customer-service-and-notifications]]; this chapter only supplies the derived status they read.
- Returns labels, return carriers and reverse logistics — [[returns-and-exchanges]].
- VAT, the One Stop Shop and invoicing for cross-border sales — [[tax-invoicing-and-ledger]]; customs appears here only as data the label call needs.
- Marketplace order import and marketplace-fulfilled tracking — [[marketplaces-and-channel-integration]].
- Click-and-collect, ship-from-store and store delivery — [[stores-and-omnichannel]].
- Peak planning and backpressure in general — [[peak-load-and-reliability]] and [[journey-peak-day]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The chapter's illustrative scan times for Eva's parcel (accepted 23:40 Wednesday, out for delivery 07:50, delivered 11:20 Thursday) and the manifest at 18:30 are labeled illustrative; [[journey-consumer-order]] may fix them canonically.
- The status of the 2026 Council proposal to delete the €150 IOSS threshold was not verified; a reviewer should check before the book is finalized.
- Whether Kestrel & Pine's "first promise service" (transit table plus cut-off and backlog, May 2027) should be recorded in the ledger as a Waypoint sub-decision; the chapter labels it an illustrative plan.

## Decision log

- **2026-11-07** — Built the chapter around the gap in the ledger between Eva's promised Wednesday and delivered Thursday, treating it as the motivating example for a computed promise, rather than around carrier features; the ledger's static-promise note made this the natural spine.
- **2026-11-07** — Adopted EasyPost's ten statuses as the normalized event vocabulary because it is public, small and documented; vendor-neutral wording was kept by presenting it as a reasonable model, not a standard.
- **2026-11-07** — Kept cross-border to one paragraph since Kestrel & Pine ships only within the EU; IOSS and customs are defined so a reader can recognize them, and the VAT side is left to chapter 14.
- **2026-11-07** — Presented the vendor conversion case studies and PostNL's 97% KPI with explicit caveats (vendor-reported; self-reported) rather than omitting them, so the reader learns to read such numbers.

## Sources

- **Internal**
  - `PLAN.md` contract 16 and the neighbouring contracts 11, 15, 17, 18, 19 and 20.
  - `_research/scenario-ledger.md` — carriers, the static promise, Eva's dates, the Black Friday queue, free-shipping threshold, marketplace fulfillment share, Waypoint W8.
  - `_research/brief-inventory-fulfillment-returns.md` — Part 4 (carrier APIs, multi-carrier platforms, delivery promise, cross-border, carrier performance) and Part 6 (status page states).
  - [[warehouse-and-fulfillment]] — the 21:00 last wave and 22:30 collection assumptions; [[meet-kestrel-and-pine]].
- **External**
  - PostNL developer portal and API overview (n.d., accessed 2026-11); PostNL Annual Report 2024 (2025).
  - DHL Parcel DE Shipping API v2 (updated 2026-11-03); DHL Shipment Tracking Unified API (2026); DHL developer portal.
  - bpost Shipping Manager API support page (2026); DPD Belgium Predict documentation (n.d.).
  - Sendcloud (2026-11-06), nShift (n.d.), EasyPost trackers (n.d.), Shopify order status pages (n.d.), Picqer (n.d.).
  - Sarkar and Mandayam Comar, SPEEDY (Amazon Science, 2025); Ye, Hijazi and Van Hentenryck, arXiv 2505.17340 (2025).
  - Directive 2011/83/EU; European Commission customs and One Stop Shop pages; Council document ST-15179-2026.
  - DutchNews reports on ACM figures (2025, 2026); Wonderment and Hive case studies (vendor-reported).

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: WHY IT MATTERS cut to two sentences, wave-release wording and Black Friday slip hedged, ACM expanded, timetoread corrected. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: ledger-as-document reference rephrased. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
