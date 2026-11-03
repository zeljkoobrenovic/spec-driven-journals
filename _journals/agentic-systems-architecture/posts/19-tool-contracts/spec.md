---
status: accepted
revised: 2026-10-28
---

# Spec: Tool Contracts: Inputs, Outputs and Validation

## Intent

Show architects how to design one tool so that a model can use it correctly and the system can trust what happens. The chapter treats the tool as an agent-computer interface rather than an API wrapper: tools shaped around one decision, with code supplying every fact the system already holds; a two-schema contract (a model-facing schema limited to what constrained decoding enforces, and a full validation schema run outside the model); four validation checks in a fixed order; errors in five outcome classes with enforced retry permissions; bounded results with readable identifiers and typed statuses with receipts; and side-effect semantics declared in a reviewed contract, with MCP annotation hints treated as advice. After reading, the reader can review a tool contract and say what the model can still get wrong.

## Audience

Architects, principal engineers and tool owners who expose systems of record to agents and must decide what a tool's arguments, errors and results look like. They know JSON Schema and API design; they need the consequences of a model being the client.

## Success criteria

- [ ] Reader can compare endpoint-shaped, workflow-shaped and primitive-shaped tools and choose by what bounds the effect, reconciling vendor guidance with the ai-coding-cli design's primitives.
- [ ] Reader can state what constrained decoding guarantees and its documented escapes (refusal, truncation, enum case, unsupported keywords), with dated vendor citations and the JSONSchemaBench and Tam et al. evidence and limits.
- [ ] Reader can apply the two-schema contract and the four validation checks (static, referential, policy, precondition at write).
- [ ] Reader can classify tool outcomes into the five classes and explain why an unknown outcome never reaches the model (consistent with [[retries-idempotency-and-concurrency]]).
- [ ] Reader can map the four MCP annotation hints to enforced contract fields (risk class, idempotency mechanism, business key, trifecta) and explain why hints are not controls.
- [ ] Reader can follow the Answerdesk credit tool redesign (v1 → 3.2.0) with Ostrell numbers consistent with the ledger and with chapters 20 and 24.
- [ ] Reader has a requirements table, a failure-scenario table, a trade-off table and an Across Domains table, plus three mermaid diagrams.

## Non-goals

- Registries, brokers, MCP transports and authorization, tool search and supply chain ([[tool-ecosystems-and-mcp]]).
- Idempotency keys, retry layers, leases and unknown-outcome mechanics in depth ([[retries-idempotency-and-concurrency]]).
- Action objects, dry runs, receipts and external commitments ([[side-effects-and-external-actions]]).
- Sandboxes for code-executing and primitive tools ([[sandboxes-and-execution-environments]]).
- Compatibility classes for contract versions in full ([[versioning-agent-systems]]); eval suite construction ([[building-agent-eval-suites]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No published study measures how often schema-valid tool calls carry wrong values in enterprise use; revisit if one appears.
- Whether provider strict modes will add numeric and length keywords; the two-schema advice stays either way, but the lint rules would change.
- The `retry` cap of 2 for model-fixable errors suits 2026–27 models; evaluate whether it should be per error class.

## Decision log

- **2026-10-28** — Used the credit tool's own redesign (v1 endpoint wrapper → 3.2.0 workflow tool) as the spine, with a 1,000-call review after the Double Credit, so the chapter stays distinct from chapter 24 (which owns the retry story) and chapter 20 (which owns the registry record derived from this contract).
- **2026-10-28** — Reconciled "workflow tools" (Anthropic, OpenAI guidance) with "orthogonal primitives" (ai-coding-cli design, step `agent-loop`) by the variable that bounds the effect, rather than picking one; labeled as judgement since no study compares them in one domain.
- **2026-10-28** — Separated "annotation" (declared in the reviewed contract, enforced) from "annotation hint" (MCP, advisory), and required the idempotency *mechanism* to be declared, consistent with chapters 20 and 24.
- **2026-10-28** — Kept policy numbers (€250 limit, tiers) out of the contract; the contract references the Bulkhead policy, matching chapter 20's registry record.

## Sources

- **Internal**
  - [[retries-idempotency-and-concurrency]] — Double Credit, action keys, unknown outcome, `issue_credit` reliability block and business key.
  - [[tool-ecosystems-and-mcp]] — Toolyard registry record for `billing.issue_credit` 3.2.0; risk classes.
  - [[provenance-and-freshness]] — re-read before write; `finalize_quote`.
  - [[context-engineering]], [[prompt-injection-defense]], [[versioning-agent-systems]], [[building-agent-eval-suites]], [[evidence-for-autonomy]], [[human-oversight-and-bounded-autonomy]].
- **Interview designs (design examples)**
  - `ai-coding-cli/interview.json` steps `agent-loop`, `safety`; `agentic-support-platform/interview.json` steps `action-gate`, `txn-safety`; `agentic-finance-platform/interview.json` step `ledger`; `agentic-healthcare-platform/interview.json` step `gate`; `agentic-platform-foundations/interview.json` `api[POST /v1/tools]`.
- **External**
  - MCP Tools and schema, revision 2026-07-28 — validation duties, error classes, `outputSchema`, annotation hints.
  - Anthropic, "Writing effective tools for AI agents" (2025); Anthropic strict tool use and structured outputs docs; OpenAI function-calling and structured-outputs guides (accessed 2026-10).
  - Yang et al., SWE-agent (2024); Lu et al., ToolSandbox (2024); Geng et al., JSONSchemaBench (2025); Tam et al. (2024); Xu et al., TheAgentCompany (2024); Yao et al., τ-bench (2024); OWASP LLM06:2025.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: conversation "turn" changed to "exchange" (ruling 19); Q3 reply-check row aligned with the Promised Credit September re-audit (2 premature statements, not 0 delivered); TheAgentCompany wording corrected to the paper's "deceiving oneself". *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
