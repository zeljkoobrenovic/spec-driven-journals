---
status: accepted
revised: 2026-10-22
---

# Spec: Part IV — DISCOVERY: From Intent to Bookable Stay

## Intent

Orient the reader to Part IV: why stays discovery retrieves promises rather than documents, why every surface must show the same bookable total, why order is a bounded policy with owners, where hotels (comparison) and homes (evidence, approximate location) differ, and what each of the five chapters decides. Frame it through the Corvane systems and cases the chapters use (Elasticsearch with Pricegrid, OpenSearch with Almanac, the destination graph, Ranking Policy v1 and the ranking council, the Trip Intent Service, the Novaks' Alfama apartment).

Productscape domains: the union of the part's chapters (TAM srch, home, prop, room; HSM srch, insp, list).

## Audience

Chief architects, search, ranking and ML leads, and engineering directors responsible for discovery and the property page.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three) and a FAILURE PATTERNS callout using exact names linked to where-stay-platforms-go-wrong.html.
- [ ] States the argument (one pipeline with one promise) and names where hotels and homes differ: comparison and exact address vs evidence and a coarse public point; shared contract and quote, templates by offer shape.
- [ ] Two figures with short captions: comparison versus evidence, and the one-pipeline-one-promise flow.
- [ ] A "Chapters in this part" list with one paragraph per chapter in config order, each linking the chapter and saying what it decides.
- [ ] Corvane facts match the ledger and chapters: the 13 May 2027 Lisbon query, four "Lisbons", the €2.4 million map bill, Prinsenkade's fall from 6 to 23, Ranking Policy v1 replacing Front Row multipliers, the Novaks' €145 and €1,271.20.
- [ ] Ends with a hand-off to [[stays-search-architecture]]; 500–900 words of body.

## Non-goals

Teaching index design, geo indexing, learning to rank or recommendation models (the chapters own them); external factual claims.

## Modalities

Article only for now.

## Open questions

None.

## Decision log

- 2026-10-21: Modeled on LISTED's part introductions, with a mermaid diagram and a paragraph-per-chapter list, per the BOOKED brief.
- 2026-10-21: Failure patterns: Phantom Availability, Price Drift and Pay-to-Rank Creep; The Hotel-Shaped Home and The Unwatched Model recur but are left to the chapters.
- 2026-10-21: No real-company claims in the intro; the documented learning-to-rank lineage and AI search launches stay in [[stays-ranking]] and [[stays-search-architecture]].

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, and the callouts, leads, Setting the Scene sections and Chief Architect's views of [[stays-search-architecture]], [[destinations-and-maps]], [[stays-ranking]], [[personalization-and-recommendations]] and [[property-page-and-room-selection]]. No external factual claims.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: renamed Visibility Plus to Front Row, fixed a stray comma. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 1 mermaid diagram to an illustration and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 834 → 832 prose words; both figure captions cut to one line (they restated the lead paragraphs); two chapter-list sentences tightened. Spec: the stale "one mermaid diagram" criterion now describes the two figures. *(AI-mediated session)*
