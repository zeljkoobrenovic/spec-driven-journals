---
timetoread: 2 min
---

Spec-Driven Journals is intentionally small but not frozen: new journals, templates, block types, and start-page entries are all expected. The way to evolve it safely is to preserve a small set of build contracts, keep source separate from generated output, prefer the smallest change that solves the problem, and verify with scoped builds and rendered-page inspection.

**What changes**

- Maintenance gets an explicit contract list that should remain stable: `config.yaml` defines journal order, posts are front matter plus markdown, non-trivial posts carry sibling specs, modality files are discovered by presence, generated pages live under `docs/`, cross-links use double-bracket permalink syntax, blocks keep the `{type, content}` envelope, and the core build stays standard-library Python.
- Adding a journal becomes a known seven-step recipe — folder, `config.yaml`, posts, specs, sections, build, start page — instead of guesswork. The journal build and start-page build are deliberately separate: a journal can generate under `docs/<journal>/` and stay undiscoverable until `_start/_config/apps.json` is updated, which lets maintainers draft before promoting.
- A lowest-impact decision table pairs each need with the smallest change: a new article collection means a new journal folder, not template work; a repeated visual language means a documented custom block type after several real examples, not raw HTML copied across posts; a rendering fix means changing source or build logic, never hand-editing `docs/`.
- Template and build extensions get gating questions — journal-specific or global, does it preserve the JSON payload contract and raw-HTML behavior — and custom block types follow a fixed pattern: fence tuple, optional parser, renderer function, documented syntax.
- Verification becomes a habit: `py_compile` the scripts, run the full builds or a scoped single-journal build, then inspect generated index, post, and spec pages, copied assets, and unresolved double-bracket links.

**What it costs**

- Permalinks (and the two public entry points — the GitHub repository and the generated site) are commitments: titles can change freely, but changing a published `permalink` breaks links, and the cost grows with every citation.
- Agent-facing instructions (`AGENTS.md`, `CLAUDE.md`, READMEs) must be updated whenever build behavior changes — otherwise future agents follow stale rules and produce reasonable-looking wrong work. Implementation, human docs, and agent instructions must stay aligned.

**What we are not doing**

- No full release process and no CI/CD design — verification stays scoped builds plus inspection for now.
- No visual redesign plan; avoid dependencies, framework abstractions, one-post content formats, and styling systems that make the system harder to inspect.

The Article tab has the full contract table, the step-by-step recipes, and the verification commands.
