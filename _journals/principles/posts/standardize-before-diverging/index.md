---
id: "ORG-PRIN-STANDARDIZE-BEFORE-DIVERGING"
status: draft:gray
title: "Design Principle: Standardize Before Diverging"
date: 2026-05-16
author: Organization Tech Strategy
permalink: standardize-before-diverging
timetoread: 12 min
excerpt: "Adopt a default before allowing variation. Organization's backend on .NET, compute on ECS Fargate, messaging on MSK, cloud on AWS, and AI tooling on Claude Code are all defaults. Teams may diverge from a default by ADR, but they may not diverge by accident. The principle protects the cost compounding of a shared platform: a golden path is only valuable if most teams are on it. Variation has to earn its keep, not be granted by silence."
tags: design, standardization, golden-path, exceptions, governance
logo: "assets/images/standardize-before-diverging/logo.jpeg"
logo_credit: "Inspired by Organization's tech-decisions log and AI strategy"
icon: "assets/icons/standardize-before-diverging.png"
---

> **Status**: DRAFT
>
> **Principle**: Organization picks defaults and stays on them until there is a written, owned reason to diverge. A team may propose an exception by ADR, name the costs, and accept the responsibility for the divergence. Silence is not a license. The platform's value compounds only when most teams use the default; exceptions are a managed minority, not a parallel norm.

## Statement

For every shared technology decision, Organization:

1. Picks a single default.
2. Documents the default as the expected choice.
3. Makes the default the easiest path - tooling, examples, support, hiring, training.
4. Permits divergence only through a documented exception.
5. Reviews exceptions on a schedule.

The principle applies to programming languages, runtimes, container bases, cloud provider, messaging, AI tooling, observability, repository conventions, and any other choice where shared compounding matters more than local optimisation.

## How to Read This Principle

| What it says | What it does **not** say |
| --- | --- |
| There is a default. | The default fits every case. |
| Divergence requires an ADR. | Divergence is forbidden. |
| Defaults should be easy. | Non-defaults should be impossible. |
| Exceptions get reviewed. | Exceptions are temporary by definition. |
| The platform compounds on the default. | The platform must do everything. |

The principle does not mean uniformity at any cost. It means *deliberate* divergence by *named* owners with *known* trade-offs.

## How to Apply This Principle

Use this principle to:

* Explain why defaults compound platform value.
* Distinguish deliberate divergence from accidental variation.
* Write or review an exception ADR that names local benefit and global cost.
* Recognise when a default is failing because it is not the easiest path.

## Rationale

A shared engineering platform pays off through repetition. Every team that adopts the default reduces the marginal cost of:

* Adding observability.
* Adding security defaults.
* Onboarding new engineers.
* Sharing patterns and golden templates.
* Operating systems on-call.
* Applying AI tooling like Claude Code with shared CLAUDE.md context.

Variation, by contrast, taxes the platform. Each new runtime, base image, cloud provider, broker, or convention duplicates work that the default already does. The platform either supports the variant - which makes it weaker - or doesn't support it - which leaves the team alone with the consequences.

Organization's strategic decisions are a long list of defaults. Backend on .NET. Compute on ECS Fargate. Container base on Ubuntu. Messaging on MSK. Cloud on AWS. AI tooling on Claude Code. AVIV Group as the inherited starting point for web, mobile, and AWS foundation tooling. This principle is the meta-decision behind those choices.

## Implications

* **Defaults are written down.** Every shared choice has a record stating what it is, who owns it, and how to depart from it.
* **Divergence is by ADR.** A team that wants to diverge writes an ADR, names the alternative, the cost, the owner, and the revisit trigger.
* **Defaults are made cheap.** Templates, golden paths, CI defaults, and Skills target the default. Friction lives on the divergence path, not the default path.
* **Exceptions are reviewed periodically.** Exceptions that have not been used or have stopped being justified should be retired.
* **A default that is not the easy path is not a default.** If most teams ignore it, the principle is failing.
* **A default that is mandatory has stopped being a principle and become an edict.** Edicts produce malicious compliance.

## Exception Test

