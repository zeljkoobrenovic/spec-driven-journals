{id: marketplace-taxonomy}
# 1. Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy

![Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy — logo](listing-systems-architecture/posts/01-marketplace-taxonomy/assets/images/01-marketplace-taxonomy/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Classify a marketplace along six independent axes, starting with the one that matters most: where the platform's job ends. You will see what each answer adds to the architecture (identity depth, payments, trust, search, monetization and data) and how documented marketplaces moved between models, sometimes successfully and sometimes at great cost.

> **WHY THE BUSINESS CARES:** The marketplace model decides what the business can charge for, which risks it carries on its balance sheet and which regulators take an interest. A general manager who moves from "we connect buyers and sellers" to "we guarantee the purchase" changes the company's margins, licences and liabilities, not only its checkout.

> **WHY ARCHITECTS SHOULD CARE:** Most expensive marketplace platform mistakes come from building one model's assumptions into systems that must serve another. A platform built for classifieds cannot simply be switched to transactions, and a transactional platform imposed on a lead-generation portal fails just as badly. The taxonomy is the first input to every boundary drawn later in this book.

> **KEY POINTS:**
>
> * **A marketplace is defined by where its job ends.** Classifieds end at the contact, lead-generation portals at a qualified lead, transactional marketplaces at a completed payment and delivery, and managed marketplaces at a guaranteed outcome. Each step adds bounded contexts, data the platform must hold and liabilities it must carry.
> * **Classify along independent axes, and per category rather than per brand.** The endpoint, horizontal or vertical scope, seller type, item identity, money flow and risk ownership vary separately. One brand usually contains several profiles, so the profile belongs in configuration per country and category, not in a brand-wide assumption buried in code.
> * **Moving toward the transaction is a category-gated bet, not a destination.** leboncoin, Kleinanzeigen and Marktplaats added payments and shipping for goods but not for cars or homes. OLX de-prioritized its pay-and-ship flow in Europe, and OLX Autos, Zillow Offers and CarGurus' CarOffer retreated from inventory risk. Build so the endpoint can move per category in both directions.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Forced Fit** — A shared platform designed around one marketplace model (usually transactional goods) is imposed on brands whose job ends somewhere else, and their teams route around it.
> * **Fast Mail for Fraudsters** — When the platform's job ends at the contact, messaging becomes the place where the money is negotiated, so it is also where fraud concentrates unless the model's endpoint is designed into trust and safety.
> * **Vanity Liquidity** — A marketplace that does not know where its job ends cannot say what success is, so it counts listings and visits instead of the contacts, leads or completed sales its model actually delivers.

Ask five people in a marketplace group what kind of business it runs, and you usually get five answers that are each partly right. The general manager says "classifieds". The product director says "we are becoming transactional". The sales director says "we sell dealer subscriptions". The finance team says "most of our money is advertising and visibility". The trust and safety lead says "we are a messaging platform with listings attached". **Each answer describes a different end point of the marketplace's job**, and each one implies a different architecture.

This chapter gives that conversation a shared vocabulary, and opens Part I because every later boundary in the book depends on it. It defines four marketplace models (classifieds, lead-generation portals, transactional marketplaces and managed marketplaces), the axes along which they vary, and what each one asks of the systems underneath. It owns the terms *classifieds*, *lead-generation marketplace*, *transactional marketplace* and *horizontal* versus *vertical*, and it introduces the *marketplace profile* that later chapters build on: [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) measures how well each profile's job is done, [Map What the Marketplace Does Before What Runs It](#business-capabilities) and [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) map what each one needs, and [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) makes the profile a configuration scope. The running example is Veldmark's four brands from [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark). How the industry arrived at today's portfolios belongs to [From Newspaper Columns to Portfolios: How the Classifieds Industry Evolved](#industry-evolution), and the detailed differences between verticals to [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements).

**The model is an architecture decision, not a pricing decision.** Moving the endpoint by one step, from contact to lead or from lead to payment, adds new bounded contexts, new data with new retention rules, new identity requirements, new regulators and new failure modes. The decision therefore needs to be explicit, recorded per country and category, and revisable, because the documented record shows marketplaces moving in both directions.

{id: marketplace-taxonomy--setting-the-scene-at-veldmark-one-group-four-models}
## Setting the Scene at Veldmark: One Group, Four Models

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), approved its Common Ground program in January 2027: €140 million over four years to build shared platform capabilities beneath four brands. Ingrid Halvorsen joined as Group Chief Architect in February. In her second week, Noor Hassan, the Group Chief Product Officer, brought her a slide titled "One listing service, one checkout, four brands". Tradeyard Safe Deal, the in-platform payment and shipping product, had processed **11.6 million** transactions and about **€1.02 billion** of gross merchandise value (GMV) in 2026, earning about €75 million in buyer fees and shipping-label margin, a take rate of about 7%. Why not extend it to Motorvane's cars and Hearthly's apartments and build a single listing and order platform for the whole group?

Ingrid did not argue with the slide. She asked Mateus Carvalho, the Group CTO, for one afternoon with the brand leaders and put a grid on the wall: brands and countries down the side, five questions across the top.

1. Where does our job end: at the contact, at a lead delivered to a professional, at a payment, or at a delivery?
2. Who supplies the listings: private people, professionals, or both?
3. Is each item unique, or could it be matched to a catalog product?
4. Who holds the buyer's money, and when?
5. If the deal goes wrong, who loses money first?

By the end of the afternoon the grid had twenty rows, not four, and the answers did not line up with the brands. Tradeyard's goods categories in the Netherlands, Belgium and (since 2026) Poland ended at the contact for most listings but at a completed payment for those sold through Safe Deal. Tradeyard Portugal had no Safe Deal at all. Tradeyard Poland's car and property sections charged insertion fees and ended at the contact. Motorvane ended at a lead delivered to one of **21,400** dealers, and sold financing referrals on the side. Hearthly ended at a lead delivered to an agency, but its Valuo valuation product also generated seller leads before a property was even listed. Keybridge, the agent CRM acquired in 2024, was not a marketplace at all: it was software that published agencies' listings to many portals, including Hearthly's competitors.

The most uncomfortable row was Poland. **Tradeyard Poland's cars section and Motorvane Poland served the same dealers under two different models**: per-listing insertion fees on one side, dealer subscriptions with listing slots on the other. Both brands' sales teams were calling on the same showrooms.

Ingrid's conclusion, recorded in the first decision record of her tenure, was not that Noor's proposal was wrong. A shared order platform might be exactly right for Tradeyard's shippable goods. It was that **"one checkout for four brands" assumed one model, and the group ran at least four**. The rest of this chapter is the vocabulary she used to explain why.

