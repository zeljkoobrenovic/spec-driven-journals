# Research brief: Booking and reservation systems in accommodation marketplaces

Prepared 21 October 2026 for chapter writers of *BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces*. The brief is vendor-neutral. Booking.com, Expedia Group and Airbnb get the most space because they publish unusually detailed partner documentation, help-centre policy and investor filings about how a reservation is created, delivered, changed and cancelled, not because the book endorses their choices.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (21 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date, not the fetch date. Live documentation and help-centre pages carry no publication date; for those the tag says **live page, fetched 2026-10-21**.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, vendor documentation of a third-party integrator, newsletter summary of a primary post), or from a primary page that was seen only as a search-engine excerpt because the page itself could not be fetched.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every architectural statement about a proprietary system the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** The deepest public description of booking-path idempotency in this domain, Airbnb's Orpheus post, dates from April 2019 and is more than seven years old. It describes the payments system of that time, not necessarily today's. Partner API documentation (Booking.com Connectivity, Expedia Rapid) is live and undated, and changes without notice. Help-centre cancellation rules change often (Airbnb introduced a new "Limited" policy for bookings from 1 October 2025). Each section gives the date of its evidence. Do not describe a dated post in the present tense without checking.

**Research limitation.** Be candid with readers about four gaps:

- **No company has published a first-party engineering description of its reservation state machine, calendar-locking scheme or double-booking prevention.** Airbnb, Booking.com, Expedia, Agoda and Vrbo describe the *external* contract (partner APIs, help-centre rules, filings) but not the internal design. Every statement in this brief about how they lock inventory internally is ASSUMPTION/JUDGEMENT. Web searches for an Airbnb calendar-concurrency post returned only system-design-interview articles, which are not evidence.
- **The Airbnb Orpheus article body could not be read.** Medium returned HTTP 403; the Internet Archive copy confirms title, authors and date but is truncated behind the member wall. Its mechanism is reported here from a 2024 newsletter summary.
- **Expedia's supply-side (hotel-facing) connectivity documentation redirects to a login-gated portal.** Booking Notification and Booking Retrieval details come from search-engine excerpts of Expedia's own pages and are tagged WIDELY REPORTED.
- **The OpenTravel Alliance specification itself was not fetched.** OTA message semantics come from implementers' documentation (Booking.com, RateGain, SiteMinder excerpts). Booking.com's partner obligation to relocate a guest on overbooking (who pays) was not found in a fetchable primary text.

**Volatility flags.** ⚠ marks claims likely to change within 12 months, such as policy names, fee percentages, time windows, API versions and feature availability.

---

## PART 1: The reservation as a long-lived distributed object

### 1.1 What makes an accommodation booking different from an e-commerce order

| Property | Retail e-commerce order | OTA hotel reservation | Hosted-stay reservation |
| --- | --- | --- | --- |
| What is sold | A unit from fungible stock | A room-type night under a rate plan, from an allotment the hotel controls | One specific home on specific nights; the unit is unique |
| Who owns inventory truth | The merchant's warehouse system | The hotel's PMS / channel manager; the OTA holds a copy | The platform calendar (unless the host syncs other channels) |
| Time between purchase and fulfilment | Days | Weeks to months (the "booking window") | Weeks to months |
| Fulfilment party | Merchant or 3PL | The hotel, a separate legal entity, often on another system | The host, often an individual with no system at all |
| Typical change after purchase | Rare (return) | Frequent: date change, guest name, cancellation under a rate's policy | Frequent: alteration request, cancellation, host cancellation |
| Where failure becomes visible | Parcel does not arrive | **Guest arrives and the hotel has no record** | Guest arrives and the home is unavailable, double-booked or misrepresented |
| Money flow | Charge at order | Merchant model (OTA charges guest) or agency model (hotel charges guest) | Platform charges guest, holds funds, pays host after check-in |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis; the money-flow rows are supported by the filings in 1.2.

The architectural consequence: **a reservation is a long-lived, multi-party object whose state is replicated across systems that the marketplace does not own**. Most of this chapter's hard problems (lost deliveries, duplicates, overbookings, "booking not found at check-in") come from that replication, not from the booking transaction itself.

### 1.2 Money timing shapes the lifecycle

- **Airbnb holds the guest's money until check-in.** "When a guest books and pays for a stay, experience, or service on our platform, we hold the total amount the guest has paid until check-in, at which time we recognize our service fee as revenue and initiate the process to remit the payment to the host, which generally occurs on the business day after the scheduled check-in, barring any alterations or cancellations, which may result in funds being returned to the guest." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026 (FY2025 10-K)]. Earlier filings described remittance as about 24 hours after check-in [WIDELY REPORTED: https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm, 2023 — search excerpt, not re-read in this session].
- **Airbnb splits payment over time.** Under the "Pay Less Upfront Program" a guest "may opt to pay a percentage of the total amount due when the booking is confirmed, with the remaining balance due prior to the stay occurring"; the FY2025 10-K also names "Reserve Now, Pay Later" and lists "unbilled amounts for confirmed bookings" under these programmes [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026]. ⚠ Product names change.
- **Booking.com is shifting from agency to merchant.** Agency revenues "consist almost entirely of travel reservation commissions from Booking.com's accommodation reservations" where Booking Holdings does "not facilitate payments from travelers"; in 2025 merchant revenues rose 25.5% to $17,755M while agency revenues fell 6.5% to $7,968M "due to the ongoing shift from agency to merchant revenues at Booking.com" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18].
- **Booking Holdings recognises revenue at check-in, so cancellations do not reverse revenue.** "Because we recognize revenues from bookings when the traveler checks in, our reported revenues are not at risk of being reversed due to cancellations." Gross bookings are "recognized at the time of booking" [VERIFIED: same 10-K, published 2026-02-18].
- **Booking Holdings sometimes absorbs cancellation cost for non-refundable rates.** "In some instances, where we had agreed to provide free cancellations to consumers for non-refundable reservations, we did not estimate a recovery of prepayments already made to travel service providers. We may also offer cancellable room rates on behalf of a partner ... even if the partner has not provided a cancellable room rate" [VERIFIED: same 10-K, published 2026-02-18]. This is important: **the guest-facing cancellation policy and the supplier-facing policy can differ**, and the platform carries the gap.
- **Expedia merchant vs agency.** Under the merchant model Expedia is "the merchant of record"; "Our travelers pay us for merchant hotel transactions prior to departing on their trip, generally when they book the reservation." Under the agency model Expedia passes "reservations booked by the traveler to the relevant travel provider" and "generally record[s] agency revenue from the hotel when the stayed night occurs" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm, published 2026-02-13].

**OTA vs hosted stays.** In both, the platform typically holds funds between booking and stay, but the **counterparty to a refund differs**. On an OTA in agency mode the hotel holds the money and the OTA cannot refund on its own. In merchant mode the OTA must reclaim prepayments from the hotel or absorb them. On Airbnb the platform holds the whole amount until check-in, so cancellations before check-in are internal ledger reversals [ASSUMPTION/JUDGEMENT, built on the filings above].

---

## PART 2: Lifecycle and state machine

### 2.1 A reference lifecycle

No company has published its internal reservation state machine. The following is a reference model assembled from the externally visible states documented in Parts 3–6 [ASSUMPTION/JUDGEMENT].

```
QUOTED ──price check──► HELD ──authorize──► PENDING ──supplier/host ok──► CONFIRMED
  │                       │                   │  (request-to-book,            │
  │                       │ expiry            │   ID verification,            │ modification
  ▼                       ▼                   │   supplier delivery)          ▼
EXPIRED               RELEASED             DECLINED / EXPIRED            CONFIRMED (v2…vn)
                                                                              │
              ┌───────────────┬───────────────┬──────────────┬────────────────┤
              ▼               ▼               ▼              ▼                ▼
       CANCELLED_BY_GUEST  CANCELLED_BY_HOST  NO_SHOW     CHECKED_IN ──► CHECKED_OUT ──► COMPLETED
       (policy refund)     (penalty, rebook)  (fee/waive)  (payout trigger)                (reviews, payout settled)
```

