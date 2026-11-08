---
status: accepted
revised: 2026-11-07
---

# Spec: The Map of a Commerce Platform: Capabilities and Layers

## Intent

Give a reader who is new to commerce architecture one map of all the parts: about two dozen capabilities grouped into six layers, the business fact each one is the natural home for, the flows that join them with their freshness and consistency requirements, and the three ways vendors cover the map (suite, platform plus apps, best-of-breed, with ERP-centered and specialist-group variants). The reader should leave able to place any system, vendor or product page on the map, to see gaps (empty boxes) and overlaps (boxes with several writers), and to recognize derived facts such as availability. The chapter is the frame every later chapter is read against; it introduces the ownership question and hands it to [[boundaries-and-systems-of-record]].

## Audience

Readers new to commerce architecture. The engineer, product manager or analyst who has just joined a merchant and needs to understand "what is all this software" benefits most; the consultant or leader who must judge a vendor proposal benefits from the "reading a product page against the map" method. Noor Visser's whiteboard in February 2027 is written at their altitude.

## Success criteria

- [x] A capability table lists every capability named in the PLAN contract (storefront, search, cart and checkout, B2B, POS, service, product information, pricing, promotions, inventory and availability, payments, order management, tax and ledger, warehouse, shipping, returns, store operations, marketplaces, EDI, ERP, integration, identity, data, platform services) with its plain-words job, the fact it is the home for, and the owning chapter as a `[[link]]`.
- [x] Capabilities are defined before systems, and the distinction capability / system / vendor product / layer / fact / flow is explicit.
- [x] Derived facts (availability, delivery promise) are distinguished from recorded facts.
- [x] A flows table gives freshness, consistency and failure behavior per flow, and a second diagram shows the flows.
- [x] Suite, platform plus apps and best-of-breed are each explained in a paragraph with dated, sourced examples (Salesforce 2026, Adobe 2026, Shopify pricing and 2023 logistics sale, Lightspeed FY2026, MACH Alliance 2020 and 2026, Business Central connector 2026, Katapull 2025–2026 from public pages only), with a trade-off table.
- [x] Kestrel & Pine's thirteen systems are placed on the map with the empty boxes (product information, order management, availability, identity) and the overlaps (six writers of stock, three writers of price), using ledger numbers (€96,000, 600 variants, €8,200, €19,400, 2.3%).
- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] The three take-away tiers are present; questions to ask; the Across Scale Stages table (optional in Part I) is included because the number of filled boxes changes with stage.
- [x] Under 6,500 words including tables.

## Non-goals

- Deciding which system is the record when several hold a fact — [[boundaries-and-systems-of-record]].
- Vendor categories, pricing models and the market timeline — [[commerce-platform-landscape]].
- The economics of suite versus assembly — [[build-buy-or-assemble]]; the stages as a model — [[commerce-scaling-stages]].
- The internals of any single capability; each row of the table links to the chapter that owns it.
- Integration styles and reliability — [[part-6]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The six-layer grouping is the author's; the Domain Coverage page may want to reconcile it with the Productscape model families' own groupings.
- "Store operations" and "point of sale" are listed as two capabilities that share one fact (store stock); a reviewer may prefer to merge them.
- The flows table's freshness figures are judgement; [[inventory-and-availability]] and [[pricing-architecture]] may tighten them.

## Decision log

- **2026-11-07** — Chose capabilities-first over systems-first for the map, because overlaps and gaps are invisible in a systems view; the Kestrel & Pine scene makes the same move on a whiteboard.
- **2026-11-07** — Six layers rather than the three or four of most vendor diagrams, so that operations (warehouse, carrier, store, returns) and partners (marketplaces, EDI, ERP) each get a layer; those are the layers hosted platforms do not cover, which is the chapter's point about vendor coverage.
- **2026-11-07** — Reduced the Kestrel & Pine placement table to the boxes that are empty or overlapping, after the first draft exceeded the length cap; the fully covered boxes are listed in one sentence instead.
- **2026-11-07** — Used no research-and-practitioner source; the layers and flows are synthesis, and the chapter says so rather than borrowing authority from a reference that does not describe this map.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — systems landscape, incidents, Waypoint decisions.
  - `_research/brief-platform-landscape.md` — platform categories, specialist layers, MACH, pricing, vendor-claim units, Katapull public facts.
  - `_research/brief-commerce-business-models.md` — Eurostat EDI figure, when OMS/PIM/WMS are introduced.
  - `_research/productscape-digest.md` — cross-model capability inventory, used as a checklist of capabilities only.
  - [[meet-kestrel-and-pine]], [[boundaries-and-systems-of-record]], [[commerce-platform-landscape]] — neighbors.
- **External**
  - Salesforce press release (2026-07-06); Adobe Commerce platform and services page (2026-10-21); Shopify pricing (accessed 2026-11), Shopify Logistics sale (2023-06-06), Shopify Q4 2025 results (2026-02-11); Lightspeed FY2026 results (2026-05-21); Microsoft Business Central Shopify Connector (2026-09-22); Manhattan "What is an OMS"; Akeneo; Fluent Commerce; ChannelEngine; Katapull pages and Dutch IT Channel (2025); EPAM MACH founding release (2020-06-24); MACH Alliance Enterprise Technology Report (2026-02-18); Eurostat E-commerce statistics (2024 reference year).

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: aligned the empty boxes with the ledger (four: product information, order management, availability, customer identity), linked the scale stages to their owning chapter, and defined theme, headless, Peppol and BI. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-11-08** — Added four figures: three ways to cover the map, the map filling with scale, reading a vendor page, and four ways the map fails (article-illustrator). *(AI-mediated session)*
