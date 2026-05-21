---
id: "ORG-PRIN-EVOLUTIONARY-SYSTEMS"
status: draft:gray
title: "Design Principle: Evolutionary Systems"
date: 2026-05-16
author: Organization Tech Strategy
permalink: evolutionary-systems
timetoread: 12 min
excerpt: "Design Organization systems for change. The next change is closer and more probable than the next clean rewrite. Architectures should enable small, safe, incremental changes throughout their lifecycle, not optimise for a fixed end-state that will never quite arrive. This shows up as backwards-compatible contracts, additive schema changes, feature flags, well-defined seams, reversible deploys, and a strong bias against grand re-architectures. Evolutionary systems are how Organization makes long-term progress without big-bang risk."
tags: design, evolution, change, refactoring, fitness-functions
logo: "assets/images/evolutionary-systems/logo.jpeg"
logo_credit: "Inspired by the JLP Engineering Principles 'Evolutionary Systems' principle"
icon: "assets/icons/evolutionary-systems.png"
---

> **Status**: DRAFT
>
> **Principle**: Organization systems should be designed and operated to support **easy, incremental change** for as long as they live. The next change matters more than the next rewrite. Contracts, schemas, deployments, and integrations should be shaped so that a small change can be made safely, observed in production, and reversed if necessary. Big-bang re-architectures are a sign that evolution failed earlier, not a celebrated norm.

## Statement

Organization systems should be:

* Easy to change in small steps.
* Hard to break with a single deploy.
* Reversible when a change is wrong.
* Backwards-compatible across contracts and schemas wherever feasible.
* Continuously refactored, not periodically rewritten.

A system that is *only* easy to change at the start of its life is not evolutionary. A system that requires a programme of work to change after two years has stopped being evolutionary, regardless of how clean its diagram looks.

## How to Read This Principle

| What it says | What it does **not** say |
| --- | --- |
| Optimise for the next change. | Avoid all big decisions. |
| Prefer additive, backwards-compatible changes. | Never break a contract. |
| Refactor continuously. | Refactor for its own sake. |
| Reversibility is a property of the change pipeline. | Reversibility means manual rollback scripts. |
| Big-bang re-architecture is a smell. | Re-architecture is forbidden. |

Evolutionary design is a way of thinking about *future* changes. It is not a license to defer every hard decision indefinitely.

## How to Apply This Principle

Use this principle to:

* Design changes as small, observable, reversible steps.
* Recognise when a migration plan has become a big-bang rewrite.
* Use contracts, schemas, feature flags, and fitness signals to support evolution.
* Explain why continuous refactoring is cheaper than periodic rescue projects.

## Rationale

The most reliable fact about a system in production is that someone will need to change it. They will need to change it because of:

* New product behaviour.
* New regulatory or compliance requirements.
* New scale or cost constraints.
* New security expectations.
* A failed assumption that the original design baked in.

If the cost of each change is high, two things happen. First, the team stops making small changes and waits for "the next refactor". Second, the refactor never quite arrives, because the system has grown around the friction.

Evolutionary design lowers the cost of each step. It accepts that the system in three years' time is going to differ from the one in production today, and prefers to get there by many small, observable steps rather than one large unobservable jump.

This principle also lines up with how Organization's wider strategy is structured. Inheriting AVIV Group's tooling and then simplifying over 6-12 months is an evolutionary move. Taking the AVIV web stack as a starting point and reserving the right to diverge is evolutionary. The AI strategy's "incremental over big-bang" rule is the same principle, expressed differently.

## Implications

* **Contracts are evolved, not replaced.** Add fields, support both shapes during a transition, retire old shapes once consumers have moved.
* **Schemas use additive migrations.** Add columns; backfill; deprecate old columns; remove later. Never combine "add", "rename", and "drop" into one deployment.
* **Feature flags are part of the architecture.** They make change a runtime decision rather than a deployment event.
* **Deploys are reversible.** Rolling back a deploy should not require a database restore.
* **Strangler patterns over rewrites.** Replace systems by routing traffic away from them piece by piece.
* **Fitness functions guard against regression.** Performance, error rate, security, and architectural properties should be measured continuously, not audited once.
* **Refactoring is part of the work, not a separate quarter.** Every change leaves the affected area at least as clean as it found it.

## Evolutionary Design Checklist

