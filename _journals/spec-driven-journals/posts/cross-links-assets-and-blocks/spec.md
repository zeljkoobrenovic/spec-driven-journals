---
status: draft
revised: 2026-05-22
---

# Spec: Cross-Links, Assets, and Blocks

## Intent

Explain the content features that make posts navigable and richer than plain markdown: cross-record links, asset rewriting, clickable images, and custom block fences.

## Audience

Authors and maintainers writing posts with links, images, diagrams, tables, or custom visualization blocks.

## Success criteria

- [ ] Reader can use double-bracket permalink links correctly.
- [ ] Reader understands image and asset path conventions.
- [ ] Reader knows body images open in a new tab after rendering.
- [ ] Reader can name the supported custom block types and where to extend them.
- [ ] Reader sees an at-a-glance map before the detailed syntax sections.
- [ ] Article includes a named illustration placeholder showing links, assets, markdown, and custom blocks flowing into rendering.

## Non-goals

- Full Markdown syntax reference.
- Detailed D3, Mermaid, force-graph, or Wardley-map tutorial.
- Accessibility policy for all media.

## Open questions

- None for this draft.

## Decision log

- **2026-05-22** - Included clickable image behavior because the template now wraps markdown images in links to their own assets.
- **2026-05-22** - Added a named illustration placeholder for the content rendering map.
- **2026-05-22** - Moved this article into the authoring-model sequence and added an at-a-glance content feature map.
- **2026-05-22** - Replaced casual repository phrasing with formal Spec-Driven Journals naming and official links.

## Sources

- **Internal**
  - [AGENTS.md](https://github.com/zeljkoobrenovic/spec-driven-journals/blob/main/AGENTS.md) - cross-link, asset, and block contracts.
  - [_templates/post.html](https://github.com/zeljkoobrenovic/spec-driven-journals/blob/main/_templates/post.html) - renderer implementation.
  - [_wiring/build.py](https://github.com/zeljkoobrenovic/spec-driven-journals/blob/main/_wiring/build.py) - cross-link and block parsing.
  - [[build-pipeline-and-rendering-model]] - implementation context.
- **External**
  - None in this draft.

## Changelog

- **2026-05-22** - Initial spec and article draft. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Added illustration requirement and placeholder plan. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Added readability and sequence review updates. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Replaced casual repository phrasing with formal project naming. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
