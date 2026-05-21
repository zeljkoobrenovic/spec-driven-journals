---
status: draft
revised: 2026-05-20
---

# Spec: Organisation Principle — Decisions Stay with Teams

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that technical decisions at Organization are **owned by the team
that will operate the result**. No centralised approval boards. Teams
seek advice through the Advice Process, document in ADRs, and remain
accountable. The Architecture Advisory Forum supports conversations,
not approvals.

## Audience

- **Teams** owning technical decisions.
- **Architects, platform teams, security, senior leadership** as
  advisors, not approvers.
- **New joiners** orienting to the decision model.

## Success criteria

- [ ] Reader knows decisions are **team-owned**, not approved by a
      board.
- [ ] Reader knows the Advice Process is mandatory; the approval
      isn't.
- [ ] Reader sees [[architecture-advisory-forum]] as a venue for
      conversation, not approval.

## Non-goals

- Eliminating senior advice or expertise input.
- Replacing the AAF.

## Open questions

- How to handle decisions that genuinely cross multiple teams with
  no natural owner.

## Decision log

- **2026-05-20** — Chose **team ownership** over centralised
  approval. Considered an Architecture Review Board; rejected
  because approval boards detach accountability from operation.
- **2026-05-20** — Made **advice mandatory, approval not**.
  Considered making it fully team-discretionary; rejected because
  without an Advice Process, important context goes unheard.

## Sources

- **Internal**
  - [[architecture-advisory-forum]] — the standing forum.
  - [[advice-in-public]] — companion practice principle.
- **External**
  - Andrew Harmel-Law, *Facilitating Software Architecture* —
    the Advice Process source.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created.
