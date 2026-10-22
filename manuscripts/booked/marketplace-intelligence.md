{id: marketplace-intelligence}
# 39. Knowing the Marketplace: Data Platform, Metrics and Partner Insight

![Knowing the Marketplace: Data Platform, Metrics and Partner Insight — logo](stays-marketplace-architecture/posts/39-marketplace-intelligence/assets/images/39-marketplace-intelligence/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow the data of a stays marketplace from the tap on a search result to the board pack, the experiment readout, the partner dashboard and the monthly report to a national registry. You will see how event taxonomies, consent, the warehouse, governed metrics, data products and partner insight fit together, and where the two marketplace types need different answers.

> **WHY THE BUSINESS CARES:** Every commercial argument in a stays group, from "bookings grew 9%" to "this hotel should join the visibility program", rests on numbers. When a chief financial officer, a brand general manager and a hotel's revenue manager each hold a different count of last month's bookings, the meeting is spent reconciling figures, not deciding.

> **WHY ARCHITECTS SHOULD CARE:** Metric definitions are business logic that lives in SQL nobody reviews. Ranking labels, experiment verdicts, partner dashboards, tax and short-term-rental reports all read them. Without an owned metric layer and data products with contracts, each consumer copies the logic, and the copies drift.

> **KEY POINTS:**
>
> * **A booking is not one number; it is a family of metrics with a time basis.** Created, net of cancellations in the period, cancellation-adjusted by cohort, stayed and honored are all correct, for different questions. Name the basis in the metric, define each one once, and never add two brands' figures unless they share a definition.
> * **Govern metrics as code with owners, tiers and reconciliation.** A metric layer with reviewed definitions, a registry and a monthly reconciliation of money metrics to the ledger is what lets the board, the experimentation platform, ranking and partner tools read the same numbers. Most of the work is ownership and review. The tooling is the smaller part.
> * **Partner insight is a product with privacy and fairness rules.** Hotels and hosts need numbers that match what ranking and programs used, benchmarks that do not reveal a single competitor, and explanations of what payment changes. Hosts are mostly natural persons, so their data is personal data and their benchmarks need stricter aggregation than hotels'.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **The Unwatched Model** — Ranking, pricing and fraud models train on labels and features computed from metric definitions that nobody owns, so a quiet change in "booking" changes what every model learns.
> * **City-by-City Firefighting** — Activity-data reports to short-term-rental registries are built as one-off exports per country, without reconciliation to the stays the platform actually recorded.
> * **Pay-to-Rank Creep** — Partner dashboards that cannot show what a paid program changed, from the same data ranking used, invite partners and regulators to assume the worst.

Every earlier part of this book produces numbers: the unit economics of [Liquidity, Take Rates and Look-to-Book: The Economics of Stays Marketplaces](#stays-marketplace-economics), the ranking labels of [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking), the partner dashboards of [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools), the activity reports of [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation). This Part VIII chapter is where those numbers get one meaning. Data is plentiful: each reservation lives for weeks or months through modifications, cancellations, staged payments, a stay, a review and a payout, behind hundreds or thousands of searches, price checks and availability lookups. **The data is not scarce. Shared meaning is.** The chapter takes the view of a Chief Architect who has to make one group's numbers agree across two marketplaces that count different things.

The chapter owns three terms: **governed metric**, **data product** and **partner insight**. It builds on the event backbone of [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays) and the reservation contract of [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle), and it supplies the definitions that [Testing Everything: Experimentation Platforms for Stays](#stays-experimentation), [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform), [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) and the partner workspace of [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools) read. It does not re-teach experiment design ([Testing Everything: Experimentation Platforms for Stays](#stays-experimentation)), feature platforms ([Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform)), channel architecture ([Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels)), platform tax reporting under the EU's DAC7 directive ([The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)) or the regulatory map ([Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation)).

{id: marketplace-intelligence--setting-the-scene-at-corvane-two-definitions-of-booking}
## Setting the Scene at Corvane: Two Definitions of "Booking"

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), runs Roomstead, an accommodation marketplace, and Nookaway, a hosted-stays marketplace. In February 2027, a month after she joined as Group Chief Architect, Mariana Costa read the draft of the group's 2026 annual review. Its first page said Corvane had handled **51.0 million bookings** in 2026.

Kenji Arai, Head of Data and ML Platform, traced the number to a sum of two figures never meant to be added:

| Source | Figure | What it counted | Time basis |
| --- | --- | --- | --- |
| Roomstead commercial reporting (Snowflake) | **45.0 million** | Reservations created, including those later canceled | Booking date |
| Nookaway business review (BigQuery) | **6.0 million** | Reservations that reached check-in | Stay date |
| Draft annual review | **51.0 million** | The sum | Mixed |

Neither consistent alternative gave 51.0 million. Counted the Roomstead way, the group created about **51.9 million** reservations (45.0 million plus about 6.9 million at Nookaway, where 13% of reservations are canceled). Counted the Nookaway way, about **36.0 million** reservations were stayed (30.0 million plus 6.0 million). The annual review's number was 42% above the stayed figure and close enough to the created figure that nobody had noticed.

![A jar of apples labeled 45.0 million created and a jar of oranges labeled 6.0 million stayed poured into one mixed jar labeled 51.0 million with a question mark, beside two tidy jars labeled 51.9 million created and 36.0 million stayed.](stays-marketplace-architecture/posts/39-marketplace-intelligence/assets/images/39-marketplace-intelligence/39-adding-different-bookings.jpeg)

**Figure 1:** *Corvane's 51.0 million "bookings" added Roomstead's reservations created to Nookaway's reservations stayed; counted consistently, the group created about 51.9 million reservations and stayed about 36.0 million.*

The cancellation rates had the same problem. Roomstead reported **34%** of room nights canceled, counted by booking cohort; Nookaway reported **13%** of reservations canceled, counted in the period they happened. Both were right, and the group's investor slide put them side by side as if they measured the same thing.

The second case came from a hotel. In June 2027 Duarte Silva, revenue manager of Hotel Miradouro in Lisbon, sent Roomstead three numbers for May 2027, each taken from a Roomstead screen or document:

| Where Duarte looked | May 2027 figure | Definition the producing team used |
| --- | --- | --- |
| Partner Hub, Performance tab | **268** reservations | Created in May for any stay date, including those canceled since |
| Rate Insights, "booked" | **231** reservations | Created in May and not canceled as of 3 June, when the job last ran |
| Commission invoice | **191** reservations | Guests who departed in May, on any booking date |

All three were correct. None was labeled with its basis, so Duarte assumed two were wrong. The case took five support contacts and an account manager's afternoon.

Kenji's inventory found the same pattern everywhere. Roomstead's experimentation platform, Trialroom, judged tests on "bookings" at 24 hours, ignoring later cancellations; Nookaway's Flipside counted only reservations the host had confirmed. Roomstead's ranker had been trained on gross bookings since 2015 ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)). In all, Kenji found **seven** SQL definitions of "booking" in production dashboards and pipelines, **two** of gross booking value and **four** of conversion.

