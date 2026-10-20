{id: case-olx}
# 47. OLX Group: Regional Platforms, Verticalization and Retreat

![OLX Group: Regional Platforms, Verticalization and Retreat — logo](listing-systems-architecture/posts/47-case-olx/assets/images/47-case-olx/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Trace OLX Group's public record from its 2006 founding and Naspers' roll-up, through the regional mergers and the OLX Autos bet, to the compact European business that Prosus reported in 2026. You will read eight years of OLX engineering posts by era, separate what is documented from the author's reading, and test the case against the book's patterns and Veldmark's choices.

> **WHY THE BUSINESS CARES:** OLX's reported margin roughly doubled in two years after it left most of its markets and closed an inventory business that had made up just over half of its revenue. A group deciding where to compete and which adjacent businesses to enter is deciding what its listing platform will have to carry, and later shed.

> **WHY ARCHITECTS SHOULD CARE:** OLX has published unusually concrete search, ranking, trust-and-safety and multi-brand engineering work from 2018 to 2026. The record shows how one listing stack evolved in place under portfolio upheaval: lexical search kept and extended, paid visibility encoded in the ranker, and several country brands served from one code base by configuration.

> **KEY POINTS:**
>
> * **OLX converged on local leadership in a few markets.** From "45 markets" in 2018 the group shrank to seven in its year to March 2026, with US$992 million of revenue, a 48% adjusted EBITDA margin, and 71% of revenue from motors, real estate and jobs. Exits went through sales, mergers and joint ventures, and each departing market took its stack with it.
> * **Owning inventory did not combine with listing economics.** OLX Autos reached US$1.6 billion of revenue in the year to March 2022, just over half of the classifieds business, while losing money; Prosus exited it from 2023. Pay-and-ship was de-prioritized in Europe and the credit broker and services marketplace were sold. Adjacent bets should be built so that they can be switched off.
> * **The listing stack improved by evolution, not replacement.** OLX kept Solr and BM25, moved ranking into the engine as learning to rank, gave paid visibility its own explicit objective, and added vector retrieval as a fixed quota, proving it first in the zero-results fallback of a smaller market. Multi-brand work moved to one repository with per-brand configuration.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Acquisition Archipelago** — OLX was assembled from dozens of acquired and rebranded local sites, and its engineering record shows the identity and service-estate clean-up that cross-brand work still needed in 2024–2025.
> * **Paid-Rank Drift** — OLX is the clearest public case of paid visibility handled as an explicit ranking objective, and of a retrieval change that quietly penalized paid listings until the ranker was retrained.
> * **The Country Fork** — The documented move to one front-end repository for three brands and one learning-to-rank repository with per-brand configuration is the remedy for per-country copies.

OLX Group has made almost every portfolio move a classifieds group can make. It rolled up local sites across four continents and rebranded many of them to one name. It merged regional businesses into joint ventures in which it kept a minority stake. It built an inventory-owning car business that briefly doubled its revenue, then sold or closed it. It left Russia after the 2022 invasion of Ukraine. And by 2026 it was a **compact European business of seven markets**, reported by its parent Prosus with margins near 50%.

Part IX tests the book's patterns against real groups, and OLX answers the question [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) leaves open: **what happens to a platform when the portfolio, not the platform strategy, changes?** This chapter asks of each phase: *which markets and businesses did the platform carry, what did the group bet on beyond listings, and what did the engineering teams publish about the stack while the portfolio changed around them?* The answers support three arguments of this book: **liquidity is local and so is the platform's value** ([Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)); **adjacent transactional and inventory bets must be designed to be retired** ([Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments)); and **a listing stack is improved by evolving search, ranking and configuration in place** ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking), [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms)).

OLX's engineering blog spans 2018 to 2026, but it describes three different organizations: the global OLX of India, Indonesia, Pakistan, South Africa and Latin America; OLX Autos; and today's OLX Europe. **Many posts describe markets OLX no longer owns.** Every "OLX runs X" statement below is true at the date of its source and for the market it names, and no further.

{id: case-olx--how-to-read-this-case}
## How to Read This Case

