---
id: "ORG-PRIN-INHERIT-THEN-SIMPLIFY"
status: draft:gray
title: "Organisation Principle: Inherit, Then Simplify"
date: 2026-05-16
author: Organization Tech Strategy
permalink: inherit-then-simplify
timetoread: 12 min
excerpt: "Organization starts from AVIV Group's existing technology and tooling: AWS contract, account foundation, networking, web and mobile golden paths, and operating practices. These give a fast start, real scale, and a coherent baseline. The principle is to inherit deliberately, then simplify deliberately. Inheritance does not mean acceptance forever. Simplification does not mean a rewrite. Both happen in time-bounded steps, with each step justified by reduced complexity, lower cost, or clearer ownership."
tags: organisation, inheritance, simplification, aviv-group, platform, modernization
logo: "assets/images/inherit-then-simplify/logo.jpeg"
logo_credit: "Inspired by Organization's tech and AI decisions logs"
icon: "assets/icons/inherit-then-simplify.png"
---

> **Status**: DRAFT
>
> **Principle**: Organization inherits AVIV Group's existing technology and tooling as the starting point for cloud, networking, web, mobile, and operating practices. The inherited baseline is honoured for a defined time window. During and after that window, Organization simplifies the baseline in evolutionary steps, each one justified by reduced complexity, lower cost, or clearer ownership. Inheritance buys time and consistency; simplification turns that into long-term ownership.

## Statement

Organization's posture toward shared technology is two-phase:

1. **Inherit.** Start from AVIV Group's existing setup where one exists: AWS organisation, account foundation, networking, web stack, mobile stack, operating model, contracts, and procurement.
2. **Simplify.** During an agreed time window (typically 6-12 months) and afterwards, reduce custom complexity, consolidate accounts, simplify networking, and align operations toward simpler, more conventional patterns.

Both phases are explicit. Inheritance is not "default forever". Simplification is not "rewrite from scratch".

## How to Read This Principle

| What it says | What it does **not** say |
| --- | --- |
| Start from the inherited baseline. | Accept the inherited baseline as final. |
| Simplify over time. | Replace everything quickly. |
| Inheritance has a time window. | The window expires with no plan. |
| Simplification is incremental. | Simplification is a programme. |
| Diverge with intent. | Diverge as soon as a team feels like it. |

The principle balances speed and ownership. Inheritance buys speed; simplification buys long-term control.

## How to Apply This Principle

Use this principle to:

* Explain why inheritance can be a deliberate strategy rather than passive acceptance.
* Distinguish alignment during the inheritance window from permanent dependency.
* Propose simplification steps that reduce complexity without triggering a rewrite.
* Identify when a fork or divergence creates real ownership obligations.

## Rationale

Organization could in theory build everything from scratch. The cost would be real: re-platforming AWS, redesigning networking, rebuilding mobile and web platforms, re-negotiating cloud contracts. None of those reduce Organization's actual product complexity in the short term.

Inheriting from AVIV Group gives:

* A working AWS estate and contract leverage.
* A landing-zone-style account model with established guardrails.
* A web Golden Path (React, TypeScript, Gemini Design System, Unified Frontend) and a mobile native baseline (Swift/SwiftUI, Kotlin/Jetpack Compose).
* Operating practices that have been refined over multiple AVIV Group brands.

Inheriting also imports complexity:

* Custom tooling (for example, AFT-based account factories, custom networking, custom access scripts).
* Coupling to AVIV Group's roadmap.
* Operating model assumptions Organization may not share long-term.

Therefore: inherit *and then simplify*. The simplification path makes inheritance sustainable. Without it, Organization is permanently a downstream consumer of decisions made elsewhere.

This principle is the meta-pattern behind Organization's AWS Foundation, AWS Networking, Web Tech Stack, and Mobile Tech Stack decisions.

## Implications

* **Each inheritance has a time window.** "Inherit for 6-12 months" is a concrete commitment with a review date, not an indefinite arrangement.
* **Forks are owned.** When Organization takes its own copy (for example, Gemini Design System, Unified Frontend, mobile apps), the fork has a named owner and a clear divergence policy.
* **Simplification has criteria.** Each simplification step articulates the complexity it removes and the consequences.
* **The default during inheritance is alignment.** Teams do not diverge from inherited patterns silently.
* **The default after the window is review.** What stays as-is, what simplifies, what diverges - all decisions, all written down.
* **Divergence costs are paid by Organization.** If Organization diverges, Organization owns the tooling, golden paths, and AI context for the divergent path.

## Inheritance Review Questions

Every inherited capability should be reviewed with the same frame:

