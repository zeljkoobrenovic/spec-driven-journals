---
status: accepted
revised: 2026-10-28
---

# Spec: Retrieval and Grounding

## Intent

Give architects a defensible design for how agents find and cite knowledge, and for how the system knows an answer is grounded. The chapter shows that retrieval is a tool with a contract: the model writes the query, while deterministic code and policy decide the scope, applied inside the index query. It explains how to choose a retrieval mode (load whole, pre-retrieval, retrieval tool, agentic search, structured lookup) from the question and the source. It shows that a citation is a pointer, checked for existence, support, authorization and currency. And it makes "no evidence" a designed, measured, successful outcome. After reading, the reader can review a RAG design and name where authorization, versions and verification live.

## Audience

Software architects, senior engineers and technical leaders who design or review enterprise agents that answer from documents and data: support, legal, research and internal assistants. They know search and vector databases. They need the agent-specific decisions: who sets retrieval scope, how citations are structured and checked, how to evaluate retrieval separately from generation, and how verification policy differs by domain.

## Success criteria

- [ ] Reader can choose a retrieval mode for a claim type from the source (system of record, small corpus, navigable source, large corpus), with the evidence for each choice dated and sourced.
- [ ] Reader can specify a retrieval tool contract in which tenant, principal and corpus scope come from the verified run context and are applied in the index query, never from model arguments or a prompt instruction.
- [ ] Reader can state the four checks on a cited claim (exists, supports, authorized/authoritative, current) and say which are decided by code.
- [ ] Reader can design a claim-level groundedness check with an uncertain band that flags or escalates, and explain why the judge runs in a fresh context and is calibrated and versioned.
- [ ] Reader can design abstention as a first-class outcome: a defined exit, a trigger outside the model, a measured rate and precision.
- [ ] Reader can lay out retrieval, authorization, grounding, abstention and end-task metrics as separate eval levels, with zero-tolerance canary tests for leakage.
- [ ] The Ostrell worked example (Answerdesk redesign, Clausewise playbook) uses ledger-consistent numbers, and the Across Domains table separates platform-common mechanism from domain policy.

## Non-goals

- Context budgets, ordering and compaction of retrieved evidence: [[context-engineering]].
- Provenance envelopes, freshness SLOs, re-read before write and the Stale Price Book: [[provenance-and-freshness]].
- Long-term memory and memory poisoning: [[agent-memory]].
- Prompt injection defenses for retrieved content: [[prompt-injection-defense]]; the threat model and lethal trifecta: [[agent-threat-model]].
- Agent identity and delegation models: [[agent-identity-and-least-privilege]].
- Eval suite construction and judge calibration in general: [[building-agent-eval-suites]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No published production measurement of unsupported- or unauthorized-citation rates in enterprise agents was found; the Ostrell audit is illustrative. Replace with documented experience if one appears.
- Citation-support rates (ALCE, 2023) and legal-tool hallucination rates (2024) predate current models; no 2026 replacement was verified.
- *Mata v. Avianca* is cited from secondary sources; the primary opinion was not fetched in this session.

## Decision log

- **2026-10-28** — Framed grounding as four checks (exists, supports, authorized/authoritative, current), generalizing the legal interview design's existence/currency/relevance gate. Three are code-decidable, which pushes model judges onto support only. Rejected a single "groundedness score".
- **2026-10-28** — Adopted retrieval-as-a-tool over pre-retrieval for conversational agents, as labeled author judgement, because no independent comparison exists. Kept "load whole" as a first-class mode for small versioned corpora (Clausewise playbook).
- **2026-10-28** — Reconciled the research design's pinned-snapshot rule with the support design's live, version-keyed cache: every retrieval records the version it read; full-run pinning only where outputs must be reproducible or approved against a fixed basis.
- **2026-10-28** — Used a new local Ostrell story (the February 2027 grounding audit and the April 2027 retrieval redesign) instead of a recurring incident, because no ledger incident covers cross-tenant retrieval or unsupported citations. Facts appended to the ledger.

## Sources

- **Internal**
  - [[context-engineering]], [[provenance-and-freshness]], [[tool-contracts]], [[agent-memory]] — neighbours this chapter builds on and hands to.
  - Interview design examples: `agentic-support-platform` (step `grounding`), `agentic-legal-platform` (steps `grounding`, `citation-gate`), `agentic-healthcare-platform` (steps `grounding`, `calibration`, `safety`, `eval`), `agentic-research-platform` (step `grounding`), `agentic-marketing-platform` (step `grounding`), `ai-coding-cli` (step `context`), `agentic-public-benefits-platform` (technology choices).
- **External**
  - Thakur et al., *BEIR* (2021); Cormack et al., *RRF* (2009); Anthropic, *Contextual Retrieval* (2024) — hybrid retrieval and chunk context.
  - Gao et al., *ALCE* (2023); Min et al., *FActScore* (2023); Rashkin et al., *AIS* (2021) — attribution and claim-level support.
  - Wu et al., *ClashEval* (2024); Zou et al., *PoisonedRAG* (2024) — models defer to retrieved evidence.
  - Magesh et al., *Hallucination-Free?* (2024); *Moffatt v. Air Canada* (2024); *Mata v. Avianca* (2023) — the cost of ungrounded statements.
  - Lei et al., *Spider 2.0* (2024); Yang et al., *SWE-agent* (2024); Li et al. (2024); Asai et al., *Self-RAG* (2023) — retrieval-mode evidence.
  - OWASP LLM08:2025; PromptArmor Slack AI (2024); CVE-2025-32711 — permission-aware retrieval.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: aligned conversation-level "turns" to exchanges or replies (ruling 19); citations spot-checked, no number changed. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
