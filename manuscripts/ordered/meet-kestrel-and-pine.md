{id: meet-kestrel-and-pine}
# Meet Kestrel & Pine

![Meet Kestrel & Pine — logo](commerce-platform-architecture/posts/meet-kestrel-and-pine/assets/images/meet-kestrel-and-pine/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Meet Kestrel & Pine, the fictional outdoor brand this book follows, its systems, its people, its 2026 incidents, the Waypoint program and the recurring order every chapter returns to.

> **KEY POINTS:**
>
> * **Kestrel & Pine is a fictional composite, not a disguised company.** It borrows the shape of many growing omnichannel brands so the book can show real tensions with consistent numbers. Every name, price, figure and incident is invented and recorded in one canonical ledger.
> * **Four channels, thirteen systems, no order hub and no product hub.** Orders live in four systems, product data in four, stock in four, and the chain that copies stock between them takes up to two hours. Nearly every incident on this page is that gap, seen from a different side.
> * **Waypoint decides ownership first and buys the hubs second.** The 2027 program names a system of record for stock, orders and product content, adds an availability service, an order management system and a product information system beside the existing platform, and sets integration standards, without replatforming.

This book tests every argument against **one fictional merchant, detailed enough to be realistic and consistent enough to follow across sixty-seven pages.** A toy example is too simple to show why the hard decisions are hard; a real company's internals cannot be verified. So the book invents a merchant, writes its facts down once, and holds every chapter to them. This page is that record in readable form; the failure patterns of [Out of Stock, Out of Sync: Sixteen Ways Commerce Platforms Go Wrong](#where-commerce-platforms-go-wrong) appear here as the incidents Kestrel & Pine lived through.

**Kestrel & Pine is fictional.** It is a composite of *patterns* common among growing brands: a web shop that became a company, stores added later on a separate till system, wholesale customers who want paper-free ordering, marketplaces added for reach, a warehouse of its own, and an integration landscape built one connector at a time. It is **not a portrait of any real brand or retailer.** Its systems are named by role (the platform, the ERP, the WMS), never by vendor, which also keeps the book platform-neutral. Real marketplaces (bol, Amazon.de, Zalando) and carriers (PostNL, bpost, DHL, DPD) appear as channels and services; Kestrel & Pine's dealings with them are invented.

If you are new to commerce, this page is also your first tour of its vocabulary. Every term is explained when it first appears, and the chapter that owns it is linked.

{id: meet-kestrel-and-pine--kestrel-pine-at-a-glance}
## Kestrel & Pine at a Glance

**Kestrel & Pine B.V.** is an outdoor apparel and equipment brand headquartered in **Arnhem, the Netherlands**, founded in **2016** by **Mara Lindqvist** and **Teun Baas**. The founders hold a majority; **Veluwe Capital**, a fictional Dutch growth investor, has held a minority stake since **2022**. It sells its own brand (about **75%** of revenue: jackets, fleeces, trail trousers, merino base layers, socks, packs) and selected third-party equipment brands (about **25%**: footwear, tents, stoves, accessories) in the Netherlands, Belgium (since 2020) and Germany (since 2022), in euros throughout. In 2026 it had revenue of **€48.0 million**, a gross margin of **54%**, EBITDA of about **€3.4 million** and **310 employees** (stores 96, warehouse 88, head office 126), of whom **14** work in technology. Technology costs about **€2.6 million** a year, **5.4%** of revenue.

The revenue comes from four business lines. This is the table the whole book keeps coming back to, because each line wants something different from the architecture ([Who Sells What to Whom: Business Models and the Economics That Shape Architecture](#commerce-business-models) explains why).

| Line | Revenue 2026 | Orders or transactions | Average value | Notes |
| --- | --- | --- | --- | --- |
| **Online D2C storefronts** (NL, BE, DE) | **€27.0M** (NL €18.5M, DE €5.5M, BE €3.0M) | **293,000 orders** | **€92** | Free shipping over €75; "ordered before 22:00, delivered tomorrow" in NL |
| **Wholesale (B2B)** | **€12.0M** | **9,400 orders** | **€1,277** | **1,100 active accounts** (NL 640, BE 210, DE 250); 30-day payment terms |
| **Stores** | **€6.0M** | **118,000 transactions** | **€51** | Six stores |
| **Marketplaces** | **€3.0M** | **43,000 orders** | **€70** | bol, Amazon.de, Zalando through a channel connector |

**D2C** (direct-to-consumer) means the brand sells to the shopper through its own storefronts rather than through a retailer. **B2B** (business-to-business) means selling to other businesses, here outdoor shops that resell the products. A €51 store receipt, a €92 web order and a €1,277 wholesale order are not the same kind of transaction, even when they contain the same jacket.

{id: meet-kestrel-and-pine--how-kestrel-pine-grew-20162027}
## How Kestrel & Pine Grew, 2016–2027

The history matters because every stage left a system behind, chosen for the stage it was bought in. The book describes four **scale stages** (Starting, Growing, Omnichannel, Group; [What Changes at Each Scale: From First Store to Group](#commerce-scaling-stages) owns them), and Kestrel & Pine has passed through three.

| Years | What happened | Stage |
| --- | --- | --- |
| **2016–2018** | Founded in Arnhem; one Dutch web shop on a hosted SaaS commerce platform (software as a service: rented by the month and run by the vendor); one payment provider; orders shipped by a third-party logistics company (3PL, a warehouse that stores and ships on a merchant's behalf) in Tiel; an agency retained for the theme and apps from 2017. | 1 — Starting |
| **2019–2022** | First store in Arnhem (2019) on a cloud point-of-sale system (POS, the till software that records store sales) from a different vendor; Belgium (2020); the Utrecht store, the marketplace connector, the integration platform and GTINs on every own-brand item (2021); Germany, Veluwe Capital's investment and Ruben Alves as lead integration engineer (2022). | 2 — Growing |
| **2023–2026** | The Duiven warehouse on its own WMS, the ERP and the platform's enterprise tier with B2B features (2023); Amsterdam, Nijmegen and Eindhoven stores and the data warehouse (2023–24); Antwerp, EDI with Bergzicht Outdoor and the returns portal (2025); Peppol e-invoicing, the Utrecht click-and-collect pilot and the Black Friday Oversell (2026). | 3 — Omnichannel |
| **2027** | Noor Visser joins as Head of Engineering (January); Waypoint is approved (March). | 3 — Omnichannel |

The revenue bands behind the stages are rough markers (Starting under about €2 million, Growing to about €20 million, Omnichannel to about €200 million, Group beyond that or several brands). The *shape* decides the stage: Kestrel & Pine became Omnichannel in 2023, when it had stores, wholesale, marketplaces, three countries and its own warehouse at the same time, and a dozen systems to join. The joins are where its problems now live.

{id: meet-kestrel-and-pine--the-catalog-and-the-products}
## The Catalog and the Products

Kestrel & Pine sells **3,400 products** in **26,000 sellable variants**. A product is "the Ridgewalker shell jacket, women's"; a variant is one size in one color of it. The book calls a sellable variant a **SKU** (stock-keeping unit, the thing you can count on a shelf and put in a parcel). About **17,000 variants are active** at any time; two main seasons a year plus carry-over lines bring about **1,200 new variants** per season. Every own-brand SKU has carried a **GTIN** (Global Trade Item Number, the number behind the EAN-13 barcode) since 2021; third-party SKUs use their brand's GTIN.

The hero product is the **Ridgewalker** shell jacket, in women's and men's cuts, six sizes and four colors including "moss". A few prices recur through the book, all fictional:

| Item | Consumer price (incl. VAT) | Wholesale price (excl. VAT) | Landed cost |
| --- | --- | --- | --- |
| **Ridgewalker** shell jacket | **€199** | **€95** | **€58** |
| **Trailhead** fleece | €119 | €57 | |
| Merino hiking socks | **€18** | **€8.50** | |

Where the product data lives is the first sign of trouble. In January 2027 it lives in **three places**, the platform (storefront content and variants), the ERP item master (purchasing and costs) and shared spreadsheets (seasonal enrichment and translations), with a **fourth copy** in the marketplace connector for listings. There is **no PIM** (product information management system: one place where product content and attributes are kept and published to every channel). [What Are We Selling? Products, Variants and the Catalog](#product-information) works this out.

{id: meet-kestrel-and-pine--channels-and-customers}
## Channels and Customers

**Online.** Three localized storefronts (the Netherlands; Belgium in Dutch and French; Germany) run in **one tenant** of the platform, meaning one account on the vendor's shared service with one configuration, theme and set of apps. The Dutch storefront promises next-day delivery for orders before **22:00**, a promise written into the page rather than computed from the warehouse's state. Shoppers pay by iDEAL, card, PayPal, Klarna, Bancontact or Apple Pay.

**Stores.** Six stores, each holding about **1,800 variants**: Arnhem (2019, the flagship next to head office), Utrecht (2021; click-and-collect pilot since 2026, meaning order online and pick up in store), Amsterdam and Nijmegen (2023), Eindhoven (2024) and Antwerp (2025, where Belgian fiscal receipt rules apply). Store stock is tracked in the POS and copied to the ERP **nightly**. There is **no link between the POS and the platform**, so the click-and-collect pilot is checked by phone and e-mail. Store card payments go through a separate terminal provider ([Stores Are Systems Too: Point of Sale and Omnichannel Fulfillment](#stores-and-omnichannel)).

**Wholesale.** **1,100 active accounts**, mostly independent outdoor shops. **62%** of their orders arrive through the platform's B2B portal (company accounts, price lists, payment terms); **38%** arrive by e-mail or phone and are keyed into the ERP by the wholesale team ([Selling to Businesses: Accounts, Contract Prices, Quotes and Approvals](#b2b-commerce)). The largest account is **Bergzicht Outdoor**, a fictional Dutch outdoor chain with **38 shops** and a distribution center in **Zwolle**, worth **€2.1 million** a year. Since 2025 Bergzicht orders by **EDI** (electronic data interchange, the long-established standard for exchanging business documents such as orders and invoices between companies' systems without anyone typing them). Belgian business customers have received **Peppol** e-invoices (a European network for structured electronic invoices) since January 2026 ([Documents Between Companies: EDI, Punchout and E-Invoicing](#edi-and-e-invoicing)).

**Marketplaces.** **bol** (NL and BE), **Amazon.de** and **Zalando** (DE and NL), all through **the marketplace connector**, a channel integration service that publishes listings, pulls orders and pushes stock levels. About **40%** of marketplace units for Germany are fulfilled by the marketplace's own fulfillment program from stock Kestrel & Pine sends there in advance, a location outside its control ([Selling on Someone Else's Platform: Marketplaces and Channel Integration](#marketplaces-and-channel-integration)).

{id: meet-kestrel-and-pine--the-volumes-every-design-is-sized-against}
## The Volumes Every Design Is Sized Against

Chapters quote these 2026 figures when they size a queue, a sync interval or a peak plan. All are illustrative.

| Measure | 2026 value |
| --- | --- |
| Online D2C orders | **293,000** (about 800 a day on average) |
| Marketplace orders | **43,000** |
| Wholesale orders | **9,400** |
| Store transactions | **118,000** |
| Active variants | about **17,000** of 26,000 |
| Shipped from Duiven | **336,000** parcels plus **9,400** wholesale shipments; **1.9 million units** |
| Returns | **72,000** parcels; item return rate **24%**, order return rate **19%** on D2C; **28%** of returns are exchanges; **61%** of returned items resold as new |
| Black Friday week (23–29 November) | **31,000** D2C orders, **10.6%** of the year's |
| Peak hour (Friday 27 November, 20:00–21:00) | **2,300** orders, **38 per minute**; storefront traffic about **41×** an average hour |
| Stock sync delay at peak | up to **two hours** from a sale to the stock shown elsewhere; the WMS connector queue backed up for **four hours** |
| Installed platform apps | **41**, of which **6** unused and **3** write to inventory |
| Integrations | **34** (point-to-point and iPaaS flows) |

Two numbers deserve a pause. A 24% item return rate means one item comes back for every four shipped, so the return path is a main road, not a side street ([The Way Back: Returns, Exchanges, Refunds and Reverse Logistics](#returns-and-exchanges)). And the peak hour is 41 times an ordinary one: a design that works at 800 orders a day meets 2,300 in one hour, once a year, which is what the pattern **The First Snowfall** warns about ([Black Friday Every Year: Peak Load, Resilience and Recovery](#peak-load-and-reliability)).

{id: meet-kestrel-and-pine--the-systems-landscape-in-january-2027}
## The Systems Landscape in January 2027

When Noor Visser arrives in January 2027, this is what she finds. Each system is named by its role.

| Area | System | Since | Notes |
| --- | --- | --- | --- |
| Storefront, cart, checkout, B2B portal | **the platform**, a hosted SaaS commerce platform, enterprise tier since 2023 | 2016 | Three storefronts in one tenant; theme customized by the agency; 41 apps |
| Finance and back office | **the ERP** (enterprise resource planning system: the books, purchasing, inventory valuation, invoicing, item master, manual wholesale order entry) | 2023 | The platform-to-ERP connector was built by the ERP partner |
| Warehouse | **the WMS** (warehouse management system: receiving, picking, packing and shipping at Duiven) | 2023 | Orders in from the platform, stock out to the ERP, via the iPaaS |
| Order management | **none** | — | Orders live in the platform, the connector, the ERP and the POS |
| Product information | **none** | — | Product data in the platform, the ERP, spreadsheets and the connector |
| Marketplaces | **the marketplace connector** | 2021 | Listings, orders, hourly stock sync |
| Stores | **the POS** | 2019 | Store stock to the ERP nightly; no link to the platform |
| Returns | **the returns portal** (SaaS) | 2025 | Labels, reasons, exchanges; refunds through the platform's API |
| Shipping | **the shipping service** (multi-carrier labels and tracking) | 2023 | Inside the WMS flow |
| Payments | **the PSP** (payment service provider: the company that takes the shopper's payment and settles the money to the merchant) | 2016 | A separate terminal provider for stores since 2019 |
| EDI | **the EDI provider** (a value-added network that relays EDI documents between trading partners) | 2025 | The order, despatch advice and invoice messages (ORDERS, DESADV, INVOIC) with Bergzicht; Peppol e-invoices |
| Integration | **the iPaaS** (integration platform as a service: a hosted tool for building and running the flows that move data between systems) plus agency scripts and vendor connectors | 2021 | 34 integrations; owned by Ruben Alves |
| Data | **the data warehouse** and a BI tool (business intelligence: reports and dashboards) | 2024 | Three definitions of "order" in use |

Two rows say "none", and they are the point of this page. There is no **OMS** (order management system: one place that holds every order from every channel, with one status model, and steers it through payment, fulfillment, delivery and return). And there is no PIM. So an order is a platform record if Eva placed it online, a connector record if she bought on bol, an ERP record if a shop e-mailed it, and a POS receipt if she bought in Nijmegen; a product is described four times. Nobody decided this. It is what buying one good system per need, one need at a time, produces ([Who Owns the Truth: Boundaries, Bounded Contexts and Systems of Record](#boundaries-and-systems-of-record) and [The Order Record: Lifecycle, State and the Order Management System](#order-management) take it from here).

![Diagram: Kestrel & Pine's January 2027 landscape](commerce-platform-architecture/posts/meet-kestrel-and-pine/assets/images/meet-kestrel-and-pine/fig01-kestrel-pine-s-january-2027-landscape.jpeg)

**Figure 1:** *Kestrel & Pine's January 2027 landscape: four channels create orders in four different systems, stock travels from the WMS to the ERP to the platform to the marketplace connector in quarter-hourly and hourly hops, and no system holds all orders or all product data.*

The **stock sync chain** in the middle of the figure is the mechanism behind the Black Friday Oversell. The WMS knows what is physically on the shelf. It tells the ERP every 15 minutes; the ERP tells the platform every hour; the platform tells the connector every hour; the connector tells the marketplaces. A sale at Duiven can take up to **two hours** to reduce the number a shopper sees on Amazon.de, and in those two hours every channel believes it can still sell the unit. [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability) owns the fix.

{id: meet-kestrel-and-pine--the-people}
## The People

Each person owns something the architecture depends on, and most of the book's tensions are between their legitimate goals. All are fictional.

| Person | Role | Pronouns | Owns |
| --- | --- | --- | --- |
| **Mara Lindqvist** | Co-founder and CEO | she/her | The Waypoint budget |
| **Teun Baas** | Co-founder, Chief Product and Brand | he/him | The catalog and the seasons |
| **Noor Visser** | Head of Engineering since January 2027 | she/her | **The reader's stand-in.** Previously lead engineer at a logistics software company; proposed Waypoint |
| **Daniel Okafor** | Head of Operations | he/him | The warehouse, the stores and the carriers |
| **Sanne de Wit** | Finance Director | she/her | The ERP, invoicing and month-end |
| **Milan Petrov** | Ecommerce and Marketplaces Manager | he/him | The storefronts, the apps and the marketplace connector |
| **Lea Moreau** | Head of Wholesale | she/her | The B2B portal and the EDI relationship |
| **Ruben Alves** | Lead Integration Engineer since 2022 | he/him | The iPaaS and the integration inventory |
| **Hanna Berg** | Data Lead | she/her | The data warehouse and metric definitions |
| **Eva Janssen** | A customer in Nijmegen | she/her | The recurring order |
| **Pieter Smit** | Buyer at Bergzicht Outdoor | he/him | The spring reorder |
| the agency | External storefront and apps agency since 2017 | — | The theme, the apps and several scripts |
| the ERP partner | External ERP implementation partner | — | The platform-to-ERP connector |

Noor leads a technology team of **14**: herself, nine engineers (four integration and back-end, three storefront and apps, two data), two product managers and two application support specialists. When a chapter says "you", it usually means Noor: new to this company, not new to engineering, and asked to decide about systems she did not choose.

{id: meet-kestrel-and-pine--the-problems-kestrel-pine-starts-2027-with}
## The Problems Kestrel & Pine Starts 2027 With

When Noor starts, every system works and the company is profitable. The problems are in the joins. Ten incidents define her starting position; each is an instance of a named pattern from [Out of Stock, Out of Sync: Sixteen Ways Commerce Platforms Go Wrong](#where-commerce-platforms-go-wrong), and each is worked in full by the chapter that owns it.

1. **The Black Friday Oversell** (Friday 27 November 2026). The Ridgewalker sold out at Duiven at 19:40; the storefronts and marketplaces kept selling it for up to two hours. **1,340 units** oversold, **1,120 orders** canceled or delayed, about **€96,000** in cost including goodwill vouchers and marketplace penalties. *The Phantom Stock* and *The First Snowfall*; [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability), [Journey 4: Black Friday, Hour by Hour](#journey-peak-day).
2. **The Three-Status Order** (December 2026). Order **#1052877** showed *Delivered* in the platform, *In picking* in the WMS and *Not invoiced* in the ERP for six days; one customer opened **11 support tickets**. *Schrödinger's Order*; [The Order Record: Lifecycle, State and the Order Management System](#order-management), [Where Is My Order? Notifications, Service and the Customer Record](#customer-service-and-notifications).
3. **The Double Refund** (January 2027). Over three weeks, **212 returns** were refunded twice: once by the returns portal through the platform's API and once by hand in the PSP console. **€19,400** went out twice, most of it recovered. *The Boomerang* and *The Message in a Bottle*; [The Way Back: Returns, Exchanges, Refunds and Reverse Logistics](#returns-and-exchanges), [Taking the Money: Payment Providers, Authorization, Capture and Refunds](#commerce-payments).
4. **The Price Drift** (October 2026). The German storefront sold the Ridgewalker at **€179** for **nine days** while the marketplace listing and the stores charged **€199**; a price-list sync had failed silently. **410 orders**, about **€8,200** of margin lost, and a price-parity warning from a marketplace. *The Price Nobody Can Explain*; [What Does It Cost? Price Lists, Contract Prices, Currencies and Tax](#pricing-architecture).
5. **The ASN Chargeback** (Q3 2026). Bergzicht deducted **€14,200** for despatch advices whose pallet labels did not match what arrived. A despatch advice (**DESADV** in EDIFACT, the UN message standard most European EDI uses; also called an ASN, advance shipping notice) tells the buyer what is on its way and on which pallets, each identified by an **SSCC** (serial shipping container code, the 18-digit number on a pallet label); Kestrel & Pine's DESADV came from the ERP's view of the order, not from what the warehouse packed. *The Pulled Rug* (the contract) and *The Lynchpin* (one EDI consultant); [Documents Between Companies: EDI, Punchout and E-Invoicing](#edi-and-e-invoicing).
6. **The Store Stock Mirage** (December 2026). Click-and-collect at Utrecht promised **37** items the store had already sold, because store stock reaches the ERP only nightly. *The Phantom Stock*, from the store side; [Stores Are Systems Too: Point of Sale and Omnichannel Fulfillment](#stores-and-omnichannel).
7. **The App That Wrote Stock** (March 2026). A pre-order app adjusted inventory in the platform while the WMS feed also wrote it: two weeks of phantom reservations on **600 variants**. *The Secret Agent* (an unowned writer) and *The Spaghetti Junction*; [Apps, Plugins and Functions: Extensibility and Ecosystem Governance](#extensibility-and-app-ecosystems).
8. **The Card-Testing Night** (August 2026). **48,000** bot attempts with stolen card numbers hit the checkout in one night; **€2,900** in PSP fees for declined authorizations, and the PSP paused the account for 40 minutes. A trust failure rather than one of the sixteen patterns; [Protecting the Shop: Card Data, Account Takeover, Bots and Skimmers](#commerce-security).
9. **The Familiar Stranger.** Eva Janssen exists as an online account, a POS loyalty customer, a newsletter subscriber and a returns-portal contact, with no shared identifier, so nobody can say she is one person. *The Familiar Stranger*; [One Customer, One Product: Identity and Master Data Across Systems](#identity-and-master-data).
10. **The Deprecated Endpoint** (February 2027). The marketplace connector retired an API version on a published date; the agency script that read it had not been updated, and stock to bol was stale for **two days**. *The Pulled Rug*; [Promises Between Systems: API Contracts, Webhooks and Versioning](#api-contracts-and-versioning).

Eight of the ten are the same problem: a fact (stock, status, price, identity) that lives in more than one system, with no agreed owner and no reliable way for the copies to learn of a change. The other two are what the outside world does to a landscape nobody watches as a whole.

![An empty jacket shelf in the warehouse at 19:40 while three storefront screens still show the jacket in stock; 1,340 units oversold.](commerce-platform-architecture/posts/meet-kestrel-and-pine/assets/images/meet-kestrel-and-pine/meet-kestrel-and-pine-black-friday-oversell.jpeg)

**Figure 2:** *The Black Friday Oversell: the Ridgewalker sold out at Duiven at 19:40, but the storefronts and marketplaces kept selling it from a copy up to two hours old, and 1,340 units were oversold.*

{id: meet-kestrel-and-pine--the-waypoint-program}
## The Waypoint Program

In **March 2027** Mara Lindqvist approved **Waypoint**, on Noor's proposal: **€1.1 million** over 2027–2028 on top of the running technology spend. The decisions are canonical; chapters explain them and never change them.

| Decision | What changes | When |
| --- | --- | --- |
| **W1 — Stock ownership** | The WMS becomes the **system of record** for physical stock at Duiven (the one system whose value is the truth when copies disagree); the POS for store stock; the marketplace fulfillment stock becomes a tracked external location. An **availability service**, bought as a module of the OMS below, computes **available-to-promise** per channel (what a channel may still sell: physical stock minus what is already promised or reserved) from stock events. The sync chain is retired. | Q4 2027 |
| **W2 — One order record** | A bought **OMS** becomes the order hub: every channel's order (platform, marketplaces, EDI, manual wholesale, later stores) is created there, with one state model and one order number family. The platform keeps the checkout and the storefront order history. | Q4 2027 |
| **W3 — Product information** | A **PIM** becomes the system of record for product content and attributes; the ERP keeps costs and purchasing; the platform and the connector become consumers. | Q3 2027 |
| **W4 — Stay and surround** | Kestrel & Pine **stays on its SaaS platform**; no replatforming. Capabilities the platform does not own well (OMS, PIM, availability) are added beside it. The platform's own POS is evaluated in 2028. | 2027; review 2029 |
| **W5 — Integration standards** | Every integration gets a named owner, a contract (fields, direction, frequency, system of record), **idempotent** handling of repeated messages (receiving a message twice has the same effect as once) and a reconciliation job; the inventory is kept current. Stock, orders and prices move by **events** (a message sent the moment something changes, instead of a periodic copy); products by scheduled publication; finance by daily batch. | From 2027 |
| **W6 — EDI compliance** | SSCC labels generated by the WMS at pack time; DESADV sent from the WMS pack confirmation, not from the ERP; one EDI partner card per trading partner. | 2027 |
| **W7 — One definition of an order** | The data warehouse adopts one metric definition for order, revenue and return, owned by the Data Lead. | 2027 |
| **W8 — Agent readiness, not agents** | Accurate product data (via the PIM), availability and delivery promise by API, and order status by API are prerequisites; no shopper-facing AI agent in 2027. | 2027 |

The order is the argument. Waypoint decides **who owns each fact** first (W1, W3, W7), then adds the hubs the landscape lacks (the availability service, the OMS, the PIM), then makes the copies trustworthy (W5, W6). It does not replace the platform (W4), because the platform is not what failed; the joins failed. [Build, Buy or Assemble: Choosing and Changing Platforms](#build-buy-or-assemble) works the stay-and-surround decision, [Built to Disagree and Recover: Events, Eventual Consistency and Reconciliation](#events-consistency-and-reconciliation) the integration standards, [Assistants and Agents: AI in Commerce and What Is Real in 2026](#ai-and-agentic-commerce) W8.

{id: meet-kestrel-and-pine--the-recurring-worked-examples}
## The Recurring Worked Examples

Five stories recur through the book. Their facts never change, so you can follow one order across many chapters and the numbers will always agree.

**Eva's jacket, the recurring order.** On **Tuesday 13 April 2027 at 21:14**, Eva Janssen in Nijmegen orders on the Dutch storefront: one **Ridgewalker shell jacket, women's, size M, color moss (€199)** and **two pairs of merino hiking socks (€18 each)**. Total **€235**, free shipping, paid by **iDEAL** (the Dutch bank-transfer method most online shoppers there use). Order number **#1072455**; because she ordered before 22:00, delivery is promised for tomorrow, Wednesday. The order is picked and packed at Duiven on **Wednesday 14 April**, shipped with PostNL and delivered **Thursday 15 April**, a day later than promised, because Duiven's last pick wave leaves at 21:00 ([Pick, Pack, Ship: Warehouse Management and Fulfillment](#warehouse-and-fulfillment)). On **Monday 19 April** she requests an **exchange of the jacket for size L** through the returns portal (too small). The return is received and inspected on **22 April**, graded resellable, and the exchange order ships the same day. If a chapter needs the refund variant, it is a refund of **€199** by iDEAL reversal, booked as a credit note.

![Diagram: Eva's jacket crosses seven systems in nine days](commerce-platform-architecture/posts/meet-kestrel-and-pine/assets/images/meet-kestrel-and-pine/fig02-eva-s-jacket-crosses-seven-systems.jpeg)

**Figure 3:** *Eva's jacket crosses seven systems in nine days: the platform sells and takes the money, the iPaaS carries the order to the WMS, PostNL delivers, stock trickles back through the ERP, and the exchange re-enters through the returns portal; every arrow is a handoff that can be late, lost or duplicated.*

This is the order [Follow the Order: What Happens Between “Buy” and “Delivered”](#journey-of-an-order) walks step by step and [Journey 1: Eva's Jacket, From Search to Doorstep](#journey-consumer-order) and [Journey 2: The Jacket Comes Back](#journey-return-and-exchange) work in full. Every chapter says near its top where in this journey it sits.

**Bergzicht's spring reorder.** An EDI ORDERS message arrives on **Tuesday 6 April 2027** for **240 units** across **18 SKUs** (Ridgewalker jackets and Trailhead fleeces), worth **€19,860** excluding VAT. It is picked to **three pallets** with SSCC labels; the DESADV is sent at pack confirmation; the pallets reach the Zwolle distribution center on **9 April**; the INVOIC (the EDI invoice) is sent the same day; payment is due **9 May**, on 30-day terms. [Journey 3: A Chain Reorders by EDI, From Order to Invoice](#journey-wholesale-order) and [Documents Between Companies: EDI, Punchout and E-Invoicing](#edi-and-e-invoicing).

**The marketplace variant.** On 13 April 2027, the day of Eva's order, one Amazon.de customer orders a Ridgewalker that Kestrel & Pine ships itself from Duiven (seller-fulfilled), and another orders one that the marketplace's fulfillment program ships from the stock sent there in advance. The two orders look alike to the customers and nothing alike to the systems. [Selling on Someone Else's Platform: Marketplaces and Channel Integration](#marketplaces-and-channel-integration).

**Black Friday 2026.** The week of 23–29 November and its Friday evening: 31,000 orders, a peak hour of 2,300, the sell-out at 19:40, the two-hour stock lag and the four-hour WMS queue, with the numbers in the volumes table and in problem 1. [Journey 4: Black Friday, Hour by Hour](#journey-peak-day), [Black Friday Every Year: Peak Load, Resilience and Recovery](#peak-load-and-reliability) and [Pick, Pack, Ship: Warehouse Management and Fulfillment](#warehouse-and-fulfillment).

**The stock reconciliation.** In **May 2027**, the first weekly reconciliation between the WMS and the platform (a job that compares the two systems' quantities and lists the differences) found **2.3%** of active variants with a different quantity, most left behind by the three apps that wrote stock. [Built to Disagree and Recover: Events, Eventual Consistency and Reconciliation](#events-consistency-and-reconciliation).

The 2026 incidents are the evidence behind Waypoint. The 2027 examples happen while Waypoint runs and test its priorities: ownership before hubs, contracts before connectors, reconciliation for every copy.

{id: meet-kestrel-and-pine--how-the-chapters-use-kestrel-pine}
## How the Chapters Use Kestrel & Pine

Each chapter opens with a 2027 scene at Kestrel & Pine, then answers its question with concepts, dated public evidence from real companies and standards, and a Kestrel & Pine worked example. Chapters in Parts II to VIII end with a table across the four scale stages, using Kestrel & Pine's own path as one column. The journeys of [Part IX — JOURNEYS: One Order, End to End](#part-9) follow the recurring orders end to end; the case studies of [Part XI — PRACTICE: How Others Built It](#part-11) leave Kestrel & Pine and test the book against the public record.

Three conventions hold. **Kestrel & Pine is labeled fictional** the first time it appears in a chapter. **Its systems are named by role**, never by vendor, so nothing in the book reads as a recommendation for or against a product. **Its facts come from one canonical record**, so the 1,340 units, the €19,400 and order #1072455 mean the same on every page; numbers that are neither Kestrel & Pine's nor documented are labeled as assumptions.

With the company, its problems and its program introduced, Part I begins where Noor began in her first week: by following one order through every system it touches, and asking at each handoff which system made the promise and which one has to keep it. Continue with [Part I — COMMERCE: What a Commerce Platform Is](#part-1).

{id: meet-kestrel-and-pine--sources-and-evidence}
## Sources and Evidence

Kestrel & Pine, Bergzicht Outdoor, Veluwe Capital and every person named here are fictional; all figures are illustrative.
