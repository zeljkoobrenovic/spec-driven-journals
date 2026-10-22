{id: converging-two-marketplaces}
# 43. One Platform or Two? Converging Hotels and Homes

![One Platform or Two? Converging Hotels and Homes — logo](stays-marketplace-architecture/posts/43-converging-two-marketplaces/assets/images/43-converging-two-marketplaces/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Make the convergence decision for a group that runs both an accommodation marketplace and a hosted-stays marketplace: which capabilities become one engine, which become one contract with two engines, which stay with each brand, how cross-type supply is routed, and in what order the shared core is built. You will follow Corvane as it reconciles eight months of sharing decisions into one register.

> **WHY THE BUSINESS CARES:** Convergence is where a travel group's acquisition logic is either paid back or quietly lost. Two of everything costs money every year, gives guests and regulators two answers to the same question, and lets a fraudster banned by one brand keep selling on the other. Merging the wrong things costs more: a re-platformed brand can lose bookings for a year while its supply model is bent into the other's shape.

> **WHY ARCHITECTS SHOULD CARE:** "One platform" is the most expensive phrase in a group architecture review, because it hides a hundred separate decisions behind one word. The architect's job is to turn it into a register with one grade, one owner and one reason per capability, and to keep that register honest as convergence moves supply across the line.

> **KEY POINTS:**
>
> * **Share what follows the guest, the money and the law; keep what follows how supply is counted.** Identity, payments and the ledger, tax, trust, messaging, support, data and the offer and reservation contracts are the same problem for hotels and homes. Room-type inventory and one-unit calendars, connectivity and ranking models are not, and merging them produces The Hotel-Shaped Home.
> * **Choose the engine by supply segment, the storefront by brand.** A boutique hotel sold by a homes brand belongs on the hotel engine, and a one-unit apartment sold by an OTA needs the hosted-stays integrity posture. The shared contracts are what let one storefront sell offers from either engine.
> * **Govern the shared core as a register, not a slogan.** Every capability carries a grade (shared engine, shared contract, brand-specific), an owner, a reason and a review date. The list will grow as later decisions land; the register is how a group tells deliberate convergence from scope creep.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **The Hotel-Shaped Home** — the "one platform" proposal that loads homes into room types, or flattens hotels into one-unit calendars, is the pattern at group scale.
> * **Policy Spaghetti** — two stacks give the same guest two answers about cancellation, refunds and fees, and a group without shared contracts cannot make them agree.
> * **Trust After the Incident** — separate trust stacks let a fraudster suspended on one brand keep trading on the other until a second incident reveals the link.

Every group that owns both kinds of stays marketplace is eventually asked the same question by its board: **are these one business on two platforms, or two businesses?** The question sounds commercial. It is an architecture question, because the answer decides which systems are built once, which are built twice on purpose, and which team owns the meaning of a night, a price and a refund across the group.

The question has become harder because the categories are blurring. Booking.com reported about **3.9 million** homes and apartments among its roughly **4.4 million** properties at the end of 2025, and alternative accommodations made up about 36% of its room nights ([Booking Holdings Form 10-K for 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), 2026). Airbnb told shareholders in August 2026 that it had added "thousands of boutique and independent hotels" and that hotel nights were growing about three times as fast as homes, from a single-digit share ([Airbnb Q2 2026 shareholder letter](https://s26.q4cdn.com/656283129/files/doc_financials/2026/q2/Airbnb-Q2-2026-Shareholder-Letter-FINAL.pdf), 2026). **Each type now sells the other's supply.** That makes it tempting to conclude that one platform should serve both. The public record, and the argument of this book, say otherwise: the guest-facing commitment converges, and the supply machinery does not.

This chapter owns two terms: the **convergence decision**, the group-level decision per capability and per supply segment about what is built once and what stays separate; and the **shared core**, the set of shared engines and shared contracts every brand must use. It builds on the capability map of [Mapping the Business: Capability Maps for Two Marketplaces](#stays-capability-map) and the context map of [Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts), and it reconciles the "what to share" judgements made in the chapters of Parts II to VIII into one register. Corvane, the fictional travel group this book follows ([Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), supplies the worked example: the One Stay program, approved in April 2027, and its first annual review in December 2027.

{id: converging-two-marketplaces--setting-the-scene-at-corvane-is-this-still-what-we-approved}
## Setting the Scene at Corvane: "Is This Still What We Approved?"

On **8 February 2027** the Group CEO, Daniel Okonkwo, asked Mariana Costa, the Group Chief Architect, for a board pre-read: *"Explain why we run two marketplaces on two platforms. If they are the same business, tell me how to make them one"* ([Two Marketplaces for a Night's Stay: OTAs, Hosted Stays and How They Grew](#two-stay-marketplaces)). A Roomstead supply team had already proposed the simplest answer: load Nookaway's 1.15 million listings into Tally, Roomstead's inventory store, as one-unit room types, and retire Almanac, Nookaway's calendar service. Mariana's capability map, presented to the architecture forum on **23 March 2027**, argued for something else: **16 shared engines, 6 shared contracts and 26 brand-specific capabilities** ([Mapping the Business: Capability Maps for Two Marketplaces](#stays-capability-map)). The board approved the result in April as the **One Stay** program, with a budget of **€145 million** over three years and a target to retire the reservation module of Keystone, Roomstead's Java and Oracle monolith, by the end of 2029.

The board paper summarized the scope in seven lines: one identity, payments and ledger, one trust platform, one messaging and notifications platform, one data platform, one customer-service platform and one tax engine; a common offer and reservation contract with separate engines; supply models, connectivity and ranking models not shared "for now".

Eight months later, on **14 December 2027**, the Group CFO, Marco Bellini, brought a printout to the program's first annual review with the board, where the capability map was reviewed. It listed the shared systems the forum had approved since April, in the order they had arrived: a place registry, a Trip Intent Service and a group review service, Vouch, in May; Corvane ID, the support platform Harbor, the offer kernel, the payment arrangement record and the destination service Waypoint in June; the cancellation policy engine Clause, the group metric layer Gauge and the ML platform Kiln in July; Stayline, the group reservation service, and the trust platform Warden in August; the conversation service Threadline, the notification platform Courier, the event backbone, an experimentation standard that made Trialroom the group platform, and a shared incident record in September; a shared supply-side spine for the partner extranet and the host app in October; per-brand booking risk score models registered in Warden in December. A recommendation from the content team to share five more content services was waiting for a decision ([Describing a Stay: Content, Media and Property Mapping](#content-and-media)).

> *"The board approved seven shared platforms. I count more than twenty names. Either the program has grown without anyone deciding it should, or the seven lines meant something else. Which is it?"*

Rafael Mendes, VP Engineering at Nookaway, had the opposite worry. Each decision had been sensible on its own, but Nookaway's listing model was its product, and he wanted to know where the line now ran and who could move it. Aisha Rahman, VP Supply and Connectivity at Roomstead, added a third question: Nookaway's boutique-hotel pilot was due in 2028, and nobody had decided which engine the hotels would run on.

The questions for the review were therefore not "one platform or two". They were: **what exactly is shared, is the line still where the board drew it, and which engine serves supply that crosses it?**

{id: converging-two-marketplaces--what-the-public-record-shows}
## What the Public Record Shows

No company publishes its convergence decision. Three groups have published enough to show where the line runs in practice.

**Expedia Group consolidated the front end and the platform services, not the supply model.** Expedia's filings say it moved to a platform operating model in 2020, began migrating Brand Expedia, Hotels.com and Vrbo onto "one unified technology front-end infrastructure" in 2021, completed Hotels.com in 2022 and began Vrbo in late 2022 ([Expedia Group Form 10-K for 2022](https://www.sec.gov/Archives/edgar/data/1324424/000132442423000007/expe-20221231.htm), 2023), and "created one unified front-end stack in 2023" ([Form 10-K for 2023](https://www.sec.gov/Archives/edgar/data/1324424/000132442424000007/expe-20231231.htm), 2024). Its 2025 filing says that "all of our transaction-based businesses now benefit from our shared platform infrastructure, including customer servicing and support, data centers, search capabilities, payment processing, and fraud operations", and that One Key, one loyalty program across Brand Expedia, Hotels.com and Vrbo, launched in the US in 2023 ([Form 10-K for 2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm), 2026). The filings say *front-end* stack and *shared platform infrastructure*; they do not say that Vrbo's inventory, pricing or supply systems were merged with the hotel side. Expedia's B2B API still describes Vrbo inventory as "whole property only", "single-unit only" and "a single rate plan", with a separate availability calendar for which "Caching is not supported at this time" ([Expedia Group Rapid, Vrbo integration guide](https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-integration-guide), n.d.).

The consolidation had a documented cost. In May 2024 Expedia's chief executive said that "Vrbo's recovery following the recent re-platforming has been slower than anticipated, which has put pressure on gross bookings" ([Expedia Group Q1 2024 earnings release](https://www.sec.gov/Archives/edgar/data/1324424/000132442424000024/earningsrelease-q12024.htm), 2024). Hotels.com, a hotel brand, had migrated a year earlier without a comparable public warning.

> **INFERENCE, NOT DOCUMENTED:** Expedia has not explained why Vrbo's migration was harder. My reading is that a front end built for hotel shopping carries hotel assumptions (room-and-rate selection, date-first search, hotel content) that a whole-home brand has to work around, and that the smaller, differently shaped brand absorbs the cost when one front end serves both. [Expedia Group and Vrbo: Consolidating Brands Onto One Platform](#case-expedia-vrbo) examines the case in full.

**Booking.com runs homes on its OTA platform and adapts the edges.** Its connectivity documentation shows hosted-stays mechanisms grafted onto hotel inventory: Request to Book gives partners 24 hours to answer, requires requests at least three days before check-in, and in its current version makes partners block and release their own availability while a request is pending ([Booking.com, Request to Book overview](https://developers.booking.com/connectivity/docs/request-to-book/overview), n.d.). Payouts follow the supply type: bank transfer or a virtual card per booking for most partners, and Stripe payouts on the check-in day "only available for Home properties in the US and Canada" ([Booking.com, understanding payouts](https://developers.booking.com/connectivity/docs/payments-by-booking-onboarding-api/understanding-payouts), n.d.). One platform, with the hosted-stays posture added where the supply needs it.

**Airbnb kept the commitment layer product-agnostic when it added new products.** Its data-warehouse team wrote in 2026 that when Services and Experiences arrived, "a domain's data model had to be either completely separate by product type or completely monolithic", while payments, messaging and customer support stayed product-agnostic ([Airbnb Tech Blog, "Scaling beyond one"](https://airbnb.tech/uncategorized/scaling-beyond-one-how-airbnb-evolved-its-data-architecture-for-a-multi-product-world/), 2026). The post describes the offline warehouse, not the online services, but the principle it states is the one this chapter argues: a clean split between what differs by product and what does not.

| Group | What it documents as shared | What its documents show as separate | Lesson |
| --- | --- | --- | --- |
| Expedia Group | Front end (2022–2023), support, data centers, search capabilities, payments, fraud operations, loyalty | Vrbo inventory contract in its B2B API | The guest layer converges; the smaller brand pays for front-end assumptions |
| Booking.com | One platform for hotels and about 3.9 million homes | Request to Book and payout rails added per supply type | One engine can carry professional homes if the edges adapt |
| Airbnb | Payments, messaging, support across Homes, Services, Experiences | Data models per product type where they differ | Decide per domain: fully shared or fully separate, not half of each |

{id: converging-two-marketplaces--concepts}
## Concepts

The decision needs a small vocabulary. The three grades come from [Mapping the Business: Capability Maps for Two Marketplaces](#stays-capability-map); the rest are this chapter's.

| Term | Definition | Corvane example |
| --- | --- | --- |
| **Convergence decision** | The group-level decision, per capability and per supply segment, of what is built once, what is built behind one contract, and what stays with each brand; recorded with an owner, a reason and a review date | The One Stay register |
| **Shared core** | The shared engines and shared contracts that every brand must use; a brand may not build its own copy | Corvane ID, Fathom, Levy, Clause, the offer and reservation contracts |
| **Shared engine** | One implementation, one owner; brand differences are policy data | Warden, the group trust platform, with per-brand detectors and policies |
| **Shared contract** | One schema and one meaning, an engine per marketplace | The offer contract, filled by Pricegrid at Roomstead and by Almanac-based quotes at Nookaway |
| **Supply segment** | A group of supply that shares a source of truth and a unit cardinality: hotels on channel managers, professional homes on property-management systems, individual hosts' homes | Roomstead's 435,000 homes, about 70% from professional managers |
| **Cross-type supply** | Supply of one marketplace type sold by a brand of the other type | Roomstead's apartments; Nookaway's 2028 boutique hotels |
| **Storefront** | The brand-facing surfaces (apps, web, search, ranking, page templates) that present offers to guests | The Nookaway app |
| **Supply engine** | The catalog, inventory and connectivity that produce offers for one supply segment | Switchyard, Tally and Pricegrid; Almanac and Nookaway's partner API |
| **Cross-listing** | A storefront showing offers produced by another brand's supply engine, with the supplier's consent | Nookaway homes in a labeled section of Roomstead results |

Two distinctions matter more than the rest. A **shared engine** is not a shared database: Warden runs on AWS beside Corvane Payments, and Nookaway's booking gate calls it from Google Cloud with a 120-millisecond budget, failing open into post-booking review ([Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety)). And a **brand-specific capability may run on shared components**. Ranking is brand-specific, but its policy layer writes to a shared ranking log; protection is Nookaway-specific, but its claims post to Fathom. The grade records who owns the decision logic, not which infrastructure it touches.

{id: converging-two-marketplaces--architecture-a-shared-core-and-two-supply-engines}
## Architecture: A Shared Core and Two Supply Engines

The reference shape has four layers: brand storefronts on top, shared contracts in the middle, shared engines underneath, and supply engines beside the contracts, one per supply segment rather than one per brand.

![Roomstead and Nookaway storefronts both feed one band of shared contracts, which feeds a hotel engine, shared engines and a unit-calendar engine; the hotel engine connects to channel managers and the unit-calendar engine to hosts.](stays-marketplace-architecture/posts/43-converging-two-marketplaces/assets/images/43-converging-two-marketplaces/43-shared-core-layers.jpeg)

**Figure 1:** *The shared core. Each storefront speaks the shared contracts; each contract can be filled by either supply engine; the shared engines serve both brands. Supply engines are chosen by segment, so the boutique hotels Nookaway sells run on the hotel-type engine.*

{id: converging-two-marketplaces--the-placement-rule}
### The placement rule

[Two Marketplaces for a Night's Stay: OTAs, Hosted Stays and How They Grew](#two-stay-marketplaces) gave a short rule: if a capability's correctness depends on how supply is counted, it belongs to a supply engine; if it depends on who the guest is, what they were promised or who owes whom, it belongs to the shared layer. In a review, I break that rule into four tests, applied in order.

![A decision tree of four questions leading to shared engine, shared contract, supply engine or brand-specific outcomes.](stays-marketplace-architecture/posts/43-converging-two-marketplaces/assets/images/43-converging-two-marketplaces/43-placement-tests.jpeg)

**Figure 2:** *Four tests for placing a capability. One answer for outsiders pulls a capability into the shared core; dependence on supply counting pushes it to a supply engine; brand differentiation keeps it with the brand; everything else is a candidate for one engine.*

The first test is the one most groups skip. A cancellation decision, a tax line, a statement of reasons, a guest's identity level and a host's annual earnings report are all read by people outside the brand: guests, auditors, tax authorities, consumer regulators. When two engines produce them, the group gives two answers, and it is the group that is asked to explain the difference. That is why **Clause**, the cancellation policy engine, became one engine in July 2027 even though Context Map v1 in May had planned one evaluator per engine ([When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations)): every evaluator answered a question that consumers and support staff compare.

The third test keeps supply engines apart. Tally and Pricegrid are built for counted rooms pushed by 140 certified connectivity partners at up to 38,000 messages a second; Almanac holds one row per listing per night and must never sell a night twice. Their write patterns, locking and failure modes differ ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model), [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity)). A shared engine would need both, and in practice gets the larger brand's.

{id: converging-two-marketplaces--what-is-shareable-and-what-is-not}
### What is shareable and what is not

| Area | Share | Do not share | Owning chapter |
| --- | --- | --- | --- |
| Identity | Identity core, sessions, identity levels, policy engine and grant graph | Brand profiles and consents (each brand stays data controller) | [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) |
| Money | Payment orchestration, payment plan, arrangement record, ledger, reconciliation, tax engine | Supplier settlement rails (virtual cards vs payouts), commission invoicing, release policy | [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models), [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) |
| Trust | Decision record, enforcement with receipts, entity graph, case tool, statements of reasons | Detectors, thresholds, the brand's risk posture | [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety), [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) |
| Post-booking | Conversation and notification platforms, trip timeline, support case platform, policy engine | Policy packs, arrival templates, playbooks, host penalty schedules | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging), [When Something Goes Wrong: Customer Service and Recovery](#customer-service) |
| Offer and booking | Offer, reservation and stay-query contracts; price composition rules; display policy | Price caches and quote engines, checkout sagas, page templates' middle | [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine), [Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration) |
| Supply | Unit identity, places, media pipeline, translation, mapping engine, stay-rule vocabulary | Catalogs, rate plans vs listings, inventory stores, connectivity gateways | [Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model), [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers) |
| Discovery | Query contract, filter vocabulary, ranking log and disclosure machinery | Indexes, availability layers, ranking models and policy values | [Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture), [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) |
| Data | Warehouse, metric layer, governed definitions, experimentation and ML platforms, demand signals for pricing | Pricing and ranking models; each brand's experiment defaults | [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence), [Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing) |

Notice what the right-hand column has in common: **trust posture** is not shared even though the trust platform is. Nookaway screens guests before they enter someone's home; Roomstead screens payments. One platform holds both brands' decisions; neither brand gets the other's thresholds.

{id: converging-two-marketplaces--routing-cross-type-supply}
### Routing cross-type supply

The second key point turns into one routing rule: **the supply segment chooses the engine; the brand chooses the storefront, the commercial terms and the policies.** Figure 3 shows the boutique-hotel pilot Nookaway plans for 2028.

![Swimlanes for guest, Nookaway, hotel engine, Stayline and channel manager: a Porto search goes to the hotel engine, room offers come back, the booking becomes a reservation in Stayline and is delivered to and accepted by the channel manager.](stays-marketplace-architecture/posts/43-converging-two-marketplaces/assets/images/43-converging-two-marketplaces/43-boutique-hotel-routing.jpeg)

**Figure 3:** *A boutique hotel sold by the homes brand. The hotel's rooms, rates and delivery run on the hotel-type engine; Nookaway's storefront, terms and money arrangement wrap the offer. No hotel is flattened into a one-unit calendar.*

The same rule works in the other direction. Roomstead's roughly 374,000 single-unit apartments and homes stay on Tally, because most come from professional managers on the same channel managers as hotels, but [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) gives every unit with a count of one the hosted-stays posture: a uniqueness guarantee at commit and no hotel-style walk. **Cardinality and source of truth, not brand, decide the posture.**

{id: converging-two-marketplaces--corvane-worked-example-the-one-stay-register-december-2027}
## Corvane Worked Example: The One Stay Register, December 2027

Mariana answered Marco's question with one claim and one table. The claim: **the seven lines were the board's summary of the capability map, and the map is the decision of record.** Media pipeline and translation, for example, were shared engines on the March map before the board approved the program; they were never in the seven lines because the paper grouped them under "supply". The table: every component the forum had approved since April, placed in a map cell, with the cell's grade before and after.

{id: converging-two-marketplaces--the-register}
### The register

| Component (approved) | Map cell | Grade v1 (March) | Grade v2 (December) | Owner |
| --- | --- | --- | --- | --- |
| Corvane ID (June) | Guest accounts and identity; identity verification | Shared engine | Shared engine | Group identity team, Kraków |
| Supply-party layer (2028) | Party onboarding and verification | Shared engine | Shared engine | Group supply domain |
| Fathom as settlement ledger (May); Plumbline reconciliation service (May–Oct) | Settlement ledger and payouts; refunds and reconciliation | Shared engine | Shared engine | Leila Haddad |
| Payment Plans v1 (Apr–Sept) | Payment orchestration | Shared engine | Shared engine | Leila Haddad |
| Levy (Q4) | Tax engine | Shared engine | Shared engine | Leila Haddad; rules: group tax team |
| Warden (Aug); booking risk scores on Warden (Dec); incident record (Sept) | Fraud and risk screening | Shared engine | Shared engine | Sofia Marín; Kenji Arai for models |
| Threadline, Courier (Sept) | Messaging; notifications | Shared engine | Shared engine | Rafael Mendes (Threadline); group platform, Kraków (Courier) |
| Harbor (June) | Customer service and recovery | Shared engine | Shared engine | Elena Petrova |
| Ordinance, the market policy registry (March) | Local compliance and bookability | Shared engine | Shared engine | Noor van Dijk (rules) |
| Gauge, the group metric layer (July); demand layer (June) | Data platform and governed metrics | Shared engine | Shared engine | Kenji Arai |
| Offer contract, offer kernel, display policy (Mar–June) | Offer and price composition | Shared contract | Shared contract | Contracts stewardship group |
| Payment arrangement record (June) | Payment arrangement | Shared contract | Shared contract | Schema: stewardship group; resolver: Leila Haddad |
| Stayline (Aug) | Reservation record | Shared contract | Shared contract | Stewardship group; Stayline team |
| Stay query contract (June) | Search and filters | Shared contract | Shared contract | Jonas Weber |
| Place registry (May) | Property and unit identity | Shared contract | Shared contract | Group supply domain, Lisbon |
| Clause (July) | Changes and cancellations | Shared contract | **Shared engine** | Group booking platform team, Lisbon |
| Trip Intent Service (May) | Saved intent | Brand-specific | **Shared engine** | Jonas Weber |
| Trip timeline on Stayline events (Sept) | Trip timeline | Brand-specific | **Shared engine** | Nookaway engineering |
| Vouch (May) | Reviews and reputation | Brand-specific | **Shared engine** | Sofia Marín |
| Concord mapping engine (Dec decision) | Content and property mapping | Brand-specific | **Shared engine** | Roomstead supply; model: Kenji Arai |
| Stay-rule vocabulary and evaluator contract | Restrictions and stay rules | Brand-specific | **Shared contract** | Group architecture |
| Experimentation Standard v1 (Sept); Kiln (July) | Experimentation and ML | Brand-specific until 2028 review | **Shared engine** | Kenji Arai |
| Waypoint (June) | Places and destinations **[ADDED v2]** | — | **Shared engine** | Jonas Weber |

The totals moved from **16 / 6 / 26** to **23 shared engines, 6 shared contracts and 20 brand-specific capabilities**, over 49 capabilities. Every move went in the direction [Mapping the Business: Capability Maps for Two Marketplaces](#stays-capability-map) predicted: from brand-specific toward shared, never the reverse. And every new shared engine sits inside one of the board's seven areas or under a shared contract. Vouch was approved inside the trust scope; Trialroom became the group experimentation platform inside the data scope, bringing the 2028 review forward; the Trip Intent Service sits under Corvane ID; Clause, the trip timeline and Stayline hang off the reservation contract. **The program grew in names, not in scope**, with two exceptions the review had to decide on its own: the content services and Waypoint.

![Seven sorting bins each holding several cards, with two cards, Content services and Waypoint, set apart on a side table to be decided separately.](stays-marketplace-architecture/posts/43-converging-two-marketplaces/assets/images/43-converging-two-marketplaces/43-names-not-scope.jpeg)

**Figure 4:** *More than twenty approved names fit inside the board's seven areas or under a shared contract; only the content services and Waypoint needed a decision of their own.*

Twenty capabilities stay with the brands, including ranking, room and rate selection, the unit calendar, connectivity, checkout sagas, the extranet and host app, promotions, loyalty, pricing guidance, protection and claims, and distribution. Many run on shared components (the extranet and host app on the shared spine of Corvane ID grants, exception queues and partner analytics; ranking on the shared policy log; protection on the incident record and Fathom), which is the "brand-specific, on shared components" grade of Figure 2 at work.

{id: converging-two-marketplaces--four-conflicts-the-review-resolved}
### Four conflicts the review resolved

**1. The five content services.** [Describing a Stay: Content, Media and Property Mapping](#content-and-media) recommended sharing the media pipeline, translation, policy rendering, the perceptual-hash index and the mapping engine, "in substance" an addition to One Stay. The review adopted all five but added only one cell. The media pipeline and translation were already shared engines in March. The perceptual-hash index is part of the media pipeline. Policy rendering is not a separate service: cancellation text is rendered from Clause's policy versions and fee text from the display policy service, both already shared. The one real change is the **mapping engine**. The map had marked mapping Roomstead-only, because Nookaway has no multi-supplier problem. The review found that the cross-brand problem is real: professional managers such as Costa Keys sell the same 38 apartments as five room types on Roomstead and as 38 listings on Nookaway ([Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model)), and Warden's entity graph needs to know that a unit on one brand is a unit on the other. Concord's matching engine becomes a group engine from 2028, still built and run by Roomstead supply with the scoring model in Kenji Arai's team; Roomstead keeps its supplier room-mapping workflow for bedbank content.

**2. The place registry and Waypoint.** [Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model) created a group "place registry" on 12 May 2027; [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps) introduced Waypoint, a group place service, in June. Context Map v1 already listed them as two shared contexts, and the review confirmed **two components with one dependency direction**:

| | Place registry | Waypoint |
| --- | --- | --- |
| Answers | What physical supply exists, and exactly where? | Which places exist in the world, and what is inside them? |
| Holds | Property and unit IDs, addresses, exact geocodes, registration numbers, jurisdictions as written by enrichment | Destination graph, boundaries, names, search areas per brand, jurisdiction zones |
| Owner | Group supply domain, Lisbon | Jonas Weber's group search team |
| Writes to the other | Never | Enrichment: cells, place IDs, public point, jurisdictions on each registry record |
| Never does | Create a place or a search area | Store a unit, a licence or an owner |

The name is the problem. In the registry, "place" means a property or unit; in Waypoint it means Lisbon or Alfama. The forum kept the registry's name because services already referenced it, and fixed the vocabulary instead: in the glossary, a **place** is a Waypoint place, and the registry's records are **properties and units**.

**3. Stay rules.** [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) argued for one restriction vocabulary and one stay-evaluator contract, with an implementation per engine and a shared conformance suite. That is a shared contract in all but name, and the map's "brand-specific" grade had been written before the argument was made. The review changed the grade; the stores stay separate.

**4. Cancellation policy.** Clause, a single engine approved in July, superseded Context Map v1's "one evaluator per engine, one vocabulary". The review recorded the change on both maps rather than leaving the older one to mislead the next reader.

{id: converging-two-marketplaces--three-things-the-review-declined}
### Three things the review declined

A register is as useful for what it refuses. The review turned down three proposals.

- **A group ranker for cross-brand results.** Federated search shows Nookaway homes in a labeled section of Roomstead results and the reverse, and a team proposed one model to merge them. The rankers' scores are not calibrated against each other, and a merged list would decide which brand's supply wins a position inside a ranking function ([Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture)). Ranking stays brand-specific; the sections stay separate.
- **Moving Roomstead's homes onto Almanac.** A Nookaway team proposed migrating Roomstead's single-unit apartments to the unit calendar. Most are professional supply on the same channel managers as hotels, and the hosted-stays guarantee they need comes from the allocation ledger beside Tally ([Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity)), not from a different store. Moving them would have forced every manager onto a second integration.
- **Group-wide loyalty.** [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty) recommends making Roomstead's marketplace-funded Circle credit group-wide once Corvane ID is live, but only if enough guests use both brands. The identity baseline found about 2.4 million people with the same verified e-mail on both brands ([Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access)); how often they book both, and whether credit would change that, can be measured only after guests link their accounts under Corvane ID from 2028. The cell stays brand-specific with a review date.

{id: converging-two-marketplaces--the-cross-type-supply-decision}
### The cross-type supply decision

Aisha's question got a written rule. **Nookaway's 2028 pilot sells boutique hotels on the hotel-type engine**: hotels connect through Switchyard and certified channel managers, their room types and rates live in Tally, their offers come from Roomstead's price composition in the shared offer contract, and Stayline delivers their reservations with the same acknowledgement rules as any Roomstead hotel ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)). Nookaway owns the storefront, the ranking, the page (a rooms table, because templates follow offer shape, as [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) requires), the reviews policy on Vouch and the commercial terms. The money is a new combination of known fields on the arrangement record, facilitated collection with virtual-card settlement ([Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models)), and fraud controls combine Roomstead's partner-account protections with Nookaway's payment policy ([Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud)). The pilot opens in Lisbon, Porto and Seville in 2028 with independent hotels of up to 40 rooms that already sell on Roomstead and opt in.

Rejecting the alternative was easy once it was written down. Putting eight identical rooms into Almanac would create eight competing listings or a new pooled shape that Almanac does not have ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model)), and each hotel's channel manager would need a second integration to a calendar API it was not built for.

![Left: a hotel's eight rooms split into competing calendar cards. Right: the same rooms grouped as one room type on the hotel engine, shown in a homes storefront.](stays-marketplace-architecture/posts/43-converging-two-marketplaces/assets/images/43-converging-two-marketplaces/43-hotel-on-the-right-engine.jpeg)

**Figure 5:** *Putting eight identical rooms into a one-unit calendar would create eight competing listings; the hotel-type engine sells them as one room type behind the homes brand's storefront.*

{id: converging-two-marketplaces--the-budget-and-the-order}
### The budget and the order

The €145 million was allocated to workstreams in April and reaffirmed in December. Contracts carry the largest share because every other workstream depends on them.

| Workstream | € million (2027–2030) | Main deliverables |
| --- | --- | --- |
| Offer and reservation contracts, Stayline, Keystone reservation retirement | 34 | Contracts, kernel, Stayline as system of record, Clause |
| Data, ML and experimentation platforms | 29 | Metric layer, one warehouse, Kiln (€8.5 million), Trialroom as group platform |
| Trust platform | 16 | Warden, booking risk score models, Vouch, incident record |
| Payments and ledger extension | 15 | Fathom settlement, reconciliation service, Payment Plans |
| Corvane ID | 13 | Identity core, grants, migration of three account bases |
| Customer service | 11 | Harbor, contact-driver taxonomy, desktop migration |
| Messaging and notifications | 8 | Threadline, Courier, trip timeline |
| Tax | 7 | Levy, ViDA readiness |
| Places and supply party | 7 | Place registry, Waypoint, party layer, mapping engine |
| Contingency | 5 | Held by the CFO |
| **Total** | **145** | |

The order followed one principle: **build first what reaches guests, auditors and regulators when it is inconsistent**, then what is expensive to run twice, and last what is merely duplicated.

![A roadmap from 2027 money and contracts to 2028 guest platforms, 2029 Keystone retired and 2030 steady state.](stays-marketplace-architecture/posts/43-converging-two-marketplaces/assets/images/43-converging-two-marketplaces/43-one-stay-sequence.jpeg)

**Figure 6:** *The One Stay sequence. Money and contracts first, because their inconsistency reached guests and regulators; guest-facing platforms next; Keystone's reservation module last, once every consumer reads the shared contract instead of its tables.*

{id: converging-two-marketplaces--trade-offs}
## Trade-offs

| Option | What it means | Gains | Costs | Right when |
| --- | --- | --- | --- | --- |
| **Federation** | Two stacks; shared money only | Speed in each brand; no coordination | Two answers to guests and regulators; fraud crosses brands unseen; duplicate run cost | The group may sell a brand soon, or brands share no guests or markets |
| **Shared core, supply engine per segment** | Shared engines and contracts; separate supply engines | One answer where outsiders look; supply models fit their supply | Contract governance; cross-cloud calls; years of dual running | Both types at scale, with convergence at the edges (Corvane) |
| **One front end, separate back ends** | One storefront codebase for several brands | Release velocity; one design system | The smaller brand inherits the larger's shopping assumptions | Brands with the same supply type, or after the shared contracts exist |
| **One platform for all supply** | One catalog and inventory engine for hotels and homes | One codebase; simple reporting | The Hotel-Shaped Home; the smaller supply type pays | Supply is genuinely one segment, such as professional pools only |
| **Absorb one brand** | Migrate the acquired brand onto the acquirer and retire it | Lowest long-run cost | Brand and supply loss during migration | The acquired brand's supply fits the acquirer's engine |

Corvane's choice is the second row. The decisive factor is not cost: Nookaway's supply is mostly individuals with one calendar, and Roomstead's is mostly companies with software. The option fails when contract governance fails, so its price is the contracts stewardship group of four engineers in Mariana's office ([Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts)) and a forum that says no.

Sequencing has its own trade-off.

| Order | Benefit | Risk | My view |
| --- | --- | --- | --- |
| **Money and contracts first** | Removes the inconsistencies auditors and regulators see; every later migration has a target | Little visible guest benefit for a year | Default for a group with a payments institution |
| **Guest-facing first** (front end, loyalty) | Visible synergy; cross-sell early | Builds on two reservation models; hides drift | Only if the contracts already exist |
| **Cheapest first** | Quick wins | Shares what is easy, not what is risky | Never as the organizing principle |
| **Supply first** | Biggest code reduction | The highest risk to bookings, for the least guest value | Not recommended |

{id: converging-two-marketplaces--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

For this chapter the useful comparison is not hotel versus home but **supply that crosses over**: what changes when each marketplace sells the other's kind of stay.

| Dimension | A home on the accommodation marketplace | A hotel on the hosted-stays marketplace |
| --- | --- | --- |
| **Typical supplier** | Professional manager with a vacation-rental PMS | Independent boutique hotel with a PMS and channel manager |
| **Engine** | OTA engine, with a one-unit integrity posture | Hotel-type engine, not the unit calendar |
| **Connectivity** | Channel manager, sometimes iCal for individual owners | Channel manager through the OTA's gateway |
| **Money** | Often needs platform collection: a host has no card terminal | Needs virtual cards or invoices and VAT documents, not individual payouts |
| **Regulation** | Short-term-rental registration per unit applies; the OTA must hold unit IDs | Registration rules for homes do not apply; hotel licensing does |
| **Trust** | Hosted-stays policies (parties, listing accuracy, deposits) | Partner-account protection; no guest screening for a staffed desk |
| **Page and support** | Listing layout, arrival instructions, damage process | Rooms table, front-desk arrival, walk and relocation process |
| **What breaks if forced** | Auto-replenishment of canceled nights, hotel-style walks | Eight identical listings competing in search |

The judgement: **convergence makes the shared core more valuable and the supply engines more important.** Every cross-type case in the table is configuration on shared money, trust, tax and messaging, and every one needs the right supply engine underneath. A group with one supply engine handles one column badly; a group with no shared core handles both columns twice.

{id: converging-two-marketplaces--failure-modes}
## Failure Modes

- **"One platform" as a slogan.** A board approves "one platform" without a register, and each team reads it differently. Supply teams start merging catalogs while payments still runs two ledgers. *Fix:* decide per capability, in writing, with a grade, an owner and a reason.
- **The shared engine with brand branches.** A shared engine accumulates `if brand == ...` code until it is two engines in one repository, owned by nobody. *Fix:* brand differences enter as policy data; count brand branches as a metric and treat growth as a design-review finding.
- **Lowest-common-denominator contracts.** The shared offer contract carries only what both engines can fill, so deposits, rental agreements or rate conditions travel in free text. *Fix:* contracts with optional typed sections per offer shape, and a steward who owns no engine.
- **Merging the supply model.** The larger brand's engine absorbs the smaller brand's supply. The Hotel-Shaped Home follows: cleaning fees folded into nightly prices, one-unit calendars sold under hotel replenishment rules, hosts asked for hotel contracts.
- **The smaller brand pays for the shared front end.** A storefront built for one supply shape carries its search, content and checkout assumptions to the other. Expedia's documented Vrbo slowdown is the public example. *Fix:* share contracts and components before codebases; migrate the smaller brand last, with its own success metrics.
- **Shared by budget line, not by migration.** A capability is marked shared and funded, but neither brand is required to stop using its own copy. Two years later the group runs three. *Fix:* every shared engine has a dated retirement plan for each brand's predecessor.
- **Cross-brand action without a policy.** Once trust is shared, a suspension on one brand can spread to the other automatically and take honest property managers with it. Warden's linked-entity review, with a second independent signal for verified managers, is the safer default ([Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety)).
- **Convergence by accident.** A template team, a search team or a pricing team decides how cross-type supply is handled because its release came first. *Fix:* the routing rule (segment chooses engine, brand chooses storefront) is a forum decision, written before the first cross-type listing goes live.

{id: converging-two-marketplaces--the-chief-architect-s-view}
## The Chief Architect's View

**Own the register, not the systems.** The Group Chief Architect owns the convergence register: one row per capability, with grade, owner, reason, review date and the predecessor systems to retire. Engine teams own their engines; the contracts stewardship group owns the contracts. The architecture forum approves grade changes; the board approves the program and its budget, not each cell.

**Decide what the board's words mean.** A board paper summarizes; the register decides. When the two diverge, as Corvane's seven lines did, say so in the next board update and point to the register. The CFO's question was the right one, and the answer was useful only because the register already existed.

**Set the entry and exit criteria for the shared core.** A capability enters the core when it passes the first test of Figure 2 and has an owner who can serve both brands. It must arrive with a contract, a service level per consuming brand, a defined behavior when it is unavailable (fail open or fail closed, with a budget, as Warden's 120 milliseconds), and a retirement date for each predecessor. It leaves the core, back to the brands, when brand branches outgrow shared logic. That exit is rare, and it should be possible.

**Write the routing rule before the first crossing.** Which engine serves each supply segment, which posture each unit cardinality gets, and who owns cross-listing consent. At Corvane, Aisha Rahman and Rafael Mendes co-own the rule, and the forum decides exceptions.

**Protect the neutral business.** Corvane Connect, the channel manager, distributes to Roomstead's and Nookaway's competitors. It stays off the shared core: public APIs, no group pricing features from its data ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers)). Convergence of the marketplaces must not become convergence with the software their suppliers buy from Corvane.

**Watch:**

- capabilities at their target grade, and predecessor systems still running past their retirement date;
- brand-specific branches inside shared engines;
- contract change lead time, from proposal to all consumers on the new version;
- duplicate run cost remaining, from the CFO's capability cost sheet;
- cross-brand detection lag: the time between an enforcement action in one brand and the review in the other (Turia Homes took 16 days in 2027);
- cross-type supply routed outside the rule, which should be zero.

**Write down what you will not share, and why.** The pressure to merge the supply engines will return with every new executive and every cost review. Corvane's register names the stressors that justify two engines: one-unit calendars that must never sell a night twice while 61% of listings also sell elsewhere; an ARI stream of up to 38,000 messages a second from software Corvane does not control; a source of truth that sits inside the platform for most homes and outside it for most hotels; and per-unit registration rules that a room-type pool cannot express without unit IDs. When a stressor disappears, the decision can be reopened; until then, the next debate starts from the record ([Built for the Next Disruption: Evolving a Stays Platform Over a Decade](#evolving-the-platform)).

**Expect the line to move.** Regulation will push more into the core: deemed-supplier VAT under the EU's "VAT in the digital age" package makes the tax decision central to the offer from 2028–2030 ([The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)), and short-term-rental rules already make unit identity a group concern ([Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation)). AI agents that book on a guest's behalf will call the shared offer and reservation contracts without seeing either storefront ([AI Across the Stay: Agents, Assistants and Automation](#ai-in-travel-stays)). Each of those shifts strengthens the shared contracts; none of them argues for one supply engine. [Built for the Next Disruption: Evolving a Stays Platform Over a Decade](#evolving-the-platform) turns the register's metrics into fitness functions.

{id: converging-two-marketplaces--questions-to-ask}
## Questions to Ask

1. Can you show the register: every capability with its grade, owner, reason and review date? Which board-level phrase does it replace?
2. For each shared engine, how many brand-specific branches does its code contain, and is the number growing?
3. Which predecessor systems are still running after their shared replacement went live, and when do they retire?
4. Who owns the offer and reservation contracts, and does that team own an engine?
5. For each supply segment, which engine serves it, and which brand's storefront sells it? Who decided?
6. What happens to a booking on each brand when a shared engine is unavailable for ten minutes?
7. If a fraudster is suspended on one brand today, when and how does the other brand find out?
8. Which inconsistencies reach guests, auditors or regulators today, and is the sequence of shared work ordered by them?
9. What did the last review decline, and why?

Convergence decides what the group's systems share. It does not yet say who builds them: which teams own the shared engines, which teams stay with each brand, and how one forum governs both. [Who Owns What: Organizing Engineering for Stays](#organizing-stays-engineering) draws the organization that this architecture needs.

{id: converging-two-marketplaces--sources-and-evidence}
## Sources and Evidence

{id: converging-two-marketplaces--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), Booking Holdings, 2026 — about 4.4 million Booking.com properties, about 3.9 million homes and apartments, alternative accommodations about 36% of room nights.
- [Request to Book overview](https://developers.booking.com/connectivity/docs/request-to-book/overview), Booking.com Connectivity documentation, n.d. (live October 2026) — 24-hour response window, three-day minimum lead time, partners block and release their own availability.
- [Understanding payouts](https://developers.booking.com/connectivity/docs/payments-by-booking-onboarding-api/understanding-payouts), Booking.com Connectivity documentation, n.d. (live October 2026) — payout rails per supply type, Stripe for US and Canadian homes.
- [Q2 2026 shareholder letter](https://s26.q4cdn.com/656283129/files/doc_financials/2026/q2/Airbnb-Q2-2026-Shareholder-Letter-FINAL.pdf), Airbnb, 2026 — boutique and independent hotels added; hotel nights growing about three times as fast as homes.
- [Scaling beyond one: how Airbnb evolved its data architecture for a multi-product world](https://airbnb.tech/uncategorized/scaling-beyond-one-how-airbnb-evolved-its-data-architecture-for-a-multi-product-world/), Airbnb Tech Blog, 2026 — data models fully separate or fully shared per domain; payments, messaging and support product-agnostic (offline warehouse).
- [Form 10-K for fiscal 2022](https://www.sec.gov/Archives/edgar/data/1324424/000132442423000007/expe-20221231.htm), Expedia Group, 2023 — front-end migration from 2021; Hotels.com completed 2022; Vrbo begun late 2022.
- [Form 10-K for fiscal 2023](https://www.sec.gov/Archives/edgar/data/1324424/000132442424000007/expe-20231231.htm), Expedia Group, 2024 — one unified front-end stack in 2023.
- [Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm), Expedia Group, 2026 — shared platform infrastructure list; One Key launch dates.
- [Q1 2024 earnings release](https://www.sec.gov/Archives/edgar/data/1324424/000132442424000024/earningsrelease-q12024.htm), Expedia Group, 2024 — Vrbo's slower recovery after re-platforming.
- [Rapid Vrbo integration guide](https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-integration-guide), Expedia Group, n.d. (live October 2026) — Vrbo inventory as a distinct single-unit, single-rate-plan product.

{id: converging-two-marketplaces--standards-regulation-and-documentation}
### Standards, regulation and documentation

- The regulatory forcing dates (EU Short-Term Rental Regulation, ViDA) are cited with their official texts in [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) and [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays).

{id: converging-two-marketplaces--research-and-practitioner-sources}
### Research and practitioner sources

- [How Do Committees Invent?](https://www.melconway.com/Home/Committees_Paper.html), Melvin E. Conway, 1968 — the link between communication structures and system structure that [Who Owns What: Organizing Engineering for Stays](#organizing-stays-engineering) builds on.
- Productscape reference models for travel accommodations and hosted stays (author's repository, 2026) — overlap matrix and residuality synthesis showing both models converging on the same separation of property, unit, listing, operator and reservation; generic models, not descriptions of any company.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
