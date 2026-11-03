---
status: accepted
revised: 2026-10-28
---

# Spec: Routing and Delegation

## Intent

Answer the chapter-11 question: how should work be routed to the right model, agent configuration, tool set or human, and what does delegation transfer? The chapter must make two moves the reader can take into a design review. First, a router is a classifier: it needs a labeled evaluation set, per-class recall targets, calibrated probabilities and thresholds derived from a cost matrix of misroutes, plus an explicit "cannot tell" route to humans. A model's self-reported confidence is not a threshold. Second, delegation is a contract enforced by the runtime: task, inputs by reference with trust labels, decisions already taken, attenuated authority, a budget carved from the parent's, an output schema and lineage identifiers. Throughout, the chapter keeps one boundary: routing selects a handler; the policy enforcement point still authorizes every action.

## Audience

Architects and principal engineers who design or review agent platforms and customer-facing agents. They know classifiers, queues and OAuth. They leave able to specify a staged router, write a cost matrix with route owners, and review a framework's delegation defaults against a contract.

## Success criteria

- [ ] Defines router, sub-agent and delegation contract precisely, and distinguishes call-and-return delegation from transfer of control (linking [[coordination-and-handoffs]] for the latter).
- [ ] Separates the four routing dimensions (intent, complexity, risk, cost) and states that risk routing may only move work toward more oversight.
- [ ] Shows expected-cost routing with calibrated probabilities (pseudocode) and cites evidence that verbalized confidence is overconfident.
- [ ] Gives a typed route decision record and a typed delegation contract, with the five enforcement rules (attenuation, carved budget, inputs by reference, explicit decisions, result as data).
- [ ] Works the Answerdesk router end to end with ledger-consistent numbers: the 13 July 2027 misroute, the audit, router v2 and results; and Scout's post-Fan-out delegation limits (depth 2, 8 parallel).
- [ ] Includes a requirements table, a failure-scenario table (detection, containment, recovery), two trade-off tables, the Across Domains table and at least two mermaid diagrams.
- [ ] Labels research findings with what was measured and their limits; dates vendor documentation; labels interview material as design examples; says where the evidence stops.

## Non-goals

- Whether to use several agents at all, topologies and token multipliers: [[single-and-multi-agent-designs]].
- Handoff payloads, peer handoffs, A2A and orphaned tasks: [[coordination-and-handoffs]].
- Plan structure and decomposition: [[planning-and-decomposition]].
- Cost-per-task arithmetic and model-routing economics in depth: [[agent-cost-and-model-routing]].
- Approval semantics and escalation-package UI: [[human-oversight-and-bounded-autonomy]], [[agent-interaction-design]].
- Token exchange and credential brokering in depth: [[agent-identity-and-least-privilege]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No published production evaluation of agent intent routing (per-class recall, calibration, downstream cost) was found; revisit if one appears.
- Framework delegation defaults (depth, concurrency, spend caps, context transfer) are volatile; re-check at each edition.
- Should the cost-matrix pattern be generalized in [[building-agent-eval-suites]] as a standard grader for routers?

## Decision log

- **2026-10-28** — Framed the router as a cost-sensitive classifier rather than as a "triage agent", because the Ostrell misroute shows top-1 accuracy hiding the expensive errors; rejected a single global confidence threshold.
- **2026-10-28** — Chose a staged router (rules → calibrated classifier → LLM router → human) as the recommended default for high-volume intent routing, with "no router, one agent" kept as a valid option.
- **2026-10-28** — Adopted a typed delegation contract over both framework defaults (full history; prompt string only), consistent with consistency rulings 3, 8 and 15 (brokered credentials, abstention, authorization separate from execution).
- **2026-10-28** — Kept action gating out of routing: routes select tool visibility and model tier; Bulkhead decides permission.

## Sources

- **Internal**
  - [[meet-ostrell]], scenario ledger — Answerdesk volumes, Lost Handoff, Weekend Fan-out limits, Keelson components.
  - [[autonomy-and-consequence]], [[policy-enforcement-and-audit]] — tiers and the enforcement point routing must not bypass.
  - Interview design examples: agentic-support-platform (steps `action-gate`, `escalation`), agentic-platform-foundations (`control-flow`), ai-coding-cli (`verify`), agentic-sales-platform (`handoff`), agentic-finance-platform (`exceptions`), agentic-hr-platform, agentic-healthcare-platform (`calibration`), agentic-public-benefits-platform.
- **External**
  - Chen et al., FrugalGPT (2023); Ding et al., Hybrid LLM (ICLR 2024); Ong et al., RouteLLM (2024–25); Hu et al., RouterBench (2024) — model routing evidence.
  - Kapoor et al., AI Agents That Matter (2024) — escalation baseline cost versus accuracy.
  - Xiong et al., confidence elicitation (ICLR 2024) — overconfidence of verbalized confidence.
  - Anthropic multi-agent research system (2025) and postmortem (2025); Cognition (2025, 2026); OpenAI guide (2025) and Agents SDK docs; Claude Agent SDK docs — delegation evidence and defaults.
  - RFC 8693 (2020); GDPR Art. 12(3).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: aligned turn/exchange wording (ruling 19), added RFC 8693 `sub` alongside `act` (ruling 22), replaced a misquoted Cognition phrase with a paraphrase, removed a banned word. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
