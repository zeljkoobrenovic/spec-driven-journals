---
status: accepted
revised: 2026-10-28
---

# Spec: Memory: What an Agent Should Remember, and for How Long

## Intent

Give architects a defensible design for agent long-term memory: what deserves to persist across sessions, who may write it at user, tenant and organization scope, how each memory carries provenance, trust and an expiry, how it is erased, and how it is defended against poisoning and evaluated. The chapter's central claim is that **memory holds only what no system of record knows**, is written through a deterministic **memory write policy** rather than by the model, and is data, never authority or the source of a commitment. It owns **long-term memory (agent)**, **memory write policy**, **memory expiry** and **memory poisoning**, and keeps them distinct from conversation history, working context ([[context-engineering]]) and task state ([[task-state-and-checkpoints]]).

## Audience

Software architects, platform owners and agent owners who are adding or reviewing memory for customer-facing, back-office, coding or high-stakes agents, plus the privacy and security reviewers who must approve it. They know caches, data retention and access control; they need the agent-specific write path, the poisoning evidence and the erasure design.

## Success criteria

- [ ] Reader can place memory among the five stores (history, working context, task state, long-term memory, corpus) and name three things that are not memory (compaction digests, progress notes, copies of records).
- [ ] Reader can classify memories as semantic, episodic or procedural and explain why per-user procedural memory is rejected.
- [ ] Reader can write a memory write policy with allowed keys, system-of-record overlap rejection, confirmation for action-shaping keys, trust derived from source labels, and supersession.
- [ ] Reader can set expiry and review per memory class, tied to the freshness register and GDPR storage limitation.
- [ ] Reader can design an erasure path that reaches store, index, transient content and backups while the evidence log keeps only references and hashes.
- [ ] Reader can summarize the poisoning evidence (AgentPoison, MINJA, SpAIware, delayed tool invocation) with its limits, and name structural controls that do not rely on detection.
- [ ] The Stale Preference numbers are consistent across the chapter and recorded in the scenario ledger; Tidemark details agree with [[provenance-and-freshness]], [[prompt-injection-defense]] and [[versioning-agent-systems]].
- [ ] The Across Domains table separates platform-common mechanisms from domain policy, including `memory: none` as a recorded decision.

## Non-goals

- Working context assembly, compaction and context budgets ([[context-engineering]], [[caching-and-context-budgets]]).
- Retrieval over corpora the agent does not write, citation and grounding ([[retrieval-and-grounding]]).
- Durable task state, checkpoints, resume and replay ([[task-state-and-checkpoints]]).
- Provenance envelopes, freshness SLOs and invalidation sweeps in general ([[provenance-and-freshness]]).
- Injection defenses beyond memory ([[prompt-injection-defense]]); memory schema migration strategies ([[versioning-agent-systems]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No published evaluation compares task outcomes of business agents with and without long-term memory; the chapter says so and uses fictional Ostrell measurement.
- No production report of memory poisoning at a real deployment was found; revisit if one is published.
- GDPR Art. 22 and other provisions may be amended by the pending Digital Omnibus; the chapter cites the 2016 text for Arts. 5, 12, 15–17.
- Whether user confirmation of preferences should be required for all keys or only action-shaping ones (Ostrell chooses action-shaping only).

## Decision log

- **2026-10-28** — Defined long-term memory by exclusion of anything a system of record holds; a contradicting memory candidate becomes a change request to the record owner. This turns the Stale Preference migration's 1,310 change requests into the chapter's argument that memory can surface record defects.
- **2026-10-28** — Adopted the platform-foundations design's memory governance (provenance, trust tier, TTL, derived index, "a recalled instruction is data, not a grant") and filled its gap: an explicit lifecycle for moving memories between tiers, with quarantine by provenance. Replaced model-rated confidence with a trust level derived from how the memory was established.
- **2026-10-28** — Set the scope ladder: model-written memory only at user scope; tenant memory written by people; organization lessons as reviewed knowledge-base or agent-version changes. Chosen because MINJA shows shared model-written memory is poisonable by ordinary users.
- **2026-10-28** — Set the Stale Preference in May 2027 and the redesign (Tidemark schema v3) in July 2027, so that the memory row of the July 2027 freshness register in [[provenance-and-freshness]] and the low-trust rule of the July 2027 injection redesign are consistent with it; schema v4 (October 2027, [[versioning-agent-systems]]) follows later.

## Sources

- **Internal**
  - [[context-engineering]], [[task-state-and-checkpoints]], [[provenance-and-freshness]], [[retrieval-and-grounding]] — the Part IV distinctions this chapter keeps.
  - [[prompt-injection-defense]], [[versioning-agent-systems]], [[caching-and-context-budgets]], [[agent-observability]] — Tidemark facts the chapter must agree with.
- **Interview design examples** (`system-design-interviews/data/book/`)
  - `agentic-platform-foundations` (step `durable`, deep dive "Memory governance", `dataModel.memories`, follow-up on poisoning); `ai-coding-cli` (steps `context`, `safety`); `ai-coding-harness` (step `guides`); `agentic-support-platform` and `agentic-marketing-platform` (step `grounding`), `agentic-sales-platform` (step `enrichment`); `agentic-legal-platform` (step `grounding`); `agentic-healthcare-platform` (steps `grounding`, `privacy`); `agentic-public-benefits-platform` (step `grounding`).
- **External**
  - MemGPT (2023), Generative Agents (2023), LongMemEval (2024), Mem0 (2025, vendor), Reflexion (2023) — memory architectures and their measured limits.
  - AgentPoison (2024), MINJA (2025), Rehberger's SpAIware (2024) and Gemini delayed-invocation (2025) write-ups; Microsoft AI Red Team taxonomy (2025); OWASP Agentic Top 10 (2025) and LLM08:2025.
  - Anthropic memory tool and Claude Code memory docs; LangGraph memory docs; Google ADK sessions docs; TechCrunch on ChatGPT memory (2025); GDPR (2016).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: replaced the repeated five-store table with a link to context-engineering; "turns" in memory provenance renamed messages (ruling 19); OWASP ASI06 claim labeled as not verified against the primary text. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-28** — Final figure-fix pass: Figure 3 (memory states) regenerated: separate Quarantined to Active return arrow, one end dot. *(AI-mediated session)*
