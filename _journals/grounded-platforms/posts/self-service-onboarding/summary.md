---
timetoread: "2 min read"
---

When a platform team in my organization builds self-service onboarding, the front door is an **API, not a portal**: a versioned onboarding API owns the provisioning logic, the developer portal is one client of it, and a new team is **one authenticated, idempotent call** that provisions namespace, RBAC, quotas, identity groups, repository, and catalog entry together. The bar the build is held to: **portal form to first deployment in about five minutes**, without a ticket and without a platform engineer in the loop.

**What changes**

* **Provisioning logic moves behind an API.** `POST /api/v1/teams`, authenticated and permission-checked, validated against an OpenAPI/JSON Schema that stays the source of truth for clients and documentation. Backstage's scaffolder calls it — like every other client — so the engine can change later without breaking a single caller.
* **A team is one call, and retries converge.** The workflow provisions the whole bundle — namespace with labels and network policies, three standing roles bound to matching Keycloak groups, tiered quotas with a LimitRange, source repository, catalog entry — with every step idempotent, so a retried half-failure completes instead of duplicating resources.
* **Guardrails ship in the bundle.** Starter/standard/enterprise quota tiers with self-service upgrade requests (approval where governance requires), secret deletion reserved for admins, no escalation outside the team's namespace, `platform-*` namespaces untouchable, and periodic Keycloak↔Kubernetes reconciliation so identity never silently drifts.
* **A project is a complete developer unit.** Repository, namespaces, CI/CD pipeline, catalog entry, and documentation scaffolding provisioned together from versioned archetype templates — never a repo with a to-do list attached.
* **Onboarding is operated and measured.** Honest 409/503/429 failure semantics with backoff and jitter, a full audit trail, Prometheus metrics, and three product metrics on a dashboard: time-to-first-deploy, onboarding ticket count, abandonment rate — plus the end-to-end five-minute walkthrough as the standing acceptance test.

**What it costs**

* The onboarding API is a production service: load-tested, versioned by URL, covered by a deprecation policy, monitored, and on somebody's pager.
* Idempotency, capacity pre-checks, rollback, and reconciliation are real engineering effort — paid up front so that retry, not archaeology, is the recovery procedure.
* Lifecycle discipline has teeth: inactivity archival and deletion rules mean namespaces of dissolved teams actually go away.

**What we are not doing**

* Not the template contents — archetypes and scaffolding depth live in [[starter-kits]]; not the pipeline service itself, which is [[cicd-as-a-platform-service]].
* Not day-2 infrastructure requests — databases and buckets after the team exists are [[self-service-infrastructure]].
* Not a tool mandate — Backstage, Keycloak, GitHub, and ArgoCD are the reference stack; the commitments hold at the capability level, and a future orchestrator may replace the engine but never the API-first and self-service principles.

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the full build, prerequisites through production readiness. Grounded in the* Platform Engineer's Handbook *chapter checklist.*
