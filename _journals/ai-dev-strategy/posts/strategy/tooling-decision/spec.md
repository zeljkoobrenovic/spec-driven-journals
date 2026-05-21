---
status: draft
revised: 2026-05-21
---

# Spec: Tooling Decision — Claude Code as the Default

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State Claude Code as **the 2026 default agentic coding tool**, framed
as a **dated operating default**, not a permanent model ranking.
Alternatives (Codex, Gemini) remain available through documented
exceptions. The default is reviewed after pilot evidence.

## Audience

- **Engineers** picking a tool for new work.
- **Architecture group** evaluating exceptions.
- **AI Engineering Enablement** running the default.

## Success criteria

- [ ] Reader knows it's a **dated default**, not a permanent
      ranking.
- [ ] Reader knows alternatives need exceptions.
- [ ] Reader knows reviews happen after pilot evidence.

## Non-goals

- Banning other tools.
- Claiming Claude is best for every task.

## Open questions

- Concrete trigger for early review before scheduled date.

## Decision log

- **2026-05-21** — Framed as **dated default**, not permanent.
  Considered eternal commitment; rejected because tool landscape
  evolves faster than commitments survive.

## Sources

- **Internal**
  - [[claude-code-as-standard]] — the capabilities argument.
  - [[review-claude]], [[review-codex]], [[review-gemini]] —
    cross-tool reviews.
  - [[ai-policy]] — the policy enforcement.
- **External**
  - Claude Code, Codex CLI, Gemini Code Assist documentation.

## Changelog

- **2026-05-21** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
