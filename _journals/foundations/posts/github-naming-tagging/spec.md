---
status: draft
revised: 2026-05-21
---

# Spec: GitHub Naming and Tagging Conventions

> Backfilled after the post. Part of the naming/tagging trio with
> [[aws-naming-tagging]] and [[package-naming-conventions]]; the same
> `<domain>-<system>-<component>` vocabulary travels across all three.

## Intent

Make Organization's GitHub estate queryable as a graph. Standardise repository
names, repository topics, branch names, commit shape, and git tags so that
humans, AI assistants, automation, and audit tooling all read the
organisation the same way. The record should be mechanical enough that a
reader can apply it without judgement calls.

## Audience

- **Engineers** creating repositories, branches, commits, and release tags.
- **Tech leads + architects** evaluating compliance and proposing exceptions.
- **Platform and devex teams** building tooling that reads GitHub topics or
  enforces the conventions in CI.
- **AI agents and inventory tooling** that query the org via the GitHub API.

## Success criteria

- [ ] Main record stays focused on the core decision; reference, tutorial, or playbook material is compact or moved out of the main flow.
- [ ] Reader can name a new repository correctly without asking.
- [ ] Reader can identify the required GitHub topic prefixes (`domain-*`,
      `system-*`, `lifecycle-*`, `tier-*`, `lang-*`) and what they mean.
- [ ] Reader can construct a branch name and a commit message that pass the
      convention check.
- [ ] Reader knows when to use SemVer `vX.Y.Z` vs date-based
      `release/YYYY.MM.DD[.N]` tags.
- [ ] Reader sees the link to [[aws-naming-tagging]] and
      [[package-naming-conventions]] and understands the shared vocabulary.

- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the opening decision flow.

## Non-goals

- Changing ownership, team structure, or which team owns which repo.
- Replacing [[jira-workflow-standards]] (Jira keys are referenced, not
  redefined).
- Defining the domain/system/component shortlist itself — that's a separate,
  evolving artefact.
- Dictating internal code structure beyond root packages and namespaces.

## Open questions

- The exact controlled vocabulary for `domain-*` and `system-*` topics —
  intentionally deferred to the shortlist record.
- Whether `lifecycle-*` should include a `lifecycle-archived` state distinct
  from GitHub's own archived flag.
- Migration plan for existing non-compliant repos (rename vs grandfather).
- How to handle multi-language repos against the `lang-*` topic convention
  (multiple topics? primary only?).

## Decision log

- **2026-05-21** — Focused the post around the core decision and condensed long tutorial, playbook, or reference sections so readers can reach the guidance quickly.
- **2026-05-20** — Moved vocabulary from the opening flow into an
  appendix so the main foundation record stays focused on decision,
  rationale, and workflow.
- **2026-05-20** — Used `<domain>-<system>-<component>` as the **shared
  logical name** across this record, [[aws-naming-tagging]], and
  [[package-naming-conventions]]. Considered per-ecosystem-native names;
  rejected because the value of the standard is precisely that one
  artefact in GitHub, AWS, and a package registry are connectable by
  string match.
- **2026-05-20** — Required **flat topic prefixes** (`domain-*`,
  `system-*`, `lifecycle-*`, `tier-*`, `lang-*`) on every repo.
  Considered hierarchical topic names (`domain/listings`); rejected
  because the GitHub API treats topics as flat strings and the prefix
  convention preserves queryability without inventing structure GitHub
  doesn't model.
- **2026-05-20** — Adopted **Jira keys embedded in branch names and
  commit footers**. Considered leaving Jira-references optional;
  rejected because the same standard wants end-to-end traceability and
  optional fields are routinely skipped.
- **2026-05-20** — Used **SemVer for libraries**, **date-based tags for
  deployable services**. Considered one scheme for both; rejected
  because they answer different questions (compatibility vs release
  ordering), and forcing one scheme hides one of those.
- **2026-05-20** — Made the policy **mechanical**, not aspirational.
  Considered guidelines-with-exceptions; rejected because the standard's
  whole point is queryability — exceptions defeat it.

## Sources

- **Internal**
  - [[aws-naming-tagging]] — companion record using the same
    `<domain>-<system>-<component>` vocabulary.
  - [[package-naming-conventions]] — companion record completing the
    naming trio.
  - [[jira-workflow-standards]] — the issue tracker whose keys this
    record requires in branch and commit footers.
- **External**
  - Conventional Commits — the commit format this record adopts.
  - SemVer 2.0 — the versioning scheme for libraries.
  - GitHub API topic documentation — informs the flat-topic-with-prefix
    pattern.

## Changelog

- **2026-05-21** — Shortened and refocused `index.md`; kept stable identifiers and permalinks. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Moved vocabulary in `index.md` to an end
  appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Retrofitted to 7-section template (added Decision log
  and Sources). *(Zeljko, AI-mediated session)*
- **2026-05-20** — Reset status to `draft`. Specs were backfilled and later cleaned up; keep them current during substantive post edits. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Backfilled spec after the post existed. *(Zeljko,
  AI-mediated session)*
