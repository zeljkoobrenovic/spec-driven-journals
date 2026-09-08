---
status: accepted
revised: 2026-08-20
---

# Spec: Starter Kit Templates

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the bar I hold a platform team to when it builds starter kit templates
— the paved-path scaffolding that turns "we need a new service" into a
working, deployed, cataloged service from a single portal action. The record
turns the Starter Kit Template chapter checklist of the *Platform Engineer's
Handbook* into a durable capability commitment: a template repository with a
complete skeleton (Dockerfile, CI/CD workflow, manifest, README, source
files), template metadata that records name and version for upgrade tracking,
a portal template that scaffolds repository, infrastructure claim, namespace,
and catalog entry in one run, template testing that generates and fully
exercises a test project before anything is published, controlled publishing
into the portal catalog, and an end-to-end proof — create a service, validate
it locally, deploy it, push a change, watch the pipeline go green. The
load-bearing idea: **a starter kit is a product that is tested like software
and proven end to end — an untested template makes every consuming team the
test.**

## Audience

Platform leads and engineers in my organization building or maintaining
starter kits (so they know the shape of the build I hold them to);
application-team leads deciding whether to trust the paved path for their
next service; peer executives assessing whether "self-service scaffolding"
claims are real. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the capability: one portal
      action produces a working repository, pipeline, infrastructure claim,
      namespace, and catalog entry; templates are versioned products tested
      like software and proven end to end before anyone consumes them.
- [x] **Repository setup and template files survive** — starter-kits
      repository structure, template directory with skeleton, all required
      starter files (Dockerfile, CI/CD workflow, package manifest, README,
      source/configuration files), `platformMetadata` in the manifest, and
      template name + version recorded for upgrade tracking.
- [x] **The portal template survives** — template definition with service
      information, team/owner, database options, service port, and repository
      location parameters; fetch steps, conditional database configuration,
      infrastructure-claim generation, repository publishing, namespace
      creation, catalog registration, and useful output links / next steps.
- [x] **Template testing survives** — structure validation, required metadata
      and skeleton files verified, a test project generated and exercised:
      dependency install, build, unit tests, linting, application start,
      `/health` responding — with all failures fixed before publishing.
- [x] **Controlled publishing survives** — portal URL/token and repository
      variables configured, publishing script run, template validation
      succeeds, template registered in the catalog and visible in the portal.
- [x] **The end-to-end proof survives** — create a service through the
      portal; confirm repository, namespace, and catalog entry; validate the
      generated service locally (clone, install, build, test, lint, container
      build, infrastructure claim, catalog metadata, local dev environment);
      deploy to the platform cluster, push a change, observe the pipeline
      complete, and confirm the full workflow from template creation through
      deployment.
- [x] **Tools stay the worked example** — Backstage, GitHub, Crossplane,
      Kubernetes are named as the reference stack, but every commitment is
      stated at capability level.
- [x] **Credit is explicit** — References name the *Platform Engineer's
      Handbook* and its Starter Kit Template chapter checklist.

## Non-goals

- Not [[self-service-onboarding]] — that record gets a team onto the platform
  (tenancy, access, quotas); this one gets a new service born on the paved
  path once the team is already on.
- Not [[cicd-as-a-platform-service]] — the pipeline capability itself lives
  there; here the starter kit only wires the workflow in and the final proof
  observes it run.
- Not [[self-service-infrastructure]] — the claim-based infrastructure model
  is defined there; the template only generates a valid claim.
- Not [[platform-as-a-product]] — the general product operating mechanics;
  this record applies them to one artifact class, the template.
- Not a frontend/library/data-pipeline template catalog — the reference build
  walks one backend-service template end to end; the shape generalizes, the
  record does not enumerate every template type.

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

- **2026-08-20** — Grounded in the Starter Kit Template chapter checklist of
  the *Platform Engineer's Handbook* — read through a practitioner-executive
  lens, as with every record in this journal. Part of the Reference
  Implementation section: the how-it-concretely-looks companion to the
  Platform Engineering records.
- **2026-08-20** — Framed around the test-and-prove discipline rather than
  the scaffolding mechanics: the chapter's distinctive contribution is not
  that templates exist (every portal demo has one) but that a template is
  versioned, tested by generating and fully exercising a project before
  publishing, and proven from portal click through deployed pipeline run. A
  pure "how to write template.yaml" framing was rejected as tool
  documentation, not an operating record.

## Sources

- **Internal**
  - `sources/checklists/plaform-engineer-handbook/Checklist_ PEH _ 10 _ Starter Kit Template.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`). A `.docx` copy of the same checklist sits alongside it.
- **External**
  - *Platform Engineer's Handbook* — the Starter Kit Template chapter and its
    checklist; the reference build uses Backstage software templates, GitHub,
    Crossplane claims, and Kubernetes namespaces.

## Changelog

- **2026-08-20** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
- **2026-08-20** — Comics modality added (comics.md, Comic tab, shared
  VERA/KAI cast); 3 inline figures generated in the article. *(Željko,
  AI-mediated session)*
- **2026-08-20** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
