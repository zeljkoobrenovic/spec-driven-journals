---
status: accepted
revised: 2026-10-21
---

# Spec: Zillow, Rightmove, Idealista and REA: What Property Portals Teach

## Intent

Use the public record of the best-documented property portals (Zillow, Rightmove, REA Group and Idealista, with CoStar as a counterpoint) as a tested case of what real estate teaches listing-system architects. The page must give the Zillow Offers episode its documented weight: the February 2021 move of the Zestimate into a cash offer, and the November 2021 wind-down in Zillow's own words. It must show that licensed supply and the unit of charge shape a portal's architecture, keep documented fact, the author's interpretation and labeled inference visibly apart, and say plainly where the evidence is thin (REA engineering, everything technical about Idealista). After reading, a Chief Architect should have three rules. Govern models by the decision they drive, and treat a tier change as a governance event. Carry supply terms as data through every pipeline. Design the monetization core for the unit of charge.

## Audience

Chief and enterprise architects, ML and data leads, and engineering directors of real-estate portals and of groups that own them. They know AVMs, feeds and search engines; they need the evidence trail and the judgement.

## Success criteria

- [ ] A dated timeline section replaces the Veldmark scene, and every company fact carries a source and publication year.
- [ ] Zillow Offers is covered from the 2021 Zestimate-offer launch to the wind-down, using the 8-K and shareholder-letter quotes, with lessons labeled as the author's reading.
- [ ] The unit-of-charge comparison (Rightmove per advertiser, REA per listing, Zillow per lead) is shown in a table and a diagram, with a warning against comparing values across rows.
- [ ] Inferences about company internals appear only in callouts labeled `INFERENCE, NOT DOCUMENTED`; no invented service names, volumes or architectures.
- [ ] Idealista and REA engineering gaps are stated explicitly rather than filled in, and an explicit "Where the Public Evidence Stops" section lists the unanswered questions.
- [ ] A trade-off table, a vertical-differences table and at least two mermaid diagrams.
- [ ] The final section compares the cases to the book's patterns and to Hearthly's 2027 decisions (Hearthly Direct, Valuo metrics, the commission-share pilot, Keybridge neutrality), using ledger-consistent facts and linking the owning chapters.
- [ ] Questions to ask (6–10) and grouped Sources and Evidence.

## Non-goals

- Not a company profile or an investment view; no verdict on the pending litigation.
- Does not re-teach the feed contract ([[listing-ingestion]]), entity resolution ([[entity-resolution]]), decision tiers ([[ml-platform]]) or monetization mechanics ([[monetization-models]], [[products-and-entitlements]]); it summarizes and links.
- Does not cover AVIV Group ([[case-aviv]]) or automotive portals ([[case-automotive]]).
- Does not describe REA's or Idealista's current systems, for which no public evidence was found.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- REA's engineering blog (rea-group.com) refused automated fetches; a reviewer with a browser should check for current architecture posts.
- Idealista's revenue, margin and closing date of the 2024 Cinven deal are not confirmed from a primary source.
- The class and theory of the Rightmove collective claim (certification hearing November 2026).
- Whether Zillow ever published the pricing and exposure controls of Zillow Offers.
- Status of the remaining FTC and state complaints named in Zillow's 2025 annual report.

## Decision log

- **2026-10-19** — Led with the Zillow Offers episode and added the February 2021 Zestimate-as-offer launch (verified via CNN Newsource) as the documented tier change, which earlier chapters did not cite.
- **2026-10-19** — Organized the comparison around the unit of charge rather than technology stacks, because the filings document economics far better than engineering.
- **2026-10-19** — Kept Idealista and REA sections short and explicit about gaps rather than padding with inference; used CoStar only as a lead-ownership counterpoint.
- **2026-10-19** — Reworded Zillow's training-use risk factor to the 10-K's text ("including the training of models"), which differs from the research brief's paraphrase. No new ledger facts added.

## Sources

- **Internal**
  - [[ml-platform]], [[entity-resolution]], [[listing-ingestion]], [[monetization-models]], [[products-and-entitlements]], [[marketplace-regulation]], [[saved-searches-and-alerts]], [[modernization-and-migration]], [[ai-in-listing-systems]] — patterns the case tests.
  - [[meet-veldmark]] and the scenario ledger — Hearthly and Valuo decisions used in the comparison.
  - `_research/brief-real-estate-portals.md` (Parts B and C), `brief-monetization-economics.md`, `brief-search-discovery.md`, `brief-platform-data-ml.md`.
- **External** (re-verified 19 October 2026)
  - Zillow 8-K and Q3 2021 shareholder letter; Zillow 10-K for 2025; CNN Newsource on Zestimate offers (2021).
  - Rightmove FY2025 and H1 2026 results; Rightmove RTDF specification v1.4.1.
  - REA Group FY26 ASX announcement (2026).
  - Online Marketplaces on the Cinven–Idealista deal (2024), Idealista duplicate control (2021) and the Compass ruling (2026); The Mortgage Point on Compass's dismissal (2026).
  - CoStar 10-K for 2025.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: re-verified 12 load-bearing claims against filings and results; hedged the Idealista deal valuation, corrected Rightmove retention to "above 90%", expanded MLS/IDX, American spelling, timetoread updated. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,800 → 6,867 prose words; opening now ties the case to [[case-aviv]], the Part IX question and the chapters it tests; 3 headings renamed (one aligned with sibling cases); Zestimate-error paragraph split; teaser first sentences replaced. *(AI-mediated session)*
- **2026-10-20** — Trade-offs heading capitalized as in the 45 chapters. *(AI-mediated session)*
- **2026-10-20** — "The final section" now points to the Veldmark comparison near the end, since two sections follow it. *(AI-mediated session)*
- **2026-10-20** — Replaced 4 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`). *(AI-mediated session)*
- **2026-10-21** — Renamed failure patterns to match [[where-listing-systems-go-wrong]]: Seeing Double, Search as System of Record, Multiplier Creep, Fast Mail for Fraudsters, The Copy-Paste Country, Deal-Shaped Architecture, The Forced Fit, Billing by Guesswork, Set-and-Forget AI. *(AI-mediated session)*
