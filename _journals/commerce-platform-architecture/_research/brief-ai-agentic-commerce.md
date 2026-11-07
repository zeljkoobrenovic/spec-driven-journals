# Research brief: AI in commerce systems and agentic commerce (status November 2026)

Prepared 7 November 2026 for chapter writers of *ORDERED: Architecting Commerce Platforms*. Feeds chapter 09 (search and discovery, AI-assisted search at an introductory level) and chapter 45 (AI and agentic commerce: what is real in 2026, the protocols, EU constraints, agent readiness, what not to build yet). The brief is platform-neutral; Shopify, Google, OpenAI, Amazon, Visa and Mastercard get the most space because they published the most dated material, not because the book endorses them.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (7 November 2026) and supports the claim. Paraphrases stay close to the source; quoted text is quoted. The date is the source's publication date. Undated product and documentation pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, legal press, a relayed press release), not from a primary document fetched in this session.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about how a proprietary assistant, ranking model or protocol implementation works internally falls here unless the company has described it.

**Evidence age matters.** This field moved faster than any other in the book between September 2025 and November 2026: the flagship in-chat checkout (OpenAI's Instant Checkout) was launched and pulled back within six months; Amazon renamed its assistant; Shopify replaced one agent API (Storefront MCP catalog/cart) with another (UCP) within a year. Sources older than about three years are flagged **(evidence age)**; the 2003 Amazon paper, the 2017 DeepAR paper and the 2019 Amazon Science history are cited for history, not for current systems.

**Volatility.** ⚠ marks claims likely to change within 12 months: protocol status, product names, buyer-market lists, fees, court outcomes. Chapter writers should re-check every ⚠ row of the status table (Part 6) before publication.

**Research limitation.** The shared web-search quota ran out near the end of the session, and several primary pages refused automated fetching (HTTP 403/503): Amazon's Conditions of Use (so the "Agent Terms" are known only through legal press), GeekWire, MediaPost, Finextra's news section, Adobe's own blog post on agentic standards (timed out twice; relayed by Glenbrook and Digital Commerce 360), and Digital Commerce 360's Adobe article (paywalled). OpenAI's own Instant Checkout announcement and its March 2026 statement were not fetched from openai.com; the Stripe release and two trade-press reports carry those facts. No usage or revenue figure for any agent checkout program (Instant Checkout, UCP, Perplexity Instant Buy, Shopify agentic channels) was found anywhere, from any party. Zalando's November 2026 shopping agent is verified from Zalando's Q3 release, but Zalando's conversion claim for its Assistant comes from secondary coverage only. Independent (non-vendor) measurements of AI results in commerce are rare; where only vendor claims exist, the brief says so.

---

## PART 1: Established AI uses in commerce, and what the evidence says

### 1.1 Search, recommendations and personalization

- Amazon's item-to-item collaborative filtering was described in the 2003 paper by Linden, Smith and York; Amazon says the algorithm had already been in use for six years when the paper appeared, and in 2017 *IEEE Internet Computing* honoured it as the paper from its history that best withstood the test of time. Amazon's own history also records that a 2014-onward deep-learning model for Prime Video first underperformed both item-to-item filtering and a plain bestseller list, and only beat them after it was reframed to predict the next two weeks of viewing from chronologically sorted data [VERIFIED: https://www.amazon.science/the-history-of-amazons-recommendation-algorithm, published 2019-11-22] **(evidence age: 7 years; describes history, not the current system)**.
- Zalando announced a beta fashion assistant built on ChatGPT on 19 April 2023, for a selected group of customers in Germany, Austria, the UK and Ireland, in English and German, letting shoppers search "using everyday fashion language" [VERIFIED: https://corporate.zalando.com/en/node/10422, published 2023-04-19].
- By Zalando's 2025 results (March 2026) the Zalando Assistant had 6 million users, four times more than a year earlier; AI-generated product content made up about 90% of marketing materials; and Zalando said AI-driven supply-chain models improved the accuracy of delivery promises by 22 percentage points [WIDELY REPORTED: https://www.retailgazette.co.uk/blog/2026/03/zalando-reports-strong-2025-growth-as-ai-strategy-drives-performance/, 2026]. Zalando's Q3 2026 release says "More than 22 million unique users visited the Zalando Assistant this year" [VERIFIED: https://corporate.zalando.com/en/financials/zalando-q3-2026-results, published 2026-11-03]. The claim that Assistant users are "twice as likely to complete a purchase" appears only in secondary coverage [WIDELY REPORTED: https://www.analyticsinsight.net/news/zalando-launches-first-ai-shopping-agent-as-margins-slip-in-q3-2026, 2026] ⚠ (self-reported, no method).
- Hosted search vendors describe "AI search" as hybrid vector plus keyword retrieval. Algolia's product page lists NeuralSearch as "Hybrid vector and keyword-powered search" and claims results in 1–20 ms, with no dated result figures [VERIFIED: https://www.algolia.com/products/ai-search/, n.d., accessed 2026-11]. Constructor markets a "Commerce Reasoning Engine" spanning search, browse and recommendations, and headlines a "13% lift in ecommerce conversions" for Petco, with no baseline, period or method given [VERIFIED: https://constructor.com/, n.d., accessed 2026-11] ⚠ (vendor claim).

**What the evidence says.** [ASSUMPTION/JUDGEMENT] The only dated, non-vendor evidence in this section is Amazon's own admission that a strong baseline (bestsellers, item-to-item) is hard to beat and that model reframing, not model size, produced the gain. Every percentage lift from a search or recommendation vendor in this brief is a vendor case study without a published control. Writers should present lifts as "the vendor reports", never as established.

**For newcomers.**
- *Collaborative filtering*: recommending items from patterns of what other shoppers bought or viewed together, without understanding the items themselves.
- *Vector (semantic) search*: search that matches the meaning of a query to product text through numeric embeddings, so "waterproof jacket" can match "rain shell"; usually combined with classic keyword matching ("hybrid search").
- *Search index*: a separate, query-optimised copy of the catalog; it is always slightly behind the catalog it copies.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] AI search does not remove the index-as-a-copy problem; it adds a second derived artifact (embeddings) that also goes stale and must be rebuilt when product text changes. Starting: use the platform's built-in or a hosted search service; measure zero-result rate before buying AI features. Growing: a hosted AI search service fed from the catalog's change events. Omnichannel: one search service shared by storefront, app and store associates, with per-channel assortments and B2B contract prices applied after retrieval. Group: a shared discovery platform with per-brand indexes and merchandising rules.

### 1.2 Content generation

- Amazon launched generative-AI listing tools in September 2023 (text prompt; later product image; and in a later post, a URL to the seller's own product page). Amazon reports that more than 100,000 selling partners have used them and that sellers accept suggested attributes "nearly 80% of the time", calling this "still early days"; the comparison method behind its quality claim is not described [VERIFIED: https://www.aboutamazon.com/news/innovation-at-amazon/amazon-generative-ai-powered-product-listings, n.d. (references a "last fall" launch), accessed 2026-11] ⚠ (vendor claim).
- Shopify's Summer '23 Edition introduced "Shopify Magic" as the brand for AI built into Shopify (blog posts, email subject lines and copy, store text "in 8 languages", Inbox replies, app-review summaries) and announced Sidekick [VERIFIED: https://www.shopify.com/editions/summer2023, published 2023 (page labelled "Summer '23"), accessed 2026-11]. Shopify's current help page no longer uses the Magic name for these features; it describes product-description, email and Inbox text generation as Sidekick and "other AI features", with availability varying "by plan, device, and language" [VERIFIED: https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic, n.d., accessed 2026-11] ⚠ (naming).

**For newcomers.**
- *Product content*: the title, description, attributes and images a shopper sees; in commerce it lives in the PIM or the platform's product record, and every channel copies it.
- *Attribute enrichment*: AI proposing structured values (colour, material, category) from unstructured text or images, which humans accept or reject.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Generated content must land in the system of record for product data (PIM or platform), not in a channel, or the channels drift apart. Keep a review state ("AI-proposed" vs "approved") on the record, and keep the human-accepted version as the source of truth for feeds to marketplaces and agents (Part 5). At every stage the question is the same: which system owns the text an agent will later read aloud to a shopper?

### 1.3 Customer-service bots: the Klarna case

- Klarna said on 27 February 2024 that its AI assistant had handled 2.3 million conversations in its first month, "two-thirds of Klarna's customer service chats", doing the work of 700 full-time agents, with resolution time under 2 minutes (down from 11), a 25% drop in repeat inquiries and an estimated USD 40 million profit improvement in 2024, across 23 markets and 35+ languages [VERIFIED: https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/, published 2024-02-27] ⚠ (vendor claim).
- In May 2025 Klarna's CEO told Bloomberg the company was rehiring human customer-service staff; the AI chatbots were cheaper but produced "lower quality" output, and "investing in the quality of human support is the way of the future for us". Headcount had fallen 22% to 3,500 during a hiring pause [WIDELY REPORTED: https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396, 2025].

**What the evidence says.** [ASSUMPTION/JUDGEMENT] The Klarna pair is the clearest dated example in commerce of a vendor's own efficiency claim being revised by the same vendor fifteen months later on quality grounds. It argues for measuring resolution quality and repeat contacts, not only deflection, and for designing the hand-off to a human as a first-class path.

**For newcomers.**
- *Deflection*: the share of contacts a bot handles without a human; it says nothing about whether the customer's problem was solved.
- *Order-status API*: the interface a bot (or agent) calls to answer "where is my order"; without it, the bot can only talk.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A service bot is only as good as the APIs behind it: order status, shipment events, return eligibility, refund state. These are the same APIs an external shopping agent will need (Part 5), so building them once, with authentication and a customer-scoped view, serves both. Starting: the platform's own inbox AI. Growing/Omnichannel: a bot in front of the OMS and returns system, with a human queue. Group: a shared service layer per brand with a common order-status contract.

### 1.4 Fraud detection

- Stripe describes Radar as fraud prevention using AI trained on data across the Stripe network, claims a "32% average reduction in fraud" and says 92% of payments come from a card Stripe has seen before; no accuracy or false-positive rate is published [VERIFIED: https://stripe.com/radar, n.d. (page served in Dutch; © 2026), accessed 2026-11] ⚠ (vendor claim).
- Visa and Mastercard's agent programs fold fraud control into agent identity: Visa's Trusted Agent Protocol lets "merchants recognise verified AI agents and separate them from unverified traffic", and in Visa's B2B pilot the protocol is said to "satisfy the site protections historically provided by CAPTCHA" [VERIFIED: https://www.visa.co.uk/about-visa/newsroom/press-releases.3457328.html, published 2026-07-02; https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.22856.html, published 2026-10-20].

**For newcomers.**
- *Fraud screening*: a score computed before or after authorization from device, address, velocity and network signals; the PSP usually does it, the merchant decides the thresholds.
- *Chargeback*: the cardholder's bank reversing a payment after a dispute; the merchant bears it unless liability shifted (for example through 3-D Secure).

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Fraud scoring belongs in the PSP or a specialist, fed with order context the merchant supplies (customer tenure, shipping address match). Agent traffic breaks the assumption behind most bot defences, namely that a non-human session is hostile; the merchant will need a policy that distinguishes verified agents from scrapers (Part 5.4). At Growing scale this is a PSP setting; at Omnichannel scale it is a rule set shared by web, app and agent channels.

### 1.5 Demand forecasting and inventory planning

- Amazon researchers published DeepAR (probabilistic forecasting with autoregressive recurrent networks, trained across many related time series) on arXiv in April 2017, with retail demand forecasting as a motivating case [VERIFIED: https://arxiv.org/abs/1704.04110, published 2017-04-13, revised 2019-02-22] **(evidence age: 9 years; a method paper, not a description of Amazon's current forecasting)**.
- Zalando researchers published a case study of deep-learning demand forecasting in online fashion in May 2023, arguing that global data-driven models suit large catalogs with irregular demand and high turnover, with the price–demand relationship controlled explicitly; the abstract does not name Zalando or give scale [VERIFIED: https://arxiv.org/abs/2305.14406, published 2023-05-23].

**For newcomers.**
- *Demand vs sales*: sales are what the data shows; demand is what customers wanted, which only appears when stock was available, so forecasting from sales alone underestimates demand for items that sold out.
- *Probabilistic forecast*: a range (quantiles) rather than a single number, so a buyer can choose a service level.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Forecasting lives beside the ERP/planning system and consumes clean sales, stock-out and price history; its outputs (purchase advice, replenishment quantities) must flow back as proposals a buyer approves, which is also the shape an "ordering agent" takes later. Starting: spreadsheet. Growing: the ERP or WMS's built-in purchase advice. Omnichannel: a dedicated planning tool or model, fed by the stock-event stream. Group: a shared forecasting service with per-brand parameters.

### 1.6 Two measurements of "AI traffic" (and why they differ)

- Adobe Analytics reported that traffic referred from generative-AI platforms to US retail sites rose 693% year over year in November–December 2025 (769% in November, 673% in December), that AI-referred shoppers converted 31% more often than other sources (54% on Thanksgiving, 38% on Black Friday), and that the gap doubled from 2024; the analysis covered more than one trillion visits, 100 million SKUs and 18 categories [WIDELY REPORTED: https://www.digitalcommerce360.com/2026/01/13/generative-ai-online-holiday-shopping-traffic-2025/, 2026] ⚠. Adobe does not publish AI referrals as a share of total visits, so 693% is growth from a small base [ASSUMPTION/JUDGEMENT].
- Salesforce says AI "influenced" 20% of global online sales in the 2025 holiday season, worth USD 262 billion, based on its own shopper data; this is an influence estimate, not a referral measure, and the two figures cannot be compared [VERIFIED: https://www.salesforce.com/ap/news/press-releases/2026/07/06/as-ai-agents-transform-commerce-salesforce-unleashes-its-biggest-agentforce-commerce-release-yet/, published 2026-07-06] ⚠ (vendor method).

---

## PART 2: Merchant-side and shopper-side assistants (dated)

### 2.1 Shopify Sidekick and the Shopify Magic features

- Sidekick was announced in the Summer '23 Edition (July 2023) [VERIFIED: https://www.shopify.com/editions/summer2023, 2023]. On 21 May 2025 Shopify said Sidekick works in "all 20 languages supported in the Shopify admin", by text and voice with screen sharing, had been rebuilt with enhanced reasoning, could run reports, create segments, filter orders and set up discount codes "with the merchant's approval", and generated images [VERIFIED: https://www.shopify.com/blog/expanding-your-ai-horizons-summer-edition-25, published 2025-05-21].
- Shopify's help page (n.d.) describes Sidekick as planning multi-step tasks and running them in the background, building Shopify Flow automations, generating custom apps, following saved "skills", writing and running code to forecast or summarise store data, searching the web, editing orders, and presenting changes for review before applying them [VERIFIED: https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick, n.d., accessed 2026-11]. The general-availability date is not stated on any Shopify page read in this session [ASSUMPTION/JUDGEMENT: unknown].
- Sidekick app extensions (apps exposing data and actions to Sidekick) were a developer preview on 10 December 2025 [VERIFIED: https://www.shopify.com/news/winter-26-edition-renaissance, published 2025-12-10]. The Fall '26 Edition says daily Sidekick sessions grew 4.2x year over year and that Sidekick tests recommendations in a simulator ("SimGym") before a merchant approves a plan [VERIFIED: https://www.shopify.com/editions/fall2026, n.d. (Fall '26), accessed 2026-11] ⚠ (vendor figure).

### 2.2 Amazon: Rufus, "Alexa for Shopping" and "Buy for Me"

- Amazon's own Rufus page states: "On May 13, 2026, Rufus was renamed Alexa for Shopping." The same page lists more than 50 upgrades, account memory, photo search, a 30/90-day price tracker, price alerts and **Auto-Buy** (for Prime members: buy at a target price with the default payment method and address, notification with 24-hour free cancellation, requests live six months), and says Rufus runs on Amazon Bedrock with Anthropic's Claude Sonnet, Amazon Nova and a custom model. It claims "more than 250 million customers" used Rufus "this year", monthly users up 149% and interactions up 210% over the past year, and that users are over 60% more likely to buy during that trip [VERIFIED: https://www.aboutamazon.com/news/retail/amazon-rufus-ai-assistant-personalized-shopping-features, n.d. (post-May-2026 note), accessed 2026-11] ⚠ (period of the figures unclear).
- Trade coverage of the 13 May 2026 announcement: Alexa for Shopping merges the Rufus chatbot with Alexa+, rolls out to all US customers over the following week in the Shopping app, Amazon.com and Echo Show devices, requires no Prime membership or Echo device, and adds **Scheduled Actions** (time- or condition-based automations such as monthly cart additions or purchases on a price drop) and **Buy for Me** [WIDELY REPORTED: https://www.ecomcrew.com/amazon-retires-rufus-and-launches-alexa-for-shopping-as-its-unified-ai-assistant/, 2026; https://www.artificialintelligence-news.com/news/amazon-alexa-for-shopping-rufus-ai-assistant/, 2026]. The second report, citing GeekWire, says Rufus helped more than 300 million customers in 2025 and that CEO Andy Jassy reported Rufus monthly active users up more than 115% and engagement up nearly 400% year over year [WIDELY REPORTED, same, 2026]. **Verdict on the renaming question: yes, verified against Amazon's own page; US-only at launch.** ⚠
- **Buy for Me** was announced on 10 April 2025 as a test for "a subset of U.S. users" on iOS and Android: Amazon buys eligible branded items from third-party brand sites on the customer's behalf; the brand handles delivery, returns and service; orders are tracked in a "Buy for Me" tab [VERIFIED: https://www.retaildive.com/news/amazon-buy-for-me-agentic-ai-thirdparty-sites/745047/, published 2025-04-10].

### 2.3 Salesforce Agentforce Commerce (GA 6 July 2026)

- On 6 July 2026 Salesforce announced its "biggest Agentforce Commerce release yet": a **Shopper Agent** (discovery to checkout and service on the storefront), a **Buyer Agent** for B2B buyers in WhatsApp and SMS, and a **Merchant Agent** for catalog organisation, all generally available; native integration with Google Search (AI Mode) and the Gemini app "in the coming months"; UCP named as the route into external channels. Pricing is "subject to change" and varies by region. Supporting statistics: AI influenced 20% of global online sales (USD 262 billion) in holiday 2025; retailers running shopper agents grew sales 59% faster; AI-referred traffic converts at eight times the rate of social (all Salesforce's own data) [VERIFIED: https://www.salesforce.com/ap/news/press-releases/2026/07/06/as-ai-agents-transform-commerce-salesforce-unleashes-its-biggest-agentforce-commerce-release-yet/, published 2026-07-06] ⚠ (vendor figures).

### 2.4 Shopware Copilot and MCP (10 June 2026)

- At Shopware Community Day (10 June 2026) Shopware said Copilot is "now agentic": it executes actions inside workflows under role restrictions, entity whitelisting and a draft-and-review step with a human; it is hosted on European servers and "moves no data without merchant approval". Shopware claims "100% MCP coverage" (every platform action reachable by agents) and "UCP-readiness"; ACP and AP2 are not mentioned. Figures such as "40% lower integration costs" carry no method [VERIFIED: https://www.shopware.com/en/press/press-releases/shopware-community-day-2026-shopware-becomes-the-open-commerce-infrastructure-for-the-agentic-era/, published 2026-06-10] ⚠ (vendor claims).
- Shopware's developer docs: the MCP server exposes an Admin API endpoint at `/api/_mcp` and a sales-channel-facing Store API endpoint at `/store-api/_mcp`, introduced in Shopware 6.7.11.0, "experimental" until 6.8 (tool names and payloads may change); clients named include Claude, Cursor, Codex, ChatGPT and Shopware Copilot; the Store API server uses the `sw-access-key` header, needs no customer login, has tighter rate limits, and can be advertised by headless sales channels through an "agentic" file family [VERIFIED: https://developer.shopware.com/docs/products/tools/mcp-server.md and https://developer.shopware.com/docs/products/tools/mcp-server/store-api.md, n.d., accessed 2026-11] ⚠ (experimental).

### 2.5 commercetools AgenticLift (21 January 2026) and Adobe (February 2026)

- commercetools launched **AgenticLift** on 21 January 2026 as a standalone offering, also for businesses not on commercetools, to sell through ChatGPT, Gemini and Microsoft Copilot without replacing the existing stack; it builds on commercetools' earlier support for MCP and Stripe/OpenAI's ACP; UCP, pricing and regions are not mentioned [VERIFIED: https://commercetools.com/press-releases/commercetools-launches-agenticlift, published 2026-01-21].
- Adobe said in February 2026 that Adobe Commerce is "moving towards supporting UCP and ACP", making catalogs, prices and stock readable by agents on platforms such as Gemini and ChatGPT; no timeline [WIDELY REPORTED: https://glenbrook.com/payments_news/adobe-commerce-commits-to-agentic-commerce-standards/, 2026; headline confirmed at https://www.digitalcommerce360.com/2026/02/23/adobe-commerce-platform-agentic-ai-standards/, 2026 (paywalled)] ⚠ (commitment, not shipped).

### 2.6 Zalando: from Assistant to its own buying agent (3 November 2026)

- Zalando's Q3 2026 release introduces **Zalando Extended**, "adding products from other online shops" that Zalando does not sell; "Customers will never have to leave the trusted Zalando app" because Zalando's own AI agent buys on their behalf; partner shops join "without complex technical integration or changes to their logistics"; Westwing is the first pilot partner, and from 2027 Zalando's agent is planned to check out Westwing's products inside the Zalando app [VERIFIED: https://corporate.zalando.com/en/financials/zalando-q3-2026-results, published 2026-11-03] ⚠. [ASSUMPTION/JUDGEMENT] This is the European retailer-run counterpart of Amazon's Buy for Me: the marketplace becomes the agent, and the partner merchant's storefront becomes the thing the agent operates.

**For newcomers (Part 2).**
- *Merchant-side assistant*: AI in the admin that helps the merchant run the store (write, analyse, configure, automate); it acts on the merchant's data with the merchant's permissions.
- *Shopper-side assistant*: AI in the storefront or marketplace that helps a customer find and compare; when it can also pay, it becomes an *agent*.
- *Human-in-the-loop / draft-and-review*: the assistant proposes a change and a person approves before it is applied; every vendor in this part describes its agentic features this way.

**Architecture implications (Part 2).** [ASSUMPTION/JUDGEMENT] Every merchant-side assistant above acts through the platform's own APIs and permission model (Sidekick through Shopify admin, Copilot through Shopware's MCP tools, Agentforce through Salesforce objects). For the merchant, the architectural question is not "which assistant" but "do our integrations and customisations expose their data and actions through the same APIs, so the assistant can see them" (Sidekick app extensions and Shopware MCP extensions are exactly that). Starting/Growing: use the platform's assistant; nothing to build. Omnichannel: ensure OMS, PIM and returns expose read/write APIs with scoped permissions, because the assistant's usefulness ends where the platform's data ends. Group: a shared policy on what assistants may change without review (prices, stock, customer data) across brands.

---

## PART 3: Agentic commerce protocols and programs

### 3.1 OpenAI and Stripe: Instant Checkout and the Agentic Commerce Protocol (ACP)

- On 29 September 2025 Stripe announced it was helping OpenAI launch **Instant Checkout** in ChatGPT, with US ChatGPT users able to buy from US Etsy sellers immediately and Shopify merchants "coming soon"; the **Agentic Commerce Protocol** was presented as an open standard usable by businesses not on Stripe; Stripe's **Shared Payment Token** is scoped to one merchant and one cart, and the merchant may process it through Stripe or another provider [VERIFIED: https://stripe.com/newsroom/news/stripe-openai-instant-checkout, published 2025-09-29].
- The ACP repository states: "The specification is maintained by OpenAI and Stripe and is currently in beta"; "ACP is jointly governed by OpenAI and Stripe as Founding Maintainers, with a clear path toward broader community governance", decisions by consensus, "Neutral foundation stewardship as ecosystem matures"; Apache 2.0; CLA required. Spec releases: 2025-09-29 (initial), 2025-12-12 (fulfillment), 2026-01-16 (capability negotiation), 2026-01-30 (extensions, discounts, payment handlers), 2026-04-17 (cart, feed, orders, authentication, MCP; latest stable) [VERIFIED: https://github.com/agentic-commerce-protocol/agentic-commerce-protocol, n.d., accessed 2026-11] ⚠ (beta).
- OpenAI's developer site frames ACP as agentic checkout, delegated payment and product feeds, and says an integration starts by sharing a structured product feed; the standard feed upload "currently targets the US", other markets need OpenAI's confirmation, and checkout requires a separately enabled integration [VERIFIED: https://developers.openai.com/commerce and https://developers.openai.com/commerce/specs/feed, n.d., accessed 2026-11] ⚠.
- **The March 2026 retreat.** On 6 March 2026 an OpenAI spokesperson told Digital Commerce 360: "We're evolving how we approach commerce in ChatGPT to better meet merchants and users where they are"; The Information had reported that Instant Checkout was being sidelined in favour of checkout through merchants' ChatGPT apps, with merchant concerns and transaction complexity (in-store stock, sales tax, pricing) offered as the explanation; ACP continues but "will no longer power purchases made directly from product listings in ChatGPT responses" [VERIFIED: https://digitalcommerce360.com/2026/03/06/openai-shifts-checkout-plans-agentic-commerce-strategy/, published 2026-03-06]. On 12 March 2026 OpenAI said Instant Checkout "is moving to Apps, where purchases can happen more seamlessly", and Shopify's ChatGPT channel became discovery with checkout on the merchant's own storefront (in-app browser on mobile, new tab on web), orders flowing through Shopify checkout [VERIFIED: https://www.modernretail.co/technology/shopify-says-purchases-are-coming-inside-chatgpt-through-agentic-storefronts-as-openai-retreats-on-instant-checkout/, published 2026-03-12]. No usage figure for Instant Checkout was published by any party [ASSUMPTION/JUDGEMENT: unknown].
- PayPal said on 28 October 2025 it would adopt ACP and bring its merchants' catalogs to ChatGPT in 2026 [WIDELY REPORTED: carried in the FEDERATED source list from https://newsroom.paypal-corp.com/2025-10-28-OpenAI-and-PayPal-Team-Up-to-Power-Instant-Checkout-and-Agentic-Commerce-in-ChatGPT; not re-fetched this session] ⚠.

### 3.2 Google: Agent Payments Protocol (AP2) and Universal Commerce Protocol (UCP)

- **AP2** was announced on 16 September 2025 as "an open protocol" for agent-led payments, built on A2A and usable as an extension of A2A and MCP, with "more than 60 organizations" (Adyen, American Express, Coinbase, Etsy, Mastercard, PayPal, Revolut, Salesforce, Worldpay and others). Its core is signed **Mandates**: an *Intent Mandate* (the user's instructions, including price limits and timing for delegated tasks) and a *Cart Mandate* (a "secure, unchangeable record of the exact items and price"), signed as verifiable credentials to give a "non-repudiable audit trail". AP2 is "payment-agnostic" (cards, stablecoins, real-time bank transfers) [VERIFIED: https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol, published 2025-09-16]. The repository is Apache-2.0 and describes itself as "code samples and demos", with the Python SDK not yet on PyPI [VERIFIED: https://github.com/google-agentic-commerce/AP2, n.d., accessed 2026-11] ⚠.
- **UCP** was announced on 11 January 2026 as an open standard covering discovery, buying and post-purchase, co-developed with Shopify, Etsy, Wayfair, Target and Walmart and endorsed by 20+ others (Adyen, American Express, Best Buy, Flipkart, Macy's, Mastercard, Stripe, The Home Depot, Visa, Zalando); checkout started with "eligible U.S. retailers" in AI Mode and the Gemini app, paid with Google Pay, PayPal "coming"; retailers "remain the seller of record" [VERIFIED: https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/, published 2026-01-11].
- ucp.dev: Apache 2.0, copyright "UCP Authors", no named foundation; shopping spec under "latest", lodging "draft", food "coming soon"; capabilities catalog, cart, checkout, identity linking, order; transports REST and JSON-RPC with A2A and MCP "built-in" and AP2 supported; shopping co-developers listed as Google, Shopify, Etsy, Wayfair, Target, Walmart, **Amazon, Microsoft, Meta, Salesforce, Stripe** [VERIFIED: https://ucp.dev/, n.d. (© 2026), accessed 2026-11] ⚠.
- **Who governs UCP.** The organisation's MAINTAINERS file lists a three-person **Governance Council** (Google, Shopify, Stripe; "2 seats open, to be elected"), a Shopping Tech Council (Google, Shopify, Etsy, Meta, **Amazon**, Target, Microsoft, Stripe, Salesforce, Wayfair), plus Food, Lodging and Payments councils (the last including PayPal, Coinbase, Adyen, Global Payments, Ant International), with "per GOVERNANCE.md rules" not described on the page [VERIFIED: https://github.com/Universal-Commerce-Protocol/.github/blob/main/MAINTAINERS.md, n.d., accessed 2026-11] ⚠. The main repository shows no releases or version tags [VERIFIED: https://github.com/Universal-Commerce-Protocol/ucp, n.d., accessed 2026-11]. [ASSUMPTION/JUDGEMENT] UCP is therefore a vendor-led consortium standard with council governance, not a standards-body specification; Google holds the most seats.
- On 20 May 2026 Google announced **Universal Cart** across retailers and surfaces, said the retailer stays merchant of record, and said UCP checkout "will roll out across Canada and Australia in the coming months" and later the UK; Europe was not mentioned [VERIFIED: https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/, published 2026-05-20]. On 16 September 2026 Google said UCP "already enables direct checkout for hundreds of thousands of brands and retailers across Google", that UCP cart transfer in Merchant Center is "rolling out gradually in the U.S. now, with Australia and Canada following early next year", and that merchants adopting feed best practices see "on average, a 5% conversion increase the following month" [VERIFIED: https://blog.google/products-and-platforms/products/shopping/google-shopping-updates-holiday-shopping/, published 2026-09-16] ⚠ ("enables", not "transacts").

### 3.3 Shopify: Agentic Storefronts, Catalog, MCP and UCP

- 10 December 2025 (Winter '26): Agentic Storefronts "available to every merchant" in the admin, syndicating products to "AI chats"; the Catalog API opened through the developer dashboard; Checkout MCP tools in preview for specific partners [VERIFIED: https://www.shopify.com/news/winter-26-edition-renaissance, published 2025-12-10].
- 11 January 2026: UCP co-announced with Google ("works with any payment processor, including Shopify Payments"); selling in Google AI Mode and Gemini "rolling out soon"; Copilot Checkout embedded in Microsoft Copilot; an **Agentic plan** opening Shopify Catalog to brands not on Shopify; no countries listed [VERIFIED: https://www.shopify.com/news/ai-commerce-at-scale, published 2026-01-11].
- Help Center (n.d., accessed 2026-11): channels are ChatGPT (discovery; checkout on the merchant's store), Google AI Mode and Gemini, Microsoft Copilot and Meta surfaces including Muse (Shopify-powered direct checkout in channel when activated), and personal agents paying with Shop Pay; active by default for eligible stores; supplemental terms required [VERIFIED: https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts]. **ChatGPT**: "Your store must sell to customers in the United States" (store may be based elsewhere); B2B-only products unsupported; purchases happen on the store's own checkout [VERIFIED: https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts/chatgpt]. **Google**: direct checkout only for customers in the United States, Canada and Australia; others are redirected to the store; requires a Merchant Center account and feed; subscriptions, bundles, customisable and B2B-only products, local delivery and pickup unsupported; Google Analytics and custom pixels do not fire [VERIFIED: https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts/google] ⚠. **No EU buyer market is in scope on any Shopify agentic channel page read.**
- Agentic plan page: no monthly fee, "Card rates from 1.9% + €0.25 EUR online", channels ChatGPT, Google AI Mode and Gemini, Copilot, Perplexity and the Shop app, with "Get updates on availability" and no country eligibility stated [VERIFIED: https://www.shopify.com/agentic-plan, n.d., accessed 2026-11] ⚠.
- Developer docs: the Storefront MCP catalog and cart tools at `/api/mcp` "were removed" and replaced by UCP endpoints at `/api/ucp/mcp` (Storefront Catalog, Cart, Ask and Order MCP); every request must carry an agent profile; Checkout MCP requires authenticated or signed requests [VERIFIED: https://shopify.dev/docs/apps/build/storefront-mcp, n.d., accessed 2026-11]. The agents overview lists Global Catalog, Storefront Catalog, Cart MCP, Checkout MCP ("completes purchases for trusted agents"), Order MCP (`get_order`), order webhooks, and profiles with trust tiers: "Higher trust tiers unlock broader access, including direct checkout completion"; other agents hand buyers to the storefront to pay; each agent hosts a profile at a well-known URL and references it on every request [VERIFIED: https://shopify.dev/docs/agents, n.d., accessed 2026-11].
- Catalog docs: Global Catalog (`catalog.shopify.com/api/ucp/mcp`, results clustered by Universal Product ID) and Storefront Catalog (`{store}/api/ucp/mcp`), tools `search_catalog`, `lookup_catalog`, `get_product`; some fields are AI-inferred and labelled so; caching limits of 24 hours for metadata and 15 minutes for price and availability; bulk harvesting, model training and standing product databases prohibited; references UCP Catalog spec version 2026-08-25 and warns "Endpoint URLs might change" [VERIFIED: https://shopify.dev/docs/agents/catalog, n.d., accessed 2026-11] ⚠.
- Fall '26 Edition (n.d., content references autumn 2026): a "Shop skill" so ChatGPT, Claude or other agents can discover and check out with Shop Pay; Shop Pay in Muse, Claude Duet, Grok Bot and Instinct; selling in Google Search, AI Mode and Gemini with Shopify checkout; agent connectors for Grok, Gemini, Meta Muse and Copilot to manage the store; a merchant-reviewed knowledge base for agents; "One MCP" for any agent to add shopping; WebMCP tools for stores; UCP `/buy` and `/ask` endpoints; most items "soon", "early access" or "beta", with no countries given [VERIFIED: https://www.shopify.com/editions/fall2026, accessed 2026-11] ⚠.

### 3.4 Perplexity and PayPal

- 14 May 2025: Perplexity selected PayPal for agentic commerce in Perplexity Pro, US first, launching "this summer" [VERIFIED: https://newsroom.paypal-corp.com/2025-05-14-Perplexity-Selects-PayPal-to-Power-Agentic-Commerce, published 2025-05-14]. 25 November 2025: PayPal merchants became discoverable and purchasable in Perplexity for "U.S. users", retailer as merchant of record (Abercrombie & Fitch, Ashley Furniture, Fabletics, Adorama, Newegg), via PayPal's "Store sync" (catalog) and "Agent ready" (payments) services [VERIFIED: https://newsroom.paypal-corp.com/2025-11-PayPal-and-Perplexity-Launch-Instant-Buy, published 2025-11-25] ⚠ (US; current status unverified).

### 3.5 Card networks: Visa Intelligent Commerce and Mastercard Agent Pay

- **Visa Intelligent Commerce** was announced on 30 April 2025: AI-Ready Cards (tokenised credentials confirming an agent is authorised to act for a consumer), consumer-set spending limits and conditions, real-time commerce signals to Visa for controls and disputes, a developer API suite, and partners including Anthropic, IBM, Microsoft, Mistral AI, OpenAI, Perplexity, Samsung and Stripe; Jack Forestell: agents "will need to be trusted with payments, not only by users, but by banks and sellers as well" [VERIFIED (republished release): https://www.silicon.co.uk/press-release/find-and-buy-with-ai-visa-unveils-new-era-of-commerce, published 2025-04-30].
- 14 October 2025: Cloudflare and Visa co-developed the **Trusted Agent Protocol** (TAP) on Web Bot Auth; Mastercard is incorporating Web Bot Auth into Agent Pay; American Express will use it; Adyen, Checkout.com, Fiserv, Worldpay, Microsoft and Shopify gave feedback. Forestell: "Merchants shouldn't have to choose between blocking bots and serving real customers" [VERIFIED: https://www.cloudflare.com/press/press-releases/2025/cloudflare-collaborates-with-leading-payments-companies-to-secure-and-enable-agentic-commerce/, published 2025-10-14].
- 2 July 2026 (Paris): Visa reported live agent-executed purchases at lastminute.com, Frasers, Cleverbridge and BrickDepot, with 31 named European issuers (Barclays, BBVA, CaixaBank, ING, Klarna, Revolut, NatWest and others) having completed live transactions; merchants participate through TAP and an Agent Directory, with Cloudflare and Akamai supporting implementation; every transaction authenticated with Visa Payment Passkeys, "which Visa says supports European Strong Customer Authentication (SCA) requirements"; no volumes; a merchant executive calls it "early days" [VERIFIED: https://www.visa.co.uk/about-visa/newsroom/press-releases.3457328.html, published 2026-07-02] ⚠ (pilot).
- 20 October 2026: Visa, BILL and Billtrust launched a live B2B pilot in which a TAP-registered agent pays approved supplier invoices through supplier portals; geography not stated (Las Vegas dateline, US companies) [VERIFIED: https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.22856.html, published 2026-10-20] ⚠.
- **Mastercard Agent Pay** was announced on 29 April 2025 with **Agentic Tokens** built on existing tokenisation (contactless, card-on-file, passkeys); trusted agents must be registered and verified; partners Microsoft (Azure OpenAI, Copilot Studio), IBM (watsonx Orchestrate, B2B), Braintree and Checkout.com; Mastercard called these its "initial steps" [VERIFIED: https://newsroom.mastercard.com/news/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai, published 2025-04-29].
- 2 June 2026: Mastercard's Europe EVP wrote that "all Mastercard issuers in Europe are enabled at a network level for Agent Pay", that 36 listed banks (including Banco Santander) completed "controlled, live agentic transactions" on Priceless.com using passkeys, and that Mastercard, Worldline and ING completed a live end-to-end transaction with every element based in Europe [VERIFIED: https://newsroom.mastercard.com/news/europe/en/perspectives/en/2026/europe-is-building-the-foundations-for-trusted-agentic-commerce/, published 2026-06-02] ⚠. [ASSUMPTION/JUDGEMENT] "Enabled at a network level" means the rails accept the token type; it does not mean issuers' cardholders can use it, nor that any merchant offers it.

### 3.6 Klarna and Adyen

- Klarna launched the **Agentic Product Protocol** on 15 December 2025 as "a new open standard" for product data exchange with agents, through a hosted API accepting Google Merchant, Shopify, Amazon, Facebook Catalog and CSV/JSON feeds, claiming 100 million+ products, 400 million prices and 12 markets; no adopters named, no relation to other protocols given [VERIFIED: https://investors.klarna.com/News--Events/news/news-details/2025/Klarna-Launches-Agentic-Product-Protocol-The-Open-Standard-That-Makes-100M-Products-Instantly-Discoverable-by-AI-Agents/default.aspx, published 2025-12-15] ⚠ (vendor claim).
- **Adyen Agentic** launched 16 June 2026: Agentic Feed (catalog, pricing, availability), Agentic Cart (orchestration to existing checkout, tax, fulfilment and OMS) and Agentic Payments (authentication, token portability, merchant-of-record preservation, risk); compatible with Meta's AI checkout; Adyen is an early endorser of UCP and also references AP2 and ACP; "limited availability for enterprise merchants operating in the U.S.", global expansion without timeline [VERIFIED: https://www.adyen.com/press-and-media/adyen-agentic, published 2026-06-16] ⚠.

### 3.7 Amazon's position on third-party agents

- 4 November 2025: Amazon sent Perplexity a cease-and-desist over the Comet browser's shopping agent. Amazon's statement: third-party agents should "operate openly and respect service provider decisions whether or not to participate", and "Agentic third-party applications such as Perplexity's Comet have the same obligations"; Perplexity replied that "User agents are exactly that: agents of the user". Amazon cited Conditions of Use clauses against using account information for a third party's benefit and against data mining, robots or similar extraction tools [VERIFIED: https://www.engadget.com/ai/amazon-and-perplexity-are-fighting-over-the-future-of-ai-shopping-215445479.html, published 2025-11-04].
- The case is *Amazon.com Services LLC v. Perplexity AI, Inc.*, No. 3:25-cv-09514 (N.D. Cal.). Amazon added "Agent Terms" to its Conditions of Use in May 2025 requiring automated agents to identify themselves and not to circumvent access controls. A preliminary injunction (March 2026) was vacated by the Ninth Circuit in August 2026, which found Amazon unlikely to succeed on its CFAA and CDAFA claims because the access was attributable to the consumers who directed Comet; Amazon filed an amended complaint on 21 September adding tortious interference with contract; Perplexity moved to dismiss on 13 October 2026; the case continues [WIDELY REPORTED: https://www.thefashionlaw.com/?p=109079, 2026; https://www.ecomcrew.com/?p=67537, 2026] ⚠ (litigation). Amazon's current Conditions of Use could not be fetched (HTTP 503) [ASSUMPTION/JUDGEMENT: unverified text].
- 20–22 September 2026: Amazon blocked Meta's Muse agent from Amazon.com after Meta declined to remove Amazon from the experience; shoppers saw pop-ups saying its use "violates Amazon's terms of use"; Amazon said an opt-in requirement is standard for food-delivery apps and online travel agencies [VERIFIED: https://www.thestar.com.my/tech/tech-news/2026/09/22/amazon-blocks-metas-muse-ai-agent-from-its-retail-site, published 2026-09-22 (Bloomberg report)].
- At the same time Amazon is listed as a UCP shopping co-developer and holds a seat on UCP's Shopping Tech Council (Part 3.2). [ASSUMPTION/JUDGEMENT] Amazon's position is consistent: agents are welcome through channels Amazon controls or consents to (its own Buy for Me, a consortium protocol where it has a seat), and unwelcome when they drive Amazon's consumer site without identifying themselves.

### 3.8 The Model Context Protocol in commerce

- Shopify built Storefront MCP "on Anthropic's Model Context Protocol" (May 2025) [VERIFIED: https://www.shopify.com/blog/expanding-your-ai-horizons-summer-edition-25, published 2025-05-21], then folded its catalog and cart tools into UCP-over-MCP at `/api/ucp/mcp` (Part 3.3). Shopware ships Admin and Store API MCP servers (Part 2.4). Mollie launched an MCP server on 29 July 2025 that lets merchants generate payment links, check payment status, create customer profiles and set up recurring mandates in natural language, with invoicing and subscriptions as future agent areas [VERIFIED: https://financialit.net/news/payments/mollie-launches-ai-ready-mcp-server-help-merchants-automate-and-simplify-workflows, published 2025-07-29].
- [ASSUMPTION/JUDGEMENT] MCP is the tool-calling transport, not a commerce protocol: it says how an agent discovers and calls "look up order" or "create cart"; UCP, ACP and AP2 say what those operations mean, who may call them and how payment is authorised. UCP explicitly rides on MCP (and A2A, REST, JSON-RPC).

**For newcomers (Part 3).**
- *Agentic commerce*: a software agent (usually inside a chat assistant) discovering, comparing and buying products on a person's behalf, as opposed to a person using a storefront.
- *Commerce protocol*: a published contract (feeds, cart, checkout, order, payment token) that lets any agent talk to any merchant without a bespoke integration; ACP, UCP and AP2 are the three in play, MCP is the transport.
- *Merchant of record / seller of record*: the party that legally sells, collects tax and owns the order; every program above says the retailer keeps that role.
- *Mandate (AP2)*: a signed record of what the user authorised (intent, then exact cart), kept as evidence if a dispute arises.
- *Agent profile / trust tier*: the agent's published identity, which the merchant platform uses to decide what the agent may do (browse only, or complete checkout).

**Architecture implications (Part 3).** [ASSUMPTION/JUDGEMENT] Two shapes exist as of November 2026: **discovery with hand-off** (the agent shows the product, the shopper pays on the merchant's checkout; ChatGPT after March 2026, Shopify's redirect mode, Zalando Extended today) and **in-channel checkout** (Google AI Mode/Gemini, Copilot, Meta, Perplexity Instant Buy, Shop Pay in agents; US-centred). The first needs only a feed and a stable product URL; the second needs cart, checkout, order and payment-token APIs plus agent identity. Because the flagship in-channel program was pulled back within six months and three protocols compete, the low-regret design is an **adapter per channel over one internal commerce API** (catalog, availability, cart, order), so a protocol change is a mapping change. Starting: do nothing beyond a correct feed. Growing: feeds through the platform's agentic channel; no custom protocol work. Omnichannel: an agent gateway (one entry point implementing UCP or ACP over the OMS and PIM, with agent authentication), still fed by the same availability and delivery-promise services as the storefront. Group: one gateway per brand on a shared implementation, with per-brand feeds and policies.

---

## PART 4: Europe

### 4.1 PSD2 strong customer authentication and agent-initiated payments

- The RTS on SCA require authentication "based on two or more elements which are categorised as knowledge, possession and inherence" producing an authentication code accepted only once (Art. 4), and **dynamic linking**: "the payer is made aware of the amount of the payment transaction and of the payee", the code "is specific to the amount of the payment transaction and the payee agreed to by the payer", and "any change to the amount or the payee results in the invalidation of the authentication code" (Art. 5) [VERIFIED: Commission Delegated Regulation (EU) 2018/389, https://publications.europa.eu/resource/celex/32018R0389, published 2018-03-13].
- Exemptions that an agent design could lean on: **trusted beneficiaries** (SCA when the payer creates or amends the list; may be skipped for payments to listed payees, Art. 13); **recurring transactions** of the same amount to the same payee (SCA on the first, may be skipped on subsequent ones, Art. 14); **low-value remote transactions** (≤ EUR 30, with cumulative EUR 100 or five transactions since the last SCA, Art. 16); **transaction risk analysis** below fraud-rate reference values and exemption thresholds (Art. 18); and dedicated corporate processes for non-consumers (Art. 17) [VERIFIED: same]. [ASSUMPTION/JUDGEMENT] None of these was written for a delegated purchase whose amount is unknown at the time of delegation; "buy when the price drops below EUR 80" fits neither a fixed recurring amount nor a known cart at authentication time, which is why the European pilots authenticate at the moment of purchase.
- A law-firm note (6 March 2026) says agent-based models "remain subject to PSD2 and the RTS requirements concerning Strong Customer Authentication", that there is "no special 'extra-regulatory' regime", that what constitutes valid authorisation and who is "in fact providing a payment service" are open questions, and that regulators are expected to "issue guidance and recommendations expressly addressing agentic payments" [VERIFIED: https://www.osborneclarke.com/insights/agentic-payments-new-challenge-europes-payments-ecosystem, published 2026-03-06].
- **PSD3/PSR status**: political agreement on 27 November 2025; final compromise texts published by the Council on 23 April 2026; formal adoption by Parliament and Council still required before Official Journal publication; nothing in the sources read addresses agent-initiated payments [VERIFIED: https://www.williamfry.com/knowledge/psd3-psr-final-compromise-texts-are-published/, published 2026-04-28] ⚠.

### 4.2 The European pilots (June–July 2026)

- 2 June 2026 (Money20/20 Europe): Worldline and ING, with Mastercard, completed what they call "Europe's first end-to-end agentic payment transaction in production": an ING cardholder used a merchant AI agent that proposed concert tickets within a budget; "the payment completed only after the consumer explicitly approved it"; merchant in the Netherlands; the same infrastructure operates in Belgium; the transaction carried identifiers marking it as agentic; the release calls it a "pilot" and announces no rollout [VERIFIED: https://worldline.com/en/home/top-navigation/media-relations/press-release/pr-2026_06_02_01, published 2026-06-02] ⚠.
- Visa's 2 July 2026 European program (Part 3.5) authenticated every transaction with passkeys to satisfy SCA, with 31 issuers and four merchants, and no volumes [VERIFIED: Visa UK, 2026-07-02].
- [ASSUMPTION/JUDGEMENT] Both pilots are human-present at payment (passkey or explicit approval bound to the cart), which satisfies dynamic linking by construction. Unattended delegated purchases in the EU remain unproven in public evidence as of November 2026.

### 4.3 EU availability of agent checkout (buyer markets)

| Program | EU buyers as of November 2026 | Source |
| --- | --- | --- |
| ChatGPT via Shopify | No in-chat checkout anywhere; discovery requires selling to US customers | Shopify Help (3.3) |
| Google AI Mode / Gemini (UCP) | Direct checkout US, Canada, Australia only; UK "later"; Europe not mentioned in May or September 2026 posts | Google (3.2), Shopify Help (3.3) |
| Microsoft Copilot, Meta Muse (Shopify direct checkout) | No buyer markets published; US-centred launches | Shopify Help (3.3) |
| Perplexity Instant Buy (PayPal) | US users | PayPal (3.4) |
| Adyen Agentic | US enterprise merchants, limited availability | Adyen (3.6) |
| Amazon Alexa for Shopping / Buy for Me | US customers | Part 2.2 |
| Klarna Agentic Product Protocol | 12 markets claimed (discovery feed, not checkout) | Klarna (3.6) |
| Mastercard Agent Pay | All EU issuers "enabled at a network level"; controlled live transactions; no consumer product named | Mastercard (3.5) |
| Visa Intelligent Commerce | Live pilot purchases with 31 EU issuers and 4 merchants | Visa (3.5) |
| Worldline/ING | One production pilot transaction (NL), infrastructure in BE | Worldline (4.2) |
| Zalando Extended | Discovery of partner products in the Zalando app now; agent checkout planned 2027 | Zalando (2.6) |

[ASSUMPTION/JUDGEMENT] For a Dutch, Belgian or German merchant in November 2026 there is no live consumer channel in which an AI agent completes checkout; the realistic 2026–2027 work is feed quality, discovery presence and payment-side readiness through the PSP and card networks.

### 4.4 The AI Act

- Regulation (EU) 2024/1689 applies generally from 2 August 2026; Chapters I–II (prohibitions) from 2 February 2025; GPAI and governance chapters from 2 August 2025 [VERIFIED: https://publications.europa.eu/resource/celex/32024R1689, Art. 113, published 2024-07-12]. **Article 50(1)**: providers must ensure AI systems "intended to interact directly with natural persons" inform those persons "that they are interacting with an AI system, unless this is obvious"; **Article 50(2)**: generated synthetic content must be "marked in a machine-readable format and detectable as artificially generated" [VERIFIED: same].
- The **Digital Omnibus on AI**, Regulation (EU) 2026/1744 of 8 July 2026 (OJ 24 July 2026), moved the high-risk obligations to "2 December 2027 as regards AI systems classified as high-risk pursuant to Article 6(2) and Annex III" and "2 August 2028" for Annex I systems, and applies new Article 5 prohibitions (points (ba), (bb), (1a), (1b)) from 2 December 2026 [VERIFIED: https://publications.europa.eu/resource/celex/32026R1744, published 2026-07-24] ⚠.
- [ASSUMPTION/JUDGEMENT] For a commerce platform, Art. 50 is the live obligation: a shopping assistant or service bot must say it is AI, and generated product images or text fall under machine-readable marking. Recommendation and search ranking are not Annex III categories; worker-facing warehouse AI (task allocation, performance monitoring) is, from December 2027.

### 4.5 Consumer law: who is the contracting party?

- A CERRE issue paper (16 July 2026, Christoph Busch) argues that EU consumer law "implicitly assumes" a human makes the purchase decision; that disclosure rules were designed around human attention and become "structurally impossible" when agents transact through APIs; that EU law requires consumers to explicitly acknowledge a payment obligation and it is unresolved whether an agent may do so; that the validity of agent-concluded contracts and the split of liability among consumer, agent provider and trader are unclear; and it recommends embedding information duties, consent and redress into the protocols and acting through the Digital Fairness Act expected in Q3 2026 [VERIFIED: https://cerre.eu/publications/agentic-ai-and-consumer-protection/, published 2026-07-16] ⚠.
- [ASSUMPTION/JUDGEMENT] Every protocol and program read for this brief keeps the merchant as seller of record and treats the agent as the consumer's instrument, which matches the "agent of the user" position Perplexity argued and Amazon disputed in a US court (Part 3.7). No EU court or regulator statement on the point was found. Writers should present "the consumer contracts with the merchant through the agent" as the industry's working assumption, not settled law.

**For newcomers (Part 4).**
- *SCA (strong customer authentication)*: the PSD2 rule that a remote payment needs two of knowledge, possession and inherence, bound to the amount and payee.
- *Dynamic linking*: the authentication code is tied to one amount and one payee; change either and it is void.
- *Passkey*: a device-bound cryptographic credential (usually unlocked by biometrics) that counts as possession plus inherence.
- *Seller of record*: the party legally selling to the consumer, responsible for VAT, withdrawal rights and warranty.

**Architecture implications (Part 4).** [ASSUMPTION/JUDGEMENT] An EU agent checkout will, for now, end in a human authentication step owned by the PSP or issuer (passkey, app approval), so the merchant's job is to make the cart the agent built identical to the cart the consumer authenticates: price, delivery promise and tax must be final before the mandate is signed. That is the same "no price drift between cart and payment" discipline the book's checkout chapter already requires. Keep an "agentic" marker on orders (the Worldline pilot carries identifiers) so service, fraud review and consumer-law disclosures can be handled per channel. Starting/Growing: rely on the PSP. Omnichannel: an order attribute for agent channel and a disclosure text for assistants (Art. 50). Group: one policy per market, because PSD3/PSR and the Digital Fairness Act may diverge in timing.

---

## PART 5: What a merchant must have before an agent can buy, and what to leave unbuilt

### 5.1 Structured product data

- **schema.org `Product`** (v30.1, 2026-09-16): `offers`, `gtin` (8/12/13/14 digits or a GS1 Digital Link), `sku`, `brand`, `aggregateRating`, with `Offer` carrying `price`, `priceCurrency` and `availability` such as `https://schema.org/InStock` [VERIFIED: https://schema.org/Product, published 2026-09-16].
- **Google Merchant Center product data specification**: `id`, `title`, `description`, `link`, `image_link`, `availability` (in_stock, out_of_stock, preorder, backorder), `price` required; `brand` required for new products in most categories; `gtin` "strongly recommended if available"; "if your products' prices and availability change often, you'll need to let us know"; attributes can update from on-site structured data [VERIFIED: https://support.google.com/merchants/answer/7052112, n.d., accessed 2026-11].
- **OpenAI/ACP product feed**: nine required fields (`item_id`, `title`, `description`, `url`, `brand`, `seller_name`, `image_url`, `availability`, `price`); `availability` values in_stock, out_of_stock, pre_order, backorder, unknown; shipping and returns optional (`shipping_price`, `accepts_returns`, `return_deadline_in_days`, `return_policy`); GTIN optional with check-digit validation; "update the feed when a sale starts or ends" and when stock changes; the standard upload "currently targets the US" [VERIFIED: https://developers.openai.com/commerce/specs/feed, n.d., accessed 2026-11] ⚠.
- **Shopify Catalog**: requires products eligible for Shopify Catalog; price and availability are cached by agents for at most 15 minutes; some fields are AI-inferred and labelled [VERIFIED: https://shopify.dev/docs/agents/catalog, n.d., accessed 2026-11]. Google says merchants adopting feed best practices see on average a 5% conversion increase the following month [VERIFIED: Google, 2026-09-16] ⚠ (vendor figure).
- [ASSUMPTION/JUDGEMENT] The three feed shapes overlap almost completely (identifier, title, description, URL, image, brand, price, availability, GTIN, shipping, returns). A merchant that already produces a correct Google Merchant feed from its PIM and availability service is most of the way to every agent channel; the new requirement is freshness (minutes, not nightly) for price and availability.

### 5.2 Availability and delivery promise

- Google's direct checkout does not support local delivery, store pickup or pickup points; subscriptions, bundles and customisable products are excluded [VERIFIED: Shopify Help, Google channel, n.d.]. Adyen's Agentic Feed is defined as "catalog, pricing, and availability data", and its Agentic Cart connects "checkout, tax, fulfillment, and order management" [VERIFIED: Adyen, 2026-06-16]. Zalando credits AI supply-chain models with a 22-point gain in delivery-promise accuracy [WIDELY REPORTED: Retail Gazette, 2026].
- [ASSUMPTION/JUDGEMENT] An agent cannot negotiate; it reads availability and a delivery promise and either shows the product or does not. The services the book's inventory and fulfilment chapters define (ATP per location, cut-off-aware delivery promise) are prerequisites, and an agent channel is the harshest consumer of them because stale data becomes a broken promise made by a third party in the merchant's name.

### 5.3 Order status and post-purchase APIs

- Shopify's agent surface includes Order MCP (`get_order`) and order webhooks for fulfilment, returns, refunds and edits [VERIFIED: https://shopify.dev/docs/agents, n.d.]; UCP's core capabilities include Order and Identity Linking [VERIFIED: https://github.com/Universal-Commerce-Protocol/ucp, n.d.]; ACP's 2026-04-17 release added orders [VERIFIED: ACP repository, n.d.]. [ASSUMPTION/JUDGEMENT] Order status, shipment events, return eligibility and refund state must be queryable per order with customer-scoped authentication; these are the same APIs a service bot (Part 1.3) needs. Merchants whose order truth is split across platform, OMS and ERP (the book's "three-status order") cannot answer an agent consistently.

### 5.4 Agent identity and bot authentication

- Cloudflare proposed **Web Bot Auth** on 15 May 2025: agents sign requests with HTTP Message Signatures (RFC 9421), a `Signature-Agent` header "indicates where the origin can find the public keys", with a validity window and the tag `web-bot-auth`; "user agent headers alone are easily spoofed", and IP-range validation is "brittle" [VERIFIED: https://blog.cloudflare.com/web-bot-auth, published 2025-05-15]. On 1 July 2025 Cloudflare added message signatures to its Verified Bots program (JWKS at `/.well-known/http-message-signature-directory`, Ed25519 verification, replay protection via `expires`) [VERIFIED: https://blog.cloudflare.com/verified-bots-with-cryptography, published 2025-07-01].
- The IETF **Web Bot Auth working group** has `draft-ietf-webbotauth-httpsig-protocol-01` ("HTTP Message Signatures for automated traffic"), dated 29 October 2026, authors from Cloudflare and Google, Standards Track, expiring 2 May 2027; it defines the `Signature-Agent` header, a JWK Set key directory and the well-known URI [VERIFIED: https://datatracker.ietf.org/doc/html/draft-ietf-webbotauth-httpsig-protocol, published 2026-10-29] ⚠ (Internet-Draft, "work in progress").
- Cloudflare alleged on 4 August 2025 that Perplexity used undeclared crawlers imitating Chrome on macOS, rotated IPs outside its published ranges and ignored robots.txt, removed Perplexity from its verified-bots list, and set out what a well-behaved agent does: identify itself (unique user agent, published IPs or Web Bot Auth, contact), serve a documented purpose, respect robots.txt and rate limits, and avoid stealth [VERIFIED: https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/, published 2025-08-04].
- Visa's Trusted Agent Protocol and Mastercard Agent Pay build on Web Bot Auth (Part 3.5); Shopify's agent profiles at a well-known URL with signed requests to Checkout MCP are the platform-level equivalent (Part 3.3); Amazon's Agent Terms require agents to identify themselves (Part 3.7).
- [ASSUMPTION/JUDGEMENT] Three identity layers are converging on one mechanism (signed HTTP requests with a published key directory): the CDN/WAF layer (Cloudflare), the payment network (TAP, Agent Pay) and the commerce platform (agent profiles). A merchant on a hosted platform inherits this; a merchant running its own storefront behind a CDN should expect to configure "verified agent" policies in the WAF rather than build verification.

### 5.5 What to leave unbuilt (practitioner sources, tagged judgement)

- Shopify's president (3 March 2026) argued that "the integrity of transactions" (checkout, subscriptions, inventory, shipping, taxes, merchandising) is the moat, in the week OpenAI pulled back from owning the checkout [VERIFIED: Digital Commerce 360, 2026-03-06]. OpenAI's own explanation for the retreat cited transaction complexity such as in-store stock, sales tax and pricing [VERIFIED: same]. Adyen's framing: "Every new agentic surface asks merchants to rebuild from scratch", hence a feed/cart/payments layer that connects to existing systems [VERIFIED: Adyen, 2026-06-16]. commercetools, Shopware and Adobe all sell "agent readiness without replatforming" [VERIFIED: Parts 2.4–2.5].
- [ASSUMPTION/JUDGEMENT] The practitioner consensus, read across these sources, is: do not build your own consumer-facing shopping agent (the assistants belong to Amazon, Google, OpenAI, Meta, Perplexity, Zalando); do not implement three protocols natively in the storefront; do not build agent authentication from scratch; do not let an agent write stock or prices. Do build: a correct, fresh feed; an availability and delivery-promise service; order-status and returns APIs; one internal commerce API that channel adapters (platform-provided where possible) map onto. Revisit in mid-2027 when UCP's governance, PSD3/PSR and the EU channel availability are clearer.

**For newcomers (Part 5).**
- *Product feed*: a machine-readable export of the catalog (identifier, title, price, availability, image, shipping, returns) consumed by marketplaces, ad platforms and now agents.
- *Delivery promise*: the date or window the merchant commits to at the moment of purchase, computed from stock location, cut-off times and carrier service.
- *Web Bot Auth*: a draft standard for an automated client to sign its HTTP requests so a site can verify who it is, instead of trusting the User-Agent string.

**Architecture implications (Part 5).** [ASSUMPTION/JUDGEMENT] "Agent readiness" is a data-quality and API program, not an AI program. Starting: one correct feed from the platform. Growing: feeds driven from the PIM/platform with price and stock refreshed in minutes, policies (returns, shipping) in structured form. Omnichannel: an availability service and an order-status API shared by storefront, service bot and agent channels, plus WAF policies for verified agents. Group: shared feed and agent-gateway infrastructure with per-brand catalogs, identities and markets.

---

## PART 6: Status table (as of 7 November 2026)

| Protocol / program | Owner / governance | Launch | Status (Nov 2026) | Buyer markets | ⚠ |
| --- | --- | --- | --- | --- | --- |
| Instant Checkout (ChatGPT) | OpenAI with Stripe | 29 Sep 2025 (US, Etsy) | Pulled back Mar 2026; "moving to Apps"; discovery with hand-off | US | ⚠ |
| Agentic Commerce Protocol (ACP) | OpenAI + Stripe, "Founding Maintainers"; Apache 2.0 | 29 Sep 2025 | **Beta**; latest spec 2026-04-17 (cart, feed, orders, auth, MCP) | Feeds "currently target the US" | ⚠ |
| Agent Payments Protocol (AP2) | Google with 60+ orgs; Apache 2.0 repo | 16 Sep 2025 | Spec + samples; SDK not on PyPI; used inside UCP | n/a (payment layer) | ⚠ |
| Universal Commerce Protocol (UCP) | Councils; Governance Council = Google, Shopify, Stripe (+2 open seats); Apache 2.0, "UCP Authors" | 11 Jan 2026 | Shopping "latest" (no version tags); lodging draft; food coming; Google claims "hundreds of thousands" of merchants enabled | Checkout US; CA/AU "early next year"; UK later; EU not mentioned | ⚠ |
| Shopify Agentic Storefronts | Shopify | 10 Dec 2025 (all merchants); channels Jan–Mar 2026 | Live; ChatGPT discovery-only; direct checkout in Google/Copilot/Meta | ChatGPT: must sell to US; Google: US, CA, AU | ⚠ |
| Shopify Storefront MCP → UCP MCP | Shopify | May 2025 → 2026 | Catalog/cart MCP removed; UCP at `/api/ucp/mcp`; Checkout MCP needs signed requests | n/a | ⚠ |
| Perplexity Instant Buy | Perplexity + PayPal | 25 Nov 2025 | Live (US) | US | ⚠ |
| Visa Intelligent Commerce / TAP | Visa (TAP with Cloudflare) | 30 Apr 2025 / 14 Oct 2025 | Live pilots EU (31 issuers, 4 merchants, Jul 2026); B2B pilot Oct 2026 | Pilot | ⚠ |
| Mastercard Agent Pay | Mastercard | 29 Apr 2025 | All EU issuers "enabled at a network level"; controlled live transactions (36 banks) | Pilot | ⚠ |
| Worldline/ING/Mastercard | Worldline, ING | 2 Jun 2026 | One production pilot transaction (NL; infra in BE) | Pilot | ⚠ |
| Klarna Agentic Product Protocol | Klarna | 15 Dec 2025 | Hosted API live; discovery only; no named adopters | 12 markets (claimed) | ⚠ |
| Adyen Agentic | Adyen | 16 Jun 2026 | Limited availability | US enterprise merchants | ⚠ |
| Amazon Alexa for Shopping (ex-Rufus), Auto-Buy, Scheduled Actions | Amazon | 13 May 2026 | Live | US | ⚠ |
| Amazon Buy for Me | Amazon | 10 Apr 2025 (test) | Live for eligible brands; in Alexa for Shopping | US | ⚠ |
| Salesforce Agentforce Commerce agents | Salesforce | 6 Jul 2026 | GA (Shopper, Buyer, Merchant agents); Google/Gemini "coming months" | Not stated | ⚠ |
| Shopware Copilot + MCP | Shopware | 10 Jun 2026; MCP from 6.7.11.0 | Copilot agentic on demand; MCP experimental until 6.8 | n/a | ⚠ |
| commercetools AgenticLift | commercetools | 21 Jan 2026 | Launched; MCP + ACP; regions not stated | Not stated | ⚠ |
| Adobe Commerce UCP/ACP | Adobe | Feb 2026 commitment | "Moving towards supporting"; not shipped | n/a | ⚠ |
| Mollie MCP server | Mollie | 29 Jul 2025 | Live (merchant-side actions) | n/a | ⚠ |
| Zalando Extended | Zalando | 3 Nov 2026 | Partner products in app (Westwing pilot); agent checkout planned 2027 | Zalando markets | ⚠ |
| Web Bot Auth | IETF WG (Cloudflare, Google authors) | May 2025 proposal; WG draft -01 29 Oct 2026 | Internet-Draft, Standards Track; deployed by Cloudflare, Visa TAP, Mastercard | n/a | ⚠ |
| Amazon v. Perplexity | N.D. Cal. / Ninth Circuit | Nov 2025 | Injunction vacated Aug 2026; amended complaint; motion to dismiss pending | US | ⚠ |

---

## Key numbers

| Number | Meaning | Source | Date |
| --- | --- | --- | --- |
| 2.3 million chats, "two-thirds", 700 FTE, USD 40m | Klarna AI assistant first-month claims | Klarna press | 2024-02-27 |
| 22% headcount fall to 3,500; "lower quality" | Klarna's reversal | Entrepreneur (Bloomberg) | 2025-05-09 |
| 100,000+ sellers; ~80% attribute acceptance | Amazon generative listing tools | aboutamazon | n.d. (2024/25) |
| 6 million → 22 million+ unique users | Zalando Assistant, 2025 results → "this year" (Q3 2026) | Retail Gazette; Zalando Q3 | 2026-03-12; 2026-11-03 |
| 90%; +22 pp | Zalando: AI share of marketing content; delivery-promise accuracy gain | Retail Gazette | 2026-03-12 |
| 693% YoY; +31% conversion; >1 trillion visits | Adobe AI-referred retail traffic, holiday 2025 (US) | Digital Commerce 360 (Adobe) | 2026-01-13 |
| 20% / USD 262bn | Salesforce "AI-influenced" holiday 2025 sales | Salesforce | 2026-07-06 |
| 250m+ (page) / 300m (2025) customers; +115% MAU | Amazon Rufus usage claims | aboutamazon; AI News (GeekWire) | n.d.; 2026-05-18 |
| 13 May 2026 | Rufus renamed Alexa for Shopping | aboutamazon | n.d. |
| 5 spec releases, latest 2026-04-17 | ACP | GitHub | n.d. |
| 60+ organisations | AP2 partners | Google Cloud | 2025-09-16 |
| 20+ endorsers; 5 co-developers; "hundreds of thousands" enabled | UCP | Google | 2026-01-11; 2026-09-16 |
| 3 Governance Council seats (Google, Shopify, Stripe) | UCP governance | GitHub MAINTAINERS | n.d. |
| 1.9% + €0.25 | Shopify Agentic plan card rate, no monthly fee | Shopify | n.d. |
| 15 minutes / 24 hours | Shopify Catalog cache limits (price, availability / metadata) | shopify.dev | n.d. |
| 4.2x | Sidekick daily sessions YoY | Shopify Fall '26 | n.d. |
| 31 issuers, 4 merchants | Visa live EU agent transactions | Visa UK | 2026-07-02 |
| 36 banks; "all" EU issuers enabled | Mastercard Agent Pay Europe | Mastercard | 2026-06-02 |
| 100m+ products, 400m prices, 12 markets | Klarna APP claims | Klarna IR | 2025-12-15 |
| 32% | Stripe Radar claimed fraud reduction | Stripe | n.d. |
| 13% | Constructor's Petco conversion lift claim | Constructor | n.d. |
| EUR 30 / EUR 100 / 5 | SCA low-value exemption thresholds | RTS 2018/389 Art. 16 | 2018-03-13 |
| 2 Aug 2026; 2 Dec 2027; 2 Aug 2028; 2 Dec 2026 | AI Act general application; Annex III; Annex I; new prohibitions | 2024/1689 Art. 113; 2026/1744 | 2024; 2026-07-24 |
| 6.7.11.0 / 6.8 | Shopware MCP introduced / experimental until | Shopware docs | n.d. |

## Open questions / not verifiable

1. **Volumes.** No party has published transactions, GMV or conversion for Instant Checkout, UCP checkout, Perplexity Instant Buy, Shopify agentic channels, Buy for Me or Auto-Buy. Google's "hundreds of thousands" counts enabled merchants, not transacting ones.
2. **Why Instant Checkout was pulled back.** Only The Information's reporting (not read) and an OpenAI spokesperson's general statement exist; the "transaction complexity" explanation is a trade-press inference.
3. **UCP governance rules.** GOVERNANCE.md was not read; whether seats are elected, how specs are versioned, and whether a foundation is planned are unknown.
4. **Amazon's Agent Terms.** The Conditions of Use could not be fetched; the May 2025 date and content come from legal press.
5. **Rufus/Alexa for Shopping figures.** The period behind "250 million this year" and "+149%" on Amazon's page is unclear and differs from the "+115%" earnings-call figure reported by press.
6. **Sidekick GA date**; **Shopify Agentic plan country eligibility**; **Copilot and Meta buyer markets**.
7. **EU consumer-law position.** No regulator or court statement on who contracts when an agent buys; CERRE's paper is academic commentary.
8. **PSD3/PSR text on agent payments.** Compromise texts (23 April 2026) were not read.
9. **Zalando Assistant conversion** ("twice as likely") is secondary; Zalando's primary release gives users only.
10. **Independent measurements** of AI search, recommendation and content results in commerce: none found; every lift in this brief is a vendor figure.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| The history of Amazon's recommendation algorithm | Amazon Science (L. Hardesty) | 2019 | https://www.amazon.science/the-history-of-amazons-recommendation-algorithm |
| Zalando to launch a fashion assistant powered by ChatGPT | Zalando corporate | 2023 | https://corporate.zalando.com/en/node/10422 |
| Zalando reports strong 2025 growth as AI strategy drives performance | Retail Gazette | 2026 | https://www.retailgazette.co.uk/blog/2026/03/zalando-reports-strong-2025-growth-as-ai-strategy-drives-performance/ |
| Zalando Q3 2026 results | Zalando corporate | 2026 | https://corporate.zalando.com/en/financials/zalando-q3-2026-results |
| Zalando launches first AI shopping agent as margins slip in Q3 2026 | Analytics Insight | 2026 | https://www.analyticsinsight.net/news/zalando-launches-first-ai-shopping-agent-as-margins-slip-in-q3-2026 |
| AI Search (NeuralSearch) | Algolia | n.d. | https://www.algolia.com/products/ai-search/ |
| Constructor home page | Constructor | n.d. | https://constructor.com/ |
| Amazon generative AI-powered product listings | Amazon (aboutamazon) | n.d. | https://www.aboutamazon.com/news/innovation-at-amazon/amazon-generative-ai-powered-product-listings |
| Shopify Editions Summer '23 | Shopify | 2023 | https://www.shopify.com/editions/summer2023 |
| Shopify Magic / AI features (help) | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic |
| Klarna AI assistant handles two-thirds of customer service chats | Klarna | 2024 | https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ |
| Klarna is hiring customer service agents after AI couldn't cut it | Entrepreneur (S. Shibu) | 2025 | https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 |
| Stripe Radar | Stripe | n.d. | https://stripe.com/radar |
| DeepAR: Probabilistic Forecasting with Autoregressive Recurrent Networks | Salinas, Flunkert, Gasthaus (arXiv) | 2017 | https://arxiv.org/abs/1704.04110 |
| Deep Learning based Forecasting: a case study from the online fashion industry | Kunz et al. (arXiv) | 2023 | https://arxiv.org/abs/2305.14406 |
| Generative AI online holiday shopping traffic 2025 (Adobe data) | Digital Commerce 360 (A. Haleem) | 2026 | https://www.digitalcommerce360.com/2026/01/13/generative-ai-online-holiday-shopping-traffic-2025/ |
| Salesforce unleashes its biggest Agentforce Commerce release yet | Salesforce | 2026 | https://www.salesforce.com/ap/news/press-releases/2026/07/06/as-ai-agents-transform-commerce-salesforce-unleashes-its-biggest-agentforce-commerce-release-yet/ |
| Expanding your AI horizons, Summer '25 Edition | Shopify blog | 2025 | https://www.shopify.com/blog/expanding-your-ai-horizons-summer-edition-25 |
| Sidekick (help) | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick |
| Winter '26 Edition: Renaissance | Shopify News | 2025 | https://www.shopify.com/news/winter-26-edition-renaissance |
| Shopify Editions Fall '26 | Shopify | 2026 | https://www.shopify.com/editions/fall2026 |
| Amazon Rufus AI assistant personalized shopping features | Amazon (aboutamazon) | n.d. | https://www.aboutamazon.com/news/retail/amazon-rufus-ai-assistant-personalized-shopping-features |
| Amazon retires Rufus and launches Alexa for Shopping | EcomCrew | 2026 | https://www.ecomcrew.com/amazon-retires-rufus-and-launches-alexa-for-shopping-as-its-unified-ai-assistant/ |
| Amazon Alexa for Shopping replaces Rufus | AI News (M. Zulhusni) | 2026 | https://www.artificialintelligence-news.com/news/amazon-alexa-for-shopping-rufus-ai-assistant/ |
| Amazon's "Buy for Me" agentic AI buys from third-party sites | Retail Dive | 2025 | https://www.retaildive.com/news/amazon-buy-for-me-agentic-ai-thirdparty-sites/745047/ |
| Shopware Community Day 2026 press release | Shopware | 2026 | https://www.shopware.com/en/press/press-releases/shopware-community-day-2026-shopware-becomes-the-open-commerce-infrastructure-for-the-agentic-era/ |
| MCP Server; Store API MCP | Shopware developer docs | n.d. | https://developer.shopware.com/docs/products/tools/mcp-server.md ; https://developer.shopware.com/docs/products/tools/mcp-server/store-api.md |
| commercetools launches AgenticLift | commercetools | 2026 | https://commercetools.com/press-releases/commercetools-launches-agenticlift |
| Adobe Commerce commits to agentic commerce standards | Glenbrook Payments News (relay) | 2026 | https://glenbrook.com/payments_news/adobe-commerce-commits-to-agentic-commerce-standards/ |
| Adobe commits commerce platform to agentic standards | Digital Commerce 360 (M. Brohan) | 2026 | https://www.digitalcommerce360.com/2026/02/23/adobe-commerce-platform-agentic-ai-standards/ |
| Stripe and OpenAI launch Instant Checkout | Stripe newsroom | 2025 | https://stripe.com/newsroom/news/stripe-openai-instant-checkout |
| Agentic Commerce Protocol repository | OpenAI and Stripe (GitHub) | 2025–2026 | https://github.com/agentic-commerce-protocol/agentic-commerce-protocol |
| Commerce; Product Feed Spec | OpenAI developers | n.d. | https://developers.openai.com/commerce ; https://developers.openai.com/commerce/specs/feed |
| OpenAI shifts checkout plans, agentic commerce strategy | Digital Commerce 360 (B. Warmoth) | 2026 | https://digitalcommerce360.com/2026/03/06/openai-shifts-checkout-plans-agentic-commerce-strategy/ |
| Shopify says purchases are coming inside ChatGPT as OpenAI retreats on Instant Checkout | Modern Retail (A. Smith) | 2026 | https://www.modernretail.co/technology/shopify-says-purchases-are-coming-inside-chatgpt-through-agentic-storefronts-as-openai-retreats-on-instant-checkout/ |
| Announcing Agent Payments Protocol (AP2) | Google Cloud blog | 2025 | https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol |
| AP2 repository | Google (GitHub) | 2025–2026 | https://github.com/google-agentic-commerce/AP2 |
| Agentic commerce: new AI tools and a protocol for retailers and platforms (UCP) | Google (The Keyword) | 2026 | https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/ |
| ucp.dev | UCP Authors | 2026 | https://ucp.dev/ |
| UCP repository; MAINTAINERS | Universal-Commerce-Protocol (GitHub) | 2026 | https://github.com/Universal-Commerce-Protocol/ucp ; https://github.com/Universal-Commerce-Protocol/.github/blob/main/MAINTAINERS.md |
| Shopping updates at Google Marketing Live (Universal Cart) | Google | 2026 | https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/ |
| Google Shopping updates for holiday shopping (UCP) | Google | 2026 | https://blog.google/products-and-platforms/products/shopping/google-shopping-updates-holiday-shopping/ |
| The agentic commerce platform (UCP, Agentic Storefronts, Agentic plan) | Shopify News | 2026 | https://www.shopify.com/news/ai-commerce-at-scale |
| Agentic storefronts; ChatGPT; Google AI Mode and Gemini (help) | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts ; …/chatgpt ; …/google |
| Agentic plan | Shopify | n.d. | https://www.shopify.com/agentic-plan |
| Storefront MCP; Agents; Catalog | shopify.dev | n.d. | https://shopify.dev/docs/apps/build/storefront-mcp ; https://shopify.dev/docs/agents ; https://shopify.dev/docs/agents/catalog |
| Perplexity selects PayPal to power agentic commerce | PayPal newsroom | 2025 | https://newsroom.paypal-corp.com/2025-05-14-Perplexity-Selects-PayPal-to-Power-Agentic-Commerce |
| PayPal and Perplexity launch Instant Buy | PayPal newsroom | 2025 | https://newsroom.paypal-corp.com/2025-11-PayPal-and-Perplexity-Launch-Instant-Buy |
| Find and buy with AI: Visa unveils new era of commerce (release copy) | Visa via Silicon UK | 2025 | https://www.silicon.co.uk/press-release/find-and-buy-with-ai-visa-unveils-new-era-of-commerce |
| Cloudflare collaborates with leading payments companies (TAP, Web Bot Auth) | Cloudflare press | 2025 | https://www.cloudflare.com/press/press-releases/2025/cloudflare-collaborates-with-leading-payments-companies-to-secure-and-enable-agentic-commerce/ |
| Visa: live agentic transactions in Europe | Visa UK newsroom | 2026 | https://www.visa.co.uk/about-visa/newsroom/press-releases.3457328.html |
| Visa, BILL and Billtrust B2B agentic pilot | Visa newsroom | 2026 | https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.22856.html |
| Mastercard unveils Agent Pay | Mastercard newsroom | 2025 | https://newsroom.mastercard.com/news/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai |
| Europe is building the foundations for trusted agentic commerce | Mastercard (B. van de Walle) | 2026 | https://newsroom.mastercard.com/news/europe/en/perspectives/en/2026/europe-is-building-the-foundations-for-trusted-agentic-commerce/ |
| Worldline and ING complete Europe's first agentic payment in production | Worldline | 2026 | https://worldline.com/en/home/top-navigation/media-relations/press-release/pr-2026_06_02_01 |
| Klarna launches Agentic Product Protocol | Klarna investor news | 2025 | https://investors.klarna.com/News--Events/news/news-details/2025/Klarna-Launches-Agentic-Product-Protocol-The-Open-Standard-That-Makes-100M-Products-Instantly-Discoverable-by-AI-Agents/default.aspx |
| Adyen Agentic | Adyen press | 2026 | https://www.adyen.com/press-and-media/adyen-agentic |
| Mollie launches AI-ready MCP server | Financial IT | 2025 | https://financialit.net/news/payments/mollie-launches-ai-ready-mcp-server-help-merchants-automate-and-simplify-workflows |
| Amazon and Perplexity are fighting over the future of AI shopping | Engadget (I. C. Campbell) | 2025 | https://www.engadget.com/ai/amazon-and-perplexity-are-fighting-over-the-future-of-ai-shopping-215445479.html |
| Amazon's AI shopping battle puts website terms to the test | The Fashion Law | 2026 | https://www.thefashionlaw.com/?p=109079 |
| Perplexity just won the appeal Amazon's court order was waiting on | EcomCrew | 2026 | https://www.ecomcrew.com/?p=67537 |
| Amazon blocks Meta's Muse AI agent from its retail site | The Star (Bloomberg) | 2026 | https://www.thestar.com.my/tech/tech-news/2026/09/22/amazon-blocks-metas-muse-ai-agent-from-its-retail-site |
| Forget IPs: using cryptography to verify bot and agent traffic | Cloudflare blog | 2025 | https://blog.cloudflare.com/web-bot-auth |
| Message Signatures are now part of our Verified Bots Program | Cloudflare blog | 2025 | https://blog.cloudflare.com/verified-bots-with-cryptography |
| Perplexity is using stealth, undeclared crawlers | Cloudflare blog | 2025 | https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/ |
| HTTP Message Signatures for automated traffic (draft-ietf-webbotauth-httpsig-protocol-01) | IETF Web Bot Auth WG (Meunier, Major) | 2026 | https://datatracker.ietf.org/doc/html/draft-ietf-webbotauth-httpsig-protocol |
| Commission Delegated Regulation (EU) 2018/389 (RTS on SCA) | EU Publications Office | 2018 | https://publications.europa.eu/resource/celex/32018R0389 |
| Regulation (EU) 2024/1689 (AI Act) | EU Publications Office | 2024 | https://publications.europa.eu/resource/celex/32024R1689 |
| Regulation (EU) 2026/1744 (Digital Omnibus on AI) | EU Publications Office | 2026 | https://publications.europa.eu/resource/celex/32026R1744 |
| Agentic payments: a new challenge for Europe's payments ecosystem | Osborne Clarke | 2026 | https://www.osborneclarke.com/insights/agentic-payments-new-challenge-europes-payments-ecosystem |
| PSD3/PSR final compromise texts are published | William Fry | 2026 | https://www.williamfry.com/knowledge/psd3-psr-final-compromise-texts-are-published/ |
| Agentic AI and consumer protection | CERRE (C. Busch) | 2026 | https://cerre.eu/publications/agentic-ai-and-consumer-protection/ |
| schema.org Product | schema.org | 2026 | https://schema.org/Product |
| Product data specification | Google Merchant Center Help | n.d. | https://support.google.com/merchants/answer/7052112 |
