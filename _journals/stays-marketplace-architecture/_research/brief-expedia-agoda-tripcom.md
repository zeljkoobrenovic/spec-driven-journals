# Research brief: Expedia Group (with Vrbo and Hotels.com), Agoda, Trip.com and other OTAs as documented cases

Prepared 21 October 2026 for chapter writers of *BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces*. The brief is vendor-neutral. Expedia Group and Agoda get the most space because they have published unusually detailed, dated primary material: SEC filings, public partner API documentation and engineering blog posts. That is not an endorsement of their choices. Trip.com is covered from its SEC annual report only.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (21 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date (for SEC filings, the filing date), not the fetch date. Where a Medium post or a moved documentation page could only be read through an Internet Archive copy, the claim still cites the original URL and says "(read via archived copy)".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, conference news, search-index excerpt of a page that could not be opened), not from the company's own technical documentation as read in this session.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every architectural statement about a proprietary system the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** OTA platforms are rebuilt continually. Expedia re-platformed Hotels.com (2022) and Vrbo (2023) onto one front end, and Agoda replaced a 72-shard SQL Server price cache with DragonflyDB in 2025–26. Each section gives the date of its evidence. A source older than about three years (for example the 2021 Expedia/Vrbo quoting-cache post or the 2020 Agoda PriceAggregator paper) carries an explicit ⏳ **age warning**: it may describe a replaced system. Do not describe a dated post in the present tense without checking.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: product names, API availability for new partners, property counts, ownership and loyalty-programme rollouts.

**Research limitation.** The session's shared web-search quota ran out about two thirds of the way through this brief. After that point the research relied on direct fetches of known URLs, SEC EDGAR, arXiv and pages found earlier. As a result:

- **Vrbo's supply-side connectivity** (the APIs used by property managers and software providers to push listings, rates and calendars into Vrbo, and Vrbo's iCal import/export rules) is **not verified**. Expedia's "Integration Central" product page returned only a one-line description. The Vrbo side of this brief is therefore drawn from the *distribution* side (Rapid's Vrbo documentation), from the 10-K, and from one PMS API (Hostaway).
- **Expedia's older Medium posts** on lodging candidate generation ("Choosing the Right Candidates for Lodging Ranking") and Kafka Streams cache colocation returned HTTP 403 and had no archived copy; they appear only via search-index excerpts and are tagged WIDELY REPORTED.
- **Agoda's use of ClickHouse** (named in the commission) could **not be confirmed** from any primary source in this session. Agoda's "How Agoda Transitioned to Private Cloud" post also returned 403.
- **Trip.com** has no English-language engineering blog reachable in this session; only its Form 20-F was read.
- **HomeToGo and Holidu** engineering blogs returned 403 or did not resolve; nothing about them is verified here.
- The Expedia Group connectivity documentation moved during 2026 from `developers.expediagroup.com/supply/lodging/docs/...` to a JavaScript-rendered portal (`connectivityportal.expediagroup.com`) that could not be read directly. The Availability and Rates and Booking Notification pages were read via archived copies dated December 2025.

---

## PART 1: Expedia Group — the business shape that drives the architecture

### 1.1 Segments, brands and scale

- Expedia Group reports three segments: **B2C**, **B2B** and **trivago** [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm, published 2026-02-13].
- B2C brands: Brand Expedia ("full-service online travel"), Hotels.com ("focuses on lodging accommodations"), Vrbo ("an online marketplace for alternative accommodations"), plus Orbitz, Travelocity, ebookers and Wotif. "We put the majority of our marketing efforts towards our three core consumer brands: Expedia, Hotels.com, and Vrbo" [VERIFIED: same 10-K, published 2026-02-13].
- B2B "fuels a wide range of travel and non-travel companies including airlines, offline travel agents, online retailers, corporate travel management and financial institutions." Partners connect "through our API, Rapid", white-label or co-branded templates, or the agent tool TAAP [VERIFIED: same 10-K, published 2026-02-13].
- trivago is a majority-owned hotel **metasearch** business earning advertising revenue from referrals [VERIFIED: same 10-K, published 2026-02-13].
- ⚠ Supply at end-2025: "approximately 3.6 million lodging properties available, including approximately 2.4 million online bookable alternative accommodations through Vrbo, approximately 1.2 million hotels and alternative accommodations through our other brands" [VERIFIED: same 10-K, published 2026-02-13]. For comparison, end-2023: "over 3 million", "over 2 million" Vrbo and "over 940,000" other [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442424000007/expe-20231231.htm, published 2024-02-09].
- 2025 gross bookings: **$119.6bn** total; **B2C $83.9bn (+3%)**, **B2B $35.7bn (+20%)**. Revenue: B2C $9.47bn, B2B $4.84bn (+18%). B2B gross bookings grew 21% in 2024 and 20% in 2025, while B2C grew 2–3% [VERIFIED: 10-K FY2025, published 2026-02-13].
- Lodging was **80%** of 2025 worldwide revenue; booked room nights grew 8% in 2025 [VERIFIED: 10-K FY2025, published 2026-02-13].
- ~16,000 employees at end-2025, "approximately one half of our people work in technology roles" [VERIFIED: 10-K FY2025, published 2026-02-13].

[ASSUMPTION/JUDGEMENT] The B2B growth figures matter architecturally: the fastest-growing part of Expedia is not its consumer sites but **selling its supply through APIs to other sellers**. That puts the shopping/availability path under traffic it does not control (partners' search traffic), which explains the traffic-versus-revenue rate limiting in Section 3.4.

**OTA vs hosted stays.** Expedia is the clearest case of both marketplace types under one roof: hotels flow through Expedia/Hotels.com and B2B; whole-home rentals flow mainly through Vrbo (2.4 of 3.6 million properties). The unit count is dominated by hosted stays, while lodging revenue growth is described as "primarily driven by... our hotel business" [VERIFIED: 10-K FY2025, published 2026-02-13]. Listing count and revenue concentration point in different directions; chapter writers should not use property counts as a proxy for business weight.

### 1.2 Merchant, agency and advertising models

- **Merchant model**: Expedia "is the merchant of record"; it contracts for "rates and availability information for rooms but for which we have no control over the rooms and do not bear inventory risk." Travelers "pay us for merchant hotel transactions prior to departing on their trip, generally when they book" [VERIFIED: 10-K FY2025, published 2026-02-13].
- **Agency model**: Expedia "act[s] as the agent in the transaction, passing reservations booked by the traveler to the relevant travel provider" and earns commissions. Hotel agency revenue is recorded "when the stayed night occurs"; "the majority of our agency gross bookings relate to air bookings" [VERIFIED: 10-K FY2025, published 2026-02-13].
- 2025 revenue split: **merchant 70%, agency 22%, advertising/media/other 8%** of $14.7bn [VERIFIED: 10-K FY2025, published 2026-02-13].
- **Expedia Traveler Preference (ETP)** lets participating hotels offer the traveler "the choice of whether to pay Expedia Group in advance under our merchant model (Expedia Collect) or pay at the hotel at the time of the stay under the agency model (Hotel Collect)" [VERIFIED: 10-K FY2025, published 2026-02-13].
- Packages are sold primarily under the merchant model because it "enables us to make certain multi-product purchases available at prices lower than those charged on an individual component basis" [VERIFIED: 10-K FY2025, published 2026-02-13].

[ASSUMPTION/JUDGEMENT] ETP means one hotel room can be sold under two payment flows with different money movement, cancellation exposure and revenue-recognition timing. The booking record, the payment service and the supplier notification must all carry the collect model as a first-class attribute. The Booking Notification API confirms that the supplier receives a **virtual card** for Expedia Collect reservations (Section 2.2).

**OTA vs hosted stays.** For Vrbo inventory sold through Rapid, "All bookings are pre-paid" and payment is collected by the platform, not the property (Section 3.6). The hotel-style "pay at the property" option has no direct equivalent in the documented Vrbo distribution flow. Instead the hosted-stays complications are **payment schedules** and **refundable damage deposits**.

### 1.3 The multi-year platform consolidation

- In 2020 Expedia "shifted to a platform operating model" and unified marketing technology across brands [VERIFIED: 10-K FY2025, published 2026-02-13]. The FY2023 10-K says that "During 2020, Expedia Group unified its technology, product, data engineering, and data science teams" [VERIFIED: 10-K FY2023, published 2024-02-09].
- Sequence of the brand migrations, as Expedia itself described it year by year:
  - FY2022 10-K: "In 2021, we began migrating our core Retail brands (Brand Expedia, Hotels.com and Vrbo) onto one unified technology front-end infrastructure... In 2022, we completed the migration of the Hotels.com front-end technology stack on to the Brand Expedia platform... In late 2022, we began the technology migration of our Vrbo business onto the Brand Expedia front-end" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442423000007/expe-20221231.htm, published 2023-02-10].
  - FY2023 10-K: "we migrated both the Hotels.com and Vrbo front-end stacks onto the Brand Expedia stack and created one unified front-end stack in 2023, which increases our test-and-learn capacity and feature release velocity" [VERIFIED: 10-K FY2023, published 2024-02-09].
