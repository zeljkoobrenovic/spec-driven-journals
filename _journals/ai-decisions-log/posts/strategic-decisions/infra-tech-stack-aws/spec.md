---
status: draft
revised: 2026-05-20
---

# Spec: Public Cloud — Consolidate on AWS via AVIV Group Contract

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Commit Organization to **AWS as its strategic public cloud** and consolidate
backend workloads under AVIV Group's existing AWS commercial contract.
Make three distinct choices visible: provider (AWS), commercial
(inheriting AVIV's contract), operating-model (delegate non-differentiating
cross-cutting work to AVIV's central functions). Each is separately
revisitable.

## Audience

- **Engineering leadership** evaluating cloud strategy.
- **Architecture group** ensuring workload-level architecture stays
  owned by Organization.
- **FinOps and procurement** seeing where the commercial line sits.
- **Workload teams** that need to know workload-level decisions stay
  with them.

## Success criteria

- [ ] Reader can separate **provider**, **commercial**, and
      **operating-model** choices — three distinct ideas, not one.
- [ ] Reader knows Organization does not negotiate its own AWS master
      contract.
- [ ] Reader knows workload architecture, security posture, and
      product roadmap stay with Organization.
- [ ] Reader can trace this as the starting point that
      [[infra-tech-stack-aws-foundation]] and downstream ADRs build on.
- [ ] The post stays focused as an ADR and does not absorb service
      selection, FinOps process, or workload-design guidance.
- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the decision flow.

## Non-goals

- Multi-cloud strategy or future cloud-provider changes.
- Workload-level architecture, security posture, or service
  decisions.
- Defining what "non-differentiating cross-cutting work" includes in
  full detail.
- Committing Organization to follow every future AVIV Group cloud decision.

## Open questions

- What signals would trigger an Organization-specific commercial
  relationship outside AVIV's contract.
- How the FinOps boundary works in practice (AVIV baseline vs
  workload-level decisions).

## Decision log

- **2026-05-20** — Refocused the post around provider choice,
  commercial model, responsibility boundary, exception criteria, and
  revisit triggers. Kept terminology as an appendix instead of inline
  explanation.
- **2026-05-20** — Chose **AWS** as the strategic public cloud.
  Considered multi-cloud and Azure; rejected because the inherited
  AWS surface already exists and a parallel cloud would multiply cost
  and complexity for no clear product gain.
- **2026-05-20** — Inherited **AVIV Group's commercial contract**
  rather than negotiating independently. Considered an independent
  Organization contract; rejected because AVIV's scale unlocks better
  unit costs and EDP terms that an independent Organization could not.
- **2026-05-20** — Delegated **non-differentiating cross-cutting
  work** (procurement, baseline FinOps, AWS relationship) to AVIV
  Group. Considered building all of these in-house; rejected because
  they are not where Organization creates product value.

## Sources

- **Internal**
  - [[infra-tech-stack-aws-foundation]] — the foundation decision
    that builds on this commercial choice.
  - [[infra-tech-stack-networking]] — the networking counterpart.
  - [[infra-tech-stack-compute]] — the compute target.
  - [[infra-tech-stack-messaging]] — the messaging target on MSK.
- **External**
  - AWS Enterprise Discount Program and consolidated billing model.
  - AVIV Group AWS commercial agreement (referenced, not public).

## Changelog

- **2026-05-20** — Rewrote `index.md` into the shorter ADR structure
  and moved cloud vocabulary to an end appendix. *(Zeljko,
  AI-mediated session)*
- **2026-05-20** — Filled in during second-pass spec rewrite. Status
  still `draft`. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
