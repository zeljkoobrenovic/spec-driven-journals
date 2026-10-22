{id: introduction}
# Introduction: Architecture for Liquidity

![Introduction: Architecture for Liquidity — logo](listing-systems-architecture/posts/introduction/assets/images/introduction/logo.jpeg)

> **IN THIS BOOK, YOU WILL:** Learn how to design, scale, govern and evolve the systems behind classifieds and listing marketplaces from the position of a Chief Architect of a multi-country, multi-vertical marketplace group. This page explains the book's argument, its nine parts, how to find the chapter for the decision already in front of you, and how to tell its documented facts from industry practice, labeled inference, recommendation and the fictional Veldmark.

> **WHY THE BUSINESS CARES:** A marketplace earns its revenue from matches: contacts, leads and sales. Most of the reasons a marketplace loses matches (slow publication, sold items that stay visible, duplicates, scams in the inbox, paid placements that push out relevant results) sit in the systems, and they rarely appear in any one team's report.

> **WHY ARCHITECTS SHOULD CARE:** In a marketplace group the most expensive architecture problems sit between systems and between brands: in the hand-off from feed to index, from moderation to alerts, from package to ranking, from an acquired stack to the group platform. The Chief Architect is one of the few people whose job is to look at all of those boundaries.

> **KEY POINTS:**
>
> * **A listing marketplace is a liquidity machine.** Listings, search, trust and monetization are not separate products; they are stages of one pipeline whose throughput is liquidity. Judge the architecture by how reliably it turns fresh, trustworthy supply into matches with demand, in every country, category and vertical, while each marketplace evolves at its own pace.
> * **Nine parts follow the machine from business model to practice.** The book moves from the business behind the listings, through modeling, supply, discovery, trust, money and the platform underneath, to the Chief Architect's long-term agenda and six publicly documented cases. The routing table on this page sends you straight to the chapter for the decision on your desk.
> * **Every statement says what kind of statement it is.** Company-specific claims are documented facts with a source and a publication date, because marketplace groups reorganize, rebrand and change owners faster than books are revised. Industry practice, labeled inference, the author's recommendations and the fictional Veldmark are each marked so you can weigh them differently.

The question usually comes at the end of a quarterly business review, after the revenue slides. The general manager of the country's largest classifieds site puts up one more chart: **contacts per live listing**, theirs against a younger competitor's estimate. The competitor has a third of the listings and, by every indication, more buyers contacting sellers per listing. *Why?*

Every team in the room has a good answer for its own part. Search availability was 99.95% for the quarter. The moderation queue met its service level. Feed imports from professional sellers were green every night. Monetization had its best quarter, with paid "top listing" sales up a fifth. Nobody owns the question, because the question is not about any one of those systems.

If you are a Chief Architect, you know what to do next: follow one listing from the seller's first tap to the buyer's message. Usually the reasons turn up quickly. A new listing takes six minutes to become searchable because moderation and indexing run in batches, and buyers who check the app at 8 p.m. see the competitor's listings first. A bike sold on Monday still appears in Tuesday morning's alert e-mails. The same flat appears three times because three agencies listed it. The first page of results is half paid placements that the ranking cannot tell apart from relevance. **The general manager's question is an architecture question.** Its answer runs through events that were never published, a search index that was never designed to forget, a ranking boost added years ago that nobody measured, and a messaging feature that was never treated as a trust surface.

![Four team dashboards show green checks while a pipeline beneath them leaks listings at every joint between its segments, so fewer reach the buyer.](listing-systems-architecture/posts/introduction/assets/images/introduction/green-dashboards-leaking-pipeline.jpeg)

**Figure 1:** *Every team's own report can be green while matches leak at the hand-offs between systems, which is why the general manager's question is an architecture question.*

This book is about answering that kind of question, and about designing marketplaces where it is asked less often.

{id: introduction--who-this-book-is-for}
## Who This Book Is For

The book is written for people who are accountable for how a listing marketplace's systems fit together:

