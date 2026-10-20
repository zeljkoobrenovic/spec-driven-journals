---
status: accepted
revised: 2026-10-20
---

# Spec: BlackLine: Matching, Certifying and Closing

## Intent

Show where a close-automation platform belongs in an enterprise finance architecture, using BlackLine as the main example, and separate what such a platform does (organize, match, evidence, orchestrate, control manual journals) from what it cannot do (repair late, unreferenced or summarized upstream data). The reader should leave able to design reconciliation populations, matching rules and auto-certification as controls, and able to tell which days of a close a tool can remove and which need upstream architecture. Continuous accounting is presented as a property of the data flow, not a product feature.

## Audience

Chief and enterprise architects, finance-systems and integration architects, and finance-transformation leaders who must decide how a close platform is integrated, governed and bounded in a multi-ERP, multi-PSP estate. Controllers and SOX leads are a secondary audience.

## Success criteria

- [x] Reader can distinguish balance-to-balance, subledger-to-GL, bank, intercompany and transaction-level reconciliation, and knows which integration each needs.
- [x] Reader can explain risk rating and auto-certification as controls, with owners, change management, IPE dependency and look-back.
- [x] Reader can design a matching rule (keys, tolerances, cardinality, fee and FX splitting) and follows a worked Adyen batch → bank credit → SFP expected receipts match with consistent figures.
- [x] Reader can state the posting boundary: matching proves, the subledger posts, Journal Entry posts only approved manual journals, and direct ERP posting must be closed.
- [x] Reader sees Northmere's 9 → 5 day plan attributing days to BlackLine-only, shared, and upstream-only measures (1 / 2 / 1).
- [x] Alternatives table uses only verified facts (BlackLine 10-K, Oracle Account Reconciliation docs, OneStream Solution Exchange, Trintech and FloQast about pages, SAP AFC).
- [x] Corporate status and AI availability are dated "as of October 2026"; BlackLine "popularized", not coined, continuous accounting.
- [x] The opening says where the chapter sits in Part II (after the ledgers, before [[onestream]]) and which Part III chapters build on it.
- [x] Five figures (generated illustrations), trade-off tables, Chief Architect's view, questions to ask, Sources and Evidence.

## Non-goals

- Consolidation, eliminations and CoA mapping inside the EPM tool — owned by [[onestream]].
- Clearing-account design, three-way match ownership and the €14m suspense remediation story — owned by [[payments-to-ledger]].
- Adyen and Stripe report families in detail — [[adyen]], [[stripe]].
- The enterprise reconciliation catalog and audit walkthrough — [[traceability-and-reconciliation]].
- SOC 1, CUECs and ITGCs in general — [[controls-and-auditability]].
- BlackLine Invoice-to-Cash modules (cash application, collections) — out of scope.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- BlackLine's corporate status (SAP interest, Strategic Committee) must be re-verified before publication.
- NetNow acquisition (Sept 2026) not confirmed; omitted.
- Current BlackLine connector mechanics for Oracle Fusion, Workday and S/4HANA were not verified; the chapter describes them generically.
- Oracle Transaction Matching licensing is inconsistent across Oracle docs; flagged in the table rather than resolved.

## Decision log

- **2026-10-18** — Framed the chapter around "organizes, does not repair" rather than a module tour, because the architectural value lies in boundaries (copies vs authority, posting boundary, status not data).
- **2026-10-18** — Chose the 1.9% APM analysis (two-thirds data problem, one-third rule problem) as the scene-setting device, to make the upstream argument concrete before the 9 → 5 plan.
- **2026-10-18** — Recommended that settlement and fee postings come from the subledger, not the matching tool; rejected BlackLine-as-posting-engine for high volume.
- **2026-10-18** — Treated intercompany as an origination problem; left the module purchase as a 2028 decision tied to ERP convergence.

## Sources

- **Internal**
  - [[finance-landscape]], [[accounting-for-architects]], [[controls-and-auditability]], [[integration-architecture]], [[payments-to-ledger]], [[onestream]], [[loosely-coupled-domains]], [[redundancy-and-coupling]] — context and ownership boundaries.
  - `_research/brief-blackline-onestream.md`, `brief-payments.md`, `brief-accounting-controls-regulation.md`, `brief-sap.md`, `brief-oracle.md`, `productscape-digest.md` §1.4 and §6, `scenario-ledger.md`.
- **External**
  - BlackLine FY2025 10-K, Q2 2026 10-Q and results release — product map, Verity, SAP resale.
  - Oracle Cloud EPM Account Reconciliation documentation — Reconciliation Compliance and Transaction Matching.
  - Adyen settlement details report documentation — journal types and payout reconciliation.
  - Trintech and FloQast about pages — competitor scope.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned Lisbon settlement and payout dates (and batch id) with the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: €1.74 split made explicit (€1.64 = €1.20 + €0.21 + €0.23; €0.10 batch fee), batch 1047 merchant account named, earlier €420 chargeback distinguished, SOC 1 scope hedged, American spelling. *(AI-mediated session)*
- **2026-10-18** — Added 1 inline illustration (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "BlackLine: Close Automation, Reconciliation and Continuous Accounting" to "BlackLine: Matching, Certifying and Closing" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 4 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 7,144 → 7,187 prose words; opening now places the chapter after the ledger chapters and before [[onestream]], and names [[payments-to-ledger]] and [[traceability-and-reconciliation]] as the Part III chapters that build on it; announcer sentences cut; buried points moved first (reconciliation integrations, risk rating, Task Management visibility, intercompany origination, control totals, SaaS archive, trade-off rules); cautions and lessons turned into lists. Spec: stale "four mermaid diagrams" criterion replaced by five figures, and a criterion added for the opening. No headings renamed. *(AI-mediated session)*
