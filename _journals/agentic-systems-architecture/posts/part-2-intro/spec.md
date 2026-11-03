---
status: accepted
revised: 2026-10-28
---

# Spec: Part II — ARCHITECTURE: The Reference Architecture

## Intent

Orient the reader to Part II: which components must surround a model whose proposals vary, and what each must own and never do. State the part's argument as one line of reasoning across its five chapters (draw the map and the one path, then make each boundary enforceable in turn: the gateway toward providers, the runtime around the loop, integration toward systems of record, interaction toward people), and frame it through the Ostrell events the chapters use (the January 2027 inventory, the February audit finding, the Quiet Failover, the message that arrived four seconds late, the August escalation review, and the fixes that followed).

## Audience

Chief architects, principal engineers and platform leads who must design or review the shared components that every agent in an organization runs on.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, exactly three KEY POINTS and a FAILURE PATTERNS THIS PART ADDRESSES callout with exact pattern names linked to where-agentic-systems-go-wrong.html.
- [ ] States the argument as one chain across the five chapters, not a list of summaries.
- [ ] Lists the questions the reader will be able to answer.
- [ ] Ostrell numbers match the chapters (212 tools and 118 with service-account keys; 31 provider keys; 40 entries without an approver; 9 contracts; 23 late-correction cases and 1 after; 500 escalations, 38% to 9%; 20 minutes).
- [ ] States the hand-off from Part I (tiers and limits) and to Part III ([[part-3]]).
- [ ] One mermaid diagram with a Figure caption.
- [ ] Ends with `## Chapters in this part`: one `[[permalink]]` per chapter in config order, saying what it decides and naming its Ostrell case.
- [ ] 500–900 words.

## Non-goals

Teaching any component in depth (the chapters own them); the Across Domains comparison; new citations or external factual claims.

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-28: Modeled on the Part I introduction of this book and the vehicle book's part-2 introduction: callouts, a short lead, one diagram, a paragraph per chapter.
- 2026-10-28: Failure patterns: Ambient Authority (chapters 05, 06, 08), The Token Bonfire (06, 07) and The Lost Handoff (08, 09), chosen so that every chapter is covered; the style guide assigns no patterns to Part II.
- 2026-10-28: The diagram follows a run along the one path rather than redrawing the full reference architecture, which chapter 05 owns.

## Sources

`PLAN.md`, `_research/style-guide.md`, and [[agentic-reference-architecture]], [[models-and-the-model-gateway]], [[agent-runtime]], [[agents-in-the-enterprise]] and [[agent-interaction-design]]. No external sources.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: corrected the February audit finding (40 sampled entries whose approvals the ERP could not show, not 40 entries with no approver) and the May–June timing of the 23 late-correction cases. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 1 mermaid diagrams to illustrations and added 1 conceptual figures (article-illustrator). *(AI-mediated session)*
