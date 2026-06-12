---
timetoread: 8 min listen
---

## Why care about maintaining a tiny system?

**Ben:** Ana, this is a small Python script, two HTML templates, and some markdown. Why does it need a whole article about "extending and maintaining the system"? What is there to maintain?

**Ana:** That smallness is exactly what's at risk. Spec-Driven Journals is intentionally small, but it is not frozen — new journals get added, templates change, the renderer grows block types, the start page publishes new entries, helper scripts evolve. The maintenance challenge the post names is to extend the system without turning it into a hidden framework that authors and AI agents can no longer reason about. Nobody sets out to build a hidden framework. You get one by making twenty individually reasonable changes without a rule for which changes are cheap and which are expensive.

**Ben:** And the rule is?

**Ana:** Preserve a short list of contracts, and for everything else, pick the smallest source change that solves the problem. There are also two public entry points that maintenance has to keep coherent — the official repository on GitHub and the generated journal site on GitHub Pages. Whatever you change, both of those should keep making sense.

## The contracts that should not move

**Ben:** Okay, what's on the contract list? Because "don't break things" is not actionable.

**Ana:** It's a concrete table in the article, eight rows. `config.yaml` in each journal defines journal order, so authors can inspect the table of contents in one file. Posts are front matter plus a markdown body, so metadata and prose stay together. Non-trivial posts have sibling specs, so intent stays visible across sessions. Modality files — `summary.md`, `dialog.md`, `comics.md` — are discovered by presence, so one spec can drive several docs without config changes. Generated pages live under `docs/`, keeping publication output separate from source. Cross-links use the double-bracket permalink syntax, so links survive title changes. Blocks keep the `{type, content}` envelope, so new renderers plug in without changing the payload shape. And the core build uses only the Python standard library, so a new machine builds without dependency setup.

**Ben:** Some of those sound like preferences, not contracts. Standard library only? In 2026? One decent dependency could probably delete half the build script.

**Ana:** And the article explicitly lists that under "when to keep it small": avoid dependencies that only save a few lines. The stated reason for the constraint is that a new machine can build without dependency setup. The deeper reason is the closing principle — the system's strength is that a reader can understand it. Every dependency, framework abstraction, or styling system that makes the templates harder to inspect spends some of that. These contracts are what make the system learnable, for humans and for AI agents working in it.

**Ben:** Fine, but contracts plus "smallest change" is still vague when I'm sitting there with an actual need.

**Ana:** That's why there's a decision table. Need a new collection of articles? That's a new journal folder with `config.yaml`, posts, and specs — not template or build changes. Need one article? One post folder, one spec, one config line — not a new content format. Want a repeated visual language? A documented custom block type, but only after several real examples — not raw HTML copied into many posts. Need to publish a journal on the start page? Edit `_start/_config/apps.json` and run the start-page build — don't touch the journal generator. And if a rendered page looks wrong, fix source markdown, asset paths, templates, or build logic — never hand-edit anything under `docs/`.

## Adding things without guessing

**Ben:** Walk me through the journal case, because that's the one where I'd expect hidden steps.

**Ana:** Seven steps, no guessing. Create `_journals/<journal>/config.yaml`, create the `posts/` directory, add at least one post folder with `index.md`, add `spec.md` for the non-trivial posts, list the post paths under `sections:` in the config, build the journal, and then — if it should be discoverable — add it to the start page.

**Ben:** That last step smells like a trap. So I can build a journal successfully and it still doesn't show up anywhere?

**Ana:** Yes, and the article argues that's a feature, not a bug. The journal build and the start-page build are separate. A new journal can generate perfectly under `docs/<journal>/` and still not appear on the start page until `apps.json` is updated and `_start/generate-docs.py` is run. That separation lets maintainers draft a journal — build it, read it, iterate on it — before promoting it to the start page. Publication and discoverability are two different decisions.

**Ben:** And a single post?

