---
status: draft
revised: 2026-05-20
---

# Spec: Organisation Principle — Tooling Decisions Are Explicit and Reversible

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that Organization's tooling decisions are made **explicitly**,
documented as ADRs, and reviewed on cadence. Decisions are
**reversible**: each includes the conditions for revisiting and the
practical steps for moving away. Tooling is a platform choice, not a
permanent identity. Explicitness and reversibility together make
tooling defensible without being defensive.

## Audience

- **Engineering leadership** owning tooling defaults.
- **Architecture group** ratifying tooling ADRs.
- **Platform owners** of tooling defaults.

## Success criteria

- [ ] Reader knows tooling decisions must have an **ADR + review
      cadence + exit path**.
- [ ] Reader knows tooling is **a platform choice**, not an
      identity.
- [ ] Reader can identify when a tooling decision should be
      revisited.

## Non-goals

- Banning tools that have no ADR yet (they need backfilling).
- Defining exit paths in detail upfront (those evolve).

## Open questions

- How rigorous the "exit path" needs to be at ADR time.

## Decision log

- **2026-05-20** — Required **reversibility** in every tooling
  ADR. Considered allowing irreversible commitments; rejected
  because reversibility forces the ADR to confront vendor lock-in
  early.
- **2026-05-20** — Made tooling **not an identity**. Considered
  framing tooling as cultural; rejected because identity-tied
  tooling becomes impossible to change.

## Sources

- **Internal**
  - [[ai-tooling]] — the AI default.
  - [[standardize-before-diverging]] — companion design principle.
- **External**
  - Dan McKinley, *Choose Boring Technology*.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created.
