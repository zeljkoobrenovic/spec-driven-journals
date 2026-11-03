---
status: accepted
revised: 2026-10-28
---

# Spec: Agent Identity, Delegation and Least Privilege

## Intent

Answer the question "whose authority does an agent act with, and how do you keep that authority minimal?" so that an architect can design the identity layer of an agent platform. The chapter separates the identities involved in one agent action (principal, agent, run, workload), adopts delegation over impersonation with RFC 8693 semantics, and shows how a run's verified principal becomes short-lived, audience-bound, account-scoped call tokens that the policy engine decides, the tool broker executes and the system of record re-checks. It names ambient authority as the anti-pattern in its three forms (service account, borrowed login, found credential), treats time as a least-privilege axis for long-running runs, and places separation of duties and tenant isolation in the authorization path. After reading, the reader can say what a brokered credential does and does not protect, and can state an agent's reach as a risk owner would sign it.

## Audience

Architects, security architects and platform leads who own or review an agent platform that touches systems of record and personal data. They know OAuth, IAM and service identity; they need the agent-specific consequences: who the principal is per channel, what the token says, where it is minted, how long it lives and who checks it.

## Success criteria

- [ ] Reader can distinguish principal, agent identity, run identity and workload identity, and say what each proves.
- [ ] Reader can explain delegation vs impersonation from RFC 8693 (with the `act` claim), and why the book puts the principal in `sub` and the agent in `act`, unlike the agentic-platform-foundations design.
- [ ] Reader can follow one call from verified principal to run token to call token to server-side tenant check, with Bulkhead deciding and Toolyard executing (consistency items 3 and 15).
- [ ] Reader can state why a brokered but service-wide credential is still ambient authority, and how per-call scoping fixes it.
- [ ] Reader can design separation of duties for an agent workflow where initiators and editors count as makers.
- [ ] Reader can follow the Ostrell identity redesign with numbers consistent with the ledger (Poisoned Ticket, 9,400 customers, Closewise `agent-closewise-post`, Forge's run token and git proxy).
- [ ] Reader has a requirements table, a failure-scenario table, a trade-off table of credential options and an Across Domains table.
- [ ] Reader will not mistake draft standards (OAuth 2.1, WIMSE AIMS, Transaction Tokens) or vendor product docs for settled or measured evidence.

## Non-goals

- Trust boundaries, the lethal-trifecta analysis and data exposure paths ([[agent-threat-model]]).
- Injection defenses, quarantined readers and sink policy ([[prompt-injection-defense]]).
- Registry, broker internals and MCP protocol detail ([[tool-ecosystems-and-mcp]]).
- Sandbox isolation and egress for coding agents ([[sandboxes-and-execution-environments]]).
- Approval-gate design and oversight quality ([[human-oversight-and-bounded-autonomy]]); policy language and the evidence log ([[policy-enforcement-and-audit]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No published measurement shows that delegated, scoped identity lowers agent incident rates; revisit if one appears.
- The agent token profile is unsettled (WIMSE AIMS -00, Transaction Tokens draft-11, OAuth 2.1 draft-16, MCP revisions); revisit claim names when an RFC lands.
- Whether the agentic-platform-foundations token shape (`sub=agent, act=user`) should be raised as a consistency item for other chapters that quote it.

## Decision log

- **2026-10-28** — Adopted RFC 8693 claim semantics (`sub` = principal, `act` = agent) over the interview design's inverted shape, and noted the departure in the text; the WIMSE draft agrees with RFC 8693.
- **2026-10-28** — Framed "brokering hides secrets; scoping limits authority" as the chapter's central distinction, because chapter 20 already moved credentials into Toolyard and the remaining risk is reach, not leakage.
- **2026-10-28** — Added time as a fourth least-privilege axis (tokens re-derived after waits) to connect identity to durable execution.
- **2026-10-28** — Treated initiators and editors as makers for separation of duties, departing from the finance design's open question; kept the legal design's requester-may-approve as a legitimate domain policy.

## Sources

- **Internal**
  - [[prompt-injection-defense]] (Poisoned Ticket, July 2027 redesign), [[tool-ecosystems-and-mcp]] (Toolyard, call proxy vs token mint), [[agent-threat-model]], [[agents-in-the-enterprise]] (Closewise ERP users), [[sandboxes-and-execution-environments]] (Forge boundary, local CLI), [[retrieval-and-grounding]], [[routing-and-delegation]], [[durable-agent-execution]], [[agent-runtime]].
  - Design examples: `agentic-platform-foundations/interview.json` (step `identity`), `agentic-finance-platform/interview.json` (step `maker-checker`), `agentic-support-platform/interview.json` (steps `action-gate`, `escalation`), `agentic-legal-platform/interview.json` (step `attorney`), `agentic-hr-platform/interview.json` (step `privacy`), `agentic-healthcare-platform/interview.json` (step `privacy`), `agentic-public-benefits-platform/interview.json` (step `audit-appeal`).
- **External**
  - IETF, RFC 8693 OAuth 2.0 Token Exchange (2020) — delegation vs impersonation, actor chains.
  - IETF, draft-ietf-wimse-aims-00 (2026) and draft-ietf-oauth-transaction-tokens-11 (2026) — emerging agent identity guidance.
  - MCP Authorization, revision 2026-07-28 — resource servers, no passthrough.
  - OWASP LLM06 Excessive Agency — complete mediation.
  - Microsoft Entra Agent ID docs (2026); GitHub installation-token docs — product examples of agent identity and short-lived scoped tokens.
  - Invariant Labs GitHub MCP case (2025); PocketOS (2026, widely reported); Replit (2025); AWS-2025-015 — incidents where credential reach set the damage.
  - Hardy, The Confused Deputy (1988).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: NIST AI Agent Standards Initiative row corrected (the page lists an RFI and an NCCoE draft concept paper; no final guidance). *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
