---
status: accepted
revised: 2026-10-20
---

# Spec: Shepherd and Fox: From Migration Campaigns to Self-Improving Codebases

## Intent

Explain who changes code across Uber's monorepos and how: Shepherd runs each migration as a campaign (a YAML policy, a deterministic OpenRewrite recipe or an agentic prompt-and-skills engine, one PR per owned module, a campaign owner and tracker), and Fox reuses that platform to run maintenance skills as a weekly, opt-in "managed agentic loop" on Sunday. Use the documented 2026 JUnit migration as the worked example, make its lesson explicit (generative AI failed at the bulk migration; deterministic tools did the work and AI debugged failures), and trace the lineage back to Piranha's weekly stale-flag diffs. Translate it into a sequenced plan for companies without a Shepherd: ownership, a per-unit build-and-test gate, a tracker, deterministic first, agents for the tail, one measured loop before many.

## Audience

Platform and developer-experience leads, staff+ engineers running migrations, and engineering leaders deciding how to spend AI capacity on maintenance. They should leave able to tell when a change needs a recipe and when an agent, and knowing the foundations (ownership, build graph, CI capacity, PR tagging) a maintenance loop depends on.

## Success criteria

- [x] Opens with IN THIS CHAPTER / WHY IT MATTERS / three KEY POINTS / BUILT ON, per the style guide.
- [x] Defines and owns Shepherd, campaign, Fox and managed agentic loop.
- [x] JUnit numbers (75,000+ classes, 1.25M+ lines, 5,000+ diffs, ~4 months) match the ledger and cite the 2026 Uber post; the failed generative-AI attempt is stated plainly.
- [x] Fox is attributed to the podcast; the Sunday loop, Monday cap and incident mining are attributed to the talk summary and its match to Fox is labeled as the book's reading.
- [x] A lineage table (Piranha → PolyglotPiranha → Shepherd → agentic Shepherd → Fox) and a foundation table with chapter links.
- [x] Trade-off table, Google Rosie and Spotify Fleet Management/Honk comparisons with dates, company-size table, failure modes, record gaps, questions to ask.
- [x] Two mermaid diagrams (campaign flow; Fox loop).
- [x] Hands off to [[wisdom-and-debug-assist]].

## Non-goals

- How review signals and the green lane work — owned by [[code-review-signals]].
- CI capacity, the code red and self-healing CI — owned by [[inner-loop-and-self-healing-ci]].
- The skills monorepo's quality loop — owned by [[skills-monorepo]].
- PR type tagging and feature velocity — owned by [[feature-velocity]].
- Monorepo and Bazel history — owned by [[monorepos-and-one-build]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Who reviewed the 5,000+ JUnit diffs, and does Uber use any global-approver-style process for mechanical campaigns?
- Do agentic Shepherd campaigns share the JUnit campaign's build-and-test gate and skip behavior?
- What are Fox's enrollment numbers, merge and revert rates, and the size of the Monday cap?
- What does "250+ automated migrations, ~9M lines" count?

## Decision log

- **2026-10-20** — Led with the JUnit post as the worked example because it is the only detailed written account of Shepherd, and kept the podcast's agentic framing alongside it with an explicit "deterministic for the bulk, agents for the tail" table rather than choosing one account.
- **2026-10-20** — Treated the talk's Sunday maintenance loop as Fox's public description, labeled as the book's reading, because the name Fox appears only in the episode.
- **2026-10-20** — Put Piranha in a lineage section rather than a footnote, to show that Fox's delivery pattern (weekly machine diffs to an accountable owner) predates LLMs at Uber.
- **2026-10-20** — Contrasted Fox's Sunday schedule with Spotify's working-hours schedule to show that scheduling follows from the review/auto-merge policy.

## Sources

- **Internal**
  - [[monorepos-and-one-build]], [[build-what-does-not-exist]], [[contracts-and-context-propagation]] — monorepos, Bazel, ownership, trace propagation.
  - [[code-review-signals]], [[inner-loop-and-self-healing-ci]], [[skills-monorepo]], [[feature-velocity]] — neighbours this chapter links to rather than re-teaches.
  - [[wisdom-and-debug-assist]] — the next chapter.
- **External**
  - Orosz and Medisetty, *Uber's AI infra, from the inside* (Pragmatic Engineer, 2026) — Shepherd campaigns and Fox.
  - Mishra and Vejju, *How Uber Executed a JUnit Migration at Massive Scale* (Uber, 2026) — the worked example.
  - Sridharan, Barik, Clapp, *Introducing Piranha* (Uber, 2020) and Ramanathan et al. (ICSE-SEIP 2020) — the precedent.
  - Einy, *How Uber built an AI software factory* (Port, 2026) — the talk's maintenance loop.
  - Wright, *Software Engineering at Google*, ch. 22 (2020); Spotify Engineering (2025); InfoQ (2026); GitClear (2025) — industry context.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: cut ~400 words of repetition (PolyglotPiranha detail, Rosie and Spotify detail, duplicated opt-out and sequencing points, a Jaeger foundation row and a trade-off row), replaced gendered pronouns for Medisetty, labeled the opt-out criteria as inference, Title Case for the JUnit subheading. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