**Ana:** Same shape, smaller: post folder with `index.md`, a `spec.md` if the work is substantive, front matter with a stable `permalink`, a line in `config.yaml`, modality docs if the spec calls for them, build, then inspect the generated post and spec pages, including the modality tabs. One convention worth keeping: use the same slug for the folder and the permalink. The system doesn't require it, but readers and maintainers benefit from the alignment.

**Ben:** You said "stable permalink" like it's sacred. Titles change all the time — why is the URL different?

**Ana:** Because everything keys off it. Titles can change, section names can change, even folder names can sometimes change before publication. But a `permalink:` is a published URL and the target of every double-bracket cross-reference. Change it after publication and you break external links and internal cross-links at once. And the cost compounds: the more a record is cited, the more expensive a permalink change becomes. It's the one rename the system genuinely punishes.

## Templates, blocks, and the no-test-suite problem

**Ben:** What about when the smallest change really is a template or build change? Those touch every page.

**Ana:** Then you slow down and ask the article's gating questions first. Is this a journal-specific need or a global rendering need? Does it affect existing posts? Does it preserve the JSON payload contract? Does it preserve raw HTML behavior where existing posts rely on it? Does it need a build-side change too? Then verify by rebuilding at least the affected journal, and eventually a full build for broad changes. For richer content, the sanctioned extension point is a custom block type — the pattern from [[cross-links-assets-and-blocks]]: add a fence tuple in `_wiring/build.py`, optionally a parser that transforms the block into JSON, a renderer function in `_templates/post.html`, keep the `{type, content}` envelope, and document the authoring syntax.

**Ben:** With the obvious failure mode that every minor markdown annoyance becomes a new block type.

**Ana:** Which the article forbids in as many words: don't add a custom block just because markdown feels slightly inconvenient. Add one when it gives authors a reusable content language that improves several posts. Same bar as the decision table — several real examples first.

**Ben:** Here's my real objection, though. You're describing template changes that touch every page, and there's no test suite. How is "be careful" a maintenance strategy?

**Ana:** There's no formal test suite *yet* — the article is honest about that — but there are practical checks, and they're listed as commands, not vibes. `py_compile` on the build script and the start-page generator, then run both builds. During scoped work there's a one-liner that rebuilds just the affected journal through the same `build_journal` path, as documented in [[build-pipeline-and-rendering-model]]. Then a concrete inspection list: the generated index, the changed post pages, the generated spec pages, copied assets, unresolved double-bracket links, and obvious rendering problems in tables, images, and custom blocks.

**Ben:** Manual inspection still depends on a human remembering to do it. What about the agents doing most of the editing?

**Ana:** That's the part of maintenance people skip, and the article calls it out: `AGENTS.md`, `CLAUDE.md`, and the READMEs are part of the operating system for AI-mediated authoring. When build behavior changes and those don't, future agents follow stale rules and produce reasonable-looking wrong work — which is worse than obviously wrong work, because it passes a glance. Good maintenance keeps three things aligned: the actual implementation, the human-facing documentation, and the agent-facing instructions. When those drift, the system gets harder to work in for everyone.

## What this post is not promising

**Ben:** Close it out. What should I *not* expect from this article?

**Ana:** Three explicit non-goals. It is not a full release process — it tells you how to change and verify the system, not how to ship versioned releases. It is not a CI/CD design — verification is scoped builds plus inspection, deliberately. And it is not a visual redesign plan. There's one open question it leaves standing: whether the project should eventually add a formal test suite or keep relying on scoped builds and inspection. That stays open until the manual checks stop being enough.

**Ben:** So the whole maintenance doctrine is: a short contract list, smallest change first, and look at what you built before you call it done.

**Ana:** Plus knowing why. The closing principle is that this works when the repository remains a clear collaboration surface — humans bring intent and judgment, AI agents help edit and verify, source files preserve the durable artifact, generated pages make it readable, and the build connects those layers with as little machinery as possible. *(laughs)* That's the system worth maintaining. Everything else in the post is just instructions for not breaking it.
