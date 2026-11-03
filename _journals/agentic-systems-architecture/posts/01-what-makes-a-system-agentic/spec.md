---
status: accepted
revised: 2026-10-28
---

# Spec: What Makes a System Agentic

## Intent

Give the reader a definition of "agent" that can be checked by reading code, and the vocabulary the rest of the book builds on. The chapter replaces the product label with a per-decision-point question (who chooses the next step: code, the model or a human?), defines the five terms it owns (agent, agentic system, agent loop, locus of control, action space), and separates the four properties of model-held decision points that change the architecture (varying proposals, open-ended action spaces, untrusted text reaching the decider, cost per step) from the distributed-systems fundamentals that do not change. After reading, an architect can draw a decision-point map of any system called an agent and knows where validation, policy, budgets and evidence must sit.

## Audience

Software architects, principal and staff engineers, and technical leaders who must review, fund or operate systems sold or built as "agents". They know distributed systems well and need a precise boundary between automation with a model inside and a system where the model controls the flow, not an introduction to language models.

## Success criteria

- [ ] Reader can state the control-flow definition and apply it per decision point, distinguishing model output as data from model output as control.
- [ ] Reader can compare the major published definitions (classical, Anthropic, OpenAI, Google, Mitchell et al.) and say why statistics that count "agents" are not comparable.
- [ ] Reader can sketch the agent loop with the model holding the locus only at the proposal step, and list the requirements at each seam (observation, proposal, authorization, execution, feedback, completion).
- [ ] Reader can place a decision point on Mitchell et al.'s ladder and say what the rung demands of code, including why code execution makes the environment the boundary.
- [ ] Reader can name the four properties that change the architecture, each with dated evidence and the response it calls for, and can explain with the Double Credit why distributed-systems rules still apply.
- [ ] Reader can produce a decision-point map (the Ostrell Answerdesk and Closewise examples) and recognize the failure scenarios in the chapter's table, with detection, containment and recovery for each.
- [ ] Reader can choose an action-space shape (fixed options, narrow tools, general tools, code execution, computer use) for given requirements.
- [ ] Reader will not mistake an instruction in a prompt for a limit.

## Non-goals

- When a model-held decision point is worth it, the decision ladder, error-compounding arithmetic and verifiability: [[when-agents-are-justified]].
- Autonomy tiers, action classes and the consequence–reversibility grid: [[autonomy-and-consequence]].
- Bounded loops, budgets, stop conditions and the three execution styles: [[workflows-loops-and-autonomous-agents]].
- The full reference architecture and the runtime: [[agentic-reference-architecture]], [[agent-runtime]].
- Prompt-injection defenses, idempotency mechanics and sandbox technology, which are only named here and linked.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Google's "Agents" whitepaper wording is cited from secondary summaries; replace with the primary text if it becomes fetchable.
- Whether Feng et al.'s autonomy certificates have been adopted by any body was not checked; the chapter uses only the "reassess when tools change" principle.
- The Answerdesk decision-point map is simplified to nine rows; [[agent-runtime]] or [[domain-customer-operations]] may need a fuller version.

## Decision log

- **2026-10-28** — Adopted a control-flow definition applied per decision point over the vendor definitions applied per product, because it can be checked in code and determines testability, worst-case cost and blast radius. Kept Anthropic's "agentic system" umbrella so that workflows with model steps are in scope.
- **2026-10-28** — Introduced the *decision-point map* as the chapter's practical tool and made Keelson's registration rule ("the enforcement column may not be empty for a model-held point that can change an external system") canonical for Ostrell, rather than leaving the definition abstract.
- **2026-10-28** — Used the trade-off table for action-space shapes instead of a workflow-versus-agent ladder, to avoid re-teaching the decision ladder owned by [[when-agents-are-justified]].
- **2026-10-28** — Kept "Across Domains" short, as Part I allows; benchmark results are cited without naming superseded model versions.

## Sources

- **Internal**
  - [[meet-ostrell]], the scenario ledger — agents, tiers, volumes and the Double Credit, Half-Posted Accrual, Weekend Fan-out and Lost Handoff figures.
  - [[when-agents-are-justified]], [[autonomy-and-consequence]], [[workflows-loops-and-autonomous-agents]] — neighbours this chapter hands to.
  - Interview designs: `agentic-platform-foundations` (steps `naive`, `control-flow`), `ai-coding-cli` (step `agent-loop`), `agentic-support-platform`, `agentic-finance-platform`, `agentic-healthcare-platform`, `agentic-public-benefits-platform` — design examples only.
- **External**
  - Anthropic, *Building effective agents* (2024); OpenAI, *A practical guide to building agents* (2025) — workflow versus agent definitions.
  - Mitchell et al. (2025) — ladder of model control; Parasuraman, Sheridan and Wickens (2000) — four functions of automation; Feng et al. (2025) — autonomy as a design choice.
  - ReAct, Toolformer, Reflexion, chain-of-thought — origins of the loop.
  - τ-bench, TheAgentCompany, CRMArena-Pro, Thinking Machines (2025), Anthropic autonomy study (2026), METR time horizons — evidence for the four properties.
  - MCP specification 2026-07-28, OWASP LLM06:2025, Willison's lethal trifecta — enforcement outside the model.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: Answerdesk stop row says step budgets (turn vs exchange, ruling 19); cut the TheAgentCompany cost arithmetic and the *Moffatt* case (owned by when-agents-are-justified and autonomy-and-consequence) and linked them; qualified METR's modeling-sensitivity range after checking the March 2026 note. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
