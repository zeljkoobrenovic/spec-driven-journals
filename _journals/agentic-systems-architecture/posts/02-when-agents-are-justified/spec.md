---
status: accepted
revised: 2026-10-28
---

# Spec: When Agents Are Worth It

## Intent

Give architects a defensible test for when an agentic approach beats a deterministic workflow, a single model call or no model at all. The chapter lands one position: place each decision point on the lowest rung of a five-rung decision ladder (code, single call, workflow with model steps, bounded loop, autonomous agent) that handles the task's real variation, and climb only on evidence, when the path cannot be written in advance, an independent check of the result is cheaper than producing it, and the higher rung beats the rung below on cost per verified outcome. After reading, the reader can reject an Agent-Shaped Hammer in a design review with numbers, and can also recognize the opposite mistake of forcing an open-ended task into a brittle workflow.

## Audience

Software architects, principal engineers and technical leaders who review, fund or build agent proposals. They know distributed systems and cost modeling; they need a vocabulary (ladder, verifiability, error compounding), the evidence on agent reliability and cost, and a procedure they can run in a review.

## Success criteria

- [x] Defines the decision ladder (five rungs, by what the model's output controls), verifiability (cost, independence, timing, coverage) and error compounding (pⁿ, with its limits in both directions and three levers).
- [x] Gives the six placement criteria (input variability, path predictability, value, cost of error, verifiability, latency and cost tolerance) in a table, and says which two do most of the work.
- [x] Presents the ladder test as a diagram, a per-rung requirements table and a rung-justification record with an admissibility check.
- [x] Defines cost per verified outcome with five components (build, run, oversight, evaluation, repair) and links to the cost chapter.
- [x] Evidence section with dated, sourced findings and their limits: TheAgentCompany, τ-bench, Laban et al., CRMArena-Pro, METR horizons and caveats, Kapoor et al. (2024, 2025), Anthropic's multipliers, the METR RCT, Klarna, Moffatt v. Air Canada.
- [x] Ostrell worked example consistent with the ledger: the March 2027 business-case review, Invoice Chaser cancelled (replay and cost table), Peoplepoint leave flow downgraded (compounding arithmetic matching the measured result).
- [x] Anti-cases table, failure-scenario table (detection, containment, recovery), trade-off table, short Across Domains table and judgement.
- [x] Article at or under 8,000 words before Sources.

## Non-goals

- Autonomy tiers, action classes and the consequence–reversibility grid: [[autonomy-and-consequence]].
- Workflow patterns, bounded-loop mechanics, budgets and stop conditions in depth: [[workflows-loops-and-autonomous-agents]].
- Definitions of agent, agent loop, locus of control and action space: [[what-makes-a-system-agentic]].
- Cost per successful task measurement, routing and budgets: [[agent-cost-and-model-routing]].
- pass^k and evaluation levels: [[evaluating-agentic-systems]].
- When to add more agents: [[single-and-multi-agent-designs]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No peer-reviewed study measures agent failure rates in production finance, legal, HR, healthcare or public-benefits work; the domain placement is judgement and should be revisited if such data appears.
- METR stopped actively updating its time-horizon page in September 2026; the horizon caveats may need a newer source.
- The cost-per-verified-outcome components overlap with [[agent-cost-and-model-routing]]; keep this chapter at business-case level and avoid duplicating the measurement detail.

## Decision log

- **2026-10-28** — Framed rungs by what the model's output controls (following Mitchell et al. and Anthropic's workflow/agent split), so a reviewer can check the rung by reading code; kept the rung separate from the autonomy tier, which chapter 03 owns.
- **2026-10-28** — Made verifiability a four-property definition (cost, independence, timing, coverage) rather than a single "is it checkable?" test, because verifier capture (TheAgentCompany renaming, the Fixture Purge) is the failure reviewers miss.
- **2026-10-28** — Presented pⁿ as a teaching device with its optimistic and pessimistic errors and three levers, per the foundations brief, rather than as a law.
- **2026-10-28** — Built the Ostrell example on the ledger's March 2027 review; added local facts (Invoice Chaser volumes, replay results, Peoplepoint leave-flow numbers) and recorded them in the ledger. Included an explicit anti-case for under-agenting so the chapter is not read as "always go lower".

## Sources

- **Internal**
  - [[what-makes-a-system-agentic]], [[autonomy-and-consequence]], [[workflows-loops-and-autonomous-agents]], [[agent-cost-and-model-routing]], [[evaluating-agentic-systems]], [[single-and-multi-agent-designs]] — neighbouring ownership.
  - Interview designs: `agentic-finance-platform` (step `pipeline`), `agentic-public-benefits-platform` (step `rules`), `agentic-support-platform` (step `action-gate`).
  - Research briefs: foundations-autonomy, performance-economics-evolution, evaluation-observability, domains-regulation.
- **External**
  - Anthropic, *Building effective agents* (2024) and *How we built our multi-agent research system* (2025) — workflow/agent split; cost multipliers.
  - OpenAI, *A practical guide to building agents* (2025) — when an agent is warranted.
  - Mitchell et al. (2025) — code-level agency levels.
  - Kapoor et al., *AI Agents That Matter* (2024) and HAL (2025) — simple baselines and cost-controlled evaluation.
  - Xu et al., TheAgentCompany; Yao et al., τ-bench; Kwa et al. and METR notes; Ord (2025); Becker et al. (2025) — reliability, horizons, productivity.
  - Wei (2025) — asymmetry of verification.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: "exchange" for one message and reply (ruling 19); replaced the restated vendor and Mitchell definitions with a link to what-makes-a-system-agentic; shortened *Moffatt* to a pointer; named Kapoor et al.'s "warming" baseline; qualified METR's 1.5–2× sensitivity as applying to the newest model. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
