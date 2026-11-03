---
status: accepted
revised: 2026-10-28
---

# Spec: Durable Execution for Long-Running Agents

## Intent

Show architects how to run agent work that lasts minutes, hours or weeks through crashes, deploys and waits for people, without repeating side effects or re-asking the model. The chapter maps the agent loop onto a durable execution engine (loop as deterministic workflow code, model calls and tool calls as separate recorded activities), then works through the four operational questions a long run raises: what re-runs after a crash, what holds a run's place during a wait, what happens to running runs on a deploy, and what cancellation stops and reports. It also says plainly when a simple job queue is enough. After reading, an architect can choose an execution substrate per class of run and review an agent runtime's recovery semantics.

## Audience

Architects, principal engineers and platform leads who build or review agent runtimes and must defend their recovery behavior to risk owners (controllers, support leads, casework managers). They know distributed systems, queues and event sourcing; they need the agent-specific consequences (model variance on replay, history growth, version pinning of models and prompts).

## Success criteria

- [ ] Reader can define durable execution, activity, heartbeat and cancellation of an agent run, and distinguish cancellation from termination and from compensation.
- [ ] Reader can state the four mapping rules and explain why a model call and the tool call it proposes must be separate activities.
- [ ] Reader can set the activity clocks (schedule-to-start, start-to-close, heartbeat, schedule-to-close, run deadline) for a long-tail model call, and explains why heartbeat progress is not a duplicate guard.
- [ ] Reader can design a wait with a timer, an escalation and a post-wait revalidation consistent with the book's approval rule.
- [ ] Reader can explain version pinning of the whole manifest per run, draining, patching and continue-as-new, and the history-size limit agent loops hit first.
- [ ] Reader can choose between request-scoped runs, a job queue, a checkpointing framework, a replay engine and a declarative state machine, with the "what does a restart cost" test.
- [ ] The Ostrell worked example (September 2027 close) agrees with the ledger: 23 entities, ~1,900 proposals, working day 5, the January Half-Posted Accrual numbers, version pinning since September 2027.
- [ ] Every engine claim is dated and sourced; the absence of production base-rate evidence is stated.

## Non-goals

- Idempotency keys, retry budgets, the different-second-answer problem in retries, leases and concurrency: [[retries-idempotency-and-concurrency]].
- Compensation, sagas, kill switch and quarantine: [[partial-failure-and-compensation]].
- The task-state model, checkpoint granularity, resume vs replay as a concept: [[task-state-and-checkpoints]].
- Run lifecycle and loop mechanics: [[agent-runtime]].
- Approval design and approver UX: [[human-oversight-and-bounded-autonomy]]; manifest versioning and rollout: [[versioning-agent-systems]], [[staged-rollout-and-rollback]].
- A tutorial for any engine.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No published study measures how often production agents duplicate or diverge side effects on recovery; revisit if one appears.
- Engine "durable agent" integrations change quickly (as of October 2026, Temporal's OpenAI Agents SDK integration records model calls but not plain tools); re-verify before a revision.
- Whether pause/suspend by an operator should be a first-class run state distinct from a held wait; left to [[agent-runtime]].

## Decision log

- **2026-10-28** — Made "separate model and tool activities" the central rule rather than "use a durable engine", because the documented engines all run side-effecting steps at least once and the agent-specific risk is re-sampling the model on recovery.
- **2026-10-28** — Used Temporal documentation as the main vocabulary source because it is the most explicit about timeouts, cancellation and versioning; kept Ostrell's engine unnamed per the ledger and contrasted LangGraph, DBOS, Restate, Inngest, Azure Durable Functions and Step Functions.
- **2026-10-28** — Included "when a job queue is enough" as a first-class trade-off (Scout) to avoid presenting durable execution as universal.
- **2026-10-28** — Adopted the interview finance design's period-lock revalidation and the benefits design's appeal-clock timers as design examples; did not adopt the platform design's "exactly-once resume" wording (consistency ruling 4).

## Sources

- **Internal**
  - [[agent-runtime]], [[task-state-and-checkpoints]], [[retries-idempotency-and-concurrency]], [[partial-failure-and-compensation]], [[human-oversight-and-bounded-autonomy]], [[versioning-agent-systems]] — neighbours this chapter builds on and hands to.
  - Interview designs: `agentic-platform-foundations` (step `durable`), `agentic-finance-platform` (steps `pipeline`, `idempotency`), `agentic-public-benefits-platform` (steps `gate`, `audit-appeal`), `ai-coding-harness` (step `lifecycle`).
- **External**
  - Temporal documentation (workflows, activities, timeouts, cancellation, timers, message passing, worker versioning, patching, continue-as-new, limits) — semantics and vocabulary.
  - Microsoft Durable Functions code constraints; AWS Step Functions docs; DBOS, Restate, Inngest, LangGraph docs — contrasting recovery models.
  - Thinking Machines Lab (2025), Anthropic glossary, τ-bench (2024) — model output variance.
  - Anthropic engineering posts (2025) on multi-agent research and long-running harnesses — rainbow deployments; git and progress files as resume state.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: kill switch described as holding work rather than mass cancellation (ruling 10); run state `cancelling` aligned with [[agent-runtime]]; model fallback limited to declared, gated fallbacks; Scout job-queue cost labeled as an assumption. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
