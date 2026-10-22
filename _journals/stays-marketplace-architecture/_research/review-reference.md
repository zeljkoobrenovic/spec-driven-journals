# Review log — Reference pages (domain-coverage, toolkit, glossary)

Editorial review pass, 21 Oct 2026. Reference pages need no Hotels-and-Homes section, Chief Architect's view or Corvane scene; glossary/toolkit tables not trimmed.

## domain-coverage — 6,360 words (unchanged length; no trim needed)
- Spot-checked all 55 brick rows against every chapter spec's "Productscape domains" line: primary chapters match; added `event-driven-stays` (payment state feed) to TAM `paym` "also".
- Ch. 42 rows (TAM `home`, `deal`, HSM `insp`, distribution [ADDED], corporate travel as a channel) match the chapter's actual content (landing assembly, merchandising slots, metasearch, B2B API, travel agents and corporate travel).
- Ch. 47: stressor rows fixed to match content. `insv` was attributed to inventory-integrity, which never discusses distributor insolvency; now stays-capability-map (primary, map test) + evolving-the-platform (stressor workshop, Algarve combined stressor) + connectivity-and-channel-managers + payouts-and-settlement. Combined-stressor row: removed stays-capability-map (no combined case there). fire/evac row: destinations-and-maps (no destination-operating-state content) replaced with changes-and-cancellations (declared events); "destination operating state" paragraph now points to protection-and-incidents and evolving-the-platform.
- Gap row "Reservation system of record" reworded to what ch. 13 actually covers.
- [ADDED] list (7) matches PLAN.md and stays-capability-map. Counts 12/15/7/3 and 7+17+3=27 gaps verified.
- timetoread 24 → 28 min.

## toolkit — 11,199 words (reference page, not trimmed)
- All 14 Corvane examples cross-checked number by number against owning chapters and the ledger (Tools 1–14: map v1 16/6/26 over 48 on 23 Mar 2027, v2 23/6/20 over 49 on 14 Dec 2027; Novak legs €1,041.60/€141.13/€32.47/€56 = €1,271.20; 12%+4% fees; Carmen strike refund table; Miradouro VCC 85%; Pricegrid, Switchyard, Stayline, Clause, Levy, Warden, Ordinance, SLO, One Stay budget €34M figures). Gauge/Plumbline usage correct.
- Lisbon tax card: €4 now "per guest per night, as of 2026" sourced to the help-center page; under-13 exemption explicitly a Corvane assumption, not a verified rule; Novak row notes the children are exempt under the assumed rule.
- Switchyard example: removed "7-day first-price check" (not in connectivity-and-channel-managers); replaced with the chapter's new-product-stays-closed behavior.
- "programme" → "program", "cancelled" → "canceled".

## glossary — generated, 557 rows, 25,900 words
- assemble.py paths verified: reads its own directory (`_research/glossary-tools`) and writes `posts/glossary/index.md` (no /private/tmp paths).
- Visibility Plus → **Front Row** in corvane.md (editor note).
- Automated check of every row: all `[[links]]` valid; rows whose term is not found in the linked chapter reviewed by hand. Fixed: Occupancy-based pricing → rates-and-availability-model (owner) + availability-engine; Physical/sellable/available inventory → property-and-listing-model (owner) + inventory-integrity.
- Duplicates dropped via drop.txt: part-1 "Agency model / merchant model" and part-5 "Merchant model / agency model" (owned by merchant-and-agency-models, row in part-6 kept).
- ~110 rows spot-read against chapters (every 5th row of every part + 25 targeted greps); regulation dates (DSA 17 Feb 2024, DAC7 2023/31 Jan, VLOP 45M, DSA Art. 31, RFC 5545 Sept 2009, HTNG 2002) correct.
- 47 Corvane rows checked against ledger and owning chapters (dates for Waypoint, Ranking Policy v1, Pay Later, Fathom, Plumbline, Corvane ID, Vouch, backbone, Kiln, Gangway, forum/board, Frontdoor, Courier/Threadline, Harbor, Concord, Smart Rate, Turnstile, Trip Intent Service, Calendar Sync v2, place registry, Experimentation Standard): all consistent.
- American spelling fixed in row files (canceled). spec.md note on `introduction` updated (page now exists).

## Build and render check
Build clean. render_check: all three pages have 0 failed mermaid; the only unresolved entry is `XJ:../finance-systems-architecture/bibliography.html` ([[bibliography]] resolves cross-journal until BOOKED's bibliography page exists — allowed).

## Open issues for others
- `[[bibliography]]` resolves to RECONCILED's bibliography until BOOKED's page is written (toolkit, glossary, domain-coverage all link it).
- inventory-integrity does not discuss the `insv` (distributor insolvency) stressor; if the author wants it there, the chapter needs a paragraph (coverage now points to ch. 03 and 47).
