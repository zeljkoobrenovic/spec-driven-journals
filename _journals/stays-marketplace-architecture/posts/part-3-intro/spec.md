---
status: accepted
revised: 2026-10-22
---

# Spec: Part III — INVENTORY: Availability, Rates and Price

## Intent

Orient the reader to Part III: why inventory is a read problem and a write problem with different answers (read models with a staleness budget, an exact commit point), why every price must be computed by one kernel and written through one resolver, where hotels and homes differ in this part, and what each of the five chapters decides. Frame it through the Corvane systems and cases the chapters use (Tally, Pricegrid, Almanac, Smart Rate, Perks, Roomstead Circle).

Productscape domains: the union of the part's chapters (TAM invt, room, cald, rate, deal, prom; HSM cala, pric).

## Audience

Chief architects, inventory, pricing and search leads, and engineering directors responsible for availability and price accuracy.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three) and a FAILURE PATTERNS callout using exact names linked to where-stay-platforms-go-wrong.html.
- [ ] States the argument (reads served from stale-but-measured read models, writes committed exactly) and names where hotels and homes differ: a derived grid pushed by an RMS vs one nightly calendar the platform owns; a claimed count vs a uniqueness constraint.
- [ ] Two illustrations, each with a Figure caption: many reads against one commit, and two stores feeding one kernel.
- [ ] A "Chapters in this part" list with one paragraph per chapter in config order, each linking the chapter and saying what it decides.
- [ ] Corvane facts match the ledger and chapters: about 1,400 lookups per reservation, 91% vs 97% accuracy, Miradouro's 37 rate plans and 168 products, the Seville and King's Day cases, Santo António 2027, Autumn Cities.
- [ ] Ends with a hand-off to [[rates-and-availability-model]]; 500–900 words of body.

## Non-goals

Teaching ARI semantics, caching designs, concurrency control or pricing models (the chapters own them); external factual claims.

## Modalities

Article only for now.

## Open questions

None.

## Decision log

- 2026-10-21: Modeled on LISTED's part introductions, with a mermaid diagram and a paragraph-per-chapter list, per the BOOKED brief.
- 2026-10-21: Failure patterns: Phantom Availability, Price Drift and Rate Plan Sprawl; The Double-Booked Night and The Unwatched Model are left to their chapters ([[inventory-integrity]], [[dynamic-pricing]]).
- 2026-10-21: The diagram shows One Stay's "shared contracts, separate engines" rule as it applies to inventory: two stores, one kernel.

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, and the callouts, leads, Setting the Scene sections and Chief Architect's views of [[rates-and-availability-model]], [[availability-engine]], [[inventory-integrity]], [[dynamic-pricing]] and [[promotions-and-loyalty]]. No external factual claims.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: aligned the search-volume sentence with the ledger (1,400 shopping requests per gross reservation, ~10 Pricegrid reads each). *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 1 mermaid diagrams to illustrations and added 1 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 853 → 874 prose words; lead now names what Parts IV and V take from this part; hotel-count sentence made concrete; chapter cases stated in one parallel form; spec's diagram criterion updated from one mermaid diagram to the two illustrations the page now has. *(AI-mediated session)*
- **2026-10-22** — Corrected the price-mismatch claim to match the chapter's audit (staleness 5.7 points, arithmetic 2.8): arithmetic is a large share, not most. *(AI-mediated session)*
