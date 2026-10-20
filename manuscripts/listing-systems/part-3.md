{class: part, id: part-3}
# Part III — SUPPLY: Getting Inventory In

![Part III — SUPPLY: Getting Inventory In — logo](listing-systems-architecture/posts/part-3-intro/assets/images/part-3-intro/logo.jpeg)

> **IN THIS PART, YOU WILL:** Follow supply from the moment it reaches the marketplace until it is visible everywhere, and later removed everywhere: ingestion and feed contracts, normalization and enrichment, entity resolution, publication and professional tooling.

> **WHY THE BUSINESS CARES:** In vertical marketplaces most inventory comes from professionals through machine feeds, and they pay for the leads it produces. A lost feed, a ghost listing or a lead count that does not match the dealer's CRM costs renewals, not just data quality.

> **WHY ARCHITECTS SHOULD CARE:** Supply is where outside systems write into yours. Every weakness here (an unstated contract, an unrecorded source, an unregistered copy) becomes a search, trust or billing problem downstream.

> **KEY POINTS:**
>
> * **Many doors, one write path, one contract per door.** Forms, APIs and feeds should end in the same idempotent listing command. Each channel needs a contract that says what absence means, who owns each field and how both sides reconcile, because partner state and platform state will drift.
> * **Keep what was said, record where every value came from.** Normalize to canonical values next to the original, attach provenance to every value, and run enrichment as a versioned, replayable pipeline. Resolve duplicates to entities that outlive their listings, with cluster identifiers governed as a product contract.
> * **Publishing is a decision followed by a propagation, and removal matters more.** A short synchronous path decides whether a listing may go live. Events carry it everywhere within a budget, and the same mechanism, audited per consumer, takes it down again.

> **[FAILURE PATTERNS THIS PART ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Feed Roulette** — Gives every channel a contract, validation, error feedback and reconciliation.
> * **The Duplicate Echo** — Separates abuse from legitimate multi-listing and clusters the second for presentation.
> * **Ghost Inventory** — Makes removal reach every copy, with evidence per consumer.

[Part II — LISTING: Modeling the Thing Being Sold](#part-2) modeled the listing: a small aggregate referencing governed categories, attributes, media, places and accounts. This part puts that model under load. **Supply arrives through many doors, at different rhythms, from systems the marketplace does not control**, and each door tends to grow its own idea of what a listing is.

The argument is that supply is **one chain, not five features**. A record enters through a channel under a contract, is normalized and enriched with recorded provenance, is recognized when it describes something already known, and is published and later unpublished within a stated freshness target. The professionals who supply most of the inventory then check the result against their own systems.

![A single conveyor carries listings from phone, dealer system and agency doors through contract, provenance, matching and publication stations, with a return path for removal.](listing-systems-architecture/posts/part-3-intro/assets/images/part-3-intro/supply-as-one-chain.jpeg)

**Figure 1:** *Supply is one chain, not five features: every door feeds the same contracted path, and the same path takes listings down again.*

{id: part-3--chapters-in-this-part}
## Chapters in this part

| Chapter | The question it answers | Read it when… |
| --- | --- | --- |
| [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) | How should a marketplace accept supply from private sellers, professionals and partners at scale? | A partner's bad file can unpublish thousands of listings overnight. |
| [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) | How do you turn heterogeneous input into consistent, enriched listings? | Nobody can tell which values a seller typed and which a model inferred. |
| [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) | How do you recognize that several listings describe the same thing, and what do you do about it? | One flat appears three times, or reposts crowd out new supply. |
| [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) | What happens between "publish" and searchable, and how fast must it be? | Publication takes minutes, or sold items still appear in alerts. |
| [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) | What do professional sellers need, and how should that tooling be built? | Dealers dispute your lead counts, or the group sells software to professionals. |

{id: part-3--how-this-part-connects}
## How this part connects

This part consumes Part II's contracts. Ingestion validates against the compiled [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas), writes commands to the [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) and attaches records to [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts). The liquidity metrics of [Part I — MARKETPLACE: The Business Behind the Listings](#part-1) set its targets: time to first contact sets the publication budget, and ghost rates set the removal guarantee. [Part IV — DISCOVERY: Matching Intent to Inventory](#part-4) then reads the result: search, alerts and recommendations are only as fresh, deduplicated and trustworthy as the supply this part delivers. Trust and safety ([Part V — TRUST: Keeping the Marketplace Safe](#part-5)) owns the moderation gate inside the publication pipeline.

{id: part-3--the-veldmark-thread}
## The Veldmark thread

At Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), supply problems arrive as incidents before they arrive as designs. In this part Ingrid Halvorsen's team:

- Responds to the **8 March 2027** Motorvane incident, in which truncated snapshot files unpublished **38,400** listings, by adopting **Supply Contract v1** in September 2027: one envelope, one error catalog, mandatory mass-change guards and brand-local adapters.
- Traces the **Essen Volkswagen Golf**'s 31 decoded attributes value by value, and gives every value a recorded source.
- Clusters the **Lyon apartment**'s three agency listings into one canonical property, using only what each listing carries as published to Hearthly, never Keybridge's own data.
- Writes Tradeyard's **90-second** p95 publication target as an SLA card with a budget per stage, after finding that the 6-minute baseline ignored the 6% of listings held for human review.
- Reconciles the Golf's **23** Dealer Hub leads against the **14** in the dealer's CRM, and keeps Keybridge's cross-portal report out of Hearthly's reach.

Begin with [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion).
