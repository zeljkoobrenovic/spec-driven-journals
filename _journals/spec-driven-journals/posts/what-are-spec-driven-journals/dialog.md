---
timetoread: 8 min listen
---

## Why should anyone care?

**Ben:** Ana, give it to me straight. The world is drowning in publishing tools — wikis, CMSes, docs platforms, Notion clones. Why should a busy engineer care about something called "spec-driven journals"?

**Ana:** Because it is deliberately none of those things. Spec-Driven Journals is not a wiki, not a content-management system, not a general application framework. It is a small static-site generator wrapped around a writing discipline: put durable records in markdown, keep source in git, make the build deterministic, and let the generated pages be the review and reading surface. The tool is small on purpose; the discipline is the product.

**Ben:** "Durable records" — what does that actually mean in practice?

**Ana:** The artifacts organizations produce that are supposed to outlive the meeting: principles, strategy notes, architecture decisions, foundation records, operating models, standards, implementation guides. Those things usually *start* in meetings, chats, documents, or AI conversations, and that is fine for creation. But it is weak for memory. If the durable artifact stays scattered across tools, future readers — and future AI agents — cannot reliably inspect it, link it, or build on it.

**Ben:** So the pitch is "give the writing a stable home."

**Ana:** Exactly. Source files live under `_journals/`, each journal has a `config.yaml`, each post has front matter and a markdown body, substantial posts have a `spec.md`, generated output lands under `docs/`, and cross-record links use stable permalinks. The goal is not to make writing more bureaucratic. The goal is to make durable writing easier to inspect, review, publish, and improve.

## Journal, post, spec, output — keep them straight

**Ben:** The name is doing two jobs, though. Unpack it for me — what is a "journal," and what does "spec-driven" add?

**Ana:** Those are the two connected ideas. A **journal** is a coherent collection of posts, published as its own static site under `docs/<journal>/`. **Spec-driven** means non-trivial posts have a sibling `spec.md` that states intent, audience, success criteria, non-goals, sources, and a changelog — written before the article is drafted. So you get a clean separation: the spec is the working contract, the post is the published artifact, and the generated HTML is the reader-facing output.

**Ben:** Four artifacts where most people manage one. That sounds like overhead.

**Ana:** It sounds like it until you ask where fixes go. The mental model has three layers: source — markdown posts, specs, configs, assets, templates; build — a small Python script that parses source and writes static HTML; and publication — the generated pages under `docs/`. The source layer is canonical. The publication layer is disposable output. That distinction is central: if a generated page looks wrong, the fix belongs in source. Editing the generated HTML directly might make one page look better, but it breaks the model that future authors and AI agents depend on.

**Ben:** And one spec maps to exactly one article?

**Ana:** One spec can drive *more* than one published doc. Besides the main article, a post folder can carry sibling modality files — a management summary, a two-host conversation like this one, an explainer comic — all rendered as tabs on the same post page. A tab appears when the file exists, the article stays the default tab, and the post URL never changes.

## The spec sounds like paperwork

**Ben:** Here is my honest reaction to `spec.md`: it sounds like a form. Why would a competent writer fill out paperwork before writing?

**Ana:** Because the spec is short on purpose, and it answers the questions that usually cause drift. Why does this article exist? Who is it for? What should a reader understand after reading it? What is deliberately out of scope? Which sources shaped it? What changed during drafting? It does not replace the post — it keeps the post honest.

**Ben:** A disciplined author holds those answers in their head anyway.

**Ana:** A human author might. But there is a second reader now. For AI agents, the spec is a contract: before generating prose, the agent has to know what the post is supposed to do. That changes the economics. When an agent drafts or revises an article, the spec is the thing you check the output against — and it is why this very journal has specs. The articles are about Spec-Driven Journals, and the project's own philosophy says non-trivial articles should be spec-driven. It would be strange to exempt ourselves.

**Ben:** Fair — eating your own cooking. But "structured source readable by humans and AI agents" is the thesis sentence of the post. Is that really two audiences, or marketing?

**Ana:** Two real audiences with the same need. Humans need to review, link, and build on records over time; agents need the same thing, just more literally — stable files, stable permalinks, predictable structure. Cross-record links keying off permalinks means the collection stays navigable as it grows, for both kinds of reader.

## Small on purpose

**Ben:** Now the part I find suspicious. "No framework, no database, no CMS" usually means "we have not needed one *yet*." Is small a feature or a stage?

**Ana:** A feature, and the post lists it explicitly: no application framework, no dependency install for the core build, no server-side rendering pipeline, no database, no schema package, no CMS workflow. The main build uses Python's standard library, HTML templates, CSS, and client-side JavaScript. That is enough for the actual goal — publish durable writing in a way that is versioned, searchable, linkable, and easy for AI agents to inspect.

**Ben:** Until it isn't.

**Ana:** Maybe — but small does not mean casual. It means the system has fewer moving parts to explain, fewer dependencies to patch, and fewer hidden behaviors for authors to memorize. For a system whose whole job is durable memory, every dependency is a future maintenance debt and every hidden behavior is a future surprise. Lightweight is the design decision, not the budget constraint.

**Ben:** Suppose I am sold. Where do I start, and where do I find the thing itself?

**Ana:** Two stable entry points: the official project repository at github.com/zeljkoobrenovic/spec-driven-journals, and the generated journal site at zeljkoobrenovic.github.io/spec-driven-journals. Then read the series in layers — that order is deliberate. Start with the philosophy in [[journals-as-source-of-truth]] — where durable changes should be made and why source wins. Then the source shape in [[anatomy-of-a-journal]]. Then authoring mechanics: [[cross-links-assets-and-blocks]] for links, images, diagrams, and custom blocks; [[spec-driven-authoring-workflow]] for how a substantive post moves from spec to generated review; [[ai-mediated-journal-operations]] for how humans and agents collaborate. Only then the implementation: [[build-pipeline-and-rendering-model]] and [[extending-and-maintaining-the-system]].

**Ben:** Philosophy before plumbing.

**Ana:** Always. If you start with the build script, you learn a tool. If you start with the philosophy, you learn why the tool is allowed to stay small.

## What this post is not

**Ben:** Close it out. What should a listener *not* expect from this introduction?

**Ana:** Three things, explicitly out of scope. It is not a detailed implementation walkthrough — the generator's internals come later in the series. It is not a full authoring checklist — the workflow post covers that. And it is not a comparison with external publishing platforms — the post defines what Spec-Driven Journals is, not how it stacks up against your wiki.

**Ben:** So if I remember one sentence?

**Ana:** The durable idea is simple: write the source, keep the spec close, generate the site, review the output, and return fixes to source.

**Ben:** Write it down, spec it first, and never edit the output. *(laughs)* Even I can remember that.

**Ana:** That is the whole discipline. The rest of the series is just making it comfortable to live by.
