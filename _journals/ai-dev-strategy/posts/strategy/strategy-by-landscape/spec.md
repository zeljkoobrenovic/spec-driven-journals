---
status: draft
revised: 2026-05-20
---

# Spec: Strategy by Current Landscape

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

Provide **three concrete playbooks** for the three legacy landscapes:
.NET/TFS monolith with SQL Server, Java/Kafka microservices on
GitLab, and overly complex Node.js serverless on GitHub. Each
implemented as a Claude Code workflow with named subagents.

## Audience

- **Engineers** working in one of the three estates.
- **Tech leads** sequencing migration work.
- **AI Engineering Enablement** building the subagents.

## Success criteria

- [ ] Reader can identify their estate's playbook.
- [ ] Reader knows each playbook has named subagents.
- [ ] Reader sees the playbooks as **strategies, not surveys**.

## Non-goals

- Listing every legacy system.
- Replacing service-level migration plans.

## Open questions

- Whether new estates emerge that don't fit the three categories.

## Decision log

- **2026-05-20** — Wrote **three concrete playbooks**. Considered a
  generic playbook; rejected because the three estates have
  genuinely different shapes.

## Sources

- **Internal**
  - [[current-state-and-problem]] — the three estates.
  - [[ai-use-case-portfolio]] — the workflows.
  - [[claude-code-enablement]] — the subagent infrastructure.
- **External**
  - Modernisation patterns (Strangler Fig, Anti-Corruption Layer).

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
