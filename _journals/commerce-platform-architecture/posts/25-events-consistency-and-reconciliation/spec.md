---
status: accepted
revised: 2026-11-07
---

# Spec: Built to Disagree and Recover: Events, Eventual Consistency and Reconciliation

## Intent

Make a reader new to the field able to follow, and ask for, the five mechanisms that keep asynchronously integrated commerce systems from drifting apart for good: idempotency keys, the transactional outbox, retries with backoff and dead-letter queues, sagas with compensation, and reconciliation as a first-class component. The chapter explains eventual consistency and at-least-once delivery in plain words, grounds each mechanism in the vendors' own documentation (Stripe, Shopify, Mollie, Kafka, AWS, Business Central) and the original sources (Vogels, Hohpe, Garcia-Molina and Salem, Richardson, Brooker), and makes reconciliation the spine through Kestrel & Pine's May 2027 stock reconciliation (2.3% of active variants) and the January 2027 Double Refund. After reading, the reader can state a flow's idempotency key, say why a reconciliation card belongs to every flow, and explain Waypoint W5's "idempotent handling and a reconciliation job" and W2's OMS as the order's saga orchestrator.

## Audience

Newcomers to commerce architecture. The integration or back-end engineer who inherits connectors without keys or checks benefits most; the operations, finance or support lead who has lived through a double refund or a stock drift benefits next, because the chapter gives them the questions ("what is the key?", "who gets the exceptions?") to ask in a design review.

## Success criteria

- [x] A reader new to the field can define every term the chapter uses from the chapter alone (copy, system of record, eventual consistency, at-least-once delivery, idempotency and idempotency key, dual-write problem, outbox, relay, exponential backoff and jitter, dead-letter queue, transaction, saga, compensating action, choreography, orchestration, reconciliation, OMS, WMS, PSP); every acronym is expanded on first use.
- [x] Idempotency, the outbox and reconciliation are each explained so a newcomer can follow: a plain definition, a diagram or table, and a Kestrel & Pine example (the twice-delivered order event, the refund path, the stock reconciliation).
- [x] A table of idempotency keys per commerce action and a reconciliation card with fields (sets compared, key, tolerance, cadence, recipient, fix) filled for stock, refunds, orders and payouts.
- [x] A requirements table (window of disagreement, freshness, consistency, availability, mechanisms) for the flows discussed; a trade-off table across the four ways to keep systems in agreement and a choreography vs orchestration table.
- [x] The "Across Scale Stages: When It Fits and When It Limits" section with the four-stage table and a judgement.
- [x] Kestrel & Pine worked examples with ledger numbers: 2.3% of about 17,000 active variants (about 390) with the cause breakdown recorded in the ledger additions; the Double Refund (212 returns, €19,400); W1, W2 and W5 explained, not changed.
- [x] Four mermaid diagrams with captions (duplicate delivery sequence, outbox, place-order saga, reconciliation loop); a "When It Goes Wrong" section covering duplicates, gaps, stale copies, retry storms, partial failures and vendor outages; the three take-away tiers present; 6–10 questions; a closing hand-off to [[api-contracts-and-versioning]]; grouped, dated Sources and Evidence.
- [x] Article at or under 6,500 words including tables.

## Non-goals

- Integration styles, triggers, iPaaS and the integration inventory — [[integration-styles]].
- API contracts, versioning, deprecation and webhook signatures — [[api-contracts-and-versioning]].
- The order state machine, order sourcing and the OMS as a product — [[order-management]]; available-to-promise and reservations — [[inventory-and-availability]].
- Payment flows, PSP status models and payout reports in depth — [[commerce-payments]] and the RECONCILED book ([[traceability-and-reconciliation]]).
- Peak-day capacity, backpressure and circuit breakers in depth — [[peak-load-and-reliability]].
- Customer and product identity matching — [[identity-and-master-data]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The cause breakdown of the 390 variants (240 from three apps, 90 in flight, 40 manual, 20 unexplained) is a new illustrative fact appended to the ledger; the job's cadence (weekly, daily in November) and the removal of the apps' stock-write permission follow the [[inventory-and-availability]] ledger addition.
- The refund-path design (return id as key, one writer, daily refund reconciliation from February 2027) is labeled illustrative; [[returns-and-exchanges]] and [[commerce-payments]] should keep the same shape.
- No public benchmark exists for WMS-to-shop stock disagreement rates; the chapter says so. A reviewer may know of one.

## Decision log

- **2026-11-07** — Made reconciliation the spine (scene, card, diagram, synthesis) rather than idempotency, because the contract's Kestrel & Pine thread is the stock reconciliation and because reconciliation is the mechanism newcomers most often omit; idempotency and the outbox are taught as what reconciliation then verifies.
- **2026-11-07** — Taught the outbox with the honest caveat that a SaaS merchant cannot build or inspect the platform's outbox and that webhook-plus-sweep is its external equivalent, rather than presenting the outbox as something every reader will implement.
- **2026-11-07** — Explained sagas through three named commerce sagas (place order, cancel after shipment, split shipment) and named the OMS as the orchestrator, rejecting a generic microservices treatment, because the reader's decision is whether W2's OMS earns its place.
- **2026-11-07** — Kept monitoring to one paragraph applying the four golden signals per flow, since [[peak-load-and-reliability]] owns observability.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the Double Refund, the stock reconciliation, W1, W2 and W5.
  - [[integration-styles]] — styles, triggers, the inventory and webhook-plus-sweep, which this chapter builds on.
  - [[boundaries-and-systems-of-record]], [[inventory-and-availability]], [[order-management]], [[returns-and-exchanges]] — owning chapters for the terms used briefly here.
  - `_research/brief-integration-and-data.md` Part 2 and `_research/brief-checkout-payments-tax.md` Part 4 — the evidence base.
  - `_research/scenario-ledger.md` — all Kestrel & Pine figures.
- **External**
  - Vogels, "Eventually Consistent" (2008); Hohpe, "Starbucks Does Not Use Two-Phase Commit" (2004) — eventual consistency and the three recoveries.
  - Kafka 4.4 design documentation; CloudEvents 1.0 — at-least-once delivery, ordering per partition, `source` plus `id`.
  - Stripe idempotent requests, webhooks, rate limits and payout reconciliation documentation (accessed 2026-11); Shopify idempotent requests and webhooks (accessed 2026-11); Mollie webhooks (accessed 2026-11).
  - Richardson, Transactional outbox and Saga (microservices.io); Garcia-Molina and Salem, *Sagas* (1987).
  - Brooker, "Exponential Backoff And Jitter" (2015); AWS SQS dead-letter queues documentation.
  - Microsoft Learn, Business Central Shopify Connector inventory sync (2026-10-14); Pattnaik, Walmart inventory on Kafka (Confluent, 2020); Google SRE book, Monitoring Distributed Systems (2017).

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: WHY IT MATTERS no longer claims an unsourced two-month window; Black Friday DLQ sentence aligned with the ledger (no order lost); Double Refund trigger aligned with the payments chapter; apps count per consistency item 10; Walmart 2020 source flagged as old; American spelling. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: scale stages are the book's, not the ledger's. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 4 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
