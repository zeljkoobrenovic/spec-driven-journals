{id: taxes-on-stays}
# 29. The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting

![The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting — logo](stays-marketplace-architecture/posts/29-taxes-on-stays/assets/images/29-taxes-on-stays/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn the taxes that attach to a night's stay (VAT on the accommodation, VAT on the marketplace's fee, tourist and occupancy taxes, income-tax withholding) and the platform reporting duties around them (DAC7, Form 1099-K). You will design a tax engine that sits beside pricing, decides who collects what, and leaves evidence that survives an audit five years later.

> **WHY THE BUSINESS CARES:** Taxes are part of the price the guest compares and a liability the marketplace may carry jointly with its hosts; one settlement can cost more than a year of engineering. Airbnb and Booking.com together have paid well over a billion dollars to settle Italian short-term-rental tax claims since 2023, and EU VAT law will make platforms the taxable supplier of most short-term rentals between 2028 and 2030.

> **WHY ARCHITECTS SHOULD CARE:** Tax logic hides in checkout code, partner free-text fields, finance spreadsheets and month-end scripts. When it moves into one engine with effective-dated rules and an immutable tax decision on every reservation, adding a city becomes a content change, and a tax authority's question becomes a query.

> **KEY POINTS:**
>
> * **A tax engine is a rules engine with a liability decision, not a rate lookup.** For every booking it must answer four questions: which jurisdictions, which taxes and amounts, who is legally liable, and who collects and remits. It must answer them at quote time, from effective-dated rules, and freeze the answer on the reservation.
> * **The platform's role is decided per booking, and it is moving.** Agency OTAs mostly display taxes that the property collects; merchant OTAs and hosted-stays platforms collect money and inherit tax duties with it. Tourist-tax agreements, Italy's withholding law, DAC7 and ViDA's "deemed supplier" rule each push hosted-stays platforms from tax displayer to tax collector and reporter.
> * **Tax lines belong in the ledger and in the reporting pipeline, not only on the receipt.** Every amount collected on someone's behalf needs a liability account per jurisdiction, a remittance trail and a link to the host or property it was collected for. DAC7 reporting is then a join over records the platform already keeps, not a seven-week spreadsheet project.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **The Tax Patchwork** — tourist taxes hard-coded city by city, VAT logic in finance scripts and reporting assembled by hand mean nobody can say what was collected for whom.
> * **Price Drift** — taxes added in different places make search, property page, checkout and receipt show four different totals.
> * **Ledgerless Money** — tax collected on a host's behalf without a liability account per jurisdiction cannot be remitted, reconciled or explained.

A night in Lisbon carries a nightly price, a cleaning fee, the marketplace's fee and a municipal tourist tax. The same night in Amsterdam carries a tourist tax that is a percentage of the room price, VAT on that price at a rate the Dutch government raised from 9% to 21% in January 2026, and a marketplace commission that is itself subject to VAT somewhere else. Each has its own taxpayer, base, rate and date rule. **No single owner sees the whole bill**: the guest sees a total, the host sees a payout, the city sees a remittance and the tax authority sees a report.

Most stays platforms meet these taxes one at a time: a city signs a collection agreement, so a developer adds a constant to checkout; a country announces platform reporting, so finance builds a spreadsheet. Ten years later the platform runs a **tax patchwork**: correct in most places, unexplainable in all of them, and slow to change just as regulators speed up.

This chapter argues for the opposite design: **tax as a bounded context with its own engine, its own data and its own owners**, called by pricing at quote time and by the ledger at booking time. It belongs to Part VI because taxes only become hard when the platform touches the money: [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models) decided who takes the guest's payment, [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments) took it, and [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) paid the supply side. This chapter decides which part of that money was never the marketplace's or the host's to keep, and [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation) then proves where it went. Total-price display belongs to [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) and the regulatory map to [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation); both read the tax engine's output.

{id: taxes-on-stays--setting-the-scene-at-corvane-a-56-line-and-a-january-deadline}
## Setting the Scene at Corvane: A €56 Line and a January Deadline

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), discovered its tax architecture in two places in the same month of 2027. The first was a single line on a receipt. On **14 February 2027** the Novak family from Prague booked a Nookaway apartment in Alfama for **2–9 August 2027**: two adults and two children aged 9 and 12. Nookaway's checkout showed this bill:

| Line | Amount | Who it belongs to |
| --- | --- | --- |
| 7 nights × €145 | €1,015.00 | Host (less host fee) |
| Cleaning fee | €70.00 | Host (less host fee) |
| **Subtotal** | **€1,085.00** | |
| Guest service fee, 12% of subtotal | €130.20 | Nookaway |
| Lisbon tourist tax: 2 adults × 7 nights × €4 | €56.00 | Municipality of Lisbon |
| **Total charged** | **€1,271.20** | |

The total was **25% above** the €1,015 that the nightly price suggested, which is why [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) uses this booking for total-price display. This chapter's line is the €56. Nookaway computed it in Burrow, the Django monolith, from a Python dictionary of **23 municipalities** where Nookaway collects and remits tourist tax under agreements with the cities. Each entry had been added by a developer from a ticket; the Lisbon entry encoded €4 per person per night, a seven-night cap and an exemption for children under 13, all three matching the municipal regulation (see tourist taxes below). It got the Novaks right only because Nookaway had started asking for children's ages at checkout in 2025, after an audit found the exemption applied to "children" as a count. Nobody outside the Nookaway checkout team knew the dictionary existed.

