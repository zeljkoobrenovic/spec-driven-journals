---
timetoread: 2 min
---

A journal is a small source tree: one `config.yaml`, a `posts/` folder, optional assets, and per-post folders that keep the article, its spec, and its media together. Anyone who understands that shape can add or inspect a journal without reading the generator first.

The contract is simple. A directory under `_journals/` with a `config.yaml` is a journal; without one, the build skips it. The config is the table of contents — title, description, and sections listing post paths relative to `posts/`. The YAML order is the reading order. Output goes to `docs/<journal>/`, which is removed and recreated on every build of that journal: source lives in the [Spec-Driven Journals](https://github.com/zeljkoobrenovic/spec-driven-journals) repository, the generated site is only the reading surface.

**What changes**

- Each post is a folder, `posts/<slug>/`, holding `index.md` (the required article), an optional sibling `spec.md`, optional modality docs (`summary.md`, `dialog.md`, `comics.md`), and its own `assets/`. Everything an article needs travels together.
- Front matter drives the generated page: `permalink` fixes the output URL (`docs/<journal>/<permalink>.html`); `title` feeds pages, index cards, browser titles, and cross-link text; `excerpt`, `tags`, `icon`, and `logo` shape the index card and post header. Published permalinks do not change — retitling is normal, moving URLs is not.
- When `spec.md` exists, it renders at `<permalink>.spec.html` and the post byline gets a "View spec" link. Specs are working documents with a predictable body — Intent, Audience, Success criteria, Non-goals, Modalities, Open questions, Decision log, Sources, Changelog — whose job is to make intent visible before the article text hardens.
- Modality files become tabs on the same post page (Article · Summary · Conversation · Comic), discovered by file presence with no config changes, deep-linkable via `#summary`, `#dialog`, `#comics`. The article stays the default tab and the URL stays stable.
- Per-post `assets/` merge into the journal-level `assets/` at build time, so body content uses plain `assets/images/...` paths regardless of where the file lives in source.

**What it costs**

- A new post is several deliberate steps, not one file: folder, front matter with a stable permalink, a spec for anything non-trivial, a config entry, and a build check that the page, spec link, and tabs all appear.
- The generated `docs/` tree is disposable, so it can never be hand-edited — every fix has to land in `_journals/` source.

**What we are not doing**

- No exhaustive Markdown syntax reference — content mechanics follow in [[cross-links-assets-and-blocks]].
- No implementation tour of `build.py`, and no visual design documentation.

The Article tab covers the folder layouts, the front matter field table, and the full wiring checklist for adding a post.
