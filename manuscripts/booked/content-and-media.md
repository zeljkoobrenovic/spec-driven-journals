{id: content-and-media}
# 7. Describing a Stay: Content, Media and Property Mapping

![Describing a Stay: Content, Media and Property Mapping — logo](stays-marketplace-architecture/posts/07-content-and-media/assets/images/07-content-and-media/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow content from its sources (extranets, connectivity content APIs, wholesale feeds and host editors) through normalization, media processing, translation and quality scoring into the pages and feeds where guests read it. You will also see how an accommodation marketplace recognizes the same hotel and the same room when they arrive from several suppliers.

> **WHY THE BUSINESS CARES:** Guests book what they can see and understand. Photos, amenities and policies drive conversion, and misleading content drives complaints, refunds and regulatory attention. For an online travel agency (OTA) that buys wholesale supply, mapping quality also decides whether new inventory adds bookings or adds duplicates.

> **WHY ARCHITECTS SHOULD CARE:** Content looks like the easy, static part of a stays platform, but it is written by hundreds of thousands of authors, arrives through several channels that overwrite each other, is read by search, ranking, pricing, checkout and regulators, and has to exist in dozens of languages. Without field-level ownership and provenance, nobody can say which version of a description or a policy a guest actually saw.

> **KEY POINTS:**
>
> * **Content is a catalog with authors, not a blob of text.** Store every field with its source, its version and the rule that lets one source overwrite another. Hotel content arrives from feeds that compete for the same fields; home content is written by the host in the marketplace's own editor. The two need different write paths into the same kind of governed store.
> * **Anything with legal or financial meaning must be structured, not written.** Cancellation terms, fees, taxes, registration numbers and accessibility claims should be rendered from structured data in every language. Free-text "important information" that contradicts the rate plan is how Policy Spaghetti reaches the guest.
> * **Property and room mapping is a core platform service for an OTA.** The same hotel arrives from extranets, channel managers, bedbanks and GDS feeds under different names and codes. Mapping needs blocking, scoring, thresholds, a human review queue, stable identifiers and a measured error rate, because a false merge sells the wrong hotel and a missed match lists the same hotel twice.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **The Same Hotel Twice** — wholesale and connectivity feeds bring hotels the catalog already has, and without a mapping service they become duplicate products with different rooms, photos and prices.
> * **Policy Spaghetti** — cancellation and fee terms typed into free-text description fields disagree with the structured policy that checkout and refunds use.
> * **The Hotel-Shaped Home** — a content template built for hotels (room types, star ratings, facility lists) is forced onto homes, so the details that sell a home (sleeping arrangements, house rules, the host) have nowhere to go.

Part II treats supply as master data with many writers, and descriptions have more writers than any other part of it. [Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model) fixed what is sold, and [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding) checked each property's content only for minimums. This chapter governs the content itself, which search, ranking, the property page, support and regulators all read.

A guest who books a night has never seen the room. They have seen **a description**: photos, amenities, a bed configuration, some text, a cancellation policy and a total price. The marketplace sells that description as a promise, and a property or host fulfils it. When the room does not match, the marketplace pays for a refund or a relocation.

An **accommodation marketplace** receives most hotel content from systems: the partner extranet, connectivity partners, wholesale (bedbank) feeds and global distribution system (GDS) content, all competing for the same fields. A **hosted-stays marketplace** receives most content from a host typing into its own listing editor: one source, closer to the truth, but unstructured and often changed. Both then need the same downstream machinery: media processing, translation, quality scoring and publication.

This chapter owns three terms. **Content mapping** decides whether a property or room arriving from one source is the same real-world property or room as one the marketplace already knows. A **content score** is a measured, explainable rating of how complete, current and consistent a property's or listing's content is. The **media pipeline** ingests, checks, classifies, transforms, moderates and serves photos and other media. Connectivity messages belong to [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers) and review text to [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation). LISTED's [Photos Sell: Media Pipelines for Listings](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/media-pipeline.html) and [One Property, Three Listings: Duplicates and Entity Resolution](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/entity-resolution.html) chapters cover the generic machinery; this chapter shows what changes when the item is a night's stay.

{id: content-and-media--setting-the-scene-at-corvane-41-000-hotels-most-of-which-we-already-had}
## Setting the Scene at Corvane: 41,000 Hotels, Most of Which We Already Had

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), sells **640,000** properties on Roomstead, its OTA-style marketplace. **68%** of that supply is in Europe and only **11%** in Asia-Pacific. In June 2027 Aisha Rahman, VP Supply and Connectivity at Roomstead, signed a wholesale agreement with **Brightwell Beds**, a fictional Singapore-based bedbank (a wholesaler that contracts hotel rooms and resells them to travel sellers). The deal was meant to fill gaps in Asia-Pacific and Latin America within one season instead of the three years that direct contracting would take.

Brightwell's content file listed **41,000** properties. The commercial team's slide counted them as 41,000 new hotels. Jonas Weber, Head of Search and Ranking, asked how many of them Roomstead already sold. Nobody could answer. Every one of its 640,000 properties had joined through Partner Hub, the Roomstead extranet, or through Switchyard, its connectivity gateway, with one Roomstead identifier from the day it signed. Roomstead had no service that could look at a hotel described by someone else and say "that is property 2,318,447".

A first naive pass made the risk concrete. Matching on exact name and city found **9,800** overlaps. Matching on name similarity and a 150-meter radius found **31,000**, along with obvious false positives: "Hotel Atlântico" and "Atlântico Apartments", two businesses in the same building in Porto, scored as one property. Brightwell's room codes were worse: free-text names such as "DLX DBL CITY VW RO" (deluxe double, city view, room only) across hundreds of thousands of room-and-board combinations.

Both kinds of error had a price. A **missed match** would put the same Bangkok hotel on Roomstead twice, once with the hotel's own photos and flexible rates and once with Brightwell's photos and non-refundable net rates: **The Same Hotel Twice**. A **false merge** would sell a Brightwell rate for one hotel on the page of another, and the guest would arrive at a hotel that had no booking: **Lost at the Front Desk**, caused by content rather than connectivity.

Mariana Costa, the Group Chief Architect, framed the question for the architecture forum: **"Who decides which supplier's description of a hotel is true, and how do we prove that a room we sell is the room the supplier will honor?"**

