---
status: accepted
revised: 2026-10-28
---

# Spec: Trust Boundaries and the Agent Threat Model

## Intent

Give architects a threat-modeling method that fits agents: draw trust boundaries by who can write the text and who can read the result (including the boundary inside the context window and the one to the model provider), analyze the lethal trifecta per session type rather than per component, and inventory the data exposure paths that need no attacker (provider retention and residency, traces, eval data, caches and indexes across tenants, outputs, derived artifacts). The chapter owns the terms **trust boundary (agent)**, **lethal trifecta** and **data exposure path**, and ends with a threat-model template tied to each agent version and re-run on defined triggers.

## Audience

Security architects, software architects and principal engineers who review or own agentic systems, and the risk owners who sign residual risk. They know STRIDE-style threat modeling, least privilege and GDPR basics; they need the agent-specific boundaries, a correct way to count trifecta legs, and an exposure-path inventory they can run on their own platform.

## Success criteria

- [ ] Reader can name the eight boundaries (principal, provider, context window, stored content, action, tool supply, agent-to-agent, egress) and the tenant and observer partitions, with the rule for what may cross each.
- [ ] Reader can map OWASP LLM Top 10 2025, the OWASP Agentic Top 10 and NIST AI 600-1 onto boundaries and owning controls.
- [ ] Reader can count trifecta legs per session type from tools and context sources, treat search queries, fetches, rendered output and delegation messages as outbound channels, and distinguish a scoped trifecta from a full one.
- [ ] Reader can list the data exposure path classes with documented evidence (Asana MCP 2025, prompt-cache sharing, embedding inversion, training-data extraction, dated provider terms) and the control for each.
- [ ] Reader can apply minimization, residency and retention as gateway and assembler decisions, not contract clauses.
- [ ] The Ostrell worked example (threat model v1 vs v2, trifecta register, 61 exposure paths, data classes) agrees with the scenario ledger; failure scenarios name detection, containment and recovery.
- [ ] Injection defenses are linked to [[prompt-injection-defense]], not re-taught; no model version is named or recommended.

## Non-goals

- Injection defenses, structural patterns (Dual LLM, CaMeL, plan-then-execute), sink policy code and injection testing: [[prompt-injection-defense]].
- Agent identity, on-behalf-of delegation, scoped credentials and the identity redesign: [[agent-identity-and-least-privilege]].
- Approval gate design and approval fatigue: [[human-oversight-and-bounded-autonomy]].
- Policy enforcement points, evidence log and audit retention: [[policy-enforcement-and-audit]]; trace content stores: [[agent-observability]].
- Sandbox isolation mechanics: [[sandboxes-and-execution-environments]]; tool registry governance: [[tool-ecosystems-and-mcp]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- The full OWASP Agentic Top 10 text was not read; category names come from a secondary source. Re-check titles against the OWASP PDF.
- Provider retention and residency terms are as documented in October 2026 for two providers; they change, and other providers were not checked.
- No published evaluation compares agent threat-modeling methods; the per-session method is the author's judgement.

## Decision log

- **2026-10-28** — Unit of analysis is the session type, not the component; the component STRIDE model is kept for platform infrastructure.
- **2026-10-28** — Defined a "scoped trifecta" (all three legs, but data and every sink belong to one principal) to reconcile the trifecta with support agents that must hold all three legs; consistent with chapter 27's "trifecta is relative to who can read the sink".
- **2026-10-28** — Model stance reconciled across interview designs: model output is fallible always and attacker-influenced whenever the context held non-operator, non-system-of-record text.
- **2026-10-28** — The coding CLI design's "read-only tools run freely" is reconciled as "reads are free only while the session has no open egress".

## Sources

- Internal: [[agentic-reference-architecture]], [[context-engineering]], [[retrieval-and-grounding]], [[tool-ecosystems-and-mcp]], [[caching-and-context-budgets]], [[agent-observability]], [[building-agent-eval-suites]], [[prompt-injection-defense]], [[agent-identity-and-least-privilege]].
- Interview designs: `agentic-platform-foundations` (step `security`), `ai-coding-cli` (step `safety`, `dataModel`), `ai-coding-harness`, `agentic-legal-platform` (step `confidentiality`), `agentic-hr-platform` (step `privacy`), `agentic-healthcare-platform` (step `privacy`).
- External: Willison (2025) lethal trifecta; Meta (2025) Rule of Two; OWASP LLM Top 10 2025 and Agentic Top 10 (2025); NIST AI 600-1 (2024); Threat Modeling Manifesto (2020); Gu et al. (2025); Morris et al. (2023); Carlini et al. (2021); The Register on Asana MCP (2025); OpenAI and Anthropic data-retention documentation (accessed 2026-10); GDPR; 45 CFR 164.502(b).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: Forge egress and token wording aligned with rulings 3 and 20 (proxy to Gateway, git proxy, package mirror and Toolyard; run-scoped token); template endpoint names aligned with the ledger's Gateway routes. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
