---
status: draft
revised: 2026-05-20
---

# Spec: Claude Code Use-Case Portfolio

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

Name **six high-priority agentic coding workflows** for modernization:
legacy understanding, modernization documentation, test generation,
service template generation, PR review assistance, developer
self-service. Each mapped to specific subagents, Skills, MCP servers,
evidence requirements, and human accountability points.

## Audience

- **Engineers** picking which workflow applies to their work.
- **AI Engineering Enablement** building the workflows.
- **Tech leads** sequencing workflow rollout.

## Success criteria

- [ ] Reader can name the six workflows.
- [ ] Reader knows each has **subagents + Skills + MCP +
      evidence**.
- [ ] Reader knows accountability stays with humans.

## Non-goals

- Implementing the workflows.
- Defining every workflow's internals.

## Open questions

- Whether six is right; whether new workflows emerge from pilots.

## Decision log

- **2026-05-20** — Picked **six workflows**. Considered fewer;
  rejected because each addresses a distinct modernization
  question.

## Sources

- **Internal**
  - [[strategic-principles]] — guides workflow design.
  - [[claude-code-enablement]] — provides primitives.
  - [[strategy-by-landscape]] — applies workflows to estates.
- **External**
  - Anthropic Claude Code workflow patterns.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
