---
title: "Whose Data Is It? Privacy, Consent and Retention"
date: 2026-11-07
author: Željko Obrenović
excerpt: "What personal data does a commerce platform hold, what may it do with it, and how do you build consent and retention in? Map every system that holds a person with its legal role, record consent with its evidence on the customer master, split the person from the transaction so invoices can stay while profiles go, and run a deletion request as a fan-out with a record of what each system did, because the law gives you one month and the data is in nine places."
permalink: privacy-and-customer-data
timetoread: 28 min read
icon: "assets/icons/35-privacy-and-customer-data.png"
logo: "assets/images/35-privacy-and-customer-data/logo.jpeg"
---

> **IN THIS CHAPTER, YOU WILL:** Learn where personal data lives in a commerce estate, which rules govern each use of it, and how to design consent, retention and deletion across many systems.

> **KEY POINTS:**
>
> * **Every integration is also a data flow with a legal role.** The merchant decides why and how customer data is used, so it is the controller; the platform, the warehouse system and most apps act on its instructions as processors; carriers, marketplaces and payment providers usually decide for themselves. The system-of-record map needs that column.
> * **The order and the marketing profile are two different things in law, even when they describe one person.** The order rests on the contract and on tax law and must be kept for years; the profile rests on consent and must go when the person says so. Design them to separate: pseudonymize the transaction (replace the name in it with a code), erase the person.
> * **A deletion request is a fan-out with a deadline.** One month, every system that holds the person, a different right answer in each, and a record of what was done. Without an identity index (a list of which systems hold each person) and an orchestrator (a workflow that sends the request to each system and records the answers) it is a seventeen-day hunt through nine systems; with them it is a job.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-commerce-platforms-go-wrong.html):**
>
> * **The Familiar Stranger** — a person the systems cannot recognize as one cannot be deleted, told the truth about, or respected when they opt out.
> * **The Secret Agent** — an app, script or export that copies customer data without a named owner or a contract is a processor nobody appointed.
> * **The Long Fuse** — a data subject request has a legal clock of one month, and a cookie or transfer rule can change with a court decision; both are discovered late by merchants with no map.

<br>
The previous chapter asked who may act on the shop and answered with a list of identities and keys, each with an owner. This chapter asks the mirror question about the data the shop holds on people: who may use it, for what and for how long. The question becomes concrete when a customer asks a merchant to remove their personal data. Their account is in the shop platform, but addresses, purchases and contacts have also reached warehouse, carrier, payment, marketing and support systems, and removing the storefront profile does not settle what happens to those copies. A forgotten export can retain a record, and an unchanged integration can recreate one after removal. So the architecture needs a map of data copies, purposes, access and retention rules, and a request must reach the systems that hold the data and produce a result the merchant can verify. This chapter offers an architect's reading of the rules; legal details and national requirements still matter.

The answer this chapter gives is that a shop holds one person in many systems for different purposes. The order and the invoice rest on the contract and on tax law, and are kept for years. The marketing profile rests on consent and goes when the person asks. Building consent and retention in, and answering requests, takes four moves: map, for each system, its legal role, the action a request requires there and how long it keeps records; keep consent with its evidence on the customer master; split the person from the transaction; and answer requests through an identity index and an orchestrator.

The chapter explains who decides the use of data (the **controller**), who processes it for that party (the **processor**), how consent is recorded, how long records are kept and how requests are handled. It starts from a deletion request that found one customer in nine of Kestrel & Pine's thirteen systems. It then gives the vocabulary and the data a merchant holds and the two roles, and follows the data to partners, other countries and software vendors, with the clock for reporting a breach. Next come the lawful bases and consent, including consent at a store's till; retention and the split of the person from the transaction; a request across many systems; and the requirements of the four privacy flows (capturing consent, withdrawing it, the retention purge and the request) side by side. The chapter compares the ways to run requests and the stage at which each fits, follows Kestrel & Pine's autumn 2027 design and ends with what goes wrong. The evidence is the scenario and dated primary sources: the GDPR and ePrivacy texts, the EDPB's guidelines, the Dutch and Belgian regulators, national retention rules and Shopify's developer documentation. [[identity-and-master-data]] connects customer identities; [[commerce-regulation]] provides the wider calendar.

**Where we are in the order's journey.** The same spread happens on every ordinary order. Eva buys a jacket from Kestrel & Pine, the fictional outdoor brand, on 13 April 2027. Fulfillment, payment and invoicing distribute her details to different systems. Notifications need an email address; newsletter enrollment needs its own legal basis. Her 19 April exchange adds the returns portal. Each copy needs a purpose and retention rule. The chapter's case is a different customer with a longer history: Lotte, in Ghent.

## Setting the Scene at Kestrel & Pine: The Request From Ghent

On **10 May 2027**, a Belgian customer, called Lotte Claes in this fictional example, asks Kestrel & Pine to delete her data and stop emailing her.

Lotte has two storefront orders, a marketplace order, a return, a newsletter subscription and an Antwerp store loyalty entry. Head of Engineering Noor Visser must identify the records behind those relationships and decide the action for each system. Deleting the storefront account alone will not complete the request.

