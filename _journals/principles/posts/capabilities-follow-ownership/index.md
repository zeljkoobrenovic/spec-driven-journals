---
id: "ORG-PRIN-CAPABILITIES-FOLLOW-OWNERSHIP"
status: draft:gray
title: "Organisation Principle: Capabilities Follow Ownership"
date: 2026-05-16
author: Organization Tech Strategy
permalink: capabilities-follow-ownership
timetoread: 12 min
excerpt: "Every shared capability at Organization - service, library, platform, golden path, Skill, MCP server, subagent, CLAUDE.md fragment, runbook - belongs to a named owner with a real lifecycle. Capabilities without owners decay, drift, and quietly poison the platform. The principle is simple: if it can be used by another team, it has an owner, a lifecycle, and a decommissioning plan. Otherwise it should not exist as a shared thing."
tags: organisation, ownership, platform, lifecycle, capabilities, skills, mcp
logo: "assets/images/capabilities-follow-ownership/logo.jpeg"
logo_credit: "Inspired by Team Topologies and Organization's AI operating model"
icon: "assets/icons/capabilities-follow-ownership.png"
---

> **Status**: DRAFT
>
> **Principle**: Every shared engineering capability at Organization has a named owner, a lifecycle, and a decommissioning path. This applies to services, libraries, platforms, golden paths, templates, Skills, MCP servers, subagents, CLAUDE.md fragments, runbooks, and any other artifact other teams depend on. Capabilities without owners decay silently and poison the platform. If a capability cannot be owned, it should not be shared.

## Statement

A **capability** is anything one team produces that another team can use: a service, an API, a library, a base image, a CI template, a CLAUDE.md fragment, a Skill, an MCP server, a subagent, a runbook, a dashboard, a build script.

Every capability has:

* **An owning team.** Named, not implied.
* **A purpose.** What it does, when to use it, when not to.
* **A lifecycle status.** Active, deprecated, retired.
* **A review cadence.** Whether it is still doing its job.
* **A decommissioning plan.** What replaces it if it goes away.

Capabilities that lose their owner do not become "everyone's"; they become nobody's. The principle prevents that by requiring ownership up front and surfacing loss of ownership when it happens.

## How to Read This Principle

| What it says | What it does **not** say |
| --- | --- |
| Shared capabilities have owners. | Every line of code has a single named author. |
| Ownership is by team. | Ownership is by individual. |
| Lifecycles are explicit. | Capabilities live forever. |
| Decommissioning is planned. | Capabilities are deleted casually. |
| Unowned capabilities should not be shared. | Unowned work cannot exist. |

The principle scopes ownership to the things other teams depend on. Personal scripts, prototypes, and experiments are not subject to the same standard.

## How to Apply This Principle

Use this principle to:

* Distinguish a team-local artifact from a shared capability.
* Explain why ownership, lifecycle, and decommissioning must be decided before broad adoption.
* Evaluate whether a capability is safe for other teams to depend on.
* Spot the early signs of capability decay: stale docs, unclear owners, hidden consumers, and permanent deprecation.

## Rationale

Shared capabilities compound when they are owned. They decay when they are not. The decay pattern is consistent:

1. A team builds a useful artifact - a CI template, a Kafka client wrapper, a Claude Code Skill.
2. Other teams adopt it.
3. The original team's priorities change.
4. The artifact stops being maintained.
5. Bugs accumulate; documentation goes stale; trust erodes.
6. Other teams either fork it, abandon it, or use it through workarounds.
7. The platform is now harder to operate than it would have been with no shared artifact at all.

Organization's AI strategy makes this acute. Skills, MCP servers, subagents, CLAUDE.md fragments, hooks, and Claude Code settings are all *capabilities*. Without explicit ownership and lifecycle, the AI engineering surface decays the same way as a Java library would.

The dedicated AI Engineering Enablement function in the AI operating model exists in part to make this principle real for AI-shaped capabilities. The same logic applies to backend libraries, frontend templates, infrastructure modules, and platform golden paths.

## Implications

* **Every shared capability has a `CODEOWNERS` (or equivalent) entry.** No file enters a shared platform without ownership.
* **Lifecycle status is visible.** Active, deprecated, retired - readers know which.
* **Deprecation has a date.** "Deprecated" without a removal date is permanent in practice.
* **A capability without an owner is decommissioned, not adopted by default.** Other teams stepping in is a deliberate choice, not an accident.
* **Capabilities are reviewed periodically.** Usage, cost, satisfaction, and fit are reviewed; outcomes are recorded.
* **Adoption is informed.** Other teams choosing to depend on a capability do so with the lifecycle visible.
* **Personal experiments are not shared capabilities.** They live in personal or experimental spaces until promoted.

