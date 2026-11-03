---
status: accepted
revised: 2026-10-28
---

# Spec: Durable Task State and Checkpoints

## Intent

Give the reader a precise model of the state an agent run must keep so it survives a crash, a deploy or a multi-day wait without repeating side effects or re-asking the model for decisions it already made. The chapter owns **task state**, **checkpoint**, **run history** and **resume vs replay**. After reading, an architect can specify a task record, choose checkpoint granularity, tell whether their framework's recovery re-samples the model, and decide where task state lives, how it evolves across versions and how long it is kept.

## Audience

Software architects, principal engineers and platform leads who design or review agent runtimes and agents that act on systems of record. They know workflow engines, event sourcing and outboxes in general; they need the agent-specific consequences (variable model output, long human waits, version skew within a run).

## Success criteria

- [ ] Task state is defined against working context, conversation history, long-term memory and the evidence log, with a single-writer rule (the orchestrator, never the model).
- [ ] The task record's entities (task, plan, step, model decision, action, approval, wait, budget, artifact) are listed with why each exists; the action lifecycle includes an explicit `unknown` state.
- [ ] Resume and replay are defined and the framework terminology clash (Temporal vs LangGraph) is explained with sources.
- [ ] Checkpoint granularity is compared in a table, with the decide/act split as the default and pseudocode showing it.
- [ ] The Ostrell example uses ledger facts (Half-Posted Accrual: 52 entries, crash after 37, 37 duplicates, €2.84 million, 2 days, one-day delay; Closewise on Keelson from April 2027; Alias Drift numbers) and shows an end-to-end resume.
- [ ] A failure-scenario table gives detection, containment and recovery; a trade-off table and the Across Domains table are present.
- [ ] Schema evolution of in-flight runs and retention (GDPR storage limitation; AI Act Art. 19 six-month log minimum) are covered.
- [ ] Every interview-derived design is labeled as a design example with path and step.

## Non-goals

- Durable execution engine internals, timers, heartbeats and cancellation: [[durable-agent-execution]].
- Idempotency-key design, retry budgets, leases: [[retries-idempotency-and-concurrency]].
- Sagas, compensation and kill switches: [[partial-failure-and-compensation]].
- Evidence-log design and audit queries: [[policy-enforcement-and-audit]]; traces and replay for investigation: [[agent-observability]].
- Long-term memory: [[agent-memory]]; working-context assembly and compaction: [[context-engineering]].
- Agent version manifests in depth: [[versioning-agent-systems]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No public production base rate for duplicated or divergent side effects on agent resume exists; revisit if one is published.
- The removed LangGraph "durable execution" concept page could not be re-read; the chapter relies on the persistence, checkpointer and interrupt pages.
- `brief-tools-execution.md` was not available while writing; tool-boundary claims rely on the reliability brief and the digests.

## Decision log

- **2026-10-28** — Defined "resume" as recovery from recorded results and "replay" as deliberate re-execution, and called out that Temporal's "replay" is a resume mechanism. Rejected adopting either framework's vocabulary, because they collide.
- **2026-10-28** — Made the decide/act split (model decision and side effect as separate recorded steps) the default checkpoint granularity, instead of per-step checkpoints, because a mixed step re-samples the model after a partial effect.
- **2026-10-28** — Built the worked example as a deliberate game day on the real close (local details added to the ledger), so the Half-Posted Accrual failure is replayed under the new design with the same numbers.
- **2026-10-28** — Kept run history, evidence log and traces as three separate readers with separate retention, following the platform-foundations design's split and the book's evidence-log rulings.

## Sources

- **Internal**
  - [[agent-runtime]], [[context-engineering]], [[agent-memory]] — neighbouring definitions this chapter builds on.
  - [[durable-agent-execution]], [[retries-idempotency-and-concurrency]], [[partial-failure-and-compensation]], [[policy-enforcement-and-audit]] — where the chapter hands off.
  - Interview designs: `agentic-platform-foundations` (step `durable`, `finalDesign`), `agentic-finance-platform` (steps `ledger`, `idempotency`), `ai-coding-cli` (step `cloud`), `agentic-support-platform` (final architecture), `agentic-healthcare-platform` (step `gate`), `agentic-public-benefits-platform` (step `audit-appeal`).
- **External**
  - Temporal docs (workflows, activities, limits, Continue-As-New, patching) and Temporal's 2025 agent post — the deterministic-coordinator model.
  - LangGraph persistence, checkpointer and interrupt docs — snapshots, durability modes, node-restart rule, replay re-executing LLM calls.
  - Microsoft Learn, Durable orchestrator code constraints (2026) — determinism and code changes breaking replay.
  - Anthropic, "Effective harnesses for long-running agents" (2025) and "How we built our multi-agent research system" (2025) — externalized progress state.
  - Thinking Machines Lab (2025); Yao et al., τ-bench (2024) — nondeterminism of model output and trajectories.
  - Fowler, "Event Sourcing" (2005); GDPR Art. 5(1)(e); EU AI Act Art. 19.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: aligned the store table with agent-memory (model only proposes memory; history kept with audit retention); approval wait aligned with durable-agent-execution's 48-working-hour escalation; Across Domains rows use exchange (ruling 19). *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-28** — Final figure-fix pass: Figure 3 (action lifecycle) corrected: added the Voided to end arrow. *(AI-mediated session)*
