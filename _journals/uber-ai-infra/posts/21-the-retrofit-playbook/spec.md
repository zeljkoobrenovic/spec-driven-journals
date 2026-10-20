---
status: accepted
revised: 2026-10-20
---

# Spec: The Retrofit Playbook: What to Copy If You Are Not Uber

## Intent

Close Part IV by turning the whole book into an order of operations for companies of about 50, 200, 2,000 and 5,000+ engineers that must build the foundations and the AI layer at the same time. The chapter must add what no system chapter gives on its own: a reading of Uber's own sequence as planned versus reactive, sequencing principles, a scored readiness assessment (seven foundation properties plus five AI-layer controls and a headroom check), an autonomy ladder gated by those scores, a sequence by company size, one table of minimum viable versions, a 12-month roadmap with exit criteria and deliberate omissions, anti-patterns, and the cases where copying Uber is wrong.

## Audience

CTOs, VPs of Engineering and platform leads who need a plan for the next year, and staff+ engineers asked to make the codebase agent-ready. They leave with a score, a ceiling on agent autonomy, a quarter-by-quarter plan and a list of what not to build yet.

## Success criteria

- [x] Synthesizes, rather than repeats, the system chapters: each system appears once in the minimum-viable-versions table with a link to its chapter.
- [x] Readiness assessment with 0–3 levels, a level-2 and level-3 description and a concrete test per property.
- [x] Autonomy ladder (A0–A5) with minimum scores per level and Uber's position as of October 2026, labeled as the author's synthesis.
- [x] Sequence by company size including the ≈200 and ≈2,000 sizes the plan names.
- [x] 12-month roadmap with moves and measurable exit criteria per quarter, and an explicit "left out of year one" list.
- [x] Anti-patterns cover harness lock-in, MCP sprawl, unmeasured spend, review by volume and agents without verification, each with evidence.
- [x] "When not to copy Uber" table and the "measure the feature path first" case.
- [x] Two mermaid diagrams, failure modes, record gaps, questions, sources; hands off to the Reference section.

## Non-goals

- The seven properties' definitions and the dependency map ([[the-harness-is-the-easy-part]]).
- Detailed minimum viable versions of any single system (each Part I–III chapter).
- Measurement design ([[feature-velocity]]) and the engineer's role ([[the-engineer-as-context-builder]]).

## Modalities

- [ ] `checklist.md` — operational checklist (a strong candidate: the assessment and roadmap)
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Where should the ladder's gates sit numerically? Uber publishes no acceptance or revert rates by task class.
- Does Uber's green lane open, and for which change classes?
- Would Uber sequence anything differently with hindsight?

## Decision log

- **2026-10-20** — Framed Uber's AI-era sequence as planned versus reactive; the classification is labeled as the author's reading.
- **2026-10-20** — Made the autonomy ceiling the minimum of the required scores rather than an average, so one weak verification property cannot be hidden.
- **2026-10-20** — Used ≈50, ≈200, ≈2,000 and ≈5,000+ bands here (the book elsewhere uses 50/500/5,000) because the plan's question names 200 and 2,000.
- **2026-10-20** — Excluded a harness wrapper, context-graph database, fleet-wide capture-replay, auto-landing and self-built workspaces from year one, each with a trigger condition.

## Sources

- **Internal**
  - All chapters; especially [[the-harness-is-the-easy-part]], [[minion]], [[code-review-signals]], [[token-spend-governance]], [[inner-loop-and-self-healing-ci]], [[shepherd-and-fox]], [[feature-velocity]].
- **External**
  - *The Pragmatic Engineer* podcast, 14 Oct 2026; Uber Blog JUnit migration (Apr 2026), "Running a Software Factory Efficiently" (Aug 2026), "Designing MCP Gateway" (Oct 2026), SLATE (2022); *Fortune*, 26 May 2026.
  - Spotify Honk Part 1 (Nov 2025); InfoQ on Spotify (Oct 2026); Stripe Minions (Feb 2026); DORA 2025; Faros AI 2025; Thoughtworks Technology Radar Vol. 34 (Apr 2026).

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Added 1 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