Part IX cases follow stricter rules than the chapters in Parts I–VIII (see [Part IX — PRACTICE: How Others Built It](#part-9)). A **documented fact** carries its source and publication year in the sentence. **The author's interpretation** is marked "my reading" or sits in the Chief Architect's view. A **reference-architecture inference** appears only in a callout labeled `INFERENCE, NOT DOCUMENTED`.

Three limits shape the case. The financial evidence is unusually good, because Prosus reports OLX separately and, since 2026, by vertical. The engineering evidence is strong on search, ranking, experimentation and trust and safety, and almost silent on platform consolidation. And the history before 2019 rests largely on secondary sources, marked as widely reported.

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), appears only in the final comparison. It operates in some of the same countries as OLX, but it is a composite of industry patterns and is not a disguised description of OLX or any other group.

{id: case-olx--timeline-olx-in-dated-events}
## Timeline: OLX in Dated Events

The chronology follows. Dates are those of the cited releases and reports; ownership facts are as of October 2026 and may change. Prosus's fiscal year ends on 31 March, so "FY26" is the year to March 2026.

| Date | Event | Source type |
| --- | --- | --- |
| 2006 | OLX founded by Fabrice Grinda and Alec Oxenford as a classifieds site for markets outside the United States | Wikipedia (widely reported) |
| 2014 | Naspers raises its stake to about 95%; acquired local brands in Central and Eastern Europe and Asia are rebranded to OLX; OLX Brazil becomes a joint venture with Schibsted (whose stake passed to Adevinta at the 2019 demerger) | Wikipedia (widely reported) |
| 2016 | Naspers' classifieds businesses consolidated as OLX Group, headquartered in Amsterdam | Wikipedia (widely reported) |
| Nov 2018 | OLX describes itself as "a network of leading classifieds platforms in 45 markets", including OLX, Avito, letgo and dubizzle | OLX tech blog, 2018 |
| Jan 2019 | Naspers takes full control of Avito (Russia) | Wikipedia (widely reported) |
| Apr 2019 | Businesses in Kenya, Ghana, Uganda, Tanzania and Nigeria sold to Jiji; OLX Philippines to Carousell, with OLX taking a 10% stake | Wikipedia (widely reported) |
| 2019 | Controlling stake in Frontier Car Group, the instant-offer car-buying business that becomes OLX Autos | TechCrunch, 2021 |
| Mar 2020 | OfferUp and letgo combine their US businesses; OLX owns 40% | OLX Group release, 2020 |
| Jun 2020 | OLX contributes dubizzle and its Middle East and South Asia businesses to Emerging Markets Property Group (later Dubizzle Group); OLX holds 39% | Wamda, 2020 |
| Oct 2020 | OLX Brazil, a 50/50 joint venture of Adevinta and Prosus, completes the R$2.9 billion acquisition of Grupo ZAP | OLX Group release, 2020 |
| Mar 2021 | Frontier Car Group's Berlin entity closed; OLX Autos focuses on Latin America and Asia | TechCrunch, 2021 |
| Oct 2022 | Avito sold for RUB 151 billion; Russian exit complete | Naspers release, 2022 |
| Mar 2023 | Prosus announces its exit from OLX Autos | News24/Fin24, 2023 |
| Aug 2023 | OLX India sold to CarTrade; Indonesian business sold to Astra | Wikipedia (widely reported) |
| Aug–Oct 2025 | Kiwi Finance sale closed; agreements to sell OLX Uzbekistan, OLX Kazakhstan and Fixly (Polish services marketplace) | OLX Group releases, 2025–2026 |
| 17 Nov 2025 | La Centrale (France, motors) acquired for about €1.1 billion | OLX Group release, 2025 |
| May 2026 | Otodim launched in beta in Ukraine, a real-estate search platform drawing on OLX Ukraine's inventory | OLX Group release, 2026 |
| Jun 2026 | FY26 results: seven markets (Bulgaria, France, Poland, Portugal, Romania, South Africa, Ukraine), US$992 million revenue | OLX Group and Prosus releases, 2026 |

![Diagram: Each phase changed what the listing platform had to carry](listing-systems-architecture/posts/47-case-olx/assets/images/47-case-olx/fig01-each-phase-changed-what-listing-platform.jpeg)

**Figure 1:** *Each phase changed what the listing platform had to carry: many markets under one brand, then fewer markets as regions left through mergers, then inventory and payment businesses beside the listings, and finally a small set of markets organized by vertical.*

{id: case-olx--phase-1-roll-up-and-rebrand-20062018}
## Phase 1: Roll-Up and Rebrand (2006–2018)

The secondary sources behind the early history agree on its shape: Naspers bought into OLX in 2010, raised its stake to about 95% in 2014, and in April 2014 rebranded acquired local leaders to OLX in Romania, Bulgaria, Kazakhstan, Belarus, Hungary and Poland, while vertical brands such as Otomoto, Otodom, Storia, Autovit, Standvirtual and Imovirtual kept their names.

**My reading** is that the 2014 rebranding was brand consolidation, not platform consolidation. A shared name says nothing about a shared code base, and nothing public describes how many stacks the 45 markets ran. The engineering record of this era does show **capabilities built once and run across regional markets**, and a habit of fitting new methods into the existing search engine rather than beside it.

- **Ranking inside the engine (2019).** A May 2019 post on the global-markets search team describes a logistic-regression ranking model whose coefficients were "plugged into the ranking function of the existing search engine", to avoid new serving infrastructure. It reports about 10% improvement on the key search metric, and states that "search generates about 80% of total conversions".
- **Synonyms from sessions (2018).** For OLX South Africa, a 2018 post describes "query2vec": a skip-gram model over chains of queries in the same session, used to expand searches. Null searches fell by 27%. An early version returned "shoes" for "clothes", which led the team to a stronger evaluation process.
- **Autosuggest across regions (2020).** A December 2020 post describes an autosuggest corpus built from user queries, served through Solr's suggest component, and reports results per market:

| Market (2020) | Null searches | Search conversion |
| --- | --- | --- |
| Indonesia | −5.1% | +1.2% |
| Pakistan | −20% | +4.1% |
| South Africa | −5% | +2.4% |
| India | −2% | not reported |

*Source: OLX tech blog, "AutoSuggest Retrieval & Ranking (Part 2)", December 2020. All four markets have since been sold, merged or reduced to a minority stake except South Africa.*

The same capability produced a tenfold spread in null-search reduction across markets. **My reading** is that this is the strongest early evidence in the record for the book's argument that a shared capability must be evaluated per market ([Testing a Two-Sided Market: Experimentation Platforms](#experimentation)): the code was shared, the liquidity and language were not.

The data platform of this era was AWS-based: a 2018 GOTO Berlin talk by OLX's chief technology officer describes a data lake "collecting and storing billions of events and records per day", and a 2019 post describes ML pipelines on SageMaker and Step Functions. Both are likely replaced; a 2023 post shows Airflow and MLflow (see [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform)).

{id: case-olx--phase-2-regional-reshaping-through-mergers-and-joint-ventures-20182021}
## Phase 2: Regional Reshaping Through Mergers and Joint Ventures (2018–2021)

From 2018 the group began to concentrate. It left Nigeria and Venezuela in 2018, sold its East and West African businesses to Jiji and OLX Philippines to Carousell in 2019, and then made three structural moves in 2020:

- **United States.** OfferUp and letgo combined their US businesses in March 2020, with OfferUp operating the merged company and OLX owning 40% (OLX Group release, 2020).
- **Middle East, North Africa and South Asia.** In June 2020 OLX contributed dubizzle and its businesses in Egypt, Lebanon, Pakistan and several Gulf countries to Emerging Markets Property Group for a 39% stake in a company valued at about US$1 billion (Wamda, 2020).
- **Brazil.** OLX Brazil, owned 50/50 with Adevinta, bought Grupo ZAP for about R$2.9 billion, creating a business with about 1,600 staff, about 400 of them in technology; the OLX, ZAP and Viva Real brands kept their names (OLX Group release, 2020).

**My reading** is that these deals swapped operating control for equity. They are portfolio decisions, but they have a direct architectural consequence that the public record makes visible by omission: **a market contributed to a merger takes its platform with it**. No source describes OLX technology being shared with OfferUp, Dubizzle Group or OLX Brazil after the deals. Whatever regional capabilities had been built centrally either were already separable or had to be made so. That is the same lesson [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) draws from Adevinta's 2025 carve-outs, reached five years earlier and by a different route.

![Many market tiles, each with its own server stack, shrink to a compact cluster of seven; departing tiles carry their stacks away to partner buildings.](listing-systems-architecture/posts/47-case-olx/assets/images/47-case-olx/markets-leave-with-their-stacks.jpeg)

**Figure 2:** *From 45 markets in 2018 to seven in 2026: every market that left through a sale, merger or joint venture took its stack with it, so a shared capability is worth only the markets that stay.*

{id: case-olx--phase-3-the-vertical-integration-bet-20192025}
## Phase 3: The Vertical Integration Bet (2019–2025)

{id: case-olx--olx-autos}
### OLX Autos

In 2019 OLX took a controlling stake in Frontier Car Group, investing about US$400 million (TechCrunch, 2021). The business, renamed OLX Autos, bought cars from consumers through an instant offer, reconditioned and resold them. In March 2021 OLX closed its Berlin entity, moved core product development to India and focused OLX Autos on Latin America and Asia (TechCrunch, 2021).

Revenue then grew while losses widened. According to News24/Fin24's March 2023 report on the Prosus results:

- OLX Autos revenue was about **US$1.6 billion** in the year to March 2022, up 158%, "just over half of the classifieds business's revenue", with about **175,000 cars** transacted (98,000 the year before).
- In the first half of the following year revenue grew about 60% to about US$1 billion, while **trading losses widened to US$206 million**, which Prosus linked to spending on retail infrastructure.
- Prosus announced the exit, citing "higher cost of capital, high inflation and a reversal of pandemic trends" and a slowdown in used cars.

In June 2023 OLX cut about 800 roles and stopped buying cars in Argentina, Mexico and Colombia (TechCrunch, 2023); OLX India and the Indonesian business were sold in August 2023. Prosus's FY25 results record that all OLX Autos operations were "disposed of, classified as held for sale or closed by 31 March 2025", with a discontinued-operations loss of US$128 million in that year. South Africa's AutoTrader, a listing business, was never part of OLX Autos.

> **INFERENCE, NOT DOCUMENTED:** A plausible reading of why the bet strained the architecture as well as the balance sheet — not a description of OLX Autos' systems — is that an inventory business needs capabilities a listing platform does not have: inspection and condition records, a pricing authority that commits capital, reconditioning workflow, vehicle logistics and stock accounting, a finance book, and a retail front end that sells owned stock. A classifieds platform influences price and approximates condition; a retailer owns both. The two share a vehicle taxonomy and an audience, and little else. [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy) places this "managed" model on the ladder and [mobile.de, Auto Trader and AutoScout24: Lessons from Automotive Marketplaces](#case-automotive) compares it with other automotive groups.

{id: case-olx--the-other-adjacent-bets}
### The other adjacent bets

Beside OLX Autos, its largest bet beyond listings, OLX entered several smaller adjacent businesses and has left most of them.

| Bet | Entered | What it was | Fate | Source |
| --- | --- | --- | --- | --- |
| OLX Autos | 2019 | Instant-offer car buying and resale | Exit announced 2023; all operations gone by March 2025 | TechCrunch, 2021; Fin24, 2023; Prosus FY25 |
| Kiwi Finance (Romania) | Dec 2020 | Credit broker | Sale closed 1 August 2025 | OLX Group releases, 2020 and 2026 |
| Pay&Ship (Europe) | by 2023 | "OLX holds the money of the transaction and transfers it to the seller when the package is delivered" (the post does not name the payment provider or licensed party) | "De-prioritisation of pay-and-ship in Europe" in the second half of FY25 | OLX tech blog, 2023; Prosus FY25 |
| Fixly (Poland) | not verified | Services marketplace | Sale agreed 29 October 2025 | OLX Group release, 2026 |
| Inmokey (Argentina) | Oct 2019 | Software for real-estate agents | Not reported after the acquisition | OLX Group release, 2019 |
| Obido (Poland) | Feb 2021 | New-build platform matching developers and buyers | Brand retained; current status not reported | OLX Group release, 2021 |

The only engineering view of the transactional layer is a May 2023 post on predicting delivery-time ranges for Pay&Ship with two quantile-regression models. Two years later the product line was de-prioritized. **My reading** is that, from outside, this is what a cheap retreat looks like: a transactional product scaled back with no visible disruption to the listing business. Whether that reflects how it was built is not public. [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) develops the design of such a flow and why the money should sit with a licensed provider.

![A listing core surrounded by four adjacent modules (inventory, credit, delivery, services), each on its own switch; two are switched off and greyed out while the core keeps running.](listing-systems-architecture/posts/47-case-olx/assets/images/47-case-olx/adjacent-bets-on-switches.jpeg)

**Figure 3:** *Adjacent bets designed to be retired: inventory, credit, delivery and services kept outside the listing core, each behind its own boundary and switch, turn a retreat into a configuration change rather than a migration.*

{id: case-olx--phase-4-retreat-to-a-european-core-20222026}
## Phase 4: Retreat to a European Core (2022–2026)

{id: case-olx--exits-and-one-acquisition}
### Exits and one acquisition

Russia went first. On 14 October 2022 Naspers announced the sale of Avito, in which Prosus held an effective 99%, for RUB 151 billion in cash, about US$2.46 billion according to Euronews/Reuters, against earlier valuation estimates of about US$6 billion.

Central Asia followed. In August 2025 OLX agreed to sell OLX Uzbekistan to a joint venture led by TBC Bank Group, to "sharpen our focus on core product categories and geographies" in the words of chief executive Christian Gisy, and in October 2025 OLX Kazakhstan to VEON's Beeline Kazakhstan for US$75 million. The FY26 release gives only signing dates, so this chapter treats completion as not confirmed.

The same period brought the one large acquisition. OLX bought **La Centrale**, a French motors marketplace, from Providence Equity for about €1.1 billion; the deal closed on 17 November 2025. The FY26 release reports 13% traffic growth and 30% more leads at La Centrale, with integration "ahead of plan". It was OLX's first market in Western Europe, entered through a vertical, not a horizontal brand.

{id: case-olx--the-economics-of-focus}
### The economics of focus

Prosus reports OLX separately, so the retreat shows directly in its margins.

| Period | Revenue | Profit measure | Margin | Source |
| --- | --- | --- | --- | --- |
| FY24 (to March 2024) | about US$660m (implied) | aEBIT | 25% | Prosus FY25 results, 2025 |
| FY25 | US$777m (+18%) | aEBIT US$270m | 35% | OLX Group FY25 release, 2025 |
| FY26 | US$992m (+28%; +16% in local currency excluding M&A) | aEBITDA US$481m (+53%) | 48% | Prosus FY26 media release, 2026 |

*aEBIT is adjusted earnings before interest and tax ("trading profit"); aEBITDA adds back depreciation and amortization. The measure changed between FY25 and FY26, so the 35% and 48% are not the same metric; Prosus describes the FY26 margin as an eight-point expansion, which implies an aEBITDA margin of about 40% in FY25.*

From FY26 Prosus also reports OLX by vertical:

| Vertical, FY26 | Revenue | Growth | aEBITDA margin |
| --- | --- | --- | --- |
| Motors | US$429m | +42% (+20% excluding M&A and currency) | 59% |
| Real estate | US$185m | +26% | 46% |
| Jobs | US$87m | +14% | 43% |
| Remainder (general classifieds and other), by subtraction | about US$291m | not reported | not reported |

*Source: Prosus FY2026 media release, 29 June 2026. The remainder row is the author's arithmetic (US$992m minus the three verticals), not a reported figure.*

Motors, including La Centrale from November 2025, is the largest and most profitable line, and the three verticals are 71% of revenue although the horizontal OLX sites carry most of the audience. Prosus's FY25 booklet ties the growth to vertical products: in motors, "dealer tools" plus vehicle-history transparency and dealer ratings; in real estate, "the rollout of a unified platform, fully reimagined app and tools optimised for agents".

**My reading** is that the horizontal brand works as a funnel and the verticals monetize it. Otodim, launched in beta in Ukraine in May 2026, shows the move in its plainest form: a dedicated real-estate search platform that "draws on OLX Ukraine's extensive listings inventory", with filters for proximity to shelters and power autonomy, and with independent listing and in-platform messaging still "in development". **A vertical was launched first as a new lens on horizontal inventory**, not as a new supply system. [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) discusses what a vertical needs beyond such a lens, and [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) shows Adevinta's parallel reorganization by vertical in 2023.

{id: case-olx--the-engineering-record-how-the-listing-stack-evolved}
## The Engineering Record: How the Listing Stack Evolved

The posts of 2022–2026 describe OLX Europe, the business that remains. They are concentrated in search, ranking, recommendations, experimentation, trust and safety, and the supply-side use of language models.

{id: case-olx--search-five-stages-on-one-engine}
### Search: five stages on one engine

OLX's search evolved through five stages on one engine, Apache Solr, and is the best-documented search evolution in the book's research.

| Stage | When | What OLX described | Source |
| --- | --- | --- | --- |
| Sort only | before about 2021 | "It wasn't possible to sort search results by any criteria other than ad age or price" | OLX tech blog, 2022 |
| Hand-tuned formula | about 2021 | A "Recommended" sort combining text similarity, ad statistics such as click-through rate, and time, "hand-crafted into a simple formula"; making click-through data available to ranking "was no joke" | OLX tech blog, 2022 |
| Learning to rank in the engine | 2022 | A LambdaMART model trained with XGBoost and run through Solr's learning-to-rank plugin; labels are purchases or "messages/calls to sellers" "because transactions aren't always confirmed"; +12% conversions on page one, +5% purchases, +4% unique buyers; unique contacted sellers also rose; offline NDCG correlated with online results | OLX tech blog, 2022 |
| Two objectives | by 2025 | "Vanilla LTR", "trained using seller contact events, which we call successful events", and "VAS LTR", which "balances two objectives: maximizing relevance for users and ensuring visibility for Value Added Services (VAS), ads that have paid for additional exposure" | OLX tech blog, 2025 |
| Hybrid retrieval | 2025 | BM25 keyword retrieval plus a fixed number of vector results, re-ranked | OLX tech blog, 2025 |

*Learning to rank (LTR) trains a model to order results from labeled outcomes; NDCG (normalized discounted cumulative gain) is the standard offline ranking metric. Both are defined in [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking).*

**The success label is a contact, not a sale**, because a classifieds platform rarely observes the sale, and the check that unique contacted sellers *rose* guards against a ranker that concentrates demand on a few sellers ([Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)). And **paid visibility is an explicit, separate objective** rather than a multiplier hidden in a scoring formula. That is the opposite of Paid-Rank Drift: whoever changes the ranker has to see the paid objective.

{id: case-olx--hybrid-search-proved-in-the-fallback-then-in-the-main-flow}
### Hybrid search: proved in the fallback, then in the main flow

The September 2025 hybrid-search post is the most instructive single document in the record, because it describes the order of proof as well as the design. Keyword matching "often led to low recall or even zero results pages (ZRPs)", and the "chain of fallback retrieval steps designed to address edge cases and mitigate ZRPs", the extension chain, had become hard to improve. What followed:

1. **Keep BM25 and add a quota of vectors.** Vector similarity scores "did not consistently separate relevant from non-relevant ads", so OLX used a fixed allocation instead of a threshold: "We began with 35 results from semantic search", later "from 35 to 70", which "improved the quality of the hybrid recall set". Embeddings came from one multilingual text model for all markets.
2. **Notice that the ranker had never seen vector candidates.** The LTR model, trained only on keyword results, "consistently assigned lower relevance scores to vector search results", which "would be particularly problematic for VAS ads retrieved via semantic search". OLX retrained it with query–ad similarity as a feature.
3. **Bootstrap training data with a deliberately modest ranker.** Because vector results had no interaction history, OLX introduced "a linear re-ranking model to temporarily replace LTR", built on its earlier BM25-weighted function plus recency. Recency was protected because paid listings receive recency resets when sellers buy services.
4. **Prove value where risk is lowest.** Vector search first ran as a step in the extension chain in a smaller market, where it more than doubled seller-contact events per user. A main-flow test failed to converge because of a web tracking bug; re-runs showed "an approximately 3% increase in the share of users who completed a successful event" on apps and "a ~5% increase" on mobile web, after which OLX decided to "proceed with a full rollout of Hybrid Search on all platforms in this market".

![Diagram: The hybrid design as OLX described it in 2025](listing-systems-architecture/posts/47-case-olx/assets/images/47-case-olx/fig04-hybrid-design-olx-described-it-2025.jpeg)

**Figure 4:** *The hybrid design as OLX described it in 2025: lexical retrieval kept, vectors added as a fixed quota, and one ranker retrained to judge both, with the zero-results fallback as the first place vectors were tested. The diagram shows the documented shape, not internal components.*

**Similarity is not relevance in local classifieds**, as a companion post in October 2025 shows. OLX chose the embedding model by memory, latency and language constraints, with an offline dataset that weighted favorites and chat replies above clicks. The online test for similar items still lost to the incumbent until location and price were brought back through re-ranking. [What Did They Mean? Query Understanding and Autocomplete](#query-understanding) and [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) develop hybrid retrieval in general.

{id: case-olx--measuring-paid-visibility-honestly}
### Measuring paid visibility honestly

**OLX treats its paid products as claims to be measured.** They are packages with a number of "boosts" per 30 days and Value Added Services (VAS), paid exposure sold per listing. In August 2026 OLX described dashboards on which premium motors packages "appeared to perform worse than ads using cheaper packages", because "professional sellers self select into a package". Propensity-score matching, validated against a randomized experiment, estimated uplifts of 17.6% to 97.4% between package levels. An August 2025 post on group sequential testing shows the same rigor in method: with daily peeking, "despite a significance level of 5%, 27.9% of the simulations yielded a significant result". [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) and [Testing a Two-Sided Market: Experimentation Platforms](#experimentation) develop both methods.

{id: case-olx--one-code-base-many-brands}
### One code base, many brands

The record has three explicit statements about multi-brand engineering, all recent.

- **Front end.** A February 2026 Poznań masterclass was titled "One-product, three brands — Our strategy for serving different countries from a single repo", on managing "multiple websites from a single repository, balancing localisation, configuration, and design".
- **Ranking.** A June 2025 post explains that LTR projects spread across teams and repositories caused "duplicated efforts", so OLX centralized "all LTR projects within a single repository", using the Hydra configuration framework for brand-level settings across the general marketplace, motors and real estate.
- **Service-estate hygiene.** A March 2026 post on OLX Motors' Work Organization Framework lists what cross-brand work required first: "standardized user identification across 71 services, with 73% now using modern UUIDs instead of legacy user IDs", 45 or more components "migrated to AWS Secrets Manager", deployment notifications unified "across 60+ services", and pipeline times cut "by up to 44% (saving teams 94 hours per week)". It opens with the diagnosis that by 2024 OLX Motors had "a classic case of 'too much of everything, not enough of anything'".

An August 2026 post on coding agents mentions, in passing, a change across "three codebases": two Go services and a PHP service.

![Diagram: A reference reading of OLX Europe's multi-brand shape, assembled from the documented fragments](listing-systems-architecture/posts/47-case-olx/assets/images/47-case-olx/fig05-reference-reading-olx-europe-s-multi.jpeg)

**Figure 5:** *A reference reading of OLX Europe's multi-brand shape, assembled from the documented fragments. Everything in this diagram except the brand names, the ranking repository and the La Centrale acquisition is the author's inference.*

> **INFERENCE, NOT DOCUMENTED:** The fragments — one front-end repository for three brands, one ranking repository with brand configuration, a "unified platform" credited for real-estate growth, user identifiers standardized across 71 services — are consistent with a common classifieds pattern: one code base per vertical, serving several country brands, with locale, taxonomy and commercial packages held as configuration, and a legacy PHP core being replaced by Go services. That is a plausible reference architecture, not a description of OLX's systems. OLX has not published which brands share which code base, when the real-estate platform was unified, or whether La Centrale will move onto the motors platform. [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) treats this tenancy model in general.

{id: case-olx--trust-and-safety-media-and-recommendations}
### Trust and safety, media and recommendations

The rest of the record belongs to the chapters that own each topic; the table summarizes it and links to them.

| Area | What OLX published | Date and era | Chapter |
| --- | --- | --- | --- |
| Moderation | An automatic moderation system of many models that accepts, rejects or escalates listings to a human moderation panel; "more than 40 machine learning services" in production, more than half in trust and safety and in search and recommendations | 2020; global and Europe | [Trust and Safety as a Platform](#trust-and-safety-architecture) |
| Duplicates and fraud rings | Two-step duplicate detection (cheap candidates, then a pairwise classifier); outlier detection plus graphs of accounts sharing phones, e-mails or message text | 2020 (also PyCon DE 2019) | [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution), [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) |
| Chat fraud | "Chat Images GenAI" blocks suspicious images and QR codes in chat in real time; fraudulent images "around 30% of all fraud cases" in Poland; QR detection at 80% precision; live in Poland, Portugal, Bulgaria, Romania and other countries | January 2026; Europe | [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) |
| Media | CDN serving about 80% of image traffic; an on-demand processor rewritten from thumbor (about 6,000 pods at peak) to Dali, a Rust service on libvips, at about twice the load per instance | 2020; current state not public | [Photos Sell: Media Pipelines for Listings](#media-pipeline) |
| Recommendations | Item2Vec embeddings with 10–20% uplift in clicks and contacts from recommendation sections (2021); a data-team-owned Python service on ScyllaDB and DynamoDB reaching "a p99 latency under 10ms" after async I/O, batching and garbage-collection tuning (2025) | 2021, 2025; Europe | [Recommendations for Inventory That Disappears](#recommendations) |

{id: case-olx--language-models-on-the-supply-side-and-off-the-platform}
### Language models on the supply side and off the platform

OLX's 2025–2026 releases describe generative AI mostly on the supply side and in new channels; the outcomes are company-reported. Auto-filled attributes and descriptions cut posting time by 35–55% (2025). Auto Description drafts a listing from a photo for the seller to review, with human evaluation of 98% for style and relevance and 89% for faithfulness (2026). A January 2024 post describes a service "subscribed to ad events" that extracted job roles with an LLM for the search index, at "approximately 15K per month" (currency unstated) for about 4,000 calls a day. AutoIQ is a copilot for Otomoto dealers (2026). And CompassGPT (property, Imovirtual) and AutoGPT (cars, Otomoto first) run as apps inside ChatGPT, built with OpenAI (2026).

**My reading** is that the last item is the architecturally significant one. A marketplace that serves its inventory to an assistant it does not control turns structured attributes, availability and API-grade access into the product, and needs the channel controls that [AI Across the Listing Lifecycle](#ai-in-listing-systems) sets out.

{id: case-olx--trade-offs-the-case-illustrates}
## Trade-offs the Case Illustrates

| Option | What OLX's record shows | When it is right | When it fails |
| --- | --- | --- | --- |
| **Global breadth under one brand** | 45 markets in 2018; shared capabilities with very different effects per market | When a market can be won early and cheaply, and capabilities are portable | When local leadership cannot be reached, or the group's attention and capital are spread thin |
| **Exit by merger or joint venture** | US, Middle East and South Asia, Brazil: minority stakes, no shared technology documented after the deals | When a stronger local partner exists and the group wants exposure without operations | When shared group capabilities cannot be separated from the departing market |
| **Owning inventory beside listings** | OLX Autos: half of revenue, growing losses, exit within four years | Rarely for a classifieds group; only with cheap capital, pricing data and a retail operation | When used-car prices or capital costs move, as they did in 2022–2023 |
| **One code base per vertical with brand configuration** | One front-end repository for three brands; one LTR repository with brand configs; identity clean-up across 71 services | When brands share a vertical's data model and differ mainly in locale and packages | When a brand's product genuinely differs, or the configuration surface grows into a second code base |
| **Evolve the search stack in place** | Solr kept; LTR in the engine; vectors as a quota proved in the fallback path | When the incumbent engine is healthy and the team can retrain the ranker | When the engine cannot host the new retrieval or ranking method at the needed latency |

The rows are not a maturity ladder. **What the OLX record adds to the usual platform discussion is that the portfolio decision comes first**: which markets and businesses the group keeps decides what a shared platform is worth, and every exit in the record went through a deal structure that took the market's platform with it.

{id: case-olx--vertical-differences-in-the-record}
## Vertical Differences in the Record

| Vertical | OLX examples (2026) | What the record shows | Implication |
| --- | --- | --- | --- |
| **General classifieds** | OLX.pl, OLX.ro, OLX.pt, OLX.bg, OLX.ua | Most of the audience; contact as the success label; VAS and boosts in ranking; chat fraud is the main trust problem; pay-and-ship de-prioritized | The horizontal site is the funnel, so search quality, chat safety and listing creation matter most |
| **Motors** | Otomoto, Autovit, Standvirtual, La Centrale | US$429m revenue at 59% margin (FY26); dealer tools, vehicle history, dealer ratings; AutoIQ; package boosts measured causally; the inventory-owning model abandoned | Dealer products and lead quality carry the economics; the listing model, not the retail model, is the one that paid |
| **Real estate** | Otodom, Storia, Imovirtual, Obido, Otodim | US$185m at 46% margin; "unified platform" and agent tools; a new vertical launched as a lens on horizontal inventory | A shared vertical platform across countries is credited with growth; its mechanics are not public |
| **Jobs** | OLX jobs sections in Poland, Romania, Ukraine | US$87m at 43% margin; job-role extraction with an LLM; AI matchmaking and CV parsing; blue- and grey-collar focus | Taxonomy normalization of free text is the core enrichment problem |

{id: case-olx--failure-modes-the-record-exposes}
## Failure Modes the Record Exposes

1. **Revenue that hides a different business.** OLX Autos made reported classifieds revenue look twice as large while losing money. A platform that books listing revenue and principal revenue from selling cars in the same metrics will mislead its own investment decisions ([How Listing Marketplaces Make Money](#monetization-models)).
2. **Shared capabilities assumed to have one effect.** The 2020 autosuggest results ranged from −2% to −20% null searches across four markets. A group that rolls out a shared capability and reports one average learns nothing about where it works.
3. **A retrieval change that silently changes revenue.** The keyword-trained ranker under-scored vector candidates, including paid ones. Without an explicit paid objective and revenue guardrails, a search improvement can become a monetization regression ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking)).
4. **Identity fragmentation after a roll-up.** Needing to standardize user identification across 71 services in 2024–2025, a decade after the rebranding, shows how long acquired identity models survive. Identity is the first thing to consolidate, and the last to finish ([Who Is on the Other Side? Identity and Verification](#identity-and-verification)).
5. **Adjacent bets without an exit design.** OLX Autos, Kiwi Finance, Pay&Ship and Fixly were all entered and left within about six years. The record does not show what the exits cost in engineering terms; the frequency alone argues for designing adjacent businesses as separable from the start.

{id: case-olx--where-the-public-evidence-stops}
## Where the Public Evidence Stops

The following questions matter to an architect and are not answered by any public source found for this book. The chapter does not fill them with inference beyond the labeled callouts above.

| Question | What is public | What is not |
| --- | --- | --- |
| How do OLX Europe's country brands share code? | One front-end repository for three brands (2026); one LTR repository with brand configuration (2025); a "unified platform" in real estate (FY25) | Which brands share which code base, when unification happened, and what remains local |
| Will La Centrale move onto the motors platform? | Integration "ahead of plan" (FY26) | Whether "integration" means technology, commercial or organizational integration |
| What is the event backbone? | Kinesis used for search ingestion of enriched ad events (2024) | Whether Kafka, Kinesis or both carry listing events; schema governance |
| How far has the PHP-to-Go migration gone? | Go and PHP services coexist (2026) | Scope, timeline and remaining legacy share |
| What runs chat in Europe today? | Real-time chat screening of images and QR codes (2026); a Cassandra chat store described by the India-era chat team (2021) | The current European messaging stack |
| What did the exits cost technically? | Deal terms and dates | Any account of separating shared systems from departing markets, or of transitional services |

Three facts are volatile as of October 2026: completion of the Uzbekistan, Kazakhstan and Fixly sales; the status of the OLX Brasil joint venture with Adevinta; and the "OLX Magic" assistant described in a 2024 talk, which later releases do not mention. Readers should check them before relying on the portfolio list above.

{id: case-olx--the-chief-architect-s-view}
## The Chief Architect's View

What I take from OLX is a set of decision rules, each conditioned on the evidence.

**Let the portfolio decide what the platform is worth.** A shared platform's value is the sum of the markets it serves for as long as the group keeps them. OLX served 45 markets in 2018 and seven in 2026, and every exit took its market's stack along. Before funding a shared capability, I would ask which of today's markets will still be in the group in five years, and design the capability so that the others can leave.

**Price adjacent bets as businesses that may be closed.** Inventory, credit, delivery and services were all entered and left. The architectural defense is cheap: keep the money with a licensed provider, keep inventory and retail systems outside the listing core, give the adjacent business its own data boundary and its own events, and make its user-facing entry points feature-flagged per category. Then a retreat is a configuration change and a contract notice, not a migration.

**Change the search stack by evolution, with a proof sequence.** OLX's hybrid-search rollout is the sequence I would adopt as a standard: keep the incumbent retrieval, add the new method as a bounded quota, retrain the ranker so that it can judge the new candidates, ship a deliberately modest ranker to collect data, test first in the fallback path of a smaller market, and only then in the main flow. Each step limits what can go wrong.

![A six-step staircase: keep keyword search, add a vector quota, retrain the ranker, ship a modest ranker, test in the fallback path, then the main flow.](listing-systems-architecture/posts/47-case-olx/assets/images/47-case-olx/search-evolution-proof-staircase.jpeg)

**Figure 6:** *Evolution with a proof sequence: keep the incumbent retrieval, add vectors as a bounded quota, retrain the ranker, collect data with a modest ranker, prove value in the fallback path of a smaller market, and only then change the main flow.*

**Make paid visibility a named objective with an owner.** A separate paid-visibility model, as OLX describes, or a policy layer with explicit caps, as [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) proposes, both force the trade-off into the open. What fails is the multiplier nobody remembers adding. Every ranking or retrieval change should carry a revenue guardrail metric next to its relevance metric.

**Treat identity and service-estate hygiene as the start of consolidation.** OLX Motors' framework spent its early effort on user identifiers, secrets, pipelines and deployment notifications. That is unglamorous work and the precondition for every cross-brand capability. I would schedule it first in any group and measure it, as OLX did, in services migrated rather than in plans approved ([After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation)).

{id: case-olx--comparing-the-case-to-the-book-s-patterns-and-to-veldmark}
## Comparing the Case to the Book's Patterns and to Veldmark

The book's patterns, as OLX's record tests them:

| Book pattern or claim | OLX's record | Verdict |
| --- | --- | --- |
| Liquidity is local; groups are portfolios of local leaders ([Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)) | From 45 markets to seven, with margin rising as the portfolio narrowed | Strongly supported |
| Contacts as the success event where sales are invisible ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking)) | LTR labels are purchases or seller contacts; unique contacted sellers checked | Supported |
| Paid visibility belongs in an explicit, governed ranking layer ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking), [How Listing Marketplaces Make Money](#monetization-models)) | "VAS LTR" as a separate objective; retraining after vector retrieval penalized paid ads | Supported, with a documented failure mode |
| Measure paid products causally ([Testing a Two-Sided Market: Experimentation Platforms](#experimentation)) | Propensity matching validated by a randomized test | Supported |
| Hybrid retrieval as an extension of lexical search ([What Did They Mean? Query Understanding and Autocomplete](#query-understanding)) | BM25 kept; vectors as a fixed quota; ranker retrained | Strongly supported |
| Configuration over code across brands ([One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms)) | One front-end repository for three brands; one LTR repository with brand configs | Supported for the layers documented; the rest is inference |
| Category-gated, reversible transactional pivot ([Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments), [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy)) | Pay&Ship de-prioritized; OLX Autos exited | Supported, from the retreat side |
| Language models first on the supply side ([AI Across the Listing Lifecycle](#ai-in-listing-systems)) | Attribute filling, Auto Description, job-role extraction, dealer copilot | Supported; outcomes company-reported |

Now Veldmark, the fictional group, as of its 2027–2028 decisions in the scenario. Veldmark's Tradeyard is a horizontal brand in the Netherlands, Belgium, Poland and Portugal, with car, property and job sections in Poland and Portugal, beside a separate automotive brand, Motorvane. That structure resembles the horizontal-plus-vertical shape OLX runs in Poland and Portugal; it is a common industry pattern, and the ledger's details are invented. The comparison sharpens five of Veldmark's choices.

| Veldmark choice (2027–2028) | OLX parallel | What the case suggests |
| --- | --- | --- |
| Tradeyard keeps Safe Deal (€75 million of 2026 revenue, about 6% of group revenue) in NL, BE and PL goods categories, on Adyen for Platforms | OLX de-prioritized pay-and-ship in Europe in FY25 | Safe Deal earns its place only while it beats the same investment in the listing core; the category gates and the provider-held money in the ledger make a retreat cheap if it stops doing so |
| "Hearthly Direct", a guaranteed-offer proposal at 94% of the Valuo estimate, declined in 2027 | OLX Autos: half of revenue, rising losses, exit | The decision is consistent with the strongest lesson in the record; the [Models in Production: ML Platforms and Use Cases](#ml-platform) reasoning (a commit-tier use without validation) is the architectural form of it |
| Ranking policy v1: a relevance model with no entitlement features, paid slots above a relevance floor, caps on paid listings | OLX's separate "VAS LTR" objective | Two defensible designs for the same problem; Veldmark's caps are easier to audit, OLX's combined objective can trade off more finely. Either needs revenue guardrails on every retrieval change |
| Shared OpenSearch platform for Tradeyard and Hearthly by end of 2028, replacing Tradeyard's Solr and Elasticsearch estates | OLX evolved ranking and retrieval on Solr for years | An engine migration is a choice, not a precondition: Veldmark should run its hybrid-retrieval work with OLX's proof sequence whichever engine hosts it |
| Feb 2028 external assistant channel, Hearthly FR and Motorvane DE first, with quotas, lead attribution and no training on returned listings | CompassGPT and AutoGPT inside ChatGPT | Same direction; Veldmark's contractual and quota controls address the questions OLX's releases leave unanswered |

The Polish overlap is the Veldmark rule the case can point toward but not validate. In the ledger, Tradeyard Poland's car section competed with Motorvane Poland for the same dealers, and Veldmark resolved it in early 2027: private car listings stay on Tradeyard with insertion fees; dealers above a small listing count are offered Motorvane packages, with their stock syndicated to Tradeyard through Motorvane's feed; and the shared listing core records which brand owns the commercial relationship for each listing. OLX runs a horizontal site and a motors vertical in the same country too, but **it has not published how OLX.pl and Otomoto divide dealers, listings or revenue**, so the case cannot validate Veldmark's rule. What the record does support is the direction: OLX's money is in the verticals, and Otodim shows a vertical being built on horizontal inventory. Ingrid Halvorsen, Veldmark's fictional Group Chief Architect, should therefore make sure the "commercial owner per listing" field and Motorvane's syndication feed are first-class parts of the Listing event contract, since they are what would let Tradeyard's cars or homes become a vertical lens later, or be handed to Motorvane entirely.

{id: case-olx--questions-to-ask}
## Questions to Ask

1. Which of our markets and businesses do we expect to own in five years, and is our shared platform sized and designed for that set rather than today's?
2. For each adjacent business (payments, shipping, financing, inventory, services), what would it take to switch it off in one category or one country, and how long?
3. Is any of our reported revenue principal revenue from inventory or pass-through, and do our dashboards keep it apart from listing revenue?
4. When we roll out a shared capability, do we measure its effect per market and per category, or only on average?
5. Where does paid visibility enter our ranking, who owns it, and which metric would catch a retrieval change that lowers paid exposure or relevance?
6. Does our search roadmap have a proof sequence (bounded quota, retrained ranker, fallback path, smaller market) or a cut-over date?
7. How many user identifier schemes do our services still use, and what is the plan and metric for converging them?
8. Which of our listing data would an external assistant need, and are its attributes, availability and access controls good enough to expose?

OLX shows a group that reached for global breadth and adjacent businesses, then concentrated on a few markets and verticals while its engineers kept improving one listing stack. The next case, [eBay Classifieds Group: Shared Platforms, Local Brands and a Sale](#case-ebay-classifieds), follows a group that built shared platforms under local brands across many countries and was then sold whole — the integration question seen from the other side of the deal.

{id: case-olx--sources-and-evidence}
## Sources and Evidence

{id: case-olx--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [OLX Group FY26 results](https://www.olxgroup.com/?p=5024) — OLX Group, 2026. Revenue, growth, margin change, 71% from three verticals, seven markets, disposals with signing dates, La Centrale closing and results, AI investment (re-verified October 2026).
- [Prosus FY2026 media release](https://www.prosus.com/~/media/Files/P/prosus-corp-v2/results-reports-and-events-archive/annual-report/2026/fy2026-media-release.pdf) — Prosus, 2026. OLX revenue and aEBITDA; motors, real estate and jobs revenue and margins (re-verified).
- [OLX Group reports strong FY 2025 results](https://www.olxgroup.com/news/olx-group-reports-strong-fy-2025-results-with-18-revenue-growth-and-61-profit-uplift-year-on-year/) — OLX Group, 2025. FY25 revenue and aEBIT, 64 million daily listings, nine brands in nine markets, unified real-estate platform (re-verified).
- [Prosus financial results FY25 booklet](https://www.lobbyregister.bundestag.de/media/57/dc/638531/prosus-financial-results-fy25-booklet.pdf) — Prosus, 2025 (copy on the Bundestag lobby register). FY24 margin, de-prioritization of pay-and-ship, OLX Autos disposals and discontinued-operations loss.
- [OLX Group H1 FY26 results](https://www.olxgroup.com/?p=4285) — OLX Group, 2025. La Centrale closing; GenAI ad-posting outcomes.
- [Disposal of Avito Group](https://www.naspers.com/news-insights/regulatory-updates/2022/disposal-of-avito-group) — Naspers, 2022. Buyer, price and rationale (re-verified).
- [OfferUp and letgo combine US marketplaces](https://www.olxgroup.com/news/offerup-and-letgo-combine-us-marketplaces-to-deliver-a-better-buying-and-selling-experience-for-more-than-20-million-monthly-users/) — OLX Group, 2020. 40% stake; non-US letgo retained.
- [OLX Brazil completes the acquisition of 100% of Grupo ZAP](https://www.olxgroup.com/news/olx-brazil-completes-the-acquisition-of-100-of-grupo-zap/) — OLX Group, 2020. Joint-venture ownership, price and combined scale (re-verified).
- [OLX Group acquires Kiwi Finance](https://www.olxgroup.com/news/olx-group-successfully-acquires-kiwi-finance-the-largest-credit-broker-in-romania/) — OLX Group, 2020. Credit-broker entry.
- [OLX Group acquires Inmokey](https://www.olxgroup.com/news/olx-group-acquires-inmokey-a-solid-commitment-towards-user-oriented-technology/) — OLX Group, 2019. Agent software in Latin America.
- [OLX Group acquires Obido](https://www.olxgroup.com/news/olx-group-acquires-obido-an-innovative-real-estate-platform-for-the-primary-market/) — OLX Group, 2021. New-build platform.
- [OLX Group to sell OLX Uzbekistan to a joint venture led by TBC Bank Group](https://www.olxgroup.com/news/olx-group-to-sell-olx-uzbekistan-to-a-joint-venture-led-by-tbc-bank-group/) — OLX Group, 2025. Scale and rationale.
- [VEON's Beeline Kazakhstan to acquire OLX Kazakhstan](https://www.olxgroup.com/news/veons-beeline-kazakhstan-to-acquire-online-classifieds-platform-olx-kazakhstan/) — OLX Group, 2025. Agreement and price.
- [OLX Group launches Otodim platform in Ukraine](https://www.olxgroup.com/news/olx-group-launches-otodim-platform-in-ukraine-deepening-commitment-to-the-countrys-real-estate-market/) — OLX Group, 2026. Vertical built on horizontal inventory (re-verified).
- [We fight online fraud with the power of AI](https://www.olxgroup.com/?p=4590) — OLX Group, 2026. Chat image and QR-code fraud detection.
- [How OLX uses AI to reduce repetitive work](https://www.olxgroup.com/news/how-olx-uses-ai-to-reduce-repetitive-work/) — OLX Group, 2026. Auto Description and its human evaluation.
- [OLX launches agentic AI products at CLAIM AI in Lisbon](https://www.olxgroup.com/news/olx-launches-agentic-ai-products-to-transform-property-search-and-car-sales-at-claim-ai-in-lisbon/) — OLX Group, 2026. CompassGPT and AutoIQ.
- [OLX launches AutoGPT agentic AI assistant](https://www.olxgroup.com/news/olx-launches-autogpt-agentic-ai-assistant-transforming-automotive-search-across-europe/) — OLX Group, 2026. Car search inside ChatGPT; company-reported outcome.
- [Hybrid Search — Where Keywords Meet Vectors, Enabling Classifieds Discovery](https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4) — OLX tech blog (Inês Soveral), 2025. Solr BM25, extension chain, vector quota, Vanilla and VAS LTR, linear re-ranker, rollout results (re-verified via the blog's RSS feed).
- [Importance of offline evaluation to guide model choice](https://tech.olx.com/importance-of-offline-evaluation-to-guide-model-choice-1c2be1c4599a) — OLX tech blog (Tiago Cabo), 2025. Embedding model selection; similarity is not relevance.
- [Learning-To-Rank: Sorting Search Results](https://tech.olx.com/learning-to-rank-sorting-search-results-b21a8bd48808) — OLX tech blog (Ilia Ivanov), 2022. Ranking stages, contact labels, results.
- [Ranking Ads with Machine Learning](https://tech.olx.com/ranking-ads-with-machine-learning-ee03d7734bf4) — OLX tech blog (Chandan Routray), 2019. Model coefficients in the existing engine; search share of conversions.
- [Understanding language through search](https://tech.olx.com/understanding-language-through-search-78ea37be7ac8) — OLX tech blog (Vaibhav Sharma), 2018. Query2vec in South Africa; 45 markets.
- [AutoSuggest Retrieval & Ranking (Part 2)](https://tech.olx.com/autosuggest-retrieval-ranking-part-2-14a8f50fef34) — OLX tech blog (Aakash Prakash), 2020. Per-market autosuggest results.
- [Unlocking Flexibility in Configuration: The Power of Hydra](https://tech.olx.com/unlocking-flexibility-in-configuration-the-power-of-hydra-3f9e69263bb4) — OLX tech blog (Catarina Goncalves), 2025. One LTR repository with brand configuration.
- [OLX Masterclass Frontend 2026](https://tech.olx.com/olx-masterclass-frontend-2026-068299a2df50) — OLX tech blog (Isaac Queiroz), 2026. One repository, three brands.
- [Empowering Innovation Through Structure](https://tech.olx.com/empowering-innovation-through-structure-93c15614f6d3) — OLX tech blog (Sara Mendes), 2026. Identity standardized across 71 services; secrets, pipelines, notifications (re-verified).
- [Does it matter how you feed an agent its context?](https://tech.olx.com/does-it-matter-how-you-feed-an-agent-its-context-ee1519586520) — OLX tech blog (Raymond Gitonga), 2026. Go and PHP code bases.
- [Correlation Lied to Us: Rethinking Product Impact with Causal Inference](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5) — OLX tech blog (Enderson Santos), 2026. Boost packages, selection bias, matched uplift.
- [Speed with Rigor: testing smarter with group sequential design](https://tech.olx.com/speed-with-rigor-testing-smarter-with-group-sequential-design-af962363ce90) — OLX tech blog (Gabriela Lewenfus), 2025. Peeking and sequential testing (re-verified).
- [Scaling recommendations service at OLX](https://tech.olx.com/scaling-recommendations-service-at-olx-db4548813e3a) — OLX tech blog (Jordi Esteve Sorribas), 2025. Data-team-owned service and latency work (re-verified).
- [Item2Vec: Neural Item Embeddings to enhance recommendations](https://tech.olx.com/item2vec-neural-item-embeddings-to-enhance-recommendations-1fd948a6f293) — OLX tech blog (Ilia Ivanov), 2021. Embedding-based recommendations.
- [Extracting Job Roles in Job Ads: A Journey with Generative AI](https://tech.olx.com/extracting-job-roles-in-job-ads-a-journey-with-generative-ai-e8b8cf399659) — OLX tech blog (Mahnaz Namazi), 2024. Event-driven LLM enrichment and its cost.
- [Machine Learning for Delivery Time Estimation](https://tech.olx.com/machine-learning-for-delivery-time-estimation-1-591c8df849a0) — OLX tech blog (Enderson Santos), 2023. Pay&Ship flow and delivery-range models.
- [Data Science at OLX](https://tech.olx.com/data-science-at-olx-7c7406d1713f) — OLX tech blog (Alexey Grigorev, Andreas Merentitis), 2020. Moderation models; more than 40 ML services.
- [A Two-Step Framework for Duplicate Detection](https://tech.olx.com/a-two-step-framework-for-duplicate-detection-fbbe4c905480) — OLX tech blog (Alexey Grigorev), 2020. Moderation pipeline and duplicates.
- [Detecting Fraud Rings with Unsupervised Learning](https://tech.olx.com/detecting-fraud-rings-with-unsupervised-learning-554bedf29dbf) — OLX tech blog (Hagop Boghazdeklian), 2020. Outlier detection and account graphs.
- [Presenting Dali, an Image Processor Service](https://tech.olx.com/presenting-dali-an-image-processor-service-514e6be00de8) — OLX tech blog (Augusto César Dias), 2020. CDN share and image processor rewrite.
- [Building an AWS Serverless ML Pipeline with Step Functions](https://tech.olx.com/building-an-aws-serverless-ml-pipeline-with-step-functions-b39feed12bab) — OLX tech blog (Rafael Felix Correa), 2019. AWS-first data and ML stack of the global era.
- [From (Big) Data Mess to Data as an Innovation Enabler](https://gotopia.tech/sessions/652/from-big-data-mess-to-data-as-an-innovation-enabler) — Olaf Zschiedrich, GOTO Berlin, 2018. Data-lake architecture on AWS.

{id: case-olx--standards-regulation-and-documentation}
### Standards, regulation and documentation

- No standards or regulatory sources are specific to this case; the regulatory context for chat moderation and trader information is in [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation).

{id: case-olx--research-and-practitioner-sources}
### Research and practitioner sources

- [Prosus looks to ditch OLX Autos business as second-hand car market slows](https://www.news24.com/fin24/companies/prosus-looks-to-ditch-olx-autos-business-as-second-hand-car-market-slows-20230302) — News24/Fin24, 2023. OLX Autos revenue, cars transacted, losses and exit rationale (re-verified).
- [OLX Group layoffs](https://techcrunch.com/2023/06/20/olx-group-layoffs) — TechCrunch, 2023. Role cuts and OLX Autos closures.
- [OLX shuts down Berlin's Frontier Car Group](https://techcrunch.com/2021/03/29/prosus-classifieds-group-olx-shuts-down-berlins-frontier-car-group-to-focus-olx-autos-on-latam-and-asia/) — TechCrunch, 2021. Frontier Car Group investment and OLX Autos refocus.
- [EMPG reveals details of merger with OLX](https://www.wamda.com/index.php/en/2020/06/empg-reveals-details-merger-olx) — Wamda, 2020. Middle East and South Asia merger and 39% stake.
- [Prosus sells Avito](https://www.euronews.com/next/2022/10/14/ukraine-crisis-prosus-avito) — Euronews/Reuters, 2022. US-dollar price and earlier valuation.
- [OLX Kazakhstan to be sold to VEON Group's Beeline for $75M](https://www.onlinemarketplaces.com/?p=104706) — Online Marketplaces, 2025. Kazakhstan sale terms.
- [OLX revenue climbs to $992m as Prosus folds classifieds into Europe](https://www.onlinemarketplaces.com/articles/olx-revenue-climbs-to-992m-as-prosus-folds-classifieds-into-europe/) — Online Marketplaces, 2026. Reporting change; final OLX Autos sale.
- [OLX](https://en.wikipedia.org/wiki/OLX) — Wikipedia, n.d. (read October 2026). Founding, Naspers stakes, 2014 rebranding, 2016 consolidation, African and Asian exits (widely reported, not primary).
- [Avito.ru](https://en.wikipedia.org/wiki/Avito.ru) — Wikipedia, n.d. (read October 2026). Avito ownership history (widely reported, not primary).

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
