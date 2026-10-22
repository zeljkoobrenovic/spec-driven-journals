---
status: accepted
revised: 2026-10-22
---

# Spec: Cox Automotive: Building a Portfolio Into a Platform

## Intent

Read Cox Automotive's public record as an architecture case about turning an acquired portfolio into a platform. The chapter must show, with dated sources, the order in which Cox shared things across its brands (infrastructure 2018, governance 2019, login 2020–2021, data 2022, federated APIs 2024, embedded features 2026). It must show what each layer left inside each product, why owning data on both sides of the transaction mattered more than owning a minority DMS, and where the public evidence stops. The reader should leave with a realistic sense of how long portfolio integration takes and which shared contracts to design first: identity and tenancy, the vehicle key, and license checks.

Productscape bricks: none owned. This is a case study. It illustrates the identity, tenancy, vehicle identity, valuation and market-data, remarketing and DMS-integration bricks owned by the chapters linked below.

## Audience

Chief architects and engineering leaders of vehicle-data and dealer-software groups that grow by acquisition, and anyone asked to "make our brands feel like one company". They should leave able to compare their own integration plan with the best-documented real sequence and to name the layers their plan skips.

## Success criteria

- [x] Every Cox claim carries a source and publication year; vendor-authored evidence (AWS, Apollo, Databricks) is flagged as such; evidence older than about three years is dated in the sentence.
- [x] Reference-architecture inferences sit in `INFERENCE, NOT DOCUMENTED` callouts. No Cox internals are invented.
- [x] The integration sequence is shown as a dated diagram and a table of what each layer shares and leaves per product.
- [x] Bridge ID's documented linking model is explained, along with its limit: no shared tenancy is documented.
- [x] The MUVVI methodology is presented as the counter-example to the Confident Valuation.
- [x] Cox's DMS position (Dealertrack about 17% in 2017, litigation against CDK 2017–2019, incadea 2015–2018) is presented as DMS Hostage at portfolio scale.
- [x] The European footprint is stated from the 2026 Cox Automotive Europe site and dated trade sources. The chapter says plainly that no NL or BE business was found, and that UK Autotrader is not Cox.
- [x] It ends with "Where the Public Evidence Stops", the Chief Architect's view, two comparison tables (book patterns, Axleby choices) and questions to ask.

## Non-goals

- The CDK side of the DMS access dispute, Fortellis and the 2024 ransomware outage belong to [[case-cdk-global]].
- How to design tenancy, identity or the vehicle key in depth: [[tenancy-and-dealer-groups]], [[identity-access-and-entitlements]], [[vehicle-identity]].
- Per-car valuation design: [[valuation-engine]].
- Portfolio integration method for Axleby: [[one-platform-from-many-products]].
- No "Across Markets" section is required for Part X. The European footprint is covered in its own section instead.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Whether Bridge ID shares roles or dealer entities across products is not public. A federation option appears only in search summaries.
- The current status of Modix, Xtime Europe and pkwNOW is unknown, and so is any Cox stake in Autorola (unverified; not stated).
- How far the AWS migration got after 2019, and where the Dealertrack DMS runs.
- Cox's reasons for selling incadea.

## Decision log

- **2026-10-22** — Organized the case around the integration *sequence* rather than brand by brand, because the dated order of layers is the transferable lesson and the brand list is volatile.
- **2026-10-22** — Kept the litigation narrow (Cox's filing and settlement only) to avoid duplicating [[case-cdk-global]].
- **2026-10-22** — Used the 2026 Cox Automotive Europe site for the European footprint and declined to name brands that site does not list, rather than relying on the out-of-date 2014 international list.
- **2026-10-22** — Kept Axleby to the final comparison, following the Part X convention set by BOOKED's case chapters.

## Sources

- **Internal**
  - `_research/brief-case-cox-cdk.md` — primary evidence base.
  - `_research/brief-platform-apis-operations.md` — AWS data-marketplace and Neptune identity-graph evidence.
  - [[one-platform-from-many-products]], [[case-cdk-global]], [[dms-integration]], [[valuation-engine]] — the book patterns the case is compared against.
- **External**
  - Cox Automotive releases (2014, 2022, 2026), fact sheet (2018), Bridge ID page and Cox Automotive Europe site (read 2026-10) — portfolio, identity, data and European footprint.
  - Manheim, *Summary Methodology for the Manheim Used Vehicle Value Index* (2023) — index methodology.
  - Amazon (2018), Classmethod re:Invent report (2019), PlatformCon (2024), Apollo GraphQL (n.d.) — infrastructure, governance and API evidence.
  - CDK Global 10-Q (2021) and Seventh Circuit opinion (2017) — litigation and market shares.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: aligned Bridge ID with the fetched Bridge Federation page (consistency item 18), attributed the size claim to Cox's 2026 boilerplate, reading time corrected. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: American spelling (enrollment). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
