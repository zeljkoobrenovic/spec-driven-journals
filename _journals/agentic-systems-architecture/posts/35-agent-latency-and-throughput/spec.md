---
status: accepted
revised: 2026-10-28
---

# Spec: Latency and Throughput

## Intent

Show the reader where an agent's time goes and how to make it fast enough for its interaction mode without trading away safety. The chapter replaces "make the model faster" with three architectural tools: a **latency budget** per user-visible milestone and interaction mode, enforced by a propagated deadline; the **critical path** of an agent run, shortened by removing serial model calls and moving read-only work into parallel or speculative branches and side effects into durable execution; and the **rate-limit ceiling**, the tightest of the shared provider, gateway, downstream and human limits, managed by quota pools, priority classes and admission with expiry. After reading, an architect can decompose an exchange, allocate a budget and size a workload against shared quota.

## Audience

Architects, principal engineers and platform leads who run interactive and background agents on shared model quota, and product owners who must set response-time targets. They know request latency, queues and rate limiting; they need the agent-specific mechanics (TTFT, output tokens, reasoning tokens, dynamic critical paths, cache-aware limits) and the decisions that follow.

## Success criteria

- [ ] Reader can decompose a model call (queueing, prefill/TTFT, output tokens ÷ OTPS) and an exchange (one user message and reply: serial turns of model and tool calls, retries; ruling 19) and explain why output tokens and serial calls dominate.
- [ ] Reader can define latency budget, critical path and rate-limit ceiling, and set milestone budgets per interaction mode (requirements table across Ostrell's agents).
- [ ] Reader can apply deadline propagation, parallel read-only tool calls, speculative reads, streaming with gated commitments and asynchronous side effects, and knows which are unsafe for side effects.
- [ ] Reader can compute a workload's rate-limit ceiling from per-exchange uncached tokens and pool limits, and explain how the cache hit rate moves it (Answerdesk worked example).
- [ ] Reader can design admission control: quota pools per workload class, priority, deadlines on queued work, one retry layer, spend-cap vs rate-limit 429s.
- [ ] Chapter includes a failure-scenario table, a trade-off table ordered by preference, an Across Domains table, three mermaid diagrams, and labels every Ostrell number as fictional and every interview figure as a design example.
- [ ] Reader will not treat a latency fix as behavior-neutral or a latency target as a reason to skip policy checks or raise autonomy.

## Non-goals

- Cost per task, model cascades and run budgets as money: [[agent-cost-and-model-routing]].
- Prompt caching mechanics, prefix layout and context budgets: [[caching-and-context-budgets]].
- Idempotency and unknown-outcome handling in depth: [[retries-idempotency-and-concurrency]].
- Whether to add sub-agents at all: [[single-and-multi-agent-designs]]; router design: [[routing-and-delegation]].
- Run lifecycle and budget enforcement mechanics: [[agent-runtime]]; trace design: [[agent-observability]].
- Inference-server engineering (batching, KV-cache management, speculative decoding implementation).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No public, dated production report gives an agent's per-step latency breakdown and rate-limit headroom; revisit if one appears.
- Whether providers' fast tiers use speculative decoding is undocumented.
- Speculative actions research does not say how irreversible actions are handled; the chapter restricts speculation to reads and staged drafts by judgement.

## Decision log

- **2026-10-28** — Framed the Ostrell thread around a new local incident (the Close-Day Queue, 2 November 2027) where batch and evaluation work exhausted shared quota, so that throughput and latency are taught as one problem.
- **2026-10-28** — Budgets are per milestone (first visible content, answer complete, action outcome), not one number; a progress line counts only if deterministic code emits it from a real step.
- **2026-10-28** — Adopted the agentic-platform-foundations `capacity` overload rules (priority classes, deadline expiry, 429 + Retry-After shedding) and the agentic-support-platform `live-loop` deadline-and-fallback shape as design examples; added the rule "never wait out a rate limit inside an interactive exchange".
- **2026-10-28** — Avoided naming model versions; vendor latency facts are dated October 2026 and stated as mechanisms.

## Sources

- Internal: [[agent-runtime]], [[models-and-the-model-gateway]], [[agent-interaction-design]], [[agent-cost-and-model-routing]], [[caching-and-context-budgets]], [[retries-idempotency-and-concurrency]], [[side-effects-and-external-actions]], [[evidence-for-autonomy]].
- Interview designs: `agentic-support-platform` (step `live-loop`), `agentic-platform-foundations` (step `capacity`), `ai-coding-cli` (capacity), `agentic-healthcare-platform`, `agentic-legal-platform`, `agentic-sales-platform`, `agentic-public-benefits-platform` (capacity).
- External: Dean and Barroso, "The Tail at Scale" (2013); Kim et al., LLMCompiler (ICML 2024); Leviathan et al., speculative decoding (ICML 2023); Ye et al., speculative actions (2025 preprint); Google SRE book (2016); AWS timeouts guidance (2019); Anthropic rate-limit, parallel tool use, fast mode and batch docs and multi-agent research post (2025); OpenAI latency guide; OpenTelemetry GenAI conventions (2026).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: aligned "turn" to "exchange" per ruling 19 throughout (definition, code sketch, budgets, ceiling in exchanges per second); Close-Day Queue containment aligned to the ledger (canary stopped, reclassification deferred by the controller's office); reconciled the 78% peak cache hit rate with July's 76% monthly read share; corrected the workspace-limit quote and the thinking-off wording; speculative-actions venue claim removed (not on arXiv). *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
