# Research brief: Uber's pre-AI developer platform foundations

Compiled 20 Oct 2026 for the `uber-ai-infra` journal. The thesis it supports: Uber's AI tooling was fast to build because it sits on a decade of developer-platform investment.

The starting point is the Pragmatic Engineer podcast "Uber's AI infra, from the inside" (Gergely Orosz with Uday Kiran Medisetty, 14 Oct 2026). Below, **[podcast]** marks a claim that appears only in the podcast notes (`_input/pragmatic-engineer-podcast/page.txt`). **[confirmed]** marks a claim that an independent fetched source also supports. Every URL in the Sources list was fetched on 20 Oct 2026, except where a note says otherwise. Paywalled Pragmatic Engineer pieces could only be read up to the paywall.

Uday Kiran Medisetty is a co-author of two primary sources below: the Edge Gateway post (2020) and the NSDI '26 failover paper. That makes them strong corroboration for what he says in the podcast.

---

## 1. Microservices: from 2 services to thousands, DOMA, and later consolidation

### Service-count timeline (sources disagree; the definitions differ)

| When | Count | Source | Note |
| --- | --- | --- | --- |
| 2014 | 2 services, `dispatch` and `api` | Edge Gateway blog (2020) | The podcast says "two services in 2015, when Uday joined". It is consistent in spirit, but the blog dates the two-service architecture to 2014 and says a new gateway was bootstrapped in January 2015. |
| Fall 2015 | ~500 microservices | Jaeger blog (Feb 2017) | |
| Jul 2016 | "hundreds of microservices" | Tech Stack Part I (2016) | |
| 2016 | ~5,000 | PE "Scaling Uber with Thuan Pham" (Apr 2026) | Conflicts with Uber's own 2016–17 figures. Treat it as a loose recollection. |
| Early 2017 | 2,000+ | Jaeger blog | |
| 2017 | 4,000+ services, thousands of repos | Devpod blog (Dec 2022) | A retrospective figure |
| 2019 | 2,200+ microservices | Edge Gateway blog | |
| Jul 2020 | ~2,200 *critical* microservices in 70 domains | DOMA blog | "Critical" is a subset |
| Sep 2023 | ~4,500 *stateless* microservices | Up blog | Matches the podcast's ~4,500 |
| 2025 | ~4,000 services on ~3M cores | Kubernetes migration blog (Apr 2025) | |
| 2025–26 | **over 6,000 microservices in over 16,000 environments** (prod, staging, canary…) | UFA paper, NSDI '26 (Uday is a co-author) | The largest figure. It probably counts all services, stateful included, not only the stateless fleet. |
| 2026 | ~4,500 | PE Thuan Pham episode; podcast (~4,500–5,000) | |

**Contradiction to flag in the journal.** The podcast says "in 2026 there will be about the same number of services as in 2019, though the business is ~10x larger." Uber's own 2019 figure is 2,200+, not ~4,500. The "same as 2019" claim only holds if one uses the higher retrospective counts (4,000+ in 2017, ~5,000 in 2016). The NSDI '26 paper gives more than 6,000 in 2025–26. The safest wording: "the count grew to several thousand by 2017 and has stayed in the 4,000–6,000 band since, depending on what is counted." That is a plateau rather than continued growth. **[podcast for the plateau framing; the numbers are confirmed, but they conflict]**

### DOMA (Domain-Oriented Microservice Architecture)
- Introduced on the Uber blog on 23 Jul 2020 by Adam Gluck. It groups ~2,200 critical microservices into **70 domains**; about 50% were implemented when the post was written. **[confirmed]**
- **Five layers:** Infrastructure, Business, Product, Presentation and Edge. A layer may depend only on the layers below it. Each domain exposes a single **gateway**. There are two extension models: logic extensions (plugin- or interface-style) and data extensions (Protobuf `Any`). **[confirmed]**
- Motivating pains: one root-cause investigation crossed ~50 services owned by 12 teams. Uber estimated the **microservice half-life at 1.5 years**. **[confirmed]**
- Results: platform support costs often fell by an order of magnitude. One team cut feature integration from 3 days to 3 hours. Onboarding time fell by 25–50%. Two of the largest platform rewrites happened behind gateways. **[confirmed]**
- Nearly 60 engineers contributed to the effort. **[confirmed]**

