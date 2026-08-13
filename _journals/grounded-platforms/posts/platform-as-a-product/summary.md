---
timetoread: "2 min read"
---

An internal platform is a product with customers, and I hold platform teams to a product bar, not an infrastructure bar. Mandatory usage is not success — a captive audience is a risk, not a moat — and a platform that customers would not choose if they had a choice is not done; it is failing slowly.

**What changes**

* **Internal engineers are treated as customers, not stakeholders.** Platform teams identify their customer segments, observe real workflows and workarounds rather than relying on what customers say they want, and share customer engagement between PMs and engineers — including engineers doing customer support.
* **Product discipline replaces the feature shop.** The customer's underlying problem is separated from their proposed solution; common needs across teams become reusable, self-service capabilities instead of a backlog of bespoke requests serving whoever asks loudest.
* **Investment requires validated internal product–market fit** — named customer segments and alpha customers committing real time, effort, or budget, not hypothetical enthusiasm — with buy-versus-build considered and migration cost included in the decision to build at all.
* **Adoption is planned like a product launch.** Migration cost, hidden dependencies, and a retirement plan for the old generation are estimated up front; launches respect the customer's finite change budget; and the platform is marketed internally so teams know an offering exists before building their own.
* **Impact metrics steer, activity metrics do not.** Teams write down the hypothesis linking platform work to customer outcomes, watch guardrail and product-health metrics alongside it, and change the strategy — not the metric — when evidence disagrees. Reliability counts as product experience: no new features on an unreliable foundation.

**What it costs**

* Customer research, support rotations, validation gates, and adoption planning are real engineering and product time spent before and around building — slower than just shipping what was asked.
* Refusing bespoke requests and loudest-team design creates short-term friction with exactly the teams that shout loudest.
* Honest impact measurement means accepting evidence that a beloved initiative is not working — and changing course instead of changing the metric.

**What we are not doing**

* Not the whole pillar model — that is [[four-pillars]]; this record unpacks the "curated product" pillar into a full operating discipline.
* Not the operational machinery — on-call, support, and operational feedback live in [[operating-platforms]]; reliability appears here only as part of the product experience. The planning mechanics behind the roadmap live in [[planning-and-delivery]].
* Not a tooling or vendor recommendation — this is the product discipline, not which developer portal to buy.

*The Article tab carries the rationale and anti-patterns; the Checklist tab holds the culture practices, validation gates, metrics discipline, and the final pre-investment review.*
