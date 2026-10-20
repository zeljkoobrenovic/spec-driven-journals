{id: web-and-seo-architecture}
# 35. Found by Google: Web, App and SEO Architecture for Listings

![Found by Google: Web, App and SEO Architecture for Listings — logo](listing-systems-architecture/posts/35-web-and-seo-architecture/assets/images/35-web-and-seo-architecture/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn how search engines crawl, render and index a listing site and why that makes URLs, status codes and sitemaps part of the architecture. You will design the landing-page generator, the lifecycle rules for live, sold and removed listings, the rendering and composition model for the web, and the backends-for-frontends behind the apps. Then you will follow Tradeyard as it cuts 40 million indexed URLs down to the ones that earn traffic.

> **WHY THE BUSINESS CARES:** For a horizontal classifieds site, organic search is often the largest free acquisition channel, and it is the one the business controls least. A rendering change, a category rename or a careless expiry rule can remove a large share of that traffic in a few weeks, and recovering it takes months.

> **WHY ARCHITECTS SHOULD CARE:** Search engines are a client of the platform with their own protocol: URLs, HTTP status codes, sitemaps, structured data and response times. That client never files a bug report. It quietly crawls less, indexes less and ranks less, so its contract has to be designed and tested like any other interface.

> **KEY POINTS:**
>
> * **Landing pages, not listing pages, are the durable SEO asset.** Listings live for days; a page for "e-bikes in Utrecht" can rank for years. Generate landing pages from measured demand and live supply under explicit rules, and give everything else a `noindex`, a `404` or no URL at all.
> * **URLs, status codes and sitemaps belong to the listing lifecycle.** A sold listing that still answers `200` with "no longer available" is Ghost Inventory in Google's index. Drive canonical URLs, redirects, sitemap entries and removal signals from the same listing events that drive search and alerts.
> * **Render on the server, own pages per team, and give each client its own backend.** Server-side rendering with edge caching serves both crawlers and phones. Page-level ownership with build-time shared components has a better documented record than runtime fragment composition. Apps that ship every two weeks need a backend-for-frontend and server-driven forms, or every schema change waits for app adoption.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Ghost Inventory** — sold and expired listing pages that keep answering `200`, stay in sitemaps and keep collecting crawls put gone inventory in front of buyers through the search engine.
> * **The Category Straitjacket** — when category paths are baked into URLs with no redirect registry, every taxonomy change becomes an SEO migration that nobody dares to schedule.
> * **Vanity Liquidity** — counting indexed URLs and organic sessions, instead of contacts from organic sessions, rewards generating pages that search engines treat as low value.

Part VII designs the platform as a set of published contracts; this chapter writes the one the marketplace keeps with the outside world. Every page has two audiences. One is a person on a phone who wants a used e-bike near home. The other is a crawler that decides whether that person will ever see the page in a search result. The crawler reads the HTML, follows links, respects status codes, reads sitemaps and measures how fast the server answers. **For a business whose inventory changes by the minute, how the site talks to crawlers is a design decision with a revenue line attached.**

Most marketplaces discover this late. The web front end is built for users, SEO is treated as a set of tags added afterwards, and the first serious conversation about crawl budget happens after a redesign that cost a third of organic traffic. This chapter takes the opposite view. **SEO architecture** — in this book, the set of components and rules that decide which URLs exist, what each URL returns over its lifetime, how pages are rendered and how search engines learn about changes — is part of the customer-facing architecture from the start, alongside rendering, composition and the app backends.

The chapter builds on the two before it. The listing events of [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) drive its URLs, sitemaps and cache purges, and the index a search engine builds from Tradeyard's pages is the outermost of the read models in [System of Record and Read Models: Listing Data Management](#listing-data-management). It does not re-teach search indexing, which [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) owns. Later chapters use what it sets up: [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) governs the organic-contact metric the worked example ends on, and [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) starts Yardstick's strangler at the web layer.

{id: web-and-seo-architecture--setting-the-scene-at-veldmark-forty-million-urls-and-a-sold-bike}
## Setting the Scene at Veldmark: Forty Million URLs and a Sold Bike

It is late March 2027 at Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). Ingrid Halvorsen, the Group Chief Architect, is reviewing Tradeyard's web estate with Daan Visser, Tradeyard's engineering director, and the brand's SEO lead. Tradeyard has about **40 million** URLs in Google's index across its four country domains, and **46%** of its web sessions start from organic search. Those two numbers appear in every board pack as evidence of strength. Ingrid wants to know what is behind them.

The answer comes from a crawl audit the SEO team finished in February. Of the 40 million indexed URLs:

| URL type | Indexed URLs | Live listings or results behind them | Organic visits in the last 90 days |
| --- | --- | --- | --- |
| Live listing detail pages | 11.4M | One live listing each | 31% of organic sessions |
| Sold, expired or removed listing pages | 6.3M | None; page answers `200` with "no longer available" | 6% of organic sessions, 0.4% of organic contacts |
| Search and landing pages (category × location × filters) | 19.8M | Varies; 7.1M have fewer than three live results | 58% of organic sessions, from about 1.1M URLs |
| Seller shops, profiles, help and guides | 2.5M | — | 5% of organic sessions |

Three findings stand out. **Most organic value comes from a small set of landing pages**: about 1.1 million of 19.8 million search URLs received an organic visit in 90 days. **A sixth of the index is gone inventory**: 6.3 million pages for listings that no longer exist still return `200`. And Googlebot fetches about 14 million Tradeyard URLs a day, 41% of them parameterized facet URLs or dead listing pages, while a new Tradeyard NL listing waits a median of **2.6 days** for its first crawl. Most private goods listings are sold or withdrawn within a week, so for them that crawl comes too late to matter.

Femke's city bike shows the problem at the scale of one item. She listed it in Rotterdam for **€240** on Sunday **7 March 2027**, and it sold on Monday **8 March** for **€225**. Tradeyard marked it sold at **18:10** and removed it from search at **18:11**. Its listing page kept answering `200` with a "this ad is no longer available" banner, stayed in the listings sitemap with an unchanged `lastmod`, and was still in Google's results nine days later, where it collected 37 clicks from people who could not buy it. The alert digest assembled that evening, which still featured it when it went out the next morning, is a problem [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) owns; the search engine result is a problem this chapter owns.

At the same time, Daan's team is preparing two changes that touch the same layer. Tradeyard's search pages are rendered by Yardstick, the 2006 PHP monolith, and score poorly on mobile performance. A team has proposed rebuilding them as a client-rendered single-page application (SPA). And the taxonomy team plans to split the single bikes category into city bikes, e-bikes, cargo bikes and kids' bikes on **1 November 2027** (see [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies)), which will change thousands of landing-page URLs. Ingrid's question for the rest of the chapter: *what should the customer-facing architecture look like so that changes like these are routine instead of risky?*

{id: web-and-seo-architecture--concepts-how-a-listing-site-earns-organic-traffic}
## Concepts: How a Listing Site Earns Organic Traffic

