---
timetoread: 2 min
---

Spec-driven product architecture treats the product domain model — not the feature brief — as the specification. The model is structured enough for AI agents to author and validate, and rich enough to connect product vision to implementation reality.

Ordinary spec-driven development starts close to code: write a spec, generate an implementation, check the match. This series moves the specification boundary upward, to the product domain itself. The reason is practical: most products lose coherence *before* code appears — customers, strategy, architecture, roadmap, teams, and evidence live in disconnected artifacts, and AI agents amplify that fragmentation when there is no shared structure.

**What changes**

- Product architecture lives in structured, versioned source models covering eight layers: customers, strategy, delivery, product capabilities, product bricks, teams, roadmap, and evidence.
- AI agents stop "writing strategy prose" and start editing source files inside a domain language — preserving stable IDs, reusing schema patterns, and validating before generated documentation is trusted.
- The practice runs in three modes: **dreaming** (the intended product), **exploring** (what real source, cloud, delivery, and finance data show), and **grounding** (explicitly connecting the two so every concept has evidence or a visible assumption).
- The model stays application-aware: product bricks and capabilities keep enough implementation structure to support real delivery conversations, not just market positioning.

**What it costs**

- The model must be maintained as a first-class artifact — structured JSON, validation, and publishing discipline rather than free-form documents.
- Early models contain bets; grounding makes them visible rather than eliminating them, which means living with explicit, tracked assumptions.

**What we are not doing**

- This is not schema documentation or a tutorial for building a full product domain.
- It is not a decision record arguing you must adopt the approach — it introduces the method and the series.

The Article tab covers the full layer model, the dreaming/exploring/grounding loop, and why product vision alone is not operational. The series continues with [[product-domain-as-source-of-truth]].
