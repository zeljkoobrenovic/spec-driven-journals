{id: location-and-geo}
# 11. Where Is It? Location, Geocoding and Privacy

![Where Is It? Location, Geocoding and Privacy — logo](listing-systems-architecture/posts/11-location-and-geo/assets/images/11-location-and-geo/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow a Rotterdam bike and a Lyon apartment from a typed address to a searchable, mappable and privacy-safe location. Along the way you will see how addresses differ by country, what geocoders and their licences allow, how place hierarchies and geo indexes work, and how a precision policy decides what each audience may see.

> **WHY THE BUSINESS CARES:** In most listing verticals, location is the first filter a buyer applies. If the location is wrong, a listing is invisible. If the location is too precise, a private seller can be found at home by a stranger. If it relies on a geocoder's results the licence did not allow the marketplace to store, a supplier can send a legal letter that forces a rebuild.

> **WHY ARCHITECTS SHOULD CARE:** Location looks like one attribute but is really three: a precise point, a public point and a set of place references. Each one has its own consumers, accuracy, licence terms and privacy class. A design that stores one field and lets every consumer read it will leak data, break licences and produce search results that disagree with the map.

> **KEY POINTS:**
>
> * **Store three representations, not one.** Keep a restricted precise point, a public point derived from it deterministically by a precision policy, and a list of stable place IDs from a versioned gazetteer. Search radius, maps, landing pages and analytics each read the representation meant for them.
> * **Privacy is enforced on the server and by policy.** The precise point must never reach a client, a partner feed, structured data or an analytics event. Distances shown to buyers have to be computed from the public point, otherwise an attacker can work out the seller's address by measuring distances from several places.
> * **Geocoding is a licensing decision before it is a technical one.** Some providers restrict storage or which maps their results may appear on, some charge extra for permanent storage, and open data can carry share-alike terms. Pick providers per country and per use, record the terms with every coordinate, and keep the gazetteer under the group's control.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Attribute Junkyard** — free-text location strings ("R'dam centrum", "near the station") stand in for structured place references, so filters, alerts and landing pages each guess differently where a listing is.
> * **The Copy-Paste Country** — every country builds its own address model, geocoder integration and privacy rule, so a cross-border search, a group map tile or a privacy fix has to be built four times.
> * **Seeing Double** — when locations are imprecise or inconsistent, the same property listed by three agencies cannot be grouped, because location is the first key every duplicate detector relies on.

A marketplace answers "where is it?" millions of times a day, and its wrong answers look like search bugs. A buyer searching "within 10 km of Utrecht" gets a city bike that is 14 km away, because the seller's postcode was resolved to the centroid of a different municipality. A landing page for "apartments in Lyon" leaves out flats in Villeurbanne, which buyers think of as Lyon but which is a separate commune. A private seller's home address can be worked out from distances in the app. None of these is a search-ranking problem. Each comes from how location was modeled.

Part II models the listing as a small aggregate that references governed subdomains by ID ([The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate)). Location is the subdomain whose model decides whether a private seller's home stays private. **Location is not an attribute but a small subsystem**: country-specific address capture, geocoding, a gazetteer of places, geo indexes, a precision policy and a set of quality and fraud signals. Its gazetteer is reference data governed like the category tree in [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies), and it relies on [Photos Sell: Media Pipelines for Listings](#media-pipeline) to strip coordinates from photos. Later chapters build on it: it feeds search ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)), map discovery ([Searching by Place: Map, Polygon and Commute Search](#map-search)), alerts ([Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts)), duplicate detection ([One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)), fraud detection ([Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)) and SEO landing pages ([Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture)). It is also one of the few listing fields that is personal data almost every time a private seller is involved.

The chapter uses Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), as its running example. Veldmark runs four brands in eight countries, and its listing brands hold five different ideas of what a location is.

{id: location-and-geo--setting-the-scene-at-veldmark-five-answers-to-where-is-it}
## Setting the Scene at Veldmark: Five Answers to "Where Is It?"

In late March 2027, Lucía Ortega, Veldmark's Group Data Protection Officer, brings Ingrid Halvorsen, the new Group Chief Architect, a complaint from a Tradeyard Netherlands seller. A man had turned up at her door in Rotterdam about a sofa she had listed. She had never given him her address. Tradeyard showed only "3014 Rotterdam" on the listing page, so how had he found her?

Daan Visser's team reconstructs it in two days. The Tradeyard app sorted results by distance and showed distances to one decimal place ("2.3 km"). The distance was computed from the **centroid of the seller's full six-character postcode** (for example 3014 AB), which in a dense Dutch street covers a few dozen front doors. That centroid was also returned, with six decimal places, in the search API's JSON payload, which the app did not display but which anyone could read. With the payload alone, the man had a point within a few tens of meters of the seller's door. Without it, he could have searched from three places and intersected the three distance circles. The page showed a district; the system behind it handed out a doorstep.

