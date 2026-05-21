---
status: draft
revised: 2026-05-20
---

# Spec: Architecture as Advice and Guardrails

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that Organization runs architecture as **advice, learning, and
reusable guardrails** — not as a central approval board. Teams own
architecture decisions inside their boundaries. Architects, staff-plus
engineers, platform owners, security, and affected teams provide
advice. Guardrails encoded in principles, golden paths, templates,
automation, and ADRs.

## Audience

- **Architects and staff-plus engineers** offering advice.
- **Stream-aligned teams** owning architecture decisions.
- **Platform owners** building guardrails.
- **New joiners** learning the architecture operating model.

## Success criteria

- [ ] Reader knows teams own decisions, not architects.
- [ ] Reader can identify what counts as a "guardrail".
- [ ] Reader sees the rejection of approval-board architecture.

## Non-goals

- Removing senior input or expertise.
- Defining specific architecture standards.

## Open questions

- Where to draw the boundary when a decision crosses teams.

## Decision log

- **2026-05-20** — Chose **advice + guardrails** over approval
  board. Considered an ARB; rejected because approval boards detach
  accountability from delivery.

## Sources

- **Internal**
  - [[decisions-stay-with-teams]] — companion principle.
  - [[architecture-advisory-forum]] — the standing advice venue.
  - [[advice-in-public]] — companion practice principle.
- **External**
  - Andrew Harmel-Law, *Facilitating Software Architecture*.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
