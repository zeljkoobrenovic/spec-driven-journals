---
status: accepted
revised: 2026-10-19
---

# Spec: Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models

## Intent

Show how to decompose a listing marketplace with domain-driven design's strategic tools, and where the boundaries belong. The chapter must establish that "listing" means different things in supply, catalog, entity resolution, trust, search, alerts, monetization, contact, valuation and analytics; that one context owns listing truth while the others own only their views; and that the context map's relationships (ACL, conformist, customer–supplier, open host with published language, separate ways, contained big ball of mud) are explicit decisions with organizational and commercial weight. It defines bounded context, context map, core domain and published language for the book.

## Audience

Chief and principal architects and engineering leaders who must draw or review a decomposition for a marketplace or a group of marketplaces, especially one with a legacy monolith and acquired brands. They should leave able to classify subdomains per brand, find language breaks, assign data ownership, draw a context map with named relationships, and spot the god listing table and its cousins.

## Success criteria

- [ ] Defines domain, subdomain (core, supporting, generic), bounded context, ubiquitous language, context map, aggregate and published language, with dated sources (Evans 2003, Vernon 2013, Fowler 2013/2014, DDD Crew).
- [ ] Relates capabilities, subdomains, contexts, services and teams in a table and states the ownership rule (one context, one team).
- [ ] Includes a per-brand subdomain classification table that differs by vertical.
- [ ] Shows the listing's meaning across at least eight contexts using the Lyon apartment, consistent with the ledger and [[entity-resolution]] (prices €389,000, €389,000, €395,000; Rhône Habitat via Keybridge).
- [ ] Presents the Veldmark Common Ground context map as a diagram, and justifies each relationship, including Keybridge as separate ways and Yardstick Relay as an ACL, consistent with [[event-driven-listings]].
- [ ] Covers aggregates and transactional boundaries with a worked bump example, and the listing event as published language with the Ghost Inventory bike.
- [ ] Cites dated public evidence (Vinted 2026 and 2024, AutoScout24 2016/2018, Kleinanzeigen 2025, Adevinta 2023) and labels inferences.
- [ ] Includes trade-off tables, vertical differences, failure modes, the Chief Architect's view and questions.

## Non-goals

- The listing aggregate's internal design and lifecycle — owned by [[listing-aggregate]].
- The event envelope, catalog, schema evolution and replay — owned by [[event-driven-listings]].
- Matching and canonical entities — owned by [[entity-resolution]].
- System of record versus read models and erasure — owned by [[listing-data-management]].
- Team topology and governance — owned by [[organizing-marketplace-engineering]]; tenancy — owned by [[multi-country-platforms]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Evans's and Vernon's books were not re-read in this session; the core/supporting/generic attribution follows standard practice and should be checked against the texts before print.
- Should the toolkit include a context-map template with the relationship legend from this chapter?
- The 19-context count for Common Ground is new in this chapter; later chapters (multi-country-platforms, organizing-marketplace-engineering) should reuse it or reconcile.

## Decision log

- **2026-10-19** — Organized the chapter around "where the meaning of listing changes" rather than around a generic DDD tutorial, because the overloaded noun is what makes marketplaces a clear case.
- **2026-10-19** — Classified subdomains per brand rather than once for the group, to show that trust is core at Tradeyard and supporting at Motorvane.
- **2026-10-19** — Modeled Keybridge as "separate ways" with a public feed contract, so that the March 2027 neutrality decision appears as an enforced context-map relationship, matching [[event-driven-listings]].
- **2026-10-19** — Kept event-contract details brief and linked to [[event-driven-listings]] to avoid re-teaching; reused its identifiers (Yardstick Relay, listing ID format, twelve event types).

## Sources

- **Internal**
  - [[business-capabilities]] — the capability map and heat-map verdicts used as input.
  - [[listing-aggregate]], [[event-driven-listings]], [[entity-resolution]], [[trust-and-safety-architecture]] — neighbouring designs this chapter must agree with.
  - `_research/productscape-digest.md`, `_research/brief-platform-data-ml.md`, `_research/brief-adevinta.md`, `_research/scenario-ledger.md`.
- **External**
  - Evans, *Domain-Driven Design* (2003); Vernon, *Implementing Domain-Driven Design* (2013).
  - Fowler, "BoundedContext" (2014) and "DDD_Aggregate" (2013); DDD Crew, Context Mapping.
  - Vinted Engineering (2024, 2026); AutoScout24 Tech Blog (2018); InfoQ (2016); Adevinta Tech Blog (2023, 2025).

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: Kleinanzeigen Debezium quote corrected to the source wording; Vinted domain claims spot-checked; IDs and Lyon prices checked against ch. 15 and ch. 33. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
