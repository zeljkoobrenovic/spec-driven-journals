---
title: "Delivering the Storefront: Themes, Headless, Rendering and Performance"
date: 2026-11-07
author: Željko Obrenović
excerpt: "How does a storefront reach shoppers and search engines, and when does headless make sense? Compare rendering models, keep product data fresh, build technical SEO into public pages, and own a separate front end when a business need and an operating team justify it."
permalink: storefront-architecture
timetoread: 27 min read
icon: "assets/icons/32-storefront-architecture.png"
logo: "assets/images/32-storefront-architecture/logo.jpeg"
---

> **IN THIS CHAPTER, YOU WILL:** Follow product pages to shoppers and search engines, compare rendering models, and judge when owning a separate storefront is worthwhile.

> **KEY POINTS:**
>
> * **A storefront renders facts other systems own.** Catalog, prices, stock and cart come from their owning services. The rendering model determines who builds and runs the pages; in the three hosted-platform models discussed here, checkout stays on the platform.
> * **Cache the shell, fetch the promise.** Cache product content per market and language, keep public price and availability snapshots current, and validate live purchase terms. Search engines need readable product pages too; a fast storefront that hides its products loses a route to customers.
> * **Go headless for a need the theme cannot meet, never for speed alone.** The performance evidence is directional, dated and self-selected; a themed storefront with disciplined app scripts can pass Google's thresholds. Headless is justified by a shared front end across brands, a content-led site or a business-customer portal with negotiated prices, and it costs a second deployable that a small team must run.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-commerce-platforms-go-wrong.html):**
>
> * **The Giant's Boots** — headless storefront architectures are copied from brands with front-end teams of fifty, by merchants with three.
> * **The Forked Platform** — a theme edited by hand for years is the storefront's version of a core that cannot take the vendor's updates.
> * **The First Snowfall** — the storefront meets forty times its normal traffic once a year, and whether its pages are cacheable decides whether it stands.

<br>
A slow product page can lose a sale before the shopper reaches checkout. Replacing the code that builds the page may help, but the delay might come from a price service, a stock lookup or an app script. A new page that waits for the same slow answers can inherit the same problem. Establish what is delaying the shopper before choosing a replacement.

The **storefront** produces the pages shoppers use to find products and buy. A platform can render them from a theme; a **headless storefront** is a separate application calling the commerce engine through APIs. The latter gives the merchant more control over how pages combine catalog, price, search and cart data. It also makes the team responsible for running that application and keeping its displayed answers fresh.

Most of the previous chapter's apps land on the storefront: as theme code, app blocks and scripts that run in the shopper's browser. Those app scripts, more often than the rendering model, are what makes a product page slow.

Kestrel & Pine, the fictional outdoor brand, runs three localized storefronts from one agency-maintained theme. It has 41 installed apps, and on its busiest hour storefront traffic reaches 41 times an average hour. The example follows Head of Engineering Noor Visser's decision to decline a February 2027 headless proposal.

**Where we are in the order's journey.** Eva sees the Ridgewalker jacket on her phone before completing checkout at 21:14 on 13 April 2027. Price, stock and the next-day delivery promise shape her decision. [[cart-and-checkout]], [[commerce-payments]] and [[order-management]] follow the obligations created by that page.

The chapter starts with the agency's headless proposal and Noor's measurements. It then sets out what a storefront owns and the three rendering models. It reads the dated performance evidence and treats accessibility as a requirement, then sets the rule for what is cached and what is fetched live and what public pages owe search engines. It compares the four options, with mobile apps beside them, and when each fits by scale stage. It ends with Noor's decision, two public checks for a merchant that does replace its storefront, the ways storefronts go wrong and what to take away.

## Setting the Scene at Kestrel & Pine: The Headless Proposal

The agency proposes a separate storefront application on the platform vendor's **edge runtime**, servers near shoppers that execute frontend code, plus a separate content system. It promises better speed, more flexible brand content and future readiness.

The illustrative estimate is **about €240,000 and nine months**, plus a second runtime to operate. Noor asks which need the existing theme cannot meet.

She starts with real-user measurements. In the illustrative February 2027 results for the NL storefront's product pages on mobile, the main content appears in **2.1 seconds**, response to interaction takes **310 milliseconds**, and layout shift scores **0.08**. These are 75th-percentile measurements: three quarters of visits perform at least as well.

Content loading and layout stability already meet Google's good ranges (2.5 seconds or less, and 0.1 or less). Responsiveness does not: good is 200 milliseconds or less. The slow responses trace to scripts from eleven of its 41 apps. That finding points to specific work before an architectural replacement.

She declined the rebuild. The next sections set out what she weighed; her four-part answer comes in In Practice.

## What a Storefront Does, and What It Does Not Own

The answer starts from what a storefront is. A storefront produces pages: home, category (also called collection) pages, product pages, search results, content pages, the cart, the account pages and, at the end, the checkout. To produce them it needs facts from almost every other part of the platform. **It owns none of those facts.** It owns the templates, the layout, the brand, and the scripts that run in the browser.

