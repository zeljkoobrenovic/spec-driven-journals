---
timetoread: "8 min listen"
---

## Three Planes or a Pile of Scripts

**Ben:** Straight question. Our team can provision anything with Terraform and a wiki page. Why do I need an "anatomy" with three planes and a control loop?

**Ana:** Because scripts create resources, and a control plane *owns* them. The anatomy is the difference between a platform and a pile of provisioning scripts: a management plane developers actually touch — portal, CLI, APIs, maybe an automation language; a control plane that records desired state and continuously reconciles it with reality; and a services plane that does the actual work — base infrastructure, third-party products, custom services behind defined interfaces, even governed user-contributed ones.

**Ben:** That sounds like an architecture diagram. What breaks without it?

**Ana:** The middle. Everyone builds the top and bottom — a portal and some services — and skips the reconciliation machinery because provisioning already works. But a platform that provisions and doesn't reconcile is only right on day one. Manual changes drift it, updates don't propagate across tenants, failures don't self-heal. Nobody notices until an audit or an outage does.

**Ben:** Isn't "build a reconciling control plane" a bit rich for most teams? That's serious machinery.

**Ana:** It is, and the record doesn't demand you hand-build it. Delegating the loop to Kubernetes or cloud automation is a legitimate implementation choice — the requirement is that the loop exists: Observe, Analyze, Act, repeated forever, diffing desired against actual state and resolving drift deliberately. What's not legitimate is skipping the engine and calling the scripts a platform.

## Self-Service and the CRUD Portal

**Ben:** Fine, the middle matters. Now the top. Every platform pitch I've seen starts with a beautiful portal. Necessary?

**Ana:** A beautiful portal, no. Self-service, absolutely — it's what makes it a platform rather than a team with a queue. If developers can't provision what they need through a portal, CLI, or API, every request becomes a ticket and every ticket becomes a human, and humans doing ClickOps don't scale. An API and CLI serving real journeys beat a lavish UI serving none.

**Ben:** "Real journeys" versus what?

**Ana:** Versus the CRUD portal — raw resource operations rendered in nicer colors. The management-plane test is whether the platform supports what developers are actually trying to accomplish, the user journeys, not whether every resource type has a create-read-update-delete screen. And self-service includes seeing what you have: an inventory of provisioned services with compliance and reference-architecture status visible, not just a button for getting more.

## The Two Tests

**Ben:** Let's do abstractions. The platform's whole pitch is hiding complexity. But I've watched teams wrap a cloud resource in a "simple" template with forty parameters. How is that better than the raw resource?

**Ana:** It's worse, and the record says so explicitly. That's the forty-parameter template anti-pattern — all the indirection of a platform with none of the cognitive-load reduction. Hohpe's warning is precise: excessive exposure to underlying resource definitions can *increase* cognitive load. So my acceptance test for any abstraction is behavioral, not architectural — did the developer's world actually get simpler?

**Ben:** And when a template can't pass that test?

**Ana:** Then templates were the wrong tool, and we move up to real orchestration — translation, composition, lookup, model translation where the platform's metamodel differs from the cloud's. The mechanics of a passing abstraction are consistent: sensible defaults for most things, a short list of values developers may provide, and clear restrictions on what they must not touch.

**Ben:** Here's my sharper worry. Every abstraction hides something. When the hidden thing breaks at 2 a.m., the developer is stranded on the wrong side of your beautiful abstraction.

**Ana:** That's the second test, and it's non-negotiable: traceability. Every generated resource links back — by reference, tag, or identifier — to the platform construct that created it, and error messages name the relevant specification. An abstraction that hides resources without providing that troubleshooting path does not ship. That's the trapdoor abstraction, and it's how platforms lose their best engineers — the first unexplainable failure converts an advocate into someone who builds around the platform.

**Ben:** So the two tests together: it must make life simpler, and it must let you climb back out.

**Ana:** Exactly. A platform that hides complexity without a troubleshooting path hasn't reduced cognitive load. It's deferred it to the worst possible moment.

## Who Owns What

**Ben:** Next fight: control. Platform teams love guardrails; application teams experience them as a ticket queue with extra steps. Why not just give teams root and hold them accountable?

**Ana:** Because some restrictions aren't the platform team's preference — they're what security and regulatory compliance genuinely require, and those stay platform-owned. But the record agrees with your instinct more than you'd think: platform speed is lost less in technology than in tickets. So application teams get enough configuration control to act without asking. Guardrails instead of gates.

**Ben:** And where exactly does the line sit?

**Ana:** Wherever you write it down — that's the actual requirement. Who owns provisioned resources, who gets which access rights, where the platform keeps lifecycle control. The content varies by platform; what's forbidden is leaving it implicit, because an implicit ownership boundary gets renegotiated in every incident. How the teams on each side of that line are staffed and led is [[organizing-for-platforms]] — this record just fixes the line.

## Tenancy Is a Decision

**Ben:** Last technical push. Tenancy models, isolation levels, noisy-neighbor fairness — for a platform with three internal customers? Sounds like premature optimization.

**Ana:** It sounds like that right up until it doesn't, because tenancy and scale failures arrive together and they arrive late. These decisions are cheap on a whiteboard and brutally expensive to retrofit. The record asks for consciousness, not gold-plating: name what a tenant is, choose deliberately among multi-tenant resources, multi-tenancy in the platform, or independent instances, and know which isolation level you picked — shared logical resource, namespace, or fully separate instance — and what it trades.

**Ben:** The alternative being?

**Ana:** Tenancy by accident — the isolation model is whatever the first prototype happened to do, and you discover noisy neighbors, cross-tenant exposure risk, and quota limits in production, with real customers attached.

**Ben:** And scale? Everyone load-tests.

**Ana:** They test normal load. Hohpe's warning is about the other kind: uneven callback bursts — after an outage, during mass updates — that overload a control plane whose everyday scale is moderate. Fifty tenants smooth, a thousand fine, until the first post-outage reconciliation storm. So we test bursts before adoption performs the test for us. Which matters double because [[growing-platforms]] is working to make that adoption arrive.

## The Fences and the Tripwires

**Ben:** Close it out. What is this record explicitly not?

**Ana:** Four fences. It's not what to design *into* the platform — boundaries and content are [[designing-platforms]]; this is how the design becomes a running system. It's not running the result in production — reliability, on-call, and support are [[operating-platforms]]; this builds the machinery they operate. It's not team setup — that's [[organizing-for-platforms]], minus the ownership boundary we fixed here. And it's not a technology endorsement — Kubernetes appears as an illustration of delegating the control loop, never as a recommendation.

**Ben:** And what would make you reopen it?

**Ana:** Three tripwires. Developers keep escaping the abstractions to work at the raw-resource level — the cognitive-load test failing in the field. A production incident can't be traced back to the specification that caused it — the traceability test failing. Or control-plane load and tenant-isolation incidents show the tenancy model was outgrown rather than chosen. Any of those means the implementation drifted from the bar, and the bar is the point.

**Ben:** One sentence for the road.

**Ana:** Three planes, one engine, two tests: developers touch self-service, reconciliation keeps it true, and no abstraction ships unless it makes the world simpler *and* leaves a path back through it when things break.
