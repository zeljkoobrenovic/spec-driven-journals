---
status: accepted
revised: 2026-10-28
---

# Spec: Tool Ecosystems, MCP and the Tool Broker

## Intent

Show architects how to expose, discover, govern and broker tools across many agents and many engineers. The chapter must separate what the Model Context Protocol (MCP) standardizes (as of the 2026-07-28 revision) from what an organization must still build: a tool registry with owners, risk classes and definition hashes, and a tool broker on every call path that resolves the authorized tool set, asks the policy engine, holds credentials, enforces idempotency, shapes results and writes evidence. It must also treat tool definitions and servers as a supply chain, and keep tool search (relevance) apart from authorization (permission). After reading, the reader can defend "one broker, no bypass" and knows what MCP will not do for them.

## Audience

Architects, principal engineers and platform leads who run or are about to run several agents against systems of record, and who must decide whether to adopt MCP, build or buy a tool gateway, and govern third-party and local MCP servers. They know OAuth and API gateways; they need the agent-specific consequences.

## Success criteria

- [ ] Reader can state what MCP 2026-07-28 standardizes (roles, transports, stateless requests, authorization, elicitation, annotations as hints) and list what it leaves to the organization, with dated, linked spec citations.
- [ ] Reader can describe the registry record and the broker's responsibilities, including what the broker must never do, and the two credential patterns (call proxy and token mint) with when each applies.
- [ ] Reader can explain why tool search is not access control and apply "authorize, then rank" with the three filters (manifest, policy, search).
- [ ] Reader can name the documented tool supply-chain attacks (tool poisoning, rug pull, shadowing, malicious package, vulnerable tooling, toxic agent flow, token passthrough) and a control for each.
- [ ] Reader can follow the Toolyard worked example with Ostrell numbers that match the ledger (Poisoned Ticket, Lost Handoff fold-back, the Tracker Update).
- [ ] Reader has a failure-scenario table (detection, containment, recovery), a trade-off table of exposure options and an Across Domains table.
- [ ] Reader will not mistake vendor-internal tool-count numbers or gateway product documentation for independent evidence.

## Non-goals

- Designing a single tool's contract, schema and errors ([[tool-contracts]]).
- Isolation technology and egress controls for sandboxes ([[sandboxes-and-execution-environments]]).
- Action objects, receipts and external commitments in depth ([[side-effects-and-external-actions]]); idempotency mechanics ([[retries-idempotency-and-concurrency]]).
- Agent identity, token exchange and least privilege in depth ([[agent-identity-and-least-privilege]]); policy as code and the evidence log ([[policy-enforcement-and-audit]]).
- Prompt injection defenses beyond the tool layer ([[prompt-injection-defense]]); agent-to-agent protocols ([[coordination-and-handoffs]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Adoption of the stateless MCP revision by SDKs, gateways and hosts is not publicly measured; revisit when data appears.
- Whether the official MCP Registry leaves preview, and what curation aggregators add, could change the "run your own registry" advice.
- No measurement of policy-gateway effectiveness exists; if one is published, update the Evidence section.

## Decision log

- **2026-10-28** — Framed MCP as "standardize the shape, terminate at the broker" rather than as either the answer or a risk to avoid. Rejected a protocol tutorial: the reader needs what MCP leaves undone.
- **2026-10-28** — Adopted the book ruling that authorization (Bulkhead) is separate from execution (Toolyard), and named both credential patterns from the agentic-platform-foundations design (call proxy, token mint) instead of picking one.
- **2026-10-28** — Put code execution as a tool interface here briefly (boundary moves to the sandbox) and handed the sandbox itself to chapter 21.
- **2026-10-28** — Added a local Ostrell incident, the Tracker Update (September 2027), to show the cost of definition pinning, not only its benefit.

## Sources

- **Internal**
  - [[tool-contracts]], [[agentic-reference-architecture]], [[caching-and-context-budgets]] (prefix layout; Answerdesk 24,000-token budget), [[prompt-injection-defense]] (Poisoned Ticket), [[coordination-and-handoffs]] (Lost Handoff fold-back), [[versioning-agent-systems]].
  - Design examples: `agentic-platform-foundations/interview.json` (steps `runtime`, `identity`; tool registration), `ai-coding-cli/interview.json` (step `extensibility`), `agentic-healthcare-platform/interview.json` (steps `gate`, `privacy`).
- **External**
  - MCP specification 2026-07-28 (architecture, tools, transports, authorization, elicitation, schema, changelog), MCP security best practices, governance, feature lifecycle and Registry pages.
  - Anthropic, *Introducing advanced tool use* (2025) and tool search docs; OpenAI function-calling guide; Gan and Sun, *RAG-MCP* (2025).
  - Wang et al., *CodeAct* (2024); Anthropic, *Code execution with MCP* (2025); Cloudflare, *Code Mode* (2025).
  - Invariant Labs on tool poisoning and the GitHub MCP exploit (2025); Snyk on `postmark-mcp` (2025); NVD entries for CVE-2025-49596 and CVE-2025-6514; Willison, *The lethal trifecta* (2025); AWS AgentCore Policy docs (2026).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: MCP revision-count sentence corrected (four revisions in twenty months after 2024-11-05, not "backward-incompatible" from 2025-03-26); billing-specialist fold-back dated 7 June 2027 (editor line). *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-28** — Final figure-fix pass: Figure 5 (tool-version lifecycle) corrected: the Deprecated arrow now ends at Retired. *(AI-mediated session)*
