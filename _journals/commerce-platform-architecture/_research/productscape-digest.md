# Productscape Digest — research maps for ORDERED: Architecting Commerce Platforms

**Local-only research digest. Compiled 7 November 2026 from the author's sibling repository (`productscape-workspace/productscape-examples/_config/product-domains/`). Not a source; a map.**

## Read this first — what these models are and are not

- The eleven Productscape models summarized here are **architectural models inferred from public product behavior. They are not descriptions of any company, product or organization.** The model authors decomposed what a product visibly does (pages, pricing matrices, help centers, integration listings) into "bricks" and "modules"; the decomposition, the module layering, the data stores and the deployment surfaces are the modelers' inferences, not any vendor's internal design. The models' own `DOMAIN.md` files say so explicitly ("brick decomposition, module layering, data stores and deployment surfaces are an architectural model inferred from public product behavior").
- **Every KPI value in the models is a modeled seed value** ("illustrative modeling baselines" in the models' own words). None is reproduced here, and none may be quoted in the book as a fact.
- The book uses these models **only as research maps**: the Domain Coverage reference page (`domain-coverage`) maps bricks to chapters so the book can check it has covered the territory. **Never cite a model as a source for a fact about Shopify, Amazon or any Katapull label.** Facts about real companies come only from the verified research briefs (`brief-*.md`, VERIFIED or WIDELY REPORTED) or from a source the chapter writer fetches and dates.
- **Katapull models in particular.** The nine `katapull-group` models were authored against the public pages of nine specialist commerce labels. This digest carries over **only the capability inventory** (which bricks and modules each product domain has, which data entities it keeps, which roles it serves, which business-context stressors its modeler listed). It deliberately **does not** carry over any statement about the group's or a label's internal plans, finances, roadmaps, acquisitions, pricing, package tiers, headcount, locations or "strategy spine" sections, and it strips vendor and partner names from brick descriptions where they are not needed to understand the capability. Stressors about group ownership or consolidation are omitted. The book is platform-neutral; Katapull labels appear in chapters only through public pages verified in the briefs.
- Brick descriptions below are paraphrased into neutral capability language. Brick ids and names are the models' own so the Domain Coverage page can reference them.
- Model short codes used throughout: **MCP** merchant-commerce-platform (Shopify-inspired), **ORM** online-retail-marketplace (Amazon-inspired), **B2B** b2b-wholesale-ecommerce-platform, **RET** ecommerce-returns-management-platform, **EDI** edi-and-b2b-document-exchange-platform, **HUB** katapull-commerce-hub, **MKT** marketplace-channel-integration-platform, **ERP** omnichannel-commerce-erp-platform, **POS** retail-pos-and-store-management-platform, **SHP** shipping-and-carrier-management-platform, **WMS** warehouse-management-and-fulfilment-platform.

### Chapter folders referenced (from `../PLAN.md`)

| Part | Chapter folders |
| --- | --- |
| I COMMERCE | `01-journey-of-an-order`, `02-commerce-business-models`, `03-commerce-capability-map`, `04-boundaries-and-systems-of-record`, `05-commerce-platform-landscape` |
| II CATALOG | `06-product-information`, `07-pricing-architecture`, `08-promotions-and-loyalty`, `09-search-and-discovery`, `10-inventory-and-availability` |
| III ORDER | `11-cart-and-checkout`, `12-payments`, `13-order-management`, `14-tax-invoicing-and-ledger` |
| IV FULFILLMENT | `15-warehouse-and-fulfillment`, `16-shipping-and-delivery`, `17-stores-and-omnichannel`, `18-returns-and-exchanges`, `19-customer-service-and-notifications` |
| V CHANNELS | `20-marketplaces-and-channel-integration`, `21-b2b-commerce`, `22-edi-and-e-invoicing`, `23-erp-and-back-office-integration` |
| VI INTEGRATION | `24-integration-styles`, `25-events-consistency-and-reconciliation`, `26-api-contracts-and-versioning`, `27-identity-and-master-data`, `28-commerce-data-and-analytics` |
| VII PLATFORM | `29-commerce-architecture-styles`, `30-multi-tenancy-and-isolation`, `31-extensibility-and-app-ecosystems`, `32-storefront-architecture`, `33-peak-load-and-reliability` |
| VIII TRUST | `34-commerce-security`, `35-privacy-and-customer-data`, `36-commerce-regulation` |
| IX JOURNEYS | `37-journey-consumer-order`, `38-journey-return-and-exchange`, `39-journey-wholesale-order`, `40-journey-peak-day` |
| X EVOLUTION | `41-build-buy-or-assemble`, `42-replatforming-and-migration`, `43-commerce-scaling-stages`, `44-organizing-commerce-engineering`, `45-ai-and-agentic-commerce` |
| XI PRACTICE | `46-case-shopify`, `47-case-amazon`, `48-case-zalando`, `49-case-composable-movement` |
| Reference | `domain-coverage`, `toolkit`, `glossary`, `bibliography` |

---

## 1. Model-by-model inventory

Each model: root groups (the model's "layers"), then one row per brick with id, name, a one-line capability description, and the module names the model lists under that brick (across its UI / API / async / service / data / adapter layers).

### 1.1 MCP — merchant-commerce-platform (Shopify-inspired)

**Model's own framing:** a platform that lets merchants of every size run branded commerce: storefront, checkout, orders, payments, point of sale, wholesale, marketing, an app ecosystem, and AI assistants as a sales channel. Adjacent systems (payment partners and card networks, carriers, banks and lenders, AI assistant platforms, social and marketplace platforms, ERP and WMS) are modeled as external.

**Root groups:** Storefront and Buyer Experience (Storefronts; Checkout and Buyer Identity) · Commerce Core and Operations (Catalog, Markets and Wholesale; Orders, Fulfillment and Retail) · Money and Merchant Financial Services (Payments and Risk; Financial and Billing Services) · Growth, Channels and AI (Marketing and Insight; AI and Channels) · Platform and Ecosystem (Developer Platform).

| Id | Brick | Capability (one line) | Modules |
| --- | --- | --- | --- |
| stfr | Online Store and Theme Engine | Hosted storefront with themes, editor and content pages, rendered at the edge | Theme Editor; Storefront Renderer; Theme and Content API; Storefront Page BFF; Template Render Orchestrator; Theme and Content Store; Domain and Launch Service; Edge CDN Adapter |
| hdrg | Headless Storefront Framework and Hosting | Developer framework, storefront API and edge hosting for custom frontends | Headless Starter Kit; Storefront GraphQL API; Deployments Console; Build and Deploy Runner; Edge Hosting Runtime; Git Provider Adapter |
| srch | Storefront Search and Discovery | Keyword plus semantic search, filtering, recommendations and merchandising rules | Search and Filter UI; Search and Recommendations API; Catalog Index Consumer; Query Understanding; Search and Vector Index; Merchandising Rules |
| chkt | Checkout and Checkout Extensibility | Hosted one-page checkout turning carts into paid orders, with upgrade-safe UI extensions and server functions | One-Page Checkout; Cart and Checkout API; Checkout Editor; Checkout Completed Queue; Checkout Orchestrator; Cart and Session Store; Discount Engine |
| shpy | Shop Pay Accelerated Checkout and Buyer Identity | Network-wide saved buyer identity and wallet: recognition, prefill, one-time-code verification, installments | Wallet Button and Sheet; In-App Wallet; Buyer Identity API; Recognition Orchestrator; Identity and Vault Store; Installments Offer Service; OTP and Lending Partner Adapter |
| shop | Shop App Consumer Experience | Consumer app aggregating order tracking, brand following, AI search and checkout across merchants | Shopping App Client; Shopping Web Experience; Shopping App BFF; Order Sync Consumer; AI Shopping Assistant; Follow and Feed Service; Order Email Import |
| ctlg | Product Catalog and Merchandising | Products, variants, media, collections, attributes; bulk import; AI-assisted content | Product Editor; Product Admin API; Catalog Change Events; Bulk Import Runner; Product and Variant Store; Collection Rules Service |
| invt | Multi-Location Inventory | Quantities and states per location, transfers, reservations, availability for every channel | Inventory Admin; Inventory API; Reservation Consumer; Inventory Ledger; Transfers and Purchase Orders; Warehouse and 3PL Adapter |
| mkts | Markets and Cross-Border Localization | Per-market currency, pricing, language, domains, duties and payment methods from one store | Markets Admin; Markets API; Market Context Resolver; Market Configuration Store; Currency Conversion; Translation and FX Adapter |
| b2bc | B2B Wholesale Commerce | Company accounts, buyer permissions, catalogs, price lists, quantity rules, payment terms on the same checkout | B2B Buyer Portal; Company Admin; Company and Catalog API; B2B Pricing Orchestrator; Company Account Store; Payment Terms Service |
| ordr | Order Management | Order system of record across channels: edits, payment state, fulfillment orders, refunds, customer records | Orders Admin; Order Admin API; Order Events; Fulfillment Order Routing; Order Store; Merchant Customer Store |
| ship | Shipping Labels and Delivery Promise | Shipping profiles, carrier rates, labels, delivery-date promises, tracking events | Shipping Admin; Shipping Rates API; Tracking Event Consumer; Delivery Promise Calculator; Label and Shipment Store; Carrier Adapter |
| rtrn | Returns and Exchanges | Self-serve returns and exchanges with rules, labels, in-store returns, refunds tied to the order | Return Request Portal; Returns API; Return Rules Engine; Return Store |
| posr | POS and Retail Store Operations | POS app, hardware, staff, cash, local inventory, pickup and in-store returns on the same core | POS App; POS Admin; POS BFF; Offline Sync Agent; Store Checkout Orchestrator; Staff and Cash Drawer Store; Terminal Hardware Adapter |
| paym | Integrated Payments Processing | Merchant onboarding, card/wallet/local methods, authorization, capture, refunds for online, in-person and agent channels | Payments Settings; Payments API; Payment Events; Payment Method Router; Payment Transaction Store; Merchant Onboarding and KYC; Processor and Network Adapter |
| risk | Fraud, Chargeback and Risk Protection | Order and payment fraud analysis, bot protection, chargeback evidence, merchant risk monitoring | Fraud Analysis Panel; Risk Operations Console; Risk Decision API; Dispute Consumer; Scoring Orchestrator; Dispute Case Store; Risk Models |
| ledg | Merchant Balance, Payouts and Ledger | Double-entry ledger of merchant funds, fees, reserves; payout scheduling; merchant money account | Balance and Payouts; Balance and Payouts API; Payout Scheduler; Merchant Ledger; Reserve and Hold Service; Banking Partner Adapter |
| capl | Merchant Capital Lending | Pre-qualified advances and loans sized from sales history, repaid as a share of sales | Capital Offers; Capital API; Offer Generation Job; Loan Book; Underwriting Models; Lending Partner Adapter |
| taxc | Tax and Duties Calculation | Sales tax, VAT, GST and import duty at checkout; liability tracking; filing support | Tax Settings; Tax Calculation API; Tax Calculator; Liability Tracker; Tax Content Adapter |
| blng | Platform Subscription and App Billing | Billing merchants for plans, apps, themes and usage; partner revenue share | Billing Page; App Billing API; Billing Cycle Runner; Plan Subscription Store; Partner Revenue Share |
| mktg | Customer Segmentation and Marketing Automation | Segments, email and messaging campaigns, automations on order and customer data | Campaign Editor; Marketing API; Send Scheduler; Segment Store; Consent and Preferences; Email Delivery Adapter |
| adsn | Shop Campaigns and Audience Ads | Pay-per-conversion ad campaigns and audience lists from network purchase signals | Campaign Manager; Ads Serving API; Auction and Pacing; Campaign Store; Audience Builder; Ad Platform Adapter |
| anly | Commerce Analytics and Reporting | Reports, dashboards and a query layer over sales, sessions, products, customers, finance | Analytics Dashboards; Analytics Query API; Event Ingestion; Analytics Warehouse; Attribution Service |
| sdkk | Sidekick AI Commerce Assistant | Admin assistant answering over store data, generating content, taking approved actions | Assistant Panel; Assistant Actions API; Proactive Insights Job; Agent Orchestrator; Conversation Store; LLM Provider Adapter |
| agnt | Agentic Commerce and Global Catalog | Structured global catalog and open commerce protocol so AI assistants discover, recommend and check out with merchant rules | Agentic Storefronts Admin; Global Catalog Search API; Commerce Protocol Endpoint; Catalog Enrichment Consumer; Global Catalog Index; AI Channel Adapter |
| chnl | Social and Marketplace Channel Sync | Publish products to social and marketplace channels; import their orders into one order system | Channel Admin; Sales Channel API; Listing Sync Consumer; Publication Store; Marketplace and Social Adapter |
| apis | Admin APIs, Webhooks and Identity | Versioned GraphQL admin API, webhooks, OAuth app authorization, staff accounts and permissions | Staff and Organization Admin; Admin GraphQL Gateway; Webhook Delivery; OAuth and Access Scopes; Account and Staff Store; App Grant Store |
| extn | Extensions, Functions and Workflow Automation | UI extensions and sandboxed server functions in checkout, admin and POS; no-code workflow automation | Workflow Builder; Extension Registry API; Workflow Trigger Consumer; Function Runtime; Extension Registry |
| apst | App Store and Partner Program | App and theme marketplace, app review, partner dashboard, development stores, partner tiers | App Store Listing; Partner Dashboard; App Review Console; Partner API; App Ranking; Listing and Review Store; Development Store Provisioning |

**Data stores the model assumes (inference):** sharded shop core database; checkout session key-value store; buyer identity vault; payments and ledger database; card tokenization vault; commerce event stream; analytics warehouse; search and vector index; object storage and media CDN; risk feature store.

### 1.2 ORM — online-retail-marketplace (Amazon-inspired)

**Model's own framing:** a large-scale retail marketplace combining shopper demand, a membership program, third-party seller supply, fulfillment infrastructure, trust controls and retail-media monetization. Internal operator roles (trust and compliance; fulfillment and resolution) are modeled as customers too. The model names the shopping assistant brick after the assistant's current public name while keeping a stable id (`rufu`).

**Root groups:** Shopper Experience (Discovery and evaluation; Conversion and service) · Seller Growth (Commercial control; Operations and demand generation) · Marketplace Foundations (Trust and platform control; Shared intelligence and integration).

| Id | Brick | Capability (one line) | Modules |
| --- | --- | --- | --- |
| home | Shopping Home & Entry | Personalized entry surfaces routing shoppers to categories, replenishment and promotions | Shopping home UI; Home feed composition |
| sear | Search, Browse & Facets | Search, browse, filters, category navigation and ranking | Search UI; Catalog indexing pipeline; Search index and ranking |
| rufu | Alexa for Shopping (assistant) | Conversational, guided shopping assistance that narrows broad intent | Assistant conversation UI; Assistant API; Model serving & grounding; Intent interpretation and grounding |
| pdet | Product Detail Experience | Detail pages, offer presentation, compatibility guidance, comparisons | Detail page UI; Offer and content assembly |
| revi | Reviews, Ratings & Q&A | Ratings, reviews, Q&A and trust feedback loops | Review surfaces; Review moderation and ranking |
| deal | Deals, Promotions & Merchandising | Promotional placements, deal eligibility, badges, merchandising programs | Promotion surfaces; Promotion orchestration |
| cart | Cart & Save-for-Later | Cart state, save-for-later, basket building | Cart UI; Cart state orchestration |
| chec | Checkout & Payments | Checkout, payment authorization, address selection, order placement | Checkout UI; Checkout & order API; Order event publisher; Payment and order placement |
| orde | Order Management & Tracking | Order history, shipment visibility, exception handling, delivery communication | Orders UI; Order event processor; Order state timeline |
| deli | Delivery Promise & Last Mile | Promise calculation, carrier routing, last-mile eventing, shopper-visible commitments | Promise APIs; Promise risk monitor; Promise calculation engine |
| retu | Returns, Refunds & Exchanges | Reverse logistics, refunds, exchanges, policy-aware recovery | Returns UI; Reverse-logistics event processor; Reverse-logistics orchestration |
| prim | Prime Membership & Benefits | Membership sign-up, state, benefit eligibility, retention value | Prime UI; Prime entitlement service |
| sell | Seller Identity & Onboarding | Seller registration, compliance, tax, verification, account health setup | Seller onboarding UI; KYC & reverification API; Merchant onboarding workflow |
| list | Catalog Authoring & Content | Product content, variation logic, compliance attributes, listing publication | Listing management UI; Listing ingestion pipeline; Catalog authoring pipeline |
| bran | Brand Protection & Registry | Brand ownership, counterfeit defense, content control, enforcement | Brand Registry UI; Brand rights and enforcement |
| price | Pricing & Offer Health | Price competitiveness, buy-box monitoring, offer health, suppression awareness | Offer health UI; Offer health monitoring |
| fbao | FBA Inbound & Operations | Inbound planning, receiving, prep compliance for platform-fulfilled inventory | FBA operations UI; Fulfillment event ingestor; Inbound orchestration |
| invn | Inventory Planning & Availability | Forecasting, replenishment, availability control, stock risk across nodes | Inventory planning UI; Inventory signal worker; Forecast and replenishment engine |
| supp | Seller-Fulfilled Operations | Merchant-managed order handling, promise management, shipping events, service quality | Merchant fulfillment UI; Merchant fulfillment workflow |
| payo | Payouts, Fees & Ledgers | Seller balances, fee explanation, reserves, settlement timing, billing reconciliation | Financial account UI; Settlement ledger poster; Merchant ledger service |
| spon | Sponsored Ads & Retail Media | Sponsored product, brand and display ads on retail intent | Ads console UI; Ad pacing controller; Retail media serving and optimization |
| dspm | DSP Audiences & Programmatic Media | Audience building, programmatic buying, retargeting off-surface | DSP workflow UI; Audience sync worker; Audience and programmatic orchestration |
| repr | Retail Analytics & Reporting | Reporting across traffic, conversion, sales, inventory and campaigns | Reporting UI; Reporting & export API; Reporting pipeline; Commerce reporting model |
| iden | Identity, Accounts & Entitlements | Shared account, household, entitlement and merchant identity platform | Identity APIs; Account graph and entitlements |
| risk | Fraud, Abuse & Policy Controls | Abuse detection, policy enforcement, account risk, trust interventions | Policy decision APIs; Abuse signal consumer; Risk scoring and enforcement |
| auth | Authenticity & Listing Trust | Listing legitimacy and authenticity signals protecting shoppers and brands | Trust signal APIs; Listing scan worker; Listing trust engine |
| care | Customer Care & Resolution | Case management, escalation, policy-guided recovery, cross-party resolution | Support UI; Agent & operator console; Case routing worker; Case orchestration |
| reco | Personalization & Recommendations | Personalized merchandising, replenishment suggestions, recirculation | Recommendation APIs; Recommendation model serving |
| anal | Commerce Measurement & Experimentation | Measurement, experimentation, incrementality, decision support | Measurement APIs; Attribution pipeline; Experiment and measurement platform |
| apii | Commerce APIs & External Integrations | APIs for reporting, partner tooling and ecosystem workflows | Partner API gateway; Partner integration gateway |

**Data stores the model assumes (inference):** one operational database per core record (customer profile, contact points, consent, credentials, access policy, payment instrument references, transactions, search, checkout, seller identity, delivery promise, payout ledger, ad campaigns, attribution, trust cases, appeals, inventory position, seller health); event topics for audit log, order tracking, returns, catalog authoring and fulfillment events; blob stores for reviews and brand registry; a session token cache.

### 1.3 B2B — b2b-wholesale-ecommerce-platform (specialist: B2B/B2C webshops for trading companies)

**Capability scope (model's own):** B2B and B2C webshops for wholesalers, technical wholesalers, e-tailers and retailers: customer-specific prices and assortments, quotes and reorder, checkout, payments and shipping, ERP and marketplace integration, CMS and SEO, and a managed service (hosting, backups, automated QA, test environments, support). Sibling specialist products appear only as integrations.

**Root groups:** Storefront and Content (Storefront and Content Management; Product Discovery) · B2B and B2C Commerce (Trade Accounts and Pricing; Checkout, Orders and After-Sales) · Integrations and Insight (Back-Office and Channel Integration; Commerce Insight) · Platform and Managed Service (Platform Foundation; Delivery and Operations).

| Id | Brick | Capability (one line) | Modules |
| --- | --- | --- | --- |
| stor | Storefront Experience and Theming | Responsive, SEO-friendly storefront from standard templates plus customer-specific theming | Storefront Pages; Theme and Layout Kit; Storefront Backend-for-Frontend; Page and Fragment Cache |
| cmsx | Content Management and Page Builder | Block-based CMS with media and per-page SEO in the same back office as products | CMS Page Editor; Content API; Content Store; Media Library |
| seox | SEO and Search Engine Visibility | Page structure, metadata, sitemaps and a shopping feed for search engines | SEO Settings Panel; Sitemap and Feed Generator; SEO Metadata Service; Google Shopping Connector |
| catg | Product Catalogue and Specifications | Products, variants, categories, technical specifications, datasheets, multilingual texts for large wholesale catalogs | Catalogue Back Office; Catalogue API; Product Import Consumer; Product Store |
| srch | Search, Filters and Suggestions | Search-engine-backed product search with specification filters and suggestions | Search and Filter UI; Search API; Index Updater; Search Index |
| acct | B2B Customer Accounts and Self-Service Portal | Company accounts with multiple buyer logins, customer groups, addresses, order history, invoices | Customer Portal; Account API; Account Store |
| prce | Customer-Specific Pricing and Assortments | Net price lists, tiered (staffel) discounts, contract prices, customer-specific assortments, special rules (e.g. commodity-indexed prices) | Pricing Back Office; Price API; Price Calculation; Price Agreement Store |
| quot | Quotes and Quick Reorder | Quote requests, quote-to-order, order repeat, quick order by article number | Quote Request UI; Quick Order and Reorder; Quote and Reorder API; Quote Store |
| cart | Cart and Checkout | Basket, addresses, shipping choice, payment and order placement for B2B and B2C in one platform | Cart and Checkout UI; Checkout API; Checkout Orchestrator |
| ordr | Order Management | Order records, statuses, back-office overview; publishes order events for ERP export, marketplaces, shipping, analytics | Order Back Office; Order API; Order Event Queue; Order Store |
| paym | Payments | Payment methods through provider connectors; payment on account for B2B buyers | Payment API; Payment Webhook Consumer; Payment Provider Connectors |
| shpo | Shipping Options and Carrier Labels | Delivery options in checkout; labels and track-and-trace through carrier and shipping-platform connectors | Shipping Options API; Shipping Rule Engine; Carrier and Shipping-Platform Connectors |
| loyl | Promotions and Loyalty Points | Promotions, discount rules and a loyalty points system with configurable earn and burn ratios | Promotion and Loyalty Admin; Promotion API; Promotion Rules; Loyalty Points Ledger |
| wdrw | Withdrawal and Return Requests | Consumer withdrawal-right form (14 days) with confirmation emails; connector to a returns platform | Withdrawal Form Page; Withdrawal API; Withdrawal Register; Returns Platform Connector |
| erpi | ERP and Back-Office Integration | Standard connectors to ERP and business systems; order export and master-data sync | Integration API; ERP Sync Worker; Order Export Consumer; ERP Connectors |
| mkti | Marketplace and Product Feed Integration | Extends the catalog to marketplaces directly or via a channel integrator; marketplace orders flow back | Channel Settings; Feed Export Worker; Marketplace Connectors |
| invs | Stock Availability and Delivery Promise | Real-time stock on product and checkout pages fed by ERP, POS or WMS | Stock API; Stock Update Consumer; Stock Store |
| anly | Commerce Analytics and Reporting | Sales, conversion, search and adoption reporting combining shop events with web analytics | Sales Dashboard; Event Collector; Reporting Store; Analytics Tag Connector |
| blck | Building-Block Library and Shop Configuration | Library of reusable building blocks and package entitlements deciding what a shop may use | Shop Configuration Console; Building-Block Registry; Package Entitlements |
| mltt | Multi-Shop, Multi-Language and Multi-Currency | Several shops or brands and languages from one back office | Site Routing; Shop Context Resolver; Translation Store |
| iamx | Identity and Access Management | Logins and roles for back-office users, B2B buyers and consumers | Login and Roles UI; Authentication API; User Directory |
| tenv | Test Environments and Release Management | Shielded per-customer test environment; custom work accepted there, released after four-eyes review | Environment Console; Deployment Pipeline; Environment Registry |
| qaut | Automated Quality Assurance | Nightly functional tests, screenshot comparison, vulnerability test against used software versions | Nightly Test Runner; Screenshot Comparator; Test Results Store; Vulnerability Feed Connector |
| host | Hosting, Backup and Security Operations | Automated patching, daily backups, certified operations; dedicated hosting option | Backup Scheduler; Patch Automation; Hosting Inventory; Infrastructure Provider Connector |
| supp | Customer Support and Change Requests | Support desk, manual, fixed contact; change requests become blocks or quoted custom work | Support Form and Manual; Ticket Desk; Ticket Store |

### 1.4 RET — ecommerce-returns-management-platform (specialist: returns)

**Capability scope (model's own):** branded self-service returns portal, policy rules, labels and carrier choice, paid returns, tracking and notifications, exchanges and store credit, return operations (AI rule agent, automations, warranty/damage approval, receipt and inspection, resolutions, in-store returns, inquiry handling) and return insights; connectors to shop platforms, carriers, WMS/fulfillment, ERP, helpdesk, marketing, size-and-fit, fraud and stock-planning apps.

**Root groups:** Shopper Returns Experience (Self-service Return Request; Return Logistics for Shoppers) · Revenue Retention (Exchanges and Credit) · Return Operations (Policy and Automation; Approval, Receipt and Resolution; Service Desk) · Return Insights (Analytics) · Integration and Merchant Platform (Commerce Stack Connectors; Platform Foundations).

| Id | Brick | Capability (one line) | Modules |
| --- | --- | --- | --- |
| rprt | Branded Returns Portal | Shopper self-service on the merchant's branding: order lookup, item and reason selection, policy-filtered options, instructions | Portal Web App; Portal BFF; Return Request Service |
| mloc | Multi-country Returns and Localisation | Country-specific return addresses, carriers, languages and rules from one merchant account | Locale Resolver; Country Configuration Service |
| rpay | Paid Returns and Return Fees | Adjustable return fees with a payment screen; fees deductible from refunds | Return Fee Checkout; Fee Calculator; Payment Service Provider Adapter |
| rlbl | Return Labels and Carrier Selection | Labels issued instantly or after approval; shopper carrier choice; merchant's own carrier contracts | Label API; Label Service; Carrier Contract Service |
| carr | Carrier Network Integration | Connectors to parcel carriers for labels and tracking events | Tracking Poller; Carrier Gateway |
| rtrk | Return Tracking and Notifications | Visual tracking flow and automatic emails about return shipments and refunds | Return Tracking Page; Notification Dispatcher; Email Delivery Adapter |
| exch | Exchange Engine | Size and variant exchanges on real-time availability; confirmed instantly or after inspection | Exchange Picker; Exchange Orchestrator; Exchange Order Service |
| scrd | Store Credit and Bonus Credit | Automatic store credit with optional bonus, synced as gift cards or credit to the shop platform | Store Credit API; Credit Ledger Service; Gift Card Sync Adapter |
| rpol | Return Policy and Rules Engine | Windows, eligible reasons, exceptions, fees and handling rules by product, region, segment | Policy Editor; Policy Evaluation API; Rule Evaluator; Policy Store |
| auto | Return Automation and AI Rule Agent | AI agent helping build rules; automation runner for resolutions, tagging, restock location | Rule Agent Chat; Automation Runner; Rule Drafting Agent; LLM Provider Adapter |
| gate | Warranty, Claims and Approval Gate | Approval before labels; answers and photos; central review of damage and warranty claims | Claim Intake Form; Review Queue Console; Claim Case Service |
| insp | Return Receipt and Inspection | Receiving and grading, inspection-dependent resolutions, restock location assignment (may run in the partner WMS) | Receiving Console; Restock Location Assigner; Inspection Service |
| rres | Refund and Resolution Orchestration | Decides and executes refund, exchange or credit; writes refunds back to the shop; deducts fees | Resolution Queue; Resolution Orchestrator; Refund Write-back Adapter |
| isrt | In-store Returns | Online orders returned in a physical store, registered in the same flow | Store Return Console; Store Return API |
| cxin | Return Inquiry Handling | Return context inside helpdesk tools; optional managed inquiry desk | Helpdesk Context API; Managed Inquiry Desk; Helpdesk Adapter |
| pipe | Return Event and Analytics Pipeline | Return lifecycle events loaded into an analytics mart for dashboards, automations, webhooks, benchmarks | Return Event Bus; Analytics Loader; Analytics Mart |
| rins | Return Insights Dashboard | Product- and revenue-level return rates, trends, exchange and credit insights, behavior patterns | Insights Dashboard; Insights Query BFF; Metrics Service |
| ridx | Product Return Impact Index | Revenue impact of returns per SKU; flags high-return SKUs with reasons | SKU Root-cause View; SKU Flagging Job; Impact Index Calculator |
| bnch | Benchmarking and Category Insights | Anonymized cross-merchant aggregates for benchmark reports | Benchmark View; Benchmark Aggregator |
| bexp | BI Export and Data Feeds | Return data into merchants' BI tools | BI Export API; BI Connector |
| ecom | E-commerce Platform Connectors | Order and catalog import, refund/exchange/credit write-back for major shop platforms | Platform App Installer; Order Import Adapter; Catalog and Stock Adapter; Order Write-back Adapter |
| erpw | ERP, WMS and Fulfilment Connectors | Native return sync with WMS, fulfillment partners and ERPs | Sync Retry Queue; WMS Return Sync; ERP Return Sync |
| ecos | Ecosystem App Connectors | Marketing, loyalty, size-and-fit, fraud prevention, stock planning connectors | App Connections Page; Ecosystem Event Router; Fraud Check Orchestrator; App Connection Service; Marketing and Loyalty Adapter; Size and Fit Adapter; Fraud Screening Adapter; Stock Planning Adapter |
| oapi | Open API and Webhooks | Public REST API and webhooks for custom integrations and partners | Public REST API; Webhook Dispatcher; API Key Service |
| tnnt | Merchant Account, Branding and Onboarding | Merchant accounts, storefronts, branding, users, plan, guided onboarding | Merchant Settings; Onboarding Console; Merchant Account Service |

### 1.5 EDI — edi-and-b2b-document-exchange-platform (specialist: EDI and e-invoicing network)

**Capability scope (model's own):** EDI network and partner directory, onboarding, translation/validation/routing, orders, despatch advice and SSCC, e-invoicing, archive, vendor managed inventory, web portal, monitoring, ERP/WMS integration, AI document mapping. Excluded: ERP functionality itself, shipping, marketplaces, payments, customs.

**Root groups:** Trading Network and Partner Onboarding (Network and Directory; Onboarding and AI Mapping) · Document Exchange Core (Transport, Translation and Validation; Business Documents) · Customer Workspace and Integration (Portal and Visibility; Systems Integration) · Platform Foundation (Commercial and Identity; Trust and Service).

| Id | Brick | Capability (one line) | Modules |
| --- | --- | --- | --- |
| tpdr | Trading Partner Directory and Network Registry | Searchable registry of reachable organizations and the documents each can send or receive | Trading Partner Search; Partner Directory API; Network Registry Service; Identifier Reference Sync |
| rprf | Retailer Requirement Profiles and Format Library | Library of partner-specific message guidelines: EDIFACT subset, mandatory segments, SSCC rules, invoice conditions | Requirement Profile Admin; Profile and Specification Store |
| ponb | Partner Onboarding and Connection Testing | Request intake, partner contact, test interchanges, parallel run, go-live | Connection Request Wizard; Onboarding API; Test Interchange Runner; Onboarding Workflow Service |
| trai | AI Document Recognition and Auto-Mapping | Recognizes documents in unfamiliar formats and proposes mappings for human review | Traci Mapping API; Mapping Proposal Orchestrator; Document Understanding Service; Mapping Review Queue; AI Model Provider Adapter |
| cnct | Communication Gateway and Secure Transport | Interchanges over the protocols partners use (TLS, AS2, SFTP) plus Peppol access-point traffic | Interchange Ingest Endpoints; Inbound and Outbound Message Queue; Protocol Session and Certificate Service; Network Interconnect Adapters |
| tran | Format Translation and Mapping Engine | Translates between each customer's in-house format and the partner's standard (EDIFACT, UBL) | Translation Worker; Syntax Converters; Mapping Repository |
| vald | Message Validation and Business Rules | Blocks erroneous messages before they reach the partner and explains the error in plain language | Validation Engine; Rule Set Service |
| rout | Message Routing and Delivery Tracking | Routes validated messages and records every status change visible to both parties | Routing Worker; Message Status Ledger |
| ordr | Order and Order Response Processing | Normalizes retailer purchase orders (ORDERS), changes and responses (ORDRSP) for the supplier ERP | Order Normaliser; Order Document Service |
| desp | Despatch Advice and SSCC Labelling | Despatch advice (DESADV) and GS1 SSCC pallet labels from order and packing data | Packing and Label Screen; Despatch API; SSCC Numbering and Label Service; Despatch Advice Builder |
| einv | E-Invoicing and Mandate Compliance | ERP invoices into EDIFACT INVOIC for retailers and EN 16931 e-invoices (XRechnung, ZUGFeRD, Peppol) for mandates | E-Invoice Format Builder; Invoice Document Service; Peppol Access Point Adapter |
| arch | Document Archive | Retains exchanged documents for audit and retrieval | Archive Retrieval API; Archive Store Service |
| vmi | Vendor Managed Inventory | Retailer sales, stock and forecast messages drive proactive supplier replenishment | VMI Forecast Dashboard; Replenishment Planner |
| webp | Web EDI Portal | Suppliers without an ERP link process orders and create confirmations, despatch advice and invoices by hand | Document Inbox and Editor; Portal Backend for Frontend |
| mntr | Monitoring, Alerts and Exception Resolution | Watches every connection and flow; alerts; resolution queue | Exception Console; Flow Watchdog; Alerting and Case Service |
| rept | Message Analytics and Reporting | Volumes, error rates, partner performance | Message Insight Dashboard; Metrics Aggregation Service |
| erpi | ERP and WMS API and Connector Framework | API-first integration with ERP and WMS; file-based exchange for older systems | Customer Integration API; File Drop Interface; ERP Connector Adapters |
| kpch | Commerce Hub Connectors | Ready links to sibling specialist products (ERP, POS, webshop, marketplace, shipping, returns, WMS) | Commerce Hub Event Bridge; Logic4 and Vendit ERP Connector; DeliveryMatch, Picqer and Returnista Connector; Highbiza and EffectConnect Connector |
| tnnt | Tenant, Subscription and Plan Management | Customer accounts, plans, terms, online purchase | Plan Selection and Checkout; Subscription and Entitlement Service; Billing System Adapter |
| iden | Identity and Access Management | Users for customers, partners and their trading partners; least-privilege access; API credentials | Authentication API; User and Role Directory |
| secu | Security, Compliance and Continuity | ISMS controls, encryption in transport, pentests, incident response levels, replicated data centers, NIS2 assurance pack | Trust and Assurance Pack Portal; Replication and Failover Daemon; Key and Certificate Vault; Security Audit Log Service |
| supp | EDI Expert Support and Service Desk | Multilingual EDI specialists supporting customers and partners | Support Desk Console; Ticket and Knowledge Service |

### 1.6 HUB — katapull-commerce-hub (aggregate of the eight specialist models)

**Model's own framing:** one high-level brick per specialist product plus two group-level hub bricks; it answers "which customers do the platforms share, and which platform does each use for which job". For the book this model matters only as the shape of a **best-of-breed stack assembled from specialist products** (webshop, marketplace connector, POS, ERP, EDI, WMS, shipping, returns, plus a connectivity layer and a shared customer view). Nothing about group plans is carried over.

**Root groups:** Sell Across Channels (Own Webshops; Marketplaces; Physical Stores) · Run the Trading Business (Commerce Core; Trade Documents) · Fulfil and Deliver (Warehouse; Delivery; After-Sales) · Commerce Hub Foundation (Connectivity; Shared Customer View).

| Id | Brick | Capability (one line) | Modules |
| --- | --- | --- | --- |
| hbza | B2B and B2C Webshops | Managed webshops with customer-specific pricing, quotes, reorder; ERP, carrier and marketplace integrations (= model B2B) | Workspace; API and Connectors; Storefront, Content and Search; B2B Accounts, Pricing and Checkout; Managed Hosting and Release Service; Hub Connectors |
| efco | Marketplace Integration | One hub connecting webshops and back offices to many marketplaces (= model MKT) | Workspace; API and Connectors; Catalog, Content Mapping and Translation; Pricing, Repricer and Buy Box; Marketplace Orders, Stock and Fulfilment; Hub Connectors |
| vndt | POS and Store Management | POS, stock, webshop and store management for specialty retailers (= model POS) | Workspace; API and Connectors; POS Checkout and Customer Service; Assortment, Stock and Purchasing; Online Order Hub and Store Webshop; Hub Connectors |
| lgc4 | Commerce ERP | All-in-one webshop and ERP: PIM, orders, stock, purchasing, CRM, POS, accounting (= model ERP) | Workspace; API and Connectors; Product Information and Pricing; Order Management, Quote to Invoice; Stock, Purchasing and Accounting; Hub Connectors |
| trns | EDI and E-invoicing | EDI network for orders, despatch advice, SSCC, invoices, VMI (= model EDI) | Workspace; API and Connectors; Trading Partner Network and Onboarding; Document Translation, Validation and Routing; E-invoicing and Mandate Compliance; Hub Connectors |
| pcqr | Warehouse Management and Fulfilment | Cloud WMS with multi-client fulfillment (= model WMS) | Workspace; API and Connectors; Inventory Ledger, Locations and Purchasing; Picking, Packing and Returns Processing; Multi-Client Fulfilment and Portal; Hub Connectors |
| dlvm | Shipping and Carrier Management | Dynamic checkout, multi-carrier booking, tracking, returns shipping, freight audit (= model SHP) | Workspace; API and Connectors; Dynamic Checkout and Delivery Promise; Shipping Rules, Carrier Booking and Labels; Tracking, Returns Shipping and Freight Audit; Hub Connectors |
| rtns | Returns Management | Returns portal, exchanges, store credit, operations, insights (= model RET) | Workspace; API and Connectors; Branded Returns Portal and Labels; Exchanges and Store Credit; Return Rules, Operations and Insights; Hub Connectors |
| hubc | Commerce Hub Bridges and Connection Registry | Group-level layer for productized connections between the specialist products; today the bridges live inside each product | Hub Connection Console; Cross-Platform Event Routing; Hub Account and Connection Registry; Platform Bridge Adapters |
| hubv | Shared Customer and Commerce Chain Insight | Which products an account uses for which jobs, connection health, chain KPIs (order-to-delivery time, margin after fees, return rate) | Shared Account Overview; Commerce Chain Dashboard; Chain KPI and Platform Fit Analysis; Cross-Brand Customer Registry |

### 1.7 MKT — marketplace-channel-integration-platform (specialist: marketplace integrator)

**Capability scope (model's own):** channel connectivity (marketplaces, feed channels, webshop plugins, back-office connectors, public API, embedded partner integrations, app store), central catalog and content mapping, pricing and repricing, order and stock synchronization, marketplace fulfillment, insights and retail media, platform foundation.

**Root groups:** Channel Connectivity and Integration (Marketplace and Feed Channels; Commerce System Connections) · Catalog and Content · Pricing and Competitiveness · Orders, Stock and Fulfilment (Order Lifecycle; Inventory and Fulfilment) · Insights and Growth · Platform Foundation.

| Id | Brick | Capability (one line) | Modules |
| --- | --- | --- | --- |
| mcon | Marketplace Connector Framework | One canonical model and an adapter library for many European marketplaces, absorbing each API, its rate limits and quirks | Channel API; Channel Sync Scheduler; Canonical Channel Mapping; Channel Adapter Registry; Marketplace API Adapters |
| chob | Channel Onboarding and Configuration | Guided marketplace connection: authentication, country and fulfillment settings, order flow options | Channel Setup Wizard; Channel Configuration API; Channel Settings Store; Marketplace Authorisation Connector |
| fdmg | Feed Manager | Builds and schedules product feeds for marketing and comparison channels from the central catalog | Feed Builder; Feed API; Feed Export Worker; Feed Destination Connectors |
| shop | Webshop Platform Plugins | Apps and plugins syncing products, stock and orders between popular webshop platforms and the hub | Webshop Connector API; Webshop Sync Consumer; Webshop Platform Plugins |
| erpi | Back-office and ERP Connectors | Native connectors to back-office systems and partner middleware | Back-office Connector API; Back-office Sync Consumer; Back-office Connectors |
| papi | Public Merchant API | Documented REST API for products, offers, stock and orders with auth, throttling, webhooks | Developer Portal; REST API v3; Webhook Dispatcher; API Authentication and Throttling |
| embd | Embedded Partner Integrations | Partner API and white-label pages letting WMS/TMS/SaaS vendors embed marketplace connections | Branded Connection Pages; Partner API; Uniform Order Format; Partner Tenant Registry |
| apst | App Store and Partner Ecosystem | Catalog of apps and partners extending the hub | App Store Catalogue; App Install API; App Listing Service |
| pcat | Product Catalog Hub | Central catalog merging products, prices and stock from webshops, back offices and file feeds; families, bundles, multilingual content | Catalogue Workspace; Catalogue API; Feed Import Worker; Product Master Service; File and Sheet Importers |
| dsel | Dynamic Product Selections | Rule-based selections deciding which products go to which marketplace, feed or repricer strategy | Selection Builder; Selection API; Selection Evaluator |
| cmap | Content Mapping and Validation | Maps catalog data to each marketplace's categories, required attributes and allowed values; validates before sending | Mapping Workbench; Mapping API; Category Schema Refresh; Listing Validator; Category Schema Cache |
| rule | Smart Data and Custom Attribute Rules | Rule engine deriving channel-specific titles, attributes and corrections | Rule Editor; Rule API; Rule Engine |
| trns | Content Translation | Automatic translation of product content per country; AI translation add-on | Translation API; Translation Worker; Translation Memory; Translation Provider Connector |
| prce | Price Calculation and Planning | Base prices per marketplace from cost, commission, fixed costs, currency; promotion planning | Price Formula Builder; Pricing API; Price Calculator; Promotion Planner; Exchange Rate Connector |
| rprc | Repricer and Buy Box Engine | Continuous re-evaluation of each offer against competitors and buy-box holders per strategy | Repricer Dashboard; Repricer API; Repricing Loop; Strategy Evaluator; Price History Store |
| cmpi | Competitor Offer Analysis | Competing offers per product and marketplace; look-alike matching | Offer Analysis View; Offer Analysis API; Offer Collector; Look-alike Matcher; Competitor Offer Store |
| ordr | Marketplace Order Hub | Imports, normalizes and routes marketplace orders to webshop, back office, WMS or partner; tracks lifecycle | Order Overview; Order API; Order Import Worker; Order Normaliser; Order Store |
| ship | Shipment and Order Status Sync | Shipment confirmations with tracking, cancellations and return statuses back to each marketplace within its deadlines | Shipment API; Status Sync Worker; Carrier Code Mapper |
| stck | Stock Synchronisation and Locations | Available-to-sell stock per channel from multiple locations with buffers, pushed in near real time | Stock Locations View; Stock API; Stock Push Worker; Available-to-sell Calculator; Stock Ledger |
| fulf | Fulfilment Manager | Ship from own or marketplace warehouses per order; switch offers; prepare replenishment shipments | Fulfilment Console; Fulfilment API; LVB Switch Daemon; Fulfilment Routing Rules; Replenishment Planner; Marketplace Fulfilment Connectors |
| rprt | Sales Reporting and Insights | Revenue, orders, buy box and margin per marketplace, product and period; exports | Insights Dashboard; Reporting API; Metrics Aggregation Worker; Sales Mart; Analytics Export |
| rmed | Retail Media Dashboard | Retail media campaign and trade-deal performance from several retailers in one dashboard | Retail Media Dashboard; Retail Media API; Campaign Import Worker; Campaign Performance Store; Retail Media Connectors |
| advs | Account Health and Optimisation Advice | Sync errors, rejections, buy box, stock-outs and optimization advice | Advice Feed; Account Health Console; Account Health Scoring |
| tnnt | Accounts, Plans and Entitlements | Merchant accounts, plans, add-on modules, metering of articles and orders | Account Administration; Usage Meter; Entitlement Checker; Subscription Service; Billing Connector |
| iden | Identity and Access | Users, roles and API keys for merchants, partners and staff | Login; Auth API; User and Role Store |
| irun | Integration Runtime and Monitoring | Shared job queue, retries, rate-limit governance, event log and monitoring for every sync | Integration Monitor; Job Queue; Retry Daemon; Rate Limit Governor; Integration Event Log |
| csup | Implementation and Support Desk | Onboarding project tracking and multilingual support | In-app Support; Implementation Tracker; Helpdesk Connector |

### 1.8 ERP — omnichannel-commerce-erp-platform (specialist: all-in-one webshop and ERP for trading companies)

**Capability scope (model's own):** webshops and B2B portal, checkout and payments, cloud POS, marketplace bridge, EDI gateway, PIM, pricing, supplier data import, quote-to-invoice order management, CRM, returns and repair, multi-warehouse stock, picking, purchasing, shipping, route planning, accounting, BI, tenancy, API hub, migration, workflow automation.

**Root groups:** Commerce Front Office (Webshops and B2B Buying; Stores; Channels and Trading Partners) · Commerce Core (Product and Price; Orders and Customers) · Supply Chain and Warehouse (Stock and Warehouse; Purchasing and Delivery) · Finance and Insight (Finance and Reporting) · Platform Foundation (Platform Services).

| Id | Brick | Capability (one line) | Modules |
| --- | --- | --- | --- |
| wshp | Webshop Storefront and Content | Responsive storefront with search, product pages, configurator, cross-sell, reviews, blog, loyalty, self-managed content | Storefront; Content and Design Editor; Storefront BFF; Content and SEO Service; Product Search and Filtering |
| b2bp | B2B Customer Portal and Accounts | Customer-specific assortments and prices, quick-order lists, order history, invoices, multiple contacts | Customer Account Portal; Account API; Account Preferences and Lists Service |
| ckpy | Checkout and Payments | Checkout and payment handling online and in store through payment-provider plugins | Checkout; Checkout API; Payment Service; Payment Provider Connector |
| posr | Cloud POS and Branch Operations | Multi-branch register: scan and pay, customer display, cross-branch reservations and lookups, cash-up, receipts posted to the branch administration | POS Register; Customer Display; POS API; POS Session and Receipt Service; Cross-Branch Reservation Service; Payment Terminal Connector |
| mkpl | Marketplace Channel Bridge | Product, offer and stock feeds to marketplace middleware; marketplace orders imported with payment and shipping data | Channel Export API; Marketplace Order Importer; Channel Mapping; EffectConnect Connector |
| edig | EDI Gateway | Orders, order responses, despatch advices and invoices with trading partners in EDI formats | EDI Partner API; EDI Message Worker; EDI Mapping; EDI Network Connector |
| pimx | Product Information Management | Central article master: items, variants, specifications, images, supplier links, channel publication | Article Editor; Product API; Channel Publication Queue; Article Master Service; Media Service |
| prce | Pricing, Price Agreements and Discounts | Sales price rules from purchase price and margin, customer agreements, tier discounts, channel prices, head-office pushes | Price Agreement Editor; Price API; Price Calculation; Price Rule Service |
| supd | Supplier Article Data Import | Imports and matches supplier article files; updates purchase prices; flags changes | Import Monitor; Supplier Feed Importer; Article Matching; Supplier and Branch Database Connector |
| ordr | Order Management (Quote to Invoice) | Quotes, orders from all channels, reservations, backorders, partial deliveries, dropshipping, credit checks, invoice runs | Order Desk; Order API; Invoice Run Worker; Order Orchestrator; Order Service; Quote Service |
| crmx | CRM and Sales Pipeline | Leads, prospects, customers, partners; pipelines, activities, contact history; sync to email marketing | Relation Workspace; Relation API; Relation Service; Pipeline Service; Email Marketing Connector |
| rtrn | Returns, Service and Repair | RMA requests, inspection, restock or scrap, credit notes, service and repair orders | Return Desk; Return API; RMA Service; Service Order Service; Returns Portal Connector |
| invt | Inventory and Multi-Warehouse Stock | Real-time stock per warehouse, branch and location as movements; reservations; serial numbers; layout; count reminders; stock events to channels | Stock Overview; Stock API; Stock Event Publisher; Count Scheduler; Stock Ledger Service; Location Service |
| pick | Warehouse Picking and Scanner App | Location-sorted pick lists on scanners, barcode confirmation, pack station, double-processing protection | Scanner App; Picking BFF; Pick Route Builder; Pick List Service |
| prch | Purchasing and Replenishment | Purchase suggestions from min/max and backorders; purchase orders; receipts; supplier invoices | Purchase Workbench; Purchase Order API; Reorder Suggestion; Purchase Order Service |
| ship | Shipping and Carrier Integration | Delivery options at checkout; shipment creation and label booking through multi-carrier platforms; tracking | Shipment API; Delivery Options API; Label Print Worker; Shipment Service; Carrier Platform Connector |
| rout | Route Planning for Own Delivery | Trips from orders, stop sequence and driver lists for own vans | Route Planner; Route Optimizer; Trip Service; Maps Connector |
| acct | Accounting and Multi-Administration | General ledger, debtors and creditors, dunning, bank import, VAT, multiple administrations; postings from orders, POS, purchasing, marketplaces | Ledger Workspace; Journal API; General Ledger Service; Receivables and Payables Service; Bank Feed Connector; E-invoice Connector |
| binf | Management Information and BI | Dashboards for revenue, margin, stock and cash-flow forecasts across administrations | Dashboard Widgets; Metrics API; Metrics Aggregator; Cash-flow Forecast; Metrics Store |
| tenn | Tenant, Users and Permissions | Environments with administrations, branches, shops and warehouses; users, roles, audit of changes | Admin Console; Identity API; Tenant Configuration API; Tenant Configuration Service; Permission Service |
| apig | Public API and Integration Hub | Public API and webhooks; integration point for sibling specialist products | Public API; Webhook Dispatcher; Integration Orchestrator; Katapull Sibling Bridge |
| migr | Data Migration and Onboarding | Import of items, relations, stock and open items from legacy systems with validation | Migration Workbench; Import Pipeline; Data Validation |
| wflw | Workflow Automation | Rule-based automation on order, stock or relation events: notifications, status changes, documents | Workflow Designer; Event Trigger Consumer; Workflow Engine |

### 1.9 POS — retail-pos-and-store-management-platform (specialist: specialty-retail POS and store management)

**Capability scope (model's own):** counter checkout and payments, receipts and day closing, store hardware, customer file and loyalty, quotes/customer orders/invoices, repair and workshop management, article master, pricing and purchase-price formulas, multi-location stock, stocktaking, purchasing and supplier connections, reporting, accounting export, tenant/user administration, onboarding, support. Webshop, marketplaces, shipping, returns and EDI are modeled as connectors.

**Root groups:** Store Checkout and Customer Service (Checkout and Payment; Customers, Orders and Service) · Merchandise and Inventory (Assortment and Pricing; Stock and Purchasing) · Omnichannel Commerce (Online Storefront; Marketplaces and Fulfilment) · Insight, Finance and Platform (Insight and Finance; Platform and Service).

| Id | Brick | Capability (one line) | Modules |
| --- | --- | --- | --- |
| posc | POS Checkout and Sales Registration | The till: scan or search, basket, prices, promotions, loyalty discounts, trade-ins; sale on name or anonymous | POS Checkout Screen; Sales Registration API; Offline Sales Sync; Basket Pricing Orchestrator; Sales Transaction Service |
| paym | Payment Terminal and Tender Integration | Card terminals and alternative tenders (cash, gift cards, installments); each tender recorded | Payment Terminal API; Tender Service; Payment Terminal Connectors |
| rcpt | Receipts, Cashbook and Day Closing | Printed or emailed receipts, cash drawer and cashbook, register closing so tenders and cash differences reconcile before accounting export | Day Closing Screen; Cashbook API; Receipt Mailer; Cashbook Service |
| hwdv | Store Hardware, Labels and Peripherals | Screens, scanners, receipt and label printers, drawers, handhelds; shelf labels | Label and Shelf-card Designer; Device Profile Service; Peripheral Drivers |
| crmc | Customer Registry | Customer file for sale on name, history, repairs, invoices, loyalty; basis for clienteling | Customer Card; Customer API; Customer Service |
| loya | Loyalty, Value Cheques and Gift Cards | Customer cards, saving for discounts or gifts, printable value cheques, own-brand gift cards | Loyalty Administration; Loyalty API; Points and Voucher Service; Gift Card and Loyalty Connectors |
| quot | Quotes, Customer Orders and Reservations | Quotes, customer orders, packing slips, reservations for items not on the shelf or sold B2B | Order Desk; Customer Order API; Order Status Notifier; Customer Order Service |
| bill | Invoicing and Receivables | Invoices for B2B and on-account sales, price lists per customer, credit notes, open-item follow-up | Invoice Screen; Invoice API; Invoice Mailer; Receivables Service |
| repr | Repair and Workshop Management | Repair orders registered, scheduled, tracked; status updates; parts and labor billed at pickup | Workshop Planning Board; Repair Order API; Repair Status Notifier; Repair Order Service |
| artm | Article and Assortment Master | Articles, variants (size/color), barcodes, brands, revenue groups, images feeding till, webshop and marketplaces | Article Editor; Article API; Article Import Worker; Article Service |
| prpr | Pricing, Promotions and Purchase Price Formulas | Selling prices, price lists, promotions; purchase-price formulas deriving net prices from gross | Price and Promotion Editor; Price API; Price Engine; Price List Service |
| form | Central Formula and Branch Management | Head-office control for chains and franchise formulas: central assortment, price and promotion publication, joint purchasing, distribution across branches | Head Office Console; Branch Distribution API; Branch Publication Worker; Branch Assortment Service |
| stck | Inventory Ledger and Multi-Location Stock | Real-time stock per branch and central warehouse; every sale, return, reservation, transfer, write-off mutates the ledger; serialized items | Stock Overview; Stock API; Stock Publication Worker; Stock Ledger Service |
| cntg | Stocktaking and Mobile Scanning | Wireless stocktaking, scanning incoming goods and pick slips with handhelds | Handheld Count App; Count API; Count Reconciliation Service |
| purc | Purchasing and Min/Max Replenishment | Purchase orders, receiving, automatic replenishment proposals from min/max and daily sales | Order Proposal Screen; Purchase API; Replenishment Daemon; Purchase Order Service |
| supi | Supplier Catalogue and Electronic Ordering | Supplier article files, supplier stock checks, electronic ordering, delivery booking; EDI order/despatch/invoice exchange via connector | Supplier Feed API; Catalogue Import Worker; Supplier Link Service; Supplier and Article Data Connectors; Transus EDI Connector |
| wshp | Store Webshop | Webshop fully linked to the retail core: articles, images, prices, promotions and stock from one master; B2B login, appointment booking add-ons | Storefront; Webshop Content Manager; Storefront BFF; Webshop Catalogue Service; Online Payment Connector |
| ordr | Online Order Hub | Single intake of orders from own webshop, connected webshops and marketplaces so stock, invoicing and shipping run from one place | Order Intake API; Order Import Worker; Online Order Service |
| hbzc | Connected Webshop Sync | Keeps third-party webshops in sync for retailers who want a custom shop | Webshop Sync Worker; Webshop Platform Connectors |
| mrkt | Marketplace Channel Connector | Publishes articles with stock, lead time, prices and images to marketplaces via an integrator; imports orders | Marketplace Publish Screen; Offer Sync Worker; Marketplace Offer Service; EffectConnect Connector |
| ship | Shipping and Label Connector | Announces shipments and prints labels through shipping platforms; track-and-trace back on the order | Shipment Screen; Shipment Booking Worker; Shipment Service; Shipping Platform Connectors |
| retn | Returns Connector | Online returns registered in a returns portal flow back into store stock and refunds | Return Intake Worker; Returns Platform Connector |
| rprt | Reporting and Online Dashboard | Turnover, margin, discount, transactions, average transaction value, items per transaction vs prior periods; report library | Online Dashboard; Report Library; Reporting API; KPI Aggregation Worker; KPI Store |
| acct | Accounting Export | Sales and cashbook mutations prepared for one-click import into accounting packages | Ledger Export Worker; Journal Mapping; Accounting Connectors |
| tenu | Tenant, Branch and User Administration | Cloud environments, branches, workstations, users and roles | Administration Console; Identity and Configuration API; Tenant Configuration Service |
| intg | Partner Integration Gateway | Shared gateway and event backbone for partner and sibling integrations (ERP, accounting, reviews, shipping, marketplaces, EDI) | Partner API; Integration Event Bus; Connector Registry |
| onbd | Onboarding, Data Migration and Training | Turnkey implementation: data prepared and migrated, hardware installed, staff trained | Onboarding Tracker; Data Migration Worker; Implementation Project Service |
| supp | Customer Success, Remote Support and Updates | Helpdesk, remote support, online help, included updates | Support Portal; Ticket API; Update Distribution Daemon; Ticket Service; Remote Support Connector |

### 1.10 SHP — shipping-and-carrier-management-platform (specialist: multi-carrier shipping and transport management)

**Capability scope (model's own):** order intake from webshops, marketplaces, ERP/WMS and sibling products; dynamic stock-aware checkout; rules, carrier selection and cost calculation; booking, documents and scan-to-ship across many carriers; tracking, branded communication, exceptions and returns; carrier invoice control, dashboards and CO2.

**Root groups:** Order Intake and System Integration (Sales Channel and Business System Connectors; Partner and Ecosystem Integration) · Delivery Promise and Checkout (Checkout Options) · Shipping Decisions and Execution (Decision Logic; Execution) · Carrier Network and Tracking (Carrier Connectivity) · Post-Purchase Experience (Recipient Communication and Returns) · Control, Insight and Sustainability (Cost and Performance Control) · Platform Foundation (Shared Services).

| Id | Brick | Capability (one line) | Modules |
| --- | --- | --- | --- |
| ordi | Webshop and Marketplace Order Connectors | Imports orders to ship from webshop systems and marketplaces; writes tracking back | Sales Channel Setup Wizard; Order Intake API; Channel Order Poller; Tracking Write-back Consumer; Shipping Order Service; Webshop Platform Connectors; Marketplace Connectors |
| erpw | ERP and WMS Connectors | Standard connectors to ERP, WMS and planning systems so shipments start where orders are picked | ERP/WMS Shipment API; Document Return Consumer; System Field Mapping; ERP Connectors; WMS Connectors |
| papi | API and Partner Integration Kit | Public REST API, webhooks and partner program for embedding carriers, rules, labels, tracking, returns, delivery options | Developer Portal; Public REST API; Webhook Gateway; API Orchestrator; API Key and Partner Registry |
| ktpl | Commerce Hub Bridges | Prebuilt bridges to sibling specialist products | Commerce Hub Bridge API; Hub Event Consumer; Hub Mapping; Logic4 and Vendit Bridge; EffectConnect and Highbiza Bridge; Transus EDI Bridge; Returnista and Picqer Bridge |
| dcko | Dynamic Checkout and Delivery Options | Shows only fulfillable delivery and pickup options with price, date and CO2, computed in real time from stock location, carrier cut-offs and rules | Checkout Delivery Options Widget; Delivery Options API; Delivery Option Composer; Quote Cache |
| stkc | Stock-Aware Delivery Promise | Checks what is in stock where and when missing items arrive; classifies the order; limits options accordingly | Availability API; Stock Sync Consumer; Delivery Promise Calculator; Stock Snapshot Service |
| pudo | Pickup Point and Locker Finder | Parcel shops, lockers and pick-up-in-store across carriers for checkout and returns | Pickup Point Map; Pickup Point Search API; Pickup Point Sync; Pickup Point Index |
| rule | Shipping Rules Engine | Merchant-, 3PL- or broker-defined logic by weight, dimensions, destination, cost, channel, client, product | Rule Editor; Rule Evaluation API; Rule Simulator; Rule Store |
| csel | Carrier and Service Selection | Best carrier and service per shipment on price, service level, transit time, capacity, SLA, CO2 | Carrier Selection API; Selection Engine; Capacity and SLA Service |
| rate | Rate Cards and Transport Cost Calculation | Purchase rates per carrier contract and sales rates per client incl. surcharges; expected cost per shipment in real time | Rate Card Editor; Rate API; Surcharge Update Daemon; Transport Cost Calculator; Rate Card Store |
| book | Carrier Booking and Label Generation | Pre-announce, retrieve tracking number, print label per order or batch, parcels and pallets, domestic and international | Shipping Workbench; Booking API; Batch Booking Worker; Shipment Service |
| docs | Transport and Customs Documents | Shipping and return labels, packing slips, customs documents, dangerous-goods (ADR) labels and documents | Document API; Document Generator; Document Archive |
| prnt | Scan-to-Ship and Print Management | One scan pre-announces, prints the right documents on the right printer, sends track-and-trace | Scan Station; Print Job API; Local Print Client; Printer Registry |
| rout | Multi-Warehouse Routing and External Fulfilment | Ship-from decision across warehouses, stores and suppliers; forwards orders to fulfillment partners and dropshippers | Routing API; Fulfilment Order Forwarder; Ship-from Selector; Fulfilment Partner Connectors |
| cnet | Carrier Connector Network | Large network of carrier and broker integrations for parcels, pallets and freight | Carrier Adapter Gateway; Carrier Onboarding Console; Carrier Credential Vault; Parcel Carrier Adapters; Pallet and Freight Carrier Adapters; Broker Adapters |
| trck | Tracking Event Hub | Carrier status events by webhook or polling, normalized into one status model, published to notifications, exceptions, dashboards, channels, partners | Carrier Webhook Receiver; Tracking Query API; Tracking Poller; Tracking Event Bus; Status Normaliser; Tracking Timeline Store |
| ntfy | Branded Track & Trace Communication | Email, SMS and messaging in the merchant's style; branded tracking page per channel or brand | Branded Tracking Page; Template Designer; Notification Dispatcher; Template and Branding Store; Messaging Connectors |
| excp | Exception Management and Carrier Performance | Detects delayed, stuck, failed or returned shipments; alerts before the customer asks; carrier scorecards | Exception Inbox; Carrier Scorecard API; Exception Detector; Performance Aggregator |
| retn | Returns Portal and Return Shipping | Consumer returns portal with reason codes, return methods, rule-based cost, labels | Returns Portal; Return Request API; Return Policy Evaluator; Return Service |
| fiac | Carrier Invoice Control | Freight audit: carrier invoices compared with cost calculated at booking; discrepancies flagged; disputes | Discrepancy Board; Carrier Invoice Upload API; Invoice Parser; Invoice Matcher; Discrepancy and Dispute Service |
| dash | Logistics Dashboard and KPI Reporting | Real-time shipment overview; cost, lead time and carrier performance per client, channel, carrier | Shipment Overview; KPI Report Builder; Reporting API; Analytics Loader; Logistics Analytics Mart |
| co2c | CO2 Calculation and Reporting | Emission estimate per option and shipment; shown in checkout and reports; weighed in selection | Emission API; Emission Calculator; Emission Factor Store |
| tnnt | Tenants, Clients and Access | Accounts, users, roles; multi-client structures (a 3PL's clients as sub-accounts with own carriers, rates, branding); audit trail | Account Administration; Tenant API; Identity and Role Service; Audit Log |
| addr | Address Validation | Postcode and house-number checks; incorrect addresses recognized before booking | Address Check API; Address Normaliser; Address Reference Data Connectors |

### 1.11 WMS — warehouse-management-and-fulfilment-platform (specialist: cloud WMS for online stores and 3PLs)

**Capability scope (model's own):** store and marketplace intake, order allocation, inventory ledger, locations, counting, batch traceability, purchasing and receiving, batch picking, packing, shipping integrations, printing and hardware, returns, rules, mobile app, collaboration, reports, multi-client fulfillment with portal and invoicing, accounts and plans.

**Root groups:** Order and Channel Intake (Channels and Orders; Open API and Commerce Hub) · Inventory and Purchasing (Stock and Locations; Inbound) · Picking, Packing and Shipping (Outbound Execution) · Automation, Mobile and Insight (Work Automation and Collaboration) · Fulfilment Services (Multi-Client Fulfilment) · Platform Foundation (Shared Services).

| Id | Brick | Capability (one line) | Modules |
| --- | --- | --- | --- |
| chan | Webshop and Marketplace Store Connectors | Turn-key import of products and orders; stock, status and tracking pushed back | Store Setup Wizard; Store Connection API; Order Import Worker; Stock Push Consumer; Status and Tracking Write-back; Store Connection Service; Store and Marketplace Adapters |
| ordm | Multi-Channel Order Management and Allocation | One overview of all orders; allocates stock; picklists per warehouse; backorders and partial deliveries; pause with reason | Order Overview; Order API; Allocation and Backorder Worker; Order Service |
| b2bp | B2B Customer Portal | Mini online store on live warehouse stock: business customers see stock and their prices, order, follow status | B2B Portal Web App; B2B Portal BFF; Price List Service |
| papi | Public API and Webhooks | Public REST/JSON API and webhooks for picklist status and stock changes | Public REST API; Webhook Dispatcher; API Auth and Rate Limiting; Webhook Subscription Service |
| ktpl | Commerce Hub Bridges | Productized connections to sibling specialist products | Hub Connection Settings; Hub Bridge Service; Sibling Product Adapters |
| prod | Product Catalogue and Barcodes | Product master with images, supplier, weight, dimensions, barcodes (incl. GS1 with lot/expiry), stock settings; bulk edit | Product Management UI; Product API; Excel Import Worker; Barcode Parser; Product Service |
| invt | Inventory Ledger and Stock Sync | Every stock change recorded from zero with user and reason; physical, reserved and free stock per warehouse and location; real-time publication | Stock and History UI; Stock Query API; Stock Event Stream; Stock Ledger Service |
| locn | Warehouses, Locations and Replenishment | Multiple warehouses, pick and bulk locations, containers, A/B fast-mover classification, pick-location replenishment | Location Management UI; Fast-Mover Classification Job; Replenishment Planner; Location Service |
| cycl | Cycle Counting | Year-round counting in small rounds: all, risk-based, or only touched locations | Count Planning UI; Count Selection Engine; Count Service |
| lotb | Batch and Best-Before Traceability | Batch numbers and best-before dates at receipt, tracked through stock, moves, picks, counts, returns; FEFO | Batch and Expiry Views; FEFO Allocator; Lot Service |
| purc | Purchase Advice and Purchase Orders | Advice per supplier from stock, sales and waiting customers; purchase orders; expected deliveries | Purchasing UI; Purchase Order Mailer; Purchase Advice Engine; Purchase Order Service |
| rcvg | Goods Receipt and Put-away | Receipt by scanning into a location or container; several people per receipt; product labels; put-away hints; backorders released | Receiving UI; Receipt Service |
| pkls | Picklist and Batch Picking Engine | Picklists and batches on the optimal route; singles and bulk picking; urgent and snoozed; pausing and splitting | Picking UI; Picklist Event Stream; Route Optimiser; Batch Builder; Picklist Service |
| pack | Packing Station and Packaging Advice | Packing with barcode verification; packaging advice from dimensions or rules; packaging recorded per shipment | Packing Station UI; Packaging Advisor; Packing Service |
| ship | Shipping Provider Integrations and Labels | Shipments and labels with carriers and shipping platforms; tracking stored and pushed to channels | Shipment API; Shipped Notification Consumer; Shipment Service; Carrier and Shipping Platform Adapters |
| prnt | Automatic Printing and Warehouse Hardware Connectivity | Labels and packing slips straight to printers; scanners, sealers, applicators, conveyors, goods-to-person systems | Printer and Device Settings; Print Agent (assumed local client); Print Job Service; Mechanisation Adapters |
| retu | Returns Processing | Returns registered manually or pre-registered by return tools; scan, inspect, restock sellable items | Returns UI; Return Intake API; Return Service |
| rule | Rules Automation Engine | If-this-then-that rules on every new order and picklist: shipping method, urgency, snooze, assignment, packaging, notes | Rule Editor; Rule Evaluator; Rule Store |
| mapp | Mobile App | Handheld app for picking, receiving, counting, moving, replenishing, tasks and comments | Picqer App; Mobile BFF |
| coll | Comments, Tasks and Notifications | Comments with mentions and photos on picklists, orders and purchase orders; tasks; inbox; shared with fulfillment clients | For You Inbox; Notification Mailer; Collaboration Service |
| rprt | Reports and Warehouse Analytics | Warehouse status, team performance, stock levels, bestsellers and slow movers | Dashboard and Reports UI; Activity Aggregator; Report Query Service |
| ften | Fulfilment Client Separation | Each 3PL client's products, stock and orders separate inside one account; one floor workflow with client-specific rules | Client Administration; Fulfilment Client Service |
| fpor | Fulfilment Client Portal | Portal in the 3PL's branding: clients see stock and orders, import products, create orders, release partial deliveries | Fulfilment Portal Web App; Fulfilment Portal BFF |
| finv | Fulfilment Client Invoicing | Client rates applied to picklists, shipments, receipts, returns, packaging and storage to build invoice lines | Rate Card Editor; Invoice Line Builder |
| acct | Accounts, Users and Rights | Multi-tenant accounts, per-user rights, portal logins | User and Rights Admin; Identity and Rights Service |
| subs | Plans, Trials and Order-Volume Billing | Self-service trial, plan selection, order counting against included volume | Plan and Trial UI; Order Volume Meter; Subscription Service |

---

## 2. Cross-model capability inventory

Deduplicated across the eleven models. "Models" lists the short codes whose bricks carry the capability (the HUB model is listed only for its two group-level bricks, since its product bricks duplicate the specialist models). "Chapter" is the proposed owning chapter folder; secondary chapters in parentheses. **GAP** marks capabilities no chapter contract owns, with a note on where they could go.

### 2.1 Discover and sell (storefront, catalog, search, pricing, promotions)

| # | Capability | Models | Chapter (proposed) |
| --- | --- | --- | --- |
| 1 | Hosted storefront with themes and content pages | MCP, B2B, ERP, POS | `32-storefront-architecture` |
| 2 | Headless storefront framework, storefront API and edge hosting | MCP | `32-storefront-architecture` |
| 3 | CMS / page builder with SEO fields, sitemaps, media library | B2B, ERP | `32-storefront-architecture` (`09-search-and-discovery` for SEO) |
| 4 | Multi-shop, multi-brand, multi-language, multi-currency from one back office | B2B, MCP (mkts) | `30-multi-tenancy-and-isolation` (`06-product-information` for localization) |
| 5 | Markets and cross-border localization (currency, duties, payment methods per market) | MCP | `07-pricing-architecture` (`14-tax-invoicing-and-ledger` for duties) |
| 6 | Product catalog: products, variants, media, attributes, collections, bulk import | MCP, ORM, B2B, ERP, POS, WMS, MKT | `06-product-information` |
| 7 | Technical specifications, datasheets, configurator, product families and bundles | B2B, ERP, MKT | `06-product-information` |
| 8 | Supplier article data import and matching into the product master | ERP, POS | `06-product-information` (`23-erp-and-back-office-integration`) |
| 9 | Barcodes and GS1 identifiers (incl. lot/expiry encoding); serialized items | WMS, POS, ERP | `06-product-information` (`10-inventory-and-availability`) |
| 10 | Catalog authoring and listing publication with compliance attributes (marketplace side) | ORM, MKT | `20-marketplaces-and-channel-integration` |
| 11 | Marketplace category and attribute mapping with pre-send validation | MKT | `20-marketplaces-and-channel-integration` |
| 12 | Channel-specific content rules (derived titles, attributes, corrections) | MKT | `20-marketplaces-and-channel-integration` (`06-product-information`) |
| 13 | Automatic content translation per country | MKT, MCP (mkts), B2B | `06-product-information` |
| 14 | Product feeds for shopping, social and comparison channels | MKT, B2B, ERP, POS | `20-marketplaces-and-channel-integration` |
| 15 | Site search with filters, facets, suggestions (keyword and semantic) | MCP, ORM, B2B, ERP | `09-search-and-discovery` |
| 16 | Merchandising rules, deals placement, badges | MCP, ORM | `09-search-and-discovery` (`08-promotions-and-loyalty`) |
| 17 | Personalization and recommendations; home feed composition | ORM, MCP (srch) | `09-search-and-discovery` |
| 18 | Reviews, ratings and Q&A with moderation | ORM, ERP (wshp) | **GAP** — fits `09-search-and-discovery` (trust signals in discovery) or `06-product-information` (user-generated content as catalog data); mention in `47-case-amazon` |
| 19 | Conversational / AI shopping assistant for shoppers | ORM, MCP (shop) | `45-ai-and-agentic-commerce` (`09-search-and-discovery`) |
| 20 | Agent-facing structured catalog and open commerce protocol (agentic checkout) | MCP | `45-ai-and-agentic-commerce` |
| 21 | Price lists, customer-specific net prices, contract prices, tiered (staffel) discounts | B2B, ERP, POS, MCP (b2bc), WMS (b2bp) | `07-pricing-architecture` (`21-b2b-commerce`) |
| 22 | Sales price rules from purchase price and margin; purchase-price formulas | ERP, POS | `07-pricing-architecture` |
| 23 | Channel prices and head-office price pushes to branches | ERP, POS | `07-pricing-architecture` (`17-stores-and-omnichannel`) |
| 24 | Marketplace price calculation from cost, commission, fixed costs, currency | MKT | `07-pricing-architecture` (`20-marketplaces-and-channel-integration`) |
| 25 | Repricing and buy-box strategy; offer health and suppression monitoring | MKT, ORM | `20-marketplaces-and-channel-integration` (`07-pricing-architecture`) |
| 26 | Competitor offer collection and look-alike matching | MKT | `20-marketplaces-and-channel-integration` |
| 27 | Promotions and discount rules (discount engine, promotion planning) | MCP, B2B, ERP, POS, MKT, ORM | `08-promotions-and-loyalty` |
| 28 | Loyalty points, customer cards, value cheques, gift cards | B2B, POS, ERP | `08-promotions-and-loyalty` |
| 29 | Store credit and bonus credit as a return resolution | RET | `18-returns-and-exchanges` (`08-promotions-and-loyalty`) |
| 30 | Membership program with benefit entitlement (Prime-style) | ORM | **GAP** — fits `08-promotions-and-loyalty` as "paid membership as a loyalty mechanism"; also `47-case-amazon` and `02-commerce-business-models` |
| 31 | Dynamic product selections (rules deciding which products go to which channel) | MKT | `20-marketplaces-and-channel-integration` |

### 2.2 Order (inventory, cart, checkout, payment, order record, money)

| # | Capability | Models | Chapter (proposed) |
| --- | --- | --- | --- |
| 32 | Multi-location inventory ledger (movements, physical/reserved/free, per location) | MCP, ERP, POS, WMS, MKT | `10-inventory-and-availability` |
| 33 | Stock reservation and allocation; backorders; partial deliveries | ERP, WMS, MCP, POS | `10-inventory-and-availability` (`13-order-management`) |
| 34 | Available-to-sell per channel with buffers; near-real-time stock publication to channels | MKT, ERP, POS, WMS, B2B | `10-inventory-and-availability` (`20-marketplaces-and-channel-integration`) |
| 35 | Real-time stock and delivery promise on product and checkout pages | B2B, SHP (stkc), MCP (ship) | `10-inventory-and-availability` (`16-shipping-and-delivery`) |
| 36 | Stock transfers between locations; cross-branch reservations and lookups | MCP, ERP, POS | `10-inventory-and-availability` (`17-stores-and-omnichannel`) |
| 37 | Forecasting, replenishment and stock-risk planning across nodes | ORM, WMS (purc), ERP, POS | `10-inventory-and-availability` (`23-erp-and-back-office-integration`) |
| 38 | Cart and save-for-later; cart state and session store | MCP, ORM, B2B, ERP | `11-cart-and-checkout` |
| 39 | Hosted one-page checkout; checkout UI extensions and server functions | MCP, B2B, ERP, ORM | `11-cart-and-checkout` (`31-extensibility-and-app-ecosystems`) |
| 40 | Accelerated checkout with network-wide saved buyer identity and wallet | MCP | `11-cart-and-checkout` (`27-identity-and-master-data`, `46-case-shopify`) |
| 41 | Installments / buy-now-pay-later offers at checkout | MCP, POS (tenders) | `12-payments` |
| 42 | Delivery options in checkout (price, date, pickup points, CO2) | SHP, ERP, B2B, MCP | `16-shipping-and-delivery` (`11-cart-and-checkout`) |
| 43 | Address validation before booking | SHP | `11-cart-and-checkout` (`16-shipping-and-delivery`) |
| 44 | Payment acceptance: methods, authorization, capture, refund; provider connectors | MCP, B2B, ERP, ORM | `12-payments` |
| 45 | Merchant onboarding and KYC for payments; seller verification and reverification | MCP, ORM | `12-payments` (`34-commerce-security`, `36-commerce-regulation`) |
| 46 | Payment on account / payment terms / credit checks for B2B | B2B, MCP (b2bc), ERP | `21-b2b-commerce` (`12-payments`) |
| 47 | Fraud, abuse and risk scoring; bot protection; chargeback and dispute handling | MCP, ORM, RET (fraud screening adapter) | `12-payments` (`34-commerce-security`) |
| 48 | Card tokenization vault; payment instrument references | MCP, ORM | `12-payments` (`34-commerce-security`) |
| 49 | Merchant / seller balance, fees, reserves, payouts, settlement ledger | MCP, ORM | `14-tax-invoicing-and-ledger` (`02-commerce-business-models`) |
| 50 | Merchant capital lending from sales history | MCP | **GAP** — fits `02-commerce-business-models` (platform revenue lines) or `46-case-shopify`; not an architecture chapter topic |
| 51 | Tax, VAT, GST and import-duty calculation; liability tracking | MCP, ERP (acct) | `14-tax-invoicing-and-ledger` |
| 52 | Order system of record across channels: edits, payment state, fulfillment orders, refunds | MCP, ORM, B2B, ERP, POS (ordr), MKT (ordr) | `13-order-management` |
| 53 | Order events published for ERP, marketplaces, shipping, analytics | B2B, MCP, ORM, ERP | `25-events-consistency-and-reconciliation` (`13-order-management`) |
| 54 | Fulfillment order routing / multi-warehouse ship-from selection | MCP, SHP (rout), MKT (fulf), ERP | `13-order-management` (`16-shipping-and-delivery`) |
| 55 | Quotes and quote-to-order; quick reorder by article number; order lists | B2B, ERP, POS, MCP (b2bc) | `21-b2b-commerce` |
| 56 | Company accounts with multiple buyers, roles, customer groups, assortments | B2B, MCP, ERP, WMS | `21-b2b-commerce` (`27-identity-and-master-data`) |
| 57 | Invoicing, credit notes, receivables, dunning; invoice runs | ERP, POS, B2B (portal) | `14-tax-invoicing-and-ledger` |
| 58 | General ledger, bank import, multiple administrations / legal entities | ERP | `14-tax-invoicing-and-ledger` (`23-erp-and-back-office-integration`) |
| 59 | Accounting export / journal mapping to accounting packages | POS, ERP | `23-erp-and-back-office-integration` (`14-tax-invoicing-and-ledger`) |
| 60 | Platform subscription, app and usage billing; partner revenue share; order-volume metering | MCP, WMS, MKT, EDI, RET | `31-extensibility-and-app-ecosystems` (`30-multi-tenancy-and-isolation`) |
| 61 | Dropshipping / forwarding orders to suppliers and fulfillment partners | ERP, SHP | `13-order-management` (`15-warehouse-and-fulfillment`) |

### 2.3 Fulfill, ship, store, return, serve

| # | Capability | Models | Chapter (proposed) |
| --- | --- | --- | --- |
| 62 | Warehouse layout: multiple warehouses, pick and bulk locations, containers | WMS, ERP, POS | `15-warehouse-and-fulfillment` |
| 63 | Purchase orders, goods receipt and put-away by scanning | WMS, ERP, POS | `15-warehouse-and-fulfillment` (`23-erp-and-back-office-integration`) |
| 64 | Pick waves / batch picking with route optimization; singles and bulk picking | WMS, ERP | `15-warehouse-and-fulfillment` |
| 65 | Packing station with barcode verification and packaging advice | WMS, ERP | `15-warehouse-and-fulfillment` |
| 66 | Cycle counting and stocktaking with handhelds | WMS, POS, ERP | `15-warehouse-and-fulfillment` (`10-inventory-and-availability`) |
| 67 | Batch / lot and best-before traceability, FEFO allocation | WMS | `15-warehouse-and-fulfillment` (`36-commerce-regulation` for recalls) |
| 68 | Pick-location replenishment and fast-mover (A/B) classification | WMS | `15-warehouse-and-fulfillment` |
| 69 | Warehouse rules automation (if-this-then-that on orders and picklists) | WMS, SHP (rule), ERP (wflw) | `15-warehouse-and-fulfillment` (`31-extensibility-and-app-ecosystems`) |
| 70 | Mobile scanner app; printers, scanners, sealers, conveyors, goods-to-person hardware | WMS, ERP, POS, SHP | `15-warehouse-and-fulfillment` |
| 71 | Multi-client (3PL) fulfillment: client separation, client portal, client invoicing | WMS, SHP (tnnt) | `15-warehouse-and-fulfillment` (`30-multi-tenancy-and-isolation`) |
| 72 | Marketplace-operated fulfillment (FBA-style) inbound and offer switching | ORM, MKT | `20-marketplaces-and-channel-integration` (`15-warehouse-and-fulfillment`) |
| 73 | Shipping rules engine (weight, destination, cost, channel, client, product) | SHP, B2B, WMS | `16-shipping-and-delivery` |
| 74 | Carrier and service selection; rate shopping on price, transit, SLA, CO2 | SHP, MCP | `16-shipping-and-delivery` |
| 75 | Rate cards, surcharges, expected transport cost at booking | SHP | `16-shipping-and-delivery` |
| 76 | Carrier booking, label generation, scan-to-ship, print management | SHP, WMS, ERP, POS, MCP, B2B | `16-shipping-and-delivery` |
| 77 | Transport and customs documents; dangerous-goods (ADR) documents | SHP | `16-shipping-and-delivery` (`36-commerce-regulation`) |
| 78 | Carrier connector network (parcel, pallet, freight, brokers) | SHP, RET, WMS | `16-shipping-and-delivery` (`24-integration-styles`) |
| 79 | Tracking event hub: normalize carrier events into one status model | SHP, MCP, ORM, WMS | `16-shipping-and-delivery` (`25-events-consistency-and-reconciliation`) |
| 80 | Delivery promise calculation and promise-risk monitoring | ORM, SHP, MCP | `16-shipping-and-delivery` (`10-inventory-and-availability`) |
| 81 | Pickup points, lockers and pick-up-in-store | SHP, MCP (posr) | `16-shipping-and-delivery` (`17-stores-and-omnichannel`) |
| 82 | Branded track-and-trace communication (email, SMS, messaging); branded tracking page | SHP, RET, ORM | `19-customer-service-and-notifications` |
| 83 | Shipment exception detection and carrier performance scorecards | SHP, ORM | `16-shipping-and-delivery` (`19-customer-service-and-notifications`) |
| 84 | Carrier invoice control / freight audit and disputes | SHP | `16-shipping-and-delivery` (`14-tax-invoicing-and-ledger`) |
| 85 | CO2 estimate per delivery option and shipment; emissions reporting | SHP | **GAP** — fits `16-shipping-and-delivery` (selection criteria) and `36-commerce-regulation` (sustainability reporting); add a short "emissions as data" note |
| 86 | Route planning for own-fleet delivery | ERP | **GAP** — fits `16-shipping-and-delivery` as a sidebar ("when the merchant is the carrier"); low priority |
| 87 | POS checkout: scanning, basket pricing, promotions, loyalty, trade-ins, sale on name | POS, ERP, MCP | `17-stores-and-omnichannel` |
| 88 | Offline-capable POS with idempotent sync | POS, MCP | `17-stores-and-omnichannel` (`33-peak-load-and-reliability`) |
| 89 | Payment terminal and tender integration (cash, cards, gift cards, installments) | POS, ERP, MCP | `17-stores-and-omnichannel` (`12-payments`) |
| 90 | Receipts, cashbook, day closing / cash-up, fiscal receipt export | POS, ERP, MCP | `17-stores-and-omnichannel` (`14-tax-invoicing-and-ledger`; fiscalization rules in `36-commerce-regulation`) |
| 91 | Store hardware, shelf labels and peripherals | POS, MCP | `17-stores-and-omnichannel` |
| 92 | Central formula / head-office control of chains and franchises (assortment, prices, promotions to branches) | POS, ERP | `17-stores-and-omnichannel` (`30-multi-tenancy-and-isolation`) |
| 93 | Click-and-collect, in-store returns, cross-branch stock visibility | MCP, POS, RET (isrt), ERP | `17-stores-and-omnichannel` |
| 94 | Repair and workshop management (service orders, parts, labor) | POS, ERP | **GAP** — fits `17-stores-and-omnichannel` as a sidebar on service revenue in specialty retail; otherwise out of scope |
| 95 | Self-service returns portal: order lookup, reasons, policy-filtered options | RET, SHP, MCP, ORM, B2B (wdrw) | `18-returns-and-exchanges` |
| 96 | Return policy and rules engine (windows, reasons, fees, exceptions by product/region/segment) | RET, MCP, SHP | `18-returns-and-exchanges` |
| 97 | Return labels, carrier choice, paid returns and return fees | RET, SHP, MCP | `18-returns-and-exchanges` (`16-shipping-and-delivery`) |
| 98 | Exchanges on real-time availability; exchange orders | RET, MCP, ORM | `18-returns-and-exchanges` |
| 99 | Warranty and damage claims approval gate with photos | RET | `18-returns-and-exchanges` |
| 100 | Return receipt, inspection, grading and return dispositions (restock, scrap, repair, donate, recycle) | RET, WMS, ERP | `18-returns-and-exchanges` (`15-warehouse-and-fulfillment`; disposition reporting in `36-commerce-regulation`) |
| 101 | Refund and resolution orchestration with write-back to the shop platform | RET, MCP, ORM | `18-returns-and-exchanges` (`12-payments`) |
| 102 | Consumer withdrawal-right handling (14-day form and confirmation) | B2B | `18-returns-and-exchanges` (`36-commerce-regulation`) |
| 103 | Return insights: per-SKU return impact, benchmarks, BI export | RET | `18-returns-and-exchanges` (`28-commerce-data-and-analytics`) |
| 104 | Customer care case management, escalation, cross-party resolution | ORM, RET (cxin), EDI (mntr) | `19-customer-service-and-notifications` |
| 105 | Helpdesk context integration (order and return context inside support tools) | RET | `19-customer-service-and-notifications` |
| 106 | Customer registry / customer file with history for clienteling | POS, MCP (ordr), ERP (crmx) | `27-identity-and-master-data` (`19-customer-service-and-notifications`) |
| 107 | CRM and sales pipeline (leads, prospects, activities) | ERP | **GAP** — fits `21-b2b-commerce` (account management) or `23-erp-and-back-office-integration`; outside commerce-platform core |
| 108 | Customer segmentation and marketing automation (email, messaging) with consent | MCP, ERP (crmx connector), RET (ecos) | `19-customer-service-and-notifications` (`35-privacy-and-customer-data` for consent) |

### 2.4 Channels, B2B documents, back office

| # | Capability | Models | Chapter (proposed) |
| --- | --- | --- | --- |
| 109 | Marketplace connector framework with canonical model and versioned adapters | MKT, MCP (chnl), ERP (mkpl), POS (mrkt) | `20-marketplaces-and-channel-integration` (`26-api-contracts-and-versioning`) |
| 110 | Marketplace order import, normalization, routing; shipment and status sync within deadlines | MKT, WMS, SHP, ERP, POS | `20-marketplaces-and-channel-integration` (`13-order-management`) |
| 111 | Marketplace account health (sync errors, rejections, buy box, stock-outs) | MKT, ORM (sell) | `20-marketplaces-and-channel-integration` |
| 112 | Seller onboarding, verification, brand registry, authenticity and listing trust | ORM | `20-marketplaces-and-channel-integration` (`36-commerce-regulation`, `47-case-amazon`) |
| 113 | Sponsored ads, retail media and programmatic audiences; retail media reporting | ORM, MKT (rmed), MCP (adsn) | **GAP** — fits `02-commerce-business-models` (advertising as a revenue line) and `47-case-amazon`; `20-marketplaces-and-channel-integration` for the retail-media dashboard |
| 114 | Trading partner directory and partner requirement profiles (message guidelines) | EDI | `22-edi-and-e-invoicing` |
| 115 | Partner onboarding with test interchanges and parallel run | EDI | `22-edi-and-e-invoicing` |
| 116 | AI-assisted document recognition and mapping proposals with human review | EDI | `22-edi-and-e-invoicing` (`45-ai-and-agentic-commerce`) |
| 117 | Secure transport gateway (AS2, SFTP, TLS, Peppol access point); network interconnects | EDI | `22-edi-and-e-invoicing` |
| 118 | Format translation and mapping (in-house format to EDIFACT/UBL) | EDI, ERP (edig), POS (supi) | `22-edi-and-e-invoicing` |
| 119 | Message validation with plain-language errors; routing; status ledger visible to both parties | EDI | `22-edi-and-e-invoicing` (`25-events-consistency-and-reconciliation`) |
| 120 | Order / order response documents (ORDERS, ORDRSP) normalized for the supplier ERP | EDI, ERP | `22-edi-and-e-invoicing` (`39-journey-wholesale-order`) |
| 121 | Despatch advice (DESADV / ASN) and SSCC pallet labels | EDI, POS (supi) | `22-edi-and-e-invoicing` (`15-warehouse-and-fulfillment`) |
| 122 | E-invoicing: EDIFACT INVOIC, EN 16931 formats, Peppol; country mandates as configuration | EDI, ERP (acct e-invoice connector), POS | `22-edi-and-e-invoicing` (`14-tax-invoicing-and-ledger`, `36-commerce-regulation`) |
| 123 | Document archive for audit and retrieval | EDI, SHP (docs) | `22-edi-and-e-invoicing` (`36-commerce-regulation`) |
| 124 | Vendor managed inventory from retailer sales, stock and forecast messages | EDI | **GAP** — fits `22-edi-and-e-invoicing` (collaboration documents) with a cross-link from `10-inventory-and-availability`; add as a sidebar |
| 125 | Web EDI portal for suppliers without an ERP link | EDI | `22-edi-and-e-invoicing` |
| 126 | Punchout / large-account EDI ordering as a channel into order management | B2B (stressor), EDI | `21-b2b-commerce` (`22-edi-and-e-invoicing`) |
| 127 | ERP / back-office connectors; order export; master-data sync; file-based exchange | B2B, MKT, SHP, RET, EDI, ERP, POS | `23-erp-and-back-office-integration` |
| 128 | Data migration and onboarding tooling (items, relations, stock, open items with validation) | ERP, POS, WMS (fpor import) | `42-replatforming-and-migration` |
| 129 | Workflow automation on commerce events (no-code triggers and actions) | MCP (extn), ERP (wflw), RET (auto), WMS (rule) | `31-extensibility-and-app-ecosystems` |

### 2.5 Integration, platform, trust, data

| # | Capability | Models | Chapter (proposed) |
| --- | --- | --- | --- |
| 130 | Public REST/GraphQL API with auth, throttling, versioning; developer portal | MCP, ORM, MKT, SHP, WMS, RET, EDI, ERP, POS | `26-api-contracts-and-versioning` |
| 131 | Webhooks and webhook subscription/delivery | MCP, MKT, SHP, WMS, RET, EDI, ERP | `24-integration-styles` (`25-events-consistency-and-reconciliation`) |
| 132 | Integration runtime: shared job queue, retries, rate-limit governance, event log, monitoring | MKT, SHP, WMS, EDI, RET, POS (intg) | `24-integration-styles` (`33-peak-load-and-reliability`) |
| 133 | Connector registry / connection configuration with credential vault | MKT, SHP, WMS, RET, EDI, POS, HUB (hubc) | `24-integration-styles` (`34-commerce-security`) |
| 134 | Event streams / event bus for orders, stock, returns, tracking | MCP, ORM, RET, SHP, WMS, ERP, POS, HUB | `25-events-consistency-and-reconciliation` |
| 135 | Embedded / white-label partner integrations and partner tenants | MKT, SHP, WMS (fpor) | `31-extensibility-and-app-ecosystems` (`30-multi-tenancy-and-isolation`) |
| 136 | App store, app review, partner program, development stores | MCP, MKT | `31-extensibility-and-app-ecosystems` |
| 137 | Sandboxed extensions and server functions (checkout, admin, POS) | MCP | `31-extensibility-and-app-ecosystems` (`11-cart-and-checkout`) |
| 138 | Building-block library and package entitlements deciding what a shop may use | B2B, MKT (tnnt), WMS (subs) | `31-extensibility-and-app-ecosystems` (`30-multi-tenancy-and-isolation`) |
| 139 | Multi-tenant accounts: tenants, administrations, branches, shops, warehouses, clients, sub-accounts | all | `30-multi-tenancy-and-isolation` |
| 140 | Identity and access: staff accounts, roles, permissions, OAuth scopes, API keys, audit of changes | all | `34-commerce-security` (`27-identity-and-master-data`) |
| 141 | Shopper / buyer identity, account graph, household and entitlements | MCP (shpy), ORM (iden) | `27-identity-and-master-data` (`35-privacy-and-customer-data`) |
| 142 | Consent records and data-sharing policies for third-party apps | ORM, MCP (mktg, stressor) | `35-privacy-and-customer-data` |
| 143 | Security assurance: ISMS, pentests, incident levels, replicated data centers, NIS2 evidence packs | EDI, B2B (host) | `34-commerce-security` (`36-commerce-regulation`) |
| 144 | Test environments, release management, automated QA (nightly, screenshot, vulnerability) | B2B | `44-organizing-commerce-engineering` (`33-peak-load-and-reliability`) |
| 145 | Hosting, patching, backups, dedicated hosting option | B2B | `29-commerce-architecture-styles` (`30-multi-tenancy-and-isolation`) |
| 146 | Commerce analytics and reporting; query layer; dashboards | MCP, ORM, B2B, MKT, ERP, POS, SHP, WMS, RET, EDI | `28-commerce-data-and-analytics` |
| 147 | Experimentation, attribution and incrementality measurement | ORM, MCP (anly) | `28-commerce-data-and-analytics` |
| 148 | Cross-merchant benchmarking from anonymized aggregates | RET | `28-commerce-data-and-analytics` (`35-privacy-and-customer-data`) |
| 149 | Chain KPIs across a multi-product stack (order-to-delivery time, margin after fees, return rate) | HUB (hubv) | `28-commerce-data-and-analytics` (`03-commerce-capability-map`) |
| 150 | Admin AI assistant that answers over store data and takes approved actions | MCP (sdkk), RET (auto) | `45-ai-and-agentic-commerce` |
| 151 | Collaboration on operational records (comments, tasks, photos, inbox) | WMS | **GAP** — minor; fits `15-warehouse-and-fulfillment` as a note on "the WMS as the floor's shared workspace"; otherwise omit |
| 152 | Implementation, onboarding and support desk as a product capability | B2B, RET, EDI, MKT, POS, ERP, WMS | `41-build-buy-or-assemble` (`44-organizing-commerce-engineering`) |

**Count:** 152 distinct capabilities; 11 flagged GAP (#18 reviews and Q&A, #30 membership programs, #50 merchant capital, #85 CO2 reporting, #86 own-fleet routing, #94 repair and workshop, #107 CRM pipeline, #113 retail media and ads, #124 vendor managed inventory, #151 collaboration, and partially #90 fiscal receipts whose regulatory side needs a home in `36-commerce-regulation`).

**Top gaps by weight for the book's reader:** retail media / advertising as a commerce revenue line (ORM, MKT, MCP all model it; no chapter owns it) · membership and paid loyalty programs · reviews, ratings and Q&A as discovery and trust data · vendor managed inventory and collaboration documents beyond ORDERS/DESADV/INVOIC · CO2 and sustainability reporting on deliveries · fiscalization of receipts (regulatory side).

---

## 3. Data assets per model and chapter ownership

Names only, grouped as the models group them. "Owner" is the chapter that should define the entity (PLAN "Owns"); other chapters link to it.

### 3.1 Data assets by model

| Model | Group | Assets |
| --- | --- | --- |
| MCP | Merchant, Account and Ecosystem | Merchant Account; Staff and Permissions; App Installations and Grants; Merchant KYC Profile |
| MCP | Catalog, Content and Market | Product Catalog; Inventory Levels; Theme and Storefront Content; Global Product Catalog Index; Price Lists and Markets; B2B Company Accounts |
| MCP | Orders, Customers and Shopper | Order Ledger; Merchant Customer Records; Fulfillment and Tracking Events; Return Records; Shopper Identity; Storefront Behavioral Events |
| MCP | Money, Risk and Compliance | Payment Transactions; Card Vault Tokens; Merchant Balance and Payouts; Platform Invoices; Risk Signals and Scores; Disputes and Chargebacks; Capital Offers and Repayments; Tax Liabilities |
| MCP | Intelligence and AI | Commerce Analytics Models; Marketing Audiences and Campaigns; Assistant Conversations |
| ORM | People, Accounts and Access | Customer Profile; Customer Contact Point; Identity Credential; Consent Record; Seller Identity & Onboarding; Session Token; Brand Protection & Registry |
| ORM | Commercial and Financial | Payment Instrument Reference; Transaction; Seller Payout Ledger; Ad Campaign; Retail Media Attribution |
| ORM | Product, Catalog and Content | Catalog Authoring & Content; Reviews, Ratings & Q&A |
| ORM | Operational Workflow and Event | Checkout & Payments; Delivery Promise; Order Management & Tracking; Returns, Refunds & Exchanges; Fulfillment Event |
| ORM | Risk, Governance, Security, Compliance | Audit Log; Access Policy; Trust Case; Enforcement Appeal |
| ORM | Core Domain Records | Search, Browse & Facets; Inventory Position; Seller Account Health |
| B2B | Commerce Transaction | Sales Order; Quote; Shopping Cart; Payment Transaction; Shipment; Withdrawal Request; Loyalty Points Ledger |
| B2B | Customer and Access | Business Customer Account; Buyer Contact; Back-Office User; Customer Price Agreement |
| B2B | Catalogue, Content and Configuration | Product Catalogue; Stock Availability; Web Content; Shop Configuration; Integration Mapping |
| B2B | Operations and Insight | Release and Test Record; Platform Backup; Support Request; Commerce Analytics |
| RET | Operational Return | Merchant Account and Branding Configuration; Return Policy Ruleset; Integration Connections and Credentials; Carrier Contracts; Order Snapshot; Product Catalog and Stock Snapshot; Shopper Contact; Return Request; Return Evidence and Photos; Return Shipment and Label; Inspection Result; Exchange Order; Store Credit Ledger; Refund and Return Fee Transaction |
| RET | Analytical Return | Return Event Stream; Return Analytics Mart; Return Benchmark Aggregate |
| EDI | Network and Configuration | Trading Partner Profile; Partner Message Specification; Partner Connection; Mapping Definition; ERP Integration Configuration; Transport Credential |
| EDI | Business Document | EDI Interchange; Purchase Order Document; Despatch Advice Document; SSCC Label Record; Invoice Document; Inventory and Forecast Report; Message Status Event; Message Exception; Document Archive Record; Message Volume Metric; AI Mapping Training Sample |
| EDI | Customer and Platform | Customer Subscription; User Account; Support Ticket; Security Audit Log |
| HUB | Commerce Master | Product and Assortment; Price and Trade Agreement; Business Customer and Trading Partner; Stock Position |
| HUB | Orders, Shipments and Returns | Customer Order; Recipient Contact and Address; Shipment and Tracking; Return and Exchange |
| HUB | Trade Documents and Money | Trade Document (EDI); Invoice, Payment and Refund; Logistics Cost and Service Billing |
| HUB | Hub Connectivity and Shared Customer | Platform Connection and Credential; Cross-Platform Event; Shared Customer Account; Commerce Chain KPI |
| MKT | Catalogue and Content | Product Catalogue Record; Product Selection; Marketplace Category Schema; Channel Listing; Content Rule Set; Translated Content |
| MKT | Pricing and Market | Price Rule Set; Offer Price History; Competitor Offer Snapshot; Feed Export Definition |
| MKT | Order and Fulfilment | Marketplace Order; Shipment and Status Update; Stock Position; Fulfilment Replenishment Plan |
| MKT | Account, Integration and Insight | Merchant Account and Subscription; Channel Connection; Partner Tenant; User Account; Integration Event Log; Sales Performance Metrics; Retail Media Campaign Performance |
| ERP | Catalog and Content | Product Master; Supplier Article Feed; Price Agreements and Price Lists; Webshop Content; Channel Mapping |
| ERP | Customer and Order | Customer Account; Sales Lead and Opportunity; Quote; Sales Order; Sales Invoice and Credit Note; Payment Transaction; POS Receipt and Session; Return Request; EDI Message |
| ERP | Supply Chain | Stock Level; Stock Movement; Warehouse Location; Pick List; Purchase Order; Shipment; Delivery Route |
| ERP | Finance and Platform | General Ledger; Receivables and Payables; Business Metrics; Users and Permissions; Integration Subscription; Migration Batch; Workflow Definition |
| POS | Merchandise | Article and Assortment Master; Prices and Promotions; Branch Formula Rules; Supplier Catalogue; Purchase Orders and Receipts |
| POS | Inventory | Stock Position; Stock Movements; Serialised Item Register |
| POS | Sales and Payment | Sales Transactions; Payment Records; Cashbook and Day Closings |
| POS | Customer | Customer Records; Loyalty Accounts and Vouchers; Quotes, Customer Orders and Reservations; Invoices and Receivables; Repair Orders |
| POS | Omnichannel | Online Orders; Marketplace Offers; Shipments and Returns |
| POS | Insight and Platform | Sales and Stock KPIs; Accounting Journal Export; Tenant and Store Configuration; Users and Roles; Support Tickets |
| SHP | Orders, Recipients and Shipments | Shipping Order; Recipient Contact and Address; Customs and Dangerous-Goods Data; Stock Availability Snapshot; Shipment Record; Shipping Label and Transport Document; Tracking Event; Return Request |
| SHP | Commercial and Carrier | Carrier Service Catalogue; Carrier Performance Metrics; Carrier Rate Card and Contract; Transport Cost Ledger; Carrier Invoice Line; Emission Estimate; Delivery Option Quote |
| SHP | Configuration and Access | Shipping Rule Set; Notification Template and Branding; Integration Connection Configuration; Tenant Account and Credentials |
| WMS | Orders, Customers and Shipments | Sales Order; Customer and Delivery Address; Picklist and Batch; Shipment Record; Shipping Label and Packing Slip; Packaging Usage; Return Record |
| WMS | Products, Stock and Purchasing | Product Master; Stock Ledger; Warehouse and Location; Stock Count; Batch and Best-Before Lot; Supplier; Purchase Order; Goods Receipt |
| WMS | Fulfilment, Collaboration and Insight | Fulfilment Client Account; Fulfilment Rate Card and Invoice Line; Comment and Task; Warehouse Activity Log |
| WMS | Configuration and Access | Integration Connection Config; API Key and Webhook Subscription; Automation Rule Set; Hardware Device Registry; User Account and Rights; Subscription and Order Usage |

### 3.2 Chapter ownership of data entities (deduplicated)

| Entity family (as it appears across models) | Owner chapter | Notes for the glossary and the systems-of-record chapter |
| --- | --- | --- |
| Product / Article Master, Product Catalogue, Supplier Article Feed, Catalog Authoring, Translated Content, Media | `06-product-information` | The PIM question: one master feeding every channel (ERP, POS, WMS, MKT all keep a copy; `04-boundaries-and-systems-of-record` decides which is the record) |
| Price Lists, Price Agreements, Price Rule Set, Offer Price History, Markets | `07-pricing-architecture` | Customer-specific agreements belong to pricing, not to the customer record |
| Promotions, Loyalty Points Ledger, Loyalty Accounts and Vouchers, Store Credit Ledger, Gift Cards | `08-promotions-and-loyalty` | Store credit is a liability; cross-link `14-tax-invoicing-and-ledger` |
| Search Index, Product Selection, Marketing Audiences, Recommendation models | `09-search-and-discovery` | Derived data, rebuildable from the masters |
| Inventory Levels / Stock Position / Stock Ledger / Stock Movement, Stock Availability Snapshot, Serialised Item Register, Batch and Best-Before Lot, Stock Count, Inventory Position | `10-inventory-and-availability` | Ledger vs snapshot distinction; WMS holds the ledger, channels hold snapshots |
| Shopping Cart, Checkout Session, Delivery Option Quote, Address | `11-cart-and-checkout` | Short-lived; the quote is a promise with an expiry |
| Payment Transaction, Payment Instrument Reference, Card Vault Tokens, Risk Signals and Scores, Disputes and Chargebacks, Payment Records (POS tenders) | `12-payments` | Tokens never leave the vault; the order stores a reference |
| Sales Order / Customer Order / Order Ledger / Marketplace Order / Online Orders / Shipping Order (as the order copy), Quote, Fulfillment and Tracking Events, Return Request (link) | `13-order-management` | Many copies, one record; `25-events-consistency-and-reconciliation` owns the copies' consistency |
| Sales Invoice and Credit Note, Invoices and Receivables, General Ledger, Receivables and Payables, Tax Liabilities, Merchant Balance and Payouts, Seller Payout Ledger, Platform Invoices, Cashbook and Day Closings, Accounting Journal Export, Transport Cost Ledger, Fulfilment Rate Card and Invoice Line, Logistics Cost and Service Billing, Carrier Invoice Line | `14-tax-invoicing-and-ledger` | The money side; POS cash and 3PL service billing are the same pattern at different altitudes |
| Warehouse and Location, Picklist and Batch, Goods Receipt, Purchase Order, Supplier, Packaging Usage, Hardware Device Registry, Warehouse Activity Log, Fulfilment Client Account | `15-warehouse-and-fulfillment` | Purchase orders are shared with `23-erp-and-back-office-integration` |
| Shipment Record, Shipping Label and Transport Document, Tracking Event, Carrier Service Catalogue, Carrier Rate Card and Contract, Carrier Performance Metrics, Customs and Dangerous-Goods Data, Emission Estimate, Delivery Route, Delivery Promise | `16-shipping-and-delivery` | Tracking Event is the canonical example of a normalized external event |
| Sales Transactions (POS), POS Receipt and Session, Branch Formula Rules, Tenant and Store Configuration (branches), Repair Orders, Quotes/Customer Orders/Reservations (store) | `17-stores-and-omnichannel` | Receipts are fiscal documents; link `36-commerce-regulation` |
| Return Request, Return Evidence and Photos, Return Shipment and Label, Inspection Result, Exchange Order, Refund and Return Fee Transaction, Return Policy Ruleset, Withdrawal Request, Return Record, Return Analytics Mart, Return Benchmark Aggregate | `18-returns-and-exchanges` | Disposition is a field on the inspection result |
| Notification Template and Branding, Support Request / Support Ticket, Trust Case, Enforcement Appeal, Comment and Task | `19-customer-service-and-notifications` | Cases are cross-party; appeals need an audit trail |
| Channel Listing, Marketplace Category Schema, Content Rule Set, Marketplace Offers, Channel Connection, Channel Mapping, Competitor Offer Snapshot, Seller Account Health, Fulfilment Replenishment Plan, Retail Media Campaign Performance, Ad Campaign, Retail Media Attribution | `20-marketplaces-and-channel-integration` | The listing is a projection of the product plus the offer |
| Business Customer Account, Buyer Contact, B2B Company Accounts, Customer Price Agreement (link), Sales Lead and Opportunity | `21-b2b-commerce` | The company-buyer-contact hierarchy |
| EDI Interchange, Purchase Order Document, Despatch Advice Document, SSCC Label Record, Invoice Document (structured), Inventory and Forecast Report, Message Status Event, Message Exception, Document Archive Record, Trading Partner Profile, Partner Message Specification, Partner Connection, Mapping Definition, Trade Document | `22-edi-and-e-invoicing` | Documents are immutable once sent; status lives in a ledger |
| ERP Integration Configuration, Integration Mapping, Supplier Catalogue, Migration Batch | `23-erp-and-back-office-integration` | Mappings as data is the chapter's central idea |
| Integration Connections and Credentials, Integration Connection Config(uration), Connector/Connection Registry, Platform Connection and Credential, Integration Event Log, Transport Credential, API Key and Webhook Subscription | `24-integration-styles` | Credentials go to `34-commerce-security` |
| Cross-Platform Event, Return Event Stream, Order Events, Fulfillment Event, Audit Log (as event) | `25-events-consistency-and-reconciliation` | Idempotency keys and event ordering |
| Customer Profile, Customer Contact Point, Merchant Customer Records, Customer Records (POS), Shopper Identity, Shopper Contact, Recipient Contact and Address, Shared Customer Account, Identity Credential, Session Token, Users and Permissions, User Account and Rights, Staff and Permissions, Access Policy, Business Customer and Trading Partner (master) | `27-identity-and-master-data` | The Familiar Stranger lives here |
| Commerce Analytics (models, marts, Sales Performance Metrics, Business Metrics, Sales and Stock KPIs, Commerce Chain KPI, Message Volume Metric, Storefront Behavioral Events) | `28-commerce-data-and-analytics` | Derived; must be rebuildable |
| Merchant Account (and Branding Configuration), Shop Configuration, Tenant Account and Credentials, Partner Tenant, Customer Subscription, Subscription and Order Usage, Merchant Account and Subscription, Package entitlements | `30-multi-tenancy-and-isolation` | Entitlements and metering are tenant data |
| App Installations and Grants, Automation Rule Set, Workflow Definition, Shipping Rule Set, Theme and Storefront Content (as extension data), Building-Block Registry | `31-extensibility-and-app-ecosystems` | Rules and workflows as data, versioned |
| Theme and Storefront Content, Web Content, Webshop Content | `32-storefront-architecture` | Content vs catalog boundary |
| Consent Record, Assistant Conversations, Marketing Audiences and Campaigns (personal data aspects), Return Benchmark Aggregate (anonymization) | `35-privacy-and-customer-data` | Retention and anonymization |
| Merchant KYC Profile, Security Audit Log, Seller Identity & Onboarding, Brand Protection & Registry | `34-commerce-security` / `36-commerce-regulation` | Split: security owns credentials and audit; regulation owns KYC, brand and product-safety obligations |
| Capital Offers and Repayments, Platform Invoices, Partner revenue share | `02-commerce-business-models` | Platform economics, not architecture |
| Release and Test Record, Platform Backup | `44-organizing-commerce-engineering` / `33-peak-load-and-reliability` | Operational evidence |

---

## 4. Personas and customers across models

One row per modeled customer (the models' "customers.json"). Useful for the business-first opening of each chapter: who loses money or trust, and what they want. These are modeled archetypes, not real people or real accounts.

| Model | Group | Role | What they want (model's "care about", condensed) |
| --- | --- | --- | --- |
| MCP | Merchants | Independent Brand Founder | Launch a credible store without a developer; low predictable fixed cost; get paid fast and see cash clearly |
| MCP | Merchants | Scaling DTC Brand Ecommerce Lead | Checkout conversion and site speed on peak days; new countries without separate stores and teams; profitable acquisition |
| MCP | Merchants | Enterprise Omnichannel Retail Director | One view of inventory, customers and orders across stores, web and wholesale; store-floor uptime; ERP/WMS/finance integration |
| MCP | Shoppers | Repeat Mobile Shopper | Pay in one tap without retyping; trust an unfamiliar brand; know where every order is |
| MCP | Ecosystem Partners | Commerce App Developer and Agency Partner | Stable, documented APIs and predictable deprecations; discovery by the right merchants; billing without building payments |
| ORM | Demand-Side Consumers | Prime Household Shopper | Find relevant products fast; trust price, quality and reviews; delivery speed that matches urgency |
| ORM | Supply-Side Merchants | Marketplace Seller / Brand Operator | Accurate, quickly approved listings; traffic and buyability on priority items; availability without excess storage or working capital |
| ORM | Retail Media Advertisers | Performance Brand Marketer | Capture high-intent shoppers; protect branded traffic; know whether spend is incremental |
| ORM | Operations and Trust | Marketplace Trust & Compliance Operator | Catch fraud, counterfeit and abuse before reports; seller verification that meets regulation; fast, explainable, appeal-proof enforcement |
| ORM | Operations and Trust | Fulfillment & Customer Resolution Operator | See at-risk promises early; rare promise exceptions during peak and weather; resolve honest claims in one contact at low cost |
| B2B | Trading Company Leadership | Wholesale Owner-Director | More trade orders without more order-desk staff; no rebuild in three years; predictable monthly cost |
| B2B | Webshop Operators | E-commerce and Marketing Manager | Publish pages and campaigns same day without a ticket; fast pages and rankings; clean product data across shop, feeds, marketplaces |
| B2B | Webshop Operators | ERP and Operations Lead | Stock and prices identical in ERP and shop; orders arrive in the ERP without retyping; changes tested before go-live |
| B2B | Online Buyers | Professional Trade Buyer | My prices and my assortment; fast reorder of the usual items; know it is in stock and when it arrives |
| B2B | Online Buyers | Consumer Shopper | Trustworthy shop and payment; clear stock and delivery time; easy returns within the legal 14 days |
| RET | Merchant Leadership | E-commerce Director (fashion/lifestyle) | Contribution margin after returns; keep revenue when items come back; a return experience that does not hurt conversion |
| RET | Merchant Teams | E-commerce and Merchandising Analyst | Which SKUs and reasons drive returns; fit vs quality vs expectation; benchmarks |
| RET | Merchant Teams | Customer Service Lead | Fewer return tickets; full return context in the helpdesk; a status the team can quote |
| RET | Merchant Teams | Returns and Warehouse Operations Lead | Know what is coming back before it arrives; fast restocking; fair decisions on damaged and warranty items |
| RET | Shoppers | Online Shopper Returning an Item | The right size quickly; know when the refund arrives; no label printing or fees |
| RET | Logistics Partners | Fulfilment and 3PL Partner Manager | Returns arrive with client data attached; reliable integration for many clients; clear resolution instructions |
| EDI | Suppliers to Retail | Supplier Order Desk and Logistics Lead | Every order in the ERP without retyping; deliveries accepted at the dock; not learning each retailer's EDI rules |
| EDI | Suppliers to Retail | Supplier Finance and AR Manager | Invoices accepted first time; cash on time; e-invoicing compliance in every country |
| EDI | Retailers and Buying Organisations | Retail Supplier Onboarding and Supply Chain Manager | Share of suppliers trading digitally; advance notice of every delivery; invoices matching orders and receipts |
| EDI | IT and Integration | IT and ERP Manager at a Trading Company | Integrations that run without daily attention; no in-house EDI know-how; migrations without breaking partner flows |
| EDI | IT and Integration | ERP Implementation Partner | Projects on time; a complete offer including EDI; recurring revenue |
| HUB | Trading Companies | Trading Company Owner-Director | Growth without growing the back office; one reliable chain from order to delivery; no in-house IT team needed |
| HUB | Trading Companies | E-commerce and Channel Manager | Conversion and buy-box share; content correct everywhere; delivery options and returns that sell |
| HUB | Trading Companies | Warehouse and Logistics Operations Lead | Ship complete and on time at peak; stock true in every system; fast accurate returns |
| HUB | Trading Companies | IT, ERP and Integration Lead | Few, stable integrations; security and compliance evidence; changes without breaking the live chain |
| HUB | Trading Companies | Financial Controller | Month close without reconciliation; invoices paid first time; true cost per order |
| HUB | Trading Companies | Platform-Based Merchant (keeps the SaaS shop as the record) | Keep the shop platform as the center; apps that install in minutes and keep working; marketplaces without a second backend |
| HUB | Specialty Retailers | Specialty Retailer and Store Chain Manager | Store margin and stock control; online without a second administration; fast counter service |
| HUB | Suppliers and Brands | Supplier and Brand Selling to Retail | Every retailer order processed without entry; deliveries accepted at the DC; consistent brand content and price |
| HUB | Logistics Service Providers | Fulfilment and 3PL Company | Fast client onboarding; billing every service; clients who self-serve |
| HUB | Logistics Service Providers | Webshop Brand Outsourcing Fulfilment | Visibility of stock and orders at the 3PL; same-day shipping; return handling they control |
| HUB | Ecosystem Partners | Software and Implementation Partner | Not building fifty integrations; stable APIs and partner support; revenue share or margin |
| HUB | Buyers and Recipients | Online and In-Store Shopper | Delivery when and where it suits; easy returns and exchanges; correct stock information |
| HUB | Buyers and Recipients | Professional Trade Buyer | Agreed prices and assortments; fast reorder; delivery certainty |
| MKT | Marketplace Merchants | Multichannel Merchant Owner | Marketplace revenue profitable after commission and shipping; no extra staff per marketplace; a partner who answers when a marketplace changes something |
| MKT | Marketplace Merchants | Marketplace and E-commerce Manager | Whole assortment live without hundreds of rejected listings; win the buy box without racing to the bottom; bulk editing |
| MKT | Marketplace Merchants | Order and Fulfilment Operations Lead | Orders in the WMS without retyping; track-and-trace to the marketplace on time; multi-warehouse stock shown correctly |
| MKT | Brands and Manufacturers | Brand E-commerce and Retail Media Manager | One view of retail media spend across retailers; consistent content and recommended prices; hold the buy box against resellers |
| MKT | Merchant IT | IT Manager and Integration Lead | One stable documented API instead of one per marketplace; predictable behavior under peak and rate limits; clear errors and monitoring |
| MKT | Software Partners | Embedded SaaS Partner Product Manager | Offer many marketplaces without building each API; customers authenticate inside our product; one uniform order and shipment format |
| ERP | Trading Company Leadership | Trading Company Owner | Margin per channel; grow without more back-office staff; one reliable system instead of a patchwork |
| ERP | Commerce and Sales | E-commerce Manager | Correct stock and prices on every channel; fast findable product pages; campaigns without developers |
| ERP | Commerce and Sales | B2B Sales and Account Manager | Quote the right net price immediately; stock and delivery date while on the phone; accounts reorder without chasing |
| ERP | Operations | Warehouse and Logistics Lead | Pick lists that never send the same order twice; know where an item is; labels without typing addresses |
| ERP | Operations | Purchaser and Product Data Manager | Availability of fast movers; cash not stuck in slow stock; supplier price changes reflected immediately |
| ERP | Stores and Finance | Branch and Store Manager | Correct prices at the register; serve customers with stock from other branches; quick cash-up |
| ERP | Stores and Finance | Financial Administrator | Books that reflect operations without retyping; receivables collected on time; reliable VAT |
| POS | Retail Entrepreneurs | Independent Specialty Retailer Owner | Margin and stock value; time on the shop floor instead of admin; trade-specific functions |
| POS | Retail Entrepreneurs | Multi-Store Retail Operations Manager | Same data in every branch; stock in the right branch; comparable branch performance |
| POS | Formulas and RSOs | Franchise or Retail Service Organisation Manager | Formula consistency; joint purchasing power; entrepreneurs independent but aligned |
| POS | Store Teams | Sales Associate at the Counter | A till that does not make them look slow; know if an item is in stock elsewhere; no cash or price errors |
| POS | Store Teams | Workshop and Repair Technician | A clear plan for the day; parts available; customers informed without calls |
| POS | Back Office | Purchasing and E-commerce Coordinator | Article data correct everywhere; fewer manual imports; listings that do not oversell |
| POS | Shoppers | Specialty-Store Shopper | Know the item is available before traveling; expert advice; easy repairs and returns |
| POS | Supply Partners | Brand Supplier or Wholesaler | Correct article data at the retailer; electronic orders without retyping; sell-out insight |
| SHP | Merchants and Shippers | E-commerce Operations Manager | Keep the promise made at checkout; cost per parcel as tariffs rise; peak without extra temps |
| SHP | Merchants and Shippers | Logistics Manager at a Manufacturer or Wholesaler | Customer-specific delivery agreements; correct export and ADR documents; transport cost known before the invoice |
| SHP | Logistics Service Providers | Fulfilment and 3PL Operations Lead | Throughput at pack stations; fast client onboarding; margin on re-invoiced shipping |
| SHP | Logistics Service Providers | Carrier or Transport Broker Partner | Clean pre-announced shipment data; reach into shippers' systems; margin per shipment |
| SHP | Software Partners | Software Integration Partner | Not maintaining hundreds of carrier connections; shipping features that win deals; short joint implementations |
| SHP | Recipients | Online Shopper and Parcel Recipient | Know when the parcel arrives; choose a moment or pickup point; low or no shipping cost |
| WMS | Online Stores with Own Warehouse | Webshop Owner Running Their Own Warehouse | Ship every order on the promised day; true stock so the shop never oversells; time for buying and marketing |
| WMS | Online Stores with Own Warehouse | Warehouse Manager at a Scaling Brand or Wholesaler | Hit carrier cut-offs at peak with a partly temporary team; throughput and walking distance; accurate stock across locations |
| WMS | Fulfilment Companies | Fulfilment (3PL) Company Owner or Operations Lead | Onboard a client in days; one workflow for all clients with separate data; charge every pick, box and pallet |
| WMS | Fulfilment Companies | Webshop Brand Outsourcing to a 3PL | Real stock and order status without calling the 3PL; never sell stock that is not there; which batch went to which customer |
| WMS | Warehouse Floor | Order Picker and Packer | Know exactly where to go and what to take; not blamed for mistakes; less walking and paper |
| WMS | Ecosystem Partners | Integration, Hardware and Commerce Hub Partner | Stable documented API with webhooks; listed on the integrations page; shared customers who stay |

**Recurring persona clusters the book can reuse (mapped to the Kestrel & Pine cast by role, never by name):** owner/director who wants growth without back-office headcount (B2B, ERP, HUB, POS, WMS) · e-commerce/channel manager who wants content correct everywhere and no rejected listings (B2B, ERP, HUB, MKT, POS) · operations/warehouse lead who wants stock true in every system and cut-offs met at peak (HUB, ERP, MKT, SHP, WMS, RET) · IT/integration lead who wants few stable integrations and changes that do not break the live chain (B2B, EDI, HUB, MKT) · finance who wants month close without reconciliation (EDI, ERP, HUB) · trade buyer who wants their prices and fast reorder (B2B, HUB) · shopper/recipient who wants one-tap payment, honest stock, a delivery moment and easy returns (MCP, ORM, RET, SHP, HUB, POS) · software/implementation partner who wants one API instead of fifty (MCP, MKT, SHP, WMS, EDI, HUB).

---

## 5. Residuality notes mapped to the book's failure patterns

Each model carries a residuality stress test (after O'Reilly's *Residues*): a naive architecture, a set of business-context stressors ("what could change"), the attractor each stressor pulls the business toward, and the residue (the structural change that survives). Below, each model's stressors are listed and mapped to the sixteen failure patterns in `style-guide.md` where they fit. Stressors concerning group ownership, consolidation, acquisitions or group targets are **omitted** for the Katapull models, as the header requires. Regulatory dates quoted by the models are the models' claims and must be re-verified in a brief before a chapter uses them.

**Pattern key:** Phantom Stock · Schrödinger's Order · Familiar Stranger · Boomerang · Price Nobody Can Explain · Spaghetti Junction · Message in a Bottle · Pulled Rug · First Snowfall · Giant's Boots · Burned Bridge · Forked Platform · One Size Fits None · Lynchpin · Long Fuse · Secret Agent.

### MCP — merchant-commerce-platform

- *Naive:* one hosted storefront per merchant, carts to a single checkout tied to one payment processor, orders read by apps through broad API scopes. *Residual:* catalog, checkout rules, buyer identity and order record as surface-independent contracts; payment routes, duties and data-sharing as effective-dated configuration; apps act through scoped extensions.
- **AI assistants become where shoppers start and finish purchases** → checkout and identity become protocol endpoints; the storefront is one client among many. Patterns: **Secret Agent** (agents acting on orders need identity and approval), **Giant's Boots** (copying agentic architecture before demand exists). Chapters: `45-ai-and-agentic-commerce`, `11-cart-and-checkout`.
- **Primary payment partner relationship changes or a market requires local licensing** → payment routes and processors are configuration behind the payments API; the merchant ledger is the source of truth independent of processor references. Patterns: **Lynchpin**, **Pulled Rug**. Chapters: `12-payments`, `14-tax-invoicing-and-ledger`.
- **A major import market removes its low-value duty exemption** → duties, customs data and market pricing are effective-dated rules resolved at checkout per destination. Patterns: **Long Fuse**, **Price Nobody Can Explain**. Chapters: `14-tax-invoicing-and-ledger`, `36-commerce-regulation`.
- **Regulators restrict sharing shopper data with third-party apps** → partner capabilities run as extensions close to the data with minimal audited scopes. Patterns: **Secret Agent**, **Long Fuse**. Chapters: `35-privacy-and-customer-data`, `31-extensibility-and-app-ecosystems`.

### ORM — online-retail-marketplace

- *Naive:* search, product page, one seller offer, checkout, one fulfillment path; returns after delivery. *Residual:* product page, seller offer, inventory, delivery path, buyer and order managed and versioned separately; humans and agents use the same offer contract; inventory and delivery replannable until confirmation.
- **Personal AI agents become the primary buyers** → a channel-independent offer and purchase-intent contract (buyer, beneficiary, payer, delegate, budget, substitution policy, evidence, expiry explicit). Patterns: **Secret Agent**. Chapters: `45-ai-and-agentic-commerce`, `47-case-amazon`.
- **A regulator requires proven product provenance before an offer is shown** → separate product content from an evidence-bearing seller offer; a policy decision service evaluates seller, product, provenance, jurisdiction, channel and time. Patterns: **Long Fuse**. Chapters: `36-commerce-regulation`, `20-marketplaces-and-channel-integration`.
- **Flooding makes a fulfillment region inaccessible for weeks** → a delivery promise is a versioned fulfillment plan over fungible supply, capacity and routes; the order owns the customer commitment. Patterns: **First Snowfall** (capacity shock), **Schrödinger's Order** (promise vs plan diverge). Chapters: `16-shipping-and-delivery`, `33-peak-load-and-reliability`.
- **A manufacturer recalls one production lot mixed across first- and third-party inventory** → a trace graph from lot through offer, unit, movement, shipment, order and beneficiary; safety actions propagate idempotently. Patterns: **Message in a Bottle** (idempotent propagation), **Phantom Stock** (unit-level identity). Chapters: `10-inventory-and-availability`, `15-warehouse-and-fulfillment`, `36-commerce-regulation`.
- **A creator livestream makes an unfamiliar seller's product the day's largest order burst** → no new structure needed if intent, eligibility and fulfillment plans are already separable. Patterns: **First Snowfall**. Chapters: `33-peak-load-and-reliability`, `40-journey-peak-day`.
- **A competitor subsidizes factory-direct prices below local economics** → an offer is a bundle of item price, landed cost, delivery commitment, provenance, seller terms, service entitlement and resolution promise. Patterns: **Price Nobody Can Explain**. Chapters: `07-pricing-architecture`, `02-commerce-business-models`.

### B2B — b2b-wholesale-ecommerce-platform

- *Naive:* one codebase per customer with point-to-point ERP scripts, prices copied nightly, carriers and payment providers wired into checkout code, quality depending on a small team. *Residual:* shared building-block platform with entitlements; connectors behind a stable integration layer with mappings as data; event-based order and stock exchange; consumer-law features as configurable blocks; automated QA gating every release.
- **A major ERP changes or rate-limits its API** → connector mappings as data with versioned adapters and health monitoring. Patterns: **Pulled Rug**, **Spaghetti Junction**. Chapters: `23-erp-and-back-office-integration`, `26-api-contracts-and-versioning`.
- **Search traffic shifts to AI assistants** → product data published as structured feeds from one catalog. Patterns: **Giant's Boots** (if over-built), **Secret Agent**. Chapters: `45-ai-and-agentic-commerce`, `09-search-and-discovery`.
- **EU consumer rules tighten withdrawal and accessibility** → compliance as configurable building blocks rolled out platform-wide. Patterns: **Long Fuse**, **Forked Platform** (per-customer code cannot be patched at once). Chapters: `36-commerce-regulation`, `30-multi-tenancy-and-isolation`.
- **A payment provider fails during peak season** → provider-agnostic payment layer with multiple active providers. Patterns: **Lynchpin**, **First Snowfall**. Chapters: `12-payments`, `33-peak-load-and-reliability`.
- **Founder-led knowledge leaves the team** → automated tests and documented blocks make the platform team-independent. Patterns: **Lynchpin** (one person). Chapters: `44-organizing-commerce-engineering`.
- **Large trade buyers demand EDI orders** → EDI as another order channel feeding order management. Patterns: **Spaghetti Junction** (if built per buyer). Chapters: `21-b2b-commerce`, `22-edi-and-e-invoicing`, `39-journey-wholesale-order`.
- *(Group-strategy stressor omitted.)*

### RET — ecommerce-returns-management-platform

- *Naive:* a shop app with a return form, a carrier label call, refunds written straight back, a reporting page on the same database. *Residual:* a versioned rules engine shared by portal, gate and automations; return lifecycle as events; one normalized interface per connector category; exchange and credit as first-class resolutions.
- **Shop platforms ship good native returns and exchanges** → value concentrates in rules, operations, integrations and analytics. Patterns: **Giant's Boots** (buying a specialist tool the platform already covers; also `41-build-buy-or-assemble`). Chapters: `18-returns-and-exchanges`, `41-build-buy-or-assemble`.
- **EU bans destruction of unsold textiles and footwear (model cites ESPR; verify)** → inspection results carry a disposition and feed the analytics mart. Patterns: **Long Fuse**, **Boomerang**. Chapters: `18-returns-and-exchanges`, `36-commerce-regulation`.
- **Paid returns become the norm in fashion** → fees are rules in the policy engine, not hard-coded checkout logic. Patterns: **Forked Platform** (fee logic in checkout code). Chapters: `18-returns-and-exchanges`, `08-promotions-and-loyalty`.
- **Return fraud and wardrobing rise** → approval gate and behavior signals reusable by any rule. Patterns: **Boomerang**, **Secret Agent** (automations refunding without review). Chapters: `18-returns-and-exchanges`, `34-commerce-security`.
- **AI agents configure and operate returns** → rules stay versioned and human-approved; agents act through the same APIs as people. Patterns: **Secret Agent**. Chapters: `45-ai-and-agentic-commerce`, `18-returns-and-exchanges`.
- *(Ownership stressor omitted.)*

### EDI — edi-and-b2b-document-exchange-platform

- *Naive:* hand-built mappings per customer and retailer, one transport server, invoices as a special case outside EDI, portal and support tools on one database, security answers per questionnaire. *Residual:* a network registry and profile library feeding one translation and validation engine; e-invoice formats as profiles; AI-proposed mappings with human review; durable queues and a replicated status ledger; one public API for everyone; assurance as a maintained artifact.
- **A country makes sending structured e-invoices mandatory (model cites German 2027–2028 dates; verify)** → e-invoice formats are profiles in the same engine; country mandates become configuration. Patterns: **Long Fuse**. Chapters: `22-edi-and-e-invoicing`, `36-commerce-regulation`, `14-tax-invoicing-and-ledger`.
- **Customers under NIS2 audit their EDI supplier** → assurance evidence is a maintained product artifact. Patterns: **Long Fuse**, **Lynchpin** (the EDI provider as a critical supplier). Chapters: `34-commerce-security`, `36-commerce-regulation`.
- **AI makes partner mapping a commodity** → mappings generated from profiles plus samples and reviewed; the profile library and network remain the asset. Patterns: **Secret Agent** (unreviewed mappings). Chapters: `22-edi-and-e-invoicing`, `45-ai-and-agentic-commerce`.
- **A major retailer moves its suppliers to a competing network** → network interconnects are a first-class transport route. Patterns: **Lynchpin**, **Pulled Rug**. Chapters: `22-edi-and-e-invoicing`, `24-integration-styles`.
- **Primary data center outage during peak ordering** → durable queues and replicated status ledgers resume delivery without loss or duplicates. Patterns: **Message in a Bottle**, **First Snowfall**. Chapters: `25-events-consistency-and-reconciliation`, `33-peak-load-and-reliability`.
- *(Ownership stressor omitted.)*

### HUB — katapull-commerce-hub

- The hub model's residuality section is not authored ("Not authored yet"). Nothing to map. The hub's two foundation bricks (bridges and connection registry; shared customer view) are themselves the residue the specialist models keep converging on: bridges on public contracts rather than private back doors, and one registry of which account uses which product. Patterns the hub shape guards against: **Spaghetti Junction**, **Familiar Stranger** (shared customer registry), **Lynchpin** (one connector per pair). Chapters: `24-integration-styles`, `27-identity-and-master-data`, `49-case-composable-movement`.

### MKT — marketplace-channel-integration-platform

- *Naive:* one hand-built connector per marketplace and per webshop, nightly price and stock batches, credentials stored with settings, one support team fixing merchant-reported failures. *Residual:* a canonical offer, order and shipment model behind versioned adapters; a shared job queue with rate-limit governance and an event log visible to merchants and consultants; rule-based content and pricing per channel; a partner-tenant model; entitlements decoupled from features.
- **A major marketplace replaces its seller API** → versioned adapters behind a stable canonical model; merchants and partners never integrate marketplace APIs directly. Patterns: **Pulled Rug**, **Spaghetti Junction**. Chapters: `20-marketplaces-and-channel-integration`, `26-api-contracts-and-versioning`.
- **A back-office vendor drops its own marketplace connector** → back-office connectors as first-class products with a repeatable migration path. Patterns: **Lynchpin**, **Burned Bridge** (forced switch without a path). Chapters: `23-erp-and-back-office-integration`, `42-replatforming-and-migration`.
- **Regulation demands more product data on marketplaces (manufacturer and responsible-person attributes)** → schema refresh and validation make new mandatory attributes visible before listings fail. Patterns: **Long Fuse**, **Pulled Rug**. Chapters: `06-product-information`, `36-commerce-regulation`, `20-marketplaces-and-channel-integration`.
- **Competitors switch to aggressive fixed or free entry pricing** → entitlements and metering decoupled from features. Patterns: none directly; informs `02-commerce-business-models` and `30-multi-tenancy-and-isolation`.
- **AI shopping agents become a meaningful sales channel** → canonical catalog and offer model reused for any new channel type. Patterns: **Giant's Boots** (new channel as a special case), **Secret Agent**. Chapters: `45-ai-and-agentic-commerce`, `20-marketplaces-and-channel-integration`.
- *(Group-strategy stressor omitted.)*

### ERP — omnichannel-commerce-erp-platform

- *Naive:* one monolithic ERP and webshop per tenant with modules sharing tables, point-to-point integrations per customer, carrier and payment plugins hard-wired into order code, accounting exports by file. *Residual:* one shared commerce core (items, prices, orders, stock, ledger) emitting events; a public API and integration hub with standard bridges; channel, EDI, carrier and returns connectors behind stable contracts; tenant hierarchy of administrations and branches; e-invoicing as a connector of the accounting brick.
- **Structured B2B e-invoicing becomes mandatory (model cites Belgium 2026, ViDA; verify)** → e-invoicing as a connector of accounting, not a separate export. Patterns: **Long Fuse**. Chapters: `22-edi-and-e-invoicing`, `14-tax-invoicing-and-ledger`, `36-commerce-regulation`.
- **Marketplaces take a growing share of online sales** → event-driven stock publication shared by webshop, POS and channels. Patterns: **Phantom Stock**, **Message in a Bottle**. Chapters: `10-inventory-and-availability`, `25-events-consistency-and-reconciliation`, `20-marketplaces-and-channel-integration`.
- **Buyers order through AI agents and conversational interfaces** → public API and structured catalog as first-class channels. Patterns: **Secret Agent**. Chapters: `45-ai-and-agentic-commerce`, `21-b2b-commerce`.
- **Fast-growing customers outgrow the all-in-one package** → composable edges: modules replaceable by specialist products while the core keeps orders and ledger. Patterns: **Burned Bridge** (if replaced all at once), **One Size Fits None**, **Giant's Boots**. Chapters: `43-commerce-scaling-stages`, `42-replatforming-and-migration`, `41-build-buy-or-assemble`, `49-case-composable-movement`.
- *(Ownership stressor omitted.)*

### POS — retail-pos-and-store-management-platform

- *Naive:* a single-tenant desktop till with a cloud database, hand-built point integrations per partner, one package-based license. *Residual:* a channel-agnostic retail core (articles, prices, stock, sales) with an integration gateway, offline-capable clients, pluggable payments and structured documents, so new channels, devices and regulations become connectors rather than rewrites.
- **Marketplaces capture most online demand in specialty categories** → event-driven stock publication to any channel. Patterns: **Phantom Stock**, **Lynchpin** (dependence on marketplace rules). Chapters: `10-inventory-and-availability`, `17-stores-and-omnichannel`, `20-marketplaces-and-channel-integration`.
- **Tap-to-pay on phones replaces dedicated terminals** → tender-agnostic payment API. Patterns: **Pulled Rug** (hardware-bound checkout), **Forked Platform**. Chapters: `17-stores-and-omnichannel`, `12-payments`.
- **Structured e-invoicing becomes mandatory for B2B** → document exchange as a shared service. Patterns: **Long Fuse**. Chapters: `22-edi-and-e-invoicing`, `36-commerce-regulation`.
- **Prolonged internet or cloud outage on a peak Saturday** → offline-capable checkout with idempotent sync. Patterns: **First Snowfall**, **Message in a Bottle** (duplicate sales on resync). Chapters: `17-stores-and-omnichannel`, `33-peak-load-and-reliability`, `25-events-consistency-and-reconciliation`.
- *(Ownership stressor omitted.)*

### SHP — shipping-and-carrier-management-platform

- *Naive:* hard-coded integrations per carrier and per webshop, fixed shipping methods per channel, labels from carrier portals, cost known only from the invoice, tracking emails sent by each carrier. *Residual:* a carrier adapter gateway with a uniform model; versioned rules and selection engines weighing cost, promise, performance and CO2; tracking normalized onto an event bus; expected cost stored at booking for freight audit; multi-client tenancy; bridges and an API.
- **A major carrier changes its API, prices or exits a service at short notice** → carriers interchangeable behind the adapter gateway; rate cards and services are versioned data, not code. Patterns: **Pulled Rug**, **Lynchpin**. Chapters: `16-shipping-and-delivery`, `26-api-contracts-and-versioning`.
- **EU removes the customs-duty exemption for low-value parcels** → customs and dangerous-goods data become first-class article data validated before booking. Patterns: **Long Fuse**. Chapters: `16-shipping-and-delivery`, `06-product-information`, `36-commerce-regulation`.
- **Shippers must report transport emissions with recognized methods** → emission estimates are versioned facts linked to each shipment. Patterns: **Long Fuse**. Chapters: `16-shipping-and-delivery`, `36-commerce-regulation` (see GAP #85).
- **Large shipping platforms consolidate and compete on price** → value sits in decision and control bricks and bridges rather than label generation. Patterns: none directly; informs `41-build-buy-or-assemble` and `05-commerce-platform-landscape`.
- *(Ownership stressor omitted.)*

### WMS — warehouse-management-and-fulfilment-platform

- *Naive:* a single-tenant stock list per webshop with hard-coded imports from one store, printed picklists, labels from carrier portals, stock counted once a year; 3PL clients get spreadsheet exports. *Residual:* a multi-tenant warehouse core with an append-only stock ledger, location model and lot tracking; adapters for stores, carriers, hub siblings and hardware behind stable contracts; an event stream feeding webhooks, reports and billing; rules as data; the same workflows in web, app and portal.
- **A major webshop platform, marketplace or carrier changes its API or terms at short notice** → store and carrier specifics in replaceable adapters; rules switch shipping method without code. Patterns: **Pulled Rug**. Chapters: `15-warehouse-and-fulfillment`, `26-api-contracts-and-versioning`.
- **Warehouse labor becomes scarce and mostly temporary** → knowledge sits in the system (locations, routes, rules, packaging advice) instead of in people. Patterns: **Lynchpin** (one person). Chapters: `15-warehouse-and-fulfillment`, `44-organizing-commerce-engineering`.
- **Peak season brings several times normal volume** → guided work and replaceable adapters make peak a capacity question, not a redesign. Patterns: **First Snowfall**. Chapters: `33-peak-load-and-reliability`, `40-journey-peak-day`.
- **Retailers and regulators demand batch and expiry traceability** → lot is a first-class dimension of the stock ledger. Patterns: **Long Fuse**, **Phantom Stock** (lot-level availability). Chapters: `10-inventory-and-availability`, `15-warehouse-and-fulfillment`, `36-commerce-regulation`.
- **Goods-to-person systems and robots become affordable for mid-size warehouses** → hardware behind adapter contracts; picking tasks device-agnostic. Patterns: **Giant's Boots** (automation copied from giants), **Lynchpin** (one hardware vendor). Chapters: `15-warehouse-and-fulfillment`, `43-commerce-scaling-stages`.
- **Fulfillment companies face margin pressure and must bill every activity** → every warehouse event is billable data via the activity log. Patterns: **Boomerang** (unbilled returns handling). Chapters: `15-warehouse-and-fulfillment`, `14-tax-invoicing-and-ledger`.
- *(Ownership stressor omitted.)*

### 5.1 Failure-pattern coverage check (which patterns the models' stressors reach)

| Pattern | Models whose stressors or residues touch it |
| --- | --- |
| The Phantom Stock | ORM (recall), ERP, POS, WMS (lot) |
| Schrödinger's Order | ORM (promise vs plan) |
| The Familiar Stranger | HUB (shared customer registry) — thin; chapter `27-identity-and-master-data` needs its own material |
| The Boomerang | RET, WMS (unbilled returns) |
| The Price Nobody Can Explain | MCP (duties at checkout), ORM (landed-cost offers) |
| The Spaghetti Junction | B2B, HUB, MKT, (all naive architectures) |
| The Message in a Bottle | ORM (idempotent recall), EDI (durable queues), ERP, POS (offline resync) |
| The Pulled Rug | MCP, B2B, MKT, EDI, POS, SHP, WMS |
| The First Snowfall | ORM, B2B, EDI, POS, WMS |
| The Giant's Boots | MCP, B2B, RET, MKT, ERP, WMS |
| The Burned Bridge | MKT (forced connector switch), ERP (outgrowing the suite) |
| The Forked Platform | B2B, RET, POS |
| One Size Fits None | ERP (all-in-one vs composable edges) |
| The Lynchpin | MCP, B2B, EDI, MKT, POS, SHP, WMS |
| The Long Fuse | MCP, B2B, RET, EDI, MKT, ERP, POS, SHP, WMS (the most frequent stressor family: e-invoicing, customs, product data, traceability, destruction ban, emissions, NIS2, accessibility) |
| The Secret Agent | MCP, ORM, B2B, RET, EDI, MKT, ERP |

**Thin spots the models do not stress (the book must supply its own material):** Schrödinger's Order beyond the marketplace promise case (three systems disagreeing on one order); The Familiar Stranger (customer identity across store and online); The Price Nobody Can Explain in the omnichannel merchant case (channel price drift); The Burned Bridge as a replatforming event; One Size Fits None across brands. The Kestrel & Pine incidents in `scenario-ledger.md` (the Three-Status Order, the Store Stock Mirage, the Price Drift, the Double Refund) cover exactly these.

---

*End of digest. Everything above is a map of eleven inferred models. Nothing in it is evidence about a company.*
