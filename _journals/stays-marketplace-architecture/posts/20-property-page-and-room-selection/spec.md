---
status: accepted
revised: 2026-10-22
---

# Spec: The Moment of Decision: Property Pages, Room Selection and Total Price

## Intent

Explain how the page where a guest decides (the hotel property page and the home listing page) should be assembled, and what it must get right: one price, shown the same way from search to checkout; a rooms table a guest can read; and, for homes, trust evidence that comes from systems the page team does not own. The chapter's argument is that price **composition** (one quote with an itemized breakdown, per engine, under a shared offer contract) must be separated from price **display** (a versioned, per-market display policy reviewed by legal), and that both must be separated from the page's descriptive fragments. After reading, an architect can name who owns the price a guest sees, measure drift between surfaces, and design a rooms table and a listing trust block without forcing one marketplace's shape on the other.

Owns: **total price display**, **rate comparison**, **property detail assembly**.

Productscape domains covered: TAM `prop` (Property Detail & Reviews), TAM `room` (Room & Rate Selection); HSM `list` (Listing Detail & Review Trust).

## Audience

Chief and principal architects, front-end and search platform leads, pricing and payments engineers, and product directors of OTAs and hosted-stays marketplaces who own or depend on the property page, plus the regulatory and legal partners who must approve how prices are displayed.

## Success criteria

- [ ] Reader can list the line types of a stay total (accommodation, discounts, supplier fees, platform fees, taxes in the rate, per-stay taxes, deposits, extras) and say which are mandatory, who is paid and when.
- [ ] Reader can describe a quote contract (ID, validity, inputs version, itemized lines, conditions, totals, confidence) and why checkout re-validates rather than recomputes.
- [ ] Reader can state the EU, UK and US total-price rules as of 2026 with dates and sources, and what each changes in code.
- [ ] Reader can walk the offer pipeline (eligibility, occupancy fit, normalization, pruning of dominated offers, grouping) and explain how it limits Rate Plan Sprawl on the page.
- [ ] Reader can name the trust evidence a listing page needs, its source systems and the legal duties behind reviews, trader status and STR registration numbers.
- [ ] The Corvane worked example uses the ledger's Novak numbers exactly (€1,015; €70; €130.20; €56; €1,271.20; 25%) and shows the before and after surfaces.
- [ ] The chapter includes a trade-off table, a "Hotels and Homes" table with a judgement on what to share, at least two diagrams, failure modes, a Chief Architect's view and design-review questions.
- [ ] Reader will not mistake labeled inferences or Corvane illustrations for documented facts about real companies.

## Non-goals

- Computing offers and caching prices at search scale, and price-accuracy metrics for metasearch: [[availability-engine]].
- The ARI data model and rate-plan structure itself: [[rates-and-availability-model]].
- Search and ranking of results lists: [[stays-search-architecture]], [[stays-ranking]].
- Holds, payment authorization and the booking saga after the guest clicks "reserve": [[checkout-orchestration]].
- Cancellation policy engine and its versioning: [[changes-and-cancellations]].
- Review collection, moderation and scoring: [[reviews-and-reputation]]; tax calculation rules: [[taxes-on-stays]]; STR registration workflows: [[stays-regulation]]; media processing: [[content-and-media]]; approximate-location geometry: [[destinations-and-maps]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Lisbon's tourist-tax exemption for children under 13 is taken from the scenario ledger; the €4.00 per person per night and seven-night cap are verified only from Airbnb's undated help page. Confirm with the City of Lisbon's official regulation.
- The CMA's final price-transparency guidance (CMA209) was not checked; the chapter cites the 2025 draft.
- Whether Price Indication Directive Article 6a (30-day prior price) applies to accommodation remains unconfirmed.
- Airbnb's 2022–2023 statements on total-price ranking and 300,000 listings lowering cleaning fees were seen only in search excerpts.

## Decision log

- **2026-10-21** — Framed the chapter around separating price composition from price display, rather than around page UX, because the drift problem is architectural (several code paths) and display rules change with law, not with rates.
- **2026-10-21** — Used the ledger's Novak booking as the main thread and added an illustrative Hotel Miradouro rooms-table funnel (37 rate plans to 5 default offers) so both marketplace types are worked with numbers; rejected a separate Roomstead incident to avoid inventing new canonical events.
- **2026-10-21** — Recommended sharing the offer contract, display policy, tax lines, reviews read model and page shell, but not the page's middle (rooms table vs trust block); layout chosen by offer shape, not brand.
- **2026-10-21** — Kept performance short and tied it to the descriptive/transactional split; detailed latency engineering belongs to [[global-scale-and-reliability]].

## Sources

- **Internal**
  - [[availability-engine]], [[rates-and-availability-model]], [[checkout-orchestration]], [[stays-ranking]], [[converging-two-marketplaces]] — neighboring contracts and terminology.
  - `_research/brief-availability-pricing.md` (Parts 7 and 12), `brief-trust-safety-regulation.md` (Parts 5, 8, 9), `brief-expedia-agoda-tripcom.md` (Part 3), `brief-booking-com.md` (Part 2), `brief-platform-data-ml.md` (Part 10), `brief-host-partner-guest-service.md` (Part 6), `productscape-digest.md` (`prop`, `room`, `list`), `scenario-ledger.md` (worked example 10).
- **External**
  - Booking.com Engineering, "Node.js at scale, rebalanced" (2026) — page and fragment ownership.
  - Airbnb, server-driven UI (2021) and total price display (2025) — listing page and price display.
  - Expedia Group Rapid documentation (n.d.) — price breakdown, price check, Vrbo single-unit model.
  - UCPD (2005), Commission UCPD guidance (2021), Omnibus Directive (2019), STR Regulation (2024), EAA (2019), FTC fees rule (2025), UK DMCC Act and CMA (2025) — display and evidence duties.
  - Airbnb Help Center article 2290 (n.d.) — Lisbon tourist tax.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed 9,501 to 8,474 words; hand-off now to part-5; Miradouro catalog aligned to 168 products; Lisbon child exemption hedged as unverified; Levy named; removed uncited sources. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 6,527 → 6,211 prose words; no headings renamed; merged the duplicate "silent fallback" failure mode into the Performance section; deleted the "rate dump" failure mode (restated the offer pipeline) and announcing sentences; trimmed Chief Architect's view items that restated the display-policy and Hotels and Homes sections; opening now names Part V as the next step. *(AI-mediated session)*
- **2026-10-22** — Verified Lisbon tourist tax / Portuguese VAT against official sources. *(AI-mediated session)*
