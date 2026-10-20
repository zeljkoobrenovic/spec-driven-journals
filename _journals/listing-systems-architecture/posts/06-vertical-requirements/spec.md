---
status: accepted
revised: 2026-10-20
---

# Spec: Same Platform, Different Physics: How Listing Verticals Differ

## Intent

Close Part I by showing what really differs between listing verticals and turning that comparison into a decision method. The reader should leave with two tools the chapter owns: the **vertical requirement profile** (fourteen dimensions, filled in with numbers) and the **shared-versus-specific decision** (a four-layer share test: shared platform, shared engine with vertical content, group-owned vertical capability, brand-local product). The chapter argues that verticals differ in physics (supply mix, item identity, external system of record, lifetime, attribute density, lead value, transaction locus, regulation), that the shareable part is the machinery underneath, and that vertical capabilities such as vehicle identity and property entities should be built once with a single vertical owner.

## Audience

Chief architects and platform leads of multi-vertical marketplace groups, and engineering directors of vertical brands who are asked to join a shared platform. They know platforms and DDD; they need a disciplined way to decide what to share across real estate, automotive, jobs, general classifieds and recommerce, and evidence for where shared platforms have broken.

## Success criteria

- [ ] The reader can name the fourteen profile dimensions and say which part of the architecture each stresses.
- [ ] A five-vertical comparison table (general, real estate, automotive, jobs, recommerce) covers every dimension.
- [ ] Item identity, external system of record and transaction locus are explained with dated, sourced public evidence.
- [ ] The four-layer share test is defined, illustrated with an architecture diagram and a listing-flow diagram of extension points, and applied to Veldmark in a classification table.
- [ ] The Veldmark worked example compares the bike, the Golf and the Lyon apartment with ledger-consistent numbers, and derives lifetime and revenue-per-listing figures from the ledger.
- [ ] A trade-off table compares four strategies (horizontal-with-categories, shared core with extension points, separate stacks, vertical platform reused by horizontal sections) with conditions for each.
- [ ] Every company claim carries a dated source; inferences and judgements are labeled as such.
- [ ] The chapter ends with Chief Architect governance (what to decide, who decides, what to watch) and ten review questions.

## Non-goals

- Business definitions of horizontal, vertical, classifieds and lead generation: [[marketplace-taxonomy]].
- The capability map itself: [[business-capabilities]]; bounded contexts: [[bounded-contexts]].
- Detailed designs of the listing aggregate, taxonomies, attribute schemas, ingestion, entity resolution and publication: the Part II and III chapters.
- Multi-country tenancy and consolidation strategy: [[multi-country-platforms]], [[platform-consolidation]].
- Monetization models and payments: [[monetization-models]], [[transactions-and-payments]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- How much of Adevinta's 2023 "unified global platform" shipped is not public; the chapter states only the documented intent and reversal.
- The EPBD recast's transposition date (Art. 35) and certificate-template date (Art. 19) were checked against the Official Journal text on 2026-10-19; the advertisement provision itself is not quoted.
- Whether Motorvane's vehicle capability can be offered to Tradeyard Poland under the vehicle-data providers' licence terms is an open Veldmark question for [[normalization-and-enrichment]].

## Decision log

- **2026-10-19** — Organized the chapter around fourteen profile dimensions rather than per-vertical sections, because the decision method needs comparable rows; per-vertical evidence follows as "In Practice" subsections.
- **2026-10-19** — Chose a four-layer share test over a binary shared/specific split; the binary version cannot express "shared engine, vertical content" or "vertical capability, group-owned", which is where most real disagreements sit.
- **2026-10-19** — Set the scene in a mid-March 2027 scoping workshop; the Golf and Lyon listings occur later in 2027, so the worked example is framed as checking the profiles against them over the spring.
- **2026-10-19** — Added local illustrative numbers for Tradeyard Poland's cars (410,000 live) and jobs (140,000 live) sections and recorded them, with the layer-3 ownership decision, in the scenario ledger.

## Sources

- **Internal**
  - [[meet-veldmark]], scenario ledger — brands, volumes, worked examples, Common Ground.
  - [[business-capabilities]] — shared capability skeleton across verticals.
  - [[monetization-models]] — Motorvane and Keybridge revenue figures.
- **External**
  - Research briefs on automotive and other verticals, real-estate portals, listing data and ingestion, monetization, Adevinta and OLX (October 2026).
  - mobile.de Seller API; Autotrader FY2026 results and developer portal; CarGurus 10-K FY2025; NHTSA vPIC; Pkw-EnVKV.
  - Rightmove RTDF v1.4.1; Service-Public DPE page; RESO Web API; OpenImmo; OS Open UPRN; Zillow 10-K FY2025; AVIV interviews (2021, 2025).
  - ESCO; O*NET; Google JobPosting documentation; OLX job-role extraction (2024); Adevinta InfoJobs post (2025); Indeed pricing.
  - Vinted 2025 results and engineering posts (2024, 2026); Adevinta AR 2023 and Strategic Report 2025; eBay PBSE playbook.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: hand-off now to [[part-2]]; Golf raw vs deduplicated leads; EPBD dates verified on the Official Journal text; toolkit link added. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 7,297 → 7,299 prose words (evidence-dense; structure unchanged); opening now ties the chapter to [[business-capabilities]], [[bounded-contexts]] and Part II; topic sentences brought forward in four sections; jobs list count corrected to four; one H3 renamed. Spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: title changed from "…: General, Real Estate, Automotive and Jobs" to "Same Platform, Different Physics: How Listing Verticals Differ", because Table 2 and In Practice compare five verticals including recommerce (spec heading and PLAN.md updated; permalink unchanged); scene heading "One Platform for Four Physics?" renamed "One Platform for Four Verticals?" so it no longer clashes with the worked example's "Three Listings, Three Physics" (the four are the verticals Veldmark runs, the three are the listings examined). *(AI-mediated session)*