Externally documented anchors for these states:

| State / transition | Documented anchor | Source |
| --- | --- | --- |
| Quote → price check | Expedia Rapid "Price Check" before a booking or hard change | Rapid docs (Part 6) |
| Hold without charge | Expedia Rapid `hold=true` booking; auto rollback if not resumed | Part 5.3 |
| Pending on host | Airbnb request: host has 24 h; authorization placed | Part 3 |
| Pending on identity | Airbnb: 12 h to complete identity verification after booking | Part 3 (WIDELY REPORTED) |
| Pending on supplier delivery | Booking.com queue until the provider acknowledges; email fallback after 30 min | Part 4 |
| Modification | Expedia Hard Change (same itinerary number); Airbnb alteration request | Part 6 |
| No-show | Booking.com Reporting API `is_no_show`, window from check-in midnight to 48 h after check-out | Part 7.4 |
| Check-in → payout | Airbnb remits on the business day after scheduled check-in | Part 1.2 |

### 2.2 Design rules the lifecycle implies

- **Model the reservation as an append-only sequence of versions, not one mutable row.** Partner messages already work this way: OTA modification messages are a "full overlay" of the reservation (Part 4.2), and Expedia keeps "the original itinerary number through a hard change" while issuing a different confirmation ID (Part 6.1). [ASSUMPTION/JUDGEMENT]
- **Separate "booked" from "delivered" from "acknowledged by supplier".** Booking.com's queue and fallback design (Part 4.1) only makes sense if the platform tracks delivery state per reservation version. [ASSUMPTION/JUDGEMENT]
- **Every timed state needs an owner and a timer.** The lifecycle has at least six clocks: hold expiry, host-response window (24 h), guest-completion window after RtB acceptance (24 h), identity-verification window (12 h), supplier-acknowledgement fallback (30 min, extendable to 24 h), and the 24-hour free-cancellation window. [ASSUMPTION/JUDGEMENT, the durations are cited in later sections]

**OTA vs hosted stays.** OTA lifecycles add a **supplier-delivery** sub-machine (push/pull, acknowledge, PMS confirmation number). Hosted-stay lifecycles add a **host-decision** sub-machine (request, pre-approval, alteration acceptance) and a **trust** sub-machine (identity verification). Hotel stays rarely need host approval; homes rarely need PMS delivery unless a professional manager uses software [ASSUMPTION/JUDGEMENT].

---

## PART 3: Instant book versus request to book

### 3.1 Airbnb

