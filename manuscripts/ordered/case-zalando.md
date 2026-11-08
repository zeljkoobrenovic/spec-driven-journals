{id: case-zalando}
# 48. Case: Zalando, Microservices, Platform Strategy and the Return to Discipline

![Case: Zalando, Microservices, Platform Strategy and the Return to Discipline — logo](commerce-platform-architecture/posts/48-case-zalando/assets/images/48-case-zalando/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow Zalando's own dated accounts from the 2015 microservices move through the corrections that followed, and take from them what a merchant can use about modularity, API contracts and becoming a platform.

> **KEY POINTS:**
>
> * **Zalando split its shop for team autonomy, not for load, and said so.** In 2015 a shared codebase and slow deployments blocked 85-plus teams; the fix was organizational first (small teams, an AWS account each, a paved road called STUPS) and architectural second. The service count followed the team count.
> * **The durable export is a written API standard, not the service count.** Zalando's guidelines, open since 2016 and still maintained in 2026, say what a merchant should demand of every vendor: extend compatibly instead of versioning, never break consumers, and sunset an API only with client consent, a date, headers and usage monitoring.
> * **Autonomy was followed by a decade of discipline.** Alignment over raw autonomy (2018), fewer languages (2020), one developer portal (2023) and, in 2025, a synchronous read API replacing a price-and-stock event stream that fell 30 minutes behind at Cyber Week and bred divergent copies of product data. Events propagate change; they are not the system of record.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-commerce-platforms-go-wrong):**
>
> * **The Giant's Boots** — Zalando's microservices move is copied for its shape; the record shows it was made for 85-plus teams and corrected for a decade afterward.
> * **The Pulled Rug** — Zalando's deprecation rules (consent, a sunset date, headers, usage monitoring) are the written cure for the vendor API change that breaks an integration before anyone is told.
> * **The Message in a Bottle** — Zalando's 2025 post documents what happens when consumers rebuild their own copy of price and stock from a stream they cannot keep up with: delays and divergent copies.

A merchant listing products on Zalando depends on a platform that serves shoppers, connects sellers and offers fulfillment services. Those jobs create coordination problems within Zalando as well as across the merchant's integrations. The Berlin fashion platform reported **€17.6 billion in gross merchandise volume**, **62 million active customers** and **278.6 million orders** for 2025 (March 2026 fact sheet). Its engineering choices address that scale; merchants such as Kestrel & Pine, the fictional brand used here, need to understand which lessons apply to their smaller operation.

From 2015, Zalando described a move to independently deployed services and autonomous teams. Later posts addressed shared standards, fewer technologies and common developer tools. A 2025 account even replaced one event-based integration with direct API calls. The case is useful because it exposes the costs of earlier decisions as well as their rationale.

Read the **2015–2017 accounts as history**, alongside newer business filings and 2023–2026 AI material. Each claim is dated; inferred internals remain labeled. "Return to discipline" is this chapter's interpretation of successive posts, not a program Zalando announced. [Case: Amazon, From Monolith to Services to the Everything Store](#case-amazon) applies the same evidence discipline to another company.

