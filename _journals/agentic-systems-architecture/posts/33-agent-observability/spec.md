---
status: accepted
revised: 2026-10-28
---

# Spec: Observability: Traces, Metrics and Investigating Failures

## Intent

Show what an agentic system must record so that it can be operated and its failures investigated. Agent failures rarely raise errors: the run completes, the tool returns success and the outcome is wrong, sometimes because something changed upstream with no deploy. The chapter defines the agent trace and its spans, separates the trace from the evidence log and the durable execution history, sets rules for capturing versus referencing content, defines outcome-first operational metrics and agent-specific alerts, and gives an investigation workflow with a safe definition of replay. After reading, an architect can specify a telemetry design for an agent platform and defend its privacy, cost and failure behavior.

## Audience

Software architects, platform engineers and technical leaders who build or run an agent platform or an agent on one. They know distributed tracing, OpenTelemetry basics and SLO alerting. They need the agent-specific parts: which spans and attributes matter, what to keep out of telemetry, which signals catch silent behavior change, and how to investigate a run without repeating its side effects.

## Success criteria

- [ ] Reader can list the span kinds of an agent trace and the attributes each must carry, including the resolved model id taken from the provider's response.
- [ ] Reader can explain how trace, evidence log and durable execution history differ in completeness, content, retention and failure behavior, and how they are joined by run id and action id.
- [ ] Reader can state the status of the OpenTelemetry GenAI conventions (Development, moved repository, dated) and why agent code should use a thin attribute layer.
- [ ] Reader can decide per field what goes on a span, what goes in a content store by reference, and what is never kept, with reference to GDPR minimization and EU AI Act Art. 12 and 26(6).
- [ ] Reader can design tail-sampling rules for agents and explain why metrics are computed before sampling.
- [ ] Reader can distinguish invariant, outcome-shift and budget alerts and size an outcome alert for a low-volume agent.
- [ ] Reader can distinguish recovery, deterministic and counterfactual replay and ensure a replay never reaches a live system.
- [ ] Reader sees the Alias Drift investigation worked end to end with ledger numbers and the Wake changes that followed.

## Non-goals

- The evidence log's design, policy enforcement points and audit duties — [[policy-enforcement-and-audit]].
- Evaluation levels, eval suites, graders and regression gates — [[evaluating-agentic-systems]], [[building-agent-eval-suites]].
- How evidence changes autonomy tiers — [[evidence-for-autonomy]].
- Version pinning, the alias ban and manifests — [[versioning-agent-systems]]; rollout and rollback — [[staged-rollout-and-rollback]].
- Durable execution and recovery replay mechanics — [[durable-agent-execution]].
- Cost and latency analysis — [[agent-cost-and-model-routing]], [[agent-latency-and-throughput]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The OpenTelemetry GenAI conventions had no tagged release as of 2026-10-28; attribute names in the code sample need re-checking at each edition.
- No published evidence links production telemetry practices to measured incident detection times for agents; the alerting recommendations are judgement.
- Automated failure attribution results (Who&When) date from early 2025 models; revisit if newer measurements appear.

## Decision log

- **2026-10-28** — Used the Alias Drift as the spine because it is an incident with no deploy and no error, which isolates what is agent-specific about observability; the Poisoned Ticket and Weekend Fan-out appear only as alerting lessons.
- **2026-10-28** — Defined three records (trace, evidence log, execution history) with different failure behavior, following consistency rulings 4 and 16 and the agentic-platform-foundations design; rejected a single "audit trace" store.
- **2026-10-28** — Defined replay as three operations with different guarantees, rather than one, because framework documentation uses the word for opposite behaviors (Temporal-style recovery vs LangGraph re-execution).
- **2026-10-28** — Adopted the OTel content-by-reference pattern and presented the three conflicting vendor defaults as evidence that capture must be decided per field.

## Sources

- **Internal**
  - [[policy-enforcement-and-audit]], [[versioning-agent-systems]], [[evidence-for-autonomy]], [[building-agent-eval-suites]] — neighbouring contracts.
  - `_research/brief-evaluation-observability.md` (Part 5, 3.3, 4.2), `_research/brief-performance-economics-evolution.md` (2.2–2.4), `_research/brief-security-oversight.md` (5.1, 6.3), `_research/brief-reliability-recovery.md` (replay engines).
  - Interview designs: `agentic-platform-foundations` steps `durable`, `eval-obs`; `agentic-support-platform` step `compliance-eval`; `agentic-sales-platform` `technologyChoices` Observability.
- **External**
  - OpenTelemetry GenAI semantic conventions repository (Development, accessed 2026-10) and the Collector tail sampling processor README.
  - Zhang et al. 2025 (Who&When), Cemri et al. 2025 (MAST), Kapoor et al. 2025 (HAL), Thinking Machines 2025 (nondeterminism).
  - Anthropic postmortem 2025-09-17; METR 2026-10-06; OpenAI Agents SDK and Claude Code monitoring docs; Google SRE Workbook ch. 5.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: rejection rate described as ~11% from working day 1 (ledger); controller rework stated as 165 of 1,498 proposals rejected, about 105 above baseline (from [[policy-enforcement-and-audit]]), replacing an unsupported "roughly 90". *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
