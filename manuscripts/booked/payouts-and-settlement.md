{id: payouts-and-settlement}
# 28. Paying the Supply Side: Payouts, Commissions and Settlement

![Paying the Supply Side: Payouts, Commissions and Settlement — logo](stays-marketplace-architecture/posts/28-payouts-and-settlement/assets/images/28-payouts-and-settlement/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow the money from the guest's payment to the hotel's or host's bank account, and the commission back from properties that collected it themselves. You will design the settlement ledger, the release rules, the payout engine, commission invoicing and the partner statement, and see where holds, deductions, split payouts and know-your-customer gates belong.

> **WHY THE BUSINESS CARES:** For a host, the payout is the product: a late, wrong or unexplained payout loses a listing faster than any ranking change. For an OTA, the commission invoice is most of the revenue, and every overdue invoice is cash the marketplace has earned but not received. The CFO needs one number for what the marketplace owes its suppliers tonight, and the auditor needs to see how it was reached.

> **WHY ARCHITECTS SHOULD CARE:** Payouts are where every upstream mistake becomes money: an alteration that was not posted, a cancellation fee nobody deducted, a bank account that changed an hour before a run. If balances are scattered across a monolith's tables, a payments provider's dashboard and a spreadsheet, nobody can answer "what do we owe this host, and why?" without an investigation. A settlement ledger with clear posting rules turns that question into a query.

> **KEY POINTS:**
>
> * **The settlement ledger, not the payout system, decides who is owed what.** Every event that changes what a partner is owed (booking, alteration, cancellation, check-in, claim, deduction, return) becomes a double-entry posting on that partner's accounts. The payout engine only pays what the ledger shows as available, and the commission invoice and partner statement are reports on the same entries.
> * **Release rules and holds are where risk is managed, so make them explicit.** Hosted stays pay individuals soon after check-in, before chargeback windows close, so pending, available and held balances, deduction order and negative-balance recovery are risk decisions that need owners. Hotels are paid later and through cards or netting, which moves the risk to commission collection instead.
> * **One ledger can serve both marketplaces; one payout product cannot.** Hosts need fast payouts to individual accounts, tax-identity gates and split payouts to co-hosts. Hotels need virtual cards, monthly invoices, value-added tax (VAT) documents and netting. Share the ledger, the beneficiary registry and the rails, and keep the release policy and statements specific to each marketplace.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Ledgerless Money** — Nookaway's host balances lived in mutable payout rows in its monolith, so a single host's payout could not be explained without reading three systems.
> * **Policy Spaghetti** — Host cancellation fees, partner recoveries and commission corrections were each applied by a different tool, with its own rule for when and from what they were deducted.
> * **The Tax Patchwork** — Tax-identity collection and reporting were attached to the listing owner's account, so payouts that reached co-hosts and managers off-platform were invisible to the DAC7 report.

A stays marketplace takes money from millions of guests and owes most of it to someone else. On a hosted-stays marketplace the platform holds the whole booking amount until the guest arrives and then pays the host, net of its fee. On an accommodation marketplace run by an online travel agency (OTA) the money moves in two directions at once: for merchant bookings the platform collects from the guest and pays the hotel, and for agency bookings the hotel collects at the desk and the platform has to invoice its commission and get paid. **Settlement** is the process that turns all of these flows into an agreed amount per partner, and a **payout** is the transfer that discharges what the marketplace owes.

Payouts look like a batch job that reads bookings and sends bank transfers. They become hard when bookings change after the payout amount was computed, when a host owes the platform money because of a cancellation, when a bank returns a transfer five days later, when a fraud team wants to stop one payout without stopping the others, and when a tax authority asks how much was paid to whom for which property. **Each of those is a change to a balance, and a balance that is not kept in a ledger is kept in many places at once.**

This chapter is the supply-side half of Part VI. It takes the payment model decided in [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models) and the funds collected by [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments), and it ends where [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation) begins: with entries that can be reconciled. It owns the **payout**, the **settlement ledger**, the **commission invoice** and the **partner statement**. It does not re-teach double-entry ledger design, which RECONCILED covers in [Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html) and [Payments-to-Ledger: Draining the Suspense Swamp](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-to-ledger.html), or tax calculation, which belongs to [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays).

{id: payouts-and-settlement--setting-the-scene-at-corvane-why-is-my-payout-244-40}
## Setting the Scene at Corvane: "Why Is My Payout €244.40?"

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), runs payouts for two very different marketplaces through one payments institution. Corvane Payments B.V., licensed as an electronic money institution by De Nederlandsche Bank since 2024, collects every Nookaway booking and every Roomstead merchant booking, holds the guest funds and pays the supply side. In 2026 it sent about **6.3 million** payouts to Nookaway hosts in **19 currencies**. Roomstead's merchant bookings, **30%** of its room nights, were paid to hotels mostly by virtual card. The other 70% were agency bookings, for which Keystone, Roomstead's Java and Oracle monolith, issued monthly commission invoices. Fathom, the double-entry ledger Corvane Payments built in 2023–24, recorded the money Corvane Payments held and moved, but not what each host or hotel was owed line by line.

In May 2027 three questions reached Leila Haddad, Head of Payments and Finance Engineering, in the same week.

The first came from Carmen Ruiz, the Seville host. In February her Nookaway payout for a three-night stay had been **€244.40** instead of the €374.40 she expected. The difference was the **€130** host cancellation fee from the Seville double booking: on 2 February she had canceled the Bauers' Feria-week reservation after the competing platform sold the same nights. The fee was correct. But Elena Petrova's support agent needed forty minutes and three systems to show it: Burrow's payout table (which held the payout amount, already overwritten), a separate "pending deductions" table (which recorded the fee as applied but not to which payout), and Corvane Payments' transfer log (which held the €244.40 transfer with no line items).

The second came from Marco Bellini, the CFO. Nookaway's year-end 2026 accounts showed **€3.4 million** in host debit balances, amounts hosts owed Nookaway because deductions exceeded their later payouts, spread across about **21,000** hosts. **€1.1 million** of it was older than 180 days. Nobody could say how much would ever be recovered, because the balances were not in Fathom; they were derived each night from Burrow's tables.

The third came from Hotel Prinsenkade in Amsterdam. After the King's Day overbooking on 27 April 2027, Roomstead had relocated four of the hotel's walked guests at a cost of **€2,150**, of which **€1,600** was recoverable from the hotel under the partner terms. A finance analyst raised a manual invoice for the €1,600 in Keystone. The hotel's controller saw a separate invoice with no reference to the reservations, while Roomstead's virtual cards for its merchant bookings kept arriving at full value, and disputed it. The same hotel also had **€33,730** of commission and recovery to pay Roomstead for April, while Roomstead had loaded **€78,948** onto virtual cards for that hotel's merchant bookings in the same month. Nobody had designed the two flows to meet.