**Where we are in the order's journey.** A merchant listing a jacket on Zalando needs correct price and stock, an imported order and a maintained API contract. [Selling on Someone Else's Platform: Marketplaces and Channel Integration](#marketplaces-and-channel-integration), [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability) and [Promises Between Systems: API Contracts, Webhooks and Versioning](#api-contracts-and-versioning) explain those responsibilities from the merchant's side.

{id: case-zalando--chapter-2015-jimmy-radical-agility-and-the-split}
## 2015: Jimmy, Radical Agility and the Split

A **monolith** is one deployed application with a shared codebase. **Microservices** split work into separately deployed programs that communicate over a network. An **autonomous team** owns its services in production and has freedom over tools and process. The practical question is how much independence helps teams deliver without making coordination harder.

Zalando's monolith, **Jimmy**, blocked teams through slow startup and complicated deployments, according to its October 2015 post. The stated problem was release speed and shared code, rather than traffic alone.

In May 2015, seven engineers and a designer began rebuilding the Fashion Store, then fifteen country sites serving over sixteen million active customers. Teams would own programming, testing, deployment and operations. A router called **Skipper**, later open-sourced, directed requests between the old and new parts.

The organizational side was called **Radical Agility**, introduced in March 2015 and built, by trade accounts of 2016, on autonomy, mastery and purpose, with teams of three to seven people owning a topic end to end. Zalando's own July 2015 post has Eric Bowman, then VP Engineering, at the AWS Summit in Berlin: "We think of teams as a unit of trust"; "we've tried to create the context where people can make mistakes and it's not fatal". By February 2016 a Zalando talk at the MicroXchange conference covered microservices across "our 85+ engineering teams"; by December 2016 InfoQ reported "about 110 teams", more than 1,400 people in Tech across six hubs, and "each team has its own AWS account".

That last fact needed a platform. **STUPS** was Zalando's answer: an **internal platform-as-a-service**, meaning one supported way for every team to deploy to the cloud. Development began in late 2014 and it was available for production to every team in May 2015. InfoQ's April 2016 account describes it as "a convenient and audit-compliant Platform-as-a-Service" on AWS: "Our employees get nearly administrative access to their AWS accounts with almost no restrictions", with near-real-time audit reporting because "Auditors need to know that we're complying with the regulations" (card-industry, financial-reporting and German rules). In plain words: Zalando gave every team its own cloud account and built the tooling that made that auditable.

The shop itself was rebuilt as **fragments**, pieces of a page owned by different teams and deployed separately, assembled behind the router. One year in, in October 2016, the effort was renamed Project Mosaic: header and footer fragments were live, product-page and wish-list fragments were going live, and the author described a shift "from prototyping to performance optimization" and toward "stable components that other teams can depend on".

![Diagram: The 2015–2016 shape as Zalando described it](commerce-platform-architecture/posts/48-case-zalando/assets/images/48-case-zalando/fig01-2015-2016-shape-zalando-described-it.jpeg)

**Figure 1:** *The 2015–2016 shape as Zalando described it: a router in front, a page assembled from fragments each owned and deployed by one team, and each team on its own cloud account behind a shared, audited platform.*

A smaller post from April 2016 is the most honest about the first months: a team in Dortmund cut its domain into two services, then into eight after modeling the boundaries properly ("Define your Microservices properly and know your boundaries"), and replaced a failed upfront plan with weekly goals.

> **INFERENCE, NOT DOCUMENTED:** Zalando's documented sequence mirrors Amazon's with a thirteen-year lag and a different stated motive. Amazon's 2006 account names a scaling wall; Zalando's 2015 posts name team autonomy. The fix was organizational first (teams, accounts, a paved road) and architectural second, which is why the service count tracked the team count: 85-plus teams in early 2016, about 110 by December, and by 2020 "4,000+ applications" for "1,200+ developers". A merchant with fourteen people in technology, like Kestrel & Pine, is below the team count at which any of this applies. What transfers is the *order of operations*: decide who owns what before deciding how to split what, which is the argument of [Who Owns the Truth: Boundaries, Bounded Contexts and Systems of Record](#boundaries-and-systems-of-record) and [Who Builds and Who Owns: Teams, Vendors, Agencies and Governance](#organizing-commerce-engineering).

{id: case-zalando--the-cost-of-distributed-data-stated-early}
## The Cost of Distributed Data, Stated Early

The clearest early statement of what the split would cost came not from the shop teams but from business intelligence. In September 2015 a Zalando post observed that the monolith's "consolidation of data in a single place makes business intelligence fairly simple", whereas "with each service owning its data, data is spread over a significantly larger number of cloud-based microservices"; article and order data alone were spread across eight PostgreSQL databases. Zalando's response was to deploy Kafka, a message log, on AWS "to make our event data available for downstream systems", and to plan a data lake.

Two terms. An **event** is a message sent the moment something happens (an order placed, a price changed) so other systems can react. An **event bus** is the shared channel on which services publish events and others subscribe.

Zalando's event bus was **Nakadi**, started in October 2015: in its own README, "a distributed event bus that implements a RESTful API abstraction on top of Kafka-like queues", with a schema registry so that producers register an event type with a **schema** (the agreed shape of the message) before publishing, and every event is validated against it.

By May 2017 a Zalando post on "third-generation microservices" described the intended style: services "process incoming events and data from other services", and data streaming becomes "a central part of the service fabric".

> **INFERENCE, NOT DOCUMENTED:** This is the earliest honest statement in the record of the rule [Built to Disagree and Recover: Events, Eventual Consistency and Reconciliation](#events-consistency-and-reconciliation) is built on: once each system owns its own data, there is no single place to query, so analytics and reconciliation need a stream of what happened. Kestrel & Pine meets this problem without a single microservice: its thirteen systems hold orders in four places and product data in four, and its data warehouse has three definitions of an order (Waypoint decision W7 picks one). An Omnichannel merchant meets the *data* problem of distribution long before the *team* problem, and should take the event-stream lesson without the service count.

{id: case-zalando--the-api-guild-and-the-guidelines}
## The API Guild and the Guidelines

The piece of Zalando's 2015 work that is still alive, still public and still maintained in 2026 is its API standard. It began as the **API Guild** in March 2015: an informal group of about 20 people who set standards and review APIs as "a sounding board and review resource, not an approval board, to avoid bottlenecks", spending about 10% of their week on it. The September 2015 post explains why it mattered to the business: Zalando's "open platform strategy relies on public APIs used by external partners", so "We cannot afford to break our APIs", and "Ideally, all Zalando APIs should look like the same author created them".

The principle is **API First**: the interface is designed and reviewed, as an OpenAPI document (a machine-readable description of an API), before any code is written. By December 2016 the guidelines were open-sourced; Zalando described API definitions as "a source truth, part of a contract between a service provider and consumers". The current guidelines (undated page, accessed November 2026) use the MUST, SHOULD and MAY of internet standards and say teams "must define APIs first, before coding its implementation, using OpenAPI as specification language" and should "Treat your API as product and act like a product owner".

The rules that matter most to a merchant are the ones about change. In plain words, a **compatible extension** adds to an API without breaking anyone who already uses it; **versioning** publishes a second, different API beside the first; **deprecation** announces that an API will stop; a **sunset** is the date it does.

| Rule (Zalando guideline number) | What it says, in plain words | What Kestrel & Pine should demand of a vendor |
| --- | --- | --- |
| #106 MUST not break backward compatibility | "Change APIs, but keep all consumers running" | Additive changes only inside a version |
| #107 SHOULD prefer compatible extensions; #113 SHOULD avoid versioning | Add fields rather than publishing a new version | A changelog of additions, not surprise versions |
| #108 MUST prepare clients to accept compatible extensions | Clients ignore fields they do not know (the **tolerant reader**) | Its own integrations must not fail on a new field |
| #114 MUST use media type versioning; #115 MUST not use URL versioning | When a version is unavoidable, put it in the content type, not the address | A stated versioning scheme, whichever it is |
| #185 MUST obtain approval of clients before API shut down; #186 MUST collect external partner consent on deprecation time span | No sunset until "all clients have given their consent on a sunset date" | A deprecation notice with a date agreed in advance |
| #187 MUST reflect deprecation in API specifications; #189 SHOULD add Deprecation and Sunset headers | `deprecated: true`, the sunset date and migration guidance in the spec; headers on every response | Machine-readable deprecation, so a script can warn before it breaks |
| #188 MUST monitor usage of deprecated API scheduled for sunset | The provider watches who is still calling | A warning to the merchant while it is still calling |
| #191 MUST not start using deprecated APIs | A client never builds on something already marked for removal | The agency checks before building |

The companion to the guidelines is the **Tech Radar**, created in 2016 "to inspire and support teams to pick the best technologies for new projects". A Technologist Guild of about 25 senior people assigns technologies to rings by vote: ADOPT ("high confidence in to serve our purpose, also in large scale"), TRIAL, ASSESS and HOLD ("not recommended to be used for new projects"). In 2016 "Teams must use the Tech Radar as one input source for their technology decisions"; that wording changes in 2020.

![Diagram: Deprecation as Zalando's guidelines prescribe it](commerce-platform-architecture/posts/48-case-zalando/assets/images/48-case-zalando/fig02-deprecation-zalando-s-guidelines-prescribe-it.jpeg)

**Figure 2:** *Deprecation as Zalando's guidelines prescribe it: announce in the specification, obtain consent on a date, signal in headers, monitor who still calls, and only then sunset; every step is a chance to avoid the Pulled Rug.*

Kestrel & Pine learned the value of these rules the expensive way. In February 2027 its marketplace connector retired an API version on a published date; the agency script that read it had not been updated, and stock to bol was stale for two days (the ledger's Deprecated Endpoint). Every row in the table above describes a step that would have caught it: a machine-readable deprecation, a header the script could have logged, usage monitoring that would have shown the script still calling. [Promises Between Systems: API Contracts, Webhooks and Versioning](#api-contracts-and-versioning) turns the guidelines into the book's contract rules.

{id: case-zalando--the-return-to-discipline-2018-to-2026}
## The Return to Discipline, 2018 to 2026

No single Zalando post declares that the autonomy era ended. The posts that follow narrow a choice each time, and read in order they tell one story.

| Year | What Zalando published | What narrowed |
| --- | --- | --- |
| 2018 | Bowman, by then leading a 500-person group, told InfoQ in September: "Our biggest challenge was that we treated autonomy like an input to teams"; unaligned teams were like "air molecules in a balloon: moving fast but not running together as a group"; autonomy became "an aspiration and a reward, not a gift"; "a set of principles and systems scales better than a set of prescriptions". Teams were embedded across the company with shared objectives and company-wide "Global Projects". | Autonomy without alignment |
| 2018 | The agile coaches: "we value principles more than frameworks"; six principles replace a single prescribed method (August). | One mandated process, replaced by principles |
| 2020 | With "1,200+ developers" and "4,000+ applications", Zalando "redefined the ring semantics" of the radar, wrote Technology Selection Principles, gave a Principal Engineering community the decision, required a sponsoring Engineering Head for TRIAL technologies, and stopped new applications in Clojure, Haskell and Rust in favor of Kotlin and TypeScript, because "A broad freedom of choice leads to increased difficulties in supporting software long-term" (July). | Free choice of language |
| 2023 | **Sunrise**, an internal developer portal built on Backstage since 2021, replaced "more than 100 disconnected interfaces" with one portal holding "over 40k registered entities (applications, teams, and users)" and 27 integrated tools; old tools were shut down (August). | Many tools, replaced by one paved road |
| 2023 | On 21 February the co-CEOs announced the removal of "several hundred overhead roles", about 5% of roughly 17,000 employees, sparing logistics, customer care and outlets (Retail Gazette). | Overhead |
| 2025 | The event-driven price and stock pipeline "became a bottleneck, introducing delays and scaling challenges"; it was replaced by a synchronous Product Read API (March). | A stream as the only source of current state |
| 2026 | Connected Retail, the ship-from-store program launched in 2018, is folded into the standard partner program; its technology "will be discontinued by June 30, 2027" (FashionUnited, April). | A separate channel technology |

Three terms. A **paved road**, or internal developer platform, is one supported way to build, deploy and find services so teams do not each solve the same problem. A **technology radar with teeth** is a list of allowed technologies teams must follow rather than consult. A **synchronous read API** is one that answers "what is the price now" when asked, instead of making the caller rebuild its own copy from a stream of changes.

The evidence does not support "microservices failed at Zalando". It supports something more specific: **autonomy produced too many technologies, too many tools and, on one critical path, an integration that could not keep up**, and each was fixed by narrowing a choice. Zalando today reports more than 17,000 employees, around 3,000 in technology and more than 7,000 in fulfillment centers (annual report 2025, March 2026).

![Many scattered paths leaving a balloon of arrows labeled Autonomy and merging past signposts 2018, 2020, 2023 and 2025 into one paved road.](commerce-platform-architecture/posts/48-case-zalando/assets/images/48-case-zalando/48-autonomy-narrowed-to-a-paved-road.jpeg)

**Figure 3:** *Zalando's return to discipline narrowed one choice at a time: alignment in 2018, fewer languages in 2020, one developer portal in 2023 and a read API in 2025.*

{id: case-zalando--chapter-2025-when-the-event-stream-fell-behind}
## 2025: When the Event Stream Fell Behind

The 2025 post deserves its own section because it is the most useful single document in the case for a merchant, and because it is the Black Friday Oversell told by a platform.

Zalando's price and stock updates were published as events. Consumers, the systems that needed current prices and stock, subscribed to the stream and maintained their own copies. The March 2025 post "From Event-Driven to API" reports what happened at scale: "over 90% of each payload unchanged" was being reprocessed, because an event carried the whole record even when one field had changed; during Cyber Week events "could be delayed by up to 30 minutes"; and teams that could not consume the streams fast enough used other sources, producing "divergent versions of product data". The pipeline was replaced by a synchronous, low-latency **Product Read API** (PRAPI): callers ask for the current price and stock and get an answer now.

![Diagram: Before 2025, every consumer rebuilt its own copy of price and stock from a stream of full records and the copies diverged under load](commerce-platform-architecture/posts/48-case-zalando/assets/images/48-case-zalando/fig03-before-2025-every-consumer-rebuilt-own.jpeg)

**Figure 4:** *Before 2025, every consumer rebuilt its own copy of price and stock from a stream of full records and the copies diverged under load; after, consumers ask the owner for the current value, and the stream is no longer the only way to know the truth.*

In plain words: an event is the right way to tell everyone that something changed. It is the wrong way to be the only place the current value can be learned, because then every consumer is a copy, every copy can lag, and on the busiest day the lag is largest. Kestrel & Pine's stock sync chain, WMS to ERP every 15 minutes, ERP to platform hourly, platform to marketplace connector hourly, is a slower version of the same design: a chain of copies, each one stale by the time it is read, which is how the Ridgewalker kept selling for two hours after it sold out at 19:40 on 27 November 2026.

![Stock notes passed from WMS to ERP to Platform to Connector, with clocks reading 15 min and hourly, while the empty shelf at the start contrasts with a jacket still for sale at the end.](commerce-platform-architecture/posts/48-case-zalando/assets/images/48-case-zalando/48-kestrel-pine-chain-of-copies.jpeg)

**Figure 5:** *Kestrel & Pine's stock sync is a chain of copies, WMS to ERP every 15 minutes, then hourly to the platform and hourly to the connector, which is how the Ridgewalker kept selling for two hours after it sold out.*

> **INFERENCE, NOT DOCUMENTED:** Zalando does not describe PRAPI's internals, its caching or how events and the API now coexist, so the diagram shows the documented before and after, not the implementation. The rule I draw is the one Waypoint decision W1 encodes: keep a **system of record** for stock and price, an **availability service** that answers "can I promise this unit on this channel now" through an API, and use events to propagate change and to feed reconciliation, not as the only source of truth. Events for "what happened"; a read API for "what is it now"; a reconciliation job for "do the copies still agree" ([Built to Disagree and Recover: Events, Eventual Consistency and Reconciliation](#events-consistency-and-reconciliation)). The 30-minute figure is Zalando's; the two-hour figure is Kestrel & Pine's; the shape of the failure is the same.

{id: case-zalando--the-platform-pieces-what-survived}
## The Platform Pieces: What Survived

Zalando open-sourced much of what it built in 2015, and the status of those projects in November 2026 is itself evidence.

| Project | What it is, in Zalando's words | Status on 7 November 2026 |
| --- | --- | --- |
| STUPS (for example Senza) | audit-compliant platform-as-a-service on AWS for autonomous teams | Senza archived; last change March 2023 |
| Skipper | "An HTTP router and reverse proxy for service composition"; used "as shop frontend http router with 350000 routes" and as the ingress controller "in more than 100 production clusters" | Active; changed the day before the check |
| Patroni | "a Python template for building PostgreSQL high availability (HA) clusters", introduced on Zalando's blog in February 2016, now under its own organization | Active |
| Nakadi | the event bus described above | Archived June 2024: "no longer developed in the open as we've not seen usage outside of Zalando for many years" |
| RESTful API and Event Guidelines | "A model set of guidelines for RESTful APIs and Events, created by Zalando" | Active; changed September 2026 |
| Tech Radar | the radar page and its generator | Active; changed October 2026 |
| Zalenium | container-based test grid | Archived September 2021: "no new maintainers were found" |

> **INFERENCE, NOT DOCUMENTED:** The pieces that survived are the ones with a life outside Zalando: a router, a database failover template and a written standard. The pieces tied to the 2015 account-per-team model (STUPS) or used only internally (Nakadi) were archived. Read the table as a warning against building platform tooling only one company needs. Archiving Nakadi says nothing about whether Zalando still uses an event bus internally; the README says only that nobody outside did.

{id: case-zalando--a-retailer-becoming-a-platform}
## A Retailer Becoming a Platform

Zalando's business story runs parallel to its architecture story, and the two meet at the warehouse.

Three terms. In the **partner program**, a brand sells on Zalando as the seller of record (the legal seller who issues the invoice and owes the consumer rights) and Zalando takes a commission, as opposed to Zalando's **wholesale** model in which it buys the stock and sells it itself. **Ship-from-store** sells a physical store's shelf stock online and ships it from the store. **Logistics as a service** offers a retailer's warehouses, carriers and software to other sellers, for orders on and off its own platform.

| Year | Move | Documented figures |
| --- | --- | --- |
| 2011 | **Partner Program** launches: brands sell as seller of record through the zDirect portal | June 2021: "more than 600 partners, representing over 2,000 brands"; about a quarter of GMV; a target of 40% by 2023 and half in the long term (targets now dated) |
| 2018 | **Connected Retail** launches: stores' stock sold on Zalando, collected by carriers (DHL in Germany, PostNL in the Netherlands), returns back to the store | March 2020: "more than 1,500" stores in Germany and the Netherlands, commissions waived for April–May 2020; January 2021: "more than 2,600"; February 2021: "over 3,000 active stores" in nine markets |
| 2010s–2021 | **Zalando Fulfillment Solutions** (ZFS) and Shipping Solutions: Zalando's warehouses and carriers for partners | June 2021: access to 16 European markets, "more than 2,300 market expansions" in 18 months |
| 2022–2023 | Multi-channel fulfillment pilot (2022), rebranded **ZEOS** Fulfillment in October 2023: one stock pool for Zalando, own-shop and other-platform orders, open to sellers "whether or not they sell through Zalando" | End of 2025: 25 markets, "over 600 partners selling across 18 sales channels (including Zalando), covering around 85% of the European marketplace volume" (annual report) |
| 2025 | **ABOUT YOU** acquired: intention announced 11 December 2024, completed 11 July 2025 at 91.45%, squeeze-out registered 6 November 2025 at €6.50 a share; B2C runs two brands on shared logistics and payment infrastructure | Targeted group synergies "around €100 million per year" |
| 2025 | B2B segment defined as ZEOS Fulfillment (including ZFS and multi-channel fulfillment), the commerce platform **SCAYLE** and the integration product **Tradebyte** | FY2025 B2B revenue €1,091.3 million (+14.6%), adjusted EBIT €53.9 million; 330 online shops on SCAYLE; a ZEOS app for Shopify's European merchants |
| 2026 | Connected Retail folded into the partner program; same standard fees for all partners from September 2026; technology discontinued by 30 June 2027 | "We are not saying goodbye to brick and mortar stores; we are simply updating the technology they use to connect with us" |

The FY2025 fact sheet (12 March 2026) gives the scale around this: GMV €17,560.2 million (+14.7%), revenue €12,346.1 million (+16.8%), adjusted EBIT €590.7 million, 278.6 million orders at 4.8 orders per customer and an average basket of €62.8. Reported growth includes ABOUT YOU; Zalando's guidance for 2026 is pro-forma growth of 5 to 10%, the honest measure of the core business. The partner share of group GMV fell to 32.1% from 34.2% because ABOUT YOU "currently operates with a lower partner business share". Zalando's December 2025 strategy note counts "over 60" live merchants on its fulfillment service; the annual report's 600 partners span all B2B services.

> **INFERENCE, NOT DOCUMENTED:** Zalando's platform story is Amazon's in European form and on a European timetable: marketplace (2011), then ship-from-store (2018), then fulfillment for partners, then fulfillment for anyone on any channel (2023), then the shop software itself (SCAYLE, in the group from 2025). The architectural consequence is the one [Case: Amazon, From Monolith to Services to the Everything Store](#case-amazon) drew: **one stock pool serving several seller-of-record models and several demand channels**, which is the Omnichannel-stage problem (own site, stores, wholesale, marketplaces) at a much larger scale. Two cautions are in the record. Connected Retail shows that a channel built on its own technology gets consolidated once the general program can do the job. And the partner share falling after the ABOUT YOU merger shows that an acquisition imports the acquired company's model mix, not only its revenue ([What Changes at Each Scale: From First Store to Group](#commerce-scaling-stages)).

{id: case-zalando--ai-at-zalando-discovery-first-then-identity}
## AI at Zalando: Discovery First, Then Identity

On 19 April 2023 Zalando announced a beta "fashion assistant powered by ChatGPT" for selected customers in four countries, letting them describe what they want in their own words and refine the results in conversation. The annual report for 2025 says the Zalando Assistant "was used by over 6 million customers" that year, and that Zalando sees "the emerging channel of agentic commerce as a great opportunity" while noting "the rise of AI agents as digital gatekeepers".

The engineering side came in September 2026. Zalando described an internal agentic platform on Kubernetes and open-sourced an **Agentic Identity Broker** that "lets agents act on behalf of users without ever holding provider tokens".

Two terms: **delegated access** means a user allows an agent to act with a subset of the user's permissions ("Delegated access is the intersection of both the user and agent permissions"), and **token exchange** means the broker swaps the agent's identity for a short-lived credential scoped to one action, so the agent never holds the user's real credentials.

The post adds that consent "should name a business capability ... instead of presenting a raw scope string", and that stronger approval is planned for high-risk transactions because users rubber-stamp approvals.

> **INFERENCE, NOT DOCUMENTED:** The 2023 assistant is a search feature: finding products in natural language. The 2026 broker is the infrastructure answer to the question Amazon answered with a policy and a lawsuit: who is this agent, for whom does it act, and what may it do. Read the two cases together. Amazon states the rule for *external* agents; Zalando publishes the identity model for *internal* ones. For Kestrel & Pine the broker is a preview of what Waypoint decision W8 will require before any agent may place or change an order: an identity for the agent, a named person it acts for, and a scope a human can read. [Assistants and Agents: AI in Commerce and What Is Real in 2026](#ai-and-agentic-commerce) owns the subject; the identity model is also treated in the sibling book at [Agent Identity, Delegation and Least Privilege](https://zeljkoobrenovic.github.io/spec-driven-journals/agentic-systems-architecture/agent-identity-and-least-privilege.html).

{id: case-zalando--what-zalando-teaches}
## What Zalando Teaches

The table is the author's synthesis; each row names its evidence.

| Lesson | Evidence | Transfers to a merchant? |
| --- | --- | --- |
| Decide ownership before decomposition; the service count follows the team count | 2015 posts; 110 teams (2016); 4,000+ applications (2020) | The order of operations, yes; the count, only at the Group stage |
| A written API standard outlives the architecture it was written for | Guild (2015); guidelines active in 2026 | Yes, as what to demand of vendors first and what to write for internal APIs later |
| Deprecate only with consent, a date, headers and monitoring | Guidelines #185–#191 | Yes; it is the cure for the Pulled Rug |
| Distributed data needs an event stream for analytics and reconciliation | 2015 BI post; Nakadi | Yes, at the Omnichannel stage, without the service count |
| An event stream must not be the only source of current state | 2025 Product Read API post | Yes; a read API on the system of record, events for propagation |
| Autonomy needs alignment, a bounded technology set and one paved road | 2018, 2020, 2023 posts | At the Group stage; a small team gets this for free from one platform |
| Build platform tooling only one company needs and it will be archived | STUPS, Nakadi, Zalenium status | Yes, at every stage |
| A retailer becomes a platform through logistics, then software; consolidation follows | 2011–2026 timeline | The pool-serving-many-channels idea, yes; the business, only at scale |

**Kestrel & Pine takes two practices from the case.** Waypoint, its improvement program, requires integration owners to track API versions and retirement notices under **W5**. That addresses the February 2027 script failure that left marketplace stock stale for two days.

Under **W1**, stock events feed an availability service that answers current availability through an API, with periodic reconciliation. That avoids reproducing the Black Friday chain of delayed copies. Neither lesson requires copying Zalando's thousands of applications or large engineering organization into a fourteen-person team.

{id: case-zalando--where-the-evidence-stops}
## Where the Evidence Stops

- **The current architecture.** Zalando has not published its service inventory, its order or pricing architecture, the internals of ZEOS or how PRAPI and its event streams coexist today. The 2015–2017 posts describe systems that have been replaced.
- **"Radical Agility" ended** nowhere in the public record. No post announces it, and no source describes a 2019 reorganization under that name; the return to discipline is this chapter's reading of a sequence of posts and one leadership change (Bowman left in 2019, by professional-profile sources). The widely reported "expanded too much" wording from the February 2023 announcement was not in the page fetched. The 2016 trade accounts of team size (three to seven) are secondary; Zalando's own posts give "85+" teams.
- **Open-source status** is as of 7 November 2026 and will change; the Tech Radar page shows no last-updated date.
- **Business figures** for 2025 include ABOUT YOU for part of the year; the 2026 guidance of 5–10% pro-forma growth is the comparable number. The "over 60" fulfillment merchants and the "over 600" B2B partners are read here as different scopes; Zalando has not reconciled them in public.
- **The Connected Retail wind-down** and the September 2026 fee change are reported by trade press from Zalando's partner communication; the primary page was not fetched.

{id: case-zalando--what-to-take-away}
## What to Take Away

**Established.**

- Zalando rebuilt its shop as microservices owned by autonomous teams from 2015 because a shared codebase and slow deployments blocked its 85-plus teams, and it built an audited platform (STUPS) so each team could have its own cloud account (Zalando posts, 2015–2016; InfoQ, 2016).
- Its API guidelines, open since 2016 and maintained in 2026, require API-first design in OpenAPI, forbid breaking consumers, prefer compatible extension to versioning, and require client consent, a sunset date, headers and usage monitoring before shutdown.
- Zalando narrowed its choices over the following decade, each in its own posts: alignment over raw autonomy (2018), a bounded language set (2020), one developer portal (2023) and a read API replacing a price-and-stock event stream that lagged up to 30 minutes at Cyber Week (2025).
- Zalando became a platform through logistics: partner program (2011), ship-from-store (2018), fulfillment for partners and then for any channel (ZEOS, 2023), commerce software (SCAYLE, 2025); 32.1% of its 2025 GMV came from partners (annual report, 2026).

**Depends on context.**

- Team-sized modularity is right when there are enough teams to need it, roughly the Group stage; below that, one platform with named owners for each capability gives the ownership without the operating cost.
- An event bus is necessary once data is spread across systems that must be analyzed and reconciled, which for a merchant is the Omnichannel stage; it is sufficient as a source of current state only while consumers can keep up, which the 2025 post shows they cannot on the busiest week.
- The compatibility and deprecation rules apply at every stage, but in different directions: a Starting or Growing merchant demands them of vendors; an Omnichannel merchant writes them into its own integration contracts; a Group-stage platform owes them to external partners.
- Building a separate technology for one channel (as Connected Retail was) is right while the general program cannot serve it, and becomes a consolidation project once it can; plan the exit when you build it.

**The author's synthesis.**

- Zalando's most valuable export is not an architecture but a habit: writing down the rules for change, and publishing the corrections. I would adopt the compatibility and deprecation chapters of its guidelines as the baseline for every vendor contract a merchant signs.
- The 2025 post is the book's thesis in a platform's own words: a copy is not a system of record, and the busiest day is when the copies drift furthest. Give every fact an owner with a read API, and let events carry the news.

{id: case-zalando--questions-to-ask}
## Questions to Ask

1. Which of our vendors publish a deprecation policy with a sunset date, consent and headers, and which retire versions on a date they choose alone?
2. Do our own scripts and connectors log Deprecation and Sunset headers, and would anyone see the warning?
3. For price and stock, which system can be asked "what is it now", and which systems only hold a copy rebuilt from events?
4. How far behind are our copies on an ordinary day, and how far on the peak hour? Has anyone measured it?
5. If we tolerate unknown fields in every payload we receive, would a vendor adding a field break anything of ours?
6. Do we have an API standard our own team and our agency follow, even a short one, and who reviews against it?
7. Which channel runs on technology built only for that channel, and what is the exit if the general program can serve it later?
8. Before an agent may act on an order, can we name the agent, the person it acts for and the capability it was granted, in words a human can read?

The two cases so far are large companies that wrote their own commerce software. The next asks what happened when vendors tried to sell that shape to everyone else: the composable movement, its promise, its costs and its 2025–2026 turn toward working beside the systems merchants already have. Continue with [Case: commercetools, Shopware and the Composable Movement](#case-composable-movement).

{id: case-zalando--sources-and-evidence}
## Sources and Evidence

*Company, product and investor sources*

- [Radical Agility on AWS (video post)](https://engineering.zalando.com/posts/2015/07/radical-agility-on-aws-video.html) — Zalando Engineering / Lauri Apple, 2015 (7 July); Bowman's "unit of trust" and STUPS as the platform for autonomous teams.
- [On APIs and the Zalando API Guild](https://engineering.zalando.com/posts/2015/09/on-apis-and-the-zalando-api-guild.html) — Zalando Engineering / Frauenstein and Schmeisky, 2015 (3 September); the guild's role, API First, "We cannot afford to break our APIs".
- [Data Integration in a World of Microservices](https://engineering.zalando.com/posts/2015/09/data-integration-in-a-world-of-microservices.html) — Zalando Engineering / Olaf Melchior, 2015 (21 September); the cost of distributed data and the Kafka deployment.
- [From Jimmy to Microservices: Rebuilding Zalando's Fashion Store](https://engineering.zalando.com/posts/2015/10/from-jimmy-to-microservices-rebuilding-zalandos-fashion-store.html) — Zalando Engineering / Dan Persa, 2015 (16 October); the monolith's name, the stated reasons, Spearheads, Skipper.
- [From Monolith to Microservices (video)](https://engineering.zalando.com/posts/2016/02/from-monolith-to-microservices-video.html) — Zalando Engineering, 2016 (10 February); "85+ engineering teams".
- [Four Lessons with Microservices](https://engineering.zalando.com/posts/2016/04/four-lessons-with-microservices.html) — Zalando Engineering / Malte Pickhan, 2016 (27 April); two services became eight; weekly goals.
- [Zalando Tech Radar](https://engineering.zalando.com/posts/2016/05/zalando-tech-radar.html) — Zalando Engineering / Thomas Frauenstein, 2016 (17 May); the radar's purpose and "one input source".
- [Jimmy to Microservices: The Journey One Year Later](https://engineering.zalando.com/posts/2016/10/jimmy-to-microservices-the-journey-one-year-later.html) — Zalando Engineering / Dan Persa, 2016 (5 October); Project Mosaic, fragments live, the shift to stable components.
- [Platform Engineering and Third Generation Microservices in Dublin](https://engineering.zalando.com/posts/2017/05/platform-engineering-and-third-generation-microservices-in-dublin.html) — Zalando Engineering / Bill de hÓra, 2017 (26 May); the event-driven intent.
- [Agile: Principles over Frameworks](https://engineering.zalando.com/posts/2018/08/agile-principles-over-frameworks.html) — Zalando Engineering / Samir Keck, 2018 (2 August); principles replacing a prescribed method.
- [Technology Choices at Zalando: Tech Radar Update](https://engineering.zalando.com/posts/2020/07/technology-choices-at-zalando-tech-radar-update.html) — Zalando Engineering / Bartosz Ocytko, 2020 (15 July); 1,200+ developers, 4,000+ applications, the narrowed language set.
- [Sunrise: Zalando's developer platform based on Backstage](https://engineering.zalando.com/posts/2023/08/sunrise-zalandos-developer-platform-based-on-backstage.html) — Zalando Engineering / Nagel, Reis Puthin, Ocytko, 2023 (3 August); 100+ interfaces replaced, 40k entities.
- [From Event-Driven to API](https://engineering.zalando.com/posts/2025/03/event-driven-to-api.html) — Zalando Engineering / Gallagher and Carta, 2025 (7 March); the 30-minute delays, 90% unchanged payloads, divergent copies, the Product Read API.
- [Agentic Platform: Open-Sourcing the Agentic Identity Broker](https://engineering.zalando.com/posts/2026/09/agentic-platform-open-sourcing-agentic-identity-broker.html) — Zalando Engineering / Brennenstuhl and Jungsbluth, 2026 (25 September); delegated access and token exchange.
- [Zalando RESTful API and Event Guidelines](https://opensource.zalando.com/restful-api-guidelines/) and the [compatibility](https://github.com/zalando/restful-api-guidelines) and deprecation chapters — Zalando, n.d., accessed 2026-11; rules #106–#115 and #185–#191.
- [Zalando Tech Radar](https://opensource.zalando.com/tech-radar/) — Zalando, n.d., accessed 2026-11; ring definitions.
- [STUPS](https://stups.io/), [Skipper](https://github.com/zalando/skipper), [Patroni](https://github.com/patroni/patroni), [Nakadi](https://github.com/zalando/nakadi), [Zalenium](https://github.com/zalando/zalenium) — Zalando and the Patroni project, GitHub, n.d., accessed 2026-11 (status from the GitHub API on 7 November 2026); project descriptions and archive notices.
- [A Decade of Changing the Game for Partners](https://corporate.zalando.com/en/node/9401) — Zalando, 2021 (24 June); Partner Program figures and targets, ZFS reach.
- [Zalando's Connected Retail Program Offers Support to Physical Stores](https://corporate.zalando.com/en/company/zalandos-connected-retail-program-offers-support-physical-stores) — Zalando, 2020 (31 March); 1,500 stores, carriers, commission waiver.
- [Stronger Together: Connecting Online and Offline Retail](https://corporate.zalando.com/en/convenience/stronger-together-connecting-online-and-offline-retail) — Zalando, 2021 (25 January); 2,600 stores, 2018 launch year.
- [Zalando Onboards C&A to Connected Retail and Expands Program to Austria](https://corporate.zalando.com/en/newsroom/news-stories/zalando-onboards-ca-connected-retail-and-expands-program-austria) — Zalando, 2021 (15 February); 3,000 stores in nine markets.
- [Zalando to launch a fashion assistant powered by ChatGPT](https://corporate.zalando.com/en/node/10422) — Zalando, 2023 (19 April); the assistant beta.
- [Zalando and ABOUT YOU successfully complete transaction](https://corporate.zalando.com/en/investor-relations/zalando-and-about-you-successfully-complete-transaction) — Zalando, 2025 (11 July); completion, 91.45%, shared infrastructure, synergies.
- [ABOUT YOU and Zalando complete final step of their strategic combination](https://corporate.aboutyou.de/en/newsroom/press-releases/about-you-and-zalando-complete-final-step-of-their-strategic-combination) — ABOUT YOU, 2025 (6 November); the squeeze-out and delisting.
- [Zalando's strategy in action: the evolution of our B2B growth engine](https://corporate.zalando.com/en/node/10922) — Zalando, 2025 (10 December); ZEOS components and "over 60" live merchants.
- [Zalando SE FY/25 Fact Sheet](https://corporate.zalando.com/sites/default/files/media-download/zalando-se_fy-2025_fact-sheet.pdf) — Zalando, 2026 (12 March); GMV, revenue, customers, orders, B2B revenue, 2026 guidance.
- [Zalando SE Annual Report 2025](https://corporate.zalando.com/sites/default/files/media-download/zalando-se_annual-report-2025_eng_261003_s.pdf) — Zalando, 2026 (March); ZEOS reach, SCAYLE shops, partner share, headcount, the assistant's users, agentic outlook.
- [ZEOS](https://www.zeos.eu/) — Zalando, n.d., accessed 2026-11; the modular service positioning.

*Standards, regulation and official documentation*

- The guidelines' MUST/SHOULD/MAY follow [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) — IETF, 1997; the deprecation headers follow the Sunset header convention the guidelines cite. Contract rules as the book uses them are in [Promises Between Systems: API Contracts, Webhooks and Versioning](#api-contracts-and-versioning).

*Research and practitioner sources*

- [Zalando's STUPS: an open-source PaaS on AWS](https://www.infoq.com/news/2016/04/zalando-stups-aws) — InfoQ / Daniel Bryant, 2016 (4 April); STUPS scope and audit model.
- [Zalando: APIs, delivery and Radical Agility](https://www.infoq.com/articles/zalando-apis-delivery-radical-agility) — InfoQ / Jerome Louvel, 2016 (24 December); 110 teams, 1,400 people, an AWS account per team, API definitions as source of truth.
- [Scaling Autonomy at Zalando](https://www.infoq.com/articles/scaled-autonomy-zalando/) — InfoQ / Ben Linders, 2018 (30 September); Bowman on autonomy and alignment.
- [Zalando embraces radical agility in its bold platform play](https://diginomica.com/zalando-embraces-radical-agility-in-its-bold-platform-play) — Diginomica, 2016; team sizes of three to seven (secondary).
- [ZEOS: Zalando Ecommerce Operating System](https://channelx.world/2023/10/zeos-zalando-ecommerce-operating-system/) — ChannelX, 2023 (26 October); the 2022 pilot and the October 2023 rebrand.
- [Zalando to axe 'hundreds of jobs' amid economic slowdown](https://www.retailgazette.co.uk/blog/2023/02/zalando-to-axe-hundreds-of-jobs-amid-economic-slowdown/) — Retail Gazette, 2023 (21 February); the overhead reduction.
- [Zalando consolidates partnership models: Connected Retail to be discontinued](https://fashionunited.com/news/business/zalando-consolidates-partnership-models-connected-retail-to-be-discontinued/2026042371971) — FashionUnited, 2026 (23 April); the wind-down date and fee change.

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
