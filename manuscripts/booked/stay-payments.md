{id: stay-payments}
# 27. Paying for a Future Night: Payment Orchestration for Stays

![Paying for a Future Night: Payment Orchestration for Stays — logo](stays-marketplace-architecture/posts/27-stay-payments/assets/images/27-stay-payments/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Take apart the payment side of a stays booking: when the guest pays (now, later, in parts, at the property), how deferred charges survive Strong Customer Authentication, how a marketplace pays hotels with virtual cards, how deposits, currencies and chargebacks work, and how one orchestration layer with a payment state feed holds it all together.

> **WHY THE BUSINESS CARES:** Flexible payment timing sells nights. Pay-later options, local methods and the guest's own currency raise conversion, but each one adds a promise to collect money later, which can fail. A finance chief needs to know how much booked value has not yet been collected, what share of it will be, and who absorbs the loss when it is not.

> **WHY ARCHITECTS SHOULD CARE:** A stays payment is not a checkout event; it is a schedule of obligations that lives for weeks and changes with every modification, cancellation and dispute. If that schedule is hidden in checkout code, cron jobs and the payment service provider's dashboard, nobody can say what the guest owes, what the property is owed, or why a charge failed.

> **KEY POINTS:**
>
> * **A stays payment is a plan, not a transaction.** Model each booking's money as a versioned **payment plan**: charges, holds, virtual cards and refunds with due dates, tied to the cancellation policy. One orchestration layer executes the plan, and a payment state feed tells the reservation, the ledger and payouts what actually happened.
> * **Every deferred charge depends on what you stored at checkout.** Pay later, balance payments, no-show fees and damage charges are merchant-initiated transactions. They work only if the card was set up with Strong Customer Authentication and the scheme's transaction reference was kept. Treat a chargeable credential as a precondition of the booking, not as a detail of the app.
> * **Hotels and homes need different rails on one platform.** Hotels are paid by single-use virtual cards that fit their card terminals; hosts are paid out to accounts after check-in; hosted-stays guests need deposits and staged payments. Share the orchestration, the instrument vault, the risk checks and the ledger feed. Keep the supply-side rails separate.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Ledgerless Money** — Deferred charges, virtual cards and deposits move money on schedules that nothing records as obligations, so nobody can say what is owed, collected or at risk.
> * **Policy Spaghetti** — The charge date of a pay-later booking depends on the cancellation policy, and when checkout, the scheduler and support each compute it, they give different answers.
> * **Price Drift** — Currency conversion, conversion at the point of sale and fees added at different steps make the amount on the card statement differ from the amount the guest agreed to.

A guest who books a stay in February for August buys a promise that two other parties will keep months later: the property or host will provide the night, and the marketplace will move the money. Between booking and stay the guest may change dates, cancel, dispute a charge or let a card expire. The property may cancel or change the price. The currency may move. The payment side of a stays marketplace therefore works with **time**: much of the money is collected, held, released or returned weeks after the checkout page closed.

Retail checkout, one authorization and one capture within days, does not prepare an architect for this. A stays guest may **pay now** for a night months away, **pay later** on a date the marketplace promises to charge, **pay at the property**, or **pay in parts**; on top come incidental holds, post-stay damage charges, and the single-use virtual cards with which an online travel agency (OTA) pays hotels. Each is a different contract with the guest, the supplier and the card schemes.

![A short retail timeline with two close dots above a long stays timeline with charge, hold, card and refund markers spread between booking and stay.](stays-marketplace-architecture/posts/27-stay-payments/assets/images/27-stay-payments/27-plan-not-transaction.jpeg)

**Figure 1:** *A retail payment is one authorization and one capture within days; a stays payment is a plan of charges, holds, cards and refunds that lives from booking to stay and beyond.*

This chapter is the second in Part VI ([Part VI — MONEY: Who Pays Whom, When and How Much](#part-6)). [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models) decides *who* is the merchant of record for each booking; this chapter decides *how and when* that merchant takes the money. It owns the **deferred charge**, the **virtual card** (VCC) and **payment orchestration** for stays. It does not re-teach card payments in general, which RECONCILED covers in [Payments for Finance Architects: Eleven Reasons the Numbers Disagree](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-fundamentals.html) together with the provider chapters [Adyen: One Platform from Checkout to Settlement](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/adyen.html) and [Stripe: Every Movement Is a Balance Transaction](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/stripe.html). Paying the supply side and the settlement ledger belong to [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement), and refunds, chargeback accounting and reconciliation to [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation).

{id: stay-payments--setting-the-scene-at-corvane-the-semana-santa-charges-that-would-not-go-through}
## Setting the Scene at Corvane: The Semana Santa Charges That Would Not Go Through

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), launched **Pay Later** on Nookaway, its hosted-stays marketplace, in **October 2026**. Guests booking a listing with a flexible or moderate cancellation policy could reserve with nothing due. Corvane Payments, the group's electronic money institution (EMI), stored the guest's card and charged the full guest total automatically **10 days before the listing's free-cancellation deadline**. If that charge failed and retries did not recover it, the guest could pay by another method until the deadline. At the deadline an unpaid reservation was canceled without charge and the nights went back on the calendar. The 10-day lead time was the design's promise to hosts: if a guest did not pay, the host would still have time to resell the nights.

By March 2027 Pay Later had taken **31%** of eligible Nookaway bookings. About **410,000** Pay Later reservations with check-in after 1 March were confirmed but not yet charged, about **€228 million** of guest totals that Corvane had promised to hosts and not yet collected. Marco Bellini, the Group CFO, had asked for that number every week since January.

In the first week of March, the scheduler ran the charges for stays starting in the second half of the month: Semana Santa (Holy Week, 21–28 March 2027) and Easter, the busiest fortnight of the spring in Andalusia and Portugal.

| 1–7 March 2027 | Charges | Declined on first attempt | Main decline reason |
| --- | --- | --- | --- |
| All scheduled Pay Later charges | **38,400** | 5,435 (14.2%) | — |
| Cards stored through the iOS app since 12 December 2026 | 6,950 | **4,240 (61%)** | Issuer requires authentication |
| All other cards | 31,450 | 1,195 (3.8%) | Insufficient funds, expired card |

Leila Haddad's payments engineering team traced the cluster to one release. A new iOS checkout, shipped on **12 December 2026**, saved the card with a zero-amount verification flagged as a one-off, customer-present payment rather than as the setup of a stored credential for later charges. The card was tokenized correctly and the guest had completed Strong Customer Authentication (SCA). But the app did not ask the acquirer to register the card for merchant-initiated use, so Corvane never received or stored the **scheme transaction reference** that later charges must quote. When the scheduler charged those cards weeks later as merchant-initiated transactions, many issuers, mostly Spanish and Italian banks, treated them as unauthenticated remote payments and answered with a soft decline: authentication required. The guest, who was not in the app, could not authenticate. About **52,000** Pay Later reservations carried such a credential before a fix shipped on 24 February.

![Two keys: one with a reference notch opens a vault door, one without it is stuck with 61% declined, beside an empty chair.](stays-marketplace-architecture/posts/27-stay-payments/assets/images/27-stay-payments/27-missing-reference.jpeg)

**Figure 2:** *Cards saved by the iOS app from 12 December 2026 had no scheme transaction reference, so 61% of their scheduled Pay Later charges were declined in the first week of March 2027, when the guest was not there to authenticate.*

The recovery plan worked, but slowly. On 4 March Rafael Mendes (VP Engineering, Nookaway) and Leila paused automatic cancellation for the affected bookings and sent each guest a link to re-authenticate the card. **3,310** of the 4,240 declined guests paid within the extended window. **930** did not, and those reservations were canceled with less than two weeks to arrival; **402** of the reopened calendars did not resell. Nookaway paid those hosts **€118,000** in goodwill, about one night of Semana Santa payout each. The other **45,050** affected guests, whose charges were due later, were asked to re-confirm their cards in advance; 88% did.

Mariana Costa, the Group Chief Architect, took the post-incident review to the architecture forum with a broader question. The defect was one flag in one app. But nothing in the platform had checked, at booking time, that a Pay Later reservation held a credential that could actually be charged later. Nothing had tracked the decline rate of scheduled charges by app version. And Roomstead, the group's OTA, planned to offer the same pay-later option on its merchant bookings in 2028. **What should own a booking's future payments, and what must it verify before it accepts a promise to collect?**

{id: stay-payments--concepts-a-payment-that-outlives-the-checkout}
## Concepts: A Payment That Outlives the Checkout

{id: stay-payments--payment-timing}
### Payment timing

The first concept is **payment timing**: when the guest's money moves, relative to booking and stay. It is a property of the offer, chosen at checkout, and it must be fixed on the reservation, because the cancellation, refund and accounting rules all depend on it.

| Timing | What the guest does at checkout | What the marketplace holds afterwards | Public example |
| --- | --- | --- | --- |
| **Pay now** | Authorizes and pays the full amount | Captured funds and a refund liability until the booking becomes non-refundable | Airbnb standard checkout; Expedia Collect; Booking.com online payment |
| **Pay at property** | Gives a card as a guarantee, or nothing | A card guarantee passed on to the property; no funds | Booking.com pay at property; Expedia Hotel Collect |
| **Pay later online** | Stores a payment method; pays nothing now | A promise to charge on a date; a stored credential | Airbnb Reserve Now, Pay Later; Booking.com "pay online later" |
| **Pay in parts** | Pays a deposit now | A stored credential for the balance | Airbnb Pay Part Now, Part Later; Vrbo payment schedules |
| **Third-party installments** | Is redirected to a buy-now-pay-later provider | A confirmed payment from the provider, which carries the credit risk | Klarna, Affirm or PayPal Credit through Payments by Booking.com |

The examples are documented. Booking.com's Demand API lets an offer declare which payment methods and timings it allows (`payment.timing`), and in its partner-collects flow requires the partner's virtual card to be funded at least two days before a pay-later collection date ([Booking.com Developers](https://developers.booking.com/demand/docs/payments/models/partner-collects), n.d., fetched October 2026). Airbnb launched Reserve Now, Pay Later for US guests on **14 August 2025** and extended it worldwide on **17 February 2026**, for listings with moderate or flexible cancellation policies; it reported adoption of "over 70 percent" of eligible bookings in the fourth quarter of 2025 ([Airbnb, 2026](https://news.airbnb.com/reserve-now-pay-later-is-now-available-worldwide/)). Its design rule is stated plainly: "because the payment from guests is always due before the free cancellation period ends, hosts have time to secure another booking even if a guest cancels" ([Airbnb, 23 February 2026](https://news.airbnb.com/introducing-reserve-now-pay-later-giving-guests-greater-flexibility/)). Airbnb's Payments Terms, as published in February 2026, add that the original payment method is charged automatically and that, if the charge fails, the guest has **72 hours** to pay by another method or the booking may be canceled ([Airbnb Payments Terms, 2026](https://www.airbnb.com/help/article/2909)).

Pay later moves cash and risk, not just a button. Airbnb's 6 August 2026 shareholder letter said unearned fees would have grown year on year absent Reserve Now, Pay Later bookings, "which defer guest payments from the time of booking closer to the date of stay" ([Airbnb Q2 2026 shareholder letter](https://investors.airbnb.com/)), and its FY2025 annual report lists "unbilled amounts for confirmed bookings" under its pay-later programs among its foreign-currency exposures ([Airbnb 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm)).

{id: stay-payments--deferred-charge}
### Deferred charge

A **deferred charge** is any charge the marketplace makes after checkout, without the guest present, under an agreement the guest accepted at checkout: pay-later collections, balances, no-show and late-cancellation fees, long-stay installments and post-stay damage charges. All of them **can fail when nobody is there to fix it**, so a decline needs retries, notifications and a deadline rather than an error message. All are **tied to the cancellation policy**, from which the charge date or penalty is derived. And all **depend on what was stored at checkout**: the card, the guest's consent and the scheme reference from the first authentication.

{id: stay-payments--customer-initiated-and-merchant-initiated-transactions}
### Customer-initiated and merchant-initiated transactions

Card schemes and payment service providers (PSPs) distinguish **customer-initiated transactions** (CIT), where the cardholder takes part, from **merchant-initiated transactions** (MIT), which the merchant starts later under a prior agreement with the cardholder. The distinction comes from card-scheme rules and European Banking Authority guidance; Stripe's summary treats MITs as outside the scope of SCA, provided the card was authenticated when it was first saved or first charged, and notes that the issuing bank makes the final decision ([Stripe SCA guide](https://stripe.com/guides/strong-customer-authentication), n.d., fetched October 2026). In practice the first CIT returns a **network transaction identifier** (a scheme-level reference to that authenticated setup), and each later MIT quotes it. That reference is what Nookaway's iOS app failed to obtain.

{id: stay-payments--strong-customer-authentication-and-the-exemptions-that-rarely-fit-stays}
### Strong Customer Authentication and the exemptions that rarely fit stays

The revised Payment Services Directive (PSD2) requires a payment service provider to apply **Strong Customer Authentication**, two of knowledge, possession and inherence, when the payer "initiates an electronic payment transaction," and for remote transactions to use elements that "dynamically link the transaction to a specific amount and a specific payee" ([Directive (EU) 2015/2366, Art. 97](http://publications.europa.eu/resource/celex/32015L2366), 2015). For cards online this is usually done with 3-D Secure (3DS), the issuer's challenge in the checkout flow. The regulatory technical standards in Delegated Regulation (EU) 2018/389 (the SCA RTS) define the exemptions ([Delegated Regulation (EU) 2018/389](http://publications.europa.eu/resource/celex/32018R0389), 2018). Read them with a stays basket in mind:

| Exemption (SCA RTS) | Rule | Fit for stays |
| --- | --- | --- |
| **Low value** (Art. 16) | Up to €30, within cumulative limits of €100 or five transactions since the last SCA | Almost never: a night costs more |
| **Recurring series** (Art. 14) | SCA on the first payment of a series with the same amount and payee; later ones may be exempt | Rare: stays charges are not same-amount series, except some monthly long stays |
| **Secure corporate payments** (Art. 17) | Dedicated processes for payers who are not consumers | Fits the B2B side: the OTA paying with a virtual card, or a corporate travel account |
| **Transaction risk analysis** (Art. 18) | Low-risk remote payments up to an exemption threshold value, if the PSP's fraud rate is at or below a reference rate: **€100 at 0.13%**, **€250 at 0.06%**, **€500 at 0.01%** for remote card payments | Limited: the average Nookaway reservation is above €500, and the 0.01% fraud rate needed at €500 is very hard to hold in travel |

The table leads to the rule I use: **a stays checkout in Europe should expect to authenticate the guest, and should spend that authentication well.** If the guest authenticates once, at checkout, for a payment plan with future charges, every later charge can be a merchant-initiated transaction. If the checkout authenticates only the first payment and forgets to set up the stored credential, each later charge falls back into SCA scope with the guest absent. Stripe's guide adds the liability side: an authenticated payment can shift fraud-chargeback liability to the issuer, but when the merchant requests an exemption and it is accepted, liability "stays with the merchant" ([Stripe SCA guide](https://stripe.com/guides/strong-customer-authentication), n.d.).

Two neighboring rules matter for stays. PSD2 Article 75 allows funds to be blocked for a card payment whose exact amount is not known at consent only if the payer "has given consent to the exact amount of the funds to be blocked," and the block must be released once the amount is known ([Directive (EU) 2015/2366, Art. 75](http://publications.europa.eu/resource/celex/32015L2366), 2015); this governs incidental and deposit holds. And business-to-business card payments sit under a different exemption: Booking.com's Demand API tells partners that pay Booking.com with a virtual card to flag that payment with an SCA exemption value of `virtual` ([Booking.com Developers](https://developers.booking.com/demand/docs/payments/models/partner-collects), n.d.), which is consistent with the Article 17 corporate exemption, although the documentation does not cite the article.

{id: stay-payments--payment-orchestration}
### Payment orchestration

**Payment orchestration** is the layer that turns a booking's payment obligations into PSP calls, in the right order, at the right time, idempotently, and reports the outcome. Airbnb's 2022 description gives the goal: "guests should be charged the right amount at the right time using their selected payment methods; hosts should be paid the right amount at the right time to their desired payout methods" ([Airbnb Engineering, 2022](https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b)). In stays, "the right time" is the hard part. A **virtual card** (virtual credit card, VCC), the single-use card with which a merchant-model OTA pays a hotel, is one of the obligations it executes; it gets its own section below.

{id: stay-payments--architecture-one-payment-plan-per-booking}
## Architecture: One Payment Plan per Booking

The core design choice is to give every booking a **payment plan**: a versioned list of money obligations, each with a type, an amount, a currency, a due date or trigger, an instrument and a state. Checkout creates the plan, modifications and cancellations version it, and the orchestrator executes it. A Pay Later booking has a scheduled charge with a deadline; a Roomstead merchant booking has a guest charge and a virtual card with an activation date; a long stay has monthly charges; a request-to-book listing has an authorization that becomes a capture when the host accepts.

Airbnb reached a similar model from the other direction. Its 2022 post describes an alteration such as "adding another night to a stay" as "a new version in a sequence of plans for that product," with the versions together giving "a complete history of the intended and actual money movement," and a data model built "around the concept of a bill," not a reservation ([Airbnb Engineering, 2022](https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b)). The post is more than four years old; the principle holds.

![Checkout and the reservation send plan versions to a central orchestrator, which uses a vault, a scheduler, PSP connectors and card issuing, and reports to ledger, payouts and the reservation through a payment state feed.](stays-marketplace-architecture/posts/27-stay-payments/assets/images/27-stay-payments/27-payment-orchestration.jpeg)

**Figure 3:** *Payment orchestration for stays. Checkout and the reservation write versions of a payment plan; the orchestrator executes it through the vault, the scheduler, PSP connectors and card issuing; and a payment state feed tells the reservation, the ledger and payouts what actually happened.*

Each component needs a contract. These are the ones I would write down.

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Payment orchestrator** | Accept, version and execute payment plans; call PSPs idempotently; decide retries | Plan state, idempotency keys, retry policy | Compute prices, fees or cancellation penalties itself |
| **Charge scheduler** | Wake obligations when they fall due; survive restarts and duplicates | Due-date index, at-least-once triggers | Decide what to charge: it only asks the orchestrator to run an obligation |
| **Instrument vault** | Store tokens, network tokens, mandates and the scheme transaction reference; report whether an instrument can be charged later | Card-on-file records, consent records, chargeability | Hold raw card numbers outside a PCI DSS-scoped zone |
| **Payment method registry** | Describe each method's flow, eligibility, currencies, refund rules and timing support | Method configuration | Be hard-coded per app or per market |
| **PSP connectors and routing** | Translate to each acquirer and local method; route by method, currency, cost and health | Connector code, routing rules, PSP health | Expose PSP-specific states to callers |
| **Virtual card issuing** | Create, fund, activate, resize and void single-use cards per reservation | Card lifecycle, issuer integration | Change the reservation; it reacts to reservation events |
| **Hold and deposit manager** | Pre-authorizations for deposits and incidentals; release and capture rules | Hold state and expiry | Keep a hold beyond its consented amount or date |
| **Payment state feed** | Publish every state change as an ordered, versioned event | Event schema, ordering per plan | Publish intentions as facts ("charged" before the PSP said so) |

Three interface choices follow from Corvane's March incident.

1. **The plan is computed by its owners and executed by the orchestrator.** The charge date of a Pay Later booking comes from the cancellation policy engine that [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) owns; the amounts come from the price breakdown of [Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration). The orchestrator stores them on the plan and never recomputes them. When support or a self-service flow asks "when will I be charged?", they read the plan, not a second copy of the rule. This is the defense against **Policy Spaghetti**.
2. **The vault answers one question: can this instrument be charged later, without the guest, for up to this amount?** A Pay Later booking is not confirmed until the answer is yes, which requires a stored credential with a scheme reference and recorded consent. Nookaway's iOS defect would have failed this check on the first booking, not in March.
3. **The feed carries facts, in order, per plan.** Ledger, reservation and payouts consume the same events; none of them polls the PSP.

{id: stay-payments--the-deferred-charge-as-a-state-machine}
### The deferred charge as a state machine

A deferred charge has a lifecycle of its own, longer than the checkout and shorter than the stay.

![Deferred charge states: Secured, Scheduled, Attempted, Paid, with Retrying, AwaitingGuest and Lapsed branches, and Canceled from Scheduled; AwaitingGuest and Lapsed are highlighted.](stays-marketplace-architecture/posts/27-stay-payments/assets/images/27-stay-payments/27-deferred-charge-states.jpeg)

**Figure 4:** *The life of a deferred charge. The two states that need product and policy decisions are AwaitingGuest, where the guest must act, and Lapsed, where the reservation is canceled and the nights return to the calendar; both must happen early enough for the host or hotel to resell.*

Four design rules come with it.

- **Classify declines before retrying.** A hard decline (stolen card, closed account) should go straight to AwaitingGuest. A soft decline for insufficient funds can be retried on a schedule. A soft decline that asks for authentication cannot be fixed by a retry at all; only the guest can fix it, so it should go to AwaitingGuest at once with an authentication link. Nookaway's scheduler retried "authentication required" three times before notifying anyone.
- **Keep the deadline in the plan.** The Lapsed transition is driven by the free-cancellation deadline stored on the plan. If the guest changes dates, the reservation sends a new plan version with a new deadline; the scheduler does not compute it.
- **Block the nights until the plan lapses.** The calendar or room inventory stays booked during AwaitingGuest. Releasing nights is a reservation decision, triggered by the Lapsed event, not a payment side effect.
- **Make every step idempotent.** The scheduler fires at least once; the orchestrator turns that into exactly one charge with an idempotency key per obligation and attempt. Airbnb's 2019 Orpheus idempotency library is the published reference ([Airbnb Engineering, 2019](https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb)); its 2026 Skipper workflow engine, used by payments teams for "scheduled financial operations," runs actions at least once and so requires them to be idempotent ([Airbnb Engineering, 2026](https://airbnb.tech/infrastructure/skipper-building-airbnbs-embedded-workflow-engine/)).

{id: stay-payments--setting-up-a-credential-that-can-be-charged-later}
### Setting up a credential that can be charged later

The sequence below shows the interaction that Nookaway's iOS checkout got wrong. The guest authenticates once; the vault stores what later charges will need; the scheduler charges weeks later without the guest.

![At booking the guest authenticates and the vault stores a reference key; weeks later, with the guest absent, the orchestrator charges using the reference and the issuer approves.](stays-marketplace-architecture/posts/27-stay-payments/assets/images/27-stay-payments/27-stored-credential-setup.jpeg)

**Figure 5:** *Setting up a stored credential for a deferred charge. The booking is confirmed only after the vault holds the token, the scheme reference and the guest's consent; the later charge quotes the reference, so the issuer can approve it without a challenge.*

{id: stay-payments--the-payment-state-feed}
### The payment state feed

The Productscape reference model names a "Payment State Feed" in its accommodation-marketplace payments capability (`paym`), a generic model rather than any company's design. In Corvane's design it is a topic of ordered events per payment plan:

| Event | Emitted when | Reservation | Ledger | Payouts | Support |
| --- | --- | --- | --- | --- | --- |
| `plan.versioned` | Checkout, modification or cancellation writes a plan | Shows payment schedule | Records new obligations | Updates expected payable | Explains "what will I pay, when" |
| `instrument.secured` | Vault confirms a chargeable credential | Allows confirmation of deferred plans | — | — | — |
| `charge.succeeded` / `charge.failed` | PSP outcome, with decline class | Paid status; payment-due banner | Cash in transit, receivable | Releases hold on payout eligibility | Shows reason and next step |
| `plan.awaiting_guest` / `plan.lapsed` | Retries exhausted / deadline passed | Notifies guest; cancels on lapse | Reverses unbilled receivable | Cancels expected payable | Contact driver |
| `vcc.issued` / `vcc.activated` / `vcc.charged` | Card lifecycle and issuer settlement | Shows card to property | Payable to property; issuer clearing | — | Hotel queries |
| `hold.placed` / `hold.released` | Deposit or incidental hold | — | Off-balance memo | — | Guest queries |
| `dispute.opened` / `dispute.closed` | Chargeback lifecycle | Flags reservation | Dispute receivable | May hold or claw back | Evidence request |

How the feed becomes journal entries in Fathom, Corvane Payments' double-entry ledger, is the subject of RECONCILED's [Payments-to-Ledger: Draining the Suspense Swamp](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-to-ledger.html) and [Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html). What matters here is that the feed is **the only source** each consumer uses. That is the defense against **Ledgerless Money**: when Marco asks how much booked value is uncollected, the answer is a sum over `plan.versioned` obligations not yet matched by `charge.succeeded`, not a query against the scheduler's tables.

{id: stay-payments--virtual-cards-paying-hotels-through-their-own-terminals}
## Virtual Cards: Paying Hotels Through Their Own Terminals

A **virtual card** is a single-use card number that the marketplace issues per reservation, loads with the amount owed to the property and sends with the reservation; the hotel charges it at its own terminal as if the guest had paid by card. Bank transfer suits chains with finance departments; for an independent hotel the card is easier, because the front desk already knows how to charge one. The documented programs show the parameters: **activation** (when it becomes chargeable), **amount** and **expiry**.

- **Booking.com** pays properties by bank transfer, virtual card or, for Homes properties in the US and Canada only, through Stripe. With a virtual card, the property receives "a new temporary digital card for every booking," which "becomes chargeable on a POS as soon as the reservation becomes non-refundable (if you meet certain criteria)" ([Booking.com for Partners](https://partner.booking.com/en-gb/solutions/payments-bookingcom), n.d., fetched October 2026). Its connectivity API documents **seven activation policies**: on check-out date, when the reservation becomes non-refundable, on check-in date, one day after check-in, long after check-out, on the cancellation date and on the booking date. A property can switch from virtual card to bank transfer, but "the reverse direction (BT to VCC) is currently not supported" ([Booking.com Developers](https://developers.booking.com/connectivity/docs/payments-by-booking-onboarding-api/understanding-payouts), n.d.).
- **Expedia Group** sends a virtual card with each Expedia Collect reservation; its Booking Notification API documentation says the reservation message carries the card ([Expedia Group Developer Hub](https://developers.expediagroup.com/supply/lodging/docs/booking_apis/booking_notification/getting_started/introduction), 2025). Integrator documentation reports that the card can be charged from the check-in day for about six months and that charges before check-in fail ([Lodgify Help Center](https://help.lodgify.com/hc/en-us/articles/360016077759), n.d.). These details come from integrators, not from Expedia, so treat them as reported.
- **Airbnb** lists a virtual card among host payout methods for eligible hosts; the card "must be charged within a set window around check-in and expires after 180 days" ([Airbnb Payments Terms, 2026](https://www.airbnb.com/help/article/2909)).

No primary source found for this book names the banks or issuing processors behind these programs; this chapter does not name them.

A virtual card program is therefore an **issuing system attached to the reservation lifecycle**: created at confirmation, chargeable on its activation date, resized on modification, and voided or reduced to a cancellation fee on cancellation.

![Confirmed, modified and canceled reservation events create, resize or void a virtual card, which the hotel charges; settlement is reconciled and mismatches become exceptions.](stays-marketplace-architecture/posts/27-stay-payments/assets/images/27-stay-payments/27-virtual-card-follows-reservation.jpeg)

**Figure 6:** *A virtual card follows the reservation. Every change to the reservation must reach the card before the hotel charges it; issuer settlement is then matched back to the reservation, and mismatches become operations work.*

At Corvane, Roomstead's "Pay with Roomstead" merchant bookings pay hotels mostly this way: Corvane Payments creates a card through its partner issuing bank when the reservation is confirmed. For a flexible rate the card activates on the check-in date; for a non-refundable rate it activates when the reservation becomes non-refundable, which is at booking. Take a three-night merchant stay at **Hotel Miradouro** in Lisbon, 14–17 June 2027, at **€150** a night: the guest pays Roomstead **€450**; with Miradouro's 15% commission deducted ([Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models)), the hotel's net is **€382.50**, and that is the amount loaded on the card. Duarte Silva's front desk charges it at check-out. If the guest had added a night on 1 June, the card would have had to grow to €510 before check-out; if the reservation had been canceled inside the hotel's penalty window, the card would have become a one-night fee card.

That last case is where Corvane's virtual cards have already cost money. In the first quarter of 2027 Corvane Payments found **€1.8 million** unreconciled between issuing statements and Roomstead merchant reservations, mostly cards that hotels charged for reservations later canceled or modified. A typical case was a non-refundable card activated at booking, charged by the hotel at once, and then canceled with a waived fee, or charged at the original amount after a modification shortened the stay. The reconciliation is the subject of [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation); the design lesson belongs here. **A card that activates at booking can be charged before any change reaches it.** Activation policy is a risk setting, and the safest default is the check-in date, with earlier activation only where the commercial terms require it and the card amount can still be adjusted.

{id: stay-payments--deposits-holds-and-post-stay-charges}
## Deposits, Holds and Post-Stay Charges

A hotel commonly takes a card pre-authorization for incidentals at check-in and releases it at check-out; under PSD2 Article 75 the guest must consent to the exact amount blocked. In the agency model this is the hotel's business: Booking.com's terms say it "won't be involved in any financial settlement related to damage deposits," although a property can submit a damage payment request through the platform within 14 days, which Booking.com then arranges to charge ([Booking.com Terms](https://www.booking.com/content/terms.html), updated 25 August 2025).

A hosted-stays platform has no front desk, and two designs are documented. Vrbo inventory distributed through Expedia's Rapid API supports refundable damage deposits and payment schedules as opt-in options; Expedia says enabling payment schedules makes "+15-25% more" properties available and damage deposits "+2% more, often higher-end" ([Expedia Group Developer Hub](https://developers.expediagroup.com/rapid/lodging/vacation-rentals/about-vacation-rentals-api), n.d., fetched October 2026). Airbnb's current terms instead provide for damage reports whose amounts Airbnb Payments "may charge [to] the Payment Method" of the booking, backed by its host protection program ([Airbnb Terms of Service](https://www.airbnb.com/help/article/2908), 2026).

| Design | Guest experience | Failure mode | Platform cost |
| --- | --- | --- | --- |
| **Pre-authorization hold** | Funds blocked before or at check-in | Authorizations expire after days, so long stays need a new one; blocked funds annoy guests | Hold management, release discipline |
| **Collected deposit** | Paid and refunded later | Refund delays; foreign-exchange difference on the refund | Funds held, refund operations |
| **Post-stay merchant-initiated charge** | Nothing blocked | Charge can fail or be disputed; needs the stored credential and evidence | Protection program absorbs what cannot be collected |

The third design depends on the same stored credential as Pay Later. When Nookaway Cover reimbursed Ivan Horvat **€3,450** after the August 2027 party at his Dubrovnik villa, it recovered **€900** from the guest after the stay ([Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) tells the story). The payment plan should carry the possibility of post-stay charges from checkout, with the guest's consent recorded in the vault, so that the protection team is not inventing a payment flow in the middle of a dispute.

{id: stay-payments--methods-local-payments-and-routing}
## Methods, Local Payments and Routing

The card is not the dominant payment method everywhere. Booking.com lists cards, PayPal, Apple Pay, Google Pay, Alipay, WeChat, iDEAL, Venmo and buy-now-pay-later providers among the methods available through Payments by Booking.com and says "up to 25%" of those reservations are paid with alternative methods ([Booking.com for Partners](https://partner.booking.com/en-gb/solutions/payments-bookingcom), n.d.), a marketing figure. Booking Holdings' FY2025 annual report names the cost: "additional payment processing costs (which are typically higher for foreign currency transactions)" and fraud costs ([Booking Holdings 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm)).

The most detailed public account of adding methods is Airbnb's 2026 "Pay as a Local" post: more than 20 local payment methods, including Pix, UPI, BLIK and Cartes Bancaires, in about 14 months, on a processor-agnostic framework called **Multi-Step Transactions** with redirect, asynchronous and direct flow archetypes, a connector model for PSPs, and a YAML payment-method configuration that makes adding a method "largely declarative" ([Airbnb Engineering, 2026](https://airbnb.tech/payments/pay-as-a-local/)).

For stays, **a payment method is defined by its timing support as much as by its flow.** A card can be stored and charged later; a bank redirect or a QR payment usually cannot. Pay Later must be limited to methods that support merchant-initiated charges, and the method registry must say which those are. Nookaway's 2027 mix shows the effect (illustrative figures): cards **71%** of guest payments, card-based wallets and PayPal **17%**, local methods such as MB WAY in Portugal, Bizum in Spain and Pix in Brazil **12%**. Pay Later was offered on the first two groups only, one reason its uptake was low in Brazil.

**Routing** decides which acquirer processes a payment. Corvane Payments uses Adyen as its primary acquirer. A second acquirer adds resilience, local acquiring where domestic processing raises approval rates, and price competition; it also adds a connector, a settlement file to reconcile and a token problem. A card stored as one acquirer's token cannot be charged through another unless the platform holds network tokens or runs its own vault. **For deferred charges, routing flexibility exists only if stored credentials are portable.** RECONCILED's [Payments for Finance Architects: Eleven Reasons the Numbers Disagree](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-fundamentals.html) covers tokens and multi-provider orchestration in general.

{id: stay-payments--currencies-presentment-settlement-and-payout}
## Currencies: Presentment, Settlement and Payout

A stays booking can involve three currencies: the **listing or rate currency** in which the host or hotel priced the night, the **presentment currency** that the guest sees and pays, and the **payout currency** that the supplier receives. Each foreign-exchange (FX) conversion has a rate, a time and an owner.

Airbnb lets guests pay "in the currency of their choice," which "may not match the currency in which the host elects to be paid," so it bears "the currency risk of both the guest payment as well as the host payment due to timing differences" and hedges it ([Airbnb 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm)). Booking.com's terms express its conversion fee "as a percentage over European Central Bank rates" ([Booking.com Terms](https://www.booking.com/content/terms.html), 2025). EU Regulation 2019/518 requires anyone offering conversion at the point of sale, including "on-screen in the case of online purchases," to disclose the charge before payment as a mark-up over the latest European Central Bank (ECB) reference rate ([Regulation (EU) 2019/518](http://publications.europa.eu/resource/celex/32019R0518), 2019); this is the rule for **dynamic currency conversion** (DCC), conversion offered at payment time rather than built into the displayed price.

A guest from Manchester books Carmen Ruiz's apartment in Seville for three October nights at her usual **€110** with the **€60** cleaning fee: a **€390** subtotal plus Nookaway's 12% guest fee of **€46.80**, **€436.80** before taxes ([The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)). Nookaway shows pounds at its own rate plus a disclosed margin; Carmen is paid in euros, €390 less the 4% host fee, **€374.40**.

- With **pay now**, Corvane collects pounds at booking and owes euros 48 hours after check-in: one open leg.
- With **Pay Later**, Corvane is owed a fixed pound amount and owes a fixed euro amount, and both legs stay open until the charge: the "unbilled amounts" exposure in Airbnb's filing.
- If the guest's **bank converts**, because Nookaway charged in euros, the statement differs from the checkout and the guest calls support: **Price Drift** in the payment step.

The rule: store each conversion on the plan, with currencies, rate, rate source, timestamp and margin, so the ledger can book FX results and support can explain the statement.

{id: stay-payments--chargebacks-liability-that-outlives-the-stay}
## Chargebacks: Liability That Outlives the Stay

A **chargeback** is a reversal of a card payment that the cardholder's issuer initiates through the card scheme, after a dispute. The merchant of record bears it. Airbnb states that "as the merchant of record, we bear all payment processing costs for our bookings, including those from chargebacks due to both fraud and non-fraud activities," and reported chargeback expense of **$67 million** for 2025, within merchant fees and chargebacks of **$1,666 million** ([Airbnb 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm)). Booking Holdings records an allowance for chargebacks because it "may be held liable for fraudulent transactions on our platforms" ([Booking Holdings 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm)); Expedia records a reserve "at the time of the transaction based on historical experience" ([Expedia Group 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm)).

Stays disputes are harder than retail ones for two reasons. The service is delivered weeks after payment, and card schemes commonly let disputes about future services run from the expected service date, so a hosted-stays platform that pays the host soon after check-in often carries the dispute after the money has left, recovering it, if at all, from future payouts ([Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement)). And the evidence that wins lives outside payments: the policy shown at checkout, guest–host messages ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging)), check-in confirmation and the authentication result. The dispute service should assemble it from those records and the state feed, not from agents' screenshots. Fraud screening before the charge belongs to [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud).

{id: stay-payments--in-practice-what-the-public-record-shows-and-corvane-s-redesign}
## In Practice: What the Public Record Shows, and Corvane's Redesign

{id: stay-payments--the-public-record}
### The public record

Most of the documented evidence appears in the sections above. Three further points complete the picture.

- **Airbnb's evolution shows the principles survive rewrites.** Its payments posts run from an append-only gateway and a double-entry financial pipeline ([2016](https://medium.com/airbnb-engineering/scaling-airbnbs-payment-platform-43ebfc99b324)), through three-way reconciliation across "a handful of gateways and dozens of processors" ([2018](https://medium.com/airbnb-engineering/measuring-transactional-integrity-in-airbnbs-distributed-payment-ecosystem-a670d6926d22)), to orchestration as directed acyclic graphs of "retryable idempotent steps" with "five 9s (99.999%) of consistency" ([2022](https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b)) and named subdomains for pay-in, payout, processing, ledger, and settlement and reconciliation ([2026](https://airbnb.tech/payments/pay-as-a-local/)). The older posts describe systems that were later replaced; plans, idempotency and append-only events carried over.
- **SCA can change who the merchant is.** Expedia's FY2025 annual report describes Expedia Traveler Preference, which lets a guest choose per booking between paying Expedia now (Expedia Collect) and paying at the hotel (Hotel Collect) ([Expedia Group 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm)); in its Rapid API's property-collect flow, Rapid becomes merchant of record "only when" SCA applies ([Expedia Group Developer Hub](https://developers.expediagroup.com/rapid/lodging/booking/property-collect), n.d.). The plan must carry who the merchant is, per booking.
- **Payment timing can be a variant of one workflow.** Agoda's November 2025 post on its multi-product booking engine describes a graph of steps per booking, itinerary-level steps that "pre-authorise and settle card" once for a cart, and "Book with ZeroPay," which reuses the hotel graph with the payment step skipped by a flag ([Agoda Engineering, 2025](https://medium.com/agoda-engineering/how-agodas-multi-product-booking-engine-powers-seamless-travel-bookings-61fc6e746821)).

> **INFERENCE, NOT DOCUMENTED:** None of these companies has described how its deferred-charge scheduler, its credential vault or its virtual card issuing integrates with its reservation system. The component boundaries in this chapter are a reference architecture derived from the documented behavior and from payments practice, not a description of any of their systems.

{id: stay-payments--corvane-s-redesign-payment-plans-v1}
### Corvane's redesign: Payment Plans v1

Mariana's review produced a design that Leila's team built between April and September 2027, inside the One Stay program's shared payments scope.

1. **The payment plan became the contract.** Checkout in both Burrow (Nookaway) and the Roomstead checkout services now sends Corvane Payments a plan rather than a charge request. The plan carries the obligations, the policy deadline from the cancellation policy engine and the currency data. Plans are versioned; reservation changes send a new version.
2. **Chargeability became a confirmation gate.** A plan with any deferred obligation is accepted only when the vault reports a stored credential with a scheme reference and recorded consent, for an amount at least the plan total. In the first month the gate rejected **0.6%** of Pay Later attempts, mostly from third-party wallets that did not return a reference, and those guests were offered pay now instead.
3. **Decline classes drove the scheduler.** Authentication-required declines skip retries and go straight to the guest; insufficient-funds declines retry on days 0, 2 and 4; hard declines notify at once. The scheduled-charge decline rate became a monitored metric per app version, per issuer country and per method, with an alert at twice its four-week baseline.
4. **Pay Later charges moved earlier for peak dates.** For check-ins in Corvane's peak calendar (Semana Santa, Feria de Abril, July and August), the first charge now runs **14 days** before the free-cancellation deadline instead of 10, giving hosts more time to resell after a lapse.
5. **Roomstead reuses the same plan for merchant bookings.** "Pay with Roomstead" bookings use one guest charge and one virtual card obligation per plan. Activation policy moved to the plan, defaulting to the check-in date, so a change to the reservation reaches the card before the hotel can charge it. The 2028 Roomstead pay-later launch will reuse the deferred-charge state machine unchanged.

The numbers that mattered to the board were simple. In March 2027 the first-attempt decline rate of scheduled Pay Later charges was 14.2%; for the August 2027 peak, with the gate and the new decline handling in place, it was **3.6%**. Lapsed Pay Later bookings fell from 2.4% of Pay Later reservations to 1.5%.

{id: stay-payments--trade-offs}
## Trade-offs

The largest choice is how much of orchestration to build.

| Option | What you build | What you get | What you give up | When it is right |
| --- | --- | --- | --- | --- |
| **PSP-native marketplace product** (for example [Adyen for Platforms](https://docs.adyen.com/marketplaces/) or [Stripe Connect](https://docs.stripe.com/connect/charges)) | Checkout integration, plan logic on top | Split payments, holds, onboarding and payouts from one provider; the provider may carry licensing | Routing flexibility; tokens tied to one provider; the provider's model of time | A single-market or early-stage stays marketplace |
| **Third-party orchestration layer** over several PSPs | Plans and scheduling; connectors bought | Multi-acquirer routing, portable vault | Another vendor in the critical path; its state model is not yours | Mid-sized platforms adding local acquiring |
| **Own orchestration and vault**, PSPs as processors | All of it | Plans, timing, routing and data under your control | A payments engineering team and, often, a license | Platforms with their own payment institution, as Corvane has |

Stripe's documentation makes the marketplace choice concrete: destination charges, "best suited for marketplaces, such as a home rental marketplace," create the charge on the platform and transfer part to the connected account, while separate charges and transfers decouple the two for "charges created before the destination account is known" ([Stripe Docs](https://docs.stripe.com/connect/charges), n.d.). For hosted stays, where the host is paid after check-in and one booking may pay a host and a co-host, decoupling charge and transfer is the natural fit; RECONCILED's [Stripe: Every Movement Is a Balance Transaction](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/stripe.html) and [Adyen: One Platform from Checkout to Settlement](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/adyen.html) chapters describe both providers' models in depth.

The second choice is when to collect.

| Timing | Conversion | Collection risk | Cash and FX | Operational load |
| --- | --- | --- | --- | --- |
| Pay now | Lowest of the online options for long lead times | Lowest | Float from booking to payout; refund liability | Refunds on cancellation |
| Pay later before the free-cancellation deadline | Higher, as the published adoption figures suggest | Charges fail with guest absent | Unbilled receivable and two open FX legs | Scheduler, dunning, lapse handling |
| Deposit now, balance later | Between the two | Balance can fail; deposit partly covers it | Partial float | Two obligations per booking |
| Pay at property | Highest for hotels that accept it | Borne by the property | None for the platform | Commission invoicing ([Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models)) |

None of these is wrong. The mistake is to offer them without a plan model that can say, for each booking, which one applies and what is still owed.

{id: stay-payments--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (OTA-style) | Hosted-stays marketplace |
| --- | --- | --- |
| **Who collects** | Mixed: the property (agency) or the platform (merchant), sometimes chosen per booking | Always the platform, as collection agent for the host |
| **Payment timings** | Pay at property, pay now, pay later online; card guarantees forwarded to the property | Pay now, pay later, pay in parts, long-stay installments; no pay-at-property path |
| **Paying the supply side** | Virtual card per reservation or periodic bank transfer to a business, often weeks after the stay | Payout to an individual's account shortly after check-in ([Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement)) |
| **Deferred charges** | No-show and late-cancellation fees; in the agency model the hotel runs them and carries the SCA problem | Pay-later collections, balances, post-stay damage charges; the platform runs all of them |
| **Deposits and incidentals** | Hotel pre-authorization at the desk | Platform deposit, schedule or post-stay claim backed by a protection program |
| **Currencies** | Hotel contracts and is paid in its currency; the card is loaded in it | Host may choose a payout currency different from the listing currency: a second conversion |
| **Typical failure** | Virtual card charged before a change reaches it; card guarantee data leaking through channel managers | Deferred charge fails with the guest absent; dispute arrives after the payout |
| **Regulation that bites** | SCA exemptions for B2B virtual cards; merchant-of-record status changing with SCA | SCA on every guest payment plan; payment licensing because the platform holds funds ([Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation)) |

The rails already cross over: Booking.com pays US and Canadian Homes properties through Stripe on the check-in day, and Airbnb pays some hosts by virtual card. Corvane will meet the overlap when Nookaway pilots boutique hotels in 2028.

My judgement: **share the guest side and the plumbing; keep the supply-side rails separate.** The plan contract, orchestrator, vault, method registry, PSP connectors, SCA handling, dispute service and state feed should be one platform, because a card, a scheme reference and a chargeback work the same way whatever was booked. Virtual card issuing for hotels and payouts to individuals have different counterparties, risks and operations, and should stay separate services on it. Payment Plans v1 drew that line: the plan, not the brand, is the unit Corvane Payments serves.

{id: stay-payments--failure-modes}
## Failure Modes

- **The uncollectable promise.** A deferred charge is accepted without a chargeable credential, and the defect surfaces only on the charge date, when the guest is absent and the deadline is near. Corvane's Semana Santa week is the example.
- **Retrying what only the guest can fix.** Authentication-required declines retried on a timer burn days of the grace period. Classify declines before retrying.
- **The second calendar of deadlines.** The scheduler computes charge dates from its own copy of the cancellation rules; after a policy change, guests are charged on dates that support cannot explain. **Policy Spaghetti** in money form.
- **Cards ahead of the reservation.** Virtual cards activated at booking are charged before a cancellation or modification reaches them, and the difference appears months later in reconciliation, as in Corvane's €1.8 million gap.
- **Facts from dashboards.** The ledger, payouts or support read payment status from the PSP's portal or poll it separately, and each sees a different state. Without one payment state feed, **Ledgerless Money** follows.
- **Retries without keys.** A client or scheduler retries a charge without reusing its idempotency key and charges twice. Roomstead's **212** duplicate bookings on 14 January 2027, **198** of them with duplicate charges, came from a mobile checkout retry; [Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration) owns that story, and the same discipline applies to every scheduled charge.
- **Tokens locked to one acquirer.** A second acquirer is added for resilience, but stored credentials cannot be charged through it, so every future charge still depends on the first one.
- **Peaks that arrive as batches.** Scheduled charges cluster before holidays, so one PSP incident or issuer rule hits thousands of bookings at once; the scheduler needs rate control and per-issuer monitoring ([Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability)).

{id: stay-payments--the-chief-architect-s-view}
## The Chief Architect's View

The decisions that matter at group scale are few, and most are not about PSPs.

- **Define the payment plan as a group contract.** It is the money half of the shared reservation contract that One Stay introduced: same obligation types, same versioning, same events for both marketplaces. Its owner is the payments platform; its inputs are owned by pricing, cancellation policy and tax.
- **Decide who carries collection risk for each timing.** Pay later shifts risk from the guest's bank to the marketplace. The CFO, the marketplace general managers and the payments head should agree, in writing, who funds a lapse that is the platform's fault (as in March 2027) and who funds one that is the guest's choice.
- **Set measurable payment health objectives.** First-attempt approval rate of scheduled charges, lapse rate, authentication challenge rate, dispute rate, uncollected booked value, and the age of unreconciled virtual card settlements. Watch them per market, method, app version and issuer country.
- **Own the credentials.** Portability of stored credentials, through network tokens or the group's own vault, is what makes acquirer routing, resilience and price negotiation possible for the money that has not yet been collected.
- **Treat activation and timing as risk configuration.** Virtual card activation policies, pay-later lead times and retry schedules change exposure. Changes should be reviewed like credit policy, with an owner and a rollback.
- **Watch regulation as an input to the plan.** The proposed third Payment Services Directive and Payment Services Regulation (still in the EU legislative process at the time of writing), consumer-credit rules for pay-later products and price-transparency rules all change what a plan may contain.

Who decides: the Group Chief Architect owns the plan contract and the boundaries; the head of payments owns the orchestration platform and its objectives; the CFO owns risk appetite for deferred collection; product leaders of each marketplace own which timings they offer, within that appetite.

{id: stay-payments--questions-to-ask}
## Questions to Ask

1. For a booking made today, can we list every future money movement it implies, with dates, amounts and currencies, from one place?
2. Before we confirm a booking with a deferred charge, what do we verify about the stored credential, and what happens if the check fails?
3. Where is the charge date of a pay-later booking computed, and does support read the same value the scheduler uses?
4. How do we classify declines on scheduled charges, and which classes go straight to the guest?
5. What is our first-attempt approval rate on scheduled charges this month, by app version and issuer country, and who is alerted when it moves?
6. When a reservation is modified or canceled, how long until the virtual card reflects it, and what stops a hotel from charging the old amount?
7. Can our stored credentials be charged through a second acquirer tomorrow?
8. Where does each currency conversion happen, at what rate and margin, and can support explain a card statement in the guest's currency?
9. Which events do the ledger, payouts and support consume, and do any of them read payment status from anywhere else?
10. When a chargeback arrives after the host has been paid, who bears it, and how is the evidence assembled?

{id: stay-payments--from-collecting-to-paying-out}
## From Collecting to Paying Out

Taking the guest's money is half of the job. The other half is getting the right share of it to the hotel, the host and the co-host, at the right time, in the right currency, net of commission, holds and disputes, with a ledger that can prove it. That is the subject of [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement).

{id: stay-payments--sources-and-evidence}
## Sources and Evidence

{id: stay-payments--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Booking Holdings Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm) — Booking Holdings via SEC EDGAR, 2026. Merchant and agency revenue, payment processing and FX costs, chargeback allowance.
- [Expedia Group Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm) — Expedia Group via SEC EDGAR, 2026. Expedia Traveler Preference, merchant model, chargeback reserve.
- [Airbnb, Inc. Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm) — Airbnb via SEC EDGAR, 2026. Merchant of record, chargeback expense, currency risk, unbilled amounts under pay-later programs.
- [Airbnb investor relations: Q2 2026 shareholder letter](https://investors.airbnb.com/) — Airbnb, 2026. Effect of Reserve Now, Pay Later on unearned fees.
- [Reserve Now, Pay Later is now available worldwide](https://news.airbnb.com/reserve-now-pay-later-is-now-available-worldwide/) — Airbnb Newsroom, 2026. Worldwide launch on 17 February 2026; eligibility; over 70% adoption.
- [Introducing 'Reserve Now, Pay Later', giving guests greater flexibility](https://news.airbnb.com/introducing-reserve-now-pay-later-giving-guests-greater-flexibility/) — Airbnb Newsroom, 2026. Payment due before free cancellation ends so hosts can rebook.
- [Payments Terms of Service](https://www.airbnb.com/help/article/2909) — Airbnb, 2026. Automatic charge, 72 hours to pay after a failed charge, virtual card payouts.
- [Terms of Service](https://www.airbnb.com/help/article/2908) — Airbnb, 2026. Damage reports charged to the booking's payment method.
- [Scaling Airbnb's Payment Platform](https://medium.com/airbnb-engineering/scaling-airbnbs-payment-platform-43ebfc99b324) — Airbnb Engineering, 2016. Billing items, payments gateway, double-entry pipeline, Boleto asynchronous pattern; describes a replaced system.
- [Measuring Transactional Integrity in Airbnb's Distributed Payment Ecosystem](https://medium.com/airbnb-engineering/measuring-transactional-integrity-in-airbnbs-distributed-payment-ecosystem-a670d6926d22) — Airbnb Engineering, 2018. Multiple gateways and processors; three-way reconciliation.
- [Avoiding Double Payments in a Distributed Payments System](https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb) — Airbnb Engineering, 2019. Orpheus idempotency library.
- [Rebuilding Payment Orchestration at Airbnb](https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b) — Airbnb Engineering, 2022. Orchestration goal, idempotent DAG steps, versioned plans, bill-centered model.
- [Pay as a Local](https://airbnb.tech/payments/pay-as-a-local/) — Airbnb Engineering, 2026. Payment subdomains, Multi-Step Transactions, config-driven local methods.
- [Skipper: Building Airbnb's embedded workflow engine](https://airbnb.tech/infrastructure/skipper-building-airbnbs-embedded-workflow-engine/) — Airbnb Engineering, 2026. Durable workflows for scheduled financial operations; at-least-once actions.
- [Payments by Booking.com](https://partner.booking.com/en-gb/solutions/payments-bookingcom) — Booking.com for Partners, n.d. (fetched 2026). Methods, virtual cards, payout rails, "up to" claims.
- [Understanding payouts (Payments by Booking onboarding API)](https://developers.booking.com/connectivity/docs/payments-by-booking-onboarding-api/understanding-payouts) — Booking.com Developers, n.d. Seven virtual card activation policies; switching rules.
- [Demand API: Partner collects payment](https://developers.booking.com/demand/docs/payments/models/partner-collects) — Booking.com Developers, n.d. Pay-later funding rule; `virtual` SCA exemption flag.
- [Booking.com Terms of Service](https://www.booking.com/content/terms.html) — Booking.com, 2025. Damage deposits, damage payment requests, currency conversion over ECB rates.
- [Property collect (Rapid)](https://developers.expediagroup.com/rapid/lodging/booking/property-collect) — Expedia Group Developer Hub, n.d. Merchant of record when SCA applies; billable currency.
- [About the vacation rentals API (Rapid)](https://developers.expediagroup.com/rapid/lodging/vacation-rentals/about-vacation-rentals-api) — Expedia Group Developer Hub, n.d. Payment schedules and damage deposits as opt-in options.
- [How Agoda's Multi-Product Booking Engine Powers Seamless Travel Bookings](https://medium.com/agoda-engineering/how-agodas-multi-product-booking-engine-powers-seamless-travel-bookings-61fc6e746821) — Agoda Engineering, 2025. Itinerary-level card steps; ZeroPay flag.

{id: stay-payments--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Directive (EU) 2015/2366 (PSD2)](http://publications.europa.eu/resource/celex/32015L2366) — Official Journal via the EU Publications Office, 2015. Article 97 (SCA) and Article 75 (blocking funds for unknown amounts).
- [Delegated Regulation (EU) 2018/389 (SCA RTS)](http://publications.europa.eu/resource/celex/32018R0389) — Official Journal via the EU Publications Office, 2018. Articles 14, 16, 17 and 18 and the Annex reference fraud rates.
- [Regulation (EU) 2019/518](http://publications.europa.eu/resource/celex/32019R0518) — Official Journal via the EU Publications Office, 2019. Disclosure of currency conversion charges at the point of sale.
- [Strong Customer Authentication guide](https://stripe.com/guides/strong-customer-authentication) — Stripe, n.d. Merchant-initiated transactions and liability under exemptions.
- [Understand how charges work in a Connect integration](https://docs.stripe.com/connect/charges) — Stripe Docs, n.d. Destination charges versus separate charges and transfers.
- [Marketplaces](https://docs.adyen.com/marketplaces/) — Adyen Docs, n.d. Split payments, holds and payout timing for platforms.

{id: stay-payments--research-and-practitioner-sources}
### Research and practitioner sources

- [Charge Expedia reservations in Lodgify](https://help.lodgify.com/hc/en-us/articles/360016077759) — Lodgify Help Center, n.d. Reported Expedia virtual card charging window (integrator documentation).
- RECONCILED: [Payments for Finance Architects: Eleven Reasons the Numbers Disagree](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-fundamentals.html), [Payments-to-Ledger: Draining the Suspense Swamp](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-to-ledger.html), [Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html), [Adyen: One Platform from Checkout to Settlement](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/adyen.html), [Stripe: Every Movement Is a Balance Transaction](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/stripe.html) — the finance companion book, for card payments, ledgers and provider models in depth.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
