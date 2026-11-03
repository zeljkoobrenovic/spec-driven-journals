---
status: accepted
revised: 2026-10-28
---

# Spec: Context Engineering: Building What the Model Sees

## Intent

Give architects a way to treat the model's working context as an engineered artifact rather than an accumulating transcript. The chapter answers one question: how should the system assemble the model's working context for each step? The answer it must land: a deterministic context assembler builds each call's context from durable stores (history, task state, memory, retrieval) under an explicit budget, in a stable-to-volatile order, with trust labels on every segment; compaction is a lossy, recorded event with pinned facts written from receipts; and every call leaves a context manifest that makes decisions traceable and replayable. Labeling untrusted content helps but is not a security boundary.

## Audience

Software architects, staff and principal engineers and technical leaders who build or review agent platforms. They know distributed systems and prompt templates; they need a component design, a budget method and the evidence behind it, not an introduction to transformers.

## Success criteria

- [ ] The reader can distinguish conversation history, working context, task state, long-term memory and knowledge corpus, and say which chapter owns each.
- [ ] The reader can name the assembler's six responsibilities (select, shape, order, label, budget, record) and sketch a context manifest.
- [ ] The reader can design a per-call budget with ceilings per segment and a rule for what gives way, using Answerdesk's 24,000-token budget as the worked example, consistent with the ledger.
- [ ] The reader can state the five compaction rules, including pinned facts from receipts and re-read after compaction.
- [ ] The reader can explain what long-context research measured (Lost in the Middle, RULER, NoLiMa, Context Rot, GSM-IC), its limits, and why the numbers are historical.
- [ ] The reader can explain why trust labels and delimiters reduce probability but do not bound injection, with AgentDojo and adaptive-attack evidence.
- [ ] The chapter has a failure-scenario table (detection, containment, recovery), a trade-off table, a requirements table, an Across Domains table and three mermaid diagrams.

## Non-goals

- Retrieval quality, hybrid search, citations and groundedness checks: [[retrieval-and-grounding]].
- What persists across sessions and memory write policy: [[agent-memory]].
- Durable task state, checkpoints, resume vs replay: [[task-state-and-checkpoints]].
- Provenance envelopes and freshness SLOs: [[provenance-and-freshness]].
- Prompt-cache pricing and the economics of the prefix layout: [[caching-and-context-budgets]].
- Injection defenses beyond labeling (trifecta split, CaMeL, dual LLM): [[prompt-injection-defense]].
- Tool-result contracts and tool discovery: [[tool-contracts]], [[tool-ecosystems-and-mcp]].
- Delegation contracts between agents: [[coordination-and-handoffs]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No post-2025 long-context benchmark of current frontier models was verified; revisit the Evidence section when one is published.
- Whether provider-side compaction (server-managed) can meet the "compaction is a recorded event" rule depends on what the provider exposes about the replaced range; not verified across providers.
- Retention of context manifests that reference personal data needs a ruling from the privacy owner; the chapter names the owners but not the period.

## Decision log

- **2026-10-28** — Built the chapter around a local Ostrell finding (second-revisit proposals after sliding-window truncation) rather than a new canonical incident, because the ledger's nine incidents are owned by other chapters; Toolyard's existing one-revisit limit made the failure harmless, which illustrates "enforcement outside the context".
- **2026-10-28** — Adopted the caching chapter's ledger facts (L0–L4 plus volatile tail, 24,000-token budget, 16,000-token compaction trigger, cache share 11% → 76%) and reconciled the ceilings: the total cap is absolute and history is compacted early when the tail needs room. Kept mean tokens per call almost unchanged so the "about two thirds" spend reduction stays attributable to the layout.
- **2026-10-28** — Reconciled the sources' compaction disagreement (Manus append-only and keep errors; Anthropic tool-result clearing; Cognition history compression) as append-only within a turn's tool loop and re-assembly at turn boundaries.
- **2026-10-28** — Treated trust labeling as a probability reducer, not a boundary, following AgentDojo, spotlighting and adaptive-attack evidence; the manifest's deterministic "has read untrusted content" signal to the policy engine is the security contribution.

## Sources

- **Internal**
  - [[agent-runtime]], [[models-and-the-model-gateway]] — the loop and gateway the assembler sits between.
  - [[caching-and-context-budgets]] — prefix layout and budget facts in the scenario ledger.
  - [[task-state-and-checkpoints]], [[agent-memory]], [[retrieval-and-grounding]], [[provenance-and-freshness]] — the durable stores the context is computed from.
  - [[prompt-injection-defense]] — where the Poisoned Ticket fix lives.
- **Interview design examples**
  - `ai-coding-cli` steps `context` and `compaction`; `agentic-support-platform` step `grounding`; `agentic-platform-foundations` step `durable`; `agentic-healthcare-platform` step `privacy`; `agentic-public-benefits-platform` step `grounding`.
- **External**
  - Anthropic, "Effective context engineering for AI agents" (2025), "Effective harnesses for long-running agents" (2025), "Writing effective tools for agents" (2025), "Introducing advanced tool use" (2025).
  - Manus, "Context Engineering for AI Agents" (2025).
  - Liu et al. (2023), Hsieh et al. (2024), Modarressi et al. (2025), Shi et al. (2023), Chroma "Context Rot" (2025), Li et al. (2024).
  - Hines et al. (2024), Debenedetti et al. AgentDojo (2024), Nasr et al. (2025).
  - OpenTelemetry GenAI semantic conventions (Development, accessed 2026-10).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: aligned conversation-level "turns" to exchanges (ruling 19); dated the billing-specialist fold-back to 7 June 2027 per the editor ruling, so the May trace review now describes the 34-tool release candidate; clarified the 77,000 → 8,700-token tool-search example. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
