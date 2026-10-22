{id: domain-coverage}
# Domain Coverage: From Productscape Models to Chapters

![Domain Coverage: From Productscape Models to Chapters — logo](stays-marketplace-architecture/posts/domain-coverage/assets/images/domain-coverage/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Trace every capability of two generic reference models of a stays marketplace, 34 in the OTA-style model and 21 in the hosted-stays model, to the chapters that cover it, and see which capabilities the book added because neither model has them and which it deliberately leaves out.

> **KEY POINTS:**
>
> * **Every one of the 55 bricks has a home.** Each capability in the two reference models maps to one chapter that covers it in depth (*primary*) and often to others that use it (*also*). The thinnest coverage is for the HSM bricks that the model itself draws thinly, such as `apix` and `idvr`.
> * **The overlap matrix tells you where to read twice.** Only 12 of the 34 OTA bricks have a same-concept counterpart in the hosted-stays model. Where a pair is only partial, or exists on one side only, a chapter's "Hotels and Homes" section argues the difference, and this page names that chapter.
> * **The most important domains are the ones nobody drew.** Seven capabilities that cut across journeys (tax engine, loyalty, channel management for hosts, content mapping, notifications, distribution and affiliates, customer data platform) are added as domains of their own. Seventeen more gaps are covered inside existing chapters, and three are deliberately left out (partner CRM, company travel programs and connected trips), each for a stated reason.

> **[FAILURE PATTERNS THIS SECTION ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **The Hotel-Shaped Home** — a coverage map that matches capabilities by name, not by meaning, hides the places where hotels and homes need different machinery; this page marks each such place and the chapter that argues it.

This book was planned from **two capability models**, not from a table of contents. One describes an OTA-style accommodation marketplace that sells rooms by room type and rate plan. The other describes a hosted-stays marketplace that sells nights in homes run by hosts. Each model lists the **product bricks** (named business capabilities) that such a marketplace needs, grouped into three root groups; together they hold 55 bricks. The chapters were drawn so that every brick lands in one, and capabilities that neither model has were added on purpose.

This page is the audit trail of that planning. It answers three questions: **"Where is my capability covered?"**, **"Where does the book argue that hotels and homes differ?"** and **"What did the book add, and what did it leave out?"** It is a lookup table and does not repeat the arguments of [Mapping the Business: Capability Maps for Two Marketplaces](#stays-capability-map) (the capability map and the rule for what a group should share) or [Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts) (the service boundaries drawn from it).

{id: domain-coverage--where-the-two-models-come-from}
## Where the Two Models Come From

Both models are **Productscape domain models**: structured descriptions of a product domain (customers and their jobs, product bricks, value streams, data assets, deployments and stress tests) kept as JSON and Markdown in the author's sibling `productscape-workspace` repository. This book used two of them, both version 1.0, both under `productscape-examples/_config/product-domains/marketplaces/`.

| Short name | Folder | Portfolio name | Shape |
| --- | --- | --- | --- |
| **TAM** (travel accommodations, OTA-style) | `travel-accommodations-marketplace/` | Travel Accommodations Marketplace Platform | 34 bricks in 3 root groups and 6 groups; 154 modules; 4 personas (leisure traveler, managed-travel booker, hotel revenue manager, independent host) |
| **HSM** (hosted stays) | `hosted-stays-marketplace/` | Hosted Stays Marketplace Platform | 21 bricks in 3 root groups and 6 groups; 77 modules; 3 personas (guest, everyday host, professional host or co-host operator) |

The two models are **generic reference models, not descriptions of any company**. Their authoring notes say they were written with public operators as inspiration: the TAM notes describe "the core accommodations marketplace in which Booking.com most clearly operates today" while being "intentionally generic rather than Booking.com-branded", and the HSM notes say the model covers "Airbnb's clearest core business". Both cite public investor, help-center and developer pages reviewed in March 2026. That does not make a brick, a module boundary, a value stream or a stress test a fact about Booking.com, Airbnb or anyone else. The book uses the models as a **worked reference model of a generic operator** and takes every company claim from dated public sources instead.

Three cautions follow from how the models were built:

- **Brand names leaked into the hosted-stays model, and the book removes them.** One HSM brick carries a real company's protection-program name, and a KPI uses a real top-host status name. This book calls them "the host and guest protection program" and "top-host status".
- **KPI values are illustrative and are never quoted.** The KPI trees carry placeholder numbers, some of them impossible. The book uses KPI *names* and tree *shapes* (for example "Reservation sync latency" or "Calendar accuracy rate") and none of the values.
- **The two models were authored separately.** They share only five brick identifiers (`srch`, `book`, `trip`, `trst`, `paym`), and one of those, `trst`, means different things in each. They are matched below by meaning, not by identifier.

{id: domain-coverage--how-to-read-the-coverage-tables}
### How to read the coverage tables

Each brick has a short identifier (four or five letters, such as `invt` or `lista`), a name, a type (`full-stack`, `service` or `integration`) and named modules. Where the same identifier appears in both models, this page prefixes it: TAM `trst`, HSM `trst`.

For each brick the tables give:

- **Primary**: the chapter that covers the brick in depth, owns its main terms and draws its architecture. When a brick's modules are split between chapters, the primary chapter is the one that owns the brick's purpose, and the split is noted.
- **Also**: chapters that cover a specific module, use the brick as an input, or compare it across the two marketplace types.

The coverage was cross-checked against three sources: the digest's complete brick inventory (every brick and module name was extracted, not sampled), the "Domains" field of every chapter contract in the book plan, and the list of brick identifiers in each written chapter's spec. Two chapters cover **all** 55 bricks at map level and are not repeated in every row: [Mapping the Business: Capability Maps for Two Marketplaces](#stays-capability-map) (the capability map and overlap matrix) and [Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts) (the context map built from it). Chapters 43 to 51 (leadership and case studies) use the bricks as context rather than covering them, and appear only where they own a specific point.

{id: domain-coverage--coverage-of-the-ota-style-model-tam}
## Coverage of the OTA-Style Model (TAM)

TAM's three root groups are **Traveler Experience** (demand side), **Partner Operations** (supply side) and **Marketplace Foundations** (shared). Its four `invest` bricks are `book`, `prom`, `paym` and `mkli`; the other 30 are `sustaining`.

{id: domain-coverage--root-a-traveler-experience}
### Root A. Traveler Experience

| Group | Brick (id) | What it is | Primary | Also |
| --- | --- | --- | --- | --- |
| A1 Discovery and consideration | Marketplace Home & Destination Landing (`home`) | Entry surfaces, recent-search recall, campaign landings, merchandising slots | [Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels) (landing assembly, merchandising slots) | [Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture) (handoff into search); [Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations) (session recall and intent recovery) |
| | Destination Discovery (`dest`) | Destination context graph, travel-intent resolution | [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps) | [Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture) (destination resolution step) |
| | Search, Ranking & Filters (`srch`) | Search index and facets, ranking and eligibility pipeline, filter explainability, inventory update feed | [Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture) (index, facets, pipeline) | [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) (ranking pipeline, explainability); [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine) (inventory update feed); [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays) (feed as an event stream) |
| | Map-Based Stay Browser (`mapb`) | Viewport search, map tiles and geometry | [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps) | [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) (ranking for maps vs lists) |
| | Personalization & Recommendations (`pers`) | Traveler-intent models, recommendation delivery | [Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations) | [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform) (models in production) |
| | Deals and Member Merchandising (`deal`) | Offer eligibility, member and urgency presentation, treatment experiments | [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty) | [Testing Everything: Experimentation Platforms for Stays](#stays-experimentation) (treatment experimentation); [Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels) (presentation on landing pages) |
| | Saved Searches & Price Alerts (`ssav`) | Saved intent store, alert trigger engine | [Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations) | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) (alerts delivered through notification routing) |
| | Property Detail & Reviews (`prop`) | Property content assembly, review and quality signals, policy explanation | [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) | [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation) (review signals); [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) (price and policy presentation duties) |
| A2 Booking and trip management | Room & Rate Selection (`room`) | Room plan resolver, rate condition comparison, room offer API | [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) (room and rate comparison) | [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) (rate plans and conditions); [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine) (room offer computation) |
| | Checkout & Booking Orchestration (`book`) | Checkout state, policy disclosure, reservation API and orchestration | [Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration) | [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) (reservation state after commit); [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays) (reservation event feed) |
| | Traveler Account & Wallet (`acct`) | Traveler profile, preferences, saved payment and invoicing context | [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) | [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments) (saved payment methods); [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty) (member status) |
| | Trip Management & Messaging (`trip`) | Trip timeline, message and notification routing, trip status explanation | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) | [When Something Goes Wrong: Customer Service and Recovery](#customer-service) (escalation from the trip) |
| | Guest-Property Messaging (`msgc`) | Conversation threads, delivery and policy controls | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) | [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) (phishing through booking messages); [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety) (message enforcement) |
| | Self-Service Changes & Recovery (`self`) | Eligibility and policy engine, recovery flow orchestration | [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) | [When Something Goes Wrong: Customer Service and Recovery](#customer-service) (deflection and escalation); [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) (disruption-specific actions) |
| | Review Collection & Stay Feedback (`reve`) | Stay-completion triggers, verified review submission | [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation) | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) (review invitation trigger); [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) (completion as trigger) |

{id: domain-coverage--root-b-partner-operations}
### Root B. Partner Operations

| Group | Brick (id) | What it is | Primary | Also |
| --- | --- | --- | --- | --- |
| B1 Supply onboarding and content | Partner Extranet (`extr`) | Partner control surface and operational workbench | [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools) | [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) (extranet takeover); [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) (partner staff roles) |
| | Partner Onboarding & Verification (`onbo`) | Eligibility and setup workflow, verification and activation controls, activation API | [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding) | [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) (partner verification); [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) (license evidence under stressor `licn`) |
| | Content & Policy Studio (`cont`) | Content quality validation, policy authoring workspace | [Describing a Stay: Content, Media and Property Mapping](#content-and-media) | [Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model) (room setup, amenities, policies as model); [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) (policy authoring and permit disclosures) |
| | Property Media Pipeline (`medi`) | Media ingestion, transformation, moderation, categorization | [Describing a Stay: Content, Media and Property Mapping](#content-and-media) | — |
| B2 Inventory and commercial performance | Inventory, Rates & Reservations (`invt`) | Rate and availability core, reservation state machine, supply integrity controls, supply core API | [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) (rate and availability core) | [Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model) (what is sold); [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers) (sync to PMS and channel managers); [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine) (source of truth for search); [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) (supply integrity controls); [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) (reservation state machine) |
| | Calendar & Availability Controls (`cald`) | Availability editing workspace, restriction policy engine | [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) (restrictions: minimum stay, closed to arrival or departure, booking windows) | [One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync) (calendar controls for homes on the OTA) |
| | Reservation Inbox & Operations (`rsrv`) | Reservation work queue, exception controls (overbooking, no-show, special requests) | [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools) (reservation operations and exception queues) | [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) (no-shows, delivery and acknowledgement); [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) (overbooking and relocation) |
| | Partner Merchandising & Programs (`prom`) | Program eligibility and enrollment, promotion authoring, program impact feedback | [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty) | [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) (program-driven visibility and its disclosure) |
| | Rate Recommendation Engine (`rate`) | Comp-set and demand models, recommendation delivery, margin guardrails | [Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing) | [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform) (pricing models and their governance) |
| | Partner Performance Analytics (`perf`) | Performance metrics warehouse, insight and narrative layer | [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools) (partner analytics as a product) | [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence) (partner insight as a data product) |
| | Reputation & Quality Operations (`rept`) | Review intake and validation, quality monitoring, partner remediation | [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation) | [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety) (content integrity) |

{id: domain-coverage--root-c-marketplace-foundations}
### Root C. Marketplace Foundations

| Group | Brick (id) | What it is | Primary | Also |
| --- | --- | --- | --- | --- |
| C1 Payments and recovery | Payments & Payouts (`paym`) | Traveler payment orchestration, partner remittance and reconciliation, payment model normalization, payment state feed | [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments) (traveler payment orchestration, payment state feed) | [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models) (payment model normalization); [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) (partner remittance); [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation) (refunds, disputes, reconciliation); [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays) (payment state feed) |
| | Partner Settlement & Ledger (`sett`) | Settlement ledger core, finance adjustment workflow | [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) (settlement ledger) | [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation) (finance adjustment workflow) |
| | Customer Support & Recovery (`supp`) | Case and workflow orchestration, recovery decisioning, escalation and SLA controls | [When Something Goes Wrong: Customer Service and Recovery](#customer-service) | [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) (recovery after incidents); [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) (rebooking and relocation) |
| C2 Trust, connectivity and intelligence | Trust, Verification & Risk Controls (TAM `trst`) | Identity and verification, fraud and abuse controls, integrity operations, risk signal feed | [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety) (trust decision, integrity operations) | [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) (fraud and abuse controls); [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) (partner and host verification) |
| | Connectivity & Partner APIs (`conn`) | Partner connectivity API, contract and validation layer, reservation and inventory sync, reliability controls | [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers) | [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays) (partner integration event feed); [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) (sync failures as an integrity risk) |
| | Marketplace Intelligence (`mkli`) | Metrics and attribution, decisioning models, experiment and causal analysis | [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence) | [Liquidity, Take Rates and Look-to-Book: The Economics of Stays Marketplaces](#stays-marketplace-economics) (metric names as economics); [Testing Everything: Experimentation Platforms for Stays](#stays-experimentation) (experiment and causal analysis); [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform) (decisioning models); [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) (ranking signals) |
| | Geo & Localization Services (`geoa`) | Place and boundary resolver, localization and market context | [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps) (place and boundary resolution) | [Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability) (localization and market context); [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) (disruption boundaries) |
| | Identity & Access Management (`idam`) | Authentication and session core, role and access policy engine | [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) | [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) (partner-account security) |

{id: domain-coverage--coverage-of-the-hosted-stays-model-hsm}
## Coverage of the Hosted-Stays Model (HSM)

HSM's three root groups are **Guest Experience**, **Host Success** and **Marketplace Foundations**. Its eight `invest` bricks are `list`, `book`, `hono`, `lista`, `pric`, `opco`, `coho` and `reso`, which shows where a hosted-stays marketplace spends: on creating supply and running it, not on monetization levers.

{id: domain-coverage--root-a-guest-experience}
### Root A. Guest Experience

| Group | Brick (id) | What it is | Primary | Also |
| --- | --- | --- | --- | --- |
| A1 Discovery and consideration | Inspiration & Category Discovery (`insp`) | Category and destination landing assembly, intent recovery and recirculation | [Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture) (category and flexible-destination browsing) | [Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations) (intent recovery, recirculation); [Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels) (landing pages) |
| | Search, Ranking & Map Browse (HSM `srch`) | Search index and relevance engine, map browse and geo-intent layer | [Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture) | [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) (relevance and ranking); [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps) (map browse layer, approximate location) |
| | Listing Detail & Review Trust (`list`) | Listing content renderer, review and trust evidence service | [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) (listing page, total price, trust evidence) | [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation) (review trust evidence) |
| | Wishlists & Sharing (`wish`) | Saved lists, sharing and group collaboration | [Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations) | — |
| A2 Booking and stay management | Booking & Checkout (HSM `book`) | Reservation orchestration with trust screening, checkout experience | [Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration) (instant book, request to book) | [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) (reservation after commit); [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) (screening before confirmation); [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays) |
| | Trip Messaging & Itinerary (HSM `trip`) | Reservation timeline, guest–host messaging | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) | [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) (reservation timeline) |
| | Guest Reviews & Re-engagement (`grev`) | Review collection, re-engagement triggers | [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation) (double-blind review) | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) (review and re-engagement triggers) |

{id: domain-coverage--root-b-host-success}
### Root B. Host Success

| Group | Brick (id) | What it is | Primary | Also |
| --- | --- | --- | --- | --- |
| B1 Host activation and optimization | Host Onboarding & Verification (`hono`) | Host activation flow, readiness service, readiness API | [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding) | [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) (registration numbers as a readiness gate) |
| | Listing Authoring & Content (`lista`) | Listing editor, content quality service | [Describing a Stay: Content, Media and Property Mapping](#content-and-media) (host-authored content, photo guidance) | [Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model) (listing as the sellable unit) |
| | Calendar & Availability (`cala`) | Availability engine for bookable dates, blocks and stay restrictions | [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) (nightly calendar model) | [One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync) (keeping one home's calendar correct across channels); [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine) (calendar in search); [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) (never selling a night twice) |
| | Pricing & Discounts (`pric`) | Pricing rules engine (nightly, discounts, length of stay), pricing guidance | [Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing) (smart pricing and guidance) | [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) (length-of-stay rules, cleaning fees); [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty) (host discount programs) |
| B2 Host operations and economics | Turnover & Operations Coordination (`opco`) | Turnover task engine, operations coordination UI | [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools) | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) (check-in and access readiness) |
| | Co-host Network & Permissions (`coho`) | Role and permission service with audit trails, co-host collaboration | [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools) | [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) (partner role model); [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) (split payouts to co-hosts and beneficiaries) |
| | Host Performance & Earnings (`host`) | Host performance warehouse, earnings dashboards | [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools) | [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence) (host insight); [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) (earnings and statements) |

{id: domain-coverage--root-c-marketplace-foundations-1}
### Root C. Marketplace Foundations

| Group | Brick (id) | What it is | Primary | Also |
| --- | --- | --- | --- | --- |
| C1 Trust, payments and policy | Identity & Verification (`idvr`) | Guest and host identity verification, document checks, screening signals | [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) (identity levels) | [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding) (host verification at activation) |
| | Trust, Safety & protection program (HSM `trst`) | Trust decision API, risk scoring and screening, protection and incident workflow, incident operations UI | [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety) (trust decision API) | [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) (risk scoring); [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) (screening, protection and incident workflow) |
| | Payments, Taxes & Payouts (HSM `paym`) | Payment orchestration, host payout ledger (fees, taxes, payout timing) | [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments) (payment orchestration) | [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models) (facilitated collection); [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) (host payout ledger); [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays) (tax flows); [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation) (refunds) |
| | Resolutions & Support (`reso`) | Support case API, case orchestration, resolution center (claims, disputes, refunds) | [When Something Goes Wrong: Customer Service and Recovery](#customer-service) | [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) (host cancellations, extenuating circumstances); [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) (damage claims); [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation) (refunds as case outcomes) |
| | Local Compliance & Policy Controls (`comp`) | Market policy registry, listing eligibility, audit state | [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) | [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays) (platform tax reporting); [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding) (eligibility at activation) |
| C2 Marketplace intelligence and connectivity | Marketplace Intelligence & Experimentation (`data`) | Insight warehouse, experimentation and recommendation layer | [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence) | [Liquidity, Take Rates and Look-to-Book: The Economics of Stays Marketplaces](#stays-marketplace-economics); [Testing Everything: Experimentation Platforms for Stays](#stays-experimentation); [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform) |
| | Partner APIs & Channel Connectivity (`apix`) | Partner gateway, sync and export services for professional operators | [One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync) (API-connected vs iCal-connected listings) | [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers) (inbound vs outbound connectivity compared); [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays) (APIs without event feeds) |

{id: domain-coverage--is-anything-uncovered}
### Is anything uncovered?

No. **All 34 TAM bricks and all 21 HSM bricks have a primary chapter.** Three bricks deserve a note, because their coverage is real but thinner than their names suggest:

- **HSM `apix`** is drawn in the model as outbound exports for operator tooling, with nothing that talks to an external calendar or channel manager. The book covers what the brick *should* be, an inbound-and-outbound channel layer for multichannel hosts, in [One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync), and treats the outbound export function only as context.
- **HSM `idvr`** has one module in the model. [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) covers it as part of a broader identity model (identity levels across guests, hosts and partner staff) rather than as a separate verification product.
- **TAM `medi`** has no "also" chapter because media is owned in one place. [Describing a Stay: Content, Media and Property Mapping](#content-and-media) links to LISTED's [Photos Sell: Media Pipelines for Listings](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/media-pipeline.html) for the generic pipeline mechanics.

The stress tests in both models (the "residuality" stressors, which ask what the architecture must separate to survive a specific shock) are covered as well:

| Stressor | Model | What it forces apart | Where the book covers it |
| --- | --- | --- | --- |
| `licn` City caps invalidate licenses | TAM and HSM | Property, unit, operator, license, rule version, stay date; bookability as an effective-dated decision | [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) (primary); [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding); [Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model) |
| `insv` A connectivity distributor becomes insolvent | TAM | Inventory assertion, source acknowledgement, property confirmation, traveler contract, merchant of record | [Mapping the Business: Capability Maps for Two Marketplaces](#stays-capability-map) (primary: the separations as a map test); [Built for the Next Disruption: Evolving a Stays Platform Over a Decade](#evolving-the-platform) (traced in the stressor workshop and the combined stressor); [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers) (reservation acknowledgement); [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) (money owed per party) |
| `fire` / `evac` Wildfire closes a destination during active stays | TAM / HSM | Destination operating state; the traveler's commitment as the unit of recovery | [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) (primary); [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) (declared disruption events); [Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability) (disruption mode) |
| `coho` Cities require a locally licensed operating host | HSM (candidate) | Owner, listing controller, licensed operator, co-host, payout beneficiary, tax party as separate roles | [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools) (primary); [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement); [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) |
| `strd` / `midt` Combined stressors | TAM / HSM | Nothing new: survived by composing the residues above | [Built for the Next Disruption: Evolving a Stays Platform Over a Decade](#evolving-the-platform) (stressor analysis; the Algarve combined stressor) |

{id: domain-coverage--the-overlap-matrix}
## The Overlap Matrix

The overlap matrix pairs each TAM brick with its HSM counterpart by meaning and grades the pair. **Same** means the same concept and scope. **Partial** means overlapping responsibility with different scope or granularity: a brick in one model is a module in the other, or the two cover different halves of a job. **Only TAM** and **only HSM** mean the other model has no counterpart. The counts match [Mapping the Business: Capability Maps for Two Marketplaces](#stays-capability-map): 12 same, 15 partial, 7 only TAM, 3 only HSM.

The last column names the chapter whose "Hotels and Homes: Where the Two Marketplaces Differ" section, or main argument, deals with the difference. For "same" pairs it names the chapter that argues what can be shared.

{id: domain-coverage--same-12}
### Same (12)

| TAM | HSM | What still differs | Where it is argued |
| --- | --- | --- | --- |
| `srch` Search, Ranking & Filters | `srch` Search, Ranking & Map Browse | OTA ranking consumes live rates and offer treatments; hosted-stays ranking consumes listing and review quality | [Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture), [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) |
| `prop` Property Detail & Reviews | `list` Listing Detail & Review Trust | Rooms and rate conditions on one side; host reputation and one home on the other | [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) |
| `book` Checkout & Booking Orchestration | `book` Booking & Checkout | Orchestration across partner systems vs trust screening before confirmation | [Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration) |
| `trip` Trip Management & Messaging | `trip` Trip Messaging & Itinerary | Arrival information comes from a front desk vs from a host, often with access codes | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) |
| `reve` Review Collection & Stay Feedback | `grev` Guest Reviews & Re-engagement | One-way verified reviews vs two-sided, double-blind reviews | [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation) |
| `onbo` Partner Onboarding & Verification | `hono` Host Onboarding & Verification | Business identity and property legitimacy vs individual verification and local eligibility | [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding) |
| `cont` Content & Policy Studio | `lista` Listing Authoring & Content | Supplier feeds and descriptive standards vs a person writing about their home | [Describing a Stay: Content, Media and Property Mapping](#content-and-media) |
| `cald` Calendar & Availability Controls | `cala` Calendar & Availability | Counted inventory with restrictions vs one unit, available or not, per night | [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model), [One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync) |
| `perf` Partner Performance Analytics | `host` Host Performance & Earnings | Revenue-manager benchmarks vs earnings and owner reconciliation | [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools), [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence) |
| `paym` Payments & Payouts | `paym` Payments, Taxes & Payouts | Several payment models normalized vs always collected and held until check-in | [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models), [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments) |
| `supp` Customer Support & Recovery | `reso` Resolutions & Support | Relocation and rebooking vs damage claims and disputes between two private parties | [When Something Goes Wrong: Customer Service and Recovery](#customer-service) |
| `mkli` Marketplace Intelligence | `data` Marketplace Intelligence & Experimentation | Partner insight and comp sets vs host insight; same platform mechanics | [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence) |

{id: domain-coverage--partial-15}
### Partial (15)

| TAM | HSM | Nature of the overlap | Where it is argued |
| --- | --- | --- | --- |
| `home` Marketplace Home & Destination Landing | `insp` (part) | HSM merges home and destination entry into one brick and leads with categories | [Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture), [Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels) |
| `dest` Destination Discovery | `insp` (part) | TAM has a destination graph and intent resolution; HSM has destination landing only | [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps) |
| `mapb` Map-Based Stay Browser | `srch` (map module) | A brick in TAM, a module in HSM; homes show an approximate location until booking | [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps) |
| `pers` Personalization & Recommendations | `data` (recommendation layer) | HSM has no traveler-intent model brick | [Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations) |
| `ssav` Saved Searches & Price Alerts | `wish` Wishlists & Sharing | TAM saves a query and watches price; HSM saves listings and shares them with a group | [Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations) |
| `msgc` Guest-Property Messaging | `trip` (messaging module) | A separate service in TAM, a module in HSM; hosted-stays messages carry more trust risk | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) |
| `self` Self-Service Changes & Recovery | `reso` (part) | HSM has no self-service change brick; changes route to resolutions | [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) |
| `invt` Inventory, Rates & Reservations | `cala` (availability only) | TAM's backbone holds rates, availability, reservation state and integrity controls; HSM splits them and has no integrity layer | [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model), [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) |
| `rsrv` Reservation Inbox & Operations | `opco` (part), `trip` | Partner work queue and exceptions vs turnover tasks per reservation | [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools), [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) |
| `prom` Partner Merchandising & Programs | `pric` (discount programs) | Programs that influence visibility vs host pricing rules | [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty) |
| `rate` Rate Recommendation Engine | `pric` (guidance layer) | Advice to a professional revenue manager vs price-setting for an amateur host | [Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing) |
| `rept` Reputation & Quality Operations | `grev` + HSM `trst` (moderation) | TAM has a partner remediation workflow; HSM does not | [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation) |
| `sett` Partner Settlement & Ledger | `paym` (host payout ledger) | A brick in TAM, a module in HSM; commission invoices vs per-booking payouts | [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) |
| TAM `trst` Trust, Verification & Risk Controls | HSM `trst` + `idvr` | Same identifier, different scope: verification and fraud vs screening, protection and incidents | [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety), [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) |
| `conn` Connectivity & Partner APIs | `apix` Partner APIs & Channel Connectivity | Opposite direction: inbound supply from PMS and channel managers vs outbound exports for operators | [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers), [One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync) |

{id: domain-coverage--only-tam-7-and-only-hsm-3}
### Only TAM (7) and only HSM (3)

| Brick | Model | Is the absence on the other side real? | Where it is argued |
| --- | --- | --- | --- |
| `room` Room & Rate Selection | Only TAM | **Real.** In hosted stays the listing is the bookable unit; there is no room-by-rate choice | [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection), [Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model) |
| `deal` Deals and Member Merchandising | Only TAM | **Mostly real.** Member pricing and urgency treatments are OTA levers; hosted stays has host discounts only | [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty) |
| `acct` Traveler Account & Wallet | Only TAM | **A gap in HSM.** A hosted-stays guest needs an account, profile and wallet too | [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) |
| `extr` Partner Extranet | Only TAM | **Different packaging.** HSM spreads host UI across capability bricks; the host app plays the extranet's role | [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools) |
| `medi` Property Media Pipeline | Only TAM | **A gap in HSM.** Hosts upload photos too; the pipeline is shareable | [Describing a Stay: Content, Media and Property Mapping](#content-and-media) |
| `geoa` Geo & Localization Services | Only TAM | **A gap in HSM.** Places, boundaries and localization are needed by both | [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps), [Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability) |
| `idam` Identity & Access Management | Only TAM | **A gap in HSM.** Co-host roles need an access-policy engine, not only a permissions screen | [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) |
| `opco` Turnover & Operations Coordination | Only HSM | **Real.** Hotels run turnover in their own PMS; the marketplace does not | [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools) |
| `coho` Co-host Network & Permissions | Only HSM | **Real, and growing.** Owner–operator splits and delegated roles are a hosted-stays structure | [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools), [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) |
| `comp` Local Compliance & Policy Controls | Only HSM | **A gap in TAM.** An OTA that sells apartments needs the same registration checks | [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) |

The last column separates two kinds of difference. One that the business explains, such as rooms and rate plans or turnover tasks, is a **design input** and survives into the architecture. One that only the model's authorship explains, such as a hosted-stays marketplace without an identity-and-access capability, is **a gap to fill**. [Mapping the Business: Capability Maps for Two Marketplaces](#stays-capability-map) develops that rule; [One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces) applies it to the one-platform-or-two decision.

{id: domain-coverage--domains-the-book-added}
## Domains the Book Added

The digest of the two models lists 27 gaps: capabilities a real stays architecture needs that neither model has as a brick. The book handles them in three ways.

{id: domain-coverage--the-seven-added-domains}
### The seven added domains

Seven gaps are added as **domains in their own right**, marked [ADDED] in the book plan. No single customer journey owns them, so models built from personas and jobs leave them as fragments inside whichever capability needed them first.

| Added domain | Traces in the models | Why the book adds it | Owning chapter | Also |
| --- | --- | --- | --- | --- |
| **Tax engine** | Traveler wants "transparent prices, taxes"; HSM `paym` mentions tax flows; host job "payouts, fees, taxes" | VAT, tourist and occupancy taxes vary by jurisdiction, stay length and property type, and the platform may collect and remit them. That is an effective-dated rules engine with evidence, not a payment module | [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays) | [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) (tax in the displayed price) |
| **Loyalty and member programs** | TAM `acct` "loyalty-adjacent preferences"; `deal` "member programs"; `prom` "member rates" | Tiers, eligibility, benefits and their funding need a ledger and rules, not a merchandising treatment | [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty) | [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) (member identity) |
| **Channel management for hosts** | HSM pro-host ambition that "channel and partner sync becomes easier where appropriate"; `apix` exports only | Multichannel hosts keep one calendar on several platforms through iCal or APIs; this is where double bookings are made or prevented | [One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync) | [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) |
| **Content and property mapping** | Stress-test residues mention "duplicate units" and "inventory mappings" | The same hotel arrives from direct contracts, channel managers, bedbanks and wholesalers; without matching, it appears several times with different rooms and prices | [Describing a Stay: Content, Media and Property Mapping](#content-and-media) | [Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model); LISTED's [One Property, Three Listings: Duplicates and Entity Resolution](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/entity-resolution.html) |
| **Notifications platform** | TAM `trip` hosts "Message and Notification Routing"; `ssav` borrows it; external email and push platforms | One preference-aware, deadline-aware delivery service for confirmations, arrival information, alerts and disruption messages | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) | [Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations) (alerts as a channel) |
| **Distribution and affiliates** | TAM notes on demand APIs "for ecosystem partners"; metasearch named only as a discovery channel | Metasearch, affiliates, travel agents and corporate-travel tools are a product with their own APIs, price-accuracy duties and commission rules | [Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels) | [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine) (metasearch price accuracy) |
| **Customer data platform and consent** | A consent-record data asset with no owning brick in either model | Consent, profile unification and audience building need one owner; otherwise every surface stores its own consent | [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence) | [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) (traveler profile) |

{id: domain-coverage--gaps-covered-inside-existing-chapters}
### Gaps covered inside existing chapters

Seventeen other gaps are covered inside a chapter whose main subject is something else.

| Gap in both models | Covered in | How |
| --- | --- | --- |
| Property, unit and room-type catalog (system of record) | [Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model) | Property, room type, unit and listing as one model for both marketplace types |
| Rate plan and offer model | [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model), [Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts) | Rate plans, derived rates and restrictions; the offer as an aggregate |
| Reservation system of record | [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle), [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) | One owner for reservation state and its events; one reservation record that survives an oversell or a relocation |
| Fees and total-price calculation | [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection), [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) | Total price display and drip-pricing rules; fees in the rate model |
| Third-party supply sourcing (bedbanks, wholesalers, GDS) | [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers), [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine) | Supply-in distribution; availability for supplier pull models |
| Metasearch integration | [Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels), [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine) | Price feeds and live queries; price accuracy |
| Partner account and entity hierarchy | [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding), [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) | Legal entities, contracts and chains at onboarding; partner role model |
| Sponsored visibility and advertising | [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking), [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty) | Program-driven visibility, labeling and ranking transparency |
| Currency, FX and multi-currency pricing | [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments), [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation), [Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability) | Presentment vs settlement currency; FX gains and losses; currency display |
| Translation and localization | [Describing a Stay: Content, Media and Property Mapping](#content-and-media), [Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability) | Machine translation of content and reviews; localization at scale |
| Availability and price cache for search | [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine) | Cache design, staleness and price accuracy |
| Damage deposits, protection program and claims ledger | [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents), [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments) | Protection ledger and claims workflow; security deposits and holds |
| Check-in and property access | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging), [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools) | Arrival information as a deliverable; access codes and smart locks in host operations |
| Platform regulatory reporting | [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays), [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation), [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence) | Tax-reporting returns for platforms; short-term-rental data sharing; the data side of reporting |
| Data platform (event backbone, lakehouse, features) | [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays), [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence), [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform) | Event contracts and streams; governed metrics and data products; feature platform |
| Fraud and payment-risk separation | [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) | Fraud typology across both sides; booking-time and post-booking decisions |
| Each model's missing bricks (HSM: media, geo, IAM, account, self-service; TAM: turnover, co-hosts, compliance, wishlists) | See "Only TAM and only HSM" above | Each chapter's "Hotels and Homes" section decides whether the absence is real |

The book also adds three things the digest does not list as gaps but that its stress tests and the research require: **journey service-level objectives, degradation modes and cost per booking** ([Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability)); **destination operating state** as a first-class object separate from every listing and booking ([Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents), [Built for the Next Disruption: Evolving a Stays Platform Over a Decade](#evolving-the-platform)); and **model governance** for pricing, ranking, screening and fraud models ([Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform)).

{id: domain-coverage--gaps-the-book-deliberately-does-not-cover}
### Gaps the book deliberately does not cover

Three gaps are left out, or covered only at their boundary, each for the reason given.

| Gap | Treatment | Reason |
| --- | --- | --- |
| **Partner CRM and market management** (account managers, commission negotiation, partner health) | Mentioned where it touches the architecture: account-managed onboarding in [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding), partner insight served to account managers in [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence) | It is a commercial operating domain that is usually bought as CRM software. Its architectural questions (one partner record, one source of commission terms) are answered in the onboarding and settlement chapters |
| **Company accounts, travel policy and invoicing** (managed travel) | Covered only as a distribution channel in [Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels) (corporate travel tools and B2B APIs) and as an invoicing context in [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments) | Managed travel is a business with its own platforms (corporate booking tools, travel-management companies). The TAM authoring notes say it "is not treated as the primary commercial center of gravity", and HSM does not model it. A full treatment would need its own book |
| **Connected trips and packages** (flights, cars, packages) | Only the boundary: package status as an input to cancellation rights in [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) and to checkout disclosures in [Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration) | The book is about stays. Neither model covers other travel products, and the Package Travel Directive matters to a stays platform only through the flag that tells the policy engine a reservation is part of a package |

Neither model has a persona for **connectivity partners** (channel managers and PMS vendors) or for **internal operators** (support agents, trust and safety reviewers, market managers). The book treats connectivity partners as customers in [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers) and internal operators as users of the case and integrity tools in [When Something Goes Wrong: Customer Service and Recovery](#customer-service) and [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety). And neither model has a **host-to-guest review** flow; [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation) covers it as part of the double-blind design.

{id: domain-coverage--how-to-use-this-map}
## How to Use This Map

If you bring a capability map of your own (an enterprise architecture repository, a product-area list or the org chart), use this page to get from it to the chapters in five steps.

1. **Match by meaning, not by name.** For each of your capabilities, find the brick that does the same job, using the "What it is" column. Expect some of yours to match a module rather than a brick: many organizations run "notifications" or "settlement" as a team while the models bury them inside another capability.
2. **Read the primary chapter first, then the "also" chapters.** The primary chapter owns the terms and the architecture. The "also" chapters show how other domains depend on the capability, which is usually where interface disputes start.
3. **For each capability you run for both hotels and homes, read the overlap row.** If the pair is *same*, the named chapter argues what to share. If it is *partial*, read its "Hotels and Homes" section before you merge anything. If it exists on one side only, decide which of the two kinds of absence it is: real, or a gap in how your map was drawn.
4. **Check the added domains against your map.** If your map has no owner for tax calculation, notifications, consent, content mapping, loyalty, host channel management or distribution, the corresponding chapter explains why the capability needs one. These are the capabilities most often found scattered across several teams.
5. **Run the stressors.** Take the five stressor rows and ask whether your architecture keeps the listed concepts apart. If removing a listing deletes the reservations attached to it, or a distributor's failure erases a reservation's history, start with the chapter named for that stressor.

The rest of the Reference section turns the map into working tools: [Field Kit: Templates for the Stays Architect](#toolkit) has the templates (including a two-marketplace capability map), [Glossary: The Language of Stays Marketplaces](#glossary) defines the terms each chapter owns, and [Bibliography: Sources and Evidence](#bibliography) lists the sources behind them.

{id: domain-coverage--sources-and-evidence}
## Sources and Evidence

{id: domain-coverage--company-engineering-and-investor-sources}
### Company engineering and investor sources

- None are cited directly on this page. Company-specific statements are made, with dated sources, in the chapters the tables point to.

{id: domain-coverage--standards-regulation-and-documentation}
### Standards, regulation and documentation

- *Travel Accommodations Marketplace* Productscape domain model (`productscape-examples/_config/product-domains/marketplaces/travel-accommodations-marketplace/`), the author, version 1.0, 2026: brick inventory, groups, modules, personas, stressors `licn`, `fire`, `insv`, `strd`.
- *Hosted Stays Marketplace* Productscape domain model (`productscape-examples/_config/product-domains/marketplaces/hosted-stays-marketplace/`), the author, version 1.0, 2026: brick inventory, groups, modules, personas, stressors `licn`, `evac`, `coho`, `midt`.
- BOOKED book plan and chapter contracts (`PLAN.md`), 2026: the "Domains" field of each contract and the [ADDED] markings.

{id: domain-coverage--research-and-practitioner-sources}
### Research and practitioner sources

- Productscape digest for BOOKED (`_research/productscape-digest.md`), 21 October 2026: the complete inventory (§3), the overlap matrix (§4), the 27-row gap list (§5) and the residuality synthesis (§10).
- Barry M. O'Reilly, *Residues: Time, Change, and Uncertainty in Software Architecture*, Leanpub, 2024: the residuality method behind both models' stressors.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
