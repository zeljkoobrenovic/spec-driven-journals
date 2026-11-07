# Research brief: Integration and data — how commerce systems talk, stay consistent, keep their promises and count the same thing

Prepared 7 November 2026 for chapter writers of *ORDERED: Architecting Commerce Platforms*. The brief feeds chapters 04 (boundaries and systems of record), 10 (inventory), 13 (order management), 19 (customer service), 23 (ERP integration), 24–28 (Part VI: integration styles, events and reconciliation, contracts and versioning, identity and master data, data and analytics) and 33 (peak load). It is platform-neutral: Shopify, Stripe, Zalando, Microsoft, Celigo and the iPaaS vendors appear because they publish dated, fetchable documentation, not as recommendations.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (7 November 2026) and supports the claim. Paraphrases stay close to the source; quoted text is quoted. The date is the source's publication date. Undated product and documentation pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (encyclopaedia, trade press, a vendor's help centre describing another vendor), not from a primary document fetched in this session.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about how a proprietary system works internally falls here unless the vendor has described it. Chapter writers should re-verify or present these as reference-architecture judgement.

**Evidence age matters.** The pattern literature in this brief is old on purpose: Sagas (1987), Starbucks and two-phase commit (2004), consumer-driven contracts (2006), eventual consistency (2008), backoff and jitter (2015), event-driven patterns (2017). These describe ideas that have not changed; they are flagged **(evidence age)** only where the surrounding technology has. Vendor documentation is current as of fetch; API versions, plan limits and prices change quarterly or faster and carry ⚠.

**Research limitation.** Several primary sites refused automated fetching (HTTP 403 or JavaScript-only pages): the Gartner glossary (iPaaS, MDM), the GS1 global site (the GS1 US site served instead), the ACM Digital Library (the Sagas paper was read from a scanned copy hosted by Cornell), ACM Queue, Taylor & Francis (Fellegi–Sunter 1969 is cited through an encyclopaedia), Salesforce Help and Trailhead (Data Cloud identity resolution rests on search-result summaries only), DZone, and Shopify's help-centre pages on sales-report definitions (the ShopifyQL schema reference on shopify.dev served the same definitions). Fivetran's Shopify connector pages returned only navigation; Airbyte's connector page is used as the worked example of SaaS extraction. No official page from Kafka's documentation gives the "11 billion events per day" Walmart figure; it is secondary. Nothing in this brief rests on the author's private *FEDERATED* journal; the two Shopify pages it also cites (API versioning, webhooks) were re-fetched here.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: prices, plan limits, API version names, product names (Databricks' sharing product appears to have been renamed between fetches of different pages), licence terms.

---

## PART 1: Integration styles — how commerce systems talk

### 1.1 The four classic styles and the criteria for choosing

Hohpe and Woolf's *Enterprise Integration Patterns* site, the reference most practitioners still cite, names four integration styles: **File Transfer** (applications write files of shared data for others to read), **Shared Database** (applications keep shared data in a common database), **Remote Procedure Invocation** (applications expose procedures other applications call to run behaviour and exchange data) and **Messaging** (applications connect to a shared messaging system and exchange data and trigger behaviour through messages). The site lists the criteria for choosing: application coupling, integration simplicity, integration technology and lock-in risk, data format and its evolution, data timeliness, data-or-functionality, and asynchronicity. It warns that "Tightly coupled applications make numerous assumptions about how the other applications work" [VERIFIED: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html, © 2003/2023, accessed 2026-11] **(evidence age: the book is from 2003; the styles are unchanged, the technology under "Messaging" and "RPI" is not)**.

Martin Fowler's 2017 article separates four things people mean by "event-driven": **event notification** (a system tells others that something changed, expecting no response; low coupling, but the overall flow is hidden), **event-carried state transfer** (events carry the changed data so receivers keep their own copy; better resilience and latency, at the cost of duplicated data), **event sourcing** (every change is stored as an event and state is derived by replay; audit trail, but replay gets hard with external systems and evolving schemas) and **CQRS** (separate read and write models; not necessarily event-based) [VERIFIED: https://martinfowler.com/articles/201701-event-driven.html, published 2017-02-07].

[ASSUMPTION/JUDGEMENT] In commerce the four EIP styles map onto flows that newcomers meet in their first week: file transfer is the nightly product feed to a marketplace or the EDI batch to a wholesaler; shared database is the ERP-centred suite where web shop and ERP read the same tables; RPI is the synchronous call from checkout to a tax or payment service; messaging is the order-placed event consumed by the WMS, the ERP and the e-mail system. Most merchants at the Omnichannel stage run all four at once, which is why an integration inventory (Section 1.8) matters more than a single "integration strategy".

### 1.2 Change data capture

Debezium, the most widely used open-source change-data-capture (CDC) tool, describes itself as "a set of source connectors for Apache Kafka Connect"; each connector "ingests changes from a different database by using that database's features for change data capture". It lists log-based CDC's properties as capturing all changes with low latency, without changing the data model, and including deletes; an initial snapshot can be taken when a connector starts and the logs no longer hold the needed history, and incremental snapshots can be triggered at runtime. The current documentation is for Debezium 3.7 and lists connectors for MySQL, MariaDB, MongoDB, PostgreSQL, Oracle, SQL Server, Db2, Cassandra, Vitess, Spanner, Informix, CockroachDB and others [VERIFIED: https://debezium.io/documentation/reference/stable/features.html, n.d. (Debezium 3.7), accessed 2026-11] ⚠.

[ASSUMPTION/JUDGEMENT] CDC is the honest way to turn a database-centred system (an on-premises ERP, a legacy OMS) into an event source without rewriting it, and it is also the mechanism behind the "transaction log tailing" variant of the outbox pattern (Section 2.5). Its limit in commerce is semantic: a row change in an ERP table is not a business event, so someone must map "row updated in ITEM_LEDGER" to "stock changed for SKU X at location Y".

### 1.3 Webhooks, polling and the reconciliation job

Two payment and commerce platforms document the same pattern in their own words.

