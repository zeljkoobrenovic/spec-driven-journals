---
status: accepted
revised: 2026-10-28
---

# Spec: Part XI — DOMAINS: How Requirements Change Across Domains

## Intent

Orient the reader to Part XI with one argument: autonomy is earned from what a domain makes cheap to undo and cheap to check, not from the model. Coding has both inside the workspace; customer operations loses most of both, so commitments are rendered from records under small caps; the back office writes into records others rely on, so the agent is a maker stopping at a staging store with an independent approver; high-stakes decisions put rules in the deciding or vetoing seat and a named human on every adverse outcome. The platform stays the same; the gate, the gating predicate and the fail-safe direction change. Frame the part through the cases its chapters use: the Fixture Purge (July 2027), the two-thirds slide and Shadow Reminder Gap (November 2027), the audit committee of 23 November 2027, and the clinical and public-benefits design examples read for Peoplepoint's performance-review request.

## Audience

Chief architects, platform leads and domain risk owners deciding which controls a new agent's domain demands, and what can be copied from agents already in production.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, exactly three KEY POINTS and a FAILURE PATTERNS THIS PART ADDRESSES callout with exact pattern names linked to where-agentic-systems-go-wrong.html.
- [ ] States the part's argument as one line of reasoning across the four chapters (workspace → caps and rendered commitments → staging store and independent approver → rules decide, humans own adverse outcomes), not a list of summaries.
- [ ] Includes a compact comparison table of the four domains' consequence profiles (reversibility, who is harmed, the verifier, the human gate, the binding constraint), drawn only from the chapters.
- [ ] Ostrell is said to be fictional once; the high-stakes designs are labeled design examples; the cautionary cases are labeled non-LLM; every number matches the chapters (9 PRs, 2 merged, about 1,100 order lines; 41%, 400 sampled, 44% re-contacted, 7 days; €250 cap; 23 November 2027).
- [ ] Lists the questions the reader will be able to answer.
- [ ] Hands off from Part X ([[owning-agentic-systems]], the platform held still) and to the Reference section ([[source-coverage]]).
- [ ] `## Chapters in this part` gives each chapter as `[[permalink]]` in config order with what it decides and its case, and ends with "Begin with".
- [ ] No external citations.

## Non-goals

Teaching verifier capture, outcome approval, the contact policy, verified resolution, the back-office spine, gate semantics, the decide/veto/screen roles or fail-safe direction: [[domain-coding-agents]], [[domain-customer-operations]], [[domain-back-office]] and [[domain-high-stakes-decisions]] own them. No new evidence or regulatory analysis.

## Modalities

Article only for now.

## Open questions

- Chapter 44 says Ostrell's register caps employment decisions at A1, while chapter 43 caps decisions about a person's employment, pay or rights at A0; the intro avoids the tier and says only that the agent decides nothing about an employee. Reconcile in the chapters.

## Decision log

- 2026-10-28: Modeled on this book's part-10 introduction and the vehicle book's part-2 introduction: callouts, a short lead, one diagram, the cases, then a paragraph per chapter.
- 2026-10-28: Added the consequence-profile table the part brief asked for; columns are the four domains, rows the five properties, each cell compressed from the chapter's own profile and controls tables.
- 2026-10-28: Failure patterns: Autonomy by Default and The Rubber Stamp (all four chapters) and Ambient Authority (coding disasters, Closewise prototype); The Silent Upgrade and Vibe Evals are left to the chapters.

## Sources

`config.yaml`, `PLAN.md`, `_research/style-guide.md`, `_research/scenario-ledger.md`, and [[domain-coding-agents]], [[domain-customer-operations]], [[domain-back-office]] and [[domain-high-stakes-decisions]] read in full; the hand-off at the end of [[owning-agentic-systems]]. No external factual claims.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 1 mermaid diagram to an illustration and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
