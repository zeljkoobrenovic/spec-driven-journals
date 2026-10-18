# Research Brief: Accounting, Controls and Regulation for Finance-Systems Architects

Prepared for: *Enterprise Architecture and Financial Systems* (chapter writers)
Prepared: 18 October 2026
Scope: accounting mechanics, revenue recognition, internal control over financial reporting (ICFR), regulatory and tax trends that reshape finance systems, record retention and privacy.

**How to read the evidence tags**

- **[VERIFIED: url]** — checked against a primary or authoritative source during this research pass (standard-setter, regulator, government, or official body page).
- **[WIDELY REPORTED: url]** — consistent across reputable secondary sources (Big-4, major law firms, recognised technical publishers); the primary text was not read directly in this pass.
- **[ASSUMPTION/JUDGEMENT]** — the analyst's professional synthesis, a teaching simplification, or an architectural opinion. Chapter writers may use it, but should present it as interpretation, not fact.
- **TIME-SENSITIVE** marks a claim likely to change after October 2026. Re-check before the manuscript is locked.

Research limitation: the web-search budget for this session ran out late in the pass. A few items (noted inline) rest on secondary sources only, and could not be re-checked against primary texts. Foundational accounting mechanics are long-settled; they are tagged as judgement or cited to standard-setter pages where useful, since they are textbook material rather than news.

---

## 1. Accounting essentials for engineers

### 1.1 Double-entry: the invariant

Every accounting event is recorded as a **journal entry** with at least two **lines**, where the sum of debits equals the sum of credits. This is the system's core invariant, and it should be enforced in the posting engine, not just checked afterwards. [ASSUMPTION/JUDGEMENT — textbook accounting; the invariant is universal across GAAPs]

The accounting equation is **Assets = Liabilities + Equity**, with Equity carrying cumulative **Income − Expenses** (retained earnings). Debit/credit is a sign convention, not "good/bad":

| Account class | Normal balance | Increased by | Statement |
| --- | --- | --- | --- |
| Assets | Debit | Debit | Balance sheet |
| Liabilities | Credit | Credit | Balance sheet |
| Equity | Credit | Credit | Balance sheet |
| Revenue / income | Credit | Credit | Income statement (P&L) |
| Expenses | Debit | Debit | Income statement (P&L) |

[ASSUMPTION/JUDGEMENT — standard convention]

Engineering translation: store amounts as signed decimals (debit positive, credit negative, or the reverse — pick one and document it) so that the invariant becomes `SUM(amount) = 0` per entry, per currency, per ledger. Never use binary floating point for money. [ASSUMPTION/JUDGEMENT]

### 1.2 Anatomy of a journal entry

A well-formed entry carries:

| Field | Purpose |
| --- | --- |
| Entry ID (immutable) | Unique, gap-tolerant identifier; many jurisdictions also require sequential document numbering for invoices (not for every GL entry). |
| Ledger / book | Which accounting book (e.g. IFRS primary ledger, US GAAP secondary ledger, local statutory ledger). |
| Legal entity | The company whose books these are; the unit of statutory reporting and tax. |
| Accounting date (posting date) | Drives the period the entry lands in. |
| Document / transaction date | When the business event occurred. |
| Entry/system timestamp and user | Audit trail: who posted, when. |
| Source system and source document reference | Traceability back to the subledger or operational record (invoice, booking, payment). |
| Lines: account, dimensions, debit/credit amount | The economic content. |
| Transaction currency, amount, rate, functional-currency amount | FX traceability (see 1.8). |
| Description, entry type (standard, accrual, reversing, adjustment, elimination) | Explains purpose; drives reversal logic. |
| Approval / workflow status | Evidence for manual journal-entry controls. |

[ASSUMPTION/JUDGEMENT — synthesis of common ERP designs and audit expectations]

Key design rule: posted entries are **never edited or deleted**; they are corrected by new entries (reversal plus re-post). This is both an audit expectation and, in several jurisdictions, a legal one (for example, German GoBD principles of immutability for electronic books). [ASSUMPTION/JUDGEMENT — GoBD cited from general knowledge, not re-verified in this pass]

### 1.3 Chart of accounts design: natural account plus dimensions

Modern charts of accounts separate **what** (the *natural account*: cash, trade receivables, revenue – commissions, salaries) from **where/who/why** (dimensions or segments: legal entity, cost centre, department, product line, geography, channel, intercompany counterparty, project). The full posting key is often called a *combination* or *accounting string*. [ASSUMPTION/JUDGEMENT]

Design guidance chapter writers can safely present:

- Keep the natural account list **small and stable** (hundreds, not tens of thousands); push analytical variety into dimensions. Account explosion ("revenue – Germany – hotels – mobile") is the classic anti-pattern.
- Define the **intercompany counterparty** as a dimension from day one; eliminations depend on it.
- Map natural accounts to **reporting hierarchies** (IFRS/US GAAP line items, statutory local charts such as the French PCG or the German SKR, tax reporting, XBRL taxonomy elements) with mapping tables rather than duplicate accounts.
- Segment reporting (IFRS 8 / ASC 280) and the US disaggregation rules (ASU 2024-03, see 2.9) need dimensions that exist *at posting time*; they are very expensive to retrofit.

[ASSUMPTION/JUDGEMENT]

### 1.4 General ledger vs subledgers vs operational systems

| Layer | Holds | Granularity | Example |
| --- | --- | --- | --- |
| Operational systems | Business events (bookings, orders, payments, usage) | Per event, high volume | Booking engine, payments platform, billing |
| Subledgers | Accounting-relevant detail with an accounting treatment applied | Per document / customer / supplier / asset | Accounts receivable (AR), accounts payable (AP), fixed assets, revenue subledger, lease subledger, inventory |
| General ledger (GL) | Summarised balances by account and dimension | Summarised (daily or per batch), with drill-back | ERP GL |

The subledger's control account in the GL (for example, "Trade receivables") must reconcile to the sum of open items in the subledger. **Subledger-to-GL reconciliation** is one of the most important key controls. [ASSUMPTION/JUDGEMENT]

The trend in high-volume businesses (marketplaces, payments, telecoms, travel) is an **accounting hub / event-based subledger** that turns operational events into accounting entries using rules, posts summarised journals to the ERP GL, and keeps line-level detail for drill-down and audit. [ASSUMPTION/JUDGEMENT — industry pattern; vendor-neutral framing]

### 1.5 Trial balance

A trial balance lists every account's balance at a date; total debits must equal total credits. It is the starting point for financial statements and for the auditor's work. A balanced trial balance proves only the double-entry invariant held — **not** that entries are correct (misclassification, wrong period, omitted transactions all leave it balanced). [ASSUMPTION/JUDGEMENT]

### 1.6 Accrual vs cash basis

- **Cash basis**: record revenue when cash is received and expense when paid.
- **Accrual basis**: record revenue when earned (per IFRS 15 / ASC 606) and expenses when incurred, regardless of cash timing.

IFRS and US GAAP financial statements (other than the cash-flow statement) are prepared on the accrual basis. [ASSUMPTION/JUDGEMENT — IAS 1 / IFRS 18 and the Conceptual Framework require accrual basis; not re-fetched in this pass]

Architectural consequence: operational systems are mostly cash- or event-driven; the finance stack must generate accruals, deferrals and timing adjustments on top of them.

### 1.7 Period close, accruals, deferrals, reversing entries and adjustments

**Period close** is the process of making a period's books complete, accurate and locked: subledger cut-off, accruals, reconciliations, FX revaluation, intercompany matching and eliminations, consolidation, review, then period lock. [ASSUMPTION/JUDGEMENT]

| Concept | What it does | Typical example |
| --- | --- | --- |
| Accrued expense | Recognise an expense incurred but not invoiced | Cloud hosting used in March, invoiced in April |
| Accrued revenue / unbilled receivable (contract asset if conditional) | Recognise revenue earned but not billed | Usage consumed in March, billed in April |
| Prepaid expense (deferral) | Defer an expense paid in advance | Annual software licence paid in January |
| Deferred revenue / contract liability | Defer revenue billed or collected before performance | Annual subscription paid upfront |
| Reversing entry | Auto-reverse an accrual on day 1 of the next period, so the actual invoice posts normally | Month-end accrual for unbilled supplier costs |
| Adjusting entry | Correct or true-up balances at period end | Bad-debt provision, inventory write-down |

**Worked example — accrual and reversal (EUR)**

| Date | Account | Debit | Credit | Note |
| --- | --- | --- | --- | --- |
| 31 Mar | Hosting expense | 10,000 | | Accrue March usage (estimate) |
| 31 Mar | Accrued liabilities | | 10,000 | |
| 1 Apr | Accrued liabilities | 10,000 | | Auto-reversal |
| 1 Apr | Hosting expense | | 10,000 | |
| 15 Apr | Hosting expense | 10,300 | | Supplier invoice arrives via AP |
| 15 Apr | Trade payables | | 10,300 | Net April effect: 300 true-up |