* What value did inheritance give us immediately?
* Which parts are still useful and should remain aligned with AVIV Group?
* Which parts create local complexity, cost, or unclear ownership?
* Which teams depend on the inherited shape today?
* What simplification step would remove the most complexity with the least migration risk?
* What would Organization need to own if it diverged?
* What is the next review date, and what evidence should be available by then?

The useful answer is rarely "keep everything" or "replace everything". The useful answer is usually a narrow simplification step with a named owner and a measurable reduction in complexity.

## What This Means for Teams

For service teams:

* During the inheritance window, use the AVIV Group baseline by default for inherited domains (cloud, networking, web, mobile).
* When pain arises, capture it precisely - this becomes simplification input.
* Avoid hand-rolled local divergence; raise it as a proposal.

For platform and architecture roles:

* Maintain explicit inheritance status: what is inherited, until when, with what review.
* Map the simplification roadmap: account consolidation, networking simplification, fork ownership, operating-model adjustments.
* Negotiate with AVIV Group functions where relevant.

For tech leads:

* Treat inheritance as a fact, not a punishment. The cost of fighting it during the window is higher than the cost of accepting it.
* Treat the simplification window as an opportunity. Bring proposals with evidence.

## Anti-Patterns

* **Inheritance forever.** No review date, no plan to simplify, no ownership.
* **Reject-on-arrival.** Organization teams refusing the inherited baseline before learning what it does and why.
* **Silent divergence.** Local "we'll just do our own" patterns without an ADR.
* **Big-bang re-platforming.** "We'll cut ties with AVIV Group entirely in one programme" - replaces the inheritance complexity with rewrite complexity.
* **Fork orphaning.** Organization takes its own copy of a platform but does not staff it; the fork goes stale.
* **Simplification theatre.** Renaming inherited tooling without reducing its complexity.
* **One-foot-each.** Teams half-inheriting and half-diverging on the same component, with no clear ownership of either side.

## Examples

Aligned with the principle:

* Organization uses AVIV Group's AWS foundation tooling for 6-12 months while planning a simpler, country-delegated model.
* Organization takes its own source copies of Gemini and Unified Frontend, accepting ownership and reserving the right to diverge.
* The AWS account estate consolidates from ~200 accounts to a smaller, key set; each consolidation is a named, time-bounded effort.
* Mobile apps run on the inherited native baseline; Organization operates them as Organization-owned codebases.

Out of alignment with the principle:

* "We won't touch AVIV Group tooling, ever" or "We will replace everything in Q1".
* A team forks a shared platform with no plan to maintain the fork.
* Custom networking simplification is celebrated while the simplification never lands.
* Inherited operating practices are followed even when Organization's situation has clearly diverged.

## Discussion Prompts

Use these prompts during inheritance reviews:

* What inherited thing is still buying us speed, and what has become drag?
* Which simplification step is small enough to complete without a rewrite programme?
* If we diverge, what new ownership work are we accepting?

## Related Principles

* [[evolutionary-systems]] - simplification is an evolutionary path, not a rewrite.
* [[standardize-before-diverging]] - inheritance is the default; divergence is by ADR.
* [[small-and-simple]] - the long-term goal of simplification is a smaller, simpler estate.
* [[tooling-explicit-and-reversible]] - inherited tooling is a default that can be replaced by ADR.

## Scope and Revisiting

This principle applies to all domains where AVIV Group provides an existing baseline: AWS contract and foundation, networking, web platform, mobile platform, operating model, procurement, security baseline, and similar.

It does not apply to greenfield areas where Organization is choosing its own primary technology (for example, the .NET backend platform decision, the MSK messaging decision, the AI tooling decision); those are made on their own merits.

The principle should be revisited if:

* AVIV Group's roadmap diverges significantly from Organization's needs.
* The cost of inheritance exceeds the cost of simplification more sharply than expected.
* Regulatory or organisational changes alter the relationship between Organization and AVIV Group.
* A simplification window ends without a planned next phase.

## Authoritative References

* Martin Fowler, [Strangler Fig Application](https://martinfowler.com/bliki/StranglerFigApplication.html).
* AWS, [Account Strategy and Multi-Account Best Practices](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/welcome.html).
* Organization Tech Decisions Log, [AWS Foundation: Inherit Central AVIV Group Tooling for 6-12 Months](../tech-decisions-log/infra-tech-stack-aws-foundation.html).
* Organization Tech Decisions Log, [Web Tech Stack: Start from AVIV Group's Golden Path, Own the Fork](../tech-decisions-log/web-tech-stack.html).
