{mainmatter}

{class: part, id: part-1}
# Part I — MARKETPLACE: The Business Behind the Listings

![Part I — MARKETPLACE: The Business Behind the Listings — logo](listing-systems-architecture/posts/part-1-intro/assets/images/part-1-intro/logo.jpeg)

> **IN THIS PART, YOU WILL:** Describe a listing marketplace as a business before describing it as software: its model, its liquidity, its history, its capabilities, its bounded contexts and the physics of each vertical it serves.

> **WHY THE BUSINESS CARES:** The model decides what the marketplace can charge for, which risks it carries and which regulators take an interest. Liquidity decides whether professionals renew and buyers come back. Both are business facts that the systems either serve or work against.

> **WHY ARCHITECTS SHOULD CARE:** Every boundary, shared platform and non-functional requirement later in this book is justified by something in this part. Without it, platform debates become contests between system owners.

> **KEY POINTS:**
>
> * **The model is an architecture decision, made per country and category.** Where the marketplace's job ends (contact, lead, payment or delivery) decides identity depth, payments, trust and data. One brand usually holds several models, so the model belongs in configuration, not in code.
> * **Liquidity is the product, and its metrics are the requirements.** Network effects work per place and category. Time to first contact, sell-through and ghost rates become publication, alert, removal and capacity targets.
> * **Map what the marketplace does before deciding what to share.** Capabilities, value streams, bounded contexts and vertical profiles turn "should this be one platform?" into a decision that can be reviewed: share the machinery, let each vertical own its content.

> **[FAILURE PATTERNS THIS PART ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Vanity Liquidity** — Defines success as matches per cell, not listings and visits.
> * **The Forced Fit** — Shows why a platform built around one model or vertical fails the others.
> * **Deal-Shaped Architecture** — Gives a group the capability vocabulary to see what it pays for several times.

This book starts with the business, not the systems, because **in a listing marketplace the business model decides the architecture** more directly than in most industries. A classifieds site whose job ends at the contact, a portal that sells qualified leads and a marketplace that holds buyers' money need different identity, trust, payment and data systems, even when their search pages look alike.

Sharing decisions need three pieces of business knowledge, and the part supplies them in order. First, know what kind of marketplace you run and what it sells: **liquidity**, the likelihood that a listing finds a buyer in a given place and category fast enough that both come back. Second, know how the industry got here, because today's portfolios carry the systems of every earlier wave. Third, describe the marketplace in terms that outlive systems and reorganizations, so that sharing decisions rest on evidence.

![Systems modules standing on a foundation of six business blocks: model, liquidity, history, capabilities, boundaries and verticals.](listing-systems-architecture/posts/part-1-intro/assets/images/part-1-intro/business-foundation-under-systems.jpeg)

**Figure 1:** *Part I lays the foundation first: the marketplace model, liquidity, history, capabilities, boundaries and vertical physics that every later system decision rests on.*

{id: part-1--chapters-in-this-part}
## Chapters in this part

| Chapter | The question it answers | Read it when… |
| --- | --- | --- |
| [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy) | What kind of marketplace is this, and why does the answer decide the architecture? | A brand plans to add payments, leads or guarantees. |
| [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) | What does a marketplace sell, and how do we know whether it works? | Dashboards count listings and visits, or nobody can say why a latency target exists. |
| [From Newspaper Columns to Portfolios: How the Classifieds Industry Evolved](#industry-evolution) | How did today's marketplace groups form, and what did each of the five waves, from print columns to private-equity break-ups, leave in their systems? | You inherit a portfolio of local stacks, or the owner may sell a brand. |
| [Map What the Marketplace Does Before What Runs It](#business-capabilities) | How do we describe what the marketplace does independently of its systems? | You must find what the group pays for several times. |
| [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) | Where do the domain boundaries go, and who owns the listing's truth? | Every change to the listing table needs a cross-team meeting. |
| [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) | What genuinely differs between verticals, and what can be shared? | A program proposes one platform for goods, cars, homes and jobs. |

{id: part-1--how-this-part-connects}
## How this part connects

This part supplies the vocabulary the rest of the book uses: marketplace profile, liquidity cell, capability, bounded context and vertical requirement profile. It builds on the Preface's failure patterns ([Unlisted: Fifteen Ways Listing Systems Go Wrong](#where-listing-systems-go-wrong)) and running example ([Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). [Part II — LISTING: Modeling the Thing Being Sold](#part-2) designs the listing domain model inside the boundaries drawn here. Later parts justify their freshness, latency and sharing decisions by pointing back to this part's liquidity metrics and share test.

{id: part-1--the-veldmark-thread}
## The Veldmark thread

Veldmark, the fictional marketplace group this book follows, approved its €140 million Common Ground program in January 2027. Ingrid Halvorsen joined as Group Chief Architect in February and spent her first months testing it against the business. In this part her team:

- Classifies the group into **20 marketplace profiles** (brand × country × category group) and resolves the Poland overlap between Tradeyard's cars section and Motorvane.
- Measures liquidity per cell (region × leaf category): **38%** of Tradeyard Netherlands' cells are liquid, against **11%** in Portugal. From then on, every new latency or freshness objective must name the liquidity metric it protects.
- Reads the group's history (Tradeyard launched in 2004, Motorvane in 2008, a Polish purchase in 2012, three acquisitions in 2023–2025) as sediment left by each wave, and records in March 2027 that any brand may be sold within five years, so every shared platform needs a documented exit path.
- Presents a capability map on 31 March 2027 with **five overlaps**, one commercial overlap and one deliberate duplicate.
- Gets a shared-versus-specific table ratified in April and a context map of **19 bounded contexts** approved by the architecture advice forum in May 2027.

Begin with [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy).
