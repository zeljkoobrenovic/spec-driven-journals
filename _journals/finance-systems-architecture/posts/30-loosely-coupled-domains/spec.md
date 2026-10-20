---
status: accepted
revised: 2026-10-20
---

# Spec: Canonical Events: A Common Language for Money

## Intent

Own the design of the canonical financial event model and the machinery around it. The reader should leave able to specify an event envelope and its semantic rules (facts, not instructions; no accounting or vendor concepts in brand events), version it in step with the close calendar, govern it with an owner, a change board, a schema registry and consumer-driven contract tests, and place the adapter kit, integration hub and anti-corruption layers so that brand releases, vendor upgrades and ledger replacements stay independent while every boundary remains reconcilable. The chapter also argues for keeping the model narrow (finance facts only) against the enterprise canonical model.

## Audience

Chief, enterprise and integration architects, finance-systems architects and platform leaders who design or govern integration between brand platforms, payment providers and ERPs; controllers who need to know what makes such integration trustworthy. They know event-driven architecture; they need the finance-specific rules and governance.

## Success criteria

- [ ] Reader can explain why loose coupling is a control requirement in finance (three clocks: product, vendor, close) and why semantic coupling is the expensive kind.
- [ ] Reader can list the Keystone envelope fields exactly as in the scenario ledger, state the rule for each, and distinguish `event_id`, natural key and `correlation_id`.
- [ ] Reader can apply the seven semantic rules, including "no GL accounts in brand events", and read full `PaymentSettled` and `StayCompleted` examples for the Lisbon booking with amounts in minor units (€600.00, €598.26 net, €1.74 fee, €90.00 commission, €510.00 partner net).
- [ ] Reader can state additive, semantic and breaking change classes, the BACKWARD_TRANSITIVE registry setting, and the close-aligned lifecycle for breaking changes (dual publish, one quarter close in parallel, no cut-over in close windows or year-end).
- [ ] Reader can describe the governance (model owner, event-family business owners, change board in the architecture review, registry, consumer-driven contract tests) and the five adapter-kit components.
- [ ] Reader can separate what the hub may do (validate, enrich with reference keys, count, route, quarantine, replay) from what it must not (accounting, brand rules, lossy aggregation, orchestration).
- [ ] Reader can state Dana's rationalization of Kafka, SAP Integration Suite and MuleSoft, with reasoning and rejected alternatives, and the ACL design at S/4HANA, Fusion, Workday, Adyen and Stripe boundaries.
- [ ] Article has two mermaid diagrams (topology; versioning lifecycle), trade-off tables, failure modes, Chief Architect's view, Questions to ask and Sources and Evidence.

## Non-goals

- Integration styles, outbox basics and the interface inventory ([[integration-architecture]]).
- Posting rules, ledger invariants and the Lisbon entries ([[designing-financial-ledgers]]).
- The coupling taxonomy and capability-overlap register ([[redundancy-and-coupling]]).
- Bounded-context decomposition and context-mapping definitions ([[capability-mapping]]).
- The reconciliation catalog and audit walkthrough ([[traceability-and-reconciliation]]); three-way match ([[payments-to-ledger]]).
- PSP-specific report mechanics ([[adyen]], [[stripe]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The 2027 Q4 Central Finance versus accounting-hub decision may change the S/4 ACL; the chapter treats it as open.
- Legal-entity identifiers (`LE-NL-0031`, `LE-NL-0007`) and group partner IDs are illustrative formats; [[finance-data-architecture]] or [[global-scale]] may later fix a canonical format.
- Whether `tax_jurisdiction` should be nullable for events with no tax consequence is decided here as "inherited from the booking"; [[satellite-platforms]] tax design could revisit.

## Decision log

- **2026-10-18** — Made events carry state (event-carried state transfer) rather than notifications, because ledgers replay history after the source services are retired.
- **2026-10-18** — Reconciled chapter 21's report view (line net €598.36 plus €0.10 batch fee) with chapters 5 and 14 (€1.74 fee, €598.26 settled) by making fee attribution an explicit job of the Adyen ACL.
- **2026-10-18** — Chose a schema-version lifecycle tied to the close calendar over a pure semantic-versioning policy, because the close is the clock that cannot move.
- **2026-10-18** — Rationalized integration technologies by job (Kafka events, Integration Suite SAP boundary, MuleSoft contained) rather than consolidating to one, rejecting both "one iPaaS" and "Kafka everywhere".

## Sources

- **Internal**
  - [[integration-architecture]], [[designing-financial-ledgers]], [[capability-mapping]], [[custom-finance-platforms]], [[adyen]], [[stripe]], [[oracle-fusion]] — terminology, the Lisbon identifiers and amounts, ACL rules.
  - `_research/brief-ea-integration-ledger.md` §1.11, §2; `productscape-digest.md` §1.5, §1.7, §3.3; `brief-payments.md` §2.4, §3.10–3.11; platform briefs for SAP, Oracle and Workday inbound surfaces.
- **External**
  - Evans, DDD Reference; Hohpe and Woolf, Canonical Data Model; Fowler on event-driven patterns and event sourcing; Lewis and Fowler on smart endpoints; Robinson on consumer-driven contracts; Pact; Confluent Schema Registry; CloudEvents; ODCS; vendor docs for Adyen, Stripe, Workday, Oracle and SAP.

## Changelog

- **2026-10-18** — Initial spec and article written in an AI-mediated session.
- **2026-10-18** — Consistency pass: aligned Lisbon settlement/payout dates and chargeback references with the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: added STD-FIN-01/02 IDs and dates (mandatory 1 Apr 2027, enforced 1 Jul 2027 with the registry); American spelling. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Canonical Events and Adapters for Loosely Coupled Financial Domains" to "Canonical Events: A Common Language for Money" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 2 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 7,053 → 7,059 prose words; outline unchanged; lead now links [[redundancy-and-coupling]] and [[traceability-and-reconciliation]] to place the chapter in Part III; about fifteen sentences tightened. *(AI-mediated session)*
- **2026-10-20** — Consistency pass across the book: headings and terms aligned with the style guide and glossary (Setting the Scene at Northmere, From X to Y hand-offs, Trade-offs, Integration with, Total Cost of Ownership, Architecture Advisory Forum, anticorruption, hand-off) and cross-chapter contradictions resolved against the scenario ledger. *(AI-mediated session)*