[ASSUMPTION/JUDGEMENT — illustrative]

Architectural point: reversals must be **system-generated and linked** to the original entry, and estimates should carry their basis (driver data) so that the accrual is auditable.

### 1.8 Intercompany and eliminations

Groups trade between their own legal entities (management fees, IP royalties, intra-group loans, cost recharges, cash pooling). Each side records its half; consolidation **eliminates** intercompany balances, revenues/expenses and unrealised profit so that the group presents only transactions with third parties (IFRS 10 / ASC 810). [ASSUMPTION/JUDGEMENT — standards named from general knowledge]

**Worked example — intercompany service charge and elimination**

| Entity | Account | Debit | Credit |
| --- | --- | --- | --- |
| HoldCo (NL) | Intercompany receivable – OpCo | 500,000 | |
| HoldCo (NL) | Intercompany revenue – management fees | | 500,000 |
| OpCo (US) | Management fee expense – intercompany | 500,000 | |
| OpCo (US) | Intercompany payable – HoldCo | | 500,000 |
| Consolidation | Intercompany revenue | 500,000 | |
| Consolidation | Management fee expense | | 500,000 |
| Consolidation | Intercompany payable | 500,000 | |
| Consolidation | Intercompany receivable | | 500,000 |

Common failure modes: the two sides use different FX rates or post in different periods, so they do not match; a counterparty dimension is missing; transfer-pricing charges are calculated outside the ERP and booked late. Intercompany matching and dispute resolution is a recurring close bottleneck. [ASSUMPTION/JUDGEMENT]

### 1.9 Currency: functional vs presentation, transaction FX, revaluation, translation, CTA

Definitions (IAS 21; the US equivalent is ASC 830):

- **Functional currency**: the currency of the primary economic environment in which the entity operates. It is determined by facts (sales prices, costs, financing), not chosen freely. [VERIFIED: https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/]
- **Presentation currency**: the currency in which financial statements are presented; an IFRS entity may choose it. [VERIFIED: https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/]
- **Transaction currency**: the currency of an individual transaction (e.g. a USD invoice in a EUR entity).

Three distinct FX processes that systems often conflate:

1. **Initial recognition**: a foreign-currency transaction is recorded in the functional currency at the spot rate on the transaction date (an average rate for a period is allowed as a practical approximation if rates do not fluctuate significantly). [ASSUMPTION/JUDGEMENT — IAS 21 para. 21–22, from general knowledge]
2. **Remeasurement / revaluation** at each reporting date: **monetary items** (cash, receivables, payables, loans) are retranslated at the closing rate; the difference goes to **profit or loss** as an FX gain/loss. Non-monetary items at historical cost (fixed assets, prepaid expenses, deferred revenue in most analyses) stay at the historical rate. [ASSUMPTION/JUDGEMENT — IAS 21 para. 23, 28; ASC 830-20]
3. **Translation** of a foreign operation's financial statements into the group's presentation currency: assets and liabilities at the closing rate, income and expenses at transaction-date rates (or average), equity at historical rates. The balancing difference goes to **other comprehensive income** as the **cumulative translation adjustment (CTA)** / foreign currency translation reserve, and is reclassified to P&L on disposal of the foreign operation. [ASSUMPTION/JUDGEMENT — IAS 21 para. 39, 48; ASC 830-30]

**Worked example — revaluation of a USD receivable in a EUR-functional entity**

| Date | Rate (EUR per USD) | Event | Entry (EUR) |
| --- | --- | --- | --- |
| 10 Mar | 0.90 | Invoice USD 100,000 | Dr Receivable 90,000 / Cr Revenue 90,000 |
| 31 Mar | 0.92 | Month-end revaluation | Dr Receivable 2,000 / Cr Unrealised FX gain (P&L) 2,000 |
| 1 Apr | — | (Optional) reverse unrealised revaluation | Dr Unrealised FX gain 2,000 / Cr Receivable 2,000 |
| 20 Apr | 0.91 | Cash received USD 100,000 | Dr Cash 91,000 / Cr Receivable 90,000 / Cr Realised FX gain 1,000 |

Revenue stays at 90,000; only the monetary item is remeasured. [ASSUMPTION/JUDGEMENT — illustrative]

Time-sensitive note: IAS 21 amendments *Lack of Exchangeability* (estimating a spot rate when a currency cannot be exchanged) apply to annual periods beginning on or after 1 January 2025. [WIDELY REPORTED: https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/]

Architecture points: keep a governed **rate table** (source, rate type: spot/closing/average/budget, timestamp), store the rate used on every line, and keep transaction-currency amounts alongside functional and group amounts. Hyperinflationary economies (IAS 29 / ASC 830 highly inflationary rules) need special handling. [ASSUMPTION/JUDGEMENT]

---

## 2. Revenue recognition

### 2.1 The five-step model (IFRS 15 / ASC 606)

IFRS 15 and ASC Topic 606 were issued jointly in May 2014 and are substantially converged. [VERIFIED: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/]

1. **Identify the contract** with a customer (enforceable rights and obligations; collectability probable).
2. **Identify the performance obligations** — distinct promised goods or services.
3. **Determine the transaction price**, including variable consideration (subject to a constraint), significant financing components, non-cash consideration, and consideration payable to the customer.
4. **Allocate the transaction price** to performance obligations on a relative **standalone selling price (SSP)** basis.
5. **Recognise revenue when (or as) each performance obligation is satisfied** — at a point in time (transfer of control) or over time.

[VERIFIED: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/] (the five-step structure is stated on the IFRS Foundation page; detailed paragraph references are from general knowledge)

Known divergences between IFRS 15 and ASC 606 that matter to systems: collectability threshold ("probable" means different things under IFRS and US GAAP), shipping and handling policy election (US GAAP), licensing renewals, and some presentation of sales taxes (US GAAP permits a policy election to present net). [ASSUMPTION/JUDGEMENT — known differences; re-verify against a Big-4 comparison guide before publishing specific claims]

### 2.2 Performance obligations and timing

A good or service is distinct if the customer can benefit from it on its own (or with readily available resources) **and** it is separately identifiable in the contract. Revenue is recognised **over time** if one of three criteria is met (e.g. the customer simultaneously receives and consumes the benefit — typical for SaaS), otherwise at a point in time. [ASSUMPTION/JUDGEMENT — IFRS 15 para. 27, 35; ASC 606-10-25-19, 25-27]

### 2.3 Principal vs agent (gross vs net)

The entity is a **principal** if it **controls** the specified good or service before it is transferred to the customer; it then reports revenue **gross**. If it arranges for another party to provide it, it is an **agent** and reports revenue **net** (its commission or fee). Indicators of control include primary responsibility for fulfilment, inventory risk, and discretion in setting price. The indicators support the control assessment; they are not a checklist that overrides it. [ASSUMPTION/JUDGEMENT — IFRS 15 B34–B38; ASC 606-10-55-36 to 55-40; the 2016 clarifying amendments moved the emphasis from "risks and rewards" to control]

The assessment is made **per specified good or service**, so one platform can be principal for some products and agent for others. [ASSUMPTION/JUDGEMENT]

**Travel marketplace contrast (illustrative)**

| Model | Typical facts | Likely conclusion | Revenue line |
| --- | --- | --- | --- |
| Agency model | Platform lists hotel rooms; traveller pays the hotel at stay; hotel pays the platform a commission | Agent: the platform never controls the room night | Commission only (net) |
| Merchant model | Platform collects payment from the traveller at booking, pays the hotel later; the hotel still provides the room and sets core terms | Still often **agent** (net), despite the platform holding cash, because it does not control the room before transfer; the margin is recognised as revenue | Net margin; customer cash shown as a liability until paid on |
| Pre-purchased inventory | Platform commits to buy room allotments with no right of return, bears unsold-inventory risk and sets prices | May be principal (gross) | Gross room price; cost of rooms as cost of sales |

