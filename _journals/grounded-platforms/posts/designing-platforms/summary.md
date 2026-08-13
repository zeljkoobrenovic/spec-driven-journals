---
timetoread: "2 min read"
---

I design platforms as **fruit salads, not fruit baskets**: the value must come from integration, defaults, automation, and reduced toil — not from cataloging tools users could have installed themselves. Every abstraction must speak a higher-level vocabulary without becoming an **illusion** that hides essential complexity, because an abstraction that hides essential complexity has not simplified anything — it has just moved the bill.

**What changes**

* The **7 Cs** — cohesion, closure, completeness, consistency, commensurate value, connectedness, captivity — are used as trade-off dimensions, never as a maximization recipe. Each platform gets a written statement of which Cs it optimizes and what it consciously traded away; an undocumented trade-off gets relitigated in every design review.
* Every **horizontal capability earns its existence** through a concrete answer: does it increase reuse, support necessary governance, or improve operations across components? Architectural preference does not qualify — an unjustified shared layer is pure coupling, and it goes.
* The platform **floats on its evolving base**: at least once a year we list what the base platform has commoditized, retire our overlapping functionality with a migration path, and reinvest the freed capacity. A roadmap that only ever adds is a platform that is sinking.
* **Wrappers become a last resort.** Before any new interface over an existing platform, we exhaust configuration, interception hooks, and tracking — because the grim wrapper lags the platform underneath, severs users from community knowledge, and adds an operational burden while claiming to reduce cognitive load.
* **Failure is designed for from day one**: platform errors trace to their lower-level origin, failure modes are documented as part of the abstraction, specialists can open the hood, and we keep people who understand the layers underneath.

**What it costs**

* Integration work is invisible in architecture diagrams and expensive in practice — we measure platform features by user value delivered, never by how hard they were to build.
* Retiring commoditized functionality means abandoning things we are proud of, and keeping components modular enough to be replaceable is itself a standing design requirement.
* Keeping failures, latency, and cost visible makes interfaces look less "clean" than a sealed facade — that honesty is the point.

**What we are not doing**

* Not re-arguing what a platform is or why harmonization beats standardization — that is [[understanding-platforms]].
* Not build/buy, sizing, or delivery mechanics — [[implementing-platforms]] owns those; this record is the design bar they must meet. Team shape and engagement models stay in [[organizing-for-platforms]].
* Not a technology catalog — no positions on specific IDPs, clouds, or orchestrators.

*The Article tab carries the rationale and anti-patterns; the Checklist tab holds the 7 Cs assessment, the fruit-salad test, the wrapper interrogation, and the go/no-go review.*