{id: web-and-seo-architecture--crawl-render-index-rank}
### Crawl, render, index, rank

A search engine processes a site in four stages. It **crawls** URLs it discovers through links and sitemaps, **renders** the HTML (and, for JavaScript-heavy pages, executes scripts, often later), **indexes** what it decides is worth keeping, and **ranks** indexed pages against queries. Each stage filters. A URL that is never crawled cannot be indexed; a page that renders as an empty shell may be indexed without its content; an indexed page that duplicates thousands of others ranks for nothing.

Google's documentation names the sites that need to manage the first stage explicitly: "large sites (1 million+ unique pages) with content that changes moderately often (once a week)" or medium sites with "very rapidly changing content (daily)" ([Google Search Central, crawl budget, updated 2026](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget)). Every sizable classifieds site meets both conditions. The same page explains that crawl capacity falls when responses are slow or return `5xx` or `429` errors, and that soft-404 pages keep being crawled and waste budget. **Crawl budget** is therefore not a fixed allowance. It is a function of how valuable the engine believes the URLs are and how healthy the server looks while it fetches them.

{id: web-and-seo-architecture--the-page-types-of-a-listing-site}
### The page types of a listing site

Each page type of a listing site has its own lifetime and its own SEO role.

| Page type | Example | Typical lifetime | SEO role | Rendered from |
| --- | --- | --- | --- | --- |
| **Landing page** (search result page eligible for indexing) | "E-bikes in Utrecht", "Used Volkswagen Golf in Essen", "3-room apartments for sale in Lyon 7e" | Years | Main durable organic asset; matches recurring queries | The search engine, with curated copy and links |
| **Listing detail page** | One bike, one car, one apartment | Days (goods) to weeks (cars, property) | Long-tail queries; shares on social and messaging | The listing read model |
| **Faceted result page** (non-curated filter combination) | Bikes, Rotterdam, red, €100–€150, sorted by price | Seconds to days | Usually none; a crawl trap if exposed | The search engine |
| **Seller or agency page** | A dealer's stock, an agency's branch | Years | Brand and local queries | Seller profile and search |
| **Editorial and tool pages** | Buying guides, price checkers, valuation pages | Years | Informational queries; links into landing pages | Content management system (CMS) and data services |
| **Gone listing page** | A sold car, an expired ad, a removed scam | Should be short | Little, except where demand persists | Archive or nothing |

In this book a **landing page** is a search result page that the platform has deliberately made indexable: it has a canonical URL, curated title and copy, internal links, and a rule that says when it may exist. The definition matters because every faceted search page *could* be crawled, and most of them should not be. **Landing page generation** is the process that decides which category, location and attribute combinations get a canonical, indexable URL, keeps that set current as demand and supply change, and retires pages cleanly.

{id: web-and-seo-architecture--why-landing-pages-carry-the-weight}
### Why landing pages carry the weight

The landing page is the page that can accumulate links, history and ranking signals, because its URL stays stable while its contents change. Classifieds inventory is short-lived and unique: a specific bike exists on the site for a few days, while a query like "tweedehands e-bike Utrecht" exists for years. This is industry practice inferred from inventory lifetime, not documented fact; no classifieds operator in the evidence published its organic traffic by page type. Detail pages matter more where items live longer and searches are specific, such as a dealer's car or an apartment.

![A sturdy landing-page window for e-bikes in a city stands for years while individual bike listing cards pass through it in days.](listing-systems-architecture/posts/35-web-and-seo-architecture/assets/images/35-web-and-seo-architecture/landing-page-outlives-listings.jpeg)

**Figure 1:** *Listings live for days, but a landing page such as e-bikes in Utrecht keeps a stable URL for years while its contents change, which is why it accumulates the links and ranking history.*

{id: web-and-seo-architecture--the-backend-for-frontend}
### The backend-for-frontend

