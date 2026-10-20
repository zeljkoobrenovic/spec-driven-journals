{class: part, id: part-2}
# Part II — LISTING: Modeling the Thing Being Sold

![Part II — LISTING: Modeling the Thing Being Sold — logo](listing-systems-architecture/posts/part-2-intro/assets/images/part-2-intro/logo.jpeg)

> **IN THIS PART, YOU WILL:** Design the listing domain model: the listing aggregate and its lifecycle, category taxonomies, attribute schemas, media, location, and the sellers and organizations that supply listings.

> **WHY THE BUSINESS CARES:** Buyers filter on category, attributes and place before they read a title, and professional sellers are billed through the account model. Weak models mean listings nobody finds, sold items that keep drawing contacts and invoices sent to the wrong business.

> **WHY ARCHITECTS SHOULD CARE:** Search, alerts, trust, monetization, analytics, SEO and partner feeds all copy the listing. The shape chosen here decides whether those copies agree.

> **KEY POINTS:**
>
> * **The listing is a small aggregate that holds references, not a wide table.** It owns identity, invariants and a lifecycle with separate seller, platform and enforcement dimensions, and references categories, attributes, media, places and accounts by ID.
> * **Each referenced subdomain is governed, versioned reference data.** Taxonomies, attribute dictionaries, gazetteers and media assets change on their own schedules and need owners, compatibility rules and migrations, not admin screens and hard-coded IDs.
> * **Several of these models carry privacy and legal weight.** Photo metadata, a seller's precise location and trader status are personal or regulated data, so their boundaries belong in the data model, not in the user interface.

> **[FAILURE PATTERNS THIS PART ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Category Straitjacket** — Treats the category tree as versioned data, so a change is a migration, not a release.
> * **The Attribute Junkyard** — Gives every attribute one definition that forms, feeds, filters and rules compile from.
> * **Ghost Inventory** — Makes every lifecycle transition an event with a deadline, so no copy outlives the listing.

Part I drew the domain boundaries and decided who owns the listing's truth; Part II designs **the thing being sold** inside them. Most marketplaces modeled the listing once, at launch, and have extended it ever since. Fifteen years later the `ads` table has two hundred columns, category IDs live in the code, and nobody can say which copy of a listing is the true one.

This part argues that a listing is **an offer about a thing, not the thing itself**. The aggregate stays small and strict. Around it sit five subdomains, each with its own owner and rate of change: categories, attributes, media, location and the parties who list. Give each one a contract, and ingestion, search, trust and billing read the same meaning instead of guessing it.

![A small central listing card linked by dashed ID references to five owned islands: categories, attributes, media, location and accounts.](listing-systems-architecture/posts/part-2-intro/assets/images/part-2-intro/small-aggregate-five-subdomains.jpeg)

**Figure 1:** *The listing stays a small, strict aggregate; categories, attributes, media, location and accounts are separate governed subdomains it references by ID.*

{id: part-2--chapters-in-this-part}
## Chapters in this part

| Chapter | The question it answers | Read it when… |
| --- | --- | --- |
| [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) | What is a listing, what must always be true about it, and how does it change? | Your status field has twenty values, or sold listings still get contacts. |
| [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) | How do you design a category tree that can change without breaking everything? | Adding or splitting a category takes weeks and a cross-team release. |
| [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) | How should attributes be modeled so they can be validated, searched and evolved? | Filters are empty, or one fact is stored under many keys. |
| [Photos Sell: Media Pipelines for Listings](#media-pipeline) | How do you ingest, store, moderate and serve billions of images? | The media bill outgrows live listings, or stolen photos go unnoticed. |
| [Where Is It? Location, Geocoding and Privacy](#location-and-geo) | How do you model location so search, maps and privacy all work? | Distances leak addresses, or the map and the results disagree. |
| [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts) | How should you model the people and organizations that supply listings? | Agencies, dealer groups or franchises do not fit your user table. |

{id: part-2--how-this-part-connects}
## How this part connects

[Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) in Part I showed where the listing means different things. This part designs the Supply-side core those meanings depend on. [Part III — SUPPLY: Getting Inventory In](#part-3) puts the model to work: forms and feeds, enrichment, duplicates and publication. Later parts read these models as contracts. Search indexes the attribute schemas, trust and safety writes the enforcement overlay, and entitlements attach to accounts.

{id: part-2--the-veldmark-thread}
## The Veldmark thread

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), starts 2027 with four Tradeyard country trees and 3,900 attribute keys, 41% of them used on fewer than 0.1% of listings. Ingrid Halvorsen's team decides:

- a **common listing lifecycle** with an enforcement overlay owned by trust and safety, shipped in Listing event contract v1 on 1 July 2027;
- **Veldmark Place**, a gazetteer and precision-policy service (May 2027), so private sellers' precise points never reach a client;
- a **group business party registry** for verified legal-entity facts (August 2027);
- the **group taxonomy and attribute service**, live for Tradeyard in October 2027, and the **bikes split** on Monday 1 November 2027;
- a **group media decision** (November 2027), with a shared perceptual-hash index from Q1 2028.

Femke's €240 Rotterdam city bike, the Lyon apartment and Agence Rhône Habitat's fourteen branches carry the thread.

By the end of Part II you should be able to say who owns each part of a listing, how it is versioned and which systems copy it. Begin with [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate).
