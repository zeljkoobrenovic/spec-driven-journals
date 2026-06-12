---
timetoread: 9 min listen
---

## Outcomes or inventory?

**Ben:** Capabilities, bricks — that sounds like two names for the same thing. Why does this model need both?

**Ana:** Because they sit on opposite ends of the most important bridge in the whole approach: the bridge between product outcomes and implementation reality. If the model stays at the outcome level, it's product strategy prose. If it jumps straight to systems and services, it's a technical inventory. Capabilities and bricks keep both sides visible — and connected.

**Ben:** Fine, but give me the actual distinction. What's a capability?

**Ana:** Something valuable the product can do for customers or the business. Good capability names sound like outcomes: "book and complete a reliable trip," "launch and tune marketplace changes with controlled experiments," "feed analytics and machine learning with fresh governed data." Notice none of those are system names.

**Ben:** They also sound suspiciously like epics. Or team missions. Why isn't a capability just a big backlog item?

**Ana:** Because capabilities are deliberately none of those things. Not modules, not teams, not epics. They're durable product abilities that often require several bricks, external systems, data assets, and operational workflows to deliver. An epic finishes; a capability persists. The reason this matters is language: capabilities preserve the language of value, so product leaders, architects, and AI agents can discuss what the product must be able to do before anyone argues about how the system does it.

## What makes a brick a brick

**Ben:** Okay, so the "how" lives in bricks. What is a brick, concretely?

**Ana:** A buildable, ownable part of the product architecture. More concrete than a capability, more product-aware than a low-level component. A brick can include user interface modules, APIs, services, message consumers, integrations, data dependencies, and dependencies on other bricks.

**Ben:** That's a description of a microservice with extra steps.

**Ana:** It's deliberately not a deployment unit. The test for a brick is five properties: buildable — a team can implement and evolve it; ownable — it has a clear primary owner; traceable — it supports capabilities, outcomes, delivery plans, and evidence; coherent — its modules belong together for a product or platform reason; and durable — its ID survives wording changes and roadmap cycles. A microservice might satisfy those. So might a mobile app surface plus its BFF plus the integration behind it. The boundary is a product reason, not a runtime.

**Ben:** And why should an AI agent care about any of this?

**Ana:** Because bricks are the key to application awareness. When an agent authors the model, bricks force it to say which implementation structures must actually exist for the strategy to be real. Without that forcing function, you get beautifully worded strategy that no team could ever pick up and build.

**Ben:** You mentioned structure. I've seen architecture catalogs with sixty entries in a flat list. Is that what a bricks file looks like?

**Ana:** That's exactly one of the two failure modes the structure exists to prevent. Bricks use a meaningful three-level structure: root group, subgroup, brick. The root group is a durable product or platform area, the subgroup organizes related workflows or capabilities, and the brick is the implementation-facing unit. That avoids both extremes — the flat list of sixty unrelated bricks, and the shallow set of vague buckets like "platform," "data," and "experience." You get a navigable architecture in the generated documentation, and a source model clear enough for agents to maintain.

**Ben:** And below the brick?

**Ana:** Modules. A module might be a web component, a mobile component, a BFF, an API, a backoffice interface, a message consumer, a stateless service, a stateful service, an integration. They're grouped into layers — `ui`, `interfaces`, `bus`, `stateless-service`, `service`, `integration`. Crucially, this is not full solution design for every domain. It's enough architectural shape to make dependencies, ownership, and delivery implications visible. No more.

## Where the model gets honest

**Ben:** That still sounds like diagram theater. Pretty boxes, nicely grouped. Where's the payoff?

**Ana:** Dependencies. That's where the model gets honest. A brick depends on another brick. A module calls or consumes another module. A brick owns or uses data assets. A capability depends on several bricks and external systems. Once those connections are explicit, you can see whether the strategy is plausible.

**Ben:** Plausible how?

**Ana:** Take a capability like "resolve trip issues through self-service and assisted support." It might depend on trip state, payments, customer identity, support case handling, trust operations, and analytics. If those bricks are missing, or owned by disconnected teams, the capability isn't just "hard" — it's architecturally under-specified. The model makes that visible before delivery surprises arrive, not after.

**Ben:** Walk me through the ride-sharing example properly. You keep using "book and complete a reliable trip."

**Ana:** That's the running example, and the point is that it's a capability, not a brick — it's an outcome the product must deliver. The implementation-facing model has to show what makes it real. Which bricks support it? Trip request and intent capture, matching and dispatch, pricing and offer management, driver availability, payments and settlement, support and recovery. Which modules make those concrete? Rider and driver app surfaces, a pricing API, a dispatch service, event consumers, a trip-state store, payment authorization, support-case tooling. Which dependencies matter? Driver supply, map and routing providers, payment providers, fraud and safety workflows, marketplace analytics.

**Ben:** That's a lot of bricks for one sentence of outcome.

**Ana:** Which is precisely the information the sentence was hiding. And the model doesn't stop at structure — it raises the ownership questions: who owns dispatch reliability, who coordinates pricing changes, who handles recovery when the trip flow breaks? And the evidence questions: ETA accuracy, cancellation patterns, incident history, repository ownership, cost signals. Capabilities become reviewable when you can see which bricks, modules, data assets, external systems, and teams make the outcome possible. That trace runs all the way up from [[customer-value-to-architecture]] — the customer value that justified the capability in the first place.

## How agents get it wrong

**Ben:** You said agents author these files. I can already picture the failure. Every domain gets "analytics," "identity," and "notifications."

**Ana:** *(laughs)* You just named one of the three documented drift patterns. Generic platform filler — the same stock entries regardless of what the domain actually needs. The other two: feature lists, where each brick is a user-visible feature with no implementation boundary; and technology catalogs, where each brick is a system name with no customer value attached.

**Ben:** And the antidote is what — a stern comment in the schema?

**Ana:** Traceability. A brick should be justified by customer value, capability needs, delivery workflows, or operating constraints. A capability should point to the bricks that make it possible. A team should be able to own or coordinate the bricks it's assigned. If a brick can't answer "which outcome do you serve, and who owns you?", it doesn't belong in the model. That cuts the filler quickly — generic "analytics" survives only if a real capability actually depends on it.

**Ben:** So the two concepts discipline each other.

**Ana:** That's the heart of it. Capabilities without bricks are aspirations. Bricks without capabilities are inventory. The useful model has both: the capability answers "what outcome must the product deliver," the bricks answer "which implementation-facing units make that possible," the modules and dependencies answer "what sits inside and what does it touch," the team model answers "who owns it," and the roadmap answers "what changes it." That chain is the application-aware heart of spec-driven product architecture.

## What this isn't

**Ben:** Closing question. What should I not expect from this record?

**Ana:** Three things, deliberately out of scope. It's not a full product-brick JSON schema reference — the concepts matter more than the field list. It's not exhaustive module-type documentation. And it's not deep system design for any one domain — the brick model gives you enough shape to review dependencies and ownership, not a blueprint you could hand to a build team as-is.

**Ben:** And once I have capabilities and bricks in the model — what's next?

**Ana:** Then the model needs delivery, ownership, and sequencing — which bricks which teams own, and which roadmap items change which capabilities. That's [[delivery-teams-and-roadmaps]], the next step in the series.

**Ben:** Outcomes above, buildable bricks below, and an honest set of arrows in between. I can work with that.

**Ana:** That's the bridge. Keep both ends visible and the strategy stays real.
