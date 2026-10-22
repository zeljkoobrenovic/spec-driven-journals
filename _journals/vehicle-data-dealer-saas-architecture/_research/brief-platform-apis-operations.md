# Research brief: Data APIs, events and integration, and platform operation for a vehicle data and dealer SaaS platform

Prepared 22 October 2026 for chapter writers of *Architecting a Vehicle Data and Dealer SaaS Platform*. The brief covers the "plumbing" chapters: how the platform exposes data (APIs, webhooks, events), how it ingests and checks data (pipelines, contracts, entity resolution), how it survives the failure of the paid and public sources it depends on, what it costs, how it is attacked and how it is observed. The brief is vendor-neutral. Stripe, Google, Microsoft and AWS get space because they publish unusually precise, dated engineering guidance, not because the book endorses their products. The design target throughout is a platform serving **about 10,000 dealer tenants plus several hundred API clients** (software vendors, portals, lessors, insurers).

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (22 October 2026) and supports the claim. Paraphrases stay close to the source; quoted text is quoted. The date is the source's publication date, not the fetch date. Undated product or documentation pages are marked "n.d., accessed 2026-10".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, encyclopaedia, vendor case study, API directory), not from the company's own technical documentation.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about a proprietary system that its owner has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Several foundational sources are old: Kreps on Kappa (2014), Fowler on circuit breakers (2014), Brooker on jitter (2015), Stripe on versioning (2017), the AWS Builders' Library articles (2019–2020), the Google SRE book (2016). Their *principles* have held, but the *products* they mention have moved on. Stripe changed its release model in October 2024; OpenTelemetry graduated in May 2026; OpenAPI reached 3.2 in September 2025. The automotive engineering material is uneven: Auto Trader UK's Istio/GKE story dates from 2018–2019, Cox Automotive's AWS migration from 2016–2021. Each section gives the date of its evidence. Do not describe a dated post in the present tense without checking.

**Research limitation.** The shared web-search quota was used sparingly; most evidence comes from direct fetches of known documentation URLs. As a result:

- **mobile.de, OLX Autos, Cars.com, Keyloop, Pinewood, Reynolds and Reynolds and DAT** have **no verified primary engineering source in this brief**. mobile.de's own engineering feed could not be found; Reynolds' partner (RCI) page and DAT's interface pages returned 404; Medium feeds for Cox Automotive and CarGurus returned 404 under the guessed names.
- **CDK Global's 2023 API announcement** (BusinessWire) returned HTTP 403; Fortellis figures in this brief come from a 2020 trade article and an API directory, which disagree with each other.
- The **2024 CDK ransomware timeline** rests on trade press and Wikipedia, not on CDK filings (CDK is privately held by Brookfield and files no SEC reports of its own).
- No source was found that publishes a **real cost per API call** for any vehicle-data provider. Unit-cost figures in this brief are framework guidance or judgement.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: product names, release cadences, registration status of public APIs, draft standards, ownership.

---

## PART 1: API product design

### 1.1 What makes a vehicle-data API different from a generic SaaS API

| Property | Generic B2B SaaS API | Vehicle data and dealer SaaS API |
| --- | --- | --- |
| Primary key | Opaque resource ID chosen by the provider | **Plate (VRM/kenteken/Kennzeichen) or VIN**: public, guessable, enumerable, and often personal data |
| Cost of a call | Mostly compute | Often a **pass-through cost** to a paid upstream (history, valuation, finance, register) |
| Upstream | Own database | Registers (RDW, DVLA, DVSA, KBA, NMVTIS), OEM build data, valuation houses, portals |
| Clients | Customer developers | Dealer DMS/CRM vendors, portals, lessors, insurers, consumers, and scrapers |
| Legacy surface | Usually one API generation | XML/SOAP, flat files and STAR/ADF-style messages coexisting with JSON REST and events |
| Change tolerance | Moderate | Low: a dealer's integration is often built once by a third-party vendor and left alone |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis. The sections below give the evidence for each row.

### 1.2 Versioning and deprecation: three published models

| Model | Who | Mechanism | Deprecation promise |
| --- | --- | --- | --- |
| Date-pinned rolling versions | Stripe (2011–2024) | Account pinned to the version current at first call; per-request override header; server-side "version change modules" transform responses backwards | Compatibility kept with every version since 2011 (as of 2017) |
| Named semiannual majors + monthly non-breaking releases | Stripe (from Oct 2024) ⚠ | Breaking changes only twice a year, in a named release ("Acacia"); monthly releases add features only | Predictable cadence |
| Major version in path; stability channels | Google AIP | `v1`, `v1beta`, `v1alpha`; never minor/patch in the path | Beta: deprecation period, rule of thumb 180 days; stable: no breaking changes within a major version |
| Required date-valued `api-version` query parameter | Microsoft Azure guidelines | `api-version=YYYY-MM-DD` with `-preview` suffix | Previews may be retired after at least 90 days' notice; no preview kept longer than one year |

Sources:

- Stripe's 2017 post: "we implement versioning with rolling versions that are named with the date they're released"; "The first time a user makes an API request, their account is automatically pinned to the most recent version available"; users can override with the `Stripe-Version` header; breaking changes are encapsulated in "version change modules" that walk responses back to the target version. Stripe says it had "maintained compatibility with every version of our API since the company's inception in 2011" [VERIFIED: https://stripe.com/blog/api-versioning, published 2017-08-05]. Evidence age: 9 years; the mechanism is still the best-documented example of server-side version transformation.
- Stripe's 2024 change: "a new release cadence and versioning system for all API endpoints that combines twice-yearly major updates with monthly feature enhancements"; each major release "includes breaking changes and is named after a plant"; monthly releases add features "without breaking changes" [VERIFIED: https://stripe.com/blog/introducing-stripes-new-api-release-process, published 2024-10-01]. ⚠
- Google AIP-185: APIs "must provide a major version number"; Google APIs "must not expose minor or patch version numbers"; channel-based versioning is "recommended"; beta functionality may be removed after deprecation "for a sufficient period; we recommend 180 days" [VERIFIED: https://google.aip.dev/185, published 2024-10-22].
- Google AIP-181: breaking changes "must be both allowed and expected in alpha"; beta should be time-boxed, "a good rule of thumb is 90 days"; stable components "must be fully-supported over the lifetime of the major API version" [VERIFIED: https://google.aip.dev/181, published 2019-02-18].
- Google AIP-180: existing components "must not be removed from existing APIs in the same major version" [VERIFIED: https://google.aip.dev/180, published 2019-07-23].
- Microsoft Azure REST guidelines: "DO use a required query parameter named `api-version`"; "DO use `YYYY-MM-DD` date values, with a `-preview` suffix"; previews may be retired "after giving customers at least 90 days"; "DO NOT keep a preview feature in preview for more than 1 year"; adding paging later "is a breaking change"; required fields "can only be introduced in the 1st version of a service" [VERIFIED: https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md, n.d. (living document, changelog to 2024+), accessed 2026-10].
- HTTP signalling: the `Sunset` header indicates a URI "is likely to become unresponsive at a specified point in the future" [VERIFIED: https://www.rfc-editor.org/rfc/rfc8594.txt, published 2019-05]. The `Deprecation` response header (Standards Track) signals that a resource "will be or has been deprecated" [VERIFIED: https://www.rfc-editor.org/rfc/rfc9745.txt, published 2025-03].
- Error bodies: RFC 9457 "Problem Details for HTTP APIs" obsoletes RFC 7807 [VERIFIED: https://www.rfc-editor.org/rfc/rfc9457.txt, published 2023-07].

**Automotive evidence: Auto Trader UK Connect.** Auto Trader's public partner API platform (Vehicles, Taxonomy, Stock, Images, Search, Valuations, Vehicle Metrics, Deals, Finance and other APIs) publishes a **Breaking Change Policy**: breaking changes "will be communicated and advised at a minimum of 30 days ahead of the change". Its list of breaking changes includes removing a property, changing a status code's class (4XX to 5XX), adding mandatory request parameters and "introducing additional validation errors". Release notes show field removals staged first in sandbox and later in production, and response-shape migrations where the old root object is duplicated under a new `results` root before removal. Access tokens "expire after 15 minutes" and unused credentials are removed after 90 days [VERIFIED: https://developers.autotrader.co.uk/documentation, n.d. (release notes to 2026-09), accessed 2026-10]. ⚠ Note that 30 days is far shorter than Google's 180-day beta guidance; it is workable only because the client base is a known set of partners.

**Across markets.**

- **UK**: the strongest public examples of vehicle-data API policy (Auto Trader Connect; DVLA VES and DVSA MOT history APIs, Part 4) are UK. **NL**: RDW publishes register data through a Socrata open-data API with no versioning promise beyond dataset IDs (Part 4.3). **DE**: no comparable public developer portal was verified for DAT, mobile.de or KBA in this session. **US**: CDK's Fortellis is the main dealer-side API marketplace (1.5). **BE**: nothing verified.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]

- Choose **one** versioning model and publish it. For ~10,000 dealers reached mostly through a few hundred integrators, date-pinned versions per client credential (Stripe 2017 style) plus a version-transformation layer give the lowest upgrade burden, at the price of a permanently growing transformation chain. A path major version (`/v1`) is still worth reserving.
- Make the deprecation window a contract term, not an engineering preference: 30 days (Auto Trader) is the floor, 6–12 months is realistic for integrations built by DMS vendors that release quarterly.
- Emit `Deprecation` and `Sunset` headers and log which client credentials still call deprecated fields; deprecation without per-client telemetry is guesswork.

### 1.3 Legacy XML/SOAP coexisting with JSON

- STAR (Standards for Technology in Automotive Retail) has developed "over 200 XML message formats covering over 35 business areas"; its schema repository "is written using the W3C XML Schema Language" and uses the OAGIS Business Object Document (BOD) methodology [VERIFIED: https://www.starstandard.org/?p=488, n.d., accessed 2026-10]. STAR released XML version 6.2.4 with 36 refactored BODs (retail delivery, vehicle order, vehicle invoice, price list, shipment, specifications, dealer support case) [VERIFIED: https://www.starstandard.org/?p=4212, published 2024-09-12]. STAR's site navigation also lists "Sales-related APIs" and a "Service Scheduling API" alongside the XML BODs (same pages). STAR is a US-centred standards body; European adoption was not verified.
- NHTSA's vPIC VIN decoder serves the same operation as XML, CSV and JSON, including a batch decode of "max 50 VINs per batch" [VERIFIED: https://vpic.nhtsa.dot.gov/api/, n.d., accessed 2026-10]. This is the common public-sector pattern: one operation, several serialisations.
- [ASSUMPTION/JUDGEMENT] German valuation and repair-calculation providers (DAT, Schwacke/Autovista) and many DMS vendors historically exposed SOAP web services; their current interface documentation was not reachable in this session (DAT interface pages returned 404).

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Model the domain once (canonical JSON Schema or protobuf), and treat XML/SOAP, CSV file drops and STAR BODs as **adapters at the edge** with their own contract tests. Never let the legacy schema leak into the canonical model; a SOAP facade should be a translation service with its own deprecation clock.

### 1.4 Describing the contract: OpenAPI, JSON Schema, AsyncAPI, schema registries

- OpenAPI 3.1.0 (2021-02-15) aligned its Schema Object with JSON Schema: it is "a superset of the JSON Schema Specification Draft 2020-12" and added a top-level `webhooks` field for "incoming webhooks that MAY be received as part of this API" [VERIFIED: https://spec.openapis.org/oas/v3.1.0, published 2021-02-15]. 3.1.1 was a patch release on 2024-10-24 [VERIFIED: https://spec.openapis.org/oas/v3.1.1, published 2024-10-24]. **OpenAPI 3.2.0 was released 2025-09-19** (with 3.1.2 the same day) and adds, among other things, sections on streaming and sequential media types and server-sent events [VERIFIED: https://spec.openapis.org/oas/v3.2.0.html, published 2025-09-19]. ⚠ Tooling support for 3.2 lags.
- JSON Schema: "The current version is 2020-12! The previous version was 2019-09" [VERIFIED: https://json-schema.org/specification, n.d., accessed 2026-10].
- Confluent Schema Registry compatibility types: BACKWARD (new consumers read old data), FORWARD, FULL and their TRANSITIVE variants; "The Confluent Schema Registry default compatibility type is BACKWARD", chosen so consumers can rewind to the beginning of a topic. With BACKWARD, "upgrade all consumers before you start producing new events"; for an incompatible change, the documented route is often "a brand-new topic" [VERIFIED: https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html, n.d., accessed 2026-10].
- **Automotive evidence**: Auto Trader validates behavioural events against "Snowplow's schema registry, Iglu"; failed events go to a separate failed-events Delta table and are recovered by a PySpark pipeline [VERIFIED: https://medium.com/autotrader-engineering/recovering-failed-snowplow-events-using-a-domain-modelled-pyspark-pipeline-752e52e90109, published 2026-06-25].
- **Automotive evidence (async API description)**: an API directory lists an AsyncAPI specification for the "Fortellis Event Relay" data-plane proxy, "used by event sources to publish events into Fortellis for fan-out to subscribers" [WIDELY REPORTED: https://providers.apievangelist.com/providers/cdk-global/, 2026].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Keep three contract artefacts under version control: OpenAPI 3.1 for synchronous APIs and webhooks, AsyncAPI or registry-held schemas for event topics, and data contracts for analytical datasets (Part 3). Run breaking-change detection in CI against all three. Default event topics to BACKWARD_TRANSITIVE, not BACKWARD, when consumers include external clients you cannot force to upgrade.

### 1.5 Developer portals and API marketplaces

- CDK Global launched **Fortellis** in March 2018 as "a developer network and marketplace for APIs and apps built specifically for developers in the automotive industry". In April 2020 it hosted "24 apps and 27 active APIs" and averaged "1 million API transactions, or calls, a month" [WIDELY REPORTED: https://www.builtinchicago.org/articles/cdk-global-fortellis-automotive-industry-api-marketplace, 2020].
- A 2026 API directory profile states "135+ published APIs, 425+ marketplace apps, 82,000+ dealer integrations, and 6.7B+ API transactions per year" [WIDELY REPORTED: https://providers.apievangelist.com/providers/cdk-global/, 2026]. ⚠ The source is a third-party directory and the figures were not checked against CDK; treat them as indicative only.
- Auto Trader Connect separates production APIs from "Beta APIs" that "are experimental or beta and may be subject to further changes", keeps a deprecated-APIs page, publishes release notes, and requires integrators to complete sandbox testing before production credentials; it also states that "connecting services and IP addresses through our platform are monitored for dynamic reputation scoring and access" [VERIFIED: https://developers.autotrader.co.uk/documentation, n.d., accessed 2026-10].

**Across markets.** US dealer-side integration is shaped by DMS-vendor access programmes (Fortellis; Reynolds' RCI programme, not verified here) and by the 2017 antitrust litigation over DMS data access (Authenticom v. CDK and Reynolds, summarised in [WIDELY REPORTED: https://en.wikipedia.org/wiki/CDK_Global, 2026]). The UK has a marketplace-run partner API (Auto Trader Connect). Continental examples were not verified.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A portal is a product: self-service keys, sandbox with realistic test plates/VINs (DVLA publishes test VRNs; Part 4.3), per-client usage dashboards, changelog, status page, and a certification step before production access. For a platform whose data has pass-through cost, the portal must also show **metered spend**, not just call counts.

### 1.6 Rate limiting, quotas and metering

- The IETF `RateLimit-Policy` and `RateLimit` header fields let servers "advertise their quota policies and the current service limits, thereby allowing clients to avoid being throttled"; the draft defines problem types for quota exceeded, temporary reduced capacity and abnormal usage [VERIFIED: https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/, published 2026-05-23 (draft -11)]. ⚠ Still an Internet-Draft.
- AWS: "we use rate limiting to shape unplanned increases in traffic, but we enforce quotas ... at a per-tenant or per-workload granularity"; Amazon services use "multiple layers of admission control" [VERIFIED: https://aws.amazon.com/builders-library/fairness-in-multi-tenant-systems/, published 2020-11-13].
- Google SRE: per-customer limits provisioned "based on the negotiated usage with their customers"; client-side "adaptive throttling" makes clients self-limit when many requests are rejected; requests carry one of four criticality values [VERIFIED: https://sre.google/sre-book/handling-overload/, published 2016].
- **Automotive and register evidence**: the DVSA MOT history API publishes a quota of 500,000 requests per day, a burst limit of 10 and an average of 15 requests per second; exceeding the daily quota restricts the key "for 24 hours"; the page recommends exponential backoff [VERIFIED: https://documentation.history.mot.api.gov.uk/mot-history-api/rate-limits/, n.d., accessed 2026-10]. ⚠ The DVLA Vehicle Enquiry Service API applies limits per client usage plan *and* an overall limit across all clients, issues one API key per company, and states "Registration closed. We are currently not accepting new VES API registrations" [VERIFIED: https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html, n.d., accessed 2026-10]. ⚠
- CarGurus describes how highly concurrent Kotlin coroutines "occasionally stressed third-party APIs thus causing rate limit exceptions"; an advertising API escalated its back-off from 15 seconds up to 15 minutes; an actor pattern per external service "reduce[d] rate limit escalations to almost none" [VERIFIED: https://cargurus.dev/2023/07/19/actor-pattern-controlling-connection-pool-in-kotlin-to-honor-api-rate-limit-exceptions/, published 2023-07-19].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Distinguish three meters that are often conflated: (1) **protective rate limits** (requests/second, per client and global); (2) **commercial quotas** (lookups per month in the contract); (3) **cost meters** (upstream spend per client, per data source). The platform needs all three at the gateway, and must also apply them **outbound**: upstream registers enforce one key per company and a global limit, so the platform's own upstream budget must be shared fairly across its 10,000 tenants (an outbound token bucket per upstream, with per-tenant fair queuing).

---

## PART 2: Webhooks and event-driven integration

### 2.1 Webhooks: the published contract

| Concern | Standard Webhooks | Stripe | GitHub | Auto Trader Connect |
| --- | --- | --- | --- | --- |
| Identity | `webhook-id` (stable across retries; idempotency key) | Event ID | `X-GitHub-Delivery` (same on redelivery) | Message key + `time` field |
| Signature | HMAC-SHA256 (`v1`) or ed25519 (`v1a`) over id.timestamp.body | `Stripe-Signature`, timestamp tolerance | HMAC with webhook secret | `AutoTrader-Signature: t=…,v1=…` (HMAC-SHA256) |
| Retries | Producer retries with exponential schedule (5 s, 5 min, 30 min, 2 h, 5 h …); disable failing endpoints | Up to 3 days, exponential back-off (live) | Respond within 10 s; redeliver missed deliveries | 10 s, 30 s, 30 min after failures |
| Ordering | Not guaranteed | "doesn't guarantee ... order" | Not guaranteed | Per-message delivery; use `time` to detect superseded messages |
| Payload style | Thin vs full discussed; keep under ~20 kB | Thin (recommended) or snapshot | Full | Full state ("Stock Notifications") |

Sources:

- Standard Webhooks spec: headers `webhook-id`, `webhook-timestamp`, `webhook-signature`; HMAC-SHA256 with a 24–64-byte secret prefixed `whsec_`, or ed25519; key rotation by sending two signatures; consumers should check the timestamp "within some allowable tolerance ... to prevent replay attacks" and "use the `webhook-id` header as an idempotency key"; an example retry schedule; "recommended to disable future delivery to the endpoint" after prolonged failure; payloads "usually smaller than 20kb"; a section on SSRF recommending an egress proxy "that filters internal IP addresses" and isolated webhook workers [VERIFIED: https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md, n.d., accessed 2026-10]. Its steering committee includes engineers from Zapier, Twilio, Lob, Mux, ngrok, Supabase, Svix and Kong [VERIFIED: https://www.standardwebhooks.com/, n.d., accessed 2026-10].
- Stripe: "Stripe attempts to deliver events to your destination for up to three days with an exponential back off in live mode"; "Stripe doesn't guarantee the delivery of events in the order that they're generated"; "Don't use created to determine event order"; return 2xx "before any complex logic"; recommends IP allowlisting plus signature verification; offers "Thin (recommended) or Snapshot" payloads [VERIFIED: https://docs.stripe.com/webhooks, n.d., accessed 2026-10]. ⚠ Thin events are a recent shift.
- GitHub: respond "with a 2XX response within 10 seconds"; use a queue to process asynchronously; "If your server goes down, you should redeliver missed webhooks"; `X-GitHub-Delivery` stays the same on redelivery [VERIFIED: https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks, n.d., accessed 2026-10].
- **Auto Trader Connect notifications** (Stock, Deal and other notifications): "Any non 2** series response code from the endpoint is considered a retryable error"; retries at 10 seconds, 30 seconds and 30 minutes; "Delivery is tracked on a per message basis, if two messages for the same key are scheduled to be sent, first one fails and the second succeeds, the first message will still be retried regardless. For use cases only interested in the latest state, implementations should store and use the time field in the message to decide if it's relevant or has been superseded." Payloads are signed with an `AutoTrader-Signature` header built with HMAC-SHA256 and a 40-character secret [VERIFIED: https://developers.autotrader.co.uk/documentation, n.d., accessed 2026-10]. This is the clearest published automotive statement of the out-of-order problem.
- OpenAPI 3.1 can describe webhooks in the same document as the API (`webhooks` field) [VERIFIED: https://spec.openapis.org/oas/v3.1.0, published 2021-02-15].

**Across markets.** No market-specific rule governs webhooks. Lead delivery to US dealers still commonly uses ADF/XML over email (covered in the leads brief); webhooks are the modern replacement in UK and continental portal APIs. [ASSUMPTION/JUDGEMENT]

**Architecture implications.** [ASSUMPTION/JUDGEMENT]

- Adopt Standard Webhooks headers and signing rather than inventing a scheme; it costs nothing and gives integrators library support.
- Assume **at-least-once, unordered** delivery and say so in the contract. Give every event a monotonic per-entity version (or `time` as Auto Trader does) so receivers can drop superseded messages.
- Ship a **replay API** and a delivery log per endpoint; at 10,000 dealers, some DMS endpoint is always down.
- Run webhook senders behind an SSRF-filtering egress proxy; dealer-supplied URLs are attacker-controllable input.
- Prefer **thin events plus fetch** for anything containing personal data (buyer details in leads and deals): access is then authorised and auditable at fetch time.

### 2.2 Reliable publishing: transactional outbox and CDC

- The transactional outbox pattern addresses "How to atomically update the database and send messages to a message broker?" when 2PC "is not an option"; its relay "might publish a message more than once ... As a result, a message consumer must be idempotent, perhaps by tracking the IDs of the messages that it has already processed"; relays are built by transaction-log tailing or polling [VERIFIED: https://microservices.io/patterns/data/transactional-outbox.html, n.d., accessed 2026-10].
- Debezium's outbox event router expects an outbox table with `id`, `aggregatetype`, `aggregateid`, `type` and `payload`; `aggregatetype` selects the topic; `aggregateid` becomes the Kafka message key, "important for maintaining correct order in Kafka partitions"; the event `id` is placed in a header for de-duplication [VERIFIED: https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html, n.d., accessed 2026-10].
- **Marketplace evidence (adjacent)**: Kleinanzeigen, "Germany's leading second-hand marketplace" and an Adevinta brand, built a migration pipeline with Debezium CDC from MySQL into Kafka, using a compacted topic, at "a throughput of 3000 events per second" [VERIFIED: https://adevinta.com/techblog/make-data-migration-easy-with-debezium-and-apache-kafka/, published 2025-01-28]. [ASSUMPTION/JUDGEMENT] Kleinanzeigen is not an automotive marketplace, but it shares group ownership with mobile.de, so its integration tooling is a reasonable proxy.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Every state change that leaves the service boundary (stock updated, price changed, lead created, valuation produced) is written to an outbox in the same transaction and relayed by CDC. Key events by the aggregate (stock item ID, not dealer ID) so per-vehicle order is preserved while dealer-level throughput spreads across partitions. Raw table-level CDC is for internal migration and analytics, not for external contracts: it couples consumers to your schema.

### 2.3 Idempotent consumers and idempotent APIs

- Stripe implements idempotency "on mutating endpoints ... by allowing clients to pass a unique value in with the special Idempotency-Key header" [VERIFIED: https://stripe.com/blog/idempotency, published 2017-02-22].
- The IETF draft standardising an `Idempotency-Key` header is listed as "Expired" (latest -07) [VERIFIED: https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/, n.d., accessed 2026-10]. ⚠ The header is a de facto convention, not a standard.
- Standard Webhooks, Stripe and GitHub all tell receivers to de-duplicate on the delivery or event ID (2.1 sources).

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Require `Idempotency-Key` on every POST that has a cost or side effect (paid history report, stock creation, lead submission, finance application). Store key → result for at least the client retry horizon (24–72 hours). For paid upstream lookups, idempotency is a **cost control**, not only a correctness control: a retried "buy report" must not buy twice.

### 2.4 Event envelopes: CloudEvents

- CloudEvents was started by the CNCF Serverless Working Group in May 2018 and **graduated on 2024-01-25**; adopters listed include Azure Event Grid, Google Cloud Eventarc, Alibaba Cloud EventBridge and Adobe I/O Events [VERIFIED: https://www.cncf.io/announcements/2024/01/25/cloud-native-computing-foundation-announces-the-graduation-of-cloudevents/, published 2024-01-25].
- Required attributes are `id`, `source`, `specversion` (value `1.0`) and `type`; "Producers MUST ensure that `source` + `id` is unique for each distinct event"; the optional `subject` supports filtering when middleware cannot read the payload; bindings exist for HTTP, AMQP, MQTT, Kafka and NATS [VERIFIED: https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md, n.d. (spec 1.0.x), accessed 2026-10].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Use the CloudEvents envelope on internal topics and on webhooks (`subject` = VIN or stock ID, plus a tenant extension attribute). It makes routing, filtering and tenant-aware telemetry possible without parsing payloads, and costs only a few header fields.

---

## PART 3: Ingestion, data quality and entity resolution

### 3.1 Batch versus streaming

- Jay Kreps, 2014: in the Lambda Architecture, "Keeping code written in two different systems perfectly in sync was really, really hard"; he proposes reprocessing by replaying the log through a second instance of the same streaming job: "Maybe we could call this the Kappa Architecture" [VERIFIED: https://www.oreilly.com/radar/questioning-the-lambda-architecture/, published 2014-07-02]. Evidence age: 12 years; the reprocessing argument still stands.
- Databricks' medallion pattern: Bronze (raw), Silver (cleaned, standardised, "more 3rd-Normal Form like"), Gold (consumption-ready, de-normalised aggregates), also called "multi-hop" [VERIFIED: https://www.databricks.com/glossary/medallion-architecture, n.d., accessed 2026-10].
- **Automotive evidence**: Auto Trader built "an in-house customer data platform in 2021" in Java that ingests Snowplow events via Kafka; it is moving segment logic to Python ML models "deployed in real-time using Spark Structured Streaming", with profile state materialised in Bigtable behind "low-latency read APIs" [VERIFIED: https://medium.com/autotrader-engineering/real-time-personalisation-on-autotrader-50d0cda4b778, published 2026-08-06].
- **Automotive evidence**: AutoScout24's DataRunner (2023) is built on "AWS Glue, AWS Athena, Airflow, Git, Jenkins, Python, PySpark", integrated with DataHub and Great Expectations, to promote "decentralized ownership" and "data as product" [VERIFIED: https://tech.autoscout24.com/blog/posts/datarunner/, published 2023-09-25].
- **Automotive evidence**: Cox Automotive "builds data products from their S3 aggregated data", used "from analytics to powering vehicle valuations in Kelley Blue Book or Autotrader"; internal builders "can get petabytes of data from the Cox Automotive Data Marketplace" [VERIFIED: https://aws.amazon.com/blogs/storage/adapting-to-change-with-data-patterns-on-aws-the-curate-cloud-data-pattern/, published 2024-12-20]. This is AWS-authored material about a customer; treat accordingly.

| Workload in a vehicle-data platform | Natural mode | Why |
| --- | --- | --- |
| Register bulk files (RDW open data, MOT bulk downloads, KBA statistics) | Batch | Published as files or full datasets on a schedule |
| Dealer stock feeds (DMS exports, CSV/XML drops) | Micro-batch | Arrive as periodic snapshots; need diffing |
| Stock/price changes inside the platform, leads | Streaming | Seconds matter for syndication and lead response |
| Valuation model training, market insight | Batch | Needs full history; daily cadence is sufficient |
| Live plate/VIN lookup | Request/response + cache | Latency-sensitive, paid per call |

[ASSUMPTION/JUDGEMENT] Table is the analyst's synthesis.

**Across markets.** [ASSUMPTION/JUDGEMENT] NL and UK expose much register data as APIs or bulk downloads, which favours scheduled batch plus on-demand lookup. Germany's register data is not openly available for individual vehicles, so DE platforms depend more on commercial providers (DAT, Schwacke) and OEM data. US platforms ingest NMVTIS-derived and auction/transaction feeds through commercial aggregators.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Keep the log (Kafka or equivalent) as the system of record for change, land everything in Bronze unchanged, and make every Silver/Gold job re-runnable from Bronze. That gives Kappa-style reprocessing for corrections (a register correction, a recalled odometer reading) without a second code path.

### 3.2 Data contracts, quality checks and freshness

- A data contract "defines the ownership, structure, semantics, quality, and terms of use for exchanging data between a data producer and their consumers. Think of an API, but for data" [VERIFIED: https://www.datamesh-manager.com/learn/what-is-a-data-contract, published 2023-11-26].
- The Open Data Contract Standard (ODCS) is maintained by Bitol, which describes itself as a Linux Foundation AI & Data project; the Bitol site (accessed 2026-10) announces ODCS v3.1.0, the joint release of ODCS v3.2.0 with ODPS v1.1.0, and Bitol's graduation in LF AI & Data [VERIFIED: https://bitol.io/, n.d., accessed 2026-10]. ⚠ Exact dates of those announcements were not captured. ODCS covers schema, data quality, pricing, team, roles, SLA and infrastructure sections [VERIFIED: https://bitol-io.github.io/open-data-contract-standard/latest/, n.d., accessed 2026-10].
- Great Expectations: "An Expectation is a verifiable assertion about data", grouped into Expectation Suites and run by Checkpoints [VERIFIED: https://docs.greatexpectations.io/docs/reference/learn/terms/expectation, n.d. (0.18 docs; GX 1.x is current), accessed 2026-10].
- Soda freshness checks "infer data freshness according to the age of the most recently added row in a table", with warn and fail thresholds (e.g. `freshness(start_date) < 27h`) [VERIFIED: https://docs.soda.io/soda-cl/freshness.html, n.d. (Soda v3 docs), accessed 2026-10].
- OpenLineage is "an open framework for data lineage collection and analysis" with a model of dataset, job and run entities extended by facets; RunEvents are emitted at runtime, Job/DatasetEvents at design time [VERIFIED: https://openlineage.io/docs/spec/object-model, n.d. (v1.54.0), accessed 2026-10].
- **Automotive evidence**: Auto Trader quarantines events that fail schema validation into a failed-events table rather than dropping them, then recovers them with a pipeline that conforms them to the target schema (1.4 source).

**Architecture implications.** [ASSUMPTION/JUDGEMENT]

- Write a contract for every **external source** as well as every internal dataset: what an RDW extract, a DVSA MOT record or a valuation file must contain, its expected arrival time and its volume range. Upstream schema drift is the most common silent failure in vehicle data.
- Set **freshness SLOs per source and per product**: "MOT history no older than 24 h", "dealer stock no older than 15 min after DMS export", "valuation model inputs no older than 7 days". Alert on the SLO, not on job failures.
- Quarantine, do not drop: a dead-letter table plus a replay tool turns schema breaks into a backlog instead of data loss.
- Emit lineage so that a recalled odometer reading or a wrong register attribute can be traced to every report and valuation that used it.

### 3.3 Entity resolution at scale

- Fellegi and Sunter, "A Theory for Record Linkage", *Journal of the American Statistical Association* 64(328): 1183–1210, December 1969 [VERIFIED: https://api.crossref.org/works/10.1080/01621459.1969.10501049, published 1969-12] (metadata fetched; the paper itself is paywalled).
- Splink is "a Python package for probabilistic record linkage (entity resolution) ... from datasets without unique identifiers", based on "Fellegi-Sunter's model of record linkage"; claims of "linking a million records on a laptop in approximately one minute" and Spark backends "for 100+ million records"; "No training data is required" (unsupervised training); used by the UK Ministry of Justice, Ministry of Defence and others; one listed user links about "30 Million records in less than 5 hours" on Databricks [VERIFIED: https://moj-analytical-services.github.io/splink/index.html, n.d., accessed 2026-10]. Citation: Linacre et al., "Splink: Free software for probabilistic record linkage at scale", *International Journal of Population Data Science* 7(3), 2022, doi:10.23889/ijpds.v7i3.1794 (same page).
- **Automotive evidence (consumer identity, not vehicle identity)**: Cox Automotive's Consumer Insights team chose an identity graph on Amazon Neptune in October 2019 for "householding and lead mapping" across business units; "approximately 0.5 billion edges and 0.4 billion vertices"; the householding process "creates a full data set every day" in S3 [VERIFIED: https://aws.amazon.com/blogs/database/cox-automotive-scales-digital-personalization-using-an-identity-graph-powered-by-amazon-neptune/, published 2020-09-17]. Evidence age: 6 years.

**Across markets.** [ASSUMPTION/JUDGEMENT] Vehicle identity is easier where a VIN is reliably present (US, OEM build data, EU type-approved vehicles post-1981) and harder in advert and dealer-stock data, where VINs are often missing or masked and plates change (UK personalised plates, NL plate transfers are rare but DE plates change on re-registration). Dealer identity (one group, many rooftops, many portal accounts) and consumer identity (leads across portals) are the other two resolution problems, and consumer linkage is constrained by GDPR in all four European markets.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Resolve three entity types separately: **vehicle** (VIN deterministic first, then plate+make+model+first-registration probabilistic), **dealer/rooftop** (company registry number, address, portal IDs), **consumer** (only where lawful basis exists). Keep match decisions, scores and the model version as data, so a bad merge can be undone and its downstream reports reissued.

---

## PART 4: Reliability with external dependencies

### 4.1 Timeouts, retries, backoff and jitter

- Amazon sets timeouts by choosing "an acceptable rate of false timeouts (such as 0.1%)" and using the matching downstream latency percentile (p99.9); "Retries are 'selfish'"; "our best practice is to retry at a single point in the stack"; circuit breakers "introduce modal behavior into systems that can be difficult to test", so Amazon limits retries locally "using a token bucket", added to the AWS SDK in 2016 [VERIFIED: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/, published 2019-12-05].
- Brooker's simulation compared "Full Jitter", "Equal Jitter" and "Decorrelated Jitter"; un-jittered exponential backoff "is the clear loser"; a 2023 update says the approach "continues to serve as a pillar for how Amazon builds remote client libraries" [VERIFIED: https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/, published 2015-03-04].
- Google SRE: "a per-request retry budget of up to three attempts" plus "a per-client retry budget": retry only while retries are below 10% of requests, which caps growth at about 1.1x instead of 3x [VERIFIED: https://sre.google/sre-book/handling-overload/, published 2016]. Deadline propagation: a deadline set at the top of the stack shrinks as it passes down [VERIFIED: https://sre.google/sre-book/addressing-cascading-failures/, published 2016].
- Circuit breaker states closed, open and half-open (trial call after a reset timeout) [VERIFIED: https://martinfowler.com/bliki/CircuitBreaker.html, published 2014-03-06].
- OWASP API10:2023 lists, among unsafe consumption of third-party APIs, an API that "Does not implement timeouts for interactions with third-party services" and that trusts third-party data more than user input [VERIFIED: https://owasp.org/API-Security/editions/2023/en/0xaa-unsafe-consumption-of-apis/, published 2023].

### 4.2 Avoiding fallback; bulkheads; load shedding

- Amazon "often avoids fallback logic" because fallback "is hard to test", is entered "only in the most chaotic moments", and may lie dormant for years; preferred alternatives: retry, proactive retry (hedging), failover, and "pushing data to systems that need it instead of pulling and risking failure of a remote call at a critical time" [VERIFIED: https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems/, published 2019-12-05].
- Load shedding is "the act of cheaply rejecting work instead of spending limited resources on it" [VERIFIED: https://aws.amazon.com/builders-library/fairness-in-multi-tenant-systems/, published 2020-11-13]; the companion article explains why throughput degrades under overload [VERIFIED: https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/, published 2019-12-05].
- AWS SaaS Lens: a noisy neighbour is a user whose load "could have an adverse effect on other users", a concern with "expanded relevance in a multi-tenant environment" [VERIFIED: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/noisy-neighbor.html, n.d., accessed 2026-10]. Silo, pool and mixed full-stack deployment models, e.g. basic tiers pooled and premium tiers siloed, all on the same software version [VERIFIED: https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/full-stack-silo-and-pool.html, published 2022-08-03] (marked "for historical reference only").

**Architecture implications for paid and public upstreams.** [ASSUMPTION/JUDGEMENT]

| Upstream type | Failure behaviour to design for | Recommended pattern |
| --- | --- | --- |
| Public register API (DVLA, DVSA, RDW) | Rate limit, daily quota lock-out (DVSA: 24 h), closed registrations | Outbound token bucket per key; bulk-download mirror where licensed; never let a tenant burst exhaust the shared key |
| Paid history/valuation provider | Per-call cost, contractual cache limits, slow tail latency | Single retry point, idempotent purchase, hedged reads only for free endpoints, per-tenant spend caps |
| DMS integration | Vendor outage, credential revocation, antitrust-sensitive access | Bulkhead per DMS vendor (separate pools and queues), push-based sync where offered |
| Portals (syndication targets) | Throttling, schema changes, per-portal semantics | Per-portal queues and circuit breakers; replay from outbox |

- **Bulkheads**: separate worker pools, queues and connection pools per upstream and per tenant tier, so a slow valuation provider cannot exhaust threads used for lead delivery.
- **Avoid fallback to a different provider at runtime** unless that path runs continuously (e.g. shadow traffic). A rarely used second valuation source will be wrong exactly when it is needed.
- **Push, do not pull**, where licensing allows: mirror register datasets (RDW open data, MOT bulk files) into the platform so that a lookup does not depend on a remote call.

### 4.3 Caching third-party paid data and contractual limits

- Caching failure modes at Amazon: cold caches after deployments, cache-fleet failures that send "a surge of traffic to downstream services", and the need for a **negative cache** "using a different TTL than positive cache entries"; "We have seen real-world examples in which a failure to cache negative responses led to increased failure rates"; soft/hard TTL to serve the last good value [VERIFIED: https://aws.amazon.com/builders-library/caching-challenges-and-strategies/, published 2019-12-05].
- Contract-limited caching is standard in data licences. Example from a non-automotive provider: Google's Places API "must not pre-fetch, cache, or store Places API content beyond the allowed exceptions", while place IDs may be stored indefinitely [VERIFIED: https://developers.google.com/maps/documentation/places/web-service/policies, n.d. (updated 2026-10-21), accessed 2026-10].
- RDW's open register dataset is served by a Socrata endpoint (response headers include `X-Socrata-Region: aws-eu-west-1-prod` and `X-SODA2-Truth-Last-Modified`), exposing fields such as `kenteken`, `vervaldatum_apk` (MOT expiry), `openstaande_terugroepactie_indicator` (open recall) and `tellerstandoordeel` (odometer judgement) [VERIFIED: https://opendata.rdw.nl/resource/m9d7-ebf2.json, n.d. (live API, last modified 2026-10-22), accessed 2026-10]. Socrata throttles requests without an app token by IP, and grants each app token "their own pool of API requests" [VERIFIED: https://dev.socrata.com/docs/app-tokens.html, n.d., accessed 2026-10].
- vPIC: "Users/Applications attempting to use vPIC APIs will be controlled by an automated traffic rate control mechanism"; NHTSA also offers standalone downloadable vPIC databases [VERIFIED: https://vpic.nhtsa.dot.gov/api/, n.d., accessed 2026-10].

**Across markets.** [ASSUMPTION/JUDGEMENT] NL register data (RDW) is open data and can generally be mirrored; UK DVLA/DVSA data is available under per-key API terms (and VES registrations are currently closed); DE KBA vehicle-level data is not openly available; US vPIC decoding data is downloadable, while history data (NMVTIS, Carfax, AutoCheck) is licensed per report with resale and caching restrictions set by contract. Chapter writers should check each licence; this brief did not verify specific commercial cache clauses.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Tag every cached record with **source, licence, fetch time and permitted TTL**, and enforce TTLs per source in the cache layer, not in application code. Separate "facts we may keep" (decoded VIN specification, our own derived valuations) from "facts we rent" (third-party history report content). Cache negative answers ("no MOT record", "plate not found") with a short TTL to stop enumeration traffic from becoming upstream spend.

### 4.4 SLOs and error budgets

- An SLI is "a carefully defined quantitative measure of some aspect of the level of service"; use percentiles because the "99th or 99.9th, shows you a plausible worst-case value"; "It's both unrealistic and undesirable to insist that SLOs will be met 100% of the time" — use an error budget; Chubby's planned outages illustrate the risk of being *more* reliable than promised [VERIFIED: https://sre.google/sre-book/service-level-objectives/, published 2016].
- **Automotive evidence**: AutoScout24 defines **Critical User Interactions (CUIs)** per journey, e.g. "Buyer browses and filters cars", "Dealer is contacted by a Buyer about a car"; SLOs are managed with Terraform and Datadog, tagged by cui, journey, team, service and system; error budgets are translated into KPI impact (e.g. lost leads) for management. The post lists earlier failure modes: SLOs on technical metrics only, unclear scope, little product-manager involvement, abandoned SLOs [VERIFIED: https://tech.autoscout24.com/blog/posts/slos-for-critical-user-interactions/, published 2024-09-03].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Define SLOs on dealer and API-client journeys (stock published to portals within N minutes; lead delivered to DMS within N seconds; plate lookup p99 < N ms; valuation available), and **separate upstream-caused errors** in the SLI so that error budgets drive the right conversation (fix our code vs renegotiate a provider).

---

## PART 5: Cost management

- The FinOps Framework organises capabilities into domains (Understand Usage & Cost; Quantify Business Value; Optimize Usage & Cost; Manage the FinOps Practice) and phases Inform, Optimize and Operate [VERIFIED: https://www.finops.org/framework/, n.d., accessed 2026-10].
- Unit Economics "brings together what an organization spends on technology and the value that technology spending creates"; it distinguishes **resource-efficiency unit metrics** (cost per GB, per vCPU, per token) from **business unit metrics** ("cost per tenant, cost per transaction, cost to serve"); mature practice uses fully loaded costs and lets unit economics shape "build vs buy, architecture ... and pricing decisions" [VERIFIED: https://www.finops.org/framework/capabilities/unit-economics/, n.d., accessed 2026-10].
- Allocation uses "account structures, tags, labels and derived metadata", with a shared-cost strategy and showback/chargeback [VERIFIED: https://www.finops.org/framework/capabilities/allocation/, n.d., accessed 2026-10].
- OWASP API4:2023 lists "Third-party service providers' spending limit" among the limits whose absence makes an API vulnerable; its example is a cloud bill rising "from US$13, on average, to US$8k" for lack of cost alerts [VERIFIED: https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/, published 2023].
- **Automotive evidence**: AutoScout24 reports that moving from cluster-autoscaler to Karpenter cut "EC2 usage costs for the Kubernetes cluster ... by almost 50%" against a 15% goal, but observability (Datadog custom metrics) costs rose [VERIFIED: https://tech.autoscout24.com/blog/posts/impact-of-karpenter/, published 2024-09-09]. Auto Trader reported "75 percent more efficient" CPU/RAM usage after moving to GKE with Istio [VERIFIED: https://cloud.google.com/customers/auto-trader-uk/, n.d. (c. 2019), accessed 2026-10] (vendor case study).
- AutoScout24 built an AI "FinOps" teammate that reports AWS and coding-agent costs from Slack [VERIFIED: https://tech.autoscout24.com/, listing dated 2026-09-15, accessed 2026-10]. ⚠

**Architecture implications.** [ASSUMPTION/JUDGEMENT]

- For a vehicle-data platform the dominant marginal cost is often **not cloud compute but upstream data**: a paid history check or valuation can cost more than a month of compute for the request path. Unit economics must therefore be **cost per product call = compute + upstream fee + amortised licence + support**, computed per client and per product.
- Meter at the gateway with tenant, client, product and upstream tags on every request and propagate those tags into the billing pipeline and into cloud cost allocation.
- Set per-tenant and per-client **spend caps** that trip before the invoice does, mirroring OWASP's "spending limit".
- Watch telemetry cost: per-tenant labels on metrics can explode cardinality (Part 7) and Datadog-style billing.

---

## PART 6: Security of APIs, scraping and ransomware

### 6.1 OWASP API Security Top 10 (2023)

The 2023 list: API1 Broken Object Level Authorization; API2 Broken Authentication; API3 Broken Object Property Level Authorization; API4 Unrestricted Resource Consumption; API5 Broken Function Level Authorization; API6 Unrestricted Access to Sensitive Business Flows; API7 Server Side Request Forgery; API8 Security Misconfiguration; API9 Improper Inventory Management; API10 Unsafe Consumption of APIs [VERIFIED: https://owasp.org/API-Security/editions/2023/en/0x11-t10/, published 2023].

- **BOLA with a VIN**: OWASP's own API1 scenario is automotive: a manufacturer's remote-control API takes the VIN from the user and "fails to validate that the VIN represents a vehicle that belongs to the logged in user, which leads to a BOLA vulnerability". Prevention: check authorisation "in every function that uses an input from the client to access a record", prefer "random and unpredictable values as GUIDs" for record IDs [VERIFIED: https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/, published 2023].
- **Business-flow abuse**: API6 covers automated abuse of legitimate flows (scalping, spam, reserving all slots); countermeasures include device fingerprinting, human detection and "non-human patterns", and the risk is noted to be high for "APIs that are consumed directly by machines (such as developer and B2B APIs)" [VERIFIED: https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/, published 2023].
- **Scraping**: OWASP OAT-011 Scraping — "Collect application content and/or other data for use elsewhere", "for subsequent use such as exploitation of proprietary data, or price-fixing"; scrapers "may attempt to read all accessible paths and parameter values" [VERIFIED: https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-011_Scraping, n.d., accessed 2026-10].
- **Plate as personal data**: the DVLA VES API takes the registration number in a POST body because "The vehicle registration number is deemed sensitive information in accordance with the Information Commissioner's Office (ICO)" and OWASP guidance says sensitive data should not be in URLs (avoids web-server logs) [VERIFIED: https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html, n.d., accessed 2026-10].

**Why plate lookups are an enumeration risk.** [ASSUMPTION/JUDGEMENT] Plates and VINs are not secrets: they are printed on the car and in adverts, and their formats are structured, so the key space can be walked. A lookup endpoint that returns history, valuation or finance status for any plate is therefore a **bulk data-extraction interface** unless metered. The control is not hiding the identifier but (1) authenticating every caller, (2) tying each call to a purpose and a contract quota, (3) detecting sequential or high-cardinality plate patterns per client, (4) returning only the fields the product licence covers, and (5) never echoing plates in URLs or logs.

**Across markets.** [ASSUMPTION/JUDGEMENT] In the UK the ICO treats VRNs as personal data (DVLA statement above). Under GDPR in NL, BE and DE, a plate linked to an identifiable keeper is likewise personal data; RDW's open dataset deliberately omits keeper identity. In the US, the Driver's Privacy Protection Act restricts disclosure of personal information from DMV records (not verified in this session; see the regulatory brief).

### 6.2 Bot and scraping defence for a vehicle-data platform

[ASSUMPTION/JUDGEMENT], drawing on OWASP API6/OAT-011 and the Auto Trader "IP reputation validation" note (1.5):

- Layered admission control: edge WAF and bot management → API gateway authentication and quotas → per-client behavioural detection (sequential plates, unusual make/model distributions, lookups without follow-on purchases) → cost caps.
- Separate consumer-facing free lookups (cheap, heavily cached, minimal fields) from B2B lookups (authenticated, contracted, full fields).
- Watermark or seed datasets (canary vehicles) to detect resale of scraped data.

### 6.3 Ransomware resilience and the 2024 CDK attack

- CISA/MS-ISAC/NSA/FBI #StopRansomware Guide (September 2023 update of the September 2020 guide): "Maintain offline, encrypted backups of critical data, and regularly test the availability and integrity of backups"; backups must be offline because "many ransomware variants attempt to find and subsequently delete or encrypt accessible backups"; maintain "golden images"; use infrastructure as code with offline copies of templates; consider immutable storage "with caution"; implement "phishing-resistant MFA for all services" [VERIFIED: https://www.cisa.gov/stopransomware/ransomware-guide, published 2023-09].
- **Industry context (brief)**: CDK Global, whose DMS platform is used by "15,000+ car dealerships across North America", suffered an attack starting the night of 18 June 2024 and a second incident late on 19 June, after which it shut down most systems and advised customers to shut down DMS access [WIDELY REPORTED: https://www.helpnetsecurity.com/2024/06/20/cdk-cyberattack/, 2024]. Dealers connected through always-on VPNs to CDK data centres [WIDELY REPORTED: https://www.bleepingcomputer.com/news/security/cdk-global-cyberattack-impacts-thousands-of-us-car-dealerships, 2024]. Secondary summaries attribute the attack to BlackSuit, report a ransom payment, and state that by 4 July 2024 access for nearly all dealers had been restored; J.D. Power estimated June 2024 US retail unit sales could fall up to 7.2% year on year because of the outage [WIDELY REPORTED: https://en.wikipedia.org/wiki/CDK_Global, 2026]. Treat ransom amount and attribution as reported, not confirmed.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A dealer SaaS platform is a **concentration risk** for its customers: one compromise stops thousands of businesses. Design for it explicitly: tenant-isolated credentials and data keys; no flat network trust between dealer sites and the platform (the VPN-to-data-centre pattern spreads blast radius); immutable, offline-tested backups with restore drills measured against an RTO per product; a documented **degraded mode** for dealers (read-only stock, offline deal paperwork, export of today's data); and pre-agreed customer communication. Fallback here is justified because the alternative is total outage, but it must be exercised regularly (4.2).

---

## PART 7: Observability and tenant-aware telemetry

- OpenTelemetry was accepted to CNCF on 2019-05-07, moved to Incubating on 2021-08-26 and **graduated on 2026-05-11** [VERIFIED: https://www.cncf.io/projects/opentelemetry/, n.d., accessed 2026-10]. ⚠
- OTel Baggage propagates request-scoped context such as "Account Identification, User IDs, Product IDs" across services; but "Sensitive Baggage items can be shared with unintended resources, like third-party APIs" because "automatic instrumentation includes Baggage in most of your service's network requests"; baggage has no integrity checks and is not automatically added to span attributes [VERIFIED: https://opentelemetry.io/docs/concepts/signals/baggage/, n.d., accessed 2026-10].
- Metrics cardinality: seven attributes with 30 values each can produce "21,870,000,000 combinations ... This cardinality explosion is a well-known challenge" [VERIFIED: https://opentelemetry.io/docs/specs/otel/metrics/supplementary-guidelines/, n.d., accessed 2026-10].
- **Automotive evidence**: AutoScout24's platform team runs Kubernetes on EKS, deploys via ArgoCD (one Application manifest per service), uses Grafana and Loki for logs, and restricts direct cluster access for some clusters "for compliance reasons"; it built an AI agent to diagnose failing services from Slack [VERIFIED: https://tech.autoscout24.com/blog/posts/ai-debug-agent-infinity-platform/, published 2026-07-20]. ⚠ The 2024 SLO post used Datadog (4.4); both may be in use.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]

- Put `tenant.id`, `client.id` and `product` on **traces and logs** (high cardinality is cheap there) but only `tenant.tier` and `product` on **metrics**; compute per-tenant views from traces or logs. Ten thousand dealer IDs as a metric label times endpoints times status codes is a cardinality bill.
- Strip baggage at the egress proxy before calls to upstream providers and webhook receivers; tenant and consumer IDs must not leak to third parties.
- Never record plates, VINs tied to consumers, or buyer contact details in span attributes; hash or tokenise them.

---

## PART 8: What automotive platforms publicly describe

| Company | What is public | Date of evidence | Source |
| --- | --- | --- | --- |
| Auto Trader UK | ~50 customer-facing apps, ~400 microservices, >30,000 req/s on GKE with Istio; migration to public cloud since 2018, motivated by GDPR and service-to-service mTLS | 2018–2021 (case study) | [VERIFIED: https://istio.io/latest/about/case-studies/autotrader/, n.d., accessed 2026-10] |
| Auto Trader UK | Deploy time from up to 10 minutes on private cloud to as low as 20 seconds on GKE; "75 percent more efficient" usage | c. 2019 | [VERIFIED: https://cloud.google.com/customers/auto-trader-uk/, n.d., accessed 2026-10] |
| Auto Trader UK | Snowplow → Kafka → Spark Structured Streaming → Bigtable profile service; GCS Delta tables; Iglu schema registry; Connect partner APIs with signed webhooks | 2026 | 1.4, 2.1, 3.1 sources |
| AutoScout24 | EKS + Karpenter (≈50% EC2 saving); ArgoCD; Grafana/Loki; SLOs on Critical User Interactions with Terraform + Datadog; DataRunner (Glue, Athena, Airflow, Great Expectations, DataHub); merged 110 AWS accounts from Trader into its AWS organisation (2025-08-21); "over 170 engineers", "1000+ Github Repositories" | 2023–2026 | [VERIFIED: https://tech.autoscout24.com/, n.d., accessed 2026-10] and posts cited above |
| Cox Automotive | Began a "concentrated migration to the cloud" on AWS in 2016; Well-Architected reviews; S3-based Data Marketplace feeding KBB and Autotrader valuations; Neptune identity graph | 2016–2024 | [VERIFIED: https://aws.amazon.com/solutions/case-studies/cox-automotive-case-study/, n.d. (c. 2021), accessed 2026-10]; 3.1, 3.3 sources |
| CarGurus | Monolith decomposition from early 2019 via Strangler Fig; moved from Java serialization to JSON messages to decouple producers and consumers; containers then Kubernetes; internal deployment platform "Mach5" over Kubernetes namespaces | 2023 | [VERIFIED: https://cargurus.dev/2023/02/27/decomposition-journey-at-cargurus-from-monolith-to-microservices/, published 2023-02-27]; [VERIFIED: https://cargurus.dev/2023/03/27/how-cargurus-is-supercharging-our-microservice-developer-experience/, published 2023-03-27] |
| Adevinta (mobile.de's group) | SCHIP: "a multi-tenant, multi-region Kubernetes distribution for Adevinta developers", upgraded by blue-green cluster migration; Kleinanzeigen Debezium/Kafka pipeline | 2023–2025 | [VERIFIED: https://adevinta.com/techblog/unpacking-the-complexities-of-kubernetes-upgrades-beyond-the-one-click-update/, published 2023-09-27]; 2.2 source |
| CDK Global | Fortellis API marketplace (2018–); async/event APIs; 2024 ransomware outage | 2020–2026 | 1.5, 6.3 sources |
| mobile.de, OLX Autos, Cars.com | No platform write-up verified in this session | — | Gap |

**Evidence-age warning.** The Auto Trader GKE/Istio facts are 6–8 years old and come from vendor case studies; the current state of Auto Trader's platform is not described in its 2026 posts read here. Cox Automotive's material is AWS-authored. Treat both as dated snapshots.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The public pattern across European automotive marketplaces is consistent: managed Kubernetes on one hyperscaler, GitOps deployment, a log (Kafka) for behavioural and change events, a lakehouse or warehouse for analytics, journey-level SLOs, and an internal platform team that hides cluster details from product engineers. None of these companies describes a multi-cloud runtime. A vehicle-data and dealer SaaS platform at ~10,000 dealers is smaller than Auto Trader's consumer marketplace in request volume but has **more external integrations per tenant**, so its platform investment should tilt toward integration operations (delivery logs, replay, per-upstream budgets) rather than raw scale.

---

## PART 9: Reference sizing for ~10,000 dealers plus API clients

[ASSUMPTION/JUDGEMENT] Illustrative arithmetic for chapter writers; replace with the book's scenario figures.

| Quantity | Assumption | Result |
| --- | --- | --- |
| Dealers | 10,000 rooftops, average 60 vehicles in stock | 600,000 live stock items |
| Stock change events | ~5 changes per vehicle per week (price, photos, status) | ~430,000 events/day, ~5/s average, peaks 50–100/s |
| Syndication fan-out | 5 portals per dealer | ~2 million outbound portal updates/day |
| Leads | 30 per dealer per month | ~10,000 leads/day, each a must-deliver webhook or ADF message |
| Plate/VIN lookups | 200 per dealer per month plus API clients | ~70,000–200,000/day, each possibly paid upstream |
| Webhook endpoints | One per DMS/CRM integration per dealer | 10,000–30,000 endpoints, some always failing |

Compare: the DVSA MOT history API's published quota of 500,000 requests per day and 15 requests/second average per key (1.6) is of the same order as this platform's total lookup demand, which is why a shared upstream key needs fair queuing across tenants.

---

## Key numbers

| Number | What | Source | Date |
| --- | --- | --- | --- |
| 2011 | Stripe: compatibility kept with every API version since founding | stripe.com/blog/api-versioning | 2017-08-05 |
| 2 per year | Stripe major (breaking) releases under the 2024 model; monthly non-breaking releases | stripe.com/blog/introducing-stripes-new-api-release-process | 2024-10-01 |
| 180 days | Google AIP recommended deprecation period for beta functionality | google.aip.dev/185 | 2024-10-22 |
| 90 days | Google AIP rule of thumb for beta time-box; Azure minimum notice before retiring a preview | google.aip.dev/181; microsoft/api-guidelines | 2019-02-18; n.d. |
| 30 days | Auto Trader Connect minimum notice for breaking changes | developers.autotrader.co.uk | n.d., accessed 2026-10 |
| 15 minutes | Auto Trader Connect access-token lifetime | developers.autotrader.co.uk | n.d., accessed 2026-10 |
| 10 s / 30 s / 30 min | Auto Trader Connect webhook retry schedule | developers.autotrader.co.uk | n.d., accessed 2026-10 |
| 3 days | Stripe live-mode webhook retry window | docs.stripe.com/webhooks | n.d., accessed 2026-10 |
| 10 seconds | GitHub webhook response deadline | docs.github.com | n.d., accessed 2026-10 |
| < 20 kB | Standard Webhooks recommended payload size | standard-webhooks spec | n.d., accessed 2026-10 |
| 500,000/day; 15 RPS; burst 10 | DVSA MOT history API quota and rate limits | documentation.history.mot.api.gov.uk | n.d., accessed 2026-10 |
| 24 hours | DVSA key restriction after exceeding daily quota | same | n.d., accessed 2026-10 |
| 50 VINs | vPIC batch decode maximum | vpic.nhtsa.dot.gov/api | n.d., accessed 2026-10 |
| 3 attempts; 10% | Google per-request retry budget; per-client retry ratio (≈1.1x load growth) | sre.google/sre-book/handling-overload | 2016 |
| 0.1% / p99.9 | Amazon false-timeout rate and corresponding latency percentile | aws.amazon.com/builders-library/timeouts-… | 2019-12-05 |
| 3,000 events/s | Kleinanzeigen Debezium/Kafka migration pipeline throughput | adevinta.com/techblog | 2025-01-28 |
| 1M records ≈ 1 min | Splink on a laptop (DuckDB); 100M+ on Spark | moj-analytical-services.github.io/splink | n.d., accessed 2026-10 |
| 0.5 bn edges / 0.4 bn vertices | Cox Automotive identity graph on Neptune | aws.amazon.com/blogs/database | 2020-09-17 |
| ~400 microservices; >30,000 req/s | Auto Trader UK on GKE + Istio | istio.io case study | n.d., accessed 2026-10 |
| ≈50% | AutoScout24 EC2 cost reduction after Karpenter (goal 15%) | tech.autoscout24.com | 2024-09-09 |
| 110 | AWS accounts migrated from Trader into AutoScout24's organisation | tech.autoscout24.com listing | 2025-08-21 |
| 24 apps / 27 APIs; 1M calls/month | Fortellis in April 2020 | builtinchicago.org | 2020-04-21 |
| 15,000+ | Dealerships using CDK's platform at the time of the 2024 attack | helpnetsecurity.com | 2024-06-20 |
| 2024-01-25 | CloudEvents CNCF graduation | cncf.io | 2024-01-25 |
| 2026-05-11 | OpenTelemetry CNCF graduation | cncf.io/projects/opentelemetry | accessed 2026-10 |
| 2025-09-19 | OpenAPI 3.2.0 release | spec.openapis.org | 2025-09-19 |
| 2025-03 | RFC 9745 Deprecation header published | rfc-editor.org | 2025-03 |

## Open questions / not verifiable

1. **mobile.de, OLX Autos, Cars.com platform architecture**: no first-party engineering write-up found. mobile.de appears in Adevinta material only as a marketplace name; its own platform choices are unverified.
2. **CDK Fortellis current scale and event APIs**: the 2023 CDK announcement could not be fetched (403); the 2026 directory figures (135+ APIs, 82,000+ integrations, 6.7bn calls/year) are unconfirmed and conflict with older figures.
3. **Commercial caching and resale clauses** of Carfax, AutoCheck, HPI/Cap HPI, DAT, Schwacke, Autotelex/VWE: not public; chapter writers need contract excerpts or must present limits as illustrative.
4. **Cost per call** of paid vehicle-history and valuation APIs: no published price list was verified.
5. **DVLA VES API registration status** ⚠: "Registration closed" at time of access; whether and when it reopens is unknown.
6. **CDK attack details** (ransom amount, attacker, restoration date): rely on secondary sources; no primary filing by CDK.
7. **Germany and Belgium**: no public register API comparable to RDW or DVSA was verified; KBA access rules belong to the regulatory brief.
8. **Bitol / ODCS dates**: graduation and v3.2.0 release dates were not captured from the source.
9. **Auto Trader's current runtime platform** (post-2021) is not described in the 2026 posts read; whether GKE/Istio remains in use is not confirmed.
10. **STAR JSON API adoption in Europe**: unverified.

## Source list

| # | Title | Publisher / author | Year | URL |
| --- | --- | --- | --- | --- |
| 1 | APIs as infrastructure: future-proofing Stripe with versioning | Stripe (B. Leach) | 2017 | https://stripe.com/blog/api-versioning |
| 2 | Introducing Stripe's new API release process | Stripe (M. Glukhovsky, W. Abirached) | 2024 | https://stripe.com/blog/introducing-stripes-new-api-release-process |
| 3 | Designing robust and predictable APIs with idempotency | Stripe (B. Leach) | 2017 | https://stripe.com/blog/idempotency |
| 4 | AIP-185 API Versioning | Google | 2024 | https://google.aip.dev/185 |
| 5 | AIP-181 Stability levels | Google | 2019 | https://google.aip.dev/181 |
| 6 | AIP-180 Backwards compatibility | Google | 2019 | https://google.aip.dev/180 |
| 7 | Microsoft Azure REST API Guidelines | Microsoft | n.d. (living) | https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md |
| 8 | RFC 8594 The Sunset HTTP Header Field | IETF (E. Wilde) | 2019 | https://www.rfc-editor.org/rfc/rfc8594.txt |
| 9 | RFC 9745 The Deprecation HTTP Response Header Field | IETF (S. Dalal, E. Wilde) | 2025 | https://www.rfc-editor.org/rfc/rfc9745.txt |
| 10 | RFC 9457 Problem Details for HTTP APIs | IETF (M. Nottingham et al.) | 2023 | https://www.rfc-editor.org/rfc/rfc9457.txt |
| 11 | RateLimit header fields for HTTP (draft-11) | IETF httpapi WG | 2026 | https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/ |
| 12 | The Idempotency-Key HTTP Header Field (expired draft-07) | IETF httpapi WG | n.d. | https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/ |
| 13 | OpenAPI Specification v3.1.0 | OpenAPI Initiative | 2021 | https://spec.openapis.org/oas/v3.1.0 |
| 14 | OpenAPI Specification v3.1.1 | OpenAPI Initiative | 2024 | https://spec.openapis.org/oas/v3.1.1 |
| 15 | OpenAPI Specification v3.2.0 | OpenAPI Initiative | 2025 | https://spec.openapis.org/oas/v3.2.0.html |
| 16 | JSON Schema specification | JSON Schema org | n.d. | https://json-schema.org/specification |
| 17 | Schema Evolution and Compatibility | Confluent | n.d. | https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html |
| 18 | Standard Webhooks specification | Standard Webhooks | n.d. | https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md |
| 19 | Standard Webhooks (home, steering committee) | Standard Webhooks | n.d. | https://www.standardwebhooks.com/ |
| 20 | Receive Stripe events in your webhook endpoint | Stripe docs | n.d. | https://docs.stripe.com/webhooks |
| 21 | Best practices for using webhooks | GitHub Docs | n.d. | https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks |
| 22 | Pattern: Transactional outbox | microservices.io (C. Richardson) | n.d. | https://microservices.io/patterns/data/transactional-outbox.html |
| 23 | Outbox Event Router | Debezium docs | n.d. | https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html |
| 24 | CNCF Announces the Graduation of CloudEvents | CNCF | 2024 | https://www.cncf.io/announcements/2024/01/25/cloud-native-computing-foundation-announces-the-graduation-of-cloudevents/ |
| 25 | CloudEvents specification | CNCF CloudEvents | n.d. | https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md |
| 26 | Questioning the Lambda Architecture | O'Reilly Radar (J. Kreps) | 2014 | https://www.oreilly.com/radar/questioning-the-lambda-architecture/ |
| 27 | What is a Medallion Architecture? | Databricks | n.d. | https://www.databricks.com/glossary/medallion-architecture |
| 28 | What is a Data Contract? | Entropy Data (J. Christ) | 2023 | https://www.datamesh-manager.com/learn/what-is-a-data-contract |
| 29 | Bitol (home) | Bitol / LF AI & Data | n.d. | https://bitol.io/ |
| 30 | Open Data Contract Standard | Bitol | n.d. | https://bitol-io.github.io/open-data-contract-standard/latest/ |
| 31 | Expectation (glossary) | Great Expectations | n.d. | https://docs.greatexpectations.io/docs/reference/learn/terms/expectation |
| 32 | Freshness checks | Soda | n.d. | https://docs.soda.io/soda-cl/freshness.html |
| 33 | OpenLineage object model | OpenLineage | n.d. | https://openlineage.io/docs/spec/object-model |
| 34 | A Theory for Record Linkage (metadata) | JASA (I. Fellegi, A. Sunter) | 1969 | https://api.crossref.org/works/10.1080/01621459.1969.10501049 |
| 35 | Splink | UK Ministry of Justice | n.d. | https://moj-analytical-services.github.io/splink/index.html |
| 36 | Timeouts, retries, and backoff with jitter | AWS Builders' Library (M. Brooker) | 2019 | https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ |
| 37 | Avoiding fallback in distributed systems | AWS Builders' Library (J. Gabrielson) | 2019 | https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems/ |
| 38 | Caching challenges and strategies | AWS Builders' Library (J. Chhabra) | 2019 | https://aws.amazon.com/builders-library/caching-challenges-and-strategies/ |
| 39 | Fairness in multi-tenant systems | AWS Builders' Library (D. Yanacek) | 2020 | https://aws.amazon.com/builders-library/fairness-in-multi-tenant-systems/ |
| 40 | Using load shedding to avoid overload | AWS Builders' Library (D. Yanacek) | 2019 | https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/ |
| 41 | Exponential Backoff And Jitter | AWS Architecture Blog (M. Brooker) | 2015 | https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/ |
| 42 | Service Level Objectives (SRE book ch. 4) | Google | 2016 | https://sre.google/sre-book/service-level-objectives/ |
| 43 | Handling Overload (SRE book ch. 21) | Google | 2016 | https://sre.google/sre-book/handling-overload/ |
| 44 | Addressing Cascading Failures (SRE book ch. 22) | Google | 2016 | https://sre.google/sre-book/addressing-cascading-failures/ |
| 45 | CircuitBreaker | M. Fowler | 2014 | https://martinfowler.com/bliki/CircuitBreaker.html |
| 46 | Noisy Neighbor (SaaS Lens) | AWS | n.d. | https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/noisy-neighbor.html |
| 47 | SaaS Architecture Fundamentals: Full stack silo and pool | AWS | 2022 | https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/full-stack-silo-and-pool.html |
| 48 | SaaS Tenant Isolation Strategies | AWS | 2020 | https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html |
| 49 | FinOps Framework | FinOps Foundation | n.d. | https://www.finops.org/framework/ |
| 50 | Unit Economics capability | FinOps Foundation | n.d. | https://www.finops.org/framework/capabilities/unit-economics/ |
| 51 | Allocation capability | FinOps Foundation | n.d. | https://www.finops.org/framework/capabilities/allocation/ |
| 52 | OWASP Top 10 API Security Risks – 2023 | OWASP | 2023 | https://owasp.org/API-Security/editions/2023/en/0x11-t10/ |
| 53 | API1:2023 Broken Object Level Authorization | OWASP | 2023 | https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/ |
| 54 | API4:2023 Unrestricted Resource Consumption | OWASP | 2023 | https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/ |
| 55 | API6:2023 Unrestricted Access to Sensitive Business Flows | OWASP | 2023 | https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/ |
| 56 | API10:2023 Unsafe Consumption of APIs | OWASP | 2023 | https://owasp.org/API-Security/editions/2023/en/0xaa-unsafe-consumption-of-apis/ |
| 57 | OAT-011 Scraping | OWASP Automated Threats | n.d. | https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-011_Scraping |
| 58 | #StopRansomware Guide | CISA, MS-ISAC, NSA, FBI | 2023 | https://www.cisa.gov/stopransomware/ransomware-guide |
| 59 | CDK Global cyberattack cripples 15,000 US auto dealerships | Help Net Security (Z. Zorz) | 2024 | https://www.helpnetsecurity.com/2024/06/20/cdk-cyberattack/ |
| 60 | CDK Global cyberattack impacts thousands of US car dealerships | BleepingComputer (L. Abrams) | 2024 | https://www.bleepingcomputer.com/news/security/cdk-global-cyberattack-impacts-thousands-of-us-car-dealerships |
| 61 | CDK Global | Wikipedia | 2026 | https://en.wikipedia.org/wiki/CDK_Global |
| 62 | OpenTelemetry project page | CNCF | n.d. | https://www.cncf.io/projects/opentelemetry/ |
| 63 | Baggage | OpenTelemetry docs | n.d. | https://opentelemetry.io/docs/concepts/signals/baggage/ |
| 64 | Metrics supplementary guidelines | OpenTelemetry | n.d. | https://opentelemetry.io/docs/specs/otel/metrics/supplementary-guidelines/ |
| 65 | Autotrader Connect developer documentation | Auto Trader UK | n.d. (release notes to 2026-09) | https://developers.autotrader.co.uk/documentation |
| 66 | Istio Pioneer AutoTrader UK Still Benefiting | Istio | n.d. | https://istio.io/latest/about/case-studies/autotrader/ |
| 67 | Auto Trader (UK): Using Istio to increase agility | Google Cloud | c. 2019 | https://cloud.google.com/customers/auto-trader-uk/ |
| 68 | Real-time Personalisation on Autotrader | Auto Trader Engineering (Medium) | 2026 | https://medium.com/autotrader-engineering/real-time-personalisation-on-autotrader-50d0cda4b778 |
| 69 | Recovering failed Snowplow events using a domain-modelled PySpark pipeline | Auto Trader Engineering (Medium) | 2026 | https://medium.com/autotrader-engineering/recovering-failed-snowplow-events-using-a-domain-modelled-pyspark-pipeline-752e52e90109 |
| 70 | SLOs for Critical User Interactions | AutoScout24 Tech (A. Carneiro) | 2024 | https://tech.autoscout24.com/blog/posts/slos-for-critical-user-interactions/ |
| 71 | Boosting Kubernetes Efficiency with Karpenter | AutoScout24 Tech (A. Vomvylas) | 2024 | https://tech.autoscout24.com/blog/posts/impact-of-karpenter/ |
| 72 | Modernizing our Data Platform – DataRunner | AutoScout24 Tech | 2023 | https://tech.autoscout24.com/blog/posts/datarunner/ |
| 73 | From Slack to Diagnosis: Building an AI Debugging Agent for Our Kubernetes Platform | AutoScout24 Tech (H. Ben Ghezail) | 2026 | https://tech.autoscout24.com/blog/posts/ai-debug-agent-infinity-platform/ |
| 74 | AutoScout24 Tech (home and listings) | AutoScout24 | n.d. | https://tech.autoscout24.com/ |
| 75 | Cox Automotive case study (Well-Architected) | AWS | c. 2021 | https://aws.amazon.com/solutions/case-studies/cox-automotive-case-study/ |
| 76 | Cox Automotive scales digital personalization using an identity graph powered by Amazon Neptune | AWS Database Blog (C. Rendon, N. Jetly) | 2020 | https://aws.amazon.com/blogs/database/cox-automotive-scales-digital-personalization-using-an-identity-graph-powered-by-amazon-neptune/ |
| 77 | Adapting to change with data patterns on AWS: the "curate" pattern | AWS Storage Blog (M.-L. Tomsen Bukovec) | 2024 | https://aws.amazon.com/blogs/storage/adapting-to-change-with-data-patterns-on-aws-the-curate-cloud-data-pattern/ |
| 78 | Decomposition Journey at CarGurus: From Monolith to Microservices | CarGurus Revved (F. Fodera) | 2023 | https://cargurus.dev/2023/02/27/decomposition-journey-at-cargurus-from-monolith-to-microservices/ |
| 79 | How CarGurus is Supercharging Our Microservice Developer Experience | CarGurus Revved | 2023 | https://cargurus.dev/2023/03/27/how-cargurus-is-supercharging-our-microservice-developer-experience/ |
| 80 | Actor Pattern Controlling Connection Pool in Kotlin to Honor API Rate Limit Exceptions | CarGurus Revved | 2023 | https://cargurus.dev/2023/07/19/actor-pattern-controlling-connection-pool-in-kotlin-to-honor-api-rate-limit-exceptions/ |
| 81 | Unpacking the Complexities of Kubernetes Upgrades | Adevinta tech blog (T. Lokejaroenlarb) | 2023 | https://adevinta.com/techblog/unpacking-the-complexities-of-kubernetes-upgrades-beyond-the-one-click-update/ |
| 82 | Make data migration easy with Debezium and Apache Kafka | Adevinta tech blog (D. Roman) | 2025 | https://adevinta.com/techblog/make-data-migration-easy-with-debezium-and-apache-kafka/ |
| 83 | Why CDK Global Launched an API Marketplace for the Auto Industry | Built In Chicago (M. Hines) | 2020 | https://www.builtinchicago.org/articles/cdk-global-fortellis-automotive-industry-api-marketplace |
| 84 | CDK Global (API provider profile) | API Evangelist | 2026 | https://providers.apievangelist.com/providers/cdk-global/ |
| 85 | STAR XML BODs | STAR | n.d. | https://www.starstandard.org/?p=488 |
| 86 | STAR releases XML BOD updates (v6.2.4) | STAR | 2024 | https://www.starstandard.org/?p=4212 |
| 87 | vPIC API | NHTSA | n.d. | https://vpic.nhtsa.dot.gov/api/ |
| 88 | MOT history API: Rate limits | DVSA | n.d. | https://documentation.history.mot.api.gov.uk/mot-history-api/rate-limits/ |
| 89 | Vehicle Enquiry Service (VES) API Guide | DVLA | n.d. | https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html |
| 90 | Open Data RDW: Gekentekende voertuigen (dataset m9d7-ebf2) | RDW (via Socrata) | live | https://opendata.rdw.nl/resource/m9d7-ebf2.json |
| 91 | Application Tokens | Socrata (Tyler Technologies) | n.d. | https://dev.socrata.com/docs/app-tokens.html |
| 92 | Places API policies | Google Maps Platform | n.d. | https://developers.google.com/maps/documentation/places/web-service/policies |
