---
status: accepted
revised: 2026-11-07
---

# Spec: Journey 1: Eva's Jacket, From Search to Doorstep

## Intent

Put the book back together for the reader after Parts I–VIII took it apart. The chapter walks the recurring order, #1072455, through every system it touches in Kestrel & Pine's late-2027 target architecture (availability service, OMS as order hub, PIM live), as one step table and one sequence diagram, so that each step names the system that performs it, the data that moves, the promise made, the failure that belongs to that step and the chapter that owns it. After reading, a newcomer can trace any order through any merchant's landscape, point at the handoffs where a message can be lost or duplicated, and say which system is the system of record for each fact on the order. The chapter also shows, in one short section, how the same order ran in January 2027 before Waypoint, so the reader sees what the program bought.

## Audience

Readers new to commerce architecture. The engineer or product manager who has read the capability chapters and now needs to see them as one path benefits most; the chapter is also written to be readable first, as a tour of the vocabulary, for a reader who starts here. Every term (SKU, GTIN, PIM, ATP, OMS, WMS, PSP, iDEAL, webhook, idempotency, fulfillment order, manifest, tracking event, system of record, reconciliation) is explained in one clause where it first appears.

## Success criteria

- [x] Every ledger fact of Eva's jacket (date, time, items, prices, total, payment method, order number, pick date, carrier, delivery date) is stated exactly; times within a day are labeled illustrative.
- [x] The chapter says it is set in the late-2027 target architecture (W1–W3) and that the April order in fact ran on the January landscape; a section compares the two.
- [x] A step table with the columns step, system, data, promise made, what could fail here and chapter, with at least twelve steps from search to the ledger.
- [x] At least one sequence diagram and one further mermaid diagram, each with a caption that states a point.
- [x] A requirements table (freshness, consistency, latency, availability) for the handoffs, with illustrative figures labeled as assumptions.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] Every company-specific claim carries a source and a date; iDEAL, webhook, fulfillment-order, invoice and payout behavior rest on vendor documentation or official pages, not on invented internals.
- [x] The three take-away tiers are present; "When it goes wrong" gives detection and recovery per failure; 6–10 questions to ask; a hand-off to [[journey-return-and-exchange]].
- [x] Body at or under 6,500 words including tables.

## Non-goals

- Teaching any capability in depth: search ([[commerce-search-and-discovery]]), product data ([[product-information]]), availability ([[inventory-and-availability]]), checkout ([[cart-and-checkout]]), payments ([[commerce-payments]]), the OMS ([[order-management]]), the warehouse ([[warehouse-and-fulfillment]]), carriers and the promise ([[shipping-and-delivery]]), notifications ([[customer-service-and-notifications]]), invoicing and the ledger ([[tax-invoicing-and-ledger]]), reconciliation ([[events-consistency-and-reconciliation]]). The chapter names each step's owner and links.
- The return and exchange path ([[journey-return-and-exchange]]), the wholesale path ([[journey-wholesale-order]]) and the peak day ([[journey-peak-day]]).
- An "Across Scale Stages" section; journeys do not carry one.
- Justifying the Waypoint decisions; the chapter uses them as given.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The ledger fixes pick on Wednesday 14 April and delivery on Thursday 15 April for an order placed at 21:14 on Tuesday, before the Dutch storefront's static 22:00 cut-off. The chapter resolves this by having the late-2027 checkout compute the promise from the warehouse's last collection (an illustrative 20:30), so the promise is Thursday and is kept, while the January static rule would have promised Wednesday and missed. [[shipping-and-delivery]] and [[journey-of-an-order]] should use the same reading; the ledger addition records it.
- The chapter assumes the delivery-promise service that W8 names as a prerequisite is live in the target architecture; the ledger gives no date for it.
- The chapter's OMS cut-over detail (D2C orders routed through the OMS from 13 October 2027) comes from the [[replatforming-and-migration]] ledger addition; if that chapter's dates move, this chapter's "late 2027" wording still holds.

## Decision log

- **2026-11-07** — Ran the April order through the late-2027 architecture rather than the January one, as the Part IX contract asks, and kept the January landscape as a short comparison table; the alternative (two full walks) would have doubled the length and taught the second walk twice.
- **2026-11-07** — Made the step table the spine of the chapter and the prose a commentary on its rows, rather than the reverse, so a reader can use the table alone as a checklist against another merchant's landscape.
- **2026-11-07** — Chose iDEAL's instant, capture-less behavior as the payment teaching point rather than the generic card authorization-and-capture story, because the ledger's order pays by iDEAL and the difference (no capture on shipment, refund as a new transfer) is the kind of fact newcomers miss.
- **2026-11-07** — Drew the second diagram as the three financial records of one order (checkout promise, ERP invoice, PSP payout against the bank) rather than a second structural view, because the money path after delivery is the part of the journey the operational chapters cover least.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — Eva's jacket, the systems, W1–W8 and the additions by chapter (OMS cut-over dates, availability buffers).
  - `PLAN.md` — the Part IX contract for chapter 37.
  - `_research/style-guide.md` — page format, callouts, evidence discipline, valid permalinks.
  - `_research/brief-inventory-fulfillment-returns.md`, `_research/brief-checkout-payments-tax.md`, `_research/brief-integration-and-data.md`, `_research/brief-shopify.md` — the verified vendor and regulatory facts cited.
  - [[meet-kestrel-and-pine]] — the systems landscape of January 2027 and the first sketch of Eva's jacket.
- **External**
  - Shopify, commercetools, Stripe, Mollie and Adyen documentation (accessed 2026-11) — inventory states, order and fulfillment-order models, webhooks, idempotency, iDEAL behavior, payouts and reconciliation.
  - Directive 2011/83/EU; Belastingdienst invoice requirements; IFRS 15 — delivery, invoicing and revenue rules.
  - Baymard Institute (2026); DeHoratius and Raman (2008); Gorgias (2023); PostNL Annual Report 2024 — abandonment, record accuracy, WISMO and carrier performance figures.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: Duiven and PostNL times aligned with chapters 15/16 (item 15), socks net corrected, pending-then-paid order creation, Three-Status mechanism per item 2. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
