---
status: accepted
revised: 2026-10-20
---

# Spec: Spend Tiers, Not Spend Caps: Governing Token Costs

## Intent

Show how Uber keeps AI spend responsible without rationing the tools: per-engineer **spend tiers** with a light manager approval to move up, a separate tier for background agents, cost visible in every session, **CostCheck** coaching, and central defaults that make each session cheaper. Set it against the public 2026 story (budget reportedly used in four months, a reported per-tool cap, then Uber's August figures: cost per session −52%, cost per 1,000 requests −34%, flat spend while requests grew 9.4×), and explain why the governance depends on the Model Gateway's attribution.

## Audience

Engineering leaders, CTOs and platform/FinOps leads deciding how to budget and govern coding-agent spend; staff engineers setting harness defaults.

## Success criteria

- [x] Reader can describe Uber's tier model, approval path, separate agent tiers, visibility and CostCheck, each attributed to the episode or the August 2026 blog.
- [x] Press reports (Fortune, Bloomberg) are kept separate from Uber's own figures; the per-tool cap versus shared tier conflict is flagged, not resolved by assertion.
- [x] The episode's "about 50%" is presented as framing of the blog's 52% / 34% / >40% figures.
- [x] The cost equation is mapped to Uber's levers and the owning chapters.
- [x] A worked cache-lifetime example shows why interactive sessions and subagents get different defaults.
- [x] Size-banded guidance, a trade-off table of governance models, failure modes (including leaderboards), record gaps, questions, sources, two or more diagrams.

## Non-goals

- Model Gateway architecture and AI Guard ([[model-gateway]]).
- AIFX status line and settings mechanics ([[aifx-harness-layer]]).
- MCP code mode and CLI projection details ([[mcp-gateway]]).
- Measuring value and feature velocity ([[feature-velocity]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Tier amounts, approval rates, and whether the June per-tool cap was replaced by the shared tier.
- Whether CostCheck tips measurably change behavior.
- How Uber will pair cost metrics with a value measure.

## Decision log

- **2026-10-20** — Framed the chapter as a third option between caps and no limits, because that is the decision leaders actually face.
- **2026-10-20** — Used the cache-lifetime arithmetic as the worked example, because it shows why central defaults by session type matter; the multipliers are Uber's, the arithmetic is labeled as the author's.
- **2026-10-20** — Included the press timeline but kept it visually and textually separate from Uber's figures, per the evidence rules.

## Sources

- **Internal**
  - [[model-gateway]], [[aifx-harness-layer]], [[mcp-gateway]], [[skills-monorepo]], [[context-graph]], [[minion]], [[feature-velocity]], [[code-review-signals]], [[plans-as-source-of-truth]].
- **External**
  - Pragmatic Engineer, *Uber's AI infra, from the inside* (14 Oct 2026) and show notes.
  - Uber blog, *Running a Software Factory Efficiently at Uber Scale* (27 Aug 2026).
  - Pragmatic Engineer, *How Uber uses AI for development* (10 Mar 2026).
  - Fortune (26 May 2026); Bloomberg (2 Jun 2026).
  - FinOps Foundation, *FinOps for AI Overview* (Feb 2026); Claude Code cost docs; LiteLLM and Kong gateway docs.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: the "about 50%" attributed to the show notes, not the episode; paraphrased most tier quotes (quote budget); fixed the cost-equation lever table (context hygiene moved to tokens per request), linked the AI Engineer talk, Title Case subheadings. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
