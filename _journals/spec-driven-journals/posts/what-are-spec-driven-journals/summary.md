---
timetoread: 2 min
---

Spec-driven journals treat durable writing as structured source: each article is authored from a lightweight spec, published as static documentation, and kept readable by humans and AI agents. The system is a small static-site generator wrapped around a writing discipline — not a wiki, not a CMS, not an application framework.

The name carries both halves of the model. A **journal** is a coherent collection of posts published as its own static site under `docs/<journal>/`. **Spec-driven** means non-trivial posts have a sibling `spec.md` stating intent, audience, success criteria, non-goals, sources, and changelog before the article is drafted. The spec is the working contract; the post is the published artifact; the generated HTML is the reader-facing output. One spec can also drive sibling modality docs — summary, dialog, comic — rendered as tabs on the same post page.

**What changes**

- Durable artifacts — principles, decisions, strategy notes, standards — get a stable home in markdown under `_journals/`, versioned in git, instead of staying scattered across meetings, chats, documents, and AI conversations where future readers and agents cannot reliably inspect them.
- Every record has three distinct layers: source (markdown, specs, configs, assets), build (a small Python script), and publication (generated pages under `docs/`). Source is canonical; the publication layer is disposable output. If a generated page looks wrong, the fix belongs in source.
- Substantial posts carry a `spec.md` answering the questions that cause drift: why the article exists, who it is for, what a reader should understand, what is out of scope, which sources shaped it, and what changed during drafting. For AI agents, the spec is a contract to satisfy before generating prose.
- Cross-record links use stable permalinks, so the collection stays navigable for humans and inspectable for agents as it grows.
- The series itself reads in layers: philosophy first ([[journals-as-source-of-truth]]), then source shape ([[anatomy-of-a-journal]]), authoring mechanics ([[cross-links-assets-and-blocks]], [[spec-driven-authoring-workflow]], [[ai-mediated-journal-operations]]), and implementation last ([[build-pipeline-and-rendering-model]], [[extending-and-maintaining-the-system]]).

**What it costs**

- Specs are extra writing before the writing — accepted deliberately, because the spec keeps the article honest and gives agents a contract; it is kept short so it never replaces the post.
- Staying intentionally small means living without framework conveniences: no database, no CMS workflow, no server-side rendering pipeline, no dependency install for the core build. Small is a discipline, not casualness — fewer moving parts to explain, patch, and memorize.

**What we are not doing**

- No detailed implementation walkthrough here — that comes later in the series.
- No full authoring checklist.
- No comparison with external publishing platforms.

The Article tab covers the layer model, the official project links, and the full series map.
