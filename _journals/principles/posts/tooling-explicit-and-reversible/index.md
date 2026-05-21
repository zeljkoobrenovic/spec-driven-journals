---
id: "ORG-PRIN-TOOLING-EXPLICIT-AND-REVERSIBLE"
status: draft:gray
title: "Organisation Principle: Tooling Decisions Are Explicit and Reversible"
date: 2026-05-16
author: Organization Tech Strategy
permalink: tooling-explicit-and-reversible
timetoread: 12 min
excerpt: "Pick tools deliberately, write down why, plan how to leave. Organization's tooling decisions - Claude Code as the AI default, .NET as the backend default, ECS as compute, MSK as messaging - are dated and reviewable, not eternal. A reversible tooling decision is one whose context, scope, and exit path are explicit enough that the next review can compare evidence to a stated frame, not to taste."
tags: organisation, tooling, ai, reversibility, governance, review-cadence
logo: "assets/images/tooling-explicit-and-reversible/logo.jpeg"
logo_credit: "Inspired by Organization's AI tooling decision and Dan McKinley's Choose Boring Technology"
icon: "assets/icons/tooling-explicit-and-reversible.png"
---

> **Status**: DRAFT
>
> **Principle**: Organization's tooling decisions are made explicitly, documented as ADRs, and reviewed on a cadence. They are reversible: each decision includes the conditions under which it would be revisited and the practical steps for moving away. Tooling is a platform choice, not a permanent identity. Explicitness and reversibility together make tooling defensible without being defensive.

## Statement

Every shared tooling decision at Organization has:

* **A named default.** Claude Code for AI coding. .NET for backend services. ECS Fargate for compute. MSK for messaging. AWS for cloud.
* **An ADR**. Decision, drivers, considered options, consequences.
* **A review cadence.** Typically six months for AI tooling; longer for slower-moving stacks.
* **An exit path.** What would change the decision; what migration would look like.
* **An exception process.** How a team can deviate, with a recorded reason.

A tooling decision is "good" when the next review can compare it to evidence against a stated frame, not when it lasts forever.

## How to Read This Principle

| What it says | What it does **not** say |
| --- | --- |
| Decisions are dated. | Decisions are temporary by nature. |
| Reviews happen on a cadence. | Reviews happen continuously. |
| Reversibility is designed in. | Reversibility means cheap. |
| Defaults exist. | Defaults are mandatory. |
| Exceptions are allowed. | Exceptions are the norm. |

The principle is about making tooling decisions *defensible by frame*, not *defensible by fashion*.

## How to Apply This Principle

Use this principle to:

* Explain why tooling decisions need a decision frame, review date, and exit path.
* Compare tooling evidence against the original ADR instead of personal preference.
* Identify lock-in honestly without treating all lock-in as unacceptable.
* Distinguish confirming, narrowing, replacing, or retiring a tooling default.

## Rationale

Tooling decisions are some of the easiest to make badly and some of the hardest to revisit:

* They feel permanent because they shape teams' day-to-day work.
* They acquire emotional attachment quickly (especially developer tools).
* They embed into hiring, training, and platform engineering investments.
* They produce sunk costs that resist reversal.

Without explicit frames, tooling debates become preference fights. With them, the conversation has somewhere to land: "according to the ADR, the decision is for these reasons, with this review date, and these exit conditions; here is the evidence we should examine."

Organization's AI tooling decision makes this concrete. Claude Code is the default for 2026. The decision is dated, paired with a six-month review cycle, and explicitly framed as a platform choice rather than a model choice. Codex, Gemini, and others remain available by exception when they fit specific workflows. Each piece is part of being explicit and reversible.

## Implications

* **A tooling decision is an ADR, not an announcement.** The ADR includes context, drivers, options, decision, and consequences.
* **Review dates are real.** Six-month reviews for fast-moving tooling (AI), longer for slower-moving (cloud, language).
* **Exit paths are designed.** "If we change our mind, here is what would have to happen" is part of the ADR.
* **Lock-in is acknowledged, not denied.** If a tool creates significant lock-in, the ADR says so, and the trade-off is accepted explicitly.
* **Exception process is documented.** Teams can request to use a non-default tool, with an ADR.
* **Reviews compare evidence to the original frame.** "Did the assumptions hold? Did costs land where expected? Did the trade-offs play out?"
* **Reversal is a real option in reviews.** A review that cannot end in reversal is not a review.

