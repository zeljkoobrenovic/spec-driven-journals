# Review — Part IV (chapters 19–20), 2026-10-20

Both pages were already in good shape: the format, opening blocks, required sections, figure numbering, trade-off tables, size tables and attributions were all correct. The fixes below are targeted.

## 19-feature-velocity (`feature-velocity`)

- **METR figures, checked with WebFetch against metr.org.** 2025 RCT: 16 developers, 246 issues, 19% slower, 24% speedup expected beforehand, 20% believed afterwards; the page is now marked out of date. Feb 2026 update (24 Feb 2026): 57 developers (10 returning, 47 new), 800+ tasks; −18% time (CI −38% to +9%) for returning developers and −4% (CI −15% to +9%) for new ones; selection effects, withheld tasks, and unreliable time tracking with concurrent agents. **Fixed:** the text now carries the exact figures and the out-of-date note, and the source entries say the same.
- "With tens of thousands of PRs a week" had no source. **Fixed:** it now uses the documented uReview volume ("tens of thousands of diffs", 2025), as the reconciliation table says.
- RADAR growth: "most of the growth" is now "more than 80% of that growth", as the brief says.
- COO named (Andrew Macdonald, Fortune, May 2026).
- Spot-checks passed: the agent-share figures (10/11/15/70%+, definitions stated), the Eng Metrics Dashboard history, NPS −50 → +8, uReview's 39 developer-years and 10-minute assumption, the DX Annual talk (16 Apr 2026), and the transcript quotes (diff → feature velocity, the 100-diffs quote, capability overhang, the PRD/launch/rollout bottleneck).
- **Left as is:** the page runs about 5,800 words including sources, and the body is within about 5% of the 5,500 limit with no repetition worth cutting. "leverage" appears only inside a direct quote.

## 20-the-engineer-as-context-builder (`the-engineer-as-context-builder`)

- **Customer-support duration, checked against the transcript (line 350):** "that used to take weeks, now it's like order of" — the transcript breaks off there. The article gave no new duration, but it cited "the ledger", an internal research file, in published prose. **Fixed:** the article now says the episode gives only the old figure ("weeks") and that the transcript breaks off before the new one. The record-gaps bullet is reworded to match. Figure 2 and KEY POINTS say only "weeks".
- "Most quoted passage, and the show notes reproduce it" was not supportable: the show notes quote only the central line and the skills list. **Fixed.**
- Code Inbox's risk score and blast radius were presented as present. **Fixed:** "being added as of October 2026", in line with [[code-review-signals]].
- DevPods date aligned with the reconciliation wording (2017–2018 monorepo move; the episode says 2017).
- Context-graph row: replaced "AI platform team", which the record does not name, with "built with help from the graph platform team".
- **Anthropic study, checked with WebFetch:** 132 surveyed and 53 interviewed, 59% (60% in the key findings), 28% a year earlier, ~50%, 27%, 0–20% fully delegated, "paradox of supervision", the 70%+ reviewer quote, and practicing without AI are all confirmed. Added the 59/60 note.
- Spot-checks passed: the Spotify Honk Part 2/3 claims, Thoughtworks Vol. 34 rings, the METR time-tracking point, and the role quotes (the "context" quote and the "code smells… regressions" quote, with "recreations" corrected to "regressions").

## Verify

The build is clean for uber-ai-infra. render_check: `feature-velocity` OK. `the-engineer-as-context-builder` has one unresolved link, `[[the-retrofit-playbook]]`, which is allowed because that page is not written yet. A Changelog line was added to both specs.
