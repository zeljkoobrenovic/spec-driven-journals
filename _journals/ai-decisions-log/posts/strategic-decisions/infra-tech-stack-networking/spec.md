---
status: draft
revised: 2026-05-20
---

# Spec: AWS Networking — Inherit Central Tooling, Simplify Deliberately

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Time-bound an inheritance of AVIV Group's central AWS networking setup
(VPCs, subnets, transit, DNS, perimeter, inter-account connectivity) for
the next 6-12 months, and commit to **deliberate simplification** during
that window: account consolidation (from ~200 to a smaller set),
internet-vs-internal traffic separation, and an evaluation of VPC
Lattice + ECS Service Connect as simpler service-to-service patterns.

## Audience

- **Cloud engineers** building or changing network configuration.
- **Architecture group** evaluating exceptions to inherited topology.
- **Platform team** owning the account-consolidation programme.
- **Engineering leadership** sizing the simplification investment.

## Success criteria

- [ ] Reader knows the inheritance is **time-bounded** at 6-12 months.
- [ ] Reader can name the four simplification fronts: direct control,
      account consolidation, internet/internal split, VPC Lattice
      evaluation.
- [ ] Reader knows non-trivial topology changes flow through AVIV
      Group, not Organization.
- [ ] Reader sees the parallel with [[infra-tech-stack-aws-foundation]]
      — same inheritance shape, different layer.
- [ ] The post stays focused as an ADR and does not absorb detailed
      request checklist, troubleshooting guide, or implementation
      playbook content.
- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the decision flow.

## Non-goals

- Workload-level networking decisions that do not change foundation
  topology.
- Forking or replacing AVIV Group's custom networking tooling during
  the period.
- Committing to a specific post-inheritance network topology in
  detail.

## Open questions

- Concrete target for "smaller set of key accounts" — how many,
  grouped how.
- Decision criteria for the VPC Lattice + ECS Service Connect
  evaluation.

## Decision log

- **2026-05-20** — Refocused the post around the 6-12 month inheritance
  decision, network/workload boundary, simplification commitments,
  operating guardrails, exception criteria, and revisit triggers. Kept
  terminology as an appendix instead of inline explanation.
- **2026-05-20** — Chose **inheritance** for the 6-12 month window.
  Considered an immediate Organization-specific network design; rejected
  because the migration cost exceeds the inheritance cost in the short
  term.
- **2026-05-20** — Committed to **four explicit simplification
  fronts**. Considered framing simplification as a goal without
  specifics; rejected because vague goals don't progress.
- **2026-05-20** — Targeted **account consolidation** from ~200
  accounts. Considered leaving the count alone; rejected because many
  cross-account networking problems disappear simply by having fewer
  accounts.

## Sources

- **Internal**
  - [[infra-tech-aws]] — the broader cloud decision.
  - [[infra-tech-stack-aws-foundation]] — the foundation counterpart
    with the same inheritance shape.
- **External**
  - Amazon VPC Lattice documentation.
  - ECS Service Connect documentation.
  - AVIV Group internal networking documentation.

## Changelog

- **2026-05-20** — Rewrote `index.md` into the shorter ADR structure,
  removed request/troubleshooting/checklist material, and moved
  vocabulary to an end appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Filled in during second-pass spec rewrite. Status
  still `draft`. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
