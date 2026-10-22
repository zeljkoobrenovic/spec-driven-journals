{id: meet-veldmark}
# Meet Veldmark: Four Brands, One Platform to Build

![Meet Veldmark: Four Brands, One Platform to Build — logo](listing-systems-architecture/posts/meet-veldmark/assets/images/meet-veldmark/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Meet Veldmark Group, the fictional marketplace group this book follows: its four brands and their business models, its volumes, its 2027 systems landscape, the people who run it, the eight problems it starts 2027 with, the Common Ground platform program approved to solve them, and the recurring worked examples whose numbers every chapter shares.

> **WHY THE BUSINESS CARES:** Veldmark earns €1.31 billion a year from four different ways of turning listings into money. Its owner wants growth and a lower run cost at the same time, and the group pays for most of its capabilities four times.

> **WHY ARCHITECTS SHOULD CARE:** Veldmark's difficulty is variety, not scale. Three clouds, three search engines, four identity systems and a PHP monolith from 2006 must serve private sellers, dealers and agencies in eight countries without slowing any marketplace down, and that is the Chief Architect's problem in miniature.

> **KEY POINTS:**
>
> * **Veldmark is a fictional composite, not a disguised company.** It generalizes patterns that commonly appear in European marketplace groups, so the book can show real architectural tensions with consistent numbers without describing any real group's internals. Every name, figure, system choice and event on this page is invented.
> * **One group, four marketplace physics.** Tradeyard sells visibility to private sellers and takes a fee on payments, Motorvane sells dealer packages and leads, Hearthly sells agency subscriptions and valuation data, and Keybridge sells software to agents who list on Hearthly's competitors. The same word, "listing", carries different supply, money and risk in each.
> * **Common Ground shares platforms, not products.** The €140 million program (2027–2030) builds identity, trust and safety, search, events, taxonomy, entitlements and data beneath the brands, retires the Yardstick monolith by the end of 2029 and must cut run costs by €38 million a year by 2030, while every brand keeps its own name, user experience and go-to-market.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Deal-Shaped Architecture** — Hearthly, its Spanish predecessor Casavista and Keybridge each arrived with a complete stack, and in 2027 the group still runs four identity systems, four trust-and-safety stacks and three data warehouses.
> * **The Copy-Paste Country** — Tradeyard's Belgian and Portuguese sites run on their own copies of Yardstick, and all four countries keep separate category trees and rule sets, so a fraud rule written on a Sunday night reaches Belgium on Wednesday and Poland and Portugal never.
> * **Ghost Inventory** — the Rotterdam city bike, sold on Monday evening, still appears in 214 alert e-mails on Tuesday morning, and it is the book's spine example for a reason.

This book tests its argument against **one fictional group, detailed enough to be realistic and consistent enough to be followed across fifty chapters.** The usual alternatives fail in opposite ways: a toy marketplace, one listing table and a search box, is too simple to show why the hard decisions are hard, and a real company's internals cannot be verified and its choices do not transfer. This page is the group's reference. The failure patterns of [Unlisted: Fifteen Ways Listing Systems Go Wrong](#where-listing-systems-go-wrong) appear here as Veldmark's 2027 problems, and every chapter from Part I on opens with a scene whose people, systems and numbers come from this page.

**Veldmark Group is fictional.** It is a composite that borrows *patterns* common in the classifieds industry: a horizontal brand that grew country by country on one codebase, a vertical brand built for professional supply, acquisitions that arrived with their own clouds, a transactional product added on top of a contact marketplace, and a private-equity owner who wants both growth and efficiency. It is **not a portrait of any real company**. Nothing on this page or in any chapter is a claim about how a real group is built; the vendor products it runs are real, but its use of them is invented. The real companies the book discusses, such as Adevinta, OLX, Kleinanzeigen, Rightmove or Auto Trader, appear under their own names, with dated sources, and never as Veldmark.

{id: meet-veldmark--the-group-at-a-glance}
## The Group at a Glance

Veldmark is a privately held, multi-country, multi-vertical marketplace group headquartered in **Rotterdam**, with engineering hubs in **Lisbon**, **Warsaw**, **Lyon** and **Düsseldorf**. Since **2025** a private-equity investor holds the majority; a founding-family trust holds a minority stake. The owner wants growth and a lower run cost at once, and will one day sell the group or parts of it, which makes clean boundaries between brands a strategic asset.

| Measure (fiscal 2026 = calendar 2026) | Value |
| --- | --- |
| Revenue | **€1.31 billion** |
| Adjusted EBITDA | about **€470 million** (about 36% of revenue) |
| Employees | about **5,200**, of whom about **1,450** in product and technology, including about **1,150 engineers** |
| Countries and marketplaces | **8** countries: Netherlands, Belgium, Poland, Portugal, Germany, Austria, France and Spain; **ten** country marketplaces (Tradeyard 4, Motorvane 4, Hearthly 2) plus Keybridge in three countries. The Netherlands, Belgium, Poland, France and Spain each host more than one brand |
| Live listings | about **17.25 million** |
| Monthly active users | about **57 million** across the three marketplaces (31M + 14M + 12M; users of several brands are counted once per brand) |
| Shared group services | **Veldmark Ads**, group finance on SAP S/4HANA, and little else |

The margin is typical of mature classifieds: the marketplaces never hold the goods, and most revenue is subscriptions and visibility fees with low marginal cost. The last row matters most to this book. With almost nothing shared beneath its brands, the group pays for search, moderation, identity, media and data several times over.

{id: meet-veldmark--how-veldmark-came-to-be}
## How Veldmark Came to Be

Veldmark's history, like everything else about it, is fictional, but its shape follows the industry's (the documented history is in [From Newspaper Columns to Portfolios: How the Classifieds Industry Evolved](#industry-evolution)).

| Year | Event |
| --- | --- |
| **2004** | Tradeyard launches in the Netherlands as a free general-classifieds site. |
| **2006** | Yardstick, Tradeyard's PHP application on MySQL, replaces the first version; it is still the core of Tradeyard in 2027. |
| **2008** | Motorvane launches in Germany, its main market, as an automotive marketplace for dealers and private sellers; the Netherlands, Poland and Austria follow later. |
| **2009–2014** | Tradeyard expands by copying itself: Belgium (2009) and Portugal (2014) launch on their own copies of Yardstick, each with its own database and deployment; Poland (2012) comes through the purchase of a local classifieds site, moved onto Yardstick's code but keeping its own Elasticsearch search. Each country has its own category tree. |
| **2023** | Veldmark acquires the French real-estate portal that becomes **Hearthly**. |
| **2024** | Veldmark acquires **Keybridge**, an agent CRM in France, Belgium and Spain. **Tradeyard Safe Deal** launches in the Netherlands. |
| **2025** | Veldmark acquires **Casavista** in Spain. The private-equity investor takes a majority stake. Safe Deal launches in Belgium. |
| **2026** | Casavista is rebranded **Hearthly.es**. Safe Deal launches in Poland. |
| **January 2027** | The board approves the **Common Ground** program. |

Each phase left a layer in the systems: four category trees in country copies of one monolith, a separate automotive stack in another AWS region, Google Cloud and Azure from the acquisitions, and a payments product on top of a contact marketplace that was never designed to know when something was sold.

{id: meet-veldmark--four-brands-four-business-models}
## Four Brands, Four Business Models

Veldmark runs four businesses and one shared advertising unit. They differ in who supplies the listings, where the marketplace's job ends and how the money is made, the classification [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy) develops.

| Brand | What it is | Markets | Business model | 2026 revenue |
| --- | --- | --- | --- | --- |
| **Tradeyard** | Horizontal general classifieds: goods, plus small cars, property and jobs sections in Poland and Portugal | NL (since 2004), BE (2009), PL (2012), PT (2014) | Free private listings with paid visibility (value-added services, VAS: bumps, top listing, highlight), professional-seller subscriptions, insertion fees in some categories (Polish vehicles and property), transactional fees from **Safe Deal** | **€410M**: VAS €150M, pro subscriptions €135M, Safe Deal €75M, insertion fees €50M |
| **Motorvane** | Automotive marketplace: cars, vans, motorbikes | DE (main, since 2008), NL, PL, AT | Dealer subscriptions (packages with listing slots), depth products, lead and financing referral fees, private-seller listing fees | **€360M**: dealer subscriptions €238M, depth/VAS €52M, leads and financing referrals €40M, private-seller fees €30M |
| **Hearthly** | Real-estate portal: sale, rent, new builds | FR (acquired 2023), ES (former Casavista, acquired 2025, rebranded 2026) | Agency subscriptions, new-build developer campaigns, valuation data and seller leads through **Valuo**, rental services (tenant application files) | **€395M**: agency subscriptions €270M, new-build campaigns €55M, Valuo data and leads €40M, rental services €30M |
| **Keybridge** | CRM and listing-management software for real-estate agents; publishes agency listings to many portals, including Hearthly's competitors ("multi-diffusion") | FR, BE, ES (acquired 2024) | SaaS subscriptions from **9,800** agency customers | **€45M** |
| **Veldmark Ads** | Group advertising unit selling across all brands | all | Display, native and sponsored listings; retail media for car makers, banks and insurers | **€100M** |

The five lines add up to €1.31 billion: Tradeyard about 31% of revenue, Hearthly 30%, Motorvane 27%, Veldmark Ads 8% and Keybridge 3%.

![Four different buildings on one shared ground plate: a goods market hall, a car showroom, a real-estate office and a software office that also sends listings to outside portals, labeled Tradeyard, Motorvane, Hearthly and Keybridge.](listing-systems-architecture/posts/meet-veldmark/assets/images/meet-veldmark/four-marketplace-physics.jpeg)

**Figure 1:** *One group, four marketplace physics: Tradeyard sells visibility to private sellers, Motorvane packages and leads to dealers, Hearthly subscriptions and valuation data to agencies, and Keybridge software to agents who also list on Hearthly's competitors.*

Four features of the brand portfolio recur throughout the book.

- **Tradeyard is mostly a contact marketplace with a transactional product inside it.** Most listings end at a message; Tradeyard never learns whether the sofa was sold. **Tradeyard Safe Deal** adds in-platform payment with shipping or "pay at pickup" for private sales in the Netherlands, Belgium and Poland, but not Portugal. Payments run on **Adyen for Platforms**: Adyen is the licensed party, and Veldmark holds no payment licence ([Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments)). The buyer pays a protection fee of **5% of the item price plus €0.70**. In 2026 Safe Deal handled **11.6 million** transactions worth about **€1.02 billion** of gross merchandise value (GMV), and earned **€75 million**: about €59 million of buyer fees and about €16 million of shipping-label margin.
- **Motorvane and Hearthly are professional-supply businesses.** Motorvane's **21,400 dealers** supply 91% of its listings, 88% of them through feeds from dealer management systems (DMS); Hearthly's **36,500 agencies** supply 84% of its listings through feeds from about **160 real-estate software vendors**. Their customers are businesses with contracts, invoices and lead expectations, which makes much of their architecture business-to-business software.
- **Valuo turns listings into a data product.** Valuo, Hearthly's automated valuation model (AVM) in France, is trained on France's public transaction records (the DVF open data, *demandes de valeurs foncières*, published by the French tax administration) together with Hearthly's own listing data; it earns money through data products and seller leads routed to agencies, and a Spanish version is planned for 2028.
- **Keybridge must stay neutral.** Keybridge publishes its customers' listings to Hearthly and to Hearthly's competitors. Agencies fear that Veldmark will use their CRM data to favor Hearthly, which makes neutrality a design constraint on every data flow between Keybridge and the group.

Veldmark Ads is the exception to "four of everything": one ad stack, on Google Ad Manager with Prebid header bidding, sells inventory on all three marketplaces ([Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms)).

{id: meet-veldmark--volumes-every-design-is-sized-against}
## Volumes Every Design Is Sized Against

2026 figures, rounded.

| Metric | Value |
| --- | --- |
| Live listings | **17.25M**: Tradeyard 13.2M (NL 6.1M, BE 2.4M, PL 3.6M, PT 1.1M); Motorvane 1.45M; Hearthly 2.6M (FR 1.9M, ES 0.7M) |
| New listings per week | Tradeyard **2.3M** (NL 1.05M, BE 0.42M, PL 0.62M, PT 0.21M); Motorvane 210,000; Hearthly 240,000 |
| Monthly active users | Tradeyard 31M (NL 14.2M, BE 5.1M, PL 8.9M, PT 2.8M); Motorvane 14M; Hearthly 12M |
| Supply mix | Tradeyard: 78% of new listings from private sellers. Motorvane: 91% from 21,400 dealers, 88% of dealer listings via DMS feeds. Hearthly: 84% via feeds from about 160 software vendors, 36,500 agencies |
| Search | Group average **9,000 queries/s**; peak **31,000 queries/s** on Sunday evenings, 20:00–22:00 CET; Tradeyard carries about 70% of queries |
| Saved searches and alerts | **46 million** active saved searches (Tradeyard 31M, Motorvane 8M, Hearthly 7M); about **38 million** alert notifications a day by push and e-mail |
| Media | about **6.4 billion** stored images, **1.8 billion** of them at Hearthly; about 9.5 million new images a day |
| Organic search | Tradeyard: about **40 million** indexed URLs; **46%** of web sessions start there |
| Moderation | Tradeyard: 94% of new-listing decisions automated, 6% (about 138,000 a week) to human review; about **210 moderators** across the brands, in-house and outsourced |
| Duplicates | Hearthly France: 1.9M listings describe about **1.12 million** distinct properties, **1.7** listings per property |
| Taxonomy | Tradeyard: four country trees with 1,420 (NL), 1,380 (BE), 980 (PL) and 760 (PT) leaf categories; **3,900** distinct attribute keys, 41% of them used on fewer than 0.1% of listings |

Two caveats. The **Sunday-evening peak is a Veldmark illustration**, not an industry statistic; the documented public example of a weekly peak, Rightmove's, is in [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale). And ratios matter more than totals: Tradeyard Netherlands and Portugal have almost the same monthly users per live listing (2.3 and 2.5), yet a new Dutch listing gets its first contact in a median of 2.6 hours and a Portuguese one in 19. [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) explains why, and why every latency target in this book names the liquidity metric it protects.

{id: meet-veldmark--the-systems-landscape}
## The Systems Landscape

The 2027 baseline estate is the product of that history, with almost nothing shared between the brands' stacks.

![Diagram: Veldmark's 2027 baseline](listing-systems-architecture/posts/meet-veldmark/assets/images/meet-veldmark/fig02-veldmark-s-2027-baseline-three-marketplaces.jpeg)

**Figure 2:** *Veldmark's 2027 baseline: three marketplaces on three stacks and two clouds, an agent CRM on a third cloud, and only advertising and finance shared beneath them.*

| Area | Tradeyard | Motorvane | Hearthly | Keybridge |
| --- | --- | --- | --- | --- |
| Core application | **Yardstick**: PHP monolith (since 2006) on MySQL in a co-located Amsterdam data center; about 40 microservices on AWS (eu-west-1, EKS) built since 2019 around it | About 120 Kotlin/JVM microservices on AWS (eu-central-1, EKS) | Go and TypeScript services on **Google Cloud** (GKE, europe-west1); Hearthly.es still partly on Casavista's code, including its login and review tool | .NET on **Microsoft Azure** |
| Search | **Solr 8**, self-hosted, for NL, BE and PT; **Elasticsearch 7** for PL | **Elasticsearch 8** on Elastic Cloud | **OpenSearch**, self-managed on GKE | — |
| Events | RabbitMQ inside Yardstick; Kafka (Amazon MSK) for the new services | Kafka (Amazon MSK) | Google Pub/Sub | Azure Service Bus |
| Identity | Own accounts | Own accounts; separate dealer-portal login | Own accounts; Hearthly.es on Casavista's login | Own accounts |
| Trust and safety | In-house rules engine and ML models (NL/BE); outsourced moderation queues (PL/PT) | Dealer business checks (KYB) at contract signature only; private-seller checks | In-house rules; manual review of new agencies | — |
| Data | Snowflake | Snowflake (separate account and model) | BigQuery | Azure Synapse |
| Media | Own image service plus CloudFront | S3 plus CloudFront | Google Cloud Storage plus Cloud CDN | — |

Three facts in this landscape shape most of the book.

- **Yardstick does almost everything for Tradeyard.** Insertion, moderation hooks, category trees, fee rules, Solr indexing, alert crons and most web pages live in one PHP application and one MySQL schema; its `ads` table has 214 columns read by 38 modules. It deploys **twice a week** and blocks about **140 Tradeyard engineers**. The newer AWS services read its data through RabbitMQ, replica queries and nightly exports, and nobody had a full list of those readers until 2027 ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)).
- **Motorvane is modern but self-contained.** Its risk is the opposite of Tradeyard's: it has little reason to share, and a group platform that serves it worse than its own stack would be a regression.
- **Hearthly and Keybridge kept their clouds.** Any group platform must work across clouds or accept that some brands reach it through a bridge.

{id: meet-veldmark--the-people}
## The People

Each person owns something the architecture depends on, and most of the book's tensions are between their legitimate goals. All are fictional.

| Name | Role | What they own and want |
| --- | --- | --- |
| **Ingrid Halvorsen** (she/her) | Group Chief Architect | The book's point of view; joined on **Monday 1 February 2027**. Reports to Mateus; chairs the architecture advice forum; owns the capability map, the context map and the cross-brand decision records. Has influence, not command, over the brands' teams. |
| **Henrik de Boer** (he/him) | Group CEO | Answers to the private-equity owner; wants growth without eating the Common Ground budget. |
| **Mateus Carvalho** (he/him) | Group CTO | Sponsor of Common Ground's engineering work; Ingrid's line manager; owns the cloud decision. |
| **Noor Hassan** (she/her) | Group Chief Product Officer | Owns the cross-brand product roadmap, from the bikes split to the AI proposals. |
| **Olivier Petit** (he/him) | VP Monetization | Owns pricing and paid products: VAS, dealer packages, agency tiers, Valuo leads. |
| **Daan Visser** (he/him) | Tradeyard engineering director | Owns Yardstick; knows where every workaround lives and why. |
| **Katarzyna Nowak** (she/her) | Tradeyard Poland general manager | Runs Tradeyard's most varied country: goods, cars, property and jobs. |
| **Felix Brandt** (he/him) | Motorvane CTO | Owns Motorvane's stack, dealer feeds and Dealer Hub, the dealer portal; skeptical of shared platforms built for Tradeyard's sofas. |
| **Claire Fontaine** (she/her) | Hearthly CEO | Owns Hearthly France and Spain; wants agencies' trust and Valuo's growth. |
| **Julien Marchand** (he/him) | Hearthly CTO | Owns Hearthly's Google Cloud estate, its feeds and its duplicate problem. |
| **Emma Laurent** (she/her) | Keybridge founder and general manager | Owns Keybridge's neutrality promise to 9,800 agencies; resists any data flow that could break it. |
| **Aisha Rahman** (she/her) | Group Head of Trust & Safety | Owns policy, moderation and fraud response; builds the shared trust-and-safety platform. |
| **Tomasz Wiśniewski** (he/him) | Head of the group search platform | Formerly Tradeyard's search lead; owns the move to a shared search platform. |
| **Priya Raman** (she/her) | Head of Data & ML | Owns the data platforms, metric definitions and model governance. |
| **Lucía Ortega** (she/her) | Group Data Protection Officer and regulatory lead | Owns GDPR, Digital Services Act (DSA) reporting and the privacy side of every design. |
| **Sven Lindqvist** (he/him) | Principal engineer, event platform | Owns the group event backbone and the Listing event contract. |
| **Yara Mendes** (they/them) | Head of Platform Engineering | Owns the shared platform teams: publication, taxonomy and attributes, entitlements, notifications. |

The recurring customers, private seller **Femke** (she/her) in Rotterdam, dealer **Autohaus Ruhrblick** in Essen and agency network **Agence Rhône Habitat** in Lyon, are fictional too.

{id: meet-veldmark--eight-problems-veldmark-starts-2027-with}
## Eight Problems Veldmark Starts 2027 With

When Ingrid arrives, the marketplaces work and the group is profitable, but its effort and duplication grow faster than the business. Eight problems define her starting position; most are instances of patterns from [Unlisted: Fifteen Ways Listing Systems Go Wrong](#where-listing-systems-go-wrong).

1. **Four of everything.** Four identity systems, four trust-and-safety stacks, three search engines, three clouds, four product catalogs, three data warehouses. *(Deal-Shaped Architecture.)*
2. **Six minutes to searchable.** On Tradeyard, a new listing takes **6 minutes** at the 95th percentile (p95) from submission to searchable, because moderation and indexing work in batches. The target is **90 seconds** p95 by the end of 2028.
3. **Six weeks for a category.** Tradeyard's four country trees cannot share features, and a new category takes about **6 weeks**. The target is **2 days**. *(The Category Straitjacket, The Attribute Junkyard.)*
4. **Duplicates at Hearthly.** With **1.7 listings per property** in France, buyers see the same flat repeatedly and agencies argue about whose copy ranks first. *(Seeing Double.)*
5. **Payment-link phishing on Tradeyard.** Scammers posing as buyers send fake Safe Deal payment pages through messaging in the Netherlands and Belgium. *(Fast Mail for Fraudsters.)*
6. **Yardstick blocks Tradeyard.** Every Common Ground capability Tradeyard needs must first be extracted from it.
7. **Keybridge neutrality.** Agencies fear that Veldmark uses their Keybridge data to favor Hearthly. If they believe it, they leave, and the group loses a business and its standing with agencies at once.
8. **Overlap in Poland.** Tradeyard Poland's cars section competes with Motorvane Poland for the same dealers: about 2,900 Polish dealers hold accounts on both, and about 40% pay both. *(Deal-Shaped Architecture, inside the group.)*

![Four separate islands, labeled Tradeyard, Motorvane, Hearthly and Keybridge, each with its own identity, trust, search and data towers and its own cloud, joined only by one thin shared bridge.](listing-systems-architecture/posts/meet-veldmark/assets/images/meet-veldmark/four-of-everything.jpeg)

**Figure 3:** *Four of everything: in 2027 the brands run four identity systems, four trust-and-safety stacks, three search engines and three clouds, with little more than advertising and finance shared beneath them.*

None of these is a technology problem alone. The phishing exists because messaging was built as a feature, not as a trust surface; the neutrality problem because a commercial promise has no architecture yet; and the Polish overlap is a portfolio decision that systems can make easier or harder, but cannot make.

{id: meet-veldmark--the-common-ground-program}
## The Common Ground Program

In **January 2027** Veldmark's board approved **Common Ground**: **€140 million** over **2027–2030** to build shared platform capabilities beneath the brands. It has three goals.

- **Shared platform capabilities**: a group identity (**Veldmark ID**), trust and safety, media, a search platform, messaging, a product catalog and entitlements, an event backbone, a data platform, and a taxonomy and attribute service.
- **Retire Yardstick by the end of 2029**, through a strangler migration: the insertion flow moves out in the second quarter of 2028, search in the fourth quarter of 2028, and the monolith is decommissioned at the end of 2029.
- **Cut run costs by €38 million a year by 2030.**

Its governing principle is **share platforms, not products.** The marketplaces keep their brands, user experience and go-to-market; the group shares the capabilities beneath them. The hard design work is deciding which *part* of each capability is shared. A shared trust-and-safety pipeline can serve local policies; a shared search engine can serve brand-specific relevance; a shared entitlement ledger can serve brand-owned packages and prices.

![Diagram: "Share platforms, not products"](listing-systems-architecture/posts/meet-veldmark/assets/images/meet-veldmark/fig04-share-platforms-not-products-brands-keep.jpeg)

**Figure 4:** *"Share platforms, not products": the brands keep what buyers and sellers see, Common Ground builds what lies beneath, and Keybridge stays outside by design.*

Common Ground is also a governance change. In **April 2027** the group adopted architecture principles and set up the **architecture advice forum**, a weekly, open meeting that gives advice rather than approvals, and made **decision records mandatory for cross-brand decisions**. Much of the book's Veldmark story happens in that forum.

The decisions the chapters rely on, in order:

| Date | Decision or milestone | Chapter that works it |
| --- | --- | --- |
| Jan 2027 | Common Ground approved | this page |
| 31 Mar 2027 | Group capability map: 10 level-1 areas, 54 level-2 and 212 level-3 capabilities; five overlaps | [Map What the Marketplace Does Before What Runs It](#business-capabilities) |
| Mar 2027 | Keybridge stays a separate, neutral SaaS: no Keybridge agency data used by Hearthly for ranking or sales targeting; annual independent review | [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts), [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) |
| Apr 2027 | Architecture principles and the advice forum; decision records mandatory | [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering) |
| May 2027 | Common Ground context map: 19 bounded contexts, one owning team each | [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) |
| Jun 2027 | Veldmark ID approved (one login, brand-specific profiles; rollout 2028); Ranking policy v1 | [Who Is on the Other Side? Identity and Verification](#identity-and-verification), [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) |
| 1 Jul 2027 | Group event backbone on **Kafka on Confluent Cloud** (AWS); **Listing event contract v1** live with a schema registry | [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) |
| 14 Sep 2027 | Shared search platform on **Amazon OpenSearch Service** for Tradeyard (all countries) and Hearthly by the end of 2028; Motorvane stays on Elasticsearch until a 2029 review | [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) |
| Oct 2027 | Group taxonomy and attribute service live, Tradeyard first; entitlement service **Tally** designed; group retention schedule | [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies), [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements), [System of Record and Read Models: Listing Data Management](#listing-data-management) |
| 1 Nov 2027 | The **bikes split** (city, e-bikes, cargo, kids) goes live | [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies), [What Did They Mean? Query Understanding and Autocomplete](#query-understanding) |
| Nov 2027 | Shared trust-and-safety platform live for Tradeyard NL and BE | [Trust and Safety as a Platform](#trust-and-safety-architecture) |
| 2028 | Veldmark ID rollout; Hearthly Spain on the shared trust-and-safety platform (Q1); one group product catalog and entitlement service (Q2); Yardstick's insertion flow moved out (Q2) and search moved (Q4); 90-second publication target | [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration), [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) |
| End 2029 | Yardstick decommissioned | [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) |
| 2030 | Run-cost reduction of €38 million a year | [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) |

![Diagram: Common Ground's four plateaus](listing-systems-architecture/posts/meet-veldmark/assets/images/meet-veldmark/fig05-common-ground-s-four-plateaus-each.jpeg)

**Figure 5:** *Common Ground's four plateaus; each must leave every marketplace working on its own, not only as a step toward the next.*

**AWS is the group's primary cloud** from 2027. **Hearthly stays on Google Cloud through 2028** and **Keybridge stays on Azure**; the book treats a multi-cloud group as normal, not as a failure.

{id: meet-veldmark--the-recurring-worked-examples}
## The Recurring Worked Examples

Five stories recur throughout the book. Their facts never change, so a reader can follow one listing across many chapters.

| Example | Canonical facts | Where it does most work |
| --- | --- | --- |
| **The Rotterdam city bike** (Tradeyard NL) | Femke lists a used city bike for **€240** on **Sunday 7 March 2027 at 19:42 CET**. Searchable at **19:48**, the six-minute baseline. Matches **312** saved searches; first contact **19:55**; **14** conversations within 24 hours. At **20:11** a "buyer" sends a fake Safe Deal payment link from a domain registered that day; Femke reports it at **20:19**; the account is suspended at **20:26**; a new rule withholds **37** similar messages. On **Monday 8 March** a Safe Deal "pay at pickup" order reserves the bike at **14:02**; it sells for **€225** with a buyer fee of **€11.95** (5% × €225 + €0.70). Marked sold at **18:10**, removed from search at **18:11** — but the alert digest assembled at 17:30 still features it in **214** e-mails at 07:00 on Tuesday. | [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate), [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline), [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts), [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads), [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) |
| **The Essen Volkswagen Golf** (Motorvane DE) | A 2021 Golf 1.5 TSI, **48,000 km**, **€21,900**, from dealer **Autohaus Ruhrblick** through its DMS feed on **Wednesday 14 April 2027**. VIN decoding fills **31** attributes; the market-value model estimates **€22,800** ("good price"). **23 raw leads in 10 days** (14 e-mails, 7 calls, 2 test-drive bookings), **19** after removing repeat contacts from the same buyers. Price cut to **€21,400** on **Thursday 22 April** triggers price-drop alerts to **1,180** watchers. Sold **Thursday 29 April**; the feed's removal arrives **26 hours** later. | [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion), [Recommendations for Inventory That Disappears](#recommendations), [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) |
| **The Lyon apartment** (Hearthly FR) | A three-room (T3) **68 m²** flat in Lyon 7e for sale at **€389,000**, energy class (DPE, the French energy performance diagnostic) **D**. Listed in **May 2027** by **three agencies**, through two real-estate software vendors and Keybridge; one is **Agence Rhône Habitat**, a network of **14 branches**. Entity resolution clusters the three listings into one canonical property. Valuo estimate: **€372,000–€401,000**. | [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution), [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts), [Searching by Place: Map, Polygon and Commute Search](#map-search), [Models in Production: ML Platforms and Use Cases](#ml-platform) |
| **The Barcelona fake-rental ring** (Hearthly ES) | In **July 2027**, **26** accounts post **180** fake rental listings in Eixample using photos stolen from real listings, priced about **35%** below market, asking for deposits by bank transfer outside the platform. Detected through perceptual-hash matches against existing listings plus price anomalies; **63** people report losses of about **€71,000** before takedown. | [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention), [Photos Sell: Media Pipelines for Listings](#media-pipeline), [Who Is on the Other Side? Identity and Verification](#identity-and-verification), [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) |
| **The Sunday-evening brown-out** (Tradeyard NL) | **Sunday 17 January 2027, 20:35 CET**: search p99 latency rises from about **400 ms** to about **7 s** for **48 minutes**, and about **9%** of searches fail. Causes: a TV campaign, a scheduled reindex job and Solr cache eviction at the weekly peak. | [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture), [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale) |

The **Rotterdam bike is the book's spine.** In about 24 hours one €240 listing passes through a dozen systems and exposes a different weakness in almost every one: batch delays behind the six minutes, a messaging check that ran after delivery, a rule that reached Belgium three days late, an analytics extract that recorded the sale as "expired", and a digest that never asked whether the bike was still for sale. Six months later, Femke's erasure request finds **seven** copies of the listing. None of this is exotic; it is what a successful classifieds platform looks like after twenty years of reasonable local decisions.

The **Golf** plays the same role for professional supply: a complete but slow feed, a lead count the dealer disputes, a carousel that recommends a sold car, and a "Pro 150" package (150 listing slots for €1,450 a month) that billed Ruhrblick for cars the platform never showed. The **Lyon apartment** carries property identity, agency structure and valuation; the **Barcelona ring** shows signals that existed from the first hour failing because nothing combined them; the **brown-out** shows three harmless things becoming an incident at peak.

Smaller stories are introduced by the chapters that own them: the Motorvane morning when a vendor's truncated files unpublished **38,400** cars ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)), the Tradeyard boost archaeology behind paid visibility ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking)), Priya Raman's inventory of **146** production models ([Models in Production: ML Platforms and Use Cases](#ml-platform)), and an Utrecht electric cargo bike listed through the photo-to-listing assistant pilot in December 2027 ([AI Across the Listing Lifecycle](#ai-in-listing-systems)).

{id: meet-veldmark--how-the-chapters-use-veldmark}
## How the Chapters Use Veldmark

Each chapter opens with a 2027 scene at Veldmark that poses its question, then answers it with concepts, dated public evidence from real marketplaces and a Veldmark worked example. The table maps the eight problems to the chapters that pose them and the chapters that do most of the work.

| Veldmark problem | Where it is posed | Where it is worked |
| --- | --- | --- |
| Four of everything | [Map What the Marketplace Does Before What Runs It](#business-capabilities), [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) | [Who Is on the Other Side? Identity and Verification](#identity-and-verification), [Trust and Safety as a Platform](#trust-and-safety-architecture), [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture), [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform), [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms), [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) |
| Six minutes to searchable | [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) | [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings), [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture), [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts), [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale) |
| Six weeks for a category | [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) | [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas), [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment), [What Did They Mean? Query Understanding and Autocomplete](#query-understanding), [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) |
| Duplicates at Hearthly | [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) | [Photos Sell: Media Pipelines for Listings](#media-pipeline), [Searching by Place: Map, Polygon and Commute Search](#map-search), [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) |
| Payment-link phishing | [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) | [Trust and Safety as a Platform](#trust-and-safety-architecture), [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention), [Who Is on the Other Side? Identity and Verification](#identity-and-verification) |
| Yardstick | [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate), [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) | [System of Record and Read Models: Listing Data Management](#listing-data-management), [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering), [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) |
| Keybridge neutrality | [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts) | [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling), [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution), [Models in Production: ML Platforms and Use Cases](#ml-platform), [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) |
| Overlap in Poland | [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy) | [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements), [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts), [How Listing Marketplaces Make Money](#monetization-models) |

Part VIII follows Common Ground as a program, through to [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution); Part IX leaves Veldmark and tests the book against the public record of real groups, starting with [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta).

Three conventions hold throughout. **Veldmark is always labeled fictional** the first time it appears in a chapter. **Its facts come from one canonical record**, so the six minutes, the 1.7 listings per property and the €240 bike mean the same thing everywhere. And a chapter that needs a new detail adds it without contradicting what is established here.

With the group, its problems and its program introduced, Part I begins where Ingrid began in February 2027: by asking what kind of marketplace each part of Veldmark actually is, and why the answer decides the architecture. Continue with [Part I — MARKETPLACE: The Business Behind the Listings](#part-1).

{id: meet-veldmark--sources-and-evidence}
## Sources and Evidence

{id: meet-veldmark--company-engineering-and-investor-sources}
### Company engineering and investor sources

- None. Veldmark Group, its brands (Tradeyard, Motorvane, Hearthly, Keybridge, Casavista, Veldmark Ads, Valuo, Safe Deal, Tally), its people, customers, figures, systems and events are fictional and invented for teaching; they are not drawn from any single real company.

{id: meet-veldmark--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Demandes de valeurs foncières (DVF)](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/), Direction générale des finances publiques, data.gouv.fr, n.d. (updated twice a year) — the real French open dataset of property transactions on which the fictional Valuo is described as trained.

{id: meet-veldmark--research-and-practitioner-sources}
### Research and practitioner sources

- The scenario's shape draws on the generalized marketplace domain models described in this book's provenance note and on the industry history covered, with dated sources, in [From Newspaper Columns to Portfolios: How the Classifieds Industry Evolved](#industry-evolution) and the Part IX case studies.

The vendor products named (Solr, Elasticsearch, OpenSearch, Kafka, Confluent Cloud, RabbitMQ, Google Pub/Sub, Azure Service Bus, Snowflake, BigQuery, Azure Synapse, Adyen for Platforms, Google Ad Manager, Prebid, SAP S/4HANA) are real; their capabilities are described, with sources, in the chapters that use them. Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
