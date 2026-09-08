---
timetoread: "8 min listen"
---

## The Five-Minute Claim

**Ben:** Blunt version first. Onboarding is a form and a script. Why does it deserve its own record in an operating model?

**Ana:** Because onboarding is where the self-service pillar becomes real or fake. [[four-pillars]] promises that new users onboard without manual platform-team work. In most organizations, joining the platform starts with a ticket — and the moment it does, the platform team is the bottleneck it was built to remove. Every new team pays the queue tax before writing a line of code. This record sets the bar for the build: a developer goes from portal form to first deployment in about five minutes, without a ticket and without a platform engineer in the loop.

**Ben:** Five minutes sounds like a demo number. Marketing writes those.

**Ana:** It's not a slogan, it's the acceptance test — and it's literally on the checklist. Open the portal as a test user, pick a template, submit, then confirm the repository, the namespace, RBAC, quotas, identity groups, catalog entry, pipeline, and cluster access, ready to trigger the first deploy. Cheap to run, hard to argue with. And it's re-run whenever the onboarding path changes, because a five-minute path that quietly degrades to forty is a ticket queue with better fonts.

## An API, Not a Portal

**Ben:** The reference build uses Backstage. So isn't this really "configure the Backstage scaffolder well"? Why insist the front door is an API?

**Ana:** Because logic that lives in the portal makes the portal the platform. The record's first commitment is API-first: provisioning logic lives in an onboarding API — `POST /api/v1/teams`, authenticated, requiring a `platform:teams:create` permission, validated against an OpenAPI schema — and Backstage's scaffolder is one client of that API. The anti-pattern has a name: the portal that ate the platform. Embed provisioning in Backstage and it's untestable in isolation, unusable from a CLI or a script, and unswappable when the portal decision changes.

**Ben:** Who actually cares about swappability? Nobody replaces their portal.

**Ana:** People replace their orchestration engine, though — and the record plans for it. The checklist ends with a maturity review: when the custom API becomes hard to maintain, evaluate Argo Workflows, Tekton, Crossplane, Kratix, or a commercial orchestrator, comparing learning curve, flexibility, maintenance, GitOps alignment, complexity, time-to-value, and cost. The reason that review is cheap instead of a rewrite is precisely that the API is the commitment and the engine behind it is an implementation detail. The OpenAPI spec stays the source of truth for every client and for the documentation; swap the engine and not a single caller breaks.

**Ben:** And the schema fussiness — lowercase names, hyphens, 63 characters? That reads like bureaucracy in a contract.

**Ana:** It reads like Kubernetes. Sixty-three characters, lowercase alphanumeric with hyphens — that's a DNS label, because the team name flows into namespace names like `team-{teamname}` and beyond. Validate it at the front door and every downstream resource inherits a legal, consistent name. Skip it and the failure shows up three systems deep, where nobody can read it. The API also tracks who asked, when, and why, and returns provisioning status — accountability is designed into the door, not bolted on.

## One Call, Whole Team

**Ben:** Walk me through what one call actually buys.

**Ana:** Permission check first — nothing touches infrastructure until the requester's authorization is validated. Then the bundle: the namespace with its labels — team, owner, tier, cost center, managed-by — and annotations linking to the catalog entry and the Slack channel; network policies applied automatically; mesh enrollment as a sidecar-injection label where required; three RBAC roles bound to Keycloak groups created in the same workflow; the resource quota for the tier; the source repository; the catalog registration. And the status comes back to the caller.

**Ben:** That's at least four systems — Kubernetes, Keycloak, GitHub, the catalog. Multi-system workflows fail partway. That's not a risk, it's a schedule.

**Ana:** The record agrees, which is why idempotency is non-negotiable: every provisioning step converges on the desired state, so retrying a partially failed request completes it instead of minting duplicates. Retry becomes the recovery procedure. Without that, you get the half-provisioned team — a namespace without a repository, groups without RoleBindings — debris that needs a human archaeologist. And the failure semantics are honest: capacity pre-checked, 409 when the quota won't fit, 503 when the infrastructure is down, GitHub rate limits retried with exponential backoff and jitter, every failed attempt in the audit trail, defined rollback for project-level partial failures.

**Ben:** You keep saying team, but developers don't deploy teams. They deploy services.

**Ana:** Which is why the second unit matters: a project is a complete developer unit, never just a repository. One template execution provisions the repo, the deployment namespaces, the CI/CD pipeline, the catalog entry, and the documentation scaffolding together — from archetype templates, backend service, frontend app, data pipeline, ML model, versioned in Git, with a preview before execution. The anti-pattern is the repo-shaped project: onboarding hands you a repository and calls it a project, and the namespace, pipeline, and catalog entry each need another request. That's not onboarding, that's a to-do list.

## Guardrails in the Box

**Ben:** Quotas. Every team believes it's special. Why tiers instead of asking teams what they need?

**Ana:** Because quota by negotiation kills fairness and capacity planning together. The record ships three tiers — starter, standard, enterprise — each defining CPU and memory requests and maximums, plus caps on volumes, load balancers, and deployments, with a LimitRange supplying defaults per container. New teams default to starter. And it's not a cage: quota upgrades are self-service requests, with an approval workflow where governance requires one. The conversation about resources becomes a workflow step, not a bespoke deal with an engineer.

**Ben:** Identity is the part I'd expect to rot. Groups in Keycloak, RoleBindings in Kubernetes — two systems, one truth, allegedly.

**Ana:** The record treats that as the silent failure mode. Two defenses: creation and reconciliation. The groups — `{team}-admins`, `-developers`, `-viewers` — are created idempotently in the same provisioning workflow, with names that exactly match the RoleBinding subjects, the lead seeded into admins. Then periodic reconciliation between Keycloak and Kubernetes, because anything not reconciled will drift — and identity drift surfaces either as developers locked out or as access that should have died with a departed teammate. There's also a hard boundary: developers can't delete secrets, team admins can't touch `platform-*` namespaces, and nothing escalates outside the team's own namespace.

**Ben:** And after day zero? Teams change, teams dissolve.

**Ana:** Team admins run their own membership — add, remove, assign roles, request quota, create sub-namespaces — while creating teams stays with platform admins, who seed the first team admin. And teams have a lifecycle: active, archived, deleted, with explicit inactivity rules for archival and deletion rules for archived teams. Otherwise you get the immortal namespace — a cluster accreting the namespaces of teams that no longer exist, each one still holding quota and secrets.

## What This Isn't

**Ben:** The operational bill for all this. You've just described a production service the platform team has to run.

**Ana:** Deliberately. Prometheus metrics, structured logs, traces, a full audit trail, load testing, URL-based versioning with a deprecation policy — the onboarding API is operated like anything else in production, because it *is* production: it's the front door. And it's measured as a product: time-to-first-deploy, onboarding ticket count, abandonment rate. Those three numbers tell you whether the door actually opens — that's onboarding as the first product surface of [[platform-as-a-product]].

**Ben:** Close it out. What is this record explicitly not doing?

**Ana:** It's day zero, not the whole platform. What goes inside the project templates is [[starter-kits]]; the pipeline service each project is wired into is [[cicd-as-a-platform-service]]; databases and buckets after the team exists are [[self-service-infrastructure]]; the cost side of those tier and cost-center labels is [[cost-performance-scalability]]. And it's not a tool mandate — Backstage, Keycloak, GitHub, ArgoCD are the reference stack the record is grounded in, honestly named. The commitments hold at the capability level.

**Ben:** So if I remember one sentence?

**Ana:** The portal is a client; the API is the platform's front door — and a new team walks through it in five minutes, or the self-service pillar is a story we tell ourselves.
