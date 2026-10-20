---
status: accepted
revised: 2026-10-20
---

# Spec: AIFX: Making the Coding Harness Swappable

## Intent

Show how Uber treats coding-harness churn as a design assumption and answers it with AIFX, a thin layer that owns configuration, distribution and feedback (personas, central and synced settings, one install for every harness, status-line spend) while leaving the agent loop to Claude Code, Codex and OpenCode. Make clear how little of AIFX is documented outside the episode, and how much of it depends on DevPods, standard builds and the two gateways. Give smaller companies a path that starts with one harness and its own managed settings.

## Audience

Developer-experience and platform leads, staff engineers and engineering leaders choosing which coding harnesses to support and how to manage agent configuration across an organization.

## Success criteria

- [x] Reader can list AIFX's six described behaviors and say which are confirmed in writing (the `aifx` CLI, MCP discovery, `aifx mcp` Code Mode, status-line cost counter) and which are the episode's account only.
- [x] Reader can cite evidence of harness churn at Uber (Cursor in early 2025; Claude Code 32% to 63%, December 2025 to February 2026).
- [x] Reader can draw the line between what AIFX owns and what the harness keeps.
- [x] Reader can name the foundations that keep the layer thin (DevPods, standard builds, Model and MCP Gateways, the Agent Skills format).
- [x] Reader can compare Claude Code, Codex and OpenCode managed-configuration mechanisms.
- [x] Reader can choose a path for ≈50, ≈500 and ≈5,000 engineers and knows what not to copy.
- [x] The inferred mechanism (rendering native configuration) is labeled as inference.

## Non-goals

- `aifx validate` and the CI code red — owned by [[inner-loop-and-self-healing-ci]].
- Skills content, quality gates and the CLI rewrite — owned by [[skills-monorepo]].
- Spend tiers and CostCheck — owned by [[token-spend-governance]].
- DevPod internals — owned by [[devpods]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Does AIFX launch harnesses or only write their configuration?
- Which personas exist, and is Cursor still supported through AIFX?
- Is there any written Uber source on AIFX settings sync?

## Decision log

- **2026-10-20** — Framed AIFX as a division of responsibilities (owns distribution, identity, feedback; leaves the agent loop) rather than as a feature list, because that is what generalizes.
- **2026-10-20** — Used Uber's own Claude Code adoption numbers (Pragmatic Engineer, March 2026) as the evidence for harness churn instead of generic market claims.
- **2026-10-20** — Recommended one harness plus its native managed settings for small companies; an AIFX-style generator only when a second harness becomes popular.

## Sources

- **Internal**
  - [[devpods]], [[monorepos-and-one-build]], [[model-gateway]], [[mcp-gateway]], [[skills-monorepo]] — the layers AIFX rests on.
  - [[inner-loop-and-self-healing-ci]], [[token-spend-governance]] — neighbours that own `aifx validate` and spend.
- **External**
  - The October 2026 Pragmatic Engineer episode and show notes.
  - Pragmatic Engineer, "How Uber uses AI for development" (March 2026); Uber Blog, MCP Gateway (October 2026) and Software Factory (August 2026); AAIF write-up (May 2026); AI Engineer 2026 talk.
  - Claude Code settings, Codex managed configuration and OpenCode config documentation; agentskills.io; AGENTS.md; Thoughtworks Radar Vol. 34.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: attributed the harness-churn number in WHY IT MATTERS, labeled persona examples as the author's guess, Title Case subheadings; Radar and AGENTS.md figures verified. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
