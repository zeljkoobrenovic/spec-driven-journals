{class: part, id: part-7}
# Part VII — PLATFORM: How Commerce Platforms Are Built

![Part VII — PLATFORM: How Commerce Platforms Are Built — logo](commerce-platform-architecture/posts/part-7-intro/assets/images/part-7-intro/logo.jpeg)

> **IN THIS PART, YOU WILL:** Open the platform a merchant rents: how it is structured inside, how it is shared among thousands of merchants, what apps may touch, how a page reaches the shopper's phone, and how the chain behind it survives forty times the normal load.

> **KEY POINTS:**
>
> * **The platform's internals are the vendor's; the code around it is yours.** Amazon split at a scaling wall in 2001, Zalando for team autonomy in 2015, and Shopify refused to split; every account describes thousands of engineers. A merchant's own code needs one deployment unit per team that must release independently, and for most merchants that is one.
> * **Renting a shared system means governing your share of it.** A hosted platform keeps its tenants apart with identifiers, pods and rate limits; the limit is what the merchant meets, a budget of calls per app per store that every installed app spends from. Every app is an integration with an owner, a scope and at most one writer per fact.
> * **The storefront renders facts it does not own, and the peak is where that shows.** Cache the page, fetch the price and the stock live, and go headless only for a need the theme cannot meet. The platform smooths its peak across tenants; the merchant's connectors see the full spike, so measure the chain in orders per minute, queue everything behind the order, and reconcile the morning after.

> **[FAILURE PATTERNS THIS PART ADDRESSES](#where-commerce-platforms-go-wrong):**
>
> * **The Giant's Boots** — a microservices rebuild or a headless storefront copied from a company with thousands of engineers, by a merchant with nine.
> * **The Forked Platform** — a core or a theme customized so deeply that every vendor release is a project.
> * **The Secret Agent** — an app that writes stock, prices or orders without a named owner, because app review protects the platform, not the merchant's facts.
> * **The First Snowfall** — the API budget, the vendor's shared capacity and the hand-built order flow meet real load for the first time on the busiest evening of the year.

Every part so far has treated the platform as a box with a name on it. **This part opens the box.** A merchant paying €2,300 a month for an enterprise subscription rents a slice of a system that one vendor runs, on one version, for thousands or millions of shops at once. That is why the subscription is cheap and why the checkout holds on Black Friday. It is also why the merchant cannot change the platform's structure, cannot see which pod (isolated group of databases) its shop lives on, and gets a budget of API calls rather than a server. What the merchant owns is everything around the box: the integration code, the apps, the theme and its scripts, and the chain that carries each order to the warehouse and the stock back.

Part VII sits under the order's path rather than at one step of it. Its storefront chapter is the first step of Eva Janssen's jacket, the product page she opened at 21:14 on 13 April 2027; its peak chapter asks what happens to that order when two thousand other shoppers place theirs in the same hour. The three chapters between them are the machinery the order runs on: how the platform is structured, how it is shared, and how other people's code changes it.

Kestrel & Pine, the fictional outdoor brand this book follows, met four platform questions in Noor Visser's first months: an outside consultancy's composable rebuild of about €3.2 million, the agency's headless storefront (a separate front-end application fed by the platform's APIs) of about €240,000, a board member's question whether it was "behind" for keeping a monolith (one program, one database), and forty-one installed apps with nobody's name on them. **The claim of this part is that the rebuild proposals would have replaced the part that held on 27 November 2026 and left the joins that failed to "phase two".** The platform served 2,300 orders in the peak hour; the hand-built order flow behind it carried about seven a minute, and the stock copied back around the loop was up to two hours old. With nine engineers, the attention belonged on the merchant's own layer, and the five chapters say how.

![Illustration: a chain whose large platform link holds while the thin order-flow and stock-copy links fray, and a consultant aims a hammer at the strong link.](commerce-platform-architecture/posts/part-7-intro/assets/images/part-7-intro/part-7-strong-box-weak-joins.jpeg)

**Figure 1:** *On 27 November 2026 the rented platform held at 2,300 orders in the peak hour; the merchant's own joins, an order flow of about seven orders a minute and stock up to two hours old, were the weak links the rebuild proposals left for phase two.*

