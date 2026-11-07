---
status: accepted
revised: 2026-11-07
---

# Spec: Domain Coverage: From Three Model Families to Forty-Nine Chapters

## Intent

Give the reader, and the author, an audit trail of the book's planning: a lookup table from every capability in the three Productscape model families the book was planned against (the merchant platform model, the retail marketplace model and the nine specialist-product models) to the chapter that covers it, read in both directions (by capability, grouped by part; by model, grouped by root group). The page states plainly what the models are and are not (inferred from public product behavior; seed values; research maps; never a source for a fact about a company), records which capabilities are mentioned only briefly or left out and why, names the places where the book's decomposition deliberately departs from the models (no integration layer, no scale stages, no failure patterns, no cross-product journeys, no evolution), maps the models' personas to the book's reader roles and the Kestrel & Pine cast, and hands off to the Toolkit.

## Audience

Readers new to commerce architecture who want to know whether "their" capability is in the book and where to start: the engineer or product manager who has just been handed a system with a vendor's name on it, and the consultant who needs to check the book's coverage against a client's estate. The author and future chapter writers, who use it to find gaps and to keep the models' provenance rules visible.

## Success criteria

- [x] The three model families are named with their paths, short codes, inspiration, brick counts and root groups, and the four provenance rules (inferred model, seed values, capability inventory only for the specialist models, fictional running example) are stated before any table.
- [x] Coverage by capability covers the digest's 152 capabilities, merged into rows grouped by the book's parts, each row naming the models that carry the capability and the primary chapter with secondary chapters in parentheses.
- [x] Coverage by model gives one compact table per family; the nine specialist models are shown by capability only, with no statement about any company's plans, finances, pricing, roadmap or strategy, and no label named.
- [x] The digest's eleven GAP capabilities are each placed as covered, mentioned only, thin or left out, with a reason; thin spots found while checking the written chapters are added to the same table.
- [x] The departures table names what the models lack (integration layer, scale-stage view, failure patterns, cross-product journeys, evolution) and where the book's decomposition disagrees (one order record, one stock ledger, checkout separate from payments, fraud in security, one price source, returns as a flow, regulation as a calendar), each with the chapter that argues it.
- [x] The personas table maps the models' persona clusters to the book's reader roles, a Kestrel & Pine seat and three starting chapters.
- [x] No KPI value, module name carrying a vendor name, or stressor about group ownership appears; every chapter link is a valid permalink; the page closes with a hand-off to [[toolkit]] and ends with the fictional-merchant statement.
- [x] No "Across Scale Stages" section, no take-away tiers and no failure-pattern block, as the style guide specifies for reference pages; 2,500–4,000 words.

## Non-goals

- The capability map itself and how to place a vendor on it — [[commerce-capability-map]].
- The entity–owner table and the rule for choosing a system of record — [[boundaries-and-systems-of-record]].
- The scale-stage map — [[commerce-scaling-stages]]; the failure patterns — [[where-commerce-platforms-go-wrong]].
- Any fact about Shopify, Amazon or a specialist vendor — the cases in [[part-11]] and the chapters, from dated public sources.
- Templates and cards — [[toolkit]]; definitions — [[glossary]]; sources — [[bibliography]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- [[case-shopify]] was still being written when this page was compiled; its placements follow the chapter contract and should be re-checked when the case is finished.
- Emissions reporting on deliveries and lot traceability are listed as left out or thin; if a later edition adds a sidebar to [[shipping-and-delivery]] or [[warehouse-and-fulfillment]], move the row to "covered".
- The brick counts per model were taken from the digest's inventories on 7 November 2026; if the models change in the sibling repository, the counts and the 152-capability total will drift.

## Decision log

- **2026-11-07** — Merged the digest's 152 capabilities into about fifty rows per chapter topic rather than reproducing the inventory, because the page is a lookup table for a newcomer and the digest remains the complete record; the per-model tables keep the brick ids so the two can be cross-checked.
- **2026-11-07** — Showed the nine specialist models in one table by capability only, with no vendor labels, so the page honors the provenance rule that Productscape files are research maps and never sources about a company.
- **2026-11-07** — Verified gap placements against the written chapters with text searches (reviews, membership, retail media, CRM, fiscal receipts, lots, dropshipping, forecasting, KYC, brand registry, hosting) and added six thin spots the digest did not flag, because a coverage page that reports only planned coverage is not an audit.
- **2026-11-07** — Mapped personas to reader roles and Kestrel & Pine seats with three starting chapters each, so the page doubles as a reading route for each role.

## Sources

- **Internal**
  - `_research/productscape-digest.md` — the model inventories, the cross-model capability table with its GAP list, data-asset ownership, personas and residuality notes.
  - `PLAN.md` — the Provenance section, the chapter contracts ("Owns") and the Reference entry for this page.
  - `_research/style-guide.md` — page format for reference pages, valid permalinks, the Katapull and Productscape rule.
  - `_research/scenario-ledger.md` and [[meet-kestrel-and-pine]] — the cast used for the persona seats.
  - The written chapters in `posts/` — the openers and text searches used to confirm where each capability landed.
- **External**
  - The three Productscape model families in the author's sibling repository (`productscape-examples/_config/product-domains/platforms/merchant-commerce-platform/`, `.../marketplaces/online-retail-marketplace/`, `.../katapull-group/`), read only through the digest.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: hand-off to toolkit added, timetoread. *(AI-mediated session)*