{id: content-and-media--concepts-sources-fields-provenance-and-scores}
## Concepts: Sources, Fields, Provenance and Scores

{id: content-and-media--where-content-comes-from}
### Where content comes from

Content reaches a stays marketplace through five kinds of source, each with its own trust problem.

| Source | Who writes | Typical content | Change rate | Trust problem |
| --- | --- | --- | --- | --- |
| **Partner extranet** | Hotel staff | Descriptions, photos, facilities, policies, room set-up | Weekly to yearly | Stale content; free text that contradicts structured data |
| **Connectivity content APIs** | Property management system (PMS), central reservation system (CRS) or channel manager on the hotel's behalf | Room types, amenities, photos, licenses, descriptions | On change, often in bulk | Overwrites edits made in the extranet; lossy code mapping |
| **Wholesale and GDS feeds** | Bedbank, wholesaler or GDS content team | Property catalog, room codes and names, photos, board basis | Daily files | Different names and codes for the same property; second-hand photos |
| **Host listing editor** | Individual host | Title, description, photos, sleeping arrangements, house rules, amenities | Frequent, small edits | Unstructured, optimistic, sometimes false |
| **Vacation-rental software API** | PMS of a professional manager | Whole listing or parts of it | Continuous | Overwrites the host's in-app edits; unclear ownership |

