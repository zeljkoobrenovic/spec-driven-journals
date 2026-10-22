---
status: accepted
revised: 2026-10-22
---

# Spec: Two Marketplaces for a Night's Stay: OTAs, Hosted Stays and How They Grew

## Intent

Give the reader the vocabulary and the history that the rest of BOOKED depends on, and prove the book's founding claim: **the type of accommodation marketplace decides the architecture**. The chapter defines six ways to sell a night (accommodation marketplace/OTA, hosted-stays marketplace, vacation-rental marketplace, metasearch, bedbank, direct booking) by four questions: who holds the supply relationship, the guest, the money, and the truth about availability and price. It argues that the last question decides the architecture (a cache with a contract versus a system of record with a duty of care), and that the professional-versus-individual operator axis matters more than "hotel or home". It tells the industry's history as six dated waves (reservation systems and GDS; US online agencies and the merchant model; the European agency model; vacation rentals and Airbnb; metasearch and consolidation; pandemic and convergence) and names what each left in today's systems. It closes with a reference layering for a group that runs both types: share the guest-facing commitment layer, keep one supply engine and connectivity edge per type. The chapter owns accommodation marketplace, hosted-stays marketplace, OTA, metasearch, bedbank and direct booking.

Productscape domains covered: framing for all domains of both models (TAM and HSM); in particular the TAM-versus-HSM structural differences (digest §4.2) and the supply-segment personas (TAM `cg3-p1`, `cg4-p1`; HSM `cg2-p1`, `cg3-p1`).

## Audience

Chief architects, principal engineers and engineering leaders of OTAs, hosted-stays and vacation-rental marketplaces, channel managers and PMS vendors, and anyone new to travel who must reason about a stays platform. They know distributed systems; they need the industry's types, money roles and history, and a way to tell which machinery each supply segment needs.

## Success criteria

- [ ] Reader can define the six types and place each one in the four-question table (supply, guest, money, truth).
- [ ] Reader can explain why the location of the truth about availability decides the architecture, and give the component consequences for each type.
- [ ] Reader can classify supply by operator (chain, independent hotel, small lodging, professional manager, individual host) and explain why connectivity, trust and regulation follow the operator.
- [ ] Reader can distinguish agency, merchant and facilitated payments, with dated public examples (Booking Holdings, Expedia, Airbnb, Trip.com).
- [ ] Reader can name the six waves with dates and say what each left in today's systems (table and Figure 1).
- [ ] Reader can use the Corvane one-night comparison (Miradouro on Roomstead, Carmen's apartment on Nookaway) to show that the two types fail, pay for failure and earn differently, with ledger-consistent numbers.
- [ ] Reader can state the placement rule (supply-count correctness → supply engine; guest, promise, money → shared layer) and sketch the layering (Figure 3).
- [ ] Every company claim carries a dated source; founding and acquisition dates are marked as widely reported secondary facts.

## Non-goals

- Unit economics, take rates, look-to-book and liquidity in depth: [[stays-marketplace-economics]].
- The capability maps and overlap matrix: [[stays-capability-map]]; service boundaries and the offer and reservation aggregates: [[stays-bounded-contexts]].
- The supply data model (property, room type, unit, listing): [[property-and-listing-model]].
- Merchant, agency and facilitated payments in depth: [[merchant-and-agency-models]].
- Whether and how to converge the two platforms: [[converging-two-marketplaces]].
- Company case studies: Part X ([[case-booking-com]], [[case-airbnb]], [[case-expedia-vrbo]], [[case-agoda-trip-com]]).
- The "Hotels and Homes" section heading: Part I chapters compare the two types throughout instead.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Founding dates and acquisition prices (Sabre, Hotels.com, Expedia, Booking.com, Priceline/Booking Holdings, Agoda, KAYAK, trivago, VRBO, HomeAway, Airbnb) come from Wikipedia, accessed 21 October 2026, because the web-search quota was exhausted. Replace with primary sources (filings, press releases) before print. Two sources disagree on details: Booking.com's acquisition price ($133 million vs $135 million) and the KAYAK deal year (announced 2012, closed 2013).
- No primary source documents why the US online agencies adopted the merchant model or why the European agency model won with independent hotels; both are presented as interpretation.
- Hotel-industry switch history (THISCO, 1989) rests on a roughly 2004 secondary source.
- The look-to-book figure (about 20,000:1) is a 2016 opinion piece; presented as an order of magnitude.

## Decision log

- **2026-10-21** — Organized the type definitions around four questions (supply, guest, money, truth) rather than around company examples, so that the last question can carry the architectural argument and the case studies stay in Part X.
- **2026-10-21** — Added the professional-versus-individual operator axis as a first-class section, because it explains why Roomstead's 435,000 homes do not make it a hosted-stays marketplace; this is the hinge of the Corvane scene.
- **2026-10-21** — Told history as six overlapping waves with a "what it left behind" paragraph each, rather than a chronology, so that every wave links to the chapter that owns its legacy.
- **2026-10-21** — Used two ledger cast members on one May weekend (Miradouro, Carmen) for the worked example, reusing the €12 rate and Seville incidents; derived a new example stay (13–16 May 2027, €436.80) consistent with the ledger fees.

## Sources

- **Internal**
  - `_research/brief-booking-com.md` Parts 1, 3.6, 4 — counts, merchant/agency mix, request-to-book, payout rails.
  - `_research/brief-airbnb.md` Parts 1 and 4 — custody, fees, hotels, co-hosting, iCal.
  - `_research/brief-expedia-agoda-tripcom.md` Parts 1, 3.6, 6.1, 7, 9 — Expedia consolidation, Vrbo in Rapid, Agoda, Trip.com agency.
  - `_research/brief-supply-connectivity.md` Parts 4–6, 8 — channel managers, switches, iCal, bedbanks, GDS, look-to-book.
  - `_research/productscape-digest.md` §4.2, §9, §10.3 — structural differences between the two models.
  - [[meet-corvane]], [[property-and-listing-model]], [[calendar-sync]], [[merchant-and-agency-models]], [[converging-two-marketplaces]].
- **External**
  - Booking Holdings 10-K FY2025 (2026); Expedia Group 10-K FY2022, FY2023, FY2025 and Q1 2024 results; Airbnb 10-K FY2025 (2026), Q2 2026 letter, 5 May 2020 CEO message; Trip.com 20-F FY2025 (2026).
  - Booking.com and Expedia Rapid developer documentation (live October 2026); Booking.com "How we work" (2025).
  - RFC 5545 (2009); Regulation (EU) 2024/1028.
  - SiteMinder FY26 (2026); Hotelbeds docs; Amadeus sales sheet; PhocusWire (2025); Hospitality Net (2016); Encyclopedia.com (c. 2004); Wikipedia company histories (accessed 2026-10-21).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed from 9,203 to 8,498 words (history waves, layer list, duplicated failure mode and questions); American spelling; history and Expedia front-end dates checked against filings. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 7,229 → 7,219 prose words; opening now names the next chapter; property-count paragraph leads with its point; one Chief Architect decision renamed to match its content; repeated 36% figure and a redundant fictional-Corvane sentence cut; spec unchanged. *(AI-mediated session)*
- **2026-10-22** — Second sharpening pass: 7,229 → 6,891 prose words cumulative from HEAD (−4.7%); Failure Modes compressed to one-line bullets that point to their sections; repeated Rafael/435,000 paragraph, section-closing recaps, figure lead-in and transitions cut; Chief Architect decision 3 now points to the layering instead of repeating it; spec unchanged. *(AI-mediated session)*
