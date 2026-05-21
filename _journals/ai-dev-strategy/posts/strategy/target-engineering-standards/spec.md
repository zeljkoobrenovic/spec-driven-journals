---
status: draft
revised: 2026-05-20
---

# Spec: Target Engineering Standards for Claude Code

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State the **repository, microservice, Kafka, and AWS standards** that
agentic coding tools should help teams follow — encoded in
**CLAUDE.md, Skills, subagents, templates, hooks, and CI** so they
are enforced **by default rather than by review**.

## Audience

- **Engineers** building services that must comply.
- **AI Engineering Enablement** encoding the standards.
- **Reviewers** validating encoded checks.

## Success criteria

- [ ] Reader knows which surfaces encode the standards.
- [ ] Reader knows standards are **enforced by default**, not by
      review.
- [ ] Reader can identify the four standard families (repo,
      microservice, Kafka, AWS).

## Non-goals

- Listing every concrete standard (those live per-repo).
- Replacing existing standards processes.

## Open questions

- How to handle standard updates without breaking running
  services.

## Decision log

- **2026-05-20** — Encoded standards in **CLAUDE.md + Skills +
  hooks + CI**. Considered standards-as-policy-doc; rejected
  because docs degrade.

## Sources

- **Internal**
  - [[target-engineering-model]] — the layer model.
  - [[claude-code-enablement]] — companion enablement.
  - [[ai-engineering-standards]] — companion strategic ADR.
- **External**
  - Policy-as-code patterns.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
