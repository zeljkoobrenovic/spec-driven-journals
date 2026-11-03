---
status: accepted
revised: 2026-10-28
---

# Spec: Planning and Task Decomposition

## Intent

Give architects a decision rule for planning in agentic systems. When should a system plan explicitly, who should write the plan (code, a person or a model), and how is the plan checked, approved, executed and revised? The chapter's central claim is that a plan is valuable to the architecture only when it is data: typed, versioned, validated by deterministic code, bound to approvals by content hash, executed by a code dispatcher, and revised only through bounded, triggered replanning. The evidence (planning benchmarks, LLM-Modulo, multi-agent failure taxonomies, engineering reports) supports "the model proposes, code checks". The Ostrell thread contrasts Scout's model-written research plan, rebuilt after the Weekend Fan-out, with Closewise's code-authored close plan.

## Audience

Software architects, principal engineers and technical leads who design or review agents whose runs are long, costly or end in side effects. They should leave able to choose a plan author per agent, specify a plan schema and validator, set replan triggers and limits, and explain why plan approval is not action approval.

## Success criteria

- [ ] Reader can distinguish implicit planning, an explicit plan, and plan-as-data, and say what each lets the architecture do.
- [ ] Reader can choose who writes the plan for a given agent using the authorship ladder and the "could a competent person write it before seeing the input" test.
- [ ] Reader can list the validation checks (schema, referential, policy, structural limits, budget, coverage, critique) and say which are deterministic and fail-closed.
- [ ] Reader can name replanning triggers, the limit and abandon path, and why replans never re-run completed side effects.
- [ ] Reader can explain why approvals bind to the plan hash and why plan approval does not replace per-action approval.
- [ ] Every research number states what was measured, its setting and its age; the Ostrell worked example matches the ledger (Weekend Fan-out: 41 h, 1,900 runs, 310M tokens, €8,700; depth 2; 8 parallel).
- [ ] The Across Domains section shows how plan authorship moves from model to code and rules as stakes rise.

## Non-goals

- Routing steps to models, agents or humans, and delegation contracts — [[routing-and-delegation]].
- Whether steps should run in separate agents; multi-agent topologies and their cost — [[single-and-multi-agent-designs]].
- Handoff payloads and agent-to-agent protocols — [[coordination-and-handoffs]].
- Durable storage, checkpoints and resume semantics — [[task-state-and-checkpoints]], [[durable-agent-execution]].
- Prompt-injection defenses in depth — [[prompt-injection-defense]].
- Bounded loop budgets and stop conditions in general — [[workflows-loops-and-autonomous-agents]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No 2025–2026 head-to-head comparison of explicit and implicit planning with current reasoning models was found; revisit when one appears.
- The replan-rate threshold ("about one replan per run") is an assumption; it needs measurement on real agents.
- No public incident attributes a production failure specifically to agent planning; add one if it is published.

## Decision log

- **2026-10-28** — Made plan-as-data the chapter's spine instead of surveying planning techniques. The 2023 technique numbers are on superseded models; the architectural separation of plan, validation and dispatch is what lasts.
- **2026-10-28** — Separated plan approval (scope and cost) from action approval (each consequence), following consistency ruling 6 on hash-bound approvals with expiry and invalidation. This avoids the reading that an approved plan pre-approves its side effects.
- **2026-10-28** — Used the Weekend Fan-out re-run as the worked example and made "workers return amendments, they do not spawn" the structural fix. Ruling 12 says multi-agent research decomposition is not in the interview sources, so the Scout design rests on the orchestration brief.
- **2026-10-28** — Kept model critique of plans as advisory only. The evidence (Valmeekam et al.; Kambhampati et al.; Huang et al.) shows gains from external verifiers, not self-verification.

## Sources

- **Internal**
  - [[workflows-loops-and-autonomous-agents]], [[agent-runtime]], [[autonomy-and-consequence]] — bounded loop, runtime, action classes.
  - [[routing-and-delegation]], [[single-and-multi-agent-designs]], [[task-state-and-checkpoints]] — neighbours this chapter hands to.
  - Interview designs (design examples): `agentic-research-platform` (steps 3–4, structured protocol IR and hash-bound authorization), `agentic-finance-platform` (step 3, deterministic pipeline), `agentic-public-benefits-platform` (steps 3–4), `ai-coding-harness` (step `behaviour`), `ai-coding-cli` (steps `agent-loop`, `compaction`).
  - `_research/brief-orchestration-multi-agent.md`, `_research/brief-foundations-autonomy.md`, `_research/brief-security-oversight.md`, `_research/brief-context-memory-state.md`.
- **External**
  - Yao et al., *ReAct* (2022); Xu et al., *ReWOO* (2023); Kim et al., *LLMCompiler* (2023) — the planning family.
  - Valmeekam et al. (2023, 2024); Kambhampati et al., *LLM-Modulo* (2024); Xie et al., *TravelPlanner* (2024); Hao et al. (2024) — planning ability and external verification.
  - Cemri et al., *MAST* (2025); Kim et al., *Scaling Agent Systems* (2025–26) — failure modes and decomposability.
  - Anthropic engineering posts (2025) on the research system and long-running harnesses — plans persisted outside context; premature completion.
  - Beurer-Kellner et al. (2025); AgentDojo (2024) — plan-then-execute as an injection defense.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: corrected the quoted wording from Anthropic's long-running-harness post after checking the source. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