{id: marketplace-taxonomy--where-the-marketplace-ends-four-models}
## Where the Marketplace Ends: Four Models

A **listing marketplace** is an intermediary that publishes offers from many suppliers and helps buyers find them. Listing marketplaces differ most in how far along the buyer's journey the platform's responsibility reaches, so this book classifies them first by **endpoint**: the last step of the transaction for which the platform takes responsibility.

{id: marketplace-taxonomy--classifieds}
### Classifieds

**Classifieds** are marketplaces whose job ends when a buyer contacts a seller: a message, a revealed phone number, an e-mail form. Price negotiation, payment and handover happen between the parties, usually off the platform. The platform publishes, ranks and protects; it does not take part in the sale. Facebook's announcement of Marketplace in October 2016 states the model in a single sentence: "Facebook does not facilitate the payment or delivery of items in Marketplace" ([Meta Newsroom, 2016](https://about.fb.com/news/2016/10/introducing-marketplace-buy-and-sell-with-your-local-community/)).

Because the platform never sees the money, classifieds monetize **visibility and access**: insertion fees in some categories, paid visibility products such as bumps and top placements (often called value-added services, VAS, a term [How Listing Marketplaces Make Money](#monetization-models) owns), professional-seller subscriptions and display advertising. Adevinta's 2023 accounts describe the core of the business as "sales of classified ad listings and related features" and report classifieds revenue of €1,399 million out of €1,826 million group revenue, with advertising at €312 million and transactional revenue at €103 million ([Adevinta Annual Report 2023, published 2024](https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm)). That is about 77% classifieds, 17% advertising and 6% transactions, years into a declared transactional push.

{id: marketplace-taxonomy--lead-generation-marketplaces}
### Lead-generation marketplaces

A **lead-generation marketplace** (or lead-generation portal) ends when a qualified enquiry is delivered to a professional: a dealer, an estate agent, an employer. Both models deliver contacts, so the difference looks commercial rather than technical. But the professional pays because the lead has value, so the platform must **qualify, count, route and attribute leads**, and prove their value at renewal time.

The documented models differ in how professionals pay and who receives the lead:

- **Subscriptions priced on value delivered.** Rightmove's revenue is per-advertiser subscriptions plus products: average revenue per advertiser (ARPA) was £1,621 a month in 2025 ([Rightmove full-year results, 2026](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf)). Autotrader reports average revenue per retailer forecourt (ARPR) of £2,995 a month for the year to March 2026 ([Autotrader FY26 results, 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf)).
- **Share of voice.** Zillow's market-based Premier Agent pricing distributes connections "in proportion to their share of voice, or a Premier Agent partner's share of total advertising purchased in a particular zip code" ([Zillow 10-K for 2025, filed 2026](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)).
- **Pay at close.** Zillow Preferred agents "pay a performance advertising fee when a real estate transaction is closed with one of the leads, generally within two years" (same filing). AVIV France "monetises seller leads through a commission-share model" ([OnlineMarketplaces, 2023](https://www.onlinemarketplaces.com/articles/seloger-parent-aviv-france-to-add-300-employees-in-2023)).
- **The lead belongs to the lister.** CoStar's Homes.com advertises a "your-listing your lead basis", a deliberate contrast with portals that resell buyer leads to agents who did not list the property ([CoStar 10-K for 2025, filed 2026](https://www.sec.gov/Archives/edgar/data/1057352/000105735226000020/csgp-20251231.htm)).

Pay-at-close pricing pulls the portal into the transaction's *outcome* without touching its *money*. The platform must learn, months later, whether a lead became a sale, which is a matching and reconciliation problem rather than a payments problem.

{id: marketplace-taxonomy--transactional-marketplaces}
### Transactional marketplaces

A **transactional marketplace** ends when payment and delivery are complete on the platform. The buyer pays through the platform (or, more precisely, through its payment provider), the item ships with a platform-integrated carrier or is handed over against a platform-confirmed payment, and disputes are resolved by the platform. Revenue becomes a **take rate** on GMV. eBay defines take rate as "net revenues divided by GMV" and reports 13.94% for 2025 on GMV of $79.6 billion ([eBay 10-K for 2025, filed 2026](https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm)). Andreessen Horowitz's 2020 marketplace metrics distinguish GMV, "the total sales dollar volume of merchandise transacting through the marketplace", from revenue, the part the marketplace "takes" ([a16z, 2020](https://a16z.com/13-metrics-for-marketplace-companies/)). Classifieds usually have no observable GMV at all, which is why they report revenue per advertiser or per listing instead. Bill Gurley's 2012 list of marketplace factors puts the commercial attraction of the transactional rung bluntly: "if you bring the cash, you are king", because it is "much easier to extract reasonable economics when you are in the flow of payment" ([Gurley, 2012](https://abovethecrowd.com/2012/11/13/all-markets-are-not-created-equal-10-factors-to-consider-when-evaluating-digital-marketplaces/)).

Vinted is the clearest example of a marketplace built transactional from the start. It describes "its proven marketplace model in an ecosystem of vertically-integrated shipping and payment infrastructure" and reported GMV of €10.8 billion and revenue of €1.1 billion for 2025 ([Vinted financial results 2025, published 2026](https://company.vinted.com/newsroom/financial-results-2025)). Sellers list free; the main fee is paid by the buyer at checkout, now called "the Vinted fee" (formerly the "Buyer Protection fee"), "usually 5% + $0.70" in the US ([Vinted US price list, updated 2026](https://www.vinted.com/pricelist)).

{id: marketplace-taxonomy--managed-marketplaces}
### Managed marketplaces

A **managed marketplace** goes one step further: the platform takes inventory, quality or outcome risk itself. It buys and resells, guarantees the result, or curates supply so tightly that it acts as a retailer. Autotrader's Autorama leasing business is a documented example inside a classifieds group: about 1,350 vehicles were "temporarily taken on balance sheet" in the year to March 2026 ([Autotrader FY26 results](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf)). iBuying, in which the portal buys homes directly from sellers, is the best-known example from real estate; Pattern 3 below covers its failure.

{id: marketplace-taxonomy--the-endpoint-ladder}
### The endpoint ladder

The four models form a ladder. Each rung adds what the platform must do, know and carry.

| Model | Platform's job ends at | What the platform observes | Primary monetization | Who holds money and risk | Documented examples |
| --- | --- | --- | --- | --- | --- |
| **Classifieds** | Contact | Views, contacts, conversations; *not* whether a sale happened | Insertion fees, VAS, pro subscriptions, display ads | Parties transact off-platform; platform holds no funds | Facebook Marketplace (2016), leboncoin, Kleinanzeigen and Marktplaats for most categories |
| **Lead generation** | Qualified lead delivered to a professional | Leads, lead channel, sometimes the outcome via CRM or public records | Subscriptions priced on leads, share of voice, pay-per-lead, pay-at-close | Off-platform transaction; platform may carry estimation risk on success fees | Rightmove, Autotrader, Zillow Premier Agent, CarGurus, Homes.com |
| **Transactional** | Completed payment and delivery | Order, payment, shipping and dispute events; true GMV | Take rate: buyer fees, commissions, shipping margin | Licensed payment provider holds funds; platform carries buyer-protection losses | Vinted, eBay; transactional layers at leboncoin, Kleinanzeigen, Marktplaats |
| **Managed** | Guaranteed outcome or owned inventory | Everything above, plus condition, cost and resale data | Spread, high take rate, principal revenue | Platform carries inventory and price risk on its balance sheet | Autorama (Autotrader), Zillow Offers (closed 2021), OLX Autos (exited 2023–2025) |

![Four descending steps labeled contact, lead, payment and outcome, with the platform figure carrying a heavier load on each step.](listing-systems-architecture/posts/01-marketplace-taxonomy/assets/images/01-marketplace-taxonomy/endpoint-ladder-growing-load.jpeg)

**Figure 1:** *Each rung of the endpoint ladder adds what the platform must do, know and carry: contacts, then leads, then payments and disputes, then inventory and price risk.*

One adjacent business model is not on the ladder but appears in almost every marketplace group: **software for professionals**. Agent CRMs, dealer management add-ons and listing-distribution tools serve the supply side directly. Scout24 reports "Transaction Enablement" revenue of €106.6 million for 2025 from CRM, data and valuation products ([Scout24 preliminary 2025 results, published 2026](https://www.scout24.com/media/scout24/Investor_Relations/Berichte_und_Praesentationen/2025/Scout24_Preliminary_IR_News_Q4_FY_2025_results_DE.pdf)), and Zillow owns the Follow Up Boss CRM. These are SaaS products whose customer is the professional and whose architecture follows SaaS rules: tenancy, data ownership and, where they publish to rival portals, neutrality. [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) covers them.

{id: marketplace-taxonomy--six-axes-one-profile}
## Six Axes, One Profile

Six axes vary independently, and together they form what this book calls a **marketplace profile**: the combination of answers that describes one marketplace in one country and category. The endpoint is the most consequential axis, but not the only one.

| Axis | Values | What it decides first |
| --- | --- | --- |
| **Endpoint** | Contact · lead · payment · delivery · guaranteed outcome | Bounded contexts, observable outcomes, regulatory obligations |
| **Scope** | Horizontal (many categories) · vertical (one domain) | Taxonomy breadth, attribute depth, search tuning, brand strategy |
| **Seller type** | C2C (consumer to consumer) · B2C (business to consumer) · B2B · mixed | Supply channels, account model, trader obligations, monetization unit |
| **Item identity** | Unique items · items with a strong external identity (VIN, address) · catalog products | Enrichment, deduplication, entity resolution, price guidance |
| **Money flow** | Off-platform · via the platform's payment provider · via the platform's own licensed entity | Payments architecture, ledger, licensing, tax reporting |
| **Risk ownership** | Parties · platform for buyer protection · platform for inventory | Provisions, dispute systems, fraud appetite, balance sheet |

**Horizontal** marketplaces cover many unrelated categories in one place: Kleinanzeigen, leboncoin, Marktplaats, OLX. They win on breadth and habit, and their supply is mostly private people. **Vertical** marketplaces specialize in one domain, usually a high-value one with professional supply: property (Rightmove, Idealista, SeLoger), vehicles (mobile.de, Autotrader, AutoScout24), jobs (StepStone, InfoJobs). The economics differ sharply. Rightmove and Autotrader both report operating margins of about 70% on professional subscriptions (sources above), while Adevinta's 2023 report shows the margin of its French business falling two points "mainly reflecting the evolution of the business mix with an increasing share of transaction services and a decreasing share of highly profitable advertising revenues".

Horizontal groups also contain verticals. Andrew Parker's much-cited 2010 post on "the spawn of craigslist" showed how startups carved niches out of Craigslist's categories ([Parker, 2010](http://thegongshow.tumblr.com/post/345941486/the-spawn-of-craigslist-like-most-vcs-that-focus)). The same unbundling happens inside groups: Adevinta reorganized in 2023 around "Re-Commerce, Mobility, and Real Estate & Emerging Verticals", and Prosus now reports OLX by vertical, with motors, real estate and jobs at 71% of OLX revenue in the year to March 2026 ([OLX Group, 2026](https://www.olxgroup.com/?p=5024)). A horizontal brand's car section and a sister vertical brand can end up competing for the same dealers, which is Veldmark's Polish problem.

**Seller type** matters because consumers and professionals respond to different prices and carry different legal status. Consumers buy per item and per event: an insertion fee, a bump, a buyer fee. Professionals buy monthly contracts with quotas and upgrades. Legally, the line between a consumer and a **trader** (a person acting for business purposes) decides which consumer-protection rules apply, what the platform must collect about the seller and what it must disclose to buyers. [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts) owns the trader-status model.

**Item identity** decides how much of the listing can be derived rather than typed. Second-hand goods are usually unique items with weak structure. Vehicles have a strong external identity (the vehicle identification number, VIN) that resolves to manufacturer data. Properties have a durable address and parcel identity that outlives any single listing. Catalog goods, such as a specific phone model, can be matched to a product record, which favors transactional models with standardized fulfillment.

**Money flow** and **risk ownership** are separate questions, and the rest of this chapter keeps them separate. A platform can route money through a licensed provider without holding it, hold it through its own licensed entity, or never touch it. Independently, it can carry buyer-protection losses without owning any inventory, or carry inventory risk without processing consumer payments. eBay books losses "resulting from our buyer protection programs, chargebacks" as transaction losses (10-K, above): **buyer protection is a liability to provision, not only a fee to collect**.

**A brand is not a profile.** Tradeyard is one brand with ten profiles across four countries. A platform that encodes the profile as "this is Tradeyard, so it is classifieds" will be wrong for Safe Deal categories in the Netherlands and right for Portugal, and will need code changes every time the business moves a category.

{id: marketplace-taxonomy--what-each-model-asks-of-the-architecture}
## What Each Model Asks of the Architecture

Moving down the endpoint ladder changes nearly every system, not just one. The table summarizes the consequences; the three sections after it explain those that most often surprise architects.

| Concern | Classifieds | Lead generation | Transactional | Managed |
| --- | --- | --- | --- | --- |
| **Identity depth** | E-mail or phone; risk-tiered checks | Verified business for professionals (KYB, know your business); consumer contact verified | KYC (know your customer) on payees through the payment provider; trader traceability | Full customer due diligence; credit and contract checks |
| **Core new contexts** | Listing, search, messaging, moderation | Lead, lead routing, attribution, pro CRM integration | Order, payment, payout, shipping, dispute, ledger | Inventory, valuation, reconditioning, resale |
| **Trust focus** | Fake listings, off-platform payment scams in messages | Fake leads, lead fraud, misrepresentation by professionals | Account takeover, payment and refund fraud, phishing of the platform's own payment brand | Valuation error, adverse selection, condition fraud |
| **Search and ranking signal** | Contact as success label | Lead quality and conversion | Purchase and completion | Margin and turn time |
| **Monetization system** | VAS catalog, insertion pricing, entitlements | Contracts, quotas, lead metering, attribution and true-ups | Fee pricing on the read path, checkout, take-rate accounting | Pricing authority, principal revenue |
| **Data the platform must keep** | Listings, messages, reports | Leads, lead outcomes, call records | Orders, payment and shipping events, financial records under statutory retention | Asset records, cost basis, condition evidence |
| **Typical regulatory switch** | DSA notice and action, ranking disclosure | Professional seller traceability, lead-data consent | Payment licensing (usually via partner), DAC7 seller reporting, buyer-protection terms | Consumer sale law as seller, financial reporting of inventory |

Figure 2 shows the same idea as a pipeline: every rung adds contexts and none replaces the ones before it.

![Diagram: The endpoint ladder as a pipeline](listing-systems-architecture/posts/01-marketplace-taxonomy/assets/images/01-marketplace-taxonomy/fig02-endpoint-ladder-pipeline-each-model-inherits.jpeg)

**Figure 2:** *The endpoint ladder as a pipeline. Each model inherits every context to its left and adds new ones; a marketplace that moves its endpoint for one category must run the additional contexts for that category alone.*

{id: marketplace-taxonomy--what-the-platform-can-observe}
### What the platform can observe

The least obvious consequence is **observability of outcomes**: a classifieds platform does not know whether a sale happened. It sees a contact and, if it is lucky, a seller marking the item sold. OLX's 2022 description of its learning-to-rank model is explicit about this: training labels were purchases *or* "messages/calls to sellers", "because transactions aren't always confirmed" ([OLX Tech, 2022](https://tech.olx.com/learning-to-rank-sorting-search-results-b21a8bd48808)). A lead-generation portal sees the lead and, with CRM integration or public records, sometimes the outcome. A transactional marketplace sees the completed order.

Observability decides **what the ranking optimizes, what the experiments measure and what can be sold**. A portal that cannot observe sales cannot price on sales without building an attribution pipeline first; Zillow's pay-at-close model treats the fee as "variable consideration" and estimates "the conversion rate of a lead to a real estate transaction" (10-K, above). [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) turns this into a metric design.

{id: marketplace-taxonomy--identity-and-regulation-deepen-with-the-endpoint}
### Identity and regulation deepen with the endpoint

Each rung down switches on more identity and regulatory obligations. In the EU, the Digital Services Act (DSA) requires platforms that allow consumers to conclude distance contracts with traders to collect trader information, and to make best efforts to assess whether it is reliable and complete, before those traders can offer products (Article 30 of [Regulation (EU) 2022/2065](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)). The Omnibus Directive defines an "online marketplace" as a service that "allows consumers to conclude distance contracts with other traders or consumers" and makes the main ranking parameters material information ([Directive (EU) 2019/2161, 2019](https://eur-lex.europa.eu/eli/dir/2019/2161/oj)).

**Adding payments switches on seller reporting that a pure classifieds site may not have.** The EU's DAC7 directive makes platform operators collect and report seller data to tax authorities when they know, or can reasonably know, what sellers were paid ([Belastingdienst, n.d.](https://belastingdienst.nl/wps/wcm/connect/en/business/content/information-for-platform-operators-dac7)). Commentary on DAC7 indicates that platforms engaged solely in listing or advertising fall outside the reporting definition. This is a reading of the rules to confirm with counsel, not settled law for every classifieds case. [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) owns these obligations; [Who Is on the Other Side? Identity and Verification](#identity-and-verification) owns the identity levels.

{id: marketplace-taxonomy--money-flows-through-a-licensed-partner-until-it-does-not}
### Money flows through a licensed partner, until it does not

Classifieds groups that add payments almost always keep the money with a licensed payment service provider (PSP). Kleinanzeigen's "Sicher bezahlen" holds funds with its provider for up to 14 days until the buyer confirms receipt ([Kleinanzeigen, n.d.](https://themen.kleinanzeigen.de/sicher-bezahlen/)). Marktplaats withdrew its earlier escrow-style "Gelijk Oversteken" in April 2022 as "not safe enough"; its successor, "Kopersbescherming" (buyer protection), runs through the PSP Online Payment Platform, which holds the money until a week after receipt, with a 5% buyer fee at the time ([AVROTROS Radar, 2022](https://radar.avrotros.nl/artikel/dit-is-de-vervanger-voor-de-gelijk-oversteken-functie-van-marktplaats-52677)). The marketplace owns the offer and acceptance flow, the fee pricing, the shipping labels, the release timer and the disputes; the provider owns the regulated money.

The step beyond that is a licence of one's own. Vinted Pay holds an e-money institution (EMI) licence from the Bank of Lithuania and began onboarding members onto its own wallet in January 2026, "expected to reduce payment-related costs and dependencies" ([Vinted, 2026](https://company.vinted.com/newsroom/vinted-pay)). With a licence comes safeguarding of client funds, a ledger that must reconcile to the cent and supervisory reporting. RECONCILED's [Payments for Finance Architects: Eleven Reasons the Numbers Disagree](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-fundamentals.html) explains why those obligations reshape the finance architecture.

{id: marketplace-taxonomy--in-practice-moving-along-the-ladder}
## In Practice: Moving Along the Ladder

The documented history of European and American marketplaces shows movement along the ladder in both directions. Four patterns recur.

{id: marketplace-taxonomy--pattern-1-classifieds-add-a-transactional-layer-category-by-category}
### Pattern 1: classifieds add a transactional layer, category by category

The large European horizontals added payments and shipping for shippable goods while keeping classifieds for everything else.

- **leboncoin** "launched a transactional business model in some of the generalist categories" in 2019, according to Adevinta's 2019 annual report, and its transactional revenue grew from €53 million in 2022 to €73 million in 2023 (Adevinta 2023 report, above).
- **Marktplaats** launched transactional services in 2017, shipping in 2019 and buyer protection, adding a second shipping company in 2022 (same report).
- **Kleinanzeigen** stated "strong ambitions to become a full transactional leader in German Re-Commerce" after its 2023 rebrand from eBay Kleinanzeigen (same report).

None of these brands moved cars or homes to on-platform payment. mobile.de, inside the same group, earned essentially no transactional revenue in 2023. **The transactional layer was category-gated**: it applied where items are shippable, prices are moderate and the buyer's main fear is non-delivery.

The transactional layer also cost margin. Transactional revenue was 5.6% of Adevinta's 2023 revenue, it diluted the French margin, and it came with rising "direct costs from transactional services (such as payment and shipping service provider costs)". It may still be the right strategy, because buyer protection changes trust and frequency, but it is not a free revenue line.

{id: marketplace-taxonomy--pattern-2-transactional-pushes-are-scaled-back}
### Pattern 2: transactional pushes are scaled back

Some groups pushed further and pulled back.

- **OLX** described its Pay&Ship flow in 2023: "OLX holds the money of the transaction and transfers it to the seller when the package is delivered" ([OLX Tech, 2023](https://tech.olx.com/machine-learning-for-delivery-time-estimation-1-591c8df849a0)). Prosus's results for the year to March 2025 then record "the de-prioritisation of pay-and-ship in Europe" in the second half of the year, while OLX concentrated on motors, real estate and jobs.
- **Adevinta**'s 2023 plan to turn the leboncoin and Kleinanzeigen platforms into "a unified global platform" for generalist marketplaces, including "the full transactional journey", was followed in 2025 by a move "from a centralised structure to a decentralised, standalone operating model" ([Adevinta strategic report 2025, published 2026](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf)). No public source confirms whether the unified transactional platform was delivered. [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) tells that story in full.

{id: marketplace-taxonomy--pattern-3-managed-models-retreat-when-prices-turn}
### Pattern 3: managed models retreat when prices turn

The most expensive moves were down to the managed rung.

- **Zillow Offers**, Zillow's iBuying business, was wound down on 2 November 2021, with a "$304.4 million write-down of inventory" in the quarter and the admission: "We have been unable to accurately forecast future home prices at different times in both directions" ([Zillow 8-K and shareholder letter, 2021](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm)).
- **OLX Autos**, an inventory-holding "buy, recondition, sell" business, reached $1.6 billion of revenue in the year to March 2022, just over half of OLX's classifieds revenue, before losses of $206 million in the following half-year led Prosus to announce its exit in March 2023 ([News24/Fin24, 2023](https://www.news24.com/fin24/companies/prosus-looks-to-ditch-olx-autos-business-as-second-hand-car-market-slows-20230302)). All operations were disposed of, held for sale or closed by March 2025.
- **CarGurus** decided on 6 August 2025 to wind down CarOffer, its digital wholesale business, which had "proven less effective in today's more volatile and unpredictable pricing environment", and to focus on "technology and analytics that will enable smarter sourcing and pricing decisions rather than facilitating the transactions themselves" ([CarGurus 10-K for 2025, filed 2026](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm)).

The common thread is that **the managed rung changes what a model error costs**, not that transactions are bad. A valuation that is 7% off is useful information on a listing page; the same error is a balance-sheet loss when the platform buys at the estimate and sellers whose homes are overvalued accept while the rest walk away. Classifieds groups have strong audience economics and weak experience of holding inventory, and the documented retreats show that the systems, the processes and the capital structure were built for the rungs above.

{id: marketplace-taxonomy--pattern-4-lead-generation-moves-closer-to-the-deal}
### Pattern 4: lead generation moves closer to the deal

Vertical portals have found a middle path: taking part in more of the deal without holding the money or the asset. Autotrader's Deal Builder lets buyers start a deal and reserve a car online; Autotrader reports that such enquiries "convert at double the rate". The same results attribute part of a 1.7% drop in average retailer forecourts in the second half of the year to "concerns with the speed and nature of our Deal Builder product roll-out" (FY26 results, above). mobile.de's 2026 platform update added an AI call assistant and a lead API "so that leads are transferred directly and securely into existing CRM systems" ([mobile.de, 2026](https://newsroom.mobile.de/plattform-update-sommer-2026/)). **The lead-generation endpoint is being extended toward reservations and deal steps**, and the Autotrader case shows that professionals can push back when the platform's new step changes their own workflow.

{id: marketplace-taxonomy--veldmark-four-brands-twenty-profiles}
### Veldmark: four brands, twenty profiles

Ingrid's grid became the **marketplace profile register**, a short, versioned table that the architecture advice forum reviews whenever a brand proposes to change its model. Each row is one profile: brand × country × category group. The summary:

| Brand | Profiles | Endpoint | Seller type | Money flow | Risk carried by Veldmark | Monetization (2026) |
| --- | --- | --- | --- | --- | --- | --- |
| **Tradeyard** goods (NL, BE, PL) | 3 | Contact; payment and pickup or delivery for Safe Deal orders | 78% private | Adyen for Platforms for Safe Deal; otherwise off-platform | Buyer protection on Safe Deal orders | VAS, pro subscriptions, Safe Deal buyer fee of 5% + €0.70 |
| **Tradeyard** goods (PT) | 1 | Contact | Mostly private | Off-platform | None beyond trust and safety | VAS, pro subscriptions |
| **Tradeyard** vehicles, property, jobs (PL, PT) | 6 | Contact | Mixed | Off-platform | None | Insertion fees (PL vehicles and property), VAS |
| **Motorvane** (DE, NL, PL, AT) | 4 | Lead delivered to a dealer | 91% of listings from 21,400 dealers | Off-platform; financing referred to partners | Lead-billing disputes | Dealer subscriptions with slots, depth products, lead and financing referral fees, private-seller fees |
| **Hearthly** sale, rent, new builds (FR, ES) | 6 | Lead delivered to an agency or developer; tenant application file for rentals | 84% of listings via feeds from about 160 software vendors | Off-platform; settles at the notary or lease signing | None on transactions | Agency subscriptions, new-build campaigns, Valuo data and seller leads, rental services |
| **Keybridge** (FR, BE, ES) | — | Not a marketplace: SaaS for 9,800 agencies | Professionals only | SaaS billing | Data-custody and neutrality obligations | SaaS subscriptions |

Read across the rows and Noor's proposal shrinks: a shared order and payment platform serves three Tradeyard profiles today and might serve others later, for example Tradeyard Portugal's goods categories, where Safe Deal is not yet live. It does not serve Motorvane, whose dealers want qualified leads in their own systems, or Hearthly, whose transactions settle at a notary. What *every* profile needs is shared beneath the endpoint: identity, listing management, media, search, messaging, trust and safety and a product catalog with entitlements. That is the list the Common Ground program already contained, and the register made the reason explicit.

The book's two running examples, Femke's city bike and the Essen Golf, sit on different rungs. When Femke sold her **€240** Rotterdam city bike on Monday 8 March 2027, the sale went through Safe Deal "pay at pickup" for **€225**, with a buyer fee of **€11.95** (5% × €225 = €11.25, plus €0.70): a transactional endpoint inside a classifieds brand. When Autohaus Ruhrblick in Essen listed a 2021 Volkswagen Golf for **€21,900** on Motorvane on Wednesday 14 April 2027, the platform's job ended at **23 leads in 10 days** (14 e-mails, 7 calls and 2 test-drive bookings; 19 once repeat contacts from the same buyers are merged); the sale on 29 April happened in the showroom, and Motorvane learned of it only when the dealer's feed removed the car 26 hours later. Both were successes of different models, measured by different events and served by different systems above a common listing core.

![Two panels on one shared listing core: a city bike handed over after an on-platform payment, and a car dealership receiving 23 leads.](listing-systems-architecture/posts/01-marketplace-taxonomy/assets/images/01-marketplace-taxonomy/two-successes-two-rungs.jpeg)

**Figure 3:** *Two successes on two rungs: Femke's €225 bike sale completed through Safe Deal, while the Essen Golf succeeded as 23 leads in 10 days, both served from the same listing core.*

The Polish overlap was resolved as a commercial decision first and an architectural one second. In the register, Tradeyard Poland's vehicles profile stayed classifieds with insertion fees for private sellers. Dealers with more than a small number of listings were offered Motorvane packages, with an option to show their stock on Tradeyard through Motorvane's feed. The architecture consequence was a **syndication contract** between two brands of the same group rather than two competing dealer sales motions, and a requirement that the shared listing core should know which brand owns the commercial relationship for each listing.

{id: marketplace-taxonomy--trade-offs-where-should-the-marketplace-end}
## Trade-offs: Where Should the Marketplace End?

Every marketplace leadership team keeps returning to one question: should we move the endpoint? The options and their costs:

| Option | What you gain | What you take on | When it is right | When it is wrong |
| --- | --- | --- | --- | --- |
| **Stop at the contact** (classifieds) | Lowest friction for supply; small set of contexts; high margins in verticals | No outcome data; fraud concentrates in messaging; monetization limited to visibility and access | Local pickup goods, high-value unique items, thin markets where friction kills supply | Shippable goods where buyers fear non-delivery more than they value low fees |
| **Own the lead** (lead generation) | Pricing on value delivered; renewal arguments backed by data | Lead qualification, routing, deduplication, attribution; pro CRM integrations; disputes over lead counts | Professional supply with high ticket sizes: cars, property, jobs, services | Private C2C supply, where there is no one to pay for a lead |
| **Own the transaction** (transactional) | GMV visibility, buyer protection, take rate, fraud converted into disputes | Orders, payments via partner, shipping, disputes, ledger, provisioning, DAC7 and trader checks | Shippable goods with moderate prices and repeat buyers | Homes and most cars, where money moves through notaries, banks or dealers |
| **Own the outcome** (managed) | High revenue per transaction; control of quality and price | Inventory and price risk, operations, capital, valuation accuracy under adverse selection | Narrow, well-understood segments with predictable resale prices and sufficient capital | As a growth bolt-on to a high-margin classifieds business when prices are volatile |
| **Hybrid, category-gated** | Each category ends where its buyers need it to | A platform that must run several endpoints and switch them by configuration | Almost every horizontal group of meaningful size | When the gate lives in code, so every change needs a release |

Two judgements follow from this table and from the documented cases.

First, **I would treat every move down the ladder as a bet with an exit plan**. The bet is reasonable: buyer protection measurably reduces some fraud, and shipping widens the market beyond the buyer's city. But the decision should define the categories, the metrics that will show whether it works and the conditions under which the business would retreat, and the architecture should make the retreat cheap. OLX's de-prioritization of pay-and-ship is what a cheap retreat looks like from the outside. Adevinta's parallel running of central and local services during its 2025 decentralization, which more than doubled its cloud-provider emissions temporarily according to its 2025 strategic report, is what an expensive reversal looks like.

Second, **the endpoint should be data, not code**. A category gate expressed as configuration ("Safe Deal: enabled for NL goods, BE goods, PL goods; not PT; not vehicles") lets the business move categories without a program. A gate expressed as `if brand == 'tradeyard' and country != 'PT'` in a checkout service, a ranking feature and a notification template turns each commercial decision into a cross-team release. The exception is a marketplace that will only ever run one model, such as a pure jobs board; it gains little from generalizing the endpoint. Few groups stay that simple for long.

![Diagram: The endpoint as configuration](listing-systems-architecture/posts/01-marketplace-taxonomy/assets/images/01-marketplace-taxonomy/fig04-endpoint-configuration-profile-register-decides-per.jpeg)

**Figure 4:** *The endpoint as configuration. The profile register decides, per country and category, which contexts a listing flows through after contact and which event counts as success; the listing core and the contact surface stay the same for every profile.*

{id: marketplace-taxonomy--vertical-differences}
## Vertical Differences

The endpoint and the other axes take typical values in each vertical. [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) covers the full comparison; this table shows only the taxonomy view.

| Vertical | Typical endpoint | Supply | Item identity | Money flow | Monetization unit | Taxonomy trap |
| --- | --- | --- | --- | --- | --- | --- |
| **General classifieds** | Contact; payment for shippable goods | Mostly private, long tail of small businesses | Weak; free text and photos | Off-platform, or via the PSP for protected sales | Per listing, per bump, per buyer fee | Treating a hybrid as one model and forcing checkout on pickup categories |
| **Real estate** | Lead to an agency or developer; rental applications | Agencies via feeds from software vendors; some owners | Strong: address and parcel; many listings per property | Off-platform, at notary or lease signing | Per advertiser subscription (Rightmove), per listing paid by the seller (Hemnet), commission share (AVIV France) | Mistaking a seller-lead valuation business for a feature |
| **Automotive** | Lead to a dealer; increasingly reservation or deal steps | Dealers via dealer management system (DMS) feeds; private sellers | Strong: VIN or plate | Off-platform, with financing referrals; managed models where the platform buys cars | Per dealer forecourt with stock-based slots (Autotrader ARPR) | Drifting into inventory risk (CarOffer, OLX Autos) |
| **Jobs** | Application delivered to an employer | Employers, agencies, career-site and applicant-tracking feeds | Probabilistic: titles mapped to occupation taxonomies | No consumer payment | Packages per posting, or pay per click or started application (Indeed) | Becoming an ad-tech auction without the systems for it |
| **Recommerce** | Completed payment and delivery | Private sellers at very high volume; separate professional channel | Weak, with brand, size and condition attributes | Through a PSP or the platform's own licensed entity | Buyer fee, shipping, promoted items | Underestimating dispute, ledger and logistics load |

Indeed's pricing page shows what the jobs endpoint becomes when it is monetized by performance: billing on "job seeker interactions like clicks or started applications", with some jobs available only as sponsored listings ([Indeed, n.d.](https://www.indeed.com/hire/pricing)). Vinted's separation of commercial sellers into a Vinted Pro channel, because "businesses have legal obligations that private sellers don't" ([Vinted, 2026](https://company.vinted.com/newsroom/qa-commercial-selling)), shows the seller-type axis enforced in product and software.

{id: marketplace-taxonomy--failure-modes}
## Failure Modes

The taxonomy fails in practice in seven recognizable ways.

**One model assumed for the whole group.** The most common mistake is the one in Noor's first slide: a shared platform designed for the model of the largest or loudest brand. A listing service with a mandatory order object, a checkout embedded in the contact flow or an identity system that requires payment-grade KYC before posting will fit transactional goods and hurt everyone else. This is how **The Forced Fit** begins. Brands whose job ends at a lead or a contact find that the platform makes them slower, and they route around it.

**The endpoint hidden in code.** When the model is never written down, it is encoded implicitly in dozens of places: a ranking feature that assumes purchases exist, a notification that promises buyer protection in a category without it, a billing rule that counts contacts as leads. Changing a category's endpoint then means first finding every place that assumes it. The symptom is that nobody can answer "which categories in which countries have protected payment?" without reading code.

**A transactional pivot launched as a feature.** Payments look like a checkout screen to product teams and like a ledger, a dispute desk, a provisioning policy and a set of tax reports to finance and compliance. A pivot that ships the screen before the rest produces payouts that cannot be reconciled, disputes handled by e-mail and reporting obligations discovered after the first year. [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) describes the minimum set.

**Contact-stage fraud ignored because "we do not handle money".** A classifieds platform does not handle money, but its messaging is where money is negotiated. Fraud therefore concentrates at the endpoint, including fake payment links that impersonate the platform's own protected-payment brand. Veldmark's first worked example contains one: at 20:11 on Sunday 7 March 2027, a "buyer" sent Femke a fake Safe Deal payment link from a domain registered that day. Designing the endpoint without designing its abuse is **Fast Mail for Fraudsters**. [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) and [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) own the countermeasures.

**Revenue from different rungs treated as comparable.** Transaction GMV, take-rate revenue and principal revenue from selling inventory are not comparable with subscription revenue. OLX Autos briefly made up just over half of OLX's classifieds revenue while losing money. An architecture that reports all of them in one "revenue" field makes portfolio decisions harder.

**The success event borrowed from the wrong model.** A lead-generation portal that optimizes for page views, or a transactional marketplace that optimizes for contacts, optimizes the wrong thing. That is **Vanity Liquidity**, and its root cause is often a taxonomy that was never agreed.

**Neutrality conflicts in professional software.** A group that owns software used by professionals to publish to rival marketplaces holds data it must not use for its own portal. Keybridge publishes Veldmark's agencies' listings to Hearthly's competitors. Veldmark's March 2027 decision that no Keybridge agency data is used by Hearthly for ranking or sales targeting, with access controls and an annual independent review, is a taxonomy decision as much as a governance one: Keybridge is a SaaS business with SaaS obligations, not a supply channel for Hearthly.

{id: marketplace-taxonomy--the-chief-architect-s-view}
## The Chief Architect's View

At group scale, the taxonomy is less a classification exercise than a set of standing decisions. Four matter most.

**Make the profile register an architecture artifact.** Every marketplace in the group should have a written profile per country and category, reviewed when it changes: endpoint, seller mix, item identity, money flow, risk owner and the event that counts as success. At Veldmark it is a table of twenty rows that fits on one page and is versioned like any other decision record. Its job is to stop shared platforms from being designed around an assumed model, and to make the cost of a model change visible before the commercial decision is final.

**Separate the decision rights.** Moving an endpoint is a commercial decision owned by the brand's general manager and the Group CPO, with finance and legal involved because it changes licences, provisions and reporting. The architecture function does not own the decision, but it owns the **cost of change** and should be consulted early enough to influence it. A rule I use: no move down the ladder is approved without a named owner for disputes, reconciliation and the regulatory switches it turns on.

**Share beneath the endpoint first.** The capabilities every profile needs (identity, listing management, media, search, messaging, trust and safety, the product catalog and entitlements, the event backbone) are the natural candidates for shared platforms. Contexts that exist only for one rung (orders and payouts for transactional goods, lead attribution for verticals) should be shared only among the profiles that use them. Adevinta's 2019 rule, which centralized areas "where investment requirements are large and the technology is uniform", is a good default; its 2023–2025 swing from converging whole product platforms to decentralizing again shows why the rule should be applied per capability, not per brand ([Adevinta Annual Report 2019, published 2020](https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf)). [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) and [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) develop this.

**Design for movement in both directions.** The documented record contains as many retreats as advances. Endpoint configuration, category-scoped contexts and separable data (orders and payments kept apart from the listing core, leads kept apart from conversations) make a retreat a configuration change and a data-retention plan, not a migration program.

What to watch at group level: the share of contacts, leads and orders per profile; whether the success event in ranking and experimentation matches the profile; the regulatory switches each profile has turned on; and the cost per profile of the contexts it uses. When a profile's endpoint changes, all four should change with it.

{id: marketplace-taxonomy--questions-to-ask}
## Questions to Ask

Take these into a design review or a strategy discussion about a marketplace model:

1. For each country and category, where does our job end today, and where do we intend it to end in three years?
2. Which event counts as success in our ranking, our experiments and our sales materials, and is it the same event in all three?
3. Who holds the buyer's money between payment and handover, and which licensed entity is responsible for it?
4. If a deal goes wrong, who loses money first, and where is that provision recorded?
5. Is the category gate for protected payment, lead products or reservations configuration or code? How long would it take to move one category?
6. Which regulatory obligations switch on if we move a category one step down the ladder (trader traceability, seller tax reporting, payment licensing), and who owns each?
7. Which of our shared platforms assume a specific endpoint, and which brands does that assumption hurt?
8. If we had to retreat from a transactional or managed model in one category next year, what data would we have to keep, for how long, and in which system?
9. Do we own software used by professionals to publish elsewhere, and what prevents our marketplaces from using its data?

{id: marketplace-taxonomy--from-model-to-liquidity}
## From Model to Liquidity

The taxonomy tells a marketplace where its job ends. It does not tell it whether the job is being done well. A classifieds platform, a lead-generation portal and a transactional marketplace all sell the same thing underneath: the probability that a buyer and a seller find each other, in a given place and category, quickly enough that both come back. [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) defines that probability, explains why it is local and winner-take-most, and turns it into the metrics that later chapters convert into freshness, latency and alerting requirements.

{id: marketplace-taxonomy--sources-and-evidence}
## Sources and Evidence

{id: marketplace-taxonomy--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Adevinta Annual Report 2023 (Exhibit 99.1 to eBay 10-K/A)](https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm) — Adevinta ASA, 2024. Revenue by type (classifieds, advertising, transactional), French margin dilution, transactional history of Marktplaats and leboncoin, Kleinanzeigen ambition, convergence plan.
- [Adevinta Annual Report 2019](https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf) — Adevinta ASA, 2020. leboncoin's 2019 transactional launch; the "built once; used many times" centralization rule.
- [Strategic Report 2025, Aurelia UK Feederco Ltd](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf) — Adevinta group, 2026. Move to a decentralized operating model; temporary parallel running of central and local services.
- [Full year results for the year ended 31 March 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf) — Autotrader Group plc, 2026. ARPR, 70% margin, Deal Builder conversion and forecourt decline, Autorama vehicles on balance sheet.
- [Full-year results 2025 (RNS)](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf) — Rightmove plc, 2026. ARPA definition and level, 70% underlying operating margin.
- [Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm) — Zillow Group, 2026. Share-of-voice and pay-at-close pricing; variable consideration.
- [Form 8-K and shareholder letter, 2 November 2021](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm) — Zillow Group, 2021. Zillow Offers wind-down and inventory write-down.
- [Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1057352/000105735226000020/csgp-20251231.htm) — CoStar Group, 2026. Homes.com "your-listing your lead" model.
- [Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm) — CarGurus, 2026. CarOffer wind-down and rationale.
- [Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm) — eBay Inc., 2026. Take rate definition and value; buyer-protection losses.
- [Financial results 2025](https://company.vinted.com/newsroom/financial-results-2025) — Vinted, 2026. GMV, revenue, vertically integrated shipping and payments.
- [Vinted Pay](https://company.vinted.com/newsroom/vinted-pay) — Vinted, 2026. EMI licence and own wallet.
- [Q&A on commercial selling](https://company.vinted.com/newsroom/qa-commercial-selling) — Vinted, 2026. Vinted Pro and the trader/consumer boundary.
- [Price list (US)](https://www.vinted.com/pricelist) — Vinted, updated 2026. Buyer fee ("the Vinted fee", formerly the Buyer Protection fee).
- [Scout24 preliminary results 2025 (in German)](https://www.scout24.com/media/scout24/Investor_Relations/Berichte_und_Praesentationen/2025/Scout24_Preliminary_IR_News_Q4_FY_2025_results_DE.pdf) — Scout24 SE, 2026. Transaction Enablement revenue from CRM, data and valuation.
- [OLX Group FY26 results release](https://www.olxgroup.com/?p=5024) — OLX Group, 2026. Motors, real estate and jobs at 71% of revenue.
- [Learning to Rank: sorting search results](https://tech.olx.com/learning-to-rank-sorting-search-results-b21a8bd48808) — OLX Tech, 2022. Contacts as success labels because transactions are not always confirmed.
- [Machine learning for delivery time estimation](https://tech.olx.com/machine-learning-for-delivery-time-estimation-1-591c8df849a0) — OLX Tech, 2023. Pay&Ship escrow-style flow. Prosus's FY25 results booklet (2025) records its de-prioritization in Europe.
- [Prosus looks to ditch OLX Autos](https://www.news24.com/fin24/companies/prosus-looks-to-ditch-olx-autos-business-as-second-hand-car-market-slows-20230302) — News24/Fin24, 2023. OLX Autos revenue, losses and exit.
- [Plattform-Update Sommer 2026](https://newsroom.mobile.de/plattform-update-sommer-2026/) — mobile.de, 2026. AI call assistant and lead API.
- [Introducing Marketplace](https://about.fb.com/news/2016/10/introducing-marketplace-buy-and-sell-with-your-local-community/) — Meta Newsroom, 2016. Pure classifieds model at launch.
- [Sicher bezahlen](https://themen.kleinanzeigen.de/sicher-bezahlen/) — Kleinanzeigen, n.d. (read 2026). Funds held by the provider until receipt is confirmed.
- [Dit is de vervanger voor de Gelijk Oversteken-functie van Marktplaats](https://radar.avrotros.nl/artikel/dit-is-de-vervanger-voor-de-gelijk-oversteken-functie-van-marktplaats-52677) — AVROTROS Radar, 2022. Kopersbescherming via OPP; withdrawal of Gelijk Oversteken.
- [SeLoger parent AVIV France to add 300 employees in 2023](https://www.onlinemarketplaces.com/articles/seloger-parent-aviv-france-to-add-300-employees-in-2023) — OnlineMarketplaces, 2023. Commission-share monetization of seller leads.
- [Indeed pricing](https://www.indeed.com/hire/pricing) — Indeed, n.d. (read 2026). Pay per click or started application.

{id: marketplace-taxonomy--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Directive (EU) 2019/2161 (Omnibus Directive)](https://eur-lex.europa.eu/eli/dir/2019/2161/oj) — Official Journal of the EU, 2019 (text checked via the EU Publications Office, October 2026). "Online marketplace" definition; ranking-parameter disclosure.
- [Regulation (EU) 2022/2065 (Digital Services Act)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) — Official Journal of the EU, 2022 (text checked via the EU Publications Office, October 2026). Article 30, traceability of traders.
- [Information about DAC7 for platform operators](https://belastingdienst.nl/wps/wcm/connect/en/business/content/information-for-platform-operators-dac7) — Belastingdienst, n.d. Seller reporting obligations for platform operators.

{id: marketplace-taxonomy--research-and-practitioner-sources}
### Research and practitioner sources

- [The spawn of craigslist](http://thegongshow.tumblr.com/post/345941486/the-spawn-of-craigslist-like-most-vcs-that-focus) — Andrew Parker, 2010. Unbundling of horizontal classifieds into verticals.
- [All Markets Are Not Created Equal](https://abovethecrowd.com/2012/11/13/all-markets-are-not-created-equal-10-factors-to-consider-when-evaluating-digital-marketplaces/) — Bill Gurley, 2012. "If you bring the cash, you are king": the economics of being in the payment flow.
- [13 Metrics for Marketplace Companies](https://a16z.com/13-metrics-for-marketplace-companies/) — Andreessen Horowitz, 2020. GMV versus revenue; why classifieds report other denominators.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
