---
status: accepted
revised: 2026-11-07
---

# Spec: Pick, Pack, Ship: Warehouse Management and Fulfillment

## Intent

Answer contract 15 of PLAN.md for a reader new to commerce architecture: what happens to an order inside the warehouse, and what does the warehouse system need from the rest of the platform? The chapter explains the warehouse steps (receiving, put-away, slotting, waves, picking, packing and cartonization, shipping confirmation, cycle counting) in plain words, then makes three arguments: the **fulfillment order** with its request, accept or reject, in-progress, shipped and cancellation-request handshake is the right contract between the order world and the warehouse; the WMS must be the only writer of on-hand stock and should report changes as events; and cut-off, capacity and the wave schedule are architecture inputs that the delivery promise must read. It covers the four ways to get warehouse execution (ERP module, dedicated WMS, 3PL, marketplace fulfillment program), wholesale fulfillment with SSCC labels and the DESADV generated from pack confirmation, and the failure modes of the warehouse interface. After reading, Noor Visser's stand-in can specify the platform-to-WMS integration and explain why the Queue That Waited broke next-day promises before any picker was late.

## Audience

Readers new to commerce architecture. The engineer or architect who must integrate a platform, an OMS or a 3PL with a warehouse system benefits most; operations leaders who need to understand why "send the order to the WMS" is not a specification benefit next. Assumes general software literacy; defines WMS, 3PL, location, wave, cartonization, cycle count, fulfillment order, on hand, committed, available, webhook, idempotent, reconciliation, system of record, SSCC, DESADV and ASN on first use.

## Success criteria

