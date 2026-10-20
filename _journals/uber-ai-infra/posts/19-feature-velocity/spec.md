---
status: accepted
revised: 2026-10-20
---

# Spec: From Diff Velocity to Feature Velocity: Measuring Productivity When PRs Are Cheap

## Intent

Explain why Uber's pre-AI productivity metrics (diff throughput, diffs per engineer, surveys, incidents per diff) stopped meaning what they used to once agents author a large share of PRs, and lay out the replacement Uber described: PR tagging by type and complexity (the PR mix), a feature-level clock (P50 feature time per complexity class per half, reconstructed from PRD → ERD → task → PR traces with AI repairing missing links), and a phase breakdown used to find the next bottleneck. Translate it into a minimum viable measurement program for companies without Uber's planning data.

## Audience

Engineering leaders, DevEx and platform leads, and CTOs who must justify AI tooling spend and choose what to put on the productivity dashboard. They leave knowing what to stop counting, what to start tagging, and which data prerequisites decide whether a feature-level metric is possible.

## Success criteria

- [x] Reader can explain why diff counts break when agents author PRs, with Uber's dated agent-share figures and their different definitions.
- [x] Reader can describe both instruments (PR mix, feature clock) and the AI trace-repair step, with podcast-only mechanics attributed.
- [x] Reader knows the DX Annual 2026 talk confirms feature velocity as North Star and PR classification, and that developer-years saved was tried and dropped.
- [x] The foundation table ties the feature clock to the design-doc hub, context graph, monorepo PR flow and measurement culture.
- [x] A trade-off table compares feature velocity with DORA metrics, trace repair with enforcement, and outcome cost with per-engineer spend.
- [x] SPACE, DevEx, DX Core 4, METR (2025 and the Feb 2026 update), DORA 2025, Faros and Meta RADAR are used with dates.
- [x] "If you are not Uber" gives a sized table and explicit things not to copy (per-engineer feature counts, developer-years saved).
- [x] Failure modes, record gaps and 6–10 questions are present; no invented classifier details (inference labeled).

## Non-goals

- Token spend tiers and cost dashboards ([[token-spend-governance]]).
- The engineer's changing day-to-day work ([[the-engineer-as-context-builder]]).
- Review mechanics, risk scores and Code Inbox ([[code-review-signals]]); CI load ([[inner-loop-and-self-healing-ci]]).
- The design-doc hub itself ([[plans-as-source-of-truth]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- How Uber's PR classifier works and how bot-authored PRs are counted in the mix.
- Whether Uber will publish feature-time values or the phase it found to be the bottleneck.
- How "flow efficiency" and "capability expansion" are computed.

## Decision log

- **2026-10-20** — Used the DX Annual 2026 talk as written confirmation of the direction and kept P50 feature time explicitly podcast-only, per the ledger's reconciliation table.
- **2026-10-20** — Presented the agent-share figures (10%, 11%, ~15%, 70%+) together as different definitions rather than picking one.
- **2026-10-20** — Labeled the PR classifier as inference instead of describing a plausible design as fact; rejected inventing complexity rubrics.
- **2026-10-20** — Positioned feature velocity above, not instead of, DORA stability metrics, using DORA 2025's stability finding.

## Sources

- **Internal**
  - [[plans-as-source-of-truth]], [[context-graph]], [[minion]], [[shepherd-and-fox]], [[inner-loop-and-self-healing-ci]] — systems the metric depends on or measures.
- **External**
  - Pragmatic Engineer episode "Uber's AI infra, from the inside" (2026) — the mechanics.
  - Smith and Tibrewal, DX Annual 2026, and DX recap (Jun 2026) — phases, developer-years saved, North Star.
  - Medisetty, "Running a Software Factory Efficiently at Uber Scale" (Uber blog, Aug 2026) — outcome cost paired with quality.
  - Pragmatic Engineer, "How Uber is Measuring Engineering Productivity" (2022) — diff-count history.
  - SPACE (2021), DevEx (2023), DX Core 4, METR (2025, 2026), DORA 2025, Faros 2025, Meta RADAR (2026).

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: METR 2025 and Feb 2026 figures verified against METR's posts and made exact (246 issues, 24% expected speedup, −18%/−4% point estimates, 2025 page marked out of date); unsupported "tens of thousands of PRs a week" replaced with the documented uReview volume; COO named; RADAR growth attribution corrected. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
