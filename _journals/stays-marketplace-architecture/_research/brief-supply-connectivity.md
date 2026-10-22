# Research brief: Supply, content and connectivity in accommodation marketplaces

Prepared 21 October 2026 for chapter writers of *BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces*. The brief is vendor-neutral. Booking.com, Google Hotel Center, Oracle OHIP and Mews get the most space because their connectivity documentation is public and could be read in full, not because the book endorses their choices. The brief keeps two worlds apart throughout: **OTA hotel connectivity** (structured ARI messages from PMS, CRS and channel managers) and **hosted-stays calendar sync** (one-unit calendars, iCal feeds, and API connections from vacation-rental software).

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (21 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date, not the fetch date. Many developer-portal and help-centre pages carry no publication date; these are marked **published undated, live 2026-10**, which means only that the page said this on the fetch date.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, vendor case study, partner press release), or from an official page that this session saw only as a search-result snippet and could not fetch (for example, because it redirected to a login portal).
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about a proprietary system a company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Connectivity standards are old and slow-moving (OpenTravel 2003B messages are still in production at Booking.com), but the APIs around them are moving fast: Booking.com is sunsetting several OTA content endpoints for Home providers on 31 December 2026, and Oracle's OPERA event streaming dates from late 2021. Look-to-book figures in particular come from 2004–2016 sources and describe GDS-era systems; they must not be quoted as current.

**Research limitation.** The web-search quota was shared with parallel researchers, so after the first round the brief relied on direct fetches of known URLs. As a result:

