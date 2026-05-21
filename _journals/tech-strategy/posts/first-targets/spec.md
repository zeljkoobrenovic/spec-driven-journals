---
status: draft
revised: 2026-05-20
---

# Spec: First Targets — Where to Concentrate the First Wave

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Name the **five target groups** for the first wave of simplification:
delivery path fragmentation, legacy backend and integration surfaces,
AWS account estate, legacy technology footprint, ownership hotspots.
Each chosen for high delivery friction, high ownership confusion, high
operational burden, high fragmentation, and a realistic path to
containment, consolidation, or retirement. The post identifies
*where*, not *what specifically* — concrete candidates come from
[[prioritization]].

## Audience

- **[[operate]] forum** sequencing the first wave.
- **Domain and platform owners** of the five target areas.
- **Engineering leadership** sizing the first-wave investment.
- **Strategy owner** validating that first-wave focus matches
  diagnosis.

## Success criteria

- [ ] Reader can name the five target groups and why each is in
      scope.
- [ ] Reader knows the criteria used to choose targets (friction,
      confusion, burden, fragmentation, realism).
- [ ] Reader knows what this post **does not** commit to: named
      systems, dates, budgets, project plans.
- [ ] Reader can trace from here to [[prioritization]] (the wave
      plan).

## Non-goals

- Naming specific systems, services, or projects.
- Sequencing the targets across waves (that's [[prioritization]]).
- Allocating budget or staffing.

## Open questions

- Whether five is the right count, or whether the legacy backend
  group should split into two.
- How long the first wave should run before being re-scoped.

## Decision log

- **2026-05-20** — Chose **five target groups** at this layer.
  Considered fewer with sharper edges; rejected because the diagnosis
  identifies five distinct fragmentation surfaces and merging them
  would obscure trade-offs.
- **2026-05-20** — Deferred **named systems and dates** to
  [[prioritization]]. Considered including them here; rejected
  because mixing "where" with "what specifically" would conflate two
  decisions that benefit from separation.
- **2026-05-20** — Included **realism criterion** (containment,
  consolidation, retirement). Considered choosing targets purely by
  impact; rejected because impact-only selection produces ambitious
  waves that don't ship.

## Sources

- **Internal**
  - [[diagnosis]] — the fragmentation evidence.
  - [[policy]] — the policies these targets serve.
  - [[roadmap]] — the phases these targets land in.
  - [[prioritization]] — the next-step wave plan.
- **External**
  - Lean / WIP-limit thinking — informs "small number of well-chosen
    targets" framing.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
