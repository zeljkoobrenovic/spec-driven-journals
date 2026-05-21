---
status: draft
revised: 2026-05-20
---

# Spec: Operating Model — How the Strategy Stays Alive Day to Day

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Define the **lightest operating model** that keeps [[policy]] applied
day to day: named strategy owner, domain/platform owners, lightweight
review forum, monthly and quarterly review cadences, exception and
legacy registers, blueprints turning policy into practical defaults.
The goal is not zero exceptions; it is preventing hidden divergence
from becoming permanent fragmentation.

## Audience

- **Strategy owner** running the model.
- **Domain and platform owners** applying the strategy in their area.
- **Engineering leadership** sizing the operating burden.
- **Tech leads** submitting exceptions or seeking guidance.

## Success criteria

- [ ] Reader knows the strategy owner's role and how it differs from
      decision authority.
- [ ] Reader can identify which forum (monthly vs quarterly) handles
      what.
- [ ] Reader knows exceptions and legacy stay visible through
      explicit registers, not buried in tickets.
- [ ] Reader sees the operating principle:
      lightweight-explicit-tied-to-real-decisions.

## Non-goals

- Building a heavyweight governance board.
- Defining team-level rituals (that stays with each team).
- Eliminating exceptions (the goal is visibility, not zero).
- Specifying the blueprints themselves (those are separate posts).

## Open questions

- Concrete bandwidth estimate for the strategy-owner role.
- Whether the quarterly review needs distinct outputs beyond the
  monthly one.

## Decision log

- **2026-05-20** — Chose **lightweight + explicit** over rigorous
  governance. Considered an ARB; rejected because heavyweight
  governance fails the "tied to real decisions" test and the
  [[architecture-advisory-forum]] is the venue for advice anyway.
- **2026-05-20** — Made **exception and legacy registers** explicit
  artefacts. Considered leaving them implicit in tickets; rejected
  because hidden exceptions accumulate into permanent fragmentation.
- **2026-05-20** — Split **monthly (live decisions)** from
  **quarterly (policy fit)**. Considered a single cadence; rejected
  because live decisions need fast cadence and policy fit needs slow
  cadence.

## Sources

- **Internal**
  - [[strategy]], [[policy]], [[implications]] — the things kept
    alive.
  - [[architecture-advisory-forum]] — the wider advice venue.
  - [[curator-role]] — companion editorial stewardship.
- **External**
  - Andrew Harmel-Law, *Scaling the Practice of Architecture,
    Conversationally* — informs the advice-process posture.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
