---
timetoread: "2 min read"
---

I introduce platform engineering when coordination costs demand it, not before. While a handful of engineers can cooperate informally, platform work stays a shared responsibility with simple, off-the-shelf tooling; when shared systems start failing because "everyone owns it" has become "nobody owns it", I make ownership explicit and form a team — and that team earns trust by fixing today's most painful problems, not by designing an architecture for a scale we do not have.

**What changes**

* Structure follows **coordination cost, not the calendar**. Early stage means source control, fast feedback, automated deployment, off-the-shelf platforms, no Kubernetes before we need it, and outsourcing non-differentiators. Growth means a standardized paved road — local environments, tested merges, ephemeral environments, feature flags, observability, infrastructure automation — plus a lightweight RFC/ADR decision process.
* Forming a platform team requires **observable friction signals**: failures with unclear ownership, recurring tooling friction, capabilities reinvented team by team. The decision becomes evidence-based rather than fashionable — someone can point at the friction we are buying our way out of.
* Every candidate capability passes the **centralization test**: one implementation must serve many teams without extensive per-team customization, and the leverage must substantially exceed the cost of a new coordination point. If every consumer needs heavy custom logic, it stays decentralized.
* The first team **starts with problems, not architecture** — explicit ownership boundaries, platform-consuming engineers treated as customers, the messiest shared code and workflows fixed first, and trust built before any major redesign.
* We **hire for the organization we have**: first-principles reasoning at our scale, not people who can only reproduce BigCo platform machinery. Product managers arrive only after engineers have built direct customer relationships; project managers later still.
* Transforming a traditional infrastructure organization is treated as a **culture transformation, not a technology migration** — changed incentives, real product thinking, fixed support, the platform team owning migration pain, and more engineering time spent with customers.

**What it costs**

* Resisting an early platform team means tolerating some shared-responsibility messiness — and honestly tracking whether support and technical-debt work is crowding out feature work.
* Fixing today's pain first delays the satisfying big redesign; credibility is earned before it is spent on architectural change.
* Owning migrations and customer support is real, ongoing platform-team work, not something exported to application teams.

**What we are not doing**

* Not the full staffing and team-shaping model — that is [[building-platform-teams]]; this record covers only the formation-time hiring cautions.
* Not defining what a real platform must be ([[four-pillars]]) or the full product operating mode ([[platform-as-a-product]]) — this record establishes only when to start and the customer framing at formation.
* Not a technology-selection guide — specific tooling choices stay with the teams that live with them.

*The Article tab carries the rationale and anti-patterns; the Checklist tab holds the runnable stage-by-stage program, the team-formation test, and the transformation plan.*