- **Chief architects and enterprise architects of marketplace groups**, who must make one coherent system out of many marketplaces, several of which arrived by acquisition.
- **Principal and staff engineers** who own a stage of the pipeline (ingestion, search, trust and safety, messaging, monetization) and need to understand the stages on either side of it.
- **Search, data and machine-learning leads** whose ranking, recommendation, fraud and valuation models make decisions that sellers, buyers and regulators will ask about.
- **Platform-engineering leads** building capabilities that several brands and countries must adopt.
- **Product and engineering directors** of classifieds, real-estate, automotive, jobs and recommerce marketplaces.
- **Technology leaders integrating acquired marketplaces**, who must decide what to consolidate, in what order, and what to leave alone.

The book takes the perspective of a **Chief Architect of a multi-country, multi-vertical marketplace group**: several brands in several countries, each with its own history, traffic, sellers and stack, and an owner who wants growth and lower run costs at the same time. A single-country, single-vertical marketplace will find almost all of the reasoning applies; the trade-offs are drawn at group scale, where the cost of building a capability four times becomes visible.

**What it assumes.** Architecture literacy: you know what an API, a database, an event stream, a search engine and Kubernetes are, and you have made and defended architecture decisions. The book does not explain them.

**What it does not assume.** Marketplace economics, search and ML vocabulary, regulatory detail and vertical specifics. Liquidity, learning to rank, percolation, statements of reasons under the EU Digital Services Act (DSA) and vehicle identification numbers (VINs) are each defined where they first matter, in the chapter that owns them.

{id: introduction--the-argument-a-liquidity-machine}
## The Argument: A Liquidity Machine

A listing marketplace sells one thing: **matches**. A private seller wants a buyer for a city bike before Saturday. A dealer wants qualified leads for the cars on the lot. An agency wants mandates and viewings. A buyer wants the right item, car or home before someone else gets it. The marketplace does not usually own the goods, set the price or, in classic classifieds, touch the money. What it provides is the probability that the two sides find each other.

That probability is **liquidity**: the likelihood that a listing finds a buyer, or a search finds a listing worth contacting, within the time window that matters in its category. [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) defines it precisely. Two properties matter for architecture from the first page. Liquidity is **local**: it is measured per cell (a region crossed with a category), so a group can be liquid in Amsterdam bikes and illiquid in rural Portuguese furniture at the same time. And liquidity is **what compounds**: buyers come back where they find things, sellers list where buyers are, and every network effect a marketplace has is liquidity accumulated over years.

The book's central claim follows: **a listing marketplace is a liquidity machine, and its architecture should be judged by how reliably it turns fresh, trustworthy supply into matches with demand**, in every country, category and vertical, while letting each marketplace evolve at its own pace. Listings, search, trust and monetization are not separate products; they are stages of one pipeline whose throughput is liquidity.

![Diagram: The liquidity machine](listing-systems-architecture/posts/introduction/assets/images/introduction/fig02-liquidity-machine-supply-becomes-listings-that.jpeg)

**Figure 2:** *The liquidity machine. Supply becomes listings that are published, found, trusted, contacted and paid for; outcomes flow back into discovery and trust, and paid effects flow back into discovery under policy. Each part of the book designs one stage, and the platform carries them all.*

Read that way, every architectural choice is judged by the liquidity it protects or spends. A freshness objective is no longer an engineering preference; it is justified by the liquidity metric it protects, such as time to first contact. A removal that reaches search but not the alert digest is not a minor bug; it spends buyers' trust on an item that no longer exists. A paid placement is not only a product line; it is a sale of liquidity that must earn more than it costs the match rate. And a shared platform in a group is not good because it is shared; it is good if every brand's machine runs faster on it than without it.

The chapters work on one stage at a time and do not stop to restate the argument. The last chapter of Part VIII, [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution), draws it together: it maps each part to the stage of the machine it designs, the guarantee that stage must give, the liquidity metric it protects and the failure pattern that appears when it does not, and turns that map into marketplace fitness functions a group can measure every quarter.

{id: introduction--why-this-book-exists}
## Why This Book Exists

Good material exists on each side of this subject. Search-engine, streaming and cloud documentation explains the engines. Marketplace economics, from two-sided market theory to practitioner writing on network effects, explains why liquidity matters. Marketplace companies have published years of engineering posts, talks and annual reports, some remarkably candid.

