---
timetoread: 8 min listen
---

## Why should I care?

**Ben:** Let me start blunt. I'm an engineering leader with a backlog and a roadmap tool. Why do I need customer groups and "jobs to be done" before anyone talks about systems and APIs?

**Ana:** Because by the time most teams talk about systems, the customer model is already gone. It's been flattened into feature requests. Product architecture then becomes a translation exercise — engineers inferring the real product shape from tickets, roadmaps, and stakeholder memory. Spec-Driven Product Architecture changes the order: start with customer value, and keep that value connected all the way down to architecture decisions.

**Ben:** "Start with the customer" is on every conference slide. What makes it architectural rather than an empathy exercise?

**Ana:** The separation does. The first architectural question isn't "which systems do we need?" — it's "whose progress are we supporting?" In a ride-sharing marketplace, riders, drivers, fleet operators, business travel administrators, and marketplace operators don't experience the product the same way. And different groups pull the system in different directions. A customer who needs real-time confidence pulls you toward reliable state, live signals, and observability. A customer making a procurement or compliance decision pulls you toward evidence, approvals, access controls, auditability. High-frequency users pull toward ergonomics and low latency; exception resolvers pull toward case management and recoverability.

**Ben:** So the grouping isn't decoration — it's load-bearing.

**Ana:** Exactly. Customer grouping is one of the first ways the architecture discovers its shape. Collapse everyone into one generic persona and every downstream artifact sounds the same — which is the first failure mode the article warns about.

## Jobs, not features

**Ben:** Fine, groups. But "jobs to be done" — half the job statements I've seen are just feature names with a verb. "Use search." "Open the dashboard."

**Ana:** Those are exactly the weak examples the article calls out. "Use search" versus "find a stay that feels trustworthy for a family trip within budget and schedule constraints." "Open a deployment dashboard" versus "understand whether a production change is safe enough to release and recover quickly if it fails." The job should describe the progress a customer is trying to make, not the product feature they click.

**Ben:** Does the distinction actually change anything, or is it wordsmithing?

**Ana:** It changes everything for AI agents, which is part of why this series exists. If the agent models jobs as feature usage, it produces a feature inventory. If it models jobs as progress, it can reason about outcomes, frictions, capabilities, and missing architecture. The model is also strict about two journey stages, and this trips people up constantly: **discovery** means how customers become aware of the offer before active use, and **evaluation** means how they decide whether the product is right before trial or commitment. Those words are never reused as labels for in-product search or task execution.

**Ben:** Why be pedantic about two words?

**Ana:** Because reusing them mixes three different things — market acquisition, product usage, and operational workflows — into one vocabulary. Once that language blurs, the model can't tell whether "discovery" needs an SEO investment or a search service. Keeping the language clean is cheap; untangling it later isn't.

## Making value measurable

**Ben:** Next objection. KPI pyramids. Every company I've worked at had a metrics tree somewhere, lovingly built, never consulted. Vanity dashboards with extra steps.

**Ana:** The article's answer is that the goal isn't a dashboard at all — it's making the product architecture *testable*. Customer value becomes operational when it has measurable signals. Riders need reliable trips? Then the model says: request-to-match time, pickup success rate, ETA accuracy, cancellation rate. Developers need usable golden paths? Time to first successful deployment, policy exception rate, paved-road adoption.

**Ben:** And the failure mode is what — metrics that are too soft?

**Ana:** Leaves that aren't leaves. A branch named "Experience" is not enough. The model should say what observable signal proves the experience is improving. If a later architecture discussion can't ask "is the system actually moving this number?", the KPI isn't doing its job.

**Ben:** You also want strategy horizons in the model. One-year, three-year, five-year. That smells like corporate planning theater.

**Ana:** It's theater only if the horizons are slogans. Each horizon has to answer concrete questions: what's the focus, which product theme dominates, which customer KPI should improve, which business KPI should improve, which milestones show progress. That's where product vision becomes a planning *constraint*. A capability irrelevant to the one-year horizon may still matter as a three-year investment. A product brick that's operationally critical today may need to be contained, replaced, or sunset by a later horizon. Without horizons, the model only describes the current product — it can't say where the product is going.

## The chain

**Ben:** OK, so groups, jobs, KPIs, horizons. At some point this has to touch actual architecture or it's a product-management document.

**Ana:** That's the central move of the whole post: the chain. Customer group, job to be done, desired outcome, KPI signal, strategy horizon, product capability, product brick, delivery release, owning team. Nine steps, and customer value stays visible as it moves downward.

**Ben:** Walk me through it. Concretely.

**Ana:** The running example is a ride-sharing marketplace. Customer group: riders who need reliable on-demand travel under time pressure. Job: get matched with a trustworthy trip that arrives when expected. Desired outcome: a completed trip with accurate ETA, transparent price, safe handoff. KPI signals: request-to-match time, pickup success rate, ETA accuracy, cancellation rate. Horizon: improve reliability this year before expanding advanced marketplace optimization. Capability: book and complete a reliable trip. Bricks: trip request, matching and dispatch, pricing, payments, support and recovery. Delivery initiative: improve dispatch resilience and cancellation recovery. Owner: the marketplace matching team, coordinated with pricing, payments, trust, and support. And evidence underneath: analytics, support tickets, incident data, driver availability, financial impact.

**Ben:** And without the chain?

**Ana:** Without it, product bricks are a technical catalog. With it, they're a product architecture. Teams own systems either way — but only with the chain can someone explain *which customer value* those systems support.

## Where this breaks

**Ben:** Be honest about the cost. A nine-step chain across every customer group sounds like a maintenance treadmill.

**Ana:** The article is explicit: the chain doesn't need to be perfect in the first draft. But it needs to *exist*, because it gives future AI sessions something to inspect and improve. The failure modes are predictable, and they're all forms of the chain quietly rotting: customer groups too generic, jobs that describe features, KPIs with vague labels, horizons that are slogans without milestones, capabilities and bricks that appear with no connection to customer outcomes.

**Ben:** And those failures matter beyond editorial tidiness?

**Ana:** That's the punchline. They reduce the usefulness of AI agents directly — the agent cannot maintain coherence that the model does not express. Sloppy modeling isn't a documentation problem anymore; it's a capability ceiling on every AI session that touches the domain. That's the same argument [[product-domain-as-source-of-truth]] makes for the model as a whole.

## What we're not saying

**Ben:** Closing question. What should I *not* take from this record?

**Ana:** Three deliberate non-goals. It's not a full customer modeling tutorial — it shows why the customer layer comes first, not how to run research. It's not domain-specific customer research; the examples deliberately span ride-sharing, developer platforms, and marketplaces so it doesn't become one domain's case study. And it doesn't calibrate KPI targets — it argues for concrete, measurable leaves, not for particular numbers.

**Ben:** So the takeaway in one line: don't start architecture at the systems layer.

**Ana:** Start with whose progress you're supporting, and never let the model lose that thread. Once customer value is explicit, the next task is making it buildable without collapsing into implementation detail — and that's exactly where [[product-bricks-and-capabilities]] picks up.
