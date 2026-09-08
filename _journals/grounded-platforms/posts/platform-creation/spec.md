---
status: accepted
revised: 2026-08-20
---

# Spec: Platform Creation: Environments, GitOps, and the Mesh

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the shape of the build I hold a platform team to when they create a
platform from scratch. The post turns the Platform Creation chapter of the
*Platform Engineer's Handbook* into a reference-implementation record: the
platform's environments are declarative infrastructure-as-code stacks with
isolated, planned networks and pinned versions; provisioning and runtime
configuration are deliberately separated into two repositories, with a GitOps
controller continuously reconciling the clusters against Git; every change
promotes through one pipeline — lint, test, preview, deploy, validate —
sandbox first, then dev, then a recorded approval before production;
service-to-service traffic runs through a mesh with controlled ingress and
mTLS; misconfiguration is killed by policy checks before it reaches the GitOps
repository; and the finished platform is a semantically versioned release. The
load-bearing idea: **the platform exists in Git, not in the clusters** — if
the clusters vanished tonight, the pipeline could rebuild every environment
from a tagged commit by morning.

## Audience

Platform leads and engineers in my organization building a new platform (so
they know the end-to-end shape the build is held to); infrastructure and
DevTools leaders reviewing a platform build plan; peer executives who want to
see what "declarative and reproducible" concretely means.
First-person declarative.

## Success criteria

- [x] **Principle is quotable** — the highlight states the defining property
      (the platform exists in Git, not in the clusters) and the running test:
      could the pipeline rebuild every environment from a tagged commit.
- [x] **Environments survive** — three stacks (platform-sandbox, app-dev,
      app-prod), one configuration file per stack, unique cluster names,
      pinned node images, readiness settings, consistent security and
      governance across environments, smaller non-prod capacity, and platform
      versus application environments as separate SDLC concepts.
- [x] **Network and runtime survive** — explicit configuration models; a
      unique network per environment; non-overlapping CIDRs checked against
      VPN and host ranges; cluster, pod, and service CIDRs defined; minimal
      ingress port maps (HTTP/HTTPS); zero-trust exposure; ordered creation
      (network before cluster); generated kubeconfig feeding the provider;
      exported stack outputs; nodes verified Ready.
- [x] **Pipeline and validation survive** — infrastructure tests (BATS) that
      read stack outputs, set up kubeconfig, and fail clearly; quality and
      security gates (Black, mypy, isort, static analysis, Semgrep, Trivy)
      tuned against false positives; pipeline stages lint → pre-deploy test →
      preview → deploy → post-deploy validation; sandbox from main, Git tags
      for production releases, validation after every environment, a recorded
      manual approval before app-prod, gates only where they add governance
      value.
- [x] **GitOps split survives** — platform-core (provisioning) versus
      platform-gitops (runtime/application configuration); no application
      manifests managed by IaC; Helm/Kustomize for application lifecycle; Flux
      installed from platform-core, version-pinned, controllers verified
      healthy; app-of-apps structure with per-environment directories,
      GitRepository and Kustomization resources, reconciliation intervals,
      pruning, health waits; drift reconciled and failures visible; new team
      repositories onboarded declaratively; platform services deployed via
      GitOps with pinned versions, never by hand.
- [x] **Mesh and observability hooks survive** — Istio deployed through
      GitOps, chart pinned; base plus control plane; gateway for controlled
      ingress; VirtualService routing; mTLS enabled and verified; authorization
      and network policies where isolation is required; proxy resource and
      latency overhead monitored; metrics, tracing, and log hooks confirmed
      with the full observability platform explicitly deferred.
- [x] **Policy-as-code survives** — OPA/Rego policies with conftest in the
      pipeline; no floating `latest` tags; no wildcard chart versions;
      reproducible pinned deployments; checks run before manifests reach the
      GitOps repository and fail the pipeline early; policies tested for both
      allowed and rejected cases; enforcement consistent across environments.
- [x] **Release and definition of done survive** — the final validation
      sweep, semantic version tag driving the release pipeline across all
      environments, the working version recorded as baseline; the chapter's
      definition of done reproduced in the checklist.
- [x] **Tools are the worked example, not the mandate** — a reference-stack
      table (role → reference tool → the property that matters) appears early;
      every commitment is stated at capability level.
- [x] **Credit is explicit** — References name the *Platform Engineer's
      Handbook* and the Platform Creation chapter checklist.

## Non-goals

- Not [[groundwork]] — repository conventions, secrets management, and
  release discipline precede this build and are assumed by it.
- Not [[platform-security]] — end-to-end hardening of the running platform
  lives there; this record stops at mesh mTLS and pipeline-level checks.
- Not [[observability-implementation]] — this record only confirms telemetry
  hooks exist; the observability platform is that record.
- Not [[cicd-as-a-platform-service]] — the pipeline here builds the platform
  itself; CI/CD offered as a product to application teams is that record.
- Not [[policy-as-code]] — pipeline-time conftest checks live here;
  admission-time enforcement inside the clusters lives there.
- Not a tool mandate — the PEH stack (Pulumi, Kind, CircleCI, Flux, Istio,
  OPA/conftest) is the reference implementation; commitments hold at the
  level of the capability.

## Modalities

The working build ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-08-20** — Grounded in the Platform Creation chapter of the *Platform
  Engineer's Handbook* (PEH), via its chapter checklist — read through a
  practitioner-executive lens, as with every record in this journal.
- **2026-08-20** — Framed around one defining property — the platform exists
  in Git, not in the clusters — rather than as a stage-by-stage build
  narrative. Rejected: a tool-mandating runbook (the journal states
  capabilities, not vendor choices); also rejected: abstracting the tools
  away entirely, which would lose the reference-implementation value — the
  stack is named honestly as the worked example.

## Sources

- **Internal**
  - `sources/checklists/plaform-engineer-handbook/Checklist_ PEH _ 02 _ Platform Creation.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the definition of done.
- **External**
  - *Platform Engineer's Handbook* — the Platform Creation chapter checklist
    (environments, network foundation, Kubernetes runtime, CI/CD, GitOps,
    Istio, pipeline policy checks, release).

## Changelog

- **2026-08-20** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
- **2026-08-20** — Comics modality added (comics.md, Comic tab, shared
  VERA/KAI cast); 3 inline figures generated in the article. *(Željko,
  AI-mediated session)*
- **2026-08-20** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
