---
status: accepted
revised: 2026-10-28
---

# Spec: Deterministic Workflows, Bounded Loops and Autonomous Agents

## Intent

Give architects a precise vocabulary and a design method for the three execution styles in which model-owned steps run: the deterministic workflow, the bounded loop and the autonomous agent. The chapter lands one position: choose the style per step, default to the least autonomous style that solves the task, and never approve a loop without a limits block (budgets, stop conditions, a completion check in code and an escalation route) that the model cannot change. Most systems should be a workflow skeleton with a few bounded loops inside it. After reading, the reader can register an execution style per step, write the stop-condition set for a loop, size its budgets, and say what a long-horizon run needs before its horizon is raised.

## Audience

Software architects, principal engineers and technical leaders who design or review agentic systems and are choosing between "build it as a workflow" and "let the agent figure it out". They know workflow engines and distributed systems; they need the loop-specific limits, where state lives in each style, and the evidence on how loops fail.

## Success criteria

- [x] Defines deterministic workflow, bounded loop, autonomous agent, budget, stop condition and workflow skeleton, and compares the three styles in a table (locus, duration, variance, state, ending, worst-case cost).
- [x] Covers the five workflow patterns with model steps (prompt chaining, routing, parallelization, orchestrator–workers, evaluator–optimizer) with what code owns and how each fails, and the external-signal condition for evaluator–optimizer loops.
- [x] Gives a budget table (step, tool, token, cost, time, delegation), a stop-condition table with evaluator and next step, a stop-condition state diagram, the exit-to-human requirements, and a typed code sketch of a bounded loop.
- [x] Explains what changes with a long horizon (state outside the context, durable execution, background runs, milestones, reliable horizon), with dated evidence (Anthropic 2025 and 2026, METR) and its limits.
- [x] Presents the two hybrids and the no-bypass rule; tables for state, testability and observability per style, and requirements per interaction.
- [x] Ostrell worked example with ledger-consistent numbers: Closewise loops' limits, Answerdesk's limits and Q3 2027 stop-reason mix, Scout's budget and milestones after the Weekend Fan-out.
- [x] Migration between styles in both directions; failure-scenario table with detection, containment and recovery; trade-off table with a recommendation and its conditions; short Across Domains table.
- [x] Article at or under 8,000 words before Sources.

## Non-goals

- Whether a model-owned step is justified and the compounding arithmetic: [[when-agents-are-justified]].
- Autonomy tiers and action classes: [[autonomy-and-consequence]].
- Runtime internals, run lifecycle and framework choice: [[agent-runtime]].
- Explicit plans and replanning: [[planning-and-decomposition]].
- Topologies and multi-agent evidence: [[single-and-multi-agent-designs]].
- Durable execution engines and replay: [[durable-agent-execution]].
- Budget hierarchy beyond the run, cost per successful task, model routing: [[agent-cost-and-model-routing]].
- Escalation-package user experience: [[agent-interaction-design]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No published study compares one production task built as a workflow, a bounded loop and an autonomous agent; the style recommendations are judgement. Revisit if such a comparison appears.
- Framework defaults for turn and spend limits change often (OpenAI Agents SDK `max_turns`, Claude Agent SDK `max_budget_usd`); re-check before a new edition.
- No public incident report attributes a production failure specifically to a missing stop condition.

## Decision log

- **2026-10-28** — Framed the chapter around "the limits block" (budgets, stop conditions, completion check, escalation route) rather than a pattern catalogue, because a reviewer needs something checkable. The five workflow patterns are kept as one table.
- **2026-10-28** — Defined an autonomous agent as a bounded loop with a long horizon, not a different mechanism, so the book has one loop model; what changes is state, milestones and tree budgets.
- **2026-10-28** — Adopted "skeleton first whenever the side effects can be listed in advance" as the default hybrid, following the finance and platform interview designs and Stripe's 2026 account, and kept the platform design's no-bypass rule.
- **2026-10-28** — Told the Weekend Fan-out from the stop-condition angle (no definition of "done"); topology and cost replays stay in [[single-and-multi-agent-designs]] and [[agent-cost-and-model-routing]]. Added Answerdesk and Closewise loop limits and Answerdesk's stop-reason mix to the scenario ledger.

## Sources

- **Internal**
  - [[what-makes-a-system-agentic]] — decision points, the agent loop, the Closewise map.
  - [[single-and-multi-agent-designs]], [[agent-cost-and-model-routing]], [[durable-agent-execution]] — Scout budgets, run budget check, close walkthrough.
  - Interview designs: `agentic-platform-foundations` (steps `control-flow`, `capacity`), `ai-coding-cli` (step `agent-loop`), `agentic-finance-platform` (step `pipeline`), `agentic-research-platform` and `agentic-public-benefits-platform` (`highLevelArchitecture`), `agentic-healthcare-platform`.
- **External**
  - Anthropic, "Building effective agents" (2024) — definitions and the five workflow patterns.
  - OpenAI, "A practical guide to building agents" (2025) and Agents SDK docs (accessed 2026-10) — exit conditions, `max_turns`.
  - Cemri et al., MAST (2025) — repetition, missed completion and verification failure modes.
  - Shinn et al. (2023); Huang et al. (2023) — self-correction needs an external signal.
  - Anthropic, "Effective harnesses for long-running agents" (2025) and "Measuring AI agent autonomy in practice" (2026); METR time horizons (2025–2026).
  - Stripe, "Minions" (2026) — agent loops interleaved with deterministic code; at most two CI rounds.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: Answerdesk loop limits and budget tables are per exchange, not per turn (ruling 19); Cemri et al. labeled a preprint (venue not verified); METR sensitivity qualified; Anthropic's "turn duration" glossed. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