Mariana Costa, the Group Chief Architect, put one question to the architecture forum: **"Where does the truth about what we owe each host and hotel, and what they owe us, live, and what is a payout system allowed to decide on its own?"** The rest of this chapter is the answer she reached with Leila's team.

{id: payouts-and-settlement--concepts-payables-receivables-and-the-life-of-a-balance}
## Concepts: Payables, Receivables and the Life of a Balance

The vocabulary matters, because the same words mean different things to engineers, finance and partners.

- **Supply side (partners and hosts).** Properties, hosts, co-hosts and property managers that fulfill the stay. In this chapter a **beneficiary** is anyone the marketplace pays, which may be a different party from the account that manages the listing.
- **Payable.** An amount the marketplace owes a partner. On a merchant or hosted-stays booking it arises when the booking is confirmed and the guest has paid.
- **Receivable.** An amount a partner owes the marketplace: agency commission, a cancellation fee, a recovery after an overbooking, an overpayment to be clawed back.
- **Settlement.** The process of determining, netting and discharging payables and receivables per partner for a period or per booking. A **settlement ledger** is the double-entry record of every payable and receivable per partner, at line level, with the event that caused it. It is a **sub-ledger**: it feeds the general ledger in summary (see [Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html)).
- **Payout** (or **remittance**, the hotel term). Any transfer that discharges what the marketplace owes the supply side.
- **Commission invoice.** A legal tax document the marketplace issues to an agency partner for commission earned on stays that took place in a period, with VAT treatment and a due date. It creates a receivable.
- **Partner statement.** A periodic, line-level account of everything that changed a partner's balance in the period, whatever the rail or document: bookings, fees, commission, adjustments, payouts, card loads, invoices and payments received. It is the one document a partner can reconcile against its own books.
- **Balance states.** A payable moves through **pending** (owed but not yet releasable), **available** (releasable and not yet paid), **held** (releasable in principle, stopped by a risk, compliance or dispute decision) and **paid**. A partner with more receivables than payables has a **debit balance** (a negative balance).
- **Release rule.** The rule that moves a payable from pending to available, usually tied to check-in, check-out or a number of days after one of them.
- **Payout rail.** The mechanism that moves the money: a bank credit transfer (in the Single Euro Payments Area, SEPA, a domestic system or an international wire), a card push, a wallet, a balance at a payment service provider (PSP), or a **virtual card**, a single-use card number loaded with the amount owed for one booking, which the hotel charges through its own card terminal.
- **Netting.** Paying the difference between payables and receivables instead of paying the payables in full and invoicing the receivables separately.

One clarification prevents most design arguments: **the payable belongs to the booking, not to the payout.** A payout settles many payables, minus receivables, at one moment, and a booking can produce a payable, a reversal, a deduction and a second payable after an alteration. "Paid" is therefore not a property of a booking; only the ledger can say what has been settled.

{id: payouts-and-settlement--three-money-paths-on-one-supply-side}
## Three Money Paths on One Supply Side

Before designing components, it helps to see the three paths side by side. [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models) owns the choice between them; this chapter owns what each one demands from settlement.

![A guest pays the platform, which pays a host and a merchant hotel; the guest pays an agency hotel directly, which pays commission back to the platform; every movement is posted to a settlement ledger.](stays-marketplace-architecture/posts/28-payouts-and-settlement/assets/images/28-payouts-and-settlement/28-three-money-paths.jpeg)

**Figure 1:** *Three money paths. Hosts and merchant-model hotels are paid by the platform after it has collected from the guest; agency-model hotels collect themselves and pay commission back. The settlement ledger has to hold both directions for the same partner.*

| | Hosted stays (facilitated) | OTA merchant booking | OTA agency booking |
| --- | --- | --- | --- |
| Who holds the guest's money before the stay | The platform's payment entity | The platform's payment entity | Nobody, or the hotel (card guarantee) |
| What the platform owes or is owed | Payable to host, net of host fee | Payable to hotel, net of commission or margin | Receivable: commission from hotel |
| Typical release | Shortly after check-in | At or after check-in; virtual card activation date | Invoice after check-out, monthly |
| Typical rail | Bank transfer, card push, wallet | Virtual card, or bank transfer | Hotel pays by direct debit, transfer or card |
| Who carries collection risk | Platform recovers deductions from future payouts | Low: platform keeps its margin before paying | **Platform: commission may never be paid** |
| What the partner needs to see | Earnings per reservation, fees, deductions, tax forms | Remittance advice per card or transfer | Invoice with stays, commission base, VAT |

The architectural point is that **one partner can sit in two columns at once.** Booking.com's partner documentation describes a "mixed model" in which a property lets Booking.com facilitate some guest payments and collects others itself, and Booking.com then sends "a monthly invoice that includes the commission and service fees for all reservations of that month" ([Payments by Booking.com](https://partner.booking.com/en-gb/solutions/payments-bookingcom), n.d., as fetched in October 2026). Expedia's guests can choose per booking whether to pay Expedia now or the hotel at the stay ([Expedia Group 10-K for 2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm), filed February 2026). A settlement design that has one module for "merchant remittance" and another for "agency invoicing", each with its own idea of the partner's balance, cannot produce a single statement for Hotel Prinsenkade. That is what happened at Roomstead.

{id: payouts-and-settlement--architecture-a-ledger-in-the-middle-engines-around-it}
## Architecture: A Ledger in the Middle, Engines Around It

The design Corvane adopted, and the one I recommend for any marketplace that both collects and invoices, puts a settlement ledger at the center and gives every other component a narrow job.

![Events feed an earnings calculator that posts to a central settlement ledger; a release scheduler guided by trust changes balance states; payout engine, invoicing and statements read from the ledger, and the payout engine pays banks.](stays-marketplace-architecture/posts/28-payouts-and-settlement/assets/images/28-payouts-and-settlement/28-ledger-in-the-middle.jpeg)

**Figure 2:** *The settlement architecture. Business events become postings; the release scheduler and trust decisions change balance states; the payout engine and invoicing only act on what the ledger says; statements are a view of the ledger, not a separate calculation.*

