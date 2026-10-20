{id: multi-country-platforms}
# 39. One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture

![One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture — logo](listing-systems-architecture/posts/39-multi-country-platforms/assets/images/39-multi-country-platforms/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn the platform models that marketplace groups use to serve many countries and brands, from the fork per country to global components beneath local products. You will design a tenancy model, a configuration hierarchy and a tenant-by-tenant release process, and decide what to share first.

> **WHY THE BUSINESS CARES:** A group with ten marketplaces pays for one fraud rule, one search upgrade or one consent change ten times when its markets are forks. When the platform is forced on them as one product, it pays in lost local fit instead. The tenancy model sets how much of every future improvement is bought once.

> **WHY ARCHITECTS SHOULD CARE:** "Multi-country" is not a deployment detail. It decides how every record, event, configuration value, release and cost line is scoped. It also decides whether one market can be changed, moved or sold without touching the others, and that decision is far cheaper to make early than to retrofit.

> **KEY POINTS:**
>
> * **The tenant is a first-class architectural element, not a column added later.** Define what a tenant is (at a marketplace group, usually brand × country), give it a stable code, and make every shared capability carry it in data, events, configuration, releases, logs and cost. Separate isolation from identity: tenants can share a cluster and still be separable.
> * **Configuration over code, with a limit.** Market differences that are data (locales, currencies, categories, fees, legal texts, feature switches) belong in versioned, schema-checked, effective-dated configuration resolved along a hierarchy. Differences that are behavior go into owned extension points. A fork is allowed only with an expiry date.
> * **Share beneath the product, starting with what is uniform and pooled.** The documented public record, Adevinta's 2019 rule above all, supports sharing infrastructure, data, trust signals, media and engines first, and treating the convergence of whole product platforms as a separate, much riskier decision. The centralization pendulum swings; design shared layers so that it can swing back.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Country Fork** — Copying a codebase per market turns every fraud rule, consent change and search fix into several projects, which this chapter replaces with tenancy and configuration.
> * **The Platform Mandate** — A shared platform that cannot express a market's real differences gets routed around, which the configure–extend–fork ladder and adoption-led sharing prevent.
> * **The Acquisition Archipelago** — Without a tenancy model, each acquired marketplace stays a separate stack because nothing exists for it to join.

Most marketplace groups grew one country at a time, by launching a site or buying a national leader, and each step was rational: local teams knew local buyers, law and competitors, and copying what worked in the last market was the fastest way into the next. The bill comes later. **Every market that was copied must later be changed separately**, and a group with ten copies of its insertion flow pays for each new rule, regulation and improvement ten times.

The opposite mistake, one platform imposed on every market, is just as common. A group sees the duplication, builds one platform and asks every market to use it as is. The platform fits the market that designed it and nobody else. Local teams add workarounds, then shadow systems, then a case for leaving. **A platform that cannot express a market's real differences is not shared; it is imposed**, and imposed platforms are routed around.

This chapter designs the architecture between those two failures, and applies Part VII's argument to markets: a shared platform earns its tenants through contracts, not mandates. It owns three terms: the **tenancy model** (what a tenant is and how every shared capability scopes, isolates and separates by it), the **global component** (a capability run once for the group beneath local products) and **configuration over code** (expressing market differences as governed data instead of code branches).

The chapter builds on the `tenant` field that the listing event envelope already carries ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)) and on the marketplace profiles of [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy). [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale) then runs the shared platform at its peak, and [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) moves acquired stacks onto the tenancy model; the organization that runs a shared platform belongs to [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering). The evidence comes from the public record of Adevinta, eBay Classifieds Group, OLX, AVIV and Vinted.

{id: multi-country-platforms--setting-the-scene-at-veldmark-one-rule-four-countries-three-days}
## Setting the Scene at Veldmark: One Rule, Four Countries, Three Days

On **Sunday 7 March 2027** at 20:11 CET, a fake "buyer" sent Femke, a private seller on Tradeyard Netherlands, a phishing link disguised as a Tradeyard Safe Deal payment page. She reported it at 20:19, the account was suspended at 20:26, and a new rule written that evening withheld **37** similar messages to other sellers. Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), had stopped the attack in one market in under an hour.

It had not stopped it in the others. Tradeyard runs four countries on **Yardstick**, its PHP monolith, and the rule reached Tradeyard Belgium only on **Wednesday 10 March**, with the next Yardstick deploy. It never reached Poland or Portugal, whose moderation runs through outsourced queues with their own rule sets. The suspended account's phone number had also registered a private-seller account on Motorvane, Veldmark's automotive marketplace, and nothing connected the two.

![Four market tiles where a fraud rule protects the first country in minutes, the second after three days, and never reaches two others or the sister car marketplace.](listing-systems-architecture/posts/39-multi-country-platforms/assets/images/39-multi-country-platforms/one-rule-four-countries.jpeg)

**Figure 1:** *One rule, four countries, three outcomes: the phishing rule protected Tradeyard Netherlands within the hour, reached Belgium three days later with the next deploy, and never reached Poland, Portugal or Motorvane.*

Ingrid Halvorsen, the Group Chief Architect, used the incident to open a question that Common Ground, the group's €140 million platform program approved in January 2027, had so far answered only with a slogan: **"share platforms, not products."** What, exactly, is a "market" in a shared platform? If one rule should reach four countries in minutes, but a Polish fee or a Belgian bilingual form should stay local, where does each difference live?

Her team's inventory in May 2027 made the problem concrete. Veldmark runs **ten marketplace tenants** across eight countries: Tradeyard in the Netherlands, Belgium, Poland and Portugal; Motorvane in Germany, the Netherlands, Poland and Austria; Hearthly in France and Spain. Keybridge, the agency software business, is a SaaS company with its own customers, not a marketplace. The tenants span **nine locales** (Dutch in the Netherlands and Belgium, French in Belgium and France, Polish, Portuguese, German in Germany and Austria, Spanish) and **two currencies**, because Poland prices in złoty. Yardstick alone contained about **2,600** conditional branches on the country code and four separate category trees (1,420, 1,380, 980 and 760 leaf categories). Motorvane, by contrast, already ran four countries on one Kotlin stack with configuration per country. Hearthly had rebranded its Spanish acquisition in 2026 and was moving it onto its French platform piece by piece; the Spanish login still ran on Casavista's code.