- Shopify webhooks: a subscription's destination can be an HTTPS URL, a Google Pub/Sub topic or an Amazon EventBridge event bus. Shopify "doesn't guarantee ordering within a topic, or across different topics for the same resource" (a `products/update` may arrive before its `products/create`), recommends sorting by the `X-Shopify-Triggered-At` header or the payload's `updated_at`, states that "Webhook delivery isn't always guaranteed, and your app can miss or mishandle events for other reasons", and tells apps to "use reconciliation jobs to periodically fetch data from Shopify so that your app stays consistent with Shopify's data", using `updated_at` filters on GraphQL queries to fetch objects changed since the last run [VERIFIED: https://shopify.dev/docs/apps/build/webhooks, n.d., accessed 2026-11].
- Shopify's HTTPS delivery rules: a one-second connection timeout and a five-second timeout for the whole request; any non-2xx response, including 3xx, counts as an error; "If Shopify receives no response or an error, it retries 8 times over the next 4 hours"; "After 8 consecutive failures, the subscription is automatically deleted if it was configured using the Admin API"; each delivery carries `X-Shopify-Hmac-SHA256` (HMAC of the raw body with the app's client secret), `X-Shopify-Webhook-Id` (per delivery, for duplicate detection) and `X-Shopify-Event-Id` (shared by deliveries of one merchant action); "Shopify minimizes duplicate deliveries, but your app might receive the same webhook more than once" [VERIFIED: https://shopify.dev/docs/apps/build/webhooks/subscribe/https, n.d., accessed 2026-11].
- Stripe webhooks: Stripe "attempts to deliver events to your destination for up to three days with an exponential back off in live mode"; "Stripe doesn't guarantee the delivery of events in the order that they're generated"; endpoints "might occasionally receive the same event more than once", so apps should log processed event IDs; handlers must "quickly return a successful status code (2xx) before any complex logic"; events should be processed through an asynchronous queue because spikes "might overwhelm your endpoint hosts"; events can also be sent to Amazon EventBridge or Azure Event Grid; up to 16 event destinations per account; manual resend works for 15 days in the Dashboard and 30 days via the CLI [VERIFIED: https://docs.stripe.com/webhooks, n.d., accessed 2026-11].

For bulk reads instead of change notifications, Shopify's bulk operations run a GraphQL query asynchronously and return a JSONL file at a signed URL; from API version `2026-01` an app can run up to five bulk query operations per shop at once (one per type before that); a bulk query must complete within 10 days; completion is signalled by the `bulk_operations/finish` webhook (recommended over polling, though "delivery isn't guaranteed, so you may still need to poll"); result URLs expire after one week [VERIFIED: https://shopify.dev/docs/api/usage/bulk-operations/queries, n.d., accessed 2026-11] ⚠.

| Mechanism | Who initiates | Latency | Failure mode the receiver must handle | Typical commerce use |
| --- | --- | --- | --- | --- |
| Synchronous API call | Caller | Milliseconds | Timeout, partial success, retry storms | Price/tax/stock check at checkout, payment authorisation |
| Webhook | Source system | Seconds | Missed, duplicated, out-of-order deliveries; endpoint must answer fast | Order placed, payment captured, shipment created |
| Polling / `updated_at` sweep | Receiver | Minutes | Rate limits, clock skew, large pages | Reconciliation, catch-up after outage |
| Bulk export / file | Either, on schedule | Hours to a day | Stale by design; late files; partial files | Product feeds, EDI batches, nightly ERP sync |
| Queue / event stream | Source publishes, consumers pull | Seconds | At-least-once duplicates, ordering per key only | Stock events, order events to many consumers |
| CDC | Database log | Seconds | Row changes are not business events | Legacy ERP/OMS as event source |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis of the sources above and Section 2. The lesson both Shopify and Stripe state in their own documentation, and that chapter 25 should teach as the rule, is that webhooks are a latency optimisation on top of a polling-based reconciliation, never a replacement for it.

### 1.4 Point-to-point versus hub: iPaaS and integration platforms

**Definition.** Gartner's definition of integration platform as a service, as relayed by an encyclopaedia entry: "Integration platform as a service (iPaaS) is a suite of cloud services enabling customers to develop, execute and govern integration flows between disparate applications." The same entry lists essential features from Gartner's reference model: multi-tenant elastic cloud, subscription pricing, no software development ("required connectors should already be available"), no deployment or platform management by the user, and integration management and monitoring [WIDELY REPORTED: https://en.wikipedia.org/wiki/Cloud-based_integration, retrieved 2015 (Gartner glossary), accessed 2026-11]. The Gartner glossary itself refused fetching (HTTP 403).

**What the vendors say they do and how they charge** (all fetched 2026-11; all ⚠):

| Vendor | Self-description on the pricing page | Pricing model | Public prices |
| --- | --- | --- | --- |
| MuleSoft (Salesforce) | API and AI management, agent orchestration, application integration and data connectivity, document automation | Usage-based "Mule Credits" shared across products; rates fall with volume "by up to 90%"; Pre-Purchase, Pre-Commit ($50K minimum annual commitment) and Unlimited models | Packages "start at $2,000 per month, billed annually"; credit rates not disclosed |
| Boomi | "The platform that puts AI into action": integration and automation, API management, data management, AI infrastructure | Annual subscription editions (Integration, API Management, Data Hub, Data Integration) with connection counts per edition; Pay-As-You-Go | $99 per month plus usage (Pay-As-You-Go); editions "Talk to sales" |
| Workato | Editions (Standard, Business MCP, Enterprise MCP, Workato ONE) metered by capability (Workflows, APIM, Event Streams), Enterprise Workbots, on-premise agents, concurrency; "1,200+ pre-built connectors"; unlimited workspaces and users | Quote-based | None |
| Celigo | "Intelligent automation platform" for integrations, workflows and AI agents; integrations, data ingestion, EDI, APIs, MCP; marketplace of prebuilt connectors; names Shopify, Amazon, NetSuite, Walmart | Editions (Standard, Professional, Enterprise); "Your price depends on the edition you choose and how your team uses the platform" | None; 30-day trial |
| Make | Visual automation; "As of August 27, credits are the billing unit in Make"; most actions cost 1 credit | Credits per month; Free, Core, Pro, Teams, Enterprise; start-up discount 50% | Free plan 1,000 credits/month; paid prices not on the page |
| n8n | Workflow automation; "Pricing is based on monthly workflow executions, regardless of complexity"; unlimited users and workflows | Executions per month; cloud or self-hosted | Starter €20/month (2.5K executions), Pro €50/month (10K), Business €667/month (40K, self-hosted), annual billing; Enterprise on request |

Sources: MuleSoft [VERIFIED: https://www.mulesoft.com/anypoint-pricing, n.d., accessed 2026-11]; Boomi [VERIFIED: https://boomi.com/pricing/, n.d. (© 2026), accessed 2026-11]; Workato [VERIFIED: https://www.workato.com/pricing, n.d. (© 2026), accessed 2026-11]; Celigo [VERIFIED: https://www.celigo.com/pricing/, n.d. (ratings "as of Oct 2026"), accessed 2026-11]; Make [VERIFIED: https://www.make.com/en/pricing, n.d. (© 2026), accessed 2026-11]; n8n [VERIFIED: https://n8n.io/pricing/, n.d. (© 2026), accessed 2026-11]. n8n's self-hosted code is under its Sustainable Use License 1.0: "You may use or modify the software only for your own internal business purposes or for non-commercial or personal use"; distribution to others only free of charge and non-commercially; files marked `.ee` need an n8n Enterprise License [VERIFIED: https://github.com/n8n-io/n8n/blob/master/LICENSE.md, n.d., accessed 2026-11] ⚠.

[ASSUMPTION/JUDGEMENT] Three observations for chapter 24. First, every vendor now sells "AI agents" on the same page as integration; the integration function underneath (connectors, mapping, scheduling, monitoring) is what a merchant actually buys, and the AI framing will date fast. Second, the metering unit differs per vendor (credits, executions, connections, tasks, concurrency), so a total-cost comparison must be made per flow volume, not per list price; the only like-for-like figures are n8n's per-execution tiers. Third, the low end (Make, n8n, Boomi PAYG) is priced for a Starting- or Growing-stage merchant's first three integrations; MuleSoft's $2,000-per-month floor and $50K pre-commit signal a Group-stage buyer.

### 1.5 Vendor-built connectors as the third option

Between hand-built point-to-point code and a general iPaaS sit connectors built by the systems' own vendors. Two dated examples:

- **Microsoft Dynamics 365 Business Central's Shopify Connector** (documentation dated 2026-09-22 to 2026-10-16). The item-sync page tells the merchant to "decide which system is the system of record for product data" before configuring: "If you manage item names, descriptions, and pricing in Business Central, choose the To Shopify direction. If your merchandising team maintains product content in Shopify ... choose From Shopify." Mapping between the two product models uses the Shopify SKU or barcode: the `SKU Mapping` options are Item No., Item No. + Variant Code (with a separator), Vendor Item No. or Bar Code, with "Find Mapping by Barcode" as a fallback [VERIFIED: https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-items, published 2026-10-16]. The inventory page states the ownership rule outright: "Business Central acts as the system of record for inventory"; stock is pushed one way with one of two calculation methods ("Projected Available Balance at Today" or "Free Inventory (not reserved)"), and the recommended job-queue frequency is "every 15-30 minutes" [VERIFIED: https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-inventory, published 2026-10-14]. Orders flow the other way: "Enable Auto Sync Orders to receive real-time notifications whenever a new order is created in a Shopify store. When a notification is received, the Connector runs the Sync Order from Shopify batch job using Job Queue Entries"; the Shopify order number can be used as the sales-document number ("Use Shopify Order No."), and every sales document keeps a `Shopify Order Id` link [VERIFIED: https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-orders, published 2026-10-14]. The connector is preinstalled in new Business Central sign-ups [VERIFIED: https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/get-started, published 2026-09-22].
- **Celigo's Shopify–NetSuite Integration Template** covers order-to-cash: Shopify orders create NetSuite sales orders; cancelled Shopify orders close them; NetSuite item shipments update Shopify fulfillments and vice versa; NetSuite invoices, refunds and credit memos map to Shopify billings and refunds; customers, items, collections, promotions and abandoned checkouts each have a flow. The page states directions but not which system is master for each entity, and lists no inventory or payout flow [VERIFIED: https://www.celigo.com/integrations/shopify-netsuite/, n.d. (© 2026), accessed 2026-11] ⚠.

[ASSUMPTION/JUDGEMENT] The Business Central documentation is unusually explicit about ownership (products: choose; inventory: ERP; orders: shop) and is a good dated example for chapters 04 and 23 of a vendor encoding the entity–owner table into configuration. Note the design: the "real-time notification" only *triggers* a batch job; the connector still polls Shopify for the order. That is the webhook-plus-reconciliation pattern of Section 1.3 built into a product.

### 1.6 Choosing per flow

[ASSUMPTION/JUDGEMENT] The sources above support a per-flow rule rather than a per-company rule. The table below is the analyst's synthesis, to be presented as recommendation:

| Flow | Default style at Growing stage | What changes at Omnichannel/Group | Why |
| --- | --- | --- | --- |
| Products and content | Scheduled sync from the system of record (PIM or ERP) | Event on change plus nightly full sync as safety net | Content tolerates minutes of lag; completeness matters more than speed |
| Prices | Scheduled sync, hourly or faster | Event-driven for promotions with start/end times | A stale price is a broken promise with legal weight |
| Stock | Push from the inventory owner every 15–30 minutes (the Business Central default) | Stock events per SKU/location, with a reconciliation job and a buffer | The oversell window is the sync interval |
| Orders | Webhook triggers import; polling catches misses | Order events to OMS, ERP, WMS; idempotent consumers | Orders must never be lost or doubled |
| Shipments and tracking | Webhook/event from WMS or carrier platform | Same | Drives notifications and WISMO |
| Customers | Sync on order; periodic merge | Identity service or CDP (Part 4) | Matching is the hard part, not transport |
| Finance (invoices, payouts) | Nightly batch to ERP | Nightly batch to ERP, reconciled | Finance works in periods, not seconds |

### 1.7 Integration debt and the integration inventory

No primary, vendor-neutral source for the phrase "integration debt" was reachable in this session (DZone refused fetching; the remaining search hits were vendor posts). The usable evidence is indirect:

- Shopify's own webhook rules (subscription deleted after eight consecutive failures when created via the API; retries limited to four hours) mean that an integration nobody monitors silently stops receiving events [VERIFIED: https://shopify.dev/docs/apps/build/webhooks/subscribe/https, n.d., accessed 2026-11].
- Shopify removes deprecated fields "in a subsequent release" after announcing them in the developer changelog, and declares the REST Admin API legacy as of 1 October 2024 (Section 3.2) — an integration that is not maintained will eventually break on a schedule the vendor, not the merchant, controls [VERIFIED: https://shopify.dev/docs/api/usage/versioning, n.d., accessed 2026-11; https://shopify.dev/docs/api/admin-rest, n.d., accessed 2026-11].
- Zalando's guidelines require that usage of deprecated APIs be monitored and that clients approve a shut-down (Section 3.4) — the provider-side half of the same discipline [VERIFIED: https://opensource.zalando.com/restful-api-guidelines/, changelog to 2026-03-16, accessed 2026-11].

[ASSUMPTION/JUDGEMENT] Integration debt is therefore best defined for the book operationally: the set of integrations whose owner, contract version, failure alert and reconciliation job are unknown. The integration inventory (one row per flow: source, target, style, owner, contract version, volume, retry/DLQ, reconciliation, last incident) is the management tool that makes the debt visible, and chapter 24's Kestrel & Pine thread (34 integrations, four styles) is the illustration.

**For newcomers (Part 1).** *Integration style*: the basic way two systems exchange data — a file, a shared database, a direct call, or a message. *Webhook*: an HTTP request the source system sends to a URL you registered when something happens; it is a notification, not a guarantee. *iPaaS*: a cloud service in which you draw or configure integration flows between applications instead of coding them, paid by usage. *Change data capture*: reading a database's own change log to turn every row change into a stream of events.

**Architecture implications (Part 1)** [ASSUMPTION/JUDGEMENT]. *Starting*: the platform's apps and a vendor connector (shop–accounting, shop–3PL) are the integrations; the merchant owns none of the code and should keep an inventory anyway. *Growing*: the first point-to-point scripts and the first iPaaS; choose per flow (Section 1.6) and insist on a reconciliation job for stock and orders. *Omnichannel*: a dozen or more systems; the integration layer becomes a product with an owner, standards (idempotency, contract versions, monitoring) and a queue or event bus for orders and stock. *Group*: shared integration platform or per-brand autonomy is a governance decision; a hub without ownership rules recreates point-to-point chaos inside the hub.

---

## PART 2: Reliability — built to disagree and recover

### 2.1 Eventual consistency in plain words

Werner Vogels (Amazon CTO) defined eventual consistency in December 2008 as "a specific form of weak consistency": if no new updates are made to an object, eventually all reads will return the last updated value. He listed the variants a designer can promise on top of it: causal consistency, read-your-writes, session consistency, monotonic reads and monotonic writes [VERIFIED: https://www.allthingsdistributed.com/2008/12/eventually_consistent.html, published 2008-12-23] **(evidence age: 18 years; the definitions are unchanged)**.

Gregor Hohpe's 2004 essay "Starbucks Does Not Use Two-Phase Commit" is the practitioner's version: the cashier takes the order and payment while baristas work asynchronously; drinks finish out of order, so a correlation identifier (the name on the cup) matches drink to customer; "Starbucks, like most other businesses is primarily interested in maximizing throughput of orders"; errors are handled by **write-off** (accept the loss), **retry** (try again) or **compensating action** (refund the money), and "a two-phase-commit can make life a lot simpler but it can also hurt the free flow of messages" [VERIFIED: https://www.enterpriseintegrationpatterns.com/ramblings/18_starbucks.html, published 2004-11-19] **(evidence age: 22 years; still the clearest commerce analogy)**.

### 2.2 At-least-once delivery and duplicates

Apache Kafka's design documentation states that "Kafka guarantees at-least-once delivery by default"; at-most-once is obtained by disabling producer retries and committing offsets before processing; exactly-once is supported within Kafka Streams and with transactions plus read-committed consumers, while destinations outside Kafka "need cooperation from those systems"; since 0.11.0.0 the idempotent producer uses a producer ID and sequence numbers so that resends do not duplicate log entries, and producers can "send messages atomically to multiple topic partitions using transactions"; a topic is "a set of totally ordered partitions", each consumed by one consumer per group at a time [VERIFIED: https://kafka.apache.org/44/design/design/, n.d. (Kafka 4.4 documentation), accessed 2026-11].

CloudEvents, the CNCF event-envelope specification, requires `id`, `source`, `specversion` and `type` on every event, requires producers to ensure that "source + id is unique for each distinct event", allows a re-sent duplicate (for example after a network error) to keep the same `id`, and lets consumers treat events with identical `source` and `id` as duplicates [VERIFIED: https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md, spec version 1.0 (document 1.0.3-wip), accessed 2026-11]. CloudEvents was accepted by CNCF on 2018-05-15 and graduated on 2024-01-25 [VERIFIED: https://www.cncf.io/projects/cloudevents/, n.d., accessed 2026-11].

[ASSUMPTION/JUDGEMENT] For chapter 25 the teaching point is that every delivery mechanism a merchant will meet — Kafka, SQS, a webhook from Shopify or Stripe, an iPaaS retry — is at-least-once in practice. "Exactly once" is a property a consumer builds (Section 2.3), not one it receives.

### 2.3 Idempotency keys: Stripe and Shopify

- **Stripe** accepts an `Idempotency-Key` header on all `POST` requests (not `GET`/`DELETE`, which "are idempotent by definition"). For API v1, "Stripe saves the status code and body of the first request made with a given idempotency key after endpoint execution begins. Retries with the same key return the saved response, including 500 errors." Keys are client-generated (V4 UUIDs suggested), up to 255 characters, must not contain sensitive data, and may be pruned "after they're at least 24 hours old"; "The idempotency layer compares incoming parameters to those of the original request and errors if they're not the same." With API v2, retries "don't repeat successful operations" and Stripe retries partially failed work to completion [VERIFIED: https://docs.stripe.com/api/idempotent_requests, n.d., accessed 2026-11].
- **Shopify** supports idempotency on the GraphQL Admin API through an `idempotencyKey` input on some mutations (for example `subscriptionBillingAttemptCreate`) or the `@idempotent(key: "...")` directive, "just a different GraphQL syntax for passing in idempotency keys"; keys are app-generated unique strings (UUIDs recommended); "repeated requests with the same parameters are executed only once, no matter how many times the request is retried"; bulk mutations take a key per JSONL row; mutations that only update or delete are idempotent by definition, while mutations such as `inventoryTransferSetItems` that perform additional non-idempotent operations require a key. The page does not state a retention period [VERIFIED: https://shopify.dev/docs/api/usage/idempotent-requests, n.d., accessed 2026-11] ⚠.
- On the receiving side, both Shopify (`X-Shopify-Webhook-Id`) and Stripe (event `id`) tell consumers to store processed IDs and skip repeats; Stripe adds that two *distinct* events can describe the same change, so deduplicate on `data.object.id` plus `event.type` as well (Section 1.3 sources).

[ASSUMPTION/JUDGEMENT] The commerce rule that follows: the order number, not a timestamp, is the idempotency key for "create order in ERP"; the (order, line, quantity, reason) tuple is the key for a refund; the (SKU, location, event id) tuple is the key for a stock adjustment. A consumer that cannot say what its key is cannot be made safe.

### 2.4 Ordering and out-of-order events

Both Shopify and Stripe disclaim ordering (Section 1.3). Stripe adds that snapshot events "record `created` in seconds, so distinct events can share a timestamp. Don't use `created` to determine event order or whether you've already processed an event"; instead fetch the current object from the API when an event arrives early [VERIFIED: https://docs.stripe.com/webhooks, n.d., accessed 2026-11]. Kafka orders only within a partition (Section 2.2). AWS warns that a dead-letter queue attached to a FIFO queue breaks "the exact order of messages or operations" [VERIFIED: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html, n.d., accessed 2026-11].

[ASSUMPTION/JUDGEMENT] Three design responses, in rising cost: (1) make handlers tolerant — a "shipped" event that arrives before "allocated" is stored and re-evaluated when the missing state arrives; (2) carry a version or sequence per entity and reject stale updates (a stock event with `updated_at` older than the stored value is dropped); (3) partition the stream by entity key (order id, SKU+location), as Walmart's inventory design does (Section 5.3), so that one consumer sees one entity's events in order.

### 2.5 The transactional outbox

Chris Richardson's pattern catalogue states the problem as "How to atomically update the database and send messages to a message broker?" and the solution: "The solution is for the service that sends the message to first store the message in the database" (in an outbox table, in the same transaction as the business change); "A separate process then sends the messages to the message broker." The relay is implemented by polling the outbox (Polling publisher) or tailing the transaction log (Transaction log tailing, that is CDC). Resulting context: "The Message relay might publish a message more than once", so "a message consumer must be idempotent" [VERIFIED: https://microservices.io/patterns/data/transactional-outbox.html, n.d., accessed 2026-11].

[ASSUMPTION/JUDGEMENT] In commerce terms: an order service that writes the order row and then calls the queue can lose the event if the process dies between the two; the outbox makes "order placed" and "order-placed event" one atomic write. For a merchant on a SaaS platform the outbox is not theirs to build; the platform's webhook plus their reconciliation job plays the same role from the outside.

### 2.6 Retries with backoff and jitter

Marc Brooker (AWS) showed in 2015, by simulation of optimistic concurrency under contention, that capped exponential backoff alone leaves clients retrying in synchronised clusters, and that adding randomness spreads retries: "The solution isn't to remove backoff. It's to add jitter." With 100 contending clients, "full jitter" cut the total number of calls by more than half compared with un-jittered exponential backoff and finished sooner; a May 2023 note adds that most AWS SDKs now implement backoff with jitter [VERIFIED: https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/, published 2015-03-04]. Stripe's rate-limit guidance gives the consumer-side rule: on `429`, "Follow an exponential backoff schedule to reduce request volume when necessary, and add randomness to the backoff schedule to avoid a thundering herd effect", or implement a client-side token bucket [VERIFIED: https://docs.stripe.com/rate-limits, n.d., accessed 2026-11]. Shopify's recommended backoff after a throttle error is one second [VERIFIED: https://shopify.dev/docs/api/usage/rate-limits, n.d., accessed 2026-11].

### 2.7 Dead-letter queues

Amazon SQS describes dead-letter queues (DLQs) as queues that "source queues can target for messages that are not processed successfully", useful "because you can isolate unconsumed messages to determine why processing did not succeed". A redrive policy's `maxReceiveCount` is "the number of times a consumer can receive a message from a source queue before it is moved to a dead-letter queue"; AWS advises setting it "high enough to allow for sufficient retries". Because a standard-queue message keeps its original enqueue timestamp when moved, "it is a best practice to always set the retention period of a dead-letter queue to be longer than the retention period of the original queue"; messages can be moved back with DLQ redrive [VERIFIED: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html, n.d., accessed 2026-11].

[ASSUMPTION/JUDGEMENT] A DLQ with nobody watching it is a silent order-loss mechanism. The operational rule for chapter 25: every DLQ has an alarm, an owner, and a documented replay procedure; the number of messages in DLQs is a health metric alongside orders per minute (chapter 33).

### 2.8 Sagas and compensation

Garcia-Molina and Salem's 1987 SIGMOD paper introduced the term: long-lived transactions "hold on to database resources for relatively long periods of time, significantly delaying the termination of shorter and more common transactions"; "A LLT is a saga if it can be written as a sequence of transactions that can be interleaved with other transactions. The database management system guarantees that either all the transactions in a saga are successfully completed or compensating transactions are run to amend a partial execution" [VERIFIED: https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf (scanned copy of *Sagas*, Proc. ACM SIGMOD 1987, p. 249, © 1987 ACM 0-89791-236-5/87/0005/0249), read 2026-11] **(evidence age: 39 years; the definition is the one still used)**.

Richardson's catalogue restates it for services: "How to implement transactions that span services?" — "A saga is a reliably coordinated sequence of local transactions"; coordination is either **choreography** ("each local transaction publishes domain events that trigger local transactions in other services") or **orchestration** ("an orchestrator (object) tells the participants what local transactions to execute"); when a step fails, "the changes made by the completed steps are undone by compensating transactions"; the drawback is "Lack of isolation (the 'I' in ACID)", requiring countermeasures the designer must choose [VERIFIED: https://microservices.io/patterns/data/saga.html, n.d., accessed 2026-11].

[ASSUMPTION/JUDGEMENT] Commerce sagas the book can name: place order = reserve stock → authorise payment → create order → confirm; cancel after shipment = request return → refund on receipt (a compensation that is a business process, not a database undo); split shipment = allocate per location, each with its own compensation. The OMS of chapter 13 is, in practice, the saga orchestrator for the order; chapter 25 should say so.

### 2.9 Reconciliation as a first-class component

The practice has a finance-side model with precise vocabulary. Stripe's payout reconciliation report "helps you match the payouts you receive in your bank account with the batches of payments and other transactions that they relate to"; each payout is reconciled "as a settlement batch" whose itemised download lists "every payment, refund, dispute, fee, and other balance transaction included in the payout", with a `balance_transaction_id` per line, an `order_id` and `payment_intent_id` for matching, and optional custom metadata "to match Stripe transactions with records in your accounting system"; merchants on manual payouts reconcile the Stripe balance "like a bank account" with the Balance report instead; the report groups by *estimated* arrival date, not the bank's posting date, and "a payout might arrive before its reconciliation data is ready" [VERIFIED: https://docs.stripe.com/reports/payout-reconciliation, n.d., accessed 2026-11].

The commerce-side model is Shopify's instruction to apps to run periodic `updated_at` sweeps because deliveries can be missed (Section 1.3), and Business Central's inventory sync, which compares "Shopify Stock" with "Last Calculated Stock" per variant and location and sends an update only when they differ, keeping "Last Synced On" and "Last Calculated On" timestamps for troubleshooting [VERIFIED: https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-inventory, published 2026-10-14].

[ASSUMPTION/JUDGEMENT] A reconciliation card for the toolkit, generalised from the finance model: *what two sets are compared* (ERP orders vs platform orders for a day; WMS stock vs platform stock per SKU/location; PSP settlement vs ledger), *the matching key* (order number, SKU+location, balance transaction id), *the tolerance* (zero for orders and money, a count threshold for stock), *the cadence* (daily for money, hourly or continuous for stock), *who gets the exceptions* and *what the fix is* (replay, manual correction, write-off). The Kestrel & Pine figure of 2.3% of variants wrong is illustrative and has no public counterpart.

### 2.10 Monitoring an integration

Google's SRE book names four golden signals: **latency** ("the time it takes to service a request"), **traffic** ("a measure of how much demand is being placed on your system"), **errors** ("the rate of requests that fail"), and **saturation** (how "full" the service is); it distinguishes symptoms ("what's broken") from causes ("why"), and black-box monitoring ("symptom-oriented and represents active—not predicted—problems") from white-box monitoring that "depends on the ability to inspect the innards of the system" [VERIFIED: https://sre.google/sre-book/monitoring-distributed-systems/, published 2017 (book)].

[ASSUMPTION/JUDGEMENT] Applied to an integration, the four signals become: end-to-end lag per flow (order placed → order in WMS), events per minute per flow against the expected rate, failed deliveries and DLQ depth, and rate-limit headroom (Shopify's `throttleStatus.currentlyAvailable`, Stripe's `429` counts — Section 3.7). The black-box check is the reconciliation job's variance; the white-box check is the connector's own log. The missing-event case (traffic drops to zero while the shop is busy) is the one most teams forget to alert on.

**For newcomers (Part 2).** *Eventual consistency*: after an update stops, all systems will agree eventually, but for a while they may show different values. *Idempotency*: doing the same request twice has the same effect as doing it once, so retries are safe. *Outbox*: a table where a system writes "event to send" in the same transaction as the business change, so an event is never lost between the database and the queue. *Saga*: a long business transaction made of steps, each with an undo step (compensation) in case a later one fails. *Reconciliation*: a job that compares two systems' records and reports or repairs the differences. *Dead-letter queue*: where messages go after they have failed too many times, so a person can look at them.

**Architecture implications (Part 2)** [ASSUMPTION/JUDGEMENT]. *Starting*: the platform and its apps handle retries; the merchant's job is to check the apps' failure logs weekly and to reconcile payouts monthly. *Growing*: the first custom integration must have idempotent writes, a retry with backoff and a daily reconciliation for orders and stock; without these the Black Friday oversell of chapter 10 is only a question of when. *Omnichannel*: integration standards (idempotency key per entity, event envelope with id/source/type, DLQ with owner, reconciliation card per flow, four golden signals per flow) are written down and reviewed; an OMS orchestrates the order saga. *Group*: shared event bus and schema registry; reconciliation becomes a data-platform job across brands (Part 5).

---

## PART 3: Contracts and versioning — promises between systems

### 3.1 Describing a contract: OpenAPI, AsyncAPI, CloudEvents, JSON Schema

- The OpenAPI Specification "defines a standard, programming language-agnostic interface description for HTTP APIs"; the latest version is 3.2.1, dated 10 September 2026 [VERIFIED: https://spec.openapis.org/oas/latest.html, published 2026-09-10] ⚠.
- "The AsyncAPI Specification is a project used to describe message-driven APIs in a machine-readable format"; version 3.0.0 models channels (addresses), operations (what an application does on them) and messages [VERIFIED: https://www.asyncapi.com/docs/reference/specification/v3.0.0, n.d., accessed 2026-11]; 3.0.0 was released on 5 December 2023 and decoupled operations from channels ("a channel and message should be detached from the operations performed") [VERIFIED: https://www.asyncapi.com/blog/release-notes-3.0.0, published 2023-12-05].
- "CloudEvents is a vendor-neutral specification for defining the format of event data" (Section 2.2 for the required attributes) [VERIFIED: https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md, accessed 2026-11].
- JSON Schema's current version is 2020-12 (previous 2019-09), split into Core and Validation specifications, with meta-schemas against which schemas are validated [VERIFIED: https://json-schema.org/specification, n.d., accessed 2026-11].
- Zalando's event bus Nakadi (2015–2024) is a dated example of a company enforcing schemas on its events: producers registered event types, "events are validated against the type's schema before publishing" (JSON Schema in the README), consumers used a Subscriptions API; the repository was archived on 2024-06-07 with the note that "Nakadi is no longer developed in the open as we've not seen usage outside of Zalando for many years" [VERIFIED: https://github.com/zalando/nakadi, archived 2024-06-07, accessed 2026-11] **(evidence age: internal use after 2024 is unknown)**.

### 3.2 Shopify's dated API versions

"Shopify releases a new API version every three months at 5pm UTC on the first day of the quarter", named by date (for example `2026-04`); "Each stable version is supported for a minimum of 12 months", with at least nine months of overlap between consecutive versions; the version is specified in the request URL; "If your app targets an inaccessible version, Shopify falls forward and responds using the oldest accessible stable version", and the `X-Shopify-API-Version` response header shows which version answered; release candidates appear on the same date as the stable release but "may include backwards-incompatible changes, so not recommended for production"; deprecations are announced in the developer changelog with migration guidance and "Deprecated fields or types are removed in a subsequent release". The latest stable version at fetch is `2026-10`, accessible until 16 October 2027 [VERIFIED: https://shopify.dev/docs/api/usage/versioning, n.d., accessed 2026-11] ⚠.

The largest deprecation in Shopify's recent history is of a whole API surface: "The REST Admin API is a legacy API as of October 1, 2024", and "Starting April 1, 2025, all new public apps must be built exclusively with the GraphQL Admin API"; "Some newer platform features may only be available in GraphQL" [VERIFIED: https://shopify.dev/docs/api/admin-rest, n.d., accessed 2026-11] ⚠.

Webhook payloads follow the subscription's API version; apps should pin it (Section 1.3 sources).

### 3.3 Stripe's dated API versions

Stripe pins each account to the API version current at its first request and lets callers override per request with the `Stripe-Version` header; breaking changes are implemented as "version change modules" with a documented transformation, applied in reverse order until the caller's version is reached; "To date, we've maintained compatibility with every version of our API since the company's inception in 2011", after "almost a hundred breaking upgrades over six years" [VERIFIED: https://stripe.com/blog/api-versioning, published 2017-08-05 (Brandur Leach)] **(evidence age: 9 years; the mechanism is still the one documented below)**. Since 1 October 2024 Stripe releases monthly versions with no breaking changes and two named major releases a year (the first, Acacia), each with new SDKs under semantic versioning; "Each monthly release adds new features without breaking changes" [VERIFIED: https://stripe.com/blog/introducing-stripes-new-api-release-process, published 2024-10-01]. The current documentation names the version `2026-10-28.endive`; webhook events use the account's default version unless the endpoint was created with a version; strongly typed SDKs (Java, Go, .NET) are fixed to the version current at the SDK's release [VERIFIED: https://docs.stripe.com/api/versioning, n.d., accessed 2026-11] ⚠.

[ASSUMPTION/JUDGEMENT] Shopify and Stripe show two different contracts with the same shape. Shopify forces consumers to move every year (12-month support, fall-forward); Stripe lets consumers stay but ships breaking changes only twice a year behind opt-in. For the merchant, both mean the same two obligations: pin the version explicitly (in the URL for Shopify, in the header and the webhook endpoint for Stripe) and schedule the upgrade.

### 3.4 Company API guidelines: Zalando and Google

Zalando's RESTful API Guidelines (published on GitHub, owned by its API Guild) require **API First**: "You must define APIs first, before coding its implementation, using OpenAPI as specification language" (OpenAPI 3.1 since the 2025-10-01 changelog entry); specifications must be "a single self-contained YAML file"; compatibility rules include **MUST not break backward compatibility** (rule #106), **MUST use media type versioning** (#114) with URL versioning prohibited, and versioning avoided where possible; deprecation rules include **MUST obtain approval of clients before API shut down** (#185), **MUST monitor usage of deprecated API scheduled for sunset** (#188) and **SHOULD add `Deprecation` and `Sunset` header to responses** (#189); keywords follow RFC 2119. The changelog's latest entry is 2026-03-16 [VERIFIED: https://opensource.zalando.com/restful-api-guidelines/, changelog to 2026-03-16, accessed 2026-11].

Google's API Improvement Proposal 180 (Backwards compatibility; created 2019-07-23, changelog to 2025-10-21) states "Existing client code **must not** be broken by a service updating to a new minor or patch release", distinguishes source, wire and semantic compatibility, allows adding fields, enum values and methods (no new required fields on existing requests; new fields default to old behaviour), and classes as breaking: removing or renaming anything, changing a field's type "even to a wire-compatible type", changing default values, resource-name formats or visible behaviour [VERIFIED: https://google.aip.dev/180, created 2019-07-23, updated to 2025-10-21].

### 3.5 Deprecation with dates: the Deprecation and Sunset headers

RFC 9745 (IETF Proposed Standard, 2025, Dalal and Wilde) defines the `Deprecation` HTTP response header, which "allows a server to communicate to a client application that the resource in the context of the message will be or has been deprecated", with a date that may be in the future or the past; the optional `Sunset` header (RFC 8594) says when the resource is expected to stop responding, and its timestamp "MUST NOT be earlier than the one given in the Deprecation header field"; a deprecation without a Sunset date "doesn't imply the resource will go offline" [VERIFIED: https://www.rfc-editor.org/rfc/rfc9745, published 2025].

[ASSUMPTION/JUDGEMENT] Chapter 26's "Pulled Rug" pattern has a precise antidote in these sources: a deprecation is a *date pair* (announced, removed) plus *usage monitoring* plus *consumer sign-off*. A vendor that publishes only "deprecated" with no date has not deprecated anything; it has warned.

### 3.6 Webhooks done well: the Standard Webhooks specification

Standard Webhooks (version 1.0.0, Apache 2.0) is "Open source tools and guidelines to send webhooks easily, securely and reliably"; its technical steering committee members are listed as employees of Zapier, Twilio, Lob, Mux, ngrok, Supabase, Svix and Kong, and its compatible-implementations list includes Svix, Kong, Twilio, Lob, ngrok, OpenAI, Anthropic and Google Gemini [VERIFIED: https://www.standardwebhooks.com/, n.d., accessed 2026-11]. The specification defines three headers: `webhook-id` (unique per event, unchanged across retries), `webhook-timestamp` (Unix seconds) and `webhook-signature` (a space-separated list, enabling zero-downtime key rotation); the signed content is `id.timestamp.body`; symmetric signatures are HMAC-SHA256, base64, prefixed `v1`, asymmetric ed25519 prefixed `v1a`; consumers should check the timestamp "within some allowable tolerance of the current timestamp to prevent replay attacks" and "Use the `webhook-id` header as an idempotency key"; senders should follow "a retry schedule spanning multiple days, with an exponential backoff" plus jitter (the example runs to 75 hours); the spec does not address ordering [VERIFIED: https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md, version 1.0.0, accessed 2026-11].

Stripe's own scheme predates and matches it: a `Stripe-Signature` header with `t=` timestamp and `v1=` HMAC-SHA256 over `timestamp.payload`, a default tolerance of five minutes, constant-time comparison, secret rolling with up to 24 hours of overlap, and IP allow-listing as a second control [VERIFIED: https://docs.stripe.com/webhooks, n.d., accessed 2026-11].

| Property | Shopify | Stripe | Standard Webhooks |
| --- | --- | --- | --- |
| Signature | HMAC-SHA256 of raw body, app secret, `X-Shopify-Hmac-SHA256` | HMAC-SHA256 of `t.body`, `Stripe-Signature` | HMAC-SHA256 of `id.ts.body`, `webhook-signature` |
| Replay protection | `X-Shopify-Triggered-At` (advisory) | 5-minute default tolerance | Timestamp tolerance (unspecified) |
| Duplicate key | `X-Shopify-Webhook-Id` | event `id` | `webhook-id` |
| Retries | 8 over 4 hours; subscription deleted after 8 consecutive failures (API-created) | Up to 3 days, exponential backoff (live) | Multi-day exponential with jitter (recommended) |
| Ordering | Not guaranteed | Not guaranteed | Not addressed |
| Response | 2xx within 5 s total (1 s connect) | 2xx quickly, before business logic | — |

(Table from the three sources above.)

### 3.7 Rate limits

- **Shopify GraphQL Admin API**: a leaky bucket per app and store measured in cost points, refilling at 100 points/second (Standard), 200 (Advanced), 1,000 (Plus) and 2,000 (Shopify for enterprise / Commerce Components); default costs are 0 per scalar or enum, 1 per object, connections sized by `first`/`last`, and 10 per mutation; a single query may not exceed 1,000 points regardless of plan; the response's `extensions.cost` reports `requestedQueryCost`, `actualQueryCost` and `throttleStatus` (`maximumAvailable`, `currentlyAvailable`, `restoreRate`) [VERIFIED: https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits, n.d., accessed 2026-11] ⚠. Platform-wide: input arrays are capped at 250 items, pagination at 25,000 objects, a store with 500,000 variants may create at most 10,000 new variants per day (not on Plus), "The recommended backoff time is one second" [VERIFIED: https://shopify.dev/docs/api/usage/rate-limits, n.d., accessed 2026-11] ⚠.
- **Stripe**: 100 requests/second per account in live mode (25 in a sandbox), 25 requests/second per endpoint, a default global concurrency limit of 50 in-progress requests, `429 Too Many Requests` with a `Stripe-Rate-Limited-Reason` header (`global-rate`, `endpoint-rate`, `global-concurrency`, `endpoint-concurrency`, `resource-specific`); a read allocation of 500 GET requests per transaction over a rolling 30 days with a minimum of 10,000 per month, with Data Pipeline recommended "for a complete export of API data to your local database or provider"; flash sales that may exceed limits should be announced to support; load-testing against the sandbox is discouraged because its limits are lower and latency unrealistic [VERIFIED: https://docs.stripe.com/rate-limits, n.d., accessed 2026-11] ⚠.

[ASSUMPTION/JUDGEMENT] Two consequences for chapters 26 and 33. A connector that syncs 50,000 variants' stock through single mutations at 10 points each needs 500,000 points, that is 83 minutes at the Standard rate before any other app runs: bulk and batch endpoints are a necessity, not an optimisation. And rate limits are per *store*, shared by all apps: at peak, a chatty analytics app can starve the WMS connector, which is why the integration inventory should record each integration's expected call rate.

### 3.8 Consumer-driven contracts and Pact

Ian Robinson (Thoughtworks) coined "consumer-driven contracts" in June 2006: a *provider contract* is the provider's complete, authoritative offering; a *consumer contract* is one consumer's expectations, binding only once the provider accepts it; a *consumer-driven contract* is the provider contract shaped by the union of its consumers' contracts — "derived contracts" that "emerge to meet consumer expectations and demands" [VERIFIED: https://martinfowler.com/articles/consumerDrivenContracts.html, published 2006-06-12] **(evidence age: 20 years; the idea is unchanged)**. Pact describes itself as "a code-first tool for testing HTTP and message integrations using contract tests", "a code-first consumer-driven contract testing tool"; the contract is generated by running the consumer's tests, so only the parts of an API consumers actually use are verified ("contract by example"), and Pact distinguishes this from provider contract testing against an OpenAPI document [VERIFIED: https://docs.pact.io/, last updated 2026-08-25].

[ASSUMPTION/JUDGEMENT] Inside a company, consumer-driven contracts are feasible between the order service and the WMS adapter. With a SaaS vendor they are not: the vendor's OpenAPI or GraphQL schema is the contract, and the merchant's defence is a schema-validation test of the vendor's sandbox run against each new version before it becomes the default.

**For newcomers (Part 3).** *API contract*: the written description (schema, fields, errors, limits) of what a system promises to accept and return. *Versioning*: naming contract generations (by date or number) so that a consumer can say which one it relies on. *Deprecation*: the announced, dated withdrawal of part of a contract; *sunset* is the date it stops working. *Rate limit*: the maximum number of calls (or cost points) a consumer may make per second; exceeding it returns an error instead of data.

**Architecture implications (Part 3)** [ASSUMPTION/JUDGEMENT]. *Starting*: the merchant consumes contracts and owns none; the one obligation is to know which API versions its apps and connectors pin and when they expire. *Growing*: the first custom integration should be built against a pinned version with the upgrade date in the integration inventory; webhook handlers verify signatures and deduplicate from day one. *Omnichannel*: the merchant becomes a provider too (to agencies, marketplaces connectors, stores): publish an OpenAPI or AsyncAPI document, version it, deprecate with dates and monitored usage, and sign webhooks the Standard Webhooks way. *Group*: API guidelines in the Zalando mould, a schema registry for events, contract tests in CI, and a vendor-contract clause on deprecation notice periods.

---

## PART 4: Identity and master data — one customer, one product

### 4.1 Customer identity in commerce

- **Accounts, guests and store customers on one platform.** Shopify's customer accounts let customers "view order history, check order statuses, edit their profile, and act on their orders"; a customer who is not logged in can open the pre-authenticated order-status page from an order notification e-mail and is asked to log in only for other account pages; "As of February 26, 2026, legacy customer accounts are deprecated" and all merchants must move to the new version [VERIFIED: https://shopify.dev/docs/apps/build/customer-accounts, n.d., accessed 2026-11] ⚠. Orders created through Shopify POS and draft orders carry a staff ID that the Business Central connector maps to a salesperson, showing that store and online orders land in one customer and order model on that platform [VERIFIED: https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-orders, published 2026-10-14].
- **Merging duplicates is a product feature with explicit survivorship rules.** Shopify's `customerMerge` mutation (API version 2026-10) "Merges two customers"; the two ids "don't guarantee which customer is kept": if `overrideFields.customerIdOfEmailToKeep` is given, that customer survives; else the one with an e-mail; if both have e-mails, an `enabled` account wins over other states, then marketing-consent state decides, else the second id is kept; per-field overrides exist for first and last name; the result is an asynchronous job, `resultingCustomerId` must be treated "as authoritative", and `customerMergePreview` shows the outcome in advance [VERIFIED: https://shopify.dev/docs/api/admin-graphql/latest/mutations/customerMerge, API version 2026-10, accessed 2026-11].
- **Consent travels with the identity.** `customerEmailMarketingConsentUpdate` records a customer's e-mail marketing state (`SUBSCRIBED`, `UNSUBSCRIBED`, `PENDING`; `NOT_SUBSCRIBED`, `REDACTED` and `INVALID` are read-only), the opt-in level, and "when and where the customer gave or withdrew consent"; the customer "must have an email address to update their consent" [VERIFIED: https://shopify.dev/docs/api/admin-graphql/latest/mutations/customerEmailMarketingConsentUpdate, accessed 2026-11].

[ASSUMPTION/JUDGEMENT] The Familiar Stranger of chapter 27 (one person as web account, store customer and newsletter subscriber) is the normal case, not the edge case, because each touchpoint creates an identity with a different key: e-mail for the web, loyalty card or phone for the store, e-mail again (possibly another one) for the newsletter, company id plus contact for wholesale. Shopify's merge rules are a public, dated example of what "survivorship" means in practice; most platforms have a comparable but undocumented rule, which is why the entity–owner table must name the customer-master.

### 4.2 Matching and merging: record linkage

Record linkage (also entity resolution, data matching, deduplication) is finding records in one or more data sets that refer to the same real-world entity when no shared identifier exists. Its lineage: Dunn (1946, *American Journal of Public Health*), Newcombe et al. (1959, *Science*: agreement on a rare value is stronger evidence than agreement on a common one) and Fellegi and Sunter (1969, *Journal of the American Statistical Association*, "A Theory for Record Linkage"). The Fellegi–Sunter model scores each candidate pair by a likelihood ratio built from m-probabilities (chance a field agrees given a true match) and u-probabilities (chance it agrees by coincidence), and classifies against two thresholds into match, non-match and "possible match" for clerical review; deterministic (rule-based) linkage needs ever more rules to cope with nicknames, typos and missing values; blocking (comparing only pairs that agree on a key) makes linkage feasible — two files of a million records would otherwise yield about 10^12 pairs — at the price of missing true matches that disagree on the blocking key [WIDELY REPORTED: https://en.wikipedia.org/wiki/Record_linkage, accessed 2026-11; the 1969 paper itself refused fetching (HTTP 403)].

[ASSUMPTION/JUDGEMENT] For commerce the practical rules follow directly: normalise before matching (lower-case e-mail, E.164 phone, postal-code format), block on e-mail or phone, score name plus address, auto-merge only above a high threshold, queue the middle band for a human, and never merge on name plus city alone. Keep the merge reversible (a merge log) because a wrong merge leaks one customer's orders into another's account, which is a privacy incident (Part VIII).

### 4.3 Master data management, the golden record and survivorship

Informatica (a leading MDM vendor) describes master data management as creating "a single master record for each person, place, or thing in a business", the master record being "also known as a 'golden record' or 'best version of the truth'", with customer (B2B and B2C), product, supplier, reference, location, asset and employee domains; MDM software is said to "identify, match, and merge data across the systems that hold it" and to "capture where the data came from, and create an audit trail of changes" [VERIFIED: https://www.informatica.com/resources/articles/what-is-master-data-management.html, n.d., accessed 2026-11]. Profisee (another MDM vendor) defines a golden record as "a complete and accurate version of a data point stored in a master data management solution" and survivorship rules as the rules "prioritized within the system when there are conflicting entries", giving source priority (for example inventory software over CRM), recency, and completeness as the usual rule types [VERIFIED: https://profisee.com/blog/what-is-a-golden-record/, published 2025-08-26]. Gartner's MDM glossary entry refused fetching. DAMA's DMBOK, "the globally recognized framework for data management", had a 2.0 revision launched in 2024 [VERIFIED: https://www.dama.org/cpages/body-of-knowledge, n.d., accessed 2026-11].

[ASSUMPTION/JUDGEMENT] Chapter 27 should keep MDM small. For a merchant below Group stage the "MDM system" is a decision, not a product: for each master entity (customer, product, supplier, location) name the system of record, the survivorship rule per attribute, and the merge process. A PIM is product MDM by another name; a CDP is customer MDM for marketing purposes; the ERP is usually supplier and location master. Buying a separate MDM platform is a Group-stage move driven by several brands or acquisitions.

### 4.4 Customer data platforms

The CDP Institute's definition (its 2026 wording): a CDP is "software that creates and maintains a persistent, unified customer record that is accessible to other systems"; "The CDP assumes primary responsibility for defining and maintaining customer identity" and for "providing a unified interface through which customer data services are governed and made operational"; it must ingest data from any source and make the data usable by other systems. The category was named by David Raab in 2013; the Institute was founded in 2016 [VERIFIED: https://www.cdpinstitute.org/learning-center/what-is-a-cdp/, n.d. (definition "as of 2026"), accessed 2026-11].

Twilio Segment's Identity Resolution (part of Unify, Business tier) "merges the complete history of each customer into a single profile" across web, mobile, server and third-party touchpoints using "an online and offline ID graph with support for cookie IDs, device IDs, emails, and custom external IDs"; `userId`, `anonymousId` and `groupId` are treated as case-insensitive, anonymous sessions are merged into identified ones, "multiple external IDs get matched to one persistent ID", Merge Protection uses "a priority trust algorithm" against non-unique anonymous IDs, and customisable ID rules can "enforce uniqueness on select external IDs"; the Profile API must be used server-side only [VERIFIED: https://www.twilio.com/docs/segment/unify/identity-resolution, last modified 2026-06-04]. Salesforce Data Cloud's identity resolution is organised in *rulesets* of match rules (exact, fuzzy, normalised methods) and reconciliation rules that pick the surviving value by frequency, recency or source object; the official help and Trailhead pages could not be fetched, so this rests on search-result summaries only [WIDELY REPORTED: https://trailhead.salesforce.com/content/learn/projects/quick-start-create-identity-resolution-ruleset/get-started-with-identity-resolution-ruleset, accessed 2026-11 via search summary] ⚠.

[ASSUMPTION/JUDGEMENT] The CDP's identity graph and an MDM golden record solve the same matching problem for different consumers (marketing activation vs operational truth). The book's advice: do not let the CDP become the system of record for the customer that service agents and the ERP use; it is a *copy* built for audiences, and copies are allowed to be fuzzier than records that drive invoices and refunds.

### 4.5 Product identity: GTIN, SKU and internal id

"GTIN stands for Global Trade Item Number", a GS1 identification key for a trade item; GTIN-8 (eight digits, small items outside North America), GTIN-12 (twelve digits, "synonymous with UPC", the only form that fits a UPC-A barcode), GTIN-13 (thirteen digits, synonymous with EAN, fits an EAN-13 barcode) and GTIN-14 (fourteen digits, for groupings such as cases, not for point of sale) [VERIFIED: https://www.gs1us.org/upcs-barcodes-prefixes/what-is-a-gtin, n.d. (© 2026), accessed 2026-11]. The GS1 global pages on the GTIN and the GTIN Management Standard (which rules govern when a change to a product requires a new GTIN) refused fetching; chapter 06's catalog brief should carry those rules.

Business Central's connector shows the three identifiers side by side: the Shopify *SKU* field may hold the ERP's item number, item number plus variant code with a separator, or the vendor's item number; the Shopify *barcode* is matched against the ERP's item references of barcode type; and the ERP's own `Item No.` plus `Variant Code` is the internal key; when an export finds "an existing variant with a matching SKU or barcode" the connector links instead of creating [VERIFIED: https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-items, published 2026-10-16].

| Identifier | Who assigns | Scope | What it is good for | What it is not |
| --- | --- | --- | --- | --- |
| GTIN (EAN/UPC) | Brand owner via GS1 | Global, one per sellable trade item | Marketplace listings, retail scanning, matching across companies | An internal key (resellers of the same item share it; variants of packaging differ) |
| SKU | Merchant | Internal, often per variant | Warehouse, stock, merchandising | Stable across systems unless governed (connectors overload it) |
| Internal id | Each system | Per system | Joins inside that system | Meaningful to any other system |
| Marketplace id (ASIN etc.) | Marketplace | Per marketplace | Listings and orders on that channel | Yours |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis. The cross-reference table (GTIN ↔ SKU ↔ internal ids ↔ channel ids) is the product-identity master and belongs to the PIM where there is one and to the ERP where there is not.

### 4.6 Consent linked to identity

The GDPR defines consent as "any freely given, specific, informed and unambiguous indication of the data subject's wishes by which he or she, by a statement or by a clear affirmative action, signifies agreement to the processing of personal data relating to him or her" (Article 4(11)); "Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented" (Article 7(1)) [VERIFIED: http://publications.europa.eu/resource/celex/32016R0679 (Regulation (EU) 2016/679, Official Journal text, English), published 2016-05-04]. The "demonstrate" duty is why Shopify's consent mutation records "when and where" (Section 4.1), and why a merge must carry consent forward with its evidence rather than recompute it. The regulation brief (`trust`) owns the legal detail.

**For newcomers (Part 4).** *Customer identity*: the set of keys (account id, e-mail, phone, loyalty number, company contact) that different systems use for the same person, and the rules that link them. *Golden record*: the one assembled record per customer or product that the business treats as true, built by merging sources under survivorship rules. *Master data*: the slowly changing reference entities (customers, products, suppliers, locations) that transactions refer to; master data management is deciding who owns them and how copies are kept in step. *GTIN*: the globally unique product number behind the EAN/UPC barcode, assigned by the brand owner through GS1. *CDP*: software that builds a unified customer profile from many sources for marketing use.

**Architecture implications (Part 4)** [ASSUMPTION/JUDGEMENT]. *Starting*: the platform's customer record is the master; the only rule is one e-mail per customer and a periodic duplicate merge. *Growing*: the first store and wholesale accounts bring new keys; decide the customer master (platform, ERP or CRM) and the product master (platform, ERP or PIM), and build the cross-reference table for product ids before the first marketplace. *Omnichannel*: a matching process with thresholds and review, consent stored with evidence on the master, a PIM as product master; a CDP if marketing needs audiences, kept as a copy. *Group*: an MDM function (or platform) across brands, with survivorship rules per attribute and a merge log that privacy can audit.

---

## PART 5: Data and analytics — counting the same thing everywhere

### 5.1 Operational versus analytical stores: warehouses and the lakehouse

Snowflake describes its architecture as "a hybrid of traditional shared-disk and shared-nothing database architectures" in three layers: database storage (Snowflake tables, Apache Iceberg tables and hybrid tables), compute in independent "virtual warehouses" so that one does not affect another, and cloud services for security, metadata and query optimisation [VERIFIED: https://docs.snowflake.com/en/user-guide/intro-key-concepts, n.d., accessed 2026-11]. BigQuery calls itself "a fully managed serverless data warehouse" and cites its "separation of compute and storage layers" [VERIFIED: https://docs.cloud.google.com/bigquery/docs/introduction, n.d., accessed 2026-11]. Databricks' co-founders argued at CIDR 2021 that the warehouse "will wither in the coming years and be replaced by a new architectural pattern, the Lakehouse", based on open direct-access formats (Parquet, ORC), first-class ML support and state-of-the-art performance; they describe the then-dominant "two-tier data lake + warehouse architecture" (data lands in a lake, is "ETLed" again into a warehouse) and its problems: reliability (keeping lake and warehouse consistent), data staleness, limited support for advanced analytics, and total cost [VERIFIED: https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf (Armbrust, Ghodsi, Xin, Zaharia, *Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics*, CIDR 2021), published 2021-01].

[ASSUMPTION/JUDGEMENT] The operational/analytical split the book needs is simpler than the vendors' architecture: operational stores answer "what is the state of this order now" for one order at a time and must never be slowed by a report; analytical stores answer "how many orders yesterday by channel" over all orders and tolerate hours of lag. The failure is running the second kind of question against the first kind of store on Black Friday (chapter 33), or trusting the second kind of store for the first kind of question ("the dashboard says it shipped").

### 5.2 Extract-and-load from SaaS: ELT tools and commerce connectors

- **Fivetran** charges by monthly active rows (MAR, counting inserts, updates and deletes; re-synced unchanged rows and initial loads are excluded), with a per-connection cost curve that falls with volume and varies by plan; the Free plan covers 500,000 MAR; Standard offers 15-minute syncs and "700+ managed connectors", Enterprise 1-minute syncs; a worked example on the page prices four marketing connections at $511.15 per month; transformations are priced per model run ($0.01 for runs 5,001–30,000) [VERIFIED: https://www.fivetran.com/pricing, n.d. (page titled 2026), accessed 2026-11] ⚠. Fivetran's Shopify connector pages returned only navigation and are not cited.
- **Airbyte's Shopify source** (version 4.3.5, changelog entry 2026-11-03) reads from the REST Admin API, the GraphQL Admin API and the GraphQL Bulk API; supports Full Refresh and Incremental (Append, and Deduped for some streams) with each record's update time as cursor and an optional lookback window "to catch late updates"; captures deletions for orders, products (a separate Deleted Products stream), collections and price rules; offers streams for orders, order refunds, products, variants, customers, transactions, fulfillments, inventory items and levels, locations, discount codes, metafields and customer-journey summaries; backs off and retries on `429`, and notes known gaps such as transactions created before their order [VERIFIED: https://docs.airbyte.com/integrations/sources/shopify, changelog to 2026-11-03, accessed 2026-11] ⚠.
- **Platform-side exports** exist to relieve the API: Shopify bulk operations (Section 1.3) and Stripe's Data Pipeline, recommended by Stripe "for a complete export of API data" instead of GET-heavy integrations (Section 3.7).

[ASSUMPTION/JUDGEMENT] Two architecture facts hide in the Airbyte page. Incremental extraction by `updated_at` plus a lookback window is the same reconciliation sweep as Section 1.3, applied to analytics; and a deleted or edited order that the connector misses becomes a permanent discrepancy between the warehouse and the platform — one of the roots of the three order counts (Section 5.5).

### 5.3 Event streaming in retail

A practitioner account by Walmart's former director of engineering (published on Confluent's blog, 4 May 2020, with the disclaimer that the views are the author's and Walmart does not endorse the products described) describes Walmart's inventory backend: more than ten event sources, each with its own schema, were normalised by Kafka Streams into a canonical inventory event feeding a debit/credit model per item–store pair; "Each item-store combination always maps to one specific partition, so only one consumer processes it", preventing concurrent updates to the same item–store; producer `acks=1` was chosen as the reliability/latency balance; "Kafka is at the heart of Walmart's inventory backend architecture" [VERIFIED: https://www.confluent.io/blog/walmart-real-time-inventory-management-using-kafka/, published 2020-05-04 (Suman Pattnaik)] **(evidence age: 6 years)**. A Confluent-affiliated blog cites Walmart's platform at 8,500 nodes processing 11 billion events per day and names Target, AO.com and Nuuly as retail Kafka users [WIDELY REPORTED: https://www.kai-waehner.de/blog/2021/01/28/apache-kafka-in-retail-use-cases-architecture-case-studies-examples/, 2021]. Zalando's Nakadi (Section 3.1) is the European example of an in-house event bus with schema enforcement, archived in 2024.

[ASSUMPTION/JUDGEMENT] For the book's merchant, "event streaming" arrives at Omnichannel stage as a managed Kafka (or a cloud equivalent) carrying order and stock events to the OMS, WMS, ERP connector and the warehouse at once, with partitioning by order id and by SKU+location. The Walmart design is the Group-stage version of the same idea.

### 5.4 The metrics layer

Benn Stancil's 2021 essay identified "the missing piece of the modern data stack": "The core problem is that there's no central repository for defining a metric"; metric logic lives in individual BI tools or even single charts, is recomputed by analysts and engineers, and drifts; "Local solutions don't work because BI tools aren't the only way companies consume data"; a metrics layer would define each metric once, generate SQL on demand and serve every tool [VERIFIED: https://benn.substack.com/p/metrics-layer, published 2021-04-22]. The products: dbt's Semantic Layer (powered by MetricFlow) lets teams define metrics on top of models; "moving metric definitions out of the BI layer and into the modeling layer allows data teams to feel confident that different business units are working from the same metric definitions, regardless of their tool of choice. If a metric definition changes in dbt, it's refreshed everywhere it's invoked"; available on Starter and Enterprise tiers; a dbt MCP server lets AI tools query governed metrics [VERIFIED: https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl, last updated 2026-09-29] ⚠. LookML is "the language that is used in Looker to create semantic data models", describing "dimensions, aggregates, calculations, and data relationships in your SQL database" once, in one place [VERIFIED: https://docs.cloud.google.com/looker/docs/what-is-lookml, n.d., accessed 2026-11]. Cube's semantic layer "is built on four pillars: data modeling, access control, caching, and APIs" (SQL, REST, GraphQL) and now brands itself an "agentic analytics platform" [VERIFIED: https://docs.cube.dev/docs/introduction, n.d., accessed 2026-11] ⚠.

### 5.5 The three order counts: metric definitions

The platform's own definitions show how many choices hide in "orders" and "sales". Shopify's ShopifyQL sales schema (API version 2026-10) defines `orders` as "Counts each order one time within the selected sales, even when the order contains multiple items"; `gross_sales` as "Top-line sales revenue before discounts and returns are taken out", excluding "taxes, shipping, duties, and fees"; `discounts`; `sales_reversals` (replacing `returns`, deprecated in 2026-10) as "Value removed from orders through refunds, returns, cancellations, or edits"; `net_sales` as "gross sales - discounts - sales reversals"; `taxes`; `shipping_charges` after shipping discounts; and `total_sales` as "net sales + additional fees + duties + shipping charges + taxes"; "Each row records one event, and a single order can produce multiple rows if refunds or adjustments follow" [VERIFIED: https://shopify.dev/docs/api/shopifyql/2026-10/schemas/sales_revenue/sales, API version 2026-10, accessed 2026-11] ⚠.

Google Analytics 4's e-commerce model counts differently: the `purchase` event requires `transaction_id` ("The unique identifier of a transaction"; "The `transaction_id` parameter helps you avoid getting duplicate events for a purchase"), `currency`, `value` ("the sum of (price * quantity) for all items", excluding shipping and tax) and `items`; `refund` is a separate event [VERIFIED: https://developers.google.com/analytics/devguides/collection/ga4/reference/events, n.d., accessed 2026-11; https://developers.google.com/analytics/devguides/collection/ga4/ecommerce, n.d., accessed 2026-11]. GA4's BigQuery export delivers raw event-level data that "does not include the processing and value additions found in standard Analytics reports, so figures can differ from the interface"; standard properties are limited to 1 million exported events per day; streaming export costs $0.05 per GB and is best-effort [VERIFIED: https://support.google.com/analytics/answer/9358801, n.d., accessed 2026-11] ⚠. Analytics vendors that reconcile Shopify against GA4 list the usual causes of the gap: subscription renewals and app-created orders that never fire a browser event, POS and draft orders, ad blockers and refused consent, refunds that Shopify nets and GA4 does not unless `refund` is sent, currency and tax/shipping inclusion, and different attribution windows [WIDELY REPORTED: https://docs.getelevar.com/docs/why-is-google-analyticsga4-under-or-over-reporting, accessed 2026-11 via search summary; https://intercom.help/polar-app/en/articles/8370728-why-do-shopify-and-polar-show-more-transactions-than-ga4, accessed 2026-11 via search summary].

[ASSUMPTION/JUDGEMENT] The three order counts of chapter 28 have three honest sources: (1) **definition** — created vs paid vs fulfilled; gross vs net; order date vs refund date; test, draft and POS orders in or out; (2) **collection** — a browser event is lost to blockers and consent, a webhook is missed, a connector skips a late edit; (3) **time** — store time zone vs UTC, order date vs settlement date (Stripe groups payouts by estimated arrival, Section 2.9). The remedy is one metric definition owned by one team, implemented once in a metrics layer, with a reconciliation between the platform's count and the warehouse's count published alongside the number.

### 5.6 Governance, ownership and data products

Zhamak Dehghani's May 2019 article proposed the data mesh: domains "host and serve their own datasets" instead of handing them to a central team (the domain as "architectural quantum"), domain teams treat "data assets as their products" with analysts and data scientists as customers, a shared self-serve data platform, and global standards so that cross-domain data interoperates [VERIFIED: https://martinfowler.com/articles/data-monolith-to-mesh.html, published 2019-05-20].

Sharing data with partners without copying it is a product feature of the warehouses: in Snowflake Secure Data Sharing "no actual data is copied or transferred between accounts"; a provider offers a share, or "a Listing, in which you offer a share and additional metadata as a data product to one or more accounts"; "consumers query the provider's data in place through a read-only database that they create from the share"; cross-region and cross-cloud sharing needs a listing with auto-fulfilment [VERIFIED: https://docs.snowflake.com/en/user-guide/data-sharing-intro, n.d., accessed 2026-11]. Databricks documents "OpenSharing", "an open protocol developed by Databricks for secure data sharing with other organizations" that "works regardless of the computing platforms those organizations use", with open sharing "with any user, whether or not they have access to Databricks" and a Databricks-to-Databricks mode; the fetched page (last updated 2026-10-27) does not use the older name Delta Sharing [VERIFIED: https://docs.databricks.com/aws/en/delta-sharing/, last updated 2026-10-27] ⚠ (product naming in flux).

[ASSUMPTION/JUDGEMENT] The commerce reading of data mesh is modest: the order domain owns the order dataset and its metric definitions; the inventory domain owns stock snapshots; the data team owns the platform and the cross-domain standards (keys, time zones, currency). Data products for partners (sell-through to a brand, listings performance to a marketplace seller, stock feeds to a wholesale customer) are the Omnichannel-stage reason to formalise ownership; the warehouse-sharing features above make the delivery cheap, which moves the cost to definitions and consent.

### 5.7 Real-time dashboards

[ASSUMPTION/JUDGEMENT] No vendor-neutral source on when real-time dashboards mislead was found; the evidence is indirect. GA4's intraday export is "best-effort and may have gaps" and some attribution lags "by up to 24 hours"; Stripe's reconciliation data "might" lag the payout; Shopify's reversals arrive as later rows against earlier orders (Sections 5.5, 2.9). A real-time dashboard therefore shows a number that will be revised. The book's rule: show operational signals in real time (orders per minute, checkout errors, queue depth, DLQ depth) because they are *rates* used for action, and show business metrics (revenue, conversion, returns) on a lag with a definition and a revision policy.

**For newcomers (Part 5).** *Data warehouse / lakehouse*: a separate store where copies of all systems' data are kept for analysis, so questions over millions of orders do not slow the shop. *ELT*: extract data from a SaaS system, load it raw into the warehouse, transform it there (the order of the letters is the point). *Metrics layer*: one place where "net sales" or "order" is defined as code, so every dashboard and tool computes it the same way. *Event stream*: a durable, ordered log of events (order placed, stock changed) that many systems read at their own pace. *Data product*: a dataset with an owner, a definition, a contract and a consumer, shared inside or outside the company.

**Architecture implications (Part 5)** [ASSUMPTION/JUDGEMENT]. *Starting*: the platform's reports and GA4; the only governance is knowing their two definitions of "order" differ. *Growing*: a warehouse via an ELT connector, a modelling tool, three or four agreed metric definitions, and a monthly reconciliation of warehouse orders against platform orders. *Omnichannel*: an event stream feeding both operations and the warehouse, a metrics layer, domain ownership of definitions, data products for key partners, and real-time operational dashboards separated from lagged business metrics. *Group*: a shared data platform with federated ownership across brands, partner data sharing through warehouse-native sharing, and a data-governance function that also serves privacy (Part VIII).

---

## Key numbers

| Number | Meaning | Source | Date |
| --- | --- | --- | --- |
| 8 retries over 4 hours; deletion after 8 consecutive failures | Shopify HTTPS webhook retry policy | shopify.dev webhooks/subscribe/https | n.d., accessed 2026-11 ⚠ |
| 1 s connect, 5 s total | Shopify webhook response timeout | same | n.d. ⚠ |
| Up to 3 days, exponential backoff | Stripe webhook retries (live mode) | docs.stripe.com/webhooks | n.d. ⚠ |
| 5 minutes | Stripe signature timestamp tolerance (default) | same | n.d. |
| 16 | Maximum Stripe event destinations per account | same | n.d. ⚠ |
| 255 characters; ≥24 hours | Stripe idempotency key length; key pruning (API v1) | docs.stripe.com/api/idempotent_requests | n.d. ⚠ |
| Every 3 months; ≥12 months support; 9 months overlap | Shopify API versioning | shopify.dev versioning | n.d. ⚠ |
| 2026-10 (until 2027-10-16) | Latest stable Shopify API version at fetch | same | 2026-11 ⚠ |
| 2024-10-01; 2025-04-01 | Shopify REST Admin API legacy date; GraphQL-only for new public apps | shopify.dev admin-rest | n.d. ⚠ |
| Monthly, no breaking changes; 2 major releases/year | Stripe release process since 2024-09-30.acacia | stripe.com blog | 2024-10-01 |
| 2026-10-28.endive | Current Stripe API version at fetch | docs.stripe.com/api/versioning | 2026-11 ⚠ |
| 100 / 200 / 1,000 / 2,000 points per second | Shopify GraphQL Admin rate by plan (Standard/Advanced/Plus/enterprise) | shopify.dev graphql-admin rate-limits | n.d. ⚠ |
| 10 points; 1,000 points | Shopify mutation cost; single-query maximum | same | n.d. ⚠ |
| 100 rps live, 25 sandbox, 25 per endpoint, 50 concurrent | Stripe rate and concurrency limits | docs.stripe.com/rate-limits | n.d. ⚠ |
| 500 reads per transaction; 10,000/month minimum | Stripe read allocation | same | n.d. ⚠ |
| 5 concurrent; 10 days; 1 week | Shopify bulk queries per shop (from 2026-01); completion limit; URL expiry | shopify.dev bulk operations | n.d. ⚠ |
| 15–30 minutes | Business Central → Shopify inventory sync frequency recommended | learn.microsoft.com synchronize-inventory | 2026-10-14 ⚠ |
| > 50% fewer calls | Full jitter vs plain exponential backoff, 100 clients (simulation) | AWS Architecture Blog | 2015-03-04 |
| $2,000/month floor; $50K pre-commit | MuleSoft packages; Pre-Commit minimum | mulesoft.com pricing | n.d. ⚠ |
| $99/month plus usage | Boomi Pay-As-You-Go | boomi.com pricing | n.d. ⚠ |
| €20 / €50 / €667 per month | n8n Starter / Pro / Business (annual) | n8n.io pricing | n.d. ⚠ |
| 1,000 credits/month | Make free plan | make.com pricing | n.d. ⚠ |
| 500,000 MAR | Fivetran free plan allowance | fivetran.com pricing | n.d. ⚠ |
| 1 million events/day; $0.05/GB | GA4 BigQuery daily export limit (standard); streaming export price | support.google.com/analytics | n.d. ⚠ |
| 2024-01-25 | CloudEvents CNCF graduation | cncf.io | n.d. |
| 2024-06-07 | Zalando Nakadi archived | github.com/zalando/nakadi | 2024 |
| 2026-02-26 | Shopify legacy customer accounts deprecated | shopify.dev customer-accounts | n.d. ⚠ |
| 8,500 nodes; 11 billion events/day | Walmart Kafka platform (secondary, vendor-affiliated) | kai-waehner.de | 2021 (WIDELY REPORTED) |

## Open questions / not verifiable

- **Gartner definitions** of iPaaS and MDM could not be fetched; the iPaaS wording is cited through an encyclopaedia entry dated 2015.
- **GS1 GTIN Management Standard** (when a product change requires a new GTIN; the 2019 non-reuse rule) was not reachable; the catalog brief should supply it.
- **Fellegi–Sunter 1969** is cited through an encyclopaedia; the paper was not fetched.
- **Salesforce Data Cloud identity resolution** rests on search summaries of Trailhead; no primary page was fetched.
- **Fivetran's Shopify connector** behaviour (API, incremental mechanism, tables) could not be read; Airbyte stands in.
- **Shopify's help-centre definitions** of sales metrics were not fetched; the ShopifyQL developer schema carries the same definitions and is cited.
- **Shopify idempotency key retention** and the API version in which `@idempotent` was introduced are not stated on the page.
- **A vendor-neutral source on "integration debt"** was not found; the term is defined operationally in Section 1.7.
- **No public reconciliation variance figures** (what share of SKUs disagree between WMS and shop in a typical merchant) exist; the ledger's 2.3% is illustrative.
- **Databricks' sharing product name** (Delta Sharing vs OpenSharing) appears to be changing; verify before print.
- **Kafka in European retail** (Zalando beyond Nakadi, Otto, bol.com, Rewe) produced no fetchable primary engineering source in this session.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Integration Styles (Enterprise Integration Patterns) | Hohpe & Woolf | 2003/2023 | https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html |
| Starbucks Does Not Use Two-Phase Commit | Gregor Hohpe | 2004 | https://www.enterpriseintegrationpatterns.com/ramblings/18_starbucks.html |
| What do you mean by "Event-Driven"? | Martin Fowler | 2017 | https://martinfowler.com/articles/201701-event-driven.html |
| Debezium Features (3.7) | Debezium project | n.d. | https://debezium.io/documentation/reference/stable/features.html |
| Webhooks | Shopify (shopify.dev) | n.d. | https://shopify.dev/docs/apps/build/webhooks |
| HTTPS webhook delivery | Shopify | n.d. | https://shopify.dev/docs/apps/build/webhooks/subscribe/https |
| Bulk operations: queries | Shopify | n.d. | https://shopify.dev/docs/api/usage/bulk-operations/queries |
| Idempotent requests | Shopify | n.d. | https://shopify.dev/docs/api/usage/idempotent-requests |
| API versioning | Shopify | n.d. | https://shopify.dev/docs/api/usage/versioning |
| REST Admin API (legacy notice) | Shopify | n.d. | https://shopify.dev/docs/api/admin-rest |
| Rate limits (overview) | Shopify | n.d. | https://shopify.dev/docs/api/usage/rate-limits |
| GraphQL Admin API rate limits | Shopify | n.d. | https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits |
| customerMerge mutation (2026-10) | Shopify | 2026 | https://shopify.dev/docs/api/admin-graphql/latest/mutations/customerMerge |
| customerEmailMarketingConsentUpdate mutation | Shopify | n.d. | https://shopify.dev/docs/api/admin-graphql/latest/mutations/customerEmailMarketingConsentUpdate |
| Customer accounts | Shopify | n.d. | https://shopify.dev/docs/apps/build/customer-accounts |
| ShopifyQL sales schema (2026-10) | Shopify | 2026 | https://shopify.dev/docs/api/shopifyql/2026-10/schemas/sales_revenue/sales |
| Receive Stripe events in your webhook endpoint | Stripe | n.d. | https://docs.stripe.com/webhooks |
| Idempotent requests | Stripe | n.d. | https://docs.stripe.com/api/idempotent_requests |
| Versioning | Stripe | n.d. | https://docs.stripe.com/api/versioning |
| Rate limits | Stripe | n.d. | https://docs.stripe.com/rate-limits |
| Payout reconciliation report | Stripe | n.d. | https://docs.stripe.com/reports/payout-reconciliation |
| APIs as infrastructure: future-proofing Stripe with versioning | Brandur Leach, Stripe | 2017 | https://stripe.com/blog/api-versioning |
| Introducing Stripe's new API release process | Stripe | 2024 | https://stripe.com/blog/introducing-stripes-new-api-release-process |
| Transactional outbox | Chris Richardson, microservices.io | n.d. | https://microservices.io/patterns/data/transactional-outbox.html |
| Saga | Chris Richardson, microservices.io | n.d. | https://microservices.io/patterns/data/saga.html |
| Sagas (Proc. ACM SIGMOD 1987) | Garcia-Molina & Salem | 1987 | https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf |
| Exponential Backoff And Jitter | Marc Brooker, AWS | 2015 | https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/ |
| Using dead-letter queues in Amazon SQS | AWS | n.d. | https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html |
| Eventually Consistent | Werner Vogels | 2008 | https://www.allthingsdistributed.com/2008/12/eventually_consistent.html |
| Monitoring Distributed Systems (SRE book, ch. 6) | Google | 2017 | https://sre.google/sre-book/monitoring-distributed-systems/ |
| Kafka Design (4.4) | Apache Software Foundation | n.d. | https://kafka.apache.org/44/design/design/ |
| OpenAPI Specification v3.2.1 | OpenAPI Initiative | 2026 | https://spec.openapis.org/oas/latest.html |
| AsyncAPI Specification 3.0.0 | AsyncAPI Initiative | n.d. | https://www.asyncapi.com/docs/reference/specification/v3.0.0 |
| AsyncAPI 3.0.0 release notes | AsyncAPI Initiative | 2023 | https://www.asyncapi.com/blog/release-notes-3.0.0 |
| CloudEvents specification | CNCF CloudEvents | n.d. | https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md |
| CloudEvents project page | CNCF | n.d. | https://www.cncf.io/projects/cloudevents/ |
| JSON Schema specification | JSON Schema | n.d. | https://json-schema.org/specification |
| Nakadi (archived) | Zalando SE | 2015–2024 | https://github.com/zalando/nakadi |
| RESTful API Guidelines | Zalando SE | to 2026-03 | https://opensource.zalando.com/restful-api-guidelines/ |
| AIP-180 Backwards compatibility | Google | 2019–2025 | https://google.aip.dev/180 |
| RFC 9745: The Deprecation HTTP Response Header Field | IETF (Dalal, Wilde) | 2025 | https://www.rfc-editor.org/rfc/rfc9745 |
| Standard Webhooks (site) | Standard Webhooks | n.d. | https://www.standardwebhooks.com/ |
| Standard Webhooks specification 1.0.0 | Standard Webhooks | n.d. | https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md |
| Consumer-Driven Contracts | Ian Robinson (martinfowler.com) | 2006 | https://martinfowler.com/articles/consumerDrivenContracts.html |
| Pact documentation | Pact Foundation | 2026 | https://docs.pact.io/ |
| Cloud-based integration (iPaaS, Gartner definition) | Wikipedia | 2015 (retrieval) | https://en.wikipedia.org/wiki/Cloud-based_integration |
| MuleSoft pricing | Salesforce/MuleSoft | n.d. | https://www.mulesoft.com/anypoint-pricing |
| Boomi pricing | Boomi | n.d. | https://boomi.com/pricing/ |
| Workato pricing | Workato | n.d. | https://www.workato.com/pricing |
| Celigo pricing | Celigo | n.d. | https://www.celigo.com/pricing/ |
| Celigo Shopify–NetSuite Integration Template | Celigo | n.d. | https://www.celigo.com/integrations/shopify-netsuite/ |
| Make pricing | Make | n.d. | https://www.make.com/en/pricing |
| n8n pricing | n8n | n.d. | https://n8n.io/pricing/ |
| n8n Sustainable Use License | n8n | n.d. | https://github.com/n8n-io/n8n/blob/master/LICENSE.md |
| Get started with the Shopify Connector | Microsoft Learn | 2026-09-22 | https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/get-started |
| Synchronize items with Shopify | Microsoft Learn | 2026-10-16 | https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-items |
| Synchronize inventory with Shopify | Microsoft Learn | 2026-10-14 | https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-inventory |
| Synchronize and fulfill sales orders | Microsoft Learn | 2026-10-14 | https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-orders |
| What is a CDP? | CDP Institute | 2026 | https://www.cdpinstitute.org/learning-center/what-is-a-cdp/ |
| Identity Resolution | Twilio Segment | 2026-06-04 | https://www.twilio.com/docs/segment/unify/identity-resolution |
| Identity resolution ruleset (Trailhead, via search summary) | Salesforce | n.d. | https://trailhead.salesforce.com/content/learn/projects/quick-start-create-identity-resolution-ruleset/get-started-with-identity-resolution-ruleset |
| Record linkage | Wikipedia | n.d. | https://en.wikipedia.org/wiki/Record_linkage |
| What is master data management? | Informatica | n.d. | https://www.informatica.com/resources/articles/what-is-master-data-management.html |
| What Is a Golden Record in MDM? | Benjamin Bourgeois, Profisee | 2025 | https://profisee.com/blog/what-is-a-golden-record/ |
| DAMA Body of Knowledge | DAMA International | n.d. | https://www.dama.org/cpages/body-of-knowledge |
| What is a GTIN? | GS1 US | n.d. | https://www.gs1us.org/upcs-barcodes-prefixes/what-is-a-gtin |
| Regulation (EU) 2016/679 (GDPR), Official Journal text | Publications Office of the EU | 2016 | http://publications.europa.eu/resource/celex/32016R0679 |
| Key Concepts & Architecture | Snowflake | n.d. | https://docs.snowflake.com/en/user-guide/intro-key-concepts |
| Introduction to Secure Data Sharing | Snowflake | n.d. | https://docs.snowflake.com/en/user-guide/data-sharing-intro |
| BigQuery overview | Google Cloud | n.d. | https://docs.cloud.google.com/bigquery/docs/introduction |
| Lakehouse: A New Generation of Open Platforms (CIDR 2021) | Armbrust, Ghodsi, Xin, Zaharia | 2021 | https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf |
| OpenSharing / Delta Sharing | Databricks | 2026-10-27 | https://docs.databricks.com/aws/en/delta-sharing/ |
| Fivetran pricing | Fivetran | n.d. | https://www.fivetran.com/pricing |
| Shopify source connector | Airbyte | 2026-11-03 | https://docs.airbyte.com/integrations/sources/shopify |
| Walmart's Real-Time Inventory System using Kafka | Suman Pattnaik (Confluent blog) | 2020 | https://www.confluent.io/blog/walmart-real-time-inventory-management-using-kafka/ |
| Use Cases for Apache Kafka in Retail | Kai Waehner | 2021 | https://www.kai-waehner.de/blog/2021/01/28/apache-kafka-in-retail-use-cases-architecture-case-studies-examples/ |
| The missing piece of the modern data stack | Benn Stancil | 2021 | https://benn.substack.com/p/metrics-layer |
| dbt Semantic Layer | dbt Labs | 2026-09-29 | https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl |
| What is LookML? | Google Cloud (Looker) | n.d. | https://docs.cloud.google.com/looker/docs/what-is-lookml |
| Cube introduction | Cube | n.d. | https://docs.cube.dev/docs/introduction |
| GA4 recommended ecommerce events | Google | n.d. | https://developers.google.com/analytics/devguides/collection/ga4/ecommerce |
| GA4 event reference (purchase) | Google | n.d. | https://developers.google.com/analytics/devguides/collection/ga4/reference/events |
| [GA4] BigQuery Export | Google | n.d. | https://support.google.com/analytics/answer/9358801 |
| How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh | Zhamak Dehghani (martinfowler.com) | 2019 | https://martinfowler.com/articles/data-monolith-to-mesh.html |
| Why is GA4 under- or over-reporting? (via search summary) | Elevar | n.d. | https://docs.getelevar.com/docs/why-is-google-analyticsga4-under-or-over-reporting |
| Why do Shopify and Polar show more transactions than GA4? (via search summary) | Polar Analytics | n.d. | https://intercom.help/polar-app/en/articles/8370728-why-do-shopify-and-polar-show-more-transactions-than-ga4 |