Each component needs a written contract, because Corvane's problems came from missing boundaries rather than from bad code.

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Earnings calculator** | Turn reservation, payment and claim events into postings, using the fee schedule and commission terms in force at booking time | Posting rules, fee and commission versions | Send money; read bank details |
| **Settlement ledger** | Record every payable, receivable and state change per partner, double-entry and append-only | Accounts, entries, balances, audit trail | Be edited in place; compute fees |
| **Release scheduler** | Move payables from pending to available when the release rule fires; apply and lift holds | Release rules per marketplace and segment, hold records with reasons | Decide fraud or compliance outcomes itself |
| **Beneficiary registry** | Hold who can be paid, to which account, in which currency, with what verification and tax status, and how a listing's earnings split | Payout accounts, KYC and tax-identity state, split rules | Store balances |
| **Payout engine** | Build payouts from available balances, choose the rail, send instructions idempotently, process confirmations and returns | Payout runs, instructions, rail adapters, return handling | Decide amounts beyond what the ledger shows |
| **Commission invoicing** | Issue legal invoices and credit notes from commission entries, collect, dun and escalate | Invoice numbering, VAT presentation, collection status | Recalculate commission from bookings |
| **Partner statements** | Present every entry in a period per partner, with references a partner can match | Statement formats, exports, APIs | Hold their own totals |

Three rules make the contracts hold.

1. **Amounts are decided once, at the earnings calculator, from versioned terms.** The fee or commission percentage in force when the booking was made is stored with the posting. A fee change, like the one Airbnb described in its 2025 annual report when it began moving from split fees to a single host fee in October 2025 ([Airbnb 10-K for 2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), filed February 2026), then changes new postings without rewriting old ones.
2. **The payout engine reads balances; it does not compute them.** A payout run asks the ledger for available balances per beneficiary and currency, and posts the payout back as an entry that moves money from "available" to "in transit". If the run fails halfway, the ledger shows exactly which beneficiaries were included.
3. **Corrections are new entries.** An alteration, a cancellation after release or a mistaken deduction is reversed and re-posted, never overwritten. Airbnb's 2022 description of its rebuilt payment orchestration makes the same choice: events are append-only, and an alteration such as "adding another night to a stay" is modeled as a new version in a sequence of plans, so that the versions together give "a complete history of the intended and actual money movement" ([Ross et al., Airbnb Engineering, 2022](https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b)).

{id: payouts-and-settlement--the-accounts-per-partner}
### The accounts per partner

The minimum chart of accounts for supply-side settlement is small. Each account exists per partner (or beneficiary), per currency and, where it matters, per legal entity.

| Account | Direction | Used by | Moves when |
| --- | --- | --- | --- |
| **Partner payable – pending** | Owed to partner | Hosted stays, OTA merchant | Booking captured; alteration; cancellation before release |
| **Partner payable – available** | Owed to partner | Hosted stays, OTA merchant | Release rule fires |
| **Partner payable – held** | Owed, blocked | Both | Risk, compliance or dispute hold placed or lifted |
| **Payout in transit** | Being paid | Both | Payout instruction sent; confirmed or returned |
| **Partner receivable** | Owed by partner | Both | Commission earned (agency), cancellation fee, recovery, clawback |
| **Unearned fee or commission** | Platform's, not yet earned | Hosted stays, OTA merchant | Booking captured; earned at check-in |
| **Tax collected on behalf** | Owed to an authority | Both, where the platform collects | Booking captured; remitted (owned by [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)) |
| **Card issued, unsettled** | Owed to issuer | OTA merchant with virtual cards | Card loaded; charged by hotel; expired or voided |

The account list is deliberately close to the reference design in the research behind this book, which derives a similar set from the public filings of Booking Holdings, Expedia and Airbnb. Those filings show the accounting shadow of such ledgers: Airbnb reported **$5,931 million** of funds held on behalf of customers at 31 December 2025, with an equal liability, plus **$1,616 million** of unearned fees ([Airbnb 10-K for 2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), filed February 2026); Booking Holdings reported **$5.3 billion** of deferred merchant bookings, "comprised principally of amounts estimated to be payable to travel service providers" ([Booking Holdings 10-K for 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), filed February 2026). How either company structures its internal ledger is not public.

{id: payouts-and-settlement--the-life-of-a-payable}
### The life of a payable

![Payable states Pending, Available, In transit and Paid, with Held and Reversed branches, and a returned transfer going from In transit back to Available.](stays-marketplace-architecture/posts/28-payouts-and-settlement/assets/images/28-payouts-and-settlement/28-life-of-a-payable.jpeg)

**Figure 3:** *The life of a payable. Every arrow is a ledger entry with a reason. A returned transfer goes back to available, not to a support queue, and a hold is a state with an owner and an expiry, not a flag on a payout row.*

The state machine looks trivial, but three of its properties are worth defending in review.

- **"Held" is a balance state, not a payout state.** If holds are flags on payout rows, a hold can only stop a whole payout. As a balance state it can stop one reservation's payable while the rest of the host's earnings flow, which is what a trust team usually wants.
- **A returned transfer returns the money to "available".** The beneficiary then needs a fixed account, and the next run pays again. Treating returns as a support ticket is how money ends up in unreconciled suspense.
- **Reversal after payment is not a state of the payable.** Once paid, a later cancellation or claim creates a new **receivable**, which is recovered by deduction from future payables or collected. This is the debit balance that Nookaway could not see.

{id: payouts-and-settlement--in-practice-how-marketplaces-pay-the-supply-side}
## In Practice: How Marketplaces Pay the Supply Side

{id: payouts-and-settlement--hosted-stays-fast-payouts-to-individuals-with-holds}
### Hosted stays: fast payouts to individuals, with holds

Airbnb's public terms are the most detailed description of hosted-stays payout policy. Its Payments Terms of Service, dated 5 February 2026, say that for accommodation Airbnb Payments initiates the payout "by the end of the business day after the Guest's scheduled check-in date." Hosts who have not completed two stays (unless they verified a listing), or who are in breach, are paid by the end of the business day after check-out, and stays of 28 nights or more follow a monthly schedule ([Airbnb Payments Terms](https://www.airbnb.com/help/article/2909), 2026; the European version uses the same wording, [Airbnb Payments Terms for European Users](https://www.airbnb.ie/help/article/2909), 2026). The same terms let Airbnb Payments "temporarily place a hold, suspend, or cancel any Payout" for fraud prevention, risk assessment, investigations or failed verification, hold funds "for up to 72 hours" when a host cancels while the guest is refunded or rebooked, and recover refunds larger than a payout from future payouts.

Four architectural facts follow from those terms, and they apply to any hosted-stays marketplace:

- **Release is tied to the scheduled check-in, not to an observed arrival.** A platform rarely knows when a guest walked in. The release rule fires on time, and the trust system has a window to stop it if the guest reports a failed check-in.
- **Release rules depend on the host's history.** The new-host rule is a risk policy: until the host has a track record, the platform waits until check-out, when a failed stay would have surfaced.
- **Arrival time depends on the rail, not on the release.** Airbnb's help center lists arrival times by method after release, from "30 minutes or less" for its fast-pay and pay-to-card options in eligible regions to three to five business days for bank accounts and three to seven for international wires, and says a fraud review can delay funds "up to 45 days after guest check-in" ([When you'll get your payout](https://www.airbnb.com/help/article/425), Airbnb, n.d., as fetched in October 2026).
- **Recovery from future payouts is the default collection mechanism.** It works only if the receivable is a ledger entry that the next payout run nets against.

The chargeback window explains why holds matter. Card schemes let a guest dispute a charge months after the transaction, and a hosted-stays platform has usually paid the host long before. Airbnb reported a total chargeback expense of **$67 million** for 2025 ([Airbnb 10-K for 2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), filed February 2026). The dispute itself belongs to [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation) and [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud); what belongs here is that **every pre-payout control is cheaper than a post-payout recovery**, which is why new-host delays and payout holds exist.

Airbnb's engineering record shows how the plumbing evolved. In 2018 Airbnb wrote that host payouts largely went by **batch** files to banks, which "leaves our systems out-of-sync until batch response files are processed" ([Airbnb Engineering, 2018](https://medium.com/airbnb-engineering/measuring-transactional-integrity-in-airbnbs-distributed-payment-ecosystem-a670d6926d22)). In 2022 it described orchestration rebuilt as "retryable idempotent steps" reaching "five 9s (99.999%) of consistency for payments", with a data model built around a bill rather than a reservation ([Ross et al., 2022](https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b)). Its 2026 "Pay as a Local" post lists **Payout**, **Ledger** and **Settlement & Reconciliation** among the subdomains of its payments domain ([Haile et al., Airbnb Engineering, 2026](https://airbnb.tech/payments/pay-as-a-local/)). These posts describe the shape of the system at their dates; the current internals of Airbnb's payout and ledger services are not public.

{id: payouts-and-settlement--co-hosts-and-split-payouts}
### Co-hosts and split payouts

The single-owner model breaks when a listing is run by more than one person. Airbnb's 2023 Winter Release mentioned "two new co-host payout options", and its Co-Host Network, launched on 16 October 2024 with more than 10,000 co-hosts in 10 countries, lets hosts share messaging, calendar access and payouts with co-hosts ([Airbnb 2024 Winter Release](https://news.airbnb.com/en-uk/airbnb-2024-winter-release-introducing-co-host-network-the-best-local-hosts-to-manage-your-airbnb), 2024). By its Q2 2025 shareholder letter, the network supported more than 100,000 listings ([Airbnb Q2 2025 letter](https://www.sec.gov/Archives/edgar/data/1559720/000119312525174438/d17531dex991.htm), 2025). Airbnb also requires that "every host, new co-host, and booking guest must be identity verified" ([Airbnb help center](https://www.airbnb.com/help/article/1237), n.d.).

A split payout is not a payout feature; it is a **beneficiary model**. The listing has an owner, possibly an operator, one or more co-hosts and perhaps a cleaner, and each payee needs its own verified account, its own tax identity and its own line on its own statement. The split rule (a percentage of the nightly payout, the whole cleaning fee, a fixed amount per stay) has to be versioned and agreed by the owner, because changing it changes who reports what income. The research digest behind this book notes that the generic hosted-stays model separates owner, controller, licensed operator, co-host, service provider, payout beneficiary and tax party when it is stressed by co-hosting; that list is the right starting point for the registry.

Platforms that rent their payments capability rather than building it meet the same choice in their provider's API. Stripe Connect's documentation describes "separate charges and transfers" for cases where one charge must be split among several connected accounts or where the charge is created "before the destination account is known", and notes that with destination charges "refunds and chargebacks reduce your platform's balance" ([Stripe Connect charges](https://docs.stripe.com/connect/charges), n.d.). Adyen's marketplace product lets a platform "split the payments between one or more users, deduct costs as needed, and hold funds until payout" ([Adyen for Platforms](https://docs.adyen.com/marketplaces/), n.d.). For a hosted-stays marketplace the separate-transfer pattern fits better than an immediate destination transfer, because the host must not be paid before check-in and the amount may change before then. RECONCILED's [Stripe: Every Movement Is a Balance Transaction](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/stripe.html) and [Adyen: One Platform from Checkout to Settlement](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/adyen.html) chapters describe both platforms in depth.

{id: payouts-and-settlement--ota-merchant-bookings-virtual-cards-and-remittance}
### OTA merchant bookings: virtual cards and remittance

An OTA pays hotels through infrastructure the hotels already have. Booking.com's payouts documentation lists three rails under Payments by Booking.com: **bank transfer**, monthly, weekly or in some countries daily; a **virtual credit card** per booking, holding "the exact amount the guest paid", which the partner charges once funded; and Stripe, "only available for Home properties in the US and Canada", with funds released per reservation on the check-in day. It distinguishes **gross** payouts, which pay "the total reservation amount" while the partner settles commission invoices separately, from **net** payouts, which exclude "Booking.com commission and payment fees"; bank transfers can be either, while virtual cards and Stripe are "almost always gross" ([Understanding payouts](https://developers.booking.com/connectivity/docs/payments-by-booking-onboarding-api/understanding-payouts), Booking.com, n.d., as fetched in October 2026). The same documentation lists seven virtual-card activation policies, from the booking date to "long after check-out" and including activation on the cancellation date, which pays a cancellation fee. Booking.com's partner page adds that a new card "becomes chargeable on a POS as soon as the reservation becomes non-refundable (if you meet certain criteria)" ([Payments by Booking.com](https://partner.booking.com/en-gb/solutions/payments-bookingcom), n.d.).

Two observations from these documents shape the settlement design.

- **The same platform runs a payout rail per supply type.** Per-check-in payouts for homes resemble hosted-stays practice; per-booking virtual cards fit hotel card-acceptance and night-audit routines.
- **A virtual card is a payable settled through someone else's ledger.** Once loaded, the amount sits with the card issuer until the hotel charges it. The ledger must track issued, charged, expired and voided cards, and a modification must resize or reissue the card. When this tracking is loose, hotels charge cards for reservations that were later canceled or changed. That is the **€1.8 million reconciliation gap** Corvane Payments found in Q1 2027, which [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation) works through.

Supplier payment terms for merchant bookings are longer than hosted-stays payouts. Expedia's 2025 annual report says "payments to suppliers are generally due within 30 days of check-in or stay" ([Expedia Group 10-K for 2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm), filed February 2026). That longer window lets an OTA net losses and corrections before paying, which a hosted-stays platform cannot do.

{id: payouts-and-settlement--ota-agency-bookings-commission-invoicing-and-collection-risk}
### OTA agency bookings: commission invoicing and collection risk

For agency bookings the money flows the other way. Booking.com describes its agency business plainly: the provider "just pays us a commission" after the stay ([How we work](https://www.booking.com/content/how_we_work.html), Booking.com, updated 31 May 2025). Booking Holdings' agency revenues, "almost entirely" commissions on Booking.com accommodation reservations, were **$7,968 million** in 2025, down 6.5% as the business shifted toward merchant ([Booking Holdings 10-K for 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), filed February 2026). Agoda's growth program shows the two collection choices side by side: its incremental "cost per booking" commission is "deducted from each booking payout or invoiced monthly on departed room nights" ([Agoda Growth Program](https://www.partnerhub.agoda.com/?p=95313), Agoda, 2025).

"Invoiced monthly on departed room nights" contains most of the design.

- **The invoice basis is the stay, not the booking.** Commission is earned when the stay happens, so the invoice is built from stayed or departed reservations in the period, after no-shows and cancellations are known. A reservation that was canceled or that the hotel marked as a no-show must not be on the invoice, or must appear with a credit note if it was.
- **The hotel's word is an input.** The platform never sees agency money; it learns that a stay happened, and at what price, from status updates, departure confirmations or disputes. "This guest never arrived" is the agency counterpart of a payout correction and flows through the ledger as a credit note. [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) owns the no-show and departure states.
- **The invoice is a legal document.** It has a sequential number, an issuing entity, VAT treatment (for a business customer in another EU member state, normally the reverse charge; see [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)), a currency and a due date. Invoices are never edited; corrections are credit notes.
- **Collection is the platform's risk.** An agency booking pays the hotel first, so the commission is an unsecured receivable. The remedies for non-payment (reminders, interest, suspending availability) are commercial decisions, but the data they need, the receivable's age and dispute status, has to come from the ledger.

**Netting reduces collection risk where the rail allows it.** A partner paid by net bank transfer settles its commission automatically. A partner paid by gross virtual cards cannot net, because each card is loaded with a booking's amount, so its commission invoice remains a receivable, which is the position Hotel Prinsenkade was in.

{id: payouts-and-settlement--know-your-customer-gates-tax-identity-and-changed-bank-details}
### Know-your-customer gates, tax identity and changed bank details

A payout is the moment money leaves the platform's control, so it is where verification has to be complete. Three gates belong in the beneficiary registry, and the payout engine must check all three before it sends anything.

1. **Identity and business verification.** Hosted-stays platforms verify individuals (know-your-customer, KYC) and OTAs verify legal entities (know-your-business, KYB). Booking.com, for example, "is required to collect and verify information from each partner willing to use Stripe" through a Know Your Partner form ([Understanding payouts](https://developers.booking.com/connectivity/docs/payments-by-booking-onboarding-api/understanding-payouts), n.d.). Onboarding collects this ([From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding)); settlement enforces it, because a beneficiary can be added after onboarding, as a co-host is.
2. **Tax identity.** The EU's DAC7 directive (the seventh amendment to the Directive on Administrative Cooperation) makes "the rental of immovable property" a reportable activity and requires platforms to report, per seller and quarter, the consideration paid, "fees, commissions or taxes withheld or charged", and for property sellers the address of each listing, for periods from 1 January 2023 ([Council Directive (EU) 2021/514](http://publications.europa.eu/resource/celex/32021L0514), 2021). Airbnb's terms allow payouts to be withheld when tax documentation is insufficient ([Airbnb Terms of Service](https://www.airbnb.com/help/article/2908), 2026). In practice that turns tax-identity collection into a payout gate for hosts. The report is generated from the settlement ledger's payouts per beneficiary and listing, which is why the beneficiary, not the listing owner, must be the unit of reporting. [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays) owns the rules.
3. **Payout-account integrity.** A changed bank account is the classic account-takeover cash-out. Hospitality-industry warnings about extranet attacks describe payout details being changed to foreign accounts after a partner account is compromised, and [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) treats bank-detail changes as a takeover signal. The defenses are step-up authentication for bank-detail changes, a cooling-off period during which payouts to a new account are held or capped, and a name check against the receiving bank. For euro transfers the last is now a legal service: the Instant Payments Regulation requires a payer's payment service provider to offer **verification of the payee**, matching the account identifier with the payee's name before the transfer is authorized, from 9 October 2025 for providers in the euro area ([Regulation (EU) 2024/886, Art. 5c](http://publications.europa.eu/resource/celex/32024R0886), 2024). The same regulation lets non-consumers that submit payment orders "as a package" opt out of the check; a marketplace sending payouts in bulk should decide deliberately whether to opt out, because the name check is cheap fraud protection.

The same regulation requires euro-area providers to send instant euro credit transfers by 9 October 2025, with funds available to the payee within ten seconds. That makes near-real-time euro payouts a commodity rail, and it removes the window in which a mistaken or fraudulent payout could be recalled: **controls must move before the payout, not after it.**

{id: payouts-and-settlement--corvane-worked-example-carmen-the-novaks-and-prinsenkade-on-one-ledger}
## Corvane Worked Example: Carmen, the Novaks and Prinsenkade on One Ledger

Mariana's forum decided that **Fathom becomes the settlement ledger of record** for both brands. Every Nookaway host and Roomstead partner gets accounts in Fathom; Burrow and Keystone stop holding balances and only emit events. The three cases from the scene show what that changes. All figures are illustrative, like everything about Corvane.

{id: payouts-and-settlement--carmen-s-february-payout}
### Carmen's February payout

On 2 February 2027 the Bauers' booking of Carmen's apartment for 20–25 April was captured: a subtotal of **€1,360** (five nights at €260 plus €60 cleaning). Under Nookaway's split fee, the guest paid a 12% service fee of €163.20 and Carmen's 4% host fee was €54.40, so her pending payable was **€1,305.60**. When Carmen canceled at 13:05 the same day, the target design posts:

| Time | Event | Debit | Credit | Amount |
| --- | --- | --- | --- | --- |
| 2 Feb, 10:12 | Booking captured | Guest funds held | Carmen payable – pending | €1,305.60 |
| | | Guest funds held | Unearned guest and host fees | €217.60 |
| 2 Feb, 13:05 | Host cancels; guest refunded in full | Carmen payable – pending | Guest funds held | €1,305.60 |
| | | Unearned guest and host fees | Guest funds held | €217.60 |
| 2 Feb, 13:05 | Host cancellation fee (10% of nightly subtotal) | Carmen receivable | Host cancellation fee income | €130.00 |

The **€420** that Nookaway paid to rebook the Bauers in a comparable apartment is a guarantee expense of Nookaway's own and never touches Carmen's accounts; [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) owns that flow. Carmen's next stay was a three-night booking at her usual €110, checking in on 13 February: a subtotal of €390, a host fee of €15.60 and a pending payable of **€374.40**. When the release rule fired 48 hours after the scheduled check-in, the payout engine netted the open receivable:

| Time | Event | Debit | Credit | Amount |
| --- | --- | --- | --- | --- |
| 15 Feb | Release rule fires | Carmen payable – pending | Carmen payable – available | €374.40 |
| 15 Feb | Deduction applied | Carmen payable – available | Carmen receivable | €130.00 |
| 15 Feb | Payout sent (SEPA credit transfer) | Carmen payable – available | Payout in transit | €244.40 |
| 16 Feb | Bank confirms | Payout in transit | Safeguarded cash | €244.40 |

Carmen's February statement now shows four lines with references to both reservations, and the support agent's forty-minute investigation becomes a link. The same structure makes the €3.4 million of host debit balances a set of dated receivables in Fathom, so finance can age them, provision for them and decide a write-off policy instead of re-deriving them every night.

![Waterfall from €374.40 minus €130 to €244.40, beside a four-line statement.](stays-marketplace-architecture/posts/28-payouts-and-settlement/assets/images/28-payouts-and-settlement/28-why-244-40.jpeg)

**Figure 4:** *Carmen's €244.40 payout is her €374.40 payable less the €130 host cancellation fee; with both in Fathom, one statement explains it instead of three systems.*

{id: payouts-and-settlement--the-novaks-booking-with-a-split-payout}
### The Novaks' booking with a split payout

The Novak family's Alfama apartment shows the hosted-stays design at its fullest. On 14 February 2027 they paid **€1,271.20** for 2–9 August: a €1,085 subtotal (seven nights at €145 plus €70 cleaning), the 12% guest service fee of €130.20 and €56 of Lisbon tourist tax. The 4% host fee on the subtotal is €43.40, so the host side is owed **€1,041.60**, held for almost six months in Corvane Payments' safeguarded accounts.

Suppose, as an illustration of the split-payout design Corvane plans for 2028, that the apartment's owner uses a local property manager as co-host, under a split agreed in Nookaway: the manager receives the cleaning fee and 20% of the accommodation payout, both net of their share of the host fee.

| Line | Owner | Manager | Total |
| --- | --- | --- | --- |
| Nightly subtotal €1,015 less 4% host fee (€40.60) | €779.52 (80%) | €194.88 (20%) | €974.40 |
| Cleaning fee €70 less 4% host fee (€2.80) | — | €67.20 | €67.20 |
| **Payable, released 4 August** | **€779.52** | **€262.08** | **€1,041.60** |

The €56 of tourist tax is posted to a tax-collected liability for Lisbon, not to either payable, and the €173.60 of guest and host fees moves from unearned to earned at check-in on 2 August. Each payee has its own Fathom account, its own verified account in the beneficiary registry and its own line in the DAC7 report. Before the design, the full €1,041.60 went to the owner, who paid the manager off-platform, and the manager's income was invisible to Nookaway's reporting.

{id: payouts-and-settlement--hotel-prinsenkade-s-april-statement}
### Hotel Prinsenkade's April statement

Hotel Prinsenkade has a 15% commission in its Roomstead contract and takes both agency and merchant bookings. Its April 2027 activity, in the target design, produces one statement:

| Line | Room nights | Amount | Effect on balance |
| --- | --- | --- | --- |
| Agency stays departed in April, room revenue €214,200 | 1,020 | Commission 15%: **€32,130.00** | Receivable from hotel |
| Merchant stays in April, guest-paid room revenue €92,880 | 430 | Net to hotel 85%: **€78,948.00** | Payable, settled by 151 virtual cards |
| King's Day relocation recovery, 4 reservations, 27 April | — | **€1,600.00** | Receivable from hotel |
| **Net position for April** | | **€45,218.00 owed to the hotel** | If netted by bank transfer |

Taxes are left out of the table; Amsterdam's tourist tax and VAT on the commission belong to [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays). The point is the last line. Paid by virtual cards, the hotel received the full €78,948 card by card and owed **€33,730** on two invoices, one of which it disputed because it could not trace it. Paid by weekly net bank transfer, the recovery and commission are deducted as they arise and the hotel receives €45,218 with a statement that explains every euro. Roomstead will offer net bank transfer to partners from 2028 and will keep virtual cards for hotels that prefer card acceptance. For partners that stay on cards, the statement still shows both directions, and the invoice references the reservations it covers. Commission invoicing moves out of Keystone into a service that reads Fathom, ahead of the reservation module's retirement at the end of 2029.

![Left: many card payments of €78,948 to the hotel and two invoices of €33,730 back. Right: one netted transfer of €45,218 with a statement.](stays-marketplace-architecture/posts/28-payouts-and-settlement/assets/images/28-payouts-and-settlement/28-prinsenkade-netting.jpeg)

**Figure 5:** *Paid by virtual cards, Hotel Prinsenkade received €78,948 and owed €33,730 on two invoices; netted by bank transfer, it receives €45,218 with one statement.*

{id: payouts-and-settlement--what-corvane-measures}
### What Corvane measures

The forum agreed five settlement metrics, each computed from Fathom rather than from any one brand's tables:

| Metric | Definition | Why |
| --- | --- | --- |
| **Time to payout** | Scheduled check-in to funds confirmed at the beneficiary's bank, p50 and p95 | The host's experience of the product |
| **Payout return rate** | Payouts returned or rejected by the receiving side, per rail | Beneficiary data quality; 0.65% of Nookaway payouts in 2026, about 41,000 |
| **Explained-payout rate** | Payouts whose amount equals the sum of their statement lines | Catches posting gaps before partners do |
| **Debit balance aging** | Partner receivables by age bucket and recovery path | The €3.4 million problem |
| **Commission days sales outstanding** | Average days from invoice to payment, and share over 90 days | Agency collection risk; 2.6% of 2026 commission, about €22 million, was over 90 days at year-end |

{id: payouts-and-settlement--trade-offs}
## Trade-offs

Four decisions shape every settlement design. None has one right answer.

| Decision | Option | When it is right | What it costs |
| --- | --- | --- | --- |
| **Release timing (hosted stays)** | At booking | Never for stays: the platform loses its leverage over a stay that has not happened | Recovery from hosts after every cancellation |
| | Shortly after scheduled check-in | Established hosts; the common hosted-stays norm | Chargebacks and claims arrive after payout; needs recovery by deduction |
| | After check-out | New hosts, high-risk segments | Slower host cash flow; weaker supply acquisition |
| | Monthly in arrears | Long stays, corporate housing | Long float; host experience suffers |
| **Rail to hotels (merchant)** | Virtual card per booking | Hotels without integration; card-acceptance routines; platform earns card economics | Card fees borne by hotel; card lifecycle tracking; no netting |
| | Net bank transfer | Hotels with mixed agency and merchant bookings | Bank details and KYB required; transfer returns to handle |
| **Commission collection (agency)** | Invoice and transfer | Default for established hotels | Collection risk; dunning work |
| | Direct debit or card on file | Small properties; high-volume partners | Mandate management; failed debits |
| | Netting against merchant payouts | Partners on both models | Requires one ledger for both directions |
| **Ledger ownership** | Payments-provider balances (Stripe Connect, Adyen for Platforms) | Smaller marketplaces; no payment license | Provider's model of splits, holds and reporting; harder to leave |
| | Own settlement ledger, provider as rail | Licensed or large marketplaces; several providers; two marketplace types | Build and operate a financial system with audit duties |

On the last row, I would rent the ledger until a marketplace holds a payments license or needs one view across several providers, both settlement directions or several brands, which is Corvane's position, and own it after. Until then, insist that the provider exports line-level data a future ledger could import.

{id: payouts-and-settlement--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (OTA-style) | Hosted-stays marketplace |
| --- | --- | --- |
| **Payee** | Businesses: hotels, chains, property managers, with finance staff | Individuals and small managers, often without a business identity |
| **Direction** | Both: payables (merchant) and receivables (agency commission) | Almost only payables, plus receivables from deductions |
| **Timing** | At check-in or check-out via card activation; transfers weekly or monthly; supplier terms commonly up to 30 days after stay | Shortly after scheduled check-in, per reservation |
| **Rails** | Virtual cards, bank transfer, direct debit for commission | Bank transfer, card push, wallets; instant euro transfers |
| **Documents** | Commission invoices and credit notes, remittance advice, VAT reverse charge | Earnings statements, annual tax summaries, DAC7 notices |
| **Verification** | KYB on legal entities; bank account ownership | KYC on individuals; tax identity per payee; co-host verification |
| **Main risk** | Commission not paid; virtual cards charged after cancellation | Payout before chargeback or claim; account takeover cash-out; debit balances that never recover |
| **Delegation** | Multi-user partner accounts with finance roles | Owners, co-hosts and cleaners as separate beneficiaries with split rules |
| **Regulatory pressure** | Commission VAT; payment licensing where merchant | Payment licensing, safeguarding, DAC7, platform withholding regimes |
| **What can be shared** | Settlement ledger, beneficiary registry, payout rails, statement engine | Same |

The ledger, the beneficiary registry and the rail adapters should be shared: a payable is a payable whether it belongs to a 140-room hotel or a two-bedroom apartment, and two ledgers recreate the reconciliation problem this chapter exists to remove. The **release policy**, the **statement format** and the **collection process** should not be shared: a host needs a phone-sized earnings view and a payout two days after check-in, while a hotel's controller needs a monthly statement and an invoice that fits an accounts-payable process. Convergence makes the shared core more valuable: when Nookaway pilots boutique hotels in 2028, those hotels need invoices and VAT documents, and when Roomstead sells apartments from individual owners, those owners need host-style payouts and tax-identity gates. Both are configuration on a shared ledger and impossible on two separate ones. [One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces) makes the wider argument.

{id: payouts-and-settlement--failure-modes}
## Failure Modes

- **Balances derived from bookings.** The payout amount is recomputed from the current booking state each night. Any alteration after payout silently changes history, and nobody can say what was paid against which version. *Fix:* post every change as an entry; never compute a balance from a mutable booking.
- **Deductions with no ledger home.** Cancellation fees, recoveries and clawbacks live in a "pending deductions" table or in a support tool, applied by whichever payout runs next. They are applied twice, or never, and debit balances are invisible. *Fix:* deductions are receivables with a recovery rule and an age.
- **Holds as payout flags.** A hold stops a whole payout, so a trust team either over-blocks honest income or does not block at all. Holds without an expiry and an owner accumulate until hosts complain publicly. *Fix:* holds on balances, with reason codes, owners and expiry, as part of the trust platform's enforcement actions ([Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety)).
- **Non-idempotent payout runs.** A run that times out is retried and pays twice; Roomstead's 212 duplicate bookings from a retried checkout without its idempotency key ([Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration)) show the same mistake on the pay-in side. *Fix:* one payout instruction per beneficiary, currency and run, with a key the rail sees, and a ledger entry before the instruction leaves.
- **Returns as tickets.** Returned transfers go to an email inbox. The money sits in a bank account no system attributes to anyone, and the host is told their payout was sent. *Fix:* rail adapters post returns to the ledger; the beneficiary sees a task to fix the account.
- **Virtual cards outliving their bookings.** Modifications and cancellations do not resize or void cards, so hotels charge amounts no longer owed. *Fix:* the card lifecycle follows the reservation lifecycle through events, and unsettled card balances are reconciled daily.
- **Statements computed separately from the ledger.** The partner portal, the PDF and the finance report each add up their own numbers and disagree by a few euros. *Fix:* statements are a query on ledger entries with a closing balance that matches the ledger.
- **Bank-detail changes paid immediately.** An attacker who takes over a host or partner account changes the bank account and waits for the next run. *Fix:* step-up authentication, a cooling-off hold for new accounts and payee verification.

{id: payouts-and-settlement--the-chief-architect-s-view}
## The Chief Architect's View

In settlement, architecture decisions are also accounting, legal and risk decisions. These are the ones I would make explicitly, and who should make them.

- **Name the system of record for partner balances.** One settlement ledger, owned by the payments and finance engineering team, with brand platforms as event producers. This is a decision for the Group Chief Architect and the CFO together, because it changes what the auditors test.
- **Make posting rules and release rules reviewed configuration.** Fee and commission rules belong to the commercial owners; release and hold rules belong to risk; posting rules belong to finance. Each has an owner, a version and a change process, and engineering implements them as data. [Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html) describes how to run posting rules as approved configuration.
- **Define the partner as a beneficiary graph, not an account.** Owners, operators, co-hosts, chain head offices and management companies are paid and reported separately. Model this before the first split-payout request, because retrofitting it touches tax reporting and identity at once.
- **Decide the collection policy for agency commission as a product decision.** Netting, direct debit and suspension for non-payment change partner relationships. Engineering provides the ledger, aging and the hooks; commercial leadership owns the policy.
- **Keep payout rails behind adapters.** Banks, payments providers and card issuers will change, and instant rails will replace batch files. The ledger and payout engine must not know the rail's file format.
- **Watch the five settlement metrics** above; a drift in any of them is an early sign of a posting gap.

The long-term consideration is regulatory. Platform withholding and reporting regimes, such as DAC7 and the deemed-supplier VAT rule for short-term accommodation that the EU's "VAT in the digital age" package introduces between 2028 and 2030, all assume that the platform knows exactly what it paid to whom for which property. A marketplace with one settlement ledger can add a new regime as postings and reports; a marketplace without one adds another special case. That is how The Tax Patchwork begins, and [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays) picks up the story.

{id: payouts-and-settlement--questions-to-ask}
## Questions to Ask

1. If a host or hotel asks why their last payout was a particular amount, how many systems does an agent need to open, and how long does it take?
2. Where do deductions such as cancellation fees, recoveries and clawbacks live, and what is the total debit balance today, by age?
3. Is a hold a state on a balance with a reason, an owner and an expiry, or a flag on a payout?
4. For a partner with both agency and merchant bookings, is there one statement and one balance, and can commission be netted?
5. Is the commission invoice built from departed stays after no-show reporting closes, and are corrections credit notes?
6. Who is paid for a listing run by an owner and a co-host, and who appears in the DAC7 report?
7. What happens between a bank-detail change and the next payout, and does the payout engine use payee verification?
8. If a payout run times out halfway, how do you know which beneficiaries were paid, and what stops the retry from paying them twice?
9. If the release rule changed from 48 hours after check-in to 24, which components would change? (The answer should be: configuration, and nothing else.)

With money reaching the supply side through one ledger, the next question is how much of it belongs to neither the platform nor the partner. Tourist taxes, VAT on stays and commissions, withholding and platform reporting run through every posting in this chapter, and [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays) turns them from special cases into a tax engine.

{id: payouts-and-settlement--sources-and-evidence}
## Sources and Evidence

*Company engineering and investor sources*

- [Airbnb, Inc. Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), Airbnb / SEC EDGAR, 2026: funds held on behalf of customers, unearned fees, chargeback expense, move to host-only fees from October 2025.
- [Booking Holdings Inc. Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), Booking Holdings / SEC EDGAR, 2026: agency revenue definition and size, deferred merchant bookings.
- [Expedia Group Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm), Expedia Group / SEC EDGAR, 2026: guest choice between Expedia Collect and Hotel Collect; supplier payment terms.
- [Measuring Transactional Integrity in Airbnb's Distributed Payment Ecosystem](https://medium.com/airbnb-engineering/measuring-transactional-integrity-in-airbnbs-distributed-payment-ecosystem-a670d6926d22), Airbnb Engineering, 2018: batch payouts and out-of-sync windows; at least two transactions per booking.
- [Rebuilding Payment Orchestration at Airbnb](https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b), Bryon Ross et al., Airbnb Engineering, 2022: idempotent workflow steps, append-only versions for alterations, bill-centered data model.
- [Pay as a Local](https://airbnb.tech/payments/pay-as-a-local/), Gerum Haile et al., Airbnb Engineering, 2026: Payout, Ledger and Settlement & Reconciliation subdomains.
- [Airbnb 2024 Winter Release: Co-Host Network](https://news.airbnb.com/en-uk/airbnb-2024-winter-release-introducing-co-host-network-the-best-local-hosts-to-manage-your-airbnb), Airbnb Newsroom, 2024: co-hosts sharing payouts; network size at launch.
- [Airbnb Q2 2025 shareholder letter](https://www.sec.gov/Archives/edgar/data/1559720/000119312525174438/d17531dex991.htm), Airbnb / SEC EDGAR, 2025: Co-Host Network supporting over 100,000 listings.
- [Agoda Growth Program](https://www.partnerhub.agoda.com/?p=95313), Agoda Partner Hub, 2025: commission deducted from payouts or invoiced monthly on departed room nights.

*Standards, regulation and documentation*

- [Payments Terms of Service](https://www.airbnb.com/help/article/2909) and [Payments Terms of Service for European Users](https://www.airbnb.ie/help/article/2909), Airbnb, 2026: payout timing after scheduled check-in, new-host rule, holds, recovery from future payouts.
- [Terms of Service](https://www.airbnb.com/help/article/2908), Airbnb, 2026: payouts withheld for insufficient tax documentation.
- [When you'll get your payout](https://www.airbnb.com/help/article/425), Airbnb Help Center, n.d. (fetched October 2026): arrival times by method; fraud review of up to 45 days.
- [Airbnb Help Center article 1237 on identity verification](https://www.airbnb.com/help/article/1237), Airbnb, n.d. (fetched October 2026): verification of hosts, co-hosts and guests.
- [Understanding payouts (Payments by Booking.com onboarding API)](https://developers.booking.com/connectivity/docs/payments-by-booking-onboarding-api/understanding-payouts), Booking.com Developers, n.d. (fetched October 2026): payout rails, gross and net payouts, virtual-card activation policies, Know Your Partner.
- [Payments by Booking.com](https://partner.booking.com/en-gb/solutions/payments-bookingcom), Booking.com for Partners, n.d. (fetched October 2026): mixed model with monthly invoice; virtual-card chargeability.
- [How we work](https://www.booking.com/content/how_we_work.html), Booking.com, 2025: commission paid after the stay.
- [Understand how charges work in a Connect integration](https://docs.stripe.com/connect/charges), Stripe, n.d.: destination charges, separate charges and transfers, who absorbs refunds and disputes.
- [Marketplaces](https://docs.adyen.com/marketplaces/), Adyen Docs, n.d.: split payments, holds until payout, seller verification.
- [Council Directive (EU) 2021/514 (DAC7)](http://publications.europa.eu/resource/celex/32021L0514), Council of the EU, 2021: platform reporting of property rentals from 2023.
- [Regulation (EU) 2024/886 on instant credit transfers in euro](http://publications.europa.eu/resource/celex/32024R0886), European Parliament and Council, 2024: verification of the payee and instant sending by 9 October 2025 in the euro area; bulk opt-out for non-consumers.

*Research and practitioner sources*

- [Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html) and [Payments-to-Ledger: Draining the Suspense Swamp](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-to-ledger.html), RECONCILED, 2026: posting rules, reversals, clearing accounts and three-way matching that this chapter assumes.
- BOOKED research briefs on payments, finance and tax, and on hosts, partners and guest service, 2026 (internal): synthesis of the reference account model and the co-host beneficiary model.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
