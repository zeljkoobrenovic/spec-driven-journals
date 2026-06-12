---
timetoread: 8 min listen
---

## Why care about a build script?

**Ben:** Ana, this one's an article about a build script. Static-site generators are a solved problem — Jekyll, Hugo, Eleventy, pick one. Why should anyone spend nine minutes reading about a homemade Python script?

**Ana:** Because the post isn't pitching the script as a better generator — it says outright that it does not try to be a general static-site framework. It reads a narrow source shape, writes predictable HTML files, and lets shared templates handle browser-side rendering. The article exists so that anyone changing the build or templates — maintainer, agent operator, technical reader — understands the contracts before touching the code. It's deliberately a set of contracts, not a line-by-line walkthrough.

**Ben:** "Contracts" is doing a lot of work in that sentence. What does the pipeline actually do?

**Ana:** Twelve steps, and they fit in a breath. Walk `_journals/`. Skip directories without a `config.yaml`. Parse each journal config. Read the posts listed in each section. Parse front matter and the markdown body. Collect sibling modality files — `summary.md`, `dialog.md`, `comics.md` — when they exist. Rewrite asset paths in every modality body. Resolve the double-bracket permalink cross-links. Split custom fenced blocks out of the markdown. Merge per-post assets into the journal's generated assets. Render post pages with their modality tabs, spec pages, and the journal index. Write everything under `docs/<journal>/`. When it works, you get one line: `[built] spec-driven-journals -> docs/spec-driven-journals`.

**Ben:** And that `docs/` folder is...?

**Ana:** Exactly what gets published. The generated output is the public Spec-Driven Journals site; the source and the generator live in the repository. What you build locally is what readers see — there's no separate deployment transform.

## A YAML parser you wrote yourself? Really?

**Ben:** I noticed the script parses its own YAML. That's usually where I close the tab. PyYAML is one `pip install` away.

**Ana:** And the post treats skipping it as a deliberate tradeoff, not an oversight. The in-script parser supports exactly the shape `config.yaml` uses — scalar key/value pairs, lists of strings, lists of mappings, quoted strings. That's enough. The win is fewer dependencies, less install friction, and a smaller contract. The build runs anywhere Python 3 runs.

**Ben:** Until someone needs an anchor, or a multi-line string, or any of the YAML features actual YAML has.

**Ana:** The article names that implication explicitly: if a future journal needs advanced YAML features, either avoid them or improve the parser deliberately. The constraint is visible and documented, which is the whole point of writing the implementation up at contract level — you learn where the edges are before you hit them.

## Posts become payloads

**Ben:** Okay, the part I actually want to understand: what does a post turn into?

**Ana:** A JSON payload with three top-level pieces: `meta`, `tags`, and `modalities`. The `meta` object comes from front matter. `tags` is parsed from the comma-separated `tags:` field. And `modalities` is a list — one entry per doc the post ships. Each entry has a `key`, a `label`, its own `meta`, and a list of `blocks`.

**Ben:** Modalities being what, exactly?

**Ana:** The article, plus any sibling docs next to it. `index.md` is always there with key `index` and label "Article". If the post folder also has a `summary.md`, a `dialog.md`, or a `comics.md`, each becomes another modality entry — the registry is `_MODALITIES` in `build.py`, and the list order is the tab order. Inside each modality, `blocks` is markdown plus whatever custom block types the build extracted — Mermaid diagrams, force graphs, bubble charts.

**Ben:** So every post page is secretly a tabbed application now? That sounds like scope creep for a "deliberately modest" generator.

**Ana:** Here's the elegant bit: a plain post has exactly one modality, and the renderer shows no tab bar at all. The page looks like a single-article page. Only when there's more than one modality does the tab bar appear — the article is the default tab, and the URL hash deep-links the others: `#summary`, `#dialog`, `#comics`. One code path covers both cases.

**Ben:** And this payload lives where?

**Ana:** Embedded in the generated HTML, inside a `<script id="data" type="application/json">` element. The browser-side renderer reads that JSON and builds the page.

**Ben:** Which brings me to my real objection. Rendering markdown in the browser, in 2026? Every other generator pre-renders to HTML. You're shipping a markdown parser to every reader.

