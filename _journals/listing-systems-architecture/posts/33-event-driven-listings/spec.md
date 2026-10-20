---
status: accepted
revised: 2026-10-20
---

# Spec: Every Change Is an Event: Event-Driven Listing Architecture

## Intent

Give architects of listing marketplaces a complete, defensible design for how listing changes travel from the system of record to search, alerts, trust and safety, SEO, analytics and partners. The chapter makes the **listing event** a published contract with one owner, shows how to publish it reliably (transactional outbox, or change data capture behind a translator during migration), how consumers stay correct under redelivery, reordering and replay (version-gated apply, per-listing keys, state-carrying events), and how the schema evolves for years without breaking consumers. After reading, the reader can review a listing event design and say what will go wrong at the Sunday-evening peak, during a backfill or after a schema change.

## Audience

Chief and principal architects, event-platform and search leads in multi-brand marketplace groups who already know Kafka and microservices but have not designed a cross-brand listing event contract. They should leave with an envelope, an event catalog, compatibility rules, replay and dead-letter rules, and governance responsibilities they can adapt.

## Success criteria

- [ ] Reader can distinguish domain events, change events and commands, and explain why CDC is a source but not a contract.
- [ ] Reader can explain the dual-write problem and how the transactional outbox and CDC-plus-translator solve it, with their costs.
- [ ] Reader can design an event envelope with listing ID key, aggregate version, cause and public state, and justify carrying state plus delta.
- [ ] Reader can choose schema compatibility rules and explain why semantic changes need human review.
- [ ] Reader can design replay, backfill and dead-letter handling that cannot resurrect sold listings.
- [ ] The chapter uses documented, dated classifieds evidence (Adevinta, Kleinanzeigen, Vinted, Adevinta Spain, AutoScout24) and labels inferences.
- [ ] The Veldmark Listing event contract v1 example matches the ledger (1 July 2027, Kafka on Confluent Cloud, schema registry; the bike and Golf timings).
- [ ] Includes a trade-off table, a vertical-differences table, failure modes, a Chief Architect's view and design-review questions.

## Non-goals

- Where copies live, consistency models, multi-region and GDPR erasure across copies — [[listing-data-management]].
- Behavioral tracking events, warehouse and data products — [[data-platform]].
- The lifecycle state machine and invariants themselves — [[listing-aggregate]].
- Publication stages and freshness SLAs — [[publication-pipeline]]; feed reconciliation — [[listing-ingestion]].
- Search index design and reindexing mechanics — [[search-architecture]]; alert fan-out — [[saved-searches-and-alerts]].
- The Yardstick strangler plan in full — [[modernization-and-migration]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No classifieds company has published its listing event names or topic layout; revisit if one does.
- Whether the Veldmark envelope should adopt CloudEvents attribute names for partner-facing webhooks (not decided; v1 is internal only).
- Hearthly's Pub/Sub bridge is a stated exception; its review date depends on the post-2028 cloud decision.

## Decision log

- **2026-10-19** — Recommended state-plus-delta events over thin notifications, because peak fan-out and self-healing dominate in listings; notification kept as the right choice only for sensitive or low-fan-out cases.
- **2026-10-19** — Presented CDC and outbox as stages (CDC behind a translator during migration, outbox as target) rather than alternatives, following the platform brief.
- **2026-10-19** — Kept behavioral tracking events off the listing stream and out of scope, to protect removal latency and keep [[data-platform]]'s ownership clean.
- **2026-10-19** — Used the March 2027 bike digest incident as the motivating story and replayed it as v1's acceptance test, rather than inventing a new incident.

## Sources

- **Internal**
  - [[listing-aggregate]], [[publication-pipeline]], [[bounded-contexts]] — lifecycle, stages, published language.
  - [[listing-data-management]] — the next chapter, which inherits the copies this one creates.
  - `_research/brief-platform-data-ml.md` Part 2; `_research/brief-listing-data-ingestion.md` Parts 5–6; `_research/scenario-ledger.md`.
- **External**
  - Debezium, *Outbox Event Router* — outbox columns and keying.
  - Confluent, *Schema Evolution and Compatibility*; *Log compaction* — compatibility modes, tombstones.
  - Martin Fowler, *What do you mean by "Event-Driven"?* (2017) — notification versus state transfer.
  - Adevinta Tech Blog (2022, 2024, 2025) and Vinted Engineering (2019, 2023, 2026) — documented Kafka, CDC, read models and contracts.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: corrected the Kleinanzeigen Debezium quote, fixed a table-row reference, flagged 2022 Adevinta evidence as older, expanded SLO, American spelling. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 2 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,291 → 6,324 prose words; lead now places the chapter as Part VII's first contract; 1 heading renamed ("In Practice: Public Evidence and Contract v1"); 7 paragraph openings brought to their point; 2 paragraphs split; spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: Event catalog count corrected to thirteen types (pause and resume share a table row). *(AI-mediated session)*
- **2026-10-20** — Replaced 2 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`). *(AI-mediated session)*
