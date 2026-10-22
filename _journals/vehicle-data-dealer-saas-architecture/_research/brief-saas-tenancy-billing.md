# Research brief: B2B SaaS architecture for dealer platforms (tenancy, identity, entitlements, onboarding, configuration, billing and auditability)

Prepared 22 October 2026 for chapter writers of *Architecting a Vehicle Data and Dealer SaaS Platform*. The brief is vendor-neutral. AWS, Microsoft and Stripe get the most space because they have published unusually detailed, dated architecture guidance on multi-tenant SaaS and metering, not because the book endorses their products. Dealer-software vendors (Cox Automotive, CDK Global, Tekion) appear wherever they have described their identity or platform model in public, which is rarely in depth.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (22 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date, not the fetch date. Undated product and documentation pages are marked "n.d., accessed 2026-10".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, analyst, vendor summary, community post), or a primary page that could not be fetched in this session (for example, HTTP 403).
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about a proprietary system the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Two of the most cited AWS sources, *SaaS Tenant Isolation Strategies* (August 2020) and *SaaS Architecture Fundamentals* (August 2022), are now banner-marked by AWS as "for historical reference only". Their vocabulary (silo, pool, bridge, control plane, application plane) is still the industry's lingua franca, but chapter writers should not cite them as current AWS product guidance. The AWS PostgreSQL row-level-security blog post is from May 2020 (older than three years); the PostgreSQL behaviour it describes was re-checked against the PostgreSQL 18 documentation. Cox Automotive's Bridge ID page describes a rollout "at the end of 2020 and the beginning of 2021".

**Research limitation.** The session shared a web-search quota with other researchers, so most evidence comes from direct fetches of known documentation URLs. As a result:

- **Dealer-software identity and tenancy internals are thinly documented.** Cox Automotive (Bridge ID, Bridge Federation) and CDK Global (CDK Unify) publish marketing-level descriptions only. Tekion publishes no identity or permission model. Nothing public describes how Reynolds and Reynolds, Keyloop, Pinewood, incadea, MijnVWE, mobile.de or AutoScout24 dealer tools model dealer groups, rooftops or user roles. Those statements are tagged ASSUMPTION/JUDGEMENT.
- **Pages that blocked fetching:** the ISO 27001 product page (403), the FASB ASC 606 page (403), the CDK Unify press release on BusinessWire (403), and the US eCFR (redirected to a bot check; Cornell LII's copy of 16 CFR 314.4 was used instead).
- **Not covered:** Okta's B2B organisation model and Google Cloud's SaaS-specific (non-GKE) multi-tenancy guidance were not fetched. Amazon Verified Permissions' multi-tenant design page returned an empty body, so per-tenant versus shared policy-store trade-offs below are judgement.
- **Germany's e-invoicing dates** come from KPMG's summary of the BMF letter, not from the BMF itself.

**Volatility flags.** ⚠ marks claims likely to change within 12 months, such as product names, ownership, API limits and regulatory dates.

---

## PART 1: Tenancy models and tenant isolation

### 1.1 What a "tenant" is on a dealer platform

The hardest early decision is not silo versus pool. It is what the tenant *is*. On a dealer platform there are at least four candidate units: the **rooftop** (one physical site, often one franchise point), the **dealer legal entity** (VAT-registered company, the party to the contract), the **dealer group** (a holding with many entities and rooftops), and the **brand or franchise** (one rooftop can hold several OEM franchises).

- Microsoft's guidance warns that for B2B customers "consider whether your customers have divisions, like teams or departments, and whether they have a presence in multiple countries or regions. You might need to map a single customer to multiple tenants if there are different requirements for these subgroups" [VERIFIED: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenancy-models, published 2025-06-11].
- The same page says choosing a tenancy model "isn't only a technical decision. It's also a commercial decision" [VERIFIED: same URL, published 2025-06-11].
- Microsoft's tenant-lifecycle guidance lists **merge and split** as first-class lifecycle events: "companies might be acquired or merge, including companies located in different geographic regions" and "companies might split or divest" [VERIFIED: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenant-lifecycle, published 2025-06-13].

[ASSUMPTION/JUDGEMENT] For dealer SaaS, the pattern that survives acquisitions best is: **tenant = contracting organisation (dealer group or independent)**, with **rooftops as first-class child resources** inside it, not separate tenants. Dealer groups buy and sell rooftops constantly. If a rooftop is a tenant, every acquisition becomes a cross-tenant data merge. If a rooftop is a child node, an acquisition is a re-parenting operation plus a data-ownership decision.

| Candidate tenant unit | Works well for | Breaks when |
| --- | --- | --- |
| Rooftop | Single-site independents; per-site billing | Group wants cross-rooftop stock, pricing, reporting and one user identity |
| Legal entity | Invoicing, VAT, contracts, GDPR controller role | One group has many entities; one entity runs many rooftops |
| Dealer group | Group-wide users, reporting, SSO | A rooftop is sold to another group (split) |
| OEM / franchise | OEM programmes, co-op marketing | Multi-franchise rooftops; independents have no OEM |

### 1.2 Silo, pool and bridge (AWS) and the Azure equivalents

- **Silo**: "tenants are provided dedicated resources", but "a silo environment still relies on a shared identity, onboarding, and operational experience". That shared control is what separates SaaS from a managed-service model "where customers might be running separate versions of your product" [VERIFIED: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/silo-pool-and-bridge-models.html, SaaS Lens published 2023-04-04].
- **Pool**: tenants share resources, "the more classic notion of multi-tenancy" [VERIFIED: same URL, 2023-04-04].
- **Bridge**: a mixed mode in which "some microservices in your architecture might be implemented with silo and others might use pool". The deciding factors are "the regulatory profile of a service's data and its noisy neighbor attributes" [VERIFIED: same URL, 2023-04-04].
- AWS's isolation whitepaper says the pool model cannot be used "as a rationale to relax the isolation requirements". Shared infrastructure "increases the chance for cross-tenant access" [VERIFIED: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/pool-isolation.html, published 2020-08-01, now marked historical].
- The same paper lists the pool model's costs: noisy neighbour, harder **tenant cost tracking**, larger **blast radius** ("an outage will likely impact all the tenants") and **compliance pushback** [VERIFIED: same URL, 2020-08-01].
- **Tier-based isolation**: premium tenants may pay for a silo, but providers "will often require these premium customers to run the same version of the product" so that "the silo environment becomes a clone of the pooled environment that happens to be supporting one tenant" [VERIFIED: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/tier-based-isolation.html, 2020-08-01].

Microsoft names four models: **automated single-tenant**, **fully multitenant**, **vertically partitioned** (some tenants shared, some dedicated, or tenants mapped to geographic deployments) and **horizontally partitioned** (shared app tier, per-tenant databases). It calls isolation "a spectrum" rather than a discrete property [VERIFIED: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenancy-models, 2025-06-11]. The single-tenant risk is put plainly: "If a single tenant requires a specific infrastructure cost, 100 tenants probably require 100 times that cost" [VERIFIED: same URL].

Microsoft also separates **tenants from deployments** ("stamps"). A tenant-mapping layer routes each request to the deployment that holds its data, and tenants can be moved between deployments [VERIFIED: same URL].

Google's GKE guidance distinguishes **enterprise multi-tenancy** (teams within one company, one namespace per team) from **SaaS provider multi-tenancy**, where end users "never touch the Kubernetes control plane". It warns that pod anti-affinity and taints can be circumvented by malicious tenants and suit only trusted tenants; GKE Sandbox (gVisor) is the option for untrusted workloads [VERIFIED: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview, updated 2026-10-13].

**Across markets.** No dealer-SaaS regulator in NL, BE, DE, UK or the US prescribes a tenancy model. Pressure for silos comes from large customers' procurement (dealer groups, OEMs, captive finance arms) and from data-residency preferences, not from law. [ASSUMPTION/JUDGEMENT] OEM-owned or OEM-mandated programmes (for example, a manufacturer's certified used-car scheme) are the most likely source of silo demands in Europe. In the US, the largest public dealer groups are the most likely source.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] For ~10,000 dealer customers, of whom perhaps 80–90% are single-rooftop or small groups, the economic default is **pool for the application plane, with a tenant-to-deployment map from day one**. That map allows a small number of **cells** (stamps) by region (EU vs US, which matches the book's Europe-first, US-contrast geography) and a premium **silo-clone** tier for the few 100-rooftop groups that demand it. Never fork the code for a silo.

### 1.3 Data isolation patterns in PostgreSQL

| Pattern | AWS term | Isolation | Cost and ops at 10,000 tenants | Typical failure |
| --- | --- | --- | --- | --- |
| Database (or instance) per tenant | Silo | Strongest | High; 10,000 databases to migrate, back up, monitor | Schema drift; migration fan-out |
| Schema per tenant | Bridge | Medium | Medium; catalogue and migration fan-out grow with tenant count | Slow migrations; connection-pool churn |
| Shared tables + `tenant_id` + RLS | Pool | Policy-enforced | Lowest | A missing policy, a `BYPASSRLS` role, or a leaked session variable |
| Shared tables, distributed by `tenant_id` (Citus) | Pool + sharding | Policy-enforced; big tenants can be moved to their own shard | Low; adds a distribution layer | Cross-tenant queries become scatter-gather |

- The AWS mapping: silo = database per tenant, bridge = schema per tenant, pool = shared tables with a tenant column. In the pool model isolation is "often enforced only by developers writing the right `WHERE` clause" unless RLS is used [VERIFIED: https://aws.amazon.com/blogs/database/multi-tenant-data-isolation-with-postgresql-row-level-security/, published 2020-05-18; older than three years].
- The RLS pattern compares `tenant_id` with `current_setting('app.current_tenant')`, set per connection. The post warns that session variables "may conflict with server-side poolers such as pgBouncer" [VERIFIED: same URL, 2020-05-18].
- PostgreSQL documentation (version 18 current): with RLS enabled, "all normal access to the table for selecting rows or modifying rows must be allowed by a row security policy". With no policy, "a default-deny policy is used". "Superusers and roles with the BYPASSRLS attribute always bypass the row security system". Table owners bypass RLS unless `FORCE ROW LEVEL SECURITY` is set. Permissive policies combine with `OR`, restrictive ones with `AND` [VERIFIED: https://www.postgresql.org/docs/current/ddl-rowsecurity.html, PostgreSQL 18.6 docs, accessed 2026-10].
- Citus's multi-tenant guide distributes every table by the tenant key (`company_id`), keeps a tenant's data on one node, and notes that tenant sizes "tend to follow a Zipfian distribution". A large tenant can be moved to a dedicated shard with `isolate_tenant_to_new_shard` [VERIFIED: https://docs.citusdata.com/en/stable/use_cases/multi_tenant.html, n.d., accessed 2026-10].

**Across markets.** No difference in law. [ASSUMPTION/JUDGEMENT] GDPR (EU) and UK GDPR make a cross-tenant leak of consumer personal data (leads, buyers, finance applicants) a notifiable breach. In the US, the FTC Safeguards Rule makes it a reportable event once 500 or more consumers' unencrypted information is involved (see 8.4). This raises the cost of the pool model's failure mode in both regions.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Use **pool + RLS as defence in depth**, not as the only control. The application layer still scopes queries by tenant.
- Run the app as a **non-owner role without BYPASSRLS** and add **FORCE ROW LEVEL SECURITY** to every tenant table.
- **Set tenant context per transaction** (`SET LOCAL`), not per session, so pooled connections cannot leak it.
- Write automated **cross-tenant leak tests** in CI. Microsoft explicitly recommends testing that "one tenant's data isn't accidentally leaked to another" [VERIFIED: tenancy-models URL above, 2025-06-11].
- Expect a Zipf-like size distribution: a 100-rooftop group may hold more stock, leads and deals than hundreds of independents together. Plan to move whales to their own shard or cell.

### 1.4 Noisy neighbours and usage limits

- Microsoft defines the antipattern: "The noisy neighbor problem occurs when one tenant's performance is degraded because of the activities of another tenant." It also occurs when many small tenants peak at once [VERIFIED: https://learn.microsoft.com/en-us/azure/architecture/antipatterns/noisy-neighbor/noisy-neighbor, published 2025-06-11].
- Provider-side mitigations: per-tenant monitoring, **resource governance** through throttling and rate limiting, rebalancing tenants across stamps, running non-time-sensitive work off-peak, capping query cost ("a maximum returnable record count or query time limit"), and QoS prioritisation [VERIFIED: same URL].
- Microsoft says to treat these as "resource governance problems" and to "be transparent with clients about any throttling mechanisms or usage quotas" [VERIFIED: same URL].
- Usage limits "are often used in combination with feature and service-level pricing", and report generation is a typical rate-limited operation [VERIFIED: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/pricing-models, published 2024-11-07].

**Across markets.** [ASSUMPTION/JUDGEMENT] Load is seasonal and calendar-driven, and the peaks differ by country:
- **UK**: plate-change months (March and September) concentrate registrations and retail activity.
- **NL and BE**: year-end and January peaks follow tax and BPM changes.
- **DE**: month-end and quarter-end OEM targets drive peaks.
- **US**: month-end and quarter-end retail pushes, plus weekend selling.

A single shared cell sees all of these.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Noisy-neighbour sources on dealer platforms are predictable:
- bulk inventory feed imports (a group re-sending 5,000 vehicles);
- syndication to dozens of portals;
- bulk valuation and VIN-decode jobs;
- end-of-month reporting and DMS re-syncs.

Put these behind **per-tenant queues with fair scheduling** and per-tenant concurrency caps, separate from interactive desk and appraisal traffic.

### 1.5 Tenant-aware observability and cost attribution

- Microsoft gives two reasons to measure per-tenant consumption: to know "the actual cost to serve each tenant" and "the amount to charge the tenant" [VERIFIED: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/measure-consumption, published 2024-11-12].
- Approaches, from cheapest to most precise: **indicative metrics** (for example, data stored), **transaction metrics** (one key business event), **per-request metrics**, and **estimates** (reasonable when each tenant uses less than about 2% of a deployment) [VERIFIED: same URL].
- Warning: APM tools sample. Application Insights "isn't designed to store every piece of telemetry", so "for billing and metering purposes, choose a data store that gives you a high level of accuracy" [VERIFIED: same URL].
- The noisy-neighbour page recommends including "the tenant's identifier in the telemetry so that you can aggregate request unit usage for each tenant" [VERIFIED: noisy-neighbor URL above, 2025-06-11].
- OpenTelemetry **baggage** propagates context such as a client or tenant ID downstream. It is not added to spans automatically, it travels in HTTP headers visible on the network, and automatic instrumentation may pass it to third-party APIs [VERIFIED: https://opentelemetry.io/docs/concepts/signals/baggage/, n.d., accessed 2026-10].

**Across markets.** [ASSUMPTION/JUDGEMENT] Telemetry that carries user identifiers or IP addresses is personal data under GDPR and UK GDPR. Keep tenant IDs in telemetry and keep user and consumer identifiers out of it, or pseudonymise them.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Carry **tenant ID and rooftop ID as mandatory span and log attributes**, set at the edge from the verified token, never from client-supplied headers.
- Strip baggage at egress to portals, lenders and OEM APIs.
- Keep **billing usage in a separate, lossless event store**, not in the observability pipeline.
- Expect per-tenant COGS to be **estimate-based for most small dealers** and **measured for the largest groups**, whose contracts are negotiated.

### 1.6 Blast radius: the CDK Global incident (June 2024)

- Back-to-back cyberattacks hit CDK Global on 19 June 2024. CDK shut down its systems as a precaution and said it serves "more than 15,000 retail locations across North America", though it was "not immediately clear whether all of them were affected" [VERIFIED: https://www.clickondetroit.com/business/2024/06/21/car-dealerships-are-being-disrupted-by-a-multi-day-outage-after-cyberattacks-on-software-supplier/, AP report published 2024-06-21].
- CDK restored its core DMS and Digital Retailing solutions on the afternoon of 19 June. A second incident followed that evening [VERIFIED: same URL].
- Stellantis said many dealerships switched to manual processes, "writing up orders by hand". NADA flagged uncertainty about what customer data may have been compromised [VERIFIED: same URL].
- Several reports say many dealers were still offline near the end of June 2024 [WIDELY REPORTED: https://arcticwolf.com/resources/blog/cdk-global-cyber-incident/, 2024].

[ASSUMPTION/JUDGEMENT] CDK has not published an architectural post-mortem, so nothing here says *why* the outage was so wide. The lesson the book can draw safely is general: when one vendor runs the system of record for many thousands of rooftops, a security incident becomes an industry outage. Shutting everything down "as a precaution" is what a provider does when it cannot prove that the compromise is contained to one cell. **Cell boundaries that are also security boundaries** (separate credentials, separate networks, separate control-plane access) let a provider isolate part of the fleet instead of all of it.

**Across markets.** The incident was North American. [ASSUMPTION/JUDGEMENT] European dealer-software markets are more fragmented by country (Keyloop, Pinewood and Autoline-family DMS in the UK; incadea and OEM-mandated DMS in Germany; VWE and others in NL), so one incident is less likely to take out a whole national market at once.

---

## PART 2: Hierarchical B2B tenancy and identity

### 2.1 Organisation hierarchies: how platforms model groups and sub-units

- **Salesforce Automotive Cloud** models dealerships as **business accounts**, linked to each other through **account-account relationships** with party-role relationships. Two dealerships "reporting to the same parent account" sit at the same level, and a parent-subsidiary relationship links a parent company to a subsidiary. **Party relationship groups** store group-level data for "dealer groups, conglomerates, or households" [VERIFIED: https://trailhead.salesforce.com/content/learn/modules/stakeholder-modeling-in-automotive-cloud/manage-households-and-groups, n.d., accessed 2026-10]. Note that this is an OEM- and dealer-CRM data model, not a SaaS tenancy model: the dealer group is a *record* inside the OEM's org.
- **ServiceNow domain separation** offers "nested-multi-tenancy so parent tenants can access child tenant resources" within a single instance. Members of a domain "see only the data contained within their domain or the child domains". Domains can carry their own business rules and notifications. Once activated, domain separation "can be disabled, [but] it cannot be removed from an instance" [VERIFIED: https://www.servicenow.com/docs/r/platform-security/c_DomainSeparation.html, n.d., accessed 2026-10].
- Microsoft: B2B customers may need "two instances of your service" (for example, dev and prod), and tenants need merge and split support [VERIFIED: tenancy-models and tenant-lifecycle URLs above].

[ASSUMPTION/JUDGEMENT] The dealer-SaaS hierarchy that matches how groups operate:

```
Tenant (contracting organisation: dealer group or independent)
 ├── Legal entity (VAT number, invoicing, GDPR controller)  [0..n]
 │    └── Rooftop / site (address, franchises, stock location) [1..n]
 │         └── Department (sales new, sales used, service, parts, F&I)
 └── Regions / brand clusters (optional groupings for reporting and permissions)
```

The ServiceNow lesson applies directly: **parent-sees-children** visibility is the default that dealer groups expect (group head office sees all rooftops), and **rooftop-only** visibility is the default for rooftop staff. Make the hierarchy a data structure, not a hard-coded depth: some groups have regions, some do not.

### 2.2 B2B identity products

- **Auth0 Organizations** "best supports business-to-business (B2B) implementations". Each customer maps to one organisation with its own enterprise connection (SSO), member roles, invitations and "lightweight branding". Users may belong to several organisations [VERIFIED: https://auth0.com/docs/manage-users/organizations/organizations-overview, n.d., accessed 2026-10].
  - Limitations listed: Universal Login only, and "no custom domains per organization" [VERIFIED: same URL].
  - The page says nothing about nested organisations. [ASSUMPTION/JUDGEMENT] Treat organisations as flat, and model the group-to-rooftop hierarchy in the application's own authorisation layer.
- **Microsoft Entra B2B collaboration** lets partners "use their own credentials" and represents them as guest users (`#EXT#`). Cross-tenant access settings can trust MFA and device claims from the partner's tenant [VERIFIED: https://learn.microsoft.com/en-us/entra/external-id/what-is-b2b, published 2026-04-24].
  - From a rollout completed by the end of 2025, guests are redirected to their home organisation's sign-in page [VERIFIED: same URL].

[ASSUMPTION/JUDGEMENT] For dealer SaaS, "B2B collaboration" is the pattern for **cross-organisation users**: a group's central marketing agency, an OEM field manager, a lender's underwriter or an auditor. These users act inside a dealer tenant but belong elsewhere. Model them as **external memberships with expiry**, not as copied accounts.

### 2.3 Enterprise SSO and SCIM provisioning

- **OpenID Connect Core 1.0** (final, incorporating errata set 2, 15 December 2023) is an identity layer on top of OAuth 2.0 [VERIFIED: https://openid.net/specs/openid-connect-core-1_0.html, published 2023-12-15].
- **SCIM 2.0** protocol, RFC 7644 (Standards Track, September 2015). Its intent is "to reduce the cost and complexity of user management operations by providing a common user schema, an extension model, and a service protocol" [VERIFIED: https://www.rfc-editor.org/rfc/rfc7644.txt, published 2015-09]. The core schema is RFC 7643.
- Microsoft Entra's provisioning service polls an app's SCIM endpoint: "The process runs every 40 minutes." Deprovisioning is commonly expressed as `"active": false`, and requests carry an OAuth 2.0 bearer token. Microsoft: SCIM "when used with federation standards like SAML or OpenID Connect" gives "an end-to-end, standards-based solution for access management" [VERIFIED: https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups, published 2026-09-15].

**Across markets.**
- **US**: the FTC Safeguards Rule requires covered dealers to "implement multi-factor authentication for any individual accessing any information system" (16 CFR 314.4(c)(5)) [VERIFIED: https://www.law.cornell.edu/cfr/text/16/314.4, accessed 2026-10]. Most US dealers that arrange financing are covered (see 8.4). This turns MFA from a feature into a customer compliance requirement.
- **EU and UK**: no dealer-specific MFA mandate was found. [ASSUMPTION/JUDGEMENT] GDPR Art. 32's "appropriate technical and organisational measures" and large groups' own security policies drive MFA and SSO demand.
- **Germany and the Netherlands**: works-council co-determination (see 8.5) can apply to systems that log employee activity, which includes identity and audit logs.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Offer **three login tiers** matched to customer size:
  1. platform-managed accounts with mandatory MFA for independents;
  2. **per-tenant OIDC/SAML federation** for groups with Entra ID, Okta or Google Workspace;
  3. **SCIM** for groups with 500+ staff and high turnover (sales staff churn is high).
- With a 40-minute provisioning cycle, a departed salesperson may keep access for up to 40 minutes after HR removes them. Short session lifetimes plus federation-time checks close that window.

### 2.4 Dealer-software examples (public evidence only)

- **Cox Automotive Bridge ID** is "Cox Automotive's single sign-on". It covers Dealer.com, Dealertrack F&I & DMS, HomeNet, KBB Instant Cash Offer, vAuto, VinSolutions, Xtime and Autotrader. Users attach one account per solution, and the rollout was "at the end of 2020 and the beginning of 2021" [VERIFIED: https://www.coxautoinc.com/bridgeid/, n.d., accessed 2026-10]. ⚠ The solution list changes with Cox's portfolio.
- **Cox Bridge Federation Single Sign On** lets dealerships and lender partners with their own IdP sign in with their existing credentials. It requires dealers to "Adopt OIDC … as the protocol for authenticating Bridge users". Every federated employee must already be a Bridge user, and employees deactivated in the dealer's IdP lose access. Enrolment is by request form, with follow-up "within 5 business days" [VERIFIED: https://www.coxautoinc.com/bridge/federation/, n.d., accessed 2026-10].
- **CDK Unify** offers "a secure, cloud-based single sign-on" with multifactor authentication and "role-based dashboards" [VERIFIED: https://www.cdkglobal.com/cdk-unify, n.d., accessed 2026-10]. CDK introduced it at NADA Show 2023 as "a personalized, secure and single sign-on to CDK applications with new modern role-based workflows" [WIDELY REPORTED: https://www.businesswire.com/news/home/20230123005158/en, 2023-01-23; page returned 403, wording taken from a search snippet].
- **Tekion** describes three clouds: ARC for retailers, AEC for OEMs and enterprises, APC for partners. It claims a platform "built on a secure, unified data foundation" and markets multi-site operation as "Run 50 stores like one". It publishes no identity or permission model [VERIFIED: https://tekion.com/, n.d., accessed 2026-10].

[ASSUMPTION/JUDGEMENT] The pattern in both Cox's and CDK's public material is **portfolio SSO bolted onto acquired products**: one identity linked to per-product accounts ("attach a single solution account from each"). This is the typical end state of growth by acquisition, and it is why both vendors present SSO as a product. A platform built new should start with **one identity and one tenant directory shared by every product**, and treat per-product accounts as a migration path, not as the model.

**Across markets.** [ASSUMPTION/JUDGEMENT] No European DMS or dealer-software vendor publishes an equivalent federation programme. UK and Dutch dealer groups commonly run Microsoft 365, so Entra ID federation is the first IdP to support in Europe.

---

## PART 3: Authorisation models

### 3.1 RBAC, ABAC and ReBAC, and Zanzibar

| Model | Decision based on | Dealer example | Weakness |
| --- | --- | --- | --- |
| RBAC | User's role | "Used-car manager" can reprice stock | Role explosion ("used-car manager at rooftops 3, 7, 12") |
| ABAC | Attributes of user, resource, context | Can approve a deal if `deal.gross < user.approval_limit` and `deal.rooftop in user.rooftops` | Policies get hard to audit |
| ReBAC | Graph of relationships | User is `manager` of `region:north`, which is `parent` of `rooftop:12`, which `owns` `vehicle:VIN` | Needs a relationship store and consistency model |

- Google's Zanzibar paper (USENIX ATC 2019) describes a system that stores "trillions of access control lists", handles "millions of authorization requests per second", keeps 95th-percentile latency under 10 ms, and achieved more than 99.999% availability over three years [VERIFIED: https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/, published 2019].
- Zanzibar's data model is the **relation tuple**, `⟨object⟩#⟨relation⟩@⟨user⟩`. Groups are "simply ACLs with membership semantics", and `tuple_to_userset` lets permissions inherit through a parent object (for example, a document inherits from its folder) [VERIFIED: https://www.usenix.org/system/files/atc19-pang.pdf, published 2019].
- The paper's **"new enemy" problem**: if the order of ACL changes is ignored, or old ACLs are applied to new content, a removed user may see new material. Zanzibar prevents this with external consistency and **zookies**, opaque consistency tokens that encode a timestamp [VERIFIED: same PDF, 2019].

[ASSUMPTION/JUDGEMENT] The dealer version of the new-enemy problem is real. A salesperson is moved from rooftop A to rooftop B (or leaves for a competitor in the same town) and, through a stale cache, still sees rooftop A's leads and trade-in valuations. Lead data is commercially sensitive between competing rooftops, even within one group.

### 3.2 Policy engines: OpenFGA, Cedar and Amazon Verified Permissions, OPA

- **OpenFGA** is open-source, "inspired by" Zanzibar, "relies on Relationship-Based Access Control", supports RBAC directly and some ABAC through contextual and conditional tuples, and "is owned by the Cloud Native Computing Foundation" [VERIFIED: https://openfga.dev/docs/fga, n.d., accessed 2026-10].
- **Cedar** is "a new authorization policy language designed to be ergonomic, fast, safe, and analyzable". It is implemented in Rust, its design properties are proved in Lean, and the authors report it performs "far better" than OpenFGA and Rego in their evaluation [VERIFIED: https://arxiv.org/abs/2403.04651, published 2024-03-07]. Treat the performance comparison as the authors' own benchmark.
- **Amazon Verified Permissions** externalises authorisation with Cedar (currently Cedar 4.12 ⚠). It "presumes that the principal has been previously identified and authenticated through other means" and is priced per authorisation request [VERIFIED: https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html, n.d., accessed 2026-10].
- **Open Policy Agent** is "a graduated Cloud Native Computing Foundation (CNCF) project". "OPA decouples policy decision-making from policy enforcement". Policies are written in Rego [VERIFIED: https://www.openpolicyagent.org/docs, n.d., accessed 2026-10].

[ASSUMPTION/JUDGEMENT] Amazon Verified Permissions offers two multi-tenant designs: a policy store per tenant (stronger isolation, but 10,000 stores to version and roll out) or one shared store with tenant-scoped policies (simpler, but a single bad policy can cross tenants). The AWS guidance page could not be read in this session.

### 3.3 Modelling a dealer group in ReBAC terms

[ASSUMPTION/JUDGEMENT] A minimal OpenFGA-style model the chapter can use as an illustration (not taken from any vendor):

```
type user
type tenant
  relations
    define admin: [user]
    define member: [user] or admin
type region
  relations
    define tenant: [tenant]
    define manager: [user] or admin from tenant
type rooftop
  relations
    define parent: [region, tenant]
    define manager: [user] or manager from parent
    define staff: [user] or manager
type vehicle
  relations
    define rooftop: [rooftop]
    define can_reprice: manager from rooftop
    define can_view: staff from rooftop
type lead
  relations
    define rooftop: [rooftop]
    define assignee: [user]
    define can_view: assignee or manager from rooftop
```

This handles group admins, regional managers, multi-rooftop staff and lead privacy without one role per combination. Attribute conditions (approval limits, deal gross, time of day) fit in conditional tuples or in a Cedar or OPA layer.

**Across markets.** [ASSUMPTION/JUDGEMENT] The **F&I role** differs by market:
- **US**: F&I managers handle credit applications covered by GLBA and the FTC Safeguards Rule, so finance-application access needs a narrower permission than sales.
- **UK**: consumer-credit broking is FCA-regulated, so dealers acting as credit brokers carry similar sensitivity.
- **NL, BE and DE**: lease and finance roles are less separated in dealer staffing.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Keep **coarse tenant isolation** (RLS plus tenant-scoped tokens) separate from **fine-grained authorisation** (ReBAC). If the authorisation service fails or is misconfigured, tenant isolation still holds.
- Cache authorisation decisions with a **consistency token** (zookie-style) after any membership change.
- Emit every permission change to the audit log.

---

## PART 4: Entitlements, plans and feature flags

- Pete Hodgson's taxonomy has four toggle categories: **release, experiment, ops and permissioning**. Permissioning toggles "change the features or product experience that certain users receive" and "may be very-long lived", "at the scale of multiple years" [VERIFIED: https://martinfowler.com/articles/feature-toggles.html, revised 2017-10-09; older than three years, still the standard reference].
- Microsoft: feature- and tier-based pricing requires "your solution to be aware of the features that are available at each price tier". Feature toggles can provide this "but this requires ongoing maintenance" and "increase the overhead to ensure high quality, because there are more code paths to test" [VERIFIED: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/pricing-models, 2024-11-07].
- Microsoft warns that "feature-based pricing isn't usually a good option for non-production environments", because tenants want to test and train on the same features they have in production [VERIFIED: same URL].

| Concept | Owned by | Lifetime | Evaluated where | Source of truth |
| --- | --- | --- | --- | --- |
| Plan / package | Commercial (pricing team) | Years | Billing + entitlement service | Contract / subscription |
| Entitlement | Product + billing | Contract term | Entitlement service, cached in token or edge | Derived from plan + add-ons + overrides |
| Limit / quota | Product + SRE | Contract term | Rate limiter, job scheduler | Entitlement service |
| Release flag | Engineering | Days to weeks | Flag service | Flag config |
| Ops / kill switch | SRE | Long | Flag service | Flag config |
| Permission | Customer admin | Ongoing | Authorisation service | Customer's role assignments |

[ASSUMPTION/JUDGEMENT] The common failure is to implement entitlements as permissioning flags in a release-flag tool. The flag tool then becomes a shadow billing system with no contract history, no effective dates and no audit trail. Keep an **entitlement service** that derives "what this tenant (and this rooftop) has bought" from the subscription, with effective-dated records, and let release flags only *narrow* what entitlements allow.

**Dealer example: the cost of rollout speed.** Auto Trader UK reports that "retailer numbers softened slightly during the year", reflecting difficult trading conditions and "concerns with the speed and nature of our Deal Builder product roll-out". Average retailer forecourts fell 0.5% to 13,942, and were 1.7% lower in the second half [VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21]. [ASSUMPTION/JUDGEMENT] Auto Trader has not described its rollout mechanics. The general lesson is that dealer customers react commercially (by withdrawing stock) to product changes that alter their workflow. Per-tenant and per-rooftop rollout control, opt-in windows and entitlement-based gating are commercial tools, not only engineering ones.

**Across markets.** [ASSUMPTION/JUDGEMENT]
- **Europe**: packaging by country is common (a German tenant may have DAT valuations entitled, a Dutch tenant RDW-based data, a UK tenant DVLA and MOT data). The entitlement model needs a **market dimension**, not only a tier.
- **US**: packaging often follows OEM certification programmes and state-specific forms (F&I, titling).

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Entitlements are **rooftop-scoped** as often as tenant-scoped. A group may buy the appraisal tool for 40 of its 100 rooftops.
- Model entitlements as **(tenant, rooftop?, product, feature, limit, effective_from, effective_to, source_contract)**. Publish changes as events so the authorisation, rate-limiting and UI layers all read the same truth.

---

## PART 5: Onboarding, data migration and offboarding

### 5.1 Onboarding

- AWS places onboarding, identity, metrics and billing in a **control plane** that is "global to all tenants" and "not actually multi-tenant". Tenant resource **provisioning** belongs to the application plane [VERIFIED: https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/control-plane-vs.-application-plane.html, published 2022-08-03, now marked historical].
- Microsoft's onboarding checklist covers: self-service vs automated vs manual process, **data residency**, compliance, disaster-recovery targets (RTO/RPO), required information, billing options and pre-production environments [VERIFIED: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenant-lifecycle, 2025-06-13].
- Trials raise their own questions: whether trial tenants share production infrastructure, "how to migrate data from a trial tenant to a paid tenant", and misuse prevention [VERIFIED: same URL].

[ASSUMPTION/JUDGEMENT] Dealer onboarding has its own steps:
1. Verify the dealer is a real trade business (company register, VAT number, dealer licence in US states, an OEM dealer code for franchised rooftops).
2. Map rooftops to addresses and franchises.
3. Connect the DMS (often requiring the DMS vendor's approval and a third-party access programme).
4. Connect portal and syndication accounts.
5. Import historic stock, customers and deals.
6. Configure pricing rules and user roles.

Self-service sign-up suits independents. Groups need an assisted onboarding project.

### 5.2 Data migration

[ASSUMPTION/JUDGEMENT] Migrations into dealer SaaS are mostly **coexistence migrations**: the dealer's DMS stays the system of record for accounting and parts while the SaaS takes over inventory, pricing or CRM. Design for idempotent, re-runnable imports keyed on natural identifiers (VIN, stock number, DMS customer number), with reconciliation reports the dealer signs off. A full DMS replacement is a different project of months, with a cut-over at month-end.

### 5.3 Offboarding and switching

- **EU Data Act** (Regulation (EU) 2023/2854) applies from 12 September 2025. Recital 81 states that "data processing services" include SaaS. Its switching chapter requires a written contract with:
  - a **maximum notice period** for initiating switching that "shall not exceed two months";
  - a mandatory maximum **transitional period of 30 calendar days**, during which the provider must "provide reasonable assistance" and "maintain business continuity";
  - an "exhaustive specification of all categories of data and digital assets that can be ported";
  - a **data retrieval period of at least 30 calendar days**;
  - "full erasure" afterwards.

  [VERIFIED: http://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22 (OJ); Articles 25 and 50, Recital 81]
- **Switching charges**: from 11 January 2024 to 12 January 2027 providers may charge only reduced switching charges, capped at direct costs. "From 12 January 2027, providers of data processing services shall not impose any switching charges" [VERIFIED: same, Article 29]. ⚠ This takes effect within months of the book's publication.
- **Custom-built services** are partly exempt: services whose main features were "custom-built to accommodate the specific needs of an individual customer" and that are "not offered at broad commercial scale" are exempt from some obligations, including Article 29 [VERIFIED: same, Article 31].
- **GDPR Art. 28(3)(g)**: a processor must, "at the choice of the controller", delete or return all personal data at the end of the service. Art. 28(2): a processor "shall not engage another processor without prior specific or general written authorisation of the controller" [VERIFIED: http://publications.europa.eu/resource/celex/32016R0679, published 2016-05-04].
- Microsoft's offboarding considerations: the retention period, whether to support re-onboarding, and deactivation as a temporary state, distinct from offboarding [VERIFIED: tenant-lifecycle URL, 2025-06-13].

**Across markets.**
- **EU (NL, BE, DE)**: the Data Act switching rules plus GDPR Art. 28 apply.
- **UK**: UK GDPR Art. 28 applies. [ASSUMPTION/JUDGEMENT] The EU Data Act does not apply in the UK, though a UK dealer platform serving EU customers falls within its scope for those customers.
- **US**: there is no equivalent switching law. The FTC Safeguards Rule requires dealers to oversee service providers "by contract" and to dispose of customer information securely [VERIFIED: https://www.law.cornell.edu/cfr/text/16/314.4, accessed 2026-10].

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Build **tenant export** as a product feature from day one: full, machine-readable, documented, and including configuration metadata and audit logs.
- Under the Data Act this is an obligation for EU customers, and from 12 January 2027 it must be free.
- Build **verified tenant erasure** (including backups, search indices and analytics copies) with a certificate of deletion.
- Pooled storage makes erasure harder than silo storage. Track every place tenant data lands.

---

## PART 6: Configuration versus customisation

- Salesforce's multitenant architecture stores customisations as metadata: "the platform simply stores some metadata that it can then use at runtime". Org-specific objects and fields are virtual, defined in "a few database tables known as the Universal Data Dictionary (UDD)". "Every org-specific record in shared database tables has an OrgID". The platform enforces "an extensive set of governors and resource limits" on customer code [VERIFIED: https://architect.salesforce.com/fundamentals/platform-multitenant-architecture, n.d., accessed 2026-10].
- ServiceNow domain separation allows "tenant-specific system policies such as email notifications, business rules" per domain [VERIFIED: https://www.servicenow.com/docs/r/platform-security/c_DomainSeparation.html, n.d., accessed 2026-10].
- ServiceNow practitioners describe the upgrade cost of customisation. A customised base record becomes a "skipped record" during upgrade that the platform "will not automatically overwrite". Recent advice is "configuration over code where possible" [WIDELY REPORTED: https://www.servicenow.com/community/developer-blog/reducing-skipped-records-in-servicenow-upgrades/ba-p/3102307, 2024; community post, not official documentation].

| Lever | What the customer changes | Upgrade risk | Dealer example |
| --- | --- | --- | --- |
| Settings | Values of predefined options | None | Default margin target, VAT scheme, working hours |
| Rules / policies | Declarative rules evaluated by the platform | Low if the rule language is versioned | Auto-reprice after 30 days by 2%; lead routing by brand |
| Custom fields / objects | Schema extension as metadata | Low–medium | "Warranty provider" field on vehicle; group-specific KPI |
| Workflow / approval designer | Steps and approvers | Medium | Deal sign-off above €X gross needs the sales director |
| Templates | Documents, emails, window stickers | Low | Brand-specific invoice and offer PDFs |
| Extensions (code) | Sandboxed functions, webhooks, partner apps | Medium–high | Custom export to a group's data warehouse |
| Forked code / per-tenant branch | Product source | Very high, never | – |

[ASSUMPTION/JUDGEMENT] With 10,000 tenants, a dealer platform cannot afford the Salesforce-scale metadata engine, and should not try. Offer **settings, rules, custom fields, approval workflows and templates** as metadata with tenant- and rooftop-level inheritance (group sets the default, rooftop overrides where allowed). Push anything beyond that to **webhooks and a partner API**. The hierarchy matters here too: groups want to *lock* some settings centrally (pricing policy, legal texts) and *delegate* others to rooftops.

**Across markets.** [ASSUMPTION/JUDGEMENT] Country-specific configuration is mandatory, not optional:
- invoice and VAT rules (margin scheme vs standard VAT on used cars in EU and UK);
- registration and tax fields (BPM in NL; Kfz-Steuer and Zulassung data in DE; V5C and MOT in UK; state titling and fees in US);
- language (NL/FR/DE for Belgium);
- legally required documents.

Treat these as **market packs** maintained by the provider, distinct from tenant configuration.

---

## PART 7: Billing, metering and revenue recognition

### 7.1 Pricing models for dealer platforms

- Microsoft's catalogue: consumption, per-user, per-active-user, **per-unit** ("in a solution sold to brick-and-mortar retailers, a per-store pricing model might be appropriate regardless of how many users are in each store"), feature- and service-level tiers, freemium, cost-of-goods and flat-rate. Its advice: "implement only one or two models, with a few tiers" [VERIFIED: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/pricing-models, 2024-11-07].
- On bill shock when pricing changes: "Calculate or simulate each tenant's bill before and after the change" [VERIFIED: same URL].
- **Dealer example (UK): Auto Trader's retailer pricing.** Auto Trader reports average revenue per retailer (ARPR) of **£2,995 per month** across **13,942 average retailer forecourts** in the year to 31 March 2026. ARPR is decomposed into three levers:
  - **price**: +£117, from "the annual 1 April 2025 pricing and product event";
  - **stock**: −£48, from retailers advertising fewer vehicles;
  - **product**: +£72, from adding Co-Driver to packages.

  It also refers to a "package staircase" [VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21]. This is a public example of **hybrid dealer pricing**: per-forecourt subscription, scaled by stock volume, with tiered packages and an annual price event. ⚠ The figures change each reporting period.

[ASSUMPTION/JUDGEMENT] Natural value metrics for dealer SaaS are **per rooftop** (subscription), **per vehicle in stock or advertised** (volume), and **per transaction** (valuation, history report, VIN decode, lead, credit check, e-signature). Seat pricing fits poorly, because dealers share logins when seats are priced (a security problem) and staff turnover is high.

### 7.2 Metering pipelines: Stripe, Metronome and Orb

- **Stripe Billing meters** aggregate meter events with **sum, count or last**, using raw or pre-aggregated ingestion. Configuration cannot be changed after creation "aside from the display name" [VERIFIED: https://docs.stripe.com/billing/subscriptions/usage-based/meters/configure, n.d., accessed 2026-10]. ⚠ All limits below may change.
  - **Timestamps**: within "the past 35 calendar days" and not more than 5 minutes in the future. Acceptance "doesn't guarantee that Stripe can include the usage on an invoice" once it is finalised [VERIFIED: https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api, n.d., accessed 2026-10].
  - **Rate limits**: 1,000 meter-event calls per second per account, one concurrent call per customer per meter. API v2 meter event streams reach 10,000 events per second, and up to 200,000 by arrangement [VERIFIED: same URL].
  - **Dimension cardinality**: 10,000 unique combinations per meter per hour, and 100 per customer per meter [VERIFIED: same URL].
  - **Corrections**: meter event adjustments can cancel events "sent to Stripe within the last 24 hours". Stripe won't issue a corrected invoice for usage already on a finalised invoice [VERIFIED: meters/configure URL above].
- **Stripe idempotency**: keys up to 255 characters. In API v1 keys may be pruned after 24 hours. Reusing a key with different parameters errors [VERIFIED: https://docs.stripe.com/api/idempotent_requests, n.d., accessed 2026-10].
- **Stripe acquired Metronome.** Stripe announced completion on 14 January 2026 [VERIFIED: https://stripe.com/newsroom/news/stripe-completes-metronome-acquisition, published 2026-01-14]. The deal was announced on 2 December 2025 [WIDELY REPORTED: https://www.pymnts.com/acquisitions/2025/stripe-acquires-metronome-to-enhance-metered-pricing-capabilities-for-ai-companies, 2025]. Stripe's docs now say the Billing Meters approach "is appropriate only if you're already using Billing Meters" and recommend Metronome "for new integrations" [VERIFIED: https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage, n.d., accessed 2026-10]. ⚠ Product positioning is moving fast.
- **Metronome**: usage events require `transaction_id`, `customer_id`, `timestamp` and `event_type`. "Subsequent events within the next 34 days with the same ID are treated as duplicates and ignored". Retry guidance:
  - "always retry a failed call to /ingest until you receive a 200";
  - back off exponentially on 429;
  - "do not automatically retry" other 4xx errors; send them to a dead-letter queue.

  [VERIFIED: https://docs.metronome.com/guides/events/send-usage-events, n.d., accessed 2026-10]
- Metronome's core concepts: billable metrics that "transform raw usage events", products, rate cards with dated rates, contracts with overrides, prepaid **credits**, and minimum-spend **commitments** [VERIFIED: https://docs.metronome.com/guides/get-started/how-metronome-works, n.d., accessed 2026-10].
- **Orb** describes **query-based billing**. "Every usage event is stored immutably in a columnar data store". At invoice time "Orb executes a fresh query over the raw event data". Amendments apply "as a read-path overlay". Late data invalidates "only the affected invoice fragments". Usage for closed periods is carried as "catch-up adjustments to the next open period" [VERIFIED: https://docs.withorb.com/architecture/query-based-billing, n.d., accessed 2026-10].

| Design choice | Counter-based (aggregate on ingest) | Query-based (store raw, compute at invoice) |
| --- | --- | --- |
| Late events | Adjust counters; risky after close | Recompute affected fragments |
| Pricing change mid-period | Hard | Re-run query with new rate card |
| Dispute evidence | Aggregates only | Raw events available |
| Cost | Low storage | Columnar store of every event |
| Example | Stripe Billing meters (aggregation per period) | Orb (as described) |

[ASSUMPTION/JUDGEMENT] For a dealer platform the billable events are few in type but high in commercial sensitivity: each vehicle history report, valuation or credit check is a line the dealer may dispute. **Keep raw usage events with their business key** (VIN, stock number, user, rooftop, request ID) for at least the dispute window plus the statutory invoice retention period. Derive the billing aggregate from them; never let the aggregate be the only record.

### 7.3 Idempotent usage events, rating, credits and disputes

[ASSUMPTION/JUDGEMENT] The reference pipeline the book can draw:

```
Product service ──(usage event: id, tenant, rooftop, sku, qty, business_key, occurred_at)──▶ outbox
    ▶ usage log (append-only, dedup on id)  ──▶ rating (rate card × entitlement × contract)
    ▶ rated usage ──▶ invoice draft ──▶ review window ──▶ finalised invoice ──▶ e-invoice / PDF
                         ▲ credits, commits, adjustments (each with reason code and actor)
```

- The **event ID is created at the business moment** (for example, the report-generation request), not at send time, so retries and replays stay idempotent. Metronome's 34-day dedup window and Stripe's 24-hour idempotency-key pruning show that vendor dedup windows are finite, so the platform needs its own dedup store.
- **Free re-pulls**: a dealer re-opening the same history report within N days should not be charged again. This is a rating rule keyed on (tenant, VIN, product, window), not a dedup rule.
- **Group billing**: a 100-rooftop group usually wants one invoice per legal entity, or one consolidated invoice with rooftop breakdown, and cost-centre codes. Billing accounts must map to the tenant hierarchy independently of the authorisation hierarchy.
- **Disputes and credits**: every credit note needs a reason code, an actor and a link to the disputed usage events. Credits are audit-relevant (Part 8).

### 7.4 Revenue recognition basics (ASC 606 / IFRS 15)

- IFRS 15 was issued in May 2014 alongside FASB Topic 606 and is effective for periods beginning on or after 1 January 2018. Its core principle is to recognise revenue to "depict the transfer of promised goods or services to the customer". Its **five steps**:
  1. identify the contract;
  2. identify the performance obligations;
  3. determine the transaction price, including variable consideration;
  4. allocate the price by relative stand-alone selling prices;
  5. recognise revenue when each obligation is satisfied, at a point in time or over time.

  [VERIFIED: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/, n.d., accessed 2026-10]
- [ASSUMPTION/JUDGEMENT] Architecture consequences:
  - Bundles of subscription, implementation services, usage and hardware need **stand-alone selling prices per SKU** in the catalogue.
  - Prepaid credits are contract liabilities until consumed.
  - Usage is usually recognised as it occurs.
  - Onboarding fees may need deferral.

  The billing system must therefore export **contract, performance obligation and SKU-level data** to the general ledger, not only invoice totals. Confirm specifics with the finance chapter and auditors.

### 7.5 Invoicing obligations across markets

- **Belgium**: "Structured electronic invoices between companies are compulsory since 2026" (from 1 January 2026 for VAT-liable businesses), with a tolerance period in the first three months of 2026 [VERIFIED: https://einvoice.belgium.be/en, n.d., accessed 2026-10]. The Belgian public sector has recommended Peppol since 2016 [VERIFIED: https://www.peppol.org/learn-more/country-profiles/belgium/, updated 2025-04-11].
- **Germany**: businesses must be able to receive EN 16931 e-invoices from 1 January 2025. Issuing becomes mandatory from 2027 for businesses with turnover above €800,000 and from 2028 for all [WIDELY REPORTED: https://kpmg.com/us/en/taxnewsflash/news/2024/10/tnf-germany-guidelines-for-complying-with-first-phase-of-e-invoicing-mandate.html, 2024]. ⚠ Verify against the BMF.
- **United Kingdom**: "the government will require the use of electronic invoicing for all VAT invoices for business-to-business and business-to-government transactions from 2029, with a roadmap to be published at Budget 2026" [VERIFIED: https://www.gov.uk/government/publications/budget-2025-document/budget-2025-html, published 2025-11-26]. ⚠ Whether the roadmap has been published was not verified.
- **EU**: ViDA was adopted on 11 March 2025. "Digital Reporting Requirements will affect cross-border B2B transactions from 1 July 2030" [VERIFIED: https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en, n.d., accessed 2026-10].
- **Netherlands**: no domestic B2B e-invoicing mandate was found in this session [ASSUMPTION/JUDGEMENT; re-verify].
- **United States**: no federal B2B e-invoicing mandate [ASSUMPTION/JUDGEMENT]. Sales tax on SaaS varies by state, so the billing engine needs a tax-calculation service for US customers.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The platform's *own* invoices to Belgian and (soon) German dealers must be structured e-invoices, so the billing stack needs an **e-invoicing output channel** (Peppol access point or equivalent) per market. Dealer SaaS that *produces invoices for dealers* (vehicle sales invoices from a DMS or sales module) faces the same mandates on the dealer's behalf. That is a bigger feature than billing.

---

## PART 8: Audit logging, compliance and assurance

### 8.1 What an audit log must be

- NIST's draft log-management guide defines log management as "the process for generating, transmitting, storing, accessing, and disposing of log data" [VERIFIED: https://csrc.nist.gov/pubs/sp/800/92/r1/ipd, initial public draft published 2023-10-11; still a draft, so cite with care].
- **Tamper evidence, reference implementation.** CloudTrail log-file integrity validation uses "SHA-256 for hashing and SHA-256 with RSA for digital signing". Hourly digest files reference that hour's log files. "Each digest file also contains the digital signature of the previous digest file", which forms a chain that detects modification and deletion and can "assert positively that no log files were delivered … during a given period" [VERIFIED: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html, n.d., accessed 2026-10].
- **Customer-facing audit log, reference implementation.** GitHub Enterprise Cloud keeps audit events for 180 days (Git events for seven), offers streaming to external systems and an Audit log API, and records actor, action (`category.operation`), date and time, country, SAML SSO and SCIM identity, authentication method and optionally source IP [VERIFIED: https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/about-the-audit-log-for-your-enterprise, n.d., accessed 2026-10].

[ASSUMPTION/JUDGEMENT] Three audit logs that dealer platforms often conflate:

| Log | Audience | Content | Retention driver |
| --- | --- | --- | --- |
| Security / admin audit | Customer admins, provider security, auditors | Logins, MFA, role and permission changes, SSO and SCIM events, exports, API keys | SOC 2 / ISO 27001 evidence; FTC Safeguards (US) |
| Business audit trail | Dealer managers, OEMs, regulators | Price changes, deal edits, discount approvals, odometer and damage edits, document versions | Consumer law, finance-compliance, dispute evidence |
| Billing audit | Finance, customer accounts payable | Usage events, rating inputs, credits, invoice changes | Tax record-keeping, revenue recognition |

The **business audit trail** is the one most specific to vehicles. Who changed the advertised price, the recorded mileage, or the damage disclosure, and when, is evidence in consumer disputes and in odometer-fraud cases.

### 8.2 Immutability design

[ASSUMPTION/JUDGEMENT]
- Write audit events to an **append-only store** with per-tenant hash chaining (CloudTrail-style digests per tenant per hour), and store digests in object storage with object lock.
- Expose a **customer-facing audit API and export** with tenant- and rooftop-scoped filters.
- Never let application admins (the provider's or the customer's) delete audit entries. Retention expiry is a policy job that itself writes a log entry.

### 8.3 SOC 2 and ISO 27001 expectations

- SOC 2 examinations report on controls "Relevant to Security, Availability, Processing Integrity, Confidentiality, or Privacy" [VERIFIED: https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services, n.d., accessed 2026-10].
- [ASSUMPTION/JUDGEMENT] Type 1 reports on control design at a point in time; Type 2 reports on operating effectiveness over a period (commonly 6–12 months). US dealer groups and lenders ask for SOC 2 Type 2. European buyers more often ask for ISO/IEC 27001 certification.
- [ASSUMPTION/JUDGEMENT; ISO page blocked] ISO/IEC 27001:2022's Annex A includes controls on logging and monitoring activities. Auditors under either framework will sample access reviews, change management, logging and tenant-isolation evidence.

### 8.4 US: FTC Safeguards Rule (dealers as financial institutions)

- The FTC states the Safeguards Rule covers "most automobile dealers who finance or lease automobiles". Dealers that "finance (or facilitate the financing of)" vehicles are financial institutions, as are those that lease "for longer than 90 days" [VERIFIED: https://www.ftc.gov/business-guidance/resources/automobile-dealers-ftcs-safeguards-rule-frequently-asked-questions, published 2025-06].
- Requirements relevant to SaaS:
  - MFA "for any individual accessing any information system" (314.4(c)(5));
  - controls "to monitor and log the activity of authorized users" (314.4(c)(8));
  - overseeing service providers, including "requiring your service providers by contract to implement and maintain such safeguards" (314.4(f)).

  [VERIFIED: https://www.law.cornell.edu/cfr/text/16/314.4, accessed 2026-10]
- The FAQ: "when you give a service provider access to customer information, you must monitor the safeguards" [VERIFIED: FTC FAQ URL above, 2025-06].
- Breach notification to the FTC applies when "at least 500 consumers' unencrypted information" is involved, no later than 30 days after discovery, and took effect in May 2024 [VERIFIED: https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know, n.d., accessed 2026-10].

**Architecture implication.** [ASSUMPTION/JUDGEMENT] For US dealers, the platform's MFA, user-activity logging and contractual safeguards are inputs to the *dealer's* compliance programme. Offer a **Safeguards evidence pack**: MFA enforcement reports, user-activity log exports, the SOC 2 report and a breach-notification commitment.

### 8.5 Europe: user-activity logs and works councils

- **Germany**: §87(1) no. 6 BetrVG gives the works council co-determination over the "introduction and use of technical devices designed to monitor the behaviour or performance of employees" (translated from German) [VERIFIED: https://www.gesetze-im-internet.de/betrvg/__87.html, accessed 2026-10].
- **Netherlands**: Article 27(1)(l) of the Works Councils Act (WOR) requires works-council consent for "a regulation on facilities aimed at or suitable for observing or monitoring the attendance, behaviour or performance" of staff (translated from Dutch) [VERIFIED: https://wetten.overheid.nl/BWBR0002747/, accessed 2026-10].

[ASSUMPTION/JUDGEMENT] German courts have read "designed to" broadly, to cover systems *capable* of monitoring. Per-user audit logs, salesperson leaderboards and lead-response-time dashboards in dealer SaaS can therefore trigger co-determination at larger German and Dutch dealer groups. Features such as **configurable pseudonymisation of user-level analytics** and **documented log purposes and retention** shorten the dealer's works-council process. The UK, Belgium and the US have no equivalent co-determination veto in this form; Belgium has consultation duties through its own bodies (not researched here).

---

## PART 9: Putting it together for ~10,000 dealer customers

[ASSUMPTION/JUDGEMENT] The reference shape for this book. Everything in this part is the analyst's synthesis of Parts 1–8.

| Concern | Independents (1 rooftop, the large majority) | Mid groups (2–20 rooftops) | Large groups (20–100+ rooftops) |
| --- | --- | --- | --- |
| Tenancy | Pooled cell per region | Pooled cell | Pooled cell by default; silo-clone cell as a paid tier |
| Identity | Platform accounts + mandatory MFA | Optional OIDC/SAML federation | Federation + SCIM; external memberships for agencies and OEM staff |
| Authorisation | Preset roles | Roles + rooftop scoping | ReBAC over group → region → rooftop → department; delegated admin |
| Entitlements | Plan package | Plan + rooftop-level add-ons | Negotiated contract; rooftop-level entitlements; market packs |
| Configuration | Settings + templates | + rules, custom fields | + locked group policies, approval workflows, webhooks and API |
| Onboarding | Self-service + verification | Assisted | Project with DMS integration, data migration, cut-over plan |
| Billing | Card or direct debit; per-rooftop subscription + usage | Invoice per entity | Consolidated invoice, cost centres, commits and credits, e-invoicing |
| Audit | In-app audit view | Export | Streaming to the group's SIEM; evidence packs |
| Offboarding | Self-service export | Export + assistance | Data Act switching plan (EU), certified erasure |

Design rules the chapters can state as the book's position:

1. **The tenant is the contracting organisation; rooftops are children.** Acquisitions are re-parenting, not merges.
2. **Two authorisation layers.** Coarse tenant isolation (tokens + RLS) never depends on fine-grained policy being correct.
3. **The control plane is a product.** Tenant registry, tenant-to-cell map, identity, entitlements, metering, billing and audit are shared services with their own SLOs.
4. **Cells are security boundaries as well as scaling units.** This is the CDK lesson.
5. **Usage events are evidence.** Store them raw, idempotent and attributable, because dealers dispute per-VIN charges.
6. **Export and erasure are features.** In the EU they are legal obligations, and switching charges end on 12 January 2027.
7. **Market packs, not forks.** Country rules (tax, registration, invoicing, documents, works-council-friendly analytics) are provider-maintained configuration.

---

## Key numbers

| Number | Value | Source | Date |
| --- | --- | --- | --- |
| Zanzibar scale | Trillions of ACLs; millions of checks/s; p95 < 10 ms; >99.999% availability over 3 years | Google, USENIX ATC | 2019 |
| CDK locations affected or served | "More than 15,000 retail locations across North America" | AP via ClickOnDetroit | 2024-06-21 |
| Entra SCIM provisioning cycle | Every 40 minutes | Microsoft Learn | 2026-09-15 |
| Stripe meter event timestamp window | Past 35 days; ≤5 minutes future | Stripe docs | accessed 2026-10 |
| Stripe meter event rate limit | 1,000 calls/s per account; v2 streams 10,000 events/s (200,000 by arrangement) | Stripe docs | accessed 2026-10 |
| Stripe meter adjustment window | Cancel events sent within last 24 hours | Stripe docs | accessed 2026-10 |
| Stripe idempotency key pruning (v1) | After ≥24 hours | Stripe API docs | accessed 2026-10 |
| Metronome dedup window | 34 days on `transaction_id` | Metronome docs | accessed 2026-10 |
| Stripe–Metronome acquisition completed | 14 January 2026 | Stripe newsroom | 2026-01-14 |
| Auto Trader average retailer forecourts | 13,942 (FY to 31 Mar 2026) | Auto Trader FY26 results | 2026-05-21 |
| Auto Trader ARPR | £2,995 per month | Auto Trader FY26 results | 2026-05-21 |
| GitHub enterprise audit log retention | 180 days (Git events 7 days) | GitHub docs | accessed 2026-10 |
| EU Data Act application | 12 September 2025 | Reg. (EU) 2023/2854 Art. 50 | 2023 |
| EU Data Act switching notice / transition / retrieval | ≤2 months / ≤30 days / ≥30 days | Reg. (EU) 2023/2854 Art. 25 | 2023 |
| EU Data Act switching charges abolished | From 12 January 2027 | Reg. (EU) 2023/2854 Art. 29 | 2023 |
| FTC breach notification threshold | ≥500 consumers; ≤30 days | FTC | effective 2024-05 |
| FTC Safeguards: leasing threshold for dealers | Leases longer than 90 days | FTC auto-dealer FAQ | 2025-06 |
| Belgium B2B e-invoicing | Mandatory from 1 January 2026 | FPS Finance e-invoice site | 2025–26 |
| UK VAT e-invoicing | Mandatory from 2029 (B2B and B2G) | HM Treasury Budget 2025 | 2025-11-26 |
| EU ViDA cross-border digital reporting | From 1 July 2030 | European Commission | 2025 |
| Microsoft "estimate" threshold for COGS | Tenant uses < ~2% of a deployment | Microsoft Learn | 2024-11-12 |

## Open questions / not verifiable

- **How do European dealer-software vendors (Keyloop, Pinewood, incadea, VWE, mobile.de and AutoScout24 dealer tools) model dealer groups, rooftops and users?** No public documentation was found.
- **Tekion's identity, tenancy and permission model** is not public. Its "unified data foundation" claim cannot be tested.
- **Root cause and containment architecture of the CDK June 2024 incident.** CDK is privately held and published no technical post-mortem. Public dealer groups' SEC 8-K filings about the incident were not retrieved.
- **Cox Bridge ID internals**: whether it supports SCIM, SAML or only OIDC federation, and whether MFA is mandatory. The pages do not say.
- **Amazon Verified Permissions multi-tenant guidance** (per-tenant vs shared policy store): the page could not be read.
- **Auth0 Organizations**: limits on the number of organisations, and any nesting support.
- **ISO/IEC 27001:2022 Annex A control text** (ISO page blocked) and SOC 2 Type 1/2 definitions from an AICPA primary page.
- **Germany e-invoicing dates** from the BMF itself; **Netherlands** domestic B2B e-invoicing plans; whether the **UK** roadmap was published at Budget 2026.
- **Belgian** works-council or CPPT rules on employee-monitoring software (not researched).
- **Real dealer-SaaS pricing structures** beyond Auto Trader (vAuto, VinSolutions, CDK, Keyloop list prices are not public).

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| SaaS Lens: Silo, Pool, and Bridge Models | AWS Well-Architected | 2023 | https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/silo-pool-and-bridge-models.html |
| SaaS Lens (overview) | AWS | 2023 | https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/saas-lens.html |
| SaaS Tenant Isolation Strategies (pool, tier-based, identity) | AWS whitepaper (historical) | 2020 | https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html |
| SaaS Architecture Fundamentals: control plane vs application plane | AWS whitepaper (historical) | 2022 | https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/control-plane-vs.-application-plane.html |
| Multi-tenant data isolation with PostgreSQL Row Level Security | AWS Database Blog, M. Beardsley | 2020 | https://aws.amazon.com/blogs/database/multi-tenant-data-isolation-with-postgresql-row-level-security/ |
| Row Security Policies (PostgreSQL 18 docs) | PostgreSQL Global Development Group | 2026 | https://www.postgresql.org/docs/current/ddl-rowsecurity.html |
| Multi-tenant applications (Citus docs) | Citus Data / Microsoft | n.d. | https://docs.citusdata.com/en/stable/use_cases/multi_tenant.html |
| Tenancy models for a multitenant solution | Microsoft Azure Architecture Center | 2025 | https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenancy-models |
| Noisy Neighbor antipattern | Microsoft Azure Architecture Center | 2025 | https://learn.microsoft.com/en-us/azure/architecture/antipatterns/noisy-neighbor/noisy-neighbor |
| Measure consumption | Microsoft Azure Architecture Center | 2024 | https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/measure-consumption |
| Pricing models for a multitenant solution | Microsoft Azure Architecture Center | 2024 | https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/pricing-models |
| Tenant life cycle considerations | Microsoft Azure Architecture Center | 2025 | https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenant-lifecycle |
| GKE multi-tenancy overview | Google Cloud | 2026 | https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview |
| Baggage (concepts) | OpenTelemetry | n.d. | https://opentelemetry.io/docs/concepts/signals/baggage/ |
| Zanzibar: Google's Consistent, Global Authorization System | R. Pang et al., USENIX ATC | 2019 | https://www.usenix.org/system/files/atc19-pang.pdf |
| Zanzibar publication page | Google Research | 2019 | https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/ |
| OpenFGA documentation | OpenFGA / CNCF | n.d. | https://openfga.dev/docs/fga |
| Cedar: A New Language for Expressive, Fast, Safe, and Analyzable Authorization | J. Cutler et al., arXiv | 2024 | https://arxiv.org/abs/2403.04651 |
| What is Amazon Verified Permissions? | AWS | n.d. | https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html |
| Open Policy Agent documentation | OPA / CNCF | n.d. | https://www.openpolicyagent.org/docs |
| Auth0 Organizations overview | Auth0 (Okta) | n.d. | https://auth0.com/docs/manage-users/organizations/organizations-overview |
| What is Microsoft Entra B2B collaboration? | Microsoft Learn | 2026 | https://learn.microsoft.com/en-us/entra/external-id/what-is-b2b |
| Develop a SCIM endpoint for user provisioning (Entra) | Microsoft Learn | 2026 | https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups |
| RFC 7644: SCIM Protocol Specification | IETF, P. Hunt et al. | 2015 | https://www.rfc-editor.org/rfc/rfc7644.txt |
| OpenID Connect Core 1.0 (errata set 2) | OpenID Foundation | 2023 | https://openid.net/specs/openid-connect-core-1_0.html |
| Bridge ID | Cox Automotive | n.d. | https://www.coxautoinc.com/bridgeid/ |
| Bridge Federation Single Sign On | Cox Automotive | n.d. | https://www.coxautoinc.com/bridge/federation/ |
| CDK Unify | CDK Global | n.d. | https://www.cdkglobal.com/cdk-unify |
| CDK Global introduces enhanced dealer workflow experience (press release, not fetched) | CDK Global via BusinessWire | 2023 | https://www.businesswire.com/news/home/20230123005158/en |
| Tekion home page | Tekion | n.d. | https://tekion.com/ |
| Car dealerships disrupted by multi-day outage after cyberattacks (AP) | Associated Press via ClickOnDetroit | 2024 | https://www.clickondetroit.com/business/2024/06/21/car-dealerships-are-being-disrupted-by-a-multi-day-outage-after-cyberattacks-on-software-supplier/ |
| CDK Global cyber incident | Arctic Wolf | 2024 | https://arcticwolf.com/resources/blog/cdk-global-cyber-incident/ |
| Manage households and groups (Automotive Cloud) | Salesforce Trailhead | n.d. | https://trailhead.salesforce.com/content/learn/modules/stakeholder-modeling-in-automotive-cloud/manage-households-and-groups |
| Platform multitenant architecture | Salesforce Architects | n.d. | https://architect.salesforce.com/fundamentals/platform-multitenant-architecture |
| Exploring domain separation | ServiceNow docs | n.d. | https://www.servicenow.com/docs/r/platform-security/c_DomainSeparation.html |
| Reducing skipped records in ServiceNow upgrades | ServiceNow Community | 2024 | https://www.servicenow.com/community/developer-blog/reducing-skipped-records-in-servicenow-upgrades/ba-p/3102307 |
| Feature Toggles (aka Feature Flags) | P. Hodgson, martinfowler.com | 2017 | https://martinfowler.com/articles/feature-toggles.html |
| Create and configure a meter | Stripe docs | n.d. | https://docs.stripe.com/billing/subscriptions/usage-based/meters/configure |
| Record usage for billing with the API | Stripe docs | n.d. | https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api |
| Record usage for billing (Metronome recommendation) | Stripe docs | n.d. | https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage |
| Idempotent requests | Stripe API reference | n.d. | https://docs.stripe.com/api/idempotent_requests |
| Stripe completes Metronome acquisition | Stripe newsroom | 2026 | https://stripe.com/newsroom/news/stripe-completes-metronome-acquisition |
| Stripe acquires Metronome | PYMNTS | 2025 | https://www.pymnts.com/acquisitions/2025/stripe-acquires-metronome-to-enhance-metered-pricing-capabilities-for-ai-companies |
| Send usage events | Metronome docs | n.d. | https://docs.metronome.com/guides/events/send-usage-events |
| How Metronome works | Metronome docs | n.d. | https://docs.metronome.com/guides/get-started/how-metronome-works |
| Query-based billing | Orb docs | n.d. | https://docs.withorb.com/architecture/query-based-billing |
| IFRS 15 Revenue from Contracts with Customers | IFRS Foundation | 2014 (page n.d.) | https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/ |
| Full year results for the year ended 31 March 2026 | Auto Trader Group plc | 2026 | https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf |
| Regulation (EU) 2023/2854 (Data Act) | EU Publications Office | 2023 | http://publications.europa.eu/resource/celex/32023R2854 |
| Regulation (EU) 2016/679 (GDPR) | EU Publications Office | 2016 | http://publications.europa.eu/resource/celex/32016R0679 |
| e-invoice Belgium | FPS Finance (BOSA/FOD Financiën) | 2025–26 | https://einvoice.belgium.be/en |
| Peppol country profile: Belgium | OpenPeppol | 2025 | https://www.peppol.org/learn-more/country-profiles/belgium/ |
| Germany: guidelines for first phase of e-invoicing mandate | KPMG | 2024 | https://kpmg.com/us/en/taxnewsflash/news/2024/10/tnf-germany-guidelines-for-complying-with-first-phase-of-e-invoicing-mandate.html |
| Budget 2025 | HM Treasury | 2025 | https://www.gov.uk/government/publications/budget-2025-document/budget-2025-html |
| VAT in the Digital Age (ViDA) | European Commission, DG TAXUD | 2025 | https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en |
| Validating CloudTrail log file integrity | AWS | n.d. | https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html |
| About the audit log for your enterprise | GitHub docs | n.d. | https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/about-the-audit-log-for-your-enterprise |
| SP 800-92 Rev. 1 (initial public draft): Cybersecurity Log Management Planning Guide | NIST, K. Scarfone and M. Souppaya | 2023 | https://csrc.nist.gov/pubs/sp/800/92/r1/ipd |
| SOC suite of services | AICPA & CIMA | n.d. | https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services |
| 16 CFR 314.4 Elements (Safeguards Rule) | Cornell LII (eCFR text) | current | https://www.law.cornell.edu/cfr/text/16/314.4 |
| Automobile Dealers and the FTC's Safeguards Rule FAQ | US Federal Trade Commission | 2025 | https://www.ftc.gov/business-guidance/resources/automobile-dealers-ftcs-safeguards-rule-frequently-asked-questions |
| FTC Safeguards Rule: What Your Business Needs to Know | US Federal Trade Commission | n.d. | https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know |
| Betriebsverfassungsgesetz §87 | German Federal Ministry of Justice (gesetze-im-internet.de) | current | https://www.gesetze-im-internet.de/betrvg/__87.html |
| Wet op de ondernemingsraden (Works Councils Act) | Dutch government (wetten.overheid.nl) | current | https://wetten.overheid.nl/BWBR0002747/ |
