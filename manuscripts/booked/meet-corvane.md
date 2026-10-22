{id: meet-corvane}
# Meet Corvane: Two Marketplaces, One Group

![Meet Corvane: Two Marketplaces, One Group — logo](stays-marketplace-architecture/posts/meet-corvane/assets/images/meet-corvane/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Meet Corvane Group, the fictional travel group this book follows: its two marketplaces and two supporting businesses, its 2026 volumes, its 2027 systems landscape, the people who run it, the problems it starts 2027 with, the One Stay program approved to solve them, the named group platforms the chapters introduce, and the recurring worked examples whose numbers every chapter shares.

> **WHY THE BUSINESS CARES:** Corvane earns €1.692 billion a year from two different ways of selling a night's stay, plus software and payments around them. Its owners want the merchant share, the hosted-stays business and the margin to grow at once, and the group pays for most of its capabilities twice.

> **WHY ARCHITECTS SHOULD CARE:** Corvane's difficulty is not size; it is that the two marketplaces hold the truth about availability, money and trust in different places. Three clouds, two monoliths, two identity systems and two trust stacks must converge without forcing a hotel and a home into one supply model, and that is the Chief Architect's problem in miniature.

> **KEY POINTS:**
>
> * **Corvane is a fictional composite, not a disguised company.** It borrows patterns common in European travel groups so the book can show real architectural tensions with consistent numbers. Roomstead is not a disguised Booking.com or Expedia, and Nookaway is not a disguised Airbnb or Vrbo; every name, figure, system and event on this page is invented.
> * **One group, two marketplace types.** Roomstead copies the truth about rooms and rates from 640,000 properties' systems and earns mostly agency commission; Nookaway holds the truth about 1.15 million homes itself, holds the guest's money until after check-in and earns split fees. The same words, "available" and "booked", mean different machinery in each.
> * **One Stay shares contracts and platforms, not supply engines.** The €145 million program (2027–2030) builds one identity, ledger, trust, messaging, support, tax and data layer, and one offer and reservation contract across both brands, while Roomstead keeps its room-type inventory and Nookaway its one-unit calendar; Keystone's reservation module is to be retired by the end of 2029.

> **[FAILURE PATTERNS THIS SECTION ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **The Hotel-Shaped Home** — in early 2027 a Roomstead team proposed loading Nookaway's listings into Tally as one-unit room types, and the group rejected it before One Stay was approved.
> * **The Double-Booked Night** — 47% of Nookaway's multichannel listings sync by iCal only, and the Seville double booking is what that looks like for one family.
> * **Phantom Availability** — Roomstead's metasearch price accuracy was 91% in 2026 against a 97% target, mostly because its price cache was stale.

This book tests its argument against **one fictional travel group, detailed enough to be realistic and consistent enough to be followed across fifty-one chapters.** A toy booking site, one hotel table and a search box, is too simple to show why the hard decisions are hard; a real company's internals cannot be verified and its choices do not transfer. This page is the group's reference. The failure patterns of [Overbooked: Sixteen Ways Stay Platforms Go Wrong](#where-stay-platforms-go-wrong) appear here as Corvane's 2027 problems, and every chapter from Part I on opens with a scene whose people, systems and numbers come from this page.

**Corvane Group is fictional.** It is a composite of *patterns* common in the travel industry: an agency-model hotel site that later added merchant payments, a hosted-stays marketplace bought rather than built, a channel manager acquired from the supply side, a payments institution created to hold guests' money, and private-equity owners who want growth and efficiency together. It is **not a portrait of any real company**. **Roomstead and Nookaway are not disguised versions of Booking.com, Expedia, Agoda, Airbnb, Vrbo or anyone else**: they carry none of those companies' documented systems, program names, fee levels or history, and their fees were set so that they match no real platform. The vendor products Corvane runs are real; its use of them is invented. Real companies appear in this book under their own names, with dated sources, and never as Corvane.

{id: meet-corvane--the-group-at-a-glance}
## The Group at a Glance

Corvane is a privately held travel group headquartered in **Lisbon** since 2021, owned by two private-equity funds (together a majority) and Roomstead's founders. Its engineering hubs are in **Dublin** (Roomstead), **Lisbon** (Nookaway and group functions), **Barcelona** (search, data and machine learning, or ML), **Kraków** (payments and platform) and **Utrecht** (Corvane Connect).

| Measure (fiscal 2026 = calendar 2026) | Value |
| --- | --- |
| Revenue | **€1.692 billion** |
| Adjusted EBITDA | about **€410 million** |
| Employees | about **6,800**, of whom about **2,300** in product and technology, including about **1,750 engineers** |
| Shared group services | Corvane Payments with its Fathom ledger, and group finance on SAP S/4HANA. Nothing else of substance |

The last row is the reason One Stay exists: beneath two brands that sell a night's stay to the same European travelers, the group runs two of almost everything.

![Two mirrored buildings labeled Roomstead and Nookaway, each with its own identical identity, trust, search and support machines under three clouds, sharing only a thin Corvane Payments base.](stays-marketplace-architecture/posts/meet-corvane/assets/images/meet-corvane/00-two-of-almost-everything.jpeg)

**Figure 1:** *Beneath two brands that sell a night's stay to the same European travelers, Corvane runs two of almost everything on three clouds; payments is one of the few things already shared.*

{id: meet-corvane--how-corvane-came-to-be}
## How Corvane Came to Be

Corvane's history is fictional, but its shape follows the industry's, whose documented history is in [Two Marketplaces for a Night's Stay: OTAs, Hosted Stays and How They Grew](#two-stay-marketplaces).

| Year | Event |
| --- | --- |
| **2001** | Roomstead is founded in Dublin as a hotel-booking site on the agency model: the guest pays at the property and Roomstead invoices commission. |
| **2004** | Keystone, Roomstead's core application, is rewritten in Java on Oracle. It still owns reservations, partner contracts and commission invoicing in 2027. |
| **2012** | Nookaway is founded in Lisbon as a hosted-stays marketplace. |
| **2020** | Nookaway launches a partner API for property-management systems (PMS) and channel managers. Roomstead launches its paid visibility program, **Front Row**. |
| **2021** | Corvane Group is formed, acquires Nookaway and moves its headquarters to Lisbon. |
| **2023** | Corvane Payments B.V. is founded; the Fathom ledger build starts. |
| **2024** | Corvane Payments is licensed as an electronic money institution (EMI) by De Nederlandsche Bank. Roomstead launches merchant bookings, "Pay with Roomstead". Corvane buys the Utrecht channel manager ChannelPier, rebranded Corvane Connect in 2025. |
| **20 May 2026** | The EU Short-Term Rental Regulation applies. |
| **January 2027** | Mariana Costa joins as Group Chief Architect. |
| **April 2027** | The board approves the **One Stay** program. |
| **End of 2029** | Target date to retire Keystone's reservation module. |

Each phase left a layer: an agency-era reservation model in an Oracle monolith, a merchant product on top of it, an acquired hosted-stays platform on another cloud, and a channel manager that also sells to Corvane's competitors.

{id: meet-corvane--two-marketplaces-four-businesses}
## Two Marketplaces, Four Businesses

The two marketplaces differ in who supplies the stay, where the truth about availability lives and how money moves. [Two Marketplaces for a Night's Stay: OTAs, Hosted Stays and How They Grew](#two-stay-marketplaces) owns the definitions; this book calls Roomstead an **accommodation marketplace** (OTA-style, after the online travel agency) and Nookaway a **hosted-stays marketplace**.

| Brand | What it is | Business model | 2026 revenue |
| --- | --- | --- | --- |
| **Roomstead** (founded 2001, Dublin) | Accommodation marketplace: hotels, B&Bs, hostels and guesthouses, plus apartments and holiday homes mostly from professional managers | **Agency** for **70%** of room nights (guest pays at the property; Roomstead invoices commission); **merchant** for **30%** through "Pay with Roomstead" (Corvane Payments charges the guest and pays the property, mostly by virtual card), target 40% by end 2028 | **€1.200B**: agency commission €860M, merchant margin €270M, partner programs and advertising €70M |
| **Nookaway** (founded 2012, Lisbon; acquired 2021) | Hosted-stays marketplace: whole homes, apartments and private rooms run by individual hosts and professional managers | Facilitated payments: the guest pays Nookaway through Corvane Payments at booking or with Pay Later; the host is paid **48 hours after scheduled check-in**. Split fee: guest service fee **12%** of the subtotal (nights plus cleaning) and host fee **4%**; PMS-connected professional managers may choose a **host-only fee of 17%** | **€430M** |
| **Corvane Connect** (ChannelPier, acquired 2024; rebranded 2025; Utrecht) | Channel manager and connectivity SaaS for **14,500** hotels and **8,200** vacation-rental managers with **96,000** units; distributes to **60+ channels**, including Roomstead's and Nookaway's competitors | SaaS subscriptions | **€62M** |
| **Corvane Payments** (founded 2023) | Corvane Payments B.V., an EMI licensed by De Nederlandsche Bank in 2024, passported in the European Economic Area (EEA); UK through a partner | Processes all Nookaway payments and Roomstead merchant bookings; issues virtual cards to hotels through a partner bank; holds guest funds until payout; margin reported in the brands' revenue | (internal) |

The three revenue lines add up to €1.692 billion: Roomstead about 71%, Nookaway 25% and Corvane Connect 4%.

Four features of the portfolio recur through the book.

- **Roomstead is an agency business learning to be a merchant.** In Pay with Roomstead, Corvane Payments acts as the property's **limited payment collection agent**: the property remains the supplier of the stay and issues the guest's VAT invoice, and Corvane Payments is merchant of record for every collected booking in the group ([Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models)).
- **Nookaway holds the money and the trust.** It holds the guest's payment until after check-in, makes about **6.3 million** payouts a year in 19 currencies, and runs **Nookaway Cover**: host damage protection up to **€500,000**, liability insurance up to **€1 million** through an insurance partner, and a guest guarantee to rebook or refund if check-in fails or the home is materially not as described ([Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents)).
- **Corvane Connect must stay neutral.** It sends its hotels' rates to Roomstead's competitors, so since **May 2027** a neutrality rule makes it an ordinary partner of Switchyard, Roomstead's connectivity gateway, with no private endpoints and no Roomstead access to its data on other channels ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers)).
- **Realized take rates differ from the headline.** Roomstead takes about **13%** of stayed booking value. Nookaway's split is 16% on paper but about **14.4%** realized, after long-stay reductions, fee credits, refunded fees and guest-guarantee costs ([Liquidity, Take Rates and Look-to-Book: The Economics of Stays Marketplaces](#stays-marketplace-economics)).

Each brand also has named products the chapters use. Roomstead has **Roomstead Circle** (three tiers; Circle rates funded by partners, Circle credit funded by Roomstead), **Front Row** (paid visibility at +2, +4 or +6 commission points), **Rate Insights** (rate recommendations in the extranet, launched 2025) and **Perks** (its coupon and campaign service). Nookaway has **Smart Rate** (automatic pricing, rule-based from 2022 and ML-based from 2025), **Pay Later** (launched October 2026) and **Hearth**, a quarterly host credential. All are fictional; none is a renamed real program.

{id: meet-corvane--volumes-every-design-is-sized-against}
## Volumes Every Design Is Sized Against

2026 figures, rounded.

| Metric | Roomstead | Nookaway |
| --- | --- | --- |
| Supply | **640,000** bookable properties: 205,000 hotels and similar, 435,000 apartments and homes (about 70% from professional managers); supply 68% in Europe; **41** languages, **52** currencies | **1.15 million** active listings in **31 countries** (Europe and the Mediterranean, plus Brazil and Mexico); **610,000** hosts, 82% with one listing; professional managers (five or more listings) hold 44% of listings |
| Volume | **109 million** room nights booked, **34%** canceled, **72 million** stayed; about **45 million** reservations made and **30 million** stayed, 2.4 room nights each | **21 million** nights stayed; about **6.9 million** reservations made and **6.0 million** stayed, 3.5 nights each; **13%** of reservations canceled |
| Price | average daily rate (ADR) **€128**; stayed booking value about **€9.2 billion** | average **€142** a night including cleaning; booking value about **€2.98 billion** |
| Supply integration | **82%** of hotel room nights arrive through **140 certified connectivity partners**; 18% are managed in the **Partner Hub** extranet; Corvane Connect serves 21% of connected Roomstead hotels | **61%** of listings are also sold elsewhere: 47% of those sync by iCal only, 53% through PMS or channel-manager APIs; iCal imports polled every **3 hours** by default |
| Traffic | about **650 million** ARI (availability, rates and inventory) messages a day, peak **38,000/s**; about **1,400 shopping requests** per gross reservation, each making about ten price-cache reads: **21,000** reads/s on average, **64,000/s** at the 2026 peak | about **420** search requests per gross reservation, 85% from Nookaway's own web and apps |
| Booking behavior | median booking window **18 days**; metasearch price accuracy **91%** (target 97%) | median booking window **41 days**; instant book on **68%** of listings, the rest request-to-book with a 24-hour response window and **79%** host acceptance |

Two cautions. The 1,400 counts **shopping requests**; the per-second figures are price-cache reads, about ten per request ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)). And ratios carry more architecture than totals: Roomstead earns about €40 per stayed reservation after paying about €13 to acquire it, largely through metasearch, so a stale price costs it money every hour; Nookaway earns about €72 and barely uses metasearch ([Liquidity, Take Rates and Look-to-Book: The Economics of Stays Marketplaces](#stays-marketplace-economics)).

{id: meet-corvane--the-systems-landscape}
## The Systems Landscape

The 2027 baseline estate is the product of that history, with only payments and finance shared.

![Roomstead lane with hotels feeding Switchyard, Tally and Pricegrid; Nookaway lane with hosts feeding the Almanac calendar, which exchanges iCal with other platforms; both lanes sit on Corvane Payments and group finance.](stays-marketplace-architecture/posts/meet-corvane/assets/images/meet-corvane/00-corvane-2027-baseline.jpeg)

**Figure 2:** *Corvane's 2027 baseline: Roomstead copies room-type truth in from hotels' systems through Switchyard into Tally and Pricegrid; Nookaway holds one calendar per home in Almanac and exchanges iCal with other platforms; only Corvane Payments and group finance sit beneath both.*

| Area | Roomstead | Nookaway | Corvane Connect | Corvane Payments |
| --- | --- | --- | --- | --- |
| Core application | **Keystone**: Java monolith (since 2004) on Oracle in co-located data centers in Dublin and Frankfurt; about **180 services** on AWS (eu-west-1, eu-central-1, EKS) built since 2018 | **Burrow**: Python/Django monolith (since 2012) on PostgreSQL, Google Cloud europe-west1; about **60 Go services** on GKE | .NET on Microsoft Azure (West Europe), SQL Server | Kotlin services on AWS (eu-central-1) |
| Inventory and calendar | **Tally**: ARI store on Cassandra (2016), per room type, rate plan and date | **Almanac**: calendar service on PostgreSQL, one row per listing per night | Channel-manager inventory store | — |
| Availability and price | **Pricegrid**: precomputed price-and-availability cache (Java, Redis plus in-process caches), refreshed from Tally change events | Computed at query time from Almanac and pricing rules | — | — |
| Search | Elasticsearch 8 (self-managed) for content; Pricegrid joined at query time | OpenSearch on GKE | — | — |
| Connectivity | **Switchyard**: OpenTravel XML and Roomstead JSON APIs for ARI, content and reservations | iCal import and export; partner API (2020) | 60+ channel APIs | — |
| Payments and ledger | Agency commission invoicing in Keystone; merchant flows through Corvane Payments | All flows through Corvane Payments | Card on file for SaaS billing | **Fathom**: double-entry ledger (PostgreSQL, 2023–24); **Adyen** as primary acquirer; virtual cards through a partner issuing bank |
| Trust and safety | Payment-fraud team and rules engine; partner-account security team | Trust platform: reservation screening, listing verification, Cover claims | — | Transaction monitoring for anti-money-laundering (AML) |

Identity, experimentation (Trialroom and Flipside), warehouses (Snowflake and BigQuery), event buses and customer-service tools are duplicated in the same way. Three facts in this landscape shape most of the book.

- **Keystone still owns Roomstead's commitments.** Reservations, partner contracts, commission invoicing, reviews, the extranet's web module and the checkout module that creates the reservation live in one Java application on Oracle, with a manually failed-over standby last rehearsed in 2025 ([Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability)). Every One Stay contract that touches a Roomstead reservation goes through Keystone until 2029.
- **Two inventory engines encode two truths.** Tally holds about **5.8 million** active products (room type × rate plan); Almanac about **840 million** listing-nights. Roomstead answers shopping from a precomputed cache and pays in staleness; Nookaway computes at query time and pays in latency ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model), [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)).
- **Three clouds, by acquisition.** A group platform must work across AWS, Google Cloud (Nookaway, one region) and Azure (Corvane Connect), or be reached through a bridge.

{id: meet-corvane--the-people}
## The People

Each person owns something the architecture depends on, and most of the book's tensions are between their legitimate goals. All are fictional.

| Name | Role | What they own and want |
| --- | --- | --- |
| **Mariana Costa** (she/her) | Group Chief Architect | The book's point of view. Joined in **January 2027** from a payments company; co-proposed One Stay; chairs the architecture forum; owns the capability map, the context map and the contracts stewardship group. Has influence, not command, over the brands. |
| **Daniel Okonkwo** (he/him) | Group CEO | Asked in February 2027 why the group runs two marketplaces on two platforms. |
| **Tobias Lindqvist** (he/him) | Group CTO | Co-proposed One Stay; chairs the group architecture board. |
| **Marco Bellini** (he/him) | Group CFO | Group finance, indirect-tax rule content, Tier 1 metric approval, recovery approval limits. |
| **Aisha Rahman** (she/her) | VP Supply and Connectivity, Roomstead | Roomstead's supply and connectivity; signed the Brightwell Beds bedbank deal; co-owner of the capability map. |
| **Rafael Mendes** (he/him) | VP Engineering, Nookaway | Burrow, Almanac and Threadline; co-owner of the capability map. |
| **Leila Haddad** (she/her) | Head of Payments and Finance Engineering, Corvane Payments | Fathom, the payment-arrangement resolver, Levy and payments reconciliation. |
| **Jonas Weber** (he/him) | Head of Search and Ranking (group-wide from 2027) | Both search stacks, ranking, Waypoint, the Trip Intent Service; declares degradation modes. |
| **Sofia Marín** (she/her) | Director of Trust and Safety | Group-wide from April 2027; Warden and Vouch. |
| **Kenji Arai** (he/him) | Head of Data and ML Platform | Warehouses, the metric layer, the model platform behind mapping and screening. |
| **Noor van Dijk** (they/them) | Head of Regulatory Affairs and Privacy | The obligation register and market rules; mandatory reviewer of display and cancellation policy. |
| **Elena Petrova** (she/her) | VP Customer Service | Contact centers and vendors; product owner of Harbor. |
| **Priyanka Shah** (she/her) | Head of Product, Corvane Connect | Connect's product, which must live with the neutrality rule. |

The recurring partners and guests are fictional too:

- **Duarte Silva** (he/him), revenue manager of **Hotel Miradouro** in Lisbon, an independent 84-room four-star hotel on Corvane Connect and a cloud PMS, sold on Roomstead and other OTAs. It sells six room types and, in early 2027, 37 rate plans forming 168 products ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model)).
- **Carmen Ruiz** (she/her), a Nookaway host since 2019 with a two-bedroom apartment in Triana, Seville, also listed on a competing platform by iCal: usually **€110** a night, **€260** during the Feria de Abril, cleaning fee **€60**.
- **Hotel Prinsenkade**, an independent 140-room hotel in Amsterdam connected to Roomstead through a third-party channel manager.
- **Ivan Horvat** (he/him), a Nookaway host with a four-bedroom villa near Dubrovnik.
- **The Novak family** from Prague: Tomáš (he/him) and Jana (she/her) Novak and their children, aged 9 and 12.

Chapters add smaller fictional partners: **Hotel Torre de Ferro** in Porto and **Maré Alta Stays** in the Algarve ([From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding)), **Costa Keys** in Málaga ([Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model)), **Alfama Keys** in Lisbon ([Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools)), the bedbank **Brightwell Beds** ([Describing a Stay: Content, Media and Property Mapping](#content-and-media)) and the fake manager **Turia Homes** ([Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety)).

{id: meet-corvane--the-problems-corvane-starts-2027-with}
## The Problems Corvane Starts 2027 With

When Mariana arrives, both marketplaces work and the group is profitable, but its duplication grows faster than the business. Six problems define her starting position; each is an instance of a pattern from [Overbooked: Sixteen Ways Stay Platforms Go Wrong](#where-stay-platforms-go-wrong).

1. **Two of almost everything.** Two identity systems, trust stacks, search engines, experimentation platforms, warehouses and customer-service tools, on three clouds. Posed in [Mapping the Business: Capability Maps for Two Marketplaces](#stays-capability-map) and [Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts); worked in [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access), [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety), [When Something Goes Wrong: Customer Service and Recovery](#customer-service) and [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence).
2. **Roomstead's prices drift from reality.** Metasearch price accuracy is 91% against 97%, and Pricegrid staleness is the main cause. *(Phantom Availability, Price Drift.)* Worked in [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine) and [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection).
3. **Nookaway sells the same night twice.** About 3,100 calendar-conflict host cancellations in 2026, 78% of them on iCal-only multichannel listings. *(The Double-Booked Night.)* Worked in [One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync) and [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity).
4. **Regulation arrives city by city.** The EU Short-Term Rental Regulation has applied since 20 May 2026, Spanish registration rules have already forced listing removals, and the VAT in the Digital Age (ViDA) package makes platforms the deemed VAT supplier of most short-term rentals from dates between 1 July 2028 and 1 January 2030, at each member state's choice. *(City-by-City Firefighting, The Tax Patchwork.)* Worked in [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) and [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays).
5. **Merchant growth on agency rails.** Roomstead's move toward 40% merchant bookings runs through Keystone's agency-era reservation model. *(Ledgerless Money.)* Worked in [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models), [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) and [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation).
6. **Keystone owns the commitments.** The Java and Oracle monolith still owns Roomstead's reservations, partner contracts and commission invoicing. Worked in [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle), [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays) and [Changing the Engine in Flight: Modernizing a Live Stays Marketplace](#modernizing-a-live-marketplace).

None of these is a technology problem alone. The price drift exists because fees, taxes and currency are composed in several places; the double bookings because a home sold on two platforms has no single calendar anyone controls; the merchant problem because a reservation record designed when Roomstead never touched the money now has to say who holds it.

{id: meet-corvane--the-one-stay-program}
## The One Stay Program

In **April 2027** Corvane's board approved **One Stay**, on a proposal from Tobias Lindqvist and Mariana Costa: **€145 million** over three years (2027–2030), with a target to retire Keystone's reservation module by **the end of 2029**. Its scope has three tiers.

- **Shared:** Corvane ID (one identity across brands), payments and ledger (already shared, to be extended), one trust platform, one messaging and notifications platform, one data platform and metric layer, one customer-service platform and one tax engine.
- **Shared contracts, separate engines:** a common **offer** and **reservation** contract across both marketplaces. Roomstead keeps Tally and Pricegrid for room-type inventory; Nookaway keeps Almanac for one-unit calendars. The argument is made in [One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces).
- **Not shared, for now:** supply models, connectivity (Switchyard and Nookaway's partner API) and ranking models.

The principle behind the tiers came out of a rejected proposal. In early 2027 a Roomstead supply team proposed loading Nookaway's listings into Tally as one-unit room types and retiring Almanac. It was rejected because Roomstead's 435,000 homes are mostly professional supply that behaves like hotels, while Nookaway's are mostly individual hosts whose calendar is the product ([Two Marketplaces for a Night's Stay: OTAs, Hosted Stays and How They Grew](#two-stay-marketplaces)). **Share what the guest and the money see; keep apart what the supply sees.**

![A three-tier stack: Roomstead and Nookaway on top, one shared contracts band in the middle, and below it separate Tally and Almanac engines beside one block of shared group platforms.](stays-marketplace-architecture/posts/meet-corvane/assets/images/meet-corvane/00-one-stay-in-one-picture.jpeg)

**Figure 3:** *One Stay in one picture: the brands keep their products and their supply engines, both speak one offer, reservation and place contract, and the platforms beneath the contracts are built once for the group.*

Contract and boundary changes go to the **architecture forum**, chaired by Mariana weekly since February 2027; funding, disputes and accepted risks go to the monthly **group architecture board**, chaired by Tobias ([Who Owns What: Organizing Engineering for Stays](#organizing-stays-engineering)). A **contracts stewardship group** in the Group Chief Architect's office owns the offer, reservation and payment-arrangement schemas, but no engine. The capability map behind the board proposal (v1, presented to the forum on 23 March 2027) counted **48** level-2 capabilities: **16** shared engines, **6** shared contracts and **26** brand-specific ([Mapping the Business: Capability Maps for Two Marketplaces](#stays-capability-map)); the December 2027 annual review adopted v2 with **49**: 23, 6 and 20 ([One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces)). The context map of **5 May 2027** drew **23** bounded contexts: 12 shared, 4 shared contracts and 7 per marketplace ([Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts)). The largest budget lines are contracts, Stayline and Keystone retirement (**€34 million**) and the data, ML and experimentation platforms (**€29 million**).

Most decisions created the named platforms of the next section. Five others recur: the **checkout attempt contract** of February 2027, one server-minted idempotency key at every hop ([Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration)); the **price-composition and display policy** decision of March 2027, after which both brands show the all-in stay total from September ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection)); the June 2027 **search decision**, one query contract over separate indexes and rankers ([Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture)); **Ranking Policy v1**, live in EEA markets on 12 October 2027 ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)); and the **Keystone Exit Plan** of 20 December 2027, which moves Roomstead's future reservations to Stayline in market cohorts during 2029 ([Changing the Engine in Flight: Modernizing a Live Stays Marketplace](#modernizing-a-live-marketplace)).

{id: meet-corvane--the-group-platforms-the-chapters-introduce}
## The Group Platforms the Chapters Introduce

One Stay's shared layer is built chapter by chapter, and each piece has a fictional name.

| Name | What it is | Owner; status | Chapter |
| --- | --- | --- | --- |
| **Corvane ID** | One identity core with separate brand accounts; cross-brand linking only by the person | Group identity team, Kraków; approved June 2027, rollout 2028–2029 | [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) |
| **Fathom** | Double-entry ledger; settlement ledger of record for both brands from May 2027 | Leila Haddad; Nookaway balances move in by end Q2 2028 | [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) |
| **Levy** | Group tax engine: rules, tax party registry, jurisdiction resolver | Leila Haddad's team, rule content under Marco Bellini; first release Q4 2027 | [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays) |
| **Plumbline** | Reconciliation service beside Fathom: card-level, business-to-ledger and safeguarding | Leila Haddad's team; built May–October 2027 | [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation) |
| **Gauge** | Group metric layer: metrics as code, 24 Tier 1 metrics reconciled to Fathom | Kenji Arai with Marco Bellini; approved July 2027 | [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence) |
| **Warden** | Group trust platform: entity graph, policy registry, decisions, enforcement, one case tool | Sofia Marín; approved 17 August 2027, first release Q4 2027 | [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety) |
| **Vouch** | Group review service with per-brand policies and one review event log | Sofia Marín; approved 18 May 2027, Nookaway November 2027 | [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation) |
| **Stayline** | Reservation service: an event-fed tracker first, then system of record | Approved August 2027; Nookaway 2028, Roomstead 2029 | [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) |
| **Clause** | Cancellation policy engine and disruption registry | Group booking platform team, Lisbon; approved July 2027 | [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) |
| **Courier** | Notification platform: intents, channel plans, delivery tracking | Group platform engineering, Kraków; approved 2 September 2027 | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) |
| **Threadline** | Conversation service with one stage-aware message policy | Nookaway engineering; approved 2 September 2027 | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) |
| **Harbor** | Support platform: cases, recovery decisions posted to Fathom, relocation | Elena Petrova; approved June 2027 | [When Something Goes Wrong: Customer Service and Recovery](#customer-service) |
| **Waypoint** | Destination graph and place resolver | Jonas Weber's team; approved June 2027, first release Q1 2028 | [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps) |
| **Place registry** | Property and unit IDs, addresses, jurisdictions, registration numbers; no prices or calendars | Approved 12 May 2027 | [Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model) |
| **Ordinance** | Market policy registry and eligibility evaluator | Noor van Dijk's team and a compliance-platform team; approved 17 March 2027 | [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) |
| **Trip Intent Service** | Shared intent store and alert evaluator under Corvane ID | Jonas Weber's organization; May 2027 | [Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations) |
| **Group event backbone** | Contract-only event backbone on Amazon MSK; brand buses keep ARI and calendar streams | Kraków platform team; approved 15 September 2027 | [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays) |
| **Kiln** | Group ML platform: model registry as serving gate, feature platform, consequence tiers | Kenji Arai's team, Barcelona; approved 21 July 2027 | [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform) |
| **Trialroom** (group) | Roomstead's experimentation platform made the group's, with delayed-outcome metrics | Experimentation Standard v1, 14 September 2027; Flipside retired end Q2 2028 | [Testing Everything: Experimentation Platforms for Stays](#stays-experimentation) |
| **Gangway** | Group partner distribution API on the One Stay contracts | Approved 12 October 2027; replaces Roomstead's affiliate XML API by end 2028 | [Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels) |

Roomstead-only services also recur: **Turnstile**, the checkout API in front of Keystone ([Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration)); **Concord**, the property and room mapping service, whose matching engine becomes a group engine from 2028 ([Describing a Stay: Content, Media and Property Mapping](#content-and-media)); **Lantern**, the metasearch integration ([Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels)); **Tideline**, a cancellation-probability model ([Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform)); **Partner Shield**, the partner-account security program ([Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud)); the **offer kernel** that composes fees, taxes, currency and audience for Pricegrid, the metasearch feed and checkout ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)); and **Switchyard**, redesigned after the €12 rate ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers)). **Calendar Sync v2** and **Payment Plans v1** are Nookaway and Corvane Payments programs, not platforms ([One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync), [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments)).

Two places where names meet need care.

- **Vouch and Warden.** Vouch was approved in May 2027 as the review service "in the shared trust platform"; Warden was approved in August as the group trust platform. The record does not say whether Vouch runs on Warden's components.
- **Ordinance, the place registry and Waypoint.** The December 2027 review records the registry (properties and units) and Waypoint (places and destinations) as two components, with Waypoint writing enrichment to registry records and never the reverse; in the glossary, "place" means a Waypoint place. Ordinance evaluates rules against the jurisdictions both carry. The chapters describe dependencies, not a merger.

{id: meet-corvane--the-recurring-worked-examples}
## The Recurring Worked Examples

Eleven stories recur through the book. Their facts never change, so a reader can follow one booking or one incident across many chapters.

**The €12 rate at Hotel Miradouro.** On Tuesday **9 March 2027**, between 07:14 and 07:52 WET, Duarte Silva's bulk rate update for **14–16 May 2027** passed through Corvane Connect, where a decimal-mapping error in a newly mapped rate plan sent **€12.00** instead of €120.00 for "Standard Double – Flexible" to Roomstead and two other channels. **41** Roomstead reservations (**63** room nights) were made in **38** minutes, because the anomaly check compared each rate only with the same plan's previous value, and the plan was new. Roomstead honored all 41; Corvane Connect compensated the hotel 63 × €108 = **€6,804**. Worked in [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers); also in [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model), [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine), [Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts) and [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays).

**The Seville double booking.** On **2 February 2027** at 10:12 CET the Bauer family from Munich booked Carmen Ruiz's apartment on Nookaway for **20–25 April 2027**, Feria week: 5 × €260 + €60 = **€1,360** before guest fees. At 10:40 a booking for 21–24 April arrived on the competing platform, which had last imported Nookaway's iCal export at 10:00; Nookaway's own imports ran at 09:00 and 12:00. Carmen canceled the Nookaway booking at 13:05. The guest guarantee rehoused the Bauers for **€1,780**, Nookaway funded the **€420** difference, and Carmen paid a **€130** host cancellation fee from her next payout. Worked in [One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync) and [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity); the money side is in [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) and [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation).

**King's Day overbooking.** For **27 April 2027**, Hotel Prinsenkade's channel manager queued updates for **47 minutes** during an outage on 26 April, and the hotel ended **9 rooms** oversold across channels. Roomstead customer service relocated **4** walked Roomstead guests to Haarlem and Amstelveen for **€2,150** and recovered **€1,600** from the hotel under partner terms that cap the hotel's liability at €400 per relocated reservation. Worked in [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) and [When Something Goes Wrong: Customer Service and Recovery](#customer-service); also in [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers), [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) and [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement).

**The Spanish registration purge.** Between **February and April 2026**, under the Spanish national registry then in force and regional registration rules, Nookaway removed **6,900** Spanish listings without a valid registration number; **2,900** future reservations with check-in within 30 days were honored and **8,300** later ones canceled with full refunds. On 21 May 2026 Spain's Supreme Court annulled the national registry; regional numbers still apply. The removal is fictional; the annulment is real and sourced in [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation), which works the example; also in [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding) and [Mapping the Business: Capability Maps for Two Marketplaces](#stays-capability-map).

**The Dubrovnik damage claim.** On **14 August 2027** a party took place at Ivan Horvat's villa despite reservation screening. Ivan claimed **€3,800**; after evidence review Nookaway Cover paid **€3,450** and recovered **€900** from the guest. Worked in [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents); also in [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments), [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation) and [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle).

**The extranet phishing wave.** In **November 2027** attackers phished staff credentials at **230** Roomstead partner properties and used in-platform messaging to send fake "payment verification" messages to **4,100** guests. **310** paid the fraudsters; Roomstead reimbursed them **€212,000** (about €684 each). Worked in [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud); also in [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety), [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access), [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging), [When Something Goes Wrong: Customer Service and Recovery](#customer-service) and [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents).

**The 212 duplicate bookings.** On **14 January 2027** a payment-service-provider latency spike made Roomstead's mobile app retry checkout without reusing its idempotency key; **212** duplicate reservations were created, **198** of them with duplicate charges. Worked in [Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration); also in [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity), [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) and [Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability).

**The ATC strike weekend.** On **5–7 June 2027** an air-traffic-control strike over France disrupted travel across Europe. About **17,000** Roomstead and **2,600** Nookaway reservations were affected, and Roomstead received **6,200** cancellation requests in 48 hours. Worked in [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations), which builds Clause from it; also in [Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing), [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging), [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation), [Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability) and [Testing Everything: Experimentation Platforms for Stays](#stays-experimentation).

**The €1.8 million reconciliation gap.** In **Q1 2027** Corvane Payments found **€1.8 million** unreconciled between virtual-card issuing statements and Roomstead merchant reservations, mostly cards charged by hotels for reservations later canceled or modified. Worked in [Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation); also in [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models), [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments), [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) and [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence).

**The Novak family's Lisbon trip.** On **11 February 2027** the Novaks searched for Lisbon, 2–9 August, two adults and two children, and abandoned the search. After a price alert, on **14 February** they booked a Nookaway apartment in Alfama: 7 × **€145** = €1,015 plus **€70** cleaning, a guest service fee of **€130.20** and Lisbon tourist tax of **€56** (€4 per adult per night; children exempt under the age rule Corvane applies, under 13, which [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays) flags for verification), **€1,271.20** in total, **25%** above what the nightly price suggested. The journey runs through [Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations), [Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture), [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps), [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection), [Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration), [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays) and [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging).

**Black Friday 2027.** On **26 November 2027** Roomstead's availability lookups peaked at **96,000** price-cache reads a second, 1.5 times the 2026 peak; Pricegrid's hit rate fell from 94% to 71% and Roomstead ran a planned degradation mode for 40 minutes. Worked in [Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability); also in [Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture), [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty), [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays) and [Testing Everything: Experimentation Platforms for Stays](#stays-experimentation).

The **Novaks' trip is the guest-side spine**: one booking crosses search, maps, alerts, price display, checkout, tax, messaging and payout. The **€12 rate is the supply-side spine**: one decimal error crosses connectivity, inventory, pricing, delivery and settlement. Between them they show each marketplace failing in its own way: the hotel's truth copied in wrong, the guest's price composed in too many places.

Smaller stories belong to the chapters that introduce them: the **Spain and Portugal metasearch downgrade** of May 2027 ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)), the **Semana Santa declines** of Pay Later charges ([Paying for a Future Night: Payment Orchestration for Stays](#stay-payments)), the **review-trading ring** ([Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation)), **Turia Homes** on both brands ([Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety)), **Hotel Miradouro's missing reservations** in July 2027 ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)), the **check-in instructions that never arrived** in August 2027 ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging)), **Smart Rate on the strike weekend** ([Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing)), the **Autumn Cities coupon** ([Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty)), the **two definitions of "booking"** ([Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence)), the **free-cancellation badge** experiments ([Testing Everything: Experimentation Platforms for Stays](#stays-experimentation)) and Nookaway's stretched **"Lisbon"** ([Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps)).

{id: meet-corvane--how-the-chapters-use-corvane}
## How the Chapters Use Corvane

Each chapter opens with a 2027 scene at Corvane, then answers its question with concepts, dated public evidence from real marketplaces and a Corvane worked example. [Part IX — LEADERSHIP: The Chief Architect's Agenda](#part-9) follows One Stay as a program, through [One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces) to [Built for the Next Disruption: Evolving a Stays Platform Over a Decade](#evolving-the-platform); the case studies of [Part X — PRACTICE: How Others Built It](#part-10), starting with [Booking.com: Experimentation, Connectivity and the Agency Model at Scale](#case-booking-com), leave Corvane and test the book against the public record.

Three conventions hold throughout. **Corvane is always labeled fictional** the first time it appears in a chapter. **Its facts come from one canonical record**, so the 91%, the 3-hour iCal poll and the €1,271.20 mean the same thing everywhere. And a chapter that needs a new detail adds it without contradicting what is established here.

With the group, its problems and its program introduced, Part I begins where Mariana began in February 2027: with the CEO's question of whether Roomstead and Nookaway are one business or two, and why the answer decides the architecture. Continue with [Part I — MARKETPLACE: The Business of a Night's Stay](#part-1).

{id: meet-corvane--sources-and-evidence}
## Sources and Evidence

{id: meet-corvane--company-engineering-and-investor-sources}
### Company engineering and investor sources

- None. Corvane Group, its brands (Roomstead, Nookaway, Corvane Connect, ChannelPier, Corvane Payments), their products and programs, its systems, people, partners, guests, figures and events are fictional and invented for teaching; they are not drawn from any single real company.

{id: meet-corvane--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2024/1028 on data collection and sharing relating to short-term accommodation rental services](http://publications.europa.eu/resource/celex/32024R1028), European Parliament and Council, 2024 — the EU Short-Term Rental Regulation, applicable from 20 May 2026.
- [Council Directive (EU) 2025/516 (VAT in the Digital Age)](http://publications.europa.eu/resource/celex/32025L0516), Council of the EU, 2025 — the deemed-supplier rule for short-term accommodation, applicable from dates between 1 July 2028 and 1 January 2030.
- The Spanish Supreme Court's May 2026 annulment of the national short-term-rental registry is sourced in [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation).

{id: meet-corvane--research-and-practitioner-sources}
### Research and practitioner sources

- The scenario's shape draws on the generic Productscape reference models summarized in [Mapping the Business: Capability Maps for Two Marketplaces](#stays-capability-map) and on the industry history told, with dated sources, in [Two Marketplaces for a Night's Stay: OTAs, Hosted Stays and How They Grew](#two-stay-marketplaces) and the case studies.

The vendor products named (AWS, Google Cloud, Microsoft Azure, Oracle, PostgreSQL, Cassandra, Redis, Elasticsearch, OpenSearch, Kafka, Amazon MSK, Google Pub/Sub, Azure Service Bus, Snowflake, BigQuery, Adyen, SAP S/4HANA) are real; their capabilities are described, with sources, in the chapters that use them. Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
