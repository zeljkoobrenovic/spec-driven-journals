{id: property-and-listing-model}
# 5. Hotels and Homes: Modeling What Is Being Sold

![Hotels and Homes: Modeling What Is Being Sold — logo](stays-marketplace-architecture/posts/05-property-and-listing-model/assets/images/05-property-and-listing-model/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Take apart the supply data model of both marketplace types (property, room type, unit, rate plan and product on the OTA side; listing, unit and rooms within a home on the hosted-stays side) and see where a group that runs both should draw the shared line.

> **WHY THE BUSINESS CARES:** Every number the marketplace sells, reports or pays out is attached to something in this model. If the model cannot say which apartment a guest stayed in, the marketplace cannot file a short-term-rental report; if it cannot say which rooms are interchangeable, it cannot sell a hotel efficiently. Supply that does not fit the model either stays off the platform or arrives in a form that converts badly.

> **WHY ARCHITECTS SHOULD CARE:** The property and listing model is the most depended-on schema in a stays platform: availability, pricing, search, content, reservations, payouts, tax and trust all key on it. It is also the hardest schema to change, because partners, channel managers and regulators hold copies of its identifiers. Getting the levels right once is far cheaper than migrating a few hundred thousand properties later.

> **KEY POINTS:**
>
> * **Separate what exists from how it is sold.** Property, unit, spaces and beds describe the physical world; room type, rate plan and listing describe commercial offers on top of it. Hotels sell a *pool* of interchangeable units under several rate plans, homes sell *one specific* unit, and a model that fuses the physical and the commercial breaks on whichever side it was not built for.
> * **The unit is the identity that regulation, operations and integrity need.** EU short-term-rental registration is per unit, a double booking is per unit, and damage happens in a unit. An OTA can keep selling room-type pools, but every sellable unit still needs a stable identifier, and the reservation must learn which unit it got.
> * **Share identifiers and vocabulary, not one supply model.** A group running both marketplaces should share property and unit identities, a taxonomy with versioned channel mappings, and a common offer contract. It should keep the room-type inventory model and the single-unit calendar separate, and represent convergence through explicit profiles such as the multi-unit listing.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **The Hotel-Shaped Home** — homes are squeezed into room types with quantity, or hotels are flattened into dozens of one-unit listings, because the platform has only one way to say what is being sold.
> * **The Same Hotel Twice** — without stable property and unit identifiers that survive channels and suppliers, one building appears as several products and nobody can prove they are the same place.
> * **City-by-City Firefighting** — registration numbers and eligibility land on a model that has no unit to attach them to, so each new rule becomes a manual project.

Ask a hotel what it sells and the answer is a matrix: room types down the side, rate plans across the top, a price and a count in every cell for every night. Ask a host and the answer is a home: this apartment, these photos, this calendar. A stays marketplace has to store both. **The supply model is the schema that turns "a night somewhere" into something with an identifier, a price and a calendar**, and every later chapter of this book reads from it.

Most platforms inherit a supply model rather than design one. An OTA (online travel agency) that began with hotels describes each new apartment as a room type with a quantity; a hosted-stays marketplace that began with spare rooms lists each room of a new boutique hotel as a home. Both moves work for a while, then fail on the same question: **which physical place did this guest actually sleep in, and what were they promised about it?**

Part II argues that supply is master data with many writers; this chapter defines the master data. It turns the place registry and supply catalogs drawn in [Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts) into a model, and onboarding, content, connectivity and the ARI model later in the part all key on its identifiers. It owns the terms **property**, **room type**, **unit** and **listing**; rate plans in depth belong to [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model), content and cross-supplier mapping to [Describing a Stay: Content, Media and Property Mapping](#content-and-media), connectivity messages to [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers), and reservations to [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle).

{id: property-and-listing-model--setting-the-scene-at-corvane-thirty-eight-apartments-two-models}
## Setting the Scene at Corvane: Thirty-Eight Apartments, Two Models

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), sells some apartments through both of its marketplaces. **Costa Keys**, a professional property manager in Málaga, has **38 apartments** in three buildings in the historic center. Costa Keys runs a vacation-rental PMS (property management system) and distributes through Corvane Connect, the group's channel-manager business, to Roomstead, Nookaway and four other channels.

On **Roomstead**, the OTA-style marketplace, Costa Keys has been one property since 2016. Its apartments are grouped into room types, and each room type is sold under four rate plans (Flexible, Non-refundable, Weekly and a Roomstead Circle member rate), so the property carries 5 × 4 = **20 products**:

| Roomstead room type | Units | Typical occupancy | What Tally stores per night |
| --- | --- | --- | --- |
| Studio | 9 | 2 | Rooms to sell (0–9), four prices, restrictions |
| One-Bedroom Apartment | 14 | 3 | Rooms to sell (0–14), four prices, restrictions |
| One-Bedroom Apartment with Terrace | 5 | 3 | Rooms to sell (0–5), four prices, restrictions |
| Two-Bedroom Apartment | 8 | 5 | Rooms to sell (0–8), four prices, restrictions |
| Penthouse | 2 | 4 | Rooms to sell (0–2), four prices, restrictions |

A Roomstead guest books "One-Bedroom Apartment, Non-refundable" and Tally, Roomstead's ARI (availability, rates and inventory) store, decrements the count for that room type. Which of the fourteen apartments the guest gets is decided later by the PMS, usually the day before arrival. Roomstead's reservation never learns the answer.

On **Nookaway**, the hosted-stays marketplace, the same 38 apartments are **38 listings**. Each has its own photos, its own calendar row per night in Almanac, its own reviews and its own registration number. A Nookaway guest books *apartment 3A in the Calle Granada building*, not a category.

![One building of 38 apartments sold two ways: pooled into bins as 20 products on Roomstead, and as 38 individual door cards on Nookaway.](stays-marketplace-architecture/posts/05-property-and-listing-model/assets/images/05-property-and-listing-model/05-same-apartments-two-models.jpeg)

**Figure 1:** *The same 38 Costa Keys apartments are 20 pooled products on Roomstead and 38 separate listings on Nookaway, and only Nookaway can say which apartment a guest slept in.*

The difference did not matter until April 2027. The EU Short-Term Rental (STR) Regulation, Regulation (EU) 2024/1028, had applied since 20 May 2026. Spain's national single registry had been annulled by the Supreme Court on 21 May 2026, but the court upheld the digital single window and the platforms' data-sharing duties, and regional registration numbers still applied ([CGPJ, 2026](https://www.poderjudicial.es/cgpj/es/Poder-Judicial/Tribunal-Supremo/Noticias-Judiciales/El-Tribunal-Supremo-anula-el-Registro-Unico-de-arrendamientos-de-corta-duracion-por-considerar-que-el-Estado-carece-de-competencia-para-su-creacion)). The regulation asks platforms for **activity data per unit**: nights rented and guests per night, with the unit's registration number, address and listing URL ([Regulation (EU) 2024/1028, Art. 9](http://publications.europa.eu/resource/celex/32024R1028), 2024). [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) covers the legal detail.

Noor van Dijk, Head of Regulatory Affairs and Privacy, asked both brands for the monthly feed. Nookaway, which had already removed its unregistered Spanish listings in 2026, produced it from Almanac and its reservation table in a week: one listing, one unit, one registration number. Roomstead could not. Its property record had a single "license number" field, designed in 2014 for hotel classification certificates, and Costa Keys had typed in the number of its first apartment. Its reservations named a room type, not an apartment. Across Roomstead, about **61,000** of the **435,000** alternative-accommodation properties were multi-unit pools of this kind, holding about **260,000** units that the platform sold but could not name.

Aisha Rahman, VP Supply and Connectivity at Roomstead, proposed the obvious fix: sell each apartment as its own room type with quantity one. Costa Keys did not want that: pooling lets it move a guest from 3A to 2C when a boiler fails, and lets Roomstead show one "One-Bedroom Apartment" card rather than fourteen near-identical ones. Rafael Mendes, VP Engineering at Nookaway, raised the mirror-image problem: Nookaway's 2028 pilot with boutique hotels would bring 20- and 30-room properties into a platform whose only answer was "one listing per room". Mariana Costa, the Group Chief Architect, put one question to the architecture forum: **what is the smallest shared model that lets each marketplace keep its way of selling, and still lets the group say which physical unit every night was sold in?**

{id: property-and-listing-model--concepts-what-exists-and-what-is-sold}
## Concepts: What Exists and What Is Sold

The model has two layers. The **physical layer** describes places that exist whether or not anyone sells them. The **commercial layer** describes how a marketplace offers those places to guests. Most modeling mistakes here put an attribute on the wrong layer.

| Term | Layer | Definition used in this book |
| --- | --- | --- |
| **Property** | Physical | A place operated as one accommodation business at one address or site: a hotel, a hostel, an aparthotel, a building of managed apartments, a single house. It has an operator, a location, a jurisdiction and property-wide policies. |
| **Unit** | Physical | The smallest space that is sold to one party for exclusive use on a night: a hotel room, an apartment, a whole house, a private room in a home, a bed in a dormitory. A unit has its own door (or bed), its own occupancy limit and, where regulation requires one, its own registration number. |
| **Space** and **bed** | Physical | The parts of a unit: bedrooms, living rooms, bathrooms, kitchens, terraces, and the beds in them. They drive occupancy, bed configuration and many filters. |
| **Room type** | Commercial (OTA) | A category of units the property treats as interchangeable for sale, with a count of units, a description and an occupancy. Booking.com's connectivity documentation calls room types "labels or categories used to organise physical rooms in a property" and uses `Quantity` for "the number of units of a room type" ([Booking.com, n.d.](https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-room-types.md)). |
| **Rate plan** | Commercial (OTA) | A named set of commercial terms under which room types are sold: price logic, cancellation and prepayment, meal plan, restrictions, eligibility. Owned in depth by [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model). |
| **Product** | Commercial (OTA) | The sellable combination of a room type and a rate plan, against which availability, rates and restrictions are set. Booking.com calls it a **roomrate**: "a unique combination of room type, rate plan, and conditions" ([Booking.com, n.d.](https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-roomrates.md)). |
| **Listing** | Commercial (hosted stays) | A published offer of one unit (or, for professional managers, a small pool of identical units) on one marketplace, with host-authored content, one calendar, one price set and one cancellation policy. |
| **Offer** | Commercial (both) | A priced, bookable answer to a guest's request for specific dates and guests, computed from the commercial layer. Defined in [Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts) and computed in [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine). |

**Physical inventory versus sellable inventory.** A hotel with 84 rooms has 84 units, but it may offer 70 through one channel, sell 86 on a night it expects no-shows, or hold six out of order. Sellable inventory is a commercial decision recorded per room type and night in the ARI model; physical inventory is a fact about the building. Storing both in one field corrupts both. Booking.com's own vocabulary separates them: "Inventory is the total number of rooms a property offers for sale", while "Availability is the portion of inventory that guests can book based on their search criteria" ([Booking.com, n.d.](https://developers.booking.com/connectivity/docs/ari)).

**A pool versus a specific unit.** A room type promises a *kind* of room; the specific room is assigned by the property, often at check-in. A listing promises *this* home. This difference decides how inventory is counted (a number per night versus a free-or-taken flag), how a guest is made whole when something goes wrong (an equivalent room versus another home), and what can be reported to a regulator.

![A shared physical layer of property, unit and beds under two commercial panels: room type and rate plan forming products that group units, and a listing that publishes one unit.](stays-marketplace-architecture/posts/05-property-and-listing-model/assets/images/05-property-and-listing-model/05-physical-and-commercial-layers.jpeg)

**Figure 2:** *The supply model has a physical layer that both marketplaces share and a commercial layer that differs. A room type groups interchangeable units and is sold under rate plans as products; a listing publishes one specific unit.*

{id: property-and-listing-model--the-accommodation-marketplace-model-property-room-type-rate-plan-product}
## The Accommodation Marketplace Model: Property, Room Type, Rate Plan, Product

The OTA model is a product catalog with four levels. Booking.com's public connectivity documentation states it most clearly, and Expedia Group's supply APIs describe the same shape.

| Level | Carries | Documented constraints (Booking.com, read October 2026) |
| --- | --- | --- |
| **Property** | Address, geocode, property type, star rating, facilities, property-wide policies, photos, licenses, contacts | Built through the Property, Facilities, Content, Photo and Licences APIs ([Booking.com, n.d.](https://developers.booking.com/connectivity/docs)) |
| **Room type** | Name, unit count, size, occupancy, bed configuration, room amenities, room photos | At most **100 room types** per property, active and inactive |
| **Rate plan** | A label and, through relations, derived pricing from a parent | "A _rate plan_ is simply a name you use to organize prices"; at most **200 active rate plans** ([Booking.com, n.d.](https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-rate-plans)) |
| **Product (roomrate)** | Room type × rate plan × conditions: cancellation and prepayment policy, meal plan, restrictions, child prices | At most **400 active roomrates**; ARI is set against them |

Three details in that documentation shape the architecture. First, **the conditions live on the product, not on the rate plan**. Booking.com attaches cancellation policy, prepayment policy and meal plan when it creates the roomrate; the rate plan is only a name ([Booking.com, n.d.](https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-rate-plans)). A platform that stores the cancellation policy on the rate plan cannot express "Flexible, with breakfast, for the suite only", and ends up creating more rate plans to compensate, which is how **Rate Plan Sprawl** begins.

Second, **ARI is keyed to the product, and products depend on room types**. Deactivating a room type deactivates all its roomrates, and reactivation requires recreating them and pushing availability again ([Booking.com, n.d.](https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-room-types.md)). Merging two room types after a renovation therefore wipes the commercial state that depends on them, so the model needs an explicit migration path for room-type changes, not a delete.

Third, **the cardinality is the cost**. Expedia Group's Availability and Rates API takes inventory per room type and prices per room type and rate plan, up to two years ahead ([Expedia Group, 2025](https://developers.expediagroup.com/supply/lodging/docs/avail_and_rate_apis/avail_rates/getting_started/introduction)). Costa Keys' 20 products over 730 days are 14,600 product-nights before occupancy variants; a hotel with 12 room types and 15 rate plans has 180 products and 131,400. Channels cap products because each one multiplies storage, ARI traffic, cache size and tests ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model)).

![A 20-product grid stretched over 730 days into 14,600 product-nights, beside a 180-product grid that becomes 131,400.](stays-marketplace-architecture/posts/05-property-and-listing-model/assets/images/05-property-and-listing-model/05-cardinality-is-the-cost.jpeg)

**Figure 3:** *Every product multiplies by every night on sale: Costa Keys' 20 products over 730 days are 14,600 product-nights, and a hotel with 180 products reaches 131,400.*

{id: property-and-listing-model--physical-rooms-behind-the-room-type}
### Physical rooms behind the room type

The room type hides the physical rooms on purpose. The property's PMS knows that room 413 connects to 414 and that 418 is out of order until Friday; the marketplace sees "Deluxe King: 6 to sell". For a hotel that is the right division of labor: the property assigns rooms itself.

It is the wrong division for three kinds of supply the OTA increasingly sells: **managed apartments** like Costa Keys, where each unit is a regulated rental with its own registration number; **distinct units under one name**, such as four resort villas that differ in view and floor plan but are sold as "Villa", so the guest who booked from photos gets a different house; and **accessible rooms**, where a guest who booked a roll-in shower and gets a room without one was sold the wrong thing. These cases need a unit layer under the room type: its units, the registration number of each, and a way for the property to report which unit a reservation was assigned.

{id: property-and-listing-model--the-hosted-stays-model-listing-unit-and-rooms-within-a-home}
## The Hosted-Stays Model: Listing, Unit and Rooms Within a Home

A hosted-stays marketplace collapses the hierarchy. The listing *is* the commercial object and, for most listings, it maps one-to-one to a unit. There is no rate-plan matrix: a listing has a nightly price per date, length-of-stay discounts, fees such as a cleaning fee, and one cancellation policy chosen from a small set of platform-standard tiers. Its inventory is a calendar in which each night is free, booked or blocked.

Expedia Group's documentation for distributing Vrbo inventory through its Rapid API states the contrast in one place. Vrbo properties are "whole property only, no shared accommodations", "single-unit only" and carry "a single rate plan"; bed groups, the hotel construct for describing beds, are "not applicable to Vrbo", and the unit configuration is described instead ([Expedia Group, n.d.](https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-integration-guide)). The same guide recommends refreshing Vrbo content at least weekly because it changes more often than hotel content. Airbnb has not published its internal listing schema. Three cases break the one-to-one mapping.

**Rooms within a home.** Hosted-stays platforms commonly let a host offer a whole home and, separately, private rooms in it. The Triana apartment of Carmen Ruiz, a Nookaway host in Seville, has two bedrooms; she could list the whole apartment at €110 a night and each bedroom as a private room. Booking the whole apartment must block both rooms, and booking either room must block the whole apartment, so the three listings must be modeled as **linked listings over shared units**: the whole-home listing publishes units {bedroom 1, bedroom 2, shared spaces}, each room listing publishes one bedroom, and a night is free for a listing only when all units it covers are free. Without the physical layer, the dependency lives in application code, where it is the commonest source of internal double bookings on platforms that allow rooms within a home.

**Multi-unit listings.** Professional managers hold **44%** of Nookaway's 1.15 million listings, and many of them operate identical units in one building. One listing per unit duplicates content, splits reviews and floods search results with near-identical cards. A **multi-unit listing** publishes a small pool of identical units with one calendar that counts free units per night. It is a room type in all but name, with the same obligation: the platform must still learn which unit each guest received.

**Hotels on a hosted-stays platform.** When a hosted-stays marketplace adds boutique and independent hotels, as Airbnb reported doing in "more than 20 destinations" in 2026 while hotels remained "a single-digit percentage of nights booked" ([Airbnb Q2 2026 shareholder letter](https://s26.q4cdn.com/656283129/files/doc_financials/2026/q2/Airbnb-Q2-2026-Shareholder-Letter-FINAL.pdf), August 2026), it meets room types from the other direction. A 24-room hotel as 24 listings is The Hotel-Shaped Home in reverse; a 24-room hotel as one listing with a count, a single price and one cancellation policy is honest but leaves out the rate plans that hotels use to manage demand.

A 2026 Airbnb engineering post states a rule for new kinds of supply that applies here. When Airbnb added Services, it introduced "a parent listing with many offerings" with time-slot availability, unlike date-based Homes, and the team's rule was that "a domain's data model had to be either completely separate by product type or completely monolithic" ([Airbnb Tech, 2026](https://airbnb.tech/uncategorized/scaling-beyond-one-how-airbnb-evolved-its-data-architecture-for-a-multi-product-world/)). The post covers the offline warehouse, not online services, but the rule applies to the supply model too: give new supply its own model or generalize the existing one completely, never half.

{id: property-and-listing-model--occupancy-beds-and-configuration}
## Occupancy, Beds and Configuration

Occupancy and beds look like content but behave like inventory rules: they decide which offers a search for "2 adults, 2 children aged 9 and 12" may return and what the guest finds at the door.

| Element | Where it lives | What it must express | Common mistake |
| --- | --- | --- | --- |
| **Occupancy limits** | Unit (physical), room type or listing (commercial) | Maximum adults, maximum children, maximum total, infants counted or not, standard occupancy (what the base price covers) | One "max guests" number, so a room for two adults is offered to one adult and three children |
| **Child age bands** | Property or rate plan | Which ages count as infant, child or adult for occupancy and price; ages vary by property and country | Treating "child" as a global constant |
| **Bed configuration** | Spaces in the unit | Beds per space, by type and size, plus **alternative arrangements** ("one double or two singles") and whether a choice is guaranteed or on request | Free-text bed descriptions; summing beds across alternatives |
| **Extra beds and cots** | Unit or room type, with a fee | Availability, count, fee and age limits | Selling an extra bed that requires a count the property never sent |

Booking.com models beds as amenity codes with a `Configuration` attribute that distinguishes standard from alternative arrangements, and describes homes through subrooms of type "Bedroom", "Living room" and "Bathroom" with beds attached to each ([Booking.com, n.d.](https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-room-types.md)). Both choices are worth copying: beds belong to spaces, and spaces belong to units, so a two-bedroom apartment can say that the second bedroom has two singles that can be joined, and a filter for "separate bedrooms for children" can be answered from data rather than from text.

Occupancy limits belong to the physical unit first, because safety rules and guest-count reporting apply per unit; the commercial layer may only narrow them. When the commercial maximum can exceed the physical one, the platform sells stays that cannot lawfully happen. [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) covers occupancy-based pricing.

{id: property-and-listing-model--attributes-and-taxonomies}
## Attributes and Taxonomies

Amenities, property types and room features drive the filters marketplaces compete on, and their data decays fastest. Most hotel connectivity uses the OpenTravel Alliance's code lists. Booking.com's connectivity documentation lists the ones it implements, including **PCT** (Property Class Type), **HAC** (Hotel Amenity Code), **RMA** (Room Amenity Type) and **MPT** (Meal Plan Type), next to its own **BC**-prefixed lists such as room types and cancellation policies ([Booking.com, n.d.](https://developers.booking.com/connectivity/docs/codes-pct)).

Booking.com implements the OpenTravel 2014B PCT list, splits it into "Hotel properties" and "Home properties", and **extends** it with its own codes from 5000 upward: Love Hotel, Capsule Hotel, Cruise Ship and Student Accommodation on the hotel side; ApartHotel, Riad, Ryokan, Homestay and Holiday Home on the home side. Some types carry rules: Apartment and ApartHotel "require" room types to have a kitchen or kitchenette "to become open and bookable" ([Booking.com, n.d.](https://developers.booking.com/connectivity/docs/codes-pct)). Standards also lose detail: Booking.com groups codes 28 (Desk), 29 (Desk with lamp) and 64 (Large desk), which "internally default to 28 (Desk)", so a value written through one code reads back as another ([Booking.com, n.d.](https://developers.booking.com/connectivity/docs/codes-rma), read October 2026).

Four rules follow for the taxonomy.

1. **Keep an internal canonical taxonomy and map to every standard.** OpenTravel code lists are an interchange vocabulary that every channel extends, not a product taxonomy. Store attributes against your own versioned taxonomy and keep one mapping table per inbound standard and per outbound channel.
2. **Expect lossy round trips and measure them.** When inbound codes collapse, a channel sees a different value than the property sent. Record which canonical value came from which source code so support can explain "I set *desk with lamp* and you show *desk*".
3. **Put attributes on the level where they are true** (see the table below). An attribute stored on a room type that is true for only some of its units is a misdescription waiting for a complaint.
4. **Let property type drive completeness rules, not code paths.** "An apartment must have a kitchen" and "a hostel must say which dormitories are mixed" are rules on data. They belong in a validation layer keyed by property type, which [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding) uses in its readiness checks.

| Attribute | Correct level | Why the level matters |
| --- | --- | --- |
| Swimming pool, parking, front desk hours | Property | Shared by every unit; filters at property level |
| Floor area, view, balcony, accessibility features | Unit (room type only if uniform) | Guests book on it; a mismatch is "not as described" |
| Beds and bedrooms | Spaces within the unit | Occupancy, family filters, guest expectations |
| Breakfast, half board | Rate plan or product | Changes price and is a common cause of metasearch price mismatches |
| Smoking, pets, parties | Property or listing policy | House rules differ per home; a hotel sets one per property |
| Registration number | Unit | Regulation registers units, not properties |

{id: property-and-listing-model--location-and-address}
## Location and Address

Location looks like one field but is at least four.

- **Address and geocode of the property.** Where the guest navigates to and what search ranks by distance. The place graph (cities, neighborhoods, areas) is a separate component owned by [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps).
- **Unit address detail.** Building, floor, door. For apartments spread over several buildings, check-in instructions and the regulator's activity data need the unit's address, not the property's.
- **Jurisdiction.** Country, region, municipality and any special zone (a short-term-rental restriction area, a tourist-tax zone). Jurisdiction should be *derived* from the geocode by a versioned resolver and stored with the version used, because zone boundaries change and a tax or eligibility decision must be reproducible later. [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays) and [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) consume it.
- **Displayed location.** For homes, the exact address is commonly hidden until booking; for hotels it is shown. The rule must be enforced at the API, not only in the page template.

Keep the true geocode, the jurisdiction and the displayed location as separate fields with separate access rules: a blurred point cannot resolve jurisdiction.

{id: property-and-listing-model--policies-where-each-rule-attaches}
## Policies: Where Each Rule Attaches

Policies are the second structural difference between the marketplaces. For each one, the model must say on which level it attaches and which level wins.

| Policy | Accommodation marketplace | Hosted-stays marketplace | Modeling rule |
| --- | --- | --- | --- |
| Check-in and check-out times | Property | Listing | Physical defaults with commercial overrides |
| House rules (pets, parties, smoking, quiet hours) | Property, sometimes room type | Listing, authored by the host | Structured fields plus free text; structured fields drive filters and trust checks |
| Cancellation and prepayment | Product (room type × rate plan); several bookable at once | Listing; one platform-standard tier at a time | Typed time windows and penalties, frozen onto the reservation at booking |
| Meal plan | Product | Rare | Product attribute that changes price |
| Mandatory fees (resort fee, cleaning fee) | Property or product | Listing (cleaning fee per stay) | Structured fees with basis (per stay, per night, per person); feed the total price |
| Damage deposit, rental agreement | Rare | Listing; Vrbo documents both as listing-level options | Listing attributes the checkout must honor |
| Children and extra-bed policy | Property and room type | Listing | Age bands and fees, not text |

Two rules keep this manageable. **Every policy is machine-evaluable data**: a cancellation policy as ordered time windows with typed penalties, as Expedia's Rapid API returns them ([Expedia Group, n.d.](https://developers.expediagroup.com/rapid/lodging/shopping/constructing-cancellation-policies)), a fee as an amount with a basis, a house rule as a code; [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) builds on this. And **the policy that applied is frozen onto the reservation**, so a later edit cannot change what a past guest is owed. Policy text that lives only in templates and support macros is the root of **Policy Spaghetti**.

{id: property-and-listing-model--identifiers-external-codes-and-versions}
## Identifiers, External Codes and Versions

Identifiers are the part of the model that other parties copy: channel managers store your room-type and rate-plan IDs, regulators your listing URLs, tax authorities your property references. Once an identifier has left the building, changing its meaning is a migration project across organizations.

| Identifier | Issued by | Scope and rule |
| --- | --- | --- |
| Property ID | Marketplace | Stable for the life of the property; never reused; survives operator change only by explicit decision |
| Unit ID | Marketplace (or group registry) | Stable per physical unit; survives a change of room type or listing |
| Room-type ID, rate-plan ID, product ID | Marketplace | Stable per commercial object; renaming must not change the ID |
| Listing ID | Marketplace | Stable per listing; the public URL derives from it |
| External codes | PMS, channel manager, supplier, bedbank | Stored as cross-references with source and validity, never as primary keys |
| Registration and license numbers | Public authority | Attached to the unit (STR) or property (hotel classification), with validation status and dates |
| Legal entity and operator IDs | Business registries, tax authorities | Attached to the operator, not the property, because operators change |

Hotel connectivity shows how sticky these are. Booking.com's rate endpoint uses `InvTypeCode` for its room-type ID and `RatePlanCode` for its rate-plan ID ([Booking.com, n.d.](https://developers.booking.com/connectivity/docs/ota-rateamountnotif)); Expedia's Availability and Rates API accepts updates "by Expedia IDs only", not the property's own codes ([Expedia Group, 2025](https://developers.expediagroup.com/supply/lodging/docs/avail_and_rate_apis/avail_rates/getting_started/introduction)). Every channel manager therefore maps the hotel's codes to each channel's IDs, and a marketplace that reissues IDs during a re-platforming forces thousands of partners to remap at once. The rules I use: **identifiers carry no meaning** (no city codes or brand prefixes inside them), **are never recycled**, and **are issued by the system that owns the concept**, not by whichever service first needed one. Mapping the same hotel across suppliers is a separate problem with its own machinery, covered in [Describing a Stay: Content, Media and Property Mapping](#content-and-media) and, for the general technique, LISTED's [One Property, Three Listings: Duplicates and Entity Resolution](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/entity-resolution.html).

{id: property-and-listing-model--versioning-and-effective-dating}
### Versioning and effective dating

Three mechanisms keep the history reproducible as supply changes: hotels merge room types, hosts add a sofa bed, cities change zones.

- **Versioned content.** Every change to a property, unit, room type or listing creates a version with an author, a source and a timestamp, so a dispute about "two bedrooms advertised" is settled by the version the guest saw, not by today's page.
- **Booking snapshots.** The reservation stores the identifiers *and* a snapshot of the commercial terms and key physical facts (room type name, bed configuration, occupancy, policies) at confirmation. [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) owns the snapshot; this model must make it cheap to produce.
- **Effective-dated eligibility.** Whether a unit may be sold on a date is not an `active` flag. The generic Productscape reference models behind this book reach the same conclusion: "bookability is evaluated per unit, operator, jurisdiction, and stay date". A registration that expires on 30 June leaves the unit sellable for June and unsellable for July, and that decision must be reproducible later.

{id: property-and-listing-model--architecture-a-supply-catalog-with-a-shared-physical-core}
## Architecture: A Supply Catalog With a Shared Physical Core

The architecture has one owner for "what is being sold" per marketplace and one small shared core for "what exists".

![Partner tools write a supply catalog that registers unit IDs in a place registry and publishes catalog events to calendar, search and reservations, with reporting reading both reservations and the registry.](stays-marketplace-architecture/posts/05-property-and-listing-model/assets/images/05-property-and-listing-model/05-catalogs-and-place-registry.jpeg)

**Figure 4:** *Each marketplace keeps its own supply catalog, its own way of selling. Both register properties and units in one place registry, which also anchors eligibility and reporting. Downstream systems consume catalog events rather than reading the catalog's tables.*

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Place registry** | Issue and hold property and unit identities, addresses, geocodes, jurisdictions, registration numbers | Physical identity and its history | Hold prices, rate plans, calendars or marketing content; own places (Waypoint's job) |
| **Supply catalog** (one per marketplace) | Hold the commercial model: room types, rate plans and products, or listings; content references; policies | Commercial objects, their versions and validation | Store availability counts or nightly prices (the ARI store's job) |
| **Eligibility** | Decide per unit, operator, jurisdiction and date whether a stay may be offered | Rules, decisions and evidence | Delete listings; it restricts, the catalog stays intact |
| **ARI store or unit calendar** | Counts, prices and restrictions per product and night, or free/booked per unit and night | Time-varying inventory | Redefine products; it refuses ARI for unknown products |
| **Search and content index** | Read-optimized projection of catalog plus eligibility | Index schema | Become a source of truth for any field |
| **Reservation service** | Reservation with identifiers and a frozen snapshot; learns the assigned unit | Reservation state | Look up "current" terms after confirmation |

Four interface decisions make this work.

1. **Catalog changes are events.** The catalog publishes versioned events such as `RoomTypeChanged` and `ListingPublished`; the ARI store, search index and content pipeline subscribe, and no consumer reads the catalog's tables ([Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays)).
2. **The unit assignment flows back.** The property's system reports the unit assigned to a pooled reservation, and the marketplace stores it as a reservation fact; otherwise the extranet asks for it before check-in (Figure 5).
3. **Eligibility is a separate decision.** It reads the registry and the rules of [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) and records "sellable or not, why, under which rule version"; the catalog holds no `is_legal` flag.
4. **One vocabulary across marketplaces.** "Unit", "property", "operator" and "registration number" mean the same in both catalogs; "room type" and "listing" stay marketplace-specific.

![Swimlanes for guest, Roomstead, Corvane Connect, PMS and reporting: a room-type booking is delivered, the PMS assigns unit Granada 3A later, and the unit ID flows back to Roomstead and into reporting.](stays-marketplace-architecture/posts/05-property-and-listing-model/assets/images/05-property-and-listing-model/05-unit-learned-after-booking.jpeg)

**Figure 5:** *For a pooled Costa Keys booking on Roomstead, the unit is learned after booking. The reservation stays valid against the room type; the assignment is a later fact, and reporting reads the unit from the reservation, not from the room type.*

{id: property-and-listing-model--in-practice-how-the-public-record-and-corvane-handle-it}
## In Practice: How the Public Record and Corvane Handle It

{id: property-and-listing-model--what-the-large-platforms-document}
### What the large platforms document

- **Booking.com models homes inside the hotel model**: a home is a room type whose `Quantity` counts identical units, with "multi-bedroom setups" for Apartment, Suite, Chalet, Bungalow, Holiday home, Villa and Mobile home built from subrooms ([Booking.com, n.d.](https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-room-types.md)). It is moving home providers off the OpenTravel content messages: `OTA_HotelInvNotif` "will sunset… for Home providers on December 31, 2026", with home providers directed to the Rooms and Facilities APIs ([Booking.com, n.d.](https://developers.booking.com/connectivity/docs/tsk-modify-room-amenities.md)). Booking Holdings reported that alternative accommodations were about **36%** of Booking.com room nights in 2025 ([Booking Holdings FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), February 2026). How Booking.com stores homes internally is not public.
- **Expedia Group keeps homes in a separate model**, as the Vrbo integration guide quoted under The Hosted-Stays Model shows, with listing-level house rules, rental agreements and damage deposits ([Expedia Group, n.d.](https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-integration-guide)). Expedia's FY2025 10-K reported about 3.6 million lodging properties, of which about 2.4 million are alternative accommodations bookable through Vrbo ([Expedia Group FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm), February 2026). [Expedia Group and Vrbo: Consolidating Brands Onto One Platform](#case-expedia-vrbo) discusses the platform history.
- **Property counts and listing counts are not comparable.** Booking Holdings' annual report gives about 4.4 million properties at 31 December 2025, about 500,000 of them hotels, motels and resorts and about 3.9 million alternative accommodations ([Booking Holdings 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm)). Its corporate site, read in October 2026, reported about 4.7 million properties and more than 33 million listings ([Booking Holdings, n.d.](https://www.bookingholdings.com/about/)). The two counts differ in date and in what they count, so neither is wrong. Define the unit and the date before comparing scale.

> **INFERENCE, NOT DOCUMENTED:** The documentation above constrains what each company's internal model must represent; it does not describe that model. Booking.com exposing homes as room types with quantity does not mean it stores them that way, and Vrbo's separate distribution model may sit on shared internal services.

{id: property-and-listing-model--corvane-s-worked-example-the-unit-layer-for-roomstead}
### Corvane's worked example: the unit layer for Roomstead

Mariana Costa's architecture forum met on **12 May 2027** and rejected both simple fixes. Selling every apartment as its own room type would have turned Costa Keys' 20 products into 152 (38 × 4), broken its pooling, and multiplied Roomstead's ARI traffic for the 61,000 pooled properties. Forcing Nookaway's listing model onto Roomstead's apartments would have discarded the rate plans that professional managers use on the OTA. The forum chose a **shared physical core with separate commercial models**, consistent with One Stay's "shared contracts, separate engines". The registry is the design of the "property and unit identity" shared contract on the March 2027 capability map (v1); the December 2027 map v2 in [One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces) keeps it.

The decision had four parts.

1. **A place registry**, owned by the supply domain in Lisbon, issues group property and unit identifiers. Both Roomstead's catalog in Keystone and Nookaway's catalog in Burrow reference them. The registry holds addresses, geocodes, resolved jurisdictions and registration numbers; it holds no prices or calendars. It is not the place service: **Waypoint**, the group destination graph approved in June 2027 and owned by Jonas Weber's search team, is a separate component that, from its first release in Q1 2028, writes geo enrichment (cells, place IDs, a public display point and jurisdictions) to registry records, never the reverse ([Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps)).
2. **Roomstead room types gain a unit list.** For alternative accommodations in jurisdictions with a registration procedure, a room type must list its units with registration numbers before it can be opened for sale. Tally is unchanged: it still counts per room type and night.
3. **Unit assignment becomes a reservation fact.** Corvane Connect and Switchyard, Roomstead's connectivity gateway, carry the assigned unit in the reservation-modification flow. Where a PMS cannot send it, the Partner Hub extranet asks the partner to assign a unit by the morning of arrival.
4. **Nookaway's multi-unit listings follow the same rule.** A multi-unit listing references its units in the registry and records the assigned unit per reservation.

For Costa Keys:

| Measure | Before (April 2027) | After (October 2027) |
| --- | --- | --- |
| Roomstead room types / products | 5 / 20 | 5 / 20 (unchanged) |
| Registration numbers held by Roomstead | 1 (in a property field) | 38 (one per unit) |
| Roomstead reservations with a known unit | 0% | 97% (the rest assigned in the extranet before arrival) |
| Nookaway listings | 38 | 38, now referencing the same 38 unit IDs |
| Units that both marketplaces can identify as the same | 0 | 38 |

The last row is an unplanned benefit: the group could count nights per apartment across both marketplaces, and Corvane Connect no longer needed a hand-maintained mapping between "Granada 3A" on Nookaway and a Roomstead "One-Bedroom Apartment" night. Across Roomstead, the rollout target was a known unit for 95% of reservations at pooled alternative-accommodation properties in EU registration markets by the end of Q1 2028. For Nookaway's 2028 boutique-hotel pilot, Rafael's team first proposed multi-unit listings over registry units; in December 2027 the group instead routed the pilot to the hotel-type engine behind a Nookaway storefront, a decision [One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces) explains.

{id: property-and-listing-model--trade-offs-four-ways-to-model-two-marketplaces}
## Trade-offs: Four Ways to Model Two Marketplaces

| Option | Fits hotels | Fits homes | Regulation per unit | Cost and risk | When it is right |
| --- | --- | --- | --- | --- | --- |
| **A. Hotel-shaped model for both** (homes are room types with quantity) | Native | Poor: homes carry rate-plan machinery they do not use, and unit identity is lost when quantity is above one | Weak unless a unit layer is added | Lowest for an OTA adding homes; rising cost of misfit | An OTA where homes are a minority sold mostly by professional managers |
| **B. Home-shaped model for both** (every unit is a listing) | Poor: no pools, no rate plans, N cards per hotel | Native | Native | Lowest for a hosted platform adding a few hotels; breaks at hotel scale | A hosted-stays platform adding small boutique hotels as a side line |
| **C. Two fully separate models** | Native | Native | Native on the home side, weak on the OTA side | Duplicate catalogs, no shared identity, cross-listed units invisible to each other | Separately run brands with no shared supply or reporting |
| **D. Shared physical core, separate commercial models** | Native | Native | Native on both | A registry and a unit-assignment flow to build and govern | A group that shares supply, reporting or integrity controls across both |

Option D is my default for any group with overlapping supply, but it has costs. The registry sits on the onboarding critical path, and its governance is harder than its code: deciding when two records are the same unit is an entity-resolution problem with human review. When the overlap is small, as in a hosted-stays platform with a few hundred hotels, Option B with explicit multi-unit listings is cheaper and good enough.

Within the OTA, a second trade-off is **pool versus unit-level selling** for managed apartments:

| Approach | Guest sees | Partner flexibility | Marketplace knows unit | Best for |
| --- | --- | --- | --- | --- |
| Pool (room type with quantity) | One card per category | High: assign and move freely | Only after assignment | Uniform apartments, aparthotels |
| Unit-level (quantity one per unit) | One card per apartment | Low: the guest bought that unit | At booking | Distinct homes, villas, regulated units where the regulator expects the booked unit |
| Pool with unit list and assignment (Corvane's choice) | One card per category | High | After assignment, with a deadline | Professional managers with uniform units in registration markets |

{id: property-and-listing-model--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (Roomstead) | Hosted-stays marketplace (Nookaway) |
| --- | --- | --- |
| **Supply** | Professionally run properties; a property has many units; a minority of alternative accommodations from professional managers | Mostly one home per host (82% of Nookaway hosts have one listing); professional managers hold 44% of listings |
| **What is sold** | A product: room type × rate plan, against a pool of interchangeable units | A listing: one specific unit, rarely a small pool |
| **Data model** | Property → room type (with count) → rate plan → product; physical rooms mostly invisible | Listing ≈ unit; spaces and beds; linked listings for rooms within a home |
| **Who authors it** | Partner systems through connectivity, or the extranet; the hotel's PMS is the source of truth for rooms | The host in the marketplace's editor, or a vacation-rental PMS in "sync everything" mode |
| **Integration** | OpenTravel messages and proprietary APIs keyed by channel IDs; certification profiles | Proprietary partner APIs; iCal carries only busy dates, never the model |
| **Failure modes** | Room-type edits that cascade into lost products; attributes on the wrong level; pools that hide regulated units | Rooms-within-home double bookings; content that drifts from reality; hotels flattened into many listings |
| **Regulation** | Hotels are outside the EU STR Regulation; apartments and homes sold by the OTA are inside it | Nearly all supply is inside the STR Regulation; registration per listing is native |
| **What can be shared** | Property and unit identity, addresses and jurisdiction, registration numbers, attribute taxonomy, policy vocabulary, the offer contract | The same |

The judgement: **share the physical layer and the vocabulary, not the commercial layer.** The EU STR Regulation draws the line in the same place. Its scope excludes "hotels and similar accommodation" but includes the apartments an OTA sells ([Regulation (EU) 2024/1028, Art. 2–3](http://publications.europa.eu/resource/celex/32024R1028), 2024), so a mixed platform needs a per-unit classification, held in the shared physical core, that decides whether the registration gate applies. Room types, rate plans and listings encode how each marketplace earns its money and should evolve with that marketplace's product.

{id: property-and-listing-model--failure-modes}
## Failure Modes

The common mistakes, roughly in order of cost:

- **A home with quantity two.** A villa is mapped as a room type with quantity 2 because the manager copied a template, and the OTA sells it to two families for the same week: a **Double-Booked Night** caused by the model, not by sync. Guard: for single-home property types, the validation layer rejects quantity above one unless units are listed.
- **Room-type merges that destroy commercial state**, leaving existing reservations pointing at a deactivated object — see the second detail under The Accommodation Marketplace Model.
- **Rooms within a home sold independently** — see Rooms within a home.
- **Occupancy defined once, sold many ways** — see Occupancy, Beds and Configuration.
- **Unit unknown at reporting time**, so the platform guesses or reports at property level — see interface decision 2 under Architecture.

{id: property-and-listing-model--the-chief-architect-s-view}
## The Chief Architect's View

The supply model is a decade-long decision: most of Roomstead's assumptions about what a "property" is were made in Keystone's 2004 schema. Four decisions belong at group level.

**Who owns "what is being sold".** Each marketplace's supply catalog should have one owning team inside the supply bounded context of [Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts), and no other team should write to it. The place registry needs its own owner with a group mandate, because regulatory reporting, tax and trust depend on it as much as the marketplaces do.

**Which vocabulary is shared.** I would make the terms in the Concepts table binding across brands (the book's glossary) and refuse local synonyms. It is the cheapest convergence a group can buy, and One Stay's offer and reservation contracts depend on it.

**How the taxonomy is governed.** Put the canonical taxonomy under a small board with versioned releases, a mapping owner per channel and standard, and a deprecation policy, so that "do we add *workation-ready*?" is decided once rather than in five services.

**How identifiers are protected.** Enforce the identifier rules in review. Keystone's reservation module retires by the end of 2029, and partners' mappings must survive it.

What to watch on the supply dashboard:

- share of sellable units with a registry unit ID, by marketplace and country;
- share of reservations at pooled, regulated properties with an assigned unit before check-in;
- share of units in registration markets with a validated registration number;
- products per property (median and 99th percentile), as an early warning of Rate Plan Sprawl;
- taxonomy mapping loss: inbound codes that collapse or have no canonical value, per channel;
- "not as described" complaints traced to a specific attribute, as a measure of model accuracy rather than content quality.

{id: property-and-listing-model--questions-to-ask}
## Questions to Ask

1. Can we name, for every reservation in the last month, the physical unit the guest stayed in? If not, for which supply types and which markets?
2. Where do physical facts (occupancy, beds, floor area) end and commercial terms (rate plan, listing price, policies) begin in our schema, and which fields sit on the wrong side?
3. What happens to products, future ARI and existing reservations when a partner merges, splits or renames a room type?
4. How does our model represent a whole home that is also sold as separate rooms, and where in the code is the dependency enforced?
5. Which identifiers have left our systems (channel managers, regulators, metasearch, guests), and what is our policy for never changing or recycling them?
6. Is our attribute taxonomy our own, with versioned mappings to OpenTravel codes and each channel, or are we storing the channel's codes as our data?
7. Where is the jurisdiction of a unit derived, from which geocode, with which resolver version, and can we reproduce last year's decision?
8. If our hosted-stays platform added 500 boutique hotels next year, or our OTA added 100,000 single-owner homes, which part of the model would break first?

{id: property-and-listing-model--from-model-to-supply}
## From Model to Supply

The next chapter, [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding), follows a 120-room hotel and Carmen Ruiz's apartment from sign-up to first booking: how each is verified, which readiness checks a property type triggers, and how a registration number becomes a gate rather than a field. [Describing a Stay: Content, Media and Property Mapping](#content-and-media) then fills the model with descriptions and photos.

{id: property-and-listing-model--sources-and-evidence}
## Sources and Evidence

*Company engineering and investor sources*

- [Scaling beyond one: how Airbnb evolved its data architecture for a multi-product world](https://airbnb.tech/uncategorized/scaling-beyond-one-how-airbnb-evolved-its-data-architecture-for-a-multi-product-world/), Airbnb Tech (Lam, Lamba, Stober), 2026: parent listing with many offerings for Services; the separate-or-monolithic rule for data models (offline warehouse only).
- [Airbnb Q2 2026 shareholder letter](https://s26.q4cdn.com/656283129/files/doc_financials/2026/q2/Airbnb-Q2-2026-Shareholder-Letter-FINAL.pdf), Airbnb, 2026: boutique and independent hotels added in more than 20 destinations; hotels a single-digit share of nights.
- [Booking Holdings Form 10-K for FY2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), Booking Holdings, 2026: alternative accommodations about 36% of Booking.com room nights in 2025.
- [About Booking Holdings](https://www.bookingholdings.com/about/), Booking Holdings, n.d. (read October 2026): approximate property and listing counts.
- [Expedia Group Form 10-K for FY2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm), Expedia Group, 2026: about 3.6 million properties, about 2.4 million through Vrbo.

*Standards, regulation and documentation*

- [Connectivity APIs overview](https://developers.booking.com/connectivity/docs), Booking.com, n.d.: API modules for property, rooms, facilities, content, photos and licenses; OpenTravel 2003B.
- [Managing room types](https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-room-types.md), Booking.com, n.d.: room-type definition, 100-room-type limit, `Quantity`, subrooms for homes, cascade on deactivation.
- [Managing rate plans](https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-rate-plans), Booking.com, n.d.: rate plan as a name; 200 active rate plans; conditions on the roomrate.
- [Managing roomrates](https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-roomrates.md), Booking.com, n.d.: roomrate definition; 400 active roomrates.
- [Rates & Availability](https://developers.booking.com/connectivity/docs/ari), Booking.com, n.d.: inventory versus availability.
- [OTA_HotelRateAmountNotif](https://developers.booking.com/connectivity/docs/ota-rateamountnotif), Booking.com, n.d.: `InvTypeCode` and `RatePlanCode` as channel IDs.
- [PCT (Property Class Type) codes](https://developers.booking.com/connectivity/docs/codes-pct), Booking.com, n.d. (read October 2026): OpenTravel 2014B property types, hotel/home split, proprietary extensions, kitchen requirement.
- [RMA (Room Amenity Type) codes](https://developers.booking.com/connectivity/docs/codes-rma), Booking.com, n.d.: amenity code normalization (codes 28, 29 and 64 default to 28).
- [Managing room amenities](https://developers.booking.com/connectivity/docs/tsk-modify-room-amenities.md), Booking.com, n.d.: sunset of `OTA_HotelInvNotif` for home providers on 31 December 2026.
- [Availability and Rates API: introduction](https://developers.expediagroup.com/supply/lodging/docs/avail_and_rate_apis/avail_rates/getting_started/introduction), Expedia Group, 2025: updates by Expedia IDs only; inventory per room type.
- [Rapid Vrbo integration guide](https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-integration-guide), Expedia Group, n.d.: single-unit, single-rate-plan Vrbo inventory; unit configuration; weekly content refresh.
- [Constructing cancellation policies](https://developers.expediagroup.com/rapid/lodging/shopping/constructing-cancellation-policies), Expedia Group, n.d.: cancellation penalties as typed time windows.
- [Regulation (EU) 2024/1028 on short-term accommodation rental data](http://publications.europa.eu/resource/celex/32024R1028), European Union, 2024 (CELEX 32024R1028; applies from 20 May 2026): unit definition, hotel exclusion, registration per unit, activity data per unit.
- [El Tribunal Supremo anula el Registro Único de arrendamientos de corta duración](https://www.poderjudicial.es/cgpj/es/Poder-Judicial/Tribunal-Supremo/Noticias-Judiciales/El-Tribunal-Supremo-anula-el-Registro-Unico-de-arrendamientos-de-corta-duracion-por-considerar-que-el-Estado-carece-de-competencia-para-su-creacion), Consejo General del Poder Judicial, 2026: annulment of Spain's national registry; data-sharing and digital single window upheld.

*Research and practitioner sources*

- Productscape travel-accommodations and hosted-stays domain models (generic reference models in the author's sibling repository), 2026: residuality stress tests concluding that bookability is evaluated per unit, operator, jurisdiction and stay date. Not a description of any company.
- Barry M. O'Reilly, *Residues: Time, Change, and Uncertainty in Software Architecture*, Leanpub, 2024: the stress-testing method behind those models.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
