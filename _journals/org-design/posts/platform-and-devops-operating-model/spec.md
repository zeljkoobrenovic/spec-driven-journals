---
status: draft
revised: 2026-05-20
---

# Spec: Platform and DevOps Operating Model

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that Organization uses a **build-and-run operating model** supported
by platform product teams. DevOps is a **way of working**, not a
separate ticket queue. Stream-aligned teams own their services in
production. Platform and reliability teams provide paved roads,
self-service capabilities, guardrails, and enablement that reduce
cognitive load.

## Audience

- **Product engineering teams** owning build-and-run.
- **Platform teams** providing paved roads.
- **SRE / reliability** supporting incident response.
- **Engineering leadership** sizing platform investment.

## Success criteria

- [ ] Reader knows there is **no separate DevOps team**.
- [ ] Reader can describe platform teams as **product teams**
      serving internal customers.
- [ ] Reader knows stream-aligned teams own their services in
      production.

## Non-goals

- Eliminating reliability expertise — it lives in platform/SRE.
- Replacing on-call responsibility for product teams.

## Open questions

- Where the boundary sits between "self-service paved road" and
  "team customisation".

## Decision log

- **2026-05-20** — Rejected **DevOps as separate team**. Considered
  a central DevOps function; rejected because handoff teams
  recreate Dev-Ops walls.
- **2026-05-20** — Treated platform teams as **product teams**.
  Considered platform-as-service-org; rejected because that strips
  product thinking from platforms.

## Sources

- **Internal**
  - [[team-topologies-operating-model]] — companion vocabulary.
  - [[stream-aligned-product-teams]] — companion record.
  - [[production-ready]] — depends on this operating model.
- **External**
  - Team Topologies (Skelton & Pais).

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
