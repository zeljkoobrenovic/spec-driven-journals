---
timetoread: 2 min
---

Spec-Driven Product Architecture starts with customer progress and keeps it connected to architecture decisions: customer groups and jobs to be done come first, then KPIs, strategy horizons, capabilities, product bricks, delivery, and team ownership. Architecture work that starts at "which systems do we need?" begins too late — by then the customer model has usually been flattened into feature requests, and engineers reverse-engineer the product shape from tickets and stakeholder memory.

**What changes**

- Customer groups come before product bricks. Riders, drivers, fleet operators, and marketplace operators pull the system in different directions — real-time confidence, compliance, high-frequency ergonomics, exception handling — and that separation is one of the first ways the architecture discovers its shape.
- Jobs to be done describe progress, not feature clicks. "Find a trustworthy stay within budget" instead of "use search." Agents that model jobs as feature usage produce feature inventories; agents that model jobs as progress can reason about outcomes, frictions, and missing architecture.
- KPI pyramids and north-star metrics make value operational and the architecture testable. Every KPI leaf names an observable signal — request-to-match time, pickup success rate — not a vague branch called "Experience."
- Strategy horizons (commonly 1, 3, and 5 years) turn product vision into a planning constraint: each names its focus, dominant theme, target customer and business KPIs, and milestones.
- A nine-step chain — customer group, job, outcome, KPI, horizon, capability, product brick, release, owning team — stays inspectable end to end. The ride-sharing running example traces it from "riders need reliable on-demand travel" down to the marketplace matching team and its evidence.

**What it costs**

- The chain is a maintained artifact. It does not need to be perfect in the first draft, but it must exist — generic customer groups, slogan horizons, and unmeasurable KPIs quietly break it, and AI agents cannot maintain coherence the model does not express.
- Language discipline: **discovery** and **evaluation** are reserved for how customers become aware and decide before commitment, never reused as labels for in-product search or task steps.

**What we are not doing**

- This is not a full customer modeling tutorial or domain-specific customer research guidance.
- It does not calibrate KPI targets — it argues for concrete, measurable leaves, not particular numbers.

The Article tab walks each layer with screenshots and the full ride-sharing trace; [[product-bricks-and-capabilities]] continues where this chain hands customer value over to buildable structure.
