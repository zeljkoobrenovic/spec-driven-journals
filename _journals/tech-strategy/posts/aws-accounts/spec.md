---
status: draft
revised: 2026-05-20
---

# Spec: AWS Account Blueprint and Consolidation Plan

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

State the **default principles** for AWS account usage in Organization
Germany (inherit AVIV central guidance, central networking,
account-on-justification with named owner/purpose/lifecycle) and the
**consolidation plan** moving roughly 200 accounts toward a governable
estate. The account estate is one of the clearest visible signs of
structural fragmentation in [[diagnosis]] and the most legible
candidate for visible simplification progress.

## Audience

- **Cloud and platform engineers** creating or auditing accounts.
- **Domain owners** of accounts targeted for consolidation.
- **FinOps and security** evaluating consolidation outcomes.
- **Engineering leadership** sizing the consolidation programme.

## Success criteria

- [ ] Reader can decide whether to create a new AWS account using
      the three justifications (ownership, isolation, compliance).
- [ ] Reader knows every account needs **explicit owner, purpose,
      lifecycle status**.
- [ ] Reader can name the three first-wave consolidation focuses:
      unclear-ownership/purpose, transitional-permanent,
      duplicated-environment.
- [ ] Reader understands ~200 is the starting point, not the steady
      state.

## Non-goals

- Germany-specific foundation divergence in the initial phase.
- Workload-level architecture inside accounts.
- Decentralised networking decisions.
- A target account count number (deferred until consolidation
  evidence arrives).

## Open questions

- How to handle the account-as-archaeology problem when original
  owners have left.
- Concrete target count for the post-consolidation estate.

## Decision log

- **2026-05-20** — Kept **central networking** in the initial phase.
  Considered Germany-specific networking; rejected because it would
  multiply the consolidation problem during the period when
  simplification is the goal.
- **2026-05-20** — Required **owner, purpose, lifecycle** for every
  account. Considered making this best-effort; rejected because the
  account-as-archaeology problem is exactly what unowned accounts
  produce.
- **2026-05-20** — Started consolidation with **unclear-ownership
  accounts**. Considered starting with biggest-cost accounts;
  rejected because cost-first consolidation hits production accounts
  that are working fine.

## Sources

- **Internal**
  - [[diagnosis]] — the AWS account fragmentation evidence.
  - [[policy]] — the account-creation policy this blueprint
    operationalises.
  - [[infra-tech-stack-aws-foundation]] — the foundation this builds
    on.
  - [[aws-naming-tagging]] — the naming and tagging conventions.
- **External**
  - AWS Organizations and account-vending best practices.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
