---
title: "Taking the Money: Payment Providers, Authorization, Capture and Refunds"
date: 2026-11-07
author: Željko Obrenović
excerpt: "How does money move from the shopper to the merchant, and what can go wrong on the way? Through a payment service provider, in four stages the merchant does not control, with the result arriving as a message that can be late, unordered or repeated; the order must treat that message as the truth, and every action that moves money must have one owner and one key."
permalink: commerce-payments
timetoread: 28 min read
icon: "assets/icons/12-payments.png"
logo: "assets/images/12-payments/logo.jpeg"
---

> **IN THIS CHAPTER, YOU WILL:** Follow Eva's €235 from her bank to Kestrel & Pine's account and learn why the order must treat the payment provider's answer as the truth and every refund as a one-owner action.

> **KEY POINTS:**
>
> * **Payment is a state machine whose truth lives outside your systems.** A payment moves between a few states by fixed steps, and the payment service provider, not the checkout, decides whether money moved, and its answer arrives by webhook: late, unordered and sometimes twice. The order keeps a small vocabulary (pending, authorized, paid, refunded, disputed) with the provider's references beside it, never a flag that says "paid: true".
> * **Money moves in four stages, and each payment method bends them differently.** Authorization reserves, capture takes, settlement moves money between banks, payout lands it in the merchant's account. A card authorization expires in days; iDEAL, the Dutch bank transfer, has no capture and no chargeback (a reversal forced by the shopper's bank); buy-now-pay-later, a short loan to the shopper, holds for weeks. A design that assumes one method's behavior breaks on the others.
> * **Every action that moves money has one writer and one key.** In the Double Refund, Kestrel & Pine sent €19,400 out a second time because two systems could refund the same return and neither sent a key the provider could recognize. Idempotency keys, a daily reconciliation against the provider's records and a card number that never touches your servers are the three disciplines this chapter is built on.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-commerce-platforms-go-wrong.html):**
>
> * **The Boomerang** — a refund issued from two systems for one return is reconciled by hand after the money has gone, and the second one cannot be pulled back.
> * **The Message in a Bottle** — a payment result sent once and trusted, or a refund request retried without a key, produces unpaid shipments and paid-twice customers.
> * **The Lynchpin** — one payment provider carries every online sale; when its account is paused for 40 minutes, the checkout is dark and nobody has rehearsed the switch.

<br>
A shopper approves a payment in a bank app and returns to the web shop. That return alone does not tell the merchant whether the money was reserved, collected or still pending. Payment providers and banks report those outcomes separately. The shop needs their confirmation to decide whether to release the order and avoid asking a customer to pay twice.

The shop cannot see this for itself because it does not move the money: the shopper's bank, the payment scheme (the card or bank network a method runs on) and the payment provider do, and the merchant only asks. So the merchant's failures come from acting on an outcome it did not see confirmed, or from moving money twice: a paid order left marked unpaid, a reservation that runs out before the money is collected, a refund sent by two systems. Checking unresolved payments against the provider's records makes these failures visible before they become customer complaints or unexplained gaps in the accounts.

**Where we are in the order's journey.** Eva buys a €199 jacket and two pairs of socks at Kestrel & Pine, the fictional outdoor brand. At 21:13 on 13 April 2027, checkout sends her to her bank's app to pay €235 through **iDEAL**, a Dutch bank-transfer payment method, and by 21:14 order #1072455 exists with its payment pending ([[cart-and-checkout]]). From here only the payment provider's message, the webhook, can say whether the money moved. Six days later she will exchange the jacket for size L; In Practice asks what a refund would have done instead.

The chapter starts with three weeks in January 2027 when Kestrel & Pine refunded 212 returns twice. It then explains what a payment service provider (PSP) does: the parties, the four stages and how methods differ by country. Next come the checks made before the money is reserved: customer authentication, fraud screening and keeping card numbers out of the merchant's systems. Then come the message that tells the order what happened and refunds and chargebacks as money flowing backward. The chapter compares four ways to take payments, adds the stores', wholesale and marketplace payout feeds, and places each setup on a scale stage. It ends with Eva's payment worked through and the ways payment integrations fail. The evidence is Kestrel & Pine's incidents, providers' documentation and EU payment law. [[tax-invoicing-and-ledger]] follows payments into the books; for deeper provider operations, see [[payments-fundamentals]], [[adyen]] and [[stripe]].

## Setting the Scene at Kestrel & Pine: Three Weeks in January

Kestrel & Pine's online **payment service provider (PSP)** offers iDEAL, cards, PayPal, Klarna (buy-now-pay-later), Bancontact (a Belgian card scheme) and Apple Pay. It collects payments through their banks and networks and pays the merchant a net daily amount. The six stores use a separate terminal provider. Wholesale customers pay invoices by bank transfer on 30-day terms. Finance must account for all three routes.

In January 2027, Finance Director Sanne de Wit found duplicate credits in the enterprise resource planning system (ERP), which keeps the books. **212 returns had been refunded twice** over three weeks: automatically through the returns portal and manually by support in the PSP console. **€19,400** had gone out a second time. This chapter calls it the Double Refund, Kestrel & Pine's case of the Boomerang.

Most of the money was recovered by asking customers to pay it back; the bank-transfer refunds could not be recalled. Head of Engineering Noor Visser reconstructed the ordinary sequence behind the incident, with illustrative day numbers.

