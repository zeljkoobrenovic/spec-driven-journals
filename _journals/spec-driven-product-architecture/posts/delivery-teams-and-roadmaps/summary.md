---
timetoread: 2 min
---

Delivery, team ownership, objectives, releases, targets, and roadmap overlays belong inside the product architecture model — not in a separate project-management layer. A product architecture model becomes operable when all of these reference the same customer and brick model.

The argument is practical: architecture that ignores delivery cannot explain how change happens; a delivery plan that ignores architecture cannot explain what is being changed; a team model that ignores [[product-bricks-and-capabilities]] cannot explain who owns the durable parts of the product. Keeping them in one domain model makes the connections inspectable — by people and by AI agents.

**What changes**

- Delivery artifacts (channels, APIs, operational workflows, MVP scope, releases, delivery risks) are modeled as architecture, because they shape interfaces, dependencies, reliability needs, and ownership boundaries.
- Teams own product bricks and coordinate around capabilities, not just tasks. The model must answer which bricks a team owns, which capabilities it enables, and which dependencies create coordination work — hidden ownership is one of the fastest ways for product architecture to decay.
- Roadmap items reference the model: the customer groups and jobs they improve, the KPIs they should move, the capabilities and bricks they change, the teams involved, and the evidence or assumptions behind them. The roadmap becomes an overlay on the architecture, not a disconnected plan.
- Objectives, initiatives, discoveries, and targets live next to the customer, capability, brick, and team model, so questions like "does this initiative still match the objective?" can be asked across artifacts.
- Generated documentation acts as a review surface for the operating model: if a rendered domain page feels disconnected, that is feedback on the source model, and the fix goes back to source.

**What it costs**

- The operating model must be maintained with the same discipline as the rest of the architecture — teams, releases, and roadmap items kept current and connected, not exported once from a planning tool.
- Coordination realities (shared bricks, multi-team capabilities, handoffs) are made explicit rather than smoothed over, which can be uncomfortable to see.

**What we are not doing**

- Prescribing a delivery methodology — the model records how delivery works, not which process to follow.
- Providing a release-planning template or a team-topology tutorial; team shapes depend on the domain.

The test is simple: the model is operable when it helps decide what to prioritize, which team owns a change, and which customer outcome is unsupported. The Article tab walks the ride-sharing example from customer group to release, owning team, roadmap target, and evidence.
