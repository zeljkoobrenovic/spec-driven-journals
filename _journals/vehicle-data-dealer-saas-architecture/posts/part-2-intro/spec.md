---
status: accepted
revised: 2026-10-22
---

# Spec: Part II — VEHICLE: Identity, Specification and History

## Intent

Orient the reader to Part II: why a vehicle record is a set of sourced, dated observations attached to one internal vehicle key, and why specifications, judgements and golden records must be computed views. Frame the part through the Axleby systems and incidents its chapters actually use (Anchor, Turnstile, Specbook, Tracewell, Inlet; the Cloned Plate, the Three Copies review, the €46-per-hundred problem, the false Volvo V60 rollback flag, the Odometer Correction).

Productscape bricks: the union of the part's chapters (vidn, rdwc, vhis, mktd ingest and matcher, dgov lineage).

## Audience

Chief architects, data-platform leads and engineering directors responsible for vehicle identity, register access, specification and history data.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, exactly three KEY POINTS and a FAILURE PATTERNS callout with exact names linked to where-vehicle-platforms-go-wrong.html.
- [ ] States the part's argument (observations with authority and provenance; computed views) and the thread through the six chapters.
- [ ] Axleby numbers match the ledger and chapters (Cloned Plate, €9,800 trade-in on a 19-day-old cache entry, Odometer Correction's 6,140 / 412 / 1,180).
- [ ] One mermaid diagram with a Figure caption.
- [ ] A "Chapters in this part" list with one short paragraph per chapter in config order, each linking the chapter, saying what it decides and naming its Axleby case.
- [ ] Hands off to [[vehicle-identity]]; the previous part's last chapter hands off here.
- [ ] Body after the callouts stays short (about 500–800 words; the whole page about 900–1,050, in line with BOOKED and LISTED part introductions).

## Non-goals

Teaching VIN structure, register access regimes, specification resolution, history assembly, ingestion or provenance (the chapters own them); the Across Markets comparison (each chapter has its own); external factual claims.

## Modalities

Article only for now.

## Open questions

- `vehicle-bounded-contexts`, the last chapter of Part I, was not yet written on 2026-10-22; its closing paragraph should hand off to [[part-2]].

## Decision log

- 2026-10-22: Modeled on BOOKED's part-2 introduction: callouts, a three-paragraph lead, one diagram, a paragraph per chapter.
- 2026-10-22: Failure patterns: The Cloned Identity, Provenance Amnesia and The Sticky Error, the three that recur across most of the part's chapters; License Blindness and Spec Guesswork are left to the chapters.
- 2026-10-22: The diagram shows the shape the part recommends: one ingestion path, one vehicle key, facts with envelopes, views computed by versioned rules.

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, and the callouts, Setting the Scene sections and closing paragraphs of [[vehicle-identity]], [[registers-and-official-data]], [[specification-and-equipment]], [[vehicle-history]], [[ingestion-and-entity-resolution]] and [[provenance-and-data-quality]]. No external factual claims.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 1 mermaid diagram to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
