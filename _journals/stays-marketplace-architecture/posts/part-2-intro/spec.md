---
status: accepted
revised: 2026-10-21
---

# Spec: Part II — SUPPLY: Properties, Homes and the Partners Behind Them

## Intent

Orient the reader to Part II: why supply should be treated as master data with many writers, where hotels and homes differ on the supply side, and what each of the six chapters decides. Frame the part through the Corvane platforms and cases the chapters actually use (place registry, readiness service, Concord, Switchyard, Corvane Connect, Almanac, Partner Hub and the host app).

Productscape domains: the union of the part's chapters (TAM invt, cont, medi, onbo, conn, cald, extr, rsrv, perf; HSM lista, hono, apix, cala, opco, coho, host).

## Audience

Chief architects, supply and connectivity leads, and engineering directors responsible for partner and host platforms.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three) and a FAILURE PATTERNS callout using exact names linked to where-stay-platforms-go-wrong.html.
- [ ] States the argument (supply is master data with many writers) and names concretely where hotels and homes differ: pool vs one unit, pushed PMS truth vs an iCal mesh, business contract vs a person with a registration number.
- [ ] One mermaid diagram with a Figure caption.
- [ ] A "Chapters in this part" list with one paragraph per chapter in config order, each linking the chapter and saying what it decides, drawn from the chapters' KEY POINTS, leads and Chief Architect's views.
- [ ] Corvane facts match the ledger and the chapters (€12 rate, Seville double booking, Costa Keys' 38 apartments, Brightwell's 41,000 properties, 187,000 shared-login listings).
- [ ] Ends with a hand-off to [[property-and-listing-model]]; 500–900 words of body.

## Non-goals

Teaching the supply model, connectivity protocols or iCal mechanics (the chapters own them); external factual claims.

## Modalities

Article only for now.

## Open questions

None.

## Decision log

- 2026-10-21: Modeled on LISTED's part introductions, with a mermaid diagram and a paragraph-per-chapter list instead of a chapter table, per the BOOKED brief.
- 2026-10-21: Failure patterns: The Hotel-Shaped Home, Connectivity Roulette and The Double-Booked Night, the three that recur across most of the part's chapters; The Same Hotel Twice is left to [[content-and-media]].
- 2026-10-21: The diagram shows writers converging on per-brand catalogs and one place registry, the shape [[property-and-listing-model]] recommends.

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, and the callouts, leads, Setting the Scene sections and Chief Architect's views of [[property-and-listing-model]], [[partner-onboarding]], [[content-and-media]], [[connectivity-and-channel-managers]], [[calendar-sync]] and [[extranets-and-host-tools]]. No external factual claims.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: tightened key points and lead, corrected Brightwell "hotels" to properties, noted that Waypoint enriches the place registry (map v2). *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 1 mermaid diagram to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