A **backend-for-frontend (BFF)** is a server-side component owned by the team that owns a client (the iOS and Android apps, or the web front end), which aggregates domain APIs into the shape that client needs and absorbs differences in release cadence. Sam Newman described the pattern in 2015, with the advice that the team building the user interface should own its backend ([Newman, 2015](https://samnewman.io/patterns/architectural/bff/)). Its relevance in classifieds comes from two facts. Pages and screens draw on many domains at once — listing, search, seller, media, ads, entitlements, trust signals — and apps cannot be updated on demand. Vinted's engineers wrote in 2019 (older evidence; current release practice may differ) that mobile releases take about two weeks to reach users, which is why they built server-side repair for malformed analytics events ([Vinted Engineering, 2019](https://vinted.engineering/2019/12/09/vinted-event-ingestion-pipeline-from-client-to-kafka/)). The same delay applies to every API change.

{id: web-and-seo-architecture--architecture-the-customer-facing-stack}
## Architecture: The Customer-Facing Stack

The customer-facing stack has five layers: the edge, the page applications, the backends-for-frontends, the SEO services and the domain APIs beneath them.

![Diagram: The customer-facing stack](listing-systems-architecture/posts/35-web-and-seo-architecture/assets/images/35-web-and-seo-architecture/fig02-customer-facing-stack-pages-apps-reach.jpeg)

**Figure 2:** *The customer-facing stack. Pages and apps reach domain data through their own backends-for-frontends; the SEO services decide which URLs exist and what they return, and the listing event stream keeps sitemaps and edge caches in step with the inventory.*

{id: web-and-seo-architecture--the-edge}
### The edge

The edge — a content delivery network (CDN) with programmable routing — does four jobs in a listing site. It **routes** URL paths to the page application that owns them, which makes it the natural seam for migration (Subito, below, configures route ownership on Akamai). It **caches** rendered pages with time-to-live (TTL) values per page type and purges them on change. It **applies bot rules**, separating verified search engine crawlers from scrapers (see [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale)). And it **terminates** redirects and simple status responses without touching the origin, which matters when millions of retired URLs must answer `301` or `410` cheaply.

Caching policy follows page type. Landing pages tolerate a few minutes of staleness and are a large share of read traffic, so they should be served from cache rather than live search. Listing detail pages can be cached longer, provided a listing event (price change, sold, removed) purges the cached copy by a surrogate key such as the listing ID. Pages with personal data — messages, account, saved searches — are never cached at the edge.

{id: web-and-seo-architecture--rendering-what-the-crawler-and-the-phone-receive}
### Rendering: what the crawler and the phone receive

The rendering strategy is the most consequential decision in the web layer. Five are in common use.

| Strategy | What happens | Crawler sees | Phone performance | Fits |
| --- | --- | --- | --- | --- |
| **Client-side rendering (CSR)** | Server sends a shell; JavaScript fetches data and renders | Content only after rendering, which may be deferred | Slow first content on mid-range phones | Logged-in tools: messaging, seller dashboards |
| **Server-side rendering (SSR) with hydration** | Server renders HTML per request; JavaScript attaches interactivity | Full content in the HTML | Fast first content; interactivity cost depends on the JavaScript shipped | Landing, search and listing pages |
| **Streaming SSR** | Server sends the page in chunks as data arrives | Full content | Faster first bytes when some data is slow | Pages with slow components such as facets or ads |
| **Static or incremental generation** | Pages built ahead of time and regenerated on a schedule or event | Full content | Fastest | Editorial pages, stable landing pages with few changes |
| **Dynamic rendering** | Server detects crawlers and serves them pre-rendered HTML | Pre-rendered HTML | Unchanged for users | Nothing new; Google calls it "a workaround and not a recommended solution" ([Google Search Central, updated 2025](https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering)) |

For public pages of a listing site the decision is rarely in doubt: **landing, search and listing detail pages should be server-rendered**, with as little client JavaScript as interaction requires. Instead of dynamic rendering, Google recommends "server-side rendering, static rendering, or hydration". Client-side rendering remains right for authenticated tools where crawlers never go. The proposed client-rendered rebuild of Tradeyard's search pages would have solved a real problem, slow Yardstick templates, by handing the most valuable pages to the crawler's deferred rendering queue.

Google also indexes the mobile rendering. Its mobile-first indexing guidance asks sites to "make sure that your mobile site contains the same content as your desktop site" and to keep the same structured data on both ([Google Search Central, updated 2025](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)). A mobile layout that hides seller details or attribute tables behind tabs that load on demand may hide them from the index too.

{id: web-and-seo-architecture--composition-who-owns-which-page}
### Composition: who owns which page

Once more than one team serves a site, someone has to decide how pages are composed. The documented record in marketplaces is unusually clear.

- **Runtime fragments.** Zalando's Mosaic assembled pages at request time from fragments served by independent services. In a 2018 post, Zalando described the costs: inconsistent user experience, "an issue most customer-facing websites cannot ignore", and a high contribution barrier because each fragment needed its own full stack. Its replacement, the Interface Framework, combined a GraphQL aggregation layer with renderers built from the design system in a monorepo ([Zalando Engineering, 2018](https://engineering.zalando.com/posts/2018/12/front-end-micro-services.html)). The post is old and describes a system that has since evolved; the lesson about consistency has aged well.
- **Server-side fragment stitching.** AutoScout24 described in 2018 how services served HTML fragments that an nginx-based service stitched together, while newer pages were written in React behind a GraphQL backend-for-frontend ([AutoScout24 Tech Blog, 2018](https://tech.autoscout24.com/blog/posts/first-year-at-autoscout24/)). The current state is not public.
- **Microsites with page-level ownership.** In a 2023 post, Subito (Adevinta, Italy) described splitting its web monolith into "many small independent sites, where each site has, at most, a few pages", each a Next.js application with its own repository, pipeline and team. Routing is configured on Akamai at page level, and shared components come from a monorepo at build time, wrapped in error boundaries ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/our-microsite-architecture/)).
- **Framework migration.** A leboncoin engineer pointed in 2021 to the team's write-up of a migration from a legacy React 15 front end to Next.js, describing about 30 million monthly users and about 40 web developers ([GitHub discussion, 2021](https://github.com/vercel/next.js/discussions/29628)). The article itself could not be retrieved for this book.

The direction of travel in this evidence is **away from runtime composition of fragments and toward page-level ownership with shared components linked at build time**. That fits listing sites well, because their page types map cleanly onto teams: discovery owns landing and search pages, the listing team owns detail pages, the supply team owns insertion, the messaging team owns conversations. My rule is that **one team owns each URL pattern end to end** — rendering, performance budget, status codes and structured data — and the design system, not a runtime composer, keeps the pages consistent.

{id: web-and-seo-architecture--the-seo-services}
### The SEO services

Four small services hold the rules that pages must not each reimplement.

1. **The URL and canonical service** builds every public URL from domain identifiers: listing ID, category ID, location ID and attribute values. It enforces one canonical form — filter order, separators, lowercase, no duplicate filters — and returns the canonical URL for any combination. Pages never assemble URLs by string concatenation.
2. **The landing page registry** holds the set of indexable combinations, each with its state, rule, copy template and history (next section).
3. **The redirect registry** maps every retired URL to its successor or to a gone status, with the reason and date. Category splits, city renames, brand migrations and listing merges all write to it. It is served from the edge.
4. **The sitemap and notification service** maintains sitemaps and change notifications from listing and landing-page events, with accurate `lastmod` values.

Putting category and location *identifiers* behind human-readable slugs, rather than treating the slug as the identifier, is what makes the redirect registry tractable. When the bikes category splits, the service knows which old landing URLs map to which new ones because both are derived from category IDs, not from strings typed into templates.

{id: web-and-seo-architecture--landing-pages-generating-the-durable-seo-inventory}
## Landing Pages: Generating the Durable SEO Inventory

{id: web-and-seo-architecture--the-rule-set}
### The rule set

A landing page should exist when three conditions hold: **people search for it, the marketplace has inventory for it, and it is meaningfully different from the pages that already exist.** Each condition becomes a rule.

| Rule | Measured by | Typical threshold (illustrative) | Action when it fails |
| --- | --- | --- | --- |
| **Demand** | External keyword data, internal search logs, saved searches for the combination | Recurring monthly searches above a floor per country | Not created; existing page reviewed |
| **Supply** | Live listings matching the combination, averaged over weeks | At least a minimum number of results (for example five) on most days | `noindex, follow` while thin; `404` when empty for a sustained period |
| **Distinctness** | Overlap of results with the parent page | Less than a set share of results identical to the parent | Not created; canonical to parent |
| **Depth** | Number of filters in the combination | At most two or three dimensions beyond category and location | Not indexable; reachable only by users |
| **Quality** | Curated title, unique intro copy, internal links, structured data | Template complete and reviewed | Not published |

The thresholds are judgement calls that differ by vertical. What matters is that indexability is a **computed state with explicit rules**, recalculated as inventory and demand change, not a side effect of a filter being clickable.

Google's guidance on faceted navigation gives the outer boundary. If filter combinations need not be indexed, block them with `robots.txt` or keep the filters in URL fragments. If they must be indexed, use standard `&` separators, keep the filter order consistent, prevent duplicate filters, and return `404` for combinations with no results rather than redirecting them to a generic page ([Google Search Central, updated 2025](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation)).

Google's spam policies define the inner boundary. **Scaled content abuse** is when "many pages are generated for the primary purpose of manipulating search rankings", and **doorway abuse** includes "multiple domain names or pages targeted at specific regions or cities that funnel users to one page" ([Google Search Central, spam policies, updated 2026](https://developers.google.com/search/docs/essentials/spam-policies)). A classifieds landing page for "e-bikes in Utrecht" with real e-bikes for sale in Utrecht is not a doorway. A page for "e-bikes in Wijk bij Duurstede" with three listings from Utrecht, wrapped in generated text, comes close. The supply rule is what keeps generated landing pages on the right side of that line.

{id: web-and-seo-architecture--the-lifecycle-of-a-landing-page}
### The lifecycle of a landing page

![Diagram: A landing page is a managed object with states](listing-systems-architecture/posts/35-web-and-seo-architecture/assets/images/35-web-and-seo-architecture/fig03-landing-page-managed-object-states-indexable.jpeg)

**Figure 3:** *A landing page is a managed object with states. Indexable pages are in sitemaps and linked; thin pages answer with noindex and stay linked for users; gone pages answer 404 or 410; redirected pages answer 301 to their successor, recorded in the redirect registry.*

Each state maps to a response: **Indexable** pages return `200`, appear in sitemaps and receive internal links; **Thin** pages return `200` with `noindex, follow`, so users can still use them and crawlers still follow their links to listings; **Gone** pages return `404` or `410`; **Redirected** pages return `301` to the successor. Hysteresis — a page must stay thin for some days before it changes state, and recover for some days before it returns — prevents seasonal or weekend swings from flipping pages in and out of the index.

{id: web-and-seo-architecture--internal-linking-and-copy}
### Internal linking and copy

Landing pages rank partly because the site links to them. The links that matter are structural: breadcrumbs from category to location, "nearby cities" and "related searches" blocks, links from listing detail pages to the landing pages they belong to, and links from editorial pages. In a 2023 post, Adevinta's SEO lead described generating internal links at scale using semantic similarity and search volume, classifying keywords and generating related searches with newer AI models, and using AI-generated meta titles and descriptions to improve click-through ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/how-we-attract-users-with-seo-from-ten-blue-links-to-ai-generated-answers/)). Generated copy is useful when it describes the actual inventory — price ranges, common brands, counts — from data. It becomes a liability when it is filler; that is the behavior the scaled-content policy targets.

{id: web-and-seo-architecture--taxonomy-changes-are-url-migrations}
### Taxonomy changes are URL migrations

Every category change touches landing pages. The taxonomy chapter ([Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies)) owns the change process; this chapter owns what the change does to URLs. When Tradeyard splits bikes into four subcategories, each old landing page — bikes in a city, bikes in a city with a brand, bikes under a price — has one of three fates: it maps to one successor (`301`), it maps to a parent that still makes sense (`301` to the broader page), or it has no meaningful successor (`410`). The redirect registry records each decision, the sitemap service publishes the new pages, and the old ones leave the sitemaps the same day. A taxonomy service that emits a `CategorySplit` event with an old-to-new mapping makes this a pipeline. A taxonomy held in templates makes it a project, which is how The Category Straitjacket shows up in the SEO layer.

{id: web-and-seo-architecture--listing-pages-across-the-lifecycle}
## Listing Pages Across the Lifecycle

{id: web-and-seo-architecture--what-each-state-should-return}
### What each state should return

A listing passes through states that [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) defines: draft, pending, published, paused, sold, expired, removed. The public page has to answer for each of them. No classifieds operator in the evidence for this book published its expired-listing handling, so the policy below is a reference-architecture inference built on Google's documented rules: return `404` or `410` for permanently removed pages, avoid soft 404s, use `unavailable_after` (as a robots meta tag or `X-Robots-Tag` header) when a page should leave results after a date, and keep `lastmod` accurate ([Google Search Central, robots meta tag, updated 2026](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag); [sitemaps, updated 2026](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)).

| Listing state | Response | Page content | Sitemap | Rationale |
| --- | --- | --- | --- | --- |
| Published | `200`, indexable | Full listing | Present, `lastmod` = last material change | The live asset |
| Paused by seller | `200`, `noindex` | Listing marked paused, related live listings | Removed | May return; should not attract searchers now |
| Sold or let, low residual demand (most private goods) | `410` after a short grace period; during grace, `200` with `noindex` | "Sold" notice, related live listings, link to the landing page | Removed at once | Links from messages and alerts still land somewhere useful; the index learns quickly that the page is gone |
| Sold or let, high residual demand (specific car models, popular buildings) | `200` with `unavailable_after` set at sale, for a fixed window, then `410` | "Sold" notice, prominent similar live listings, price context if allowed | Removed at once | The URL may still rank for a specific query; use it to route searchers to live supply, not to pretend the item is available |
| Expired without sale | As for sold, per vertical | "No longer listed", related live listings | Removed at once | Same logic |
| Removed for policy or fraud | `410` immediately | Minimal page, no listing content | Removed at once | Nothing worth keeping; content may be harmful |
| Merged into a canonical listing (duplicates) | `301` to the canonical listing | — | Removed | One URL per item; see [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) |

Two details matter in practice. **The grace period is for people, not crawlers.** Sellers share links in messaging apps and buyers follow links from alerts; a sold page that explains what happened and offers alternatives is better than an error for those visitors. That does not require the page to stay indexable. **Removal latency is a metric.** The time from `ListingSold` to the page returning its new status, leaving the sitemap and being purged from the edge should be measured like publication latency is measured in [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline).

{id: web-and-seo-architecture--sitemaps-from-events}
### Sitemaps from events

Sitemaps should be built from the listing event stream, not regenerated nightly from a database scan. Google's limits shape the design: a sitemap holds at most 50,000 URLs or 50 MB uncompressed, a sitemap index holds up to 50,000 sitemaps, `priority` and `changefreq` are ignored, and `lastmod` is used only if it is "consistently and verifiably" accurate ([Google Search Central, updated 2026](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap); [sitemap index files, updated 2025](https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps)).

![Diagram: Sitemaps and removal signals driven by listing events](listing-systems-architecture/posts/35-web-and-seo-architecture/assets/images/35-web-and-seo-architecture/fig04-sitemaps-removal-signals-driven-listing-events.jpeg)

**Figure 4:** *Sitemaps and removal signals driven by listing events. The same ListingSold event that removes the listing from search purges the edge cache, drops the URL from its sitemap shard and schedules the gone status, so the search engine learns about the sale through every channel at once.*

A practical shard layout for a large site is by page type, country and creation date: new listings append to the current day's shard, so recently changed shards are small and their `lastmod` is meaningful. Landing pages live in their own shards, updated when the registry changes state. Search Console's per-sitemap reporting then shows indexing coverage by page type, which is the diagnostic the SEO team needs.

Push notification beyond sitemaps varies by engine. **IndexNow** lets a site notify participating engines — the protocol site lists Bing, Naver, Seznam.cz, Yandex, Yep and Amazon — when URLs are added, updated or deleted, while warning that submission "does not guarantee immediate indexing" ([IndexNow FAQ, n.d.](https://www.indexnow.org/faq)). Google is not listed. Google's Indexing API is documented for job postings: its job-posting guide recommends the Indexing API over sitemaps because it prompts a faster recrawl, and says "we don't allow expired job postings", which must be removed by setting `validThrough` in the past, returning `404` or `410`, or removing the markup ([Google Search Central, job postings, updated 2026](https://developers.google.com/search/docs/appearance/structured-data/job-posting)). For a jobs section such as Tradeyard's in Poland and Portugal, expiry is a compliance rule, not only hygiene.

{id: web-and-seo-architecture--structured-data-saying-what-the-page-is}
## Structured Data: Saying What the Page Is

Structured data is machine-readable markup — usually JSON-LD using the schema.org vocabulary — that describes what a page is about. For listing sites it has three uses: rich results in search engines, consistent machine-readable facts for other consumers, and a check that the visible page and the data agree.

The available types and the search features they enable change, and the architecture should not depend on any one of them.

- **Product and Offer.** Google distinguishes **product snippets**, for pages where people cannot buy the product directly, from **merchant listings**, for "pages where customers can purchase products from you" ([Google Search Central, product structured data, updated 2025](https://developers.google.com/search/docs/appearance/structured-data/product)). Most classifieds pages fall in the first group. Whether a page with an in-platform payment option, such as Tradeyard Safe Deal, qualifies for the second is a question for the SEO team and counsel, not a default.
- **Vehicle listings.** Google added vehicle listing markup in October 2023, announced on 12 June 2025 that "we will be phasing out support for a few structured data features in Search", and on 9 September 2025 removed the vehicle listing documentation because the type was "no longer shown in Google Search results" ([Google Search Central, documentation updates, 2025](https://developers.google.com/search/updates)). An automotive marketplace that built a pipeline for that feature in 2024 found its rich result gone within two years.
- **Real estate.** schema.org has a `RealEstateListing` type, with properties such as `datePosted` and `leaseLength`, in its "new" area, which means the definition is still open to change ([schema.org, n.d.](https://schema.org/RealEstateListing)).
- **Jobs.** `JobPosting` remains a documented Google feature with strict expiry rules (above).

**Generate structured data from the same read model that renders the visible page**, in one builder per page type, so a search feature can be added or dropped by changing the builder, not every template. Never put data in the markup that the page does not show, and never put data in it that the page must not show: the precise address of a private seller's home, which [Where Is It? Location, Geocoding and Privacy](#location-and-geo) keeps out of every public surface, includes JSON-LD.

{id: web-and-seo-architecture--performance-core-web-vitals-as-an-architecture-budget}
## Performance: Core Web Vitals as an Architecture Budget

Google's **Core Web Vitals** measure three aspects of user experience at the 75th percentile of page loads, separately for mobile and desktop: **Largest Contentful Paint (LCP)**, good at 2.5 seconds or less; **Interaction to Next Paint (INP)**, good at 200 milliseconds or less; and **Cumulative Layout Shift (CLS)**, good at 0.1 or less. INP replaced First Input Delay as a stable Core Web Vital in 2024 ([web.dev, updated 2024](https://web.dev/articles/vitals)).

For listing pages the main threats to those numbers are predictable: large hero images, third-party advertising and tracking scripts, heavy client-side state for filters, and layout shifts from late-loading ad slots. The best-documented marketplace case is QuintoAndar, the Brazilian rental and real-estate marketplace. In a 2025 case study it reported that mobile INP fell from 1,006 ms to 216 ms during 2024 and the share of pages rated "good" rose from 42% to 78%. It linked a 36% year-over-year rise in conversions — scheduled property visits — to the work "strongly, but not solely". Its techniques included yielding in long tasks, removing third-party pixels and dropping CSS-in-JS, governed through alarms and canary rollbacks ([web.dev, 2025](https://web.dev/case-studies/quintoandar-inp)).

Three architectural consequences follow.

1. **Performance budgets belong to page owners.** Each URL pattern has an LCP and INP budget in the owning team's objectives, measured from field data. A shared dashboard nobody owns does not move.
2. **Advertising is a budgeted guest.** Display advertising pays for much of a free classifieds site, and header bidding delays ad decisions by design (see [Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms)). Reserve ad slot dimensions to prevent layout shift, load ads after the main content, and give the ads team an explicit share of the performance budget rather than an open line.
3. **Images come from the media pipeline at the right size.** Responsive derivatives, modern formats and explicit dimensions are a [Photos Sell: Media Pipelines for Listings](#media-pipeline) responsibility that shows up as LCP.

Performance and crawl capacity are the same budget seen from two sides. A landing page that renders in 400 ms at the origin serves users faster and lets the crawler fetch more pages per day; a page that takes four seconds under load does the opposite on both counts.

{id: web-and-seo-architecture--apps-backends-for-frontends-server-driven-ui-and-deep-links}
## Apps: Backends-for-Frontends, Server-Driven UI and Deep Links

Apps and the web do different jobs. At Tradeyard in 2027, the apps account for **57%** of sessions and the web for **43%**. My reading, which no source in this chapter quantifies for other brands, is that apps carry the most engaged users while the web, through organic search, carries most of the acquisition. The architecture must serve both without building every capability twice.

{id: web-and-seo-architecture--one-backend-per-client-family}
### One backend per client family

Tradeyard's apps call Yardstick and about 40 newer services directly, through an API gateway, with versioning negotiated case by case. Every screen makes several calls, and every backend change has to stay compatible with app versions that some users will not update for months. A **mobile BFF** owned by the app teams changes that: the apps call one backend shaped for their screens, and the BFF calls the domain APIs. The web has its own BFF, used by the server-rendered pages. The BFFs hold presentation logic and aggregation, not business rules: if the BFF decides whether a seller may bump a listing, the entitlement rule now lives in two places, which is how Entitlement Spaghetti starts (see [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)).

The trade-off is duplication between BFFs. I accept some, because the alternative — one general-purpose API for all clients — tends to grow into a lowest-common-denominator interface that every client works around. The rule I use is that **domain APIs are shared and stable, BFFs are per client family and allowed to change fast**, and a BFF that starts holding domain rules gets those rules pushed down.

{id: web-and-seo-architecture--server-driven-forms}
### Server-driven forms

Insertion forms in classifieds are defined by the category's attribute schema: a bike has frame size and gears, a car has mileage and first registration, an apartment has rooms and energy class (see [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas)). If the form is compiled into the app, every schema change waits for app adoption, and a taxonomy change like the bikes split cannot go live on a date. My recommendation, a reference-architecture inference rather than documented practice, is to render insertion forms from the attribute schema served by the backend, so the app ships a form engine rather than forms. The same mapping problem appears in the app-first photo-to-listing features covered in [AI Across the Listing Lifecycle](#ai-in-listing-systems).

{id: web-and-seo-architecture--deep-links-and-webapp-parity}
### Deep links and web–app parity

A listing URL shared in a messaging app or clicked in a search result should open the app if it is installed and the web page otherwise. Both platforms support this through verified associations between the domain and the app: Android App Links verify the app's signing certificate against an `assetlinks.json` file on the domain ([Android Developers, n.d.](https://developer.android.com/training/app-links)), and Apple's universal links rely on an `apple-app-site-association` file ([Apple Developer, n.d.](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app)). The requirement that is often missed: **the app must understand the same canonical URLs the web uses**, including retired ones, so the redirect registry serves both. An app that cannot resolve a URL the web redirected last month opens on an error screen.

{id: web-and-seo-architecture--localization-and-multi-country-domains}
## Localization and Multi-Country Domains

Multi-country groups usually run one domain per country; Tradeyard runs four, and Tradeyard Belgium serves Dutch and French speakers with the same inventory. Google's `hreflang` annotations tell the engine which pages are language or regional versions of the same content. They can be declared in HTML, HTTP headers or sitemaps; every version must list itself and all other versions, and "if two pages don't both point to each other, the tags will be ignored" ([Google Search Central, updated 2026](https://developers.google.com/search/docs/specialty/international/localized-versions)). For a bilingual landing page — "e-bikes in Brussels" in Dutch and in French — that reciprocity is only reliable when both URLs come from the URL service, keyed on the same category and location identifiers, rather than from translated templates maintained separately.

The landing page registry should be per country, sharing rules and code but not data, because category names, location hierarchies and useful combinations differ by market. [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) owns the tenancy model that makes that configuration rather than code.

{id: web-and-seo-architecture--ai-search-and-answer-engines-a-new-channel-and-a-new-crawler}
## AI Search and Answer Engines: A New Channel and a New Crawler

Between 2024 and 2026 the search results page itself changed. Google introduced AI Overviews in Search in May 2024, documented them as replacing the Search Generative Experience, and from June 2025 counted AI Mode data in Search Console's performance totals ([Google Search Central, documentation updates, 2024–2025](https://developers.google.com/search/updates)). Assistants such as ChatGPT, Claude and Perplexity answer shopping and housing questions with links to sources.

For a listing site, three points matter.

- **There is no special markup.** Google's guidance says "there are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary", and that no special schema.org structured data is needed. Pages must be indexed and eligible for a snippet; `nosnippet`, `data-nosnippet`, `max-snippet` and `noindex` control what is shown ([Google Search Central, AI features, updated 2025](https://developers.google.com/search/docs/appearance/ai-features)).
- **Opting out of Google's AI training does not opt out of Search.** The same page says the `Google-Extended` token applies to "AI training and grounding in some of Google's other systems", and that Search crawling is controlled through `Googlebot` rules.
- **Clicks per crawl are falling.** On 1 July 2025 Cloudflare announced that it would block AI crawlers by default for its customers unless they pay for access, and claimed that getting traffic had become far harder: by its estimate, publishers get about ten times less traffic from Google for the same content than a decade earlier, and much less again from AI assistants ([Cloudflare, 2025](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)). These are a vendor's figures with a commercial interest, but the direction is consistent with what publishers report.

Classifieds have an advantage that informational publishers lack: **an answer engine cannot complete the job**. Whoever wants the bike still has to contact Femke, and whoever wants the apartment still has to book a viewing. The defensible asset is fresh, contactable inventory, which an answer cannot copy without going stale. Classifieds evidence is thin: Adevinta's 2023 post saw no drastic click loss after Bing's AI snippets, but that predates AI Overviews.

The architectural moves are practical: keep landing and listing pages fast, accurate and crawlable for the engines that send buyers; decide per crawler, as policy, which automated agents may read the site (see [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale) for bot management); measure referrals from AI assistants as their own channel; and treat structured, licensed access for agents as a product question that [AI Across the Listing Lifecycle](#ai-in-listing-systems) owns. Tradeyard's 2027 numbers are a reminder of scale: assistants refer about **0.7%** of its web sessions, while self-declared AI crawlers make about **11%** of requests for public HTML.

{id: web-and-seo-architecture--veldmark-worked-example-rebuilding-tradeyard-s-seo-inventory}
## Veldmark Worked Example: Rebuilding Tradeyard's SEO Inventory

Ingrid does not approve the client-rendered rebuild. In May 2027 the architecture advice forum adopts a decision record for Tradeyard's web layer with five parts, and the web and SEO work is scheduled ahead of the Yardstick search extraction planned for Q4 2028, because the web layer is where the strangler starts (see [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration)).

1. **Server-rendered page applications per URL pattern**, React with server-side rendering and streaming, owned by the discovery, listing and supply teams, behind CloudFront route rules. Yardstick keeps rendering any page type that has not moved.
2. **A web BFF and a mobile BFF**, owned by the web and app teams, over the domain APIs.
3. **The four SEO services** — URL and canonical, landing page registry, redirect registry, sitemap and notification — built once and configured per country.
4. **Listing lifecycle rules** as in the table above, driven by the Common Ground listing event contract v1, which goes live on 1 July 2027 (see [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)).
5. **Performance budgets** for landing and listing pages: mobile LCP p75 at or under 2.5 s, INP p75 at or under 200 ms, owned by the page teams.

The landing page registry starts from data. The SEO team takes 14 months of internal search logs, saved searches and external keyword data and scores every category × location × attribute combination with recurring demand. It applies the supply rule — at least five live results on most days over the previous eight weeks — and the depth rule, at most two attributes beyond category and location. About **2.4 million** combinations across the four countries qualify. They become the indexable set. The remaining 17.4 million search URLs that were in the index get `noindex, follow` if they are reachable from the user interface, `404` if they have no results, and drop out of all sitemaps.

The old gone-listing pages are handled in one pass and then by the event-driven rules: about 6.3 million pages move to `410`, except roughly 180,000 that the SEO team identifies as still ranking for specific queries — mostly sold cars and cargo bikes — which keep a `200` page with similar live listings and an `unavailable_after` date. Femke's bike falls under the general rule: under the new policy its page would have answered `noindex` from 18:11 on 8 March and `410` from 22 March.

| Measure | February 2027 (before) | February 2028 (after) |
| --- | --- | --- |
| Indexed URLs, all Tradeyard domains | 40.0M | 15.9M |
| Sold, expired or removed listing pages indexed | 6.3M | 0.4M |
| Share of Googlebot fetches on facet or dead URLs | 41% | 9% |
| Median time to first crawl, new NL listing | 2.6 days | 0.6 days |
| Organic sessions, all domains (index, Feb 2027 = 100) | 100 | 104 |
| Contacts from organic sessions (index, Feb 2027 = 100) | 100 | 117 |
| Mobile LCP p75, landing pages | 3.4 s | 2.2 s |
| Mobile INP p75, landing pages | 310 ms | 180 ms |

The number that went down — indexed URLs, by 60% — is the one the board pack used to celebrate. The number that matters went up: **contacts from organic sessions rose 17%** while organic sessions rose only 4%, because searchers landed on pages with live inventory. The forum also changes the board pack: indexed URLs disappear from it, and organic contacts per thousand organic sessions replaces organic sessions as the headline SEO metric. That is the Vanity Liquidity correction applied to SEO.

![An overgrown hedge of 40.0M indexed pages where searchers hit dead ends, beside a pruned bush of 15.9M pages where searchers reach sellers, with contacts up 17%.](listing-systems-architecture/posts/35-web-and-seo-architecture/assets/images/35-web-and-seo-architecture/pruning-the-index.jpeg)

**Figure 5:** *Tradeyard cut its indexed URLs from 40.0 million to 15.9 million, and contacts from organic sessions rose 17%, because searchers now land on pages with live inventory.*

The bikes split on **1 November 2027** is the first test. The taxonomy service emits the split with its mapping; the URL service derives about 18,400 old bike landing URLs in the Netherlands and Belgium and their candidates; the SEO team reviews about 1,100 ambiguous cases by hand (a "bikes under €200 in Utrecht" page has no single successor and is redirected to the broader city page); and the redirect registry, sitemaps and new landing pages go live with the category. Organic sessions to bike landing pages dip by about 8% in the first three weeks and recover by mid-December. Under the old architecture the same change would have needed template edits in Yardstick for each country and a spreadsheet of redirects.

{id: web-and-seo-architecture--trade-offs}
## Trade-offs

| Decision | Option A | Option B | Choose A when | Choose B when |
| --- | --- | --- | --- | --- |
| Rendering of public pages | **SSR with hydration** | Client-side rendering | Pages must rank or be shared; mid-range phones matter | Logged-in tools with no SEO role |
| Composition | **Page-level ownership, build-time shared components** | Runtime fragment composition | Page types map to teams; consistency matters | A single page genuinely needs independently deployed parts from many teams, and you can fund the consistency work |
| Landing page breadth | **Rule-based allow-list** | Index every reachable combination | Large inventory; crawl budget is binding | Small site where crawl budget is not a constraint |
| Gone listing pages | **`410` after grace; `200` only for proven demand** | Permanent `200` "sold" pages | Most verticals with short-lived, unique items | Verticals where sold-item pages are a product (price history, model pages) with clear unavailability signals |
| App backend | **BFF per client family** | One shared public API | Several clients with different release cycles | One client, or an external API product for partners |
| Structured data | **Builder per page type from the read model** | Markup in templates | Search features change and several page types share data | A very small site |
| Edge caching of landing pages | **Cached with minutes of TTL and event purges** | Rendered live per request | High read volume, inventory tolerant of minutes of staleness | Very low traffic or results that must be exact |
| AI crawlers | **Explicit per-agent policy** | Default allow or default block | Always; the default should be a decision | — |

The trade-off that generates the most argument is the gone-listing policy, because a `200` sold page does capture some organic traffic. The question is what that traffic converts into. At Tradeyard, sold and expired pages drew 6% of organic sessions and 0.4% of organic contacts. In automotive and property, where people search for specific models and buildings, the numbers can justify keeping a curated subset; the evidence should decide, page group by page group.

{id: web-and-seo-architecture--vertical-differences}
## Vertical Differences

| Concern | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Main landing page dimensions | Category × city, with one attribute (brand, type) | Transaction type × property type × area, with rooms or price band | Make × model × city, with fuel or body type | Role × city, with contract type |
| Listing lifetime and detail page value | Days; detail pages matter little after sale | Weeks to months; detail pages earn long-tail traffic | Weeks; specific model searches persist after sale | Weeks; expiry must be prompt |
| Gone listing rule | `410` after short grace | `410` or sold page per market practice and law; the same property may return with a new listing | Curated sold pages for proven demand, then `410` | Required removal: `validThrough`, `404` or `410` |
| Duplicates | Reposts; canonicalize to the newest | Several agencies list one property: one canonical URL per cluster (see [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)) | Dealer feeds across brands | Same job via several job boards |
| Structured data | Product snippet | `RealEstateListing` (schema.org "new" area) | Vehicle listing feature retired by Google in 2025 | `JobPosting`, with strict policy |
| Location precision on public pages | Neighborhood | Address only with seller consent; otherwise area | Dealer address public; private seller area only | Employer location |
| Performance pressure | Ads-heavy pages | Many large images, maps | Many images, finance calculators | Light pages |

Real estate needs one more rule: when several agencies advertise the same apartment, the cluster gets one canonical URL, through canonical tags or a property page. Otherwise the Lyon apartment listed by three agencies in May 2027 would produce three detail pages competing for the same queries. Choosing which listing is canonical is commercially sensitive, because agencies pay for visibility. The rule should be published and neutral; Hearthly's rule picks the listing with the highest completeness and media-quality score, never paid status, and it is owned with the clustering rules in [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution).

{id: web-and-seo-architecture--failure-modes}
## Failure Modes

- **The soft-404 graveyard.** Gone listings answer `200` with "no longer available". Crawlers keep fetching them, sitemaps keep listing them, and searchers keep landing on them. This is Ghost Inventory at the search-engine layer, and it hides because no user-facing metric moves.
- **The infinite facet space.** Every filter combination has a crawlable URL with parameters in arbitrary order. Crawlers spend their budget on red bikes between €110 and €115, and new listings wait days to be discovered.
- **The SPA cliff.** A redesign moves public pages to client-side rendering. Indexing of content lags, rankings drop over several weeks, and the cause is found only after the traffic is gone.
- **The template redirect spreadsheet.** Category and location changes are handled by hand-maintained redirect lists in templates. Old URLs break, chains of redirects build up, and teams avoid taxonomy changes.
- **Doorway drift.** Landing page generation is tuned for coverage. Pages for small towns with borrowed inventory and generated filler accumulate until the site's quality signals suffer.
- **The app that cannot follow.** A taxonomy or schema change ships on the web, while app versions in the field cannot render the new form or resolve the new URLs.
- **The vanity index count.** Indexed URLs and organic sessions are reported as success; the share of organic sessions that produce a contact is not reported at all.

{id: web-and-seo-architecture--the-chief-architect-s-view}
## The Chief Architect's View

**What to share.** The four SEO services, the event-driven sitemap pipeline, the redirect registry pattern, the structured-data builders and the lifecycle rules are good group capabilities: they are rules plus data, configured per brand and country. The page applications, design and copy are not. Under Common Ground's principle — share platforms, not products — Tradeyard, Motorvane and Hearthly keep their own pages, brands and SEO strategies, while running on shared services that make the rules explicit.

**What to decide centrally.** Three decisions should be group policy recorded in decision records: the rendering standard for public pages (server-rendered), the gone-listing rules per vertical, and the per-agent crawler policy, which has commercial and legal implications beyond SEO. Everything else — landing page dimensions, thresholds, copy — belongs to each brand's SEO and product teams.

**Who owns what.** Each URL pattern has one owning team. The SEO team owns the rules, the registry and the measurement, not the pages. The platform team owns the edge, the URL service and the sitemap pipeline. The taxonomy team must not be able to ship a category change without the redirect registry being updated in the same release; that dependency is enforced in the pipeline, not by memory.

**Migrations are SEO events.** Brand migrations, domain consolidations and monolith extractions all change URLs or responses at scale. [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) and [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration), in [Part VIII — LEADERSHIP: The Chief Architect's Agenda](#part-8), own those programs; the Chief Architect's job is to require a URL migration plan, a redirect registry and a traffic baseline before any of them starts.

**What to watch.** Organic contacts per thousand organic sessions, by brand and page type; the share of crawl spent on indexable URLs; time to first crawl for new listings; removal latency from sale to gone status; Core Web Vitals at the 75th percentile by page type; and AI-assistant referrals as a separate channel. Indexed URL count belongs on an operational dashboard, never in a board pack.

{id: web-and-seo-architecture--questions-to-ask}
## Questions to Ask

1. Which URL patterns exist, which team owns each one end to end, and where is that ownership recorded?
2. What rule decides whether a search result page is indexable, how often is it recomputed, and how many pages are in each state today?
3. What does a listing URL return in each lifecycle state, and how long after a sale does the page reach its final status, leave the sitemap and leave the edge cache?
4. Are sitemaps generated from listing events with accurate `lastmod`, and can we see indexing coverage by page type?
5. What share of crawler fetches land on indexable URLs, and what is the median time to first crawl of a new listing?
6. Which public pages are rendered on the client, and what would they look like to a crawler that does not execute JavaScript?
7. How is a category split or a city rename turned into redirects, and can the taxonomy change ship without them?
8. Who owns each page type's Core Web Vitals, and what share of the performance budget is reserved for advertising and third-party scripts?
9. Can the apps resolve every canonical and retired URL the web uses, and how long does a form change take to reach most app users?
10. What is our policy for each AI crawler and assistant, who decided it, and how do we measure the traffic they send?

{id: web-and-seo-architecture--from-pages-to-data}
## From Pages to Data

The customer-facing layer is where a marketplace meets its two most demanding clients: people on phones and the crawlers that send them. Both are served best by the same architecture — fast server-rendered pages owned by clear teams, URLs derived from domain identifiers, and lifecycle rules driven by the listing event stream. The decisive change at Tradeyard was not a framework but a metric, organic contacts instead of indexed URLs. Defining such metrics consistently across brands — what a "contact" is, which session counts as organic, how page views are tracked with consent — is the work of the data platform, which [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) takes up next.

{id: web-and-seo-architecture--sources-and-evidence}
## Sources and Evidence

{id: web-and-seo-architecture--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Our microsite architecture](https://adevinta.com/techblog/our-microsite-architecture/) — Alessandro Grosselle (Subito), Adevinta Tech Blog, 2023. Next.js microsites with page-level team ownership, Akamai routing, build-time shared components.
- [How We Attract Users with SEO: From Ten Blue Links to AI-Generated Answers](https://adevinta.com/techblog/how-we-attract-users-with-seo-from-ten-blue-links-to-ai-generated-answers/) — Norbert Híres, Adevinta Tech Blog, 2023. Internal linking at scale, AI-generated meta data, early Bing AI-snippet observations.
- [Front-End Micro Services: Fragments, limitations, solutions](https://engineering.zalando.com/posts/2018/12/front-end-micro-services.html) — Jeremy Colin, Zalando Engineering, 2018. Costs of runtime fragment composition and the move to a renderer framework.
- [What I learned in my first year at AutoScout24](https://tech.autoscout24.com/blog/posts/first-year-at-autoscout24/) — Martin Lechner, AutoScout24 Tech Blog, 2018. Server-side fragment stitching and a GraphQL backend-for-frontend.
- [Next.js discussion #29628](https://github.com/vercel/next.js/discussions/29628) — GitHub, comment dated 2021. Pointer to leboncoin's migration from React 15 to Next.js; the article itself was not retrieved.
- [Scalable and non-blocking event ingestion pipeline](https://vinted.engineering/2019/12/09/vinted-event-ingestion-pipeline-from-client-to-kafka/) — Vinted Engineering, 2019. Two-week mobile release adoption as a constraint on server and client design.
- [How QuintoAndar improved INP](https://web.dev/case-studies/quintoandar-inp) — web.dev, 2025. Marketplace INP improvement, techniques and conversion effect.
- [Content Independence Day: no AI crawl without compensation](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/) — Cloudflare, 2025. Default blocking of AI crawlers; vendor estimates of falling traffic per crawl.

{id: web-and-seo-architecture--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Managing crawl budget for large sites](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget) — Google Search Central, updated 2026. Which sites need crawl budget management; effect of slow and error responses; soft 404s.
- [Managing crawling of faceted navigation URLs](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation) — Google Search Central, updated 2025. Facet URL rules, `404` for zero-result combinations.
- [Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) and [Manage your sitemaps with sitemap index files](https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps) — Google Search Central, updated 2026 and 2025. Sitemap limits and `lastmod` accuracy.
- [Robots meta tag, data-nosnippet, and X-Robots-Tag specifications](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) — Google Search Central, updated 2026. `unavailable_after` and snippet controls.
- [Dynamic rendering as a workaround](https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering) — Google Search Central, updated 2025. Dynamic rendering not recommended; SSR, static rendering or hydration instead.
- [Mobile-first indexing best practices](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) — Google Search Central, updated 2025. Content and structured data parity between mobile and desktop.
- [Spam policies for Google web search](https://developers.google.com/search/docs/essentials/spam-policies) — Google Search Central, updated 2026. Scaled content abuse and doorway abuse.
- [Product structured data](https://developers.google.com/search/docs/appearance/structured-data/product) — Google Search Central, updated 2025. Product snippets versus merchant listings.
- [Job posting structured data](https://developers.google.com/search/docs/appearance/structured-data/job-posting) — Google Search Central, updated 2026. Expired job removal and the Indexing API.
- [Latest Google Search documentation updates](https://developers.google.com/search/updates) — Google Search Central, 2023–2026. Vehicle listing markup added (2023) and retired (2025); AI Overviews (2024); AI Mode in Search Console (2025).
- [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) — Google Search Central, updated 2025. No special requirements for AI features; snippet controls; scope of `Google-Extended`.
- [Localized versions of your pages](https://developers.google.com/search/docs/specialty/international/localized-versions) — Google Search Central, updated 2026. `hreflang` methods and reciprocity.
- [Web Vitals](https://web.dev/articles/vitals) — web.dev, updated 2024. Core Web Vitals thresholds; INP replacing FID.
- [RealEstateListing](https://schema.org/RealEstateListing) — schema.org, n.d. Real-estate listing type in the "new" area.
- [IndexNow FAQ](https://www.indexnow.org/faq) — IndexNow, n.d. URL change notification protocol and participating engines.
- [About deep links (Android App Links)](https://developer.android.com/training/app-links) — Android Developers, n.d. Verified app links.
- [Supporting universal links in your app](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) — Apple Developer, n.d. Universal links and site association.

{id: web-and-seo-architecture--research-and-practitioner-sources}
### Research and practitioner sources

- [Pattern: Backends For Frontends](https://samnewman.io/patterns/architectural/bff/) — Sam Newman, 2015. Definition of the backend-for-frontend and the advice that the UI team owns it.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
