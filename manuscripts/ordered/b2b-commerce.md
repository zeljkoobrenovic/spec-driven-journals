{id: b2b-commerce}
# 21. Selling to Businesses: Accounts, Contract Prices, Quotes and Approvals

![Selling to Businesses: Accounts, Contract Prices, Quotes and Approvals — logo](commerce-platform-architecture/posts/21-b2b-commerce/assets/images/21-b2b-commerce/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn what is different when the buyer is a company, the records every business-to-business (B2B) platform needs, who should own accounts, prices and credit, and the choices for building a wholesale channel.

> **KEY POINTS:**
>
> * **The customer stops being flat.** A business buyer is a company with locations, several people and roles, an assortment, a price agreement, payment terms and a credit limit. Shopify, commercetools, SAP, Adobe and BigCommerce all model it that way, under different names, and the model must have one owner.
> * **A B2B price is a promise with a validity date.** List, tiered, contract and quoted prices coexist and must say which wins; a quote freezes a price, and the invoice must match what the portal showed, or the wholesale team keys orders in by hand to make it so.
> * **Credit and terms are finance facts.** Payment terms and credit limits usually belong to the ERP (enterprise resource planning system, the back office for finance, purchasing and invoicing), which is why a portal that cannot read them at checkout cannot replace e-mail and phone; the order record, not the ERP's order entry, is where a wholesale order should live.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-commerce-platforms-go-wrong):**
>
> * **The Price Nobody Can Explain** — the portal shows one wholesale price, the ERP invoices another, and the negotiated pre-season discount lives in an e-mail.
> * **Schrödinger's Order** — portal orders live in the platform, keyed orders in the ERP, EDI (electronic data interchange) orders in the EDI provider's mailbox; one customer, three order lists.
> * **The Spaghetti Junction** — each large buyer asks for its own way in (a portal login, a punchout session, an EDI mailbox, a spreadsheet by e-mail), each with its own connector.

A consumer buys a jacket and pays before dispatch. An outdoor shop may order sixty jackets at a negotiated price, request delivery to two locations and pay thirty days after invoicing. The buyer, approver and bookkeeper may be different people. **Business-to-business (B2B) commerce** must represent that agreement, or checkout can accept an order the seller cannot fulfill on the promised terms.

The agreement includes an account price, quantity breaks, **payment terms** specifying when the invoice is due, and a **credit limit** on what the customer may owe. Orders may require approval or delivery in agreed size combinations before a season starts. Checkout must check those conditions before making a commitment.

Those checks depend on knowing **who owns the company account, contacts, prices, terms, credit and orders**. If checkout reads an old credit balance or a different price list, having the right features will not protect the agreement. Evaluate how the systems obtain and enforce the same answers.

**Where we are in the order's journey.** Kestrel & Pine, the fictional outdoor brand, sells to consumers such as Eva and to wholesale customers. This chapter follows independent shops ordering through its portal or by email. Retail chain Bergzicht Outdoor sends structured orders through **electronic data interchange (EDI)**; [Documents Between Companies: EDI, Punchout and E-Invoicing](#edi-and-e-invoicing) and [Journey 3: A Chain Reorders by EDI, From Order to Invoice](#journey-wholesale-order) follow that route.

{id: b2b-commerce--setting-the-scene-at-kestrel-pine-the-38}
## Setting the Scene at Kestrel & Pine: The 38%

Wholesale lead Lea Moreau manages **1,100 active accounts**: 640 in the Netherlands, 210 in Belgium and 250 in Germany. Most are independent outdoor shops; Bergzicht is the one retail chain using EDI. Wholesale produced **€12.0 million** in 2026 through **9,400 orders**, averaging **€1,277**, on 30-day terms.

Since 2023, shops have used the platform's **B2B portal**, with company accounts, price lists and payment terms in the same platform account as the consumer storefronts. It receives **62% of wholesale orders**.

The remaining **38% arrive by email or phone** and are keyed into the **enterprise resource planning system (ERP)**. That is where Finance Director Sanne de Wit's team manages terms, credit limits and invoices. The portal needs those facts to handle more of the work.

When Noor Visser asks Lea in February 2027 why the 38% has not fallen since 2024, the answer is not that shops dislike the portal. It is that the portal cannot express what those shops have agreed *(illustrative)*:

- The portal shows one **wholesale price list per country**. The accounts that order by e-mail are mostly the larger ones, whose **pre-season terms** (an extra discount on orders placed before the season, agreed per account) live in the ERP's customer price lists and in Lea's e-mail, not in the platform.
- The portal cannot see **credit**. A shop near its limit can place a portal order that finance then holds, by hand, a day later; the team keys larger orders into the ERP because the ERP checks the limit at entry.
- A portal order and a keyed order are **two different records**: one in the platform, one only in the ERP. To see one shop's orders, Lea opens both.

That is the chapter's problem in one company. The portal is good at what the platform owns (the catalog, the cart, the checkout) and weak at what the ERP owns (terms, credit, negotiated prices, invoices), and neither holds the order record for the whole channel. Waypoint's answer, W2, is that every wholesale order, portal, keyed or EDI, is created in the OMS (order management system, the one record of every channel's orders) from Q4 2027, and the ERP keeps finance.

![Before: portal orders in the platform and keyed orders in the ERP. After: every wholesale order created once in the OMS.](commerce-platform-architecture/posts/21-b2b-commerce/assets/images/21-b2b-commerce/21-two-doors-one-record.jpeg)

**Figure 1:** *Today 62% of Kestrel & Pine's wholesale orders arrive through the portal and 38% are keyed into the ERP, so one shop's orders live in two records; under W2 every wholesale order is created once in the OMS.*

{id: b2b-commerce--what-is-different-when-the-buyer-is-a-company}
## What Is Different When the Buyer Is a Company

The contrasts below are industry practice; the vocabulary is defined as it appears.

| | Consumer (B2C) | Business (B2B) |
| --- | --- | --- |
| **Who buys** | One person, one account | A **company account**: an organization with several locations, several users and roles (who may order, who may approve, who may see invoices) |
| **Price** | One list price, promotions on top | **Contract pricing** (a price agreed with one customer or group), **tiered pricing** (price breaks by quantity), customer-specific assortments; prices quoted **excluding VAT** |
| **How the price is agreed** | Fixed | Often negotiated; a **quote** (the seller's offer at a stated price with a validity date) that the buyer accepts into an order |
| **Payment** | At checkout, before shipment | On **payment terms** (net 30: due 30 days after the invoice) within a **credit limit**; sometimes card or direct debit |
| **Order size and units** | One or two items | Dozens to hundreds of units in cartons, inner packs and size runs; sometimes pallets |
| **When orders are placed** | Any time | In apparel, a **pre-season order** months ahead for delivery in a window, then **in-season reorders** of what sells |
| **Who may commit** | The buyer | The buyer, subject to the buyer's own **approval workflow** (a manager must approve above a limit) |
| **Document that matters** | The order confirmation | The **invoice**, matched by the buyer against its purchase order and the delivery |

Each row introduces a fact that has to live somewhere and be readable by the checkout at the moment of the promise. Three of them, **the company account, the price and the credit limit**, are the ones the ERP and the platform fight over.

{id: b2b-commerce--the-vocabulary-the-platforms-share}
### The vocabulary the platforms share

Whatever the vendor, the documented object models converge on the same shapes. The table is my synthesis of the vendors' documentation as of November 2026; a blank cell means "not verified", not "absent".

| Concept | Shopify | commercetools | SAP Commerce (Spartacus docs) | Adobe Commerce B2B | BigCommerce B2B Edition | OroCommerce |
| --- | --- | --- | --- | --- | --- | --- |
| **The buying organization** | Company, CompanyLocation, CompanyContact | Business Unit (Company and Divisions, up to five levels) with Associates | B2BUnit tree with B2BUser | Company account, company hierarchies | Company account with users | Customer, customer group, customer user |
| **Who may do what** | Contact permissions (ordering only, location admin) | Associate Roles | Roles including approver and administrator; purchase limits | Company roles; administrators bypass rules | Roles controlling Buyer Portal access | Customer user roles |
| **Customer-specific prices and assortment** | Catalogs (price lists plus product sets) assigned to company locations | Stores and prices per Business Unit | Cost centers, budgets | Shared catalogs with custom pricing | Price lists per company | Price lists with scheduled adjustments |
| **Negotiation** | Draft orders for review and approval | Quote Request, Staged Quote, Quote | Quotes | Quotes | Sales quotes | RFQ (request for quote) to Quote, with approval workflow |
| **Spending control** | — (apps) | Approval Rules and Approval Flows | Order approval, budgets, purchase limits | Purchase orders with approval rules | — | Quote approval workflows |
| **Pay later** | Payment terms per company location (net, fixed date, on receipt, on fulfillment) | — (payment integrations) | — | Payment on Account | Net terms and available credit | — |

Shopify's developer documentation defines a Company as "Information about the business entity that makes a B2B purchase", a CompanyLocation as "A single location or branch of the company" to which catalogs, tax exemptions and payment terms are assigned, and a CompanyContact as "A person that acts on behalf of the company" (shopify.dev, accessed November 2026). commercetools says "Business Units are representations of Companies or Divisions", nesting up to five levels, with Associates whose roles "grant Associates different permissions" (commercetools documentation, accessed November 2026). The structure is the same: **organization, places, people, permissions**, with prices and terms attached to the organization or the place, not to the person.

![Diagram: The B2B object model every platform shares](commerce-platform-architecture/posts/21-b2b-commerce/assets/images/21-b2b-commerce/fig01-b2b-object-model-every-platform-shares.jpeg)

**Figure 2:** *The B2B object model every platform shares: an organization with locations and people, with prices and terms attached to the organization, and an order that draws on all of them at checkout.*

{id: b2b-commerce--who-owns-what}
## Who Owns What

The company account is the first place the customer record stops being flat, and the first place two systems claim it. The commerce platform needs the company, its contacts and its catalog to run the portal. The ERP needs the customer, its terms and its credit to invoice and to manage receivables. Both can hold all of it; neither should.

Microsoft's documentation for its Business Central to Shopify connector states the problem and the usual answer without hedging: merchants must "decide which system is the system of record for customer data. Most businesses manage customer records, payment terms, and credit limits in Business Central and export them to Shopify … Mixing both directions without a clear ownership rule can lead to conflicting records" (Microsoft Learn, 14 October 2026). The connector imports company locations with payment terms and tax IDs and can create a B2B catalog per exported company so that portal prices follow the ERP customer's price group. Shopify's own 2026 guidance on ERP integration says the same in general: "Document every field that moves between systems, and name the system of record for each" (Shopify enterprise blog, updated 28 August 2026).

My ownership table for a merchant with an ERP, a commerce platform with B2B features and, at the Omnichannel stage, an OMS:

| Fact | System of record | Readers | Why there |
| --- | --- | --- | --- |
| Company identity, legal name, VAT number, locations | The ERP (or a master-data system at Group stage) | Platform, OMS, invoicing, EDI | The ERP must know the customer before it can invoice; the VAT number drives tax treatment |
| Contacts, logins, roles, permissions | The platform (or an identity service) | Portal, service tools | Logins and sessions are the platform's job |
| List and tiered wholesale prices | The pricing source: ERP price lists or a pricing engine ([What Does It Cost? Price Lists, Contract Prices, Currencies and Tax](#pricing-architecture)) | Platform, OMS, EDI | One source, published to channels; the platform's catalogs are a copy with an effective date |
| Contract and pre-season agreements | The same pricing source, as customer-specific price lists | Platform, OMS | If they live only in e-mail and the ERP's order entry, the portal cannot show them, and the 38% stays |
| Quotes | The platform or OMS, as an explicit object with a validity date | Portal, sales reps, OMS | A quote is a frozen price; the order is created from it |
| Payment terms, credit limit, open balance | The ERP (receivables) | Platform or OMS at checkout, by a credit check | Finance facts; the ERP knows what is owed |
| The customer's own approval rules | The platform or OMS | Portal | The buyer's internal control; invisible to the ERP |
| Orders (portal, keyed, EDI, punchout) | The OMS at stage 3 and beyond; the platform at stages 1 and 2; never only the ERP's order entry | ERP (for posting), WMS (warehouse management system), service | One order record with one state model ([The Order Record: Lifecycle, State and the Order Management System](#order-management)) |
| Invoices, credit notes | The ERP | Peppol (the European e-invoice network) or EDI gateway, portal (for display) | Numbering, archive and legal weight live here ([Tax, Invoices and the Books: From Order to Ledger](#tax-invoicing-and-ledger)) |

The pattern is that **the ERP owns the money facts and the platform owns the session facts**, with prices sourced once and published. For wholesale and contract prices that source is the ERP: it publishes them as price events with effective dates to the OMS and the platform's B2B catalogs, and feeds no channel directly, so no storefront reads the ERP live. It is the split SAP describes for its own suite: master data replicated from the ERP to the commerce system, storefront orders sent to the ERP (SAP Learning, accessed November 2026). [The Back Office: ERP Integration and Who Is the Hub](#erp-and-back-office-integration) works out when the ERP should also be the live source at checkout and when it should not.

{id: b2b-commerce--what-the-flows-need}
### What the flows need

| Interaction | Freshness | Consistency | Latency at checkout | When it fails |
| --- | --- | --- | --- | --- |
| **Price lookup** for a company | Effective-dated; changes published hours ahead | The portal price must equal the invoice price for the same date and quantity | Precomputed per catalog; milliseconds | Recompute at invoicing and hope: The Price Nobody Can Explain |
| **Credit check** at order placement | Open balance as of today, including unposted shipments | One answer from the receivables system | Under a second if synchronous *(assumption)*; otherwise place the order and hold it | Nightly copy of the balance: an order accepted at 09:00 against yesterday's balance |
| **Order creation** | Immediate | One record, one number, idempotent on the buyer's purchase order number | Seconds | Keyed duplicates of e-mailed orders |
| **Invoice** on shipment | Same day as shipment | Generated from what shipped at the price the order carried | Batch | Invoice from the order rather than the shipment: short shipments invoiced in full |

The credit-check row decides whether the portal can replace e-mail. If the ERP's open balance is copied to the platform nightly, the portal is a day behind and finance keeps holding orders by hand. If the platform or OMS asks the ERP at order time, or receives balance changes as events, the portal can say "this order needs approval from Kestrel & Pine" at once. Stock for wholesale follows the same logic: it is promised from available-to-promise (stock not yet promised to another order) with a wholesale allocation, so that wholesale and consumer channels do not sell the same units ([Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability)).

{id: b2b-commerce--how-a-price-becomes-a-promise}
## How a Price Becomes a Promise

B2B pricing is layered, and every layer must say whether it beats or adds to the one below.

1. **List wholesale price**: the price in the seasonal wholesale price list, excluding VAT, per country or currency. Kestrel & Pine's Ridgewalker is €95, the Trailhead fleece €57, merino socks €8.50.
2. **Tiered or volume price**: breaks by quantity. Shopify's catalogs support "discounted price breaks when a customer buys a set quantity" and quantity rules per order (Shopify Help Center, accessed November 2026).
3. **Contract or customer-group price**: a price agreed with one account or group, usually a percentage off list or a fixed price per product, with an effective period. Shopify expresses it as catalogs assigned to company locations; Adobe as shared catalogs "with custom pricing for different companies" (Adobe B2B guide, 1 October 2026); OroCommerce as price lists with scheduled adjustments (OroCommerce documentation, version 7.0).
4. **Quote**: a one-off price for a specific request, with a validity date.

**The rule that matters is which layer wins.** Commonly the most specific wins (quote over contract over tier over list), and discounts do not stack unless the agreement says so. Write it down and implement it once in the pricing source, so the portal, the OMS and the invoice compute from the same rule; a portal that applies the rule its own way produces the invoice dispute.

![Four stacked price layers, list, tier, contract and quote, with the quote on top setting the price used by portal, order and invoice.](commerce-platform-architecture/posts/21-b2b-commerce/assets/images/21-b2b-commerce/21-price-layers-most-specific-wins.jpeg)

**Figure 3:** *B2B prices are layered: the most specific layer wins, and the portal, the order and the invoice must all compute the price from that one rule.*

**A quote freezes the price.** commercetools models negotiation as three objects, Quote Request, Staged Quote (with a `validTo` date) and Quote, and says "Quotes are legally binding custom offers presented to a Buyer" (commercetools documentation, accessed November 2026). Adobe's purchase-order flow states the consequence for the order built from one: "If the price of an item changes after the PO is created, the original price is used" (Adobe Commerce documentation, accessed November 2026).

On Shopify, no native "request a quote" page was found in November 2026; the documented mechanism is the **draft order** a merchant creates "for contacts to review and approve", into which third-party quote apps convert accepted quotes.

Under every name the decision is the same: the moment a seller states a price to a named buyer with a validity date, that price is stored as an object the order is created from, not recomputed later from whatever the price list then says.

**VAT follows the buyer.** B2B prices are shown and invoiced excluding VAT, and the treatment depends on who the buyer is and where: a Dutch shop is invoiced with Dutch VAT; a German or Belgian business customer with a valid VAT identification number is commonly invoiced without Dutch VAT under the EU rules for cross-border business supplies, and accounts for the tax itself. [Tax, Invoices and the Books: From Order to Ledger](#tax-invoicing-and-ledger) owns the rules; this chapter only insists that the VAT number is master data with an owner and a validation date, not a free-text field on the portal signup form.

{id: b2b-commerce--credit-terms-and-the-buyer-s-own-controls}
## Credit, Terms and the Buyer's Own Controls

**Payment terms** are typed, not free text. Shopify's Admin API (version 2026-10) models them as `NET` ("Payment is due a set number of days after the invoice is issued"), `FIXED` (a calendar date), `RECEIPT`, `FULFILLMENT` and `UNKNOWN`, with templates carrying the number of days. The due date is then computed from the invoice date, and the invoice date is the ERP's. This is why terms belong to the ERP and are *mirrored* to the platform: the platform needs them to show "net 30" and skip card payment at checkout; the ERP needs them to age receivables and chase payment.

**The credit limit** is the seller's control: the most a customer may owe. A credit check at order time compares the open balance (unpaid invoices, plus shipped orders not yet invoiced, plus accepted orders not yet shipped, depending on policy) with the limit, and accepts, holds for approval or rejects. BigCommerce's B2B Edition documents "available credit, and net terms" in payment settings (accessed November 2026); Microsoft's connector can carry credit limits to Shopify as metafields (custom fields), which is a mirror, not a check.

**The buyer's approval workflow** is the opposite control: the buyer's own rule that an order above an amount needs a manager. commercetools' Approval Rules are tiered ("Each tier contains one or more roles that are required to approve an Order before it can proceed to the next tier"), inherited down the Business Unit hierarchy, and "a single instance of rejection will lead to the rejection of the entire Approval Flow". SAP Commerce's organization model adds cost centers, budgets and purchase limits (Spartacus documentation, which describes an unmaintained storefront version); Adobe lets company administrators "bypass all approval rules". For a brand selling to independent shops, approval workflows are rarely needed; for one selling to a chain's 38 branches, or to corporate buyers, they are the difference between an order and a request.

![Diagram: A portal order at the Omnichannel stage](commerce-platform-architecture/posts/21-b2b-commerce/assets/images/21-b2b-commerce/fig02-portal-order-omnichannel-stage-prices-come.jpeg)

**Figure 4:** *A portal order at the Omnichannel stage: prices come from the pricing source, the credit decision from the ERP, and the order is created once in the order record, where the approval and the release are states, not e-mails.*

{id: b2b-commerce--the-choices}
## The Choices

A merchant that sells to businesses has four realistic ways to give them a channel, and the choice depends less on features than on who the buyers are and which system is fast enough to answer at checkout.

**1. The B2C platform's B2B features.** Shopify's B2B runs "in one store or use a separate B2B-only store", on the Basic, Grow, Advanced and Plus plans (Shopify Help Center, accessed November 2026; the expansion beyond Plus is recent and undated, and plans below Plus allow at most three active catalog assignments). Adobe Commerce ships company accounts, shared catalogs, quick order, purchase orders, quotes and requisition lists as a B2B module (Adobe guide, 1 October 2026); BigCommerce's B2B Edition serves its APIs from a separate domain, the trace of a partner-built origin.

This is Kestrel & Pine's choice: one tenant, one catalog, one checkout, with company accounts and price lists added. It fits a brand whose wholesale customers are many small shops buying the same products as consumers, and it limits when terms, credit and negotiated prices must come from the ERP in real time and the platform's model cannot express them.

**2. A dedicated B2B platform.** OroCommerce (open source, for "distributors, wholesalers, and manufacturers") models requests for quote, quotes with approval workflows, price lists with scheduled adjustments and order entry by matrix form (OroCommerce documentation, version 7.0); SAP Commerce carries budgets and cost centers from its procurement heritage. These fit a wholesaler or manufacturer whose whole business is B2B, with quotes as the normal path and buyers with their own controls; they are a second platform to run beside a consumer storefront, with a second catalog copy to govern.

**3. An ERP-driven web store.** Sana Commerce's pitch is "built on your SAP or Dynamics ERP", so that "your buyers order online with the prices you agreed and the stock you really have" (sana-commerce.com, accessed November 2026). The store is a window on the ERP: no price copy, no terms copy, no separate order list. It fits a B2B-first company with one ERP and modest traffic; it limits when consumer traffic arrives, when the ERP's response time becomes the storefront's, and when the business adds channels the ERP cannot model.

**4. The buyer's system as the channel.** Large buyers do not log into a supplier's portal. They send EDI orders ([Documents Between Companies: EDI, Punchout and E-Invoicing](#edi-and-e-invoicing)), or they **punch out**: their procurement system opens the supplier's catalog in a session, the buyer fills a cart, and the cart returns to the procurement system as a requisition that later comes back as a purchase order.

The cXML (commerce XML, a procurement message standard) User's Guide (version 1.2.037, dated 2018 and still the "current" link) describes it: "procurement applications display a button instead of product or pricing details … When users are done selecting items, they click a button that returns the order information to the procurement application." SAP's OCI (Open Catalog Interface) is the equivalent for SAP procurement.

A punchout cart returns the buyer's selections for approval; it does not yet authorize the supplier to ship. Wait for the subsequent cXML OrderRequest or EDI ORDERS and bring it into the same order record as a portal order. Building punchout is justified when a buyer requires that approval workflow; otherwise its buyer-specific integration adds work without replacing a missing capability.

| | B2C platform's B2B features | Dedicated B2B platform | ERP-driven web store | EDI and punchout |
| --- | --- | --- | --- | --- |
| **Fits** | Brands selling to many small resellers alongside consumers | B2B-first wholesalers and manufacturers with quotes and buyer controls | B2B-first companies with one ERP and modest traffic | A few large buyers who dictate the channel |
| **Where prices live** | Platform catalogs, mirrored from the pricing source | The platform's price lists; ERP mirrored | The ERP, read live | The buyer's contract; the supplier confirms |
| **Credit check** | Mirror of the limit; a live check needs integration | Built in or integrated | Live, in the ERP | In the ERP on order receipt |
| **Order record** | The platform (stages 1–2); the OMS (stage 3) | The B2B platform | The ERP | The OMS or ERP |
| **Limits** | Negotiated terms, approvals and credit beyond the platform's model; catalog caps on lower plans | A second platform and catalog copy; weak consumer features | ERP latency becomes storefront latency; no multichannel model | Per-buyer mapping cost; no self-service |
| **Kestrel & Pine** | Today, for 1,100 shops | Not needed | Not chosen: three consumer storefronts share the tenant | Bergzicht by EDI |

My recommendation for a brand like Kestrel & Pine is to stay with the platform's B2B features and fix the three gaps that keep the 38% alive: publish contract and pre-season price lists from the ERP into the platform's catalogs as price events with effective dates; add a credit check at order placement against the ERP's open balance (synchronous if the ERP answers in under a second, otherwise accept-and-hold with an event-driven release); and create every wholesale order, however it arrives, in the OMS. That assumes the ERP exposes prices and balances by API and the platform's catalogs can carry per-account lists; where either fails, the ERP-driven store is the better answer for the wholesale channel alone.

**Sales reps and B2B2C.** The rep's tooling is the seller-side portal: create an order or a draft on behalf of a shop (Shopify's draft orders; BigCommerce's "Masquerade" lets staff act as a buyer), see terms and open balance, convert a quote. A rep's order is the same order object as the shop's own, with a different creator; a rep tool that writes straight into the ERP is another unowned writer. **B2B2C** names a flow, not a product: either a brand feeds product content and stock to a retailer who sells to consumers (a data and document problem, [What Are We Selling? Products, Variants and the Catalog](#product-information)), or a business customer's own end users buy under the business's terms, as in a dealer portal, which is the model above with the company holding the prices and terms and its end users as contacts.

{id: b2b-commerce--across-scale-stages-when-it-fits-and-when-it-limits}
## Across Scale Stages: When It Fits and When It Limits

| Stage | What is typical | What becomes necessary | Warning signs of outgrowing it |
| --- | --- | --- | --- |
| **1 — Starting** | A few resellers served by e-mail and a spreadsheet price list; orders keyed into the shop or the accounting package; payment by invoice at the founder's discretion | Wholesale prices excluding VAT in one list; a written rule for which price wins; GTINs on every variant for the first chain | More than a few wholesale orders a week keyed by hand; a reseller's invoice disputed over a price |
| **2 — Growing** | The platform's B2B features or a simple portal: company accounts, one price list per country, net terms; the ERP or accounting system holds customers and invoices; a partner-built connector between them | One system of record for the company account (usually the ERP), mirrored to the portal; typed payment terms; a credit limit per account in the ERP, checked by hand | Negotiated accounts bypass the portal; the portal's and the ERP's prices drift; two order lists for one customer |
| **3 — Omnichannel** | Hundreds to thousands of accounts in several countries; contract and pre-season price lists; the first EDI buyer; wholesale competing with consumer and marketplace channels for the same stock | Prices published from one source with effective dates; a credit check at order placement; quotes as objects; wholesale orders in the OMS; wholesale allocation in the availability service; punchout for the buyers who require it | The share of keyed orders stops falling; credit holds by hand; a chain's chargeback for a document the ERP generated; the wholesale team cannot see a customer's orders in one place |
| **4 — Group** | Business units per brand or country; buyers with their own hierarchies and approval rules; key accounts on EDI and punchout; distributors and dealers as B2B2C | Business units with inherited rules; per-brand price lists under one pricing service; an ERP-fed credit check shared across brands; a master-data service for company identity and VAT numbers | Each brand runs its own portal and terms; the same retailer is three customers in three ERPs; approvals re-implemented per platform |

The judgement: the B2B channel outgrows the platform's features not when the account count grows but when **the facts the checkout needs stop living in the platform**: negotiated prices, credit, approvals. Kestrel & Pine's 38% is that signal in numeric form, and it has held steady since 2024 because the facts behind it never moved.

{id: b2b-commerce--in-practice}
## In Practice

**The platforms converge on one model, and none resolves ownership for you.** Shopify, commercetools, Adobe and BigCommerce (whose older B2B authentication token was deprecated on 30 September 2025) added B2B objects to consumer platforms; OroCommerce and SAP Commerce came from the B2B-first side with RFQs, budgets and cost centers. Every one of them can hold terms and credit, and the advice to pick one owner appears in the connector documentation (Microsoft's, above), not in the platforms'.

**The market is large by any definition, and the definitions differ.** Forrester's June 2022 release put US B2B e-commerce sales at $1.7 trillion in 2021, forecast to exceed $3 trillion by 2027, when it would be 24% of US B2B sales (a four-year-old forecast counting manufacturer and distributor sales to businesses). Digital Commerce 360 counted digital B2B sales "on ecommerce sites, password-protected sites, and apps", excluding EDI, at about $2.1 trillion in 2023 (7 February 2024), against total US manufacturing and wholesale sales of $15.12 trillion in 2025 (26 January 2026). No European figure meeting this book's sourcing standard was found. The point for an architect is the share that is *not* on a portal yet.

{id: b2b-commerce--kestrel-pine-de-kaap-buitensport-s-pre-season-order}
### Kestrel & Pine: De Kaap Buitensport's pre-season order

Let me work one order through the portal as it is in spring 2027 and as it should be after Waypoint. **De Kaap Buitensport** is a fictional independent outdoor retailer with two shops, in Groningen and Assen, one of Kestrel & Pine's larger Dutch accounts, on net 30 terms with a **credit limit of €15,000** and pre-season terms of **5% off list** on orders placed before 1 March *(illustrative)*. On **25 February 2027** its buyer wants 60 Ridgewalker jackets (a size run across women's and men's) and 120 pairs of merino socks for delivery in the first week of April.

| | What happens in February 2027 | What happens after Waypoint |
| --- | --- | --- |
| **Price** | The portal shows list: 60 × €95 = €5,700 and 120 × €8.50 = €1,020, total €6,720 excl. VAT. The 5% pre-season discount exists only in the ERP's customer price list and Lea's e-mail, so the buyer e-mails the order instead | The pre-season list is published from the ERP as a price event into the account's portal catalog, effective to 1 March; the portal shows €6,384 |
| **Credit** | The wholesale team keys the order into the ERP, which flags that open invoices of €9,800 plus this order exceed the €15,000 limit by €1,520 (at list) and holds it for Lea | The portal asks the ERP at placement; the order is created in the OMS as *awaiting seller approval*, and the buyer sees that status at once |
| **Approval** | Lea approves by e-mail on 27 February because a €4,100 invoice is due on 2 March; the team releases it in the ERP | Lea approves in the OMS; the release is an event; the ERP posts the order |
| **Order record** | The order exists in the ERP only; the portal history for De Kaap shows nothing for February | One order, one number family, visible to the shop, Lea, finance and the warehouse |
| **Stock** | The ERP reserves 60 jackets from a figure 15 minutes behind the WMS and an hour ahead of the platform | The availability service reserves against wholesale allocation; consumer channels see the reduced figure within minutes |
| **Invoice** | On shipment in April, from the ERP, at the price keyed in; if it differs from the e-mail, a credit note follows | From the ERP, from what shipped, at the price the order carried |

The after-Waypoint column assumes the ERP can answer a credit check in under a second at the portal's volume and that the platform's catalogs can carry per-account, effective-dated lists; both should be tested before the 38% is promised to fall.

{id: b2b-commerce--when-it-goes-wrong}
## When It Goes Wrong

| Failure | How it shows | Detection | Recovery |
| --- | --- | --- | --- |
| **Portal price differs from invoice** (the ERP recomputes at invoicing; a contract list expired) | Credit notes, disputes, shops asking for the "real" price | Compare order-line price with invoice-line price daily; alert on any difference | Invoice at the order's price; publish price lists with effective dates and recalculate only on explicit change |
| **Stale credit balance** (nightly copy) | Orders accepted that finance later holds, or rejected against an outdated balance | Age of the balance the portal used, logged per order | Credit check against the ERP at placement, or accept-and-hold with an event-driven release |
| **Duplicate orders** (the shop e-mails and then uses the portal; the rep keys an order the buyer already placed) | Double shipments, double invoices | Uniqueness on the buyer's purchase order number per company; a same-day duplicate check on lines | One order record for every entry path; a rep tool that creates the same order object |
| **Wrong unit of measure** (12 pieces ordered as 12 cartons) | A twelve-fold shipment and invoice | Order-line quantity against pack sizes and the account's history | Units as master data on the product; the portal confirms pack sizes |
| **Expired or invalid VAT number** | The wrong tax treatment on an invoice; a correction months later | Validate at account creation and periodically; store the validation date | The VAT number as master data with an owner |
| **Quote accepted after it expired, or at a changed price** | A dispute over which price was agreed | Quote state and `validTo` enforced when the order is created | Create orders only from valid quotes; expire the rest |

The first two rows are the Kestrel & Pine story. The others arrive with scale, and all are cheaper to prevent in the object model than to fix at month-end.

{id: b2b-commerce--what-to-take-away}
## What to Take Away

**Established.**

- Every major platform's B2B model has the same shape: an organization with locations, people and roles; customer-specific prices and assortments; quotes; approval rules; and payment terms, documented by Shopify, commercetools, SAP, Adobe, BigCommerce and OroCommerce as of 2026.
- A quote freezes a price. commercetools' "legally binding custom offers" with a validity date and Adobe's "the original price is used" are the same design decision, and the order must be created from the quote.
- Payment terms and credit limits are receivables facts; connector vendors' own documentation (Microsoft, 2026) says to manage them in the ERP and name one system of record for customer data.

**Depends on context.**

- The B2C platform's B2B features are the right channel for a brand selling to many small resellers, provided prices are published from one source and a credit check reaches the ERP at order time; once negotiated terms, approvals and credit live outside the platform's model, an ERP-driven store or a dedicated B2B platform fits better.
- A synchronous credit check is right when the ERP answers in under a second at the portal's volume; otherwise accept the order and hold it, with the hold released by an event, rather than copy the balance nightly.
- Punchout and EDI are worth building only for the buyers who require them; for everyone else they are cost without benefit, but the orders they produce must still enter the same order record.

**The author's synthesis.**

- The share of wholesale orders keyed in by hand is the best single measure of a B2B architecture, because it counts the facts the portal cannot see; Kestrel & Pine's 38% is a list of missing integrations (contract prices, credit, one order record), not a list of missing features.
- Decide ownership of the company account, the price and the credit limit before choosing or configuring any B2B platform; every platform can hold all three, and the one that does by default is the one nobody decided on.

{id: b2b-commerce--questions-to-ask}
## Questions to Ask

1. Which system is the system of record for the company account, and which fields are mirrored to the portal, in which direction?
2. Where do contract and pre-season prices live, and can the portal show them to the right account on the right dates?
3. Which price wins when a quote, a contract price, a volume break and a list price all apply, and is that rule implemented once?
4. Is the credit limit checked at order placement against today's balance, or against a copy, and how old is the copy?
5. What share of wholesale orders arrive outside the portal, and for each reason, which fact is the portal missing?
6. Are quotes objects with a validity date, and is an order created from the quote or recomputed from the price list?
7. Is the invoice generated from the shipment at the order's price, and how often do portal price and invoice price differ?
8. Do punchout and EDI orders enter the same order record as portal orders, with the buyer's purchase order number as a uniqueness key?

Portal orders are the wholesale channel's self-service path. The largest buyers do not use it: they send documents. The next chapter opens the EDI envelope, from the ORDERS message to the despatch advice whose pallet labels cost Kestrel & Pine €14,200, and the e-invoicing mandates that now reach every business customer in Belgium. Continue with [Documents Between Companies: EDI, Punchout and E-Invoicing](#edi-and-e-invoicing).

{id: b2b-commerce--sources-and-evidence}
## Sources and Evidence

*Company, product and investor sources*

- [Shopify B2B](https://help.shopify.com/en/manual/b2b) and [Catalogs in B2B](https://help.shopify.com/en/manual/b2b/catalogs), Shopify Help Center, n.d., accessed 2026-11 — plan availability, catalogs, volume pricing, the three-catalog cap below Plus.
- [B2B app development overview](https://shopify.dev/docs/apps/build/b2b), Shopify, n.d., accessed 2026-11 — Company, CompanyLocation and CompanyContact definitions; draft orders for review and approval.
- [PaymentTermsType](https://shopify.dev/docs/api/admin-graphql/latest/enums/PaymentTermsType) and [PaymentTermsTemplate](https://shopify.dev/docs/api/admin-graphql/latest/objects/PaymentTermsTemplate), Shopify Admin API 2026-10 — typed payment terms.
- [ERP Integration: Methods, Benefits, and Examples](https://www.shopify.com/enterprise/blog/erp-integration), Shopify, 2026 — "name the system of record for each" field.
- [Business Units](https://docs.commercetools.com/api/projects/business-units), [Quote Requests](https://docs.commercetools.com/api/projects/quote-requests), [Staged Quotes](https://docs.commercetools.com/api/projects/staged-quotes), [Quotes](https://docs.commercetools.com/api/projects/quotes), [Approval Rules](https://docs.commercetools.com/api/projects/approval-rules) and [Approval Flows](https://docs.commercetools.com/api/projects/approval-flows), commercetools, n.d., accessed 2026-11 — the B2B object model, quoting and approval.
- [B2B Commerce Organization](https://sap.github.io/spartacus-docs/b2b-commerce-organization/) and [B2B Order Approval](https://sap.github.io/spartacus-docs/b2b-order-approval), SAP Spartacus documentation, n.d., accessed 2026-11 — units, budgets, cost centers, purchase limits, approval (documents an unmaintained storefront version).
- [Implement an Integration of SAP S/4HANA Cloud with SAP Commerce Cloud](https://learning.sap.com/learning-journeys/implement-an-integration-of-sap-s-4hana-cloud-with-sap-commerce-cloud), SAP Learning, n.d., accessed 2026-11 — master data to commerce, orders to ERP.
- [B2B for Adobe Commerce guide overview](https://experienceleague.adobe.com/en/docs/commerce-admin/b2b/guide-overview), Adobe, 2026, and [Purchase order flow](https://experienceleague.adobe.com/en/docs/commerce-admin/b2b/purchase-orders/purchase-order-flow), Adobe, n.d., accessed 2026-11 — company accounts, shared catalogs, purchase orders, "the original price is used".
- [About B2B Edition APIs](https://docs.bigcommerce.com/b2b-edition/docs/about), BigCommerce, n.d., accessed 2026-11 — company hierarchies, net terms and available credit, the separate API domain, the 30 September 2025 token deprecation.
- [Sana Commerce](https://www.sana-commerce.com/), vendor page, n.d., accessed 2026-11 — the ERP-driven web store.
- [OroCommerce README](https://raw.githubusercontent.com/oroinc/orocommerce/master/README.md), Oro Inc., 2026, and [Back-office Sales documentation](https://doc.oroinc.com/user/back-office/sales/), version 7.0, accessed 2026-11 — RFQs, quotes, price lists, order entry.
- [Synchronize customers and companies](https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-customers), Microsoft Learn, 2026 — the system-of-record advice for customers, payment terms and credit limits.
- [Forrester: US B2B e-commerce will reach an estimated $3 trillion by 2027](http://www.forrester.com/press-newsroom/forrester-us-b2b-e-commerce-will-reach-an-estimated-3-trillion-by-2027/), Forrester, 2022 — market size and definition (evidence age).
- [B2B ecommerce market (US)](https://www.digitalcommerce360.com/article/b2b-ecommerce-market-us/), Digital Commerce 360, 2024, and [US B2B sales exceed $15 trillion in 2025](https://www.digitalcommerce360.com/2026/01/26/us-b2b-sales-exceed-15-trillion-2025/), Digital Commerce 360, 2026 — digital B2B sales and total sales, with their definitions.

*Standards, regulation and official documentation*

- [cXML User's Guide 1.2.037](https://xml.cxml.org/current/cXMLUsersGuide.pdf), cXML.org (SAP Ariba), 2018 — the punchout protocol and messages (evidence age; still the current link).

*Research and practitioner sources*

- [SAP SRM OCI PunchOut](https://tradecentric.com/blog/sap-srm-oci-punchout/), TradeCentric, 2026 — OCI's fields and limits compared with cXML (integrator source).

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
