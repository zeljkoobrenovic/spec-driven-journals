---
status: draft
revised: 2026-05-21
---

# Spec: Markdown Records as the Default Format

> Backfilled after the post. This is the foundation that everything else in
> this repository assumes; the spec captures why the choice is durable
> rather than just expedient.

## Intent

Establish markdown records in git, published as a static site, as
Organization's default format for high-quality, long-lived technical writing —
decisions, strategies, discussion documents, principles, foundational
engineering records. The record should justify the choice well enough that
future challenges ("why not Confluence?", "why not Notion?", "why not
ADRs-in-Jira?") can be answered without rediscovering the reasoning.

## Audience

- **Authors** of decisions, strategies, and principles deciding where to
  put a new record.
- **Reviewers and architects** evaluating proposals to migrate away from
  markdown.
- **Tool buyers / leadership** comparing markdown-in-git against SaaS
  alternatives.
- **AI agents** that will consume the corpus as long-form context.

## Success criteria

- [ ] Main record stays focused on the core decision; reference, tutorial, or playbook material is compact or moved out of the main flow.
- [ ] Reader can state what kind of writing belongs in markdown records
      and what doesn't (runbooks, product docs, Slack threads, etc.).
- [ ] Reader can describe the canonical format (MADR-inspired markdown,
      small metadata header) without looking it up.
- [ ] Reader understands that discussion may happen elsewhere (PRs, Slack,
      Google Docs) but the markdown record is the durable source of truth.
- [ ] Reader sees how this foundation enables [[ai-mediated-authoring]],
      [[spec-driven-authoring]], the curator role, and the static-site
      pipeline.
- [ ] Reader can argue the choice against Confluence/Notion/Jira-ADRs with
      reference to specific properties (diff-friendly, git-native,
      AI-readable, no vendor lock-in).

## Non-goals

- Replacing short-lived communication, runbooks owned by service teams,
  ticket descriptions, or product documentation.
- Mandating a single repository — domain repos following the same
  conventions are explicitly allowed.
- Pre-committing to a specific publication target (GitHub Pages vs
  Okta-protected CDN proxy depends on access control needs).
- Defining the full editorial workflow — that's the job of
  [[ai-mediated-authoring]], [[spec-driven-authoring]], and the curator
  record.

## Open questions

- How tightly to couple "markdown record" to *this* repository's specific
  build (MADR shape, `[[…]]` resolver, block fences) versus keeping the
  format portable.
- Whether to add a "deprecated record" lifecycle state with a redirect
  mechanism in the build.
- Long-term storage and search across multiple domain repos that adopt the
  format.

## Decision log

- **2026-05-21** — Focused the post around the core decision and condensed long tutorial, playbook, or reference sections so readers can reach the guidance quickly.
- **2026-05-20** — Chose **markdown in git, published as a static site**
  over Confluence, Notion, and Jira-ADRs. Considered all three;
  rejected because: Confluence/Notion lock content to one vendor and one
  rich-text shape, neither survives diff review or AI ingestion well,
  and Jira ADRs lock long-form writing into an issue tracker that wasn't
  designed for it.
- **2026-05-20** — Adopted **MADR-inspired** structure with a small
  metadata header. Considered free-form markdown; rejected because the
  whole corpus reads as one body of reasoning, and structural
  consistency makes that legible.
- **2026-05-20** — Allowed **multiple repositories** following the same
  conventions, not a single monorepo. Considered enforcing one repo;
  rejected because domain teams need locality and federated repos can
  still adopt the same build + format.
- **2026-05-20** — Treated **discussion venues as ephemeral**, the
  markdown record as canonical. Considered embedding discussion threads
  in records; rejected because the discussion fades while the decision
  endures, and conflating them dilutes the record.

## Sources

- **Internal**
  - [[ai-mediated-authoring]] — depends on this record's choice of
    markdown for AI-readability.
  - [[spec-driven-authoring]] — same.
  - [[curator-role]] — same.
- **External**
  - [MADR: Markdown Architectural Decision Records](https://adr.github.io/madr/)
    — the structural inspiration.
  - Michael Nygard, *Documenting Architecture Decisions* — the original
    ADR pattern.
  - Jekyll and similar static-site generators — informs the build
    pipeline shape (markdown source, plain HTML output).

## Changelog

- **2026-05-21** — Shortened and refocused `index.md`; kept stable identifiers and permalinks. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Retrofitted to 7-section template (added Decision log
  and Sources). *(Zeljko, AI-mediated session)*
- **2026-05-20** — Reset status to `draft`. Specs were backfilled and later cleaned up; keep them current during substantive post edits. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Backfilled spec after the post existed. *(Zeljko,
  AI-mediated session)*
