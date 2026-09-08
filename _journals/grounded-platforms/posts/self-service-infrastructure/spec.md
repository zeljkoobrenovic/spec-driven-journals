---
status: accepted
revised: 2026-08-20
---

# Spec: Self-Service Infrastructure Management

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the shape I hold a platform team to when they build self-service
infrastructure: application teams provision real infrastructure by declaring
a small, validated claim in their own namespace — and everything else (the
provider translation, the security non-negotiables, the environment defaults,
the tags, the governance check, the lifecycle limits, the credential
delivery) is carried by a platform-owned blueprint, not by tickets or by
hand. The post turns the Self-Service Infrastructure Management chapter
checklist of the *Platform Engineer's Handbook* — the Crossplane PostgreSQL
build — into a reference-implementation record: the worked example is
Crossplane, an XRD/claim interface, an AWS RDS composition, an admission
webhook, and a lifecycle controller; the commitments are stated at the level
of the capability. The load-bearing idea: **the blueprint is the product** —
a few parameters for the developer, the organization's standards compiled
into everything beneath them, and a control plane that keeps declared and
actual state converged.

## Audience

Platform leads and teams in my organization building infrastructure
self-service (so they know the end-to-end shape the build is held to);
infrastructure and security leaders assessing whether "self-service" is real
or a ticket queue wearing an API; peer executives funding the work.
First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the claim-not-ticket
      model: developers declare a small claim; the blueprint carries the
      standards; governance runs before creation; lifecycle and drift are
      automated; escape hatches are governed.
- [x] **The blueprint interface survives** — XRD + claim with a deliberately
      small parameter surface: storage (15–500 GB bounds), supported
      PostgreSQL versions (13–16), dev/staging/production tiers, backup
      toggle, and connection-status fields (endpoint, port) — defaults and
      validation enforcing platform standards.
- [x] **The composition and environment defaults survive** — tier-to-instance
      mapping (db.t3.micro / db.t3.small / db.r6g.large), storage and version
      mapping, backup-to-retention conversion, public access disabled,
      encryption enabled, network/subnet references, connection-secret
      generation; per-environment defaults (minimal dev retention, 7-day
      staging backups + performance insights, 30-day production backups +
      Multi-AZ + deletion protection) selected by composition labels.
- [x] **Tagging survives** — team, cost-center, environment, and managed-by
      on every resource; every resource identifies its owner and purpose and
      supports cost allocation.
- [x] **Governance survives** — validating admission webhook checking tier
      and namespace (production tier only in approved production namespaces),
      actionable rejection messages, tested with both accepted and rejected
      claims.
- [x] **Lifecycle automation survives** — owner-label requirement, 30-day
      development and 90-day staging age limits, no automatic production
      limit, automatic cleanup of eligible dev resources, detection and
      reporting of policy violations.
- [x] **End-to-end proof survives** — the demo claim (20 GB, PostgreSQL 15,
      development tier, backups, generated connection secret), the
      application consuming the secret (host/port/user/password/db name,
      readiness probe), the workflow test (claim Ready, secret created,
      health endpoint reports connectivity), and failure/drift validation
      (invalid storage, unsupported version, wrong namespace, manual drift
      reconciled, claim→composite→managed-resource debugging, dev-cluster
      validation before promotion).
- [x] **Escape hatches survive** — a governed process for needs no blueprint
      covers, with business justification, plus specialized blueprints (GPU),
      cost controls, and scheduling restrictions.
- [x] **Credit is explicit** — References name the *Platform Engineer's
      Handbook* and the Self-Service Infrastructure Management chapter.

## Non-goals

- Not [[self-service-onboarding]] — that record gets teams *onto* the
  platform (namespaces, access, quotas); this one governs what they can
  provision once they are on it.
- Not [[policy-as-code]] — the cluster-wide policy engine lives there; the
  admission webhook here is blueprint-scoped tier/namespace validation.
- Not [[cost-performance-scalability]] — the tagging here feeds cost
  allocation; the cost, performance, and scaling discipline itself lives
  there.
- Not [[platform-creation]] — the cluster, GitOps, and mesh substrate this
  capability runs on is built there.
- Not [[starter-kits]] — the application scaffolding that consumes these
  claims from day one is its own record.

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

- **2026-08-20** — Grounded in the Self-Service Infrastructure Management
  chapter checklist of the *Platform Engineer's Handbook* — the
  reference-implementation companion this journal's Reference Implementation
  section is built from — read through a practitioner-executive lens, as
  with every record in this journal.
- **2026-08-20** — Commitments stated at the capability level with the PEH
  stack (Crossplane, XRD/claims, AWS RDS composition, admission webhook,
  lifecycle controller) named honestly as the reference stack; a
  tool-mandate framing ("use Crossplane") was rejected — the record binds
  the blueprint model, not the vendor.

## Sources

- **Internal**
  - `sources/checklists/plaform-engineer-handbook/Checklist_ PEH _ 09 _ Self-Service Infrastructure Management.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the final completion check.
- **External**
  - *Platform Engineer's Handbook* — the Self-Service Infrastructure
    Management chapter checklist.

## Changelog

- **2026-08-20** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
- **2026-08-20** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-20** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
