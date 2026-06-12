---
timetoread: 8 min listen
---

## Why so many domains?

**Ben:** Honest question. The repository models ride sharing, online retail, public cloud, a premium airline, audio streaming, freight logistics, industrial water intelligence... That reads like a demo reel. Why does a method need twenty example domains?

**Ana:** Because the variety *is* the method. AI agents improve when they can inspect examples — but examples only teach when they show both consistency and variation. If every example is the same type of product, the agent learns a narrow pattern and over-applies it everywhere. If every example uses a different structure, there's no stable model to follow at all. You need many domains that share one modeling language and disagree on everything else.

**Ben:** So it's a training set, not a showcase.

**Ana:** A pattern library, yes. And there's a published [product-domain overview](https://zeljkoobrenovic.github.io/spec-driven-product-architecture/start-packages/overview/index.html) that works as the map — agents and reviewers use it to compare domains before choosing which ones to inspect deeply.

**Ben:** Fine, but "consistency and variation" sounds like one of those phrases that can justify anything. What concretely stays the same?

**Ana:** The modeling language. Across every domain you should be able to express the product through the same building blocks: customer groups, personas, jobs to be done, journeys, KPI pyramids, strategy horizons, deployments, channels and APIs, product capabilities, product bricks, data assets, objectives and initiatives, teams and ownership, evidence. That stability is what lets an agent transfer learning — a new domain borrows the *structure* of mature domains without copying their business content.

## The mush problem

**Ben:** Here's my worry with that list. Once you have a fixed set of categories, every domain starts answering them the same way. Give a template to enough people and you get twenty copies of the template. What stops a ride-sharing marketplace and an airline from ending up with the same capabilities under different names?

**Ana:** That's exactly the failure mode the article names — standardizing the domain story into mush. And the defense is the split: the reusable model asks the same *categories* of questions, but each domain must answer them differently. A ride-sharing marketplace genuinely has live supply-demand balancing, dispatch, pricing, driver earnings, city operations. A public cloud domain has developer APIs, governance, reliability, marketplace services, usage-based economics. A premium long-haul airline has retailing, loyalty, disruption recovery, partner connectivity, cargo, regulated service delivery. Those aren't renamed versions of each other.

**Ben:** Give me the question-and-answer version.

**Ana:** Same question: who are the materially different customers? Riders and drivers in one domain; developers and platform teams in another; travelers and airline operations in a third. Same question: which KPIs prove improvement? ETA accuracy, deployment lead time, recovery time — completely different answers. The reusable question is the invariant. The answer is the domain.

**Ben:** And the diversity of examples is what keeps that honest?

**Ana:** Right. If all the examples were marketplaces, the method would quietly turn into a marketplace template that fills itself. The airline, the cloud platform, the water-intelligence domain — they force the structure to prove it generalizes without flattening anything.

## Archetypes, not an inventory

**Ben:** Twenty-plus domains is still a lot to inspect. If I'm an agent — or a human — starting a new domain, where do I even look first?

**Ana:** That's where archetypes come in. The existing set clusters naturally: **marketplaces** like ride sharing, local delivery, travel accommodations, online retail; **platforms** like the internal developer platform, public cloud services, the cloud data and AI platform; **regulated or operational services** like the premium airline, payments infrastructure, industrial water intelligence; **enterprise systems** like CRM and enterprise architecture management; and **consumer subscription or content products** like audio streaming and digital news. A new marketplace should inspect marketplace domains. A new developer tool should inspect platforms. A regulated product should inspect the domains where compliance and evidence are strong.

**Ben:** Why archetypes rather than just documenting every domain in detail?

**Ana:** Deliberate choice, and it's in the spec's decision log: representative archetypes rather than an exhaustive inventory, to keep the thing readable. There's an open question about whether to later expand three domains into proper case studies — but cataloguing everything was rejected.

**Ben:** One caveat I'd want on record: archetypes sound like they could become a shortcut. "It's a marketplace, copy the marketplace."

**Ana:** The article is explicit about that — archetypes guide comparison, they do not replace repository reading. The agent still has to inspect what the generators actually expect and what the current schemas look like. Which brings us to the part people underestimate.

## Depth and drift

**Ben:** Go on.

**Ana:** Examples teach *depth*. Without them, an agent produces a shallow skeleton — three customer groups, five generic capabilities, ten vague product bricks, a team list with no ownership, a roadmap that reads like a project plan. Mature examples show a higher bar: customer groups with distinct jobs and fears, KPI trees with specific leaves, bricks with modules and dependencies, capabilities composed from multiple bricks, teams that plausibly own them, assumptions made visible. The examples are how the repository makes "good enough" concrete instead of leaving it as taste.

**Ben:** Okay, but here's the cost question. A living repository with twenty domains — they can't all be equally current. Some were authored against older schemas, file names move, generator expectations shift. Your pattern library is partly a museum.

**Ana:** True, and the article doesn't hide it — it calls it schema drift, and it's the price of a living example set. The consequence is a rule: inspect before editing. Which comparable domains look most mature? Which file names do the generators actually expect now? Which schema shape is canonical? Are there legacy fields that shouldn't be copied? Copying an old pattern blindly doesn't just produce one stale domain — it *preserves* the drift and propagates it forward.

**Ben:** So the examples are simultaneously the quality bar and a drift hazard.

**Ana:** Yes — and that tension is why [[ai-agents-as-product-architecture-authors]] insists agents work inside validation and current schemas rather than freestyle from any one example. The quality test for the whole example set is simple: does a fresh AI session, inspecting the repository, infer how deep a mature domain should be, how to separate market facts from assumptions, how to avoid generic brick filler, how to wire capabilities to bricks and teams to ownership? If yes, the diversity is doing its job.

**Ben:** Can a reader actually check that, or do they have to take your word for it?

**Ana:** They can check it directly — that's why the article ends with a table pairing each representative generated domain page with its GitHub source specification folder. The useful way to read an example is source next to publication: the spec folder shows what the agent and human reviewers authored; the generated pages show how that model becomes navigable documentation. Ride Sharing Marketplace is the one to start with, since it's also the running example of the whole series.

## What we're not claiming

**Ben:** Let's close the way we usually do. What is this record explicitly *not* saying?

**Ana:** Three non-goals. It's not a deep comparison of all existing domains — archetypes and a link table, not a survey. It's not a maturity ranking; nobody is grading domains against each other. And it's not market analysis — the airline domain doesn't tell you anything true about the airline industry beyond what the modeling needed.

**Ben:** And the examples themselves — final form?

**Ana:** Explicitly not. The examples are not final truth; they're a growing pattern library for structured product-architecture work. The open question on the spec is whether to expand a few domains into full case studies later. And the revisit trigger is built into the method: when a new session inspects the repository and *can't* infer the quality bar, the example set needs work.

**Ben:** A demo reel that turned out to be the curriculum. Fine — I'll allow it. *(laughs)*

**Ana:** And if you want the trust side — how evidence and validation keep that curriculum honest — [[evidence-validation-and-publishing]] closes the series with exactly that.
