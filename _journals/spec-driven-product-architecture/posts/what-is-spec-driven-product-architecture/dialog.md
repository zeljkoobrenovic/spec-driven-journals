---
timetoread: 8 min listen
---

## Why should I care?

**Ben:** So give it to me straight. "Spec-driven product architecture" — isn't this just spec-driven development with a fancier name?

**Ana:** That's exactly the right first question, because the difference is the whole point. Spec-driven development starts close to code: you write a spec, an agent or a developer implements it, tests check the match. Useful — but narrow. Spec-driven product architecture moves the specification boundary upward. The spec isn't a feature brief or a technical design. It's a structured model of the entire product domain.

**Ben:** Why does the boundary need to move? The code is where things actually break.

**Ana:** Is it, though? Most products fail to stay coherent *before* code appears. Customer groups are described in one document, product vision in another, architecture in diagrams, roadmap in planning tools, teams in org charts, evidence scattered everywhere. Nothing connects them. And here's the uncomfortable part: AI agents make that worse, not better, when there's no shared structure. They happily produce plausible text for every one of those artifacts — text that's hard to compare, hard to validate, and impossible to trace back to delivery reality.

**Ben:** So the pitch is: one model to rule them all?

**Ana:** One model to *connect* them all. Eight layers, concretely: customers, strategy, delivery, product capabilities, product bricks, teams, roadmap, and evidence. Written as structured JSON, rendered into documentation, maintained by humans and AI agents together. Vision flows down into customer groups, capabilities, implementation-facing bricks, ownership, and sequencing — and every layer can be inspected.

## The vision objection

**Ben:** Let me push back. Plenty of great products were built on a strong vision and a whiteboard. "Build a better ride-sharing marketplace" — a good team fills in the rest.

**Ana:** A good *human* team, with years of shared context, maybe. Now hand that sentence to an AI agent. "Build a better ride-sharing marketplace" doesn't tell it how rider jobs connect to dispatch, pricing, risk, payments, driver earnings, or marketplace analytics. Vision is necessary — it's just not operational. It becomes operational when the model can answer practical questions: which customer groups are materially different? Which jobs to be done drive the outcomes that matter? Which KPIs say whether they're improving? Which capabilities make them possible, which bricks support those capabilities, who owns the bricks, and which roadmap items change them?

**Ben:** That's a long list of questions for a planning artifact.

**Ana:** Those questions *are* the spec. That's the reframe. The spec isn't prose describing intent — it's a structure that can answer.

## Dreaming, exploring, grounding

**Ben:** You keep saying "evidence." Architecture documents are famously fiction. What stops this model from being beautifully structured fiction?

**Ana:** The three modes — this is my favorite part. **Dreaming** defines the intended product: vision, customer value, capabilities, target architecture, roadmap. **Exploring** looks at what's actually happening, through real data — source-code maps, cloud activity, deployment and incident history, finance data, ownership signals. That part inherits directly from Grounded Architecture and its data-led practice. And **grounding** is the explicit join: does this product brick map to real repositories and services? Does this team-ownership claim match repository activity and incident responsibility? Does this roadmap target respond to an observed trend, or only to an aspirational story?

**Ben:** And when a concept has no evidence? Early-stage products are mostly bets.

**Ana:** Then it stays in the model as a *visible* assumption. The goal isn't to reject every concept that lacks evidence — early product architecture always contains bets. The goal is to make the bets explicit, keep the model current, and notice when reality starts drifting away from the dream. Fiction is fine when it's labeled fiction.

## Where the AI fits

**Ben:** You said agents amplify fragmentation. Now you want them maintaining the model. Which is it?

**Ana:** Both — structure is the difference. Without it, an agent asked to "write a strategy" produces general strategy prose. With structure, examples, and validation, the same agent edits source files: `customers.json`, `product-bricks.json`, capability maps, release models. It has to work inside a domain language, preserve stable IDs, reuse schema patterns, keep references consistent, and pass validation before anything generated is trusted. That's a different operating model — the agent is an author inside a constrained language, not a text generator.

**Ben:** Constrained languages have a way of drifting into abstraction. Strategy frameworks especially — customers, needs, value propositions, and then a chasm down to actual systems.

**Ana:** Which is why the model is deliberately application-aware. A product brick isn't just a feature and isn't just a system — it's an implementation-facing unit that can be built, owned, and evolved: user-facing components, APIs, message consumers, services, data dependencies, dependencies on other bricks. Capabilities then describe the outcome-based combinations of bricks that produce customer or business value. It keeps enough implementation structure to support real delivery conversations, not just market positioning.

## What this isn't

**Ben:** Closing question. What should I *not* expect from this series?

**Ana:** Three things, deliberately. It's not schema documentation — the layers matter more than field-by-field detail. It's not a tutorial for building a full product domain end to end. And it's not a decision record telling your organization to adopt this — it's an introduction to a method, with the public repository as the working implementation.

**Ben:** And if I want the next layer down?

**Ana:** Start with [[product-domain-as-source-of-truth]] — why the domain folder is the source of truth — then the series walks the model layer by layer, with a ride-sharing marketplace as the running example. Concrete enough to show the model end to end; not so specific that the method only works for marketplaces.

**Ben:** Structured enough to be useful, durable enough to survive change. I've heard worse pitches. *(laughs)*

**Ana:** That's the whole goal — a shared product-architecture language for humans and AI agents. The dream, the data, and the join between them.
