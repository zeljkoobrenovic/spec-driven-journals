---
status: draft
revised: 2026-05-20
---

# Spec: AI Operating Model — Dedicated AI Engineering Enablement Function

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Establish a **dedicated AI Engineering Enablement function** owning the
shared AI developer platform (Claude Code defaults, CLAUDE.md templates,
Skills, MCP / subagent registries, policy controls, exception process,
adoption support, incident coordination, six-month review). Product
teams keep delivery accountability; enablement owns shared primitives,
**not product features**. This is a platform operating model, not an AI
centre that does teams' work.

## Audience

- **AI Engineering Enablement function** running the platform.
- **Product teams** consuming the shared primitives.
- **Engineering leadership** sizing the function's staffing and scope.
- **Security and compliance** as policy-control stakeholders.

## Success criteria

- [ ] Reader can name the function's owned surface (defaults,
      templates, registries, policy controls, exception process,
      adoption, incidents, reviews).
- [ ] Reader knows the function **does not** do product teams' work.
- [ ] Reader can identify the **six-month review cycle**
      (next: 2026-11-15).
- [ ] Reader can route the right concern to the right party
      (platform vs product).
- [ ] The post stays focused as an ADR and does not absorb registry
      examples, maturity models, detailed cadence tables, or staffing
      implementation content.
- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the decision flow.

## Non-goals

- Building an "AI centre of excellence" that takes over team work.
- Replacing existing engineering management structures.
- Defining the function's headcount or budget.
- Listing every approved tool / Skill / MCP (those live in the
  registry).

## Open questions

- Concrete staffing model — small core team, embedded liaisons, or
  hybrid.
- How exceptions get prioritised when the exception queue grows.

## Decision log

- **2026-05-20** — Refocused the post around the enablement-function
  decision, ownership boundaries, operating commitments, consequences,
  team expectations, and revisit triggers. Kept terminology as an
  appendix instead of inline explanation.
- **2026-05-20** — Chose **dedicated function**, not distributed
  ownership. Considered making this a guild responsibility;
  rejected because shared platforms need a single accountable
  owner to avoid bystander dynamics.
- **2026-05-20** — Limited scope to **shared primitives**, not
  product features. Considered embedding enablement in product
  teams; rejected because that turns shared platforms into local
  forks and undermines the compounding benefit.
- **2026-05-20** — Made the function **own policy controls**, not
  just defaults. Considered separating policy enforcement from
  enablement; rejected because the two are tightly coupled and
  splitting them creates handoff cost.
- **2026-05-20** — Set the **six-month review** as a function
  responsibility. Considered making it an architecture-group
  review; rejected because the AAF doesn't have the platform
  context to do it well.

## Sources

- **Internal**
  - [[ai-tooling]] — the platform this function owns.
  - [[ai-policy]] — the policy this function enforces.
  - [[ai-engineering-standards]] — the standards this function
    operationalises.
  - [[architecture-advisory-forum]] — where exceptions surface for
    advice.
- **External**
  - Team Topologies (Skelton & Pais) — informs the
    platform-team-vs-product-team split.
  - Internal Developer Platform writing — informs the "shared
    primitives, not features" framing.

## Changelog

- **2026-05-20** — Rewrote `index.md` into the shorter ADR structure,
  removed registry examples/cadence/maturity material, and moved
  vocabulary to an end appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
