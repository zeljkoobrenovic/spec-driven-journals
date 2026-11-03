---
status: accepted
revised: 2026-10-28
---

# Spec: Cost, Model Selection and Routing

## Intent

Give the reader a way to say what an agentic task costs and to bound it. The chapter replaces "cost per token" with **cost per successful task** (all attempts, retries, fan-out, oversight and repair divided by successful outcomes), treats model choice as a per-step, evaluated decision (static tiers, routers, **model cascades**), and makes **run budgets** and **cost attribution** runtime and gateway controls that terminate work rather than report on it. After reading, an architect can design the metric, the routing and the budget hierarchy for an agent and defend them to a CFO and a risk owner.

## Audience

Architects, principal engineers and platform leads who run or fund agents and must answer "what does one resolved task cost, and what stops a run from spending without limit?" They know cloud cost management; they need the agent-specific cost anatomy and controls.

## Success criteria

- [x] Reader can list the cost components of an agentic task and explain why re-read input and fan-out dominate, with dated evidence (Anthropic 2025 multipliers, Manus 2025 ratio) and labeled arithmetic.
- [x] Reader can define cost per successful task, including what counts as success (correct abstention counts), agent-side vs blended cost, and where repair costs are booked.
- [x] Reader can choose between static per-step tiers, routers and cascades, knows the evidence for and against (FrugalGPT, RouteLLM, *AI Agents That Matter*, HAL), and the rule that routing pays only with a reliable quality signal.
- [x] Reader can design a run budget (tokens, money, wall-clock, depth, fan-out) that terminates and holds, and a budget hierarchy up to the provider spend cap.
- [x] Reader can specify the attribution attributes needed to join cost to outcome and re-price history.
- [x] The Ostrell worked example computes cost per resolved Answerdesk conversation and a routing evaluation with labeled assumptions; the Weekend Fan-out is replayed under budgets with ledger numbers.
- [x] All prices are dated and volatile; no model version is named as a recommendation.

## Non-goals

- Prompt caching mechanics, prefix stability and context budgets — [[caching-and-context-budgets]].
- Latency budgets, rate limits as throughput ceilings and capacity planning — [[agent-latency-and-throughput]].
- The gateway's general responsibilities — [[models-and-the-model-gateway]].
- When multi-agent designs are justified — [[single-and-multi-agent-designs]]; delegation contracts — [[coordination-and-handoffs]].
- Evaluation method, pass^k and graders — [[evaluating-agentic-systems]], [[building-agent-eval-suites]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No public, dated production writeup reports an agent's cost per task, routing mix and cache hit rate together; the chapter uses Ostrell arithmetic. Replace with documented experience if one appears.
- No dated public postmortem of a runaway agent-cost incident was found; revisit.
- Should the toolkit carry a "cost per successful task" worksheet? Proposed for [[toolkit]].

## Decision log

- **2026-10-28** — Made cost per successful task, not cost per token or request, the organizing metric, because the evidence (*AI Agents That Matter*; Klarna's 2025 qualification) shows cost-only optimization hides quality loss.
- **2026-10-28** — Reported both agent-side and blended cost in the Answerdesk example; the blended figure shows human escalation dominates, which is the chapter's main surprise.
- **2026-10-28** — Kept prices as ranges and ratios with access dates and avoided naming model versions; only the 100× tier spread (Anthropic pricing page) and Google's scheduled price increases were re-verified on 2026-10-28.
- **2026-10-28** — Placed the run budget in the runtime's durable state, not only in gateway counters, so spend survives resume (consistent with [[durable-agent-execution]] and the hold-not-drop kill-switch rule).

- **2026-10-28** — Made the routing evaluation's profile B the same change as the Answerdesk latency redesign in [[agent-latency-and-throughput]] (Mid-tier decide-or-answer replacing the Large planning call), and used Scout's run budget from [[single-and-multi-agent-designs]], so the three Part III/IX chapters tell one story.

## Sources

- **Internal**
  - [[models-and-the-model-gateway]], [[agent-runtime]], [[evaluating-agentic-systems]], [[agent-observability]], [[retries-idempotency-and-concurrency]] — neighbouring mechanisms.
  - `_research/brief-performance-economics-evolution.md` (§1.1–1.5, 1.7), `_research/brief-evaluation-observability.md` (§1.3, 2.1, 5.1), `_research/brief-orchestration-multi-agent.md` (§3.3), `_research/brief-domains-regulation.md` (§6.2).
  - Interview designs: agentic-platform-foundations (`capacity`), agentic-support-platform (`live-loop`), ai-coding-cli (`inference`), ai-coding-harness (`capacity`), agentic-healthcare-platform (`capacity`, step 3), agentic-research-platform (`capacity`).
- **External**
  - Kapoor et al., *AI Agents That Matter* (2024) and *Holistic Agent Leaderboard* (2025) — cost-controlled evaluation.
  - Chen, Zaharia, Zou, *FrugalGPT* (2023); Ong et al., *RouteLLM* (2024) — cascades and routers.
  - Anthropic, *How we built our multi-agent research system* (2025) — token multipliers and economics of fan-out.
  - Anthropic, Google and OpenAI pricing, caching, rate-limit and SDK docs (accessed 2026-10) — dated price dimensions and budget defaults.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: re-verified all October 2026 prices (Anthropic, OpenAI, Gemini pricing pages, 2026-10-28) and removed the unverified markers; dropped the unverified OpenTelemetry "moved in May 2026" clause; Weekend Fan-out replay now ends "within half an hour of starting, on the Saturday" (41 h before Monday morning); "turn" to "exchange" where ruling 19 applies. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