| What the page shows | Who owns the fact | Chapter |
| --- | --- | --- |
| Product name, description, images, attributes | The catalog, or the PIM (product information management system) once there is one | [[product-information]] |
| Price, and the tax-inclusive display for EU shoppers | The pricing engine or price list | [[pricing-architecture]] |
| Discounts and badges | The promotion engine | [[commerce-promotions]] |
| Search results, facets, sort order | The search index | [[commerce-search-and-discovery]] |
| "In stock", "only 3 left", pre-order | The availability service, or the platform's stock until there is one | [[inventory-and-availability]] |
| The delivery promise | The shipping service, or a static rule | [[shipping-and-delivery]] |
| The cart and the checkout | The platform's checkout | [[cart-and-checkout]] |
| Editorial content (stories, guides, campaign pages) | A content management system (CMS), the tool editors use to write and publish pages without engineers | this chapter |
| Who the shopper is, and which prices they see | Identity and the customer record | [[identity-and-master-data]] |

![Diagram: The storefront renders facts it does not own](assets/images/32-storefront-architecture/fig01-storefront-renders-facts-it-does-not.jpeg)
**Figure 1:** *The storefront renders facts it does not own: product data, prices, availability, search results and content come from other systems, and the buy button hands the shopper to a checkout the platform runs.*

That table is the reason the storefront question is an architecture question. A headless storefront does not move any of those facts; it moves the **rendering** and the **glue** between them into the merchant's hands. Whether that is a gain depends on whether the merchant wanted either.

## Three Rendering Models

Two words first. **Server-side rendering** means a server builds the complete page as HTML and sends it; the browser shows it at once. **Client-side rendering** means the server sends a mostly empty page plus JavaScript, and the browser fetches data and builds the page itself. Early headless storefronts were client-rendered single-page applications, which is where their reputation for slow first loads comes from; today's headless frameworks render on the server by default, so the distinction between the models is no longer about rendering technique but about **who runs the renderer and where the templates live**.

### Model 1: the theme, rendered by the platform

A **theme** is a set of templates (and, on hosted platforms, the settings and scripts around them) that the platform's own renderer turns into pages. Shopify's Liquid themes, BigCommerce's Stencil ("BigCommerce's Handlebars-based theme engine") and the templates of Salesforce's Storefront Reference Architecture (SFRA) are the dated examples. The platform owns rendering, caching, delivery, security and scale; the merchant owns the templates.

Shopify's account shows what that delivery infrastructure involves. Its August 2020 account describes a dedicated Liquid renderer using database replicas, a query cache, an in-memory cache and a full-page cache. It reported response times four to six times faster than its predecessor. In January 2022 Shopify's CTO described deploying that renderer regionally without the whole Rails monolith. These are dated architectural examples, not measurements of today's service.

The merchant inherits delivery infrastructure but is limited by the platform's page types. Shopify's Online Store 2.0 (29 June 2021) extended those types through JSON templates, sections and app blocks, reducing the need to edit templates directly.

### Model 2: headless on the vendor's runtime

The vendor supplies a storefront **API** and hosting; the merchant builds the front end. Shopify's Hydrogen toolkit adds Storefront and Customer Account API clients to a chosen framework, with React Router 7 as its starter and Oxygen as hosting (Shopify's documentation, version 2026-10). Oxygen became available on Shopify's main plans at no extra cost in February 2023. Salesforce's React-based PWA Kit runs on Salesforce's hosting service, Managed Runtime. Adobe Commerce as a Cloud Service, Adobe's hosted version of its platform, uses a headless storefront delivered through Adobe's Edge Delivery Services (Adobe documentation, 20 October 2026).

Checkout stays on the commerce platform: Hydrogen explicitly excludes checkout UI. The merchant's application builds the cart and hands the shopper over.

### Model 3: headless anywhere

The merchant chooses its framework and hosting, calling one or several commerce platforms. Vercel's server-rendered Next.js Commerce template used Shopify as reference, with forks for other platforms; it has since moved to a successor repository, which shows how quickly the templates and tools at this layer change (accessed November 2026). Alokai's **unified data layer** normalizes several platforms' product data into one interface (docs accessed November 2026). A group can then share a front end across brands while retaining different commerce engines.

![Diagram: Three rendering models differ in who renders, who hosts and how many engines the front end can face](assets/images/32-storefront-architecture/fig02-three-rendering-models-differ-who-renders.jpeg)
**Figure 2:** *Three rendering models differ in who renders, who hosts and how many engines the front end can face; under all three the checkout stays on the platform.*

## Performance: What the Evidence Says, With Dates

Whichever model renders the page, its speed is measured the same way, and the agency's first promise was speed. **Core Web Vitals** are Google's three field metrics for page experience, measured from real visitors and assessed at the 75th percentile of page loads, mobile and desktop separately (web.dev, updated 31 October 2024): **largest contentful paint** (LCP, when the main content has loaded; "good" is 2.5 seconds or less), **interaction to next paint** (INP, how quickly the page responds to a tap or click; good is 200 milliseconds or less) and **cumulative layout shift** (CLS, how much the page jumps while loading; good is 0.1 or less).

