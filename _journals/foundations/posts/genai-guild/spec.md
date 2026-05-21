---
status: draft
revised: 2026-05-20
---

# Spec: GenAI Guild as a Cross-Team Generative AI Consortium

> Backfilled after the post. Companion to [[backend-guild]],
> [[frontend-guild]], and [[mobile-guild]]; same guild shape with a
> GenAI-specific four-pillar mandate.

## Intent

Establish a GenAI Guild as a standing community of practice that moves
Organization from ad-hoc GenAI experimentation to measurable productivity gains
across Product & Technology. The guild operates through four pillars
(Evangelization & Knowledge Sharing, Architecture & Standards, Research &
Innovation, Tooling & Licensing). The record should make the purpose,
mandate, scope, and resourcing legible enough that any engineer can decide
how to engage.

## Audience

- **All Avivers** experimenting with or building on GenAI — the guild is
  explicitly open.
- **Architecture team** as the facilitating body.
- **Security, legal, and procurement** as parties affected by Shadow AI
  mitigation and tooling/licensing choices.
- **Engineering leadership** as the audience for productivity-gain framing.
- **AI agents** cross-linking from AI-related decisions and strategy
  records.

## Success criteria

- [ ] Reader can state the guild's purpose (productivity gains, not
      experimentation theatre) in one sentence.
- [ ] Reader can name the four pillars and what each is for.
- [ ] Reader understands the guild is advisory and contributory, not a
      governance/procurement gate.
- [ ] Reader knows the scope (enterprise GenAI adoption) and what is out of
      scope (classical ML, recommender systems unless they intersect with
      GenAI).
- [ ] Reader can find the right Slack channel (open vs volunteer) for their
      level of engagement.

## Non-goals

- Defining the AI tooling allowlist itself. The guild *owns* that work; the
  record does not pre-empt it.
- Becoming the AI-policy authority — that lives in [[ai-policy]] and related
  records.
- Centralising AI procurement.
- Absorbing classical ML/AI work that does not intersect with GenAI.

## Open questions

- How the guild's "Architecture & Standards" pillar interacts with the
  [[architecture-advisory-forum]] without duplicating it.
- Whether Shadow AI mitigation needs its own record once the guild has run
  long enough to see real patterns.
- How "measurable productivity gains" gets measured — the guild owns the
  question, but the metric framework is not yet defined.

## Decision log

- **2026-05-20** — Adopted a **four-pillar structure** (Evangelization &
  Knowledge Sharing, Architecture & Standards, Research & Innovation,
  Tooling & Licensing). Considered a flat working-group model; rejected
  because GenAI adoption has genuinely distinct concerns
  (evangelism vs governance vs experimentation vs procurement) that need
  separate organising buckets.
- **2026-05-20** — Kept the guild **advisory and contributory**,
  facilitated by the Architecture team. Considered placing it under a
  procurement or security function for tighter Shadow AI control;
  rejected because policing-oriented bodies kill adoption, and the
  Shadow AI risk is best mitigated by making the legitimate path
  attractive.
- **2026-05-20** — Bounded scope to **GenAI**, not all ML/AI. Classical
  ML, recommender systems, and search ranking are out unless they
  intersect with GenAI capabilities. Considered widening to all AI;
  rejected because the audience, tooling, and risks of classical ML
  diverge enough to warrant separate framing.
- **2026-05-20** — Provisioned **two Slack channels** (open +
  volunteer-core). Considered a single channel; rejected because GenAI
  adoption has a large curious audience and a smaller active-contributor
  group, and a single channel buries one inside the other.

## Sources

- **Internal**
  - [[backend-guild]], [[frontend-guild]], [[mobile-guild]] — sibling
    guild records; this spec mirrors their shape with GenAI-specific
    pillars.
  - [[ai-mediated-authoring]] — the workflow this spec was authored
    through; also informs the guild's posture on AI-in-the-org.
  - [[architecture-advisory-forum]] — destination for guild proposals
    that become decisions.
- **External**
  - Spotify guild/chapter/tribe model — pattern reference.
  - Public writing on enterprise GenAI adoption (Shadow AI, evaluation
    frameworks, agentic patterns) — informs the four-pillar mandate.
  - Claude Code, Codex CLI, and MCP server documentation — informs the
    Tooling & Licensing pillar's surface.

## Changelog

- **2026-05-20** — Retrofitted to 7-section template (added Decision log
  and Sources). *(Zeljko, AI-mediated session)*
- **2026-05-20** — Reset status to `draft`. Specs were backfilled and later cleaned up; keep them current during substantive post edits. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Backfilled spec after the post existed. *(Zeljko,
  AI-mediated session)*
