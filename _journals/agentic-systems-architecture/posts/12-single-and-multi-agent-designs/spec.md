---
status: accepted
revised: 2026-10-28
---

# Spec: One Agent or Many?

## Intent

Give architects a defensible test for when additional agents add value and what they cost. The chapter lands one position: start with one agent and split only on evidence, for one of four named reasons (context isolation, parallel read-only breadth, separated authority, independent verification). Once split, the design obeys many-readers-one-writer, a verifier before effects, one accountable agent per task tree, and budgets enforced by the runtime on the whole tree. After reading, the reader can reject an Agent Committee in a design review with evidence rather than taste, and can price and bound a fan-out that is justified.

## Audience

Software architects, principal engineers and technical leaders who review or fund agent designs and are shown multi-agent proposals, often framework-driven. They know distributed systems; they need the evidence, the topology vocabulary and the controls.

## Success criteria

- [x] Defines multi-agent system, topology, orchestrator–worker and context isolation precisely, and distinguishes call-and-return from transfer of control.
- [x] Compares five topologies (single agent, orchestrator–worker, supervisor, peer handoff, pipeline) plus ensemble and clean-context reviewer in tables.
- [x] Presents Anthropic (2025), Cognition (2025, 2026), Kim et al. (v3 2026), MAST and the debate literature with what was measured and its limits, and reconciles the apparent Anthropic–Cognition disagreement.
- [x] Gives the token, latency (tail) and error arithmetic for fan-out with labeled assumptions.
- [x] Ostrell worked example with ledger numbers: Weekend Fan-out caps, Scout conditional fan-out with costed run, Answerdesk specialist folded back after the Lost Handoff, Dealroom split rejected.
- [x] Failure-scenario table with detection, containment and recovery; trade-off table; requirements-per-interaction table; three mermaid diagrams.
- [x] Across Domains table and judgement on platform-common versus domain policy.
- [x] Article under 8,000 words before Sources.

## Non-goals

- Handoff payloads, A2A protocols, blackboards and accountability transfer mechanics: [[coordination-and-handoffs]].
- How a task is decomposed and how plans are represented: [[planning-and-decomposition]].
- Router design, delegation contract in general, sub-agent definition: [[routing-and-delegation]].
- Prompt-injection mechanics behind the trifecta split: [[prompt-injection-defense]].
- Pricing, tiering and caching in depth: [[agent-cost-and-model-routing]], [[caching-and-context-budgets]].
- Framework tutorials.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No public incident report attributes a production failure to multi-agent coordination; revisit if one appears.
- Whether the 2023 debate and planning results hold for 2026 reasoning models; no head-to-head found.
- Kim et al. is a preprint; update if it reaches a venue or the numbers change again.

## Decision log

- **2026-10-28** — Framed the chapter around "four reasons to add an agent" rather than a topology catalogue, because reviewers need a test, not a menu. Rejected tool count and team ownership as standalone reasons, following OpenAI's guide and the author's judgement.
- **2026-10-28** — Adopted "many readers, one writer" as the book default (reconciling Anthropic and Cognition as domain differences), with the ai-coding-cli worktree rule for unavoidable parallel edits.
- **2026-10-28** — Cited Kim et al. arXiv v3 numbers as current and the 17.2×/4.4× amplification figures as the earlier blog version's, per the orchestration brief.
- **2026-10-28** — Per consistency issue 12, multi-agent research decomposition rests on published reports; the interview designs are used only for the platform sub-agent rule, the coding worktree rule, a mislabeled "hierarchical multi-agent" counter-example and the single-node high-stakes pipelines.

## Sources

- **Internal**
  - [[routing-and-delegation]], [[planning-and-decomposition]], [[coordination-and-handoffs]], [[agent-runtime]], [[agent-threat-model]] — neighbouring ownership.
  - Interview designs: `agentic-platform-foundations` (step `control-flow`), `ai-coding-cli` (step `verify`), `agentic-sales-platform` (`highLevelArchitecture`), healthcare, public-benefits and research platforms (`highLevelArchitecture`).
  - `_research/brief-orchestration-multi-agent.md`, `brief-performance-economics-evolution.md` §1.4–1.6, `brief-evaluation-observability.md` §2.3, `brief-security-oversight.md` §1.2.
- **External**
  - Anthropic, *How we built our multi-agent research system* (2025) — token multiples, variance explained, fit and failures.
  - Cognition, *Don't Build Multi-Agents* (2025) and *Multi-Agents: What's Actually Working* (2026) — shared decisions, scoped children, no parallel writers.
  - Kim et al., *Towards a Science of Scaling Agent Systems* (2025, v3 2026) — task structure predicts benefit.
  - Cemri et al., *Why Do Multi-Agent LLM Systems Fail?* (2025) — failure taxonomy.
  - Choi, Zhu, Li, *Debate or Vote* (2025) — voting explains debate's gains.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: removed draft verification markers after checking the Claude Agent SDK page, corrected the MAST verification-mode names, aligned Scout workers with the July 2027 internal-or-web rule, applied turn/exchange wording, normalized source headings. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-28** — Final figure-fix pass: Figure 4 (review test) corrected: the "team ownership or personas" arrow now starts at the "Which reason?" diamond. *(AI-mediated session)*
