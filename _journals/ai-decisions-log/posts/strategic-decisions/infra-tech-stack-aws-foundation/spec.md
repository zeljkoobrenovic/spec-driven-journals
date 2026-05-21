---
status: draft
revised: 2026-05-20
---

# Spec: AWS Foundation — Inherit Central AVIV Group Tooling for 6-12 Months

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Time-bound a decision to **inherit** AVIV Group's central AWS foundation
(Organizations, Control Tower, AFT, access scripts) for the next 6-12
months — and explicitly state that the steady-state is a simpler,
country-delegated, AWS-native foundation. The post should make the
"inherit now, simplify later" framing impossible to misread as a
permanent commitment.

## Audience

- **Cloud and platform engineers** standing up new AWS accounts or
  changing landing-zone configuration in the short term.
- **Architecture group** evaluating exception requests to fork or
  parallel-stand-up tooling.
- **Engineering leadership** sizing the 6-12 month investment.
- **AVIV Group central teams** as the parties whose tooling is
  inherited.

## Success criteria

- [ ] Reader knows the inheritance is **time-bounded**, not permanent.
- [ ] Reader can list the inherited components (Organizations, Control
      Tower, AFT, access scripts).
- [ ] Reader understands what is **not** in scope: workload
      architecture, runtime, compute, messaging.
- [ ] Reader sees the link to [[infra-tech-aws]] (the broader cloud
      decision) and [[infra-tech-stack-networking]] (the networking
      counterpart).
- [ ] The post stays focused as an ADR and does not absorb training,
      account-request checklist, detailed readiness model, or
      implementation-guide content.
- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the decision flow.

## Non-goals

- Deciding workload architecture, runtime, or service-level patterns.
- Forking or replacing the central AVIV Group tooling.
- Committing Organization to follow every future AVIV Group change.
- Defining the steady-state foundation in detail (deferred to a
  later ADR).

## Open questions

- What triggers the "ready to leave inheritance" decision at the end
  of the 6-12 month window — concrete signals, not just dates.
- How much of the access-script custom tooling Organization eventually
  owns vs replaces.

## Decision log

- **2026-05-20** — Refocused the post around the 6-12 month inheritance
  decision, foundation/workload boundary, concrete inheritance-period
  commitments, exception criteria, and revisit triggers. Kept
  terminology as an appendix instead of inline explanation.
- **2026-05-20** — Chose **inheritance** over parallel tooling for the
  6-12 month window. Considered standing up Organization-specific tooling
  immediately; rejected because the migration risk and the cost of
  duplicating in-house tooling exceed the value of early independence.
- **2026-05-20** — Bounded the decision to **6-12 months**.
  Considered an open-ended commitment; rejected because the steady
  state should be simpler and country-delegated, and an open commitment
  drifts toward permanence by default.
- **2026-05-20** — Committed to **no forking** of the central tooling
  during the period. Considered selective forks; rejected because
  forks defeat the cost-saving rationale and create silent divergence.

## Sources

- **Internal**
  - [[infra-tech-aws]] — the broader public-cloud decision this sits
    underneath.
  - [[infra-tech-stack-networking]] — the networking counterpart with
    the same inheritance shape.
  - [[infra-tech-stack-compute]] — the compute decision that builds on
    this foundation.
- **External**
  - AWS Organizations, AWS Control Tower, Account Factory for
    Terraform (AFT) — the AWS-native components inherited.
  - AVIV Group internal documentation on central AWS tooling.

## Changelog

- **2026-05-20** — Rewrote `index.md` into the shorter ADR structure,
  removed checklist/learning-path material, and moved vocabulary to an
  end appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Filled in during second-pass spec rewrite. Status
  still `draft`. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
