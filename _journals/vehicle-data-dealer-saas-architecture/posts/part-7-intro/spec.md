---
status: accepted
revised: 2026-10-22
---

# Spec: Part VII — OPERATIONS: Running the Platform

## Intent

Orient the reader to Part VII: why a vehicle data and dealer SaaS platform is operated at its edges — registers, paid suppliers, portals and DMS products — and how reliability, cost, observability, security and privacy each move their controls to the journey, the call path, the confirmed outcome, the caller and the copy. Frame the part through the Axleby cases the chapters actually use: the Month-End Register Outage, Rijnstaal's Saturday batch, green dashboards during the Zombie Golf, the Plate Enumeration Attack and one consumer's erasure request across nine systems.

Productscape bricks: the union of the part's chapters (see PLAN for [[reliability-and-dependencies]], [[scale-and-cost]], [[observability-and-data-operations]], [[vehicle-platform-security]] and [[privacy-and-retention]]).

## Audience

Chief architects, heads of platform and SRE, CISOs and data protection leads, and engineering directors who run the platform day to day.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three) and a FAILURE PATTERNS THIS PART ADDRESSES callout using exact pattern names linked to where-vehicle-platforms-go-wrong.html.
- [ ] States the argument (the platform is operated at its edges) and names the five control points.
- [ ] One mermaid diagram with a Figure caption.
- [ ] A "Chapters in this part" list with one paragraph per chapter in config order, each linking the chapter by `[[permalink]]` and saying what it decides and which case drives it.
- [ ] Axleby facts match the ledger and the chapters (31 March 2027, 5 h 40 min, 214 double submissions; €96,525 revenue vs €96,140 build-data fees; €0.031 average lookup, €0.46 per build-data fetch; 58% of severity 1–2 incidents customer-reported; 61 channels; 2,250 DMS-connected rooftops; about 9 million requests in six days).
- [ ] Ends with a hand-off to [[reliability-and-dependencies]]; 500–800 words of body.

## Non-goals

Teaching SLOs, FinOps, monitoring, threat modeling or GDPR (the chapters own them); tenant isolation ([[tenancy-and-dealer-groups]]) and license enforcement ([[data-licensing-and-governance]]); external factual claims.

## Modalities

Article only for now.

## Open questions

None.

## Decision log

- 2026-10-22: Mirrors BOOKED's and this book's Part II introduction: opening callouts, a short lead, one mermaid diagram and a paragraph-per-chapter list.
- 2026-10-22: Failure patterns: Borrowed Uptime, License Blindness and The Sticky Error, the three that recur most across the part's chapter callouts; Feed Roulette, DMS Hostage, The Tenant Blur and The Unmetered Call are left to the chapters.
- 2026-10-22: The diagram places the controls at the external edges and reports back to the dealer's journey, the shape [[reliability-and-dependencies]] and [[observability-and-data-operations]] recommend.

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, and the callouts, leads and Setting the Scene sections of [[reliability-and-dependencies]], [[scale-and-cost]], [[observability-and-data-operations]], [[vehicle-platform-security]] and [[privacy-and-retention]]. No external factual claims.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Saturday Batch cost in WHY THE BUSINESS CARES now states the full €105,490 cost, not only the build-data fees. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 1 mermaid diagram to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
