---
status: accepted
revised: 2026-10-28
---

# Spec: Part IV — CONTEXT: Context, Knowledge, Memory and State

## Intent

Orient the reader to Part IV: what an agent knows at each step and how errors in it are contained. Make the part's central distinction explicit (conversation history vs working context vs durable task state vs long-term memory, each with its own writer and lifetime) and state the argument as one line of reasoning across the five chapters: the working context is computed from the other stores; retrieval fills it and grounding checks it; memory gets the strictest write path; task state is never written by the model; and because wrong facts still travel from output to memory and back into context, every fact carries its source and age and code checks them before acting. Frame it through the Ostrell cases the chapters use.

## Audience

Chief architects, principal engineers and platform leads who design or review how agents assemble context, retrieve knowledge, remember and recover.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, exactly three KEY POINTS and a FAILURE PATTERNS THIS PART ADDRESSES callout with exact pattern names linked to where-agentic-systems-go-wrong.html.
- [ ] Contains a table of the four stores (writer, lifetime, what it holds) and explains how an error propagates among them.
- [ ] States the argument as one chain across the five chapters, not a list of summaries.
- [ ] Lists the questions the reader will be able to answer.
- [ ] Ostrell numbers match the chapters and the ledger (37 of 52 postings, €2.84 million; 11.2% → 2.4%; 41 of 57 second-revisit proposals; 11 failed visits; 14 quotes, €46,000, 3 later drafts from account briefs); Ostrell named as fictional once.
- [ ] States the hand-off from Part III ([[part-3]], the Lost Handoff) and to Part V ([[part-5]], re-read before write in tool contracts).
- [ ] One mermaid diagram with a Figure caption; ends with `## Chapters in this part`, one `[[permalink]]` per chapter in config order with what it decides and its case.
- [ ] About 500–900 words of prose.

## Non-goals

Teaching any mechanism in depth (the chapters own them); the Across Domains comparison; new citations or external factual claims.

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-28: Modeled on this book's Part III introduction and the vehicle book's part-2 introduction: callouts, a short lead, one diagram, a paragraph per chapter.
- 2026-10-28: The four-store table (history, working context, task state, memory) is placed in the lead because it is the part's central distinction; the knowledge corpus, which the chapters' tables also list, is left to retrieval-and-grounding.
- 2026-10-28: Failure patterns: Context Soup (chapters 14, 15, 18), Amnesiac Execution (16, 17) and Memory Without Expiry (16, 18), the three the style guide assigns to Part IV.
- 2026-10-28: The diagram shows the propagation loop (output → memory → later context) rather than any single chapter's architecture.

## Sources

`PLAN.md`, `_research/style-guide.md`, `_research/scenario-ledger.md`, and [[context-engineering]], [[retrieval-and-grounding]], [[agent-memory]], [[task-state-and-checkpoints]] and [[provenance-and-freshness]]. No external sources.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 1 mermaid diagram to an illustration and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
