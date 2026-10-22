---
status: accepted
revised: 2026-10-22
---

# Spec: Part I — MARKET: The Business of Vehicle Data and Dealer Software

## Intent

Orient the reader to Part I: the market draws the architecture's first lines. Before a vehicle data and dealer SaaS platform draws service boundaries, it must know who owns which fact and on what terms, what each call, car and rooftop earns and costs, what the business must be able to do, and which context may say a fact is true. Frame the part through the Axleby scenes its chapters actually use (the License Breach and the ecosystem map, the One Dossier business case, capability map v1, the five meanings of "sold" and the entity–owner table).

Productscape bricks: the union of the part's chapters (the reference model as a whole in the capability map; context and ownership framing across bricks).

## Audience

Chief architects, principal engineers and engineering leaders of vehicle-data companies, dealer-software vendors and groups that sell both.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, exactly three KEY POINTS and a FAILURE PATTERNS callout with exact names linked to where-vehicle-platforms-go-wrong.html.
- [ ] States the part's argument (the market sets sources of truth, requirements, shared capabilities and context lines) and the thread through the four chapters.
- [ ] Axleby numbers match the chapters and ledger (€38 million One Dossier, €1,110 per rooftop per month, 9 of 39 capabilities duplicated, 29 / 11 / 4 entity census, €0.46 fetch, 58 vs 51 days, 16 March and 3 June 2027).
- [ ] One mermaid diagram with a Figure caption.
- [ ] A "Chapters in this part" list with one paragraph per chapter in config order, each linking the chapter, saying what it decides and naming its Axleby case.
- [ ] Hands off to [[vehicle-data-ecosystem]]; [[meet-axleby]] hands off here.
- [ ] Body after the callouts about 500–800 words.

## Non-goals

Teaching the ecosystem, unit economics, capability mapping or bounded contexts (the chapters own them); the Across Markets comparison; external factual claims.

## Modalities

Article only for now.

## Open questions

- None.

## Decision log

- 2026-10-22: Modeled on this book's Part II introduction: callouts, a three-paragraph lead, one diagram, a paragraph per chapter.
- 2026-10-22: Failure patterns: The Acquisition Archipelago, The Unmetered Call and License Blindness, the three that recur across the part's chapters; Borrowed Uptime, The Sticky Error and The Cloned Identity are left to the chapters.
- 2026-10-22: The diagram shows the part as a chain of business questions that become architectural inputs, ending in Parts II–IX.

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, and the callouts, Setting the Scene sections and closing paragraphs of [[vehicle-data-ecosystem]], [[dealer-and-data-economics]], [[vehicle-capability-map]] and [[vehicle-bounded-contexts]]. No external factual claims.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 1 mermaid diagram to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
