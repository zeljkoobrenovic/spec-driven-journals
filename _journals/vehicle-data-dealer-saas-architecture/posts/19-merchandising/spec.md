---
status: accepted
revised: 2026-10-22
---

# Spec: Making the Car Sellable Online: Photos, Descriptions and Equipment

## Intent

Show how a dealer SaaS platform produces complete, accurate, lawful and attractive adverts at scale. The chapter argues that the advert is a rendering of sourced, versioned facts plus a small amount of dealer-authored content, not a form the dealer types. Its media pipeline is guided, offline-tolerant and rights-aware. Equipment text never claims more than the specification's resolution state supports. Generated descriptions are grounded in a fact sheet and gated by a deterministic claim checker. Mandatory disclosures are computed by versioned per-market rule sets. A listing quality score earns its keep through a ranked, outcome-tested action list. After reading, an architect can design the advert content model, the composer and its re-render triggers, the media pipeline's vehicle-specific parts, the generation guardrails and the disclosure engine, and can say where merchandising ends and syndication begins.

Productscape bricks covered: `advf` (the advert editor and advert store side; channel delivery is covered by `listing-syndication`). [ADDED]: the vehicle media pipeline.

## Audience

Chief architects, product and engineering leads of dealer software, portals and dealer groups that run their own merchandising, plus data and ML leads asked to ship generated descriptions. They know content pipelines and LLMs. They need the domain: why the edition and mileage in an advert are liabilities, what representative financing examples and energy-label rules require per market, and how portals constrain photos.

## Success criteria

- [ ] Reader can distinguish stock item, advert and channel listing, and classify every advert element into the five content kinds with its source of truth and edit rights.
- [ ] Reader can sketch the composer, media pipeline, generator and claim checker, disclosure rules and quality scorer, with what each owns and the boundary with syndication.
- [ ] Reader can explain how equipment wording follows the resolution state, including the intersection rule for "edition unknown".
- [ ] Reader can specify a fact sheet, a claim checker and a generation record, and explain why prices and regulated figures never enter generated prose.
- [ ] Reader can name, with dated sources, the financing-example rules (CCD2 Art. 8, PAngV §17 two-thirds, CONC 3.5 51%, Regulation Z triggering terms), the energy-label boundary (Directive 1999/94/EC, Pkw-EnVKV new-car presumption), Car-Pass enforcement and the EU 30-day prior-price rule.
- [ ] Reader can work through the Axleby seven-day gap, the 307 stale-text adverts of the Odometer Correction and Brandsma's Golf Variant advert.
- [ ] Reader can handle corrected facts, duplicate and partial photo sets, conflicting edits, provider outages, stale rate cards and missed claims.
- [ ] Reader can state what is common and what is a market rule set across NL/BE, DE, UK and US.

## Non-goals

- Channel adapters, publish rules, per-channel validation, withdrawal and reconciliation (`listing-syndication`).
- Specification resolution, build-data purchasing and portal equipment-code mapping (`specification-and-equipment`).
- Price setting, repricing and price history (`used-car-pricing`); the stock lifecycle and preparation track (`inventory-and-vehicle-dossier`).
- Financing referral, lender integration and the deal's disclosure record (`deals-and-sales-documents`); battery certificates (`ev-battery-health`).
- Generic image engineering: derivatives, CDN, perceptual hashing, storage tiers (LISTED `media-pipeline`).
- The wider AI strategy for dealer workflows (`ai-in-dealer-workflows`); license mechanics (`data-licensing-and-governance`).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Whether Belgian law itself requires a Car-Pass link in every online advert, or only AutoScout24 enforces it, is unverified; the chapter applies it to all Belgian channels as Axleby policy.
- UK reference-pricing rules beyond the DMCC Act's general misleading-actions test, and US state dealer-advertising law, were not researched.
- Auto Trader has not published how Co-Driver grounds or checks generated text; the chapter labels its reading as inference.
- Dutch and Belgian transposition details of CCD2 Article 8 (exact warning wording) were not checked.

## Decision log

- **2026-10-22** — Framed the chapter around the seven-day gap (58 vs 51 days-to-turn, from `dealer-and-data-economics`) and the Sticky Error in advert text, rather than around photo aesthetics, because time-to-advert and correctness are where architecture moves money.
- **2026-10-22** — Chose a five-kind content model ("render, don't copy") over a richer form editor; dealer free text is kept but checked for stale facts.
- **2026-10-22** — Made the deterministic claim checker, not prompt design, the central guardrail for generated descriptions, and kept prices and regulated figures out of prose.
- **2026-10-22** — Linked LISTED's `media-pipeline` for generic image engineering and kept only vehicle-specific media concerns (guided capture, intake vs retail photos, angle tags, masking, cross-tenant reuse).

## Sources

- **Internal**
  - [[inventory-and-vehicle-dossier]], [[specification-and-equipment]], [[used-car-pricing]] — inputs to the advert.
  - [[listing-syndication]] — the next page; channel validation and delivery.
  - [[deals-and-sales-documents]], [[ev-battery-health]], [[data-licensing-and-governance]], [[journey-data-correction]], [[dealer-and-data-economics]].
  - `_research/brief-syndication-leads.md` (2.7–2.9), `_research/brief-dealer-workflows-economics.md` (Parts 5–6), `_research/brief-specification-history.md` (1.4–1.6), `_research/brief-case-autotrader-carfax-vwe.md` (1.3, 1.7), `_research/productscape-digest.md` (`advf`).
- **External**
  - Auto Trader Group FY2025 and FY2026 results; Autotrader Connect developer documentation; mobile.de Seller API; AutoScout24 Listing Creation API changelog; Marktplaats API; Google Merchant Center vehicle ads help; DAT Austria VIN guide (2026).
  - CCD2 (CELEX 32023L2225); PAngV §17; FCA CONC 3.5; 12 CFR 1026.24; Directive 1999/94/EC; Pkw-EnVKV; Directive (EU) 2019/2161 (Art. 6a of 98/6/EC); UCPD (2005/29/EC); DMCC Act 2024 s226; Car-Pass; RDW open data.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Golf Variant mileage 61,302 km, appraisal three days earlier and stock-in timing aligned with journey-inventory-to-portal; 118,000 described as a sample. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: American spelling (labeling). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
