---
status: accepted
revised: 2026-10-18
---

# Spec: Finance Data Architecture: Master Data, Systems of Record and Governance

## Intent

Give the reader a working model of the data under every finance platform: which master data domains exist, how to choose a management style per domain, who owns and stewards each, and how the chart of accounts and its mappings are designed and governed as controlled configuration. The chapter answers the PLAN question "which financial data must be mastered where, and how is it governed?" and turns Northmere's "three charts of accounts" and partner-duplication problems into a concrete design: a group CoA with seven dimensions, governed mappings, a change workflow tied to SOX, and a partner master in coexistence with attribute-level authority.

## Audience

Chief and enterprise architects, finance-systems and data architects, and finance-transformation leads who must decide where master data is authored, how it reaches ERP, consolidation, reconciliation and the data platform, and how its changes are controlled. They should leave able to defend a style per domain, design a group chart, and recognize mapping tables as master data and as a control.

## Success criteria

- [ ] Distinguishes reference, master, transactional and derived data with examples and governance consequences.
- [ ] Covers the ten financial master data domains (legal entity, CoA and dimensions, cost/profit centers, organizational hierarchy from HCM, business partners, bank accounts, products and fee types, tax codes, FX rates, fiscal calendars) with golden source and difficulty.
- [ ] Compares registry, consolidation, coexistence and centralized MDM in a table, with a stated rule for when each fits finance (CoA centralized, partner master coexistence).
- [ ] Shows Northmere's group CoA v2 (natural account + entity, brand, business model, market, product, IC partner, cost center), a worked mapping table with rule types and an unmappable row, and a CoA change-request flow diagram tied to SOX.
- [ ] Works through the 850,000-partner problem across SFP, FI-CA, Northmere Pay/Adyen balance platform and Vertex, with attribute-level authority.
- [ ] Includes ownership and stewardship roles, data quality rules with examples, lineage (data and rule strands), a finance data contract example, and retention vs GDPR.
- [ ] Contains a trade-off table, at least two mermaid diagrams, a Chief Architect's view, questions to ask, and Sources and Evidence; Northmere figures agree with the ledger.
- [ ] Does not re-teach the SoR matrix, ITGCs/SOX mechanics, or consolidation mechanics owned elsewhere.

## Non-goals

- The full system-of-record matrix and authority hand-off along the transaction lifecycle ([[systems-of-record]]).
- ICFR, ITGCs, IPE, SoD and evidence-by-design in depth ([[controls-and-auditability]]).
- Legal entity, intercompany and multi-currency design ([[global-scale]]).
- Consolidation mechanics and OneStream mapping features ([[onestream]]); canonical event design ([[loosely-coupled-domains]]); warehouse and governed metrics ([[finance-data-flows]]).
- Product-level evaluation of MDM tools (SAP MDG versus specialist MDM platforms).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- SAP-specific claims (MDG capabilities, Universal Journal account assignments) are stated cautiously and could not be verified against SAP help pages in this session; the SAP chapter should confirm or correct them.
- Should the group CoA design show a full numbering scheme for the 1,150 accounts in the toolkit?
- Whether Northmere's partner hub is bought or built is left to [[build-versus-buy]]; this chapter only fixes the style.

## Decision log

- **2026-10-18** — Opened with the Tablekin usage-revenue misclassification (consistent with the failure-patterns chapter) rather than an abstract MDM story, because it shows a mapping as a control failure with a number.
- **2026-10-18** — Treated mapping tables, account determination and summarization keys as master data, rejecting the vendor framing of them as configuration, because they decide where amounts land.
- **2026-10-18** — Chose "centralize the vocabulary, coexist on operational masters" as the governing rule; registry and consolidation framed as transitional steps rather than end states.
- **2026-10-18** — Kept PSP clearing accounts and partner versus trade payables as natural-account splits, to show that reconciliation units and liability meaning override dimensional purity.

## Sources

- **Internal**
  - [[where-finance-architecture-goes-wrong]] — The Many Masters and Spreadsheet Glue patterns and the Tablekin mapping incident.
  - [[systems-of-record]], [[controls-and-auditability]], [[global-scale]], [[onestream]] — neighboring ownership boundaries.
  - `_research/brief-ea-integration-ledger.md` §2 (MDM styles, data mesh, contracts, lineage); `brief-accounting-controls-regulation.md` §1.3, §3, §5 (CoA design, controls, retention, GDPR); `productscape-digest.md` §1.1 and §3 (financial master data brick, data assets, retention); Oracle, Workday and BlackLine/OneStream briefs.
- **External**
  - Informatica, *MDM Implementation Styles* — the four styles.
  - Oracle Fusion GL documentation — ledger and balances-cube constraints.
  - Workday Financial Management datasheet — Foundation Data Model and worktags.
  - Bitol, *Open Data Contract Standard*; OpenLineage documentation — contract and lineage models.
  - Zhamak Dehghani, *Data Mesh Principles and Logical Architecture* — domain ownership limits.
  - GDPR Art. 17; Haufe on German retention; Deloitte DART on ASU 2024-03.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: partner bank-details authority in Northmere Pay reframed as the target state (authored in SFP in 2027, moves by 30 June 2028); noted no MDG in 2027; spelling fix. *(AI-mediated session)*
