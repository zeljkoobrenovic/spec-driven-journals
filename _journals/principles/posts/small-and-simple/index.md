---
id: "ORG-PRIN-SMALL-AND-SIMPLE"
status: draft:gray
title: "Design Principle: Small (and Not Too Small) and Simple (and Not Too Simple)"
date: 2026-05-16
author: Organization Tech Strategy
permalink: small-and-simple
timetoread: 12 min
excerpt: "Prefer small, simple components over large, clever ones - but not too small and not too simple. Organization systems should be decomposed into pieces that one team can understand end-to-end, that one engineer can hold in their head, and that can be replaced without rewriting the platform around them. The opposite extreme - nanoservices, where every endpoint or function becomes its own service - replaces internal complexity with distributed complexity that often costs more than the monolith it was supposed to replace. The principle is not 'microservices for everything', and not 'split until it can't be split'; it is 'no piece bigger or smaller than it needs to be for what it actually does'."
tags: design, simplicity, modularity, microservices, nanoservices, complexity
logo: "assets/images/small-and-simple/logo.jpeg"
logo_credit: "Inspired by the JLP Engineering Principles 'Small and Simple' principle"
icon: "assets/icons/small-and-simple.png"
---

> **Status**: DRAFT
>
> **Principle**: Break Organization software into small, simple pieces - but not too small and not too simple. A component should be small enough for one team to own end-to-end and simple enough for one engineer to hold in their head, **and large enough that the cost of being a separate piece is paid back by the cohesion it provides.** Where a system gets large, decompose it. Where a system gets fragmented, consolidate it. Size and cleverness are paid for every time the code is read, changed, deployed, or recovered; *smallness* is paid for every time pieces have to be coordinated across the network.

## Statement

Build software out of **small and simple pieces** - but not smaller or simpler than the problem actually rewards. Prefer:

* Small services over large monoliths, **and cohesive services over nanoservices**.
* Simple control flow over clever abstractions, **and meaningful behaviour over trivial wrappers**.
* One purpose per component over multi-purpose modules, **where "one purpose" is a real business or technical responsibility, not a single function**.
* Boring, mainstream technology over novel platforms.
* Composition of small parts over generalisation of one large part, **as long as the composition itself is comprehensible**.

A piece of software is "small and simple enough" when:

1. A single engineer joining the team can read it end-to-end, run it locally, and reason about a change without consulting a senior maintainer; **and**
2. The cost of operating it as a separate piece - its deployment pipeline, its observability, its on-call, its inter-service contracts - is paid back by the cohesion, autonomy, or scalability it provides.

If either test fails, the piece is the wrong size. Too big fails test 1. Too small fails test 2.

## How to Read This Principle

This principle is easy to misquote. Treat the following pairs carefully:

| What it says | What it does **not** say |
| --- | --- |
| Decompose where complexity hurts. | Microservices everywhere by default. |
| Decompose where complexity hurts. | Nanoservices everywhere by default. |
| Prefer simple control flow. | Avoid all abstractions. |
| Boring technology by default. | Never adopt new technology. |
| Components a team can own end-to-end. | Components owned by one person. |
| Simplicity is a property of the system. | Simplicity is a feeling. |
| Smallness has a lower bound. | Below that bound, "smaller" is "more complex". |

The principle is a bias, not a rule. A small monolith with strong internal boundaries is simpler than a constellation of micro-things wired together by accident. The right size is the one whose total complexity - code, deployment, integration, on-call, *and the cost of distribution itself* - is smallest for the problem at hand.

## How to Apply This Principle

Use this principle to:

* Explain why both oversized components and nanoservices increase complexity.
* Evaluate component boundaries using ownership, lifecycle, operational cost, and cognitive load.
* Decide when to split, merge, or leave a component alone.
* Challenge "smaller is always better" and "one service per thing" as slogans rather than reasoning.

## But Not Too Small, and Not Too Simple

The opposite of a tangled monolith is not a swarm of nanoservices. Nanoservices push fragmentation past the point where it pays off, and replace one kind of complexity with another that is usually worse, not better.

A piece of software is **too small** when:

* It exists only to wrap one or two operations.
* It has no autonomous behaviour or independent lifecycle.
* It cannot be reasoned about without simultaneously reasoning about three or four of its siblings.
* It has more deployment, observability, and on-call apparatus than business logic.
* It exists because of a rule ("one service per resource", "one service per endpoint") rather than a reason.

When pieces drop below the minimum useful size, the cost moves from inside the process to between processes - and that cost is harsher:

* **Network as control flow.** Logic that would have been a function call becomes a remote call, with latency, partial failure, retries, timeouts, and version skew.
* **Coordinated deployment.** Many tiny services must be deployed together to make any meaningful change work; the team has built a distributed monolith.
* **Debugging by distributed tracing.** What would have been a stack trace becomes a multi-hour archaeology project across logs from many systems.
* **Operational sprawl.** Each tiny service needs its own pipeline, dashboards, alerts, runbooks, on-call rotation, and lifecycle attention - all paid before the first line of business value.
* **Schema gravity.** Tiny services share data through ever-growing shared schemas or events, recreating the implicit coupling they were meant to eliminate.
* **Cognitive load on the team.** The number of moving parts grows faster than the team's ability to keep them in mind.

The "right small" is the size at which a component is **autonomously meaningful**: it owns a real responsibility, it has a useful lifecycle of its own, and the cost of being a separate piece is paid back by the cohesion and autonomy it provides. Below that point, "smaller" stops being "simpler".

Similarly, a component is **too simple** when:

* Its abstraction hides what callers must know to use it safely.
* Its simplicity is a trick of presentation; the complexity has moved to the call sites or the configuration.
* It is so generic that every consumer reinvents the same wrapper around it.
* Simplification has erased a real distinction in the domain.

Simplicity is a property of the *whole system*, not of one component in isolation. A simpler component that makes the surrounding system more complicated is a net loss.

## Rationale

Complexity is the recurring cost in software. It is paid:

* Every time someone reads the code.
* Every time someone changes the code.
* Every time someone joins the team and has to learn the code.
* Every time an incident requires the code to be understood quickly.
* Every time a dependency is upgraded, a deployment is rolled, or a region is failed over.

The interest rate on accidental complexity is high. Small, simple components reduce that rate by making each piece individually cheap. They also reduce blast radius: a small piece fails small, a small piece is rewritten cheaply, a small piece can change technology without a programme.

But the same logic cuts the other way at the small end. Every additional process boundary, every additional repository, every additional pipeline, every additional alert and on-call rota is a fixed cost that does not scale down. When that cost exceeds what the piece does for users, the system as a whole gets more complex, not less - even though each individual piece looks "simpler". Nanoservices are the canonical example: a hundred trivial services collectively impose more cognitive, operational, and integration cost than a well-organised modular monolith would.

Organization's wider technology decisions push from both directions. ECS Fargate is chosen over self-managed Kubernetes because it is simpler to own; .NET is chosen because it removes accidental backend variance; AVIV Group's existing tooling is inherited for 6-12 months because re-platforming on day one would add complexity instead of reducing it. At the same time, the backend platform is consolidating onto a small set of cohesive services rather than fragmenting into per-endpoint micro-things. Each of those decisions is a Small-and-Simple decision wearing different clothes - chosen with both extremes in mind.

## Implications

* **Decompose where it hurts, not because it is fashionable.** Service splits should track ownership and change boundaries, not architectural taste.
* **Consolidate where fragmentation hurts.** When several "services" are always deployed together, debugged together, and reasoned about together, they are one service in disguise; merge them.
* **A service needs autonomous behaviour to deserve its boundary.** "One operation" is a method. "One real responsibility" might be a service.
* **Limit the technology palette.** A small set of mainstream technologies is simpler than a wider, more "best-tool-for-the-job" set.
* **Prefer composition over generalisation.** Three small services with focused jobs are usually simpler than one large service with three configurable modes - *and* simpler than thirty nano-services with the same job split arbitrarily.
* **Make local reasoning possible.** A change should be reviewable inside one repository, one service, and one team's context where realistic. If a routine change spans many services, the boundaries are wrong.
* **Reject cleverness without a reason.** Abstractions that are not paying their cost should be removed or never introduced.
* **Count the operational cost.** If splitting a service adds two new pieces of infrastructure, the split is not small.
* **Count the distribution cost.** Every additional process boundary is a fixed tax. Pay it only when the responsibility is large enough to amortise it.
* **Treat new technology as a complexity event.** Adopting it should require evidence that it removes more complexity than it adds.
* **Prefer modular monoliths to nanoservices** when the system fits in one team's head and the responsibilities do not require independent scaling, lifecycles, or runtimes.

## Sizing Diagnostics

Use these questions before splitting or merging components:

* Does the component own a real responsibility, or only a technical slice?
* Can one team operate it end-to-end without coordinating routine changes with several other teams?
* Does it have an independent deploy, scale, failure, or data lifecycle?
* Are its contracts more stable than its implementation?
* Would splitting it reduce cognitive load, or simply move complexity into the network?
* Would merging it reduce coordination cost without creating a new large ball of mud?
* Can a new joiner understand the component and its boundaries in a week?

The right answer may be to split, merge, or leave the boundary alone. The principle asks teams to size components against real complexity, not against architectural fashion.

## What This Means for Teams

For service teams:

* Aim for services a single squad can own end-to-end, including deployment and on-call.
* Resist clever frameworks, code generators, and dynamic indirection unless they pay clear, measurable rent.
* When a service grows, look for a seam to split along, not a configuration flag to add.
* Document the *boundary* of the service - inputs, outputs, contracts - and keep the boundary smaller than the implementation.

