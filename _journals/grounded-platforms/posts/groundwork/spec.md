---
status: accepted
revised: 2026-08-20
---

# Spec: Groundwork — Repositories, Secrets, and Releases

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Open the Reference Implementation section: fix the shape of the groundwork a
platform team in my organization lays before it builds anything for anyone
else. The post turns the Groundwork chapter of *The Platform Engineer's
Handbook* into an operating record: the platform's own foundation is code —
repositories provisioned by IaC from one configuration file that is the source
of truth, secrets kept in a vault and never in source control, team onboarding
and offboarding as reviewed configuration diffs, commits conventional and
signed under branch protection that binds administrators too, and trunk-based
delivery where pushes trigger validation and annotated tags trigger a gated
release workflow. The load-bearing test: a second platform engineer can
reproduce the entire foundation from the repository alone. The handbook's
stack (Pulumi + Python, Bitwarden, GitHub, CircleCI, Kind/Helm) is named
honestly as the reference stack; the record's commitments are stated at the
capability level.

## Audience

Platform teams in my organization starting a platform build (so they know the
shape of the groundwork I hold them to); platform leads reviewing an existing
foundation against the bar; peer executives who want to see what
"everything-as-code from day zero" concretely means. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the foundation-as-code
      shape end to end and the groundwork test: reproducible by a second
      platform engineer from the repository alone.
- [x] **Foundation-as-product survives** — platform treated as a product
      focused on DevEx from day zero: stakeholders identified, short feedback
      loops, metrics for adoption/reliability/delivery/satisfaction, golden
      paths and sensible defaults, security/governance/testing/compliance
      embedded from the beginning.
- [x] **Tooling baseline and repository architecture survive** — the core
      tooling preparation (IaC, vault, source control, CI/CD with local
      runner, local Kubernetes for later, Python quality toolchain) and the
      deliberate repository decisions: monorepo vs. polyrepo, domain
      boundaries, naming and branch conventions, access roles, policies,
      cross-domain guardrails; plus the reproducible administration project.
- [x] **Secrets discipline survives** — example files committed, real values
      gitignored, credentials held in the vault via a scripted
      authenticate/unlock/upsert/sync/lock flow, verified in the vault;
      including the Pulumi-secret exercise.
- [x] **Configuration-driven repos and membership survive** — one YAML file
      as source of truth; repositories created programmatically through
      preview → review → apply; visibility by configuration; delete
      protection proven against accidental destroy; org members defined with
      name/username/role/email; onboarding, offboarding, and role changes as
      applied-and-verified config diffs; admin access preferred through a
      service account or group.
- [x] **Commit and policy discipline survives** — Conventional-Commits-style
      structure validated by a distributed commit-msg hook, pre-commit fast
      checks, planned changelog/version automation; branch protection and
      merge requirements enforced through IaC; signed commits required and
      verified (rejection and success), administrators included, extended to
      all branches per the expand-policy exercise.
- [x] **Trunk-based release flow survives** — integration through main,
      validation triggered by pushes, releases triggered by annotated tags
      through preview, automated tests, configuration validation, and an
      approval gate before apply; rollback triggers considered and rollback
      mechanisms regularly tested; the first-release exercise and the
      chapter completion check reproduced in the checklist.
- [x] **Credit is explicit** — References name *The Platform Engineer's
      Handbook* and the Groundwork chapter checklist.

## Non-goals

- Not [[platform-creation]] — no clusters, environments, GitOps, or mesh yet;
  this record ends at a tagged, gated release of the foundation itself.
- Not [[cicd-as-a-platform-service]] — the pipelines here serve the platform
  team's own administration repositories; CI/CD offered as a product to
  application teams lives there.
- Not [[policy-as-code]] — repository policies here are enforced through IaC
  at the source-control layer; cluster admission policy and general
  policy-as-code live there.
- Not [[self-service-onboarding]] — membership automation here covers the
  platform team itself; onboarding application teams to the platform at
  scale lives there.
- Not a tool mandate — the reference stack is the worked example; the
  commitments hold under any stack with the same properties.

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

- **2026-08-20** — Grounded in the Groundwork chapter checklist of *The
  Platform Engineer's Handbook* — the build-it-end-to-end companion whose
  reference implementation this section follows — read through a
  practitioner-executive lens, as with every record in this journal.
- **2026-08-20** — Tools framed as the worked example, not the mandate: the
  article commits at the capability level ("repositories are provisioned by
  IaC from one configuration file") and carries a Reference Stack table
  naming the handbook's tools with the property each one stands for; the
  checklist keeps the concrete tool-and-file steps because it is the runnable
  build sequence. Rejected: scrubbing tool names entirely (the record would
  stop being a reference implementation) and mandating the stack (the
  journal's commitments must outlive any one tool choice).

## Sources

- **Internal**
  - `sources/checklists/plaform-engineer-handbook/Checklist_ PEH _ 01 _ Groundwork.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the exercises and the completion check.
- **External**
  - *The Platform Engineer's Handbook* — the Groundwork chapter checklist.

## Changelog

- **2026-08-20** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
- **2026-08-20** — Comics modality added (comics.md, Comic tab, shared VERA/KAI
  cast); 3 inline figures generated in the article. *(Željko, AI-mediated
  session)*
- **2026-08-20** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
