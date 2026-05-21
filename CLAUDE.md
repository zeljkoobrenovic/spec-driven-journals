# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A multi-journal static-site generator that publishes Organization's durable technical writing. Each subdirectory under `_journals/` is one journal site (e.g. `_journals/principles/`). The build emits one site per journal under `docs/<journal-name>/`. There is no framework — just a small Python script, two HTML templates, and inline JS.

### Current journals

| Journal | Purpose | Layout |
| --- | --- | --- |
| `tech-decisions-log` | Strategic tech ADRs (cloud, backend, mobile, web, messaging, networking, compute). | Per-post folder |
| `ai-decisions-log` | Strategic AI/Claude Code ADRs (tooling, policy, operating model, engineering standards). | Per-post folder |
| `ai-dev-strategy` | The 2026 AI development strategy, framing, workflows, governance, reviews. | Per-post folder |
| `foundations` | Foundational engineering decisions and rituals (e.g. markdown records, Architecture Advisory Forum, AI-mediated authoring). | Per-post folder |
| `principles` | Durable engineering principles, grouped into Design / Operational / Organisation / Practices. | Per-post folder |

A successful build prints one `[built] <journal> -> docs/<journal>` line per journal — six today. Directories under `_journals/` without a `config.yaml` are skipped with a `[skip] <name>: no config.yaml` line rather than failing the build, so empty placeholder directories (e.g. an in-progress `tech-strategy/`) are safe to leave in place.

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

1. **Flat file** — `posts/<year>/YYYY-MM-DD-slug.md`. Assets live only at the journal level. (Historical layout; none of the current journals use it.)
2. **Per-post folder** — `posts/<...>/<slug>/index.md`. Used by every current journal (`tech-decisions-log`, `ai-decisions-log`, `ai-dev-strategy`, `foundations`, `principles`). The folder may contain its own `assets/` directory; on build, it is merged into `docs/<j>/assets/` so post-body `assets/...` references still resolve.

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

Editorial fields that are not consumed by the build but are conventional for ADR-shaped posts (`tech-decisions-log`, `ai-decisions-log`, `foundations`, `principles`):

| Key | Purpose |
| --- | --- |
| `id` | Stable record identifier, e.g. `ORG-PRIN-SMALL-AND-SIMPLE`. Doesn't change when the title is reworded. |
| `status` | `proposed:orange`, `accepted:green`, `deprecated:gray`, `superseded:gray`, etc. Convention is `<state>:<colour>`. |

These survive in the front matter and the JSON payload, and may be used by future renderers; they are not currently rendered by the templates.

`permalink` should not change once a post is published (URL stability). Same for `id` — rewrite the title freely, but keep the identifier stable.

### ADR-shaped opening highlight

Foundation-, decision-, and principle-shaped posts open with a fixed two-line highlight blockquote before the first `## Heading`:

```markdown
> **Status**: PROPOSED
>
> **Decision**: One paragraph stating the decision clearly enough that a reader gets the direction before reading the body.
```

For principle posts, replace `**Decision**` with `**Principle**`. Keep it short, keep the labels exact, and align the visible status with the front-matter `status:` value. The main body should start with `## Statement` (principles) or `## Decision` (decisions); the highlight is the scannable summary, not a duplicate of that section.

### Cross-record links: `[[name]]`

Posts link to other records with `[[record-name]]`, where `record-name` is the target post's `permalink:`. The build resolves these at compile time (`build_crosslink_index` + `_rewrite_crosslinks` in `build.py`):

- **In-journal target** (`[[evolutionary-systems]]` from another post in `principles/`) → `[Design Principle: Evolutionary Systems](evolutionary-systems.html)`.
- **Cross-journal target** (`[[ai-policy]]` from a `principles/` post, where `ai-policy` lives in `ai-decisions-log/`) → `[AI Coding Policy: ...](../ai-decisions-log/ai-policy.html)`.
- **Unresolved slug** → passed through as literal `[[slug]]` so it stays visible as an authoring TODO.

Link text uses the target's `title:` from front matter, so reworking a title automatically updates every page that links to it. The `permalink:` is what `[[…]]` keys off, which is one of the reasons `permalink` should never change once published.

Link liberally — a `[[name]]` whose target doesn't exist yet survives the build (as literal text) and marks a record worth writing later.

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

