{id: loosely-coupled-domains}
# 33. Canonical Events: A Common Language for Money

![Canonical Events: A Common Language for Money — logo](finance-systems-architecture/posts/30-loosely-coupled-domains/assets/images/30-loosely-coupled-domains/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Design a canonical financial event model in depth (envelope, identifiers, money, classification tags, semantic rules and versioning), then the adapter kit, integration hub, schema registry, contract tests and anti-corruption layers that let finance domains change independently without losing reconcilability.

> **WHY FINANCE CARES:** The close runs on a fixed calendar, and every interface that changes inside that calendar is a risk to it. A controller needs brand releases and vendor upgrades to stop surprising the ledger, and needs proof that every financial fact a brand produced reached the books exactly once.

> **WHY ARCHITECTS SHOULD CARE:** A finance estate has three clocks that do not agree: product releases weekly or daily, vendor upgrades quarterly or twice a year, the close monthly. Coupling between them makes every team wait for the slowest. A published language of financial facts is the cheapest way to decouple them, and a canonical model that tries to be more than that is one of the most expensive ways to fail.

> **KEY POINTS:**
>
> * **Publish facts, not accounting.** A canonical financial event states what happened in business terms, with identifiers, money in minor units, and explicit entity, brand and business-model tags. It never carries a GL account, a debit or a vendor document type; the accounting engine derives those. That one rule is what lets brands, ledgers and ERPs change independently.
> * **Keep the canonical model narrow and governed.** Model only the facts the ledger, reconciliation or a regulator needs, about eighteen event types at Northmere, and give the model an owner, a change board, a schema registry and consumer-driven contract tests. The "enterprise canonical model" of everything fails by becoming the lowest common denominator and a central bottleneck.
> * **Smart edges, a counting hub, translation at vendor boundaries.** Adapters validate and map at the producer; the hub validates, enriches with reference keys, counts, routes and replays, but holds no business rules; anti-corruption layers stop every vendor's model and version changes at the boundary. Breaking changes run in parallel through at least one quarter close.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-finance-architecture-goes-wrong):**
>
> * **Point-to-Point Spaghetti** — 1,100 interfaces on three integration technologies, each with its own format and error handling, are replaced as they are touched by one published language of financial facts.
> * **The Permanent Exception** — the adapter kit turns "our booking model is different" into a mapping inside the brand's adapter, not a fork of the finance core.
> * **The Borrowed Roadmap** — anti-corruption layers keep S/4HANA, Fusion, Workday, Adyen and Stripe concepts out of the event model, so a vendor's release or replacement changes one adapter, not the estate.

Every finance estate has a canonical model, whether anyone designed it or not. In most enterprises it is the general ledger's journal format, reached through a few hundred translations written by different teams in different decades. That model is **implicit, owned by nobody and versioned by accident**, so each brand release and each vendor upgrade becomes a negotiation with every downstream system.

The opposite failure is just as common. An integration team, tired of the spaghetti, sets out to define one enterprise data model of customers, products, orders, payments and ledgers, and spends two years in schema committees while the brands keep building point-to-point feeds. The model that survives is the one nobody needs to agree on.

This chapter argues for a middle path that is specific to finance: **a narrow, explicit and versioned language of financial facts**, published by the domains that own those facts, translated at vendor boundaries and governed as rigorously as a chart of accounts. [Files, Events and APIs: How Finance Systems Talk](#integration-architecture) introduced the integration styles, idempotency, the outbox and the first sketch of canonical events; this chapter owns their design and governance.

{id: loosely-coupled-domains--setting-the-scene-a-field-that-changed-its-meaning}
## Setting the Scene: A Field That Changed Its Meaning

Northmere, the fictional group this book follows, closed April 2027 half a day late because a boolean changed its meaning.

On Tuesday 4 May 2027, working day 2 of the April close, Stayloft's booking team released a change to an internal `booking_updated` message. Partial cancellations, a new product feature, now set `cancelled: true` and carried a new `cancellation_scope` field. The change was correct by every rule the booking team had: tests passed, the message's own consumers in the booking domain were updated, and the release went out with about forty others that week. The Stayloft Finance Platform (SFP), Northmere's custom finance platform for Stayloft, also read that message, through a consumer written in 2019 that nobody on the booking team knew existed. SFP's merchant subledger treated 2,180 partially canceled bookings as fully canceled and released **€1.3 million** of traveler funds held. No money left the group, because Northmere Pay executes refunds from its own records, but the subledger was wrong. BlackLine's tie-out of traveler funds against the safeguarding calculation caught it on working day 4, and Jonas Berg's team posted reversals.

Nobody had made a mistake by their own rules. The failure was the coupling: a product team's release cadence and finance's close calendar were joined by a message that had no contract, no owner on the finance side and no version. Lucía Romero, Dana Whitlock's lead enterprise architect for integration, counted how many similar joins the estate had. Of about **1,100 interfaces** in the finance inventory, she could identify the owning team on both sides for fewer than half; about 240 were flat files and about 70 had a spreadsheet in the loop. They ran on three integration technologies: SAP Integration Suite for SAP-centric flows, Kafka as the event backbone owned by Platform Engineering, and MuleSoft for flows inherited with Wayfare and Tablekin.

Dana put one question to Lucía, and it is the question of this chapter: **what integration architecture lets Stayloft release forty times a week, Wayfare take Oracle's quarterly update, and Leila Haddad close in five days, without any of them needing the others' permission, and with proof that nothing was lost between them?** Lucía's answer became Keystone's canonical financial events v1, the brand adapter kit and the integration hub, approved by the Keystone design authority in June 2027.

{id: loosely-coupled-domains--why-loose-coupling-matters-more-in-finance}
## Why Loose Coupling Matters More in Finance

Loose coupling is a general virtue. In finance it is a control requirement, because finance systems are governed by **three clocks that cannot be synchronized**.

| Clock | Who sets it | Typical cadence at Northmere (2027) | What breaks when it is coupled to the others |
| --- | --- | --- | --- |
| **Product release** | Brand engineering teams | SFP about 40 deploys a week; booking platforms daily | Every release becomes a finance change; finance asks for release freezes; brands route around finance |
| **Vendor release** | SAP, Oracle, Workday, Stripe, Adyen | Oracle Fusion quarterly (Wayfare in update cohort B, about 14 working days of regression each); Workday twice a year; Stripe monthly non-breaking and twice-yearly breaking API versions; S/4HANA upgrades took 7 months | Each upgrade ripples into brand code; upgrades get deferred until they become projects; **Customization Concrete** sets in |
| **Close** | Leila Haddad, Chief Accounting Officer | Monthly, 9 working days, target 5 by end of 2028 | Interfaces that change inside the close window put the close at risk; closed periods cannot absorb a changed interpretation |

The close clock is the one that does not bend. A closed period is locked, and anything learned later is corrected in an open one (see [Never Update, Only Append: Designing Custom Ledgers](#designing-financial-ledgers)). An integration that changes meaning on working day 2 produces a wrong number in a period about to be certified. A finance integration architecture therefore has to deliver two properties that are usually traded against each other:

- **Independence.** A producer can release, a vendor can upgrade and a ledger can be replaced without coordinated change elsewhere.
- **Reconcilability.** At every boundary, someone can prove that what was sent was received, completely and once, and that it means the same thing on both sides.

The coupling taxonomy (temporal, data, semantic, deployment, vendor) belongs to [Duplicates and Dependencies: The Hidden Costs of a Grown Estate](#redundancy-and-coupling). The design consequence for this chapter is that **semantic coupling is the expensive one in finance**. Temporal coupling is solved with queues and deployment coupling with contracts; semantic coupling, two systems reading the same field differently, is solved only by a governed language. The `cancelled` flag was a semantic coupling.

![Three clocks running at different speeds, each connected loosely to a shared stream of event cards rather than geared to each other.](finance-systems-architecture/posts/30-loosely-coupled-domains/assets/images/30-loosely-coupled-domains/three-clocks.jpeg)

**Figure 1:** *Finance runs on three clocks that cannot be synchronized, product releases, vendor releases and the close, so the integration must let each turn without dragging the others.*

{id: loosely-coupled-domains--concepts-published-language-facts-and-translations}
## Concepts: Published Language, Facts and Translations

[Map What Finance Does Before What Runs It](#capability-mapping) decomposed Northmere's finance domain into bounded contexts and defined the relationship patterns from Eric Evans's domain-driven design ([DDD Reference, 2015](https://www.domainlanguage.com/ddd/reference/)). Three carry this chapter: the canonical events are Northmere's **published language**; every vendor boundary gets an **anti-corruption layer (ACL)**, a translation layer that keeps the vendor's model out of models Northmere owns; and the hub's intake is an **open host service** that any producer can use without negotiating a bespoke interface.

Gregor Hohpe and Bobby Woolf's *Enterprise Integration Patterns* names the underlying idea **Canonical Data Model**: design a data model "independent from any specific application" and require each application to produce and consume messages in it ([EIP, Canonical Data Model](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html)). Their illustration makes the economics plain: six applications need 30 direct translators but only 12 with a canonical model. The arithmetic is why canonical models are attractive; what follows is about why most of them fail and how to keep one from failing.

Three more definitions, each one clause:

- A **canonical financial event** is an immutable, versioned record of one business fact with financial consequences, expressed in the published language and owned by the domain where the fact originates.
- A **brand adapter kit** is the set of libraries, mappings, tests and guides a producing team uses to publish canonical events correctly without designing its own integration.
- An **integration hub** is the governed transport and control layer between producers and finance consumers: it validates, enriches with reference keys, counts, routes, quarantines and replays.

Martin Fowler distinguishes **event notification**, where an event says that something changed and consumers call back for details, from **event-carried state transfer**, where the event carries the data consumers need ([Fowler, 2017](https://martinfowler.com/articles/201701-event-driven.html)). Canonical financial events are deliberately the second kind. A ledger may replay an event years later, when the service that could answer a callback has been retired; an event that the accounting engine cannot interpret on its own is not a financial record.

{id: loosely-coupled-domains--the-canonical-financial-event-model}
## The Canonical Financial Event Model

{id: loosely-coupled-domains--the-envelope}
### The envelope

Every Keystone event shares one envelope. The envelope is what the hub, the schema registry, the delivery ledger and every consumer can rely on without knowing the event type; the `payload` is type-specific.

| Field | Type and rule | Why finance needs it |
| --- | --- | --- |
| `event_id` | UUID, assigned by the producer when the fact is recorded; **identical on every retry** | Transport deduplication; the key every downstream record points back to |
| `event_type` | One of the registered names, past tense (`PaymentSettled`) | Routing; selection of the posting rule |
| `event_version` | Integer major version of that type's schema | Consumers select the right reader; posting rules are bound to versions |
| `occurred_at` | Timestamp with offset: when the business fact happened | Period assignment, revenue timing, cut-off |
| `recorded_at` | Timestamp: when the producer recorded it | Lateness measurement; producer health |
| `brand` | Code from the group brand list (`STL`, `WAY`, `TBK`, `ADS`, `PAY`, `CORP`) | Segment reporting; derivation of profit center |
| `legal_entity` | Identifier from the legal entity register | The entity whose books the fact affects; never inferred from brand |
| `business_model` | Code from the business-model list (agency, merchant, subscription, usage, payments facilitation, advertising, other) | Selects the accounting pattern; Stayloft runs agency and merchant side by side |
| `source_system` | Registered producer identifier | Control totals per source; ownership of errors |
| `correlation_id` | Business key that ties events of one business object together, for example the booking ID | Drill-back from a ledger line to every event of the booking |
| `amount` | Object: integer `value_minor` plus ISO 4217 `currency` | The headline value of the fact; never floating point |
| `counterparty_id` | Group partner ID of the other party (property, venue, PSP, advertiser) | Partner balances, payouts, tax and intercompany |
| `tax_jurisdiction` | ISO country or subdivision of the underlying supply | Tax determination and reporting; inherited from the booking for downstream events |
| `payload` | Type-specific object validated against the registered schema | The facts the consumers need, carried, not referenced |

The envelope overlaps the CloudEvents specification, which requires `id`, `source`, `specversion` and `type` and makes `time`, `subject` and `dataschema` optional ([CloudEvents spec](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md)), and Northmere maps onto those attributes so generic tooling works. The finance fields have no CloudEvents equivalent: **a generic event standard tells you how to move an event, not what a ledger needs to know.**

**Mandatory means mandatory.** The hub rejects an event with a missing `legal_entity` or `business_model`; it does not default them. A default is a guess, and a guessed legal entity is a misstatement in an entity's statutory accounts. [Global by Design: Entities, Currencies, Jurisdictions and Brands](#global-scale) explains why entity, brand, business model, market and jurisdiction must each be carried explicitly; the envelope is where that rule becomes enforceable.

{id: loosely-coupled-domains--identifiers-and-idempotency}
### Identifiers and idempotency

Three identifiers do three different jobs, and teams that merge them regret it.

- **`event_id` identifies the record of the fact.** It is generated once, in the database transaction that records the business change, and written to the producer's transactional outbox. The outbox relay can publish a message more than once after a crash, so **consumers must be idempotent** ([Richardson, Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html)); because the identifier was fixed before publication, every redelivery carries the same `event_id`.
- **The natural key identifies the fact itself.** Each type's contract names the payload fields that make the business fact unique: for `PaymentSettled`, the PSP, its payment reference and the settlement journal type. It catches **semantic duplicates**: a new `event_id` for a fact already published, or the same fact arriving from a webhook and from a report.
- **`correlation_id` identifies the business object**: the booking ID for Stayloft, the ticket ID for Wayfare, the invoice for Tablekin. It lets the auditor pull every event of one booking.

[Never Update, Only Append: Designing Custom Ledgers](#designing-financial-ledgers) shows how the subledger enforces these with database constraints. The architectural point is the one the sources agree on: Kafka's exactly-once semantics cover read-process-write inside Kafka, not side effects in external systems ([Confluent, 2017](https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/)), and change-data-capture tools such as Debezium deliver at least once after failures ([Debezium FAQ](https://debezium.io/documentation/faq/)). **Exactly-once effect is a property of the design, not of the middleware**: at-least-once delivery, idempotent consumers keyed on `event_id` and the natural key, and reconciliation to prove the result.

{id: loosely-coupled-domains--money}
### Money

Amounts are objects, never bare numbers: `{"value_minor": 60000, "currency": "EUR"}`. The rules are short and absolute:

- **Integers in minor units.** The exponent comes from the [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) table held as reference data: 2 for EUR and USD, 0 for JPY, 3 for KWD. A producer never sends `600.00`, and no consumer ever parses a float.
- **Currency on every amount**, including every amount inside the payload. A `PaymentSettled` event for a GBP payment settled in EUR carries both currencies explicitly.
- **Conversions are facts.** When a PSP or Northmere Pay converts currency, it publishes `FXRateApplied` with the rate as a decimal string, its source, its timestamp and the two amounts. The consumer never recomputes a conversion; it records the one that happened.
- **Splits are stated, not implied.** When an event carries a total and its parts (gross, fees, net), the parts must sum exactly to the total in minor units, and the contract says which part absorbs a rounding remainder.

{id: loosely-coupled-domains--classification-tags-and-reference-data}
### Classification tags and reference data

`brand`, `legal_entity`, `business_model`, `tax_jurisdiction` and `counterparty_id` are **values from governed registries**, not free text. The legal entity register, the brand and business-model code lists from the group chart of accounts v2 design, and the group partner ID from the partner hub described in [Finance Data Architecture: Who Owns the Truth](#finance-data-architecture) are the sources. The hub validates every value against the current registry, so a brand that launches a new market cannot publish events for a legal entity that the register does not yet know. That turns a common close-time surprise into a launch-time checklist item, which is the mechanism [The Next Brand Should Be Boring: Onboarding as Configuration](#brands-entities-markets) builds on.

{id: loosely-coupled-domains--semantic-rules}
### Semantic rules

The envelope and schemas are the syntax. The semantic rules decide whether the model stays useful for a decade. Northmere's v1 contract has seven:

| Rule | Allowed | Not allowed | Why |
| --- | --- | --- | --- |
| **Events state facts** | `StayCompleted`, `PaymentSettled`, `RefundIssued` | `ReleaseFunds`, `PostRevenue`, `CreateInvoice` | An instruction makes the producer responsible for the consumer's behavior; a fact lets each consumer decide |
| **No accounting in brand events** | Commercial amounts: gross, commission as contracted, fees as charged | GL accounts, debits and credits, profit centers, "revenue_amount" | The accounting engine derives accounts from approved, versioned rules; a brand that picks accounts is running a **Shadow Ledger** |
| **No vendor concepts** | Northmere identifiers; PSP references as payload attributes | S/4 company codes, document types, posting keys; Fusion segment values; Workday worktags | Vendor models stop at the anti-corruption layer |
| **Corrections are new facts** | `BookingModified`, `RefundIssued`, a reversal event that references the original | Updating or deleting a published event; republishing with changed values under the same `event_id` | The ledger corrects by adding; so does the event log |
| **Self-contained for replay** | Every amount the consumer needs, carried in the event | "Look up the booking for the commission" | A replay in 2033 cannot call a service retired in 2029 |
| **Every financial fact is published** | A fact with no accounting effect today (`BookingConfirmed` in the merchant model) | Suppressing events because "finance doesn't need that one" | Completeness is proven per source; accounting policy may change |
| **Business time is the producer's** | `occurred_at` as the business moment, with offset | Producers deciding the accounting period | The accounting date is derived by the engine from the entity's calendar |

The second rule is the one Northmere fought hardest over; removing SFP's own GL-account mapping table was the first boundary fix in [When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms). A brand engineer's objection is reasonable: "we know what this is; why not send the account?" The answer is that **the account is not a property of the fact; it is a property of the policy, the ledger and the chart**. When the group chart of accounts v2 goes live in 2029, every event carrying a 2027 account would carry a wrong one and every brand would need a release. When events carry facts, the rule store changes and no brand releases anything.

{id: loosely-coupled-domains--the-lisbon-booking-in-the-published-language}
### The Lisbon booking in the published language

The Lisbon booking is this book's running example: a traveler from Germany books a three-night stay in a Lisbon apartment on Stayloft, **€600.00** including VAT, paid by card through Adyen on 12 March 2027; the stay runs 18 to 21 April; commission is **15%, €90.00**; the illustrative Adyen processing cost is **€1.74**; the property's **€510.00** payout is instructed on 22 April and settled on 26 April. The booking ID is `SL-BK-9921347`; Northmere Pay's payment ID, sent to Adyen as the merchant reference, is `NPY-270312-004418` (see [Adyen: One Platform from Checkout to Settlement](#adyen)).

The first event is `PaymentSettled`, published by Northmere Pay's Adyen adapter from line 1 of the settlement details report for batch 1047 of merchant account `NMPay_Stayloft_EEA`. The `//` comments are annotations for the reader, not part of the message.

```text
{
  "event_id": "7c1e4a52-9b3d-4f0e-8d21-5a6f0c93b7e4",
  "event_type": "PaymentSettled",
  "event_version": 1,
  "occurred_at": "2027-03-14T06:40:12+01:00",   // batch booking time, Adyen account time zone
  "recorded_at": "2027-03-15T08:05:17Z",        // report processed by the adapter
  "brand": "STL",
  "legal_entity": "LE-NL-0031",                 // Northmere Payments B.V., receives the funds
  "business_model": "merchant",
  "source_system": "northmere-pay.adyen-adapter",
  "correlation_id": "SL-BK-9921347",
  "amount": { "value_minor": 59826, "currency": "EUR" },   // net settled for this payment
  "counterparty_id": "GP-PSP-000002",           // Adyen, as a group partner
  "tax_jurisdiction": "PT",                     // inherited from the booking
  "payload": {
    "payment_id": "NPY-270312-004418",
    "psp": "ADYEN",
    "psp_reference": "8827101993562344",
    "psp_journal_type": "Settled",
    "merchant_account": "NMPay_Stayloft_EEA",
    "batch_number": 1047,
    "settlement_date": "2027-03-14",
    "gross":      { "value_minor": 60000, "currency": "EUR" },
    "fees_total": { "value_minor": 174,   "currency": "EUR" },
    "net":        { "value_minor": 59826, "currency": "EUR" },
    "fee_event_ids": ["e3b0a7d4-61c2-4c8e-9f55-2d7e1b6a0c19"],  // the PSPFeeCharged event
    "fx": null,
    "source_document": {
      "report": "settlement_detail_report_batch_1047",
      "line": 1,
      "file_sha256": "9f2c...e71a"
    }
  }
}
```

Four details are deliberate. The **natural key** is `psp` plus `psp_reference` plus `psp_journal_type`, so the same line arriving twice, or arriving once from a report and once from a reprocessed file, is caught. The **source document and file hash** let an auditor walk from the event back to the exact report Adyen produced. The **amounts reconcile in the event itself**: 60000 minus 174 equals 59826. And the event carries **no account**: the accounting engine's rule for `PaymentSettled` in the merchant model decides that 59826 moves from the PSP receivable to cash.

The amounts need one more sentence, because they are the work of an anti-corruption layer. Adyen's settlement details line for this payment shows a gross credit of 600.00, a commission of 1.64 (interchange, scheme fees and markup) and a net of 598.36; the remaining 0.10 processing fee arrives in the batch's separate Fee entry ([Adyen: One Platform from Checkout to Settlement](#adyen) walks through it). Northmere Pay's adapter attributes that 0.10 to the payment using the payment accounting report, so the canonical `PSPFeeCharged` event carries the full **€1.74** and `PaymentSettled` carries **€598.26**. Adyen's report structure stops at the adapter; every consumer sees one payment, one fee, one net amount.

The second event is `StayCompleted`, published by the Stayloft booking platform when the check-out date passes without an open dispute:

```text
{
  "event_id": "b52f9d10-4e7a-4c3b-a1d8-0e6c27f4a983",
  "event_type": "StayCompleted",
  "event_version": 1,
  "occurred_at": "2027-04-21T11:00:00+01:00",   // check-out, Lisbon local time
  "recorded_at": "2027-04-21T10:04:37Z",
  "brand": "STL",
  "legal_entity": "LE-NL-0007",                 // Stayloft B.V., the contracting entity
  "business_model": "merchant",
  "source_system": "stayloft.booking-platform",
  "correlation_id": "SL-BK-9921347",
  "amount": { "value_minor": 60000, "currency": "EUR" },   // booking value at completion
  "counterparty_id": "GP-0004417352",           // the property, group partner ID
  "tax_jurisdiction": "PT",
  "payload": {
    "booking_id": "SL-BK-9921347",
    "booking_revision": 1,                      // no modifications since confirmation
    "stay": { "check_in": "2027-04-18", "check_out": "2027-04-21", "nights": 3 },
    "completion_basis": "checkout_passed_no_open_dispute",
    "commercial_terms": {
      "contract_ref": "STL-EU-MERCH-2026.3",
      "commission_rate_bp": 1500,
      "commission": { "value_minor": 9000,  "currency": "EUR" },
      "partner_net": { "value_minor": 51000, "currency": "EUR" },
      "rating_id": "CR-2027-03-12-55817310"     // SFP commission rating result
    },
    "traveler_country": "DE"
  }
}
```

The payload carries the commission as a **commercial fact**: the amount rated under contract `STL-EU-MERCH-2026.3`, with a reference to the rating result. It does not say "revenue". Under Northmere's policy the €90.00 is commission revenue at stay completion, as an agent with net presentation (see [Accounting for Architects: Ledgers, Journals and Revenue](#accounting-for-architects)), but that is the engine's interpretation; if recognition moved to check-in, the rule would change and the event would not. The `booking_revision` makes a late `BookingModified` detectable rather than silently ignored. The traveler's identity is absent: finance needs the country for tax, not the person, which keeps the event log out of most erasure requests.

[Never Update, Only Append: Designing Custom Ledgers](#designing-financial-ledgers) shows the entries the accounting engine derives from these two events and the other seven of the booking's life. The point here is the boundary: **the producer states what happened; the engine owns what it means for the books**.

{id: loosely-coupled-domains--the-v1-catalog}
### The v1 catalog

Keystone v1 registers eighteen event types. The catalog is small on purpose, and every type has a producing domain, a natural key and at least one named finance consumer.

| Event type | Producing domain at Northmere (2027) | Natural key (payload) | Primary finance consumers |
| --- | --- | --- | --- |
| `BookingConfirmed`, `BookingModified`, `BookingCancelled` | Stayloft and Wayfare booking platforms | booking ID + revision | Subledger, FinDB, tax |
| `StayCompleted` | Stayloft booking platform | booking ID + revision | Subledger (revenue trigger) |
| `PaymentAuthorised`, `PaymentCaptured` | Northmere Pay; Wayfare and Tablekin Stripe adapters | PSP + PSP reference + event code | Subledger, payments-to-ledger matching |
| `PaymentSettled`, `PSPFeeCharged` | Same, derived from settlement reports | PSP + PSP reference + journal type | Subledger, BlackLine matching, FinDB |
| `RefundIssued` | Same | PSP + modification reference | Subledger, matching |
| `ChargebackReceived`, `ChargebackResolved` | Northmere Pay dispute tool; Stripe adapters | PSP + dispute reference + stage | Subledger, matching, controls |
| `PartnerPayoutInstructed` | SFP payout engine; Wayfare payout engine until 2029 | payout instruction ID | Subledger, treasury |
| `PartnerPayoutSettled` | Northmere Pay; Stripe Connect adapter | payout ID + bank reference | Subledger, bank reconciliation |
| `CommissionInvoiced` | SFP commission billing; FI-CA | invoice number | Subledger, tax, e-invoicing |
| `SubscriptionInvoiced`, `UsageRated` | Tablekin Stripe Billing adapter | Stripe invoice ID or usage record ID | Workday Financials via Accounting Center |
| `AdClickBilled` | Northmere Ads billing service | billing run + advertiser + day | FI-CA from 2028 |
| `FXRateApplied` | Northmere Pay; PSP adapters | conversion reference | Subledger, treasury |

Anything not on this list is not a canonical financial event, however financial it sounds. A customer profile, a property's listing, a marketing campaign: those stay in their domains' own models. Section "Keeping the canonical model narrow" below explains why that boundary is the most important governance decision in the chapter.

{id: loosely-coupled-domains--versioning-and-compatibility}
## Versioning and Compatibility

A canonical model is only as stable as its change rules. Northmere's rules distinguish three classes of change and tie the dangerous one to the close calendar.

**Additive changes** add an optional field to a type's schema within the same `event_version`. They are checked automatically by the schema registry. Confluent's Schema Registry, for example, supports BACKWARD, FORWARD and FULL compatibility and their transitive variants, and defaults to BACKWARD, which checks a new schema only against the latest version ([Confluent, Schema evolution](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html)). Northmere sets **BACKWARD_TRANSITIVE** on every canonical subject, because a ledger replays years of history and a schema that can read only last month's events is not good enough. Under backward compatibility the documented upgrade order is consumers first, then producers, which matches finance's interest: the ledger learns to read a field before anyone sends it.

**Semantic changes** are the dangerous ones that a registry cannot see: a field whose type is unchanged but whose meaning changes, as the `cancelled` flag did. The rule is absolute: **a field never changes its meaning, its unit or its sign convention within a major version.** A new meaning gets a new field, or a new major version. Adding a value to a code list (a new `business_model`, a new `psp_journal_type`) is treated as a semantic change: consumers are required to quarantine unknown values rather than default them, and the change board schedules the value's introduction after the rule store has a rule for it.

**Breaking changes** (removing a field, renaming, changing a type, splitting an event) create a new major version and follow a lifecycle that respects the close:

![A path from Proposed and Approved to Dual publish, where v1 and v2 envelopes are both sent while consumers migrate, then Verified after a quarter close, v1 deprecated, v1 retired at a month start, and finally Readable in an archive for replay.](finance-systems-architecture/posts/30-loosely-coupled-domains/assets/images/30-loosely-coupled-domains/breaking-change-lifecycle.jpeg)

**Figure 2:** *The lifecycle of a breaking change to a canonical event. The producer publishes both versions until every consumer has migrated and one quarter close has been tied out on both; v1 stops being produced only at a month start outside year-end, and its schema remains readable for the retention period because replay must read history in the version it was written.*

Three calendar rules make this a finance discipline rather than an engineering one:

- **No cut-over inside a close window.** At Northmere in 2027 the window runs from two working days before month end to working day 9, shrinking as the close does. A producer may start dual publishing at any other time; it may stop publishing the old version only on a month start.
- **One quarter close in parallel.** A breaking change runs through a full quarter close, including the quarter-end tie-out, on both versions, and the subledger's entries derived from v1 and v2 are compared before v1 is retired. A quarter close exercises accruals, revaluation and reporting paths that an ordinary month does not.
- **No retirement in December or January.** Year-end and the audit fieldwork that follows are not the time to change what the ledger reads.

The cost is real: a producer may carry two versions for four to six months. That is the price of never coordinating a release with the close. Windows also have a maximum: a version deprecated for two quarters with a consumer still on it is escalated to the design authority, because indefinite dual publishing is how canonical models accumulate dead weight.

Schemas are never deleted from the registry. Northmere retains financial records for 10 years, and a replay in 2035 of an event published in 2027 must read it with the 2027 schema. Consumers that need the current shape **upcast** old versions in code that is tested against stored historical samples.

{id: loosely-coupled-domains--governing-the-canonical-model}
## Governing the Canonical Model

A canonical model without an owner becomes the implicit model again within two years. Northmere's governance has four parts.

**An owner.** Lucía Romero owns the canonical model as an architecture product: its catalog, envelope, rules and registry. She does not own the meaning of each fact. Each **event family has a business owner** in the domain that produces it: Ingrid Solberg's Northmere Pay for payment and payout-settlement events, the brand engineering directors for booking events (Jonas Berg for Stayloft), Arjun Rao for Tablekin's billing events. Leila Haddad's accounting policy team is a mandatory reviewer of every change, because a change in facts can change what the rules must do.

**A change board inside the architecture review.** The Canonical Event Change Board is a standing 30-minute weekly slot of the architecture review board described in [Architecture Governance That Speeds Decisions](#architecture-governance), not a separate committee. Its rules:

| Change class | Example | Decided by | Target lead time |
| --- | --- | --- | --- |
| **Additive** | New optional `cancellation_scope` field on `BookingModified` | Registry check plus Lucía's team; consumers notified | 2 working days |
| **Semantic** | New `business_model` value; new event type | Change board, with accounting policy and the consuming teams | 10 working days |
| **Breaking** | Splitting `PaymentSettled` into gross and net events | Change board, then the Keystone design authority; Mei Tanaka's team assesses control impact | 25 working days |

The lead-time targets match the decision-velocity targets Dana set for the architecture function in [The Chief Architect's Job: Making Many Systems Tell One Story](#chief-architect-role). A board that takes six weeks to approve an optional field will be bypassed, and the bypass will look exactly like the 2019 `booking_updated` consumer.

**A schema registry as the source of truth.** Producers serialize against it, the hub validates against it, and CI refuses a producer build whose schema is not registered. Confluent's registry, for example, supports Avro, Protobuf and JSON Schema ([Confluent, Schema Registry](https://docs.confluent.io/platform/current/schema-registry/index.html)). Beside each schema sits the human contract: definitions, natural key, semantic rules, business owner and example events. The Open Data Contract Standard, a YAML format with sections for schema, data quality, service levels and roles ([Bitol, ODCS](https://bitol-io.github.io/open-data-contract-standard/latest/)), is a reasonable template for it.

**Consumer-driven contract tests.** Ian Robinson described consumer-driven contracts in 2006 as provider contracts derived from the expectations of existing consumers, which tell a provider what it must keep stable ([Robinson, 2006](https://martinfowler.com/articles/consumerDrivenContracts.html)). Pact implements the idea for HTTP and message integrations ([Pact docs](https://docs.pact.io/)), and its `can-i-deploy` check asks whether an application version is compatible with the versions already deployed alongside it ([Pact, can-i-deploy](https://docs.pact.io/pact_broker/can_i_deploy)). At Northmere every finance consumer publishes a message pact stating the fields and values it relies on; every producer pipeline runs those pacts and blocks a deployment that would break one. Had the 2019 SFP consumer published a pact on `booking_updated`, the May 2027 release would have failed its build instead of the April close.

Contract tests do not replace the registry; they cover what a schema cannot. A schema says `cancelled` is a boolean; a pact says SFP relies on `cancelled: true` meaning the whole booking.

{id: loosely-coupled-domains--architecture-adapters-hub-and-consumers}
## Architecture: Adapters, Hub and Consumers

![Producers publish through adapter kits onto Kafka; a simple hub validates, adds reference keys, counts and routes, rejects to quarantine, and delivers to the subledger, FinDB, BlackLine, Workday and Fusion, with vendor ledgers including S/4HANA behind their own adapter layers.](finance-systems-architecture/posts/30-loosely-coupled-domains/assets/images/30-loosely-coupled-domains/target-event-topology.jpeg)

**Figure 3:** *Northmere's target topology. Producers publish canonical events through the adapter kit or a vendor ACL onto Kafka; the hub validates, enriches with reference keys, counts and routes; consumers receive the delivery shape they need; every vendor ledger is reached through its own anti-corruption layer. Business rules live at the edges, never in the hub.*

{id: loosely-coupled-domains--the-brand-adapter-kit}
### The brand adapter kit

The adapter kit is what makes the canonical model cheap to adopt. Without it, each brand designs its own publication code, and the canonical model becomes a document that producers interpret. Keystone funds the kit centrally, which [The Chief Architect's Job: Making Many Systems Tell One Story](#chief-architect-role) identifies as the condition for brands adopting a standard at all. It contains five things.

| Component | What it does | Why it matters |
| --- | --- | --- |
| **Event SDK with validation** | Client libraries in the brands' languages (Java, Kotlin, Go, TypeScript at Northmere) that build envelopes, generate `event_id`, write to a transactional outbox, serialize against the registry and validate code-list values before publication | A malformed event fails in the producer's test suite, not in the hub on working day 2 |
| **Reference mapping templates** | Worked mappings from typical brand models (a booking with revisions, a ticket, a subscription invoice) to canonical events, plus the derivation configuration for entity, brand, business model and jurisdiction | A new brand starts from Stayloft's mapping, not a blank page |
| **Conformance test suite** | A certification runner that replays a brand's sample events through hub validation and a **posting simulation** against the current rule store, then compares the simulated entries with expected entries agreed with the accounting policy team | A brand proves its events produce the right accounting before go-live, with evidence the auditor can read |
| **Reconciliation hooks** | Producer-side control totals: per source, per event type, per day, the count and amount sum of published events, emitted as a control record the hub's delivery ledger compares with what it received | Completeness is proven from both ends, not asserted by the hub |
| **Onboarding guide** | Go-live checklist, ownership template (business owner, on-call, contract pacts), cut-over and parallel-run guidance tied to the close calendar | Onboarding becomes a repeatable process measured in weeks |

The conformance suite changes the conversation with Finance. Before it, a brand's go-live was approved by engineers and discovered by accountants at month end; with it, Leila's team signs off a posting simulation of the brand's own events before the first production event.

{id: loosely-coupled-domains--the-integration-hub}
### The integration hub

The hub is not one product. At Northmere it is a set of services on the Kafka platform that Platform Engineering runs, owned by Lucía's integration team. It **validates** contracts (envelope, registered schema version, known code values, amounts that add up); **enriches with reference keys only**, such as the group partner ID where a producer still sends a legacy partner identifier; keeps a **delivery ledger** of counts and amounts received, rejected, delivered and replayed per source, type and day, compared with the producer's control record; **routes** to each consumer in the shape it needs; holds rejects in a **quarantine** with an owner and an age, watched like a suspense account; **replays** a time range or a correlation ID to a named consumer on request; and runs the **file gateway** for PSP, bank and vendor files, which become canonical events at the first adapter they reach.

James Lewis and Martin Fowler's 2014 microservices article argued for **smart endpoints and dumb pipes**, against products that put "significant smarts into the communication mechanism itself", with the enterprise service bus as the example ([Lewis and Fowler, 2014](https://martinfowler.com/articles/microservices.html)). A finance hub looks, at first sight, like the ESB they warned about. The distinction that matters is between **control** and **logic**:

| The hub may | The hub must not |
| --- | --- |
| Validate envelopes and schemas | Decide accounts, revenue timing or tax treatment |
| Enrich with reference keys from governed registries | Apply brand-specific business rules |
| Count, compare control totals, quarantine | Aggregate or summarize in a way that loses detail |
| Route by event type, entity and consumer | Orchestrate business processes across domains |
| Replay on request | Correct or rewrite events |

In my experience the test is simple: **if a change to accounting policy, a brand's product or a vendor's release requires a change to the hub, logic has leaked into the pipe.** Counting and validating are not logic in that sense; they are the evidence that the pipe did its job, and finance cannot do without them. An ESB fails by knowing too much about the messages; a finance hub fails by knowing too little about whether they arrived.

![A pipeline with checkpoint, counter, quarantine tank and replay loop, connecting producer workshops to consumers where the accounting rules live.](finance-systems-architecture/posts/30-loosely-coupled-domains/assets/images/30-loosely-coupled-domains/counting-pipe-smart-edges.jpeg)

**Figure 4:** *The hub validates, counts, quarantines and replays, but never decides accounts or timing: if an accounting-policy change needs a hub change, logic has leaked into the pipe.*

{id: loosely-coupled-domains--rationalizing-three-integration-technologies}
### Rationalizing three integration technologies

Lucía's inventory made a decision unavoidable: three integration technologies with overlapping capability, three monitoring approaches and three places where a financial interface could fail silently. Dana's design-authority decision, recorded in June 2027, gave each technology one job.

| Technology | Decision | Job | Reasoning |
| --- | --- | --- | --- |
| **Kafka** (Platform Engineering) | Invest; the only backbone for canonical financial events | Event transport, retention, replay; hub services built on it | Northmere's volume (about 1.1 billion operational financial events a year) and replay over months need a log, not a request router; Platform Engineering already runs it at that scale |
| **SAP Integration Suite** | Invest, scoped to the SAP boundary | The anti-corruption layer into and out of S/4HANA and FI-CA | SAP-maintained content and monitoring for SAP interfaces; keeps translation to SAP's model outside the ERP, consistent with clean core |
| **MuleSoft** | Contain: no new flows from July 2027 | Existing Wayfare and Tablekin flows, until their ledgers' future is decided | Wayfare's Fusion and Tablekin's Workday integrations run on it today; rewriting them before the 2027 Q4 convergence decision would be work that the decision might discard |

Two alternatives were rejected. **One iPaaS for everything** would have put a billion-event stream and its replay through a platform built for orchestrated flows. **Kafka for everything** would have meant custom code posting into S/4HANA without SAP's interface content and monitoring. MuleSoft's containment is dated: each remaining flow has an owner and retires with its ledger convergence wave (wave 3, 2029–2030, conditional on the Q4 decision). Two strategic technologies are not the minimum possible; they are **the minimum that does not force one platform to do what it was not designed for**.

{id: loosely-coupled-domains--anti-corruption-layers-at-vendor-boundaries}
## Anti-Corruption Layers at Vendor Boundaries

Every vendor has a model, a release cadence and quirks of delivery. The ACL's job is to absorb all three so that no consumer of a canonical event knows which vendor produced or will receive it.

| Boundary | Direction | What the ACL absorbs | Northmere design |
| --- | --- | --- | --- |
| **SAP S/4HANA** | Inbound postings | Company codes, document types, posting keys; released APIs versus classic interfaces | Summarized journals from the subledger are translated in Integration Suite; SAP classifies released APIs as the upgrade-stable "Level A" and BAPIs as classic "Level B" ([SAP News, 2025](https://news.sap.com/2025/08/extend-sap-s4hana-cloud-right-way-clean-clear/)), so new postings use released APIs |
| **Oracle Fusion** (Wayfare) | Inbound postings and transactions | Segment values, FBDI file and job mechanics, quarterly update changes | Today about 2,600 summarized GL lines a day via FBDI on MuleSoft; if Wayfare adopts Oracle Accounting Hub, its event types reuse the canonical names, as [Oracle Fusion: An Accounting Hub for High-Volume Events](#oracle-fusion) proposes |
| **Workday** (Tablekin) | Inbound transactions | Worktags, ledger accounts, versioned web services | Accounting Center ingests external transactions through an accounting source and Prism ingestion tables, then generates and posts summarized journals ([Workday docs](https://doc.workday.com/admin-guide/en-us/financial-management/accounting-center/accounting-generation/iue1611339888720.html)); the ACL maps canonical events into those rows |
| **Adyen** | Outbound from PSP | Webhook delivery semantics, report formats, fee attribution | Webhooks are at-least-once and duplicates share `eventCode` and `pspReference`; Adyen expects acknowledgment within 10 seconds ([Adyen webhooks](https://docs.adyen.com/development-resources/webhooks/handle-webhook-events)); settlement events come from reports, with fees attributed per payment |
| **Stripe** (Tablekin, Wayfare, Stayloft secondary) | Outbound from PSP | Unordered events, duplicate events, API versions | Stripe does not guarantee event order and can send two distinct events for the same change ([Stripe webhooks](https://docs.stripe.com/webhooks)); the ACL dedupes on object ID plus type, and pins the API version, as [Stripe: Every Movement Is a Balance Transaction](#stripe) describes |

Two design rules apply at all five boundaries:

- **A vendor's version change stops at the ACL.** Stripe ships monthly non-breaking versions and two breaking releases a year ([Stripe versioning](https://docs.stripe.com/api/versioning)); Oracle updates Fusion quarterly; Workday releases twice a year. Each change is regression-tested against the ACL's contract tests, and the canonical events do not change unless the vendor introduces a genuinely new fact, which then goes through the change board.
- **The ACL is owned by the team that owns the vendor relationship**: Northmere Pay for the PSPs, Sven Aalto's SAP platform team for S/4HANA, Hana Kowalski's and Arjun Rao's teams for Fusion and Workday. The integration team owns the pattern and the tests. An ACL owned by people with no vendor knowledge becomes a pass-through.

Not every boundary deserves an ACL. [Map What Finance Does Before What Runs It](#capability-mapping) gave the test: **build an ACL where a vendor's model would otherwise spread into contexts you own; conform where it stays inside the vendor's context.** OneStream's dimensional model stays inside consolidation; the trial-balance load into it is a conformist interface, and that is fine.

{id: loosely-coupled-domains--event-or-batch-per-consumer-from-one-source}
## Event or Batch: Per Consumer, From One Source

"Event-driven or batch?" is the wrong question for finance. The right question is **what each consumer needs, delivered from one stream of facts**. A batch built from the events, with control totals that tie back to them, is not a second integration; a batch extracted separately from the source system is.

| Consumer | Delivery shape | Latency | Why |
| --- | --- | --- | --- |
| SFP merchant subledger and accounting engine | Event stream | Seconds to minutes | Per-booking liabilities and payout availability need current state |
| SAP S/4HANA GL | Daily summarized journals with drill-back key | Daily | About 3 million subledger lines become about 38,000 GL lines a day; the GL needs balances, not events |
| BlackLine transaction matching | Daily files of normalized settlement and payout events, with control totals | Daily | Matching runs on complete days; a partial day creates false breaks |
| FinDB (Snowflake) | Continuous load to the raw layer | Minutes | Analytics and the ledger-to-warehouse tie-out need detail, see [One Number, Many Views: Finance Data from Operations to Analytics](#finance-data-flows) |
| OneStream | Trial balances from the ledgers, not events | Monthly, plus flash | Consolidation reads ledgers of record, never events |
| Vertex tax determination | Synchronous API at invoicing | Real time | An open host service, not an event consumer |

The last two rows matter as much as the first. **Not everything should consume events.** Consolidation that read events would become a second ledger; tax determination is a request that needs an answer. The canonical model is for facts that finance must account for, reconcile or report, not for every interaction.

{id: loosely-coupled-domains--in-practice-northmere-s-first-year}
## In Practice: Northmere's First Year

Keystone's canonical events v1 were approved in June 2027 and the registry went live on 1 July 2027. Stayloft and Northmere Pay were the first two producers, because they carry most of the volume and because SFP's redesign in [Never Update, Only Append: Designing Custom Ledgers](#designing-financial-ledgers) depended on a stable contract.

**The first producer migration.** Stayloft's booking platform adopted the adapter kit for the four booking events in July and August. The 2019 `booking_updated` consumer in SFP was switched off on 1 October 2027, after the September quarter close ran on both feeds and the subledger's traveler-funds balance from the canonical feed agreed with the legacy feed to the cent for every entity. The conformance suite found two mapping defects before go-live: modifications that shortened a stay were published with the original `occurred_at`, and bookings of properties in the Azores carried `PT` instead of the subdivision code `PT-20`, which tax determination needs because the Azores apply lower regional VAT rates. Both were fixed in the brand's adapter configuration; neither reached the ledger.

**The delivery ledger on an ordinary day.** The Lisbon booking's `StayCompleted` on 21 April was one of a few hundred thousand that day. Once the redesigned flow was live, the delivery ledger for a typical fourth-quarter day showed, for source `stayloft.booking-platform` and type `StayCompleted`: **214,906** events in the producer's control record; 214,906 received; **37** rejected and quarantined because their `legal_entity` was a new Stayloft entity not yet in the register; 214,869 delivered to the subledger; 0 replayed. The entity was registered the same afternoon and the 37 events were replayed and delivered. The numbers are illustrative; the mechanism is the point. **Every event is delivered, quarantined with an owner, or explicitly replayed, and the counts are compared with the producer's own.** That comparison is the completeness control the auditor tests.

**The second producer type.** Northmere Pay's Adyen and Stripe ACLs replaced six PSP-specific feeds into SFP and BlackLine with the canonical payment events. BlackLine's matching rules, which [BlackLine: Matching, Certifying and Closing](#blackline) describes as one rule set for every provider once data is normalized, now read one record shape. The payments-to-ledger program in [Payments-to-Ledger: Draining the Suspense Swamp](#payments-to-ledger) uses these events as its foundation.

**What did not move.** Wayfare and Tablekin kept their MuleSoft flows into Fusion and Workday, as decided, but both publish canonical events to FinDB from the fourth quarter so that analytics and tax see one shape across brands. Adoption is **staged by value**, not by a mandate to rewrite everything.

{id: loosely-coupled-domains--trade-offs-ways-to-connect-financial-domains}
## Trade-offs: Ways to Connect Financial Domains

| Approach | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- |
| **Point-to-point translations** | Fast for the first few interfaces; no central team | Translations grow roughly with the square of systems; no shared completeness evidence | A small estate, or a temporary bridge with an expiry date |
| **Narrow canonical financial events** (this chapter) | One translation per producer and consumer; facts stable across vendor and ledger changes; completeness provable per source | Needs an owner, a registry, a change board and an adapter kit; dual publishing costs producers | Several brands, ledgers or PSPs; a convergence program; a close under time pressure |
| **Conform to the ERP's model** (brands post ERP documents) | No translation for the ERP; vendor tooling works | Every ERP change and every ledger replacement ripples into brands; accounting decided by producers | One ERP, few producers, no plan to change either |
| **Consumer-specific contracts** (each consumer defines what it wants) | Each consumer gets exactly its shape | Producers maintain many contracts; no shared meaning; the same fact differs by consumer | Non-financial integrations; analytics extracts |
| **Enterprise canonical model of everything** | Promise of one language across the company | Slow, lowest common denominator, central bottleneck; rarely finished | Almost never; see the next section |

The second row is the recommendation for a multi-brand, multi-ledger group like Northmere. Its precondition is investment in the adapter kit and governance; without them it degrades into the fifth row or back into the first.

{id: loosely-coupled-domains--keeping-the-canonical-model-narrow}
## Keeping the Canonical Model Narrow

Canonical models fail in three well-known ways, and each has a specific defense.

**The enterprise canonical model.** The model tries to describe customers, products, inventories, orders and ledgers for every system in the company. Agreement takes years, because every domain has a legitimate and different model of each noun; "account" alone means a customer account in sales, a bank account in treasury and a GL account in accounting. The defense is a **scope test**: an event type belongs in the canonical model only if the ledger, a reconciliation or a regulator needs it. Northmere's catalog has eighteen types and no customer object. Everything else stays in its domain's own language, exchanged by whatever contract those domains agree.

**The lowest common denominator.** When a model must fit every producer, it keeps only what all of them share: Stayloft's revisions, Wayfare's multi-leg tickets and Tablekin's usage tiers become a generic "order". The defense is a **common envelope with type-specific payloads**, and payload fields that are optional for producers to whom they do not apply. A narrow namespace, `payload.ext.<brand>`, is allowed for brand-specific attributes that analytics wants, on the condition that **no finance consumer may depend on an `ext` field**; a field that finance needs is promoted into the governed payload through the change board.

**The central bottleneck.** When every change waits for one team, producers route around the model. The defense is the governance above: automated additive changes, two-week semantic ones, a centrally funded kit, and a board embedded in an existing forum whose lead time Lucía measures. When it rises, the board is the problem, not the producers.

There is a fourth failure specific to finance: **the canonical model as the ERP's model in disguise.** If the envelope carries company codes or the payload carries posting keys "for convenience", the model is conformist to one vendor, and the 2027 Q4 decision between Central Finance and an accounting-hub pattern would require every producer to change. Northmere's rule that no vendor concept enters an event is what makes that decision, in [Converge or Coexist: Living with More Than One ERP](#multiple-erps), a change of adapters rather than of brands.

{id: loosely-coupled-domains--integration-with-the-rest-of-the-estate}
## Integration with the Rest of the Estate

[The Life of a Booking: From €600 Payment to $97.38 of Revenue](#transaction-to-report) traces the Lisbon booking from these events to the published statements. [Payments-to-Ledger: Draining the Suspense Swamp](#payments-to-ledger) builds the three-way match between order, PSP and bank on the payment events and PSP ACLs. [Systems of Record: Ending the Doppelgänger Record](#systems-of-record) decides which domain is authoritative for each fact, and therefore who may publish each event type. [One Number, Many Views: Finance Data from Operations to Analytics](#finance-data-flows) lands the same events in FinDB, where the ledger-to-warehouse tie-out joins on `event_id` and `correlation_id`. [The Next Brand Should Be Boring: Onboarding as Configuration](#brands-entities-markets) turns the adapter kit into the onboarding kit for new brands and markets. And [Modernizing Without Stopping the Close](#incremental-modernization) uses the stable contract as the seam for migrating SFP's merchant subledger into the group core in 2029: producers keep publishing the same facts while the consumer behind them is replaced.

{id: loosely-coupled-domains--failure-modes}
## Failure Modes

- **Accounts in events.** A producer adds `gl_account` "temporarily"; within a year three consumers depend on it and the chart change becomes a brand release. Remedy: the registry rejects reserved field names, and the rule store is fixed instead.
- **IDs generated on send.** Every retry becomes a new event; the natural-key check catches it, but quarantine fills. Remedy: the SDK generates the ID in the outbox transaction.
- **Logic in the hub.** An enrichment step starts deriving profit centers "because it already has the entity", and the hub becomes an accounting engine nobody audits. Remedy: the hub test above; enrichment reviewed by the accounting policy team.
- **Replay that sends money.** A replay re-delivers `PartnerPayoutInstructed` to a consumer that executes payouts. Fowler's event-sourcing essay warns that replay must suppress calls to external systems ([Fowler, 2005](https://martinfowler.com/eaaDev/EventSourcing.html)). Remedy: replays are delivered only to named consumers, flagged as replays, and money-moving consumers are idempotent on the instruction ID.
- **Batch extracts beside events.** A team builds a nightly extract from the source database "because it's easier", and two versions of the same facts reach finance. Remedy: batch shapes are produced from the event stream by the hub, with control totals tied to it.
- **ACL as pass-through.** Vendor field names appear in canonical payloads because the ACL "just forwards". Remedy: ACL ownership with the vendor-owning team; contract tests that reject vendor identifiers outside named reference fields.

{id: loosely-coupled-domains--the-chief-architect-s-view}
## The Chief Architect's View

The decisions in this chapter are few, but each one is hard to reverse.

- **Scope of the canonical model.** Finance facts only, with the scope test written into the standard. This is the decision that prevents the enterprise canonical model, and it is the Chief Architect's to make and defend.
- **The semantic rules, especially "no accounting in events".** These become a mandatory enterprise-application standard (Northmere's first proposed standard in late 2026 was exactly "canonical financial events"), with waivers that carry an expiry. At Northmere it is STD-FIN-01, declared mandatory from 1 April 2027 and enforced, together with STD-FIN-02 on idempotent posting, from 1 July 2027, when the schema registry went live ([Principles That Decide Things](#principles-standards-reference)).
- **One job per integration technology.** A dated rationalization decision, with containment rules for the technology being retired, beats both a big-bang consolidation and a permissive "use what you like".
- **Funding.** The adapter kit and the integration team are funded centrally. A standard that each brand must pay for from its own roadmap loses to the roadmap.
- **Ownership.** The model has an architecture owner; each event family has a business owner; each ACL is owned by the team that owns the vendor. Leila's accounting policy team is a reviewer of every semantic change, and Mei Tanaka's controls team assesses breaking changes for control impact.

What to watch, quarterly: the share of financial-event feeds on canonical events (Northmere's 2027 target was the first two brand feeds); the change board's lead time by change class; the age and value of quarantined events; control-total breaks per source; the number of consumers still on deprecated versions; and the count of interfaces into finance that bypass the hub. The last one is the honest measure. An estate where new finance feeds still appear outside the canonical model has a standard on paper only.

Over ten years the event log becomes more than an integration layer: a **portable, vendor-neutral record of every financial fact the group produced**, which lets each change of ledger, ERP or PSP be a migration rather than a reconstruction. [Built to Be Replaced: Evolving the Finance Estate Over a Decade](#long-term-evolution) returns to that idea.

{id: loosely-coupled-domains--questions-to-ask}
## Questions to Ask

1. Can you list every event type finance consumes, its producing domain, its business owner and its natural key? If not, where is the implicit model?
2. Does any producer send GL accounts, profit centers, debits or credits, or vendor document types? Who decided, and when does it stop?
3. Is `event_id` generated when the fact is recorded, or when the message is sent?
4. Are amounts integers in minor units with a currency on every amount, including inside the payload?
5. What does the hub do that would have to change if accounting policy changed? Whatever it is does not belong in the hub.
6. For each source, can you show yesterday's counts and amounts published, received, rejected, delivered and replayed, and do the producer's and hub's numbers agree?
7. What is the rule for a breaking change, and does it forbid cut-over inside the close window and at year-end?
8. Which finance consumers have published contract tests, and do producer pipelines block on them?
9. At each vendor boundary, which team owns the anti-corruption layer, and what happened to the canonical events at the last vendor upgrade?
10. How long does an additive change take to approve today, and who measures it?

{id: loosely-coupled-domains--from-coupling-to-proof}
## From Coupling to Proof

Loose coupling buys independence: brands release, vendors upgrade and ledgers are replaced without asking each other's permission. It does not, by itself, buy confidence. The control totals, natural keys and correlation IDs in this chapter are the raw material for something finance needs even more: the ability to trace any number in the statements back to the facts behind it, and to prove at every boundary that nothing was lost, duplicated or changed. [Reconciled by Design: Traceability and Audit Across Boundaries](#traceability-and-reconciliation) takes those keys and builds the reconciliation catalog and the audit walkthrough on top of them.

{id: loosely-coupled-domains--sources-and-evidence}
## Sources and Evidence

{id: loosely-coupled-domains--vendor-documentation}
### Vendor documentation

- [Schema evolution and compatibility](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html), Confluent (accessed October 2026) — compatibility types, BACKWARD as the non-transitive default, consumer-first upgrade order.
- [Schema Registry overview](https://docs.confluent.io/platform/current/schema-registry/index.html), Confluent (accessed October 2026) — supported formats (Avro, Protobuf, JSON Schema).
- [Exactly-Once Semantics Are Possible: Here's How Kafka Does It](https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/), Neha Narkhede and Guozhang Wang, Confluent, 2017 — exactly-once scope limited to Kafka read-process-write.
- [Debezium FAQ](https://debezium.io/documentation/faq/), Debezium project — at-least-once delivery after failures.
- [Extend SAP S/4HANA Cloud the right way](https://news.sap.com/2025/08/extend-sap-s4hana-cloud-right-way-clean-clear/), SAP News, 2025 — released APIs as Level A and classic APIs as Level B in clean-core terms.
- [Accounting Center: accounting sources](https://doc.workday.com/admin-guide/en-us/financial-management/accounting-center/accounting-generation/iue1611339888720.html), Workday administrator guide — ingestion tables, enrichment, summarized journal posting.
- [How Oracle Accounting Hub works](https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/how-oracle-accounting-hub-cloud-works.html), Oracle, release 26C — accounting rules engine for non-Oracle sources.
- [Handle webhook events](https://docs.adyen.com/development-resources/webhooks/handle-webhook-events), Adyen — acknowledgment window, HMAC verification, duplicate identification by eventCode and pspReference.
- [Webhooks](https://docs.stripe.com/webhooks) and [API versioning](https://docs.stripe.com/api/versioning), Stripe — unordered delivery, duplicate events, monthly and twice-yearly versions.

{id: loosely-coupled-domains--standards-and-regulation}
### Standards and regulation

- [CloudEvents specification](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md), CloudEvents project, version 1.0 — required and optional context attributes; uniqueness of source plus id.
- [ISO 4217 Currency codes](https://www.iso.org/iso-4217-currency-codes.html), International Organization for Standardization — currency codes and minor units.
- [Open Data Contract Standard](https://bitol-io.github.io/open-data-contract-standard/latest/), Bitol — YAML data contract structure used as a template for the human contract.

{id: loosely-coupled-domains--practitioner-and-research-sources}
### Practitioner and research sources

- [Domain-Driven Design Reference](https://www.domainlanguage.com/ddd/reference/), Eric Evans, 2015 — published language, anticorruption layer, open host service, conformist.
- [Canonical Data Model](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html), Gregor Hohpe and Bobby Woolf, *Enterprise Integration Patterns*, 2003 — the pattern and its translator arithmetic.
- [What do you mean by "Event-Driven"?](https://martinfowler.com/articles/201701-event-driven.html), Martin Fowler, 2017 — event notification versus event-carried state transfer.
- [Microservices](https://martinfowler.com/articles/microservices.html), James Lewis and Martin Fowler, 2014 — smart endpoints and dumb pipes; the ESB critique.
- [Consumer-Driven Contracts: A Service Evolution Pattern](https://martinfowler.com/articles/consumerDrivenContracts.html), Ian Robinson, 2006 — the consumer-driven contract idea.
- [Pact documentation](https://docs.pact.io/) and [can-i-deploy](https://docs.pact.io/pact_broker/can_i_deploy), Pact Foundation — contract testing for HTTP and message integrations; deployment compatibility checks.
- [Pattern: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html), Chris Richardson — outbox and the need for idempotent consumers.
- [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html), Martin Fowler, 2005 — replay hazards with external systems.

Northmere is fictional; its systems, people, identifiers and figures are illustrations. Architectural recommendations are the author's judgment.
