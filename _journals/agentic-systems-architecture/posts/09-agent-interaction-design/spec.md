---
status: accepted
revised: 2026-10-28
---

# Spec: Interaction Design for Agents: Chat, Delegation and Handoff to Humans

## Intent

Answer the chapter-9 question: how should people interact with agents, and what does each interaction pattern demand of the architecture? The chapter must move interaction design from "chat UI" to architecture. Three moves carry it. First, an interaction mode (conversational, copilot inline, delegated asynchronous task, background agent, escalation to a human) is defined by initiation, presence and where the result lands, and it fixes where state lives, how long a human gate may wait and who may act. Second, the surface renders facts (progress, pending actions, outcomes, commitments, evidence) from records, and model text is one labeled kind of content. Third, escalation transfers ownership, so it carries a typed escalation package built by code and moves write authority from the agent to the person.

## Audience

Architects, principal engineers and product leads who design or review customer-facing, copilot and background agents. They know web front ends, queues and job APIs. They leave able to record a mode per entry point, specify the content kinds a channel may render, design a delegated-task state machine and an escalation package, and review disclosure, interruption and accessibility as release criteria.

## Success criteria

- [ ] Defines interaction mode, delegated task and escalation package precisely, with a mode table mapped to Ostrell's agents and entry points.
- [ ] Derives the state, latency, gate and authority consequences of each mode, including a requirements-per-interaction table, without re-teaching latency budgets ([[agent-latency-and-throughput]]) or approval-gate design ([[human-oversight-and-bounded-autonomy]]).
- [ ] States the "facts from records" rule with a content-kinds table, grounded in *Moffatt v. Air Canada* (2024).
- [ ] Separates interruption from steering and confirmation from approval, consistent with consistency ruling 6 (approvals bound to content hash) and ruling 10 (hold, not drop).
- [ ] Covers notifications and inbox, disclosure (EU AI Act Art. 50, verified text and dates) and accessibility (WCAG 2.2 SC 4.1.3 and 2.2.1).
- [ ] Gives a typed escalation package, the ownership-transfer sequence and an Ostrell worked example with numbers; adds the Forge run card as the pull-request interface after the Fixture Purge.
- [ ] Includes evidence with limits (Amershi et al. 2019; Magentic-UI 2025; Bansal et al. 2021; automation-bias reviews; Anthropic 2025–26 telemetry; GitHub coding-agent docs) and says where the evidence stops.
- [ ] Has a failure-scenario table, two trade-off tables, the Across Domains table, three mermaid diagrams, Chief Architect's view, questions and sources; article ≤ 8,000 words.

## Non-goals

- Latency budgets per mode, streaming versus output guards: [[agent-latency-and-throughput]].
- Approval gate design, approval fatigue measurement, oversight modes and regulation of oversight in depth: [[human-oversight-and-bounded-autonomy]].
- Agent-to-agent handoff payloads, A2A in depth: [[coordination-and-handoffs]].
- Routing and the delegation contract: [[routing-and-delegation]].
- Durable execution of waits and timers: [[durable-agent-execution]]; task record design: [[task-state-and-checkpoints]].
- Visual or brand design of chat widgets.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No controlled study of escalation-package content or agent progress displays was found; revisit if one is published.
- Commission guidance on Article 50 (what counts as "obvious", disclosure in voice and email) may change the disclosure section.
- Should the content-kinds rule become a Sounding check in [[building-agent-eval-suites]] (model text claiming an outcome without a receipt)?

## Decision log

- **2026-10-28** — Defined modes by initiation, presence and result location rather than by channel, so one agent can have several modes per entry point; aligned the mode names with [[agent-latency-and-throughput]].
- **2026-10-28** — Adopted the agentic-support-platform design's package contents and full-ownership transfer, with three changes: identifiers and commitments as separate fields, pending actions explicit, model writes only the labeled summary. Rejected co-handling for actions with external effect.
- **2026-10-28** — Used the Forge pull request as the second worked example to show that the same "facts from records" defect appears in a mode with no conversation at all.
- **2026-10-28** — Treated customer confirmation as intent, never authority, following the support design's "a customer message can request an action but can never approve a policy bypass".

## Sources

- **Internal**
  - [[meet-ostrell]] and the scenario ledger — Answerdesk volumes and escalation rate, €5.50 per escalation, Fixture Purge, Rubber Stamp metrics, Scout plan approval thresholds, Closewise approval timers, Toolyard ownership rule.
  - [[routing-and-delegation]], [[agent-latency-and-throughput]], [[context-engineering]], [[prompt-injection-defense]], [[planning-and-decomposition]], [[durable-agent-execution]].
  - Interview design examples: agentic-support-platform (description, steps `action-gate`, `escalation`, technology choices), ai-coding-cli (`api`, step `cloud`), agentic-healthcare-platform (capacity), agentic-public-benefits-platform (capacity).
- **External**
  - Amershi et al., Guidelines for Human-AI Interaction (CHI 2019); Mozannar et al., Magentic-UI (2025 preprint); Bansal et al. (CHI 2021); Goddard et al. (JAMIA 2012); Parasuraman and Manzey (2010); Bainbridge (1983); Feng, McDonald, Zhang (2025).
  - EU AI Act Arts. 14 and 50; Digital Omnibus on AI (2026); WCAG 2.2; MCP elicitation (2026-07-28).
  - Anthropic research and engineering posts (2025, 2026); GitHub Copilot cloud agent documentation (accessed 2026-10); Moffatt v. Air Canada (2024); Klarna (2024) and Fortune (2025).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: turn vs exchange wording (ruling 19); escalations aligned to about 2,300 a day with recomputed savings; pending-credit example raised to €320 (credits ≤ €250 are A2 after October 2027); removed an internal ruling reference from the prose; Moffatt award broken down. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