- Filenames: `YYYY-MM-DD-slug.md` for the flat layout; `<slug>/index.md` for the folder layout. Pick one per journal — current journals all use the folder layout.
- Once a post is published, `permalink` should not change (URL stability). Same goes for `id` if the post has one.
- Image paths in post bodies stay relative to the journal root (`assets/images/...`); the build handles the rewrite, including the per-post-folder merge.
- Engineering standards travel with the journal: each journal can have its own `CLAUDE.md`-style conventions in its own README, but the build behaviour above is constant across all of them.

### AI-mediated authoring (default workflow)

Substantive changes to this repository — new posts, edits, restructures, illustrations, config and template changes — go through an AI coding agent (Claude Code, Codex CLI, or an equivalent CLI tool) rather than being hand-edited. The author describes intent; the agent edits; the author reviews the diff. See the foundation ADR at `_journals/foundations/posts/ai-mediated-authoring/index.md` for the full rationale and exception list.

### Spec-driven authoring (per-post specs)

Non-trivial posts are driven by a lightweight spec — a `spec.md` file sitting next to `index.md` in the same post folder. The spec is the contract the agent works against; `index.md` is the published artifact.

- **Template**: `_wiring/spec-template.md`. Seven sections: Intent, Audience, Success criteria, Non-goals, Open questions, Decision log, Sources — plus a trailing Changelog. Keep each section short; trim ruthlessly if the spec grows longer than the post.
- **Layout**: `_journals/<journal>/posts/<slug>/spec.md`. Only the per-post folder layout supports specs (every current journal uses that layout).
- **Build behaviour**: when `spec.md` exists, the build renders it as `docs/<journal>/<slug>.spec.html` and adds a "View spec" link to the post's byline. Specs use the same markdown renderer as posts and support the same `[[…]]` cross-links.
- **When to write one**: any post where the intent is not self-evident from the title — new foundations, principles, decisions, and strategy posts. Skip for trivial fixes, status flips, and minor edits. If you can't articulate Intent + Success criteria in a paragraph each, the post probably is not ready to write yet.
- **Lifecycle**: the spec is the working doc for the *first* version of a post. Update it when the post's intent shifts; leave Open questions until they are answered or moved to a follow-up record. Specs are versioned in git like everything else.
- **Tracking evolution**: specs have a small front-matter block (`status:` + `revised:`) and a trailing `## Changelog` section. Status values are `draft` (still being written), `accepted` (spec and post agree), `drifted` (post has moved beyond the spec — needs reconciliation), `superseded` (a replacement spec exists). The build renders the status as a chip on the spec page and decorates the "View spec" link on the post page when the spec is `drifted` (amber) or `superseded` (muted). When you change a spec or notice drift, update `revised:` and add a Changelog line.
- **Edit the spec first**: when intent for a post shifts, update the spec *before* the post. If you find yourself updating the post first, that's a signal the spec is being treated as documentation, not as a contract.
- **Foundation ADR**: see `_journals/foundations/posts/spec-driven-authoring/index.md` for the durable rationale.

### House style for new posts

When adding to `tech-decisions-log`, `ai-decisions-log`, `foundations`, or `principles`, follow the established record shape so the journal stays internally consistent:

- Open with the **Status / Decision (or Principle)** highlight blockquote.
- Use a MADR-inspired body: `Statement` or `Decision` → `How to Read This` → `Rationale` → `Implications` → `What This Means for Teams` → `Anti-Patterns` → `Examples` → `Related Principles` / cross-links → `Scope and Revisiting` → `Authoritative References`. Sections may be omitted, but the order is conventional.
- Lean on tables of contrasts ("What it says / What it does **not** say") and grouped bullets — they read well in the rendered HTML.
- Cross-link related records with `[[name]]` rather than ad-hoc text references.
- Keep tone declarative; the records are written to be read by humans and by AI tools as context.

### Wiring a new post

To add a new post to an existing journal:

1. Create `_journals/<journal>/posts/<slug>/index.md` with the front matter and body.
2. Add `      - <slug>/index.md` to the appropriate section under `posts:` in `_journals/<journal>/config.yaml`. Order in the file is preserved (basename sort is a no-op for the folder layout).
3. Run `python3 _wiring/build.py` and confirm `[built] <journal> -> docs/<journal>` and `docs/<journal>/<permalink>.html` appear.
4. Optionally run `generate_icons.py` / `generate_logos.py` (with `GEMINI_API_KEY`) to fill in the visual front-matter fields.
