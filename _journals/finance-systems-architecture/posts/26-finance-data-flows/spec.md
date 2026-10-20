---
status: accepted
revised: 2026-10-20
---

# Spec: One Number, Many Views: Finance Data from Operations to Analytics

## Intent

Show how finance data should flow from operational systems, subledgers, ledgers, close and consolidation into analytics, planning and AI without creating competing truths. The chapter owns three ideas the book relies on: the finance data platform's boundary ("the book for nothing"), the governed metric, and the ledger-to-warehouse tie-out. After reading it, an architect should accept that operational, accounting and management numbers legitimately differ. They should be able to design the definitions, status labels, bridge, tie-out and certification that make those differences explainable, and to say exactly where a data platform must stop.

## Audience

Chief and enterprise architects, data and finance-systems architects, heads of finance data, and FP&A and controllership leaders who share a cloud data platform with the ledgers. They know warehouses and dbt-style pipelines. They may not know why revenue differs from bookings, or what IPE and disclosure controls imply for a data platform.

## Success criteria

- [ ] Reader can name the three kinds of finance numbers (operational, accounting, management) and the four reasons they differ (timing, presentation, scope, currency). They can read a Q1 2027 bridge from dashboard "revenue" ($2,431m) to closed US GAAP revenue ($1,986m) to the IR model's figure ($2,021m), with every line a named mechanism.
- [ ] Reader can state the platform's boundary in a does/does-not table, including the conditions under which a posting service may read a contracted FinDB dataset.
- [ ] Reader can follow a medallion architecture (sources, ingestion, bronze/silver/gold, governed metrics, consumers) in a diagram, with control totals, ledger keys and certification placed explicitly.
- [ ] Reader can define a governed metric's six parts and apply them to worked definitions of Net revenue and GTV, including the difference between a tie-out and an anchor.
- [ ] Reader can design a three-level tie-out (copy, derivation, bridge) with unit, schedule, tolerances (zero for closed periods), break routing and certification.
- [ ] Reader can apply latency tiers and status labels (operational, preliminary, flash, closed, restated) aligned with the close calendar.
- [ ] Reader can design lineage end to end (pipeline lineage, ledger keys, version stamps), the zones of self-service versus certified reporting, access, MNPI and retention controls, and safe feeds to planning and AI agents.
- [ ] Vendor and regulatory facts are sourced and dated: medallion, ODCS, OpenLineage and dbt, dbt Semantic Layer, Snowflake semantic views and row access policies, SAP BDC, Oracle FDI, Workday Data Cloud, SEC Release 33-10751, Regulation G.

## Non-goals

- Master data domains, MDM styles, chart-of-accounts governance, the two lineage strands and data contract anatomy: [[finance-data-architecture]].
- The full booking-to-filing trace: [[transaction-to-report]]. System-of-record authority per object and stage: [[systems-of-record]].
- Subledger design and the subledger-to-GL tie-out: [[designing-financial-ledgers]]. PSP normalization and three-way match: [[payments-to-ledger]].
- Consolidation mechanics and the mapping decision: [[onestream]]. AI agent controls: [[ai-in-finance]]. IPE and ITGC in depth: [[controls-and-auditability]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Snowflake semantic views' general-availability status and Databricks metric views were not checked; the article names them without claiming status.
- Whether Northmere discloses GTV as an MD&A KPI is not in the ledger; the article treats it as possible, not as fact.
- Workday Data Cloud finance GA (targeted 2027R1 as of October 2026) should be rechecked before final copy.

## Decision log

- **2026-10-18** — Framed the "three revenue numbers" problem as numbers of different kinds sharing one name, not as wrong numbers. The bridge table carries the argument, and renaming ("revenue" reserved for accounting) is the first fix. Rejected framing it as a data-quality incident because it would teach the wrong remedy.
- **2026-10-18** — Split the tie-out into three levels (copy, derivation, bridge) and gave GTV an "anchor" instead of a tie-out. Operational metrics cannot equal a ledger balance, and pretending otherwise would make the control meaningless.
- **2026-10-18** — Northmere keeps OneStream as source of truth for closed totals and the dbt semantic layer as the single home of definitions ("OneStream decides the total; FinDB decomposes it"). Rejected a vendor semantic model because of three ERPs, and rejected CPM-only because of grain.
- **2026-10-18** — Accepted the [[stripe]] chapter's posting services reading FinDB's normalized layer, under three stated conditions, rather than contradicting it.

## Sources

- **Internal**
  - [[finance-landscape]] — layer 8 and "the book for nothing".
  - [[onestream]] — mapping ADR, close calendar (WD3 flash, WD9 lock), planning drivers.
  - [[stripe]], [[adyen]] — Data Pipeline into FinDB, canonical money movements.
  - [[finance-data-architecture]] — lineage strands, data contracts, retention.
  - `_research/brief-ea-integration-ledger.md`, `_research/brief-satellites-ai.md`, `_research/productscape-digest.md` (finance data platform and metrics bricks, data assets).
- **External**
  - Databricks, *Medallion architecture*; Dehghani, *Data Mesh Principles*; Bitol, *ODCS*; OpenLineage docs and dbt integration.
  - dbt Labs, *dbt Semantic Layer*; Snowflake, *semantic views* and *row access policies*.
  - SEC Release 33-10751 (2020) on KPIs in MD&A; 17 CFR 244.100 (Regulation G); KPMG segment reporting handbook.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: partner bank-details authority reworded to SFP in 2027 with Northmere Pay as sole author from mid-2028; American spelling. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-18** — Added a cross-reference to [[finops]] (cloud billing data product and unit cost as a governed metric). *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Finance Data Across the Estate: From Operations to Analytics" to "One Number, Many Views: Finance Data from Operations to Analytics" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 4 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,952 → 6,908 prose words; opening now places the chapter in Part III (builds on [[transaction-to-report]] and [[payments-to-ledger]], used by [[systems-of-record]], [[traceability-and-reconciliation]] and [[ai-in-finance]]); "Design" subsection renamed "How the tie-out works"; teaser and recap first sentences replaced with claims; no spec criteria changed. *(AI-mediated session)*
