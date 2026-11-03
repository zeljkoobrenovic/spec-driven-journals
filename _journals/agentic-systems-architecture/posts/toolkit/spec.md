---
status: accepted
revised: 2026-10-28
---

# Spec: Toolkit: Templates for Agentic Architecture Decisions

## Intent

Give the reader copyable templates for the records an architect keeps before agents may act on anything that matters: why a decision point is a model's, how far each action class may go, what a tool promises, what crosses a delegation or handoff, what an effect and its approval bind, where the trifecta sits, what gates a release, what a version pins, how a rollout is reversed, what the registry enforces and how an incident is contained. Each template comes from the chapter that teaches it, keeps that chapter's field names, says who fills it and who signs, and is filled in once with a few lines of Ostrell (fictional) whose numbers match the scenario ledger. A one-page design-review checklist collects the most important "Questions to ask" across the book, grouped by part.

## Audience

Chief and enterprise architects, principal engineers and platform leads who run agent design reviews; agent owners and risk owners who sign tiers; security architects and evaluation leads who own the threat model and the gates.

## Success criteria

- [x] Opens with IN THIS SECTION, YOU WILL; exactly three KEY POINTS; a FAILURE PATTERNS block with three exact pattern names; `<br>`; a lead; a "find the template" table (template · use it when · chapter).
- [x] Twelve templates in the contract's order, each with when to use it, who fills it, the template as a table or fenced YAML block, a short Ostrell example labeled fictional, common mistakes, and a `[[chapter]]` link.
- [x] Field names match the owning chapters: rung justification ([[when-agents-are-justified]]); effect type, C1–C4 bands, grid ceilings and limits ([[autonomy-and-consequence]]); `billing.issue_credit` 3.2.0 contract fields ([[tool-contracts]]); `DelegationContract` and `HandoffPayload` ([[routing-and-delegation]], [[coordination-and-handoffs]]); action object field groups and lifecycle ([[side-effects-and-external-actions]]); `ApprovalRecord` and revalidation ([[human-oversight-and-bounded-autonomy]]); the threat-model YAML and B1–B8 ([[agent-threat-model]]); the pyramid, `EvalCase` and gate criteria ([[evaluating-agentic-systems]], [[building-agent-eval-suites]]); the manifest YAML and registration checks ([[versioning-agent-systems]]); plan elements, guardrail families and forward-fix classes ([[staged-rollout-and-rollback]]); `AgentRegistryEntry` and the runbook ([[owning-agentic-systems]]).
- [x] Ostrell examples use ledger figures exactly (Peoplepoint 91% vs 98.4%; credits ≤ €250 at A2 with the October 2027 limits and demotion triggers; Scout's delegation budget; `billing_handoff.v1`; the €420 R2 credit; Scout's full trifecta; Closewise suite v2; `cw-2027.09.3`; the Closewise migration and the 7 December forward fix; Answerdesk's registry entry; the Fixture Purge).
- [x] The design-review checklist covers Parts I–XI with questions taken from the chapters' "Questions to ask".
- [x] One mermaid diagram shows how the records reference each other; cross-links use only valid permalinks; no new external citations; 4,000–7,000 words excluding table separators.

## Non-goals

- Re-teaching the reasoning behind each template; each section summarizes and links to its chapter.
- The decision-point map ([[what-makes-a-system-agentic]]), context manifest ([[context-engineering]]), provenance envelope ([[provenance-and-freshness]]) and task record ([[task-state-and-checkpoints]]), which are linked, not reproduced.
- Definitions ([[glossary]]), the interview-source map ([[source-coverage]]) and the source list ([[bibliography]]).
- Downloadable file formats.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Approval expiry for Answerdesk credits: [[human-oversight-and-bounded-autonomy]] says an approval is valid 4 hours; [[side-effects-and-external-actions]] says A1 credit approvals expire after 24 hours (local rule). Template 5 follows the approvals chapter; the editor should align one of the two.
- The Fixture Purge hold dates differ between [[partial-failure-and-compensation]] and [[domain-coding-agents]]; Template 11 avoids dates for the hold and its release.
- Manifest labels follow consistency ruling 23 (`cw-2027.09.3`, `cw-2027.10.2`); chapters 38 and 39 print Closewise labels without the prefix.

## Decision log

- **2026-10-28** — Chose the twelve templates in the brief, merging PLAN's "autonomy tier register" and "action class table" into one register and folding the "approval gate spec" into the approval record, because the chapters define them as one record each.
- **2026-10-28** — Reproduced the threat-model YAML of [[agent-threat-model]] verbatim, since that chapter points to this page for it; other templates are abridged skeletons of the chapters' code.
- **2026-10-28** — Wrote the design-review checklist as task-list items grouped by part, one to five questions per part, each linking its chapter, rather than a table, so it can be ticked in the rendered page.

## Sources

- **Internal**: the chapters linked above; `_research/scenario-ledger.md`, `_research/consistency-issues.md` (rulings 6, 9, 10, 21, 22, 23) and `PLAN.md` (Reference: toolkit).
- **Interview design examples**: `agentic-platform-foundations` (step `eval-obs`, `security`), `agentic-support-platform` (step `compliance-eval`, `escalation`), `agentic-finance-platform` (step `ledger`).
- **External**: none new; the chapters cite them.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 1 mermaid diagram to illustrations and added 0 conceptual figures (article-illustrator). *(AI-mediated session)*
