---
status: accepted
revised: 2026-10-28
---

# Spec: The Agent Runtime: Running the Loop

## Intent

Define what the component that runs the agent loop must do and must never do. The chapter states a runtime contract: an explicit run lifecycle (nine states, with waiting distinguished from suspension and terminal states carrying outcome codes), a turn pipeline that treats model output as untrusted input (stop-reason handling, validation, read/write partitioning, registry-verified parallelism, one side effect per turn, no action on partial output), an inbox read at turn boundaries and before every side effect, budget admission before calls, and four layers of run isolation. It closes with the build-versus-adopt decision between vendor SDKs, frameworks, a thin loop on a durable engine, hosted services and wrapping an opaque loop. After reading, an architect can review any agent runtime, bought or built, against the contract.

## Audience

Architects, platform leads and principal engineers who build an agent platform or choose a framework or SDK for one, and who must explain to risk owners what happens when a run loops, is interrupted, is cancelled or shares workers with another tenant.

## Success criteria

- [ ] Reader can define agent run, turn (versus exchange), run lifecycle and agent runtime, and distinguish runtime, framework and SDK.
- [ ] Reader can draw the run lifecycle, say who may cause each transition, and explain why suspension is a separate state from waiting.
- [ ] Reader can walk through one turn: stop reasons, validation, parallel reads, one write, intent recording, policy check, denial as a result.
- [ ] Reader can state the inbox rules and explain why voiding an undispatched action is safe while re-asking after dispatch is not.
- [ ] Reader can name the four isolation layers and a failure for each.
- [ ] Reader can choose among build, adopt and wrap options and name the condition for building a platform runtime.
- [ ] Ostrell numbers agree with the ledger (Weekend Fan-out, Double Credit, A2 credits ≤ €250 since October 2027, one revisit per ticket, 24,000-token context budget, Scout budget, 8-second receipt wait).
- [ ] Vendor semantics are dated and sourced; the absence of evidence on steering faults and build-versus-adopt outcomes is stated.

## Non-goals

- Durable execution mechanics (activities, heartbeats, timers, cancellation settlement, versioning in-flight runs): [[durable-agent-execution]].
- The task record, checkpoints, resume versus replay: [[task-state-and-checkpoints]].
- Idempotency keys, retry layers, leases: [[retries-idempotency-and-concurrency]].
- Budget hierarchy and cost attribution: [[agent-cost-and-model-routing]]; latency budgets and streaming UX: [[agent-latency-and-throughput]].
- Delegation contracts and task trees: [[routing-and-delegation]], [[single-and-multi-agent-designs]].
- Tool design and sandboxes: [[tool-contracts]], [[sandboxes-and-execution-environments]].
- A tutorial for any SDK or framework.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No published study measures stale-decision faults from mid-run input or compares runtime steering designs; revisit if one appears.
- Other chapters use "turn" for a conversational exchange in places (latency budgets, compaction); a later consistency pass may want to rename those to "exchange".
- Provider-hosted agent services are described generically; name and date them in a revision once their lifecycle and policy hooks can be verified.

## Decision log

- **2026-10-28** — Made `suspended` a first-class state distinct from waiting, answering the open question left by [[durable-agent-execution]]: only the suspending authority may release a run.
- **2026-10-28** — Defined "turn" as one model call plus its handling (the SDK meaning) and introduced "exchange" for a user message and reply, so turn caps and latency budgets count different units explicitly.
- **2026-10-28** — Adopted "one side effect per turn" and "parallelism only from registry classification" as Ostrell rules, because MCP annotations are untrusted hints and one effect per decision makes the pre-dispatch inbox check possible.
- **2026-10-28** — Used the local "four seconds late" revisit case (May–June 2027, 23 conversations) as the scene, rather than re-telling the Double Credit, which [[retries-idempotency-and-concurrency]] owns.

## Sources

- **Internal**
  - [[durable-agent-execution]], [[task-state-and-checkpoints]], [[retries-idempotency-and-concurrency]], [[agent-cost-and-model-routing]], [[agent-latency-and-throughput]], [[single-and-multi-agent-designs]], [[routing-and-delegation]].
  - Interview designs: `agentic-platform-foundations` (steps `naive`, `runtime`, `capacity`), `ai-coding-cli` (steps `agent-loop`, `safety`, `cloud`), `ai-coding-harness` (step `naive`), `agentic-public-benefits-platform` (step 3).
- **External**
  - Claude Agent SDK agent-loop and subagent docs; Anthropic stop-reason, streaming, parallel tool use and structured-output docs (accessed 2026-10).
  - OpenAI Agents SDK running-agents docs; LangGraph interrupts; Temporal's OpenAI Agents integration (accessed 2026-10).
  - MCP specification 2026-07-28 (tools, annotations).
  - ReAct (2022), τ-bench (2024), MAST (2025), Laban et al. (2025); Anthropic agent-autonomy study (2026).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: idempotency key wording aligned with retries-idempotency-and-concurrency; MCP annotation quote replaced with the verified 2026-07-28 wording; removed an uncited source. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-28** — Final figure-fix pass: Figure 1 (run lifecycle) corrected: added the Waiting for Human to Suspended arrow, labelled Running to Cancelling "cancel accepted", removed the stray arrowhead into Running. *(AI-mediated session)*
