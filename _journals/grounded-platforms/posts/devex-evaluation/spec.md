---
status: accepted
revised: 2026-08-20
---

# Spec: Developer Experience Evaluation

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the shape of the developer-experience evaluation I hold a platform team
to once their platform can run applications: DevEx is **measured, not
assumed**. The post turns the DevEx-evaluation chapter of the *Platform
Engineer's Handbook* into a reference-implementation record: deploy a
realistic demo application through the entire journey — code change to
running, monitored, HTTPS-served production application — to set a baseline
(workflow friction, DORA metrics, efficiency/satisfaction/impact), verify
each capability the journey depends on (pipeline, self-service, production
defaults, environments, observability, access, errors, recovery, templates),
put a developer who has never seen the platform in front of it, then
re-measure after every improvement round and attack the highest remaining
friction. The load-bearing idea: the final examiner is a fresh developer
shipping to production from minimal inputs — everything else is the platform
team grading its own homework.

## Audience

Platform leads and teams in my organization (so they know the evaluation
their platform is held to before and after every improvement round);
infrastructure and DevTools leaders judging whether a platform is ready to
onboard teams; peer executives who want DevEx claims backed by measurement.
First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states that DevEx is measured,
      not assumed: a realistic application through the full journey,
      baseline → improve → re-measure, with a developer who has never seen
      the platform as the final examiner.
- [x] **The measurement loop survives** — baseline via a realistic demo app
      and the complete developer journey; workflow friction recorded;
      efficiency, satisfaction, and impact tracked; the four DORA metrics
      (deployment frequency, lead time, MTTR, change failure rate)
      captured; after improvements the same deployment is repeated, results
      compared with the baseline, all measures re-taken, the highest-friction
      steps prioritized, and the evaluation repeated as the platform matures
      (source §1, §16).
- [x] **The pipeline journey survives** — push triggers the workflow;
      checkout, tests, lint/quality checks, build, container image, registry
      push, deployment update all automatic; GitOps keeps desired and actual
      state aligned; failed deployments roll back; every action leaves an
      audit trail (§2).
- [x] **Genuine self-service survives** — no tickets, no unnecessary
      approvals or manual infrastructure work; at least one simple touchpoint
      (CLI/UI/API); pre-configured templates; auto-provisioning from
      application requirements; config validation before deployment;
      generated manifests; policies applied automatically; immediate access
      to endpoints and monitoring (§3) — and the frictionless-deploy test:
      minimal inputs (application name, Git repository) with namespace,
      replicas, autoscaling, ingress, HTTPS, monitoring, alerts, backups,
      scanning, network policies, and secret rotation configured
      automatically (§6).
- [x] **Production-ready defaults survive** — container readiness
      (reproducible/multi-stage builds, non-root, minimal runtime files,
      health checks, requests/limits, liveness/readiness probes, no
      privilege escalation, read-only root FS, dropped capabilities) (§4);
      security built into the deployment (CVE scanning, committed-secret
      detection, RBAC validation, automatic policies, secure workload
      defaults, network policies, exposure detection, HTTPS remediation,
      checks before production) (§5); production-ready defaults enabled
      rather than hidden as optional features (§13).
- [x] **Environments survive** — preview environments with auto-generated
      PR URLs; full-stack local development with debugging; local/preview
      parity (env-var names, service discovery, sample data); documented
      when and how to use each; local setup a first-class capability;
      preview TTLs to control cost (§7).
- [x] **Observability by default survives** — metrics, logs, and traces via
      vendor-neutral instrumentation (OpenTelemetry); automatic collection;
      trace and metric export verified visible; HTTP and database
      telemetry; custom spans/metrics; span attributes and recorded
      exceptions; cross-service propagation (§8); structured logs with
      timestamps, levels, meaningful messages, injected trace/span IDs, and
      verified log-to-trace navigation (§9).
- [x] **Access and HTTPS survive** — declarative public access hiding
      ingress, gateway, and routing complexity; auto-provisioned ingress,
      DNS, and routing rules; team-chosen subdomains (§10); HTTPS as the
      path of least resistance: automated certificate provisioning,
      management (e.g. cert-manager), ACME integration, renewal, secure
      storage, expiry monitoring, never a developer-facing incident (§11).
