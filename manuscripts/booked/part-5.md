{class: part, id: part-5}
# Part V — BOOKING: Making and Keeping the Reservation

![Part V — BOOKING: Making and Keeping the Reservation — logo](stays-marketplace-architecture/posts/part-5-intro/assets/images/part-5-intro/logo.jpeg)

> **IN THIS PART, YOU WILL:** Design the booking path from checkout to check-out: checkout orchestration, the reservation lifecycle and its delivery to properties and hosts, changes, cancellations and disruptions, the trip timeline with messaging and notifications, and customer service as the platform's failure path.

> **WHY THE BUSINESS CARES:** This is where the marketplace makes promises to guests, partners and payment networks at once. A duplicate charge, a booking the hotel never received or a door code that never arrived costs a refund, a relocation or a customer.

> **WHY ARCHITECTS SHOULD CARE:** A reservation lives for weeks or months, is replicated into systems the marketplace does not own, and is read by payments, tax, trust and regulatory reporting.

> **KEY POINTS:**
>
> * **One guest intention, one key, one pivot.** Checkout is a saga whose pivot is chosen per payment model and supply type; before it every step can be undone, after it every step retries until it succeeds. A server-minted checkout attempt key travels to every hop, and an unknown outcome is a state to resolve, not an error to retry.
> * **A reservation is a versioned agreement with separate dimensions.** Keep what was agreed, who knows about each version, what happened at the property and what was paid apart, each with one writer. "Delivered" means the supplier's system accepted this version, and a pre-arrival check confirms it again.
> * **Policies, messages and remedies are decisions with owners.** One engine evaluates cancellation policy for every channel. Arrival-critical messages are tracked to the guest. Every refund, relocation and credit is a recovery decision with a funder and a liable party, posted to the ledger.

> **[FAILURE PATTERNS THIS PART ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Lost at the Front Desk** — Tracks every reservation version and every arrival message to acknowledgement, and verifies arrivals before the guest travels.
> * **Policy Spaghetti** — Replaces policy rules copied into checkout, self-service, macros and partner systems with one engine and a frozen snapshot.
> * **Built for Sunny Days** — Designs for slow payment providers, mass cancellations and arrival-day peaks: unknown states, declared disruptions and a surge mode.

Part IV ended at a quote on a property page. Part V turns that quote into **a reservation and keeps it true** until the guest checks out. Everything before checkout can be recomputed. From the moment the guest presses "Book", each mistake lands in a system the marketplace does not control: a card network, a channel manager, a property management system (PMS), a host's phone.

The argument of this part is that **the reservation is the object that crosses every boundary in the book**, and it must be designed as a contract before it is built as a service. Checkout creates it, the lifecycle replicates and verifies it, changes version it, the trip platform explains it, and customer service repairs it.

![One reservation contract at the centre of the marketplace, with copies travelling across its boundary to a card network, a channel manager, a hotel PMS and a host's phone.](stays-marketplace-architecture/posts/part-5-intro/assets/images/part-5-intro/part-5-reservation-crosses-boundaries.jpeg)

**Figure 1:** *The reservation is the object that crosses every boundary: from the moment the guest presses Book, copies of it live in a card network, a channel manager, a PMS or a host's phone.*

Hotels and homes take different paths through it. A hotel reservation must be **delivered**: through Switchyard and a channel manager to a PMS that may reject it silently. The hotel reports no-shows and departures. A home reservation often has **nothing to deliver**, since the host works in the app, but it may wait 24 hours for a host decision under request to book. The stay is inferred from time passing without a dispute, and the arrival depends on a door code rather than a front desk. Corvane, the fictional travel group this book follows, shares the contract, the event catalog, the policy engine and the support platform, and keeps the checkout sagas separate.

![A path of reservation states from a keyed checkout attempt through Confirmed v1 and Delivered, with a loop to Modified v2 and back, then Arrival verified and Stayed or no-show, and a branch from Delivered to Canceled.](stays-marketplace-architecture/posts/part-5-intro/assets/images/part-5-intro/part-5-reservation-journey.jpeg)

**Figure 2:** *The reservation's journey through Part V: one keyed attempt becomes a versioned agreement that is delivered, changed, verified before arrival and closed by a stay outcome or a policy decision, each step owned by one chapter.*

{id: part-5--chapters-in-this-part}
## Chapters in this part

[Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration) decides **how an offer becomes exactly one booking**: quote re-validation, holds, payment, supplier confirmation as a saga with an explicit pivot, and one checkout attempt key from the app to the hotel. On 14 January 2027 a slow payment path and an app that retried with new keys created 212 duplicate Roomstead reservations through Turnstile, 198 of them charged twice.

[The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) decides **how all parties stay in agreement for weeks**. It separates commercial, delivery, stay and money state, defines delivery as the supplier's acceptance, and verifies every arrival beforehand. Stayline is the cross-brand projection built from contract events. Nineteen reservations that Hotel Miradouro's PMS silently rejected in July 2027 are the case.

[When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) decides **who gets what back when plans change**. One engine evaluates versioned cancellation policies, a change is a new reservation version, and disruptions are declared events with a funding rule: waive what you hold, request what you do not. The air-traffic-control strike weekend of 5–7 June 2027 is the case.

[Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) decides **what the guest needs between booking and check-out and how it reaches them**: a trip timeline that explains itself, Threadline's stage-aware messaging policy, and notification routing that treats arrival information as a deliverable with a deadline. A scam filter that replaced door codes with "[hidden]" in August 2027 is the case.

[When Something Goes Wrong: Customer Service and Recovery](#customer-service) decides **how broken promises are repaired**: cases bound to reservations, parties and an arrival clock, a recovery-decision service posting to Fathom, and AI agents acting only through the same tools. The four Roomstead guests walked from Hotel Prinsenkade on King's Day led to Harbor, the group support platform.

Begin with [Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration).
