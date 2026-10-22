{id: transactions-and-payments}
# 29. Beyond the Contact: Payments, Shipping and Buyer Protection

![Beyond the Contact: Payments, Shipping and Buyer Protection — logo](listing-systems-architecture/posts/29-transactions-and-payments/assets/images/29-transactions-and-payments/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn when a classifieds marketplace should take part in the transaction, and how to architect it when it does. You will follow two Tradeyard Safe Deal orders through their whole lives, compare the payment models that marketplace payment products offer, design the order, shipping and dispute contexts, and see which regulatory switches the decision turns on.

> **WHY THE BUSINESS CARES:** In-platform payment with buyer protection makes a marketplace safer, adds a transactional revenue line and makes sales observable for the first time. It also dilutes margin, adds payment, shipping and support costs, puts buyer-protection losses on the profit and loss statement and brings tax reporting with it. A general manager should know the full bill before the first checkout screen ships.

> **WHY ARCHITECTS SHOULD CARE:** A transactional pivot looks like a checkout to product teams and like a ledger, a dispute desk, a carrier integration and a tax report to everyone else. The order, not the listing, becomes the system of record for the sale. Getting its state machine, its money boundaries and its reconciliation right decides whether the pivot is a trust gain or an operational liability.

> **KEY POINTS:**
>
> * **The transactional pivot is a category decision, not a brand decision.** It works where items ship, prices are moderate and the buyer's main fear is non-delivery. leboncoin, Kleinanzeigen and Marktplaats added payments for goods, not for cars or homes; OLX scaled its pay-and-ship flow back. Gate it per country and category, in configuration, and design it to be switched off again.
> * **Let a licensed partner hold the money; own everything around it.** Most classifieds groups use a payment provider's marketplace product (Adyen, Stripe, Online Payment Platform), so the provider is the licensed party that holds funds and verifies payees. The marketplace still owns the order state machine, fee pricing, shipping, release rules, disputes, buyer-protection losses, reconciliation and DAC7 reporting.
> * **Buyer protection is a liability with a product attached.** It converts unrecoverable scams into mediated disputes, which is its main value, but it needs evidence-based release rules, a case-management desk, a loss provision and a ledger that can explain every payout. Ship those with the checkout, or the pivot produces unreconciled money and disputes handled by e-mail.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Fast Mail for Fraudsters** — Off-platform payment is where classifieds fraud lands, and a protected-payment brand becomes the scammers' favorite disguise, as the fake Safe Deal link sent to Femke shows.
> * **Ghost Inventory** — An item sold through an order but still searchable, alertable or payable lets a second buyer pay for something that is gone, so the order must own the listing's availability.
> * **The Forced Fit** — A checkout designed for shippable goods and imposed on car dealers or property agencies fits none of their workflows, and the professionals route around it.

For twenty years, the classifieds bargain was simple: the platform finds the buyer, and the buyer and seller sort out the money themselves. That bargain kept classifieds cheap to run and free of payment regulation. It also left the most dangerous moment of the transaction, **the moment money changes hands, entirely outside the platform's control**, which is why advance-payment scams and fake payment links became the industry's characteristic fraud ([Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)).

From about 2017 the large European horizontals began to move into that moment for some categories. They added in-platform payment, shipping labels and buyer protection, so that a buyer in Utrecht can pay a seller in Groningen for a phone without either of them trusting the other. This chapter owns three terms: the **transactional pivot** (adding payment, delivery and protection to a classifieds marketplace), **marketplace payments** (the payment architecture in which a platform collects from buyers and pays out to many sellers) and **buyer protection** (the platform's promise to refund the buyer when a covered problem occurs).

This chapter starts where [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) ends: with an offer accepted in chat, which the marketplace can leave to the parties or carry through payment and delivery. The question is architectural and strategic: **when should a listing marketplace take part in the transaction, and which systems does it then have to own?** The answer becomes the transactional revenue line that [How Listing Marketplaces Make Money](#monetization-models) compares with the other ways a marketplace earns. The chapter does not re-teach payments. The sibling book RECONCILED covers the payment lifecycle in [Payments for Finance Architects: Eleven Reasons the Numbers Disagree](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-fundamentals.html), the two main providers in [Adyen: One Platform from Checkout to Settlement](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/adyen.html) and [Stripe: Every Movement Is a Balance Transaction](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/stripe.html), and the reconciliation design in [Payments-to-Ledger: Draining the Suspense Swamp](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-to-ledger.html) and [Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html).

{id: transactions-and-payments--setting-the-scene-at-veldmark-three-proposals-and-a-clearing-account}
## Setting the Scene at Veldmark: Three Proposals and a Clearing Account

On Wednesday 22 September 2027, the architecture advice forum of Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), had three transaction proposals on its agenda, and Ingrid Halvorsen, the Group Chief Architect, had asked for them to be heard together.

**Tradeyard Safe Deal** was the reason they existed. Launched in the Netherlands in 2024, Belgium in 2025 and Poland in 2026, it lets private buyers pay in the app and either receive the item by parcel or collect it with "pay at pickup". Payments run on Adyen for Platforms, and Adyen, not Veldmark, is the licensed party. In 2026 Safe Deal processed **11.6 million** orders worth about **€1.02 billion** of gross merchandise value (GMV) and earned **€75 million**: about €59 million of buyer protection fees at **5% of the item price plus €0.70**, and about €16 million of margin on shipping labels. It was Tradeyard's third revenue line, behind visibility products and professional subscriptions.

The three proposals all wanted more of it:

1. **Tradeyard Portugal** (Daan Visser, Tradeyard engineering director): launch Safe Deal in Portugal, the one Tradeyard country without it. The liquidity analysis in [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) had shown that shipping widens a goods market from a district to the whole country.
2. **Motorvane** (Felix Brandt, Motorvane CTO): a "secure payment" for private-to-private car sales in Germany, where buyers and sellers meet strangers with tens of thousands of euros at stake.
3. **Hearthly Spain** (Julien Marchand, Hearthly CTO): a protected rental deposit. In July 2027, a ring of **26** accounts had posted **180** fake rental listings in Barcelona and collected about **€71,000** from **63** people as deposits paid by bank transfer outside the platform ([Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) tells that story).

Ingrid added a fourth item, which nobody had proposed. At the December 2026 month-end, Veldmark's group finance team had found about **€2.3 million** of Safe Deal items in a clearing account that could not be matched to orders: refunds issued after payouts, label charges netted from settlements, partial refunds agreed in chat. The amount was a fraction of GMV, but nobody could say what it consisted of without a week of spreadsheet work. Her point to the forum was that **Safe Deal had shipped its checkout before it had shipped its ledger**, and that every proposal on the agenda would make that worse unless the transaction platform was designed properly first.

The rest of this chapter is the framework the forum used to decide.

{id: transactions-and-payments--concepts-what-changes-when-the-platform-takes-part-in-the-sale}
## Concepts: What Changes When the Platform Takes Part in the Sale

A classifieds marketplace's job ends at the contact ([Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy)). A transactional marketplace's job ends when payment and delivery are complete. The transactional pivot moves a category from the first to the second, and brings terms the classifieds side of the organization has usually never needed.

- **Order**: the record of an agreed sale between a buyer and a seller for a listing, with a price, fees, a fulfilment method and a state. It is created when the buyer commits, not when the listing is published.
- **Marketplace payments**: a payment model in which the platform collects one payment from a buyer and pays out to the seller, net of the platform's fees, often after holding the funds for a period. In the EU, the platform either holds a payment licence itself or uses a licensed provider whose marketplace product does the collecting, holding and paying out.
- **Payment service provider (PSP)**: a licensed company that processes payments for merchants; its **marketplace product** (Adyen for Platforms, Stripe Connect, Online Payment Platform) adds seller onboarding, split payments, held balances and payouts.
- **Payee verification (KYC)**: the identity and account checks a licensed provider must run before paying money to someone. For private sellers it is light; for businesses it is know-your-business (KYB). [Who Is on the Other Side? Identity and Verification](#identity-and-verification) owns the levels.
- **Hold and release**: keeping the buyer's payment in a held balance until a release event (buyer confirmation, a delivery scan plus a waiting period, a handover code), then making it available for payout. This is often called "escrow" informally; legally it is usually not an escrow arrangement, which is why the provider's terms, not the marketing name, define it.
- **Payout**: the transfer of released funds from the seller's balance to their bank account.
- **Merchant of record**: the party whose name is on the buyer's payment statement and which carries the payment-side obligations, refunds and chargebacks ([Payments for Finance Architects: Eleven Reasons the Numbers Disagree](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-fundamentals.html) defines it fully).
- **Buyer protection**: the platform's contractual promise to refund the buyer if a covered problem occurs, such as non-delivery, an item significantly not as described, a counterfeit, a wrong or incomplete item. Covered cases, evidence rules and time windows are product decisions with financial consequences.
- **Dispute** versus **chargeback**: a dispute is opened with the platform under its buyer protection; a chargeback is opened by the buyer's card issuer under card-scheme rules. Both can occur for the same order, and they follow different clocks.
- **Pick-up and drop-off point (PUDO)**: a shop or locker where parcels are handed in and collected; the default shipping method for low-value consumer parcels in much of Europe.

**Holding the money and taking the risk are separate**: the PSP holds the funds, but a buyer-protection refund that the seller cannot cover is paid by the marketplace. And **the order is a separate aggregate from the listing**: a listing can have many conversations and, for multi-quantity sellers, many orders; an order belongs to one buyer, one seller and one agreed price. [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) keeps availability on the listing and leaves everything about money to the order.

{id: transactions-and-payments--when-to-take-part-in-the-transaction}
## When to Take Part in the Transaction

The documented record suggests that the pivot pays where four conditions hold together.

| Condition | Why it matters | Strong fit | Weak fit |
| --- | --- | --- | --- |
| **The item ships** | Shipping widens the market and creates the delivery event that protection is built on | Phones, clothes, books, small electronics, toys | Sofas, bikes in some markets, cars, homes |
| **The price is moderate** | A percentage fee is acceptable; losses per dispute are bounded; payment methods have no limits | Roughly tens to a few hundred euros | Tens of thousands of euros, where a percentage fee is absurd and a single loss is large |
| **The buyer's main fear is non-delivery or misdescription** | Buyer protection answers exactly that fear | Distance purchases between private people | Professional sellers with their own guarantees and legal duties |
| **The sale is otherwise completed between strangers** | The platform adds trust that does not already exist | C2C goods | Dealer and agency sales, which already have contracts, invoices and showrooms |

**Category gating is what the European horizontals did.** leboncoin "launched a transactional business model in some of the generalist categories" in 2019, according to Adevinta's 2019 annual report. Marktplaats launched transactional services in 2017, shipping in 2019 and buyer protection after that. eBay Kleinanzeigen launched "Sicher bezahlen" for all users in October 2020, initially only for toys, phones, and PCs and notebooks ([onlinemarketing.de, 2020](https://onlinemarketing.de/?p=214785)). mobile.de, in the same group, earned essentially no transactional revenue in 2023 (Adevinta Annual Report 2023, published 2024).

**The economics are documented too.** Adevinta's transactional revenue reached **€103 million** in 2023, about 6% of group revenue, and in France the EBITDA margin fell two points "mainly reflecting the evolution of the business mix with an increasing share of transaction services". The same report notes rising "direct costs from transactional services (such as payment and shipping service provider costs)" ([Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf)). OLX described its Pay&Ship flow in 2023, "OLX holds the money of the transaction and transfers it to the seller when the package is delivered", and Prosus then recorded "the de-prioritisation of pay-and-ship in Europe" in the second half of the year to March 2025, while OLX concentrated on motors, real estate and jobs ([OLX Tech, 2023](https://tech.olx.com/machine-learning-for-delivery-time-estimation-1-591c8df849a0); Prosus FY25 results, 2025).

**The trust case is the strongest argument.** In a December 2024 investigation, the UK consumer organization Which? found that eBay, Vinted, Depop, Shpock, Preloved and Amazon Marketplace offered some buyer protection while Facebook Marketplace, Gumtree and Nextdoor did not, and that a quarter of Facebook Marketplace and Gumtree buyers believed theirs did ([Which?, 2024](https://www.which.co.uk/policy-and-insight/article/scam-ads-slipping-through-the-net-too-easily-on-second-hand-marketplaces-which-warns-aqyF66m1TlU1)). In-platform payment turns an authorized push-payment fraud, which the victim may never recover, into a dispute the platform can resolve. That is why it belongs as much to [Trust and Safety as a Platform](#trust-and-safety-architecture) as to monetization.

My rule of thumb: **take part in the transaction where the platform's presence removes a fear that stops sales, and stay out where professionals already carry that fear for the buyer.**

![A four-layer sieve that lets small shippable goods through to protected payment while cars and homes are diverted to contact only.](listing-systems-architecture/posts/29-transactions-and-payments/assets/images/29-transactions-and-payments/four-condition-sieve.jpeg)

**Figure 1:** *The transactional pivot is a per-category decision: it pays where the item ships, the price is moderate, the buyer fears non-delivery and the sale is otherwise between strangers, and it stays out where those conditions fail.*

{id: transactions-and-payments--payment-models-who-holds-the-money}
## Payment Models: Who Holds the Money

A marketplace that wants to collect from buyers and pay sellers in the EU has three basic options. In practice, classifieds groups have used the first.

{id: transactions-and-payments--use-a-licensed-provider-s-marketplace-product}
### Use a licensed provider's marketplace product

The provider is the licensed payment institution or e-money institution. It onboards and verifies sellers, collects the buyer's payment, keeps funds in held balances, splits fees and pays out. Adyen describes its platform product as letting a platform "onboard users of your platform, process payments for them, and pay out their funds", with Adyen verifying users before payouts, the option to "split the payments between one or more users, deduct costs as needed, and hold funds until payout", and payouts on a schedule the platform controls ([Adyen documentation, n.d.](https://docs.adyen.com/marketplaces/)). Stripe Connect offers three charge types with different money flows: **direct charges** on the seller's connected account, **destination charges** on the platform's account with an immediate transfer to the seller, and **separate charges and transfers**, which let the platform charge first and transfer later or to several sellers. For destination charges and separate charges and transfers, "refunds and chargebacks reduce your platform's balance", and the platform must recover them from the seller by reversing the transfer ([Stripe documentation, n.d.](https://docs.stripe.com/connect/charges)). [Stripe: Every Movement Is a Balance Transaction](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/stripe.html) and [Adyen: One Platform from Checkout to Settlement](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/adyen.html) in the sibling book describe both products in depth.

Specialist marketplace providers serve the same need. Online Payment Platform, a Dutch payment institution, carried Marktplaats' first escrow-style flow in 2017 and eBay Kleinanzeigen's in 2020; Worldline's 2022 announcement of a 40% stake named Marktplaats, eBay Kleinanzeigen and Gumtree among its clients ([Worldline, 2022](https://worldline.com/de-at/home/top-navigation/media-relations/press-release/pr-2022_09_09_01); [t3n, 2023](https://t3n.de/news/?p=1565510)). Kleinanzeigen's own help page named "unserem Zahlungsdienstleister Adyen" when consulted in October 2026 ([Kleinanzeigen, n.d.](https://themen.kleinanzeigen.de/sicher-bezahlen/)); when and why the provider changed is not public. leboncoin has acted as a trusted third party for consumer-goods transactions since 2018 with Adyen as its payment partner (Wikipedia, leboncoin, 2026, widely reported).

{id: transactions-and-payments--hold-a-licence-yourself}
### Hold a licence yourself

A marketplace can become an e-money or payment institution and hold users' funds itself. Vinted Pay holds an e-money licence from the Bank of Lithuania (2023) and began moving members onto its own wallet in January 2026, "expected to reduce payment-related costs and dependencies", while continuing to work with other providers ([Vinted, 2026](https://company.vinted.com/newsroom/vinted-pay)). A licence brings safeguarding of client funds, capital requirements, supervision and a double-entry ledger the marketplace must run itself ([Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html)). It makes sense when payment volume is large, payments are the core of the product and the group wants to own the economics; for a classifieds group whose transactions are a minority of revenue, it rarely does.

{id: transactions-and-payments--stay-out-of-the-flow-of-funds}
### Stay out of the flow of funds

The marketplace can avoid payments entirely and rely on contact plus safety advice, or pass buyers to an external payment option. This keeps it out of payment regulation and DAC7, at the cost of the trust and observability gains.

> **Why "we just collect and pass it on" does not work.** The EU's Second Payment Services Directive excludes payment transactions made "through a commercial agent authorised via an agreement" to negotiate or conclude the sale on behalf of only the payer or only the payee ([Directive (EU) 2015/2366, Art. 3(b)](https://eur-lex.europa.eu/eli/dir/2015/2366/oj)). A marketplace that collects money on behalf of both buyers and sellers does not fit that exclusion, which is the practical reason most marketplaces use a licensed provider. The precise legal position depends on the contracts and the jurisdiction; treat this as a question for counsel, not a design default.

{id: transactions-and-payments--comparing-the-models}
### Comparing the models

| Model | Who holds funds | Who verifies payees | Who carries chargebacks and refunds first | Marketplace owns | Fits |
| --- | --- | --- | --- | --- | --- |
| Provider marketplace product, platform as merchant (Adyen for Platforms, Stripe destination or separate charges) | The provider, in the platform's or sellers' held balances | The provider | The platform's balance; recovery from the seller by debit or transfer reversal | Order, fees, release rules, disputes, losses, reconciliation | C2C goods at scale; one brand on the statement |
| Provider marketplace product, seller as merchant (Stripe direct charges, on-behalf-of models) | The provider, in the seller's account | The provider | The seller's balance | Order, fees; less of the risk | Professional sellers with their own customer relationship |
| Specialist marketplace payment institution (OPP) | The institution, in intermediary accounts | The institution | Contract-dependent | Order, fees, disputes in cooperation with the institution | Mid-size marketplaces wanting a turnkey escrow flow |
| Own licence (Vinted Pay) | The marketplace, in safeguarded accounts | The marketplace | The marketplace | Everything, including safeguarding and the ledger | Transaction-first marketplaces at very large volume |
| Off-platform | The parties | Nobody | The victim | Safety advice only | Lead-generation and high-value categories |

Veldmark chose the first row. [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) records the consequence: the Safe Deal context **conforms** to Adyen's model of accounts, balances and payouts and translates only at its edge, where an order meets a listing.

{id: transactions-and-payments--architecture-the-transaction-platform}
## Architecture: The Transaction Platform

A transactional pivot adds six bounded contexts beside the listing core. None of them belongs inside the listing service.

| Context | Owns | Key events | Must not own |
| --- | --- | --- | --- |
| **Order** | The agreed sale: parties, listing, price, fees, fulfilment method, state, timers | `OrderPlaced`, `OrderPaid`, `OrderShipped`, `OrderDelivered`, `OrderCompleted`, `OrderCancelled` | Listing content; money balances |
| **Payment edge** | The translation between orders and the provider: payment sessions, captures, refunds, account holders, payout status | `PaymentAuthorized`, `PaymentCaptured`, `RefundIssued`, `PayoutSettled` | Business rules about when to release |
| **Fees and pricing** | Buyer fee, seller fee, shipping prices, promotions, rounding, VAT treatment of fees | `FeeQuoted`, `FeeCharged` | Visibility products ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)) |
| **Shipping** | Carrier contracts, label purchase, PUDO selection, tracking events, address validation | `LabelCreated`, `ParcelHandedIn`, `ParcelDelivered`, `ParcelReturned` | The release decision |
| **Buyer protection and disputes** | Coverage rules, dispute cases, evidence, decisions, refunds funded by the platform, loss provision | `DisputeOpened`, `DisputeDecided`, `ProtectionPaid` | Account sanctions ([Trust and Safety as a Platform](#trust-and-safety-architecture)) |
| **Transaction ledger and reporting** | The double-entry record of every amount owed and moved; reconciliation with provider reports; per-seller aggregates for tax | `JournalPosted`, `ReconciliationBreak`, `SellerPeriodAggregated` | Payment execution |

![Diagram: The transaction platform beside the listing core](listing-systems-architecture/posts/29-transactions-and-payments/assets/images/29-transactions-and-payments/fig02-transaction-platform-beside-listing-core-order.jpeg)

**Figure 2:** *The transaction platform beside the listing core. The order context owns the sale and its timers; the payment edge translates to the licensed provider; shipping and disputes feed the order's release decision; the ledger receives both order and money events, so finance and tax reporting are built from the same record.*

{id: transactions-and-payments--the-order-owns-availability}
### The order owns availability

The most common integration bug in a transactional pivot is the double sale: two buyers pay for the same one-off item because the listing still looked available. The order context must therefore **reserve the listing atomically when payment is committed**, and the listing must treat a reservation from an order as authoritative. At Tradeyard, a Safe Deal order emits `ListingReserved` on the listing event stream and the listing transitions to reserved; search shows a badge and alerts stop notifying ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)). A reservation needs a timeout: an order that is never paid, never shipped or never collected must release the listing again, or the reservation becomes Ghost Inventory in reverse, a sellable item nobody can buy.

When the order completes, the listing becomes sold through the same stream, and every copy of the listing must react: search, saved-search alerts, digests, recommendations and sitemaps ([Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts), [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline)). Femke's bike is the canonical warning. It sold through Safe Deal at 18:10 on Monday 8 March 2027 and was gone from search a minute later, but the next morning's alert digest, assembled from an older snapshot, still featured it to **214** users.

{id: transactions-and-payments--the-order-state-machine}
### The order state machine

![Diagram: A protected-payment order for goods](listing-systems-architecture/posts/29-transactions-and-payments/assets/images/29-transactions-and-payments/fig03-protected-payment-order-goods-every-waiting.jpeg)

**Figure 3:** *A protected-payment order for goods. Every waiting state has a deadline, every exit to cancellation or refund returns money and releases the listing, and a completed order can still be reopened by a card chargeback weeks later, which is why the ledger must handle states after payout.*

Four design rules follow from the diagram.

1. **Every waiting state has a timer and an owner.** Unshipped orders, uncollected pickups and silent buyers are the normal case, not the exception. Kleinanzeigen documents one such rule: if the buyer does not confirm receipt, "wird der Betrag nach 14 Tagen automatisch an den Verkäufer überwiesen" (the amount is paid to the seller automatically after 14 days) ([Kleinanzeigen, n.d.](https://themen.kleinanzeigen.de/sicher-bezahlen/)). Marktplaats' successor to its first escrow product, as described in 2022, paid the seller on day 8 if there were no complaints ([AVROTROS Radar, 2022](https://radar.avrotros.nl/artikel/dit-is-de-vervanger-voor-de-gelijk-oversteken-functie-van-marktplaats-52677)).
2. **Release is a decision, not a side effect.** The order context decides when funds become payable, using the delivery event, the dispute window, the buyer's confirmation and the risk score. The payment edge only executes. A fraud rule must be able to hold a payout, and that hold is itself a restricting decision that needs a statement of reasons under the Digital Services Act ([Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)).
3. **Money states and order states are reconciled, not assumed equal.** "Paid" in the order means the provider confirmed capture; it does not mean cash has arrived. Provider webhooks arrive asynchronously, at least once and out of order ([Adyen: One Platform from Checkout to Settlement](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/adyen.html)), so the payment edge must be idempotent and the ledger must match order events to provider records.
4. **States after completion are first-class.** Chargebacks, late refunds and returned parcels arrive after the seller has been paid. The design needs a policy for recovering money from sellers (debit their balance, net against future payouts, absorb it) and a ledger that records each case.

{id: transactions-and-payments--shipping-as-an-integration-surface}
### Shipping as an integration surface

Shipping turns a marketplace into a logistics integrator. Kleinanzeigen's protected-payment flow offers DHL parcels in four sizes and Hermes in four (a small packet and three parcel sizes), handed in at shops, lockers or to the carrier ([Kleinanzeigen, n.d.](https://themen.kleinanzeigen.de/sicher-bezahlen/)). Vinted reports more than **500,000** pick-up and drop-off points across Europe and runs its own carrier, Vinted Go, in five countries ([Vinted, 2026](https://company.vinted.com/newsroom/financial-results-2025)). Adevinta's 2025 report discusses shipment-driven emissions for five of its marketplaces, a reminder that shipping volume is now material enough to appear in sustainability reporting (Adevinta Strategic Report 2025, published 2026).

The shipping context needs one adapter per carrier, a normalized tracking-event model (handed in, in transit, at PUDO, delivered, returned, lost), label pricing by size and route, address validation and a policy for lost parcels. Tracking events are the evidence that buyer protection rests on, so their timeliness is a reliability requirement: a delivery scan that arrives a day late delays a payout by a day.

Shipping also changes discovery. An item that ships nationwide is no longer constrained by a radius search; distance becomes a delivery-cost input rather than a filter ([Where Is It? Location, Geocoding and Privacy](#location-and-geo)), and the price a buyer sees in search may need to include the fee and shipping. Vinted's price list describes its buyer-paid fee as varying with "item characteristics, order value, order type" ([Vinted UK price list, updated October 2026](https://www.vinted.co.uk/pricelist)), and a fee that varies per item has to be computed on the search and listing read path, not only at checkout.

{id: transactions-and-payments--buyer-protection-and-dispute-management}
### Buyer protection and dispute management

A dispute desk is a case-management system with money attached. Kleinanzeigen's coverage, as published in 2026, lists five cases: item not shipped, significantly different from the description, not authentic, a different item, incomplete ([Kleinanzeigen, n.d.](https://themen.kleinanzeigen.de/sicher-bezahlen/)). Adevinta built a dispute-management back office as a reusable component "that can be plugged into any marketplace", which ingested per-marketplace transaction events through Kafka, SQS or REST and normalized them into a common model; its designers noted, "We couldn't hardcode anything… or make any assumptions" ([Adevinta tech blog, 2023](https://adevinta.com/techblog/from-hello-world-to-a-dispute-management-back-office/)). That is the right shape for a shared capability across brands: an anti-corruption layer per marketplace and a canonical case model.

A protection promise is also a liability that must be provisioned, measured per category and priced into the fee. eBay's 2025 annual report describes its transaction losses as consisting "primarily of losses resulting from our buyer protection programs, chargebacks" ([eBay Form 10-K for 2025, filed 2026](https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm)).

{id: transactions-and-payments--reconciliation-and-the-ledger}
### Reconciliation and the ledger

Every amount in an order has to be explainable later: what the buyer paid, which part was the item, the fee and the label, what the provider charged, what was refunded, what was paid out and when, and what the platform absorbed. Provider settlement reports are net and batched, use the provider's vocabulary and arrive after the order events. RECONCILED's [Payments-to-Ledger: Draining the Suspense Swamp](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-to-ledger.html) designs the normalization layer, clearing accounts and three-way match between commerce events, provider records and bank movements; [Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html) designs the ledger itself. A marketplace adds two requirements on top: **per-seller balances**, because payouts are owed to many parties, and **per-seller, per-period aggregates**, because tax reporting is computed from them.

{id: transactions-and-payments--the-regulatory-switches}
### The regulatory switches

Moving money on-platform turns on obligations that a classifieds site largely avoids.

- **DAC7 seller reporting.** EU platform operators must collect, verify and report seller identity, financial account identifiers and the total consideration per quarter for sellers of goods above the excluded-seller test: fewer than 30 sales and no more than €2,000 of consideration in the period are excluded ([Belastingdienst, n.d.](https://belastingdienst.nl/wps/wcm/connect/en/business/content/information-for-platform-operators-dac7)). A lead-only site largely falls outside DAC7; in-platform payment makes the consideration known. **The decision to launch payments is also a tax-reporting decision**, and the ledger should aggregate per seller, per quarter and per Member State from the first day. [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) owns the detail.
- **Consumer and platform law.** A platform that lets consumers conclude distance contracts with traders takes on trader-traceability duties under the Digital Services Act and information duties under EU consumer law ([Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation), [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts)). Professional sellers using a protected-payment flow must be identified as traders.
- **Payment regulation**, through the provider. The provider's onboarding, limits and monitoring become constraints on the product: which sellers can be paid, how much and how fast.

{id: transactions-and-payments--in-practice-two-safe-deal-orders}
## In Practice: Two Safe Deal Orders

{id: transactions-and-payments--the-rotterdam-city-bike-pay-at-pickup}
### The Rotterdam city bike: pay at pickup

Femke listed her city bike on Tradeyard Netherlands for **€240** on Sunday 7 March 2027 at 19:42. Early on Monday afternoon she agreed **€225** with a buyer in chat. The order shows how "pay at pickup" works: the buyer pays in the app before the meeting, the money is held, and the seller receives it at the handover.

| Time (Mon 8 Mar 2027) | Step | Context | Money |
| --- | --- | --- | --- |
| 14:01 | Buyer accepts Femke's €225 offer in chat; order placed with "pay at pickup" | Order | Fee quoted: 5% × €225 = €11.25, plus €0.70 = **€11.95** |
| 14:02 | Buyer pays €236.95 by iDEAL; provider confirms; listing reserved | Payment edge, Listing | €236.95 captured into Femke's held balance and Tradeyard's fee balance |
| 14:02–18:05 | Femke's other open conversations are told the bike is reserved; alerts stop | Listing, Messaging | None |
| 18:08 | At the handover, Femke enters the buyer's six-digit handover code | Order | €225 released to Femke's available balance; €11.95 recognized as Tradeyard revenue |
| 18:10 | Order completed; listing marked sold | Order, Listing | None |
| Tue 9 Mar | Payout to Femke's bank account | Payment edge | €225 paid out |

The handover code is the release event: by giving it, the buyer confirms they have seen and accepted the bike, so pay-at-pickup protection covers payment security and the seller not turning up, not "not as described" after handover. Femke had already been verified as a payee by Adyen before her first Safe Deal payout, which is why Veldmark ID will carry that fact as a `payee.verified` claim ([Who Is on the Other Side? Identity and Verification](#identity-and-verification)). The €11.95 fee is charged to the buyer on top of the price, so Femke's DAC7 consideration is €225; with four Safe Deal sales in 2027 totaling €610, she is an excluded seller.

**A protected-payment brand is the scammer's favorite disguise**, as Femke's Sunday evening showed. At 20:11 on Sunday a "buyer" had sent her a link to a fake Safe Deal payment page, on a domain registered that day. Tradeyard users in the Netherlands and Belgium reported about **41,000** payment-link phishing attempts in 2026. The countermeasure is not in the payment platform, which never saw the fake page; it is in the message safety gate that holds links imitating Safe Deal ([From Interest to Contact: Messaging and Lead Management](#messaging-and-leads)). A transactional pivot that does not budget for this is building **Fast Mail for Fraudsters** with its own logo on it.

{id: transactions-and-payments--a-shipped-order-with-a-dispute}
### A shipped order with a dispute

On Tuesday 13 April 2027, a buyer in Antwerp agrees to buy a used camera lens from a private seller in Ghent on Tradeyard Belgium for **€60**, shipped by parcel.

| Date | Step | Money and evidence |
| --- | --- | --- |
| Tue 13 Apr | Order placed and paid by card | Buyer pays €60 + fee €3.70 (5% × €60 + €0.70) + label €6.95 = **€70.65**; listing reserved |
| Wed 14 Apr | Seller prints the label and hands the parcel in at a PUDO point | `ParcelHandedIn`; the seller's deadline was three days |
| Fri 16 Apr | Parcel delivered to a PUDO point near the buyer and collected | `ParcelDelivered`; the two-day dispute window starts |
| Sat 17 Apr | Buyer opens a dispute: a scratch on the front element not shown in the photos | Funds stay held; the case gets the listing photos, chat history and the buyer's photos |
| Mon 19 Apr | Seller offers a €15 partial refund in the dispute flow; buyer accepts | `DisputeDecided`; €15 refunded to the buyer's card |
| Tue 20 Apr | €45 released and paid out to the seller | The fee is not refunded on a partial refund; the label margin (€6.95 charged, about €5.20 carrier cost) stays with Tradeyard |

Every step produced an event, and every amount has a ledger line: €70.65 captured; €3.70 fee revenue; €6.95 label revenue against a carrier cost; €15 refund; €45 seller payout; the provider's processing fee, absorbed by Tradeyard. The December 2026 clearing balance existed because, before 2027, partial refunds were agreed in chat and executed manually by support, and nothing linked them to the order.

![Left: a jumble of unmatched refunds, label charges and payments in a clearing bin. Right: a ledger where every line is linked to an order event and reconciled.](listing-systems-architecture/posts/29-transactions-and-payments/assets/images/29-transactions-and-payments/clearing-to-ledger.jpeg)

**Figure 4:** *The December 2026 clearing balance existed because refunds, label charges and partial refunds were handled outside the order; in the target design every amount is an event with a ledger line, traceable from order to bank movement.*

{id: transactions-and-payments--safe-deal-in-2026-in-numbers}
### Safe Deal in 2026, in numbers

| Measure (2026) | Value |
| --- | --- |
| Orders | 11.6 million (NL, BE, PL) |
| GMV | about €1.02 billion; average item price about €88 |
| Revenue | €75 million: buyer fees about €59 million, shipping-label margin about €16 million |
| Shipped share | about 78% of orders (about 9 million labels); the rest "pay at pickup" |
| Distinct sellers paid | about 1.3 million, of whom about 21,000 above the DAC7 excluded-seller test |
| Disputes opened | about 1.3% of orders (about 151,000); about 70% resolved by agreement or return |
| Buyer-protection losses funded by Tradeyard | about €4.1 million, 0.4% of GMV |
| Card chargebacks | under 0.1% of orders |
| Unmatched items in clearing at the December month-end | about €2.3 million |

Safe Deal is a good business: €75 million of revenue on €1.02 billion of GMV is a 7.4% take rate, and losses are an order of magnitude below revenue. But it was **run as a feature on top of Yardstick's world view** until 2027: its dispute desk worked from e-mail templates, partial refunds were manual and the finance view was reconstructed at month-end.

{id: transactions-and-payments--the-architecture-advice-forum-s-decisions}
## The Architecture Advice Forum's Decisions

On 22 September 2027 the forum applied the four conditions and the architecture above to each proposal.

**Safe Deal Portugal: approved for Q3 2028**, on the target platform rather than as a fourth copy. The conditions all hold for Portuguese goods. The launch adds local payment methods and two national carrier and PUDO networks through new shipping adapters, runs under the same Tradeyard B.V. contract with Adyen, and reports Portuguese sellers under DAC7 through the existing Dutch filing. It waits for the platform work below, because launching a fourth country on the 2024 design would multiply the clearing problem.

**Motorvane private car payment: not escrow; a narrow pilot.** A 5% fee on the Essen Golf's **€21,900** would be about **€1,095**, which no buyer would pay, and a single misdirected payment of that size is a material loss. Most Motorvane listings come from dealers, who have their own payment processes and legal duties. The forum approved only a design study for a "secure handover" for private-to-private sales in Germany: funds held for at most 72 hours around a scheduled handover, a flat buyer fee, release by handover code, and payee verification at proof-of-person level. It is to be decided in Q2 2028 with Adyen's limits and Motorvane's fraud data in hand. Until then, Motorvane invests in the warning and verification controls that [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) describes.

**Hearthly Spain protected deposits: declined.** A rental deposit is a large payment to a landlord under a lease, governed by its own legal rules, and holding it would put Hearthly into the rental contract itself, a different marketplace model with its own licensing and consumer-law questions. The Barcelona ring is better answered upstream: the private-landlord rule that requires proof of person with name match before publishing rentals in Spain, live in Q4 2027 ([Who Is on the Other Side? Identity and Verification](#identity-and-verification)), plus warnings in messaging when a counterparty asks for a deposit before a viewing. **This was the forum's clearest case of declining The Forced Fit**: a goods checkout is not a rental product.

**The transaction platform: funded first.** Before Portugal, Safe Deal moves to the six-context design: an order service that owns availability and timers, a shipping context with normalized tracking events, a dispute case service built on the shared trust-and-safety case management, and a transaction ledger that receives order and money events and feeds group finance. The forum set three objectives for the end of 2028: every Safe Deal amount traceable from order to bank movement; unmatched clearing items under **€100,000** at any month-end; and DAC7 aggregates computed from the ledger rather than assembled from exports.

{id: transactions-and-payments--trade-offs}
## Trade-offs

| Decision | Option A | Option B | Prefer A when | Prefer B when |
| --- | --- | --- | --- | --- |
| Who holds funds | Licensed provider's marketplace product | Own e-money or payment licence | Transactions are a minority of revenue; the group wants speed and less regulation | Payments are the core product and volume justifies safeguarding, capital and a full ledger |
| Merchant of record | Platform | Seller | Private sellers; one brand and one buyer protection | Professional sellers with their own customer relationship and refunds |
| Release rule | Buyer confirmation or a fixed window after delivery | Fixed days after payment | Reliable tracking events exist | Tracking is weak; simpler but slower and riskier for buyers |
| Fee payer | Buyer pays a protection fee | Seller pays a commission | Supply growth matters most (free to sell) | Professional sellers or very low price points |
| Fee shape | Percentage plus fixed amount | Flat fee | Moderate prices | High-value items (cars) or tiny items |
| Shipping | Integrated carriers and labels | Seller arranges shipping | Parcels are standard and tracking drives release | Bulky or specialist items |
| Scope of a shared platform | One transaction platform for all goods brands and countries | Per-brand transaction stacks | Same model, same provider, same legal regime | Different providers, carriers and consumer rules that make sharing an abstraction tax |
| Pivot depth | Optional protected payment beside contact | Payment-first, contact second | Classifieds liquidity is the asset | The marketplace is recommerce from the start (Vinted) |

**Buyer-paid fees** keep selling free, which protects supply, and put the price at the moment of highest intent; Vinted describes its mandatory fee, long known as the Buyer Protection fee and called "the Vinted fee" on its UK price list as of October 2026, as paid at checkout and "usually 3% to 8% + £0.3 to £0.8" in the UK ([Vinted UK price list, 2026](https://www.vinted.co.uk/pricelist)). Marktplaats' 2017 product charged the buyer 2% plus €0.40 ([RetailTrends, 2017](https://retailtrends.nl/news/pdf/50855)), its 2022 successor 5% ([AVROTROS Radar, 2022](https://radar.avrotros.nl/artikel/dit-is-de-vervanger-voor-de-gelijk-oversteken-functie-van-marktplaats-52677)).

**Sharing the transaction platform across countries** is attractive, but it is the layer most exposed to local differences: payment methods, carriers, consumer law and dispute norms. Adevinta's 2023 plan named "the full transactional journey" among the investments it would stop duplicating; under its 2025 decentralization, each market's provider contracts, carriers and consumer-law regimes argue for local ownership again (Adevinta Annual Report 2023; Strategic Report 2025).

> **INFERENCE, NOT DOCUMENTED:** The public descriptions of Kleinanzeigen's and Marktplaats' flows fit a common pattern: a licensed provider holds funds; the marketplace owns the offer and acceptance in chat, the buyer-fee pricing, label generation and tracking, the release timer and dispute handling. It is a plausible reference architecture, not a description of either company's systems.

{id: transactions-and-payments--vertical-differences}
## Vertical Differences

| Dimension | General classifieds goods | Real estate | Automotive | Recommerce and jobs |
| --- | --- | --- | --- | --- |
| Is the pivot common? | Yes, category-gated (leboncoin, Kleinanzeigen, Marktplaats) | Rare; transactions settle with notaries, agents and lease contracts | Reservations and deal steps, rarely full payment | Recommerce is payment-first; jobs have no payment between parties |
| What gets paid on platform | Item, buyer fee, shipping | At most reservation or application fees | Reservation fees, deposits through dealers, financing referrals | Item, fees, shipping, wallet balances |
| Who holds funds | Licensed provider | Notaries, agents, landlords | Dealers and their banks; finance partners | Provider or own licence (Vinted Pay) |
| Main fear protection answers | Non-delivery, misdescription | Fake listings and deposit fraud, answered by verification | Deposit scams, hidden damage, answered by history checks and verification | Non-delivery, counterfeits |
| Typical failure | Ledger missing; Fast Mail for Fraudsters with the platform's brand | Platform holding money it is not allowed to hold | Workflow imposed on dealers (the reservation backlash) | Operational load of shipping and disputes |

Automotive shows the professional side of the trade-off. Autotrader's Deal Builder moved reservations, part-exchange, finance and delivery steps online; the company attributed part of a fall in retailer forecourts in the second half of its 2026 financial year to "concerns with the speed and nature of our Deal Builder product roll-out", and responded by pausing auto-rollout and, as reported in December 2025, introducing a "request a reservation" option that does not require buyer payment ([Autotrader, 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf); [Car Dealer Magazine, 2025](https://cardealermagazine.co.uk/auto-trader-tweaks-deal-builder-product-making-reservations-optional/320706)). **Transactional state placed on a professional's inventory must be opt-in, configurable and reversible.** [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) compares the verticals in full.

{id: transactions-and-payments--failure-modes}
## Failure Modes

**The checkout ships before the ledger.** The order flow goes live, payouts work, and finance discovers at the first month-end that refunds, partial refunds, label charges and chargebacks cannot be matched. Veldmark's €2.3 million clearing balance is the mild version. The fix is to make the ledger and reconciliation part of the launch criteria, not a later phase.

**Release by timer only.** Funds released a fixed number of days after payment, regardless of delivery evidence, pay scammers who never ship and make disputes after release unrecoverable. Release should depend on the delivery event and the dispute window, with a fraud hold able to stop it.

**The double sale.** The listing stays available while an order is in progress, a second buyer pays, and one of them must be refunded. The order must reserve the listing atomically and the reservation must expire.

**Sold, but still everywhere.** A completed order that does not reach every copy of the listing creates **Ghost Inventory**: alerts and digests promote an item that is gone, and a contact form invites buyers to ask about it. The bike in the Tuesday digest is the example.

**Disputes by e-mail.** Without a case system, evidence lives in mailboxes, decisions are inconsistent, decision deadlines are missed and there is no data to price protection. A dispute desk needs cases, evidence, decision codes and service levels.

**The protected-payment brand turned against users.** Phishing pages that imitate the platform's own payment flow follow every launch. Messaging must treat links and payment requests that imitate the brand as high-risk, and users must learn that Safe Deal payments happen only inside the app.

**Tax reporting discovered late.** A platform that discovers DAC7 after its first year of payments has to collect tax identification numbers from thousands of sellers retroactively, with payout holds for non-responders. The data collection belongs in seller onboarding thresholds.

**Provider lock-in by accident.** Seller verification data, card tokens and payout accounts held only in one provider's systems make a later change of provider a migration of every seller. The marketplace should hold its own references and the verification outcome, even when the provider holds the documents ([Adyen: One Platform from Checkout to Settlement](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/adyen.html) discusses the dependency).

**Imposing the goods checkout on other verticals.** A checkout built for parcels is extended to cars, homes or rentals because it exists. This is **The Forced Fit** in its transactional form.

{id: transactions-and-payments--the-chief-architect-s-view}
## The Chief Architect's View

At group scale, transactions raise four standing decisions.

**Decide the pivot per profile, and record it.** Whether a country and category has protected payment, which fulfilment methods and which coverage belongs in the marketplace profile register ([Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy)), as configuration. The general manager owns the commercial decision; finance and legal sign off on the provider, the loss provision and the reporting obligations; architecture owns the cost of change and the platform it runs on. A rule I use: **no category gets protected payment without a named owner for disputes, reconciliation and DAC7.**

**Share the transaction platform among the profiles that use it, and only them.** At Veldmark, Safe Deal is the transaction platform for goods in Tradeyard's countries; Motorvane and Hearthly use the shared layers beneath it (identity, messaging, trust and safety, the event backbone) but not the checkout. Within the platform, keep country-specific parts (payment methods, carriers, consumer-law texts, dispute norms) as adapters and configuration, and keep the order model, the ledger and the dispute case model shared.

**Treat the provider as a strategic dependency.** Conforming to the provider's model is right for speed, and it ties the platform to that provider's accounts, onboarding and reporting. Keep the order, the ledger and the seller's verification outcome in Veldmark's own systems, keep provider identifiers as references, and review the dependency at each contract renewal. Separability matters here too: a brand sold with its transaction business needs its seller balances, open orders and ledger history to go with it ([From Newspaper Columns to Portfolios: How the Classifieds Industry Evolved](#industry-evolution)).

**Measure trust and money together.** The metrics that matter are the share of eligible sales that go through protected payment, dispute rate and outcome by category, buyer-protection losses as a share of GMV, payout delay from delivery, reconciliation breaks at month-end and payment-phishing reports. A rising protected share with falling phishing losses is the pivot working; a rising take rate with rising unmatched items is the pivot borrowing from the future.

{id: transactions-and-payments--questions-to-ask}
## Questions to Ask

1. For which countries and categories do all four conditions hold (ships, moderate price, fear of non-delivery, strangers), and is the gate configuration or code?
2. Which licensed entity holds the buyer's money, who is merchant of record, and who loses money first when a refund cannot be recovered from the seller?
3. What exactly releases funds to the seller, and can a fraud rule hold a payout with a recorded reason?
4. How does an order reserve the listing, when does a reservation expire, and how quickly does a sale reach alerts, digests and recommendations?
5. Can we trace every amount in an order, including partial refunds, labels, provider fees and chargebacks, from the order to the bank movement?
6. Where do disputes live, what evidence do they use, and what is the loss provision per category?
7. Are DAC7 aggregates computed from the ledger, and do we collect tax identifiers before sellers cross the thresholds?
8. Which data would we lose if we changed payment provider next year: tokens, seller verification, payout accounts, transaction history?
9. What stops scammers imitating our protected-payment brand in messages and e-mail?
10. If we had to switch protected payment off in one category, what happens to open orders, held funds and sellers' expectations?

{id: transactions-and-payments--from-transactions-to-monetization}
## From Transactions to Monetization

Protected payment adds a revenue line, but it is one of several ways a listing marketplace makes money, and usually not the largest. Visibility products, professional subscriptions, insertion fees, lead products and advertising each ask for different systems and each spend liquidity differently. [How Listing Marketplaces Make Money](#monetization-models) catalogs the models with their published KPIs and shows what each one requires from the architecture.

{id: transactions-and-payments--sources-and-evidence}
## Sources and Evidence

{id: transactions-and-payments--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Adevinta Annual Report 2019](https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf) — Adevinta, 2020. leboncoin's transactional launch in generalist categories.
- [Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf) — Adevinta, 2024. Transactional revenue, margin dilution, transactional costs, Marktplaats' transactional history, "full transactional journey".
- [Strategic Report 2025, Aurelia UK Feederco Ltd](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf) — Adevinta, 2026. Decentralization and shipment-driven emissions.
- [From Hello World to a dispute management back office](https://adevinta.com/techblog/from-hello-world-to-a-dispute-management-back-office/) — Adevinta tech blog, 2023. A reusable cross-marketplace dispute component.
- [Sicher bezahlen](https://themen.kleinanzeigen.de/sicher-bezahlen/) — Kleinanzeigen, n.d. (consulted October 2026). Provider, 14-day automatic release, methods, carriers, covered cases.
- [Machine learning for delivery time estimation](https://tech.olx.com/machine-learning-for-delivery-time-estimation-1-591c8df849a0) — OLX Tech, 2023. Pay&Ship flow.
- Prosus FY25 results booklet — Prosus, 2025. De-prioritization of pay-and-ship in Europe.
- [Financial results 2025](https://company.vinted.com/newsroom/financial-results-2025) — Vinted, 2026. GMV, PUDO network, Vinted Go.
- [Vinted Pay](https://company.vinted.com/newsroom/vinted-pay) — Vinted, 2026. E-money licence and wallet.
- [Vinted UK price list](https://www.vinted.co.uk/pricelist) — Vinted, updated October 2026. The buyer-paid fee and its formula.
- [eBay Form 10-K for 2025](https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm) — eBay, 2026. Transaction losses from buyer protection and chargebacks.
- [Autotrader FY2026 results](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf) — Autotrader Group, 2026. Deal Builder and retailer reaction.
- [Worldline to acquire 40% stake in Online Payment Platform](https://worldline.com/de-at/home/top-navigation/media-relations/press-release/pr-2022_09_09_01) — Worldline, 2022. OPP's marketplace clients.

{id: transactions-and-payments--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Adyen for Platforms: marketplaces](https://docs.adyen.com/marketplaces/) and [platforms](https://docs.adyen.com/platforms/) — Adyen, n.d. Onboarding, verification, split payments, held funds and payouts.
- [How charges work in a Connect integration](https://docs.stripe.com/connect/charges) — Stripe, n.d. Charge types, refunds and dispute liability.
- [Directive (EU) 2015/2366, Article 3](https://eur-lex.europa.eu/eli/dir/2015/2366/oj) — European Union, *Official Journal*, 2015 (wording checked against the Publications Office text, October 2026). The commercial-agent exclusion.
- [Information about DAC7 for platform operators](https://belastingdienst.nl/wps/wcm/connect/en/business/content/information-for-platform-operators-dac7) — Belastingdienst, n.d. Reportable data, deadlines and the excluded-seller test.

{id: transactions-and-payments--research-and-practitioner-sources}
### Research and practitioner sources

- [eBay Kleinanzeigen launches "Sicher bezahlen"](https://onlinemarketing.de/?p=214785) — onlinemarketing.de, 2020. Launch, 14-day hold, initial categories.
- [Kleinanzeigen payment provider OPP](https://t3n.de/news/?p=1565510) — t3n, 2023. Sellers registering with Online Payment Platform.
- [Gelijk Oversteken open to all users](https://retailtrends.nl/news/pdf/50855) — RetailTrends, 2017. Marktplaats' first escrow-style flow and its fee.
- [Dit is de vervanger voor de 'Gelijk Oversteken'-functie van Marktplaats](https://radar.avrotros.nl/artikel/dit-is-de-vervanger-voor-de-gelijk-oversteken-functie-van-marktplaats-52677) — AVROTROS Radar, 2022. Withdrawal of the first product and the buyer-protection successor.
- [Scam ads slipping through the net too easily on second-hand marketplaces](https://www.which.co.uk/policy-and-insight/article/scam-ads-slipping-through-the-net-too-easily-on-second-hand-marketplaces-which-warns-aqyF66m1TlU1) — Which?, 2024. Which marketplaces offer buyer protection.
- [Auto Trader tweaks Deal Builder product, making reservations optional](https://cardealermagazine.co.uk/auto-trader-tweaks-deal-builder-product-making-reservations-optional/320706) — Car Dealer Magazine, 2025. Professional pushback against transactional state.
- [Leboncoin](https://en.wikipedia.org/wiki/Leboncoin) — Wikipedia, accessed 2026. Trusted-third-party role since 2018 and Adyen partnership (secondary source).

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
