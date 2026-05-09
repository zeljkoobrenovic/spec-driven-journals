# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A multi-journal static-site generator. Each subdirectory under `_journals/` is one journal site (e.g. `_journals/underhood/`). The build emits one site per journal under `docs/<journal-name>/`. There is no framework — just a small Python script, two HTML templates, and inline JS.

## Build

```bash
python3 _wiring/build.py        # builds every journal under _journals/
python3 -m http.server 8000 --directory docs   # local preview
```

The script uses only the Python standard library (no PyYAML, no requirements file). The `venv/` in the repo root is unused by the build.

There is no test suite, lint config, or CI yet.

## Pipeline (data flow)

1. `_wiring/build.py` walks each journal directory.
2. Reads `_journals/<j>/config.yaml` (parsed by a small in-script YAML subset parser — only the shape used by `config.yaml` is supported).
3. For each post listed under a section, parses front matter (`---`-fenced YAML-ish key/value block) and treats the body as markdown.
4. Splits the body into typed **blocks** (currently always one `markdown` block) — see "Extending blocks" below.
5. Embeds the structured data as JSON inside `_templates/index.html` and `_templates/post.html` via `__DATA_JSON__` placeholder substitution; client-side JS does the rendering.
6. Writes output to `docs/<j>/index.html` and `docs/<j>/posts/<slug>.html`. Assets are copied wholesale from `_journals/<j>/assets/` to `docs/<j>/assets/`.

The templates use plain `__PLACEHOLDER__` string substitution (not Jinja). Placeholders: `__TITLE__`, `__DESCRIPTION__`, `__JOURNAL__`, `__LOGO_HTML__`, `__BYLINE__`, `__DATA_JSON__`.

## config.yaml shape

```yaml
title: <site title>
description: <site subtitle>
logo: assets/images/<file>      # optional; rendered as a hero image on the index
sections:
  - title: <section title>
    description: <optional>
    posts:
      - <year>/<filename>.md     # path relative to _journals/<j>/posts/
```

The `logo` path is journal-relative (resolved against `docs/<j>/`); no rewrite is applied since the index sits at the journal root.

Posts within a section are sorted by **basename** at build time, regardless of yaml order. Both `.md` and `.markdown` extensions are accepted (the 2023 post still uses `.markdown`).

## Asset paths in posts

Posts reference images as `assets/images/...` (Jekyll-style, relative to the journal root). The build rewrites these to `../assets/...` so they resolve from the post's output location (`docs/<j>/posts/<slug>.html` — one level below the journal root). The rewrite (`_ASSET_REF` in `build.py`) covers markdown image/link syntax and raw HTML `src=`/`href=` attributes.

## Client-side rendering

- `index.html` builds the section list from embedded JSON and provides a search input that filters by `title + excerpt` substring (case-insensitive).
- `post.html` contains a small markdown renderer (subset: ATX headings, paragraphs, blockquotes, fenced code, inline code, bold/italic, links, images, lists, hr) and a `renderers` dispatch table keyed by block type.
- The renderer treats post content as **trusted** and lets raw HTML pass through unescaped — several posts embed inline `<blockquote style="…">` / `<div>` markup. Don't reintroduce a blanket HTML-escape in the inline pass.

## Block types

The post payload shape is `{ meta, blocks: [{ type, content }] }`. `split_into_blocks()` in `build.py` walks the post body and lifts recognized custom fences into their own blocks; everything else stays in `markdown` blocks.

Currently recognized fences (declared in `_BLOCK_FENCES`):

| Type | Open | Close | Build-side transform |
| --- | --- | --- | --- |
| `mermaid` | `---begin mermaid---` | `---end mermaid---` | none (raw diagram source) |
| `force-graph` | `---begin force-graph---` | `---end force-graph---` | `_parse_force_graph` → JSON `{nodes, links}` |
| `bubble-chart` | `---begin bubble-chart---` (also `buble-chart`) | `---end bubble-chart---` (also `buble-chart`) | `_parse_bubble_chart` → JSON `{nodes:[{name,size}]}` |

Open and close strings are each lists in `_BLOCK_FENCES` so a fence can accept multiple spellings (the bubble-chart entry tolerates both `bubble-chart` and the typo `buble-chart` on either side).

`mermaid` blocks render via `mermaid.js`; the renderer creates a `<div class="mermaid">` per block and calls `mermaid.run({nodes})` once after all blocks are in the DOM.

`bubble-chart` blocks render via D3's `d3.pack()` (circle packing) — same approach as the obren.io reference. The DSL parses just the `nodes:` mapping (any other section is ignored).

`force-graph` blocks render via Vasco Asturiano's `force-graph` library (`https://cdn.jsdelivr.net/npm/force-graph`). The DSL is parsed at build time:

```
nodes:
  A: 10
  B: 4
links:
  A --> B
  A --> C
```

`A: 10` declares node A with size 10. Node names referenced in `links` but not declared get size 1. The block's `content` becomes a JSON string `{nodes:[{id,size}], links:[{source,target}]}` that the client renders directly — keeps client-side logic minimal.

To add a new block type:

1. Add a `(type, opens, closes, transform_or_None)` tuple to `_BLOCK_FENCES` in `build.py` (`opens`/`closes` are tuples of acceptable strings).
2. Add a `<type>: function(block) { … return DOMNode; }` entry to the `renderers` object in `_templates/post.html`.

Do not change the `{ type, content }` envelope — the dispatcher in `post.html` is the seam.

## Front matter

Posts use Jekyll-style front matter. Recognized keys used by the build: `title`, `date`, `author`, `excerpt`, `icon`, `permalink`, `timetoread`. `permalink` becomes the URL slug (`docs/<j>/posts/<permalink>/index.html`); falls back to the file stem if absent. `icon` is looked up under `assets/icons/<name>` of the journal.

## Conventions

- Filenames: `YYYY-MM-DD-slug.md`, placed under `posts/<year>/`.
- Once a post is published, `permalink` should not change (URL stability).
- Image paths in post bodies stay relative to the journal root (`assets/images/...`); the build handles the rewrite.
