---
timetoread: 8 min listen
---

## Why should I care?

**Ben:** Straight question first. Architecture is structure. Delivery is process. Team design is org charts. Three disciplines, three owners, three tools. Why is this article insisting on stuffing all of them into one product architecture model?

**Ana:** Because the separation is a fiction we maintain at our own expense. A product architecture that ignores delivery cannot explain how change happens. A delivery plan that ignores architecture cannot explain *what* is being changed. A team model that ignores product bricks cannot explain who owns the durable parts of the product. In practice the three are inseparable — the model just makes that visible.

**Ben:** "Inseparable" is easy to say. Give me the architectural argument for, say, delivery. Why is a release schedule an architecture concern?

**Ana:** Because delivery information shapes interfaces, dependencies, reliability needs, and ownership boundaries. A product delivered through mobile apps, partner APIs, and backoffice operations has a different architecture than one delivered through a single web workflow. A product with regulated approvals has different delivery constraints than a consumer experiment platform. A marketplace with live supply-demand balancing has different release risk than a static content site. The delivery model — channels, APIs, operational workflows, MVP scope, releases, risks — records those differences explicitly instead of leaving them as tribal knowledge.

## Teams own bricks, not tasks

**Ben:** Let's do teams. Every org I've seen has a team list. What does putting it in the architecture model add?

**Ana:** The team list answers "who exists." The model has to answer harder questions: which product bricks does this team own? Which capabilities does it enable or coordinate? Which dependencies create collaboration needs? Which operating responsibilities are ongoing? Which teams need platform, data, reliability, or compliance support? Teams own bricks, not just tasks — that's the rule. The bricks come from [[product-bricks-and-capabilities]]; the team model gives them an ownership surface.

**Ben:** Sounds tidy on a slide. Reality is messier — shared platforms, capabilities that need four teams, operational handoffs. Does the model pretend each brick has its own neat little team?

**Ana:** Explicitly not. Some capabilities require multiple teams. Some platform bricks serve many teams. Some workflows require handoffs. The requirement is not one-brick-one-team — it's that those realities are *visible*. There's a dependency view for exactly this: a team can look well-scoped on paper and still depend on shared bricks, enabling teams, and supporting platforms that need to be planned explicitly. The model exposes the coordination work instead of letting it surprise you mid-quarter.

**Ben:** And if ownership is fuzzy?

**Ana:** Then you've found the rot early. Hidden ownership is one of the fastest ways for product architecture to decay. A brick nobody owns gets changed by everyone and maintained by no one.

## Roadmaps that point somewhere

**Ben:** Now roadmaps. Mine is a list of initiatives in a planning tool, reviewed quarterly, and honestly it works fine. What's wrong with it?

**Ana:** Nothing — for planning. It's weak for architecture, unless the initiatives point back to the model. A strong roadmap item references the customer groups or jobs it improves, the KPIs it should move, the capabilities it creates or changes, the bricks it builds, evolves, or retires, the teams involved, the releases or targets it belongs to, and the evidence or assumptions behind it.

**Ben:** That's a lot of metadata for a planning ticket.

**Ana:** It's the difference between asking "what are we doing next quarter?" and being able to ask: which customer outcome does this item change? Which bricks are affected? Which team owns the long-term capability after delivery? Which dependencies make it risky? Which target state does it move us toward? Which assumptions must be validated first? The roadmap becomes an overlay on the architecture, not a disconnected plan. Sequencing turns into an architecture discussion instead of calendar management.

**Ben:** You also model objectives and "discoveries." Why drag OKRs into an architecture repository?

**Ana:** Because product architecture is never fully known upfront, and the model should support uncertainty rather than hide it. Discoveries capture hypotheses and unresolved constraints. Objectives express outcomes and priorities. Initiatives create movement; targets describe desired future states. When those live next to the customer, capability, brick, and team model, a future session — human or AI — can ask: does this initiative still match the objective? Does this discovery change the capability map? Does this team own the brick the release depends on? That's nearly impossible when objectives live in one tool, architecture in another, and delivery notes in a third.

## The trace

**Ben:** Make it concrete. Walk the ride-sharing example through the whole thing.

**Ana:** The full trace, top to bottom. Customer group: riders who need dependable trips under time pressure. Job: get matched with a trustworthy trip that arrives when expected. KPIs: request-to-match time, pickup success rate, ETA accuracy, cancellation rate. Capability: book and complete a reliable trip. Bricks: matching and dispatch, coordinated with trip request, pricing, payments, and support. Team: the marketplace matching team owns dispatch reliability and coordinates with pricing, payments, trust, and support. Release: improve dispatch resilience and cancellation recovery. Roadmap target: reduce marketplace failure modes before expanding advanced optimization. Evidence underneath: product analytics, support tickets, incident history, repository ownership, cloud activity, financial impact.

**Ben:** And that trace is the actual payoff?

**Ana:** It's the main reason to keep delivery, teams, and roadmaps inside the model at all. Every step is inspectable, so every step can be challenged.

## The review surface

**Ben:** One more skeptical pass. You generate a documentation site from all this. Isn't that just publishing?

**Ana:** At this stage it's more than publishing — it's a review surface for the operating model. Raw JSON serves agents and validation; rendered pages serve humans. And here's the useful part: if the generated page for a domain feels disconnected, that's feedback on the *source model*. Maybe the customer groups are vague. Maybe bricks don't map to capabilities. Maybe teams are named but not connected to ownership. Maybe roadmap items read like generic plans. The review goes back to source — the same loop [[product-domain-as-source-of-truth]] establishes.

**Ben:** So how do I know when the model is good enough? There must be a test.

**Ana:** The operating test: can the model help a team make better decisions? Should this initiative be prioritized? Which brick carries the long-term responsibility? Which team should own the change? Which capability is missing? Which customer outcome is unsupported? Which dependency creates risk? If it can't help answer questions like those, it may be a useful description — but it's not yet an operating product architecture.

## What we're not saying

**Ben:** Close it out. What is this record *not* telling me to do?

**Ana:** Three non-goals, on purpose. It does not prescribe a delivery methodology — model how delivery works; pick your own process. It's not a release-planning template. And it's not a team topology tutorial — teams can be stream-aligned, platform, enabling, data, compliance, whatever the domain demands; the only rule is a plausible relationship between teams and the bricks and capabilities they affect.

**Ben:** So the headline: my org chart, my roadmap tool, and my architecture diagrams are describing one system, and only the model admits it.

**Ana:** That's the whole argument. And the natural next question — how AI agents help author all of this without turning it into disconnected generated prose — is exactly where [[ai-agents-as-product-architecture-authors]] picks up.
