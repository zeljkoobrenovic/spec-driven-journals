---
status: accepted
revised: 2026-11-08
---

# Spec: Part II — CATALOG: Products, Prices and Promises

## Intent

Orient a reader new to commerce architecture to Part II: the facts a shopper sees before the cart (product, price, discount, search result, "in stock") look alike but have different owners, different clocks and different legal weight, so each needs its own system of record and its own path to every channel, and every copy needs a source, an effective date and a reconciliation. Frame the part through the Kestrel & Pine cases its five chapters actually use: the season typed four times, the Price Drift, the Black Friday Stacking Bug, the waterproof jacket nobody could find, and the Black Friday Oversell.

## Audience

Readers new to commerce architecture who are about to read the catalog chapters. Product managers and engineers joining a merchant's catalog, pricing or storefront team benefit most; leaders get the part's argument from the callouts and the table alone.

## Success criteria

- [x] Opens with exactly three tight KEY POINTS (a bold claim plus one short sentence each), then `<br>`; no IN THIS PART or FAILURE PATTERNS block.
- [ ] The lead frames the part in business terms first, says where it sits in Eva's jacket (before "add to cart"), and names Kestrel & Pine as fictional once.
- [ ] Kestrel & Pine figures match the ledger and the chapters (€8,200 / 410 orders; €52,000 / 2,860 orders; €96,000 / 1,340 units / 1,120 orders; 9.4% to 4.1%; about 140 declined variants).
- [ ] One mermaid diagram of 5–9 nodes with a Figure caption showing the part's shape.
- [ ] A "Chapters in this part" list with one paragraph per chapter in config order, each opening with the `[[permalink]]`, bolding the question it decides and naming its Kestrel & Pine case; ends with "Begin with [[product-information]]."
- [ ] No "Across Scale Stages" section and no take-away tiers; a one-line Sources and Evidence.
- [ ] A reader new to the field meets no undefined term: the few terms used (PIM, SKU, GTIN, ERP, WMS, system of record) are either explained in a clause or carried by the chapter links.
- [ ] 500–900 words.

## Non-goals

Teaching the product model, price selection, promotion stacking, indexing or availability arithmetic (the chapters own them); scale-stage comparisons (each chapter has its own table); external factual claims.

## Modalities

Article only for now.

- [ ] `checklist.md`
- [ ] `summary.md`
- [ ] `dialog.md`
- [ ] `comics.md`

## Open questions

- `commerce-platform-landscape`, the last chapter of Part I, should hand off to [[part-2]] in its closing paragraph; not checked in this session.

## Decision log

- **2026-11-07** — Modeled on the vehicle-data book's part-2 introduction (callouts, a three-paragraph lead, one diagram, a paragraph per chapter), with the mermaid diagram the intro brief asks for instead of images.
- **2026-11-07** — Failure patterns: The Spaghetti Junction, The Price Nobody Can Explain and The Phantom Stock, one per family of catalog fact; The Message in a Bottle and The First Snowfall are left to the chapters that own them.
- **2026-11-07** — Added a five-row table (what the shopper sees, the fact, the owner, how fast it changes, the chapter) because the part's argument is the difference in clocks, and a table shows that faster than prose.

## Sources

- **Internal**
  - `config.yaml`, `PLAN.md`, `_research/scenario-ledger.md` and `_research/INTRO-BRIEF.md`.
  - The callouts, scene-setting sections and closing paragraphs of [[product-information]], [[pricing-architecture]], [[commerce-promotions]], [[commerce-search-and-discovery]] and [[inventory-and-availability]].
- **External**
  - None; the introduction makes no factual claim of its own.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: tightened the chapter list and lead, defined SKU, GTIN, PIM and system of record on first use. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: "the scenario ledger's" figures rephrased. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 1 mermaid diagram as illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
- **2026-11-08** — Openers: dropped IN THIS PART and FAILURE PATTERNS blocks; tightened KEY POINTS (author request). *(AI-mediated session)*
