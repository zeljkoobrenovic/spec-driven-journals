---
timetoread: 2 min
---

In Spec-Driven Journals, source wins: durable changes belong in the markdown, specs, config, templates, and assets under version control — not in the generated HTML. The generated site is what readers see and share, but it is a review and publication surface, recreated on every build, never the place to edit.

**What changes**

- Markdown in git becomes canonical. The files humans and AI agents edit live under `_journals/`, `_templates/`, `_wiring/`, and `_start/` — post sources, specs, modality docs, config, templates, the build script, and the start-page catalog. All of it is diffable, citable, and readable by an agent before it acts.
- Generated HTML under `docs/` is treated strictly as output. It still matters — it exposes rendering problems, broken cross-links, and missing assets, and it is what static hosting publishes — but each build removes and recreates `docs/<journal>/`, so manual edits there are fragile by design.
- Authoring becomes a stable loop: change source, build, inspect the rendered page, return to source if something is wrong, commit source and output together. The generated site is a feedback loop, not a second editing surface — which prevents source and published page from silently diverging.
- Specs, posts, and generated docs get distinct roles: `spec.md` states intent and which modalities it drives; `index.md` carries the published argument; `summary.md`, `dialog.md`, and `comics.md` derive from the same spec; the generated `.spec.html` and post HTML let reviewers and readers inspect everything in the browser. When a post changes direction, the spec changes first.
- The principle extends existing foundation records — [[markdown-records]] and [[markdown-records-as-canonical]] — and is anchored in concrete URLs: the official GitHub repository is canonical, the generated GitHub Pages site is the reading surface.

**What it costs**

- Discipline at the boundary: a rendered page that exposes a problem sends you back to source, never to a quick patch in `docs/` — even when the HTML fix would be faster.
- Spec upkeep: when a post moves beyond its spec, the spec is drifted and must be reconciled, an obligation accepted to keep intent visible across AI-mediated sessions.

**What we are not doing**

- Not rewriting the foundation decision on markdown records — this article cross-links it rather than restating the ADR.
- Not comparing knowledge-management tools, and not defining publishing governance for every journal.
- Not claiming every thought must start in markdown — conversations, sketches, and AI sessions shape the work; only the accepted durable artifact must land in source.

The Article tab has the full canonical-layer table, the practical test for whether a journal behaves like source of truth, and the workflow detail.
