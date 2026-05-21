---
id: "ORG-PRIN-ADVICE-IN-PUBLIC"
status: draft:gray
title: "Practice Principle: Advice in Public"
date: 2026-05-16
author: Organization Tech Strategy
permalink: advice-in-public
timetoread: 12 min
excerpt: "Architecture advice happens in the open at Organization. Decisions are made by teams; the conversations supporting those decisions take place where many people can listen, contribute, and learn. The Architecture Advisory Forum is the standing venue, but the principle is broader: prefer ADRs over private memos, public PR reviews over private feedback, and shared forums over 1-1 escalations. Conversation is a learning multiplier; private advice serves one team, public advice serves the organisation."
tags: practices, advice-process, communication, aaf, learning-organisation, transparency
logo: "assets/images/advice-in-public/logo.jpeg"
logo_credit: "Inspired by Andrew Harmel-Law and the Architecture Advisory Forum"
icon: "assets/icons/advice-in-public.png"
---

> **Status**: DRAFT
>
> **Principle**: Advice that shapes Organization's technical decisions happens **in public**. The default venue is the Architecture Advisory Forum; the default written form is an ADR with reviewable comments; the default conversation is one many people can witness. Private advice is allowed and sometimes necessary, but the bias is toward shared learning. The organisation gets smarter only if many people hear the same conversations.

## Statement

Organization prefers:

* **Public forums over private meetings** for architecture advice.
* **Public ADRs over private memos** for proposals.
* **Public PR reviews over private feedback** for code-level architecture.
* **Open invites over closed lists** for advisory conversations.
* **Documented disagreement over silent dissent.**

Privacy is allowed and sometimes required (personnel, sensitive business, security incidents). The default is public.

## How to Read This Principle

| What it says | What it does **not** say |
| --- | --- |
| The default venue is open. | All conversations must be public. |
| Many people listening is the value. | Many people speaking is the value. |
| Disagreement is documented. | Disagreement must escalate. |
| ADRs and forums are primary. | Slack and 1-1s are forbidden. |
| Public advice creates learning. | Public advice replaces expertise. |

The principle is about *bias*, not absolutism. Some conversations belong in private. Most do not.

## How to Apply This Principle

Use this principle to:

* Explain why public advice creates organisational learning, not just transparency.
* Decide when advice belongs in the AAF, an ADR, a PR, or a private conversation.
* Turn a useful private exchange into a public record without exposing sensitive detail.
* Recognise when private advice is becoming hidden authority.

## Rationale

Private architecture advice has a known failure mode. Two people exchange context, and only two people learn. The next time the same question arises, a different two people repeat the same conversation. Over a year, the organisation rediscovers the same answers dozens of times, each rediscovery costing the time of senior engineers and never producing a durable shared understanding.

Public advice changes the economics:

* One conversation educates many.
* Tacit knowledge becomes visible.
* New joiners ramp by listening, not just by asking.
* Cross-team patterns emerge from exposure, not mandate.
* Disagreements happen openly and are resolved with reasoning.
* The organisation accumulates a shared trail that future decisions can cite.

The Architecture Advisory Forum is the central instance of this principle. It is explicitly *open-invite*, not because every attendee will contribute, but because the audience itself is part of the value.

The principle also reinforces decision ownership. Public advice supports teams that own the decision; private advice tends to look like instruction whether it is intended that way or not.

## Implications

* **AAF is open-invite, weekly, on a stable cadence.** Anyone can attend.
* **Proposed decisions arrive as ADRs.** The text is the starting point for advice.
* **PR comments are reviewed in the open.** Significant architectural feedback goes on the PR, not in DMs.
* **Disagreement is documented.** Dissent shows up in the ADR, the PR, or the forum minutes, not in private channels.
* **1-1 conversations summarise into the public artifact.** If a useful 1-1 advice exchange happens, the outcome is folded into the ADR or PR.
* **Privacy is justified, not assumed.** Personnel, security incidents, sensitive business: yes. Architecture: no.
* **Conversation quality is curated.** Public does not mean low-signal; people who attend are expected to contribute, not just spectate.

## Application Questions

Use this principle whenever advice could change a technical decision or teach more than one team. A useful test is simple: if the same explanation would be valuable to a second team later, the advice should probably leave a public trace.

