---
status: accepted
revised: 2026-10-22
---

# Spec: One Stock, Sixty Channels: Listing Syndication to Portals

## Intent

Show how a dealer SaaS platform keeps one dealer's stock correct on dozens of advertising channels whose formats, APIs, identity keys, update and delete semantics, rate limits and regulatory rules all differ, and which also edit, lock, enrich and expire listings on their own. The chapter argues for **desired-state sync keyed by channel listing** over a command queue, treats **withdrawal as a saga** with deadlines and guards, and makes **reconciliation against what each portal actually shows** a standing function. It teaches the reader to run channel adapters as products with contracts, owners and per-channel health metrics. The Axleby thread is Relay and the Zombie Golf (February 2027): a delete stuck behind updates that could never succeed, in a queue keyed by rooftop.

Productscape bricks covered: `advf` (Advertising Feed Syndication: advert API, channel publish queue, advert store with channel mappings and delivery status, channel adapters).

Owns: **channel listing**, **publish queue**, **desired-state sync**, **channel adapter**.

## Audience

Chief and principal architects of dealer-software vendors, integration and platform leads who run portal adapters, and product and engineering directors of dealer groups or portals who want to understand why sold cars stay online and what a syndication engine should promise.

## Success criteria

- [ ] Reader can define channel, channel listing, desired state, actual state, publish queue and channel adapter, and name the three identifiers a channel listing must keep.
- [ ] Reader can explain why command semantics with a queue keyed by rooftop produced the Zombie Golf, and how desired state keyed by channel listing, coalescing and priority lanes prevent it.
- [ ] Reader can classify adapter errors into transient, throttled, permanent and locked, and say what the scheduler does with each.
- [ ] Reader can design a withdrawal saga per channel, including portal deal locks, a deadline alarm and a mass-withdrawal guard.
- [ ] Reader can describe a reconciler: its observers (push plus pull), its drift classes and the field-ownership rules it depends on.
- [ ] Every portal contract detail is cited to dated public documentation (mobile.de, AutoScout24, Auto Trader, Marktplaats, Google, Meta); Axleby numbers match the ledger; assumptions are labeled.
- [ ] The Across Markets table distinguishes REST publisher APIs (NL/BE, DE, UK) from US file feeds, and names market rule sets (Car-Pass, Pkw-EnVKV/WLTP, UK lifecycle and deal locks).

## Non-goals

- Advert content, media pipeline, mandatory disclosures and listing quality scores ([[merchandising]]).
- The stock lifecycle and the dossier as system of record ([[inventory-and-vehicle-dossier]]).
- Lead capture, routing and attribution ([[leads-and-crm]]).
- DMS integration patterns and DMS outages ([[dms-integration]]).
- Event backbone, outbox and webhook contracts for external clients ([[events-webhooks-and-sync]]).
- The portal side of ingestion and ranking (LISTED).
- The full end-to-end journey with all failure cases ([[journey-inventory-to-portal]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- US portal feed specifications (Cars.com, CarGurus, Autotrader.com) are not public; the US column rests on secondary sources and a 10-K.
- mobile.de and AutoScout24 publish no numeric rate limits; budgets in the chapter are behavioral, not numeric.
- Whether Kleinanzeigen accepts dealer listings by its own API or only via mobile.de was not verified.

## Decision log

- **2026-10-22** — Built the Zombie Golf mechanism from two faults (a DriveDesk sold row unmatched after a rooftop transfer, as fixed in the dms-integration ledger line, and a requeue loop on unmapped equipment codes in a queue keyed by rooftop and channel) so that the ledger's "deletes queued behind failed updates" has a concrete, teachable cause; RabbitMQ's documented requeue behavior anchors it.
- **2026-10-22** — Framed the core choice as command versus desired-state semantics, with BOOKED's channel managers as the mirror image, rather than as "queue technology"; the key, not the broker, is the lesson.
- **2026-10-22** — Kept the four-portal contract comparison (create idempotency, update semantics, withdrawal, observers) inside the architecture section instead of a separate portal catalog, to stay under the length cap and avoid re-teaching LISTED.
- **2026-10-22** — Treated US syndication as a separate product line (file feeds with little read-back) rather than a market adapter.

## Sources

- **Internal**
  - [[meet-axleby]] — Relay, the Zombie Golf, volumes and prices.
  - [[connectivity-and-channel-managers]] — BOOKED's channel-manager parallel.
  - `_research/brief-syndication-leads.md`, `_research/brief-platform-apis-operations.md`, LISTED `brief-automotive.md`.
- **External**
  - mobile.de Seller API and Ad Stream documentation (n.d., accessed 2026-10).
  - AutoScout24 Listing Creation API documentation and changelog (to 2026-10-19).
  - Autotrader Connect documentation (2024–26) and Auto Trader FY26 results (2026).
  - Marktplaats API documentation (2019, © 2023).
  - Google vehicle ads and Vehicle Listings documentation; Meta automotive catalog reference.
  - Bundeskartellamt mobile.de/Carwow clearance (2026); Emerce on AutoTrack and Gaspedaal (2025).
  - RabbitMQ consumer acknowledgements documentation; Amazon Builders' Library on retries (2019); CarGurus Revved on rate limits (2023).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: publish rules no longer treat advertised as a lifecycle state; American spelling; Bundeskartellamt date verified. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: American spelling (labeling). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
