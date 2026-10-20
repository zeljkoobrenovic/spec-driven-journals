---
status: accepted
revised: 2026-10-20
---

# Spec: Modernizing Without Stopping the Close

## Intent

Close Part III with the book's worked migration: moving Stayloft's merchant subledger from the Stayloft Finance Platform (SFP) onto the group accounting engine and the S/4HANA core, following the 8 December 2027 convergence decision in [[multiple-erps]], over 2028–2030 without disrupting the close or partner payouts. The chapter owns **migration stage-gate design**. Each stage is shown with scope, transitional architecture, dual running and reconciliation gates, cut-over calendar, rollback, controls and auditor involvement, people and hypercare, and measured outcome. The reader also gets a stage-gate table, a cut-over runbook excerpt (T−30 to T+10), an honest account of the stage 1 setbacks and how the design absorbed them, and the decommissioning of SFP's subledger components.

## Audience

Chief and enterprise architects, finance-systems architects, program leads, controllers and controls leads who must plan, sign and evidence a live book-of-record migration. They know the pattern catalog from [[modernization-patterns]]. They need to see it applied end to end with real constraints.

## Success criteria

- [ ] Reader can choose a slicing dimension by testing candidates against the reconciliation catalog, and explain why Northmere sliced by contracting entity aligned with PSP merchant accounts.
- [ ] Reader can fit cohorts to a blackout calendar, including the rule that blackouts freeze deployments, not effective dates.
- [ ] Reader can specify gates G0–G3 with what must tie out, tolerance, duration and approvers.
- [ ] Reader can design dual running with a reverse shadow, per-entity rollback and a stated point of no return.
- [ ] Reader can read a cut-over runbook from T−30 to T+10 and explain the purpose of each step.
- [ ] Reader can name the stage 1 setbacks (late chargebacks on pre-cut-over bookings, FX rounding misclassified as timing, payout reference) and the gate criteria they produced.
- [ ] Reader can describe the controls, disclosure and auditor steps of a migration for a SOX registrant, and why a first stage before year-end matters for control evidence.
- [ ] Reader can plan decommissioning: archive with reconciliation pack, retrieval drills, access removal, deletion, and the retirement of transitional components.

## Non-goals

- The pattern catalog, parallel-run variants and the calendar rule itself ([[modernization-patterns]]).
- The convergence decision and its alternatives ([[multiple-erps]]); the engine's internal design ([[designing-financial-ledgers]]).
- Program governance, go/no-go roles and integrator management ([[finance-transformation]]); the reconciliation catalog ([[traceability-and-reconciliation]]); plateau planning ([[target-and-transition-states]]).
- Wayfare's convergence onto S/4HANA and the payout-engine collapse (mentioned only as capacity constraints).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Ch. 13 recommended FI-CA for the merchant subledger and ch. 25 assumes expected receivables "move with the subledger"; this chapter follows ch. 28's hub decision (payables in the engine, FI-CA for invoicing and residual receivables). Reviewers should check ch. 13's wording is read as a 2027 recommendation superseded in December 2027.
- Ch. 12 blocks February via the year-end blackout; ch. 38's calendar summary excludes only quarter-end months, December, January and July–August. This chapter follows ch. 12. Align the two.
- The Item 308(c) disclosure is presented as a disclosure-committee judgment, not a rule; AS 2201 is cited only as the framework because the PCAOB page could not be fetched.

## Decision log

- **2026-10-18** — Revised the target from FI-CA to the group accounting engine after ch. 28 recorded the 8 December 2027 hub decision; FI-CA keeps merchant invoicing (May 2028) and residual recoveries.
- **2026-10-18** — Two cut-over stages (1 May and 1 November 2029) instead of three: the calendar leaves two good windows, CoA v2 must come first, and the board's 2029 commitment ruled out a 2030 stage. Per-entity go/no-go and rollback make the large second stage incremental in risk.
- **2026-10-18** — Chose late chargebacks on bookings settled before cut-over as the main stage 1 setback, because the shadow-versus-snapshot lesson generalizes to any migration that moves open items only.
- **2026-10-18** — Counted the migration finished at decommissioning (October 2030), not at the last cut-over.

## Sources

- **Internal**
  - [[modernization-patterns]], [[designing-financial-ledgers]], [[custom-finance-platforms]], [[multiple-erps]], [[target-and-transition-states]], [[systems-of-record]], [[traceability-and-reconciliation]], [[payments-to-ledger]], [[redundancy-and-coupling]], [[finance-transformation]].
  - `_research/scenario-ledger.md`; `brief-ea-integration-ledger.md` §4; `brief-sap.md` §2.13, §6; `brief-accounting-controls-regulation.md` §3.3–3.4.
- **External**
  - Fowler, *Strangler Fig* (2024); *BranchByAbstraction* (2014).
  - Cartwright, Horn and Lewis, *Patterns of Legacy Displacement* and *Transitional Architecture*.
  - 17 CFR 229.308(c) (Regulation S-K Item 308); PCAOB AS 2201.
  - SAP Learning, FI-CA general ledger integration.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(author, AI-mediated session)*
- **2026-10-18** — Editorial review pass: FI-CA merchant-invoicing 2028 cohort timing aligned; STD-05 → STD-FIN-05; verified 2029 concurrency with ch. 28/29 and the Dec 2027 accounting-hub decision; American spelling. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Modernizing Without Stopping the Close: An Incremental Migration" to "Modernizing Without Stopping the Close" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 4 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,718 → 6,769 prose words (fact-dense chapter; gain is in structure); lead now ties the chapter to Part III's question and names what depends on it (the group gate standard, Part IV governance); 2 headings renamed ("The Target and the Transitional Architecture" → "Shadow and Transitional Architecture", "What we learned after stage 1" → "What Went Wrong in Stage 1"); Stage 0 paragraph split; point-first openings for the setback, scope and advantage paragraphs. No spec content changes. *(AI-mediated session)*
