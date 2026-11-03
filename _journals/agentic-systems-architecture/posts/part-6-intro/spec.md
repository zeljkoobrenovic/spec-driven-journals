---
status: accepted
revised: 2026-10-28
---

# Spec: Part VI — RELIABILITY: Long-Running Work and Recovery

## Intent

Orient the reader to Part VI as one line of reasoning: a run that outlives its process needs durable execution, which records the model's decision once and replays it; because every engine runs side-effecting steps at least once, the problem moves to the tool boundary, where retries repeat a keyed action object, timeouts become unknown outcomes resolved by lookup, and per-entity guards stop parallel runs; when finishing is no longer right, deterministic code reads the effect ledger and chooses forward, backward (compensations attached to tools) or hold. Carry the Ostrell thread (Half-Posted Accrual, September 2027 close, Double Credit, Fixture Purge, compensation drill) and the hand-offs from Part V and to Part VII.

## Audience

Chief architects, platform leads and agent owners deciding how agent runs survive failure and how half-finished work is recovered.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, exactly three KEY POINTS and FAILURE PATTERNS THIS PART ADDRESSES with exact pattern names linked to where-agentic-systems-go-wrong.html.
- [ ] States the part's argument as one chain across the three chapters, not as a list of summaries.
- [ ] Says once that Ostrell is fictional; numbers match the ledger and chapters (52 / 37 / €2.84 million / 2 days; 23 entities, 61 entries once each; 212 customers, €31,400, 30 s; 11 timeouts, 0 duplicates; 9 PRs, 2 merged; about 35 minutes in the drill).
- [ ] Names the questions the reader will be able to answer.
- [ ] Hands off from Part V (tools and the effect boundary) and to Part VII (an agent that may be pushed to do the wrong thing).
- [ ] One mermaid diagram with a Figure caption.
- [ ] Ends with `## Chapters in this part`: each chapter as a `[[permalink]]` with what it decides and its Ostrell case, in config order.
- [ ] About 500–900 words of prose; no new citations.

## Non-goals

Teaching durable execution, activities, heartbeats, idempotency keys, leases, sagas, compensation or kill switches (the three chapters own them); the Across Domains comparison; any external factual claim.

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-28: Modeled on the vehicle book's part-2 introduction and this book's Part VIII introduction: callouts, a short lead stating the chain, one diagram, an Ostrell paragraph, a paragraph per chapter.
- 2026-10-28: Failure patterns: Amnesiac Execution, The Different Second Answer and The Fire-and-Forget Action, the three the style guide assigns to Part VI and that recur across its chapters.
- 2026-10-28: The Half-Posted Accrual opens the Ostrell thread because all three chapters return to it; the compensation drill closes it because it shows the part's last step, designed undo.

## Sources

`config.yaml`, `PLAN.md`, `_research/style-guide.md`, `_research/scenario-ledger.md`, and [[durable-agent-execution]], [[retries-idempotency-and-concurrency]], [[partial-failure-and-compensation]]. No external factual claims.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 1 mermaid diagram to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