Noor handed the search to Ruben Alves and the application support team, and finding every record took them seventeen working days. Lotte was in nine of the thirteen systems, and each needed a different action; several actions were out of Kestrel & Pine's reach, because bol (a Dutch and Belgian marketplace), bpost (the Belgian postal carrier) and the PSP keep their own records:

| System | What it held | What they did | What they could not do |
| --- | --- | --- | --- |
| The shop platform | Account, addresses, two orders, consent flag, the apps' copies | Deleted the account; the shop platform anonymized the orders and notified its apps | Confirm that every installed app complied |
| The marketplace connector | A copy of the bol order with name and address | Anonymized the copy | Touch bol's own record; bol is a separate controller |
| The ERP | Two consumer invoices and a credit note | Nothing: invoices are tax records | Erase; retention rules apply |
| The WMS | Three shipments with name and address | Deleted addresses from shipments older than a year | Erase recent shipments while a claim is possible |
| The shipping service | Labels and tracking for three parcels | Scheduled deletion for the end of the claims window | Reach bpost's own delivery record |
| The PSP | Payment records for two orders | Removed shopper details from the console view | Erase the PSP's own records |
| The POS | A loyalty entry with phone number and five purchases | Deleted the entry; receipts kept as fiscal records | Unlink receipts already exported to the ERP |
| The returns portal | A contact and one return | Deleted the contact; anonymized the return | Nothing further |
| The data warehouse | Rows keyed by e-mail in four tables and a BI extract | Replaced identifiers with a hash (a code computed from them that cannot be turned back into them) | Reach a spreadsheet export made in 2026 |

