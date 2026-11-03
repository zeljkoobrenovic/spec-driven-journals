---
status: accepted
revised: 2026-10-28
---

# Spec: Part VIII — EVIDENCE: Evaluation and Observability

## Intent

Orient the reader to Part VIII as one line of reasoning: an agent's output varies and its work is a trajectory, so evaluation needs levels and pass^k; the levels need suites, graders and gates that run on every manifest change; production needs traces and outcome metrics that record what actually answered; and the evidence must change autonomy per action class, raised by a signed, pre-registered criterion and lowered automatically. Carry the Ostrell thread (Alias Drift, Fixture Purge, Rubber Stamp, the October 2027 autonomy review) and the hand-offs from Part VII and to Part IX.

## Audience

Chief architects, platform leads, evaluation leads and risk owners deciding what evidence an agent must produce before it ships or gains autonomy.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, exactly three KEY POINTS and FAILURE PATTERNS THIS PART ADDRESSES with exact pattern names linked to where-agentic-systems-go-wrong.html.
- [ ] States the part's argument as one chain across the four chapters, not as a list of summaries.
- [ ] Says once that Ostrell is fictional; Ostrell numbers match the ledger and chapters (4% to 11% over 4 days; 96.1% to 89.4%; 9 PRs, 2 merged; 4,812 approvals, 99.3%, 6 seconds; the October 2027 outcomes).
- [ ] Names the questions the reader will be able to answer.
- [ ] Hands off from Part VII (controls) and to Part IX (time and money).
- [ ] One mermaid diagram with a Figure caption.
- [ ] Ends with `## Chapters in this part`: each chapter as a `[[permalink]]` with what it decides and its Ostrell case, in config order.
- [ ] About 500–900 words of prose; no new citations.

## Non-goals

Teaching evaluation levels, pass^k, graders, LLM-as-judge, trace design, OTel conventions, gates or promotion criteria (the four chapters own them); the Across Domains comparison; any external factual claim.

## Modalities

Article only for now.

## Open questions

- `policy-enforcement-and-audit`, the last chapter of Part VII, was not yet written on 2026-10-28; its closing paragraph should hand off to [[part-8]].

## Decision log

- 2026-10-28: Modeled on the vehicle book's part-2 introduction: callouts, a short lead stating the chain, one diagram, an Ostrell paragraph, a paragraph per chapter.
- 2026-10-28: Failure patterns: Vibe Evals, The Silent Upgrade and Autonomy by Default, the three the style guide assigns to Part VIII and that recur across its chapters; The Rubber Stamp appears in the Ostrell thread instead.
- 2026-10-28: The Alias Drift is the lead case because all four chapters use it; the October 2027 review closes the thread because it is where evidence changes tiers.

## Sources

`config.yaml`, `PLAN.md`, `_research/style-guide.md`, `_research/scenario-ledger.md`, and [[evaluating-agentic-systems]], [[building-agent-eval-suites]], [[agent-observability]], [[evidence-for-autonomy]]. No external factual claims.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 1 mermaid diagrams to illustrations and added 1 conceptual figures (article-illustrator). *(AI-mediated session)*
