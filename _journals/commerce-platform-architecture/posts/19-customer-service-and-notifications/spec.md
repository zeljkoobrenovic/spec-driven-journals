---
status: accepted
revised: 2026-11-07
---

# Spec: Where Is My Order? Notifications, Service and the Customer Record

> Working doc for chapter 19 of *ORDERED: Architecting Commerce Platforms* (Part IV — FULFILLMENT, last chapter). Lives next to `index.md`; the spec drives the post, the post is the artifact.

## Intent

Newcomers see customer service as a department and notifications as e-mail templates. This chapter shows both as the customer-facing read side of the order record: messages triggered by events from the platform, the warehouse and the carrier; a status page and an agent's screen that must read the same status; self-service gated on the goods state; and "where is my order" volume as a measurement of the integrations. The spine is the Three-Status Order, told as the eleven tickets one customer opened in six days and the five tabs the agent used to answer them. After reading, the reader can say which system must emit each message, why the status page and the agent's tool must share a source, and what to measure.

## Audience

Newcomers to commerce architecture. The roles that benefit most: a product manager asked to "reduce support tickets", an engineer wiring notifications to a new warehouse or OMS integration, and a head of customer service deciding between a helpdesk integration and an OMS service view. Readers should leave able to define transactional notification, order status page, service view, read model, WISMO and the separate status machines of an order, and to explain why a single "status" string loses what the customer is asking about.

## Success criteria

- [ ] A reader new to the field can define every term the chapter uses from the chapter alone (WMS, ERP, iPaaS, PSP, OMS, webhook, read model, transactional notification, order status page, service view, WISMO, idempotency key, fulfillment order, Order Defect Rate, restricted data token), with every acronym expanded on first use.
- [ ] The business problem (11 tickets, six days, order #1052877) comes before any component; the ticket table shows what the customer asked and what the agent could see, and the missing message ("two parcels") is identified as the one with no emitter.
- [ ] The notification map names, per message, the event and the emitting system, with dated vendor documentation behind it.
- [ ] The chapter states that money, goods and returns are separate status machines (Shopify and commercetools documentation) and ties the Three-Status Order to that fact without re-teaching the order lifecycle (chapter 13's).
- [ ] Four choices for the service layer are compared in a trade-off table, with the recommendation tied to which system owns the goods state.
- [ ] Self-service actions are gated on the fulfillment state with a state diagram and the Shopify constraints (edit only unfulfilled; cancel becomes a request after acceptance).
- [ ] WISMO is sourced (Gorgias 2023, 18% of tickets, basis stated; Branvas 2026 critique) and reframed as a per-shipped-order measure; a measurement table with labeled assumptions is present.
- [ ] The "Across Scale Stages: When It Fits and When It Limits" table is specific per stage and ends with a judgement; at least two mermaid diagrams, a Kestrel & Pine worked example (Eva's jacket, ledger dates), a "When it goes wrong" section, the three take-away tiers, 6–10 questions and grouped Sources and Evidence are present.
- [ ] Customer identity depth is deferred to [[identity-and-master-data]] with an explicit link; the chapter only shows what the agent cannot see without it.

## Non-goals

- The order state machine, order edits as transactions and the OMS as a product category: [[order-management]].
- Carrier integration, tracking-event vocabularies and the delivery promise: [[shipping-and-delivery]].
- Return policies, dispositions and refund reconciliation: [[returns-and-exchanges]]; this chapter only names the helpdesk as a refund path.
- Customer matching, the golden record and consent: [[identity-and-master-data]] and [[privacy-and-customer-data]].
- Marketplace order import, performance metrics and strikes in full: [[marketplaces-and-channel-integration]]; only the service-side obligations are covered here.
- AI agents in service and agentic commerce: [[ai-and-agentic-commerce]]; W8 is mentioned only as the reason order status by API matters.
- Metric definitions and the data platform: [[commerce-data-and-analytics]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- The only WISMO figure with a stated basis is one vendor's 2023 number; no independent or European study was found. Replace or supplement if one appears.
- The Three-Status Order's mechanism (a two-line order, a partial shipment collapsed into "fulfilled" by the iPaaS flow, the ERP invoicing on "order complete") is this chapter's reconstruction, appended to the ledger. Chapter 13, written in parallel, should be checked for agreement.
- The 2026 service measures for Kestrel & Pine (9 contacts per 100 orders, 3.5 WISMO per 100 shipped orders) are labeled assumptions, not ledger facts; promote them to the ledger only if other chapters need them.

## Decision log

- **2026-11-07** — Chose the eleven tickets as the spine, told as a day-by-day table, rather than a tour of notification channels, because the tickets show the customer's and the agent's views at once and make "two parcels" the missing message.
- **2026-11-07** — Gave the Three-Status Order a concrete mechanism (partial shipment collapsed into one status) and recorded it in the ledger, so that chapters 13 and 19 can share it; a vaguer "the systems disagreed" would not have taught the state-machine point.
- **2026-11-07** — Framed the status page, the notifications and the agent's screen as three read models over one record, and made "which system owns the goods state" the trigger for changing the design, rather than order volume.
- **2026-11-07** — Kept customer identity to one table row, one failure bullet and links, as the contract requires; the Familiar Stranger is chapter 27's.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the Three-Status Order, the Double Refund, Eva's jacket dates, Waypoint W2 and W8.
  - [[order-management]] — the order record and its state machines.
  - [[shipping-and-delivery]] — tracking events and the computed promise.
  - [[returns-and-exchanges]] and [[commerce-payments]] — the return record and the refund path.
  - [[identity-and-master-data]] — the customer record.
  - `_research/brief-inventory-fulfillment-returns.md` (Parts 2, 4 and 6) and `_research/brief-integration-and-data.md` (Parts 2 and 4) — the verified vendor and research facts.
- **External**
  - Shopify help and developer pages (notifications, order status page, order status families, edit orders, fulfillment order), accessed 2026-11.
  - commercetools orders API, accessed 2026-11 — separate state machines.
  - Zendesk Shopify integration, Gorgias, Fluent Commerce, Kibo, Narvar pages, accessed 2026-11 — helpdesk and OMS service views (vendor claims).
  - Gorgias 2023 and Branvas 2026 — WISMO figures and their basis.
  - EasyPost trackers, DPD Belgium Predict — tracking statuses and carrier notifications.
  - Meta WhatsApp Business Platform pricing, accessed 2026-11 — channel economics and dates.
  - bol service standards and Amazon order performance policy (2026) — marketplace service obligations; Amazon Tokens API — personal data access.
  - Directive 2011/83/EU — the withdrawal clocks referenced in return messages.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: WHY IT MATTERS cut to two sentences, Three-Status tickets corrected to three channels, Eva's times aligned with the ledger, WhatsApp pricing claim corrected, OMS/3PL/SP-API expanded. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: ledger-as-document references rephrased. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
