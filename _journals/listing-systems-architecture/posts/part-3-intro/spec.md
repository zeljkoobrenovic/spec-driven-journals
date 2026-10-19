---
status: accepted
revised: 2026-10-19
---

# Spec: Part III — SUPPLY: Getting Inventory In

## Intent

Orient the reader to Part III: supply as one chain rather than five features. A record enters through a channel under a contract, is normalized and enriched with provenance, is resolved against what the marketplace already knows, is published and later unpublished within a freshness target, and is judged by professionals against their own systems. Show how the part consumes Part II's models and Part I's liquidity targets, and what Part IV depends on.

## Audience

Architects and engineering leads responsible for ingestion, catalog, publication, partner integration or professional products in a listing marketplace.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three bullets) and a failure-pattern callout with exact names linked to [[where-listing-systems-go-wrong]].
- [ ] KEY POINTS synthesize the five chapters' own KEY POINTS without contradicting them.
- [ ] A "Chapters in this part" table lists all five chapters in config order as cross-links | question | read it when.
- [ ] Connects to [[part-2]] (schemas, aggregate, accounts), to Part I's liquidity metrics and to [[part-4]].
- [ ] Veldmark thread (labeled fictional) matches the ledger and chapters: 8 March 2027 snapshot incident (38,400 listings), Supply Contract v1 (Sep 2027), Essen Golf's 31 decoded attributes, Lyon apartment clustered without Keybridge data, 90-second p95 SLA card, 23 vs 14 Golf leads.
- [ ] Hands off to [[listing-ingestion]].
- [ ] 500–800 words.

## Non-goals

Re-teaching feed contracts, provenance, matching, pipeline budgets or neutrality design (the chapters own them); search and alerts ([[part-4]]); the moderation gate's design ([[trust-and-safety-architecture]]).

## Modalities

Article only.

## Open questions

None.

## Decision log

- 2026-10-19: Structure follows the sibling [[part-2]] intro for consistency; no diagram, to stay within 800 words.
- 2026-10-19: Failure patterns chosen: Feed Roulette, The Duplicate Echo, Ghost Inventory, each the lead pattern of at least one chapter in the part.

## Sources

Internal: [[listing-ingestion]], [[normalization-and-enrichment]], [[entity-resolution]], [[publication-pipeline]], [[professional-seller-tooling]], [[meet-veldmark]]; `_research/scenario-ledger.md`.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: restored [[part-1]] and [[part-5]] links in the connections section. *(AI-mediated session)*
- **2026-10-19** — Added 1 inline illustration (article-illustrator); figures renumbered. *(AI-mediated session)*
