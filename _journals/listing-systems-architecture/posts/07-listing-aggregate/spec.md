---
status: accepted
revised: 2026-10-20
---

# Spec: The Listing Aggregate: Identity, Lifecycle and Invariants

## Intent

Give the reader a precise, defensible model of the listing as a domain-driven-design aggregate: what is inside it and what it only references, how it is identified, which rules always hold, how its lifecycle works and how every change leaves it as a versioned event. The chapter must turn "the ads table" into a designed object with one owner, so that later chapters (publication pipeline, search, alerts, trust, monetization, data management) can build on stable states and events. The reader should leave able to write a lifecycle specification and an event contract for their own marketplace and to explain why ghost inventory is an event-consumption problem, not a search problem.

## Audience

Chief and principal architects, staff engineers and engineering leaders who own or depend on a listing service in a classifieds, real-estate, automotive or jobs marketplace. They know DDD vocabulary loosely and event-driven systems well; they need the marketplace-specific choices (seller vs platform vs enforcement states, renewal vs creation, outcomes, units, regulated price history) made explicit.

## Success criteria

- [ ] Reader can distinguish listing, underlying entity, product, placement and case, and decide what lives inside the aggregate.
- [ ] Reader can explain the identity scheme (internal ID, public ID, external key, entity reference) and the relisting rules.
- [ ] Reader can separate invariants enforced in the aggregate from policies enforced asynchronously, with state-dependent validation.
- [ ] Reader can draw the publication lifecycle with an orthogonal enforcement overlay and derive visibility, contactability and URL behavior from it.
- [ ] Reader can explain why bumps and renewals move a ranking timestamp, not `created_at`, citing documented API evidence.
- [ ] Reader can choose a history storage approach (state + history + outbox, event sourcing, CDC) and justify it.
- [ ] Reader can specify per-consumer removal deadlines and the re-check-at-send rule, using the Rotterdam bike replay.
- [ ] Reader will not mistake the chapter's reference architecture for any named company's internals.

## Non-goals

- Feed mechanics, reconciliation and idempotency at the boundary — [[listing-ingestion]].
- Freshness SLAs, expiry jobs and unpublish propagation end to end — [[publication-pipeline]].
- Outbox, schema registry and event governance mechanics — [[event-driven-listings]].
- Category trees, attribute schemas, media, location and seller accounts — their Part II chapters.
- Moderation decisions, statements of reasons and appeals — [[trust-and-safety-architecture]], [[marketplace-regulation]].
- Erasure across copies and read-model consistency — [[listing-data-management]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The Omnibus prior-price rule (lowest price in at least 30 days) is stated from the directive's Article 6a; the official EUR-Lex text could not be fetched in the writing session. Verify the wording before print.
- Should the toolkit's "listing lifecycle state table" template be derived directly from the visibility table in this chapter?
- No classifieds operator has published its lifecycle or event model; revisit if one does.

## Decision log

- **2026-10-19** — Modeled the lifecycle as a publication state plus an enforcement overlay rather than one status enum, because DSA treats demotion as a restriction and because seller commands must never undo enforcement. Rejected a three-field model with a separate clock dimension as over-engineered; clock transitions are publication transitions with a distinct trigger.
- **2026-10-19** — Used the canonical Rotterdam bike as the single worked example and added only local details (version numbers, a Safe Deal reservation at 14:02, per the editor's ledger line, the 214 digests, the 41,000-listing audit) that do not contradict the ledger. The phishing episode is shown as an account case that does not touch the listing.
- **2026-10-19** — Kept the event table as the bridge to [[event-driven-listings]] and [[publication-pipeline]], defining event meaning here and mechanics there.
- **2026-10-19** — Included Auto Trader's Deal Builder episode as evidence that transition permissions are business-model decisions; labeled the lesson as interpretation.

## Sources

- **Internal**
  - [[bounded-contexts]], [[meet-veldmark]], [[entity-resolution]], [[publication-pipeline]], [[event-driven-listings]], [[categories-and-taxonomies]] — neighbouring ownership.
  - Research briefs: listing data and ingestion (lifecycle evidence, state-machine inference), platform/data/ML (lifecycle events, outbox, expired pages), real-estate portals (RTDF, DPE), automotive (Deal Builder), trust/regulation (DSA Arts. 17, 20, 30; Omnibus); productscape digest (listing definitions, stream pain points, residuality).
- **External**
  - mobile.de Seller-API; Vinted Help (Bump); eBay Inventory and Taxonomy APIs, PBSE playbook; Rightmove RTDF v1.4.1 (2023); RESO Data Dictionary 2.0 StandardStatus (revised 2023); Auto Trader FY26 results (2026); Google Merchant Center and JobPosting docs; Debezium outbox router; DSA (2022); European Commission, Price Indication Directive page; Service-Public.fr DPE (2026).

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: reservation time aligned to the canonical 14:02, photo count to six (media-pipeline), search removal target to the publication-pipeline SLA card (10 s p95), erasure date clarified, reading time corrected. *(AI-mediated session)*
- **2026-10-19** — Editor: bike version numbers aligned with event-driven-listings (reserved v8, sold v9). *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 1 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,786 → 5,836 words; outline unchanged; lead now names what the chapter builds on and which chapters use its states and events; Auto Trader paragraph leads with its lesson; trade-offs count corrected to four; publication-state/overlay split explained in one sentence; no spec criteria changed. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: heading, third key point and excerpt now say two lifecycle dimensions (publication state plus enforcement overlay, three owners), matching the body, Figure 3 and the glossary; unsourced "among the most effective notifications" claim about price-drop alerts reduced to the plain fact. *(AI-mediated session)*
- **2026-10-20** — Replaced 2 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`); known differences from the source: Figure 4: kept attempt 1: prints 'START' and 'END' beside the dots; 'seller resumes' arrow points from Paused to Rejected instead of Active. *(AI-mediated session)*