![Diagram: A merchant on a hosted platform rents the renderer, the checkout and a share of a multi-tenant system, and owns the theme, the apps and the integration code around them](commerce-platform-architecture/posts/part-7-intro/assets/images/part-7-intro/fig01-merchant-hosted-platform-rents-renderer-checkout.jpeg)

**Figure 2:** *A merchant on a hosted platform rents the renderer, the checkout and a share of a multi-tenant system, and owns the theme, the apps and the integration code around them; the owned layer and the budget it spends are where the peak day is won or lost.*

![Diagram: The five questions of Part VII in reading order, from the inside of the platform outward to the day it is tested](commerce-platform-architecture/posts/part-7-intro/assets/images/part-7-intro/fig02-five-questions-part-vii-reading-order.jpeg)

**Figure 3:** *The five questions of Part VII in reading order, from the inside of the platform outward to the day it is tested; each answer narrows what a merchant should treat as its own.*

{id: part-7--chapters-in-this-part}
## Chapters in this part

[Monolith, Modular Monolith, Microservices, Composable: What the Evidence Says](#commerce-architecture-styles) decides **how a commerce system should be structured inside, and what the famous examples really show**: the four styles differ in how many separately deployed pieces exist and who owns the joins, and the rule is one deployment unit per team that must release without waiting for another. The case is the April 2027 board question "did we choose right?" and Noor's May memo: one storefront codebase and one integration service with a module per flow, against a rebuild of about a dozen services for nine engineers.

[Many Merchants, One Platform: Multi-Tenancy, Pods and Isolation](#multi-tenancy-and-isolation) decides **how a hosted platform serves thousands of merchants on shared systems, and why a merchant should care**: pool, silo and bridge (shared, dedicated or mixed arrangements of tenants), pods and regions, and the rate limit, a budget per app per store that every app spends from and the vendor may lower under load. The case is Ruben Alves's June 2027 reading of the Black Friday logs: nine spenders of one budget, the stock-writing apps and the marketplace sync taking about 55%, the order flow 20% and throttled about 1,900 times, against a WMS limit of about 30 calls a minute.

[Apps, Plugins and Functions: Extensibility and Ecosystem Governance](#extensibility-and-app-ecosystems) decides **how platforms let other people's code change them, and how a merchant should govern the apps it installs**: five mechanisms differ by where the code runs and what it may touch, and app review never tells a merchant which two of its apps write the same fact. The case is the April 2027 spreadsheet, 41 apps, 6 unused, 3 writing stock, and the governance rule (an owner per app, scopes on a card, one writer per fact, a quarterly uninstall review) that left 34 apps by July.

[Delivering the Storefront: Themes, Headless, Rendering and Performance](#storefront-architecture) decides **how the storefront reaches the shopper's phone, and when headless is worth it**: a storefront renders facts other systems own, the checkout stays on the platform under every rendering model, and headless is justified by a shared front end, a content-led site or a B2B portal, never by speed alone. The case is the agency's February 2027 headless proposal, declined after measurement: the page's main content loaded in 2.1 seconds and its layout barely shifted, both already good by Google's thresholds, while its response to a tap (310 milliseconds) was slowed by scripts from eleven apps, down to 180 by June after a €38,000 theme pass.

[Black Friday Every Year: Peak Load, Resilience and Recovery](#peak-load-and-reliability) decides **how to prepare a platform and its integrations for a day with forty times the normal traffic**: measure every link in orders per minute, load-test the connectors with marked orders, queue everything behind the order, write a switch-off ladder on which checkout, payment and the order record never appear, and name who reconciles what the morning after. The case is the post-mortem of 27 November 2026 (31,000 orders in the week, the order flow four hours behind, 1,340 units oversold) and the 2027 plan: 60 orders a minute forecast, every link tested at 80, eight rehearsed switches, a freeze from 15 November, a situation room and a reconciliation report at 08:00 on Saturday.

Begin with [Monolith, Modular Monolith, Microservices, Composable: What the Evidence Says](#commerce-architecture-styles).

{id: part-7--sources-and-evidence}
## Sources and Evidence

Every public claim in this part is sourced and dated in the chapter that makes it, under that chapter's Sources and Evidence. Kestrel & Pine is fictional; recommendations and labeled assumptions are the author's judgement.
