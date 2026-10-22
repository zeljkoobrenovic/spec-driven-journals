---
status: accepted
revised: 2026-10-22
---

# Spec: Domain Coverage: From the Productscape Model to Chapters

## Intent

A Reference page that makes the book's planning auditable. It maps every root group (5), group (11), product brick (28) and module (140) of the Productscape research model behind the book to the chapters that cover it, with exact identifiers, marked *primary* (owns the brick's purpose and terms) or *also* (covers a module, uses the brick, or departs from its decomposition), and names the fictional Axleby system each chapter uses as its example. It also lists where the book departs from the model's decomposition, the nine [ADDED] domains and why, the remaining digest gaps placed in chapters, the seven personas and twelve value streams mapped to chapters, the seven model stressors and seven digest-proposed stressors mapped to [[evolving-the-vehicle-platform]] and the chapters that build each residue, and what the book deliberately leaves out, with reasons. After reading, a reader can find the chapter for any capability in their own map and see which cross-cutting capabilities a journey-driven map tends to miss.

Provenance must be explicit: the model describes one real company (VWE Automotive) from public sources, its internals are inferred and its KPI values are invented seeds; it is used as a research map only; VWE facts appear only in [[case-vwe]] from dated public sources; Axleby is fictional.

Productscape bricks covered: **all** 28 (`rdwc`, `vidn`, `vhis`, `evsh`, `dmgc`, `mktd`, `valu`, `bpmc`, `dosr`, `occm`, `tapp`, `advf`, `dweb`, `admn`, `finc`, `rdwt`, `mats`, `impx`, `b2bt`, `vapi`, `fenr`, `mins`, `cool`, `fnnk`, `ctrv`, `iden`, `bill`, `dgov`), all 140 modules, and the stressors `rdwoutage`, `freedata`, `portalconsolidation`, `bpmchange`, `evshift`, `acquisitions`, `privacy`.

## Audience

Readers who arrive with their own capability map (chief and enterprise architects, product and engineering directors of vehicle-data companies, dealer-software vendors and dealer groups) and want the right chapter fast; reviewers checking that the book covers the domain; future writers extending the book.

## Success criteria

- [x] Provenance stated: model path and version, that it describes VWE from public sources with inferred internals and seed KPI values, that nothing in it is presented as VWE fact, that brand names in brick names are neutralized, and that Axleby is fictional.
- [x] Every one of the 28 bricks appears in a coverage table with its id, group, root group, a primary chapter and, where relevant, "also" chapters, as valid `[[permalink]]` links.
- [x] Every one of the 140 module identifiers appears exactly as in the digest, with its layer and covering chapter (checked by script: 140 of 140, none extra).
- [x] States that nothing is uncovered and names the thinly covered bricks (`ctrv`, `mats`, `finc`, `mins` benchmark module) with reasons.
- [x] A departures table covering the model's inconsistencies the book resolves (dossier and stock, appraisal and buying app, identity, license-check edges, billing edges, shared stores).
- [x] The nine [ADDED] domains with model traces, reason and owning chapter; the other digest gaps placed in chapters; personas, value streams and stressors mapped; deliberate omissions with reasons.
- [x] Preface-like callouts with exactly three KEY POINTS and two failure patterns; no "Across Markets" section; no Axleby scene; under 8,000 words.

## Non-goals

- Re-arguing the capability map or heat map ([[vehicle-capability-map]]), the context map and entity–owner table ([[vehicle-bounded-contexts]]), or portfolio integration ([[one-platform-from-many-products]]).
- Company-specific claims; [[case-vwe]] and the topic chapters carry them with dated sources.
- Model KPI values, deployment topology, data-asset governance fields and the model's tutorial walkthrough.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only.

## Open questions

- Several chapters were not yet written when this page was built (`vehicle-capability-map`, `vehicle-bounded-contexts`, `consumer-vehicle-checks`, the four journeys, `one-platform-from-many-products`, `organizing-engineering`, `modernizing-the-platform`, `ai-in-dealer-workflows`, `evolving-the-vehicle-platform`); their rows rely on PLAN contracts. Re-check especially `consumer-vehicle-checks` (all `fnnk` and `ctrv` modules), `evolving-the-vehicle-platform` (all fourteen stressors) and `vehicle-bounded-contexts` (the shared-store departure) once they exist.
- `build-buy-or-partner` had an index but no spec at build time; its rows (licensed build data, estimating, supplier-loss stressor) follow its contract.
- The archive store's retention is placed in `privacy-and-retention` and `deals-and-sales-documents`; neither names the write-once archive explicitly. Revisit if a chapter takes ownership.

## Decision log

- **2026-10-22** — Bricks get neutral names (VWE product names removed); module identifiers are kept exactly, because they are the model's keys and the page's audit value depends on them.
- **2026-10-22** — Modules mapped one row each where chapters split them, and grouped in one row where a single chapter covers the whole brick (`bpmc`, `mats`, `impx`, `ctrv`), to keep the page a usable lookup table.
- **2026-10-22** — Added a "Where the Book Departs From the Model" section, because the digest's inconsistencies (§10.2) are design decisions the chapters took, not gaps.
- **2026-10-22** — Stressors mapped twice: to `evolving-the-vehicle-platform` as the owner of stressor analysis, and to the chapter that builds each residue.

## Sources

- Internal: every chapter spec's "Productscape bricks" line; `PLAN.md` contract "Bricks" fields and [ADDED] markings; [[vehicle-capability-map]], [[vehicle-bounded-contexts]], [[evolving-the-vehicle-platform]], [[case-vwe]].
- `_research/productscape-digest.md` §1, §2, §3, §4, §5, §7, §10.
- Productscape model: `productscape-examples/_config/product-domains/mobility/vehicle-data-and-dealer-saas-platform/` (portfolio v1.0, updated 2026-10-10).
- O'Reilly, *Residues* (Leanpub, 2024).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: verified placements against the finished chapters, named Axleby systems for added domains and empty cells, rewrote the added-stressor table to match the evolution chapter's sixteen stressors, callouts aligned with BOOKED. *(AI-mediated session)*
