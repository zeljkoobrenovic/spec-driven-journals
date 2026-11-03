---
status: accepted
revised: 2026-10-28
---

# Spec: Part III — ORCHESTRATION: Planning, Delegation and Coordination

## Intent

Orient the reader to Part III: how work is planned, routed, split between agents and handed between agents and people. State the part's argument as one line of reasoning about boundaries (a plan checked before execution, a route or delegation that decides who handles each step and what travels with it, a topology decision on whether another agent is warranted, a handoff that moves ownership), with one rule throughout: the model proposes, code validates, enforces and records what crosses. Frame it through the Ostrell events the chapters use (the Weekend Fan-out and the April 2027 re-run, the Lost Handoff and `billing_handoff.v1`, the May 2027 topology forum, the Sync Outage Misroute and router v2).

## Audience

Chief architects, principal engineers and platform leads who design how agentic work is decomposed, routed, delegated and transferred, and who review proposals for multi-agent designs.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, exactly three KEY POINTS and a FAILURE PATTERNS THIS PART ADDRESSES callout with exact pattern names linked to where-agentic-systems-go-wrong.html.
- [ ] States the argument as one chain across the four chapters, not a list of summaries.
- [ ] Lists the questions the reader will be able to answer.
- [ ] Says once that Ostrell is fictional; Ostrell numbers match the chapters and ledger (1,900 runs, €8,700, 41 hours; 17 worker runs, ~€57; 1 in 40, 3 wrong-contract credits, ~25,000 handoffs; 0.81 vs 0.64; 64 of 143; 71% → 97%).
- [ ] Hands over from Part II (the shape of the system) and to [[part-4]] (context).
- [ ] One mermaid diagram with a Figure caption.
- [ ] Ends with `## Chapters in this part`: one `[[permalink]]` per chapter in config order, saying what it decides and naming its Ostrell case, then hands off to [[planning-and-decomposition]].
- [ ] 500–900 words.

## Non-goals

Teaching plan validation, router calibration, topologies, handoff state machines or A2A (the chapters own them); the Across Domains comparison; new citations or external factual claims.

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-28: Modeled on the vehicle book's part-2 introduction and this book's part-1 introduction: callouts, a short lead, one diagram, a paragraph per chapter.
- 2026-10-28: Failure patterns: The Compounding Error, The Agent Committee and The Lost Handoff, the three the style guide assigns to Part III. The Token Bonfire, which several chapters also name, is left to the chapters and Part IX.
- 2026-10-28: The argument is framed as four boundaries work crosses (goal to plan, plan to handler, one context to several, one owner to the next), so the diagram shows the chain rather than components.

## Sources

`PLAN.md`, `config.yaml`, `_research/style-guide.md`, `_research/scenario-ledger.md`, and [[planning-and-decomposition]], [[routing-and-delegation]], [[single-and-multi-agent-designs]] and [[coordination-and-handoffs]]. No external sources.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 1 mermaid diagram to an illustration and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
