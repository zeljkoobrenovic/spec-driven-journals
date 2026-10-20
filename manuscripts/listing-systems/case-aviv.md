{id: case-aviv}
# 49. AVIV Group: Building a European Real-Estate Platform from Acquisitions

![AVIV Group: Building a European Real-Estate Platform from Acquisitions — logo](listing-systems-architecture/posts/49-case-aviv/assets/images/49-case-aviv/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Trace AVIV Group's public record from Axel Springer's first property-portal acquisitions in 2010–2012 to the 2025 carve-out under KKR and CPP Investments and the move to local autonomy. You will separate the few documented facts from the author's reading and from labeled reference-architecture inferences, and test the case against the book's patterns and Veldmark's choices.

> **WHY THE BUSINESS CARES:** AVIV's portals were bought as national leaders and challengers, and their value came from local agent relationships, local data and local monetization. A group that tries to turn such portals into one platform spends against the very assets it bought.

> **WHY ARCHITECTS SHOULD CARE:** AVIV is the clearest public example of a multi-country real-estate group stating an integration goal and then, four years later, reversing it. The case shows which layers of a property portal travel across borders and which do not, even though AVIV itself has published almost nothing about its systems.

> **KEY POINTS:**
>
> * **AVIV is a portfolio built by acquisition, and its public record is corporate, not technical.** SeLoger, Immoweb, Immowelt and Immonet, Logic-Immo, Yad2 and Meilleurs Agents joined between 2010 and 2019 as separate businesses with separate stacks. AVIV publishes no engineering blog, talks or public code, so every statement about its systems below is either dated press evidence or a labeled inference.
> * **The group's documented integration moves are commercial and data-driven, not a shared listing platform.** The 2019 Meilleurs Agents purchase, the 2022 Ultimmo bundle across SeLoger, Logic-Immo and Meilleurs Agents, and the 2023 opening of SeLoger to private sellers all serve one funnel: capture the future seller early and route them to a paying agent. Valuation science and the professional offer were shared before any platform was.
> * **The 2021 integration intent gave way in 2025 to local autonomy with selected group functions.** In 2021 AVIV's CEO spoke of "aligning our tech roadmap across the organization to create a European real estate marketplace". In December 2025 the press described AVIV as having rowed back "on its plans for a fully integrated platform", and the new head of Immowelt described "group-level functions where they create clear advantages". The shape fits a "shared core, local edge" model; what the integrated platform contained is not public.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Acquisition Archipelago** — AVIV's portals arrived over nine years as complete businesses, and the public record shows brands such as Immowelt and Immonet still operating side by side nine years after their 2015 combination.
> * **The Platform Mandate** — A fully integrated European platform for portals with different feed standards, disclosures and pricing norms is the kind of central plan the 2025 shift toward local autonomy undid.
> * **Vanity Liquidity** — AVIV's documented strategy measures supply acquisition (sellers identified, seller leads, commission share) rather than listing counts, which is the cure for this pattern in a lead-generation vertical.

Most marketplace groups in this book's Part IX either built their platforms or bought marketplaces that already shared one. AVIV Group did neither. Axel Springer bought national property portals one at a time (SeLoger in France, Immoweb in Belgium, Immowelt in Germany, Logic-Immo in France again) together with an Israeli horizontal site, Yad2, and a French valuation business, Meilleurs Agents. It then gave them a common name and a common technology leadership, and in 2021 announced the goal of a European real-estate marketplace. **The case is a test of one question: how much of a property portal can be shared across countries?**

The evidence is thin. AVIV's GitHub organization has no public repositories, its Medium publication had no posts when the book's research fetched it in October 2026, and no conference talk by AVIV engineers was found. What exists is corporate history, regulatory decisions, trade-press interviews with AVIV executives and a handful of product announcements. **That evidence is enough to show the direction of the strategy and the funnel it served; it is not enough to describe a single system.**

The record tests the argument of [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) and [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms): in real estate, ingestion formats, mandatory disclosures, address systems, agent software and monetization norms are national, so a group platform has to stop well short of the product. **AVIV's documented moves (shared valuation science, a bundled professional offer, then local autonomy with group functions) trace that boundary from the outside.** The comparison with Veldmark near the end applies the same boundary to Hearthly, Veldmark's property portal in France and Spain.

{id: case-aviv--how-to-read-this-case}
## How to Read This Case

Part IX cases follow stricter rules than the chapters in Parts I–VIII (see [Part IX — PRACTICE: How Others Built It](#part-9)). A **documented fact** carries its source and publication year in the sentence or in the timeline. **The author's interpretation** is marked "my reading" or sits in the Chief Architect's view. A **reference-architecture inference** appears in a callout labeled `INFERENCE, NOT DOCUMENTED`, and describes how a group like AVIV could plausibly be built, never how AVIV is built.

The limits are tighter than in [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta). AVIV has not been listed: before 2025 it was a segment inside Axel Springer, which itself delisted in 2020, and since April 2025 it has been a privately held joint venture. Trade press notes that AVIV "does not publish" a financial breakdown (Online Marketplaces, July 2023). Most of the evidence below comes from one trade publication, Online Marketplaces, and the French real-estate trade site MySweetImmo, both quoting AVIV executives; from Axel Springer, KKR and CPP Investments releases; and from the German and French competition authorities.

**Three kinds of evidence were found and deliberately not used as fact**: job advertisements seen only as search snippets (one mentions a team managing networking for hundreds of AWS accounts), a tech-stack aggregator's profile, and former employees' CVs. They are weak signals about technology choices and say nothing about architecture.

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), appears only in the final comparison. Hearthly's overlap with AVIV's French business is a teaching device, not a disguised description of AVIV or SeLoger.

{id: case-aviv--timeline-aviv-in-dated-events}
## Timeline: AVIV in Dated Events

Dates are those of the cited releases, decisions and articles; ownership and portfolio facts are as of October 2026 and may change.

| Date | Event | Source |
| --- | --- | --- |
| Sep 2010 | Axel Springer offers €34 per share for SeLoger.com, valuing it at about €566 million, after agreeing to buy 12.4% from the co-founders and other shareholders | Tradingsat (BFM), 2010 |
| Nov 2012 | Axel Springer Digital Classifieds, a joint venture with General Atlantic, buys 80% of Immoweb, Belgium's leading property portal, for €127.5 million; the founding family keeps 20% | FrenchWeb, 2012 |
| 2014 | Axel Springer buys Yad2 (Israel; real estate, cars, jobs and general goods) from Walla for about NIS 800 million | Online Marketplaces, 2025 |
| 11 Feb 2015 | Immowelt and Immonet combine under a new Immowelt Holding AG, valued together at €420 million; Axel Springer Digital Classifieds holds 55% and pays former Immowelt shareholders about €131 million; the stated aim is to be a "starke Nummer zwei" (strong number two) | Immowelt press release, 2015 |
| 21 Apr 2015 | The Bundeskartellamt clears the combination of Germany's second- and third-largest property portals, expecting ImmoScout24 to remain the leader | Bundeskartellamt, 2015 |
| 1 Feb 2018 | France's Autorité de la concurrence clears, without conditions, Axel Springer's purchase of Concept Multimédia (Logic-Immo), after its first in-depth review of a merger between two online platforms | Autorité de la concurrence, 2018 |
| 2018–2019 | AVIV Group described in later company profiles as founded in 2018; in 2019 SeLoger and Logic-Immo get the shared corporate brand "Groupe SeLoger" | Company profiles (search snippets); MySweetImmo, 2019 |
| 27 Sep 2019 | AVIV completes the purchase of Meilleurs Agents (valuation and owner-to-agency matching) for €200 million, to "élargir la chaîne de valeur" (widen the value chain) | FrenchWeb, 2019 |
| 23 Aug 2021 | Ex-eBay Classifieds and Domain CTO Brent McLean becomes AVIV CTO; CEO Ait Voncke: "we are aligning our tech roadmap across the organization to create a European real estate marketplace" | Online Marketplaces, 2021 |
| Oct 2022 | AVIV France's vice-president of client operations describes bringing SeLoger and Meilleurs Agents together "sous l'ombrelle AVIV" (under the AVIV umbrella) | MySweetImmo, 2022 |
| 3 Nov 2022 | AVIV launches **Ultimmo**, one professional offer across SeLoger, Logic-Immo and Meilleurs Agents | MySweetImmo, 2022 |
| Mar 2023 | AVIV France plans 300 Tech, Product and Data hires in 2023 and aims to double visits to its French sites by 2025; it monetizes seller leads "through a commission-share model" | Online Marketplaces, 2023 |
| Late Jun 2023 | SeLoger opens free sale listings to private sellers, with the stated goal of routing undecided sellers to professionals | MySweetImmo, 2023 |
| Jul 2023 | Brand list: SeLoger, Logic-Immo, Meilleurs Agents (France); Immoweb (Belgium); Immowelt, Immonet, AllMyHomes, Homeday (Germany); Yad2 (Israel); Housell (Spain); a stake in Zumper (US). H1 revenue up about 3%, about 6% adjusted for consolidation effects | Online Marketplaces, 2023 |
| Jan 2024 | Immoweb agrees to buy Realo, a Belgian portal and valuation-data specialist; both services "unaffected" in the short term | Online Marketplaces, 2024 |
| Feb 2024 | Immowelt GmbH renamed **AVIV Germany**; it runs Immowelt, immonet.de and umzugspreisvergleich.de | Online Marketplaces, 2024 |
| 19 Dec 2024 | Axel Springer signs the split: Stepstone and AVIV to become joint ventures majority-owned by KKR and CPP Investments, Axel Springer keeping about 10%, "following significant platform and technology investments over the past five years" | Axel Springer/CPP Investments release, 2024 |
| Jan 2025 | AVIV Germany takes majority stakes in two German tax-depreciation services, to be integrated into Immowelt and Immoweb | Online Marketplaces, 2025 |
| Feb–Mar 2025 | Ait Voncke leaves after four years as CEO; Vladimir Pravdivy, former CEO of Avito, takes over in March | Online Marketplaces, 2025 |
| 29 Apr 2025 | The new structure becomes effective; AS Classifieds GmbH, led by Julian Deutz from 1 June, supports the management of Stepstone and AVIV | KKR release, 2025 |
| 2 Dec 2025 | Apax Partners signs a deal to buy Yad2 from KKR for about $950 million; sale documents reportedly projected 2025 revenue of about €83 million (real estate 56%, autos 27%, jobs 15%). No closing announcement found as of October 2026 | Online Marketplaces, 2025; Globes, 2025 |
| 4 Dec 2025 | New Immowelt head Theo Mseka, asked about AVIV rowing back "on its plans for a fully integrated platform for all its European portals", describes strengthened local autonomy plus group-level functions | Online Marketplaces, 2025 |

**A correction worth stating once.** Immowelt and Immonet were combined as companies in **2015**, not in 2023. The 2015 release describes a holding and two sites (Nuremberg and Hamburg) and says nothing about merging the portals' technology. In February 2024 both brands were still operated by AVIV Germany. No public source found for this book documents a platform merger or a shutdown of immonet; readers should check before relying on either brand's current status.

![Diagram: AVIV's public record moves from separate portals to a shared commercial and data layer, then to a stated group technology goal, and back to local businesses with selected group functions](listing-systems-architecture/posts/49-case-aviv/assets/images/49-case-aviv/fig01-aviv-s-public-record-moves-separate.jpeg)

**Figure 1:** *AVIV's public record moves from separate portals to a shared commercial and data layer, then to a stated group technology goal, and back to local businesses with selected group functions. Only the second step is documented in any product detail.*

{id: case-aviv--phase-1-assembling-national-portals-20102019}
## Phase 1: Assembling National Portals (2010–2019)

{id: case-aviv--what-was-bought}
### What was bought

Every AVIV portal was bought as a working business with its own customers, brand and technology. The deals came through Axel Springer and, until General Atlantic's exit, through Axel Springer Digital Classifieds, of which General Atlantic held 15% in 2015 (Immowelt release, 2015). SeLoger was a listed French company when Axel Springer bid for it in 2010; Immoweb was a family-founded Belgian portal from 1996; Immowelt and Immonet were Germany's second and third portals; Logic-Immo came with print magazines; Yad2 was Israel's horizontal classifieds leader; Meilleurs Agents was a ten-year-old valuation start-up.

None of the acquisition announcements found for this book describes a technology integration plan. The 2015 Immowelt–Immonet release is typical: it describes the shareholdings, the leadership, the two sites and the Immowelt broker-software products (estateOffice, estatePro), and says nothing about merging platforms. **My reading** is that the group was built as a holding of national leaders, each kept whole because its value was local: agency relationships, brand traffic, local data and local pricing power.

{id: case-aviv--what-the-regulators-saw}
### What the regulators saw

Two competition decisions give the clearest public description of how these markets work, and both bear on architecture.

The **Bundeskartellamt** (April 2015) cleared the Immowelt–Immonet combination with an argument about network effects: where many small portals compete, property providers and seekers both drift to the leader, so with the merger "customers will have another large portal", in the words of its president, Andreas Mundt. The combination was justified as liquidity aggregation, not as cost synergy.

The **Autorité de la concurrence** (February 2018) cleared Logic-Immo's acquisition after its first in-depth review of a merger between two online platforms. Its reasoning was that agencies facing a price rise at SeLoger or Logic-Immo would shift their listings to other portals, mainly leboncoin, and it noted the rise of Bien'ici, a portal created on the initiative of the property industry. In the book's terms, French agencies **multi-home** (list on several portals at once, see [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)), and the regulator counted on that.

**My reading** of what this means for systems: a French or German portal does not own its supply. The agency's own software holds the mandate and pushes the same listing to several portals, so every portal in the group competes for the same feed and must accept the agency software's formats. That is why [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) treats real-estate feeds as contracts with external systems of record, and why a group that owns two portals in one country still runs two ingestion edges facing the same vendors.

![An agency's software holds the mandate and pushes copies of the same listing through separate feeds to three generic portals.](listing-systems-architecture/posts/49-case-aviv/assets/images/49-case-aviv/one-mandate-many-portals.jpeg)

**Figure 2:** *Reference illustration, not AVIV's systems: in a multi-homing market the agency's software holds the mandate and pushes the same listing to several portals, so every portal competes for the same feed.*

{id: case-aviv--two-portals-in-one-country}
### Two portals in one country

AVIV kept both of its same-country pairs, Immowelt and Immonet in Germany and SeLoger and Logic-Immo in France, as separate brands for years. Immonet was still listed in AVIV's brand list in July 2023 and run by AVIV Germany in February 2024; SeLoger and Logic-Immo shared a corporate brand from 2019 and a professional offer from 2022.

> **INFERENCE, NOT DOCUMENTED:** When two portals in one country keep their brands, the cheapest technical integration is usually below the brand: one ingestion pipeline that accepts each agency's feed once and publishes to both sites, one media store, one agency account and contract system, with two front ends and two search experiences on top. Whether AVIV did this for either pair is not public. "Two brands" says nothing about "two stacks" in either direction, so an architect assessing such a group has to ask.

{id: case-aviv--phase-2-moving-up-the-seller-funnel-20192023}
## Phase 2: Moving Up the Seller Funnel (2019–2023)

{id: case-aviv--meilleurs-agents-valuation-as-supply-acquisition}
### Meilleurs Agents: valuation as supply acquisition

Valuation is AVIV's best-documented business, because it was a product, not a platform.

When Meilleurs Agents launched in 2008, FrenchWeb described its method: a historical base of "les informations enregistrées par les notaires depuis 1990" (the information recorded by notaries since 1990), recent sales by partner agencies added in real time, an algorithm that re-indexes past transactions to current market conditions, and a price per square meter that the user then adjusts for condition, exposure, layout and extras (FrenchWeb, 2008).

Fourteen years later, Meilleurs Agents' VP Data and Science, Thomas Lefevre, said that "it is not complicated to make an estimation tool. What is complicated, however, is to make a fair estimate", that the data team had grown to 45 people, and that "the median estimate error of our valuations against final transaction value in 2021 was just 6%" (Online Marketplaces, June 2022). The 6% figure is self-reported; no independent audit or methodology note was found.

The 2019 purchase carries the earliest public statement of something AVIV intended to share across countries, and it is a capability (valuation science), not a system. AVIV bought the company in September 2019 for €200 million; FrenchWeb reported that Axel Springer wanted to widen the value chain of its French portals and **share Meilleurs Agents' valuation expertise with its foreign sites** (FrenchWeb, 2019).

![One recipe book labeled Method travels to three separate kitchens, each using its own basket of local data to produce its own estimate.](listing-systems-architecture/posts/49-case-aviv/assets/images/49-case-aviv/shared-method-local-data.jpeg)

**Figure 3:** *What AVIV said in 2019 it would share was valuation expertise, a method that can travel between countries while each country's model still has to be trained on its own transaction data.*

**My reading** is that the valuation tool is a **supply-acquisition product**. A homeowner who asks what their flat is worth is a likely seller months before they choose an agent. A portal that captures that moment can sell it to agents as a seller lead. This is the same logic as Rightmove's Online Agent Valuation and Zillow's Zestimate, compared in [Zillow, Rightmove, Idealista and REA: What Property Portals Teach](#case-property-portals); the modeling side, including why on-market and off-market accuracy must be reported separately, is in [Models in Production: ML Platforms and Use Cases](#ml-platform).

{id: case-aviv--ultimmo-the-professional-offer-as-the-first-integration}
### Ultimmo: the professional offer as the first integration

In November 2022 AVIV launched **Ultimmo**, one offer for agents across SeLoger, Logic-Immo and Meilleurs Agents. The launch material cites "plus d'1 million de visites par jour" (more than one million visits a day) across the three brands' platforms, 630,000 sellers identified each month, and the claim that two sales in three begin on one of the group's platforms. It bundles listing distribution and promotion, logo display on result pages, an estimation tool called Inventory, **detection of seller prospects among buyer contacts**, and an optional prospecting map. AVIV France's managing director, Caroline Evans de Gantès, framed it: "Les professionnels ne sont plus seulement en demande de mandats" (professionals no longer just want mandates; they also want visibility with buyers) (MySweetImmo, November 2022).

A month earlier, AVIV France's vice-president of client operations, Franck Le Tendre, described the goal of combining SeLoger's relationship with professionals and Meilleurs Agents' work on mandate acquisition, and said Meilleurs Agents' prospecting map had already been rolled out across the group's entities (MySweetImmo, October 2022).

**This is the only cross-brand integration in AVIV's public record described at the level of features**, and it is commercial: one contract and one set of tools sold to an agent, over brands that stay separate. Its features need shared data (sellers identified across brands, buyer contacts classified as potential sellers) and a shared professional account, but nothing in the record says they required a shared listing or search platform.

{id: case-aviv--opening-seloger-to-private-sellers}
### Opening SeLoger to private sellers

In late June 2023 SeLoger, until then an agent-only portal for sales, opened free sale listings to private sellers. Le Tendre explained the reasoning: professionals' share of the market had been flat for 15 to 20 years, about a third of sellers who try to sell alone give up, and "notre objectif est de capter ces indécis et de les diriger vers des professionnels" (our goal is to capture these undecided sellers and direct them to professionals). He said the group had 800 people working on innovation, and that many agents were angry about the move. At the end of September 2023 about 6,000 private sale listings were online, against just under a million professional listings for sale and rent (MySweetImmo, October 2023).

The revenue model behind the funnel was stated the same year: AVIV France monetizes seller leads "through a commission-share model" (Online Marketplaces, March 2023).

![Diagram: The seller funnel that AVIV's documented French moves serve, drawn from the public product descriptions (2019–2023) — not a description of AVIV's systems](listing-systems-architecture/posts/49-case-aviv/assets/images/49-case-aviv/fig04-seller-funnel-that-aviv-s-documented.jpeg)

**Figure 4:** *The seller funnel that AVIV's documented French moves serve, drawn from the public product descriptions (2019–2023) — not a description of AVIV's systems. Every entry point produces a seller lead; the revenue event, a commission share, happens outside the portal.*

> **INFERENCE, NOT DOCUMENTED:** A commission-share model makes the portal's revenue depend on a sale recorded by an agency and a notary, weeks or months after the lead. A plausible reference architecture — not a description of AVIV's systems — needs a lead ledger with stable identifiers for the homeowner, the property and the agency, homeowner consent to routing and outcome tracking, and a reconciliation process against agent-reported or contractually reported closings. That is closer to the attribution systems of [How Listing Marketplaces Make Money](#monetization-models) and [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) than to a classifieds listing service, and it is local by nature: French mandates, fees and notarial practice do not exist in the same form in Germany or Belgium.

{id: case-aviv--germany-and-belgium}
### Germany and Belgium

**Each market built its own adjacencies around its own transaction**: valuation and commission share in France, tax and financing services in Germany, valuation data in Belgium. The German and Belgian records are thinner but point the same way. In December 2025 Theo Mseka said "the subscription model remains the core model in the German market today", that Immowelt offers AI features including "a tool for creating high-quality property descriptions", and that in 2025 Immowelt bought Kaufpreis-Aufteilung.com, nutzungsdauer.com and BauDarlehen24 to build an ecosystem around the property transaction (Online Marketplaces, December 2025). In Belgium, Immoweb bought Realo, a portal that also sells "data as a service" and valuations, in January 2024.

{id: case-aviv--phase-3-the-integration-intent-20212024}
## Phase 3: The Integration Intent (2021–2024)

{id: case-aviv--what-was-said}
### What was said

The integration phase is documented almost entirely by statements of intent.

- In August 2021, announcing Brent McLean as CTO with responsibility for technology at Immoweb, SeLoger, Yad2 and Immowelt, CEO Ait Voncke said: "we are aligning our tech roadmap across the organization to create a European real estate marketplace" (Online Marketplaces, 2021). McLean came from eBay Classifieds Group and Domain, both groups that ran platforms across several marketplaces.
- In March 2023 AVIV France planned 300 technology, product and data hires against an industry trend of cuts; its managing director, Caroline Evans de Gantès, said AVIV would "write the future of real estate" (Online Marketplaces, 2023).
- In February 2024 the German company's managing director, Felix Kusch, explained the rename to AVIV Germany as combining a well-known brand with "the know-how and innovative strength of an international tech company", while the services Immowelt was known for would stay (Online Marketplaces, 2024).
- In December 2024 the signing release for the Axel Springer split referred to "significant platform and technology investments over the past five years" at Stepstone and AVIV (Axel Springer/CPP Investments, 2024).

{id: case-aviv--what-was-not-said}
### What was not said

No public source found for this book describes what the European marketplace or the "fully integrated platform" was meant to contain: a shared listing service, a shared search engine, shared agent tools, shared billing, or only shared infrastructure and data. No source describes a portal moving onto a group platform, a migration milestone or a cost. The phrase "fully integrated platform" itself comes from the interviewer's question in December 2025, not from an AVIV statement.

**My reading** is that the integration intent is documented as a direction of travel, with leadership and hiring behind it, and its scope is unknown. The book therefore treats it as a goal set and later changed, and draws lessons only from that sequence and the structure of the markets, not from any assumed architecture.

{id: case-aviv--phase-4-separation-and-local-autonomy-2025}
## Phase 4: Separation and Local Autonomy (2025)

{id: case-aviv--the-ownership-change}
### The ownership change

The split signed in December 2024 became effective on 29 April 2025. AVIV and Stepstone became "independent joint venture companies with KKR and CPP Investments as majority owners", with Axel Springer holding "ten percent in both classifieds companies"; a holding company, AS Classifieds GmbH, led by Julian Deutz, supports their management (KKR, 2025). The signing release said the classifieds businesses "will continue to independently pursue their respective growth strategies". AVIV's CEO changed the same spring.

The first visible portfolio move under the new owners was the signed sale of the most separable asset. In December 2025 Apax Partners signed to buy Yad2 from KKR for about $950 million. The trade report names KKR, not AVIV, as the seller and says KKR gained full control of Yad2 in March 2025 through the carve-out; whether Yad2 still sat inside AVIV's structure at the time is not clear from public sources (Online Marketplaces, December 2025). Yad2 is a horizontal marketplace in a non-European market, with real estate only 56% of its projected 2025 revenue; it never fitted a European real-estate platform.

{id: case-aviv--the-reversal-in-an-executive-s-words}
### The reversal, in an executive's words

The clearest statement of AVIV's current model comes from the December 2025 interview with Immowelt's new head. The interviewer's question records the reversal: "We recently saw AVIV Group row back on its plans for a fully integrated platform for all its European portals." Mseka answered that "AVIV has strengthened the autonomy of its local businesses", making them faster in marketing and sales, while "we continue to operate group-level functions where they create clear advantages"; depending on the task, the group uses "sometimes local and sometimes cross-group" approaches. He said he had worked on multi-country platforms and seen their efficiency and scale, but was convinced by the localization strategy because it lets each business "run at their own pace" (Online Marketplaces, December 2025).

**My reading** has three parts, each conditional on thin evidence.

1. **The reversal is real but its size is unknown.** "Row back on plans" can mean a platform half-built and stopped, or a plan never far advanced. The record does not say which.
2. **The timing coincides with the ownership change, and no source links the two.** Under owners who had just sold Yad2 separately, separable businesses are worth more, as [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) shows for Adevinta's 2025 break-up. That is a plausible motive, not a documented one.
3. **The stated end state is a recognizable architecture.** "Group-level functions where they create clear advantages" plus local autonomy in "marketing and sales" is the "shared core, local edge" model of [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms). What AVIV includes in its group functions is not public.

{id: case-aviv--why-real-estate-resists-one-platform}
## Why Real Estate Resists One Platform

National supply software, ingestion standards, disclosures, monetization and property data explain AVIV's record, and they are documented outside AVIV. [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) develops them; the table keeps the points relevant to AVIV's markets.

| Dimension | France (SeLoger, Logic-Immo, Meilleurs Agents) | Germany (Immowelt, Immonet) | Belgium (Immoweb) | What a group platform must absorb |
| --- | --- | --- | --- | --- |
| Supply source | Agency transaction software pushing to many portals | Broker software exporting OpenImmo XML, typically over FTP | Agency software and portal-specific feeds | One adapter set per national software ecosystem |
| Ingestion standard | Portal- or vendor-defined export formats (no public common standard found) | OpenImmo since 2001; REST and JSON version 2.0 expected at the end of 2026 | Not documented in the research | Two generations of standards at once in some markets |
| Mandatory disclosures | DPE (diagnostic de performance énergétique) energy and climate classes, estimated annual energy costs, warning for F and G homes | Energy-certificate data (national rules; not verified for this book) | Regional rules (not verified for this book) | Country-specific fields, validation and display rules |
| Main monetization | Agency subscriptions plus commission-share seller leads | Subscriptions remain "the core model" (2025) | Not documented in the research | Different products, contracts and billing per market |
| Property data | Notary transaction history since 1990, agency sales, open DVF (demandes de valeurs foncières) transaction data | Different sources and no free national address-ID register widely used by portals | Valuation data via Realo (2024) | Valuation models trained per country |

*Sources: Service-Public.fr on DPE (page verified January 2026); OpenImmo e.V. (accessed October 2026); Mseka interview (2025); FrenchWeb (2008); Immoweb–Realo (2024). The France ingestion row, the Germany address entry and the unverified disclosure entries are the book's research findings and judgement, not AVIV statements.*

OpenImmo e.V. lists AVIV Group as its member from France (accessed October 2026). **My reading** is that AVIV has at least looked at a German standard as a possible common ingestion format beyond Germany; no detail of how it uses the standard was found.

> **INFERENCE, NOT DOCUMENTED:** A plausible reference architecture for a federated multi-country property group — not a description of AVIV's systems — puts cloud landing zones, security, identity tooling, the data platform and machine-learning tooling at group level; offers a shared ingestion engine and a core listing schema (location, price, surface, rooms, media) that each country extends with its own disclosure fields and property-type taxonomy; may share a search engine while keeping ranking policy and paid visibility local; shares valuation *methods* while training on local data; and keeps monetization, billing, agent CRM and professional tools local. In that design the group platform ends at the ingestion adapters on one side and the ranking policy on the other.

![Diagram: A labeled reference architecture for a multi-country property group, not AVIV's](listing-systems-architecture/posts/49-case-aviv/assets/images/49-case-aviv/fig05-labeled-reference-architecture-multi-country-property.jpeg)

**Figure 5:** *A labeled reference architecture for a multi-country property group, not AVIV's: the shared core is infrastructure, data, identity, engines and methods; the local edge is everything an agent, a regulator or a homeowner sees.*

{id: case-aviv--trade-offs-the-case-illustrates}
## Trade-offs the Case Illustrates

| Option | What AVIV's record shows | When it is right | When it fails |
| --- | --- | --- | --- |
| **Keep acquired portals whole** | 2010–2019: each portal bought and kept as a business; two brands per country in Germany and France | Early in a roll-up, when each portal's value is local relationships and brand | When the same capability (valuation, agent tools, media) is bought or built four times |
| **Share a capability, not a system** (valuation science) | Meilleurs Agents bought in 2019 partly to share valuation expertise with foreign sites | When the method transfers and the data does not | When a group expects the French model to work on German or Belgian data unchanged |
| **Bundle the professional offer within a country** | Ultimmo (2022) across three French brands | When several brands in one market sell to the same agents | When the bundle hides which brand delivers the value, or invites competition scrutiny |
| **Integrate into one European platform** | Stated in 2021; reversed by 2025; scope never published | When markets share standards, disclosures and monetization, and ownership is stable | When feeds, disclosures, address systems and pricing norms are national, as in real estate |
| **Local autonomy with group functions** | Stated in 2025 | When the businesses may be sold or run at different paces, and group functions pass a clear-advantage test | When "group functions" is left undefined and each local business rebuilds them |

The table is not a ladder. **The line that AVIV's record draws runs through the capability map, not between countries**: methods, data science and infrastructure can be shared; the agent-facing product, the feed edge and the monetization stay local.

{id: case-aviv--vertical-differences-in-the-record}
## Vertical Differences in the Record

AVIV was a real-estate group with one horizontal asset, and the two behaved differently.

| Asset type | AVIV examples | What the record shows | Implication |
| --- | --- | --- | --- |
| **Agency-supplied property portals** | SeLoger, Logic-Immo, Immowelt, Immonet, Immoweb | Kept as brands; national monetization (commission share in France, subscriptions in Germany); local adjacencies (tax services, valuation data) | The feed edge and the professional product are the least shareable parts |
| **Valuation and seller-lead services** | Meilleurs Agents, Realo | Bought for data and seller acquisition; valuation expertise to be shared across countries (2019) | Methods and teams travel; training data and lead routing do not |
| **Hybrid brokerage** | Homeday (Germany), Housell (Spain) | In the 2023 brand list; later status not documented | A portal owning brokers competes with its own customers, a trust constraint on data use |
| **Horizontal classifieds** | Yad2 (Israel) | Real estate 56%, autos 27%, jobs 15% of projected 2025 revenue; sale signed December 2025 | The asset least aligned with a property platform was the first to be separated |

A portal group that also owns brokerages, or that routes private sellers to agents, holds data its agency customers would not want a competitor to see. That is the same neutrality problem Veldmark faces with Keybridge, discussed below, and it is one reason seller-lead and agent data are usually kept inside the local business.

{id: case-aviv--failure-modes-the-record-exposes}
## Failure Modes the Record Exposes

1. **Integration goals without a published scope.** The 2021 goal had a leader, a budget signal and hiring, but no public statement of which layers it covered. A plan whose scope is not written down is easy to reverse and hard to evaluate afterwards.
2. **Two portals in one market, two of everything.** Keeping brands is a sound commercial choice; keeping two ingestion edges, two media stores and two agent account systems behind them is a cost that the brand decision does not require. The public record does not show which AVIV did.
3. **Treating valuation as a feature.** Meilleurs Agents shows valuation driving seller acquisition and revenue; a group that files it under "data science" will underinvest in its governance, accuracy reporting and data rights. [Models in Production: ML Platforms and Use Cases](#ml-platform) covers the governance.
4. **Funnel moves that anger the supply side.** The 2023 private-seller opening was explained as routing sellers to agents, and many agents were still angry. In a lead-generation vertical, agents control supply and multi-home; any product that looks like disintermediation is a liquidity risk (see [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)).
5. **Group functions defined after the fact.** "Where they create clear advantages" is a sound test, but if each function's owner, interface and exit path are not explicit, local businesses rebuild them and the group pays twice.

{id: case-aviv--where-the-public-evidence-stops}
## Where the Public Evidence Stops

The following questions matter to an architect and are not answered by any public source found for this book. The chapter does not fill them with inference.

| Question | What is public | What is not |
| --- | --- | --- |
| What was the "European real estate marketplace" or "fully integrated platform"? | The 2021 intent; the 2025 interviewer's description of rowing back | Scope, architecture, how far it got, cost, which portals moved |
| Which group-level functions remain? | That they exist "where they create clear advantages" (2025) | The list, their owners and interfaces |
| Do Immowelt and Immonet, or SeLoger and Logic-Immo, share a stack? | Corporate combinations (2015, 2019) and a shared French professional offer (2022) | Whether ingestion, search, media or agent accounts are shared |
| How do AVIV portals ingest agency feeds? | AVIV's OpenImmo membership as a French member | Formats, adapters, validation, reconciliation |
| How does Meilleurs Agents estimate prices? | The 2008 method description; a self-reported 6% median error for 2021 | Model family, features, intervals, retraining, how agency and notary records are de-duplicated |
| How does the commission-share model attribute revenue? | That it exists (2023) | Lead identifiers, consent, outcome tracking, reconciliation |
| What do AVIV's engineers run? | Job ads, an aggregator profile and CVs, seen as search snippets | Any first-party technical description; no blog posts, talks or public repositories were found |
| What happened to Housell, Homeday and the Zumper stake? | Their presence in the 2023 brand list | Current status |

Two facts are volatile as of October 2026: the closing of the Yad2 sale to Apax, and the status of immonet as a separate brand. Readers should check both before relying on the portfolio described here.

{id: case-aviv--the-chief-architect-s-view}
## The Chief Architect's View

What I take from AVIV is less about systems, which are not public, than about where the boundary of a property group's platform sits.

**Draw the shared boundary by capability, and expect it to stop short of the agent.** In real estate the agent's software, the national feed format, the disclosure rules and the pricing model meet in one place: the professional edge. I would share infrastructure, data, identity tooling and engines without hesitation, share valuation and ranking *methods* as group science, and keep the feed adapters, disclosure validation, professional products and lead routing local. If a proposal for a group platform crosses that line, it needs a separate case.

**Write down the scope of any integration goal before staffing it.** A goal such as "one European marketplace" can mean anything from shared cloud accounts to one listing service. I would require a layer-by-layer scope, the markets in each stage, and an exit criterion per stage. That is what makes a later change of direction cheap rather than a write-off, and it is what [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) calls a consolidation sequence.

**Treat valuation as a supply product with its own governance.** The AVIV and Meilleurs Agents record, together with Zillow's and Rightmove's in [Zillow, Rightmove, Idealista and REA: What Property Portals Teach](#case-property-portals), says that the estimate is how a portal reaches the seller first. It deserves an owner, published accuracy definitions (on-market and off-market separately), data-rights checks on every source, and a clear line between an estimate that informs and one that commits money.

**Keep the attribution chain local and explicit.** Commission-share revenue depends on events outside the platform. The lead ledger, consent and reconciliation are local, legal and auditable work; they should be designed as such, not bolted onto a listing service.

**Design every group function to be handed over.** Yad2's sale was signed about seven months after the carve-out became effective. Any function a business might take with it (identity, data products, valuation models) should be tenant-scoped from its first release, as [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) argues at greater length.

{id: case-aviv--comparing-the-case-to-the-book-s-patterns-and-to-veldmark}
## Comparing the Case to the Book's Patterns and to Veldmark

The book's patterns, as AVIV's record tests them:

| Book pattern or claim | AVIV's record | Verdict |
| --- | --- | --- |
| Real estate is the least portable vertical across countries ([Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements)) | National feeds, disclosures and monetization; 2025 shift to local autonomy | Supported, though AVIV never stated its reasons |
| Share global components beneath local products ([One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms)) | Group functions "where they create clear advantages" (2025) | Consistent with the stated end state; contents not public |
| Consolidate enabling layers first, core product last ([After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation)) | A "fully integrated platform" planned and rowed back | Consistent, as a cautionary data point |
| Valuation is a supply-acquisition engine ([Models in Production: ML Platforms and Use Cases](#ml-platform), [How Listing Marketplaces Make Money](#monetization-models)) | Meilleurs Agents, Ultimmo seller detection, commission-share seller leads | Strongly supported for France |
| Real-estate feeds are contracts with external systems of record ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)) | Multi-homing agencies cited by the French regulator (2018); OpenImmo membership | Supported by regulators' descriptions; AVIV's ingestion not public |
| Measure matches, not listings ([Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)) | "630,000 sellers identified each month"; seller leads monetized | Supported: AVIV's public metrics are funnel metrics |

Now Veldmark, the fictional group, as of its 2027 decisions in the scenario. Hearthly, Veldmark's real-estate portal, operates in France (acquired 2023) and Spain (acquired 2025), with **€395 million** of 2026 revenue, **84%** of listings arriving through feeds from about **160** real-estate software vendors, and **Valuo**, its valuation product, trained on France's open DVF transaction data and Hearthly listing data. Veldmark's Common Ground program follows the principle **"share platforms, not products"**. The comparison sharpens four choices.

| Veldmark choice (2027) | AVIV parallel | What the case suggests |
| --- | --- | --- |
| Supply Contract v1 (September 2027): one envelope, error catalog and validator library for the group, but **adapters stay brand-local**; ingestion is not a Common Ground shared platform | National software ecosystems; OpenImmo as one possible common standard | The right line: share the contract and the validator, keep the adapters where the vendors are |
| Hearthly stays on Google Cloud through 2028 and moves to the shared OpenSearch platform by end of 2028, keeping its own ranking policy | Group functions plus local autonomy (2025) | Sharing the engine and keeping the relevance policy local is the "shared core, local edge" the case points to |
| Valuo seller leads: flat-fee product, plus a **commission-share pilot in the Lyon metropolitan area in 2028**, with homeowner consent and no use of Keybridge mandate data | AVIV France's commission-share seller leads (2023) | The attribution chain must be local, consented and auditable before the pilot starts; it is not a group listing feature |
| Keybridge kept a separate, neutral SaaS (March 2027); no Keybridge agency data used by Hearthly | SeLoger's private-seller opening angered agents (2023); hybrid brokerages in AVIV's portfolio | Agent trust is a supply constraint; neutrality has to be enforced in data access, not promised |

The worked question is the one AVIV faced in 2021. Suppose Claire Fontaine, Hearthly's fictional CEO, proposed in 2027 a single Hearthly platform for France and Spain, to be extended to any future property acquisition. Under the ledger, Hearthly France already de-duplicates **1.9 million** listings into about **1.12 million** distinct properties (**1.7** listings per property), with clustering in a Hearthly property registry; Hearthly Spain was rebranded only in 2026; and Valuo's Spanish version is planned for 2028. Following AVIV's record and the trade-off table above, I would advise Ingrid Halvorsen, Veldmark's fictional Group Chief Architect, to approve the parts that pass the clear-advantage test (the shared search engine, the property-registry *design*, the Valuo *method* and its governance, the group event backbone) and to reject a single product platform until the Spanish feed vendors, disclosure fields and pricing norms have been profiled against the French ones. **The decision record should state which layers are shared, which are local, and the evidence that would change the split** — the scope that the public AVIV record never shows.

{id: case-aviv--questions-to-ask}
## Questions to Ask

1. For each capability we plan to share across countries, is it a method, an engine or a product, and does it pass a written clear-advantage test?
2. Where exactly does our group platform stop on the supply side: at the ingestion engine, the validator library, or the feed adapters?
3. Which mandatory disclosure fields differ by country, and who owns their validation and display rules?
4. Is our valuation product governed as a supply-acquisition product, with an owner, accuracy definitions and data-rights checks per source?
5. If we monetize seller leads by commission share, what identifiers, consent records and reconciliation process prove the outcome?
6. When two of our brands serve one market, which layers behind the brands are duplicated, and is that duplication a decision or an accident?
7. What is the written scope, stage plan and exit criterion of any integration goal we have announced?
8. Which product moves could look like disintermediation to agents, and how will we detect supply withdrawal early?
9. If one business were sold within a year, which group functions would it take, and are they tenant-scoped today?

AVIV shows how little of a property portal travels across borders, seen from the outside. The next case, [Zillow, Rightmove, Idealista and REA: What Property Portals Teach](#case-property-portals), turns to the portals that publish the most about their economics and engineering — Zillow, Rightmove, Idealista and REA — and to what their valuation, ingestion and monetization records teach.

{id: case-aviv--sources-and-evidence}
## Sources and Evidence

{id: case-aviv--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [immowelt und immonet schließen sich zusammen](https://www.immowelt.de/ueberuns/presse/pressemitteilungenkontakt/immowelt-group/immowelt-und-immonet-schliessen-sich-zusammen/) — Immowelt (press release), 2015. Combination structure, valuation, payment, sites and "number two" aim.
- [Axel Springer and KKR signing announcement](https://cppinvestments.com/wp-content/uploads/2024/12/Axel-Springer-Signing-Announcement-Final-19Dec2024-ENGLISH.pdf) — Axel Springer, KKR and CPP Investments, 2024. Joint-venture structure, about 10% Axel Springer stake, "significant platform and technology investments".
- [Axel Springer's new corporate structure effective](https://media.kkr.com/news-details?news_id=3ae6964b-af1f-4893-a221-d5bc7e32ce75) — KKR, 2025. Effective date, majority owners, AS Classifieds GmbH.
- [AVIV Group GitHub organization](https://github.com/aviv-group) — AVIV Group, n.d. (accessed October 2026). No public repositories.
- [AVIV Group Insights (Medium RSS)](https://medium.com/feed/aviv-group) — AVIV Group, n.d. (accessed October 2026). No posts in the feed.

{id: case-aviv--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [The Bundeskartellamt clears the Immonet/Immowelt merger](https://www.bundeskartellamt.de/SharedDocs/Meldung/EN/Pressemitteilungen/2015/21_04_2015_Immonet_Immowelt.html) — Bundeskartellamt, 2015. Market ranking and network-effect reasoning.
- [Online property advertising: Axel Springer / Concept Multimédia](https://www.autoritedelaconcurrence.fr/en/communiques-de-presse/01-february-2018-online-property-advertising) — Autorité de la concurrence, 2018. Clearance of Logic-Immo; agencies switching portals; Bien'ici.
- [OpenImmo](https://www.openimmo.de/) — OpenImmo e.V., n.d. (accessed October 2026). XML standard, version 2.0 timeline, AVIV Group as French member.
- [Diagnostic de performance énergétique (DPE)](https://www.service-public.gouv.fr/particuliers/vosdroits/F16096) — Service-Public.fr, page verified January 2026. French listing disclosure obligations.

{id: case-aviv--research-and-practitioner-sources}
### Research and practitioner sources

- [Selogercom: Axel Springer veut racheter le groupe Seloger.com](https://www.tradingsat.com/selogercom-FR0010294595/actualites/selogercom-axel-springer-veut-racheter-le-groupe-selogercom-273198.html) — Tradingsat, 2010. SeLoger offer price and stake.
- [Axel Springer continue ses emplettes sur le net avec Immoweb](https://www.frenchweb.fr/axel-springer-continue-ses-emplettes-sur-le-net-avec-immoweb/85502) — FrenchWeb, 2012. Immoweb stake and price.
- [Un nouveau site immobilier: MeilleursAgents.com](https://www.frenchweb.fr/un-nouveau-site-immobilier-meilleursagents-com/245) — FrenchWeb, 2008. Original valuation method and data sources.
- [MeilleursAgents racheté par Axel Springer pour 200 millions d'euros](https://www.frenchweb.fr/meilleursagents-rachete-par-axel-springer-pour-200-millions-deuros/377533) — FrenchWeb, 2019. Acquisition price and rationale.
- [Groupe SeLoger, la nouvelle marque corporate](https://www.mysweetimmo.com/2019/05/07/groupe-seloger-la-nouvelle-marque-corporate-seloger-et-logic-immo/) — MySweetImmo, 2019. Shared corporate brand for SeLoger and Logic-Immo.
- [Ex-eBay Classifieds and Domain CTO Brent McLean switches to AVIV Group](https://onlinemarketplaces.com/?p=37137) — Online Marketplaces, 2021. CTO appointment and the 2021 integration intent.
- [Meilleurs Agents launches new campaign](https://www.onlinemarketplaces.com/articles/meilleurs-agents-launches-new-campaign-fake-websites-included) — Online Marketplaces, 2022. Data team size and self-reported 6% median error.
- [Franck Le Tendre: regrouper MeilleursAgents et SeLoger sous l'ombrelle AVIV](https://www.mysweetimmo.com/2022/10/17/franck-le-tendre-regrouper-meilleurs-agents-et-se-loger-sous-lombrelle-aviv/) — MySweetImmo, 2022. Combining brand expertise; group-wide prospecting map.
- [Pros de l'immo: AVIV Group lance Ultimmo](https://www.mysweetimmo.com/2022/11/03/pros-de-limmo-aviv-group-lance-ultimmo-une-offre-pour-capter-vendeurs-et-acheteurs/) — MySweetImmo, 2022. The cross-brand professional offer and its figures.
- [SeLoger parent AVIV France to add 300 employees in 2023](https://www.onlinemarketplaces.com/articles/seloger-parent-aviv-france-to-add-300-employees-in-2023) — Online Marketplaces, 2023. Hiring plan, traffic goal, commission-share seller leads.
- [Pourquoi ouvrir SeLoger aux annonces des particuliers](https://www.mysweetimmo.com/2023/10/09/immobilier-pourquoi-ouvrir-seloger-aux-annonces-des-particuliers-franck-le-tendre-aviv-france/) — MySweetImmo, 2023. Private-seller opening, reasons, agents' reaction, listing counts.
- [SeLoger, Immoweb and Immowelt parent reports 3% growth in first half of 2023](https://www.onlinemarketplaces.com/articles/aviv-group-hy1-2023-results/) — Online Marketplaces, 2023. Brand list and growth figures.
- [Belgian market leader Immoweb acquires rival Realo](https://onlinemarketplaces.com/articles/belgian-market-leader-immoweb-acquires-rival-realo) — Online Marketplaces, 2024. Realo deal and integration statements.
- [Immowelt's German parent company rebranded to AVIV Germany](https://www.onlinemarketplaces.com/articles/immowelts-german-parent-company-rebranded-to-aviv-germany) — Online Marketplaces, 2024. Rename and portals operated.
- [AVIV Germany closes two tax-focused acquisitions](https://www.onlinemarketplaces.com/articles/aviv-germany-closes-two-tax-focused-acquisitions) — Online Marketplaces, 2025. German adjacencies.
- [Axel Springer appoints ex-Avito CEO to lead AVIV Group as Ait Voncke departs](https://www.onlinemarketplaces.com/?p=103886) — Online Marketplaces, 2025. CEO change.
- [AVIV Group sells Israeli classifieds brand Yad2 to Apax Partners for $950M](https://www.onlinemarketplaces.com/articles/aviv-group-sells-israeli-classifieds-brand-yad2-to-apax-partners-for-950m/) — Online Marketplaces, 2025. Yad2 history, sale signing and revenue mix.
- [Apax Partners to buy Yad2 for $950m](https://en.globes.co.il/en/article-1001528063) — Globes, 2025. Signing of the Yad2 sale.
- [Interview: new Immowelt boss Theo Mseka on challenges and plans for the German market](https://www.onlinemarketplaces.com/articles/interview-new-immowelt-boss-theo-mseka-on-challenges-and-plans-for-the-german-market/) — Online Marketplaces, 2025. The reversal, local autonomy, group functions, subscriptions, AI features.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
