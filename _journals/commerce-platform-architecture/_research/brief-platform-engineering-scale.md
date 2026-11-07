# Research brief: Platform engineering at scale — architecture styles, multi-tenancy, extensibility, storefront delivery, peak load, and team practice

Prepared 7 November 2026 for chapter writers of *ORDERED: Architecting Commerce Platforms*. The brief feeds chapters 11 (checkout, lightly), 29 (architecture styles), 30 (multi-tenancy), 31 (extensibility), 32 (storefront), 33 (peak load) and 44 (organizing engineering). It is platform-neutral: Shopify appears only where its engineering blog is the clearest public evidence of a pattern; the separate `brief-shopify` covers Shopify in depth, and writers should prefer the other companies' evidence here where it exists.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (7 November 2026) and supports the claim. Paraphrases stay close to the source and quoted text is quoted. The date is the publication date; undated product or documentation pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, an official blog relaying a document, a search summary) rather than from the primary document fetched in this session.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about how a proprietary system works internally falls here unless the company has described it in a fetched source.

**Evidence age matters.** Engineering blogs describe the system as it was on the day of writing. Several load-bearing sources here are old: Conway (1968), Vogels at Amazon (2006), Lewis and Fowler (2014–2015), Netflix (2016), Segment (2018), Shopify pods (2018), Zalando (2019–2020), Uber (2020), the Deloitte speed study (2020). Each is flagged **(evidence age)** where it appears; treat them as evidence that the pattern existed and worked at that date, not as a description of today's system.

**Research limitation.** Several primary pages blocked automated fetching (HTTP 403): the ACM Queue text of the 2006 Vogels interview, Salesforce's developer documentation (B2C Commerce cartridges, sandboxes), DoorDash's engineering blog, Etsy's Code as Craft, and the Internet Archive. The original Prime Video 2023 post has been taken down and is reported through InfoQ. The PagerDuty post often cited for "Amazon alerts on orders per second" could not be found at any live URL and is **not** used. Shopify App Store counts come from Shopify's store front page (a round marketing number), not from a filing. No public figure for Amazon's or Zalando's current service count was found. Dutch and Belgian practitioner sources on commerce engineering teams were not found; Part 6 therefore leans on general sources plus judgement.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: rate limits, plan names, API versions, app counts, support dates, AI-tooling findings.

---

## PART 1: Architecture styles, with the evidence behind the famous examples

### 1.1 Vocabulary

| Style | What it means in one sentence | Canonical public example (date) |
| --- | --- | --- |
| Monolith | One deployable application holding all the domains; one database, one release | Zalando's Java "Jimmy" shop 2010–2014; Shopify's Rails core (still) |
| Modular monolith | One deployable, but with enforced boundaries between domains inside it | Shopify 2019–2024 (Packwerk); Medusa's module layout |
| Microservices | Many independently deployable services, each owning its data, organized around business capabilities | Amazon from ~2001 (described 2006); Netflix 2008–2016; Zalando from 2015 |
| Composable / MACH | A commerce stack assembled from separately bought, API-first SaaS services | commercetools and the MACH Alliance vendors |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis of the sources in 1.2–1.9.

### 1.2 Amazon: services and "you build it, you run it" (2006)

