---
status: accepted
revised: 2026-10-18
---

# Spec: Designing Custom Ledgers and Financial Event Processing

## Intent

Show, with code-level precision, how to build a custom subledger and the financial event pipeline that feeds it so that accountants and auditors can trust it. The chapter separates financial events from accounting entries, treats posting rules as versioned and approved configuration, enforces ledger invariants in the write path, and designs summarization, reconciliation, testing and time handling as part of the system. After reading it, an architect can review a subledger design against a concrete list of invariants and evidence, and can decide when an ERP accounting hub or a ledger product is the better choice.

## Audience

Chief Architects, solution and finance-systems architects, and engineering leads who own or will build a high-volume subledger (payouts, customer funds, marketplace settlement). They know databases and event streaming; they need the accounting and control consequences made concrete.

## Success criteria

- [x] Defines financial event, accounting entry, posting rule, accounting engine and ledger invariants, citing Fowler's Posting Rule from the *Analysis Patterns* supplement (not the eaaDev page).
- [x] Gives a worked rule table for the Lisbon booking events (BookingConfirmed through ChargebackReceived) with amounts matching the scenario ledger and stated simplifications; account names, revenue timing and the chargeback treatment agree with [[accounting-for-architects]].
- [x] Covers idempotency (transport, semantic, posting duplicates), money in minor units with rounding and allocation, multi-currency entries with an FX worked example, balances and hot accounts, bi-temporality and late events into closed periods, corrections by reversal.
- [x] Designs summarization to the GL with a durable drill-back key and control totals, and a daily subledger-to-GL tie-out.
- [x] Covers testing (property-based invariants, production replay, shadow posting), scaling, retention and business observability.
- [x] Includes at least three mermaid diagrams: pipeline architecture, event-to-entry sequence, period-state machine.
- [x] Compares build versus TigerBeetle, Formance, Modern Treasury, Oracle Accounting Hub, Workday Accounting Center and SAP FI-CA using only documented facts, saying "not documented" where a vendor publishes no figure.
- [x] Northmere example: the SFP merchant subledger redesign, its decision record, migration and illustrative results.

## Non-goals

- Teaching double entry, revenue recognition or principal-versus-agent from first principles ([[accounting-for-architects]]).
- When to build a custom finance platform at all ([[custom-finance-platforms]], [[build-versus-buy]]).
- The general integration patterns (outbox, CDC, canonical events in general) ([[integration-architecture]]).
- PSP settlement normalization and the three-way match ([[payments-to-ledger]]).
- ITGC and rule-store change control in depth ([[controls-and-auditability]]).
- The estate-wide reconciliation catalog ([[traceability-and-reconciliation]]) and the group multi-currency model ([[global-scale]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The rule table was aligned with [[accounting-for-architects]] (account names, check-out revenue timing, chargeback under dispute with partner recovery). If that chapter's entries change, this table must change with it.
- Formance Ledger's license could not be confirmed from the repository page; the chapter makes no license claim.

## Decision log

- **2026-10-18** — Used SQL DDL, a YAML-like rule grammar and pseudo-code rather than a real language, to stay language-neutral while keeping code-level precision.
- **2026-10-18** — Collapsed Stayloft B.V. and Northmere Payments B.V. into one set of books in the rule table, stated as a simplification, and pointed to the intercompany entries in [[accounting-for-architects]], to keep the rule table readable.
- **2026-10-18** — Framed the volume as modest (about 35 lines a second) to move the argument from throughput to evidence; rejected a section on distributed ledger databases at Uber scale as irrelevant to the reader's typical problem.
- **2026-10-18** — Had Northmere keep a relational journal and defer TigerBeetle, so the trade-off table reads as a genuine choice rather than an endorsement.

## Sources

- **Internal**
  - [[accounting-for-architects]] — the merchant-model entries and account names the rule table implements.
  - [[controls-and-auditability]] — rule-store lifecycle and the SFP significant deficiency; account naming for the Lisbon split.
  - [[where-finance-architecture-goes-wrong]] — the 13-month drill-back map failure.
  - [[meet-northmere]] — SFP volumes, the Lisbon booking, Keystone timeline.
- **External**
  - Martin Fowler, *Accounting Patterns* (Analysis Patterns supplement), *Patterns for Accounting*, *Money*, *Event Sourcing*, *Bitemporal History* — patterns and vocabulary.
  - Square (Books), Stripe (Ledger, idempotency), TigerBeetle, Formance, Modern Treasury — published ledger designs and products.
  - Oracle Accounting Hub (26C), Workday Accounting Center, SAP Learning on FI-CA GL integration — ERP accounting-hub facts.
  - Confluent and Debezium documentation — delivery guarantees.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned Lisbon settlement and payout dates (and batch id) with the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Added a one-sentence cross-reference to the new Part V case study [[case-uber-payments]]. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: SFP subledger cut-over moved to Mon 2 Aug 2027 (shadow through June and July closes) per the second-month-of-quarter rule; Lisbon `PaymentSettled` debits Cash in transit until the 16 Mar bank credit; forward note on the Dec 2027 hub decision; Uber cross-reference reworded to match ch. 44; OLTP expanded. *(AI-mediated session)*
- **2026-10-18** — Editor correction superseding the item-24 date: SFP subledger cut-over is Mon 1 Nov 2027 (shadow through the August, September and October 2027 closes), clear of the July–August peak; results table now covers the Nov–Dec 2027 closes. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
