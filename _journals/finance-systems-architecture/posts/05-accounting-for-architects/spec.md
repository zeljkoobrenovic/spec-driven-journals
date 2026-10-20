---
status: accepted
revised: 2026-10-18
---

# Spec: Accounting for Architects: Ledgers, Journals and Revenue

## Intent

Give architects the accounting they need to design finance systems correctly, and nothing they do not. The chapter is the book's accounting foundation: later chapters link here instead of re-explaining double entry, journal entries, subledgers, revenue recognition, principal versus agent, contract liabilities, funds held for customers, revaluation versus translation and intercompany. Every concept is tied to the design decision it drives, and every rule is shown in a worked journal entry built from the shared Northmere examples. The chapter ends with five accounting invariants (balanced, immutable, period-locked, traceable, complete) that later chapters turn into designs, standards and controls.

## Audience

Chief, enterprise, solution and integration architects and senior engineering leaders who know systems deeply but have never had to read a journal entry. They should leave able to read and challenge a posting design, to ask Finance the right policy questions, and to recognize the accounting-shaped failure modes in their own estate.

## Success criteria

- [ ] Reader can explain double entry as a machine-checkable invariant and say what a balanced trial balance does not prove.
- [ ] Reader can list the fields of a journal entry and why each matters to a system design (posting date vs event date, source reference, rate, entry type).
- [ ] Reader can place a piece of detail correctly: natural account, GL dimension, subledger or operational system.
- [ ] Reader can walk the Lisbon merchant booking through eight entries (capture, fee, settlement, safeguarding top-up, stay completion, sweep, payout instructed, payout settled) and contrast it with the agency model's three.
- [ ] Reader can explain why collecting cash does not make a platform the principal, and why VAT deemed-supplier status is a separate question.
- [ ] Reader can distinguish contract liability, funds held for customers and partner payables, and explain safeguarding's effect on the chart of accounts.
- [ ] Reader can show why the Tablekin $1,029 invoice and March revenue of $1,029 are different things, and handle a refund and the €420 chargeback in later periods without reopening closed ones.
- [ ] Reader can tell revaluation (P&L) from translation (CTA in OCI) and state what every foreign-currency line must store.
- [ ] Every simplification (single-entity view, VAT on commission, policy judgments) is stated explicitly.

## Non-goals

- Payment lifecycle, interchange and dispute mechanics — [[payments-fundamentals]].
- Clearing-account design and three-way matching — [[payments-to-ledger]].
- Posting-engine, money-representation and summarization design — [[designing-financial-ledgers]].
- Control frameworks (SOX, ITGC, SoD, SOC 1) — [[controls-and-auditability]].
- Multi-currency model, rate types, transfer pricing and legal-entity design — [[global-scale]].
- Process view of the close and Order-to-Cash — [[finance-processes]].
- Leases, tax determination and disclosure rules beyond one-line mentions.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Length runs above the 7,500-word Part I guide because of the worked-entry tables the brief requires; a reviewer may move the FX or intercompany sections into [[global-scale]].
- ASC 606 paragraph references rest on the research brief; the FASB Codification is access-controlled and was not re-read.
- The safeguarding top-up and own-funds sweep are Northmere policy illustrations; a payments-regulation reviewer should confirm the framing is not read as a statement of EU law.

## Decision log

- **2026-10-18** — Presented the Lisbon booking in a single-entity (consolidated) view first, then split it across Stayloft B.V. and Northmere Payments B.V. in the intercompany section, rather than showing two-entity entries throughout, which would have doubled every table.
- **2026-10-18** — Dated the Tablekin invoice 1 April (April subscription in advance, March usage in arrears) so the same $1,029 figure demonstrates that billing is not revenue; recorded in the scenario ledger.
- **2026-10-18** — Treated chargeback recovery from the property and contra-revenue for the lost commission as Northmere policy, with the alternatives named, rather than stating one treatment as required.
- **2026-10-18** — Used a USD partner payable in a euro entity for revaluation instead of a GBP or PLN example, so the translation step to the US-dollar group follows naturally.

## Sources

- **Internal**
  - [[finance-landscape]] — subledger layer and volume gradient this chapter assumes.
  - [[designing-financial-ledgers]], [[traceability-and-reconciliation]], [[payments-to-ledger]] — chapters that deepen the invariants.
  - Research brief *Accounting, Controls and Regulation*; productscape digest §6 "Following the money"; scenario ledger.
- **External**
  - IFRS Foundation, *IFRS 15* and *IAS 21* summary pages — five-step model; currency concepts.
  - FASB ASC 606 and ASC 830 — US GAAP counterparts (via the brief).
  - Directive 2009/110/EC Article 7 — e-money safeguarding.
  - European Commission ViDA page — deemed-supplier dates.
  - Stripe documentation, *Record usage for billing* — usage aggregated at period end.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned Lisbon settlement and payout dates (and batch id) with the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: Lisbon bank-credit entries moved to 16 Mar (batch 1047 booked 14 Mar); €420 outcome tied to the canonical lost chargeback; Wayfare rail stated as merchant of record but agent; event count corrected; American spelling. *(AI-mediated session)*
- **2026-10-18** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
