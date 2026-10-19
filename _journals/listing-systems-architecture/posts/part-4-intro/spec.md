---
status: accepted
revised: 2026-10-19
---

# Spec: Part IV — DISCOVERY: Matching Intent to Inventory

## Intent

Orient the reader to Part IV: why search, query understanding, ranking, recommendations, map search and alerts should be designed as one discovery pipeline of read models over the listing stream, which question each chapter answers, and when to read each one. Frame the part through Veldmark's 2027 discovery decisions.

## Audience

Chief architects, search, data and ML leads, and engineering directors responsible for discovery on listing marketplaces.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three bullets) and a FAILURE PATTERNS callout using exact names linked to [[where-listing-systems-go-wrong]].
- [ ] States the argument: one pipeline with six surfaces; every surface is a rebuildable projection; structure beats cleverness; order is a policy with owners.
- [ ] A "Chapters in this part" table covers all six chapters in config order, drawn from their KEY POINTS and leads.
- [ ] Connects back to [[part-2]] and [[part-3]] and forward to [[part-5]], [[part-6]] and [[part-7]].
- [ ] A Veldmark thread, labeled fictional, matching the ledger: 17 Jan 2027 brown-out (about 9% failed searches, 48 minutes), Ranking policy v1 (Jun 2027; live NL/BE 1 Dec 2027), Motorvane carousel (41% → 8%), OpenSearch decision of 14 Sep 2027 with Listing Search API v1 and Motorvane on Elasticsearch to 2029, Hearthly geo query compiler, group saved-search service with a 5-minute p95 target for 46M saved searches.
- [ ] Ends with a hand-off to [[search-architecture]].
- [ ] 500–800 words of body.

## Non-goals

Engine comparisons, ranking methods or alert designs (the chapters own them); external factual claims.

## Modalities

Article only for now.

## Open questions

None.

## Decision log

- 2026-10-19: Modeled on RECONCILED's part introductions with this book's callout set and a chapter table.
- 2026-10-19: Failure patterns: Index-as-Database, Paid-Rank Drift and Ghost Inventory, the three that recur across most of the part's chapters.
- 2026-10-19: The Airbnb map-traffic figure from [[map-search]] is left to that chapter to avoid an external claim here.

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, and the KEY POINTS and lead paragraphs of [[search-architecture]], [[query-understanding]], [[ranking]], [[recommendations]], [[map-search]] and [[saved-searches-and-alerts]]. No external factual claims.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: made the Ranking policy v1 summary match the ledger (paid cap plus relevance floor) and credited the brands for the carousel decision. *(AI-mediated session)*
- **2026-10-19** — Added 1 inline illustration (article-illustrator); figures renumbered. *(AI-mediated session)*
