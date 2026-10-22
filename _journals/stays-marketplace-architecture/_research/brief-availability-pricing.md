# Research brief: Availability, rates and pricing in accommodation marketplaces

Prepared 21 October 2026 for chapter writers of *BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces*. The brief is vendor-neutral. Booking.com, Expedia Group, Agoda, Airbnb and Google get the most space because they publish detailed, dated developer documentation or engineering posts on this topic, not because the book endorses their choices.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (21 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date, not the fetch date. Developer documentation pages are often undated ("Last updated N minutes ago" with no calendar date); these are marked **published n.d.**, and they describe the API as of the fetch date.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, vendor guide, law-firm commentary, conference summary), or from a search-result excerpt of a primary page that could not be fetched in full.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every architectural statement about a proprietary system the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Pricing products, fee models and loyalty programmes change every year, and regulation in this area moved sharply in 2024–2025 (FTC fees rule, EU DMA designation of Booking.com, UK DMCC Act). The Airbnb pricing-model evidence is from 2015 (IEEE Spectrum) and 2018 (KDD paper). Both are older than three years and describe a system that has almost certainly been retrained and extended since. Do not describe them in the present tense without saying so. The single best-documented, recent engineering source on rate caching is Agoda's August 2026 Price Cache post.

**Research limitation.** Several things in the commission could not be verified from primary sources in this session:

- **No first-party engineering material on availability-search computation at Booking.com, Expedia or Trivago was found.** The Booking.com and Expedia Group Medium feeds (fetched as RSS) held no recent posts on this topic; Trivago's tech blog returned nothing usable. Statements about how these companies compute availability inside search are therefore ASSUMPTION/JUDGEMENT, anchored where possible on their public partner APIs (which constrain what the internal model must be able to represent).
- **Airbnb's 2018 engineering post "Learning Market Dynamics for Optimal Pricing"** returned HTTP 403 (Cloudflare) on Medium. The KDD 2018 paper page and a secondary paper summary were used instead.
- **Expedia Rapid's dedicated price-check page** returned 404 at its documented URL; the price-check behaviour is verified from Rapid's "About the Shopping API" and error-response pages instead.
- **Booking.com's partner help pages** (Genius) returned HTTP 403; Genius terms are tagged WIDELY REPORTED.
- **Beyond (Beyond Pricing)** produced no fetchable primary documentation; it is mentioned only as a market participant.
- **The OpenTravel Alliance specification itself** was not fetched; message-level detail comes from channel implementations (Booking.com, Agoda) that implement it.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: fee percentages, loyalty-tier thresholds, product names, enforcement status, and API limits.

---

## PART 1: The ARI model: what "availability, rates and inventory" means

### 1.1 Vocabulary

| Term | Meaning in this brief |
| --- | --- |
| **Inventory** | The number of sellable units of a room type on a night. For a hotel, many identical rooms; for a hosted home, almost always one. |
| **Availability** | The part of inventory a guest can actually book for a given search (dates, occupancy, rate plan), after restrictions. |
| **Rate plan** | A named pricing product (e.g. "Flexible", "Non-refundable", "Breakfast included"). |
| **Room-rate (product)** | The combination of a room type and a rate plan, carrying conditions: cancellation and prepayment policy, meal plan. |
| **Restrictions** | Rules that remove availability for some stays without changing inventory: MinLOS, MaxLOS, closed to arrival/departure, stop-sell, advance-purchase windows. |
| **ARI** | The stream of updates to all three, pushed from the supplier's system (PMS, channel manager, revenue management system) to each channel. |

Booking.com's connectivity documentation makes the inventory/availability distinction explicit: "Inventory is the total number of rooms a property offers for sale", whereas "Availability is the portion of inventory that guests can book based on their search criteria" [VERIFIED: https://developers.booking.com/connectivity/docs/ari, published n.d.].

Booking.com separates the *rate plan* (a label) from the *roomrate* (the bookable product with conditions): "A _rate plan_ is simply a name you use to organize prices." Cancellation policy, prepayment policy and meal plan are attached by creating a roomrate, not to the rate plan itself [VERIFIED: https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-rate-plans, published n.d.]. In v1.1 a property can have at most 200 active rate plans, and deactivating a rate plan also deactivates its roomrates and removes their inventory [VERIFIED: same page].

### 1.2 The grain of the data

[ASSUMPTION/JUDGEMENT] The natural storage grain for OTA-style ARI is **property × room type × rate plan × night**, with occupancy and length of stay as further price dimensions for some pricing types (Part 2). A property with 10 room types, 8 rate plans and a 365-day horizon already has ~29,000 price cells before occupancy variants; multiplied across a few million properties this makes ARI one of the largest write-heavy datasets in the platform. Agoda's figures (Part 6) are consistent with this: its rate cache takes far more writes than reads.