[ASSUMPTION/JUDGEMENT — illustrative; facts vary, and large online travel companies disclose different conclusions for different product lines. Chapter writers should cite the specific company's 10-K revenue-recognition note if naming a company.]

Key teaching point: **collecting the cash does not make you the principal**. Merchant-of-record status, payment flow and tax obligations (e.g. VAT "deemed supplier" rules — see 4.3) are separate questions from the IFRS 15 / ASC 606 principal-versus-agent assessment. [ASSUMPTION/JUDGEMENT — important; tax deemed-supplier status does not determine accounting presentation]

**Worked example — merchant-model booking, agent conclusion (EUR)**

Traveller pays 1,000 at booking; hotel is owed 850; stay occurs one month later; platform pays the hotel after the stay.

| Date | Account | Debit | Credit | Note |
| --- | --- | --- | --- | --- |
| Booking | Cash (or receivable from payment processor) | 1,000 | | |
| Booking | Customer deposits / amounts due to suppliers (liability) | | 1,000 | Nothing earned yet; cancellation possible |
| Stay (performance obligation satisfied) | Customer deposits | 1,000 | | |
| Stay | Payable to hotel | | 850 | |
| Stay | Revenue – net merchant margin | | 150 | Agent: net |
| Payment to hotel | Payable to hotel | 850 | | |
| Payment to hotel | Cash | | 850 | |

[ASSUMPTION/JUDGEMENT — the point at which the agent's obligation is satisfied (booking vs stay) is a judgement that varies by contract terms; some platforms recognise at booking when their service is complete and cancellation risk is low. Chapter writers must not present one timing as universal.]

### 2.4 Contract liabilities, deferred revenue, customer funds held

- **Contract liability**: the obligation to transfer goods or services for which consideration has been received (or is due). "Deferred revenue" is the common label. **Contract asset**: a right to consideration conditional on something other than the passage of time; once unconditional it is a receivable. [ASSUMPTION/JUDGEMENT — IFRS 15 para. 105–108]
- **Customer funds held / amounts payable to third parties**: cash an agent collects on behalf of a principal is **not** a contract liability for the agent's own revenue; it is a payable to the principal (hotel, seller, driver). Keep them in separate accounts. [ASSUMPTION/JUDGEMENT]
- **Regulated funds**: if the business is a payment or e-money institution, those funds may also be subject to **safeguarding** rules (see 4.9), which drive segregated bank accounts and daily reconciliations. [ASSUMPTION/JUDGEMENT]

### 2.5 Commission revenue

For an agent, revenue is the commission or fee, recognised when the agent's own promise (arranging the transaction) is satisfied. When the commission depends on a later event (e.g. stay completed, no cancellation), it is **variable consideration** and is subject to the constraint. [ASSUMPTION/JUDGEMENT]

### 2.6 Variable consideration

Discounts, rebates, refunds, credits, incentives, performance bonuses, penalties and usage-based fees are variable consideration. Estimate using the **expected value** or **most likely amount** method, then **constrain** to the amount for which it is *highly probable* (IFRS) / *probable* (US GAAP — the boards intended the same meaning here) that a significant reversal will not occur. Re-estimate each period. [ASSUMPTION/JUDGEMENT — IFRS 15 para. 50–59]

Practical systems consequence: refund and cancellation reserves need **historical data by cohort** and a governed estimation model; the model and its inputs become key controls (see IPE, 3.6). [ASSUMPTION/JUDGEMENT]

### 2.7 Subscriptions and usage billing

- Standard SaaS subscription: a stand-ready obligation satisfied over time; recognise ratably over the service period. Billing annually in advance creates a contract liability that unwinds monthly.
- Usage-based fees: often recognised as usage occurs, using the **variable consideration allocation exception** (allocate variable fees entirely to the distinct period in which they arise) or the **"as-invoiced" practical expedient** when the invoiced amount corresponds directly to value delivered.
- Sales-based or usage-based royalties on licences of IP have a specific exception (recognise when the later of the sale/usage or satisfaction occurs).

[ASSUMPTION/JUDGEMENT — IFRS 15 para. 85, B16, B63; ASC 606-10-32-40, 55-18, 55-65]

**Worked example — annual subscription billed upfront (EUR)**

| Date | Account | Debit | Credit |
| --- | --- | --- | --- |
| 1 Jan (invoice) | Trade receivable | 12,000 | |
| 1 Jan | Contract liability (deferred revenue) | | 12,000 |
| 31 Jan (and monthly) | Contract liability | 1,000 | |
| 31 Jan | Subscription revenue | | 1,000 |

[ASSUMPTION/JUDGEMENT — illustrative; some practitioners recognise the receivable only when payment is due under a non-cancellable contract.]

Billing (invoices, the legal and tax document) and revenue recognition (the accounting schedule) are **different processes** that must reconcile. A billing system is not a revenue subledger. [ASSUMPTION/JUDGEMENT]

### 2.8 SSP allocation

Allocate the transaction price to performance obligations in proportion to their **standalone selling prices**; if not observable, estimate using adjusted market assessment, expected cost plus margin, or (limited circumstances) the residual approach. Discounts are allocated proportionally unless specific criteria are met. [ASSUMPTION/JUDGEMENT — IFRS 15 para. 73–86]

**Worked example — bundle allocation**

Bundle price 900 for software licence (SSP 600) + one year support (SSP 400). Total SSP 1,000.

| Obligation | SSP | Allocation | Recognition |
| --- | --- | --- | --- |
| Licence | 600 | 540 | Point in time (delivery) |
| Support | 400 | 360 | Ratably over 12 months (30/month) |

[ASSUMPTION/JUDGEMENT — illustrative]

SSP tables are reference data with an owner, versioning, effective dates and an approval trail — they directly drive reported revenue. [ASSUMPTION/JUDGEMENT]

### 2.9 Presentation changes that hit finance systems (time-sensitive)

- **IFRS 18** *Presentation and Disclosure in Financial Statements* replaces IAS 1 for annual periods beginning on or after **1 January 2027** (earlier application permitted). It introduces defined P&L categories (operating, investing, financing), required subtotals, and disclosure of **management-defined performance measures (MPMs)** in a single note. Comparative periods must be restated, so 2026 data needs IFRS 18 classification capability. [WIDELY REPORTED: https://www.ey.com/content/dam/ey-unified-site/ey-com/en-za/services/ifrs/documents/ey-ifrs18-brochure.pdf] **TIME-SENSITIVE** (EU endorsement status should be re-checked).
- **ASU 2024-03** (*Disaggregation of Income Statement Expenses*, "DISE"), as clarified by **ASU 2025-01**: US public business entities adopt for annual periods beginning after **15 December 2026** and interim periods beginning after 15 December 2027. It requires footnote disaggregation of relevant expense captions into categories such as purchases of inventory, employee compensation, depreciation and intangible amortisation. [WIDELY REPORTED: https://dart.deloitte.com/USDART/home/news/all-news/2025/jan/fasb-effective-date-asu-disaggregation-income-statement] **TIME-SENSITIVE**

Both are classic examples of "a disclosure change that is really a data-model change": the categorisation must exist at posting time or be derivable from dimensions. [ASSUMPTION/JUDGEMENT]

### 2.10 Leases (IFRS 16 / ASC 842), briefly

- **IFRS 16** (effective 2019): a single lessee model — a **right-of-use asset** and a **lease liability** for almost all leases (exemptions for short-term and low-value leases); depreciation plus interest in P&L. [ASSUMPTION/JUDGEMENT — from general knowledge; https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/]
- **ASC 842** (effective 2019 for US public companies): also on-balance-sheet, but keeps the **finance vs operating** classification for lessees; operating leases have a straight-line single lease cost. [ASSUMPTION/JUDGEMENT]
- Systems impact: a lease subledger (contract terms, modifications, index-linked payments, discount rates, remeasurements) with schedule generation and GL posting; data collection (finding embedded leases in service contracts, e.g. dedicated data-centre capacity) is usually the hard part. [ASSUMPTION/JUDGEMENT]

---

## 3. Controls: ICFR, SOX, COSO, ITGCs, SOC reports

### 3.1 SOX 302 and 404

- **Section 302**: the CEO and CFO certify each quarterly and annual report — including that they are responsible for disclosure controls and have evaluated them, and have disclosed significant deficiencies, material weaknesses and fraud to auditors and the audit committee. [ASSUMPTION/JUDGEMENT — Sarbanes-Oxley Act 2002 s.302; SEC rules 13a-14/15d-14]
- **Section 404(a)**: management's annual report on the effectiveness of **internal control over financial reporting (ICFR)**, using a suitable framework (in practice COSO 2013). [ASSUMPTION/JUDGEMENT]
- **Section 404(b)**: the external auditor's attestation on ICFR — required for accelerated and large accelerated filers; non-accelerated filers (including many smaller companies) are exempt from 404(b) but not 404(a). [ASSUMPTION/JUDGEMENT — SEC guidance; re-verify current filer-status thresholds before quoting numbers]
- SEC interpretive guidance for management's evaluation (2007) sets a risk-based, top-down approach. [ASSUMPTION/JUDGEMENT — https://www.sec.gov/rules/interp/2007/33-8810.pdf, not re-fetched]

**Time-sensitive SEC item**: on 5 May 2026 the SEC proposed allowing domestic registrants to elect **semiannual reporting** (a new Form 10-S) instead of quarterly 10-Qs; comments closed 6 July 2026. As of the latest sources found, it remains a proposal. If adopted, it changes close cadence and 302 certification frequency for electing companies, not ICFR obligations. [WIDELY REPORTED: https://www.dlapiper.com/insights/publications/2026/05/sec-proposes-optional-semiannual-reporting-for-public-companies] **TIME-SENSITIVE**

### 3.2 COSO 2013 Internal Control — Integrated Framework

Five components and 17 principles; effective internal control requires each component and each relevant principle to be **present and functioning** and the components to operate together. The 2013 update codified principles implicit in the 1992 framework, which was superseded after 15 December 2014. [WIDELY REPORTED: https://www.iasplus.com/en/publications/us/heads-up/2013/coso]

| Component | Principles |
| --- | --- |
| Control environment | 1 Integrity and ethical values; 2 Board independence and oversight; 3 Structures, reporting lines, authorities; 4 Commitment to competence; 5 Accountability |
| Risk assessment | 6 Specifies suitable objectives; 7 Identifies and analyses risk; 8 Assesses fraud risk; 9 Identifies and analyses significant change |
| Control activities | 10 Selects and develops control activities; 11 Selects and develops **general controls over technology**; 12 Deploys through policies and procedures |
| Information and communication | 13 Uses relevant, quality information; 14 Communicates internally; 15 Communicates externally |
| Monitoring activities | 16 Ongoing and/or separate evaluations; 17 Evaluates and communicates deficiencies |

[ASSUMPTION/JUDGEMENT — principle wording paraphrased from the framework; numbering matches COSO 2013]

For architects, principles **11** (technology general controls) and **13** (quality information — the root of IPE expectations) are where system design directly shows up in the audit. [ASSUMPTION/JUDGEMENT]

### 3.3 PCAOB AS 2201

AS 2201 (*An Audit of Internal Control Over Financial Reporting That Is Integrated with an Audit of Financial Statements*) governs the US 404(b) audit. Key concepts: a **top-down, risk-based** approach starting at the financial statement level and entity-level controls, then significant accounts, relevant assertions and the controls that address them; walkthroughs; and the definitions of **material weakness** (a reasonable possibility that a material misstatement will not be prevented or detected on a timely basis) and **significant deficiency** (less severe, but merits attention of those charged with governance). [ASSUMPTION/JUDGEMENT — standard text at https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201; the page returned HTTP 403 to the research tool, so wording is from general knowledge]

### 3.4 ITGCs (IT general controls)

ITGCs are the controls over the IT environment that let auditors rely on automated controls and system-generated data. Typical domains:

| Domain | What auditors look for |
| --- | --- |
| Logical access | Provisioning approved, timely deprovisioning of leavers, periodic user access reviews, privileged/admin access restricted and monitored, generic/shared accounts controlled, service accounts owned |
| Change management | Changes authorised, tested, approved before production; segregation between developers and production deployment (or compensating controls such as peer review plus automated pipelines with immutable logs); emergency change process |
| IT operations | Job scheduling and monitoring, interface failure handling, backup and recovery, incident management |
| SDLC / program development | Controls over new system implementations and data migrations (migration completeness and accuracy reconciliations are a frequent audit focus) |

[ASSUMPTION/JUDGEMENT — common audit-firm taxonomy; COSO principle 11]

Modern-engineering note: continuous deployment is compatible with ITGCs if the pipeline enforces review, testing and traceability, and if pipeline configuration changes are themselves controlled. Auditors want **evidence that the control operated for every change in the period**, not just a policy. [ASSUMPTION/JUDGEMENT]

### 3.5 Application controls

Automated controls inside applications: input validation, three-way match (PO / goods receipt / invoice), credit limits, posting-period locks, balanced-entry enforcement, duplicate invoice detection, automated calculations (revenue schedules, depreciation, FX revaluation), interface completeness checks (record counts and hash totals). An automated control is typically tested once (a "test of one") plus reliance on effective ITGCs ("benchmarking" over time) — weak ITGCs undermine reliance on every automated control. [ASSUMPTION/JUDGEMENT]

### 3.6 Key reports and IPE (information produced by the entity)

Any report, query, spreadsheet or extract used **in the performance of a control** (e.g. an aged receivables report used in a reserve review) or as **audit evidence** must be shown to be **complete and accurate**. Auditors test the report logic (source, parameters, filters), and the ITGCs over it. Since around 2015–2016 PCAOB inspection findings repeatedly cited deficiencies in testing IPE and management review controls, making IPE a sustained focus. [ASSUMPTION/JUDGEMENT — widely known audit trend; specific PCAOB inspection reports not re-fetched]

Architecture consequence: data platforms, BI dashboards and reconciliation tools used by finance become **in-scope systems** once a key control depends on them. A data lake feeding a key reconciliation drags its pipelines into ITGC scope. [ASSUMPTION/JUDGEMENT]

### 3.7 Segregation of duties (SoD)

No single person should be able to initiate, approve, record and reconcile the same transaction (e.g. create a vendor *and* approve payments to it; post *and* approve manual journals). SoD is implemented through role design in ERP and adjacent systems, conflict rulesets, and compensating detective controls where conflicts are unavoidable (small teams). Cross-system SoD (e.g. access to the payments platform *and* the GL) is a frequent gap. [ASSUMPTION/JUDGEMENT]

### 3.8 SOC 1 Type II and CUECs — critical for SaaS ERPs

- A **SOC 1** report (performed under AICPA attestation standard SSAE 18, AT-C 320) covers a service organisation's controls relevant to **user entities' ICFR**. **Type I**: design at a point in time. **Type II**: design and **operating effectiveness over a period** (typically 6–12 months). The international equivalent is an ISAE 3402 report. [ASSUMPTION/JUDGEMENT — https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-1, not re-fetched]
- **SOC 2** covers the Trust Services Criteria (security, availability, etc.) — useful for vendor risk, but **not a substitute for SOC 1** when the service affects financial reporting. [ASSUMPTION/JUDGEMENT]
- **Complementary user entity controls (CUECs)** are controls the *customer* must operate for the service organisation's controls to achieve their objectives — e.g. "user entities are responsible for granting and reviewing access to their tenant", "for reviewing interface error reports", "for approving configuration changes". Every CUEC must be mapped to an owned, tested control in the customer's control framework. [ASSUMPTION/JUDGEMENT]
- **Complementary subservice organisation controls (CSOCs)**: when the SaaS vendor relies on a hyperscaler, the report may use the **carve-out** method, pushing reliance down to the subservice provider's own reports. [ASSUMPTION/JUDGEMENT]
- **Coverage gaps**: if the SOC 1 period ends before the customer's fiscal year-end, a **bridge (gap) letter** from the vendor plus the customer's own monitoring covers the gap. Exceptions noted in the report must be assessed for impact. [ASSUMPTION/JUDGEMENT]

Architect takeaways: (1) a SaaS ERP **transfers operation of** but not **accountability for** controls; (2) your configuration, integrations, roles and reports remain fully in scope; (3) obtain and review SOC 1 Type II reports annually for every finance-relevant SaaS (ERP, billing, payroll, revenue subledger, payments, consolidation, tax engine). [ASSUMPTION/JUDGEMENT]

### 3.9 Audit trail requirements

Auditors and regulators expect: immutable posted records; who/what/when for creation, approval and changes; preserved before/after values for master-data changes (vendor bank details, customer credit limits, account mappings, SSP tables); traceability from financial statement line to GL to subledger to source document; and logs retained for the retention period. Jurisdictions add specifics (e.g. Germany's GoBD for electronic bookkeeping; France's FEC — *fichier des écritures comptables* — standard GL export required on tax audit; Spain's Verifactu for invoicing software integrity). [ASSUMPTION/JUDGEMENT — country items from general knowledge except Verifactu, see 4.4]

### 3.10 Non-US regimes: UK Provision 29 and the EU

- **UK Corporate Governance Code 2024**: the Code applies to financial years beginning on or after 1 January 2025; **Provision 29** (board declaration on the effectiveness of **material controls** — financial, operational, reporting and compliance — as at the balance-sheet date, with a description of any material controls that did not operate effectively and remediation) applies to financial years beginning on or after **1 January 2026**. [VERIFIED: https://www.frc.org.uk/library/standards-codes-policy/corporate-governance/uk-corporate-governance-code/]
  - So the first declarations for December year-ends appear in annual reports published in early 2027. [ASSUMPTION/JUDGEMENT — follows from the date]
  - It is "comply or explain" for premium/commercial-company listed issuers; there is **no mandatory external audit attestation** and the FRC does not prescribe the declaration wording or what is "material" — boards decide. [WIDELY REPORTED: https://assets.kpmg.com/content/dam/kpmgsites/ie/pdf/insights/consulting/ie-uk-corporate-governance-code-provision-29.pdf]
  - It is **broader than SOX** (not limited to financial reporting) but **lighter** (no auditor opinion). Do not call it "UK SOX". [ASSUMPTION/JUDGEMENT]
- **EU**: there is **no EU-wide SOX equivalent** requiring management ICFR assessments with auditor attestation. EU-level requirements come through the Accounting Directive (corporate governance statement describing internal control and risk management systems for financial reporting, for listed companies), the Audit Regulation/Directive (auditor reports to audit committees), and sectoral rules (CRD for banks, Solvency II for insurers, DORA for ICT risk). Some member states have stronger national regimes (e.g. France's *Loi de sécurité financière* reporting on internal control; Germany's FISG 2021 requirement for listed-company boards to have an appropriate internal control and risk management system). [ASSUMPTION/JUDGEMENT — national examples from general knowledge; verify before naming specific provisions]

---

## 4. Regulatory and tax trends affecting finance systems

### 4.1 OECD Pillar Two (GloBE) — status as of October 2026

Mechanics:

- Applies to MNE groups with consolidated revenue of at least **EUR 750 million** in two of the four preceding years. Computes an effective tax rate **per jurisdiction** and collects top-up tax to **15%**. [ASSUMPTION/JUDGEMENT — OECD Model Rules 2021, from general knowledge]
- Charging mechanisms in order of priority: **QDMTT** (qualified domestic minimum top-up tax, collected by the source jurisdiction itself), **IIR** (income inclusion rule, at parent level), **UTPR** (undertaxed profits rule, backstop). [ASSUMPTION/JUDGEMENT]
- **GloBE Information Return (GIR)**: standardised return; first filing due **18 months** after the end of the first fiscal year in scope (15 months thereafter). For calendar-year 2024, the first GIR/top-up tax filings fell due **30 June 2026** in many jurisdictions. [WIDELY REPORTED: https://globaltaxnews.ey.com/news/2026-0244] Ireland, for example, set its first top-up tax return and pay-and-file deadline at 30 June 2026. [VERIFIED: https://www.revenue.ie/en/companies-and-charities/pillar-two/dates/index.aspx]
- Some jurisdictions moved first deadlines (reported: France to 1 September 2026; Turkey to 31 July 2026); and an OECD common approach (18 May 2026) lets tax administrations refrain from enforcing local filing for six months after deadlines falling on or before 31 December 2026 if conditions are met. [VERIFIED for the Irish application of the common approach: https://www.revenue.ie/en/companies-and-charities/pillar-two/dates/index.aspx; country extensions WIDELY REPORTED: https://oecdpillars.com/lithuania-updates-draft-globe-legislation/] **TIME-SENSITIVE**

**Side-by-Side package (5 January 2026)**: The OECD/G20 Inclusive Framework adopted a package containing: a **Side-by-Side system** recognising qualifying existing domestic minimum-tax regimes (in practice exempting **US-parented groups** from the IIR and UTPR for periods beginning on or after 1 January 2026, while QDMTTs still apply); a **permanent simplified ETR safe harbour** (based on financial-accounting data, from 2027 with possible early election for 2026); a **one-year extension of the transitional CbCR safe harbour** (to fiscal years beginning on or before 31 December 2027); and a **substance-based tax incentive safe harbour**. The European Commission published a Notice (C/2026/253) on 12 January 2026 on the EU interaction. [VERIFIED for package date and EU notice: https://www.revenue.ie/en/companies-and-charities/pillar-two/dates/index.aspx; content WIDELY REPORTED: https://bdo.com/insights/tax/oecd-releases-guidance-on-side-by-side-system and https://www.deloitte.com/ie/en/services/tax/perspectives/oecd-side-by-side.html] **TIME-SENSITIVE**

Finance-systems impact: GloBE needs **jurisdiction-by-constituent-entity** data that sits between statutory accounts, consolidation (the GloBE calculation starts from the financial accounts used for consolidation, before eliminations), tax provisioning and CbCR. Typical gaps: deferred-tax data by entity, intra-group transaction data, data lineage for the many GloBE adjustments, and evidence retention for multi-year recapture rules. The permanent simplified ETR safe harbour, which leans on accounting data, increases the premium on clean entity-level financials. [ASSUMPTION/JUDGEMENT]

### 4.2 EU VAT in the Digital Age (ViDA)

Adopted 11 March 2025; published in the Official Journal 25 March 2025 as Directive (EU) 2025/516, Regulation (EU) 2025/517 and Implementing Regulation (EU) 2025/518; in force 14 April 2025. [VERIFIED: https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en]

| Pillar | Date | Detail |
| --- | --- | --- |
| E-invoicing (domestic) | From 14 April 2025 | Member states may impose mandatory domestic e-invoicing without EU derogation. |
| OSS/IOSS clarifications | 1 January 2027 | |
| Platform "deemed supplier" (short-term accommodation rental; passenger transport by road) | 1 July 2028 | Member states may delay until 1 January 2030. |
| Single VAT Registration (OSS extension; mandatory reverse charge for non-established suppliers) | 1 July 2028 | |
| Digital Reporting Requirements (DRR) + mandatory e-invoicing for intra-EU B2B | 1 July 2030 | Near-real-time transaction reporting for cross-border B2B; EN 16931 structured e-invoices as the default. |
| Alignment of existing domestic real-time reporting systems | 1 January 2035 | |

[VERIFIED: https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en]

Deemed-supplier mechanics: where the underlying provider does not charge VAT (e.g. private hosts, non-VAT-registered drivers), the platform is treated as having received and supplied the service itself and must charge VAT. The platform is relieved where the provider gives a valid VAT identification and declares it will account for VAT. [WIDELY REPORTED: https://www.pwc.lu/en/newsletter/2025/vat-in-the-digital-age-vida.html]

Architect's key point: **deemed supplier for VAT does not make the platform the principal for revenue recognition**. Systems will need the tax treatment and the accounting treatment as separate attributes of a transaction. (Some platforms may need to evaluate VAT as a cost or a pass-through in pricing, a commercial decision with margin effects.) [ASSUMPTION/JUDGEMENT]

### 4.3 National e-invoicing mandates (state as of October 2026)

| Country | Status | Evidence |
| --- | --- | --- |
| Italy | B2B e-invoicing through the SdI (Sistema di Interscambio) clearance platform mandatory since 1 January 2019 (extended to most flat-rate taxpayers from 2024). | [ASSUMPTION/JUDGEMENT — well-known; not re-fetched] |
| France | Receive: all VAT-registered businesses from **1 September 2026**. Issue + e-reporting: large and mid-sized companies from 1 September 2026; SMEs and micro-enterprises from **1 September 2027**. Exchange through certified platforms (PDPs, now termed *plateformes agréées*). | [WIDELY REPORTED: https://cms.law/en/fra/news-information/electronic-invoicing-what-does-the-reform-entail] **TIME-SENSITIVE**: the first phase has just gone live; verify any tolerance measures on impots.gouv.fr. |
| Germany | Receive structured e-invoices (EN 16931: XRechnung, ZUGFeRD ≥2.0.1) from 1 January 2025 for all domestic B2B. Issue: mandatory from 1 January 2027 for businesses with prior-year turnover above EUR 800,000; all from 1 January 2028. EDI permitted transitionally. | [WIDELY REPORTED: https://www.avalara.com/us/en/blog/germany-e-invoicing.html] |
| Poland | KSeF mandatory: large taxpayers (2024 sales > PLN 200m) from **1 February 2026**; other taxpayers from **1 April 2026**; smallest (sales ≤ PLN 10,000/month) from **1 January 2027**. Penalties for KSeF errors deferred through 2026; a proposal (16 Sept 2026) would extend the deferral to 31 December 2027. | [WIDELY REPORTED: https://www.ey.com/en_gl/technical/tax-alerts/poland-signs-into-law-mandatory-national-e-invoicing-system and https://lookuptax.com/tax-changes/poland/ksef-penalty-deferral-2027-announced] **TIME-SENSITIVE** — one secondary source characterises April 2026 differently; verify on ksef.podatki.gov.pl. |
| Belgium | Domestic B2B structured e-invoicing mandatory from **1 January 2026** via Peppol (EN 16931); conditional penalty tolerance ended 31 March 2026. Near-real-time e-reporting planned from **1 January 2028** (draft law, not yet enacted as of the latest sources). | [WIDELY REPORTED: https://www.vertexinc.com/resources/resource-library/belgiums-2026-e-invoicing-regulations-explained-scope-deadlines-and-penalties] **TIME-SENSITIVE** |
| Spain | **Verifactu** (invoicing-software integrity and optional real-time submission to AEAT) postponed by Royal Decree-law 15/2025 to **1 January 2027** (corporate taxpayers) and **1 July 2027** (others). B2B e-invoicing under the *Crea y Crece* law: Royal Decree 238/2026 reportedly published 31 March 2026, with expected obligations from 1 October 2027 (turnover > EUR 8m) and 1 October 2028 (others) **once the implementing ministerial order is in force** — reported as still pending in mid-2026. | [WIDELY REPORTED: https://www.vatcalc.com/spain/spain-verifactu-delay-till-jan-2027-for-certified-e-invoicing/ and https://kpmg.com/us/en/taxnewsflash/news/2026/03/spain-e-invoicing-mandate-b2b.html] **TIME-SENSITIVE** |

Architectural patterns to describe (vendor-neutral): **post-audit** (exchange e-invoices, tax authority audits later), **clearance** (tax authority validates before the invoice is legally valid — Italy, Poland), **decentralised CTC / five-corner** (Peppol plus reporting to the authority — France, Belgium's planned model). E-invoicing moves the legal invoice into a structured data exchange with failure modes (rejections, network outages, clearance latency) that the order-to-cash design must handle. [ASSUMPTION/JUDGEMENT]

### 4.4 DAC7 platform reporting

Council Directive (EU) 2021/514 (DAC7) requires digital platform operators to collect, verify and report information on sellers (immovable property rental, personal services, sale of goods, transport rental) annually; applies from 1 January 2023, with reports due by **31 January** of the following year (first deadline 31 January 2024). [WIDELY REPORTED: https://news.pwc.be/deadline-for-first-dac7-reporting-now-imminent] Overlaps with the OECD Model Reporting Rules for platforms adopted outside the EU (e.g. UK). DAC7 data (seller identity, TIN, consideration per quarter, fees) and ViDA deemed-supplier data should come from the **same seller master and transaction ledger**. [ASSUMPTION/JUDGEMENT]

### 4.5 Digital services taxes

Several countries levy unilateral DSTs on revenue from specified digital services (e.g. France 3%, Italy 3%, Spain 3%, UK 2%, Austria 5% on online advertising). [ASSUMPTION/JUDGEMENT — rates from general knowledge; not re-verified in this pass] Canada rescinded its DST on 29 June 2025, halting collection scheduled for 30 June 2025, to advance trade negotiations with the US. [VERIFIED: https://www.canada.ca/en/department-finance/news/2025/06/canada-rescinds-digital-services-tax-to-advance-broader-trade-negotiations-with-the-united-states.html] The broader DST landscape is entangled with US trade policy and Pillar One's stalled Amount A. **TIME-SENSITIVE**. Systems need: in-scope revenue identification by user location — a data-model requirement that often does not exist in billing systems. [ASSUMPTION/JUDGEMENT]

### 4.6 US sales tax: Wayfair and marketplace facilitator laws

*South Dakota v. Wayfair, Inc.* (US Supreme Court, 21 June 2018) overturned the physical-presence nexus rule, permitting states to impose sales-tax collection based on **economic nexus** (South Dakota's threshold was USD 100,000 sales or 200 transactions). [ASSUMPTION/JUDGEMENT — case facts from general knowledge; https://www.supremecourt.gov/opinions/17pdf/17-494_j4el.pdf] Since then, essentially all states with a general sales tax adopted economic nexus and **marketplace facilitator** laws making marketplaces collect and remit on behalf of third-party sellers. [WIDELY REPORTED: https://www.avalara.com/us/en/blog/how-marketplace-facilitator-sales-tax-laws-in-different-states-affect-marketplace-sellers.html] Thresholds and whether facilitated sales count towards a seller's own nexus vary by state. Systems implication: tax determination per ship-to jurisdiction (thousands of local rates), exemption-certificate management, and remittance on behalf of others — again distinct from revenue recognition. [ASSUMPTION/JUDGEMENT]

### 4.7 EU DORA

The Digital Operational Resilience Act (Regulation (EU) 2022/2554) has applied since **17 January 2025** to some 20 types of financial entities (banks, insurers, investment firms, payment and e-money institutions, crypto-asset service providers, etc.) and to ICT third-party service providers. Pillars: ICT risk management, ICT incident management and reporting, digital operational resilience testing (including threat-led penetration testing for significant entities), ICT third-party risk (contract terms, register of information), information sharing, and an EU oversight framework for **critical ICT third-party providers**. [VERIFIED: https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en]

Finance-systems relevance: for financial entities, the SaaS ERP, core ledger, payments and treasury platforms are ICT services that may support **critical or important functions**, triggering DORA contractual clauses (audit rights, exit strategies, subcontracting) and the register of information. DORA does **not** apply to non-financial corporates simply because they are large. [ASSUMPTION/JUDGEMENT]

### 4.8 PSD3 / PSR

The Commission proposed PSD3 (a directive) and the Payment Services Regulation (PSR) in June 2023. A provisional political agreement was reached on **27 November 2025**; COREPER endorsed final compromise texts and the Council published them on 23 April 2026. As of the latest sources found, formal adoption and Official Journal publication were **still pending**; most provisions are expected to apply roughly 21 months after entry into force (commentators expect around 2028). [WIDELY REPORTED: https://www.williamfry.com/knowledge/psd3-psr-final-compromise-texts-are-published/ and https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2026/04/impact-of-psd3-are-you-ready.pdf] **TIME-SENSITIVE** — check EUR-Lex.

Themes relevant to finance systems: e-money institutions folded into the payment-institution framework (EMD2 regime absorbed); strengthened **safeguarding** rules; fraud-liability shifts (impersonation fraud refunds, IBAN/name verification); open-banking API performance requirements. [WIDELY REPORTED: https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2026/04/impact-of-psd3-are-you-ready.pdf]

### 4.9 E-money and safeguarding (EMD2, PSD2, UK CASS 15)

- Under the **E-Money Directive 2009/110/EC (EMD2)** and **PSD2 (Directive (EU) 2015/2366) Article 10**, e-money and payment institutions must safeguard customer funds — by **segregation** (separate accounts at credit institutions or secure low-risk assets, protected from other creditors in insolvency) or by **insurance/comparable guarantee**. [ASSUMPTION/JUDGEMENT — from directive texts known generally; not re-fetched]
- The EBA has addressed safeguarding in supervisory work and in its contributions to the PSD3 package; PSD3 harmonises and tightens safeguarding. [ASSUMPTION/JUDGEMENT — no specific EBA guideline number was verified in this pass; chapter writers must not cite a specific "EBA safeguarding guideline" without checking]
- **UK**: the FCA's new safeguarding regime (CASS 15, Policy Statement PS25/12) for payment and e-money institutions took effect **7 May 2026**, requiring daily reconciliations, monthly regulatory returns, an annual safeguarding audit for firms above a threshold, and a resolution pack. [WIDELY REPORTED: https://www.swgroup.com/insights-events/insights/cass-15-safeguarding-for-payments-and-e-money-firms/] **TIME-SENSITIVE**

Systems implication: safeguarding converts treasury reconciliation into a **regulatory** control — daily internal (ledger of client money owed) vs external (bank balances) reconciliation, break management, and segregation of client and own funds in the chart of accounts and bank structure. [ASSUMPTION/JUDGEMENT]

### 4.10 EU AI Act timelines relevant to finance

- The AI Act (Regulation (EU) 2024/1689) entered into force 1 August 2024. Prohibited practices and AI-literacy obligations applied from 2 February 2025; general-purpose AI model obligations from 2 August 2025. [ASSUMPTION/JUDGEMENT — well known; not re-fetched]
- **Digital Omnibus on AI — Regulation (EU) 2026/1744**, published in the OJ on 24 July 2026 and in force since 27 July 2026, **postponed** high-risk obligations: **2 December 2027** for Annex III stand-alone high-risk systems and **2 August 2028** for Annex I product-embedded systems. [WIDELY REPORTED: https://abreuadvogados.com/en/conhecimento/publications/digital-omnibus-regulation-on-ai-the-key-amendments-to-the-ai-act/ and https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/] **TIME-SENSITIVE**
- Finance-relevant Annex III uses: **creditworthiness assessment / credit scoring of natural persons** (excluding fraud detection) and **risk assessment and pricing in life and health insurance**; employment-related AI (e.g. HR screening) is also Annex III. Most finance-function AI (close automation, reconciliation matching, invoice coding, anomaly detection) is **not** high-risk under the Act, though it remains an ICFR matter (model as a control, IPE, change management). [ASSUMPTION/JUDGEMENT — Annex III content from general knowledge]

### 4.11 SEC filing, ESEF and iXBRL

- **SEC**: operating companies file financial statements with **Inline XBRL** (phased in 2019–2021), tagged against the US GAAP taxonomy; cover-page tagging is also required. [ASSUMPTION/JUDGEMENT — https://www.sec.gov/structureddata, not re-fetched]
- **EU ESEF** (Delegated Regulation (EU) 2019/815): issuers with securities on EU regulated markets prepare annual financial reports in **XHTML**, with IFRS consolidated statements marked up in **iXBRL** using the ESEF taxonomy; detailed tagging of primary statements, **block tagging of notes** from financial years beginning on or after 1 January 2022. [ASSUMPTION/JUDGEMENT — from general knowledge; https://www.esma.europa.eu/issuer-disclosure/electronic-reporting]
- Systems implication: the **disclosure management / tagging** layer sits after consolidation; the account-to-taxonomy mapping should be governed like the chart of accounts mapping. [ASSUMPTION/JUDGEMENT]

### 4.12 CSRD and the 2025–2026 Omnibus (high level)

- The **Omnibus I Directive** amending CSRD and CSDDD was published in the OJ on **26 February 2026** and entered into force 18 March 2026. CSRD scope narrows to EU undertakings/groups with **more than 1,000 employees and net turnover above EUR 450 million**; non-EU groups are in scope above EUR 450 million EU turnover with an EU subsidiary or branch above EUR 200 million. New thresholds apply from financial years starting on or after 1 January 2027; member states may exempt companies falling out of scope for 2025–2026; transposition deadline for CSRD changes 19 March 2027. Estimates suggest roughly 80–90% of previously in-scope companies drop out. [WIDELY REPORTED: https://www.lw.com/en/insights/eu-sustainability-omnibus-published-in-the-official-journal] **TIME-SENSITIVE**
- The earlier "stop-the-clock" directive (April 2025) postponed wave 2 and 3 reporting by two years. [ASSUMPTION/JUDGEMENT — from general knowledge]
- The ESRS are being simplified by EFRAG at the Commission's request. [ASSUMPTION/JUDGEMENT — status not re-verified]
- Systems view: sustainability data (energy, emissions, workforce) increasingly flows through the same close-and-control machinery as financial data, with limited assurance where required. [ASSUMPTION/JUDGEMENT]

---

## 5. Record retention, audit trail, GDPR and data residency

### 5.1 Statutory retention examples

| Jurisdiction | Requirement (illustrative) | Evidence |
| --- | --- | --- |
| Germany | Books, annual financial statements, inventories: 10 years. Accounting vouchers (*Buchungsbelege*, incl. invoices): **8 years** since 1 January 2025 under the Fourth Bureaucracy Relief Act (§ 257(4) HGB, § 147(3) AO, § 14b UStG); commercial letters 6 years; reportedly banks, insurers and investment firms keep 10 years. | [WIDELY REPORTED: https://www.haufe.de/steuern/gesetzgebung-politik/viertes-buerokratieentlastungsgesetz_168_613390.html] |
| US public companies | Auditors must retain audit documentation 7 years (SOX s.802 / SEC Rule 2-06 of Reg S-X); companies follow IRS rules (generally 3–7 years) and litigation holds. | [ASSUMPTION/JUDGEMENT — from general knowledge] |
| EU VAT | Invoices retained for a period set by each member state (VAT Directive Art. 247); typically 5–10 years. | [ASSUMPTION/JUDGEMENT] |
| Netherlands, France, UK | Typically 7 years (NL), 10 years accounting documents (FR Commercial Code), 6 years (UK Companies Act for public companies; 3 for private). | [ASSUMPTION/JUDGEMENT — verify each before quoting] |

Retention runs from the end of the year in which the record was created (Germany) or the end of the fiscal year — not from the transaction date. Pillar Two, transfer pricing and tax audits can extend practical retention. [ASSUMPTION/JUDGEMENT]

### 5.2 GDPR right to erasure vs statutory retention

GDPR Article 17(3) disapplies the right to erasure to the extent processing is necessary **"(b) for compliance with a legal obligation which requires processing by Union or Member State law"** and **"(e) for the establishment, exercise or defence of legal claims."** [VERIFIED: https://gdpr-info.eu/art-17-gdpr/]

Practical resolution pattern:

1. The legal retention obligation prevails **for the data the law requires** (the invoice, the booking, the ledger entry), for the **statutory period only** (storage limitation, Art. 5(1)(e)).
2. Personal data **not required** for the statutory record (marketing preferences, browsing history, free-text notes) must be erased or anonymised on request.
3. Data under retention-only basis should be **restricted** (Art. 18-style): access-controlled, removed from operational use, then deleted at expiry.
4. Ledgers should hold **minimal personal data**: reference a customer ID, keep identity in a separate store with its own lifecycle; consider pseudonymisation so that erasure of the identity map does not break the immutable ledger.
5. Crypto-shredding (per-subject encryption keys) is a technique, but its acceptance as "erasure" is a legal judgement for the controller, not a settled rule.

[ASSUMPTION/JUDGEMENT — items 1–5 are the analyst's synthesis of GDPR principles; Art. 17(3) verified]

### 5.3 Data residency

GDPR does not require EU data residency; it restricts **transfers** to third countries without adequacy or appropriate safeguards (Chapter V: adequacy decisions, standard contractual clauses, BCRs; the EU–US Data Privacy Framework adequacy decision of July 2023 for certified US organisations). [ASSUMPTION/JUDGEMENT — from general knowledge; DPF validity is subject to litigation, **TIME-SENSITIVE**] Separately, some tax and accounting laws require books to be kept, or be accessible, in-country (or require notification/approval for keeping electronic books abroad — e.g. Germany § 146(2a) AO permits storing electronic books in another EU state, and elsewhere with approval). Sector regulators (banking outsourcing guidelines, DORA) add location and access-right requirements. [ASSUMPTION/JUDGEMENT — verify country-specific provisions]

---

## 6. Common misconceptions

1. **"A balanced trial balance means the books are right."** It only proves debits equal credits. [ASSUMPTION/JUDGEMENT]
2. **"Billing equals revenue."** Invoices are legal/tax documents; revenue follows performance obligations. Upfront billing creates a contract liability, not revenue. [ASSUMPTION/JUDGEMENT]
3. **"If we collect the cash, we are the principal and book gross."** Control of the good/service before transfer decides gross vs net; merchant-model platforms are often agents. [ASSUMPTION/JUDGEMENT]
4. **"VAT deemed-supplier status means we book gross revenue."** Tax treatment and IFRS 15/ASC 606 presentation are separate assessments. [ASSUMPTION/JUDGEMENT]
5. **"Customer funds held are deferred revenue."** Amounts collected on behalf of third parties are payables (and possibly safeguarded funds), not contract liabilities of the agent. [ASSUMPTION/JUDGEMENT]
6. **"Moving to a SaaS ERP moves SOX responsibility to the vendor."** Management remains responsible; the vendor's SOC 1 Type II plus your CUECs plus your own configuration controls form the evidence. [ASSUMPTION/JUDGEMENT]
7. **"A SOC 2 report covers our financial controls."** SOC 1 addresses ICFR; SOC 2 addresses trust services criteria. [ASSUMPTION/JUDGEMENT]
8. **"Functional currency is whatever we choose."** It is determined by economic facts; presentation currency is the choice. [VERIFIED: https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/]
9. **"Revaluation and translation are the same."** Revaluation of monetary items hits P&L; translation of foreign operations goes to OCI (CTA). [ASSUMPTION/JUDGEMENT]
10. **"UK Provision 29 is UK SOX."** No external attestation, wider scope (material controls of all types), comply-or-explain. [VERIFIED date: https://www.frc.org.uk/library/standards-codes-policy/corporate-governance/uk-corporate-governance-code/; characterisation ASSUMPTION/JUDGEMENT]
11. **"Pillar Two no longer matters for US groups."** The Side-by-Side system relieves US-parented groups from IIR/UTPR from 2026, but QDMTTs and the GIR obligations (and 2024–2025 obligations) remain. [WIDELY REPORTED: https://bdo.com/insights/tax/oecd-releases-guidance-on-side-by-side-system]
12. **"ViDA mandates EU-wide domestic e-invoicing in 2030."** The 2030 mandate is for intra-EU B2B; domestic mandates remain national choices (now without derogation). [VERIFIED: https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en]
13. **"GDPR erasure overrides financial retention"** — or the reverse, "retention lets us keep everything." Both are wrong; retention covers only the data the law requires, for the period required. [VERIFIED Art.17(3): https://gdpr-info.eu/art-17-gdpr/; rest ASSUMPTION/JUDGEMENT]
14. **"GDPR requires EU data residency."** It regulates transfers, not location per se. [ASSUMPTION/JUDGEMENT]
15. **"The EU AI Act's high-risk rules applied from August 2026."** Postponed by Regulation (EU) 2026/1744 to December 2027 / August 2028. [WIDELY REPORTED: https://abreuadvogados.com/en/conhecimento/publications/digital-omnibus-regulation-on-ai-the-key-amendments-to-the-ai-act/]
16. **"Automated controls never need retesting."** Reliance depends on effective ITGCs (especially change management) across the period. [ASSUMPTION/JUDGEMENT]

---

## 7. Points chapter writers must be careful about

1. **Dates are moving targets.** Re-verify before manuscript lock: Pillar Two filing deadlines and Side-by-Side transposition; France, Poland, Spain, Belgium e-invoicing phases; PSD3/PSR OJ publication; SEC semiannual reporting proposal; IFRS 18 EU endorsement; UK CASS 15 details; CSRD transposition; DST landscape.
2. **Do not name companies' accounting conclusions** (gross vs net, timing) without citing their own filings; facts differ by product line and change over time.
3. **Avoid asserting one revenue timing for agents** (booking vs stay vs completion). It depends on the contract and on what the agent promised.
4. **Distinguish US GAAP from IFRS** wherever details diverge (lease classification, collectability, sales-tax presentation, certain disclosure rules). Use "IFRS 15 / ASC 606 are substantially converged", not "identical".
5. **Use precise control vocabulary**: material weakness vs significant deficiency; ICFR vs disclosure controls; ITGC vs application control; SOC 1 vs SOC 2; Type I vs Type II; CUEC vs CSOC.
6. **Do not call Provision 29 "UK SOX"**, and do not imply an EU-wide SOX regime exists.
7. **Keep tax, accounting and regulatory treatments separate** in examples: the same transaction can be "agent" for revenue, "deemed supplier" for VAT, "marketplace facilitator" for US sales tax, and "reporting platform" under DAC7.
8. **Safeguarding citations**: cite EMD2 / PSD2 Art. 10 and national rules; do not invent an "EBA safeguarding guideline" number. UK rules (CASS 15) are FCA rules, not EU.
9. **Retention periods vary by country, record type, and sector**, and the clock usually starts at year-end. Germany's 8-year voucher rule (2025) is a good, current example — but note the financial-sector exception.
10. **Rounding and FX**: show worked examples with explicit rates and rounding policy; do not imply that average rates are always acceptable.
11. **"Immutable ledger" is a control concept, not a blockchain requirement.** Append-only with reversal entries satisfies auditors; do not imply a technology mandate.
12. **AI in finance**: most finance-function AI is not "high-risk" under the AI Act, but is still subject to ICFR (model change management, IPE, review controls). Credit scoring of natural persons is high-risk.
13. **Source hierarchy**: prefer standard-setter and regulator texts; mark Big-4 and law-firm summaries as such; vendor blogs (e-invoicing vendors especially) are useful for dates but should be cross-checked.
14. **This brief's tags**: material tagged ASSUMPTION/JUDGEMENT on foundational accounting is textbook-level but was not re-fetched; quote standard paragraphs only after checking the authoritative text.

---

## 8. Sources (URLs with one-line descriptions)

Standard-setters and regulators
- https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/ — IFRS Foundation summary of IFRS 15 and the five-step model.
- https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/ — IFRS Foundation summary of IAS 21 (functional/presentation currency; Lack of Exchangeability amendment).
- https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/ — IFRS Foundation page for IFRS 16 Leases.
- https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201 — PCAOB AS 2201 text (blocked to the research tool; cited from general knowledge).
- https://www.sec.gov/rules/interp/2007/33-8810.pdf — SEC interpretive guidance for management's ICFR evaluation (2007).
- https://www.sec.gov/structureddata — SEC structured data / Inline XBRL program.
- https://www.esma.europa.eu/issuer-disclosure/electronic-reporting — ESMA ESEF electronic reporting page.
- https://www.frc.org.uk/library/standards-codes-policy/corporate-governance/uk-corporate-governance-code/ — FRC page confirming 2024 Code dates and Provision 29 effective 1 Jan 2026.
- https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en — European Commission ViDA page with adoption and application dates.
- https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en — EIOPA DORA page (application 17 Jan 2025, pillars, scope).
- https://www.revenue.ie/en/companies-and-charities/pillar-two/dates/index.aspx — Irish Revenue Pillar Two key dates (Side-by-Side, EU notice, 30 June 2026 deadlines, OECD common approach).
- https://www.canada.ca/en/department-finance/news/2025/06/canada-rescinds-digital-services-tax-to-advance-broader-trade-negotiations-with-the-united-states.html — Canada Department of Finance DST rescission (29 June 2025).
- https://gdpr-info.eu/art-17-gdpr/ — Text of GDPR Article 17 (right to erasure and exceptions).
- https://www.supremecourt.gov/opinions/17pdf/17-494_j4el.pdf — South Dakota v. Wayfair opinion (2018).
- https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-1 — AICPA SOC 1 overview.

Big-4, law firms and technical publishers
- https://www.iasplus.com/en/publications/us/heads-up/2013/coso — Deloitte Heads Up on COSO 2013 (components, principles, transition).
- https://assets.kpmg.com/content/dam/kpmgsites/ie/pdf/insights/consulting/ie-uk-corporate-governance-code-provision-29.pdf — KPMG explainer on Provision 29 (material controls, no audit sign-off).
- https://ey.com/content/dam/ey-unified-site/ey-com/en-uk/services/assurance/documents/ey-2024-uk-corporate-governance-code-addressing-the-new-risk-management-and-internal-control-requirements-including-provision-29.pdf — EY guide to Provision 29 readiness.
- https://www.ey.com/content/dam/ey-unified-site/ey-com/en-za/services/ifrs/documents/ey-ifrs18-brochure.pdf — EY IFRS 18 brochure (effective 2027, MPMs).
- https://dart.deloitte.com/USDART/home/news/all-news/2025/jan/fasb-effective-date-asu-disaggregation-income-statement — Deloitte DART on ASU 2025-01 clarifying ASU 2024-03 effective dates.
- https://globaltaxnews.ey.com/news/2026-0244 — EY Global Tax News on Pillar Two filings due 30 June 2026.
- https://kpmg.com/lu/en/home/insights/2026/01/luxembourg-launches-pillar-two-registration-filing-process-oecd-reaches-agreement-side-by-side-package.html — KPMG Luxembourg on Side-by-Side agreement and filing.
- https://bdo.com/insights/tax/oecd-releases-guidance-on-side-by-side-system — BDO on Side-by-Side system content.
- https://www.deloitte.com/ie/en/services/tax/perspectives/oecd-side-by-side.html — Deloitte Ireland on the Side-by-Side package and safe harbours.
- https://oecdpillars.com/lithuania-updates-draft-globe-legislation/ — Pillar Two developments tracker (country deadline extensions; secondary).
- https://www.pwc.lu/en/newsletter/2025/vat-in-the-digital-age-vida.html — PwC Luxembourg ViDA overview (deemed supplier mechanics).
- https://cms.law/en/fra/news-information/electronic-invoicing-what-does-the-reform-entail — CMS France on the French e-invoicing reform phases.
- https://www.avalara.com/us/en/blog/germany-e-invoicing.html — Avalara on German e-invoicing phases (vendor source).
- https://www.ey.com/en_gl/technical/tax-alerts/poland-signs-into-law-mandatory-national-e-invoicing-system — EY on Poland's KSeF law.
- https://lookuptax.com/tax-changes/poland/ksef-penalty-deferral-2027-announced — Report of proposed KSeF penalty deferral to end-2027 (secondary).
- https://www.vertexinc.com/resources/resource-library/belgiums-2026-e-invoicing-regulations-explained-scope-deadlines-and-penalties — Vertex on Belgium's 2026 Peppol mandate (vendor source).
- https://www.vatcalc.com/spain/spain-verifactu-delay-till-jan-2027-for-certified-e-invoicing/ — vatcalc on Verifactu postponement to 2027.
- https://kpmg.com/us/en/taxnewsflash/news/2026/03/spain-e-invoicing-mandate-b2b.html — KPMG on Spain's B2B e-invoicing royal decree.
- https://news.pwc.be/deadline-for-first-dac7-reporting-now-imminent — PwC Belgium on DAC7 first reporting deadline.
- https://www.avalara.com/us/en/blog/how-marketplace-facilitator-sales-tax-laws-in-different-states-affect-marketplace-sellers.html — Avalara on marketplace facilitator laws post-Wayfair.
- https://www.williamfry.com/knowledge/psd3-psr-final-compromise-texts-are-published/ — William Fry on PSD3/PSR final compromise texts (April 2026).
- https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2026/04/impact-of-psd3-are-you-ready.pdf — Clifford Chance on PSD3/PSR content and expected application timing.
- https://www.swgroup.com/insights-events/insights/cass-15-safeguarding-for-payments-and-e-money-firms/ — Consultancy note on UK CASS 15 safeguarding (from 7 May 2026).
- https://abreuadvogados.com/en/conhecimento/publications/digital-omnibus-regulation-on-ai-the-key-amendments-to-the-ai-act/ — Abreu Advogados on Regulation (EU) 2026/1744 (AI Omnibus) dates.
- https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ — Gibson Dunn on the AI Omnibus agreement and postponed high-risk deadlines.
- https://www.lw.com/en/insights/eu-sustainability-omnibus-published-in-the-official-journal — Latham & Watkins on Omnibus I (CSRD/CSDDD) OJ publication and thresholds.
- https://www.dlapiper.com/insights/publications/2026/05/sec-proposes-optional-semiannual-reporting-for-public-companies — DLA Piper on the SEC semiannual reporting proposal (May 2026).
- https://www.haufe.de/steuern/gesetzgebung-politik/viertes-buerokratieentlastungsgesetz_168_613390.html — Haufe on Germany's BEG IV shortened retention for accounting vouchers.
