---
status: draft
revised: 2026-05-21
---

# Spec: AWS Account and Resource Naming and Tagging Conventions

> Backfilled after the post. Companion to [[github-naming-tagging]] and
> [[package-naming-conventions]]; the AWS view of the org should line up
> with the GitHub view.

## Intent

Standardise AWS account structure, resource naming, and resource tagging so
that cost, ownership, blast radius, and compliance scope are all queryable
from tags alone. Make the AWS view of Organization's estate align with the
GitHub view via the shared `<domain>-<system>-<component>` vocabulary. The
record should be mechanical and enforceable, not aspirational.

## Audience

- **Cloud engineers and platform team** provisioning accounts and resources.
- **FinOps and security teams** reading cost reports, audit dashboards, and
  compliance scopes off tags.
- **Domain teams** that own workloads and need to know what to put on their
  resources.
- **Tooling owners** writing SCPs, AWS Config rules, tag policies, and
  inventory exports.
- **AI agents** correlating an AWS resource with its GitHub repo and owning
  team.

## Success criteria

- [ ] Main record stays focused on the core decision; reference, tutorial, or playbook material is compact or moved out of the main flow.
- [ ] Reader can name a new AWS account (`org-<domain>-<env>`) and place it
      under the correct OU.
- [ ] Reader can name a resource (`org-<domain>-<system>-<component>-<env>
      [-<qualifier>]`) without ambiguity.
- [ ] Reader can list the required tag keys from memory or the table:
      `Owner`, `Domain`, `System`, `Component`, `Environment`, `CostCenter`,
      `DataClass`, `Compliance`, `ManagedBy`, `RepoUrl`.
- [ ] Reader understands names are for humans and tags are authoritative
      for tooling.
- [ ] Reader sees enforcement is automated (SCP/Config/tag policies), not
      manual review.

## Non-goals

- Defining the controlled vocabularies for `Environment`, `CostCenter`,
  `DataClass`, `Compliance` — those are governed lists maintained by the
  platform team.
- Changing IAM permissions, account-vending workflow, or the operating model.
- Replacing existing service runbooks or migration plans.
- Covering non-AWS clouds.

## Open questions

- Migration path for existing non-compliant resources (rename impossible for
  many AWS types — re-create or grandfather with a deprecation tag?).
- How to handle multi-tenant resources where `Owner` is ambiguous.
- Whether the `qualifier` slot in resource names should have its own
  controlled vocabulary.
- Whether `RepoUrl` should be enforced via tag policy or remain advisory.

## Decision log

- **2026-05-21** — Focused the post around the core decision and condensed long tutorial, playbook, or reference sections so readers can reach the guidance quickly.
- **2026-05-20** — Made **tags authoritative**, not resource names.
  Considered embedding all metadata in names; rejected because resource
  names are mostly immutable in AWS, while tags can evolve with
  ownership and lifecycle. Names are for humans; tags are for tools.
- **2026-05-20** — Required a **fixed set of tag keys** (`Owner`,
  `Domain`, `System`, `Component`, `Environment`, `CostCenter`,
  `DataClass`, `Compliance`, `ManagedBy`, `RepoUrl`). Considered
  team-by-team tag conventions; rejected because cross-account cost
  reports and audit dashboards need uniform keys to be useful at all.
- **2026-05-20** — Adopted **automated enforcement** (SCPs, AWS Config
  rules, tag policies) for production. Considered review-time
  enforcement only; rejected because manual review of every resource
  doesn't scale and silent drift is the default failure mode.
- **2026-05-20** — Used **PascalCase tag keys, controlled-vocabulary
  tag values**. Considered free-form values; rejected because free-form
  tag values defeat reporting — by the second year they would contain
  every spelling variant of the same concept.
- **2026-05-20** — One AWS account per **single primary purpose**.
  Considered multi-purpose accounts to reduce account count; rejected
  because the account boundary is AWS's strongest isolation primitive,
  and merging purposes inside one account is the most common source of
  blast-radius incidents.

## Sources

- **Internal**
  - [[github-naming-tagging]] — companion record; the AWS view should
    line up with the GitHub view via the shared
    `<domain>-<system>-<component>` vocabulary.
  - [[package-naming-conventions]] — third leaf of the naming trio.
- **External**
  - AWS Well-Architected Framework, tagging best practices — informs
    the required tag keys.
  - AWS Organizations and Service Control Policies documentation —
    informs the enforcement model.
  - FinOps Foundation guidance on cost allocation by tags — informs
    `CostCenter`, `Owner`, `Domain`, `System` as cost-cuttable keys.

## Changelog

- **2026-05-21** — Shortened and refocused `index.md`; kept stable identifiers and permalinks. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Retrofitted to 7-section template (added Decision log
  and Sources). *(Zeljko, AI-mediated session)*
- **2026-05-20** — Reset status to `draft`. Specs were backfilled and later cleaned up; keep them current during substantive post edits. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Backfilled spec after the post existed. *(Zeljko,
  AI-mediated session)*