- The ACM Queue conversation between Jim Gray and Werner Vogels (May 2006) is the primary text in which Amazon's CTO describes the move from a monolithic application to a service-oriented architecture with small teams owning services end to end. The text itself returned HTTP 403 in this session [WIDELY REPORTED: https://queue.acm.org/detail.cfm?id=1142065, 2006] **(evidence age: 20 years)**.
- AWS's own blog relayed the interview the week it appeared: Vogels' line "You build it, you run it", and his argument that giving developers operational responsibility improved service quality for customers and for the technology, replacing the older hand-off from development to operations [VERIFIED: https://aws.amazon.com/blogs/aws/acm_queue_inter, published 2006-05-16].
- Conway's 1968 thesis, which every later source leans on: "organizations which design systems ... are constrained to produce designs which are copies of the communication structures of these organizations" [VERIFIED: https://www.melconway.com/Home/Committees_Paper.html, published 1968-04 (Datamation)].

### 1.3 Netflix: seven years from monolith to cloud microservices (2008–2016)

- Netflix's migration began after an August 2008 database corruption stopped DVD shipping for three days; it finished in early January 2016 when the last streaming data-centre components were shut down. Netflix "split a monolithic application into hundreds of microservices", used denormalized NoSQL data models, and moved from centralized release coordination to continuous delivery by DevOps teams; streaming members grew eightfold and viewing by three orders of magnitude over the same eight years [VERIFIED: https://about.netflix.com/en/news/completing-the-netflix-cloud-migration, published 2016-02-12] **(evidence age: 10 years)**.
- [ASSUMPTION/JUDGEMENT] Netflix is not a commerce platform; it is cited because it is the best-documented case of a company taking seven years to finish the move, which is the duration a merchant should expect to hear quoted and discount.

### 1.4 Zalando: microservices in 2015, standardization afterwards

- Zalando adopted "Microservices, API First, REST, Cloud, Software as a Service" as its technology principles in March 2015; the repository is now marked deprecated and says the principles "no longer reflect the current reality (2020) in all aspects" [VERIFIED: https://github.com/zalando/engineering-principles, n.d., accessed 2026-11].
- Henning Jacobs' decade retrospective: Zalando began as a PHP/MySQL (Magento-stack) shop, rewrote it in Java/Spring/PostgreSQL in summer 2010 because the Magento stack hit scaling limits, built in-house ZEOS order and payment services in 2012 to replace the ERP, moved to AWS with containerized REST/OAuth microservices under "Radical Agility" in 2015, introduced Kubernetes in 2017, and by 2020 had more than 260 engineering teams, more than 1,300 developers, more than 4,000 applications and 140+ Kubernetes clusters. He reports that team autonomy over technology produced "similar CRUD REST services written in six languages", which "hurts productivity at scale", that fun service names created cognitive overhead, and that a standard microservice stack would have been "a major win"; in 2020 Zalando still dealt with monoliths from 2010 and some functionality was implemented twice [VERIFIED: https://srcco.de/posts/one-decade-in-zalando-tech.html, published 2020-03-03] **(evidence age: 6 years)**.
- Zalando's RESTful API Guidelines explain the later discipline: "API First" means microservice development begins with an API specification outside the code plus a peer review; the guild's goal is a "consistent API look and feel" so that "Ideally, all Zalando APIs will look like the same author created them" [VERIFIED: https://opensource.zalando.com/restful-api-guidelines/, n.d., accessed 2026-11].
- The "Radical Agility" talks by Jan Löffler (DevOps Con and code.talks 2015) and Rodrigue Schaefer's "From monolith to microservices at Zalando" (microXchg 2016) are the dated public talks for the 2015 move [WIDELY REPORTED: https://gotopia.tech/sessions/7/from-monolith-to-microservices-at-zalando, 2016].

### 1.5 The modular monolith: Shopify's documented path, and Medusa's layout

- Shopify, February 2019: the codebase was one of the largest Rails applications, worked on for over a decade by more than 1,000 developers, with about 6,000 Ruby classes. A modular monolith keeps all code in one application with "strictly enforced boundaries between different domains". Microservices were rejected because they would add multiple test and deployment pipelines, infrastructure per service, and network calls that add latency and reduce reliability; the team "wanted more modularity without more deployment units". Code was regrouped from models/views/controllers into business components (orders, shipping, inventory, billing), and an in-house tool, Wedge, scored each component's isolation from a CI call graph. The isolation work later made it possible to replace a legacy tax engine [VERIFIED: https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity, published 2019-02-21] **(evidence age: 7 years)**.
- Shopify, September 2020: the core monolith had "over 2.8 million lines of Ruby code and 500,000 commits", 37 components, Packwerk in use on about a third of them, an Architecture Guild of about 400 members; services are split out "only for good reasons" (examples: storefront rendering, credit-card vaulting) because a distributed system adds considerable complexity [VERIFIED: https://shopify.engineering/shopify-monolith, published 2020-09-16] **(evidence age: 6 years)**.
- Shopify's Packwerk retrospective, February 2024: Packwerk (released September 2020) is a static checker of constant references that enforces a package dependency graph, recording existing violations in `package_todo.yml` so new ones are blocked. What worked: isolating a base "Platform Essentials" package with zero violations and zero dependencies, held by CI. What did not: privacy checks pushed teams into API design instead of dependency management and were removed in Packwerk 3.0; semantic (domain) grouping often conflicted with how code runs at runtime; `require`/`autoload`, routes, fixtures and initializers are blind spots, so "a package can show zero violations and still fail at runtime". The team is shifting from domain components to functional packages and has discussed removing Packwerk. Quoted lessons: "Packwerk is a sharp knife, and it must be wielded with care" and "running code, more than any metric, will always be the best indicator of real progress" [VERIFIED: https://shopify.engineering/a-packwerk-retrospective, published 2024-02-07].
- Medusa (open-source, Node) documents a layered single application: an HTTP layer on Express.js, workflows holding the business logic, domain modules each connecting to PostgreSQL, replaceable commerce modules for providers (e.g., a Payment Module Provider for Stripe), and infrastructure modules (cache, event, locking, notification, workflow engine). It is headless: storefront and admin consume API routes [VERIFIED: https://docs.medusajs.com/learn/introduction/architecture, n.d., accessed 2026-11]. [ASSUMPTION/JUDGEMENT] This is a modular monolith by construction; the page does not say whether modules may depend on each other directly.

### 1.6 "Monolith first", the trade-offs, and the costs that are easy to miss

- Lewis and Fowler's definition (March 2014): an application built as a suite of small services, each in its own process, communicating by lightweight mechanisms (often HTTP), "organized around business capabilities", independently deployable, with decentralized data ("Microservices prefer letting each service manage its own database") and therefore eventual consistency and compensating operations. The authors are explicit that "we aren't arguing that we are certain that microservices are the future direction", that remote calls force coarser APIs, that refactoring across service boundaries is harder, and that splitting can move complexity "into the connections between them" [VERIFIED: https://martinfowler.com/articles/microservices.html, published 2014-03-25] **(evidence age: 12 years)**.
- Fowler, "MonolithFirst" (June 2015): start with a monolith even if you expect to need microservices; "the premium of microservices is a drag you should do without" early on, and "even experienced architects working in familiar domains have great difficulty getting boundaries right at the beginning" [VERIFIED: https://martinfowler.com/bliki/MonolithFirst.html, published 2015-06-03].
- Fowler, "Microservice Trade-Offs" (July 2015): benefits are strong module boundaries, independent deployment and technology diversity; costs are distribution (remote calls slower and failure-prone), eventual consistency ("Microservices introduce eventual consistency issues because of their laudable insistence on decentralized data management") and operational complexity ("There's just no way to handle dozens of services without the automation and collaboration that continuous delivery fosters") [VERIFIED: https://martinfowler.com/articles/microservice-trade-offs.html, published 2015-07-01].

### 1.7 Microservices at scale: Uber's Domain-Oriented Microservice Architecture (2020)

- Uber had about 2,200 critical microservices in 2020. Problems listed: a root-cause investigation could run through about 50 services owned by 12 teams; latency spikes cascade through deep dependency chains; a simple feature needed 10 touchpoints across teams; ownership blurred into "networked monoliths" that must be deployed together; microservices had a half-life of about 1.5 years. DOMA groups services into about 70 domains, each behind a gateway, in five layers (infrastructure, business, product, presentation, edge) with extension points. Reported results: platform support costs often dropped by an order of magnitude, feature onboarding time fell 25–50%, one integration dropped from three days to three hours [VERIFIED: https://www.uber.com/blog/microservice-architecture/, published 2020-07-23] **(evidence age: 6 years)**.
- [ASSUMPTION/JUDGEMENT] Uber is not commerce, but its numbers are the clearest public statement of the cost side at the far end of the scale: the gateways and layers DOMA adds are the modular-monolith disciplines (boundaries, public interfaces, dependency direction) rebuilt on top of microservices.

### 1.8 Consolidating back: Segment (2018) and Prime Video (2023)

- Segment grew from one service per destination to over 140 services and repositories, each with its own queue, adding about three destinations a month; three full-time engineers spent most of their time keeping it running, shared-library versions diverged, and scaling services with different load patterns was hard. They consolidated the destinations into one monorepo and one service, replayed recorded HTTP traffic for tests, cut deploys from 140+ services to minutes, and raised shared-library improvements from 32 to 46 in a year. Stated trade-offs: weaker fault isolation, less effective in-memory caching across 3,000+ processes, and a shared-dependency upgrade can break several destinations. "the solution for us was a monolith" [VERIFIED: https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices/, published 2018-07-10] **(evidence age: 8 years)**.
- Prime Video's Video Quality Analysis team built a monitoring service on Step Functions orchestrating Lambda functions with S3 for intermediate frames; S3 reads/writes and state transitions drove cost, the design hit the account limit on state transitions and supported only about 5% of expected load. They consolidated the logic into a single process on ECS/EC2 with data passed in memory, and operational cost fell by 90% [WIDELY REPORTED: https://www.infoq.com/news/2023/05/prime-ec2-ecs-saves-costs/, 2023]. The original post (March 2023) has since been removed from primevideotech.com, which now redirects to a corporate page [ASSUMPTION/JUDGEMENT, observed in this session].
- [ASSUMPTION/JUDGEMENT] Both cases are consolidations of one subsystem that had been over-decomposed, not reversals of the companies' overall architecture. Writers should present them as "right-size the unit of deployment", not "microservices failed".

### 1.9 Composable and MACH as a style

- The MACH Alliance describes itself as "the global industry body for open, composable, and connected enterprise technology", says it works with "hundreds of enterprise brands", claims a practitioner community of "over 250,000", and publishes a 2026 Maturity Assessment and a 2026 "Charter for the Agent Ecosystem"; MACH certification "validates that the product meets the standards" for open, composable and connected technology. The home page does not spell out the acronym (Microservices, API-first, Cloud-native SaaS, Headless is the standard expansion) [VERIFIED: https://machalliance.org/, n.d., accessed 2026-11] ⚠.
- commercetools' own limits page shows what a composable vendor sells as a unit: a Project is "the top-level container for your commercetools data and configuration", isolated from other Projects, with 25 API Extensions and 50 Subscriptions per Project (Part 3) [VERIFIED: https://docs.commercetools.com/api/general-concepts, n.d., accessed 2026-11; https://docs.commercetools.com/api/limits, n.d., accessed 2026-11].
- [ASSUMPTION/JUDGEMENT] For a merchant, "composable" is a buying style (several API-first SaaS products, a front end you own, an integration layer you own) rather than an internal architecture. The costs Fowler lists for microservices (distribution, eventual consistency, operational complexity) transfer to the merchant's integration layer almost unchanged, which is why the book's Giant's Boots pattern applies to composable just as it does to a microservices rebuild.

**For newcomers.**
- *Monolith*: one program that contains the whole application and is deployed as one unit.
- *Modular monolith*: still one deployed program, but with internal boundaries that a tool or a review enforces, so that one domain cannot reach into another's tables or classes.
- *Microservices*: many small programs, each deployed and scaled on its own, each owning its own data, talking over the network.
- *Composable (MACH)*: a commerce stack assembled from separately purchased API-first SaaS services rather than one suite.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- *Starting*: a hosted SaaS platform plus a handful of apps; architecture style is not a decision the merchant makes. *Growing*: the first custom services (a connector, a product feed) should be few and boring; a modular monolith for custom code sized to a 5–15-person team is the evidence-backed default (Fowler 2015, Shopify 2019). *Omnichannel*: boundaries matter more than deployment units; decide system-of-record ownership (catalog, stock, orders) before splitting anything. *Group*: platform teams, shared services, standard stacks and API guidelines (Zalando 2020) are what make many teams productive; without them microservices reproduce Jacobs' "six languages" problem.
- The merchant's view differs from the vendor's: Shopify and commercetools must be modular to ship with thousands of engineers; a merchant must be modular only to the degree that two or three teams need to work without blocking each other.

---

## PART 2: Multi-tenancy, pods and isolation

### 2.1 Tenancy models

- AWS SaaS Lens: in the **silo** model "tenants are provided dedicated resources" (a separate stack or a separate database per tenant) while still sharing identity, onboarding and operations; in the **pool** model "tenants share resources", "the more classic notion of multi-tenancy"; the **bridge** model mixes both, "some microservices in your architecture might be implemented with silo and others might use pool", steered by regulatory profile, noisy-neighbour risk, agility and cost [VERIFIED: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/silo-pool-and-bridge-models.html, n.d., accessed 2026-11].
- Noisy neighbour: "a user of a system could place load on the system's resources that could have an adverse effect on other users"; in multi-tenant systems unpredictable tenant workloads heighten the need for strategies that "manage and minimize the potential impacts of noisy tenants" [VERIFIED: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/noisy-neighbor.html, n.d., accessed 2026-11].

### 2.2 Pods and shard balancing: Shopify as the dated example

- Shopify pods (March 2018): a pod is "a set of shops that live on a fully isolated set of datastores" (not Kubernetes pods). Shared resources (job workers, app servers, load balancers) sit outside the pod and talk to one pod at a time; every unit of work (web request, delayed job) is assigned to one pod, so serving a request needs only that pod to be online. A routing component ("Sorting Hat") matches each request to its pod. Each pod has an active and a recovery data centre, and a "Pod Mover" moves a whole pod between data centres in about a minute without dropping requests [VERIFIED: https://shopify.engineering/a-pods-architecture-to-allow-shopify-to-scale, published 2018-03-02] **(evidence age: 8 years)**.
- Shard balancing (September 2021): each shop's data lives in one pod with its own MySQL shard plus Redis and Memcached; the shop is the sharding unit, with a `shop_id` on every shop-owned table, and an unsharded routing table maps domains to pods. Shops are moved with Ghostferry (copy and tail the binlog, a short write lock at cutover, update the routing table, prune later). Balancing is needed because shops land on shards arbitrarily and grow at different rates; the least- and most-loaded shards differed by almost 4x before rebalancing. The worked example is two flash-sale merchants on the same pod with synchronized bursts, one of which is moved [VERIFIED: https://shopify.engineering/mysql-database-shard-balancing-terabyte-scale, published 2021-09-24] **(evidence age: 5 years)**.
- [ASSUMPTION/JUDGEMENT] In SaaS-Lens terms a pod is a silo of datastores under pooled compute: a bridge model. The merchant-relevant consequence is that a hosted platform's isolation unit is invisible to the merchant and can be changed by the vendor (a shop can be moved) — the merchant's own lever is the rate limit, not the pod.

### 2.3 Metadata-driven multi-tenancy: Salesforce

- Salesforce's platform is "multitenant and metadata-driven": one shared database with one schema per instance, tenant metadata and data in shared tables (object and field definitions as rows in MT_Objects and MT_Fields; data in MT_Data flex columns), each organization identified by an OrgID; "When the kernel accesses the database, it uses this unique identifier to ensure that each org's activities are private"; data, metadata and pivot tables are physically partitioned by OrgID; schema changes are metadata updates applied online; governors and resource limits on code execution protect shared resources [VERIFIED: https://architect.salesforce.com/fundamentals/platform-multitenant-architecture, n.d., accessed 2026-11].
- [ASSUMPTION/JUDGEMENT] This is the purest pool model in commercial use and the reason Salesforce products (including B2C Commerce's Business Manager settings) expose "governor limits": in a pool, limits are the isolation mechanism.

### 2.4 Projects, regions and data residency: commercetools

- commercetools hosts in five Regions — North America (Google Cloud, Iowa), North America (AWS, Ohio), Europe (Google Cloud, Belgium), Europe (AWS, Frankfurt), Australia (Google Cloud, Sydney); Regions "are completely isolated from each other, and no data is transferred between them", and user accounts are region-specific [VERIFIED: https://docs.commercetools.com/api/general-concepts, n.d., accessed 2026-11] ⚠.
- [ASSUMPTION/JUDGEMENT] Data residency on SaaS commerce is decided at sign-up by region choice, not by configuration later; a European merchant should record which region every SaaS component (platform, PIM, OMS, returns, search) was provisioned in, because moving is a migration, not a setting.

### 2.5 Rate limits as a tenancy tool

| Platform | Model | Figures (⚠ all volatile) | Source |
| --- | --- | --- | --- |
| Shopify GraphQL Admin API | Leaky bucket of calculated query cost per app-and-store pair; refills at a plan-dependent rate | 100 points/s Standard, 200 Advanced, 1,000 Plus, 2,000 enterprise (Commerce Components); mutations cost 10; a single query may not exceed 1,000 points; resource-based throttle on variant mutations once a store has 500,000 variants (not on Plus) | [VERIFIED: https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits, n.d., accessed 2026-11] |
| Shopify (all APIs) | "Both the bucket size and the restore rate vary by API and by plan"; buyer traffic to the storefront is not rate-limited; recommended backoff 1 s | — | [VERIFIED: https://shopify.dev/docs/api/usage/limits, n.d., accessed 2026-11] |
| Amazon SP-API | Token bucket per operation with a rate (tokens per second) and a burst (bucket size), looked up from the caller's access token; 429 is retryable with backoff; **standard** usage plans are static for all callers, **dynamic** plans are "automatically adjusted to each selling partner based on the current and historical business needs" | Example on the page: rate 1, burst 2 | [VERIFIED: https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits, n.d., accessed 2026-11] |
| BigCommerce | Request quota per time window, by plan | Scale 60k/hour (450 per 30 s); Growth and Core 20k/hour (150 per 30 s); Performance "varies"; some Performance clients on an unlimited plan; headers `X-Rate-Limit-Requests-Left` etc. | [VERIFIED: https://docs.bigcommerce.com/docs/start/best-practices/api-rate-limits, n.d., accessed 2026-11] |
| commercetools | No fixed published request rate; instead per-Project resource and query limits | 500 elements per query (100 for Product Search), max offset 10,000, 500 update actions per request, GraphQL complexity ≥ 20,000 rejected, 14 MB request body, 16 MB document; 10M customers, 10M carts, 10,000 categories, 300,000 stores, 25 API Extensions, 50 Subscriptions; many raisable on request | [VERIFIED: https://docs.commercetools.com/api/limits, n.d., accessed 2026-11] |

- [ASSUMPTION/JUDGEMENT] Three different philosophies: cost-based (Shopify charges by query shape), operation-based with per-seller adaptation (Amazon), and capacity-based (commercetools caps data and query shape rather than request rate). For a merchant, the practical consequence is identical: every app and connector shares the store's bucket, so a badly written stock-sync app can starve the order export on Black Friday — the "noisy neighbour" inside one tenant.

**For newcomers.**
- *Tenant*: one customer (a merchant) of a shared software platform, with its own data and configuration.
- *Pool / silo*: whether tenants share the same servers and database (pool) or get dedicated ones (silo).
- *Pod (Shopify sense)*: a group of shops that share one isolated set of databases, so a failure or overload stays inside the group.
- *Rate limit*: the maximum number of API calls (or units of query cost) a platform lets one app make for one store in a time window.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- *Starting / Growing*: the merchant is a pooled tenant; the only tenancy facts to manage are the region (residency) and the API bucket (which apps consume it). *Omnichannel*: one tenant or several for three countries and six stores is a real decision — one tenant shares the bucket and the catalog, several tenants multiply integrations; most hosted platforms have added multi-market features precisely to keep one tenant. *Group*: the group becomes a tenant-of-tenants (brands as sub-tenants) and starts to care about vendor-side isolation (pods, dedicated instances, enterprise plans) and about its own specialist SaaS (WMS, PIM, returns) being pooled with strangers on peak days.

---

## PART 3: Extensibility — plugins, cartridges, apps, functions and the upgrade problem

### 3.1 Mechanisms

| Mechanism | Runs where | Can touch | Upgrade coupling | Examples |
| --- | --- | --- | --- | --- |
| In-process plugin / extension / cartridge | Inside the platform's process, same language | Anything the code can reach, including the database | Tight: must be re-tested on every platform release | Magento/Adobe Commerce plugins and modules, SAP Commerce extensions, WordPress/WooCommerce hooks, Shopware plugins, SFCC cartridges |
| Theme code | Inside the storefront renderer (templates) | Presentation and, via scripts, the page | Medium: theme updates can conflict with edits | Liquid themes, Stencil (Handlebars), SFRA templates |
| App over APIs + webhooks | Outside, vendor-hosted | Only what scopes permit | Loose: versioned APIs with a support window | Shopify, BigCommerce, Shopware apps, Saleor apps, Adobe App Builder |
| Serverless function at a platform extension point | Inside the platform's request path, sandboxed | A fixed input, a fixed output | Loose but time-boxed | Shopify Functions (Wasm), commercetools API Extensions (HTTP call-out) |
| Synchronous call-out | Platform calls the merchant's endpoint before persisting | Validate or amend one resource | Loose; latency becomes the merchant's problem | commercetools API Extensions |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis of 3.2–3.5.

### 3.2 In-process extension: how the suites and open-source platforms do it

- **Magento / Adobe Commerce plugins (interceptors)** change a public method's behaviour by running code *before*, *after* or *around* it without modifying the class; an around plugin that never calls `$proceed` skips the original method and all later plugins; plugins cannot intercept final methods or classes, non-public or static methods, constructors, virtual types, or objects created before interception is bootstrapped; `sortOrder` in `di.xml` orders multiple plugins on one method, otherwise module load order decides; around plugins "should be avoided unless they're required, because they add to stack traces and can hurt performance" [VERIFIED: https://developer.adobe.com/commerce/php/development/components/plugins, n.d., accessed 2026-11].
- **SAP Commerce**: "SAP Commerce has a flexible, modular architecture based on extensions"; an extension is "an encapsulated piece of software that extends SAP Commerce functionality" by modifying existing features or adding new ones, and extensions can depend on other extensions [VERIFIED: https://help.sap.com/doc/b490bb4e85bc42a7aa09d513d0bcb18e/2205/en-US/8bbf0b9d866910149688b8d696c8d47e.html, n.d. (release 2205), accessed 2026-11].
- **WordPress hooks (the basis of WooCommerce extensions)**: hooks are "a way for one piece of code to interact/modify another piece of code at specific, pre-defined spots"; *actions* do work and return nothing, *filters* take a value and return a modified one and "should never have side effects"; plugins register callbacks so Core files are never edited [VERIFIED: https://developer.wordpress.org/plugins/hooks/, n.d., accessed 2026-11]. WooCommerce's extension guide warns that code marked `@internal` is for core use only and "your extension may break if you use them", that "backwards compatibility between WooCommerce releases is not guaranteed", and offers the Marketplace to reach "3.6M+ active stores" [VERIFIED: https://developer.woocommerce.com/docs/extensions/getting-started-extensions/, n.d., accessed 2026-11] ⚠.
- **Shopware** draws the line explicitly: "Plugins are executed within the Shopware Core process and can react to events, execute custom code or extend services" and "have direct access to the database", therefore "plugins are not supported by Shopware cloud"; "Apps are not executed within the process of the Shopware Core" and interact through webhooks and the Admin REST API [VERIFIED: https://developer.shopware.com/docs/concepts/extensions/, n.d., accessed 2026-11].
- **Salesforce B2C Commerce cartridges**: a storefront is a stack of cartridges ordered by the cartridge path; "B2C Commerce searches the path from left to right and picks the first matching file it finds", so a custom overlay cartridge placed left of `app_storefront_base` overrides it; "you never edit `app_storefront_base` directly", which "keeps the backward compatibility guarantee intact and makes future upgrades straightforward" [VERIFIED: https://trailhead.salesforce.com/content/learn/modules/b2c-cartridges/b2c-cartridges-customize, n.d., accessed 2026-11]. The example cartridge path in Salesforce's SFRA documentation (`app_custom_mybrand:app_custom_mysite:LINK_bazaarvoice:LINK_wordpress:plugin_applepay:plugin_comparison:app_storefront_base`) shows custom, partner (LINK) and plug-in cartridges layered over the base [WIDELY REPORTED: https://developer.salesforce.com/docs/commerce/sfra/guide/b2c-sfra-features-and-comps.html, n.d.; the page returned 403 in this session].

### 3.3 The upgrade problem ("Forked Platform") in the vendors' own words

- Adobe Commerce upgrade best practices: "The amount of custom work and the number of installed third-party modules strongly affects the complexity of an upgrade"; "The quality of the custom work and modules can determine whether an upgrade goes smoothly"; skipping releases makes the next upgrade harder; test in staging; validate extensions against the target version; run the Upgrade Compatibility Tool; it is "critical that you develop on the latest available release"; testing is the most time-consuming phase; if upgrades cost more than expected, audit the project [VERIFIED: https://experienceleague.adobe.com/en/docs/commerce-operations/upgrade-guide/prepare/best-practices, n.d., accessed 2026-11].
- The Upgrade Compatibility Tool checks a customized instance's installed modules and core code against a target version and reports "critical issues, errors, and warnings"; it is available for Adobe Commerce, not Magento Open Source [VERIFIED: https://experienceleague.adobe.com/en/docs/commerce-operations/upgrade-guide/upgrade-compatibility-tool/overview, updated 2026-10-08].
- Adobe Commerce lifecycle: three years of standard support from GA (quality fixes, security patches, support), one extra year of extended support for 2.4.6 and 2.4.7, then a security-only period as a one-time exception. Dates: 2.4.4 GA 2022-04-12, standard support ended 2025-04-12; 2.4.7 GA 2024-04-09, standard support to 2027-05-31; 2.4.8 GA 2025-04-08; 2.4.9 GA 2026-05-12. From 2027-06-01 Adobe will no longer maintain Cloud environments on unsupported versions and storefronts "may be taken offline"; customers are responsible for PHP, MySQL and OpenSearch versions (PHP 8.1 EOL 2025-12-31) [VERIFIED: https://experienceleague.adobe.com/en/docs/commerce-operations/release/planning/lifecycle-policy, n.d., accessed 2026-11] ⚠.
- Adobe's stated reason for its newer out-of-process model: in-process code "must stay compatible with each Commerce version and its runtime", while App Builder apps can be "developed, deployed, and operated on their own schedule", scale independently and do not compete with the core for resources; the trade-off is that in-process extensibility offers "deep, synchronous control of the Commerce runtime" that out-of-process does not [VERIFIED: https://developer.adobe.com/commerce/extensibility/, n.d., accessed 2026-11].
- [ASSUMPTION/JUDGEMENT] The "customized core cannot upgrade" failure is therefore documented by the vendor that suffers from it most: upgrade cost scales with the number and quality of in-process modules, and the vendor's support clock (three years) is what turns a postponed upgrade into a forced migration. Salesforce's overlay rule and Shopware's cloud rule are the same lesson expressed as a constraint rather than as advice.

### 3.4 Out-of-process extension: apps, functions and call-outs

- **Shopify Functions** plug into a *target* (discounts, payment customization, delivery customization, checkout validation, bundles, fulfillment constraints, pickup options and location rules). Shopify passes a JSON input produced by a GraphQL input query, the function (compiled to WebAssembly, Rust "strongly recommended") returns a JSON list of operations; functions cannot be called by URL. Limits (API 2026-10): 11 million instructions per run for carts of up to 200 lines, 10 MiB linear memory, 512 kB stack, 256 KiB compiled module. Custom apps containing functions require Shopify Plus; public App Store apps with functions run on any plan [VERIFIED: https://shopify.dev/docs/apps/build/functions, n.d., accessed 2026-11; https://shopify.dev/docs/api/functions, API 2026-10, accessed 2026-11] ⚠. Shopify Scripts and the Script Editor "were retired on June 30, 2026" and scripts no longer run on any store [VERIFIED: https://help.shopify.com/en/manual/checkout-settings/script-editor, n.d., accessed 2026-11].
- **commercetools API Extensions** are synchronous call-outs after a create/update is processed but before it is saved, on carts, orders, payments, customers, quotes, business units, shopping lists and products; an extension may reject with validation errors or return up to 100 update actions. "if it fails or takes a second longer to return a result, the whole API call fails or takes a second longer." Timeouts: 2 s to connect, 2 s to respond by default, configurable to a maximum of 10 s (beyond that needs a support request and performance review); recommended target about 50 ms; 25 extensions per Project; up to 5 dependencies and a chain depth of 3; any failure (504 `ExtensionNoResponse`, 502 `ExtensionBadResponse`) fails the whole API call and is not retried within it [VERIFIED: https://docs.commercetools.com/api/projects/api-extensions, n.d., accessed 2026-11].
- **commercetools Connect** hosts "Connect applications" on commercetools-provisioned infrastructure, deployed through the Connect API with logs and revisions; marketplace integrations are "certified to ensure functionality, security, and compatibility" [VERIFIED: https://docs.commercetools.com/connect/, n.d., accessed 2026-11].
- **Saleor apps** are external, technology-agnostic services that "add new functionalities on top of Saleor", communicating through webhooks and the API, installable in the Dashboard if they meet its requirements [VERIFIED: https://docs.saleor.io/developer/extending/apps/overview, n.d., accessed 2026-11].
- **Adobe App Builder / out-of-process**: custom logic runs as serverless actions on I/O Runtime, connected through Commerce APIs, events and webhooks, with an Admin UI SDK for admin extension points and App Management for install/update/remove [VERIFIED: https://developer.adobe.com/commerce/extensibility/, n.d., accessed 2026-11].
- [ASSUMPTION/JUDGEMENT] The common design across vendors: an extension point is a *named moment* in the platform's flow with a fixed input, a fixed output, a time budget and a failure rule. The time budget (commercetools 2 s default, Shopify an instruction count) is the vendor protecting the checkout from the merchant's code — the architectural fact behind the book's "checkout is the most protected part" claim (chapter 11).

### 3.5 App store governance

- **Shopify** app review: request only the access scopes the app needs (merchants see them on the OAuth grant page); an app "shouldn't lower a store's Lighthouse performance score by more than 10 points" (weighted: Home 17%, Product 40%, Collection 43%); apps using APIs deprecated within 90 days cannot be submitted; charges must go through Shopify's billing; a screencast of setup and functionality is required; an app whose core functionality changes must be resubmitted [VERIFIED: https://shopify.dev/docs/apps/launch/app-requirements-checklist, n.d., accessed 2026-11]. The App Store front page says "With over 16,000 apps" [VERIFIED: https://apps.shopify.com/, n.d., accessed 2026-11] ⚠. Third-party trackers reported roughly 12,300 apps in January 2025 and about 17,600–17,900 active apps by April 2026, with different counting rules [WIDELY REPORTED: https://magecomp.com/blog/shopify-app-store-statistics/, 2026] ⚠.
- **BigCommerce** marketplace: every submission is tested against published standards (Required vs Recommended); apps must request only needed scopes and "Apps configured with all scopes aren't approved"; the Checkout Content scope triggers a security assessment and checkout-modifying apps must use the Checkout SDK; apps that handle card data need a PCI review and an Attestation of Compliance; BigCommerce "has paused new externally built payment integrations for the public Marketplace"; uninstall must return the control panel and storefront to their pre-install state and remove storefront scripts; listings may not reference competing platforms [VERIFIED: https://docs.bigcommerce.com/docs/integrations/apps/guide/requirements, n.d., accessed 2026-11] ⚠.
- **WooCommerce**: 3.6M+ active stores reachable through the Marketplace; a Quality Insights Toolkit tests extensions for vendors [VERIFIED: https://developer.woocommerce.com/docs/extensions/getting-started-extensions/, n.d., accessed 2026-11] ⚠.
- [ASSUMPTION/JUDGEMENT] The three governance levers every store uses are scopes (what an app may read or write), review (performance, security, billing, uninstall hygiene) and API versioning (Part 6). None of them tells the merchant which installed app is writing stock; that inventory is the merchant's own job — the "App That Wrote Stock" pattern is a governance gap on the merchant side, not the vendor side.

**For newcomers.**
- *Extension point*: a named place in the platform's flow where the platform agrees to run or call someone else's code.
- *Plugin (in-process)*: code that runs inside the platform program itself and can therefore do anything the platform can.
- *App (over APIs)*: a separate program, run elsewhere, that may only do what its granted permissions (scopes) allow.
- *Scope*: one named permission an app asks for at install, such as "read orders" or "write inventory".

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- *Starting*: public apps only; keep an inventory with the scope list from day one. *Growing*: the first custom app or function; prefer out-of-process mechanisms even on open-source platforms (Shopware apps, Adobe App Builder) so upgrades stay cheap. *Omnichannel*: an owner per app, a rule that only one system may write stock and one may write prices, and a quarterly uninstall review; on in-process platforms, the module count and quality decide the upgrade bill. *Group*: a shared extension catalogue across brands and an upgrade calendar aligned to the vendors' support clocks.

---

## PART 4: Storefront delivery — themes, headless, rendering, performance, accessibility

### 4.1 Themes: server-rendered templates inside the platform

- Shopify's Storefront Renderer (August 2020) is a server-side application that loads a merchant's Liquid theme and the data a request needs and returns HTML, rebuilt from the Rails monolith (where storefront code had lived for more than 15 years) because storefront has stricter performance needs than, say, payment processing. It reads from dedicated read replicas, caches frequent queries in a key-value store and in application memory, and caches full page renders. Results: server response times 4x–6x faster than the legacy path (later "about 4x on average"), +0.11 Apdex on average, +0.20 on cache misses, about 500 ms better time-to-first-byte for some merchants [VERIFIED: https://shopify.engineering/how-shopify-reduced-storefront-response-times-rewrite, published 2020-08-20] **(evidence age: 6 years)**.
- BigCommerce's Stencil is "BigCommerce's Handlebars-based theme engine", with widgets and Page Builder [VERIFIED: https://docs.bigcommerce.com/docs/storefront/stencil/start, n.d., accessed 2026-11].
- Salesforce's SFRA is template-and-controller code layered through cartridges (3.2).
- [ASSUMPTION/JUDGEMENT] The theme model's architectural property is that the platform owns rendering, caching, availability and security of the storefront; the merchant owns templates and scripts. Its performance ceiling is the platform's, which (Shopify's numbers show) is high; its flexibility ceiling is the template language.

### 4.2 Headless: storefront frameworks and the APIs under them

- **Hydrogen** (Shopify) is "not a framework itself" but a toolkit added to a framework (React Router 7 in framework mode is the starter), supplying the Storefront API client, cart and request handlers; it covers the Storefront and Customer Account APIs, not the Admin API; the template is deployed to Oxygen; browser-side forms let customers shop before JavaScript loads [VERIFIED: https://shopify.dev/docs/storefronts/headless/hydrogen, n.d., accessed 2026-11] ⚠.
- **Salesforce PWA Kit** is "a storefront technology for headless commerce using Salesforce Commerce APIs and React", deployed as bundles to a Managed Runtime; Node 18–24 [VERIFIED: https://github.com/SalesforceCommerceCloud/pwa-kit, n.d., accessed 2026-11].
- **Next.js Commerce** (Vercel) is "A high-performance, server-rendered Next.js App Router ecommerce application" using React Server Components, Server Actions, Suspense and `useOptimistic`, with Shopify as reference and forks for BigCommerce, Medusa, Saleor, Shopware, Swell, Wix and others; the repository is archived and the template deprecated, with development moved to `vercel/shop` [VERIFIED: https://github.com/vercel/commerce, n.d., accessed 2026-11] ⚠.
- **Alokai (formerly Vue Storefront)** Unified Data Layer normalizes "product data from each platform into this common format" (`SfProduct` and similar) through a middleware that calls the backend and runs a normalizer; backends listed: BigCommerce, commercetools, Magento, SAP Commerce Cloud, Salesforce Commerce Cloud [VERIFIED: https://docs.alokai.com/unified-data-layer, n.d., accessed 2026-11] ⚠.
- **Adobe Commerce Storefront** is built from "drop-in" components with document-based authoring and a separate publishing path; the page promises "the fastest storefronts on the web" without benchmark data on that page [VERIFIED: https://experienceleague.adobe.com/developer/commerce/storefront/, n.d., accessed 2026-11].
- [ASSUMPTION/JUDGEMENT] Every headless framework above is server-rendered React by default; "headless" no longer means a client-rendered single-page app. The merchant takes over three things the theme model gave for free: rendering infrastructure, caching, and the glue to search, pricing and availability.

### 4.3 Static generation, edge delivery and caching catalog pages

- Vercel's ISR "combines the speed of static content with the flexibility of server-side rendering", following stale-while-revalidate: visitors get the cached page while it is regenerated in the background on a time interval or an API call; the documentation names e-commerce catalogs "that need current pricing and availability without rebuilding the entire site" as the first use case; concurrent requests to an uncached path are collapsed "into one function invocation per region, protecting your backend during traffic spikes"; purges propagate to all regions within 300 ms; on failed revalidation stale content is served and retried after 30 s [VERIFIED: https://vercel.com/docs/incremental-static-regeneration, updated 2026-08-28].
- [ASSUMPTION/JUDGEMENT] The practical split in every storefront, themed or headless: product and category pages are cacheable per market and language (and should be, for peak days); price for a logged-in B2B account, live stock, cart and checkout are not, and are fetched after the cached shell renders. The Storefront Renderer's full-page cache and ISR are the same idea at two layers.

### 4.4 Core Web Vitals and conversion: what the dated evidence actually says

- Deloitte Ireland for Google (March 2020): a four-week study of mobile sites across retail, travel, luxury and lead generation in Europe and the US found that a 0.1-second improvement in mobile site speed went with +8.4% retail conversions and +9.2% retail average order value, +10.1% travel conversions, and −8.3% bounce on lead-generation information pages. Caveats: commissioned by Google; number of sites not disclosed; correlation [VERIFIED: https://www.deloitte.com/ie/en/services/consulting/research/milliseconds-make-millions.html, published 2020-03-24] **(evidence age: 6 years)**.
- web.dev's business-impact collection (undated case studies): Vodafone Italy LCP −31% → sales +8%; Lazada 3x LCP → +16.9% mobile conversion; Cdiscount improved all three metrics → +6% revenue in a Black Friday sale; Tokopedia LCP −55% → +23% session duration; Agrofy LCP −70% → −76% load abandonment; Flipkart improved CWV → −2.6% bounce; AliExpress CLS 10x better and LCP doubled → −15% bounce [VERIFIED: https://web.dev/case-studies/vitals-business-impact, n.d., accessed 2026-11].
- INP replaced FID as the responsiveness Core Web Vital on 12 March 2024 (FID removed from Search Console the same day; a six-month deprecation period in PageSpeed Insights and CrUX) [VERIFIED: https://web.dev/blog/inp-cwv-march-12, published 2024]. Thresholds: good ≤ 200 ms, needs improvement 200–500 ms, poor > 500 ms, assessed at the 75th percentile of page loads, mobile and desktop separately [VERIFIED: https://web.dev/articles/inp, n.d., accessed 2026-11].
- [ASSUMPTION/JUDGEMENT] The honest reading: the direction is consistent across every published case, the magnitudes are self-selected success stories, and none isolates speed from the redesign that came with it. Writers should quote the Deloitte retail numbers with the caveats and treat the web.dev cases as illustrations.

### 4.5 Accessibility: WCAG 2.2 and the European Accessibility Act

- WCAG 2.2 is a W3C Recommendation dated 12 December 2024 (the current edition; first published October 2023), with nine success criteria new since 2.1, three conformance levels (A, AA, AAA) and four principles (Perceivable, Operable, Understandable, Robust) [VERIFIED: https://www.w3.org/TR/WCAG22/, published 2024-12-12].
- Directive (EU) 2019/882 (the European Accessibility Act) applies to services "provided to consumers after 28 June 2025", listing "(f) e-commerce services" alongside electronic communications, audiovisual media access, passenger transport elements, consumer banking and e-books. It defines e-commerce services as "a service provided at a distance, through websites and mobile device-based services, by electronic means and at the individual request of a consumer, with a view to concluding a consumer contract". Member States had to transpose by 28 June 2022 and apply from 28 June 2025. "Microenterprises providing services shall be exempt", a microenterprise being one with fewer than 10 persons and turnover or balance sheet not exceeding EUR 2 million. Transitional measures let service contracts agreed before 28 June 2025 run unaltered until expiry but no longer than five years, and allow products lawfully used before that date to continue until 28 June 2030 [VERIFIED: http://publications.europa.eu/resource/celex/32019L0882, published 2019-06-07 (OJ L 151)].
- [ASSUMPTION/JUDGEMENT] For a Dutch, Belgian or German B2C merchant above the microenterprise threshold, the storefront, checkout, account pages and transactional e-mails are in scope since June 2025; national enforcement differs. B2B-only storefronts are outside "consumer" scope. Writers should send readers to `brief-security-privacy-regulation` for national transposition and penalties.

### 4.6 Progressive web apps and native apps

- PWAs are "web apps built and enhanced with modern APIs", installable into "a standalone window", expected to work "even when offline", and able to use push notifications [VERIFIED: https://web.dev/articles/what-are-pwas, n.d., accessed 2026-11].
- [ASSUMPTION/JUDGEMENT] For a merchant the PWA question is mostly a headless question in disguise: the same server-rendered React storefront can be installable. A native app is justified by loyalty, push and store-mode features, not by performance, and adds a second storefront to keep consistent with pricing and availability services.

**For newcomers.**
- *Theme*: the template files that a hosted platform renders into pages on its own servers.
- *Headless*: the storefront is a separate application that fetches products, carts and checkout from the platform through a Storefront API.
- *Server-side rendering (SSR)*: HTML is produced on a server and sent complete; *client-side rendering* ships JavaScript that builds the page in the browser.
- *Edge delivery / CDN*: copies of pages or code served from data centres near the shopper, with rules for when a copy is stale.
- *Core Web Vitals*: Google's three field metrics for loading (LCP), responsiveness (INP, since March 2024) and visual stability (CLS).

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- *Starting / Growing*: the theme; measure CWV at the 75th percentile and police app scripts (Shopify's 10-point Lighthouse rule is a vendor admitting apps are the usual culprit). *Omnichannel*: headless becomes worth it only when the storefront needs what the theme cannot do (a shared front end across brands or countries, a CMS-led content model, or a B2B portal with account pricing) and the team can own rendering, caching and the three service dependencies; otherwise it is the Giant's Boots. *Group*: one front-end platform (framework, design system, UDL-style normalization) across brands is the usual reason to go headless at this stage.

---

## PART 5: Peak load and reliability

### 5.1 What peaks look like, with definitions

| Event | Figure | Definition / caveat | Source |
| --- | --- | --- | --- |
| Alibaba 11.11, 2020 | 583,000 orders per second, 26 seconds after midnight on 11 Nov 2020; 1,400x the 2009 debut peak; PolarDB 140 million queries per second at peak | "orders" undefined in the release; company-reported, unaudited | [VERIFIED: https://www.alibabacloud.com/press-room/magic-behind-the-worlds-largest-online-shopping-festival, published 2020-11-19] |
| Alibaba 11.11, 2020 | GMV RMB 498.2 billion (US$74.1 billion) over 1–11 November 2020 | GMV = value of orders "settled through Alipay" across Alibaba's marketplaces, real-time, incl. shipping, unaudited | [VERIFIED: https://www.alibabagroup.com/document-1491144671282331648, published 2020-11-12] |
| Alibaba 11.11, 2019 | 544,000 peak transactions per second | Reported in Alibaba Cloud's 2020 release as the prior record | [WIDELY REPORTED: https://www.alibabacloud.com/press-room/magic-behind-the-worlds-largest-online-shopping-festival, 2020] |
| US Cyber Monday 2024 (Adobe) | $13.3 billion online, +7.3% YoY; peak hour 8–10 pm $15.8 million per minute; Cyber Week $41.1 billion; 57% of Cyber Monday sales on mobile | Adobe Analytics over 1 trillion visits to US retail sites, 100 million SKUs, 18 categories | [VERIFIED: https://news.adobe.com/news/2024/12/120324-adi-cyber-monday-recap, published 2024-12-03] |
| Shopify BFCM 2025 (comparison only) | $14.6 billion GMV, +27% YoY; peak $5.1 million per minute at 12:01 pm EST on Black Friday; 81+ million buyers | GMV = "total dollar value of orders facilitated through the Shopify platform", net of refunds, incl. shipping, duties and VAT; approximate and unaudited | [VERIFIED: https://www.shopify.com/news/bfcm-data-2025, published 2025-12-02] |
| Zalando Cyber Week 2019 | 7,200 peak orders per minute (from 4,200 in 2018, +71%); about 840,000 new customers; GMV +32% YoY | Company blog | [VERIFIED: https://engineering.zalando.com/posts/2020/10/how-zalando-prepares-for-cyber-week.html, published 2020-10-08] |
| Shopify BFCM 2024 platform load | 284 million requests per minute at the edge, 80 million on app servers, 12 TB per minute, 10.5 trillion database queries over the weekend | Company blog | [VERIFIED: https://shopify.engineering/bfcm-readiness-2025, published 2025-11-20] |

- [ASSUMPTION/JUDGEMENT] Three different units in one table (orders per second, dollars per minute, requests per minute) is the point: a merchant's peak plan must state its own unit — orders per minute is the one that every system in the chain (platform, OMS, WMS, carrier, ERP) can be measured against.

### 5.2 Load testing: two documented programmes

- Zalando (April 2019) load-tested the production website end to end because team-level tests could not show whether the distributed system held together under Black Friday load: real user journeys (home, browse, add to cart, checkout) were recorded as HAR files, converted to Locust scripts, and run from four Locust stacks of 300 nodes each, reaching about 130,000 requests per second, above the real Cyber Week peak; recorded scenarios broke on replay because sessions expired, items sold out and rate limiting blocked requests; component teams sat in "situation rooms" and could stop the test; the team forked Locust when its distributed mode misbehaved at scale [VERIFIED: https://engineering.zalando.com/posts/2019/04/end-to-end-load-testing-zalandos-production-website.html, published 2019-04-11] **(evidence age: 7 years)**.
- Zalando's 2020 retrospective: each year's Cyber Week project invests in one capability the company lacked (resilience engineering, load testing, capacity planning, production-readiness reviews); more than 1,122 of 4,000+ applications were in scope; 10 volunteer SREs ran production-readiness reviews and workshops on dependency failures, overload and timeouts; distributed tracing was rolled out to tier-1 browse-path systems first, with traffic-source tags (App, Web, push, load test) for capacity planning and "adaptive paging" to page the team most likely at fault; order-flow simulators place test orders that fulfillment skips, exercising inventory and payments; in 2015 pausing non-essential asynchronous processing protected order acceptance; a Situation Room with engineering, SRE and Incident Commanders is staffed through the peak [VERIFIED: https://engineering.zalando.com/posts/2020/10/how-zalando-prepares-for-cyber-week.html, published 2020-10-08] **(evidence age: 6 years)**.
- Shopify (November 2025): five scale tests from April to October on production infrastructure from three GCP regions with its in-house tool Genghis, ramping scripted browse/cart/checkout workflows and layering flash-sale bursts, plus Toxiproxy fault injection; the main target was roughly 150% of the previous year's load, with p90 forecasts for scale tests and p99 for the final one (200 million requests per minute; one test reached 80,000+ checkouts per minute); adding authenticated checkout mid-programme exposed rate-limit paths anonymous browsing missed; Game Days injected faults into "critical journeys" (checkout, payments, order creation, fulfillment) and fed a Resiliency Matrix of vulnerabilities, runbooks and recovery objectives; 24/7 incident coverage and merchant status communication during the event [VERIFIED: https://shopify.engineering/bfcm-readiness-2025, published 2025-11-20].
- [ASSUMPTION/JUDGEMENT] The transferable practices for a merchant that does not own the platform: test the *journeys* not the servers; include authenticated and checkout traffic; include the integrations (the order export, the stock sync, the ERP) because that is where Zalando's "dependency failures, overload and timeouts" workshops point; mark test orders so fulfillment skips them.

### 5.3 Overload, load shedding and backpressure

- AWS Builders' Library (December 2019): "When a system is given more work than its resources support, it becomes slow"; a server near overload "should start rejecting excess requests so that it can focus on the requests it decides to let in"; *goodput* is "the subset of the throughput that is handled without errors" and fast enough to be useful; prioritize — "The most important request that a server will receive is a ping request from a load balancer", then human-originated over crawler traffic [VERIFIED: https://builder.aws.com/content/3Eun1EEyX6p2e3VYNyRLSJzLuMV/using-load-shedding-to-avoid-overload, published 2019-12-05] **(evidence age: 7 years)**.
- Vercel's request collapsing (4.3) and commercetools' 2-second extension timeout (3.4) are the same principle applied at the CDN and at the API: bound what one request may cost the system [ASSUMPTION/JUDGEMENT].
- [ASSUMPTION/JUDGEMENT] In a commerce chain, backpressure means: accept and persist the order fast, queue everything downstream (confirmation e-mail, ERP export, WMS release, marketplace stock update), and let queues grow rather than fail checkout. Zalando's 2015 "pause non-essential asynchronous processing" is this rule in practice.

### 5.4 Graceful degradation and feature switches

- Hodgson's taxonomy (October 2017): release toggles, experiment toggles, ops toggles and permissioning toggles; ops toggles "are used to control operational aspects of our system's behavior", and long-lived kill switches "allow operators of production environments to gracefully degrade non-vital system functionality" under high load [VERIFIED: https://martinfowler.com/articles/feature-toggles.html, published 2017-10-09].
- Amazon Prime Day 2018 (CNBC on internal documents): glitches began within 15 minutes of the noon launch; Amazon "did not secure enough servers", a breakdown in the internal Sable storage/computation system cascaded to dependent services; at 12:00 the site switched to a simplified fallback front page, at 12:15 all international traffic was cut off to relieve Sable, at 12:37 the default front page was restored for 25% of traffic, and 50–150 hosts were added manually [VERIFIED: https://www.cnbc.com/2018/07/19/amazon-internal-documents-what-caused-prime-day-crash-company-scramble.html, published 2018-07-19] **(evidence age: 8 years)**.
- [ASSUMPTION/JUDGEMENT] A merchant's "switch-off order" for peak day, in the order the sources suggest: recommendations and personalization, search facets and sort options, live stock badges (fall back to cached), gift wrap and non-essential checkout options, marketplace stock pushes (slow them), then — last — new sign-ups. Checkout, payment and order persistence are never on the list.

### 5.5 Waiting rooms and virtual queues

- Cloudflare launched Waiting Room in January 2021 after COVID-19 vaccine registration sites failed under demand; it "limits requests inbound to an application, and places these requests into a virtual queue", admitting users in batches as load drops, built on Workers and Durable Objects with no application change; configuration is five fields: name, hostname, maximum active users, new users per minute, session duration [VERIFIED: https://blog.cloudflare.com/cloudflare-waiting-room/, published 2021-01-22]. Settings today: `total_active_users` (must exceed 200; suggested 75% of origin capacity), `new_users_per_minute` (a threshold, suggested 100% of peak), `session_duration` 1–30 minutes (default 5) [VERIFIED: https://developers.cloudflare.com/waiting-room/reference/configuration-settings/, n.d., accessed 2026-11] ⚠; queueing methods are FIFO ("orders visitors according to when they entered the waiting room"), random, passthrough and reject [VERIFIED: https://developers.cloudflare.com/waiting-room/reference/queueing-methods/, n.d., accessed 2026-11].
- Queue-it: visitors are redirected only when traffic exceeds a set capacity; a safety-net queue is first-in-first-out, while scheduled sales use a countdown and randomized positions; outflow is set in visitors per minute and adjustable during the event; admitted visitors carry a token; bot rules challenge or block by IP, user agent and reputation [VERIFIED: https://queue-it.com/how-does-queue-it-work/, n.d., accessed 2026-11].
- [ASSUMPTION/JUDGEMENT] A waiting room converts an unknown spike into a known outflow rate — which is only useful if the merchant knows its capacity in orders per minute end to end (5.1). It protects the storefront; it does nothing for the ERP export that falls over at 2,000 orders an hour.

### 5.6 SLOs, error budgets and incident response

- Google SRE (2017): an SLI is "a carefully defined quantitative measure of some aspect of the level of service", an SLO "a target value or range of values for a service level that is measured by an SLI", an SLA "an explicit or implicit contract with your users that includes consequences of meeting (or missing) the SLOs"; an error budget is "just an SLO for meeting other SLOs", and the chapter warns not to overachieve because users come to depend on actual, not promised, behaviour [VERIFIED: https://sre.google/sre-book/service-level-objectives/, published 2017].
- Zalando staffs a Situation Room through the peak with engineering, SRE and Incident Commanders, and uses tracing-driven "adaptive paging"; Shopify runs 24/7 IMOC coverage, a Resiliency Matrix with runbooks and recovery objectives, and merchant status communications (5.2).
- [ASSUMPTION/JUDGEMENT] For a merchant the SLOs that matter are expressed in the business unit: checkout success rate, order-confirmation latency, time from order to WMS release, and stock-sync lag to marketplaces (overselling risk). The vendors' SLAs cover their own uptime; the merchant's integration SLOs are nobody else's.

### 5.7 Observability: orders per minute as the health signal

- The sources in 5.1 and 5.2 show that the operators of the largest peaks report their own health in business units: orders per second (Alibaba), orders per minute (Zalando), checkouts per minute and sales per minute (Shopify), spend per minute (Adobe) [VERIFIED, as cited in 5.1 and 5.2].
- A frequently cited 2015 PagerDuty post claiming Amazon alerts on a drop in orders per second could not be found at any live URL in this session and is not used [ASSUMPTION/JUDGEMENT].
- [ASSUMPTION/JUDGEMENT] The practitioner rule writers can state as judgement: plot orders per minute against the same weekday and hour of recent weeks, alert on a sustained drop, and overlay checkout error rate and payment authorization rate; it catches failures that server health never shows (a broken promotion, a payment provider decline spike, a stock feed that zeroed the catalog).

### 5.8 Recovery after an incident

- Zalando's test-order simulators that fulfillment skips, Shopify's "recovery objectives" per critical journey, and Ghostferry's verified, formally specified data moves (2.2) are the public traces of recovery design [VERIFIED, as cited].
- [ASSUMPTION/JUDGEMENT] The commerce-specific recovery work is reconciliation: orders accepted during the incident but never exported, payments captured without an order, stock decremented twice, webhooks dropped. The brief `brief-integration-and-data` owns replay and reconciliation mechanics; this chapter should insist that the peak plan names who reconciles what, with which report, before the day.

**For newcomers.**
- *Peak*: a planned or unplanned period when traffic and orders are many times normal (Black Friday, a launch, a TV mention).
- *Load test*: deliberately sending realistic artificial traffic to find where the system breaks before customers do.
- *Backpressure*: letting slow downstream systems slow the producers (or queue the work) instead of failing the customer-facing step.
- *Graceful degradation*: switching off non-essential features in a planned order so the essential ones keep working.
- *SLO*: a measurable target for how well a service must perform (for example, 99.9% of checkouts succeed within 3 seconds).

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- *Starting*: the platform's peak is not yours; your risks are the 3PL's cut-off and a payment provider's test mode left on. *Growing*: the first integrations are the first bottlenecks; test the order export at 10x, set queues between platform and ERP, and write the switch-off list. *Omnichannel*: a peak plan with a named owner, orders-per-minute capacity per system, a waiting room decision, a situation room, and a reconciliation owner; marketplace stock pushes and store POS stock are now part of the blast radius. *Group*: shared peak tooling (load tests, dashboards, runbooks) across brands, and vendor SLAs read against the group's own SLOs.

---

## PART 6: Engineering practices for small commerce teams

### 6.1 Environments and sandboxes on SaaS

- Shopify development stores are "for development and testing only", "can't be used in production or process real transactions", use Shopify's test gateway or a provider's test mode, cannot be transferred to a client or converted to production, are always password-protected, and are capped at 250 per organization [VERIFIED: https://shopify.dev/docs/apps/build/dev-dashboard/stores/development-stores, n.d., accessed 2026-11] ⚠.
- Adobe Commerce Cloud Pro provides four environments: integration (limited testing; no Fastly or New Relic, so not for performance or UAT), staging (dedicated hardware matching production, for UAT, regression against production data, performance and B2B testing), production (public storefronts, redundant nodes) and a master copy for debugging; code moves integration → staging → production [VERIFIED: https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/architecture/pro-architecture, n.d., accessed 2026-11].
- Stripe sandboxes are isolated test environments with their own API keys where "card networks and payment providers don't process payments"; accounts may create up to five general sandboxes with isolated settings and separate access control, suited to "local development, CI, and staging"; test objects are not visible in live mode; the legacy test mode shares some settings with live mode [VERIFIED: https://docs.stripe.com/test-mode, n.d., accessed 2026-11] ⚠.
- [ASSUMPTION/JUDGEMENT] On SaaS the merchant never gets a full copy of production; the testable surface is apps, themes, functions and integrations against a test store plus each provider's sandbox. The gap is the *chain*: no vendor offers a sandbox of platform + PSP + ERP + WMS together, which is why order-flow simulators with marked test orders (Zalando, 5.2) are the pattern small teams should copy at small scale.

### 6.2 Release management against versioned APIs and support clocks

- Shopify releases an API version "every three months at 5pm UTC on the first day of the quarter"; each stable version is supported for at least 12 months, overlapping the next by at least nine; versions are date-named (`2026-04`); requests to a retired version are not rejected — "Shopify falls forward and responds using the oldest accessible stable version"; release candidates "May include backwards-incompatible changes" [VERIFIED: https://shopify.dev/docs/api/usage/versioning, n.d., accessed 2026-11] ⚠.
- Adobe Commerce's three-year standard support per release line and the June 2027 cloud enforcement (3.3) set the upgrade calendar for in-process platforms [VERIFIED, as cited in 3.3].
- WooCommerce: "backwards compatibility between WooCommerce releases is not guaranteed" [VERIFIED: https://developer.woocommerce.com/docs/extensions/getting-started-extensions/, n.d., accessed 2026-11].
- [ASSUMPTION/JUDGEMENT] A small team's release calendar is therefore set by its vendors: quarterly API-version bumps on hosted platforms (with a one-year grace), yearly platform upgrades on suites, and connector updates whenever a marketplace or carrier changes an API. Pinning versions in every connector and recording the pinned version per integration in the ownership map is the cheapest control.

### 6.3 Feature flags

- Hodgson's four toggle types (5.4) give small teams a vocabulary: release toggles for shipping unfinished storefront or checkout changes dark; ops toggles as the peak-day switch-off list; permissioning toggles for staff-only or B2B-only features; experiment toggles for A/B tests [VERIFIED: https://martinfowler.com/articles/feature-toggles.html, published 2017-10-09].

### 6.4 Team topologies applied to commerce

- Team Topologies defines four team types — stream-aligned ("aligned to a flow of work from (usually) a segment of the business domain"), enabling, complicated-subsystem and platform ("a grouping of other team types that provide a compelling internal product") — and three interaction modes (collaboration, X-as-a-Service, facilitation), built on the premise that "Teams can only handle so much complexity before breaking down" [VERIFIED: https://teamtopologies.com/key-concepts, n.d., accessed 2026-11]. The book is Skelton and Pais, *Team Topologies* (IT Revolution, 2019) [WIDELY REPORTED: https://teamtopologies.com/, 2019].
- Zalando's 2020 lesson that autonomous teams without a standard stack built the same CRUD service in six languages (1.4), and Uber's finding that 2,200 services needed domains, gateways and layers to be workable (1.7), are the two public cautions against stream-aligned autonomy without a platform team [VERIFIED, as cited].
- [ASSUMPTION/JUDGEMENT] For a 10–20-person commerce team the honest mapping is: one or two stream-aligned teams by *journey* (buy; fulfil-and-return) rather than by system, one person or pair acting as an enabling/integration role that owns the connectors and the ownership map, and the vendors and agency as X-as-a-Service providers with explicit contracts. A "platform team" appears at Group stage, when several brands need the same front end, integration layer and peak tooling.

### 6.5 Working with agencies and implementation partners

- The vendor-side evidence for partner programmes is structural rather than quantitative: Shopify's client-transfer stores exist so an agency can build a store and hand it to a merchant, with real transactions disabled until transfer [VERIFIED: https://help.shopify.com/en/partners/dashboard/managing-stores/development-stores, n.d., accessed 2026-11]; Salesforce's LINK cartridges are partner-built layers in the cartridge path (3.2); BigCommerce requires an active Technology Partner account and agreement for any marketplace app (3.5).
- [ASSUMPTION/JUDGEMENT] No dated practitioner study on merchant–agency engineering practice in the Netherlands, Belgium or Germany was found. The analyst's rules, stated as judgement: the merchant owns the repository, the vendor accounts, the API credentials, the ownership map and the decision records; the agency is a contributor with review rights, not the owner; every custom module or app the agency builds is listed with its scopes and an exit plan; and the contract names the API versions and platform releases the deliverable is tested against.

### 6.6 AI coding tools in commerce teams (dated evidence)

- DORA 2024 (announced 23 October 2024): more than 75% of respondents rely on AI for at least one daily task; more than a third report "moderate" to "extreme" productivity gains; a 25% increase in AI adoption is associated with +7.5% documentation quality, +3.4% code quality, +3.1% code-review speed, but an estimated −1.5% delivery throughput and −7.2% delivery stability; 39% report little or no trust in AI-generated code; AI "does not appear to be a panacea" without small batches and robust testing [VERIFIED: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report, published 2024-10-23] ⚠.
- DORA 2025, *State of AI-assisted Software Development*: "AI's primary role is as an amplifier, magnifying an organization's existing strengths and weaknesses", with the largest returns from the "underlying organizational system" rather than the tools; the companion DORA AI Capabilities Model lists the practices [VERIFIED: https://dora.dev/research/2025/dora-report/, published 2025] ⚠.
- METR's randomized controlled trial (arXiv, July 2025): 16 experienced open-source developers, 246 tasks in mature repositories, early-2025 tools (Cursor Pro with Claude 3.5/3.7 Sonnet); allowing AI *increased* completion time by 19%, while developers had predicted a 24% speed-up and afterwards still believed they had been 20% faster [VERIFIED: https://arxiv.org/abs/2507.09089, published 2025-07-12 (v2 2025-07-25)] ⚠.
- Shopify's CEO memo (sent to staff in late March 2025, posted publicly 7 April 2025): employees must show they "cannot get what they want done using AI" before requesting headcount, embracing AI is a "fundamental expectation", and AI use will be part of performance reviews [VERIFIED: https://www.cnbc.com/2025/04/07/shopify-ceo-prove-ai-cant-do-jobs-before-asking-for-more-headcount.html, published 2025-04-07] ⚠.
- [ASSUMPTION/JUDGEMENT] For a commerce team the stability finding is the one that matters: AI tools raise output on connectors, theme code and app glue — exactly the code that touches stock and prices — so the controls that DORA names (small batches, tests, review) and the merchant's own app-scope governance (3.5) are the preconditions, not the afterthought.

**For newcomers.**
- *Sandbox / test store*: a copy of a service where nothing real happens (no money moves, no orders ship), used to try changes safely.
- *API version*: a dated edition of an API that a vendor promises to keep working for a stated period, so integrations do not break overnight.
- *Feature flag*: a switch in configuration that turns a feature on or off without redeploying code.
- *Stream-aligned team*: a team that owns one flow of customer value end to end (for example, "buy") rather than one technology.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- *Starting*: an agency builds, the founder owns the accounts; no environments beyond the test store and the PSP sandbox. *Growing*: the first in-house engineer owns the ownership map, the connector repository and the API-version pins; a staging store with marked test orders. *Omnichannel*: two journey teams, an integration owner, a peak plan, decision records, quarterly upgrade and app reviews, AI tooling with tests and review as the gate. *Group*: a platform team for the shared front end, integration layer and peak tooling; agency work scoped per brand against group standards.

---

## Key numbers

| Number | What | Source | Date |
| --- | --- | --- | --- |
| 1,000+ developers, ~6,000 Ruby classes | Shopify monolith when modularization began | shopify.engineering, Deconstructing the Monolith | 2019-02-21 |
| 2.8 million lines of Ruby, 500,000 commits, 37 components | Shopify core monolith | shopify.engineering, State of the Monolith | 2020-09-16 |
| 260+ teams, 1,300+ developers, 4,000+ applications, 140+ Kubernetes clusters | Zalando Tech | srcco.de | 2020-03-03 |
| ~2,200 microservices, ~70 domains, half-life ~1.5 years | Uber | uber.com blog | 2020-07-23 |
| 140+ services → 1 service; 3 engineers on upkeep | Segment destinations | Twilio Segment blog | 2018-07-10 |
| 90% cost reduction; prior design handled ~5% of load | Prime Video monitoring service | InfoQ (original removed) | 2023-05-03 |
| Shards differed almost 4x before rebalancing | Shopify shard balancing | shopify.engineering | 2021-09-24 |
| 100 / 200 / 1,000 / 2,000 points per second | Shopify GraphQL Admin rate by plan ⚠ | shopify.dev | accessed 2026-11 |
| 450 per 30 s (Scale), 150 per 30 s (Growth/Core) | BigCommerce API quota ⚠ | docs.bigcommerce.com | accessed 2026-11 |
| 2 s default, 10 s max, 25 per Project | commercetools API Extension timeout and count ⚠ | docs.commercetools.com | accessed 2026-11 |
| 11 million instructions, 10 MiB, 256 KiB module | Shopify Functions limits (API 2026-10) ⚠ | shopify.dev | accessed 2026-11 |
| 3 years standard support; cloud enforcement from 2027-06-01 | Adobe Commerce lifecycle ⚠ | experienceleague.adobe.com | accessed 2026-11 |
| 10 Lighthouse points | Max storefront slowdown an app may cause (Shopify review) | shopify.dev | accessed 2026-11 |
| "over 16,000 apps" | Shopify App Store ⚠ | apps.shopify.com | accessed 2026-11 |
| 3.6M+ active stores | WooCommerce ⚠ | developer.woocommerce.com | accessed 2026-11 |
| 4x–6x faster server response | Shopify Storefront Renderer vs legacy | shopify.engineering | 2020-08-20 |
| +8.4% conversions, +9.2% AOV per 0.1 s (retail, mobile) | Deloitte/Google | deloitte.com | 2020-03-24 |
| INP good ≤ 200 ms; replaced FID 2024-03-12 | Core Web Vitals | web.dev | 2024 |
| 9 new success criteria; Recommendation 2024-12-12 | WCAG 2.2 | w3.org | 2024-12-12 |
| Applies from 28 June 2025; microenterprise < 10 staff and ≤ EUR 2M exempt; transition to 28 June 2030 | European Accessibility Act | publications.europa.eu, CELEX 32019L0882 | 2019-06-07 |
| 583,000 orders per second; RMB 498.2 bn GMV | Alibaba 11.11 2020 | alibabacloud.com; alibabagroup.com | 2020-11 |
| $13.3 bn; $15.8 M per minute peak | US Cyber Monday 2024 (Adobe) | news.adobe.com | 2024-12-03 |
| $14.6 bn GMV; $5.1 M per minute peak | Shopify BFCM 2025 | shopify.com/news | 2025-12-02 |
| 7,200 orders per minute; 130,000 requests per second in load test | Zalando Cyber Week 2019 / 2019 load test | engineering.zalando.com | 2020-10-08 / 2019-04-11 |
| 150% of last year's load; 200 M requests per minute (p99); 80,000+ checkouts per minute | Shopify BFCM 2025 readiness targets | shopify.engineering | 2025-11-20 |
| 75% use AI daily; −1.5% throughput, −7.2% stability per +25% adoption | DORA 2024 ⚠ | cloud.google.com blog | 2024-10-23 |
| +19% task time with AI (expected −24%) | METR RCT, 16 developers, 246 tasks ⚠ | arxiv.org | 2025-07 |

## Open questions / not verifiable

- The primary text of the 2006 Vogels interview (monolith → services narrative, "two-pizza teams", number of services behind a page) could not be fetched; only "you build it, you run it" is verified through AWS's blog.
- No current public count of Amazon's or Zalando's services; Zalando's "4,000+ applications" is 2020.
- Prime Video's original 2023 post is gone; only InfoQ's account is available.
- Shopify's pod count, shop count per pod and the rules that assign shops to pods are not public; the 2018 and 2021 posts describe mechanisms, not sizes.
- Salesforce B2C Commerce sandbox model and cartridge documentation (developer.salesforce.com) returned 403; cartridge facts come from Trailhead and a search summary.
- SAP Commerce extension dependency mechanics (`extensioninfo.xml`) are described only in community sources; the official page fetched gives the concept, not the schema.
- DoorDash's monolith-to-microservices post (403) and Etsy's "Measure Anything" (403) were not usable.
- Shopify App Store exact counts and Adobe Commerce Marketplace counts; all app counts are marketing or tracker figures.
- The often-quoted PagerDuty post on Amazon alerting on orders per second could not be located; the "orders per minute" practice is stated as judgement supported by how peak operators report their own events.
- No dated practitioner source on merchant–agency engineering practice in NL/BE/DE; Part 6.5 is judgement.
- The seven capabilities of the DORA 2025 AI Capabilities Model and the 2025 survey size were not on the fetched page.
- Costco's 2019 Black Friday outage and other retailer-specific outage costs were not verified and are not used.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| How Do Committees Invent? | Melvin Conway, Datamation | 1968 | https://www.melconway.com/Home/Committees_Paper.html |
| A Conversation with Werner Vogels | ACM Queue (Jim Gray) | 2006 | https://queue.acm.org/detail.cfm?id=1142065 |
| ACM Queue Interview with Werner Vogels | AWS News Blog (Jeff Barr) | 2006 | https://aws.amazon.com/blogs/aws/acm_queue_inter |
| Microservices | James Lewis and Martin Fowler | 2014 | https://martinfowler.com/articles/microservices.html |
| MonolithFirst | Martin Fowler | 2015 | https://martinfowler.com/bliki/MonolithFirst.html |
| Microservice Trade-Offs | Martin Fowler | 2015 | https://martinfowler.com/articles/microservice-trade-offs.html |
| Completing the Netflix Cloud Migration | Netflix | 2016 | https://about.netflix.com/en/news/completing-the-netflix-cloud-migration |
| From monolith to microservices at Zalando (talk) | GOTO / Rodrigue Schaefer | 2016 | https://gotopia.tech/sessions/7/from-monolith-to-microservices-at-zalando |
| Zalando Engineering Principles (deprecated) | Zalando, GitHub | 2015/2020 | https://github.com/zalando/engineering-principles |
| One Decade in Zalando Tech | Henning Jacobs | 2020 | https://srcco.de/posts/one-decade-in-zalando-tech.html |
| Zalando RESTful API Guidelines | Zalando API Guild | n.d. | https://opensource.zalando.com/restful-api-guidelines/ |
| Deconstructing the Monolith | Shopify Engineering (Kirsten Westeinde) | 2019 | https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity |
| Under Deconstruction: The State of Shopify's Monolith | Shopify Engineering (Philip Müller) | 2020 | https://shopify.engineering/shopify-monolith |
| A Packwerk Retrospective | Shopify Engineering (Gannon McGibbon, Chris Salzberg) | 2024 | https://shopify.engineering/a-packwerk-retrospective |
| Medusa Architecture Overview | Medusa docs | n.d. | https://docs.medusajs.com/learn/introduction/architecture |
| Introducing Domain-Oriented Microservice Architecture | Uber Engineering (Adam Gluck) | 2020 | https://www.uber.com/blog/microservice-architecture/ |
| Goodbye Microservices | Twilio Segment (Alexandra Noonan) | 2018 | https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices/ |
| Prime Video Switched from Serverless to EC2 and ECS to Save Costs | InfoQ (Rafał Gancarz) | 2023 | https://www.infoq.com/news/2023/05/prime-ec2-ecs-saves-costs/ |
| MACH Alliance | MACH Alliance | n.d. | https://machalliance.org/ |
| Silo, Pool, and Bridge Models | AWS Well-Architected SaaS Lens | n.d. | https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/silo-pool-and-bridge-models.html |
| Noisy Neighbor | AWS Well-Architected SaaS Lens | n.d. | https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/noisy-neighbor.html |
| A Pods Architecture to Allow Shopify to Scale | Shopify Engineering (Xavier Denis) | 2018 | https://shopify.engineering/a-pods-architecture-to-allow-shopify-to-scale |
| MySQL Database Shard Balancing at Terabyte Scale | Shopify Engineering (Paarth Madan) | 2021 | https://shopify.engineering/mysql-database-shard-balancing-terabyte-scale |
| Platform Multitenant Architecture | Salesforce Architects | n.d. | https://architect.salesforce.com/fundamentals/platform-multitenant-architecture |
| General Concepts (Regions, Projects) | commercetools docs | n.d. | https://docs.commercetools.com/api/general-concepts |
| Limits | commercetools docs | n.d. | https://docs.commercetools.com/api/limits |
| API Extensions | commercetools docs | n.d. | https://docs.commercetools.com/api/projects/api-extensions |
| Connect | commercetools docs | n.d. | https://docs.commercetools.com/connect/ |
| Shopify API rate limits | Shopify.dev | n.d. | https://shopify.dev/docs/api/usage/limits |
| GraphQL Admin API rate limits | Shopify.dev | n.d. | https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits |
| Usage Plans and Rate Limits | Amazon Selling Partner API docs | n.d. | https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits |
| API rate limits | BigCommerce docs | n.d. | https://docs.bigcommerce.com/docs/start/best-practices/api-rate-limits |
| Plugins (interceptors) | Adobe Commerce PHP developer guide | n.d. | https://developer.adobe.com/commerce/php/development/components/plugins |
| Out-of-process extensibility | Adobe Commerce developer docs | n.d. | https://developer.adobe.com/commerce/extensibility/ |
| Upgrade best practices | Adobe Experience League | n.d. | https://experienceleague.adobe.com/en/docs/commerce-operations/upgrade-guide/prepare/best-practices |
| Upgrade Compatibility Tool overview | Adobe Experience League | 2026 | https://experienceleague.adobe.com/en/docs/commerce-operations/upgrade-guide/upgrade-compatibility-tool/overview |
| Adobe Commerce lifecycle policy | Adobe Experience League | n.d. | https://experienceleague.adobe.com/en/docs/commerce-operations/release/planning/lifecycle-policy |
| Pro architecture (environments) | Adobe Experience League | n.d. | https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/architecture/pro-architecture |
| Adobe Commerce Storefront | Adobe Experience League | n.d. | https://experienceleague.adobe.com/developer/commerce/storefront/ |
| Extension Concept | SAP Help Portal (SAP Commerce 2205) | n.d. | https://help.sap.com/doc/b490bb4e85bc42a7aa09d513d0bcb18e/2205/en-US/8bbf0b9d866910149688b8d696c8d47e.html |
| Hooks | WordPress Plugin Handbook | n.d. | https://developer.wordpress.org/plugins/hooks/ |
| Getting started building extensions | WooCommerce developer docs | n.d. | https://developer.woocommerce.com/docs/extensions/getting-started-extensions/ |
| Extensions (plugins vs apps) | Shopware developer docs | n.d. | https://developer.shopware.com/docs/concepts/extensions/ |
| Customize with cartridges | Salesforce Trailhead | n.d. | https://trailhead.salesforce.com/content/learn/modules/b2c-cartridges/b2c-cartridges-customize |
| SFRA Features and Components | Salesforce developer docs (403 in session) | n.d. | https://developer.salesforce.com/docs/commerce/sfra/guide/b2c-sfra-features-and-comps.html |
| Apps overview | Saleor docs | n.d. | https://docs.saleor.io/developer/extending/apps/overview |
| Shopify Functions | Shopify.dev | n.d. | https://shopify.dev/docs/apps/build/functions |
| Function APIs (limits) | Shopify.dev, API 2026-10 | 2026 | https://shopify.dev/docs/api/functions |
| Script Editor (retired) | Shopify Help Center | 2026 | https://help.shopify.com/en/manual/checkout-settings/script-editor |
| App requirements checklist | Shopify.dev | n.d. | https://shopify.dev/docs/apps/launch/app-requirements-checklist |
| Shopify App Store | Shopify | n.d. | https://apps.shopify.com/ |
| Shopify App Store statistics | MageComp (tracker) | 2026 | https://magecomp.com/blog/shopify-app-store-statistics/ |
| App marketplace requirements | BigCommerce docs | n.d. | https://docs.bigcommerce.com/docs/integrations/apps/guide/requirements |
| How Shopify Reduced Storefront Response Times with a Rewrite | Shopify Engineering (Maxime Vaillancourt) | 2020 | https://shopify.engineering/how-shopify-reduced-storefront-response-times-rewrite |
| Stencil | BigCommerce docs | n.d. | https://docs.bigcommerce.com/docs/storefront/stencil/start |
| Hydrogen | Shopify.dev | n.d. | https://shopify.dev/docs/storefronts/headless/hydrogen |
| PWA Kit | Salesforce Commerce Cloud, GitHub | n.d. | https://github.com/SalesforceCommerceCloud/pwa-kit |
| Next.js Commerce (archived) | Vercel, GitHub | n.d. | https://github.com/vercel/commerce |
| Unified Data Layer | Alokai docs | n.d. | https://docs.alokai.com/unified-data-layer |
| Incremental Static Regeneration | Vercel docs | 2026 | https://vercel.com/docs/incremental-static-regeneration |
| Milliseconds Make Millions | Deloitte Ireland for Google | 2020 | https://www.deloitte.com/ie/en/services/consulting/research/milliseconds-make-millions.html |
| The business impact of Core Web Vitals | web.dev | n.d. | https://web.dev/case-studies/vitals-business-impact |
| INP becomes a Core Web Vital on March 12 | web.dev | 2024 | https://web.dev/blog/inp-cwv-march-12 |
| Interaction to Next Paint (INP) | web.dev | n.d. | https://web.dev/articles/inp |
| What are Progressive Web Apps? | web.dev | n.d. | https://web.dev/articles/what-are-pwas |
| Web Content Accessibility Guidelines (WCAG) 2.2 | W3C | 2024 | https://www.w3.org/TR/WCAG22/ |
| Directive (EU) 2019/882 (European Accessibility Act) | Publications Office of the EU | 2019 | http://publications.europa.eu/resource/celex/32019L0882 |
| Alibaba Cloud Unveils 'Magic' Behind 11.11 | Alibaba Cloud press room | 2020 | https://www.alibabacloud.com/press-room/magic-behind-the-worlds-largest-online-shopping-festival |
| Alibaba Generates RMB498.2 billion GMV during 2020 11.11 | Alibaba Group | 2020 | https://www.alibabagroup.com/document-1491144671282331648 |
| Cyber Monday 2024 recap | Adobe (Adobe Analytics) | 2024 | https://news.adobe.com/news/2024/12/120324-adi-cyber-monday-recap |
| BFCM 2025 data | Shopify News | 2025 | https://www.shopify.com/news/bfcm-data-2025 |
| BFCM Readiness 2025 | Shopify Engineering (Kyle Petroski, Matthew Frail) | 2025 | https://shopify.engineering/bfcm-readiness-2025 |
| End-to-end load testing Zalando's production website | Zalando Engineering | 2019 | https://engineering.zalando.com/posts/2019/04/end-to-end-load-testing-zalandos-production-website.html |
| How Zalando prepares for Cyber Week | Zalando Engineering (Bartosz Ocytko) | 2020 | https://engineering.zalando.com/posts/2020/10/how-zalando-prepares-for-cyber-week.html |
| Using load shedding to avoid overload | Amazon Builders' Library (author shown as "David", Sr. Principal Engineer) | 2019 | https://builder.aws.com/content/3Eun1EEyX6p2e3VYNyRLSJzLuMV/using-load-shedding-to-avoid-overload |
| Feature Toggles (aka Feature Flags) | Pete Hodgson, martinfowler.com | 2017 | https://martinfowler.com/articles/feature-toggles.html |
| Amazon internal documents on the Prime Day crash | CNBC | 2018 | https://www.cnbc.com/2018/07/19/amazon-internal-documents-what-caused-prime-day-crash-company-scramble.html |
| Cloudflare Waiting Room (launch post) | Cloudflare blog | 2021 | https://blog.cloudflare.com/cloudflare-waiting-room/ |
| Waiting Room overview, configuration settings, queueing methods | Cloudflare docs | n.d. | https://developers.cloudflare.com/waiting-room/ |
| How does Queue-it work? | Queue-it | n.d. | https://queue-it.com/how-does-queue-it-work/ |
| Service Level Objectives (SRE book, ch. 4) | Google | 2017 | https://sre.google/sre-book/service-level-objectives/ |
| Development stores | Shopify.dev; Shopify Help Center | n.d. | https://shopify.dev/docs/apps/build/dev-dashboard/stores/development-stores |
| Testing use cases / sandboxes | Stripe docs | n.d. | https://docs.stripe.com/test-mode |
| API versioning | Shopify.dev | n.d. | https://shopify.dev/docs/api/usage/versioning |
| Key Concepts | Team Topologies (Skelton and Pais) | n.d. | https://teamtopologies.com/key-concepts |
| Announcing the 2024 DORA report | Google Cloud blog | 2024 | https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report |
| State of AI-assisted Software Development 2025 | DORA | 2025 | https://dora.dev/research/2025/dora-report/ |
| Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | METR (Becker, Rush, Barnes, Rein), arXiv | 2025 | https://arxiv.org/abs/2507.09089 |
| Shopify CEO: prove AI can't do the job before asking for headcount | CNBC | 2025 | https://www.cnbc.com/2025/04/07/shopify-ceo-prove-ai-cant-do-jobs-before-asking-for-more-headcount.html |
