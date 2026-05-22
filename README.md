# Spec-Driven Journals

This repository publishes Organization's durable technical writing as a set of
small static journal sites. Source content lives under `_journals/`, the build
writes static HTML under `docs/`, and the start page links the journals
together from `docs/start/index.html`.

There is no application framework and no dependency install step for the core
build. The site generator is a small Python standard-library script, HTML
templates, CSS, and client-side JavaScript.

See generated examples journals here: [zeljkoobrenovic.github.io/spec-driven-journals](https://zeljkoobrenovic.github.io/spec-driven-journals/)

## Quick Start

Build the journals and the start page:

```bash
python3 _wiring/build.py
python3 _start/generate-docs.py
```

Preview the generated site locally:

```bash
python3 -m http.server 8000 --directory docs
```

Then open `http://localhost:8000/`. The root page redirects to
`/start/index.html`.

## Current Journals

| Journal | Source | Output | Purpose |
| --- | --- | --- | --- |
| Foundations | `_journals/foundations/` | `docs/foundations/` | Foundational engineering decisions, rituals, forums, and shared conventions. |
| Tech Decisions Log | `_journals/tech-decisions-log/` | `docs/tech-decisions-log/` | Strategic technical decisions for frontend, backend, and infrastructure. |
| AI Decisions Log | `_journals/ai-decisions-log/` | `docs/ai-decisions-log/` | Strategic decisions about AI tooling, policy, operating model, and standards. |
| Org Design | `_journals/org-design/` | `docs/org-design/` | Organisation-design decisions for engineering teams, governance, talent, and flow. |
| Tech Strategy | `_journals/tech-strategy/` | `docs/tech-strategy/` | The engineering strategy narrative, policy, roadmap, and convergence plans. |
| Engineering Principles | `_journals/principles/` | `docs/principles/` | Durable engineering principles used to guide technical decisions and daily practice. |
| AI Development Strategy | `_journals/ai-dev-strategy/` | `docs/ai-dev-strategy/` | The 2026 AI-assisted development strategy, governance, workflows, and review material. |

## Repository Map

| Path | Role |
| --- | --- |
| `_journals/` | Source content. Each child directory with a `config.yaml` is one generated journal site. |
| `_wiring/` | Build and maintenance scripts. `build.py` is the main journal generator. |
| `_templates/` | Shared HTML templates and CSS used by the journal generator. |
| `_start/` | Source for the start page that links all journals together. |
| `docs/` | Generated publication output. Commit it when source changes are meant to be published. |
| `AGENTS.md`, `CLAUDE.md` | Agent-facing operating instructions. Keep them aligned with the build behavior when changing conventions. |

## How Publishing Works

`_wiring/build.py` scans every directory under `_journals/`. If a directory has
a `config.yaml`, it is built into `docs/<journal>/`; if it does not, it is
skipped. Each listed post is parsed from Markdown with front matter, split into
typed blocks, embedded as JSON into the templates, and rendered by browser-side
JavaScript.

The build also copies journal assets and per-post assets into the generated
journal's `assets/` directory. Post pages are written at the journal root, for
example `docs/principles/small-and-simple.html`.

The start page is generated separately by `_start/generate-docs.py`, using
`_start/_config/apps.json` and `_start/_templates/index.html`.

## Editing Workflow

For content changes, edit the source under `_journals/<journal>/posts/...`.
Most current posts use the per-post folder layout:

```text
_journals/<journal>/posts/<optional-section>/<slug>/
  index.md
  spec.md
  assets/
```

For non-trivial posts, update `spec.md` before changing the published
`index.md`. The spec is the working contract; the post is the published
artifact. The build renders specs as `<slug>.spec.html` and adds a "View spec"
link when a sibling `spec.md` exists.

After edits:

```bash
python3 _wiring/build.py
python3 _start/generate-docs.py
git status --short
```

## Common Tasks

Add a post:

1. Create `_journals/<journal>/posts/<slug>/index.md`.
2. Add an optional sibling `spec.md` using `_wiring/spec-template.md`.
3. Add the post path to the relevant section in `_journals/<journal>/config.yaml`.
4. Run `python3 _wiring/build.py`.
5. Check the generated page under `docs/<journal>/<permalink>.html`.

Add a journal:

1. Create `_journals/<journal>/config.yaml`, `posts/`, and optional `assets/`.
2. Add posts to `config.yaml`.
3. Run `python3 _wiring/build.py`.
4. Add the generated journal to `_start/_config/apps.json`.
5. Run `python3 _start/generate-docs.py`.

Change rendering:

1. Update `_templates/index.html`, `_templates/post.html`, or `_templates/site.css`.
2. If adding a custom block type, update both `_wiring/build.py` and the
   renderer dispatch table in `_templates/post.html`.
3. Rebuild all journals with `python3 _wiring/build.py`.

## Constraints

- The core build is standard-library Python only.
- `permalink:` values are stable URLs. Do not change them after publication
  unless you deliberately accept broken links.
- Cross-record links use `[[permalink]]`; unresolved links are left visible in
  the rendered content as authoring TODOs.
- Generated HTML in `docs/` should be rebuilt from source rather than edited
  directly.
- Substantive authoring work in this repository is AI-mediated by convention:
  the human describes intent, the agent edits, and the human reviews the diff.
