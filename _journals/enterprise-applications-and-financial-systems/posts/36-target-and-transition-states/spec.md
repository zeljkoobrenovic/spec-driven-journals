---
status: accepted
revised: 2026-10-18
---

# Spec: Target State, Transition States and the Roadmap

## Intent

Show a Chief Architect how to describe where a finance estate is going and the stable steps that get there. The reader should leave treating the target state as a hypothesis with an explicit register of open decisions, able to define baseline, target and transition architectures and plateaus, and able to test whether a transition state is stable in finance terms: operable, auditable, closable at period end and valuable on its own. The chapter shows Northmere's Keystone roadmap (baseline, Plateau 1 at the FY2027 close, 2028 waypoints, Plateau 2 at the FY2029 close, 2031 target), maps its dependencies and critical path, and explains confidence labels, plateau funding and the mechanisms that keep a roadmap honest. It owns the terms target state, transition state and plateau.

## Audience

Chief and enterprise architects, finance-systems leaders and finance-transformation executives who must turn a transformation business case into a roadmap a CFO can fund and an auditor can follow. They know what a roadmap is; what they usually lack is a definition of "stable" that survives a year-end close, and a way to plan around decisions not yet taken.

## Success criteria

- [ ] Reader can explain why a target state is a hypothesis and write target elements with assumptions and the evidence that would change them.
- [ ] Reader can define baseline, target, transition architecture, plateau, gap and transitional architecture, citing TOGAF, ArchiMate and Thoughtworks.
- [ ] Reader can apply the four stability tests and the period-boundary rules to a proposed transition state.
- [ ] Reader can describe a finance target state in six views at the right altitude, with a "not decided yet" register (Central Finance vs accounting hub shown as open).
- [ ] Reader can read Northmere's per-plateau table (changes, retirements, control changes, value) and the scaffolding register.
- [ ] Reader can classify dependencies as technical, contractual, regulatory or organizational and find the critical path (Figure 3, CoA v2 year-start constraint).
- [ ] Reader can label roadmap items committed / planned / exploratory and explain plateau funding tied to the $95m savings and close-day targets.
- [ ] Reader can set up quarterly re-baselining, kill criteria and plateau value measurement; Northmere figures match the scenario ledger.

## Non-goals

- Migration execution patterns (strangler, parallel run, cut-over): [[modernization-patterns]], [[incremental-modernization]].
- Program leadership, business case, design authority, SI model: [[finance-transformation]].
- The convergence decision itself and ERP tiering criteria: [[multiple-erps]], [[sap-s4hana]].
- Vendor tiering, exit plans and contract levers: [[vendor-portfolio-strategy]].
- Portfolio scoring, TCO and decommissioning criteria: [[application-portfolio]].
- Fitness functions and debt registers: [[technical-debt-and-fitness]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The TOGAF and ArchiMate definitions are quoted via secondary sources (Orbus glossary, Bizzdesign) because the Open Group pages require registration; replace with primary citations if access is available.
- The per-plateau spend split ($54m / $171m / $85m) and the $95m savings composition ($31m / $38m / $26m) are new illustrative facts; later chapters (finance-transformation) should reuse or reconcile them.
- Plateau 2 is drawn route-neutral; update once a chapter settles the 2027 Q4 decision.

## Decision log

- **2026-10-18** — Defined plateaus as "the estate on which a fiscal year-end closes" rather than as program phases, because closability and auditability are the finance-specific meaning of "stable".
- **2026-10-18** — Treated 2028 as waypoints rather than a third plateau, because the estate's shape changes little that year and the contract asked for 2027/2029/2031 states; waypoints still pass the stability tests.
- **2026-10-18** — Kept the Central Finance vs accounting-hub decision open and showed Plateau 2 with two internal routes and shared exit tests, so the chapter does not pre-empt [[multiple-erps]].
- **2026-10-18** — Put funding by plateau tranche in the main line and dropped a separate funding-model comparison table to stay within length; the trade-off table compares roadmap styles instead.

## Sources

- **Internal**
  - [[meet-northmere]], scenario ledger — Keystone Year 1/3/5, budget, savings target, timeline anchors.
  - [[application-portfolio]] — rationalization waves, contract dates, decision-due arithmetic.
  - [[sap-s4hana]], [[oracle-fusion]], [[workday]], [[custom-finance-platforms]] — convergence options and conditional decisions.
  - [[blackline]] — 9→5 day close plan.
  - [[chief-architect-role]] — "end state only, no route" diagnosis.
- **External**
  - The Open Group, *TOGAF Standard, 10th Edition* and *ArchiMate 3.2* — baseline/target/transition and plateau/gap/work package.
  - Marc Lankhorst, Bizzdesign (2025) — plateau definition and time span.
  - Cartwright, Horn and Lewis, "Transitional Architecture" (2022) — scaffolding concept.
  - European Commission, ViDA — 2028 and 2030 dates.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(author, AI-mediated session)*
- **2026-10-18** — Editorial review pass: Plateau 1 standards named STD-FIN-01..06; product funding of platforms from 2028 aligned with ch. 41; cross-references to ch. 38's benefit and budget breakdowns; American spelling. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass (follow-up): Tablekin ledger decision dated to the June 2027 recommendation (ch. 16). *(AI-mediated session)*
