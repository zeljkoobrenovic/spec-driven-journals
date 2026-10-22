---
status: accepted
revised: 2026-10-22
---

# Spec: Streams of Nights: Event-Driven Architecture for Stays

## Intent

Show chief architects which events drive a stays platform and how to design them by the **cost of losing one**. The chapter separates the high-volume, supersedable ARI stream (keyed by property or listing, kept close to its read models) from the low-volume, ledger-grade streams (reservation events, the payment state feed, delivery events) that money, partners, tax and guest communication depend on. It argues for publishing reservations as **versioned full-state contracts** through a **transactional outbox** (or log-based CDC with a translator for legacy systems), for idempotent consumers that track applied versions, for **state plus events** rather than event sourcing for reservations, and for governing published events as contracts: owner, schema compatibility, personal-data class, retention, replay rules and an independent completeness check. The reader leaves able to review an event design for a stays platform and to decide what a multi-brand group should share.

Productscape domains covered: TAM event-feed workers across bricks (notably the Reservation Event Feed in `book` and `invt`, the Payment State Feed in `paym`, the Partner Integration Event Feed in `conn`, the Inventory Update Feed in `srch`); HSM APIs (`apix`, `book`, `cala`), which the hosted-stays model lists without event feeds.

Owns: **reservation event**, **ARI stream**, **outbox (stays)**.

## Audience

Chief and enterprise architects of travel groups, platform-engineering and data-platform leads, principal engineers on booking, payments and connectivity, and engineering directors planning a monolith-to-services migration. They know Kafka and publish-subscribe messaging; they need the stays-specific design: which streams matter, what guarantees each needs, and how to prove nothing was lost.

## Success criteria

- [ ] Reader can list the main event streams of a stays platform with source, volume shape and cost of losing one event, and explain the roughly thousand-to-one gap between ARI and reservation events using Corvane's ledger numbers.
- [ ] Reader can distinguish event notification, event-carried state transfer, event sourcing and CQRS (Fowler, 2017) and say when a thin notification is right (partners outside the trust boundary) and when it is wrong.
- [ ] Reader can sketch a two-tier topology (brand buses plus a contract-only group backbone) with components, responsibilities and "must not" rules.
- [ ] Reader can specify a reservation event contract (envelope, version, change, stay, commercials, payment arrangement, references) and defend full state, one event type and references instead of personal data.
- [ ] Reader can explain the outbox, log-based relay, ordering by key and the idempotent consumer, and when CDC with a translator replaces an outbox.
- [ ] Reader can state ARI stream rules: key by property, absolute values, emit only real changes, supersession rules, poison-message quarantine and end-to-end lag.
- [ ] The Corvane worked example (Fathom shadow run July–August 2027: 2,870 reservations, €412,000; second run 14; bootstrap backfill) is consistent with the ledger, and the "Hotels and Homes" section has a specific table and a share/not-share judgement.
- [ ] Every company claim carries a dated source; the reference architecture for large OTAs is labeled as inference.

## Non-goals

- The reservation state machine, delivery acknowledgement and no-shows: [[reservation-lifecycle]] and [[connectivity-and-channel-managers]].
- The booking saga and idempotency keys on the booking path: [[checkout-orchestration]].
- The payment state feed's event list and payment plans: [[stay-payments]]; ledger posting design: [[payouts-and-settlement]] and RECONCILED's [[payments-to-ledger]].
- Availability caches and search projectors in depth: [[availability-engine]] and [[stays-search-architecture]].
- Behavioral tracking, warehouses and governed metrics: [[marketplace-intelligence]].
- Multi-region replication, peaks and degradation: [[global-scale-and-reliability]].
- Kafka, Pub/Sub or broker internals.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Should place-registry, trust-decision and identity events join the group backbone in 2028 as stated, and does that change the cross-chapter story in [[stays-trust-and-safety]] and [[identity-accounts-and-access]]?
- Exact archive retention for reservation and payment events (finance, tax and dispute periods) is left to [[stays-regulation]] and [[refunds-and-reconciliation]] to pin down.
- [[modernizing-a-live-marketplace]] should reuse the Keystone CDC translator as its migration-seam example rather than invent another.

## Decision log

- **2026-10-21** — Built the Corvane thread around the Fathom shadow run (a ledger consumer exposing lost, raced and duplicated events) rather than an ARI incident, because ARI ordering and full-sync problems are already worked in [[connectivity-and-channel-managers]] and [[availability-engine]]; the ARI stream gets its own design-rules section instead.
- **2026-10-21** — Recommended versioned state plus outbox events for reservations, not event sourcing; kept event sourcing for the ledger. Rejected a "one shared bus for everything" topology in favor of brand buses plus a contract-only backbone, given three clouds and the volume gap.
- **2026-10-21** — Chose one `reservation.versioned` event type carrying full state, aligned with the payment feed's `plan.versioned` naming in [[stay-payments]], over a family of fine-grained event types.
- **2026-10-21** — Kept Corvane Connect off the backbone for ARI to respect the May 2027 neutrality rule.

## Sources

- **Internal**
  - [[connectivity-and-channel-managers]] — Switchyard ordered lanes per property, delivery outbox, full-sync diffing.
  - [[rates-and-availability-model]], [[availability-engine]], [[stays-search-architecture]] — ARI provenance, 13-month retention, Pricegrid lag, projector flip rate.
  - [[calendar-sync]] — calendar claims with provenance.
  - [[stay-payments]], [[payouts-and-settlement]], [[merchant-and-agency-models]] — payment state feed, Fathom as settlement ledger of record, the `PAYMENT_TYPE` audit.
  - `_research/brief-platform-data-ml.md`, `brief-supply-connectivity.md`, `brief-booking-reservations.md`, `brief-payments-finance-tax.md`, `productscape-digest.md`, `scenario-ledger.md`.
- **External**
  - Airbnb Engineering, SpinalTap (2018), payment orchestration (2022), Riverbed via InfoQ (2023) — CDC, idempotent processing, materialized views.
  - Agoda Engineering (2023, 2024, 2025, 2026) — Kafka volume, two-step logging, active-passive consumers, price-update bursts.
  - Booking.com Engineering (2026) and Developers (n.d.) — consumer capacity tests, acknowledge-until-received reservations, notification service.
  - Expedia Group Technology (2023) — event stream as source of truth for reviews.
  - Martin Fowler (2017), Chris Richardson (microservices.io), Debezium, CloudEvents, Confluent, Google Pub/Sub documentation — patterns and mechanics.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: American spelling fix; added the closing Corvane-is-fictional line to Sources. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 6,938 → 6,619 prose words; no headings renamed; Failure Modes and Chief Architect's view trimmed of repeats (poisoned partition kept, personal-data-in-archive bullet, 'keep the firehose local' and 'plan the long memory' paragraphs cut); duplicate closing line in Sources removed. *(AI-mediated session)*