### Monolith decomposition
- The first monolith was Python on a single PostgreSQL database (Up blog, 2023). It was called "API" (Thuan Pham episode). The rule was that anything new is built outside the monolith. Decomposition took "a good two years," with an "ugly middle phase" in which the monolith still grew. **[confirmed by PE/Thuan, not by an Uber blog]**

### Languages (Go/Java standardization)
- In Jul 2016, Uber's Tech Stack Part I named **Python, Node.js, Go and Java** as the main service languages. Thrift was the IDL (Protobuf was also mentioned), alongside TChannel, Ringpop and Hyperbahn. **[confirmed]**
- Uber now runs "one monorepo per core language" (2025 rollout blog), with six major monorepos and seven languages (2025 CI blog). **[confirmed]**
- I found **no official Uber post declaring Go and Java the standard backend languages**. The evidence is indirect. The Node.js RTAPI gateway was replaced by a Go service (Edge Gateway, 2020). Marketplace posts describe rewriting Python in Go. Go and Java are the backend monorepos that receive the large platform investment. **[gap: the standardization is inferred]**

### Organisation: the Program/Platform split (2014)
- In spring 2014, CPO Jeff Holden emailed the team to launch "Programs & Platforms". Uber had over 100 engineers, 10 PMs and 15 designers. The reorg created **16 program teams and 11 platform teams** all at once. Programs were ~60–70% of engineering; platforms ~30–40%. Developer Platform owned CI/CD and developer experience. Teams were reviewed quarterly. (PE, 6 Sep 2021) **[confirmed]**
- This is the structural root of the thesis: a dedicated developer-platform organisation has existed since 2014.

---

## 2. Monorepos, Bazel, SubmitQueue, and CI scale

- **Before the monorepos:** in 2017 the code lived in "thousands of repositories with 10+ programming languages, 4000+ services, 500+ Web Apps, 9+ build tools and 6+ configuration tools" (Devpod blog). Gautam Korlam describes "hundreds of repos" for the Rider, Driver and Eats apps. iOS moved to a monorepo first, then Android. **[confirmed]**
- **Go monorepo:** launched in **early 2018**. Monthly commits grew from <100 to ~10,000; monthly active developers from <10 to ~900. It held 70,000+ files and 1,000+ external modules by May 2020, and is "likely one of the largest Go repositories on Bazel". Uber engineers were the #2 and #3 contributors to Gazelle (April 2020). Uber also contributed the Bazel feature that reads target lists from a file (Bazel 3.1). (Zhongpeng Lin, 13 May 2020) **[confirmed]**
- **Java monorepo:** it used Buck until 2023 and is now entirely on Bazel. Services run Java 17 and 21, with Java 25 under way. (Pavel Belousov talk, Amsterdam, Nov 2025; this comes from a third-party recap, so it is **secondary**.) The JUnit migration blog (Apr 2026) confirms a Bazel Java monorepo with **600,000+ JUnit 4 tests across ~15M lines of code**. **[confirmed]**
- **Largest monorepo:** "over 70 million lines of code" (Devpod blog, 2022). **[confirmed]**
- **SubmitQueue**, from "Keeping Master Green at Scale" (Ananthanarayanan, Saeida Ardekani, Haenikel, Varadarajan, Soriano, Patel, Adl-Tabatabai; EuroSys 2019, art. 29). Details are taken from The Morning Paper summary because the paper PDF was not fetched:
  - Before SubmitQueue, the iOS mainline was green only **52%** of the time in a one-week sample. Afterwards it stayed green at all times, and had been in production for over a year at publication.
  - A speculation engine builds a probabilistic tree of possible future HEAD states and runs the likely builds in parallel. Two changes conflict when they touch a shared Bazel or Buck build target.
  - A logistic-regression success predictor uses ~100 features and reaches 97% accuracy. Turnaround is within 1.2x of an oracle. **[confirmed]**