- **Precision note for writers:** the filings consistently say **front-end** stack. They do not say that Vrbo's or Hotels.com's back-end inventory, pricing or supply systems were merged. The FY2025 10-K states more broadly that "All of our transaction-based businesses now benefit from our shared platform infrastructure, including customer servicing and support, data centers, search capabilities, payment processing, and fraud operations" [VERIFIED: 10-K FY2025, published 2026-02-13]. Do not claim "one back end" beyond these words.
- ⚠ **One Key**: a unified loyalty programme across Brand Expedia, Hotels.com and Vrbo, launched in the US in 2023, the UK in 2024, and further Brand Expedia markets in 2025, "with the majority of Expedia Rewards members now migrated" [VERIFIED: 10-K FY2025, published 2026-02-13].
- **Re-platforming cost, in Expedia's own words:** "Vrbo's recovery following the recent re-platforming has been slower than anticipated, which has put pressure on gross bookings" (CEO Peter Kern, Q1 2024 results), and full-year guidance was lowered [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442424000024/earningsrelease-q12024.htm, published 2024-05-02].
- Cloud: FY2022 and FY2023 10-Ks describe "a multi-year effort to migrate products, data storage and processing... to new technology platforms and significantly increase our utilization of public cloud computing services, such as Amazon Web Services" and say Expedia was "nearing the end" of that project [VERIFIED: 10-K FY2023, published 2024-02-09]. By FY2025: "our websites and apps are powered primarily through cloud platforms and, to a lesser extent, legacy company-owned data centers" [VERIFIED: 10-K FY2025, published 2026-02-13].
- The FY2025 10-K states the platform direction: "developing configurable technical capabilities that support various travel products while using simpler, standard architecture and common applications and frameworks" [VERIFIED: 10-K FY2025, published 2026-02-13].

[ASSUMPTION/JUDGEMENT] Expedia's case gives the book a rare, primary-sourced example of **the hidden cost of merging a hosted-stays brand into an OTA front end**. Hotels.com, a hotel brand, migrated in 2022 without a public warning. Vrbo, a hosted-stays brand, followed in 2023 and was named as the cause of a guidance cut. The filings do not explain why. Plausible reasons, none verified, include different search semantics (whole-home, date-flexible, group-size-driven search), different listing content, host-facing flows and SEO landing pages. Present this as an inference, not as Expedia's explanation.

**OTA vs hosted stays.** The consolidation shows the two marketplace types can share a **traveler-facing front end, loyalty and payments**. The evidence does not show that they share **supply and inventory models**. Rapid's documentation (Section 3.6) still treats Vrbo inventory as a distinct product with different rules.

---

## PART 2: Expedia supply connectivity — how hotels get rates and inventory in

### 2.1 Who may connect

