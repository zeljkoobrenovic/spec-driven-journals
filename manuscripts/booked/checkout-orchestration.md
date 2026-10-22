{id: checkout-orchestration}
# 21. Turning an Offer Into a Booking: Checkout Orchestration

![Turning an Offer Into a Booking: Checkout Orchestration — logo](stays-marketplace-architecture/posts/21-checkout-orchestration/assets/images/21-checkout-orchestration/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow a stays booking from "Book" to a promised night: quote re-validation, holds, payment authorization, supplier confirmation, instant book and request to book, the booking saga with its pivot, idempotency keys from the app to the hotel, unknown outcomes, policy disclosure, guest details and the placement of risk checks.

> **WHY THE BUSINESS CARES:** Checkout is where the marketplace converts the money spent on acquisition, search and ranking into revenue, and where it most easily destroys trust. A guest who is charged twice, told "sold out" after paying, or left without a confirmation calls support, disputes the charge and books elsewhere next time.

> **WHY ARCHITECTS SHOULD CARE:** A booking spans the inventory store, the payment provider, the partner's property management system and the reservation store with no shared transaction. Whether one guest intention produces exactly one reservation and one charge depends on who mints the idempotency key, where the point of no return sits, and what happens when a call neither succeeds nor fails.

> **KEY POINTS:**
>
> * **A booking is a saga with one pivot, and the pivot is a design decision.** Before the pivot, every step must have a compensation that really undoes it: release the hold, void the authorization. After it, every step must be retryable until it succeeds. Placing the pivot differently for agency, merchant, facilitated and request-to-book flows is legitimate; leaving it implicit is how bookings end up paid but not confirmed, or confirmed but not paid.
> * **One guest intention needs one key, minted by the server and carried to every hop.** A checkout attempt created when the guest enters checkout, bound to the quote and the hold, becomes the idempotency key for the reservation, the payment, the inventory commit and the supplier message. Keys minted per HTTP request let a retry look like a new purchase, which is how Roomstead created 212 duplicate bookings in 40 minutes.
> * **"Unknown" is a state, not an error.** A payment or supplier call that times out may have succeeded. The saga must record the unknown outcome, show the guest an honest "confirming" state, and resolve it by looking up the result with the same key. Compensating an unknown outcome refunds bookings that exist; retrying it with a new key creates bookings that should not.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Built for Sunny Days** — checkout works at normal latency, but a payment provider that slows from two seconds to forty turns client retries into duplicate reservations and duplicate charges.
> * **Phantom Availability** — a checkout that does not re-validate the quote and commit against the inventory of record sells nights that search showed but that no longer exist.
> * **Policy Spaghetti** — when checkout shows one cancellation policy, the payment plan uses another and the partner receives a third, every later change becomes a dispute about which one the guest agreed to.

Everything before checkout is reversible: a search can be repeated, a ranking recomputed, and nobody has promised anything. Checkout is where the marketplace makes promises to three parties at once: to the guest that the night is theirs at the stated price and terms, to the property or host that a guest is coming, and to the payment network that an amount is owed. **Checkout is the first step whose mistakes cannot be undone by recomputing**, because each of those promises lands in a system the marketplace does not control.

A stays marketplace usually sells a copy of someone else's inventory, often collects money for someone else, and confirms a service delivered weeks later by a hotel on its property management system (PMS) or by a host on a phone, with money moving through payment service providers (PSPs) that have their own timeouts. The booking path crosses at least three systems with independent failure modes, so it cannot be one transaction. It is a **saga**: a sequence of local steps, each committed on its own, with defined ways to undo them.

This chapter opens Part V ([Part V — BOOKING: Making and Keeping the Reservation](#part-5)) and turns the quote handed over by [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) into a confirmed reservation. It owns the **booking saga**, the **idempotency key** for stays, **instant book** and **request to book**. It uses, without re-teaching, the commit point and holds of [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity), the price check of [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine), the payment arrangement of [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models) and the payment plan of [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments). Delivery to the property and everything after confirmation belong to [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle).

{id: checkout-orchestration--setting-the-scene-at-corvane-212-bookings-nobody-made-twice}
## Setting the Scene at Corvane: 212 Bookings Nobody Made Twice

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), takes about **45 million** reservations a year on Roomstead, its accommodation marketplace (about 123,000 a day), and roughly 19,000 a day on Nookaway, its hosted-stays marketplace. In January 2027 Roomstead's checkout had two layers. **Turnstile**, a Java checkout API on AWS built in 2021, served the apps and web and called Corvane Payments for merchant ("Pay with Roomstead") bookings. Behind it, the checkout module of Keystone, the monolith that still owns Roomstead reservations, re-priced the booking and created the reservation. Turnstile's booking endpoint accepted an `Idempotency-Key` header and remembered each key for 24 hours.

On Thursday **14 January 2027**, at the start of the January booking peak, the card-authorization path through Corvane Payments slowed down.

| Time (CET) | Event |
| --- | --- |
| 19:48 | Authorization latency at the median rises from about 1.4 seconds to 18 seconds; the 99th percentile passes 40 seconds |
| 19:52 | Roomstead app requests to Turnstile start to exceed the app's 20-second timeout. The app's networking layer, changed in a release on 7 January to retry timed-out requests up to twice on poor mobile networks, re-sends the booking request |
| 19:52–20:32 | Each retry is built by the app's request builder, which **generates a new idempotency key for every request**. Turnstile sees a new key, finds no record and starts a second booking for the same guest, quote and room |
| 20:32 | Authorization latency recovers |
| 20:41 | First support contacts: "I was charged twice" |
| 21:15 | Corvane Payments' duplicate-charge rule (same card, same amount, same merchant within ten minutes) flags the pattern |
| 15–18 January | Cleanup: duplicates identified, canceled with properties, refunded |

The result was **212** duplicate reservations, **198** of them with duplicate charges: Pay with Roomstead bookings on which the guest was charged twice and Corvane Payments issued two virtual cards to the hotel. The other 14 were pay-at-property bookings: no money had moved, but Keystone delivered two reservations to each hotel, each consuming a room until it was canceled. On non-refundable rates, whose virtual cards are active from booking, a few hotels charged both cards before the cleanup reached them.

Leila Haddad, Head of Payments and Finance Engineering, made the first point in the review: **the server had done exactly what it was told.** Every request carried a valid, unseen key. The key protected against a repeat of the same HTTP request, which the app never sent, not against a second purchase of the same intention.

Mariana Costa, who had joined as Group Chief Architect that month, made the second. When the first request timed out, neither the app nor Turnstile knew whether a booking existed. The design had two outcomes, success and failure, and the world had three. **The question for the architecture forum was not "how do we fix the app's retry" but "what is one booking, who names it, and what does every system do when it cannot tell whether it happened?"**

![Before and after: keys minted per request turn three retries into three reservations and double charges; one server-minted attempt key carried by every retry yields exactly one reservation.](stays-marketplace-architecture/posts/21-checkout-orchestration/assets/images/21-checkout-orchestration/21-one-intention-one-key.jpeg)

**Figure 1:** *A key minted per request lets each retry look like a new purchase, which is how 212 duplicate bookings appeared; one server-minted checkout attempt key makes every retry the same booking.*

{id: checkout-orchestration--concepts-from-quote-to-reservation}
## Concepts: From Quote to Reservation

- A **quote** is a priced offer with an identity, an itemized breakdown, the versions of the data it was computed from and a validity window ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) defines it). Checkout starts from a quote ID, not from a price passed by the client.
- **Re-validation** (or **price check**) re-computes the selected quote from the system of record and returns one of three designed outcomes: unchanged within tolerance, changed (shown to the guest with the old price and a reason), or unavailable ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine) owns the mechanics). At Corvane a successful check makes the quote **binding for 15 minutes**.
- An **inventory hold** reserves the unit or room type for the minutes the guest spends paying. It is an efficiency device; the guarantee is the commit against the allocation ledger ([Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity)). Nookaway holds a listing for 10 minutes from the start of payment, extended once to 20 minutes on a 3-D Secure challenge; Roomstead holds a room type for 15 minutes.
- A **checkout attempt** is one guest's intention to buy one quote, recorded by the server when the guest enters checkout. It is the unit this chapter protects: one attempt may produce at most one reservation.
- A **booking saga** is the sequence of local steps that turns an attempt into a confirmed reservation, each with either a compensation (a step that undoes it) or a guarantee that it will be retried until it succeeds. The term comes from Hector Garcia-Molina and Kenneth Salem's 1987 paper on long-lived transactions ([Garcia-Molina and Salem, 1987](https://dl.acm.org/doi/10.1145/38713.38742)).
- The **pivot** is the saga's point of no return. Microsoft's architecture guidance defines the pivot transaction as "the point of no return": steps after it must be retryable and idempotent, because the saga can no longer be compensated as a whole ([Microsoft Azure Architecture Center, 2025](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga)).
- An **idempotency key (stays)** is an identifier every system on the booking path uses to recognize a repeated request and return the original result instead of repeating the effect. In stays it must survive several hops, some across company boundaries and legacy XML, where the "key" is a reservation ID plus a message version.

