---
status: accepted
revised: 2026-11-07
---

# Spec: The Order Record: Lifecycle, State and the Order Management System

> Working doc for the post in this folder. Lives next to `index.md`, versioned
> in git, surfaced as a "View spec" link in the rendered post. The spec drives
> the post; the post is the artifact.

## Intent

Chapter 13 of *ORDERED* (contract 13 in `PLAN.md`) answers: where does the order live once it is placed, what states does it pass through, and when does a merchant need an order management system? The reader should leave knowing what an order record holds, why it carries several state machines (money, goods per shipment, returns) rather than one status, how edits, holds and cancellations interact with those machines, what routing and split shipments decide and need as inputs, how orders from several channels become one record with one number family, and the "two of four" rule for when an OMS is needed. The Three-Status Order is the spine: the chapter explains why three systems held three honest statuses and replays the order through Waypoint W2's bought OMS.

## Audience

Newcomers to commerce architecture. The reader who benefits most is the engineer or product manager who owns, or is about to own, an integration between the commerce platform, a warehouse system and an ERP, and must decide which system is the order's home. Service and operations managers gain the vocabulary to ask why "Delivered" was wrong.

## Success criteria

- [ ] A reader new to the field can define every term the chapter uses from the chapter alone (order record, state machine, fulfillment order, split shipment, sourcing, routing, backorder, hold, compensation, idempotency, order hub, OMS, WMS, ERP, PSP, 3PL, POS, EDI, SKU, system of record), with acronyms expanded on first use.
- [ ] The business problem (11 tickets, six days, €137) comes before any component; every component is tied to a business consequence.
- [ ] The state-machine section cites Shopify's three status families and fulfillment-order statuses and commercetools' order, shipment, payment and return states, dated, and states the two summary rules ("fulfilled is not delivered"; "summary from the least-advanced shipment").
- [ ] Edits, holds and cancellations are tied to the edit window closing at warehouse acceptance, with Shopify's order-editing and fulfillment-order documentation as evidence.
- [ ] Routing and splits are explained with a diagram and with Kibo's, Fluent's, Manhattan's and Adobe's documented rules; the split is framed as a cost decision with named inputs.
- [ ] The OMS component table, a requirements table with labeled assumptions, a sequence diagram of Eva's order under W2, four options with a trade-off table, and the "Across Scale Stages: When It Fits and When It Limits" table with specific content per stage are present.
- [ ] The Kestrel & Pine worked example uses the ledger's W2 rollout dates and costs and the Three-Status Order mechanism recorded by chapter 19 (fleece shipped 7 December, delivered 8 December, socks on replenishment, shipped 14 December).
- [ ] "When it goes wrong" covers duplicates, lost confirmations, collapsed status, out-of-order events, edits after acceptance, cancel after shipment, unowned routing and stuck invoice triggers; the three take-away tiers are present; 8–10 questions; Sources and Evidence with dated entries.

## Non-goals

- The cart and checkout orchestration that produces the order ([[cart-and-checkout]]); payment authorization, capture, refunds and PSP webhooks ([[commerce-payments]]).
- Invoice numbering, tax, credit notes and what the ERP posts ([[tax-invoicing-and-ledger]]); the ERP-as-hub debate in depth ([[erp-and-back-office-integration]]).
- Warehouse execution: waves, picking, the fulfillment-order contract from the warehouse side ([[warehouse-and-fulfillment]]); carrier events and the delivery promise ([[shipping-and-delivery]]).
- Store fulfillment models and the POS ([[stores-and-omnichannel]]); marketplace order import mechanics ([[marketplaces-and-channel-integration]]); wholesale order entry and EDI ([[b2b-commerce]], [[edi-and-e-invoicing]]).
- The returns flow and refund reconciliation ([[returns-and-exchanges]]); notifications and the service tool ([[customer-service-and-notifications]]).
- Idempotency, outbox, sagas and reconciliation design ([[events-consistency-and-reconciliation]]); the migration method for introducing the OMS ([[replatforming-and-migration]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- The "invoice per shipment or per completed order" decision is left open as a finance choice; chapter 14 may fix it for Kestrel & Pine, in which case this chapter's worked example should cite that choice.
- SAP Commerce's current order management and sourcing documentation was not fetched for the brief; only inventory Javadoc (2022) was verified, so SAP is not cited here.
- The illustrative routing rule ("wait up to one working day for replenishment on a two-line D2C order under €150") is new; later chapters should reuse rather than restate it.

## Decision log

- **2026-11-07** — Opened with the Three-Status Order as a table of "status, true of what" rather than with the order data model, so the business problem precedes the vocabulary; rejected opening with the state-machine theory.
- **2026-11-07** — Adopted chapter 19's recorded mechanism for #1052877 (split shipment, agency flow without partial-shipment handling, ERP waiting on "order complete") instead of inventing a second one, so the two chapters agree.
- **2026-11-07** — Framed the hub question as three truths (customer-facing, operational, financial) with three candidate homes, rather than "platform vs OMS", because the ERP-as-hub option is the real alternative for wholesale-heavy merchants and chapter 23 owns the deeper debate.
- **2026-11-07** — Reused the ledger's W2 rollout dates and costs added by the build-buy and replatforming chapters rather than inventing a timeline.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the four order sources, the Three-Status Order, W2.
  - [[customer-service-and-notifications]] — the reconstructed mechanism and dates of #1052877.
  - [[journey-of-an-order]] — cart, order, shipment and invoice distinctions.
  - [[boundaries-and-systems-of-record]] — the three truths of one order as bounded contexts.
  - [[warehouse-and-fulfillment]] — the fulfillment order from the warehouse side.
  - [[replatforming-and-migration]], [[build-buy-or-assemble]] — W2 rollout dates and costs (ledger additions).
  - `_research/brief-inventory-fulfillment-returns.md` (Parts 1.3, 2, 3.2), `_research/brief-integration-and-data.md` (Parts 2.3, 2.8), `_research/brief-shopify.md` (5.4) — the factual base.
- **External**
  - Shopify Help Center and developer documentation (order status; FulfillmentOrder; fulfillment services; edit orders; webhooks) — status families, handshake, edit constraints, duplicate deliveries.
  - Shopify Engineering (2022-01-20) — 13 billion webhooks.
  - commercetools documentation (orders; states) — separate state enumerations; custom state machines.
  - Adobe Commerce documentation (2026-08-20) — sourcing algorithms.
  - Kibo documentation and product pages — routing candidates and suggestions, child shipments.
  - Fluent Commerce documentation and site — split rules; "your ERP stays the system of record".
  - Manhattan Associates and IBM product pages — OMS definitions.
  - Chris Richardson, microservices.io, *Saga* — compensation vocabulary.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: invoice-per-shipment ruling (issues item 18) applied; internal research brief removed from sources; 2022 Shopify figure flagged as historical. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: ledger-as-document reference rephrased. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