| Day | What happened | Which system acted |
| --- | --- | --- |
| 0 | A returned parcel arrives at Duiven; the customer sees PostNL's "delivered" scan | The carrier |
| 0–3 | The customer writes to support: "my return arrived, where is my refund?" | The customer |
| 1 | The agent opens the PSP console, sees the payment and no refund, and refunds €199 to be helpful | Support, in the PSP console |
| 2–5 | The warehouse grades the item resellable; the returns portal, which refunds on inspection, calls the shop platform's API; the shop platform instructs the PSP, which accepts a request that names only the order and an amount | The returns portal, the platform, the PSP |
| 31 | Finance finds two credits per order when matching the PSP's payout report to the ERP | The ERP |

Two systems could refund, neither sent a key that named the business event (an **idempotency key**, which lets the provider recognize a repeat), and the only place the two paths meet is the ledger. Noor's whiteboard question in February is the chapter's: **who may move money, with what key, and how does the order find out what the PSP actually did?**

Kestrel & Pine's other payment incident, five months earlier, raises a second question, answered in the choices section and in the failures at the end: what happens when the one provider stops? On the Card-Testing Night of August 2026, bots fired **48,000** stolen card numbers at the guest checkout, costing **€2,900** in fees for declined authorizations and a **40-minute** pause of the PSP account, and of every online sale. [[commerce-security]] owns the defense; this chapter owns the fact that one provider carried every sale, the Lynchpin.

## What a Payment Service Provider Does

Finding out what the PSP did starts with who moves the money. When Eva pays, at least five parties take part.

