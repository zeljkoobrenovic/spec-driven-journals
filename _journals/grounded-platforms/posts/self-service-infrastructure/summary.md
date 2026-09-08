---
timetoread: "2 min read"
---

When a platform team in my organization builds infrastructure self-service, application teams provision by **declaring a claim, not filing a ticket** — a small, validated request (size, version, tier, backups) in their own namespace — while a platform-owned blueprint carries everything beneath it: provider translation, security non-negotiables, environment defaults, required tags, pre-creation governance, and lifecycle automation. The test: a developer goes from claim to connected application without a human in the loop, and I can still answer who owns every resource and why it exists.

**What changes**

* **A blueprint interface, deliberately small.** Developers state intent — in the reference build, a PostgreSQL claim with storage bounded 15–500 GB, versions 13–16, a dev/staging/production tier, and a backup toggle — and the schema's validation enforces the platform's opinion. Endpoint and port are reported back on the claim itself.
* **Standards compiled into the composition.** Tier maps to instance class, backups convert to retention, public access is off and encryption is on for every database; production gets Multi-AZ, deletion protection, and 30-day backups by default, without the developer asking.
* **Governance before creation.** An admission gate validates tier against namespace — production-tier claims only in approved production namespaces — and rejections return errors a developer can act on. Both accepted and rejected claims are tested before the capability ships.
* **Ownership and hygiene automated.** Every resource carries team, cost-center, environment, and managed-by tags; a lifecycle controller requires owner labels, expires development resources at 30 days and staging at 90, cleans up automatically, and reports violations. Production is exempt from auto-expiry by design.
* **The loop closes at the application.** Done means a demo application consuming the generated connection secret behind a readiness probe, a health endpoint reporting database connectivity, and failure modes tested: invalid claims rejected, manual drift reconciled by the control plane.
* **Governed escape hatches.** Needs no blueprint covers get a request path with captured justification — and recurring exceptions become new blueprints (GPU workloads, with cost controls and scheduling restrictions, are the canonical next one).

**What it costs**

* The platform team owns real software — blueprints, compositions, an admission webhook, a lifecycle controller — with versioning, testing in a development cluster before promotion, and practiced debugging of the claim → composite → managed-resource chain.
* Defaults-as-policy means the platform team is accountable for every default; a wrong one ships to every claim.
* Lifecycle enforcement will delete resources teams forgot they wanted — that friction is the policy working, and it must be paired with clear violation reporting.

**What we are not doing**

* Not platform onboarding — namespaces, access, and quotas live in [[self-service-onboarding]].
* Not the cluster-wide policy engine — that is [[policy-as-code]]; the gate here is blueprint-scoped.
* Not the cost discipline itself — the tags built here feed [[cost-performance-scalability]].
* Not mandating Crossplane — the reference stack is the worked example; the commitments bind the capability.

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the full build, prerequisites through the final completion check. Grounded in the* Platform Engineer's Handbook*, Self-Service Infrastructure Management chapter.*
