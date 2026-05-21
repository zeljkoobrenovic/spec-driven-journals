---
status: draft
revised: 2026-05-20
---

# Spec: Operating Model for AI Engineering Enablement

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

Define **who owns what** for agentic coding: who maintains Claude
Code standards, who approves MCP servers, Skills, and subagents, who
owns modernization workflows, and who remains accountable for
production decisions. The strategy needs clear ownership — without it,
the rest is theory.

## Audience

- **AI Engineering Enablement** running the model.
- **Product teams** consuming the platform.
- **Architecture group** evaluating ownership clarity.

## Success criteria

- [ ] Reader knows who owns Claude Code standards.
- [ ] Reader knows who approves MCP / Skills / subagents.
- [ ] Reader knows production decisions stay with teams.

## Non-goals

- Building an AI centre that does product teams' work.
- Defining headcount.

## Open questions

- Staffing model (centralised vs embedded liaisons).

## Decision log

- **2026-05-20** — Separated **platform ownership** (Enablement)
  from **production decisions** (teams). Considered conflating;
  rejected because conflating recreates the bottleneck.

## Sources

- **Internal**
  - [[claude-code-enablement]] — the enablement stack owned.
  - [[ai-policy]] — the policy enforced.
  - [[ai-operating-model]] — same shape in strategic decisions log.
- **External**
  - Team Topologies — platform team patterns.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
