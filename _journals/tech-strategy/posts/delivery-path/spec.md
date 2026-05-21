---
status: draft
revised: 2026-05-20
---

# Spec: Delivery Path Blueprint and Convergence Plan

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

State the **default code-to-production path** for Organization Germany:
one preferred source-control path per codebase, one preferred CI path,
one preferred deployment path per runtime class, automated build,
automated deploy, standard rollback. Name **GitHub + CircleCI** as the
current best candidate for the modern path; **TFS + manual** and
**Bitbucket + Jenkins** as retirement targets; GitLab as transitional.
Delivery path simplification is a strategy-level concern, not tooling
hygiene.

## Audience

- **Engineers** picking CI/CD for a new codebase.
- **Platform / devex team** maintaining the preferred paths.
- **Tech leads** evaluating delivery-path exceptions.
- **[[operate]] forum** sequencing convergence work.

## Success criteria

- [ ] Reader can pick the right delivery path for a new codebase
      without asking.
- [ ] Reader knows which combinations are **retirement targets**
      (TFS + manual, Bitbucket + Jenkins) and what "retirement
      target" means.
- [ ] Reader sees the three "no new" refusals: no new manual
      builds, no new manual deployments, no new CI/CD tool without
      approval.
- [ ] Reader knows delivery-path simplification is a strategy-level
      concern, not local tooling hygiene.

## Non-goals

- Picking the strategic CI/CD tool for the next 5 years
  (GitHub + CircleCI is "current best candidate", not eternal).
- Migration plans for specific services.
- Build-pipeline performance optimisations.

## Open questions

- Concrete classification process for GitLab paths (transitional vs
  retired).
- When and how to revisit GitHub + CircleCI as the preferred
  candidate.

## Decision log

- **2026-05-20** — Treated delivery-path simplification as
  **strategy**, not hygiene. Considered leaving it to platform team
  judgement; rejected because [[policy]] P3 makes it strategic and
  hygiene framing doesn't unlock investment.
- **2026-05-20** — Chose **GitHub + CircleCI** as current best
  candidate. Considered consolidating on GitLab; rejected because
  newer services already use GitHub + CircleCI and switching now
  would add migration cost.
- **2026-05-20** — Named TFS + manual and Bitbucket + Jenkins as
  **retirement targets**. Considered allowing them to stay where
  they work; rejected because duplication of modern capability is
  exactly the fragmentation the strategy removes.
- **2026-05-20** — Made the refusals **explicit** ("no new manual
  builds", "no new manual deployments", "no new CI/CD tool without
  approval"). Considered implicit guidance; rejected because
  delivery decisions are made one-at-a-time and need to fail loudly.

## Sources

- **Internal**
  - [[policy]] — P3 delivery path.
  - [[diagnosis]] — delivery fragmentation evidence.
  - [[github-naming-tagging]] — the GitHub conventions delivery
    paths sit inside.
- **External**
  - CircleCI, GitLab pipelines, Jenkins, TFS documentation.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
