---
status: draft
revised: 2026-05-20
---

# Spec: Operational Principle — Production Ready

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that an Organization service is **Production Ready** when it can be
operated safely and recoverably by the team that owns it. Checked
against an explicit list, signed off by the owning team, refreshed on
a cadence. Services that fail the list do not receive production
traffic regardless of feature completeness. Production-readiness is a
property of the **service**, not a stage in a release plan.

## Audience

- **Engineers** taking a service to production.
- **Tech leads** signing off on production-readiness.
- **On-call team** depending on services that have passed the bar.

## Success criteria

- [ ] Reader knows production-readiness is **service-level**, not
      release-level.
- [ ] Reader can name the checklist items (ownership, observability,
      health checks, secrets, deploy/rollback, capacity, on-call,
      runbooks, security, data protection).
- [ ] Reader knows failing services don't get traffic regardless of
      feature completeness.

## Non-goals

- Defining the exact checklist contents (those evolve over time).
- Replacing security review.

## Open questions

- How to handle services where one item is genuinely
  not-applicable.

## Decision log

- **2026-05-20** — Made it a **property of the service**, not a
  release stage. Considered making it a release gate; rejected
  because services live longer than releases and need ongoing
  production-readiness.
- **2026-05-20** — Required a **refresh cadence**. Considered
  one-time sign-off; rejected because services drift out of
  readiness over time.

## Sources

- **Internal**
  - [[observable-by-default]] — companion operational principle.
- **External**
  - JLP Engineering Principles "Production Ready".
  - SRE Book — service-readiness checklists.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created.
