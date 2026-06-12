---
status: draft
revised: 2026-06-12
---

# Spec: Build Pipeline and Rendering Model

## Intent

Explain how `_wiring/build.py` turns journal source into generated pages and why Spec-Driven Journals keeps Python-side build logic small while rendering markdown and custom blocks client-side.

## Audience

Maintainers, agent operators, and technical readers who need to understand implementation behavior before changing build or template code.

## Success criteria

- [ ] Reader can describe the build pipeline from config scan to generated HTML.
- [ ] Reader understands the embedded JSON payload model.
- [ ] Reader knows why templates use placeholder substitution instead of a framework.
- [ ] Reader understands specs, assets, cross-links, and post navigation at build time.
- [ ] Reader can connect generated local output to the public generated journal URL.
- [ ] Article includes a named illustration placeholder showing the build pipeline and rendering split.

## Non-goals

- Line-by-line walkthrough of `build.py`.
- Reimplementation guide for the renderer.
- Full browser-side JavaScript tutorial.

## Modalities

Which docs this spec drives beyond the main article (`index.md`).

- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None for this draft.

## Decision log

- **2026-05-22** - Explained implementation at the contract level rather than documenting every helper function.
- **2026-05-22** - Added a named illustration placeholder for the pipeline and renderer model.
- **2026-05-22** - Added an opening orientation that positions the article after the authoring-model articles.
- **2026-05-22** - Added source repository and generated journal links to the pipeline explanation.
- **2026-05-22** - Replaced casual repository phrasing with formal Spec-Driven Journals naming and official links.

## Sources

- **Internal**
  - [_wiring/build.py](https://github.com/zeljkoobrenovic/spec-driven-journals/blob/main/_wiring/build.py) - generator implementation.
  - [_templates/post.html](https://github.com/zeljkoobrenovic/spec-driven-journals/blob/main/_templates/post.html) - client-side renderer.
  - [_wiring/README.md](https://github.com/zeljkoobrenovic/spec-driven-journals/blob/main/_wiring/README.md) - build overview.
  - [[anatomy-of-a-journal]] - source layout.
- **External**
  - None in this draft.

## Changelog

- **2026-06-12** - Added Modalities section; the spec now drives summary.md, dialog.md, and comics.md alongside the article. Status `draft`. *(Zeljko, AI-mediated session)*
- **2026-05-22** - Initial spec and article draft. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Added illustration requirement and placeholder plan. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Added readability and sequence review updates. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Added official project and generated journal links. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Replaced casual repository phrasing with formal project naming. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
