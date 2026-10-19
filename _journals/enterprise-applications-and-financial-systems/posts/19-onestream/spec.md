---
status: accepted
revised: 2026-10-18
---

# Spec: OneStream: Consolidating Actuals, Planning the Future

## Intent

Explain what an EPM/CPM platform does that an ERP does not, and how to integrate and govern one in an estate with several ledgers. The chapter uses OneStream at Northmere as its example, but the mechanics and decisions transfer to Oracle Cloud EPM, SAP Group Reporting and other platforms. After reading it, an architect should understand consolidation mechanics well enough to design the data contracts that feed them. They should also treat the ERP-to-EPM mapping layer as governed master data, not configuration, and know which decisions about the platform belong to architecture and which to finance.

## Audience

Chief and enterprise architects, finance-systems and integration architects, and finance-transformation leads who own or depend on a consolidation and planning platform. They know systems well, but may not know how translation, eliminations and NCI work, or why mapping rules are a control.

## Success criteria

- [ ] Reader can name what an EPM platform adds above the ERP (group scope, group chart and mapping, translation, cross-ledger intercompany, ownership, multi-GAAP, top-side journals, workflow) and when ERP-embedded consolidation is the better choice.
- [ ] Reader can follow a worked consolidation of two entities with one intercompany charge: translation with CTA by component, a revaluation in the ledger, the intercompany difference caused by rates, eliminations, and the NCI and equity-pickup variants. All the numbers must reconcile.
- [ ] Reader understands extensible dimensionality as documented (17 dimensions, vertical and horizontal extensibility, data-unit sizing) and the cube-design trade-offs.
- [ ] Reader can design workflow gates (no unmapped data, control totals, reconciliation status before lock, unlock with reason) and the integration patterns (TB versus detail, drill-back and where it stops, load frequency, flash versus final close).
- [ ] Reader sees how planning integrates with Workday HCM and FinDB governed drivers, and how locked results hand off to Workiva.
- [ ] Every vendor fact is dated and sourced, including the Hg take-private (completed 1 April 2026), SensibleAI as announced in May 2025, Azure SaaS, and the alternatives table. Unverified internals are stated as unverified.
- [ ] The Keystone decision moves CoA mapping from spreadsheets into governed mapping with named owners, with the options considered and the fitness measures.

## Non-goals

- Reconciliation, transaction matching and continuous accounting in depth: [[blackline]].
- Accounting fundamentals (double entry, trial balance, revaluation basics): [[accounting-for-architects]]; multi-currency and entity architecture across the estate: [[global-scale]].
- Group chart of accounts as master data, and MDM styles: [[finance-data-architecture]].
- ERP convergence (Central Finance versus accounting hub): [[multiple-erps]].
- Disclosure platforms and tax provisioning: [[satellite-platforms]].
- AI controls in general: [[ai-in-finance]]. Vendor exit plans and negotiation: [[vendor-portfolio-strategy]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The order of OneStream's Consolidation dimension members and the design of the Smart Integration Connector could not be verified in public documentation; verify both before adding detail.
- General-availability status of SensibleAI Agents as of late 2026 is unverified.
- CCH Tagetik scope and SAP planning packaging (SAP Analytics Cloud) are stated only as "to be confirmed"; a verification pass could strengthen the alternatives table.
- OneStream SOC 1 report scope not checked.

## Decision log

- **2026-10-18** — Built the worked example on two invented entities (Stayloft B.V., Northmere Technology Inc.) with simple round numbers rather than ledger-scale figures, so that CTA, the intercompany rate difference and the non-elimination of intragroup FX gains stay visible. A three-entity example with NCI was rejected as too dense; NCI and equity pickup are shown as variants.
- **2026-10-18** — Chose Option B (OneStream as the single governed home for mapping, with brand ownership) over a separate hierarchy-management tool. The group CoA will shrink the problem by 2029. Option C will be revisited then.
- **2026-10-18** — Treated OneStream internals at the level of verified documentation only (dimensions, extensibility guide, Consolidation dimension contents) and described the consolidation sequence generically.
- **2026-10-18** — Assigned all balance-sheet reconciliation to BlackLine and let the 2022 OneStream reconciliation solution lapse. The rule: ownership follows data grain and the team doing the work.

## Sources

- **Internal**
  - `_research/brief-blackline-onestream.md` — OneStream corporate, platform, dimensionality, consolidation, integration, Solution Exchange, SensibleAI, alternatives and overlap guidance.
  - `_research/brief-accounting-controls-regulation.md` — intercompany elimination and currency translation mechanics.
  - `_research/brief-oracle.md`, `_research/brief-workday.md` — Oracle Cloud EPM and Workday consolidation and Adaptive Planning.
  - `_research/productscape-digest.md` §1.4, §2.1 — consolidation, planning and close streams.
  - [[where-finance-architecture-goes-wrong]] — the earlier Tablekin mapping incident and failure-pattern names.
- **External**
  - OneStream FY2025 10-K, platform page, documentation (Dimensions, Extensible Dimensionality, Consolidation Dimension), Hg and OneStream deal releases, SensibleAI release.
  - SAP group reporting product page; Workday consolidations guide; Oracle Cloud EPM documentation; Thoma Bravo Anaplan completion release; IFRS 10 and IAS 21 pages; Forrester on the take-private.

## Changelog

- **2026-10-18** — Initial spec and article written in an AI-mediated session. Status `accepted`.
- **2026-10-18** — Editorial review pass: functional-currency count aligned with the ledger (19); OneStream docs URLs verified (no change needed). *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "OneStream: Consolidation, Planning and Performance Management" to "OneStream: Consolidating Actuals, Planning the Future" at the author's request. *(AI-mediated session)*
