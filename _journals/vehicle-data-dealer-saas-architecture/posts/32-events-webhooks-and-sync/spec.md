---
status: accepted
revised: 2026-10-22
---

# Spec: Keeping Everyone in Step: Events, Webhooks and Synchronization

## Intent

Answer the contract question: which events should a vehicle data and dealer SaaS platform publish, and how do internal services, partners and external systems that cannot receive events stay synchronized? The chapter defines the domain event and separates it from commands, change-data events, flow events and usage events. It sets out a small event catalog with one owner per event type, the CloudEvents envelope with tenant, rooftop, vehicle-key and version attributes, the transactional outbox with a log-tailing relay as the way out of a monolith, entity-keyed partitions with version guards at every consumer, schema compatibility rules, webhooks for partners on the Standard Webhooks contract with retries, disabling and a replayable event feed, thin events for personal and licensed data, and reconciliation jobs for every flow events alone cannot guarantee. It ends with the required table of consistency, latency, freshness and availability per flow. The reader should leave able to design and review an event layer whose delay and loss rate can be stated for every flow.

Owns: **domain event (vehicle)**, **outbox**, **webhook subscription**, **reconciliation job**. Productscape bricks: none; this is a gap chapter **[ADDED]**, plus `vapi` (webhooks roadmap).

## Audience

Chief architects, platform and integration leads, and API product owners at vehicle-data providers, dealer-software vendors, portals and dealer groups. They know Kafka, queues and HTTP APIs. They need the vehicle-specific catalog, the ownership and license rules, and the synchronization picture with portals, DMS products and registers.

## Success criteria

- [ ] Defines domain event, outbox, webhook subscription and reconciliation job, and contrasts domain events with commands, change-data, flow and usage events.
- [ ] Gives an event catalog table with owner, key, payload style, consumers and webhook exposure, and states the inclusion rule.
- [ ] Explains the outbox with Debezium evidence, why dual writes lose events (Axleby's sold audit), and why table-level CDC is a migration tool, not a contract (including SQL Server change tracking's limits for Connect XML).
- [ ] Covers ordering by entity key, entity versions, idempotent consumer inboxes and BACKWARD vs BACKWARD_TRANSITIVE compatibility, with dated sources.
- [ ] Specifies a webhook contract (Standard Webhooks headers, signatures, retries, disabling, replay, SSRF egress) and compares it with Stripe, Autotrader Connect and Marktplaats.
- [ ] Includes the per-flow table of consistency, latency, freshness and availability, with assumptions labeled.
- [ ] Works an Axleby example with numbers (the October 2027 sold audit, sizing, and the Odometer Correction replayed through the backbone) consistent with the ledger.
- [ ] Includes failure handling, trade-off tables, the Across Markets table, the Chief Architect's view, questions and dated sources.

## Non-goals

- Channel adapters, desired-state syndication and delete propagation per portal ([[listing-syndication]]).
- Lead normalization and routing ([[leads-and-crm]]); DMS adapters and commands with receipts ([[dms-integration]]).
- API product design, versioning of synchronous APIs and gateway metering ([[vehicle-data-apis]]); usage events and rating ([[billing-and-metering]]).
- Publish-lag dashboards, flow events and tracing ([[observability-and-data-operations]]); the full correction journey ([[journey-data-correction]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- CDK's 2023 Fortellis asynchronous-API announcement could not be fetched; it is cited as widely reported. Delivery guarantees of Fortellis and Tekion events are not public.
- No public source describes how any automotive company builds its internal event infrastructure; the chapter makes no claims about it.
- Whether the Standard Webhooks specification will be adopted by European portals is unknown.

## Decision log

- **2026-10-22** — Opened with one transition (*stock item sold*) traced through eight consumers and six mechanisms, so the chapter's question is "who knows what, how late" rather than "which broker".
- **2026-10-22** — Kept Connect XML out of the event backbone (change tracking records keys only; sunset in 2029) and used table-level CDC only for migration, to keep event contracts independent of legacy schemas.
- **2026-10-22** — Made lead, deal and fact-correction events thin and stock, price, listing and registration events state-carrying, decided by personal data and license exposure; corrections go only to clients who received the fact, per Charter's access audit, with a `data_correction` credit on re-fetch.
- **2026-10-22** — Recorded the sold audit, the 14 December 2027 design record, the webhook contract and the Odometer Correction client counts in the ledger for reuse.

## Sources

- **Internal**
  - [[inventory-and-vehicle-dossier]], [[dms-integration]], [[deals-and-sales-documents]] — the stock item, Hitch and the reservation.
  - [[observability-and-data-operations]], [[billing-and-metering]], [[tenancy-and-dealer-groups]] — publish lag, Meterline, tenant context.
  - `_research/brief-platform-apis-operations.md`, `_research/brief-syndication-leads.md`, `_research/brief-dms-integration.md`, `_research/brief-identity-registers.md`, `_research/scenario-ledger.md`.
- **External**
  - CloudEvents 1.0 and CNCF graduation (2024); Standard Webhooks; Stripe webhooks.
  - microservices.io transactional outbox; Debezium outbox router and SQL Server connector; Microsoft change tracking docs (2025); Confluent schema evolution.
  - Fowler, "What do you mean by Event-Driven?" (2017).
  - Autotrader Connect, Marktplaats Lead Management API, mobile.de Lead API and Ad Stream, AutoScout24 FAQ, Google Vehicle Listings feed setup (2024).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: registration start aligned with the June 2027 Sales Admin rule (consistency item 25), `vehicle.fact.disputed` added to the catalog (item 33), v2 milestones named, acronyms expanded. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
