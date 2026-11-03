---
status: accepted
revised: 2026-10-28
---

# Spec: Policy Enforcement and Audit

## Intent

Show how to enforce rules outside the model and prove afterwards what an agent did and why. The chapter puts policy enforcement points at four positions on a run's only paths (before the model call, before the tool call, immediately before the side effect, on the output), shows agent policy as code with a release pipeline (unit cases, static analysis, decision replay, manifest binding), states what guardrail models can and cannot carry, and designs the evidence log: record families, write ordering, tamper evidence, retention and erasure, and audit queries. After reading, an architect can place PEPs, specify an evidence-log schema from the questions risk owners will ask, and defend both to security, audit and privacy reviewers.

## Audience

Software architects, platform and security engineers, and technical leaders who build an agent platform or run consequential agents on one. They know access control, policy engines and audit logging in general. They need the agent-specific parts: session-aware policy, the dispatch-time re-check, guardrails as signals, and an evidence log that survives sampling, privacy law and an auditor's question a year later.

## Success criteria

- [ ] Reader can name the four PEPs, the component each lives in, the question each answers and its failure behavior.
- [ ] Reader can explain why authorization and routing are separate steps, and why policy context must be computed by deterministic code.
- [ ] Reader can describe a policy release pipeline with static analysis and a decision-replay diff, using the October 2027 credit promotion.
- [ ] Reader can state the guardrail asymmetry (tighten, never loosen) and cite the measured limits of classifier defenses.
- [ ] Reader can list the evidence log's record families, the intent → execute → receipt ordering, and why raw reasoning is kept apart.
- [ ] Reader can design tamper evidence (hash chain, anchoring, verifier) and reconcile retention with erasure (record classes, reference, crypto-shredding).
- [ ] Reader can map EU AI Act Arts. 12, 19, 26(6) and 86 and the Regulation (EU) 2026/1744 dates to the design.
- [ ] Reader sees the auditor's sample and the Alias Drift question answered with ledger-consistent numbers.

## Non-goals

- The threat catalogue and trust boundaries — [[agent-threat-model]]; injection defenses — [[prompt-injection-defense]].
- Agent identity, delegation and scoped credentials — [[agent-identity-and-least-privilege]].
- Approval gate design, card content and oversight metrics — [[human-oversight-and-bounded-autonomy]].
- Traces, sampling and replay — [[agent-observability]]; manifests and pinning — [[versioning-agent-systems]].
- Idempotency mechanics — [[retries-idempotency-and-concurrency]]; tier promotion — [[evidence-for-autonomy]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No published evaluation measures the effect of tool-boundary policy gateways on attack success in production; the structural argument is judgement.
- AI Act harmonized standards for logging (Art. 12) are not published; minimum fields for non-biometric systems remain undefined.
- Pending GDPR amendments (Digital Omnibus) could change Art. 22; Art. 5 and 17 citations are to the 2016 text.
- The provider-and-deployer reading for in-house agents is the author's; confirm with counsel at each edition.

## Decision log

- **2026-10-28** — Used an external auditor's interim sample plus the Alias Drift question as the spine, because it tests the evidence log by the question it must answer and exposes the failure mode of a missing field.
- **2026-10-28** — Split Bulkhead into authorization (Cedar) and routing (typed code keyed by action class), so tier changes never touch permissions; OPA presented as the alternative that folds both.
- **2026-10-28** — Adopted the finance interview design's hash-chained decision record as the baseline; rejected the platform design's "same transaction as the side effect" claim and its mutable-immutable evidence row (consistency rulings 4, 16, 18).
- **2026-10-28** — Made the guardrail rule asymmetric (may tighten, never loosen), following the June 2027 Ostrell principle from the injection chapter.

## Sources

- **Internal**
  - [[agent-observability]], [[versioning-agent-systems]], [[tool-ecosystems-and-mcp]], [[retries-idempotency-and-concurrency]], [[human-oversight-and-bounded-autonomy]], [[evidence-for-autonomy]] — neighbouring chapters kept consistent.
  - `_research/brief-security-oversight.md` (Parts 2, 5.1, 6), `_research/brief-domains-regulation.md` (Parts 2–4), `_research/brief-evaluation-observability.md` (5.1, 5.3), `_research/consistency-issues.md` items 4, 6, 15–18.
  - Interview designs: `agentic-platform-foundations` (steps `security`, `control-flow`, `dataModel[action_evidence]`), `agentic-finance-platform` (`decision-record`), `agentic-healthcare-platform` (`privacy`), `agentic-public-benefits-platform` (`audit-appeal`), `agentic-support-platform` (`compliance-eval`), `agentic-sales-platform` (`technologyChoices`), `ai-coding-cli` (`safety`).
- **External**
  - Regulation (EU) 2024/1689 Arts. 12, 19, 26(6), 86; Regulation (EU) 2026/1744; GDPR Arts. 5, 17.
  - OWASP LLM06:2025; Cedar docs and Cutler et al. 2024; OPA docs and decision logs; RFC 6962 / 9162.
  - Inan et al. 2023; Sharma et al. 2025; Debenedetti et al. 2024; Nasr et al. 2025; Chen et al. 2025; Anthropic auto mode 2026; METR 2026; AWS AgentCore Policy 2026.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: closing hand-off now goes to [[part-8]]; Bulkhead policy version labels aligned with chapter 28's format. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
