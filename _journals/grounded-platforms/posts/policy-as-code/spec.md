---
status: accepted
revised: 2026-08-20
---

# Spec: Policy as Code Implementation

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the shape of the build I hold a platform team to when they implement
policy as code — part of the Reference Implementation section, the
how-it-concretely-looks companion to the conceptual records. The post turns
the Policy-as-Code Implementation chapter checklist of the *Platform
Engineer's Handbook* into a reference-implementation record: policies are
versioned code with **one policy source evaluated at three gates** — the
developer's desk (pre-commit), the pipeline (every pull request), and cluster
admission (the backstop). A core security floor is enforced, every violation
explains itself in language a developer can act on, enforcement is
progressive (audit before enforce), compliance is visible on a dashboard, and
the policy engine fits deliberately into the wider governance map. The
reference stack (OPA Gatekeeper, Rego, Conftest, Prometheus, Grafana,
Backstage) is named honestly as the worked example; the commitments are
stated at the level of the capability.

## Audience

Platform leads and teams in my organization building policy enforcement into
a Kubernetes-based platform (so they know the end-to-end bar the build is
held to); security and compliance leaders deciding where policy lives and who
owns it; peer executives assessing whether "we have guardrails" is actually
true. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states one policy source, three
      gates; the core floor; progressive enforcement; visible compliance; and
      the closing test that a policy that cannot explain itself does not get
      to block a deployment.
- [x] **Admission setup survives** — Gatekeeper installed and verified,
      validating admission webhook active, system-namespace exclusions
      deliberate; ConstraintTemplates and Constraints created, scoped,
      applied, and proven with a deliberately non-compliant workload
      (checklist §1, §3).
- [x] **The core policy floor survives** — CPU/memory requests and limits,
      no root, no privileged containers, read-only root filesystem where
      appropriate, dangerous capabilities blocked, approved image registries,
      and clear human-readable violation messages (checklist §2).
- [x] **Progressive enforcement survives** — audit mode first where
      appropriate, developer education on why each policy exists, feedback
      and exemption review, friction fixed, genuine security risks enforced,
      lower-risk standards monitored before enforcement (checklist §4).
- [x] **Shift-left survives** — the same policies run locally with Conftest,
      in pre-commit hooks, and as a policy-validation job on every pull
      request; the pipeline fails on required violations and feedback appears
      in the PR itself (checklist §5–§6).
- [x] **Compliance visibility survives** — Gatekeeper audit enabled,
      Prometheus scraping, violations by constraint and by namespace, an
      exporter where needed, and a Grafana dashboard with total-violations,
      by-constraint, by-namespace, compliance-rate, and remediation-trend
      panels, accessible to stakeholders; optional Backstage surfacing and
      service-level scorecard (checklist §7–§8, §11).
- [x] **Governance integration survives** — a deliberate split between
      Kubernetes-level and cloud-provider governance, portability watched,
      compliance data exported where required, and named ownership for policy
      creation, review, and remediation (checklist §9).
- [x] **The demo exercise and final validation survive** — the checklist
      reproduces the demo-application exercise (§10) and the Final Validation
      bar; the article's practice section states that bar as the definition
      of done.
- [x] **Tools are the worked example, not the mandate** — a reference-stack
      table (role → reference tool → the property that matters) appears
      early; commitments are stated at capability level.
- [x] **Credit is explicit** — References name the *Platform Engineer's
      Handbook* and the Policy-as-Code Implementation chapter.

## Non-goals

- Not [[platform-security]] — the end-to-end security build (identity,
  network, secrets, supply chain) lives there; this record is the policy
  engine and its lifecycle.
- Not [[cicd-as-a-platform-service]] — pipeline architecture lives there;
  this record only adds the policy-validation gate to it.
- Not [[observability-implementation]] — the metrics and dashboard
  infrastructure lives there; this record adds compliance panels on top of
  it.
- Not [[platform-creation]] — the cluster, GitOps, and mesh baseline these
  policies protect lives there; pipeline-level provisioning checks appear in
  that record, admission-time enforcement lives here.
- Not a Rego tutorial and not an OPA mandate — the stack is the reference
  implementation, not the commitment.

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

- **2026-08-20** — Grounded in the Policy-as-Code Implementation chapter
  checklist of the *Platform Engineer's Handbook*, read through a
  practitioner-executive lens, as with every record in this journal.
- **2026-08-20** — Framed around "one policy source, three gates" rather
  than as a Gatekeeper install guide: the durable commitment is that the
  same policy is evaluated at the desk, in the pipeline, and at admission.
  Rejected the tool-first framing — the stack is named in a reference table
  and the commitments stay at capability level.
- **2026-08-20** — Progressive enforcement kept as a first-class commitment
  rather than an implementation detail; rejected the binary on/off framing
  of enforcement, because the source's final validation explicitly requires
  policies enforced progressively and exceptions reviewed.

## Sources

- **Internal**
  - `sources/checklists/plaform-engineer-handbook/Checklist_ PEH _ 11 _ Policy as a Code Implementation.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the demo-application exercise and the final
    validation bar.
- **External**
  - *Platform Engineer's Handbook* — the Policy-as-Code Implementation
    chapter and its checklist.

## Changelog

- **2026-08-20** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
- **2026-08-20** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-20** — Initial spec, article, checklist, summary, and dialog written; spec and post agree. Status `accepted`. *(Željko, AI-mediated session)*
