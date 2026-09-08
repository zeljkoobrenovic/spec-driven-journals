---
status: accepted
revised: 2026-08-20
---

# Spec: CI/CD as a Platform Service

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the shape I hold a platform team to when it takes over CI/CD as a
platform service. The post turns the "CI/CD as a Platform Service" chapter
checklist of the *Platform Engineer's Handbook* into a reference-implementation
record: CI/CD stops being a per-team craft and becomes a product. One
platform repository holds the reusable actions and composed pipeline
templates, semantically versioned so teams can pin; team pipelines shrink to
minimal wrappers (roughly thirty lines) that declare *what* the service needs
while the platform owns *how*. Security scanning is a gate that keeps
vulnerable images out of the registry, not a report; delivery is progressive
(canary or blue-green) with metric-driven automated rollback; and the
pipeline itself is instrumented, so DORA metrics, bottlenecks, and adoption
are measured rather than guessed. The load-bearing idea: a growing team pipeline is not that
team's problem — it is a platform capability we have not built yet.

## Audience

Platform leads and teams in my organization building or consolidating CI/CD
(so they know the end-to-end shape the build is held to); application-team
leads deciding whether to migrate onto the platform pipeline; peer executives
funding the consolidation. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight carries the what/how split, the
      ~30-line wrapper test, the versioned platform repository, the scan
      gate, progressive delivery with automated rollback, and the
      instrumented pipeline.
- [x] **Baseline survives** — checklist §1: inventory of existing workflows,
      workflow and pipeline line counts, shared-action usage, baseline
      adoption rate, and the recorded baselines (deployment frequency, lead
      time, change failure rate, MTTR, p95 build duration, security scan
      pass rate).
- [x] **The platform repository survives** — checklist §2–§4: the
      `actions/` / `workflows/` / `tests/` / `docs/` layout, reusable tasks
      kept separate from composed templates, the container-build action
      (Buildx, caching, metadata and tags, registry auth, Trivy, fail on
      HIGH/CRITICAL, vulnerable images never pushed, tag and digest outputs,
      pinned third-party actions), and CI for the platform's own actions
      (action.yml validation, required fields, described inputs, invalid
      actions cannot release).
- [x] **Templates and minimal wrappers survive** — checklist §5–§6: reusable
      workflows per application type with typed inputs, defaults,
      workflow-level secrets, testing, linting, build-and-scan, deployment
      stages, job dependencies, controlled escape hatches, exposed outputs;
      team pipelines as sub-30-line wrappers; large team-specific logic read
      as a missing platform capability.
- [x] **Versioning survives** — checklist §7: semantic versioning with
      major/minor/patch semantics, specific release tags, floating major
      tags, team pinning, documented breaking changes and migration
      requirements.
- [x] **Progressive delivery survives** — checklist §8: Argo Rollouts,
      strategy chosen per service (blue-green for instant switching, canary
      for gradual shifting), analysis wired to Prometheus success-rate
      thresholds, automatic stop/rollback of unhealthy releases, previous
      stable release recoverable.
- [x] **CI/CD observability survives** — checklist §9: OpenTelemetry
      Collector receiving workflow events, metrics to Prometheus, traces to
      the tracing backend and visible in Grafana, trigger-to-deployment
      tracing, stage timing, failures associated with commits, telemetry
      used to find bottlenecks.
- [x] **Migration and validation survive** — checklist §10–§11: a real
      application pipeline migrated end to end (inputs, secrets, pinned
      version, GitOps manifests, Flux applies, Rollouts deploys) and the
      final validation list including DORA measurability, adoption metrics,
      demonstrated line-count reduction, and migration documentation.
- [x] **Tools are the worked example, not the mandate** — a reference-stack
      table names the PEH stack honestly; every commitment is stated at the
      capability level.
- [x] **Credit is explicit** — References name the *Platform Engineer's
      Handbook* and the "CI/CD as a Platform Service" chapter checklist.

## Non-goals

- Not [[observability-implementation]] — the platform-wide observability
  stack lives there; this record instruments only the pipeline itself
  (workflow telemetry, traces, DORA metrics).
- Not [[platform-security]] — end-to-end cluster and supply-chain security
  lives there; this record carries only the build-time scan gate.
- Not [[platform-creation]] — the GitOps machinery (Flux, environments, the
  mesh) is built there; this record's pipeline ends at a manifest change and
  a verified handoff to it.
- Not [[starter-kits]] — how *new* services get the platform pipeline from
  day one lives there; this record covers building the service and migrating
  existing pipelines onto it.
- Not [[policy-as-code]] — admission-time policy enforcement inside clusters
  lives there; this record's gates run in the pipeline.
- Not [[platform-as-a-product]] — the general product operating mechanics;
  this record applies them to one offering: CI/CD.

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

- **2026-08-20** — Grounded in the "CI/CD as a Platform Service" chapter
  checklist of the *Platform Engineer's Handbook* — the reference
  implementation companion to this journal's Platform Engineering section —
  read through a practitioner-executive lens, as with every record in this
  journal.
- **2026-08-20** — Commitments stated at the capability level with the PEH
  stack (GitHub Actions, Trivy, Argo Rollouts, Flux, OpenTelemetry,
  Prometheus, Grafana) named as the reference stack rather than a mandate;
  the alternative — writing the record as a GitHub-Actions-specific runbook —
  was rejected because the journal's records must survive a tooling change.
- **2026-08-20** — The ~30-line team pipeline kept as a concrete, quotable
  test rather than softened to "small": the number is the chapter's own
  target and is what makes the what/how split checkable.

## Sources

- **Internal**
  - `sources/checklists/plaform-engineer-handbook/Checklist_ PEH _ 08 _ CI_CD as a Platform Service.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`).
- **External**
  - *Platform Engineer's Handbook* — the "CI/CD as a Platform Service"
    chapter and its checklist.

## Changelog

- **2026-08-20** — Post-review fixes applied (see REVIEW.md), including a
  spec-side edit: the Intent's long semicolon-chain sentence split into three
  sentences. *(Željko, AI-mediated session)*
- **2026-08-20** — Comics modality added (comics.md, Comic tab, shared
  VERA/KAI cast); 3 inline figures generated in the article. *(Željko,
  AI-mediated session)*
- **2026-08-20** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
