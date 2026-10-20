{class: part, id: part-9}
# Part IX — PRACTICE: How Others Built It

![Part IX — PRACTICE: How Others Built It — logo](listing-systems-architecture/posts/part-9-intro/assets/images/part-9-intro/logo.jpeg)

> **IN THIS PART, YOU WILL:** Test the book's patterns against six public cases: Adevinta, OLX Group, eBay Classifieds Group, AVIV Group, the property portals Zillow, Rightmove, Idealista and REA, and the automotive marketplaces mobile.de, Auto Trader and AutoScout24.

> **WHY THE BUSINESS CARES:** These groups bought, merged, shared, sold and retreated in public. Their records show what platform decisions were worth when the capital strategy changed, and which adjacent bets cost more than they earned.

> **WHY ARCHITECTS SHOULD CARE:** Parts I–VIII argue from principles and a fictional group. Here the argument meets evidence that the author did not design, including evidence that cuts against it.

> **KEY POINTS:**
>
> * **Share the uniform layers, and treat product convergence as a separate, riskier bet.** Infrastructure, data, experimentation and narrow machine-learning services were shared with documented success. Adevinta's 2023 plan to turn two generalist platforms into one was reversed by 2025, and AVIV's 2021 goal of "a European real estate marketplace", whose scope was never published, gave way to local autonomy.
> * **Every shared dependency must survive a change of owner.** eBay's 2020–2021 sale and Adevinta's 2025 break-up turned shared platforms into transitional-service terms and separation costs. Separability is a design requirement, not a contingency plan.
> * **Contracts and models carry the vertical lessons.** Automotive leaders publish their dealer-feed contracts, property portals depend on licensed supply, and Zillow showed in 2021 what happens when an estimate built to inform is used to commit capital.

> **[FAILURE PATTERNS THIS PART ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Acquisition Archipelago** — Four of the six cases are portfolios assembled by acquisition, and the record shows what each kept, shared and paid for.
> * **The Platform Mandate** — Adevinta's planned product-platform convergence and AVIV's 2021 integration goal both gave way to local autonomy with selected group functions.
> * **The Unwatched Model** — Zillow Offers and automotive price ratings show models making consequential decisions about money and exposure.

[Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution) closed the argument of this book. Part IX asks **whether it survives contact with what real groups did**. The cases are not company profiles. Each asks what was shared, at which layer, and what it cost when the strategy changed.

{id: part-9--how-to-read-the-cases}
## How to read the cases

Part IX follows stricter evidence rules than Parts I–VIII: every statement is one of three kinds.

| Kind of statement | How you recognize it |
| --- | --- |
| **Documented fact** | Source and publication year in the sentence or the timeline. Old sources describe systems that may since have been replaced: "true at the date of its source, and no later". |
| **The author's interpretation** | Marked "my reading", or placed in the Chief Architect's view. |
| **Reference-architecture inference** | Only in a callout labeled `INFERENCE, NOT DOCUMENTED`. It describes how a group like this *could* be built, never how it *is* built. |

The evidence is uneven, and each case says where it stops. Adevinta published a great deal, eBay Classifieds almost nothing as a group, and AVIV no engineering material at all. **The depth of each section follows the evidence, not the importance of the company.**

Veldmark appears only in each case's final comparison. That keeps the fiction from being read as a disguised real group, and the real record from being stretched to fit the fiction.

{id: part-9--chapters-in-this-part}
## Chapters in this part

| Chapter | The question it answers | Read it when… |
| --- | --- | --- |
| [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) | What does a full swing from federation to shared platform and back teach? | You are deciding what a group platform should share. |
| [OLX Group: Regional Platforms, Verticalization and Retreat](#case-olx) | What happens to a platform as a portfolio shrinks to its local leaders? | You are weighing an inventory or transactional bet. |
| [eBay Classifieds Group: Shared Platforms, Local Brands and a Sale](#case-ebay-classifieds) | How thin can a shared layer be, and what does a sale expose? | A brand may be sold, or a parent may leave. |
| [AVIV Group: Building a European Real-Estate Platform from Acquisitions](#case-aviv) | How much of a property portal can be shared across countries? | You are integrating acquired national portals. |
| [Zillow, Rightmove, Idealista and REA: What Property Portals Teach](#case-property-portals) | What do licensed supply, durable properties and valuation models demand? | Your models start to price, not describe. |
| [mobile.de, Auto Trader and AutoScout24: Lessons from Automotive Marketplaces](#case-automotive) | What do dealer-fed listing systems reveal through their public APIs? | Most of your supply arrives through vendor feeds. |

{id: part-9--the-cases-side-by-side}
## The cases side by side

| Company | Platform strategy | What the public record shows | Lesson |
| --- | --- | --- | --- |
| Adevinta | Selective centralization (2019), product convergence (2023), decentralization (2025) | Wins in uniform layers; no public source shows the 2023 convergence completed before the reversal | Share uniform layers first; let tenants leave |
| OLX Group | Roll-up and rebrand, then retreat to a European core | From 45 markets (2018) to seven (FY to March 2026); OLX Autos exited from 2023 | Liquidity is local; build adjacent bets to be switched off |
| eBay Classifieds | Federation of national leaders with a thin shared layer | Shared search choice migrated brand by brand; sale completed June 2021 with transitional services | A sale turns shared dependencies into contract terms |
| AVIV Group | Acquired portals, shared valuation and professional offer | 2021 integration intent of unpublished scope; by December 2025, local autonomy with group functions where they "create clear advantages" | In real estate, stop sharing well short of the product |
| Property portals | Four economic engines (per advertiser, per listing, per lead) | Zillow Offers wound down in November 2021; supply licensed from MLSs and agents | Govern models by decision tier; carry license terms as data |
| Automotive | Dealer-fed platforms with published APIs | Feed contracts, change feeds and five-band price ratings in public | Price ratings need ranking-model governance |

![A building cross-section with solid shared lower floors, separate local product modules on top, a faded abandoned merged top floor, and one module lifted off cleanly by a crane.](listing-systems-architecture/posts/part-9-intro/assets/images/part-9-intro/shared-layers-separable-products.jpeg)

**Figure 1:** *The cases' common lesson: sharing the uniform layers held up, converging products into one was the riskier bet, and every shared dependency had to let a tenant leave when its owner changed.*

{id: part-9--how-this-part-connects}
## How this part connects

Each case links back to the chapters it tests, chiefly [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms), [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation), [Models in Production: ML Platforms and Use Cases](#ml-platform) and [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion), and ends with a verdict table. The [Field Kit: Templates for the Marketplace Architect](#toolkit) then turns the book's decisions into templates.

{id: part-9--the-veldmark-thread}
## The Veldmark thread

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), is tested here, not extended. Ingrid Halvorsen's team holds its 2027 choices against the record:

- **"share platforms, not products"** in Common Ground, with every shared capability tenant-separable from its first release;
- the **shared OpenSearch platform** for Tradeyard and Hearthly, with Motorvane on Elasticsearch until a 2029 review (14 September 2027);
- **Supply Contract v1** (September 2027): one contract and validator for the group, adapters kept brand-local;
- **"Hearthly Direct" declined** in 2027 as a commit-tier use of Valuo without validation.

By the end of Part IX you should be able to say which of the book's patterns the public record supports, which it only fails to contradict, and where it is silent. Begin with [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta).