INP replaced the older first-input-delay metric on 12 March 2024. Google's Search documentation says it "highly recommend[s]" good Core Web Vitals "for success with Search" and that they "align with what our core ranking systems seek to reward", without stating a weight (accessed November 2026).

The evidence that speed moves money is consistent in direction and weak in precision:

- **Deloitte Ireland for Google (24 March 2020; six years old):** across mobile sites in retail, travel, luxury and lead generation, a 0.1-second improvement in site speed went with +8.4% retail conversions and +9.2% retail average order value. Caveats the study carries: commissioned by Google, the number of sites not disclosed, and a correlation, not an experiment.
- **web.dev's case collection (undated, accessed November 2026):** Vodafone Italy improved LCP 31% and saw sales up 8%; Lazada tripled LCP speed and saw mobile conversion up 16.9%; Cdiscount improved all three metrics and reported +6% revenue in a Black Friday sale. Every case is a self-selected success story, and none separates speed from the redesign that came with it.
- **A vendor's admission (Shopify, accessed November 2026):** the theme-performance page says performance "directly influences conversion rates, repeat business, and search engine rankings" without citing a figure; the Theme Store requires a minimum average performance score of 60 in Lighthouse, Google's automated lab test of a page (unlike the field measurements above); public apps "shouldn't reduce Lighthouse performance scores by more than 10 points"; and the admin's performance report warns that theme code and apps "can slow down your site".

The honest reading: **faster is better, nobody can tell you by how much, and the usual culprit is not the rendering model but the scripts.** A rule that caps each app at ten points is a vendor admitting that apps are where storefront speed goes. Kestrel & Pine's INP of 310 milliseconds was eleven apps' scripts; the rendering model was innocent.

![A phone weighed down by eleven app boxes, with a stopwatch reading INP 310 ms beyond a 200 ms good mark, beside an innocent theme card.](assets/images/32-storefront-architecture/32-eleven-apps-weigh-down-the-page.jpeg)
**Figure 3:** *Kestrel & Pine's interaction to next paint of 310 milliseconds was eleven apps' scripts, not the rendering model; good is 200 milliseconds or less.*

## Accessibility Is a Requirement, Not a Performance Option

Speed is not the only requirement every page must meet. An accessible storefront lets people find products, understand choices and complete payment using the ways they interact with a device, including keyboards and screen readers. A fast page still fails its customer if a form or payment control cannot be used.

**WCAG 2.2**, the Web Content Accessibility Guidelines of the World Wide Web Consortium (W3C), is a Recommendation dated 12 December 2024, with three conformance levels (A, AA, AAA) and four principles (perceivable, operable, understandable, robust).

The **European Accessibility Act** (Directive (EU) 2019/882) applies to services "provided to consumers after 28 June 2025" and lists "e-commerce services" explicitly, defined as a service provided at a distance "with a view to concluding a consumer contract"; microenterprises (under 10 people and up to €2 million turnover) are exempt.

Kestrel & Pine, with 310 employees and three consumer storefronts, has been in scope since June 2025; its B2B portal, serving businesses, is not a consumer service. National enforcement differs; [[commerce-regulation]] owns the calendar.

Being in scope covers the whole purchase flow, not only the theme. An accessible theme can still contain an app block that a shopper cannot navigate or use. Apply accessibility criteria to both the theme and the inserted components, and test their combined purchase flow. The shopper needs to complete the whole task, whichever rendering model or supplier produced each piece.

## Cache the Shell, Fetch the Promise

Keeping pages fast and usable for every shopper on a peak day depends on one more decision: which answers on a page can be reused. Some page content can be computed once and served repeatedly; other answers depend on this shopper and the current purchase.

**Cacheable:** the product page's content, images, attributes and layout, per market and language; category pages; editorial pages; search facets to a degree. These change when the catalog or the campaign changes, not when a shopper arrives.

**Validate live:** account prices, stock commitments, cart and checkout. Public pages may carry price and availability snapshots with explicit freshness limits, but accepting an order must check current terms. Showing a stale price or stock answer is how the Price Drift and the Black Friday Oversell reached shoppers' pages. Never share account-specific answers across customers.

![A cached page shell stacked many times on the left, with a live price tag, stock badge and cart flying into empty slots on the page from the right.](assets/images/32-storefront-architecture/32-shell-and-promise-split.jpeg)
**Figure 4:** *Cache the shell, fetch the promise: the page content is computed once and served many times, while the price, the stock badge and the cart are fetched for this shopper, now.*

**Cache the shell, fetch the promise** means serving useful cached content, refreshing changing facts and validating purchase terms. Shopify's full-page cache supplies the platform-level mechanism.

At the headless layer the same idea appears as **incremental static regeneration**: Vercel's documentation (updated 28 August 2026) describes serving the cached page while regenerating it in the background on a timer or on demand, names e-commerce catalogs "that need current pricing and availability without rebuilding the entire site" as the first use case, collapses concurrent requests for an uncached page "into one function invocation per region, protecting your backend during traffic spikes", and serves stale content with a retry if regeneration fails.