**Ana:** That's the split the post defends. The Python side handles filesystem and source concerns — read files, parse config, rewrite asset paths, resolve cross-links, copy assets, emit HTML. The browser side handles presentation — render markdown, tags, modality tabs, initialize Mermaid, render force graphs and bubble charts, dispatch custom block renderers. The result is that the build script stays small and every renderer change is visible in one template, `_templates/post.html`. You don't coordinate changes across a Python markdown library and a JavaScript diagram library; presentation lives in one place.

**Ben:** Fine, but then explain "lazy" tab rendering. Why not render all tabs up front since the data's already on the page?

**Ana:** Because of a concrete browser fact the article calls out: lazy pane rendering is not an optimization detail. Mermaid, force-graph, and D3 all measure their container's width — and inside a hidden element, that width is zero. Render a diagram into a hidden tab and you get a zero-width diagram. So non-default panes render on first activation, after they're visible. It's a correctness requirement dressed up as a performance feature.

## Templates, specs, and the rest of the machine

**Ben:** The templates. No Jinja, no React — just `__TITLE__`-style placeholders that get string-substituted. A misspelled placeholder just... silently ships?

**Ana:** Yes, and the article is honest about that cost: there's no template engine to catch it, so template changes should be made carefully. The compensating benefit is that the Python side stays trivially easy to inspect — `index.html` takes `__TITLE__`, `__DESCRIPTION__`, `__JOURNAL__`, `__LOGO_HTML__`, `__DATA_JSON__`; `post.html` takes `__TITLE__`, `__SECTION_HTML__`, `__BYLINE__`, `__LOGO_HTML__`, `__POST_NAV__`, `__DATA_JSON__`. That's the entire templating contract, in one table.

**Ben:** What about specs? This whole project is named after them.

**Ana:** When a post folder has a `spec.md`, the build renders a sibling page — `<permalink>.spec.html` — and the post's byline gets a "View spec" link. Same template, same markdown renderer, same cross-link logic as posts. Internally, the spec payload is just a single-modality payload, which is why spec pages never show a tab bar — again, one code path. The spec's front matter drives a status chip, and if a spec is marked `drifted` or `superseded`, the post's spec link is decorated so readers see the contract may no longer match the article.

**Ben:** And navigation between posts?

**Ana:** Comes from config order. The build flattens the post order in `config.yaml` into previous/next navigation. That's also why the per-post folder layout matters: every listed path ends in `index.md`, so sorting by basename doesn't disturb config order. The config file *is* the reading sequence.

**Ben:** One more skeptical poke. The renderer lets raw HTML pass through unescaped. That's an XSS hole with documentation.

**Ana:** It's a trust assumption, stated as one. The renderer treats post content as trusted because some posts embed custom HTML, and the article flags the boundary explicitly: Spec-Driven Journals is not currently designed for untrusted public user submissions. Authors are the threat model's insiders, and they're the same people running the build.

## What this article is not

**Ben:** Close it out. If I change `build.py` tomorrow, what's the one thing I must not break?

**Ana:** The block envelope: `{"type": ..., "content": ...}`. Every block in every modality wears it, and the dispatcher in `post.html` expects it. New block types are welcome — add a fence on the Python side, a renderer entry on the template side — but changing the envelope means coordinated changes in both files. And note the layering: the modality layer wraps *above* the envelope, so adding a whole new modality never touches the block contract. The system stays easy to extend only if extensions keep that contract clear.

**Ben:** And what did the article deliberately not do?

**Ana:** Three named non-goals. It's not a line-by-line walkthrough of `build.py` — the helpers aren't the point, the contracts are. It's not a reimplementation guide for the renderer. And it's not a browser-side JavaScript tutorial. If you want the source layout that feeds this pipeline, that's [[anatomy-of-a-journal]]; this article is about what the system does with that source once you hit build.

**Ben:** A build script small enough to explain in a podcast. *(laughs)* Maybe that's the actual feature.

**Ana:** The post would agree. It's easy to extend because the contract is small — and the article exists to keep it that way.