![A €1,271.20 receipt cut into three strips going to the host, Nookaway, and Lisbon's city hall for €56.](stays-marketplace-architecture/posts/29-taxes-on-stays/assets/images/29-taxes-on-stays/29-one-bill-many-owners.jpeg)

**Figure 1:** *One €1,271.20 Nookaway bill belongs to three owners: the host, Nookaway for its fee, and the municipality of Lisbon for the €56 tourist tax.*

Two streets away, Alfama Keys, a property manager with 38 apartments that it sells on Nookaway, also sold them on Roomstead, Corvane's OTA, under the agency model. Roomstead's property page said "City tax of €4 per person per night is not included and is payable at the property", text the manager had typed into a free-text field in the Partner Hub extranet. But the apartments had no front desk, only key boxes. Alfama Keys told Aisha Rahman's supply team that about **11%** of its Roomstead guests in 2026 had left without paying the tax it was legally required to collect, and asked why Roomstead could collect it for merchant bookings in Paris but not for its apartments, when Nookaway already did.

The second discovery was a deadline. Under the EU's DAC7 directive, Corvane's two platform operators had to report every reportable seller and what they earned in 2026 by **31 January 2027**. Nookaway's Portuguese operating company reported **538,000** hosts to the Portuguese tax authority after a nine-day pipeline run that joined Fathom, the group's ledger, to the listing catalog. Roomstead's Irish company reported **248,000** sellers covering **352,000** property listings to Ireland's Revenue, but only after **seven weeks** of work by a finance analytics team: Roomstead's agency bookings never pass through Corvane Payments, so the "consideration" each seller earned had to be reconstructed from Keystone reservations and commission invoices. **26,400** Roomstead sellers had no valid tax identification number at year end.

Mariana Costa, the Group Chief Architect, asked Leila Haddad (payments and finance engineering) and Noor van Dijk (regulatory affairs and privacy) where tax logic lived. The answer fit on one slide:

| Where | What it does | Who changes it |
| --- | --- | --- |
| Burrow (Nookaway checkout) | Tourist tax for 23 municipalities, hard-coded; VAT on the guest fee | Nookaway checkout team, by code release |
| Keystone (Roomstead) | Structured "taxes and fees" fields per property for 61 countries; free text elsewhere | Partners, in the extranet |
| Pricegrid (Roomstead search cache) | Excludes taxes; adds an "estimated taxes" line only on the property page | Search team |
| Corvane Payments | Merchant bookings: collects taxes the partner declared; Nookaway: posts the tourist tax to one "taxes payable" account per brand | Payments team |
| SAP S/4HANA | VAT on commissions and fees; VAT returns | Group finance |
| Spreadsheets | DAC7, tourist-tax remittance files for 23 cities | Finance analysts |

Mariana's question to the architecture forum was not "which tax engine should we buy?" but **"where should a tax decision be made, and what must every system downstream be able to prove about it?"** The answer became Levy, the One Stay tax engine.

![Left: a patchwork quilt of code, spreadsheet and note patches. Right: one tax engine called Levy with a versioned rulebook feeding three systems.](stays-marketplace-architecture/posts/29-taxes-on-stays/assets/images/29-taxes-on-stays/29-patchwork-to-engine.jpeg)

**Figure 2:** *Corvane's tax logic was a patchwork of checkout code, extranet text and spreadsheets for 23 cities; Levy turns it into one engine with versioned rules that every system calls.*

{id: taxes-on-stays--the-taxes-on-a-night-s-stay}
## The Taxes on a Night's Stay

A stays platform deals with four kinds of tax and two kinds of reporting. They differ in who owes them, what they are calculated on and where they are due, and the architecture has to carry all three.

| Tax or duty | Who is liable by default | Base | Where it is due | Platform's typical role |
| --- | --- | --- | --- | --- |
| **VAT on the accommodation** | The property or host, if VAT-registered | Price of the stay | Where the property is | None (agency); margin-scheme VAT (merchant reseller); **deemed supplier** under ViDA (2028–2030 onward) |
| **VAT on the platform's fee or commission** | The platform | Commission or service fee | Where the customer is established (B2B) or where the property is (B2C) | Charges and files it |
| **Tourist, occupancy or city tax** | Usually the guest, collected by the property or host | Per person, per room or a percentage, per night | Municipality, region or state | Displays it; or collects and remits under agreement or law |
| **Income-tax withholding** | The host | Host's rental income | Host's or property's country | Withholds and remits where law requires it (Italy) |
| **Platform reporting (DAC7, Form 1099-K)** | The platform | Consideration paid to sellers | Platform's reporting jurisdiction | Collects tax identity, reports annually |
| **Short-term-rental activity data** | The platform | Nights and guests per unit | Member state's single digital entry point | Reports monthly ([Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation)) |

Keeping four roles separate is the first design decision: the **taxpayer** owes the tax by law, the **collector** takes it from the guest, the **remitter** pays it to the authority and the **reporter** tells the authority what happened. On a hotel's agency booking the hotel plays all four. On a hosted-stays booking in a city with a collection agreement, the host may be the taxpayer while the platform collects, remits and reports. One `tax_amount` column cannot express that.

{id: taxes-on-stays--vat-on-the-night-itself}
### VAT on the night itself

In the EU, accommodation "in the hotel sector or in sectors with a similar function" is a service connected with immovable property and is taxed **where the property is** ([Council Directive 2008/8/EC](http://publications.europa.eu/resource/celex/32008L0008), 2008, substituting Article 47 of the VAT Directive). The rule is simple; the rates are not. Many member states apply a reduced rate to accommodation, and they change it: the Netherlands abolished its 9% rate for accommodation from **1 January 2026**, moving hotels, holiday homes, B&Bs and platform rentals to 21% while camping stays stayed at 9% ([Grant Thornton Netherlands](https://www.grantthornton.nl/insights/tax/verlaagd-btw-tarief-voor-logies-vervalt-per-1-januari-2026/), 2025). A booking made in 2025 for a 2026 stay crossed that line, so the engine has to know which event a rule keys on.

The **merchant model** adds a twist. When an OTA buys accommodation and resells it **in its own name**, EU law treats it as a travel agent under the special scheme of Article 306 of the VAT Directive, which applies only to agents who "deal with customers in their own name" and not to those acting "solely as intermediaries" ([Council Directive 2006/112/EC](http://publications.europa.eu/resource/celex/32006L0112), 2006). In *Alpenchalets Resorts* (C-552/17), the Court of Justice held that "the mere supply by a travel agent of holiday accommodation rented from other taxable persons" is a single service under that scheme and "cannot be subject to a reduced tax rate" ([CJEU, C-552/17](http://publications.europa.eu/resource/celex/62017CJ0552), 2018). How each OTA's contracts are characterized country by country is not public, and I will not guess. The architectural point: **the payment model is also a VAT model**: whether a booking is agency, merchant-as-agent or merchant-as-reseller must be a recorded attribute of the reservation, because it decides which VAT treatment applies ([Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models)).

{id: taxes-on-stays--vat-on-the-marketplace-s-own-fee}
### VAT on the marketplace's own fee

An OTA's commission and a hosted-stays platform's host and guest fees are the platform's own supplies. For a business customer, such as a hotel or a VAT-registered professional manager, the general rule taxes the service where the customer is established (Article 44, as substituted in 2008), normally by reverse charge. For a consumer, an intermediary "acting in the name and on behalf of another person" is taxed where the underlying transaction is supplied (Article 46), which for accommodation means where the property is ([Council Directive 2008/8/EC](http://publications.europa.eu/resource/celex/32008L0008), 2008). From 1 July 2028 the VAT in the Digital Age package (ViDA) restates this for platforms in a new Article 46a: the facilitation service to a non-taxable person through an electronic interface is supplied "where the underlying transaction is supplied" ([Council Directive (EU) 2025/516](http://publications.europa.eu/resource/celex/32025L0516), 2025).

So **one fee line can be taxed in a different country for every listing**, depending on whether the payer is a business; the engine needs the counterparty's VAT status as an input, not just the listing's address. The EU's One-Stop Shop (OSS), introduced in 2021, lets a business declare cross-border B2C services in one return instead of registering everywhere.

{id: taxes-on-stays--tourist-occupancy-and-city-taxes}
### Tourist, occupancy and city taxes

Tourist taxes are where the patchwork is densest. Municipalities, regions or states set them, in at least five shapes:

| Shape | Example | Data the engine needs |
| --- | --- | --- |
| Fixed amount per person per night, with caps and exemptions | Lisbon, since 1 September 2024: €4.00 per guest per night, up to 7 nights per stay, guests under 13 exempt (Regulamento Geral de Taxas, arts. 70.º and 71.º, as amended by [Aviso n.º 18684/2024/2](https://dados.gov.pt/api/1/datasets/r/d8ea0fd2-6762-4abf-8d8f-3ce6390f34d6), Diário da República, 2.ª série, 26 August 2024) | Guest count, ages, nights, property location |
| Percentage of the room price | Amsterdam: 12.5% of the overnight price excluding VAT since 2024; the city's coalition proposed 16% for 2027 and then one point a year up to 20% ([NL Times](https://nltimes.nl/2025/11/28/amsterdam-may-raise-tourist-tax-curb-mass-tourism), 2025; [Skift](https://skift.com/2026/06/05/amsterdam-proposes-tourism-tax-hike-to-20/), 2026) | Price excluding VAT, VAT rate |
| Percentage per person, capped by category | France: for unclassified furnished tourist rentals, communes set 1%–5% of the per-person nightly price, capped at the commune's highest tariff, plus departmental and regional surcharges ([Hostaway guide](https://www.hostaway.com/vacation-rental-guide/tourist-tax/france/), 2026) | Price, guest count, classification, surcharges |
| Tiered by property classification | Common in hotel-heavy cities: rates by star rating | Official classification of the property |
| Per room per night, or per stay | Common in US occupancy-tax ordinances | Room count, stay length thresholds |

The Lisbon rule shows how much a one-line rate hides. The regulation exempts guests "com idade inferior a 13 anos" and extends the exemption to the day a child turns 13, caps the tax at seven nights per guest and per stay, and exempts guests staying for medical treatment, plus one companion, and students starting higher education for up to 60 days; the €4.00 rate replaced €2.00 on 1 September 2024. The Amsterdam increase was still a proposal. **Both are the lesson**: tourist-tax rules change by municipal decision, so every rule in the engine needs a source and a review date.

Who collects depends on agreements and law. Airbnb's help center lists **72 locations** (20 countries and 52 US entries, at country and state level) where "Airbnb calculates these taxes and collects them from guests at the time of booking" and "then remits collected taxes to the applicable tax authority on the hosts' behalf"; hosts there remain "responsible for assessing all other tax obligations" ([Airbnb Help Center, article 2509](https://www.airbnb.com/help/article/2509), n.d., fetched 2026-10). Where Airbnb does not collect, "the responsibility for collecting and remitting these taxes, if applicable, generally rests with hosts", and Airbnb's FY2025 annual report says it reserves for jurisdictions where it could be held "jointly and severally liable with hosts" ([Airbnb 10-K](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), filed February 2026). The phrase "joint and several" is the architectural trigger: **if the platform can be made to pay a tax it did not collect, it needs to know, per booking, whether it collected it.**

{id: taxes-on-stays--the-united-states-occupancy-tax-and-the-merchant-model}
### The United States: occupancy tax and the merchant model

The US had the longest-running fight over platforms and lodging taxes. Expedia's FY2025 annual report says it still has "two lawsuits involving hotel occupancy taxes", argues that the statutes "generally impose occupancy and other taxes on entities that own, operate or control hotels", and notes that some jurisdictions have since legislated taxes on "businesses that facilitate the booking of hotel or alternative accommodations" ([Expedia Group 10-K](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm), filed February 2026). Booking Holdings reports litigation relating to "travel transaction taxes (e.g., hotel occupancy taxes)" ([Booking Holdings 10-K](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), filed February 2026).

The core dispute, as commonly summarized, was whether occupancy tax on a merchant-model booking is due on the **retail price the guest pays the OTA** or only on the **net rate the hotel receives**; many jurisdictions answered with intermediary or marketplace-facilitator laws that tax the full guest price and make the platform collect. (I have not verified individual cases from court records and do not cite them.) So **the tax base is not always the supplier's price**: depending on jurisdiction and payment model, the engine must tax the guest price, the supplier's net price or the platform's margin.

US platform reporting moved too. The IRS states that third-party settlement organizations need not file Form 1099-K unless payments to a payee exceed "$20,000 and the number of transactions exceeds 200", retroactively restoring the pre-2021 threshold that had been scheduled to fall to $600 ([IRS](https://irs.gov/newsroom/irs-issues-faqs-on-form-1099-k-threshold-under-the-one-big-beautiful-bill-dollar-limit-reverts-to-20000), 2025). Thresholds that change this often belong in configuration, not code.

{id: taxes-on-stays--withholding-when-the-platform-becomes-the-host-s-tax-agent}
### Withholding: when the platform becomes the host's tax agent

Italy's 2017 short-term-rental law shows how far a platform's role can extend. Airbnb's annual report says Italy passed a law "purporting to require short-term rental platforms that process payments to withhold and remit host income tax and collect and remit tourist tax"; Airbnb Ireland settled the 2017–2021 audit periods for **€576 million** in December 2023, 2022 for €139 million and 2023 for €179 million, without admitting liability ([Airbnb 10-K](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), filed February 2026). Booking.com settled a claim under the same law, that it should have withheld 21% of transaction value for certain Italian short-term-rental partners, for **$332 million** in November 2024, also without admitting liability ([Booking Holdings 10-K](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), filed February 2026).

A withholding duty works only if the platform controls the money flow and can tell which sellers are in scope. It is the clearest case where **tax classification of the seller** (individual host, professional manager, hotel company) becomes an input to payouts, not just to reports.

{id: taxes-on-stays--deemed-supplier-vida-and-short-term-accommodation}
### Deemed supplier: ViDA and short-term accommodation

The biggest change ahead is ViDA's **deemed supplier** rule. Council Directive (EU) 2025/516 inserts Article 28a into the VAT Directive: a platform facilitating "short-term accommodation rental services, namely the uninterrupted rental of accommodation to the same person for a maximum of 30 nights" through an electronic interface is "deemed to have received and supplied those services themselves", unless the underlying provider has given the platform a VAT identification number for the member state of supply **and** "declared to the taxable person facilitating the supply that they will charge any VAT due" ([Council Directive (EU) 2025/516](http://publications.europa.eu/resource/celex/32025L0516), 2025).

Three details shape the architecture:

- **Dates.** The article applies from 1 July 2028, but member states may apply it "at the earliest from 1 July 2028 and at the latest from 1 January 2030". A group with listings in many member states faces a staggered go-live it does not control.
- **Options.** Member states may require the platform to validate the supplier's VAT number (Art. 28a(4)) and may exclude suppliers under the small-enterprise scheme (Art. 28a(5)). The rule set differs per member state.
- **Consequences.** When the platform is deemed supplier, the host's supply to the platform is exempt (new Article 136b) and the platform charges VAT on the accommodation to the guest. When it is not, it must keep records "sufficiently detailed" for authorities to verify that VAT was accounted for.

The recitals say platforms "should be required to charge VAT where underlying suppliers do not charge VAT because they are, for example, non-taxable persons or taxable persons availing themselves of the special scheme for small enterprises". In plain terms: **hotels mostly stay outside the rule, and individual hosts mostly fall inside it**. Booking Holdings already lists ViDA as a change that "could increase complexity and costs associated with compliance" ([Booking Holdings 10-K](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), filed February 2026).

{id: taxes-on-stays--platform-reporting-dac7}
### Platform reporting: DAC7

Council Directive (EU) 2021/514, known as **DAC7**, makes "the rental of immovable property, including both residential and commercial property" a relevant activity for platform reporting from the reportable period starting **1 January 2023**, with reports due "no later than 31 January of the year following the calendar year" in which a seller is identified as reportable ([Council Directive (EU) 2021/514](http://publications.europa.eu/resource/celex/32021L0514), 2021). Five definitions in its annex carry most of the design weight:

- A **reportable seller** is an active seller, other than an excluded seller, "that is resident in a Member State **or** that rented out immovable property located in a Member State". A host living in Brazil with an apartment in Seville is reportable.
- **Excluded sellers** include governmental entities, listed companies and their related entities, and "an Entity for which the Reporting Platform Operator facilitated more than 2 000 Relevant Activities by means of the rental of immovable property in respect of a Property Listing". Large hotels can fall out; small hotels do not.
- A **property listing** is "all immovable property units located at the same street address, owned by the same owner and offered for rent on a Platform by the same Seller".
- **Consideration** is "compensation in any form, net of any fees, commissions or taxes withheld or charged by the Reporting Platform Operator, that is paid or credited to a Seller ... the amount of which is known or reasonably knowable by the Platform Operator". Agency bookings count, even though the platform never touches the money.
- For individuals the platform must collect name, primary address, any tax identification number (TIN) with its issuing state, VAT number where available, and date of birth; for property sellers it reports each listing's address, consideration and number of rentals per quarter, and, where available, days rented and property type.

DAC7 also sets the enforcement path: if a seller does not provide the required information "after two reminders following the initial request", but not before 60 days have passed, the platform "shall close the account of the Seller and prevent the Seller from re-registering on the Platform **or** withhold the payment of the Consideration to the Seller" until the information arrives. A platform that pays its sellers can withhold payouts, the gentler lever. **An agency-model OTA has no payout to withhold**, so its only lever is closing the account and delisting a property that guests may have booked.

{id: taxes-on-stays--architecture-a-tax-engine-beside-the-price}
## Architecture: A Tax Engine Beside the Price

The design I recommend separates five responsibilities that the tax patchwork fuses: knowing the parties, knowing the places, knowing the rules, deciding per booking, and keeping the books.

![Seller profile, jurisdictions and rules feed a tax calculation engine that answers the quote; the reservation freezes the result, the ledger records liabilities, and remittance and reporting read from the ledger.](stays-marketplace-architecture/posts/29-taxes-on-stays/assets/images/29-taxes-on-stays/29-tax-engine-five-parts.jpeg)

**Figure 3:** *A tax engine as five parts around one decision. The calculation service is a pure function of the request, the seller's tax profile, the jurisdictions and the effective-dated rules; the reservation freezes its answer; the ledger turns it into liabilities that remittance and reporting read.*

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Tax party registry** | Who the seller is for tax purposes: individual or entity, residence, TIN and issuing state, VAT numbers per member state and their validation results, ViDA declarations, trader status, small-enterprise status | Seller tax profiles, versioned over time; collection and reminder workflow | Copy identity data the identity platform already holds ([Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access)) |
| **Jurisdiction resolver** | Turn a property's location into the set of taxing jurisdictions: country, region, municipality, special districts | Boundaries, geocodes, overrides for addresses on boundaries | Rely on a host-entered city name |
| **Rule and rate content** | Rates, bases, caps, exemptions, thresholds, rounding, collection agreements, date basis, each with source, effective dates and reviewer | Versioned rule content; review workflow | Live in code |
| **Tax calculation service** | Given a tax request, return tax lines, inclusion mode and the liability decision (who is taxpayer, collector, remitter) | Calculation logic; determination record format | Call payment, reservation or ledger services |
| **Ledger postings** | Record every tax line as a liability, receivable or expense per jurisdiction | Tax accounts in the ledger ([Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement)) | Recompute tax |
| **Remittance and filing** | Aggregate liabilities per authority and period, file returns, pay, reconcile | Filing calendar, returns, payment evidence | Change determinations; corrections are new entries |
| **Platform reporting** | DAC7, 1099-K and similar: join ledger consideration, listings and tax profiles per period | Report generation, submission receipts, corrections | Derive consideration from anything but booked and ledgered facts |

Four rules make the design work.

**1. The liability decision is an output, not an assumption.** The engine's answer is not "€56 of tax" but "€56 of Lisbon tourist tax, owed by the guest, collected by Nookaway under the Lisbon agreement, remitted by Nookaway, reported in Nookaway's monthly return". For a Roomstead agency booking in the same street it is "€56 owed by the guest, collected and remitted by the property, displayed by Roomstead". Same rule, different roles; downstream systems read the roles instead of inferring them from the brand.

**2. Calculate at quote, freeze at booking, recalculate only as a delta.** The engine runs when an offer is priced, so the guest sees the tax before paying, as consumer law requires ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection)). At booking the reservation stores the **tax determination**: inputs, rule versions, outputs and engine version. A later rate change never silently alters it; where the rule keys on the stay date, the engine issues an explicit, recorded adjustment. A modification (an extra night, a third guest) produces a new determination and a delta, never an overwrite. Airbnb described the same idea for payments in a [2022 engineering post](https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b), where an alteration such as "adding another night to a stay" is modeled "as a new version in a sequence of plans for that product".

**3. Every rule declares its date basis.** A rule can key on the booking date, the stay night, the payment date or the invoice date. VAT rate changes often follow the chargeable event and tourist taxes the night stayed, but each rule must say so, never "the rate in force when the code ran". The Dutch move from 9% to 21% tested every system that took 2025 bookings for 2026 nights.

**4. Rounding, currency and inclusion are part of the rule.** Per-night or per-stay calculation, per-line or per-invoice rounding, local currency and price inclusion vary by jurisdiction. Corvane found three rounding behaviors for the same French percentage tax across Burrow, Keystone and Corvane Payments. The engine computes in the jurisdiction's currency and returns both the local amount and the presentment amount, so [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments) never recomputes tax in another currency.

{id: taxes-on-stays--the-tax-request-and-response}
### The tax request and response

The interface is small on purpose. Pricing, checkout, modification and the extranet's "preview your guest price" screen all call the same endpoint.

| Request field | Why the engine needs it |
| --- | --- |
| Property or listing id, with resolved location | Jurisdiction set |
| Seller tax profile reference and version | VAT status, deemed-supplier test, withholding scope |
| Stay dates, nights, booking date | Date basis, caps, length-of-stay exemptions (ViDA's 30-night limit, monthly-stay rules) |
| Guests with ages and, where rules need it, residence | Per-person taxes, child and resident exemptions |
| Price components: nightly prices, cleaning and other fees, discounts, platform fees, each with its currency | Bases differ per tax |
| Payment model: agency, merchant-as-agent, merchant-reseller, facilitated | Collector role, VAT scheme |
| Guest type: consumer or business, with VAT number | Fee VAT place of supply |
| Purpose: quote, booking, modification, cancellation | Determinations are only stored for bookings and changes |

| Response field | Who uses it |
| --- | --- |
| Tax lines: tax type, jurisdiction, base, rate, amount, local and presentment currency | Checkout, receipt, ledger |
| Inclusion mode per line: included in price, added to total, payable at property | Property page, search price display |
| Liability decision per line: taxpayer, collector, remitter | Ledger, payouts, partner statements |
| Rule version ids and sources | Audit, support |
| Determination id and expiry | Reservation, price re-check at checkout |

Search is the exception. It prices hundreds of candidates per query from caches such as Corvane's Pricegrid ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)), and a call per candidate would put the engine on the platform's hottest path. I recommend that the engine **publish a compiled, read-only rule set** per jurisdiction that search evaluates locally (at Corvane, inside the shared offer kernel that Pricegrid, the metasearch feed and checkout already use), labeling the result an estimate only where the rule needs data search lacks, such as ages. The checkout determination stays authoritative, and the price-accuracy metric measures how often the two disagree.

{id: taxes-on-stays--one-booking-from-quote-to-report}
### One booking, from quote to report

![Swimlanes for guest, checkout, tax engine, ledger and filing: a quote calls the tax engine once, the booking posts a liability to the ledger, and the ledger feeds monthly remittance and DAC7 reporting.](stays-marketplace-architecture/posts/29-taxes-on-stays/assets/images/29-taxes-on-stays/29-booking-quote-to-report.jpeg)

**Figure 4:** *One booking from quote to report. The engine is called before payment and never again for the same version of the reservation; the ledger, not the checkout, is the source for remittance and for platform reporting.*

{id: taxes-on-stays--where-tax-sits-among-the-bounded-contexts}
### Where tax sits among the bounded contexts

Tax is a **supporting subdomain** in the sense of [Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts): essential, regulated and nothing a guest chooses a marketplace for. That argues for one group engine, not a module per brand, and against folding tax into pricing. Pricing decides what the host and the marketplace charge; tax decides what the law adds and who owes it. A revenue manager may change a price; only the tax function changes a rate. Where a group buys rate content from a commercial provider, the rule store imports it through an anti-corruption layer so the vendor's schema never reaches reservations.

{id: taxes-on-stays--in-practice-levy-at-corvane}
## In Practice: Levy at Corvane

{id: taxes-on-stays--the-decision-who-collects-per-booking}
### The decision: who collects, per booking

Levy's first release, in **Q4 2027**, replaced Burrow's dictionary for Nookaway's 23 tourist-tax municipalities in Portugal, Spain, France, Italy and Greece. Its most-used output was the liability decision, which follows a short tree.

![Decision tree: if a law or agreement applies the platform collects; otherwise if it takes the payment and the partner opted in it collects, else the tax is shown as payable at the property; both outcomes are recorded.](stays-marketplace-architecture/posts/29-taxes-on-stays/assets/images/29-taxes-on-stays/29-liability-decision.jpeg)

**Figure 5:** *The liability decision. Law and agreements come first; where neither applies, the payment model and the partner's choice decide whether the platform collects or only displays the tax. Both branches are recorded on the reservation, because "we did not collect" is also a fact an authority may ask about.*

The tree answered Alfama Keys' question: on agency bookings Roomstead could not collect the tax without taking the guest's payment. The fix was commercial, not technical: Alfama Keys moved its apartments to "Pay with Roomstead", the merchant model, where Levy could mark the tourist tax as platform-collected and Corvane Payments could pass it on with the remittance to the manager or remit it to the city under an agreement. For hotels with a front desk, Levy kept "payable at property", because the hotel collects reliably and prefers its own folio.

{id: taxes-on-stays--worked-example-the-novak-booking-in-the-ledger}
### Worked example: the Novak booking in the ledger

Every party appears in the Novaks' booking. Levy's determination, frozen on the reservation on 14 February 2027, contained two tax decisions: the Lisbon tourist tax, collected and remitted by Nookaway, and VAT on Nookaway's two fees. In Corvane's model both fees are VAT-inclusive and supplied to consumers in Portugal, so VAT is due at Portugal's standard rate, 23% in mainland Portugal ([Código do IVA, art. 18.º](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva18.aspx), n.º 1, alínea c), as of October 2026). Fathom, the double-entry ledger, records the money as follows at booking:

| Account | Debit | Credit |
| --- | --- | --- |
| Guest funds receivable (Adyen, EUR) | €1,271.20 | |
| Payable to host (Alfama listing), held until payout | | €1,041.60 |
| Unearned fee revenue, Nookaway (net of VAT): guest fee €105.85 + host fee €35.28 | | €141.13 |
| VAT payable, Portugal (fees): €24.35 + €8.12 | | €32.47 |
| Tourist tax payable, Lisboa | | €56.00 |

The entries balance: €1,041.60 + €141.13 + €32.47 + €56.00 = €1,271.20. The host's €1,041.60 is the €1,085 subtotal less the 4% host fee of €43.40. At check-in on 2 August the fee revenue becomes earned, and 48 hours later, on 4 August, the payout releases the host's balance ([Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement)). The tourist tax waits for the August return to the municipality, and the VAT for Nookaway's Portuguese VAT return; both read balances and compute nothing.

Two details mattered more than the arithmetic. First, the liability is posted **per jurisdiction and per reservation**, so a cancellation reverses exactly the €56 it created ([Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation)). Second, the host's statement lists the €56 as "collected and remitted by Nookaway on your behalf"; a manager who sells the same apartment on Nookaway and on an agency OTA needs that line to avoid remitting the tax twice, or not at all.

{id: taxes-on-stays--worked-example-rehearsing-vida-on-the-same-booking}
### Worked example: rehearsing ViDA on the same booking

In the autumn of 2027 Leila Haddad's team replayed the Novak booking under ViDA, using an illustrative design date of 1 July 2028 because Portugal's choice of date was not yet known. Suppose the Alfama host is an individual without a Portuguese VAT number. Under Article 28a, Nookaway becomes the deemed supplier of the seven nights to the Novaks. Using 6%, the mainland Portuguese reduced rate for accommodation (Código do IVA, art. 18.º, n.º 1, alínea a), and Lista I, verba 2.17, which the tax authority applies to *alojamento local*, cleaning fee included, in a 2026 binding ruling), the team found three business decisions in one calculation:

| Question | Option A | Option B |
| --- | --- | --- |
| Is the host's price VAT-exclusive? | VAT added on top: €1,085 × 6% = **€65.10**; guest total rises to €1,336.30 | Price treated as VAT-inclusive: VAT = €1,085 × 6/106 = **€61.42**, carved out of the host's payout |
| Is the guest fee now part of the accommodation supply? | No: fee keeps standard-rate VAT | Yes: fee taxed with the accommodation; requires tax counsel's view per member state |
| Is the tourist tax inside the VAT base? | Assumed no for this illustration | Must be confirmed per jurisdiction |

Option A protects the host and raises the guest's price by 5%; Option B keeps the guest's price and cuts the host's payout by €61.42 on a €1,085 stay. Neither is an engineering decision, but **both require the same engineering**: a seller tax profile that knows whether the host has a VAT number and has made the Article 28a declaration, a per-member-state rule set for the go-live date, a guest invoice issued in Nookaway's name, and a host statement that explains the change. The rehearsal also found that 31% of Nookaway's professional managers in Portugal had a VAT number on file but no record of whether they charge VAT on their stays; until ViDA nobody needed that field.

{id: taxes-on-stays--worked-example-dac7-for-the-2027-period}
### Worked example: DAC7 for the 2027 period

The DAC7 report for 2027, due by 31 January 2028, was Levy's second test. It treated reporting as a **read model** over three sources the group already owned:

1. **Consideration per seller per quarter** from Fathom. For Nookaway and Roomstead merchant bookings it is the payable posted to the host or property, net of fees and of taxes the platform withheld or charged. For Roomstead agency bookings, which never pass through Corvane Payments, the team added a ledger posting that Fathom had never needed: a memorandum entry at check-out recording the agency booking's "reasonably knowable" consideration (the stayed amount less Roomstead's commission), reversed if the commission invoice was later credited.
2. **Property listings** from the listing and property catalogs, grouped by DAC7's definition: same street address, same owner, same seller. A hotel is one listing; so is a building of eight apartments owned by one of Alfama Keys' landlords.
3. **Seller tax profiles** from the tax party registry, with the reminder history that DAC7's 60-day rule needs.

The excluded-seller test ran on the same data. Hotel Miradouro, the 84-room Lisbon hotel that sells through Roomstead, had **2,140** stayed Roomstead reservations in 2027, so it crossed the 2,000-rental threshold and was excluded; a 12-room guesthouse on the same street was reportable. The threshold applies per platform operator, so a hotel can be excluded on one OTA and reportable on a smaller one.

Enforcement differed by payment model. On Nookaway, hosts without a TIN after two reminders and 60 days had their payouts withheld; in 2026 that had affected **14,900** hosts, most of whom supplied the number within two weeks. On Roomstead agency bookings the same rule meant closing accounts. Noor van Dijk's team made the TIN mandatory at onboarding for new partners and ran the two reminders for the **26,400** existing sellers through the Partner Hub with the 60-day clock visible to each partner; **1,700** accounts were closed at the end of it, against a forecast of several thousand. The report for 2027 ran in four days.

{id: taxes-on-stays--trade-offs}
## Trade-offs

| Decision | Option | When it is right | Cost |
| --- | --- | --- | --- |
| **Engine sourcing** | Buy a commercial tax engine and content | Wide jurisdiction coverage needed quickly; US lodging taxes; small tax team | License cost; vendor schema; weaker fit for platform-specific roles (collector vs taxpayer) and ViDA declarations |
| | Build the engine, buy the content | Group with several brands, its own ledger, and roles that commercial engines do not model | Engineering team of its own; content import and review |
| | Build both | Narrow footprint (a few countries) | Research burden grows with every market |
| **Collection policy** | Platform collects and remits wherever allowed | Hosted stays; merchant bookings; cities that prefer platform collection | Registration, filing and liability in many jurisdictions; joint-liability exposure when it is wrong |
| | Display only; property or host collects | Agency bookings; hotels with front desks | Uncollected tax at self-check-in homes; Price Drift if the display is wrong |
| **Price display** | Tax-inclusive everywhere | Markets whose consumer law expects all-in prices; guest trust | Search must estimate taxes for many candidates |
| | Tax shown separately before payment | Markets that allow it (the US FTC fees rule allows taxes to be excluded if disclosed before payment details are entered) | Two numbers to keep consistent; surprise at checkout |
| **Determination timing** | Freeze at booking, adjust by explicit delta | Almost always | Adjustment flows for rate changes keyed on the stay date |
| | Recompute at stay or invoice | Long-stay or monthly billing where law taxes each period | Guest may owe more than quoted; needs disclosure |
| **Ownership** | One group engine | Several brands in overlapping countries | Cross-brand governance; brand teams lose a lever |
| | One engine per brand | Brands in disjoint markets with different payment models | Duplicate content and duplicate audits |

The decision I would defend in most groups is **build the engine, buy the content, collect wherever the platform takes the money, and freeze at booking**. Commercial engines are strong on rates and weak on who, for this booking, is the taxpayer, the collector and the remitter, because that depends on the payment model, the seller's tax profile and the platform's agreements. For a single-country marketplace or an agency-only OTA, a commercial engine behind a thin adapter is cheaper.

{id: taxes-on-stays--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (OTA-style) | Hosted-stays marketplace |
| --- | --- | --- |
| **Who the supplier is for tax** | VAT-registered businesses that charge VAT and collect city tax at the desk | Mostly individuals and small managers, often not VAT-registered, with no desk |
| **Platform's default role** | Displayer (agency); collector of taxes the partner declares (merchant); possibly margin-scheme VAT as reseller | Collector and remitter of tourist taxes where agreements exist; future deemed supplier for VAT; withholding agent where law requires |
| **Data model** | Taxes and fees per property, often per rate plan; inclusion flags per country; tiered by star rating | Taxes per listing location and guest mix (ages, nights); fees split guest and host |
| **Integration** | Taxes arrive with ARI and content from channel managers and the extranet; risk of partner-entered errors | Platform owns the calculation; PMS-connected managers need the platform's tax lines in their statements |
| **DAC7** | Many small hotels reportable; large hotels excluded by the 2,000-rental test; agency consideration must be derived | Nearly every host reportable; consideration comes straight from payouts; payout withholding is available |
| **Failure modes** | Wrong partner-entered tax data; taxes excluded from search price; occupancy-tax disputes on merchant margins | Hard-coded city rules; uncollected tax at self-check-in; missing TINs; VAT status unknown when ViDA arrives |
| **Regulation trend** | Stable: hotels already collect | Accelerating: DAC7, Italian withholding, ViDA, STR data reporting all target hosts |

**What to share:** the engine, the rule content, the jurisdiction resolver, the tax party registry and the reporting pipeline. A Lisbon tourist-tax rule is the same for a hotel room and an apartment; only the liability decision differs. **What not to share:** each brand's collection policy and commercial terms, and its partner-facing presentation. Convergence raises the shared engine's value: when Nookaway pilots boutique hotels in 2028 and Roomstead keeps adding apartments, a brand-specific tax module would have to learn the other brand's supply.

{id: taxes-on-stays--failure-modes}
## Failure Modes

- **Tax as a constant in checkout code.** Every new city is a release and every rate change a hotfix. The rate goes live when the code ships, not when the ordinance says, so bookings that straddle a change get whichever rate the developer assumed.
- **One tax amount, no roles.** When a city asks what was remitted for a host, the answer requires reading code.
- **Unvalidated partner tax data.** A hotel enters a percentage where the city charges a fixed amount, and the OTA displays it for years. Check partner input against the rule store.
- **Ages and residence not collected.** A rule exempts children or residents, but checkout asks only for a guest count, so the engine overcharges or underpays and nobody sees it until an audit.
- **Liabilities without jurisdictions.** A single "taxes payable" account per brand makes remittance a spreadsheet exercise and a cancellation a guess: Ledgerless Money for tax.

{id: taxes-on-stays--the-chief-architect-s-view}
## The Chief Architect's View

At group scale the tax engine is less a technical system than an **accountability boundary**. These are the decisions I would put to the architecture forum and the CFO.

**Ownership.** The engine and the tax party registry belong to payments and finance engineering, because their outputs are ledger entries. The rule content belongs to the group's indirect-tax team, with regulatory affairs for non-tax duties that share the same data, such as STR activity reporting. Tax specialists, not developers, change rates, through a reviewed workflow with a source and a second approver. At Corvane, Levy sits in Leila Haddad's team in Kraków, and the indirect-tax team under Marco Bellini owns the content.

**Contracts.** The tax determination id and the liability decision become fields in the shared **offer** and **reservation** contracts of the One Stay program ([One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces)). Every brand that books a stay must carry them; that keeps a group engine a group engine.

**Forcing dates.** ViDA's window of 1 July 2028 to 1 January 2030 anchors the plan. Working back from it: seller VAT status and declarations collected in 2027–2028, guest invoices in the platform's own name, per-member-state go-live configuration, and a replay of a full year of bookings under the new rules before the first country switches.

**What to watch.** Four measures show the board whether the patchwork is shrinking:

| Measure | What it shows |
| --- | --- |
| Share of booked tax lines produced by the engine (target 100%) | How much tax logic still lives elsewhere |
| Days from an ordinance to a live rule | Whether rate changes are content changes or projects |
| Unremitted tax liability older than its filing deadline, per jurisdiction | Whether collection and remittance are connected |
| Seller tax-profile completeness (TIN, VAT status, declarations) | Readiness for DAC7 enforcement and ViDA |

{id: taxes-on-stays--questions-to-ask}
## Questions to Ask

1. For one booking in each of your top ten cities, can you show who is the taxpayer, the collector and the remitter of each tax line, and where that decision is recorded?
2. Which date does each rule key on, and what happens to a booked reservation when a rate changes before the stay?
3. Does checkout collect every attribute your rules need, such as children's ages, guest residence and business VAT numbers?
4. Is tax collected on behalf of others posted to liability accounts per jurisdiction, and does a cancellation reverse exactly what the booking created?
5. Can you produce your last DAC7 report again from source data, including the reminder history for sellers without a TIN?
6. For agency bookings, how do you compute "reasonably knowable" consideration, and what is your enforcement lever when a seller will not provide tax data?
7. Which of your hosts and partners will make your platform the deemed supplier under ViDA, and do you know their VAT status per member state today?
8. Who can change a tax rate in production, and what source and review does that change require?

The tax engine decides which part of the guest's money belongs to a city or a tax authority, and the ledger records it as a liability. The next chapter, [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation), follows the money when bookings are canceled, charged back or settled late, and shows how a stays marketplace proves that every euro, including every euro of tax, ended up where it should.

{id: taxes-on-stays--sources-and-evidence}
## Sources and Evidence

*Company engineering and investor sources*

- [Airbnb, Inc. Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm) — Airbnb, 2026: Italian STR settlements (€576M, €139M, €179M), joint and several liability reserves, taxes excluded from revenue.
- [Booking Holdings Inc. Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm) — Booking Holdings, 2026: $332M Italian STR settlement (November 2024), ViDA as a compliance risk, travel transaction tax litigation.
- [Expedia Group, Inc. Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm) — Expedia Group, 2026: hotel occupancy tax lawsuits and the company's position on who owes the tax.
- [Areas where tax collection and remittance by Airbnb is available](https://www.airbnb.com/help/article/2509) — Airbnb Help Center, n.d. (fetched October 2026): 72 collect-and-remit locations; host responsibility elsewhere.
- [Occupancy tax collection and remittance by Airbnb in Portugal](https://www.airbnb.com/help/article/2290) — Airbnb Help Center, n.d. (fetched October 2026): Airbnb collects and remits the Lisbon tourist tax.
- [Rebuilding Payment Orchestration at Airbnb](https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b) — Bryon Ross et al., Airbnb Engineering, 2022: alterations modeled as new versions of a plan, the idea reused here for tax determinations.

*Standards, regulation and documentation*

- [Council Directive 2006/112/EC (VAT Directive)](http://publications.europa.eu/resource/celex/32006L0112) — Council of the EU, 2006: Article 306, the special scheme for travel agents.
- [Council Directive 2008/8/EC (place of supply of services)](http://publications.europa.eu/resource/celex/32008L0008) — Council of the EU, 2008: Articles 44, 46 and 47.
- [Council Directive (EU) 2025/516 (VAT in the Digital Age)](http://publications.europa.eu/resource/celex/32025L0516) — Council of the EU, 2025: Article 28a deemed supplier for short-term accommodation, Article 46a, dates 2028–2030, member-state options.
- [Council Directive (EU) 2021/514 (DAC7)](http://publications.europa.eu/resource/celex/32021L0514) — Council of the EU, 2021: reportable and excluded sellers, property listing, consideration, data items, the two-reminder and 60-day enforcement rule.
- [Judgment in Case C-552/17, Alpenchalets Resorts](http://publications.europa.eu/resource/celex/62017CJ0552) — Court of Justice of the EU, 2018: resale of accommodation under the travel-agent scheme, no reduced rate.
- [Aviso n.º 18684/2024/2: Alteração ao Regulamento Geral de Taxas, Preços e Outras Receitas do Município de Lisboa](https://dados.gov.pt/api/1/datasets/r/d8ea0fd2-6762-4abf-8d8f-3ce6390f34d6) — Município de Lisboa, Diário da República, 2.ª série, n.º 164, 26 August 2024: Lisbon tourist tax of €4.00 per guest per night from 1 September 2024, maximum 7 nights per stay (art. 70.º), guests under 13 exempt (art. 71.º).
- [Código do IVA, artigo 18.º](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva18.aspx) — Autoridade Tributária e Aduaneira, Portal das Finanças (consolidated text, fetched 22 October 2026): mainland rates of 6% (Lista I), 13% (Lista II) and 23% (standard).
- [Código do IVA, Lista I, verba 2.17](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/c-iva-listas.aspx) — Autoridade Tributária e Aduaneira, Portal das Finanças (fetched 22 October 2026): the 6% rate for "alojamento em estabelecimentos do tipo hoteleiro".
- [Informação vinculativa, processo 29462](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/informacoes_vinculativas/despesa/civa/Documents/PIV_29462.pdf) — Autoridade Tributária e Aduaneira, 2026 (despacho of 27 March 2026): verba 2.17 covers *alojamento local*, and a cleaning fee included in the stay follows the 6% rate.
- [IRS issues FAQs on Form 1099-K threshold under the One, Big, Beautiful Bill](https://irs.gov/newsroom/irs-issues-faqs-on-form-1099-k-threshold-under-the-one-big-beautiful-bill-dollar-limit-reverts-to-20000) — Internal Revenue Service, 2025: $20,000 and 200-transaction threshold.
- [FTC announces bipartisan rule banning junk ticket and hotel fees](https://www.ftc.gov/news-events/news/press-releases/2024/12/federal-trade-commission-announces-bipartisan-rule-banning-junk-ticket-hotel-fees) — US Federal Trade Commission, 2024: total price for short-term lodging; taxes may be shown separately if disclosed before payment.

*Research and practitioner sources*

- [Verlaagd btw-tarief voor logies vervalt per 1 januari 2026](https://www.grantthornton.nl/insights/tax/verlaagd-btw-tarief-voor-logies-vervalt-per-1-januari-2026/) — Grant Thornton Netherlands, 2025: Dutch accommodation VAT moving from 9% to 21%.
- [Amsterdam may raise tourist tax to curb mass tourism](https://nltimes.nl/2025/11/28/amsterdam-may-raise-tourist-tax-curb-mass-tourism) — NL Times, 2025: Amsterdam's 12.5% tourist tax and the proposed increase.
- [Amsterdam proposes tourism tax hike to 20%](https://skift.com/2026/06/05/amsterdam-proposes-tourism-tax-hike-to-20/) — Skift, 2026: the stepwise proposal from 2027.
- [Tourist tax in France](https://www.hostaway.com/vacation-rental-guide/tourist-tax/france/) — Hostaway, 2026: taxe de séjour structure for unclassified furnished rentals (secondary source; verify against municipal deliberations).

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
