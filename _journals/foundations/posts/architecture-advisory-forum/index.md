---
id: "ORG-FOUND-ARCHITECTURE-ADVISORY-FORUM"
status: draft:gray
title: "Architecture Advisory Forum as a Standing Advice Ritual"
date: 2026-05-16
author: Organization Tech Strategy
permalink: architecture-advisory-forum
timetoread: 13 min
excerpt: "Organization will run a weekly Architecture Advisory Forum as the standing place for cross-team architecture advice. The forum does not approve or own decisions. It helps teams expose options early, improve ADRs, revisit decisions with evidence, and learn from shared engineering signals."
tags: architecture, advice-process, governance, decision-making, learning-organisation, adr
logo: "assets/images/architecture-advisory-forum/logo.jpeg"
logo_credit: "Inspired by Andrew Harmel-Law, 'Scaling the Practice of Architecture, Conversationally'"
icon: "assets/icons/architecture-advisory-forum.png"
---

> **Status**: DRAFT
>
> **Decision**: Organization will run a weekly Architecture Advisory Forum (AAF) as the standing ritual for cross-team architecture advice. The AAF is not an Architecture Review Board. It does not approve, reject, or own decisions. Decisions remain with the accountable team or individual. The forum creates a reliable place to test options early, improve decision records, revisit decisions with evidence, and build shared architecture judgment.

## Decision

Adopt a weekly **Architecture Advisory Forum** for architecture advice and organisational learning.

| Element | Decision |
| --- | --- |
| Cadence | Weekly, one hour, at a stable time. |
| Authority | Advisory, not approval-based. |
| Decision ownership | Stays with the team or person making the decision. |
| Inputs | Spikes, proposed ADRs, revisits, risks, metrics, and cross-team constraints. |
| Outputs | Advice, recorded concerns, follow-up questions, links, and clearer decision records. |
| Default behaviour | Discuss in public unless confidentiality, security, legal, or people concerns require a smaller setting. |

The forum exists because architecture decisions are better when teams can ask for advice before they are locked in.

## How to Read This Decision

The AAF changes the venue for advice, not the ownership of decisions.

| It is | It is not |
| --- | --- |
| A recurring advice ritual. | An approval board. |
| A place to expose trade-offs early. | A late-stage gate. |
| A way to teach architecture reasoning in public. | A substitute for team accountability. |
| A way to improve ADRs and principles. | A place for status reporting. |
| A learning loop across teams. | A central architecture command channel. |

If a team leaves the forum with sharper options, clearer risk language, and better evidence, the forum worked even when no one agreed on a single answer.

## Operating Model

The AAF has five recurring modes:

| Mode | Purpose | Typical output |
| --- | --- | --- |
| **Spike preview** | Test a question before a team spends time investigating. | Better spike framing and likely evidence sources. |
| **Proposed decision** | Improve an ADR before it becomes accepted. | Concrete advice and recorded trade-offs. |
| **Decision revisit** | Check whether an accepted decision still holds. | Keep, amend, supersede, or schedule evidence collection. |
| **Shared signals** | Read metrics, incidents, cost, reliability, or delivery data in context. | Learning themes and possible record updates. |
| **Exception review** | Discuss justified divergence from a standard. | Documented exception or path back to the standard. |

The forum should prefer fewer topics with better discussion over a full agenda with shallow handling.

## Advice Process

The AAF follows the Advice Process:

1. The decision maker frames the decision, options, and constraints.
2. People affected by the decision give advice.
3. People with relevant expertise give advice.
4. The decision maker records the advice and decides.
5. The decision record links back to the discussion when appropriate.

Advice is not consensus. A team may choose an option after hearing objections, but the record should show that the objections were heard and why the chosen trade-off still makes sense.

## What Good Advice Sounds Like

Good advice is specific, evidence-seeking, and owned:

| Weak advice | Better advice |
| --- | --- |
| "This feels risky." | "The risk is operational ownership: who will page on this after launch?" |
| "Use the standard." | "The standard applies unless you can show latency or data-residency constraints that break it." |
| "We tried this before." | "In 2024 this failed because ownership was split; here is the incident link." |
| "I disagree." | "I would choose option B because it keeps rollback independent from the migration." |

