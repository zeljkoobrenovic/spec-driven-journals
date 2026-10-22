# Research brief: Listing syndication to portals, merchandising data and lead handling

Prepared 22 October 2026 for chapter writers of *Architecting a Vehicle Data and Dealer SaaS Platform*. The brief takes the dealer-software side of the wire. It covers how a dealer platform publishes stock to portals and ad channels, and how leads come back into the dealer's CRM and DMS. The brief is vendor-neutral. Companies appear because their integration contracts are public, not because the book endorses them.

**Relation to the sibling brief.** LISTED's `_journals/listing-systems-architecture/_research/brief-automotive.md` (19 October 2026) covers the *portal* side: Auto Trader UK's corporate facts and API catalogue, mobile.de's history and its Seller/Search/Ad Stream APIs, AutoScout24's platform, CarGurus, Cars.com, the ingestion pipeline inside a marketplace, and lead types from the portal's point of view. This brief does not repeat that material. It builds on it with:

- the *publisher's* contract details (idempotency, update and delete semantics, rate limits, image rules, equipment codes, quality and regulatory validation);
- two primary sources the sibling brief did not have: the **AutoScout24 Listing Creation API** and the **Marktplaats/2dehands API and Lead Delivery Webhook**;
- the **mobile.de Lead API** (version 2026-06-25);
- the ADF 1.0 lead standard, read in full, and STAR's 2025 Sales Lead API;
- Google and Meta vehicle feeds;
- lead-response research and the 2025–26 Auto Trader price and Deal Builder dispute, seen from the dealer side.

Where this brief needs a fact from the sibling brief, it says so.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page or document was fetched in this session (22 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. German and Dutch sources are quoted in English translation, and the brief says so. "n.d." means the page carries no publication date; such pages were accessed 2026-10.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, a vendor help page, a press summary). The page was fetched unless the tag says otherwise.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about a proprietary system that a company has not described carries this tag. Re-verify before printing it as fact, or present it explicitly as reference-architecture judgement.

**Research limitation.** The web-search quota shared with parallel researchers ran out about halfway through this session. After that point the evidence comes from direct fetches of known or discovered URLs: API documentation (including Docsify markdown sources and OpenAPI YAML), SEC EDGAR filings, company PDFs and newsrooms. As a result:

- **No primary feed specification was found for Cars.com, CarGurus, Autotrader.com (US), Motors.co.uk, CarGurus UK, Kleinanzeigen, Gaspedaal or AutoTrack.** CarGurus says in its 10-K that it gets data from inventory management systems, website providers, CRMs and DMSs, but publishes no feed specification. US feed mechanics in this brief therefore rest on secondary sources and judgement.
- **Facebook Marketplace's current dealer-inventory policy could not be checked.** Meta's catalog reference was read and is cited. Whether dealer inventory still appears on Marketplace in each market, as opposed to only in paid automotive inventory ads, is an open question.
- **The STAR Sales Lead BOD schema and the Salesforce Automotive Cloud STAR mapping page could not be read** (HTTP 403 and 404). Only STAR's June 2025 press release was verified.
- **CRM market shares** (VinSolutions, Elead/CDK, DealerSocket) and EU CRM tools could not be verified. Statements about them are judgement.
- **Portal price evidence outside the UK** (mobile.de, AutoScout24, Marktplaats price rises) was not found.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: product names, ownership, API versions, prices, rollout states.

**Evidence age.** Most API documentation here is current (changelogs run into 2026). The exceptions are flagged in place. ADF 1.0 dates from 2000, but it is still the working standard. The AutoScout24 API introduction cites "ACTA 2013" audience figures, so its marketing paragraph is stale even though the API itself is current. The Marktplaats API v1 reference says "1.0, May 19, 2019". The HBR lead-response study dates from 2011.

---

## PART 1: The syndication landscape by market

### 1.1 Who the dealer platform publishes to

| Market | Main automotive portals and channels | Public publisher contract found in this session | Evidence |
| --- | --- | --- | --- |
| NL | Marktplaats, AutoTrack, Gaspedaal (aggregator), AutoScout24.nl; Google and Meta ads | Marktplaats REST API (OAuth 2.0) + Lead Delivery Webhook; AutoScout24 Listing Creation API with `AutoTrack*` channels | Sections 2.1, 3.3 |
| BE | 2dehands/2ememain, AutoScout24.be; Traxio's AutoTrends (not verified) | Same Marktplaats API (multi-tenant); AutoScout24 API (Carpass rule) | Sections 2.1, 2.7 |
| DE | mobile.de, AutoScout24.de, Kleinanzeigen | mobile.de Seller API, Ad Stream, Lead API; AutoScout24 API (incl. `mobile_de` export channel) | Sections 2.1–2.9 |
| UK | Auto Trader UK, Motors, CarGurus UK, eBay Motors, Gumtree, Carwow, PistonHeads | Auto Trader Connect (Stock, Images, Deals, Messages, Calls, Leads APIs; Stock Notifications) | Sections 2.1–2.9, 4.1 |
| US | Cars.com, CarGurus, Autotrader.com (Cox), Facebook Marketplace; Google Vehicle Ads | No public portal specification found; feeds flow through IMS providers; leads usually by ADF e-mail | Sections 2.1, 3.1 |

- Auto Trader's FY26 results name its competitive set for the share-of-minutes metric: "Autotrader, CarGurus, Gumtree.com - Motors, eBay Motors UK, Motors, Carwow and Pistonheads" [VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21].
- The Bundeskartellamt's mobile.de/Carwow clearance found that consumers and dealers "often use several platforms in parallel" and that "many platforms also offer dealers a data export to other platforms" (translated from German) [VERIFIED: https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html, published 2026-10-08]. Dealer multi-homing is therefore a regulator-recorded fact in Germany, not only an industry assumption.
- CarGurus lists the sources of its data as "inventory management systems, automotive website providers, customer relationship management systems, dealer management systems, governmental entities, and third-party data brokers or licensors". It warns that competitors may make dealers dependent on them "such as hosting dealers' websites and providing inventory feeds for dealers" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm, filed 2026-02-19].

