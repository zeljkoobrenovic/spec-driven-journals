---
status: accepted
revised: 2026-10-20
---

# Spec: Many Doors In: Forms, APIs and Bulk Feeds

## Intent

Show architects that listing ingestion is a boundary capability with its own contracts, not a set of importers. Supply enters through four kinds of channel (insertion flow, partner API, bulk feed, replication from an external system of record). Each should end in the same idempotent, validated command on the listing service, keyed by the partner's own reference. The chapter owns **ingestion channel**, **feed contract** and **delta feed**. It argues that most ingestion incidents (truncated snapshots deleting stock, lost deletes leaving ghosts, the same stock arriving twice) come from contract questions nobody asked: what absence means, who owns each field, how fast removals must arrive and how both sides reconcile. After reading it, a Chief Architect should know what to standardize across brands (the contract, error catalog, validator and guards) and what to keep local (the adapters for each partner ecosystem).

## Audience

Chief and enterprise architects, principal engineers and engineering leads responsible for supply, partner integrations and pro-seller platforms in classifieds, real-estate and automotive marketplaces. They know APIs, queues and batch processing; they need the marketplace-specific shape of partner ingestion and the evidence from public contracts.

## Success criteria

- [ ] Reader can name the four channel types and, for each, say where the truth about a listing lives (channel table).
- [ ] Reader can explain full-snapshot versus delta semantics, why neither is sufficient alone, and the incremental-plus-reconciliation pattern, with Rightmove RTDF and RESO as dated evidence.
- [ ] Reader can list the clauses of a feed contract beyond schema (identity, semantics, field ownership, timeliness, media, errors, limits, reconciliation, change management).
- [ ] Reader can draw the "many doors, one write path" architecture and state each component's responsibility and what it must not do (Figure 2 and table).
- [ ] Reader can distinguish external key, request idempotency key and record sequence, and explain why the key mapping must survive removals.
- [ ] Reader can design a mass-change guard and scheduled reconciliation, and explain the Motorvane 8 March 2027 incident and the Essen Golf's 26-hour removal lag in those terms.
- [ ] Reader can compare transport, semantics, acceptance, media, authentication, standards and group-ownership options (trade-off table) and the vertical differences.
- [ ] Every company claim carries a dated source; no proprietary internals are invented.

## Non-goals

- The listing aggregate's identity, invariants and lifecycle: owned by [[listing-aggregate]].
- Attribute dictionaries and compiled category schemas: owned by [[attribute-schemas]].
- Value normalization, enrichment and attribute provenance: owned by [[normalization-and-enrichment]].
- Cross-seller duplicates and canonical entities: owned by [[entity-resolution]] (only same-seller, cross-channel merges are covered here).
- Freshness SLAs end to end and unpublish propagation: owned by [[publication-pipeline]].
- Dealer and agent products built on the channels: owned by [[professional-seller-tooling]]. Media processing: [[media-pipeline]]. Outbound syndication: [[event-driven-listings]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- mobile.de's full-versus-delta semantics for its XML upload are documented on a page the research did not fetch; the chapter does not state them.
- The French agency-software export landscape (*passerelles*) is described only as industry practice; no current vendor or format facts were verified.
- The DSA Article 30 wording was read at summary level; check the article text on EUR-Lex before print.
- Kleinanzeigen's photo-to-listing evidence is trade press, not a company engineering source.

## Decision log

- **2026-10-19** — Organized the chapter around "where the truth lives" per channel rather than around transports, because the system-of-record question is what separates a UX problem (insertion flow) from a reconciliation problem (feeds).
- **2026-10-19** — Used publicly documented partner contracts (Rightmove RTDF, mobile.de Seller-API, Autotrader, OpenImmo, RESO, eBay Feed API) as the evidence base, since marketplaces rarely publish their internal pipelines; inferences about internals were avoided.
- **2026-10-19** — Opened with a fictional truncated-snapshot incident (Motorvane, 8 March 2027) and explained the ledger's 26-hour Golf removal as a contract consequence (daily snapshot equals a 24-hour removal SLA), resolved by a hybrid snapshot-plus-status-delta contract.
- **2026-10-19** — Recommended a shared group contract (Supply Contract v1) with local adapters instead of a single group ingestion platform, consistent with "share platforms, not products" and the different partner ecosystems per brand. Treated Keybridge neutrality as an ingestion-contract requirement.

## Sources

- **Internal**
  - `_research/brief-listing-data-ingestion.md` Part 6 — feed specifications, idempotency, error formats, partner pipeline inference.
  - `_research/brief-real-estate-portals.md` Parts B.2 and C — Rightmove RTDF, RESO, OpenImmo, NAR listing options.
  - `_research/brief-automotive.md` Part A — mobile.de Seller-API, Autotrader developer platform, Bundeskartellamt 2026, dealer-feed inference.
  - `_research/productscape-digest.md` — integration-partner KPIs and seller-journey pains.
  - [[listing-aggregate]], [[attribute-schemas]], [[entity-resolution]] — terminology and ownership boundaries.
- **External**
  - Rightmove, *Real Time Datafeed Specification v1.4.1* (2023) — the most detailed public portal ingestion contract.
  - mobile.de, *Seller-API* and *Upload interface XML* (n.d.) — TSP access model, idempotent create, per-ad serialization.
  - IETF, *RFC 9457* (2023) and *RFC 9700* (2025) — error envelope and OAuth best practice.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: labeled the Golf's 23 leads as raw (19 deduplicated), expanded PKCE and DVLA, American spelling, timetoread corrected. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 1 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,806 → 6,826 words; outline unchanged; opening now places the chapter as the first link of Part III's supply chain; Vertical Differences paragraph split in three; topic sentences brought forward in six paragraphs. *(AI-mediated session)*
- **2026-10-20** — Replaced 2 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`). *(AI-mediated session)*
