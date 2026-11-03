---
status: accepted
revised: 2026-10-28
---

# Spec: Connecting Agents to the Enterprise

## Intent

Show architects how agents connect to existing applications, data platforms and organizational processes without becoming a parallel shadow system. The chapter must define the system of record in its agent context (the system wins any disagreement, and the design makes the disagreement visible), separate the state an agent may keep (task state, a registered staging store, evidence) from business state it may not, and give four agent integration patterns (tool over an existing API, event-triggered agent, agent step inside a workflow, agent as a service inside an application) with who starts the run, who owns state and who writes. It must cover governed data access for reads, the staging store → gate → executor → system of record → reconciler → evidence spine for writes, which identity appears in the target system's audit trail, and how agent work lands in existing queues with a named accountable human. After reading, the reader can write a system-of-record rule for their organization and defend it to an auditor.

## Audience

Architects, principal engineers and technical leaders integrating agents with ERP, CRM, ticketing, HRIS, CLM and warehouse systems owned by other teams, who must answer to auditors, process owners and data owners. They know enterprise integration; they need what changes when the client proposes its own actions.

## Success criteria

- [ ] Reader can define system of record (agent context), shadow system, agent integration pattern and governed data access, and state the five invariants of Ostrell's system-of-record rule.
- [ ] Reader can choose among the four integration patterns with the comparison table and the "workflow vs in-application" rule.
- [ ] Reader can choose a read interface (typed lookup, governed view, semantic layer, free SQL) by what the result drives, citing Spider 2.0, the Sequeda study and CRMArena-Pro with their limits.
- [ ] Reader can trace a write through staging store, Bulkhead decision, Toolyard executor, ERP receipt and Logbook, and explains version preconditions and reconciliation with human edits.
- [ ] Reader can compare four identity options for the target system's audit trail and apply one-named-agent-user-per-duty where delegation is not supported.
- [ ] Reader has a requirements-per-interaction table, a failure-scenario table, a trade-off table (platform agent vs vendor embedded agent vs own store vs direct database) and an Across Domains table.
- [ ] Ostrell numbers match the ledger (1,912 proposals in September 2027, 164 for Ostrell Field Deutschland GmbH; 7,100 conversations a day, 33% escalation, 41% resolution).

## Non-goals

- Token exchange, workload identity and scoped credentials in depth ([[agent-identity-and-least-privilege]]).
- Action objects, receipts and external commitments in depth ([[side-effects-and-external-actions]]); idempotency mechanics ([[retries-idempotency-and-concurrency]]).
- Tool brokering and MCP ([[tool-ecosystems-and-mcp]]); retrieval design ([[retrieval-and-grounding]]); freshness ([[provenance-and-freshness]]).
- Approval gate design and approval fatigue ([[human-oversight-and-bounded-autonomy]]); escalation package UX ([[agent-interaction-design]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No published evaluation compares integration patterns on reliability, cost or audit outcomes; revisit if one appears.
- Whether major ERPs will accept delegated agent tokens (RFC 8693 `act` claims) by 2028, which would retire the named-agent-user workaround.
- How vendor-embedded agents in SaaS systems can feed a platform evidence log; no standard exists as of October 2026.

## Decision log

- **2026-10-28** — Opened with an audit finding (approvals outside the ERP, a create-and-post service account) rather than a technical outage, because the shadow-system cost shows first in audit and accountability.
- **2026-10-28** — Adopted the back-office digests' staging-store spine but separated authorization (Bulkhead) from execution (Toolyard), rejecting the interview designs' identity-broker-as-executor shortcut, per the book's consistency rulings.
- **2026-10-28** — Recommended named agent users per duty for legacy systems of record instead of insisting on delegated tokens, because most ERPs will not validate them in 2027; recorded the human via reference fields and Logbook.
- **2026-10-28** — Kept free SQL out of agents that act, citing enterprise text-to-SQL results, rather than treating text-to-SQL as a general data-access tool.

## Sources

- **Internal**
  - [[agentic-reference-architecture]], [[tool-ecosystems-and-mcp]] — placement of broker and policy point; per-system-of-record servers.
  - [[task-state-and-checkpoints]], [[durable-agent-execution]] — Closewise task record, posting key and the September 2027 close.
  - [[retrieval-and-grounding]], [[provenance-and-freshness]] — structured lookup and re-read before commit.
  - Interview designs: `agentic-finance-platform` (steps `ledger`, `pipeline`, `maker-checker`, `idempotency`, `capacity`), `agentic-hr-platform` (`privacy`, `service-eval`), `agentic-support-platform` (`grounding`, `escalation`), `agentic-sales-platform` (`enrichment`, `handoff`), `agentic-healthcare-platform` (`gate`, `privacy`).
- **External**
  - Lei et al., *Spider 2.0* (2024) — enterprise text-to-SQL gap.
  - Sequeda, Allemang and Jacob (2023) — contextual layer raises SQL QA accuracy.
  - Huang et al., *CRMArena-Pro* (2025) — confidentiality awareness of agents.
  - RFC 8693; MCP Authorization 2026-07-28; OWASP LLM06:2025; Microsoft Entra Agent ID docs — delegation and identity.
  - EU AI Act Art. 26(7) and the Digital Omnibus; 15 U.S.C. 7262 — worker information and internal control.
  - Moffatt v. Air Canada (2024); Mata v. Avianca (2023) — organizational and professional ownership of output.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: turn vs exchange wording; escalations aligned to about 2,300 a day; Peoplepoint AI Act status aligned with Ostrell's documented assessment; Entra Agent ID link updated to the current page. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
