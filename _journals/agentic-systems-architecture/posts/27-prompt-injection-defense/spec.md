---
status: accepted
revised: 2026-10-28
---

# Spec: Prompt Injection: Designing for an Unsolved Problem

## Intent

Give architects a defensible position on prompt injection: it is not solved, detection and model training only lower its probability, and the controls that bound it are architectural. The chapter must move the reader from "how do we stop the model being fooled?" to "what can a fooled model reach?", and give them a layered design (source hygiene, model and classifier, structural separation, sink enforcement) in which only the last two count toward stated risk. It owns the terms prompt injection, indirect prompt injection, privilege separation (agent) and sink.

## Audience

Software architects, security architects and principal engineers who design or review agents that read untrusted content and call tools. They know classic injection, least privilege and authorization; they need the agent-specific evidence (benchmarks, adaptive attacks, documented exploits) and patterns they can put into a design review.

## Success criteria

- [ ] Reader can distinguish direct, indirect and stored injection and say what bounds each.
- [ ] Reader can name the six exploit classes and which of them a sink policy can stop (and which, like misleading output, it cannot).
- [ ] Reader can cite the measured evidence (AgentDojo, InjecAgent, spotlighting, "The Attacker Moves Second", CaMeL, dated vendor series) with what was measured and its limits, and explain why vendor ASRs are not comparable across posts.
- [ ] Reader can choose among the structural patterns (action-selector, plan-then-execute, map-reduce, Dual LLM, code-then-execute/CaMeL, context-minimization) by how much the model may decide after reading untrusted data.
- [ ] Reader can write a sink policy keyed on argument provenance and list the forgotten sinks (rendering, fetches, memory writes, handoffs).
- [ ] Reader can design an injection test suite that reports task success under attack alongside ASR and uses adaptive attackers.
- [ ] The Poisoned Ticket worked example agrees with the scenario ledger and shows detection, containment and recovery.
- [ ] Exploits are described as classes, never as step-by-step working payloads; no model version is recommended.

## Non-goals

- The full threat model, trust-boundary map and lethal trifecta definition ([[agent-threat-model]]).
- Agent identity, on-behalf-of delegation and scoped credentials, including the Answerdesk identity redesign ([[agent-identity-and-least-privilege]]).
- Approval-gate design and approval fatigue in depth ([[human-oversight-and-bounded-autonomy]]).
- Policy-as-code engines and the evidence log ([[policy-enforcement-and-audit]]).
- MCP architecture and tool-registry governance ([[tool-ecosystems-and-mcp]]); sandbox technology ([[sandboxes-and-execution-environments]]); memory poisoning mechanics ([[agent-memory]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No independent measurement of injection success in production agents exists as of October 2026; revisit if one is published.
- Whether any shipped product implements CaMeL-style capability tracking end to end is unconfirmed.
- The full text of the OWASP Agentic Top 10 was not read; only category names are used.

## Decision log

- **2026-10-28** — Framed defenses as four layers by guarantee and adopted the rule that only structural separation and sink enforcement count toward an agent's stated risk; prompt-level, classifier and model defenses are presented as probability reducers.
- **2026-10-28** — Used the Rule of Two (Meta) rather than the trifecta as the design-review check, because its third leg includes state change; showed that the trifecta is relative to who can read the sink (Answerdesk scopes private data and outbound to the same verified principal).
- **2026-10-28** — Did not name post-mid-2026 model versions from Anthropic's August 2026 post; reported its results by evaluation and safeguard configuration after re-verifying the page.
- **2026-10-28** — Resolved the coding-harness "positive prompt injection" tension with the channel rule: content may shape behavior but never grants permissions, egress or credentials.

## Sources

- Internal: [[agent-threat-model]], [[context-engineering]], [[tool-contracts]], [[tool-ecosystems-and-mcp]], [[sandboxes-and-execution-environments]], [[agent-memory]], [[agent-identity-and-least-privilege]], [[human-oversight-and-bounded-autonomy]], [[policy-enforcement-and-audit]], [[building-agent-eval-suites]], [[evidence-for-autonomy]].
- Interview designs (design examples): `agentic-platform-foundations` (step `security`), `agentic-support-platform` (`grounding`, `txn-safety`), `ai-coding-cli` (`context`, `safety`), `ai-coding-harness` (`sensors`), `agentic-finance-platform` (`pipeline`), `agentic-healthcare-platform` (`privacy`), `agentic-public-benefits-platform` (`grounding`, `compliance-eval`).
- External: Greshake et al. 2023; AgentDojo 2024; InjecAgent 2024; spotlighting 2024; instruction hierarchy 2024; Nasr et al. 2025; CaMeL 2025; Beurer-Kellner et al. 2025; NCSC 2025; Meta Rule of Two 2025; Willison 2022, 2023, 2025; Anthropic 2025 and 2026; EchoLeak (NVD, 2025); Invariant Labs 2025; PromptArmor 2024; OWASP 2025.
- Research brief: `_research/brief-security-oversight.md` (Parts 1–3, 5.3).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: corrected the Anthropic 1.4% vs 17.6% comparison (different safeguard conditions and evaluations); Rule of Two cut to one sentence linking to [[agent-threat-model]]; "evaluation harness" per ruling 1; dated the Invariant Labs observation. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
