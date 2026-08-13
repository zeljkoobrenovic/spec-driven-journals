---
timetoread: "2 min read"
---

An internal platform is implemented as three planes: a self-service **management plane** developers touch, a **control plane** that continuously reconciles desired state with actual state, and a **services plane** that does the actual work. Every abstraction the platform introduces must pass two tests — it genuinely reduces cognitive load, and a failure can be traced back through it — because a platform that hides complexity without a troubleshooting path has not reduced cognitive load; it has deferred it to the worst possible moment.

**What changes**

* Every platform implementation names what fills each plane: portal, CLI, APIs, and automation built around real user journeys (not resource CRUD) on top; desired state, reconciliation, identity, catalog, and orchestration in the middle; base, third-party, custom, and governed user-contributed services below.
* Reconciliation is treated as the engine, not a feature. The control loop — Observe → Analyze → Act — detects drift from manual changes and resolves it deliberately. A platform that provisions but does not reconcile is only right on day one.
* Abstractions earn their keep behaviorally: sensible defaults, a short list of values developers may set, restrictions on what they must not touch. A template with a long, confusing parameter list has *increased* cognitive load, and we move to higher-level orchestration instead.
* Every generated resource links back — by reference, tag, or identifier — to the platform construct that created it, and errors name the relevant specification. An abstraction without that path does not ship.
* The platform-versus-application ownership boundary is written down: application teams get enough configuration control to avoid ticket friction; the platform keeps only the restrictions security and compliance genuinely require.
* Tenancy is a conscious decision — what a tenant is, which of the three tenancy approaches we use, which isolation level (logical, namespace, resource) — with noisy-neighbor fairness validated and the control plane tested against reconciliation bursts before adoption performs that test involuntarily.

**What it costs**

* A reconciling control plane is real machinery — built or delegated to tools like Kubernetes or cloud automation — and strictly more work than provisioning scripts.
* Traceability and the cognitive-load review are standing acceptance criteria on every abstraction, which slows shipping abstractions and is meant to.
* Burst and scale testing happens before general availability, not after the first post-outage callback storm.

**What we are not doing**

* Not deciding what the platform should contain — that is [[designing-platforms]]; nor how to run it in production — that is [[operating-platforms]].
* Not team setup — [[organizing-for-platforms]] owns that; this record only fixes the platform/application responsibility boundary.
* Not endorsing technologies — the record stays at the anatomy level; specific tools appear only as illustrations.

*The Article tab carries the rationale and anti-patterns; the Checklist tab holds the plane-by-plane build checklist and the final readiness check.*
