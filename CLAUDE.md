# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A multi-journal static-site generator. Each subdirectory under `_journals/` is one journal site (e.g. `_journals/underhood/`). The build emits one site per journal under `docs/<journal-name>/`. There is no framework — just a small Python script, two HTML templates, and inline JS.

## Build

```bash
python3 _wiring/build.py        # builds every journal under _journals/
python3 -m http.server 8000 --directory docs   # local preview
```

The build uses only the Python standard library (no PyYAML, no requirements file). The `venv/` in the repo root is unused by `build.py`.

There is no test suite, lint config, or CI yet.

## Pipeline (data flow)

1. `_wiring/build.py` walks each journal directory.
2. Reads `_journals/<j>/config.yaml` (parsed by a small in-script YAML subset parser — only the shape used by `config.yaml` is supported).
3. For each post listed under a section, parses front matter (`---`-fenced YAML-ish key/value block) and treats the body as markdown.
4. Splits the body into typed **blocks** — see "Block types" below.
5. Embeds the structured data as JSON inside `_templates/index.html` and `_templates/post.html` via `__DATA_JSON__` placeholder substitution; client-side JS does the rendering.
6. Writes output to `docs/<j>/index.html` and `docs/<j>/<slug>.html` (posts sit alongside the index, not under a `posts/` subdir). Journal-level assets are copied wholesale from `_journals/<j>/assets/` to `docs/<j>/assets/`. Per-post `assets/` directories (when posts use the folder layout) are merged into the same destination.

The templates use plain `__PLACEHOLDER__` string substitution (not Jinja). Placeholders in `index.html`: `__TITLE__`, `__DESCRIPTION__`, `__JOURNAL__`, `__LOGO_HTML__`, `__DATA_JSON__`. In `post.html`: `__TITLE__`, `__SECTION_HTML__`, `__BYLINE__`, `__LOGO_HTML__`, `__POST_NAV__`, `__DATA_JSON__`.

## config.yaml shape

```yaml
title: <site title>
description: <site subtitle>
logo: assets/images/<file>      # optional; rendered as a hero image on the index
logo_credit: <optional caption shown under the logo>
sections:
  - title: <section title>
    description: <optional>
    posts:
      - <relative-path>.md     # path relative to _journals/<j>/posts/
```

The `logo` path is journal-relative (resolved against `docs/<j>/`); no rewrite is applied since the index sits at the journal root.

Posts within a section are sorted by **basename** at build time, regardless of yaml order. With the per-post folder layout (`<slug>/index.md`) every post's basename is `index.md`, so Python's stable sort preserves the config order — that is the intended behaviour. Both `.md` and `.markdown` extensions are accepted (the 2023 underhood post still uses `.markdown`).

## Post layout (two conventions, both supported)

The build accepts either layout for a post; pick one per journal and keep it consistent.

1. **Flat file** — `posts/<year>/YYYY-MM-DD-slug.md`. Used by `underhood`. Assets live only at the journal level.
2. **Per-post folder** — `posts/<...>/<slug>/index.md`. Used by `documents`, `decisions-log`, `madr`, `adr-templates`, `ai-dev-strategy`. The folder may contain its own `assets/` directory; on build, it is merged into `docs/<j>/assets/` so post-body `assets/...` references still resolve.

The output URL is driven by the post's `permalink:` front matter, not by the file path — both layouts produce `docs/<j>/<permalink>.html`.

## Asset paths in posts

Posts reference images as `assets/images/...` (Jekyll-style, relative to the journal root). Since posts now live at the journal root (`docs/<j>/<slug>.html`) the build rewrites these to `assets/...` (no path prefix needed). The rewrite (`_ASSET_REF` in `build.py`) covers markdown image/link syntax and raw HTML `src=`/`href=` attributes.

For the per-post folder layout, drop images into `posts/<slug>/assets/images/...`; `_merge_copytree` lifts them into the journal-level assets so the same `assets/images/...` reference resolves at runtime. This is also why `generate_logos.py` writes per-post logos to `posts/<slug>/assets/images/logo.jpeg` and the post then references `logo: assets/images/logo.jpeg`.

## Front matter

Posts use Jekyll-style front matter. Recognized keys used by the build:

| Key | Purpose |
| --- | --- |
| `title` | Post title (also used in nav and `<title>`) |
| `date` | Date string; the byline shows the first 10 chars |
| `author` | Byline author |
| `excerpt` | Index card summary; also the lead paragraph in many posts |
| `permalink` | URL slug; output goes to `docs/<j>/<permalink>.html`. Falls back to file stem if absent. |
| `timetoread` | Byline reading-time string |
| `icon` | Path under the journal (typically `assets/icons/<slug>.png`); shown on the index card |
| `logo` | Optional hero image at the top of the post |
| `logo_credit` | Optional caption shown under the post hero image |
| `tags` | Comma-separated; rendered as chips below the post title |

