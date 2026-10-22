# Research brief: Payments, finance and tax for stays marketplaces

Prepared 21 October 2026 for chapter writers of *BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces*. The brief is vendor-neutral. Booking Holdings, Expedia Group and Airbnb get the most space because their 10-K filings, partner documentation and payment terms are public and dated, not because the book endorses their choices. EU law is quoted from the official texts served by the EU Publications Office.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page or document was fetched in this session (21 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date (for a 10-K, the filing date; for a statute, the date in the Official Journal), not the fetch date. Where a page shows no date, the tag says "undated, fetched 2026-10".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, vendor or integrator documentation, trade press), not from the company's own primary material.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about a proprietary system a company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Payment architecture and payment regulation both move fast. Airbnb's best engineering material on payments is from 2016, 2018, 2019 and 2022, plus one 2026 post. The 2016 post describes a Rails-era system that the 2022 post says was replaced by a service-oriented one; describe each in the past tense unless a newer source confirms it. The 10-K filings used here are for fiscal year 2025 (filed February 2026), so they are current.

**Research limitation.** The session's shared web-search quota ran out about two thirds of the way through. After that the research relied on direct fetches of known URLs (SEC EDGAR, EU Publications Office, company terms and developer docs). As a result:

- **Expedia's virtual card (EVC) and the payment pages of Expedia Partner Central** could not be fetched: the developer-docs URL redirects to a portal that renders no text. EVC claims rest on integrator documentation (WIDELY REPORTED).
- **Booking.com's payments licence** (which Booking.com entity holds which EU payment authorisation, if any) is **not verified**. Neither the FY2025 10-K nor the traveller terms name a licence.
- **US hotel-occupancy-tax case law** (the litigation wave against OTAs, roughly 2005–2017) could not be fetched from court sources. The brief relies on the OTAs' own 10-K language and flags case names as unverified.
- **Paris's taxe de séjour rates** come from a vendor guide, not from a Ville de Paris deliberation.
- **Medium-hosted Airbnb posts** return HTTP 403; four of them were read through Internet Archive snapshots of the original Medium pages (the content is Airbnb's own, so they are tagged VERIFIED with the original URL and the post date).
- **Issuing partners behind OTA virtual cards** (which bank or issuing processor funds Booking.com's or Expedia's VCCs) were not found in any primary source.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: fee structures, product availability (pay-later options by country), tax rates, thresholds and transposition dates.

---

## PART 1: Who takes the money — business models and how they are booked

### 1.1 Merchant model versus agency model

The single most important payments decision in an OTA-style marketplace is **who is the merchant of record for the guest's payment**. Every downstream system (payment acceptance, supplier settlement, VAT, fraud liability, refunds, revenue recognition) follows from it.

| Dimension | Agency model ("pay at property", "Hotel Collect") | Merchant model ("prepaid", "Expedia Collect", "Payments by Booking.com") | Hosted-stays platform (Airbnb) |
| --- | --- | --- | --- |
| Who charges the guest | The property, usually at the stay | The platform (or its payment affiliate), usually at booking | The platform's payment entity, at booking or on a later schedule |
| Who holds the guest's money before the stay | Nobody (card may be held as a guarantee) | The platform | The platform's payment entity, as collection agent for the host |
| How the platform earns | Commission invoiced to the property after the stay | Commission or margin kept from the guest payment before paying the property | Service fee kept from the guest payment before paying the host |
| How the property/host is paid | It already has the money; pays commission to the OTA | Bank transfer or a virtual card per booking | Payout to bank, PayPal, card, etc. |
| Who carries fraud and chargeback cost | The property | The platform | The platform |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis; the claims below support each row.

- **Booking Holdings' definitions.** "Merchant revenues are derived from transactions where we facilitate payments from travelers for the services provided, generally at the time of booking." Merchant revenues include "travel reservation commissions and transaction net revenues, which is the amount charged to travelers ... less the amount owed to travel service providers; revenues from facilitation of payments such as credit card processing rebates and customer processing fees; and ancillary fees." "Agency revenues are derived from travel-related transactions where we do not facilitate payments from travelers for the services provided, and consist almost entirely of travel reservation commissions from Booking.com's accommodation reservations." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18]
- **Expedia Group's definitions.** "Under the merchant model, we facilitate the booking of hotel rooms, alternative accommodations, airline seats, car rentals and destination services from our travel suppliers and we are the merchant of record for such bookings." Expedia has "no control over the rooms and do[es] not bear inventory risk." Under the agency model Expedia "act[s] as the agent in the transaction, passing reservations booked by the traveler to the relevant travel provider" and receives "commissions or ticketing fees." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm, published 2026-02-13]
- **Expedia lets the guest choose per booking.** The Expedia Traveler Preference (ETP) programme offers guests at participating hotels "the choice of whether to pay Expedia Group in advance under our merchant model (Expedia Collect) or pay at the hotel at the time of the stay under the agency model (Hotel Collect)." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm, published 2026-02-13]
- **Booking.com allows a mixed model per property.** A property can let Booking.com facilitate some guest payments and collect others itself. Under "full facilitation" Booking.com deducts commission and payment service fees from each payout; under the "mixed model" it sends "a monthly invoice that includes the commission and service fees for all reservations of that month." [VERIFIED: https://partner.booking.com/en-gb/solutions/payments-bookingcom, undated, fetched 2026-10]

**Architectural consequence.** [ASSUMPTION/JUDGEMENT] Because one property can have both merchant and agency bookings in the same month, an OTA's finance platform must run two settlement directions side by side: *payables* to properties (merchant bookings, netted against commission) and *receivables* from properties (agency commission invoices). The booking record has to carry the payment model as a first-class attribute set at booking time and immutable afterwards, because it decides which ledger flow, which tax treatment and which invoice the booking produces.

> **OTA vs hosted stays.** OTAs run both models and are moving towards merchant. Airbnb has only ever had one model: the platform always collects. Airbnb's ToS describe it as "not acting as an agent for any Member except for where Airbnb Payments acts as a collection agent." [VERIFIED: https://www.airbnb.com/help/article/2908, published 2026-02-05] Hosted-stays platforms therefore never need an agency-commission invoicing flow, but they always need a payout system to individuals.

### 1.2 The shift from agency to merchant at Booking.com

- Booking Holdings' FY2025 merchant revenues were **$17,755m** (2024: $14,142m, +25.5%) and agency revenues **$7,968m** (2024: $8,524m, −6.5%). The filing attributes the movement to "the ongoing shift from agency to merchant revenues at Booking.com." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18]
- Merchant gross bookings were **$130,025m** and agency gross bookings **$56,082m** in 2025 (total $186,107m). Three years earlier, in 2023, agency revenue ($9,414m) was still close to merchant revenue ($10,936m). [VERIFIED: same filing]
- Booking Holdings states the cost side of that shift: "processing transactions on a merchant basis allows us to offer a variety of payment methods and flexible transaction terms, [but] we incur additional payment processing costs (which are typically higher for foreign currency transactions) and other costs related to these transactions, such as costs related to managing and detecting fraudulent payments." [VERIFIED: same filing]
- Expedia's FY2025 revenue mix was **70% merchant, 22% agency, 8% advertising, media and other**, on total revenue of $14.7bn. [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm, published 2026-02-13]

**Why OTAs move to merchant.** [ASSUMPTION/JUDGEMENT] The merchant model lets the OTA offer local payment methods, instalments and buy-now-pay-later; cut no-shows; earn payment-related revenue (FX, card rebates); and hold guest float. Booking.com's partner page claims partners on Payments by Booking.com see "up to 40% fewer cancellations and up to 80% fewer no-shows" and that "up to 25% of reservations made through Payments by Booking.com are paid through alternative payment methods" [VERIFIED: https://partner.booking.com/en-gb/solutions/payments-bookingcom, undated, fetched 2026-10]. These are marketing figures ("up to") and should be quoted as such.

### 1.3 Revenue recognition: gross versus net, and when

- **All three companies present revenue net.** Booking Holdings: its contracts with travel service providers "give them the ability to market their reservation availability without transferring to the Company the responsibility to deliver the travel services. Therefore, the Company's revenues are presented on a net basis." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18]
- Expedia records merchant hotel payments "in deferred merchant bookings until the stayed night occurs, at which point we recognize the revenue, net of amounts paid to suppliers." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm, published 2026-02-13]
- Airbnb "presents revenue net, as an agent, because it does not control the right to use the properties either before or after completion of its service. It does not fulfill rental promises, bear inventory risk, or set prices." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12]
- **Timing is check-in.** Booking Holdings recognises revenue "at a point in time when the Company has completed its post-booking services and the travelers begin using the arranged travel services," and notes that "because we recognize revenues from bookings when the traveler checks in, our reported revenues are not at risk of being reversed due to cancellations." Gross bookings are recognised at booking, revenue at check-in; the gap is the booking window. [VERIFIED: Booking Holdings FY2025 10-K, as above]
- Airbnb's service fees cover "platform use, customer support, and payment processing activities, which are not distinct and collectively constitute a single performance obligation" that "is satisfied at the point of check-in." For stays of more than a month, each month is a separate contract and revenue is recognised at the first check-in and at each monthly anniversary. [VERIFIED: Airbnb FY2025 10-K, as above]
- Expedia's agency hotel revenue is also recognised "when the stayed night occurs as we provide post booking services," while air agency revenue is recognised at booking. [VERIFIED: Expedia FY2025 10-K, as above]