![A city map where a shaded district is shown publicly, but three distance circles from different searchers intersect at one house's front door.](listing-systems-architecture/posts/11-location-and-geo/assets/images/11-location-and-geo/three-circles-find-a-door.jpeg)

**Figure 1:** *The page showed a district, but distances to one decimal place from a postcode centroid let three searches intersect at the seller's front door.*

Ingrid asks each brand how it handles location. The answers show why Common Ground needs one location model:

| Brand | What is captured | What is stored | What is shown publicly | Geocoder |
| --- | --- | --- | --- | --- |
| Tradeyard NL/BE | Postcode from the account profile; optional street | Postcode centroid in Yardstick's MySQL database and in Solr | Postcode district and city on the page; the precise centroid in the API | In-house postcode table built from the national address registers |
| Tradeyard PL/PT | Free-text city plus optional postcode | Coordinates from a commercial geocoder, kept indefinitely | City; map pin at the stored coordinates on an open-data map | Commercial API on a standard plan |
| Motorvane | Dealer branch address from the contract; postcode for private sellers | Exact dealer address; postcode centroid for private sellers | Dealer address in full; city for private sellers | A second commercial API |
| Hearthly FR | Full address from agency feeds | Exact point from the French national address base | The agency chooses: exact, street, or district | Self-hosted geocoder on the national address base |
| Hearthly ES (former Casavista) | Full address, including private landlords' rentals | Exact point | **Exact pin for every listing, including private landlords** | Third commercial API |

Each of these rows was reasonable when it was built. Together they mean that Veldmark cannot answer a regulator who asks what location data it publishes about private individuals. It cannot say whether its Polish and Portuguese coordinates were licensed for storage. It cannot draw one group map, run one radius search across Motorvane's German and Austrian sites, or compare rents per neighborhood across Hearthly's two countries. The rest of this chapter is the model Ingrid's team proposes.

{id: location-and-geo--concepts-what-location-means-for-a-listing}
## Concepts: What "Location" Means for a Listing

{id: location-and-geo--four-kinds-of-location}
### Four kinds of location

A listing can carry several locations, and confusing them is the first modeling mistake.

| Kind | Definition | Example | Who needs it |
| --- | --- | --- | --- |
| **Item location** | Where the thing being sold physically is | The Lyon apartment; the Essen Golf on Autohaus Ruhrblick's lot | Search, maps, duplicate detection, valuation |
| **Seller location** | Where the seller is based | A dealer's head office; a private seller's home | Trust, regulatory disclosure, contact routing |
| **Handover location** | Where buyer and seller meet or where the item is collected | "Pickup near Rotterdam Centraal" | Buyer convenience; safety advice |
| **Service area** | The region a seller serves, for services and jobs | A removals company covering South Holland; a remote-friendly job | Search for services and jobs, where a point is the wrong shape |

For goods, item and seller location usually coincide, which is why many systems store one field. They part ways often enough to matter: a dealer group with ten branches, a seller who keeps the item at a parent's house, a property listed by an agency in another city, and every shipped item. When Tradeyard Safe Deal ships a parcel (see [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments)), the item location stops being a hard filter and becomes a delivery-cost input. A listing flagged "ships nationwide" should match a radius search it would otherwise fall outside.

{id: location-and-geo--addresses-are-country-shaped}
### Addresses are country-shaped

An **address model** is the structure a marketplace uses to capture and store a postal address. There is no universal one. The postcode alone shows the range across Veldmark's countries:

| Country | Postcode shape | How specific it is | Practical consequence |
| --- | --- | --- | --- |
| Netherlands | Four digits plus two letters ("3014 AB") | Six-character code covers part of a street; the four-digit part a neighborhood | Postcode plus house number identifies an address; the four-digit part is a natural public district |
| Belgium | Four digits | A municipality or part of one | Bilingual place names: one postcode, two official names in Brussels |
| Germany, Austria | Five digits (DE), four (AT) | Delivery districts; not administrative units | A postcode can cross municipal borders, so postcode and municipality must be stored separately |
| France | Five digits | Delivery offices; one postcode can cover several communes, and Lyon, Paris and Marseille split by arrondissement | Postcode alone cannot answer "which commune" |
| Spain, Portugal, Poland | Five digits (ES), "1234-567" (PT), "12-345" (PL) | Varies from district to street segment | Validation rules per country; formats must be data, not code |

Industry practice is to parse free-text addresses into components before matching. The open-source **libpostal** library does this with a statistical parser trained on OpenStreetMap and other open address data. Its README reports 99.45% full-parse accuracy on held-out data and normalization in "60+ languages" ([libpostal](https://github.com/openvenues/libpostal), n.d.). Its model is about 1.8 GB, which in practice means it runs as a shared service, not inside every application.

{id: location-and-geo--geocoding-and-its-outputs}
### Geocoding and its outputs

**Geocoding** turns an address or place name into coordinates. **Reverse geocoding** turns coordinates into an address or place. Both are inexact, and a geocoder's result should always come with three things the listing keeps:

1. **Match level** — what the coordinate actually represents: a rooftop or building entrance, an interpolated position along a street, a postcode centroid, a locality centroid. A "point" that is the centroid of Rotterdam is a very different fact from a point at a front door, even though both are two numbers.
2. **Confidence** — the geocoder's own score, which drives whether the result is accepted, shown to the seller for confirmation, or sent to review.
3. **Provenance** — which provider, which data version, under which licence, on which date. This is what lets a team answer a licensing audit or re-geocode everything from one provider when a contract ends. [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) owns provenance for derived attributes in general; location is the case where the licence makes it mandatory.

{id: location-and-geo--places-gazetteers-and-hierarchies}
### Places, gazetteers and hierarchies

A **gazetteer** is a reference dataset of named places (countries, regions, municipalities, districts, neighborhoods) with stable identifiers, names in several languages, geometries and parent-child relations. Two public models show the design space:

- **OpenStreetMap's `admin_level`** runs from 2 to 10. Level 2 "is almost always a de-facto independent country", but higher levels "vary in meaning between countries": a city can sit anywhere from level 4 (Berlin) to level 10 ([OpenStreetMap Wiki](https://wiki.openstreetmap.org/wiki/Key:admin_level), n.d.). A marketplace cannot use the levels as a cross-country hierarchy without a mapping per country.
- **Who's On First** gives each place a stable 64-bit ID and placetypes from continent down to neighbourhood, macrohood and microhood. It supports **multiple hierarchies** for places with more than one parent, and it advises querying by ID, never by name ([Who's On First](https://whosonfirst.org/docs/placetypes/), n.d.).

Marketplaces need both multiple parents and places no administration defines. A place can have several parents: Lyon's 7th arrondissement is in the commune of Lyon, in the Métropole de Lyon and in the Rhône department. And buyers use names that do not match any administrative unit ("Randstad", "Costa del Sol", "Eixample"). The gazetteer therefore holds two kinds of place: **administrative places** imported from official sources, and **marketplace places** curated by the marketplace for how buyers search, each with a geometry and links to the administrative places it overlaps.

**Listings reference places by ID, and every listing carries the IDs of all its ancestors.** "All listings in Rotterdam" then becomes a term filter on a place ID, not a polygon query, and renaming a place changes no listing.

{id: location-and-geo--location-precision}
### Location precision

**Location precision** is the level of detail at which a location is known, stored or shown. A shared scale makes policies writable. Veldmark adopts six levels:

| Level | Name | Example (Tradeyard NL) | Example (Hearthly FR) |
| --- | --- | --- | --- |
| P0 | Country | Netherlands | France |
| P1 | Region | South Holland | Auvergne-Rhône-Alpes |
| P2 | Locality | Rotterdam | Lyon |
| P3 | District | Postcode area 3014; a neighborhood | Lyon 7e arrondissement |
| P4 | Street or block | A street segment | The street name, without house number |
| P5 | Exact | Address with house number; rooftop point | Address, building and unit |

Precision applies three times over: **capture precision** (what the seller or feed gave), **stored precision** (what the platform keeps after geocoding) and **display precision** (what a given audience may see). The design mistake in the Rotterdam case was to let display precision follow stored precision by default, with the page template as the only place that blurred it.

{id: location-and-geo--geo-indexes}
### Geo indexes

A **geo index** is a data structure that makes spatial queries cheap: "points within this circle", "points inside this polygon", "counts per map tile". Four families matter in listing systems:

- **The search engine's native types.** Elasticsearch and OpenSearch index `geo_point` and `geo_shape` fields in BKD trees. Shapes are tessellated into triangles, the precision is about 1e-7 degrees, and tessellation cost grows with vertex count ([Elastic documentation](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-shape), n.d.). This is what radius and polygon queries should use at query time.
- **Geohash.** A base-32 string built by interleaving latitude and longitude bits. Shared prefixes mean nearby cells, so prefixes work as keys in stores without spatial indexes. Two points a meter apart on either side of a cell edge can have completely different prefixes, so proximity queries must always include neighboring cells.
- **H3.** Uber's hexagonal hierarchical grid, published in 2018, has 16 resolutions, each about one-seventh the area of the one above. Hexagons were chosen because a hexagon's center is the same distance from all six neighbors ([Uber, 2018](https://www.uber.com/blog/h3/)). Children are only approximately contained in their parents. Average cells range from 36.13 km² at resolution 6 to 0.105 km² at resolution 9 ([H3 documentation](https://h3geo.org/docs/core-library/restable/), n.d.).
- **S2.** Google's library projects a cube onto the sphere and orders cells along a Hilbert curve. It has levels 0 to 30 and 64-bit cell IDs that preserve locality, and a region coverer approximates any shape with a small set of cells ([S2 Geometry](https://s2geometry.io/devguide/s2cell_hierarchy), n.d.). Airbnb's 2026 paper on embedding-based retrieval uses S2 cells as a listing-location feature ([Airbnb, 2026](https://arxiv.org/html/2601.06873v1)).

The four are complementary: **the engine's native types serve queries, H3 serves aggregation and privacy, and S2 or geohash serve key-value lookups.** The trade-offs section compares them job by job.

{id: location-and-geo--architecture-three-representations-and-the-services-behind-them}
## Architecture: Three Representations and the Services Behind Them

{id: location-and-geo--the-location-value-object}
### The location value object

Inside the listing aggregate ([The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate)), location is a value object with three parts that are written together but read by different consumers.

| Part | Contents | Classification | Readers |
| --- | --- | --- | --- |
| **Precise location** | Normalized address components; precise point; match level; confidence; provider and data version; capture channel | Restricted personal data for private sellers; confidential for professionals | Geo service, duplicate detection, fraud models, valuation; never clients or partners |
| **Public location** | Public point; display precision level; display label ("3014 Rotterdam"); radius of uncertainty for maps | Public | Search documents, listing pages, maps, apps, partner feeds, structured data |
| **Place references** | Place ID at the finest level allowed for display, plus all ancestor IDs, with the gazetteer version | Public | Search filters, landing pages, alerts, analytics, ad targeting |

Each part can be recomputed from the one above it: the public point from the precise point and the policy, the place references from the public or precise point and the gazetteer. That is what makes policy changes and boundary reforms backfills rather than migrations.

A private seller's precise listing location is personal data; the gazetteer is not. The GDPR is explicit that **location data is one of the identifiers that make a person identifiable** ([GDPR Art. 4(1)](https://gdpr-info.eu/art-4-gdpr/), unofficial reproduction). The real-estate Productscape domain model behind this book's research classifies its geo reference data as internal and non-personal, but the listing that carries a private owner's location as "possible-personal". Its general-listings model treats the listing as non-personal, which the model's own review notes is wrong for private sellers, whose listings routinely embed location and contact data (see the research digest).

{id: location-and-geo--components}
### Components

![Diagram: Location enters as text and leaves as two different products](listing-systems-architecture/posts/11-location-and-geo/assets/images/11-location-and-geo/fig02-location-enters-text-leaves-two-different.jpeg)

**Figure 2:** *Location enters as text and leaves as two different products. Everything to the right of the precision policy engine sees only what the policy allows, while duplicate detection and fraud models read the restricted store through an audited path.*

The components and their responsibilities:

1. **Address capture per country.** The form, app and feed mappers know the country's address shape, validate postcodes and offer autocomplete. Address formats are configuration in the gazetteer, not code in the form. That is the same configuration-over-code argument [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) makes for the platform as a whole.
2. **Geocoding gateway.** One internal API in front of all providers. It routes by country and use, caches within what each licence allows, records provenance and match level, and enforces per-provider quotas. No product service calls a geocoding provider directly; that rule alone makes a provider switch a configuration change.
3. **Gazetteer service.** Owns place IDs, names in every language, aliases, geometries, hierarchies and versions. It is reference data in the same sense as the category tree in [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) and needs the same governance: versioned releases, change notes, mappings when places split or merge.
4. **Place resolver.** Given a point, returns the place IDs that contain it and their ancestors, using the gazetteer version stamped on the result.
5. **Precision policy engine.** Given the precise location, the brand, category, seller type and the seller's own choice, it produces the public part. It is a pure function with versioned rules, which makes it testable and auditable.
6. **Restricted location store.** Holds the precise part, separated from the listing's public read models and with access logged. [System of Record and Read Models: Listing Data Management](#listing-data-management) owns the general model of read models and erasure; for location, the separation is the control.

{id: location-and-geo--deriving-the-public-point}
### Deriving the public point

The precision policy can derive the public point in two sound ways:

- **Snap to a cell.** Replace the precise point with the center of the H3 cell containing it, at a resolution chosen for the display level. At resolution 7 the average cell has an edge of 1.41 km; at resolution 8, 0.53 km ([H3 documentation](https://h3geo.org/docs/core-library/restable/), n.d.). Every listing in the same cell gets the same public point, which is honest and simple, but in sparse rural areas a cell may contain a single house.
- **Seeded offset.** Move the point by a random distance and bearing within a radius, using a seed derived from the listing ID. **The offset must be deterministic.** If it is drawn again on every render, every edit or every relisting, an attacker who collects enough versions can average them back to the true point.

![Left, every render shows the same offset pin; right, many redrawn pins scatter around a house and their average points back to it.](listing-systems-architecture/posts/11-location-and-geo/assets/images/11-location-and-geo/seeded-offset-vs-redrawn.jpeg)

**Figure 3:** *A public offset must be seeded by the listing ID: if it is drawn again on every render or edit, enough versions average back to the true point.*

Two refinements apply to both. First, the public point must stay inside the public place: a snapped or offset point for a Rotterdam listing that lands in the river or in the next municipality creates support tickets and wrong landing pages. Second, in sparse areas the policy should coarsen automatically until the public area contains a minimum number of addresses. The national address registers make that count possible.

The best-documented public example of display obfuscation is Airbnb's. By default, its map shows a radius "within about a half mile (less than 1 kilometer) of the street address", and "guests don't receive the address until their reservation is confirmed" ([Airbnb, 2025](https://airbnb.com/resources/hosting-homes/a/setting-expectations-with-an-accurate-location-491)). The principle carries over to classifieds directly: the exact address is released when there is a reason to release it, to a person the platform knows, not when the listing is published.

{id: location-and-geo--the-rule-for-distances}
### The rule for distances

Distances leak locations, as the Rotterdam case showed. A distance from a searcher's chosen point to a listing's precise point, shown with enough precision, turns every search into a measurement, and three measurements locate the seller. **Distances shown to users, and distance sorting, must be computed from the public point**, and displayed values should be rounded to the precision of the public location (whole kilometers for district-level listings). Radius filters can still use the public point; the fuzziness at the edge of the circle is the same size as the fuzziness of the location, which is acceptable.

Internal consumers are different. Duplicate detection for real estate needs the precise point, since two listings of the same flat should agree within meters ([One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) uses H3 resolution 9 cells as a blocking key). Fraud models need it to compare a listing's location with the account's history. These reads go to the restricted store and are logged.

![Diagram: One precise point, many audiences](listing-systems-architecture/posts/11-location-and-geo/assets/images/11-location-and-geo/fig04-one-precise-point-many-audiences-public.jpeg)

**Figure 4:** *One precise point, many audiences. Public consumers see a derived point and place references; only internal models with a documented purpose read the precise point, and every distance a buyer sees comes from the public side.*

{id: location-and-geo--location-in-the-listing-event-and-the-search-document}
### Location in the listing event and the search document

The listing event contract ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)) carries the public part and the place references, not the precise part. Consumers that need the precise point — duplicate detection, fraud scoring, valuation — call the restricted store with their own credentials. The cost is an extra call for those consumers. The gain is that the event stream, the data lake and every downstream copy stay free of precise private locations. That matters, because [System of Record and Read Models: Listing Data Management](#listing-data-management) found seven copies of Femke's bike listing alone, and erasing a precise point from seven copies is much harder than never having written it there.

The search document ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)) then holds:

- a `geo_point` for the public point, used by radius filters, distance sorting and map clustering;
- a keyword array of all place IDs and ancestors, used for "in Lyon" filters and for landing pages;
- one or two H3 cell IDs at the resolutions used for aggregation and heat maps;
- the display label and display level, so the result card does not need a second lookup.

For real estate, the search document may also hold a precise `geo_point` that is never returned in responses but is used for polygon queries when the agency has chosen exact display. [Searching by Place: Map, Polygon and Commute Search](#map-search) owns the details of polygon, isochrone and clustering queries; this chapter's contribution is the rule about which point those queries may use.

{id: location-and-geo--radius-polygon-and-place-getting-the-semantics-right}
## Radius, Polygon and Place: Getting the Semantics Right

Each kind of location query hides a decision that produces a visible bug if left implicit.

**"Within 10 km of Utrecht" — from where?** The radius has to start from a point. If the buyer typed a city, the choice is between the city's centroid, its main station, or a population-weighted center. For a small town the choice makes little difference. For Rotterdam it matters: the municipality includes Hoek van Holland on the coast, about 30 km from the city center, so the geometric centroid of the municipality can fall somewhere unhelpful. Veldmark's gazetteer stores an explicit **reference point** for every place used as a search origin, curated for the largest cities and computed for the rest.

**"In Lyon" — which Lyon?** The commune of Lyon has nine arrondissements. Villeurbanne, which most buyers consider part of Lyon, is a separate commune inside the Métropole de Lyon. "Apartments in Lyon" can mean the commune, the metropolis or a buyer's mental map. The answer is not to pick one silently but to offer both as places: an administrative place ("Lyon, commune") and a marketplace place ("Lyon and surroundings") with a curated geometry. The query-understanding layer decides which one a typed query means ([What Did They Mean? Query Understanding and Autocomplete](#query-understanding)); the gazetteer makes both possible.

![A stylized city with a commune outline, a neighboring commune, and a dashed marketplace place enclosing both, matching a buyer's mental map.](listing-systems-architecture/posts/11-location-and-geo/assets/images/11-location-and-geo/which-lyon-places.jpeg)

**Figure 5:** *"In Lyon" can mean the commune or the wider area buyers have in mind, so the gazetteer holds administrative places and curated marketplace places, each with its own ID.*

**Brussels in two languages.** The Brussels-Capital Region has 19 municipalities with official French and Dutch names. A Tradeyard Belgium buyer may type "Elsene" or "Ixelles" for the same place. Names belong to place IDs, not the reverse, and alias lists cover common spellings and English names ("The Hague", "Den Haag", "'s-Gravenhage").

**Polygon or place?** A drawn polygon and an administrative place answer different questions. A polygon is a geometric filter on points. An administrative place is a containment fact that was computed once, when the listing was published, against a specific gazetteer version. They can disagree at boundaries, for example when a listing's public point was snapped across a municipal line. The rule Veldmark adopts is that **place filters use stored place IDs and polygons use public points**, and the listing page always names the place that was stored, so what the buyer sees is consistent with the filter that found it.

**Cross-border radius.** Motorvane operates in Germany, the Netherlands, Poland and Austria. A buyer in Aachen searching "within 50 km" is, geographically, searching parts of three countries. Whether the result should include Motorvane's Dutch listings is a product decision, but it is only possible if the three countries' listings share one coordinate system, one gazetteer and one index or a federated query. A **country fork in the location model rules out cross-border search** before anyone has decided whether it is wanted.

**Travel time instead of distance.** For housing and jobs, buyers care more about commute time than distance. Rightmove's "My Places" feature computes travel times from listings to a user's saved places using the third-party TravelTime API. The vendor's case study says Rightmove chose a fixed annual licence with unlimited requests partly to avoid the cost growth of pay-as-you-go pricing ([TravelTime](https://traveltime.com/case-study/rightmove-property-poi-search-traveltime), n.d.; a vendor case study). The lesson for this chapter is that **the routing provider's commercial model is an architectural constraint**, in the same way as the geocoder's licence. [Searching by Place: Map, Polygon and Commute Search](#map-search) covers isochrone queries in depth.

{id: location-and-geo--geocoding-providers-and-licences}
## Geocoding Providers and Licences

{id: location-and-geo--what-the-terms-say}
### What the terms say

Licences for geocoding and map data differ in ways that decide what a marketplace can store. The terms below were checked on the providers' pages in October 2026; providers change them, so treat this as a snapshot.

| Option | What the terms say | Consequence for a listing system |
| --- | --- | --- |
| **Google Geocoding API** | Caching and storage are generally restricted, but place IDs may be stored indefinitely. Results displayed on a map must be shown on a Google Map ([Google, last updated 2026-10-16](https://developers.google.com/maps/documentation/geocoding/policies)) | A permanent table of listing coordinates, shown on a non-Google map, does not fit these terms. Store place IDs and re-geocode as the terms allow, or use another provider for stored coordinates |
| **Mapbox Geocoding** | Default "temporary" results "are not allowed to be cached"; `permanent=true` allows storing results indefinitely and requires a payment method or contract ([Mapbox](https://docs.mapbox.com/api/search/geocoding/), n.d.) | Storage rights are a separately priced product. Budget for permanent geocoding if coordinates live in the listing database |
| **OpenStreetMap Nominatim, public instance** | "An absolute maximum of 1 request per second"; bulk geocoding discouraged; results must be cached by the user ([OSM Foundation](https://operations.osmfoundation.org/policies/nominatim/), n.d.) | Unusable for production ingestion. Self-host Nominatim or another geocoder, or buy a hosted OSM-based service |
| **OpenStreetMap data** | Open Database License: attribution required; a database built on the data may be distributed "only under the same license" ([OpenStreetMap](https://www.openstreetmap.org/copyright), n.d.) | Get legal advice on whether an enriched place or address database counts as a derivative database before mixing it with proprietary data |
| **Pelias** | Open-source geocoder on Elasticsearch; imports OSM, OpenAddresses, Who's On First and GeoNames; MIT licensed ([Pelias](https://github.com/pelias/pelias), n.d.) | A natural self-hosted option for a marketplace that already runs Elasticsearch or OpenSearch, and a source of place hierarchies |
| **National address registers** | The Dutch BAG is open data under the Creative Commons Public Domain Mark, with municipalities as the source holders ([Kadaster](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag), n.d.). France's Base Adresse Nationale is published under Licence Ouverte 2.0 ([data.gouv.fr](https://www.data.gouv.fr/fr/datasets/base-adresse-nationale/), updated 2026-10-19). Great Britain's OS Open UPRN publishes coordinates for about 40 million addressable locations, free to use ([Ordnance Survey](https://www.ordnancesurvey.co.uk/products/os-open-uprn), n.d.) | Where a good open register exists, it is usually the best primary geocoding source: authoritative, storable and free. Coverage and licence vary by country |

The general rule is that **the provider is chosen per country and per use, and the licence is a property of every stored coordinate.** Geocoding a listing for storage and indexing is one use. Autocomplete in the insertion form is another, with different volume and different terms; public Nominatim, for example, explicitly prohibits client-side autocomplete. Displaying a base map is a third, often from a different provider again.

{id: location-and-geo--building-versus-buying}
### Building versus buying

Most marketplace groups end up with a mix:

- **National registers, self-hosted**, where they exist and are open: the Netherlands and France in Veldmark's footprint. They give authoritative, storable rooftop points for addresses and stable address identifiers that also help duplicate detection.
- **A commercial geocoder with storage rights** for countries without a usable open register and for messy free-text input.
- **An open-data gazetteer** (built from OSM, Who's On First or national boundary datasets) for administrative places, extended with the marketplace's own curated places. The legal review of share-alike terms happens once, at the gazetteer boundary.

The volumes that drive the cost are usually smaller than people fear. Most private listings are geocoded from a postcode, which is a lookup in a local table, not a provider call. Full address geocoding is concentrated in real estate and dealer feeds, where addresses change rarely and results can be stored.

{id: location-and-geo--in-practice-at-veldmark}
## In Practice at Veldmark

{id: location-and-geo--the-rotterdam-city-bike}
### The Rotterdam city bike

Femke lists her €240 city bike on Tradeyard Netherlands on Sunday 7 March 2027 at 19:42. Her account profile holds her six-character postcode in Rotterdam. Under the policy Ingrid's team adopts later that year, the bike's location would be processed like this:

1. **Capture.** The insertion form pre-fills the postcode from her profile and asks whether the bike is there. She confirms. Her photos were taken in her hallway, and their EXIF metadata carries GPS coordinates within a few meters of her door. The media pipeline strips EXIF on upload ([Photos Sell: Media Pipelines for Listings](#media-pipeline)); this chapter's privacy rule would be pointless without it, since EXIF carries `GPSLatitude` and `GPSLongitude` tags ([ExifTool](https://exiftool.org/TagNames/GPS.html), n.d.).
2. **Geocode.** The postcode resolves, through the gateway, to the centroid of that six-character postcode from the national address register. Match level: postcode centroid. Stored precision: close to P5 in a dense street, which is exactly why it is restricted.
3. **Place references.** The resolver returns the four-digit postcode area 3014, the district, the municipality of Rotterdam, the province of South Holland and the Netherlands, all stamped with the gazetteer version.
4. **Public location.** The Tradeyard private-seller rule sets display level P3. The public point is the center of the H3 resolution-7 cell that contains her postcode centroid, constrained to stay inside postcode area 3014. The label reads "3014 Rotterdam".
5. **Indexing.** The search document receives the public point, the place IDs and the label. The event carries the same.
6. **Search.** A buyer 2.6 km away sees "about 3 km" and a shaded district on the map. Of the 312 saved searches the bike matches, those with a radius are evaluated against the public point ([Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts)).

Nothing in steps 4 to 6 can reveal more than the district. The precise centroid exists only in the restricted store. The 20:11 fake payment link that reaches Femke that evening is a messaging and fraud problem, not a location one ([From Interest to Contact: Messaging and Lead Management](#messaging-and-leads)); but a scammer who wanted to turn up at her door instead would now find nothing more precise than a 5 km² cell.

{id: location-and-geo--the-lyon-apartment}
### The Lyon apartment

The three-room, 68 m² flat in Lyon 7e arrives in May 2027 from three agencies through two software vendors and Keybridge. The feeds carry full addresses with differences in spelling and one with the unit number.

1. **Parse and normalize.** The parser splits street, number, postcode and commune; normalization expands abbreviations ("av." to "avenue") so the three addresses compare equal.
2. **Geocode.** The French national address base gives a rooftop point for the building and a stable address identifier. All three listings resolve to the same building within a few meters.
3. **Place references.** Lyon 7e arrondissement, commune of Lyon, Métropole de Lyon, Rhône, Auvergne-Rhône-Alpes, France, plus Hearthly's curated places that contain the point.
4. **Precision.** Each agency chooses its display level in its account settings ([Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts)). Agence Rhône Habitat shows the street without a house number (P4); the other two show the arrondissement (P3). The listing page for the clustered property uses the coarsest choice among the agencies whose listings are shown together, so one agency's discretion is not overridden by another's openness.
5. **Duplicate detection.** [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) reads the precise points from the restricted store, blocks on H3 resolution-9 cells and address identifier, and clusters the three listings into one canonical property.
6. **Valuation.** Valuo uses the precise point and the property's attributes to estimate €372,000 to €401,000, drawing on geolocated public transaction data for comparables.

Agencies hide the street for privacy and for business. The owner may still live there, and an agency that publishes the exact address invites buyers to approach the owner directly, bypassing the agency. Whatever the reason, the portal's job is to honor the choice consistently, including in the map, the structured data and the alert e-mail.

{id: location-and-geo--the-barcelona-fake-rental-ring}
### The Barcelona fake-rental ring

In July 2027, 26 accounts post 180 fake rental listings in Eixample with photos stolen from real listings, priced about 35% below market and asking for deposits by bank transfer. The ring is detected through perceptual-hash matches against existing listings and price anomalies ([Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)). Location is part of both signals:

- **Price anomaly is a location feature.** "35% below market" means below the median asking rent for comparable flats in the same small area. Hearthly computes that median per H3 resolution-8 cell (average area 0.737 km²) and property type. Without a consistent grid, "the market" would be the whole of Barcelona, and the anomaly would disappear in the average.
- **Stolen photos come with a location.** Many of the stolen photos belonged to listings in other districts. A perceptual-hash match between two listings whose precise points are kilometers apart is a much stronger fraud signal than a match between two listings in the same building, which may be the legitimate case of two agencies listing the same flat.

After the incident, Aisha Rahman's team adds two more location signals for new accounts: a listing location far from every location the account has shown in its device and network history, and a burst of listings concentrated in one high-demand district. Neither signal is decisive alone, but both are cheap and work well in combination.

{id: location-and-geo--location-quality-measured}
### Location quality, measured

Ingrid's team defines a small set of location quality metrics per brand and country, published weekly:

| Metric | Definition | Tradeyard NL, Q3 2027 | Hearthly FR, Q3 2027 |
| --- | --- | --- | --- |
| Match-level mix | Share of listings geocoded at rooftop, street, postcode, locality level | 97% postcode centroid; 2% street; 1% locality | 88% rooftop; 9% street; 3% locality |
| Low-confidence rate | Share of new listings whose geocode fell below the acceptance threshold | 0.4% | 2.1% |
| Coordinate defects | Points at (0, 0), outside the country, or with latitude and longitude swapped | 31 listings | 112 listings |
| Place drift | Listings whose stored place IDs disagree with the current gazetteer version | 0 after the January backfill | 4,800 pending a commune merger update |
| Precise-point exposure | Precise points found in any public payload by the weekly scan | 0 (target) | 0 (target) |

These figures are Veldmark's illustrative baselines. Swapped coordinates are a perennial bug because GeoJSON and WKT order coordinates as longitude, latitude, while most people say "latitude, longitude" ([Elastic documentation](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-shape), n.d.). A Lisbon listing with swapped coordinates lands in the Indian Ocean. The quality check is trivial; the damage when nobody runs it is not.

{id: location-and-geo--trade-offs}
## Trade-offs

{id: location-and-geo--where-to-store-location}
### Where to store location

| Option | How it works | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- | --- |
| **Single point per listing** | One latitude-longitude field, read by everyone | Simple; fast to build | Privacy depends on every consumer blurring correctly; no audit; licence unclear | A prototype, or a vertical where every listing is a business at a public address |
| **Precise plus public point** | Restricted precise point; derived public point | Privacy enforced once; distances safe | No place hierarchy, so "in Rotterdam" needs polygons | Small single-country marketplaces |
| **Three representations** | Precise, public, and place references with ancestors | Privacy, consistent filters, cheap landing pages, backfillable | A gazetteer to run and govern; more fields per event | Multi-country groups and any marketplace with SEO landing pages |
| **Property-first** (real estate) | Location belongs to a persistent property entity; listings reference it | Location agreed once for every listing of a property; supports valuation and history | Requires entity resolution and a property store | Real-estate portals at scale ([One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)) |

{id: location-and-geo--which-geo-index-for-which-job}
### Which geo index for which job

| Job | Best fit | Why | Avoid |
| --- | --- | --- | --- |
| Radius and polygon filters at query time | Engine-native `geo_point` and `geo_shape` | Exact geometry; maintained by the engine | Geohash prefix filters, which miss neighbors at cell edges |
| Map clustering by tile | Engine tile aggregations | Matches map zoom levels | Precomputed clusters that go stale as inventory churns |
| Heat maps, local price statistics, privacy cells | H3 | Uniform neighbors and areas; the same cell everywhere | Administrative areas of very different sizes |
| Key-value lookups and range scans | S2 or geohash | Locality-preserving 64-bit or string keys | Engine queries for simple lookups |
| "All listings in place X" | Place-ID term filter | Cheap; stable across geometry changes | Polygon queries on large administrative areas |
| Duplicate blocking (real estate) | H3 fine resolution plus address identifier | Candidate pairs limited to nearby listings | Exact coordinate equality, which misses geocoder noise |

{id: location-and-geo--public-point-methods}
### Public-point methods

| Method | Privacy | Map quality | Main risk |
| --- | --- | --- | --- |
| Show place label only, no pin | Strong | Poor; buyers cannot judge distance | Lower engagement on map-led verticals |
| Snap to H3 cell center | Good in dense areas; weak where a cell holds one house | Pins stack on cell centers | Sparse-area exposure unless the policy coarsens |
| Deterministic seeded offset | Good if seeded per listing and bounded to the place | Natural-looking spread | Re-randomized offsets can be averaged out |
| Circle of uncertainty | Good | Honest, but large circles look vague | Circles drawn around the precise point give the center away |

The last row is a classic mistake: a "privacy circle" centered on the real address reveals the address as its center. The circle must be centered on the public point.

{id: location-and-geo--vertical-differences}
## Vertical Differences

| Dimension | General classifieds | Real estate | Automotive | Jobs and services |
| --- | --- | --- | --- | --- |
| What is located | The item, usually at the seller's home | A persistent property | A vehicle on a dealer lot or at a private home | A workplace, a service area, or "remote" |
| Typical capture | Postcode from the profile | Full address from agency software | Dealer branch address from the contract; postcode for private sellers | Office address; region; remote flag |
| Default public precision | District (P3) for private sellers | Agency's choice; district for private landlords | Exact for dealers (a business address); locality or district for private sellers | Locality for workplaces; region for service areas |
| Role of location in search | Radius filter, often secondary to category | **The primary filter**; maps, polygons, commute | Radius matters, but buyers travel far for the right car | Commute; remote and hybrid flags change the shape |
| Location in duplicate detection | Weak | **Central**: same building, same unit | Weak; the VIN identifies the car ([From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment)) | Moderate: same employer, same office |
| Regulatory angle | GDPR for private sellers | GDPR; mandatory disclosures linked to the property, such as France's energy class | Trader address display for dealers ([Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)) | Equality law on job ads; remote-work tax questions |
| Shipping | Changes radius semantics for shipped goods | Not applicable | Occasional delivery services | Not applicable |

Real estate is the vertical where location carries the most weight. The property outlives every listing of it, so its location is resolved once against the property, not per listing ([Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements)). General classifieds is the vertical where location is most often personal data. Automotive sits in between: dealer addresses are public business information, and the car's identity comes from the VIN, not from where it stands.

{id: location-and-geo--failure-modes}
## Failure Modes

1. **The precise point leaks through a side door.** The page shows a district, but the precise point is in the search API response, the JSON-LD structured data, an image's EXIF, a sitemap, an analytics event, a partner feed or an alert e-mail's static map. The control is architectural: the public read models never receive the precise point, and a weekly scan of public payloads looks for coordinates that match restricted ones.
2. **Distances give away the address.** Precise distances from a searcher's point to a seller's precise point allow trilateration. Compute from the public point; round to the display precision.
3. **Jitter that is not deterministic.** A random offset recomputed on each request or edit is averaged out by anyone who collects enough samples.
4. **Licence debt.** Coordinates from a provider whose terms forbid storage, or whose results may appear only on its own maps, sit in the listing database for years. Discovering this during a provider negotiation or an acquisition's due diligence is expensive. Record provider and licence per coordinate from day one.
5. **Name-based place matching.** Systems that join on place names break on bilingual names, renames and homonyms; there are several Bergens in Veldmark's markets alone. Join on IDs.
6. **Stale place references after boundary reforms.** Municipal mergers and boundary changes happen every year in several European countries. If place IDs were computed once and never recomputed, landing pages and filters quietly diverge from reality. Recompute ancestors as a backfill each time the gazetteer version changes, the same way [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) handles category migrations.
7. **Centroid fallbacks treated as precise.** A listing geocoded to "Rotterdam" lands on the city centroid. If the match level is not stored, that listing appears in every "near the center" search and distorts local price statistics. Low-precision listings should be excluded from fine-grained statistics and shown as area matches.
8. **Polygon queries that explode.** A hand-drawn polygon with thousands of vertices, or an administrative boundary at full resolution, makes every query slow, because shape tessellation cost grows with vertex count. Simplify shapes before querying and use place-ID filters for administrative areas.
9. **One country's model imposed on another.** A Dutch-style "postcode plus house number" form fails in Portugal and Poland, and a French "commune" field means little in the Netherlands. Address formats belong in configuration per country.

{id: location-and-geo--the-chief-architect-s-view}
## The Chief Architect's View

In most organizations nobody owns location end to end. Search teams treat it as an index field, product teams as a form field, legal teams as a privacy question, and finance as a line on a provider invoice. At group scale it needs one owner and four explicit decisions.

**Decision 1: one gazetteer and geocoding gateway for the group.** Place IDs are shared language across search, alerts, landing pages, ads targeting, analytics and fraud. If each brand keeps its own, the group cannot aggregate, cannot run cross-border search and pays for several provider contracts. Veldmark's decision record, approved at the architecture advice forum in May 2027, puts a **Veldmark Place** service (gazetteer, geocoding gateway, place resolver and precision policy engine) inside the Common Ground taxonomy and attribute platform, under Yara Mendes's platform engineering organization. It goes live for Tradeyard alongside the taxonomy service in October 2027, with Hearthly and Motorvane following in 2028.

**Decision 2: the precision policy is group policy with brand parameters.** The rule that precise private locations never leave the restricted store is not negotiable per brand. The display levels per category and seller type are brand parameters, owned by brand product leads and reviewed by Lucía Ortega's privacy team. Changes to the policy are versioned and backfilled like any other reference data. Hearthly Spain's exact pins for private landlords are the first thing the policy fixes, in its first release.

**Decision 3: providers are chosen per country and use, behind the gateway.** National open registers where they exist; one commercial provider with storage rights for the rest; a self-hosted open geocoder for bulk work. The gateway's licence register is reviewed when contracts renew and during every acquisition's due diligence. When Veldmark bought Casavista in 2025, nobody asked what its coordinates were licensed for; the next deal team will.

**Decision 4: location quality is a published metric.** The match-level mix, coordinate defects, place drift and precise-point exposure are reported weekly per brand and country, next to the publication-time and duplicate-rate metrics in [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) and [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution). Precise-point exposure has a target of zero and is treated as a privacy incident when it is not.

What to watch over the long term: open address registers improving in more countries, which can retire commercial contracts; the share of shipped transactions, which changes what location means for general goods; regulators' interest in how platforms protect private sellers' locations; and AI search agents that scrape listing pages and analytics endpoints at scale, which make every leaked coordinate easier to harvest ([AI Across the Listing Lifecycle](#ai-in-listing-systems)).

The design is too much for a single-country marketplace where nearly every listing comes from businesses at public addresses: it can live with a precise point and a place hierarchy, and skip the policy engine. The moment private sellers appear, it cannot.

{id: location-and-geo--questions-to-ask}
## Questions to Ask

1. For each brand, what is the most precise location of a private seller that any public payload contains — page, API, structured data, sitemap, feed, analytics, alert e-mail?
2. Are distances shown to buyers computed from the precise point or the public point, and how are they rounded?
3. Is the public point derived deterministically, and does it stay inside the public place?
4. For every stored coordinate, can we name the provider, the data version and the licence terms that allow us to keep and display it?
5. Do listings reference places by stable ID with all ancestors, or by name? What happens to landing pages and filters when a municipality merges?
6. Where does "in [city]" mean the administrative unit and where a marketplace-curated area, and who decides?
7. Which internal consumers read precise locations, for which documented purpose, and is each read logged?
8. Do we store the geocoder's match level and confidence, and do low-precision listings stay out of fine-grained price statistics?
9. Could a buyer search across our country sites near a border today, and if not, is that a product decision or an accident of the data model?
10. What is our weekly figure for coordinate defects, and who looks at it?

{id: location-and-geo--from-place-to-seller}
## From Place to Seller

Location tells the marketplace where a listing is; it does not say who is selling it. That question — private sellers, dealers, agencies with fourteen branches, and the accounts, roles and integrations behind them — is the subject of [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts).

{id: location-and-geo--sources-and-evidence}
## Sources and Evidence

{id: location-and-geo--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Setting expectations with an accurate location](https://airbnb.com/resources/hosting-homes/a/setting-expectations-with-an-accurate-location-491) — Airbnb, 2025. Default approximate-location radius and address release after booking.
- [Embedding-based retrieval at Airbnb](https://arxiv.org/html/2601.06873v1) — Airbnb, 2026. S2 cells as a listing-location feature; the prevalence of map-based filters.
- [H3: Uber's Hexagonal Hierarchical Spatial Index](https://www.uber.com/blog/h3/) — Uber, 2018. Design and rationale of H3.
- [Rightmove property POI search case study](https://traveltime.com/case-study/rightmove-property-poi-search-traveltime) — TravelTime, n.d. (vendor case study). Travel-time search and the fixed-licence pricing choice.

{id: location-and-geo--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Article 4 GDPR — Definitions](https://gdpr-info.eu/art-4-gdpr/) — unofficial reproduction of Regulation (EU) 2016/679, n.d. Location data as an identifier of a natural person.
- [Geocoding API policies](https://developers.google.com/maps/documentation/geocoding/policies) — Google, last updated 2026. Storage restrictions, place-ID exception and display on Google Maps.
- [Geocoding API](https://docs.mapbox.com/api/search/geocoding/) — Mapbox, n.d. Temporary versus permanent geocoding.
- [Nominatim usage policy](https://operations.osmfoundation.org/policies/nominatim/) — OpenStreetMap Foundation, n.d. Rate limit, caching and autocomplete rules for the public instance.
- [Copyright and License](https://www.openstreetmap.org/copyright) — OpenStreetMap, n.d. Open Database License attribution and share-alike terms.
- [Key:admin_level](https://wiki.openstreetmap.org/wiki/Key:admin_level) — OpenStreetMap Wiki, n.d. Administrative levels and their variation by country.
- [Placetypes](https://whosonfirst.org/docs/placetypes/) — Who's On First, n.d. Stable place IDs, placetypes and multiple hierarchies.
- [H3 resolution table](https://h3geo.org/docs/core-library/restable/) — H3 project, n.d. Average cell areas and edge lengths.
- [S2 cell hierarchy](https://s2geometry.io/devguide/s2cell_hierarchy) — S2 Geometry, n.d. Cell levels, Hilbert ordering and region covering.
- [Geo-shape field type](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-shape) — Elastic, n.d. BKD indexing, tessellation cost and coordinate order.
- [Basisregistratie Adressen en Gebouwen (BAG)](https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag) — Kadaster, n.d. Dutch address and building register as open data maintained by municipalities.
- [Base Adresse Nationale](https://www.data.gouv.fr/fr/datasets/base-adresse-nationale/) — data.gouv.fr, updated 2026. French national address base under Licence Ouverte 2.0.
- [OS Open UPRN](https://www.ordnancesurvey.co.uk/products/os-open-uprn) — Ordnance Survey, n.d. Open coordinates for about 40 million addressable locations in Great Britain.
- [GPS tags](https://exiftool.org/TagNames/GPS.html) — ExifTool, n.d. GPS metadata carried in image EXIF.

{id: location-and-geo--research-and-practitioner-sources}
### Research and practitioner sources

- [libpostal](https://github.com/openvenues/libpostal) — OpenVenues, n.d. Statistical address parsing and normalization; reported accuracy and model size.
- [Pelias](https://github.com/pelias/pelias) — Pelias project, n.d. Open-source geocoder on Elasticsearch with open data importers.
- *Productscape domain models for general listings and real-estate marketplaces* — the author's research digest, 2026. Geo reference and property reference data assets; personal-data classification of listings.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