- **CI scale in 2025** ("Slashing CI Costs at Uber", 23 Jun 2025):
  - 4,500+ engineers use SubmitQueue daily, landing tens of thousands of changes per month across "hundreds of millions of lines of code across six major monorepos and seven programming languages".
  - Uber runs hundreds of thousands of deployments and millions of config changes per month.
  - A new prioritisation model (NGBoost build-time prediction), rolled out in 2024, cut CI resource use by **53%** and wait times by **37%**. The earlier design's early-termination policy had affected 40–65% of builds.
  - The follow-up paper is arXiv 2501.03440. An open-source `uber/submitqueue` repository exists. **[confirmed]**
- **Monorepo blast radius** (Aug 2025): across 500,000 Go-monorepo commits, **1.4% touched more than 100 services and 0.3% touched more than 1,000**. A tiered (T0–T5) cross-service deployment gate rolls large commits out tier by tier within 24 hours. **[confirmed]**
- Podcast tie-in: Bazel is cited in the "Testing and code review with Bazel, Slate, and Capri" segment. **[podcast]**

---

## 3. DevPods (remote development environments)

- Blog: "Devpod: Improving Developer Productivity at Uber with Remote Development", 13 Dec 2022, by Strukčinskas, Badem and Jokubauskas. **[confirmed]**
- Each Devpod is a container on **Kubernetes**, on clusters outside production. A **Devpod Operator** (CRDs plus a custom controller) translates high-level descriptions into Kubernetes primitives. Idle pods are snapshotted through VolumeSnapshotContents and PVCs. Images use Debian, to match production. Pods get up to **48 cores / 96 GB RAM**. They run in five regions: Oregon, Virginia, Netherlands, Mumbai and São Paulo. **[confirmed]**
- Go builds run 2.5x faster at p95 and 1.8x faster at p75 than on laptops. p95 `git status` stays under 4 s on the largest monorepo. Provisioning takes 2–3 minutes, with a goal of under 3 s. **[confirmed]**
- Supported IDEs: VS Code (remote and web), JetBrains Gateway over SSH, Projector (deprecated), and vim/emacs. **[confirmed]**
- More than **60% of engineers** were using Devpods by Nov 2022, out of a developer platform serving ~5,000 core engineers. **[confirmed]**
- Gautam Korlam (PE, 12 Mar 2025) describes DevPods as cloud environments that hold the code, build artifacts and IDE indices. **[confirmed]**
- **Possible contradiction:** the podcast notes say "Minion – built in 2025 – is powered by DevPods, which Uber created in 2017." The Uber blog uses 2017 as the *problem baseline* (the fragmented repos), not as Devpod's start date. Its narrative implies Devpod followed the monorepo move, which began in 2018. I found no public source dating Devpod to 2017. Better wording: "DevPods grew out of the post-2017 monorepo push and were mainstream by 2022." **[podcast date unverified]**

---

## 4. Ownership: uOwn

- The podcast says uOwn "shows who owns a service or asset. Back in 2015, no such vendor existed." **[podcast only]**
- **Gap:** I found no public Uber blog post, talk or paper about uOwn. Indirect support: the UFA paper's tiering (T0–T5 criticality per service) and the 2025 rollout blog both assume per-service metadata (tier and owner) is available platform-wide.

---

## 5. Observability: Jaeger tracing and M3 metrics

