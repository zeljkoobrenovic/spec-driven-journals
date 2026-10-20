---
status: accepted
revised: 2026-10-20
---

# Spec: From Submitted to Searchable: The Publication Pipeline

## Intent

Show architects how to design the path between "publish" and "findable" and back again. The chapter splits the pipeline into a short synchronous decision path and an event-driven propagation path, defines a freshness SLA as a contract (coverage, clock, removal), budgets the 90-second target stage by stage, and makes unpublish propagation reliable through a consumer registry, version-gated consumers, tombstones, send-time re-checks and a propagation monitor. After reading, the reader can write a pipeline SLA card and find where a slow or ghost listing comes from.

## Audience

Chief and principal architects, platform and search leads, and engineering directors of classifieds, automotive and real-estate marketplaces who own (or inherit) publication latency targets, moderation integration or Ghost Inventory complaints.

## Success criteria

- [ ] Reader can list the eight pipeline stages and say which belong on the synchronous path and why.
- [ ] Reader can explain platform latency vs source latency and why a freshness SLA must state coverage (including the human-review path).
- [ ] Reader can explain risk-tiered pre/post-moderation as a pipeline-shape decision, with the leboncoin 2015 and Which? 2024 lessons.
- [ ] Reader can explain version-gated apply, tombstones and the zombie-listing failure.
- [ ] Reader can design unpublish propagation with a consumer registry, send-time re-checks and a propagation monitor; takedowns on the same rails.
- [ ] Worked example: Tradeyard's 6-minute baseline decomposed and the 90-second budget allocated; Femke's bike timings match the ledger and neighboring chapters (19:42 submit, 19:44 cleared, 19:48 searchable, 18:10 sold, 18:11 removed, 214 Tuesday digests).
- [ ] Includes three mermaid diagrams, a trade-off table, a vertical SLA table, observability instruments, Chief Architect's view, questions, dated sources.

## Non-goals

- Lifecycle states and durations ([[listing-aggregate]]).
- Moderation policy, decision service and enforcement ladder ([[trust-and-safety-architecture]]).
- Event contract, outbox and schema evolution ([[event-driven-listings]]).
- Index design and engine choice ([[search-architecture]]); alert matching and fan-out ([[saved-searches-and-alerts]]).
- Feed reconciliation and source-latency fixes ([[listing-ingestion]]); gone-page HTTP policy ([[web-and-seo-architecture]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- The baseline stage breakdown is illustrative; if a later chapter needs exact Yardstick figures, add them to the ledger.
- Whether Motorvane and Hearthly SLA values should become canonical numbers (left qualitative here).
- No classifieds operator documents its full publication pipeline; replace the reference design if one appears.

## Decision log

- **2026-10-19** — Framed publication as "decide, then propagate" rather than as a linear stage list, because the sync/async split explains most latency and failure.
- **2026-10-19** — Defined the 90-second target as covering gate-cleared listings only, with a separate review-path objective and the held share published, to stop the metric being gamed or dominated by the review queue (recorded in the ledger).
- **2026-10-19** — Made takedowns ride the same removal path on a priority lane, consistent with [[trust-and-safety-architecture]] and [[event-driven-listings]]; rejected a separate takedown mechanism.
- **2026-10-19** — Reused the index budget (15 s), removal targets (10 s search, 2 min consumers, 15 min partner feeds) from neighboring chapters instead of inventing new ones.

## Sources

- **Internal**
  - Scenario ledger — Tradeyard 6-minute p95, 90-second target, 94%/6% moderation split, the Rotterdam bike, Yardstick milestones.
  - [[listing-aggregate]], [[search-architecture]], [[event-driven-listings]], [[trust-and-safety-architecture]], [[listing-ingestion]] — times, budgets and removal objectives kept consistent.
  - Research briefs: platform (Parts 2 and 12), trust (Part 3), data ingestion (Parts 5 and 11), search (2.5, 2.6).
- **External**
  - Vinted Engineering 2021, 2023, 2024 — indexing ordering and freshness improvements.
  - Elastic near-real-time search; Solr 8.11 commit and warming documentation.
  - leboncoin judgment (Clubic, 2015); Which? undercover test (2024).
  - Google Merchant Center expiry; Google job-posting guidance; mobile.de Seller-API.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: digest snapshot source aligned with the ledger, restored [[toolkit]] link, Vinted p99 claim worded as published, American spelling, timetoread corrected. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 3 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