A divergence proposal should answer these questions before work starts:

* Which default is being diverged from?
* What requirement is not met by improving or using the default?
* What local benefit does the divergence create?
* What global cost does it add to hiring, support, operations, AI context, security, or platform tooling?
* Which team owns the divergence and its lifecycle?
* What evidence would cause the team to return to the default?
* When will the exception be reviewed?

The test is not meant to block every exception. It ensures exceptions are deliberate enough that the organisation can learn from them instead of accumulating accidental variety.

## What This Means for Teams

For service teams:

* If a default exists for what you need, use it. Even if a different choice would be marginally better in isolation.
* If you need to diverge, write the ADR before you start, not after.
* Treat your divergence as a cost your team owns: tooling gaps, hiring constraints, lack of golden paths.

For platform and architecture roles:

* Maintain the list of defaults publicly.
* Invest in making the default the easy path: templates, Skills, sane defaults, observability, security.
* Run periodic exception reviews.

For tech leads:

* Before proposing a new technology, ask whether the default can be improved to cover the case.
* When mentoring teams, prefer the default unless there is a real reason not to.
* Bring divergence proposals to the Architecture Advisory Forum early.

## Anti-Patterns

* **Best-tool-for-the-job per team.** Every team chooses its own runtime, broker, and database, justified locally and expensive globally.
* **Default by silence.** A default exists in slides but not in tooling; teams quietly diverge because no path supports the default.
* **Default by edict.** A default is enforced bureaucratically without ever being made the easy path.
* **Exception drift.** Exceptions accumulate, are never reviewed, and gradually outnumber default usage.
* **Standard-then-shadow.** A team officially adopts the default but maintains a parallel non-default system "for now".
* **Single-team standard.** A standard set by one team for everyone else, without consultation.
* **Greenfield exemption.** New work is allowed to diverge because "it's new"; old work keeps the default.

## Examples

Aligned with the principle:

* New backend service starts on .NET, ECS Fargate, Ubuntu base, MSK for messaging - no ADR needed.
* A team needing a small TypeScript BFF writes a short ADR explaining the narrow scope, with .NET still the default for new core services.
* Claude Code is the default AI coding tool; Codex or Gemini use is allowed by exception with a recorded rationale.
* AVIV Group's web Golden Path is the starting point; divergence is recorded and owned.

Out of alignment with the principle:

* A team adopts a new runtime "just for this service" without an ADR, and the runtime spreads.
* A new database engine is introduced because a vendor demo was compelling, with no review of how it compares to the default.
* The default is documented but the only golden template ships for a different runtime.
* Exceptions are granted in Slack threads with no recording.

## Discussion Prompts

Use these prompts in exception reviews:

* Is the default genuinely insufficient, or is it merely less familiar?
* What global cost does this local optimisation create?
* What would make the exception unnecessary in six months?

## Related Principles

* [[small-and-simple]] - a small palette of defaults is itself a form of simplicity.
* [[inherit-then-simplify]] - inherited defaults are honoured until simplified, not abandoned.
* [[tooling-explicit-and-reversible]] - tooling defaults are deliberately chosen and revisited on a cadence.
* [[governance-as-code]] - defaults are reinforced through executable golden paths.

## Scope and Revisiting

This principle applies to all shared technology choices: language, runtime, cloud, messaging, observability, AI tooling, repository structure, and similar.

It does not apply to choices that are local to one component and do not affect other teams (for example, a library used only within one service that has no operational footprint outside it).

The principle should be revisited if:

* The defaults stop reflecting where Organization actually invests.
* The exception process becomes a bottleneck or a rubber stamp.
* A major shift in the AVIV Group relationship changes what "inherited" means.

## Authoritative References

* Mike Amundsen, [Paved Roads vs Guard Rails](https://www.thoughtworks.com/insights/blog/microservices/paved-roads-vs-guard-rails).
* Spotify Engineering, [Paved Path for Backend Services](https://engineering.atspotify.com/).
* Charity Majors, [Paved Roads](https://charity.wtf/).
* Organization, AI Tooling Decision: Claude Code as Default ([[ai-tooling]]).
