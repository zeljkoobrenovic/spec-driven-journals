---
status: draft
revised: 2026-06-12
---

# Spec: AI-Mediated Journal Operations

## Intent

Explain how AI agents should work in Spec-Driven Journals: read before editing, respect source of truth, update specs first for substantive changes, build scoped output, and summarize assumptions and verification.

## Audience

Human collaborators using Codex, Claude Code, or similar agents; AI agents reading Spec-Driven Journals guidance; maintainers reviewing AI-authored changes.

## Success criteria

- [ ] Reader understands the human-agent division of labor.
- [ ] Reader can describe a good AI-mediated authoring session.
- [ ] Reader knows what agents should avoid.
- [ ] Reader understands why dirty worktrees require caution.
- [ ] Reader sees the official project repository as the source agents should inspect.
- [ ] Article includes a named illustration placeholder showing the human-agent session flow.

## Non-goals

- Tool-specific prompt catalog.
- Security policy for all AI development.
- Model selection guidance.

## Modalities

Which docs this spec drives beyond the main article (`index.md`).

- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None for this draft.

## Decision log

- **2026-05-22** - Kept this article focused on repository operations rather than general AI coding practice.
- **2026-05-22** - Added a named illustration placeholder for the AI-mediated workflow.
- **2026-05-22** - Added a closing handoff from authoring operations to the implementation articles.
- **2026-05-22** - Added the official project repository to the agent read-before-editing context.
- **2026-05-22** - Replaced casual repository phrasing with formal Spec-Driven Journals naming and official links.

## Sources

- **Internal**
  - [[ai-mediated-authoring]] - durable rationale and workflow.
  - [AGENTS.md](https://github.com/zeljkoobrenovic/spec-driven-journals/blob/main/AGENTS.md) - agent-facing operating instructions.
  - [[spec-driven-authoring-workflow]] - local workflow.
- **External**
  - None in this draft.

## Changelog

- **2026-06-12** - Added Modalities section; the spec now drives summary.md, dialog.md, and comics.md alongside the article. Status `draft`. *(Zeljko, AI-mediated session)*
- **2026-05-22** - Initial spec and article draft. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Added illustration requirement and placeholder plan. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Added readability and sequence review updates. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Added official project link to the AI operating guidance. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Replaced casual repository phrasing with formal project naming. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
