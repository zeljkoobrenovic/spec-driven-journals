---
status: accepted
revised: 2026-10-28
---

# Spec: Coordination, Handoffs and Agent-to-Agent Protocols

## Intent

Give architects a design for passing work, context and responsibility between agents and people without loss. The chapter lands one position: a handoff is a transfer of ownership, so it is a recorded, accepted transaction on a shared task record, not a message; identifiers and commitments are filled by code from receipts, never by a model's summary; and agent-to-agent protocols (A2A) belong at organizational boundaries, where everything that crosses is untrusted and accountability is contractual. After reading, the reader can review any proposed handoff by asking why it exists, what only code can supply, and who owns the task before acceptance.

## Audience

Software architects, principal engineers and technical leaders who design or review multi-agent systems, human escalation paths and integrations with other organizations' agents. They know distributed systems and messaging; they need the vocabulary (handoff vs delegation), the payload and ownership mechanics, and a dated, sober picture of A2A.

## Success criteria

- [x] Defines handoff, handoff payload, agent card and task (A2A), and separates control, context, authority and responsibility for delegation, handoff, approval and escalation in one table.
- [x] Presents a handoff state machine (proposed, refused, offered, accepted, declined, expired, returned, closed) with deadlines and fallback owners, and a typed payload schema with field provenance.
- [x] Compares message passing, shared task state and blackboards, with a one-writer-per-field conflict rule and optimistic concurrency.
- [x] Describes A2A v1.0 as of October 2026 (agent card, task states, artifacts, cancellation, opacity, security warnings) with dated sources, and states when to use it and when not.
- [x] Tells the Lost Handoff end to end with ledger-consistent numbers and dates (April 2027 incident, typed payload 2027-04-28, fold-back 2027-06-07), plus the escalation payload and the A2A pilot.
- [x] Evidence section covers historical agent communication languages, MAST, vendor reports and framework defaults, with limits, and says where evidence stops.
- [x] Failure-scenario table (detection, containment, recovery), trade-off table, requirements table, three mermaid diagrams, Across Domains table with judgement.
- [x] Article under 8,000 words before Sources.

## Non-goals

- Whether to have several agents at all, and the topology rule: [[single-and-multi-agent-designs]].
- Routing, the delegation contract and sub-agents: [[routing-and-delegation]].
- The durable task record and resume semantics: [[task-state-and-checkpoints]], [[durable-agent-execution]].
- How escalation packages are presented to people: [[agent-interaction-design]]; approvals: [[human-oversight-and-bounded-autonomy]].
- Token exchange and agent identity in depth: [[agent-identity-and-least-privilege]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No published production evaluation compares free-text and typed handoffs, and no operator has published A2A production experience; revisit when either appears.
- A2A field names and bindings may change after 1.0.x; re-check the specification before any revision.
- Whether Ostrell's A2A pilot should ever allow write skills (it would require the A1 cap on external commitments to be designed into the protocol flow).

## Decision log

- **2026-10-28** — Defined handoff as transfer of ownership complete only on acceptance, to separate it from framework handoff tool calls and from approval.
- **2026-10-28** — Payload fields carry provenance; identifiers and commitments are code-filled from receipts, model fields are labeled, consistent with the context and provenance chapters.
- **2026-10-28** — Preferred shared task state over message passing inside one platform; A2A only at trust boundaries; remote artifacts are untrusted input.
- **2026-10-28** — Used the `[editor]` ledger dates (typed payload 2027-04-28, fold-back 2027-06-07) and added local incident numbers (640 billing handoffs a day, the 2,000-handoff audit) to the ledger.

## Sources

- Internal: [[routing-and-delegation]], [[single-and-multi-agent-designs]], [[task-state-and-checkpoints]], [[context-engineering]], [[provenance-and-freshness]], [[prompt-injection-defense]], [[agent-identity-and-least-privilege]], [[agent-interaction-design]].
- Interview designs: agentic-support-platform (step `escalation`), agentic-sales-platform (`handoff`), agentic-legal-platform (`attorney`), agentic-hr-platform (`grounding`, `hiring-gate`), agentic-healthcare-platform (`gate`), agentic-public-benefits-platform (`gate`).
- External: A2A specification v1.0 and releases; Linux Foundation and AAIF announcements; OpenAI practical guide and Agents SDK handoff docs; Claude Agent SDK subagents docs; Google ADK collaboration docs; Cognition 2025 and 2026; Anthropic 2025 research-system and long-running-harness posts; Cemri et al. (MAST); Kim et al.; Han and Zhang (blackboard); Erman et al. (Hearsay-II); Smith (Contract Net); FIPA communicative acts; RFC 8693.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: corrected quotes (ADK, Anthropic harness post, Cognition), qualified the Linux Foundation press release, noted the A2A 1.0 `TASK_STATE_` prefix, added RFC 8693 `sub`, reconciled escalation_handoff.v2 (June 2027) with the November 2027 escalation package in agent-interaction-design, applied turn/exchange wording. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