Booking.com recommends that connectivity partners publish availability "at least 12 months in advance" [WIDELY REPORTED: search excerpt of https://developers.booking.com/connectivity/docs/ari, 2026], and its B.XML availability endpoint accepts dates from one day in the past (CET) up to five years ahead [VERIFIED: https://developers.booking.com/connectivity/docs/b_xml-availability, published n.d.].

### 1.3 OTA vs hosted stays

| Dimension | OTA / professional hotel | Hosted stay (single home) |
| --- | --- | --- |
| Units per product | Many identical rooms per room type | One unit; the listing *is* the inventory |
| Rate plans | Many per room type (refundable, non-refundable, breakfast, member, mobile, package) | Usually one nightly price plus discounts (weekly, monthly, early-bird, last-minute) and fees (cleaning) |
| Who sets price | Revenue manager or RMS, distributed via PMS/CRS/channel manager | Host directly, Airbnb's Smart Pricing, or a third-party tool (PriceLabs, Wheelhouse, Beyond) |
| Source of truth | Often outside the marketplace (PMS/CRS) | Often the marketplace's own calendar, unless a PMS or channel manager is connected |
| Sync mechanism | Push API (OpenTravel-style XML, proprietary JSON) | Platform calendar, API for connected software, or iCal pull every few hours |
| Overselling posture | Overbooking is a deliberate revenue tool | Any double booking is a failure: there is no second unit |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis; each row is supported by sources later in the brief.

---

## PART 2: Pricing types: standard, derived, occupancy-based and length-of-stay

### 2.1 Booking.com's four pricing types (the best-documented public taxonomy)

Booking.com's Rates & Availability API supports four pricing types: **Standard**, **Derived pricing / Rate-Level Occupancy (RLO)**, **Occupancy-Based Pricing (OBP)** and **Length of Stay (LOS)**. "All pricing types need certification prior to implementing them", and OBP and LOS have additional technical requirements [VERIFIED: https://developers.booking.com/connectivity/docs/ari, published n.d.].

| Pricing type | What one price means | How it is pushed (per Booking.com) |
| --- | --- | --- |
| Standard | "The price for a room's maximum occupancy, applying to any booking with equal or fewer guests" | `availability` (B.XML) or `OTA_HotelRateAmountNotif` |
| Derived (RLO) | A base price plus offsets for other occupancies | Base price via `availability`; offsets via a separate `derivedprices` endpoint |
| Occupancy-based (OBP) | A separate price per number of guests | `availability` or `OTA_HotelRateAmountNotif` |
| Length of stay (LOS) | A price per arrival date *and* stay length | `OTA_HotelRateAmountNotif` or CSV `los_pricing`; "Does not support adding restrictions" |

[VERIFIED: https://developers.booking.com/connectivity/docs/understanding-pricing-types, published n.d.; https://developers.booking.com/connectivity/docs/ari, published n.d.]

Switching from derived pricing to LOS loses the base occupancy price, so all prices must be redefined [WIDELY REPORTED: search excerpt of https://developers.booking.com/connectivity/docs/con-faq-rates-availability, 2026].

**Why LOS pricing matters architecturally.** [ASSUMPTION/JUDGEMENT] With per-night pricing, the price of a stay is the sum of nightly prices, so a search engine can precompute nightly cells and add them. With LOS pricing, the price of a 3-night stay starting Tuesday is its own value, not a sum; the cache key must include arrival date and length. That multiplies the search space by the maximum supported length of stay and is a main reason LOS pricing is gated behind certification. Agoda's cache key (hotel, occupancy, check-in, check-out) is shaped exactly this way (Part 6).

### 2.2 Derived and linked rate plans

Booking.com models linked rates as **rate relations**: a child rate plan can follow its parent's price (`FollowsPrice`), restrictions (`FollowsRestrictions`), policy group (`FollowsPolicyGroup`) and open/closed status (`FollowsClosed`, with modes 0 never, 1 when parent open, 2 when parent closed, 3 always). The price offset is a `Percentage` ("`80` = 20% discount, `120` = 20% surplus", valid range 1–200) or a fixed `Amount`, which may be negative [VERIFIED: https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-rate-plans, published n.d.]. A business model cannot be assigned to a rate plan that has rate relations, and cannot be changed after the rate plan is created [VERIFIED: same page].

[ASSUMPTION/JUDGEMENT] Derived rates are a write-amplification problem for the channel, not the supplier. One base-price update can fan out to dozens of child products. A platform has two options: **materialise** child prices at write time (fast reads, write amplification, consistency risk if a derivation rule changes), or **derive at read time** (cheap writes, more CPU in search). Most OTAs are likely to do some of both. A writer should present this as a design choice, not as any named company's implementation.

### 2.3 BAR-ladder pricing vs "open pricing"

Hotel revenue management traditionally derives most rates as fixed offsets from a **Best Available Rate (BAR)**. IDeaS defines BAR as the base pricing output of its RMS, generated from demand, forecast and occupancy: "It is the base rate value that is sold to unqualified guests." BAR is used with last room value and overbooking controls to price reservations by occupancy date, number of occupants, length of stay and room type, and the RMS distributes pricing to the PMS, CRS and/or rate distribution system [VERIFIED: https://developers.ideas.com/concepts/decisioncontrols/1pricing/, published n.d.].

Duetto markets **Open Pricing**, which prices "all customer segments, room types, and distribution channels in real time" under the tagline "Go beyond the best available rate" [VERIFIED: https://www.duettocloud.com/open-pricing, published n.d.]. Duetto's glossary describes it as pricing each segment, channel and room type independently, without tying rates to a BAR ladder, and on compression nights flexing discounts to zero rather than closing channels [WIDELY REPORTED: search excerpt of https://www.duettocloud.com/es/glossary/open-pricing, 2026]. This is vendor positioning; no independent benchmark was found.

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] The OTA data model must accept both derived and independently priced products, because suppliers use both. A hosted-stays platform usually needs only one nightly price per date plus rule-based discounts, so its pricing model is simpler but its *price-suggestion* problem is harder (Part 11).

---

## PART 3: Restrictions

### 3.1 The restriction set

Booking.com's B.XML `availability` endpoint documents this set [VERIFIED: https://developers.booking.com/connectivity/docs/b_xml-availability, published n.d.]:

| Restriction | Field | Meaning |
| --- | --- | --- |
| Minimum stay (stay through) | `minimumstay` | Any stay including this night must be at least N nights |
| Minimum stay (arrival) | `minimumstay_arrival` | Stays *arriving* on this date must be at least N nights |
| Maximum stay (stay through / arrival) | `maximumstay`, `maximumstay_arrival` | Upper bounds, same two flavours |
| Exact stay (arrival) | `exactstay_arrival` | Arrivals on this date must stay exactly N nights |
| Closed to arrival | `closedonarrival` | No check-ins on this date |
| Closed to departure | `closedondeparture` | No check-outs on this date |
| Closed (stop-sell) | `closed` | Room type or room-rate not sellable on this date |
| Advance purchase | `min_advance_res`, `max_advance_res` | Booking window relative to arrival; maximum value 360D |
| Rooms to sell | `roomstosell` | Inventory count; maximum 254, 255 = unlimited |

The same page notes `to` dates are exclusive, recommends one hotel and one month per request, and lists a €50,000 per-night price ceiling under "v1.0 behavior" [VERIFIED: same page].

Booking.com warns: "Exercise caution when specifying restrictions." Overlapping restrictions can make a room unbookable, and the API neither validates them nor returns errors or warnings for conflicts [VERIFIED: https://developers.booking.com/connectivity/docs/understanding-pricing-types, published n.d.].

### 3.2 The same restrictions in OpenTravel messages

Agoda's supply API implements the OpenTravel `OTA_HotelAvailNotifRQ` message [VERIFIED: https://developer.agoda.com/supply/reference/ota_hotelavailnotifrq, published n.d.]:

- **Stop-sell**: `RestrictionStatus Status="Close"` (and `"Open"` to reopen).
- **Closed to arrival / departure**: `RestrictionStatus Status="Close" Restriction="Arrival"` / `Restriction="Departure"`.
- **MinLOS / MaxLOS**: `LengthOfStay MinMaxMessageType="SetMinLOS" Time="n"` / `SetMaxLOS`, cleared with `RemoveMinLOS` / `RemoveMaxLOS`.
- Each update targets a room and rate plan together (`InvTypeCode` + `RatePlanCode`); `Start` and `End` are inclusive; Agoda recommends "one hotel and one room per request".

Note the **date-range semantics differ**: Booking.com's B.XML `to` is exclusive; Agoda's OTA `End` is inclusive. [ASSUMPTION/JUDGEMENT] This kind of off-by-one difference is a classic source of stop-sell and overbooking defects in channel managers; a platform should normalise every inbound ARI message to one internal convention at the edge.

Channel-manager vendors document further conventions that vary by implementation, such as using placeholder values (1 for "no MinLOS", 999 for "no MaxLOS") instead of explicit removal [WIDELY REPORTED: search excerpts of SiteMinder and Tesipro developer documentation, 2026].

### 3.3 Restrictions in the hosted-stays world

Vrbo's availability calendar API (exposed through Expedia Group's Rapid) returns, per day, an `available` flag, `checkin` and `checkout` eligibility, and `stay_constraints` with `min_stay` and `max_stay`, because minimum stays vary by season. Ineligible check-ins carry an explanation such as `CHECKIN_INVALID_DUE_TO_NO_VALID_CHECKOUT_WITHIN_CONSTRAINTS`. The calendar returns no daily rates: "No, only an indication as to whether the property is bookable or not" [VERIFIED: https://developers.expediagroup.com/docs/products/rapid/lodging/vacation-rentals/vrbo-availability-calendar, published n.d.].

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] Hotels use restrictions mainly as *revenue controls* set by an RMS (IDeaS sends MinLOS decisions to the PMS; see Part 10). Hosts use them mainly as *operational controls*: turnover days, cleaning capacity, avoiding one-night gaps. The vocabulary is the same; the producer and the update frequency differ. Hosted-stay tooling adds "orphan night" logic (PriceLabs discounts 1–2 night gaps by 20% by default, Part 11), which hotels rarely need because a hotel's gap nights are absorbed across many rooms.

---

## PART 4: Meal plans and cancellation policies tied to rates

### 4.1 Policies attach to the product, not the price

At Booking.com, a policy is a combination of a cancellation policy and a prepayment policy, attached by policy ID at the roomrate level; if omitted, the property's default policy applies [WIDELY REPORTED: search excerpt of https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-roomrates, 2026]. Under the net-rate business model a non-refundable cancellation policy must be specified [WIDELY REPORTED: search excerpt of https://developers.booking.com/connectivity/docs/business-models-api/managing-business-models, 2026].

### 4.2 Expedia Rapid's machine-readable cancellation model

Expedia's Rapid API returns cancellation as data, not prose [VERIFIED: https://developers.expediagroup.com/rapid/lodging/shopping/constructing-cancellation-policies, published n.d.]:

- `cancel_penalties` entries each define a window (`start`, `end`) and a penalty: a fixed **amount** in a currency, a number of **nights** (charged from the first night, plus taxes and fees), or a **percent** of total stay charges. Amount can be combined with nights or percent; nights and percent cannot be combined in one window. Up to 3 tier windows.
- "The ISO-8601 offset returned in `cancel_penalties.start` and `cancel_penalties.end` is the authoritative value"; partners must not recompute times from the property's geography.
- **Nonrefundable date ranges** are stay dates "completely non-refundable from the time of booking"; they take precedence over `cancel_penalties`.
- California properties: the cancellation period starts 24 hours after booking unless the booking is made within 72 hours of check-in.
- After booking, `GET /itineraries` and `cancel_refund` are the source of truth for refund amounts.

Rapid's `current_refundability` returns `refundable`, `non_refundable` or `partially_refundable`, and the documentation warns that the legacy `refundable` Boolean "returns a `false` result for partially refundable rates, which is misleading for travelers" [VERIFIED: https://developers.expediagroup.com/rapid/lodging/shopping/about-shopping-api, published n.d.].

[ASSUMPTION/JUDGEMENT] This is a good reference design for the book: cancellation terms as an ordered list of time windows with typed penalties, carried with each priced offer and frozen onto the booking at confirmation. A policy stored only as text cannot be enforced, refunded or audited automatically.

### 4.3 The legal backdrop: no statutory withdrawal right for dated accommodation

The EU Consumer Rights Directive excludes from the 14-day withdrawal right "the provision of accommodation other than for residential purpose ... if the contract provides for a specific date or period of performance" (Article 16(l)) [VERIFIED: http://publications.europa.eu/resource/celex/32011L0083, published 2011-10-25]. [ASSUMPTION/JUDGEMENT] This is why cancellation terms in EU accommodation are a commercial product attribute (and a pricing lever: non-refundable rates are cheaper) rather than a legal default, and why the cancellation policy must be shown with the price.

### 4.4 Meal plans

Meal plans are set through roomrates at Booking.com and identified by a meal plan code from a published code list [WIDELY REPORTED: search excerpt of https://developers.booking.com/connectivity/docs/mobile-rates-management/managing-mobile-rates, 2026]. [ASSUMPTION/JUDGEMENT] A meal plan is best modelled as a product attribute that changes the price and the description shown in search; it is a frequent cause of metasearch price mismatches when the landing page defaults to a different board basis (see Google's "Wrong itinerary" mismatch reason, Part 7).

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] Hosted stays almost never sell board basis; their price variants are length-of-stay discounts and fees. Their cancellation policies are platform-standard tiers chosen per listing (Airbnb, Vrbo) rather than per rate plan, so a home has one policy at a time while a hotel room may have three or four bookable at once.

---

## PART 5: Moving ARI: push, pull and iCal

### 5.1 Push APIs from PMS, channel managers and RMS (OTA side)

The IDeaS integration with a PMS distribution hub lists the decision files the RMS sends: DailyBAR, LRV (last room value), MinLOS, and overbooking by hotel and by room type [WIDELY REPORTED: search excerpt of https://help-guestline.theaccessgroup.com/en/articles/13117003-ideas-revenue-management-system-rms-g2-g3, 2026]. The OTA receives the *result* of these decisions as ARI messages (Part 3); it rarely sees the forecast behind them.

### 5.2 iCal pull (hosted side)

Airbnb's calendar sync imports external calendars and "automatically updates every 3 hours"; hosts can press Refresh, but "we're only able to request updates from the other website so many times". Imported calendars pull up to two years of data. Nights blocked or booked on Airbnb "will be blocked on the other website's calendar", while nights blocked elsewhere "may or may not be blocked on Airbnb" depending on settings [VERIFIED: https://www.airbnb.com/help/article/99, published n.d.].

iCalendar (RFC 5545, September 2009) is a calendaring and scheduling format with event and free/busy components [VERIFIED: https://www.rfc-editor.org/rfc/rfc5545, published 2009-09]. [ASSUMPTION/JUDGEMENT] It has no concept of price, rate plan, occupancy or restriction, so iCal sync carries **blocked dates only**. Prices, minimum stays and discounts must be maintained separately on every channel, or via an API-connected PMS/channel manager. The 3-hour polling interval is the main structural cause of cross-platform double bookings for multi-listed homes.

Hosts in Airbnb's Community Center describe the polling gap as leaving them "wide open to receiving double bookings from your other STR platforms during that time frame" [WIDELY REPORTED: search excerpt of https://communitycenter.airbnb.com/ (host forum), date unknown]. This is anecdote, not data.

**OTA vs hosted stays.** The hotel world pushes deltas in near real time from a system of record; the long tail of hosted stays still relies on polled iCal feeds with hours of latency. A platform serving both must support both, and should treat iCal-sourced availability as lower-confidence (for example, by preferring request-to-book or a final availability recheck for such listings) [ASSUMPTION/JUDGEMENT].

---

## PART 6: Computing and caching availability for search

### 6.1 Agoda's Price Cache (the best recent primary source)

Agoda's August 2026 engineering post describes the Price Cache at the centre of its pricing architecture [VERIFIED: https://medium.com/agoda-engineering/how-agoda-scaled-its-price-cache-with-dragonflydb-0828e478e84f (fetched via RSS feed), published 2026-08-19]:

- The cache "stores terabytes of volatile rate data fetched from our global network of suppliers". Search backends read from it; "A cache hit provides an immediate response. A cache miss triggers an on-demand workflow that fetches the latest rates and integrates them back into the system."
- Before migration: ~**300,000 reads/s** and close to **1.5 million writes/s**, P99 latency requirement under **50 ms**; dataset ~**1.5 TB** in memory. Load tests modelled a **1:6 read-to-write ratio** with ~10 keys per MGET.
- The legacy store was SQL Server with **72 shards**, application-level routing, and step-wise scaling (6 → 12 → 18 servers) requiring manual shard remapping; hardware was doubled in early 2024 and was near its limits again within a year.
- Replacement: DragonflyDB (Redis-compatible), chosen partly for built-in TTL expiry, because "Hotel rates are highly volatile and change frequently" and SQL Server needed a separate cleanup job for stale supplier data.
- The first deployment stored only "hot data, defined as itineraries with a length of stay between one and four days"; that grew to ~900 GB and hit a 90% memory threshold, forcing a move to a sharded cluster (three shards per cluster) holding the full dataset, at ~1.6 million writes/s with P99 ~10 ms.
- The Price API retrieves by "hotel, occupancy, check-in date, and check-out date". Parity during migration was measured on supplier count and price-data length per supplier (>99.9% match); read P99 ~8 ms at ~300,000 requests/s.
- Two clusters (A/B) for availability; after maintenance a cold cluster took **~3 hours** to warm to the healthy cluster's hit ratio. Automated failover: every 5 s each pod compares A/B hit ratios over the previous 5 minutes and marks a cluster unreadable if its ratio falls ≥10 percentage points below and the gap is statistically significant (recovery at 3 points); ~40 pods failed over within ~2 minutes in a test, with no coordinator.

**What this tells the book.** [ASSUMPTION/JUDGEMENT] (1) For an OTA aggregating many suppliers, availability-and-price for search is a **cache of supplier answers keyed by itinerary**, not a live query. (2) Writes dominate reads, because supplier updates arrive whether or not anyone searches. (3) The cache's hit ratio is itself a business metric: a cold cache means "customers receiving no prices for their searches", so warming and failover are product concerns. (4) Short stays (1–4 nights) dominate demand, which justifies tiering by length of stay.

### 6.2 Expedia Rapid: what partners are told about freshness

Expedia's Rapid documentation states: "Many suppliers use dynamic pricing, or what is also called 'time-based pricing'", and "Expedia Group receives updated rates multiple times per second, which means that rates change frequently." It also states there is caching for rates and availability at multiple levels, which can add latency to any booking, and that sold-out errors "may also occur if the connection to the supplier is degraded", in which case true availability is unknown [VERIFIED: https://developers.expediagroup.com/rapid/resources/error-responses-lodging, published n.d.].

Rapid's Shop call returns rates and availability for up to **250 properties** and up to **8 rooms** per request, each rate with promotions, refundability, cancellation penalties and a price breakdown [VERIFIED: https://developers.expediagroup.com/rapid/lodging/shopping/about-shopping-api, published n.d.]. Rapid's rate limiting names "the number of hotels, the number of rooms, and the length of the stays being searched in each request" as the main load factors for shopping traffic [VERIFIED: https://developers.expediagroup.com/rapid/lodging/shopping/rate-limiting, published n.d.].

### 6.3 Booking.com and Airbnb: what is not public

No Booking.com or Airbnb primary source describing internal availability-search computation was found in this session.

[ASSUMPTION/JUDGEMENT] A reasonable reference architecture for both:

1. **Candidate retrieval** on a search index that holds a coarse availability projection (e.g. per-listing bitmaps of open nights or precomputed "available for stays of length k starting on day d"), filtered by location and attributes.
2. **Exact availability and price** for the top candidates, computed from the ARI store (or a price cache like Agoda's) with restrictions applied: MinLOS/MaxLOS, CTA/CTD, advance purchase, occupancy.
3. **Final check at booking**, transactional against the system of record.

The search tier may be eventually consistent; the booking tier must not be. Interview-prep sources describe this two-phase pattern [WIDELY REPORTED: https://www.techinterview.org/post/3233474326/system-design-design-airbnb-accommodation-booking-search-availability-calendar-pricing-review-system-geospatial/, 2026], but they are generic, not company documentation, and must not be cited as how Airbnb or Booking.com work.

### 6.4 Hosted-stays specifics

Vrbo's availability calendar API "should be called on page load when the UI calendar view is displayed", and "Caching is not supported at this time" [VERIFIED: https://developers.expediagroup.com/docs/products/rapid/lodging/vacation-rentals/vrbo-availability-calendar, published n.d.]. [ASSUMPTION/JUDGEMENT] For one-unit listings, the calendar is small (one bit per night plus constraints), so serving it live is cheap and the risk of a stale "available" is high. That is the opposite trade-off from a hotel price cache, where the dataset is enormous and individual staleness is tolerable because a hotel rarely sells its last room.

**OTA vs hosted stays.** For an OTA the hard problem is *volume and price freshness* across millions of supplier products; for a hosted-stays platform it is *correctness of a single unit's calendar* across several channels. The first is solved with large write-heavy caches and price checks; the second with authoritative calendars, fast cross-channel sync and request-to-book where sync is weak [ASSUMPTION/JUDGEMENT].

---

## PART 7: Look-to-book, staleness and price checks before booking

### 7.1 Look-to-book ratios

A 2016 Hospitality Net opinion piece by Triometric (a channel-analytics vendor) says top hotel distributors saw ~500 searches per booking five years earlier, and that this "is now the order of 20,000:1". The author argues metasearch explains only a small part (20 metasearch sites × 20 calls = ~400 searches) and attributes most of the rest to machine-generated scraping of prices by hotel and check-in date [VERIFIED: https://www.hospitalitynet.org/opinion/4074433.html, published 2016-02-18]. ⚠ The figure is ten years old, comes from a vendor, and is not an audited industry statistic.

Pegasus (a hotel distribution switch) has described its shopping-cache enhancements as a response to distributors sending "many single property availability transactions", producing "excessively high look-to-book ratios" [WIDELY REPORTED: https://www.travelagentcentral.com/hotels/pegasus-introduces-enhanced-shopping-transaction, date unknown].

Expedia Rapid sets shopping rate limits per partner per minute and per day; existing partners' limits are recalculated monthly "based on traffic versus revenue", typically over about three months, and partners are advised to reduce load by pre-filtering properties "less likely to convert" [VERIFIED: https://developers.expediagroup.com/rapid/lodging/shopping/rate-limiting, published n.d.]. [ASSUMPTION/JUDGEMENT] "Traffic versus revenue" is a look-to-book control in all but name: affiliates that search much and book little get less capacity.

[ASSUMPTION/JUDGEMENT] The architectural consequence: an OTA or bedbank cannot pass every search through to supplier systems. Search must be served from caches; only the last steps (rate selection, price check, booking) go live. Look-to-book is the economic reason caches exist and the reason they are stale.

### 7.2 The price check step

Expedia Rapid documents an explicit shop → price check → book flow [VERIFIED: https://developers.expediagroup.com/rapid/lodging/shopping/about-shopping-api, published n.d.]:

- "If the price is matched, the response returns a link to request a booking."
- "If the price has changed, the response returns new price details and a booking link for the new price."
- If the rate is unavailable, the response returns a new Shop link to search again.
- "Tokenized request links will expire after a short period"; "Do not store link values for long term re-use."
- "There may be a slight variation of approximately 0.1% (per room × person × night) in the billable amount."

Expedia's test-request documentation lists price-check test values `available`, `price_changed` and `sold_out` [WIDELY REPORTED: search excerpt of https://developers.expediagroup.com/docs/products/rapid/lodging/shopping/rapid-shopping-test-request, 2026]. A 410 response means the followed link "has expired or the inventory requested is no longer available"; the recovery for a price mismatch is a fresh price check [VERIFIED: https://developers.expediagroup.com/rapid/resources/error-responses-lodging, published n.d.].

Sabre's hotel API has the same step ("Hotel Price Check", between shopping and booking, keyed by a rate key) [WIDELY REPORTED: https://developer.sabre.com/docs/rest_apis/hotel/search/hotel_price_check, 2026], which suggests the pattern is industry-standard rather than Expedia-specific.

### 7.3 The consumer-law limit on price checks

The European Commission's 2021 UCPD guidance says traders may use dynamic pricing as long as they inform consumers about total costs, but "A dynamic pricing practice where a trader raises the price for a product during the booking process, in particular after the consumer has put it in his digital shopping cart or proceeds to payment, without giving the consumer reasonable time to complete the transaction, could be considered contrary to professional diligence or as aggressive practice under Articles 8 and 9 of the UCPD" [VERIFIED: http://publications.europa.eu/resource/celex/52021XC1229(05), published 2021-12-29].

[ASSUMPTION/JUDGEMENT] The design implication: a price check that *finds* a supplier price change and shows it transparently, with the option to abandon, is defensible; a funnel that *introduces* increases at checkout is not. Platforms should hold a confirmed price for a short, explicit window once the guest enters checkout, absorb small variances (Expedia documents ~0.1%), and log every price change shown to a guest.

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] An OTA reselling supplier inventory faces genuine price drift between search and book; the price check is how it reconciles. A hosted-stays platform that owns the calendar and price usually computes the quote itself, so a search-to-checkout price change should be rare and is mostly self-inflicted (stale search index, discount rules evaluated differently in search and checkout).

---

## PART 8: Metasearch and price accuracy

### 8.1 Google's Price Accuracy Policy

Google Hotel Center's Price Accuracy Policy requires that "Prices must be accurate and bookable online". Google checks a sample ("Google may not check every price offered to users"), comparing the total on the partner's booking page with the total shown on Google, in "the currency that a user would find on Google"; partners should "keep your site's conversions updated every few hours". "Taxes and fees must represent all mandatory charges", "must not be manipulated to create an artificially low base rate", and "must be clearly disclosed on the final booking page" [VERIFIED: https://support.google.com/hotelprices/answer/6064419?hl=en, published n.d.].

Consequences are graded: scores of Excellent, Fair, Poor, At Risk and Failed; at Failed "Your ads and free booking links will be turned off". Individual itineraries may be hidden "due to inaccurate prices" regardless of the account score; a hotel may be added to a suspension list; and "Your Hotel Center account may be suspended" for persistent non-compliance [VERIFIED: same page]. The page sets no numeric tolerance above the advertised price [VERIFIED: same page].

Hotel Center's Accuracy tab shows a 30-day score trend and the most common mismatch reasons over the last 7 days, including *Discount missing*, *Taxes + fees missing*, *Room not available*, *Login missing*, *Site error*, *Wrong itinerary* and *Blocked* (the site rejected Google's checker, e.g. by rate limiting or bot detection) [WIDELY REPORTED: search excerpt of https://support.google.com/hotelprices/answer/6318506, 2026].

[ASSUMPTION/JUDGEMENT] Each mismatch reason maps to an engineering cause: *Room not available* is cache staleness; *Taxes + fees missing* is a price-composition difference between feed and site; *Login missing* is member pricing leaking into a public feed; *Blocked* is bot defence catching the auditor. A metasearch-facing platform therefore needs (a) one price-composition service used for both the feed and the checkout, and (b) an allow-list for verified price-accuracy crawlers.

### 8.2 Conditional and private rates on metasearch

Google supports **conditional rates** (formerly "fenced") that depend on device, country, language, a random user sample, or Google sign-in status, and **private rates** (formerly "member" or "qualified") bookable only by members of a loyalty programme or audience list; Google always selects the lowest eligible rate for each user [WIDELY REPORTED: search excerpts of https://developers.google.com/hotels/hotel-prices/dev-guide/fenced-rates and https://support.google.com/hotelprices/answer/9983829, 2026]. Rates conditioned on sub-country location, age or paid third-party memberships are not accepted [WIDELY REPORTED: same].

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] Google's hotel price-accuracy regime was built for hotels and OTAs; vacation rentals are also listed on Google, but the single-unit calendar makes "Room not available" the dominant risk rather than price drift.

---

## PART 9: Rate parity

### 9.1 EU law: the DMA and the CJEU

The Digital Markets Act prohibits a gatekeeper from preventing business users "from offering the same products or services to end users through third-party online intermediation services or through their own direct online sales channel at prices or conditions that are different from those offered through the online intermediation services of the gatekeeper" (Article 5(3)) [VERIFIED: http://publications.europa.eu/resource/celex/32022R1925, published 2022-10-12].

The Commission designated Booking Holdings a gatekeeper for Booking.com on 13 May 2024, with compliance due by 14 November 2024 [WIDELY REPORTED: https://legalblogs.wolterskluwer.com/competition-blog/bookingcoms-dma-compliance-workshop-the-power-of-no-win-lose-lose/, 2024]. Booking.com said it removed narrow and wide parity clauses EU-wide, applying to new and existing partners from 2 December 2024; hotel associations (HOTREC) dispute that the compliance is complete ⚠ [WIDELY REPORTED: same].

On 19 September 2024 the Court of Justice ruled (Case C-264/23, Booking.com) that "parity clauses, both wide and narrow, inserted into the agreements concluded between online hotel reservation platforms and providers of accommodation services do not fall outside the scope of [Article 101(1) TFEU] on the ground that they are ancillary to those agreements" [VERIFIED: http://publications.europa.eu/resource/celex/62023CJ0264, published 2024-09-19].

### 9.2 What parity means for systems

[ASSUMPTION/JUDGEMENT] With contractual parity gone in the EU, price *competitiveness* replaces price *parity* as the platform's lever: platforms monitor rates elsewhere and may surface or rank on them, and hotels are free to undercut OTAs on their own sites. For architecture this means: rate-shopping data pipelines (competitor price ingestion), comparisons shown to suppliers in extranets, and a clear audit trail showing that ranking does not penalise suppliers for pricing elsewhere (the DMA's recitals target "measures with equivalent effect", such as raised commissions or de-listing [WIDELY REPORTED: Wolters Kluwer, 2024]).

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] Parity disputes are a hotel–OTA phenomenon. Individual hosts rarely run direct-booking channels at scale; professional managers do, and the same EU rules protect them where a gatekeeper is involved.

---

## PART 10: Overbooking, double booking, allotments and free sale

### 10.1 Hotel overbooking is a revenue control

A 2018 University of Delaware dissertation (Riasi) found that hotels that overbook outperformed those that do not; risk-based overbooking produced the highest RevPAR index among four approaches; and the best results came from overbooking below 5% of capacity on roughly 6–10 days per month, while overbooking above 10% of capacity or on more than 20 days per month was associated with lower RevPAR index. Data: cancellation policies of ~600 US hotels and a survey of 10,000 hotels with a 3.77% response rate [VERIFIED: https://udspace.udel.edu/items/b2eefd99-8e27-4927-b6be-996c3b264b1e, published 2018]. The low response rate limits generalisation.

Cornell's executive-education course on overbooking (Sheryl Kimes) frames it as protection against revenue loss from no-shows, built on no-show forecasting, no-show rates and cancellation forecasts, with costs including displacement and the customer impact of overbooking [VERIFIED: https://ecornell.cornell.edu/courses/hospitality-and-foodservice-management/overbooking-practices-in-hotel-revenue-management/, published n.d.]. IDeaS RMS sends overbooking decisions by hotel and room type to the PMS [WIDELY REPORTED: Guestline/IDeaS integration guide, 2026].

### 10.2 Overbooking on the OTA side is mostly an integration failure

Booking.com's connectivity documentation lists the causes of overbookings it sees: "System outages preventing availability from being updated", "Incorrect auto-replenishment of cancelled reservations or room nights", "Late requests to close availability before bookings are made", "Non-XML rates being used in the reservation", and "The rate not being correctly mapped for ARI updates". "Auto-replenishment is an automatic default function that puts cancelled rooms back up for sale on Booking.com", even on closed dates unless the property disables "Reopen closed rooms"; connectivity partners cannot turn it off. When a room is overbooked, Booking.com's Customer Service contacts guest and property to arrange an alternative room or a relocation [VERIFIED: https://developers.booking.com/connectivity/docs/con-faq-reservations-troubleshooting-overbookings, published n.d.].

[ASSUMPTION/JUDGEMENT] So the OTA sees two kinds of oversell: deliberate overbooking inside the hotel (handled by the hotel's walk procedures) and accidental overselling across channels (handled by the OTA's relocation process). Auto-replenishment is a good example of a platform-side default that is revenue-positive on average and overbooking-negative in edge cases; it deserves explicit design discussion.

### 10.3 Hosted stays: one unit, zero tolerance

[ASSUMPTION/JUDGEMENT] A home has one unit, no-shows still pay (under most cancellation policies), and there is no comparable room down the corridor. Overbooking has no revenue logic, and the platform must prevent double booking with (a) a transactional lock on the listing-night set at booking, (b) fast propagation of the block to other channels, and (c) host-side controls (request-to-book, buffer days). The residual risk is cross-channel lag, which on iCal is up to ~3 hours on Airbnb's side (Part 5).

### 10.4 Allotments vs free sale

Industry explainers define an **allotment** as a block of rooms a hotel commits to a buyer (tour operator, wholesaler, bedbank), with unsold rooms released back on a contractual release date (examples cite days before arrival) [WIDELY REPORTED: https://en.wikipedia.org/wiki/Allotment_(travel_industry), 2026], and **free sale** as permission to sell up to an agreed quantity without checking with the hotel first, each booking decrementing the pool [WIDELY REPORTED: https://help.nomadstays.com/kb/about-listing/what-do-you-mean-by-free-sale/, date unknown]. Terminology varies; some B2B vendors use "free sale with availability check" for contracted rates with no committed inventory [WIDELY REPORTED: https://dmcquote.com/blog/post/b2b-hotel-portal-inventory-allotment-vs-free-sale, date unknown]. Contract wording governs.

[ASSUMPTION/JUDGEMENT] For the data model: an allotment is inventory *owned by a channel* for a period (a per-channel counter with a release date that must fire on schedule), while modern OTA connectivity is overwhelmingly a shared pool ("last-room availability"), where every channel sells from the same count pushed by the PMS. Bedbanks and tour operators still mix both. Hosted stays have no allotment concept.

---

## PART 11: Price setting: hotel RMS and host dynamic pricing

### 11.1 Hotel revenue management systems

- **IDeaS**: BAR generated from demand, forecast and occupancy; used with last room value and overbooking controls; output distributed to PMS, CRS and/or rate distribution systems [VERIFIED: https://developers.ideas.com/concepts/decisioncontrols/1pricing/, published n.d.]. Vendor-reported uplifts (e.g. 15% over non-RM properties) are marketing claims [WIDELY REPORTED: https://ideas.com/wp-content/uploads/2020/06/IDeaS-G3-RMS-Brochure-EE.pdf, 2020].
- **Duetto**: "Open Pricing", pricing segments, room types and channels independently rather than via BAR offsets [VERIFIED: https://www.duettocloud.com/open-pricing, published n.d.].

[ASSUMPTION/JUDGEMENT] For the marketplace, the RMS is upstream and invisible: what arrives is a dense stream of ARI changes, often recomputed several times a day. The marketplace's job is to ingest those changes quickly and faithfully, not to second-guess them.

### 11.2 Airbnb's pricing model (dated evidence)

- **2015.** Airbnb's product lead Dan Hill described a system that "calculates price tips based on hundreds of attributes", estimates booking probability at a price, uses lead time ("number of lead days before booking day"), redraws neighbourhood boundaries from booking and price data, lets hosts go "higher or lower than the price tip", and "later checks back on the fate of the listing and uses this information to adjust future tips". It ran on Aerosolve, which Airbnb open-sourced [VERIFIED: https://spectrum.ieee.org/the-secret-of-airbnbs-pricing-algorithm, published 2015-08-20]. ⚠ Over ten years old.
- **2018 (KDD).** "Customized Regression Model for Airbnb Dynamic Pricing" (Peng Ye et al.) describes three stages: a binary classifier for booking probability per listing-night; a regression model with a customised loss for the optimal price per listing-night; and personalisation logic on top. It notes that "there are no 'identical' products on Airbnb", which makes demand curves hard to estimate. The strategy powers Price Tips and Smart Pricing, and online A/B tests showed it to be effective [VERIFIED: https://www.kdd.org/kdd2018/accepted-papers/view/customized-regression-model-for-airbnb-dynamic-pricing, published 2018-08].
- A secondary summary explains the loss: zero inside a band bounded below by the booked price (for booked nights) or by a fraction of the listed price (for unbooked nights), and above by a multiple of the booked price or by the listed price; and two offline metrics, price-decrease recall and booking regret, noting that recall alone would teach the model to give rooms away free [WIDELY REPORTED: https://blog.acolyer.org/2018/03/customized-regression-model-for-airbnb-dynamic-pricing/, 2018].
- **2019 (Experiences).** An Airbnb Experiences paper proposes pricing from search data; offline it beats baselines by at least 20% in booking regret and 55% in revenue potential [VERIFIED: https://arxiv.org/abs/1911.05887, published 2019-11-14].

### 11.3 Airbnb's host-facing pricing tools today

- **Smart Pricing** uses "hundreds of factors about your listing and your area"; the host sets a minimum and maximum; "Your pricing changes will not affect pending or confirmed reservations"; early-bird-type discounts can take the guest price below the Smart Pricing minimum; weekly, monthly and trip-length discounts "override Smart Pricing"; "Smart Pricing overrides rule-sets"; and Airbnb may "temporarily turn off Smart Pricing to prevent extreme price changes" during disasters, emergencies or political unrest, and to comply with local laws [VERIFIED: https://www.airbnb.com/help/article/1168, published n.d.]. ⚠ Airbnb's own Resource Center pages describe the rule-set interaction the other way round; check before citing [WIDELY REPORTED: search excerpt of https://www.airbnb.com/resources/hosting-homes/a/using-airbnb-pricing-tools-707, 2026].
- **Similar listings and price tips.** In October 2024 Airbnb said its similar-listings tool showing average nearby prices "has been used by over 2 million hosts" and introduced a one-tap "nightly price tip suggestion" based on comparable listings [VERIFIED: https://news.airbnb.com/airbnb-2024-winter-release-highlights, published 2024-10-16]. In April 2025 it said "more than four out of five hosts used at least one" of its pricing tools (discounts, promotions, price tips, similar listings) in the past year [VERIFIED: https://news.airbnb.com/total-price-display-is-now-standard-globally, published 2025-04-21]. Airbnb said two-thirds of hosts offered weekly or monthly discounts by the end of 2023 [WIDELY REPORTED: search excerpt of https://news.airbnb.com/airbnb-q4-2023-and-full-year-financial-results, 2024].

### 11.4 Third-party host pricing tools

- **PriceLabs.** Prices are customised at listing, group or account level ("group/account level settings will be ignored for listings with their own specific customization"); account-level settings can be set per PMS or channel; discounts cannot push rates below the listing minimum; default **orphan-day discount of 20%** for 1–2 night gaps; default **last-minute discount of 30% phased over 15 days**; far-out minimum prices; day-of-week adjustments "applied on top of our default recommendations" [VERIFIED: https://help.pricelabs.co/portal/en/kb/articles/pricing-customizations, published n.d.]. ⚠ Defaults change.
- **Wheelhouse.** Pushes recommended rates to Airbnb, Vrbo and many PMSs; offers rules for minimum stays and gap nights; pricing has included a revenue-share plan ⚠ [WIDELY REPORTED: https://strspecialist.com/reviews/wheelhouse-dynamic-pricing-review, 2026].
- **Beyond.** A comparable host-pricing vendor; no primary documentation was fetched in this session.

[ASSUMPTION/JUDGEMENT] Architecturally, third-party pricing tools are **write clients** of the marketplace's pricing API, often through a PMS. The platform must define precedence (host manual override vs Smart Pricing vs third-party tool vs discounts), rate-limit nightly full-calendar rewrites from thousands of tools, and make the effective price for any night explainable to the host. The Smart Pricing help article's precedence rules show how quickly this becomes non-obvious even inside one platform.

**OTA vs hosted stays.** Hotels price through professional RMS with forecasts of many identical rooms; hosts price unique single units with sparse booking signal, which is exactly why Airbnb's 2018 paper replaced classic demand-curve optimisation with a booking-probability classifier plus a bounded regression [VERIFIED: KDD 2018 page, above]. The marketplace's role differs too: OTAs mostly *receive* prices; Airbnb *suggests and sets* them for many hosts.

---

## PART 12: Price display regulation: total price, drip pricing, personalised pricing

### 12.1 United States: FTC Rule on Unfair or Deceptive Fees

The FTC's Rule on Unfair or Deceptive Fees (16 CFR Part 464) took effect on **12 May 2025**. It covers businesses that offer, display or advertise live-event tickets or **short-term lodging**, "including third-party platforms, resellers, and travel agents". Short-term lodging includes "Temporary sleeping accommodations at a hotel, motel, inn, short-term rental, vacation rental, or other place of lodging"; the rule "doesn't mandate what length of stay qualifies as short-term". "The total price includes all charges or fees the business knows about and can calculate upfront", including mandatory fees such as resort fees; businesses may exclude taxes and government charges from the displayed total but must disclose them before asking for payment; and they must "display the total price more prominently than other pricing information". Dynamic pricing "based on demand or inventory" is allowed if not misleading. Marketplaces must give sellers what they need to calculate the total [VERIFIED: https://www.ftc.gov/business-guidance/resources/rule-unfair-or-deceptive-fees-frequently-asked-questions, published 2025-05].

The final rule was announced in December 2024 and set to take effect 120 days after Federal Register publication [WIDELY REPORTED: https://www.reedsmith.com/es/perspectives/2025/01/junk-fees-no-more-the-ftc-releases-final-rule-on-unfair-or-deceptive-fees, 2025].

### 12.2 European Union

- **UCPD Article 7(4)(c)**: in an invitation to purchase, material information includes "the price inclusive of taxes, or where the nature of the product means that the price cannot reasonably be calculated in advance, the manner in which the price is calculated" plus additional charges [VERIFIED: http://publications.europa.eu/resource/celex/32005L0029, published 2005-06-11].
- **2021 Commission UCPD guidance**: "Drip pricing covers situations where traders add costs along the purchase process, for example, by adding charges which are unavoidable and should have been included in the price from the outset"; it can be a misleading action or omission. The guidance names drip pricing among unfair practices in travel and states that UCPD information duties apply to intermediaries "such as travel booking" platforms, not only hotels [VERIFIED: http://publications.europa.eu/resource/celex/52021XC1229(05), published 2021-12-29]. It also notes that, after CPC joint actions, Booking.com and Expedia agreed to show when payments affect the ranking of accommodations [VERIFIED: same].
- **Omnibus Directive (EU) 2019/2161** added to the Consumer Rights Directive a duty to inform consumers "where applicable, that the price was personalised on the basis of automated decision-making" (new Article 6(1)(ea)). Recital 45 says this "should not apply to techniques such as 'dynamic' or 'real-time' pricing that involve changing the price in a highly flexible and quick manner in response to market demands when those techniques do not involve personalisation based on automated decision-making" [VERIFIED: http://publications.europa.eu/resource/celex/32019L2161, published 2019-12-18].
- The Omnibus also inserted Article 6a into the Price Indication Directive 98/6/EC: "Any announcement of a price reduction shall indicate the prior price", meaning "the lowest price applied by the trader during a period of time not shorter than 30 days" [VERIFIED: same]. [ASSUMPTION/JUDGEMENT] Directive 98/6/EC concerns products sold by traders and is generally read as applying to goods, so its application to accommodation strikethrough prices is doubtful; strikethrough and "was" prices on accommodation are policed mainly under the UCPD and through CPC commitments. Chapter writers should get legal confirmation before stating either way.
- **CPC enforcement**: following a 2018 common position, Airbnb changed its price presentation so that "the consumer is provided with the total price inclusive of all the applicable mandatory charges and fees" (factsheet of 11 July 2019); Booking.com (18 December 2019) and Expedia Group (18 December 2020, covering Expedia, ebookers and hotels.com) gave EU-wide commitments on how offers, discounts and prices are presented [VERIFIED: https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/accommodation-booking_en, published n.d.].
- ⚠ A proposed EU **Digital Fairness Act** is reported to target unfair pricing practices further (e.g. upfront totals), but it is a proposal, not law [WIDELY REPORTED: https://www.osborneclarke.com/insights/digital-fairness-act-unpacked-unfair-pricing-practices, 2026].

### 12.3 United Kingdom

The consumer-protection provisions of the Digital Markets, Competition and Consumers Act came into force in April 2025; they ban drip pricing and let the CMA fine up to 10% of global turnover [VERIFIED: https://www.gov.uk/government/news/cma-to-boost-consumer-and-business-confidence-as-new-consumer-protection-regime-comes-into-force, published 2025-04-07]. The CMA's draft price-transparency guidance lists "local taxes, resort fees and other unavoidable charges that become payable on arrival or departure at hotels" as mandatory charges for the headline price; the hospitality sector raised questions about damage deposits and visitor levies [WIDELY REPORTED: https://assets.publishing.service.gov.uk/media/691b1fef0dcbf6343e9a28cc/Draft_price_transparency_guidance.pdf, 2025]. ⚠ Check the final CMA209 text.

### 12.4 Platform responses

Airbnb made total price display standard worldwide on 21 April 2025: search results show "the total price of their stay", including all fees but generally before taxes ("In some countries and regions taxes are included"), with the tax-inclusive total always shown before checkout. It had launched total price display in parts of Europe, Australia, Canada and Korea in 2019, then offered a toggle in the US and 200+ other countries and regions; "almost 17 million guests" had used the toggle by 31 December 2024 [VERIFIED: https://news.airbnb.com/total-price-display-is-now-standard-globally, published 2025-04-21]. Airbnb previously said it prioritises total price rather than nightly price in search ranking, and that over 300,000 listings lowered or removed cleaning fees after the feature launched [WIDELY REPORTED: search excerpts of https://news.airbnb.com/airbnb-is-introducing-total-price-display-and-updating-guest-checkout and https://news.airbnb.com/airbnb-2023-fall-update, 2022–2023].

⚠ Airbnb has also moved hosts connected through PMS or channel-manager software to a single **15.5% host-only service fee** (guests see no separate Airbnb service fee), reported as from 27 October 2025, with later waves for other hosts; the rollout dates in secondary sources conflict [WIDELY REPORTED: https://www.altexsoft.com/travel-industry-news/airbnb-to-move-hosts-to-15-5-host-only-single-fee/, 2025; https://www.hostfully.com/blog/airbnb-host-fees/, 2026]. Airbnb's own help centre still describes guest service fees "ranging from 14.1% to 16.5% of the booking subtotal" for split-fee bookings [VERIFIED: https://www.airbnb.com/help/article/1857, published n.d.].

[ASSUMPTION/JUDGEMENT] Total-price rules turn price **composition** into core infrastructure. The search tier must compute (or cache) the full stay total, including mandatory fees and, where required, taxes, for the guest's dates and occupancy, and rank on it. Per-night "from" prices are no longer sufficient anywhere these rules apply. That pushes OTAs towards itinerary-keyed price caches (as Agoda's is) and pushes hosted-stays platforms to fold cleaning and service fees into search-time pricing.

**OTA vs hosted stays.** Hotels' regulatory exposure is resort and destination fees; hosted stays' is cleaning and service fees. Both are now in scope of the same US rule, and Airbnb's history shows that a display rule can change supplier behaviour (lower cleaning fees) [WIDELY REPORTED, above].

---

## PART 13: Discounts, member pricing and loyalty

### 13.1 OTA loyalty discounts funded by suppliers

- **Booking.com Genius.** Partner help pages describe eligibility (a minimum review score of 7.5 and a minimum number of reviews), a mandatory 10% discount on the property's best-selling or cheapest room type, optional deeper Level 2/3 discounts (15%, 20%) and perks such as breakfast, and the ability to block Genius discounts on up to 30 days per year; Booking.com reports averages of ~18% more bookings and ~17% more revenue for joining partners ⚠ [WIDELY REPORTED: search excerpts of https://partner.booking.com/en-us/help/growing-your-business/increase-revenue/what-genius-program and https://partnerhelp.booking.com/hc/en-us/articles/212708969, 2026]. Guest tiers are reported as Level 1 (10%), Level 2 (5 stays in 2 years, up to 15%) and Level 3 (15 stays in 2 years, up to 20%) ⚠ [WIDELY REPORTED: https://pointhacks.com.au/guides/loyalty-programs/booking-com-genius, 2026]. Commission is reportedly charged on the discounted price [WIDELY REPORTED: https://www.smartness.com/en/blog/booking-genius-program, 2026].
- **Expedia Group One Key** (launched 2023) unifies Expedia, Hotels.com and Vrbo loyalty around one currency, OneKeyCash; co-branded cards (July 2024) give Silver/Gold tier status associated with member savings of 15–20%+ at selected hotels ⚠ [WIDELY REPORTED: https://www.pymnts.com/travel-payments/2023/expedia-hotels-com-and-vrbo-join-forces-in-one-loyalty-program/, 2023; https://www.mastercard.com/ca/en/news-and-trends/press/2024/july/expedia-group-wells-fargo-and-mastercard-announce-new-suite-of-one-key-credit-cards.html, 2024].
- **AgodaVIP** added a Diamond tier on 16 October 2025 [VERIFIED: https://www.aap.com.au/aapreleases/cision20251015ae98423, published 2025-10-16]; Diamond is reported to give up to 25% off exclusive deals, with tier thresholds varying across sources ⚠ [WIDELY REPORTED: https://kyodonewsprwire.jp/release/202510167227, 2025].

### 13.2 What member pricing does to the data model

[ASSUMPTION/JUDGEMENT] A member price is a **conditional rate**: the same room-night has different prices depending on who is asking (logged in, tier, country, device, app). The price key for caching becomes (product, dates, occupancy, *audience*), and every surface that shows a price (search, map, metasearch feed, email) must evaluate eligibility the same way. Google's private-rates rules (Part 8.2) and its *Login missing* mismatch reason are the external enforcement of that consistency. Supplier-funded discounts (Genius) also change settlement: the commission base, the invoice, and the guest's receipt must all reflect the discount.

[ASSUMPTION/JUDGEMENT] Personalised discounts based on automated profiling of the user would trigger the EU personalised-pricing disclosure (Part 12.2). Tier- or membership-based discounts that a user can see and qualify for are usually treated as a different category, but this boundary should be checked with counsel for any ML-driven offer targeting.

**OTA vs hosted stays.** OTAs run supplier-funded loyalty discounts across millions of hotels. Airbnb's discounting is host-set (weekly, monthly, early-bird, last-minute, new-listing promotions) rather than a guest loyalty tier; Vrbo participates in One Key [WIDELY REPORTED, above].

---

## PART 14: Currency display

- Google checks price accuracy "in the currency that a user would find on Google" and advises partners to "keep your site's conversions updated every few hours" [VERIFIED: https://support.google.com/hotelprices/answer/6064419?hl=en, published n.d.].
- Expedia Rapid notes that for Expedia Collect rates the `property_inclusive` amounts are billed in the supplier's contract currency, not necessarily the request currency [VERIFIED: https://developers.expediagroup.com/rapid/lodging/shopping/about-shopping-api, published n.d.].
- Airbnb: the host sets a currency per listing; cross-currency bookings add an amount to the guest service fee, up to 16.5% of the booking subtotal ⚠ [VERIFIED: https://www.airbnb.com/help/article/1857, published n.d.]. Airbnb's payment terms reportedly pay hosts in the payout method's currency, with conversion at rates Airbnb determines that may differ from real-time market rates [WIDELY REPORTED: search excerpts of Airbnb help/terms pages, 2026].

[ASSUMPTION/JUDGEMENT] The design rule: store and settle in the supplier's currency; convert for display with a dated FX rate that is part of the quote; freeze the rate (or the charged amount) at booking; and use the same FX snapshot for the metasearch feed and the landing page, or price-accuracy checks fail on rounding. Currency is a third axis, with audience and itinerary, of the price cache key.

---

## Key lessons for the book

1. **ARI is a write-heavy, supplier-driven dataset.** Agoda's cache sees ~1.5–1.6 million writes/s against ~300,000 reads/s. Design ingestion first, search second.
2. **Search shows a cached price; booking needs a confirmed one.** The shop → price check → book flow (Expedia Rapid, Sabre) is the industry's answer to cache staleness and high look-to-book ratios; EU guidance limits how a price may rise during checkout.
3. **Price composition is now regulated infrastructure.** FTC (May 2025), the UK DMCC Act (April 2025) and EU UCPD practice all require mandatory fees in the headline or total price; one price-composition service must feed search, checkout and metasearch.
4. **Overbooking is a hotel revenue tool and a hosted-stay defect.** The OTA must support hotels' controlled overselling, recover from accidental cross-channel overselling (relocation), and still guarantee no double booking for single-unit homes.
5. **The marketplace's pricing role differs by type.** OTAs mostly ingest prices from RMS-driven suppliers (and now compete without parity clauses in the EU); hosted-stays platforms suggest or set prices for unique units with sparse demand data and must arbitrate between host, platform and third-party pricing tools.

---

## Key numbers

| Number | What it is | Source | Date |
| --- | --- | --- | --- |
| ~300,000 reads/s | Agoda Price Cache read load before migration | Agoda Engineering | 2026-08-19 |
| ~1.5 M writes/s (1.6 M after migration) | Agoda Price Cache write load | Agoda Engineering | 2026-08-19 |
| 1:6 | Read-to-write ratio modelled in Agoda's load tests | Agoda Engineering | 2026-08-19 |
| ~1.5 TB | Agoda price dataset in memory | Agoda Engineering | 2026-08-19 |
| < 50 ms P99 | Agoda Price Cache latency requirement | Agoda Engineering | 2026-08-19 |
| 72 shards | Agoda's legacy SQL Server price cache | Agoda Engineering | 2026-08-19 |
| 1–4 nights | Length of stay defining Agoda's "hot" price data | Agoda Engineering | 2026-08-19 |
| ~3 hours | Time for a cold Agoda cache cluster to warm | Agoda Engineering | 2026-08-19 |
| 4 | Pricing types in Booking.com's ARI API (Standard, Derived/RLO, OBP, LOS) | Booking.com developers | n.d. (fetched 2026-10-21) |
| 200 | Max active rate plans per property (Booking.com API v1.1) | Booking.com developers | n.d. |
| 1–200 | Valid `Percentage` range for derived rate plans (100 = parent price) | Booking.com developers | n.d. |
| 254 / 255 | Max rooms to sell / "unlimited" sentinel (Booking.com B.XML) | Booking.com developers | n.d. |
| 360 days | Max advance-booking restriction (Booking.com B.XML) | Booking.com developers | n.d. |
| 5 years | ARI horizon accepted by Booking.com B.XML | Booking.com developers | n.d. |
| 250 properties, 8 rooms | Max per Expedia Rapid Shop request | Expedia Group developers | n.d. |
| ~0.1% | Tolerated billable variance (per room × person × night) at Rapid price check | Expedia Group developers | n.d. |
| 3 | Max cancellation-penalty tier windows in Rapid | Expedia Group developers | n.d. |
| 20,000:1 | Claimed hotel distributor look-to-book (vs ~500:1 five years earlier) | Hospitality Net / Triometric (vendor opinion) | 2016-02-18 |
| 3 hours | Airbnb iCal import refresh interval | Airbnb Help Center | n.d. |
| < 5% of capacity, 6–10 days/month | Best-performing hotel overbooking levels in a US study | Riasi, Univ. of Delaware | 2018 |
| 20% / 30% over 15 days | PriceLabs default orphan-day and last-minute discounts | PriceLabs help | n.d. |
| > 2 million | Hosts who used Airbnb's similar-listings tool | Airbnb newsroom | 2024-10-16 / 2025-04-21 |
| ~17 million | Guests who used Airbnb's total-price toggle by end-2024 | Airbnb newsroom | 2025-04-21 |
| 12 May 2025 | FTC fees rule effective (lodging and tickets) | FTC | 2025-05 |
| 19 Sept 2024 | CJEU C-264/23: parity clauses not ancillary restraints | Court of Justice | 2024-09-19 |
| 13 May 2024 | Booking.com designated DMA gatekeeper (reported) | Wolters Kluwer blog | 2024 |
| 10% of global turnover | Max CMA fine under DMCC Act consumer regime | CMA / GOV.UK | 2025-04-07 |
| 15.5% ⚠ | Airbnb host-only single fee for software-connected hosts (reported) | AltexSoft / Hostfully | 2025–2026 |
| 14.1–16.5% ⚠ | Airbnb guest service fee range under split fee | Airbnb Help Center | n.d. |
| 10% / 15% / 20% ⚠ | Booking.com Genius discount levels (reported) | Partner help excerpts, consumer guides | 2026 |

---

## Open questions / not verifiable

- **How Booking.com, Expedia and Airbnb compute availability inside search**: index projection vs live computation, cache keys, TTLs, invalidation on ARI push. No first-party source found; everything in Part 6.3 is reference-architecture judgement.
- **Trivago and other metasearch price-freshness engineering**: no primary engineering source fetched. Trivago's 2024 acquisition of Holisto (a real-time rate aggregator) is reported but not verified here.
- **Current Airbnb pricing model**: the latest public technical description is the 2018 KDD paper. Whether Smart Pricing and price tips still use that three-stage design is unknown.
- **Actual look-to-book ratios today** at any named OTA, bedbank or metasearch engine: only a 2016 vendor opinion and vendor blogs exist.
- **Expedia Rapid's dedicated price-check page** (404 at the documented URL): exact response schema not verified; behaviour verified from overview and error pages.
- **Booking.com Genius terms** (403 on partner pages): tiers, eligibility thresholds and the commission base are reported, not verified.
- **Airbnb single-fee rollout dates**: secondary sources conflict (October/December 2025 vs waves through 2026).
- **Whether EU Price Indication Directive Article 6a (30-day prior price) applies to accommodation**: analyst reading is that it does not (goods only); needs legal confirmation.
- **Hotel overbooking prevalence and walk rates**: no authoritative, recent, industry-wide figure found; the Delaware study rests on a 3.77% survey response.
- **Beyond (Beyond Pricing)**: no primary documentation fetched.
- **Status of HOTREC's complaints about Booking.com DMA compliance**: ongoing ⚠; no Commission decision verified.

---

## Source list

| # | Title | Publisher / author | Year | URL |
| --- | --- | --- | --- | --- |
| 1 | How Agoda Scaled Its Price Cache with DragonflyDB | Agoda Engineering (Clarkson Chang), Medium (via RSS) | 2026-08-19 | https://medium.com/agoda-engineering/how-agoda-scaled-its-price-cache-with-dragonflydb-0828e478e84f |
| 2 | Rates & Availability API overview | Booking.com Developers | n.d. | https://developers.booking.com/connectivity/docs/ari |
| 3 | Understanding pricing types | Booking.com Developers | n.d. | https://developers.booking.com/connectivity/docs/understanding-pricing-types |
| 4 | Create or update inventory, rates and restrictions (B.XML availability) | Booking.com Developers | n.d. | https://developers.booking.com/connectivity/docs/b_xml-availability |
| 5 | Managing rate plans | Booking.com Developers | n.d. | https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-rate-plans |
| 6 | Troubleshooting overbookings | Booking.com Developers | n.d. | https://developers.booking.com/connectivity/docs/con-faq-reservations-troubleshooting-overbookings |
| 7 | Managing roomrates (search excerpt only) | Booking.com Developers | n.d. | https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-roomrates |
| 8 | Managing business models (search excerpt only) | Booking.com Developers | n.d. | https://developers.booking.com/connectivity/docs/business-models-api/managing-business-models |
| 9 | Managing mobile rates (search excerpt only) | Booking.com Developers | n.d. | https://developers.booking.com/connectivity/docs/mobile-rates-management/managing-mobile-rates |
| 10 | Rates & Availability FAQ (search excerpt only) | Booking.com Developers | n.d. | https://developers.booking.com/connectivity/docs/con-faq-rates-availability |
| 11 | OTA_HotelAvailNotifRQ | Agoda Supply API | n.d. | https://developer.agoda.com/supply/reference/ota_hotelavailnotifrq |
| 12 | About the Shopping API | Expedia Group Developer Hub (Rapid) | n.d. | https://developers.expediagroup.com/rapid/lodging/shopping/about-shopping-api |
| 13 | Rate limiting | Expedia Group Developer Hub (Rapid) | n.d. | https://developers.expediagroup.com/rapid/lodging/shopping/rate-limiting |
| 14 | Constructing cancellation policies | Expedia Group Developer Hub (Rapid) | n.d. | https://developers.expediagroup.com/rapid/lodging/shopping/constructing-cancellation-policies |
| 15 | Common error responses (lodging) | Expedia Group Developer Hub (Rapid) | n.d. | https://developers.expediagroup.com/rapid/resources/error-responses-lodging |
| 16 | Vrbo Availability Calendar | Expedia Group Developer Hub (Rapid) | n.d. | https://developers.expediagroup.com/docs/products/rapid/lodging/vacation-rentals/vrbo-availability-calendar |
| 17 | Shopping test requests (search excerpt only) | Expedia Group Developer Hub (Rapid) | n.d. | https://developers.expediagroup.com/docs/products/rapid/lodging/shopping/rapid-shopping-test-request |
| 18 | Hotel Price Check (search excerpt only) | Sabre Developer | n.d. | https://developer.sabre.com/docs/rest_apis/hotel/search/hotel_price_check |
| 19 | Price Accuracy Policy | Google Hotel Center Help | n.d. | https://support.google.com/hotelprices/answer/6064419?hl=en |
| 20 | Pricing: Check your price accuracy (search excerpt only) | Google Hotel Center Help | n.d. | https://support.google.com/hotelprices/answer/6318506 |
| 21 | Conditional rates (search excerpt only) | Google for Developers | n.d. | https://developers.google.com/hotels/hotel-prices/dev-guide/fenced-rates |
| 22 | About conditional and private rates (search excerpt only) | Google Hotel Center Help | n.d. | https://support.google.com/hotelprices/answer/9983829?hl=en |
| 23 | Customized Regression Model for Airbnb Dynamic Pricing | KDD 2018 (Peng Ye et al., Airbnb) | 2018 | https://www.kdd.org/kdd2018/accepted-papers/view/customized-regression-model-for-airbnb-dynamic-pricing |
| 24 | Customized regression model for Airbnb dynamic pricing (paper summary) | The Morning Paper (Adrian Colyer) | 2018 | https://blog.acolyer.org/2018/03/customized-regression-model-for-airbnb-dynamic-pricing/ |
| 25 | The Secret of Airbnb's Pricing Algorithm | IEEE Spectrum (Dan Hill) | 2015-08-20 | https://spectrum.ieee.org/the-secret-of-airbnbs-pricing-algorithm |
| 26 | Revenue Maximization of Airbnb Marketplace using Search Results | arXiv (Wen, Vahabi, Grbovic) | 2019-11-14 | https://arxiv.org/abs/1911.05887 |
| 27 | Use Smart Pricing to automatically adjust your prices based on demand | Airbnb Help Center | n.d. | https://www.airbnb.com/help/article/1168 |
| 28 | Sync your home host calendar to other websites | Airbnb Help Center | n.d. | https://www.airbnb.com/help/article/99 |
| 29 | Service fees (article 1857) | Airbnb Help Center | n.d. | https://www.airbnb.com/help/article/1857 |
| 30 | Total price display is now standard for guests worldwide | Airbnb Newsroom | 2025-04-21 | https://news.airbnb.com/total-price-display-is-now-standard-globally |
| 31 | Airbnb 2024 Winter Release highlights | Airbnb Newsroom | 2024-10-16 | https://news.airbnb.com/airbnb-2024-winter-release-highlights |
| 32 | Airbnb Q4-2023 and full-year financial results (search excerpt only) | Airbnb Newsroom | 2024 | https://news.airbnb.com/airbnb-q4-2023-and-full-year-financial-results |
| 33 | Airbnb is introducing total price display and updating guest checkout (search excerpt only) | Airbnb Newsroom | 2022 | https://news.airbnb.com/airbnb-is-introducing-total-price-display-and-updating-guest-checkout |
| 34 | Using Airbnb pricing tools (search excerpt only) | Airbnb Resource Center | n.d. | https://www.airbnb.com/resources/hosting-homes/a/using-airbnb-pricing-tools-707 |
| 35 | Airbnb to Move Hosts to 15.5% Host-Only Single Fee | AltexSoft | 2025 | https://www.altexsoft.com/travel-industry-news/airbnb-to-move-hosts-to-15-5-host-only-single-fee/ |
| 36 | Airbnb Host Fees: The 15.5% Host-Only Fee Explained | Hostfully | 2026 | https://www.hostfully.com/blog/airbnb-host-fees/ |
| 37 | Decision controls: Pricing | IDeaS Developer Portal | n.d. | https://developers.ideas.com/concepts/decisioncontrols/1pricing/ |
| 38 | IDeaS G3 RMS brochure | IDeaS | 2020 | https://ideas.com/wp-content/uploads/2020/06/IDeaS-G3-RMS-Brochure-EE.pdf |
| 39 | IDeaS RMS G2/G3 integration (search excerpt only) | Guestline / The Access Group | n.d. | https://help-guestline.theaccessgroup.com/en/articles/13117003-ideas-revenue-management-system-rms-g2-g3 |
| 40 | Open Pricing | Duetto | n.d. | https://www.duettocloud.com/open-pricing |
| 41 | Open pricing glossary (search excerpt only) | Duetto | n.d. | https://www.duettocloud.com/es/glossary/open-pricing |
| 42 | Setting pricing customizations in PriceLabs | PriceLabs Help | n.d. | https://help.pricelabs.co/portal/en/kb/articles/pricing-customizations |
| 43 | Wheelhouse Review | STR Specialist | 2026 | https://strspecialist.com/reviews/wheelhouse-dynamic-pricing-review |
| 44 | Is Metasearch to blame for Hospitality's 5-digit Look-to-Book? | Hospitality Net (Jonathan Boffey, Triometric) | 2016-02-18 | https://www.hospitalitynet.org/opinion/4074433.html |
| 45 | Pegasus introduces enhanced shopping transaction | Travel Agent Central | date unknown | https://www.travelagentcentral.com/hotels/pegasus-introduces-enhanced-shopping-transaction |
| 46 | Overbooking practices in the hotel industry and their impact on hotels' financial performance | Arash Riasi, University of Delaware (dissertation) | 2018 | https://udspace.udel.edu/items/b2eefd99-8e27-4927-b6be-996c3b264b1e |
| 47 | Overbooking Practices in Hotel Revenue Management (course) | eCornell (Sheryl E. Kimes) | n.d. | https://ecornell.cornell.edu/courses/hospitality-and-foodservice-management/overbooking-practices-in-hotel-revenue-management/ |
| 48 | Allotment (travel industry) | Wikipedia | 2026 | https://en.wikipedia.org/wiki/Allotment_(travel_industry) |
| 49 | What do you mean by 'free sale'? | Nomad Stays help | date unknown | https://help.nomadstays.com/kb/about-listing/what-do-you-mean-by-free-sale/ |
| 50 | B2B hotel portal inventory: allotment vs free sale | DMCquote | date unknown | https://dmcquote.com/blog/post/b2b-hotel-portal-inventory-allotment-vs-free-sale |
| 51 | RFC 5545: iCalendar | IETF (B. Desruisseaux, ed.) | 2009-09 | https://www.rfc-editor.org/rfc/rfc5545 |
| 52 | Rule on Unfair or Deceptive Fees: FAQ | US Federal Trade Commission | 2025-05 | https://www.ftc.gov/business-guidance/resources/rule-unfair-or-deceptive-fees-frequently-asked-questions |
| 53 | Junk fees no more: the FTC releases final rule | Reed Smith | 2025 | https://www.reedsmith.com/es/perspectives/2025/01/junk-fees-no-more-the-ftc-releases-final-rule-on-unfair-or-deceptive-fees |
| 54 | Directive 2005/29/EC (Unfair Commercial Practices Directive) | EU Publications Office | 2005 | http://publications.europa.eu/resource/celex/32005L0029 |
| 55 | Commission Notice: Guidance on the interpretation and application of Directive 2005/29/EC (C/2021/526) | European Commission / EU Publications Office | 2021-12-29 | http://publications.europa.eu/resource/celex/52021XC1229(05) |
| 56 | Directive (EU) 2019/2161 (Omnibus / "Better enforcement and modernisation") | EU Publications Office | 2019 | http://publications.europa.eu/resource/celex/32019L2161 |
| 57 | Directive 2011/83/EU (Consumer Rights Directive) | EU Publications Office | 2011 | http://publications.europa.eu/resource/celex/32011L0083 |
| 58 | Regulation (EU) 2022/1925 (Digital Markets Act) | EU Publications Office | 2022 | http://publications.europa.eu/resource/celex/32022R1925 |
| 59 | Judgment in Case C-264/23, Booking.com and Booking.com (Deutschland) | Court of Justice of the EU / EU Publications Office | 2024-09-19 | http://publications.europa.eu/resource/celex/62023CJ0264 |
| 60 | Coordinated actions: accommodation booking (Airbnb, Booking.com, Expedia) | European Commission | n.d. | https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/accommodation-booking_en |
| 61 | Booking.com's DMA Compliance Workshop: The Power of No | Kluwer Competition Law Blog | 2024 | https://legalblogs.wolterskluwer.com/competition-blog/bookingcoms-dma-compliance-workshop-the-power-of-no-win-lose-lose/ |
| 62 | Digital Fairness Act unpacked: unfair pricing practices | Osborne Clarke | 2026 | https://www.osborneclarke.com/insights/digital-fairness-act-unpacked-unfair-pricing-practices |
| 63 | CMA to boost consumer and business confidence as new consumer protection regime comes into force | UK CMA / GOV.UK | 2025-04-07 | https://www.gov.uk/government/news/cma-to-boost-consumer-and-business-confidence-as-new-consumer-protection-regime-comes-into-force |
| 64 | Unfair commercial practices: price transparency (draft CMA209) | UK CMA | 2025 | https://assets.publishing.service.gov.uk/media/691b1fef0dcbf6343e9a28cc/Draft_price_transparency_guidance.pdf |
| 65 | What is the Genius program? (search excerpt only; page 403) | Booking.com Partner Hub | n.d. | https://partner.booking.com/en-us/help/growing-your-business/increase-revenue/what-genius-program |
| 66 | Booking.com Genius guide | Point Hacks | 2026 | https://pointhacks.com.au/guides/loyalty-programs/booking-com-genius |
| 67 | What nobody ever told you about Booking's Genius program | Smartness | 2026 | https://www.smartness.com/en/blog/booking-genius-program |
| 68 | Expedia, Hotels.com and Vrbo join forces in one loyalty program | PYMNTS | 2023 | https://www.pymnts.com/travel-payments/2023/expedia-hotels-com-and-vrbo-join-forces-in-one-loyalty-program/ |
| 69 | Expedia Group, Wells Fargo and Mastercard announce new suite of One Key credit cards | Mastercard | 2024-07 | https://www.mastercard.com/ca/en/news-and-trends/press/2024/july/expedia-group-wells-fargo-and-mastercard-announce-new-suite-of-one-key-credit-cards.html |
| 70 | Agoda expands loyalty program with brand-new Diamond tier | AAP / Cision (Agoda release) | 2025-10-16 | https://www.aap.com.au/aapreleases/cision20251015ae98423 |
| 71 | Agoda expands loyalty program with brand-new Diamond tier | Kyodo News PR Wire | 2025 | https://kyodonewsprwire.jp/release/202510167227 |
| 72 | System Design: Design Airbnb (generic interview-prep; not company documentation) | techinterview.org | 2026 | https://www.techinterview.org/post/3233474326/system-design-design-airbnb-accommodation-booking-search-availability-calendar-pricing-review-system-geospatial/ |