Mariana did not ask the forum which number was right. She asked: **what is a booking, who decides, and how does every number the group produces, for the board, experiments, models, partners and regulators, come from the same definition?**

{id: marketplace-intelligence--the-vocabulary-of-marketplace-intelligence}
## The Vocabulary of Marketplace Intelligence

**Marketplace intelligence** is this book's name for the capability that collects, models and governs a marketplace's data and turns it into reporting, experiment verdicts, model labels and features, partner and host analytics, and regulatory data. In Productscape terms it covers the accommodation model's Marketplace Intelligence and Partner Performance Analytics bricks and the hosted-stays model's Marketplace Intelligence & Experimentation and Host Performance & Earnings bricks. Neither model has a brick for the data platform underneath; this book adds one.

- A **behavioral event** records what a person did in a client: a search, a filter change, a property page view, a tap on a room, a checkout step. It is evidence of intent, collected under consent rules, and it can be lost or duplicated without changing the business.
- A **business event** records a change of state in a system of record: a reservation created, modified or canceled; a payment captured; a payout sent; an availability, rates and inventory (ARI) update accepted. It is a fact. Losing one is an incident ([Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays)).
- An **event taxonomy** (or tracking plan) is the controlled list of behavioral event names, their properties and their meaning, versioned like an API.
- A **governed metric** is a business measure whose definition is written once, as code, with an owner, a grain, a time basis, explicit inclusions and exclusions, a restatement policy and a tier that says who may change it and who may consume it.
- A **metric layer** (also called a semantic layer) is the component that holds governed metric definitions and serves them to every consumer: dashboards, notebooks, the experimentation platform, feature pipelines and APIs.
- A **data product** is a dataset or stream that a named team publishes for others to use, with a schema contract, a freshness and quality objective, documentation, access rules and a support channel. A table that someone else happens to query is not a data product.
- **Partner insight** is the analytics a marketplace gives its supply side, hotels, property managers and hosts, about their own performance, their market and the effect of their choices, computed from the same data the marketplace uses to rank, price and pay them.
- **Attribution** assigns credit for a booking to the channels and touchpoints that preceded it.
- A **customer data platform** (CDP) unifies a guest's profiles and events under consent rules and builds audiences for marketing and personalization.

{id: marketplace-intelligence--the-booking-metric-family}
### The booking metric family

"Booking" names several measures. Each answers a different question and needs a **time basis**: the date that decides which period a reservation counts in.

| Metric | Counts | Time basis | Answers | Typical misuse |
| --- | --- | --- | --- | --- |
| **Reservations created** | Every confirmed reservation | Booking date | Demand and funnel volume | Reported as "bookings" to investors |
| **Net reservations** | Created minus cancellations recorded in the period | Event date | Period volume net of cancellations, restated never | Compared with a cohort figure |
| **Cancellation-adjusted reservations** | Reservations created in a cohort, not canceled by a measurement point (for example check-in) | Booking date, measured later | Real demand from a cohort; experiment outcomes | Read before the cohort has matured |
| **Stayed reservations** | Reservations whose guests checked in and out | Check-out (or check-in) date | Fulfilled business; revenue for agency models | Used to judge a funnel change that will show months later |
| **Honored stays** | Stayed reservations without a property or host cancellation, relocation or material "not as described" case | Check-out date | Supply reliability; ranking labels | Computed separately by ranking and by trust |
| **Room nights / nights** | Any of the above, counted per night (and per room for multi-room reservations) | As the parent metric | Volume weighted by length of stay | Mixed with reservation counts in one ratio |
| **Gross booking value (GBV)** | The money value of any of the above | As the parent metric | Scale, take rate | Compared across companies without reading the definitions |

![A timeline with pins at 14 February, 2 August and 9 August; one suitcase travels along it, filling Created and Net jars in February, a Cohort retained jar at check-in and Stayed and Honored jars in August.](stays-marketplace-architecture/posts/39-marketplace-intelligence/assets/images/39-marketplace-intelligence/39-one-reservation-five-metrics.jpeg)

**Figure 2:** *One reservation, five metrics, three periods. The Novak family's Nookaway booking counts in February as created, in the February cohort once it survives to check-in, and in August as stayed and honored; a dashboard that does not name its basis cannot say which.*

Two public definitions show how much the words hide. Airbnb's 2025 annual report defines Nights and Seats Booked as nights and seats booked "net of cancellations and alterations that occurred in that period", and gives the example that a booking made on 15 February counts in the first quarter while its cancellation on 15 May reduces the second quarter ([Airbnb Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), 2026). Its GBV is "inclusive of host earnings, service fees, cleaning fees, and taxes" on the same basis. Booking Holdings' 2025 annual report defines **gross** bookings as the total dollar value of travel services booked, "generally inclusive of taxes and fees", **net of cancellations** ([Booking Holdings Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), 2026). The word "gross" there means gross of the company's revenue share, not gross of cancellations. Both are *net reservations* on an event-date basis in the table above.

