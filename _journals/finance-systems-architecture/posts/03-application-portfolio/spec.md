---
status: accepted
revised: 2026-10-18
---

# Spec: Manage the Application Portfolio as an Investment

## Intent

Show a Chief Architect how to turn an application inventory into a decision list that a CFO and an audit committee can test. The reader should leave knowing how to build a fact base that reconciles to independent sources, how to score fitness without theater, how to use TIME and pace layering for different purposes, how to cost a finance application in full (including integration and audit and control cost), why contract dates are architecture inputs, and what decommissioning has to prove before a saving counts. The chapter owns application portfolio management, TIME, pace layering and TCO for the rest of the book.

## Audience

Chief and enterprise architects, finance-systems leaders and finance-transformation executives who own or fund an application portfolio. They already know what an EA repository is. What they usually lack is a way to make portfolio data credible enough to fund retirements, and the discipline to make those retirements real.

## Success criteria

- [ ] Reader can name the independent sources an inventory must reconcile to (SSO, AP spend, SOX scoping list, interface catalog) and explain why.
- [ ] Reader can write anchored fitness criteria and explain calibration and the borderline rule.
- [ ] Reader can apply TIME as a time-bound disposition and pace layering as a governance, cadence and funding model, and explain why one application (SFP) can span layers.
- [ ] Reader can build a six-component TCO, including audit and control cost, and separate cash from capacity savings (worked table for three candidates).
- [ ] Reader can compute a decision-due date from renewal date, notice period and migration lead time.
- [ ] Reader can lay out rationalization waves with triggers, gates and savings (sample wave plan), and read a portfolio heat map.
- [ ] Reader can list decommissioning criteria, including archive with a read path, access removal and control-matrix update.
- [ ] Gartner-attributed models are labeled as attributed, with secondary sources; Northmere numbers match the scenario ledger.

## Non-goals

- Capability-map construction and bounded contexts: [[capability-mapping]].
- The layered reference model of a finance estate: [[finance-landscape]].
- Decision records, review boards and waivers: [[architecture-governance]].
- Vendor tiering, exit plans and contract levers in depth: [[vendor-portfolio-strategy]].
- Debt registers and fitness functions: [[technical-debt-and-fitness]].
- Control design and ITGCs: [[controls-and-auditability]].
- Migration patterns: [[incremental-modernization]], [[modernization-patterns]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No primary Gartner source for TIME or pace layering was retrievable; replace the secondary citations if a Gartner note can be cited by title and date.
- The SAP LeanIX lifecycle phase names are taken from product documentation snippets, not a definitive docs page; re-check before print.
- Wave 3 savings depend on the 2027 Q4 Central Finance versus accounting-hub decision; update once a later chapter settles it.

## Decision log

- **2026-10-18** — Treated the inventory as a ledger that must reconcile, rather than as a catalog, because it ties the chapter to the book's reconciliation theme and gives a concrete answer to "inventory as a one-off project".
- **2026-10-18** — Separated cash from capacity savings in the TCO and wave tables, rather than presenting one savings figure, so the Keystone numbers stay testable and do not overstate the $95M case.
- **2026-10-18** — Classified the two brand ERPs as Tolerate pending the 2027 Q4 decision, rather than Migrate, to avoid prejudging a decision other chapters own.
- **2026-10-18** — Introduced RateKeeper (a fictional Wayfare tax-rate service) as the "legacy tax tool" candidate and tied its retirement to the 2028 EBS archive decommissioning, to show a date-forced retirement.

## Sources

- **Internal**
  - [[meet-northmere]] and the scenario ledger — Northmere figures, cast and Keystone targets.
  - [[capability-mapping]], [[finance-landscape]], [[architecture-governance]] — neighboring contracts.
- **External**
  - Neil Sheppard, "Gartner TIME Framework for App Rationalization: Tolerate", SAP LeanIX, 2023 — TIME quadrants.
  - CIO Wiki, "Gartner's PACE Layered Application Strategy" — layer definitions; modules spanning layers.
  - SAP News, 2023 — LeanIX acquisition date.
  - OneStream FY2025 10-K and Hg completion release, 2026 — reconciliation applications; ownership change.
  - business.gov.nl; Haufe on BEG IV; GDPR Art. 17 — retention and erasure constraints at sunset.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: canonical-event ownership link corrected to [[loosely-coupled-domains]]; wave 3 row notes the December 2027 accounting-hub decision. *(AI-mediated session)*
- **2026-10-18** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-18** — Added a cross-reference to [[finops]] for hosting cost per application from tagged, ledger-tied cloud billing data. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
