---
status: accepted
revised: 2026-10-20
---

# Spec: Built to Be Replaced: Evolving a Marketplace Platform Over a Decade

## Intent

Close Parts I–VIII by stating the book's argument and turning it into a way to steer a marketplace platform over ten years. The argument: a listing marketplace is a liquidity machine, and its architecture should be judged by how reliably it turns fresh, trustworthy supply into matches with demand. The chapter connects every part to a stage of that machine, then gives the Chief Architect two durable tools. The first is **stressor analysis**, adapted from Barry O'Reilly's residuality theory, which finds the structures that survive an unknown future (capital events, regulation, channel shifts, fraud, supplier changes, physical-world shocks). The second is the **marketplace fitness function**, a small scorecard that says every quarter whether the machine still works. After reading it, the reader can tell which of their decisions must last a decade and which should be easy to replace, and can answer an owner's question about the cost of separating a brand.

## Audience

Group Chief Architects, CTOs and CPOs of multi-country, multi-vertical marketplace groups, and the architects who will inherit their decisions. They have read, or can navigate to, the earlier chapters; they need the synthesis, a method for the long horizon and a measurable steering instrument.

## Success criteria

- [ ] The book's argument is stated in one place, with a figure and a table mapping each part to a stage of the liquidity machine, the guarantee it gives, the metric it protects and its failure pattern.
- [ ] Reader can explain stressor, attractor, residue, naive and residual architecture, with dated sources for O'Reilly's work, and how the Productscape models used them.
- [ ] Reader can sort decisions into three rates of change (contracts and identifiers, engines, content) using Veldmark's 2027 decisions.
- [ ] Reader can follow Veldmark's stressor workshop: a ten-row stressor table across seven families, a residue count per component, one combined stressor that finds a missing residue, and a labeled carve-out estimate.
- [ ] Reader can apply portability and separability rules, with Adevinta's 2025 decentralization as dated evidence of separation cost.
- [ ] Reader can use "cost to reverse" to manage the centralization pendulum without re-teaching [[multi-country-platforms]].
- [ ] Reader has a twelve-function marketplace fitness scorecard with Veldmark baselines that match the ledger, owners, targets, kinds (monitor, drill, audit) and failure patterns.
- [ ] Chapter ends with a bridge to [[part-9]].

## Non-goals

- The tenancy model and the documented history of central versus local platforms: [[multi-country-platforms]].
- Consolidation sequence and synergy cases: [[platform-consolidation]].
- Team topology and the advice process: [[organizing-marketplace-engineering]].
- Migration techniques (strangler, parallel run, relevance parity): [[modernization-and-migration]].
- AI governance: [[ai-in-listing-systems]].
- Journey SLOs and unit-cost definitions: [[reliability-and-scale]] (reused here as fitness functions).
- Company case detail: [[case-adevinta]] and the other Part IX cases.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- O'Reilly's Procedia Computer Science papers (2020–2022) were found only through secondary references and are not cited; the chapter cites the 2024 Leanpub book and a 2020 Cutter article. Add the papers once their citations are verified.
- The publication year of the second edition of *Building Evolutionary Architectures* (2022) is from the author's knowledge; the Thoughtworks page fetched did not state it.
- Schibsted's 2016 "one global product and tech organization" quote is widely reported, not primary.
- The residue count per component and the carve-out estimate are Veldmark illustrations; a reviewer should check that they stay consistent if later chapters (39, 41, 42, 43) add facts about shared platforms.

## Decision log

- **2026-10-19** — Placed the synthesis of the book's argument near the start rather than at the end, so the stressor analysis and the scorecard can be judged against it; the end keeps a short restatement and the bridge to Part IX.
- **2026-10-19** — Made the investor's carve-out question the scene, because capital events are the dominant documented stressor for marketplace groups and the one Common Ground's 2027 design made worse.
- **2026-10-19** — Built the scorecard only from baselines already in the ledger and earlier chapters; added the stressor workshop, the scorecard adoption, the separability estimate and the tabletop to the ledger.
- **2026-10-19** — Treated the centralization pendulum through "cost to reverse" to avoid re-teaching [[multi-country-platforms]].

## Sources

- **Internal**
  - `_research/productscape-digest.md` §8 (residuality stressors, naive and residual architectures).
  - `_research/scenario-ledger.md` including all Additions by chapter.
  - `_research/brief-adevinta.md` Parts 1 and 5; `_research/brief-olx.md`; `_research/brief-real-estate-portals.md` (Zillow Offers); `_research/brief-automotive.md` (Auto Trader ArchUnit).
  - KEY POINTS and Chief Architect's view sections of every chapter in Parts I–VIII.
- **External**
  - O'Reilly, *Residues* (Leanpub, 2024); O'Reilly, Cutter Consortium (2020).
  - Ford, Parsons, Kua, Sadalage, *Building Evolutionary Architectures* (2017; 2nd ed. 2022).
  - Adevinta Annual Report 2019, Strategic Report 2025, 2021 and 2024 press releases; Zillow 8-K (2021); News24 on OLX Autos (2023); Auto Trader UK Engineering (2026); European Parliament Legislative Observatory on the GPSR (2023).

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: synthesis claims checked against chapter KEY POINTS and the ledger; Part IX bridge aligned with the eBay Classifieds case (thin shared layer); boost-history and five-weeks/four-weeks timing fixed; Schibsted 2016 citation pointed to [[industry-evolution]]; Adevinta AR 2023 added to Sources; Sources reformatted; American spelling; timetoread 46 min. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 1 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 7,081 → 7,046 prose words; outline unchanged; opening now names the Part IX dependency; "insertion freshness" aligned with F1's name "publication freshness"; two paragraphs split, several teaser sentences cut. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: Scorecard intro no longer promises a cadence column the table does not have. *(AI-mediated session)*
