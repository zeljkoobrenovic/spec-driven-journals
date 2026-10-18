---
status: accepted
revised: 2026-10-18
---

# Spec: Systems of Record and Authoritative Data Boundaries

## Intent

Answer the PLAN question "who is authoritative for what, and how is that decided and enforced?" The chapter replaces the vague "system of record" label with a precise model: authority is assigned per data element (attribute group) and per lifecycle stage, it moves along a transaction's life through defined hand-offs, and each hand-off is proven by a named reconciliation. It owns the system-of-record matrix as a working artifact and the authority hand-off, and shows how authority is enforced (write paths, contracts, detective controls) and kept clean during migrations through temporary, dated dual authority.

## Audience

Chief and enterprise architects, finance-systems, data and integration architects, and controllers or internal-control leads who must settle "which system is the real number" disputes, design integrations that do not create competing truths, and plan migrations that move authority between platforms. They should leave able to build and maintain an SoR matrix, write conflict rules, and design enforcement.

## Success criteria

- [x] Defines and contrasts system of record, system of reference, system of engagement, golden copy and derived store in a table, and separates data authority from Gartner's pace-layer use of the term.
- [x] Shows attribute-level authority for the Stayloft partner (bank account in SFP moving to Northmere Pay, verified tax ID in a KYC service, agency balance in FI-CA, payable in SFP, balance in S/4HANA).
- [x] Walks the Lisbon booking through its authority hand-offs with a diagram and a stage table; each hand-off has trigger, acceptance, reference and proof.
- [x] Presents the matrix columns (object, attribute group, stage, authoritative system with status, owner, consumers, propagation, reconciliation control, retention), a 22-object summary and a substantial detailed excerpt.
- [x] States explicit conflict-resolution rules and shows them applied (the SFP netting case).
- [x] Covers enforcement in three layers (write paths, contracts, detective controls) with a diagram.
- [x] Covers migrations with temporary dual authority, split by key, shadow runs, end dates and authority for history, with a diagram.
- [x] Uses The Many Masters and The Shadow Ledger with the 850,000-partner example and ledger numbers; includes trade-off table, Chief Architect's view, questions, sources; hands off to [[multiple-erps]].

## Non-goals

- Master data domains, MDM styles, stewardship, CoA design and the partner hub's design ([[finance-data-architecture]]).
- The reconciliation catalog and audit walkthrough design ([[traceability-and-reconciliation]]); payments matching ([[payments-to-ledger]]).
- Canonical event design and contract registry mechanics ([[loosely-coupled-domains]]); control-total mechanics ([[integration-architecture]]).
- ERP coexistence and convergence patterns ([[multiple-erps]]); migration stage-gates ([[incremental-modernization]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The matrix row counts (96 rows, 14 double claims, 9 gaps), the 46,000 dual-model partners, the netting design and the 1,300 tickets are illustrative local facts added in this chapter; later chapters ([[payments-to-ledger]], [[traceability-and-reconciliation]]) should reuse rather than re-invent them.
- Control identifiers in the excerpt (MD-07, R2R-11 etc.) are local labels; [[controls-and-auditability]] does not define a numbering scheme yet.
- Whether the matrix should be published as a toolkit template ([[toolkit]]).

## Decision log

- **2026-10-18** — Opened with Mei Tanaka's audit question and the extranet netting balance rather than a definitions section, because a balance with four claimed sources shows why per-system authority fails.
- **2026-10-18** — Chose object × attribute group × lifecycle stage as the default granularity; rejected per-system and per-field as defaults (trade-off table).
- **2026-10-18** — Treated refund and chargeback as one case object (as in the productscape data assets) so the matrix has 22 objects.
- **2026-10-18** — Framed partner bank details as SFP-authoritative in 2027 and moving to Northmere Pay by mid-2028, reconciling [[custom-finance-platforms]] (SFP component converges 2028) with [[finance-data-architecture]] (bank/KYC authored only in Northmere Pay as target).

## Sources

- **Internal**
  - [[finance-data-architecture]], [[custom-finance-platforms]], [[designing-financial-ledgers]], [[accounting-for-architects]], [[controls-and-auditability]], [[global-scale]] — partner registry numbers, SFP boundary and ADR, summary_id drill-back, Lisbon entries, SFP deficiency, rate service.
  - `_research/productscape-digest.md` §3.2–3.5 (data assets with SoR, lineage spine, retention); `brief-ea-integration-ledger.md` §1.4, §2.8–2.9, §4.2–4.4; `brief-accounting-controls-regulation.md` §1.4, §3.5–3.9, §5.
- **External**
  - Geoffrey Moore, *Systems of Engagement and the Future of Enterprise IT* (AIIM, 2011) — the engagement versus record distinction.
  - Open Data Contract Standard; Thoughtworks Transitional Architecture and Patterns of Legacy Displacement; *Building Evolutionary Architectures* (2nd ed.); SAP Learning on FI-CA GL integration.

## Changelog

- **2026-10-18** — Initial spec and article, written in an AI-mediated session.
- **2026-10-18** — Consistency pass: aligned Lisbon settlement and payout dates (and batch id) with the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: FI-CA merchant-invoicing timing aligned (April 2028 parallel run, first cohort May 2028, rest through 2028); added closing hand-off heading; American spelling. *(AI-mediated session)*
