{id: entity-resolution}
# 15. One Property, Three Listings: Duplicates and Entity Resolution

![One Property, Three Listings: Duplicates and Entity Resolution — logo](listing-systems-architecture/posts/15-entity-resolution/assets/images/15-entity-resolution/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn the five kinds of duplicate listing, the real-world identities that listings can be resolved to, and the pipeline that turns candidate pairs into stable clusters and canonical entities. You will also see how merge policies decide what buyers, sellers and downstream systems see, using the Lyon apartment that three agencies listed on Hearthly.

> **WHY THE BUSINESS CARES:** Duplicates make a marketplace look bigger than it is and work worse than it should. Buyers scroll past the same flat three times, agencies argue about whose card was shown, alerts fire twice, and the inventory numbers used to sell subscriptions overstate the real supply by about 70%.

> **WHY ARCHITECTS SHOULD CARE:** Entity resolution creates an identifier that search, alerts, valuation, analytics, fraud detection and pro reporting will all depend on. If that identifier is unstable, lives only in the search index, or is produced by a model nobody evaluates, every one of those systems inherits the error.

> **KEY POINTS:**
>
> * **"Duplicate" names two problems with opposite answers.** Reposts, freshness gaming and stolen listings are abuse, and the action is enforcement. Several agencies listing the same flat, or one dealer feeding the same car through two channels, is legitimate, and the action is clustering for presentation. One detector can serve both, but the policies, owners and appeals must stay separate.
> * **Resolve listings to an entity that outlives them.** A property or a vehicle has an identity that persists across listings, agencies and years. Model it as its own record with a stable identifier, owned by a named domain, and keep the listing as an offer that refers to it. Goods mostly have no such identity, so do not invent one.
> * **The cluster identifier is a product contract, not a model output.** Blocking, pairwise scoring and clustering produce candidate links. A governed process turns them into stable cluster IDs with merge and split lineage, measured precision and recall, a correction path for sellers, and a policy for which listing represents the cluster. That policy must never be for sale silently.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Duplicate Echo** — reposts, multi-feed copies and multi-agency listings crowd result pages and alerts, and nobody owns the decision of what to show once.
> * **The Unwatched Model** — a pairwise matcher merges and hides listings without labeled evaluation, drift monitoring or an owner who can explain a wrong merge to an agency.
> * **Ghost Inventory** — a cluster keeps a property "on the market" after its last live listing has gone, because the cluster's state was never tied to the lifecycle of its members.

Part III follows supply from the seller to the result page. [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) left every listing with a canonical address, a decoded VIN where one exists, and image hashes, so listings can now be compared, and the comparison shows that many of them describe the same thing. This chapter's online checks run inside [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline), and search, alerts and valuation read the cluster identifiers it creates.

The duplicates come in several kinds. A private seller reposts a bike every two days because new listings rank higher. A dealer's management system and a listing aggregator both send the same car. Three agencies hold mandates on one flat and each publishes it. A fraudster copies a real rental listing, photos and all, and prices it 35% lower. On a result page each looks the same: one thing appears more than once. **They are different problems, and treating them as one is the most common mistake in this area.**

This chapter covers two capabilities. **Duplicate detection** finds listings that are copies or near-copies of each other. **Entity resolution** (ER), sometimes called record linkage, decides which listings refer to the same real-world thing and gives that thing an identity. A **canonical entity** is the resulting record: one property, one vehicle, sometimes one product, with a stable identifier and attributes reconciled from its listings. In real estate, the canonical entity is the **canonical property**. This chapter owns all three terms.

Neighboring chapters own adjacent parts. [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) owns the feeds that bring the copies in. [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) owns the address, VIN and attribute normalization that matching depends on. [Photos Sell: Media Pipelines for Listings](#media-pipeline) owns perceptual hashing as an image capability. [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) owns what happens once a duplicate turns out to be a scam. This chapter owns the matching, the clusters, the canonical entity and the policies that decide what each side of the market sees.

{id: entity-resolution--setting-the-scene-at-veldmark-the-lyon-apartment-three-times}
## Setting the Scene at Veldmark: The Lyon Apartment, Three Times

In May 2027, Hearthly France receives three listings for a three-room (T3) **68 m²** flat in Lyon's 7th arrondissement, energy class (DPE, the French energy performance diagnostic) **D**. Hearthly is the real-estate portal of Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). **Agence Rhône Habitat**, a network of **14 branches**, publishes it through Keybridge, the group's agent CRM. Two other agencies hold mandates too, and their transaction software sends the flat through two different real-estate software vendors. Rhône Habitat lists it at **€389,000**. The other agencies list it at €389,000 and €395,000, because French sale prices are usually shown fees included, and the agencies charge different fees.

Before 2027, a buyer searching "T3 Lyon 7e under €400,000" saw three cards with three photo sets, two prices and three agency names. A buyer who saved that search received three alerts. Hearthly's market report counted three listings. The price history behind Valuo, Hearthly's valuation product, showed three properties for one sale. Agencies complained twice: first that "their" flat was shown below a competitor's copy, and then that a competitor's lower-fee copy undercut them on the same page.

The flat is not unusual. Across Hearthly France, **1.9 million** live listings describe about **1.12 million** distinct properties, an average of **1.7** listings per property. Claire Fontaine, Hearthly's CEO, puts the problem to Ingrid Halvorsen, Veldmark's Group Chief Architect, in two sentences: "Buyers think we have more flats than we do, and agencies think we pick favorites. Fix the first without making the second worse."

Julien Marchand, Hearthly's CTO, has a nightly deduplication job that already groups some listings by exact address. Ingrid asks four questions about it. *What is the thing being duplicated? Who decides that two listings are the same, and how often is that decision wrong? What does each audience see once they are grouped? And who can dispute a grouping?* The rest of this chapter answers those questions.

{id: entity-resolution--five-kinds-of-duplicate}
## Five Kinds of Duplicate

The word "duplicate" covers five situations that differ in who creates them, why, and what the marketplace should do.

| Kind | Typical example | Who creates it, and why | Typical signals | Right action | Owning context |
| --- | --- | --- | --- | --- | --- |
| **Same-seller repost** | The same bike posted three times in a week | A seller wanting more exposure, or one who forgot the first listing | Same account or device, near-identical text and photos, same category and area | Block the new one, or replace the old one and keep its history | Trust and safety; listing policy |
| **Relisting to game freshness** | A listing deleted and recreated every few days to reach the top of a recency sort | A seller substituting a free repost for a paid bump | Same as above, plus a delete-and-recreate pattern in time | Enforce: keep the original creation date, limit reposts, offer a paid bump instead | Trust and safety with monetization |
| **Cross-feed duplicate** | One dealer's car arriving through its DMS (dealer management system) feed and an aggregator feed | An integration configuration: two channels for one seller | Same organization, same VIN or partner reference, different channel IDs | Merge silently at ingestion: one listing, two sources | Supply and ingestion |
| **Multi-agency listing** | The Lyon flat, listed by three agencies | Legitimate: several professionals hold mandates on one property | Same address or parcel, matching surface and rooms, different organizations, overlapping photos | Cluster for presentation: show the property once, list every agency | Listing and discovery |
| **Stolen or cloned listing** | A rental in Barcelona copied from a real listing, priced far below market | Fraud | Different seller, matching photos (perceptual hash), price anomaly, new account | Enforce: hold or remove, investigate the account network | Trust and safety ([Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)) |

Two more cases look like duplicates but are not. **The same entity with a different offer**, such as one flat listed both for sale and for rent, or a car listed again by a new owner two years later, is a new listing on the same entity. Price history and valuation need the link, but search should not hide either listing. **Similar but distinct entities**, such as two identical flats on different floors of a new building or two white 2021 Golfs at one dealer, are the main source of wrong merges.

The chapter's first rule follows: **detection can be shared; decisions cannot.** The same blocking and similarity machinery finds a same-seller repost, a multi-agency cluster and a stolen copy. What separates them is the relationship between the sellers and the evidence of intent. The design note in Veldmark's research puts it plainly: *same seller, same photos* is spam or ranking abuse; *different seller, same photos* is a fraud signal or a legitimate multi-agency listing, and seller, device and organization keys are what tell them apart. The OLX duplicate pipeline described publicly in 2019, discussed below, used exactly those keys to generate candidates.

![One shared similarity detector feeds a junction that checks seller keys; abusive duplicates go to enforcement, while legitimate multi-agency listings are clustered into one property card.](listing-systems-architecture/posts/15-entity-resolution/assets/images/15-entity-resolution/shared-detection-separate-decisions.jpeg)

**Figure 1:** *The same detection machinery finds reposts, stolen copies and multi-agency listings; the relationship between the sellers decides whether the result is enforcement or presentation.*

The two families of action also sit under different legal regimes. Removing or demoting a listing because it is an abusive duplicate is a content-moderation restriction. Under the EU Digital Services Act (DSA), the affected seller is owed a statement of reasons, and demotion counts as a restriction (Art. 17; see [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)). Grouping three agencies' listings under one property card is a presentation choice. It has no DSA consequences, but the rules for choosing the card a buyer sees first are a ranking parameter, and those rules have transparency obligations (see [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking)). An architecture that runs both through one "dedup" flag cannot meet either set of obligations.

{id: entity-resolution--what-is-the-thing-real-world-identity-by-vertical}
## What Is the Thing? Real-World Identity by Vertical

Entity resolution needs an answer to a prior question: *same what?* The answer differs by vertical, and it decides how far resolution can go.

| Vertical | Real-world entity | Identifiers available | How reliable | What ER can achieve |
| --- | --- | --- | --- | --- |
| Real estate | Property (dwelling unit), inside a building, on a parcel | National address bases, building registries, cadastral parcels; in Great Britain the Unique Property Reference Number (UPRN); in the US county assessor parcel numbers | Good for the building, weak for the unit inside it; listings often omit or blur the address | A durable **canonical property** with price and listing history |
| Automotive | Vehicle | The 17-character vehicle identification number (VIN), plus registration plates in some countries | Strong when present; dealers often send it, private sellers often do not | Exact merging of cross-feed duplicates; vehicle history across owners |
| General goods (used, unique) | The physical item | None | No identifier; the listing *is* the item | Near-duplicate detection only, mostly for abuse |
| Catalog goods (new, recommerce) | The product model, not the item | Global Trade Item Number (GTIN) or EAN barcodes, manufacturer part numbers | Good for products; says nothing about the individual item | Product matching for attributes and price comparison, not deduplication |
| Jobs | The vacancy | Employer reference numbers, sometimes | Weak; the same vacancy is reposted by agencies and job boards | Clustering of reposted vacancies |

Real estate is where the entity matters most, because **the property outlives every listing of it**. The same flat is listed for sale, sold, let, relisted by a different agency, and valued off-market. Public reference data exists, but each country's is different. In Great Britain, Ordnance Survey's open UPRN product publishes coordinates for about 40 million "addressable locations", each with "a unique numeric identifier for every addressable location in Great Britain" ([Ordnance Survey, n.d.](https://www.ordnancesurvey.co.uk/products/os-open-uprn)). France has the Base Adresse Nationale, an open national address base updated twice a week ([adresse.data.gouv.fr, n.d.](https://adresse.data.gouv.fr/)), and the Référentiel National des Bâtiments (RNB), which gives each building "un identifiant unique et pérenne", the ID-RNB, designed as a pivot for linking building data between administrations and private parties ([RNB, n.d.](https://rnb.beta.gouv.fr/)). In the US, county assessor parcel numbers vary by county, and data aggregators sell normalized parcel IDs. None of these identifies a **unit inside a building**. In a Lyon apartment block, the address and the ID-RNB narrow the candidates to one building; floor, surface, room count and photos must do the rest.

Zillow is the documented example at scale of a property-first model. Its annual report for fiscal 2025 describes a "living database" of about 173 million US homes, with user-generated updates to more than 46 million property records, which powers its Zestimate valuation and its indices ([Zillow Group 10-K, filed 2026-02-11](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)). The filing describes the database, not how listings are matched to it, and the internal matching method is not public.

Vehicles are easier when the VIN is there. A VIN identifies one vehicle across feeds, dealers and owners, so two listings with the same VIN at the same time are a cross-feed duplicate or a dealer group listing the car at two sites, and one listing with a VIN seen two years earlier is the same car with a new seller. The work is in the listings without a VIN, and in protecting the VIN itself, which some markets treat as personal data when linked to an owner. Enrichment from the VIN is owned by [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment).

General goods have no entity to resolve to. **Do not invent one.** A marketplace that tries to attach every used item to a product catalog meets the problem eBay met when it mandated catalog association for listings in 2018–2019 and later relaxed it (see [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas)). For goods, duplicate detection protects the result page from abuse; it does not build an entity.

{id: entity-resolution--the-matching-pipeline}
## The Matching Pipeline

The reference architecture below is an inference from public algorithms and the few public marketplace designs, not a description of any company's system. Its stages are standard in the record-linkage literature; what is specific to listings is the mix of signals and the speed at which clusters change.

![Diagram: The matching pipeline](listing-systems-architecture/posts/15-entity-resolution/assets/images/15-entity-resolution/fig02-matching-pipeline-blocking-scoring-clustering-propose.jpeg)

**Figure 2:** *The matching pipeline. Blocking, scoring and clustering propose links; the entity registry owns the identifiers; a policy engine turns one cluster into different actions for different duplicate kinds; and human decisions feed back into both the registry and the model.*

{id: entity-resolution--blocking-finding-candidates-cheaply}
### Blocking: finding candidates cheaply

Comparing every listing with every other listing is impossible: Hearthly France alone has 1.9 million live listings, which is about 1.8 trillion pairs. **Blocking** generates a small set of candidate pairs using cheap keys with high recall, so that the expensive scoring runs only on plausible pairs. A listing usually gets several blocking keys, and any shared key makes a pair a candidate:

- **Category and place**: property type and an H3 hexagonal cell at fine resolution (H3 is Uber's open hierarchical geo index; see [Where Is It? Location, Geocoding and Privacy](#location-and-geo)), plus a rounded price band.
- **Normalized address** where one exists: the address normalized by the enrichment stage, and the building ID once the address is linked to it.
- **Hard identifiers**: VIN, partner listing reference, the agency's own mandate number when a feed carries it.
- **Text fingerprints**: MinHash locality-sensitive hashing over shingles of title and description. MinHash estimates the Jaccard similarity of two sets; it goes back to Andrei Broder's 1997 work on document resemblance, first used for duplicate web pages. SimHash, published by Manku, Jain and Das Sarma at Google in 2007 ([WWW 2007](https://research.google/pubs/detecting-near-duplicates-for-web-crawling/)), does the same job with a single fingerprint compared by Hamming distance.
- **Image fingerprints**: bands of a perceptual hash for each photo. Meta's PDQ, released as open source on 1 August 2019 ([Meta, 2019](https://about.fb.com/news/2019/08/open-source-photo-video-matching/)), is a common choice; its documentation suggests starting with a match threshold of Hamming distance 31 or less and discarding low-quality hashes, then tuning on your own data ([PDQ documentation, n.d.](https://github.com/facebook/ThreatExchange/tree/main/pdq)). [Photos Sell: Media Pipelines for Listings](#media-pipeline) computes these hashes for every image.
- **Account keys**: seller, organization, device and network identifiers, which separate same-seller reposts from cross-seller matches.

Blocking is a recall decision. A pair that shares no key is never compared, so a missing key is a silent miss. The usual failure is a key that seems safe but splits true matches: blocking on exact address misses the agency that writes "rue de Marseille" without a number, and blocking on the H3 cell misses listings near a cell boundary unless neighboring cells are included.

{id: entity-resolution--pairwise-scoring-is-this-pair-the-same-thing}
### Pairwise scoring: is this pair the same thing?

Each candidate pair gets a score from field-level comparisons: text similarity, image distance, geographic distance, surface and room agreement, price gap, same organization, same device, time between postings. Two families of scorer are in common use.

**Probabilistic record linkage** in the Fellegi–Sunter tradition weighs how much each field's agreement or disagreement says about a match, and can estimate those weights without labeled data. Splink, an open-source library from the UK Ministry of Justice, implements it; its documentation says "no training data is required", that it links "a million records on a laptop in around a minute", and that Spark suits 100 million records or more ([Splink, n.d.](https://github.com/moj-analytical-services/splink)). It is a good first scorer because its weights are explainable to a reviewer.

**Supervised pairwise classifiers**, often gradient-boosted trees, learn from pairs that people have labeled as same or different. The best public classifieds-specific design is still OLX's, presented by Alexey Grigorev at PyCon DE in 2019: candidate generation by category, city, seller, IP and device, and image hashes, then a classifier trained on human-labeled pairs using price difference, location distance, title similarity and image similarity. For images it layered MD5, then dHash, then MobileNet embeddings reduced with PCA and indexed with random-projection locality-sensitive hashing in Elasticsearch, fed by an S3 upload event, AWS Lambda and a queue, with a target of about 10 million listings a day. The talk also noted that cropping, rotating and flipping break the hashes ([PyCon DE, 2019](https://pycon.de/archive/2019/talks/fighting-fraud-finding-duplicates-at-scale/)). The design is seven years old and OLX's current system is not public, but the shape has aged well.

Scores must be **calibrated** so that thresholds mean something, and the score bands map to actions: above an upper threshold, link automatically; below a lower one, do nothing; between them, send the pair to human review. The gray zone is where the money is spent, so its width is a budget decision.

{id: entity-resolution--clustering-from-pairs-to-groups}
### Clustering: from pairs to groups

Pairs are not clusters. If listing A matches B and B matches C, the obvious step is to put A, B and C together, which is **connected components** clustering. It is simple and it fails in a predictable way: **chaining**. One weak link between two otherwise separate groups merges them, and in dense housing a chain of plausible links can merge a whole building. Safer methods require a cluster to be internally consistent: every member must match most other members (correlation clustering, or a minimum average link score), and a cluster above a size limit is split or sent to review. In real estate, a cluster with more than a handful of members is almost always wrong, because a property rarely has more than four or five agencies at once.

{id: entity-resolution--the-entity-registry-stable-identifiers-and-lineage}
### The entity registry: stable identifiers and lineage

The entity registry keeps cluster identifiers stable. Clustering produces new groups each time it runs, but consumers need **identifiers that stay the same** when it reruns, so that a buyer's saved property, a price-history chart and a valuation series do not jump to a new ID every night. The registry assigns each cluster a durable ID, keeps the ID when membership changes slightly, and records **merge and split events** with lineage when two clusters become one or one becomes two. A merge keeps the older ID and retires the other with a pointer; a split keeps the ID on the larger part. Consumers subscribe to these events like any other domain event (see [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)).

The registry is also where the **canonical entity** lives: the canonical property's address, building, unit features and identifiers, with per-attribute provenance. Survivorship rules decide which value wins when members disagree. Surface might come from the energy diagnostic where present, else the most common value among professional listings; the address comes from the most precise geocode. The listing keeps the seller's own values. **The canonical property does not overwrite the listing**, because the listing is the seller's statement and carries legal weight in some markets. Valuation, price history and analytics read from the canonical record; the listing page shows what the seller published.

![Diagram: A listing's membership in a cluster has its own lifecycle](listing-systems-architecture/posts/15-entity-resolution/assets/images/15-entity-resolution/fig03-listing-s-membership-cluster-has-own.jpeg)

**Figure 3:** *A listing's membership in a cluster has its own lifecycle. Human decisions are durable: a rejected or disputed pair is suppressed so that the next model run cannot re-create it, and unpublished listings detach so the cluster's state follows its live members.*

**A human "not the same" decision must be stored as a constraint** (Figure 3), not just as a label for the next training run, or the nightly job will reunite the pair and the agency that complained will complain again.

Membership also follows the listing lifecycle (see [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate)). When the last live listing in a cluster is unpublished, the cluster is no longer "on the market", even though the property entity persists. A cluster that stays active after its members have gone is Ghost Inventory in a new form: an alert subscriber or a market report sees a property for sale that nobody is selling.

{id: entity-resolution--online-and-batch}
### Online and batch

Resolution runs at two speeds. **Online** checks at publication time are cheap and local: exact and perceptual image hashes against recent listings, same-seller text near-duplicates, VIN and partner-reference lookups. They catch reposts and cloned listings before they go live, and they attach new listings to existing clusters when a strong key matches. **Batch** resolution, typically nightly, runs global blocking and clustering across all listings, finds cross-seller and cross-feed clusters, and repairs clusters as listings change. The online path must finish inside the publication budget set in [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline); anything that does not fit runs after publication and adjusts the presentation a few minutes later.

{id: entity-resolution--merge-policies-what-each-audience-sees}
## Merge Policies: What Each Audience Sees

A cluster changes something different for each audience, and choosing what it changes is product policy expressed in architecture. The most common mistake is to apply one policy, usually "hide the others", everywhere.

| Audience or system | Policy options | Recommended default for legitimate clusters |
| --- | --- | --- |
| Buyer, search results | Show all; collapse to one card with "also listed by"; hide the others | Collapse to one property card, with every agency reachable from it |
| Buyer, listing page | Show only this listing; show "also listed by" with other agencies and prices | Show the other listings, including prices, with clear agency names |
| Buyer, saved-search alerts | Alert per listing; alert per property | One alert per property; a new agency on a known property is an update, not a new match |
| Buyer, price-drop alerts | Per listing; per property | Per property, on the lowest live asking price, with the agency named |
| Agency or dealer | Not shown; shown own clusters only | Show each agency the clusters its own listings belong to, never other agencies' private data |
| Valuation and price history | Per listing; per property | Per property, using one asking-price series per listing to avoid triple counting |
| Inventory and market metrics | Count listings; count properties | Report both; use properties for "supply" and listings for "advertising volume" |
| Lead routing | To the card shown | To the agency the buyer chose; never re-route a lead to another agency |

{id: entity-resolution--collapsing-in-search}
### Collapsing in search

The usual implementation stores the cluster ID on each listing's search document and asks the engine to return one document per cluster. Elasticsearch calls this **field collapsing**: the `collapse` parameter keeps only the top-sorted document for each value of a single-valued keyword or numeric field, and optional `inner_hits` return the other members. Its documentation also lists the costs an architect should know before relying on it: the total hit count still counts all matching documents, not the number of groups; aggregations are not collapsed; each `inner_hits` request adds a query per collapsed hit; and collapsing cannot be combined with scroll ([Elastic, n.d.](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/collapse-search-results)). So the result list shows 1,000 properties while the facet counts and the "2,400 results" header still count listings. **Either the counts are computed on a property-level document, or the page shows numbers that disagree with the list.** A common answer is a second, property-level index for counting and map pins, built from the same events; [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) covers the index design.

{id: entity-resolution--choosing-the-representative}
### Choosing the representative

When a cluster collapses to one card, one listing's photos, price and agency appear first. This is the most politically sensitive decision in the chapter. The options are the most complete listing, the earliest published, the lowest price, the highest quality score, rotation among agencies, or the listing that pays for visibility. Each one rewards a different behavior. "Lowest price" rewards the agency with the lowest fee. "Earliest" rewards the agency that publishes first. "Quality score" rewards good photos and complete attributes, which is what buyers want. "Paid" silently turns deduplication into an auction.

My rule is that **the representative rule is a published ranking parameter**, decided by product and legal together, and never changed by an engineer tuning a model. If paid placement affects it, the card says so. The EU Platform-to-Business Regulation and the DSA both require the main ranking parameters to be described to business users and consumers ([Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)). A representative rule is one of them. **Paid-Rank Drift often starts in a cluster rule that nobody thinks of as ranking.**

{id: entity-resolution--a-documented-example-idealista-s-duplicate-control}
### A documented example: Idealista's duplicate control

The clearest public product example comes from Idealista, the Spanish, Italian and Portuguese property portal. In April 2021 it launched a duplicate-control tool for home seekers that groups the ads for one property published by several agencies or individuals, *including on other portals*, so that users can compare them in one place. Users see the number of duplicates, price changes, removed ads and new duplicates, and get push notifications when a price changes, an ad is removed or a new duplicate appears. Agents see duplicates only of their own properties, and only once a listing has been published. The tool is updated daily ([Online Marketplaces, 2021-04-11](https://onlinemarketplaces.com/articles/idealista-launches-new-tool-to-help-organize-duplicate-listings)). The report describes the product, not the matching system, and the current state of the tool is not public. Three design choices are worth noting: the cluster is presented as **buyer information** rather than hidden, the **agent view is limited to their own properties**, and the cadence is daily, which suggests batch resolution.

{id: entity-resolution--in-practice-resolving-the-lyon-apartment}
## In Practice: Resolving the Lyon Apartment

Here is how the Lyon flat moves through the pipeline Hearthly built in 2027. The design is Veldmark's, and the numbers are illustrative.

**The three listings.** The listings arrive over four days in May 2027:

| | Listing A | Listing B | Listing C |
| --- | --- | --- | --- |
| Agency | Agence Rhône Habitat (branch Lyon Jean-Macé) | A second agency, independent | A third agency, part of a franchise |
| Channel | Keybridge | Software vendor 1 | Software vendor 2 |
| Asking price, fees included | €389,000 | €389,000 | €395,000 |
| Surface and rooms | 68 m², T3 | 68 m², 3 rooms | 67.8 m², 3 rooms, 2 bedrooms |
| Address in feed | Full street and number | Street only | Street and number, different spelling |
| DPE | D | D | D |
| Photos | 14 | 11 | 9, of which 6 match listing A's photos (PDQ distance below 20) |

**Blocking.** All three share the building: listings A and C geocode to the same address, and the address links to one building ID. Listing B has no street number, but it shares the H3 cell, the property type and the price band, and five of its photos fall into the same perceptual-hash bands as listing A's. Blocking produces three candidate pairs and, in the same building and cell, 41 pairs with other listings, mostly other flats in the same block.

**Scoring.** Pair A–C scores 0.97: same address, same DPE class, surface within 0.5%, six shared photos, different organizations. Pair A–B scores 0.88: no street number, but matching surface, rooms and DPE, five shared photos taken from the same viewpoints. Pair B–C scores 0.84. The 41 other pairs score below 0.3. Hearthly's thresholds put automatic linking at 0.92 and the gray zone between 0.70 and 0.92.

**Clustering and review.** A–C links automatically. A–B and B–C go to the review queue. A reviewer sees the shared photos and the same balcony, confirms both within the hour, and the three listings become one cluster with one canonical property ID. The canonical record takes its address from listing A, its surface from the DPE certificate data, and its building ID from the address link.

**Presentation.** Search shows one card. The representative rule Hearthly published in 2027 picks the listing with the highest completeness and media-quality score, here listing A, and shows "also listed by 2 other agencies, from €389,000". All three agencies are one click away, and a lead goes to whichever agency the buyer contacts. The price-drop alert subscribes to the cluster, so when listing C drops to €389,000 it is reported as "now €389,000 at a third agency", not as a new listing. Valuo values the property once, with its estimate of **€372,000–€401,000**, and the property's price history records three asking-price series against one property instead of three properties.

![Before: three cards, three alerts and a triple count for one Lyon flat. After: one property card with all three agencies reachable, one alert and one count.](listing-systems-architecture/posts/15-entity-resolution/assets/images/15-entity-resolution/lyon-flat-before-after.jpeg)

**Figure 4:** *Resolved, the Lyon flat is one property card with every agency one click away, one alert per property and one property in Valuo's price history instead of three.*

**The Keybridge constraint.** Veldmark decided in March 2027 that Hearthly may not use Keybridge agency data for ranking or sales targeting (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). Keybridge holds far more about the Lyon flat than Hearthly does, including the mandate and the seller's identity. Entity resolution at Hearthly may use **only what each listing carries as published to Hearthly**, exactly as it would for a listing from any other software vendor. That rule is enforced in the data path: the matcher reads Hearthly's listing read model, never Keybridge's database, and the access-control review checks it every year. Without it, a better match rate would cost Veldmark the trust of every agency that uses Keybridge to publish to Hearthly's competitors.

**What changed.** After the first quarter of the new pipeline, Ingrid's review uses four numbers, all illustrative. Search pages in Lyon show 31% fewer cards for the same queries. Saved-search alerts for Lyon sales fall by 24% with no fall in click-through, which means the removed alerts were noise. Precision measured on 4,000 labeled pairs is 98.6% and recall 91%. Agency disputes run at about 60 a month across France, two thirds of them for flats in the same building that the matcher wrongly merged. Those disputes are the most valuable labels the team has.

{id: entity-resolution--the-same-machinery-pointed-at-abuse}
### The same machinery pointed at abuse

The same detectors run on Tradeyard, Veldmark's general classifieds brand, for a different purpose. A same-seller repost of a listing already live in the same category is blocked at publication, with a message that offers a paid bump instead. A delete-and-recreate within days keeps the original creation timestamp, so the new listing gains no freshness advantage (see [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) on why bumps and renewals update a ranking timestamp, never the creation time). This is a monetization and trust decision as much as a technical one: **a marketplace that sells bumps and tolerates free reposts is competing with itself.**

**The registry must record why listings were linked**, because a stolen copy must never be shown to buyers as "also listed by". At Hearthly Spain, the same kind of perceptual-hash matching flagged the Barcelona fake-rental ring in July 2027. Twenty-six accounts posted 180 fake rental listings in Eixample using photos stolen from real listings and priced about 35% below market. The match between a new, unrelated account and photos already attached to another agency's live listing, combined with the price anomaly, is the fraud signal. The hash matches fired from the first day, but they went to a different queue from the price flags, and eleven photo-match items were closed as legitimate multi-agency duplicates before an analyst linked the cluster. The policy engine sends such clusters to trust and safety, not to the presentation layer. The case and its cost are in [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention).

{id: entity-resolution--trade-offs}
## Trade-offs

| Decision | Option | When it is right | What it costs |
| --- | --- | --- | --- |
| Where duplicates are resolved | At ingestion, before publication | Abuse checks, strong keys (VIN, partner reference) | Latency in the publication path; must be cheap and local |
| | Batch, after publication | Cross-seller clusters, global repair | Duplicates visible for hours |
| | At query time only (collapse on a similarity key) | Prototypes | No stable entity; counts and alerts stay wrong |
| Scorer | Probabilistic linkage (Fellegi–Sunter, Splink) | No labels yet; explainability needed | Weaker on images and free text |
| | Supervised classifier | Labeled pairs available; mixed signals | Needs a labeling program and monitoring |
| | Embedding similarity | Augmented images, multilingual text | Hard to explain; expensive at scale |
| Clustering | Connected components | Small, sparse data; strong keys | Chaining into giant clusters |
| | Consistency-constrained clustering with size limits | Dense housing, many weak signals | More complex; needs tuning |
| Presentation | Hide duplicates | Abusive duplicates only | Agencies lose visibility; disputes |
| | Collapse with "also listed by" | Legitimate multi-agency clusters | Count and facet inconsistencies to solve |
| | Show all with a badge | Early stage, low confidence | Buyers still see the echo |
| Entity ownership | Shared group registry | Several brands in one vertical and country | Coordination and legal review across brands |
| | Per-brand registry | Brands in different verticals | Duplicated machinery |

The trade-off that decides most of the others is **where the cluster ID is stored**. If it exists only as a field on search documents, the index becomes the only place that knows which listings belong together, and nobody can rebuild it from anything else. That is **Index-as-Database** in miniature. The registry is the system of record for clusters; search, alerts and analytics hold copies.

{id: entity-resolution--vertical-differences}
## Vertical Differences

| Dimension | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Dominant duplicate kind | Same-seller reposts, freshness gaming, cloned scam listings | Multi-agency listings, cross-feed copies | Cross-feed copies, dealer groups listing at several sites | Reposts by recruiters and job boards |
| Resolvable entity | None for unique goods; product for catalog goods | Property, building, parcel | Vehicle by VIN | Vacancy, weakly |
| Strongest signals | Account, device, image hashes, text | Address and building ID, surface, rooms, energy class, photos | VIN, partner reference, make, model, mileage | Employer, title, location, text |
| Main action | Enforcement | Clustering for presentation | Silent merge at ingestion | Clustering, enforcement for spam |
| Typical scale of clusters | Many small groups | Two to five members | Two members | Two to dozens |
| Specific risk | Stock and manufacturer photos flooding the detector | Over-merging units in one building | Missing VINs on private listings | Merging distinct vacancies with the same title |
| Who disputes | Rarely anyone | Agencies, strongly | Dealers, occasionally | Employers and agencies |

In general classifieds, a perceptual-hash detector without an allowlist of manufacturer images floods moderators with false matches, because **legitimate stock photos** are common in some categories, such as new phones or furniture.

In automotive, the VIN makes resolution easy, which tempts teams to skip the gray zone entirely; the cost shows up when a dealer group lists one car at two sites with different prices and the merge picks the wrong one as representative.

{id: entity-resolution--failure-modes}
## Failure Modes

1. **One "duplicate" flag for everything.** Abusive and legitimate duplicates share a boolean, so agencies' legitimate listings get demoted like spam, or scam copies get shown as "also listed by". Keep the duplicate kind on every link.
2. **Giant clusters.** Connected components chains weak links until a 40-flat building becomes one "property". Cap cluster size, require internal consistency, and alert when a cluster grows past a threshold.
3. **Unstable cluster IDs.** The nightly job renumbers clusters, so favorites, alert subscriptions and price histories break or jump between properties. The registry must keep IDs stable and publish merges and splits as events.
4. **Human decisions forgotten.** A reviewer separates two flats; the next batch run merges them again. Store reviewer and dispute outcomes as constraints the clustering must respect.
5. **Counts that disagree with the page.** Collapsed results with listing-level facet counts tell buyers "2,400 results" above 1,000 cards. Decide what a result is and count that.
6. **The representative rule as a hidden auction.** An engineer adds paid status to the representative score. Agencies notice within a week. Treat the rule as a published ranking parameter with an owner.
7. **Clusters that outlive their listings.** The last live member is sold and unpublished, but the cluster still drives alerts and market reports. Tie the cluster's market state to the lifecycle of its members.
8. **The unmeasured matcher.** Thresholds were set once, the model was never re-evaluated, and a new software vendor's address format halves recall without anyone noticing. Keep a labeled evaluation set, refreshed every quarter, and monitor match rates per source.
9. **Using data you are not allowed to use.** Matching across brands, or using a CRM's private data, links records the group has no legal basis or business permission to link. Make the allowed inputs part of the matcher's contract and review them.
10. **Keeping hashes forever.** Perceptual hashes of removed listings are valuable against fraud and are also personal data in some contexts. Retain them for a documented purpose and period, owned with trust and safety.

{id: entity-resolution--the-chief-architect-s-view}
## The Chief Architect's View

At group scale, entity resolution raises five decisions.

**1. Share the machinery, not necessarily the entities.** Blocking, scoring, clustering, the registry pattern, review tooling and evaluation are the same problem in every brand, and Common Ground should build them once. Entities are vertical: Hearthly's canonical property, Motorvane's vehicle and Tradeyard's abuse clusters have different identifiers, policies and owners. The platform provides the engine; each vertical domain owns its entity model and its policies.

**2. Name the owner of each entity.** The canonical property belongs to Hearthly's listing data domain, because valuation, search and pro reporting depend on it. Abuse clusters belong to the trust-and-safety platform under Aisha Rahman, because their actions are enforcement with appeals. Cross-feed merges belong to ingestion. Each owner sets thresholds, answers disputes and signs off on model changes. **A matcher without an owner is The Unwatched Model, even if it is very accurate.**

**3. Decide the legal boundary of linking.** Linking listings across brands, such as a Tradeyard Portugal flat and a Hearthly listing, or using Keybridge data at Hearthly, is a data-protection and competition question before it is a technical one. Lucía Ortega, the Group Data Protection Officer, decides with the brand owners which sources may be linked, and the decision is written into the matcher's input contract.

**4. Govern the representative rule as ranking.** Product, legal and the search platform decide it together, publish it, and change it through the same experiment and review process as any ranking change (see [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) and [Testing a Two-Sided Market: Experimentation Platforms](#experimentation)).

**5. Watch a small set of numbers.** Listings per entity by market (1.7 at Hearthly France is the baseline); precision and recall on a labeled sample; gray-zone volume and review cost; cluster churn per night; dispute rate and overturn rate by agency; and the share of live listings with a resolved entity. A sudden change in any of them is usually a feed or enrichment change upstream, which is why the dashboard belongs next to the feed-health dashboard of [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion).

{id: entity-resolution--questions-to-ask}
## Questions to Ask

1. For each duplicate kind we see, what is the action, who owns it, and does the seller get a statement of reasons when the action is a restriction?
2. What real-world entity are we resolving to in this vertical, and which identifiers do we actually receive, at what fill rate?
3. Where is the cluster ID stored as the system of record, and can we rebuild every downstream copy from it?
4. Are cluster IDs stable across runs, and are merges and splits published as events with lineage?
5. How do reviewer decisions and seller disputes constrain the next clustering run?
6. What are precision and recall on a labeled sample from the last quarter, per market and per source?
7. What stops a chain of weak links from merging a whole building or a dealer's whole stock?
8. What is the published rule for the representative listing, and does payment affect it?
9. Do result counts, facets, map pins and alerts count the same thing as the result list?
10. Which data sources is the matcher allowed to read, who approved that list, and how is it enforced?

{id: entity-resolution--from-clean-supply-to-live-supply}
## From Clean Supply to Live Supply

Entity resolution turns many copies into one view of what is really for sale. It works only if it fits inside the path every listing takes from submission to visibility, with cheap checks before publication and the heavier clustering after. That path, its stages, its latency budget and the way removals propagate to every copy, is the subject of [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline).

{id: entity-resolution--sources-and-evidence}
## Sources and Evidence

{id: entity-resolution--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Fighting fraud: finding duplicates at scale](https://pycon.de/archive/2019/talks/fighting-fraud-finding-duplicates-at-scale/) — Alexey Grigorev (OLX), PyCon DE, 2019. Candidate generation, pairwise classifier and layered image hashing for duplicate listings; the hashing limits.
- [Zillow Group Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm) — Zillow Group, filed 2026. The "living database" of about 173 million homes and 46 million user-updated property records.
- [Idealista launches new tool to help organize duplicate listings](https://onlinemarketplaces.com/articles/idealista-launches-new-tool-to-help-organize-duplicate-listings) — Online Marketplaces, 2021. Idealista's duplicate-control tool: cross-portal grouping, notifications, agent visibility rules, daily updates.

{id: entity-resolution--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [OS Open UPRN](https://www.ordnancesurvey.co.uk/products/os-open-uprn) — Ordnance Survey, n.d. Unique identifiers and coordinates for about 40 million addressable locations in Great Britain.
- [Base Adresse Nationale](https://adresse.data.gouv.fr/) — French government, n.d. National open address base and its update cadence.
- [Référentiel National des Bâtiments](https://rnb.beta.gouv.fr/) — RNB team, n.d. The ID-RNB as a unique, durable building identifier and open data.
- [Collapse search results](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/collapse-search-results) — Elastic, n.d. Field collapsing semantics and limits: total hits, aggregations, inner hits, scroll.
- [PDQ and TMK+PDQF open-source release](https://about.fb.com/news/2019/08/open-source-photo-video-matching/) — Meta, 2019. Release of the PDQ perceptual hash.
- [PDQ documentation](https://github.com/facebook/ThreatExchange/tree/main/pdq) — Meta ThreatExchange, n.d. Quality and Hamming-distance starting thresholds.
- Regulation (EU) 2022/2065 (Digital Services Act), Art. 17 — European Union, 2022. Statements of reasons for restrictions, including demotion; detailed in [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation).

{id: entity-resolution--research-and-practitioner-sources}
### Research and practitioner sources

- [Detecting near-duplicates for web crawling](https://research.google/pubs/detecting-near-duplicates-for-web-crawling/) — Manku, Jain and Das Sarma, Google, WWW 2007. SimHash fingerprints for near-duplicate detection.
- A. Broder, "On the resemblance and containment of documents" — 1997. Origin of MinHash for estimating document similarity.
- [Splink](https://github.com/moj-analytical-services/splink) — UK Ministry of Justice, n.d. Open-source Fellegi–Sunter record linkage without training data; scale guidance.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
