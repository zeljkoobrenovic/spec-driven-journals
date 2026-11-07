---
status: accepted
revised: 2026-11-07
---

# Spec: Follow the Order: What Happens Between "Buy" and "Delivered"

## Intent

Give a reader who has never worked in commerce a complete, concrete picture of what happens to one online order between "buy" and "delivered" and back: the thirteen steps, the systems that touch each one, the promise the merchant makes at each step and which system has to keep it, and the handoffs between systems where the promises are lost. The chapter owns three words the whole book leans on, **the order's journey**, **promise** and **handoff**, and fixes the vocabulary (SKU, cart, order, PSP, webhook, fulfillment order, WMS, shipment, return, invoice, credit note, idempotency, reconciliation, system of record) at first-contact depth. After reading it, the reader can follow any later chapter's worked example, can draw the order's path through their own company's systems, and understands why the book spends its energy on the joins rather than the boxes.

## Audience

Readers new to commerce architecture: engineers, product managers, analysts, consultants and leaders in their first weeks at a merchant, a vendor or an agency. The engineer or product manager who has been handed "the order flow" without a map benefits most, as does anyone who has to answer "where is my order" for a living. No commerce or architecture vocabulary is assumed; every term is explained when it first appears.

## Success criteria

- [x] The thirteen steps (discovery, product page, cart, checkout, payment, order creation, fulfillment, shipping, delivery, service, return, refund or exchange, accounting) appear in one table with what happens, the promise made and who must keep it.
- [x] "Promise" and "handoff" are defined in plain words, and a commerce platform is defined as the whole set of systems that make and keep promises.
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym (SKU, PSP, ERP, WMS, iPaaS, 3PL, SaaS, VAT, IFRS) is expanded on first use.
- [x] Eva's jacket is walked system by system with every ledger fact intact (13 April 2027 21:14, €199 + 2 × €18 = €235, iDEAL, #1072455, picked 14 April, PostNL, delivered 15 April, exchange request 19 April, received and inspected 22 April, exchange ships 22 April; refund variant €199 by iDEAL reversal and a credit note), plus a table of what each system knows at each moment.
- [x] Three mermaid diagrams with captions: the journey as handoffs (flowchart), the goods status line (state diagram), and Eva's jacket across systems (sequence diagram).
- [x] A requirements table (freshness, consistency, speed, availability) for the main handoffs; a "when it goes wrong" table per step with detection and recovery; the four ways a message fails (late, lost, duplicated, misread), each tied to a ledger incident with matching numbers.
- [x] Dated, sourced public evidence for the asynchronous payment handoff (Stripe, commercetools), duplicate and unordered webhooks (Stripe, Mollie), the fulfillment handshake and three status families (Shopify), status enumerations (commercetools), invoice immutability (Odoo) and the three legal promises (Directive 2011/83/EU); no inferred internals of any real company.
- [x] The three take-away tiers are present; 6–10 questions to ask; a short "Across Scale Stages" paragraph (optional in Part I); closes with a hand-off to [[commerce-business-models]]; article at or under 6,500 words including tables.

## Non-goals

- How checkout is orchestrated and protected — [[cart-and-checkout]]; authorization, capture, SCA and refunds in depth — [[commerce-payments]].
- The order state machine, order edits, sourcing and routing, and when an OMS is needed — [[order-management]].
- Available-to-promise, reservations and the oversell problem — [[inventory-and-availability]]; the warehouse's own steps — [[warehouse-and-fulfillment]]; carriers and the computed delivery promise — [[shipping-and-delivery]]; the return data model and dispositions — [[returns-and-exchanges]]; notifications and the service view — [[customer-service-and-notifications]].
- Tax, invoicing and the ledger — [[tax-invoicing-and-ledger]]; integration styles, idempotency and reconciliation in depth — [[integration-styles]] and [[events-consistency-and-reconciliation]]; the system-of-record decision — [[boundaries-and-systems-of-record]].
- The four journeys in full, hour by hour — [[part-9]]; business models and the economics of an order — [[commerce-business-models]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The chapter uses the ledger's canonical mechanism for the Three-Status Order (a two-parcel order and an integration flow without a notion of partial shipment, recorded under "Additions by chapter" by [[customer-service-and-notifications]]); if that entry changes, the "One Order, Three Status Lines" section must follow.
- The exchange flow assumes the exchange order for size L is created at request time and held until the return is inspected; [[returns-and-exchanges]] may prefer "create on inspection". Both match the ledger's dates; the book should pick one.
- The chapter's January 2027 whiteboard scene is a local detail not in the ledger; later chapters may reuse it but need not. "The five tabs" follows the ledger's list (platform order screen, WMS, shipping service, PSP console, returns portal).

## Decision log

- **2026-11-07** — Chose a thirteen-step table with a "promise made / who must keep it" pair per step over a prose walk, because the pair is the chapter's thesis (promises made early by one system, kept late by another) and a table lets a newcomer see it at once.
- **2026-11-07** — Opened with a scene of four people drawing four different orders rather than with an incident, because the chapter's problem is not a failure but the absence of a shared map; the ledger incidents appear later as the four ways a message fails.
- **2026-11-07** — Walked Eva's jacket in the body rather than leaving it to Part IX, because this is the reader's first chapter and the book's vocabulary is easier to fix on one concrete order; the Part IX journeys add the detail each system's chapter supplies.
- **2026-11-07** — Kept the "Across Scale Stages" section as a short paragraph, not the full table, since the steps do not change with scale and the chapter is in Part I where the section is optional; the length cap was the deciding constraint.
- **2026-11-07** — Cut iDEAL, PostNL and returns-rate statistics from the "In practice" section after the first draft exceeded the cap; the owning chapters carry them.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] and `_research/scenario-ledger.md` — Eva's jacket, the systems landscape, the stock sync chain, the Three-Status Order, the Double Refund, the Deprecated Endpoint, the Black Friday Oversell, the May 2027 reconciliation.
  - `PLAN.md` contract 1 — scope, owned terms, neighbours.
  - `_research/brief-checkout-payments-tax.md` — checkout as orchestration, PSP flow, iDEAL, webhooks, idempotency, invoice rules, VAT rate.
  - `_research/brief-inventory-fulfillment-returns.md` — order status models, fulfillment-order handshake, notifications, order status page, WISMO, consumer-law clauses.
  - `_research/brief-commerce-business-models.md` — cart abandonment figures.
- **External**
  - Stripe, *Checkout fulfillment*, *Webhooks*, *Idempotent requests* — asynchronous payment handoff, duplicates, retries.
  - Mollie, *Webhooks*, *iDEAL* — identifier-only webhook, iDEAL properties.
  - commercetools, *Payments lifecycle*, *Orders* — order pending before payment result; separate state enumerations.
  - Shopify, *Order status*, *Build for fulfillment services*, *Customer notifications*, *Understanding order status pages* — three status families, handshake, notifications, tracking.
  - Odoo, *Customer invoices*, *Credit notes and refunds* — invoice numbering and immutability.
  - Directive 2011/83/EU — delivery, withdrawal and refund clauses.
  - business.gov.nl, *VAT rates and exemptions* — 21% Dutch standard rate.
  - Baymard Institute, cart abandonment statistics; Gorgias, WISMO share; IFRS 15.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: added the missing definitions (3PL, theme, marketplace connector, bol), corrected Eva's delivery promise (promised Wednesday under the static 22:00 rule, delivered Thursday, as the ledger records), and noted that the order is created with the payment pending before the iDEAL webhook. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: removed the reference to the book's ledger as a document. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
