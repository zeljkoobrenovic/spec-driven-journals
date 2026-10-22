{id: destinations-and-maps}
# 17. Where Exactly? Destinations, Geo and Map Search

![Where Exactly? Destinations, Geo and Map Search — logo](stays-marketplace-architecture/posts/17-destinations-and-maps/assets/images/17-destinations-and-maps/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Build the geographic layer of stays discovery: the destination graph, place resolution and disambiguation, search areas, spatial indexing with geohash, S2 and H3, viewport search with dates, ranking on the map, distance and location scores, approximate location for homes, map tiles and their cost, and place names in many languages.

> **WHY THE BUSINESS CARES:** Location is the first thing a guest decides and the one thing a property or home cannot change. If "Lisbon" returns the wrong part of the city, or the map shows homes the guest cannot book, the session is lost before ranking or price can win it. Map and geocoding bills also grow with every session and are easy to miss in the search budget.

> **WHY ARCHITECTS SHOULD CARE:** Place data is used well beyond search. Landing pages, pricing features, tourist taxes, short-term-rental rules and disaster response all read it. Without one owned place model, each team keeps its own copy of "Lisbon", and the copies disagree in front of guests, tax authorities and regulators.

> **KEY POINTS:**
>
> * **A destination is not a boundary.** What a guest types resolves to a place in a destination graph, but the area worth searching comes from where guests who search for that place actually book. Keep the two apart: the place has an official polygon and a legal meaning; the search area is a set of cells that can be tuned and learned.
> * **The map is a separate result surface, not a list drawn on a map.** A viewport query carries dates and a party, so pins must show bookable stays at total prices. Guests do not read pins in order, so ranking on the map means choosing which stays get a pin and how many. Caching works only for the date-free geography, not for availability.
> * **A home's location is personal data until the booking.** Hosted-stays maps need a public point that is stable, coarse and derived once from the exact address. Every pin, cluster and distance must come from that public point. Tax, regulatory reporting and the guest's confirmation need the exact address, behind separate access.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Phantom Availability** — Map pins and cluster counts computed without the guest's dates show stays that cannot be booked, at prices that will not hold.
> * **The Hotel-Shaped Home** — One location model for both marketplaces either puts a pin on a host's front door or hides a hotel's exact address behind a vague circle.
> * **City-by-City Firefighting** — Tax and short-term-rental jurisdictions are kept as text fields and hand-made lists rather than versioned boundaries, so every new city rule starts with a manual hunt for the affected listings.

Every stays search starts with a place. The guest types "Lisbon", "near the Sagrada Família" or "Algarve", or drags a map across the coast, and the marketplace has to turn that into a set of properties and homes before dates, prices or ranking matter. **Geography is the primary filter in stays search**, and unlike most filters it is fuzzy: few guests know where a city's boundary runs, and many do not want to stay inside it.

[Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture) built the search pipeline but took the resolved place on trust. This chapter supplies that first stage, deciding *where* to search, and the map as a result surface. It defines the **destination graph**, **viewport search** and **approximate location**. What it produces feeds [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) (the candidates and the map surface) and [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays) and [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) (each unit's jurisdiction). LISTED's [Searching by Place: Map, Polygon and Commute Search](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/map-search.html) covers general map mechanics; this chapter adds what changes when every query has dates, every pin carries a price that depends on them, and half the inventory sits in somebody's home.

{id: destinations-and-maps--setting-the-scene-at-corvane-lisbon-means-four-things}
## Setting the Scene at Corvane: "Lisbon" Means Four Things

Corvane, the fictional travel group this book follows ([Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), has its headquarters in Lisbon. In March 2027 its own city exposed the problem.

Noor van Dijk's regulatory team was preparing the One Stay tax engine and the short-term-rental reporting pipeline. They asked which Nookaway listings are inside the Municipality of Lisbon, the area where the municipal tourist tax applies and a registration rule would cover. Nobody could answer quickly; the search turned up four different "Lisbons" in Corvane's systems (all figures in this chapter are illustrative, like everything about Corvane):

| Where | What "Lisbon" meant | How it was built | Problem |
| --- | --- | --- | --- |
| Roomstead place table (Keystone) | The municipality polygon, about 100 km², from a geodata vendor | Licensed boundary data, loaded in 2015 | A second entity, "Lisboa", had been created by a supplier content import in 2019; **312** properties were attached only to it and never appeared in "Lisbon" searches |
| Roomstead "Lisbon area" | A multi-city entry covering the metropolitan area | Hand-made in 2017 for a paid-search campaign | Included towns 40 km away; nobody owned it |
| Nookaway search (Burrow) | A rectangle drawn by hand in 2014 | Bounding box stored as four numbers in a settings file; stretched west in 2019 to reach the Cascais coast | Stretching it to Cascais also pulled in Almada, Seixal and Barreiro across the Tagus estuary |
| Nookaway listings | A city field the host typed | Free text at listing creation | "Lisbon", "Lisboa", "Lisbon, Portugal", "Lx" and 41 other spellings |

![A simplified map of Lisbon with four overlapping outlines: a municipality polygon, a large metro area, a stretched rectangle crossing the river, and a sticky note of free-text city spellings.](stays-marketplace-architecture/posts/17-destinations-and-maps/assets/images/17-destinations-and-maps/17-four-lisbons.jpeg)

**Figure 1:** *In March 2027 "Lisbon" meant four things in Corvane's systems: a municipality polygon, a hand-made metro area, a rectangle stretched across the river and a free-text city field. None was the area guests actually book.*

The rectangle had a measurable cost. Jonas Weber, Corvane's Head of Search and Ranking, pulled a month of Nookaway "Lisbon" searches. **31%** of first-page results were south of the river, but those areas got **6%** of the bookings from Lisbon searches. Cascais, the reason the rectangle had been stretched, got 9%. Roomstead had the reverse problem: its municipality polygon was legally precise but too narrow for guests who wanted a beach hotel 25 minutes from the center.

The map added a cost problem. Roomstead and Nookaway used a commercial maps platform under separate contracts; their combined 2026 bill was about **€2.4 million**, and nobody had checked whether it grew with bookings or just with page loads.

Mariana Costa, the Group Chief Architect, put three questions to the architecture forum. **Should Corvane have one place model for both marketplaces, and who owns it? How should a typed place become a search area? And what may a map show about a home before it is booked?**

{id: destinations-and-maps--places-destinations-and-the-destination-graph}
## Places, Destinations and the Destination Graph

Blurring these six terms causes most of the bugs.

- A **place** is a named geographic entity with a stable identifier: a country, a municipality, a neighborhood, an airport, a landmark. It has a geometry (a polygon or a point), names in many languages, and relationships to other places.
- A **destination** is a place that guests search for and that the marketplace sells. All destinations are places; not all places are destinations. The parish where a hotel's tax is levied is a place; "Lisbon" is both a place and a destination.
- The **destination graph** is the versioned dataset of places, their geometries, names and relationships. Search, landing pages, pricing, tax and regulation all read it. The generic Productscape reference model behind this book calls it a "Destination Context Graph"; it is the core of this chapter.
- **Place resolution** turns a guest's input (a typed string, an autocomplete pick or a deep link) into a place identifier, and resolves ambiguity on the way.
- A **search area** is the geographic region the marketplace actually searches for a resolved place. It is often different from the place's official boundary.
- **Viewport search** is a query whose geographic constraint is the rectangle of map the guest is looking at, with the guest's dates, party size and filters attached.

{id: destinations-and-maps--what-the-graph-contains}
### What the graph contains

Expedia Group documents its destination graph for partners, the best public reference for the shape. Its Rapid Geography API describes "over 600,000 regions and airports" with types from `continent` and `country` through `high_level_region` (tourist regions), `multi_city_vicinity` (metropolitan areas), `city` and `neighborhood`, down to `airport` and `point_of_interest`. Regions carry a GeoJSON `bounding_polygon`; point types have none. **"A region may have more than one parent"**, so the hierarchy is a graph, not a tree. When a polygon "does not contain at least 100 properties", an expanded mapping adds properties within 30 km ([Expedia Group Developer Hub, About the Geography API](https://developers.expediagroup.com/rapid/lodging/geography/about-geography-api), n.d., fetched October 2026). These are documented features of a partner API; how Expedia maintains the data internally is not public.

Three of these choices apply to any stays marketplace: places can have several parents, point places need a radius, and a thin place is widened by a separate, labeled mapping, not by quietly redrawing its boundary.

| Node type | Geometry | Typical sources | Used by |
| --- | --- | --- | --- |
| Country, region, municipality | Official polygon | National statistics offices, licensed boundary data, OpenStreetMap | Tax and regulation jurisdiction, landing pages, market reporting |
| Metropolitan area, tourist region | Curated polygon or set of cells | Editorial team, booking data | Search areas, landing pages, paid-search campaigns |
| Neighborhood | Polygon, often unofficial | Editorial, local knowledge, OpenStreetMap | Filters, location descriptions, ranking features |
| Airport, station | Point plus a service radius | IATA (International Air Transport Association) codes, transport operators | "Near airport" searches, travel-time features |
| Landmark, venue, beach | Point, sometimes a small polygon | Editorial, OpenStreetMap, events data | Point-of-interest searches, distance labels |
| Jurisdiction zone | Official polygon, effective-dated | Laws and municipal registers | Tourist tax, short-term-rental rules, reporting |

A useful minimum set of edges is: **contains** (official, from geometry), **part of** (curated, for tourist regions that cross administrative lines), **served by** (airport to the places it serves), **alias of** (names and duplicates that point to one canonical place) and **supersedes** (when a municipality merges or a boundary changes, with an effective date).

![A destination graph: Portugal contains the Lisbon Metro Area, which contains Lisbon and Cascais; Lisbon contains Alfama; Lisboa is an alias of Lisbon; Lisbon airport serves the metro area; Lisbon Coast is part of both Cascais and Lisbon.](stays-marketplace-architecture/posts/17-destinations-and-maps/assets/images/17-destinations-and-maps/17-lisbon-destination-graph.jpeg)

**Figure 2:** *A slice of a destination graph around Lisbon. Solid edges are official containment from geometry; dashed edges are curated relationships. "Lisboa" is an alias, not a second place, and the airport is a point with a service relationship, not a polygon.*

{id: destinations-and-maps--why-one-graph-owned-by-one-team}
### Why one graph, owned by one team

Place data looks like reference data, so it gets copied into the search index, the landing-page generator, the feature store and the tax engine, and each copy drifts. Roomstead's "Lisboa" duplicate is **The Same Hotel Twice** at the level of places.

The rule I use: **one destination graph, published as versioned snapshots and change events, with one owning team**. Consumers keep read-optimized copies but never create places. The owner is usually the search or discovery platform team, because search is the heaviest user and has the best signal on what guests mean. The regulatory team owns *what the rules are* ([Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation), [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)), but the jurisdiction polygons live in the same graph, so a listing's tax jurisdiction and its search destination come from the same geometry.

{id: destinations-and-maps--resolving-what-the-guest-typed}
## Resolving What the Guest Typed

Place resolution is a small, latency-critical service that runs on every autocomplete keystroke and once more on submit.

{id: destinations-and-maps--the-hard-cases}
### The hard cases

| Input | Why it is hard | Resolution approach |
| --- | --- | --- |
| "Paris" | Paris, France and Paris, Texas | Popularity priors per market and locale; show the country in autocomplete; never auto-pick when two candidates are close |
| "Lisboa" in a German session | Endonym used in a foreign locale | Aliases in every language map to one place ID |
| "Algarve", "Amalfi Coast", "Lake Como" | No single official boundary | Curated polygon or cell set, marked as curated, with an owner |
| "near Lisbon airport" | A point, not an area | Radius or travel-time area; show distance on results |
| "Sagrada Família" | A landmark inside a city | Point place; search area = radius; ranking uses distance to the point |
| "Porto" | City, district and wine (and Porto Santo, an island) | Type-aware ranking of candidates; show type labels ("City", "Island") |
| "beach house Portugal" | Place plus intent | Hand the non-place part to query understanding ([What Did They Mean? Query Understanding and Autocomplete](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/query-understanding.html)) |
| A pasted Google Maps link or coordinates | No name at all | Reverse-resolve to the smallest containing destination; search a radius |

Resolution returns a structured result, not a polygon. Corvane's contract:

| Field | Meaning |
| --- | --- |
| `place_id` | The canonical place from the destination graph |
| `place_type` | City, neighborhood, point of interest, and so on |
| `display_name` | Localized name for the guest's locale, with disambiguating parent ("Paris, France") |
| `search_area_id` | The search area to use, with its version |
| `anchor_point` | The point used for distance labels and map centering (a city center, a landmark) |
| `confidence` and `alternatives` | When confidence is low, the client shows "Did you mean…" instead of guessing |

Two practices keep resolution honest. **Log the resolution with every search**: a "Porto" search that books in Vila Nova de Gaia is a signal about the search area; one immediately retyped as "Porto Santo" is a resolution failure. And **keep the autocomplete index separate from the property index**: it ranks places and hotel names, needs prefix matching in every script and per-locale popularity, and changes with the graph, not with availability.

{id: destinations-and-maps--where-guests-actually-stay-search-areas-not-boundaries}
## Where Guests Actually Stay: Search Areas, Not Boundaries

A city's official polygon is often the wrong area to search. Guests who search for a city often book in a neighboring town; guests who search for a national park book in the towns outside it; guests who search for a coastline want the coast, not the inland half of every municipality that touches it.

{id: destinations-and-maps--the-documented-case-airbnb-s-location-retrieval}
### The documented case: Airbnb's location retrieval

Airbnb has published more on this problem than anyone else, in a sequence of papers. Dates matter, because each paper describes a system the next one replaced.

- In 2024, Airbnb described building machine-learning location retrieval that identifies "a topological map area that is relevant to the searched query" ([Davis et al., Transforming Location Retrieval at Airbnb, 2024](https://arxiv.org/abs/2408.13399)).
- A 2026 paper describes the system that followed. The earlier one predicted **one rectangular retrieval area** per search. A rectangle is contiguous, so stretching it to reach a popular but distant place (Playa del Carmen, from a Cancun search) also pulled in the unbooked area in between. For "San Francisco" searches, 39.8% of candidates and 14.7% of shown results came from locations not previously booked for that search ([Davis et al., High Precision Audience Expansion via Extreme Classification in a Two-Sided Marketplace, 2026](https://arxiv.org/html/2602.14358v1)).
- The replacement divides the world into **S2 level-11 cells**, 25,165,824 of them (about 20 km² each on average), keeps a vocabulary of about 360,000 cells that contain booked listings, and trains extreme-classification models that output a probability per cell for a query. Cells above a tuned threshold become the search area. Each listing in the Lucene-based index stores its level-11 cell ID, and the selected cells become one OR query. Level 11 was the finest level the production search could handle at scale. Offline, recall of booked locations was unchanged (−0.04%) and precision rose 11.01%. In an online test with about 66 million users, uncancelled bookers rose 0.17% (same source, 2026).

The architectural lesson is mine, not Airbnb's: **a set of cells is a better retrieval contract than a polygon or a rectangle**. A cell set can be non-contiguous (the city plus the beach town, without the industrial zone between them). It turns geography into index terms that any inverted-index engine filters on like keywords, and caches well per place. And it can start curated and become learned without changing the contract.

{id: destinations-and-maps--spatial-indexing-primitives}
### Spatial indexing primitives

| Primitive | What it is | Strength | Weakness | Use in stays |
| --- | --- | --- | --- | --- |
| **Bounding box or radius** | Rectangle or circle in latitude and longitude | Simple; native in every engine | Contiguous; poor fit to real places | Viewport queries; "within 2 km of" |
| **Polygon** | Exact boundary | Legally precise | Expensive to test; one shape per query | Jurisdictions, landing-page membership |
| **Geohash** | Base-32 string from interleaved latitude and longitude bits; a prefix is a coarser cell | Cheap prefix filters and cache keys | Rectangular cells distort with latitude; neighbors can share no prefix | Cache keys; legacy indexes |
| **S2 cells** | Hierarchical cells on a sphere; a region coverer approximates any shape as a set of cells at mixed levels | Exact parent–child containment; good coverings of irregular areas | Cells are squarish, which shows if used for display | Retrieval terms; search areas |
| **H3 cells** | Hierarchical hexagons | Equidistant neighbors; good for aggregation and smoothing | Children only approximately fill their parent | Demand heatmaps, pricing and ranking features, map clusters |

S2 approximates "arbitrary regions as collections of discrete S2 cells" ([S2 Geometry](http://s2geometry.io/), n.d.); H3 "partitions the world into hexagonal cells", with logical containment exact and geometric containment approximate ([H3 documentation](https://h3geo.org/docs/), n.d.), and an average hexagon of about 0.74 km² at resolution 8 ([H3, cell statistics](https://h3geo.org/docs/core-library/restable/), n.d.).

My recommendation for a group: **use one grid for retrieval and one for analytics, and write the choice down**. S2 suits retrieval because its coverings nest exactly, so a search area at mixed levels is a clean union of index terms. H3 suits features and aggregation because hexagons smooth well. A third grid "because the new team prefers it" leaves a group unable to join its pricing features to its search logs.

{id: destinations-and-maps--curated-first-learned-later}
### Curated first, learned later

Airbnb's approach needs many bookings per destination to train, and most of Corvane's destinations have far fewer. A staged approach suits most marketplaces:

1. **Official boundary as default.** Search area = the place's polygon, covered by cells.
2. **Curated overrides** for the top destinations by search volume: add the beach town, drop the port. An editor owns each override, and each records a reason and a review date.
3. **Booking-derived expansion.** For each place, count where guests who searched it booked over the last year, at cell level; add cells above a threshold share of bookings. This is a query, not a model, and it already captures most of the Cancun–Playa del Carmen effect.
4. **Learned cell selection**, once a destination has enough bookings to train and evaluate a model per query, with the curated set as the fallback.

Every stage outputs a versioned set of cells per place, so search never knows which stage made it.

{id: destinations-and-maps--architecture-geo-services-in-the-discovery-stack}
## Architecture: Geo Services in the Discovery Stack

The geographic layer has five components.

![The destination graph feeds the place resolver at query time and geo enrichment at write time; enrichment writes cells and public points to the search index and jurisdictions to tax and regulation, and stays search returns list and pins.](stays-marketplace-architecture/posts/17-destinations-and-maps/assets/images/17-destinations-and-maps/17-geo-layer-of-discovery.jpeg)

**Figure 3:** *The geographic layer of discovery. The destination graph feeds both query-time resolution and index-time enrichment, so a guest's "Lisbon" and a listing's "in Lisbon" are calculated from the same geometry. Enrichment also gives tax and regulation each unit's jurisdiction.*

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Destination graph** | Places, geometries, names, relationships, search areas, jurisdiction zones; versioned | Place IDs and their lifecycle | Store property or listing data |
| **Place resolver** | Autocomplete and resolution of input to place and search area | Resolution logs, locale priors | Return raw polygons to clients |
| **Geo enrichment** | For each property or listing: geocode and validate the address, compute the exact point, the public point, cell IDs at the chosen levels, containing place IDs and jurisdictions | The computed location fields on each unit's place-registry record | Let hosts or partners write cell IDs or place IDs directly |
| **Viewport search API** | Normalize map gestures into queries; snap to tiles; select pins | Map query contract, pin selection | Compute availability itself |
| **Map rendering** | Tiles, styles, attribution, client libraries | Map vendor contracts and tile hosting | Receive exact home locations |

**Enrichment runs at write time, not query time.** When a host saves an address or a partner feed sends new coordinates, geo enrichment computes what search and compliance need (neighborhood, municipality, tax zone, cells, distance to the nearest metro) and writes it to the unit's record in the group place registry ([Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model)). The index stores place IDs as keyword terms, so "in Lisbon" is a term filter, not a polygon test. When the graph changes (a corrected boundary, a new short-term-rental zone), it publishes a change event and enrichment recomputes the units in the cells the changed geometry covers.

That recomputation makes regulation manageable. The EU Short-Term Rental Regulation ([Regulation (EU) 2024/1028](http://publications.europa.eu/resource/celex/32024R1028), applying from 20 May 2026) requires platforms to collect registration numbers for units in areas where a Member State runs a registration procedure, and to report activity data monthly per unit with its "specific address". With versioned jurisdiction polygons and write-time enrichment, a new registration area becomes a recomputation job that lists every affected unit. Without them, a city rule starts a manual hunt: **City-by-City Firefighting**. [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) owns the rules engine; this layer makes "which units are in this zone?" a quick, exact query.

Corvane's architecture forum approved this split in June 2027 as part of One Stay, a month after it created the group place registry for property and unit identities. The destination graph and place resolver become one group service, **Waypoint**, owned by Jonas Weber's group search team, with a first release in the first quarter of 2028. The supply domain keeps the place registry (what a unit is and where exactly it stands); Waypoint owns the geography it is resolved against. Roomstead keeps Elasticsearch and Nookaway keeps OpenSearch, but both index the same place IDs and S2 cell IDs computed by one enrichment service.

{id: destinations-and-maps--viewport-search-with-dates}
## Viewport Search with Dates

A map query is not a destination query with a picture. Every drag and zoom produces a new query: *this rectangle, these dates, this party, these filters*. Three things follow.

**First, the dates make every pin a priced offer.** A pin that says "€145" must mean €145 for a stay the guest can book on those dates, or better, the total for the stay. A pin computed without the dates or from yesterday's cache is **Phantom Availability** at its most visible: the guest taps a price, and the property page shows another or "no availability". The availability join is the one [Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture) describes, but a map session sends many more queries than a list session, each covering a different set of candidates.

**Second, caching has to split along the date line.** LISTED's [Searching by Place: Map, Polygon and Commute Search](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/map-search.html) shows how snapping viewports to map tiles turns unrepeatable rectangles into shared cache keys. For stays, cache only what does not depend on the dates: for each tile and set of static filters (property type, bedrooms, amenities), the candidate IDs and their public points. Then compute availability and total price for the candidates in the viewport on every request: a few hundred to a few thousand per viewport, the scale the availability layer is built for.

![A swimlane of one viewport query: the viewport API snaps to tiles, gets candidates and public points from the tile cache, checks the exact stay and total prices per request, asks the pin ranker to choose pins, and returns pins with totals to the guest app.](stays-marketplace-architecture/posts/17-destinations-and-maps/assets/images/17-destinations-and-maps/17-viewport-query.jpeg)

**Figure 4:** *One viewport query. The tile cache holds only date-free geography; availability and total price are computed per request for the candidates in view, so a pin never shows a price the guest cannot book on those dates.*

**Third, the cache must be invalidated by supply events, not only by time.** Delisting and contract-end events should invalidate the tiles containing the unit's public point, with a short time-to-live as a backstop, or the map sends guests to dead pages.

On 26 November 2027 Roomstead's availability lookups peaked at 96,000 per second and Pricegrid's cache hit rate fell from 94% to 71% ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)). Map sessions add lookups faster than list sessions, because each pan sends new candidates, so Roomstead's degradation mode includes a map rule: above a threshold zoom, show pins without prices and ask the guest to zoom in.

{id: destinations-and-maps--ranking-on-the-map}
## Ranking on the Map

Ranking a map is a different problem from ranking a list. In 2024 Airbnb reported that list and map had used the same ranking, ordering listings by booking probability, and argued that the assumptions behind list ranking do not hold for maps ([Haldar et al., Learning to Rank for Maps at Airbnb, 2024](https://arxiv.org/abs/2407.00091)). In a list, attention falls with position, which is the assumption behind NDCG (normalized discounted cumulative gain, the standard ranking metric). On the map, randomizing the order of the top pins on mobile made no difference to bookings, so the paper models attention as **uniform across pins**. If each pin gets an equal share of attention, then showing fewer, better pins can raise expected bookings. The paper's changes and their reported results:

| Change | What it did | Reported result |
| --- | --- | --- |
| Bookability filter | Show a pin only if its booking probability exceeds the top listing's probability divided by e^α (α = 1.0 in production) | Offline: about 39% fewer pins, 47% higher average booking probability than a fixed 18-pin baseline; online: +1.9% uncancelled bookings |
| Tiered pins (desktop) | Mini-pins with roughly one-eighth the attention of regular pins | +0.7% uncancelled bookings |
| Viewport choice | For search-box queries, choose the initial map center to maximize expected bookings | +0.39% uncancelled bookings for new guests |
| Map-move queries | Distance from the viewport center as a ranking feature | +0.27% uncancelled bookings |

Airbnb's Help Center tells guests that "the listings that appear on the map may differ from those that appear in the list" ([Airbnb, How search results work](https://www.airbnb.com/help/article/39), n.d., fetched October 2026). I found no comparable map-ranking work from an online travel agency (OTA), so whether hotel maps behave the same way is an open question.

Three design consequences follow for any marketplace:

- **Pin selection is a ranking decision.** Which stays get a pin, and how many, is a policy owned by ranking, not a client-side cap. [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) owns the objectives and the governance; the viewport API calls the ranker with a "map" surface flag.
- **The initial viewport is a ranking decision too.** Where the map opens for "Lisbon" decides what the guest sees first, so it should come from the search area and booking data, not from the center of the official polygon.
- **Paid visibility on the map needs the same disclosure as in the list.** A pin promoted because of a partner program is ranking under EU consumer law, which defines ranking by "relative prominence … irrespective of the technological means" ([Directive (EU) 2019/2161](http://publications.europa.eu/resource/celex/32019L2161), 2019). A bigger pin is prominence.

{id: destinations-and-maps--distance-travel-time-and-location-scores}
## Distance, Travel Time and Location Scores

Location enters ranking and display as three kinds of numbers; mixing them confuses guests.

**Distance to an anchor.** "1.2 km from the center" needs a defined center: the resolved place's `anchor_point` (a curated point such as Lisbon's Praça do Comércio), not the polygon's centroid, which may fall in the river. Straight-line distance must be labeled as such: across the Tagus, Almada is 2 km from central Lisbon in a straight line but much farther by road or ferry.

**Travel time.** Walking or transit time to an anchor is more useful than distance and much more expensive ([Searching by Place: Map, Polygon and Commute Search](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/map-search.html) covers routing). Precompute it at enrichment time from each unit to a few anchors per destination (center, main station, airport), because properties do not move; reserve per-query routing for a guest-entered address.

**Location scores.** A location score rates a location from data (density of restaurants, transit, attractions) or from guest reviews. Expedia's 2013 public ranking dataset already included two property location scores ([Liu et al., 2013](https://ar5iv.arxiv.org/html/1311.7679); thirteen years old, and silent on Expedia's current systems). Two rules I apply:

- **Say what a score means.** A review-based location rating reflects guests' expectations ("great for nightlife"), so a quiet residential street can score low with guests who wanted bars. A data-based score reflects the density of what the platform counts. Label which one is shown.
- **Compute scores per cell, not per unit, when they come from the surroundings.** An H3 resolution-8 cell (about 0.74 km² on average) is a common neighborhood-level resolution. Per-cell scores are stable, cheap and, for homes, do not reveal more than the public point does.

{id: destinations-and-maps--approximate-location-for-homes}
## Approximate Location for Homes

A hotel's address is public; a home's address is the host's. Hosted-stays marketplaces commonly show an approximate area (a circle or a neighborhood) before booking and the exact address after confirmation. The reasons are safety (an empty home with its calendar on the internet), privacy (the host often lives there) and disintermediation (an exact address makes it easier to contact the host and book off-platform). No platform documents its method; what follows is the design I recommend.

**Approximate location** is the location shown before booking: a **public point** derived from the exact point, plus a display radius. Everything a guest or a scraper sees before booking comes from the public point: pins, clusters, distance labels, the circle on the property page.

| Method | How it works | Weakness |
| --- | --- | --- |
| Random offset per request | Move the exact point by a fresh random amount on every request | Averaging many requests recovers the exact point. **Never do this.** |
| Stable random offset | Generate one random offset (for example 150–350 m in a random direction) when the address is set; store it; regenerate only when the address changes | The circle may cross a river or sit in the sea; needs a land and plausibility check |
| Snap to a cell | Public point = center of the containing cell at a fixed resolution | All homes in a cell share a point, so pins stack; looks mechanical |
| Neighborhood only | Show the neighborhood polygon, no point | Too coarse for map browsing in large neighborhoods |

The stable offset is the usual best choice, with two safeguards. The offset is **generated once and stored**, never computed from a seed a client could guess. And the public point must fall on land, inside the same neighborhood as the exact point, so the circle does not suggest the wrong side of a river.

Three leaks are common even with a good public point:

- **Aggregations computed from the exact point.** A cluster of one, a heatmap or a per-cell count from exact points puts a marker on the front door ([Searching by Place: Map, Polygon and Commute Search](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/map-search.html)). Rule: **the hosted-stays search index holds only the public point**; the exact point stays in the place registry.
- **Distances computed from the exact point.** "350 m to the beach", computed exactly and shown alongside the circle, narrows the circle to an arc. Compute guest-facing distances from the public point and round them.
- **Content.** A photo of the street sign or a title naming the building defeats the circle; that is a content and trust problem ([Describing a Stay: Content, Media and Property Mapping](#content-and-media)).

**When does the exact address appear?** At confirmation for instant book, after acceptance for request-to-book. Corvane adds one rule: the exact address goes into the confirmation and the trip view ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging)), never to the search stack's map client.

**The platform still needs the exact address** for tax jurisdiction, short-term-rental registration and reporting (the "specific address" above), damage claims and emergency response. So geo enrichment computes jurisdictions from the exact point and writes them to the place registry. The exact address sits behind access controls ([Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access)) that search, ranking and analytics do not have.

![A public circle with a public point feeding pins, clusters and distances, separated by a wall from a locked vault holding the exact address, which feeds only tax and reporting and the booking confirmation.](stays-marketplace-architecture/posts/17-destinations-and-maps/assets/images/17-destinations-and-maps/17-public-point-and-exact-address.jpeg)

**Figure 5:** *A home has two locations: a stored public point that every pin, cluster and distance uses, and an exact address behind access controls that only tax, reporting and the booking confirmation may read.*

For hotels an exact pin is part of the product, and a circle looks like an error. One display rule for both marketplaces is **The Hotel-Shaped Home** in miniature, so the place-registry record carries a `display_precision` field (exact or approximate) set by unit type, not by brand; Roomstead's 435,000 apartments and holiday homes include both private homes and serviced apartments with a reception.

At Corvane, the review of Nookaway's map found that Burrow's old web map recomputed a random offset on every request, while the newer Go map service used a stored offset, so anyone who compared enough web-map responses could narrow down an address. The fix shipped in July 2027: one stored public point per listing, computed by geo enrichment, used by every client. The old field was removed from the API.

{id: destinations-and-maps--map-tiles-geocoding-and-what-they-cost}
## Map Tiles, Geocoding and What They Cost

The map itself is usually bought. Base-map tiles, geocoding (address to coordinates), reverse geocoding and place autocomplete come from a commercial platform or from self-hosted open data, and the choice sets both cost and what the marketplace may store.

As of October 2026, Google Maps Platform lists Dynamic Maps at $7.00 per 1,000 loads and Geocoding at $5.00 per 1,000 requests in its first paid tier, after a monthly free allowance ([Google Maps Platform pricing](https://developers.google.com/maps/billing-and-pricing/pricing), last updated 20 October 2026). Licenses also constrain storage: Google's Places policies say "You must not pre-fetch, cache, or store Places API content beyond the allowed exceptions", while the place ID is exempt and may be stored "indefinitely" ([Google, Places API policies](https://developers.google.com/maps/documentation/places/web-service/policies), last updated 20 October 2026).

That storage rule is an architectural reason to own the destination graph: on a vendor's places API, the marketplace cannot keep places, names or geometry as its own data, or build search areas and jurisdiction polygons on them. Use vendor autocomplete for *addresses*; own the *destinations* you sell.

The open-data route has its own terms. The OpenStreetMap Foundation's public tile servers are "best-effort" with "no SLA or guarantee" and prohibit bulk downloading ([OSMF Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/), n.d.), so a marketplace should host its own OpenStreetMap tiles. Single-file formats such as PMTiles, read with HTTP range requests ([Protomaps, PMTiles](https://docs.protomaps.com/pmtiles/), n.d.), and renderers such as MapLibre GL JS ([MapLibre](https://maplibre.org/), n.d.) make that a build pipeline and a CDN.

| Option | Cost profile | What you own | Main risk |
| --- | --- | --- | --- |
| Commercial platform for everything | Per load and per request; grows with sessions, not bookings | Little: place IDs, your own overlays | Bills that follow traffic spikes and bots; storage limits on place content |
| Commercial tiles, own destination graph | Per-load tiles; resolution in-house | Places, names, search areas | Two systems to keep consistent at the edges (addresses vs places) |
| Self-hosted open-data tiles, own graph, commercial geocoding for addresses only | Fixed hosting and engineering; small per-request geocoding | Almost everything | Map quality and style are your problem; data update pipeline |

Corvane's 2026 map bill of about €2.4 million came mostly from per-load charges, many of them from bots and from property pages that rendered a map nobody scrolled to. The decision in Waypoint's plan: an own destination graph and resolver for both brands in 2028; lazy-loaded maps on property pages immediately (a client change); and a pilot of self-hosted vector tiles for Nookaway's map browse in 2028. Commercial geocoding stays for address entry during onboarding ([From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding)), where accuracy matters more than cost.

{id: destinations-and-maps--place-names-in-many-languages}
## Place Names in Many Languages

Roomstead runs in 41 languages. Place names are not a translation problem but a data problem, and they belong in the destination graph.

- **Endonyms and exonyms.** Lisboa, Lisbon, Lissabon, Lisbonne and リスボン are one place. Each name is an attribute of the place, tagged with language and with a flag for the preferred display name per locale. Search indexes every name as an alias; display uses the preferred one for the guest's locale.
- **Informal names.** Transliterations and nicknames ("Lx" for Lisbon) come from search logs; an editor approves them as aliases.
- **Names change and places merge.** Reforms and renamings are `supersedes` edges with effective dates, so old URLs and tax rules still resolve.
- **Disputed names and borders.** Legal and regulatory affairs decide per locale, not a developer in a translation file.

Host-entered location text is the opposite: free text for describing the neighborhood is content ([Describing a Stay: Content, Media and Property Mapping](#content-and-media)), but the city, region and country of a listing must be derived from its geocoded point and the graph, never typed. Nookaway's 45 spellings of "Lisbon" disappeared when Waypoint enrichment started writing the listing's place IDs and the city field became read-only.

{id: destinations-and-maps--destination-pages-and-the-place-hierarchy}
## Destination Pages and the Place Hierarchy

Destination landing pages ("Apartments in Alfama") are pre-built search results. My recommendation, for which I found no primary source: **one hierarchy drives search and pages**. The graph's places and parent edges define landing pages, breadcrumbs and URLs; a page exists only where the place has enough bookable inventory and redirects to its parent otherwise ([Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture) owns landing assembly, [Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels) the SEO side).

{id: destinations-and-maps--worked-example-the-novaks-search-lisbon}
## Worked Example: The Novaks Search "Lisbon"

On 11 February 2027, Jana Novak searched Nookaway for Lisbon, 2–9 August, two adults and two children ([Meet Corvane: Two Marketplaces, One Group](#meet-corvane)). Here is that search in the target architecture Corvane designed in mid-2027, planned for Nookaway by late 2028.

1. **Resolution.** Jana types "Lisa" in the Nookaway app, set to Czech; autocomplete offers "Lisabon, Portugalsko" first (the Czech exonym, with the parent country), ahead of two smaller places. She picks it. The resolver returns the place ID for the Municipality of Lisbon, `place_type = city`, and the search area *Lisbon – stays*, version 14.
2. **Search area.** Version 14 is booking-derived (stage 3): the S2 cells covering the municipality, plus cells along the Cascais coast and in Sintra that held more than 2% of bookings from "Lisbon" searches over the previous year. Almada and Seixal fall below the threshold and are left out. The area covers the **16,800** active Nookaway listings in the municipality and about **2,400** outside it.
3. **Retrieval and availability.** Of those **19,200** listings, about **2,600** sleep four, allow children, have every night from 2 to 9 August open and break no minimum-stay or check-in rule; the quote engine prices the top 600 and returns 571 stay totals ([Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture) traces this stage).
4. **The map.** The app opens the map on the viewport the ranker chose for this search area, centered on the historic center rather than the polygon's centroid, and shows **14** pins. The pin ranker chose them by bookability, not as the top 14 rows of the list. Each pin shows the total for seven nights. The family's eventual choice, the Alfama apartment at **€145** a night, appears as a circle on its property page, centered on its stored public point about 250 m from the building.
5. **Abandonment and return.** The Novaks leave without booking. The saved search stores the place ID and search-area version, not a rectangle, so the price alert ([Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations)) re-runs the same geographic query.
6. **Booking.** On 14 February they book the Alfama apartment: 7 × €145 = €1,015, plus €70 cleaning, a 12% guest service fee of €130.20 and €56 of Lisbon tourist tax, for €1,271.20. The confirmation carries the exact address.
7. **Tax and reporting.** The tourist tax line was computed from the listing's jurisdiction, which geo enrichment derived from the **exact** point: inside the Municipality of Lisbon. A listing whose public circle overlapped the boundary but whose exact point lay in Oeiras would have used Oeiras's rules. [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays) owns the tax.

Under the old rectangle, the same search held about **3,100** listings south of the river and the map opened on the estuary; under Roomstead's old place table, a hotel attached only to "Lisboa" would not have appeared at all.

{id: destinations-and-maps--trade-offs}
## Trade-offs

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| Search area | Official polygon | Curated or learned cell set | Small destinations; regulatory and tax uses; landing-page membership | Large destinations where guests book outside the boundary; anywhere with booking data |
| Retrieval primitive | Polygon or bounding box at query time | Precomputed cell IDs and place IDs as index terms | Low volume; few destinations; prototypes | Any production stays search; anything that must be cached |
| Place data | Vendor places API | Own destination graph, vendor for addresses | Very early stage; one market | Several markets, landing pages, tax and regulation needs |
| Map tiles | Commercial platform | Self-hosted vector tiles | Small teams; quality-sensitive map styles | High map volume; cost predictability; control of what is drawn |
| Home location display | Approximate area with stored public point | Exact pin | Private homes and rooms | Hotels, serviced apartments with reception, aparthotels |
| Map pin set | Top N of the list ranking | Separate pin selection by bookability | Very small result sets | Any map with more candidates than pins |
| Ownership | Each brand keeps its own place data | One group destination graph | Brands in unrelated geographies with no shared reporting | Overlapping geographies; shared tax, regulation and data platforms |

{id: destinations-and-maps--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (Roomstead) | Hosted-stays marketplace (Nookaway) |
| --- | --- | --- |
| **Where location comes from** | Partner content feeds and connectivity partners; supplier coordinates that disagree across sources | Host enters an address at listing creation; geocoded once and verified |
| **Location precision shown** | Exact; the pin is part of the product | Approximate until booking; stored public point |
| **What guests choose by** | Brand, star rating, district name, distance to a landmark | The home itself and its surroundings; location within a city is a main differentiator |
| **Map importance** | Supporting view; list dominates | Primary browsing mode for many guests (documented for Airbnb, 2024) |
| **Search area problem** | Narrow boundaries miss resort and airport hotels | Wide areas pull in unbookable or unwanted districts; homes spread farther from centers |
| **Duplicates** | Same property from several suppliers at different coordinates ([Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model)) | Same home on several platforms; less a geo problem than a calendar one ([One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync)) |
| **Regulation by place** | Hotels outside the EU Short-Term Rental Regulation; tourist tax by jurisdiction | Registration areas, night caps and zone bans by address; tourist tax by jurisdiction |
| **Failure mode** | Wrong or missing properties in a destination; hotels pinned in the wrong place | Address leaks; listings in banned zones; host-typed city names |
| **What can be shared** | Destination graph, resolver, enrichment, tile hosting, place names | The same, plus the approximate-location service |

**Judgement.** This is one of the clearest cases in the book for sharing. Places are facts about the world, while ranking is a marketplace-specific judgement: Lisbon's boundary, its name in Czech and the location of its airport are the same for both brands. Share the destination graph, the resolver, write-time enrichment and the map tile stack. Keep separate what reflects each marketplace's guests: search areas (Roomstead's guests and Nookaway's guests book in different places for the same query, so each brand gets its own area version per place), and map pin selection and ranking. Because `display_precision` follows the unit, not the brand, Nookaway's boutique-hotel pilot in 2028 gets exact pins without a new system.

{id: destinations-and-maps--failure-modes}
## Failure Modes

- **Text instead of place IDs** — properties vanish from searches with no error, as Nookaway's 45 spellings of "Lisbon" did; see Place Names in Many Languages.
- **Duplicate places** — a hotel attached only to Roomstead's "Lisboa" never appears; see Places, Destinations and the Destination Graph.
- **The boundary as the search area** — resort towns go missing or unbooked districts fill the page; see Where Guests Actually Stay.
- **Date-free pins and list ranking reused for pins** — Phantom Availability and undisclosed paid prominence; see Viewport Search with Dates and Ranking on the Map.
- **Aggregations or distances from the exact point** — a home's address leaks before booking; see Approximate Location for Homes.
- **Unversioned jurisdictions and unmetered maps** — the wrong tax rule and a bill that follows bots; see Architecture and Map Tiles, Geocoding and What They Cost.

{id: destinations-and-maps--the-chief-architect-s-view}
## The Chief Architect's View

The geographic layer is small in code and large in reach. My agenda:

**Write down the ownership mandate.** One team owns the destination graph, the resolver and enrichment, and other teams may not create places. At Corvane that is Jonas Weber's group search team, with Noor van Dijk's regulatory team owning the *content* of jurisdiction zones and an editorial function owning curated search areas and names. Without the mandate, the second "Lisbon" appears within a year.

**Make the place contract boring and stable.** Place IDs never change meaning and are never reused; places are superseded, not edited, when boundaries change; every snapshot is versioned; every booking records the place IDs and the jurisdiction version that applied. That last rule lets regulatory affairs answer "which rule applied to this stay in March?" without archaeology.

**Separate exact and public locations in the schema, not in the UI.** Treat it as a data-classification decision ([Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety) and [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) cover the controls); a schema enforces it more reliably than code review.

**Measure the geography.** Three metrics: the share of bookings inside the searched place's search area (low means too narrow), the share of shown results in cells that rarely get bookings for that query (high means too wide; Airbnb's 14.7% for San Francisco under the old rectangle is a reference), and immediate re-searches with a different place.

**Put the map bill on someone's desk, and watch for the next consumer.** Map spend belongs in the search platform's cost per booking; Corvane's €2.4 million bill had no owner. The consumer most groups forget is disaster response: when a wildfire, flood or strike closes an area, customer service needs "every active and upcoming stay inside this polygon" within minutes. A place layer that answers jurisdiction queries quickly can answer that one too ([Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability)).

{id: destinations-and-maps--questions-to-ask}
## Questions to Ask

1. How many entities in our systems mean "Lisbon" (or our biggest destination), and which properties are attached to each?
2. Is a property's or listing's city derived from its coordinates and a destination graph, or typed by a person?
3. For our top ten destinations, what share of bookings from that destination's searches lands outside its search area, and what share of first-page results sits in cells that almost never get bookings?
4. Do our map pins and cluster counts use the guest's dates, and does a pin price equal the price on the property page for those dates?
5. Are map pins chosen by a ranking decision, or are they the top N rows of the list?
6. Where is the exact location of a home stored, which services can read it, and can any guest-facing number (pin, cluster, distance) be computed from it?
7. Are tax and short-term-rental jurisdictions computed from the exact point against versioned polygons, and can we list every unit inside a new zone within an hour?
8. Do our vendor contracts allow us to store the places we sell, and what does the map cost per booking?
9. Who approves a new place, alias or search-area change, and where is that change logged?

{id: destinations-and-maps--from-places-to-order}
## From Places to Order

The geographic layer decides which stays are candidates and where they appear on a map. It does not decide which ones come first. The next chapter, [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking), orders the candidates for guests, partners and the marketplace: learning to rank, commission and programs, and the transparency that EU law requires for both the list and the map.

{id: destinations-and-maps--sources-and-evidence}
## Sources and Evidence

{id: destinations-and-maps--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Transforming Location Retrieval at Airbnb](https://arxiv.org/abs/2408.13399), Davis et al., Airbnb (CIKM), 2024 — location retrieval as its own machine-learning problem upstream of ranking.
- [High Precision Audience Expansion via Extreme Classification in a Two-Sided Marketplace](https://arxiv.org/html/2602.14358v1), Davis et al., Airbnb, 2026 — rectangle retrieval's flaws, the 39.8% and 14.7% figures, S2 level-11 cell selection and its offline and online results.
- [Learning to Rank for Maps at Airbnb](https://arxiv.org/abs/2407.00091), Haldar et al., Airbnb (KDD), 2024 — uniform map attention, the bookability filter, tiered pins, viewport choice and their reported results.
- [Academic Publications: Airbnb Tech 2025 Year in Review](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/), Airbnb Tech, 2026 — the 2025 maps ranking follow-up with a map-specific NDCG.
- [How search results work](https://www.airbnb.com/help/article/39), Airbnb Help Center, n.d. (fetched October 2026) — map listings may differ from list listings.
- [About the Geography API](https://developers.expediagroup.com/rapid/lodging/geography/about-geography-api) and [Geography reference lists](https://developers.expediagroup.com/rapid/lodging/geography/geography-reference-lists), Expedia Group Developer Hub, n.d. (fetched October 2026) — region types, polygons, multiple parents, property mapping and the 30 km expansion.
- [Combination of Diverse Ranking Models for Personalized Expedia Hotel Searches](https://ar5iv.arxiv.org/html/1311.7679), Liu et al., 2013 — location scores among the features of Expedia's 2013 public ranking dataset (historical only).

{id: destinations-and-maps--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2024/1028 on short-term rental data](http://publications.europa.eu/resource/celex/32024R1028), European Union, 2024 — registration areas, monthly reporting with the unit's specific address, application from 20 May 2026.
- [Directive (EU) 2019/2161 (Omnibus Directive)](http://publications.europa.eu/resource/celex/32019L2161), European Union, 2019 — the definition of ranking as relative prominence, which covers map pins.
- [S2 Geometry](http://s2geometry.io/), Google, n.d. — spherical hierarchical cells and region coverings.
- [H3 documentation](https://h3geo.org/docs/) and [Tables of cell statistics across resolutions](https://h3geo.org/docs/core-library/restable/), H3 project, n.d. — hexagonal grid, containment, average cell areas.
- [Google Maps Platform pricing](https://developers.google.com/maps/billing-and-pricing/pricing), Google, 2026 (last updated 20 October 2026) — first-tier prices and free caps for maps, tiles, autocomplete and geocoding.
- [Places API policies](https://developers.google.com/maps/documentation/places/web-service/policies), Google, 2026 (last updated 20 October 2026) — storage restrictions on places content; place IDs exempt.
- [Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/), OpenStreetMap Foundation, n.d. — best-effort service, no SLA, prefetching prohibited.
- [PMTiles](https://docs.protomaps.com/pmtiles/), Protomaps, n.d. — single-file tile archives served with HTTP range requests.
- [MapLibre](https://maplibre.org/), MapLibre project, n.d. — open-source vector map rendering.

{id: destinations-and-maps--research-and-practitioner-sources}
### Research and practitioner sources

- [Searching by Place: Map, Polygon and Commute Search](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/map-search.html), LISTED, 2026 — tile-aligned caching, clustering, drawn polygons, isochrones and the aggregation privacy trap, which this chapter builds on.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
