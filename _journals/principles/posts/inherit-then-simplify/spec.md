---
status: draft
revised: 2026-05-20
---

# Spec: Organisation Principle — Inherit, Then Simplify

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State Organization's two-phase posture toward shared AVIV Group
technology: **inherit** the existing setup as the starting point
(AWS, networking, web, mobile, operating practices), then
**simplify** during a defined window (typically 6-12 months) in
evolutionary steps. Inheritance buys time and consistency;
simplification turns that into long-term ownership.

## Audience

- **Engineering leadership** sizing inheritance vs simplification.
- **Domain owners** of inherited systems.
- **Architecture group** evaluating simplification proposals.

## Success criteria

- [ ] Reader can name the two phases.
- [ ] Reader knows inheritance is **time-bounded**, not permanent.
- [ ] Reader knows simplification is **evolutionary**, not a
      rewrite.

## Non-goals

- Defining the specific simplification target.
- Banning all inheritance after the window.

## Open questions

- What signal ends the inheritance phase.

## Decision log

- **2026-05-20** — Chose **two phases**, not single phase.
  Considered "always inherit" or "always custom"; rejected because
  inheritance pays off short-term and custom pays off long-term.
- **2026-05-20** — Bounded inheritance to a **defined window**.
  Considered open-ended; rejected because open-ended drifts to
  permanent.

## Sources

- **Internal**
  - [[infra-tech-stack-aws-foundation]] — applies this principle to
    AWS foundation.
  - [[infra-tech-stack-networking]] — applies it to networking.
  - [[web-tech-stack]], [[mobile-tech-stack]] — applies it to web
    and mobile.
- **External**
  - Strangler Fig pattern — informs the evolutionary
    simplification.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created.
