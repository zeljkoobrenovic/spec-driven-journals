---
status: accepted
revised: 2026-10-19
---

# Spec: Part VII — PLATFORM: The Distributed System Underneath

## Intent

Orient the reader to Part VII: why the platform beneath a listing marketplace should be built as a set of published contracts (events, registered copies, URLs, governed metrics, experiments, models, tenants and journey objectives) rather than imposed products, which question each of the eight chapters answers, and when to read each one. Frame the part through Veldmark's 2027 platform decisions.

## Audience

Chief architects, platform-engineering, data and ML leads, and principal engineers responsible for the shared layers beneath a multi-brand marketplace group.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three bullets) and a FAILURE PATTERNS callout using exact names (Index-as-Database, The Country Fork, The Unwatched Model) linked to [[where-listing-systems-go-wrong]].
- [ ] States the part's argument: a shared platform earns trust through contracts, not mandates.
- [ ] A "Chapters in this part" table lists all eight chapters in config order with the question each answers and when to read it, drawn from each chapter's KEY POINTS and lead.
- [ ] Connects back to [[part-6]], [[part-2]], [[part-4]] and [[part-5]], and forward to [[part-8]].
- [ ] A Veldmark thread, labeled fictional, whose facts match the scenario ledger (17 Jan 2027 brown-out; journey SLOs Apr 2027; Tradeyard web decision May 2027 for 40 million indexed URLs; Tenancy model v1 9 Jun 2027; Experimentation standard v1 30 Jun 2027; Listing event contract v1 1 Jul 2027; data platform Sep 2027; retention schedule Oct 2027; model registry 9 Nov 2027; 146 production models).
- [ ] Ends with a hand-off to [[event-driven-listings]].
- [ ] 500–800 words of prose outside the callouts and table.

## Non-goals

Re-teaching any chapter's content; explaining Kafka, lakehouses or SLOs; external factual claims.

## Modalities

Article only for now.

## Open questions

- [[multi-country-platforms]] (chapter 39) was complete when this intro was drafted, but has no line in the ledger's "Additions by chapter"; the Tenancy model v1 facts (9 June 2027, ten tenants) come from the chapter itself. Re-check if the chapter is revised.

## Decision log

- 2026-10-19: Modeled on [[part-2]] so all part intros look alike; the eight-chapter table makes this intro the longest of the set.
- 2026-10-19: Failure patterns chosen for the platform layer; Ghost Inventory, already named in Part II, is left to the chapters.
- 2026-10-19: Veldmark decisions listed in date order; figures stay in the chapters.

## Sources

`config.yaml`, `PLAN.md` (contracts 33–40), `_research/scenario-ledger.md`, and the KEY POINTS and lead paragraphs of [[event-driven-listings]], [[listing-data-management]], [[web-and-seo-architecture]], [[data-platform]], [[experimentation]], [[ml-platform]], [[multi-country-platforms]] and [[reliability-and-scale]]. No external factual claims.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Added 1 inline illustration (article-illustrator); figures renumbered. *(AI-mediated session)*
