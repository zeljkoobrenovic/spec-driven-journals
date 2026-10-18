# Research brief: Payments for finance architects (fundamentals, Adyen, Stripe, multi-PSP)

Prepared 18 October 2026 for chapter writers of *Enterprise Architecture and Financial Systems*. Vendor-neutral; Adyen and Stripe are documented because they are the two most common enterprise PSPs and both publish unusually detailed reconciliation documentation, not because the book endorses either.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url]**: checked against the cited page during this research session (October 2026). Paraphrases are close to the source; quoted text is quoted.
- **[WIDELY REPORTED: url]**: from a reputable secondary source or vendor marketing, not from primary documentation or regulation.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's synthesis. It was not checked against a primary source in this session. Chapter writers should re-verify it before printing it as fact, or present it explicitly as an architectural judgement.

**Research limitation.** The session's web-search quota ran out partway through. Topics researched after that point (Pix, UPI, BNPL, DCC mechanics, scheme-level reason-code numbering, network-token economics, Adyen's IPO details, the iDEAL→Wero migration dates) rely on direct fetches of known URLs. Where those fetches returned nothing useful, the claim is tagged ASSUMPTION/JUDGEMENT. Do not upgrade these tags without checking the source.

**Volatility flags.** ⚠ marks claims that are likely to change within 12 months. Examples are product preview status, regulatory adoption dates and API version names.

---

## PART 1: Payments fundamentals for finance architects

### 1.1 The parties

| Party | Role | Finance-architecture relevance |
| --- | --- | --- |
| Cardholder | Pays; can dispute | Source of disputes months after the sale |
| Issuer | Bank that issued the card. Authorises, receives interchange, raises chargebacks | Interchange is paid *to* the issuer |
| Acquirer | Bank or licensed institution that contracts the merchant, receives funds from the scheme and pays the merchant | Legal counterparty for settlement funds |
| Card scheme / network | Visa, Mastercard, Amex, etc. Sets rules, routes authorisation and clearing, charges scheme fees | Rules drive dispute windows and authorisation validity |
| PSP | Packages gateway, acquiring (own or third-party), risk, payment methods and reporting | Your primary data source for reconciliation |
| Gateway | Technical routing of payment requests only; no funds flow | Technically a single point of failure; holds no money |
| Payment facilitator (PayFac) | Master merchant that onboards sub-merchants under its own acquiring relationship | Platform carries KYC and loss liability |
| Merchant of record (MoR) | Entity whose name is on the cardholder statement. Carries the legal sale, tax, refunds and chargebacks | Determines who books revenue gross vs net, and who owns tax |
| Payment orchestrator | Abstraction layer over multiple PSPs/acquirers: routing, retries, vault, normalised data | Adds a normalisation layer *before* the ledger |

[ASSUMPTION/JUDGEMENT] The table is standard industry vocabulary. Exact legal definitions differ by jurisdiction and contract. In particular, "PSP" is a regulatory term in the EU (PSD2) and a commercial term elsewhere. Stripe's Connect docs use "business of record" for the `on_behalf_of` concept rather than "merchant of record" [VERIFIED: https://docs.stripe.com/connect/charges].

### 1.2 Card payment lifecycle

