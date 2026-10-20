---
status: accepted
revised: 2026-10-18
---

# Spec: The Technology Is the Easy Part: Leading a Finance Transformation

## Intent

Explain what a Chief Architect does in a multi-year ERP modernization and finance transformation to make it succeed, and what they must not give away. The chapter separates three authorities (Finance owns the why and the benefits, the program owns plan and cost, the architect and design authority own the design) and works through the architect's continuous, narrow responsibilities: a benefits register owned by Finance, sequencing by dependency, regulatory, contract, value and calendar criteria, a design authority guarding one global template with budgeted variations, fit-to-standard with the "show me the control or the regulation" test, the SI model, data migration, reconciliation-based testing, operating-model change, cut-over governance and hypercare. Publicly documented failures are read cautiously for their architecture lesson. Northmere's Program Keystone supplies the governance structure, the first year's decisions and one hard trade-off (Stayloft's invoice-time commission rules versus the FI-CA global template).

## Audience

Chief and enterprise architects, finance-systems architects, program directors and finance-transformation leaders who are starting, running or rescuing a multi-year finance program. They know programs and ERPs; they may not have held the line on a template or written a finance testing strategy.

## Success criteria

- [x] Reader can split a business case into benefit lines with a Finance owner, baseline, measuring source and budget line, and separate lead indicators and risk reduction from banked savings.
- [x] Reader can sequence a program by dependency, regulatory dates, contract dates, value and risk, and the business calendar.
- [x] Reader can charter a design authority: membership, decision rights, and the border with the program and with Finance policy.
- [x] Reader can apply the variation classes, the variation budget and the "show me the control or the regulation" test to a customization request.
- [x] Reader can state what must never be outsourced to an SI and how each commercial model shapes incentives.
- [x] Reader can write a finance testing strategy with reconciliation-based exit criteria, mock closes, a parallel close and month-end volume tests.
- [x] Reader can describe go/no-go readiness statements, calendar windows and evidence-based hypercare exit.
- [x] Reader sees publicly documented failures with sources and a one-line architecture lesson each, without attributing cause to products.

## Non-goals

- Migration pattern catalog and SAP migration approaches: [[modernization-patterns]], [[sap-s4hana]].
- Stage-gate mechanics, parallel-run design, rollback and decommissioning of a live migration: [[incremental-modernization]].
- Decision records, review board, waivers in general: [[architecture-governance]].
- Roadmap plateaus and horizons: [[target-and-transition-states]].
- Coexistence and convergence criteria, and the 2027 Q4 Central Finance decision: [[multiple-erps]].
- Team topology and architecture roles: [[organizing-for-architecture]].
- Debt measurement after the program: [[technical-debt-and-fitness]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- National Grid, Hershey's, Target Canada, Lidl and Haribo rest on one press compilation (CIO, July 2025); find primary sources (regulator filings, company statements) before a print edition.
- The Revlon material-weakness wording is confirmed from the FY2018 10-K risk factors; Item 9A text was not read directly.
- Re-verify ViDA application dates and member-state delays before publication.
- Update the first-year decision table once [[multiple-erps]] records the 2027 Q4 convergence decision.

## Decision log

- 2026-10-18 — Framed the chapter around ownership gaps (benefits, template, proof) seen at a steering committee, so the architect's role is defined against the program manager's, not in isolation.
- 2026-10-18 — Introduced the variation budget and four variation classes as the author's device; only commercial and preference variations count against the budget.
- 2026-10-18 — Chose Stayloft's invoice-time rules (rebates, credits, netting) as the hard trade-off, consistent with the May 2027 ADR that keeps commission rating in SFP; the decision moves logic to rating rather than into FI-CA.
- 2026-10-18 — Referenced Birmingham briefly and pointed to [[oracle-fusion]] for its costs; used Revlon's 10-K as the one primary-sourced case.

## Sources

- Internal: [[chief-architect-role]], [[application-portfolio]], [[custom-finance-platforms]], [[sap-s4hana]], [[oracle-fusion]], [[workday]], [[onestream]], [[satellite-platforms]], [[finance-data-architecture]], [[systems-of-record]], [[controls-and-auditability]], [[traceability-and-reconciliation]], [[incremental-modernization]], [[architecture-governance]], [[target-and-transition-states]], [[multiple-erps]], [[technical-debt-and-fitness]].
- Research: `_research/brief-sap.md` §6; `_research/brief-oracle.md` §8.4; `_research/brief-workday.md` §8; `_research/brief-ea-integration-ledger.md` §1.7, §4; `_research/brief-accounting-controls-regulation.md` §4.2; `_research/scenario-ledger.md`.
- External: SAP Learning (Activate methodology structure); Workday Launch Flex and Methodology pages; European Commission ViDA page; Revlon FY2018 Form 10-K; CIO ERP disasters compilation (2025); The Register and Computing on Birmingham; Cartwright, Horn and Lewis, Patterns of Legacy Displacement; Nygard on decision records.

## Changelog

- 2026-10-18 — Initial spec and article written in an AI-mediated session.
- **2026-10-18** — Editorial review pass: benefits register realigned to ch. 36 ($22M+$9M retired systems = $31M, $38M effort, $26M PSP/bank); budget tied to plateau tranches; cut-over calendar aligned with ch. 12 blackout rule; partner bank-details authority as target state; 8 Dec 2027 convergence decision recorded; S/4HANA cadence corrected. *(AI-mediated session)*
- **2026-10-18** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Leading an ERP Modernization and Finance Transformation" to "The Technology Is the Easy Part: Leading a Finance Transformation" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