The three brands had each solved "multi-country" inside their own walls, in three different ways. **Common Ground had to solve it across brands**, and the decision record Ingrid's team brought to the architecture advice forum on **Wednesday 9 June 2027**, "Tenancy model v1", is the thread of this chapter.

{id: multi-country-platforms--concepts-tenants-global-components-and-configuration}
## Concepts: Tenants, Global Components and Configuration

{id: multi-country-platforms--market-brand-tenant-and-profile}
### Market, brand, tenant and profile

Marketplace groups use four words interchangeably, and the confusion causes defects. This book uses them as follows.

| Term | Definition | Veldmark example |
| --- | --- | --- |
| **Brand** | The consumer-facing marketplace identity: name, domain, design, go-to-market | Tradeyard, Motorvane, Hearthly |
| **Market** | One country (or region) in which a brand operates, with its own law, language, currency and competitors | Poland |
| **Tenant** | The unit a shared capability scopes, configures, isolates, releases and bills by; at a marketplace group, usually **brand × country** | `ty:pl` (Tradeyard Poland) |
| **Marketplace profile** | A configuration scope below the tenant for a category group with its own endpoint and monetization (see [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy)) | Tradeyard Poland vehicles: contact endpoint, insertion fees |

A **tenancy model** is the set of decisions that answer, for every shared capability: what is a tenant, how is it identified, how strongly is it isolated, how is its configuration resolved, how are changes released to it, how are its costs attributed, and how could it leave. The questions are the same for search, identity, trust and safety, media and events; the answers may differ by capability, but the tenant codes may not.

The tenant is usually brand × country rather than brand alone, because the things that differ most between markets (law, language, currency, competitors, partner ecosystems) follow the country. It is usually not smaller, because a marketplace profile or a category group shares its market's users, accounts and legal entity. Profiles are configuration scopes inside a tenant, not tenants.

{id: multi-country-platforms--isolation-is-not-identity}
### Isolation is not identity

Tenant identity and tenant isolation are separate properties, although many teams read "multi-tenant" as "shared database".

- **Tenant identity** means every record, event, request, log line, metric and cost line carries the tenant code. It is mandatory everywhere; without it nothing else in this chapter works.
- **Tenant isolation** means how strongly one tenant's data and load are separated from another's. It is a per-capability choice with a cost.

| Isolation tier | What is separate | Typical use | Cost |
| --- | --- | --- | --- |
| **Logical** | Nothing physical; a tenant key on every row, message and document, enforced in queries and access policies | Event topics, configuration, catalogs with small tenants | Cheapest; a missing filter leaks data; noisy neighbors |
| **Partitioned** | Schema, index, topic or bucket per tenant on shared infrastructure | Search indices, listing schemas, data products | Moderate; a tenant can be moved or exported as a unit |
| **Dedicated** | Cluster, database, cloud account or region per tenant | The largest tenant's peak workload; a tenant with contractual or regulatory demands; a tenant that may be sold | Highest; fleet economics lost for that tenant |

The right default for a marketplace group is **partitioned**: shared fleets, with each tenant's data in units that can be moved, rebuilt or handed over. The search chapter reaches the same conclusion for index topology: one index per brand and country, on shared clusters sized by load, with dedicated clusters only where a workload or market needs isolation ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)). One design rule follows: **moving a tenant from partitioned to dedicated must not change any client**. Aliases, routing tables and per-tenant connection configuration make that possible.

![A shared room with tagged boxes, an apartment building with movable flats, and separate houses, all with tenant tags on every box.](listing-systems-architecture/posts/39-multi-country-platforms/assets/images/39-multi-country-platforms/isolation-tiers-building.jpeg)

**Figure 2:** *Identity is mandatory at every tier; isolation is a choice. The partitioned default keeps shared fleets while each tenant's data lives in units that can be moved, rebuilt or handed over.*

{id: multi-country-platforms--global-component}
### Global component

A **global component** is a capability built and run once for the group, with a stable contract, serving many tenants beneath their local products. Examples are an image pipeline, an identity service, a moderation decision pipeline, a search engine platform or an experimentation statistics engine. A global component is not a shared product: the tenant's product team decides how, and whether, the capability appears to its users.

Adevinta's first annual report as a listed company gave the clearest public test for choosing global components. It adopted "a centralised strategy to data and analytics" because this was the area "where investment requirements are large and the technology is uniform, and where the maxim 'built once; used many times' clearly applies", while keeping "local autonomy and decentralised capacity in product and technology" elsewhere ([Adevinta Annual Report 2019](https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf), 2020). The rule has two conditions, large investment and uniform technology, and a capability must meet both. [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) shows how well the components that passed it held up over the next five years.

{id: multi-country-platforms--configuration-over-code}
### Configuration over code

**Configuration over code** is the principle that differences between tenants which are *data* are expressed as governed configuration, not as branches in code. "Data" here means values a tenant owner can change without a developer: locales, currencies, category trees, attribute requirements, fee tables, legal texts, consent purposes, moderation thresholds, feature switches, endpoints per profile.

Configuration that can express anything becomes an unreviewed programming language, so the principle comes with three companions: a **schema** for every configuration type, so invalid values fail at review rather than in production; a **resolution hierarchy**, so a value is set once at the right level and inherited below; and **change control** (versioning, review, effective dates, audit), because a configuration change in a shared platform is a production change for a tenant.

When a difference is behavior — a vehicle identification number (VIN) decoder for cars, an energy-certificate validator for French property, a Polish tax rule — it does not belong in configuration. It belongs in an **extension point**: a defined interface in the shared capability where a tenant-owned component plugs in. The ladder is configure, then extend, and only then fork.

{id: multi-country-platforms--platform-models-from-the-fork-to-the-product-platform}
## Platform Models: From the Fork to the Product Platform

Marketplace groups use six platform models, and they are not a maturity ladder: most groups run several at once, for different capabilities.

