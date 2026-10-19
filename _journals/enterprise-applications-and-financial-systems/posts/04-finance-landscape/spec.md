---
status: accepted
revised: 2026-10-18
---

# Spec: Anatomy of a Finance Estate: Layers, Planes and Boundaries

## Intent

Give the book its master reference model: a layered decomposition of an enterprise finance estate that later chapters cite by name. Eight layers (1 Operational and engagement systems; 2 Financial event and subledger layer; 3 Accounting core: GL and ERP; 4 Close, reconciliation and consolidation; 5 Planning and performance; 6 Reporting and disclosure; 7 Satellite services; 8 Finance data platform) and two cross-cutting planes (integration plane, control plane). The organizing argument is the **volume gradient**: finance data shrinks by orders of magnitude as it moves up, every boundary is a summarization, and that is why layers exist and where detail must live. Northmere's landscape is mapped onto the model to expose overlaps, gaps and leaks.

## Audience

Chief and enterprise architects, finance-systems and integration architects who need a shared vocabulary for placement decisions ("which layer does this system belong to, and who already holds it?"). They leave with the model, the four tests for a layer, a vendor footprint map, a set of placement rules, and a way to spot layer failures in their own estate.

## Success criteria

- [x] Defines each layer and plane with purpose, why it is separate, typical components, typical vendors (sourced), data mastered, volume and latency, and typical owner; names are stable and match how other chapters already refer to them ("financial event and subledger layer", "accounting core").
- [x] Explains the volume gradient with ledger numbers (1.1bn events/yr; ~3M SFP subledger lines/day; ~38,000 GL lines/day; ~6,800 reconciled accounts; a few hundred reported lines) and derives three consequences, including "every layer keeps what it must prove, and points down for the rest".
- [x] Maps Northmere's 2027 baseline onto the model in a mermaid diagram and a findings table that marks overlaps, gaps and leaks consistently with the scenario ledger (two payout engines, three billing approaches, three reconciliation tools, Vertex/Oracle tax overlap, three integration technologies, FinDB tie-out gap, CoA mappings in spreadsheets).
- [x] Compares alternative decompositions (process, vendor-suite, capability, domain, postmodern/composable ERP) in a trade-off table and argues the model is a thinking tool, not a deployment rule.
- [x] Names three layer failure families (leakage, skipped layers, duplicate layers) with Northmere examples and the book's failure-pattern names.
- [x] Chief Architect's view with placement standards, decision rights and four measures; Questions to ask; Sources and Evidence; hands off to [[accounting-for-architects]].
- [x] Three mermaid diagrams following the style-guide syntax; 5,500–7,500 words.

## Non-goals

- The accounting behind subledgers and control accounts ([[accounting-for-architects]]).
- Process hand-offs ([[finance-processes]]); capability map and bounded contexts ([[capability-mapping]]).
- Designing a subledger or posting engine ([[designing-financial-ledgers]], [[custom-finance-platforms]]).
- Integration styles and canonical events ([[integration-architecture]], [[loosely-coupled-domains]]).
- The payments-ledger decision itself ([[payments-to-ledger]]) and the Central Finance vs accounting-hub decision ([[multiple-erps]]).
- Vendor deep dives (Part II chapters).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- "A few hundred reported lines" is deliberately approximate; if a later chapter (e.g. [[transaction-to-report]]) needs an exact count of consolidated line items, add it to the scenario ledger and align here.
- The ad-billing service's posting of summarized documents to S/4HANA receivables is raised as an open question (which system is the receivables subledger?). [[payments-to-ledger]] or [[systems-of-record]] may resolve it.
- Should the reference-model diagram and the placement rules appear in the [[toolkit]] as a reusable template?

## Decision log

- **2026-10-18** — Kept the suggested eight-layer numbering but treated satellites (7) and the data platform (8) as sitting *beside* the stack, because each attaches at several layers; integration and control are planes because they master no financial data of their own.
- **2026-10-18** — Introduced "four tests for a layer" (what it masters, grain/volume, change cadence, owner/control profile) so the model can be defended, not just drawn.
- **2026-10-18** — Classified Wayfare's booking platform posting ~2,600 summarized lines/day directly into Fusion GL as the canonical "skipped layer" example, and reframed part of the 2027 Q4 ledger decision as a layer-2 question.
- **2026-10-18** — Used Northmere Pay's February 2027 "payments ledger" proposal as the scene; left the decision to [[payments-to-ledger]] and used it only to show placement framing.

## Sources

- **Internal**
  - [[meet-northmere]], [[capability-mapping]], [[application-portfolio]], [[accounting-for-architects]], [[custom-finance-platforms]] — terminology and figures kept consistent.
  - `_research/productscape-digest.md` §1, §1.7, §3.4, §4 — bricks, cross-cutting patterns, lineage spine, platform roles and runtime split.
  - `_research/brief-sap.md`, `brief-oracle.md`, `brief-workday.md`, `brief-blackline-onestream.md`, `brief-payments.md`, `brief-satellites-ai.md`, `brief-ea-integration-ledger.md` §5.1 — vendor placement and postmodern/composable ERP.
  - `_research/scenario-ledger.md` — all Northmere numbers.
- **External**
  - Oracle Accounting Hub and GL balances cube documentation (26C); Workday Financial Management datasheet and Accounting Center page; SAP Learning (BRIM, Business Data Cloud); BlackLine and OneStream FY2025 10-Ks; Adyen settlement details report; Stripe balance transaction and Revenue Recognition docs; Zuora products; Vertex O Series; Kyriba; TechTarget on postmodern/composable ERP.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: layer-5 row records Tablekin's Adaptive Planning overlap; blank lines before figure captions. *(AI-mediated session)*
- **2026-10-18** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Anatomy of a Financial Systems Landscape" to "Anatomy of a Finance Estate: Layers, Planes and Boundaries" at the author's request. *(AI-mediated session)*
