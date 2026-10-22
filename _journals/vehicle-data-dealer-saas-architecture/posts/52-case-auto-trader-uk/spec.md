---
status: accepted
revised: 2026-10-22
---

# Spec: Auto Trader UK: From Classifieds Portal to Data and Software Platform for Retailers

## Intent

Read Auto Trader's public record (FY2023–FY2026 results, the Autotrader Connect developer documentation and changelog, 2026 engineering posts, 2019 infrastructure case studies and trade press on the November 2025 Deal Builder protest) as the case of a marketplace that became the data and software supplier of UK car retailers. The reader should leave with three things: the retailer products form a dependency ladder keyed on the taxonomy; the partner API carries the business model (capabilities per advertiser, stock lifecycle, change policy); and a bundled workflow feature that moves control of a dealer's stock is a commercial change that needs consent states and per-retailer rollout.

The case deliberately takes the **retailer-platform** angle (valuations, Connect API, Co-Driver, Deal Builder as dealer software). The sibling book LISTED already reads Auto Trader as a marketplace (price ratings as a control loop, ARPR levers); this chapter does not repeat that angle and does not link to it, because its permalink is not in the allowed sibling list.

Productscape bricks touched (as comparison, not coverage): valu (valuation), stock and syndication, API distribution, entitlements, AI assistance. The case maps them to Auto Trader's documented products only where the public record supports it.

## Audience

Chief architects and engineering leaders of vehicle-data companies, dealer-software vendors and portals who must decide whether and how to bundle data products into a subscription, run a partner API, or put workflow features on dealers' stock.

## Success criteria

- [ ] Every Auto Trader claim carries a source and publication year; the developer documentation is cited as undated, read October 2026; 2019 infrastructure evidence is flagged as old and vendor-authored.
- [ ] The capability ladder is shown with dates and a diagram, and the derivative identifier is shown as the join key (documented API fields).
- [ ] The Connect contract is analyzed: capabilities per advertiser, split stock-write capabilities, lifecycle states with timers, per-channel publish status, change policy with dated changelog entries.
- [ ] The Deal Builder dispute is dated November 2025 (not 2024), separates press reports from Auto Trader's own account, and links the response to API changes (`Requested` state, January and May 2026).
- [ ] Inferences sit in a labeled callout or are marked "my reading"; a "Where the Public Evidence Stops" table lists the gaps.
- [ ] A trade-off table, a requirements table with labeled assumptions, a market comparison, a Chief Architect's view, a comparison with the book's patterns and Axleby, and 6–10 questions are present.
- [ ] Axleby facts match the ledger and Axleby's Connect XML is distinguished from Autotrader Connect.

## Non-goals

- Price ratings as a ranking control loop and the ARPR lever arithmetic (LISTED's automotive case).
- Valuation-model design in general ([[valuation-engine]]), syndication design ([[listing-syndication]]), AI governance ([[ai-in-dealer-workflows]]), API sunset policy ([[vehicle-data-apis]]): linked, not re-taught.
- Carfax and VWE (VWE has its own case, [[case-vwe]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Notification retry, ordering and signature behavior were not found in the parts of the developer documentation read; a later pass could read the remaining sections.
- The IMDA claim of 165 cancellations was seen only as a search summary and is not used.
- "Retailer Stores" did not appear in any results document; omitted.

## Decision log

- **2026-10-22** — Framed the case as a retailer platform (data and software supplier) rather than a marketplace, to avoid duplicating LISTED's automotive case.
- **2026-10-22** — Read the developer documentation directly (October 2026) to add capability, lifecycle, valuation, Co-Driver and Deals field-level evidence beyond the brief; all such facts are cited as undated documentation.
- **2026-10-22** — Kept the infrastructure section short because its best evidence is from about 2019; the 2026 data-platform posts carry the transferable practices.
- **2026-10-22** — Used Showroomly as the Axleby comparison on the integrator side and Lotwise/Axleby Data on the platform side.

## Sources

- **Internal**
  - [[part-10]], [[meet-axleby]], [[case-vwe]] — framing and handoff.
  - [[vehicle-capability-map]], [[specification-and-equipment]], [[listing-syndication]], [[identity-access-and-entitlements]], [[vehicle-data-apis]], [[valuation-engine]], [[ai-in-dealer-workflows]], [[deals-and-sales-documents]], [[onboarding-and-configuration]] — the book's patterns tested by the case.
  - `_research/brief-case-autotrader-carfax-vwe.md`, Part 1 — primary factual base.
- **External**
  - Auto Trader full-year results, 2023, 2024, 2025, 2026 — products, dates, numbers, Deal Builder response.
  - Autotrader Connect developer documentation (n.d., read 2026-10) — API contract and changelog.
  - Autotrader Engineering posts (2026); Google Cloud and Istio case studies (2019, undated) — platform evidence.
  - Car Dealer Magazine (2025-11-13) — the dealer protest.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: added Auto Trader's published forecast accuracy with its own-later-valuation caveat (item 12), clarified the stock-lever outlook, removed a buzzword, reading time corrected. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
