---
status: accepted
revised: 2026-10-20
---

# Spec: Part II — LISTING: Modeling the Thing Being Sold

## Intent

Orient the reader to Part II: why the listing must be modeled as a small aggregate that references governed subdomains (categories, attributes, media, location and seller accounts), which question each of the six chapters answers, and when to read each one. Frame the part through the Veldmark decisions that give the listing model its contracts in 2027.

## Audience

Chief and enterprise architects, principal engineers and listing-platform leads who are deciding what a listing is and who owns each part of it.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three bullets) and a FAILURE PATTERNS callout using exact names linked to [[where-listing-systems-go-wrong]].
- [ ] States the part's argument: a listing is an offer about a thing, a small aggregate around five governed subdomains.
- [ ] A "Chapters in this part" table lists all six chapters in config order with the question each answers and when to read it, drawn from each chapter's KEY POINTS and lead.
- [ ] Connects to Part I ([[bounded-contexts]]) and hands forward to [[part-3]] and later parts.
- [ ] A Veldmark thread, labeled fictional, whose dates and figures match the scenario ledger (lifecycle in Listing event contract v1 on 1 Jul 2027, Veldmark Place May 2027, business party registry Aug 2027, taxonomy and attribute service Oct 2027, bikes split 1 Nov 2027, media decision Nov 2027 with the hash index from Q1 2028).
- [ ] Ends with a hand-off to [[listing-aggregate]].
- [ ] 500–800 words of body.

## Non-goals

Re-teaching any chapter's content; defining terms the chapters own; external factual claims.

## Modalities

Article only for now.

## Open questions

None.

## Decision log

- 2026-10-19: Modeled on RECONCILED's part introductions, with the callout set from this book's style guide and a chapter table instead of a learning-path diagram.
- 2026-10-19: Failure patterns limited to the three strongest for the part (Category Straitjacket, Attribute Junkyard, Ghost Inventory).
- 2026-10-19: The Veldmark thread lists decisions only; numbers stay in the chapters.

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, and the KEY POINTS and lead paragraphs of [[listing-aggregate]], [[categories-and-taxonomies]], [[attribute-schemas]], [[media-pipeline]], [[location-and-geo]] and [[sellers-and-accounts]]. No external factual claims.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Added 1 inline illustration (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 628 → 632 words; lead now ties the part to Part I's boundaries and listing ownership; argument sentence tightened; no headings changed. *(AI-mediated session)*
