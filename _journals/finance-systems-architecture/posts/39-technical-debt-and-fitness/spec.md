---
status: accepted
revised: 2026-10-20
---

# Spec: Technical Debt on the Balance Sheet

## Intent

Answer the Chief Architect's question "how healthy is the finance estate, and what do we modernize first?" with two instruments the CFO can act on: a debt register that prices each item as a carrying cost in three columns (cost carried, risk carried, speed lost), and a catalog of finance fitness functions that measure the estate's architectural properties with thresholds, owners and automated feeds. The chapter adapts the author's OWNED method (three-column register, dates-first sequencing rule, tranches with gates) to an enterprise finance estate and extends it with finance-specific debt types, Finance's own units (close days, key controls, suspense balances) and gates read from fitness functions. It owns the concepts *fitness function for finance* and *debt register*.

## Audience

Chief and enterprise architects, finance-systems and integration architects, and finance-transformation leaders who must justify modernization spending to a CFO and keep standards from decaying after a program ends. Controllers and SOX leads are a secondary audience for the control-debt and EUC material.

## Success criteria

- [x] Reader can name seven finance-specific debt types (ERP custom code, unsupported versions and vendor deadlines, EUCs in the close, integration, data, control, knowledge) and link each to a failure pattern.
- [x] Reader can define a fitness function in five parts (metric, measurement, threshold, owner, automation) and distinguish it from portfolio fitness scores.
- [x] A fitness-function catalog table covers reconciliation completeness, auto-match rate, suspense aging, tie-out breaks, close duration by phase, interface error rate and replay count, idempotency conformance, clean-core score, upgrade lead time, mapping-rule coverage, EUCs in key controls, key-control automation, ledger-to-warehouse tie-out, partner master quality and decision lead time.
- [x] The chapter shows how fitness functions are automated (transport and deployment pipelines, BlackLine data, delivery ledgers, a dbt-tested FinDB mart) and reviewed (quarterly architecture fitness review), with a figure of the feeds and the review.
- [x] Northmere's register has eight items in three columns, with cash and capacity separated at the $165k planning rate, figures consistent with the ledger and with [[sap-s4hana]], [[application-portfolio]], [[integration-architecture]] and [[blackline]].
- [x] The opening ties the chapter to [[finance-transformation]] (what the program leaves behind must keep being measured) and names what later uses it ([[finops]], the debt register in [[toolkit]]).
- [x] The OWNED sequencing rule is adapted (finance's five kinds of date; close critical path and key controls as tie-break) and applied to the register.
- [x] Tranche funding uses gates written as fitness-function readings; the CFO presentation answers Tomás's two questions in his units.
- [x] Failure modes include debt as a backlog count, fitness theater and metrics without owners; figures for the carrying cost, the measurement feeds, the sequencing rule and a register item's life; trade-off table; Chief Architect's view; questions; sources.

## Non-goals

- Application-level TIME classification, TCO and retirement waves — owned by [[application-portfolio]].
- Clean-core levels, the ABAP Test Cockpit and the custom-code remediation tracks in detail — owned by [[sap-s4hana]].
- Decision records, review boards and waivers — owned by [[architecture-governance]].
- Migration stage gates and parallel runs — owned by [[incremental-modernization]].
- Money in flight and business observability, recovery and incidents — owned by [[resilience-and-security]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Tool 12 in [[toolkit]] carries one fitness-function card. Should the whole catalog appear there too?
- The interface error-rate baseline is "being measured"; a later chapter may want a number.

## Decision log

- **2026-10-18** — Kept OWNED's three columns unchanged and added finance units inside them rather than a fourth "control" column, so the method stays recognizable and the CFO reads one shape.
- **2026-10-18** — Made gates fitness-function readings rather than milestone checks; rejected a single "estate remediation program" as the worked alternative.
- **2026-10-18** — Kept the FinDB fitness mart outside SOX scope deliberately, to let definitions evolve; BlackLine remains the audit evidence.
- **2026-10-18** — Gave auto-match rate to Ingrid (payment data owner) rather than Leila, to illustrate "metrics without owners".

## Sources

- **Internal**
  - [[sap-s4hana]] — 2,300 custom objects, clean-core levels, the clean-core fitness function and upgrade lead time.
  - [[application-portfolio]] — EUC registration (31 of ~70), wave plan and cash/capacity convention.
  - [[integration-architecture]] — 1,100 interfaces, control totals, idempotency, the January 2027 double post, lane model.
  - [[blackline]] — match rates, risk tiers, 9→5 day plan.
  - [[controls-and-auditability]] — 610 key controls, 38% automated, SFP deficiency.
  - OWNED, "Manage Technical Debt" — the three-column register, sequencing rule and tranches.
- **External**
  - Ford, Parsons, Kua and Sadalage, *Building Evolutionary Architectures*, 2nd ed. (2022) — fitness functions as automated governance.
  - Martin Fowler, "Technical Debt Quadrant" (2009) — debt classification.
  - dbt Labs, data tests documentation — thresholds as tests returning failing records.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(author, AI-mediated session)*
- **2026-10-18** — Editorial review pass: mandatory standards referenced as STD-FIN-01..06; American spelling (catalog, program, theater). *(AI-mediated session)*
- **2026-10-18** — Editorial review pass (follow-up): SFP subledger cut-over date aligned to 2 August 2027 (consistency item 24). *(AI-mediated session)*
- **2026-10-18** — Consistency pass: SFP subledger cut-over date set to 1 November 2027; calendar rule wording clarified where relevant. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-18** — Closing hand-off now points to the new chapter [[finops]] (read after this one), then [[resilience-and-security]]. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Technical Debt, Architectural Fitness and Modernization Priorities" to "Technical Debt on the Balance Sheet" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,324 → 5,362 prose words; opening now ties the chapter to [[finance-transformation]] and names [[toolkit]] and [[finops]] as users; 2 subheadings renamed (Five parts of a finance fitness function; Five kinds of external date); topic sentences brought forward in 5 paragraphs; spec criteria updated for figures (mermaid replaced), an opening criterion added, and the toolkit open question narrowed to the catalog. *(AI-mediated session)*