For platform and architecture roles:

* Curate a small, well-supported technology palette.
* Make the easy path the simple path: golden templates, default container bases, default runtime, default observability.
* Push back on architectural elaboration that does not match the size of the actual problem.

For tech leads:

* Use "could a new joiner reason about this end-to-end in a week?" as a standing diagnostic.
* Treat unexplained abstraction, multi-level dynamic dispatch, and configuration-as-control-flow as smells to investigate.

## Anti-Patterns

At the "too big" end:

* **Framework Stockholm syndrome.** A team treats a homegrown framework as load-bearing when the framework is the source of most complexity.
* **Configuration-as-code-disguise.** A "simple" service whose real logic lives in a 2,000-line YAML file.
* **Premature generality.** A component built for cases that have not appeared, and may not.
* **Cleverness as identity.** A team that takes pride in how subtle the code is should be asked what that subtlety buys.

At the "too small" end:

* **Nanoservice sprawl.** One service per endpoint, per resource, or per database table, with no autonomous business behaviour in any of them.
* **Distributed monolith.** Many small services that must all deploy together to make any change work, with network calls standing in for function calls.
* **Wrapper services.** A "service" that exists only to forward a call to another service, adding latency, failure modes, and on-call burden but no behaviour.
* **One-team, twenty-services.** A single team that spends more time on cross-service coordination than on the product it owns.
* **Schema-shaped boundaries.** Services split along table boundaries, so any meaningful change touches several services and a shared schema.

Spanning both extremes:

* **Microservices for organisational symmetry.** Splitting a service to match the org chart, not to reduce complexity - usually produces either too-big services or too-small ones, never the right ones.
* **Best-tool-for-the-job sprawl.** Each service chooses its own runtime, database, and queue technology, multiplying the operations surface.
* **Architecture by slogan.** "Microservices everywhere", "monolith forever", or "smaller is always better" - each is a refusal to size pieces against the actual problem.

Aligned with the principle:

* Standardising backend services on .NET, ECS Fargate, and Ubuntu containers rather than letting each team pick.
* Choosing ECS over self-managed Kubernetes for the next phase of platform work.
* Keeping the markdown-record build script to the Python standard library rather than introducing a framework.
* Splitting a backend integration into a small Kafka producer and a small consumer, both owned by the same team, rather than building one larger orchestrator.
* Keeping a cohesive domain - for example, "listings" - as a single well-modularised service rather than fragmenting it into "create-listing", "update-listing", "publish-listing", "expire-listing" micro-services.
* Merging three tiny services that always change and deploy together back into one, after evidence shows the split is paying no dividends.

Out of alignment with the principle:

At the "too big" end:

* A "platform" service that handles authentication, feature flags, configuration, and notifications because all four are "infrastructure-ish".
* Adding a service mesh, a sidecar, and a custom CRD to deploy a single new API.
* A new runtime adopted because one team wanted to try it, with no path to replace the existing default.

At the "too small" end:

* A separate microservice for each CRUD endpoint of a single resource, all owned by the same team, sharing the same database, and always deployed together.
* A "service" whose only behaviour is to call another service and rename one field in the response.
* Forty production services for what is, in practice, one product domain handled by one squad.

## Discussion Prompts

Use these prompts in architecture reviews:

* Which boundary is making local reasoning easier, and which boundary is only moving complexity into coordination?
* What evidence tells us this component is too large, too small, or roughly right?
* If we split or merge this component, what operational cost changes?

## Related Principles

* [[evolutionary-systems]] - small pieces are easier to evolve.
* [[smarts-in-the-nodes]] - simple, autonomous nodes beat clever middleware.
* [[standardize-before-diverging]] - smallness without standardisation becomes sprawl.
* [[inherit-then-simplify]] - inherited platforms must be actively simplified over time.

## Scope and Revisiting

This principle applies to Organization's software, services, libraries, and platforms. It does not apply to product surface area, user journeys, or organisational design directly, though those benefit from similar thinking.

The principle should be revisited if:

* A measurably simpler architectural pattern becomes the industry default.
* The current technology palette stops being mainstream or well-supported.
* The cost of inter-service operation becomes higher than the cost of running fewer, larger services - or the cost of running fewer, larger services becomes higher than the cost of splitting them.
* Patterns of fragmentation or consolidation in the estate consistently outrun the team's ability to keep them in mind.

## Authoritative References

* John Lewis Partnership, [Small and Simple Principle](https://engineering-principles.jlp.engineering/), engineering-principles.jlp.engineering.
* Sam Newman, *Building Microservices*, O'Reilly.
* Martin Fowler, [MicroservicePremium](https://martinfowler.com/bliki/MicroservicePremium.html).
* Arnon Rotem-Gal-Oz, [Nanoservices Antipattern](https://www.infoq.com/news/2014/05/microservices/).
* Dan McKinley, [Choose Boring Technology](https://boringtechnology.club/).
