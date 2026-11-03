---
status: accepted
revised: 2026-10-28
---

# Spec: Retries, Idempotency and Concurrency

## Intent

Show architects how to retry safely when the component choosing the next action is a model whose output varies, and when actions change external systems. The chapter must land one separation, *deciding* versus *doing*: the model's proposal is recorded once and frozen into an action object, and everything that retries, replays or resumes works on that object with an orchestrator-minted idempotency key, never on the model. It must also show that idempotency keys stop duplicate retries but not duplicate decisions, so per-entity concurrency guards (business uniqueness keys, version checks, leases with fencing tokens) are a separate, required control. After reading, the reader can place retry owners per layer, size retry budgets, and recognize the different second answer in a design.

## Audience

Software architects, principal engineers and platform leads who design or review agent runtimes, tool brokers and tool contracts. They know idempotency keys, retries with backoff and optimistic locking from ordinary distributed systems; they need to know what changes when a model sits in the retry path and many agent runs act on the same entities.

## Success criteria

- [ ] Reader can name the five retry layers (transport, model call, tool call, step, run), what each regenerates, and assign one retrying owner per hop.
- [ ] Reader can define the different second answer and explain why a key minted from the model's output, or fresh per call, cannot catch it.
- [ ] Reader can design an idempotency key bound to an action object (minted by the orchestrator, recorded before the first attempt, with a parameter fingerprint) and the attempt state machine with `unknown` as a state.
- [ ] Reader can state the book's rule for unknown outcomes: lookup by key, retry only keyed tools proven "not applied", otherwise repair queue; never re-ask the model.
- [ ] Reader can distinguish idempotency keys, business uniqueness keys, version checks and leases with fencing tokens, and choose among them.
- [ ] Reader can define a retry budget at dependency and run scope and relate it to rate limits and backpressure.
- [ ] The Double Credit is told with ledger numbers (30 s timeout, 212 customers, €31,400) and the post-fix design is worked end to end.
- [ ] The Across Domains table is specific per domain and ends with a judgement on platform versus domain policy.

## Non-goals

- Durable execution engines, activities, heartbeats and cancellation in depth — [[durable-agent-execution]].
- Action objects, receipts, dry runs and external commitments — [[side-effects-and-external-actions]].
- Sagas, compensating actions, kill switches and multi-step partial failure — [[partial-failure-and-compensation]].
- Approval semantics in depth — [[human-oversight-and-bounded-autonomy]].
- Cost budgets and model routing beyond retries — [[agent-cost-and-model-routing]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No public source measures how often production agents duplicate side effects on retry or resume; revisit if one appears.
- The IETF Idempotency-Key header is still a draft (-08, October 2026); update the chapter if it becomes an RFC or stalls.
- Whether model providers will offer server-side idempotency or reproducibility guarantees for generation requests (none verified).

## Decision log

- **2026-10-28** — Made "retry the recorded action, never the model" the central rule, rather than presenting retries as an ordinary distributed-systems topic with an agent appendix, because the different second answer is the one mechanism the reader's existing practice misses.
- **2026-10-28** — Added the business uniqueness key as a named guard alongside leases and version checks, because the Double Credit review's parallel-conversation finding shows idempotency keys cannot enforce per-entity limits; rejected treating leases as the default because long model calls make lease expiry during work likely.
- **2026-10-28** — Explained the March 2027 approval as attached to the run step rather than to the action object, which reconciles the ledger's A1 tier for credits with the retried execution and ties the chapter to the book's approval rule (consistency issue 6).
- **2026-10-28** — Kept Ostrell's durable engine unnamed and cited Temporal's documented workflow-id uniqueness as an example of the property, not as Ostrell's product.

## Sources

- **Internal**
  - [[durable-agent-execution]], [[side-effects-and-external-actions]], [[partial-failure-and-compensation]], [[tool-contracts]], [[tool-ecosystems-and-mcp]], [[human-oversight-and-bounded-autonomy]] — neighbouring contracts.
  - `_research/brief-reliability-recovery.md` (parts 2, 4–7, 11) and `_research/consistency-issues.md` (items 4, 5, 6).
  - Interview designs (design examples): agentic-platform-foundations (step `durable`), ai-coding-cli (steps `agent-loop`, `cloud`), agentic-support-platform (step `txn-safety`), agentic-sales-platform (step `send-gate`), agentic-finance-platform (step `idempotency`), agentic-healthcare-platform (step `gate`), agentic-public-benefits-platform.
- **External**
  - Google SRE book (2016) — retry budgets and retry multiplication.
  - Stripe (2017; API reference n.d.), AWS Builders' Library, IETF draft-08 (2026) — idempotency key semantics.
  - Kleppmann, "How to do distributed locking" (2016) — leases and fencing tokens.
  - RFC 9110 (2022) and RFC 6585 (2012) — conditional writes; 429 and Retry-After.
  - Thinking Machines Lab (2025), Anthropic docs, τ-bench (2024), MAST (2025) — output variance and step repetition.
  - Temporal and LangGraph documentation — what recovery re-runs; workflow-id uniqueness.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: credit limits worded per ruling 21 (one service credit per technician visit; one pending credit proposal per ticket); approval re-checked by Bulkhead before dispatch (rulings 6, 15); Half-Posted Accrual linked to its owner; spend-cap 429 wording matched to Anthropic's current errors page. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