What I have found missing, working with marketplace architecture, is the material **between** them. Engine documentation explains how to run an index; it does not say that the index must never become the system of record for listings, or what to do when a dealer's truncated file unpublishes tens of thousands of cars at three in the morning. Economics explains liquidity; it does not say which latency target, event contract or duplicate policy protects it. Company engineering posts describe one team's solution at one moment, usually without the constraints, the alternatives or what happened two years later.

The gap is most expensive at **group scale**. The classifieds industry has spent twenty years assembling portfolios: country marketplaces launched from a shared template, vertical portals bought one at a time, groups merged, demerged, taken private and partly sold again. [From Newspaper Columns to Portfolios: How the Classifieds Industry Evolved](#industry-evolution) tells that history from the public record. Each wave left systems behind: in many groups, several copies of identity, search, moderation and data sit beneath brands that buyers see as unrelated. **The failures appear at the boundaries**, between stages of the pipeline and between brands, and the boundaries belong to no project, no vendor and often no team. The Chief Architect is one of very few people with a mandate to look at all of them, between a board asking about synergies and the engine room where the costs sit. This book is written from that position.

{id: introduction--how-this-book-is-written}
## How This Book Is Written

**Company-aware but company-neutral.** The book draws on the public engineering and investor record of Adevinta, OLX Group, eBay Classifieds Group, AVIV Group, Kleinanzeigen, Marktplaats, leboncoin, mobile.de, Auto Trader, Rightmove, Zillow, Idealista, CoStar and others, because architects work with real precedents and generic advice does not survive contact with them. But it organizes the argument around architectural questions, not company profiles. Engines and vendors (Elasticsearch, OpenSearch, Solr, Vespa, Kafka, Adyen and others) appear where the choice between them is the decision; no chapter recommends a product in general.

**Five kinds of statement.** Architecture writing becomes unreliable when facts, habits, guesses, opinions and examples blur into one confident voice. Every chapter keeps them apart, and the wording and the sources show which is which:

| Kind of statement | What it is | How to recognize it |
| --- | --- | --- |
| **Documented fact** | A company's public statement, a filing, a regulation, a standard, a date | Linked inline to the source the first time it matters, with the **year of publication** in the sentence ("in a 2025 engineering post…", "the 2023 annual report states…"), and listed in the chapter's Sources and Evidence and in the [Bibliography: Sources and Evidence](#bibliography). |
| **Industry practice** | What marketplaces commonly do | Phrased as "commonly", "a typical pattern is"; no invented percentages. It describes the field, not a rule. |
| **Reference-architecture inference** | How a system like this is plausibly built, reasoned from engineering principles | When it concerns a real company, it is labeled explicitly, as a callout marked **INFERENCE, NOT DOCUMENTED** or as "a plausible reference architecture, not a description of that company's systems". It is never presented as a company's internals. |
| **Recommendation** | My judgment as a Chief Architect | First person ("I would", "the rule I use"), with the reasoning and the conditions under which it does not hold. No source validates it; argue with it. |
| **Illustration** | An example set at Veldmark | Labeled fictional the first time Veldmark appears in each chapter; its numbers come from one canonical record and agree across the book. |

![A sorting desk routes mixed cards into five trays labeled Fact, Practice, Inference, Recommendation and Illustration, with a balance scale beside them.](listing-systems-architecture/posts/introduction/assets/images/introduction/five-kinds-of-statement.jpeg)

**Figure 3:** *The book keeps five kinds of statement apart, from dated documented fact to fictional illustration, so each can be weighed for what it is.*

Three of these distinctions are easy to lose. A Veldmark figure, such as six minutes from submission to searchable, is an illustration, not a benchmark. An inference about how a public marketplace probably indexes its listings is not evidence of how it does. And a recommendation that sounds like a fact, such as "the search index is not the system of record", is still a recommendation, which is why each one comes with its reasoning and its exceptions.

**Why company claims carry dates.** Marketplace groups change faster than their engineering blogs. Adevinta's [2023 annual report](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf) (published 2024) described turning the leboncoin and Kleinanzeigen platforms into "a unified global platform" for its generalist marketplaces; the same report records the rebrand of eBay Kleinanzeigen as Kleinanzeigen. After a 2024 take-private, the group's [2025 strategic report](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf) (published 2026) describes a move to "a decentralised, standalone operating model". Both statements were true when they were written. A chapter that cited the first without its date would describe a strategy the company had since reversed. So every company-specific claim says when it was published, and where the evidence is more than about three years old, the chapter says that the current state may differ. Where a brand has been renamed or a business sold, the chapter uses the current name and mentions the former one once.

**As of October 2026.** Facts in this book were checked against public sources in October 2026 unless a chapter says otherwise. Treat any date-sensitive statement as a pointer to its source, and check the source before relying on it in a board paper or a contract.

{id: introduction--what-the-book-draws-on}
## What the Book Draws On

The book uses three kinds of material, and no other.

- **Two domain models.** The book started from two Productscape domain models in my sibling repository: a model of a horizontal general-listings marketplace and a model of a residential real-estate marketplace, each covering customers and their jobs, business capabilities, product streams, data assets and the stressors that test the architecture. Both are generic models written in the style of public operators, not descriptions of any company; the book never presents their contents as facts about a real marketplace or quotes their illustrative metrics as benchmarks.
- **The public record of the named companies.** Engineering blogs and talks, annual and strategic reports, filings, press releases and help pages, each cited with its publication year. Where the record stops, the chapter says so.
- **Standards, regulation and research.** EU regulations from the Official Journal, industry data standards for property and vehicle feeds, and published research and practitioner books on search, experimentation, machine learning and architecture.

**No internal material.** Nothing in this book comes from confidential documents, private conversations or inside knowledge of any company, and nothing describes a real company's internal architecture beyond what that company has published. Where a chapter needs a realistic situation the public record cannot supply, it uses Veldmark.

{id: introduction--how-the-book-is-organized}
## How the Book Is Organized

The book opens with three preface pages, continues with eight parts that form a learning path along the machine, tests the patterns against public cases in Part IX, and ends with reference material.

| Section | Question it answers | Chapters |
| --- | --- | --- |
| **Preface** | What is this book for, how do listing systems fail, and which group do the examples follow? | This page, [Unlisted: Fifteen Ways Listing Systems Go Wrong](#where-listing-systems-go-wrong), [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark) |
| **[Part I — MARKETPLACE: The Business Behind the Listings](#part-1)** MARKETPLACE | What business is behind the listings, and why does it decide the architecture? | 1–6: taxonomy, liquidity, industry history, capabilities, bounded contexts, verticals |
| **[Part II — LISTING: Modeling the Thing Being Sold](#part-2)** LISTING | What is the thing being sold, and how should it be modeled? | 7–12: listing aggregate, categories, attributes, media, location, sellers and accounts |
| **[Part III — SUPPLY: Getting Inventory In](#part-3)** SUPPLY | How does inventory get in, and how fast does it become searchable? | 13–17: ingestion, normalization and enrichment, entity resolution, publication, professional tooling |
| **[Part IV — DISCOVERY: Matching Intent to Inventory](#part-4)** DISCOVERY | How is buyers' intent matched to inventory that changes by the minute? | 18–23: search, query understanding, ranking, recommendations, map search, alerts |
| **[Part V — TRUST: Keeping the Marketplace Safe](#part-5)** TRUST | How does a marketplace keep contact between strangers safe? | 24–27: trust and safety, fraud, identity, regulation |
| **[Part VI — MONEY: Conversion and Monetization](#part-6)** MONEY | How do contacts become deals, and deals revenue, without selling out liquidity? | 28–32: messaging and leads, payments, monetization, entitlements, advertising |
| **[Part VII — PLATFORM: The Distributed System Underneath](#part-7)** PLATFORM | What distributed system do all of these stand on? | 33–40: events, data management, web and SEO, data, experimentation, ML, multi-country platforms, reliability |
| **[Part VIII — LEADERSHIP: The Chief Architect's Agenda](#part-8)** LEADERSHIP | How does a Chief Architect keep the machine coherent over a decade? | 41–45: consolidation, organization, modernization, AI, long-term evolution |
| **[Part IX — PRACTICE: How Others Built It](#part-9)** PRACTICE | What do publicly documented groups teach, and where does the evidence stop? | 46–51: Adevinta, OLX, eBay Classifieds, AVIV, property portals, automotive |
| **Reference** | Where are the templates, definitions and sources? | [Field Kit: Templates for the Marketplace Architect](#toolkit), [Glossary: The Language of Listing Systems](#glossary), [Bibliography: Sources and Evidence](#bibliography) |

![Diagram: Parts II to VI follow a listing through the machine, Part I sets the business terms they rely on, Part VII builds the platform beneath them and Part VIII keeps it coherent over time](listing-systems-architecture/posts/introduction/assets/images/introduction/fig04-parts-ii-vi-follow-listing-through.jpeg)

**Figure 4:** *Parts II to VI follow a listing through the machine, Part I sets the business terms they rely on, Part VII builds the platform beneath them and Part VIII keeps it coherent over time; Part IX tests the patterns against public evidence.*

**Part I, MARKETPLACE,** starts with the business, because in a listing marketplace the business model decides the architecture: a site whose job ends at the contact, a portal that sells leads and a marketplace that holds buyers' money need different identity, trust, payment and data systems. The part defines liquidity and the marketplace models, tells the industry's history from the public record, and describes the marketplace in capabilities and bounded contexts that outlive reorganizations. Do not skip it; later chapters justify their targets by pointing back to it.

**Part II, LISTING,** models the thing being sold. Its argument is that a listing is **an offer about a thing, not the thing itself**: a small, strict aggregate with one owner and a lifecycle, surrounded by categories, attributes, media, location and accounts, each governed as data with its own owner and rate of change.

**Part III, SUPPLY,** puts that model under load: supply arrives through forms, partner APIs and bulk feeds from systems the marketplace does not control. Ingestion, normalization, duplicate resolution, publication and professional tooling form one chain with contracts, provenance and a freshness target, in which removal must be faster than publication.

**Part IV, DISCOVERY,** turns to the buyer. Listing search looks like web search but behaves like a high-write operational system: documents live for days, most queries carry no text, and quality is judged by how fast a new listing appears and a sold one disappears. Search, ranking, recommendations, map search and alerts are one pipeline with several surfaces.

**Part V, TRUST,** treats trust and safety as a platform capability, not a team with a queue: shared decision services, signals and evidence; local policy, thresholds and legal grounds. It covers fraud, identity and the regulations, chiefly the DSA, that become system requirements.

**Part VI, MONEY,** follows the conversion from first message to invoice. Its argument is that **conversion and monetization are one pipeline with a conflict built in**: many revenue lines earn more when buyers see more pages or when paid listings displace relevant ones, so every sale of attention must be measured, and capped, against what it costs the match rate.

**Part VII, PLATFORM,** builds the distributed system underneath, from listing events and systems of record to experimentation in a two-sided market, machine learning, multi-country tenancy and reliability at the weekly peak. Its claim is that a shared platform earns trust through contracts, not mandates.

**Part VIII, LEADERSHIP,** is the Chief Architect's agenda: consolidation after acquisitions in an order that protects liquidity, an organization in which every journey, context and shared capability has one owning team, modernizing a live marketplace without losing traffic, governing AI, and evolving the platform over a decade against stressors rather than toward a target state. Its claim is that the hard problems of a marketplace group are problems of change, not of design.

**Part IX, PRACTICE,** steps outside the fiction. Six cases (Adevinta, OLX Group, eBay Classifieds Group, AVIV Group, the major property portals and the automotive marketplaces) separate what each group has documented, with dates, from my interpretation, say where the public evidence stops, and test the book's patterns against what actually happened.

Each part opens with a short introduction. Each chapter follows the same shape: opening callouts and three key points; a Veldmark scene that poses the question; concepts, architecture, documented practice and a worked example; trade-offs, vertical differences and failure modes; the Chief Architect's view; questions for a design review; and Sources and Evidence.

{id: introduction--start-with-the-decision-in-front-of-you}
## Start With the Decision in Front of You

The parts are a learning sequence for a first reading. If a decision is already waiting, find the row that matches it, read the chapter in the **Start with** column, and follow the **Then** column in order if you need more. Return to Part I whenever a marketplace term is unfamiliar.

| Your immediate need | Start with | Then |
| --- | --- | --- |
| The board asks whether the marketplace works, and the dashboards count listings and visits | [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) | [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform), [Testing a Two-Sided Market: Experimentation Platforms](#experimentation), [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution) |
| Sold or removed listings still appear in search, alerts or recommendations | [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) | [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings), [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts), [System of Record and Read Models: Listing Data Management](#listing-data-management) |
| Adding or splitting a category takes weeks and a cross-team release | [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) | [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas), [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts), [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) |
| A partner's or dealer's feed breaks, and imports are a surprise every night | [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) | [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment), [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) |
| The same property or car appears many times in results | [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) | [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking), [Photos Sell: Media Pipelines for Listings](#media-pipeline), [Zillow, Rightmove, Idealista and REA: What Property Portals Teach](#case-property-portals) |
| We are choosing a search engine, planning a reindex or failing at the weekly peak | [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) | [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale), [What Did They Mean? Query Understanding and Autocomplete](#query-understanding), [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) |
| Paid placements crowd the first page, and nobody can explain position 3 | [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) | [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements), [How Listing Marketplaces Make Money](#monetization-models), [Testing a Two-Sided Market: Experimentation Platforms](#experimentation) |
| Scams close in our messaging, or fake listings reach buyers within minutes | [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) | [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads), [Trust and Safety as a Platform](#trust-and-safety-architecture), [Who Is on the Other Side? Identity and Verification](#identity-and-verification) |
| A regulator, an auditor or the DSA transparency database needs evidence we cannot reproduce | [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) | [Trust and Safety as a Platform](#trust-and-safety-architecture), [System of Record and Read Models: Listing Data Management](#listing-data-management) |
| A brand wants to add payments, shipping or buyer protection | [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy) | [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments), [Payments for Finance Architects: Eleven Reasons the Numbers Disagree](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-fundamentals.html), [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) |
| An acquisition just closed, and it arrives with its own stack | [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) | [Map What the Marketplace Does Before What Runs It](#business-capabilities), [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts), [AVIV Group: Building a European Real-Estate Platform from Acquisitions](#case-aviv) |
| We want one platform for several countries, brands or verticals | [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) | [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms), [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering), [eBay Classifieds Group: Shared Platforms, Local Brands and a Sale](#case-ebay-classifieds) |
| A legacy monolith blocks every team, and we must retire it without losing traffic | [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) | [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings), [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture), [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) |
| We are piloting a photo-to-listing assistant or conversational search | [AI Across the Listing Lifecycle](#ai-in-listing-systems) | [Models in Production: ML Platforms and Use Cases](#ml-platform), [What Did They Mean? Query Understanding and Autocomplete](#query-understanding), [Trust and Safety as a Platform](#trust-and-safety-architecture) |
| The owner asks what it would cost to sell or carve out one brand | [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution) | [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms), [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation), [OLX Group: Regional Platforms, Verticalization and Retreat](#case-olx) |

Two rows start somewhere unexpected, on purpose. The payments row starts with the marketplace taxonomy, not with payments: moving from contact to transaction changes who holds the money and the risk, and that decides identity depth, trust and regulation before it decides a payment provider. And the single-platform row starts with what differs between verticals, because the most common failure I see is a shared platform designed for one vertical's physics and then imposed on the others.

{id: introduction--the-failure-patterns}
## The Failure Patterns

Listing marketplaces rarely fail through one bad decision. They lose liquidity through recurring patterns that each looked reasonable when it was chosen: a category tree hard-coded at launch, a dealer feed accepted as it was, one more ranking boost. The next page, [Unlisted: Fifteen Ways Listing Systems Go Wrong](#where-listing-systems-go-wrong), names fifteen of them, from **The Category Straitjacket** and **Feed Roulette** through **Ghost Inventory**, **Search as System of Record** and **Multiplier Creep** to **The Copy-Paste Country**, **Deal-Shaped Architecture** and **Set-and-Forget AI**. Each comes with its warning signs, its mechanism, its cost and the chapters that address it, so a design review can say "this is Feed Roulette" and move straight to the remedy. Every chapter in Parts I to VIII opens by naming the patterns it works on.

{id: introduction--veldmark-and-the-toolkit}
## Veldmark and the Toolkit

**Veldmark Group is fictional.** It is a privately held marketplace group headquartered in Rotterdam, with €1.31 billion of revenue in 2026 and four brands in eight European countries: Tradeyard, a horizontal classifieds site with paid visibility and an in-platform payment service; Motorvane, an automotive marketplace that sells dealer packages and leads; Hearthly, a real-estate portal assembled from acquisitions in France and Spain; and Keybridge, an acquired CRM for estate agents that also publishes their listings to Hearthly's competitors. It runs three clouds, three search engines, four identity systems and a PHP monolith from 2006, and in January 2027 its board approves Common Ground, a €140 million platform investment governed by one principle: **share platforms, not products**. [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark) introduces its brands, systems, people and the worked examples the chapters reuse, such as the €240 Rotterdam city bike that is sold on Monday and still advertised in 214 alert e-mails on Tuesday. Veldmark is a composite of patterns common in European marketplace groups, not a disguise for any of them. Use it as a rehearsal space: when a chapter shows a decision that Ingrid Halvorsen, its Group Chief Architect, makes, ask what the equivalent decision would be in your marketplace and what would change it.

The **[Field Kit: Templates for the Marketplace Architect](#toolkit)** collects the book's instruments as twelve templates, from the capability map and the feed contract to the listing event specification, the entitlement matrix and the architecture decision record. Do not adopt them all at once; start with the one that changes the decision on your desk this week. The [Glossary: The Language of Listing Systems](#glossary) defines the book's terms, grouped by part, and names the chapter that owns each one.

{id: introduction--a-living-journal}
## A Living Journal

This book is a living journal, and a work in progress, that I revise as I learn more through [my work](https://obren.io). Every chapter has a "View spec" link in its byline that opens the specification it was written against: its intent, its audience, its success criteria, what it deliberately leaves to other chapters, and the open questions it has not settled. Each spec ends with a changelog recording what changed and why. Read the book as current thinking with its limits stated, not as a finished text, and use the specs to see where those limits are.

I developed the book through AI-mediated authoring: I set the concept, the structure, the chapter contracts and the arguments; AI tools supported research against public sources, drafting from those contracts, consistency checks across chapters and editing; I reviewed and decided. The specs and the scripts used to build this site are in the [book's GitHub repository](https://github.com/zeljkoobrenovic/spec-driven-journals). The content, its judgments and its errors are my responsibility.

{id: introduction--where-to-go-next}
## Where to Go Next

If you read in order, turn next to [Unlisted: Fifteen Ways Listing Systems Go Wrong](#where-listing-systems-go-wrong). It names the fifteen failure patterns the rest of the book keeps returning to, and will help you recognize which are already in your marketplace. Then read [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark), so that every chapter's opening scene lands in a group you know. If a decision is waiting, use the routing table and come back to the preface later. Either way, keep the general manager's question in mind: why does a smaller competitor turn its listings into more contacts? Every chapter is part of the answer, and part of the design of a marketplace that turns fresh, trustworthy supply into matches with demand.

{id: introduction--sources-and-evidence}
## Sources and Evidence

*Company engineering and investor sources*

- [Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf), Adevinta, 2024: the plan to turn the leboncoin and Kleinanzeigen platforms into "a unified global platform", and the rebrand of eBay Kleinanzeigen as Kleinanzeigen.
- [Strategic Report 2025, Aurelia UK Feederco Ltd (Adevinta)](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf), Adevinta, 2026: the move to "a decentralised, standalone operating model".

*Research and practitioner sources*

- Productscape general-listings and real-estate marketplace domain models (author's sibling repository, 2026): the generic domain models the book started from; summarized for writers in the book's research digest. Not descriptions of any company.

Company, regulatory and research sources for each topic are listed in the chapter that owns the topic and collected in the [Bibliography: Sources and Evidence](#bibliography). Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
