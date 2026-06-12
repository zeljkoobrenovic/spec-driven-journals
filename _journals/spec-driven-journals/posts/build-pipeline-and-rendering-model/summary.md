---
timetoread: 2 min
---

The journal build is intentionally small: Python collects source into structured JSON payloads, templates embed those payloads, and browser-side JavaScript renders markdown, links, images, diagrams, and custom blocks. The generator does not try to be a general static-site framework — it reads a narrow source shape and writes predictable HTML under `docs/<journal>/`.

**What changes**

- The pipeline is describable end to end: `_wiring/build.py` walks `_journals/`, skips directories without `config.yaml`, parses each journal config with a tiny in-script YAML subset parser (no PyYAML), reads the posts each section lists, rewrites asset paths, resolves `[[permalink]]` cross-links, splits custom fenced blocks, merges per-post assets, and writes generated pages.
- Every post becomes a JSON payload shaped `{meta, tags, modalities: [{key, label, meta, blocks}]}` embedded in a `<script id="data" type="application/json">` element. `modalities` holds one entry per doc the post ships — the article plus any sibling `summary.md`, `dialog.md`, or `comics.md`. A single-modality post shows no tab bar; with more than one, the article is the default tab, non-default tabs render lazily on first activation, and the URL hash (`#summary`, `#dialog`, `#comics`) deep-links a tab.
- Templates use plain placeholder substitution (`__TITLE__`, `__DATA_JSON__`, ...) rather than Jinja or a framework, keeping the Python side easy to inspect.
- Specs render through the same template and renderer: `spec.md` becomes `<permalink>.spec.html`, the post byline gets a "View spec" link, and `drifted`/`superseded` statuses decorate that link. Previous/next navigation comes straight from `config.yaml` order.
- Local generated output maps directly to the public site: the same `docs/` tree the build writes is what the published journal serves.

**What it costs**

- The YAML parser supports only the config shape the project uses; advanced YAML features mean either avoiding them or improving the parser deliberately.
- Placeholder substitution has no template engine to catch mistakes — a misspelled placeholder fails silently.
- The renderer treats post content as trusted and lets raw HTML through, so the system is not designed for untrusted public submissions.
- Lazy tab rendering is a hard requirement, not an optimization: Mermaid, force-graph, and D3 measure container width, which is zero inside a hidden pane.

**What we are not doing**

- No line-by-line walkthrough of `build.py` — the article documents contracts, not helper functions.
- No reimplementation guide for the renderer, and no browser-side JavaScript tutorial.

The contract to preserve is the block envelope `{"type": ..., "content": ...}`; the modality layer wraps above it and never touches it. The Article tab covers the full pipeline, the payload model, and the rendering split — source layout is in [[anatomy-of-a-journal]].
