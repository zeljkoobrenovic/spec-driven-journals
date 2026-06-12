---
timetoread: 8 min listen
---

## Isn't this just "use git"?

**Ben:** Ana, give it to me straight. "Source wins, don't edit generated HTML" — isn't that just telling people to use git? Why does this need a whole record?

**Ana:** Because the failure it prevents is one everyone has lived through: the source says one thing, the published page says another, and no one knows which one to trust. Spec-Driven Journals makes the rule explicit and structural. Durable changes belong in the source files — under `_journals/`, `_templates/`, `_wiring/`, and `_start/`. The generated site under `docs/` is what readers see, search, and share, but it is not where durable changes belong.

**Ben:** And the temptation to edit the generated page directly is real enough to legislate against?

**Ana:** It's the most natural temptation there is. You spot a typo in the browser, the HTML file is right there, the fix takes ten seconds. But during a build, `docs/<journal>/` is removed and recreated for each journal being built. Any manual change made there is fragile because the next build can overwrite it. You haven't fixed the journal — you've created a divergence with a countdown timer on it.

**Ben:** So the rule is really "the generated layer is disposable."

**Ana:** Disposable but not unimportant — that distinction matters and we'll get to it. First the positive half: what *is* canonical.

## The two layers

**Ben:** Okay, draw me the map. What counts as canonical?

**Ana:** The files humans and AI agents should actually edit. The journal's `config.yaml` — title, description, sections, the ordered post list. Each post's `index.md` — the published article source, the required default modality. The post's `spec.md` — the working contract for non-trivial work. The optional modality docs — `summary.md`, `dialog.md`, `comics.md` — driven by the same spec and rendered as tabs. Per-post `assets/`. The shared templates and CSS, the build script, and the start-page catalog. Everything in that list is reviewable in git: it can be diffed, cited, linted, generated from, and read by an AI coding agent before it changes anything.

**Ben:** That last clause is doing some work. We'll come back to it. And the generated layer — you said it's still important. How, if it's overwritten on every build?

**Ana:** Five concrete ways, straight from the record. It shows whether the article reads well after rendering. It exposes broken cross-links and missing assets. It gives reviewers a browser-friendly surface. It is what static hosting can publish. And it lets non-authors read the system without opening markdown files. The generated site is genuinely the public reading surface — the project even keeps the split visible in its URLs: the GitHub repository is the canonical source, the GitHub Pages site is the generated output.

**Ben:** So important as a *surface*, never as a *medium*. You read it, you don't write it.

**Ana:** Exactly. And that gives authors a stable five-step workflow: change the post, spec, config, template, or script. Build the journal. Inspect generated output. If the rendered page exposes a problem, return to source. Commit source and generated output together when the change is meant to publish. The generated site becomes a feedback loop, not a second editing surface.

## The AI agent angle

**Ben:** Here's my skeptical read, though. This sounds like discipline for discipline's sake. Plenty of teams edit wikis directly and survive. What's actually at stake?

**Ana:** The stakes went up when AI agents joined the authoring loop. AI agents need stable context. If the source of truth is a set of markdown files and small scripts, an agent can inspect the current system before acting — read the config, find the post, check the spec, understand the build, make scoped edits, run a scoped build, summarize the result.

**Ben:** And if it isn't?

**Ana:** Then the truth is scattered across generated pages, chat history, local browser edits, and unpublished documents — and the agent has to guess. Guessing is where confident but wrong output starts. That's the line I'd underline in the whole record. Spec-Driven Journals reduces that risk by making the source tree the memory.

**Ben:** "The source tree is the memory." Meaning the agent doesn't need to remember anything between sessions, because everything it needs is on disk?

**Ana:** Right — and so does the human, which is the same benefit wearing two hats. The record ends with a practical test: a journal is behaving like source of truth when a future author can answer, from source alone — which posts exist and in what order, what each permalink is, what the intent of the post was, which source files generate the page, which template renders it, which assets it depends on, which related records it links to, and what changed in the last meaningful authoring session. If those answers live in source, the journal can keep improving. If they live only in memory, the journal decays.

## Where specs fit

**Ben:** You keep mentioning specs as part of the canonical layer. But isn't a spec just documentation about the post? Why is it source of truth rather than scaffolding you throw away?

**Ana:** Because specs and posts carry different things, and both are durable. The record lays out the roles: `spec.md` states the intent and contract for a post — and which modalities it drives. `index.md` carries the published argument, the Article tab. The summary, dialog, and comic are optional modality docs derived from the same spec and article. And both get generated counterparts: a `.spec.html` so reviewers can inspect the contract in the browser, and the post HTML where readers see all the modalities as tabs.

**Ben:** And when the post and the spec disagree?

**Ana:** Then the spec is drifted and should be reconciled. The rule of direction is: when a post changes direction, the spec should change first. And the record is explicit that this is not process for its own sake — it is how Spec-Driven Journals keeps intent visible across AI-mediated sessions. Sessions end; context windows close. The spec is the piece of intent that survives.

**Ben:** Let me push once more. The build step itself — doesn't requiring a build between edit and review just add friction compared to editing the page you're looking at?

**Ana:** It adds one command, and it buys you the thing direct editing destroys: the guarantee that what you reviewed is what the source produces. A post that builds but reads poorly in the browser is not done — the record says that outright. The loop is edit source, build, look, go back to source. The friction is the feature: every fix lands where the next build, the next author, and the next agent can find it.

## What this is not saying

**Ben:** Alright. Fence it off for me — what should listeners *not* take away?

**Ana:** Three explicit non-goals. This record is not rewriting the foundation decision on markdown records — that rationale lives in [[markdown-records]] and [[markdown-records-as-canonical]], and this article only explains how the principle works inside Spec-Driven Journals. It is not a tool-by-tool comparison of knowledge systems. And it is not publishing governance for every journal.

**Ben:** And the softer misreadings?

**Ana:** The record names those too. Source-first does not mean every thought must be written in markdown before discussion — conversations, sketches, meetings, and AI sessions can all help shape the work. And it does not mean generated pages are unimportant; we covered why they matter. The point is narrower and stronger: when the durable artifact is accepted, its canonical form belongs in source.

**Ben:** So the one-line version for someone closing the tab now?

**Ana:** Source wins. Edit the markdown, the spec, the config — never the generated page. Build to see, return to source to fix, commit both together.

**Ben:** And if I forget all that, the next build will remind me by deleting my cleverness. *(laughs)*

**Ana:** That's the system working as designed.
