---
status: draft
revised: 2026-05-20
---

# Spec: Design Principle — Evolutionary Systems

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

Design Organization systems for **incremental change**, not for a fixed
end-state. The next change is closer and more probable than the next
clean rewrite. Backwards-compatible contracts, additive schema
changes, feature flags, well-defined seams, reversible deploys, and a
strong bias against grand re-architectures. Big-bang rewrites are a
sign earlier evolution failed.

## Audience

- **Engineers** designing services and contracts.
- **Tech leads** evaluating "rewrite vs evolve" proposals.
- **Architecture group** sanity-checking proposals against the
  principle.

## Success criteria

- [ ] Reader can name the evolutionary affordances (backwards
      contracts, additive schema, feature flags, seams, reversible
      deploys).
- [ ] Reader knows big-bang rewrites are an **anti-pattern**, not a
      milestone.
- [ ] Reader can pattern-match "this system is hard to evolve" as
      a design problem.

## Non-goals

- Banning all rewrites (some are unavoidable).
- Defining specific contract or schema versioning schemes.

## Open questions

- How to teach the difference between "evolution" and "drift
  without intent".

## Decision log

- **2026-05-20** — Made **change the design target**, not the
  end-state. Considered target-architecture-driven design;
  rejected because target architectures get outdated before they
  ship.
- **2026-05-20** — Treated big-bang rewrites as **anti-pattern**.
  Considered allowing them as legitimate modernisation; rejected
  because most failed modernisations were big-bang rewrites that
  ran out of runway.

## Sources

- **Internal**
  - [[small-and-simple]] — companion design principle.
  - [[smarts-in-the-nodes]] — companion design principle.
- **External**
  - JLP Engineering Principles, "Evolutionary Systems".
  - Rebecca Parsons et al., *Building Evolutionary Architectures*.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created.