{id: checkout-orchestration--instant-book-and-request-to-book}
### Instant book and request to book

Two booking modes decide whether the saga waits for a human.

**Instant book** confirms the reservation when the guest completes payment, against rules the host or property set in advance (minimum stay, lead time, guest requirements). Hotel bookings are instant; on hosted-stays marketplaces it is a host choice. Airbnb's help center describes it as letting guests "book immediately without needing to send a request to the host for approval" ([Airbnb Help Center, article 523](https://www.airbnb.com/help/article/523), n.d., fetched October 2026).

**Request to book** inserts a host decision between payment and confirmation. The documented designs differ in instructive ways:

| Platform (live documentation, fetched October 2026) | Host window | Money during the request | Inventory during the request |
| --- | --- | --- | --- |
| Airbnb ([article 315](https://www.airbnb.com/help/article/315), [article 313](https://www.airbnb.com/help/article/313)) | 24 hours, then the request expires | An authorization "for the full amount of the reservation"; on decline or expiry it is removed, which "may take up to 5 business days" | Not stated on the pages fetched |
| Booking.com Request to Book for homes ([Connectivity docs](https://developers.booking.com/connectivity/docs/request-to-book/overview)) | 24 hours to accept or decline; then the guest has 24 hours to complete | Payment pre-authorized when the request is created | Standard requests do not block Booking.com inventory, so price can change; under "RtB 2.0" the provider "must now block and release provider-side availability" as the request changes state. Requests must be sent at least three days before check-in |
| Vrbo integrated accounts ([Vrbo Help](https://help.vrbo.com/articles/IPM-About-booking-requests-for-integrated-accounts)) | Aim for 24 hours; "Declines after 24 hours are considered cancellations" | Not stated | "a hold is placed on your calendar to block other requests for those dates"; for integrated managers the decision is made in the property management system |

Request to book turns a minutes-long saga into a day-long one, so the hold, the authorization and the quote need validity windows that match the host's window. **Where the hold lives is a choice**: Booking.com's RtB 2.0 pushes it into the supplier's system, Vrbo keeps it on its own calendar. And for an iCal-synchronized listing, a host confirmation turns a silent double booking into a declined request ([One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync)). At Corvane, instant book is enabled on **68%** of Nookaway listings; the rest are request to book with a 24-hour host window.

{id: checkout-orchestration--architecture-the-booking-saga}
## Architecture: The Booking Saga

The booking path has eight components, each with its own owner, failure mode and answer to "what happens if I am called twice".

![A checkout attempt hub with a key tag calling price composition, risk and screening, the allocation ledger, the payment orchestrator and the reservation store, which sends events through an outbox to supplier delivery and notifications.](stays-marketplace-architecture/posts/21-checkout-orchestration/assets/images/21-checkout-orchestration/21-booking-saga-components.jpeg)

**Figure 2:** *The booking path as one coordinator and seven participants. The checkout attempt service owns the saga and its state; each participant owns one local step and recognizes repeats by the attempt's key. Everything after the reservation is confirmed leaves through an outbox as events, outside the guest's wait.*

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Checkout attempt service** (the saga coordinator) | Create one attempt per guest intention, run the steps in order, record each outcome, decide compensations | Attempt state, step log, the attempt ID as idempotency key | Compute prices, policies or risk itself |
| **Price composition** ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection)) | Re-validate the quote by ID and return unchanged, changed or unavailable | The binding quote and its window | Introduce a change the earlier surfaces did not show |
| **Eligibility and policy** | Check that this guest may book this offer now; freeze the terms the guest is agreeing to | Terms snapshot: cancellation policy version, house rules, payment arrangement, display policy version | Let checkout copy policy text from its own templates |
| **Risk and screening** ([Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud), [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety)) | Return allow, challenge, review or deny with reasons, within a latency budget | Models, rules, decision log | Block silently; every deny carries a reason code |
| **Allocation ledger** ([Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity)) | Place holds and commit nights against the inventory of record | The no-overlap or no-overdraw guarantee | Accept a commit without the attempt's key |
| **Payment orchestrator** ([Paying for a Future Night: Payment Orchestration for Stays](#stay-payments)) | Execute the payment plan: authorize, capture, store credentials, issue virtual cards | Obligation state, PSP idempotency keys | Decide whether the booking exists |
| **Reservation store** (Keystone for Roomstead, Burrow for Nookaway in 2027) | Create the reservation, version it, publish events | The reservation aggregate ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)) | Create a second reservation for an attempt that already has one |
| **Supplier delivery** ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)) | Deliver the reservation to the PMS, channel manager or host and record acknowledgement | Delivery state per version | Sit inside the guest's synchronous wait unless the supply model requires it |

Two interface choices matter more than the boxes.

1. **Participants recognize repeats, so the coordinator need not be perfect.** The coordinator will crash, time out and re-run steps; every participant must treat a second call with the same key as a request for the first call's result. Airbnb's 2026 description of Skipper, its embedded durable workflow engine, states the contract plainly: "Actions may execute more than once in edge cases", and failures run compensations in reverse order ([Airbnb Engineering, 2026](https://airbnb.tech/infrastructure/skipper-building-airbnbs-embedded-workflow-engine/)).
2. **The reservation is created before the money moves, in a pending state.** The pending reservation, keyed by the attempt and confirmed at the pivot, is invisible to the property, but it gives a payment whose outcome is unknown somewhere to be recorded.

{id: checkout-orchestration--the-saga-step-by-step}
### The saga, step by step

The reference saga below is my recommendation for an instant-book stay paid at booking; the variants follow.

| Step | Action | Compensation | Key used | Timeout behavior |
| --- | --- | --- | --- | --- |
| 1 | Create the checkout attempt from the quote ID; return the attempt ID to the client | Expire the attempt | Server-minted attempt ID | Client may repeat; the same attempt is returned for the same session and quote |
| 2 | Re-validate the quote; freeze the terms snapshot | — (read only) | Attempt ID | Fail closed: no binding quote, no checkout |
| 3 | Pre-payment risk decision | — | Attempt ID | Fail open to "review after booking" for low-value, known guests; fail closed above a threshold |
| 4 | Place the inventory hold | Release the hold | Attempt ID | Holds expire by condition; a timed-out hold call is retried with the same key |
| 5 | Create a pending reservation | Close it as expired ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)'s "declined or expired") | Attempt ID | Idempotent on the attempt ID |
| 6 | Authorize payment (with Strong Customer Authentication where needed) | Void the authorization | Attempt ID + obligation | A timeout is an **unknown outcome**, resolved by lookup |
| 7 | **Pivot:** commit the nights and confirm the reservation | Not compensable as a whole; a later failure becomes a cancellation under the frozen terms or a relocation | Attempt ID | Commit is retried with the same key until it returns |
| 8 | Capture or schedule the charge per the payment plan | Refund (a business action, not a saga compensation) | Obligation key | Retried until success |
| 9 | Deliver to the supplier, notify guest and host | — | Reservation ID + version | Asynchronous, at least once, from the outbox |

The hard part is ordering steps 6 and 7. Commit first, and an authorization failure leaves a confirmed reservation to cancel, a visible event on a hotel's PMS. Authorize first, and a commit that fails because someone took the last room costs only a void. **Authorize, then commit, then capture** keeps the steps before the pivot cheap to undo.

![Swimlanes for guest, checkout attempt, allocation ledger, payment and reservation store, with the attempt ID returned before Book and a pivot line at the commit separating steps that can be undone from steps that are retried.](stays-marketplace-architecture/posts/21-checkout-orchestration/assets/images/21-checkout-orchestration/21-booking-saga-sequence.jpeg)

**Figure 3:** *The booking saga for an instant-book stay paid at booking. The guest receives the attempt ID before pressing "Book", so every repeat of that press carries the same key. Before the commit, every step can be undone cheaply; after it, every step is retried until it succeeds.*

{id: checkout-orchestration--where-the-pivot-sits}
### Where the pivot sits

| Flow | Steps before the pivot | Pivot | Cost of being wrong after the pivot |
| --- | --- | --- | --- |
| **Agency, pay at property** (Roomstead, 70% of room nights) | Re-validate, optional card guarantee check, hold | Commit and confirm on the platform | A canceled reservation delivered to the hotel; no money to return |
| **Merchant, pay now** (Pay with Roomstead) | Re-validate, hold, authorize | Commit and confirm; virtual card issued after | A refund and a voided card; on non-refundable rates with an active card, recovery from the hotel |
| **Facilitated, pay now** (Nookaway) | Re-validate, screen, hold, authorize | Commit on Almanac and confirm | Refund; the host's calendar was blocked and may have lost another booking |
| **Facilitated, Pay Later** (Nookaway) | Re-validate, screen, hold, set up a chargeable credential | Commit and confirm with a scheduled charge | A confirmed booking that may never be paid; [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments) owns the deferred charge |
| **Request to book** (Nookaway, Booking.com homes) | Re-validate, screen, authorize, host decision | Host acceptance | Before acceptance, a void; after, as facilitated |
| **Pull-model supply** (bedbank or affiliate API) | Re-validate with the supplier, authorize | **The supplier's booking call** | Supplier cancellation fees on non-refundable rates; manual remediation |

In the last row the pivot leaves the marketplace. When Roomstead sells rooms from **Brightwell Beds**, the Singapore-based bedbank it signed in June 2027 ([Describing a Stay: Content, Media and Property Mapping](#content-and-media)), the booking exists only when Brightwell's API says it does. Hotelbeds documents the commit-time recheck such suppliers require: a rate marked `RECHECK` must pass CheckRate before booking ([Hotelbeds booking workflow](https://developer.hotelbeds.com/documentation/hotels/booking-api/workflow/), n.d., fetched 2026). Expedia Group's Rapid API, which sells Expedia inventory to affiliates, offers a compensable first step across a company boundary: a booking made with a `hold` flag is not charged and is "automatically rolled back if left in the hold state without confirmation" ([Expedia Group Rapid, Hold and Resume](https://developers.expediagroup.com/rapid/lodging/booking/hold-resume), n.d., fetched October 2026).

![Four tracks for agency, merchant, request-to-book and pull-model flows, each with a one-way pivot gate at a different position, undoable steps before it and retried steps after it.](stays-marketplace-architecture/posts/21-checkout-orchestration/assets/images/21-checkout-orchestration/21-pivot-moves-by-flow.jpeg)

**Figure 4:** *The pivot moves with the payment model and booking mode; for pull-model supply it leaves the marketplace and becomes the supplier's booking call.*

{id: checkout-orchestration--synchronous-or-asynchronous-supplier-confirmation}
### Synchronous or asynchronous supplier confirmation

Most hotel bookings are confirmed on the platform's own inventory copy and delivered to the hotel afterwards, asynchronously ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)). For pull-model supply the supplier's confirmation is the pivot, and its latency is the guest's wait. Expedia's Rapid documentation recommends a 90-second booking timeout, says "most bookings will resolve into a confirmed booking within 13–30 seconds", warns that "any error returned within 90 seconds does not indicate the final status of the booking", and tells partners to "retry the retrieval for 30 minutes" before contacting its call center ([Expedia Group Rapid, Common error responses](https://developers.expediagroup.com/rapid/resources/error-responses-car), n.d., fetched October 2026; the page sits in the car section but states that it applies to lodging).

The rule I use: **keep the guest's synchronous wait to the steps the platform controls, and make every longer wait an explicit pending state.** "We are confirming your booking with the property" and a status page beat an error at second 20 for a booking that confirms at second 25.

{id: checkout-orchestration--idempotency-end-to-end}
## Idempotency End to End

{id: checkout-orchestration--who-mints-the-key}
### Who mints the key

Stripe's API gives the reference semantics for one API: it saves the first response for a key, returns it to retries "including `500` errors", "compares incoming parameters to those of the original request and errors if they're not the same", and may prune keys "after they're at least 24 hours old" ([Stripe API reference, Idempotent requests](https://docs.stripe.com/api/idempotent_requests), n.d., fetched October 2026). Brandur Leach's 2017 Stripe post adds the client side: retry with the same key, with exponential backoff and jitter ([Stripe, 2017](https://stripe.com/blog/idempotency)). The IETF's draft `Idempotency-Key` header specifies the same behavior: a completed duplicate gets the previous result, a concurrent duplicate gets a conflict error, and a reused key with a different payload gets HTTP 422 ([draft-ietf-httpapi-idempotency-key-header-07](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/), October 2025; an Internet-Draft, not yet an RFC).

All three assume the client sends the same key for the same intention. At Roomstead **the client minted the key at the wrong layer**: per HTTP request, not per purchase. A client-minted key is safe only if it is generated once per intention and survives restarts and every retry layer; in mobile apps the retry logic lives in shared HTTP code whose authors do not know which calls are purchases.

My recommendation is to **let the server mint the key for purchases**. The client starts checkout with a quote ID, the server returns an attempt ID, and "Book" carries that ID. Every retry and double tap carries the same ID, because the client has no other identifier to send. The attempt also stores the binding quote, the terms snapshot and the hold, so a "Book" request with a different price or terms is refused, the IETF draft's 422 case.

{id: checkout-orchestration--carrying-the-key-to-every-hop}
### Carrying the key to every hop

The coordinator's retries, a crashed worker and a redelivered message all cross the next hop, so each participant needs a key derived from the attempt.

| Hop | Key | Documented example | What it prevents |
| --- | --- | --- | --- |
| Client → checkout | Checkout attempt ID (server-minted) | Stripe and IETF semantics, applied to purchases | A retried "Book" creating a second reservation |
| Checkout → allocation ledger | Attempt ID on the hold and commit | Unique constraint per night in [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) | A retried commit consuming a second room |
| Checkout → reservation store | Attempt ID as a unique column on the reservation | — | Two reservations for one attempt after a coordinator crash |
| Checkout → payment orchestrator → PSP | Attempt ID + obligation, then a PSP key per attempt | Airbnb's Orpheus library (2019) | A retried authorization charging twice |
| Affiliate → marketplace supply API | Partner reference | Expedia Rapid `affiliate_reference_id` | An affiliate's retry booking twice |
| Marketplace → property management system | Reservation ID + version | OpenTravel reservation messages, Booking.com acknowledgement queue | A redelivered or reordered message creating or overwriting a reservation |

Expedia's affiliate contract shows the cross-company version: partners must "always use a unique `affiliate_reference_id` for each booking request", and a duplicate returns "An itinerary already exists with this affiliate reference id" ([Expedia Group Rapid, Common error responses](https://developers.expediagroup.com/rapid/resources/error-responses-car), n.d., fetched October 2026). Airbnb's payments team published the internal version in April 2019: Orpheus, "a generic idempotency framework to achieve eventual consistency and correctness across our payments micro-service architecture" ([Chew and Khisti, Airbnb Engineering, 2019](https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb)). A 2024 secondary summary describes three phases per request (record the request against its key, make the remote call, record the response including failures), all on the primary database because replica lag could produce duplicate payments ([Biweekly Engineering, 2024](https://biweekly-engineering.beehiiv.com/p/handling-double-payments-airbnb-biweekly-engineering-episode-32)). The post is seven years old and may describe a replaced system.

{id: checkout-orchestration--a-second-line-the-natural-key-guard}
### A second line: the natural-key guard

A server-minted key does not stop a guest who opens checkout in two tabs, or an app bug that creates two attempts. For that I add a **natural-key guard**: before step 5, the coordinator looks for a pending or confirmed reservation by the same account for the same property or listing, dates and party within the last 30 minutes. A match does not block the booking, because some guests do book two identical rooms; it asks the guest to confirm ("You booked this stay at 19:53. Book another?"). The guard is a product rule, not an integrity guarantee.

{id: checkout-orchestration--timeouts-and-unknown-outcomes}
## Timeouts and Unknown Outcomes

Every remote call in the saga can succeed, fail, or time out and leave the caller not knowing. A slow payment provider produces the third case in quantity.

![Checkout attempt states from Started through Held and Authorizing to Authorized and Confirmed, with an Unknown state after a timeout whose only exits are lookups to Authorized or Declined, and Declined leading to Abandoned.](stays-marketplace-architecture/posts/21-checkout-orchestration/assets/images/21-checkout-orchestration/21-checkout-attempt-states.jpeg)

**Figure 5:** *The checkout attempt as a state machine. The Unknown state has only two exits, both driven by a lookup with the same key. Nothing compensates an unknown outcome and nothing retries it with a new key.*

Four rules govern the unknown state.

1. **Never compensate an unknown.** Voiding or refunding an authorization whose outcome is unknown either does nothing or undoes a payment the guest believes is a booking: the guest receives a confirmation and a refund for the same booking, or "booking failed" followed by a charge.
2. **Never retry an unknown with a new key.** That is the Roomstead incident in one sentence.
3. **Resolve by lookup, with a deadline.** The coordinator asks the participant for the result of the attempt's key, on a backoff schedule, until a deadline. Expedia's 30 minutes is a documented deadline for supplier bookings; for card authorizations I would use five minutes, then a reconciliation queue that reads the provider's report.
4. **Tell the guest the truth.** An Unknown attempt shows "We are confirming your booking" and a status page, never a "Try again" button, which invites the duplicate.

Timeouts need a budget set from the outside in: the client waits longer than the server, and the server longer than its slowest synchronous call. In January 2027 Roomstead's app gave up at 20 seconds while authorizations took 40. A defensible "Book" budget: authorization up to 25 seconds (a 3-D Secure challenge is guest time and runs as its own step), a server response by 30 seconds with the attempt in Unknown if authorization has not returned, and a client that waits 35 seconds and then polls instead of re-sending.

{id: checkout-orchestration--checkout-eligibility-policy-disclosure-and-guest-details}
## Checkout Eligibility, Policy Disclosure and Guest Details

{id: checkout-orchestration--eligibility}
### Eligibility

Eligibility checks are cheap one by one and expensive when scattered. I would collect them behind one eligibility call: **offer validity** (the quote is binding for these dates and this party); **stay rules** (minimum and maximum stay, closed-to-arrival, lead time, occupancy), evaluated by the same stay evaluator that priced the quote ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model)); **audience** (member, closed-user-group and point-of-sale rates, [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty)); the **payment arrangement** the offer allows for this guest and market ([Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models)); **regulatory gates** such as a listing's registration status ([Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation)) and sanctions; and **guest requirements** that hosts set on instant-book listings, plus minimum age. Each check returns a reason code; a refusal the property page could have predicted is a defect of the page.

{id: checkout-orchestration--policy-disclosure-and-the-terms-snapshot}
### Policy disclosure and the terms snapshot

The guest agrees to the cancellation policy, the payment schedule, house rules, the price breakdown and what is payable at the property. Those terms must be **frozen by version at checkout and attached to the reservation**, because everything later, from a free cancellation to a chargeback, is judged against what the guest saw.

| Term | Frozen as | Owner | Read later by |
| --- | --- | --- | --- |
| Price breakdown | Quote ID and itemized lines | Price composition | Payment plan, invoices, support |
| Cancellation policy | Policy ID and version, rendered text hash | Cancellation policy engine ([When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations)) | Self-service cancellation, refunds, partner |
| Payment arrangement and schedule | Arrangement version, payment plan v1 | Corvane Payments | Payment orchestrator, ledger |
| House rules and property policies | Content version | Property and listing content ([Describing a Stay: Content, Media and Property Mapping](#content-and-media)) | Support, trust and safety, claims |
| Display policy | Display-policy version for the market | Regulatory affairs | Regulators, dispute evidence |

Checkout **renders** these terms from their owners and **stores references**, never copies of text maintained in checkout templates. A checkout that keeps its own copy of "free cancellation until 48 hours before arrival" is the start of Policy Spaghetti.

Consumer law sets the boundary for what checkout may still change. The European Commission's 2021 guidance on the Unfair Commercial Practices Directive says that a trader who "raises the price for a product during the booking process ... without giving the consumer reasonable time to complete the transaction" could be acting contrary to professional diligence ([European Commission, 2021](http://publications.europa.eu/resource/celex/52021XC1229(05))). The binding quote window is the architecture's answer: once re-validation succeeds, the price does not move for 15 minutes.

{id: checkout-orchestration--guest-details-and-identity}
### Guest details and identity

Guest details look like form fields and behave like data with legal consequences. The ages of children decide tourist tax in some cities: Nookaway has asked for children's ages at checkout since 2025 because Lisbon's municipal regulation exempts guests under 13 ([The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)), which is why the Novak family's tax was €56 and not €112. The lead guest's name must match the name the hotel will look for at the desk. Whether the platform collects identity details that some countries require providers to record on arrival is a decision that [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) and [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) own.

Hosted-stays platforms often put identity verification on the booking path: Airbnb states that "every host, new co-host, and booking guest must be identity verified" ([Airbnb Help Center, article 1237](https://www.airbnb.com/help/article/1237), n.d., fetched October 2026). Verification after confirmation converts better but blocks a host's calendar for a guest who may never verify, so it needs the same timer discipline as a request to book.

Checkout is also where a marketplace can cross a legal line without noticing. Under the EU Package Travel Directive, combining accommodation with another travel service can create a **package**, among other cases when the traveler's name, payment details and e-mail address are passed to another trader and that contract is concluded "at the latest 24 hours after the confirmation of the booking of the first travel service" ([Directive (EU) 2015/2302, Art. 3(2)(b)(v)](http://publications.europa.eu/resource/celex/32015L2302), 2015; amended by Directive (EU) 2026/1024 of 29 April 2026, per the [European Commission](https://commission.europa.eu/law/law-topic/consumer-protection-law/travel-and-timeshare-law/package-travel-directive_en), live page, fetched October 2026). The saga must therefore timestamp the first confirmation; [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) covers the consequences.

{id: checkout-orchestration--where-the-fraud-and-risk-checks-go}
## Where the Fraud and Risk Checks Go

Each team tends to put its risk check where its data is available. The placement decides both the latency the guest pays and the loss the marketplace absorbs.

| Placement | What it checks | Latency budget | Typical actions | Fits |
| --- | --- | --- | --- | --- |
| **Entering checkout** | Bots, velocity, account takeover signals, inventory-hoarding behavior | Under 50 ms | Allow, rate-limit, challenge | Both; protects holds from abuse |
| **Before authorization** | Payment fraud score, card testing, stolen credentials | Under 200 ms | Allow, require 3-D Secure, deny | Merchant and facilitated bookings |
| **Before confirmation** | Reservation screening: guest history, trip pattern, listing type | Under 300 ms | Allow, redirect to other inventory, require host approval, deny | Hosted stays |
| **After confirmation** | Slower models, manual review, link analysis | Minutes to hours | Hold payout, cancel with refund, ask for documents | Both; cost is a canceled confirmed booking |

Airbnb's 2022 anti-party announcement for the US and Canada described a system that flags "potentially high-risk reservations" from signals such as review history, account age, trip length and distance from the listing, and "is designed to prevent a reservation attempt from going through"; blocked guests may still book a private room or a hotel room ([Airbnb Newsroom, 2022](https://news.airbnb.com/airbnb-introduces-new-anti-party-technology-in-us-and-canada)). The action set includes **redirect**, which keeps the guest in the marketplace and costs nothing to undo only if the risk decision runs before the hold and the authorization. Airbnb has not published the model or its place in its booking architecture; the placement here is my inference.

Payment risk interacts with Strong Customer Authentication (SCA), the EU's two-factor rule for electronic payments under the second Payment Services Directive (PSD2). Its technical standards, applied since 14 September 2019, let a provider skip SCA for low-risk remote card payments only below reference fraud rates of 0.13% up to €100, 0.06% up to €250 and 0.01% up to €500 ([Commission Delegated Regulation (EU) 2018/389, Art. 18 and Annex](http://publications.europa.eu/resource/celex/32018R0389), 2018). Stays baskets are mostly above €250, so checkout must model the challenge as a guest-time step with its own hold extension. [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments) covers SCA in depth; [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) owns the models.

The rule I would hold to: **risk returns a decision with a reason, and the coordinator acts on it**. Risk services that call the reservation store to cancel bookings, or checkout code that interprets raw scores, spread one decision over two owners and make every false positive untraceable.

{id: checkout-orchestration--performance-and-conversion}
## Performance and Conversion

Supplier delivery, notifications, non-urgent virtual-card issuing, loyalty accrual and analytics run behind the outbox, outside the guest's wait. Corvane's target for the "Book" call is under four seconds of server time at the 95th percentile, excluding any 3-D Secure challenge; authorization takes about three of them. The checkout dashboard measures integrity as well as conversion: completion per started attempt, re-validations returning changed or unavailable (the checkout share of Phantom Availability), attempts entering Unknown and their time to resolve, **duplicate reservations per 100,000 confirmed attempts** (from the natural-key guard in reporting mode), and confirmed bookings canceled by risk.

{id: checkout-orchestration--in-practice-the-public-record-and-corvane-s-redesign}
## In Practice: The Public Record and Corvane's Redesign

{id: checkout-orchestration--what-the-public-record-shows}
### What the public record shows

No stays company has published its booking saga, reservation state machine or internal locking. What is public is the external contract, such as Expedia's Rapid holds and partner references and Booking.com's Request to Book, and, for Airbnb, a decade of payments engineering: Orpheus (2019); orchestration rebuilt in 2022 as "a directed acyclic graph (DAG) of retryable idempotent steps", reaching "five 9s (99.999%) of consistency for payments" ([Airbnb Engineering, 2022](https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b)); and Skipper (2026).

> **INFERENCE, NOT DOCUMENTED:** These sources show that large stays platforms treat booking as a multi-step process with explicit holds, idempotent references and unknown outcomes. They do not show where each company places its pivot, how its coordinator stores state, or how it resolves unknown supplier outcomes internally. The saga in this chapter is a reference architecture consistent with the public contracts, not a description of any company's system.

{id: checkout-orchestration--corvane-s-redesign-the-checkout-attempt-contract}
### Corvane's redesign: the checkout attempt contract

In **February 2027** Mariana's architecture forum adopted a **checkout attempt contract** for both brands, which became part of the One Stay offer and reservation contract when the board approved the program in April. "Book" takes only the server-minted attempt ID, which is the unique key of the pending reservation in Keystone and Burrow and of the hold and commit in the allocation ledger, and the root of every payment obligation key Corvane Payments sends to its acquirers. Turnstile returns the attempt as Unknown after 30 seconds; the app, its generic retry interceptor disabled for purchase calls, waits 35 seconds and then polls the attempt's status for up to five minutes. Unresolved authorizations go to a reconciliation queue after five minutes. A natural-key guard runs first in reporting mode, then as a confirmation prompt.

Roomstead's app shipped the change in March 2027 and the web checkout in April. Nookaway adopted the contract in Burrow as part of Payment Plans v1 between April and September 2027 ([Paying for a Future Night: Payment Orchestration for Stays](#stay-payments)), because its checkout had the same client-minted keys and had not yet been tested by a provider slowdown.

**The incident replayed.** Under the new contract the app would have waited 35 seconds instead of 20, so most of the 40-second authorizations would have returned in time; the rest would have entered Unknown and shown a confirming state. A retry that slipped through would have carried the same attempt ID and received the original result, or a conflict while the original was running: no second reservation, charge or virtual card. The guard in reporting mode would have shown the residue: guests who started a second checkout from a second device.

**The Novaks' booking through the new contract.** The Novak family's Nookaway booking is a facilitated, instant-book stay paid at booking. On **14 February 2027** they booked an Alfama apartment for **2–9 August**: 7 nights × **€145** = €1,015, **€70** cleaning, a 12% guest service fee of **€130.20** and Lisbon tourist tax of **€56**, total **€1,271.20**. Replayed through the target design, with illustrative timings:

| Step | What happens | Recorded |
| --- | --- | --- |
| Start checkout | Quote re-validated against Almanac; party of 2 adults and children aged 9 and 12; terms snapshot: the listing's cancellation policy version, house rules version, arrangement `FACILITATED` with Corvane Payments as merchant of record | Attempt ID; quote binding for 15 minutes; total €1,271.20 |
| Risk | Pre-authorization payment score and reservation screening: an established account, a family of four, a seven-night stay booked six months ahead | Allow, reason codes logged |
| Hold | Seven listing-nights held in the allocation ledger for 10 minutes from the start of payment | Hold keyed by attempt ID |
| Pending reservation | Created in Burrow, invisible to the host | Reservation keyed by attempt ID |
| Authorization | €1,271.20 with a 3-D Secure challenge; the challenge extends the hold once to 20 minutes; the card is stored with the scheme reference for later charges | Authorization and credential under obligation keys |
| Pivot | Seven nights committed; reservation confirmed | Confirmation event in the outbox |
| After the pivot | Capture of €1,271.20; ledger entries in Fathom (host payable €1,041.60, fees, €56 tourist tax payable); host notified; confirmation e-mail | Payment state feed events |

The guest's synchronous wait, excluding the time Jana spent in her bank's app, was under four seconds, and one attempt with one frozen set of terms is what makes the payout on 4 August ([Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement)) and the €56 ([The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)) explainable months later.

{id: checkout-orchestration--trade-offs}
## Trade-offs

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| **Coordination style** | Orchestration: one coordinator owns the saga state | Choreography: each service reacts to the previous one's events | Booking paths with a pivot, compensations and a guest waiting for an answer; almost always | Post-confirmation fan-out (delivery, notifications, loyalty), where nobody waits and order matters less |
| **Who mints the key** | Server-minted checkout attempt | Client-minted key per intention | Mobile apps and any client with shared retry code | Server-to-server partners with disciplined clients, such as affiliates under a documented reference contract |
| **Supplier confirmation** | Confirm on the platform's copy, deliver after | Supplier confirms synchronously as the pivot | Push-connected hotels and platform-owned calendars | Pull-model supply such as bedbanks, where the platform's copy is not authoritative |
| **Money at booking** | Authorize, commit, then capture | Capture before commit | Most flows: a void is cheaper than a refund | Payment methods that cannot authorize separately, such as many redirect and bank-transfer methods, which need a pending-payment reservation instead |
| **Booking mode** | Instant book | Request to book | Hotels; homes with an API-connected or single-channel calendar | iCal-only multichannel homes on peak dates; hosts who need to vet guests |
| **Workflow runtime** | Durable workflow engine | Hand-written state machine in the reservation service's database | Several sagas, long waits (request to book, Pay Later), many teams | One saga, short waits, a team that already owns the reservation store |

I recommend **orchestration before the pivot and choreography after it**: a booking with a guest waiting needs one owner that knows the whole state, can say "this attempt is Unknown", and can decide a compensation. [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays) covers the events.

{id: checkout-orchestration--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Concern | Accommodation marketplace (Roomstead) | Hosted-stays marketplace (Nookaway) |
| --- | --- | --- |
| **What is committed** | One room of a room type, a conditional decrement on a count the hotel claims | One unit's nights, a uniqueness constraint on a calendar the platform owns |
| **Who confirms** | The platform on its inventory copy; for pull-model supply, the supplier's API | The platform for instant book; the host for request to book |
| **Typical pivot** | Commit on the platform after authorization (merchant) or with no payment step (agency) | Commit on Almanac after authorization; host acceptance for request to book |
| **Payment at checkout** | Agency: card guarantee or nothing; merchant: authorize and capture, then a virtual card to the hotel | Always collected by the platform: pay now or a chargeable credential for Pay Later |
| **Risk check that matters most** | Payment fraud and card testing; affiliate and bot abuse of holds | Reservation screening of the guest for the home; host-account takeover |
| **Hard-to-undo step** | Non-refundable rates and active virtual cards; bedbank bookings with supplier penalties | A blocked calendar on a peak date that may have cost the host another guest |
| **Long waits in the saga** | Rare: pull-model supplier confirmation in seconds | Common: 24-hour host decisions, identity verification, Pay Later |
| **Duplicate cost** | A second room consumed at the hotel, a second card, a refund | A refund and a host who sees two bookings on one calendar, or a refused second commit |

**What to share.** I would share the **checkout attempt contract**, the **idempotency discipline** and key derivation, the **terms snapshot** format, the **unknown-outcome handling** and its reconciliation queue, the **risk decision interface** and the **checkout metrics**: one fix there protects both brands. The One Stay offer and reservation contracts are their natural home ([One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces)).

**What to keep separate.** The sagas differ in their steps: Roomstead's has supplier variants and virtual cards, Nookaway's has host decisions, screening and long waits. One coordinator expressing both produces a configuration language nobody can read, the checkout version of **The Hotel-Shaped Home**. Two coordinators speaking one contract is the One Stay pattern; a shared durable workflow runtime is a reasonable later platform choice, not a reason to merge the sagas.

{id: checkout-orchestration--failure-modes}
## Failure Modes

**Holds as the guarantee.** *Symptom:* double bookings when holds expire during a slow payment. *Cause:* checkout trusts a hold instead of committing against the allocation ledger. *Defense:* expiry evaluated at commit; commit refused cleanly; authorization voided. Martin Kleppmann's 2016 argument that a lease is not a correctness guarantee without a fencing check in storage applies directly ([Kleppmann, 2016](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)); [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) works it through.

**Request to book without timers.** *Symptom:* calendars blocked by expired requests and authorizations held for days. *Defense:* every timed state has a timer, an owner and an expiry action.

{id: checkout-orchestration--the-chief-architect-s-view}
## The Chief Architect's View

Checkout is small in code and large in consequence; each of its few decisions needs a named owner.

**Decide what one booking is, at group level.** Changes to the checkout attempt and its key go through Mariana's forum, because a change in one brand's key semantics breaks reconciliation in Corvane Payments for both.

**Decide the pivot per flow and write it down.** A one-page table per brand, reviewed whenever a payment model or supply type is added, prevents bookings confirmed without money or charged without a booking. Roomstead's growth toward 40% merchant bookings by the end of 2028 moves more bookings to flows where the pivot follows a payment.

**Own the unknown.** At Corvane, Leila Haddad's team owns the queue of unresolved payment attempts and Roomstead supply owns bedbank unknowns. A queue without an owner becomes a reconciliation gap like the €1.8 million mismatch between virtual cards and reservations ([Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation)).

**Test the bad evening.** The test that matters injects 40-second payment calls, dropped responses and coordinator crashes, and asserts one reservation and one charge per attempt. I would make it a release gate for any change on the booking path, including app releases that touch networking code; the 7 January release would not have passed it.

**Keep the migration in view.** Keystone still creates Roomstead reservations in 2027, and One Stay retires its reservation module by the end of 2029. Because the key lives in the contract, not in Keystone, a new reservation service can take over creation behind the same attempt without the app, Corvane Payments or the allocation ledger noticing.

{id: checkout-orchestration--questions-to-ask}
## Questions to Ask

1. Who mints the idempotency key for a purchase, and can any client retry path, including generic networking code, generate a new one?
2. For each flow (agency, merchant, facilitated, pay later, request to book, pull-model supply), where is the pivot, and what is the compensation for each step before it?
3. What does the system do when a payment or supplier call times out? Is there an Unknown state, who resolves it, by what deadline?
4. Does checkout re-validate the quote by ID through the same composition service as the property page, or compute the price itself?
5. Which terms are frozen on the reservation at checkout, by version, and which are still read live later?
6. Where does each risk check run, what is its latency budget, and what happens when it is unavailable?
7. Does a hold ever stand in for the commit, and is hold expiry checked at commit time?
8. When did we last run checkout against 40-second payment latency and dropped responses, and how many duplicates did it produce?

{id: checkout-orchestration--from-booking-to-reservation}
## From Booking to Reservation

A confirmed booking must still reach the property or host, change as plans change, survive cancellations and no-shows, and trigger reviews and payouts at the right moments. Checkout hands over one reservation with one key and one frozen set of terms; [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) takes it from there.

{id: checkout-orchestration--sources-and-evidence}
## Sources and Evidence

{id: checkout-orchestration--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Avoiding Double Payments in a Distributed Payments System](https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb), Jon Chew and Ninad Khisti, Airbnb Engineering, 2019: Orpheus idempotency framework (title and framing; body not read).
- [Handling Double Payments at Airbnb](https://biweekly-engineering.beehiiv.com/p/handling-double-payments-airbnb-biweekly-engineering-episode-32), Biweekly Engineering newsletter, 2024: secondhand summary of Orpheus's three-phase mechanism and primary-database rule.
- [Rebuilding Payment Orchestration at Airbnb](https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b), Airbnb Engineering, 2022: workflows as DAGs of retryable idempotent steps, five-nines consistency, payments formerly coupled to the stay reservation.
- [Skipper: Building Airbnb's Embedded Workflow Engine](https://airbnb.tech/infrastructure/skipper-building-airbnbs-embedded-workflow-engine/), Airbnb Engineering, 2026: durable workflows, at-least-once actions, compensations in reverse order, charge-then-accept example.
- [Airbnb introduces new anti-party technology in US and Canada](https://news.airbnb.com/airbnb-introduces-new-anti-party-technology-in-us-and-canada), Airbnb Newsroom, 2022: reservation screening before confirmation, redirect action.
- [Instant Book](https://www.airbnb.com/help/article/523), [request declined or expired](https://www.airbnb.com/help/article/315), [payment on declined or expired requests](https://www.airbnb.com/help/article/313), [identity verification](https://www.airbnb.com/help/article/1237), Airbnb Help Center, n.d. (live pages fetched October 2026): booking modes, 24-hour window, authorization, verification at booking.
- [Request to Book overview](https://developers.booking.com/connectivity/docs/request-to-book/overview), Booking.com Connectivity, n.d. (fetched October 2026): host and guest windows, pre-authorization, RtB 2.0 provider-side holds, three-day lead time.
- [About booking requests for integrated accounts](https://help.vrbo.com/articles/IPM-About-booking-requests-for-integrated-accounts), Vrbo Help, n.d. (fetched October 2026): 24-hour guidance, calendar hold during requests.
- [Hold and Resume](https://developers.expediagroup.com/rapid/lodging/booking/hold-resume) and [Common error responses](https://developers.expediagroup.com/rapid/resources/error-responses-car), Expedia Group Rapid, n.d. (fetched October 2026): two-step booking, automatic rollback, `affiliate_reference_id`, 90-second timeout, 13–30-second resolution, 30-minute retrieval.
- [Booking API workflow](https://developer.hotelbeds.com/documentation/hotels/booking-api/workflow/), Hotelbeds, n.d. (fetched 2026): CheckRate recheck before booking pull-model supply.

{id: checkout-orchestration--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Idempotent requests](https://docs.stripe.com/api/idempotent_requests), Stripe API reference, n.d. (fetched October 2026): saved first response, parameter comparison, 24-hour pruning.
- [Designing robust and predictable APIs with idempotency](https://stripe.com/blog/idempotency), Brandur Leach, Stripe, 2017: cached results on retry, backoff with jitter.
- [The Idempotency-Key HTTP Header Field, draft-ietf-httpapi-idempotency-key-header-07](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/), Jena and Dalal, IETF, 2025: duplicate, concurrent and mismatched-payload behavior (Internet-Draft).
- [Saga design pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga), Microsoft Azure Architecture Center, 2025: pivot transaction, compensations that may fail, isolation countermeasures.
- [Commission Delegated Regulation (EU) 2018/389](http://publications.europa.eu/resource/celex/32018R0389), 2018 (CELEX 32018R0389): SCA technical standards, transaction-risk-analysis thresholds, application from 14 September 2019.
- [Guidance on the interpretation and application of Directive 2005/29/EC](http://publications.europa.eu/resource/celex/52021XC1229(05)), European Commission, 2021 (CELEX 52021XC1229(05)): price increases during the booking process, drip pricing.
- [Directive (EU) 2015/2302 on package travel and linked travel arrangements](http://publications.europa.eu/resource/celex/32015L2302), 2015 (CELEX 32015L2302): 24-hour linked-booking test; applied from 1 July 2018.
- [Package Travel Directive](https://commission.europa.eu/law/law-topic/consumer-protection-law/travel-and-timeshare-law/package-travel-directive_en), European Commission, live page (fetched October 2026): amendment by Directive (EU) 2026/1024, 28-month transposition.

{id: checkout-orchestration--research-and-practitioner-sources}
### Research and practitioner sources

- [How to do distributed locking](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html), Martin Kleppmann, 2016: leases are not correctness guarantees without fencing.
- [Sagas](https://dl.acm.org/doi/10.1145/38713.38742), Hector Garcia-Molina and Kenneth Salem, SIGMOD 1987: origin of the saga concept for long-lived transactions.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