1. **Authorisation.** The issuer approves and places a hold on the cardholder's open-to-buy. No money moves. [ASSUMPTION/JUDGEMENT]
2. **Authentication (3DS2 / SCA).** In the EEA, PSD2's RTS requires strong customer authentication. SCA means two or more elements from different categories (knowledge, possession, inherence), producing a one-time authentication code [VERIFIED: https://eur-lex.europa.eu/eli/reg_del/2018/389/oj]. For remote payments the code must be *dynamically linked* to amount and payee. Any change to either invalidates it (Art. 5) [VERIFIED: same]. Exemptions that matter architecturally [VERIFIED: same]:
   - **Low value (Art. 16):** ≤ EUR 30, provided the cumulative total since the last SCA stays ≤ EUR 100 or the count stays ≤ 5 consecutive transactions.
   - **Transaction risk analysis (Art. 18):** thresholds of EUR 100 / 250 / 500, tied to the PSP's card fraud rates of 0.13% / 0.06% / 0.01%.
   - **Recurring same-amount, same-payee series (Art. 14).** SCA applies on the first payment only.
   - **Trusted beneficiaries (Art. 13).**
   - **Secure corporate payment processes (Art. 17).**
   - [WIDELY REPORTED / ASSUMPTION] Merchant-initiated transactions are treated as outside SCA scope rather than exempt. That treatment comes from EBA Q&A guidance, not the RTS text. Verify against the EBA Q&A before stating it.
   - Liability shift: Stripe documents that 3DS-authenticated payments can still be disputed, and that it supplies 3DS evidence automatically [VERIFIED: https://docs.stripe.com/disputes/how-disputes-work].
3. **Capture.** The merchant instructs that the authorised amount (or less) be collected. Capture can be immediate, delayed or partial.
   - Authorisations expire. Stripe documents CNP windows of 7 days for Mastercard/Amex/Discover, and 7 days (CIT) or ~5 days (MIT; exactly 4 days 18 hours) for Visa. Card-present windows are mostly 2 days [VERIFIED: https://docs.stripe.com/payments/place-a-hold-on-a-payment-method].
   - A partial capture releases the remainder unless multicapture is enabled [VERIFIED: same]. Adyen behaves the same way: the unclaimed remainder is cancelled automatically, and multiple partial captures are "disabled by default" [VERIFIED: https://docs.adyen.com/online-payments/capture].
4. **Clearing.** Captured transactions are submitted to the scheme in batches and matched to authorisations. Interchange and scheme fees are determined at this stage. [ASSUMPTION/JUDGEMENT]
5. **Settlement.** The scheme nets positions between issuers and acquirers, and funds move issuer → scheme → acquirer. [ASSUMPTION/JUDGEMENT]
6. **Funding / payout.** The acquirer or PSP pays the merchant *net* of fees, refunds, chargebacks and reserve movements.
   - Adyen pays out per "payable batch". If the batch's payable balance is positive when it closes, Adyen instructs a payout [VERIFIED: https://docs.adyen.com/account/getting-paid].
   - Stripe pays out from the "available" balance on a schedule [VERIFIED: https://docs.stripe.com/payouts].

**Key architectural point:** an "order paid" event in commerce systems is usually an *authorisation* or *capture*. Cash arrives days later, as part of a net batch amount. [ASSUMPTION/JUDGEMENT]

### 1.3 Pricing: interchange, scheme fees, acquirer markup

- **Interchange:** paid by the acquirer to the issuer. In the EU, the Interchange Fee Regulation (EU) 2015/751 caps consumer debit at **0.2%** (Art. 3) and consumer credit at **0.3%** (Art. 4). Member States may set lower domestic caps. **Commercial cards are excluded** from these caps (Art. 1(3)(a)) [VERIFIED: https://eur-lex.europa.eu/eli/reg/2015/751/oj]. ⚠ The UK has separate post-Brexit rules. Interchange on UK-issued cards used at EEA merchants (CNP) is a known exception that is not covered here [ASSUMPTION/JUDGEMENT].
- **Scheme fees:** charged by the network to both issuer and acquirer. They are numerous and opaque. [ASSUMPTION/JUDGEMENT]
- **Acquirer/PSP markup:** the processor's margin.
- **Interchange++ (IC++):** passes interchange and scheme fees through at cost and adds an explicit markup.
  - Adyen's public pricing shows Visa/Mastercard at "$0.13 + Interchange++ + 0.60%". It describes IC++ as a model that "accurately tracks Interchange rates and scheme fees" [VERIFIED: https://www.adyen.com/pricing]. ⚠ The listed prices are indicative; Adyen says custom pricing is available.
  - Adyen's settlement report splits "Commission" into **Markup**, **Scheme Fees** and **Interchange** columns when interchange-level data is available. Otherwise only Commission is populated [VERIFIED: https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report].
- **Blended pricing:** a single percentage plus a fixed fee per transaction. Simpler to forecast, but it hides cost drivers. [ASSUMPTION/JUDGEMENT]
- **Finance implication:** under IC++ the fee for a transaction may only be known at clearing, and some scheme fees arrive later on invoices. Adyen's Payment accounting report exists explicitly to "match fees to payment statuses and perform invoice reconciliation" [VERIFIED: https://docs.adyen.com/reporting/invoice-reconciliation/payment-accounting-report]. Fee accruals therefore need a true-up process.

### 1.4 Alternative payment methods (APMs)

| Method | Nature | Status notes |
| --- | --- | --- |
| Wallets (Apple Pay, Google Pay, PayPal) | Apple/Google Pay are tokenised cards (card rails). PayPal is its own stored-value/acquiring network | [ASSUMPTION/JUDGEMENT] |
| iDEAL (NL) → "iDEAL \| Wero" | Bank-redirect, account-to-account | The iDEAL site now brands the product "iDEAL \| Wero" and describes it as "an online payment method that allows consumers to pay via their own bank" [VERIFIED: https://www.ideal.nl/en/]. EPI says Wero launched in Belgium, France and Germany in 2024, with the Netherlands and Luxembourg next [VERIFIED: https://epicompany.eu/]. ⚠ No migration timeline could be verified; do not print one without a primary source. |
| Pix (Brazil) | Central-bank-operated instant payments | [ASSUMPTION/JUDGEMENT] Operated by Banco Central do Brasil, launched November 2020, 24/7. The BCB page fetch returned no content. Verify at bcb.gov.br before printing. |
| UPI (India) | NPCI-operated real-time account-to-account | Operator is NPCI [VERIFIED: https://www.npci.org.in/what-we-do/upi/product-overview]. Launch year (2016) and features are [ASSUMPTION/JUDGEMENT]. |
| BNPL (Klarna, Afterpay, Affirm) | Lender pays the merchant; consumer repays the lender | Authorisation windows differ. On Stripe, Klarna must be captured by midnight of the 28th day, Afterpay within 13 days, and Affirm within 30 days [VERIFIED: https://docs.stripe.com/payments/place-a-hold-on-a-payment-method] |
| Bank transfers / SEPA Credit Transfer / SEPA Instant | Push payments | EU Instant Payments Regulation (EU) 2024/886: euro-area PSPs must *receive* instant credit transfers by 9 Jan 2025 and *send* them, with Verification of Payee, by 9 Oct 2025. Payment and e-money institutions must comply by 9 Apr 2027. Non-euro Member States follow from 9 Jan 2027 (receive) and 9 Jul 2027 (send/VoP) [VERIFIED: https://eur-lex.europa.eu/eli/reg/2024/886/oj] |
| Direct debit (SEPA DD, ACH) | Pull payments with long return windows | Stripe settles ACH Debit in 4 business days and SEPA DD in 6 [VERIFIED: https://docs.stripe.com/payouts]. Some methods cannot be separately authorised and captured (ACH, iDEAL) [VERIFIED: https://docs.stripe.com/payments/place-a-hold-on-a-payment-method] |
| Open banking (PSD2 PIS/AIS) | API-initiated bank payments and account data | Stripe Financial Connections offers account data (balances, ownership, transactions) for US bank accounts. ⚠ The docs list availability to businesses in the US, UK, EEA countries and Switzerland, "for use with US bank accounts" [VERIFIED: https://docs.stripe.com/financial-connections] |

**Finance implication:** APMs differ in when the payment becomes final, whether it can be refunded or disputed, and settlement delay. Each payment method needs its own cash-recognition and receivable-ageing rules. [ASSUMPTION/JUDGEMENT]

### 1.5 Tokenisation and network tokens

- **PSP tokens** (vault tokens) stand in for a PAN within one PSP. **Network tokens** are issued by the scheme (e.g. Visa Token Service, Mastercard MDES). They are bound to a merchant/token-requestor and updated by the scheme when the card is reissued. [ASSUMPTION/JUDGEMENT]
- Claimed benefits are higher approval rates, fewer failed recurring payments and lower fraud. [ASSUMPTION/JUDGEMENT] The Adyen and Stripe network-token doc URLs tried in this session returned 404, so treat specific uplift percentages as vendor marketing.
- **Portability:** PSP tokens are not portable between PSPs. Network tokens are requested by a token requestor (often the PSP). Migrating them requires the scheme and both PSPs to cooperate. This is one reason orchestration vendors sell "merchant-owned" vaults (§4) [ASSUMPTION/JUDGEMENT]. Spreedly describes its vault as one "the merchant owns", usable with any provider [WIDELY REPORTED: https://www.spreedly.com/].

### 1.6 Refunds

- A refund is a new money movement that can fail or be returned. Adyen journals **Refunded**, **RefundedReversed** (refund returned because it could not be credited) and, for Sales day payout, **RefundNotCleared** [VERIFIED: https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report].
- Stripe has `refund`, `refund_failure` and `payment_refund` balance transaction types [VERIFIED: https://docs.stripe.com/api/balance_transactions/object].
- Stripe can create *pending* refunds when the balance is insufficient. They process automatically when funds arrive [VERIFIED: https://docs.stripe.com/connect/charges].
- Cancelling an uncaptured authorisation (a "void" or "cancel") is not a refund: no money moved. Adyen's `cancelOrRefund` covers both cases [ASSUMPTION/JUDGEMENT; Adyen glossary URL returned 404].

### 1.7 Chargebacks / disputes lifecycle

- **Window:** "Card networks typically allow cardholders to initiate disputes within 120 days of the original payment". For future-dated services the window can start at the event date [VERIFIED: https://docs.stripe.com/disputes/how-disputes-work]. LPMs such as Klarna/PayPal "typically allow customers up to 180 days" [VERIFIED: same].
- **Response window:** merchants usually have 7–21 days to respond. The issuer then takes 60–75 days to decide, so the full lifecycle "can take 2-3 months" [VERIFIED: same].
- **Stages (Adyen vocabulary):** Request for Information → Notification of Chargeback (starts the defence period) → Chargeback (funds debited) → Information Supplied → Chargeback Reversed → (Pre-arbitration) → (Scheme Arbitration; a loss can add a fee of up to USD 600) → Second Chargeback [VERIFIED: https://docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow].
- **Webhook event codes (Adyen):** `NOTIFICATION_OF_CHARGEBACK`, `CHARGEBACK`, `CHARGEBACK_REVERSED`, `SECOND_CHARGEBACK`, `PREARBITRATION_WON`, `PREARBITRATION_LOST` [VERIFIED: same].
- **Stripe specifics:** Stripe debits the disputed amount *plus a dispute fee* from the balance.
  - The dispute-received fee is generally non-refundable outside Mexico. A separate "dispute countered fee" is returned if you win [VERIFIED: https://docs.stripe.com/disputes/how-disputes-work].
  - Inquiries (retrievals/RFIs) are mostly used by Amex and Discover; "Mastercard and Visa no longer use it" [VERIFIED: same].
  - Stripe "doesn't support the arbitration phase" [VERIFIED: same].
  - "Late win" status changes can occur outside the normal lifecycle [VERIFIED: same].
- **Disputed amount ≠ original amount:** FX movement between sale and dispute, aggregated recurring disputes, partial disputes, and disputes on partially refunded charges [VERIFIED: same].
- **Early fraud warnings** (Visa TC40, Mastercard SAFE) are informational. Stripe states that ~40% of Visa/Mastercard EFWs become fraud disputes if not refunded [VERIFIED: same].
- **Reason codes:** schemes publish reason codes by category. [ASSUMPTION/JUDGEMENT] Visa groups them as 10 Fraud, 11 Authorisation, 12 Processing Errors and 13 Consumer Disputes; Mastercard uses 48xx numeric codes. Adyen's reason-code page organises codes by dispute event (Chargeback, RFI, Notification of Fraud) and by scheme, without a cross-scheme taxonomy [VERIFIED: https://docs.adyen.com/risk-management/understanding-disputes/dispute-reason-codes]. Writers should not print specific code numbers without checking current scheme rules.

### 1.8 Reserves and rolling reserves

- Adyen journal types include **DepositCorrection** (security deposit changes), **MerchantPayin** (funding the Reserve), **ReserveAdjustment** (funds withheld or released because of Reserve funding or usage) and **Balancetransfer** (to/from later payout batches to cover negative balances) [VERIFIED: https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report].
- Stripe balance transaction types include `reserve_hold`, `reserve_release`, `reserved_funds`, `reserve_transaction`, `payment_network_reserve_hold/release` and `payout_minimum_balance_hold/release`. There is a `risk_reserved` balance type [VERIFIED: https://docs.stripe.com/api/balance_transactions/object].
- **Finance implication:** reserved funds belong to the merchant but are restricted. They should be booked as a separate receivable/restricted-cash sub-ledger, not netted into sales. [ASSUMPTION/JUDGEMENT]

### 1.9 FX: multi-currency pricing and DCC

- **Multi-currency pricing (presentment currency ≠ settlement currency):** the PSP converts at its rate plus a margin. Stripe exposes `exchange_rate` on the balance transaction: "amount in currency A, multiplied by the exchange_rate, equals the amount in currency B" [VERIFIED: https://docs.stripe.com/api/balance_transactions/object]. There is a separate `stripe_fx_fee` type [VERIFIED: same].
- Adyen's settlement report carries Gross (transaction currency), Net (settlement currency) and an **Exchange Rate** column. For externally settled payments it is "Adyen's reference rate, not the acquirer's actual rate" [VERIFIED: https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report].
- **DCC (Dynamic Currency Conversion):** the cardholder chooses to pay in their home currency at the point of sale. The merchant/acquirer earns the FX margin. [ASSUMPTION/JUDGEMENT] In the EU, DCC disclosure rules apply under Regulation (EU) 2019/518 [ASSUMPTION/JUDGEMENT]. Adyen's aggregate report nets "DCC markup" out of Settled amounts [VERIFIED: https://docs.adyen.com/reporting/settlement-reconciliation/batch-level/aggregate-settlement-details-report].
- **Revenue implication:** Stripe Revenue Recognition books FX differences between invoice finalisation and payment to an **FxLoss** account. It uses "the exchange rate for the actual money movement (that is, reflected on the balance transaction)" [VERIFIED: https://docs.stripe.com/revenue-recognition/methodology].

### 1.10 Payouts to sellers/partners and marketplace models

- **Three structural models** [ASSUMPTION/JUDGEMENT]:
  1. **Platform as MoR.** The platform sells, books gross revenue and pays sellers as suppliers.
  2. **Seller as MoR, facilitated by the platform.** The platform takes a commission (net revenue). This is a PayFac/marketplace structure.
  3. **Pure SaaS.** Sellers have their own merchant relationship and the platform takes an application fee.
- Stripe Connect maps to these:
  - **Direct charges:** payment on the connected account; refunds and chargebacks hit the connected account. The platform earns an application fee.
  - **Destination charges:** charge on the platform with an immediate transfer. Refunds and chargebacks hit the platform; Stripe fees are debited from the platform.
  - **Separate charges and transfers:** decoupled, one-to-many; the platform's balance is debited for fees, refunds and chargebacks.

  All three are [VERIFIED: https://docs.stripe.com/connect/charges].
- Adyen for Platforms: payments settle into balance accounts, and "You define how each payment is split between your liable balance account and the user's balance accounts" [VERIFIED: https://docs.adyen.com/platforms/account-structure-resources/platform-structure].
- **Accounting judgement:** principal vs agent (IFRS 15 / ASC 606) determines gross vs net revenue. The payment flow is evidence for that judgement but does not settle it. Chapter writers should keep the legal/contractual MoR question separate from the funds-flow choice. [ASSUMPTION/JUDGEMENT]

### 1.11 ISO 20022 for bank payments

- [ASSUMPTION/JUDGEMENT] ISO 20022 is the XML-based financial messaging standard. The core corporate messages are `pain.001` (credit transfer initiation), `pain.008` (direct debit initiation), `pacs.008` (interbank customer credit transfer), `camt.053` (end-of-day statement), `camt.054` (debit/credit notification) and `camt.052` (intraday report).
- [ASSUMPTION/JUDGEMENT ⚠] SWIFT's MT/MX coexistence period for cross-border payments (CBPR+) was scheduled to end in November 2025, with structured/hybrid postal address requirements following in November 2026. The swift.com FAQ returned HTTP 403, so verify both dates at swift.com before printing.
- **Why it matters for reconciliation:** `camt.053/054` carries structured remittance and end-to-end IDs. Richer bank statements improve cash application for PSP payouts. Matching relies on the PSP's payout reference (Adyen: the payout reference on the MerchantPayout entry; Stripe: `trace_id` / `payout_reference_token`) appearing in the bank statement. [VERIFIED for the reference fields: https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report; https://docs.stripe.com/reports/payout-reconciliation]

### 1.12 PSD3 / PSR status (EU) ⚠

- Commission proposal: 28 June 2023. Provisional political agreement: 27 November 2025. ECON committee approval: 5 May 2026. The European Parliament Legislative Train (updated 20 Sept 2026) lists the file as **"Close to adoption"**. The text "needs to be formally adopted by Parliament and Council before it can enter into force" [VERIFIED: https://www.europarl.europa.eu/legislative-train/theme-an-economy-that-works-for-people/file-payment-services-and-electronic-money-services-(directive)].
- The Council published the final compromise texts on 23 April 2026 [WIDELY REPORTED: https://www.hoganlovells.com/en/publications/final-texts-for-psd3-and-psr-awaited-as-european-parliament-and-council-of-eu-announce-provisional].
- **Transition (per Legislative Train):** existing payment institution and e-money institution licences stay valid until 30 months after entry into force, provided a new application is made within 24 months [VERIFIED: Legislative Train URL above]. Application dates of roughly 18 months after entry into force for PSD3, and 2027–2028 in vendor guides, are **estimates** [ASSUMPTION/JUDGEMENT].
- **Structure:** PSD3 is a directive (licensing and supervision, folding in the E-Money Directive). The PSR is a directly applicable regulation (conduct rules: fraud, IBAN/name verification, open banking, SCA refinements). [WIDELY REPORTED: https://www.algoodbody.com/insights-publications/psd-3-psr-final-compromise-texts-published]
- **Writer instruction:** as of 18 Oct 2026 PSD3/PSR is **not yet law in force**. Check Official Journal publication before going to print.

### 1.13 E-money and safeguarding basics

- PSD2 Art. 10 requires payment institutions holding user funds to safeguard them. Option one is *segregation*: no commingling, and funds still held at the end of the business day following receipt are placed in a separate account at a credit institution or in secure low-risk assets, insulated from other creditors in insolvency. Option two is an *insurance policy or comparable guarantee* from an unaffiliated insurer or credit institution [VERIFIED: https://eur-lex.europa.eu/eli/dir/2015/2366/oj].
- The E-Money Directive (2009/110/EC) applies equivalent safeguarding to e-money institutions [ASSUMPTION/JUDGEMENT].
- **Why architects care:** a PSP that is a *bank* (Adyen N.V. holds a European banking licence) holds client money under a different regime from an e-money or payment institution. This affects counterparty-risk assessment, treasury policy on how long to leave funds at the PSP, and audit evidence. [ASSUMPTION/JUDGEMENT]
- In the US, Stripe Treasury financial accounts are either a DDA at Stripe's banking partner (a "checking account") or an FBO arrangement (a "business account"). FDIC pass-through eligibility depends on the structure. Stripe states it "isn't an FDIC-insured depository institution" and names Fifth Third Bank, N.A. as the partner [VERIFIED: https://docs.stripe.com/treasury].

### 1.14 Why payments-to-ledger reconciliation is hard

This is the core thesis chapter writers will need. Each point is [ASSUMPTION/JUDGEMENT] unless a source is cited.

1. **Timing mismatch.** The commerce system records the sale at authorisation or capture; the GL needs revenue at fulfilment and cash at bank receipt. Stripe separates `created` from `available_on` per balance transaction [VERIFIED: https://docs.stripe.com/api/balance_transactions/object]. Adyen separates Booking Date from Value Date in the Balance Platform accounting report [VERIFIED: https://docs.adyen.com/marketplaces/reports-and-fees/balance-platform-accounting-report]. Settlement delays vary by country: Stripe's default is 2 business days in the US, 7 calendar days initially then 3 business days in Germany, and 4 business days in Japan [VERIFIED: https://docs.stripe.com/payouts].
2. **Batching and netting.** One bank credit equals many sales, minus refunds, chargebacks, fees and reserve movements. Adyen: "Payouts are net" [VERIFIED: https://docs.adyen.com/account/getting-paid]. Stripe's payout reconciliation report exists to list "every payment, refund, dispute, fee, and other balance transaction included in the payout" [VERIFIED: https://docs.stripe.com/reports/payout-reconciliation].
3. **Fees netted, and sometimes invoiced separately.** Adyen's **InvoiceDeduction** journal deducts invoice amounts (processing invoices, terminal hardware) from payouts [VERIFIED: settlement details report URL]. IC++ fees may be determined after the sale.
4. **FX** at conversion, at dispute and at refund (§1.9).
5. **Partial and multiple captures.** One authorisation can map to N captures with N references. Adyen gives each modification its own pspReference; `originalReference` points to the authorisation [VERIFIED: https://docs.adyen.com/online-payments/capture].
6. **Chargebacks months later**, often in a different period, possibly in a different amount (§1.7).
7. **Status reversals.** Adyen's Sales day payout pre-finances sales and later posts reversals such as **SettledReversed** (funds not received within 30 days) and **CaptureFailed**. The webhooks for these are "disabled by default" [VERIFIED: settlement details report URL].
8. **Time zones and cut-offs.** Adyen reports follow the account's time zone setting, but invoices are CET-based [VERIFIED: https://docs.adyen.com/reporting/invoice-reconciliation/payment-accounting-report]. Stripe Dashboard reports default to local time zone while Sigma templates use UTC [VERIFIED: https://docs.stripe.com/stripe-data/how-sigma-works].
9. **Report data lags payouts.** Stripe: "a payout might arrive before its reconciliation data is ready" [VERIFIED: https://docs.stripe.com/reports/payout-reconciliation].
10. **Reference propagation.** The merchant's order ID must be passed as Adyen `merchantReference` or Stripe metadata, and it survives into reports only if the integration does this consistently. Stripe's itemised reports can include `payment_metadata[key]` [VERIFIED: https://docs.stripe.com/reports/payout-reconciliation].
11. **Multiple PSPs** multiply all of the above, each with different semantics (§4).

**Recommended pattern for writers** [ASSUMPTION/JUDGEMENT]: a three-way match.

1. Order/commerce record ↔ PSP transaction record (by merchant reference).
2. PSP transaction records ↔ PSP payout/batch (by batch number or payout ID).
3. PSP payout ↔ bank statement line (by payout reference or trace ID, via camt.053/BAI2).

A **payments sub-ledger or clearing account per PSP and currency** should reach zero once all three legs are matched. This is the same clearing-account idea Stripe describes for its internal Ledger (§3.12).

---

## PART 2: Adyen

### 2.1 Company facts

- **Banking licence:** Adyen holds "a pan-European banking license", granted in 2017 [WIDELY REPORTED: https://www.adyen.com/press-and-media/adyens-branch-license-application-approved-by-us-federal-reserve]. [ASSUMPTION/JUDGEMENT] The supervisor is De Nederlandsche Bank (DNB) under ECB SSM arrangements; this was not confirmed in this session.
- **US branch:** the Federal Reserve approved Adyen N.V.'s application for a federally licensed branch in San Francisco on 24 May 2021 [VERIFIED: https://www.federalreserve.gov/newsevents/pressreleases/orders20210524a.htm]. The OCC approved the Federal Foreign Branch in June 2021 [WIDELY REPORTED: https://www.adyen.com/press-and-media/adyen-granted-us-branch-license]. The OCC gave preliminary conditional approval in June 2020 [WIDELY REPORTED: https://ots.gov/topics/charters-and-licensing/interpretations-and-actions/2020/ca1246.pdf].
- **Listing:** [ASSUMPTION/JUDGEMENT] listed on Euronext Amsterdam (ticker ADYEN) since June 2018. The investor site (investors.adyen.com) was reachable but did not show listing details. It shows the latest published period as **H1 2026** and a "Business Update – Q3 2026" scheduled for **28 October 2026** [VERIFIED: https://investors.adyen.com/]. ⚠ Do not quote volumes or revenue without the shareholder letter.

### 2.2 Platform positioning

- **Single platform:** gateway, risk and acquiring on one stack, with unified commerce across online and in-person. [WIDELY REPORTED: https://www.adyen.com/pricing; ASSUMPTION/JUDGEMENT on "single code base" claims, which are Adyen marketing]
- **Risk:** the risk module, formerly "RevenueProtect", is now marketed as **Protect** within **Adyen Uplift**, an AI-driven optimisation suite announced January 2025 covering risk, authentication, checkout and cost [WIDELY REPORTED: https://thepaypers.com/payments-general/adyen-launches-adyen-uplift--1271691; https://www.adyen.com/protect]. Reported pilot outcomes (e.g. 86% fewer manual rules) are company-reported figures.
- **Externally settled payments:** Adyen can also process as a gateway for transactions acquired elsewhere. Its journal types include **EpaPaid**, MiscCosts, and record types such as `SettledExternally`, `RefundedExternally`, `ChargebackExternally` [VERIFIED: settlement details report URL; payment accounting report URL]. This matters for multi-acquirer estates.

### 2.3 Account structure and identifiers

- **Company account:** "holds all your merchant accounts and users"; the monthly invoice is issued here by default [VERIFIED: https://docs.adyen.com/account/account-structure].
- **Merchant account:** where payments are processed, payouts received and reconciliation reports produced; payment methods and currencies are configured here. Many businesses need only one; multiple accounts can be split by region or brand. **Stores** sit under merchant accounts for POS. **Account groups** are optional [VERIFIED: same].
- **pspReference:** Adyen's unique reference per payment, and separately per modification (capture, refund). `originalReference` links a modification to the authorisation [VERIFIED: https://docs.adyen.com/online-payments/capture].
- **merchantReference:** the merchant's own reference, e.g. an order ID [ASSUMPTION/JUDGEMENT; glossary page 404]. This is the join key to ERP/OMS.
- **Modifications are asynchronous.** A capture request returns `received`, and the outcome arrives by webhook (eventCode `CAPTURE`, `success` true/false) [VERIFIED: https://docs.adyen.com/online-payments/capture]. Architects must not treat the API response as the final state.

### 2.4 Webhooks

- **Accept quickly:** return 2xx (e.g. 202) and "store the webhook message in your database or a queue" before processing. If Adyen does not get a response "within 10 seconds", the webhook is marked as failing [VERIFIED: https://docs.adyen.com/development-resources/webhooks/handle-webhook-events].
- **HMAC:** "Always verify the HMAC signature before processing the payload". Server libraries include a validator [VERIFIED: same].
- **Duplicates (at-least-once):** duplicates "have the same values in the eventCode and pspReference fields", and the server "should use the details from the latest webhook event" [VERIFIED: same].
- **Ordering:** check the timestamp; some payloads include a `sequenceNumber` [VERIFIED: same].
- **Retries:** a few quick retries, then a retry queue with intervals "from 30 seconds up to 8 hours", for up to **30 days**. You can manually Retry or Ignore queued messages in the Customer Area [VERIFIED: https://docs.adyen.com/development-resources/webhooks/troubleshoot].
- **Reports via webhook:** classic accounts get a `REPORT_AVAILABLE` webhook whose payload carries the file name and download URL. The file is fetched by HTTP GET using a Report Service user credential (API key or Basic auth). Balance Platform uses `balancePlatform.report.created` with a `downloadUrl` [WIDELY REPORTED via docs search summary: https://docs.adyen.com/reporting/automatically-get-reports]. ⚠ Field names differ between webhook versions (`reason` vs `remoteAccessUrl`), so check the configured version.

### 2.5 Reports (classic acquiring)

| Report | Level | Purpose | Source |
| --- | --- | --- | --- |
| **Settlement details report** (SDR) | Transaction, per batch | Every credit/debit in a payable batch with fees. Generated per merchant account per batch (`settlement_detail_report_batch_<N>`), or on a daily/weekly/monthly schedule. Formats: CSV, XLS_GEN, TSV, XML, XMLE | [VERIFIED: https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report] |
| **Aggregate settlement details report** | Batch | Settled batches and other movements over a date range, grouped by merchant account/store/payment method/journal type. Used to match payouts to bank deposits; generated before 10:00 in the account time zone | [VERIFIED via docs search summary: https://docs.adyen.com/reporting/settlement-reconciliation/batch-level/aggregate-settlement-details-report] |
| **Payment accounting report** (PAR) | Transaction lifecycle | Every status change (record type) with associated costs. Used for invoice reconciliation and fee-to-status matching. Booking Date in account time zone, plus an AMS column | [VERIFIED: https://docs.adyen.com/reporting/invoice-reconciliation/payment-accounting-report] |
| **Received payment details report** | Transaction | Payment attempts with method, issuing country, 3DS interaction, statuses and reason codes. Used to find unsettled payments | [VERIFIED via docs search summary: https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level] |
| **Balance Platform accounting report** | Transfer, daily | All balance changes across liable and user balance accounts. Multiple rows per Transfer Id as status progresses. Categories: `bank`, `internal`, `platformPayment`, `issuedCard`. Booking Date vs Value Date | [VERIFIED: https://docs.adyen.com/marketplaces/reports-and-fees/balance-platform-accounting-report] |

**Two vocabularies, do not conflate them:**

- **Journal types** (SDR) describe *money movements in a payable batch*: Settled (credit), Refunded (debit), Chargeback, SecondChargeback, ChargebackReversed, RefundedReversed, Fee, MiscCosts, MerchantPayout, DepositCorrection, InvoiceDeduction, MatchedStatement, ManualCorrected, BankInstructionReturned, EpaPaid, Balancetransfer, PaymentCost, PaidOut, PaidOutReversed, instalment variants, Sales-day-payout reversals (CaptureFailed, RefundFailed, RefundNotCleared, SettledReversed), MerchantPayin, ReserveAdjustment, MerchantPayinReversed, XASTransfer [VERIFIED: SDR URL].
- **Record types** (PAR) describe *lifecycle statuses*: Received, Authorised, AuthorisedPending, SentForSettle, Settled, SentForRefund, Refunded, Refused, Cancelled, Expired, CaptureFailed, Chargeback, SecondChargeback, ChargebackReversed, plus *Externally* variants, payout and instalment records, and AuthenticationRequested [VERIFIED: PAR URL].
- **Received, Authorised and SentForSettle are PAR record types, not SDR journal types.** The SDR's **Fee** journal covers Adyen transaction fees "for received and sent-for-refund transactions in the batch period" [VERIFIED: SDR URL].

**Key SDR columns:** Gross Debit/Credit (transaction currency), Net Debit/Credit (settlement currency), Exchange Rate, Commission (or Markup + Scheme Fees + Interchange when interchange-level data exists), Payment Fees, Batch Number [VERIFIED: SDR URL].

### 2.6 Settlement batches and payout timing

- **Payout models** [VERIFIED: https://docs.adyen.com/account/getting-paid]:
  - **Sales day payout** is the default and recommended model: a whole sales day in one batch, pre-financed.
  - **Pass-through payout** splits a sales day across batches as funds arrive from schemes. It is "the only available payout model in Africa, Brazil, and India".
- **Timing:** payout frequency is configured per merchant account. After batch close, initiation takes 1–2 business days, and the bank may need up to 3 more. If funds have not arrived 5 business days after batch close, check the **BankInstructionReturned** journal in the Aggregate SDR [VERIFIED: same].
- **Bank holidays** block payouts for the affected currencies [VERIFIED: same].
- **Reconciliation guidance (Adyen's own):**
  - Batch level: match MerchantPayout (payout reference + batch number + merchant account) to the bank statement [VERIFIED: SDR URL].
  - Transaction level: compare the Settled totals in the Aggregate report against your sales, then use the Received payment details and Payment accounting reports to find items not yet Settled [VERIFIED via docs search summary: https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level].
  - Platforms: use API responses and webhooks for real-time ledger updates, and the accounting report for confirmation [WIDELY REPORTED via docs search summary: Balance Platform accounting report URL].

### 2.7 Adyen for Platforms / Balance Platform

- **Resources** [VERIFIED: https://docs.adyen.com/platforms/account-structure-resources/platform-structure; docs search summary of https://docs.adyen.com/marketplaces/account-structure-resources]:
  - Company account, plus a merchant account per country/region.
  - One balance platform per acquiring region.
  - **Liable account holder** and **liable balance account** (the platform's own funds).
  - Per user: **legal entity** (KYC data), **account holder** (capabilities; one per country of operation), **balance accounts** (funds, with a base currency), **transfer instrument** (verified bank account for payouts), stores and business lines.
- **Funds flow:** payment → store → merchant account → settles into balance accounts according to the platform's split instructions → stays until paid out to the transfer instrument [VERIFIED: platform-structure URL].
- **Transfers:** internal (between balance accounts) or bank (to/from a transfer instrument or bank account). Webhooks: `balancePlatform.transfer.created/updated` and `balancePlatform.transaction.created`. Status `booked` means funds actually moved [WIDELY REPORTED via docs search summary: https://docs.adyen.com/api-explorer/transfer-webhooks/4/post/balancePlatform.transfer.created].
- **Booked is not final for payouts:** instant payouts can be rejected and regular/wire payouts returned, so ledgers must handle later `returned`/`failed` [WIDELY REPORTED via docs search summary: https://docs.adyen.com/payouts/payout-service/payout-lifecycle/].
- **Classic vs Balance Platform:** the `XASTransfer` journal type refers to "classic Adyen for Platforms integrations" [VERIFIED: SDR URL]. ⚠ Writers should describe the Balance Platform as current and the classic version as legacy, but should not state a sunset date without verification.

### 2.8 Issuing and Capital

- **Issuing:** virtual and physical Visa and Mastercard cards in the EEA, UK and US. **Authorisation relay** lets your server approve or decline each authorisation, or you can use transaction rules. Cards draw on balance accounts, and the liable balance account funds loads [VERIFIED: https://docs.adyen.com/issuing].
- **Capital:** business financing offers presented by the platform to its users. Repayment is daily, a fixed percentage of processed volume. Credit risk and underwriting sit with Adyen [VERIFIED via docs search summary: https://docs.adyen.com/platforms/financial-products; WIDELY REPORTED: https://www.adyen.com/capital].
- **Business accounts:** users can make transfers to third-party bank accounts [VERIFIED via docs search summary: https://www.adyen.com/accounts].

### 2.9 Tokenisation, network tokens, data access

- Adyen supports tokenisation and network tokens [ASSUMPTION/JUDGEMENT; the specific network-token doc URL returned 404 this session].
- **Data access:** reports (CSV/TSV/XML) are pulled programmatically after a report webhook, plus webhooks for events. For the platform model, Adyen recommends "a script to load the reports and reconcile into your systems" [WIDELY REPORTED via docs search summary: https://docs.adyen.com/marketplaces/prepare-reports/generate-download-reports]. ⚠ "Reports API" in the brief request is not an exact Adyen product name as far as this session could verify. Describe it as "report download via report credentials + report webhooks".

---

## PART 3: Stripe

### 3.1 PaymentIntents and Charges

- **PaymentIntent** tracks a payment attempt's lifecycle: `requires_payment_method` → (`requires_confirmation`) → `requires_action` (e.g. 3DS) → `processing` (async methods) or `requires_capture` (manual capture) → `succeeded` / `canceled`. A failed attempt returns to `requires_payment_method` [VERIFIED: https://docs.stripe.com/payments/paymentintents/lifecycle].
- ⚠ Stripe now recommends the **Checkout Sessions API** over raw PaymentIntents for most integrations [VERIFIED: same].
- A PaymentIntent creates **Charge** objects (one per attempt). The charge carries `payment_method_details.card.capture_before` [VERIFIED: https://docs.stripe.com/payments/place-a-hold-on-a-payment-method].
- **Capture:** `capture_method=manual`, then capture with optional `amount_to_capture`. A partial capture releases the rest. Multicapture and overcapture exist for eligible payments. ⚠ `automatic_delayed` capture is in **private preview** [VERIFIED: same].

### 3.2 Balance Transactions: Stripe's ledger-like object

- **Every movement of funds in a Stripe balance** produces a Balance Transaction [ASSUMPTION/JUDGEMENT for "every"; the object docs describe it as the transaction's net impact on a Stripe balance].
- Fields [VERIFIED: https://docs.stripe.com/api/balance_transactions/object]:
  - `amount` (gross), `fee`, `fee_details[]`, `net` (= amount − fee).
  - `currency`, `exchange_rate`.
  - `available_on` ("the date that the transaction's net funds become available"), `status` (`pending` / `available`).
  - `balance_type` (`payments`, `issuing`, `refund_and_dispute_prefunding`, `risk_reserved`).
  - `reporting_category`, `source` (expandable link to the originating object), `type`.
- `type` has ~55 values, including:
  - payments and refunds: `charge`, `payment`, `refund`, `payment_refund`, `refund_failure`;
  - Connect: `application_fee`, `transfer`, `transfer_cancel`/`transfer_failure`/`transfer_refund`, `connect_collection_transfer`;
  - payouts: `payout`, `payout_failure`, `payout_cancel`;
  - adjustments and fees: `adjustment` (disputes appear here), `stripe_fee`, `stripe_fx_fee`, `tax_fee`;
  - reserves: `reserve_hold/release`;
  - Issuing: `issuing_*`;
  - funding: `topup`, `advance`, `anticipation_repayment`.
- Stripe advises: "To classify transactions for accounting purposes, consider `reporting_category` instead" of `type` [VERIFIED: same].
- **Architectural reading:** the balance transaction is a *single-entry* record of the effect on Stripe's view of your balance. It is not a double-entry GL. The merchant must map `reporting_category` to accounts and post fees, FX and reserves separately. [ASSUMPTION/JUDGEMENT]

### 3.3 Payouts and payout reconciliation

- **Automatic vs manual** [VERIFIED: https://docs.stripe.com/payouts]:
  - Automatic payouts follow a schedule (daily, weekly or monthly).
  - Manual payouts let you choose when and how much; they typically take 1–4 business days.
  - Same-day manual payouts exist in the US, UK and Eurozone, subject to cut-offs and limits.
  - Brazil and India are always automatic and daily.
  - The initial payout is typically 7–14 days after the first live payment.
  - Instant payouts usually arrive within 30 minutes.
  - Negative balances can be debited from the bank account.
- **Payout reconciliation report** [VERIFIED: https://docs.stripe.com/reports/payout-reconciliation]:
  - Available only with **automatic payouts**, or for a platform whose connected accounts use automatic payouts. Manual-payout users should use the Balance report.
  - For instant payouts, "Stripe can't identify which transactions are included in each payout", so you reconcile them yourself.
  - Sections: Balance summary, Payout reconciliation (grouped by reporting category), Failed payouts, Ending balance reconciliation (unsettled at period end).
  - API report types: `payout_reconciliation.summary.2`, `payout_reconciliation.itemized.7`, `ending_balance_reconciliation.itemized.4`, `failed_payouts.itemized.2`, `balance.summary.2`. ⚠ The version suffixes change.
  - Itemised columns include `automatic_payout_id`, `automatic_payout_effective_at`, `available_on`, `balance_transaction_id`, `reporting_category`, `gross/fee/net`, `payment_intent_id`, `payment_metadata[key]`, `trace_id`, `payout_reference_token`, `withheld_tax`, and `regulatory_tag` (Brazil only).
  - Payouts are grouped by *estimated arrival date*, not bank posting date. Dashboard reports cover whole days; the Reporting API allows partial days. Webhooks fire twice daily when 00:00 and 12:00 UTC data becomes available.

### 3.4 Connect

- **Charge types:** direct, destination, and separate charges and transfers, with refund, dispute and fee liability as described in §1.10 [VERIFIED: https://docs.stripe.com/connect/charges].
- **`on_behalf_of`:** makes the connected account the "business of record". Settlement happens in that account's country, and its fee structure and statement descriptor apply [VERIFIED: same].
- **Application fees:** on direct charges, the fee transfers to the platform's balance when the connected account collects the payment [VERIFIED: same].
- **Disputes on indirect charges** debit the platform. Recovery is via transfer reversal; `debit_negative_balances` controls whether Stripe debits the connected account's bank [VERIFIED: same].
- **Account models** ⚠ (the model has shifted):
  - Standard, Express and Custom are now documented as **legacy "account types"** ("Deprecated feature") [VERIFIED: https://docs.stripe.com/connect/accounts].
  - Stripe recommends **controller properties** (Accounts v1) or the **Accounts v2 API**. v2 uses *configurations*: `merchant` (accept payments), `customer` (be charged by the platform, replacing Customer objects), `recipient` (receive transfers). `defaults.responsibilities` sets `fees_collector` and `losses_collector` [VERIFIED: https://docs.stripe.com/connect/accounts-v2].
  - v2 cannot yet be used for OAuth, the `treasury` or `card_issuing_*` capabilities, or recipient service agreements [VERIFIED: same].
  - Legacy fraud/dispute liability: Standard puts it on the connected account for direct charges; Express and Custom put it on the platform [VERIFIED: https://docs.stripe.com/connect/accounts].

### 3.5 Billing (subscriptions, invoices, usage)

- Subscriptions generate invoices each cycle. Each subscription item becomes an invoice line item with a service period [VERIFIED: https://docs.stripe.com/revenue-recognition/methodology].
- **Usage-based billing ⚠:** Stripe docs now say "Metronome is now part of Stripe". **Metronome** is "Stripe's primary usage-based billing platform and the recommended starting point for all new integrations". The **Meters API** ("basic usage-based billing") remains supported, and legacy **usage records** are documented as legacy [VERIFIED: https://docs.stripe.com/billing/subscriptions/usage-based]. The acquisition date was not verified because the newsroom URL returned 404.

### 3.6 Stripe Tax

Stripe Tax covers calculation of sales tax/VAT/GST by product tax code and location, threshold monitoring, registration management (including registering on your behalf in the US), filing/remittance (directly or via partners), Connect support, and a Tax API for off-Stripe payments [VERIFIED: https://docs.stripe.com/tax]. The `tax_fee` and `tax_fund` balance transaction types exist [VERIFIED: balance transactions URL].

### 3.7 Stripe Revenue Recognition

- **Purpose:** automates accrual accounting. Stripe positions it for ASC 606 / IFRS compliance [VERIFIED: https://docs.stripe.com/revenue-recognition/methodology].
- **Mechanics** [VERIFIED: same]:
  - "Built … on top of a double-entry accounting ledger".
  - Each invoice line item is treated as its own performance obligation and amortised evenly over its period.
  - One-time PaymentIntent/Charge payments are recognised immediately unless data is imported.
  - Refunds and disputes generate contra-revenue.
  - Invoices paid outside Stripe go to an "External asset" account.
- **Default chart of accounts** [VERIFIED: same]:
  - Revenue; contra-revenue accounts (Refunds, Disputes, Credit notes, Bad debt, Voids).
  - AR, Cash, Deferred revenue (with long-term deferred revenue on by default), Unbilled AR, Tax liability.
  - FxLoss, Fees, Pending cash (async methods such as ACH), Connect transfer loss.
- **Customisation:** rules, chart-of-accounts mapping to your GL, **data import** (non-Stripe transactions, service periods, exclusions), CSV exports including a debits-and-credits (journal entry) report, and audit drill-down [VERIFIED: https://docs.stripe.com/revenue-recognition].
- **Writer caution:** this is a sub-ledger for Stripe-originated revenue. It is not an enterprise revenue engine for multi-element contracts across non-Stripe channels without significant import work. That is a judgement, not a Stripe statement [ASSUMPTION/JUDGEMENT].

### 3.8 Sigma and Data Pipeline

- **Sigma:** a read-only SQL environment in the Dashboard with report templates (e.g. `payout_reconciliation.itemized.5`). It filters in UTC, and the `data_load_time` parameter tells you how fresh the data is [VERIFIED: https://docs.stripe.com/stripe-data/how-sigma-works]. [ASSUMPTION/JUDGEMENT] The dialect is Trino/Presto-based; not confirmed this session.
- **Data Pipeline:** data shares to **Snowflake, Amazon Redshift, Databricks, BigQuery**, or Parquet to **S3, GCS, Azure Blob** [VERIFIED: https://docs.stripe.com/stripe-data/access-data-in-warehouse].
  - Initial data arrives within 12 hours, then "a full load of data every 3 hours".
  - Live and test data go to separate schemas (`STRIPE`, `STRIPE_TESTMODE`); every table has `merchant_id`.
  - Not offered in India.
- **Architectural point:** Data Pipeline is the usual feed for an enterprise reconciliation engine or data warehouse, and webhooks feed operational systems. Reports and Sigma are for finance self-service. [ASSUMPTION/JUDGEMENT]

### 3.9 Financial Connections, Treasury / Financial Accounts, Issuing

- **Financial Connections:** see §1.4 [VERIFIED: https://docs.stripe.com/financial-connections].
- **Treasury ⚠** [VERIFIED: https://docs.stripe.com/treasury]:
  - Now framed around **financial accounts** that receive settled Stripe earnings, hold fiat (USD/EUR/GBP), and power cards, FX and **Global Payouts**.
  - Eligible businesses can hold **stablecoin balances (USDC, OUSD)**.
  - Availability: US and UK in public preview, Australia in private preview.
  - US accounts are DDA ("checking account") or FBO ("business account") at Fifth Third Bank.
  - Treasury for platforms is documented separately.
- **Issuing:** balance transaction types `issuing_authorization_hold/release`, `issuing_transaction`, `issuing_dispute` and an `issuing` balance type [VERIFIED: balance transactions URL]. Real-time authorisation uses the `issuing_authorization.request` webhook, which cannot go to organisation-level destinations [VERIFIED: https://docs.stripe.com/webhooks].

### 3.10 Webhooks and idempotency

- **Signature:** the `Stripe-Signature` header carries `t=` (timestamp) and `v1=` (HMAC-SHA256 over `timestamp.payload` with the endpoint's `whsec_` secret). Ignore non-`v1` schemes. Libraries default to a 5-minute tolerance, and the raw body is required [VERIFIED: https://docs.stripe.com/webhooks].
- **Retries:** "up to three days with an exponential back off in live mode"; sandbox retries three times over a few hours. Manual resend is available for 15 days (Dashboard) or 30 days (CLI) [VERIFIED: same].
- **Ordering:** "Stripe doesn't guarantee the delivery of events in the order that they're generated". Don't use `created` (second granularity) for ordering [VERIFIED: same].
- **Duplicates:** log event IDs. In some cases two distinct Event objects describe the same thing; dedupe on `data.object.id` + `event.type` [VERIFIED: same].
- **Snapshot vs thin events ⚠:** new event destinations offer **Thin (recommended)** or **Snapshot** payloads. Events can also go to Amazon EventBridge or Azure Event Grid. Snapshot events are frozen at the API version in force when they were created [VERIFIED: same].
- **Idempotency keys** [VERIFIED: https://docs.stripe.com/api/idempotent_requests]:
  - Supported on all v1 POSTs.
  - Keys are up to 255 characters and can be pruned after ≥24 hours.
  - Parameter mismatches error.
  - v1 replays the saved response, including 500s. v2 retries failed work to completion.

### 3.11 API versioning ⚠

- Since `2024-09-30.acacia`, Stripe ships **monthly non-breaking versions** and **twice-yearly major releases** with breaking changes (e.g. Basil). The current version is **`2026-09-30.endive`** [VERIFIED: https://docs.stripe.com/api/versioning].
- Requests use the account default unless the `Stripe-Version` header is set. Typed SDKs pin the version. Webhook payloads follow the endpoint's configured version, or else the account default [VERIFIED: same].
- **Finance implication:** report column sets and event shapes are versioned. A reconciliation pipeline needs version pinning and regression tests at upgrade. [ASSUMPTION/JUDGEMENT]

### 3.12 Stripe's internal "Ledger" (engineering blog)

- **Exists and verified:** "Ledger: Stripe's system for tracking and validating money movement", by Ilya Ganelin, published **16 February 2024** [VERIFIED: https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement].
- **Claims** [VERIFIED: same]:
  - A system of record for Stripe's financial data, using double-entry bookkeeping and an immutable log; corrections are made by reversal and reprocessing.
  - Producer systems are modelled as state machines and logical *fund flows*.
  - **Clearing accounts** should be zero at steady state; a non-zero balance flags missing, late or incorrect data.
  - Data-quality metrics: clearing, timeliness, completeness.
  - Scale: ~5 billion events/day; 99.99% of dollar volume ingested and verified within four days.
- **Use in the book:** a strong vendor-neutral illustration of the "clearing account reaches zero" reconciliation pattern (§1.14). It describes Stripe's *internal* system. It is **not** a product merchants can use, and writers must not imply otherwise [ASSUMPTION/JUDGEMENT].

### 3.13 Stripe Orchestration ⚠

- **Status:** "Orchestration is in private preview" (October 2026) [VERIFIED: https://docs.stripe.com/payments/orchestration]. It was previewed at Sessions 2025 [WIDELY REPORTED: https://stripe.com/blog/top-product-updates-sessions-2025].
- **Features** [VERIFIED: same]:
  - Route PaymentIntents (and Billing, Checkout, Payment Links, Dashboard payments) to "Stripe-supported processors".
  - Retry on an alternative processor; monitor performance by processor.
  - Rules on card country, currency, amount, BIN, etc., executed in order with the first match winning [VERIFIED via docs search summary: https://docs.stripe.com/payments/orchestration/rules].
- **Limits** [VERIFIED: same]:
  - Supports no non-card payments, Link, Capital, Connect, Terminal or Organizations.
  - "doesn't support disputes or settlement-related activity". Those stay in the third-party processor's dashboard, and fees and loss liability stay under that processor's contract.
- **Third-party processors named in a secondary source:** Adyen, Braintree, Worldpay, Checkout.com [WIDELY REPORTED; undated secondary source, do not print without checking].
- **Implication:** Stripe Orchestration unifies *routing*, but not *settlement data*. Reconciliation across processors remains the merchant's problem. [ASSUMPTION/JUDGEMENT, grounded in the docs statement above]

---

## PART 4: Multi-PSP and orchestration

### 4.1 Why enterprises use multiple PSPs [ASSUMPTION/JUDGEMENT unless noted]

- **Resilience:** failover when a PSP or acquirer is degraded.
- **Approval rates:** local acquiring in key markets (domestic issuers approve domestic acquirers more often), plus cascading retries on soft declines.
- **Cost:** routing by cost (e.g. debit networks in the US, local schemes such as Cartes Bancaires) and commercial leverage in negotiations.
- **Coverage:** local payment methods and countries one PSP doesn't serve. Pass-through-only markets (Africa, Brazil, India in Adyen's case [VERIFIED: https://docs.adyen.com/account/getting-paid]) behave differently.
- **M&A legacy:** acquired businesses arrive with their own PSPs.
- **Regulatory/data-residency** constraints. For example, Stripe Data Pipeline is unavailable in India [VERIFIED: https://docs.stripe.com/stripe-data/access-data-in-warehouse].
- **Counter-argument:** Stripe's Sessions 2026 talk "More PSPs, more problems?" frames multi-processor setups as a trade-off [WIDELY REPORTED: https://stripe.com/sessions/2026/more-psps-more-problems]. Each extra PSP adds integration, reconciliation, dispute-operations and token-portability cost, and splits volume (weakening pricing tiers). Writers should present both sides.

### 4.2 Orchestration vendors (sample; descriptions are vendor self-descriptions)

| Vendor | Self-description (verified on homepage, Oct 2026) | Notes |
| --- | --- | --- |
| **Primer** | Unified platform for payments and finance teams. Centralised vault, no-code Workflows, **Reconciliation**, Fallbacks to a secondary processor, dynamic routing [WIDELY REPORTED: https://primer.io/] | Homepage does not use the word "orchestration" |
| **Spreedly** | "Open payments platform". Merchant-owned **Vault**, Connect (orchestration layer), Optimize (routing on cost/approval data), Protect (fraud/3DS) [WIDELY REPORTED: https://www.spreedly.com/] | Positioned on token portability |
| **Gr4vy** | Cloud payment orchestration as "Infrastructure as a Service"; dedicated instance per merchant, 400+ payment methods and anti-fraud connections, PCI DSS Level 1 [WIDELY REPORTED: https://gr4vy.com/] | ⚠ Ownership changes not verified; check before printing |
| **Juspay** | "Global Payments Operating System": orchestration, tokenisation, payouts, reconciliation. Claims $1Tn+ annual TPV and 300+ PSP integrations [WIDELY REPORTED: https://juspay.io/] | Company-reported figures |
| **Hyperswitch** (Juspay) | Open-source (Apache-2.0, Rust) composable payments platform; 100+ processors, routing, PCI vault, 2- and 3-way reconciliation [VERIFIED: https://github.com/juspay/hyperswitch] | Relevant for "build vs buy" chapters |
| **CellPoint Digital** | [ASSUMPTION/JUDGEMENT] Orchestration with an airline/travel focus; not fetched this session | Verify before printing |
| **Stripe Orchestration** | §3.13, private preview | PSP-native orchestration |

### 4.3 Normalisation of settlement data

The minimum canonical model a multi-PSP finance architecture needs [ASSUMPTION/JUDGEMENT, synthesised from §2.5 and §3.2–3.3]:

| Canonical concept | Adyen source | Stripe source |
| --- | --- | --- |
| Payment ID | pspReference (per payment, and per modification) | PaymentIntent ID / Charge ID / balance transaction `source` |
| Merchant order reference | merchantReference | `metadata` / `payment_metadata[key]` |
| Lifecycle event | PAR Record Type | Event type + PaymentIntent status |
| Money movement | SDR Journal Type | Balance Transaction `type` / `reporting_category` |
| Gross / fee / net | Gross, Commission or (Markup + Scheme Fees + Interchange), Net | `amount`, `fee` + `fee_details`, `net` |
| Currencies and rate | Gross currency, Net currency, Exchange Rate | `currency`, `exchange_rate`, `customer_facing_amount/currency` |
| Funds-availability date | Batch close / Value Date (platforms) | `available_on` |
| Payout grouping | Batch Number + MerchantPayout | `automatic_payout_id` |
| Bank match key | Payout reference on MerchantPayout | `trace_id`, `payout_reference_token` |

Design notes [ASSUMPTION/JUDGEMENT]:

- Keep the raw PSP record immutably next to the normalised one.
- Normalise sign conventions. Adyen uses separate debit/credit columns; Stripe uses signed amounts.
- Treat fees at the most granular level available. IC++ splits are not available for every transaction.
- Model status reversals (SettledReversed, payout_failure, RefundedReversed) as new events, never as updates in place.

### 4.4 Token portability

- PSP-issued tokens lock the merchant in. Options [ASSUMPTION/JUDGEMENT]:
  1. A third-party, merchant-controlled vault (orchestrator), which forwards PANs or network tokens to each PSP.
  2. Network tokens requested under the merchant's own token-requestor ID, where available.
  3. A negotiated PAN export from the outgoing PSP to the incoming one, PCI-to-PCI. Writers should note that contract clauses on data export at exit are a procurement item.
- Orchestrator vaults are themselves a dependency. Merchants should verify export rights from the orchestrator too. [ASSUMPTION/JUDGEMENT]

### 4.5 PCI DSS v4.0 / v4.0.1 scope implications

- **Versions ⚠:** PCI DSS **v4.0.1** was published 11 June 2024. v4.0 was retired on 31 December 2024. The future-dated requirements became effective **31 March 2025** and are unchanged by v4.0.1 [VERIFIED: https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1]. [ASSUMPTION/JUDGEMENT] v3.2.1 was retired on 31 March 2024.
- **Scope logic** [ASSUMPTION/JUDGEMENT]:
  - Using PSP-hosted fields, redirects or SDKs keeps PANs off merchant systems and minimises scope (typically SAQ A / A-EP territory).
  - A merchant-hosted vault or an orchestrator that proxies raw PANs brings the merchant's own systems into scope.
  - v4.0's script-integrity requirements for payment pages (6.4.3, 11.6.1) apply even to iframe/redirect integrations. ⚠ The PCI SSC later adjusted SAQ A eligibility wording; verify the current SAQ A text before printing.
- Stripe Orchestration with the Off-Session Payments API does not support "requests that contain raw card data" [WIDELY REPORTED via docs search summary: https://docs.stripe.com/payments/off-session-payments/orchestration]. Raw-PAN flows are a design choice with scope consequences.

---

## Common misconceptions

1. **"Authorised means paid."** No money moves at authorisation, and authorisations expire (5–7 days CNP on major schemes, ~2 days card-present) [VERIFIED: https://docs.stripe.com/payments/place-a-hold-on-a-payment-method].
2. **"The PSP payout equals sales for the day."** Payouts are net of fees, refunds, chargebacks, reserve movements and invoice deductions [VERIFIED: https://docs.adyen.com/account/getting-paid; SDR URL].
3. **"Received / Authorised / SentForSettle are Adyen journal types."** They are Payment accounting report *record types*. The Settlement details report's journal types are money movements (Settled, Refunded, Fee, MerchantPayout, …) [VERIFIED: SDR and PAR URLs].
4. **"A webhook arrives once and in order."** Adyen and Stripe both deliver at least once and do not guarantee order [VERIFIED: Adyen handle-webhook-events URL; https://docs.stripe.com/webhooks].
5. **"A chargeback is final when it is raised."** It can be reversed, re-raised (second chargeback), pre-arbitrated, or late-won [VERIFIED: Adyen dispute flow URL; Stripe disputes URL].
6. **"The chargeback amount equals the original sale."** FX, partial and aggregated disputes change it [VERIFIED: https://docs.stripe.com/disputes/how-disputes-work].
7. **"Stripe's Ledger is a product."** It is Stripe's internal system, described on its engineering blog [VERIFIED: stripe.dev URL].
8. **"Stripe Orchestration solves multi-PSP reconciliation."** It is in private preview and explicitly excludes settlement and disputes [VERIFIED: https://docs.stripe.com/payments/orchestration].
9. **"Interchange is capped for all EU card payments."** Commercial cards are excluded from IFR caps [VERIFIED: https://eur-lex.europa.eu/eli/reg/2015/751/oj].
10. **"PSD3 is in force."** As of Oct 2026 it is "close to adoption"; formal adoption is still pending [VERIFIED: Legislative Train URL].
11. **"Interchange++ means the fee is known at authorisation."** Fees are finalised at clearing, and some scheme fees are invoiced. [ASSUMPTION/JUDGEMENT; consistent with the existence of Adyen's PAR for invoice reconciliation]
12. **"Standard / Express / Custom are how you set up Stripe Connect."** They are now documented as legacy; new platforms use controller properties or Accounts v2 [VERIFIED: https://docs.stripe.com/connect/accounts].
13. **"Revenue = cash received via the PSP."** Revenue follows performance obligations; Stripe RevRec itself defers invoice line items over service periods [VERIFIED: https://docs.stripe.com/revenue-recognition/methodology].
14. **"A 'booked' payout is complete."** Adyen payouts can still be returned; Stripe has `payout_failure` [VERIFIED via docs search summary: Adyen payout lifecycle; Stripe balance transactions URL].

## Points chapter writers must be careful about

1. **Dates that move ⚠:**
   - Stripe API version (`2026-09-30.endive` at time of writing).
   - Stripe Orchestration and Treasury preview status.
   - PSD3/PSR adoption and OJ publication.
   - iDEAL→Wero migration timing (unverified).
   - SWIFT CBPR+ milestones (unverified this session).
   - PCI SAQ A wording.
   - Adyen's Q3 2026 update on 28 Oct 2026, which may supersede any figures.

   Re-check every one immediately before print.
2. **Don't invent product internals.** Adyen's "single code base", Stripe's ledger implementation details beyond the blog, and orchestrator scale claims are vendor statements. Attribute them.
3. **Use exact vendor vocabulary.** Adyen's balance platform, account holder, balance account, transfer instrument, liable balance account and payable batch, and Stripe's balance transaction, `reporting_category`, `available_on` and connected account configurations, are distinct concepts and not interchangeable.
4. **Keep legal and accounting concepts separate from funds flows.** MoR / principal-vs-agent / gross-vs-net are legal and accounting judgements. Stripe's `on_behalf_of` uses the term "business of record" for its own purposes.
5. **Regulatory figures:** quote IFR caps (0.2%/0.3%, consumer cards only), SCA exemption thresholds and IPR deadlines from the primary texts cited here. UK rules differ post-Brexit.
6. **Don't print reason-code numbers or scheme dispute timelines as universal.** They vary by scheme, region and rule release. Stripe's "120 days / 7–21 days / 60–75 days" are typical ranges, not rules.
7. **Company facts to re-verify:** Adyen's Euronext listing date, DNB as supervisor, and current product names (Protect/Uplift vs RevenueProtect) are not all primary-verified here.
8. **Metronome:** Stripe docs confirm "Metronome is now part of Stripe". The acquisition date and terms were not verified.
9. **Vendor neutrality:** the orchestration table is a sample of vendor self-descriptions. Don't rank vendors or imply completeness. CellPoint Digital and any Gr4vy ownership change are unverified.
10. **Report and API version suffixes** (e.g. `payout_reconciliation.itemized.7` vs the Sigma template's `.5`) differ between surfaces and change over time. Name the report, not the suffix, unless the version itself is the point.
11. **Time zones:** Adyen invoices are CET-based while reports follow the account setting; Stripe Sigma is UTC while Dashboard reports default to local time. Period-end cut-offs need an explicit rule.
12. **Search-budget limitation:** see "How to read this brief". ASSUMPTION/JUDGEMENT tags are honest flags, not padding.

---

## Sources (all URLs referenced)

**Regulation and standards**
- https://eur-lex.europa.eu/eli/reg_del/2018/389/oj — PSD2 RTS on SCA (definitions, dynamic linking, exemptions Arts. 13–18).
- https://eur-lex.europa.eu/eli/reg/2015/751/oj — EU Interchange Fee Regulation (0.2%/0.3% caps, commercial-card exclusion).
- https://eur-lex.europa.eu/eli/reg/2024/886/oj — Instant Payments Regulation (receive/send/VoP deadlines).
- https://eur-lex.europa.eu/eli/dir/2015/2366/oj — PSD2 (Art. 10 safeguarding).
- https://www.europarl.europa.eu/legislative-train/theme-an-economy-that-works-for-people/file-payment-services-and-electronic-money-services-(directive) — PSD3 status ("close to adoption", key dates).
- https://www.hoganlovells.com/en/publications/final-texts-for-psd3-and-psr-awaited-as-european-parliament-and-council-of-eu-announce-provisional — law-firm note on the PSD3/PSR provisional agreement.
- https://www.algoodbody.com/insights-publications/psd-3-psr-final-compromise-texts-published — law-firm note on the final compromise texts.
- https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1 — PCI DSS v4.0.1 publication and v4.0 retirement dates.
- https://www.federalreserve.gov/newsevents/pressreleases/orders20210524a.htm — Fed approval of Adyen's US branch (May 2021).
- https://ots.gov/topics/charters-and-licensing/interpretations-and-actions/2020/ca1246.pdf — OCC preliminary conditional approval (2020).

**Payment methods / schemes**
- https://www.ideal.nl/en/ — iDEAL | Wero current branding.
- https://www.ideal.nl/en/the-new-ideal/ — features of the new iDEAL (no timeline).
- https://epicompany.eu/ — EPI/Wero launch countries.
- https://www.npci.org.in/what-we-do/upi/product-overview — UPI operator (NPCI).

**Adyen**
- https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report — SDR journal types, columns, batches, generation.
- https://docs.adyen.com/reporting/invoice-reconciliation/payment-accounting-report — PAR record types, fee columns, booking date.
- https://docs.adyen.com/reporting/settlement-reconciliation/batch-level/aggregate-settlement-details-report — batch-level report.
- https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level — transaction-level reconciliation guidance.
- https://docs.adyen.com/reporting/automatically-get-reports — programmatic report retrieval.
- https://docs.adyen.com/account/getting-paid — payout models, timing, batches.
- https://docs.adyen.com/account/account-structure — company/merchant accounts, stores, account groups.
- https://docs.adyen.com/online-payments/capture — capture types, pspReference vs originalReference, async results.
- https://docs.adyen.com/development-resources/webhooks/handle-webhook-events — accept, HMAC, duplicates, ordering, 10-second rule.
- https://docs.adyen.com/development-resources/webhooks/troubleshoot — retry queue (30 s to 8 h, 30 days).
- https://docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow — dispute stages and webhook codes.
- https://docs.adyen.com/risk-management/understanding-disputes/dispute-reason-codes — reason codes by event and scheme.
- https://docs.adyen.com/platforms/account-structure-resources/platform-structure — Balance Platform resources and funds flow.
- https://docs.adyen.com/marketplaces/account-structure-resources — account holder/balance account/legal entity definitions.
- https://docs.adyen.com/marketplaces/reports-and-fees/balance-platform-accounting-report — platform accounting report.
- https://docs.adyen.com/api-explorer/transfer-webhooks/4/post/balancePlatform.transfer.created — transfer webhooks.
- https://docs.adyen.com/payouts/payout-service/payout-lifecycle/ — payout statuses, booked not final.
- https://docs.adyen.com/marketplaces/prepare-reports/generate-download-reports — platform report download.
- https://docs.adyen.com/issuing — Adyen Issuing scope.
- https://docs.adyen.com/platforms/financial-products — Capital, Issuing, business accounts.
- https://www.adyen.com/pricing — IC++ and indicative pricing.
- https://www.adyen.com/capital — Capital marketing page.
- https://www.adyen.com/accounts — business accounts marketing page.
- https://www.adyen.com/protect — Protect (risk) product page.
- https://thepaypers.com/payments-general/adyen-launches-adyen-uplift--1271691 — Uplift launch report (Jan 2025).
- https://www.adyen.com/press-and-media/adyens-branch-license-application-approved-by-us-federal-reserve — Adyen press release (EU licence 2017, Fed approval).
- https://www.adyen.com/press-and-media/adyen-granted-us-branch-license — Adyen press release (OCC approval).
- https://investors.adyen.com/ — IR site (H1 2026 letter, Q3 2026 update date).

**Stripe**
- https://docs.stripe.com/api/balance_transactions/object — Balance Transaction fields and types.
- https://docs.stripe.com/reports/payout-reconciliation — payout reconciliation report and columns.
- https://docs.stripe.com/payouts — payout schedules, timing, manual vs automatic.
- https://docs.stripe.com/payments/paymentintents/lifecycle — PaymentIntent statuses.
- https://docs.stripe.com/payments/place-a-hold-on-a-payment-method — auth windows, partial capture.
- https://docs.stripe.com/connect/charges — Connect charge types, on_behalf_of, refunds/disputes liability.
- https://docs.stripe.com/connect/accounts — legacy account types (deprecated).
- https://docs.stripe.com/connect/accounts-v2 — Accounts v2 configurations.
- https://docs.stripe.com/webhooks — signatures, retries, ordering, duplicates, thin/snapshot.
- https://docs.stripe.com/api/idempotent_requests — idempotency keys.
- https://docs.stripe.com/api/versioning — release cadence, current version.
- https://docs.stripe.com/disputes/how-disputes-work — dispute lifecycle, timings, fees.
- https://docs.stripe.com/revenue-recognition — RevRec feature index.
- https://docs.stripe.com/revenue-recognition/methodology — RevRec ledger, chart of accounts, journal entries.
- https://docs.stripe.com/billing/subscriptions/usage-based — Metronome vs Meters.
- https://docs.stripe.com/tax — Stripe Tax capabilities.
- https://docs.stripe.com/stripe-data/how-sigma-works — Sigma.
- https://docs.stripe.com/stripe-data/access-data-in-warehouse — Data Pipeline destinations and freshness.
- https://docs.stripe.com/financial-connections — Financial Connections.
- https://docs.stripe.com/treasury — Treasury/financial accounts, availability, FDIC structure.
- https://docs.stripe.com/payments/orchestration — Orchestration (private preview, limits).
- https://docs.stripe.com/payments/orchestration/rules — Orchestration routing rules.
- https://docs.stripe.com/payments/off-session-payments/orchestration — Off-session orchestration limits.
- https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement — Stripe engineering: Ledger (Feb 2024).
- https://stripe.com/blog/top-product-updates-sessions-2025 — Sessions 2025 product updates (Orchestration preview).
- https://stripe.com/sessions/2026/more-psps-more-problems — Sessions 2026 talk on multi-processor trade-offs.

**Orchestration vendors**
- https://primer.io/ — Primer self-description.
- https://www.spreedly.com/ — Spreedly self-description.
- https://gr4vy.com/ — Gr4vy self-description.
- https://juspay.io/ — Juspay self-description and scale claims.
- https://github.com/juspay/hyperswitch — Hyperswitch open-source repository.