The most useful advice names the constraint, the evidence, and the consequence.

## Standing Agenda

A simple agenda is enough:

1. **New questions**: spikes or decisions that need early advice.
2. **Decision records**: proposed ADRs, exceptions, or important revisions.
3. **Revisits**: decisions with new evidence, incidents, cost shifts, or repeated exceptions.
4. **Shared signals**: metrics or patterns that imply a standards or principle update.
5. **Actions**: owners, record updates, and next discussion dates.

The agenda should stay lightweight. Detailed facilitation scripts, templates, and training material belong in a playbook, not in this decision.

## Roles

| Role | Responsibility |
| --- | --- |
| **Decision maker** | Brings the question, owns the final decision, updates the record. |
| **Facilitator** | Keeps the conversation on advice, options, evidence, and next actions. |
| **Recorder** | Captures advice, concerns, links, and follow-up items. |
| **Advisers** | Offer expertise or affected-party perspective without taking over ownership. |
| **Curators** | Improve the resulting records without changing the decision meaning. |

Participants should come prepared to help the decision maker think, not to win the room.

## Records and Follow-Up

Every material topic should leave a trace:

* a linked ADR, foundation, principle, strategy, or discussion record;
* a short summary of advice received;
* named follow-up owners when evidence is missing;
* clear status when a decision is accepted, proposed, superseded, or abandoned.

The forum does not replace durable writing. It improves it.

## What This Means for Teams

* Bring decisions early, while options are still real.
* Bring evidence, not only preference.
* Use the forum for cross-team impact, standards exceptions, and decisions likely to be copied.
* Do not wait for forum approval to make ordinary team-local decisions.
* Update the record after the conversation; otherwise the learning disappears.

## Anti-Patterns

* **Approval theatre.** Teams present finished decisions and wait for a stamp.
* **Architecture veto.** Senior people use the forum to take ownership away from teams.
* **Status meeting drift.** The agenda becomes progress reporting instead of decision advice.
* **Private architecture.** Important trade-offs happen in side channels and the forum only sees the result.
* **Advice without records.** Good discussion disappears because no ADR or follow-up captures it.
* **Metric blame.** Shared signals are used to rank teams rather than understand system constraints.

## Success Indicators

The AAF is working when:

* teams bring questions before they are locked in;
* ADRs mention real alternatives, trade-offs, and advice received;
* repeated exceptions trigger principle or standard updates;
* cross-team dependencies become visible earlier;
* decisions are revisited with evidence instead of opinion;
* teams still feel accountable for their own decisions.

## Scope and Revisiting

This decision applies to architecture-relevant choices with cross-team impact, standards implications, meaningful risk, or durable learning value.

Out of scope:

* routine code-level design decisions owned by a team;
* people-management decisions;
* incident command during active incidents;
* confidential security, legal, vendor, or HR matters that need a smaller setting.

Revisit the forum design after two quarters, or earlier if it becomes an approval gate, loses attendance from affected teams, or stops producing useful record updates.

## Related Records

* [[markdown-records]] — the durable format for decisions discussed in the forum.
* [[curator-role]] — the editorial role that keeps records coherent after discussions.
* [[decisions-stay-with-teams]] — the principle that decision ownership remains with teams.
* [[advice-in-public]] — the principle behind visible advice and record-linked discussion.

## Authoritative References

* Andrew Harmel-Law, *Scaling the Practice of Architecture, Conversationally*
* Team Topologies writing on enabling teams and interaction modes
* Advice Process writing from consent-based and decentralized decision-making traditions

## Appendix: Vocabulary

| Term | Meaning |
| --- | --- |
| **AAF** | Architecture Advisory Forum, the weekly advice ritual. |
| **Advice Process** | A decision maker seeks advice from affected people and experts before deciding. |
| **Decision maker** | The accountable person or team that owns the final decision. |
| **Adviser** | A participant who contributes expertise or affected-party perspective. |
| **Revisit** | A structured check of an earlier decision against new evidence. |
| **Exception** | A documented, justified divergence from an accepted standard or principle. |
