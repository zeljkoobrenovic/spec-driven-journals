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
6. Writes output to `docs/<j>/index.html` and `docs/<j>/posts/<slug>/index.html`. Assets are copied wholesale from `_journals/<j>/assets/` to `docs/<j>/assets/`.

The templates use plain `__PLACEHOLDER__` string substitution (not Jinja). Placeholders: `__TITLE__`, `__DESCRIPTION__`, `__JOURNAL__`, `__BYLINE__`, `__DATA_JSON__`.

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

Posts reference images as `assets/images/...` (Jekyll-style, relative to the journal root). The build rewrites these to `../../assets/...` so they resolve from the post's deeper output location (`docs/<j>/posts/<slug>/index.html`). The rewrite (`_ASSET_REF` in `build.py`) covers markdown image/link syntax and raw HTML `src=`/`href=` attributes.

## Client-side rendering

- `index.html` builds the section list from embedded JSON and provides a search input that filters by `title + excerpt` substring (case-insensitive).
- `post.html` contains a small markdown renderer (subset: ATX headings, paragraphs, blockquotes, fenced code, inline code, bold/italic, links, images, lists, hr) and a `renderers` dispatch table keyed by block type.
- The renderer treats post content as **trusted** and lets raw HTML pass through unescaped — several posts embed inline `<blockquote style="…">` / `<div>` markup. Don't reintroduce a blanket HTML-escape in the inline pass.

## Extending blocks (forward-looking)

The post payload shape is `{ meta, blocks: [{ type, content, ...}] }`. Today every post produces a single `{ type: "markdown", content: "<full body>" }`. To add new block kinds (e.g. mermaid):

1. In `build.py`, expand `split_into_blocks()` to recognize a fence (e.g. ` ```mermaid ` … ` ``` `) and emit a separate `{ type: "mermaid", content: "<diagram src>" }` block alongside the surrounding markdown blocks.
2. In `_templates/post.html`, add an entry to the `renderers` object: `mermaid: function(block) { … return DOMNode; }`.

Do not change the `{ type, content }` envelope — the dispatcher in `post.html` is the seam.

## Front matter

Posts use Jekyll-style front matter. Recognized keys used by the build: `title`, `date`, `author`, `excerpt`, `icon`, `permalink`, `timetoread`. `permalink` becomes the URL slug (`docs/<j>/posts/<permalink>/index.html`); falls back to the file stem if absent. `icon` is looked up under `assets/icons/<name>` of the journal.

## Conventions

- Filenames: `YYYY-MM-DD-slug.md`, placed under `posts/<year>/`.
- Once a post is published, `permalink` should not change (URL stability).
- Image paths in post bodies stay relative to the journal root (`assets/images/...`); the build handles the rewrite.
