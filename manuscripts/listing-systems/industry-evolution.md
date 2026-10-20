{id: industry-evolution}
# 3. From Newspaper Columns to Portfolios: How the Classifieds Industry Evolved

![From Newspaper Columns to Portfolios: How the Classifieds Industry Evolved — logo](listing-systems-architecture/posts/03-industry-evolution/assets/images/03-industry-evolution/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow the classifieds industry from newspaper columns to the portfolio groups of 2026 through a dated, sourced timeline. You will see what each wave of strategy left in the systems (country copies, acquired stacks, shared platforms, rebrands and carve-outs) and learn to read a group's architecture as the sediment of its history.

> **WHY THE BUSINESS CARES:** Marketplace groups are bought, merged, split and sold more often than their systems are replaced. The history explains why synergy cases routinely overestimate what a merger saves, why break-ups cost more than their spreadsheets assumed, and why the owner's capital strategy should shape the platform roadmap.

> **WHY ARCHITECTS SHOULD CARE:** Most of what a chief architect inherits was not designed; it was deposited by a strategy that has since changed. Knowing which wave created a system tells you what assumptions it carries, who will defend it and how expensive it will be to separate, share or retire.

> **KEY POINTS:**
>
> * **The industry moved in five waves, and each wave left systems behind.** After print columns came the online pioneers, portfolio building, consolidation and private-equity break-ups, each with a characteristic architecture: minimal free local sites, country copies of one codebase and acquired national stacks kept "as a separate business", shared group platforms, and finally carve-outs that had to undo the sharing.
> * **Network effects are local, so groups are portfolios of local number-ones.** Leadership is won per country and vertical, which is why acquired national leaders mostly survived while many greenfield group brands closed. The architecture follows the same logic: strong local products sit on top of whatever the group has managed to share underneath.
> * **Capital strategy sets platform topology, and it changes faster than platforms do.** Adevinta converged in 2023 and decentralized in 2025; AVIV integrated in 2021 and rowed back in 2025. A shared platform built for synergies becomes a separation cost when the owner wants to sell, so separability belongs in every group platform from the first design review.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Country Fork** — The copy-paste market-entry model of the 2000s launched each country on its own copy of the codebase, and those copies diverged into separate systems that every later improvement has to touch several times.
> * **The Acquisition Archipelago** — Portfolio groups bought national leaders and promised to run them as separate businesses, so the group still pays for several search engines, identity systems and data platforms years after the deal.
> * **The Platform Mandate** — When consolidation programs tried to converge whole product platforms across countries, the platform ran into the local differences that had made each marketplace win, and the record shows several groups reversing course within two to four years.

[Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) showed that leadership is won country by country, so marketplace groups are portfolios of local leaders. This chapter shows what building those portfolios did to the systems a Chief Architect inherits, and answers the question every review of such a landscape reaches: *why is it like this?* Why does a group run three search engines, four identity systems and a monolith from 2006? The honest answer is rarely "because someone chose it". It is usually "because a strategy that made sense at the time put it there, and the strategy changed before the system did". **A marketplace group's architecture is the sediment of its corporate history.**

The chapter traces the classifieds industry from newspaper columns through the first free websites, the country-by-country land-grabs of Schibsted, eBay and Naspers, the vertical portals, the consolidation of 2020–2023 and the private-equity take-privates and break-ups of 2024–2026. It owns two terms: the **industry timeline** used throughout the book and the **portfolio model**, the way multi-country groups are built from local marketplaces. It does not repeat the taxonomy of marketplace models ([Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy)) or the economics of liquidity, and it tells the Adevinta story only in outline; [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) tells it in full. Later chapters build on it: [Map What the Marketplace Does Before What Runs It](#business-capabilities) maps what Veldmark's brands duplicate, and [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) and [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) turn its separability rule into a method.

For each wave, the chapter gives the dated public record, then asks what the wave did to the systems. **Every company statement below carries its source and year**, and where the record is thin or old, the chapter says so. Architectural readings of real companies are labeled as inferences. The worked example is Veldmark, whose fictional history was written to mirror the industry's, so that its 2027 landscape can be read the same way.

{id: industry-evolution--setting-the-scene-at-veldmark-twenty-three-years-in-one-diagram}
## Setting the Scene at Veldmark: Twenty-Three Years in One Diagram

In her first week as Group Chief Architect, in February 2027, Ingrid Halvorsen asked each brand's engineering lead for one slide: every production system, with the year it was built and the reason it exists. Veldmark is the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)): four brands, eight countries, **€1.31 billion** of revenue in 2026 and about **1,150 engineers**. The slides came back with dates from 2004 to 2027.

Ingrid laid them out by year rather than by brand, and the landscape changed shape. The systems clustered into five layers, and each layer matched a period of Veldmark's corporate history:

| Period | What Veldmark did | What it left in the systems |
| --- | --- | --- |
| 2004–2008 | Tradeyard launched in the Netherlands (2004); **Yardstick**, the PHP monolith on MySQL, rewritten in 2006; Motorvane launched in Germany (2008) as a separate automotive brand | A monolith in a co-located Amsterdam data center that still runs Tradeyard and blocks 140 engineers |
| 2009–2014 | Tradeyard expanded by copying itself: Belgium (2009) and Portugal (2014) launched on their own copies of Yardstick; Poland (2012) came through the purchase of a local site | Four country category trees; Solr for three countries and Elasticsearch for Poland, which kept its own search after the acquisition |
| 2015–2022 | Motorvane added the Netherlands, Poland and Austria on one Kotlin service platform on AWS; Tradeyard built about 40 services on AWS around Yardstick from 2019 | Two cloud estates that share nothing; Tradeyard Poland's cars section competing with Motorvane Poland for the same dealers |
| 2023–2025 | Acquisitions: Hearthly France (2023), Keybridge (2024), Casavista in Spain (2025, rebranded Hearthly.es in 2026); a private-equity investor took majority ownership in 2025 | A third cloud (Hearthly on Google Cloud), a fourth (Keybridge on Azure), a third search engine (OpenSearch), a third data warehouse |
| 2027– | The **Common Ground** program: **€140 million** over 2027–2030 to share platforms beneath the brands | The decisions this book follows |

The board had approved Common Ground in January 2027 on a slide that said "four of everything". Ingrid's diagram said something more useful: **each "of everything" was a fossil from a different strategy**. The four identity systems were not four mistakes. They were the residue of organic launches, a country acquisition, an automotive build and two recent purchases, each of which was right, or at least defensible, when it was made.

![Cutaway of five rock strata, each holding generic system fossils from print columns to carve-outs, examined by an architect from the surface.](listing-systems-architecture/posts/03-industry-evolution/assets/images/03-industry-evolution/architecture-as-sediment.jpeg)

**Figure 1:** *A group's architecture is sediment: each wave of strategy, from print columns to break-ups, left systems behind that outlived the strategy that deposited them.*

Two questions followed. Mateus Carvalho, the Group CTO, asked which of these layers the industry's larger groups had managed to consolidate, and at what cost. Henrik de Boer, the CEO, asked a sharper one: *if our owner sells a brand in 2030, which of the platforms we are about to build will we have to take apart?* The rest of this chapter is the industry's answer to both.

{id: industry-evolution--concepts-waves-portfolios-and-sediment}
## Concepts: Waves, Portfolios and Sediment

- **Classifieds**: marketplaces whose job ends when a buyer contacts a seller (defined fully in [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy)). In print, a classified was a short paid notice in a newspaper column; online, the listing became free and the monetization moved to visibility, professional subscriptions and advertising.
- **Local number-one**: the marketplace with the largest share of audience and supply in one country and one vertical. Because network effects are local ([Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)), most of the industry's value sits in local number-ones.
- **Portfolio model**: a group strategy that owns many local marketplaces, usually one leader per country and vertical, and shares some capabilities beneath their brands. The group's value is the sum of local leaderships plus whatever the shared layer saves or enables. This chapter owns the term.
- **Copy-paste market entry**: launching a marketplace in a new country by deploying a copy of an existing marketplace's codebase and operating model, then localizing it. Fast to start, expensive later, because the copies diverge.
- **Shared platform**: capabilities built once and run for several marketplaces, from infrastructure and data to whole product stacks. [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) owns the design.
- **Convergence**: moving several marketplaces' *product* platforms (listing, search, transactions, apps) onto one platform, as distinct from sharing *enabling* layers such as cloud or data.
- **Take-private**: the acquisition of a listed company by a private-equity buyer, followed by delisting.
- **Carve-out** and **transitional services agreement (TSA)**: separating a business from its group for sale, and the contract under which the seller keeps providing shared services (hosting, software, operations) to the buyer for a period.
- **Architectural sediment**: this book's name for the systems each strategy leaves behind after the strategy itself has changed. Sediment is not a defect. It becomes a problem when nobody remembers which strategy deposited it and therefore what assumptions it carries.

The chapter divides the history into five waves. The boundaries are approximate and overlap, because different groups reached each wave at different times.

![Diagram: Five waves of classifieds strategy](listing-systems-architecture/posts/03-industry-evolution/assets/images/03-industry-evolution/fig02-five-waves-classifieds-strategy-vertical-portals.jpeg)

**Figure 2:** *Five waves of classifieds strategy. Vertical portals grew alongside the horizontals and were absorbed into portfolios; the transactional pivot runs through the consolidation wave. Each arrow is a strategic change that left the previous wave's systems in place.*

{id: industry-evolution--the-timeline-in-dated-events}
## The Timeline in Dated Events

The table is the book's reference timeline. It keeps to events with public sources; the sections that follow add the architectural reading.

| Date | Event | Source |
| --- | --- | --- |
| 1977 | *Thames Valley Trader* founded in the UK; renamed Auto Trader in 1988 | Wikipedia, Auto Trader Group (2026) |
| 1995–1996 | Craig Newmark's e-mail list for Bay Area events becomes craigslist; web-based from 1996, a company from 1999, other US and Canadian cities from 2000 | Wikipedia, Craigslist (2026) |
| 1996 | mobile.de founded in Hamburg; 50,000 listings and 1,200 dealers by 1998 | mobile.de newsroom timeline (n.d.) |
| 1998 | ImmobilienScout24 and AutoScout24 (as MasterCar.de) founded in Germany | Wikipedia, Scout24 and AutoScout24 (2026) |
| 1999 | Marktplaats founded in the Netherlands | eBay 8-K exhibit (2004) |
| 2000 | Rightmove founded by four UK estate-agency and financial groups; Gumtree founded in London | Wikipedia, Rightmove (2026); eCG brand page (2014 snapshot) |
| 2004 | eBay buys mobile.de (about €121 million, closed April 2004) and Marktplaats (about €225 million, November 2004), the latter to be run "as a separate business" | eBay SEC filings (2004) |
| 2005 | eBay launches Kijiji as a greenfield brand and buys Gumtree and LoQUo | eCG brand pages (2014 snapshots) |
| 2006 | Schibsted founds leboncoin (France) and, with Styria, willhaben (Austria); OLX founded; Zillow launches; Rightmove lists in London | Adevinta AR 2023; Wikipedia (2026) |
| 2008 | eBay buys dba.dk and Bilbasen (about US$390 million); its classifieds unit has "five major brands" in more than 20 countries | eBay (2008-10-06) |
| 2009 | eBay Kleinanzeigen launches in Germany, built "to process 10K new ads per day" | Berlin Tech Blog (2019) |
| 2010 | Naspers takes a majority stake in OLX | Wikipedia, OLX (2026) |
| 2013 | Final print edition of Auto Trader UK, after 36 years | Wikipedia, Auto Trader Group (2026) |
| 2014 | Naspers raises its OLX stake to 95% and rebrands acquired local sites to OLX across Eastern Europe | Wikipedia, OLX (2026) |
| 2015 | Auto Trader lists in London; Immowelt and Immonet combine under Axel Springer; Kleinanzeigen introduces Kafka; Marktplaats replaces eBay's Voyager search with Elasticsearch | Wikipedia (2026); Immowelt (2015); Berlin Tech Blog (2019); Marktplaats Technology (2015/2017) |
| 2016 | Naspers consolidates classifieds under OLX Group; Schibsted presents "one global product and tech organization"; Facebook launches Marketplace | Wikipedia (2026); investor-material summary (2016); Meta (2016) |
| 2017 | Marktplaats launches transactional services | Adevinta AR 2023 |
| Feb–Apr 2019 | Schibsted demerges its non-Nordic marketplaces as Adevinta, listed in Oslo | Schibsted/Vend (2019-02-25) |
| 2019–2020 | OLX buys control of Frontier Car Group (OLX Autos); OLX merges its Middle East and South Asia businesses into EMPG (39% stake) and combines letgo US with OfferUp (40% stake); Hellman & Friedman buys AutoScout24 | TechCrunch (2021); OLX Group (2020); Wamda (2020); Wikipedia (2026) |
| 25 Jun 2021 | Adevinta completes its acquisition of eBay Classifieds Group; UK competition remedies force the sale of Gumtree UK, Motors.co.uk and Shpock | Adevinta (2021) |
| 2022 | Prosus sells Avito (RUB 151 billion); Adevinta sells Gumtree Australia and its Mexican brands | Naspers (2022-10-14); Adevinta (2022-08-25) |
| 2023 | eBay Kleinanzeigen becomes Kleinanzeigen; Adevinta reorganizes by vertical and plans "a unified global platform" for its generalists; Prosus exits OLX Autos | Adevinta (2023-05-16); AR 2023; News24 (2023-03-02) |
| May 2024 | Permira- and Blackstone-led consortium completes the take-private of Adevinta | Adevinta (2024-05-29) |
| Apr 2025 | AVIV and Stepstone separate from Axel Springer under KKR and CPP Investments | KKR (2025-04-29) |
| 2025–2026 | Adevinta moves to "a decentralised, standalone operating model" and sells its Spanish business to EQT (completed 27 Feb 2026); CoStar completes the purchase of Domain; OLX buys La Centrale (€1.1 billion) and agrees to sell its Central Asian sites | Adevinta Strategic Report 2025 (2026); CoStar 10-K (2026); OLX Group (2025, 2026) |

The timeline shows two patterns before any architecture. First, **the same assets change hands repeatedly**: Gumtree has had at least three owners, mobile.de three, AutoScout24 two. Second, **the waves are short compared with the systems**. Kleinanzeigen's original platform, built in 2009, served through eBay's ownership, Adevinta's listing, its take-private and its decentralization before Kleinanzeigen began migrating users off it in 2025 ([Berlin Tech Blog, 2025](https://medium.com/berlin-tech-blog/handling-user-migration-with-debezium-apache-kafka-and-a-synchronization-algorithm-with-cycle-3c239b32326f)). A system routinely outlives two or three owners.

{id: industry-evolution--wave-0-and-wave-1-from-paid-columns-to-free-pages}
## Wave 0 and Wave 1: From Paid Columns to Free Pages

{id: industry-evolution--print-economics}
### Print economics

For most of the twentieth century, classifieds were a newspaper's most profitable pages: small paid notices for jobs, cars, homes and goods, sold by the line, with the newspaper as the only local marketplace. The listing *was* the product, and the reader paid for the paper that carried it. Specialist print titles grew alongside: Auto Trader began in 1977 as *Thames Valley Trader*, a magazine of car photographs, and published its final print edition only in June 2013, "after thirty six years" (Wikipedia, Auto Trader Group, 2026).

The architectural legacy of print is not code but **vocabulary and pricing habits**. Category columns became category trees. The idea that a professional pays per listing, or per week of visibility, survives in insertion fees and bump products. And the newspaper's habit of treating each city as its own market survives in the per-country, per-city structure of almost every classifieds platform.

{id: industry-evolution--free-local-and-minimal}
### Free, local and minimal

The pioneers inverted the print model: listings became free for private sellers, and money came from a few paid categories. Craigslist began in 1995 as Craig Newmark's e-mail list for San Francisco events, moved to the web in 1996, incorporated in 1999 and expanded to other cities from 2000; its revenue came mainly from paid job ads in selected US cities, with $25 job posts in New York and Los Angeles from August 2004 (Wikipedia, Craigslist, 2026, widely reported).

Free listings pushed down the newspapers' classified prices. Robert Seamans and Feng Zhu studied craigslist's entry into US local markets in the 2000s and found that newspapers relying heavily on classifieds saw **classified-ad rates fall by 20.7%**, with smaller effects on circulation and display-ad rates; they estimated that classified-ad buyers saved about **$5 billion** between 2000 and 2007 ([NYU Stern, 2013](https://www.stern.nyu.edu/experience-stern/faculty-research/seamans-craigslist), on a paper then forthcoming in *Management Science*).

In Europe the same years produced the national leaders that still dominate: mobile.de (1996), ImmobilienScout24 and AutoScout24 (1998), Marktplaats (1999), Rightmove and Gumtree (2000). Some were start-ups; others were founded by the incumbents the internet threatened: Rightmove's founding shareholders were Countrywide, Halifax, Royal & Sun Alliance and Connells, estate-agency and financial groups that would otherwise have been its customers (Wikipedia, Rightmove, 2026). That origin matters for architecture, because **a portal founded by its suppliers inherits a feed-first relationship with them**: agents' systems push listings in, and the portal's job is to publish them well.

{id: industry-evolution--what-wave-1-left-in-the-systems}
### What Wave 1 left in the systems

- **Minimal, monolithic stacks** built for modest scale. Kleinanzeigen's 2009 architecture was "a plain old database backend", "a search backend based on Apache Solr™ (with a Master/Slave setup)" and web servers, built "to process 10K new ads per day" ([Berlin Tech Blog, 2019](https://medium.com/berlin-tech-blog/microservices-and-kafka-part-2-b37dd08a7d8f)). By 2019 the same marketplace had 34 million live ads and up to a million new ads a day. The original design survived a hundredfold growth because it was simple; it also became the system that had to be strangled later.
- **Free listings as the default for private sellers**, which shifts the economic burden onto visibility products, professional subscriptions and advertising, and onto moderation, because free listings attract abuse. [How Listing Marketplaces Make Money](#monetization-models) and [Trust and Safety as a Platform](#trust-and-safety-architecture) pick up both threads.
- **Categories as the unit of the business.** Andrew Parker's 2010 post on "the unbundling of craigslist" showed how start-ups carved niches out of craigslist's categories, and observed that "a team of thirty-or-so people manages a top 10 ranked English-speaking website" ([Parker, 2010](http://thegongshow.tumblr.com/post/345941486/the-spawn-of-craigslist-like-most-vcs-that-focus)). Category-level competition is why taxonomy and vertical-specific schemas later became strategic ([Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies)).

{id: industry-evolution--wave-2-the-portfolio-builders}
## Wave 2: The Portfolio Builders

Between roughly 2005 and 2016, three groups turned local classifieds into international portfolios: Schibsted, eBay and Naspers (later Prosus) with OLX. They used different entry methods, and each method left a different architecture.

{id: industry-evolution--schibsted-launch-copy-localize}
### Schibsted: launch, copy, localize

Schibsted, a Norwegian media group, moved its growth focus from newspapers to online classifieds in the 2000s, anchored on FINN.no in Norway and Blocket in Sweden. Its international expansion is widely described as built on the Blocket platform; a 2012 Nieman Lab article is quoted as saying Schibsted ran classifieds in 28 countries on it. That article could not be retrieved for this book, so the claim is reported, not verified. The standard account of the playbook (launch or buy a generalist site per country, run it on a shared code base with free private listings, monetize later through verticals and advertising) is industry lore without a primary Schibsted source. Dated facts are clearer: Schibsted founded leboncoin on 28 April 2006 and willhaben in 2006 as a 50/50 joint venture with Styria (Adevinta Annual Report 2023, published 2024).

The record does show that **the federation stayed local in product and technology for a long time**, and that the tension with central scale was visible early. A Schibsted investor presentation in 2016 carried the heading "one global product and tech organization" (widely reported). In 2019, Adevinta's first annual report as a listed company named the trade-off directly: "one of our historic success formulas has been local autonomy and decentralised capacity in product and technology", while data and analytics would be centralized because "investment requirements are large and the technology is uniform" ([Adevinta Annual Report 2019, published 2020](https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf)).

The federation also produced group platforms from local inventions. FIAAS, the deployment abstraction later used across Adevinta's marketplaces, was built at FINN.no and open-sourced in early 2019; FINN.no reported 350 microservices and about 1,200 deployments a week at KubeCon Europe in 2017 (both as documented in Adevinta's 2020 talk write-up and the 2017 slides). [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) follows that thread.

> **INFERENCE, NOT DOCUMENTED:** A copy-paste entry model produces country codebases that start identical and diverge with every local change. After a few years, the group owns several related but incompatible systems: the same data model with different extensions, the same category idea with different trees, the same search engine at different versions. This is the mechanism behind **The Country Fork**, and it is consistent with the later history, in which the group's central scale had to be built as *new* shared components rather than by merging the country copies.

{id: industry-evolution--ebay-buy-the-leader-keep-the-brand}
### eBay: buy the leader, keep the brand

eBay assembled its classifieds portfolio mainly by buying national leaders and keeping their brands. It bought mobile.de in 2004 for about €121 million and Marktplaats the same year for about €225 million, stating that Marktplaats would be run "as a separate business" ([eBay 8-K exhibit, 2004](https://www.sec.gov/Archives/edgar/data/0001065088/000129993304001734/exhibit1.htm)). It added Gumtree and LoQUo in 2005, dba.dk and Bilbasen in 2008 for about US$390 million, 2dehands/2ememain in 2013 and Vivanuncios in 2015. Where it had no leader, it launched a group brand: Kijiji in 2005 in Canada, Italy and Taiwan, later in other countries, and eBay Kleinanzeigen in Germany in 2009 ([eBay, 2008](https://www.ebayinc.com/stories/news/ebay-acquires-leading-classifieds-companies-in-denmark/); eCG brand pages, 2014 snapshots).

The bought leaders mostly survived and grew; many greenfield launches were closed, renamed or sold: Kijiji Hong Kong and Taiwan closed in 2015, Kijiji China became Baixing, Kijiji India became Quikr, and eBay's Mexican brand iBazar was retired when Vivanuncios was bought (eBay, 2015; Wikipedia, Kijiji, 2026). The exception that proves the rule is eBay Kleinanzeigen, a greenfield brand that became Germany's leader, partly because it absorbed an existing Kijiji audience and launched with about 700,000 live ads.

Technically, eCG was a federation with group functions, not a single platform. Group job advertisements from 2009–2011 speak of a "sister Classifieds platform" and "a variety of eCommerce platforms that form the portfolio of the group", with reuse encouraged rather than mandated (eCG careers pages, 2009–2011 snapshots). The clearest documented shared element is the inheritance from the parent. Marktplaats ran **Voyager**, a search engine "developed internally by eBay in the USA", from around 2008; by 2015 eBay "has moved on from Voyager several years ago" and it "has almost become a black box for us". eCG companies jointly evaluated replacements and chose Elasticsearch; Marktplaats migrated itself in three months with two or three developers, behind unchanged interfaces, with zero downtime ([Marktplaats Technology, 2015, republished 2017](https://medium.com/marktplaats-technology/replacing-our-legacy-search-engine-with-elasticsearch-4ad03aeceb3d)).

Two lessons travel. **Coordinate the technology choice across brands, but let each brand migrate itself.** And **a parent's platform can become orphaned legacy faster than local code**, because its owner moves on and local knowledge decays.

{id: industry-evolution--naspers-and-olx-the-global-roll-up}
### Naspers and OLX: the global roll-up

OLX was founded in 2006 as a classifieds alternative outside the United States. Naspers took a majority stake in 2010 and 95% in 2014, the year it rebranded acquired local sites to OLX across Romania, Bulgaria, Kazakhstan, Belarus, Hungary, Poland and Indonesia; in 2016 it consolidated its classifieds under OLX Group in Amsterdam (Wikipedia, OLX, 2026, widely reported). The vertical brands kept their own names: Otomoto and Otodom in Poland, Standvirtual and Imovirtual in Portugal, Autovit and Storia in Romania. In 2018 the group described itself as "a network of leading classifieds platforms in 45 markets" ([OLX Tech, 2018](https://tech.olx.com/understanding-language-through-search-78ea37be7ac8)).

Rebranding to one name implies a stronger push toward shared product than eBay's keep-the-brand strategy. The public engineering record, however, documents shared practices and some shared code more than one global platform: one frontend repository serving three brands in 2026, a centralized learning-to-rank repository with per-brand configuration in 2025, and the standardization of user identification "across 71 services" at OLX Motors in 2024–2025 ([OLX Tech, 2026](https://tech.olx.com/empowering-innovation-through-structure-93c15614f6d3)). That last item is a direct trace of sediment: user identity had been per platform, and consolidation had to fix it first.

{id: industry-evolution--the-vertical-portals-grow-up}
### The vertical portals grow up

While the horizontals built portfolios, the verticals became the industry's most profitable businesses. Vertical portals (property, motors, jobs) monetize professionals through subscriptions and depth products, and the leaders earn very high margins: Rightmove reported a **70%** underlying operating margin on £425.1 million of revenue for 2025, and Autotrader a 70% operating margin for the year to March 2026 ([Rightmove, 2026](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf); [Autotrader, 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf)). Both report that most of their traffic arrives directly rather than through paid channels.

Verticals were also the assets portfolios most wanted to own. eBay bought mobile.de; Axel Springer assembled the property portals that became AVIV, combining Immowelt and Immonet in 2015 and buying Meilleurs Agents for €200 million in 2019 ([Immowelt, 2015](https://www.immowelt.de/ueberuns/presse/pressemitteilungenkontakt/immowelt-group/immowelt-und-immonet-schliessen-sich-zusammen/); FrenchWeb, 2019); OLX built and bought motors and property brands per country. Their architecture differs from the horizontals' because their supply arrives through professional feeds, their items have authoritative identities (a vehicle identification number, an address) and their data products, such as price evaluations and valuations, are part of what they sell ([Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements)).

{id: industry-evolution--what-wave-2-left-in-the-systems}
### What Wave 2 left in the systems

| Entry method | Example | Typical architecture left behind |
| --- | --- | --- |
| Copy the codebase into a new country | Schibsted federation (industry account) | Diverged country copies; per-country category trees and data models; the **Country Fork** |
| Buy the national leader, keep it separate | eBay with Marktplaats, mobile.de | Self-sufficient national stacks with their own search, identity, data and billing; the **Acquisition Archipelago**, accepted on purpose |
| Launch a group brand on group technology | Kijiji, eBay Kleinanzeigen | Platforms built by a group team; fragile where the brand did not reach leadership |
| Buy and rebrand to one name | OLX in Eastern Europe | Brand unity ahead of platform unity; identity and data consolidation work deferred |
| Build or buy verticals per country | mobile.de, Otomoto, Immowelt | Feed ingestion, vertical schemas and valuation data per country, deeply local by necessity |

Each method was a reasonable way to win local leadership quickly, and local leadership was what created the value, so the table is not a ranking. **The architecture cost was deferred, not avoided.**

{id: industry-evolution--wave-3-consolidation}
## Wave 3: Consolidation

From around 2016, the portfolio builders turned to integrating what they owned. Three forces drove it: the cost of running many stacks, the rising expectations of users (apps, personalization, payments, AI-assisted search) that each local team could not meet alone, and deals that combined portfolios of comparable size.

{id: industry-evolution--the-adevintaebay-classifieds-deal}
### The Adevinta–eBay Classifieds deal

The largest was Adevinta's acquisition of eBay Classifieds Group, announced on 21 July 2020 for US$2.5 billion in cash plus about 540 million Adevinta shares, which left eBay with about 44% of Adevinta's capital. It completed on 25 June 2021, with a claimed footprint of number-one positions in 16 countries and targeted run-rate cost synergies of **€130–165 million after three years** ([Adevinta, 2021](https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/)).

Competition law shaped the result before any integration began. The UK Competition and Markets Authority found that Shpock and Gumtree competed closely in UK generalist classifieds; the undertakings required the sale of Gumtree UK with Motors.co.uk and of Shpock, and "Adevinta and eBay have offered to provide transitional services" to the buyers ([CMA, 2021](https://assets.publishing.service.gov.uk/media/606de28fe90e076f520fecdb/Adevinta-eBay_-_Decision_that_UILs_offer_may_be_acceptable.pdf)). Within about eighteen months Adevinta also sold its Australian, Mexican and South African horizontals, focusing on "five core European markets: Benelux, France, Germany, Italy and Spain" ([Adevinta, 2022](https://adevinta.com/press-releases/adevinta-asa-ade-adevinta-announces-sale-of-gumtree-australia-carsguide-and-autotrader-australia/)).

Integration then proceeded layer by layer. Adevinta's 2023 annual report describes consolidating infrastructure "to a single public cloud vendor for our EU5 businesses", plans to "close three of four data centre footprints", and a history of consolidating "enabling capabilities such as cloud and data, and overarching elements such as chat and moderation". The integration of eBay Classifieds cost €69 million in 2023, and the rebrand of eBay Kleinanzeigen to Kleinanzeigen another €15 million (Adevinta Annual Report 2023, published 2024). The rebrand alone shows how far sediment reaches: the old domain was to "remain accessible for several more years" ([Adevinta, 2023](https://adevinta.com/press-releases/adevintas-eBay-kleinanzeigen-is-now-kleinanzeigen/)).

**Sharing the enabling layers worked and paid**, at least while the portfolio held together. Adevinta's internal Kubernetes platform served "more than 4,000 developers" in 2023 and ran "over 2,000 Kubernetes nodes and 30 clusters across 25 marketplaces" in 2024; experimentation went from roughly ten tools across 22 marketplaces to one ([Adevinta tech blog, 2023](https://adevinta.com/techblog/transparently-providing-arm-nodes-to-4000-engineers/); [2024](https://adevinta.com/techblog/the-karpenter-effect-redefining-our-kubernetes-operations/); [2024](https://adevinta.com/techblog/from-ten-to-one-streamlining-experimentation-tooling-at-adevinta/)).

In 2023 Adevinta went further and set out to achieve **convergence of the product platform itself**. It decided to stop "individually addressing local market customer needs — such as the full transactional journey, AI-assisted search and modern approaches to first-party advertising", and "Kleinanzeigen, leboncoin and global teams embarked on transforming the two platforms into a unified global platform to support Adevinta's generalist marketplaces" (Adevinta Annual Report 2023). The convergence spanned two countries, languages and legal regimes. In May 2024 the project was "progressing well and according to plan"; no later public source confirms that it was delivered (Adevinta, 2024).

{id: industry-evolution--regional-mergers-and-joint-ventures}
### Regional mergers and joint ventures

OLX consolidated differently, by merging regional businesses into larger local players and keeping minority stakes. In June 2020 it contributed dubizzle and its Middle East and South Asia operations to Emerging Markets Property Group for a 39% stake; in March 2020 it combined letgo's US business with OfferUp for 40%; in 2020 its Brazilian joint venture with Adevinta bought Grupo ZAP for about R$2.9 billion ([Wamda, 2020](https://www.wamda.com/index.php/en/2020/06/empg-reveals-details-merger-olx); [OLX Group, 2020](https://www.olxgroup.com/news/olx-brazil-completes-the-acquisition-of-100-of-grupo-zap/)). Architecturally, a merger into another operator is the cleanest exit: the merged business runs on the partner's platform, and the group keeps equity, not systems.

Axel Springer's property business took the integrate-first path. When AVIV appointed a chief technology officer with multi-country platform experience in 2021, its CEO said "we are aligning our tech roadmap across the organization to create a European real estate marketplace" ([Online Marketplaces, 2021](https://onlinemarketplaces.com/?p=37137)).

{id: industry-evolution--the-transactional-pivot-runs-through-the-wave}
### The transactional pivot runs through the wave

In the same years the horizontals moved toward payments and shipping for goods, and **payments became the main product capability the consolidators wanted to build once**. Marktplaats launched transactional services in 2017 and shipping in 2019; leboncoin launched a transactional model in some generalist categories in 2019; eBay Kleinanzeigen launched "Sicher bezahlen" for all users in October 2020; Adevinta's group transactional revenue reached €103 million in 2023, about 6% of the total (Adevinta Annual Reports 2019 and 2023; onlinemarketing.de, 2020). OLX described its Pay&Ship flow in 2023, and Prosus recorded "the de-prioritisation of pay-and-ship in Europe" two years later ([OLX Tech, 2023](https://tech.olx.com/machine-learning-for-delivery-time-estimation-1-591c8df849a0); Prosus FY25 results, 2025). Recommerce specialists built the model from the start: Vinted reported **€10.8 billion** of gross merchandise value and **€1.1 billion** of revenue for 2025 on "vertically-integrated shipping and payment infrastructure" ([Vinted, 2026](https://company.vinted.com/newsroom/financial-results-2025)). [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) owns the pivot.

{id: industry-evolution--what-wave-3-left-in-the-systems}
### What Wave 3 left in the systems

- **Shared enabling platforms** (cloud landing zones, Kubernetes, data, experimentation, media, moderation services) with real fleet economics, and with the coupling that comes with them: one upgrade, many tenants.
- **Partially converged product platforms**, whose state at the end of the wave is often not public.
- **Transitional-services dependencies** wherever a brand was sold while running on group components. The CMA remedy depended on them; so did the sale of Gumtree Australia, which Adevinta promised to support "during the transition".
- **Rebrand residue**: redirect estates, token-based design systems and identity migrations. mobile.de's Android team reported in 2025 that a rebrand "took only two weeks to implement once the base refactoring was done", after removing "technical debt from 8 years ago" ([Berlin Tech Blog, 2025](https://medium.com/berlin-tech-blog/rebranding-on-android-apps-behind-the-scenes-57b8a58c294a)).

{id: industry-evolution--wave-4-take-privates-focus-and-break-ups}
## Wave 4: Take-Privates, Focus and Break-Ups

From 2022 the cost of capital rose, and the industry's owners changed their minds about breadth.

**Focus and retreat at OLX.** Prosus sold Avito in Russia for RUB 151 billion in October 2022 and announced its exit from OLX Autos, its inventory-holding car-trading business, in March 2023, after the business had reached $1.6 billion of revenue in the year to March 2022, just over half of classifieds revenue, while losing money ([Naspers, 2022](https://www.naspers.com/news-insights/regulatory-updates/2022/disposal-of-avito-group); [News24, 2023](https://www.news24.com/fin24/companies/prosus-looks-to-ditch-olx-autos-business-as-second-hand-car-market-slows-20230302)). India and Indonesia were sold in 2023, Uzbekistan and Kazakhstan agreed for sale in 2025. By the year to March 2026, OLX operated in seven markets, earned US$992 million of revenue at a 48% adjusted EBITDA margin, and had bought La Centrale in France for €1.1 billion ([OLX Group, 2026](https://www.olxgroup.com/?p=5024); [Online Marketplaces, 2026](https://www.onlinemarketplaces.com/articles/olx-revenue-climbs-to-992m-as-prosus-folds-classifieds-into-europe/)). From 45 markets in 2018 to seven in 2026 is the starkest public example of a group concluding that **local leadership in a few markets beats global breadth**.

**The Adevinta take-private and break-up.** A consortium led by Permira and Blackstone offered NOK 115 per share in November 2023 and completed the take-private in May 2024. In July 2024 work began on a new operating model "empowering local marketplaces". By 2025 the group had "evolved from a centralised structure to a decentralised, standalone operating model… This transition has included the ramp-down of central functions, the transfer of key capabilities, the localisation of intellectual property, and the realignment of reporting structures" ([Adevinta Strategic Report 2025, published 2026](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf)). It sold its willhaben stake in 2025 and its Spanish business to EQT, completed on 27 February 2026; EQT sold the property portals Fotocasa and Habitaclia on to Scout24 ([Scout24, 2025](https://www.scout24.com/en/news-media/news/detail/scout24-acquires-spanish-online-real-estate-platforms-fotocasa-and-habitaclia)). The same report notes that cloud emissions "more than doubled", mainly because decentralization "required parallel running of central and local services during a transitional period". **Undoing a shared platform costs real money, and for a while you pay for both.**

The outcome of mobile.de's sale process is not public as of October 2026. The Financial Times reported in October 2025 that Adevinta was exploring an IPO or a sale at up to about €10 billion (as relayed by PYMNTS, 2025). In August 2026 mobile.de's own press release still called it an Adevinta subsidiary, while the German competition authority's October 2026 clearance of its purchase of Carwow's German business named "Oak Germany Buyer GmbH" as mobile.de's parent ([Bundeskartellamt, 2026](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html)).

**The AVIV reversal.** AVIV and Stepstone became separate joint ventures majority-owned by KKR and CPP Investments on 29 April 2025, with Axel Springer keeping about 10% ([KKR, 2025](https://media.kkr.com/news-details?news_id=3ae6964b-af1f-4893-a221-d5bc7e32ce75)). In a December 2025 interview, the interviewer (not AVIV) said that AVIV had rowed "back on its plans for a fully integrated platform for all its European portals", and Immowelt's new head explained that "AVIV has strengthened the autonomy of its local businesses", using group functions "where they create clear advantages… sometimes local and sometimes cross-group" ([Online Marketplaces, 2025](https://www.onlinemarketplaces.com/articles/interview-new-immowelt-boss-theo-mseka-on-challenges-and-plans-for-the-german-market/)). A sale of Yad2, AVIV's Israeli marketplace, to Apax was signed the same month. What the integrated platform consisted of, and how far it got, is not public.

**Platform buyers keep buying.** The consolidation logic did not disappear; it moved to owners who integrate *into* a platform rather than building one across peers. CoStar completed its purchase of Domain in Australia in August 2025 and said it was "ready to apply that same proven playbook in Australia" (CoStar, 2025). AutoScout24, owned by Hellman & Friedman since 2020, migrated "110 AWS accounts across 4 business units" of Trader in Canada into its own AWS organization in 2025 ([AutoScout24, 2025](https://tech.autoscout24.com/blog/posts/aws-trader-migration/)).

> **INFERENCE, NOT DOCUMENTED:** For owners pursuing break-up value, a shared product platform is a liability at exit: it creates transitional services, intellectual-property questions and double running costs. The same shared platform that a synergy case valued in 2021 became a separation cost in 2025. The documented pattern does not say centralization was wrong; it says **platform topology has to match the capital strategy**, and that the capital strategy can change within two or three years.

![Diagram: The centralize–decentralize swing in Adevinta's own words, 2019–2026](listing-systems-architecture/posts/03-industry-evolution/assets/images/03-industry-evolution/fig03-centralize-decentralize-swing-adevinta-s-own.jpeg)

**Figure 3:** *The centralize–decentralize swing in Adevinta's own words, 2019–2026. Each step was justified by the ownership and strategy of its moment; the systems built in one step became the inheritance, or the separation cost, of the next.*

{id: industry-evolution--reading-a-group-s-architecture-as-sediment}
## Reading a Group's Architecture as Sediment

The waves give an architect a practical tool: for each major system, ask **which wave deposited it, and under what assumption about ownership and sharing**. The answers predict behavior better than the technology does.

| Layer of sediment | Assumption it carries | Typical symptom in 2027 | What to do with it |
| --- | --- | --- | --- |
| Pioneer monolith (Wave 1) | One country, one team, modest scale | Single deployable; slow releases; schema nobody fully understands | Strangle by capability; never "rewrite and switch" |
| Country copies (Wave 2, copy-paste) | Countries are similar enough to share a codebase once, then diverge | Same concept implemented several ways; fixes built per country | Converge reference data first (taxonomy, attributes), code later |
| Acquired national stacks (Wave 2, buy-and-keep) | The acquisition stays a separate business | Duplicate search, identity, data, billing; local pride | Share beneath the product only where the layer is uniform and expensive |
| Inherited parent technology | The parent keeps investing | Orphaned components; knowledge in another company | Replace early, coordinated across brands, migrated per brand |
| Shared enabling platforms (Wave 3) | The portfolio stays together | Upgrade blast radius; tenants depending on incidental behavior | Treat as products with tenancy, cost allocation and exit paths |
| Converged product platforms (Wave 3) | Markets' needs overlap enough to share product | Local workarounds; feature requests queuing at the center | Re-examine per capability; keep local edges local |
| Carve-out residue (Wave 4) | A separation will happen once, quickly | Transitional services that last years; parallel running costs | Design separability in advance, not at signing |

![Diagram: The loop behind the timeline](listing-systems-architecture/posts/03-industry-evolution/assets/images/03-industry-evolution/fig04-loop-behind-timeline-ownership-sets-platform.jpeg)

**Figure 4:** *The loop behind the timeline. Ownership sets platform topology; platforms and local stacks outlive the strategy that created them; that sediment then sets the cost of the next deal, which changes the ownership again. The architect's leverage is in making the sediment cheap to separate.*

{id: industry-evolution--in-practice-veldmark-s-history-read-as-sediment}
## In Practice: Veldmark's History, Read as Sediment

Veldmark's history is fictional, but it was written to follow the industry's waves, and Ingrid's February 2027 diagram can be read with the table above.

**Wave 1: the pioneer monolith.** Tradeyard launched in the Netherlands in 2004, when the founding family's regional publishing business moved its classified pages online. Yardstick, the 2006 PHP rewrite on MySQL, was built for one country and a few hundred thousand listings. In 2026 Tradeyard Netherlands alone carried **6.1 million** live listings, and Yardstick remained a single deployable for **140 engineers**, released twice a week, in a co-located Amsterdam data center. Its assumption, one country and one team, is the reason the Common Ground plan strangles it capability by capability (insertion flow out in Q2 2028, search in Q4 2028, decommissioned at the end of 2029) instead of rewriting it.

**Wave 2: copies and an acquisition.** Belgium (2009) and Portugal (2014) launched on copies of Yardstick, each with its own database and deployment. Between 2016 and 2018 the copies were folded back into one Yardstick codebase, still with a database and deployment per country; the merge is where Yardstick's roughly 2,600 country branches come from (see [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms)). Poland (2012) came through the purchase of a local classifieds site that was rebranded Tradeyard and moved onto Yardstick's code, but kept its own Elasticsearch search because the migration was never finished. The result is in the 2027 numbers: four country category trees with **1,420**, **1,380**, **980** and **760** leaf categories, **3,900** distinct attribute keys of which 41% are used on fewer than 0.1% of listings, and about **six weeks** to add a category. That is **The Country Fork** in reference data, which is why the group taxonomy and attribute service ([Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies)) comes before any attempt to share Tradeyard's code across countries.

**Wave 2, vertical: Motorvane.** Motorvane launched in Germany in 2008 as a separate automotive brand rather than a Tradeyard category, because its supply was dealers with feeds, not private sellers with photographs. Its 2017–2020 rebuild as about 120 Kotlin services on AWS, and its expansion to the Netherlands, Poland and Austria on that one platform, is the vertical-portal pattern: deeply specific ingestion and data, shared across countries within the vertical. The sediment shows in Poland, where Tradeyard's cars section and Motorvane Poland were selling to the same dealers under two different models by 2027 ([Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy) describes how the overlap was resolved).

**Wave 3 and Wave 4 at once: acquisitions under a new owner.** Veldmark bought Hearthly France in 2023, Keybridge in 2024 and Casavista in Spain in 2025, and a private-equity investor became majority owner in 2025. Each acquisition brought its own cloud, search engine and data warehouse. Unlike the industry's consolidators of 2021, Veldmark started its consolidation program *after* its change of owner, which makes Henrik's question, "what will we have to take apart?", a design input rather than an afterthought.

Ingrid's analysis of the inventory produced a table she showed the board in March 2027:

| Capability | Copies in 2027 | Wave that created the copies | Common Ground decision | Separability rule |
| --- | --- | --- | --- | --- |
| Identity | 4 | Every wave | Veldmark ID, one login with brand profiles (approved June 2027, rollout 2028) | Per-brand profiles and tenant-scoped data, so a brand can be cut out with its users ([Who Is on the Other Side? Identity and Verification](#identity-and-verification)) |
| Search | 3 engines | Wave 1 (Solr), Wave 2 acquisition (Elasticsearch, PL), Wave 4 acquisition (OpenSearch) | Shared OpenSearch platform for Tradeyard and Hearthly by end of 2028; Motorvane stays on Elasticsearch until 2029 | One cluster set per brand, indexes rebuildable from the event stream |
| Taxonomy and attributes | 4 Tradeyard trees plus vertical schemas | Wave 2 copies | Group taxonomy and attribute service (October 2027) | Per-brand trees on one service; schemas exportable |
| Events | 4 technologies | Every wave | Kafka on Confluent Cloud, listing event contract v1 (July 2027) | Topics keyed by brand; consumers registered |
| Data warehouses | 3 | Waves 2–4 | Group data platform | Per-brand accounts and data products with contracts |
| Product catalog and entitlements | 4 | Every wave | One service by Q2 2028 | Catalog content owned by each brand |
| Keybridge platform | 1 (Azure) | Wave 4 | Stays separate and neutral | Already separate by design |

The last column is the lesson of Wave 4 applied in advance. Every shared platform in Common Ground is specified with **tenant-scoped data, per-brand accounts and cost centres, exportable contracts and a documented exit path**, because the owner that approved the program is, by its nature, a future seller. The run-cost target of **€38 million per year** by 2030 is treated as a business case that must survive the sale of any one brand, not as a synergy that assumes the portfolio is permanent.

![Left, fused brand modules tearing cables when one is lifted out; right, a cabinet of brand drawers where one slides out cleanly with its data and accounts.](listing-systems-architecture/posts/03-industry-evolution/assets/images/03-industry-evolution/separable-by-design.jpeg)

**Figure 5:** *Because the owner that funds a shared platform is a future seller, every Common Ground platform carries tenant-scoped data, per-brand accounts and a documented exit path, so a brand can leave like a drawer, not a demolition.*

{id: industry-evolution--trade-offs-growth-strategies-and-their-architecture-bills}
## Trade-offs: Growth Strategies and Their Architecture Bills

Each wave's growth strategy sent an architecture bill that arrived later.

| Strategy | Speed to local leadership | Architecture left behind | When it is the right choice | When it backfires |
| --- | --- | --- | --- | --- |
| Greenfield launch on a copy of an existing codebase | Fast to start, slow to win | Diverging country copies | Similar markets; a team that can keep copies aligned; a plan to converge reference data early | When the copies diverge for years and every improvement is built several times |
| Greenfield launch on a group platform | Slow to start | One platform, group-owned | The group platform is mature and markets are similar | When the brand does not reach leadership, the platform's cost has no market under it (Kijiji outside Canada) |
| Buy the local leader, keep it separate | Immediate | A full national stack per acquisition | Strong leaders, very different markets, short holding horizon | When the group wants scale benefits it never designed for |
| Buy and integrate onto a group platform | Immediate, then a long migration | Converged platforms and transitional dependencies | A buyer with a proven platform and a long horizon (CoStar with Domain, AutoScout24 with Trader) | When local differences were the reason the target won |
| Regional merger into another operator | Immediate, with diluted control | Equity, not systems | Markets where the group is number two | When control matters more than exposure |
| Vertical spin-out from a horizontal | Slow | Separate vertical stack, possible overlap with the horizontal's category | Categories with professional supply and data products | When the horizontal's category and the vertical compete for the same customers |
| Convergence of whole product platforms | Slow, large | One product platform for several brands | Same model, same supply type, same legal regime, stable ownership | When ownership or strategy changes before convergence completes |

A second trade-off sits underneath: **how much to share, given the capital strategy**.

| Topology | What is shared | Best fit for | Cost at exit |
| --- | --- | --- | --- |
| Federation | Practices, standards, some tools | Short holding horizons; very different markets | Low |
| Shared enabling layers | Cloud, data platform, CI/CD, media, moderation tooling | Most groups, most of the time | Moderate, if tenancy and accounts are clean |
| Shared capability services | Identity, messaging, search platform, catalog and entitlements, event backbone | Groups with a long horizon or a credible exit path per brand | Moderate to high; depends on separability by design |
| Converged product platform | Listing, search, apps, transactions | One model across similar markets, stable owner | High: transitional services, IP splits, parallel running |

Adevinta's 2019 rule, "centralise where investment requirements are large and the technology is uniform", remains the best single default in the public record. The swings that followed suggest a second rule: **share whatever you can separate cheaply, and be explicit about what you cannot**.

{id: industry-evolution--vertical-differences}
## Vertical Differences

The waves hit verticals differently, and that is visible in their architectures today.

| Dimension | General classifieds | Real estate | Automotive | Jobs and recommerce |
| --- | --- | --- | --- | --- |
| Pioneer origin | Start-ups and newspaper spin-offs; free private listings | Often founded by or with agents; feed-first | Print magazines and start-ups; dealer-driven | Job boards from print; recommerce born transactional |
| How portfolios grew | Copy-paste launches and rebranded acquisitions | Country-by-country acquisitions of leaders | Acquisitions of national leaders | Separate groups (Stepstone) or recommerce specialists (Vinted) |
| Consolidation outcome | Shared enabling layers; product convergence attempted and reversed | Integration attempted and rowed back (AVIV); integration into a platform buyer (CoStar–Domain) | Strong national stacks; selected cross-border platforms (AutoScout24) | Vinted merged its per-country "portals" into one marketplace with per-user consent (2022) |
| Why local wins | Language, consumer habits, local trust | Agent software ecosystems, disclosures, address systems, contract norms | Dealer systems, vehicle data, financing partners | Labour law and taxonomies (jobs); carriers and payment methods (recommerce) |
| Typical sediment | Pioneer monoliths and country forks | Feed adapters per country and portal-owned agent software | Feed importers, vehicle decoders, price models per country | Order, payment and logistics state; legal-entity-per-country data |

Real estate and recommerce sit at opposite ends. In real estate, **local differences are structural**: each country has its own professional software ecosystem and mandatory disclosures, which is the most plausible reading of why AVIV's integrated platform was scaled back. Vinted shows the opposite case: a recommerce marketplace whose model is the same everywhere could merge its country "portals", but even it had to migrate per user and obtain consent, because each country had been a separate legal entity with separate databases ([Vinted Engineering, 2022](https://vinted.engineering/2022/03/03/portal-merge/)). [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) develops the comparison.

{id: industry-evolution--failure-modes}
## Failure Modes

Misreading the history produces seven recurring mistakes.

**Copying the last wave's answer.** A new chief architect who arrives during a consolidation wave proposes convergence; one who arrives during a break-up proposes autonomy. Both are copying a fashion rather than reading their own group's ownership, markets and sediment.

**The synergy case that counts platforms as savings.** Deal models often count the retirement of duplicate platforms in year two or three. The public record shows long tails: rebrands that keep old domains for years, integration costs that recur (€69 million at Adevinta in 2023), transitional services for divested brands. A synergy that depends on platform convergence should carry the convergence's risk, not a straight-line saving.

**Building shared platforms with no exit path.** A shared platform without tenant-scoped data, per-brand accounts and cost allocation turns every later sale into a carve-out project. Adevinta's report of parallel running during decentralization is the visible cost; the invisible one is the deal that does not happen because separation is too expensive.

**Treating acquired stacks as temporary.** "We will migrate them next year" is the sentence that creates **The Acquisition Archipelago**. Acquired stacks that are not on a dated, funded plan become permanent, and their teams build around them.

**Forcing convergence where local differences are the product.** Real-estate ingestion, dealer feeds, local payment methods and regulatory disclosures are where local marketplaces win. A converged platform that flattens them invites **The Platform Mandate**: local teams route around it, and the group pays for both.

**Forgetting inherited dependencies.** Components inherited from a former parent, a former sister brand or a TSA keep running quietly until their owner stops supporting them. Marktplaats' Voyager is the documented example.

**Rebrands priced as marketing projects.** A brand change touches domains, search-engine equity, identity, design systems, app stores and payment descriptors. mobile.de's two-week app rebrand was possible only after a refactoring that removed eight years of debt.

{id: industry-evolution--the-chief-architect-s-view}
## The Chief Architect's View

At group scale, history is an input to four standing decisions.

**Know the owner's horizon, and design to it.** A family owner, a listed company and a private-equity fund imply different holding periods and different exit routes. The architecture function should ask for the capital strategy explicitly, in writing, and should revisit platform topology when it changes. This is not disloyal; it is the information without which a platform roadmap is a guess. At Veldmark, a decision record from March 2027, Ingrid's second month, states the assumption plainly: any brand may be sold within five years.

**Make separability a non-functional requirement.** Every shared platform should be specified with tenant-scoped data, per-brand cloud accounts and cost centres, exportable contracts and a tested exit path. A rule I use: **no shared platform goes live without a written answer to "how would we hand this brand's slice to a buyer in six months?"** If the answer is a transitional services agreement, the agreement's scope belongs in the design.

**Separate the enabling layers from the product edge.** The public record is consistent: sharing infrastructure, data platforms, media, moderation tooling and experimentation paid; converging whole product platforms across countries was slow and frequently reversed. Decide per capability, using Adevinta's 2019 rule as the default and the separability rule as the constraint. [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) and [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) turn this into a method.

**Keep a sediment register.** For each major system: the wave that created it, the assumption it carries, its owner, its consumers and its fate (keep, share, converge, retire, separate). It is a short table, reviewed with the architecture roadmap. It turns "why is it like this?" from folklore into a decision record, and it tells the next owner what they are buying.

What to watch: the share of engineering spent on duplicated capabilities; the number of transitional or cross-brand dependencies a sale would break; run costs per brand that can be stated without allocation arguments; and, after each deal, whether the platform plan was updated within a quarter.

{id: industry-evolution--questions-to-ask}
## Questions to Ask

Take these into a strategy review or a due-diligence meeting:

1. For each major system, which strategy created it, and does that strategy still hold?
2. What is the owner's expected holding period, and which exit routes (sale of the group, sale of a brand, listing) does the platform roadmap need to support?
3. If one brand were sold next year, which shared services would it lose, and how long would a transitional services agreement need to run?
4. Which of our shared platforms are enabling layers, and which are product platforms? Is the distinction deliberate?
5. Which acquired stacks are on a dated, funded plan, and which are "temporary" without one?
6. Are any components inherited from a former parent or sister company, and who still maintains their knowledge?
7. Does our synergy case count platform retirements as savings, and does it carry the risk of the convergence they depend on?
8. Where are local differences the reason our marketplaces win, and does our platform plan protect them?
9. What did the last rebrand or migration actually cost, including redirects, identity and design-system work, and is that cost in the next plan?

{id: industry-evolution--from-history-to-capabilities}
## From History to Capabilities

The history explains how the systems got here; it does not say what they should become. To decide what to share, converge or keep local, a group first needs a description of what its marketplaces *do* that is independent of the systems that happen to do it today. [Map What the Marketplace Does Before What Runs It](#business-capabilities) builds that description: a capability map for listing marketplaces, the value streams that cross it, and a heat map that shows where Veldmark's four brands duplicate one another and where their differences are the point.

{id: industry-evolution--sources-and-evidence}
## Sources and Evidence

{id: industry-evolution--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Introducing Adevinta, an international family of local digital marketplaces](https://vend.com/news/introducing-adevinta-an-international-family-of-local-digital-marketplaces) — Schibsted/Vend, 2019. The demerger and Adevinta's 2019 footprint.
- [Adevinta Annual Report 2019](https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf) — Adevinta, 2020. Local autonomy as a "historic success formula"; centralized data and analytics; leboncoin's transactional launch.
- [Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf) — Adevinta, 2024. Verticalization, the unified-platform decision, cloud consolidation, integration and rebrand costs, willhaben and leboncoin founding, transactional history.
- [Acquisition of eBay Classifieds Group complete](https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/) — Adevinta, 2021. Deal terms, synergy target, Shpock and Denmark sales.
- [Adevinta announces sale of Gumtree Australia, CarsGuide and Autotrader Australia](https://adevinta.com/press-releases/adevinta-asa-ade-adevinta-announces-sale-of-gumtree-australia-carsguide-and-autotrader-australia/) — Adevinta, 2022. Focus on five core European markets.
- [Adevinta's eBay Kleinanzeigen is now Kleinanzeigen](https://adevinta.com/press-releases/adevintas-eBay-kleinanzeigen-is-now-kleinanzeigen/) — Adevinta, 2023. The rebrand and the old domain kept for years.
- [Completion of the voluntary offer for Adevinta ASA](https://adevinta.com/press-releases/adevinta-asa-ade-completion-of-the-voluntary-offer-for-all-issued-and-outstanding-ordinary-class-a-shares-in-adevinta-asa/) — Adevinta, 2024. The take-private.
- [Strategic Report 2025, Aurelia UK Feederco Ltd](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf) — Adevinta, 2026. Decentralization, IP localization, parallel running, Spanish sale.
- Adevinta tech blog: [ARM nodes for 4,000 engineers](https://adevinta.com/techblog/transparently-providing-arm-nodes-to-4000-engineers/) (2023), [The Karpenter effect](https://adevinta.com/techblog/the-karpenter-effect-redefining-our-kubernetes-operations/) (2024), [From ten to one: experimentation tooling](https://adevinta.com/techblog/from-ten-to-one-streamlining-experimentation-tooling-at-adevinta/) (2024). Scale of shared enabling platforms.
- [How to build a PaaS for 1500 engineers](https://varoa.net/paas/infrastructure/platform/kubernetes/cloud/2020/01/02/talk-how-to-build-a-paas-for-1500-engineers.html) — Galo Navarro, 2020. FIAAS's FINN.no origin.
- [eBay 8-K exhibit on the Marktplaats acquisition](https://www.sec.gov/Archives/edgar/data/0001065088/000129993304001734/exhibit1.htm) — eBay, 2004. Price and "separate business".
- [eBay acquires leading classifieds companies in Denmark](https://www.ebayinc.com/stories/news/ebay-acquires-leading-classifieds-companies-in-denmark/) — eBay, 2008. Five brands in more than 20 countries.
- [eBay Classifieds expands in Mexico, acquires Vivanuncios](https://www.ebayinc.com/stories/news/ebay-classifieds-expands-mexico-acquires-vivanuncios/) — eBay, 2015. iBazar retired.
- eBay Classifieds Group brand and careers pages (Internet Archive snapshots, 2009–2014) — eCG. Brand founding and acquisition dates; plural platforms.
- [Replacing our legacy search engine with Elasticsearch](https://medium.com/marktplaats-technology/replacing-our-legacy-search-engine-with-elasticsearch-4ad03aeceb3d) — Marktplaats Technology, 2015 (republished 2017). Voyager as inherited, orphaned search.
- [Microservices and Kafka, part 2](https://medium.com/berlin-tech-blog/microservices-and-kafka-part-2-b37dd08a7d8f) — Berlin Tech Blog (Kleinanzeigen), 2019. The 2009 architecture and its growth.
- [Rebranding on Android apps: behind the scenes](https://medium.com/berlin-tech-blog/rebranding-on-android-apps-behind-the-scenes-57b8a58c294a) — Berlin Tech Blog (mobile.de), 2025. Rebrand cost after refactoring.
- [Handling user migration with Debezium, Apache Kafka and a synchronization algorithm](https://medium.com/berlin-tech-blog/handling-user-migration-with-debezium-apache-kafka-and-a-synchronization-algorithm-with-cycle-3c239b32326f) — Berlin Tech Blog (Kleinanzeigen), 2025. Per-user migration off the legacy platform.
- [Introducing Marketplace](https://about.fb.com/news/2016/10/introducing-marketplace-buy-and-sell-with-your-local-community/) — Meta Newsroom, 2016. Facebook Marketplace launch.
- Prosus FY25 results booklet — Prosus, 2025. De-prioritization of pay-and-ship in Europe.
- [Understanding language through search](https://tech.olx.com/understanding-language-through-search-78ea37be7ac8) — OLX Tech, 2018. 45 markets.
- [Empowering innovation through structure](https://tech.olx.com/empowering-innovation-through-structure-93c15614f6d3) — OLX Tech, 2026. User identification standardized across 71 services.
- [Machine learning for delivery time estimation](https://tech.olx.com/machine-learning-for-delivery-time-estimation-1-591c8df849a0) — OLX Tech, 2023. Pay&Ship.
- [OLX Brazil completes the acquisition of Grupo ZAP](https://www.olxgroup.com/news/olx-brazil-completes-the-acquisition-of-100-of-grupo-zap/) — OLX Group, 2020. Regional consolidation.
- [OLX Group FY26 results](https://www.olxgroup.com/?p=5024) — OLX Group, 2026. Seven markets; divestments.
- [Disposal of Avito Group](https://www.naspers.com/news-insights/regulatory-updates/2022/disposal-of-avito-group) — Naspers, 2022. Avito sale.
- [Rightmove FY2025 results](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf) — Rightmove, 2026. Revenue and margin.
- [Autotrader FY2026 results](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf) — Autotrader Group, 2026. Margin and traffic mix.
- [Immowelt und Immonet schließen sich zusammen](https://www.immowelt.de/ueberuns/presse/pressemitteilungenkontakt/immowelt-group/immowelt-und-immonet-schliessen-sich-zusammen/) — Immowelt, 2015. AVIV's German formation.
- [KKR announcement on the Axel Springer classifieds separation](https://media.kkr.com/news-details?news_id=3ae6964b-af1f-4893-a221-d5bc7e32ce75) — KKR, 2025. AVIV and Stepstone ownership.
- [Scout24 acquires Fotocasa and Habitaclia](https://www.scout24.com/en/news-media/news/detail/scout24-acquires-spanish-online-real-estate-platforms-fotocasa-and-habitaclia) — Scout24, 2025. Onward sale after the Spanish carve-out.
- [Migrating Trader's AWS accounts](https://tech.autoscout24.com/blog/posts/aws-trader-migration/) — AutoScout24, 2025. Integration into a platform buyer.
- CoStar Group Form 10-K for 2025 — CoStar, 2026. Completion of the Domain acquisition.
- [Financial results 2025](https://company.vinted.com/newsroom/financial-results-2025) — Vinted, 2026. Recommerce scale and integrated shipping and payments.
- [Portal merge](https://vinted.engineering/2022/03/03/portal-merge/) — Vinted Engineering, 2022. Per-country legal entities merged with per-user consent.

{id: industry-evolution--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Adevinta/eBay: decision that undertakings may be acceptable](https://assets.publishing.service.gov.uk/media/606de28fe90e076f520fecdb/Adevinta-eBay_-_Decision_that_UILs_offer_may_be_acceptable.pdf) — UK Competition and Markets Authority, 2021. Divestment remedies and transitional services.
- [mobile.de / Carwow clearance](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html) — Bundeskartellamt, 2026. Parent entity named; dealer multi-homing.

{id: industry-evolution--research-and-practitioner-sources}
### Research and practitioner sources

- [New research looks at Craigslist's damaging blow to local newspapers](https://www.stern.nyu.edu/experience-stern/faculty-research/seamans-craigslist) — NYU Stern, 2013. Seamans and Zhu's findings on classified-ad rates.
- [The spawn of craigslist](http://thegongshow.tumblr.com/post/345941486/the-spawn-of-craigslist-like-most-vcs-that-focus) — Andrew Parker, 2010. Category unbundling.
- [Craigslist](https://en.wikipedia.org/wiki/Craigslist), [Auto Trader Group](https://en.wikipedia.org/wiki/Auto_Trader_Group), [Rightmove](https://en.wikipedia.org/wiki/Rightmove), [OLX](https://en.wikipedia.org/wiki/OLX), [Scout24](https://en.wikipedia.org/wiki/Scout24), [Kijiji](https://en.wikipedia.org/wiki/Kijiji) — Wikipedia, accessed 2026. Founding dates and ownership history (secondary sources).
- Schibsted Q3 2016 investor presentation, as summarized by financialfilings.com — 2016. "One global product and tech organization" (secondary summary; the primary slide was not retrieved).
- [eBay Kleinanzeigen "Sicher bezahlen" launch](https://onlinemarketing.de/?p=214785) — onlinemarketing.de, 2020. Launch date of the protected-payment flow.
- [MeilleursAgents racheté par Axel Springer pour 200 millions d'euros](https://www.frenchweb.fr/meilleursagents-rachete-par-axel-springer-pour-200-millions-deuros/377533) — FrenchWeb, 2019. AVIV's valuation acquisition.
- [AutoScout24](https://de.wikipedia.org/wiki/AutoScout24) — Wikipedia (German), accessed 2026. Founding as MasterCar.de and the 2020 sale to Hellman & Friedman.
- [EMPG reveals details of merger with OLX](https://www.wamda.com/index.php/en/2020/06/empg-reveals-details-merger-olx) — Wamda, 2020. OLX's regional merger.
- [Prosus classifieds group OLX shuts down Berlin's Frontier Car Group](https://techcrunch.com/2021/03/29/prosus-classifieds-group-olx-shuts-down-berlins-frontier-car-group-to-focus-olx-autos-on-latam-and-asia/) — TechCrunch, 2021. OLX Autos origin.
- [Prosus looks to ditch OLX Autos](https://www.news24.com/fin24/companies/prosus-looks-to-ditch-olx-autos-business-as-second-hand-car-market-slows-20230302) — News24/Fin24, 2023. OLX Autos exit.
- [AVIV appoints Brent McLean as CTO](https://onlinemarketplaces.com/?p=37137) — Online Marketplaces, 2021. Integration intent.
- [Interview: new Immowelt boss Theo Mseka](https://www.onlinemarketplaces.com/articles/interview-new-immowelt-boss-theo-mseka-on-challenges-and-plans-for-the-german-market/) — Online Marketplaces, 2025. The integrated-platform reversal.
- [OLX revenue climbs to $992m](https://www.onlinemarketplaces.com/articles/olx-revenue-climbs-to-992m-as-prosus-folds-classifieds-into-europe/) — Online Marketplaces, 2026. OLX FY26 figures and La Centrale.
- [Adevinta considers IPO or sale of mobile.de](https://www.pymnts.com/?p=3112865) — PYMNTS, citing the Financial Times, 2025. mobile.de dual track.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
