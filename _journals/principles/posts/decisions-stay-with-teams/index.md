---
id: "ORG-PRIN-DECISIONS-STAY-WITH-TEAMS"
status: draft:gray
title: "Organisation Principle: Decisions Stay with Teams"
date: 2026-05-16
author: Organization Tech Strategy
permalink: decisions-stay-with-teams
timetoread: 12 min
excerpt: "Technical decisions at Organization are owned by the team that will operate the result. Centralised approval boards are not the model. Teams seek advice from the people most affected and most expert through an Advice Process, document the decision in an ADR, and remain accountable for the consequences. The Architecture Advisory Forum exists to make those conversations easier, not to approve work. Ownership of the decision is what makes the team accountable for the outcome."
tags: organisation, advice-process, ownership, governance, accountability, adr
logo: "assets/images/decisions-stay-with-teams/logo.jpeg"
logo_credit: "Inspired by Andrew Harmel-Law and the Advice Process"
icon: "assets/icons/decisions-stay-with-teams.png"
---

> **Status**: DRAFT
>
> **Principle**: Technical decisions are owned by the team that will operate the result. Teams seek advice through a written Advice Process, document outcomes in ADRs, and remain accountable for the consequences. Other roles - architects, platform teams, security, senior leadership - offer advice. Nobody approves on behalf of the team. Boards and forums (including the AAF) exist to support conversations, not to replace ownership.

## Statement

Organization's decision model is:

* **Each technical decision has an owning team.**
* **The owning team seeks advice** from those affected and those with relevant expertise.
* **The owning team decides.** Advice is taken seriously; advice is not authority.
* **The decision is documented in an ADR**, including the advice received.
* **The owning team is accountable for the consequences**, including revisiting the decision if reality teaches something new.

This applies to architecture, technology choices, integration patterns, operational decisions, and significant trade-offs in delivery.

## How to Read This Principle

| What it says | What it does **not** say |
| --- | --- |
| The owning team decides. | One person on the team decides alone. |
| Advice must be sought. | Advice must be followed. |
| Decisions are written down. | Documentation comes after the deploy. |
| Forums exist to advise. | Forums approve. |
| Accountability sits with the team. | The team is on its own. |

The principle pushes decision-making to the people who run the outcome. It does not reduce the responsibility of architects, platform owners, or senior engineers; it changes their role from "approver" to "advisor".

## How to Apply This Principle

Use this principle to:

* Explain the difference between advice, authority, ownership, and accountability.
* Identify the team that should own a technical decision.
* Use the Advice Process without turning it into an approval queue.
* Document disagreement without treating disagreement as a veto.

## Rationale

Centralising decisions creates predictable failure modes:

* **Bottlenecks**: decisions queue at the board faster than the board can review.
* **Detachment**: the people approving are not the people who operate the result.
* **Theatre**: review meetings become rubber-stamp processes once the queue grows.
* **Reduced ownership**: teams stop deciding; they prepare submissions.
* **Lost feedback**: the board never sees the consequences of its decisions at the timescale that matters.

The Advice Process keeps the decision with the team that owns the outcome. It also forces explicit advice-seeking, which is the actual value of a review board done well - cross-team perspective, expertise from other domains, awareness of constraints. The advice still happens; it just no longer pretends to be authority.

This principle directly enables the Architecture Advisory Forum decision: the AAF works because decisions stay with teams. If the AAF began approving or blocking, the principle would be broken and the forum would collapse into a traditional review board.

## Implications

* **A decision has a named owning team.** Not a "DRI" alone; a team that will operate the consequences.
* **The Advice Process is the default decision-making pattern.** Mandatory advice list, written ADR, conscious decision.
* **ADRs include the advice received.** Not as transcripts, but as a clear record of what was considered.
* **Disagreement is documented.** A dissenting voice deserves a paragraph in the record, not silence.
* **Forums advise, never approve.** AAFs, working groups, and review meetings exist for shared learning and broader advice.
* **Decisions can be revisited.** Reality is a legitimate reason to change a decision; the original owner usually leads the revisit.
* **Some decisions need explicit guardrails** (legal, regulatory, security). Those guardrails are *constraints* on the decision, not approvals of it.

