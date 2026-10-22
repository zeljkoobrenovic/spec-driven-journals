---
status: accepted
revised: 2026-10-22
---

# Spec: Part VIII — JOURNEYS: End-to-End Scenarios

## Intent

Orient the reader to Part VIII and explain why the book walks four flows end to end after six parts organized by context. The argument: what only the journey view shows is (1) the hops and which of them still run on an old mechanism, (2) the identifiers that cross each boundary and serve as the next hop's idempotency key, (3) the evidence at the ends of the journey, outside the hop that sent it, and (4) recovery when a hop says done and is not, which needs a journey owner. One paragraph per journey (folders 40–43), naming its case and what it owns.

Productscape bricks: the union of the part's chapters (see PLAN for [[journey-inventory-to-portal]], [[journey-data-correction]], [[journey-lead-to-dms]] and [[journey-sale-to-registration]]); the part owns none.

## Audience

Chief architects, principal engineers and product directors who own cross-team flows in vehicle data and dealer software.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three) and FAILURE PATTERNS THIS PART ADDRESSES with exact pattern names linked to where-vehicle-platforms-go-wrong.html, then `<br>`.
- [ ] States the four things only the journey view shows: hops, identifiers as idempotency keys, evidence at the ends, recovery.
- [ ] One mermaid diagram with a Figure caption.
- [ ] "Chapters in this part": one paragraph per journey in config order, linked by `[[permalink]]`, naming its Axleby case.
- [ ] Axleby facts match the ledger and the chapters (Golf Variant September 2027, 7 channels, 5 in about four hours; Odometer Correction 2,870 / 6,140 / 412 / 1,180; Lost Leads 1,460, 9 hubs; Month-End Outage 31 March 2027, 214 double submissions).
- [ ] Ends with a hand-off to [[journey-inventory-to-portal]]; 500–800 words of body.

## Non-goals

Re-telling the journeys' mechanics (the chapters own them); teaching the contexts of Parts II–VII; external factual claims.

## Modalities

Article only for now.

## Open questions

None.

## Decision log

- 2026-10-22: Mirrors the Part VI introduction: callouts, a short lead, one diagram, a paragraph per chapter.
- 2026-10-22: Failure patterns: The Zombie Listing (journeys 40 and 43), The Sticky Error (41) and The Leaky Lead (42). Borrowed Uptime and The Cloned Identity are left to the chapters' own callouts.
- 2026-10-22: The diagram is generic (event → hops → evidence → owner → recovery) rather than one per journey, because the chapters each carry their own sequence diagram.

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, `_research/consistency-issues.md` (items 24–28), and the callouts, scenes and failure cases of [[journey-inventory-to-portal]], [[journey-data-correction]], [[journey-lead-to-dms]] and [[journey-sale-to-registration]]. No external factual claims.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: acronyms expanded on first use; facts checked against the four journeys and the ledger. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 1 mermaid diagram to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
