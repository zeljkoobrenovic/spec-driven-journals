---
status: accepted
revised: 2026-10-22
---

# Spec: From Trade-In to Live Advert: Ingesting and Publishing Dealer Inventory

## Intent

Walk one car, Autobedrijf Brandsma's 2021 Volkswagen Golf Variant (September 2027), from the trade-in handover to live adverts on seven channels, and show what only the journey view reveals: the identifier chain that each hop must key on, the different definitions of "done" per hop, the gap between "published" and channel evidence, the hops that still ran on 2027 mechanisms beside redesigned ones, and the safety nets that made the partly modernized journey safe. Then break the journey six times (DMS duplicate stock numbers, two candidate editions, an equipment-code rejection, a partial photo upload, a price change racing a reservation, a portal outage) with detection and recovery for each. The Zombie Golf (February 2027) is the contrast thread.

Productscape bricks covered (by journey, no new ownership): `tapp`, `occm`, `dosr`, `advf`.

Owns: no new terms. Uses appraisal, stock item, advert revision, channel listing, publish lag and DMS adapter as defined by their owning chapters.

## Audience

Chief and principal architects of dealer-software vendors, integration and platform leads, and product directors who own a dealer journey rather than a component.

## Success criteria

- [ ] A sequence diagram, a hop table (owner, input identifier, minted identifier, done-condition) and a timeline of the Golf Variant agree with the ledger and with the chapters that follow the same car.
- [ ] A requirements table per hop (consistency, latency, freshness, availability) with the Golf Variant's actual values; assumptions labeled.
- [ ] The identifier chain is explicit, and the reader can say which identifier is each hop's idempotency key.
- [ ] Six failure cases, covering duplicates, incomplete records, permanent errors, partial failure, conflicting updates and an external outage, each with detection and recovery, plus a summary table.
- [ ] A trade-off table with a reasoned recommendation (choreography plus journey monitor, not an orchestrator) and the condition under which it changes.
- [ ] A journey metrics table measured from business events to channel evidence, split by cause.
- [ ] A short "What Changes in Another Market" section with a table.
- [ ] No re-teaching of the owning chapters; company claims are dated and sourced.

## Non-goals

- Syndication engine design, desired state, withdrawal saga ([[listing-syndication]]).
- Advert content, media pipeline, disclosures ([[merchandising]]).
- Appraisal, MPP and offers ([[vehicle-acquisition]]); edition resolution ([[specification-and-equipment]]).
- Stock lifecycle and dossier ([[inventory-and-vehicle-dossier]]); Hitch design ([[dms-integration]]); event backbone ([[events-webhooks-and-sync]]).
- Leads after the first enquiry ([[journey-lead-to-dms]]); sale, withdrawal and registration ([[journey-sale-to-registration]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Whether Meta's automotive catalog is available to Dutch dealers in 2027 was not verified, so the seventh channel is an unnamed dealer-association portal instead.
- How portals behave on an update for a listing they no longer hold is not documented; the two "update-as-create" channels are an Axleby illustration.

## Decision log

- **2026-10-22** — Used the Golf Variant already threaded through specification, acquisition and merchandising instead of a new car, so the journey adds seams rather than repeating hops; the seven channels reconcile merchandising's "five channels" (five at stock-in, two catalogs gated on Ready).
- **2026-10-22** — Set the walk in September 2027 on the patched old Relay, not on Relay 2, so the chapter can show hops at different maturity and the safety nets as load-bearing.
- **2026-10-22** — Ran three failures on the Golf Variant and three at other cars (Velto's DMS re-booking, Brandsma's Insignia and Yaris, an unnamed portal) so the car's sale stays with journey-sale-to-registration.
- **2026-10-22** — Recommended choreography plus a journey monitor over an orchestrator.

## Sources

- Internal: [[listing-syndication]], [[merchandising]], [[vehicle-acquisition]], [[specification-and-equipment]], [[inventory-and-vehicle-dossier]], [[used-car-pricing]], [[dms-integration]], [[events-webhooks-and-sync]], [[observability-and-data-operations]].
- External: AutoScout24 Listing Creation API docs and changelog; AutoScout24 Tech Blog (2024) on SLOs for Critical User Interactions; Marktplaats API docs; Google Merchant Center vehicle ads help; Autotrader Connect docs; RDW trade-stock stock-in page; Emerce (2025).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: dealer pronoun in WHY THE BUSINESS CARES made neutral; facts checked against the ledger and items 24–28. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: offer v2 validity aligned with vehicle-acquisition (seven days or 500 km); American spelling. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