| Model | What is shared | Documented example | Where it works | Where it fails |
| --- | --- | --- | --- | --- |
| **Fork per country** | A starting codebase, copied and then evolved locally | The Schibsted-era model is widely described as local sites on a Blocket-derived code base; primary documentation is not available (see [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta)) | Fast market entry when nothing else exists | Every later improvement is built per copy: **the Country Fork** |
| **Federation with coordinated choices** | Technology decisions and sometimes tools; each brand implements | In 2015 Marktplaats described how "Marktplaats and other eBay Classifieds Group (eCG) companies" jointly evaluated replacements for eBay's legacy search engine; Marktplaats then migrated itself in three months with two or three developers ([Marktplaats Technology, 2015, republished 2017](https://medium.com/marktplaats-technology/replacing-our-legacy-search-engine-with-elasticsearch-4ad03aeceb3d)) | Strong national brands with capable teams | Duplication of every implementation; slow convergence |
| **Shared core with local configuration** | One codebase per vertical or region, configured per brand and country | OLX's 2026 frontend talk, "One-product, three brands", on "serving different countries from a single repo" ([OLX Tech, 2026](https://tech.olx.com/olx-masterclass-frontend-2026-068299a2df50)); Marktplaats, 2dehands and 2ememain "hosted on a multi-tenant platform, operated from our Amsterdam location" (Adevinta job posting, read October 2026) | Markets in one vertical with similar products | Markets whose products have really diverged |
| **Global components beneath local products** | Capabilities with contracts; products stay local | Adevinta's 2019 rule and its shared infrastructure, data, OCR, media and experimentation services (see [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta)) | Multi-brand, multi-vertical groups | Components whose contracts leak one market's assumptions |
| **Platform as product** | An internal platform that tenants choose to use | Adevinta's Common Platform, voluntary, onboarding in about ten minutes, grown from about 1,500 engineers in 2020 to more than 4,000 developers by 2023 ([Navarro, 2020](https://varoa.net/paas/infrastructure/platform/kubernetes/cloud/2020/01/02/talk-how-to-build-a-paas-for-1500-engineers.html); see [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta)) | Infrastructure and developer tooling | Capabilities where one tenant's opt-out breaks the pooled value |
| **Converged product platform** | The product itself: one platform for several brands' user journeys | Adevinta's 2023 plan to turn the leboncoin and Kleinanzeigen platforms into "a unified global platform"; AVIV's 2021 ambition of "aligning our tech roadmap across the organization to create a European real estate marketplace" | Markets that share language, law and product strategy, under stable ownership | Both public examples were reversed or rowed back by 2025 |