- ⚠ Expedia's lodging supply hub addresses "property management systems, channel managers, and central reservation systems" and states: "At this time we're not accepting direct connections from individual properties" [VERIFIED: https://developers.expediagroup.com/supply/lodging, fetched 2026-10-21, undated page].
- The hub's current tutorials are for **GraphQL** APIs: property status, reservation retrieval, reservation update, compliance (regulatory information for integrated properties) and messaging [VERIFIED: https://developers.expediagroup.com/supply/lodging, undated page].
- The documentation index (December 2025 copy) groups the supply APIs as: **Availability and rates** (Availability and Rates, Promotions); **Booking** (Booking Notification, Booking Retrieval and Booking Confirmation, Reservation management); **Property management** (Deposit, Image, Product, Property, Compliance, Messaging, Notifications/webhooks, Product management, Property status, Reviews) [VERIFIED: https://developers.expediagroup.com/supply/lodging/docs/avail_and_rate_apis/avail_rates/getting_started/introduction, page © 2025 (read via archived copy dated 2025-12-20)].
- The 10-K describes the same ecosystem in business terms: "direct connect" technology lets suppliers "upload information about available products and services and rates directly from their central reservation systems", either through Expedia's own tools or "through third-party channel managers" [VERIFIED: 10-K FY2025, published 2026-02-13].

### 2.2 Availability and Rates (AR) and booking delivery

The Availability and Rates API is the hotel push channel. Its documented scope:

| Included in AR | Not included in AR (managed elsewhere) |
| --- | --- |
| Update inventory and/or rates per room type and/or rate plan, **by Expedia IDs only** | Property's own internal codes as identifiers |
| Updates by date range and day of week; many products in one message | Inventory count **by rate plan** (inventory is per room type) |
| Open/close room types and rate plans | Content: room names, descriptions, pictures, amenities |
| Min/max length of stay (arrival-based or stay-through) | Deposit and cancellation policies |
| Closed-to-arrival and closed-to-departure | Compensation or promotional discounts |
| Rooms available per room type **up to two years ahead** | Resort fees, cleaning fees and other fees |
| Pricing models: per-day, per-day + LOS, occupancy-based, day-of-arrival | Tax remittance details |
| Rates as **Sell** (gross) or **Net** (sell minus compensation) | |

[VERIFIED: https://developers.expediagroup.com/supply/lodging/docs/avail_and_rate_apis/avail_rates/getting_started/introduction, page © 2025 (read via archived copy dated 2025-12-20)]

- "Availability and Rates API cannot be implemented alone": it must be paired with Booking Notification, Booking Retrieval/Booking Confirmation, or Reservation management [VERIFIED: same page].
- Messages are XML (`AvailRateUpdateRQ` / `AvailRateUpdateRS` with `DateRange` and `RoomType` elements) [VERIFIED: same page, navigation]. The requirement for well-formed XML against an XSD, UTF-8, TLS 1.2 and basic authentication appears in search-index excerpts of the "requirements and best practices" page [WIDELY REPORTED: https://developers.expediagroup.com/supply/lodging/docs/avail_and_rate_apis/avail_rates/getting_started/requirements-best-practices, 2025].
- **Booking Notification** is push from Expedia to the partner's CRS/PMS: "a notification-based API where Expedia Group initiates the notifications", delivering "new, modified or cancelled reservations in near real time" [VERIFIED: https://developers.expediagroup.com/supply/lodging/docs/booking_apis/booking_notification/getting_started/introduction, page © 2025 (read via archived copy dated 2025-12-20)].
- ⚠ "At this time, Booking Notification API is not available for adoption by new or existing partners. This API and its documentation are maintained for existing connections" [VERIFIED: same page]. New integrations use pull-style Booking Retrieval/Confirmation or the GraphQL reservation APIs.
- The key architectural statement: "Expedia Group allows customers to book against the most recent information received from you through Partner Central or Availability and Rates API and **stored locally in Expedia Group's systems**. Reservations sent through Booking Notification API to you have already been confirmed with the traveler" [VERIFIED: same page].
- Consequently: "You cannot reject these reservation notifications. Inventory issues are not an acceptable reason to reject a booking since these are avoidable if you update your inventory regularly" [VERIFIED: same page].
- Delivery semantics: Expedia "is responsible for the sequencing of messages" and "will always wait for a valid response for the previous notification before sending the next one" for the same booking. Failed messages are retried several times, then fall back to **email**; once a booking falls back to email, its later modifications and cancellations also go by email [VERIFIED: same page].
- The reservation carries only room type and rate plan **IDs**, not names; it does not carry pricing model or cancellation policy. It carries the point of sale (Hotels.com, Orbitz, Expedia and so on) and a virtual card for Expedia Collect bookings [VERIFIED: same page].

[ASSUMPTION/JUDGEMENT] Three reference-architecture lessons follow and are worth stating in the book:

1. **The OTA holds a local copy of supplier inventory and sells against it.** The supplier is not asked at booking time. Overbooking risk is pushed onto the supplier contractually ("you cannot reject"). This is the opposite of a pull/live-check model (see Agoda's third-party suppliers in Section 6.3).
2. **Per-booking ordering, not global ordering.** Expedia serialises messages per reservation and blocks on acknowledgement, which is the minimum needed for correct create→modify→cancel sequences.
3. **Graceful degradation to a human channel** (email) is part of the protocol, and it is sticky per booking to avoid split-brain between channels.

**OTA vs hosted stays.** AR's model of **room types × rate plans × dates, with inventory counts per room type** is a hotel model. A one-unit hosted-stays listing has inventory of 0 or 1 per night. Rapid's Vrbo documentation says Vrbo properties return "a single rate plan" and are "single-unit only" (Section 3.6). The hosted-stays calendar is therefore a per-day availability bit with min/max stay and check-in/check-out validity, not an inventory count.

### 2.3 Vrbo supply side (gap)

- The 10-K says Vrbo's listing services give supply partners "tools to help them manage an availability calendar, respond to customer inquiries, edit the content of a property listing" [VERIFIED: 10-K FY2025, published 2026-02-13].
- Expedia's developer hub lists "Integration Central" with the one-line description "Integrate your connectivity product on the Vrbo platform"; the product page itself returned a not-found body [VERIFIED: https://developers.expediagroup.com/docs/products/integration-central, fetched 2026-10-21].
- Vrbo's iCal import/export rules, sync frequency and the Vrbo software-partner API were **not verified** in this session (see Open questions).
- Evidence from a PMS: Hostaway's public API lists predefined reservation channels including `homeaway` (2002), `vrboical` (2010), `homeawayical` (2009), `customIcal` (2015), `airbnbOfficial` (2018), `bookingcom` (2005) and `expedia` (2007) [VERIFIED: https://api.hostaway.com/documentation, changelog entries dated up to 2026-10-05]. This shows that, in at least one widely used PMS, **iCal-based and API-based connections to the same marketplace coexist as separate channels**.

---

## PART 3: Expedia's B2B distribution API — Rapid

### 3.1 The booking flow as documented

Rapid's lodging documentation describes this sequence [VERIFIED: https://developers.expediagroup.com/rapid/lodging, fetched 2026-10-21, undated page]:

1. **Content**: static property content (ID, name, address, star rating and so on). "Property content requires daily refreshes."
2. **Geography**: regions, region hierarchy and properties within them.
3. **Shopping**: "Call the Shopping API with stay dates, occupancy details, and your desired property IDs."
4. **Price check**: confirms the chosen rate and returns a booking link (or a new price, or a link to search again).
5. **Booking**: returns an itinerary ID and links to retrieve, cancel or resume a held booking. "We recommend you store the retrieval link with each traveler's details."
6. **Itinerary retrieval / Manage booking**: change, cancel, receipts, guest name change, notifications.

Rapid also covers Notifications, Vacation rentals, Sponsored Listings, Merchandising, Trip Protection ("Cancel for any reason") and Typeahead [VERIFIED: same page, navigation].

[ASSUMPTION/JUDGEMENT] The flow is a textbook **content → shop → price-check → book → manage** pipeline. Each step trades freshness against cost: content is cached by the partner (daily), shopping is live but rate-limited, price check re-confirms just before payment, and booking is authoritative. It is a useful template for any chapter on availability and pricing freshness.

### 3.2 Content

- Two file-based APIs: a **Property Catalog File** (all active properties, "useful for mapping suppliers") and a **Property Content File** (all property, room and rate content). Incremental updates use `date_added_*` and `date_updated_*` filters, which must never be combined in one request. An **Inactive Property** endpoint returns IDs to remove "from your cache or storage" [VERIFIED: https://developers.expediagroup.com/rapid/lodging/content/about-content-api, fetched 2026-10-21, undated page].

**OTA vs hosted stays.** Vrbo content "changes more often than hotel content", and Expedia recommends refreshing it "at a minimum of a weekly basis", while property content in general needs daily refreshes [VERIFIED: https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-integration-guide, fetched 2026-10-21, undated page]. [ASSUMPTION/JUDGEMENT] Read together, the two pages give the book a concrete number: a distribution partner is expected to re-pull content daily, and Vrbo content is singled out as more volatile.

### 3.3 Shopping and price check

- Shopping returns rates and availability for **up to 250 properties per request**, capped at **8 rooms**. "The Shop API provides the most current information for available rooms and rates." Tokenised links "expire after a short period"; "Do not store link values for long term re-use" [VERIFIED: https://developers.expediagroup.com/rapid/lodging/shopping/about-shopping-api, fetched 2026-10-21, undated page].
- The two-letter `country` parameter sets "the traveler's point of sale"; the response schema is "the same for B2B and B2C", and "Only the launch and compliance requirements differ by audience" [VERIFIED: same page].
- Rate attributes: refundability (`refundable`, `non_refundable`, `partially_refundable`), business rates (`travel_purpose=business`), loyalty-eligible rates, deal rates, non-holdable rates; penalties in `cancel_penalties` [VERIFIED: same page].
- Pricing breakdown includes `property_inclusive` totals, `strikethrough` (pre-discount, tax-exclusive) and `inclusive_strikethrough`. "APIs provide prices based on one room only, multiple room bookings require an additional calculation by yourself." Some mandatory taxes and fees are excluded from the total and must be displayed prominently [VERIFIED: same page].
- Price check "Confirms the price returned by the Shop response"; fees may vary by about 0.1% from the prior shop response [VERIFIED: same page].

### 3.4 Rate limiting as a look-to-book control

- "Expedia Group calculates rate limits monthly, taking into account a partner's traffic vs. revenue", typically over a three-month window for seasonality; new partners get "a very generous allowance for the first 3 months" [VERIFIED: https://developers.expediagroup.com/rapid/lodging/shopping/rate-limiting, fetched 2026-10-21, undated page].
- Load is driven by "the number of hotels, the number of rooms" and length of stay searched. "Exceeding your daily rate limit will not affect your API calls"; per-minute limits still apply, and "Daily rate limits will no longer impact bookings" [VERIFIED: same page].

[ASSUMPTION/JUDGEMENT] "Traffic vs. revenue" is a look-to-book ratio in all but name. The book can cite it as a primary-sourced example of an OTA **pricing its expensive live-availability path by the conversion of the caller**. The same pressure appears from the other side at Agoda (Section 6.3), where suppliers cap Agoda's QPS.

### 3.5 Property Collect through Rapid

- Under Property Collect "the property will charge customers at check-in", but card details are still captured; Rapid or the property may pre-authorise or charge no-show and late-cancellation fees. Integrators handling card data "must be PCI compliant". Properties can cancel "within 72 hours of confirmation". "Rapid will be the merchant of record for property collect bookings only when" SCA applies [VERIFIED: https://developers.expediagroup.com/rapid/lodging/booking/property-collect, fetched 2026-10-21, undated page].
- Two currencies: an onsite payment currency for extras and a **billable currency** "used by the property to charge the card" [VERIFIED: same page].

### 3.6 Vrbo inventory through Rapid — the clearest documented OTA-vs-hosted-stays contrast

| Dimension | Hotel inventory in Rapid | Vrbo inventory in Rapid |
| --- | --- | --- |
| Unit model | Room types, many rate plans | "whole property only, no shared accommodations"; "single-unit only"; "a single rate plan" |
| Room description | Bed groups | Unit configuration (bed groups "don't apply") |
| Payment | Expedia Collect or Property Collect | "All bookings are pre-paid"; payment schedules and damage deposits are opt-in "advanced" options |
| Damage deposit | n/a | Properties with refundable damage deposits must be excluded from shop requests unless enabled |
| House rules | Policies | `enhanced_house_rules` (pets, parties, children, smoking) |
| Rental agreement | n/a | "must be displayed on any check-out page"; guest may need to sign |
| Host contact | Property message centre | Contact details only after booking; "Special requests are currently not relayed to the property" |
| Booking window | Same-day allowed | "Same day bookings are not supported"; windows under 72 hours not allowed |
| Changes | Hard change, name change, hold/resume | No hold/resume; no change to guest name, dates, occupancy or pets |
| Content refresh | Daily | At least weekly; changes more often than hotel content |
| Availability calendar | Shopping only | Separate `/calendars/availability`: per-day `available`, `min_stay`, `max_stay`, check-in/out validity codes; up to 3 years ahead; "Caching is not supported at this time" |

Sources: [VERIFIED: https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-integration-guide, fetched 2026-10-21, undated page]; [VERIFIED: https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-availability-calendar, fetched 2026-10-21, undated page]; [VERIFIED: https://developers.expediagroup.com/rapid/lodging/vacation-rentals/about-vacation-rentals-api, fetched 2026-10-21, undated page].

Further detail:

- ⚠ "Vrbo inventory is a new product that is currently only available to a limited number of partners", giving access to "650k+ Vrbo properties via the same Rapid API used for access to our hotels and vacation rentals today"; the page also lists "265k+ integrated with Expedia Group" vacation rentals and "900,000+" in total [VERIFIED: about-vacation-rentals-api page, undated]. The page is undated, and its figures do not reconcile with the 10-K's 2.4 million Vrbo listings. ⚠ Treat them as "the subset of Vrbo inventory distributable via Rapid at an unknown date", not as Vrbo's size.
- Enabling payment schedules adds "+15-25% more available properties"; enabling damage deposits adds "+2% more, often higher-end" properties [VERIFIED: same page].
- The availability calendar returns "only an indication as to whether the property is bookable or not", with no daily rates, and "availability more than one year out may be less accurate"; partners should call it "on page load when the UI calendar view is displayed" [VERIFIED: vrbo-availability-calendar page, undated].
- Hosts need lead time: same-day and sub-72-hour bookings are excluded "because hosts need time to process bookings and prepare the property" [VERIFIED: vrbo-integration-guide page, undated].

[ASSUMPTION/JUDGEMENT] This table is the single best primary-sourced artefact in this brief for the book's comparison chapters. The hosted-stays product needs a **calendar-first** search UI with per-day check-in/check-out validity (because min-stay and changeover-day rules make some dates valid only as arrivals or only as departures). It needs **payment schedules and deposits** as first-class payment concepts, and **host lead time** as a booking constraint. A hotel-shaped shopping API cannot express any of these.

---

## PART 4: Expedia lodging search, ranking and ML

### 4.1 The ranking pipeline

- Expedia describes lodging ranking as a stage that "arrives after the candidate generator selects a subset of properties to rank and before the final business adjustments are applied" [VERIFIED: https://medium.com/expedia-group-tech/learning-to-rank-at-expedia-group-how-to-adapt-the-property-search-result-page-based-on-f4ebef78c94b, published 2024-07-23 (read via archived copy)].
- Training data: "converted search logs (searches which led to a booking)" with displayed properties; relevance labels follow "booking > click > impression" [VERIFIED: same post].
- Features: search context (destination, check-in/check-out, rooms, adults, children, **point of sale**, device, personalisation features) and property features (price, guest review, star rating, amenities), including a Word2vec-inspired property embedding. The model is "a deep neural network" for learning to rank over very sparse categorical features [VERIFIED: same post].
- **Property search vs destination search**: when a traveler arrives from an external channel (an affiliate or social link to one hotel), Expedia shows a results page with that property "pinned" on top and ranks alternatives by a blend of relevance and **similarity to the searched property**. Same architecture and loss, different training data and added similarity features; a fully similarity-based model underperformed [VERIFIED: same post].
- A search-index excerpt of the (unreadable) candidate-generation post says the availability and pricing step "identifies room-type availability and corresponding prices, including discounts, for each property", that "extensive caching is already implemented" but is not sufficient given the "large number of pricing combinations", and that context-dependent ranking "cannot be efficiently pre-computed and cached" [WIDELY REPORTED: https://medium.com/expedia-group-tech/choosing-the-right-candidates-for-lodging-ranking-d0841bf40c0e, date not confirmed].

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] The "property search" pattern (a traveler wants one specific property, it is unavailable, so the system recommends close substitutes) is much sharper in hosted stays, where every listing is unique and is often sold out for the exact dates. Expedia's posts describe it for hotels; whether Vrbo uses the same model is not stated.

### 4.2 Multi-stakeholder ranking: the Juggler model

- Final rank = **relevance score + weighted business adjustments**. "Since this is proprietary information, we do not provide details regarding each adjustment." Weights are predicted per search ("linear scalarization") by a meta-learning model called **Juggler** [VERIFIED: https://medium.com/expedia-group-tech/the-juggler-model-balancing-expectations-in-lodging-rankings-6d09b9b8e341, published 2023-09-19 (read via archived copy)].
- The stakeholders are named explicitly: travelers (best property, lowest price), properties ("best exposure while paying the lowest fees"; Expedia provides "mechanisms to improve their rankings in exchange for fees or special deals") and the marketplace (profitable inventory, short-term conversion versus long-term repeat rate) [VERIFIED: same post].
- Adjustments must be "easy to interpret and explain to stakeholders", for example so Expedia can explain to property managers "why a specific property is assigned a given ranking" [VERIFIED: same post].
- Follow-up research, **Juggler-MAB**, adds a multi-armed bandit for per-segment (device, brand) weight refinement; evaluated in simulation on "0.6 million searches from Expedia's lodging booking platform", reporting +2.9% NDCG and 13.7% lower regret versus Juggler [VERIFIED: https://arxiv.org/abs/2409.08752, published 2024-09-13].

### 4.3 Retrieval and embeddings

- Expedia published a tutorial-style post on a **two-tower** retrieval model (query encoder + item encoder, in-batch sampled softmax with logQ correction, ANN indexing of item vectors), framed within the standard two-stage retrieve-then-rank pattern [VERIFIED: https://medium.com/expedia-group-tech/candidate-generation-using-a-two-tower-approach-with-expedia-group-traveler-data-ca6a0dcab83e, published 2023-12-12 (read via archived copy)]. The post is a worked example on Expedia data; it does not state that this model is in production for lodging search. Do not present it as the production candidate generator.

### 4.4 Serving the ranker: Keras 3, Kamae, ONNX/TensorRT and Triton (2026)

- The lodging ranking service "handles users' search requests and returns a personalised property ranking on top of a lightweight candidate generator" and "is frequently retrained" [VERIFIED: https://medium.com/expedia-group-tech/how-keras-3-helped-modernise-expedia-groups-lodging-ranking-stack-7fec96f052fd, published 2026-08-11].
- Feature preprocessing is done by **Kamae**, Expedia's open-source library that maps Spark preprocessing to Keras/TensorFlow layers so the same transformations run in training and serving [VERIFIED: same post; https://arxiv.org/abs/2507.06021, published 2025-07-08].
- The old design fused string-heavy preprocessing and the network into one TensorFlow graph. The 2026 design splits it: preprocessing stays in TensorFlow, the purely numeric network is exported to **ONNX** and **TensorRT** (FP16), and both are ensembled at serving time on **Triton Inference Server** [VERIFIED: Keras 3 post, published 2026-08-11].
- Reported results: training 30% faster with JIT/XLA; dataset staging 75% faster; some models' training "down from a working week to a day" with multi-GPU; P99 inference latency cut by about two thirds ("our prior P50 is now our P99"); FP16 ranking order kept above 99% rank-biased overlap with the full-precision baseline [VERIFIED: same post].

### 4.5 ML governance (2026)

- ⚠ Expedia's ML principles require "both offline and online evaluation" before broad deployment, "Build on shared foundations; specialize only when justified", "Minimize and sunset manual business rules", four named owners per model (business, product, AI, operational), and risk-proportional governance: "A customer-facing model that affects pricing or availability for millions of travelers demands a far higher bar than an internal tool". It mentions "Agentic Release tollgates" and "algorithm score cards" for marketplace algorithms [VERIFIED: https://medium.com/expedia-group-tech/how-expedia-group-builds-ai-that-lasts-at-scale-434677770fe9, published 2026-07-14].

---

## PART 5: Expedia data, streaming and caching

### 5.1 A quoting cache for unit-level pricing (⏳ 2021)

⏳ **Age warning**: published March 2021 about a system as it was at the end of 2019. It may describe a replaced system.

- "At the end 2019, we used Kafka to prime our quoting cache and to keep it in sync with our pricing pipeline... This system was responsible for all prices shown on our website." The pricing cluster ran **Apache Ignite**; quote requests for multiple **units** were parallelised, each node quoting the units it cached [VERIFIED: https://medium.com/expedia-group-tech/mongo-change-streams-in-production-97a07c7c0420, published 2021-03-02 (read via archived copy)].
- Priming from a compacted Kafka topic made start-up slow ("nearly an hour in production"). The team moved to **MongoDB change streams** filtered by a partition number (0–1023) aligned with Ignite's partition ranges, with replay from "5 minutes before the previous subscriber died" after failures. Production priming fell "from 120–150 minutes to less than 10 minutes" across 18 machines per cluster [VERIFIED: same post].

[ASSUMPTION/JUDGEMENT] The word "units" and the per-unit quoting design suggest a Vrbo/HomeAway-lineage pricing system (hosted-stays systems quote a whole stay per unit, including fees and LOS rules). The post does not name the brand. If a chapter uses it, say "an Expedia Group pricing team" and keep the inference explicit.

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] Hotel pricing at OTA scale is dominated by **many rate plans × occupancies × dates per property**. Hosted-stays pricing is dominated by **stay-level quotes per unit**: nightly rates plus cleaning fees, LOS discounts and deposits, computed for an exact date range. A partitioned in-memory **quote engine** over a unit-sharded cache fits the second case well.

### 5.2 Reviews as an event-sourced pipeline (2023)

- Moderated reviews are written to a Kafka topic that "acts as the source of truth for all moderated reviews"; independent consumers build aggregation, an in-memory cache behind APIs, an Elasticsearch index and sentiment analysis [VERIFIED: https://medium.com/expedia-group-tech/how-expedia-reviews-engineering-is-using-event-streams-as-a-source-of-truth-d3df616cccd8, published 2023-04-25 (read via archived copy)].

### 5.3 Kafka Streams cache colocation

- A search-index excerpt describes a team using a Kafka Streams state store attached to two input topics so that identical keys landed on the same task, giving "one API call per unique key" [WIDELY REPORTED: https://medium.com/expedia-group-tech/colocating-input-partitions-with-kafka-streams-when-consuming-multiple-topics-sub-topology-matters-f92da955c905, date not confirmed]. The domain (lodging or not) is not confirmed.

---

## PART 6: Agoda

### 6.1 Ownership and positioning

- Agoda is one of Booking Holdings' five primary consumer-facing brands (Booking.com, Priceline, Agoda, KAYAK, OpenTable). "Agoda is a leading online accommodation reservation service catering primarily to consumers in the Asia-Pacific region, with headquarters in Singapore. Agoda also offers flight, ground transportation, and attractions" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18].
- Booking Holdings reports merchant gross bookings growth "due primarily to growth in accommodation reservation services and flight reservation services at Booking.com and Agoda" [VERIFIED: same 10-K]. Agoda's own volumes are not broken out.
- Booking Holdings acquired Agoda in 2007 [ASSUMPTION/JUDGEMENT: widely known; not re-verified in this session].
- Agoda says it "began its journey in 2005 as a pioneer in online hotel bookings" [VERIFIED: https://medium.com/agoda-engineering/how-agodas-multi-product-booking-engine-powers-seamless-travel-bookings-61fc6e746821, published 2025-11 (read via archived copy)].
- Agoda serves **white-label partners** from one design system using design tokens and per-partner themes: "New partner = new theme, not new code" [VERIFIED: https://medium.com/agoda-engineering/how-agoda-powers-multiple-travel-brands-with-one-design-system-a48de5f906af, published 2026-05-13].

[ASSUMPTION/JUDGEMENT] Agoda and Booking.com are sister companies, but their engineering blogs describe separate stacks (Agoda's on-premise data centres versus Booking.com's own estate). Do not assume shared systems.

### 6.2 Infrastructure: on-premise by choice

- "We operate our own infrastructure across four data centers in Asia, Europe, and the US." "At our current size, running in-house remains more cost-effective and gives us greater control." For portability Agoda "moved from HDFS to a proprietary S3 provider that is protocol-compliant" (CTO Idan Zalzberg) [VERIFIED: https://medium.com/agoda-engineering/agodas-cto-on-why-managers-should-code-running-on-prem-and-adopting-generative-ai-b1b4c5c7028b, published 2025-05-14 (read via archived copy)].
- Agoda runs a Kubernetes-based "private cloud" in which hardware generations vary per application, which affects consumer processing rates [VERIFIED: https://medium.com/agoda-engineering/how-we-solve-load-balancing-challenges-in-apache-kafka-8cd88fdad02b, published 2024-05-16 (read via archived copy)].
- Agoda built **Storefront**, a Rust reverse proxy on Cloudflare's Pingora, in front of S3-compatible object storage (VAST Data) to replace DNS round-robin, which clumped traffic because clients cached DNS [WIDELY REPORTED: https://www.infoq.com/news/2026/03/agoda-rust-reverse-proxy/, 2026].

**OTA vs hosted stays.** Not a type difference. [ASSUMPTION/JUDGEMENT] It is a useful counter-example to "everyone runs on public cloud": Agoda and (per its 10-Ks) Expedia made opposite hosting choices at similar scale.

### 6.3 Getting prices from suppliers: push, pull and QPS budgets

⏳ **Age warning** for the first bullet: the paper is from 2020.

- **PriceAggregator (2020)**: Agoda "aggregates non-direct suppliers' hotel rooms". "Each supplier only allows Agoda to fetch for the hotel price with a limited amount of Queries Per Second (QPS)", which "is never enough to cover all user searches. Inevitably, many user searches have to be ignored. Hence, booking lost." PriceAggregator "intelligently determines when, how and what to send to the suppliers to fetch for price", and online A/B tests showed it "increases Agoda's bookings significantly" [VERIFIED: https://arxiv.org/abs/2008.02087, published 2020-06-30].
- Search-index excerpts of Agoda's two blog posts on the same system describe a cache that stores supplier prices until they expire, a service that proactively fetches prices "on a constant QPS", and "SmartTTL", which estimates how long a price stays valid [WIDELY REPORTED: https://medium.com/agoda-engineering/priceaggregator-an-intelligent-system-for-hotel-price-fetching-part-1-ba6ce66354c2 and https://medium.com/agoda-engineering/priceaggregator-an-intelligent-system-for-hotel-price-fetching-part-2-f551a10cede, c. 2020].
- **Push-side volumes (2024)**: "a single supplier can provide 1.5M price updates and offer details in just one minute." In a typical supply system, a **distributor** "consumes price updates from 3rd party systems and distributes processing jobs to downstream processor service in multiple data centers", which "eventually" write to databases. Agoda says "any delays or failures in reflecting these updates can lead to incorrect pricing and customer booking failures" [VERIFIED: Kafka load-balancing post, published 2024-05-16 (read via archived copy)].
- The same post explains why naïve Kafka partitioning failed: heterogeneous hardware across the private cloud, and messages with very uneven cost (third-party HTTP calls, variable DB latency) [VERIFIED: same post].

[ASSUMPTION/JUDGEMENT] Agoda documents **both** supply modes the book needs to contrast. **Pull** suppliers (bedbanks and wholesalers queried per itinerary under a QPS cap) force a cache-plus-prefetch design that is economically optimised. **Push** suppliers send update streams that must be fanned out reliably. Expedia's AR (Section 2.2) is the pure push case.

### 6.4 The Price Cache: SQL Server to DragonflyDB (2025–26)

- The **Price Cache** "stores terabytes of volatile rate data fetched from our global network of suppliers". On a hit, search responds immediately; "A cache miss triggers an on-demand workflow that fetches the latest rates" [VERIFIED: https://medium.com/agoda-engineering/how-agoda-scaled-its-price-cache-with-dragonflydb-0828e478e84f, published 2026-08-19].
- Before migration: **72 SQL Server shards** with application-level routing, scaled only in fixed steps (6→12→18 servers) with manual remapping; hardware doubled in early 2024 and was near limits again within a year. Load: **~300,000 reads/s and ~1.5 million writes/s**, P99 under 50 ms, ~1.5 TB in memory [VERIFIED: same post].
- Why DragonflyDB: multi-threaded shared-nothing design, Redis protocol and cluster mode (workload is mostly `MGET`/`SET`), **built-in TTL**, which retired a custom job purging stale supplier data, and existing in-house use for a feature store and microcache [VERIFIED: same post].
- Migration: a "hot data" phase (length of stay 1–4 days) on one 1 TB instance, which hit 900 GB and its eviction threshold within months; then clusters of three shards holding the full ~1.5 TB. Writes ran at ~1.6 million/s with P99 ~10 ms. **Dual reads** checked parity by supplier count and price-data length (>99.9% match). Traffic moved by an **A/B experiment on booking metrics**, then to 100% [VERIFIED: same post].
- Result: P99 read latency improved about 8×, with ~8 ms P99 at ~300,000 reads/s [VERIFIED: same post].
- Resilience: two clusters (A/B). A drained cluster takes about **three hours to re-warm** to its peer's hit ratio. Each pod now compares the clusters' hit ratios every five seconds over a five-minute window and fails over on a statistically significant gap (10-point threshold to mark unreadable, 3-point threshold to recover), with no coordinator; about 40 pods converged within about two minutes in a drill [VERIFIED: same post].

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] The price cache exists because OTA prices come from **many external suppliers per property** and change constantly; the key space is hotel × occupancy × check-in × check-out × supplier. A hosted-stays marketplace usually owns the host's calendar and price rules and can compute a quote on demand. It needs a quote engine (Section 5.1), not a supplier-price cache.

### 6.5 Price Delivery System (2023)

- Agoda's **Price Delivery System (PDS)** "serves hotel room prices for our web, mobile, and affiliate APIs, handling over a million requests per second in four data centers across the globe" [VERIFIED: https://medium.com/agoda-engineering/improving-performance-using-distributed-cache-with-couchbase-aa7ebf3a12c9, published 2023-10-12 (read via archived copy)].
- PDS work splits into "metadata retrieval" and "price calculation". Metadata came from local in-memory LRU caches with a 50% hit ratio; P99 response was 460 ms, of which metadata was 110 ms. **Affiliate traffic** with broad searches drove evictions. Adding a Couchbase distributed cache improved PDS response by 20% [VERIFIED: same post].

[ASSUMPTION/JUDGEMENT] The affiliate detail mirrors Expedia's B2B rate limiting (Section 3.4): **distribution partners' broad searches are the workload that breaks pricing caches**.

### 6.6 Kafka at Agoda

- "At Agoda, we send around **1.8 trillion events per day** through Apache Kafka", with "2x growth YOY on average" since 2015. Kafka also serves as "an asynchronous API, facilitating data replication across our on-premise data centers" and feeds ML pipelines [VERIFIED: https://medium.com/agoda-engineering/how-agoda-manages-1-8-trillion-events-per-day-on-kafka-1d6c3f4a7ad1, published 2023-09-18 (read via archived copy)].
- Design choices: a **two-step logging architecture** (client library writes to disk, a node-level Forwarder ships to Kafka) used only for analytics, at P99 ~10 s end to end, for about 85% of developers; direct producers for sub-second needs. Many smaller **use-case clusters** instead of one per data centre. Audit counts per pipeline stage. **Cost attribution by bytes produced** to the owning team [VERIFIED: same post].
- ⚠ By mid-2025: "Every day, this platform ingests over **3 trillion records**". Cross-data-centre consumption is **active-passive** with offset translation via MirrorMaker 2; stretch clusters were rejected because of the latency between Agoda's distant data centres [VERIFIED: https://medium.com/agoda-engineering/how-agoda-handles-kafka-consumer-failover-across-data-centers-a3edbacef6d0, published 2025-06-25 (read via archived copy)].
- ClickHouse at Agoda: **not verified** (see Open questions).

### 6.7 Booking and post-booking

- **Multi-Product Booking Engine (MPBE)**: a Workflow Orchestrator receives a signal from RabbitMQ and generates a **dynamic graph** of steps (availability confirmation, fraud check, payment and so on), each run by a single-purpose asynchronous **agent**. "Book with ZeroPay" reuses the hotel graph with the payment step skipped by flag [VERIFIED: MPBE post, published 2025-11 (read via archived copy)].
- For carts (for example flight + hotel), per-product graphs are **merged**: itinerary-level steps (pre-authorise and settle card) run once, product-level steps run sequentially or in parallel. A **Risk Profiler** picks the confirmation order by free-cancellation terms: confirm the free-cancellable product first so it can be rolled back without penalty if the other fails [VERIFIED: same post].
- Scale: four regions; 96 Kubernetes pods per region; "over 25 unique booking graphs"; the largest graphs reach "up to 60 nodes" [VERIFIED: same post].
- **Post-booking (BAPI)**: in 2019 Agoda split its core monolith into booking creation and post-booking (cancellations, amendments, refunds, communications), porting the post-booking code "line by line". Merge requests "more than quadrupled between 2022 and 2025" and some files exceeded 4,000 lines. Agoda then introduced a **modular monolith** with domain components (`rebook`, `cancellation`, `payment`), enforced by ArchUnit tests in CI. In Q2 2026, framework-backed MRs completed review 64% faster at the median (the sample was small: 4–21 platform MRs a month) [VERIFIED: https://medium.com/agoda-engineering/how-we-cut-the-coupling-tax-in-a-post-booking-api-2156a3175538, published 2026-10-20].

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] MPBE's Risk Profiler is an OTA problem: it combines products from suppliers with different cancellation terms. In hosted stays, the equivalent risk is **host acceptance** (request-to-book): the booking graph must wait on a human, and Rapid's Vrbo rules (no same-day bookings, 72-hour minimum window) exist for the same reason.

### 6.8 Experimentation

- Agoda uses one-tailed tests with a **p-value threshold of 0.3 to 0.45** rather than 0.05, arguing that a business should maximise the "sum taken actual lift" across many experiments rather than minimise false positives [VERIFIED: https://medium.com/agoda-engineering/why-we-use-lenient-p-value-thresholds-like-0-4-for-a-b-experiments-at-agoda-part-1-e93c7c56e666, published 2023-12-15 (read via archived copy)].
- The DragonflyDB migration was itself rolled out as an A/B experiment judged on booking metrics (Section 6.4), and MPBE's dynamic graphs are justified partly by "quick A/B testing... without redeploying code" [VERIFIED: posts cited above].

---

## PART 7: Trip.com Group

All Trip.com facts below come from one source: the Form 20-F for fiscal 2025 [VERIFIED: https://www.sec.gov/Archives/edgar/data/1269238/000119312526183379/d27369d20f.htm, published 2026-04-28].

- Brands include Ctrip, Trip.com and Qunar (operating data mostly presented for Ctrip + Trip.com combined).
- 2025 revenue RMB 62.5bn (US$8.9bn); **accommodation reservation RMB 26.1bn, 42% of revenue** (39% in 2023, 40% in 2024).
- "We act as an agent in substantially all of our hotel-related transactions" and earn "substantially all" accommodation revenue "through commissions from hotel reservation partners", recognised "when the reservation becomes non-cancelable".
- Risk factors also note that the business "depends significantly upon our ability to contract with hotels in advance for the guaranteed availability of certain hotel rooms".
- ⚠ Its "open platform provided approximately 1.7 million global accommodation listings" at end-2025, with flights from over 680 airlines and over 60,000 other ecosystem partners.
- "Over 90% of our total transaction orders were executed through our mobile channels" in 2025.
- Accommodation search technology "can support billions of queries per day" and processes "tens of billions of data points needed to calculate numerous room types, room status data, and room price data incrementally updated every day". It includes "a hotel matching system".
- Partner tooling includes "an e-booking system for accommodation partners, which provides standardized information input to accommodation partners to digitalize their offerings".
- "We use both public and private cloud technologies."

[ASSUMPTION/JUDGEMENT] Trip.com is the clearest **agency-model** OTA among the three (Expedia is about 70% merchant by revenue). Its 20-F confirms the generic OTA pattern of a **hotel matching** system (deduplicating the same hotel arriving from many suppliers) and **incremental** rate and room-status updates. No English-language engineering material was reachable, so nothing below the 20-F level should be asserted.

---

## PART 8: Hosted-stays intermediaries — Hostaway, HomeToGo, Holidu

- **Hostaway** (a vacation-rental PMS / channel manager) exposes a REST/JSON public API that lets users "create, update and delete listings and reservations, read listing calendars, block and unblock calendar days". It offers **unified webhooks** ("you don't need to poll the API"), retried up to three times with exponential backoff, and then an email alert. "Webhook events may arrive out of order", so receivers must tolerate events that reference unknown entities. Per-endpoint rate limits return HTTP 429. The predefined channel list distinguishes API channels (Airbnb official, Booking.com, Expedia, HomeAway/Vrbo) from iCal channels (`vrboical`, `homeawayical`, `customIcal`, `tripadvisorical`) [VERIFIED: https://api.hostaway.com/documentation, changelog to 2026-10-05].
- **HomeToGo** (vacation-rental metasearch/marketplace) and **Holidu**: engineering blogs did not resolve or returned 403; nothing verified.

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] The hosted-stays connectivity layer is dominated by **PMS/channel-manager APIs plus iCal as a lowest-common-denominator fallback**. The hotel world instead runs on channel managers using XML ARI messages (Expedia AR, Section 2.2). Hostaway's channel IDs make the iCal fallback visible as a separate, lower-fidelity channel next to the API connection for the same marketplace.

---

## PART 9: Cross-case synthesis for chapter writers

[ASSUMPTION/JUDGEMENT] All points in this part are the analyst's synthesis, grounded in the verified claims above.

| Architectural concern | Expedia (documented) | Agoda (documented) | Trip.com (20-F only) | Hosted-stays contrast |
| --- | --- | --- | --- | --- |
| Supply ingestion | Push ARI XML (AR API) from channel managers/CRS/PMS; no direct property connections | Push streams (1.5M updates/min from one supplier) **and** QPS-capped pull from non-direct suppliers | Hotel e-booking system; incremental room/price updates | PMS/channel-manager APIs, iCal fallback; one-unit calendars |
| Sellable truth at booking | Expedia's locally stored copy; supplier cannot reject | Price cache with on-miss fetch | Not described | Platform-owned calendar; host acceptance may still gate |
| Price serving | Shopping API live-ish, price check before book | PDS >1M req/s; DragonflyDB price cache 300k reads/s | "Billions of queries per day" | Stay-level quote per unit (Expedia 2021 Ignite quote engine) |
| Distribution to others | Rapid (B2B, +20% gross bookings 2025) with traffic-vs-revenue limits | Affiliate APIs; white-label themes | Open platform to other channels | Vrbo in Rapid: limited partners, calendar API, no caching |
| Payment model | 70% merchant revenue; ETP Expedia/Hotel Collect | Pay-now and ZeroPay flows in MPBE | Agency for substantially all hotels | Pre-paid, payment schedules, damage deposits |
| Ranking | Candidate gen → DNN LTR → weighted business adjustments (Juggler) | Not documented here | TripBest ranking for destination products | Unique items, similarity substitutes matter more |
| Hosting | Primarily public cloud (AWS named) | Four own data centres, private K8s cloud | Public and private cloud | — |

Key lessons:

1. **Freshness is bought with money, not just engineering.** Both directions of the OTA supply chain ration expensive live calls: Expedia rations its partners by revenue; suppliers ration Agoda by QPS.
2. **The OTA sells from a copy.** Expedia's documentation says so explicitly, and Agoda's price cache is the same idea at the price layer. The design question is who carries the overbooking risk when the copy is stale: the supplier, by contract.
3. **Hosted stays need a different unit model.** Expedia's own documentation encodes the difference: single unit, single rate plan, calendar with check-in/out validity, host lead time, deposits, rental agreements and weekly content churn.
4. **Merging a hosted-stays brand into an OTA front end is risky.** Expedia attributed a 2024 guidance cut to Vrbo's re-platforming.

---

## Key numbers

| Number | Value | Source | Date |
| --- | --- | --- | --- |
| Expedia lodging properties | ~3.6M, of which ~2.4M Vrbo, ~1.2M other | Expedia 10-K FY2025 | 2026-02-13 |
| Expedia gross bookings 2025 | $119.6bn (B2C $83.9bn, B2B $35.7bn) | Expedia 10-K FY2025 | 2026-02-13 |
| Expedia B2B gross bookings growth | +21% (2024), +20% (2025) | Expedia 10-K FY2025 | 2026-02-13 |
| Expedia revenue mix 2025 | Merchant 70%, agency 22%, advertising/other 8% of $14.7bn | Expedia 10-K FY2025 | 2026-02-13 |
| Lodging share of Expedia revenue | 80% | Expedia 10-K FY2025 | 2026-02-13 |
| Expedia staff in technology roles | ~half of ~16,000 | Expedia 10-K FY2025 | 2026-02-13 |
| Front-end unification | Hotels.com 2022, Vrbo 2023 | Expedia 10-K FY2022, FY2023 | 2023-02-10; 2024-02-09 |
| One Key launches | US 2023, UK 2024, more markets 2025 | Expedia 10-K FY2025 | 2026-02-13 |
| AR inventory horizon | Up to 2 years ahead per room type | Expedia AR API docs | © 2025 |
| Rapid shopping request size | ≤250 properties, ≤8 rooms | Rapid Shopping docs | fetched 2026-10-21 |
| Vrbo availability calendar horizon | 3 years (less accurate beyond 1 year) | Rapid Vrbo calendar docs | fetched 2026-10-21 |
| Vrbo in Rapid | 650k+ (limited partners) ⚠ | Rapid vacation-rentals page | undated |
| Expedia ranking P99 latency | Cut ~⅔; training 30% faster | Expedia Tech blog | 2026-08-11 |
| Juggler-MAB simulation | 0.6M searches; +2.9% NDCG | arXiv 2409.08752 | 2024-09-13 |
| Expedia quote-cache priming | 120–150 min → <10 min (18 nodes) ⏳ | Expedia Tech blog | 2021-03-02 |
| Agoda data centres | 4 (Asia, Europe, US) | Agoda CTO post | 2025-05-14 |
| Agoda Price Cache load | ~300k reads/s, ~1.5–1.6M writes/s, ~1.5 TB | Agoda engineering blog | 2026-08-19 |
| Agoda Price Cache old design | 72 SQL Server shards | Agoda engineering blog | 2026-08-19 |
| Agoda Price Cache P99 after migration | ~8 ms reads, ~10 ms writes; 8× read improvement | Agoda engineering blog | 2026-08-19 |
| Agoda cache re-warm time | ~3 hours per cluster | Agoda engineering blog | 2026-08-19 |
| Agoda PDS traffic | >1M requests/s, 4 data centres | Agoda engineering blog | 2023-10-12 |
| Agoda supplier update burst | 1.5M price updates/min from one supplier | Agoda engineering blog | 2024-05-16 |
| Agoda Kafka volume | 1.8T events/day (2023); >3T records/day (2025) ⚠ | Agoda engineering blog | 2023-09-18; 2025-06-25 |
| Agoda MPBE | 4 regions, 96 pods/region, >25 graphs, ≤60 nodes | Agoda engineering blog | 2025-11 |
| Agoda A/B p-value threshold | 0.3–0.45 | Agoda engineering blog | 2023-12-15 |
| Trip.com accommodation revenue | RMB 26.1bn (42% of revenue) | Trip.com 20-F FY2025 | 2026-04-28 |
| Trip.com accommodation listings | ~1.7M ⚠ | Trip.com 20-F FY2025 | 2026-04-28 |
| Trip.com mobile share of orders | >90% | Trip.com 20-F FY2025 | 2026-04-28 |

## Open questions / not verifiable

- **Vrbo supply connectivity**: the API(s) software partners use to push listings, rates and calendars into Vrbo, whether Vrbo's supply side now runs on Expedia's lodging supply stack, and Vrbo's iCal import/export interval. Not verified; Integration Central's page was empty.
- **Depth of Vrbo/Hotels.com back-end consolidation**: filings say "front-end stack" and "shared platform infrastructure" (servicing, data centres, search capabilities, payments, fraud). Whether inventory, pricing and listing services were merged is not public.
- **Why the Vrbo re-platforming hurt**: Expedia named the effect, not the cause.
- **Expedia's lodging candidate generator and availability/pricing cache**: only search-index excerpts were available; production details unverified.
- **Booking Retrieval/Confirmation and GraphQL reservation APIs**: their polling intervals and message formats were not read (the documentation portal is JavaScript-rendered).
- **Whether Expedia AR messages follow OpenTravel (OTA) schemas**: the Booking Notification page mentions "an OTA error" response, but AR uses Expedia-specific element names (`AvailRateUpdateRQ`). Treat Expedia's format as proprietary XML unless verified.
- **Agoda**: ClickHouse use; the supplier connectivity model for direct hotels (Agoda's extranet); Agoda Homes (hosted-stays inventory) architecture; whether PriceAggregator/SmartTTL (2020) still runs in front of the 2026 DragonflyDB cache.
- **Trip.com**: no English engineering sources reached; hotel matching and incremental-update architecture known only from 20-F sentences.
- **HomeToGo, Holidu**: no verified engineering material.
- **Agoda acquisition year (2007)**: not re-verified in this session.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Form 10-K for fiscal 2025 | Expedia Group | 2026 | https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm |
| Form 10-K for fiscal 2023 | Expedia Group | 2024 | https://www.sec.gov/Archives/edgar/data/1324424/000132442424000007/expe-20231231.htm |
| Form 10-K for fiscal 2022 | Expedia Group | 2023 | https://www.sec.gov/Archives/edgar/data/1324424/000132442423000007/expe-20221231.htm |
| Q1 2024 earnings release (8-K exhibit) | Expedia Group | 2024 | https://www.sec.gov/Archives/edgar/data/1324424/000132442424000024/earningsrelease-q12024.htm |
| Lodging supply connectivity hub | Expedia Group Developer Hub | undated (2026) | https://developers.expediagroup.com/supply/lodging |
| Availability and Rates API — Introduction | Expedia Group | © 2025 | https://developers.expediagroup.com/supply/lodging/docs/avail_and_rate_apis/avail_rates/getting_started/introduction |
| Availability and Rates API — Requirements and best practices (excerpt) | Expedia Group | 2025 | https://developers.expediagroup.com/supply/lodging/docs/avail_and_rate_apis/avail_rates/getting_started/requirements-best-practices |
| Booking Notification API — Introduction | Expedia Group | © 2025 | https://developers.expediagroup.com/supply/lodging/docs/booking_apis/booking_notification/getting_started/introduction |
| Integration Central product card | Expedia Group Developer Hub | undated | https://developers.expediagroup.com/docs/products/integration-central |
| Rapid API overview | Expedia Group Developer Hub | undated | https://developers.expediagroup.com/docs/products/rapid |
| Rapid Lodging overview | Expedia Group | undated | https://developers.expediagroup.com/rapid/lodging |
| Rapid Content API | Expedia Group | undated | https://developers.expediagroup.com/rapid/lodging/content/about-content-api |
| Rapid Shopping API | Expedia Group | undated | https://developers.expediagroup.com/rapid/lodging/shopping/about-shopping-api |
| Rapid Shopping rate limiting | Expedia Group | undated | https://developers.expediagroup.com/rapid/lodging/shopping/rate-limiting |
| Rapid Property Collect | Expedia Group | undated | https://developers.expediagroup.com/rapid/lodging/booking/property-collect |
| Rapid Vacation Rentals overview | Expedia Group | undated | https://developers.expediagroup.com/rapid/lodging/vacation-rentals/about-vacation-rentals-api |
| Rapid Vrbo integration guide | Expedia Group | undated | https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-integration-guide |
| Rapid Vrbo availability calendar | Expedia Group | undated | https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-availability-calendar |
| Channel-Smart Property Search: How Expedia Tailors Rankings for You | Anne Morvan, Expedia Group Tech | 2024 | https://medium.com/expedia-group-tech/learning-to-rank-at-expedia-group-how-to-adapt-the-property-search-result-page-based-on-f4ebef78c94b |
| The Juggler Model: Balancing Expectations in Lodging Rankings | Tiago Cunha, Expedia Group Tech | 2023 | https://medium.com/expedia-group-tech/the-juggler-model-balancing-expectations-in-lodging-rankings-6d09b9b8e341 |
| A Hybrid Meta-Learning and Multi-Armed Bandit Approach for Context-Specific Multi-Objective Recommendation Optimization | Cunha, Marchini (arXiv) | 2024 | https://arxiv.org/abs/2409.08752 |
| Candidate Generation Using a Two Tower Approach With Expedia Group Traveler Data | Eric Rincon, Expedia Group Tech | 2023 | https://medium.com/expedia-group-tech/candidate-generation-using-a-two-tower-approach-with-expedia-group-traveler-data-ca6a0dcab83e |
| Choosing the Right Candidates for Lodging Ranking (excerpt only) | Expedia Group Tech | n.d. | https://medium.com/expedia-group-tech/choosing-the-right-candidates-for-lodging-ranking-d0841bf40c0e |
| How Keras 3 Helped Modernise Expedia Group's Lodging Ranking Stack | Expedia Group Tech | 2026 | https://medium.com/expedia-group-tech/how-keras-3-helped-modernise-expedia-groups-lodging-ranking-stack-7fec96f052fd |
| Kamae: Bridging Spark and Keras for Seamless ML Preprocessing | Barrowclough et al. (arXiv) | 2025 | https://arxiv.org/abs/2507.06021 |
| How Expedia Group Builds AI That Lasts at Scale | Expedia Group Tech | 2026 | https://medium.com/expedia-group-tech/how-expedia-group-builds-ai-that-lasts-at-scale-434677770fe9 |
| Mongo Change Streams in Production | Mauricio Mena, Expedia Group Tech | 2021 | https://medium.com/expedia-group-tech/mongo-change-streams-in-production-97a07c7c0420 |
| How Expedia Reviews Engineering Is Using Event Streams as a Source Of Truth | Ritesh Kapoor, Expedia Group Tech | 2023 | https://medium.com/expedia-group-tech/how-expedia-reviews-engineering-is-using-event-streams-as-a-source-of-truth-d3df616cccd8 |
| Colocating Input Partitions with Kafka Streams... (excerpt only) | Expedia Group Tech | n.d. | https://medium.com/expedia-group-tech/colocating-input-partitions-with-kafka-streams-when-consuming-multiple-topics-sub-topology-matters-f92da955c905 |
| Form 10-K for fiscal 2025 | Booking Holdings | 2026 | https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm |
| How Agoda Scaled Its Price Cache with DragonflyDB | Clarkson Chang, Agoda Engineering | 2026 | https://medium.com/agoda-engineering/how-agoda-scaled-its-price-cache-with-dragonflydb-0828e478e84f |
| Improving Performance Using Distributed Cache with Couchbase | Johan Tiesinga, Agoda Engineering | 2023 | https://medium.com/agoda-engineering/improving-performance-using-distributed-cache-with-couchbase-aa7ebf3a12c9 |
| How We Solve Load Balancing Challenges in Apache Kafka | Yifan Huang, Agoda Engineering | 2024 | https://medium.com/agoda-engineering/how-we-solve-load-balancing-challenges-in-apache-kafka-8cd88fdad02b |
| PriceAggregator: An Intelligent System for Hotel Price Fetching | Agoda (arXiv) | 2020 | https://arxiv.org/abs/2008.02087 |
| PriceAggregator blog posts, parts 1–2 (excerpts only) | Agoda Engineering | c. 2020 | https://medium.com/agoda-engineering/priceaggregator-an-intelligent-system-for-hotel-price-fetching-part-1-ba6ce66354c2 |
| How Agoda manages 1.8 trillion Events per day on Kafka | Napong Thammanochit, Agoda Engineering | 2023 | https://medium.com/agoda-engineering/how-agoda-manages-1-8-trillion-events-per-day-on-kafka-1d6c3f4a7ad1 |
| How Agoda Handles Kafka Consumer Failover Across Data Centers | Pattarapon Kittisrisawai, Agoda Engineering | 2025 | https://medium.com/agoda-engineering/how-agoda-handles-kafka-consumer-failover-across-data-centers-a3edbacef6d0 |
| Agoda's CTO on Why Managers Should Code, Running On-Prem, and Adopting Generative AI | Agoda Engineering | 2025 | https://medium.com/agoda-engineering/agodas-cto-on-why-managers-should-code-running-on-prem-and-adopting-generative-ai-b1b4c5c7028b |
| How Agoda's Multi-Product Booking Engine Powers Seamless Travel Bookings | Pavanavimutti, Nanakorn, Agoda Engineering | 2025 | https://medium.com/agoda-engineering/how-agodas-multi-product-booking-engine-powers-seamless-travel-bookings-61fc6e746821 |
| How We Cut the Coupling Tax in a Post-Booking API | Pungchaichan et al., Agoda Engineering | 2026 | https://medium.com/agoda-engineering/how-we-cut-the-coupling-tax-in-a-post-booking-api-2156a3175538 |
| Why we use lenient p-value thresholds like 0.4 for A/B experiments at Agoda — Part 1 | Varat Intaraprasonk, Agoda Engineering | 2023 | https://medium.com/agoda-engineering/why-we-use-lenient-p-value-thresholds-like-0-4-for-a-b-experiments-at-agoda-part-1-e93c7c56e666 |
| How Agoda Powers Multiple Travel Brands with One Design System | Lehtonen, Jittjana, Agoda Engineering | 2026 | https://medium.com/agoda-engineering/how-agoda-powers-multiple-travel-brands-with-one-design-system-a48de5f906af |
| Inside Agoda's Storefront: A Latency-Aware Reverse Proxy... | InfoQ | 2026 | https://www.infoq.com/news/2026/03/agoda-rust-reverse-proxy/ |
| Form 20-F for fiscal 2025 | Trip.com Group | 2026 | https://www.sec.gov/Archives/edgar/data/1269238/000119312526183379/d27369d20f.htm |
| Hostaway Public API Reference | Hostaway | 2026 (changelog) | https://api.hostaway.com/documentation |
