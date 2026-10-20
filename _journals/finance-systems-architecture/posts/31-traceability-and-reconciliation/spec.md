---
status: accepted
revised: 2026-10-20
---

# Spec: Reconciled by Design: Traceability and Audit Across Boundaries

## Intent

Give the reader the estate-wide design catalog for traceability and reconciliation. The catalog covers the identifiers that must cross each hop, the control totals that prove each hand-off, the completeness and accuracy checks per boundary, a catalog of reconciliation types with owners and evidence, drill-down retention by level, immutable evidence, and a consistency model that ends in "closed means reconciled". The external auditor's two-direction walkthrough request is the spine: pick any number in the revenue note and show the transactions; pick any booking and show where it landed. After reading, an architect can design an estate in which every boundary can be proven, and in which a walkthrough is a product, not an investigation.

## Audience

Chief and enterprise architects, integration and finance-systems architects, and controllers and SOX leads who must make a multi-ledger, multi-PSP estate provably complete and traceable. Readers are assumed to know the ledger design (ch. 14) and close platform (ch. 18) material, or to follow the links.

## Success criteria

- [x] Reader can list the correlation keys of a booking-to-statement chain and write a propagation contract (hop → key in → key out → stored where → breaks if).
- [x] Reader can specify control totals (count, per-currency debit and credit sums, order-independent hash, period totals) and say who computes and who checks each one.
- [x] Reader can fill in a reconciliation catalog entry (purpose and assertion, independent data, frequency, owner, tolerance, exception path, evidence) for nine reconciliation types, and can apply the independence test.
- [x] Reader can state what each summarization level must retain, and the rule that no level expires before a level that depends on it.
- [x] Reader can describe an eventual-consistency model with a system-enforced close gate, and can trade off its cost.
- [x] Reader can follow the Lisbon trace top-down and bottom-up with figures consistent with the scenario ledger (€600, €90, €510, batch 1047, 16 March bank credit, 22 April sweep).
- [x] Reader can define reconciliation metrics (gross suspense, recurrence, breaks by cause) and run root-cause reviews instead of clearing sessions.
- [x] Three mermaid diagrams, trade-off table, Chief Architect's view, questions, sources.

## Non-goals

- Clearing-account design, three-way match rules and the €14m suspense remediation — [[payments-to-ledger]], [[blackline]].
- Subledger internals (posting rules, period states, summarization key) — [[designing-financial-ledgers]].
- Canonical event envelope and adapter kit — [[loosely-coupled-domains]].
- Governed metrics and the data platform — [[finance-data-flows]].
- ICFR, IPE, SOC 1 and evidence-by-design fundamentals — [[controls-and-auditability]].
- Consolidation mapping and workflow detail — [[onestream]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The AS 2201 walkthrough wording is paraphrased; the PCAOB page returned 403 during research. Verify it against the standard's text.
- The Adyen batch and bank-credit details follow [[adyen]] (batch 1047, credit 16 March). [[blackline]] uses batch 412 and a 14 March credit for the same booking. An editor should reconcile the two chapters.
- The illustrative 21 April summary document (€1,184,226.40, 13,870 lines) is local to this chapter.

## Decision log

- **2026-10-18** — Built the chapter on the auditor's two-direction walkthrough request, so that every design element answers "how would we show this?".
- **2026-10-18** — Treated the catalog as nine reconciliation types (R1–R9) in one large table, with three design rules (independence, two owners, result destination) instead of one section per type, to avoid re-teaching [[blackline]] and [[payments-to-ledger]].
- **2026-10-18** — Made "closed means reconciled" a system-enforced gate and stated its cost (the first gated close delayed two entities), so the trade-off is real.
- **2026-10-18** — Positioned lineage (OpenLineage) as complementary to item-level traceability, not a substitute, and rejected reconstruction-only traceability (option D).

## Sources

- **Internal**
  - [[controls-and-auditability]], [[designing-financial-ledgers]], [[custom-finance-platforms]], [[blackline]], [[onestream]], [[adyen]], [[where-finance-architecture-goes-wrong]].
  - `_research/brief-accounting-controls-regulation.md` (§3.5, 3.6, 3.9, 5.1), `brief-blackline-onestream.md` (A6, A7, B5, C1), `brief-ea-integration-ledger.md` (§2.1, 2.10, 3.3, 3.6, 3.7), `brief-payments.md` (§1.11, 1.14, 2.3–2.6, 4.3), `scenario-ledger.md`.
- **External**
  - PCAOB AS 2201 (walkthroughs); COSO 2013 summary; Haufe on German retention; GDPR Art. 17.
  - Adyen settlement details report and payout docs; Stripe payout reconciliation report; OpenLineage docs; OneStream dimensions; SAP Learning FI-CA GL integration.
  - Hohpe, "Your Coffee Shop Doesn't Use Two-Phase Commit"; Hohpe and Woolf, Correlation Identifier; Garcia-Molina and Salem, "Sagas"; Fowler, "Bitemporal History"; Stripe Ledger blog.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned Lisbon settlement and payout dates (and batch id) with the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: "closed means reconciled" now extends STD-FIN-03 rather than a 2026 standard; American spelling. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Designing for Traceability, Reconciliation and Audit Across Boundaries" to "Reconciled by Design: Traceability and Audit Across Boundaries" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 4,765 → 4,798 prose words; lead now ties the chapter to Part III's boundary argument, what it builds on ([[loosely-coupled-domains]]) and what reuses the catalog; 2 subheadings renamed; 3 topic sentences moved forward; 1 paragraph split. *(AI-mediated session)*
- **2026-10-20** — Consistency pass across the book: headings and terms aligned with the style guide and glossary (Setting the Scene at Northmere, From X to Y hand-offs, Trade-offs, Integration with, Total Cost of Ownership, Architecture Advisory Forum, anticorruption, hand-off) and cross-chapter contradictions resolved against the scenario ledger. *(AI-mediated session)*
