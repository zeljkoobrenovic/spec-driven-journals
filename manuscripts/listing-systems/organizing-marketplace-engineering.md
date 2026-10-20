{id: organizing-marketplace-engineering}
# 42. Who Owns What: Organizing Marketplace Engineering

![Who Owns What: Organizing Marketplace Engineering — logo](listing-systems-architecture/posts/42-organizing-marketplace-engineering/assets/images/42-organizing-marketplace-engineering/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Design the team topology and the architecture governance for a group of marketplaces: which teams are aligned to which journeys, which shared capabilities get platform teams, where specialist search, ranking and valuation teams sit, how platform work is funded, and how cross-brand decisions are made, recorded and revisited. You will follow Veldmark's Common Ground organization design and its architecture advice forum through their first year.

> **WHY THE BUSINESS CARES:** A marketplace group pays for its organization twice: once in salaries, and again in the time it takes for one improvement to reach every brand and country. A fraud rule that takes three days to reach Belgium and never reaches Poland is an organizational defect, not a technical one.

> **WHY ARCHITECTS SHOULD CARE:** Systems follow the communication structure of the teams that build them. A shared platform without an owning team decays, a bounded context split between two teams becomes a permanent negotiation, and an architecture function that reviews without owning anything is routed around. The org chart is part of the architecture.

> **KEY POINTS:**
>
> * **Assign owners before you assign services.** Every buyer and seller journey, every bounded context and every shared capability needs exactly one owning team, and the team's cognitive load must fit. Stream-aligned teams own marketplace journeys; platform teams own shared capabilities as internal products; specialist teams own the few subsystems, such as ranking models and valuation, that need rare expertise.
> * **A platform team earns its tenants.** Shared capabilities become platforms when an accountable team offers them with a contract, a roadmap and migration help, funded so that the cheapest choice for a marketplace is to use them. Mandates without those things produce shadow copies; voluntary adoption with them is the best-documented success in the public record.
> * **Govern with decisions, not with gates.** An advice process — anyone affected may decide, after seeking advice from those affected and from experts, and must record the decision — plus a small set of principles and an open weekly forum scales better across brands than an architecture review board. Decision rights still need to be explicit: what the group decides, what platforms decide and what each marketplace decides.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Platform Mandate** — a central platform imposed by deadline, without a team that treats marketplaces as customers, is the failure that organization design is most often asked to prevent and most often causes.
> * **The Country Fork** — when each country or brand has its own full-stack teams for the same journey, every improvement is built, staffed and maintained once per team, and the code forks to follow the org chart.
> * **The Acquisition Archipelago** — acquired marketplaces arrive with their own engineering organizations, and unless ownership of shared capabilities is assigned deliberately, the group keeps four of everything because four teams each own one.

Marketplace groups are usually assembled, not designed. A founding marketplace grows its own engineering organization; acquisitions bring theirs; a group function appears to run finance, security and perhaps an advertising stack. Each organization works. Together they produce the familiar picture of four identity systems and four trust-and-safety stacks, because **each capability exists as many times as there are teams that believe they own it.**

The technical chapters of this book argue for shared platforms beneath local products: one event backbone, one search platform, one trust-and-safety pipeline, one entitlement ledger, configured per brand and country. None of that survives contact with an organization that has no team to own it. [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) set the order in which the shared capabilities move after acquisitions; this chapter covers the other half of the architecture: **who owns which journey, which capability and which decision**, how those teams interact, how they are paid for, and how a group makes architectural decisions that bind several brands without a central committee that slows all of them. [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) then moves the code to the owners named here.

This chapter owns two terms. A **marketplace team topology** is the assignment of team types to a marketplace group's journeys, bounded contexts and shared capabilities, together with the interaction mode between each pair of teams. **Architecture governance** is the set of decision rights, forums, records, principles and standards through which architectural decisions are made, communicated and revisited. Where boundaries come from is the subject of [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts); what to share across countries and brands is [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms).

{id: organizing-marketplace-engineering--setting-the-scene-at-veldmark-the-rule-that-reached-belgium-three-days-late}
## Setting the Scene at Veldmark: The Rule That Reached Belgium Three Days Late

On Sunday 7 March 2027, Femke, a private seller in Rotterdam, listed a city bike on Tradeyard Netherlands. At 20:11 a "buyer" sent her a fake Safe Deal payment link. She reported it at 20:19, the account was suspended at 20:26, and Tradeyard NL's trust-and-safety team wrote a new rule that withheld 37 similar messages to other sellers that evening. Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), handled the incident well in the Netherlands.

The rule reached Tradeyard Belgium on **Wednesday 10 March**, because Belgian rules shipped with Yardstick, Tradeyard's PHP monolith, which deploys twice a week. It never reached Tradeyard Poland or Portugal, where moderation was run by two outsourced vendors with their own rule sets. And the phone number behind the suspended account had also registered a private-seller account on Motorvane, Veldmark's automotive marketplace, which nobody at Motorvane learned about.

Ingrid Halvorsen, Veldmark's Group Chief Architect since February, does not read this as a trust-and-safety failure. She reads it as an organization chart. She asks each brand for its team list and gets four documents in four formats:

| Brand | Engineers (2027) | Teams | How teams are cut | Architecture function |
| --- | --- | --- | --- | --- |
| Tradeyard | about 430, of whom about 140 work in teams whose changes ship only with a Yardstick deploy | 61 | Mixed: Yardstick component teams, country teams in Poland and Portugal, a few journey teams on the AWS services | Two architects in Daan Visser's office |
| Motorvane | about 290 | 38 | Journeys (dealer supply, discovery, leads, financing) | Principal engineers' guild |
| Hearthly | about 250 | 33 | France and Spain as separate organizations since the 2025 acquisition | One architect, in France |
| Keybridge | about 70 | 10 | Product modules of the CRM | The founder's CTO |
| Group functions (Veldmark Ads, group IT) | about 110 | 16 | Functions | None |
| **Total** | **about 1,150** | **158** | | |

The team list explains the incident better than the rule engine does. Trust and safety for Tradeyard was owned by an in-house team for the Netherlands and Belgium and by vendors for Poland and Portugal; nobody owned *trust and safety for Tradeyard*, let alone for the group. The capability map that Ingrid presented on 31 March 2027 (see [Map What the Marketplace Does Before What Runs It](#business-capabilities)) found the same shape in identity, search, catalog and analytics: **each overlap existed because several teams each owned a piece of it, and no team owned the whole.**

![A courier with one fraud rule reaches the Netherlands at once, waits days behind a slow machine for Belgium, and is turned away by contractor desks at Poland and Portugal.](listing-systems-architecture/posts/42-organizing-marketplace-engineering/assets/images/42-organizing-marketplace-engineering/one-rule-four-countries.jpeg)

**Figure 1:** *The March 2027 phishing rule reached Belgium three days late and Poland and Portugal never, because each country's trust and safety had a different owner and nobody owned trust and safety for Tradeyard.*

Mateus Carvalho, the Group CTO, asks Ingrid the question this chapter answers: *Common Ground has €140 million and four years to build shared platforms. Who will own them, who will use them, and who decides when the two disagree?*

{id: organizing-marketplace-engineering--concepts-teams-as-part-of-the-architecture}
## Concepts: Teams as Part of the Architecture

{id: organizing-marketplace-engineering--conway-s-law-read-as-a-design-tool}
### Conway's law, read as a design tool

Melvin Conway observed in 1968 that organizations which design systems produce designs that copy their own communication structures ([Conway, 1968](https://www.melconway.com/Home/Committees_Paper.html)). In a marketplace group the observation is easy to verify: four brands with four engineering organizations have four identity systems. The useful reading is the reverse one, sometimes called the *inverse Conway maneuver*: **if you want a shared search platform, create a team whose job is the search platform**, and give the brands' discovery teams a reason to depend on it.

The maneuver has two limits. First, changing teams does not change code; the old structure persists in the systems until someone migrates them, which is why [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) follows this chapter. Second, teams have a limited capacity for complexity. The Team Topologies authors, Matthew Skelton and Manuel Pais, put it as a principle: "Teams can only handle so much complexity before breaking down" ([Team Topologies, key concepts](https://teamtopologies.com/key-concepts), n.d.). A team asked to own Tradeyard's insertion flow in four countries, the pro-seller API and the image pipeline will own all three badly.

{id: organizing-marketplace-engineering--four-team-types-and-three-interaction-modes}
### Four team types and three interaction modes

Team Topologies names four fundamental team types and three ways teams interact ([Team Topologies, key concepts](https://teamtopologies.com/key-concepts), n.d.). The tables below map each onto a listing marketplace.

| Team type | Definition (Team Topologies) | In a marketplace group | Example at Veldmark (2027 design) |
| --- | --- | --- | --- |
| **Stream-aligned** | Organized around a flow of work, usually a slice of the business domain | A buyer or seller journey of one marketplace: supply and insertion, discovery, conversation and transaction, pro-seller tooling, monetization | Tradeyard Discovery; Motorvane Dealer Supply; Hearthly Agency Experience |
| **Platform** | Provides an internal product that speeds up stream-aligned delivery | A shared capability with a contract: event backbone, search platform, identity, trust-and-safety pipeline, media, entitlement ledger, taxonomy service, developer platform | Event Platform (Sven Lindqvist); Search Platform (Tomasz Wiśniewski) |
| **Complicated subsystem** | Owns work that needs deep specialist expertise | Ranking models, automated valuation models (AVMs), fraud models, query understanding for one language family | Valuo AVM team; group fraud-modeling team |
| **Enabling** | Helps stream-aligned teams overcome obstacles and adopt new capabilities | Migration help, reliability engineering, experimentation practice, accessibility | Yardstick Exit team; Search Migration enablement |

| Interaction mode | Meaning | When it fits in a marketplace |
| --- | --- | --- |
| **Collaboration** | Two teams work together for a set period to discover an API, practice or technology | A platform team and its first tenant designing a contract (the event platform and Tradeyard in 2027) |
| **X-as-a-Service** | One team provides, another consumes | The steady state for every mature platform |
| **Facilitation** | One team helps and mentors another | An enabling team moving a brand's alerts onto the new matcher |

The mode is a property of a pair of teams at a point in time. **Collaboration that never ends is a sign that the platform has no contract**; X-as-a-Service from the first day is a sign that the platform was designed without its tenants.

{id: organizing-marketplace-engineering--the-marketplace-team-topology}
### The marketplace team topology

Every marketplace organization design must choose the axis that cuts its stream-aligned teams: country, journey or capability layer.

| Axis | Teams look like | Strength | Weakness |
| --- | --- | --- | --- |
| **Country** | "Tradeyard Poland" with full-stack teams | Close to the local market, language and law | Every journey is built once per country; the Country Fork in organizational form |
| **Journey** | "Tradeyard Discovery" serving all four countries | One implementation per journey; local needs carried by market product leads and configuration | Needs strong configuration and localization; local managers feel distant |
| **Capability layer** | "Tradeyard Search Backend", "Tradeyard Android" | Deep technical skill | Every product change needs several teams; nobody owns an outcome |

For marketplaces with one product in several countries, I would cut stream-aligned teams **by journey within a brand**, and carry the country through product roles and configuration rather than through separate teams. The exception is a country whose product differs, such as Tradeyard Poland's vehicles and property sections with insertion fees, which may justify a market team for those sections. The rule I use: **a country team is justified by a different product, not by a different language.**

Across brands, the same journey stays separate. Motorvane's dealer supply and Hearthly's agency supply are different products with different customers, feeds and contracts, and the shared part — the supply contract, the validator library, the taxonomy — is a platform, not a shared team (see [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)).

{id: organizing-marketplace-engineering--ownership-is-the-unit-of-design}
### Ownership is the unit of design

[Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) establishes the rule that each bounded context has exactly one owning team. This chapter extends it to three kinds of things a marketplace must own:

1. **Journeys** — the flow a buyer or seller experiences, with an outcome metric: time to first contact, listings published within the publication SLA, contacts per search session.
2. **Contexts** — the models and their truth: the listing catalog, entitlements, trust decisions, the search read model.
3. **Shared capabilities** — the platforms that several journeys use.

An owner is the team that is woken up when it breaks, decides its roadmap, and answers for its cost. A team that is consulted is not an owner. A committee is never an owner.

{id: organizing-marketplace-engineering--architecture-governance}
### Architecture governance

Governance is often treated as a synonym for review. In a marketplace group it has five parts, and review is the least important:

| Part | What it is | Failure when it is missing |
| --- | --- | --- |
| **Decision rights** | Who may decide what: group, platform, brand, team | Every decision escalates, or none does |
| **Decision records** | Short documents that capture context, decision, status and consequences, kept with the code | The same argument is held every year; nobody knows why the system is shaped the way it is |
| **Principles** | A small set of testable rules against which options are judged | Decisions are argued from taste |
| **Forum** | A regular, open place where proposed decisions get advice in public | Advice is private, inconsistent and slow |
| **Standards and golden paths** | The few things every team must do the same way, ideally made easy by a platform | Either everything is a standard or nothing is |

Michael Nygard's 2011 proposal for architecture decision records (ADRs) is still the common shape: a title, the context ("the forces at play"), the decision in active voice, a status (proposed, accepted, deprecated, superseded) and the consequences, positive and negative ([Nygard, 2011](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)).

Andrew Harmel-Law's **advice process**, described in 2021, replaces approval with one rule: "anyone can make an architectural decision", provided they first seek advice from everyone meaningfully affected and from people with relevant expertise, and record the advice they received; they need not follow it. It is supported by decision records, a weekly open architecture advisory forum, team-sourced principles and a local technology radar ([Harmel-Law, martinfowler.com, 2021](https://martinfowler.com/articles/scaling-architecture-conversationally.html)).

{id: organizing-marketplace-engineering--architecture-a-topology-for-a-group-of-marketplaces}
## Architecture: A Topology for a Group of Marketplaces

{id: organizing-marketplace-engineering--stream-aligned-teams-on-top-of-platform-teams}
### Stream-aligned teams on top of platform teams

A group of marketplaces needs stream-aligned teams per brand and journey on top, platform teams per shared capability underneath, a few complicated-subsystem teams beside them, and enabling teams that move between them. Figure 2 shows the version Veldmark adopted for Common Ground.

![Diagram: Veldmark's Common Ground team topology (target 2028)](listing-systems-architecture/posts/42-organizing-marketplace-engineering/assets/images/42-organizing-marketplace-engineering/fig02-veldmark-s-common-ground-team-topology.jpeg)

**Figure 2:** *Veldmark's Common Ground team topology (target 2028). Brands keep their journeys and their products; the group owns the capabilities beneath them; specialists and enablers sit beside both. Keybridge stays outside the platform organization because its neutrality commitment requires it.*

Three properties of the figure matter more than its boxes:

- **Arrows point down.** Brands depend on platforms; platforms never depend on a brand's internals. When a platform needs something from a brand — Tradeyard's listing events, for example — it gets it through a published contract, not a call into Yardstick.
- **Specialists serve brands through platforms.** A ranking model is trained by a specialist team, served through the search platform's ranking service, and configured by each brand's discovery team. The relevance objective stays with the brand, as [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) argues; the model mechanics stay with the specialists.
- **Enabling teams are temporary by design.** The Yardstick Exit team exists to make itself unnecessary by the end of 2029.

{id: organizing-marketplace-engineering--platform-teams-as-internal-products}
### Platform teams as internal products

A platform team differs from a shared-services department in five things it must have:

| A platform team has | Why it matters in a marketplace group | Evidence it is missing |
| --- | --- | --- |
| A **product owner** with a tenant-facing roadmap | Brands plan around it; the roadmap is where conflicts between brands become visible | Priorities set by whichever brand escalated last |
| A **contract** (API, event schema, service levels) | Brands can depend on it without reading its code | Tenants call internal endpoints; upgrades break them |
| **Self-service onboarding** | A new tenant or country costs days, not a project | Every onboarding is a ticket to the platform team |
| **Migration help** | Moving onto the platform is the tenant's cost; reducing it is how the platform wins | Adoption stalls at the second tenant |
| **Run responsibility and cost transparency** | The team owns incidents and can show cost per tenant | Brands blame the platform; the platform blames brands' usage |

The best-documented example in the classifieds record is Adevinta's internal platform. A 2019 talk, written up in January 2020, described a "Common Platform" for about 1,500 engineers in about 20 marketplace companies, with voluntary adoption, about ten minutes of self-service onboarding, and platform engineers embedded with large tenants during migration; by 2023 the platform, by then called SCHIP, served "more than 4,000 developers" (see [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) for the sources and the later decentralization). **Voluntary adoption with migration help is the pattern; a mandate is what you use only after the platform is clearly cheaper and the last holdouts are cost, not need.**

![Left, brand teams walk up a ramp into an open platform hub with a contract and a helper; right, a fenced hub with a deadline clock while teams build shadow copies outside.](listing-systems-architecture/posts/42-organizing-marketplace-engineering/assets/images/42-organizing-marketplace-engineering/platform-earns-tenants.jpeg)

**Figure 3:** *A platform team earns its tenants with a contract, self-service onboarding and migration help; a mandate without those things produces compliance on paper and shadow copies behind it.*

{id: organizing-marketplace-engineering--decision-rights-across-group-platform-and-brand}
### Decision rights across group, platform and brand

Governance starts with a table, not a forum. The decision-rights matrix below is the one that Veldmark's forum adopted in April 2027 and revised in September. *D* means decides, *A* means must be asked for advice, *I* means informed.

| Decision | Group (CTO, Chief Architect) | Platform team | Brand engineering | Brand product |
| --- | --- | --- | --- | --- |
| Whether a capability is shared (enters Common Ground) | **D** (CTO, after forum advice) | A | A | A |
| Platform contract and roadmap | A | **D** | A | A |
| Engine, store or vendor behind a platform | I | **D** | I | — |
| Brand product features, UX, ranking objective, packages and prices | — | A (feasibility) | A | **D** |
| Brand-internal architecture (services, stores) within principles | I | — | **D** | — |
| Exception to a principle or standard | A | A | **D**, with a decision record | — |
| Personal data crossing brands | Group DPO **D** | A | A | A |
| Funding shifts between platforms and brands | **D** (CTO and CFO) | A | A | A |

The matrix has two deliberate features. Brands decide exceptions themselves, provided they record them; the forum's job is to make the trade-off visible, not to veto it. And the decision whether a capability becomes shared sits with the CTO, because it moves money and people, but only after the forum has heard the brands.

{id: organizing-marketplace-engineering--the-advice-process-in-a-marketplace-group}
### The advice process in a marketplace group

Under the advice process, most cross-brand decisions stay with the team that proposes them. Figure 4 shows the path as Veldmark runs it.

![Diagram: The advice process applied to cross-brand decisions](listing-systems-architecture/posts/42-organizing-marketplace-engineering/assets/images/42-organizing-marketplace-engineering/fig04-advice-process-applied-cross-brand-decisions.jpeg)

**Figure 4:** *The advice process applied to cross-brand decisions. Most decisions stay with the team that proposes them; the forum makes advice public and consistent; only decisions that move funding, people or personal data across brands go to an accountable executive.*

The process gives up approval and keeps three things that matter: **advice is public**, so the Motorvane team hears what the search platform told Hearthly; **decisions are recorded**, so the reasons survive the people; and **every record carries a review date or trigger**, so decisions are revisited when the facts change rather than when someone new arrives.

![Left, teams queue in front of a review board with an approval stamp while some route around it; right, teams present at an open table, receive advice, and file their own decision record.](listing-systems-architecture/posts/42-organizing-marketplace-engineering/assets/images/42-organizing-marketplace-engineering/review-board-vs-advice-forum.jpeg)

**Figure 5:** *An approval board becomes a queue that teams learn to route around; under the advice process the team decides after public advice, records why, and sets a date to revisit.*

{id: organizing-marketplace-engineering--funding-models}
### Funding models

How platform work is paid for shapes behavior more than any principle. Five models are common:

| Model | How it works | Behavior it produces | When it fits |
| --- | --- | --- | --- |
| **Central program budget** | A board-approved program funds platform teams directly | Fast start; platforms can be built before tenants pay | The build phase of a consolidation program |
| **Fixed allocation ("platform tax")** | Platform cost split by a fixed key, such as revenue share | Predictable; no incentive for tenants to use the platform efficiently or for the platform to serve them well | Stable, uncontested infrastructure |
| **Showback** | Usage-based cost reported per tenant, not charged | Visibility without budget fights; a rehearsal for chargeback | The first year after a platform goes live |
| **Chargeback by usage** | Tenants pay per unit (per thousand searches, per million events, per stored image) | Efficient use; risk that tenants avoid a platform to save budget, or build shadow copies | Mature platforms with stable unit costs |
| **Internal market** | Tenants may buy outside if the platform is not competitive | Strong pressure on the platform | Rarely right for capabilities that must be shared for policy reasons, such as trust and safety or identity |

The trap is to pick one model for all platforms. Trust and safety and identity are shared because the group needs one answer for fraud and for login; charging per decision would tempt a brand to skip checks. Search and media are shared for cost; usage pricing makes their cost visible and fair.

**Cost attribution needs an ownership catalog before it needs a pricing model.** Adevinta's cloud governance team stated the principle for accounts and infrastructure in a December 2024 post as "You build it, you run it (and you pay for it)", backed by an ownership catalog mapping more than a thousand cloud accounts and projects to teams and cost centers ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/multi-cloud-governance-at-scale/)).

{id: organizing-marketplace-engineering--the-roles-of-architects}
### The roles of architects

A marketplace group needs fewer architects than it thinks, placed where decisions are made.

| Role | Owns | Does not own |
| --- | --- | --- |
| **Group Chief Architect** | The principles, the decision-rights matrix, the forum, the capability and context maps, the consolidation sequence, and the architectural case for funding shifts | Brand designs; platform internals; any approval gate |
| **Brand lead architect** (one per brand) | The brand's target architecture and migration plan; the brand's voice in group decisions | Group platforms' contracts |
| **Platform architect** (for large platforms) | Contract design, tenancy model, evolution and deprecation of the platform | Brand product decisions |
| **Principal engineers in teams** | Most decision records; the code that proves or disproves them | Group-level trade-offs alone |

A 2018 post on the Berlin Tech Blog, shared by the eBay Kleinanzeigen and mobile.de engineering teams, stated the rule I would put on the wall: "A Software Architect should never make a decision that the team can effectively make on their own", and described the architect's job as replicating success stories across teams and finding the weakest link ([Berlin Tech Blog, 2018](https://medium.com/berlin-tech-blog/software-architects-and-autonomous-teams-328138202df1)). That is old evidence, from a period before the brands' later replatforming, but it describes the role rather than a system, and it has aged well.

{id: organizing-marketplace-engineering--in-practice-what-the-public-record-shows}
## In Practice: What the Public Record Shows

Few marketplace groups publish their organization designs; each dated fragment below is evidence about one organization at one time.

**Marktplaats: from business-unit teams to Journey Teams (2017).** In a November 2017 post, Marktplaats described replacing product teams aligned to business units, each product owner with a "huge backlog", by cross-functional **Journey Teams** organized around the customer journey, which included product, technology, marketing, customer relations, product analytics and data science. The company moved to objectives and key results, with at most three company objectives and four key results each, refreshed quarterly. The head of technology wrote that in this way of working "the platform has been changed from a set of monolithic services to microservices, allowing teams to deliver 10x faster each year" — a self-reported claim ([Marktplaats Technology, 2017](https://medium.com/marktplaats-technology/the-marktplaats-journey-becoming-the-best-version-of-ourselves-5ece9829f13f)). The post is nine years old, and the current organization is not public. It is still the clearest classifieds account of cutting teams by journey rather than by business unit, and of the architecture following the teams.

**Vinted: domains first, then teams.** In January 2026, Vinted described how a few engineers introduced domain-driven design to map responsibilities in its Rails monolith: "It took us at least two years to understand the domains, as we identified almost 300 of them." The domains "gave teams clarity about what they owned" and "eventually, it guided how we restructured teams and how we planned the future of the architecture" ([Vinted Engineering, 2026](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-1/)). The order is the lesson: the domain map came before the team restructure, and both came before the services.

**AutoScout24: growing the new organization one team at a time.** A 2016 conference report described AutoScout24's move from a .NET monolith to microservices on AWS, "Project Tatsu", which began in November 2014 with one team and grew to eight, adding teams every two to three months, with no big upfront plan ([InfoQ, 2016](https://www.infoq.com/news/2016/02/autoscout-microservices/)). The evidence is ten years old; it shows a migration staffed by growing the new organization rather than reassigning the old one in one move.

**OLX: squads and chapters, then a framework for cross-functional work.** A 2021 post from OLX Autos, a business OLX has since closed, described squads owning end-to-end journeys and chapters (Android, backend, quality) led by chapter leads who also line-managed ([OLX Tech, 2021](https://tech.olx.com/scaling-agile-olx-2b2dd7b9def4)). In March 2026, OLX Motors described its "Work Organization Framework", introduced because "by 2024, at OLX Motors, we had a classic case of 'too much of everything, not enough of anything'": a governance model with champions, drivers and outcome tracking that completed 29 initiatives, including standardized user identification across 71 services and one deployment-notification center across more than 60 services ([OLX Tech, 2026](https://tech.olx.com/empowering-innovation-through-structure-93c15614f6d3)). Two lessons: journey squads alone do not deliver cross-cutting hygiene; and a lightweight, outcome-tracked structure for cross-team initiatives is a governance tool in its own right.

A third OLX fragment concerns ownership: a July 2025 post explains that recommendations serving moved out of "a shared backend service" to the data team "to gain greater autonomy and flexibility" ([OLX Tech, 2025](https://tech.olx.com/scaling-recommendations-service-at-olx-db4548813e3a)) — a complicated subsystem taking ownership of its own runtime, with the efficiency trade-offs the post describes.

**Adevinta: voluntary platforms, harvested inventions, and a swing back.** Adevinta's record covers the full pendulum and is told in [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta). For organization design, three fragments matter. The deployment abstraction that ran across its marketplaces, FIAAS, came from FINN.no, and its experimentation analysis package, Fisher, came from Marktplaats; both were local inventions promoted to group level (2017–2023 sources). In 2023 the group "redesigned the operating model and created a robust structure organised by verticals", and in 2025 it "evolved from a centralised structure to a decentralised, standalone operating model", with "the ramp-down of central functions, the transfer of key capabilities, the localisation of intellectual property" (Adevinta Annual Report 2023; Strategic Report 2025). In a September 2026 post about an infrastructure self-service bot, leboncoin's engineering blog described about ten infrastructure engineers supporting about 70 feature teams ([leboncoin tech blog, 2026](https://medium.com/feed/leboncoin-tech-blog); figures from the blog's feed summary, the full post not retrieved).

> **INFERENCE, NOT DOCUMENTED:** Read as Conway's law in reverse, Adevinta's 2023 reorganization by verticals preceded its plan to converge the leboncoin and Kleinanzeigen product platforms, and its 2025 decentralization preceded the localization of intellectual property and the parallel running of central and local services. In both directions the organization moved first and the platforms were expected to follow. The public record does not describe the internal team designs, so this is the author's reading of the sequence, not a description of Adevinta's organization.

**eBay Classifieds Group: a federation with group functions.** The public traces of eCG's organization, mostly job postings from 2009–2011 and a 2018 conference talk, show national businesses with their own platforms, group roles asked to "leverage existing technology components" across the portfolio, and a "Global Motors vertical" with a shared partner API by 2018–2020 (see [eBay Classifieds Group: Shared Platforms, Local Brands and a Sale](#case-ebay-classifieds)). It is a federation that coordinated choices — the eCG companies jointly evaluated replacements for eBay's Voyager search engine in 2015 — while each brand migrated itself.

The common thread is modest: **journey-aligned teams, domain maps before reorganizations, platforms that grew by adoption, and specialists owning their runtime.** No classifieds group has published a complete topology, and anyone who claims to know one should be asked for the source.

{id: organizing-marketplace-engineering--veldmark-worked-example-the-common-ground-organization-design}
## Veldmark Worked Example: The Common Ground Organization Design

{id: organizing-marketplace-engineering--three-options}
### Three options

In May 2027 Ingrid and Yara Mendes, the Head of Platform Engineering, bring three organization options to the advice forum.

| Option | Description | For | Against |
| --- | --- | --- | --- |
| **A. Federated guilds** | Platforms built by brand teams "on behalf of the group", coordinated by cross-brand guilds | No reorganization; brand budgets keep control | Nobody owns a platform; the strongest brand's version wins by default; the 2027 overlaps exist because this is the current model |
| **B. Central platform organization, product-run** | Group platform teams under the Head of Platform Engineering, each with a product owner and tenant-facing contract; brands keep journeys | One owner per shared capability; fleet-level economics | Brands lose engineers and some control; risk of the Platform Mandate if platforms are slow |
| **C. Central product and technology** | One group organization owning all products and platforms, with brand "market teams" for local needs | Maximum reuse | Breaks "share platforms, not products"; the 2023-style convergence bet; expensive to reverse if a brand is sold |

The forum's advice is option B, with conditions. Mateus Carvalho decides it on **Tuesday 22 June 2027**, effective **1 September 2027**, in the decision record "Common Ground organization v1". It has five parts:

1. **One owning team per shared capability.** The group platform organization, under Yara Mendes, owns the Common Ground platforms: event backbone, search platform, identity (Veldmark ID), trust-and-safety pipeline engineering, media, messaging, catalog and entitlements, taxonomy and attributes, the listing platform (publication pipeline and consumer registry) and the developer platform. Data and ML platforms stay in Priya Raman's Data & ML organization, which follows the same platform rules.
2. **Brands keep their journeys, products and teams.** Stream-aligned teams stay in Tradeyard, Motorvane and Hearthly, cut by journey. Tradeyard's Polish and Portuguese country teams become journey teams serving all four Tradeyard countries, with market product leads per country; Tradeyard Poland keeps one market team for its vehicles and property sections.
3. **Policy stays local, mechanism goes central.** Aisha Rahman, Group Head of Trust & Safety, owns group policy standards; each brand's trust operations own local policy and moderation; the platform team owns the pipeline, rule engine and case tooling. This is the split the capability map recommended.
4. **People move with work, not with a date.** Engineers move to a platform team when their capability moves, not on 1 September. About **150** engineers transfer from brands in 2027 and about **80** are hired, giving the platform organization about **230** engineers in **24** teams by the end of 2027.
5. **Keybridge stays outside.** Keybridge's engineering organization is not merged into the platform organization and is not a tenant of the shared trust-and-safety platform or the listing event stream; group security standards apply. The March 2027 neutrality decision makes this a structural choice, not a postponement.

| Measure | March 2027 | December 2027 |
| --- | --- | --- |
| Engineers | about 1,150 | about 1,200 |
| Teams | 158 | 152 |
| Common Ground capabilities with exactly one owning team | 0 of 9 | 8 of 9 (the data platform migration is still split with the brands) |
| Teams whose changes ship only with a Yardstick deploy | 19 | 14 |
| Stream-aligned teams cut by country | 17 | 4 |
| Teams with more than three owned contexts or capabilities (cognitive-load flag) | 23 | 9 |

{id: organizing-marketplace-engineering--the-platform-contract-per-team}
### The platform contract per team

Each platform team publishes a one-page **team API**: what it offers (contracts, service levels), how to get help, its roadmap for the next two quarters, and its current interaction mode with each tenant. For the second half of 2027 the search platform's page reads, in part: *collaboration* with Tradeyard Portugal (index design, until the Q2 2028 migration), *facilitation* with Motorvane (moving to Listing Search API v1 on Elasticsearch), *X-as-a-Service* with nobody yet. **The page makes visible that the platform has no steady-state tenant yet**, which is the honest state of a platform in its first year.

Collaboration is time-boxed to two quarters per tenant. When the box runs out, the forum asks one question: what is missing from the contract that still requires the two teams to work together?

{id: organizing-marketplace-engineering--funding}
### Funding

The decision record sets funding per phase:

- **2027–2028: Common Ground funds platform build.** The €140 million program pays for platform teams' build work and for the enabling teams.
- **From Q1 2028: showback.** Each platform publishes monthly cost per tenant with a unit: per thousand searches, per million events, per thousand stored images, per moderation decision.
- **From 2029: usage allocation for cost-driven platforms** (search, media, event backbone, developer platform), and **fixed allocation for policy-driven platforms** (identity, trust and safety), so that no brand saves money by skipping a fraud check.

Olivier Petit, VP Monetization, adds one condition that turns out to matter: the catalog and entitlement service, Tally, is funded centrally through 2029, because its first tenants (Motorvane in Q1 2028, Tradeyard in Q2 2028) are migrating revenue-critical billing and should not also be negotiating its price.

{id: organizing-marketplace-engineering--the-architecture-advice-forum-one-year-in}
### The architecture advice forum, one year in

Veldmark set up the forum in April 2027, together with its architecture principles, and made decision records mandatory for cross-brand decisions. It meets weekly, for an hour, and anyone may attend; about 60 people do on a typical week. Its first year can be read from its decision log.

| Month (2027) | Decision records the forum advised on, as told in other chapters |
| --- | --- |
| April | Architecture principles; decision-rights matrix |
| May | Common Ground context map ([Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts)); data platform design ([Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform)); Tradeyard web layer ([Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture)) |
| June | Ranking policy v1 ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking)); Veldmark ID ([Who Is on the Other Side? Identity and Verification](#identity-and-verification)); Common Ground organization v1 (this chapter) |
| July | Listing event contract v1 live ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)) |
| September | Supply Contract v1 ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)); search platform decision ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)) |
| October | Group taxonomy release and bikes split ([Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies)); Tally ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)) |
| November | ML platform decision ([Models in Production: ML Platforms and Use Cases](#ml-platform)); shared trust-and-safety platform live for Tradeyard NL and BE |

By 31 December 2027 the log holds **74 cross-brand decision records**. The median time from first draft to decision is **nine working days**; **six** went to the CTO because they moved funding or people, and **two** to the data protection officer because they moved personal data across brands. Three were superseded within the year, which Ingrid counts as a sign of health: the forum changes its mind when facts change, and the records say why.

Veldmark's principles fit on one page. Four of the twelve do most of the work in the log:

| Principle | Test it implies | A 2027 decision it shaped |
| --- | --- | --- |
| Share platforms, not products | Is the proposal a capability beneath several products, or a product feature? | Ranking policy: shared ranking service, brand-owned objective |
| One owner per context and capability | Can the proposer name the single owning team? | Removal propagation to alerts given to the Alerts team |
| Contracts before migrations | Does a published contract exist before any tenant moves? | Every application on Listing Search API v1 before its engine changes |
| Separable by tenant | Can a brand leave this capability within 18 months with its data? | Per-brand topics and schemas on the event backbone |

The fourth principle comes from Veldmark's ownership: a private-equity owner might one day sell a brand, and [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) shows what unwinding a shared platform costs when separability was not designed in.

{id: organizing-marketplace-engineering--the-phishing-rule-replayed}
### The phishing rule, replayed

In November 2027 the shared trust-and-safety platform goes live for Tradeyard Netherlands and Belgium. The forum's acceptance test is the March incident. A rule written by Tradeyard's trust operations team in Lisbon is a configuration change in the platform, reviewed in the platform's rule workflow, and effective for every tenant that subscribes to the rule family within an hour, without any Yardstick deploy. The phone number of a terminated fraud account enters the shared hashed block list, which the data protection officer approved with a two-year retention, so Motorvane sees the match at its next account check. Poland and Portugal are not tenants yet; their move is on the platform's roadmap, and the gap is listed on the team API page rather than hidden.

The rule engine did not change. **The ownership did**: there is now one team that owns "a rule reaches every tenant", and its service level is written down.

{id: organizing-marketplace-engineering--trade-offs}
## Trade-offs

| Decision | Option | When it is right | When it is wrong |
| --- | --- | --- | --- |
| Stream-aligned axis | By journey within a brand | One product in several countries; strong configuration | Countries with genuinely different products, or a brand with one country |
| Stream-aligned axis | By country | Distinct local products, regulation or ownership; a brand that may be sold separately per country | One product in several countries: it rebuilds the Country Fork |
| Shared capability ownership | Central platform team | Uniform technology, pooled volume, group-wide policy need | Capability is really a product feature; only one brand uses it |
| Shared capability ownership | "Lead brand" builds for the group | Early discovery, one dominant tenant | Long term: the lead brand's roadmap always wins |
| Specialists | Central complicated-subsystem team | Rare skills (ranking ML, AVMs, fraud models), shared tooling | The model is inseparable from one brand's product decisions; embed instead |
| Governance | Advice process and open forum | Many autonomous teams; decisions must be fast and visible | Regulated decisions that require formal sign-off (handled by named executives, not the forum) |
| Governance | Architecture review board with approval | Small organizations with few architects; safety-critical systems | Multi-brand groups: it becomes a queue and teams route around it |
| Funding | Central program budget | Build phase | Run phase: hides cost, removes pressure to be efficient |
| Funding | Usage chargeback | Mature, cost-driven platforms | Policy-driven platforms (trust, identity) where skipping use is the risk |

{id: organizing-marketplace-engineering--vertical-differences}
## Vertical Differences

| Topic | General classifieds | Real estate | Automotive | Professional SaaS (agent or dealer tools) |
| --- | --- | --- | --- | --- |
| Dominant stream-aligned teams | Private-seller supply, discovery, conversation and transaction | Agency supply and feeds, discovery, new-build campaigns, valuation products | Dealer supply and feeds, discovery, leads, financing | Product modules of the customer's workflow |
| Specialist teams | Fraud and scam models, category prediction, image models | AVM and price estimates; entity resolution for multi-agency listings | Market-value models, VIN decoding, lead scoring | Integrations with portals and back-office systems |
| Sales and account management | Small; pro sellers mostly self-serve | Large; agency relationships drive revenue | Large; dealer contracts and packages | Customer success is the product |
| Local-team pressure | Low to medium: one product, many countries | High: national legal regimes, mandates, energy labels, fee rules | Medium: national registries and dealer markets | High: per-country agency practices |
| Fit with group platforms | Strong for most capabilities | Strong for infrastructure, media and events; weaker for supply, which is vendor-driven | Strong; may stay on its own search engine for a while | Often separate, as Keybridge is, for neutrality or because it is not a marketplace |

Two consequences for organization design. In real estate and automotive, the **supply journey has a commercial side** — agency and dealer contracts, feeds, packages — so the supply team needs close links to sales and account management, which a central platform cannot provide. And a SaaS business that serves the marketplaces' competitors, like Keybridge, needs an organization boundary that customers can see, not only an access control list.

{id: organizing-marketplace-engineering--failure-modes}
## Failure Modes

- **The platform without a product owner.** A team builds what the loudest brand asks for, has no roadmap that tenants can read, and measures itself by tickets closed. Tenants start building around it within a year. The fix is a product owner, a team API page and a tenant review each quarter.
- **The mandate before the platform.** A deadline for all brands to move onto a platform that is not yet cheaper, faster or safer than what they have. The brands comply on paper and keep their copies running. This is the Platform Mandate; it often follows a board-level synergy target.
- **Reorganizing on a date.** Hundreds of engineers move to new teams on the first of the month, before contexts are mapped and before the systems they will own are separable. For months the new teams own code they cannot deploy independently. Move people when their work moves.
- **Country teams for language.** A brand creates a full-stack team per country because the countries speak different languages. Within two years the four teams have four insertion flows.
- **The review board.** A central board approves designs. Its queue becomes the critical path for every cross-brand change, and teams learn to describe changes as local. Decisions get slower and less visible at the same time.
- **Governance without records.** Decisions are made in meetings and remembered by the people who attended. When those people leave, the same questions return, and inherited constraints become folklore.
- **Specialists with no runtime.** A ranking or valuation team that hands models to another team to deploy cannot own model quality in production, and nobody else can either. This is how The Unwatched Model begins (see [Models in Production: ML Platforms and Use Cases](#ml-platform)).
- **Enabling teams that never end.** A migration team becomes a permanent second owner of the systems it migrated. Give each enabling team an end condition at creation.
- **The forgotten acquired organization.** An acquired marketplace keeps its engineering organization intact "until integration", which never comes. Its people are never asked to own a group capability, and its best inventions never become one.

{id: organizing-marketplace-engineering--the-chief-architect-s-view}
## The Chief Architect's View

**Design ownership first, and draw it on the same map as the architecture.** The capability map, the context map and the team topology are three views of one model. If a capability or context has no owning team on the map, it has none in reality. I would review the three together twice a year and treat any orphan or any split ownership as an architectural defect with a named fix and date.

**Measure platforms by adoption and by tenant cost, not by output.** The questions I ask of every platform team each quarter: how many tenants use it in production; what it costs a new tenant to onboard; how many brands still run a shadow copy and why; and what share of its roadmap came from tenants. A platform that cannot answer these is a shared-services department.

**Keep the forum open and the executive decisions few.** The advice forum works because it is open and because most decisions stay with teams. The executive escalation path must exist — money, people and personal data need an accountable decision-maker — but if more than about one decision in ten escalates, the decision rights are wrong, not the teams.

**Expect the pendulum.** Groups centralize for synergy and decentralize for focus, often after a change of owner or strategy. The organization will swing; the architecture should not have to be rebuilt each time. That is why separability by tenant belongs in the principles from the start, and why platform contracts, not team structures, are the durable assets. [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution) returns to this.

**Who decides, and what to watch.** The CTO decides the topology and funding, on the forum's advice; the Group Chief Architect owns the principles, the decision-rights matrix and the maps; platform heads own contracts; brand leaders own journeys. Watch: orphaned or split capabilities; teams over the cognitive-load threshold; teams blocked by another team's deploy (Yardstick's count is the headline number at Veldmark); median time from decision draft to decision; decisions with an expired review date; and shadow copies of platform capabilities in brands.

{id: organizing-marketplace-engineering--questions-to-ask}
## Questions to Ask

1. For each shared capability, which single team is woken up when it breaks, and who decides its roadmap?
2. Which bounded contexts or journeys are owned by more than one team, and which by none?
3. Are stream-aligned teams cut by journey, country or technical layer, and what product difference justifies each country team?
4. What does it cost a brand, in engineering weeks, to adopt each platform, and who pays for that migration?
5. Which platforms are funded by program budget, allocation, showback or chargeback, and does each model fit why the capability is shared?
6. Where do ranking, valuation and fraud specialists sit, and do they own their models in production?
7. Who may decide an exception to a principle, and where is the record?
8. How many cross-brand decisions were made last quarter, how long did they take, and how many escalated?
9. Which decisions are past their review date or trigger?
10. If a brand were sold in 18 months, which teams and platforms would have to split, and is that written down?

{id: organizing-marketplace-engineering--from-organization-to-migration}
## From Organization to Migration

The organization assigns owners; it does not move code. Tradeyard's teams still deploy through Yardstick, and the new platform teams own capabilities that the monolith still implements. [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) takes up the work of moving a live marketplace from the old system to the new one without losing traffic, sellers or revenue.

{id: organizing-marketplace-engineering--sources-and-evidence}
## Sources and Evidence

{id: organizing-marketplace-engineering--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [The Marktplaats Journey: becoming the best version of ourselves](https://medium.com/marktplaats-technology/the-marktplaats-journey-becoming-the-best-version-of-ourselves-5ece9829f13f) — Marktplaats Technology, 2017. Journey Teams replacing business-unit teams; OKRs; self-reported delivery speed (older evidence).
- [Building a Global, Event-Driven Platform, Part 1](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-1/) — Vinted Engineering, 2026. Almost 300 domains identified over at least two years; domains guided team restructuring.
- [AutoScout24's journey to microservices](https://www.infoq.com/news/2016/02/autoscout-microservices/) — InfoQ (Daniel Bryant), 2016. Project Tatsu grew from one team to eight (older evidence).
- [Scaling agile at OLX](https://tech.olx.com/scaling-agile-olx-2b2dd7b9def4) — OLX Tech, 2021. Squads and chapters at OLX Autos (historical; business closed).
- [Empowering innovation through structure](https://tech.olx.com/empowering-innovation-through-structure-93c15614f6d3) — OLX Tech, 2026. Work Organization Framework at OLX Motors; 29 initiatives; identity across 71 services.
- [Scaling recommendations service at OLX](https://tech.olx.com/scaling-recommendations-service-at-olx-db4548813e3a) — OLX Tech, 2025. Serving ownership moved from a shared backend to the data team.
- [Software architects and autonomous teams](https://medium.com/berlin-tech-blog/software-architects-and-autonomous-teams-328138202df1) — Berlin Tech Blog (eBay Kleinanzeigen and mobile.de), 2018. The architect's role in autonomous teams (older evidence).
- [Multi-cloud governance at scale](https://adevinta.com/techblog/multi-cloud-governance-at-scale/) — Adevinta Tech Blog (Pablo Rodriguez), 2024. Ownership catalog; "You build it, you run it (and you pay for it)".
- [How to build and scale an internal PaaS for 1,500 engineers](https://adevinta.com/es/cuentos/articulos/how-to-build-and-scale-an-internal-paas-for-1500-engineers-galo-navarro/) — Adevinta (Galo Navarro), 2020. Voluntary platform adoption and embedded migration help.
- [Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf) — Adevinta, 2024. Operating model organized by verticals; platform convergence plan.
- [Strategic Report 2025, Aurelia UK Feederco Ltd](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf) — Adevinta, 2026. Decentralized, standalone operating model; ramp-down of central functions; localized intellectual property.
- [leboncoin tech blog (RSS feed)](https://medium.com/feed/leboncoin-tech-blog) — leboncoin, 2026 (September post on the BotISS self-service bot, read via the feed summary). About ten infrastructure engineers supporting about 70 feature teams.

{id: organizing-marketplace-engineering--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Team Topologies: key concepts](https://teamtopologies.com/key-concepts) — Team Topologies (Matthew Skelton and Manuel Pais), n.d. Four team types, three interaction modes, cognitive load.
- [Documenting Architecture Decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — Michael Nygard, Cognitect, 2011. The decision record format.

{id: organizing-marketplace-engineering--research-and-practitioner-sources}
### Research and practitioner sources

- ["How Do Committees Invent?"](https://www.melconway.com/Home/Committees_Paper.html) — Melvin E. Conway, *Datamation*, 1968. Systems copy communication structures.
- [Scaling the Practice of Architecture, Conversationally](https://martinfowler.com/articles/scaling-architecture-conversationally.html) — Andrew Harmel-Law, martinfowler.com, 2021. The advice process, decision records, advisory forum, principles and technology radar.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