## Decision Ownership Test

Before a significant decision is accepted, the owning team should be easy to name. If it is not, the decision is not ready.

Use this test:

* Which team will operate the result in production?
* Which team will receive the pager, support request, or cost report if it fails?
* Which team can change the decision later without waiting for a central board?
* Which affected people and expert people have been asked for advice?
* Where is dissent recorded?
* What evidence would cause the owning team to revisit the decision?

If different answers appear for "who decides", "who operates", and "who pays the consequences", the ownership boundary is wrong. Resolve that before arguing about the technical option.

## What This Means for Teams

For service teams:

* Identify the owning team for each significant decision.
* Use the Advice Process: name affected people and experts, seek their input, write the ADR.
* Make decisions without waiting for permission once advice has been sought.
* Revisit decisions when evidence changes.

For platform and architecture roles:

* Offer advice. Bring expertise, prior art, and broader context.
* Do not approve. Do not block.
* If a decision concerns you, write your concern down where the team will read it.

For senior leadership:

* Resist the urge to formalise approval boards.
* When a team makes a decision you would not have made, ask what advice they sought before overriding.
* Protect the Advice Process; do not bypass it through informal channels.

For security, data, compliance, and similar functions:

* Express constraints clearly so teams can incorporate them.
* Distinguish "this is a hard constraint" from "this is my preference" in advice.

## Anti-Patterns

* **Approval boards in disguise.** Forums renamed to "advisory" while still issuing decisions.
* **Advice-as-veto.** Senior voices treating advice as authority and overriding teams quietly.
* **No-advice decisions.** Teams making decisions in isolation and discovering affected parties later.
* **Documentation theatre.** ADRs written after the deploy to justify what already happened.
* **Owner-less decisions.** Significant choices that no team will admit to owning.
* **Bypass via Slack.** Approvals flowing through informal channels with no record.
* **Architect-as-decider.** A senior architect's preference treated as Organization policy without an ADR.

## Examples

Aligned with the principle:

* A service team proposes adopting a new caching pattern, brings it to the AAF, takes the advice, writes the ADR, deploys.
* A platform team's recommendation is recorded in an ADR as advice; the service team chooses a different approach, with reasons.
* A security concern is recorded as a constraint in the ADR; the team designs around it.

Out of alignment with the principle:

* A central architect's slide deck becomes the de facto pattern with no ADR or team ownership.
* The AAF starts producing "approved" labels in meeting notes.
* A team builds a service without seeking advice from the platform team that will operate parts of it.

## Discussion Prompts

Use these prompts in onboarding or AAF preparation:

* Who owns the next significant decision, and who will operate the consequences?
* Which advice has been sought, and which affected people are still missing?
* Where might we be confusing senior advice with decision authority?

## Related Principles

* [[advice-in-public]] - the AAF makes advice-seeking visible.
* [[markdown-records-as-canonical]] - decisions live in ADRs.
* [[capabilities-follow-ownership]] - decisions and capabilities both follow team ownership.
* [[tooling-explicit-and-reversible]] - tooling decisions are also team-owned within the standard frame.

## Scope and Revisiting

This principle applies to all technical decisions at Organization that have meaningful operational, architectural, or cross-team impact.

It does not apply to internal team choices that affect only one team's day-to-day work (for example, coding style choices inside a single repository), nor to decisions that legal, regulatory, or security obligations have already constrained from the outside.

The principle should be revisited if:

* The Advice Process becomes a bottleneck on its own (advice-seeking takes longer than the decision warrants).
* Repeated incidents tied to team-owned decisions reveal a category that needs central control.
* The organisation grows or splits in a way that requires a new shape for cross-team decisions.

## Authoritative References

* Andrew Harmel-Law, [Scaling the Practice of Architecture, Conversationally](https://martinfowler.com/articles/scaling-architecture-conversationally.html).
* Andrew Harmel-Law, [Architecture Advice Process](https://martinfowler.com/articles/scaling-architecture-conversationally.html#TheArchitectureAdviceProcess).
* MADR, [Markdown Architectural Decision Records](https://adr.github.io/madr/).
* Organization Foundations, Architecture Advisory Forum ([[architecture-advisory-forum]]).