- [x] Opens with the exact callouts in order (IN THIS CHAPTER, YOU WILL; three KEY POINTS; WHY THE BUSINESS CARES; WHY ARCHITECTS SHOULD CARE; FAILURE PATTERNS with The First Snowfall, Schrödinger's Order and The Phantom Stock), then the lead and the "Where we are in the order's journey" paragraph placing the chapter on Wednesday 14 April at Duiven.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] A step table for warehouse work, a requirements table (freshness, consistency, speed, availability) for the four warehouse flows, a trade-off table for the four execution choices, and the "Across Scale Stages: When It Fits and When It Limits" table with Starting, Growing, Omnichannel and Group.
- [x] Two mermaid diagrams with captions: the warehouse's four interfaces, and the fulfillment-order handshake for Eva's order as a sequence including a rejected cancellation request.
- [x] Kestrel & Pine worked examples with ledger numbers: Duiven (8,500 m², 2023, 88 staff, 336,000 parcels, 9,400 wholesale shipments, 1.9 million units), Eva's jacket (#1072455, 13 April 21:14, picked 14 April, delivered 15 April), the Black Friday queue (2,300 orders in the peak hour, four-hour backlog), the ASN Chargeback (€14,200), Bergzicht's spring reorder (240 units, 18 SKUs, three pallets, 9 April), the May 2027 reconciliation (2.3%), and Waypoint W1, W2, W5 and W6 explained without change.
- [x] Every company-specific claim carries a source and a year; vendor pages are marked n.d., accessed November 2026; the 2008 inventory-accuracy study and the 2019 ZFS source are flagged as older; illustrative figures (wave times, daily volumes, the throttling mechanism, the 8,000 late orders) are labeled assumptions or illustrations.
- [x] "When It Goes Wrong" covers duplicate fulfillment orders, late cancellations, lost confirmations, missing or out-of-order stock events, short picks, SKU mismatch and WMS outage, each with detection and recovery.
- [x] "What to Take Away" has the three tiers; "Questions to Ask" has 10 questions; the closing paragraph hands off to [[shipping-and-delivery]]; Sources and Evidence is grouped and ends with the fictional-merchant line.
- [x] Article under 6,500 words including tables.

## Non-goals

- Available-to-promise, reservations, allocation, safety stock and the availability service as such — [[inventory-and-availability]] owns them; this chapter uses on hand, committed and available only to say what the warehouse writes.
- The order state machine, order splits, sourcing and routing, and the OMS as a product — [[order-management]].
- Carrier selection, labels, manifests, tracking events and the computed delivery promise — [[shipping-and-delivery]]; this chapter only exposes cut-off, capacity and wave schedule as its inputs.
- EDI messages, Peppol, mapping and partner onboarding — [[edi-and-e-invoicing]]; this chapter decides only where the SSCC and the DESADV are generated.
- Returns receiving, grading and dispositions — [[returns-and-exchanges]].
- Store stock, click-and-collect and ship-from-store — [[stores-and-omnichannel]].
- Peak planning, queues and backpressure in general — [[peak-load-and-reliability]] and [[journey-peak-day]]; the chapter shows the Black Friday queue from the warehouse's side only.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The chapter explains the ledger's Eva dates (ordered Tuesday 21:14, picked Wednesday, delivered Thursday, under a "before 22:00, tomorrow" promise) with an assumed 21:00 last wave and 22:30 PostNL collection at Duiven, appended to the ledger. [[journey-consumer-order]] and [[shipping-and-delivery]] should reuse these times rather than invent others.
- The throttling mechanism behind the four-hour queue (several API calls per order against the WMS vendor's rate limit) is labeled illustrative; [[journey-peak-day]] may want to fix the exact numbers.
- Whether the book should name Gartner's warehouse complexity levels more fully; the chapter cites them only as Infios quotes them.

## Decision log

- **2026-11-07** — Made the fulfillment order, not the WMS product landscape, the spine of the chapter, because the newcomer's decision is almost always the integration, not the vendor; Shopify's and Kibo's public models were chosen as evidence because they are the only ones that document the handshake in detail.
- **2026-11-07** — Kept the stock discussion to "one writer per state" and the two propagation patterns, deferring ATP and buffers to chapter 10, to avoid re-teaching the availability service.
- **2026-11-07** — Included wholesale fulfillment (SSCC, DESADV from pack confirmation) here rather than leaving it entirely to chapter 22, because the contract says the chapter owns the WMS and the DESADV's source system is a warehouse decision; the messages themselves stay in chapter 22.
- **2026-11-07** — Explained Eva's Thursday delivery as a promise-versus-warehouse mismatch (assumed 21:00 last wave) rather than leaving the ledger's dates unexplained, so chapter 16 can build its computed-promise argument on it.

## Sources

- **Internal**
  - `PLAN.md` contract 15 and the neighbouring contracts 10, 13, 16, 18 and 22.
  - `_research/scenario-ledger.md` — Duiven, volumes, the Black Friday queue, Eva's jacket, Bergzicht's reorder, the ASN Chargeback, Waypoint W1, W2, W5, W6.
  - `_research/brief-inventory-fulfillment-returns.md` — Parts 1 to 3: stock vocabulary, fulfillment orders, WMS vendors, marketplace fulfillment programs.
  - `_research/brief-b2b-edi-erp.md` — GS1 identifiers, DESADV and SSCC rules, chargebacks.
  - `_research/brief-platform-engineering-scale.md` — backpressure and queues at peak.
  - [[meet-kestrel-and-pine]], [[inventory-and-availability]], [[order-management]], [[shipping-and-delivery]], [[edi-and-e-invoicing]], [[events-consistency-and-reconciliation]].
- **External**
  - Shopify developer documentation (fulfillment services, FulfillmentOrder), n.d., accessed 2026-11 — the handshake and its rules.
  - Kibo fulfillment and routing documentation, n.d., accessed 2026-11 — shipment states, reassignment.
  - Picqer, Odoo, Manhattan, Infios, Blue Yonder product pages, n.d., accessed 2026-11 — warehouse steps, picking methods, segment boundaries, rate limit.
  - Amazon FBA page (n.d.), Zalando ZFS and ZEOS sources (2019, 2023, 2024, 2026) — marketplace fulfillment programs.
  - GS1 General Specifications 26.0 (2026), bol SSCC page (n.d.), Jumbo DC guidelines (2025) and purchasing conditions (2026) — wholesale label and ASN rules.
  - DeHoratius and Raman, *Management Science* (2008) — inventory record inaccuracy.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: WHY IT MATTERS cut to two sentences, Figure 2 framed as the late-2027 OMS design, iDEAL defined, timetoread corrected. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: ledger-as-document references rephrased as Kestrel & Pine facts. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
