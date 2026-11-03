---
status: accepted
revised: 2026-10-28
---

# Spec: Evaluating Agentic Systems: Components, Trajectories, Workflows, Systems

## Intent

Give the reader a precise answer to "what should be evaluated in an agentic system, at which level, and with what kind of evidence?" The chapter opens Part VIII by defining the four evaluation levels (component, trajectory, workflow, system), the rule for grading outcomes versus trajectories, pass^k as the reliability measure that matches production, and the outcome metric as distinct from activity metrics. It shows from documented evidence why public benchmarks are a model-shortlisting tool and not deployment evidence, and why every result must carry its noise and the versions that produced it. After reading, the reader can design an evaluation system as part of the architecture rather than as a test phase.

## Audience

Software architects, principal engineers and technical leaders who design, review or fund agentic systems and must decide what evidence a change or a launch needs. They know testing and monitoring of conventional services; they need the agent-specific concepts and the architectural requirements evaluation places on the runtime, tool broker and evidence log.

## Success criteria

- [x] Reader can name the four evaluation levels, the question each answers, its grader and cadence, and which Ostrell incident each would have caught.
- [x] Reader can explain the outcome-for-success, trajectory-for-constraints rule and when strict path matching is still right, with the source disagreement (Anthropic vs OpenAI/τ-bench) presented and reconciled.
- [x] Reader can compute and interpret pass^k versus pass@1 and pass@k, including the two-version illustration where equal pass@1 hides different reliability.
- [x] Reader can distinguish an outcome metric from an activity metric and say who should own it.
- [x] Reader can list the documented limits of public benchmarks (flawed graders, null-agent passes, contamination and grader exploitation, cost blindness, infrastructure noise, nondeterminism), each with a dated source and its limitation.
- [x] The Alias Drift worked example uses ledger numbers (96.1% to 89.4%, 4% to 11%, 4 days, 1,900 entries a month) and labels every assumption.
- [x] The chapter includes a requirements table, a failure-scenario table, a trade-off table, the Across Domains table and at least two mermaid diagrams.
- [x] Reader will not mistake this chapter for a guide to building datasets, graders or gates; those are linked onward.

## Non-goals

- Building datasets, simulators, graders, LLM-as-judge calibration and CI regression gates: [[building-agent-eval-suites]].
- Trace design, OpenTelemetry GenAI conventions, replay and operational metrics: [[agent-observability]].
- Promotion criteria, shadow mode, demotion triggers and autonomy reviews: [[evidence-for-autonomy]].
- Version manifests and model deprecations: [[versioning-agent-systems]]; rollout mechanics: [[staged-rollout-and-rollback]].
- Frontier-lab safety frameworks as application gates.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No published, dated evidence links offline agent evaluation scores to online incident rates; revisit if such a study appears.
- Bias magnitudes for 2026-generation model judges are unmeasured in the sources; chapter 32 owns the consequence.
- OpenAI's primary pages on SWE-bench Verified could not be read; the retirement figures are from press reports and should be re-checked against the primary source in a later edition.

## Decision log

- **2026-10-28** — Used four levels (component, trajectory, workflow, system) as the contract names them, rather than the brief's five (adding "outcome"); outcome is treated as an axis of workflow and system evaluation and as the owned "outcome metric", to avoid a level that duplicates workflow.
- **2026-10-28** — Placed trajectory evaluation beside the pyramid rather than as a layer, because invariants run at every level and on 100% of production traffic; reconciled Anthropic's "grade outcomes, not paths" with path-scoring guidance as "outcomes for success, trajectories for constraints".
- **2026-10-28** — Made the Alias Drift the main worked example (component canary vs system outcome metric, with noise arithmetic) and used Forge's Fixture Purge as the counter-case where the outcome grader was gamed; kept the Answerdesk pass^k comparison illustrative and left the promotion decision to [[evidence-for-autonomy]].
- **2026-10-28** — Used METR's June 2026 time-horizon result (verified on metr.org) only to show how scoring of grader exploitation moves a headline number, without naming the model in the prose.

## Sources

- **Internal**
  - [[agentic-reference-architecture]], [[agent-runtime]], [[autonomy-and-consequence]] — where Sounding sits and why bars differ by action class.
  - [[building-agent-eval-suites]], [[agent-observability]], [[evidence-for-autonomy]] — neighbours this chapter hands to.
  - `_research/brief-evaluation-observability.md` — primary factual base.
  - `_research/digest-platform-and-coding.md`, `digest-customer-facing.md`, `digest-back-office.md`, `digest-high-stakes-and-research.md` — design examples.
  - Interview designs: agentic-platform-foundations (`eval-obs`), agentic-support-platform (`compliance-eval`), agentic-finance-platform (`exceptions`), agentic-healthcare-platform (`eval`), agentic-public-benefits-platform (`compliance-eval`), ai-coding-cli (`cloud`).
- **External**
  - Anthropic, *Demystifying evals for AI agents* (2026) — vocabulary, outcome grading, pass^k arithmetic.
  - Yao et al., *τ-bench* (2024) — pass^k definition and policy-violating successes.
  - Zhu et al., *Establishing Best Practices for Building Rigorous Agentic Benchmarks* (2025) — validity properties and benchmark flaws.
  - Kapoor et al., *AI Agents That Matter* (2024) and *Holistic Agent Leaderboard* (2025) — cost, reproducibility, log inspection.
  - Anthropic, infrastructure-noise and BrowseComp eval-awareness posts (2026); METR GPT-5.6 Sol evaluation (2026); Thinking Machines on nondeterminism (2025).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: Closewise component suite aligned to the accrual suite (860 cases in August, 1,244 in v2) and the daily canary to a 300-case subset, 3 trials, alert below 93.5%; close-week volume 380/day stated as a ledger fact; workflow-level k made per-suite (4 for Answerdesk credit policy); Answerdesk pass^8 comparison recast as an undated illustration on revisit scheduling; SWE-bench Verified paragraph corrected (SWE-bench Pro recommendation; audit-pool claim labeled unverified). *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
