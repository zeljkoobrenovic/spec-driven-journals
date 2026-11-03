---
status: accepted
revised: 2026-10-28
---

# Spec: Part X — EVOLUTION: Deployment, Change and Ownership

## Intent

Orient the reader to Part X with one argument: an agent's behavior lives mostly outside its code and changes on other organizations' calendars, so the unit of change must be one pinned, hashed manifest; a nameable version can be released in stages and stopped by a pointer move; a pointer move repairs no effect, so every release needs a forward-fix plan over receipts labeled by manifest hash; and none of it holds without a named owner whose authority the platform enforces. Frame the part through the Ostrell cases its chapters use: the Alias Drift (August 2027), the Closewise model migration (November–December 2027) and the Close-Day Queue (2 November 2027) with the Keelson 2.0 roadmap.

## Audience

Chief architects, platform leads and engineering directors who must keep agents safe through model retirements, releases and reorganizations, and defend the operating model to risk owners and the CFO.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, exactly three KEY POINTS and a FAILURE PATTERNS THIS PART ADDRESSES callout with exact pattern names linked to where-agentic-systems-go-wrong.html.
- [ ] States the part's argument as one line of reasoning across the three chapters (name → stage → repair → own), not a list of summaries.
- [ ] Ostrell is said to be fictional once; every number matches the chapters (11% vs 4% rejections, four-day trace; five entries, €183,400, 196 postings re-adjudicated, 94.1% shadow agreement; ten minutes to diagnose, two hours to contain).
- [ ] Lists the questions the reader will be able to answer.
- [ ] Hands off from Part IX (configuration that changes with every release) and to [[part-11]] (the platform held still while the stakes vary).
- [ ] `## Chapters in this part` gives each chapter as `[[permalink]]` in config order with what it decides and its Ostrell case, and ends with "Begin with".
- [ ] No external citations; body after the callouts about 500–700 words.

## Non-goals

Teaching manifests, alias drift, behavior regressions, canaries, rollback plans, forward fixes, agent owners, the registry lifecycle or architecture review: [[versioning-agent-systems]], [[staged-rollout-and-rollback]] and [[owning-agentic-systems]] own them. No Across Domains comparison (each chapter has its own).

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-28: Modeled on the vehicle book's part-2 introduction and this book's part-9 introduction: callouts, a short lead with the cases, one diagram, a paragraph per chapter.
- 2026-10-28: Failure patterns: The Silent Upgrade (all three chapters), The Fire-and-Forget Action (effects a rollback cannot undo) and Autonomy by Default (unowned tiers and zombie agents); Memory Without Expiry and Vibe Evals are left to the chapters.
- 2026-10-28: The diagram shows the part's chain (manifest → staged rollout → rollback → forward fix) with the registry as the place where ownership of each step is recorded and enforced.

## Sources

`config.yaml`, `PLAN.md`, `_research/style-guide.md`, and [[versioning-agent-systems]], [[staged-rollout-and-rollback]] and [[owning-agentic-systems]] read in full; the hand-off line at the end of [[part-9]]. No external factual claims.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 1 mermaid diagrams to illustrations and added 1 conceptual figures (article-illustrator). *(AI-mediated session)*
