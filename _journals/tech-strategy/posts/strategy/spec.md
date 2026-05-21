---
status: draft
revised: 2026-05-20
---

# Spec: Organization Tech Strategy — Reducing Fragmentation and Complexity

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Frame the **top-level strategy** for Organization engineering: optimise for
Germany-scale needs (stable single-brand operation, next 2-3 years),
not for the inherited White-Label-era platform optionality. The post
exists to give every downstream document (diagnosis, policy,
implications, roadmap, blueprints) a single re-framing they can refer
back to.

## Audience

- **Engineering leadership** setting direction for the next 2-3 years.
- **Tech leads and architects** evaluating proposals against the
  strategy.
- **Product partners** who need to know what "Germany-scale" means
  for engineering decisions.
- **New joiners** asking "why is the estate shaped the way it is".

## Success criteria

- [ ] Reader can state the one re-framing in their own words
      (Germany-scale, not White-Label-scale).
- [ ] Reader can name the four strategic outcomes: delivery speed,
      operational stability, ownership clarity, legacy retirement.
- [ ] Reader knows the main strategic move is **simplification and
      convergence**, not adding new architectural variety.
- [ ] Reader can navigate from this overview to [[diagnosis]],
      [[implications]], [[policy]], [[roadmap]], and the blueprints.

## Non-goals

- Detailed defaults, blueprints, or exceptions (those live in
  downstream records).
- Multi-brand or multi-country strategy.
- A target-state architecture diagram.
- Project-level dates, budgets, or staffing.

## Open questions

- How explicitly to call out the "next 2-3 years" boundary, given
  that strategy windows usually drift longer than planned.
- Whether to add a fifth strategic outcome around developer
  experience (currently absorbed into delivery speed).

## Decision log

- **2026-05-20** — Chose **single re-framing** (Germany-scale, not
  White-Label-scale) as the load-bearing decision. Considered listing
  many independent strategy themes; rejected because a single frame
  makes downstream choices testable in a way a list does not.
- **2026-05-20** — Made **simplification and convergence** the
  strategic move. Considered adding more architectural sophistication;
  rejected because the diagnosis identifies fragmentation as the main
  problem, not lack of sophistication.
- **2026-05-20** — Defined outcomes as **delivery speed, stability,
  quality, onboarding, ownership clarity**. Considered headcount or
  cost-reduction outcomes; rejected because those are second-order
  consequences, not the primary outcome.

## Sources

- **Internal**
  - [[diagnosis]] — the evidence base this strategy responds to.
  - [[implications]] — narrows the space of acceptable strategy
    choices.
  - [[policy]] — operationalises the strategy at decision points.
  - [[roadmap]] — sequences the strategy across phases.
  - [[operate]] — keeps the strategy alive day to day.
- **External**
  - Richard Rumelt, *Good Strategy / Bad Strategy* — informs the
    "single re-framing" framing.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