**Across markets.** In DE, NL/BE and the UK, the main portals publish **REST write APIs** for dealer-software vendors. In the US the main portals publish no write API in public. Inventory reaches them through inventory-management or website providers sending feeds, mostly files over FTP [WIDELY REPORTED: https://www.dataonesoftware.com/download/pdf/white-paper-classified-listing-sites-101-091509.pdf, 2009 — not fetched; ⚠ an old vendor white paper, which the search summary described]. [ASSUMPTION/JUDGEMENT] US syndication is therefore mostly *file-feed* engineering and European syndication mostly *API-client* engineering. A platform serving both needs both adapter styles.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Model each portal as a **channel** with its own adapter, credentials, capability flags (supports PATCH, supports delete, pushes status back, delivers leads) and validation profile. Don't model "syndication" as one export job.

### 1.2 Consolidation: portals that syndicate to each other

Portal consolidation is changing the channel map underneath dealer software.

- **AutoTrack and Gaspedaal.nl to AutoScout24 (NL).** Emerce reported on 28 November 2025 that the two sites "have come into the hands of the international group AutoScout24". Both keep their brands. Dealers on AutoTrack will use AutoScout24's technology platform, and AutoScout24.nl will gain Gaspedaal's reach. The two sites had been combined in 2019 in a joint venture of De Persgroep and Telegraaf Media Groep (translated from Dutch) [VERIFIED: https://www.emerce.nl/nieuws/autotrack-gaspedaalnl-onderdeel-autoscout24, published 2025-11-28]. PitchBook gives the completion date as 25 November 2025 [WIDELY REPORTED: https://pitchbook.com/profiles/company/62462-98, 2025 — search snippet, not fetched]. ⚠
- **AutoScout24's API already exposes this.** Its `ChannelId` values include `AutoTrack` ("published on AutoTrack in the Netherlands and displayed on both platforms"), `AutoTrackShared` ("an existing shared listing displayed on both platforms") and `AutoTrackOnly` [VERIFIED: https://listing-creation.api.autoscout24.com/assets/docs/data-models.md, n.d.; changelog to 2026-10-19].
- **AutoScout24 can export to mobile.de**, its main German competitor. `mobile_de` was added as a publication channel on 2022-11-28. "Publishing to the channel `mobile_de` marks listings as eligible for export to mobile.de if the customer has opted-in to selective mobile.de export handling. If a customer has not opted-in (which is the default) but has an export to mobile.de configured, then all listings will be exported." The channel "is not available for all customers yet" [VERIFIED: AutoScout24 data-models.md and changelog.md, https://listing-creation.api.autoscout24.com/docs].
- **AutoScout24 also feeds its B2B auction arm.** The `autoproff` channel exports a vehicle "without publishing it (can be used for Auctions)". A May 2026 endpoint, `GET /customers/{customerId}/listings/export-status`, reports per-listing results for Autoproff as `SUCCESS`, `FAILURE` (with errors such as "Image quality does not meet marketplace requirements") or `NOT_EXPORTED` [VERIFIED: AutoScout24 changelog 2026-05-15].
- **Marktplaats and 2dehands share one API.** "The API is identical for Marktplaats and 2dehands/2ememain", but an ad can only be placed on the platform whose URL is used [VERIFIED: https://api.marktplaats.nl/docs/v1/overview.html, n.d. (© 2023)]. In the lead documentation, "Any listings on 2dehands are also available on 2ememain and vice versa" [VERIFIED: https://api.marktplaats.nl/docs/v2/lms/index.html, n.d.].
- **Aggregators.** Gaspedaal describes itself as comparing cars from more than 40 car sites and about 10,000 dealers [WIDELY REPORTED: Apple App Store listing, search snippet, not fetched]. A dealer-stock tool, CarCollect, lists one-click publishing to AutoScout24, AutoTrack, Marktplaats, Gaspedaal and six smaller Dutch sites [VERIFIED: https://www.carcollect.com/integrations/tag/b2c-advertising, n.d.].

**Across markets.** NL is the clearest case of portal consolidation in 2025–26. In DE, mobile.de and AutoScout24 remain separate, but AutoScout24 offers an export to mobile.de. In the UK, Auto Trader's Stock API has an `exportAdvert` destination that "Controls the stock being exported from Autotrader to other 3rd parties" [VERIFIED: https://developers.autotrader.co.uk/documentation, n.d.]. In the US, Cox owns both Autotrader.com and the inventory tool vAuto (sibling brief, A.5).

**Architecture implications** [ASSUMPTION/JUDGEMENT]:

1. **A portal can also be a syndicator.** When a dealer platform publishes to AutoScout24 with `mobile_de`, *and* to mobile.de directly, the same car can appear twice on mobile.de. The channel model needs a "reached via" relation, so the dealer sees one decision per destination. Otherwise duplicates arise that the dealer platform did not create.
2. **Channel IDs are volatile.** `autoproff_marketplace_internal` was removed on 2025-12-17, and requests carrying it now fail with HTTP 400 [VERIFIED: AutoScout24 changelog]. Store channel configuration as data and validate it against the portal's current reference list.

---

## PART 2: Publishing contracts

### 2.1 API versus feed: the contracts compared

| Channel | Style | Write model | Identity keys | Back-channel | Evidence date |
| --- | --- | --- | --- | --- | --- |
| mobile.de Seller API | REST, JSON or XML, Basic auth; access for Transfer Service Providers (TSPs) and self-uploading dealers | POST create; PUT replaces the "complete ad with all fields"; DELETE | `mobileAdId`; seller's `internalNumber` (≤40 chars, unique per seller) | Ad Stream WebSocket; Lead API | n.d. (2026) |
| AutoScout24 Listing Creation API | REST, JSON, Basic auth "acting on behalf of a given dealer" | POST create (not idempotent); PUT; PATCH (with exceptions); DELETE | UUID; `offerReferenceId` (visible "Offer number"); `crossReferenceId` (hidden technical id) | Statistics; export-status | changelog 2026-10-19 |
| Auto Trader Connect Stock API | REST, bearer token from key/secret | POST, PATCH `/stock/{stockId}`; lifecycle states; per-destination publish flags | `stockId`, `searchId`; `externalStockId` (200 chars), `externalStockReference` (25 chars) | Stock Notifications webhooks; Deals/Leads/Messages/Calls | n.d. (release notes 2024–26) |
| Marktplaats / 2dehands API v1 | REST, OAuth 2.0 (user and client flows), PATCH supported | Ads by category; "Car Dealer API partner" fields for cars | `itemId`; `licensePlate` (6 or 8 chars) | Lead Delivery Webhook; chat API and webhook | 2019 (v1); © 2023 |
| Google Vehicle Ads (Merchant Center) | File, Google Sheet or API; "Website crawl feeds and manually added vehicles are not supported" | Product data per offer | `id`, `VIN` (17 chars; optional in FR, DE, IT, JP, ES, NL, UK) | Merchant Center diagnostics | n.d. |
| Google Vehicle Listings (organic, partner feed) | CSV/TSV over SFTP; **discontinued** | Full snapshot only | VIN, `store_code` | None | 2024-11-20 / 2025-03-05 |
| Meta automotive inventory catalog | CSV, TSV or XML hosted at a URL for scheduled fetches | Catalog items with `status` active or archived | `vehicle_id` | Ads Manager | n.d. |

Sources: [VERIFIED: https://services.mobile.de/manual/seller-api.html, n.d.]; [VERIFIED: https://listing-creation.api.autoscout24.com/assets/docs/design.md, workflow.md and migrating_from_other_as24_systems.md, n.d.]; [VERIFIED: https://developers.autotrader.co.uk/documentation, n.d.]; [VERIFIED: https://api.marktplaats.nl/docs/v1/advertisement.html, n.d.]; [VERIFIED: https://support.google.com/merchants/answer/11192663, n.d.]; [VERIFIED: https://developers.google.com/vehicle-listings/integration-process/feed-setup, last updated 2024-11-20]; [VERIFIED: https://developers.facebook.com/documentation/ads-commerce/marketing-api/auto-ads/reference, n.d.].

Additional facts:

- **AutoScout24 is moving partners off FTP.** Its migration guide targets dealers "using the FTP file upload". It tells them to match existing listings by `offerReferenceId`. If that is missing, it says a combination of `customerId + makeId + modelId + bodyId + bodyColor + firstRegistration` and further attributes "can be used with a high level of confidence to identify a listing". The purpose is "preventing duplicates when starting to send listings that already exists as if they were new" [VERIFIED: AutoScout24 migrating_from_other_as24_systems.md].
- **Google's organic vehicle listings feed was switched off.** The Vehicle Listings partner documentation carries the notice: "Processing of vehicle listing feeds will also be stopped" and "The Organic Search Auto Listings feature will no longer appear in the coming days" [VERIFIED: https://developers.google.com/vehicle-listings/reference/feed-specification, last updated 2025-03-05]. Paid **vehicle ads** continue. They are fully released in Australia, Canada, Japan and the US; in **open beta in the UK, Germany, France, Italy, Spain and the Netherlands**, for which advertisers must be allowlisted; and "Vehicle ads from private sellers, individuals, or auto brokers aren't permitted" [VERIFIED: https://support.google.com/merchants/answer/11189169, n.d.]. ⚠ Belgium is not on the list.
- **Marktplaats car-dealer status is an account configuration.** "Specifically for cars, we have some fields that are editable only by API partners that are configured on our side as 'Car Dealer API partner'" [VERIFIED: https://api.marktplaats.nl/docs/v1/advertisement.html].

**Across markets.** DE and NL/BE portals offer per-ad REST writes with partner onboarding: mobile.de requires TSPs serving more than ten customers to supply contacts, VAT ID and customer numbers. The UK's Auto Trader uses a capability model; its Integrations API (beta) shows which "API, Datafeeds, or Exports" an integration has [VERIFIED: Auto Trader documentation]. The US relies on files. Google and Meta are file or catalog channels in every market.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Hold a **desired-state record per (vehicle, channel)** and let each adapter converge the portal to it. An API adapter diffs and issues per-listing calls. A file adapter renders a full snapshot. A change-feed or webhook consumer reads the portal's actual state back. The record keeps the portal's ID, the platform's idempotency key, the last acknowledged version and the last error.

### 2.2 Create idempotency and duplicate prevention

- **mobile.de** offers an explicit idempotency header. "When the POST operation fails e.g. due to network connectivity problems or internal server error, the user does not know whether the ad has been created or not. If the user retries the POST operation it is possible that duplicated ad is created." The client sends `X-Mobile-Insertion-Request-Id` (≤100 characters, "unique per each ad creation"; UUIDs recommended). A retry with the same ID returns **303** with a `Location` header pointing to the existing ad [VERIFIED: https://services.mobile.de/manual/seller-api.html, n.d.].
- **mobile.de** also rejects a reused seller key with the error `duplicate-seller-inventory-key`: "The internalNumber (AKA seller inventory key) must be unique for given seller" [VERIFIED: same].
- **AutoScout24** marks POST as not idempotent, except that "some POST operations are made idempotent by offering specific implementation strategies" [VERIFIED: https://listing-creation.api.autoscout24.com/assets/docs/design.md]. Its error guide warns: "If you encounter a 500 when fetching listings, do not assume that the listing does not exist. Assuming those listings do not exist and creating them can lead to duplicates" [VERIFIED: https://listing-creation.api.autoscout24.com/assets/docs/error_handling.md]. A `listing-creation-limit-exceeded` error caps how many listings a customer may create "within a certain time period" [VERIFIED: same].
- **Auto Trader** stores the partner's own key in `externalStockId` ("Field to store a third party system unique stock id, (200 chars)") [VERIFIED: https://developers.autotrader.co.uk/documentation].

**Architecture implications** [ASSUMPTION/JUDGEMENT]:

1. **Generate the idempotency key once per (vehicle, channel, creation attempt)** and persist it *before* the call. Reuse it on every retry.
2. **Treat "unknown" as distinct from "absent".** After a timeout or a 5xx, reconcile by listing the dealer's ads and matching on the platform's own key (`internalNumber`, `offerReferenceId`, `externalStockId`) before re-creating.
3. **Always write the platform's stock key into the portal's external-ID field.** That field is the only stable join between the two systems, and it is what makes migration and reconciliation possible.

### 2.3 Update semantics: full replace, patch and list fields

- **mobile.de PUT** requires "the complete ad with all fields" [VERIFIED: mobile.de Seller API].
- **AutoScout24 PATCH** is supported, but with a documented trap. Several fields are "not supported by the PATCH API", and for most of them "existing value gets removed, patched value is ignored". This applies to `financingOffer`, `leasingOffers`, `highlights`, `schwackeCode`, `drivingMode` and others. For `marketing`, the "existing value remains" [VERIFIED: https://listing-creation.api.autoscout24.com/assets/docs/workflow.md]. A PATCH can therefore **silently delete** a financing or leasing offer.
- **Auto Trader** list fields are replace-only: "When updating the list of features (or any list type field) the complete list should be sent in the request, you cannot add or remove individual items from the list in isolation" [VERIFIED: Auto Trader documentation].
- **Image order is a list too.** AutoScout24: "To reorder the images of a listing - update the listing so that its `images` attribute has the list of images in the new desired order" [VERIFIED: AutoScout24 workflow.md].
- **Concurrency.** mobile.de: "Do not send multiple requests for the same ad at the same time" (sibling brief; re-verified). Auto Trader's stock record carries a `versionNumber` [VERIFIED: Auto Trader documentation].
- **Partial failure is total failure at AutoScout24.** "Upon a partial failure, the API cancel the whole operation", for example when associating several images and one no longer exists [VERIFIED: AutoScout24 design.md].

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Adapters should send **full desired state** wherever the portal's partial-update semantics are lossy, and keep PATCH as a per-channel optimisation guarded by a field allow-list. Serialize writes per (listing, channel) through a keyed queue. Concurrent price and image updates for one car are the usual source of lost writes.

### 2.4 Delete, withdraw and lifecycle

Portals model "the car is gone" very differently:

| Channel | Withdraw semantics (as documented) |
| --- | --- |
| Auto Trader | Lifecycle states `DUE_IN`, `FORECOURT`, `SALE_IN_PROGRESS`, `SOLD`, `WASTEBIN`, `DELETED`. Only the first three can be published. "Before these lifecycle states can be set all advert destinations should be first updated to NOT_PUBLISHED". `WASTEBIN` "is also used by Datafeeds when a record is removed". Automatic transitions: unadvertised `DUE_IN` → `WASTEBIN` after 28 days unedited; `FORECOURT` → `WASTEBIN` after 56 days; `SALE_IN_PROGRESS` → `SOLD` after 28 days; `SOLD` → `DELETED` after 60 days; `WASTEBIN` deleted after 28 days |
| Auto Trader (deals) | "partners will be prohibited from updating the lifecycleState once the reservationDealId is present"; "Updating to DELETED is only permitted once the vehicle is no longer advertised and no deals are linked to a vehicle". A completed deal moves the car to `SOLD`; a cancelled one moves it back to `FORECOURT` |
| mobile.de | DELETE removes the ad, and "All associated images will be purged as well". The general section says a successful DELETE returns 204; the ad-deletion section says 200 (an inconsistency in the docs) |
| AutoScout24 | DELETE (idempotent in effect; a second delete of an image yields 404). Images of a deleted listing are deleted; images left unassociated after an update are deleted "immediately"; uploaded but never-associated images are deleted after one day |
| Google Vehicle Listings (discontinued) | Full snapshot: "Vehicles and dealerships that aren't present in a feed are removed from Google within a few hours"; vehicles stop showing three days after the last feed; a feed that would "reduce the total inventory by more than 30%" is blocked |
| Meta catalog | `status` "Controls whether an item is active or archived"; `availability` `available`/`not_available` ("unavailable vehicles aren't shown in the ad") |
| Marktplaats | `closeDate`: "The date the advertisement will be closed" |

Sources: [VERIFIED: Auto Trader documentation]; [VERIFIED: mobile.de Seller API]; [VERIFIED: AutoScout24 workflow.md]; [VERIFIED: Google feed-setup, 2024-11-20]; [VERIFIED: Meta auto-ads reference]; [VERIFIED: Marktplaats advertisement.html].

- **Renewal versus re-creation.** mobile.de's FAQ answers "How to prevent new ad placements?" by noting that "New ad placements can be obtained by deleting and replacing the same ad" or by using `renewalDate`. Renewed ads "will be displayed as New for three days", and renewal "comes with costs if the amount of free feature contingents has been already exceeded" [VERIFIED: mobile.de Seller API]. [ASSUMPTION/JUDGEMENT] Delete-and-recreate is a known way to fake freshness. It destroys the portal's price history and days-on-market for the car, so a syndication engine should never use it as a routine update path.

**Across markets.** UK: Auto Trader's state machine is rich, and transactions (deals, reservations) block withdrawal. DE and NL/BE: plain delete. Ad platforms (Google, Meta): absence from the feed or an availability flag. The 30% guard on Google's discontinued feed is the clearest published "truncated feed" protection.

**Architecture implications** [ASSUMPTION/JUDGEMENT]:

1. **Delete propagation is a saga, not a call.** For each channel: unpublish, wait for the acknowledgement, then delete or archive. Handle channel-specific blockers, such as an Auto Trader deal holding a reservation. Alert when a sold car is still live on any channel after N minutes.
2. **Guard against mass withdrawal.** Copy Google's 30% rule: a DMS feed that would withdraw more than a threshold share of a rooftop's stock pauses for human confirmation.
3. **Expect portal-side auto-transitions** (Auto Trader's 28/56/60-day rules). Reconciliation must accept that the portal changes state without the platform's command.

### 2.5 Rate limits, retries and webhook delivery

- **AutoScout24** returns 429 and advises: "try to avoid sending requests in big batches"; if batches cannot be avoided, "configure 5 to 10 minutes timeframe to ramp up your batch jobs from 0 to maximum capacity". For 5xx and timeouts: "retry your request at least 3 times", starting "after 100 ms, 200 ms and 400 ms", with exponential backoff and jitter. The internal error rate is "normally far below 1%". Client timeouts "should not be too short" because uploads are large [VERIFIED: https://listing-creation.api.autoscout24.com/assets/docs/error_handling.md].
- **Auto Trader** warns that its test environments are "not designed to be used in production - you might experience poor performance or rate limiting". Inbound connections are subject to "dynamic reputation scoring", and an unexpected volume of 403s is a symptom [VERIFIED: Auto Trader documentation]. Stock list requests return up to 200 results per page (20 is the default and recommended) [VERIFIED: same].
- **Auto Trader webhooks (outbound to partners).** "Any non 2** series response code from the endpoint is considered a retryable error". Retries come 10 seconds after the first failure, then 30 seconds, then 30 minutes. "Delivery is tracked on a per message basis, if two messages for the same key are scheduled to be sent, first one fails and the second succeeds, the first message will still be retried regardless. For use cases only interested in the latest state, implementations should store and use the time field in the message to decide if it's relevant or has been superseded." Payloads are signed in an `AutoTrader-Signature: t=…,v1=…` header (HMAC-SHA256 over `time.body`). Partners may return 429 to apply their own rate limit [VERIFIED: Auto Trader documentation].
- **Marktplaats webhooks.** The receiver must answer within **2 seconds**. A 5xx or timeout "may" be retried. A 4xx means "You cannot accept the message no matter what. We cannot retry, and will log this as a bug with your system", and receivers must "NOT use 4xx errors if you receive a request you simply don't care about". Requests are signed with RSA HTTP signatures (cavage draft) over `(request-target) (created) digest` [VERIFIED: https://api.marktplaats.nl/docs/v2/lms/index.html, n.d.].
- **mobile.de Ad Stream.** One WebSocket connection per user; `catchup=true` replays events from the last disconnect, retained for **24 hours**. Mixing catchup and non-catchup connections "causes unpredictable behavior" [VERIFIED: https://services.mobile.de/manual/ad-stream.html, n.d.]. No ordering guarantee is documented.
- **Standard Webhooks** (a community specification with a steering committee from Zapier, Twilio, Svix, Kong and others) recommends `webhook-id`, `webhook-timestamp` and `webhook-signature` headers. It says to "Use the `webhook-id` header as an idempotency key" and to retry "following a retry schedule spanning multiple days, with an exponential backoff" [VERIFIED: https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md, n.d.; https://www.standardwebhooks.com/, n.d.].

**Across markets.** No two portals share a signature scheme: HMAC with timestamp at Auto Trader, RSA HTTP signatures at Marktplaats, no push at all at mobile.de (WebSocket and polling instead). Auto Trader's retry window is short (about 31 minutes in total), against the multi-day schedule Standard Webhooks recommends.

**Architecture implications** [ASSUMPTION/JUDGEMENT]:

1. **Each channel gets its own token bucket and ramp-up**, which absorbs AutoScout24's slow-start advice and the 429s.
2. **Inbound webhook endpoints acknowledge fast** (Marktplaats's 2-second budget) and process asynchronously from a durable inbox, deduplicating on the event ID.
3. **Short retry windows mean the platform cannot rely on push alone.** Pair every webhook subscription with a periodic pull (`GET /stock?…`, `listListings`, the Lead API cursor) to repair missed events. Auto Trader's 31-minute window is the extreme case.
4. **For Auto Trader-style per-message retries, order by the event's own `time`, not by arrival.**

### 2.6 Shared ownership: when the dealer or the portal edits the listing

A syndicated listing has several writers. The portals document this openly:

- **AutoScout24 FAQ, "Do other systems update listings?"**: "Yes". It lists manual edits by the dealer, edits by customer care, the fraud system activating or deactivating listings, and phishing: "If a dealer gets phished, all their listings get deleted. If the dealer gets reactivated and requests to restore their listings, suddenly all listings reappear" [VERIFIED: https://listing-creation.api.autoscout24.com/assets/docs/faq.md, n.d.].
- **AutoScout24 `overwriteProtection`**: "When overwriteProtection is true, it's not possible to edit or delete the listing using the API. Changes or deletions are only possible on the listing using the dealers My Area on the website." Since 2026-09-03, `GET /customers/{customerId}/listings?include=overwriteProtection` exposes the flag in bulk. A separate `sealsOverwriteProtection` stops data providers from overwriting quality seals [VERIFIED: AutoScout24 data-models.md and changelog].
- **mobile.de `uploadSticky`**: "Indicates that an ad can only be changed within dealer area. Modifications via Seller-API will be rejected", returned as the error `ad-only-modifiable-in-dealer-area` [VERIFIED: mobile.de Seller API].
- **Auto Trader provenance fields.** Stock notifications carry `stockEventSource` (e.g. `AT_CONNECT`) and an `integrationId` for changes made through Connect. They also carry a `changedFields` object. Images carry a `source`: "Portal, AT Connect, Datafeeds or Other" [VERIFIED: Auto Trader documentation].

**Architecture implications** [ASSUMPTION/JUDGEMENT]:

1. **Field-level ownership.** Decide per field which system wins: price from the DMS or pricing tool, description from the dealer platform, seals from the portal. Record the decision in the channel profile.
2. **Read lock flags before every write**, and surface "locked on portal" to the dealer as a state, not as an error storm.
3. **Status reconciliation must handle appearance as well as disappearance.** The AutoScout24 phishing-restore case shows that listings can come back on their own.

### 2.7 Images and media

| Channel | Documented limits and rules |
| --- | --- |
| mobile.de | Per-seller `maxImages` (examples: 15 and 30); upload first, then reference by URL; images feed the price rating, so "the recommendation is to upload images upfront" (listings "are not directly visible to end customers after creation"); external Auto Panorama: 12–60 frames, 1–4 MB optimal, 3:2 or 2:1 |
| AutoScout24 | PNG or JPEG, max 20 MB, 50–10,000 px; images are independent resources associated by ID; each image can belong to only one listing; `duplicated-image` error if one appears twice; an MD5 of the original is returned so clients can skip re-uploads; 360° collections up to 75 images |
| Auto Trader | Images API stores files on Auto Trader's CDN; URLs carry a `{resize}` placeholder (e.g. `w260h195`); `classificationTags` label each image (e.g. "Rear Left", "Exterior"); Co-Driver recommends an order and flags missing angles |
| Google Vehicle Ads | One `image_link` plus up to 10 `additional_image_link`; minimum 500×500 px (1500×1500 suggested); 4:3 recommended; main image a front-to-side view at about 45°; no watermarks, overlays, logos or "Coming Soon" placeholders; stock photos only for new cars matching make, model and colour; max 16 MB |
| Meta catalog | At least one image, max 20, up to 4 MB each; Marketplace needs at least 2 images and vehicles "over 500 miles/kms" |

Sources: [VERIFIED: mobile.de Seller API]; [VERIFIED: AutoScout24 workflow.md and error_handling.md]; [VERIFIED: Auto Trader documentation]; [VERIFIED: https://support.google.com/merchants/answer/11192663 and https://support.google.com/merchants/answer/11190670, n.d.]; [VERIFIED: Meta auto-ads reference].

**Across markets.** The common dealer habit of overlaying the dealer logo or a price banner on photos is **disallowed on Google** and unrestricted in the portal APIs read here. A US Marketplace listing needs at least two images; the sibling brief records that Auto Trader's Co-Driver re-orders images by AI.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Store **one master image set** (original resolution, with a content hash, angle tag and overlay-free flag). Derive per-channel renditions (crop, overlay, count cap, order) at publish time. Use the content hash, as AutoScout24's MD5 does, to avoid re-uploading unchanged images. Image uploads dominate syndication bandwidth and rate-limit budgets.

### 2.8 Taxonomy and equipment-code mapping

- **mobile.de**: enumerated fields (`gearbox: AUTOMATIC_GEAR`, `climatisation: AUTOMATIC_CLIMATISATION`, `airbag: FRONT_AND_SIDE_AND_MORE_AIRBAGS`) whose valid values come from reference-data endpoints such as `/refdata/gearboxes`. Each seller is "at home" on one site (mobile.de or automobile.fr), and "the specific reference data and validation rules of that site apply" [VERIFIED: mobile.de Seller API]. KBA `hsn`/`tsn` and a Schwacke code (sibling brief, A.3).
- **AutoScout24**: `equipment` is an array of **integer IDs** from the References API, with mutual-exclusion rules. Example: "You are only allowed to send one Automatic Climate Control equipment for a given listing", choosing between 2-, 3- and 4-zone variants (241, 242, 243) or the generic (30). Sliding door: either generic (152) or left/right (244/245), not both [VERIFIED: AutoScout24 data-models.md]. `natCode` ("Classification of makes and models given by Eurotax/Schwacke") replaced `schwackeCode` from 2024-06-13. Make, model and reference values have been marketplace-specific since 2025-02-19 (Canada differs now; European differences possible later). On **2026-10-19** localized names changed, with the warning: "Data providers using reference names to map IDs should review and update their mappings" [VERIFIED: AutoScout24 changelog].
- **Auto Trader**: features carry `factoryCodes` (from 14 July 2025) "which the manufacturer provides to assist with identifying the specific standard specification or optional equipment", plus `genericName`, `category`, `rarityRating` and `valueRating`. Up to three `advertiserVehicleHighlights` and a `priceCommentary` were added for sellers [VERIFIED: Auto Trader documentation].
- **Marktplaats**: car ads with a valid licence plate "will be enriched with data from a third party partner after posting. This process is asynchronous". Dealer-supplied values take precedence. `categoryId` decides the brand category, and the model attribute "decides the model search filter"; `makeDescription`/`modelDescription` are display-only [VERIFIED: Marktplaats advertisement.html].
- **Google**: `model` "without trim"; `vehicle_option` repeatable; `body_style` and `engine` enumerations [VERIFIED: Google attributes page].

**Across markets.** DE uses KBA codes plus Schwacke/natCode; NL lets the portal enrich from the plate; the UK keys on Auto Trader's derivative taxonomy plus OEM factory codes; the US relies on VIN decoding (sibling brief, A.7.1).

**Architecture implications** [ASSUMPTION/JUDGEMENT]:

1. **Map once to a canonical equipment model** (OEM option code → normalized feature → per-portal code), keyed by IDs and never by display names. AutoScout24's 2026-10-19 rename is the warning.
2. **Validate per-portal mutual-exclusion rules** before sending, and version the mapping tables.
3. **Don't overwrite portal-enriched fields** (Marktplaats plate enrichment) unless the dealer's value is better sourced.

### 2.9 Listing quality and regulatory validation

- **mobile.de quality check**: endpoints return quality scores that evaluate "images, description, and attribute completeness", plus a dealer-feedback endpoint for image quality. Access is "available exclusively to partners participating in the mobile.de Data Partner Program" [VERIFIED: mobile.de Seller API].
- **AutoScout24 Germany WLTP** (2026-09-16): WLTP requirements apply to German dealer car listings when "mileage ≤ 1,000 km (or is not set) OR firstRegistrationDate is less than 8 months old (or is not set)". Plug-in hybrids in Germany need four consumption and fuel fields "as required by German law (Anlage 1 … PKW-EnVKV)" [VERIFIED: AutoScout24 changelog and faq.md]. This mirrors the Pkw-EnVKV "new car" presumption in the sibling brief (A.7.8).
- **AutoScout24 Belgium Car-Pass** (from 2026-06-01): `belgianCarpassMileageUrl` "is mandatory for used car listings … from Belgian dealers". A request without it gets HTTP 400 `missing-belgian-carpass-mileage-url`, enforcing "Belgian Carpass law (Loi Car-Pass / Car-Pass wet)" [VERIFIED: AutoScout24 changelog 2026-05-14]. Car-Pass vzw operates under the law of 11 June 2004. In 2025 it issued 855,169 Car-Pass documents, recorded 1,466 fraud cases and received 345.5 million mileage readings [VERIFIED: https://www.car-pass.be/nl, n.d.; translated from Dutch].
- **Auto Trader**: rejects a price below the minimum ("Rejected due to price of null not meeting minimum price of 75"), DVLA category A/B vehicles, and, per a release note (date not captured), Car/Van/Bike/Cycle adverts with a POA price indicator [VERIFIED: Auto Trader documentation].
- **Google**: the landing page must show the dealership name and location, price, VIN, mileage for used cars, and so on; "In the EEA+UK, it [`id`] must also appear on the landing page"; a dealer-supplied `title` "is not used" [VERIFIED: Google attributes page and https://support.google.com/merchants/answer/11189169].
- **Meta**: VIN "must be exactly 17 characters and it isn't required for pre-1983 vehicles"; `dealer_privacy_policy_url` is "Required for Lead Form contact method" [VERIFIED: Meta auto-ads reference].

**Across markets.** BE: Car-Pass URL (hard rule since June 2026). DE: Pkw-EnVKV/WLTP for near-new cars. UK: write-off categories, POA ban, minimum price. US: no portal-side regulatory validation found; FTC and state dealer-advertising rules apply (not researched here).

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Put a **pre-publish validation layer** in the dealer platform that runs each channel's rules (regulatory and portal policy) and tells the dealer *before* sending why a car will not go live on a channel. Regulatory rules arrive via portal changelogs with a few weeks' notice (Car-Pass: announced 2026-05-14, enforced 2026-06-01), so someone must own changelog monitoring.

### 2.10 Duplicates across and within channels

- **Google**: "If a VIN is submitted for more than one vehicle offer, those offers will be disapproved". Multi-store cases use repeated `store_code` instead; multi-language offers are the exception [VERIFIED: Google attributes page].
- **Meta**: "If there are multiple instances of the same ID, we ignore all instances" [VERIFIED: Meta auto-ads reference].
- **Marktplaats lead IDs** are unique per (lead kind, advertisement, buyer) (see 3.3). Its multi-rooftop dealers are told apart by `seller.vestiging` and `location.postcode` [VERIFIED: https://api.marktplaats.nl/docs/v2/lms/lead-delivery-webhook-v3.yaml, v3.2.0].
- **Portal-to-portal exports** (AutoScout24 → mobile.de; AutoScout24 ↔ AutoTrack; Auto Trader `exportAdvert`) create duplicates the dealer platform did not send (section 1.2).

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Deduplicate on **vehicle identity** (VIN, or plate in the UK and NL) across the dealer group *before* syndication. Two rooftops in one group listing the same car is the common case after an inter-branch transfer. The platform should publish one listing with repeated location codes where the channel supports it (Google), and pick a single owning rooftop otherwise.

---

## PART 3: Lead handling

### 3.1 ADF/XML: the US lead lingua franca (read in full)

- **History.** ADF 1.0 was drafted from December 1998 with comments from Reynolds and Reynolds, Autovantage, Cobalt, Microsoft, Cars.com, AutoSite and Kelley Blue Book. The final document is dated **3 May 2000** [VERIFIED: https://adfxml.info/adf_spec.pdf, 2000-05-03]. adfxml.info, which hosts the spec, says it was "built … by Dealer Inspire" (a Cars.com company) [VERIFIED: https://adfxml.info/, n.d.].
- **Why it exists.** In 2000, lead transmission was "generally in the form of email, Fax or through a proprietary lead management system". Dealers "need to provide nearly immediate customer response". The format was designed to be "easy to append to existing email leads making them both human and electronically readable" [VERIFIED: same].
- **Structure.** Root `<adf>` → `<prospect>` with `<requestdate>` (ISO 8601), then `<vehicle>`, `<customer>`, `<vendor>` and an optional `<provider>`. `<prospect status="new|resend">` marks resent leads [VERIFIED: same].
- **Minimum valid lead.** "Date and time; Vehicle: year, make, model; Customer: name, and either phone number or email address; Vendor: name" [VERIFIED: same].
- **Identity across hops.** `<id sequence="1" source="…">` can repeat. "Different sources may use different ids for the same data as it is passed around. The sequence is a number used to track the history of this piece of data"; "Source attribute is required" [VERIFIED: same].
- **Transport.** The "standard transfer mechanism" is e-mail: (1) a multipart MIME message with an `application/xml` part holding the lead, or (2) a plain e-mail whose entire body is the lead, which "does not support UTF-8". "If an error occurs accepting the lead, the lead email should be bounced back to the source email address" [VERIFIED: same].
- **Interpretation drift.** Kelley Blue Book's LeadDriver guide: "the original ADF 1.0 specification contradicts itself in certain places and the DTD does not validate. Also, over the years, variations and customizations to the specification have been used". LeadDriver fills missing required contact fields with "not provided", and puts engine and drivetrain into `<option>` tags because ADF has no such tags [VERIFIED: https://ldti.syndication.kbb.com/reference/files/ADF_Usage_Guide.pdf, published 2014-05]. ⚠ The guide is 12 years old, but it shows how implementations diverge.
- **How a CRM receives ADF today.** One small CRM's documentation describes a per-dealership read-only leads e-mail address. ADF "is the standard format that providers such as CarGurus, AutoTrader, and Cars.com use". The e-mail "must be plain text with only the XML, and the XML must be valid". Invalid or non-ADF e-mails still create a lead, with the sender as the name and the source "Regular Email Lead" [WIDELY REPORTED: https://dealr.cloud/docs/docs/leads/receiving-leads/, n.d. — vendor documentation].

**Across markets.** ADF is US-born and US-dominant. None of the European portal lead contracts read here use it: mobile.de uses JSON events over REST, Marktplaats a JSON webhook, Auto Trader JSON APIs. [ASSUMPTION/JUDGEMENT] European OEM lead programmes and some UK CRMs may accept ADF; not verified.

**Architecture implications** [ASSUMPTION/JUDGEMENT]:

1. Build a **tolerant ADF parser** (namespace-free, DTD-free, "not provided" handling, `resend` handling), behind an inbound-mail gateway with per-rooftop addresses.
2. Keep the **raw message** for audit.
3. Emit ADF *outbound* for US CRMs that only accept e-mail, and do it through a queue: e-mail has no delivery acknowledgement beyond bounces.

### 3.2 STAR standards

- STAR (Standards for Technology in Automotive Retail) is a non-profit, dues-paying standards body of dealers, manufacturers and retail system providers. Its site lists STAR6 and STAR5 XML BOD releases, sales-related APIs, a Service Scheduling API and an Automotive Retail Domain Model announced in January 2026 [VERIFIED: https://www.starstandard.org/, n.d. (footer © 2023; featured post 2026-01-27)].
- **Sales Lead API (June 2025).** STAR released its first Sales Lead API to "standardize sales lead data". It "facilitates seamless communication between manufacturers, dealers, and related service providers". Users can "create new sales leads, retrieve details of any specific sales lead", "update information for existing sales leads, remove a sales lead from the system" and "curate a list of all sales leads, with optional query parameters such as status or creation date". It is "available for free to download" [VERIFIED: https://www.starstandard.org/index.php/2025/06/03/star-announces-new-sales-lead-standards-api-for-automotive/, published 2025-06-03]. The release does not mention ADF.
- Salesforce's Automotive Cloud developer guide has a page titled "Sales Lead BOD" with change, get, process and update operations [WIDELY REPORTED: https://developer.salesforce.com/docs/industries/automotive/guide/sales-lead-bod.html, search snippet; the page returned HTTP 403].

**Across markets.** STAR membership and adoption are US-centred. [ASSUMPTION/JUDGEMENT] No European equivalent lead standard was found; European portals each publish their own JSON contracts.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Use STAR's Sales Lead resource model as the **canonical internal lead schema** for OEM-facing integrations. It is free, CRUD-shaped and backed by US dealers and vendors. Map portal-specific payloads into it, rather than designing a proprietary schema from scratch.

### 3.3 How European portals deliver leads

**mobile.de Lead API (version 2026-06-25)** [VERIFIED: https://services.mobile.de/manual/lead-api.html, version 2026-06-25]:

- Access "can be granted to Transfer Service Providers and Lead Management System partners". It is REST with Basic auth; OpenAPI is published at `services.sandbox.mobile.de/lead-api/openapi.json`.
- A lead "represents 'qualified intent'". A lead has many **lead events** ordered by time: `MessagingLeadSubmitted`, `BuyerReplied`, `MessagingLeadResubmitted` (the buyer resubmits the form on a listing with an existing conversation, "but can contain contact information changes"), `LeasingLeadSubmitted`, `BuyerSearchBehaviourAdded`, `BuyerPreferencesUpdated` and `PhoneCallReceived` (missed or taken).
- **Pull with a cursor**: `GET /lead-api/sellers/:mobileSellerId/events?cursor=…` returns events after the cursor plus a `nextCursor`; `cursor=0` starts "from the oldest retrievable lead event".
- **Bidirectional status**: `POST …/leads/:leadId/status` with `newStatus` in `IN_PROGRESS`, `SOLD`, `NOT_INTERESTED`, `SPAM`, an optional `occurredAt` "in case of asynchronous communication", and a `traceId`. "More options might arrive in the near future."
- Payloads carry a pseudonymous `buyerIdentifier`, the source ("MOBILE") and the vehicle, including the dealer's `internalNumber`, which joins the lead back to stock.
- **Consent-gated enrichment**: `BuyerSearchBehaviourAdded` "is present if the user has given their consent to share their data and there are sufficient data points available".
- Product context (July 2026): the Lead Manager's AI writes "45 percent of all written replies"; a lead-performance report shows "response times, response rate and processing status"; a WhatsApp integration is tied to the listing; Lead Manager Pro offers "a central pipeline for leads from all channels"; "the new Lead API ensures that leads are transferred directly and securely into existing CRM systems". The mobee call assistant's pilot ("in the Netherlands with 19 dealers, March to May 2026") found 91% of answered calls fell outside opening hours and one in three became a qualified lead (translated from German) [VERIFIED: https://newsroom.mobile.de/plattform-update-sommer-2026/, published 2026-07-15]. ⚠ The Dutch pilot location is from the footnote; it suggests mobile.de is testing products in NL.

**Marktplaats / 2dehands Lead Delivery Webhook v3.2.0** [VERIFIED: https://api.marktplaats.nl/docs/v2/lms/index.html and lead-delivery-webhook-v3.yaml, n.d.]:

- Three services: the **Lead Delivery Webhook** (push; enriched leads), the **Bidirectional Communication API** (pull; read conversations and send replies; can switch off e-mail notifications to the seller) and the **Chat Message Webhook** (push; fast, unenriched).
- Lead kinds: `MessagingLead`, `BidCreatedLead`, `BidRemovedLead` and `CallTrackingLead` ("when the buyer called or tried to call the seller"; fields `callStart`, `answered`, `callDuration`, caller number "Not available for anonymous calls").
- Enrichments: `TradeIn` (plate, mileage, damage description), `CallbackRequest` and `FinancingInfoRequest`.
- **Rooftop routing data**: `seller.vestiging` is "Intended to distinguish different rooftops of the same dealer organisation", and the location postcode distinguishes "different locations used by the same user account". The docs suggest using "our seller data fields to route it immediately to a specific sales agent".
- **Lead identity**: "The lead id identifies the lead based on leadKind, advertisementId and buyer id. That means it is unique, unless one buyer creates multiple leads of the same leadKind for the same advertisement". Each call-tracking lead has a unique ID.
- **No ordering**: "All processing on our side is async, so we do not give guarantees on the specific order you will receive webhook messages in".
- **Forward compatibility**: "We can always add new properties to our payloads (even in patch version updates)". Receivers must tolerate unknown fields (the docs cite Jackson's default as a pitfall).
- Subscription used to be manual through Marktplaats/2dehands Zakelijk customer service per dealer; it can now be done through a configuration endpoint.

**Auto Trader** [VERIFIED: https://developers.autotrader.co.uk/documentation, n.d.]:

- Deals, Messages ("maximum character limit for a message is 1500 characters"), Part Exchange, Delivery and Calls APIs, plus Deal Notifications (`DEAL_CREATE`, `DEAL_UPDATE`).
- The Leads API returns at most 100 leads per request (from June 2024), and partners can no longer set a lead's status to `NEW_MESSAGE`.
- A 2025 change lets retailers "create Deals in their system which have originated outside of the Autotrader consumer journey".
- For volumes and Buying Signals, see the sibling brief (A.2).

**Across markets.** DE: pull API with cursor, plus status write-back. NL/BE: signed push webhooks, plus a pull chat API. UK: deal-centric APIs and webhooks, with leads as part of a transaction object. US: ADF e-mail is the baseline (3.1). Only mobile.de documents **outcome write-back** (`SOLD`, `NOT_INTERESTED`, `SPAM`) as a public contract. [ASSUMPTION/JUDGEMENT] That write-back gives the portal closed-loop data on which leads convert, which strengthens its ROI story and its models.

### 3.4 Lead types the platform must model

| Lead type | Where evidenced | Data the platform receives |
| --- | --- | --- |
| Form or e-mail message | ADF; mobile.de `MessagingLeadSubmitted`; Marktplaats `MessagingLead` | Contact details, message, vehicle reference |
| Conversation follow-up | mobile.de `BuyerReplied`; Marktplaats Chat Message Webhook | Message appended to an existing lead |
| Bid or offer | Marktplaats `BidCreatedLead`/`BidRemovedLead`; mobile.de "Direct Offer" resource | Amount, bid ID |
| Phone call (tracked) | Marktplaats `CallTrackingLead`; mobile.de `PhoneCallReceived`; Auto Trader Calls API | Start, duration, answered flag, caller number if not anonymous |
| Leasing or finance request | mobile.de `LeasingLeadSubmitted`; Marktplaats `FinancingInfoRequest`; Auto Trader Finance API (beta) | Product interest; possibly an application |
| Trade-in | ADF `<vehicle interest="trade-in">`; Marktplaats `TradeIn`; Auto Trader Part Exchange API | Second vehicle with mileage and condition |
| Reservation or deal | Auto Trader Deals and reservations | Transactional state that locks stock (2.4) |
| Callback request | Marktplaats `CallbackRequest` | Preferred contact |
| Clicks to the website or directions | CarGurus "connections" | Counted, not routed |

CarGurus defines "connections as interactions between consumers and dealers on our marketplace through phone calls, email, managed text and chat, and clicks to access the dealer's website or map directions to the dealership" [VERIFIED: CarGurus 10-K FY2025, filed 2026-02-19]. Sources for the other rows are given in 3.1–3.3.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Model a **Lead** (buyer × vehicle × dealer, with a lifecycle) separately from **Interactions** (each message, call, bid or enrichment). Portals already do this: mobile.de's lead events, Marktplaats's lead webhook versus chat webhook. A CRM that stores each e-mail as a new lead inflates lead counts and breaks attribution.

### 3.5 Lead response time: the evidence

- **HBR 2011 (cross-industry, US).** Oldroyd, McElheran and Elkington audited 2,241 US companies with a web-generated test lead. 37% responded within an hour; the average response time among those that answered within 30 days was **42 hours**; 23% never responded. A companion analysis of 1.25 million leads at 29 B2C and 13 B2B companies found that firms contacting a lead within an hour were "nearly seven times as likely to qualify the lead" as those waiting an hour longer, and "more than 60 times as likely" as those waiting 24 hours or more [WIDELY REPORTED: https://www.smartcompany.com.au/?p=20719, 2011-07-01; citation verified at https://scholarsarchive.byu.edu/facpub/9711, HBR vol. 89 no. 3, 2011; HBR page verified only for authors and date: https://hbr.org/2011/03/the-short-life-of-online-sales-leads]. ⚠ 15-year-old and not automotive-specific; "qualify" meant a conversation with a decision maker.
- **Pied Piper PSI Internet Lead Effectiveness 2025 (US automotive).** Mystery-shopper e-mails through the websites of 4,023 dealerships across 35 brands, with responses evaluated by e-mail, phone, text and chat over 24 hours. The industry average was a record 65/100. **19% of dealers failed to personally respond**; dealers phoned 66% of web customers; they answered the customer's question by e-mail or text 69% of the time; 49% used several channels. Pied Piper: dealers who move from below 40 to above 80 "on average sell 50% more units from the same quantity of internet leads" [WIDELY REPORTED: https://www.autoremarketing.com/ar/retail/dealerships-responsiveness-to-internet-leads-hits-record-high-again, published 2025-03-03].
- **mobile.de (DE)**: the 2026 lead-performance report measures response times; 91% of calls answered by the AI assistant in the pilot were outside opening hours [VERIFIED: mobile.de newsroom, 2026-07-15].
- **Auto Trader (UK)**: Deal Builder enquiries "convert at double the rate into sales" [VERIFIED: Auto Trader FY26 release]; full reservations are "the very best enquiries" (sibling brief).

**Across markets.** Response-time research is US-heavy. In Europe the portals themselves now measure dealer responsiveness (mobile.de's report). [ASSUMPTION/JUDGEMENT] Portals may later use responsiveness in ranking or pricing; no public evidence was found.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Response time is a **latency budget on the lead path**: portal → ingestion → routing → salesperson notification → first reply. Measure it end to end per rooftop, and keep the platform's share in seconds. After-hours coverage (auto-acknowledge, AI assistant, callback scheduling) matters because a large share of buyer contact happens outside opening hours.

### 3.6 CRM and lead-management systems

- **US**: VinSolutions is a Cox Automotive brand (sibling brief A.5). DealerSocket's CRM page offers "robust call management and lead management systems"; its privacy links point to solera.com domains [VERIFIED: https://dealersocket.com/solutions/crm-software/, n.d.]. [ASSUMPTION/JUDGEMENT] DealerSocket has been part of Solera since about 2020; verify. CDK's CRM page promotes an AI Virtual Assistant that will "Automatically engage every lead with AI-powered conversations, intelligent routing, and timely follow-up" and lists the FAQ "Is Elead the same as CDK CRM?" [VERIFIED: https://www.cdkglobal.com/crm, n.d.]. Salesforce markets Automotive Cloud for "automotive lead management, partner performance management" and for unifying "OEM, dealer, captive finance and connected-vehicle data" [VERIFIED: https://www.salesforce.com/automotive/, n.d.].
- **Europe**: the portals themselves increasingly act as the lead-management system (mobile.de Lead Manager Pro; Auto Trader deal tooling). They also open APIs to "Lead Management System partners" (mobile.de) and "lead management systems (LMSs)" (Marktplaats) [VERIFIED: sources in 3.3]. [ASSUMPTION/JUDGEMENT] European dealer groups use OEM-mandated CRMs, DMS-integrated CRMs (Keyloop, Pinewood, incadea, VWE) or Salesforce/Microsoft-based builds; market shares were not verified.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The dealer platform is usually **not** the system of record for leads. Its job is lossless, deduplicated, routed delivery into whichever CRM the rooftop uses, with outcome data flowing back. In Europe, the portal's own lead tool competes with the platform for the dealer's attention, so the platform's value is consolidation across portals.

### 3.7 Deduplication, attribution and routing

- Portal-side lead identity differs: Marktplaats keys on (kind, ad, buyer); mobile.de uses lead plus events and treats a resubmission as a reply; ADF carries a `sequence`/`source` id chain [VERIFIED: sources in 3.1 and 3.3].
- Multi-rooftop routing data exists in Marktplaats payloads (`vestiging`, postcode). mobile.de carries the vehicle's `internalNumber` and the dealer's `customerNumber` [VERIFIED: same].

**Architecture implications** [ASSUMPTION/JUDGEMENT]:

1. **Three-level deduplication.** (a) Exact: the portal's event or lead ID, for idempotent ingestion. (b) Within portal: the same buyer and vehicle → merge into one lead. (c) Cross-portal: the same person (normalized phone or e-mail) on the same or a similar vehicle within N days → link and attribute, but do not merge silently. The dealer may pay each portal per lead.
2. **Attribution rule.** Record *every* touch (portal, channel, call-tracking number) and let reports choose first-touch, last-touch or "the portal that sent the lead which became the sale". Portal ROI disputes, like the UK one in 4.1, are settled with this data.
3. **Routing.** Vehicle → owning rooftop (from the stock record via `internalNumber`/`externalStockId`) → team or salesperson, with fallback rules for unmatched vehicles and after-hours queues. Then push to the CRM or DMS with its own retry and dead-letter handling.

### 3.8 Consent and privacy on the lead path

- mobile.de passes behavioural enrichment only with the buyer's consent (3.3) [VERIFIED].
- Meta requires a dealer privacy-policy URL for lead forms [VERIFIED: Meta auto-ads reference].
- CarGurus' platforms "enable us, dealers, and users to send and receive text messages and other mobile phone communications, which requires us to comply with the Telephone Consumer Protection Act, or TCPA" [VERIFIED: CarGurus 10-K FY2025].
- [ASSUMPTION/JUDGEMENT] In the EU and UK, a portal and a dealer each act as controllers for the buyer's data once a lead is delivered. Marketing follow-up beyond answering the enquiry needs a lawful basis (often consent under ePrivacy rules for e-mail, SMS and WhatsApp marketing). Verify articles against GDPR and national telecom law before printing; this brief did not fetch the legal texts.

**Across markets.** US: TCPA governs calls and texts (CarGurus' risk factor). EU/UK: GDPR plus ePrivacy. NL/DE/BE portals pass pseudonymous buyer IDs (mobile.de `buyerIdentifier`) alongside contact data.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Store **consent as data on the lead** (scope, source, timestamp, text version). Propagate it to the CRM. Enforce it in outbound channels (SMS, WhatsApp, marketing e-mail). Apply retention rules per market to lead payloads, raw ADF e-mails and call recordings.

---

## PART 4: Commercial dynamics: portal pricing and dealer pushback

### 4.1 Auto Trader UK, 2025–26: price rises, Deal Builder and the dealer revolt ⚠

- **Price rises.** CEO Nathan Coe confirmed a 5.5% increase in package prices from 1 April 2026, "lower than normal", after 8% the year before. Starter packages were excluded ("You pay more, you get more") [WIDELY REPORTED: https://cardealermagazine.co.uk/autotrader-boss-confirms-package-prices-will-rise-again-and-explains-why-in-car-dealer-podcast/321583, published 2026-01-23].
- **The November 2025 protest.** On 12 November 2025, dealers organized in a Facebook group (more than 3,300 members) cancelled or downgraded packages at 11:59 am. Their reasons: the mandatory Deal Builder rollout, changes to contact buttons, fewer leads (blamed on requiring an account before an enquiry), annual price rises, and the £99 reservation, seen as taking a car off sale. Individual dealers reported saving £3,500 and £20,000 a month; one cut from 70 advertised cars to seven. Auto Trader said cancellations were "less than 100". Shares fell 3.7% in a day and 14.6% over five days. A 0.25% transaction fee had been removed in May 2025, though Auto Trader did not rule out future charges [WIDELY REPORTED: https://cardealermagazine.co.uk/hundreds-of-car-dealers-claim-they-have-cancelled-auto-trader-packages-as-part-of-mass-protest/320149, published 2025-11-13].
- **Company account (FY26).** H2 revenue growth slowed to 3%, "reflecting both the more difficult trading conditions and retailer feedback regarding our Deal Builder product roll-out". The response: "pausing auto-rollout; holding open listening sessions; establishing customer advisory groups; and introducing 'request a reservation'". The stock lever cost £48 of ARPR because "From November 2025 … a number of retailers reduced the number of vehicles advertised on the platform". Average forecourts fell 0.5% to 13,942. Deal Builder nonetheless grew to more than 6.7k retailers and 175k live vehicles, and the rollout "recommenced" [VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21].

**Across markets.** US portals report comparable dealer-economics KPIs: Cars.com's monthly ARPD of $2,460 (2025, down 1%) for 19,544 dealer customers, and CarGurus' QARSD with 34,409 paying dealers [VERIFIED: Cars.com 10-K FY2025, filed 2026-02-26; CarGurus 10-K FY2025, filed 2026-02-19]. No comparable dealer-pushback evidence was verified for mobile.de, AutoScout24 or Marktplaats in this session.

**Architecture implications for dealer software** [ASSUMPTION/JUDGEMENT]:

1. **Dealers respond to portal pricing by changing what they syndicate.** The UK revolt showed up directly as cut advertised stock. Dealer platforms need **per-channel, per-vehicle publish rules** (e.g. "only cars over 30 days on Auto Trader", "all stock to Marktplaats") and fast bulk changes to them.
2. **Portal-controlled transactional states** (reservations, deals) reach into the dealer's stock record. The platform must ingest them (Deal Notifications, lifecycle locks) and propagate a reservation on one portal to every other channel. Otherwise a car reserved on Auto Trader stays live, and sellable, elsewhere.
3. **Multi-portal attribution data is the dealer's negotiating evidence.** Platforms that can show cost per sold car by portal give dealers leverage in exactly the disputes above.

---

## PART 5: Reference architecture (synthesis)

[ASSUMPTION/JUDGEMENT] All of this part is the analyst's synthesis of the contracts above.

```
                  DMS / IMS / pricing tool / photo studio
                                  │  (stock events, full snapshots)
                                  ▼
        ┌──────────── Vehicle stock record (canonical) ─────────────┐
        │ identity (VIN/plate/HSN-TSN) · spec + equipment (canonical│
        │ codes) · price · images (master set + hashes) · rooftop   │
        └───────────────┬───────────────────────────────────────────┘
                        ▼
        Publish rules per (rooftop, channel)  ──►  Pre-publish validation
        (who, what, when; dealer pricing levers)    (regulatory + portal policy)
                        ▼
        Desired state per (vehicle, channel)  ──►  Publish queue keyed by (vehicle, channel)
                                                   rate limiter + ramp-up per channel
                        ▼
   ┌──────────────┬───────────────┬───────────────┬──────────────┬────────────┐
   mobile.de      AutoScout24      Auto Trader     Marktplaats/   Google/Meta/
   adapter        adapter          adapter         2dehands       US file feeds
   (PUT full,     (PUT/PATCH       (PATCH, life-   adapter        (snapshot
   idempotency    allow-list,      cycle saga,     (OAuth)        render, 30%
   header)        channels)        destinations)                  guard)
   └──────────────┴───────────────┴───────────────┴──────────────┴────────────┘
                        ▲  actual state: Ad Stream, Stock Notifications,
                        │  list/poll endpoints, export-status
        Reconciler (desired vs actual; locks; portal-initiated changes; alerts)

   Leads: ADF mailboxes · mobile.de Lead API (cursor) · Marktplaats webhooks ·
          Auto Trader deals/leads · call tracking
            ▼
   Durable inbox (dedupe on event id) → normalize (STAR-like lead + interactions)
            → match vehicle → rooftop → route → CRM/DMS push (retry, dead-letter)
            → outcome write-back to portals (mobile.de status) · consent ledger
```

Design rules distilled from the evidence:

1. **Desired state, not commands.** Syndication converges each channel to a per-(vehicle, channel) desired state, so retries, outages and replays are safe.
2. **Idempotency at both ends.** Outbound: persisted idempotency keys and external IDs (2.2). Inbound: event-ID deduplication (2.5, 3.7).
3. **Serialize per listing per channel**; parallelize across listings within each channel's rate budget (2.3, 2.5).
4. **Delete is a saga with guards** (2.4). Withdrawal blockers and mass-withdrawal thresholds are first-class.
5. **Reconcile continuously.** Portals edit listings too (2.6), push incompletely (2.5) and auto-transition states (2.4).
6. **Canonical taxonomy with versioned per-portal mappings**, keyed by IDs (2.8).
7. **Lead path latency is a product SLO** (3.5). Ingest within seconds, route deterministically, measure first-response time per rooftop.
8. **Consent travels with the lead** (3.8).

---

## Key numbers

| Number | Value | Source | Date |
| --- | --- | --- | --- |
| mobile.de Ad Stream catch-up retention | 24 hours | mobile.de Ad Stream docs | n.d. (accessed 2026-10) |
| mobile.de idempotency header max length | 100 chars | mobile.de Seller API | n.d. |
| mobile.de `internalNumber` max length | 40 chars, unique per seller | mobile.de Seller API | n.d. |
| mobile.de lead statuses | IN_PROGRESS, SOLD, NOT_INTERESTED, SPAM | mobile.de Lead API | 2026-06-25 |
| mobile.de share of written replies AI-generated | 45% | mobile.de newsroom | 2026-07-15 |
| mobee pilot: answered calls outside opening hours | 91% (19 NL dealers, Mar–May 2026) | mobile.de newsroom | 2026-07-15 |
| AutoScout24 retry start | 100 / 200 / 400 ms, ≥3 retries, jitter | AutoScout24 error_handling.md | n.d. |
| AutoScout24 batch ramp-up advice | 5–10 minutes | same | n.d. |
| AutoScout24 image limits | PNG/JPEG ≤20 MB, 50–10,000 px | AutoScout24 workflow.md | n.d. |
| AutoScout24 orphan image deletion | 1 day (never associated); immediate (de-associated) | same | n.d. |
| Belgian Car-Pass URL mandatory on AS24 | from 2026-06-01 | AutoScout24 changelog | 2026-05-14 |
| Car-Pass documents issued (BE, 2025) | 855,169; 1,466 fraud cases | car-pass.be | n.d. (2025 report) |
| Auto Trader webhook retries | +10 s, +30 s, +30 min | Auto Trader docs | n.d. |
| Auto Trader auto-transitions | DUE_IN 28 d, FORECOURT 56 d, SALE_IN_PROGRESS 28 d, SOLD 60 d, WASTEBIN 28 d | Auto Trader docs | n.d. |
| Auto Trader Leads API page size | 100 | Auto Trader docs | 2024-06 |
| Marktplaats webhook response budget | 2 seconds | Marktplaats LMS docs | n.d. |
| Google Vehicle Listings feed cadence (discontinued) | every 4 h recommended, ≥ daily; expiry 3 days; 30% drop guard | Google developers | 2024-11-20 |
| Google vehicle ads images | 1 + up to 10; min 500×500; ≤16 MB | Google Merchant Center help | n.d. |
| Meta catalog images | ≤20, ≤4 MB each; Marketplace ≥2 and >500 mi/km | Meta developers | n.d. |
| ADF 1.0 final | 3 May 2000 | adfxml.info | 2000 |
| HBR lead study | 37% within 1 h; 42 h average; 23% never; 7× / 60× | SmartCompany summarizing HBR | 2011 |
| Pied Piper 2025 | 4,023 dealers; 19% no personal response; score 65/100 | Auto Remarketing | 2025-03-03 |
| Auto Trader package price rise | 8% (Apr 2025); 5.5% (Apr 2026) | Car Dealer Magazine | 2026-01-23 |
| Auto Trader stock-lever effect on ARPR | −£48 (FY26) | Auto Trader FY26 release | 2026-05-21 |
| Deal Builder retailers / live vehicles | 6.7k / 175k (March 2026) | same | 2026-05-21 |
| Cars.com monthly ARPD | $2,460 (2025) | Cars.com 10-K | 2026-02-26 |
| CarGurus paying dealers | 34,409 (end 2025) | CarGurus 10-K | 2026-02-19 |

## Open questions / not verifiable

- **US portal feed specifications** (Cars.com, CarGurus, Autotrader.com): formats, update cadence, delete semantics and image rules are not public. Ask an IMS vendor, or treat them as judgement.
- **Kleinanzeigen** dealer publishing: is it a separate API, or are mobile.de dealer listings shown there? Not verified.
- **Facebook Marketplace** dealer inventory in NL/BE/DE/UK/US in 2026: Meta's catalog documents Marketplace rules, but current eligibility by country is unverified.
- **Motors.co.uk and CarGurus UK** dealer integration contracts: not found.
- **Whether mobile.de dealer listings will be offered on AutoTrack/Gaspedaal**, or AutoScout24 listings beyond its mobile_de export, after the 2025 NL consolidation. Watch both changelogs.
- **mobile.de and AutoScout24 rate limits**: AutoScout24 documents 429 behaviour but no numbers; mobile.de documents none.
- **The STAR Sales Lead API schema** (format, fields) and its relation to ADF: the download was not read.
- **Lead-response research for Europe**: no independent study comparable to Pied Piper was found.
- **Portal price rises and dealer pushback outside the UK**: not found.
- **CRM market shares** (US and EU) and DealerSocket ownership: not verified.
- **Belgian Car-Pass law details** (whether a URL or QR must appear in online ads by law, or only on the document at sale): the portal enforces a URL; the legal basis was cited by the portal, not read.

## Source list

| # | Title | Publisher / author | Year | URL |
| --- | --- | --- | --- | --- |
| 1 | Seller API Documentation | mobile.de | n.d. (2026) | https://services.mobile.de/manual/seller-api.html |
| 2 | Lead API Documentation (version 2026-06-25) | mobile.de | 2026 | https://services.mobile.de/manual/lead-api.html |
| 3 | Ad Stream documentation | mobile.de | n.d. | https://services.mobile.de/manual/ad-stream.html |
| 4 | APIs overview | mobile.de | n.d. | https://services.mobile.de/manual/index.html |
| 5 | Schneller zum Abschluss: Plattform-Update Sommer 2026 | mobile.de newsroom | 2026 | https://newsroom.mobile.de/plattform-update-sommer-2026/ |
| 6 | AutoScout24 Listing Creation API documentation (README, design, workflow, data models, error handling, FAQ, migration, changelog) | AutoScout24 | n.d. (changelog to 2026-10-19) | https://listing-creation.api.autoscout24.com/docs |
| 7 | Autotrader Connect developer documentation and release notes | Autotrader UK | n.d. (2024–26) | https://developers.autotrader.co.uk/documentation |
| 8 | Full year results for the year ended 31 March 2026 | Autotrader Group plc | 2026 | https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf |
| 9 | Marktplaats API 1.0 documentation (overview, advertisement, webhooks) | Marktplaats B.V. | 2019 / © 2023 | https://api.marktplaats.nl/docs/v1/index.html |
| 10 | Marktplaats / 2dehands / 2ememain API solutions for Lead Management Systems | Marktplaats B.V. | n.d. | https://api.marktplaats.nl/docs/v2/lms/index.html |
| 11 | Lead Delivery Service webhook V3 (OpenAPI 3.2.0) | Marktplaats B.V. | n.d. | https://api.marktplaats.nl/docs/v2/lms/lead-delivery-webhook-v3.yaml |
| 12 | AutoTrack en Gaspedaal.nl onderdeel van AutoScout24 | Emerce | 2025 | https://www.emerce.nl/nieuws/autotrack-gaspedaalnl-onderdeel-autoscout24 |
| 13 | B2C advertising integrations | CarCollect | n.d. | https://www.carcollect.com/integrations/tag/b2c-advertising |
| 14 | Freigabe mobile.de / Carwow | Bundeskartellamt | 2026 | https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html |
| 15 | Vehicle ads attributes (product data) | Google Merchant Center Help | n.d. | https://support.google.com/merchants/answer/11192663 |
| 16 | Vehicle ads overview | Google Merchant Center Help | n.d. | https://support.google.com/merchants/answer/11189169 |
| 17 | Vehicle ads image guidelines | Google Merchant Center Help | n.d. | https://support.google.com/merchants/answer/11190670 |
| 18 | Vehicle Listings: feed setup | Google for Developers | 2024 | https://developers.google.com/vehicle-listings/integration-process/feed-setup |
| 19 | Vehicle Listings: feed specification | Google for Developers | 2025 | https://developers.google.com/vehicle-listings/reference/feed-specification |
| 20 | Automotive Ads reference (catalog fields) | Meta for Developers | n.d. | https://developers.facebook.com/documentation/ads-commerce/marketing-api/auto-ads/reference |
| 21 | Auto-lead Data Format (ADF) Version 1.0 | ADF working group (hosted by Dealer Inspire) | 2000 | https://adfxml.info/adf_spec.pdf |
| 22 | ADF XML Info | Dealer Inspire | n.d. | https://adfxml.info/ |
| 23 | Auto-Lead Data Format (ADF) Usage by LeadDriver, release 1.1 | Kelley Blue Book | 2014 | https://ldti.syndication.kbb.com/reference/files/ADF_Usage_Guide.pdf |
| 24 | Receiving Leads | Dealr.cloud | n.d. | https://dealr.cloud/docs/docs/leads/receiving-leads/ |
| 25 | STAR home page | STAR | n.d. | https://www.starstandard.org/ |
| 26 | STAR Announces New Sales Lead Standards API for Automotive | STAR | 2025 | https://www.starstandard.org/index.php/2025/06/03/star-announces-new-sales-lead-standards-api-for-automotive/ |
| 27 | Standard Webhooks specification | Standard Webhooks (community) | n.d. | https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md |
| 28 | The Short Life of Online Sales Leads | Oldroyd, McElheran, Elkington, Harvard Business Review 89(3) | 2011 | https://hbr.org/2011/03/the-short-life-of-online-sales-leads |
| 29 | BYU ScholarsArchive record for #28 | Brigham Young University | 2011 | https://scholarsarchive.byu.edu/facpub/9711 |
| 30 | SmartCompany summary of #28 | SmartCompany | 2011 | https://www.smartcompany.com.au/?p=20719 |
| 31 | Dealerships' responsiveness to internet leads hits record high again | Auto Remarketing | 2025 | https://www.autoremarketing.com/ar/retail/dealerships-responsiveness-to-internet-leads-hits-record-high-again |
| 32 | Hundreds of car dealers claim they have cancelled Auto Trader packages as part of mass protest | Car Dealer Magazine (J. Baggott) | 2025 | https://cardealermagazine.co.uk/hundreds-of-car-dealers-claim-they-have-cancelled-auto-trader-packages-as-part-of-mass-protest/320149 |
| 33 | Autotrader boss confirms package prices will rise again | Car Dealer Magazine | 2026 | https://cardealermagazine.co.uk/autotrader-boss-confirms-package-prices-will-rise-again-and-explains-why-in-car-dealer-podcast/321583 |
| 34 | CarGurus, Inc. Form 10-K for FY2025 | CarGurus / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm |
| 35 | Cars.com Inc. Form 10-K for FY2025 | Cars Commerce / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1683606/000119312526076546/cars-20251231.htm |
| 36 | Car-Pass home page (2025 figures) | Car-Pass vzw | n.d. | https://www.car-pass.be/nl |
| 37 | DealerSocket CRM software | DealerSocket | n.d. | https://dealersocket.com/solutions/crm-software/ |
| 38 | CDK CRM | CDK Global | n.d. | https://www.cdkglobal.com/crm |
| 39 | Salesforce Automotive Cloud | Salesforce | n.d. | https://www.salesforce.com/automotive/ |
| 40 | Research brief: Automotive marketplaces (sibling brief, LISTED) | This repository | 2026 | `_journals/listing-systems-architecture/_research/brief-automotive.md` |