`permalink` should not change once a post is published (URL stability).

## Client-side rendering

- `index.html` builds the section list from embedded JSON and provides a search input that filters by `title + excerpt` substring (case-insensitive).
- `post.html` contains a small markdown renderer and a `renderers` dispatch table keyed by block type.
- The renderer treats post content as **trusted** and lets raw HTML pass through unescaped — several posts embed inline `<blockquote style="…">` / `<div>` markup. Don't reintroduce a blanket HTML-escape in the inline pass.

### Markdown subset supported by `post.html`

ATX headings (`#`–`######`), paragraphs, blockquotes, fenced code (```), inline code, bold/italic, links, images, unordered/ordered lists, hr, and **GitHub-flavored tables** (header row + `| --- |` separator + body rows). Inline formatting applies inside table cells. The paragraph collector stops at table rows so a table doesn't get swallowed into a `<p>`.

If you need anything fancier, add it to the renderer in `_templates/post.html` rather than pre-rendering on the Python side — the build deliberately keeps the server-side logic minimal.

## Block types

The post payload shape is `{ meta, tags, blocks: [{ type, content }] }`. `split_into_blocks()` in `build.py` walks the post body and lifts recognized custom fences into their own blocks; everything else stays in `markdown` blocks.

Currently recognized fences (declared in `_BLOCK_FENCES`):

| Type | Open | Close | Build-side transform |
| --- | --- | --- | --- |
| `mermaid` | `---begin mermaid---` | `---end mermaid---` | none (raw diagram source) |
| `force-graph` | `---begin force-graph---` | `---end force-graph---` | `_parse_force_graph` → JSON `{nodes, links}` |
| `bubble-chart` | `---begin bubble-chart---` (also `buble-chart`) | `---end bubble-chart---` (also `buble-chart`) | `_parse_bubble_chart` → JSON `{nodes:[{name,size}]}` |
| `wardley-map` | `---begin wardley-map---` | `---end wardley-map---` | none (raw `<wardley-map>` HTML, rendered by the upstream web component) |

Open and close strings are each tuples in `_BLOCK_FENCES` so a fence can accept multiple spellings (the bubble-chart entry tolerates both `bubble-chart` and the typo `buble-chart` on either side).

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

`A: 10` declares node A with size 10. Node names referenced in `links` but not declared get size 1. The block's `content` becomes a JSON string `{nodes:[{id,size}], links:[{source,target}]}` that the client renders directly.

`wardley-map` blocks pass through unchanged; the upstream `<wardley-map>` web component (https://github.com/jamesaduncan/Wardley-map) renders them client-side.

To add a new block type:

1. Add a `(type, opens, closes, transform_or_None)` tuple to `_BLOCK_FENCES` in `build.py` (`opens`/`closes` are tuples of acceptable strings).
2. Add a `<type>: function(block) { … return DOMNode; }` entry to the `renderers` object in `_templates/post.html`.

Do not change the `{ type, content }` envelope — the dispatcher in `post.html` is the seam.

## Auxiliary scripts in `_wiring/`

Two opt-in helpers sit alongside `build.py`. They share the same standard-library-only constraint and reuse `build.py`'s `parse_yaml`.

- `generate_icons.py` — calls Google Gemini to generate a per-post icon image. Run with `GEMINI_API_KEY=... python3 _wiring/generate_icons.py --journal <name>`. For each post in the journal's `config.yaml` that has no `icon:` field, it builds a short prompt from title + excerpt, writes `_journals/<j>/assets/icons/<slug>.png`, and rewrites the post's front matter to add `icon: assets/icons/<slug>.png`.
- `generate_logos.py` — same shape, for per-post hero images. Writes `_journals/<j>/posts/<slug>/assets/images/logo.jpeg` (per-post folder layout assumed) and adds `logo:` and `logo_credit:` to the front matter.

Both scripts are idempotent: if the front-matter field is already set, the post is skipped.

## Conventions

- Filenames: `YYYY-MM-DD-slug.md` for the flat layout; `<slug>/index.md` for the folder layout. Pick one per journal.
- Once a post is published, `permalink` should not change (URL stability).
- Image paths in post bodies stay relative to the journal root (`assets/images/...`); the build handles the rewrite, including the per-post-folder merge.
- Engineering standards travel with the journal: each journal can have its own `CLAUDE.md`-style conventions in its own README, but the build behaviour above is constant across all of them.
