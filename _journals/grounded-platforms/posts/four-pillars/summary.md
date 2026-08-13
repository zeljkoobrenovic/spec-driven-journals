---
timetoread: "2 min read"
---

Before I call anything in my organization a platform, it has to stand on **four pillars at once**: a curated product with paved paths, software abstractions that genuinely manage complexity, self-service breadth across many application teams, and operation as a reliable foundation. Miss a pillar and what you have is tooling, provisioning, or enablement wearing a platform badge — and the running test is whether the offering manages complexity for application developers or merely moves it somewhere else.

**What changes**

* **Pillar 1 — curated product.** The platform has identified customers, priorities driven by their needs, an explicit opinion about scope, and paved paths covering most recurring needs — with the freedom to leave the path, and new "railway" capabilities built where common gaps justify them. Success is measured by customer outcomes, not platform delivery metrics.
* **Pillar 2 — software-based abstractions.** Real software built by real engineers, not documentation stapled to configuration. APIs simplify underlying systems, but nothing is hidden unless the abstraction genuinely improves productivity; thick clients come with a lifecycle plan, and metadata — ownership, usage, access, cost, dependencies, migration impact — is collected automatically.
* **Pillar 3 — a broad developer base.** Many teams and skill levels served through self-service onboarding, multiple interfaces (UI, CLI, API, SDK, config-as-code), user-facing observability, guardrails with safe defaults, and deliberate multitenancy — so each new adopting team costs the platform team less than the last.
* **Pillar 4 — operated as a foundation.** The platform team owns the operational experience of the complete offering, down through cloud, OSS, and vendor layers: incident ownership, SLOs, capacity, runbooks, on-call — and support treated as product feedback.
* **A standing truth check.** Every offering we call a platform carries a current four-pillar score (0–2 per pillar): 7–8 supports the platform claim; 0–3 means the honest name is tooling or provisioning — and it gets renamed, refunded as what it is, or given a plan to earn the missing pillars.

**What it costs**

* Honest naming has consequences: things we have been calling platforms may turn out to be tooling or enablement, which are funded and staffed differently.
* Pillar 4 is expensive — owning the operational experience of dependencies you chose, not just the software you wrote.
* The scorecard recurs; it is a periodic truth serum, not a one-time gate.

**What we are not doing**

* Not the case for platform engineering itself — that is [[what-is-platform-engineering]].
* Not the full product or operating mechanics — pillar 1 expands in [[platform-as-a-product]], pillar 4 in [[operating-platforms]], and staffing lives in [[building-platform-teams]].
* Not mandating an internal developer portal — an IDP is built only if it solves a validated problem.

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries all four pillars, the supporting quality dimensions, and the scorecard. Grounded in Fournier and Nowland's* Platform Engineering *(O'Reilly, 2024).*
