# Wiring

`_wiring/` contains the scripts that turn journal source files into generated
static output. The core scripts use only the Python standard library.

## Main Build

```bash
python3 _wiring/build.py
```

`build.py`:

1. Scans every child directory under `_journals/`.
2. Skips directories without `config.yaml`.
3. Parses the small YAML subset used by journal configs.
4. Parses post front matter and Markdown bodies.
5. Rewrites `assets/...` references and `[[permalink]]` cross-links.
6. Splits custom fenced content into typed blocks.
7. Renders `docs/<journal>/index.html`, post pages, optional spec pages, assets,
   and `site.css`.

The script deletes and recreates each generated `docs/<journal>/` directory.
It does not generate the start page.

## Start Page

The start page has its own generator in `_start/`:

```bash
python3 _start/generate-docs.py
```

Run it when `_start/_config/apps.json`, `_start/_templates/index.html`, or
start-page icon assets change.

## Content Helpers

```bash
GEMINI_API_KEY=... python3 _wiring/generate_icons.py --journal <journal>
GEMINI_API_KEY=... python3 _wiring/generate_logos.py --journal <journal>
```

These scripts call Google Gemini to create missing per-post icons or hero
images. They are idempotent around existing files and front-matter fields.
They require network access and a valid `GEMINI_API_KEY`.

## Spec Helpers

`spec-template.md` is the canonical template for per-post specs. Specs sit next
to `index.md`, are versioned in git, and are rendered by `build.py` when
present.

The leading-underscore scripts are one-off migration helpers:

| Script | Purpose |
| --- | --- |
| `_backfill_specs.py` | Creates stub `spec.md` files for selected journals. |
| `_backfill_status_flip.py` | Updates front-matter and visible highlight status to draft values. |

Treat these as maintenance scripts, not routine authoring commands.

## Build Contracts

The templates expect the post payload shape to remain:

```json
{
  "meta": {},
  "tags": [],
  "blocks": [
    {"type": "markdown", "content": "..."}
  ]
}
```

When adding a custom block type:

1. Add the fence tuple to `_BLOCK_FENCES` in `build.py`.
2. Add any build-side parser needed for the block.
3. Add a matching renderer function in `_templates/post.html`.
4. Rebuild all journals.

Do not change the `{type, content}` envelope unless you also update the
template renderer.

## Validation

There is no test suite yet. For now, validate changes with:

```bash
python3 -m py_compile _wiring/build.py _wiring/generate_icons.py _wiring/generate_logos.py _start/generate-docs.py
python3 _wiring/build.py
python3 _start/generate-docs.py
python3 -m http.server 8000 --directory docs
```

Then inspect the affected pages in a browser.