### Jaeger
- "Evolving Distributed Tracing at Uber Engineering", 2 Feb 2017, by Yuri Shkuro. **[confirmed]**
  - The first tracer, **Merckx**, worked only inside the Python monolith; Tornado broke its thread-local context. **TChannel** (2015) built trace fields (trace ID, span ID, parent ID, flags) into its binary protocol.
  - A two-engineer Distributed Tracing team sat inside the NYC Observability group, which started in early 2015.
  - In 2016, Jaeger ran in hundreds of microservices and recorded thousands of traces per second. It used a host-local `jaeger-agent` over UDP and adaptive sampling pulled from the backend. Clients existed for Go, Java, Python and Node.js.
  - Jaeger was open-sourced in Apr 2017, became a CNCF incubation project in Sep 2017, and graduated in Oct 2019.
- **Baggage / context propagation:** the 2017 post describes "distributed context propagation" but never uses the word "baggage". Shkuro's 2019 Medium essay "Embracing context propagation" (medium.com/jaegertracing/embracing-context-propagation-7100b9b6029a) returned HTTP 403 and **could not be verified**. **[gap]**
- Podcast tie-in: "Jaeger tracing made Slate routing and Context graph easier." **[podcast]**

### M3 / M3DB
- "M3: Uber's Open Source, Large-scale Metrics Platform for Prometheus", 7 Aug 2018, by Rob Skillington. **[confirmed]**
  - M3 aggregates **500 million metrics per second** and persists 20 million per second. It holds 6.6 billion time series and writes each value to 3 replicas per region by quorum.
  - The predecessor was Graphite (Carbon/Whisper) in late 2014, which had no replication. M3 shipped in 2015 on Cassandra, which Uber later replaced with M3DB.
  - The 500M/s figure matches the podcast. **[confirmed]**
- PE "How Uber Built its Observability Platform", 12 Sep 2023, narrated by Martin Mao (paywalled after the intro):
  - In 2015 the stack was Graphite + Carbon + WhisperDB. It was not horizontally scalable, and adding capacity took a week offline.
  - M3 handled **600 million data points per second** in 2018. Mao went on to co-found Chronosphere. **[confirmed]**
  - Note: 500M/s (Uber blog, metrics aggregated) and 600M/s (Mao, data points) are different measures from the same year. Use 500M/s when quoting the podcast.

---

## 6. Cadence workflow engine (and the Temporal lineage)

- "Announcing Cadence 1.0", 22 Jun 2023, by Ender Demirkaya: **[confirmed]**
  - Cadence is a "6+ year project".
  - It runs over 12 billion executions and 270 billion actions per month at Uber, across 1,000+ services from T0 to T5, with 99.9% availability.
  - External users include DoorDash, HashiCorp and Coinbase.
- **Lineage:** Temporal's "Who We Are" page says Maxim Fateev and Samar Abbas co-created Cadence at Uber, and that it grew to ~100 internal use cases in 3 years. Fateev had led AWS Simple Workflow; Abbas had worked on SWF and Azure Durable Task. Temporal was founded in 2019. **[confirmed]**
  - Start dates differ: Temporal says 2015, while Abbas has said ~2017 in an interview. Cadence 1.0 being "6+ years" in mid-2023 points to ~2017. **[sources conflict]**
- Podcast: Cadence was built for multi-day flows such as driver onboarding, and Temporal was built on the open-sourced Cadence. **[podcast; the lineage is confirmed]**

---

## 7. Experimentation (Morpheus → XP) and Flipr configuration

### Flipr
- "Flipr: Making Changes Quickly and Safely at Scale", 12 Apr 2021, by Andy Maule. **[confirmed]**
  - **350K+ active properties**, ~150K changes per week, 700+ client services on 50K+ hosts, ~3M QPS.
  - Each property is a *multimap*: its value depends on runtime context. Override rules ("exceptions/constraints") can key on geography, **city ID**, user, driver or vehicle ID, device, app version, time and experiment treatment.
  - Rollouts expand from a few users in one city, to beta testers in a city, to several cities, to everyone, which limits the blast radius. Monitoring can trigger automatic rollback.