Ask these questions before keeping advice private:

* Is the topic genuinely confidential, or merely uncomfortable?
* Would another team learn from this reasoning?
* Is the advice likely to become precedent?
* Is a senior person's private opinion being mistaken for authority?
* Can the useful part be summarised in an ADR, PR, or AAF note without exposing sensitive detail?

Public advice does not mean every conversation must happen in a meeting. It means the reasoning that shaped the decision is visible enough for others to inspect, challenge, and reuse.

## What This Means for Teams

For service teams:

* Bring decisions to the AAF as ADRs while advice can still change them.
* Use the forum to gather advice; the decision remains yours.
* Capture advice received - in the ADR, in PR comments, or in linked notes - so the trail is durable.

For senior engineers and architects:

* Default to giving advice in public.
* When you find yourself repeating the same 1-1 advice, raise the pattern in the AAF and write it down.
* Use the public forum to model the behaviour you want others to repeat.

For platform and AI Engineering Enablement roles:

* Make AAF attendance easy and rewarding.
* Capture and link meeting outcomes back into the relevant ADRs.
* Treat the public trail as part of the platform's documentation.

For senior leadership:

* Attend the AAF as a listener. Modelling presence without dominance is itself valuable.
* Resist setting up parallel private forums for "the important decisions"; those undercut the principle.

## Anti-Patterns

* **DM-as-default.** All useful advice happens in private messages; the public artifact is empty.
* **Shadow forum.** A small private group makes the real decisions; the AAF is briefed afterwards.
* **Audience-without-participation.** The forum exists but only three people ever speak.
* **Performance.** Public discussions become performative because everyone is watching; honest disagreement moves to private.
* **Silent dissent.** A senior engineer disagrees in private but stays quiet in public.
* **Permanent privacy.** A topic is treated as sensitive once and never re-opened to the public.
* **Forum theatre.** The AAF runs but the decisions were already made and only the appearance of advice remains.

## Examples

Aligned with the principle:

* A team brings a proposed caching pattern to the AAF, hears advice from several other teams, updates the ADR with what changed.
* A PR comment from a platform engineer about a Kafka topic design becomes the seed for an ADR.
* A senior engineer who is asked the same question repeatedly turns the answer into a markdown record and links to it in future replies.

Out of alignment with the principle:

* A platform decision quietly emerges from a senior architect's private conversations; nobody else can find the rationale.
* AAF attendance shrinks to a closed list of senior engineers because juniors "don't have much to add".
* A team's "consultation" amounts to one DM with one architect.

## Discussion Prompts

Use these prompts in onboarding or team retrospectives:

* Which recent technical conversation should have left a more public trail?
* Where are we using private advice because it is genuinely sensitive, and where are we using it because it is convenient?
* What repeated 1-1 advice should become an ADR, principle, or AAF topic?

## Related Principles

* [[decisions-stay-with-teams]] - public advice supports team-owned decisions.
* [[markdown-records-as-canonical]] - the public trail lives as markdown.
* [[governance-as-code]] - some advice patterns are encoded in checks and templates rather than meetings.
* [[capabilities-follow-ownership]] - public advice prevents tacit knowledge becoming personal capital.

## Scope and Revisiting

This principle applies to architecture advice for Organization's technical decisions: design, integration, platform, tooling, AI configuration, and operating model.

It does not apply to:

* Personnel and performance conversations.
* Security incident response (which has its own forum and confidentiality rules).
* Genuinely confidential commercial or legal topics.
* Internal team retrospectives where psychological safety requires privacy.

The principle should be revisited if:

* AAF attendance and participation drop persistently.
* The volume of architectural decisions outgrows what a single forum can support and the principle needs additional venues.
* Cultural or organisational shifts mean "public" no longer scales the way it does today.

## Authoritative References

* Andrew Harmel-Law, [Scaling the Practice of Architecture, Conversationally](https://martinfowler.com/articles/scaling-architecture-conversationally.html).
* Will Larson, [An Elegant Puzzle: Systems of Engineering Management](https://lethain.com/an-elegant-puzzle/), Stripe Press.
* Organization Foundations, Architecture Advisory Forum ([[architecture-advisory-forum]]).
* John Lewis Partnership, [Engineering Principles](https://engineering-principles.jlp.engineering/).