Corvane's own headline GBV is different again. The ledger figures, about **€9.2 billion** at Roomstead (72 million stayed room nights at an average daily rate of €128) and about **€2.98 billion** at Nookaway (21 million stayed nights at €142 including cleaning), are **stayed** values, excluding Nookaway's guest service fee and taxes. A slide comparing Corvane's GBV with a competitor's published GBV would set a stay-basis, fee-exclusive figure against a booking-basis, fee-inclusive one. The comparison is wrong, not just inexact.

The rule I use: **the basis is part of the name.** "Bookings" alone is not allowed in a governed metric. "Reservations created (booking date)", "net room nights (event date)" and "stayed GBV excluding guest fees" are.

{id: marketplace-intelligence--architecture-from-taps-and-reservations-to-governed-numbers}
## Architecture: From Taps and Reservations to Governed Numbers

A plausible reference architecture for a stays group has five layers, each with one owner.

![Clients pass a consent gate and systems of record feed an event backbone into a lakehouse, then owned data products, then a metric layer that fans out to reporting, experiments and partners, while regulatory exports read the data products directly.](stays-marketplace-architecture/posts/39-marketplace-intelligence/assets/images/39-marketplace-intelligence/39-five-layers.jpeg)

**Figure 3:** *Marketplace intelligence as five layers. Behavioral and business events arrive separately, are conformed into owned data products, and every consumer reads metrics from one governed layer; regulatory exports read the data products directly, so that they can be reconciled record by record.*

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Collection and consent gate** | Validate behavioral events against the tracking plan; attach consent state and purpose; drop or degrade events the guest did not consent to | Tracking plan, client SDKs, consent enforcement | Let a product team ship an untracked event name or an event without consent state |
| **Event backbone** | Carry behavioral and business events with ordering and replay ([Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays)) | Topics, schemas, retention | Treat behavioral events as facts that systems of record depend on |
| **Lakehouse** | Store raw events and system-of-record snapshots; build conformed core tables | Storage, compute, access control, lineage | Become a place where business logic is written for the first time |
| **Data products** | Publish owned, contracted datasets: reservation facts, stay nights, place and partner dimensions, partner performance, market demand, activity data | Schema, freshness objective, quality checks, documentation | Change a column's meaning without a new version |
| **Metric layer** | Hold governed metric definitions and serve them to every consumer | Metric registry, review workflow, tiering, reconciliation | Allow a Tier 1 metric to be redefined in a dashboard |
| **Partner insight read model** | Serve precomputed, privacy-checked partner and host analytics to the extranet, the host app and APIs | Aggregation rules, comp-set logic, as-of times | Expose a single competitor's numbers or a metric the partner cannot match to their own records |

Three boundaries carry the design.

1. **Behavioral and business events stay separate until the conformed layer.** A "booking completed" tap is not a reservation; the reservation exists when the reservation service says so. Join the two by reservation ID for funnel analysis. Counting reservations from client events is how dashboards drift from the ledger.
2. **Business logic enters once, in data products and the metric layer.** Dashboards, notebooks and model pipelines call the definitions; they do not copy them.
3. **Partner-facing and regulator-facing outputs are external interfaces**, with the discipline of a public API: versioned, reconciled and explainable.

{id: marketplace-intelligence--behavioral-tracking-and-the-event-taxonomy}
### Behavioral tracking and the event taxonomy

A **tracking plan** settles the conflict between product teams, who want to track freely, and analysts, who need events that mean the same thing next year. Each event has a name from a controlled vocabulary (`search_results_viewed`, `property_viewed`, `room_selected`, `checkout_step_completed`), required properties (search ID, stay dates, party, currency, page position, offer ID and quote ID where they exist), a schema version and an owner. New events go through review like an API change, and the collection gate rejects events that do not match.

Stays tracking has four specific needs:

- **Carry the stay context on every event.** Destination, dates, length of stay and party size change what a search means: a view of a Lisbon apartment for 2–9 August for four people is a different signal from the same view for one night in November.
- **Carry the offer and quote identifiers.** The price a guest saw is a quote from the price-composition service ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection)). Logging its ID, not a copy of the price, lets analysts join what was shown to what was charged, and measures **Price Drift** directly.
- **Separate machine traffic.** Metasearch price queries, affiliate API calls, crawlers and scrapers dominate request counts on an OTA. Roomstead serves about **1,400 shopping requests** per gross reservation across all channels, about 300 of them on its own web and apps ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)). Conversion computed over all of them is meaningless. Classify traffic at collection, and keep the classification as a dimension, not a filter someone forgets.
- **Plan for volume and cost.** Agoda described in 2023 a two-step logging design in which client libraries write analytics events to local disk and a forwarder owned by the Kafka team ships them, at around **1.8 trillion events per day**, with costs attributed to owning teams by bytes produced ([Agoda Engineering, 2023](https://medium.com/agoda-engineering/how-agoda-manages-1-8-trillion-events-per-day-on-kafka-1d6c3f4a7ad1); the current design is not public beyond a 2025 update of over 3 trillion records a day). The point that travels is the cost attribution: behavioral events are a stays group's largest data stream, and without a bill per producer nobody deletes an event.

{id: marketplace-intelligence--consent-as-data}
### Consent as data

In the EU, storing or reading information on a guest's device needs the guest's consent unless it is strictly necessary for the service requested (ePrivacy Directive Article 5(3), as amended by [Directive 2009/136/EC](http://publications.europa.eu/resource/celex/32009L0136), 2009). The General Data Protection Regulation (GDPR) then requires a lawful basis and a purpose for each processing of personal data ([Regulation (EU) 2016/679](http://publications.europa.eu/resource/celex/32016R0679), 2016). For a gatekeeper, the Digital Markets Act adds a ban on combining personal data across its services without consent (Article 5(2), [Regulation (EU) 2022/1925](http://publications.europa.eu/resource/celex/32022R1925), 2022). Booking.com was designated a gatekeeper for its online intermediation service on 13 May 2024 (European Commission press release IP/24/2561, 2024).

Architecturally, consent is **data that travels with the event**, not a banner. The collection gate stamps every event with the consent state and the purposes it permits (measurement, personalization, advertising), and the lakehouse enforces purpose-based access: a marketing audience job cannot read events whose consent excludes advertising. Withdrawal applies forward and to stored profiles, which works only if events carry a stable, pseudonymous identifier the deletion process can find.

Two consequences follow for the metric layer. Behavioral metrics are computed on a **consented subset**, so funnel rates are estimates, and the consented share must be monitored. And **business metrics never depend on behavioral consent**: Tomáš Novak, who declined marketing cookies on Roomstead's website ([Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations)), is invisible to Roomstead's funnel analysis, but his family's Nookaway reservation is in every booking metric.

{id: marketplace-intelligence--the-lakehouse-and-the-conformed-core}
### The lakehouse and the conformed core

The storage choice matters less than the modeling discipline above it, as two recent public accounts show.

- In October 2026 Booking.com described migrating about **80–90 PB** (excluding replication) from its on-premises Hadoop 2 estate to the **Booking Data Exchange (BDX)**, whose data lakes run on AWS S3 and Snowflake, in one year, and deliberately leaving about **110 PB** of raw data behind. ([Booking.com Engineering, 2026](https://medium.com/booking-com-development/how-we-migrated-europes-largest-data-lake-on-time-and-without-turning-the-lights-off-61ee8a07db76)). Two details are worth copying: it migrated in waves, with intermediate tables copied so that teams could move independently, and it treated deletion as part of the migration.
- In 2026 Airbnb's data-warehouse team described how it modeled three products (Homes, Experiences and Services): each data domain was either "completely separate by product type or completely monolithic". Product-facing domains chose separate tables; cross-cutting domains such as customer support chose one model, because "a monolithic model was the only way to maintain a single, unified view of a user's support history" ([Airbnb Tech, 2026](https://airbnb.tech/uncategorized/scaling-beyond-one-how-airbnb-evolved-its-data-architecture-for-a-multi-product-world/), airbnb.tech date).

Airbnb's rule maps directly onto a two-marketplace group. **Supply-shaped domains stay per brand**: Roomstead's room-type and rate-plan facts and Nookaway's listing-night facts have different grains ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model)). **Guest-shaped and money-shaped domains are shared**: the guest, the reservation contract, payments, payouts, support cases and trust cases. The conformed core therefore has a small set of shared tables keyed by group identifiers (Corvane ID, the place registry's property and unit IDs, the shared reservation ID) and per-brand supply tables that join to them.

{id: marketplace-intelligence--governed-metrics-and-the-metric-layer}
### Governed metrics and the metric layer

Airbnb described **Minerva** in 2021 as its metric platform and "single source of truth for analytics, reporting, and experimentation", holding more than **12,000 metrics** and **4,000 dimensions** from more than **200 data producers** ([Airbnb Tech Blog, 2021](https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70); as described in 2021, the current state is not public). In August 2026 Booking.com described a semantic layer built on Snowflake semantic views so that definitions "like 'active booking' or 'gross revenue'" stay consistent across every dashboard, with changes to definitions and to expert-verified queries going through a merge request that needs two approvals ([Booking.com Engineering, 2026](https://medium.com/booking-com-development/beyond-the-dashboard-accelerating-real-time-intelligence-in-the-age-of-ai-6f1f0f9c123f)). Booking.com's motive was an AI agent that answers business questions in plain language. An agent that writes its own SQL over raw tables reproduces the seven definitions of "booking" faster; one that reads governed definitions does not.

The definition card I would require for a governed metric:

| Field | Example: stayed room nights |
| --- | --- |
| Name and basis | Stayed room nights (check-out date) |
| Owner | A named person in the finance data team, not a channel |
| Grain and dimensions | Reservation-night; brand, market, place, property or listing, channel, payment arrangement |
| Inclusions and exclusions | Includes relocated guests at the receiving property; excludes no-shows, test bookings, staff bookings |
| Source data products | Reservation facts, stay-night facts |
| Restatement policy | Restated for 90 days after period end, then frozen; later corrections booked in the current period |
| Tier and consumers | Tier 1: board, investor reporting, partner invoices, regulatory reports |
| Reconciliation | Monthly to the ledger's stay-based revenue recognition within a stated tolerance |
| Change process | Owner plus finance controller approval; consumers notified; old version kept for comparison |

Tiers make governance livable. **Tier 1** metrics leave the company: board and investor figures, partner invoices and dashboards, regulatory reports. They change rarely and only with the finance owner's approval. **Tier 2** metrics drive internal decisions: experiment outcomes, ranking labels, operational dashboards. Domain teams own them under review. **Tier 3** is exploration; it is welcome in notebooks and forbidden on partner, board and regulator surfaces.

**Reconciliation makes a metric layer credible.** Money metrics computed from reservation data must agree with the ledger, and in a stays group each difference is a real problem: virtual cards charged for canceled stays, commission invoiced on a reservation that changed payment type, guest fees refunded outside the reservation flow. Corvane Payments, not the data platform, found the **€1.8 million** gap of Q1 2027 ([Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation)); a metric layer reconciled monthly to Fathom, Corvane's ledger, would have shown the drift in its first month.

{id: marketplace-intelligence--attribution-without-self-deception}
### Attribution without self-deception

Attribution in stays has three complications that general e-commerce mostly avoids.

- **Long, multi-session journeys.** The Novak family searched on 11 February 2027, abandoned, received a price alert on 13 February, and booked on 14 February ([Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations)). Last-click attribution credits the alert, though Jana's first search came from elsewhere and Tomáš's cookieless Roomstead session is invisible.
- **Cancellations change the value of the credit.** A channel that brings refundable bookings that later cancel looks better on reservations created than on stayed reservations. Judge paid channels on cancellation-adjusted value, from the same booking metric family.
- **Metasearch is both a channel and a price-accuracy test.** At Roomstead, paid search and metasearch bring **38%** of sessions. The click arrives with the price the metasearch partner showed; attribution and price-accuracy monitoring ([Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels)) should share the same click and quote records.

My recommendation is to keep three kinds of evidence and not confuse them: **rule-based attribution** (last click, position-based) for daily channel operations; **modeled attribution** for budget planning; and **incrementality from holdouts and experiments** as the truth the other two are calibrated against. Nookaway's permanent **5%** alert holdout is that kind of design. [Testing Everything: Experimentation Platforms for Stays](#stays-experimentation) owns the methods; this chapter makes all three read one definition of the outcome.

{id: marketplace-intelligence--data-products}
### Data products

Data products are the units of ownership the metric layer reads. A plausible set for a stays group, owned by the domain that produces the facts:

| Data product | Grain | Owner | Main consumers | Freshness objective |
| --- | --- | --- | --- | --- |
| **Reservation facts** | Reservation version | Reservations domain | Metric layer, finance, trust, service | Minutes |
| **Stay nights** | Reservation-night | Reservations domain with finance | Metrics, tax, regulatory exports, partner insight | Daily |
| **Offer and quote log** | Quote | Pricing and availability | Price-accuracy, attribution, experiments | Minutes |
| **Search and impression log** | Impression | Search and ranking | Ranking training, partner explanations | Hourly |
| **Partner performance** | Property or listing × day | Partner analytics team | Partner Hub, host app, account managers | Daily, with as-of time |
| **Market demand** | Place × stay date × day | Data platform | Pricing, partner insight, forecasting | Daily |
| **Activity data** | Unit × month | Regulatory data team | Short-term-rental registries | Monthly |

The test of a data product is whether a consumer can use it **without talking to the producer**: the schema states meaning, not just types; freshness is published and monitored; quality checks run before publication; breaking changes get a new version with an overlap period; access is granted by purpose. A data product without an owner is where **The Unwatched Model** starts: a ranking label read from a table whose cancellation join someone rewrote without knowing that ranking depended on it ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)).

{id: marketplace-intelligence--customer-data-platform-an-added-domain}
### Customer data platform: an added domain

Neither Productscape model has a brick for consent and profile unification; the consent record in both data catalogs has no owner. Marketing fills the gap by buying a CDP, which becomes a second identity system, a second consent store and a third copy of booking history. I recommend separating the three jobs a CDP bundles:

1. **Identity resolution** belongs to the identity platform ([Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access)), at Corvane Corvane ID. A CDP must not be the place where two accounts become one person.
2. **Consent** belongs to one consent service, stamped on events at collection and read at the point of use, as personalization already does ([Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations)).
3. **Audiences and activation** can live in a packaged CDP or be computed in the warehouse and sent to the notifications platform ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging)) and advertising partners. The warehouse-native option keeps one copy of booking history and one definition of "a guest who booked in the last year"; the packaged one reaches marketers sooner. Either way, audiences are logged, because a guest or a regulator may ask why a message was sent.

{id: marketplace-intelligence--partner-insight-numbers-the-supply-side-can-act-on}
## Partner Insight: Numbers the Supply Side Can Act On

Partner insight is where marketplace intelligence becomes a product that third parties use for money decisions: a hotel sets prices, closures and program participation from it; a host decides whether to accept automatic pricing. It adds three problems of its own: the numbers must match the partner's own systems, benchmarks must not reveal competitors, and explanations must cover what payment changes.

{id: marketplace-intelligence--what-partners-need-and-what-the-industry-shows}
### What partners need and what the industry shows

Public partner tools answer three questions: *how am I doing*, *compared with whom*, and *what should I change* ([Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools) describes the extranet surfaces). Booking.com's Connectivity API list includes Reporting, Property scores and Market Insights APIs alongside rates, availability and reservations ([Booking.com developer documentation](https://developers.booking.com/connectivity/docs), live page as of October 2026), so for professional partners insight is an API, not only a screen. Agoda's Partner Portal, announced on 17 August 2026, includes a comp-set benchmark that flags periods needing attention and AI suggestions up to 90 days ahead ([Agoda, 2026](https://kyodonewsprwire.jp/release/202608174214)). On the hosted-stays side, Airbnb's October 2024 release added price tips "based on similar local listings" and an earnings dashboard with custom reports ([Airbnb, 2024](https://news.airbnb.com/en-uk/airbnb-2024-winter-release-introducing-co-host-network-the-best-local-hosts-to-manage-your-airbnb)).

Regulation now makes partner data access an obligation for the largest platforms. DMA Article 6(10) requires a gatekeeper to provide business users, at their request and free of charge, with "effective, high-quality, continuous and real-time access to, and use of, aggregated and non-aggregated data, including personal data" generated in the context of their use of the platform, with personal data limited to end users' use of that business user's products and subject to consent ([Regulation (EU) 2022/1925, Art. 6(10)](http://publications.europa.eu/resource/celex/32022R1925), 2022). It has applied to Booking.com since its designation; for a smaller marketplace it previews what partners will expect. **INFERENCE, NOT DOCUMENTED:** a gatekeeper meeting Article 6(10) plausibly needs per-partner data products with contracts and consent filters, not exports from a reporting database; Booking.com has not published how it meets the obligation.

{id: marketplace-intelligence--the-architecture-of-partner-insight}
### The architecture of partner insight

![Partner performance, market demand and ranking log feed an insight builder, then privacy checks, then one read model that serves the same chart to the extranet, the API and an account manager.](stays-marketplace-architecture/posts/39-marketplace-intelligence/assets/images/39-marketplace-intelligence/39-partner-insight-pipeline.jpeg)

**Figure 4:** *Partner insight is built from the same data products as internal metrics and ranking, passes privacy and fairness checks before it is stored, and is served from one read model to every partner surface, so a hotel sees the same number on screen, in the API and from its account manager.*

Four rules carry the design.

1. **Every partner metric is a Tier 1 metric with its basis on the screen.** "Reservations created in May (any stay date)", "departed in May" and "not canceled as of 3 June" are three labels and three registry definitions. The invoice metric is the anchor; the others explain how it was reached.
2. **Benchmarks are aggregates with minimum group sizes and dominance limits.** A comp set of four hotels in a small town reveals each competitor's occupancy to the others. The common protections are a minimum number of comparable properties, a cap on any one property's share of the aggregate, and indices or ranges instead of exact values. These rules are partly competition law: showing hotels their competitors' exact future prices risks facilitating coordination, so have competition counsel set the thresholds.
3. **Explanations come from the ranking log, not from a separate model.** "Why am I on page three?" is answered from the features, policy terms and reasons that [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) logged for the property's impressions, summarized into levers the partner controls, with any paid program's effect shown separately. A partner dashboard that cannot show what Front Row changed, from the same log the ranker wrote, invites **Pay-to-Rank Creep** suspicions even when the policy is bounded.
4. **Recommendations are measured like models.** Roomstead's Rate Insights recommendations were accepted **9%** of the time in 2026 ([Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing)). Acceptance, outcome after acceptance and a holdout belong in the model's monitoring, owned by a named team.

{id: marketplace-intelligence--hotels-and-hosts-are-different-data-subjects}
### Hotels and hosts are different data subjects

A hotel's occupancy is commercially sensitive business data. A host's occupancy is **personal data**: Carmen Ruiz's calendar shows when she earns money and, for a home she sometimes lives in, when she is away. Most hosts are natural persons, so GDPR applies to their performance data, to benchmarks built from it, and to anything other hosts see about them. A benchmark that says "listings like yours in Triana earned a median of €260 a night during the Feria" is safe when it aggregates dozens of listings. A benchmark over five two-bedroom apartments on one street is close to publishing five people's income.

The rule I recommend: **hosted-stays benchmarks need larger minimum groups, coarser geography and longer time windows than hotel benchmarks**, and price tips should be built from booked prices of comparable listings over periods long enough that no single booking dominates.

{id: marketplace-intelligence--in-practice-at-corvane-gauge-and-the-booking-family}
## In Practice at Corvane: Gauge and the Booking Family

In July 2027 the group architecture forum approved the metric part of One Stay's "one data platform and metric layer" scope, on a proposal from Kenji Arai and Marco Bellini, the Group CFO. The decisions:

**One definition of the booking family.** The seven production definitions became the family above, each in the registry with a basis in its name. The group's headline volume metrics became **stayed reservations** and **stayed room nights**, because they reconcile to revenue for both the agency and the facilitated-payment models, and **reservations created** and **net room nights** became the leading indicators. The 2026 annual review was corrected before publication: about **51.9 million** reservations created and about **36.0 million** stayed. Cancellation rates are reported on both bases (per reservation and per room night) for both brands, so the 34% and 13% figures stopped appearing side by side.

**One label for honored stays.** The **honored stay**, which [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) uses as its training label and [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety) uses for reliability signals, is defined once in the metric layer, with the joins to cancellation reasons, relocation records and "not as described" cases owned by the data platform.

**Gauge, the metric layer.** Gauge holds metric definitions as code in one repository, reviewed by the metric owner and one platform reviewer. **24** Tier 1 metrics need the approval of Marco Bellini's finance controllers, and their history is restated when the definition changes. Trialroom and Flipside read experiment outcomes from Gauge from Q4 2027, which made the two platforms' readouts comparable while Flipside was being retired under the September 2027 Experimentation Standard v1 ([Testing Everything: Experimentation Platforms for Stays](#stays-experimentation)). Tier 1 money metrics reconcile monthly to Fathom. Fathom's memorandum entries for agency-booking consideration, added for DAC7 ([The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)), give the agency side something to reconcile against.

**One warehouse, two hard boundaries.** Snowflake in an EU region becomes the group warehouse; Nookaway's BigQuery datasets move in waves through 2028, the most-shared data products first, with copies of intermediate tables so that teams can move in their own order (the Booking.com pattern). Two boundaries are written into access control. **Corvane Connect's data is a separate domain**: under the May 2027 neutrality rule ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers)), Roomstead may not see the rates Connect sends to other channels, and group pricing features already exclude Connect data ([Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing)). And **Nookaway host performance data is personal data**, readable only for stated purposes.

**Partner insight on one read model.** The partner analytics read model that the October 2027 workspace decision put on the shared spine ([Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools)) reads Gauge. For Hotel Miradouro, Partner Hub's May 2027 view now shows the three figures with their bases, linked: **268** created, of which **37** canceled by 3 June, giving **231** not canceled; and separately **191** departed in May, which matches the commission invoice line by line. Benchmarks use these illustrative thresholds: hotel comp sets of at least **5** properties with no property above **30%** of the set's room nights, shown as indices; host benchmarks of at least **15** listings, at neighborhood level or coarser, over at least **28** days.

![A dashboard card showing 268 created minus 37 canceled giving 231 not canceled, beside a separate bar of 191 departed linked to a checked invoice.](stays-marketplace-architecture/posts/39-marketplace-intelligence/assets/images/39-marketplace-intelligence/39-miradouro-three-figures.jpeg)

**Figure 5:** *Hotel Miradouro's three May figures, once labeled with their bases, fit together: 268 reservations created, 37 of them canceled by 3 June leaving 231, and 191 guests departed in May, matching the commission invoice.*

**Activity data as a data product.** The EU Short-Term Rental (STR) Regulation requires platforms to send each Member State's single digital entry point, monthly and machine to machine, activity data for units in areas with a registration procedure: per unit, the number of nights rented and of guests per night with each guest's country of residence, with the registration number, address and listing URL ([Regulation (EU) 2024/1028, Arts. 3 and 9](http://publications.europa.eu/resource/celex/32024R1028), 2024; applicable from 20 May 2026). The regulation excludes hotels from its definition of a unit, so at Corvane it covers Nookaway's listings and Roomstead's alternative accommodations in registration areas. In 2026 Nookaway built the first reports as per-country exports from Burrow. Under Gauge they are one data product over **stay nights**, joined to the place registry ([Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model)) for registration numbers and to reservation facts for the guest's country of residence. Each month's export is reconciled to Gauge's stayed nights for the same units before it is sent; corrections after sending (late no-shows, post-stay alterations) follow a documented procedure. A new Member State endpoint is then a new adapter, not a new pipeline, which keeps short-term-rental reporting from becoming **City-by-City Firefighting**. [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) owns the compliance design; this chapter owns the data.

The decision had a cost: the group data platform budget, about **€19 million** in 2026 across Snowflake, BigQuery, tracking and business intelligence (BI) tools, rises during the 2028 migration because both warehouses run in parallel. Kenji's case rested on retiring BigQuery by the end of 2028, deleting behavioral data older than 25 months that no data product reads, and charging storage and compute to owning teams.

{id: marketplace-intelligence--trade-offs}
## Trade-offs

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| **Warehouse** | One group warehouse | Federated warehouses per brand with a shared metric layer over both | Brands share guests, payments and a reservation contract; one team can run it | Brands are being sold or kept at arm's length; data residency or neutrality forbids pooling |
| **Metric ownership** | Central metrics team defines everything | Domain owners define metrics; a central registry reviews and tiers | Few metrics, one business | Many domains; central team would become a queue |
| **Definition storage** | Metric layer as code (semantic layer) | Definitions in BI tool models | Several consumers beyond dashboards: experiments, features, APIs, agents | One BI tool and one consumer |
| **Behavioral collection** | Client-side SDKs | Server-side collection from back-end calls | Need interaction detail (scroll, map moves, hover) | Need completeness and consent control; much traffic is machine traffic |
| **Headline volume** | Booking-basis net reservations (peer-comparable) | Stay-basis stayed reservations (revenue-aligned) | Investor comparability with public peers | Internal performance, partner invoices, regulatory data |
| **Partner analytics freshness** | Daily, with an as-of time | Near real time | Benchmarks, programs, performance trends | Operational views: today's arrivals, pickup in the last hour |
| **CDP** | Packaged CDP | Warehouse-native audiences | Marketing needs a tool quickly and the warehouse is not ready | One copy of booking history and one consent model matter more than speed |

At group level I would choose a single warehouse, domain-owned metrics with a central registry, metrics as code, server-side collection for anything that feeds a Tier 1 metric, both headline bases with the stay basis internally, daily partner benchmarks with real-time operational views, and warehouse-native audiences once the consent service exists. Choose the federated warehouse when a brand may be sold: pooling its data makes a carve-out harder.

{id: marketplace-intelligence--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

The two marketplaces differ in the grain of supply data, the meaning of the metrics and the supply-side data subject; the platform underneath is the same.

| Dimension | Accommodation marketplace (Roomstead) | Hosted-stays marketplace (Nookaway) |
| --- | --- | --- |
| **Core supply fact** | Room night at a rate plan of a room type, often from several suppliers or channels for one hotel | Night on one listing owned by one host |
| **Cancellation and the booking metric** | High: Roomstead cancels **34%** of room nights, driven by refundable rates; cohort maturity takes months | Lower: Nookaway cancels **13%** of reservations; host declines and host cancellations matter as much as guest cancellations |
| **Traffic to clean** | Dominated by metasearch, affiliate and crawler requests; about 1,400 shopping requests per gross reservation | More app and logged-in traffic; less machine shopping |
| **Supply-side data subject** | Mostly businesses; performance data is commercially sensitive | Mostly natural persons; performance and earnings data is personal data under GDPR |
| **Partner insight content** | Comp sets, rate competitiveness, demand, paid-program effect, conversion by room and rate | Earnings, occupancy, price tips, response and review progress toward quality credentials |
| **Benchmark privacy** | Minimum comp-set size and dominance limits; competition law sets the bar | Larger groups, coarser geography and longer windows; privacy and competition law both apply |
| **Regulatory data** | Hotels outside STR activity data and mostly outside DAC7 (entity sellers above 2,000 rentals per listing are excluded) | Almost every listing in registration areas reports activity data; almost every host is a DAC7 seller |
| **What can be shared** | Platform, metric layer, tracking plan, consent, data-product standards, partner insight read model | The same |

**Judgement: share the platform and the definitions, not the supply metrics.** One warehouse, one metric layer, one tracking plan and one partner insight read model serve both marketplaces, and the booking family is defined once for both. Supply-shaped metrics, such as rate-plan mix and room-type pickup at Roomstead or calendar availability and instant-book share at Nookaway, stay brand-specific because they describe different things. Convergence makes this pressing: Roomstead's 435,000 alternative accommodations already need host-style privacy rules for the individual owners among them, and when Nookaway pilots boutique hotels in 2028, its partner insight will need comp sets.

{id: marketplace-intelligence--failure-modes}
## Failure Modes

- **The silent redefinition** — a "bug fix" to a booking query changes every model label, experiment readout and partner dashboard on the same day, without a version; see Governed metrics and the metric layer, and Data products.
- **Adding numbers with different bases** — Corvane's 51.0 million; name the basis in the metric and have the metric layer refuse to sum metrics with different bases (see The booking metric family).
- **Reading a cohort metric too early** — an experiment that lifts refundable bookings looks like a win at 24 hours and a loss at check-in; state cohort maturity on every cancellation-adjusted metric ([Testing Everything: Experimentation Platforms for Stays](#stays-experimentation)).
- **Benchmarks that identify a competitor or a host** — see The architecture of partner insight; enforce minimum groups and dominance checks in the insight builder, not in the front end.
- **Consent applied at the banner, not at use** — events collected for measurement end up in an advertising audience; see Consent as data.
- **Regulatory exports that do not reconcile** — a registry query cannot be answered; see the activity-data decision in In Practice at Corvane.
- **The everlasting event stream** — behavioral data is kept forever because nobody owns its cost; attribute cost to producers and set retention per event class.

{id: marketplace-intelligence--the-chief-architect-s-view}
## The Chief Architect's View

**Decide** at group level what Corvane decided in July 2027: the booking metric family and the board and investor headline metrics; the tiers and their approvers, with Tier 3 kept off partner, board and regulator surfaces; which domains the warehouse keeps apart (a connectivity business serving competitors; anything that might be sold); one consent service with enforcement at use; the partner insight rules for labels, hotel and host benchmarks, and paid programs; and that regulatory data (STR activity data, DAC7 seller reports, Digital Services Act transparency figures) comes from data products reconciled to Tier 1 metrics.

**Who decides.** The CFO's organization owns Tier 1 definitions, because they must reconcile to the ledger. Domain teams own Tier 2 metrics and their data products. The data platform team owns the platform, the registry and the review workflow, not the definitions. Regulatory affairs and privacy sign off partner benchmarks, consent purposes and regulatory exports. The architecture forum owns the boundaries between brands and between the group and its connectivity business.

**Watch**, every month:

- the number of production definitions of each Tier 1 concept (the target is one);
- the reconciliation gap between Tier 1 money metrics and the ledger;
- the share of behavioral events rejected at the collection gate, and the share of sessions with measurement consent;
- data products missing their freshness objective;
- partner support contacts about numbers, per thousand active partners and hosts;
- regulatory exports reconciled before sending, and corrections sent after;
- data platform cost per stayed reservation, by brand.

**Long term.** AI agents answering business questions and regulators asking for per-unit and per-seller data will keep adding consumers. A group with one governed layer meets each with a new consumer; a group with scattered SQL builds a new project each time.

{id: marketplace-intelligence--questions-to-ask}
## Questions to Ask

1. How many definitions of "booking", "GBV" and "conversion" exist in production today, and who owns each?
2. Does every booking metric name its time basis, and does anything prevent two brands' figures with different bases from being summed?
3. Which metrics leave the company, to the board, investors, partners or regulators, and who must approve a change to them?
4. Do Tier 1 money metrics reconcile to the ledger every month? What was last month's gap?
5. Are behavioral events validated against a tracking plan, stamped with consent purposes, and kept separate from business events until the conformed layer?
6. Can a hotel match every number on its dashboard to its invoice or its PMS, with the basis shown?
7. What are the minimum group sizes for hotel and host benchmarks, who set them, and where are they enforced?
8. Is each regulatory export built from a data product and reconciled before it is sent? How are corrections handled?
9. What does the data platform cost per stayed reservation, and which team pays for each event stream?

A test is only as good as the definition of the outcome it is judged on. [Testing Everything: Experimentation Platforms for Stays](#stays-experimentation) takes the booking family into experiment design, where long booking windows, delayed cancellations and interference between guests competing for the same nights make "did it work?" harder to answer than in almost any other online business.

{id: marketplace-intelligence--sources-and-evidence}
## Sources and Evidence

{id: marketplace-intelligence--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), Airbnb, Inc., 2026: definitions of Nights and Seats Booked and GBV, net of cancellations and alterations in the period.
- [Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), Booking Holdings Inc., 2026: definition of gross bookings, net of cancellations.
- [How Airbnb Achieved Metric Consistency at Scale](https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70), Airbnb Tech Blog, 2021: Minerva as the single source of metrics for analytics, reporting and experimentation; scale figures.
- [Scaling beyond one: How Airbnb evolved its data architecture for a multi-product world](https://airbnb.tech/uncategorized/scaling-beyond-one-how-airbnb-evolved-its-data-architecture-for-a-multi-product-world/), Airbnb Tech, 2026 (airbnb.tech date): separate versus monolithic data models per domain.
- [Airbnb 2024 Winter Release](https://news.airbnb.com/en-uk/airbnb-2024-winter-release-introducing-co-host-network-the-best-local-hosts-to-manage-your-airbnb), Airbnb Newsroom, 2024: price tips from similar local listings; earnings dashboard.
- [How We Migrated Europe's Largest Data Lake](https://medium.com/booking-com-development/how-we-migrated-europes-largest-data-lake-on-time-and-without-turning-the-lights-off-61ee8a07db76), Booking.com Engineering (D. Abrazhevich, K. van Berge Henegouwen), 2026: BDX on S3 and Snowflake, migration in waves, data left behind.
- [Beyond the Dashboard: Accelerating Real-Time Intelligence in the Age of AI](https://medium.com/booking-com-development/beyond-the-dashboard-accelerating-real-time-intelligence-in-the-age-of-ai-6f1f0f9c123f), Booking.com Engineering, 2026: semantic views for consistent business definitions; two-approval change process; verified queries for AI agents.
- [How Agoda Manages 1.8 Trillion Events per Day on Kafka](https://medium.com/agoda-engineering/how-agoda-manages-1-8-trillion-events-per-day-on-kafka-1d6c3f4a7ad1), Agoda Engineering, 2023: two-step logging for analytics events; cost attribution by bytes produced.
- [How Agoda Handles Kafka Consumer Failover Across Data Centers](https://medium.com/agoda-engineering/how-agoda-handles-kafka-consumer-failover-across-data-centers-a3edbacef6d0), Agoda Engineering, 2025: over 3 trillion records a day.
- [Agoda Partner Portal announcement](https://kyodonewsprwire.jp/release/202608174214), Agoda via Kyodo News PR Wire, 2026: comp-set benchmark and AI suggestions for partners.

{id: marketplace-intelligence--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2024/1028](http://publications.europa.eu/resource/celex/32024R1028), on data collection and sharing for short-term accommodation rental services, 2024: activity data, monthly machine-to-machine reporting, hotels outside the definition of unit; applicable from 20 May 2026.
- [Regulation (EU) 2022/1925](http://publications.europa.eu/resource/celex/32022R1925), Digital Markets Act, 2022: Article 5(2) on combining personal data; Article 6(10) on business users' data access.
- [Regulation (EU) 2016/679](http://publications.europa.eu/resource/celex/32016R0679), General Data Protection Regulation, 2016: lawful basis and purpose limitation for guest and host data.
- [Directive 2009/136/EC](http://publications.europa.eu/resource/celex/32009L0136), amending the ePrivacy Directive 2002/58/EC, 2009: consent for storing or accessing information on users' devices (Article 5(3)).
- [Council Directive (EU) 2021/514 (DAC7)](http://publications.europa.eu/resource/celex/32021L0514), 2021: platform seller reporting and the 2,000-rental exclusion.
- European Commission press release IP/24/2561, 2024: designation of Booking as a gatekeeper on 13 May 2024 (as summarized in the book's regulation research brief).
- [Connectivity APIs overview](https://developers.booking.com/connectivity/docs), Booking.com, n.d. (live as of October 2026): Reporting, Property scores and Market Insights APIs for partners.

{id: marketplace-intelligence--research-and-practitioner-sources}
### Research and practitioner sources

- *BOOKED* research briefs on platform, data and ML, and on host and partner tools (October 2026), and the Productscape digest (bricks `mkli`, `perf`, `data`, `host`; the missing consent and data-platform domains).

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
