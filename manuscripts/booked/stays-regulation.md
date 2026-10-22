{id: stays-regulation}
# 36. Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law

![Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law — logo](stays-marketplace-architecture/posts/36-stays-regulation/assets/images/36-stays-regulation/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Map the rules that reach into a stays platform's systems: the EU Short-Term Rental Regulation, national and city rules, the Digital Services Act (DSA), the Digital Markets Act (DMA), platform-to-business and consumer law, data protection, payments, accessibility and AI law. Then design the machinery that turns them into requirements: a market policy registry, enforcement points, an evidence trail and a regulator gateway.

> **WHY THE BUSINESS CARES:** In many European cities, short-term-rental rules now decide which homes may be sold, which nights may be sold and what must be reported every month. A removal that is slow costs fines and political standing; a removal that is wrong costs hosts, guests and revenue. Both happen when compliance is a spreadsheet.

> **WHY ARCHITECTS SHOULD CARE:** Regulation changes faster than code and is sometimes reversed by a court. If each rule is coded into the listing wizard, checkout and a reporting script, every change is an emergency project. If rules are versioned data evaluated at a few known points, a new city rule becomes a content change and a court ruling becomes a query.

> **KEY POINTS:**
>
> * **A rule is data with a legal source, an effective period and an owner.** Registration areas, number formats, validating registers, night caps and reporting duties belong in a versioned market policy registry, not in code. Spain's national registry went from mandatory to annulled within eleven months, and only a platform that recorded which rule each decision used could undo the decisions that rested on it.
> * **Compliance by design means a few enforcement points and one evidence trail.** Check rules when a listing is published, when a stay is booked and in scheduled sweeps, and report from the same records. Store every decision with its rule version and reason code, because the DSA, the Platform-to-Business Regulation and short-term-rental law all require the platform to explain restrictions to the person affected.
> * **Most hotels sit outside short-term-rental law and most homes sit inside it, and the boundary runs through the online travel agency (OTA).** A hosted-stays platform has the rule engine on the critical path for almost every listing. An OTA needs a per-unit legal classification for its apartments and holiday homes. The registry, evidence store and regulator gateway can be shared across brands; the enforcement points stay with each marketplace.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **City-by-City Firefighting** — each registration regime, night cap and removal order is handled as a one-off project, so the platform is late every time and nothing carries over to the next city.
> * **The Hotel-Shaped Home** — an OTA that models apartments as hotel room types cannot name the unit that the law regulates, so it cannot validate, display or report per unit.
> * **Policy Spaghetti** — what happens to existing reservations when a listing loses its right to be sold is decided separately in trust tools, support scripts and checkout, and gives guests different answers.

Most regulation that reaches an accommodation marketplace used to be someone else's problem. Hotels hold licenses, collect city tax at the desk and register guests for the police; the OTA displayed what the hotel told it. Homes changed that. When individuals and small managers sell nights in apartments, **the platform is the only party that sees every listing, every booking and every night**, and regulators have made it the place where rules are checked and data is collected.

The obligations land on different parts of the system. Short-term-rental law reaches the listing and the calendar; platform law reaches moderation, ranking and partner terms; consumer law reaches the price on the screen; data, payments, accessibility and AI law reach almost everything. Each arrives with its own dates, authority and idea of what "the platform" must do.

This chapter closes Part VII ([Part VII — TRUST: Making Strangers Safe to Stay With](#part-7)). It owns three concepts: **STR registration** (STR: short-term rental; the duty to collect, display, check and report a unit's short-term-rental registration number), the **market policy registry** (the versioned store of jurisdiction rules that other systems evaluate) and **compliance by design for stays** (rules enforced at fixed points with evidence). Neighboring chapters own individual duties: trader verification ([From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding)), price display ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection)), ranking transparency ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)), statements of reasons ([Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety)), review law ([Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation)) and tax reporting ([The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)). Here they meet as one map and one architecture.

{id: stays-regulation--setting-the-scene-at-corvane-6-900-listings-and-a-spreadsheet}
## Setting the Scene at Corvane: 6,900 Listings and a Spreadsheet

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), learned its regulatory architecture from a removal it ran in early 2026 and had to partly undo a few months later.

Spain's Royal Decree 1312/2024 of 23 December 2024 created a national single registry for short-term rentals and a digital single window for platform data, with effect from **1 July 2025** ([BOE, Real Decreto 1312/2024](https://www.boe.es/buscar/act.php?id=BOE-A-2024-26931), 2024). Platforms were expected to show a national number on each listing, on top of the regional tourist-housing numbers that Spain's autonomous communities already issued, and authorities pursued unregistered listings on other platforms in 2025 (see "In Practice"). Nookaway had collected Spanish numbers as free text since 2019 and never checked them against a register ([From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding)).

Between **9 February and 24 April 2026**, Noor van Dijk, Head of Regulatory Affairs and Privacy, ran a removal in three waves. Analysts compared the numbers in a spreadsheet export against regional open-data registers and, by hand, the national registry, marked rows "INVALID", and engineering deactivated them with a bulk script: **6,900** listings. Their future reservations went to a support playbook: **2,900** with check-in within 30 days were honored, and **8,300** later ones were canceled with full refunds. At Nookaway's averages (3.5 nights at €142), those cancellations removed about €4.1 million of booking value and roughly €660,000 of guest and host fees. That is an estimate, not a ledger figure.

Four weeks later the law moved. In a judgment announced on **21 May 2026** (judgment 620/2026), Spain's Supreme Court annulled the provisions that created the national registry, holding that the State lacked competence for a national registry layered on top of the regional ones. It upheld the digital single window, the platforms' data-transmission duties and statistical reporting ([CGPJ press note](https://www.poderjudicial.es/cgpj/es/Poder-Judicial/Tribunal-Supremo/Noticias-Judiciales/El-Tribunal-Supremo-anula-el-Registro-Unico-de-arrendamientos-de-corta-duracion-por-considerar-que-el-Estado-carece-de-competencia-para-su-creacion), 2026). The consolidated decree in the official gazette now marks Article 10, on verifying the registration number, as annulled, citing Supreme Court judgments of 19 May, 21 May and 1 June 2026 ([BOE consolidated text](https://www.boe.es/buscar/act.php?id=BOE-A-2024-26931), updated July 2026). Regional registration numbers still apply.

Hosts whose only fault was the missing national number asked to come back, and on counsel's advice Noor's team agreed to reinstate listings with a valid regional number. (This book takes no view on Spanish law.) The engineering question was **which of the 6,900 listings had been removed for that reason**, and the spreadsheet, with one status column and no reason, rule or source, could not answer it. Nine analysts spent seven weeks rechecking every row. They found **1,240** listings removed only for the national number, and **870** were live again by the end of August 2026. The rest had left, or moved to other platforms. Of the 8,300 canceled reservations, **1,510** had been on those 1,240 listings.

When Mariana Costa joined as Group Chief Architect in January 2027, she asked Noor for the list of obligations the group had to meet. It was a spreadsheet of **387** rows covering 33 countries. Only **61** rows named the system that enforced the obligation, and none named the record that proved it had been met. In April 2027, Roomstead could not produce the unit-level monthly feed the EU Short-Term Rental Regulation expects ([Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model)). Mariana's question to the architecture forum was the one this chapter answers: **how does a rule written by a legislature, a city or a court become a system requirement once, with evidence, instead of an emergency every time it changes?**

{id: stays-regulation--concepts-from-legal-text-to-enforced-rule}
## Concepts: From Legal Text to Enforced Rule

Six terms carry the rest of the chapter.

- **Obligation.** One duty from one legal source, stated so that an engineer can test it: "before a unit in a listed area is offered, the host must have provided a registration number" (Regulation (EU) 2024/1028, Article 7(1)(b)). It has a source, an authority, an effective period, a scope and an owner.
- **Control.** The system behavior that meets an obligation: a publish gate, a booking-time check, a sweep, a disclosure or a report. One control can serve several obligations.
- **Rule.** The machine-readable part of an obligation for one jurisdiction: "units in Seville province require an Andalusian registration number of this format, validated against this register, from this date." Rules change most often.
- **Market policy registry.** The versioned store of rules, keyed by jurisdiction and supply type, with legal sources and effective dates. Other systems evaluate its rules; the registry makes no decisions.
- **Enforcement point.** A place in a business flow where rules are evaluated: publish, quote or book, a scheduled sweep, a report run, an authority's order.
- **Evidence.** The record that a control ran: which unit, rule version, inputs, result, notice and receipt. Evidence lets a platform answer an authority in an afternoon rather than in seven weeks.

**STR registration** is the bundle of duties around a unit's registration number. In the EU text, a **unit** is furnished accommodation in the Union rented short term. It excludes hotels and similar accommodation (group 55.1 of NACE, the EU classification of economic activities), hostels and campsites. A **registration number** is "a unique identifier issued by the competent authority which identifies a unit in that Member State" ([Regulation (EU) 2024/1028, Art. 3](http://publications.europa.eu/resource/celex/32024R1028), 2024). **Activity data** is the number of nights a unit is rented and the number of guests per night, "along with the country of residence of each guest". A **single digital entry point** (SDEP) is the national interface where platforms send that data and check numbers.

{id: stays-regulation--the-regulatory-map}
## The Regulatory Map

The subsections after the table explain the rows that most change architecture. Dates are dates of application; check each row's current status before acting on it.

| Instrument | Applies from | What it requires of a stays platform | System requirement | Owning chapter |
| --- | --- | --- | --- | --- |
| **EU Short-Term Rental Regulation**, (EU) 2024/1028 | 20 May 2026 | Host self-declaration; registration number before offering, displayed; random checks; act on removal orders; monthly activity data per unit | Registration gate, validator adapters, order intake, SDEP reporting | This chapter |
| **National and city rules** (registration, night caps, zones, license expiry) | Varies | Whatever the jurisdiction decides, within EU law | Rule primitives in the registry; jurisdiction resolution | This chapter; [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps) |
| **Digital Services Act**, (EU) 2022/2065 | 17 February 2024 | Notice and action, statements of reasons, internal complaints, trader traceability, compliance by design, transparency reporting; more for very large platforms | Case workflow, reason codes, trader records, transparency database feed | [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety), [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding) |
| **Digital Markets Act**, (EU) 2022/1925 | Gatekeepers only (Booking since 13 May 2024) | No parity clauses or equivalent measures; business-user data access | Ranking feature limits; partner data export | [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) |
| **Platform-to-Business Regulation**, (EU) 2019/1150 | 12 July 2020 | Terms explaining restrictions and ranking; statement of reasons for restriction; 30 days' notice for termination; complaint handling | Partner notices, terms versioning, partner complaint queue | [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking), [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools) |
| **Consumer law** (Unfair Commercial Practices and Consumer Rights Directives, as amended by Omnibus Directive (EU) 2019/2161) | 28 May 2022 (Omnibus) | Total price; trader or non-trader status; ranking parameters; review verification disclosure | Display policy, trader flag on listing, ranking page | [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection), [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation) |
| **General Data Protection Regulation (GDPR)**, (EU) 2016/679 | 25 May 2018 | Minimization, storage limits, special-category limits, rights on automated decisions | Purpose-tagged fields, retention jobs, human review paths | [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) |
| **Guest registration for police** (for example Spain's Royal Decree 933/2021) | National | Record and communicate guest identity data | Property-side duty that platforms may support | This chapter |
| **Second Payment Services Directive (PSD2)**, (EU) 2015/2366 | 13 January 2018 | Licensing when holding funds for others; strong customer authentication (SCA) | Payment entity design, SCA flows | [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models), [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments) |
| **European Accessibility Act**, (EU) 2019/882 | 28 June 2025 | Accessible e-commerce services | Accessible web, apps and checkout | [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) |
| **AI Act**, (EU) 2024/1689, as amended by the 2026 AI Omnibus | Staged 2025–2028 | AI literacy, transparency for systems that talk to people; high-risk duties only for listed uses | AI system inventory, disclosure in assistants | [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform) |
| **DAC7** (platform reporting) and **ViDA** (VAT in the Digital Age) | 2023; 2028–2030 | Seller reporting; deemed VAT supplier for short-term accommodation | Tax party registry, reporting pipeline | [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays) |

{id: stays-regulation--short-term-rental-law-the-eu-regulation}
### Short-term-rental law: the EU Regulation

The EU Short-Term Rental Regulation applies from **20 May 2026** ([Regulation (EU) 2024/1028](http://publications.europa.eu/resource/celex/32024R1028), 2024). It does not decide whether short-term renting is allowed anywhere; that stays with national, regional and local rules (Article 2(2)). What it harmonizes is the data: how registration works where a Member State requires it, and what platforms must collect and send. Five provisions shape systems.

1. **Registration on the host's declaration (Articles 4 and 5).** Registration must be online, allow "the automatic and immediate issue of a registration number" without personal data in it, and come with technical means "to assess the validity of registration numbers". Registration becomes a lookup the platform can make, not a document it inspects.
2. **Compliance by design (Articles 7 and 8).** The interface must make hosts self-declare whether the unit is in a registration area, ensure a number is provided **before** the unit is offered, and display it. The platform must "make reasonable efforts to randomly check on a regular basis" declarations and numbers through the SDEP, and tell the authority and host "without undue delay" about invalid numbers or misuse. Article 8 adds a best-efforts automated check of the declaration against the Member State's list of registration areas.
3. **Orders (Article 6).** Authorities may suspend or withdraw numbers and order platforms to "remove, or to disable access to" listings "without undue delay". An order must carry a statement of reasons and enough to identify the listing, such as its URL.
4. **Monthly reporting (Article 9).** For units in areas where authorities have requested data, the platform must collect activity data and send it monthly to the SDEP "by machine-to-machine communication means", together with the registration number, the unit's specific address and the listing URL. Small or micro platforms with fewer than 4,250 listings a month on average may report quarterly. Article 9(3) makes the platform responsible for complete and accurate datasets, "based on the information provided by the hosts".
5. **Lists (Article 13).** Each Member State publishes two lists through its SDEP: areas where registration applies, and areas where data has been requested. These lists are the inputs to the platform's jurisdiction rules, and they change.

The DSA's enforcement regime covers Articles 7(1) and 8; national authorities enforce the rest, with penalties due by 20 May 2026 (Article 15). By 20 May 2031 the Commission must evaluate whether one EU-level SDEP should replace the national ones (Article 18): design for that possibility without depending on it.

{id: stays-regulation--national-and-city-rules}
### National and city rules

Whether a night may be sold at all is decided locally, and those rules change often. Documented examples show the range:

| Place | Rule (as documented) | Rule primitive |
| --- | --- | --- |
| Spain | National registry from 1 July 2025 under Royal Decree 1312/2024; registry annulled by the Supreme Court in May 2026; regional numbers and data transmission remain | Registration required, validating register, effective period |
| Barcelona | About 10,000 tourist-apartment licenses not renewed from November 2028; Constitutional Court upheld the Catalan decree in March 2025 ([Catalan News](https://www.catalannews.com/society-science/item/barcelona-mayor-welcomes-constitutional-court-ruling-on-tourist-apartment-restrictions), 2025) | License expiry by zone |
| Amsterdam | Entire homes at most 30 nights a year; registration number and permit; host notifies the city before each rental; the city can ask the platform to block the calendar for the rest of the year ([Airbnb Help Center, article 860](https://www.airbnb.com/help/article/860), n.d., fetched October 2026) | Night cap per unit; authority-requested calendar block |
| France | A 13-character registration number shown on every listing ([Service-Public.fr](https://www.service-public.gouv.fr/particuliers/vosdroits/F2043), 2026); Paris reduced its primary-residence cap from 120 to 90 nights from 1 January 2025 ([Houst](https://www.houst.com/blog/reglementation-airbnb-paris), 2025, secondary) | Number format; night cap |
| New York City | Local Law 18: hosts register with the city; platforms may not process transactions for unregistered rentals and must use the city's verification system, enforced from 5 September 2023 ([NYC Office of Special Enforcement](https://www.nyc.gov/site/specialenforcement/registration-law/registration.page), n.d., fetched October 2026) | Check before payment |

The pattern matters more than the cases. **About ten rule primitives cover nearly every regime** I have seen: registration required; number format; validating register; night cap per unit per year; minimum stay; maximum guests; prohibited buildings or zones; license expiry; check before payment; authority-requested block or removal; and a reporting duty. A platform that models these primitives, with parameters per jurisdiction, can add a city by adding data. A platform that writes code per city is doing City-by-City Firefighting.

![A shelf of six standard rule blocks, reused in different combinations to build three different city skylines.](stays-marketplace-architecture/posts/36-stays-regulation/assets/images/36-stays-regulation/36-ten-primitives.jpeg)

**Figure 1:** *About ten rule primitives cover nearly every regime, so a platform that models them can add a city by adding data instead of writing code for each city.*

Night caps need care. A cap counts nights **across all platforms and direct bookings**, and a platform sees only its own. That is why Amsterdam makes hosts notify the city and lets the city ask platforms to block calendars. A platform can count its own nights, warn, honor a block and report; it cannot prove a host stayed under a cap ([One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync)).

{id: stays-regulation--platform-law-dsa-dma-and-p2b}
### Platform law: DSA, DMA and P2B

The **Digital Services Act** applies from 17 February 2024 ([Regulation (EU) 2022/2065, Art. 93](http://publications.europa.eu/resource/celex/32022R2065), 2022). For a stays marketplace, the duties that change systems are:

- **Notice and action (Art. 16)** and **authority orders (Art. 9).** Anyone can notify illegal content electronically. Orders from authorities must identify the content, for example by exact URL, and the platform must report back what effect it gave them.
- **Statement of reasons (Art. 17)** for removal, demotion, payment suspension or account suspension imposed because content is illegal or breaches the terms. Each statement also goes, without personal data, to the Commission's public database (Art. 24(5)).
- **Internal complaints (Art. 20)** for at least six months after a decision.
- **Trader traceability (Art. 30)** and **compliance by design (Art. 31)** for marketplaces where consumers contract with traders ([From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding)).
- **Right to information (Art. 32).** When the platform learns that an illegal service was sold, it must tell consumers who bought it in the previous six months, giving the trader's identity and means of redress. A home sold without a required registration number may count, and the purchasers are the guests on its reservations.

The online-platform and marketplace duties from Article 20 onward do not apply to micro or small enterprises (Arts. 19 and 29). Platforms with 45 million or more average monthly active recipients in the EU are **very large online platforms** (VLOPs) with risk assessments, audits and a non-profiling recommender option (Art. 33 onward). Booking.com has been a VLOP since 25 April 2023 and publishes its DSA reports ([Booking.com, DSA page](https://www.booking.com/content/dsa.html), 2026). Corvane's brands are below the threshold: Roomstead had about 30 million EU recipients in the first half of 2027 ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)).

The **Digital Markets Act** applies only to gatekeepers; Booking was designated for Booking.com on 13 May 2024 ([European Commission](https://digital-markets-act.ec.europa.eu/gatekeepers_en), live 2026), and Article 5(3) bans parity clauses and equivalent measures ([Regulation (EU) 2022/1925](http://publications.europa.eu/resource/celex/32022R1925), 2022). For everyone else, the Court of Justice held in Case C-264/23 (19 September 2024) that wide and narrow parity clauses with hotels are not ancillary restraints ([CJEU](http://publications.europa.eu/resource/celex/62023CJ0264), 2024). [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) covers the consequences for ranking.

The **Platform-to-Business (P2B) Regulation** applies from 12 July 2020 and protects business users: hotels, property managers and professional hosts ([Regulation (EU) 2019/1150](http://publications.europa.eu/resource/celex/32019R1150), 2019). Terms changes need at least 15 days' notice (Art. 3). Restricting a business user's offers needs a statement of reasons "prior to or at the time" it takes effect, and terminating the whole service needs 30 days' notice unless a legal obligation prevents it (Art. 4); a complaint system is required (Art. 11). One removal can owe a professional host both a P2B and a DSA statement, and one notice generator fed by reason codes can produce both.

{id: stays-regulation--consumer-law}
### Consumer law

The Omnibus Directive, applied from 28 May 2022, added duties for online marketplaces: show the main ranking parameters, and **whether the party offering the service is a trader** based on that party's declaration, with a statement that consumer rights do not apply when it is not. It also set fines for widespread infringements of at least 4% of annual turnover in the Member States concerned ([Directive (EU) 2019/2161](http://publications.europa.eu/resource/celex/32019L2161), 2019). Coordinated consumer actions reached both models: Airbnb committed by July 2019 to show total prices and to distinguish professional from private hosts; Booking.com (2019) and Expedia Group (2020) committed to change how they presented prices and offers ([European Commission](https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/accommodation-booking_en), n.d.). In the US, the Federal Trade Commission's fees rule has required short-term lodging to show the total price since 12 May 2025 ([FTC](https://www.ftc.gov/news-events/news/press-releases/2024/12/federal-trade-commission-announces-bipartisan-rule-banning-junk-ticket-hotel-fees), 2024). Price display belongs to [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) and review law to [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation). The new data item here is the trader flag: captured at onboarding, stored on the listing, shown on the listing page.

{id: stays-regulation--data-payments-accessibility-and-ai}
### Data, payments, accessibility and AI

**GDPR** ([Regulation (EU) 2016/679](http://publications.europa.eu/resource/celex/32016R0679), 2016) adds three points to regulation-driven data. The STR Regulation makes **guest country of residence** a new data item, and minimization (Art. 5(1)(c)) says to collect it only where a report needs it and keep it only until the report is settled. Face matching used to identify a person is special-category biometric data (Art. 9; see [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access)). And a fully automated decision with significant effects triggers the safeguards of Art. 22, so the machinery in this chapter needs a human review path.

**Guest registration for the police** is a property-side duty in many Schengen states that sometimes reaches platforms: Spain's Royal Decree 933/2021 lists digital platforms intermediating lodging among the parties that must record guest data, kept for three years ([BOE, Real Decreto 933/2021](https://www.boe.es/buscar/act.php?id=BOE-A-2021-17461), 2021). Collect only what a law names, for the party it names.

**PSD2** decides whether a platform that collects guest money needs a payment license: its commercial-agent exclusion covers agents acting for "only the payer or only the payee" ([Directive (EU) 2015/2366, Art. 3(b)](http://publications.europa.eu/resource/celex/32015L2366), 2015), which is why Corvane Payments is a licensed institution ([Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models)). The **European Accessibility Act** covers e-commerce services from 28 June 2025 and exempts microenterprises providing services ([Directive (EU) 2019/882](http://publications.europa.eu/resource/celex/32019L0882), 2019); the platform's booking flow is in scope even when its hosts are tiny.

The **AI Act** applies in stages: prohibitions and AI literacy from 2 February 2025, general-purpose model duties from 2 August 2025, most other provisions from 2 August 2026 ([Regulation (EU) 2024/1689, Art. 113](http://publications.europa.eu/resource/celex/32024R1689), 2024). The AI Omnibus, in force since 27 July 2026, moved the Annex III high-risk rules to **2 December 2027** ([European Commission](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force), 2026). For stays the live duty is Article 50: a support assistant must tell people they are talking to an AI unless that is obvious. Ranking and pricing are not on the Annex III list, which also excludes biometric verification that only confirms a claimed identity and excludes fraud detection from its creditworthiness category. My reading is that most stays systems are not high-risk; the work is an inventory of AI systems, disclosure in assistants and a check that nothing drifts into a listed use.

{id: stays-regulation--architecture-compliance-by-design-for-stays}
## Architecture: Compliance by Design for Stays

The architecture's job: a rule enters once, reaches every place it applies, and every decision it causes can be explained and replayed (Figure 2).

![A U-shaped chain: laws and rulings to the obligation register, policy registry and eligibility evaluator, then down to enforcement points, the evidence store and the regulator gateway, which sends reports to authorities and receives orders.](stays-marketplace-architecture/posts/36-stays-regulation/assets/images/36-stays-regulation/36-compliance-by-design.jpeg)

**Figure 2:** *A rule enters once, through the obligation register, and becomes versioned data that one evaluator applies at every enforcement point. Decisions land in an evidence store, which also feeds the regulator gateway, so the platform reports from the same records it enforced.*

**The obligation register** is the legal team's tool and the piece most platforms skip. Each row is one obligation with its source, effective period, authority, scope, the controls that implement it, each control's owner and the evidence that proves it ran. Noor's spreadsheet lacked the last three columns, and those are what turn a list of laws into system requirements.

**The policy authoring workspace** is where regulatory analysts write rules. It needs a form per rule primitive, so analysts set parameters rather than write code; a mandatory legal source; a **dry run** that lists the units a change would affect before it goes live; and two-person approval. The dry run matters most: "this rule makes 1,240 Spanish listings eligible again" is a sentence a regulatory lead can sign, and a code diff is not.

**The market policy registry** stores rules as effective-dated versions. A rule version records:

| Field | Example | Why it exists |
| --- | --- | --- |
| Rule ID and version | `es-and-vut-v3` | Every decision cites it |
| Jurisdiction | Andalusia, Spain (region) | Scope, resolved from the unit's location |
| Supply scope | Units under Regulation (EU) 2024/1028; excludes hotels and similar | Hotels and homes differ |
| Primitive and parameters | Registration required; format pattern; validating register | Evaluated without code changes |
| Effective period | From 2025-07-01; to open | Decisions are reproducible later |
| Enforcement points | Publish (blocking), random check monthly, report | Where the rule applies |
| Failure behavior | Fail closed at publish; fail open at booking if register unreachable | Known in advance, not decided during an outage |
| Transition policy | Existing reservations within 30 days honored | What happens to bookings already made |
| Legal source | Andalusian decree reference; Regulation (EU) 2024/1028 Art. 7 | Audit and expiry |
| Owner and approvers | Regulatory analyst, Spain; legal counsel | Accountability |

Two fields deserve emphasis. **The transition policy belongs to the rule**, because what happens to reservations already made is a legal and commercial decision that varies by jurisdiction and reason; in a support playbook it becomes Policy Spaghetti. **The effective period can be closed retroactively** by a court: the registry must record "this version stopped applying on 21 May 2026" after the fact, and the evaluator must find every decision that cited it.

**The jurisdiction resolver** maps a unit's exact location to the areas that matter: country, region, municipality, registration area, data-request area and any special zone. It runs at write time and stores the jurisdictions on the unit, with the version of the boundaries used ([Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model), [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps)). Article 13 lists change, so a new list version must trigger re-resolution of the affected units, not wait for the next host edit.

**The eligibility evaluator** is a stateless service with one question: may this unit be offered, booked or kept live here, on these dates, under current rules, and if not, why? Its answer carries the decision, the rule versions, the inputs (number, validation result and its age, nights counted) and a **reason code** from a controlled list. The readiness service of [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding) treats it as one readiness check among several.

**The evidence store** is append-only: decisions, validation results, notices, orders, reports and receipts, with references to personal data rather than copies. Statements of reasons, transparency reports and answers to authorities are read from it.

**The regulator gateway** is the integration with authorities, run as a product with service levels rather than a folder of scripts. Outbound it sends SDEP reports, order confirmations and statements of reasons to the DSA database; inbound it takes orders, Article 13 list updates and validity lookups, and opens cases. Each SDEP is an adapter behind one internal interface: the Commission sets technical requirements for the APIs, but adapters make national variants survivable.

{id: stays-regulation--four-enforcement-points}
### Four enforcement points

| Point | When | Typical rules | If the check fails | If the check cannot run |
| --- | --- | --- | --- | --- |
| **Publish** | Listing created, address or type changed, rule changes | Registration required and valid; zone allowed; license in force | Listing stays unpublished, with the reason shown to the host | Fail closed: a legal gate does not open on missing data |
| **Book** | Quote and booking | Night cap remaining; minimum stay; guest limit; check before payment where required | Dates not bookable; reason in the quote | Usually fail open with a sweep afterwards; fail closed where the law puts the check on the transaction, as in New York |
| **Sweep** | Scheduled, and on rule or list change | Random validity checks; license expiry; changed boundaries | Suspension with notice to host and authority; transition policy applied | Retry; escalate when overdue |
| **Report** | Monthly, quarterly, on request | Activity data, DAC7, transparency reports | Rejected rows go to a correction queue | Retry with receipts; alert before the deadline |

The report point is enforcement in reverse: it proves to the authority what the other three did.

{id: stays-regulation--when-eligibility-is-lost}
### When eligibility is lost

A listing that loses eligibility has future reservations, collected money and a host who is owed an explanation. Figure 3 follows an authority's removal order through the system.

![Swimlanes for authority, regulator gateway, evaluator, listing, reservations and notices: a removal order becomes an authority block, the unit is made ineligible, the transition policy is applied to reservations, notices go out and the authority receives confirmation.](stays-marketplace-architecture/posts/36-stays-regulation/assets/images/36-stays-regulation/36-removal-order.jpeg)

**Figure 3:** *A removal order is a case with a clock, not a bulk script. One reason code drives the listing, the reservations, the host's statement of reasons, the guests' notices and the confirmation to the authority, so all five say the same thing.*

The transition policy is a business decision with legal limits: honor everything, honor within a window (Nookaway's 30 days in 2026), cancel with refunds, or rehouse the guest at the platform's cost. An authority order to disable access "without undue delay" may not allow honoring later stays; a platform-initiated cleanup usually does. Whatever the choice, the policy is part of the rule version, each reservation records which policy was applied, and guests get a reason they can act on, including the redress information DSA Article 32 requires when the service was illegal. [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) owns the refund mechanics.

{id: stays-regulation--in-practice}
## In Practice

{id: stays-regulation--what-the-public-record-shows}
### What the public record shows

Public sources show the pressure, not the internals. No company has published the design of its compliance systems in the sources checked for this book.

- **Airbnb in Spain.** Airbnb's annual report for 2025 says that in 2025 "the Spanish Ministry of Consumer Affairs proposed to assess a fine of approximately 65 million Euro ($76 million) in connection with alleged non-compliance with short-term rental listing regulations in Spain". It also says, about regulatory disputes generally, "We have resolved some disputes by agreeing to remove listings or share data with authorities" ([Airbnb Form 10-K](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), 2026). The press reported that Airbnb removed nearly 65,000 Spanish listings at the ministry's request in 2025 ([Catalan News](https://www.catalannews.com/housing-crisis/item/airbnb-removes-almost-65000-illegal-listings-at-request-of-spains-consumer-affairs-ministry), 2025). Both point to removals at a scale no spreadsheet handles well.
- **Government data portals.** In 2021 Airbnb reported that more than 100 local and national governments and destination organizations used its City Portal ([Airbnb newsroom](https://news.airbnb.com/building-on-our-commitment-to-trust-2), 2021). The source is five years old and the current state is not public, but a self-service regulator interface clearly predates the EU Regulation.
- **Regulation travels through connectivity.** Booking.com's connectivity documentation lists a Licences API beside its content and rates APIs ([Booking.com developers](https://developers.booking.com/connectivity/docs), n.d., live 2026). Expedia Group's lodging supply hub lists a compliance API for "regulatory information for integrated properties" ([Expedia Group developers](https://developers.expediagroup.com/supply/lodging), n.d., live 2026). For managed homes, numbers arrive through software, not forms ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers)).
- **The VLOP and gatekeeper regimes in operation.** Booking.com publishes DSA transparency reports and an ad repository ([Booking.com DSA page](https://www.booking.com/content/dsa.html), 2026), and its annual report for 2025 describes changes for the DMA ban on parity arrangements and a DMA compliance function ([Booking Holdings Form 10-K](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), 2026).
- **Ranking features as regulated choices.** In July 2024 Spain's competition authority fined Booking.com €413.24 million. Among the conduct it cited were a ranking factor based on total bookings and program eligibility based on the hotel's profitability for Booking.com. The fine was suspended pending appeal, as reported in March 2025 ([TechCrunch](https://techcrunch.com/2024/07/30/spains-antitrust-watchdog-fines-booking-com-nearly-450m-for-unfair-terms-and-restricting-rivals), 2024; [Hosteltur](https://www.hosteltur.com/168767_la-audiencia-nacional-paraliza-la-multa-millonaria-de-la-cnmc-a-booking.html), 2025). Feature choices in ranking now have legal owners ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)).

> **INFERENCE, NOT DOCUMENTED:** Platforms that remove tens of thousands of listings from government lists, share data with authorities and expose license fields in partner APIs plausibly run something like the registry, evaluator and gateway described above. None of the companies named has published such a design, and this chapter does not describe their systems.

{id: stays-regulation--corvane-ordinance}
### Corvane: Ordinance

On **17 March 2027** Corvane's architecture forum approved **Ordinance**, the group market policy registry and eligibility evaluator, as part of the One Stay program. The decisions:

- **Ownership.** Noor van Dijk's team owns the obligation register and rule content: eleven country analysts, with legal counsel as approvers. A group compliance-platform team of nine engineers in Lisbon owns the registry, evaluator, evidence store and regulator gateway. The brands own their enforcement points: Nookaway calls the evaluator from Burrow's listing flow, checkout and Almanac sweeps; Roomstead from Keystone's property flow, the Partner Hub and Switchyard, its connectivity gateway.
- **Scope.** Short-term-rental rules first, then DSA and P2B notice templates. Display rules stay in the display policy service of [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) and tax rules in Levy ([The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)); all three read jurisdictions from the place registry.
- **Sequence.** Spain and Portugal went live in **May 2027**, Nookaway first. A random check under rule `es-and-vut-v3` suspended its first listing on 14 May 2027 ([From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding)). Italy, France, Greece and the Netherlands followed in the third quarter. The regulator gateway took over SDEP reporting and order intake in **September 2027**. Roomstead's unit-level reports depend on its multi-unit pools naming units, which is targeted at 95% of reservations by the end of the first quarter of 2028 ([Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model)).

**The replay.** Ordinance's first test was to replay the 2026 Spanish removal against the rules as they stood then. With rules entered for the national registry (`es-nru-v1`, effective 1 July 2025) and each regional register, the evaluator classified the 6,900 listings in under an hour:

| Reason code | Listings | Rule cited |
| --- | --- | --- |
| No registration number provided | 3,180 | Regional rule and `es-nru-v1` |
| Regional number failed format or register lookup | 2,480 | Regional rule |
| Valid regional number, no national number | 1,240 | `es-nru-v1` only |
| **Total** | **6,900** | |

Closing `es-nru-v1` with an end date of 21 May 2026 and re-running the evaluator produced the 1,240 reinstatement candidates, the same set nine analysts had needed seven weeks to find. With the transition policy stored on each reservation, it also listed the 1,510 canceled reservations on those listings. On counsel's advice, Nookaway offered those guests a goodwill credit in July 2026; a registry would have let it do so in June. The lesson Mariana drew for the forum: **the hard part was never the removal; it was knowing why each removal happened.**

![Before: analysts buried in spreadsheet printouts over seven weeks. After: an evaluator machine sorting listing cards into three bins in under an hour.](stays-marketplace-architecture/posts/36-stays-regulation/assets/images/36-stays-regulation/36-weeks-versus-hour.jpeg)

**Figure 4:** *Nine analysts needed seven weeks to find the 1,240 listings removed only for the national number; Ordinance's replay, with a reason code on every decision, found them in under an hour.*

**Monthly reporting.** Figure 5 shows the report pipeline, and the table shows September 2027, the first month the gateway sent both brands' reports.

![Stayed nights, the place registry and guest country feed an activity data builder that produces a country report, sent through entry-point adapters; receipts go to the evidence store and rejections to a correction queue that feeds back into the builder.](stays-marketplace-architecture/posts/36-stays-regulation/assets/images/36-stays-regulation/36-activity-reporting.jpeg)

**Figure 5:** *Monthly activity reporting is a read model over records the platform already keeps: stayed nights from the reservation stream, the unit and its number from the place registry, and guest country from checkout. Rejections go to a correction queue with a deadline.*

| September 2027 | Nookaway | Roomstead |
| --- | --- | --- |
| Member States reported to | 9 | 9 |
| Unit rows submitted | 412,000 | 141,000 |
| Rows rejected at first submission | 2.1% | 6.8% |
| Main rejection cause | Number not matching register format after a host edit | Pooled room types with no unit assigned (reported at property level) |
| Guest country basis | Each guest's country from checkout | Booker's country for the whole party |

Guest country is a minimization choice. Until August 2027 Nookaway reported every guest under the booker's country, which the Regulation does not support: its definition of activity data asks for the country of residence "of each guest". From September 2027 checkout asks for each guest's country, only for stays in reporting areas, with the booker's country as default and no names. The per-guest field is deleted 90 days after the month's report is accepted; the aggregated row is kept five years as evidence. Roomstead adopts the flow with its unit work in 2028.

{id: stays-regulation--trade-offs}
## Trade-offs

| Choice | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| **Where rules live** | Code per market | Rule primitives in a registry | One country, few rules, early stage | Several countries or regimes that change; any platform that reports to authorities |
| **Rule language** | Fixed primitives with parameters | General rules language | Almost always: analysts can author, dry runs are simple | A rule that no primitive covers. Add a primitive rather than a language, and resist the second exception |
| **Publish-gate failure** | Fail closed | Fail open, sweep later | Legal gates the law places before offering (registration) | Advisory checks; external registers with poor uptime, where the law allows later checks |
| **Response to lost eligibility** | Disable booking, keep the page and the reservations | Remove listing and cancel | Platform-initiated cleanups; reasons the host can fix quickly | Authority orders requiring removal or disabled access; illegal services |
| **Ownership** | One group compliance platform | Per-brand compliance | Groups with several marketplaces in the same jurisdictions | Single brand, or brands in disjoint markets |
| **Content source** | Write rules in-house | License regulatory content from a vendor | Registration and caps where you hold local relationships | Long-tail jurisdictions; but keep the registry and evidence your own |

I would choose primitives over a rules language: analysts must be able to author and review rules, and a dry run is only trustworthy when the evaluator's semantics are small. A genuinely new rule type then needs an engineering change, which is acceptable because new primitives arrive a few times a year and new parameters weekly.

{id: stays-regulation--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (Roomstead) | Hosted-stays marketplace (Nookaway) |
| --- | --- | --- |
| **Supply in scope of STR law** | Alternative accommodation only (435,000 properties, many as multi-unit pools); hotels are outside the EU Regulation | Nearly every EU listing |
| **Who provides the registration number** | Property managers, often through property-management systems (PMS) and channel managers | Individual hosts in the app; managers through the partner API |
| **Data model problem** | Pooled room types cannot name the unit the law regulates; classification of B&Bs, guesthouses and aparthotels needs legal judgement | One listing is one unit, but numbers were free text and declarations unverified |
| **Where rules bite in the flow** | Property activation and connectivity messages; reporting needs unit assignment on reservations | Listing publish, instant book, calendar blocks, night caps |
| **Platform and consumer law** | P2B weighs heavily (hotels are business users with alternatives); price-presentation history; DMA for gatekeeper OTAs | Trader or non-trader flag per host; DSA notices about homes and hosts; private hosts outside P2B |
| **Failure modes** | Under-reporting pooled units; hotel-shaped records holding one license for 38 apartments | Mass removals without reasons; night caps unenforceable across channels |
| **What can be shared** | Obligation register, market policy registry, evaluator, evidence store, regulator gateway, notice generator | Same |

The judgement: **share the registry, the evaluator, the evidence and the gateway; keep the enforcement points and the classification decision with each brand.** A Spanish court ruling should be entered once for the group. But Roomstead's question ("is this a hotel or a unit, and which unit was sold?") and Nookaway's ("is this number valid, and how many nights has this home been sold?") arise at different points in different flows. A shared evaluator answers both if each brand asks at the right moment about the right unit; for Roomstead's pools, that fix sits in [Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model).

{id: stays-regulation--failure-modes}
## Failure Modes

- **Removals without reasons.** A bulk deactivation records "inactive" and nothing else. When the law changes or a host appeals, nobody can say which rule removed which listing. Corvane's seven-week reconstruction is the typical cost.
- **Rules frozen into the onboarding wizard.** The number format is validated in the front end, so a format change needs an app release and connectivity partners bypass the check. Validate in the evaluator for every channel.
- **The register as a hard dependency.** A publish gate that calls a national register synchronously goes down with the register. Cache validation results with their age, define the fail behavior per rule and let sweeps catch up.
- **Night caps counted on one channel.** The platform blocks a home after 30 of its own nights and claims compliance, though the host sold 20 more elsewhere. Count, warn, honor blocks and report; do not certify what you cannot see.
- **Reporting as a month-end script.** The report comes from a warehouse query that disagrees with the reservation system about cancellations, and rejections surface after the deadline. Report from operational events and track receipts.
- **Guest data collected "for compliance" without a law.** Passport scans and full guest lists are collected everywhere because one country requires them somewhere. Collect per jurisdiction, per purpose, with retention.
- **Notices that disagree.** The host's email, the guest's cancellation message, the support agent's script and the statement of reasons each describe the removal differently. Generate them all from the reason code.

{id: stays-regulation--the-chief-architect-s-view}
## The Chief Architect's View

**Decide ownership along the obligation chain.** Regulatory affairs owns the register and rule content and signs every rule version; a platform team owns the registry, evaluator, evidence and gateway and their service levels; each marketplace owns its enforcement points and supply classification. Without that split, every regulatory request lands on the platform team and the brands stop owning their compliance.

**Treat the regulator as a client with service levels.** Track order handling time, report acceptance rate, time from a list change to re-resolved units and time from a rule's effective date to enforcement, on the same dashboard as booking-path objectives. A missed order deadline is an incident.

**Make every rule change a reviewed release with a blast radius.** The dry run, two-person approval and an effective date are the release process. For rules that remove supply, I would also require sign-off from the brand's supply lead, because removals cost hosts and revenue. That is the same discipline as blocking readiness checks in [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding).

**Keep a regulatory calendar beside the architecture roadmap.** For Corvane the next items are known: Annex III AI duties from 2 December 2027; ViDA's deemed-supplier rule between 1 July 2028 and 1 January 2030 ([The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)); Barcelona's license non-renewals from November 2028; and the Commission's evaluation of the STR Regulation by May 2031, which may bring one EU-level entry point. A rule you can see coming is not an emergency.

**Watch for the opposite failure.** A compliance platform can grow into a bureaucracy that blocks every listing it cannot classify. Measure false removals and reinstatement time as carefully as missed removals.

{id: stays-regulation--questions-to-ask}
## Questions to Ask

1. For each jurisdiction we sell in, where is the rule written down, who approved it, and what is its legal source and effective date?
2. If a court annulled one of our rules yesterday, how long would it take us to list every listing, reservation and notice that relied on it?
3. Which enforcement points evaluate registration, caps and zones, and what does each do when the external register is unreachable?
4. Do connectivity partners and property-management systems pass through the same checks as hosts using our own forms?
5. For a removed listing, what happens to its future reservations, who decided that policy, and is the decision recorded per reservation?
6. Can we produce the DSA and P2B statements of reasons, the guest notices and the authority confirmation from the same reason code?
7. How do we classify supply as hotel or unit for short-term-rental purposes, and who reviews the hard cases?
8. Is our monthly activity data built from the same reservation events that operations uses, and what is our first-submission rejection rate?
9. Which personal data do we collect only because a regulation requires it, for which jurisdictions, and when do we delete it?
10. Which of our AI systems interact with guests or hosts, and how do they disclose it?

{id: stays-regulation--from-rules-to-events}
## From Rules to Events

The machinery in this chapter depends on events the rest of the platform must emit reliably: a reservation created, altered or stayed; a listing published or suspended; a unit's address or number changed. Reports, sweeps and removal orders are only as accurate as those streams. Part VIII ([Part VIII — PLATFORM: The Distributed System Underneath](#part-8)) turns to the platform underneath, starting with [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays): which events a stays platform runs on, and how to design them so that operations, analytics and regulators read the same truth.

{id: stays-regulation--sources-and-evidence}
## Sources and Evidence

*Company engineering and investor sources*

- [Airbnb, Inc. Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm) — Airbnb, 2026: proposed Spanish fine of about €65 million over short-term-rental listings; disputes resolved by removing listings or sharing data.
- [Building on our commitment to trust](https://news.airbnb.com/building-on-our-commitment-to-trust-2) — Airbnb newsroom, 2021: City Portal used by more than 100 governments and destination organizations.
- [Responsible hosting in Amsterdam (help article 860)](https://www.airbnb.com/help/article/860) — Airbnb Help Center, n.d. (fetched October 2026): 30-night cap, registration and permit, calendar block on the city's request.
- [Booking Holdings Inc. Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm) — Booking Holdings, 2026: DMA parity changes in the EEA and the DMA compliance function.
- [Digital Services Act (Booking.com DSA page)](https://www.booking.com/content/dsa.html) — Booking.com, 2026: VLOP recipient figures, transparency reports, ad repository.
- [Connectivity documentation](https://developers.booking.com/connectivity/docs) — Booking.com, n.d. (live 2026): Licences API among connectivity modules.
- [Lodging supply APIs](https://developers.expediagroup.com/supply/lodging) — Expedia Group, n.d. (live 2026): compliance API for regulatory information.

*Standards, regulation and documentation*

- [Regulation (EU) 2024/1028 on short-term accommodation rental data](http://publications.europa.eu/resource/celex/32024R1028) — EU, 2024: definitions, registration, orders, compliance by design, monthly reporting, SDEPs, lists, enforcement; applies from 20 May 2026.
- [Real Decreto 1312/2024 (consolidated text)](https://www.boe.es/buscar/act.php?id=BOE-A-2024-26931) — Boletín Oficial del Estado, 2024 (updated 2026): Spain's national registry and digital single window from 1 July 2025; annulled provisions and the Supreme Court judgments of May and June 2026.
- [El Tribunal Supremo anula el Registro Único de arrendamientos de corta duración](https://www.poderjudicial.es/cgpj/es/Poder-Judicial/Tribunal-Supremo/Noticias-Judiciales/El-Tribunal-Supremo-anula-el-Registro-Unico-de-arrendamientos-de-corta-duracion-por-considerar-que-el-Estado-carece-de-competencia-para-su-creacion) — Consejo General del Poder Judicial, 2026: national registry annulled; single window and platform data duties upheld.
- [Real Decreto 933/2021](https://www.boe.es/buscar/act.php?id=BOE-A-2021-17461) — Boletín Oficial del Estado, 2021: guest-record duties for lodging, including digital platforms; three-year retention.
- [Regulation (EU) 2022/2065, Digital Services Act](http://publications.europa.eu/resource/celex/32022R2065) — EU, 2022: Articles 9, 16, 17, 19, 20, 24(5), 29–33, 93.
- [Regulation (EU) 2022/1925, Digital Markets Act](http://publications.europa.eu/resource/celex/32022R1925) — EU, 2022: Article 5(3) on parity.
- [Gatekeepers](https://digital-markets-act.ec.europa.eu/gatekeepers_en) — European Commission, live 2026: Booking designated 13 May 2024.
- [Judgment in Case C-264/23, Booking.com v 25hours Hotel Company](http://publications.europa.eu/resource/celex/62023CJ0264) — Court of Justice of the EU, 2024: parity clauses are not ancillary restraints.
- [Regulation (EU) 2019/1150, Platform-to-Business](http://publications.europa.eu/resource/celex/32019R1150) — EU, 2019: Articles 3, 4, 5, 11; applies from 12 July 2020.
- [Directive (EU) 2019/2161, Omnibus](http://publications.europa.eu/resource/celex/32019L2161) — EU, 2019: trader status and ranking information on online marketplaces; turnover-based fines; applies from 28 May 2022.
- [Accommodation booking: coordinated actions](https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/accommodation-booking_en) — European Commission, n.d.: Airbnb, Booking.com and Expedia Group commitments, 2018–2020.
- [FTC announces bipartisan rule banning junk ticket and hotel fees](https://www.ftc.gov/news-events/news/press-releases/2024/12/federal-trade-commission-announces-bipartisan-rule-banning-junk-ticket-hotel-fees) — US Federal Trade Commission, 2024: total price for short-term lodging, effective 12 May 2025.
- [Regulation (EU) 2016/679, GDPR](http://publications.europa.eu/resource/celex/32016R0679) — EU, 2016: Articles 5, 9 and 22.
- [Directive (EU) 2015/2366, PSD2](http://publications.europa.eu/resource/celex/32015L2366) — EU, 2015: commercial-agent exclusion, Article 3(b).
- [Directive (EU) 2019/882, European Accessibility Act](http://publications.europa.eu/resource/celex/32019L0882) — EU, 2019: e-commerce services from 28 June 2025; microenterprise exemption.
- [Regulation (EU) 2024/1689, AI Act](http://publications.europa.eu/resource/celex/32024R1689) — EU, 2024: Articles 4, 50 and 113; Annex III.
- [AI Omnibus enters into force](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force) — European Commission, 2026: Annex III high-risk rules from 2 December 2027; simplified AI literacy duty.
- [Registration Law (Local Law 18)](https://www.nyc.gov/site/specialenforcement/registration-law/registration.page) — NYC Office of Special Enforcement, n.d. (fetched October 2026): platform verification before transactions.
- [Faire de sa résidence secondaire une location de vacances](https://www.service-public.gouv.fr/particuliers/vosdroits/F2043) — Service-Public.fr, 2026: 13-character registration number on listings.

*Research and practitioner sources*

- [Airbnb removes almost 65,000 illegal listings at request of Spain's consumer affairs ministry](https://www.catalannews.com/housing-crisis/item/airbnb-removes-almost-65000-illegal-listings-at-request-of-spains-consumer-affairs-ministry) — Catalan News, 2025: scale of government-driven removals in Spain.
- [Barcelona mayor welcomes Constitutional Court ruling on tourist apartment restrictions](https://www.catalannews.com/society-science/item/barcelona-mayor-welcomes-constitutional-court-ruling-on-tourist-apartment-restrictions) — Catalan News, 2025: non-renewal of about 10,000 licenses from November 2028.
- [Spain's antitrust watchdog fines Booking.com nearly $450M](https://techcrunch.com/2024/07/30/spains-antitrust-watchdog-fines-booking-com-nearly-450m-for-unfair-terms-and-restricting-rivals) — TechCrunch, 2024: CNMC findings on ranking factors and program eligibility.
- [La Audiencia Nacional paraliza la multa millonaria de la CNMC a Booking](https://www.hosteltur.com/168767_la-audiencia-nacional-paraliza-la-multa-millonaria-de-la-cnmc-a-booking.html) — Hosteltur, 2025: fine suspended pending appeal.
- [Réglementation Airbnb Paris](https://www.houst.com/blog/reglementation-airbnb-paris) — Houst, 2025: Paris 90-night cap from 1 January 2025 (secondary source; verify against the city's decision).
- For the regulation of classifieds and general marketplaces, see LISTED's [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/marketplace-regulation.html) and [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/multi-country-platforms.html).

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
