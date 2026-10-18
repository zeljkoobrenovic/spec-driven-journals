---
status: accepted
revised: 2026-10-18
---

# Spec: Evolving the Finance Estate Over a Decade

## Intent

Close the book by answering how a Chief Architect keeps a finance estate coherent over ten years of vendor change, acquisitions and disposals, regulation and AI. The chapter teaches **stressor analysis** (adapted from Barry O'Reilly's residuality theory) as a design method: list stressors, simulate them against the architecture, and invest in the residues that recur across many of them. It argues that optionality comes from keeping identifiers, canonical events and evidence in the enterprise's own form. The architecture function must evolve from reviewing to providing platforms, checks and decision services, and runs on an annual rhythm. A short, honest 2031 retrospective and a synthesis of the book's argument around "reconciled" end the chapter.

## Audience

Chief and enterprise architects, finance-transformation leaders and CFO-level sponsors who own a multi-year finance estate and need a method for long-horizon decisions that does not depend on a forecast. Secondary: anyone finishing the book who wants its argument in one place.

## Success criteria

- [ ] The decade view separates what will change (vendors, products, regulation, business models, M&A, AI), with dated, sourced examples, from what must not change (books of record, invariants, identifiers, meaning, evidence, accountability).
- [ ] Residuality theory is attributed to Barry O'Reilly with verifiable sources, and its vocabulary (naive architecture, stressor, residue, attractor) is defined. It is contrasted with risk registers and scenario planning and positioned beside Wardley mapping and evolutionary architecture.
- [ ] Northmere stressor table with ten stressors × impact × residue × response × owner, including a Wayfare carve-out (S4) and a PSP outage/exit (S9), each simulated in depth with numbers.
- [ ] An incidence matrix shows which residues recur across stressors and how that ranking changed funding.
- [ ] Optionality is defined. Canonical events, owned identifiers and exportable evidence are presented as the antidote to Vendor Gravity, with the explicit limit that the GL is not wrapped.
- [ ] The architecture function's evolution (reviewing → providing; documents → decision services) is shown with examples drawn from earlier chapters, plus the ICFR limit.
- [ ] The annual rhythm (strategy, fitness, portfolio, vendor, stressor reviews) is shown with timing, inputs, outputs and owners.
- [ ] The 2031 retrospective states what worked, what did not and what was deliberately left unfinished. The synthesis maps five reconciliations to the chapters that teach them, followed by ten things to remember and a hand-off to [[toolkit]].

## Non-goals

- Vendor tiering, dependency budgets and exit-plan mechanics: [[vendor-portfolio-strategy]].
- Target-state and plateau design: [[target-and-transition-states]].
- The fitness-function catalog and debt register: [[technical-debt-and-fitness]].
- Team topology and architect roles: [[organizing-for-architecture]].
- The outcome of the 2027 Q4 convergence-route decision and the Q1 2028 Tablekin review: [[multiple-erps]], [[workday]]. The convergence outcome (accounting hub, 8 December 2027) is now named briefly for consistency with [[multiple-erps]] (editor decision, 2026-10-18) but not re-argued; the Tablekin review outcome is not named.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The 2020 *Procedia Computer Science* paper on residuality theory could not be fetched; the chapter cites only the Leanpub book, the 2020 Cutter article and a practitioner summary. Add the primary paper if it can be verified.
- PSD3/PSR Official Journal status and the ViDA member-state deferrals should be re-checked before manuscript lock.
- The 2031 retrospective figures are new fictional facts. Reconcile them with [[finance-transformation]] and [[organizing-for-architecture]] once those chapters exist.

## Decision log

- **2026-10-18** — Set probability aside in the stressor method and ranked residues by recurrence, so the chapter does not duplicate the risk register; probability only sizes spend.
- **2026-10-18** — Simulated each stressor against both Plateau 1 and the 2031 target, so the method tests the plan, not just the baseline; the carve-out simulation produced the "separability" convergence condition.
- **2026-10-18** — Kept the retrospective silent on the convergence route, and had Dana say that both routes needed the same residues. This avoids contradicting chapters that own the decision and makes the residuality point.
- **2026-10-18** — Presented the closing synthesis as a five-row table of reconciliations with the chapters that teach each, rather than a chapter-by-chapter recap.

## Sources

- **Internal**
  - [[vendor-portfolio-strategy]], [[target-and-transition-states]], [[technical-debt-and-fitness]], [[architecture-governance]], [[principles-standards-reference]], [[chief-architect-role]], [[ai-in-finance]], [[build-versus-buy]], [[modernization-patterns]], [[traceability-and-reconciliation]], [[payments-fundamentals]], [[adyen]].
  - `_research/productscape-digest.md` §7 (stressors and residues); `brief-ea-integration-ledger.md` §1.12, §4.4, §5; `brief-accounting-controls-regulation.md` §2.9, §4; `brief-sap.md` §1.5; `scenario-ledger.md`.
- **External**
  - Barry O'Reilly, *Residues: Time, Change, and Uncertainty in Software Architecture* (Leanpub) and "Residuality Theory: An Introduction" (Cutter, 2020): the method and vocabulary.
  - Ford, Parsons, Kua, Sadalage, *Building Evolutionary Architectures*, 2nd ed. (2022): fitness functions.
  - Simon Wardley, *Learn Wardley Mapping*: evolution axis.
  - European Commission (ViDA), Irish Revenue (Pillar Two dates), William Fry (PSD3/PSR), Deloitte DART (ASU 2024-03), SAP News (release maintenance), EUR-Lex (DORA).

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(author, AI-mediated session)*
- **2026-10-18** — Editorial review pass: separability criterion tied to the 8 Dec 2027 accounting-hub decision; 2031 figures reconciled with ch. 36/38 (apps vs 158, savings ramp, Wayfare on S/4HANA from FY2029); six standards; bridge paragraph to Part V and the Uber case before the toolkit hand-off. *(AI-mediated session)*
- **2026-10-18** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
