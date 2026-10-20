---
status: accepted
revised: 2026-10-20
---

# Spec: mobile.de, Auto Trader and AutoScout24: Lessons from Automotive Marketplaces

## Intent

Use the public record of the leading automotive marketplaces (mobile.de, Autotrader UK, AutoScout24 and CarGurus, with OLX Autos as a contrast) as a tested case of listing architecture in a vertical where the item has a machine-readable identity, supply arrives through dealer software, and the supplier is also the paying customer. The page reads the companies' integration APIs, investor reports and engineering posts as architectural evidence, keeps documented fact, the author's interpretation and labeled reference-architecture inference visibly apart, and ends by testing the book's patterns and Veldmark's Motorvane against the case. After reading, a Chief Architect should hold three rules: write and publish the dealer contract (accountable integrators, idempotency, serialized writes, change feed with replay); govern a price rating as an exposure model once ranking or dealer tools use it; and treat every platform-controlled state on a supplier's stock as a commercial-model change that must be opt-in and reversible.

## Audience

Chief and enterprise architects, principal engineers and engineering leaders of vertical or multi-vertical marketplace groups, especially those running dealer-fed automotive brands or deciding how far a marketplace should reach into the transaction. They know APIs, event streams and ML serving; they need the evidence trail and the judgement.

## Success criteria

- [x] A dated timeline replaces the Veldmark scene, and every company fact carries a source and publication year; undated API manuals are marked n.d. with the read date.
- [x] Each company section states what is documented and where the evidence is thin; mobile.de's internals, AutoScout24's product platform and all valuation methods are explicitly not inferred as fact.
- [x] Inferences appear only in callouts labeled `INFERENCE, NOT DOCUMENTED` or in figure captions stating "not a description of".
- [x] A cross-case comparison of price products (bands, no-rating path, recalculation, dealer tools, link to ordering) with a control-loop diagram.
- [x] A trade-off table, a vertical-differences table, failure modes and a "Where the Public Evidence Stops" table.
- [x] At least two mermaid diagrams (four delivered).
- [x] The final comparison uses only ledger-consistent Veldmark facts (truncated-snapshot incident, Essen Golf timing and rating, Pro 150 overbilling, opt-in reservations, lead ledger, Elasticsearch until 2029) and links to the owning chapters.
- [x] Questions to ask (6–10) and grouped Sources and Evidence.

## Non-goals

- Not a company profile, market-share analysis or investment view.
- Does not re-teach feed contracts ([[listing-ingestion]]), enrichment and provenance ([[normalization-and-enrichment]]), model governance ([[ml-platform]]), ranking design ([[ranking]]), entitlements ([[products-and-entitlements]]) or the automotive requirement profile ([[vertical-requirements]]).
- Does not cover OLX Group beyond OLX Autos ([[case-olx]]) or mobile.de's place in Adevinta ([[case-adevinta]]).
- Does not cover US dealer-software conglomerates (Cox Automotive, Cars.com) beyond what the comparison needs; they are omitted.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- mobile.de's ownership as of October 2026: the Bundeskartellamt names Oak Germany Buyer GmbH as parent; whether the reported 2025 dual track ended in a sale or listing is not confirmed.
- Full-versus-delta semantics of mobile.de's XML upload (documented on a page not read).
- Whether price ratings feed ranking at Autotrader and AutoScout24.
- The corporate relationship between AutoScout24 and Trader (Canada) is not stated in the migration post; common ownership is widely understood but not verified here.
- mobile.de newsroom pages returned HTTP 403 on re-verification; their facts rest on the automotive brief's verified reads of the same day.

## Decision log

- **2026-10-19** — Organized by company, then a cross-case section, because each company's public evidence is of a different kind (API contracts, investor levers, platform posts, a 10-K); a phase structure like the Adevinta case did not fit.
- **2026-10-19** — Made the price rating the case's central technical thread, since it is the one product all four document and the one where the book's Unwatched Model pattern is visible in public (mobile.de's Preis-Planer linking price to search position).
- **2026-10-19** — Framed Deal Builder and the CarOffer and OLX Autos retreats as one "transaction ladder" (Figure 1) rather than as separate anecdotes; labeled the reading as the author's.
- **2026-10-19** — Avoided Autohaus Ruhrblick's package price in the Veldmark comparison, because chapter 17 and the ledger give different package details; used only the Pro 150 overbilling facts recorded in the ledger. No new canonical facts added.

## Sources

- **Internal**
  - [[listing-ingestion]], [[normalization-and-enrichment]], [[event-driven-listings]], [[listing-aggregate]], [[ranking]], [[ml-platform]], [[products-and-entitlements]], [[marketplace-taxonomy]], [[vertical-requirements]] — patterns the case tests.
  - [[meet-veldmark]] and the scenario ledger — Motorvane facts used in the comparison.
  - `_research/brief-automotive.md`, `brief-monetization-economics.md`, `brief-listing-data-ingestion.md`, `brief-platform-data-ml.md`, `brief-search-discovery.md`, `brief-olx.md`.
- **External (re-verified 19 October 2026)**
  - Autotrader full-year results to March 2026 (PDF text extracted and checked).
  - mobile.de Seller API and Ad Stream manuals; Bundeskartellamt clearance of 8 October 2026; CarGurus IMV help article; AutoScout24 Trader migration post and careers page; Berlin Buzzwords 2024 abstract; Press Gazette 2013 on Auto Trader's last print edition.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: re-verified 11 load-bearing claims (Autotrader FY26, mobile.de manuals, Bundeskartellamt, CarGurus 10-K, Fin24, AutoScout24, Berlin Buzzwords); tightened the Prosus exit wording, expanded WLTP, American spelling, timetoread updated. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,757 → 5,793 prose words; opening now places the case as the last of Part IX and names what it tests; one subheading renamed ("The platform, dated" → "The platform from 2019 to 2026"); buried points moved to paragraph openings; spec otherwise unchanged. *(AI-mediated session)*
- **2026-10-20** — Trade-offs heading capitalized as in the 45 chapters. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: "Vertical Differences: How the Lessons Transfer" renamed to the fixed case heading "Vertical Differences in the Record"; the table under it is unchanged. *(AI-mediated session)*
