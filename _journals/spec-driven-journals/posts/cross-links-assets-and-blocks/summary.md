---
timetoread: 2 min
---

Spec-driven journals stay navigable through four content mechanisms layered on plain markdown: stable cross-record links, simple asset-path conventions, generated clickable images, and a small set of custom block fences for diagrams and visualizations. Authors write simple source; the build and the browser-side renderer do the rest — and the same mechanics apply to every modality file in a post folder, not only `index.md`.

**What changes**

- Posts link to other records with double-bracket permalink references. The build resolves each one to a normal link using the target's `title:` — same-journal targets become `target.html`, cross-journal targets become `../other-journal/target.html`, and unresolved references stay visible as literal tokens, turning broken links into authoring TODOs instead of silent failures.
- Links key off `permalink`, not file path or title. Permalinks never change after publication, so titles can be reworded freely and every page that links to a record picks up the new wording on the next build.
- Asset paths in post bodies stay relative to the journal root (`assets/images/...`). Per-post assets live next to the post source and are merged into the generated journal assets at build time, so the same reference resolves on the rendered page.
- Markdown images render wrapped in links to their own files, so readers can open any diagram, screenshot, or generated illustration full-size in a new tab. Hero images defined through `logo:` get the same treatment.
- Four custom block fences — `mermaid`, `force-graph`, `bubble-chart`, `wardley-map` — are lifted out of markdown into typed `{type, content}` blocks and rendered client-side. Extending the set means touching exactly three places: `_BLOCK_FENCES` in `_wiring/build.py`, an optional build-side parser, and a renderer entry in `_templates/post.html`.

**What it costs**

- The markdown renderer is deliberately small — the subset the journals actually use. Richer markdown means a deliberate update to `_templates/post.html`, not ad hoc generated HTML.
- The `{type, content}` envelope is a renderer contract. Changing it changes the seam between build and template, so it must be an intentional decision, not a side effect.
- Custom blocks demand restraint: they should support the argument, not become a second undocumented language inside the post.

**What we are not doing**

- Not a full Markdown syntax reference.
- Not a D3, Mermaid, force-graph, or Wardley-map tutorial.
- Not an accessibility policy for all media — though meaningful alt text remains a stated authoring habit.

The Article tab covers the full syntax, the rendering map, and the step-by-step recipe for adding a new block type. Read [[anatomy-of-a-journal]] first; [[spec-driven-authoring-workflow]] comes next.
