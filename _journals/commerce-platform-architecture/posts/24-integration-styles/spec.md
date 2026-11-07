---
status: accepted
revised: 2026-11-07
---

# Spec: APIs, Events, Files and Middleware: How Commerce Systems Talk

## Intent

Give a reader new to commerce architecture the vocabulary and the decision rule for how systems exchange data, so that they can look at any integration in their first week and say what style it is, what it will do when the other side is down, and whether anyone owns it. The chapter names the four integration styles (file, shared database, direct call, message), the five triggers (call, webhook, poll, schedule, change data capture), the three ways to wire a landscape (point to point, hub, vendor connector), and a per-flow choosing rule tied to a requirements table. It ends by establishing the integration inventory as the management tool and defining integration debt operationally. After reading, the reader can explain why Waypoint decision W5 says "stock, orders and prices by events; products by scheduled publication; finance by daily batch" and why every flow needs a named owner.

## Audience

Newcomers to commerce architecture: engineers, product managers, analysts and leaders who have just joined a merchant, vendor or agency. The engineer or engineering lead who inherits an integration landscape they did not build (Noor Visser's position) benefits most; the product manager or operations lead who has to ask "how do we know it worked?" benefits next.

## Success criteria

- [x] A reader new to the field can define every term the chapter uses from the chapter alone (integration, system of record, API, synchronous, asynchronous, queue, broker, webhook, polling, change data capture, iPaaS, event notification vs state transfer, reconciliation job, integration inventory, integration debt); every acronym is expanded on first use.
- [x] The four EIP styles, the five triggers and the three wiring options are each explained with a commerce example a newcomer can picture.
- [x] A requirements table (freshness, consistency, latency, availability) for the six standard flows and a per-flow recommendation table that matches Waypoint W5.
- [x] At least one trade-off table across styles; the "Across Scale Stages: When It Fits and When It Limits" section with the four-stage table and a judgement.
- [x] Kestrel & Pine worked example with ledger numbers: the 34 integrations, Noor's February 2027 inventory, Eva's order flow before and after Waypoint, and an inventory excerpt; all consistent with the ledger and with the additions recorded for this chapter.
- [x] Dated public evidence: Hohpe and Woolf (2003), Fowler (2017), Shopify and Stripe webhook documentation (accessed 2026-11), Business Central Shopify connector (October 2026), Debezium 3.7, iPaaS pricing pages (accessed 2026-11), with evidence-age notes where sources are old.
- [x] Two mermaid diagrams with captions; a "When It Goes Wrong" section; the three take-away tiers present; 6–10 questions; a closing hand-off to [[events-consistency-and-reconciliation]]; Sources and Evidence grouped and dated.
- [x] Article at or under 6,500 words including tables.

## Non-goals

- Idempotency, the outbox, retries, dead-letter queues, sagas and reconciliation as a component — [[events-consistency-and-reconciliation]] owns them; this chapter only names them.
- API contracts, versioning, deprecation and webhook security — [[api-contracts-and-versioning]].
- Which system should be the hub (ERP, OMS or iPaaS) — [[erp-and-back-office-integration]]; the entity–owner table — [[boundaries-and-systems-of-record]].
- Rate limits and peak behaviour of integrations — [[multi-tenancy-and-isolation]] and [[peak-load-and-reliability]].
- App governance inside the platform (the 41 apps) — [[extensibility-and-app-ecosystems]].
- Customer and product identity matching — [[identity-and-master-data]]; the data platform — [[commerce-data-and-analytics]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The breakdown of the 34 integrations by style (9/1/11/13) and by builder (14/9/11), the 13 unowned flows and the 3 reconciliation jobs are new illustrative facts appended to the ledger; other chapters (23, 26, 33) should reuse rather than re-invent them.
- The hourly platform-to-ERP order batch matches the [[erp-and-back-office-integration]] ledger addition (hourly sales-order copy, retired flow by flow in late 2027); if that chapter changes the interval, this one should follow.
- Gartner's iPaaS definition is cited through an encyclopedia entry (2015 retrieval); a reviewer with access to the Gartner glossary may replace it.

## Decision log

- **2026-11-07** — Separated "style" (how data moves: the four EIP styles) from "trigger" (when: call, webhook, poll, schedule, CDC) rather than presenting one flat list of six mechanisms as the brief does, because newcomers confuse "we use webhooks" with "we are event-driven", and the split makes the per-flow rule explainable.
- **2026-11-07** — Made the integration inventory the chapter's spine (scene, worked example, owned concept) rather than the iPaaS, because the inventory is the tool the reader can build in their first month regardless of tooling, and every ledger incident maps to an unowned row.
- **2026-11-07** — Kept iPaaS pricing to one paragraph of dated public price points and a lesson about metering units, rejecting a vendor comparison table, because prices date fast and the comparison is only meaningful per flow volume.
- **2026-11-07** — Folded Fowler's four meanings of "event-driven" into the triggers section as one paragraph, keeping only notification vs state transfer, because event sourcing and CQRS are platform-internal choices outside a merchant's integration decisions.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the 34 integrations, the stock sync chain, the incidents and Waypoint W5.
  - [[boundaries-and-systems-of-record]] — system of record and copies, used as the base vocabulary.
  - [[inventory-and-availability]] — stock events and the oversell window.
  - [[events-consistency-and-reconciliation]], [[api-contracts-and-versioning]] — the two chapters this one hands terms to.
  - `_research/brief-integration-and-data.md` Part 1 — styles, mechanisms, iPaaS, vendor connectors, per-flow table, integration debt.
  - `_research/scenario-ledger.md` — all Kestrel & Pine figures.
- **External**
  - Hohpe and Woolf, *Enterprise Integration Patterns*, Integration Styles (2003) — the four styles and criteria.
  - Fowler, "What do you mean by Event-Driven?" (2017) — notification vs state transfer.
  - Shopify webhooks and HTTPS delivery documentation (accessed 2026-11) — retries, deletion after failures, reconciliation jobs.
  - Stripe webhooks documentation (accessed 2026-11) — three-day retries, ordering, queue-first processing.
  - Microsoft Learn, Business Central Shopify Connector (October 2026) — a vendor connector's ownership model and sync intervals.
  - Debezium 3.7 documentation — change data capture.
  - MuleSoft, Boomi, Workato, Celigo, Make and n8n pricing pages (accessed 2026-11) — metering units and price points.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: Omnichannel stage defined on first use; daily order volume corrected to about 950 (ledger 2026 totals); App That Wrote Stock writer aligned with the ledger. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass (follow-up): 13 unowned integrations dated to January 2027 and the April 2027 figure of 5 added, per consistency item 16. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass (follow-up): the post-Waypoint stock path now states that WMS stock events and availability reach the platform and the connector through the iPaaS, not the ERP. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: tied the four stock-writing flows to six writers of Duiven stock in all (consistency item 22); scale stages are the book's, not the ledger's. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