## Capability Registry Minimum

A shared capability should not enter a platform, catalog, or team-facing default without a minimum record:

| Field | Why it matters |
| --- | --- |
| **Name** | Gives teams a stable thing to refer to. |
| **Owner** | Makes support and change responsibility explicit. |
| **Purpose** | Explains what the capability is for and when to use it. |
| **Status** | Shows whether it is active, deprecated, experimental, or retired. |
| **Consumers** | Helps assess blast radius when it changes. |
| **Support path** | Tells users where to ask questions and report problems. |
| **Review date** | Prevents quiet decay. |
| **Exit path** | Explains what teams should do if the capability is retired. |

This registry does not need to be heavy. A simple markdown page, YAML catalog, or repository index is enough if it is maintained and linked from the places teams actually look.

## What This Means for Teams

For service teams:

* Before publishing a capability for others to use, accept the ownership cost.
* Mark personal or experimental things as such; do not let them become shared by accident.
* When a capability you own no longer fits, deprecate it formally; do not just stop maintaining it.

For platform and AI Engineering Enablement roles:

* Curate the registry of shared capabilities, including Skills, MCP servers, subagents, and CLAUDE.md fragments.
* Enforce the ownership requirement for entries into shared registries.
* Run lifecycle reviews and publish results.

For tech leads:

* When adopting a capability, check its owner and lifecycle status.
* Refuse to adopt unowned shared artifacts; raise the gap instead of working around it.

For senior leadership:

* Treat lifecycle reviews as a real signal of platform health.
* Resist the urge to "consolidate" unowned things into a single team without funding ownership.

## Anti-Patterns

* **Tragedy of the commons.** A useful library that everyone uses and nobody maintains.
* **Ghost capability.** A Skill, template, or service in production that no team admits to owning.
* **Promotion-by-use.** A team's internal helper becomes a de facto platform because adoption outran ownership decisions.
* **Permanent deprecation.** Capabilities marked deprecated for years with no removal plan.
* **Owner-of-record only.** A team is technically the owner but has no capacity to operate the capability.
* **Forced adoption.** Other teams told to depend on a capability that has no real owner.
* **Personal Skill at platform scale.** An individual's Claude Code Skill becomes used across the org without a named team behind it.

## Examples

Aligned with the principle:

* A Claude Code Skill in the shared registry has a named owning team, a lifecycle status, and a review date.
* A CI template lives in a repo with CODEOWNERS, a README explaining the purpose and lifecycle, and a deprecation plan if applicable.
* A platform team explicitly accepts ownership of an inherited capability before it is promoted to a shared default.

Out of alignment with the principle:

* A subagent used across teams that was written by one engineer who has since changed teams.
* A "deprecated since 2024" capability that 30 services still depend on.
* A Skill registry that contains entries with no owner column.

## Discussion Prompts

Use these prompts in onboarding or team retrospectives:

* Which shared capability do we depend on whose owner is unclear?
* Which capability have we accidentally promoted from team-local helper to platform dependency?
* What should we decommission rather than continue maintaining weakly?

## Related Principles

* [[standardize-before-diverging]] - defaults are themselves capabilities and need owners.
* [[decisions-stay-with-teams]] - capability ownership lines up with decision ownership.
* [[governance-as-code]] - ownership and lifecycle are partly enforced by automation.
* [[production-ready]] - operational ownership is a readiness item.
* [[ai-output-must-be-governed]] - AI-shaped capabilities are subject to the same ownership rules as code.

## Scope and Revisiting

This principle applies to all shared capabilities consumed across team boundaries at Organization: code, infrastructure, templates, AI configuration, documentation, dashboards, runbooks, and similar.

It does not apply to genuinely team-local artifacts that other teams do not depend on.

The principle should be revisited if:

* The shared registry becomes too granular or too coarse to be useful.
* Lifecycle reviews are repeatedly skipped or repeatedly inconclusive.
* A new kind of capability (for example, a new AI primitive) requires a different ownership model.

## Authoritative References

* Matthew Skelton, Manuel Pais, *Team Topologies*, IT Revolution.
* Charity Majors, [What is "Ownership"?](https://charity.wtf/).
* Organization AI Decisions Log, AI Operating Model: Dedicated AI Engineering Enablement Function ([[ai-operating-model]]).
* John Lewis Partnership, [Engineering Principles](https://engineering-principles.jlp.engineering/).
