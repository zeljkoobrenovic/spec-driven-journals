---
status: accepted
revised: 2026-11-07
---

# Spec: Toolkit: Cards and Templates for Commerce Architecture Decisions

## Intent

Collect, in one reference page, the sixteen cards and templates the chapters introduce, so a reader can find the record that fits the question in front of them, copy its fields, and see it filled in once with Kestrel & Pine's ledger facts. Each card keeps the fields of the chapter that teaches it, names an owner, a system of record and a date, and links back to the chapters that use it. The page shows how the records cite each other, with the entity–owner table at the center, and ends with the architecture decision record.

## Audience

Readers new to commerce architecture who now have to keep these records: the engineer or integration lead who inherits a dozen systems and their flows benefits most, followed by the product manager or operations lead who owns a fact (stock, price, an order) and the consultant who wants a checklist of records to ask a client for.

## Success criteria

- [x] A "Find the Template for the Question on Your Desk" table maps a question to each of the sixteen tools and its owning chapter, with `#tool-N` anchors.
- [x] "How the Records Connect" has one mermaid diagram with a caption that states the point.
- [x] Each tool has a two-sentence purpose a newcomer can follow, the template as a table or fenced block, a short "how to use it" note, one filled Kestrel & Pine example labeled fictional and drawn from the ledger, and a "Used in" line of valid `[[permalink]]` links.
- [x] Card fields match the owning chapters: capability map (03), entity–owner table (04), integration inventory (24), contract card (26) and reconciliation card (25), ATP (10), order state (13), delivery promise (16), channel allocation (20), EDI partner card (22), app governance card (31), peak plan and ladder (33, 40), regulatory calendar (36), decision card (41), migration plan (42), ADR (44).
- [x] A reader new to the field can define every term the page uses (ATP, SSCC, GLN, DESADV, idempotency, system of record, dead-letter queue) from the page or the linked glossary.
- [x] No "Across Scale Stages" section, no take-away tiers and no failure-pattern block, as the style guide specifies for reference pages; about 4,500–6,500 words.
- [x] The page hands off to [[glossary]] and ends with Sources and Evidence citing Nygard (2011) with a link, and the fictional-merchant statement.

## Non-goals

- Re-teaching why each field exists — the owning chapters do that.
- The ownership map and vendor card — [[organizing-commerce-engineering]]; the W7 metric definitions — [[commerce-data-and-analytics]].
- Definitions — [[glossary]]; the full source list — [[bibliography]].
- New Kestrel & Pine facts: every example uses ledger facts or values the chapters already mark as illustrative.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The ledger gives two counts of unowned integrations in February 2027 (13 in the integration-styles line, 5 in the organizing-commerce-engineering line); the page avoids both until the ledger is reconciled.
- Chapters 10, 13, 16 and 20 teach their content without a named card; the ATP, order state, delivery promise and channel allocation cards are this page's distillation and should be cross-checked if those chapters add a card later.
- [[glossary]] did not exist when this page was written; the hand-off link resolves once it is built.

## Decision log

- **2026-11-07** — Put the entity–owner table at the center of the "How the Records Connect" diagram, because every other card either fills, changes or reads one of its rows.
- **2026-11-07** — Filled each example with one row or one object (the women's M moss Ridgewalker, order #1052877, Eva's lane, Bergzicht, the pre-order app, KP-004) rather than whole tables, to keep the page within length and every figure traceable to the ledger.
- **2026-11-07** — Took the contract card from the bol stock flow of [[api-contracts-and-versioning]] although PLAN assigns it with the reconciliation card to chapter 25, because chapter 26 is where the card is written out in full.
- **2026-11-07** — Extended Nygard's ADR with ownership, vendor, confirmation and review fields, matching how [[organizing-commerce-engineering]] uses decision records.

## Sources

- **Internal**
  - `PLAN.md` — the Reference entry listing the sixteen cards.
  - `_research/scenario-ledger.md` — every Kestrel & Pine figure and date.
  - `_research/style-guide.md` — reference-page format and valid permalinks.
  - [[commerce-capability-map]], [[boundaries-and-systems-of-record]], [[integration-styles]], [[events-consistency-and-reconciliation]], [[api-contracts-and-versioning]], [[inventory-and-availability]], [[order-management]], [[shipping-and-delivery]], [[marketplaces-and-channel-integration]], [[edi-and-e-invoicing]], [[extensibility-and-app-ecosystems]], [[peak-load-and-reliability]], [[journey-peak-day]], [[commerce-regulation]], [[build-buy-or-assemble]], [[replatforming-and-migration]], [[organizing-commerce-engineering]].
- **External**
  - [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), Michael Nygard, 2011.
  - [Strangler Fig Application](https://martinfowler.com/bliki/StranglerFigApplication.html), Martin Fowler, 2024.
  - [Feature Toggles](https://martinfowler.com/articles/feature-toggles.html), Pete Hodgson, 2017.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 1 mermaid diagram as illustrations and added 0 conceptual figures (article-illustrator). *(AI-mediated session)*
