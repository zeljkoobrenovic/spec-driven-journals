{id: changes-and-cancellations}
# 23. When Plans Change: Modifications, Cancellations and Policies

![When Plans Change: Modifications, Cancellations and Policies — logo](stays-marketplace-architecture/posts/23-changes-and-cancellations/assets/images/23-changes-and-cancellations/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Take apart what happens when a guest or supplier wants to change a confirmed stay: policy models and versioning, the cancellation policy engine, modifications, host and property cancellations, extenuating circumstances and mass disruptions, self-service changes and the consumer law that bounds them.

> **WHY THE BUSINESS CARES:** At an OTA a large share of booked room nights never become stays (34% were canceled at the fictional Roomstead in 2026), and every cancellation is a contact, a refund, a resale problem and a judgement about who absorbs the loss. A general manager needs cancellation rules that guests trust, partners accept and finance can predict.

> **WHY ARCHITECTS SHOULD CARE:** A cancellation rule is evaluated in at least six places: the property page, checkout, the confirmation e-mail, the self-service flow, the support tool and the payment scheduler. If each computes it separately, guests, partners and agents get different answers, and the money follows the wrong one.

> **KEY POINTS:**
>
> * **A cancellation policy is versioned data, and one engine evaluates it.** Freeze the policy on the reservation as typed time windows, keep a guest-facing and a supplier-facing policy where they differ, and let one deterministic engine answer "what happens if this actor does this now", with itemized lines per party, for every channel from the property page to the AI support agent.
> * **A change is a new reservation version, delivered and acknowledged like a booking.** Modifications re-price, re-check availability, version the payment plan and reach the property, PMS or host as a message that must be acknowledged. Whether the original policy carries over is a product rule written down in the engine, not an accident of the code path.
> * **Disruptions are declared events, and the marketplace waives only what it controls.** Model a disruption as data (place, window, booking cutoff, class, funding) and run it as a batch with self-service. Under agency, merchant and facilitated payments the marketplace holds different money, so it can waive its own share, must ask suppliers to waive theirs, and must never refund supplier money it does not hold.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Policy Spaghetti** — Cancellation rules computed separately in checkout, self-service, support macros, payments and partner systems give guests, partners and agents different answers, and refunds follow whichever system acted first.
> * **Built for Sunny Days** — A platform tuned for a steady trickle of cancellations meets a strike, an ash cloud or a pandemic with nothing but a support queue, because no mechanism exists to declare an event and decide thousands of bookings at once.
> * **Lost at the Front Desk** — Modifications and cancellations sent to properties without acknowledgement leave the hotel charging a guest the platform refunded, or expecting a guest who moved their dates.

Guests move dates or cancel, hotels oversell, hosts cancel, and sometimes a strike closes airspace. Each of these turns one confirmed reservation into a **negotiation among three parties about money that sits in different places** depending on the payment model. The refund arithmetic is easy; the hard part is that **the same question gets asked of many systems**, including the hotel's own property management system (PMS), and the money follows whichever answers first.

This chapter is the third in Part V ([Part V — BOOKING: Making and Keeping the Reservation](#part-5)). [Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration) creates the reservation and [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) owns its state machine and delivery to properties; this chapter owns what happens when someone wants to change it. It owns the **cancellation policy engine**, **extenuating circumstances** (declared disruption events) and the **self-service change**. Refund execution and reconciliation belong to [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation), case handling and relocation decisions to [When Something Goes Wrong: Customer Service and Recovery](#customer-service), and the price composition behind a re-quote to [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection).

{id: changes-and-cancellations--setting-the-scene-at-corvane-the-strike-weekend-that-gave-three-answers}
## Setting the Scene at Corvane: The Strike Weekend That Gave Three Answers

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), runs two marketplaces: Roomstead, an online travel agency (OTA) for hotels and professionally managed apartments, and Nookaway, a hosted-stays marketplace. On **Thursday 3 June 2027** French air-traffic controllers announced a strike for **Saturday 5 to Monday 7 June**. Flights over and into France were canceled across Europe. About **17,000** Roomstead and **2,600** Nookaway reservations had guests who could not get there, or could not get home. Roomstead received **6,200** cancellation requests in 48 hours.

Neither brand could declare the strike as an event, so each request was handled by whatever system the guest reached first.

| Path | Roomstead requests | What it did |
| --- | --- | --- |
| Self-service cancel in app and web | **2,950** completed | Keystone, the Java monolith that owns Roomstead reservations, applied the rate plan's policy as frozen at booking. It worked for free-cancellation bookings and showed "100% cancellation fee" for the rest. |
| Contact with customer service | **3,250** | **750** guests inside the free-cancellation window called anyway, because the confirmation e-mail rendered the deadline in Irish time and the app in property time. **2,500** held non-refundable or past-deadline rates. |
| Agent "travel disruption" macro | **1,860** of the 2,500 | A support-tool macro written on Friday set the penalty to zero and canceled the booking in Keystone. It did not ask the property and did not distinguish payment models. |

![Three guests holding the same booking card before three doors labeled Self-service, Support and Macro, each leading to a different outcome during a strike weekend.](stays-marketplace-architecture/posts/23-changes-and-cancellations/assets/images/23-changes-and-cancellations/23-three-answers.jpeg)

**Figure 1:** *On the strike weekend the same question got a different answer depending on the path the guest reached first: the app, a support agent or a macro that waived penalties.*

The macro is where the money went wrong. Roomstead sells **70%** of its room nights under the **agency model**, where the guest pays the property, and **30%** under the **merchant model** ("Pay with Roomstead"), where Corvane Payments charges the guest and pays the property with a virtual card ([Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models)).

- **1,140** waived bookings were agency bookings. Roomstead held none of the guests' money. The cancellations reached properties as ordinary cancellations of non-refundable rates with a free-text remark, "fee waived – ATC strike", which most PMSs do not display. **610** properties charged the guests' cards under their own policy. Guests who had been promised a free cancellation disputed the charges or complained, and Roomstead reimbursed them **€167,900** from its own funds.
- **720** waived bookings were merchant bookings, refunded in full. But virtual cards for non-refundable rates were still active from booking (the default changed only with Payment Plans v1, [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments)), and **290** hotels had already charged them, the pattern behind **€1.02 million** of the first quarter's €1.8 million virtual-card gap ([Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation)). Corvane Payments recovered most of it over the following weeks; **€31,200** was never recovered.

In 2020 Nookaway's support tool had gained a per-reservation "extenuating circumstances" flag for COVID-19: full refund to the guest regardless of the listing's policy, no payout to the host. Agents used it on **1,050** of the **1,480** Nookaway requests that weekend, because it resolved a case in one step; the other **430** were refunded under the listing's policy. Identical bookings got different outcomes depending on the agent, and hosts who lost a whole payout for a transport strike their policy did not cover filed **310** complaints. In Lisbon, Nookaway's automatic pricing read the cancellations as falling demand and cut prices for the following weekend ([Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing)).

At the post-incident review on 15 June, Elena Petrova (VP Customer Service) put the numbers on the table: almost **€200,000** of Roomstead's money spent refunding money it never held or had already paid out, and Nookaway hosts who had learned the platform could take their payout for reasons their policy did not mention. Mariana Costa, the Group Chief Architect, framed the architectural question for the architecture forum: **what should own the answer to "what happens if I change or cancel this booking", and how should the platform act when thousands of people ask it at once?**

{id: changes-and-cancellations--concepts-policies-changes-and-who-holds-the-money}
## Concepts: Policies, Changes and Who Holds the Money

{id: changes-and-cancellations--the-vocabulary}
### The vocabulary

| Term | Definition in this book |
| --- | --- |
| **Cancellation policy** | The rule that says what a guest gets back, and what the supplier keeps, if the guest cancels at a given time. Expressed as ordered time windows before arrival, each with a typed penalty. |
| **Policy snapshot** | The policy frozen onto the reservation at booking, with its version. Later edits to the rate plan or listing do not change it. |
| **Guest-facing and supplier-facing policy** | The policy the marketplace sold to the guest and the one the supplier granted the marketplace. Usually identical; sometimes deliberately not. |
| **Modification** | A change to a confirmed reservation that keeps its identity: dates, guests, room type, rate plan, guest name, special requests. |
| **Extenuating circumstances** | Events outside the guest's and supplier's control that justify overriding the booking's policy. In this book they are modeled as **declared disruption events**. |
| **Cancellation policy engine** | The single service that evaluates a policy snapshot, an action, an actor, a time and any overrides into an itemized decision. |
| **Self-service change** | A guest- or supplier-initiated change completed without an agent: the guest knows what it costs, whether it is confirmed and what was sent to the property or host. |

{id: changes-and-cancellations--what-a-cancellation-policy-is}
### What a cancellation policy is

[Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) defines the data shape: ordered time windows before arrival, each with a typed penalty (an amount, nights, or a percentage), in the property's local time. Expedia's Rapid API is a good public reference, with an ISO-8601 offset on each deadline ([Expedia Group, Constructing cancellation policies](https://developers.expediagroup.com/rapid/lodging/shopping/constructing-cancellation-policies), n.d., fetched October 2026).

**Hosted-stays policies are platform templates.** A host chooses one tier from a small set the platform defines. Airbnb's set for stays under 28 nights, as of October 2026: Flexible (full refund until 24 hours before check-in), Moderate (5 days), Limited (14 days, for bookings from 1 October 2025), Firm (30 days), Strict variants by invitation, and a discounted non-refundable option; all standard policies refund in full within 24 hours of confirmation if booked at least 7 days before check-in ([Airbnb Help Center, Cancellation policies for your listing](https://www.airbnb.com/help/article/475), live page, fetched 21 October 2026). The host's policy "may be overridden" by Airbnb's disruption and rebooking policies, which the platform can apply itself because it holds the guest's money until check-in ([Airbnb FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), 2026).

**OTA policies are supplier rules per rate.** A hotel attaches a policy to each sellable product, and it arrives with the rate feed. Booking.com's customer terms, as updated in August 2025, say the booking is "directly with the Service Provider" and "any cancellation/no-show fee and any refund will depend on the Service Provider's cancellation/no-show policy" ([Booking.com Terms](https://www.booking.com/content/terms.html), 2025). The OTA does not own the rule; it carries and enforces a copy.

{id: changes-and-cancellations--two-policies-on-one-reservation}
### Two policies on one reservation

The two can differ on purpose. Booking Holdings' 2025 annual report states that it may "offer cancellable room rates on behalf of a partner ... even if the partner has not provided a cancellable room rate", and that where it had agreed to provide free cancellation for non-refundable reservations it "did not estimate a recovery of prepayments already made" to suppliers ([Booking Holdings FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), 2026). In such cases the marketplace sells flexibility it underwrites itself.

A reservation may therefore carry **two policy snapshots**: a guest-facing one that decides the refund and a supplier-facing one that decides what the supplier keeps. The gap is a marketplace liability and must be a ledger account, not an unexplained loss.

{id: changes-and-cancellations--there-is-no-right-to-change-your-mind}
### There is no right to change your mind

EU consumer law does not give guests a cooling-off period for accommodation. The Consumer Rights Directive excludes "the provision of accommodation other than for residential purpose" with a specific date or period of performance from the 14-day withdrawal right ([Directive 2011/83/EU, Article 16(l)](http://publications.europa.eu/resource/celex/32011L0083), 2011). Cancellation terms are therefore a commercial attribute of the offer, which is why non-refundable rates can be cheaper.

Two other bodies of law bound those terms.

- **Fair and clear presentation.** Consumer protection law treats misleading information about the main characteristics of a product, which includes the conditions of cancellation, as an unfair commercial practice ([Directive 2005/29/EC, Article 6](http://publications.europa.eu/resource/celex/32005L0029), 2005). A policy that the property page, the e-mail and the self-service flow describe differently is a legal risk as well as a support cost. [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) covers enforcement.
- **Packages.** When accommodation is sold as part of a package, the Package Travel Directive (applying since 1 July 2018) lets the traveler terminate "without paying any termination fee in the event of unavoidable and extraordinary circumstances occurring at the place of destination or its immediate vicinity ... or which significantly affect the carriage of passengers to the destination", with refunds due "not later than 14 days after" termination ([Directive (EU) 2015/2302, Articles 3(12) and 12](http://publications.europa.eu/resource/celex/32015L2302), 2015). The European Commission states it was amended by Directive (EU) 2026/1024 of 29 April 2026, with 28 months to transpose ([European Commission, Package Travel Directive](https://commission.europa.eu/law/law-topic/consumer-protection-law/travel-and-timeshare-law/package-travel-directive_en), live page, fetched October 2026); press coverage reported tighter voucher rules ([Travel Extra, 2025](https://www.travelextra.ie/provisional-agreement-reached-on-package-travel-directive-revision/)). The amending text was not reviewed for this chapter; check the Official Journal before relying on details.

For architects: **the same strike can give a hotel-only guest no right to a free cancellation and a package guest a full refund within 14 days**, so the engine must know whether a reservation is part of a package, a fact recorded at checkout ([Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration)).

{id: changes-and-cancellations--who-holds-the-money-decides-who-can-refund}
### Who holds the money decides who can refund

The payment model ([Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models)) decides which refunds the marketplace can make on its own.

| Model | Who holds the guest's money before arrival | What the marketplace can do alone | What needs the supplier |
| --- | --- | --- | --- |
| **Agency** (pay at property) | The property, or nobody yet | Waive or credit its own commission; offer its own credit or voucher | Any refund of the room price; any waiver of a property's penalty |
| **Merchant** (OTA charges the guest) | The marketplace, then the property via virtual card or transfer | Refund the guest from funds it holds until the supplier is paid | Recovering money already paid to the property; waiving the supplier-facing penalty |
| **Facilitated** (hosted stays) | The marketplace, until payout after check-in | Refund the guest, withhold or reverse the host's share, waive its own fees | Only the host's consent to give up money the policy entitles them to, as a matter of fairness rather than mechanics |

Roomstead's June macro ignored this table. It "waived" penalties on agency bookings, where it held nothing, and on merchant bookings whose virtual cards were already chargeable. Nookaway's flag ignored the last cell: the platform *could* take the host's share, so it did, without a rule saying when it should.

{id: changes-and-cancellations--architecture-one-engine-one-change-path-one-event-registry}
## Architecture: One Engine, One Change Path, One Event Registry

Three components carry the design: a **cancellation policy engine** that answers every "what happens if" question, a **change orchestrator** that turns an accepted answer into a new reservation version, and a **disruption registry** that applies declared events to many reservations at once.

![Policy snapshot, action and actor, payment arrangement and disruption overrides feed one policy engine, whose decision goes both to every channel for display and to the change orchestrator, which updates the reservation, payments and the property or host.](stays-marketplace-architecture/posts/23-changes-and-cancellations/assets/images/23-changes-and-cancellations/23-one-policy-engine.jpeg)

**Figure 2:** *Every channel asks the same engine for one itemized decision; the change orchestrator executes it across the reservation, payments and the supplier.*

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Cancellation policy engine** | Evaluate an action against a reservation's frozen policies and active overrides; return an itemized, explainable decision | Policy templates, the evaluation rules, override precedence, decision records | Move money, change reservations, or read live rate-plan policies for existing bookings |
| **Change orchestrator** | Quote, confirm and execute modifications and cancellations as sagas | Change quotes, change requests and their timers, compensation | Recompute penalties or prices itself |
| **Disruption registry** | Hold declared events: class, place, window, booking cutoff, affected-party filter, override, funding | Event records, the matcher, batch runs | Be edited without an owner, a reason and an expiry |
| **Price composition** | Re-price changed nights and occupancy for a modification | Quotes for the new version ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection)) | Apply cancellation penalties |
| **Payments** | Version the payment plan; refund, charge, resize or void virtual cards | Payment plan execution ([Paying for a Future Night: Payment Orchestration for Stays](#stay-payments)) | Decide whether a refund is due |
| **Reservation** | Store versions; deliver to the supplier; track acknowledgement | State machine and delivery ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)) | Hold a second copy of the policy rules |
| **Case management** | Exceptions, goodwill, approvals above thresholds | Cases and recovery decisions ([When Something Goes Wrong: Customer Service and Recovery](#customer-service)) | Override penalties except through the engine's goodwill override type |

{id: changes-and-cancellations--the-engine-as-a-pure-function}
### The engine as a pure function

The engine is a pure function: the same inputs always give the same decision.

| Input | Example |
| --- | --- |
| Policy snapshots | Guest-facing `NKW-MODERATE v3`; supplier-facing identical |
| Reservation version | Stay 6–10 June 2027, 4 nights, 2 adults 2 children; itemized price lines |
| Payment arrangement | Facilitated; guest paid in full; host payout due 48 hours after check-in |
| Action and actor | Cancel, by guest |
| Instant | 3 June 2027 18:20 in the listing's time zone (Europe/Madrid) |
| Overrides | Active declared events matched to this reservation; package flag; any goodwill override with its approver |

The output is a **decision record**, not a number:

| Field | Content |
| --- | --- |
| `allowed` | Whether the action is permitted, and if not, why (past checkout, already canceled, supplier approval required) |
| `lines` | Itemized money lines per party: guest refund, supplier retained amount, marketplace fee retained or refunded, who funds each line |
| `effective_policy` | Which policy, window and override applied, with versions |
| `deadline_next` | When the outcome changes next ("full refund until 30 May 23:59 Europe/Madrid" has passed; "no refund of nights from 4 June 18:00") |
| `explanation` | Message keys and parameters for rendering in every language |
| `engine_version`, `decision_id` | For replay, audit and support |

Three rules come with it.

1. **Every channel asks the engine.** The property page ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection)), the confirmation e-mail, self-service, the support tool, the Pay Later charge scheduler ([Paying for a Future Night: Payment Orchestration for Stays](#stay-payments)) and any AI support agent call the same API. Nothing paraphrases the rule.
2. **Times are evaluated in the place of the stay.** Deadlines are instants with an explicit offset in the property's or listing's time zone.
3. **Decisions are replayable.** A versioned, pure engine can replay last month's cancellations against a new version before it ships: that is how a policy change gets a test and a disputed refund gets an answer.

{id: changes-and-cancellations--policy-versioning}
### Policy versioning

Policies change in three ways, and each needs a different rule.

| Change | Example | Rule |
| --- | --- | --- |
| **A supplier edits a rate plan's policy** | A hotel shortens its free-cancellation window from 3 days to 1 | Applies to new bookings only. Existing reservations keep their snapshot. |
| **The platform changes a template** | Nookaway tightens its Moderate tier | New template version; existing reservations keep the version they were booked under. Migrating existing bookings is a consumer-law decision, not a deploy. |
| **The engine's interpretation changes** | A fix to how partial nights round | New engine version, replayed against recent decisions before release; differences reviewed. |

The first rule is often broken: a reservation that stores a `rate_plan_id` and looks up the policy at cancellation time lets a revenue manager's edit in October change what an August guest is owed.

{id: changes-and-cancellations--modifications-a-new-version-not-an-edit}
## Modifications: A New Version, Not an Edit

Changing dates means checking availability, re-pricing, deciding whether the original policy still applies, changing the payment plan, and telling a supplier who may need to accept. The public partner APIs show the range.

- **Expedia's Rapid API** separates "soft" changes (such as guest name) from a **Hard Change** for "date, room type, and occupancy modifications": new dates "must be no more than one year after the original booked dates", "Change or cancellation penalties are determined by the property", the itinerary number is kept, and partners "should do an Itinerary Retrieve to confirm the changes have been applied" ([Expedia Group, Hard Change](https://developers.expediagroup.com/rapid/lodging/manage-booking/hard-change), live page, fetched October 2026).
- **Airbnb alterations need the host.** A date change request goes to the host; if declined or unanswered, the reservation stays as it was; price differences are charged or refunded ([Airbnb Help Center, Change the dates of your home reservation](https://www.airbnb.com/help/article/913), live page, fetched October 2026).
- **OpenTravel modification messages** are full overlays of the reservation, and need the same acknowledgement discipline as new bookings ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)).

{id: changes-and-cancellations--types-of-modification}
### Types of modification

| Change | Re-price? | Re-check availability? | Supplier must accept? | Typical policy rule |
| --- | --- | --- | --- | --- |
| Guest name, arrival time, requests | No | No | No; must be delivered | Free |
| Add or remove a guest | Often (occupancy pricing, tourist tax) | Capacity only | Hotel: usually no; host: yes | Price difference only |
| Shorten the stay | Yes (length-of-stay pricing may rise per night) | No | Hotel: no; host: yes | Removed nights treated as a partial cancellation under the policy |
| Extend the stay | Yes | Yes | Hotel: no if available; host: yes | Added nights at current price |
| Move dates | Yes | Yes | Hotel: no if available and rate allows; host: yes | Product rule: carry over the original policy or apply the new offer's |
| Change room type or rate plan | Yes | Yes | Hotel: no if available | New rate's policy applies |

Two product rules must be explicit, because the engine cannot guess them.

1. **Does the original policy carry over?** My rule: carry the original policy over for a guest-initiated change on a refundable rate; apply the new offer's policy for a change of rate plan; allow non-refundable changes only through a supplier-accepted request or a declared event. (Rapid hides changes when the penalty equals the booking value.)
2. **Is a change a modification or a cancel-and-rebook?** Cancel-and-rebook is simpler to build and breaks four things: the original penalty may apply, the guest loses history and loyalty status, reviews and messages attach to two records, and the supplier may receive the cancellation and the new booking out of order. Model a modification as a new **version** of the same reservation ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)); reserve cancel-and-rebook for changes the supplier's channel cannot express, such as moving to another property.

{id: changes-and-cancellations--the-self-service-change-flow}
### The self-service change flow

![Swimlanes for guest, change orchestrator, policy engine, payments and property or host: new dates, a change quote, acceptance, delivery and acknowledgement of the modification, a new payment plan version, and confirmation of version two.](stays-marketplace-architecture/posts/23-changes-and-cancellations/assets/images/23-changes-and-cancellations/23-self-service-date-change.jpeg)

**Figure 3:** *A self-service date change. The guest sees one change quote; the orchestrator confirms the new version only after the supplier acknowledges or accepts and the payment plan is versioned.*

The flow is a saga ([Garcia-Molina and Salem, 1987](https://dl.acm.org/doi/10.1145/38713.38742)) with the same design questions as checkout ([Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration)): where the **pivot**, "the point of no return" ([Microsoft, Saga design pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga), 2025), sits, and what compensates a failure after it.

- **Quote validity.** The change quote is binding for a short window, using the same mechanism as Roomstead's 15-minute checkout quotes ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)).
- **Supplier first, money second.** For hotels, wait for the PMS to acknowledge the modification before moving money; a rejected modification must not leave a charged guest. For hosts, the host's acceptance is the pivot.
- **Timers.** A host change request needs a response window and a default outcome; on a stay starting within 72 hours, Nookaway's usual 24 hours is too long.
- **Show the difference.** Whoever approves a change sees the old version, the new version and the money difference side by side.

{id: changes-and-cancellations--host-and-property-cancellations}
## Host and Property Cancellations

When the supplier cancels, the guest asks "where do I sleep", and the two marketplace types answer differently.

**Hotels cancel mostly by overbooking**, and industry practice is to "walk" the guest to a comparable nearby hotel at the property's cost. Booking.com's documentation says its customer service "will notify both the guest and the property to arrange either an alternative room or a relocation for the guest" ([Booking.com Connectivity, Troubleshooting overbookings](https://developers.booking.com/connectivity/docs/con-faq-reservations-troubleshooting-overbookings), live page, fetched October 2026); partner terms usually say who pays. Corvane's King's Day overbooking at Hotel Prinsenkade, where Roomstead relocated four guests for **€2,150** and recovered **€1,600** from the hotel, is the worked case in [When Something Goes Wrong: Customer Service and Recovery](#customer-service).

**Hosts cancel individually, and the platform enforces reliability through money.** Airbnb documents host cancellation fees of 10%, 25% or 50% of the reservation amount depending on timing (minimum USD 50), plus calendar blocks "even when the fee is waived" ([Airbnb Help Center, Host cancellation fees](https://www.airbnb.com/help/article/990), live page, fetched October 2026); Vrbo treats a decline after 24 hours as a cancellation ([Vrbo Help](https://help.vrbo.com/articles/IPM-About-booking-requests-for-integrated-accounts), live page, fetched October 2026). These penalties work because the platform controls the host's next payout ([Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement)). Nookaway charged Carmen Ruiz a **€130** fee, 10% of the nightly subtotal, after she canceled the Seville booking in February ([One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync)).

Three design rules apply to both.

1. **Supplier cancellations are a different action with a different policy**: the engine evaluates the supplier-penalty policy (fees, calendar block, metrics) and the guest-remedy policy (refund, rebooking, credit), not the guest's cancellation policy.
2. **Relocation is a linked reservation, not a ticket note.** The original closes as "relocated", and the cost difference is a ledger line with a liable party; a relocation recorded only as a support case loses the liability trail and counts the stay twice.
3. **Reason codes carry consequences.** "Host canceled: double booking via iCal", "property canceled: overbooking" and "canceled under declared event" lead to different fees, metrics and ranking effects; free text cannot be enforced.

**No-shows** are supplier-reported state changes owned by [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle); the engine evaluates the no-show fee from the snapshot as it evaluates a late cancellation.

{id: changes-and-cancellations--mass-disruption-declared-events-instead-of-ten-thousand-tickets}
## Mass Disruption: Declared Events Instead of Ten Thousand Tickets

When something happens to a place or a transport system, thousands of bookings need the same decision at once. On a platform **built for sunny days** the only override is an agent's judgement, one case at a time, when agents are scarcest.

{id: changes-and-cancellations--what-the-public-record-shows}
### What the public record shows

The pandemic is the documented case (evidence from 2020; the policies have since changed). Airbnb wrote that in March 2020 it "applied its extenuating circumstances policy to cancellations resulting from COVID-19", "committed up to $250 million for hosts impacted by COVID-19", paying eligible hosts 25% of what their cancellation policy would have given them, and recorded "$205.1 million of payments, primarily for hosts" in 2020 ([Airbnb FY2020 10-K](https://www.sec.gov/Archives/edgar/data/1559720/000155972021000010/airbnb-10k.htm), 2021). Booking Holdings reported "higher than normal cash outlays to refund consumers for prepaid reservations" ([Booking Holdings FY2020 10-K](https://www.sec.gov/Archives/edgar/data/1075531/000107553121000019/bkng-20201231.htm), 2021), and Expedia "significant spikes in customer support call volumes" ([Expedia Group FY2020 10-K](https://www.sec.gov/Archives/edgar/data/1324424/000132442421000015/expe-20201231.htm), 2021).

Commission Recommendation (EU) 2020/648 described fair **vouchers** as an alternative to cash refunds, subject to the traveler's "voluntary acceptance": at least 12 months' validity and automatic reimbursement "at the latest 14 days after the end of its validity period" if unused ([Commission Recommendation (EU) 2020/648](http://publications.europa.eu/resource/celex/32020H0648), 2020). It covers transport and packages, not hotel-only bookings, but is the clearest official statement of what a fair credit looks like.

Airbnb's current policy shows how such events became data. Its **Major Disruptive Events** policy, which replaced the extenuating circumstances name, covers events after booking that affect the reservation's location and prevent or legally prohibit the stay, such as declared public-health emergencies, government travel restrictions and unforeseeable natural disasters. It excludes events affecting only the guest, illness, transport disruptions and foreseeable weather; hosts can cancel without fees but are not paid; and it "is not an insurance policy" ([Airbnb Help Center, Major Disruptive Events Policy](https://www.airbnb.com/help/article/1320), live page, fetched October 2026). The page states that coverage "applies only to the defined area and timeframe"; it does not give the date the policy was renamed. The June 2027 strike was exactly the kind of event it excludes, because it affected the guest's journey, not the destination; a marketplace must decide in advance whether and how it responds to such events.

> **INFERENCE, NOT DOCUMENTED:** The phrase "the defined area and timeframe" suggests an event entity with a geography and a window that is matched against reservations. Airbnb has not published how its policy is implemented; the registry described below is a reference architecture, not a description of Airbnb's systems.

{id: changes-and-cancellations--the-declared-event}
### The declared event

A **declared disruption event** is a record with an owner, created when something happens and applied by machines.

| Field | Example: ATC strike, June 2027 |
| --- | --- |
| `class` | `TRAVEL_DISRUPTED` (guests cannot reach the destination) vs `STAY_PREVENTED` (the destination is affected) |
| `places` | Place IDs or polygons from the destination graph ([Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps)); for a transport event, the affected routes and the origin markets of guests |
| `stay_window` | Check-in 5–9 June 2027, and check-out 5–8 June for guests stranded at their destination |
| `booking_cutoff` | Bookings made before 3 June 2027 12:00 CEST, when the strike was announced; later bookings knew the risk |
| `party_filter` | Guests whose origin market or itinerary is affected (for transport events); all guests (for destination events) |
| `override` | The policy outcome per payment model, by reference to a versioned disruption policy |
| `funding` | Who pays each line: marketplace, supplier, guest; budget cap and alert |
| `owner`, `approver`, `expires_at`, `version` | Named roles, legal review for regulated markets, an expiry so events cannot linger |

Without a **booking cutoff**, the disruption policy becomes free flexibility for anyone who books into it. The **party filter** makes transport events tractable: a strike over France does not affect a Lisbon guest flying from Porto. Corvane rarely knows the guest's flight, so origin market is the first approximation, and guests outside the filter can still request an exception.

{id: changes-and-cancellations--the-batch-path}
### The batch path

![A declared event enters the disruption registry; a matcher selects the affected reservations, the policy engine computes options, guests are notified and choose in self-service, the change orchestrator executes into payments, waiver requests go to properties and hosts, and finance tracks the budget.](stays-marketplace-architecture/posts/23-changes-and-cancellations/assets/images/23-changes-and-cancellations/23-declared-event-batch.jpeg)

**Figure 4:** *A declared event as a batch. The registry matches affected reservations, the engine computes their options, the change orchestrator executes what guests choose, and finance watches spend against the event's budget.*

Four rules make the batch path safe.

1. **Notify, then let the guest choose.** A declared event changes what the engine returns; it does not cancel reservations, because many guests still travel. The notification states the options with amounts, and self-service executes the choice.
2. **Idempotent and resumable.** Every decision is keyed by reservation version and event version, so a rerun after the event is edited never refunds twice.
3. **Capacity planned for the spike.** Self-service, the engine and payments must absorb a multiple of a normal day's refunds ([Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability)); the support queue is the overflow, not the main path.
4. **Supply-side effects are part of the event.** Calendars of canceled stays reopen or stay blocked according to the class; pricing models are told about the event so they do not read disruption cancellations as falling demand ([Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing)); ranking does not penalize suppliers for cancellations under a declared event ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)).

{id: changes-and-cancellations--waive-what-you-hold-request-what-you-do-not}
### Waive what you hold, request what you do not

The rule I use: **the marketplace waives its own share, asks the supplier to waive the supplier's share, and never refunds supplier money it does not hold as if it were its own.** It may still fund a guest remedy itself, as a recorded marketplace expense, not a waiver.

| Line | Agency (Roomstead) | Merchant (Roomstead) | Facilitated (Nookaway) |
| --- | --- | --- | --- |
| Marketplace fee or commission | Waive the commission on the canceled booking | Refund the margin share to the guest | Refund the guest service fee; waive the host fee |
| Supplier share under the policy | **Request** a waiver from the property; the property decides | **Request** a waiver; void or resize the virtual card only after acceptance or if not yet chargeable | **Request** a waiver from the host for `TRAVEL_DISRUPTED`; override for `STAY_PREVENTED` with the host paid nothing and charged no fee |
| Guest remedy if the supplier declines | Marketplace-funded credit, if the event's policy says so | Marketplace-funded credit or refund, booked as marketplace expense | Marketplace-funded credit or refund, booked as marketplace expense |
| Supplier-facing message | Cancellation with structured waiver code, acknowledged | Same, plus card status | Host notification with the event and the options |

![Three columns for agency, merchant and facilitated models showing where the guest's money sits, inside the hotel or held by the marketplace, with a waiver request sent to the hotel or host in each.](stays-marketplace-architecture/posts/23-changes-and-cancellations/assets/images/23-changes-and-cancellations/23-waive-what-you-hold.jpeg)

**Figure 5:** *The marketplace waives its own share and asks the supplier to waive theirs; it never refunds supplier money it does not hold as if it were its own.*

{id: changes-and-cancellations--in-practice-corvane-s-redesign}
## In Practice: Corvane's Redesign

{id: changes-and-cancellations--clause-and-disruption-policy-v1}
### Clause and Disruption Policy v1

In **July 2027** the architecture forum approved **Clause**, a group cancellation policy engine and disruption registry, as part of the One Stay program. Clause is owned by the group booking platform team in Lisbon; policy content is owned by the brands' commercial teams, with Noor van Dijk's regulatory team as mandatory reviewer of templates and disruption policies. The forum agreed five decisions.

1. **One engine, many channels.** Clause answers every policy question for both brands. Burrow, Nookaway's Django monolith, called it from **November 2027**; Roomstead merchant bookings move in **Q2 2028**; Keystone's agency path from **Q4 2028**, a year before Keystone's reservation module is retired.
2. **Two snapshots per reservation.** Every reservation version in Stayline, the One Stay reservation service ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)), stores the guest-facing and supplier-facing policy versions and the Clause decision; any difference has a ledger account in Fathom, the group ledger.
3. **Support overrides are engine inputs.** The macro and the flag were removed. Agents choose a typed override (goodwill credit, supplier-accepted waiver, declared event, legal requirement) with a reason code and an approval threshold.
4. **Disruption Policy v1.** Two event classes. `STAY_PREVENTED`: on Nookaway, full refund to the guest, and hosts receive no payout and pay no fee; on Roomstead, waiver requests go to properties with a 12-hour answer target, virtual-card activation is held for merchant bookings, and if a property declines, Roomstead funds the guest's refund as a recorded marketplace expense within the event budget. `TRAVEL_DISRUPTED`: guests may move dates free of change fees, subject to availability and supplier acceptance; or cancel under their policy with the marketplace's own fees refunded and waiver requests sent to the supplier; Roomstead may add a credit for Roomstead Circle members, its loyalty program ([Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty)), funded from a capped event budget.
5. **Events have owners and budgets.** Declaring an event needs the brand's VP of customer service and a finance approver, and every event carries a budget and an expiry.

Nookaway's cancellation tiers, Burrow code paths since 2014, became Clause templates.

| Nookaway tier (template v3, 2027) | Full refund of nights until | Then | Cleaning fee | Guest service fee |
| --- | --- | --- | --- | --- |
| Flexible | 48 hours before check-in | First night retained | Refunded if canceled before check-in | Refunded in proportion to the refunded subtotal |
| Moderate | 7 days before check-in | 50% of nights refunded until 48 hours before; none after | Refunded if canceled before check-in | Same |
| Strict | 21 days before check-in | 50% until 7 days before; none after | Refunded if canceled before check-in | Same |
| Non-refundable (10% discount) | — | None | Refunded if canceled before check-in | Not refunded |

All tiers include a full refund within 24 hours of booking for stays at least 14 days away, and deadlines are evaluated in the listing's time zone. Host cancellation fees moved into Clause as a schedule: **10%** of the nightly subtotal more than 14 days before check-in, **20%** within 14 days, **30%** within 48 hours or after check-in, with the dates blocked in every case.

{id: changes-and-cancellations--worked-example-1-a-seville-family-under-three-regimes}
### Worked example 1: a Seville family under three regimes

A family from Lyon had booked Carmen Ruiz's apartment in Triana, Seville, for **6–10 June 2027**: 4 nights × **€110** = €440, plus the **€60** cleaning fee, a subtotal of **€500**. Nookaway's 12% guest service fee was **€60**, so the guest paid **€560** (taxes are left out of this simplified example). Carmen's listing uses the Moderate tier. On **3 June at 18:20** Seville time, after the strike was announced, the family canceled, three days before check-in.

| Line | Moderate policy alone | June 2027: extenuating-circumstances flag | Disruption Policy v1, `TRAVEL_DISRUPTED` |
| --- | --- | --- | --- |
| Nights refunded | 50% of €440 = €220 | €440 | €220 (Carmen declined the waiver request) |
| Cleaning fee refunded | €60 | €60 | €60 |
| Guest service fee refunded | €60 × (280 ÷ 500) = €33.60 | €60 | €60 (marketplace waives its own fee) |
| **Guest refund** | **€313.60** | **€560.00** | **€340.00** |
| Carmen's payout | €220 − 4% host fee = €211.20 | €0 | €220, host fee waived: **€220.00** |
| Nookaway keeps | €26.40 + €8.80 = €35.20 | €0 | €0 |

Under v1, Nookaway gives up the €35.20 it would have kept, Carmen keeps what her policy promised, and the family is first offered a free date change if Carmen accepts one. Had the family booked a package with the flight, the package organizer, not Nookaway, would owe the refund.

{id: changes-and-cancellations--worked-example-2-a-merchant-booking-at-hotel-miradouro}
### Worked example 2: a merchant booking at Hotel Miradouro

A couple from Brussels had a Pay with Roomstead reservation at Hotel Miradouro in Lisbon for **5–8 June 2027** on the non-refundable rate with breakfast: 3 nights × **€137.60** = **€412.80**. Miradouro's commission is 15%, so Corvane Payments loaded a virtual card net of commission with **€350.88**. Under the pre-v1 default the card was chargeable from booking because the rate was non-refundable.

- **June 2027.** An agent applied the macro on 4 June and refunded €412.80. Miradouro's PMS showed a canceled non-refundable rate, the hotel charged the card on 5 June, and Corvane Payments recovered the money only in July, when Duarte Silva, Miradouro's revenue manager, agreed to a refund.
- **Under v1.** Clause returns: cancellation not refundable under the supplier policy; a `TRAVEL_DISRUPTED` waiver request sent to the property through the extranet and the connectivity channel with a 12-hour answer target; marketplace margin of **€61.92** refundable to the guest if the hotel declines. Duarte accepts a date move to **18–21 September** at the original price. The reservation becomes version 2, the PMS acknowledges the modification, and the payment plan moves the card's activation to the new check-in date.

{id: changes-and-cancellations--replaying-the-strike}
### Replaying the strike

In October 2027 the booking platform team replayed the June strike against Clause and Disruption Policy v1, using the 2027 reservation data. The replay is an estimate, not an outcome, and it assumed waiver acceptance rates from a September pilot.

| Measure | June 2027 actual | Replay under v1 |
| --- | --- | --- |
| Roomstead requests completed in self-service | 2,950 of 6,200 | about 5,100 of 6,200 |
| Roomstead support contacts | 3,250 | about 1,100 |
| Waivers promised without supplier consent | 1,860 | 0 (replaced by about 2,500 waiver requests) |
| Roomstead money spent on supplier-held amounts | about €199,100 | 0, plus about €58,000 of capped Circle credits |
| Nookaway full refunds at host expense | 1,050 | 0 for a transport event |
| Nookaway fees waived | not tracked | about €61,000 |

The forum's conclusion was not that June was too generous; Corvane could reasonably fund a strike-weekend gesture. The gesture had been funded **by accident**, in the wrong places, at a cost nobody saw until month-end.

{id: changes-and-cancellations--trade-offs}
## Trade-offs

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| **Where policy logic lives** | One central engine called by every channel | Each channel computes, from a shared library | Several channels, two brands, regulated markets: almost always | One channel and one team, small scale; the library drifts as soon as a second team forks it |
| **Policy reference on the reservation** | Snapshot (the full policy, versioned) | Reference to the live rate plan or listing policy | Always for existing reservations | Never, except for display before booking |
| **Date change model** | New version of the same reservation | Cancel and rebook | Same supplier and channel can express the change | Change to another property, or a channel that cannot modify |
| **Policy on changed dates** | Carry over the original policy | Apply the new offer's policy | Guest-initiated change on refundable rate; disruption-driven change | Change of rate plan or room type; abuse of flexible-to-peak moves |
| **Disruption remedy** | Cash refund | Credit or voucher | Package travelers (legal duty); stays prevented; markets where credits damage trust | Travel-disrupted cases with voluntary acceptance, clear validity and automatic cash-out at expiry |
| **Batch application** | Notify and let the guest choose | Cancel affected bookings automatically | Most events: many guests still travel | Destination closed by law; the stay cannot happen |

A shared library saves a network call on every page view, but the evaluation is cheap and cacheable per policy version and instant, and a library cannot give one version in production, one replay facility and one audit trail.

{id: changes-and-cancellations--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (OTA) | Hosted-stays marketplace |
| --- | --- | --- |
| **Who writes the policy** | The property, per rate plan; arrives in ARI feeds | The platform, as templates; the host chooses a tier |
| **Number of policies in play** | Many per property; several on one property page | One per listing at a time |
| **Who holds the money before arrival** | The property (agency) or the OTA until supplier payment (merchant) | The platform, until payout after check-in |
| **Who can waive a penalty** | The property; the OTA only by funding it | The platform can override; fairness to hosts is the constraint |
| **Modification approval** | Automatic if available and the rate allows; delivered to the PMS and acknowledged | Host approves most changes |
| **Supplier cancellation** | Rare, mostly overbooking; relocation to a comparable hotel at the property's cost | More frequent, individual; platform rehouses and charges a host fee |
| **Typical failure** | Platform promise not delivered or not acknowledged at the PMS; hotel charges the guest anyway (Lost at the Front Desk) | Platform overrides the host's policy inconsistently; hosts lose payouts without a rule |
| **Disruption response** | Ask thousands of properties for waivers through extranet and connectivity | Decide centrally, but owe hosts a predictable rule |
| **Regulation** | Package rules where flights or other services are combined; presentation rules | Same presentation rules; short-term-rental rules can force cancellations ([Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation)) |

**What to share.** The engine, the decision record, the disruption registry, the change orchestrator, the support override types and the self-service patterns: building them twice guarantees two answers. **What to keep separate.** Policy content (Nookaway templates, Roomstead supplier policies), supplier-facing message formats and the host-penalty schedule. The funding rule (what the group waives on its own account during an event, from one budget) must be decided at group level.

{id: changes-and-cancellations--failure-modes}
## Failure Modes

- **The live-policy lookup.** The reservation reads the rate plan's policy at cancellation time. *Symptom:* complaints spike after a partner edits policies. *Defense:* a versioned snapshot at booking.
- **The macro that moves money.** A macro or admin flag changes refunds outside the engine. *Symptom:* identical cases get different outcomes; finance cannot explain refund spend. *Defense:* typed overrides with reason, approver and threshold. This is **Policy Spaghetti** at its most expensive.
- **Unacknowledged changes.** A change sent without acknowledgement, or as free text the PMS does not show. *Symptom:* charges on canceled bookings. *Defense:* structured waiver and change codes, acknowledgement tracking ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)).
- **Time-zone drift.** *Symptom:* disputes clustered around deadline hours. *Defense:* compute in the stay's time zone; render from the decision.
- **Disruption read as demand.** *Symptom:* price cuts and supplier demotions after a strike. *Defense:* publish events to pricing and ranking; exclude event cancellations from reliability metrics.
- **Credits without a ledger.** *Symptom:* an unknown outstanding balance of vouchers and credits. *Defense:* credits are ledger accounts with expiry and cash-out rules ([Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation)).

{id: changes-and-cancellations--the-chief-architect-s-view}
## The Chief Architect's View

The decisions I would take to the architecture forum:

1. **Name the owner of policy evaluation.** One engine, one team, one API; this single change removes most Policy Spaghetti.
2. **Make the snapshot rule non-negotiable** in both brands; migrating Keystone's agency path is a prerequisite for retiring its reservation module.
3. **Agree the funding rule at group level.** The CFO, the brand leaders and regulatory affairs sign it before the next event, not during it.
4. **Build the disruption registry before you need it**: a table, a matcher, a batch and a dashboard, tested twice a year by replaying a past event.
5. **Treat support overrides as product.** Watch the override rate by reason; a rising "goodwill" share means a policy, not the agents, is wrong.

What to watch: self-service share of changes, refund spend by funder and reason, waiver acceptance by supplier segment, reservations whose two snapshots differ, and disputes where the guest quotes a different policy than the engine applied. Long term, the engine is also the safest interface for AI agents: an agent should call it, show the decision and execute through the orchestrator, never compute a refund ([AI Across the Stay: Agents, Assistants and Automation](#ai-in-travel-stays)).

{id: changes-and-cancellations--questions-to-ask}
## Questions to Ask

1. Where is the cancellation rule for an existing reservation evaluated today, and how many systems compute it independently?
2. Does every reservation store the policy as it was at booking, with a version, and can you show both the guest-facing and the supplier-facing policy?
3. In which time zone are deadlines computed and displayed, and is that the same in the e-mail, the app and the support tool?
4. When a guest changes dates, is that a new version of the same reservation or a cancellation and a new booking, and what does the property's PMS receive?
5. Which policy applies to changed nights, and where is that rule written down?
6. Can support agents change a refund outside the engine? If so, how would finance find out?
7. For each payment model, which money does the marketplace hold at each point before arrival, and does the engine know?
8. Could you declare a disruption event this afternoon with a place, a window, a booking cutoff and a budget, and how long would it take to notify affected guests?
9. Do pricing and ranking know which cancellations came from a declared event?

{id: changes-and-cancellations--from-changes-to-the-trip-itself}
## From Changes to the Trip Itself

A reservation that survives changes and disruptions still has to become a stay: the guest needs check-in instructions, a way to talk to the property or host, and timely word when plans move. [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) covers the trip timeline, guest–host messaging and the notification routing that carries every change described here.

{id: changes-and-cancellations--sources-and-evidence}
## Sources and Evidence

{id: changes-and-cancellations--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm) — Airbnb, Inc., 2026. The platform holds guest funds until check-in and remits after it; the basis for the platform's ability to override host policies.
- [Form 10-K for fiscal year 2020](https://www.sec.gov/Archives/edgar/data/1559720/000155972021000010/airbnb-10k.htm) — Airbnb, Inc., 2021. COVID-19 extenuating circumstances scope, the USD 250 million host commitment and USD 205.1 million paid.
- [Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm) — Booking Holdings Inc., 2026. Cancellable rates offered on behalf of partners; free cancellation for non-refundable reservations without estimated recovery.
- [Form 10-K for fiscal year 2020](https://www.sec.gov/Archives/edgar/data/1075531/000107553121000019/bkng-20201231.htm) — Booking Holdings Inc., 2021. Customer-service costs and refund outlays from pandemic cancellations.
- [Form 10-K for fiscal year 2020](https://www.sec.gov/Archives/edgar/data/1324424/000132442421000015/expe-20201231.htm) — Expedia Group, Inc., 2021. Widespread cancellations and support call spikes in 2020.
- [Cancellation policies for your listing](https://www.airbnb.com/help/article/475) — Airbnb Help Center, live page, fetched 2026. Policy tiers, 24-hour window, override by disruption policies.
- [Major Disruptive Events Policy](https://www.airbnb.com/help/article/1320) — Airbnb Help Center, live page, fetched 2026. Covered and excluded events, defined area and timeframe, host consequences.
- [Host cancellation fees](https://www.airbnb.com/help/article/990) — Airbnb Help Center, live page, fetched 2026. Fee schedule, calendar blocks and other consequences.
- [Change the dates of your home reservation](https://www.airbnb.com/help/article/913) — Airbnb Help Center, live page, fetched 2026. Host approval of alterations and price differences.
- [About booking requests for integrated accounts](https://help.vrbo.com/articles/IPM-About-booking-requests-for-integrated-accounts) — Vrbo Help, live page, fetched 2026. Declines after 24 hours count as cancellations.
- [Customer terms of service](https://www.booking.com/content/terms.html) — Booking.com, 2025 (updated 25 August 2025). The booking is with the service provider; refunds follow its policy.
- [Troubleshooting overbookings](https://developers.booking.com/connectivity/docs/con-faq-reservations-troubleshooting-overbookings) — Booking.com Connectivity, n.d. Customer service arranges an alternative room or relocation.
- [Hard Change](https://developers.expediagroup.com/rapid/lodging/manage-booking/hard-change) — Expedia Group Developer Hub, n.d. Date, room and occupancy modifications, one-year limit, property-determined penalties, retrieve after commit.
- [Constructing cancellation policies](https://developers.expediagroup.com/rapid/lodging/shopping/constructing-cancellation-policies) — Expedia Group Developer Hub, n.d. Cancellation policies as typed time windows with authoritative offsets.

{id: changes-and-cancellations--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Directive 2011/83/EU on consumer rights](http://publications.europa.eu/resource/celex/32011L0083) — European Parliament and Council, 2011. Article 16(l): no withdrawal right for accommodation with a specific date.
- [Directive 2005/29/EC on unfair commercial practices](http://publications.europa.eu/resource/celex/32005L0029) — European Parliament and Council, 2005. Article 6: misleading information on the main characteristics of a product.
- [Directive (EU) 2015/2302 on package travel and linked travel arrangements](http://publications.europa.eu/resource/celex/32015L2302) — European Parliament and Council, 2015. Unavoidable and extraordinary circumstances; termination rights and 14-day refunds.
- [Package Travel Directive](https://commission.europa.eu/law/law-topic/consumer-protection-law/travel-and-timeshare-law/package-travel-directive_en) — European Commission, live page, fetched 2026. Amendment by Directive (EU) 2026/1024 and its transposition period.
- [Commission Recommendation (EU) 2020/648 on vouchers](http://publications.europa.eu/resource/celex/32020H0648) — European Commission, 2020. Characteristics of fair vouchers offered instead of cash refunds.
- [Saga design pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga) — Microsoft Azure Architecture Center, 2025. Pivot transactions and compensations, for the change saga.

{id: changes-and-cancellations--research-and-practitioner-sources}
### Research and practitioner sources

- [Sagas](https://dl.acm.org/doi/10.1145/38713.38742) — Hector Garcia-Molina and Kenneth Salem, SIGMOD 1987. Origin of the saga pattern used for change orchestration.
- [Provisional agreement reached on Package Travel Directive revision](https://www.travelextra.ie/provisional-agreement-reached-on-package-travel-directive-revision/) — Travel Extra, 2025. Press report on the revision's voucher and refund rules; secondary source.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
