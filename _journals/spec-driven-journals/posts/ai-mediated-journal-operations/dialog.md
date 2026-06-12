---
timetoread: 8 min listen
---

## Doesn't the AI just write the journal?

**Ben:** Ana, give it to me straight. The repository says it assumes AI-mediated authoring for substantive work. Why isn't this post just one sentence — "the AI writes the journal"?

**Ana:** Because that's exactly what it is *not*. The model is: a human describes intent, an agent edits the Spec-Driven Journals source, and the human reviews the diff and the generated output. The durable rationale is in [[ai-mediated-authoring]]; this post is about the operating behavior inside the repository. The agent helps move the work through source files. It does not own the editorial judgment.

**Ben:** That's a nice slogan. Where's the actual line between what I do and what the agent does?

**Ana:** The post draws it as a table, and it's pragmatic. The human states the intent, decides whether the direction is good, provides missing context, reviews the generated output, and accepts or redirects the work. The agent inspects the repository's guidance and current source, drafts specs, posts, config, and template changes, preserves existing conventions and stable permalinks, runs scoped builds, and reports verification — and it avoids reverting unrelated changes.

**Ben:** So why should a busy colleague care about any of this? They just want the post written.

**Ana:** Because the failure mode of skipping it is an agent writing plausible prose that does not fit Spec-Driven Journals. The whole point of the session shape — read the request, inspect configs, posts, specs, templates, and scripts, update specs first, edit source, run a scoped build, check the output, report — is not to slow down. It's to prevent exactly that.

## Read before editing

**Ben:** "Inspect the source first" sounds like ceremony. Modern models know what a static-site generator looks like. Can't the agent just guess and fix later?

**Ana:** The post's answer is blunt: reading these files is cheaper than repairing a model that guessed wrong. Agents should first ask Spec-Driven Journals what it already does. There's a concrete reading list — `README.md` for purpose and the journal map, `AGENTS.md` for the build, authoring, and rendering contract, the `_journals/` README for folder layout and front matter, the `_wiring/` README for build scripts, `_templates/post.html` for what the client-side renderer actually supports, plus existing `config.yaml` files and existing posts and specs for tone and cross-link conventions.

**Ben:** And the source of truth is the repo, not the published site?

**Ana:** The official Spec-Driven Journals repository is the primary source context. The generated site is useful for reader-facing review, but source edits belong in source. That distinction comes back later in a sharper form.

**Ben:** Fine, sharper form now. What happens when the agent finds the working tree already messy — half-finished changes from me, or from another agent?

**Ana:** That's the dirty-worktree rule, and it's strict: do not revert unrelated changes. And it has a practical consequence for builds. A full `python3 _wiring/build.py` regenerates every journal, including ones with unrelated dirty output. So during scoped work, a journal-specific build can be safer — it updates only the affected generated site. Either way the agent should still say what it built. Silent verification is not useful to the reviewer.

## Source in, disposable output

**Ben:** Here's my skeptical scenario. An image doesn't render on the published page. The fastest fix is to patch the HTML in `docs/`. Two seconds. Why not?

**Ana:** Because generated output is disposable by design. Agents should not edit `docs/<journal>/*.html` directly. Generated files are useful for verification and publication — they are not the source of the article. If an image does not render, the fix belongs in the markdown path, the asset location, or the build logic. If a cross-link is unresolved, the fix belongs in the source permalink or the link target.

**Ben:** And if the agent patches the HTML anyway?

**Ana:** The post actually frames this as a quality signal: it's one of the easiest ways to evaluate agent quality. A good agent returns to source. An agent that patches output has become casual about source, and that's the root of most of the failure modes.

**Ben:** Name a few. What's on the avoid list?

**Ana:** Editing generated HTML instead of source. Changing permalinks unnecessarily. Adding posts without wiring `config.yaml`. Writing an article that doesn't match its spec. Skipping the build. Ignoring unresolved double-bracket links. Overwriting user changes in unrelated journals. Inventing repository behavior instead of inspecting the scripts. And treating specs as polished documentation rather than working contracts. The post insists these aren't abstract risks — they're the practical failure modes of AI-assisted documentation systems.

## The spec is the contract

**Ben:** You keep saying "spec first." Why does an AI agent need a spec? It can hold the whole conversation in context.

**Ana:** Context isn't a contract. For non-trivial posts, the spec should be the first source file the agent creates or updates, because it gives the agent a compact contract: intent, audience, success criteria, non-goals, modalities, open questions, decision log, sources, changelog. Without that contract, the agent may optimize for fluent prose. With it, it can optimize for a specific article outcome.

**Ben:** You said "modalities." That's new — the post folder isn't just an article anymore?

**Ana:** Right, and the post has a whole section on it. The modality docs that share a folder with `index.md` are agent-authored by design, and four skills in `.claude/skills/` define the formats and workflows. `detailed-article` writes `index.md` — the canonical home of the house style, required, the default tab. `management-summary` writes `summary.md` — 300 to 500 words keyed to the spec's success criteria and non-goals. `podcast-dialog` writes `dialog.md` — two named hosts, consistent per journal, walking the success criteria as conversation beats.

**Ben:** Which is what we're doing right now, rather self-referentially.

**Ana:** *(laughs)* The format demonstrates itself. The fourth is `explainer-comics`, which writes `comics.md` plus panels — panel placeholders and a Gemini generation script with a shared style block, so the characters stay consistent across panels. And all four skills share two rules: the spec is a read-only contract — drift gets flagged, not silently patched — and every run ends with a build plus verification that the generated page embeds the new modality.

**Ben:** Last objection. At the end of a session, do I really want a transcript of everything the agent did? That's noise.

**Ana:** The post agrees — the user does not need a transcript of every action. They need enough to review the result and continue confidently. Concretely, five things: source files changed, generated output rebuilt, verification commands run, known limitations or skipped checks, and unrelated dirty files noticed but not touched.

## What this post is not

**Ben:** Close it out. What should I *not* take away from this?

**Ana:** Three explicit non-goals. It is not a tool-specific prompt catalog — no library of magic prompts for Claude Code or Codex. It is not a security policy for AI development in general. And it offers no model selection guidance. It's deliberately scoped to repository operations, not general AI coding practice.

**Ben:** Then what's the payoff for keeping it this narrow?

**Ana:** That the repository is structured enough for agents to reason about. Markdown source, sibling specs, stable config, a deterministic build, and generated review surfaces give the agent guardrails — it can do real editorial and implementation work without turning every session into a fresh context negotiation. That's the operating promise of spec-driven journals. And it's the hinge point of the series: structure, content mechanics, workflow, and AI collaboration are covered, and [[build-pipeline-and-rendering-model]] opens the implementation side.

**Ben:** So the headline isn't "AI writes the journal." It's "the journal is built so AI can work in it without breaking it."

**Ana:** And so a human can always see, in one diff and one report, exactly what it did.