### Morpheus → new XP platform
- "Supercharging A/B Testing at Uber", 21 Jul 2022, by Puttaswamy, Duncan and Arun Babu. **[confirmed]**
  - **Morpheus** was built "7+ years ago" (~2015) for both feature flags and A/B tests. A 2020 review found that a large share of experiments had fatal problems.
  - Treatment groups were hard-coded in client code, so an experiment change could require a release costing 2–4 weeks. Clients failed closed when the backend did not respond.
  - The new platform was built as an **overriding layer on Flipr**, unifying mobile, backend and experiment configuration. Over 50,000 stale Morpheus experiments were deprecated.
  - The migration covered 2,000+ developers, 15+ partner systems, 10+ apps and 350+ services. Logging handles more than 1M messages per second.
- **Switchback experiments:** the 2022 post does not mention them. I found no Uber-authored source; there are only academic papers (Bojinov, Simchi-Levi and Zhao, arXiv 2009.00148) and secondary claims of 90-minute switchback windows at Uber. **[gap]**

---

## 8. Large-scale code change tooling: Piranha, Shepherd, OpenRewrite

- **Piranha**, from "Introducing Piranha", 17 Mar 2020, by Sridharan, Barik and Clapp (architect: Murali Krishna Ramanathan). **[confirmed]**
  - It parses ASTs, deletes the code behind stale feature flags and opens a diff assigned to the flag's author. A weekly pipeline queries the flag system for stale flags (e.g. untouched for ~8 weeks), and the reminder bot PiranhaTidy nudges authors.
  - Generating a diff takes under 3 minutes. Piranha had removed ~2,000 stale flags across Android and iOS.
  - Implementations: Java on Error Prone, Swift on SwiftSyntax, and Objective-C as a Clang plugin. A paper appeared at ICSE-SEIP '20.
- **Shepherd** is named publicly in "How Uber Executed A JUnit Migration at Massive Scale" (7 Apr 2026, Mishra and Vejju). It is "an internal tool for large-scale code changes" that ran the migration across thousands of Bazel targets. A "code-change campaign" script applied the recipe, built and tested each target, and Shepherd generated the diffs, which went through normal CI. **[confirmed by name; no dedicated Shepherd post was found]**
- **OpenRewrite:** the same JUnit post covers it.
  - Uber used Moderne's OpenRewrite with a custom Bazel aspect for sources and classpath, packaged as the `JUnit4to5Migration` recipe.
  - It migrated **75,000+ test classes and 1.25M+ lines in 4 months**, producing 5,000+ diffs.
  - GenAI failed at multi-file migration and was used only to debug failures.
  - A Nov 2025 talk recap adds that OpenRewrite was used for Spring Boot 2→3, and that an in-house dependency-update bot was chosen over Renovate or Dependabot. **[confirmed; the recap is secondary]**
- Podcast tie-in: Shepherd appears in the "Edge Gateway, Shepherd, and Wisdom" segment. **[podcast]**

---

## 9. Cities as a first-class concept; region pinning and failover

- **Region pinning is confirmed** by "Uber's Failover Architecture" (UFA), NSDI '26. Its 24 authors include Uday Kiran Medisetty and Albert Greenberg.
  - "During normal operations (steady state), each city's traffic is routed to exactly one region." There are two primary regions, **DCA and PHX**, running active-active, each with zones both on-prem and in the cloud.
  - The **Outage Mitigator (OMG)** tool orchestrates region-to-region *city migrations* during failovers.
  - Previously every service was provisioned at 2x to absorb a full regional failover. UFA cut this to **1.3x**, raising utilisation from ~20% to ~30% at 99.97% availability. It removed over **1M of ~4M CPU cores** and hardened 4,000+ unsafe "fail-close" dependencies.
  - Full-peak failovers happen less than 20 hours per year. The fleet handles ~62 trillion RPCs per week. Up orchestrates ~700K deployments per week. Compute launches over 1M pods per day. A canary zone takes 2% of regional traffic. **[confirmed]**
- **Cities in the platform primitives:**
  - Flipr constraints key on city ID, and rollouts proceed city by city (2021). **[confirmed]**
  - Tech Stack Part I (2016) reports "300 operational cities as of April 2015" and says every data center handled live trips, with failover between them. **[confirmed]**
  - Sharding databases by city in the early days. **[podcast only]**
