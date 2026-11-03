---
status: accepted
revised: 2026-10-28
---

# Spec: Partial Failure, Recovery and Compensating Actions

## Intent

Show architects what to do when an agent run has caused some of its effects and cannot or should not cause the rest, or finished and was wrong. The chapter must land three ideas. First, partial failure is a state that deterministic code resolves from the run's effect ledger into forward completion, backward compensation or a hold for a human (with "accept and remediate" reserved for a human with business authority); the model never chooses the direction. Second, the saga pattern applies to agents only if compensations are attached to *tools*, because the model picks the steps: every write tool declares reversible, compensable (with its compensating tool, window and approver) or pivot. Third, agent incidents need a kill switch at the policy layer that holds work, quarantine that freezes runs and their outputs, and reverts built as compensation plans. The documented agent incidents of 2025–26 were single destructive actions that only controls outside the agent's reach could recover from.

## Audience

Software architects, principal engineers, platform leads and risk owners who design or approve agents that change external systems. They know sagas and incident response from ordinary systems; they need to know what changes when a model chooses the steps and when "undo" must be designed before an action is exposed.

## Success criteria

- [ ] Reader can distinguish partial failure from ordinary recovery and unknown outcomes, and classify the seven catalogue scenarios (crash mid-batch, lost response, later external rejection, approval expiry, refusal mid-task, budget exhaustion, wrong action found later) by default recovery direction and decider.
- [ ] Reader can define a saga for an agent run (compensable, pivot, retryable at the tool; pivots last and gated; compensations run by the orchestrator in reverse order) and a compensating action (semantic, an action in its own right, no isolation).
- [ ] Reader can specify the registry fields that make compensation a designed tool (`reversibility`, `compensated_by`, `compensation_window`, `compensation_tier`, `outcome_channel`) and explain why pivots are capped at A1 without an exception.
- [ ] Reader can define kill switch (policy layer, scopes, holds not drops) and run quarantine (freeze run and outputs at consumers, preserve evidence) and build a revert from a blast-radius query.
- [ ] The documented incidents are reported with their evidence class and the chapter states plainly that durable execution would not have helped them.
- [ ] The Fixture Purge (9 PRs, 2 merged; noticed Friday 16 July 2027, re-enabled Monday 9 August 2027, consistency ruling 24) and the Half-Posted Accrual (52/37, €2.84 million, 2 days) match the ledger; illustrative counts and drill timings are labeled.
- [ ] The Across Domains table is specific per domain and ends with a judgement on platform machinery versus domain policy.

## Non-goals

- Durable execution engines, activities, heartbeats and cancellation of one run — [[durable-agent-execution]].
- Idempotency keys, retry layers, unknown outcomes and leases — [[retries-idempotency-and-concurrency]].
- Task record design and resume versus replay — [[task-state-and-checkpoints]].
- Action objects, receipts and the external-commitment cap — [[side-effects-and-external-actions]].
- Approval design in depth — [[human-oversight-and-bounded-autonomy]]; release rollback — [[staged-rollout-and-rollback]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No public source measures how often production agents end in partial failure, how often compensations fail, or whether per-tool compensation registries reduce incident cost.
- The PocketOS and DataTalks.Club accounts are founder-sourced; revisit if platform postmortems are published.
- SagaLLM's evaluation details are not stated in its abstract; read the full paper before citing any number from it.

## Decision log

- **2026-10-28** — Put reversibility in the tool registry rather than in workflow definitions, because the model chooses steps at runtime; rejected letting the model generate compensations ("undo what you did"), which reintroduces the different second answer.
- **2026-10-28** — Treated small card refunds as a pivot, departing from the support interview design's "compensatable" small refund (digest note on refund-then-recharge).
- **2026-10-28** — Review: `issue_credit` aligned with [[autonomy-and-consequence]] and [[side-effects-and-external-actions]] as compensable (debit on the next invoice with customer notice), with an A0 compensation tier because the undo is a customer-facing decision; earlier draft called it a pivot.
- **2026-10-28** — Revisited the Half-Posted Accrual as a compensation drill in a staging tenant rather than inventing a second production incident, and used the Alias Drift as the counterexample where A1 approval made compensation unnecessary.
- **2026-10-28** — Framed the documented 2025–26 incidents as pivots exposed at full autonomy, to keep Part VI from reading as "use a workflow engine and you are safe".

## Sources

- **Internal**
  - [[task-state-and-checkpoints]], [[durable-agent-execution]], [[retries-idempotency-and-concurrency]], [[side-effects-and-external-actions]], [[tool-ecosystems-and-mcp]], [[evidence-for-autonomy]], [[provenance-and-freshness]] — neighbouring contracts and Ostrell facts.
  - `_research/brief-reliability-recovery.md` (parts 3, 8, 9, 10), `_research/brief-domains-regulation.md` (Robodebt), `_research/consistency-issues.md` (items 5, 6, 10, 14).
  - Interview designs (design examples): agentic-support-platform (`txn-safety`, `compliance-eval`), agentic-sales-platform (`/v1/fleet/pause`), agentic-finance-platform (`ledger`, `idempotency`), agentic-hr-platform (`service-eval`), agentic-legal-platform, agentic-healthcare-platform (`gate`), agentic-public-benefits-platform (`audit-appeal`), ai-coding-cli, ai-coding-harness.
- **External**
  - Garcia-Molina and Salem, *Sagas* (1987); Microsoft Azure Architecture Center, *Saga design pattern* (2025); Restate, *Sagas guide* (n.d.).
  - Patil et al., *GoEX* (2024, preprint); Chang and Geng, *SagaLLM* (2025, preprint); Zhu et al. (2025) and Cemri et al. (2025) failure taxonomies.
  - Anthropic documentation on streaming refusals and on Claude Code checkpointing (n.d., accessed 2026-10).
  - Press and incident-database accounts of the Replit, Gemini CLI, DataTalks.Club and PocketOS incidents (2025–26).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: Fixture Purge timeline aligned to ruling 24 and [[domain-coding-agents]] (noticed Fri 16 July 2027, held that day, open PRs closed and merged PRs compensated 19 July, re-enabled Mon 9 August on 120 repositories; was 22 July / 2 August / 11 days); `issue_credit` reclassified pivot → compensable (A0 compensation tier) to match chapters 03 and 22; Restate quote corrected; refusal guidance now notes Anthropic's fallback-model recommendation; Robodebt figures matched to the cited source. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