Request collapsing is the peak-day feature: when 41 times the normal traffic hits one hero product at once, the backend sees one request, not thousands. On the 2026 peak night Kestrel & Pine's cached pages held at about 41 times the traffic of an average hour. The stock sync chain behind the stock badge did not: its scheduled copies took up to two hours to carry a sale from the warehouse system through the ERP to the shop platform and the channels.

![Diagram: Eva's product page arrives from the edge cache first](assets/images/32-storefront-architecture/fig03-eva-s-product-page-arrives-edge.jpeg)
**Figure 5:** *Eva's product page arrives from the edge cache first; the storefront then fetches the facts that must be true now, availability and price, and fills them in.*

### Requirements per page type

Applied to each page type, the rule sets how fresh, how consistent and how fast each part of the page must be, and what it does on a peak day.

| Page | How fresh | How consistent | How fast | On a peak day |
| --- | --- | --- | --- | --- |
| Product and category content | Minutes after a catalog publish | Same content in every channel (the PIM's job after W3, the decision to buy a PIM) | Cached at the edge; server response in tens of milliseconds *(assumption)* | Must be fully cacheable; request collapsing on misses |
| Price shown | Within the price change's effective time; [[pricing-architecture]] | One price per market and channel | Fetched live or cached for seconds, by market | Cache per market, never per shopper, for anonymous visitors |
| Stock badge and delivery promise | Seconds to a minute after a stock event *(assumption)* | Same answer the checkout will give | Fetched after the shell | Degrade to "in stock / out of stock" or hide the count ([[peak-load-and-reliability]]) |
| Search results | Minutes after a catalog publish | Index matches the catalog | Under 300 ms *(assumption)* | Fewer facets, simpler sorts |
| Logged-in B2B (business-to-business, wholesale) pages | Live | Contract price per account | Never cached across accounts | Rate-limited by account |
| Cart and checkout | Live | One cart per session; the checkout's rules win | Platform-owned | Never switched off |

## Technical SEO and Product Discoverability

Cached public pages have a second reader besides the shopper: search engines. A product can load quickly and still be hard to find before a shopper reaches the store. **Search-engine optimization (SEO)** helps people discover relevant pages through search engines. Its technical foundation is letting engines retrieve pages (**crawling**), understand them and include them in a searchable collection (**indexing**). The platform controls much of that foundation: links, rendered content, URLs and product data. [[commerce-search-and-discovery]] covers finding products once the shopper is inside the store.

Start with a path to every product you want found. Category pages and links between pages of results need ordinary HTML links, not only buttons that run scripts. A **sitemap** lists URLs the merchant wants search engines to discover; it complements navigation without guaranteeing indexing. Google generally does not submit searches into a store's search box, so being findable there is insufficient ([ecommerce navigation guidance](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure), accessed 9 November 2026).

### Make the rendered page and the product data agree

Google can execute JavaScript, but rendering is a separate processing step, and other crawlers may not. I would deliver useful product content in the initial HTML, including a descriptive page title, then enhance it in the browser. Google's [JavaScript guidance](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) supports server rendering or pre-rendering; headless alone provides no SEO advantage.

**Structured data** embeds named product facts in the page for machines: `Product` describes the item; `Offer` describes its price and availability. Google recommends putting product markup in the initial HTML because JavaScript-generated markup can be less reliable for shopping crawls ([merchant listing guidance](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)). Generate it from the same records as the visible page and product feed, the channel export described in [[product-information]].

The caching rule must serve search engines too. Public price and availability snapshots need a maximum age and coordinated updates in HTML, markup and feeds. A browser-only refresh can leave machines reading yesterday's price. Good markup makes a page eligible for richer search results; it does not guarantee them.

### Give each kind of page an explicit policy

Product variants, filters and translations multiply the URLs a platform can publish. Decide what each address means before exposing all of them to crawlers.

| Case | Platform decision and reason |
| --- | --- |
| Product variants | Use stable addresses that open the intended selection. A **canonical URL** is the preferred address for duplicate or equivalent content; `rel="canonical"` signals that preference. Keep internal links and sitemaps consistent with it. Google can choose a different canonical. |
| Filters and sorting | Size, color and sort combinations can create enormous numbers of low-value URLs. Choose useful landing pages to index and limit crawling of the rest, so new products get discovered without unnecessary server work. Canonical hints alone are not a dependable crawl limit. |
| Languages and countries | Give localized pages distinct URLs. **`hreflang`** annotations identify alternate language or regional versions. Each version names itself and its alternatives, helping Google choose the appropriate offer. |
| Temporary stockouts | Keep a useful product page available and update its visible availability and markup. A sell-out need not destroy the address shoppers may revisit when stock returns. |
| Moves and retirement | Use permanent `301` or `308` redirects for moved content or a genuine replacement. Keep useful discontinued-product information when warranted; if a page is removed with no suitable replacement, return `404` (not found) or `410` (gone). Sending every retired product to the homepage frustrates visitors. |

These policies follow Google's guidance on [ecommerce URLs](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites), [faceted navigation](https://developers.google.com/crawling/docs/faceted-navigation), [localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions) and [site moves](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes), checked 9 November 2026. Stockout handling above is an implementation recommendation: availability changes and page retirement are different events.

Two controls must stay distinct. **`robots.txt`** tells cooperating crawlers which URLs they may fetch. **`noindex`** tells a supporting search engine to exclude a fetched page from results. Blocking crawling can prevent Google seeing `noindex`; neither control protects private customer data ([indexing guidance](https://developers.google.com/search/docs/crawling-indexing/block-indexing)). Check that a release has not carried test-site exclusions into public product pages.

I would make the storefront team own these rules, with catalog and marketing owners choosing the intended landing pages. For Kestrel & Pine, a useful check would follow one jacket's localized pages and variants through a price change and a stockout. Inspect what Google receives with Search Console's URL Inspection, validate markup with its Rich Results Test, and monitor indexing, crawl errors and organic visits by landing page. Repeat after template changes; preserve the URL policy during [[replatforming-and-migration]].

## The Choices and Their Trade-Offs

Speed, accessibility, caching and discoverability can all be met on a theme, so the choice between rendering models rests on other needs. The realistic options for a merchant on a hosted platform are four: the three rendering models, with the theme split into two.

1. **The theme, disciplined.** Keep the platform's renderer; use sections and app blocks instead of edited templates; police app scripts with a performance budget; let the platform's cache and edge do the peak-day work.
2. **The theme plus a content system.** Keep the theme for commerce pages and feed editorial content from a CMS through the platform's content features or a small integration; the brand team gets its content model without a new renderer.
3. **Headless on the vendor's runtime.** Own the front end; let the vendor host it, serve the storefront API and run checkout. The team now owns rendering, caching rules and the glue to search, prices and availability.
4. **Headless anywhere, possibly over several engines.** Own everything in front of the APIs; add a unified data layer if several engines or brands sit behind one front end.

| Option | Who runs rendering and caching | Flexibility | Peak-day posture | Team it needs | When it is right |
| --- | --- | --- | --- | --- | --- |
| Theme, disciplined | The vendor | The template language and page types | The vendor's cache and edge; apps are the risk | One or two front-end engineers plus an agency | Starting through Omnichannel, unless a need below applies |
| Theme plus CMS | The vendor, plus a content feed | Content model of the CMS; commerce pages as the theme allows | As above | The same, plus editors | A content-led brand on a themed platform |
| Headless on the vendor runtime | The merchant renders, the vendor hosts | Full control of the front end; checkout stays the vendor's | The merchant's caching rules; request collapsing if used | Three or more front-end engineers who can own a production application | A design system shared across brands or countries; a B2B portal with account pricing that the theme cannot express |
| Headless anywhere | The merchant | Full, including several engines behind one front end | Entirely the merchant's | A front-end platform team | Group stage: several brands or engines behind one storefront |

Options 1 and 2 assume the platform's page types and checkout fit the business. I would choose headless only for one of three needs they cannot express: a shared design across brands, an editorially driven site, or a B2B portal's account pricing and approvals ([[b2b-commerce]]). Options 3 and 4 also require a team that owns on-call, caching, framework upgrades and [[api-contracts-and-versioning]] after the agency leaves. Speed alone establishes neither the need nor that operational capacity.

### Mobile apps and progressive web apps

The same rule applies to mobile apps, the other front end often proposed in speed's name. A **progressive web app** (PWA) is a website "built and enhanced with modern APIs" that can be installed like an app, work offline and send push notifications (web.dev, accessed November 2026). For a merchant it is mostly the headless question in disguise: the same server-rendered storefront can be made installable. A **native app** adds a second storefront that must show the same prices, stock and promises as the first, and is justified by loyalty, push and in-store features, not by speed.

## Across Scale Stages: When It Fits and When It Limits

| Stage | What is typical | What becomes necessary | Warning signs of outgrowing the approach |
| --- | --- | --- | --- |
| **1 — Starting** (Kestrel & Pine 2016–2018) | A purchased theme with light customization; a handful of apps; the platform's defaults for caching and delivery | Field measurements at the 75th percentile, read monthly; a rule that every app's script is justified | A theme edited by hand "just this once"; LCP drifting past 2.5 seconds after each app install |
| **2 — Growing** (2019–2022) | An agency-customized theme; two or three storefronts for countries; thirty apps; the first content pages fought over by brand and engineering | A performance budget per page type; sections and app blocks instead of edited templates; a content model decision (theme sections or a CMS) | Theme updates skipped because the merge is painful; brand asking for page types the theme lacks; a headless proposal arriving before any need is measured |
| **3 — Omnichannel** (2023–now) | Several localized storefronts in one tenant; a B2B portal; forty apps; a peak hour many times normal; accessibility obligations in force since June 2025 | Cacheability per page type as a design rule; the stock badge and the delivery promise fed by the availability service (W1) and the shipping service rather than static text; an app-script audit each quarter; accessibility testing on theme and app blocks; a headless decision made against the three needs, not the pitch | Peak-day slowness traced to uncacheable pages; the B2B portal needing account logic the theme cannot express; a second brand or a native app that must share the design system |
| **4 — Group** | Several brands or engines; a front-end platform team; design systems; possibly a unified data layer over several commerce engines | One front-end platform (framework, design system, normalization layer) across brands; headless as the shared surface, with each brand's engine behind it; a performance and accessibility standard enforced across brands | Each brand running its own storefront stack; a group-wide campaign needing five implementations; the One Size Fits None pattern when a brand with a different model is forced onto the shared front end |

I would retain the theme while it meets the requirements. Group scale makes a shared front end more valuable; Omnichannel scale alone does not establish a reason to build one.

## In Practice

### Kestrel & Pine: why Noor said no, and what she said yes to

Kestrel & Pine is at the Omnichannel stage, where the table above keeps the disciplined theme unless one of the three needs applies. Noor's answer to the agency in late February 2027 had four parts, recorded as a short decision note that later folded into Waypoint's W4 (stay and surround; no replatforming, with the platform's own point-of-sale (POS) system evaluated in 2028 and the whole decision revisited in 2029).

1. **The speed argument did not survive measurement.** LCP 2.1 seconds and CLS 0.08 were already "good"; INP of 310 milliseconds was the problem, and it was app scripts. The agency's retainer was redirected for one quarter to a theme performance pass and an app-script audit, run alongside the app governance review of April 2027 ([[extensibility-and-app-ecosystems]]). By June 2027 INP on product pages measured 180 milliseconds (illustrative), inside the threshold, after six unused apps and four redundant scripts were removed.
2. **The content argument was real, and headless was the wrong remedy.** Teun Baas's brand team wanted seasonal guides and stories that the theme's page types handled badly. The remedy was option 2: theme sections for commerce pages, and a content model that waits for the PIM (W3, Q3 2027) so product stories draw on one product record rather than one more copy of the product text.
3. **"Ready for the future" named no need.** None of the three needs applied. One brand and its three countries share one design; the content need was met by option 2; and the platform's B2B features already serve the portal, through which 62% of wholesale orders arrive. There was no native app either. A headless rebuild would have been the Giant's Boots: an architecture borrowed from brands with front-end teams of fifty, run by three engineers who also own the apps.
4. **The peak-day argument pointed the other way.** The 2026 peak hour (2,300 orders, with storefront traffic about 41 times an average hour) was survived by the platform's cache; what failed was the stock sync chain behind the badge. The fix for the badge is the availability service (W1), not a new renderer. Until W1 lands in Q4 2027, the 2027 peak plan hides the stock count on product pages and shows "in stock / low stock" from a per-channel buffer ([[peak-load-and-reliability]], [[journey-peak-day]]).

What she said yes to cost about €38,000 of agency time over the quarter (illustrative) instead of €240,000 and nine months, and left the storefront on the one rendering model her team can run. The decision is revisited at the 2029 review together with the POS question, because the one need that could change the answer, a second brand or an app for store staff sharing the design system, is a Group-stage question Kestrel & Pine has not yet reached.

### Dated public examples

For a merchant whose need does justify a new storefront, two public examples give checks before switching.

- **Compare before switching traffic.** Shopify's renderer rollout (2020–2022) compared old and new status codes, headers and bodies on sampled production traffic, with fallback to the old path. That provides a concrete check for a merchant replacing its storefront.
- **Test regeneration failures before the peak.** Vercel documents request collapsing and serving stale content after failed regeneration (28 August 2026). A merchant choosing its own hosting should demonstrate those behaviors with its own product pages.

Whatever renders the pages, two things from earlier sections still need checking: checkout stays on the platform, and the whole purchase flow, theme and app blocks together, must still work for every shopper.

## When It Goes Wrong

Not every storefront decision goes as Noor's did. Seven failures recur, each with a sign to detect it and a recovery; six break one of this chapter's rules. The Forked Platform appears here as the forked theme and The First Snowfall as the uncacheable peak; The Giant's Boots was Noor's third point. One row is new: bots, meaning crawlers and AI agents that read the catalog.

| Failure | What it looks like | Detection | Recovery |
| --- | --- | --- | --- |
| **A cached promise** | A price change or a sell-out shows on the page minutes or hours after the fact; a shopper buys at the old price or orders the last unit twice | Compare what the page showed with what checkout computed; the Price Drift and the Oversell are both this | Bound public snapshot age, update on change and validate live purchase terms; keep visible content and markup aligned |
| **The uncacheable peak** | Pages that depend on a per-shopper fact are rendered fresh for every visitor; the renderer or the APIs behind it saturate at 41 times normal | Cache hit rate per page type in the load test ([[peak-load-and-reliability]]) | Make product and category pages cacheable per market; collapse requests on misses; degrade the badge |
| **Script sprawl** | INP and LCP drift with every app install; checkout steps slow or break when a script errors | Field metrics at the 75th percentile, monthly; the platform's app performance rule | A performance budget; the quarterly app-script audit; app blocks instead of injected scripts |
| **The forked theme** | Theme updates skipped for years; security and feature updates unavailable; every change a merge | The gap between the installed and the current theme version; the count of hand-edited templates | Rebuild the customizations as sections and app blocks on a current theme; treat the theme like code, with versions |
| **The headless storefront that drifted** | A front end pinned to an old storefront API version breaks on the vendor's retirement date; a framework upgrade stalls for a year | The API version on the integration card ([[api-contracts-and-versioning]]); the framework's support calendar | Treat the storefront as the integration it is: an owner, a version pin, an upgrade calendar |
| **Bots at the front door** | Crawlers and AI agents read the catalog at a rate that costs money or starves real shoppers; Commerce.com's (formerly BigCommerce) second-quarter 2026 filing reported lower gross margin, and an earnings-call summary attributed part of it to hosting costs from AI crawlers and agents (6 August 2026) | Traffic by source; the storefront API's bot limits (Shopify limits bots "most strictly when unsigned") | Bot rules and signed agent access; a catalog feed for agents instead of page scraping ([[ai-and-agentic-commerce]]) |
| **An inaccessible storefront** | A complaint or an enforcement notice under the Accessibility Act; checkout unusable with a screen reader | Automated and manual WCAG 2.2 testing of theme and app blocks | Fix in the theme and in every app block; add accessibility to the app review on the governance card |

## What to Take Away

The slow product page at the start of this chapter has one answer. The storefront owns templates and scripts, not facts, so the cause of a slow page is found by measuring it in the field and tracing the slow metric. At Kestrel & Pine that led to eleven apps' scripts, not to the renderer, and a new page would have carried the same scripts. The same split decides the rest: what is the same for many shoppers is cached and shown to search engines, what is a promise is fetched or checked live, and the renderer changes only for a need the theme cannot meet, with a team to run it.

**Established.**

- Core Web Vitals measure real-user experience. The cited conversion studies support improving speed, without predicting a merchant's exact revenue gain.
- The hosted-platform models discussed here keep checkout on the commerce platform; both full-page caching and incremental regeneration have documented implementations.
- Search discovery depends on crawlable pages and consistent product information. Good performance alone does not supply them.
- The European Accessibility Act applies to consumer e-commerce services since 28 June 2025; theme and app components both need assessment.

**Depends on context.**

- Headless needs both a requirement the theme cannot meet and a team able to operate the result.
- Editorial needs may be met by theme sections or a CMS feeding the theme; a content requirement does not automatically require a new renderer.
- Cache policy follows the business model: public pages can share market-specific snapshots; private account prices cannot be shared across customers.

**The author's synthesis.**

- I would decide ownership, freshness and product discoverability before the framework. A renderer must serve shoppers and expose useful public pages to search engines.
- I would ask a headless proposal to identify the unmet requirement and its operating owner. Noor's measurements justified improving the existing theme and availability service.

## Questions to Ask

1. What do the field Core Web Vitals say at the 75th percentile on mobile for the product and category pages, and when were they last read?
2. Which rendering model is in use, who runs the renderer, and who is on call when it fails on a Friday evening in November?
3. Which facts on the product page are cached, for how long, and which are fetched live; is the stock badge one of the live ones?
4. How many hand-edited theme templates exist, and when was the theme last updated from the vendor's version?
5. How many apps add scripts to the storefront, and what is the performance budget each must meet?
6. If a headless storefront is proposed, which of the three needs (shared front end, content-led site, B2B portal) does it serve, and who will run it in year two?
7. Which storefront API version does the front end target, and when does that version leave support?
8. Has the storefront, including every app block and the checkout, been tested against WCAG 2.2, and who owns the result?
9. What does the page show for stock and delivery when the availability service or the shipping service is down?
10. Can search engines discover the intended product pages, and who checks their rendered data, localized URLs and retirement rules after a release?

On the 2026 peak night this storefront held, because its pages could be cached. The chain behind it did not: orders reached the warehouse hours late, and a sale took up to two hours to reduce the stock shown on other channels. That chain belongs to the merchant, and no shared platform cache absorbs its load. The next chapter is about it: how to size, test, protect and recover it. Continue with [[peak-load-and-reliability]].

## Sources and Evidence

*Company, product and investor sources*

- [How Shopify Reduced Storefront Response Times with a Rewrite](https://shopify.engineering/how-shopify-reduced-storefront-response-times-rewrite), Shopify Engineering (Maxime Vaillancourt), 20 August 2020 — the Storefront Renderer, its three cache layers, the 4x–6x result and the verifier-and-fallback rollout; six years old.
- [Cloud, Load, and Modular Code: What 2022 Looks Like for Shopify](https://shopify.engineering/cloud-load-modular-code-shopify-2022), Shopify Engineering, 20 January 2022 — the renderer deployed in regions without the monolith.
- [Shopify Unite 2021 announcements](https://www.shopify.com/in/partners/blog/shopify-unite-announcements-2021), Shopify Partners blog, 29 June 2021 — Online Store 2.0, JSON templates and sections, theme app extensions, Hydrogen and Oxygen previewed.
- [Shopify Editions](https://www.shopify.com/partners/blog/editions), Shopify Partners blog, 9 February 2023 — Oxygen hosting on the Basic, Shopify, Advanced and Plus plans at no extra cost.
- [Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen), shopify.dev, documentation version 2026-10, accessed 2026-11 — Hydrogen as a toolkit, the APIs it covers, no checkout UI, the React Router 7 starter and Oxygen.
- [Storefront API](https://shopify.dev/docs/api/storefront), shopify.dev, n.d., accessed 2026-11 — access modes, no fixed limit for real buyers, bots limited most strictly when unsigned, versioned paths.
- [Theme performance best practices](https://shopify.dev/docs/storefronts/themes/best-practices/performance), shopify.dev, n.d., accessed 2026-11 — Core Web Vitals as a ranking signal, the Lighthouse 60 minimum, app scripts.
- [App requirements checklist](https://shopify.dev/docs/apps/launch/app-requirements-checklist), shopify.dev, n.d., accessed 2026-11 — the ten-point Lighthouse rule for public apps.
- [Web performance](https://help.shopify.com/en/manual/online-store/web-performance), Shopify Help Center, n.d., accessed 2026-11 — theme code and apps as what can slow a site.
- [Stencil](https://docs.bigcommerce.com/docs/storefront/stencil/start), BigCommerce developer documentation, n.d., accessed 2026-11 — the Handlebars-based theme engine.
- [PWA Kit](https://github.com/SalesforceCommerceCloud/pwa-kit), Salesforce Commerce Cloud, GitHub, n.d., accessed 2026-11 — the React storefront on a Managed Runtime.
- [Adobe Commerce as a Cloud Service overview](https://experienceleague.adobe.com/en/docs/commerce/cloud-service/overview), Adobe Experience League, 20 October 2026 — the headless Commerce Storefront on Edge Delivery Services as the only storefront.
- [Adobe Commerce Storefront](https://experienceleague.adobe.com/developer/commerce/storefront/), Adobe Experience League, n.d., accessed 2026-11 — drop-in components and document-based authoring.
- [Next.js Commerce](https://github.com/vercel/commerce), Vercel, GitHub, n.d., accessed 2026-11 — the server-rendered template, its platform forks, and its archiving.
- [Incremental Static Regeneration](https://vercel.com/docs/incremental-static-regeneration), Vercel documentation, updated 28 August 2026 — stale-while-revalidate, the e-commerce use case, request collapsing and failure behavior.
- [Unified Data Layer](https://docs.alokai.com/unified-data-layer), Alokai documentation, n.d., accessed 2026-11 — normalizing product data across platforms.
- [Commerce.com, Form 8-K exhibit 99.1, second quarter 2026 results](https://www.sec.gov/Archives/edgar/data/0001626450/000119312526336701/bigc-ex99_1.htm), U.S. Securities and Exchange Commission, 6 August 2026 — revenue and gross-margin figures; the attribution of hosting costs to AI crawlers comes from an earnings-call summary ([Nasdaq](https://www.nasdaq.com/articles/cmrc-q2-earnings-call-flags-softer-b2c-demand-outlook-cut), 2026), not from the exhibit.

*Standards, regulation and official documentation*

- [Ecommerce site navigation](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure) and [Ecommerce URL structure](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites), Google Search Central, n.d., accessed 2026-11-09 — product discovery, links, sitemaps and URL consistency.
- [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) and [Merchant listing structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing), Google Search Central, n.d., accessed 2026-11-09 — rendering and product markup in initial HTML.
- [Managing crawling of faceted navigation URLs](https://developers.google.com/crawling/docs/faceted-navigation), Google Crawling Infrastructure, n.d., accessed 2026-11-09 — filter combinations and crawl costs.
- [Block indexing with noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing) and [Localized versions of pages](https://developers.google.com/search/docs/specialty/international/localized-versions), Google Search Central, n.d., accessed 2026-11-09 — indexing controls and language or regional alternatives.
- [Site moves and migrations](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes), Google Search Central, n.d., accessed 2026-11-09 — relevant redirects, removed content and monitoring.
- [Web Vitals](https://web.dev/articles/vitals), web.dev (Google), updated 31 October 2024 — the three metrics, their thresholds and the 75th-percentile rule.
- [Interaction to Next Paint becomes a Core Web Vital on March 12](https://web.dev/blog/inp-cwv-march-12), web.dev, 2024 — INP replacing first input delay.
- [Understanding Core Web Vitals and Google search results](https://developers.google.com/search/docs/appearance/core-web-vitals), Google Search Central, n.d., accessed 2026-11 — "highly recommend" and alignment with ranking systems, without a weight.
- [What are Progressive Web Apps?](https://web.dev/articles/what-are-pwas), web.dev, n.d., accessed 2026-11 — the PWA definition.
- [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/), W3C Recommendation, 12 December 2024 — levels, principles and the current edition.
- [Directive (EU) 2019/882, the European Accessibility Act](http://publications.europa.eu/resource/celex/32019L0882), Publications Office of the European Union, 7 June 2019 — e-commerce services in scope, application from 28 June 2025, the microenterprise exemption.

*Research and practitioner sources*

- [Milliseconds Make Millions](https://www.deloitte.com/ie/en/services/consulting/research/milliseconds-make-millions.html), Deloitte Ireland for Google, 24 March 2020 — the 0.1-second study and its caveats; six years old.
- [The business impact of Core Web Vitals](https://web.dev/case-studies/vitals-business-impact), web.dev, n.d., accessed 2026-11 — the self-reported case studies quoted as illustrations.

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
