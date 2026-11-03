---
status: accepted
revised: 2026-10-28
---

# Spec: Building Eval Suites: Datasets, Graders and Regression Gates

## Intent

Chapter 32 turns the evaluation levels of [[evaluating-agentic-systems]] into machinery that runs on every change. Readers learn how to source and label cases, build resettable environments (tool twins, fault injection, user simulators), design a grader stack in which code checks what code can check and model judges are calibrated, versioned components, and wire the results into statistical regression gates. Those gates are triggered by any change to the agent version manifest and backed by a daily canary on production. The chapter owns **eval suite**, **grader**, **LLM-as-judge** and **regression gate**. The Ostrell thread is the Closewise accrual suite, rebuilt after the Alias Drift, and the Answerdesk simulator.

## Audience

Architects, evaluation leads and senior engineers who must make an agent's quality evidence trustworthy enough for a risk owner to sign off on. They know CI and testing, and they do not need the definition of a benchmark. They need to know where suites deceive and how to stop that.

## Success criteria

- [ ] Reader can name the five case sources, the blind spot of each, and why labels need adjudication and agreement measurement.
- [ ] Reader can design an environment that grades end state, injects tool faults and keeps graders and answers out of the agent's reach, with cited evidence of grader exploitation.
- [ ] Reader can apply "outcomes for success, invariants for constraints", and the chapter reconciles the Anthropic, OpenAI and interview-design positions on trajectory grading.
- [ ] Reader can calibrate an LLM judge: atomic rubric, reference, different family, both orders, chance-corrected agreement against a human ceiling, pinned versions, advisory before blocking. Dated research on judge biases supports each step.
- [ ] Reader can specify a gate with manifest-wide triggers, k trials, paired comparison, pre-registered thresholds, hard vs soft criteria and a daily canary.
- [ ] Ostrell worked example: the Closewise v2 suite (1,244 cases, the gate, canary arithmetic showing day-one detection of the Alias Drift) and Answerdesk simulator validation. The numbers agree with the ledger.
- [ ] The chapter includes a failure-scenario table (detection, containment, recovery), a trade-off table, an Across Domains table, at least two mermaid diagrams, the Chief Architect's view and Questions to ask.
- [ ] The chapter says where the evidence stops: no published link from offline scores to incident rates, and no bias measurements for current judges.

## Non-goals

- Evaluation levels, pass^k definition and public benchmark critique in depth: [[evaluating-agentic-systems]].
- Trace capture, redaction, replay and operational metrics: [[agent-observability]].
- Promotion criteria, shadow mode and demotion triggers: [[evidence-for-autonomy]].
- The manifest itself and alias policy: [[versioning-agent-systems]]; canary rollouts: [[staged-rollout-and-rollback]].
- Injection defenses (only the test cases appear here): [[prompt-injection-defense]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Should the platform mandate a minimum judge-vs-human kappa, or leave it to risk owners per suite?
- Is there published evidence on how user simulators compare with real customers for enterprise support agents? None was found as of October 2026.
- When the canary pages, how far should demotion be automated? This is deferred to [[evidence-for-autonomy]].

## Decision log

- **2026-10-28** — Adopted invariants as the default trajectory grader, with the interview design's match modes only where order is a requirement. This reconciles Anthropic's "grade outcomes, not paths" with OpenAI's tool and handoff evaluation.
- **2026-10-28** — Made the Alias Drift the opening, because it exposes the trigger gap (no deploy, no gate) and the convenience-sample gap together. The rebuilt suite's first run (95.2%, not 96.1%) shows the second gap.
- **2026-10-28** — Kept judge-bias magnitudes in a dated table with limitations, not in the prose, because they come from 2023–2024 judges.
- **2026-10-28** — Did not name current model versions. HealthBench's grader is described only as "a model grader".

## Sources

- **Internal**
  - [[evaluating-agentic-systems]], [[versioning-agent-systems]], [[agent-observability]], [[evidence-for-autonomy]], [[sandboxes-and-execution-environments]], [[tool-contracts]].
  - `_research/brief-evaluation-observability.md` (Parts 1–4), `_research/digest-platform-and-coding.md`, `digest-customer-facing.md`, `digest-back-office.md`, `digest-high-stakes-and-research.md`.
  - Interview designs: agentic-platform-foundations (`eval-obs`), ai-coding-harness (`review-agents`, `scale`), ai-coding-cli (`cloud`), support (`compliance-eval`), sales, marketing (`eval`), finance (`exceptions`), legal (`workflows-eval`), healthcare (`eval`), public benefits (`compliance-eval`).
- **External**
  - Anthropic, *Demystifying evals for AI agents* (2026). Vocabulary and suite practice.
  - Zhu et al., *Agentic Benchmark Checklist* (2025). Grader flaws and the null-agent result.
  - Zheng et al. (2023), Thakur et al. (2024) and Arora et al., *HealthBench* (2025). Judge evidence.
  - Shankar et al. (2024). Criteria drift.
  - Miller (2024). Statistics for gates.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: daily canary now 3 trials per case (aligned with [[evaluating-agentic-systems]]), clustered-error arithmetic adjusted; injection suite described as the Poisoned Ticket plus 1,200 variants with a fixed 200-case stratified gate sample (consistency ruling 26); τ²-bench drop stated as the two reported models (18 and 25 points). *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