- Kafka active/active and active/passive multi-region consumption is described on the Uber Kafka blog (search result only, **not fetched**).

---

## 10. Cloud migration (bare metal → OCI and GCP)

- **Data-center history** (PE "Inside Uber's move to the Cloud" Part 1, 7 Mar 2023):
  - ~2013: Peak Hosting, on "about a dozen Dell PowerEdge servers".
  - 2014: first own data center, SJC, then DCA.
  - ~2019: PHX was built to replace SJC.
  - The multi-zone/multi-region push began ~2017. At the time Uber had "two regions and around 10 zones". **[confirmed]**
- **Deals:** on 13 Feb 2023 Uber signed **seven-year agreements with Oracle Cloud Infrastructure and Google Cloud** (CEO Dara Khosrowshahi per news coverage; the Up blog confirms the date). Uber said it would retire most of its on-prem data centers within a few years. PE notes it will not be 100% cloud. **[confirmed]**
- **Crane** ("Crane: Uber's Next-Gen Infrastructure Stack", 15 Sep 2022): **[confirmed]**
  - Started from the 2018 situation and aimed at a fleet of 100,000+ servers.
  - Zone turn-up went from "dozens of engineers, 6+ months" to a record of **3 days**; a cloud test zone spins up in about an hour.
  - Five production zones had been built with the new tooling.
  - It is cloud-agnostic by design. PE describes it as "a 5-year project".
- **Up** ("Up: Portable Microservices Ready for the Cloud", 7 Sep 2023): **[confirmed]**
  - Up started in 2018, had a prototype in early 2019 and reached GA in mid-2020.
  - Over 4,000 services and ~2M cores were migrated over two years, finishing in 2022.
  - ~4,500 stateless services are deployed 100K+ times a week by 4,000 engineers.
  - Every service is moved between zones every few weeks to prove portability.
- **Kubernetes** ("Migrating Uber's Compute Platform to Kubernetes", 24 Apr 2025): **[confirmed]**
  - Mesos → Kubernetes was completed in 2024 (shared stateless services 100% done by Jul 2024), with a peak of ~300K cores migrated in a week.
  - There are 50+ clusters across on-prem, **Oracle Cloud and Google Cloud**, each with ~5,000–7,500 hosts. ~4,000 services use ~3M cores.
  - Services deploy ~100K times a day, producing ~1.5M pod launches a day.

---

## 11. Edge Gateway (successor to RTAPI)

- "Designing Edge Gateway, Uber's API Lifecycle Management Platform", 18 Aug 2020, by Pavel Astakhov, Madan Thangavelu and **Uday Kiran Medisetty**. **[confirmed]**
  - **Gen 1 (2014):** `dispatch` plus `api`, using a `messageType` field and ~15 RPC commands. In January 2015 a new gateway was bootstrapped; its first REST API (destination search) served a few thousand QPS.
  - **Gen 2, RTAPI (Real-Time API, 2015→):** one of Uber's largest Node.js apps. It had 110 endpoint groupings, **800K req/s at peak**, ~1M lines of code, 400+ downstream services owned by 100+ teams, 40+ independently deployed services, 2,500 npm libraries and 50,000 integration tests per diff. 40% of engineering had committed to it. Its pains: a dynamic language across 1,500 engineers, null-pointer errors, business logic leaking into the gateway, and the gateway team becoming a bottleneck.
  - **Gen 3, Edge Gateway:** a standalone **Go** service with a configuration UI, layered as Edge / Presentation / Product / Domain, with no business logic at the edge. It is built on the **Glue** framework (on Fx) and **CFF**, a Go DAG orchestration library.
  - The migration took ~2 years. Latency improved and requests per core rose.
- The NSDI '26 paper's architecture figure still shows the traffic path "Frontend → Edge Gateway → Microservices" (2025–26). **[confirmed]**

