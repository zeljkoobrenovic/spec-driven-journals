---
status: accepted
revised: 2026-10-28
---

# Spec: Part IX — ECONOMICS: Performance, Cost and Scale

## Intent

Orient the reader to Part IX with one argument: the context an agent re-reads on every model call sets its latency, most of its cost and its share of the shared rate limit, so time, money and capacity are one design problem. The controls (deadlines, quota pools, run budgets, per-step model choice, prefix layout, context budgets) are enforced in the runtime and gateway, and the results are judged per successful task. Frame the part through the Ostrell cases its chapters use: the Close-Day Queue of 2 November 2027, the Weekend Fan-out, and the May 2027 prefix that broke the cache.

## Audience

Chief architects, platform leads and engineering directors who must make agents fast enough, affordable and bounded, and defend the numbers to product owners and the CFO.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, exactly three KEY POINTS and a FAILURE PATTERNS THIS PART ADDRESSES callout with exact pattern names linked to where-agentic-systems-go-wrong.html.
- [ ] States the part's argument as one line of reasoning across the three chapters, not a list of summaries.
- [ ] Ostrell is said to be fictional once; every number matches the chapters (41 hours, €8,700; 11% and 76% cache-read share; p95 14 s and abandonment 9% to 17%; ceiling 3.4 vs 1.2 exchanges per second against a 2.1 peak; 9.6 s to 1.8 s; €0.39; €90 cap).
- [ ] Lists the questions the reader will be able to answer.
- [ ] Hands off from Part VIII (evaluation gates) and to [[part-10]] (versioned configuration).
- [ ] `## Chapters in this part` gives each chapter as `[[permalink]]` in config order with what it decides and its Ostrell case, and ends with "Begin with".
- [ ] No external citations; body after the callouts about 500–700 words.

## Non-goals

Teaching latency budgets, rate-limit ceilings, cost per successful task, routing, run budgets, prompt caching or context budgets: [[agent-latency-and-throughput]], [[agent-cost-and-model-routing]] and [[caching-and-context-budgets]] own them. No Across Domains comparison (each chapter has its own).

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-28: Modeled on the vehicle book's part-2 introduction: callouts, a short lead with the cases, one diagram, a paragraph per chapter.
- 2026-10-28: Failure patterns: The Token Bonfire (all three chapters), The Agent Committee (latency and fan-out cost) and Context Soup (context budgets); The Different Second Answer and Vibe Evals are left to the chapters.
- 2026-10-28: The diagram shows the part's thesis: one cause (re-read context) with three effects (wait, invoice, ceiling) and controls in the runtime and gateway.

## Sources

`config.yaml`, `PLAN.md`, `_research/style-guide.md`, and [[agent-latency-and-throughput]], [[agent-cost-and-model-routing]] and [[caching-and-context-budgets]] read in full; the hand-off line at the end of [[evidence-for-autonomy]]. No external factual claims.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: "turn" to "exchange" per ruling 19; trimmed to under 900 words. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 1 mermaid diagram to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
