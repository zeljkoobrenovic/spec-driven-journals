---
status: accepted
revised: 2026-10-28
---

# Spec: Provenance, Freshness and Consistency of What Agents Know

## Intent

Show architects how wrong and stale facts enter an agent's working context, gain authority as they move through outputs, notes, memories and other agents, and become commitments, and give them four mechanisms to contain this: the **provenance envelope** on every fact, the **freshness SLO** per data class measured at the point of use, **re-read before write** at the tool boundary, and lineage recorded at write time so an **invalidation sweep** can find everything a bad fact touched. The chapter closes Part IV by joining context, retrieval, memory and task state into one data-quality argument: freshness and provenance are data contracts enforced by deterministic code, not instructions to the model.

## Audience

Software architects, principal engineers and platform owners who design context assembly, retrieval indexes, memory and commit tools for agents, and the risk owners who must answer "what did the agent know, and when?" after an incident. They know replication, caching and optimistic concurrency; they need the agent-specific propagation and the controls per hop.

## Success criteria

- [ ] Reader can name the three clocks on a fact (valid time, record time, `as_of` confirmation time) and compute age as *use time − as_of*.
- [ ] Reader can specify a provenance envelope schema and say which component writes it (code, never the model) and how it is rendered to the model.
- [ ] Reader can write a freshness register with separate bounds for informing and committing, owners and breach behavior, including the rule that a model-derived artifact is never fresher than its oldest input.
- [ ] Reader can design re-read before write in a commit tool, including version checks, conditional writes and approval voiding on change.
- [ ] Reader can trace the error propagation path hop by hop and name a control and owner chapter per hop.
- [ ] Reader can run an invalidation sweep from lineage and say what happens to drafts, memories, approvals and already-made commitments.
- [ ] The Stale Price Book numbers match the ledger (23 days, 2027-06-01 increase, 14 quotes, €46,000, ≤ 24 h SLO, A3 → A2 in October 2027).
- [ ] The Across Domains table distinguishes what goes stale, the bound, the re-read target and breach behavior per domain, with interview material labeled as design examples.

## Non-goals

- Context assembly, compaction and context budgets ([[context-engineering]], [[caching-and-context-budgets]]).
- Retrieval quality, hybrid search, citation and groundedness checks ([[retrieval-and-grounding]]).
- Memory write policy, memory expiry mechanics and memory poisoning in depth ([[agent-memory]], [[prompt-injection-defense]]).
- Task state, checkpoints and run history ([[task-state-and-checkpoints]]).
- Action objects, receipts, idempotency keys and leases ([[side-effects-and-external-actions]], [[retries-idempotency-and-concurrency]]).
- Compensation of commitments already made ([[partial-failure-and-compensation]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No published evaluation measures whether showing `as_of` headers to a model reduces its use of stale facts; revisit if one appears.
- No production study of stale-fact incident rates in deployed agents was found; the chapter says so.
- Whether the invalidation sweep should run automatically on a source correction or only on request of the data owner (the chapter chooses "on request" for Ostrell).

## Decision log

- **2026-10-28** — Defined age against confirmation time (`as_of`), not record time, and added confirmation time as a third clock beside Fowler's valid and record time; the Stale Price Book is a confirmation-time failure plus a valid-time flattening defect.
- **2026-10-28** — Added a local Ostrell detail (three post-repair drafts at old prices sourced from Dealroom's own account briefs) to make the memory → context propagation concrete and to motivate the A3 → A2 demotion already in the ledger; the 14 sent quotes and €46,000 remain the canonical totals.
- **2026-10-28** — Put enforcement in Bulkhead (decides) and Toolyard (re-reads and writes), following consistency ruling 15; the model sees age headers but they are not a control.
- **2026-10-28** — Adopted the research design's write-time lineage over post-hoc extraction and the sales design's re-check at send, and rejected a platform-wide default between live reads and snapshots in favor of a per-data-class register.

## Sources

- **Internal**
  - [[context-engineering]], [[retrieval-and-grounding]], [[agent-memory]], [[task-state-and-checkpoints]] — the Part IV chapters this one joins.
  - [[side-effects-and-external-actions]], [[retries-idempotency-and-concurrency]], [[human-oversight-and-bounded-autonomy]] — action objects, version checks and approval invalidation.
  - [[caching-and-context-budgets]] — Toolyard cache bounds by data class.
- **Interview design examples** (`system-design-interviews/data/book/`)
  - `agentic-sales-platform` (steps `enrichment`, `send-gate`), `agentic-research-platform` (steps `grounding`, `reproducibility`), `agentic-support-platform` (step `grounding`), `agentic-legal-platform` (steps `grounding`, `citation-gate`), `agentic-healthcare-platform` (steps `grounding`, `gate`), `agentic-public-benefits-platform` (step `grounding`), `ai-coding-cli` (step `compaction`).
- **External**
  - ClashEval (Wu, Wu and Zou, 2024), FreshQA (Vu et al., 2023), snowballing (Zhang et al., 2023), ALCE (Gao et al., 2023), MINJA (2025), PoisonedRAG (2024), CaMeL (2025) — how models adopt and propagate context.
  - W3C PROV-DM (2013), Fowler's bitemporal history (2021), Vogels on client consistency (2008), Google SRE Workbook ch. 13 (2018), RFC 9110 `If-Match` (2022), CWE-367 — the durable data-management base.
  - Anthropic engineering posts on harnesses and multi-agent research (2025); *Moffatt v. Air Canada* (2024).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: cut evidence re-teaching owned by retrieval-and-grounding, agent-memory and context-engineering (ALCE/Citations, MINJA/PoisonedRAG, Anthropic harness post, Moffatt) to one sentence each with links; memory row and Tidemark row aligned with agent-memory (90-day review is Ostrell policy; trust level, not confidence); fixed the meaningless "above tier A3" recommendation; corrected the Zhang et al. quotation. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