**Most successful multi-country sharing is within a vertical.** OLX's evidence points to one codebase per vertical serving several country brands: one frontend repository for three brands, a centralized learning-to-rank repository with brand-level configuration, and a "unified platform" in real estate credited with growth in Prosus's 2025 results ([Prosus FY25 results](https://www.lobbyregister.bundestag.de/media/57/dc/638531/prosus-financial-results-fy25-booklet.pdf), 2025). Which OLX brands share which codebase is not documented; that reading is an inference. eCG's motors vertical published a partner-facing listing API and webhook contract in 2020 (the "MoVe" reference repositories), which suggests a shared motors platform for several national sites, though the tenants are not named ([eBay Classifieds Group on GitHub, 2020](https://github.com/eBayClassifiedsGroup/reference-move-webhook-receiver)).

**Across verticals, the shared layers sit lower.** A car marketplace and a property portal share infrastructure, identity, media, messaging, trust signals and data far more easily than they share an insertion flow. [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) explains why the listing models differ.

**Both public attempts at a converged product platform were rowed back.** Adevinta's is told in [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta); AVIV's is the second. In August 2021, announcing a new chief technology officer, AVIV's chief executive said the group was "aligning our tech roadmap across the organization to create a European real estate marketplace" ([Online Marketplaces, 2021](https://onlinemarketplaces.com/?p=37137)). In December 2025 an interviewer asked the head of Immowelt about AVIV having rowed "back on its plans for a fully integrated platform for all its European portals" (the interviewer's phrase, not AVIV's). The answer was that AVIV had "strengthened the autonomy of its local businesses" while continuing "to operate group-level functions where they create clear advantages… sometimes local and sometimes cross-group" ([Online Marketplaces, 2025](https://www.onlinemarketplaces.com/articles/interview-new-immowelt-boss-theo-mseka-on-challenges-and-plans-for-the-german-market/)). What the integrated platform consisted of is not public.

{id: multi-country-platforms--architecture-a-tenancy-model-for-a-marketplace-group}
## Architecture: A Tenancy Model for a Marketplace Group

{id: multi-country-platforms--shared-and-local-layer-by-layer}
### Shared and local, layer by layer

The reference architecture below is the author's model, not a description of any company's systems. It separates what is shared from what is local by layer, and puts the tenancy services, which every layer depends on, in the middle.

![Diagram: Shared and local by layer](listing-systems-architecture/posts/39-multi-country-platforms/assets/images/39-multi-country-platforms/fig03-shared-local-layer-brands-own-product.jpeg)

**Figure 3:** *Shared and local by layer. Brands own the product surfaces, commercial terms and market policies; the group owns global components and infrastructure; the tenancy services in the middle carry every market difference down into the shared layers as configuration, extensions and release scope.*

**Local does not mean "outside the platform".** A Polish fee table, a Belgian bilingual form or a French energy-label rule is local content, but it is applied by shared components through configuration and extension contracts. The brand owns the content; the platform owns the mechanism.

{id: multi-country-platforms--the-tenant-register}
### The tenant register

The tenant register is the authoritative list of tenants and their attributes. It is small, changes rarely, and every shared capability reads it. A useful register entry holds:

- **Tenant code** — stable, never reused, short enough to appear in identifiers and log lines (`ty:pl`).
- **Brand, country, legal entity** — the entity that contracts with users and sellers, which matters for terms, invoices, data protection and statements of reasons under the EU Digital Services Act (DSA) ([Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)).
- **Locales** — as BCP 47 language tags ([RFC 5646](https://www.rfc-editor.org/rfc/rfc5646), 2009), with a default; a tenant may have several (`nl-BE`, `fr-BE`).
- **Currency** — as an ISO 4217 code with its minor unit ([ISO 4217](https://www.iso.org/iso-4217-currency-codes.html), n.d.); prices are stored in minor units with the code.
- **Time zone, territorial scope and regulator** — for scheduling, statutory deadlines and the Member State whose rules apply.
- **Hosting and isolation profile** — region, cloud account, and the isolation tier per capability.
- **Profiles** — the marketplace profiles inside the tenant, with their endpoints.
- **Lifecycle** — onboarding, live, frozen, leaving, retired.

The last attribute is the one most groups omit. A tenant that is *leaving* (sold, closed or moved to another platform) needs export jobs, transitional services and a switch-off plan, and capabilities should be able to see that state. [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) covers the deal side; the register is where the platform learns about it.

{id: multi-country-platforms--the-configuration-hierarchy}
### The configuration hierarchy

Configuration is resolved along a hierarchy, from the most general scope to the most specific. A value set at a higher level is inherited unless a lower level overrides it, and the configuration schema says at which levels each key may be set.

![Diagram: The configuration hierarchy](listing-systems-architecture/posts/39-multi-country-platforms/assets/images/39-multi-country-platforms/fig04-configuration-hierarchy-most-keys-are-set.jpeg)

**Figure 4:** *The configuration hierarchy. Most keys are set at one or two levels; the schema forbids the rest. Experiment arms sit last so that an experiment can override any value for its population without forking it.*

OLX published a small, concrete version of this idea in 2025. Its learning-to-rank projects had spread across teams and repositories and caused "duplicated efforts", so it centralized them in one repository and used the Hydra library for hierarchical configuration, with brand-level configs such as `brand: olx` and `brand: real_estate` ([OLX Tech, 2025](https://tech.olx.com/unlocking-flexibility-in-configuration-the-power-of-hydra-3f9e69263bb4)). The scope there is one capability, but the shape generalizes: one code path, configuration composed by scope.

Four rules keep a configuration hierarchy healthy.

1. **Every key has a schema, an owner and a level.** The schema states type, allowed values and the levels at which the key may be set. The owner is the team that decides its value at each level. A fee table is owned by the brand's monetization team at tenant level; a moderation threshold for phishing is owned by the trust and safety platform at group level, with tenant overrides allowed only upward (stricter).
2. **Changes are versioned, reviewed and effective-dated.** A configuration change that alters what users see is a production change. It gets a reviewer, an effective time and an audit record. Effective dating matters for regulation: a new disclosure rule applies from a date, and listings created before and after it may be validated differently.
3. **Configuration is data, not logic.** If a key starts to need conditions ("if category is bikes and the price is above €500 and the seller is new…"), it has become code. Move it into a rule engine that is designed for rules (with tests and simulation), or into an extension.
4. **Resolution is observable.** For any request, an engineer can see which value was resolved and where it came from. Without this, a multi-tenant incident becomes guesswork.

{id: multi-country-platforms--extension-points}
### Extension points

When configuration is not enough, a shared capability offers **extension points**: interfaces at defined places in its processing where a tenant-owned component runs. Each extension point has a contract (inputs, outputs, latency budget, failure behavior) and an owner on each side.

Adevinta's 2023 dispute back office is the clearest published example of the shape. Transaction events from each marketplace arrived via Kafka, SQS or REST and were normalized into one model; the user interface was a micro-frontend that marketplaces could extend; and the stated constraint was "We couldn't hardcode anything… or make any assumptions" ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/from-hello-world-to-a-dispute-management-back-office/)). Per-tenant adapters on the way in, a canonical model in the middle and an extension surface on the way out: that is the general pattern for a global component that serves different products.

The configure–extend–fork ladder decides which mechanism a difference gets:

| Rung | When | Who owns it | Exit |
| --- | --- | --- | --- |
| **Configure** | The difference is a value | Brand (content) on a group schema | — |
| **Extend** | The difference is behavior at a known point | Brand (extension) on a group contract | Promote to the core if a second tenant needs it |
| **Fork** | Neither works, and the market cannot wait | Brand, under a decision record | Expiry date and a plan to fold back or to leave the platform |

The fork rung exists because pretending it does not is how shadow systems start. A fork that is declared, dated and reviewed is a managed exception. An undeclared fork is the Country Fork in miniature.

{id: multi-country-platforms--release-by-tenant}
### Release by tenant

A shared platform changes every tenant at once unless its releases are scoped by tenant, with two mechanisms.

- **Release rings.** Deployments of a global component progress through rings of tenants: synthetic test tenants first, then small and low-risk tenants, then the largest. The ring definitions live in the tenant register.
- **Feature flags scoped by tenant.** A deployed change stays dark until a flag turns it on for a tenant, a profile or an experiment population. Pete Hodgson's taxonomy distinguishes release toggles, experiment toggles, operational toggles and permission toggles, each with a different lifetime ([martinfowler.com, 2017](https://martinfowler.com/articles/feature-toggles.html)); in a multi-tenant platform, release toggles must expire or they become permanent configuration nobody owns.

Rings and flags solve opposite problems. Rings limit the blast radius of a defect; flags let a tenant adopt a change on its own schedule. A platform needs both, and it needs one more rule: **some changes must not wait for a tenant's schedule.** A fraud rule, a security fix or a legal takedown applies everywhere it is relevant, at once. The tenancy model should name these "group-urgent" change classes in advance.

{id: multi-country-platforms--data-residency-and-data-boundaries}
### Data residency and data boundaries

For an EU marketplace group, data residency (the requirement that certain data is stored or processed only in certain places) does not mean keeping data in the user's country. The General Data Protection Regulation (GDPR) restricts transfers of personal data to countries outside the European Economic Area unless one of the transfer mechanisms in Chapter V applies ([Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj), 2016). Hosting every tenant in EU regions, and governing support and vendor access from outside the EU through those mechanisms, therefore covers most marketplace needs. Some sectors and contracts impose stricter national rules; the register's hosting profile is where such a constraint is recorded.

The harder boundary in a multi-brand group is not geographic but legal and commercial: **which tenant may use which data.** Purpose limitation under the GDPR, competition law, platform-to-business commitments and the group's own promises to customers all restrict sharing between tenants, even when the data sits in the same warehouse. A shared platform therefore needs tenant-scoped access policies by default and explicit, recorded exceptions (a shared fraud block list, for example). [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) covers governed data sharing across brands; [System of Record and Read Models: Listing Data Management](#listing-data-management) covers erasure across copies.

Multi-region deployment is a separate decision. Classifieds are mostly country-scoped businesses, so "multi-country" usually means many tenants on a platform rather than one global dataset. Vinted is the documented exception: it runs one cross-border catalog and chose "not to shard our primary data models across regions", with writes going to a primary site and read projections replicated, accepting freshness lag because "Eventual consistency is being built into how the system works, not an edge case we try to hide" ([Vinted Engineering, 2026](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-2/)). A group whose markets do not trade across borders rarely needs that design.

{id: multi-country-platforms--localization-is-more-than-translation}
### Localization is more than translation

Localization in a listing platform touches at least six layers, and only the first is text:

1. **Interface text** in each locale, owned by the brand, translated through a managed workflow, with plural and gender rules from the Unicode Common Locale Data Repository (CLDR) ([Unicode CLDR](https://cldr.unicode.org/), n.d.).
2. **Formats**: numbers, dates, prices, units and addresses. Address shapes and postcode rules belong in the gazetteer configuration ([Where Is It? Location, Geocoding and Privacy](#location-and-geo)).
3. **Taxonomy and attribute labels** per locale, on one shared concept model ([Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies), [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas)).
4. **Search analysis**: analyzers per language, and per-language fields where a country is multilingual ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)).
5. **Legal and policy content**: terms, consent texts, prohibited-item lists, mandatory disclosures, statement-of-reasons templates.
6. **Trust content**: scam patterns, phishing domains and message templates differ by language; a rule written in Dutch does not catch a Polish phishing message.

Belgium is the test case. When eBay bought 2dehands.be and 2ememain.be in 2013, its brand page described one marketplace with "bilingual" Dutch and French search and listing under two names ([eBay Classifieds Group, 2013 snapshot](https://web.archive.org/web/20130825000000/http://ebayclassifiedsgroup.com/2dehands-be-2ememain-be)). One tenant, one inventory, two locales and two consumer-facing names: a tenancy model that equates tenant with locale, or brand with domain, cannot represent it.

{id: multi-country-platforms--in-practice-veldmark-s-tenancy-model-v1}
## In Practice: Veldmark's Tenancy Model v1

{id: multi-country-platforms--the-decision-record}
### The decision record

The decision record adopted on **9 June 2027** had nine parts, summarized below with the reason for each.

| # | Decision | Reason |
| --- | --- | --- |
| 1 | A tenant is **brand × country**; ten tenants with codes `ty:nl`, `ty:be`, `ty:pl`, `ty:pt`, `mv:de`, `mv:nl`, `mv:pl`, `mv:at`, `hl:fr`, `hl:es` | Law, language, currency and competitors follow the country; the 20 marketplace profiles are configuration scopes inside tenants |
| 2 | Tenant codes appear in every group identifier (`vm:<brand>:<country>:<id>`), event envelope, API call, log line, metric label and cost tag | Identity is mandatory everywhere; the listing event contract adopted it on 1 July 2027 ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)) |
| 3 | **Keybridge is not a tenant** of Common Ground's marketplace capabilities; it integrates with Hearthly through the same public supply contract as every other vendor, and reaches the shared seller registry only as an integration principal with scoped grants ([Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts)) | The March 2027 neutrality commitment: no Keybridge agency data is used for Hearthly's advantage |
| 4 | Default isolation is **partitioned**; logical isolation is allowed for configuration and the event backbone; dedicated isolation is decided per capability and recorded | Fleet economics with movable units |
| 5 | One **configuration service** with schemas per key; resolution order group → brand → tenant → profile → seller segment → experiment; every change versioned, reviewed and effective-dated | Removes country branches from code as capabilities move out of Yardstick |
| 6 | Extension points defined per global component; brand-owned extensions must meet the component's latency and failure contract | VIN decoding (Motorvane), energy-certificate checks (Hearthly) and Polish insertion-fee rules (Tradeyard) are behavior, not values |
| 7 | **Release rings**: ring 0 synthetic tenants; ring 1 `ty:pt` and `mv:at`; ring 2 `ty:be`, `ty:pl`, `mv:nl`, `mv:pl`, `hl:es`; ring 3 `ty:nl`, `mv:de`, `hl:fr` | Smallest tenants first; the three largest tenants last |
| 8 | **Group-urgent change classes** bypass rings: fraud and scam rules, security fixes, legal takedowns | The 7 March phishing rule would have taken minutes, not three days |
| 9 | Every shared capability documents its **tenant exit path**: export format, handover, transitional run and switch-off | Veldmark is majority-owned by a private-equity investor; any tenant could be sold |

Two choices drew argument. Felix Brandt, Motorvane's chief technology officer, objected that Motorvane already ran four countries on one stack and did not need a group configuration service to tell it how. The forum's answer was decision 5's scope: the configuration service is mandatory for **global components**, not for a brand's internal services. Motorvane keeps its own configuration for its own services and uses the group service only where it consumes a group capability. Katarzyna Nowak, Tradeyard Poland's general manager, asked why her market sat in ring 2 rather than ring 1 when it had the least to lose from an early defect. The answer was traffic: with **3.6 million** live listings and 8.9 million monthly users, Poland is too large to be a canary.

{id: multi-country-platforms--the-phishing-rule-replayed}
### The phishing rule, replayed

Before the shared trust-and-safety platform went live for Tradeyard Netherlands and Belgium in **November 2027** ([Trust and Safety as a Platform](#trust-and-safety-architecture)), Ingrid's team replayed the March incident against it as a design test of the tenancy model.

![Diagram: The 7 March rule replayed on the shared platform](listing-systems-architecture/posts/39-multi-country-platforms/assets/images/39-multi-country-platforms/fig05-7-march-rule-replayed-shared-platform.jpeg)

**Figure 5:** *The 7 March rule replayed on the shared platform. The rule is policy content with a tenant scope, not a deployment. Tenants whose language the rule was written for enforce at once; tenants in other languages run it in shadow mode until a locale-specific term list is reviewed.*

The replay produced three findings that went back into the tenancy model.

- **The rule's structure was global, its content was not.** The domain-age signal (a payment domain registered that day) and the link pattern applied everywhere. The message wording that triggered the rule was Dutch. The platform split rules into a group-owned **detector** and tenant-owned **locale packs**, so a rule reaches every tenant at once, and a Polish or Portuguese pack can follow within the 48-hour shadow window.
- **Cross-brand signals need an explicit boundary.** The phone number that linked the Tradeyard account to a Motorvane account is exactly the kind of signal that pooled trust data is for. The Group Data Protection Officer had approved a shared block list holding only hashed identifiers of accounts terminated for fraud ([Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)). The tenancy model records it as the one standing exception to tenant-scoped access in trust and safety.
- **Statements of reasons are tenant-scoped.** Each moderation decision carries its tenant's legal entity, locale and territorial scope, because the DSA statement of reasons is issued by the provider to the user in the relevant Member State ([Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)). A global rule produces local decisions.

{id: multi-country-platforms--configuration-replacing-branches}
### Configuration replacing branches

The second test, on the Tradeyard insertion flow that moves out of Yardstick in the second quarter of 2028, found no country branch that justified a fork. Daan Visser's team sampled 300 of the roughly 2,600 country branches in Yardstick and classified them. About 70% were values (field lengths, mandatory attributes per category, fee amounts, legal text keys, date formats): configuration. About 20% were behavior at a small number of points (Polish insertion-fee calculation, Belgian language detection on titles, Portuguese tax identifier validation): extensions. About 10% were dead, referring to features retired years earlier.

![Country branches from a monolith sorted into a full configuration bin, a smaller extension bin, a small bin of dead code and an empty fork bin.](listing-systems-architecture/posts/39-multi-country-platforms/assets/images/39-multi-country-platforms/country-branches-sorted.jpeg)

**Figure 6:** *Sorting 300 sampled Yardstick country branches: about 70% were values for configuration, about 20% behavior for extensions, about 10% dead code, and none justified a fork.*

The Polish vehicles section shows how the layers combine. Tradeyard Poland's vehicle listings keep classifieds-style insertion fees for private sellers, priced in złoty from the brand's fee table (configuration at the `ty:pl` vehicles profile). They consume Motorvane's VIN decoding through the same extension contract Motorvane uses, as [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) recommends. And dealers above a small listing count are offered Motorvane packages, with their stock syndicated to Tradeyard through Motorvane's feed; the shared listing core records which brand owns the commercial relationship for each listing ([Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy)). **One market, two brands, one shared capability, two commercial owners**: the tenancy model has to represent all four facts.

{id: multi-country-platforms--release-rings-in-numbers}
### Release rings in numbers

The rings were used for the first time for the group taxonomy and attribute service, which went live in October 2027 with Tradeyard first. Ring 1 (`ty:pt`) received the new category resolution on Monday 4 October 2027, ring 2 a week later and ring 3 (`ty:nl`) on Monday 25 October, one week before the bikes split went live on **Monday 1 November 2027** ([Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies)). The ring-1 week found two defects that would have mattered at scale: a Portuguese label falling back to Dutch where a translation was missing, and a cache key that omitted the tenant code. **The second defect is the classic multi-tenant bug**, and it is the reason decision 2 makes the tenant code mandatory in every cache key, not only in data.

{id: multi-country-platforms--trade-offs}
## Trade-offs

{id: multi-country-platforms--choosing-a-platform-model-per-capability}
### Choosing a platform model per capability

| Capability | Fork per country | Shared core, local config | Global component | Converged product | Veldmark 2027 choice |
| --- | --- | --- | --- | --- | --- |
| Compute, cloud accounts, observability | Wasteful | — | **Yes** | — | Global; AWS primary, Hearthly on Google Cloud through 2028 |
| Identity | Splits fraud signals | Possible per brand | **Yes**, with brand profiles | — | Veldmark ID, approved June 2027, rollout 2028 |
| Trust and safety | Rules built four times | — | **Yes**, local policy as content | — | Shared pipeline, local policies |
| Search | Upgrades done three times | — | **Yes**: engine, indexer, ranking service; relevance per brand | — | Shared OpenSearch for Tradeyard and Hearthly; Motorvane stays on Elasticsearch until 2029 |
| Taxonomy and attributes | The Category Straitjacket | — | **Yes**, trees per tenant on one concept model | — | Group service, October 2027 |
| Product catalog and entitlements | Entitlement Spaghetti risk | — | **Yes**, shared model and ledger; packages and prices per brand | — | Group catalog by Q2 2028 |
| Listing insertion flow | — | **Per brand**, configured per country | — | Possible within one brand only | Per brand |
| Web and apps | — | **Per brand** | Shared SEO services ([Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture)) | — | Per brand |
| Packages, prices, sales | — | **Per brand and market** | — | — | Local |

{id: multi-country-platforms--isolation-choices}
### Isolation choices

| Choice | Benefit | Cost | When it is right |
| --- | --- | --- | --- |
| Logical isolation everywhere | Lowest cost; simplest operations | Leaks from a missing filter; noisy neighbors; hard to separate a tenant | Configuration, low-risk metadata, small tenants |
| Partitioned by default | Movable, exportable units; shared fleet | Many objects to manage; per-tenant schema changes | Most listing, search and data workloads |
| Dedicated for the largest tenant | Protects the peak; independent maintenance | Pooled economics lost; two operating modes | When one tenant's peak sets the fleet's capacity |
| Dedicated per tenant | Strongest separation; easiest sale | Fleet economics lost entirely | Regulated data, contractual isolation, an imminent sale |

{id: multi-country-platforms--when-the-guidance-does-not-hold}
### When the guidance does not hold

The configure-and-share approach assumes that markets are similar enough to be described by one model with parameters. It fails in three situations. When a market's product has diverged for structural reasons — a transactional model where others are lead-based, or a regulatory regime with no equivalent elsewhere — a shared core turns its differences into extensions that carry most of the logic, and a separate product is more honest. When one tenant is so much larger than the others that its needs dominate every design review, the "shared" platform becomes that tenant's platform with passengers, and the others are better served by components than by a core. And when ownership is likely to change soon, deep sharing creates separation work that the group will pay for at exit ([Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta)).

{id: multi-country-platforms--vertical-differences}
## Vertical Differences

| Concern | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| What varies most by country | Language, payment and shipping options, prohibited items, consumer law | Partner feed ecosystems, mandatory disclosures (energy labels), address and parcel systems, agency monetization norms | Vehicle data sources (VIN and registration databases), dealer management systems, financing partners | Labor law, salary disclosure rules, job classification standards |
| Easiest to share across countries | Identity, trust, media, messaging, search engine, ads | Media, identity, data and ML tooling, search engine | Media, VIN decoding where sources overlap, lead management, search engine | Matching infrastructure, identity, data |
| Hardest to share | Transactional journeys (PSP and carrier contracts are national) | Ingestion adapters, pro tools, valuation data sources | Dealer packages and price ratings | Classification and compliance |
| Documented signal | OLX's one-repo, three-brand frontend (2026) | AVIV integrate-then-localize (2021–2025); OLX "unified platform" in real estate (2025) | eCG motors vertical partner API (2020) | — |

Real estate is the hardest vertical to share across countries. National professional-software ecosystems, mandatory disclosures and valuation data sources differ more between countries than anything in general classifieds, and the abstraction cost falls on exactly the features that make a portal win locally. A shared engine with local ingestion, disclosure and pro-tooling edges fits the evidence; a single property product across countries does not. [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) owns the profiles; [AVIV Group: Building a European Real-Estate Platform from Acquisitions](#case-aviv) examines AVIV's record.

{id: multi-country-platforms--failure-modes}
## Failure Modes

1. **The tenant added as an afterthought.** A capability built for one brand gains a `tenant` column when a second brand joins. Caches, search queries, exports, metrics and cost reports miss it for months, and the first cross-tenant leak is found by a customer.
2. **Brand equated with domain or locale.** Belgium breaks it (one tenant, two locales, two names); Poland's vehicles section breaks it (one tenant, two commercial owners); a rebrand breaks it (one tenant, two domains during migration).
3. **Configuration that became code.** Conditional expressions in configuration values, with no tests, no simulation and no owner. The shared platform's real behavior is now spread across hundreds of untested configuration files.
4. **Release toggles that never expire.** Every release flag left in place becomes permanent per-tenant configuration with no schema, and the number of possible platform behaviors grows with the product of all of them.
5. **Rings without a group-urgent lane.** A fraud rule waits for the largest tenant's release window, which is the Yardstick problem rebuilt on a modern platform.
6. **The largest tenant as the design authority.** Tradeyard Netherlands carries about 45% of Tradeyard's search traffic. If every shared component is designed in its review meetings, the smaller tenants get a platform built for someone else.
7. **Pooled data without recorded boundaries.** Signals pooled for fraud detection quietly become inputs to ranking, pricing or sales targeting, in breach of the purpose they were pooled for and of commitments such as Keybridge's.
8. **No exit path.** A shared capability that cannot export or hand over one tenant's data turns any future sale or carve-out into a rebuild under deadline.

{id: multi-country-platforms--the-chief-architect-s-view}
## The Chief Architect's View

**Decide the tenancy model once, early, at group level.** The tenant definition, the code format, the mandatory carriage of the tenant code and the exit-path requirement are group decisions recorded in one decision record and changed only through the architecture forum. Everything else in this chapter can vary by capability; those cannot.

**Decide the platform model per capability, not for the group.** "Are we a shared platform or a federation?" is the wrong question. The right one is asked capability by capability: does it pass both halves of Adevinta's 2019 test, large investment *and* uniform technology? Does its value grow when data is pooled, as it does for fraud signals and experimentation statistics? Can it be shared without converging the product above it? I would score every Common Ground capability on those three questions and publish the scores, because the scores make the disagreements discussable.

**What to share first.** In order: infrastructure and cloud governance, because they are uniform and invisible to users; the event backbone and data platform, because every later capability depends on them; trust signals and identity, because their value grows with pooling and fraud does not respect brand boundaries; media and the search engine, because they are expensive and technically uniform; then the taxonomy service and the catalog and entitlements model, which need the tenancy services to exist. Product surfaces come last and are often never shared. The sequence after an acquisition follows similar logic with deal-specific constraints; [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) develops it.

**Who decides.** The group decides schemas, contracts and the tenancy model; the brand decides configuration values, extensions and product. The platform team decides how a capability is built and run, and is accountable to its tenants for service levels and cost. When a brand asks for a fork, the forum decides, and the decision record carries an expiry date.

**What to watch.**

- **Adoption without mandate.** For each global component, the share of eligible tenants and workloads using it, and the reasons of those that do not. A platform that only grows by mandate is heading for the Platform Mandate.
- **Country branches in code.** The count should fall as capabilities move to configuration; a rising count is an early sign of a new fork.
- **Configuration health.** Keys without an owner, release toggles older than their expiry, values set at forbidden levels.
- **Lead time from one tenant to all.** For a fraud rule, a consent change or a search improvement: the time from first tenant to last. On 7 March 2027 this was three days to Belgium and never to Poland or Portugal.
- **Cost per tenant.** Every shared capability reports cost by tenant, so tenants can see what they pay for and the group can see whether pooling saves money.
- **Separability drills.** Once a year, export one tenant's data from each shared capability and prove it can run on its own. The drill is cheap; discovering at signing that it cannot be done is not.

**The pendulum.** Marketplace groups swing between centralization and local autonomy, and the public record shows both Adevinta (2023 convergence, 2025 decentralization) and AVIV (2021 integration, 2025 localization) swinging within a few years. I do not think a Chief Architect can stop the pendulum; ownership, strategy and leadership change faster than platforms. What the architecture can do is make the swing cheap in both directions: global components with contracts that a tenant can leave, configuration that a tenant can take with it, and products that never depended on another brand's code. **The goal is not the right position on the pendulum; it is a platform that survives the next swing.** [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution) returns to this as the cost to reverse each sharing decision.

{id: multi-country-platforms--questions-to-ask}
## Questions to Ask

1. What is a tenant in our platform, what is its code, and does every record, event, cache key, log line and cost line carry it?
2. For each shared capability, what is its isolation tier, and could we move one tenant to dedicated infrastructure without changing any client?
3. Which market differences live in code today, and how many of them are values that belong in configuration?
4. Does every configuration key have a schema, an owner, permitted levels and an effective date? Who reviewed the last change to it?
5. Which extension points does each global component offer, and which brand-owned extensions run in them under what contract?
6. How long does a fraud rule, a security fix or a consent change take to reach every relevant tenant? Which change classes bypass release rings?
7. Which data do our tenants share with each other, under which recorded exception, and for which purpose only?
8. For each shared capability, what is the exit path for one tenant: export, handover, transitional run, switch-off?
9. Which shared components grew by adoption and which by mandate, and what would happen if the mandate were withdrawn?
10. Is any current initiative converging whole product platforms rather than sharing capabilities beneath them? If so, where is its separate investment case?

{id: multi-country-platforms--from-sharing-to-staying-up}
## From Sharing to Staying Up

A tenancy model decides how the platform is shared; it does not decide whether the shared platform stays up when everyone uses it at once. The next chapter, [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale), takes the shared platform to its Sunday-evening peak and asks how to keep it fast, available and affordable.

{id: multi-country-platforms--sources-and-evidence}
## Sources and Evidence

{id: multi-country-platforms--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Adevinta Annual Report 2019](https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf) — Adevinta, 2020. The "large investment, uniform technology" rule for centralizing data and analytics while keeping product local.
- [How to build a PaaS for 1500 engineers](https://varoa.net/paas/infrastructure/platform/kubernetes/cloud/2020/01/02/talk-how-to-build-a-paas-for-1500-engineers.html) — Galo Navarro, 2020. Voluntary adoption and ten-minute onboarding of Adevinta's Common Platform.
- [From Hello World to a dispute management back office](https://adevinta.com/techblog/from-hello-world-to-a-dispute-management-back-office/) — Adevinta Tech Blog, 2023. Per-tenant ingestion, canonical model and extensible micro-frontend for a cross-marketplace component.
- [Replacing our legacy search engine with Elasticsearch](https://medium.com/marktplaats-technology/replacing-our-legacy-search-engine-with-elasticsearch-4ad03aeceb3d) — Marktplaats Technology, 2015 (republished 2017). Coordinated technology choice across eCG companies, local migration.
- [Reference MoVe webhook receiver](https://github.com/eBayClassifiedsGroup/reference-move-webhook-receiver) — eBay Classifieds Group, 2020. Partner listing API and webhook contract of the eCG motors vertical.
- [eBay Classifieds Group: 2dehands.be – 2ememain.be](https://web.archive.org/web/20130825000000/http://ebayclassifiedsgroup.com/2dehands-be-2ememain-be) — eBay Classifieds Group, 2013 (archived snapshot). One bilingual marketplace under two names.
- [Adevinta job posting describing the Benelux multi-tenant platform](https://portfoliojobs.tcv.com/companies/adevinta-2/jobs/64812161-business-development-customer-success-operations-smb) — Adevinta via TCV portfolio jobs, n.d. (read October 2026). Marktplaats, 2dehands and 2ememain on one multi-tenant platform; recruiter copy, not a technical account.
- [OLX Masterclass Frontend 2026](https://tech.olx.com/olx-masterclass-frontend-2026-068299a2df50) — OLX Tech, 2026. One repository serving three brands in different countries.
- [Unlocking flexibility in configuration: the power of Hydra](https://tech.olx.com/unlocking-flexibility-in-configuration-the-power-of-hydra-3f9e69263bb4) — OLX Tech, 2025. Centralized learning-to-rank repository with hierarchical brand configuration.
- [Prosus financial results FY25](https://www.lobbyregister.bundestag.de/media/57/dc/638531/prosus-financial-results-fy25-booklet.pdf) — Prosus, 2025. OLX real-estate growth credited to "the rollout of a unified platform".
- [Building a global event-driven platform, part 2](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-2/) — Vinted Engineering, 2026. Single-writer primary with replicated read projections across regions.
- [Ex-eBay Classifieds and Domain CTO Brent McLean switches to AVIV Group](https://onlinemarketplaces.com/?p=37137) — Online Marketplaces, 2021. AVIV's integration ambition across its European portals.
- [Interview: new Immowelt boss Theo Mseka](https://www.onlinemarketplaces.com/articles/interview-new-immowelt-boss-theo-mseka-on-challenges-and-plans-for-the-german-market/) — Online Marketplaces, 2025. AVIV rowing back from a fully integrated platform toward local autonomy with selective group functions.

{id: multi-country-platforms--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — European Union, 2016. Chapter V rules on transfers outside the EEA; purpose limitation.
- [Regulation (EU) 2022/2065 (Digital Services Act)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) — European Union, 2022. Statements of reasons and Member State scope of moderation decisions.
- [RFC 5646: Tags for Identifying Languages](https://www.rfc-editor.org/rfc/rfc5646) — IETF, 2009. BCP 47 locale tags such as `nl-BE` and `fr-BE`.
- [ISO 4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html) — ISO, n.d. Currency codes and minor units.
- [Unicode Common Locale Data Repository](https://cldr.unicode.org/) — Unicode Consortium, n.d. Locale formats and plural rules.

{id: multi-country-platforms--research-and-practitioner-sources}
### Research and practitioner sources

- [Feature Toggles (aka Feature Flags)](https://martinfowler.com/articles/feature-toggles.html) — Pete Hodgson, martinfowler.com, 2017. Toggle categories and lifetimes.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
