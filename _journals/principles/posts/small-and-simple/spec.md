---
status: draft
revised: 2026-05-20
---

# Spec: Design Principle — Small (and Not Too Small) and Simple (and Not Too Simple)

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that Organization prefers **small, simple components** over large
clever ones — **but not too small and not too simple**. A component
should be small enough for one team to own end-to-end and simple
enough for one engineer to hold in their head, **and large enough
that the cost of being a separate piece is paid back by the cohesion
it provides**. The principle rejects both monoliths *and* nanoservices.

## Audience

- **Engineers** sizing components in a new design.
- **Tech leads** evaluating "split or consolidate" decisions.
- **Architecture group** preventing both fragmentation and
  monolithification.

## Success criteria

- [ ] Reader knows the principle is **not** "microservices for
      everything".
- [ ] Reader can identify both anti-patterns (oversized monoliths,
      nanoservices).
- [ ] Reader knows smallness has a **cost** (network coordination)
      paid every time pieces interact.

## Non-goals

- Defining a service size threshold.
- Banning monoliths outright.

## Open questions

- Concrete signals that a component is "too small".

## Decision log

- **2026-05-20** — Stated **both extremes** as anti-patterns.
  Considered "smaller is better"; rejected because nanoservices
  cost more than the monolith they replace.
- **2026-05-20** — Tied size to **team ownership**. Considered
  size-by-LOC; rejected because LOC is a poor proxy for cognitive
  load.

## Sources

- **Internal**
  - [[evolutionary-systems]] — companion design principle.
  - [[smarts-in-the-nodes]] — companion design principle.
- **External**
  - JLP Engineering Principles "Small and Simple".
  - Sam Newman on microservices sizing.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created.
