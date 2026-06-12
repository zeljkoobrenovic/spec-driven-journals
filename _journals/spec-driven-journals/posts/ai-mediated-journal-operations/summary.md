---
timetoread: 2 min
---

AI agents are useful journal collaborators when they treat the Spec-Driven Journals repository as source: read the local contract before editing, update specs before substantial posts, build scoped output, and leave a clear verification trail. This is not "AI writes the journal" — a human states intent, an agent edits source, and the human reviews the diff and the generated output; the durable rationale lives in [[ai-mediated-authoring]].

**What changes**

- The division of labor is explicit. Humans state intent, judge direction, supply missing context, and accept or redirect; agents inspect source, draft specs and posts, preserve conventions and stable permalinks, run scoped builds, and report what they verified. The agent moves work through source files — it does not own editorial judgment.
- A good session has a predictable shape: read the request, inspect configs/posts/specs/templates, update specs first when intent shifts, edit source (never generated HTML), run a scoped build, check output for unresolved links, and report what changed and what was verified.
- Agents read before editing. `README.md`, `AGENTS.md`, the `_journals/` and `_wiring/` READMEs, `_templates/post.html`, and existing posts and specs teach the contract — reading them is cheaper than repairing a model that guessed wrong.
- The spec is the agent contract for non-trivial posts: intent, audience, success criteria, non-goals, modalities, open questions, decision log, sources, changelog. Without it, agents optimize for fluent prose; with it, they optimize for a specific article outcome.
- Modality docs are agent-authored by design. Four skills in `.claude/skills/` — `detailed-article`, `management-summary`, `podcast-dialog`, `explainer-comics` — define the formats, treat the spec as read-only (drift gets flagged, not silently patched), and end every run with a build plus verification.

**What it costs**

- Discipline around dirty worktrees: never revert unrelated changes, prefer journal-scoped builds over full rebuilds during scoped work, and always say what was built — silent verification is useless to the reviewer.
- Generated output stays disposable. If something renders wrong, the fix belongs in source — the markdown path, the asset location, the permalink, the build logic — never in `docs/<journal>/*.html`. Agent quality is partly measured by whether the agent returns to source.
- A final report is owed every time: source files changed, output rebuilt, verification commands run, known limitations, and unrelated dirty files noticed but not touched.

**What we are not doing**

- No tool-specific prompt catalog.
- No security policy for AI development in general.
- No model selection guidance.

The Article tab covers the session shape in full, the failure modes to watch for, and why the repository's structure is what makes agent guardrails work.