**Balance-sheet objects the ledger must produce.** Booking Holdings reports **deferred merchant bookings of $5.3bn** at 31 December 2025, "comprised principally of amounts estimated to be payable to travel service providers as well as our estimated future revenues for our commission or margin and fees," which are "mostly subject to refunds for cancellations." [VERIFIED: Booking Holdings FY2025 10-K] Airbnb reports **funds receivable and amounts held on behalf of customers of $5,931m** with an equal liability, **funds payable and amounts payable to customers**, plus **unearned fees of $1,616m** at 31 December 2025. [VERIFIED: Airbnb FY2025 10-K]

> **OTA vs hosted stays.** The accounting is the same in principle (net, at check-in), but the cash shape differs. An OTA merchant booking holds the *whole* guest payment as deferred merchant bookings and owes most of it to a business supplier, generally within 30 days of the stay (Expedia: "Payments to suppliers are generally due within 30 days of check-in or stay" [VERIFIED: Expedia FY2025 10-K]). Airbnb holds guest funds as customer funds in safeguarded accounts and pays the host the business day after check-in (§3.2), so its float per booking is shorter after check-in but longer before it.

### 1.4 Fee structures ⚠

- **Airbnb moved to host-only fees.** "Historically, the Company operated only under a split-fee structure, charging service fees as a percentage of the booking amount to both hosts and guests. In October 2025, the Company began transitioning to a single-fee structure, charging only the host a service fee." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12]
- Airbnb excludes from revenue "amounts assessed by governmental authorities, such as taxes ... cleaning and pet fees." [VERIFIED: same filing]
- Booking.com charges a "payment service fee" per reservation for bank-transfer payouts, "based on your property's location"; with VCC payouts the property pays "a transaction fee directly to your bank or payment provider" instead. [VERIFIED: https://partner.booking.com/en-gb/solutions/payments-bookingcom, undated, fetched 2026-10]

[ASSUMPTION/JUDGEMENT] A fee model change such as Airbnb's (two fee lines collapsing into one) is a pricing-engine, invoice, tax and ledger change at the same time: VAT on the guest fee disappears from the guest invoice and VAT on a larger host fee appears on the host invoice. Chapters should use it as the worked example of why fee lines must be data-driven, versioned components rather than hard-coded columns.

---

## PART 2: When the guest pays — pay now, pay at property, pay later

### 2.1 The menu of payment timings

| Timing | OTA example | Hosted-stays example | What the platform must hold |
| --- | --- | --- | --- |
| Pay now (prepaid) | Booking.com `pay_online_now`; Expedia Collect | Airbnb standard checkout | Captured funds; refund liability until non-refundable |
| Pay at property | Booking.com pay-at-property; Expedia Hotel Collect | Not offered by Airbnb | Optional card guarantee, forwarded to the property |
| Pay later online | Booking.com "pay online later" | Airbnb Reserve Now, Pay Later | Stored credential; a scheduled merchant-initiated charge |
| Pay in parts | — | Airbnb Pay Part Now, Part Later | Two charges against one booking |
| Third-party instalments | Klarna, Affirm, PayPal Credit via Payments by Booking.com | Pay Over Time with Klarna | Provider-specific redirect/async flow |

- **Booking.com Demand API models.** The Demand API (for affiliates and partners booking Booking.com inventory) documents separate payment models: "Booking.com collects payment" ("Booking.com is the merchant of record"; "Booking.com charges the traveller's credit card"), "partner collects payment" (the partner charges the traveller and pays Booking.com with a VCC), pay-at-property, and corporate models. The `orders/preview` call returns which `payment.method` and `payment.timing` values are allowed for an offer. [VERIFIED: https://developers.booking.com/demand/docs/payments/models/booking-collects, undated (docs v3.3 labelled latest), fetched 2026-10]
- **Pay at property.** "The traveller pays the property directly during their stay"; where a card is required "to guarantee the booking," Booking.com "securely forwards the booking guarantee information to the property," which then charges the traveller. [VERIFIED: https://developers.booking.com/demand/docs/payments/models/pay-at-property, undated, fetched 2026-10]
- **Pay later online.** In the partner-collects flow, the pay-later schedule obliges the partner to "ensure that the VCC has sufficient funds at least 2 days prior to the pay-later collection date." [VERIFIED: https://developers.booking.com/demand/docs/payments/models/partner-collects, undated, fetched 2026-10]
- **Payment methods behind Payments by Booking.com.** All partners can take cards and cash; partners that opt in can also offer PayPal, Apple Pay, Google Pay, Alipay, WeChat, iDEAL, Venmo, "Buy now, pay later solutions such as Klarna, Affirm or PayPal Credit," and Booking.com Wallet credits. [VERIFIED: https://partner.booking.com/en-gb/solutions/payments-bookingcom, undated, fetched 2026-10]

### 2.2 Airbnb Reserve Now, Pay Later (2025) ⚠

- **Launch.** Airbnb announced Reserve Now, Pay Later on **14 August 2025** for US guests booking eligible domestic listings "with a moderate or flexible cancellation policy." Guests pay nothing at booking and "don't need to pay the full amount until shortly before the end of the listing's free cancellation period." "Cancellation policies selected by hosts remain unchanged." [VERIFIED: https://news.airbnb.com/reserve-now-pay-later/, published 2025-08-14]
- **Rationale given.** In an Airbnb/Focaldata survey of 2,159 US adults (July 2025), 42% said they had delayed or missed their preferred accommodation because of coordinating payments with co-travellers. [VERIFIED: same page]
- **Expansion.** On **23 February 2026** Airbnb extended the option to Asia Pacific guests booking eligible listings worldwide (excluding users paying in BRL, INR or TRY) and said the US launch helped accelerate nights and seats booked in Q4 2025 versus Q3 2025. The design point is explicit: "because the payment from guests is always due before the free cancellation period ends, hosts have time to secure another booking even if a guest cancels." [VERIFIED: https://news.airbnb.com/introducing-reserve-now-pay-later-giving-guests-greater-flexibility/, published 2026-02-23]
- **Contract mechanics.** Airbnb's Payments Terms (non-European users) say that under Reserve Now, Pay Later the full price is due "at a later time prior to check-in," shown at checkout, and the original payment method is charged automatically; if that charge fails the guest has **72 hours** to pay by another method or the booking may be cancelled under the host's policy. Pay Part Now, Part Later works the same way for the balance. [VERIFIED: https://www.airbnb.com/help/article/2909, published 2026-02-05]
- **Balance sheet.** Airbnb's 10-K lists "unbilled amounts for confirmed bookings under the terms of our payment programs (Pay Less Upfront and Reserve Now, Pay Later)" among its foreign-currency-exposed items, and describes the instalment accounting: the first instalment goes to funds receivable/payable net of fees, and "the full value of the service fees is recorded as cash ... and unearned fees ... upon receipt of the first installment payment." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12]

[ASSUMPTION/JUDGEMENT] Architecturally, pay-later converts a booking from "paid" to "promised", adding a state machine: confirmed-unpaid → charge scheduled → charge attempted → paid / grace period / auto-cancelled. It also needs a scheduler that is idempotent across retries and an inventory rule (the night stays blocked while unpaid). It is the hosted-stays mirror of the OTA's long-standing "pay at property with card guarantee", except that the platform, not the property, runs the deferred charge and owns the failure.

### 2.3 Strong customer authentication and deferred charges (EU/EEA)

- **SCA duty.** PSD2 Article 97(1) requires a payment service provider to apply strong customer authentication where the payer "initiates an electronic payment transaction," and Article 97(2) requires remote transactions to use elements that "dynamically link the transaction to a specific amount and a specific payee." [VERIFIED: http://publications.europa.eu/resource/celex/32015L2366, published 2015-12-23 (OJ L 337)]
- **Recurring series.** The SCA regulatory technical standards require SCA "when a payer creates, amends, or initiates for the first time, a series of recurring transactions with the same amount and with the same payee," and allow PSPs not to apply it for subsequent transactions in that series (Article 14). Low-value payments up to EUR 30 are exempt within cumulative limits (Article 16). Article 17 exempts "dedicated payment processes or protocols that are only made available to payers who are not consumers" where the competent authority is satisfied of equivalent security. [VERIFIED: http://publications.europa.eu/resource/celex/32018R0389, published 2018-03-13 (OJ L 69)]
- **Merchant-initiated transactions.** Stripe's SCA guide treats merchant-initiated payments (charges made later, with the customer's prior mandate, while the customer is not present) as technically out of SCA scope, provided the card was authenticated when first saved or at the first payment; the issuing bank makes the final decision. [WIDELY REPORTED: https://stripe.com/guides/strong-customer-authentication, undated, fetched 2026-10] The MIT construct itself comes from card-scheme rules and EBA Q&A, which were not fetched in this session.
- **Liability.** Stripe's guide states that a successfully authenticated payment can shift fraud-chargeback liability away from the merchant, but when an exemption is requested and accepted, liability "stays with the merchant." [WIDELY REPORTED: same page]
- **Pre-authorisation for unknown amounts.** PSD2 Article 75: where a card payment is initiated by or through the payee "and the exact amount is not known at the moment when the payer gives consent," the payer's PSP "may block funds on the payer's payment account only if the payer has given consent to the exact amount of the funds to be blocked," and must release the block once the amount is known. [VERIFIED: http://publications.europa.eu/resource/celex/32015L2366, published 2015-12-23] This governs hotel incidental holds and damage-deposit holds.
- **VCCs and the B2B exemption.** Booking.com's Demand API tells partners paying it by virtual card to set `card.authentication.sca_exemption` to `virtual`. [VERIFIED: https://developers.booking.com/demand/docs/payments/models/partner-collects, undated, fetched 2026-10] [ASSUMPTION/JUDGEMENT] This is consistent with the Article 17 secure-corporate-payment exemption for non-consumer payment processes, but the document does not cite the article.
- Booking.com tells properties that Payments by Booking.com keeps them compliant with "data privacy and Strong Customer Authentication" without work on their side. [VERIFIED: https://partner.booking.com/en-gb/solutions/payments-bookingcom, undated, fetched 2026-10]

[ASSUMPTION/JUDGEMENT] Design rule for chapters: any flow that charges later (pay later, pay in parts, post-stay damage, no-show fee, monthly-stay instalments) must (1) run SCA at checkout for the *setup* of the stored credential, (2) store the network transaction identifier returned by that first authentication, and (3) flag every later charge as merchant-initiated with that reference. Without step 2, deferred charges fall back into SCA and fail with the guest absent.

> **OTA vs hosted stays.** In the agency model the *hotel* is the merchant for the deferred charge and the OTA only forwards the card guarantee; the hotel's PSP carries the SCA problem. In the merchant model and on Airbnb the platform carries it. That is one reason the shift to merchant concentrates payment engineering at the platform.

---

## PART 3: Paying the supply side

### 3.1 Virtual credit cards to hotels

A **virtual credit card (VCC)** is a single-use card number issued per booking and loaded with the amount owed to the property. The property charges it through its own card terminal or PSP as if the guest had paid by card. It lets an OTA pay tens of thousands of hotels through infrastructure they already have, without collecting bank details or running cross-border bank transfers.

- **Booking.com.** Payouts under Payments by Booking.com go by bank transfer, VCC, or (for Homes properties in the US and Canada only) Stripe. With VCC, "Booking.com facilitates their payment and loads the exact amount onto that virtual credit card. You'll receive a new temporary digital card for every booking, which becomes chargeable on a POS as soon as the reservation becomes non-refundable (if you meet certain criteria)." [VERIFIED: https://partner.booking.com/en-gb/solutions/payments-bookingcom, undated, fetched 2026-10]
- **VCC activation policies.** Booking.com's connectivity API documents seven VCC activation policy codes: on check-out date (1), when the reservation becomes non-refundable (2), on check-in date (3), one day after check-in (4), "long after check-out" (5), on cancellation date (6), and on booking date (7). Switching from VCC to bank transfer is supported; "the reverse direction (BT to VCC) is currently not supported." [VERIFIED: https://developers.booking.com/connectivity/docs/payments-by-booking-onboarding-api/understanding-payouts, undated, fetched 2026-10]
- **Expedia Virtual Card (EVC).** Integrator documentation describes an Expedia-issued single-use card delivered with each Expedia Collect booking notification and visible in Partner Central; properties typically charge it at check-out for the net rate plus taxes, with incidentals on a separate folio paid by the guest. One PMS vendor states the EVC can be charged only from the check-in day to six months afterwards, and that charging before check-in fails. [WIDELY REPORTED: https://help.lodgify.com/hc/en-us/articles/360016077759, undated; https://blog.hotellinksolutions.com/experience-seamless-payments-at-your-hotel-with-expedia-virtual-card, undated] Expedia's developer documentation on EVCs could not be fetched (see Research limitation).
- **Airbnb also pays some hosts by VCC.** Airbnb's Payments Terms list VCC among host payout methods for eligible hosts; the card "must be charged within a set window around check-in and expires after 180 days." [VERIFIED: https://www.airbnb.com/help/article/2909, published 2026-02-05] Airbnb's European Payments Terms state which PSD2 provisions do not apply to non-consumer hosts using VCC payouts (Section 3.10.2.6.1). [VERIFIED: https://www.airbnb.ie/help/article/2909, published 2026-02-05]
- **Issuers.** [ASSUMPTION/JUDGEMENT] OTA VCC programmes are run with commercial-card issuers and issuing processors (Mastercard is commonly reported for Booking.com's cards). No primary source naming the issuing bank was found; do not name one in the book without a source.

[ASSUMPTION/JUDGEMENT] Architecture implications: a VCC programme is an *issuing* system (card creation, funding, activation date, amount limits, expiry, reconciliation of card settlements against bookings) attached to the booking lifecycle. Booking modifications must re-size or re-issue cards; cancellations must void them (Booking.com's activation code 6 shows that some cards activate *on* cancellation to pay a cancellation fee). The interchange the issuer earns on VCC spend is also why OTAs prefer VCC to bank transfer: the hotel pays card acceptance fees, the OTA side may earn rebates (Booking Holdings lists "credit card processing rebates" in merchant revenue — VERIFIED above).

### 3.2 Host payouts on hosted-stays platforms

- **Airbnb timing (contractual).** For accommodation, Airbnb Payments initiates the payout "by the end of the business day after the Guest's scheduled check-in date." Hosts without two completed stays (unless they verified a listing), or hosts in breach, are paid by the end of the business day after **check-out**. Stays of 28 nights or more follow a monthly schedule. [VERIFIED: https://www.airbnb.com/help/article/2909, published 2026-02-05] The European terms use the same wording (Section 3.3.1) and say the UK and Luxembourg entities "endeavor" to deliver payouts by the end of the business day after initiation. [VERIFIED: https://www.airbnb.ie/help/article/2909, published 2026-02-05]
- **Airbnb timing (10-K).** Airbnb holds the guest's payment "until check-in, at which time we recognize our service fee as revenue and initiate the process to remit the payment to the host, which generally occurs on the business day after the scheduled check-in." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12] The commonly quoted "about 24 hours after check-in" is a help-centre simplification; the contract says "end of the business day after."
- **Arrival by method.** After release: Fast Pay and pay-to-card "30 minutes or less" (eligible regions), Payoneer prepaid card within 24 hours, PayPal within one business day, Western Union one business day, US ACH 3 business days, bank account 3–5 business days, international wire 3–7 business days. A fraud review can delay funds "up to 45 days after guest check-in." [VERIFIED: https://www.airbnb.com/help/article/425, undated, fetched 2026-10]
- **Holds.** Airbnb Payments may "temporarily place a hold, suspend, or cancel any Payout" for fraud prevention, risk assessment, investigations or failed verification, and may delay release "until a refund decision is made." When a host cancels, funds are held "for up to 72 hours" while the guest is refunded or rebooked. Refunds larger than a host's payout may be recovered from future payouts. [VERIFIED: https://www.airbnb.com/help/article/2909 and https://www.airbnb.com/help/article/2908, both published 2026-02-05]
- **Interest on float.** Airbnb Payments "may combine collected funds and invest them, keeping the interest" (Payments Terms, Section 3.9). [VERIFIED: https://www.airbnb.com/help/article/2909, published 2026-02-05] Airbnb reported interest income of $705m in 2025 ($818m in 2024). [VERIFIED: Airbnb FY2025 10-K]
- **Booking.com payouts to properties.** Bank-transfer payouts "monthly, weekly or – in some countries – even daily"; the Stripe option (Homes in US/Canada) releases funds "per reservation on the reservation check-in day." [VERIFIED: https://partner.booking.com/en-gb/solutions/payments-bookingcom, undated; https://developers.booking.com/connectivity/docs/payments-by-booking-onboarding-api/understanding-payouts, undated; both fetched 2026-10] An integrator guide reports bank-transfer payouts processed on Thursdays or the 1st of the month and arriving about 14 days after check-out; treat as possibly outdated. [WIDELY REPORTED: https://nightsbridge.screenstepslive.com/a/1722322-booking-com-payment-options, undated]

> **OTA vs hosted stays.** An OTA pays businesses: invoices, VAT numbers, monthly netting, VCCs, 30-day terms. A hosted-stays platform pays millions of individuals: KYC at payout setup, many payout rails, next-day release, payout holds as a primary fraud control, and tax-information collection (DAC7, 1099-K) gating payouts. Airbnb's terms allow payouts to be withheld when tax documentation is insufficient [VERIFIED: https://www.airbnb.com/help/article/2908, published 2026-02-05].

### 3.3 Split payments and platform payment providers

Most stays marketplaces smaller than Airbnb or Booking.com do not build licensed payment entities; they rent one from a platform PSP.

- **Stripe Connect** offers three charge types. *Destination charges* — "best suited for marketplaces, such as a home rental marketplace" — create the charge on the platform and transfer a portion to the connected account; "refunds and chargebacks reduce your platform's balance." *Separate charges and transfers* decouple the charge from transfers, for "one-to-many" splits or "charges created before the destination account is known." *Direct charges* make the connected account the seller, with refunds and chargebacks hitting its balance. Setting `on_behalf_of` makes the connected account the business of record and settles in its country. [VERIFIED: https://docs.stripe.com/connect/charges, undated, fetched 2026-10]
- **Adyen for Platforms / Marketplaces** lets a marketplace "split the payments between one or more users, deduct costs as needed, and hold funds until payout," choose managed or custom payout timing, and onboard sellers that "Adyen verif[ies] ... before paying out." [VERIFIED: https://docs.adyen.com/marketplaces/, undated, fetched 2026-10]
- Booking.com itself uses Stripe as one payout rail for Homes properties in the US and Canada. [VERIFIED: https://developers.booking.com/connectivity/docs/payments-by-booking-onboarding-api/understanding-payouts, undated, fetched 2026-10]

[ASSUMPTION/JUDGEMENT] For a hosted-stays marketplace, the natural fit is "separate charges and transfers" (or an Adyen split with a hold), because the host payout must wait for check-in, a single booking may pay a host *and* a co-host or cleaner, and the platform's fee is known at booking but the payout may be altered by later events (cancellation, damage claim, alteration). Destination charges with an immediate transfer move money to the host too early.

---

## PART 4: Regulation of the money — licences and the commercial-agent exclusion

### 4.1 PSD2's commercial-agent exclusion and why marketplaces lost it

- **The text.** PSD2 Article 3(b) excludes "payment transactions from the payer to the payee through a commercial agent authorised via an agreement to negotiate or conclude the sale or purchase of goods or services on behalf of **only the payer or only the payee**." [VERIFIED: http://publications.europa.eu/resource/celex/32015L2366, published 2015-12-23]
- **The intent.** Recital 11 says the exclusion under the earlier directive was "applied very differently across the Member States," including "by e-commerce platforms that act as an intermediary on behalf of both individual buyers and sellers without a real margin to negotiate or conclude the sale." PSD2 therefore keeps the exclusion for agents acting for only one side "regardless of whether or not they are in possession of client funds," while agents acting for both sides "should be excluded only if they do not, at any time enter into possession or control of client funds." [VERIFIED: same document]

[ASSUMPTION/JUDGEMENT] Consequences for stays marketplaces:

- An OTA in the **agency** model never touches the guest's money and needs no payment licence for it.
- A platform that **collects** guest money and pays it on to a host or hotel is in scope unless it can show it is the commercial agent of *only one side* — typically the property/host. That is why both Airbnb's and many OTAs' terms appoint the platform (or its payment affiliate) as the *host's* "limited payment collection agent," and why payment to that agent discharges the guest's debt (see §4.2). Whether a regulator accepts the one-sided-agent position is jurisdiction-specific; Airbnb has chosen to hold licences anyway.
- PSD3/PSR (in EU legislative process at the time of writing ⚠) were not reviewed in this brief; Booking Holdings' 10-K names "the EU's Payment Services Directive 3 and Payment Services Regulations" as a compliance risk. [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18]

### 4.2 How Airbnb structures licensed payment entities

- **Entities and licences (10-K).** Airbnb Payments, Inc. is "regulated as a 'Money Services Business' by the Financial Crimes Enforcement Network and requires state licenses to act as a money transmitter." Airbnb Payments Luxembourg SA (APLux) "operates as a licensed payments institution across the European Economic Area"; Airbnb Payments UK Limited (APUK) "is licensed as an electronic money institution"; Airbnb Payments Canada Inc. is registered as a PSP in Canada. Compliance spans DORA, Luxembourg's PSD2 transposition, the UK Payment Services Regulations 2017 and Canada's Retail Payment Activities Act. [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12]
- **Entities by user residence (terms).** For users outside Europe, UK and Australia: Airbnb Payments, Inc. (US and territories), Airbnb Payments India Pvt. Ltd. (India), Airbnb Plataforma Digital Ltda. (Brazil), Airbnb Payments Canada Inc. (Canada, for bookings confirmed on or after 8 September 2025), Airbnb Payments Mexico (some Mexican services from 20 March 2026), and Airbnb Payments UK for China and all other countries. [VERIFIED: https://www.airbnb.com/help/article/2909, published 2026-02-05] For EEA residents the counterparty is Airbnb Payments Luxembourg S.A., supervised by the CSSF under Luxembourg's Law of 10 November 2009 on payment services; UK and Swiss users contract with Airbnb Payments UK Ltd. [VERIFIED: https://www.airbnb.ie/help/article/2909, published 2026-02-05]
- **Collection-agent clause.** Hosts appoint Airbnb Payments as their payment collection agent "solely for the limited purpose of accepting and processing funds from Guests," and once a guest pays, "the Guest's payment obligation to the Host(s) for the agreed upon amount is extinguished." [VERIFIED: https://www.airbnb.ie/help/article/2909 and https://www.airbnb.com/help/article/2909, both published 2026-02-05]
- **Safeguarding.** "In certain jurisdictions, we are required to either safeguard customer funds in bankruptcy-remote bank accounts, or hold such funds in eligible liquid assets ... equal to at least 100% of the aggregate amount held on behalf of customers." [VERIFIED: Airbnb FY2025 10-K, as above]

**Booking.com.** Booking Holdings' 10-K says regulators "may determine, and in some cases are likely to determine, that certain aspects of our business are subject to laws that govern payments activities, such as money transmission and online payments processing, which could require us to obtain licenses." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18] Booking.com's traveller terms say "If we organize your payment, we (or, in some cases, our affiliate) will be responsible for managing it," name Booking.com B.V. as the platform provider for accommodation, and name Booking.com Transport Limited as merchant of record for transport. [VERIFIED: https://www.booking.com/content/terms.html, updated 2025-08-25] Which Booking.com entity holds which EU payment authorisation for accommodation payments was **not verified**.

> **OTA vs hosted stays.** The licensing burden scales with how much of the flow is merchant/collect. Airbnb, which collects everything and pays individuals in ~190 countries, operates licensed payment entities on three continents. An agency-only OTA needs none; a mixed OTA needs one wherever it facilitates payments, or a PSP partner that carries the licence (Stripe, Adyen).

---

## PART 5: Risk — deposits, damage, refunds, chargebacks and fraud

### 5.1 Security deposits and damage

- **Booking.com.** A property "might require a 'damage deposit' before or at check-in"; Booking.com "won't be involved in any financial settlement related to damage deposits." Separately, under Booking.com's damage policy the property "will have 14 days to submit a damage payment request through our Platform," and Booking.com then arranges the charge on the property's behalf. [VERIFIED: https://www.booking.com/content/terms.html, updated 2025-08-25]
- **Airbnb.** The ToS provide for Damage Reports whose amounts "Airbnb via Airbnb Payments may charge [to] the Payment Method" of the booking; no security deposit appears in the current ToS. [VERIFIED: https://www.airbnb.com/help/article/2908, published 2026-02-05] AirCover for Hosts "includes property damage protection of up to $3 million per stay, liability coverage of up to $1 million per occurrence," deep-cleaning and pet-damage protection. [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12] ⚠
- [ASSUMPTION/JUDGEMENT] Airbnb's 2016 payments post lists "security deposits" among the financial actions its old system struggled to attach to a reservation [VERIFIED: https://medium.com/airbnb-engineering/scaling-airbnbs-payment-platform-43ebfc99b324, published 2016-09-12]. The current terms replace a held deposit with a post-stay claim charged to the stored card and backed by a platform-funded protection programme. Chapters can present this as the hosted-stays answer to the hotel incidental pre-authorisation: a merchant-initiated charge after the stay rather than an Article 75 block before it.

### 5.2 Refunds and cancellations

- Booking.com: "any cancellation/no-show fee and any refund will depend on the Service Provider's cancellation/no-show policy." [VERIFIED: https://www.booking.com/content/terms.html, updated 2025-08-25]
- Airbnb: "if you cancel a Reservation, the amount refunded to you is determined by the Host's cancellation policy," unless other policies take precedence. [VERIFIED: https://www.airbnb.com/help/article/2908, published 2026-02-05]
- Booking.com takes on refund costs for chargebacks for partners using Payments by Booking.com: "We also handle chargebacks and disputed payments, covering any refund costs." [VERIFIED: https://partner.booking.com/en-gb/solutions/payments-bookingcom, undated, fetched 2026-10]

### 5.3 Chargebacks and fraud liability

- **Booking Holdings.** "We may be held liable for fraudulent transactions on our platforms, as well as other payment disputes. Accordingly, we calculate and record an allowance for resulting chargebacks." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18]
- **Expedia.** "We record a reserve for chargebacks and cancellations at the time of the transaction based on historical experience." Cost of revenue includes "credit card processing, including merchant fees, fraud and chargebacks." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm, published 2026-02-13]
- **Airbnb.** "For the year ended December 31, 2025, total chargeback expense was $67 million." Merchant fees and chargebacks together were **$1,666m** in 2025 ($1,508m in 2024), about 13.6% of revenue. [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12]
- **Who absorbs the loss on a platform PSP.** With Stripe destination charges or separate charges and transfers, "your platform balance is automatically debited for the disputed amount and fee"; the platform may then try to recover by reversing the transfer to the connected account. [VERIFIED: https://docs.stripe.com/connect/charges, undated, fetched 2026-10]

[ASSUMPTION/JUDGEMENT] The chargeback window (card schemes allow disputes months after the transaction) is longer than the host-payout delay (one business day after check-in). A hosted-stays platform therefore carries the dispute risk after it has already paid the host, and recovers it, if at all, from future payouts. This is the structural reason for new-host payout delays (paid after check-out until two stays complete), payout holds and fraud reviews of up to 45 days (all VERIFIED above).

> **OTA vs hosted stays.** For an agency booking the hotel owns disputes. For an OTA merchant booking the OTA owns them but pays the hotel only after the stay (VCC activation or 30-day terms), so it can still net losses. A hosted-stays platform pays sooner and to individuals, so it must lean more on risk scoring before payout.

---

## PART 6: FX and multi-currency

- **Guest presentment versus host settlement.** Airbnb's platform "generally enables guests to make payments in the currency of their choice to the extent that the currency is supported by Airbnb, which may not match the currency in which the host elects to be paid. As a result, in those cases, we bear the currency risk of both the guest payment as well as the host payment due to timing differences in such payments." Airbnb hedges with foreign-currency derivatives. [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12]
- **Airbnb's terms on rates.** "The price displayed to you is based on a currency conversion rate determined by us." Payouts are sent in the currency of the payout method; providers may add "transaction, currency conversion or other fees." Where the guest's bank converts, it does so "based on an exchange rate and fee amount determined solely by your bank." [VERIFIED: https://www.airbnb.com/help/article/2908 and https://www.airbnb.ie/help/article/2909, both published 2026-02-05]
- **Booking.com's terms on rates.** If the currency selected on the platform differs from the property's currency, Booking.com may convert, and "the fee will be expressed as a percentage over European Central Bank rates"; the card issuer may add a foreign-transaction fee. [VERIFIED: https://www.booking.com/content/terms.html, updated 2025-08-25]
- **EU transparency rule for conversion at the point of sale (DCC).** Regulation (EU) 2019/518 says information on currency conversion charges "have not achieved sufficient transparency" and requires parties offering conversion "at an ATM or at the point of sale" to disclose charges before payment, including "on-screen in the case of online purchases," expressed as a mark-up over the latest ECB reference rate. [VERIFIED: http://publications.europa.eu/resource/celex/32019R0518, published 2019-03-29 (OJ L 91)]
- **Scale of currencies.** In 2016 Airbnb described supporting 191 countries, "over 70 currencies, and a network of over two dozen payment routes." [VERIFIED: https://medium.com/airbnb-engineering/scaling-airbnbs-payment-platform-43ebfc99b324, published 2016-09-12] — evidence over three years old; numbers will have changed.
- Booking Holdings notes merchant processing costs "are typically higher for foreign currency transactions." [VERIFIED: Booking Holdings FY2025 10-K]

[ASSUMPTION/JUDGEMENT] The ledger must store three currencies per booking: the **listing/rate currency** (what the host or hotel priced), the **presentment currency** (what the guest saw and paid), and the **settlement/payout currency** (what the supplier receives), plus the rate and timestamp of each conversion. The platform's FX exposure sits between booking and payout; with pay-later options (Part 2) it also sits between booking and *collection*.

> **OTA vs hosted stays.** Hotels contract rates in a currency and are typically paid in it (VCC loaded in that currency). Hosts can often pick a payout currency different from the listing currency, adding a second conversion that the platform owns.

---

## PART 7: Taxes

### 7.1 VAT on the accommodation itself

- **Place of supply.** Accommodation "in the hotel sector or in sectors with a similar function" is a service connected with immovable property, taxed where the property is (VAT Directive Article 47 as substituted in 2008, in force from 2010). [VERIFIED: http://publications.europa.eu/resource/celex/32008L0008, published 2008-02-20]
- **OTAs acting in their own name fall into the tour-operator margin scheme.** The CJEU held in *Alpenchalets Resorts* (C-552/17) that "the mere supply by a travel agent of holiday accommodation rented from other taxable persons ... amount[s] to a single service covered by the special scheme for travel agents," and that such a supply "cannot be subject to a reduced tax rate." [VERIFIED: http://publications.europa.eu/resource/celex/62017CJ0552, published 2018-12-19] Article 306 limits the scheme to travel agents who "deal with customers in their own name" and excludes those acting "solely as intermediaries." [VERIFIED: http://publications.europa.eu/resource/celex/32006L0112, published 2006-12-11]
- [ASSUMPTION/JUDGEMENT] The *Alpenchalets* rule is why the merchant-versus-agency distinction is also a VAT distinction in Europe: a merchant-model OTA that resells accommodation in its own name may owe margin-scheme VAT at the standard rate on its margin, whereas a disclosed agent supplies an intermediation service. How each OTA's contracts are characterised country by country is not public; treat any specific claim as unverified.
- **Rates change.** ⚠ The Netherlands abolished the reduced 9% VAT rate for accommodation from 1 January 2026, moving hotels, holiday homes, B&Bs and platform rentals to 21% (camping stays at 9%). [WIDELY REPORTED: https://www.grantthornton.nl/insights/tax/verlaagd-btw-tarief-voor-logies-vervalt-per-1-januari-2026/, 2025; https://www.khn.nl/nieuws/informeer-je-gasten-over-de-btw-verhoging-in-2026, 2025]

### 7.2 VAT on the platform's commission

- **B2B (hotel or VAT-registered host).** The general rule for services to a taxable person is the place where that person is established (Article 44), so a Netherlands-based platform's commission to a hotel in another member state is taxed there, normally by reverse charge. [VERIFIED: http://publications.europa.eu/resource/celex/32008L0008, published 2008-02-20; reverse-charge mechanics are ASSUMPTION/JUDGEMENT]
- **B2C (non-taxable host).** Services by an intermediary "acting in the name and on behalf of another person" to a non-taxable person are taxed where the underlying transaction is supplied (Article 46), i.e. where the property is. [VERIFIED: same]
- **ViDA restates this for platforms.** From 1 July 2028 a new Article 46a says "the place of supply of the facilitation service provided to a non-taxable person through the use of an electronic interface, such as a marketplace, platform, portal ... shall be the place where the underlying transaction is supplied." [VERIFIED: http://publications.europa.eu/resource/celex/32025L0516, published 2025-03-25 (OJ L 2025/516)]
- [ASSUMPTION/JUDGEMENT] For a hosted-stays platform with hosts across the EU, the commission is therefore taxed in the property's country, which requires either many VAT registrations or use of the One-Stop Shop (OSS) introduced by the 2021 EU VAT e-commerce package. The e-commerce package's own "deemed supplier" rule applies to goods sold through interfaces, not to accommodation; for accommodation the deemed-supplier rule arrives only with ViDA (§7.3).

### 7.3 ViDA: platforms as "deemed supplier" of short-term accommodation ⚠

- **The rule.** Council Directive (EU) 2025/516 of 11 March 2025 ("VAT in the digital age") inserts Article 28a: a taxable person facilitating, through an electronic interface, "short-term accommodation rental services, namely the uninterrupted rental of accommodation to the same person for a maximum of 30 nights," is "deemed to have received and supplied those services themselves" unless the underlying provider has (a) given the platform a VAT identification number for the member state where the supply takes place and (b) "declared to the taxable person facilitating the supply that they will charge any VAT due." [VERIFIED: http://publications.europa.eu/resource/celex/32025L0516, published 2025-03-25]
- **Purpose.** The recitals say the deemed-supplier model is "a legal fiction having no impact on rules outside the VAT legislation," and that platforms "should be required to charge VAT where underlying suppliers do not charge VAT because they are, for example, non-taxable persons or taxable persons availing themselves of the special scheme for small enterprises." [VERIFIED: same]
- **Dates.** Article 28a is part of the amendments "with effect from 1 July 2028," but by derogation member states apply it "at the earliest from 1 July 2028 and at the latest from 1 January 2030." [VERIFIED: same] The Dutch business portal gives the same window for the Netherlands ("between 1 July 2028 and 1 January 2030"). [VERIFIED: https://business.gov.nl/amendment/vat-overnight-accommodation-goes-up/, undated, fetched 2026-10]
- **Member-state options.** Member states may require the platform to validate the supplier's VAT number (Art. 28a(4)) and may exclude supplies under the small-enterprise scheme from the deemed-supplier rule (Art. 28a(5)); the Commission will publish the list of states using that option and report on the article by 1 July 2033. [VERIFIED: same]
- **Knock-on rules.** The supply from the underlying provider to the platform is exempt (new Article 136b), and the deemed supply does not affect the platform's right of deduction (Article 172a). Where the platform is *not* deemed supplier, it must keep records "sufficiently detailed to enable the tax authorities ... to verify that VAT has been accounted for correctly." [VERIFIED: same]
- Booking Holdings flags that "changing value-added tax regulation such as the VAT in the digital age proposal in the EU could increase complexity and costs associated with compliance." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18]

[ASSUMPTION/JUDGEMENT] Architecture implications: from 2028–2030 a stays platform must (1) capture each supplier's VAT status per member state (VAT ID, validation result, declaration that they will charge VAT), versioned over time; (2) decide per booking, at booking time, whether the platform is deemed supplier; (3) when it is, compute and charge VAT on the *full accommodation price* (not just the fee), issue the guest invoice in its own name and file it; and (4) keep the decision auditable. Hotels (VAT-registered, charging VAT) mostly stay outside the rule; non-registered individual hosts fall inside it. This is the clearest regulatory driver for a hosted-stays tax engine.

### 7.4 DAC7 platform reporting

- **Scope.** Council Directive (EU) 2021/514 makes "the rental of immovable property, including both residential and commercial property" a Relevant Activity for platform reporting, first reported for periods from **1 January 2023**, with reports due "no later than 31 January of the year following the calendar year" in which the seller is identified as reportable. [VERIFIED: http://publications.europa.eu/resource/celex/32021L0514, published 2021-03-25]
- **Exclusions.** "Excluded Seller" includes a governmental entity, a listed entity, an entity for which the platform "facilitated more than 2 000 Relevant Activities by means of the rental of immovable property in respect of a Property Listing during the Reporting Period" (in effect, large hotels), and small goods sellers (fewer than 30 sales and EUR 2,000). [VERIFIED: same]
- **Property-specific data.** For immovable-property sellers the platform reports "the address of each Property Listing" and land-registration number where available, consideration per quarter, the number of Relevant Activities per listing, and "where available, the number of days each Property Listing was rented ... and the type of each Property Listing," plus "fees, commissions or taxes withheld or charged" each quarter. [VERIFIED: same]

[ASSUMPTION/JUDGEMENT] DAC7 forces the payments ledger and the listings catalogue to join: quarterly consideration per listing per seller, with a verified address. It also turns tax-identity collection (TIN, date of birth, address) into an onboarding and payout gate for hosts.

### 7.5 United States: Form 1099-K ⚠

- The IRS states that under the One, Big, Beautiful Bill, third-party settlement organisations need not file Form 1099-K unless "the gross amount of reportable payment transactions to a payee exceeds $20,000 and the number of transactions exceeds 200"; the law "retroactively reinstated the reporting threshold" in effect before the American Rescue Plan Act of 2021. [VERIFIED: https://irs.gov/newsroom/irs-issues-faqs-on-form-1099-k-threshold-under-the-one-big-beautiful-bill-dollar-limit-reverts-to-20000, published 2025-10-23]
- The superseded phase-in had been more than $5,000 for 2024, $2,500 for 2025 and $600 from 2026. [WIDELY REPORTED: https://cpapracticeadvisor.com/2025/07/30/one-big-beautiful-bill-act-changes-1099-thresholds/165863/, 2025]
- [ASSUMPTION/JUDGEMENT] Airbnb Payments, Inc. as a money transmitter paying US hosts is the natural 1099-K filer for US hosts; platforms should keep the threshold as configuration because it has changed four times since 2021.

### 7.6 Tourist, occupancy and city taxes

- **Platform collection.** Airbnb's help centre lists 72 locations where "Airbnb calculates these taxes and collects them from guests at the time of booking" and "then remits collected taxes to the applicable tax authority on the hosts' behalf" — 20 countries worldwide and 52 US entries (states, DC, Puerto Rico, US Virgin Islands); these can include occupancy taxes, VAT and GST. Hosts there remain "responsible for assessing all other tax obligations." [VERIFIED: https://www.airbnb.com/help/article/2509, undated, fetched 2026-10] ⚠ The page lists jurisdictions at country/state level; the often-quoted "thousands of jurisdictions" figure counts sub-jurisdictions (cities, counties) and was **not verified** in this session.
- **Where Airbnb does not collect.** "In jurisdictions where we do not collect and remit lodging taxes, the responsibility for collecting and remitting these taxes, if applicable, generally rests with hosts." Airbnb reserves for jurisdictions where it could be held "jointly and severally liable with hosts." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12]
- **Amsterdam.** Tourist tax is **12.5%** of the overnight price (excluding VAT) since 1 January 2024, scheduled to stay through 2026; the 2026 coalition has proposed raising it to 16% in 2027 and then 1 point a year to 20%. [WIDELY REPORTED: https://nltimes.nl/2025/11/28/amsterdam-may-raise-tourist-tax-curb-mass-tourism, 2025; https://skift.com/2026/06/05/amsterdam-proposes-tourism-tax-hike-to-20/, 2026] The official amsterdam.nl page returned HTTP 403.
- **Paris / France.** For unclassified furnished tourist rentals French communes set taxe de séjour at 1%–5% of the per-person nightly price, capped at the commune's highest tariff, plus departmental and Île-de-France regional surcharges. A vendor guide gives Paris's 2026 cap as EUR 15.93 per person per night. [WIDELY REPORTED: https://www.hostaway.com/vacation-rental-guide/tourist-tax/france/, 2026] Airbnb began collecting taxe de séjour for Paris hosts in 2015. [WIDELY REPORTED: https://hospitality-on.com/fr/reglementation/airbnb-va-collecter-la-taxe-de-sejour-pour-ses-hotes-parisiens, 2015] Verify current rates against a Ville de Paris deliberation before quoting.
- **Italy: withholding host income tax.** Airbnb's 10-K says Italy "passed a law in 2017, purporting to require short-term rental platforms that process payments to withhold and remit host income tax and collect and remit tourist tax." Airbnb Ireland settled the 2017–2021 audit periods for **€576m** (December 2023), 2022 for €139m (December 2024) and 2023 for €179m (January 2025), without admitting liability. [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12] Booking.com settled a Guardia di Finanza claim under the same "STR Law" — that it should have withheld 21% of transaction value for certain Italian short-term-rental partners — for **$332m** in November 2024, also without admitting liability. [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18]
- **Airbnb's indirect-tax costs.** Airbnb's G&A rose $157m in 2025, "primarily due to a $74 million increase from non-income taxes and related fees and penalties." [VERIFIED: Airbnb FY2025 10-K]

### 7.7 US hotel occupancy tax litigation against OTAs

- **Expedia's current position.** "We currently have two lawsuits involving hotel occupancy taxes ... We believe that the statutes or ordinances at issue generally impose occupancy and other taxes on entities that own, operate or control hotels (or similar businesses) or furnish or provide hotel rooms." Expedia keeps a reserve and notes that "many of the statutes and regulations that impose these taxes were established before the emergence of the internet and ecommerce" and that some jurisdictions "have enacted ... legislation regarding the imposition of taxes on businesses that facilitate the booking of hotel or alternative accommodations." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm, published 2026-02-13]
- **Booking Holdings** reports travel transaction taxes collected from travelers net in revenue and is "involved in other tax-related audits, investigations, and litigation relating to ... travel transaction taxes (e.g., hotel occupancy taxes)." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18]
- [ASSUMPTION/JUDGEMENT] The core dispute in the US litigation wave (mid-2000s to late 2010s) was whether occupancy tax is due on the **retail price the guest pays the OTA** or only on the **net/wholesale rate the hotel receives** under the merchant model. Many jurisdictions answered by passing "marketplace facilitator" or "accommodations intermediary" laws that tax the full guest price and put the collection duty on the platform. Specific case names (e.g. San Antonio, District of Columbia, Hawaii) were **not verified** in this session and should be sourced from court records before use.

> **OTA vs hosted stays (tax).** Hotels are VAT-registered, collect city tax at the desk (or the OTA passes it through on a merchant booking) and sit outside DAC7. Individual hosts are often non-registered, cannot run a tax engine, and are exactly the population that DAC7, the Italian STR law, US marketplace-facilitator laws and ViDA's deemed-supplier rule target. The hosted-stays platform therefore becomes a tax collector and tax reporter by law, not by choice.

---

## PART 8: Ledgers, orchestration and reconciliation — what Airbnb has published

The most detailed public account of payments engineering at a stays marketplace is Airbnb's. It spans ten years; read the dates.

### 8.1 2016: from audit-trail reporting to a double-entry financial pipeline

- Early payments ran in a Rails app on mutable ActiveRecord models; finance relied on database triggers writing "audit trail tables," and "we had to reverse-engineer these audit entries to infer what happened in the production system." Reporting runtime "grew to many hours." [VERIFIED: https://medium.com/airbnb-engineering/scaling-airbnbs-payment-platform-43ebfc99b324, published 2016-09-12]
- The second generation introduced three systems: a **billing interface** that treats "each item (reservation nights, fees, taxes, etc) as discrete items" and emits platform events on Kafka; a **payments gateway** where "all payment transactions pass through this API layer and are recorded using an append-only data model"; and a **financial data pipeline** in Spark and Scala "built around the concept of discrete financial events." [VERIFIED: same]
- "The financial data pipeline is also constructed around the principle of double-entry bookkeeping, which means money must be added somewhere and removed from somewhere else. In other words, money can't be created out of thin air." It tracks "receivables, payables, revenues, and taxes" and "produces all of the data required for financial reporting to regulators, local governments, and even Airbnb's investors." [VERIFIED: same] — evidence is ten years old.
- The same post introduced the Brazilian Boleto support that gave Airbnb "a general-purpose pattern for asynchronous payments and booking": the reservation waits in a pending-payment state until the cash payment is confirmed. [VERIFIED: same]

### 8.2 2018: transactional integrity and three-way reconciliation

- "A singular processor relationship to move money globally simply does not exist," so Airbnb "integrates with a handful of gateways and dozens of processors," with settlement ranging from synchronous card payments to Boletos that "can take up to several days to settle." [VERIFIED: https://medium.com/airbnb-engineering/measuring-transactional-integrity-in-airbnbs-distributed-payment-ecosystem-a670d6926d22, published 2018-01-17]
- Host payouts largely go by **batch** files to banks, which "leaves our systems out-of-sync until batch response files are processed" — "up to several hours." [VERIFIED: same]
- Even the simplest booking has "at least two financial transactions" (guest pays Airbnb; Airbnb pays host), and "alterations, deposits/installments, group travel, tax withholding, VAT etc. all dramatically increase the number and complexity." [VERIFIED: same]
- "Typically, merchants reconcile all the money movement on the platform via 3-way reconciliation between platform transaction records, processor settlement files, and bank statements." Airbnb built a service that imports daily processor reports from SFTP into S3, normalises them, de-duplicates files and feeds reconciliation, which can also "'self-heal' certain aberrations when detected." [VERIFIED: same]

### 8.3 2019: idempotency (Orpheus)

- Airbnb built **Orpheus**, "a general-purpose idempotency library," used across payments services: an idempotency key per request, idempotency tables "always read and written from a sharded master database (for consistency)," and a library rather than a service for low latency. [VERIFIED: https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb, published 2019-04-16]

### 8.4 2022: rebuilt payment orchestration

- The orchestration system ensures "guests should be charged the right amount at the right time using their selected payment methods; hosts should be paid the right amount at the right time to their desired payout methods." It was rebuilt during the SOA migration rather than ported one-to-one. [VERIFIED: https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b, published 2022-02-24]
- "Every major workflow is divided into a directed acyclic graph (DAG) of retryable idempotent steps," built on Orpheus, giving "five 9s (99.999%) of consistency for payments"; Kafka event processors use the framework to turn at-least-once delivery into exactly-once processing. [VERIFIED: same]
- **Data immutability:** events are append-only, and an alteration ("adding another night to a stay") is modelled "as a new version in a sequence of plans for that product," so the versions together give "a complete history of the intended and actual money movement." The new data model is built "around the concept of a bill," not a reservation. [VERIFIED: same]
- **Migration:** four phases (Pricing, Payouts, Bookings, Data Migration); the stays bookings migration alone had "over 30 milestones"; two orchestration systems ran in parallel behind a translation layer for most of the migration. [VERIFIED: same]

### 8.5 2026: payment domains and local payment methods

- Airbnb's multi-year "Payments LTA" replatforming moved to "a capability-oriented services system structured by domains." The core payment domain covers "pay-in, payout, and payment intermediation" with subdomains "Pay-in, Payout, Transaction Fulfillment, Processing, Wallet & instruments, Ledger, Incentives & Stored Value, Issuing, and Settlement & Reconciliation." [VERIFIED: https://airbnb.tech/payments/pay-as-a-local/, undated (2026; the Medium original is https://medium.com/airbnb-engineering/pay-as-a-local-bef469b72f32), fetched 2026-10]
- Airbnb launched 20+ local payment methods in just over a year using **Multi-Step Transactions (MST)**, "a processor-agnostic framework that supports payment flows completed across multiple stages," with redirect, async (e.g. QR code plus webhook) and direct flow archetypes, a connector/plugin model for PSPs, YAML payment-method configuration and a PSP emulator. [VERIFIED: same]
- A separate 2026 post on **Skipper**, Airbnb's embedded durable-workflow engine, says it powers "critical workflows across insurance, payments, media processing, and infrastructure automation"; its example workflow charges a reservation, durably waits for payment capture, then marks the reservation accepted. [VERIFIED: https://airbnb.tech/infrastructure/skipper-building-airbnbs-embedded-workflow-engine/, undated, fetched 2026-10]
- "Issuing" appearing as a payment subdomain is consistent with the VCC host-payout method in Airbnb's terms (§3.1). [ASSUMPTION/JUDGEMENT]

### 8.6 Reference ledger design for stays (judgement)

[ASSUMPTION/JUDGEMENT] Combining the public material with the regulatory requirements above, a stays-marketplace ledger needs at least these accounts per booking, all double-entry, append-only and versioned on alteration:

| Account | Merchant/hosted booking | Agency booking |
| --- | --- | --- |
| Guest funds receivable / cash in transit (per PSP, per currency) | Yes | No |
| Customer funds held (safeguarded) | Yes (if licensed) | No |
| Payable to supplier (hotel/host), per payout currency | Yes, released at check-in or VCC activation | No |
| Commission/fee — unearned → earned at check-in | Yes | Commission receivable from property, invoiced |
| Taxes collected on behalf (VAT, city tax, withholding) per jurisdiction | Yes | Only where the platform is liable |
| VAT on platform fee (OSS/reverse charge) | Yes | Yes |
| Chargeback allowance / dispute receivable | Yes | No (property's risk) |
| FX gain/loss between presentment and payout | Yes | No |
| Protection-programme claims (damage, rebooking) | Hosted stays | Rare |

Reconciliation runs three ways (ledger ↔ PSP settlement files ↔ bank statements) for pay-in, and two more ways for payout (ledger ↔ payout-rail returns; ledger ↔ VCC issuer settlement).

---

## Key numbers

| Number | Value | Source | Date |
| --- | --- | --- | --- |
| Booking Holdings total gross bookings | $186.1bn (merchant $130.0bn, agency $56.1bn) | Booking Holdings 10-K FY2025 | 2026-02-18 |
| Booking Holdings merchant / agency revenue | $17,755m (+25.5%) / $7,968m (−6.5%) | Booking Holdings 10-K FY2025 | 2026-02-18 |
| Booking Holdings deferred merchant bookings | $5.3bn at 31 Dec 2025 | Booking Holdings 10-K FY2025 | 2026-02-18 |
| Booking.com properties | ~4.4 million at 31 Dec 2025 | Booking Holdings 10-K FY2025 | 2026-02-18 |
| Booking.com Italy STR-law settlement | $332m (Nov 2024) | Booking Holdings 10-K FY2025 | 2026-02-18 |
| Expedia revenue mix | 70% merchant / 22% agency / 8% other, of $14.7bn | Expedia 10-K FY2025 | 2026-02-13 |
| Expedia total gross bookings | $119.6bn | Expedia 10-K FY2025 | 2026-02-13 |
| Expedia supplier payment terms | Generally within 30 days of check-in or stay | Expedia 10-K FY2025 | 2026-02-13 |
| Airbnb GBV / nights and seats booked | $91.3bn / 533m | Airbnb 10-K FY2025 | 2026-02-12 |
| Airbnb revenue | $12,241m | Airbnb 10-K FY2025 | 2026-02-12 |
| Airbnb funds held on behalf of customers | $5,931m at 31 Dec 2025 | Airbnb 10-K FY2025 | 2026-02-12 |
| Airbnb merchant fees and chargebacks | $1,666m; chargeback expense $67m | Airbnb 10-K FY2025 | 2026-02-12 |
| Airbnb Italy settlements | €576m (2017–21), €139m (2022), €179m (2023) | Airbnb 10-K FY2025 | 2026-02-12 |
| Airbnb fee change | Host-only single fee from Oct 2025 | Airbnb 10-K FY2025 | 2026-02-12 |
| Airbnb host payout | End of business day after scheduled check-in | Airbnb Payments Terms | 2026-02-05 |
| Airbnb fraud-review delay | Up to 45 days after check-in | Airbnb help article 425 | fetched 2026-10 |
| Airbnb tax collect-and-remit list | 72 locations (20 countries, 52 US entries) | Airbnb help article 2509 | fetched 2026-10 |
| AirCover for Hosts | Up to $3m damage per stay; $1m liability | Airbnb 10-K FY2025 | 2026-02-12 |
| Payments by Booking.com claims | Up to 40% fewer cancellations, up to 80% fewer no-shows, up to 25% alternative payment methods | partner.booking.com | fetched 2026-10 |
| ViDA deemed supplier for STR | ≤30 nights; applies from between 1 Jul 2028 and 1 Jan 2030 | Directive (EU) 2025/516 | 2025-03-25 |
| DAC7 hotel exclusion | >2,000 rentals per listing per period | Directive (EU) 2021/514 | 2021-03-25 |
| SCA low-value exemption | ≤ EUR 30 (cumulative limits) | Delegated Reg. (EU) 2018/389 | 2018-03-13 |
| US 1099-K threshold | >$20,000 and >200 transactions | IRS IR-2025-107 | 2025-10-23 |
| Amsterdam tourist tax | 12.5% of room price excl. VAT (2024–2026) | NL Times (secondary) | 2025 |
| Netherlands VAT on accommodation | 9% → 21% from 1 Jan 2026 | Grant Thornton NL (secondary) | 2025 |
| Airbnb currencies (historic) | 191 countries, 70+ currencies, 24+ payment routes | Airbnb Engineering | 2016-09-12 |
| Airbnb payment consistency | 99.999% | Airbnb Engineering | 2022-02-24 |

## Open questions / not verifiable

- **Booking.com's payment licence.** Which Booking.com entity facilitates accommodation payments in the EEA and under which authorisation (or exclusion) is not stated in the 10-K or the terms. Do not assert a licence.
- **VCC issuers.** No primary source names the issuing bank or processor for Booking.com or Expedia virtual cards.
- **Expedia EVC rules.** Charging window, activation and refund handling come only from integrator documentation.
- **"Thousands of jurisdictions."** Airbnb's help centre lists 72 country/state-level locations; the sub-jurisdiction count was not verified.
- **US occupancy-tax case law.** Case names, courts and outcomes need court sources.
- **ViDA transposition.** Which member states will apply Article 28a from 1 July 2028 rather than 1 January 2030, and which will use the small-enterprise exclusion (Art. 28a(5)), is not yet published. ⚠
- **PSD3/PSR.** Final texts and how they treat marketplace commercial agents were not reviewed.
- **MIT rules.** The EBA Q&A and card-scheme rules defining merchant-initiated transactions were not fetched; the brief relies on Stripe's guide.
- **Airbnb's current ledger internals.** Beyond the 2016 description and the 2026 list of subdomains ("Ledger", "Settlement & Reconciliation"), Airbnb has not described its current ledger design.
- **Agoda, Trip.com and Vrbo** payment models were not researched in this brief.
- **Paris and Amsterdam official rate pages** were not fetched (403 or not found); figures come from secondary sources.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Booking Holdings Inc. Form 10-K for FY2025 | Booking Holdings / SEC EDGAR | 2026 | https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm |
| Expedia Group Form 10-K for FY2025 | Expedia Group / SEC EDGAR | 2026 | https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm |
| Airbnb, Inc. Form 10-K for FY2025 | Airbnb / SEC EDGAR | 2026 | https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm |
| Directive (EU) 2015/2366 (PSD2) | European Parliament and Council, OJ L 337 | 2015 | http://publications.europa.eu/resource/celex/32015L2366 |
| Delegated Regulation (EU) 2018/389 (SCA RTS) | European Commission, OJ L 69 | 2018 | http://publications.europa.eu/resource/celex/32018R0389 |
| Regulation (EU) 2019/518 (cross-border charges, currency conversion) | European Parliament and Council, OJ L 91 | 2019 | http://publications.europa.eu/resource/celex/32019R0518 |
| Council Directive 2006/112/EC (VAT Directive, original text) | Council of the EU | 2006 | http://publications.europa.eu/resource/celex/32006L0112 |
| Council Directive 2008/8/EC (place of supply of services) | Council of the EU | 2008 | http://publications.europa.eu/resource/celex/32008L0008 |
| Council Directive (EU) 2025/516 (VAT in the digital age) | Council of the EU | 2025 | http://publications.europa.eu/resource/celex/32025L0516 |
| Council Directive (EU) 2021/514 (DAC7) | Council of the EU | 2021 | http://publications.europa.eu/resource/celex/32021L0514 |
| Judgment C-552/17 Alpenchalets Resorts | Court of Justice of the EU | 2018 | http://publications.europa.eu/resource/celex/62017CJ0552 |
| Introducing 'Reserve Now, Pay Later' (US) | Airbnb Newsroom | 2025 | https://news.airbnb.com/reserve-now-pay-later/ |
| Introducing 'Reserve Now, Pay Later', giving guests greater flexibility (APAC) | Airbnb Newsroom | 2026 | https://news.airbnb.com/introducing-reserve-now-pay-later-giving-guests-greater-flexibility/ |
| Airbnb Terms of Service | Airbnb | 2026 | https://www.airbnb.com/help/article/2908 |
| Payments Terms of Service (outside Europe, UK, Australia) | Airbnb | 2026 | https://www.airbnb.com/help/article/2909 |
| Payments Terms of Service for European Users | Airbnb | 2026 | https://www.airbnb.ie/help/article/2909 |
| When you'll get your payout | Airbnb Help Centre | undated | https://www.airbnb.com/help/article/425 |
| Areas where tax collection and remittance by Airbnb is available | Airbnb Help Centre | undated | https://www.airbnb.com/help/article/2509 |
| Scaling Airbnb's Payment Platform | Angela Zhu, Karen Kim / Airbnb Engineering | 2016 | https://medium.com/airbnb-engineering/scaling-airbnbs-payment-platform-43ebfc99b324 |
| Measuring Transactional Integrity in Airbnb's Distributed Payment Ecosystem | Airbnb Engineering | 2018 | https://medium.com/airbnb-engineering/measuring-transactional-integrity-in-airbnbs-distributed-payment-ecosystem-a670d6926d22 |
| Avoiding Double Payments in a Distributed Payments System | Airbnb Engineering | 2019 | https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb |
| Rebuilding Payment Orchestration at Airbnb | Bryon Ross et al. / Airbnb Engineering | 2022 | https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b |
| Pay as a Local | Gerum Haile et al. / Airbnb Engineering | 2026 | https://airbnb.tech/payments/pay-as-a-local/ |
| Skipper: Building Airbnb's embedded workflow engine | Ricardo Gamba, Andriy Sergiyenko / Airbnb Engineering | 2026 | https://airbnb.tech/infrastructure/skipper-building-airbnbs-embedded-workflow-engine/ |
| How Airbnb Rolled Out 20+ Local Payment Methods (summary, used for dating) | ByteByteGo | 2026 | https://blog.bytebytego.com/p/how-airbnb-rolled-out-20-local-payment |
| Booking.com Terms of Service | Booking.com | 2025 | https://www.booking.com/content/terms.html |
| Payments by Booking.com | Booking.com for Partners | undated | https://partner.booking.com/en-gb/solutions/payments-bookingcom |
| Understanding payouts (Payments by Booking onboarding API) | Booking.com Developers | undated | https://developers.booking.com/connectivity/docs/payments-by-booking-onboarding-api/understanding-payouts |
| Demand API: Booking.com collects payment | Booking.com Developers | undated | https://developers.booking.com/demand/docs/payments/models/booking-collects |
| Demand API: Partner collects payment | Booking.com Developers | undated | https://developers.booking.com/demand/docs/payments/models/partner-collects |
| Demand API: Pay at property | Booking.com Developers | undated | https://developers.booking.com/demand/docs/payments/models/pay-at-property |
| Understand how charges work in a Connect integration | Stripe | undated | https://docs.stripe.com/connect/charges |
| Strong Customer Authentication guide | Stripe | undated | https://stripe.com/guides/strong-customer-authentication |
| Marketplaces | Adyen Docs | undated | https://docs.adyen.com/marketplaces/ |
| IRS issues FAQs on Form 1099-K threshold (IR-2025-107) | Internal Revenue Service | 2025 | https://irs.gov/newsroom/irs-issues-faqs-on-form-1099-k-threshold-under-the-one-big-beautiful-bill-dollar-limit-reverts-to-20000 |
| One Big Beautiful Bill Act changes 1099 thresholds | CPA Practice Advisor | 2025 | https://cpapracticeadvisor.com/2025/07/30/one-big-beautiful-bill-act-changes-1099-thresholds/165863/ |
| Digital platforms will be liable to pay VAT on rentals and transport | Business.gov.nl (Netherlands government) | undated | https://business.gov.nl/amendment/vat-overnight-accommodation-goes-up/ |
| Verlaagd btw-tarief voor logies vervalt per 1 januari 2026 | Grant Thornton Netherlands | 2025 | https://www.grantthornton.nl/insights/tax/verlaagd-btw-tarief-voor-logies-vervalt-per-1-januari-2026/ |
| Informeer je gasten over de btw-verhoging in 2026 | KHN (Dutch hospitality association) | 2025 | https://www.khn.nl/nieuws/informeer-je-gasten-over-de-btw-verhoging-in-2026 |
| Amsterdam may raise tourist tax to curb mass tourism | NL Times | 2025 | https://nltimes.nl/2025/11/28/amsterdam-may-raise-tourist-tax-curb-mass-tourism |
| Amsterdam proposes tourism tax hike to 20% | Skift | 2026 | https://skift.com/2026/06/05/amsterdam-proposes-tourism-tax-hike-to-20/ |
| Tourist tax in France (vacation rental guide) | Hostaway | 2026 | https://www.hostaway.com/vacation-rental-guide/tourist-tax/france/ |
| Airbnb va collecter la taxe de séjour pour ses hôtes parisiens | Hospitality ON | 2015 | https://hospitality-on.com/fr/reglementation/airbnb-va-collecter-la-taxe-de-sejour-pour-ses-hotes-parisiens |
| Charge Expedia reservations in Lodgify | Lodgify Help Center | undated | https://help.lodgify.com/hc/en-us/articles/360016077759 |
| Experience seamless payments at your hotel with Expedia Virtual Card | Hotel Link Solutions | undated | https://blog.hotellinksolutions.com/experience-seamless-payments-at-your-hotel-with-expedia-virtual-card |
| Booking.com payment options | NightsBridge | undated | https://nightsbridge.screenstepslive.com/a/1722322-booking-com-payment-options |
