---
timetoread: 2 min
---

Product capabilities describe the outcomes a product must deliver; product bricks describe the implementation-facing units that make those outcomes buildable, ownable, and traceable. Together they form the most important bridge in spec-driven product architecture — without it, the model collapses into either product strategy prose or a technology inventory.

**What changes**

- Outcomes and implementation are modeled as distinct, connected layers: capabilities keep the language of value ("book and complete a reliable trip"), while bricks name the implementation-facing units that make the outcome real.
- Every brick must be buildable, ownable, traceable, coherent, and durable — a team can implement it, a primary owner is named, and its ID survives rewording and roadmap cycles.
- Bricks follow a meaningful three-level structure (root group → subgroup → brick) and become concrete through layered modules (UI, interfaces, bus, stateless services, services, integrations) — enough architectural shape for delivery conversations, well short of full solution design.
- Dependencies are first-class: brick-to-brick links, module calls, and data-asset producer/consumer relationships reveal whether a capability is plausible or architecturally under-specified before delivery surprises arrive.
- For AI agents authoring the model, bricks are the application-awareness mechanism: they force the model to say which implementation structures must exist for the strategy to be real.

**What it costs**

- Maintaining two connected vocabularies takes discipline — capabilities must stay in outcome language while bricks stay implementation-facing, and the trace between them must be kept current.
- Honest dependency modeling surfaces uncomfortable findings (missing bricks, disconnected owners, unclear coordination) that teams must then resolve rather than ignore.
- Agents drift into feature lists, technology catalogs, or generic platform filler unless every brick is justified by customer value, capability needs, or operating constraints.

**What we are not doing**

- No full product-brick JSON schema reference and no exhaustive module-type documentation.
- No deep system design for any one domain — the brick model gives architectural shape, not a solution blueprint.

The Article tab walks the ride-sharing running example from "book and complete a reliable trip" down to bricks, modules, dependencies, ownership, and evidence. [[customer-value-to-architecture]] covers the customer-value input upstream; [[delivery-teams-and-roadmaps]] takes the next step into delivery, ownership, and sequencing.