| Party | In plain words | In Eva's iDEAL payment |
| --- | --- | --- |
| **The shopper** | Pays with a card, a bank account or a wallet | Eva, in her bank's app |
| **The issuer** | The shopper's bank, which holds her money or her credit | Eva's Dutch bank |
| **The scheme or network** | The rules and rails a method runs on: Visa, Mastercard, iDEAL, SEPA (the euro area's bank-transfer scheme), PayPal's own network | The iDEAL scheme |
| **The acquirer** | The licensed institution that accepts payments on the merchant's behalf and receives the money from the issuer | Part of the PSP |
| **The PSP** | The merchant's single counterparty: one API, many methods, fraud screening, authentication, a balance, payouts and reports | Kestrel & Pine's PSP |

A PSP hides the other four behind one contract. As a general pattern, not a fact about any one company, most PSPs serving European merchants are also acquirers or partner with one. The documentation of three PSPs, Adyen, Stripe and Mollie (all n.d., accessed November 2026), describes the same four-stage flow: **authorization, capture, settlement, payout**, with **refund** and **chargeback** flowing backward.

### The four stages

Each stage has a different actor and leaves something different in the order record, as Figure 1 and the table show: a reference and an expiry, a captured amount tied to a shipment, nothing for settlement, and a batch that finance matches.

![Diagram: Money moves in four stages the merchant does not control](assets/images/12-payments/fig01-money-moves-four-stages-merchant-does.jpeg)
**Figure 1:** *Money moves in four stages the merchant does not control; the order learns the result by webhook, triggers capture and refunds through one path, and finance matches the payout to the orders it contains.*

| Stage | Who acts | In plain words | What the order record keeps |
| --- | --- | --- | --- |
| **Authorization** | The issuer approves; the PSP reserves | "The money is there and held for you" | PSP reference, amount, method, authentication result, expiry |
| **Capture** | The merchant, or the PSP automatically | "Now take it"; Adyen: manual capture "lets you settle funds on fulfillment, when an order is shipped" | Captured amount, capture reference, link to the shipment |
| **Settlement** | The scheme or bank moves money to the PSP | The merchant's systems do nothing | Nothing |
| **Payout** | The PSP pays the merchant's bank | One batch per sales day, net of fees, refunds and chargebacks | Batch id, net amount, fees; matched by finance, not by the order system |

The windows matter. Stripe lists card authorizations as valid for seven days for Visa, Mastercard, American Express and Discover when the shopper initiates an online payment; if the authorization expires before capture "the funds are released and the payment status changes to canceled". Klarna, a buy-now-pay-later method, must be captured within 28 days at Stripe and Mollie. **"Capture on shipment" is a promise with a deadline**: if the warehouse ships on day eight, the card money is gone and the parcel is a gift. The only way to collect after the window is a **merchant-initiated transaction** (MIT): a charge the merchant triggers later, without the shopper present, under an earlier agreement. A split shipment captured late, a pre-order or a "charge on dispatch" depends on one, and it is allowed only if the shopper's first payment was authenticated (next section) and flagged for future use.

Payout timing is separate: Adyen's default is "sales day payout", all funds from one sales day in one batch with a two-business-day delay, and Stripe's initial settlement timing in most EU countries is seven calendar days, moving to three business days for later payouts. Either way, a payout does not equal one day's sales: it arrives days later and nets that day's payments against refunds and fees. The batch report, listing the payments, refunds, chargebacks and fees it nets, is what finance matches against orders ([[tax-invoicing-and-ledger]]; in depth, [[payments-to-ledger]]).

### Methods are not interchangeable

Kestrel & Pine sells in three countries, and each pays differently. Cards lead across the euro area, at 48% of online payments by number (the European Central Bank's SPACE 2024 study). In each of Kestrel & Pine's three countries, though, a different method leads, and only Belgium's works like a card. The figures are the latest dated public ones; the last column is the author's judgement.

| Country | Dominant online method | Evidence | What it means for the design |
| --- | --- | --- | --- |
| **Netherlands** | **iDEAL**, a transfer from the shopper's own bank account | Dutch Payments Association, February 2025: 1.47 billion iDEAL payments worth €141 billion in 2024; the ECB's SPACE 2024 study puts "e-payment solutions" at 76% of Dutch online payments by number | Instant and irrevocable, no separate capture, no chargeback, a 15-minute session; a refund is a new transfer back, partial refunds for 365 days. The scheme now brands itself "iDEAL \| Wero", moving under the European Payments Initiative's wallet; what that changes for integrations is undocumented, so these are Mollie's documented semantics (November 2026) |
| **Belgium** | **Bancontact**, a card scheme paid mostly through its app | Bancontact Payconiq Company, February 2025: 382 million online payments in 2024, 90% from a smartphone | Card-like: authorized then captured; refunds and disputes follow card rules |
| **Germany** | **PayPal**, **purchase on account** (*Kauf auf Rechnung*) and direct debit | EHI's "Online-Payment 2024" study as reported by Ecommerce News, April 2024 (data for 2023): PayPal 27.7%, invoice 26.7%, bank transfer 16.7% | "Payment" may be a 30-day receivable (an amount owed, collected later) or a buy-now-pay-later loan; the lender captures late and bears the credit risk |

Costs differ too. Adyen's indicative price list (n.d., accessed November 2026) quotes a processing fee in dollars plus a fee per method: "$0.13 + €0.22" for iDEAL, "$0.13 + Interchange++ + 0.60%" for Visa and Mastercard and "$0.13 + 2.99%" for Klarna in Germany. **Interchange**, the fee the merchant's side pays the cardholder's bank, is capped in the EU at 0.2% for consumer debit and 0.3% for consumer credit cards (Regulation (EU) 2015/751, in force since 9 December 2015), at most €0.30 on a €100 sale; Interchange++ means it and the card-scheme fees passed on at cost. As an illustration, on a €100 sale and taking $0.13 as about €0.12, iDEAL costs about €0.34 and Klarna about €3.11, some nine times as much: the method mix is a pricing decision before it is a technical one.

## Strong Customer Authentication and 3-D Secure

Before the issuer authorizes a payment, it often has to check who is paying. Payment authentication checks that the person paying is entitled to use the payment method. **Strong customer authentication (SCA)** combines independent checks, such as a password and possession of a phone. Checkout must allow that verification to finish before treating the payment as confirmed.

**PSD2**, the second Payment Services Directive (Directive (EU) 2015/2366, applied from 13 January 2018), defines SCA in Article 4(30) as authentication using two or more of knowledge, possession and inherence (something the payer knows, has or is), and Article 97 requires it when a payer initiates an electronic payment. The detailed rules are in Commission Delegated Regulation (EU) 2018/389, applied from **14 September 2019**, which sets the exemptions: contactless at the terminal up to €50 (Article 11), trusted beneficiaries (Article 13), recurring transactions after the first (Article 14), low-value remote payments up to €30 (Article 16) and transaction risk analysis up to €500 for PSPs with low fraud rates (Article 18).

For cards the protocol that performs SCA is **3-D Secure 2** (3DS): low-risk transactions pass "frictionless" and higher-risk ones require "a challenge, such as a one-time passcode" (EMVCo, n.d., accessed November 2026). Two rules follow from Stripe's SCA page. Exemptions belong to the PSP and the issuer, not the merchant: "Exemptions aren't guaranteed." And the **liability shift**: "If a cardholder disputes a 3DS payment as fraudulent, the liability typically shifts from you to the card issuer"; where an exemption was applied, "liability shift doesn't apply". An exemption buys conversion (more checkouts that end in a payment) at the price of fraud liability, so the order should store the authentication result, the liability flag and whether the payment was flagged for a later merchant-initiated charge.

## Fraud and Card Data: Keep the Attack Out and the Card Number Out

Besides authentication, two decisions act before the payment request leaves the shop: keeping attackers out and keeping card numbers out. [[commerce-security]] owns the layered defense and the sibling book LISTED covers fraud scoring in [[fraud-prevention]]; this chapter keeps to what shapes the payment design.

**Fraud screening before authorization.** The Card-Testing Night is the case. An attacker can automate payment attempts to discover which stolen card details still work. Screening and request limits help stop that traffic before it accumulates processing fees or triggers payment-provider restrictions. Stripe's card-testing guidance (n.d., accessed November 2026) describes spikes in failed payments, small amounts and implausible customer details. Its controls include risk models, rate limits, CAPTCHA challenges, login requirements and limits on attempts from one address. I would also provide a **kill switch**: a setting that pauses guest card payments or one method while keeping unaffected methods and customers trading.

**Card data is a scope decision.** **PCI DSS** (Payment Card Industry Data Security Standard) is the card industry's security standard for anyone who stores, processes or transmits card data; version 4.0.1 was published on 11 June 2024, and its future-dated requirements took effect on 31 March 2025. The merchant's obligations depend on which systems can see a card number, and the design goal is that none of the merchant's can.

The mechanism is **hosted fields**: the PSP draws the card-number box inside the merchant's page from its own domain, or redirects to its own page, so the number never touches the merchant's code or servers. Stripe's PCI guide maps the integration to the self-assessment questionnaire (SAQ) the merchant signs: hosted checkout or hosted fields to **SAQ A**, a merchant-hosted form posting via the PSP's script to **SAQ A-EP**, direct API with raw card data to **SAQ D**, where a business "might be required to meet more than 300 security controls". Adyen adds the boundary: "Adyen is solely responsible for the security of cardholder data only as soon as Adyen receives the data."

Hosted fields do not cover the rest of the payment page. SAQ A once had two requirements on the page's scripts; since 30 January 2025 the PCI Security Standards Council has replaced them with an eligibility statement that the site "is not susceptible to attacks from scripts", so every analytics, chat and testing script on the payment page remains the merchant's risk. The rule: **never store, log or transmit a card number; use the PSP's token, the reference it issues in place of the card number; keep a list of every script on the payment page.**

## The Order Depends on a Message It Does Not Control

Once the request has left, everything that happens to the payment happens outside the merchant's systems, which gives the rule the rest of the chapter builds on: **nothing in the merchant's own systems knows whether a payment succeeded.** The checkout sent a request. The shopper left for her bank's app or a 3-D Secure challenge and may never come back. The PSP learns the outcome from the issuer and tells the merchant by **webhook**: an HTTP call to an address the merchant registered, saying "something happened to payment X". The order's job is to wait for that message and to be safe when it arrives twice or not at all.

The documentation is blunt about that message. Stripe (n.d., accessed November 2026): "Stripe doesn't guarantee the delivery of events in the order that they're generated"; "Webhook endpoints might occasionally receive the same event more than once"; and every event is signed with a secret the merchant shares with Stripe, so the endpoint can check who sent it, because "Without verification, an attacker could send fake webhook events to your endpoint to trigger actions like fulfilling orders." Mollie's webhook carries only an id, so "fake calls to your webhook will never result in orders being processed without being actually paid"; the merchant must fetch the status; and Mollie retries ten times over 26 hours before giving up.

Three consequences follow, and I would write them into the integration contract of any order system:

1. **Persist every event id and treat a repeat as a no-op.** The second "payment succeeded" changes nothing; so does the second "refund succeeded".
2. **When the decision matters, fetch the object rather than trust the payload.** The webhook is the doorbell; the PSP's record is the truth.
3. **Run a daily job for everything still pending.** Webhooks stop retrying, after 26 hours at Mollie and three days at Stripe. A job that lists every order whose payment has not reached a final state within the method's expiry window, and asks the PSP, is the floor under the design. [[cart-and-checkout]] placed the same job at the end of checkout; [[events-consistency-and-reconciliation]] generalizes it.

![A doorbell labeled webhook rings at the shop, while a clerk confirms with the payment provider's record and a daily job checks pending orders.](assets/images/12-payments/12-webhook-is-the-doorbell.jpeg)
**Figure 2:** *The webhook is only the doorbell: the order trusts the PSP's record, ignores a repeated ring, and runs a daily job for every payment still pending.*


The order records each confirmed event in its **own small payment vocabulary**, a handful of states such as pending, authorized, paid, refunded and disputed, and translates the PSP's statuses (Mollie has seven, Stripe's PaymentIntent six) into it inside an adapter, the small piece of code that translates between the order and one PSP, so that a merchant that changes PSP changes an adapter, not every downstream system.

![Diagram: The order's payment vocabulary](assets/images/12-payments/fig02-order-s-payment-vocabulary-few-states.jpeg)
**Figure 3:** *The order's payment vocabulary: a few states every channel and system understands, moved only by the PSP's confirmed events, with the PSP's raw status and references stored beside them.*

The incoming message is one of four flows between the order and the PSP, each with its own requirements, previewed in the table; the latencies are assumptions for a merchant of Kestrel & Pine's shape.

| Flow | How fresh | How consistent | How fast | If the other side is down |
| --- | --- | --- | --- | --- |
| Payment outcome (webhook in) | As soon as the PSP knows | Applied once; duplicates ignored by event id | Seconds, but tolerate hours *(assumption)* | The daily pending-payments job settles it |
| Capture (out, on shipment) | Within the authorization window | One capture per fulfillment, keyed by it | Minutes *(assumption)* | Retry with the same key; alert before the window closes |
| Refund (out, on inspection) | Within the legal 14 days ([[returns-and-exchanges]]) | Exactly one per return, keyed by return id | Hours *(assumption)* | Retry only with the same key; check the PSP's refund list first |
| Payout report (in) | Daily batch | Every line matched to an order, refund, fee or dispute | A day | Finance waits; nothing else does |

## Refunds, Cancels and Chargebacks: Money Flowing Backward

Requests going out to the PSP need a key and a deadline, and the refund needs the most care: it must happen exactly once per return. A refund looks like an undo. It is not. **A refund is a new payment in the opposite direction**, with its own state, failure modes and fees.

- **You can only refund what was captured.** Adyen: "You can only refund a payment after it has been captured"; an uncaptured authorization is *canceled* instead. Stripe's cost advice points the same way: businesses that refund soon after the sale should capture manually and cancel before capture "rather than processing a refund", because "Stripe's processing fees from the original transaction aren't returned."
- **A refund is asynchronous and can fail later.** Adyen: a webhook with `success: true` means the request went to the scheme, and "Although rare, a refund can fail after you received" it; for iDEAL, Bancontact and bank transfers a REFUNDED_REVERSED event means the money came back because the account was invalid; funds can take "up to 40 business days" to reach the shopper. Stripe: the customer "sees the refund as a credit approximately 5-10 business days later".
- **Refunds go only to the original method, and partial refunds are bounded** (Stripe; Adyen). Store credit is a different instrument with its own ledger ([[commerce-promotions]]).

**Chargebacks** are the other backward flow, and not the merchant's decision: a dispute "occurs when a cardholder questions your payment with their card issuer"; the issuer "immediately reverses the payment", and the PSP "debits your balance for the payment amount and dispute fee" (Stripe). At Adyen a notification opens a defense period, then come the chargeback, the merchant's defense and a possible reversal, and Adyen auto-defends a dispute "that was already refunded". Cardholders "can dispute a charge up to 120 days after a payment was made", so a month's dispute ratio keeps changing for four months. The ratio has teeth: Visa's Acquirer Monitoring Program (fact sheet, May 2025) counts fraud reports plus disputes over settled transactions, with the excessive-merchant line lowered to 150 basis points (1.5%) on 1 April 2026. A slow refund path pushes customers to dispute instead, a second reason to get refunds right; iDEAL has no chargeback at all.

Refunds, unlike chargebacks, are the merchant's own to get right, and the Double Refund got them wrong. Figure 4 shows it as two refunds, two new payments for one return: how it happened, and where one key would have stopped the second.

![Diagram: The Double Refund](assets/images/12-payments/fig03-double-refund-two-writers-two-paths.jpeg)
**Figure 4:** *The Double Refund: two writers, two paths, no shared key; the PSP cannot refuse the second request because nothing in it says it is for the same return, and the two paths meet only in the ledger.*

The fix Waypoint adopted in February 2027, which [[events-consistency-and-reconciliation]] describes from the integration side, has three parts. **One writer per money action**: refunds are issued by the returns portal through the shop platform, and support's PSP console access becomes read-only. **One key**: every refund request carries the return id as its idempotency key, so a retry does nothing twice. Stripe's implementation is the public reference (it "saves the status code and body of the first request made with a given idempotency key" and returns it on retries, and may prune keys after 24 hours, so the merchant's own key store must outlive the PSP's). **One daily check**: refunds issued by the PSP against refunds recorded by the shop platform, by order number and amount, with exceptions to Sanne de Wit's team.

![Before and after: two desks refund the same parcel twice, versus one desk whose refund key makes the provider refuse the repeat.](assets/images/12-payments/12-one-writer-one-key.jpeg)
**Figure 5:** *The fix for the Double Refund: one writer per money action and one key per business event, so the PSP refuses a repeat instead of paying twice.*


## The Choices: Four Ways to Take Payments

With these pieces in place, a merchant can put them together in four ways. **1. The platform's built-in payments.** A hosted platform offers its own payment service, a wrapper over one or more PSPs, with a hosted checkout, automatic capture, refunds from the admin screen and payouts to the merchant's bank; Shopify Payments is the public example. Nothing to integrate, SAQ A, one payout feed. The limits: the method mix and fees are the platform's, and any second system that must move money goes through the platform's API or not at all.

Shopify Payments shows what lies under this option. Shopify's processor list (n.d., accessed November 2026) names Stripe, PayPal and Adyen as the processors behind Shopify Payments in the Netherlands, Belgium and Germany, and its European payment terms state that no Shopify entity is "licensed as a bank, payment institution, or money services business". "The platform's own payments" is a commercial wrapper over PSPs, and the four stages apply underneath.

**2. One external PSP through the platform's connector.** The merchant contracts with a PSP and uses its app or the platform's native integration; the PSP's hosted page or drop-in component (a ready-made payment form the PSP supplies) renders the methods. Kestrel & Pine's setup since 2016. The merchant gains the PSP's local methods, pricing and risk tools, and SAQ A if the page stays hosted; it must own the relationship, the webhook endpoint and the question of who else may call the PSP.

**3. A custom integration with hosted fields.** A headless checkout (one built apart from the platform's own pages) or a heavily customized one ([[storefront-architecture]]) calls the PSP's API directly and embeds its hosted fields: full control of capture on shipment, partial captures and MITs; SAQ A if the eligibility criteria hold; and a checkout team that handles every property of the webhook itself.

**4. A payment service of the merchant's own, over several PSPs.** An internal service presents one payment API to every channel, routes each payment to one of several PSPs and reconciles across them. [[payments-fundamentals]] covers the trade-offs; it is worth its complexity only when volume, countries or resilience demand it.

| Criterion | 1. Platform's own payments | 2. One PSP via connector | 3. Custom with hosted fields | 4. Own payment service, several PSPs |
| --- | --- | --- | --- | --- |
| Time to first sale | Hours | Days | Weeks to months | Months |
| Method mix and pricing | The platform's | The PSP's, negotiable at volume | The PSP's | Best per method and country |
| PCI scope | SAQ A | SAQ A | SAQ A or A-EP | SAQ A-EP to SAQ D |
| Capture on shipment, partial capture, MIT | What the platform exposes | Via the connector's settings | Full | Full |
| Who else may move money | The platform's API only | Whoever holds the PSP's API key | The payment adapter | The payment service, by policy |
| Resilience to a provider outage | None | None | None without a second PSP | Routing to another PSP |
| Fits | Starting; one country | Growing; Omnichannel with discipline | Omnichannel with a checkout team | Group, or very high volume |

The table shows that only option 4 keeps selling through a provider outage, and it is also the most to run; option 2's "None" is the connector on its own, before any fallback is added. My rule for a merchant of Kestrel & Pine's size: **stay on option 2 and spend the effort on discipline, not orchestration.** One PSP, local methods per country, capture on shipment for cards, one refund path, verified webhooks handled by an adapter, a daily reconciliation, and a rehearsed fallback for one method (a tested way to keep taking it if the PSP account is paused) rather than an orchestration layer (software that routes each payment across several PSPs) a 14-person team would have to run.

## Stores, Wholesale and Marketplaces: Four Feeds, Not One

Online is one of four ways money reaches Kestrel & Pine.

**Stores** take cards through the terminal provider, where SCA is chip-and-PIN or the contactless limit, the PCI questionnaire is a different one (SAQ C or a validated point-to-point encryption solution), and the payout is a separate daily feed into the ERP. A web order refunded at the till is the store's version of the Double Refund ([[stores-and-omnichannel]]).

**Wholesale** customers do not pay at checkout. Bergzicht's spring reorder was invoiced on 9 April 2027 and is due on 9 May: "payment" is a **receivable**, an amount owed and tracked in the ERP, settled by a bank transfer that finance matches to the invoice ([[b2b-commerce]], [[tax-invoicing-and-ledger]]).

**Marketplaces** collect the shopper's money and pay the seller out, net of fees, on their own schedule: a third payout feed ([[marketplaces-and-channel-integration]]).

**Online** is the PSP's daily batch. Four feeds, four reconciliations, and the reason Waypoint's W5, the integration standards, says finance moves by daily batch: the books need completeness, not speed. Where four feeds meet, a payments sub-ledger, a separate record of every payment, refund, fee and payout that the main ledger summarizes, earns its place ([[designing-financial-ledgers]]).

## Across Scale Stages: When It Fits and When It Limits

Set against the four scale stages, the options and feeds above show one pattern: the payment *mechanism* does not change with scale. What changes is **how many systems can move money and how many feeds finance must match**; the risk behind the Double Refund starts at stage 2, when the first integration beyond the platform gets a PSP key.

| Stage | What is typical | What becomes necessary | Signs the stage is ending |
| --- | --- | --- | --- |
| **1 — Starting** (under about €2M) | The platform's own payments or one PSP on a hosted page; automatic capture; refunds from the admin screen; one country's methods | Two-step authentication on the PSP and admin logins; someone who reads the decline rate | Refunds done by hand in the PSP console; a second country whose shoppers want a method the setup lacks |
| **2 — Growing** (about €2M–€20M) | One PSP with local methods per country; the first custom integrations (a returns portal, an ERP connector) that can call the PSP; card testing as the first incident | Capture on shipment for cards; one writer per money action; a webhook endpoint that is owned and verified; a rate limit at the edge of the site and a kill switch for guest card payments | Two systems can refund; an agency script handles webhooks and nobody knows how; a dispute lost for want of a stored 3DS result |
| **3 — Omnichannel** (about €20M–€200M) | Four feeds: online PSP, terminal provider, marketplaces and wholesale receivables; payment states on an order hub | The order hub's payment vocabulary and adapter; refund keys; a rehearsed PSP fallback; a payment-page script inventory; a payments sub-ledger | Payout matching takes days each month; a PSP account pause stops every channel; fee lines nobody can explain per country |
| **4 — Group** (over about €200M, or several brands) | Several PSPs or an orchestration layer; network tokens (card-scheme stand-ins for the card number that any PSP can use) so saved cards are not locked to one PSP; a central regulatory calendar | A payment service with routing and one reconciliation pipeline; a deliberate decision whether any system may touch card numbers | Each brand negotiating its own PSP contract; a tokenized card base that cannot move |

## In Practice

**Eva's €235, start to finish.** The shop platform requests an iDEAL payment at 21:13 on 13 April 2027. At 21:14 it creates order #1072455 with payment pending. Seconds later, the PSP's webhook confirms success and the order becomes paid ([[cart-and-checkout]]). iDEAL has no separate capture step or card chargeback.

With a card, the example would instead authorize on Tuesday and capture on Wednesday when the label prints, within the cited seven-day Visa window. The fulfillment order id would identify that capture so a retry could not collect it twice.

For the payout, assume a €0.30 fee and payment to Kestrel & Pine on Thursday 15 April, two business days later. These are illustrative assumptions, matching [[tax-invoicing-and-ledger]]. The batch includes that day's sales, less fees and earlier refunds. Sanne's team matches it to orders using the PSP reference.

**The refund variant.** Had Eva chosen a refund instead of size L on 19 April, the returns portal would have waited for the inspection on 22 April, then asked the shop platform to refund €199 with the return id as the key; the platform would have instructed the PSP; the PSP would have made a new iDEAL transfer back to Eva's account and reported it by webhook; the ERP would have booked a credit note, the document that reverses the invoice, against it ([[tax-invoicing-and-ledger]]). The refund is deducted from the payout batch for 22 April, which is why that payout does not equal the sales of 22 April, and why matching is by line, not by total. Support, since February 2027, could have seen all of this in the returns portal and issued nothing in the PSP console.

## When It Goes Wrong

**The duplicate refund.** Two systems, no key. Detection: a daily list of refunds at the PSP against refunds in the shop platform by order and amount. Recovery: ask for the money back, because bank transfers cannot be recalled, and block the writer. Prevention: one writer, the return id as idempotency key, read-only console access for everyone else.

**The lost outcome.** The shopper paid and never returned; the webhook failed; the PSP stopped retrying. Detection: the daily job for payments pending beyond their method's expiry (at Mollie, 15 minutes for an iDEAL session and 30 for a card checkout session, not the seven-day authorization). Recovery: query the PSP, settle the order either way. Prevention: a webhook endpoint that is owned and verified.

**The expired authorization.** The warehouse shipped on day eight and the capture failed. Detection: an alert when an authorized order approaches its window uncaptured. Recovery: only a merchant-initiated charge, where the first payment was set up for one. Prevention: capture at label print, and a fulfillment hold when the window is close.

**The provider outage or account pause.** The Card-Testing Night: 40 minutes with no online sales. Detection: a checkout health check that watches the PSP's error rate, not only its status page. Recovery: a rehearsed fallback for one method, a kill switch for the attacked method, an honest storefront message. Prevention: rate limits at the edge of the site and velocity rules (limits on attempts per card, address or device) before authorization, so the PSP never has to pause you.

## What to Take Away

The shopper of the opening returned from her bank app to a shop that could not tell whether her money had moved; the order should wait for the provider's confirmed message and ask about anything still pending each day. The 212 returns refunded twice had the same cause from the other side: two systems moved money the provider holds, and neither request named the return. The merchant only asks, so every action that moves money needs one writer and one key, and a daily comparison with the provider's records finds what slips through. Kestrel & Pine's fix kept the provider it had.

**Established.**

- Money moves in four stages, authorization, capture, settlement and payout, with refunds and chargebacks flowing backward; capture must happen inside an authorization window of days, and a refund is a new payment that can fail later (Adyen, Stripe and Mollie documentation, n.d., accessed November 2026).
- The payment outcome arrives by webhook, at least once, in no guaranteed order, and must be verified; the merchant persists event ids, fetches the object when the decision matters, and runs a daily job for everything still pending (Stripe and Mollie documentation).

**Depends on context.**

- Capture on shipment is right for cards where cancellations before dispatch are common, because it saves refund fees and ties money to goods; it does not exist for iDEAL and other instant methods, and it is a liability if the warehouse cannot ship inside the window.
- One PSP with disciplined integration is right up to the Omnichannel stage; orchestration across PSPs is right at Group scale or where one provider's outage would stop several brands, and it changes the PCI scope if the merchant's service ever sees a card number.

**Still moving.** The rules behind authentication, fraud and payment rails are changing, so the payment design needs someone who tracks them.

- **PSD3**, the third Payment Services Directive, and the Payment Services Regulation are agreed but not yet law. They reached provisional agreement on 27 November 2025 (PSPs liable for customers' losses where fraud prevention was inadequate, mandatory payee-name checks, all charges disclosed before payment, per the European Parliament's press release of that day); the Council published compromise texts on 23 April 2026, and both files were still open in its state of play of 29 October 2026. As of 7 November 2026 neither is in the Official Journal.
- The Instant Payments Regulation (Regulation (EU) 2024/886) is in force: euro-area PSPs had to receive instant credit transfers by 9 January 2025 and send them by 9 October 2025, with payee verification free of charge, which makes instant transfer a plausible checkout and refund rail.

**The author's synthesis.**

- I treat payments as a problem of writers and keys before a problem of providers: name one system that may refund, one that may capture, one that may create a payment, give each action a business key the PSP will remember, and reconcile daily; everything else about the PSP can be changed later.
- The order's payment vocabulary should be the merchant's, not the PSP's: five or six states, moved only by confirmed events, with the provider's raw status beside them, so that changing provider changes one adapter.

## Questions to Ask

1. Which systems hold a credential that can refund, capture or create a payment at the PSP, and who approved each one?
2. What is the idempotency key for a refund, a capture and a payment creation, and what does the PSP do when it sees the same key twice?
3. Where does the order store the PSP's reference, the authentication result and the liability-shift flag?
4. How long is the authorization window for each method, and what happens when a shipment approaches it uncaptured?
5. If the PSP's account is paused for an hour, what still sells, and who flips which switch?
6. How many payout feeds does finance match each month, by line or by total, and how long does it take?
7. Which regulatory changes (PSD3, 3-D Secure versions, PCI DSS) are on a calendar with an owner?

The money is in: the PSP's confirmed message has moved Eva's order to "paid" in the order's own payment vocabulary. Money is one of its three status lines; the jacket and socks still have to leave the warehouse, and the jacket will come back, on the goods and returns lines. Copies of the order sit in the shop platform, the warehouse and the carrier and, when Waypoint delivers it, in an order management system that holds every channel's orders in one record. [[order-management]] follows the order from "paid" onward and asks which of those systems is its home.

## Sources and Evidence

*Company, product and investor sources*

- [Capture](https://docs.adyen.com/online-payments/capture/), [Adjust authorisation](https://docs.adyen.com/online-payments/adjust-authorisation/), [Refund](https://docs.adyen.com/online-payments/refund/), [Sales day payout](https://docs.adyen.com/account/sales-day-payout.md), [Dispute process and flow](https://docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow), [Webhooks](https://docs.adyen.com/development-resources/webhooks/), [Batch-level reconciliation](https://docs.adyen.com/reporting/settlement-reconciliation/batch-level), [PCI DSS compliance guide](https://docs.adyen.com/development-resources/pci-dss-compliance-guide/) and [SAQ A eligibility](https://docs.adyen.com/development-resources/pci-dss-compliance-guide/saq-a-eligibility), Adyen documentation, n.d., accessed 2026-11 — authorization and capture semantics, expiry windows, asynchronous refunds, payout batches, dispute stages, the PCI responsibility boundary.
- [Pricing](https://www.adyen.com/pricing), Adyen, n.d., accessed 2026-11 — indicative per-method fees (volatile).
- [Place a hold on a payment method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method), [Refunds](https://docs.stripe.com/refunds), [Disputes](https://docs.stripe.com/disputes), [Measuring disputes](https://docs.stripe.com/disputes/measuring), [Monitoring programs](https://docs.stripe.com/disputes/monitoring-programs), [Strong Customer Authentication](https://docs.stripe.com/strong-customer-authentication), [CITs and MITs](https://docs.stripe.com/payments/cits-and-mits), [Idempotent requests](https://docs.stripe.com/api/idempotent_requests), [Webhooks](https://docs.stripe.com/webhooks), [Payouts](https://docs.stripe.com/payouts), [Payout reconciliation](https://docs.stripe.com/reports/payout-reconciliation), [Security guide](https://docs.stripe.com/security/guide), [Card testing](https://docs.stripe.com/disputes/prevention/card-testing) and [PCI compliance guide](https://stripe.com/guides/pci-compliance), Stripe documentation, n.d., accessed 2026-11 — authorization windows, refund behavior and fees, dispute mechanics and thresholds, SCA exemptions and liability shift, MITs, idempotency keys, webhook delivery, settlement timing, reconciliation reports, SAQ mapping, card-testing controls.
- [iDEAL](https://docs.mollie.com/docs/ideal.md), [Place a hold for a payment](https://docs.mollie.com/docs/place-a-hold-for-a-payment.md), [Refunds](https://docs.mollie.com/docs/refunds.md), [Webhooks](https://docs.mollie.com/docs/webhooks), [Handling payment status](https://docs.mollie.com/docs/handling-payment-status.md) and [Settlement report](https://docs.mollie.com/docs/settlement-report.md), Mollie documentation, n.d., accessed 2026-11 — iDEAL semantics, hold periods, duplicate-refund blocking, id-only webhooks with ten retries over 26 hours, status model and expiry per method, settlement contents.
- [Shopify Payments Terms of Service (Ireland)](https://www.shopify.com/legal/terms-payments-ie) and [Processor list](https://www.shopify.com/legal/processor-list), Shopify, n.d., accessed 2026-11; [Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm), Shopify Inc., 2026-02-11; [Shopify Payments supported countries](https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries), Shopify Help Center, n.d., accessed 2026-11 — a platform's payments as a wrapper over licensed PSPs; Payments penetration; country availability.
- [Annual turnover iDEAL and PIN payments](https://www.betaalvereniging.nl/en/news/annual-turnover-ideal-pin-payments/), Dutch Payments Association, 2025-02-18 — 2024 iDEAL volumes; [iDEAL | Wero](https://www.ideal.nl/en/), Currence iDEAL, n.d., accessed 2026-11 — the scheme's current branding.
- [2.5 billion payments with Bancontact and Payconiq in 2024](https://www.bancontact.com/en/news/2-5-billion-payments-with-bancontact-and-payconiq-in-2024-2-5-billion-times-thank-you-for-your-trust-in-us), Bancontact Payconiq Company, 2025-02-12 — Belgian online volumes.
- [PayPal remains most popular online payment method in Germany](https://ecommercenews.eu/paypal-remains-most-popular-online-payment-method-in-germany/), Ecommerce News reporting EHI's "Online-Payment 2024", 2024 — German method shares for 2023 (secondary source).

*Standards, regulation and official documentation*

- [Directive (EU) 2015/2366 (PSD2)](http://publications.europa.eu/resource/celex/32015L2366), Official Journal, 2015-12-23 — the SCA definition (Article 4(30)) and requirement (Article 97); applied from 13 January 2018.
- [Commission Delegated Regulation (EU) 2018/389](http://publications.europa.eu/resource/celex/32018R0389), Official Journal, 2018-03-13 — the RTS on SCA, applied from 14 September 2019, and its exemptions.
- [Regulation (EU) 2015/751 on interchange fees](http://publications.europa.eu/resource/celex/32015R0751), Official Journal, 2015-05-19 — the 0.2% and 0.3% caps (older than three years; still in force).
- [Regulation (EU) 2024/886 on instant credit transfers](http://publications.europa.eu/resource/celex/32024R0886), Official Journal, 2024-03-19 — receive and send deadlines, free payee verification.
- [Payment services deal: more protection from online fraud and hidden fees](https://www.europarl.europa.eu/news/en/press-room/20251121IPR31540/payment-services-deal-more-protection-from-online-fraud-and-hidden-fees), European Parliament, 2025-11-27, and [State of play of legislative files](https://data.consilium.europa.eu/doc/document/ST-15005-2026-INIT/en/pdf), Council of the EU, 2026-10-29 — PSD3 and PSR content and status.
- [EMV 3-D Secure](https://www.emvco.com/emv-technologies/3-d-secure/), EMVCo, n.d., accessed 2026-11 — frictionless and challenge flows.
- [Just published: PCI DSS v4.0.1](https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1), PCI Security Standards Council, 2024-06-11; [Important updates announced for merchants validating to SAQ A](https://blog.pcisecuritystandards.org/important-updates-announced-for-merchants-validating-to-self-assessment-questionnaire-a), PCI SSC, 2025-01-30; [PCI DSS](https://www.pcisecuritystandards.org/standards/pci-dss/), PCI SSC, n.d., accessed 2026-11 — versions, dates, scope, the SAQ A change.
- [Visa Acquirer Monitoring Program fact sheet](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf), Visa, 2025-05 — VAMP ratio and thresholds (volatile).
- [Study on the payment attitudes of consumers in the euro area (SPACE 2024)](https://www.ecb.europa.eu/stats/ecb_surveys/space/html/ecb.space2024~19d46f0f17.en.html), European Central Bank, 2024-12 — online payment shares by method and country.

*Research and practitioner sources*

- [[payments-fundamentals]], [[adyen]], [[stripe]], [[payments-to-ledger]], [[designing-financial-ledgers]] and [[traceability-and-reconciliation]] in RECONCILED — the deeper treatment of parties, pricing, orchestration, tokens, the payments sub-ledger and reconciliation this chapter points to.
- [[fraud-prevention]] in LISTED — scoring and velocity controls beyond the basics given here.

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
