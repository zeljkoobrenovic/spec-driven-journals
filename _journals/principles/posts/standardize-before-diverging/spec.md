---
status: draft
revised: 2026-05-20
---

# Spec: Design Principle — Standardize Before Diverging

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that Organization picks defaults and **stays on them until there is
a written, owned reason to diverge**. Teams may propose exceptions by
ADR with named costs and accepted responsibility. **Silence is not a
license.** The platform's value compounds only when most teams use
the default; exceptions are a managed minority, not a parallel norm.

## Audience

- **Engineers** choosing a stack for new work.
- **Tech leads** evaluating divergence proposals.
- **Architecture group** ratifying exception ADRs.

## Success criteria

- [ ] Reader knows the default applies unless an **exception ADR
      exists**.
- [ ] Reader knows silent divergence is **not allowed**.
- [ ] Reader can name the current defaults (.NET, ECS Fargate, MSK,
      AWS, Claude Code).

## Non-goals

- Banning divergence outright.
- Defining the exception ADR template.

## Open questions

- How to detect silent divergence systematically.

## Decision log

- **2026-05-20** — Made **silence not a license**. Considered
  team-discretion; rejected because team-discretion silently
  re-creates the fragmentation the strategy removes.
- **2026-05-20** — Allowed **exception by ADR**. Considered hard
  bans; rejected because some divergences are genuinely the right
  call and need an honest path.

## Sources

- **Internal**
  - [[backend-tech-stack-framework]], [[infra-tech-stack-compute]],
    [[infra-tech-stack-messaging]], [[ai-tooling]] — the defaults.
  - [[policy]] — the strategic policy this principle supports.
- **External**
  - Dan McKinley, *Choose Boring Technology* — informs the
    "innovation token" framing.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created.