---

## 12. Developer experience as a measured function

- Gautam Korlam (PE, 12 Mar 2025) was Android engineer #9 (joined 2014). Early Uber had about one commit per minute and 10–30 minute CI runs. The 2016 app rewrite made builds very long. **Developer-tooling NPS went from −50 to +8** over his tenure. **[confirmed]**
- Thrift and Protobuf registries made the MCP Gateway fast to build. **[podcast only]** Thrift as Uber's IDL since at least 2016 is **[confirmed]** (Tech Stack Part I).

---

## Gaps and open items

1. **uOwn:** no public source. Attribute it to the podcast.
2. **DevPods "created in 2017":** unverified, and probably conflated with the 2017 monorepo baseline.
3. **Service counts:** the podcast's "same as 2019" conflicts with Uber's 2,200+ (2019) and with NSDI '26's 6,000+. State the range and the counting caveat.
4. **Jaeger baggage:** the primary essay was blocked (403). Only generic "context propagation" is confirmed.
5. **Switchback experiments:** no Uber-authored public source was found.
6. **Go/Java standardization:** no explicit policy post. It is inferred from the monorepos and rewrites.
7. **Shepherd:** confirmed by name only. No architecture post exists.
8. **SubmitQueue paper:** details come from The Morning Paper summary. The PDF itself (ACM DL, EuroSys '19) was not fetched.
9. **Paywalled PE pieces** (cloud Part 2, observability, Developer Experience transcript) were read only up to the paywall.

---

## Sources

All accessed 20 Oct 2026.

1. Pragmatic Engineer, "Uber's AI infra, from the inside" (G. Orosz with U. K. Medisetty), 14 Oct 2026. https://newsletter.pragmaticengineer.com/p/ubers-ai-infra-from-the-inside (local copy: `_input/pragmatic-engineer-podcast/page.txt`)
2. A. Gluck, "Introducing Domain-Oriented Microservice Architecture", Uber Blog, 23 Jul 2020. https://www.uber.com/blog/microservice-architecture/
3. P. Astakhov, M. Thangavelu, U. K. Medisetty, "Designing Edge Gateway, Uber's API Lifecycle Management Platform", Uber Blog, 18 Aug 2020. https://www.uber.com/blog/gatewayuberapi/
4. M. A. Strukčinskas, S. Badem, A. Jokubauskas, "Devpod: Improving Developer Productivity at Uber with Remote Development", Uber Blog, 13 Dec 2022. https://www.uber.com/blog/devpod-improving-developer-productivity-at-uber/
5. Z. Lin, "Building Uber's Go Monorepo with Bazel", Uber Blog, 13 May 2020. https://www.uber.com/blog/go-monorepo-bazel/
6. Z. Lin, D. Juloori, M. Williams, "Slashing CI Costs at Uber", Uber Blog, 23 Jun 2025. https://www.uber.com/blog/slashing-ci-costs-at-uber/
7. S. Ananthanarayanan et al., "Keeping Master Green at Scale", EuroSys 2019. Summary by A. Colyer, The Morning Paper, Apr 2019: https://blog.acolyer.org/2019/04/18/keeping-master-green-at-scale/ (follow-up: arXiv 2501.03440, https://arxiv.org/abs/2501.03440, not fetched; repository: https://github.com/uber/submitqueue, not fetched)
8. A. Lorincz, G. Alvarez, R. Vestergaard, "Controlling the Rollout of Large-Scale Monorepo Changes", Uber Blog, 28 Aug 2025. https://www.uber.com/blog/controlling-the-rollout-of-large-scale-monorepo-changes/ (InfoQ coverage, 10 Sep 2025: https://www.infoq.com/news/2025/09/uber-monorepo-deployment/)
9. A. Mishra, K. Vejju, "How Uber Executed A JUnit Migration at Massive Scale", Uber Blog, 7 Apr 2026. https://www.uber.com/us/en/blog/junit-migration/
10. L. Berton, recap of "Friends of OpenJDK" at Uber Amsterdam (P. Belousov talk), 11 Nov 2025 (secondary). https://lucaberton.com/blog/friends-of-openjdk-uber-amsterdam-2025/
11. Y. Shkuro, "Evolving Distributed Tracing at Uber Engineering", Uber Blog, 2 Feb 2017. https://www.uber.com/blog/distributed-tracing/
12. R. Skillington, "M3: Uber's Open Source, Large-scale Metrics Platform for Prometheus", Uber Blog, 7 Aug 2018. https://www.uber.com/blog/m3/
13. G. Orosz (with M. Mao), "How Uber Built its Observability Platform", The Pragmatic Engineer, 12 Sep 2023 (paywalled). https://newsletter.pragmaticengineer.com/p/how-uber-built-its-observability-platform
14. E. Demirkaya, "Announcing Cadence 1.0", Uber Blog, 22 Jun 2023. https://www.uber.com/blog/announcing-cadence/
15. Temporal, "Who We Are". https://temporal.io/about (seen through search results only, not fetched directly)
16. A. Maule, "Flipr: Making Changes Quickly and Safely at Scale", Uber Blog, 12 Apr 2021. https://www.uber.com/blog/flipr/
17. K. Puttaswamy, L. Duncan, Arun Babu A S P, "Supercharging A/B Testing at Uber", Uber Blog, 21 Jul 2022. https://www.uber.com/blog/supercharging-a-b-testing-at-uber/
18. M. Sridharan, R. Barik, L. Clapp, "Introducing Piranha: An Open Source Tool to Automatically Delete Stale Code", Uber Blog, 17 Mar 2020. https://www.uber.com/blog/piranha/
19. M. Bansal, M. Chabbi, … A. Greenberg, U. K. Medisetty, "Uber's Failover Architecture: Reconciling Reliability and Efficiency in Hyperscale Microservice Infrastructure", USENIX NSDI '26. https://www.cs.ubc.ca/~bestchai/papers/nsdi26-ufa2.pdf
20. K. Nusbaum, T. Miller, B. Siravara, "Crane: Uber's Next-Gen Infrastructure Stack", Uber Blog, 15 Sep 2022. https://www.uber.com/blog/crane-ubers-next-gen-infrastructure-stack/
21. M. Schwarz, A. Neverov, "Up: Portable Microservices Ready for the Cloud", Uber Blog, 7 Sep 2023. https://www.uber.com/blog/up-portable-microservices-ready-for-the-cloud/
22. A. Bhave, A. Krishnan, "Migrating Uber's Compute Platform to Kubernetes: A Technical Journey", Uber Blog, 24 Apr 2025. https://www.uber.com/blog/migrating-ubers-compute-platform-to-kubernetes-a-technical-journey/
23. G. Orosz, "Inside Uber's move to the Cloud: Part 1", The Pragmatic Engineer, 7 Mar 2023. https://newsletter.pragmaticengineer.com/p/uber-move-to-cloud (Part 2, 9 Mar 2023, paywalled: https://newsletter.pragmaticengineer.com/p/inside-ubers-move-to-the-cloud-part)
24. G. Orosz, "The Platform and Program Split at Uber", The Pragmatic Engineer, 6 Sep 2021. https://newsletter.pragmaticengineer.com/p/program-platform-split-uber
25. Pragmatic Engineer podcast, "Scaling Uber with Thuan Pham (Uber's first CTO)", 1 Apr 2026. https://newsletter.pragmaticengineer.com/p/scaling-uber-with-thuan-pham-ubers
26. Pragmatic Engineer podcast, "Developer Experience at Uber with Gautam Korlam", 12 Mar 2025. https://newsletter.pragmaticengineer.com/p/developer-experience-at-uber
27. L. Lozinski, "The Uber Engineering Tech Stack, Part I: The Foundation", Uber Blog, 19 Jul 2016. https://www.uber.com/blog/tech-stack-part-one-foundation/
