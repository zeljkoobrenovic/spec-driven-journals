---
status: accepted
revised: 2026-10-20
---

# Spec: Files, Events and APIs: How Finance Systems Talk

## Intent

Make this the book's authoritative chapter on how financial data should move between systems. The reader should leave able to choose an integration style by the finance use case, and to specify what any interface that carries money must guarantee: completeness, accuracy, an exactly-once *effect*, bounded ordering, cut-off and period assignment, control totals and batch manifests, safe replay and backfill, behavior under month-end load, a clean separation of dead letters from suspense accounts, and observability of money in flight. The spine is a Northmere incident: a retried SFP-to-S/4HANA daily posting that put 31 January into the ledger one and a half times. The chapter then redesigns that interface with a manifest, an idempotency gate and superseding runs. It argues that middleware delivers messages, while idempotency, control totals and reconciliation deliver correctness.

## Audience

Chief, enterprise and integration architects, and finance-systems and platform engineering leaders, who own or approve interfaces into ERPs, subledgers, PSPs and close tools. Secondary: controllers and internal-controls leads who need a shared vocabulary with integration teams.

## Success criteria

- [x] Defines the five integration styles and gives a decision table for at least eight finance use cases, with Northmere's 1,100 interfaces classified by style.
- [x] States the ten finance requirements, each with a design rule; ordering limits cite Kafka's per-partition guarantee and Stripe's and Adyen's documented behavior.
- [x] Distinguishes dead letters from suspense accounts in a table and a diagram, and links the confusion to The Suspense Swamp.
- [x] Explains why exactly-once is an effect (Kafka EOS scope, Debezium at-least-once), with idempotency keys derived from business identity and a transactional outbox plus idempotent consumer sequence diagram.
- [x] Compares iPaaS, ESB, event backbone and code by ownership, fit and finance risk, and records Northmere's lane decision for its three integration technologies.
- [x] Gives a vendor-surface table for SAP, Oracle, Workday, Adyen and Stripe using only documented facts and limits.
- [x] Introduces the canonical event envelope with the Lisbon capture and hands depth to [[loosely-coupled-domains]].
- [x] Works the SFP-to-S/4HANA redesign with manifest numbers consistent with [[custom-finance-platforms]] (12 March 2027: 2,114,880 events, 3,061,442 detail lines, 38,210 summary lines) and covers governance, failure modes, the Chief Architect's view, questions and sources.

## Non-goals

- Canonical event model in depth, adapter kit, schema registry and contract testing: [[loosely-coupled-domains]].
- Reconciliation catalog and audit walkthrough: [[traceability-and-reconciliation]].
- PSP clearing-account design and the €14m suspense remediation: [[payments-to-ledger]].
- Ledger internals (posting rules, immutability): [[designing-financial-ledgers]].
- Platform-specific integration detail: [[sap-s4hana]], [[oracle-fusion]], [[workday]], [[adyen]], [[stripe]].
- Multi-entity, multi-currency and multi-time-zone design: [[global-scale]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- SAP's duplicate-check and timeout statements are cited from SAP KBA previews (2817042, 2830584); the full KBA text requires an SAP login. Re-check before manuscript lock.
- MuleSoft's API-led connectivity page returned HTTP 403; the three-layer description is phrased as widely cited, not linked.
- The 500-line document chunk size is a Northmere design choice, not an SAP limit; keep it labeled as such.
- Oracle's 26A extraction tool name and coverage are still moving; the vendor table mentions it only briefly.

## Decision log

- **2026-10-18** — Opened with a concrete double-posting incident rather than a styles survey, so that every later requirement answers a failure the reader has just seen.
- **2026-10-18** — Made "dead letter vs suspense account" a stand-alone section with its own diagram, because it is the point where integration design and accounting meet, and it is often missed.
- **2026-10-18** — Recommended a lane model for Northmere's three integration technologies (event lane, ERP/SaaS lane, contained legacy lane, domain adapters) instead of picking one platform, because MuleSoft retirement is tied to the 2029 ledger convergence.
- **2026-10-18** — Accepted about 8,700 words including tables (~6,500 prose) because the contract owns four terms and includes a five-vendor comparison table.

## Sources

- **Internal**
  - `_research/brief-ea-integration-ledger.md` §2 and §3.5–3.7 — EIP, outbox, Debezium, Kafka EOS scope, idempotency keys, Hohpe on 2PC.
  - `_research/brief-sap.md` §4, `brief-oracle.md` §4, `brief-workday.md` §5, `brief-payments.md` §2.4 and §3.10–3.11 — vendor surfaces and limits.
  - `_research/productscape-digest.md` §1.5 and §3.3 — integration hub, delivery ledger and control totals, canonical events and file interfaces.
  - [[custom-finance-platforms]], [[finance-data-architecture]], [[adyen]], [[stripe]] — SFP summary controls, posting contract, webhook consumers.
- **External**
  - SAP KBAs 2817042 and 2830584 — no duplicate check in Journal Entry Post APIs; asynchronous API for large postings.
  - Apache Kafka introduction — per-partition ordering.
  - Hohpe and Woolf, *Enterprise Integration Patterns* — Idempotent Receiver, Dead Letter Channel.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: canonical-event approval date and STD-FIN-02 reference added, MuleSoft retirement aligned with convergence, acronyms expanded, unverified SAP naming claim softened. *(AI-mediated session)*
- **2026-10-18** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Integration Architecture for Finance" to "Files, Events and APIs: How Finance Systems Talk" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 4 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,999 → 7,005 prose words; opening now ties the chapter to [[controls-and-auditability]]; teaser first sentences replaced with claims; long platform-options sentence split; CDC point given its own paragraph; no headings renamed and no sections moved; spec otherwise unchanged. *(AI-mediated session)*
- **2026-10-20** — Consistency pass across the book: headings and terms aligned with the style guide and glossary (Setting the Scene at Northmere, From X to Y hand-offs, Trade-offs, Integration with, Total Cost of Ownership, Architecture Advisory Forum, anticorruption, hand-off) and cross-chapter contradictions resolved against the scenario ledger. *(AI-mediated session)*
