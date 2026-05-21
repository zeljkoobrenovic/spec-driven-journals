---
status: draft
revised: 2026-05-20
---

# Spec: Practice Principle — Markdown Records as Canonical

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that the canonical record of any Organization technical decision,
strategy, or durable discussion is a **markdown file in git**. Slack,
Google Docs, meeting notes, and wiki pages support discussion; the
markdown record is the artifact other people will cite, search, link,
and learn from in two years. Where markdown and any other artifact
disagree, the markdown wins.

## Audience

- **Authors** of decisions, strategies, principles.
- **Reviewers** evaluating PRs against the canonical record.
- **Tools** (search, AI agents) treating markdown as the source.

## Success criteria

- [ ] Reader knows the markdown record **wins** in conflicts.
- [ ] Reader knows what canonicality buys (citability, search,
      AI-readability, longevity).
- [ ] Reader can identify when something belongs in a markdown
      record vs a transient venue.

## Non-goals

- Replacing Slack, Google Docs, or meetings as discussion venues.
- Defining the markdown structure (that's [[markdown-records]]).

## Open questions

- How to handle conflicts when a wiki page is more up-to-date than
  its markdown counterpart.

## Decision log

- **2026-05-20** — Made markdown **canonical**, not just
  recommended. Considered "multiple formats, pick one";
  rejected because multiple formats produce drift.
- **2026-05-20** — Stated **markdown wins in conflicts**.
  Considered "most recent wins"; rejected because that incentivises
  side-channel updates.

## Sources

- **Internal**
  - [[markdown-records]] — the foundational decision.
  - [[ai-mediated-authoring]] — depends on this principle.
- **External**
  - MADR — Markdown ADR template.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created.