## Reversibility Test

A tooling ADR should make reversal thinkable even when reversal is expensive.

Ask:

* What data, code, workflow, or training becomes coupled to this tool?
* Which teams would have to change behaviour if the decision reversed?
* What export, migration, compatibility, or parallel-run path exists?
* Which assumptions should be checked at the next review?
* What evidence would narrow the tool's scope rather than fully replace it?
* What would make the tool a default, an exception, or a deprecated choice?
* Who owns the review and the migration plan if reversal becomes necessary?

Reversibility does not mean every decision is cheap to undo. It means the organisation knows what undoing would require before the decision becomes identity.

## What This Means for Teams

For service teams:

* Read the ADR before choosing tools for a new project.
* Use the default unless you can write a useful exception.
* Treat the next review as input: bring evidence, not opinions.

For platform and architecture roles:

* Maintain the tooling ADRs. Keep them current.
* Schedule reviews. Run them. Publish the outcomes.
* Track the evidence: usage, cost, satisfaction, productivity signals.

For tech leads:

* When a tooling change is proposed, ask for the ADR.
* When a review approaches, gather the team's lived experience as input.

For senior leadership:

* Resist the urge to change a tooling decision outside its review cadence.
* Protect the review cadence; it is the principle's main defence against drift.

## Anti-Patterns

* **Tooling-by-announcement.** A decision is communicated in slides with no ADR.
* **Eternal commitment.** No review date; the decision becomes a tradition.
* **Lock-in denial.** "We can switch easily" said about a tool that has shaped six months of platform work.
* **Exception soup.** Exceptions granted in Slack and accumulated until exceptions outnumber the default.
* **Vanity reversal.** Reversal driven by hype, not evidence.
* **Vanity persistence.** Persistence driven by sunk-cost, not evidence.
* **Review theatre.** A meeting where the outcome was decided in advance.

## Examples

Aligned with the principle:

* Claude Code is adopted as the 2026 default AI tool, in an ADR, with a six-month review cycle.
* .NET is adopted as the default backend platform with an ADR explaining drivers and trade-offs.
* A team uses Codex by exception for a specific narrow workflow; the exception is recorded.
* The six-month AI review evaluates evidence and either confirms, narrows, or reverses the decision.

Out of alignment with the principle:

* "We're standardising on tool X" announced without an ADR.
* A team adopts a new database engine because the maintainer gave a good talk.
* A review skipped because "the decision is obviously still right".
* An ADR that explicitly says "this is irreversible".

## Discussion Prompts

Use these prompts during tooling reviews:

* Which original assumption has the strongest evidence for or against it now?
* What would we do differently if we were making this decision today?
* Are we keeping the tool because it still wins, or because switching feels hard?

## Related Principles

* [[standardize-before-diverging]] - tooling defaults are the most visible standards.
* [[markdown-records-as-canonical]] - tooling decisions live as ADRs.
* [[decisions-stay-with-teams]] - tooling decisions, like other decisions, are owned not approved.
* [[ai-output-must-be-governed]] - AI tooling decisions carry specific governance obligations.

## Scope and Revisiting

This principle applies to Organization's shared tooling: developer tools, AI coding tools, languages, runtimes, cloud, messaging, observability, CI/CD, repositories, and similar.

It does not apply to tooling chosen inside one team that has no operational footprint outside it (for example, a personal IDE preference).

The principle should be revisited if:

* The review cadence proves consistently mismatched to how fast the relevant tooling category changes.
* The exception process either becomes a bottleneck or stops being meaningful.
* A class of tooling decisions becomes more or less reversible due to platform changes.

## Authoritative References

* Dan McKinley, [Choose Boring Technology](https://boringtechnology.club/).
* MADR, [Markdown Architectural Decision Records](https://adr.github.io/madr/).
* Organization AI Decisions Log, AI Tooling Decision ([[ai-tooling]]).
* John Lewis Partnership, [Engineering Principles](https://engineering-principles.jlp.engineering/).
