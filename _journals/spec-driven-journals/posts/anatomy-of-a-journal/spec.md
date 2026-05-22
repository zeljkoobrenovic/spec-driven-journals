---
status: draft
revised: 2026-05-22
---

# Spec: Anatomy of a Journal

## Intent

Describe the concrete folder and file structure of a journal so readers can add or inspect a journal without reading the generator first.

## Audience

Authors and maintainers adding posts, adding journals, or reviewing source structure.

## Success criteria

- [ ] Reader can identify the purpose of `config.yaml`, `posts/`, per-post `index.md`, `spec.md`, and assets.
- [ ] Reader understands how front matter controls generated URLs, titles, bylines, tags, icons, and hero images.
- [ ] Reader knows that post paths in config are relative to `posts/`.
- [ ] Reader understands why per-post folder layout is preferred.
- [ ] Reader can connect the described folder shape to the official project repository.
- [ ] Article includes a named illustration placeholder showing the journal folder anatomy.

## Non-goals

- Exhaustive Markdown syntax reference.
- Full implementation details of `build.py`.
- Visual design documentation.

## Open questions

- None for this draft.

## Decision log

- **2026-05-22** - Focused on the per-post folder layout because it is the convention used by current journals and supports sibling specs.
- **2026-05-22** - Added a named illustration placeholder for the folder and asset model.
- **2026-05-22** - Adjusted the article handoff so content mechanics follow the folder anatomy before the workflow article.
- **2026-05-22** - Added official source and generated-site links where the article introduces folder and output locations.
- **2026-05-22** - Replaced casual repository phrasing with formal Spec-Driven Journals naming and official links.

## Sources

- **Internal**
  - [_journals/README.md](https://github.com/zeljkoobrenovic/spec-driven-journals/blob/main/_journals/README.md) - journal structure and front matter.
  - [AGENTS.md](https://github.com/zeljkoobrenovic/spec-driven-journals/blob/main/AGENTS.md) - generator contract and conventions.
  - [[what-are-spec-driven-journals]] - series framing.
- **External**
  - None in this draft.

## Changelog

- **2026-05-22** - Initial spec and article draft. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Added illustration requirement and placeholder plan. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Added readability and sequence review updates. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Added official project and generated journal links. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Replaced casual repository phrasing with formal project naming. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
