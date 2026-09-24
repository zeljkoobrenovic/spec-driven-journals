---
status: accepted
revised: 2026-09-24
---

# Spec: Scale the Team With AI: Capacity Claims Need the Same Evidence as Headcount

## Intent

Give a leader under investors a way to answer the claim that artificial intelligence (AI) changes what the existing team can complete, whether the claim arrives as a reason to reorganize teams to leverage AI better, hire fewer people, as a reason to cut, or as a reason to buy tools. The chapter treats an AI capacity claim exactly as [[fix-decisions-before-hiring]] treats a headcount claim: trace the work, find which constraint the tool touches (decision, knowledge or staffing), measure the change in the work that actually completes, count the cost before payback, and record a decision with a dated gate and the evidence that would reverse it. The reader leaves able to say, for one piece of work, what an AI tool would change, what it would not, what it costs, and what an investor's "AI means fewer people" argument is really asking for.

The chapter is the third team chapter of Part V: scaling up ([[fix-decisions-before-hiring]]), scaling down ([[anatomy-of-a-layoff]]), and scaling with AI. It complements [[ai-strategy-three-questions]] rather than repeating it: that chapter sorts an AI strategy request into three investments; this one takes the capacity question inside the second of them and puts it through the sizing discipline of this part.

## Context

Larkspur, the book's fictional scheduling-software company, is where [[fix-decisions-before-hiring]] left it: the two invoicing specialists' queue remains after the delegation changes, the forecast end-to-end lead time for a pricing change is about ten working days of which seven wait for the two specialists, one billing engineer is being brought into the module, and a second team is deferred pending demand, committed funding and board approval. This chapter continues that scenario with the same people (Alex technology, Priya product, Ines the company, Sam finance, Morgan the investor's adviser) and the same figures, and says so once. The shared Larkspur ledger (`_research/shared-scenario-record.md`) is not touched; no new recurring cost is invented.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- **Same trace, new question.** Reuse the hiring chapter's traced pricing change and its three constraints. For each constraint, say whether an AI tool can touch it: decision waits (no; they are authority), the specialists' knowledge queue (only if the tool lets someone other than the two specialists change the module safely, which is a knowledge-transfer question tested the way the hiring chapter tests it), building and release (yes, and measurably). The reader can repeat this sorting on their own trace.
- **Capacity, not activity.** Define capacity as the work that completes, as in the hiring chapter, and reject activity measures (lines written, requests handled, tokens used, tool seats active) as evidence of capacity. Every claimed gain in every format is stated as work completed per period with the same quality checks that applied before the tool.
- **Product and engineering, not developers only.** Give one engineering example (the pricing change) and one implementation or support example (customer setup work, which the book has traced since Part III), and show that the measurement method is the same while the risks differ (code defects versus wrong customer configuration).
- **The evidence box, kept in scope.** Reuse the dated coding-study evidence already registered ([S19] Copilot experiment 2022/2023, [S20] METR early-2025 randomized study, [S21] METR 2026 update) with the distinction between the date an experiment ran and its publication date, the measured quantity and the participant group, and say what none of them measures (Larkspur's own work). Add newer registered evidence only if verified; do not cite from memory.
- **The investor argument as a capacity claim.** Give the "AI means fewer people" argument its own section: separate a formal condition (a funding condition or reserved matter), a director's vote and an adviser's benchmark, as [[anatomy-of-a-layoff]] does for reduction pressure, and answer each with the response it requires. Show one Larkspur version: Morgan proposes that the deferred second team is no longer needed because of AI tools; the chapter tests that claim against the trace instead of accepting or refusing it.
- **Cost before payback, in full.** For the tool pilot, separate additional cash (licences, usage-based charges, any data or security work required by [S18]) from existing employees' time (training, review of generated work, the specialists' time in the pilot), one-off from recurring, and label estimates built from internal time as cost-based estimates rather than cash. No option is described as free because no licence is bought.
- **A recorded decision with a dated gate.** End the Larkspur example with the chosen option, alternatives rejected, funding, scarce capacity, who is authorized, a dated gate with what happens when the condition is met, missed or falls between thresholds, and the evidence that would reopen it. Quality is a prerequisite for every continuation branch, and the decision about the deferred second team is explicitly *not* changed by the pilot until the gate is passed.
- **House rules.** Status highlight and key points that read without prior study; terms explained at first use in each format (AI, capacity, lead time, pilot, licence, funding condition); the company leader's decision, authority and funding assumptions explicit; historical findings within source scope; fictional scenarios labelled; a meaningful counterargument (the tool may raise output while lowering the quality of what completes, or shift the constraint to review) with the evidence that would change the judgment; hand-off to [[growth-into-design]] with the system constraint still open; TL;DR and comic consistent with the article.

## Non-goals

- Not a second treatment of the three AI investment questions, the customer-facing AI product or the substitute threat; those stay in [[ai-strategy-three-questions]] and are linked.
- Not a tool comparison, a vendor recommendation or a prediction of how good AI tools will be; the chapter's claims are about measurement and decision, not about the technology's trajectory.
- Not a reduction method; when the pilot result bears on staffing, the chapter hands the reduction question to [[anatomy-of-a-layoff]].
- No prevalence claims about what companies "usually" gain; no invented study results; no new figures in the shared Larkspur ledger.

## Modalities

- [ ] `checklist.md` — not used; the book's main chapters use article, TL;DR and comic.
- [x] `summary.md` — TL;DR of 300–500 words with one overview visual, as every main chapter.
- [ ] `dialog.md` — not used in this journal.
- [x] `comics.md` — comic pages of three stacked strips, VERA-style cast as in the neighbouring chapters, with the Morgan proposal and the gate decision reached causally rather than by assertion.

## Open questions

- Whether to register new external evidence (for example DORA's reports on AI adoption and delivery performance) as S-ids; each candidate must be fetched and checked before it enters the bibliography.
- Whether the implementation/support example uses the onboarding specialist from the shared ledger (then its figures must match `shared-scenario-record.md`) or a separate, smaller example.

## Decision log

- 2026-09-24: The author proposed the chapter after the SCALE part was created, first as a move of the existing AI chapter ("Scaling With AI"), then as a new chapter once it was agreed that the existing chapter is an investment-choice chapter that belongs in COMMIT. Rejected: renaming or moving [[ai-strategy-three-questions]].
- 2026-09-24: Scenario continues the hiring chapter's invoicing-queue trace (author's choice) rather than a separate scenario, so the three team chapters read as one story and the capacity definition is inherited rather than restated.
- 2026-09-24: Scope is product and engineering including customer setup and support (author's choice), not developers only, because the book's traced work is onboarding as much as code.
- 2026-09-24: The investor's "AI means fewer people" argument is a central section (author's choice), treated as a capacity claim to test, not as a reduction to plan.
- 2026-09-24: Title form "Scale the Team With AI: …" chosen to match the retitled neighbours "Scale the Team Up" and "Scale the Team Down"; subtitle "Capacity Claims Need the Same Evidence as Headcount" states the argument. Alternatives considered: "Scaling With AI: Three Different Investment Questions" (rejected: the three questions belong to the COMMIT chapter).

## Sources

- Author's intent from the 24 September 2026 conversation (no `INPUT.md`).
- [[fix-decisions-before-hiring]] — the trace, the three constraints, the capacity definition, the deferred second team and the appointment-authority pattern this chapter inherits.
- [[anatomy-of-a-layoff]] — the three kinds of reduction pressure and the "find the real source" method reused for the investor argument.
- [[ai-strategy-three-questions]] — the three investment questions and the registered coding-study evidence box; this chapter links rather than repeats.
- [[can-the-team-deliver]] — the capability finding behind the scenario.
- Bibliography: [S18] NIST generative AI profile (data and security obligations of a pilot), [S19] Peng et al. Copilot experiment, [S20] METR early-2025 experiment, [S21] METR 2026 update. Further external evidence only after verification.

## Changelog

- 2026-09-24: Status `accepted` at the author's instruction (“all of it”) after the article, TL;DR, comic, figures, logo, icon and Probe Further were produced; the folder-placement open question is resolved by the renumbering.
- 2026-09-24: Created as `draft` from the author's intent; scenario, scope and investor-angle decisions recorded. No `index.md` yet.