- **Instant Book**: "Places with Instant Book allow you to book immediately without needing to send a request to the host for approval," for reservations under 31 nights [VERIFIED: https://www.airbnb.com/help/article/523, live page, fetched 2026-10-21]. ⚠
- **Request window**: a request is declined or expires if the host does not act; "The host took longer than 24 hours to accept or decline the request, and it expired." If declined or expired, "no reservation is made" and "The authorization placed on your payment method will be removed" [VERIFIED: https://www.airbnb.com/help/article/315, live page, fetched 2026-10-21].
- **Authorization during a request**: "we may place a hold on your payment method, called an authorization, for the full amount of the reservation"; on decline or expiry "the authorization will disappear or appear as a refund," which "may take up to 5 business days, depending on the processing time of your bank or financial institution" [VERIFIED: https://www.airbnb.com/help/article/313, live page, fetched 2026-10-21].
- **Identity-verification pending state**: guests have "12 hours from the time you booked to complete identity verification, otherwise the reservation will be automatically canceled" [WIDELY REPORTED: search excerpt of Airbnb Help Center, 2026 — page not fetched]. ⚠
- **Calendar during an expired request**: a search excerpt reported that on the host side dates "remain blocked on the calendar until the host manually unblocks them" [WIDELY REPORTED: search excerpt of Airbnb Help Center, 2026 — not fetched; re-verify before using].

### 3.2 Booking.com Request to Book (homes)

- Request to Book is a "new booking model that offers eligible partners full control over the booking flow"; the partner "has 24 hours to accept or decline"; after acceptance the guest has 24 hours to complete the booking or the request expires [VERIFIED: https://developers.booking.com/connectivity/docs/request-to-book/overview, live page, fetched 2026-10-21]. ⚠
- **Payment** for `RTB` requests is pre-authorized when the request is created [VERIFIED: same page].
- **Inventory is not blocked by Booking.com during a standard RtB request, so price can change.** Under "RtB 2.0" the provider "must now block and release provider-side availability whenever an RTB request" is created or changes state [VERIFIED: same page]. This is an unusual and instructive design choice: **the hold is pushed to the supplier's system rather than kept in the platform**.
- **Lead time**: guests must send requests "at least three days before the check-in date"; RtB properties do not appear for closer dates [VERIFIED: same page].
- **Eligibility**: secondary sources report that RtB is limited to new properties and to apartments, holiday homes and villas [WIDELY REPORTED: https://docs.rentalsunited.com/hc/en-gb/articles/35086274489117-Understanding-request-to-book-flow-for-Booking-com, 2025]. ⚠

### 3.3 Vrbo

- Hosts "should aim to accept or decline booking requests within 24 hours"; "Declines after 24 hours are considered cancellations" and bring a cancellation fee; on a request "a hold is placed on your calendar to block other requests for those dates" [VERIFIED: https://help.vrbo.com/articles/IPM-About-booking-requests-for-integrated-accounts, live page, fetched 2026-10-21].
- For integrated property managers, "You can't accept or decline booking requests in the Vrbo Inbox"; the decision is made in the PMS and status can take up to 24 hours to update in the Vrbo dashboard [VERIFIED: same page]. That lag is itself a consistency risk.
- One channel-manager vendor reports a 48-hour timer for Vrbo "Quotehold" listings, conflicting with the 24-hour guidance [WIDELY REPORTED: https://support.hostaway.com/hc/en-us/articles/360039031293, undated]. Treat the window as platform- and integration-specific.

### 3.4 Architectural contrast

| Concern | Instant book | Request to book |
| --- | --- | --- |
| Who decides | Platform rules (host-set requirements) | Host, within 24 h |
| Inventory during decision | Atomically taken at booking | Airbnb/Vrbo block the dates; Booking.com standard RtB does not; RtB 2.0 pushes the block to the provider |
| Payment | Captured or authorized at booking | Authorized at request; released on expiry |
| Failure mode | Double booking if calendars are out of sync | Abandonment; price drift; guest books elsewhere |
| Extra states | None | PENDING_HOST, ACCEPTED_AWAITING_GUEST (Booking.com), EXPIRED, DECLINED |

[ASSUMPTION/JUDGEMENT, synthesised from 3.1–3.3]

**OTA vs hosted stays.** Request-to-book is a hosted-stays mechanism; hotels on OTAs confirm instantly against allotment. Booking.com's RtB exists for its homes segment and is confined to eligible apartments, holiday homes and villas. Booking Holdings reported roughly 3.9 million "homes, apartments, and other unique places to stay" against about 500,000 hotels, motels and resorts at 31 December 2025 [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18], so the hosted-stay mechanics now sit inside the largest OTA.

---

## PART 4: Delivering the reservation to the hotel

### 4.1 Pull with acknowledgement and fallback: Booking.com

- **Queue per provider**: "Booking.com maintains all incoming reservations specific to a provider using a dedicated queue"; for OTA-format integrations it "waits until you acknowledge receiving the reservations successfully" [VERIFIED: https://developers.booking.com/connectivity/docs/reservations-api/acknowledging-new-reservations-ota, live page, fetched 2026-10-21].
- **Acknowledge success or failure**: on success "Booking.com acknowledges and removes the reservation from the queue"; on failure "Booking.com keeps the reservations in the queue until you acknowledge successfully or until the timeout period." Acknowledgements use `HotelReservationID` with `ResID_Type="14"` [VERIFIED: same page].
- **Fallback to e-mail after 30 minutes**: if a reservation is not acknowledged (OTA) or retrieved (B.XML) within "a certain acknowledgement window (30 minutes) after the reservation's creation," Booking.com e-mails it to the property; the window can be extended to 24 hours via Connectivity Support. B.XML retrieval does not support acknowledgement. A 5-minute client timeout is recommended for pull and acknowledge calls [VERIFIED: https://developers.booking.com/connectivity/docs/reservations-api/reservations-overview, live page, fetched 2026-10-21]. ⚠
- **Polling cadence**: "call `GET OTA_HotelResNotif` once per twenty seconds" and "wait five seconds between `POST OTA_HotelResNotif` and the next `GET OTA_HotelResNotif`"; responses contain "only reservations which have not yet been acknowledged" by default; `limit` accepts 10–200 [VERIFIED: https://developers.booking.com/connectivity/docs/reservations-api/retrieving-new-reservations-ota, live page, fetched 2026-10-21].
- Modifications and cancellations use the separate `OTA_HotelResModifyNotif` endpoint [WIDELY REPORTED: search excerpt of https://developers.booking.com/connectivity/docs/reservations-api/retrieving-modifcancel-reservations-ota, 2026].

**Reading.** This is an **at-least-once delivery** design: unacknowledged messages are redelivered, so the PMS side must be idempotent on the Booking.com reservation ID, and the e-mail fallback means **two channels can deliver the same reservation** (XML and e-mail) [ASSUMPTION/JUDGEMENT].

### 4.2 Push with synchronous confirmation: Expedia Booking Notification and OTA messages

- Expedia's Booking Notification API delivers reservations by "HTTPS post of a SOAP formatted XML message" using `OTA_HotelResNotifRQ` for new bookings, `OTA_HotelResModifyNotifRQ` for changes and `OTA_CancelRQ` for cancellations; the partner responds "on the same connection" and, for a confirmed booking, returns "an additional HotelReservationID that will contain your confirmation number" [WIDELY REPORTED: search excerpt of https://developers.expediagroup.com/supply/lodging/docs/booking_apis/booking_notification/getting_started/integration-overview-landing-page/, 2026 — the page redirects to a login-gated portal on fetch].
- Partners must "acknowledge and accept all bookings created, modified, or cancelled and return confirmation number in the response" [WIDELY REPORTED: search excerpt of Expedia Booking Notification requirements page, 2026].
- **Expedia's pull APIs are closed to new partners.** Booking Retrieval and Booking Confirmation are "maintained for existing connections"; under that model the partner pulls and then sends back "the property's confirmation number for all bookings that have been retrieved" [WIDELY REPORTED: search excerpt of https://developers.expediagroup.com/supply/lodging/docs/booking_apis/booking_retrieval/getting_started/introduction, 2026]. ⚠
- A newer Expedia "reservation delivery" path uses event notifications; bookings delivered through the older APIs but not confirmed "will not trigger future event notifications" [WIDELY REPORTED: search excerpt of Expedia reservation-management page, 2026]. ⚠

### 4.3 The OpenTravel message family as implemented

- RateGain's channel-manager push spec: "Each message will contain only one reservation record" and "The PMS should process the message synchronously and respond with the confirmation of receipt and PMS confirmation number." The sample uses the `http://www.opentravel.org/OTA/2003/05` namespace and `ResStatus="Commit"` / `"Cancel"`, and carries several `HotelReservationID` elements with different `ResID_Type` codes [VERIFIED: https://developer.rategain.com/our-products/channel-manager/rg-bridge-supply-push/interface-specifications-reservation-notification-service/operations/reservation-notification/ota_hotelresnotifrq.md, live page, fetched 2026-10-21]. The sample XML is malformed in places; check the schema before quoting.
- SiteMinder's pmsXchange documentation (seen as search excerpts; the Confluence pages require login) says an undelivered message should be "retained in the partner PMS application's retry cycle and resent once the error is resolved," that resend "may need to be done manually upon expiry of retry cycle," that `OTA_HotelResModifyNotifRQ` is "used for a full overlay of the reservation," and that "No PCI sensitive data should be communicated within the OTA_HotelResNotifRQ" [WIDELY REPORTED: https://developer.siteminder.com/siteminder-apis/apps/api-reference/reservations, 2026].

| Pattern | Who initiates | Delivery guarantee | Where the confirmation number comes from | Fallback |
| --- | --- | --- | --- | --- |
| Pull + ack (Booking.com OTA) | Provider polls every ~20 s | At-least-once until ack | Provider may report its own; Booking.com ID is the key | E-mail after 30 min |
| Pull, no ack (Booking.com B.XML) | Provider polls | Retrieval counts as delivery | — | E-mail after 30 min |
| Push + sync response (Expedia BN, OTA ResNotif) | Platform posts | Retries by sender; manual resend after retry window | PMS returns it in the response | Extranet / call centre [ASSUMPTION/JUDGEMENT] |
| Extranet only | Hotel staff log in | Human | Hotel types it | E-mail / fax notification [ASSUMPTION/JUDGEMENT] |

### 4.4 Confirmation numbers and "booking not found at check-in"

The guest-facing symptom has several distinct root causes, each with a different architectural control [ASSUMPTION/JUDGEMENT, built on 4.1–4.3]:

| Root cause | Where it happens | Control |
| --- | --- | --- |
| Delivery never acknowledged; fallback e-mail ignored | Channel manager ↔ PMS | Ack-based queues; alert on unacked age; fallback with human follow-up |
| Delivered to channel manager, rejected by PMS (mapping error, closed room) | Channel manager → PMS | Error responses propagated back to the OTA; reconciliation report |
| Modification or cancellation applied in wrong order | Any hop | Version/sequence numbers on overlays; reject stale versions |
| Guest quotes OTA number, front desk searches PMS number | Front desk | Store all IDs (OTA, channel manager, PMS) on the PMS record and show them |
| Duplicate created on retry, then one copy cancelled | OTA ↔ supplier | Idempotency keys end to end (Part 5) |
| Platform booked against stale availability (overbooking) | OTA inventory | Faster ARI updates; overbooking playbook (Part 8) |

The multiplicity of identifiers is real and documented: one RateGain sample carries `UniqueID Type="14"` plus `HotelReservationID` values of `ResID_Type` 16, 13 and 14 [VERIFIED: RateGain page above]. The OpenTravel code list gives each type a meaning, but the spec itself was not fetched, so chapter writers should not assert type-code semantics without checking the OTA code tables.

**OTA vs hosted stays.** The whole delivery problem largely disappears for a single-unit host who manages the listing in the platform app: the platform calendar **is** the system of record, and the "confirmation" is the platform's own record. It reappears for professional hosts and property managers who connect through a PMS or channel manager (for example Vrbo integrated accounts, Part 3.3), and in a weaker form through iCal sync, which only exchanges blocked dates [ASSUMPTION/JUDGEMENT].

---

## PART 5: Holds, double-booking prevention and idempotency

### 5.1 Where double bookings come from

- **Booking.com's own list of overbooking causes**: "System outages preventing availability from being updated," "Incorrect auto-replenishment of cancelled reservations or room nights," "Late requests to close availability before bookings are made," "Non-XML rates being used in the reservation," and "The rate not being correctly mapped for ARI updates." Recommended mitigation: "increase the frequency of the periodic pull to 30 seconds or less"; and "As a Connectivity Partner, you cannot deactivate auto-replenishment" — properties must ask Booking.com support to turn off "Reopen closed rooms" [VERIFIED: https://developers.booking.com/connectivity/docs/con-faq-reservations-troubleshooting-overbookings, live page, fetched 2026-10-21].
- **Auto-replenishment is a two-writer problem**: when a guest cancels, the OTA reopens the room in its copy of inventory while the PMS may already have resold it elsewhere. [ASSUMPTION/JUDGEMENT]
- **iCal sync lag** for hosted stays: a vendor reports that iCal updates take "anywhere from 15 minutes to 24 hours depending on the platform" while direct API connections update within seconds [WIDELY REPORTED: https://www.hostfully.com/blog/sync-airbnb-vrbo-calendars/, 2025]. Host forum reports describe imports lagging by more than 24 hours and double bookings within 20 minutes of a feed update [WIDELY REPORTED: https://community.withairbnb.com/t5/Hosting/iCal-calendar-sync-lag-results-in-double-booking/m-p/387520, undated]. No official Airbnb refresh interval was found.

### 5.2 Inside one system: let the database refuse overlaps

- PostgreSQL's own documentation uses a room reservation to illustrate exclusion constraints: `EXCLUDE USING GIST (room WITH =, during WITH &&)` "will reject overlapping ranges only if the meeting room numbers are equal," producing `conflicting key value violates exclusion constraint` on the second insert [VERIFIED: https://www.postgresql.org/docs/current/rangetypes.html, PostgreSQL 18 docs, live page, fetched 2026-10-21].
- **Approaches compared** [ASSUMPTION/JUDGEMENT]:

| Approach | How it works | Fits | Risk |
| --- | --- | --- | --- |
| Store-enforced constraint (exclusion constraint, unique key on unit-night) | DB rejects the second overlapping write | Hosted stays: one unit, date ranges | Hot rows; sharding by unit needed at scale |
| Pessimistic row lock (`SELECT … FOR UPDATE` on unit-night rows) | Serialise writers per unit | Short critical sections | Lock contention on popular units; deadlocks on multi-night ranges unless locked in order |
| Optimistic concurrency (version column / compare-and-set on an allotment counter) | Read version, write if unchanged, retry | Hotel room-type allotments (counters, not unique units) | Retry storms on last-room races |
| Distributed lock / lease (Redis, ZooKeeper) | Lock the unit outside the DB | Coordinating across services | Unsafe for correctness without fencing (below) |
| Soft hold with TTL | Reserve for N minutes during checkout | Payment step, hold-and-resume | Abandoned holds suppress availability; hold expiry races |

- **Distributed locks are not a correctness mechanism on their own.** Kleppmann shows that a client whose lease expires during a process pause can still write: "You cannot fix this problem by inserting a check on the lock expiry just before writing back to storage." His remedy is a fencing token — "a fencing token is simply a number that increases" — checked by the storage layer, and "if you need locks for correctness, please don't use Redlock" [VERIFIED: https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html, published 2016-02-08]. Evidence-age note: ten years old, but the argument is about distributed-systems fundamentals and remains current.
- [ASSUMPTION/JUDGEMENT] For the book: **put the final no-overlap check in the store that owns the unit's calendar**, and treat any upstream lock or hold as an efficiency device that reduces failed attempts, not as the guarantee.

### 5.3 Holds as a product feature: Expedia Rapid hold and resume

- "Rapid Booking API's Hold and Resume functionality gives you the ability to support a 2-step booking model"; a single room can be put "on hold without an immediate charge"; "If the `hold` flag is used to book, no payment will be charged for the booking" [VERIFIED: https://developers.expediagroup.com/rapid/lodging/booking/hold-resume, live page, fetched 2026-10-21].
- "The booking will automatically be rolled back if left in the hold state without confirmation" and "If the booking is abandoned, it is automatically rolled back and the selected inventory is released." The page gives no fixed hold duration [VERIFIED: same page]. ⚠
- Eligibility is per rate: "The holdable flag in the Rapid Shop response indicates whether a particular rate is eligible for hold and resume" [VERIFIED: same page].
- Resume returns "HTTP 204 - no content," so the client must re-read the itinerary; after resume, itinerary-level cancel fails ("itinerary level cancel not supported") and room-level cancel is required [VERIFIED: same page].
- Retrieving a held booking "will provide additional links to resume and cancel," but "the Retrieve response will only contain minimal information" [VERIFIED: https://developers.expediagroup.com/rapid/lodging/manage-booking/about-mg-booking-api, live page, fetched 2026-10-21].

**Reading.** Hold-and-resume is the **compensable first step of a saga** exposed as an API: an affiliate can hold the room, run its own payment or fraud checks, and then resume (commit) or let it roll back [ASSUMPTION/JUDGEMENT].

### 5.4 Idempotency on the booking path

- **Expedia Rapid**: "Always use a unique `affiliate_reference_id` for each booking request"; a duplicate yields "An itinerary already exists with this affiliate reference id." For Lodging, Expedia recommends a 90-second timeout; "Any error returned within 90 seconds does not indicate the final status of the booking"; "most bookings will resolve into a confirmed booking within 13–30 seconds"; and if retrieval of a created itinerary fails, "retry the retrieval for 30 minutes before following up with Rapid API call center agents." The page sits in the Cars section but states that the errors apply across Lodging, Car, Flight and Activities [VERIFIED: https://developers.expediagroup.com/rapid/resources/error-responses-car, live page, fetched 2026-10-21]. ⚠
- A search excerpt of Expedia's Rapid guidance adds that if resending the same request "the same affiliate_reference_id should be used. This prevents accidental duplicate bookings," and that after a timeout the client should retrieve with `affiliate_reference_id` + `email`; one SDK reference states the field accepts up to 28 characters [WIDELY REPORTED: search excerpts of https://developers.expediagroup.com/rapid/resources/handle-booking-reqs-car and the Rapid Java SDK docs, 2026].
- **Stripe idempotency keys**: Stripe "saves the status code and body of the first request made with a given idempotency key after endpoint execution begins. Retries with the same key return the saved response, including `500` errors"; keys "are up to 255 characters long"; keys can be pruned "after they're at least 24 hours old"; the layer "compares incoming parameters to those of the original request and errors if they're not the same"; results are not saved when validation fails or "the request conflicts with another request that's executing concurrently" [VERIFIED: https://docs.stripe.com/api/idempotent_requests, live page, fetched 2026-10-21]. API v2 instead retries failed or partially failed work to completion [VERIFIED: same page]. ⚠
- **Stripe's design rationale**: on a lost response "the server simply replies with a cached result of the successful operation"; clients retry with the same key, with exponential backoff ("waits proportionally to 2^n") plus "jitter" [VERIFIED: https://stripe.com/blog/idempotency, published 2017-02-22]. Evidence age: nine years old; the principles are stable.
- **Airbnb Orpheus**: "Avoiding Double Payments in a Distributed Payments System — How we built a generic idempotency framework to achieve eventual consistency and correctness across our payments micro-service architecture," by Jon Chew and Ninad Khisti [VERIFIED: https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb via https://web.archive.org/web/20191217073850/, published 2019-04-16 — header only; body behind member wall]. Evidence age: seven years; may describe a replaced system.
- **Orpheus mechanism, as summarised secondhand**: a request is split into pre-RPC (record the request against its idempotency key, check whether it already completed), RPC (the external call, with no database work) and post-RPC (record the response, including failures) phases; there are no service calls in the pre- and post-RPC phases and no database interaction during the RPC phase; errors are classified retryable (5xx) vs non-retryable (4xx); idempotency data is read and written on the primary database, not replicas, because replication lag can cause duplicate payment requests [WIDELY REPORTED: https://biweekly-engineering.beehiiv.com/p/handling-double-payments-airbnb-biweekly-engineering-episode-32, 2024]. Chapter writers should quote the original if they can obtain it.
- A later Airbnb post on rebuilding payment orchestration reportedly describes workflows as DAGs of retryable idempotent steps built on Orpheus and payments that were "tightly coupled with the concept of a reservation for a stay" before the redesign [WIDELY REPORTED: search excerpt of "Rebuilding Payment Orchestration at Airbnb," airbnb.tech, c. 2021 — the URL returned 404 on fetch].

**Synthesis: idempotency at each hop** [ASSUMPTION/JUDGEMENT]

| Hop | Natural key | Documented example |
| --- | --- | --- |
| Client → platform "book" | Client-generated booking attempt ID | Stripe-style idempotency key |
| Platform → payment processor | Payment intent / idempotency key | Stripe; Airbnb Orpheus |
| Affiliate → OTA supply API | Affiliate reference ID | Expedia `affiliate_reference_id` |
| OTA → hotel PMS | OTA reservation ID + version | Booking.com `ResID_Value` + ack queue |
| PMS → OTA (confirmation) | PMS confirmation number | `HotelReservationID` in `OTA_HotelResNotifRS` |

**OTA vs hosted stays.** Hosted stays mostly need idempotency on the client→platform and platform→payments hops, because inventory and booking live in one platform. OTAs need it on **every** hop, including ones that cross company boundaries and legacy XML, where the "key" is a reservation ID plus a message version rather than a header [ASSUMPTION/JUDGEMENT].

---

## PART 6: Sagas, modifications and cancellations

### 6.1 Sagas and compensations across payment, inventory and supplier

- Microsoft's Saga pattern reference: a saga is "a sequence of local transactions"; if one fails, "the saga performs a series of compensating transactions"; a **pivot transaction** is "the point of no return," after which subsequent steps must be retryable and idempotent; sagas lack isolation, risking "lost updates," "dirty reads" and "fuzzy, or nonrepeatable, reads," with countermeasures including "Semantic lock," "Commutative updates," "Pessimistic view," "Reread values" and "Version files"; and "Compensating transactions might not always succeed" [VERIFIED: https://learn.microsoft.com/en-us/azure/architecture/patterns/saga, published 2025-02-25].
- The saga concept originates with Garcia-Molina and Salem, "Sagas," SIGMOD 1987 [WIDELY REPORTED: https://dl.acm.org/doi/10.1145/38713.38742, 1987 — not fetched].

**A reference booking saga** [ASSUMPTION/JUDGEMENT]:

| Step | Action | Compensation | Notes |
| --- | --- | --- | --- |
| 1 | Re-price / price check | — | Expedia exposes price check before booking and hard change |
| 2 | Hold inventory (internal or supplier hold) | Release hold | Expedia hold auto-rolls back; Booking.com RtB 2.0 pushes the hold to the provider |
| 3 | Authorize payment | Void authorization | Airbnb authorizes full amount on request |
| 4 | **Pivot:** commit reservation with the supplier / confirm on the platform | Cancel under a free-cancellation rule if possible; otherwise human remediation | After a supplier commit, "undo" may cost money (non-refundable rate) |
| 5 | Capture payment (or schedule capture) | Refund | Retryable, idempotent |
| 6 | Deliver to PMS, obtain confirmation number | — (retry, then fallback) | At-least-once; e-mail fallback |
| 7 | Notify guest / host | — | Retryable |

The key design decision is **where the pivot sits**: capture before supplier commit and you risk refunds; commit before capture and you risk unpaid bookings. Expedia's guidance that a 5xx within 90 seconds "does not indicate the final status of the booking" (5.4) shows why the pivot must be followed by a **reconcile-by-lookup** step, not a blind retry or a blind compensation [ASSUMPTION/JUDGEMENT].

### 6.2 Modifications

- **Expedia Rapid Hard Change** handles "date, room type, and occupancy modifications via API"; new dates "must be no more than one year after the original booked dates"; "Change or cancellation penalties are determined by the property"; "we cannot guarantee that nightly rates will be the same"; when money is owed "payment is required"; "You retain the original itinerary number through a hard change"; and "After committing the change, you should do an Itinerary Retrieve to confirm the changes have been applied." It is hidden for non-refundable bookings where the penalty equals the booking value, and cannot switch property-collect vs Expedia-collect models [VERIFIED: https://developers.expediagroup.com/rapid/lodging/manage-booking/hard-change, live page, fetched 2026-10-21]. ⚠
- Guest-name and other "soft" changes use a separate change call; "To make date changes, room type changes, and/or occupancy changes use the Hard Change API"; the Retrieve API "will reflect the latest check in/out dates in case of a change made by the property" [VERIFIED: https://developers.expediagroup.com/rapid/lodging/manage-booking/about-mg-booking-api, live page, fetched 2026-10-21]. Note that **the property can change dates**, so the platform must accept supplier-originated mutations.
- **Airbnb alterations require host approval**: "your host will receive a notification to approve or decline your request"; if declined or unanswered, the reservation stays the same; price differences are charged or refunded to the original payment method; "You can't make changes if your checkout has already passed"; Instant Book extensions must be requested at least 72 hours before checkout [VERIFIED: https://www.airbnb.com/help/article/913, live page, fetched 2026-10-21]. A search excerpt also reported limits of 3 changes per day and 10 per reservation; this was **not** confirmed on the fetched page.
- **Modification as a price-integrity risk**: one host forum thread reports an alteration request with a manually lowered nightly price that the host accepted unnoticed [WIDELY REPORTED: https://communitycenter.airbnb.com/forum/2d51a5c2-16fb-4016-833b-8f987dae813c/post/bGVnYWN5X2Nj_1828323, undated — single anecdote]. [ASSUMPTION/JUDGEMENT] Show the diff, not just the new state, to whoever approves a modification.

### 6.3 Guest cancellation policies

**Airbnb (short stays under 28 nights)** [VERIFIED: https://www.airbnb.com/help/article/475, live page, fetched 2026-10-21] ⚠

| Policy | Full refund until | After that |
| --- | --- | --- |
| Flexible | 24 h before check-in | Host paid nights stayed + 1 night |
| Moderate | 5 days before | Host gets 1 night + 50% of unspent nights |
| Limited (bookings from 1 Oct 2025) | 14 days before | 7–14 days: 50% refund; < 7 days: no refund of price |
| Firm | 30 days before | 7–30 days: 50%; < 7 days: no refund of price |
| Strict (invitation only) | — | 50% refund if ≥ 7 days before |
| Super strict 30 / 60 (invitation only) | — | 50% refund if ≥ 30 / 60 days before |
| Non-refundable option | — | Discounted; no refund |

- All standard policies include a window in which, if the booking is confirmed at least 7 days before check-in, guests can cancel for a full refund within 24 hours of confirmation. The non-refundable option is still subject to the 24-hour window "except for certain non-refundable hotel listings" [VERIFIED: same page].
- Long stays (28+ nights) have separate Firm and Strict long-term policies [VERIFIED: same page].
- The host's policy "may be overridden" by a Major Disruptive Event or Airbnb's Rebooking and Refund policy [VERIFIED: same page].

**Booking.com**: Booking.com is not a party to the booking: "When you make (or request) a booking, it's directly with the Service Provider – we're not a 'contractual party'"; "any cancellation/no-show fee and any refund will depend on the Service Provider's cancellation/no-show policy"; "Some bookings can't be canceled for free, while others can only be canceled for free before a deadline" [VERIFIED: https://www.booking.com/content/terms.html, "Updated August 25, 2025"]. ⚠

**Architectural reading** [ASSUMPTION/JUDGEMENT]:

- Hosted-stays policies are **platform-defined templates** chosen by the host, so the refund calculation lives in one platform service and is the same everywhere.
- OTA policies are **supplier-defined per rate plan** and arrive with the ARI feed. The OTA must snapshot the policy on the reservation at booking time, because the rate plan can change later. The Booking Holdings 10-K shows the OTA sometimes sells a more flexible policy than the supplier gave it (1.2), so the platform may need **two policies per reservation**: guest-facing and supplier-facing.
- Policies are functions of (booking time, check-in time, cancellation time, stay length, local time zone). Store them as versioned, testable rules, not as free text.

### 6.4 Force majeure overrides

- Airbnb's **Major Disruptive Events Policy** covers events that occur after booking, affect the reservation location, and prevent or legally prohibit the stay: public health emergencies (COVID-19 excluded), mandatory government travel restrictions, military actions, large-scale utility outages, and unforeseeable natural disasters. It excludes events affecting only the guest, illness, transport disruptions and "Weather or natural conditions that are common enough to be foreseeable in a given location." Guests may receive a refund, travel credit or other consideration regardless of the listing's policy; hosts can cancel without fees but "the calendar is blocked for the canceled dates" and they are not paid; it "is not an insurance policy" [VERIFIED: https://www.airbnb.com/help/article/1320, live page, fetched 2026-10-21]. The earlier "extenuating circumstances" policy name was replaced by this policy; the effective date was not stated on the page. ⚠
- [ASSUMPTION/JUDGEMENT] Architecturally, MDE is a **bulk, geo- and time-scoped override** applied to thousands of reservations at once. It needs an event registry (area polygon + date window), a batch job that finds affected reservations, and idempotent bulk refunds, not a per-booking support workflow.

**OTA vs hosted stays.** On an OTA in agency mode the hotel decides waivers; the OTA can ask but not compel, unless it absorbs the cost itself. On a hosted-stays platform the platform can override the host's policy unilaterally, because it holds the funds (1.2) [ASSUMPTION/JUDGEMENT].

---

## PART 7: Host cancellations, no-shows and penalties

### 7.1 Airbnb host cancellation fees

- Fees (minimum $50 USD): 50% of the reservation amount for nights not stayed if cancelled 48 hours or less before check-in or after check-in; 25% between 48 hours and 30 days; 10% more than 30 days out. Fee base is base rate, cleaning and pet fees, excluding taxes and guest fees [VERIFIED: https://www.airbnb.com/help/article/990, live page, fetched 2026-10-21]. ⚠
- Other consequences: the listing's calendar may be blocked for the affected dates "even when the fee is waived"; Superhost status may be lost; listing or account may be suspended. Fees may be waived for an MDE or a documented "valid reason"; even then the host gets no payout [VERIFIED: same page].

### 7.2 Vrbo

- "Declines after 24 hours are considered cancellations," with a fee and metric impact [VERIFIED: https://help.vrbo.com/articles/IPM-About-booking-requests-for-integrated-accounts, live page, fetched 2026-10-21].

### 7.3 Guest remedies when the host cancels: Airbnb AirCover for guests

- AirCover for guests covers serious issues including the host cancelling before check-in, inability to check in, and a listing significantly different from its advertisement. Guests should report within 72 hours of discovering a problem. If covered and unresolved, Airbnb first looks for comparable accommodation; otherwise a full or partial refund including service fees. It "doesn't cover travel related issues" [VERIFIED: https://www.airbnb.com/help/article/3218, live page, fetched 2026-10-21].
- The FY2025 10-K describes AirCover for guests as support "including host cancellations, inability to check-in, inaccurate listings, and a 24-hour safety support line" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026].

### 7.4 No-shows: Booking.com Reporting API

- A property can mark a no-show "from 00:00 (midnight, in property's local time) on the planned check-in date" until 48 hours after the planned check-out date, provided the reservation can still be modified and is not overbooked; it can be reported per room or for the whole reservation; a `waived_fees` flag says whether the property waives the no-show fee (and then Booking.com charges no commission); once marked, the reservation "can no longer be modified"; the booker receives an e-mail that the reservation has been cancelled [VERIFIED: https://developers.booking.com/connectivity/docs/reporting-api/b_xml-reporting/, live page, fetched 2026-10-21].
- Invalid credit cards can be reported "immediately after the reservation is made" until midnight on the check-in day; the booker is invited by e-mail and SMS to update the card, and "If the booker does not enter valid credit card details before the deadline, the property may cancel the reservation" [VERIFIED: same page].

**Reading.** No-show and invalid-card reporting are **supplier-originated state transitions** that flow back to the OTA and change commission. They need the same idempotency and versioning as inbound reservations [ASSUMPTION/JUDGEMENT].

**OTA vs hosted stays.** Hotels cancel rarely and mostly through overbooking; the remedy is relocation (Part 8). Hosts cancel more often and individually, so platforms use **behavioural penalties** (fees, calendar blocks, status loss) to protect booking reliability, which the platform can enforce because it controls the host's payout [ASSUMPTION/JUDGEMENT, built on 7.1–7.3].

---

## PART 8: Overbooking, relocation and walking guests

- When a room is overbooked, Booking.com's "Customer Service team will notify both the guest and the property to arrange either an alternative room or a relocation for the guest" [VERIFIED: https://developers.booking.com/connectivity/docs/con-faq-reservations-troubleshooting-overbookings, live page, fetched 2026-10-21]. The page does not say who pays.
- Agoda's partner hub reportedly requires a property with no rooms to find an alternative "of equal or higher standard" and provide transport at no extra cost [WIDELY REPORTED: https://www.partnerhub.agoda.com/?p=1429, undated — search excerpt only]. Hostelworld's guidance says the replacement should be the same or higher standard, in the same area, with the property covering any price difference [WIDELY REPORTED: https://support.hostelworld.com/knowledge/how-to-handle-overbookings, undated].
- Industry practice for "walking" a guest, per a PMS vendor's guide, is typically one night's room and tax at the relocation hotel, transport, a phone call and internet access, and the booking channel should be told about the relocation [WIDELY REPORTED: https://myfrontdesk.cloudbeds.com/hc/en-us/articles/218512777-emergency-process-to-handle-last-minute-overbookings, undated].
- [ASSUMPTION/JUDGEMENT] Architecturally, relocation creates a **linked reservation**: a new booking at another property, with the original reservation closed as "relocated" rather than "cancelled", the cost charged to the liable party, and the guest's loyalty, reviews and support history carried over. Few systems model this explicitly; most treat it as a support-ticket side effect, which breaks analytics and liability tracking.

**OTA vs hosted stays.** Hotels deliberately overbook to offset no-shows and walk guests when wrong; it is a known, priced operational practice. Hosted-stay "overbooking" is almost always an **accident** (sync lag, host error), and there is no equivalent second room on site, so the platform itself must find and fund a replacement (AirCover, 7.3) [ASSUMPTION/JUDGEMENT].

---

## PART 9: Consistency across channels

- The reservation and its availability consequence are replicated across: the platform; the channel manager; the PMS; other OTAs (through the channel manager); and, for homes, iCal feeds of other platforms. Each hop has its own latency: Booking.com recommends polling every 20 seconds and 30 seconds or less to reduce overbookings (4.1, 5.1); Booking.com's e-mail fallback triggers at 30 minutes (4.1); Vrbo PMS status can take up to 24 hours to show (3.3); iCal is reported at 15 minutes to 24 hours (5.1).
- [ASSUMPTION/JUDGEMENT] **The double-booking window is the sum of the slowest path**: booking on channel A → delivery to PMS/channel manager → availability push to channel B → channel B's cache refresh. Architects should measure this end-to-end window per supplier, not just per hop.
- [ASSUMPTION/JUDGEMENT] Recommended controls:
  - One **system of record per unit** (PMS for hotels; platform calendar for single-channel hosts), with every other copy treated as a cache.
  - **Reconciliation jobs** that compare platform reservations against PMS reservations daily (and pre-arrival for the next 48 hours), catching "booking not found at check-in" before the guest arrives.
  - **Version numbers** on every reservation message so out-of-order overlays are rejected.
  - **Close-out buffers** (stop selling the last unit on slow channels) where sync latency is high.

**OTA vs hosted stays.** OTA consistency is a *multi-system* problem with standards (OpenTravel XML) and contracts. Hosted-stay consistency is mostly a *single-system* problem, except for multi-listed homes, where the weakest link is iCal, which transfers only blocked dates — not prices, guest details or messages [WIDELY REPORTED: https://www.hostfully.com/blog/sync-airbnb-vrbo-calendars/, 2025].

---

## PART 10: Regulation touching the booking path — EU Package Travel Directive

- Directive (EU) 2015/2302 defines "travel service" to include "accommodation which is not intrinsically part of carriage of passengers and is not for residential purposes" [VERIFIED: http://publications.europa.eu/resource/celex/32015L2302, published 2015-12-11 (OJ); adopted 25 November 2015].
- A **package** arises where at least two different types of travel service are combined for the same trip, including where they are "purchased from separate traders through linked online booking processes where the traveller's name, payment details and e-mail address are transmitted from the trader with whom the first contract is concluded to another trader or traders and a contract with the latter trader or traders is concluded at the latest 24 hours after the confirmation of the booking of the first travel service" [VERIFIED: same text, Article 3(2)(b)(v)].
- A **linked travel arrangement** arises where a trader facilitates, among other things, "in a targeted manner, the procurement of at least one additional travel service from another trader where a contract with such other trader is concluded at the latest 24 hours after the confirmation of the booking of the first travel service" [VERIFIED: same text, Article 3(5)]. Traders facilitating LTAs "shall provide security for the refund of all payments they receive from travellers" if a service is not performed because of their insolvency (Article 19) [VERIFIED: same text].
- The package **organiser is responsible for performance** of all included services "irrespective of whether those services are to be performed by the organiser or by other travel service providers" (Article 13); travellers may terminate before the start against "an appropriate and justifiable termination fee" (Article 12) [VERIFIED: same text]. Member States applied the rules from 1 July 2018 [VERIFIED: same text].
- **Revision** ⚠: the European Commission states that Parliament and Council "reached a provisional political agreement on 2 December 2025" and that the Directive "has been amended by Directive (EU) 2026/1024 of 29 April 2026," with "28 months to transpose" [VERIFIED: https://commission.europa.eu/law/law-topic/consumer-protection-law/travel-and-timeshare-law/package-travel-directive_en, live page, fetched 2026-10-21]. Press and Council documents report that the revision removes linked travel arrangements as a separate category in favour of a unified package definition, and sets a 14-day refund deadline and refusable vouchers [WIDELY REPORTED: https://www.travelextra.ie/provisional-agreement-reached-on-package-travel-directive-revision/, 2025]. The amending directive's text was not fetched; verify against the Official Journal before writing.

**Architectural reading** [ASSUMPTION/JUDGEMENT]:

- The **24-hour, data-transmission test** turns a cross-sell feature into a legal classification. A platform that passes the guest's name, payment details and e-mail to a second trader (for example, a car rental or a flight after a hotel) within 24 hours may become a package organiser, liable for performance of the whole trip. That is a **booking-system design decision**: whether the cart is one checkout or several, whether payment tokens are shared, and how the system timestamps "confirmation of the booking of the first travel service."
- The booking system therefore needs to record, per trip: which services were combined, at which point of sale, the timestamps of each confirmation, and whether traveller data was transmitted — enough to decide the legal category after the fact.

**OTA vs hosted stays.** OTAs that sell flights, cars and hotels together (Booking.com offers flights in over 55 markets [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18]; Booking Holdings' "Connected Trip" strategy) are directly in scope. A hosted-stays platform selling only accommodation is not creating packages, but it enters scope as soon as it bundles other travel services such as experiences or transport in a qualifying way. The "not for residential purposes" qualifier matters for long stays [ASSUMPTION/JUDGEMENT; legal advice required].

---

## Key numbers

| Number | What | Source | Date |
| --- | --- | --- | --- |
| 24 h | Airbnb host window to accept or decline a request | airbnb.com/help/article/315 | live, fetched 2026-10-21 |
| up to 5 business days | Release of an Airbnb authorization after decline/expiry | airbnb.com/help/article/313 | live, fetched 2026-10-21 |
| 24 h + 24 h | Booking.com RtB: host window, then guest completion window | developers.booking.com RtB overview | live, fetched 2026-10-21 |
| ≥ 3 days | Booking.com RtB minimum lead time before check-in | same | live, fetched 2026-10-21 |
| 30 min (extendable to 24 h) | Booking.com unacknowledged-reservation e-mail fallback | developers.booking.com reservations overview | live, fetched 2026-10-21 |
| every 20 s; 5 s after POST | Booking.com recommended reservation polling | developers.booking.com retrieving new reservations | live, fetched 2026-10-21 |
| ≤ 30 s | Booking.com pull frequency recommended to reduce overbookings | developers.booking.com overbooking FAQ | live, fetched 2026-10-21 |
| 90 s | Expedia Rapid recommended booking timeout; errors within it are not final | developers.expediagroup.com error responses | live, fetched 2026-10-21 |
| 13–30 s | Typical Expedia Rapid booking resolution time | same | live, fetched 2026-10-21 |
| 30 min | Retry retrieval before contacting Rapid call centre | same | live, fetched 2026-10-21 |
| 1 year | Max shift of new dates in Expedia Hard Change | Rapid Hard Change page | live, fetched 2026-10-21 |
| 255 chars; ≥ 24 h | Stripe idempotency key length; minimum retention before pruning | docs.stripe.com idempotent requests | live, fetched 2026-10-21 |
| 50% / 25% / 10% (min $50) | Airbnb host cancellation fee by timing | airbnb.com/help/article/990 | live, fetched 2026-10-21 |
| 24 h (if booked ≥ 7 days out) | Airbnb guest free-cancellation window after confirmation | airbnb.com/help/article/475 | live, fetched 2026-10-21 |
| 72 h | AirCover: report issue to host after discovery | airbnb.com/help/article/3218 | live, fetched 2026-10-21 |
| business day after check-in | Airbnb host payout initiation | Airbnb FY2025 10-K | 2026 |
| $17,755M / $7,968M | Booking Holdings 2025 merchant / agency revenues | Booking Holdings FY2025 10-K | 2026-02-18 |
| ~500k hotels; ~3.9M homes | Booking.com properties at 31 Dec 2025 | same | 2026-02-18 |
| ~3.6M lodging properties (~2.4M Vrbo) | Expedia Group at 31 Dec 2025 | Expedia FY2025 10-K | 2026-02-13 |
| 24 h | PTD linked-booking / LTA time test | Directive (EU) 2015/2302 Art. 3 | 2015 |
| 28 months | Transposition of the 2026 PTD amendment | European Commission PTD page | live, fetched 2026-10-21 |

## Open questions / not verifiable

1. **Internal reservation state machines and calendar-locking designs** of Airbnb, Booking.com, Expedia, Agoda, Trip.com and Vrbo. No first-party engineering source was found. Any chapter statement about them must be framed as reference architecture.
2. **Airbnb Orpheus details** beyond the title, authors and date. The body was not readable; the mechanism comes from a 2024 newsletter. Whether Orpheus is still in use in 2026 is unknown.
3. **Airbnb's iCal import refresh interval.** No official figure; only forum reports and vendor estimates.
4. **Expedia supply-side delivery details** (Booking Notification retry schedule, fallback channel when a hotel does not confirm, the newer reservation-delivery webhooks). The pages are behind a login-gated portal; only search excerpts were seen.
5. **Booking.com's contractual relocation obligation for overbookings** — who pays and to what standard. Not found in fetchable partner terms.
6. **OpenTravel `ResID_Type` code semantics** and the official `OTA_HotelResNotifRQ` schema. The OpenTravel specification was not fetched.
7. **Airbnb alteration limits** (3 per day / 10 per reservation) appeared only in a search excerpt and not on the fetched help page.
8. **The final text of Directive (EU) 2026/1024** amending the PTD, including whether LTAs are fully removed. Only the Commission's summary page and press coverage were seen.
9. **Agoda and Trip.com** booking-path behaviour (holds, delivery, cancellation). No primary source was researched in this session.
10. **Measured rates** (overbooking frequency, "booking not found" incidents, cancellation rates) — none of the companies publish them; Booking Holdings only says the 2025 cancellation rate "was lower than the prior year."

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Form 10-K for fiscal year 2025 | Airbnb, Inc. | 2026 | https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm |
| Form 10-K for fiscal year 2022 | Airbnb, Inc. | 2023 | https://www.sec.gov/Archives/edgar/data/1559720/000155972023000003/abnb-20221231.htm |
| Form 10-K for fiscal year 2025 | Booking Holdings Inc. | 2026 | https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm |
| Form 10-K for fiscal year 2025 | Expedia Group, Inc. | 2026 | https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm |
| Instant Book for guests and hosts | Airbnb Help Center | live | https://www.airbnb.com/help/article/523 |
| What happens if your home reservation request is declined or expires | Airbnb Help Center | live | https://www.airbnb.com/help/article/315 |
| What happens to your payment when a home reservation request is declined or expires | Airbnb Help Center | live | https://www.airbnb.com/help/article/313 |
| Cancellation policies for your listing | Airbnb Help Center | live | https://www.airbnb.com/help/article/475 |
| Major Disruptive Events Policy | Airbnb Help Center | live | https://www.airbnb.com/help/article/1320 |
| Host cancellation fees | Airbnb Help Center | live | https://www.airbnb.com/help/article/990 |
| AirCover for guests | Airbnb Help Center | live | https://www.airbnb.com/help/article/3218 |
| Change the dates of your home reservation | Airbnb Help Center | live | https://www.airbnb.com/help/article/913 |
| Avoiding Double Payments in a Distributed Payments System | Jon Chew, Ninad Khisti / Airbnb Engineering (archived copy) | 2019 | https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb |
| Handling Double Payments at Airbnb (Episode 32) | Biweekly Engineering newsletter | 2024 | https://biweekly-engineering.beehiiv.com/p/handling-double-payments-airbnb-biweekly-engineering-episode-32 |
| About booking requests for integrated accounts | Vrbo Help | live | https://help.vrbo.com/articles/IPM-About-booking-requests-for-integrated-accounts |
| Understanding the Reservations API | Booking.com Connectivity | live | https://developers.booking.com/connectivity/docs/reservations-api/reservations-overview |
| Acknowledging new reservations (OTA) | Booking.com Connectivity | live | https://developers.booking.com/connectivity/docs/reservations-api/acknowledging-new-reservations-ota |
| Retrieving new reservations (OTA) | Booking.com Connectivity | live | https://developers.booking.com/connectivity/docs/reservations-api/retrieving-new-reservations-ota |
| Troubleshooting overbookings | Booking.com Connectivity | live | https://developers.booking.com/connectivity/docs/con-faq-reservations-troubleshooting-overbookings |
| Request to Book overview | Booking.com Connectivity | live | https://developers.booking.com/connectivity/docs/request-to-book/overview |
| B.XML Reporting API (no-show, invalid card) | Booking.com Connectivity | live | https://developers.booking.com/connectivity/docs/reporting-api/b_xml-reporting/ |
| Customer terms of service | Booking.com | 2025 (updated 25 Aug 2025) | https://www.booking.com/content/terms.html |
| Hold and Resume | Expedia Group Developer Hub (Rapid) | live | https://developers.expediagroup.com/rapid/lodging/booking/hold-resume |
| About the Manage Booking API | Expedia Group Developer Hub (Rapid) | live | https://developers.expediagroup.com/rapid/lodging/manage-booking/about-mg-booking-api |
| Hard Change | Expedia Group Developer Hub (Rapid) | live | https://developers.expediagroup.com/rapid/lodging/manage-booking/hard-change |
| Common error responses | Expedia Group Developer Hub (Rapid) | live | https://developers.expediagroup.com/rapid/resources/error-responses-car |
| Booking Notification API integration overview (search excerpt) | Expedia Group | live | https://developers.expediagroup.com/supply/lodging/docs/booking_apis/booking_notification/getting_started/integration-overview-landing-page/ |
| Booking Retrieval and Booking Confirmation APIs (search excerpt) | Expedia Group | live | https://developers.expediagroup.com/supply/lodging/docs/booking_apis/booking_retrieval/getting_started/introduction |
| OTA_HotelResNotifRQ (RG Bridge supply push) | RateGain | live | https://developer.rategain.com/our-products/channel-manager/rg-bridge-supply-push/interface-specifications-reservation-notification-service/operations/reservation-notification/ota_hotelresnotifrq.md |
| Reservations API reference (search excerpt) | SiteMinder | live | https://developer.siteminder.com/siteminder-apis/apps/api-reference/reservations |
| Understanding request to book flow for Booking.com | Rentals United | 2025 | https://docs.rentalsunited.com/hc/en-gb/articles/35086274489117-Understanding-request-to-book-flow-for-Booking-com |
| Vrbo request handling | Hostaway support | undated | https://support.hostaway.com/hc/en-us/articles/360039031293 |
| How to Sync Your Airbnb and Vrbo Calendars | Hostfully | 2025 | https://www.hostfully.com/blog/sync-airbnb-vrbo-calendars/ |
| iCal calendar sync lag results in double booking | Airbnb Community Center (host forum) | undated | https://community.withairbnb.com/t5/Hosting/iCal-calendar-sync-lag-results-in-double-booking/m-p/387520 |
| Emergency process to handle last-minute overbookings | Cloudbeds | undated | https://myfrontdesk.cloudbeds.com/hc/en-us/articles/218512777-emergency-process-to-handle-last-minute-overbookings |
| How to handle overbookings | Hostelworld support | undated | https://support.hostelworld.com/knowledge/how-to-handle-overbookings |
| Agoda partner hub (overbooking) | Agoda | undated | https://www.partnerhub.agoda.com/?p=1429 |
| Idempotent requests | Stripe API reference | live | https://docs.stripe.com/api/idempotent_requests |
| Designing robust and predictable APIs with idempotency | Brandur Leach / Stripe | 2017 | https://stripe.com/blog/idempotency |
| Saga design pattern | Microsoft Azure Architecture Center | 2025 | https://learn.microsoft.com/en-us/azure/architecture/patterns/saga |
| Sagas (SIGMOD '87) | Hector Garcia-Molina, Kenneth Salem / ACM | 1987 | https://dl.acm.org/doi/10.1145/38713.38742 |
| How to do distributed locking | Martin Kleppmann | 2016 | https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html |
| Range Types — Constraints on Ranges | PostgreSQL 18 documentation | live | https://www.postgresql.org/docs/current/rangetypes.html |
| Directive (EU) 2015/2302 on package travel and linked travel arrangements | European Parliament and Council (EU Publications Office) | 2015 | http://publications.europa.eu/resource/celex/32015L2302 |
| Package Travel Directive | European Commission | live | https://commission.europa.eu/law/law-topic/consumer-protection-law/travel-and-timeshare-law/package-travel-directive_en |
| Provisional agreement reached on Package Travel Directive revision | Travel Extra (Ireland) | 2025 | https://www.travelextra.ie/provisional-agreement-reached-on-package-travel-directive-revision/ |