Booking.com's connectivity documentation separates content into Property, Rooms, Facilities, Charges, Content, Photo and Licences APIs, next to the rates, availability and reservations APIs ([Booking.com Connectivity APIs](https://developers.booking.com/connectivity/docs), undated, live October 2026). Expedia's Rapid API, the distribution side of Expedia Group, gives downstream sellers a **Property Catalog File** that it calls "useful for mapping suppliers" and a separate **Property Content File** with property, room and rate content. It recommends refreshing property content daily ([Expedia Group Rapid content](https://developers.expediagroup.com/rapid/lodging/content/about-content-api), undated, fetched October 2026). On the hosted-stays side, Airbnb lets hosts who use connected software choose between "Sync everything", where listing details come from the software, and "Sync pricing and availability", where content stays under the host's control on Airbnb ([Airbnb Help Center, article 2348](https://www.airbnb.com/help/article/2348/what-are-the-ways-i-can-sync-listings-through-my-api-connected-software), undated, live October 2026). That choice is a content-ownership decision exposed to the host.

{id: content-and-media--descriptive-content-standards}
### Descriptive content standards

The OpenTravel Alliance message set, the XML standard most hotel connectivity uses, includes descriptive-content messages (`OTA_HotelDescriptiveContentNotif` for property content and `OTA_HotelInvNotif` for room definitions and amenities) and code lists such as the room amenity (RMA) codes. HTNG (Hospitality Technology Next Generation) built a Distribution Content Management specification on top of it ([AltexSoft overview](https://www.altexsoft.com/blog/hotel-tech-specifications-htng-opentravel/), 2020; the source is six years old), and regional profiles such as AlpineBits carry descriptions, images and license metadata ([AlpineBits HotelData](https://www.alpinebits.org/hotel-data/), release 2024-10).

In practice the standard gives names, not interoperability. Every channel publishes its own profile and code list. Booking.com's amenity code documentation says that several codes collapse into one internally (codes 28, 29 and 64 all default to 28, "Desk"), so a value written with one code reads back as another ([Booking.com RMA codes](https://developers.booking.com/connectivity/docs/codes-rma), undated, fetched October 2026). Channels are also moving away from the original messages: as of October 2026, Booking.com has deprecated `OTA_HotelInvNotif` for Home providers (December 2024) and will sunset it for them on 31 December 2026, in favor of its Rooms and Facilities APIs ([Booking.com, managing room amenities](https://developers.booking.com/connectivity/docs/tsk-modify-room-amenities.md), undated, live October 2026). Hosted-stays marketplaces have no open content standard at all; content travels over each marketplace's own partner API.

**The marketplace's internal content model must be its own**, defined by what guests need to compare and what regulators require, with adapters that translate each source's vocabulary into it. Treating OpenTravel codes as the canonical model makes every channel's quirks permanent.

{id: content-and-media--fields-provenance-and-precedence}
### Fields, provenance and precedence

A property description is hundreds of fields with different owners: the address, the star rating, check-in times, each room type's beds, each amenity, each photo, each policy. Three things about each field matter.

- **Provenance**: which source wrote the current value, when, and through which channel.
- **Precedence**: which sources may overwrite which, per field. A hotel's PMS may own room amenities while the extranet owns the description and a bedbank may only fill fields that nobody else has supplied.
- **Verification state**: whether the value is a claim, has been checked by a person or a model, or is backed by evidence such as a photo or a registration database.

Airbnb's accessibility review is the clearest public example of verification state. Hosts submit a photo for each accessibility feature, and "a specialized team of Airbnb agents" reviews them; by November 2021 (the latest public figure; the program may have changed since) the team had confirmed **100,000** accessibility features across **25,000** homes ([Airbnb 2021 Winter Release](https://news.airbnb.com/2021-winter-release/), 2021). For hotels the same attribute usually arrives as an unverified code in a content feed. The asymmetry is reasonable, because a hotel is a professional operator that can be held accountable, but the data model must tell the two apart.

{id: content-and-media--the-content-score}
### The content score

A useful **content score** is measurable from the stored content, shows the partner or host which components cost them points, and predicts something that matters (conversion, complaints, or "not as described" claims). In its 2023 Winter Release, Airbnb introduced a listing editor and claimed that "Listings with more details can get up to 20% more bookings" ([Airbnb 2023 Winter Release](https://news.airbnb.com/en-uk/airbnb-2023-winter-release/), 2023). Booking.com's 2025 ranking disclosure says that review scores, availability, policies, pricing and **photo quality** feed the click-through and booking performance on which its default sort is based ([Booking.com, How we work](https://www.booking.com/content/how_we_work.html), updated May 2025). How either company computes its internal content measures is not public.

{id: content-and-media--architecture-a-governed-content-catalog}
## Architecture: A Governed Content Catalog

The architecture has five parts (Figure 1): source adapters, a canonical content store with field-level provenance, processing pipelines (media, translation, enrichment, mapping), a quality and policy layer, and published read models.

![Extranet, content APIs and bedbank files (through mapping) feed source adapters into a canonical content store; media, translation and quality services write back; read models publish to guests.](stays-marketplace-architecture/posts/07-content-and-media/assets/images/07-content-and-media/07-canonical-content-store.jpeg)

**Figure 1:** *Content flows from many writers into one canonical store that records who wrote each field. Wholesale feeds pass through mapping before they may write anything; media, translation and quality checks write their results back; guests only ever read published read models.*

{id: content-and-media--source-adapters}
### Source adapters

Each source gets an adapter that translates its vocabulary into the internal model and applies the precedence rules. The connectivity adapter maps OpenTravel amenity codes to internal identifiers; the host-editor adapter validates input as the host types; the bedbank adapter writes only after the mapping service has resolved the property and room identifiers. **Adapters never write directly to read models**: if a source adapter can update the search index, the marketplace has as many truths as it has adapters.

Precedence rules belong in versioned, reviewable configuration, not in the adapters' code. A rule reads like: "for a contracted hotel, room amenities from the connected PMS override the extranet; descriptions from the extranet override everything; bedbank content may fill empty fields only and never overwrites photos". Then, when a hotel's description keeps reverting (for example, a nightly channel-manager message restoring a 2021 version), support can show which source wrote each version and which rule allowed it, and the extranet can show "last written by".

Field-level writes also avoid overlay semantics, where a partial message replaces a whole section and loses content. Booking.com describes its Photo API as "completely separate from the Content API" and says it "does not use an overlay system", so that uploading photos will not "affect any other property content, which could result in potential data loss" ([Booking.com Photo API](https://developers.booking.com/connectivity/docs/photo-api/understanding-the-photo-api), undated, live October 2026).

{id: content-and-media--the-canonical-content-store}
### The canonical content store

The store holds each field's current value, history, provenance and verification state, keyed by the canonical identifier from [Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model). Three design choices matter more than the database.

1. **Versioned snapshots for what guests saw.** A guest who books on 14 February and complains on 9 August that the pool was closed is complaining about the description of 14 February, which may no longer exist. The reservation should reference a content version (or a hash of the published description and policies), so support can retrieve exactly what was shown. [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) owns the reservation; the content store owns the ability to reproduce the description.
2. **Structured fields for everything that has legal or financial meaning.** Fees, cancellation terms, deposits, check-in windows, registration numbers, pet and party rules and accessibility features are structured data, rendered into text per language. Free text is for atmosphere.
3. **Change events, not polling.** Every published change emits an event with the field, the old and new value and the source. Search indexing, ranking features, distribution feeds and the trust platform subscribe. [Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays) covers the event contracts.

{id: content-and-media--policies-and-fees-render-do-not-write}
### Policies and fees: render, do not write

Policy Spaghetti usually starts in a free-text field. Hotel staff type "Cancellations within 7 days of arrival are charged the first night" into the extranet's "important information" field in 2019; in 2024 the revenue manager changes the rate plan's structured policy to a 3-day window. The guest now sees two policies on one page, checkout charges one, and support quotes the other.

The rule I use is that **the marketplace renders every policy statement from the structured policy that the money path uses**: the same object that [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) evaluates when the guest cancels, in every language, by a template the policy team owns. Fees and charges work the same way: Booking.com's Charges API and Vrbo's structured `enhanced_house_rules` (pets, parties, children, smoking) in Expedia's Rapid documentation are public examples of moving such terms out of free text ([Expedia Group Rapid, Vrbo integration guide](https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-integration-guide), undated, fetched October 2026). A classifier scans the remaining free text for policy-like statements (deadlines, amounts, percentages, "non-refundable", "deposit") and asks the partner to remove the text or change the structured policy.

![Before: a handwritten 7-day note and a structured 3-day policy contradict each other. After: one structured policy renders the guest text and drives checkout, both saying 3 days.](stays-marketplace-architecture/posts/07-content-and-media/assets/images/07-content-and-media/07-render-policy-do-not-write.jpeg)

**Figure 2:** *When the guest's text is rendered from the same structured policy that checkout charges, a 7-day note can no longer contradict a 3-day rule.*

Regulation turns these fields into legal obligations. EU consumer law treats misleading information about the main characteristics of a product as an unfair commercial practice ([Directive 2005/29/EC](http://publications.europa.eu/resource/celex/32005L0029), Article 6). In the EU's coordinated consumer action of 2018–2019, Airbnb committed to show the total price including all mandatory charges and to distinguish professional traders from private hosts ([European Commission, accommodation booking action](https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/accommodation-booking_en), 2018–2020). The EU Short-Term Rental Regulation, which applies from **20 May 2026**, requires platforms to make sure hosts provide a registration number before a unit in a registration area is offered and to display it clearly ([Regulation (EU) 2024/1028](http://publications.europa.eu/resource/celex/32024R1028), Article 7). Each of these arrived on a regulator's date as a content field with a legal owner, a validation rule and a display rule; a store of structured fields absorbs the next one as configuration, a store of free text does not. [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) covers the obligations, and [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) covers how totals are shown.

{id: content-and-media--the-media-pipeline-for-stays}
## The Media Pipeline for Stays

The generic pipeline (upload, sanitize, hash, derive, store, serve through a content delivery network or CDN) is covered in LISTED's [Photos Sell: Media Pipelines for Listings](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/media-pipeline.html). Four things are specific to stays.

{id: content-and-media--photos-belong-to-rooms-not-just-to-properties}
### Photos belong to rooms, not just to properties

A guest choosing between a standard and a superior double needs to see each room type's photos. Booking.com's Photo API models this directly: uploaded photos land in a property-level gallery and can be moved to **room-level galleries** attached to room types; a property can upload at most **299** photos; and by default the property gallery is shown in an order chosen by a machine-learning model that Booking.com calls "smart ordering", which partners can switch off ([Booking.com Photo API](https://developers.booking.com/connectivity/docs/photo-api/understanding-the-photo-api), undated, live October 2026). Uploads are asynchronous: the partner submits a batch and later retrieves each photo's status, including errors and **duplicates**.

For a home, the unit is the listing, but the same need appears one level down: guests want to see each bedroom, the bathroom and the kitchen. Airbnb's 2023 Winter Release introduced an "AI-powered photo tour" that groups a listing's photos by room ([Airbnb 2023 Winter Release](https://news.airbnb.com/en-uk/airbnb-2023-winter-release/), 2023).

{id: content-and-media--classification-is-weakly-supervised-and-it-validates-the-description}
### Classification is weakly supervised, and it validates the description

In a 2018 engineering post, Airbnb described classifying listing photos into room types (bedrooms, bathrooms, living rooms, kitchens, swimming pools and views) by retraining a ResNet50 network ([Yao, Zhu and Siclait, Airbnb, 2018](https://medium.com/airbnb-engineering/categorizing-listing-photos-at-airbnb-f9483f3ab7e3)). Two details generalize:

- **Host captions as cheap labels.** Instead of paying vendors to label millions of photos, the team extracted labels from captions hosts had written, filtered them with rules because many captions did not match the image, and used a vendor-labeled random sample of thousands to tens of thousands of photos only as a "golden set" for evaluation.
- **Classification serves two sides.** On the guest side it allowed photos to be re-ranked and grouped by room; on the host side it made it "much easier to validate the number of certain rooms and check whether the basic room information is correct". The team aimed for 95% precision and 80% recall before launch.

Airbnb followed with a 2019 post on detecting amenities in listing photos ([Yao, Li and Chen, Airbnb, 2019](https://medium.com/airbnb-engineering/amenity-detection-and-beyond-new-frontiers-of-computer-vision-at-airbnb-144a4441b72e)). Both posts are seven or more years old and describe models that have likely been replaced; the current state is not public. The point holds: **vision models turn photos into evidence that can confirm or contradict structured content**. A listing that claims three bedrooms but shows one bed is a content-quality task; one that claims a pool and has no pool photo is a likely "not as described" complaint.

{id: content-and-media--moderation-and-abuse}
### Moderation and abuse

Photos carry risks that text does not: faces of previous guests, children, house numbers, car plates, documents left on tables, watermarks from other platforms, and photos copied from another listing to build a fake one. Perceptual hashing (a fingerprint that survives resizing and recompression) finds re-used photos across listings, and the results go to the trust platform as signals, not to the content team as edits. [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety) owns enforcement; the media pipeline owns detection and evidence. For wholesale content, perceptual hashes also help mapping: two supplier records whose photos match are very likely the same hotel.

{id: content-and-media--what-blocks-publication}
### What blocks publication

Not every check should block:

| Check | Blocks publication? | Why |
| --- | --- | --- |
| File is valid, safe and within size limits | Yes | Cannot be served otherwise |
| Photo is an exact or near duplicate of another listing's photo | Yes for homes, review for hotels | Copied photos are a common fake-listing signal for homes; hotels legitimately share photos across suppliers |
| Faces, documents or plates detected | Blur or hold for review | Privacy of third parties |
| Room-type classification disagrees with the gallery it was placed in | No; create a partner task | Cheap to fix, costly to block |
| Low resolution or poor lighting | No; lowers the content score | A quality problem, not a safety one |

{id: content-and-media--translation-one-source-of-truth-many-renderings}
## Translation: One Source of Truth, Many Renderings

Roomstead shows content in **41 languages**, so a description written in Portuguese needs 40 renderings and a policy must be correct in all 41. Three classes of text need three treatments.

| Text class | Examples | Treatment |
| --- | --- | --- |
| **Structured content** | Amenities, bed types, policies, fees, check-in times, property type | Never machine-translated: rendered from structured data with templates and terminology maintained per language |
| **Partner and host free text** | Descriptions, room names written by hand, house rules prose | Machine translation, cached per field version and language, with the original always one tap away |
| **Generated text** | Summaries, AI-written descriptions | Generated per language from structured data, with the same checks as partner text |

Airbnb's **Translation Engine**, announced in November 2021, automatically translates listing descriptions in "over 60 languages"; an evaluation commissioned by Airbnb across its ten top languages found that it "improves the quality of more than 99% of listings" ([Airbnb 2021 Winter Release](https://news.airbnb.com/2021-winter-release/), 2021). Slator reported in 2021 that the engine ran on ModernMT ([Slator](https://slator.com/airbnb-translation-engine-applies-machine-translation-to-ugc/), 2021); the engine has likely changed since. Airbnb later extended automatic translation to messages and reviews.

Three design rules apply to translated free text. **Store the original as the record of truth**, with its source language. **Key translations by field version**, so a source change invalidates exactly the translations it affects. **Show the original on request**, because a guest disputing a description, or a support agent judging a complaint, must refer to what the host or hotel actually wrote. Machine translation is how a "non-refundable deposit" becomes a "deposit" in one language, and complaints rise in one market only; that is why policies are rendered, not translated, and why complaints are monitored per language.

{id: content-and-media--property-and-room-mapping}
## Property and Room Mapping

**Content mapping** is the stays version of entity resolution, and an OTA and business-to-business (B2B) problem. The same hotel reaches distribution through its own extranet, channel managers, chain CRS content, several bedbanks and GDS aggregator content. Amadeus, a GDS, markets access to "+1M properties, including content from top regional and global aggregators" ([Amadeus aggregator content](https://amadeus.com/documents/en/hospitality/sales-sheet/amadeus-hotels-aggregator-content.pdf), undated, live October 2026). Sabre's content service, announced in 2017, displayed the same hotel from different sources side by side because inclusions differ by source ([PhocusWire](https://www.phocuswire.com/Sabre-Corp-to-integrate-multisource-hotel-content-into-GDS), 2017; the partner list has changed since). Trip.com Group's annual report for 2025 names "a hotel matching system" as part of its accommodation search technology, without describing it ([Trip.com Group Form 20-F](https://www.sec.gov/Archives/edgar/data/1269238/000119312526183379/d27369d20f.htm), 2026).

The mapping vendor Gimmonix writes that suppliers "list the same hotel under different names, addresses, or details", with "Hilton Garden Inn Times Square" and "HGI NYC Times Sq." as its example, and that room matching compares "30+ attributes, including bed configuration, size, view, amenities, location, special features, and board basis" ([Gimmonix, hotel mapping](https://gimmonix.com/news/how-does-hotel-mapping-work), 2026; [Gimmonix, room mapping](https://gimmonix.com/news/room-mapping-the-process-explained), 2026). Vervotech lists the failure modes as duplicates across suppliers, supplier "ID drift", schema mismatch and room-name inconsistency ("Deluxe King" vs "King Deluxe Room" vs "DLX-K"), and describes combining deterministic rules, machine-learning models and a content operations team ([Vervotech, hotel mapping](https://www.vervotech.com/hub/hotel-mapping/), 2026). Both vendors publish accuracy figures without a stated measurement method, so treat them as marketing claims. How Booking.com or Expedia map affiliate and wholesale supply internally is not public, and this chapter does not describe it.

{id: content-and-media--the-mapping-pipeline}
### The mapping pipeline

Figure 3 shows the pipeline Corvane built, following the entity-resolution structure of LISTED's [One Property, Three Listings: Duplicates and Entity Resolution](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/entity-resolution.html).

![A supplier file normalized and scored, split by thresholds into auto-match, human review or new property, recorded in a mapping registry, then room-mapped before it becomes sellable.](stays-marketplace-architecture/posts/07-content-and-media/assets/images/07-content-and-media/07-property-then-room-mapping.jpeg)

**Figure 3:** *Property mapping, then room mapping. Thresholds send uncertain pairs to people, the registry keeps stable identifiers and lineage, and a supplier room is sellable only after it is mapped to a canonical room type.*

**Normalization** removes the cheap differences: transliteration and diacritics ("Atlântico" and "Atlantico"), abbreviations ("HGI", "Htl", "Apts"), chain and brand prefixes, phone formats, and address parsing into street, number and postal code. Coordinates need a sanity check, because supplier coordinates are often the city center or a geocoder's guess.

**Blocking** limits comparisons to plausible pairs: records in the same or a neighboring geographic cell that share at least one rare name token. Without blocking, comparing 41,000 records with 640,000 is 26 billion pairs.

**Pairwise scoring** combines name similarity, distance, address and phone agreement, property type, star rating, room count, and photo similarity from perceptual hashes. A model trained on reviewed pairs works better than hand-tuned weights once a few thousand labeled pairs exist. Two features are stays-specific: **property type disagreement** (a hotel and an apartment building at the same address are a common false merge) and **chain codes**, which are strong evidence when present and misleading when a supplier reuses them.

**Thresholds** turn scores into three outcomes: automatic match, human review or new property. They are a business decision, trading review cost against missed matches and false merges, and they should be set per region and property type from a labeled sample, not once globally: a threshold tuned for one region can merge a resort's similar room names wrongly in another.

**The mapping registry** stores every supplier identifier with the canonical property identifier it maps to, the score, the decision (automatic or by whom), the date and the lineage. Canonical identifiers never change and are never reused; when two canonical properties turn out to be one, the registry records a merge and keeps the old identifier as an alias. A spreadsheet or the search indexer cannot do this, and when a supplier re-issues its codes (ID drift), every mapping kept there breaks at once. Gimmonix advertises IDs that "never change and never get recycled/renamed" ([Gimmonix, mapping](https://gimmonix.com/mapping-works/), 2026), which is the right property regardless of who builds the registry.

{id: content-and-media--room-mapping-is-harder-than-property-mapping}
### Room mapping is harder than property mapping

Property mapping answers "is this the same building". Room mapping answers "will the guest get the room they paid for". A supplier room string combines the room category, bed type, view, occupancy and often the board basis (room only, breakfast included) and rate conditions. Room mapping therefore splits each supplier room into **attributes of the room** (category, beds, size, view) and **attributes of the offer** (board basis, refundability), maps the first to a canonical room type and passes the second to the offer as rate conditions. [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) owns that split on the rate side.

Two rules keep room mapping safe:

- **Unmapped means unsellable.** A supplier room that cannot be mapped to a canonical room type is not sold under a guessed name; guests cannot compare it and support cannot handle it.
- **Mapping to a "better" room is a false merge.** If "DLX DBL CITY VW" is mapped to the hotel's "Superior Double with River View", the guest who booked a river view arrives to a city view. Map to the more generic room type when attributes are uncertain, and record the uncertainty.

{id: content-and-media--in-practice-mapping-brightwell-s-41-000-properties}
## In Practice: Mapping Brightwell's 41,000 Properties

Corvane built **Concord**, a mapping service on Roomstead's AWS estate, between June and September 2027. Aisha's supply team owned its decisions; Kenji Arai's data and ML platform team built the scoring model; a content operations team of **14** reviewers in Lisbon handled the queue. The numbers below are Corvane's (fictional) results.

**Property mapping.** After normalization and blocking, the 41,000 Brightwell properties produced about **190,000** candidate pairs. The first scoring model was trained on **6,000** pairs labeled by the reviewers and evaluated on a separate random sample of **1,500**.

| Outcome | Properties | Share | What happened next |
| --- | --- | --- | --- |
| Auto-matched (score ≥ 0.95) | 27,900 | 68% | Linked to an existing Roomstead property |
| Review queue (0.75–0.95) | 6,150 | 15% | 4,300 confirmed as matches, 1,850 judged distinct |
| No candidate above 0.75 | 6,560 | 16% | Created as new Roomstead properties |
| Rejected | 390 | 1% | Closed, invalid coordinates or duplicated inside Brightwell's own file |
| **Total** | **41,000** | **100%** | **32,200 matched, 8,410 new, 390 rejected** |

The real number of new hotels was **8,410**, mostly in Asia-Pacific and Latin America. The 32,200 matched properties gained Brightwell rates, which sometimes filled dates that hotels had closed on direct connections: a different business case, more offers per property rather than more properties.

![A stack of 41,000 property cards sorted by a matching machine into a large pile of 32,200 already sold and a small pile of 8,410 new.](stays-marketplace-architecture/posts/07-content-and-media/assets/images/07-content-and-media/07-41000-mostly-known.jpeg)

**Figure 4:** *Brightwell's 41,000 new properties were mostly hotels Roomstead already sold: mapping found 8,410 new ones and Brightwell rates for 32,200 existing ones.*

The reviewers cleared about **450** pairs a day, so the queue took about 14 working days, and their decisions became training data for the next model.

**Measured accuracy.** On the evaluation sample, the auto-match band showed **0.4%** false merges and the "no candidate" band hid **3%** missed matches: about **110** false merges and **200** duplicates still in the catalog at launch. Concord accepted this with two safety nets:

1. **A post-launch duplicate sweep** runs nightly over all Roomstead properties, not only Brightwell's, and sends high-scoring pairs to review. It caught 140 duplicates in its first month, including 23 that predated the Brightwell deal.
2. **Booking-time protection.** For the first 90 days, every Brightwell-sourced reservation on an auto-matched property triggered a confirmation check with Brightwell before the guest's confirmation email, so a false merge would be caught before the guest traveled. For these bookings Corvane Payments collects from the guest and settles with Brightwell, not with the hotel; [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models) covers that money flow.

**The Porto pair.** "Hotel Atlântico" and "Atlântico Apartments" scored 0.91 and went to review, where a reviewer separated them because the property types differed and the photos did not match. Property type became a hard rule in the review guidelines.

**Room mapping.** The 32,200 matched properties carried **412,000** Brightwell room-and-board combinations. Concord split each into room attributes and offer attributes. **74%** mapped automatically to an existing Roomstead room type, **19%** went to review and **7%** stayed unmapped and were never sold. The unmapped share was concentrated in large resorts with many room categories that Brightwell described differently from the hotels' own content, where a wrong mapping would have cost most.

**Content precedence.** For the 32,200 matched properties, Brightwell content was allowed to fill empty fields only. It added photos to about 3,100 properties that had fewer than 10, after the media pipeline had checked them for duplicates and watermarks. For the 8,410 new properties, Brightwell content was the only content, so their content scores started low and the partner-acquisition team got them as candidates for direct contracts; Corvane's 2028 plan counts how many sign and replace wholesale content with their own.

**What it bought.** Concord took four engineers about four months, plus the reviewers. Mariana kept it beyond the Brightwell deal because the nightly sweep found duplicates unrelated to wholesale and every future supply source would need it.

{id: content-and-media--content-scoring-at-roomstead-and-nookaway}
## Content Scoring at Roomstead and Nookaway

Both brands score content, but they score different things, because the authors differ.

| Component | Roomstead (property) | Nookaway (listing) |
| --- | --- | --- |
| Completeness | Required fields per property type; facilities; room-type details; check-in times | Sleeping arrangements, amenities, house rules, arrival guide, location description |
| Photos | Count per room type; resolution; room-level galleries populated | At least one photo per bedroom and bathroom; cover photo quality |
| Consistency | Free-text policy statements that conflict with structured policies; room counts vs photos | Bedrooms claimed vs photos; amenities claimed vs photos; registration number present where required |
| Freshness | Months since last description or photo update | Photos older than the last major edit; seasonal amenities |
| Translation | Coverage of the 41 site languages for free text | Original language recorded; translation available |
| Evidence | Not usually required | Accessibility features with photos; verified registration number |

Each component is shown to the partner or host with the action that improves it. The scores feed ranking only as tested features, not fixed boosts; [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) owns that decision. The photo component counts **distinct rooms covered**, not photos, so uploading more photos of the same room does not raise the score.

{id: content-and-media--ai-generated-descriptions}
## AI-Generated Descriptions

Booking.com announced in October 2024 a **Property Q&A** feature that answers questions from "listing details, reviews and photos" ([Booking Holdings press release](https://www.bookingholdings.com/press-releases/booking-com-enhances-travel-planning-with-new-ai-powered-features-for-easier-smarter-decisions/), 2024). In October 2026 it described an agent platform whose use cases include "automated property descriptions" ([Booking.com, AgentHub](https://booking.ai/introducing-agenthub-booking-com-platform-for-modular-travel-ai-agents-68bc521a0f50), 2026). As described in 2022, Airbnb's categories were built by machine learning over listing titles, descriptions, photo captions, host data and guest reviews, and then checked by a curation team ([Airbnb 2022 Summer Release](https://news.airbnb.com/2022-summer-release/), 2022).

A generated description is still a description the marketplace publishes, so it carries the same legal exposure as a human one. My rules for it:

- **Generate from structured facts, not from other text.** Every amenity, distance and policy the output mentions must exist in the structured input. A sentence about "a short walk to the beach" needs a distance in the data.
- **Never generate policies, fees or legal statements.** Those are rendered.
- **Mark provenance.** The store records the model version and the input version, and the partner or host approves the text before it replaces their own. For hosts, the host's voice is part of what sells the home; a generated draft is an offer, not a replacement.
- **Regenerate on change.** When a structured fact changes (the pool closes for renovation), provenance finds every generated text that used it, and those texts are invalidated.

[AI Across the Stay: Agents, Assistants and Automation](#ai-in-travel-stays) covers AI assistants, evaluation and liability more broadly.

{id: content-and-media--trade-offs}
## Trade-offs

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| Content model | Adopt OpenTravel codes as the internal model | Own an internal model, with adapters | A connectivity hub whose product is translating between channels | Any marketplace that competes on filters, comparison and regulatory display |
| Field ownership | Last writer wins | Per-field precedence rules with provenance | One source per property, as for a small host with no software | Several sources per property, as for any connected hotel |
| Policies | Free-text policy fields | Structured policies rendered per language | Never, for anything a guest can be charged for | Always for cancellation, fees, deposits and rules |
| Mapping | Buy a mapping vendor's IDs | Build a mapping service | Wholesale is a small, stable share of supply and the vendor's coverage fits | Mapping decisions drive search deduplication, support and money at scale, or the same service will also handle cross-brand duplicates |
| Mapping thresholds | Aggressive auto-matching | Conservative auto-matching with review | Low-value supply where duplicates cost little | Supply where a false merge sends a guest to the wrong hotel |
| Translation | Translate everything at write time | Translate on first read, then cache | High-traffic languages and frequently viewed properties | Long-tail languages and rarely viewed listings |
| Photo classification | Block publication on disagreement | Create partner tasks and lower the score | Fake-listing signals for homes | Ordinary quality problems |
| Generated descriptions | Publish automatically | Require partner or host approval | Missing descriptions for wholesale-only properties, with clear labeling | Any property or listing with an active author |

A mapping vendor's identifiers are a good **input**: they make blocking cheap and give a second opinion. They are a poor **system of record** for an OTA at scale, because the decisions that follow from a mapping (which offers compete on one page, which reviews belong together, which hotel a support agent calls) are core to the marketplace, which must be able to correct a mapping in minutes, not wait for the vendor's next daily file.

{id: content-and-media--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (Roomstead) | Hosted-stays marketplace (Nookaway) |
| --- | --- | --- |
| Who writes content | Hotel staff, PMS and CRS systems, channel managers, wholesalers, GDS content teams | The host in the listing editor, or a professional manager's PMS through "sync everything" |
| Sources per item | Several, competing for the same fields | Usually one; two when software and host both edit |
| Content model | Property, room types and facilities, standardized codes, star rating | One listing: sleeping arrangements, amenities, house rules, arrival guide, the host |
| Change rate | Low for descriptions, bursty for photos and rooms | High: photos, rules, prices and registration details change often. Expedia's Rapid guidance recommends refreshing Vrbo content at least weekly because it "changes more often than hotel content" |
| Photos | Professional, shared across suppliers, per room type | Taken by the host, unique, per room of the home; copied photos are a fake-listing signal |
| Mapping problem | Same hotel from many suppliers: entity resolution is a core service | Same home on several marketplaces (legitimate) or copied onto one (fraud); a trust problem more than a mapping one |
| Main failure modes | The Same Hotel Twice; wrong room mapped; free-text policies contradicting rate plans | Listing not as described; inflated bedroom counts; missing or invalid registration number; The Hotel-Shaped Home when homes are forced into room-type templates |
| Regulation reaching content | Consumer law on misleading information and price display | The same, plus short-term-rental (STR) registration numbers displayed per unit and trader/non-trader labeling |
| What can be shared | Media pipeline (including the perceptual-hash index), translation service, policy rendering from the group cancellation-policy engine, content events, mapping engine | Same |

Booking.com shows that the categories blur. It models a holiday home as a room type with sub-rooms (bedroom, living room, bathroom) and requires a kitchen or kitchenette before an apartment-type property can be bookable ([Booking.com, managing room types](https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-room-types.md), undated, live October 2026). That works for a hotel-first platform, but every home-specific idea (the host, the arrival guide, the house rules prose) has to be bolted onto a hotel model.

My judgement for Corvane: **share the machinery, not the content model**. The media pipeline, the translation service, the policy-rendering templates, the content-change events and the perceptual-hash index are the same problem in both marketplaces and should be one group service each. The mapping engine should also be shared, because the professional managers who sell the same apartments on Roomstead and Nookaway create a cross-brand duplicate problem that neither brand can see alone. What a hotel page and a home page say should stay brand-specific, consistent with One Stay's decision not to share supply models.

{id: content-and-media--failure-modes}
## Failure Modes

- **The extranet that keeps reverting** — see Source adapters, under Architecture.
- **Free-text policies** contradicting structured ones — see Policies and fees: render, do not write.
- **Machine-translated terms** — see Translation.
- **Aggressive auto-matching** with a threshold tuned for another region — see Thresholds in The mapping pipeline; evaluate on a labeled sample before each launch.
- **Mapping without a registry**, broken by supplier ID drift — see The mapping registry.
- **A complaint about a description that no longer exists** — see versioned snapshots in The canonical content store.

{id: content-and-media--the-chief-architect-s-view}
## The Chief Architect's View

**Decide who owns each kind of field.** Descriptions and photos belong to supply product teams. Policies and fees belong to the team that owns the money path, which renders them as content. Registration numbers and trader status belong to regulatory compliance, with validation rules the content store enforces. Accessibility claims belong to whoever runs the verification workflow. Write this down as a field ownership matrix; it settles most arguments before they start.

**Give each shared content service one owning team.** The March 2027 capability map already listed the media pipeline and translation as shared engines; the December 2027 capability map v2 adopted the other three (policy rendering, the perceptual-hash index and the mapping engine) without adding new services. The perceptual-hash index became part of the media pipeline. Policy text is rendered from Clause, the group changes-and-cancellations engine, and the display policy service. Concord's matching engine became a group engine from 2028, still run by Roomstead supply with the model from Kenji Arai's team, while the bedbank room-mapping workflow stays with Roomstead ([One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces)).

**Treat mapping as a model with an owner.** Concord makes decisions that send guests to buildings. It needs a named owner, a labeled evaluation set refreshed every quarter, published precision and recall per region, and a rollback path for a bad threshold, as [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform) asks of any consequential model. That prevents **The Unwatched Model** as much as **The Same Hotel Twice**.

**Watch three numbers.** The share of reservations with a "not as described" complaint, per property type and source. The duplicate rate found by the nightly sweep. The share of properties whose free-text fields contain policy statements that conflict with structured policies. A dashboard that shows only content scores measures effort, not outcomes.

{id: content-and-media--questions-to-ask}
## Questions to Ask

1. For any field on the property page, can we show which source wrote the current value, when, and which precedence rule allowed it?
2. Is every cancellation, fee and deposit statement a guest can read rendered from the same structured object that checkout and refunds use?
3. Can support retrieve the exact description and policies a guest saw when they booked?
4. When a new supply feed arrives, what share of its properties will be duplicates, and how was that number measured?
5. What are the precision and recall of property and room mapping per region, who owns them, and when was the evaluation set last refreshed?
6. What happens to a supplier room that cannot be mapped? Is it sold under a guessed name?
7. Which content checks block publication, which create partner or host tasks, and who decided the split?
8. Are structured terms ever machine-translated? How do we detect a mistranslated policy in one language?
9. Does the content score reward accuracy and coverage, or volume? Which outcome does it predict?
10. If a generated description mentions an amenity, can we trace it to a structured fact, and what invalidates the text when the fact changes?

{id: content-and-media--from-description-to-connection}
## From Description to Connection

Content describes what a guest can book; it does not say whether that room is free next Tuesday or what it costs. For most hotels, that information arrives through the same systems that send content, but as hundreds of millions of rate and availability messages a day instead of a few content edits. The next chapter, [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers), follows those messages from the hotel's systems into Roomstead, through Corvane Connect and the morning a €12 rate reached Hotel Miradouro's guests.

{id: content-and-media--sources-and-evidence}
## Sources and Evidence

{id: content-and-media--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Categorizing Listing Photos at Airbnb](https://medium.com/airbnb-engineering/categorizing-listing-photos-at-airbnb-f9483f3ab7e3) — Shijing Yao, Qiang Zhu and Phillippe Siclait, Airbnb Engineering, 2018. Room-type photo classification, caption-derived labels, golden-set evaluation, precision and recall targets, uses on both sides.
- [Amenity Detection and Beyond: New Frontiers of Computer Vision at Airbnb](https://medium.com/airbnb-engineering/amenity-detection-and-beyond-new-frontiers-of-computer-vision-at-airbnb-144a4441b72e) — Shijing Yao, Dapeng Li and Shawn Chen, Airbnb Engineering, 2019. Detecting amenities in listing photos.
- [Airbnb 2021 Winter Release](https://news.airbnb.com/2021-winter-release/) — Airbnb, 2021. Translation Engine (over 60 languages, commissioned evaluation); accessibility review with photo evidence (100,000 features, 25,000 homes).
- [Airbnb 2022 Summer Release](https://news.airbnb.com/2022-summer-release/) — Airbnb, 2022. Categories built by machine learning over titles, descriptions, photo captions, host data and reviews, with human curation.
- [Airbnb 2023 Winter Release](https://news.airbnb.com/en-uk/airbnb-2023-winter-release/) — Airbnb, 2023. Listing editor, "up to 20% more bookings" claim, AI-powered photo tour.
- [What are the ways I can sync listings through my API-connected software?](https://www.airbnb.com/help/article/2348/what-are-the-ways-i-can-sync-listings-through-my-api-connected-software) — Airbnb Help Center, n.d. (live October 2026). "Sync everything" vs "Sync pricing and availability".
- [Booking.com enhances travel planning with new AI-powered features](https://www.bookingholdings.com/press-releases/booking-com-enhances-travel-planning-with-new-ai-powered-features-for-easier-smarter-decisions/) — Booking Holdings, 2024. Property Q&A from listing details, reviews and photos.
- [Introducing AgentHub](https://booking.ai/introducing-agenthub-booking-com-platform-for-modular-travel-ai-agents-68bc521a0f50) — Booking.com, 2026. Agent platform with automated property descriptions as a use case.
- [How we work](https://www.booking.com/content/how_we_work.html) — Booking.com, updated 2025. Photo quality among the inputs to default-sort performance.
- [Form 20-F for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1269238/000119312526183379/d27369d20f.htm) — Trip.com Group, 2026. "A hotel matching system" in accommodation search technology.

{id: content-and-media--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Connectivity API documentation](https://developers.booking.com/connectivity/docs) — Booking.com, n.d. (live October 2026). Content API modules; OpenTravel 2003B and B.XML.
- [Understanding the Photo API](https://developers.booking.com/connectivity/docs/photo-api/understanding-the-photo-api) — Booking.com, n.d. (live October 2026). Room-level galleries, 299-photo limit, smart ordering, asynchronous status including duplicates, no overlay.
- [Managing room types](https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-room-types.md) and [Managing room amenities](https://developers.booking.com/connectivity/docs/tsk-modify-room-amenities.md) — Booking.com, n.d. (live October 2026). Homes as room types with sub-rooms; kitchen requirement; sunset of `OTA_HotelInvNotif` for Home providers on 31 December 2026.
- [Room amenity (RMA) codes](https://developers.booking.com/connectivity/docs/codes-rma) — Booking.com, n.d. (fetched October 2026). Internal normalization of synonymous amenity codes.
- [Rapid content API](https://developers.expediagroup.com/rapid/lodging/content/about-content-api) and [Vrbo integration guide](https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-integration-guide) — Expedia Group, n.d. (fetched October 2026). Catalog file for mapping suppliers, daily content refresh, weekly Vrbo refresh, structured house rules.
- [AlpineBits HotelData](https://www.alpinebits.org/hotel-data/) — AlpineBits Alliance, n.d. (release 2024-10). Regional OpenTravel profile carrying descriptive content and images.
- [Amadeus Hotels aggregator content](https://amadeus.com/documents/en/hospitality/sales-sheet/amadeus-hotels-aggregator-content.pdf) — Amadeus, n.d. GDS hotel content including aggregator content.
- [Regulation (EU) 2024/1028 on short-term accommodation rental data](http://publications.europa.eu/resource/celex/32024R1028) — EU, 2024 (applies from 20 May 2026). Registration number before offering and clear display (Article 7).
- [Directive 2005/29/EC on unfair commercial practices](http://publications.europa.eu/resource/celex/32005L0029) — EU, 2005. Misleading information about main characteristics (Article 6).
- [Coordinated action on accommodation booking](https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/accommodation-booking_en) — European Commission, 2018–2020. Airbnb and Booking.com commitments on price display and trader labeling.

{id: content-and-media--research-and-practitioner-sources}
### Research and practitioner sources

- [Hotel tech specifications: HTNG and OpenTravel](https://www.altexsoft.com/blog/hotel-tech-specifications-htng-opentravel/) — AltexSoft, 2020. HTNG Distribution Content Management; relationship to OpenTravel.
- [Airbnb Translation Engine applies machine translation to UGC](https://slator.com/airbnb-translation-engine-applies-machine-translation-to-ugc/) — Slator, 2021. Reported use of ModernMT.
- [Sabre to integrate multisource hotel content into GDS](https://www.phocuswire.com/Sabre-Corp-to-integrate-multisource-hotel-content-into-GDS) — PhocusWire, 2017. Side-by-side display of the same hotel from several sources.
- [How does hotel mapping work](https://gimmonix.com/news/how-does-hotel-mapping-work), [Room mapping: the process explained](https://gimmonix.com/news/room-mapping-the-process-explained) and [Mapping](https://gimmonix.com/mapping-works/) — Gimmonix, 2026. Name and address variation, 30+ room attributes, stable IDs (vendor claims).
- [Hotel mapping](https://www.vervotech.com/hub/hotel-mapping/) — Vervotech, 2026. Mapping failure modes and hybrid rules, models and operations (vendor claims).

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
