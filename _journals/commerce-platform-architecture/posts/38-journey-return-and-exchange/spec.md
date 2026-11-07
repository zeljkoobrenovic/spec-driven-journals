---
status: accepted
revised: 2026-11-07
---

# Spec: Journey 2: The Jacket Comes Back

## Intent

Follow the recurring order back: Eva's exchange of the Ridgewalker jacket from size M to size L, as the ledger states it, through Kestrel & Pine's late-2027 target architecture (availability service, OMS with its own return state machine, PIM), as one step table and one sequence diagram, so that each step names the system, the data, the promise, the failure that belongs to that step and the chapter that owns it. The chapter's argument is that a return is three flows (stock, money, books) released by one event (the warehouse's disposition), that the refund has one writer and one key, and that an exchange is a return plus a new order at the frozen price. The refund is the alternative path, the Double Refund of January 2027 is the failure path, and marketplace and store returns are variants. A short section shows how the same return ran on the January 2027 landscape, before Waypoint.

## Audience

Readers new to commerce architecture. The engineer or product manager who has read Part IV and Part III and now needs to see returns, refunds and credit notes as one path benefits most; finance and operations readers get the money-and-books half in plain words. Every term (returns portal, RMA, reverse fulfillment order, disposition, right of withdrawal, idempotency key, credit note, available-to-promise, system of record) is explained in one clause where it first appears.

## Success criteria

- [x] Every ledger fact of Eva's exchange (dates 15, 19 and 22 April 2027, items, prices, reason, "graded resellable", exchange ships 22 April, refund variant €199 by iDEAL booked as a credit note) is stated exactly; times within a day, ids and carrier scans are labeled illustrative.
- [x] The chapter says it is set in the late-2027 target architecture and includes a short "same return in January 2027" comparison.
- [x] A step table with the columns step, system, data, promise made, what could fail here and chapter, covering request, label, carrier, receiving, inspection, disposition, exchange order, refund, credit note, stock, notifications and reconciliation.
- [x] A sequence diagram and one further mermaid diagram, each with a caption that states a point; the sequence diagram shows both the exchange and the refund variant.
- [x] The Double Refund is told with mechanism, detection, recovery and the February 2027 fix; marketplace and store returns are treated as variants with their own first step.
- [x] A requirements table (freshness, consistency, latency, availability) for the handoffs, with illustrative figures labeled as assumptions.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] Every company-specific claim carries a source and a date (Shopify, commercetools, Adyen, Stripe, Mollie, Odoo, Amazon, Zalando, NRF, Coresight, Directive 2011/83/EU); no invented internals.
- [x] The three take-away tiers are present; "When it goes wrong" gives detection and recovery per failure; 6–10 questions to ask; a hand-off to [[journey-wholesale-order]].
- [x] Body at or under 7,000 words including tables (it runs about 6,700, above the 6,500 target; the step table, the two variants and the January comparison are all required).

## Non-goals

- Teaching returns, refunds or credit notes in depth: [[returns-and-exchanges]] owns RMA, disposition, exchange and refund reconciliation; [[commerce-payments]] owns refund mechanics and webhooks; [[tax-invoicing-and-ledger]] owns credit notes and the ledger; [[commerce-regulation]] owns the right of withdrawal; [[stores-and-omnichannel]] and [[marketplaces-and-channel-integration]] own the variants' home systems.
- The forward path ([[journey-consumer-order]]), the wholesale path ([[journey-wholesale-order]]) and the peak day ([[journey-peak-day]]).
- An "Across Scale Stages" section; journeys do not carry one.
- Return fraud models and returns-portal vendor comparison.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The ledger's February 2027 rule makes the returns portal the single refund writer through the platform's API; this chapter has the writer move to the OMS when the OMS takes over return records in Q4 2027, through the same platform API, and records that in the ledger. [[returns-and-exchanges]] (being written in parallel) should use the same reading.
- The Double Refund mechanism follows the ledger line added by [[commerce-payments]] (support refunding by hand after a carrier scan, the portal refunding again on inspection, no key naming the return); the chapter adds nothing to it.
- The return policy (free returns within 14 days of delivery), the exchange as a held order #1072455-X1 created at request time and released by the disposition, and the return id R-20270419-1 follow the ledger line added by [[returns-and-exchanges]]; the delivery of the exchange on 23 April and the credit-note figures are this chapter's additions.

## Decision log

- **2026-11-07** — Made the WMS disposition event the hinge that releases stock, settlement and the credit note, rather than the return request or the carrier scan, because that single ordering is what makes the three flows agree and is the clearest answer to the Boomerang.
- **2026-11-07** — Told the Double Refund with the ledger's mechanism (two writers, no key, no single view) and spent the words on the fix (one writer, one key, read-only console, daily match), since [[commerce-payments]] owns the incident's payment side.
- **2026-11-07** — Treated the exchange as a held order at the frozen price, created at request time and released by the disposition, with a credit note and a new invoice netting to zero, following the returns chapter's held-order model, the pricing chapter's "exchanges copy frozen prices" rule and the ERP's invoice immutability, rather than as an order edit.
- **2026-11-07** — Kept marketplace and store returns as two short variants on the same step table rather than two further walks, to stay within the length cap.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — Eva's exchange, the refund variant, the Double Refund, the returns figures, W1–W5 and the additions by chapter (one refund writer since February 2027, the OMS state machines, the Black Friday stacking refunds, the May 2027 reconciliation).
  - `PLAN.md` — the Part IX contract for chapter 38.
  - `_research/style-guide.md` — page format, evidence discipline, valid permalinks.
  - `_research/brief-inventory-fulfillment-returns.md`, `_research/brief-checkout-payments-tax.md`, `_research/brief-security-privacy-regulation.md` — return data models, refund behavior, credit notes, the 14-day right of withdrawal, marketplace return obligations.
  - [[journey-consumer-order]] and [[meet-kestrel-and-pine]] — the forward path, the invoice figures and the January 2027 landscape.
- **External**
  - Shopify returns documentation; commercetools order states — the return versus reverse-fulfillment-order split, dispositions, return item states.
  - Adyen, Stripe and Mollie refund and idempotency documentation — asynchronous refunds, late failures, duplicate blocking, idempotency keys.
  - Odoo credit-note documentation; FPS Finance Belgium e-invoicing pages; IFRS 15 — invoice immutability, credit notes, revenue reversal.
  - Directive 2011/83/EU — Articles 9, 13, 14 and 16.
  - Amazon seller-fulfilled returns guidance (2025); Zalando partner logistics overview — marketplace return obligations and fees.
  - NRF (2024, 2025) and Coresight (2023) — return rates, fraud share, free-returns preference.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: trimmed under 6,500 words, Belgian mandate hedged, orphaned sources removed. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