- **Expedia Group's supply documentation** (`developers.expediagroup.com/supply/lodging/...`) now redirects to a partner login portal (`connectivityportal.expediagroup.com`) and could not be read. Expedia claims come from search-result snippets of the official pages and are tagged WIDELY REPORTED.
- **The OpenTravel Alliance specification itself** (schemas and message users' guides) was not fetched; the public home page does not expose them. Message semantics are therefore taken from implementers' documentation (Booking.com, Google, AlpineBits), which is how most engineers meet the standard anyway.
- **HTNG specifications** were not fetched; the only HTNG material is a 2020 secondary overview and press items.
- **Channel managers other than SiteMinder** (Cloudbeds, D-EDGE, RateGain, STAAH) have no verified primary figures here; RateGain's Indian-exchange annual report was not reached.
- **Vrbo's own help centre and developer documentation** did not surface; the Vrbo iCal interval comes from third-party PMS help pages (one of which returned HTTP 403).
- **Airbnb's partner API documentation** is private to approved partners. Everything about Airbnb's API is from Airbnb's host help centre or partner announcements.
- **No company has published current message volumes** for its ARI pipeline (updates per second, messages per property per day). The brief says so where it matters and does not estimate them.

**Volatility flags.** ⚠ marks claims likely to change within 12 months, such as endpoint deprecations, partner tiers, ownership, and refresh intervals.

---

## PART 1: The supply data model

### 1.1 Property → room type → rate plan → product

The professional (OTA) supply model has four layers. Booking.com's connectivity documentation is the clearest public statement of it.

| Layer | What it is | Booking.com term and limits |
| --- | --- | --- |
| Property | The bookable establishment: address, policies, facilities, photos, licences | "accommodation", built via Property / Content APIs |
| Room type | A category of physical rooms with an occupancy and a count of units | "room type"; max 100 per property, active and inactive |
| Rate plan | A commercial offer: price logic, meal plan, cancellation policy, restrictions | "rate plan" |
| Product (sellable unit) | A room type × rate plan × conditions combination; ARI is set against this | "roomrate"; max 400 active per property |

- Booking.com defines a room type as "labels or categories used to organise physical rooms in a property", allows "a maximum of 100 room types for a property, including both active and inactive room types", and uses `Quantity` to mean "the number of units of a room type" [VERIFIED: https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-room-types.md, published undated, live 2026-10].
- Booking.com defines the sellable product explicitly: "A roomrate is a unique combination of room type, rate plan, and conditions." A roomrate can add a cancellation policy, meal plan, booking restrictions, value adds and child prices; the room type and rate plan must exist first; a property can have at most 400 active roomrates [VERIFIED: https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-roomrates.md, published undated, live 2026-10].
- Deactivating a room type cascades: "all roomrates (products) you have created for a property with this room type become deactivated as well", and reactivation requires recreating roomrates and pushing availability again [VERIFIED: https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-room-types.md, published undated, live 2026-10]. This is direct evidence that ARI is keyed to the product, not the room type.
- Derived (child) rate plans inherit fields from a parent: Booking.com rejects an update that sets a field the child follows, for example `price` when `FollowsPrice` is set [VERIFIED: https://developers.booking.com/connectivity/docs/ota-rateamountnotif, published undated, live 2026-10].
- Occupancy-based derived pricing ("RLO") prices additional occupancies relative to a base price; LOS and OBP pricing types require property-level enablement [VERIFIED: https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-roomrates.md, published undated, live 2026-10].

[ASSUMPTION/JUDGEMENT] The cardinality is the architectural point. A 60-room hotel with 6 room types and 10 rate plans is not 60 inventory records but up to 60 products × 365–730 days × (price per occupancy + availability + 5–10 restriction flags). Product explosion is why ARI pipelines are delta-based and why channels cap products per property.

### 1.2 Whole homes and units

- Booking.com models a home as a room type whose `Quantity` is the number of identical units, with "multi-bedroom setups" for Apartment, Suite, Chalet, Bungalow, Holiday home, Villa and Mobile home, built from subrooms of type "`Bedroom`, `Living room`, and `Bathroom`" with bed types attached as subroom amenities [VERIFIED: https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-room-types.md, published undated, live 2026-10].
- Apartment, Aparthotel and Condominium property types "require a kitchen or kitchenette in the room types to become open and bookable" [VERIFIED: same URL, published undated, live 2026-10]. The content model enforces category-specific completeness rules.
- ⚠ Booking.com is moving Home providers off the OTA content messages. `OTA_HotelInvNotif` (room content and amenities): "We will sunset this endpoint for Home providers on December 31, 2026", with Home providers urged to adopt "the Rooms API and the Facilities API" [VERIFIED: https://developers.booking.com/connectivity/docs/tsk-modify-room-amenities.md, published undated, live 2026-10]. `OTA_HotelDescriptiveInfo` "was deprecated for Home providers in December 2024" with the same 31 December 2026 sunset [VERIFIED: https://developers.booking.com/connectivity/docs/tsk-retrieve-property, published undated, live 2026-10]. `OTA_HotelDescriptiveContentNotif` (property-level content) is reported as deprecated 31 December 2024 with sunset 31 December 2026 in favour of the Property Details API [WIDELY REPORTED: https://developers.booking.com/connectivity/docs/ota-hoteldescriptivecontentnotif_ctrip, 2024 — official page seen as search snippet; the URL returned 404 on fetch].

[ASSUMPTION/JUDGEMENT] A hosted-stays marketplace typically collapses the hierarchy: the listing is the unit, there is one "room type" of quantity 1, and the "rate plan" layer is replaced by a nightly price plus discounts, fees and a single cancellation policy. Airbnb has not published its internal listing schema; do not describe one.

**OTA vs hosted stays.** The OTA model is a product catalogue (room type × rate plan) with inventory counts per product per day; overbooking risk is about counts going negative. The hosted-stays model is a single-unit calendar where a night is either free or taken; the risk is two channels selling the same night. A platform that serves both (Booking.com does) has to represent a holiday home as a room type with quantity 1 inside the hotel model, which is exactly what its API does.

### 1.3 Content: amenities, photos and taxonomies

- Booking.com publishes a fixed room-amenity code list (OpenTravel "RMA" codes) and normalises synonyms: "Codes 28, 29 and 64 all internally default to 28 (Desk)", so a value written via one code reads back as another [WIDELY REPORTED: https://developers.booking.com/connectivity/docs/codes-rma, 2026 — official page seen as search snippet]. Bed types are amenity codes with a `Configuration` attribute (standard vs alternative arrangement) [WIDELY REPORTED: https://developers.booking.com/connectivity/docs/api-reference/amenity, 2026].
- Booking.com's API modules separate content into Property, Rooms, Facilities, Charges, Content, Photo and Licences APIs, alongside Rates & Availability, Reservations and Request to Book [VERIFIED: https://developers.booking.com/connectivity/docs, published undated, live 2026-10]. A dedicated Licences module reflects short-term-rental registration requirements reaching the connectivity layer.
- AlpineBits HotelData carries "images and licence metadata, descriptions, and room and accommodation categories" alongside availability, rates and reservations [VERIFIED: https://www.alpinebits.org/hotel-data/, published undated (current release 2024-10), live 2026-10].
- HTNG defined a Distribution Content Management specification for delivering hotel descriptive content from the property to distributors [WIDELY REPORTED: https://www.altexsoft.com/blog/hotel-tech-specifications-htng-opentravel/, 2020]. ⚠ Evidence age: six years old.

[ASSUMPTION/JUDGEMENT] Amenity taxonomies are where marketplaces compete on filters, and every channel extends the OpenTravel code lists with its own. Expect a mapping table per channel in any channel manager or PMS, and expect lossy round trips (as the Booking.com desk example shows).

**OTA vs hosted stays.** Hotel content is mostly static, chain-managed and often pushed once from a CRS or content hub; the hard problem is mapping it across many suppliers (PART 6). Hosted-stays content is written by the host, changes often (photos, house rules, licence numbers), and is the main lever for conversion, so it lives inside the marketplace's own editor; API "sync everything" mode hands that control to the software (§4.3).

---

## PART 2: Connectivity standards

### 2.1 OpenTravel (OTA) message set

| Message | Direction (typical) | Purpose |
| --- | --- | --- |
| `OTA_HotelAvailNotifRQ` | supplier → channel | Availability status and restrictions (open/close, MinLOS/MaxLOS, CTA/CTD) per product per date range |
| `OTA_HotelInvCountNotifRQ` | supplier → channel | Inventory counts (rooms left to sell) |
| `OTA_HotelRateAmountNotifRQ` | supplier → channel | Prices per product, date range, occupancy |
| `OTA_HotelResNotifRQ/RS` | channel → supplier (or pulled) | New, modified, cancelled reservations; RS acknowledges |
| `OTA_HotelDescriptiveContentNotifRQ` | supplier → channel | Property-level descriptive content |
| `OTA_HotelInvNotifRQ` | supplier → channel | Room-type definitions and amenities |

[ASSUMPTION/JUDGEMENT] The table synthesises the implementers' docs cited below; directions describe the common case, not a rule of the standard.

- Booking.com uses OpenTravel "at version 2003B", describing it as "a common data model to exchange information", and supplements it with its own B.XML because "OTA cannot support all the functionality we want to offer, so we use B.XML to fill in the gaps"; it also offers JSON APIs and warns "we strongly recommend that you do not mix OTA and B.XML requests" [VERIFIED: https://developers.booking.com/connectivity/docs, published undated, live 2026-10].
- Booking.com's rates endpoint is `POST https://supply-xml.booking.com/hotels/ota/OTA_HotelRateAmountNotif`. It asks partners to "Send only changes, not full refreshes", to keep one hotel and one month per request, and to load availability at least 12 months ahead; dates run from one day in the past to five years ahead; `InvTypeCode` is the Booking.com room type ID and `RatePlanCode` the rate plan ID; a price of 0 means unavailable [VERIFIED: https://developers.booking.com/connectivity/docs/ota-rateamountnotif, published undated, live 2026-10].
- Google's Hotel Prices ARI uses `OTA_HotelAvailNotifRQ` "to update room rate availability and restrictions"; "Each <OTA_HotelAvailNotifRQ> message is treated as a delta update"; "Each type of length of stay restriction is set independently"; closed-to-arrival does not restrict the nights after check-in; Google points to `OTA_HotelInvCountNotifRQ` for counts [VERIFIED: https://developers.google.com/hotels/hotel-prices/xml-reference/ari-avail, published undated, live 2026-10].
- OpenTravel now promotes "OpenTravel 2.0" as a model-driven route from XML to JSON, arguing that "Bespoke JSON implementations hinder clean data acquisition" [VERIFIED: https://opentravel.org/, published undated, live 2026-10].
- Implementers pin different schema vintages: Booking.com 2003B (above), AlpineBits based on OTA 2015A (below), and a Tourisoft integration marking 2009A legacy and 2014A current [WIDELY REPORTED: https://tourisoft.atlassian.net/wiki/spaces/HOT/pages/6520882/Open+Travel+Alliance+OTA, 2024].

[ASSUMPTION/JUDGEMENT] "OTA-compliant" therefore means "uses OpenTravel element names", not "interoperable without mapping". Every channel publishes its own profile (required attributes, code lists, extensions in `TPA_Extensions`), and certification against that profile is the real contract (PART 7).

### 2.2 HTNG (now within AHLA)

- HTNG was founded in 2002 as Hotel Technology Next Generation and renamed Hospitality Technology Next Generation in June 2017 [VERIFIED: https://en.wikipedia.org/wiki/Hotel_Technology_Next_Generation, published undated, live 2026-10].
- ⚠ HTNG is now part of the American Hotel & Lodging Association: in May 2022 HFTP's CEO referred to AHLA's "recent takeovers of HTNG and HAMA" [VERIFIED: https://www.hospitalitynet.org/news/4110267.html, published 2022-05-02]. The brief did not find the takeover announcement itself; the commission's "HTNG/HFTP" pairing reflects a 2018 partnership, not a merger [WIDELY REPORTED: https://www.hotelmanagement.net/tech/hftp-and-htng-sign-partnership-agreement, 2018].
- "Most HTNG standards are developed using specs by OpenTravel Alliance"; HTNG's Product Distribution family covers Availability, Groups, Rates, Reservations, Seamless Shop/Book and Statistics; on-property specs cover PMS-adjacent systems [VERIFIED: https://www.altexsoft.com/blog/hotel-tech-specifications-htng-opentravel/, published 2020-07-20]. ⚠ Evidence age: over three years.
- HTNG's Product Distribution Reservations specification v3.1 is based on OpenTravel 2014B [WIDELY REPORTED: https://confluence.protel.net/download/attachments/84213852/HTNG_Product_Distribution_Reservations_v3.1_2014B_Technical_Specification.pdf?api=v2, 2014].

### 2.3 AlpineBits (Alpine / DACH)

- AlpineBits HotelData is run by the AlpineBits Alliance at NOI Techpark in Bolzano/Bozen, is "developed with a special focus on, but not limited to, Alpine tourism", and is based on OTA 2015A [VERIFIED: https://www.alpinebits.org/hotel-data/, published undated, live 2026-10].
- "The AlpineBits Alliance publishes a new AlpineBits HotelData release every two years"; 2024-10 is current; the 2026-10 release has implementations and certification due in October 2026; the page cites more than 125 known implementations and requests or reservations worth more than €60 million in 2020 [VERIFIED: same URL]. ⚠ A 2026-10 release may have published by the time the chapter is written.

[ASSUMPTION/JUDGEMENT] AlpineBits matters to the book as a worked example of a regional profile of OpenTravel with its own certification, aimed at small independent hotels that sell through regional tourism boards and local portals rather than only global OTAs. Its existence is evidence that "the standard" fragments by market.

**OTA vs hosted stays.** All of PART 2 is OTA hotel connectivity. Hosted-stays marketplaces have no equivalent open standard: they offer either a proprietary partner API (Airbnb, Vrbo, Booking.com's Homes APIs) or the generic calendar format iCalendar (PART 5), which carries busy dates and nothing commercial.

---

## PART 3: Push vs pull ARI and reservation delivery

### 3.1 Four delivery models

| Model | Who opens the connection | Freshness | Load profile | Public example |
| --- | --- | --- | --- | --- |
| ARI push (delta) | Supplier → channel | Seconds–minutes after change | Proportional to change rate | Booking.com, Google ARI, Expedia AR |
| Pull / cache refresh | Channel → supplier | Bounded by poll interval | Proportional to catalogue × frequency | Google Pull |
| Changed-pricing pull | Channel → supplier, for a subset | Better than pull | Smaller | Google Changed Pricing |
| Live query | Channel → supplier per shopper request | Real time | Proportional to shopping (look-to-book) | Google Live Pricing Queries; bedbank/GDS availability calls |

- Google documents all four. ARI push: "you push messages containing a subset of information that represent a pricing model for your properties." Pull: "Google queries your service on a regular basis to refresh its cache of pricing and availability data", best when the partner does not know when prices change. Changed Pricing: "Similar to Pull, except that Google only requests data for a subset of properties", and Google recommends it for reducing message size and volume. Live Pricing Queries are "pricing requests from Google for a current auction", which Google may cache [VERIFIED: https://developers.google.com/hotels/hotel-ads/dev-guide/delivery-mode, published 2025-10-22].
- Partners migrating to ARI can run it alongside Pull; when several sources exist for a property, Google shows the newest price; old Pull or Live Query prices expire within four days of confirmed migration [WIDELY REPORTED: https://support.google.com/hotelprices/answer/10864209, 2025].
- Expedia's Availability and Rates (AR) API is synchronous and partner-initiated at `https://services.expediapartnercentral.com/eqc/ar`; it "cannot be implemented alone" and is paired with either Booking Notification (Expedia opens the connection and pushes) or Booking Retrieval/Confirmation (the partner opens the connection and pulls) [WIDELY REPORTED: https://developers.expediagroup.com/supply/lodging/docs/avail_and_rate_apis/avail_rates/getting_started/introduction, 2025 — official page seen as search snippet; it now redirects to a partner login portal].

### 3.2 Reservations: pull-and-acknowledge at Booking.com

- Booking.com queues reservations per provider in a "Message dispatcher", "The system that consolidates reservation messages specific to providers in a dedicated queue"; `GET OTA_HotelResNotif` "will repetitively return bookings until they are acknowledged" [VERIFIED: https://developers.booking.com/connectivity/docs/reservations-api/reservations-overview, published undated, live 2026-10].
- Partners should "call `GET OTA_HotelResNotif` once per twenty seconds", wait five seconds after an acknowledgement before the next GET, and by default "the response contains only reservations which have not yet been acknowledged" [VERIFIED: https://developers.booking.com/connectivity/docs/reservations-api/retrieving-new-reservations-ota, published undated, live 2026-10].
- If a reservation is not acknowledged (OTA) or retrieved (B.XML) "within a certain acknowledgement window (30 minutes)", Booking.com emails it to the property; the window can be extended to 24 hours via Connectivity Support [VERIFIED: https://developers.booking.com/connectivity/docs/reservations-api/reservations-overview, published undated, live 2026-10].
- Booking.com's Connectivity Notification Service is a webhook layer for "real-time updates to events that either need attention or action"; notifications are "designed to be simple alerts", so the partner makes a follow-up API call for the data [VERIFIED: https://developers.booking.com/connectivity/docs/notification-service/notification-service-overview, published undated, live 2026-10]. Setup requires an HTTPS receiving endpoint and an endpoint serving JWTs for authentication [WIDELY REPORTED: https://developers.booking.com/connectivity/docs/notification-service/notification-service-getting-started, 2026].
- Older OTA_HotelResNotif pages are marked "outdated and is soon going to be deprecated" [WIDELY REPORTED: https://developers.booking.com/connectivity/docs/ota-resnotif, 2026 — page returned 404 on fetch].

[ASSUMPTION/JUDGEMENT] The Booking.com design is a durable outbox with at-least-once delivery, idempotent consumer acknowledgement, and a human fallback (email) when the machine path fails. It is a good pattern for the book's reservation chapter: it decouples channel availability from partner uptime, and the 30-minute email fallback is an explicit, documented degradation mode. The thin-notification webhook (CNS) is the "notify, then fetch" pattern that avoids putting sensitive payloads into webhooks.

### 3.3 PMS-side event delivery

- Oracle's OHIP added a streaming API in Release 21.4 (November 2021): "A new Steaming [sic] API for business event push ... based on GraphQL Subscriptions and uses WebSocket as the transport", initially only for early adopters [VERIFIED: https://docs.oracle.com/en/industries/hospitality/integration-platform/axern/c_release_21_4.htm, published 2021-11].
- OHIP retains streamed messages for 7 days ("Messages not consumed within 7 days are lost and cannot be replayed"); the polling API retains events for 48 hours, cannot replay, and returns at most 20 events per call; partners are charged per event consumed (streaming) or per API call (polling); "Only inbound API calls to OPERA Cloud are throttled; events produced from OPERA Cloud are not"; streaming requires OPERA Cloud Foundation 22.3.0.1 or later; OHIP is "available only through a paid subscription under a pay-as-you-go model" [VERIFIED: https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/c_faqs.htm, published undated, live 2026-10].
- Mews treats polling as the default ("This is called polling, and is not very efficient"), webhooks as the norm when a delay is acceptable ("there may be a lag of up to several minutes"), and WebSockets as "a special case for rare use cases" such as digital keys [VERIFIED: https://docs.mews.com/connector-api/events/communicate, published undated, live 2026-10].
- Mews' Channel Manager API is bidirectional: Mews receives new, modified and cancelled reservations from channel managers, and channel managers must host endpoints to receive Mews' availability updates for "distributing availability, rates and inventory data to sales channels" [VERIFIED: https://docs.mews.com/channel-manager-api, published undated, live 2026-10].
- apaleo exposes Core, Payment and Distribution/ARI APIs with OAuth (auth-code grant for marketplace apps, client credentials for single-hotel projects) and lets integrators "Subscribe to webhooks or ARI updates (availability, rates, and inventory)" [VERIFIED: https://apaleo.dev/, published 2025].

**OTA vs hosted stays.** In hotel connectivity the PMS or CRS is the system of record and pushes ARI outward; reservations flow back via a queue that the connector must drain. In hosted stays, the marketplace calendar is often the system of record for a small host, and the vacation-rental PMS becomes the system of record only for professional managers who connect via API. Whichever system is the system of record is the one that must win conflicts, and the help-centre evidence in §4.3 shows marketplaces still let hosts override synced values locally.

---

## PART 4: The connectivity stack — who sits between the property and the guest

### 4.1 Channel managers

- SiteMinder's FY26 results (year to June 2026): revenue A$266.1m (+22.0% constant-currency organic; +18.6% reported); transaction revenue A$110.9m (+33.8% cc,org); subscription revenue A$155.2m; ARR A$313.7m; "Net property additions were 5.9k, bringing total properties to 56.0k"; Channels Plus grew "from 7k hotels in H1FY26 to almost 10k hotels at year-end" [VERIFIED: https://www.siteminder.com/wp-content/uploads/2026/08/Earnings-Release-SiteMinder-FY26.pdf, published 2026-08-25].
- SiteMinder states that it "generates 140 million reservations worth over A$85 billion in revenue for its hotel customers each year" through "the largest partner ecosystem in the global hotel industry" [VERIFIED: same URL, published 2026-08-25]. This is a self-description in the "About" boilerplate, not an audited KPI.
- FY25 comparison: revenue A$224.3m, total properties 50.1k [WIDELY REPORTED: https://www.siteminder.com/wp-content/uploads/2025/08/sm-fy25-earnings-release-v2.pdf, 2025 — PDF text not extractable in this session; figures from search snippets].
- SiteMinder's channel-side API, SiteConnect, is "Built on Open Travel Alliance standards" and pushes rates, availability and restrictions to channels while handling reservations, modifications and cancellations across OTAs, GDS, booking engines and wholesalers; it claims 99.95% uptime [VERIFIED: https://developer.siteminder.com/siteminder-apis/channels/introduction/siteconnect/api-reference/availability-and-restrictions, published undated, live 2026-10].
- Other vendors publish only channel counts: RateGain's UNO channel manager integrated with Cloudbeds PMS reaches "400+ distribution channels" (announced 1 July 2025); Cloudbeds partnered with STAAH (May 2025); D-EDGE claims 300+ distribution websites [WIDELY REPORTED: https://www.cloudbeds.com/articles/rategain-partnership/, 2025].

[ASSUMPTION/JUDGEMENT] A channel manager is a fan-out and fan-in adapter: one ARI source (PMS or extranet) to N channel dialects, and N reservation sources back to one PMS. Its hard problems are mapping (local room/rate codes to each channel's IDs), ordering (an older update arriving after a newer one), rate-limit shaping per channel, and reconciliation after outages. None of SiteMinder, Cloudbeds, D-EDGE, RateGain or STAAH has published its internal architecture; do not describe one.

### 4.2 PMS, CRS and the switch

- OHIP partner production access requires a listing on the Oracle Hospitality Cloud Marketplace, Oracle Partner Network membership, and customer approval of an integration user in the customer's tenancy [VERIFIED: https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/c_faqs.htm, published undated, live 2026-10]. The gate is commercial and contractual, not only technical.
- ⚠ SynXis (Sabre Hospitality Solutions) changed hands: Sabre closed the sale of Hospitality Solutions to TPG on 7 July 2025 for $1.1 billion; the sale excluded Sabre's hotel B2B distribution business [WIDELY REPORTED: https://www.phocuswire.com/sabre-closes-hospitality-business-sale, 2025]. Chapter writers should not call SynXis "Sabre's CRS" in the present tense.
- SynXis CRS pushes availability, rates and inventory to OTAs, GDSs, booking engines and call centres, and reaches GDSs via direct connections and switch partners [WIDELY REPORTED: https://hospitalitytech.com/oyo-uk-joins-sabres-reservation-system, 2019]. ⚠ Evidence age.
- Pegasus began as THISCO (Hotel Industry Switch Company), founded in 1989 by a consortium of hotel companies to connect hotel reservation systems to the GDSs; its switch was branded UltraSwitch [WIDELY REPORTED: https://encyclopedia.com/books/politics-and-business-magazines/pegasus-solutions-inc, c. 2004]. ⚠ Evidence age: two decades; current ownership not checked.

[ASSUMPTION/JUDGEMENT] The "switch" exists because GDSs speak airline-era seamless-availability protocols and hotels run many CRSs; the switch translates and routes. For the book, the switch is the ancestor of today's channel manager and connectivity hub, and the reason chain hotels hold a CRS as the "single image of inventory" above many PMSs.

### 4.3 Vacation-rental PMS and marketplace APIs

- Airbnb lets API-connected hosts choose between "Sync everything" (listing details come from the software; "Any updates made to new listings through your software will be automatically updated on Airbnb") and "Sync pricing and availability" (content stays on Airbnb, and hosts can still override discounts, fees, taxes and availability on Airbnb) [VERIFIED: https://www.airbnb.com/help/article/2348/what-are-the-ways-i-can-sync-listings-through-my-api-connected-software, published undated, live 2026-10].
- Airbnb warns that "changes made directly on Airbnb might override the rates or availability sent via your software" and that "If you set a promotion or discount directly on Airbnb, the same pricing will not be reflected within your software" [VERIFIED: https://www.airbnb.com/help/article/2965, published undated, live 2026-10]. The marketplace and the PMS are both writable; neither is a strict master.
- Airbnb's Software Partner programme has tiers up to Preferred+; providers undergo a "comprehensive evaluation" against integration, technical, foundational and performance standards and must pass a data security and API quality review; Preferred+ partners have "exceeded" the requirements [VERIFIED: https://www.hostaway.com/blog/airbnb-preferred-software-partner-2025/, published 2025-05-12 — vendor announcement describing Airbnb's programme]. Airbnb's own programme criteria were not found.
- A channel-manager vendor reports that an Airbnb listing can use iCal or API but not both, and that Airbnb at the time allowed only instant booking for API-connected listings [WIDELY REPORTED: https://wiki.beds24.com/index.php/AirBnB.com, 2024]. ⚠ Airbnb policy; re-check before stating.
- Vrbo's Connectivity Partner programme awards "an Elite or Preferred designation"; providers "are rated on several technical and performance criteria", including integration quality, connection reliability and client performance on Vrbo; the page lists Track, Bluetent, Rentals United, Hostfully, Streamline, OwnerRez, Lodgix, iTrip, Hostaway, Escapia, Avantio and Ciirus among "more than a hundred" software solutions [VERIFIED: https://partner.expediagroup.com/en-au/industries/vacation-rentals/vrbo-connectivity-solutions, published undated, live 2026-10].
- Guesty claims direct API connections to Airbnb, Vrbo, Booking.com and Expedia and top-tier status with each; a Guesty for Hosts help article says pricing syncs with Airbnb in real time but daily for Booking.com and Vrbo; a hands-on review measured sub-minute cross-channel sync [WIDELY REPORTED: https://www.guesty.com/channel-manager-guide/, 2026]. Vendor claims; the daily-pricing note applies to the lighter product.

**OTA vs hosted stays.** Hotel connectivity is many-to-many through specialist intermediaries (PMS → CRS/channel manager → OTA/GDS/bedbank). Hosted-stays connectivity is shallower: host → vacation-rental PMS → three or four marketplaces, or host → marketplace directly with iCal stitching the rest together. The VR PMS often bundles channel manager, PMS, messaging and pricing in one product, so the "channel manager" layer is usually not a separate company.

---

## PART 5: iCal calendar sync (hosted stays)

### 5.1 What the standard gives you

- iCalendar is defined in RFC 5545 (September 2009, editor B. Desruisseaux, obsoleting RFC 2445): it "defines the iCalendar data format for representing and exchanging calendaring and scheduling information" [VERIFIED: https://www.rfc-editor.org/rfc/rfc5545, published 2009-09].
- All-day events "have a DATE value type for the "DTSTART" property instead of the default value type of DATE-TIME", and "The "DTEND" property for a "VEVENT" calendar component specifies the non-inclusive end of the event" [VERIFIED: same URL]. A booking from 3 to 6 June is DTSTART 20260603 / DTEND 20260606 and blocks the nights of 3, 4 and 5 June, which matches hotel night semantics; off-by-one bugs come from implementers who treat DTEND as inclusive.
- UID "defines the persistent, globally unique identifier for the calendar component" [VERIFIED: same URL]. It is the only key a consumer can use to detect a changed or cancelled block between polls.
- The visible portions of RFC 5545 define no polling or refresh interval [VERIFIED: same URL]. [ASSUMPTION/JUDGEMENT] RFC 5545 is a file format; the feed is fetched over plain HTTP(S) on the consumer's own schedule, so freshness is set by each platform's importer, not by the standard.

### 5.2 Platform behaviour

| Platform | Import refresh | What is carried | Evidence |
| --- | --- | --- | --- |
| Airbnb | "every 3 hours", manual Refresh available, up to 2 years imported, link must end in .ics | Blocked/booked nights | VERIFIED (help centre, 2026-10) |
| Vrbo | about every 60 minutes; 1–2 hours in practice | Blocked dates | WIDELY REPORTED (third-party PMS help) |
| Booking.com | not documented publicly; export "Booked dates only" or "Booked and closed dates" | Booked/closed dates | WIDELY REPORTED (third-party help) |
| Typical third-party tools | 5 minutes to 24 hours | Busy dates only | WIDELY REPORTED |

- Airbnb: "Your Airbnb calendar automatically updates every 3 hours"; hosts can press Refresh, but "we're only able to request updates from the other website so many times"; imports cover "up to 2 years of data"; import links must end in .ics; nights blocked elsewhere "may or may not be blocked on Airbnb" [VERIFIED: https://www.airbnb.com/help/article/99, published undated, live 2026-10]. ⚠ A search snippet of the same article showed "every 2 hours"; the interval has changed before and may change again.
- Airbnb's iCal export carries only blocked dates and the last four digits of the guest's phone number; "Personal information like guests name and Email address and the price are not provided"; refresh "can be as slow as once per day" from the importing side; the vendor recommends the API as "much more reliable" [VERIFIED: https://wiki.beds24.com/index.php/Airbnb_iCal, published undated, live 2026-10].
- From 1 December 2019, new Airbnb reservations received over iCal stopped carrying guest name, phone number or other personally identifiable information [WIDELY REPORTED: https://myallocator.cloudbeds.com/hc/en-us/articles/360038298514-Airbnb-iCal-Announcement-and-Next-Steps-December-2019, 2019 — page returned 403 on fetch].
- Vrbo imports iCal calendars every 60 minutes, and a PMS vendor recommends manually blocking dates until the next sync for urgent bookings [WIDELY REPORTED: https://support.hostaway.com/hc/en-us/articles/360002562114-Vrbo-Connect-via-iCal, 2024 — 403 on fetch]; another vendor reports Vrbo is usually up to date after one to two hours [WIDELY REPORTED: https://support.smoobu.com/hc/en-us/articles/360007320340-Why-is-my-Vrbo-calendar-not-up-to-date, 2024].
- When Booking.com is connected to a channel manager, imported iCal connections cannot stay active [WIDELY REPORTED: https://help.hospitable.com/en/articles/8709568-check-for-and-disconnect-an-imported-ical-from-booking-com, 2024]. A tool vendor warns against editing availability in Booking.com's own calendar while syncing because it "overrides the imported availability and can lead to double bookings" [WIDELY REPORTED: https://www.bookingmood.com/hr-HR/docs/synchronization/ical, 2025].
- An Airbnb community thread reports a Booking.com feed failing validation for a missing `DTSTAMP` (a required property) and newly blocked dates not appearing [WIDELY REPORTED: https://community.withairbnb.com/t5/Help-with-your-business/iCAL-Calendar-Import-Issue-from-Booking-com/m-p/360608, c. 2020]. Anecdotal, but it illustrates that producers ship non-conforming feeds.

### 5.3 Why iCal double-books

[ASSUMPTION/JUDGEMENT] The double-booking window is structural and can be reasoned about without proprietary data:

- **Window = producer publish lag + consumer poll interval + processing.** With Airbnb polling every 3 hours and Vrbo every hour, two marketplaces can each sell the same night for up to several hours. No help page found in this session gives an explicit "double booking" warning tied to iCal latency, though Airbnb's "may or may not be blocked" wording comes close.
- **No transactions, no holds.** iCal has no reserve-then-confirm step; the first booking to land wins on its own platform and the second platform learns of it on its next poll.
- **No commercial data.** Prices, restrictions, guest counts and cancellation policies do not travel, so iCal-only hosts maintain rates by hand on every platform.
- **Cancellation is inferred.** A block disappearing from the feed is the only signal of a cancellation; a failed fetch (timeout, invalid feed) must not be read as "all blocks removed".

The defensible design stance for the book: treat iCal as an eventual-consistency fallback for single-unit hosts, design the cancellation path (who pays, who rehouses) as a first-class flow, and push professional hosts to API connections.

**OTA vs hosted stays.** Hotel ARI is a counted, transactional, minutes-fresh feed with restrictions and prices. iCal is an uncounted, non-transactional, hours-fresh feed of busy dates. Hotels absorb occasional overbooking by walking guests to a nearby hotel; a single-unit host has nowhere to walk the guest, so the marketplace's cancellation and rebooking policy carries the cost.

---

## PART 6: Wholesale, GDS and content mapping

### 6.1 Bedbanks and wholesalers

- Hotelbeds' booking flow is availability → choose a `rateKey` → CheckRate if the rate is `RECHECK` (it "re-evaluates the pricing and availability of this rate") → booking; `BOOKABLE` rates skip the recheck; the Content API is assumed to be used first "to map the hotelbeds codes against your system" [VERIFIED: https://developer.hotelbeds.com/documentation/hotels/booking-api/workflow/, published undated, live 2026-10].
- HBX Group (Hotelbeds' parent) described itself at its 2025 IPO as a B2B marketplace connecting "more than 250,000 hotels" to approximately 60,000 B2C distributors [WIDELY REPORTED: https://www.phocuswire.com/hbx-group-ipo-spanish-stock-exchanges, 2025].
- WebBeds (Web Travel Group) reported FY25 (to March 2025) total transaction value of about A$4.9 billion (+22%) on 8.4 million bookings, and FY26 TTV of about A$5.8 billion (+20%) [WIDELY REPORTED: https://www.raskmedia.com.au/2025/05/28/web-travel-asxweb-share-price-soars-12-on-strong-fy25-result/, 2025; https://www.webtravelgroup.com/news/1h26/, 2026].

[ASSUMPTION/JUDGEMENT] The bedbank's two-step rate (search returns a cached or contracted price, check-rate re-prices before booking) is the pull-model counterpart to ARI push: the distributor cannot hold the full catalogue fresh, so it re-validates at the point of commitment. The book should present "price changed at booking" as an expected outcome with a designed user flow, not an error.

### 6.2 GDS hotel content

- Amadeus markets "access to +1M properties, including content from top regional and global aggregators" and "around 310 chains", with aggregator content "seamlessly integrated into the Amadeus shopping display" following "the same automated booking method and flow", while "Payment settlement is handled according to each aggregator's individual specifications" (prepaid rates with commission upfront) [VERIFIED: https://amadeus.com/documents/en/hospitality/sales-sheet/amadeus-hotels-aggregator-content.pdf, published undated, live 2026-10].
- Sabre's Content Services for Lodging (announced 2017, launched 2018) combined GDS chain content with non-GDS aggregators (initially Bedsonline, TravelBound and Expedia Affiliate Network), with side-by-side display because the same hotel from different sources can carry different inclusions [WIDELY REPORTED: https://www.phocuswire.com/Sabre-Corp-to-integrate-multisource-hotel-content-into-GDS, 2017]. ⚠ Evidence age; partner list has since changed.

[ASSUMPTION/JUDGEMENT] GDS hotel content now means "chain CRS content via switch or direct connect, plus resold aggregator content", which is exactly why the same hotel appears several times and mapping becomes a core platform service.

### 6.3 Hotel and room mapping

- Gimmonix states that suppliers "list the same hotel under different names, addresses, or details" (e.g. "Hilton Garden Inn Times Square" vs "HGI NYC Times Sq."), that matching compares "name, address, geo-coordinates" after normalisation, and that "The rest hides duplicates, mismatched properties, and rates attached to the wrong hotel" for the roughly 40% of inventory it says is not accurately mapped industry-wide [VERIFIED: https://gimmonix.com/news/how-does-hotel-mapping-work, published 2026 (dated 03.08.2026)]. The 60% figure is a vendor claim without a cited method.
- Room mapping: "The same room is often described in dozens of ways"; Gimmonix matches on "30+ attributes, including bed configuration, size, view, amenities, location, special features, and board basis" and scores primary vs secondary matches [VERIFIED: https://gimmonix.com/news/room-mapping-the-process-explained, published 2026].
- Vervotech lists the failure modes: duplicates across suppliers, supplier "ID drift", schema mismatch, and room-name inconsistency ("Deluxe King" vs "King Deluxe Room" vs "DLX-K"); it combines "deterministic rules (geocoding, name fuzzy-matching, address resolution)" with ML models and a content operations team, refreshes daily, and claims 3M+ properties, 400+ suppliers and 99.998% accuracy [VERIFIED: https://www.vervotech.com/hub/hotel-mapping/, published 2026]. Accuracy figures are vendor claims with no stated measurement method; Vervotech's own pages quote figures from 95% to 99.999%.
- Gimmonix advertises stable IDs that "never change and never get recycled/renamed" [WIDELY REPORTED: https://gimmonix.com/mapping-works/, 2026].

[ASSUMPTION/JUDGEMENT] Mapping is an entity-resolution system with human review, and its outputs (a canonical property ID, a canonical room ID, confidence) are load-bearing for search deduplication, price comparison and post-booking support. Expedia and Booking.com operate their own mapping for affiliate and metasearch supply but have not, in sources found here, documented how; do not describe it.

**OTA vs hosted stays.** Mapping is an OTA and B2B problem: the same hotel arrives from chain CRS, bedbanks and GDS. Hosted-stays duplication is a different problem: the same home listed by the host on several marketplaces (fine) or listed twice on one marketplace, or fraudulently copied (a trust-and-safety problem, covered elsewhere in the book).

---

## PART 7: Certification and partner programmes

| Programme | Tiers (as reported) | Criteria (as reported) | Evidence |
| --- | --- | --- | --- |
| Booking.com Connectivity Partner | Standard, Advanced, Premier; Premier Plus reported for 2026 | Business value (portfolio), implementation, connection quality, engagement | Official onboarding page + partner press releases |
| Airbnb Software Partner | Recognized → Preferred → Preferred+ | Integration, technical, foundational, performance standards; data-security and API-quality review | Partner announcement |
| Vrbo Connectivity Partner | Preferred, Elite | Integration quality, connection reliability, client performance | Official partner page |
| Oracle OHIP | Marketplace listing + OPN membership | Commercial gate, customer approval | Official FAQ |
| AlpineBits | Release-based certification | Conformance to the biennial release | Official page |

- Booking.com: "To become Booking.com Connectivity Partners, companies must meet specific onboarding requirements", and partners are expected to support all API functions and keep up with API changes [VERIFIED: https://developers.booking.com/connectivity/docs, published undated, live 2026-10].
- ⚠ Booking.com ranks providers into tiers by points for business value, product implementation, connection quality and engagement; one source reports a fourth tier, Premier Plus, added in 2026 [WIDELY REPORTED: https://www.e-gds.com/en/News/e-GDS-Booking-Premier-Partner-2023, 2023; https://hotelrunner.com/en/news/corporate/hotelrunner-named-bookingcoms-premier-connectivity-partner-for-an-impressive-10th-time/, 2026]. Official point weights were not found.

[ASSUMPTION/JUDGEMENT] Certification programmes are the marketplace's quality gate on someone else's software: they turn connection reliability (missed reservations, stale ARI, mapping errors) into a ranking the marketplace can enforce commercially. For the book, they belong with SLOs: the marketplace cannot own the partner's uptime, so it scores it.

**OTA vs hosted stays.** Hotel programmes rate channel managers and PMSs that mostly move ARI and reservations. Hosted-stays programmes also rate content sync, messaging and guest experience, because the software often owns the whole listing ("sync everything").

---

## PART 8: Message volumes and look-to-book

- No marketplace or channel manager found in this session publishes ARI message volumes. Do not invent them.
- Booking.com's documented constraints shape volume: deltas only, one hotel and one month per request, up to five years ahead, 400 active roomrates per property [VERIFIED: https://developers.booking.com/connectivity/docs/ota-rateamountnotif and https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-roomrates.md, published undated, live 2026-10].
- OHIP: "there is no maximum number of events" on streaming, while the polling API returns at most 20 events per call [VERIFIED: https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/c_faqs.htm, published undated, live 2026-10].
- Look-to-book: a 2016 industry opinion piece reported distributor ratios rising from about 500:1 to "the order of 20,000:1", attributing the excess not mainly to metasearch but to the same request being sent by "several different bedbanks, wholesalers or aggregators to the same supply source" and to automated price scraping [VERIFIED: https://www.hospitalitynet.org/opinion/4074433.html, published 2016-02-18]. ⚠ Evidence age: ten years.
- PhocusWire reports ratios exceeding 25,000:1 on some indirect channels, with uncached traffic hitting the CRS at peak [WIDELY REPORTED: https://www.phocuswire.com/Reconsider-GDS-OTA-connections-hotels, c. 2017]. A 2004 piece lists several competing definitions of the metric [WIDELY REPORTED: https://www.hotel-online.com/News/PR2004_4th/Oct04_LooktoBook.html, 2004].
- Pegasus introduced an "Enhanced Shopping Transaction" to reduce many single-property availability calls degrading supplier CRSs [WIDELY REPORTED: https://www.travelagentcentral.com/hotels/pegasus-introduces-enhanced-shopping-transaction, c. 2010s].

[ASSUMPTION/JUDGEMENT] Look-to-book is the economic argument for push. A pull/live-query channel loads the supplier in proportion to shopping, which is orders of magnitude above bookings; a push channel loads it in proportion to change, which is bounded by the hotel's own repricing. That is why OTAs that hold large direct hotel supply standardise on ARI push and cache, while B2B distribution and metasearch still rely on cached pull plus re-check at booking. Pricing algorithms that reprice frequently erode the advantage of push: SiteMinder's growth in dynamic-pricing products (Dynamic Revenue Plus "more than 50k rooms") implies more ARI changes per room per day [VERIFIED for the product figure: https://www.siteminder.com/wp-content/uploads/2026/08/Earnings-Release-SiteMinder-FY26.pdf, published 2026-08-25; the implication is judgement].

**OTA vs hosted stays.** Hotel look-to-book pressure lands on the CRS and channel manager; a cache in front of supply is mandatory. A hosted-stays marketplace holds its own calendar, so search hits the marketplace's own index rather than the host's system; look-to-book becomes an internal search-cost question, and the only outbound load is iCal export polling by other platforms.

---

## Key numbers

| Number | Value | Source | Date |
| --- | --- | --- | --- |
| Booking.com max room types per property | 100 (active + inactive) | developers.booking.com managing-room-types | live 2026-10 |
| Booking.com max active roomrates (products) per property | 400 | developers.booking.com managing-roomrates | live 2026-10 |
| Booking.com rate date horizon | 1 day past to 5 years ahead; load ≥12 months | developers.booking.com ota-rateamountnotif | live 2026-10 |
| Booking.com recommended reservation poll interval | once per 20 seconds | developers.booking.com retrieving-new-reservations-ota | live 2026-10 |
| Booking.com unacknowledged reservation email fallback | 30 minutes (extendable to 24 h) | developers.booking.com reservations-overview | live 2026-10 |
| Booking.com OTA content endpoints sunset for Home providers | 31 December 2026 | developers.booking.com | live 2026-10 |
| Booking.com OTA schema version | 2003B | developers.booking.com/connectivity/docs | live 2026-10 |
| AlpineBits release cadence / implementations | every 2 years; >125 implementations | alpinebits.org | release 2024-10 |
| OHIP streaming retention / polling retention | 7 days / 48 hours | Oracle OHIP FAQ | live 2026-10 |
| OHIP polling page size | 20 events per call | Oracle OHIP FAQ | live 2026-10 |
| OHIP streaming launch | Release 21.4 | Oracle release notes | 2021-11 |
| Mews webhook lag | "up to several minutes" | docs.mews.com | live 2026-10 |
| SiteMinder properties | 56.0k | SiteMinder FY26 release | 2026-08-25 |
| SiteMinder revenue / ARR | A$266.1m / A$313.7m | SiteMinder FY26 release | 2026-08-25 |
| SiteMinder reservations generated (self-described) | 140m/yr, >A$85bn | SiteMinder FY26 release | 2026-08-25 |
| Airbnb iCal import refresh | every 3 hours; up to 2 years imported | airbnb.com/help/article/99 | live 2026-10 |
| Vrbo iCal import refresh | ~60 minutes | Hostaway help (third party) | c. 2024 |
| RFC 5545 published | September 2009 | rfc-editor.org | 2009-09 |
| HBX Group hotels connected | >250,000 | PhocusWire (IPO coverage) | 2025 |
| WebBeds FY25 TTV / bookings | ~A$4.9bn / 8.4m | Rask Media | 2025 |
| Sabre Hospitality Solutions (SynXis) sale to TPG | $1.1bn, closed 7 July 2025 | PhocusWire | 2025 |
| Amadeus hotel content | >1M properties, ~310 chains | Amadeus sales sheet | undated |
| Look-to-book (distributors) | ~20,000:1 | Hospitality Net opinion | 2016-02-18 |
| Vervotech claimed mapping scale | 3M+ properties, 400+ suppliers | vervotech.com | 2026 |

## Open questions / not verifiable

- **ARI message volumes** at any OTA, channel manager or PMS (messages per second, per property per day, peak multipliers). Not published.
- **Expedia supply API details** (AR message limits, Booking Notification retry semantics, EQC deprecation status). Documentation is behind a partner login portal as of October 2026.
- **Airbnb partner API**: endpoint semantics, rate limits, webhook guarantees and the current instant-book requirement for API-connected listings. Private to partners.
- **Vrbo's own** iCal interval and API documentation. Only third-party statements found.
- **Booking.com's iCal import interval** for Homes. Not found in official sources.
- **OpenTravel schema text** for the messages in §2.1, and the current OpenTravel release. Not fetched.
- **HTNG**: the date and terms of its move into AHLA; current specification versions.
- **Booking.com Connectivity Partner Programme** scoring rules and the reported 2026 Premier Plus tier. Only partner press releases.
- **Channel managers other than SiteMinder**: property counts and architecture (Cloudbeds, D-EDGE, RateGain, STAAH).
- **Current look-to-book ratios**; all figures found are 2004–2017.
- **Mapping accuracy**: no independent benchmark for Gimmonix, Vervotech or GIATA; how Expedia and Booking.com map affiliate supply internally.
- **Pegasus** current ownership and role.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| RFC 5545: Internet Calendaring and Scheduling Core Object Specification (iCalendar) | IETF / B. Desruisseaux (ed.) | 2009 | https://www.rfc-editor.org/rfc/rfc5545 |
| Connectivity API documentation (overview) | Booking.com | undated, live 2026 | https://developers.booking.com/connectivity/docs |
| Content overview | Booking.com | undated, live 2026 | https://developers.booking.com/connectivity/docs/index-content |
| Update rates (OTA_HotelRateAmountNotif) | Booking.com | undated, live 2026 | https://developers.booking.com/connectivity/docs/ota-rateamountnotif |
| Managing room types | Booking.com | undated, live 2026 | https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-room-types.md |
| Managing roomrates | Booking.com | undated, live 2026 | https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-roomrates.md |
| Managing room amenities (HIN deprecation for Homes) | Booking.com | undated, live 2026 | https://developers.booking.com/connectivity/docs/tsk-modify-room-amenities.md |
| Retrieving property details (HDI deprecation for Homes) | Booking.com | undated, live 2026 | https://developers.booking.com/connectivity/docs/tsk-retrieve-property |
| OTA_HotelDescriptiveContentNotif (deprecation) | Booking.com | 2024 | https://developers.booking.com/connectivity/docs/ota-hoteldescriptivecontentnotif_ctrip |
| RMA codes | Booking.com | 2026 | https://developers.booking.com/connectivity/docs/codes-rma |
| Understanding the Reservations API | Booking.com | undated, live 2026 | https://developers.booking.com/connectivity/docs/reservations-api/reservations-overview |
| Retrieving new reservations (OTA) | Booking.com | undated, live 2026 | https://developers.booking.com/connectivity/docs/reservations-api/retrieving-new-reservations-ota |
| Connectivity Notification Service overview | Booking.com | undated, live 2026 | https://developers.booking.com/connectivity/docs/notification-service/notification-service-overview |
| CNS getting started | Booking.com | 2026 | https://developers.booking.com/connectivity/docs/notification-service/notification-service-getting-started |
| OTA_HotelResNotif (outdated page) | Booking.com | 2026 | https://developers.booking.com/connectivity/docs/ota-resnotif |
| ARI: OTA_HotelAvailNotifRQ | Google Hotel Prices | undated, live 2026 | https://developers.google.com/hotels/hotel-prices/xml-reference/ari-avail |
| Pricing delivery modes | Google Hotel Ads | 2025 | https://developers.google.com/hotels/hotel-ads/dev-guide/delivery-mode |
| Migrate from pull or changed pricing to ARI | Google Hotel Center Help | 2025 | https://support.google.com/hotelprices/answer/10864209 |
| Availability and Rates API: introduction | Expedia Group | 2025 | https://developers.expediagroup.com/supply/lodging/docs/avail_and_rate_apis/avail_rates/getting_started/introduction |
| OpenTravel Alliance home | OpenTravel Alliance | undated, live 2026 | https://opentravel.org/ |
| Open Travel Alliance (OTA) implementation notes | Tourisoft | 2024 | https://tourisoft.atlassian.net/wiki/spaces/HOT/pages/6520882/Open+Travel+Alliance+OTA |
| AlpineBits HotelData | AlpineBits Alliance | undated (release 2024-10) | https://www.alpinebits.org/hotel-data/ |
| Hotel Technical Specifications: HTNG and OpenTravel | AltexSoft | 2020 | https://www.altexsoft.com/blog/hotel-tech-specifications-htng-opentravel/ |
| HTNG Product Distribution Reservations v3.1 (2014B) | HTNG | 2014 | https://confluence.protel.net/download/attachments/84213852/HTNG_Product_Distribution_Reservations_v3.1_2014B_Technical_Specification.pdf?api=v2 |
| Hotel Technology Next Generation | Wikipedia | undated, live 2026 | https://en.wikipedia.org/wiki/Hotel_Technology_Next_Generation |
| HFTP Board of Directors Rejects AHLA Unsolicited Merger Offer | Hospitality Net | 2022 | https://www.hospitalitynet.org/news/4110267.html |
| HFTP and HTNG sign partnership agreement | Hotel Management | 2018 | https://www.hotelmanagement.net/tech/hftp-and-htng-sign-partnership-agreement |
| Release 21.4 — November 2021 | Oracle Hospitality Integration Platform | 2021 | https://docs.oracle.com/en/industries/hospitality/integration-platform/axern/c_release_21_4.htm |
| OHIP FAQs | Oracle | undated, live 2026 | https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/c_faqs.htm |
| Mews Channel Manager API | Mews | undated, live 2026 | https://docs.mews.com/channel-manager-api |
| Ways to communicate (Connector API events) | Mews | undated, live 2026 | https://docs.mews.com/connector-api/events/communicate |
| apaleo developer documentation | apaleo | 2025 | https://apaleo.dev/ |
| SiteMinder FY26 earnings release (ASX) | SiteMinder | 2026 | https://www.siteminder.com/wp-content/uploads/2026/08/Earnings-Release-SiteMinder-FY26.pdf |
| SiteMinder FY25 earnings release | SiteMinder | 2025 | https://www.siteminder.com/wp-content/uploads/2025/08/sm-fy25-earnings-release-v2.pdf |
| SiteConnect: Availability and Restrictions | SiteMinder | undated, live 2026 | https://developer.siteminder.com/siteminder-apis/channels/introduction/siteconnect/api-reference/availability-and-restrictions |
| RateGain integrates with Cloudbeds | Cloudbeds | 2025 | https://www.cloudbeds.com/articles/rategain-partnership/ |
| Sabre closes hospitality business sale | PhocusWire | 2025 | https://www.phocuswire.com/sabre-closes-hospitality-business-sale |
| OYO UK joins Sabre's reservation system | Hospitality Technology | 2019 | https://hospitalitytech.com/oyo-uk-joins-sabres-reservation-system |
| Pegasus Solutions, Inc. | Encyclopedia.com (International Directory of Company Histories) | c. 2004 | https://encyclopedia.com/books/politics-and-business-magazines/pegasus-solutions-inc |
| Pegasus introduces Enhanced Shopping Transaction | Travel Agent Central | c. 2010s | https://www.travelagentcentral.com/hotels/pegasus-introduces-enhanced-shopping-transaction |
| Sync your Airbnb calendar to other websites | Airbnb Help Centre | undated, live 2026 | https://www.airbnb.com/help/article/99 |
| What are my choices to sync listings through software? | Airbnb Help Centre | undated, live 2026 | https://www.airbnb.com/help/article/2348/what-are-the-ways-i-can-sync-listings-through-my-api-connected-software |
| Why are rates and availability displaying incorrectly ... software-connected host? | Airbnb Help Centre | undated, live 2026 | https://www.airbnb.com/help/article/2965 |
| Hostaway named 2025 Airbnb Preferred+ Software Partner | Hostaway | 2025 | https://www.hostaway.com/blog/airbnb-preferred-software-partner-2025/ |
| Airbnb iCal | Beds24 wiki | undated, live 2026 | https://wiki.beds24.com/index.php/Airbnb_iCal |
| AirBnB.com (API vs iCal) | Beds24 wiki | 2024 | https://wiki.beds24.com/index.php/AirBnB.com |
| Airbnb iCal announcement, December 2019 | Cloudbeds / myallocator | 2019 | https://myallocator.cloudbeds.com/hc/en-us/articles/360038298514-Airbnb-iCal-Announcement-and-Next-Steps-December-2019 |
| Vrbo connectivity solutions | Expedia Group | undated, live 2026 | https://partner.expediagroup.com/en-au/industries/vacation-rentals/vrbo-connectivity-solutions |
| Vrbo: connect via iCal | Hostaway support | 2024 | https://support.hostaway.com/hc/en-us/articles/360002562114-Vrbo-Connect-via-iCal |
| Why is my Vrbo calendar not up to date | Smoobu support | 2024 | https://support.smoobu.com/hc/en-us/articles/360007320340-Why-is-my-Vrbo-calendar-not-up-to-date |
| Check for and disconnect an imported iCal from Booking.com | Hospitable | 2024 | https://help.hospitable.com/en/articles/8709568-check-for-and-disconnect-an-imported-ical-from-booking-com |
| iCal synchronization | Bookingmood | 2025 | https://www.bookingmood.com/hr-HR/docs/synchronization/ical |
| iCAL calendar import issue from Booking.com | Airbnb Community | c. 2020 | https://community.withairbnb.com/t5/Help-with-your-business/iCAL-Calendar-Import-Issue-from-Booking-com/m-p/360608 |
| Channel manager guide | Guesty | 2026 | https://www.guesty.com/channel-manager-guide/ |
| Booking API workflow | Hotelbeds | undated, live 2026 | https://developer.hotelbeds.com/documentation/hotels/booking-api/workflow/ |
| HBX Group IPO on Spanish stock exchanges | PhocusWire | 2025 | https://www.phocuswire.com/hbx-group-ipo-spanish-stock-exchanges |
| Web Travel share price soars on FY25 result | Rask Media | 2025 | https://www.raskmedia.com.au/2025/05/28/web-travel-asxweb-share-price-soars-12-on-strong-fy25-result/ |
| WebBeds 1H26 / FY26 news | Web Travel Group | 2026 | https://www.webtravelgroup.com/news/1h26/ |
| Amadeus Hotels: aggregator content (sales sheet) | Amadeus | undated, live 2026 | https://amadeus.com/documents/en/hospitality/sales-sheet/amadeus-hotels-aggregator-content.pdf |
| Sabre to integrate multisource hotel content into GDS | PhocusWire | 2017 | https://www.phocuswire.com/Sabre-Corp-to-integrate-multisource-hotel-content-into-GDS |
| How does hotel mapping work? | Gimmonix | 2026 | https://gimmonix.com/news/how-does-hotel-mapping-work |
| Room mapping: the process explained | Gimmonix | 2026 | https://gimmonix.com/news/room-mapping-the-process-explained |
| Mapping.Works | Gimmonix | 2026 | https://gimmonix.com/mapping-works/ |
| Hotel mapping: how Vervotech solves it | Vervotech | 2026 | https://www.vervotech.com/hub/hotel-mapping/ |
| e-GDS Booking.com Premier Partner 2023 | e-GDS | 2023 | https://www.e-gds.com/en/News/e-GDS-Booking-Premier-Partner-2023 |
| HotelRunner named Booking.com Premier Connectivity Partner (10th time) | HotelRunner | 2026 | https://hotelrunner.com/en/news/corporate/hotelrunner-named-bookingcoms-premier-connectivity-partner-for-an-impressive-10th-time/ |
| Is metasearch to blame for hospitality's 5-digit look-to-book? | Hospitality Net / J. Boffey (Triometric) | 2016 | https://www.hospitalitynet.org/opinion/4074433.html |
| Reconsider GDS/OTA connections (hotels) | PhocusWire | c. 2017 | https://www.phocuswire.com/Reconsider-GDS-OTA-connections-hotels |
| Look-to-book special report | Hotel Online | 2004 | https://www.hotel-online.com/News/PR2004_4th/Oct04_LooktoBook.html |
