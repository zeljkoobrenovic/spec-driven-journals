---
status: accepted
revised: 2026-08-20
---

# Spec: Self-Service Platform Onboarding

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the shape I hold a platform team to when they build self-service
onboarding — the capability that takes a new team or project from a portal
form to a first deployment without a ticket and without a platform engineer
in the loop. The post turns the Self-Service Platform Onboarding chapter of
the *Platform Engineer's Handbook* into a reference-implementation record:
the front door is a versioned, schema-validated onboarding API (the portal is
one client of it, never the home of the logic); a new team is one
authenticated call that provisions the whole bundle — namespace, RBAC,
quotas, identity groups, source repository, catalog entry — with every step
idempotent so retried half-failures converge instead of duplicating; a
project is a complete developer unit, not a repository; and failure
semantics, auditability, and onboarding metrics are part of the door, not an
afterthought. The load-bearing bar: portal form to first deploy in about
five minutes.

## Audience

Platform teams in my organization building team and project onboarding (so
they know the end-to-end shape the build is held to); platform leads and
architects deciding where provisioning logic lives; peer executives asking
why onboarding tickets still exist. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight names the API-first front door,
      the one-call idempotent provisioning bundle, guardrails shipped in the
      bundle, project as a complete developer unit, and the five-minute
      portal-to-first-deploy bar.
- [x] **API-first design survives** — `POST /api/v1/teams`; authentication
      plus the `platform:teams:create` permission; OpenAPI/JSON Schema
      validation; required team name, display name, and lead email;
      lowercase-alphanumeric-with-hyphens names capped at 63 characters;
      resource tier defaulting to starter; requester, timestamp, and purpose
      tracked; provisioning status returned; the OpenAPI spec as the source
      of truth for clients and documentation.
- [x] **The provisioning bundle survives** — permission check before any
      infrastructure is touched, then namespace, RBAC roles, resource quota,
      source repository, Keycloak groups, and Backstage catalog registration
      in one workflow; every step idempotent; retrying a partial failure
      does not duplicate resources.
- [x] **Namespace and RBAC conventions survive** — `team-{teamname}` and
      `team-{teamname}-{environment}` naming; labels for team, owner, tier,
      cost center, managed-by; Backstage and Slack annotations; Istio
      sidecar injection where mesh enrollment is required; automatic network
      policies; team-admin/team-developer/team-viewer roles; secret deletion
      reserved for admin roles; RoleBindings bound to
      `{team}-admins`/`-developers`/`-viewers` OIDC groups; no escalation
      outside the team namespace; `platform-*` namespaces untouchable.
- [x] **Quota tiers survive** — starter/standard/enterprise tiers with CPU
      and memory requests and maximums; PVC, load-balancer, and deployment
      limits; a LimitRange with defaults and per-container maximums; quota
      alerts wired to the observability platform; self-service quota upgrade
      requests with an approval workflow where governance requires.
- [x] **Identity integration survives** — Keycloak Admin REST API; team
      groups created idempotently at provisioning; the lead in the admins
      group; group names matching Kubernetes RoleBinding subjects;
      membership in JWT claims where required; periodic Keycloak↔Kubernetes
      reconciliation.
- [x] **Lifecycle and the project unit survive** — platform admins create
      teams and seed the first team admin; team admins manage members,
      roles, quota requests, and sub-namespaces; active/archived/deleted
      lifecycle states with inactivity and deletion rules; a project
      provisions repository, namespaces, CI/CD pipeline, catalog entry, and
      documentation scaffolding together, from archetype templates versioned
      in Git with metadata and a pre-execution preview; scaffolder
      validations (name uniqueness, team membership, quota availability,
      cost center for production, GPU approval for ML) and completion links.
- [x] **Failure, observability, and readiness survive** — capacity
      pre-checks; 409/503/429 semantics; exponential backoff with jitter;
      audit of successes, failures, and retries with requester, timestamps,
      and purpose; duplicate prevention and project-level rollback;
      Prometheus metrics, structured logs, and traces;
      time-to-first-deploy, onboarding ticket count, and abandonment
      tracked; the end-to-end five-minute walkthrough; API versioning and
      deprecation policy; load, rate-limit, quota-exhaustion,
      partial-failure, and escalation testing; the future maturity review
      (Argo Workflows, Tekton, Crossplane, Kratix, commercial orchestrators)
      that preserves API-first and self-service whatever engine wins.
- [x] **Credit is explicit** — References name the *Platform Engineer's
      Handbook* and its Self-Service Platform Onboarding chapter checklist.

## Non-goals

- Not [[starter-kits]] — the contents and archetypes of project templates
  live there; here templates appear only as the complete unit the
  scaffolder provisions.
- Not [[cicd-as-a-platform-service]] — the pipeline service itself lives
  there; here a CI/CD pipeline is one resource in the project bundle.
- Not [[self-service-infrastructure]] — day-2 self-service infrastructure
  (databases, buckets, queues) lives there; this record is team and project
  day zero.
- Not [[cost-performance-scalability]] — cost engineering and optimization
  live there; the quota tiers and cost-center labels here are onboarding
  guardrails, not the cost model.
- Not [[four-pillars]] — pillar 3 states the self-service bar; this record
  is its reference build, not a restatement of the argument.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-08-20** — Grounded in the Self-Service Platform Onboarding chapter
  checklist of the *Platform Engineer's Handbook* — the build-it-end-to-end
  companion whose reference stack (Backstage, Keycloak, GitHub, Kubernetes,
  ArgoCD, Istio) this record names honestly — read through a
  practitioner-executive lens, as with every record in this journal.
- **2026-08-20** — Framed as an API-first capability rather than a portal
  feature: the chapter's distinctive claim is that provisioning logic lives
  behind a versioned API with the portal as one client, so the record
  commits at the capability level ("a team is one idempotent call") and
  treats the named tools as the worked example, not the mandate.

## Sources

- **Internal**
  - `sources/checklists/plaform-engineer-handbook/Checklist_ PEH _ 07 _ Self-Service Platform Onboarding.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`). (The handbook's checklist series skips number 06;
    this is the sixth record of the Reference Implementation section.)
- **External**
  - *Platform Engineer's Handbook* — the Self-Service Platform Onboarding
    chapter checklist.

## Changelog

- **2026-08-20** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
- **2026-08-20** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-20** — Initial spec, article, checklist, summary, and dialog written; spec and post agree. Status `accepted`. *(Željko, AI-mediated session)*
