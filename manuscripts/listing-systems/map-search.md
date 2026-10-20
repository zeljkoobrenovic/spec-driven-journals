{id: map-search}
# 22. Searching by Place: Map, Polygon and Commute Search

![Searching by Place: Map, Polygon and Commute Search — logo](listing-systems-architecture/posts/22-map-search/assets/images/22-map-search/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn the five ways a buyer says "here" (radius, viewport, drawn polygon, named area and travel time), how each becomes an index query, how maps cluster and cache results, and how commute search works, following one Lyon apartment search through Hearthly's draw-your-area feature.

> **WHY THE BUSINESS CARES:** In real estate, and increasingly in automotive and local goods, buyers decide on place before anything else. A map that is slow, cluttered with duplicates or wrong at the edges loses the session to a competitor, and a commute filter priced per request can quietly become one of the largest variable costs in the search budget.

> **WHY ARCHITECTS SHOULD CARE:** Map traffic is chattier, harder to cache and more expensive per request than list traffic, and it brings constraints the list never had: polygon complexity, aggregation that can leak private locations, and routing providers whose licenses shape the design.

> **KEY POINTS:**
>
> * **A map is not a list with pins.** Map sessions send many small viewport queries, show clusters and counts instead of a ranked top ten, and need their own ranking and evaluation. Airbnb reports that maps carry about 80% of its search interactions and that list metrics misjudge them.
> * **Compile every place expression into a few primitives.** Named areas become term filters on place IDs, drawn shapes become simplified polygons, commutes become isochrone polygons or post-retrieval travel times, and viewports become tile-aligned boxes. The geo query compiler, not the client, owns that translation, so caching, privacy and cost rules apply everywhere.
> * **Precision, privacy and routing cost are design inputs, not details.** Every pin and every cluster must be computed from the listing's public point, never from its exact one. One canonical property should show as one pin, not three. And the routing provider's pricing and license decide whether commute search runs per search or per listing.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Duplicate Echo** — On a map, three agencies' listings of one flat become three stacked pins, and the clutter is visible at a glance in a way a ranked list hides.
> * **Ghost Inventory** — Cached map tiles and cluster counts keep showing sold and withdrawn listings long after search has removed them.
> * **The Platform Mandate** — A shared search platform tuned for list-shaped horizontal classifieds, imposed on a map-first property portal, pushes the portal's teams to build a shadow geo stack.

Part IV argues that most discovery queries are filters in disguise, and that the platform should compile a buyer's words, places and saved searches into its own structure. This chapter does that for place. Search usually treats location as one filter among many, a radius around a postcode applied before price and category; for many listing marketplaces that is backwards. A family looking for a flat starts with *where*: near a school, within half an hour of work, on this side of the river. A car buyer starts with *how far I am willing to drive to see it*. A buyer of a used sofa starts with *how far I can carry it*. **Place is often the first filter and the main one**, and in real estate it is also the main way people browse.

This chapter owns **map search** (discovery where the result set is displayed on, and scoped by, a map), **isochrone search** (filtering by travel time rather than distance) and **geo clustering** (grouping many results into fewer map markers). It builds on [Where Is It? Location, Geocoding and Privacy](#location-and-geo), which owns geocoding, location precision and the geo index; that chapter decides *what point a listing has*, and this one decides *how buyers search over those points*. It sits on the engine and index design of [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture), uses the ranking concepts of [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking), and turns the canonical properties of [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) into map pins. The next chapter, [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts), turns saved map searches into alerts.

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), offers the case. Its property portal Hearthly launched a draw-your-area search in France, and by 2027 it has become both the feature agencies praise and the workload the search team fears.

{id: map-search--setting-the-scene-at-veldmark-the-polygon-problem-at-hearthly}
## Setting the Scene at Veldmark: The Polygon Problem at Hearthly

It is late September 2027, two weeks after Veldmark decided on **14 September** to move Tradeyard and Hearthly onto a shared search platform on Amazon OpenSearch Service by the end of 2028 (see [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)). Julien Marchand, Hearthly's CTO, asks Ingrid Halvorsen, Veldmark's Group Chief Architect, and Tomasz Wiśniewski, who heads the group search platform, for a session about one feature before the migration is planned.

Hearthly's search runs on self-managed OpenSearch on Google Kubernetes Engine. In France it serves **1.9 million** live listings, which entity resolution groups into about **1.12 million** distinct properties ([One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)), and **0.7 million** in Spain. Julien's numbers for September 2027, local to this chapter and illustrative, are these:

- **61%** of Hearthly France search sessions open the map view at least once; on mobile, 54%.
- **17%** of sessions use *Dessinez votre zone* ("draw your area"), the draw-your-area search launched in France in 2024.
- At the Sunday-evening peak, Hearthly's search API handles about **4,200 requests per second**, of which about **2,700** are map requests: viewport queries, cluster requests and count updates as users pan and zoom.
- Drawn polygons arrive with a median of **146 vertices** and a maximum of more than **2,000**, because the mobile client sends the raw finger trace.
- p99 latency for polygon queries at peak is **1.8 seconds**; for list queries over the same area defined by city, it is **210 milliseconds**.
- About **1.1 million** of Hearthly's 7 million saved searches contain a drawn polygon.

Two complaints arrive with the numbers. Agencies in Lyon, among them **Agence Rhône Habitat** (fictional, 14 branches), complain that the map shows their listing as one of three stacked pins for the same flat. And product wants commute search, *"30 minutes by public transport to my office"*, for the spring 2028 season, with a routing provider's quote that prices each isochrone request.

Tomasz's worry is that Hearthly's traffic does not fit the shared platform. The shared OpenSearch platform was sized and tuned for Tradeyard, which produces about 70% of group queries and is list-shaped: category, keyword, radius and price, with a ranked page of results. Hearthly is map-shaped. And Hearthly stays on Google Cloud through 2028 while the shared platform runs on AWS, so every pan and zoom could cross clouds.

Ingrid frames three questions for the session. **What query shapes does the map need, and who translates the user's gesture into them? How should results be grouped, cached and ranked on a map? And what does commute search cost, in latency, money and license terms?** The rest of this chapter answers them.

{id: map-search--five-ways-to-say-here}
## Five Ways to Say "Here"

Buyers express place in five ways. Each has a different meaning, a different index primitive and a different cost. Treating them as one "location filter" is the source of most map-search bugs.

| Expression | What the buyer means | Index primitive (Elasticsearch/OpenSearch terms) | Cost and cacheability |
| --- | --- | --- | --- |
| **Radius** | "Within 25 km of Essen" | `geo_distance` filter on a point | Cheap; cacheable if the center is snapped to a grid |
| **Viewport** (bounding box) | "What is in the part of the map I am looking at" | `geo_bounding_box` filter | Cheap per query, but many queries per session; cacheable only if aligned to tiles |
| **Drawn polygon** | "Only this area I traced" | `geo_shape` query with a polygon against a point field | Cost grows with vertex count; rarely cacheable; must be normalized |
| **Named area** | "Lyon 7e", "Eixample", "postcode 3011" | Term filter on a denormalized array of ancestor place IDs | Cheapest and most cacheable; boundaries are reference data |
| **Travel time** (isochrone) | "30 minutes by tram from my office at 08:30" | A `geo_shape` filter on an isochrone polygon, or travel times computed per listing after retrieval | One routing call per search or many per page; the provider's pricing dominates |

A **bounding box** is the rectangle defined by the map's south-west and north-east corners at the current zoom. An **isochrone** is a polygon enclosing every point reachable from an origin within a time budget, for a given mode of transport and departure time. A **place ID** is a stable identifier for an administrative or named area (country, region, city, district, neighborhood). [Where Is It? Location, Geocoding and Privacy](#location-and-geo) recommends storing on each listing the ancestor place IDs, so that "all listings in Lyon 7e" is a term filter, not a polygon query. A **public point** is the coordinate a listing may expose to clients, which for private sellers is deliberately coarser than the true location (also from [Where Is It? Location, Geocoding and Privacy](#location-and-geo)).

Elasticsearch documents these primitives, and OpenSearch uses the same names: `geo_point` stores points and `geo_shape` stores polygons, lines and rectangles. Shapes are tessellated into triangles indexed in a BKD tree, at a precision of about 1e-7 degrees, and **tessellation cost scales with the number of vertices** ([Elastic, geo-shape field type, n.d.](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-shape)). The `geo_shape` query can run against `geo_point` fields with the spatial relations `intersects`, `within`, `disjoint` and `contains`. It can also reference a shape already indexed in another index by its ID, which is how a platform can store named areas or saved polygons once and refer to them by name ([Elastic, geo-shape query, n.d.](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-geo-shape-query)).

Three semantic traps sit inside the table.

1. **Radius and named area disagree at the edges, and users notice.** A flat 300 meters outside the Lyon 7e boundary is in a 2 km radius around the district center but not in "Lyon 7e". Neither answer is wrong; the product must say which one it applies, and saved searches must store which one the user chose.
2. **A viewport is a display scope, not intent.** A user who zooms out to orient themselves has not asked for all of Lyon. Systems that silently turn the last viewport into a filter on the list view, or into a saved search, produce results the user never meant. The rule I use: the viewport filters the map; it filters the list only when the user has chosen "search this area".
3. **A coarse public point makes "within" probabilistic.** If a private seller's bike in Rotterdam is shown at the center of an H3 cell with an edge of about 1.4 km (resolution 7, see [Where Is It? Location, Geocoding and Privacy](#location-and-geo)), a polygon that cuts through that cell includes or excludes the bike based on the cell center, not the bike. For goods that is acceptable. For real estate with exact addresses it is not an issue. For the cases between, such as an agency that hides the street number, the product must decide whether to match on the true point and show the coarse one, which leaks a little information through the result set, or to match on the coarse point and accept edge errors.

{id: map-search--the-map-is-a-different-product}
## The Map Is a Different Product

The strongest public evidence on map search comes from Airbnb, which is not a classifieds site but shares the property: place-first discovery of unique inventory. In a 2024 paper, Airbnb's search team reported that its two result interfaces, a ranked list and price pins on a map, had used the same booking-probability ranking, and that list assumptions did not hold on the map. The team rebuilt the model of user attention for maps ([Haldar et al., *Learning to Rank for Maps at Airbnb*, arXiv, 2024](https://arxiv.org/abs/2407.00091v1)). Airbnb's 2025 review of its research says maps account for "roughly 80% of search interactions" and describes a map-specific NDCG (normalized discounted cumulative gain, the standard list-ranking metric), because list NDCG "fails to model user attention on maps" ([Airbnb Tech, 2025 year in review](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/)). Airbnb's January 2026 paper on embedding-based retrieval adds that nearly all its searches carry filters, "especially map-based geographic filters", and that it uses S2 cells as a location feature ([arXiv 2601.06873, 2026](https://arxiv.org/html/2601.06873v1)).

Property portals have long treated the map as central. Rightmove named "rich, map-centric results" among the three priorities of its 2014 move to Elasticsearch, according to a case study Elastic published in 2025 ([Elastic, 2025](https://www.elastic.co/pdf/elastic-rightmove-partnership-success-story.pdf)); the case study does not detail Rightmove's current map stack. Applying Airbnb's ranking findings to property portals is my inference, not something the portals have published. The mechanics carry over, though, and the table shows how they change the architecture.

| Property | List view | Map view |
| --- | --- | --- |
| **Unit of result** | A ranked page of 20–50 listings | Every match in the viewport, as pins or clusters |
| **Queries per session** | A few, at each filter change | Dozens: every pan, zoom and "search this area" |
| **What must be fast** | The first page | Counts and clusters at every zoom level, plus the pins at the deepest zoom |
| **What ranking means** | Order of the page | Which pins to show when there are too many, which pin to highlight, and the order of the side list |
| **Attention model** | Top positions get most attention, decaying down the page | Attention follows geography and the user's area of interest, not a position |
| **Evaluation** | NDCG, click-through by position | Map-specific metrics; contacts per map session; time to shortlist |

Two consequences follow. First, **the map is a search client in its own right**, with its own latency budget and query mix. Capacity planning that counts "searches" as list queries will underestimate the map's load. Second, **ranking does not disappear on the map; it moves**. When a viewport over central Lyon holds 2,400 matching flats, the system must decide which 300 to show as individual pins and which to fold into clusters, which pins carry a price label, and what the side list shows. Paid placements raise the same questions on the map that [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) discusses for lists: a "featured" pin that is larger or always shown is a paid boost, and ranking transparency obligations apply to it.

{id: map-search--architecture-a-geo-query-compiler-in-front-of-the-engine}
## Architecture: A Geo Query Compiler in Front of the Engine

The design I recommend puts a geo query compiler between the map clients and the engine, and gives each other map concern its own component with a narrow interface. Figure 1 shows them for Hearthly's target state on the shared search platform.

![Diagram: The geo query compiler turns every place expression into a normalized query before any cache or engine sees it](listing-systems-architecture/posts/22-map-search/assets/images/22-map-search/fig01-geo-query-compiler-turns-every-place.jpeg)

**Figure 1:** *The geo query compiler turns every place expression into a normalized query before any cache or engine sees it. Commute requests go through an isochrone service with its own cache, and listing events invalidate cached tiles so the map does not show ghost inventory.*

- **Map search API** (a backend-for-frontend, see [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture)). Receives the gesture (viewport, zoom, drawn shape, chosen areas, commute parameters) and the ordinary filters. Returns pins, clusters, counts and the side list in one response shaped for the map client. It owns debouncing rules and response budgets per zoom level.
- **Geo query compiler.** The center of the design. It normalizes every place expression into one of the engine primitives: it resolves names to place IDs, simplifies and validates polygons, snaps viewports to tiles, asks the isochrone service for commute polygons, and enforces the precision rule (match and display fields, see below). Because every query passes through it, it is also where cost limits, vertex caps and cache keys are defined.
- **Place and boundary service.** Reference data owned by the location capability of [Where Is It? Location, Geocoding and Privacy](#location-and-geo): place IDs, hierarchies, boundary polygons and their versions. Boundaries change (municipal mergers, new postcode areas), so saved searches that reference place IDs must be migrated like taxonomy changes ([Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies)).
- **Isochrone service.** Turns (origin, mode, time budget, departure time) into a polygon, through a routing provider or a self-hosted engine, with a cache in front. It is a separate service because its cost, latency and license terms differ from everything else in the search path.
- **Tile and cluster cache.** Stores aggregated results per map tile and normalized filter set. It is invalidated by listing events (publication, unpublish, price change) from the listing event stream ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)).
- **Search engine.** Executes geo filters together with the ordinary filters and returns hits and grid aggregations. It holds no geo logic the compiler does not control.
- **Neighborhood data service.** Serves points of interest and area facts (schools, transit stops, noise, flood zones, price statistics) as map layers and, selectively, as filters.

The rule that holds the design together: **clients send intent, not engine queries**. A mobile client that sends a raw 2,000-vertex finger trace straight to the engine, or that constructs its own bounding boxes at arbitrary precision, puts the cost and correctness of the map in the hands of every app release. Mobile releases are slow to reach all users (see [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture)), so a client-side mistake can live for a year. The compiler makes the server the owner.

{id: map-search--a-pan-a-zoom-a-count}
### A pan, a zoom, a count

Figure 2 shows the sequence for a single pan on the map, the most frequent interaction.

![Diagram: Snapping the viewport to tiles turns an uncacheable bounding box into a set of reusable cache entries](listing-systems-architecture/posts/22-map-search/assets/images/22-map-search/fig02-snapping-viewport-tiles-turns-uncacheable-bounding.jpeg)

**Figure 2:** *Snapping the viewport to tiles turns an uncacheable bounding box into a set of reusable cache entries. A pan typically reuses most of the previous tiles, so the engine sees only the edge of the movement.*

Three choices in the figure matter.

1. **Debounce in the client, but enforce budgets on the server.** Clients should wait for a gesture to settle before querying. But the server must still rate-limit per session, because a buggy client release can multiply map traffic overnight.
2. **Snap viewports to tiles.** A raw bounding box is almost never repeated exactly, so it cannot be cached. A viewport rounded to the tiles of a fixed grid at the current zoom produces cache keys that many users share. Web-map tiles use the standard `zoom/x/y` scheme; Elasticsearch's `geotile_grid` aggregation buckets points into exactly these tiles, at precisions 0 to 29, and returns only non-empty cells. Its documentation warns that the finest precision is smaller than 10 cm × 10 cm and recommends a bounding-box filter to avoid huge numbers of buckets ([Elastic, geotile grid aggregation, n.d.](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-geotilegrid-aggregation)).
3. **Separate the count from the pins.** The total count in the header ("2,412 homes in this area") and the cluster counts are the expensive part, much as facet counts are for list search ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) discusses Vinted's 2023 experience with facets). Approximate counts above a threshold ("2,000+") and a separate request path for the side list keep the map responsive.

{id: map-search--clustering-three-ways-to-show-ten-thousand-results}
## Clustering: Three Ways to Show Ten Thousand Results

At city zoom levels a map cannot show every match as a pin. **Geo clustering** groups nearby results into a marker with a count, which splits into smaller clusters and finally pins as the user zooms in. There are three places to do it.

| Approach | How it works | When it fits | Main risk |
| --- | --- | --- | --- |
| **Server-side grid aggregation** | The engine buckets matching listings into grid cells (`geotile_grid` for square map tiles; `geohex_grid` for H3 hexagons) and returns counts, optionally with centroids and sub-aggregations such as median price | Large result sets; filters change often; the default for real estate and automotive | Engine CPU at peak; grid-shaped clusters look mechanical unless centroids are used |
| **Client-side clustering** | The server returns all matching public points in the viewport (capped); the client clusters them, for example with Mapbox's open-source Supercluster library, which builds a hierarchy of clusters per zoom level over a k-d tree | Up to tens of thousands of points; smooth zoom without server round trips | Payload size on mobile; the cap silently drops listings; every point sent is data that can be scraped |
| **Pre-rendered vector tiles** | The engine or a tile service returns map tiles with hits and aggregated cells already encoded. Elasticsearch's vector tile search API returns a binary Mapbox vector tile with `hits`, `aggs` (from `geotile` or `geohex` cells) and `meta` layers | Very high read volume with few filter combinations; base layers such as "all homes for sale" | Combinations of filters multiply the tile space; cache invalidation on every listing change |

The sources for the table are documentation, all undated: OpenSearch's `geohex_grid` aggregation groups points into H3 cells identified by their H3 index, at precision 0 to 15 ([OpenSearch, geohex grid, n.d.](https://docs.opensearch.org/latest/aggregations/bucket/geohex-grid/)). Supercluster describes itself as "a very fast geospatial point clustering library for browsers and Node", built to power clustering in Mapbox GL JS ([Mapbox, Supercluster, n.d.](https://github.com/mapbox/supercluster)). Elasticsearch's `_mvt` endpoint returns the tile layers listed above, with `grid_agg` set to `geotile` or `geohex` and up to 10,000 hits per tile ([Elastic, vector tile search API, n.d.](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search-mvt)). A team on OpenSearch that wants vector tiles should check the current OpenSearch documentation before assuming the same endpoint exists; the aggregations underneath are available in both engines.

The approaches combine. A common split is server-side aggregation at city and region zoom, client-side clustering of capped point sets at street zoom, and individual pins when the viewport holds fewer than a few hundred matches. H3 hexagons, introduced by Uber in 2018 ([Uber Engineering, 2018](https://www.uber.com/blog/h3/)), make clusters that look less like a chessboard than square tiles do, because every hexagon has six equidistant neighbors; [Where Is It? Location, Geocoding and Privacy](#location-and-geo) gives the resolution table.

{id: map-search--the-privacy-trap-in-aggregation}
### The privacy trap in aggregation

**Aggregations can leak what pins hide.** If a private seller's exact point is stored next to the public point, and the cluster centroid or the cell is computed from the exact point, a cluster of one at high zoom places a marker at the seller's front door. The same holds for heatmaps, "price per square meter" grids computed at fine resolution, and the `hits` layer of a vector tile.

The rule is absolute: **every geometry returned to a client is computed from the public point field**, and the exact point field is not readable by the map search API at all. [Where Is It? Location, Geocoding and Privacy](#location-and-geo) recommends a deterministic public point per listing, either a snapped cell center or a seeded random offset. Determinism matters again here: if the offset changed with each query, averaging cluster positions over many requests would reveal the true point. For Tradeyard's private sellers the public point is the center of an H3 resolution-7 cell. For Hearthly's agency listings it follows the precision each agency chooses (P3 district, P4 street or P5 exact address), and a property listed by several agencies shows the coarsest of their choices.

![Top, a cluster of one placed on a seller's front door from the exact point; bottom, the same cluster at the centre of a coarse hexagon from the public point.](listing-systems-architecture/posts/22-map-search/assets/images/22-map-search/aggregation-privacy-trap.jpeg)

**Figure 3:** *Aggregations can leak what pins hide: a cluster of one computed from the exact point marks the seller's front door, so every geometry the map returns is computed from the public point.*

{id: map-search--drawn-polygons-normalize-before-you-query}
## Drawn Polygons: Normalize Before You Query

A drawn polygon is the most expressive place query and the most dangerous one. Its cost depends on vertex count, its validity depends on the user's finger, and its meaning depends on rules the user never sees. Large portals offer draw search (Rightmove, Idealista and Zillow among them), but how they implement it is not publicly documented. The natural implementation in Elasticsearch-style engines is a `geo_shape` query with the user's polygon against listing points, and Hearthly uses it.

The geo query compiler should apply six steps to every drawn shape before it reaches the engine.

1. **Validate and repair.** Close the ring; remove repeated points; fix self-intersections, which a finger trace that crosses itself produces, by splitting into valid polygons or taking the outer boundary; reject zero-area shapes. Engines reject or misinterpret invalid polygons, and the error should be the compiler's, with a clear message to the user, not a 500 from the cluster.
2. **Simplify.** Reduce vertices with a tolerance tied to the zoom level at which the shape was drawn, for example with the Douglas–Peucker algorithm. A trace drawn at city zoom does not need meter-level precision; 15–25 meters is invisible on screen and cuts most vertices.
3. **Cap.** Enforce a maximum vertex count after simplification (Hearthly's target is 64) and a maximum area. A polygon covering half of France is a region search and should be compiled as one.
4. **Snap to known areas when the shape is close to one.** If a drawn shape matches a named area within a tolerance, offer the named area. Named-area filters are cheaper, cacheable and stable when boundaries are versioned.
5. **Store it as an object.** A drawn shape that will be reused, in a saved search or a shared link, gets an ID and is stored once, then referenced (the pre-indexed shape mechanism in the `geo_shape` query, or the platform's own shape store). Saved polygons are the input to alerts in [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts), so their normalized form is the one to keep.
6. **Pre-filter coarsely.** Add a bounding-box filter or a set of covering cells (H3 or S2 cells that cover the polygon) before the exact polygon test, so that the expensive geometric test runs on few candidates. Whether the engine already does this internally depends on the engine and version; adding it explicitly is cheap.

For Hearthly, steps 2 and 3 alone change the workload. Julien's team tests the Lyon polygons from September: simplification at 20 meters cuts the median from 146 to 31 vertices and the maximum from over 2,000 to the cap of 64. In a replay of a Sunday-evening hour against a staging cluster, polygon query p99 falls from 1.8 seconds to **240 milliseconds**. These are illustrative figures for Veldmark; the direction is what the Elastic documentation predicts.

![A jittery finger-traced polygon with many vertices simplified by a compiler into a clean polygon with few vertices, with latency dropping from red to green.](listing-systems-architecture/posts/22-map-search/assets/images/22-map-search/polygon-simplification.jpeg)

**Figure 4:** *Normalize before you query: at Hearthly, simplifying drawn shapes at 20 meters cut the median from 146 to 31 vertices, and polygon p99 at peak fell from 1.8 seconds to 240 milliseconds in replay.*

The remaining semantic choice is **`within` versus `intersects` for points**. For point data the two give the same answer except for points exactly on the boundary, which is rare. The real boundary question is the coarse public point discussed earlier, and the right answer is a product decision that should be written down once, in the compiler, and not rediscovered by each client team.

{id: map-search--commute-search-isochrones-and-travel-times}
## Commute Search: Isochrones and Travel Times

Commute search lets buyers filter or sort by travel time to a place that matters to them. For property it matters because the cost of a home is partly the cost of getting to work from it. There are two documented forms in the property sector.

- **Per-listing travel times to the user's places.** Rightmove's *My Places* feature calculates travel times from each property to points of interest the user saves (work, school, family), for walking, cycling, driving and public transport, using the third-party TravelTime API. The places persist in the user's session, so travel times appear on every property they view. According to TravelTime's case study (undated; the page carries a 2026 footer and is vendor marketing), Rightmove chose it partly for a **fixed annual license with unlimited requests**, because computing travel times to every place, for every mode, across millions of daily searches "would simply not be possible in a transactional model" ([TravelTime, Rightmove case study, n.d.](https://traveltime.com/case-study/rightmove-property-poi-search-traveltime)). The case study describes per-listing travel times, not isochrone filtering.
- **Commute as a search criterion.** Zillow added commute time, affordability and nearby points of interest as natural-language search criteria in September 2024, with the example "homes within 30 minutes of downtown Dallas" ([HousingWire, 2024-09-04](https://www.housingwire.com/articles/zillow-artificial-intelligence-search/)). The article gives no technical detail, so how Zillow computes it is not public.

Behind both forms sit two patterns, which a platform will usually need together.

| Pattern | How it works | Cost profile | Accuracy |
| --- | --- | --- | --- |
| **Isochrone filter** | Compute the isochrone polygon for (origin, mode, minutes, departure time) once per search; run it as a `geo_shape` filter like a drawn polygon | One routing call per search; cacheable by quantized origin, mode, budget and time bucket | Approximate at the polygon's edges; the polygon is a simplification of a network |
| **Per-listing travel time** | Retrieve listings normally; compute travel times from the top N results to the user's places with a matrix call; display, sort or filter the page | N × places routing computations per page; grows with traffic | Exact per listing for the chosen departure time |

The isochrone filter is what makes "show me only homes within 30 minutes" possible over the whole inventory; per-listing travel time is what makes each result card honest. A design that uses only the first shows "28 minutes" on a home that the router would say is 33 minutes away; a design that uses only the second cannot filter, only annotate a page.

{id: map-search--routing-providers-are-an-architectural-constraint}
### Routing providers are an architectural constraint

**The commercial model of the routing provider is an architectural input**, as the Rightmove case shows. Three kinds of terms matter.

1. **Pricing unit.** Per request, per element of a matrix, or a fixed license. Per-listing travel time on a pay-per-element contract scales with page views, which in a property portal peak at exactly the moments marketing works hardest.
2. **Limits.** Mapbox's Isochrone API, for example, documents (as of 2026) a maximum of 60 minutes per contour, at most four contours per request, profiles for driving (with and without traffic), walking and cycling, a limit of 300 requests per minute, and a requirement that results be displayed on a Mapbox map ([Mapbox, Isochrone API, n.d.](https://docs.mapbox.com/api/navigation/isochrone/)). The rate limit alone rules it out as an uncached per-search call for a portal at Hearthly's peak, and the display requirement constrains the choice of map renderer.
3. **Storage and display rights.** Whether you may cache results, for how long, and on which maps you may display them. [Where Is It? Location, Geocoding and Privacy](#location-and-geo) shows the same issue for geocoding, where storing results is a priced option at some providers.

The alternative is a self-hosted routing engine. Valhalla, an open-source engine, offers an isochrone service that "computes areas that are reachable within specified time intervals from a location", with costing models for car, bicycle, pedestrian and multimodal travel, up to four contours by default, and polygon output ([Valhalla documentation, n.d.](https://valhalla.github.io/valhalla/api/isochrone/)). Self-hosting moves the cost from license fees to engineering: road and transit data, which for public transport means importing operators' timetables (commonly published in the General Transit Feed Specification, GTFS) and keeping them current, plus capacity for the peaks. For public transport in particular, the departure time changes the answer, so the cache key must include a time bucket and the product must state the assumption ("weekdays, leaving at 08:30").

{id: map-search--caching-isochrones}
### Caching isochrones

Commute requests repeat often, because people commute to the same few places. The isochrone cache key I recommend is:

- the origin snapped to an H3 resolution-9 cell (about 0.1 km², average edge about 200 m; [Where Is It? Location, Geocoding and Privacy](#location-and-geo)), so that two users working in the same building share an entry;
- the mode;
- the time budget, rounded to the options the product offers (15, 20, 30, 45, 60 minutes);
- the departure time bucket (for example weekday morning peak, weekday off-peak, weekend).

Snapping the origin by up to about 200 meters changes the isochrone by a small margin, which is an acceptable trade for a high hit rate; the per-listing travel time on the result card then corrects the displayed number. Cache entries must expire when the transit timetable or road data changes, and isochrones should be stored in simplified form, through the same normalization as drawn polygons.

{id: map-search--neighborhood-data-and-points-of-interest}
## Neighborhood Data and Points of Interest

Neighborhood context (schools, transit stops, shops, parks, noise, flood risk and local price statistics) is the part of map search most often under-designed, because it looks like content rather than data.

Four rules apply.

1. **It is reference data with owners, sources and refresh cycles.** School lists, transit stops and flood zones come from public registries or licensed providers, each with its own update cycle and license. OpenStreetMap data, for instance, is under the Open Database License (ODbL), which requires attribution and has share-alike terms for derivative databases ([Where Is It? Location, Geocoding and Privacy](#location-and-geo) discusses the legal review this needs). The neighborhood data service should record source, license and as-of date for every layer.
2. **Display is cheap; filtering is not.** "Show schools on the map" is a layer the client fetches per tile. "Only homes within 500 meters of a primary school" is a geo query that must be compiled, typically as a union of buffers precomputed per school or as a precomputed per-listing attribute ("distance to nearest primary school") written at enrichment time ([From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment)). Precomputing is usually better: the listing's location rarely changes, and the attribute can be filtered and ranked like any other.
3. **Area statistics must use enough data.** A "median price per m²" for a cell with four sales is noise presented as fact. Aggregate at a resolution where the counts support the number (H3 resolution 8, about 0.74 km² on average, is a common neighborhood-level choice), and suppress cells below a minimum count. For Hearthly, area statistics come from Valuo, Hearthly's automated valuation model, whose prices are learned from France's open transaction data (DVF, *Demandes de valeurs foncières*), never from asking prices ([Models in Production: ML Platforms and Use Cases](#ml-platform)); Hearthly computes its local price medians per H3 resolution-8 cell.
4. **Some neighborhood facts are legally sensitive.** In the United States, fair-housing rules (24 CFR §100.75) prohibit housing advertisements that indicate a preference based on protected characteristics, including through the selection of media or locations ([Cornell LII, 24 CFR §100.75](https://www.law.cornell.edu/cfr/text/24/100.75)). Demographic overlays and "neighborhood character" scores attached to listings are therefore a compliance question for US portals, not a design flourish. Europe has different rules, but the same caution applies to any layer that could be read as steering buyers by who lives in an area; [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) owns the details.

{id: map-search--performance-and-caching-at-the-peak}
## Performance and Caching at the Peak

Map traffic peaks with all search traffic. At Veldmark the group peak is about **31,000 queries per second** on Sunday evenings, 20:00–22:00 CET; that peak is Veldmark's illustration, while the documented public example of a sharp, marketing-driven peak is Rightmove's busiest minute, "8:48 pm on Wednesday, during the final ad break on prime-time TV" ([Google Cloud press release, 2021](https://www.googlecloudpresscorner.com/2021-12-09-Rightmove-Sets-up-Home-With-Google-Cloud); see [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale)). Map requests are about 2,700 of Hearthly's 4,200 peak requests per second, because each session sends many of them.

The levers, in the order I would pull them:

1. **Tile-aligned caching of aggregations** with filter-set hashing. Normalize filters (sorted keys, bucketed price ranges) before hashing, as for facets.
2. **Cheaper shapes**: named areas where the user's intent allows, and normalized polygons everywhere else.
3. **Approximate counts** and separate request paths for counts, clusters and the side list.
4. **Zoom-dependent result limits.** At region zoom, clusters only; at street zoom, a capped set of pins. Never return 10,000 points to a phone.
5. **Degradation modes.** Under overload, serve cached clusters even if slightly stale, disable live counts, and fall back from per-listing travel times to isochrone-only. [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale) owns the general model; the map needs its own entries in it.

Cache invalidation is where map caching meets **Ghost Inventory**. A cluster tile cached for ten minutes shows a sold flat for ten minutes, and a pin that opens a "listing no longer available" page is the most visible kind of staleness. The listing event stream should invalidate tiles: an unpublish or price-change event identifies the tiles containing the listing's public point at each cached zoom level, and those entries are dropped. With tile keys derived from the public point, this is a direct calculation, not a search. A short time-to-live (one to two minutes) as a backstop limits the damage if an event is missed. [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) owns the unpublish propagation SLA; the tile cache is one more consumer that must meet it.

Hearthly's cross-cloud constraint adds one more lever. With the shared search platform on AWS and the Hearthly application on Google Cloud through 2028, Ingrid's recommendation is to run the map search API and the tile cache on the Hearthly side, so that most pans are answered without crossing clouds, and only cache misses go to the engine. The cost of the cross-cloud round trip is then paid only by the edge of each movement.

{id: map-search--worked-example-the-lyon-apartment-on-the-map}
## Worked Example: The Lyon Apartment on the Map

In May 2027, a three-room (T3) **68 m²** flat in Lyon 7e is listed for sale at **€389,000**, energy class (DPE, *diagnostic de performance énergétique*) **D**, by **three agencies**: one listing arrives through each of two real-estate software vendors and one through Keybridge, Veldmark's agency software. One of the agencies is Agence Rhône Habitat. Entity resolution clusters the three listings into one canonical property, and Valuo estimates it at **€372,000–€401,000** (the canonical facts are in [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)).

Ingrid's team uses the flat as its design walk-through: it replays a buyer's May 2027 evening session as it would run in the target design of Figure 1, with commute search included. Sophie (fictional, she/her) works near Lyon Part-Dieu station and wants a T3 under €400,000 within 30 minutes of the office by public transport.

1. **Commute filter.** Sophie enters her office address and "30 minutes, public transport, weekdays at 08:30". The compiler snaps the origin to its H3 resolution-9 cell and asks the isochrone service. The key is already cached; colleagues of hers asked the same question this week. The isochrone, simplified to 58 vertices, covers most of Lyon 3e, 7e and 8e and parts of Villeurbanne.
2. **Map view.** At city zoom the compiler intersects the isochrone with the viewport, snaps to 9 tiles, and asks for H3 grid aggregations with the filters (sale, T3, up to €400,000). Seven tiles are cache hits. The map shows 14 clusters with 412 matching properties. The count is per **canonical property**, not per listing: the engine collapses listings of the same property (the canonical property ID is in the listing document, see [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)), so the three agency listings of the 7e flat count once.
3. **Draw.** Sophie draws around the streets near the Jean-Macé metro stop. Her trace has 181 vertices; the compiler repairs a self-intersection, simplifies it to 27 vertices and intersects it with the isochrone. 63 properties remain.
4. **Pins.** At street zoom the map shows 63 pins. The 7e flat is **one pin**, at the exact address because all three agencies chose to publish it (a clustered property shows the coarsest precision any of its agencies chose). Tapping it shows the three agency offers on one property card, with the price, the DPE class, the Valuo range and a per-listing travel time of **24 minutes**, computed by a matrix call for the pins on screen.
5. **Save.** Sophie saves the search. The saved search stores the normalized polygon by reference, the isochrone parameters (not the polygon, which may change when timetables change) and the filters. From this point, [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) takes over.

The example shows the value of the compiler as one owner: the canonical-property rule, the public-point rule, the polygon normalization and the isochrone cache are each enforced once. And it shows the value of entity resolution on the map: without it, the flat would be three stacked pins, and the agency that complained in September would be right.

![Left, three stacked pins for one flat; right, one canonical pin opening a card with the three agency offers.](listing-systems-architecture/posts/22-map-search/assets/images/22-map-search/three-pins-one-property.jpeg)

**Figure 5:** *Entity resolution on the map: the Lyon 7e flat listed by three agencies is one pin and one property card with three offers, instead of the three stacked pins that Agence Rhône Habitat complained about.*

The commute arithmetic, not a feature comparison, decides the routing choice. If 10% of Hearthly's 2,700 peak map requests per second come from commute sessions, and each needs a new isochrone per parameter change plus a travel-time matrix per page of pins, then even with a 70% isochrone cache hit rate the peak load is in the low hundreds of isochrones and tens of thousands of matrix elements per second. On a per-request price list, that cost rises with every marketing campaign; with a fixed license or a self-hosted engine, it is capacity planning. So for the spring 2028 commute launch Hearthly chooses a fixed-license provider for travel-time matrices and a self-hosted engine for cached isochrones (an illustrative Veldmark decision).

{id: map-search--trade-offs}
## Trade-offs

The main design choices, with when each is right:

| Decision | Option A | Option B | Choose A when | Choose B when |
| --- | --- | --- | --- | --- |
| Where geo logic lives | Clients build engine queries | Server-side geo query compiler | Single web client, small scale, prototype | Several clients, mobile apps, saved searches, any cost or privacy rule |
| Area filtering | Polygons for everything, including named areas | Place-ID term filters for named areas; polygons only for drawn and commute shapes | Boundaries are not available as reference data | Always, once place hierarchies exist ([Where Is It? Location, Geocoding and Privacy](#location-and-geo)) |
| Clustering | Server-side grid aggregation | Client-side clustering of capped point sets | Large result sets, frequent filter changes | Small result sets, smooth zooming, low scraping risk |
| Commute | Isochrone filter | Per-listing travel time | The user needs to filter the whole inventory | The user needs exact times on a page of results; usually you need both |
| Routing | Commercial API, pay per use | Fixed license or self-hosted engine | Low or uncertain volume, fast launch | Volume is high and peaky; display or storage terms constrain the product |
| Map ranking | Reuse the list ranker for pin selection | Map-specific selection and evaluation | Map is a minor surface | Map carries a large share of interactions, as in real estate |
| Map unit | One pin per listing | One pin per canonical property or item | Goods, where duplicates are rare and listings are the items | Real estate, multi-dealer automotive inventory, any vertical with multi-listing |

The table hides one cross-cutting cost: **every geo feature that becomes a saved search becomes an alert workload**. A drawn polygon in a saved search is percolated against every new listing in the area; an isochrone in a saved search must be recomputed when timetables change. Product decisions on map features are therefore also capacity decisions for [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts).

{id: map-search--vertical-differences}
## Vertical Differences

| Dimension | General classifieds (Tradeyard) | Real estate (Hearthly) | Automotive (Motorvane) | Jobs |
| --- | --- | --- | --- | --- |
| Role of place | Pickup distance; local liquidity | **The** primary filter and browse mode | Willingness to travel to a dealer, often 25–200 km | Commute and remote-work options |
| Typical query | Radius around the user or a postcode | Named areas, drawn polygons, commute | Radius from postcode; sometimes "nationwide with delivery" | City or region; commute radius; "remote" as a non-place |
| Point precision | Coarse public point for private sellers | Exact address where the agency allows; hidden street number otherwise | Exact dealer address; coarse for private sellers | Employer office address; sometimes region only |
| Map view | Secondary, mostly for local goods | Primary; often the majority of sessions | Secondary; dealer locations matter more than car positions | Rare |
| Duplicates on the map | Reposts, usually filtered by moderation | Multi-agency listings of one property: a pin per canonical property | The same car advertised by a dealer group across branches | The same job through several recruiters |
| Commute search | Rarely useful | High value | Low; distance to dealer suffices | High value |
| Neighborhood data | Little | Schools, transit, noise, flood, prices; legally sensitive in some markets | Dealer reviews and opening hours | Transit; employer location |

For automotive, the place that matters is the seller's, not the car's, so Motorvane's map is effectively a dealer map, and its main geo query is a radius around the buyer's postcode in German (*Umkreissuche*). Motorvane stays on Elasticsearch until a 2029 review, which is fine: the geo primitives in this chapter exist in both engines. For general classifieds, the strongest geo lever is not the map but **local liquidity**: ranking by distance and recency together, and expanding the radius when local results are thin, so a buyer in a small town does not see an empty page. [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) owns the scoring; the compiler owns the radius expansion policy.

{id: map-search--failure-modes}
## Failure Modes

The mistakes I would look for first in a design review of map search:

1. **Raw client geometry.** Clients send unbounded polygons or arbitrary bounding boxes straight to the engine. Symptoms: p99 driven by a few users' shapes; cache hit rates near zero; incident reports that start with "after the app release".
2. **The viewport becomes a filter by accident.** The last map viewport leaks into the list view or into a saved search, and users get alerts for an area they only zoomed into. The fix is an explicit "search this area" state.
3. **Aggregations over exact points.** Cluster centroids, heatmaps or vector-tile hits computed from the private point field. This is a privacy incident waiting to be discovered by a journalist or a stalker; the fix is that the map path cannot read the exact field.
4. **Stacked pins (The Duplicate Echo).** One property, three listings, three pins. Agencies and buyers both notice, and it undermines trust in every count on the map.
5. **Stale tiles (Ghost Inventory).** Long-lived tile caches without event-based invalidation keep sold listings on the map, and the pin opens a dead page.
6. **Isochrones without stated assumptions.** A transit commute computed for Sunday at noon, shown to a buyer who commutes on weekdays at 08:30. The departure time and mode must be visible and stored with saved searches.
7. **Per-request routing at peak.** A routing contract priced per call, used uncached in the search path, turns a TV campaign into an invoice. The symptom is a monthly bill nobody forecast.
8. **Boundaries as hard-coded polygons.** District polygons copied into the codebase or the index without versions. When the municipality redraws a boundary, saved searches and SEO landing pages silently change meaning.
9. **List metrics for the map.** Evaluating pin selection and map ranking with list NDCG and position-based click models, which Airbnb's published work shows mislead on maps.

{id: map-search--the-chief-architect-s-view}
## The Chief Architect's View

At group level, map search is a test of the principle Veldmark adopted with Common Ground: **share platforms, not products**. The geo primitives, the geo query compiler, the place and boundary service, the isochrone service and the tile cache are platform capabilities: they are the same problems for every brand, and building them four times is waste. The map product itself, with its gestures, layers, pin design and the decision whether the map or the list is the default, belongs to each brand. Hearthly's map-first experience and Tradeyard's radius-first experience should not converge.

The decisions I would put in front of the architecture advice forum:

1. **Own the geo query compiler as part of the search platform.** Tomasz's team owns it; brands configure it (vertex caps, snapping tolerances, precision rules per category). This is the seam that keeps the shared platform from becoming **The Platform Mandate**: Hearthly gets the map-specific behavior it needs as configuration of a shared component, not as a fork.
2. **Write the precision rule as a platform invariant.** Which field may be matched, which may be returned, per brand and seller type, enforced in the compiler and the index mapping. Lucía Ortega, the group's Data Protection Officer, signs it off; changes go through a decision record.
3. **Treat the canonical property as the map unit for real estate.** This makes entity resolution ([One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)) a dependency of map search. Its accuracy becomes visible to every user, so its quality metrics belong on the search platform's dashboard, not only the data team's.
4. **Buy or build routing on a volume forecast, not a feature list.** The commercial model, limits and display terms are decided by Ingrid with Mateus Carvalho (CTO) and finance, with a forecast of peak isochrone and matrix volumes. Re-forecast whenever a brand plans a commute-led campaign.
5. **Budget the map separately in capacity planning.** Count map requests, not searches, and size the tile cache and engine for the Sunday-evening peak of map traffic in the map-heavy brands.
6. **Measure the map as a product.** Contacts and saves per map session, time to shortlist, and the share of sessions that end on the map. Owned by the brands' product teams, reviewed with search.

What to watch over the long term: **conversational and natural-language search will express place in sentences** ("near a good school, 30 minutes from Part-Dieu"), as Zillow's 2024 feature already does. That raises the value of the compiler. An LLM that turns sentences into filters, as [What Did They Mean? Query Understanding and Autocomplete](#query-understanding) recommends, should emit place IDs, normalized polygons and isochrone parameters, the same intermediate form as the map client. A platform with one compiler absorbs the new interface; a platform where each client builds its own geo queries has to rebuild them for it.

{id: map-search--questions-to-ask}
## Questions to Ask

1. Which component translates a user's map gesture into an engine query, and can a client release change the shape or cost of geo queries without a server change?
2. For each brand and seller type, which location field is used for matching and which for display, and can the map path read the exact point at all?
3. Are clusters, heatmaps and area statistics computed from public points, with minimum counts per cell?
4. What are the vertex cap, simplification tolerance and maximum area for drawn polygons, and what happens to a shape that violates them?
5. Is the map unit a listing or a canonical property, and how many duplicate pins does a sample of dense areas show today?
6. How are map tiles and counts invalidated when a listing is sold, removed or repriced, and what is the measured staleness?
7. What does commute search cost per peak hour under the current routing contract, and what are its limits, caching rights and display terms?
8. Do commute results state mode and departure time, and do saved searches store the parameters rather than the polygon?
9. How are map ranking and pin selection evaluated, and are list metrics being used where they do not apply?
10. Which neighborhood layers carry legal or reputational risk in each market, and who approved them?

{id: map-search--from-maps-to-standing-promises}
## From Maps to Standing Promises

The map turns place into a query. The next step is to turn a query into a standing promise: when a buyer saves the polygon around Jean-Macé, Hearthly commits to telling her within minutes when a matching flat appears. That promise, and the reverse search and fan-out machinery behind it, is the subject of [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts).

{id: map-search--sources-and-evidence}
## Sources and Evidence

{id: map-search--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Learning to Rank for Maps at Airbnb](https://arxiv.org/abs/2407.00091v1) — M. Haldar et al., arXiv, 2024. List-ranking assumptions fail on map interfaces; a rebuilt attention model for maps.
- [Airbnb Tech: 2025 year in review of academic publications](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/) — Airbnb, 2025. Maps at about 80% of search interactions; map-specific NDCG.
- [Embedding-based retrieval at Airbnb](https://arxiv.org/html/2601.06873v1) — Airbnb, arXiv, 2026. Map-based geographic filters on nearly all searches; S2 cells as a location feature.
- [Rightmove case study: property POI search](https://traveltime.com/case-study/rightmove-property-poi-search-traveltime) — TravelTime, n.d. (vendor case study). Rightmove's My Places per-listing travel times; fixed annual license with unlimited requests.
- [Rightmove Sets up Home With Google Cloud](https://www.googlecloudpresscorner.com/2021-12-09-Rightmove-Sets-up-Home-With-Google-Cloud) — Google Cloud press release, 2021. Rightmove's busiest minute during a prime-time TV ad break.
- [Zillow AI search adds commute time, affordability](https://www.housingwire.com/articles/zillow-artificial-intelligence-search/) — HousingWire, 2024. Commute, affordability and points of interest as natural-language criteria.
- [H3: Uber's Hexagonal Hierarchical Spatial Index](https://www.uber.com/blog/h3/) — Uber Engineering, 2018. The H3 grid used for hexagonal clustering and cell keys.

{id: map-search--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Geo-shape field type](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-shape) — Elastic, n.d. Tessellation, precision, cost growing with vertex count.
- [Geo-shape query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-geo-shape-query) — Elastic, n.d. Polygon queries against points; spatial relations; pre-indexed shapes.
- [Geotile grid aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-geotilegrid-aggregation) — Elastic, n.d. Tile-based clustering and the bounding-box advice.
- [Vector tile search API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search-mvt) — Elastic, n.d. Hits, aggregation and metadata layers in Mapbox vector tiles.
- [Geohex grid aggregation](https://docs.opensearch.org/latest/aggregations/bucket/geohex-grid/) — OpenSearch, n.d. H3-cell aggregation at precision 0–15.
- [Isochrone API](https://docs.mapbox.com/api/navigation/isochrone/) — Mapbox, n.d. Contour, profile, rate and display limits of a commercial isochrone API.
- [Isochrone and isodistance service](https://valhalla.github.io/valhalla/api/isochrone/) — Valhalla project, n.d. Open-source isochrones with multimodal costing.
- [Supercluster](https://github.com/mapbox/supercluster) — Mapbox, n.d. Client-side hierarchical point clustering.
- [24 CFR §100.75: Discriminatory advertisements, statements and notices](https://www.law.cornell.edu/cfr/text/24/100.75) — US Code of Federal Regulations via Cornell LII, n.d. Fair-housing limits on housing advertisements.

{id: map-search--research-and-practitioner-sources}
### Research and practitioner sources

- [Elastic and Rightmove partnership success story](https://www.elastic.co/pdf/elastic-rightmove-partnership-success-story.pdf) — Elastic, 2025 (vendor material). "Rich, map-centric results" among the priorities of Rightmove's 2014 move to Elasticsearch.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