Two more copies sat outside the nine: the newsletter tool, one of the shop platform's apps, unsubscribed her through the shop platform's notification; the iPaaS (the integration platform) held her in three days of logs that expired on their own; nobody checked the backups. (Kestrel & Pine had no order management system yet; the OMS that appears later in this chapter took its first orders in September 2027.) The reply went out on **4 June 2027**, inside the one-month limit the GDPR (the EU's General Data Protection Regulation) sets for a reply, with six days to spare. It had taken three people and a shared spreadsheet. **The request was answered. The next one would arrive before anyone had written down how.**

![Thirteen filing drawers, nine open with the same person's card inside, and three workers with a spreadsheet and a calendar marked 17 working days.](assets/images/35-privacy-and-customer-data/35-lotte-in-nine-of-thirteen-systems.jpeg)
**Figure 1:** *One customer's deletion request found her in nine of the thirteen systems and took seventeen working days, three people and a shared spreadsheet to answer.*

## What Personal Data a Commerce Platform Holds, and Under Which Rules

The scene used words that carry the design: controller, the one-month limit, records that must be kept. **Personal data** is any information relating to an identified or identifiable person: a name, an e-mail, an order with an address, a cookie id tied to a browser. The **GDPR**, Regulation (EU) 2016/679, has applied across the European Union since 25 May 2018; it gives the person rights (access, rectification, erasure, objection, portability) and the organizations that handle the data duties.

A **controller** is the organization that decides why and how personal data is used; a **processor** handles data only on the controller's instructions (Article 4(7) and 4(8)). A **data processing agreement (DPA)** is the contract Article 28 requires between them. A **lawful basis** is the legal reason a controller may use the data at all; Article 6 lists six, of which four matter here: consent, performance of a contract, a legal obligation and the controller's legitimate interests. A **data subject request (DSR)** is a person exercising a right: send me my data, correct it, delete it. **Retention** is how long data is kept, and the law pulls two ways: no longer than the purpose needs, and at least as long as tax law demands.

What a merchant like Kestrel & Pine holds, by purpose:

| Data | Where it lives | Purpose | Usual lawful basis | How long it is needed |
| --- | --- | --- | --- | --- |
| Name, delivery and billing address | Platform, OMS (order management system), WMS, shipping service, ERP, carriers | Deliver and invoice | Contract; legal obligation for the invoice | Order: the fiscal period; shipment: the claims window |
| E-mail and phone | Platform, notification service, returns portal, POS, newsletter tool | Order messages; service; marketing | Contract for order messages; consent or the soft opt-in (both explained below) for marketing | Service: while the account exists; marketing: until withdrawn |
| Order history, returns, refunds | Platform, OMS, ERP, returns portal, PSP, data warehouse | Fulfill, account, support, warranty | Contract; legal obligation; legitimate interests for fraud | Fiscal period; then pseudonymized |
| Browsing and behavior | Analytics, advertising tags, CDP (customer data platform), personalization | Measurement; marketing | Consent (the ePrivacy Directive for the device; GDPR for the profile) | Until withdrawn or aggregated |

The right-hand columns are the design. The same person appears in every row, but each row has its own basis and its own clock. **The order record and the marketing profile need separate lawful bases, separate retention clocks and separate deletion behavior, even though they refer to the same person.**

Getting this wrong has a price. The fine ceiling for the core infringements is €20 million or 4% of worldwide annual turnover, whichever is higher (Article 83(5)). For Kestrel & Pine, with €48.0 million of 2026 revenue, 4% would be about €1.9 million, so its ceiling is the €20 million figure; commoner sanctions are orders to stop processing and the public finding.

## Controller, Processor and the Commerce Supply Chain

Who is the controller for Lotte's data? The merchant: Kestrel & Pine decides that orders are taken, delivered and invoiced, that a newsletter exists, that a warehouse system is used. The guidelines of the European Data Protection Board (EDPB) on the two roles (version 2.0, July 2021) draw the line: decisions on the purpose of processing "are clearly always for the controller to make"; the "essential means" (which data, for how long, who receives it, whose data) are the controller's; the "non-essential means" (the choice of hardware or software, the detailed security measures) may be left to the processor.

Applied to the commerce supply chain, the usual outcome of that test, as the author reads it and not as a rule:

| System | Role for the merchant's customer data | Why |
| --- | --- | --- |
| The hosted platform, the WMS, the OMS, the iPaaS, the returns portal, the data warehouse | Processor | Tools the merchant chose, used for the merchant's purposes under its instructions and a DPA |
| Most apps | Processor | Installed by the merchant to act on its data; each needs a DPA |
| The PSP | Processor for the merchant's order data; usually an independent controller for the payment itself | Payment providers have their own legal duties (anti-money-laundering, fraud) that they decide on |
| The carrier; the marketplace | Independent controllers | The carrier decides how it delivers and keeps its own records; the shopper is the marketplace's customer |
| Advertising platforms | Often joint or independent controllers | They use the data for their own purposes too |

Platforms encode this in their app rules. Shopify, one widely used hosted shop platform, requires every App Store app to subscribe to three compliance webhooks: `customers/data_request`, `customers/redact` (sent "10 days after the deletion request") and `shop/redact` (48 hours after a store owner uninstalls the app); apps must complete the action within 30 days and may decline redaction where the law requires them to retain data (developer documentation, n.d., accessed November 2026). Its protected-customer-data program gates name, address, phone and e-mail behind approval and requires minimum data, stated purposes, respect for consent, retention periods and encryption. That is a platform acting as the merchant's processor and policing the sub-processors (here, the apps that act on the merchant's data through it) on its behalf.

![Diagram: The merchant is the controller](assets/images/35-privacy-and-customer-data/fig01-merchant-controller-most-systems-are-processors.jpeg)
**Figure 2:** *The merchant is the controller; most of its systems are processors it must instruct and contract; carriers, payment providers and marketplaces decide for themselves.*

The consequence: **the system-of-record map from [[boundaries-and-systems-of-record]] needs a column for each system's legal role, and the integration inventory from [[integration-styles]] is also the inventory of data flows.** Of the 34 integrations in Kestrel & Pine's January 2027 integration inventory, 13 had no named owner: 13 data flows with nobody accountable for them, each a Secret Agent in the book's terms; five were still unowned in April 2027, after the ownership map.

## Sharing and Transfers

**Sharing with partners.** The roles reach beyond the merchant's own systems, because much of the data leaves them. Every order sends personal data to a carrier, the PSP, sometimes a marketplace, and to apps and connectors. The rules are minimization (the warehouse does not need the e-mail, the carrier does not need the order history), a recorded role per recipient, and a DPA or terms that cover the transfer. Kestrel & Pine's marketplace connector copied everything the marketplace sent; after Lotte's request it copies what the warehouse needs.

**International transfers.** Most commerce stacks send data to the United States somewhere: analytics, e-mail delivery, support tooling, hosting. The lawful routes are an adequacy decision (a Commission decision that a country outside the EU protects personal data well enough for data to flow there as within the EU), standard contractual clauses (SCCs: contract terms approved by the Commission that the sender and the receiver sign) or binding corporate rules (approved rules inside one corporate group). The EU-US Data Privacy Framework (DPF), Commission Implementing Decision (EU) 2023/1795 of 10 July 2023, is the adequacy decision for certified US companies; the modern SCCs are Decision (EU) 2021/914.

That route has been challenged in court. The EU's General Court (the court below the Court of Justice) dismissed Philippe Latombe's challenge to the DPF on 3 September 2025; an appeal (Case C-703/25 P) is pending as of November 2026; law firms advise keeping SCCs as a fallback.

The architectural asset is a **transfer inventory** keyed to the integration map: per vendor, where the data goes and under which mechanism, so that a court decision becomes a filter on a list rather than a discovery project. If the DPF appeal succeeds, a merchant with that list can see which vendors are affected in an afternoon.

**The vendor's side.** The software vendors on the map are recipients too. A commerce software vendor has a processor's obligations: a DPA the merchant can sign, sub-processors listed and announced, data kept in the regions it promises, the ability to export and erase one customer of one merchant, security it can evidence, and breach notification to the merchant without undue delay (Article 33(2)). The merchant needs that notice because, as controller, it must notify its supervisory authority (its national data protection regulator, such as the Dutch and Belgian regulators named in the consent section) of a personal data breach without undue delay and, where feasible, not later than 72 hours after becoming aware of it, unless the breach is unlikely to result in a risk to people's rights and freedoms (Article 33(1)). That clock runs in hours from the breach; it is separate from the one-month clock for a person's request, which comes later in the chapter.

## Lawful Bases: The Order Versus the Marketing

Knowing who holds and receives the data leaves the question of why each use is allowed at all. In commerce terms, the four bases divide the work like this:

| Use | Basis | In practice |
| --- | --- | --- |
| Taking, delivering, invoicing and supporting the order; warranty; returns | **Contract** | Needed to do what the customer asked; no consent needed; cannot be withdrawn while the contract runs |
| Keeping invoices, accounting records, VAT evidence | **Legal obligation** | Kept for the statutory period even if the customer objects |
| Fraud screening; security; basic analytics; defending claims | **Legitimate interests** | Allowed where the merchant's interest is not overridden by the person's; documented; can be objected to |
| Newsletters; profiling for personalized marketing; cross-site tracking | **Consent**, or for e-mail to existing customers about similar products, the ePrivacy **soft opt-in** | Freely given, specific, informed, recorded, and as easy to withdraw as to give |

The soft opt-in deserves a sentence because every merchant asks about it. The ePrivacy Directive (the EU law on electronic communications that covers e-mail marketing and cookies; Article 13(2), 2002 text consolidated in 2009) lets a business that obtained a customer's e-mail "in the context of the sale of a product or a service" use it "for direct marketing of its own similar products or services", provided the customer can object, free of charge, at collection and in every message. National transpositions differ; the lawyer confirms the local reading. The architectural point holds either way: **the order's e-mail address and the marketing permission are two facts, and the second must be recorded with its basis.**

## Consent, Cookies and Tracking

A consent choice must control what the shop and its connected tools actually do. Recording a preference in a banner is insufficient if tracking scripts ignore it or another system continues the marketing the customer declined.

Consent lives in two laws. The GDPR defines it (Article 4(11)) as a freely given, specific, informed and unambiguous indication of the person's wishes by a statement or a clear affirmative action, and requires the controller to be able to demonstrate it (Article 7(1)). The ePrivacy Directive (Article 5(3), as amended in 2009) adds a rule about the device: storing information on, or reading information from, a user's device is allowed only with consent after clear information, except for what is strictly necessary to transmit a communication or to provide a service the user explicitly asked for.

In plain words: the cart cookie and the language choice need no consent; the tags (scripts on the page that send visitors' events to analytics and advertising vendors), such as the analytics tag, the advertising pixel and the personalization script, do, before they fire. The regulators Kestrel & Pine answers to agree on the substance:

- The **EDPB's consent guidelines** (May 2020) forbid cookie walls (a banner that blocks the site until the visitor accepts) and say scrolling or swiping "will not under any circumstances" count as consent; its technical-scope guidelines (version 2.0, October 2024) bring tracking pixels, URL tracking and IP-only tracking within the device rule.
- The **Dutch regulator** (Autoriteit Persoonsgegevens, n.d., accessed November 2026) exempts functional cookies and "limited analytical cookies" with little privacy impact, requires consent for tracking cookies, and calls cookie walls prohibited.
- The **Belgian regulator** (Gegevensbeschermingsautoriteit, November 2023) exempts only strictly necessary functional and technical cookies (naming the language choice, cookie preferences and the shopping basket), rejects pre-ticked boxes and continued browsing, and requires cookies to be grouped by purpose, with own and third-party advertising as separate purposes.

A **consent management platform (CMP)** is the banner and the record behind it: it stores each visitor's choices per purpose and tells each tag whether it may run. **Server-side tagging**, in which the merchant's own server receives the browser's events and forwards them to vendors, changes who receives the data first, not whether consent is needed: the browser is still told to emit identifiers, so the device rule still applies. Present it as a governance improvement, never as a consent bypass; that reading follows the EDPB's technical-scope guidelines and is the author's.

These consent rules are still moving in Europe. The European Commission's **Digital Omnibus** proposal of November 2025 would move the device rule into the GDPR with four no-consent purposes (transmission, requested service, audience measurement, security), require a one-click refusal and oblige controllers to honor machine-readable browser signals; one law firm's reading (Osborne Clarke, December 2025) is that the end of cookie banners "is not yet in sight". It is a proposal, not law, as of November 2026.

In the United States, by contrast, the model is opt-out: California's law lets consumers opt out of the "sale or sharing" of their data, including through the Global Privacy Control browser signal, and the 2025 chart of the IAPP (International Association of Privacy Professionals) lists nineteen state laws of that family. That model has already been enforced on the tag layer. In a case from **August 2022**, more than three years old but still the reference example, California's Attorney General's settlement with Sephora (US$1.2 million) found that third-party trackers on Sephora's site and app amounted to a sale of personal information without notice, and that Global Privacy Control signals were not honored. The tag layer is a legal surface, and a browser signal must be read as well as a banner.

Whatever the rules become, consent has to be asked well where it is asked. **The store** is where consent is easiest to ask badly. The POS holds a loyalty list and receipts; a store may also run cameras, Wi-Fi analytics and tablet sign-ups. Consent asked at a till by a member of staff, in the staff member's own words, leaves no evidence. Kestrel & Pine's rule from mid-2027: the POS loyalty sign-up shows the same purposes and wording as the web, records the time and the store, and carries the master's consent once matched ([[identity-and-master-data]]).

The design consequence of all these rules joins this chapter to the identity chapter. **Consent is state that must travel**: from the CMP to the tag layer (the tags and the tool that loads them), to the newsletter tool and the CDP, to the POS where staff ask for a loyalty sign-up, and to every app that sends a message. [[identity-and-master-data]] put consent on the customer master with its time, place, wording and source. The reason is that the merchant must demonstrate it per person and per purpose, and withdraw it everywhere at once.

![A consent ticket on a customer record fanning out to the banner, tags, newsletter tool, store till and apps, each holding a copy.](assets/images/35-privacy-and-customer-data/35-consent-travels.jpeg)
**Figure 3:** *Consent is state that must travel: recorded once with its evidence on the customer master, it must reach every tag, tool, till and app, and a withdrawal must reach them all at once.*

## Retention: The Person Versus the Transaction

Consent decides which marketing may run; tax law decides how long the records of a sale must be kept. Tax law makes the merchant keep what privacy law makes it release. The retention facts, with their status:

- **Netherlands.** The government's business portal states that businesses "must keep your business records for at least 7 years", naming the general ledger, stock records, purchase and sales records and debtor and creditor accounts, with at least 10 years for data on immovable property, and requires digital files to remain accessible for inspection (business.gov.nl, n.d., accessed November 2026).
- **Germany.** §147 of the Abgabenordnung (the German Fiscal Code) requires books, records, inventories and annual accounts to be kept for ten years, accounting vouchers for eight, and other records including commercial letters for six, from the end of the calendar year of the record (gesetze-im-internet.de, current text, accessed November 2026).
- **Belgium.** Ten years for accounting records and invoices is widely cited; the official text was not verified for this chapter, and Sanne de Wit, the Finance Director, treats ten years as the Belgian rule pending confirmation.

So Lotte's invoice from November 2026 stays until at least the end of 2036 under the Belgian reading, whatever she asks; "legal obligation" is a lawful basis. The conflict arises only when the invoice *is* the customer record, as it is in many ERPs and platforms: the order carries name, address and e-mail, and the customer master is the list of people with orders. Deleting the person then means deleting the order, which tax law forbids, so nothing is deleted.

One design move reconciles the two laws: **split the person from the transaction.** The order and the invoice carry a customer reference and the delivery address (part of the transaction, kept for the fiscal period); the profile (e-mail, phone, preferences, consent, browsing, loyalty) is a separate, erasable record; and the analytics tables carry a hash of the customer reference, not the e-mail. **Retention periods become a property of each record type, not of the person**, and a nightly job purges what has expired without anyone deciding per customer.

![Diagram: Profiles are erasable](assets/images/35-privacy-and-customer-data/fig03-profiles-are-erasable-transactions-are-kept.jpeg)
**Figure 4:** *Profiles are erasable; transactions are kept with a reference that no longer points to a person once the profile is gone.*

Backups need a sentence. A deletion cannot reach into last month's backup; the accepted practice is a bounded, documented exception: backups are kept for a stated period, never used to resurrect erased data, and if one is restored the deletion log is replayed against it.

## Data Subject Requests Across Many Systems

With each record type sorted into what can go and what must stay, a request can be answered. A customer may ask to see, correct or delete personal data, and different vendors may hold the account, the orders and the marketing history. The GDPR requires the controller to act on a request "without undue delay and in any event within one month", extendable by two months for complex or numerous requests (Article 12(3)); a merchant that discovers the clock only when a request arrives meets the Long Fuse. What makes it hard is not the law but the fan-out: one person, many systems and vendors, a different right answer in each. Three parts make it a job.

**An identity index**: which systems hold this person, under which identifiers. This is the cross-reference [[identity-and-master-data]] built for another reason; a deletion request is its second customer. Without it, every request starts with a search of every system by e-mail, phone and name, which is where Lotte's seventeen days went.

**A request orchestrator**: a small workflow that verifies the requester (asking for "all my data" with someone else's e-mail is a way to steal it), fans the request out, records each answer and produces the reply. Shopify's compliance webhooks are the platform-side half of one; for the systems outside the platform, the merchant builds or buys the other half.

**A per-system action table**, decided in advance, applies the retention split to each system. (Anonymizing, which the shop platform does to orders, goes further than pseudonymizing: the link to the person is removed for good.)

| Answer | When | Example at Kestrel & Pine |
| --- | --- | --- |
| **Erase** | The purpose has ended and no law requires the data | The platform account, the loyalty entry, the newsletter subscription, the returns contact, old shipment addresses |
| **Pseudonymize** | The record must stay for accounting, statistics or evidence, but the person need not be identifiable from it | Orders in the platform and the OMS, warehouse rows, data-warehouse rows: name and address replaced by a token the merchant cannot reverse |
| **Retain** | A legal obligation applies or a claim is still possible | Invoices and credit notes in the ERP; recent shipments during the carrier's claims window; fraud evidence |

Two answers fall outside erase, pseudonymize and retain: **refer** (the carrier, the marketplace and the PSP are told, and the person must ask them too, because they are controllers in their own right) and **except** (backups, under the bounded exception described in the retention section: erased data is not restored, and if a backup is restored the deletion is replayed).

![Diagram: A deletion request is verified once, resolved against the identity index, fanned out with a predetermined action per system, and answered with a record of what each system did](assets/images/35-privacy-and-customer-data/fig02-deletion-request-verified-once-resolved-against.jpeg)
**Figure 5:** *A deletion request is verified once, resolved against the identity index, fanned out with a predetermined action per system, and answered with a record of what each system did.*

The reply should say, in plain words, what was erased, what was kept and why, and whom else to ask; the record behind it is what a regulator asks for.

## Requirements per Flow

With the request described, the chapter has met four privacy flows: capturing consent and withdrawing it (the consent section), the retention purge (the retention section) and the request. They differ in how fresh, consistent, fast and available each must be, and the consent flows must fail toward "no consent":

| Flow | How fresh | How consistent | How fast | How available |
| --- | --- | --- | --- | --- |
| Consent capture (banner, checkout box, store sign-up) | Immediate for the device; hours to reach every outbound tool | One record per person per purpose, with evidence | Must not slow the page or the till | Degrade to "no consent" when the CMP is down, never to "consent" |
| Consent withdrawal | Immediate for the channel used; same day everywhere | Strictest state wins across tools | Minutes | Works even if the master is unreachable; reconcile later |
| Data subject request | One month, extendable by two | Every system that holds the person answers; answers recorded | Days | Batch; the orchestrator can queue |
| Retention purge | Daily or weekly | Pseudonymize transactions; erase profiles; log what ran | Hours | Batch; a failed run must be visible |

## The Choices

The index, the orchestrator and the action table can be put together in different ways. For the data subject request there are four realistic designs; choose by the number of systems and requests:

- **A runbook by hand:** list the action and responsible person for each system. This can suit a small merchant with few requests.
- **Platform-centered handling:** use the platform's erasure and app notifications, with a runbook for outside systems.
- **An orchestrator on an identity index:** an integration flow that verifies the request, resolves identities, sends the required actions, records the results and replies. Kestrel & Pine adopts this in autumn 2027.
- **A privacy management product:** software that automates more intake, discovery and records across a larger group.

Map the data before choosing the product. Automation still needs to know which systems and records it must reach. The table compares the four options on when each fits, its strengths, its costs and limits, and the warning sign that a merchant has outgrown it.

| Option | Fits when | Strengths | Costs and limits | Warning sign |
| --- | --- | --- | --- | --- |
| Runbook by hand | Few systems, few requests | No build; forces the map to be written | Slow; no record unless disciplined | The runbook is a person's memory |
| Platform-centered | Most data in the platform and its apps | Erasure and app fan-out come with the platform | ERP, WMS, POS and warehouse are outside it | "The platform handles GDPR" |
| Orchestrator plus identity index | A dozen systems; weekly requests | Repeatable; a record per request; reuses the identity index | A flow to own; per-system steps; a human verification step | Requests queued behind other integration work |
| Privacy management product | Several brands, countries, entities | Intake, verification, discovery, consent and records in one place | License and configuration; connectors still map to your systems | Bought before the map exists |

## Across Scale Stages: When It Fits and When It Limits

Which of the four options fits depends on the stage. Across the four scale stages of this book ([[commerce-scaling-stages]]), the practices a merchant needs grow with the number of systems that hold a person. The table shows, for each stage, what is typical, what becomes necessary and the warning signs of outgrowing it.

| Stage | What is typical | What becomes necessary | Warning signs of outgrowing it |
| --- | --- | --- | --- |
| **1 — Starting** | The platform's standard DPA, cookie banner, checkout consent box and app vetting; requests handled in the platform admin | A privacy notice that matches the stack; a DPA for the 3PL and the e-mail tool; one person who answers requests | An app with no DPA; a newsletter list built from every order without a soft opt-in notice |
| **2 — Growing** | The first store, ERP and marketplace bring data outside the platform; a CMP with per-purpose consent | A DPA register and the rule that nothing goes in without one; a runbook for requests; consent on the customer record; a retention rule per record type | A request that takes two weeks; POS consent that never reaches the newsletter tool; tags firing before the banner answers |
| **3 — Omnichannel** | A dozen systems, 20–40 flows, requests weekly; a data warehouse keyed by e-mail | A data-flow map kept with the integration inventory; an identity index and a request orchestrator; the person split from the transaction; a transfer inventory; a bounded backup exception | A request that touches nine systems by hand; an erased customer resurrected by a backup; a court decision that forces a vendor-by-vendor investigation |
| **4 — Group** | Several brands, countries and legal entities, each a controller; a privacy function | One consent model with national differences as configuration; a privacy management product; a data protection officer where required; group-wide records of processing | One brand's consent used by another; two brands answering the same person differently |

The judgement: the duties do not change with scale; a Starting-stage merchant is as much a controller as a Group. What changes is where the data is. Below the Omnichannel stage the platform holds most of it and its DPA, banner and app rules do most of the work; from the Omnichannel stage the person is in a dozen systems and the merchant must own the map, the index and the orchestrator itself. Kestrel & Pine, an Omnichannel-stage merchant, learned that lesson from one request from Ghent.

## In Practice

### Kestrel & Pine's deletion design (autumn 2027, illustrative)

Kestrel & Pine built these parts after Lotte's request, in two steps. In **June 2027** the identity rule linked every system's record to the customer master ([[identity-and-master-data]]), and the July matching run produced the index.

In **October 2027** Ruben Alves built the request orchestrator as an iPaaS flow with a human verification step: the request is logged, the requester verified through the platform's account or a signed e-mail reply, the index queried and the action table applied.

The shop platform deletes the account, anonymizes the orders and notifies its apps; the OMS (taking marketplace orders since 15 September 2027) pseudonymizes its order copies; the WMS and the shipping service purge addresses older than their claims window of **twelve months** *(assumption)*; the ERP keeps invoices and credit notes and marks the customer reference as erased; the POS deletes the loyalty entry; the returns portal deletes the contact; the data warehouse replaces e-mail and name with a hash.

The carrier, the marketplace and the PSP are notified and the customer told to ask them directly. Backups are kept for **35 days** *(assumption)* and the deletion log is replayed after any restore.

The second request through the flow, in November 2027, took **two working days** *(illustrative)*. The map that made it possible, one row per system with its legal role, data, action and retention clock, is now the legal-role column on Noor's ownership map (her map of systems and their owners), reviewed quarterly.

## When It Goes Wrong

The design fails when one of its rules is skipped. Six failures recur, and each has a detection and a recovery that the chapter's rules supply. The missed copy is the one that recurs most, and its cause is a system added after the map was made; that is why the privacy map lives with the integration inventory and is reviewed when a row is added.

| Failure | How it shows | Detection | Recovery |
| --- | --- | --- | --- |
| **The missed copy** | An erased customer receives a newsletter because nobody reached the newsletter tool | A complaint; a reconciliation of erased master ids against each tool's list | Erase; add the tool to the index and the action table; ask who else was missed |
| **The resurrected customer** | A restore from backup brings back erased records | The deletion log replayed after a restore | Replay the log; document the backup exception |
| **The impostor** | Someone requests "all my data" with another person's e-mail | A verification step that fails | Never answer an unverified request with data; verify through the account or a signed reply |
| **The over-deletion** | An invoice or a fraud record is erased with the profile | The ERP's retention check; a tax audit | Restore from the retained copy; fix the action table: transactions retained, the person erased |
| **Consent without evidence** | Marketing cannot show when or how a person consented | A consent audit sampling records | Treat unevidenced consent as absent; re-ask where the soft opt-in does not apply |
| **The invalidated transfer** | A court or a decision removes a transfer mechanism | A transfer inventory naming the mechanism per vendor | Switch to SCCs or an EU region, vendor by vendor from the list |

## What to Take Away

The request from Ghent took seventeen working days for three reasons. Every integration had copied Lotte into a system with its own legal role. Her orders carried her as the person, so they could not simply be deleted. And nothing listed where she was or what each system should do. One map answers all three: for each system, its legal role, the action a request requires there and its retention clock, kept beside the integration inventory. With that map, consent on the customer master, the person split from the transaction and an orchestrator on the identity index, Kestrel & Pine answered its second request in two working days, with a record of what each system did, which is what a regulator asks for. A request from Eva about her jacket order would now take the same path.

**Established.**

- The merchant is the controller of its customers' data; its platform, warehouse system, integration platform and most apps are processors that need a contract; carriers, payment providers for the payment itself, and marketplaces usually decide for themselves (GDPR Articles 4 and 28; EDPB Guidelines 07/2020).
- Orders rest on the contract and on tax law; marketing rests on consent or the soft opt-in; consent must be demonstrable, and cookie walls, scrolling and pre-ticked boxes do not produce it (GDPR Articles 6 and 7; EDPB Guidelines 05/2020; the Dutch and Belgian regulators).
- Requests must be answered within one month, extendable by two (Article 12(3)); business records must be kept at least seven years in the Netherlands and ten, eight or six years in Germany depending on the record (business.gov.nl; §147 Abgabenordnung).
- Platforms have operationalized the fan-out: Shopify's three compliance webhooks and 30-day window are a documented, dated example.

**Depends on context.**

- Below the Omnichannel stage the platform's DPA, banner, consent box and app rules do most of the work; from the Omnichannel stage the merchant must own a data-flow map, an identity index and an orchestrator, because the platform's reach ends at its apps.
- The soft opt-in depends on national transposition and on the "similar products" test; take the lawyer's reading per country.
- The retention period per record type is a legal and finance decision per country; the architecture needs only that it be a property of the record type, not of the person.

**The author's synthesis.**

- Privacy in a commerce estate is an integration problem wearing a legal coat: the map, inventory and identity index that fix the Familiar Stranger make a deletion request a job rather than a hunt.
- Split the person from the transaction in the data model before the first request, because every system that stores the name on the order otherwise forces a choice between the tax law and the person.

## Questions to Ask

1. Which systems hold personal data, and does the system-of-record map say, per system, whether it is a processor or a controller?
2. Is there a signed DPA for every processor, including every app, and who keeps the register?
3. Where is consent recorded, with what evidence, and how long does a withdrawal take to reach every outbound tool?
4. Do tags fire before the banner is answered, and what happens when the CMP is down?
5. How would you find every record of one person today, and how long did the last request take?
6. Can an order outlive its customer in your data model, or does deleting the person delete the invoice?
7. Which vendors receive data outside the EU, under which mechanism, and is that a list or a memory?
8. What happens to an erased person when a backup is restored?

A deletion request is one legal clock among many. [[commerce-regulation]] lays out the others, from the right of withdrawal and the 30-day prior-price rule to e-invoicing, accessibility, product safety and the platform rules for marketplaces, and shows how Kestrel & Pine turned them into a regulatory calendar for 2027 so that no deadline is discovered only months before it applies.

## Sources and Evidence

*Company, product and investor sources*

- [Privacy law compliance](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance), Shopify developer documentation, n.d., accessed 2026-11 — the three compliance webhooks, the 10-day and 48-hour delays, the 30-day completion window.
- [Protected customer data](https://shopify.dev/docs/apps/launch/protected-customer-data), Shopify developer documentation, n.d., accessed 2026-11 — minimum data, purpose limitation, consent, retention, encryption and level-2 controls for apps.
- [Attorney General Bonta announces settlement with Sephora](https://oag.ca.gov/news/press-releases/attorney-general-bonta-announces-settlement-sephora-part-ongoing-enforcement), California Department of Justice, 2022-08-24 — trackers as a sale, Global Privacy Control, the US$1.2 million settlement.
- [Latombe's challenge to EU-US data transfers fails](https://www.lewissilkin.com/insights/2025/09/03/transatlantic-trouble-not-this-time-latombes-challenge-to-eu-us-data-transfers-fails), Lewis Silkin, 2025-09-03 — the General Court judgment and the advice to keep SCCs as a fallback.
- [Digital Omnibus reshapes EU cookie rules, leaves banner fatigue largely intact](https://www.osborneclarke.com/insights/digital-omnibus-reshapes-eu-cookie-rules-leaves-banner-fatigue-largely-intact), Osborne Clarke, 2025-12-10 — a reading of the November 2025 proposal.

*Standards, regulation and official documentation*

- [Regulation (EU) 2016/679 (GDPR)](https://publications.europa.eu/resource/celex/32016R0679), Official Journal text, 2016 — Articles 4, 6, 7, 12(3), 28, 33 and 83(5); application from 25 May 2018.
- [Directive 2009/136/EC](https://publications.europa.eu/resource/celex/32009L0136), Official Journal text, 2009 — the amended Article 5(3) device rule of the ePrivacy Directive.
- [Directive 2002/58/EC (ePrivacy), consolidated 2009](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02002L0058-20091219), EUR-Lex — Article 13(2), the soft opt-in; text more than three years old, national transpositions differ.
- [Guidelines 07/2020 on the concepts of controller and processor](https://www.edpb.europa.eu/system/files/2023-10/EDPB_guidelines_202007_controllerprocessor_final_en.pdf), European Data Protection Board, version 2.0, 2021-07-07 — purposes, essential and non-essential means.
- [Guidelines 05/2020 on consent](https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf), European Data Protection Board, 2020-05-04 — cookie walls, scrolling.
- [Guidelines 2/2023 on the technical scope of Art. 5(3) of the ePrivacy Directive](https://www.edpb.europa.eu/system/files/documents/2024-10/edpb_guidelines_202302_technical_scope_art_53_eprivacydirective_v2_en_0.pdf), European Data Protection Board, version 2.0, 2024-10-07 — pixels, URL tracking, IP-only tracking.
- [Cookies](https://www.autoriteitpersoonsgegevens.nl/themas/internet-slimme-apparaten/cookies), Autoriteit Persoonsgegevens (Dutch), n.d., accessed 2026-11 — functional and limited analytical cookies, tracking cookies, cookie walls.
- [Cookies en andere traceringsmiddelen](https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/internet/cookies), Gegevensbeschermingsautoriteit (Belgium, Dutch), 2023-11-17 — exempt categories, pre-ticked boxes, purpose grouping.
- [Keeping business records](https://business.gov.nl/regulation/keeping-business-records/), business.gov.nl (Netherlands Enterprise Agency), n.d., accessed 2026-11 — at least seven years; ten for immovable property; digital files accessible.
- [§147 Abgabenordnung](https://www.gesetze-im-internet.de/ao_1977/__147.html), gesetze-im-internet.de, current text, accessed 2026-11 — ten, eight and six years.
- [Commission Implementing Decision (EU) 2023/1795 (EU-US Data Privacy Framework)](https://publications.europa.eu/resource/celex/32023D1795), Official Journal text, 2023 — the adequacy decision.
- [Commission Implementing Decision (EU) 2021/914 (standard contractual clauses)](https://publications.europa.eu/resource/celex/32021D0914), Official Journal text, 2021.
- [Case C-703/25 P, Latombe v Commission](https://publications.europa.eu/resource/celex/62025CN0703), Official Journal C/2025/6610, 2025-12-22 — the pending appeal.
- [California Consumer Privacy Act](https://oag.ca.gov/privacy/ccpa), California Department of Justice, n.d., accessed 2026-11 — thresholds, rights, Global Privacy Control; [US State Privacy Legislation Tracker](https://iapp.org/resources/article/us-state-privacy-legislation-tracker/), IAPP, updated 2026-09-08, and its [2025 chart](https://prod.iapp.org/media/pdf/resource_center/State_Comp_Privacy_Law_Chart.pdf) — nineteen state laws.

*Research and practitioner sources*

- [[identity-and-master-data]] — the identity index this chapter's orchestrator depends on; [[fraud-prevention]] in the sibling book LISTED for the legitimate-interest side of risk screening.

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
