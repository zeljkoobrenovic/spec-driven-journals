---
timetoread: 2 min
---

AI agents are treated as structured product-architecture authors, not autonomous strategists. They become genuinely useful when the repository gives them structure to work inside: examples to inspect, local skills to follow, source models to edit, validation gates to pass, and source-first media generation — with humans keeping intent, judgment, source selection, and review.

The risk this addresses is speed in both directions. An agent drafts source files, fills repetitive structure, and generates documentation far faster than a human starting from a blank page — and, unconstrained, just as quickly produces a confident model that looks coherent but is ungrounded, schema-incompatible, and unmaintainable by the next session.

**What changes**

- A clear human–agent division of labor: humans choose the domain, provide sources and constraints, decide tradeoffs, and accept or reject the model; agents inspect existing patterns, edit source files, keep IDs and references stable, and run validators. Accountability for strategy stays human.
- Agent sessions follow a source-first workflow: read repository guidance, inspect comparable domains, load only the relevant local skills, draft or revise source files, validate, and only then generate documentation — closing with a summary of assumptions and gaps.
- A repo-local skill library replaces generic prompting: market research, jobs to be done, KPI architecture, product bricks, team topology, and structured JSON each get phase-specific guidance, so the agent stops treating every task as the same writing exercise.
- Validation changes what the agent optimizes for: when output must be valid JSON, reference-consistent, and renderable, the agent works with the actual model instead of optimizing prose fluency.
- AI-generated visuals — domain icons, JTBD comics, customer journey panels, capability infographics, dependency maps — make the documentation engaging, but are derived from the source model (prompts built from the actual `customers.json` language), never invented as disconnected decoration.

**What it costs**

- The structured workflow is slower than asking for a polished article; the bet is that it is much faster than repairing a disconnected product model later.
- Human review gets harder, not easier: reviewers must inspect model coherence — distinct customers, ownable bricks, connected roadmaps, visible assumptions — not just proofread text.
- Examples, skills, and validators are authoring infrastructure that must be maintained for agents to stay effective.

**What we are not doing**

- This is not a prompt-engineering catalog or a tool-specific guide for Codex or Claude Code.
- It does not claim AI agents can replace product judgment; validation proves the model is parseable and consistent, not that the strategy is right.

The Article tab covers the full workflow, the skill library, source-first image generation, and the failure modes to watch for. [[modeling-diverse-domains]] explains the example library agents learn from; [[delivery-teams-and-roadmaps]] gives the operating-model context.