A proposed change is evolutionary when it can move through production in controlled steps. Ask:

* Can old and new behaviour run side by side for at least one deploy?
* Can the change be enabled for a subset of users, traffic, tenants, or consumers?
* Can rollback happen without restoring a database from backup?
* Are contract and schema changes additive before they are destructive?
* Is the migration observable through metrics, logs, traces, and business signals?
* Is there a clear retirement plan for flags, adapters, compatibility layers, and old paths?
* Does each step deliver learning or value, rather than only preparing for a future cutover?

If the plan has only two states - "old system" and "new system" - it is probably a rewrite plan, not an evolutionary plan.

## What This Means for Teams

For service teams:

* When changing a published contract, support old and new in parallel for at least one deploy.
* Treat database migrations as a sequence of additive, reversible steps.
* Wrap risky changes in feature flags with a clear off-switch and a clear retirement date.
* Use canary or progressive deploys where the platform supports them.
* Pay refactoring cost continuously rather than letting it accumulate.

For platform and architecture roles:

* Make rollback and progressive deploy the default in golden paths.
* Provide patterns for additive schema changes, contract versioning, and feature flagging.
* Track architectural fitness signals - error rate, latency, change failure rate, lead time - as first-class outputs of the platform.

For tech leads:

* Push back on changes that bundle "fix", "refactor", and "rewrite" into a single deploy.
* Plan migrations in slices with clear, observable milestones.
* Treat any decision that says "we'll fix it in the rewrite" as a red flag.

## Anti-Patterns

* **The Big Rewrite.** A new system replaces an old one in a single cutover, after a long parallel build, with limited production feedback until the end.
* **Breaking change as default.** Every consumer is forced to update at the same time because the producer changed the contract.
* **One-way migration.** A deploy that cannot be rolled back without data loss or a restore.
* **Refactor quarter.** A long pause in feature work to "clean things up", followed by a return to the same patterns.
* **Feature flag graveyard.** Hundreds of unused flags accumulating, hiding the real control flow.
* **Architecture as a frozen artifact.** A diagram approved once and not updated as the system evolves.
* **"We'll fix it in the rewrite."** Used as a license to add the very debt the rewrite is supposed to remove.

## Examples

Aligned with the principle:

* Adding a new Kafka event type while keeping the old one supported until consumers migrate.
* Migrating from one library to another via an internal adapter that lets services move one at a time.
* Splitting a large service by extracting one route at a time behind a feature flag.
* Consolidating AWS accounts gradually rather than re-platforming everything in one cutover.

Out of alignment with the principle:

* A "v2" service rebuilt next to "v1" for nine months and switched over in a single weekend.
* A schema change that renames and drops columns in the same migration.
* A library upgrade that requires every team to deploy on the same day.
* A re-architecture proposal whose only success criterion is "v2 is live".

## Discussion Prompts

Use these prompts in design reviews:

* What is the smallest safe step that teaches us something useful?
* Which part of the plan is reversible, and which part is not?
* What compatibility layer, flag, or metric needs a retirement date?

## Related Principles

* [[small-and-simple]] - small pieces are individually easier to evolve.
* [[standardize-before-diverging]] - shared defaults give you safe seams to evolve along.
* [[inherit-then-simplify]] - inherited estates become simpler through evolution, not replacement.
* [[production-ready]] - evolutionary change depends on production feedback.

## Scope and Revisiting

This principle applies to all Organization-owned systems: backend services, web and mobile applications, data and integration pipelines, internal platforms, and shared libraries.

It does not apply to genuinely throwaway prototypes, short-lived experiments, or one-off scripts; though even there, a habit of reversibility usually pays off.

The principle should be revisited if:

* The platform stops supporting safe, progressive deploys or rollback.
* The cost of running parallel versions of a contract or schema becomes unsustainable.
* A radical architectural shift (for example, a regulatory event) requires a deliberate, exceptional big-bang change.

## Authoritative References

* Neal Ford, Rebecca Parsons, Patrick Kua, *Building Evolutionary Architectures*, O'Reilly.
* Martin Fowler, [Strangler Fig Application](https://martinfowler.com/bliki/StranglerFigApplication.html).
* John Lewis Partnership, [Evolutionary Systems Principle](https://engineering-principles.jlp.engineering/).
* DORA, [Four Key Metrics](https://dora.dev/research/).
