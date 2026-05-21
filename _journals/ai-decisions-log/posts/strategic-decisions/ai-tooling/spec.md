---
status: draft
revised: 2026-05-20
---

# Spec: AI Developer Tooling — Claude Code as Default Agent Platform for 2026

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Pick **Claude Code as the default AI developer tool** for 2026, framed
explicitly as a **platform decision, not a model leaderboard call**.
The shared developer-agent surface (CLAUDE.md, Skills, MCP, subagents,
hooks, settings, permission modes, registries, audit) is built once on
Claude Code. Codex, Gemini, and future tools stay available by
documented exception. Tooling default reviewed every six months.

## Audience

- **Engineers** picking up an AI coding tool for new work.
- **AI Engineering Enablement** owning the shared surface.
- **Architecture group and security** reviewing exceptions.
- **Engineering leadership** sizing the platform investment.

## Success criteria

- [ ] Reader can state the decision as a **platform** choice, not a
      model claim.
- [ ] Reader knows Codex, Gemini, and future tools require a
      one-page exception reviewed by AI Engineering Enablement.
- [ ] Reader sees the **six-month review cycle** (next: 2026-11-15)
      and what it covers.
- [ ] Reader can connect this to [[ai-policy]],
      [[ai-operating-model]], [[ai-engineering-standards]].
- [ ] The post stays focused as an ADR and does not absorb examples,
      learning-path, prompt-pattern, scorecard, or implementation-guide
      content.
- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the decision flow.

## Non-goals

- Claiming Claude Code is permanently best.
- Banning Codex, Gemini, or future tools.
- Freezing the model choice for 2026.
- Defining the exception form contents in detail.

## Open questions

- Concrete metrics that would trigger an early review before
  2026-11-15.
- How to onboard new tools that emerge mid-cycle.

## Decision log

- **2026-05-20** — Refocused the post around the default-tool decision,
  exception model, consequences, team expectations, and review triggers.
  Kept terminology as an appendix instead of inline explanation.
- **2026-05-20** — Chose **a single default platform** over "use
  whatever". Considered tool-of-the-week freedom; rejected because
  the shared surface (CLAUDE.md, Skills, MCP, subagents) needs a
  stable substrate to compound on.
- **2026-05-20** — Framed it as a **platform decision, not a model
  decision**. Considered framing as model-leaderboard; rejected
  because model leadership changes faster than tooling surfaces and
  re-platforming every six months destroys the compounding benefit.
- **2026-05-20** — Set a **six-month review cycle**. Considered
  annual review; rejected because the AI tooling landscape moves
  faster than annual cadence can track.
- **2026-05-20** — Allowed **exception-based use** of other tools.
  Considered banning alternatives; rejected because some workflows
  genuinely fit other tools better and a hard ban would push that
  use underground.

## Sources

- **Internal**
  - [[ai-policy]] — the policy this tooling implements.
  - [[ai-operating-model]] — the function that owns this platform.
  - [[ai-engineering-standards]] — what the platform enforces.
  - [[ai-mediated-authoring]] — depends on this tooling choice.
  - [[claude-code-as-standard]] — same choice in the principles
    journal.
- **External**
  - Claude Code documentation (Anthropic).
  - Codex CLI (OpenAI), Gemini Code Assist (Google) — the
    exception-allowed alternatives.
  - Model Context Protocol (MCP) specification.

## Changelog

- **2026-05-20** — Rewrote `index.md` into the shorter ADR structure,
  removed worked examples/learning-path material, and moved vocabulary
  to an end appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
