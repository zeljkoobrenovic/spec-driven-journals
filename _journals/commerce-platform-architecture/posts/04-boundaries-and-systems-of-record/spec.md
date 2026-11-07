---
status: accepted
revised: 2026-11-07
---

# Spec: Who Owns the Truth: Boundaries, Bounded Contexts and Systems of Record

## Intent

Teach a newcomer the one decision behind most commerce failures: for each business fact that several systems hold (product, price, stock, availability, order, payment, shipment, return, invoice, customer), which system is the record, which are copies, how copies learn, and what happens when they disagree. The chapter defines fact, system of record, copy and writer in plain words; explains bounded contexts with the Three-Status Order so the reader sees that the warehouse's "order" and the ledger's "order" are different objects; delivers the entity–owner table with writer, refresh and reconciliation columns; compares ERP-as-hub, platform-as-hub, per-fact ownership with an order hub, and no decision; shows how ownership shifts across the four scale stages; and works Kestrel & Pine's stock from six writers to one under Waypoint decision W1. The reader should leave able to write the table for their own landscape and to recognize the five Truth patterns as missing owners.

## Audience

Readers new to commerce architecture. The engineer or integration lead who inherits a landscape of connectors benefits most, because the table is the tool they will use first; product managers and finance or operations leaders benefit from seeing why "sync it both ways" makes disagreements unresolvable. The chapter is written at Noor Visser's altitude in the week before Waypoint was approved.

## Success criteria

- [x] Fact, system of record, copy, writer and bounded context are each defined in one plain sentence before use; "single source of truth" is corrected to "one record per fact".
- [x] A table shows "order" in four bounded contexts (storefront, order management, warehouse, ERP) and the Three-Status Order (#1052877, six days, 11 tickets) is explained as three honest contexts with no owner of the cross-context view.
- [x] The entity–owner table has one row per fact with record, who may write, where copies live, how copies learn and how disagreement is found; stock has three records (warehouse, stores, external location) and availability is derived with no human writer.
- [x] A freshness table gives how stale each copy may be and why, tied to ledger incidents (two hours, nine days).
- [x] Four ownership options are explained in a paragraph each with dated public evidence (Microsoft Business Central connector 2026, Shopify ERP guidance 2026, Fluent Commerce and OneStock vendor statements, Salesforce 2026, Walmart 2020 with its age noted) and compared in a trade-off table.
- [x] The five Truth patterns are mapped to the fact without a record, the Kestrel & Pine incident and the Waypoint owner.
- [x] The "Across Scale Stages: When It Fits and When It Limits" table shows ownership per stage with warning signs, and the Kestrel & Pine worked example uses ledger numbers (1,340 units, €96,000, €19,400, 212 returns, 600 variants, 2.3%).
- [x] Three mermaid diagrams (record and copies; three contexts of one order; stock before and after W1), "When it goes wrong" with detection and recovery, the three take-away tiers, questions to ask, and a hand-off to [[commerce-platform-landscape]].
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; under 6,500 words including tables.

## Non-goals

- The capability map itself — [[commerce-capability-map]].
- How copies are kept consistent (events, idempotency, outbox, reconciliation job design) — [[events-consistency-and-reconciliation]]; integration styles — [[integration-styles]].
- Available-to-promise and the availability service's design — [[inventory-and-availability]]; the order state machine and the OMS as a product — [[order-management]].
- Customer matching, golden records and master data management — [[identity-and-master-data]].
- The ERP-as-hub debate in depth and ERP connector mechanics — [[erp-and-back-office-integration]].
- The finance ledger's own system-of-record rules — RECONCILED's [[systems-of-record]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The six-quantity reconstruction for the Ridgewalker variant at 20:00 on 27 November 2026 is labeled illustrative; the ledger addition records it so that [[journey-peak-day]] and [[inventory-and-availability]] can reuse or refine it.
- The entity–owner table names the platform's price lists as the consumer price record; [[pricing-architecture]] may move that to a pricing engine for the omnichannel stage and should update the row here if so.
- Customer identity is left "not yet decided" in the Truth-pattern table because the ledger's Waypoint decisions do not name a customer master; [[identity-and-master-data]] should resolve it.

## Decision log

- **2026-11-07** — Led with "which of the six is right?" rather than with the definition of a system of record, so that the business problem (six honest answers, one oversell) precedes the vocabulary; the definitions follow the scene.
- **2026-11-07** — Used the Three-Status Order, not stock, to teach bounded contexts, because order status is the case where the copies are *all correct* about different objects, which is the point of the concept; stock is used for records and copies, where one value is simply wrong.
- **2026-11-07** — Kept the hub comparison to four options and cited vendors' own boundary statements (Fluent, OneStock, Microsoft) rather than inferring any vendor's internals; vendor interest is noted in the text.
- **2026-11-07** — Included the "Across Scale Stages" section although it is optional in Part I, because the chapter's third key point is that ownership changes with scale and the table is where that is shown.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — incidents, W1–W3, W5, the stock sync chain, the May 2027 reconciliation.
  - `_research/brief-integration-and-data.md` — Business Central connector ownership statements, Walmart partitioning, reconciliation and master-data material.
  - `_research/brief-b2b-edi-erp.md` — the ERP/commerce/OMS hub comparison, Shopify ERP guidance, OneStock and Business Central customer ownership.
  - `_research/brief-platform-landscape.md` — Salesforce 2026 release, Fluent Commerce.
  - `_research/brief-inventory-fulfillment-returns.md` — availability as a derived value.
  - [[commerce-capability-map]], [[meet-kestrel-and-pine]], [[where-commerce-platforms-go-wrong]] — neighbors.
- **External**
  - Microsoft Learn, Business Central Shopify Connector pages (2026-09-22 to 2026-10-16); Shopify, "ERP integration" (updated 2026-08-28); Fluent Commerce and OneStock product pages (accessed 2026-11); Salesforce press release (2026-07-06); Confluent blog, Walmart inventory (2020-05-04); Eric Evans, *Domain-Driven Design* (2003); Martin Fowler, "BoundedContext" (2014-01-15, verified by fetch 2026-11).

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: corrected the Three-Status Order mechanism to the ledger (second line waiting on replenishment; ERP invoices on the WMS's order-complete message), made wholesale prices move by price events (ruling 3), and replaced a paraphrased Walmart quote with the source's verified wording. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: ledger-as-document references rephrased as Kestrel & Pine facts. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
