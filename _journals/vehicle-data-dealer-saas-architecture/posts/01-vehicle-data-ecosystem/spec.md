---
status: accepted
revised: 2026-10-22
---

# Spec: Who Knows What About a Car: The Vehicle Data and Dealer Software Ecosystem

## Intent

Frame the whole book by answering one question: who produces, owns, sells and uses facts about a specific used car, and how did dealer software grow around those facts? The reader should leave with a map of the participants and the terms on which each holds its facts, a dated history that explains why today's integration landscape looks as it does (guides, DMS, portals, consolidation, connected cars), the argument for why the data half and the workflow half need each other and what they should share, the value chain (Identify → Check → Value → Stock → Advertise → Sell → Register → Trade → Insight) that later chapters hang on, the customer segments, and the four market archetypes (open register, dominant portal, closed register with data houses, no national register).

The chapter owns **vehicle data provider**, **dealer SaaS**, **DMS** (brief; deep in [[dms-integration]]), **dealer group**, **rooftop** (brief; deep in [[tenancy-and-dealer-groups]]) and **the value chain**.

Productscape bricks covered: framing for all bricks (the dependency spine, personas and relations, residuality stressors on portal consolidation and free register data).

## Audience

Chief architects, principal engineers and engineering leaders of vehicle-data companies, dealer-software vendors, portals, lessors and dealer groups who need the industry context before the technical chapters, and product and business leaders who must decide where their company sits in the ecosystem.

## Success criteria

- [ ] Names every participant class from the plan contract with what it knows, how its facts reach a platform, and examples by market.
- [ ] Gives a dated, sourced history from printed guides (1926, 1931, 1938) through DMS, the VIN, portals, consolidation and the EU Data Act, and says what layer each era left.
- [ ] Argues, with dated public evidence (Auto Trader, Carfax, Cox, VWE), that data and workflow need each other, and states what the two halves should share and keep apart, with the condition under which the rule fails.
- [ ] Defines the value chain with an owner per step, a requirements table (latency, freshness, consistency, availability) and a diagram showing it as a loop.
- [ ] Shows how the ecosystem's shape differs across NL, BE, DE, UK and US in an evidenced table and reduces it to four archetypes plus the Belgian warning.
- [ ] Includes an Axleby worked example (the January 2027 ecosystem map) consistent with the ledger, ecosystem-level failure handling, a trade-off table of ecosystem positions, a Chief Architect's view and questions to ask.
- [ ] Routes readers to the owning chapters rather than re-teaching them; every company claim carries a dated source.

## Non-goals

- Unit economics of dealers, data providers and SaaS ([[dealer-and-data-economics]]).
- The capability map and investment heat map ([[vehicle-capability-map]]); bounded contexts and sources of truth ([[vehicle-bounded-contexts]]).
- Register access regimes in depth ([[registers-and-official-data]]); DMS integration patterns ([[dms-integration]]); syndication mechanics ([[listing-syndication]]).
- The company cases ([[case-cox-automotive]], [[case-cdk-global]], [[case-auto-trader-uk]], [[case-vwe]]).
- A formal "Across Markets" section (Part I); the market comparison is part of the ecosystem argument instead.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Founding dates of HPI (1938), Eurotax (1960s) and the VIN mandate (1981) rest on encyclopedic sources; replace with primary sources if a company history page becomes fetchable.
- Belgian DMS landscape and DIV access were not verified; the Belgian column relies on the identity brief and Car-Pass.
- Black Book's founding date and current methodology were not verified; it appears only as a named US valuation reference.

## Decision log

- **2026-10-22** — Opened with the ecosystem map that Axleby built after the January 2027 License Breach, rather than tracing one car, because later chapters already trace specific cars (the Octavia, the Golf) and the map tests the chapter's claim that Axleby owns few of the facts it sells.
- **2026-10-22** — Described Axleby's and VWE's register relationship in plain words ("register-connected", "officially recognized RDW provider" as VWE's own claim) and avoided the term "authorised information provider" (consistency issue 13).
- **2026-10-22** — Cited the CDK outage effect on AutoNation only as a material per-share effect (consistency issue 10), and placed incadea with Volaris since 2018 (issue 1).
- **2026-10-22** — Replaced the Parts II–VII "Across Markets" heading with "How the Ecosystem's Shape Differs by Market", with five columns because NL and BE differ on plates, register openness and odometer history.

## Sources

- **Internal**
  - [[meet-axleby]] — group, brands, volumes, the License Breach.
  - [[dealer-and-data-economics]], [[vehicle-capability-map]], [[vehicle-bounded-contexts]] — the next Part I chapters.
  - [[case-cox-automotive]], [[case-cdk-global]], [[case-auto-trader-uk]], [[case-vwe]] — the documented positions.
- **External**
  - Auto Trader Group FY26 results (2026); Mobility Global information statement and 8-K (2026); Cox Automotive fact sheet (2018), formation release (2014) and sales insight (2026); CDK Global 10-K FY2021; AutoNation 10-K (2026); VWE API documentation (accessed 2026-10).
  - RDW open data (queried 2026-10-22); Car-Pass (2025 figures); KBA ZFZR and §39 StVG; DVLA VES and DVSA MOT API documentation; NMVTIS and 18 U.S.C. § 2721; Directive 1999/37/EC; Regulation (EU) 2023/2854; ADF 1.0 (2000); *Authenticom v. CDK* (7th Cir. 2017).
  - Wikipedia entries for founding dates (Kelley Blue Book, DAT, HPI, Eurotax, Reynolds and Reynolds, Carfax, Auto Trader, mobile.de, AutoScout24), accessed 2026-10.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: defined registers and expanded acronyms (CRM, DPPA, AAMVA, B2B), American spelling, added a second source for CDK 2022 events; no structural change. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
