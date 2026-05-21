---
status: draft
revised: 2026-05-20
---

# Spec: Organisation Principle — Capabilities Follow Ownership

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that every shared capability at Organization (service, library,
platform, golden path, Skill, MCP server, subagent, CLAUDE.md
fragment, runbook) has a **named owner, a lifecycle, and a
decommissioning plan**. Capabilities without owners decay silently and
poison the platform. If a capability cannot be owned, it should not
be shared.

## Audience

- **Platform owners** maintaining shared capabilities.
- **Architecture group** evaluating new shared capabilities.
- **Engineering leadership** sizing platform investment.

## Success criteria

- [ ] Reader can name what counts as a "capability" (broad list,
      not just services).
- [ ] Reader knows every capability needs **owner + lifecycle +
      decommissioning plan**.
- [ ] Reader knows unowned shared things should not exist as shared.

## Non-goals

- Naming specific owners.
- Defining the lifecycle stages in detail.

## Open questions

- How to surface unowned capabilities systematically.

## Decision log

- **2026-05-20** — Made the scope **broad** (Skills, MCP, runbooks
  count). Considered scoping to services; rejected because all
  shared things share the ownership-decay problem.
- **2026-05-20** — Required a **decommissioning plan**. Considered
  owner + lifecycle only; rejected because decommissioning is the
  test that owner + lifecycle are real.

## Sources

- **Internal**
  - [[ownership-clarification]] — operationalises this principle
    for the strategy.
  - [[ai-operating-model]] — applies it to AI platform.
- **External**
  - Team Topologies (Skelton & Pais).

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created.