- [x] **The failure experience survives** — realistic failures triggered;
      errors understandable without deep Kubernetes knowledge; infrastructure
      errors translated with remediation guidance at the point of failure —
      error messages as documentation at the point of need (§12); rollback
      self-service, discoverable, tested, and ticket-free; autoscaling
      verified under significant traffic (§13).
- [x] **Paved paths are validated** — service templates with pre-configured
      CI/CD, health checks, metrics endpoints, and security scanning;
      organizational best practices encoded; no manual recreation of common
      patterns; templates used to accelerate new-developer onboarding (§14).
- [x] **The fresh-eyes test survives** — a developer unfamiliar with the
      platform completes the workflow without handholding; delight,
      confusion, and friction recorded; steps requiring infrastructure
      knowledge, another team, or manual configuration identified; secure
      defaults, immediate observability value, and safe recovery from
      mistakes verified (§15).
- [x] **The final bar survives** — the source's closing success criteria
      (code to production with minimal manual effort, velocity balanced with
      governance, security built in, observability by default, automatic
      HTTPS and safe networking, supported local and preview environments,
      self-served failure recovery, complexity behind declarative
      interfaces, DevEx measured not assumed, continuously falling cognitive
      load) are reproduced in the checklist.
- [x] **Tools are the worked example, not the mandate** — the reference
      stack (CircleCI, Flux, Backstage, OpenTelemetry, Prometheus/Grafana,
      cert-manager, Istio) is named honestly, but every commitment is stated
      at the capability level.
- [x] **Credit is explicit** — References name the *Platform Engineer's
      Handbook* and its Developer Experience Evaluation chapter checklist.

## Non-goals

- Not [[cicd-as-a-platform-service]] — that record builds the pipeline as a
  platform service; this one evaluates the developer's experience of the
  journey the pipeline enables, end to end.
- Not [[observability-implementation]] — the platform observability stack is
  built there; here observability appears only as what every deployed
  application must get by default, and as one lens of the evaluation.
- Not [[platform-security]] — end-to-end platform hardening lives there;
  here security appears as the checks a developer's deployment passes
  through without noticing.
- Not [[starter-kits]] — template mechanics and contents live there; here
  templates are validated from the developer's seat as paved paths that
  actually pave.
- Not [[self-service-onboarding]] — the day-zero onboarding flow is its own
  record; the fresh-eyes evaluation here tests the workflow, not the
  sign-up.
- Not [[platform-success]] — organization-level success measures live
  there; this record is the hands-on evaluation loop for one platform
  build.

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

- **2026-08-20** — Grounded in the Developer Experience Evaluation chapter
  checklist of the *Platform Engineer's Handbook* — the build-it-end-to-end
  companion whose reference stack (Pulumi, CircleCI, Flux, Istio, Backstage,
  OpenTelemetry, cert-manager) this journal's Reference Implementation
  section follows — read through a practitioner-executive lens, as with
  every record in this journal.
- **2026-08-20** — Framed as an evaluation loop rather than a feature list:
  the chapter's distinctive move is baseline → improve → re-measure with a
  fresh developer as the final examiner, so the record commits to the loop
  and to capability-level outcomes; the named tools stay a worked example,
  never a mandate. A pure capability-inventory framing was rejected — it
  would duplicate the sibling build records and lose the measurement
  discipline that makes this chapter distinct.

## Sources

- **Internal**
  - `sources/checklists/plaform-engineer-handbook/Checklist_ PEH _ 05 _ Developer Experience Evaluation.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the final success criteria.
- **External**
  - *Platform Engineer's Handbook* — the Developer Experience Evaluation
    chapter checklist.

## Changelog

- **2026-08-20** — Post-review fixes applied (see REVIEW.md): panels 3 and 8 regenerated, Panel 2 alt corrected, minor/nit wording fixes in article and summary; spec itself unchanged. *(Željko, AI-mediated session)*
- **2026-08-20** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-20** — Initial spec, article, checklist, summary, and dialog written; spec and post agree. Status `accepted`. *(Željko, AI-mediated session)*
