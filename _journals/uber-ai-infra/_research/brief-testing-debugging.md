# Research brief: Uber testing, validation, debugging and observability — the public record

Compiled 20 Oct 2026 for the `uber-ai-infra` journal. Starting point: Pragmatic Engineer podcast "Uber's AI infra, from the inside" (14 Oct 2026, Uday Kiran Medisetty). Transcript at `_input/pragmatic-engineer-podcast/transcript.txt`.

Every URL in "Sources" was fetched on 20 Oct 2026 unless marked otherwise. Labels used:

- **CONFIRMED**: an Uber primary source (blog, talk abstract) states it.
- **PARTLY CONFIRMED**: the mechanism is public but the podcast's name or detail is not.
- **PODCAST-ONLY**: no public source found.

---

## 1. Slate (SLATE: Short-Lived Application Testing Environment)

**Primary source:** "Simplifying Developer Testing Through SLATE", Uber blog, 20 Oct 2022, by Ankit Srivastava, Alok Srivastava and Rohan Rathi.

- The acronym is **S**hort-**L**ived **A**pplication **T**esting **E**nvironment. It is an on-demand, ephemeral environment *inside production*. Services deployed into it are called *services under test* (SUTs).
- A developer can have several SLATE environments at once and can deploy from git branches or refs. Each SLATE holds one version and one instance of a given service, and a new deployment replaces the old one.
- **Default TTL is 2 days.** When it expires, deployments are terminated and resources are freed.
- **Routing:** test tenancy travels as **Jaeger baggage** under the key `request-tenancy`, with the value `uber/test/slate/<name>` (for example `uber/test/slate/SLATE1`). All requests have production tenancy by default.
- **Routing overrides:** on SUT deploy, a tenancy-to-routing-info mapping goes into `config-cache`. **Edge Gateway** looks up the mapping and injects a `routing-overrides` key into the request baggage. A **host-routing-agent** then sends the request to the SUT instead of production. The post says services need no routing logic of their own.
- **Test accounts:** the Test-Accounts service creates test riders, drivers and profiles. Trips and orders those users create are test entities too. Developers *associate test users with an environment*, and only those users' requests reach the SUTs. This is the public form of the podcast's "pin test-account UUIDs".
- **Clients:** user association makes testing from mobile apps possible. cURL and scripts also work.
- **Dependencies:** SUTs call production instances of their dependencies by default. Services that need stronger isolation declare isolated resources in `slate.yaml`.
- The post does not mention Cerberus, Deputy or agents.

**Related primary source:** "Shifting E2E Testing Left at Uber" (Aug 2024, see section 2) calls SLATE "a sister project built on BITS primitives" for manual sanity testing.

**Podcast claims checked:**

| Podcast claim | Status |
| --- | --- |
| Personal, short-lived instances; deploy your branch | CONFIRMED (2022 post) |
| Pin test-account UUIDs to an instance | CONFIRMED as "associate test users"; "UUID pinning" wording is podcast-only |
| Routing via Jaeger trace baggage through the service mesh | CONFIRMED (baggage key `request-tenancy`; host-routing-agent; Edge Gateway injects overrides) |
| Multi-service tests (two or three SUTs) | CONFIRMED (SUTs across multiple services) |
| Covers iOS/Android/web/backend | PARTLY CONFIRMED: mobile and scripts in 2022; web via agent browser is podcast-only |
| Agents create Slate envs via MCP/CLI ("slate mcp"), run agent-browser A/B (main vs branch), attach before/after reports, screenshots, videos to PRs | PODCAST-ONLY in Uber's own words. Secondary summaries (Dealroom, ZenML) say Minion "self-validates using Slate environments, an agent browser and staging deploys". Uber's 27 Aug 2026 "Running a Software Factory Efficiently" post mentions only "completing E2E PRs with visual validation" and does not name Slate. |
| "Slate took years to build"; retrofitting all services for context propagation took years | Consistent with the 2020 multitenancy post and 2022 SLATE post (multi-year arc). No public figure. |

**Small contradiction:** the podcast says Jaeger was built "back in maybe 2017-18". The 2017 Jaeger post (section 6) dates the work to 2015–2016 and internal adoption to 2016. Jaeger was open-sourced in April 2017.

---

## 2. BITS (Backend Integration Testing Strategy) and test sandboxes

**Primary source:** "Shifting E2E Testing Left at Uber", Uber blog, 22 Aug 2024, byline "Uber" (no named authors).

- **BITS** is a company-wide initiative for on-demand deployment and routing to **test sandboxes**, so commits can be tested before they land.
- **Scale:** it gates changes to **1,000+ core backend services** and runs several thousand E2E tests, with an average pass rate above 90% per attempt.
- **Data isolation:** most APIs are entity-scoped, so test users limit side effects. Cross-entity flows use tenancy tags, which either route to a separate datastore or filter a shared production DB by a tenancy column.
- **Infrastructure isolation:**
  - Sandboxes receive no production traffic.
  - A Kafka consumer proxy routes messages to sandboxes.
  - Cadence workflows are sandbox-scoped.
  - Metrics and logs are tagged so they can be filtered.
  - SPIFFE/SPIRE gives sandboxes their identities.
  - **Routing overrides travel as OpenTelemetry context baggage.** The 2022 SLATE post says *Jaeger* baggage, so this suggests a migration from Jaeger clients to OpenTelemetry.
- **Cadence** orchestrates CI, provisioning and test scheduling.
- **Configuration:** configuration changes cause **up to 30% of incidents**. BITS also tests rollouts from **Flipr**, Uber's config system.
- **Trace indexing:** every test is force-sampled with Jaeger. The indexes map which services each test covers and which tests cover each service. Uber uses them for endpoint coverage and for selecting tests when a service changes.
- **Composable Testing Framework (CTF):** a code-level DSL for composing actions against centralized trip state. It was originally built for the Fulfillment re-architecture.
- **Reliability practices:**
  - Retries raise the signal to 99.9%.
  - **Placebo runs** execute each test against a sandbox on the latest main, producing a truth table: production broke, the test broke, or a real defect.
  - Tests that drop below a 90% placebo pass rate are auto-quarantined as non-blocking, and a ticket goes to the owning team.
  - The largest service has 300 tests.
- **Result:** incidents per 1,000 diffs fell **71% in 2023**.
- It does not mention capture/replay, Cerberus or Deputy.

**Journal relevance:** the podcast's "agent runs main vs branch" A/B is the same move as BITS placebo runs (test the baseline to separate real regressions from noise).

---

## 3. Multitenancy and test tenancy (the foundation)

**Primary source:** "Why We Leverage Multi-tenancy in Uber's Microservice Architecture", Uber blog, 11 Mar 2020, Amit Gud (Infrastructure). A related USENIX ;login: article by Gud (Winter 2019) surfaced in search but was not fetched.

- **Tenancy** covers tests, canaries, shadow systems, service tiers and product lines. It applies to data in flight (requests, queue messages) and data at rest (storage, caches).
- **Context:** tenancy is attached at the **edge gateway**, kept for the request's lifetime and passed downstream. The example is `"request-tenancy": "product-foo/testing/TID1234"`. The post names OpenTracing/Jaeger for propagation and Kafka message headers for queues.
- **Routing** can happen at egress (service discovery) or at ingress (a sidecar inspects tenancy). The post suggests Envoy or Istio. A `services_under_test` field in the context directs test traffic to a test build. This is the conceptual ancestor of SLATE.
- **Rejects parallel staging stacks** because of hardware cost, drift, unreliable results and bad capacity estimates. Prefers **testing in production** with test builds alongside production.
- **Names shadow traffic and record/replay as tenancy use cases:** copy production traffic to an isolated area, stub outbound calls from the instance under test, and give replayed traffic its own tenancy. This is the conceptual ancestor of Capri (section 4).
- **Canaries are tenants.** The edge samples requests as canary by user type, product or location.

---

## 4. Capri (capture-replay) and MatchGuard

**Public record:** no Uber blog post, paper or talk abstract names **Capri** or **MatchGuard** as of 20 Oct 2026. The Pragmatic Engineer show page uses "Capri" only in a section title ("Testing and code review with Bazel, Slate, and Capri"). Every other hit (BigGo, Dealroom) is a summary of the podcast itself, so it is **not independent confirmation**.

**Podcast claims (from the transcript):**

- Captures production traffic "with just one middleware" because Uber has standardized language frameworks. It records inbound and outbound traffic at the service layer and **all downstream API request/response pairs**.
- A pipeline applies simple rules ("if you see this field, this is the value for that dimension"). Sessions are tagged, for example marketplace type `eats`, line of business `eats`, terminal state.
- **MatchGuard** generates the full set of *live* dimension combinations and runs pre-deploy in CI/CD. It validates every PR in a deploy against that set and shows before/after data, for example catching a break that affects only "cash trips only in Brazil".
- A session can be replayed on your Slate environment ("replay just this request on my slate environment and show me the delta").
- Capri is being exposed to agents in a loop: find sessions of a type, compose a request on Slate, check the delta, repeat.
- **Edge Gateway** has its own capture-replay, which uses Capri behind the scenes.
- Uber "had many versions of [this] in the past". Gergely's outro calls it "event capture and replay software".

**Public predecessors and adjacent tools (CONFIRMED):**

- **Ballast** ("Introducing Ballast: An Adaptive Load Test Framework", 1 Mar 2022, Minglei Wang and Cristian Velazquez):
  - Captures production traffic with **BPF/pcap** off the wire and reassembles request payloads. Supports HTTP/1.1, HTTP/2 and TChannel.
  - Replays through the **Shadower** load generator.
  - A **PID controller** adjusts RPS against SLO targets on M3 golden signals. Example targets: 80% CPU, 600 ms latency, 0.1% errors.
  - Use cases: peak capacity estimation, canary regression detection, Uber Eats load-shedder testing, and **replaying high-error-rate production traffic in staging to isolate failing code paths**. That last one is a debugging use of capture/replay.
- **Shadower** ("Introducing Shadower: A Minimalistic Load Testing Tool", 30 Jun 2022, Cristian Velazquez):
  - Payloads are captured from production hosts with eBPF and stored base64-encoded in blob storage.
  - It mirrors the same request to multiple hosts so two builds can be compared.
  - The post explains why Uber did *not* use a shared in-process shadowing library: filtering in production is complex, and the service pays CPU and memory cost.
  - **Contrast:** Capri, per the podcast, does take the in-process middleware route that Shadower's post argued against. The likely enabler is the later standardization of language frameworks the podcast mentions.
- **Multitenancy post (2020):** describes record/replay and shadow traffic with stubbed outbound calls as a design goal.

**Status:** Capri, MatchGuard, dimension tagging and the Edge Gateway use of Capri are **PODCAST-ONLY**. The *pattern* (production capture, replay in isolation) is CONFIRMED as long-running Uber practice through Ballast, Shadower and the multitenancy design.

---

## 5. Deputy and Cerberus (predecessors)

- **Public record:** none found. Searches for Uber + Cerberus/Deputy return only unrelated open-source projects. The Pragmatic Engineer show page does not mention them.
- **Podcast:** "Deputy and Cerberus allowed [the] ability to route any request from production to your testing instance and Cerberus allowed from your local testing instance back to the staging servers". Slate made both unnecessary.
  - The transcript is ambiguous: the first clause credits both tools with prod-to-test routing.
  - Reading it with the brief: **Deputy** = production request to test instance; **Cerberus** = local instance to staging.
- Gergely's outro spells it "**Cerebrus**" and places both in 2016–2020 as tools for "some level of production data replay" that were hard to use.
  - **Inconsistency to flag:** the guest describes them as *routing* tools; the host describes them as *replay* tools.
- **Status: PODCAST-ONLY.**

---

## 6. Jaeger, context propagation and the mesh

**Primary source:** "Evolving Distributed Tracing at Uber Engineering", Uber blog, 2 Feb 2017, Yuri Shkuro.

- The NYC Observability team took on distributed tracing in 2015 with two engineers. **Jaeger** (German for "hunter") was adopted internally in 2016. Its clients supported the OpenTracing API from the start.
- **Predecessor:** **Merckx**, built for the Python monolith, had no distributed context propagation.
- **TChannel** (RPC protocol, started early 2015) carried Dapper-style trace fields.
- **Scale:** about 500 microservices in fall 2015 and more than 2,000 by early 2017. Jaeger was in hundreds of services and recorded thousands of traces per second. Clients existed for Go, Java, Node.js and Python.
- Open-sourced 15 Apr 2017. CNCF incubation Sep 2017, graduated Oct 2019.
- The 2017 post does not discuss "baggage". The baggage-for-routing link is documented in the 2020 multitenancy post and the 2022 SLATE post.

**Header-level evidence:** Jaeger's baggage headers use the `uberctx-<key>` prefix and the trace header `uber-trace-id`. Signadot's docs list `uberctx-sd-routing-key` as the legacy Jaeger header for sandbox routing. This shows how Uber's tracing conventions spread into the industry's sandbox-routing tools.

**Evolution:** BITS (2024) says routing overrides now ride **OpenTelemetry** baggage. The podcast mentions an AI "Shepherd" campaign to "fix context propagation across all the services so that tracing works better". That suggests propagation coverage is still being hardened.

**Service mesh:** the SLATE post names a **host-routing-agent** (per-host, not per-pod sidecar) that acts on the baggage. One secondary source names Uber's mesh **Muttley**. No Uber primary post on Muttley was found, so treat the name as unverified.

**Podcast claims:**

| Podcast claim | Status |
| --- | --- |
| All services have Jaeger spans; baggage propagated across the call stack | CONFIRMED |
| Service mesh reads the baggage and reroutes | CONFIRMED (host-routing-agent) |
| Jaeger built "2017-18" | CONTRADICTED: 2015–16, open-sourced 2017 |

---

## 7. Edge Gateway

**Primary sources:**

- "Designing Edge Gateway, Uber's API Lifecycle Management Platform", Uber blog, 18 Aug 2020, Pavel Astakhov, Madan Thangavelu and **Uday Kiran Medisetty**. The podcast guest co-authored it.
  - Three generations: (1) dispatch/API with `messageType` routing; (2) **RTAPI**, a Node.js gateway started early 2015; (3) Edge Gateway, a standalone **Go** service with no business logic, with a layered model of Edge, Presentation, Product and Domain.
  - RTAPI numbers: 110 endpoint groupings, 800K req/s peak, about 1M lines of code, 400+ downstream services owned by 100+ teams, 50,000 integration tests, 40% of engineers committed to it.
  - The migration took about two years. The gateway uses the CFF orchestration framework and the Glue/Fx frameworks. **gRPC** was adopted as the protocol of choice.
  - Features are UI-configured: auth, request transforms, header propagation, rate limiting, load shedding.
- "The Architecture of Uber's API gateway", Uber blog, 19 May 2021, Madan Thangavelu, Abhishek Parwal and Rohit Patali.
  - Built in **Go and Java**. The Go codegen output hit linker limits.
  - The protocol manager handles JSON, Thrift and Protobuf.
  - Request pipeline: protocol manager, middleware, validation, endpoint handler, backend client.
  - APIs are defined as YAML plus Thrift IDL and stored in git. The code is generated on the open-source **Zanzibar** library.
  - 1,500+ APIs migrated from Node.js. Scaled to 500K QPS. A CI job blocks backward-incompatible schema changes for mobile.
- The SLATE post (2022) gives Edge Gateway a testing role: it **injects routing overrides** into baggage for SLATE requests.

**Podcast claims:**

| Podcast claim | Status |
| --- | --- |
| Edge Gateway is written in Go | CONFIRMED (2020); the 2021 post says Go and Java |
| Successor to RTAPI | CONFIRMED |
| Supports REST, gRPC, webhooks, GraphQL | PARTLY CONFIRMED: gRPC (2020) and JSON/Thrift/Protobuf (2021) are public; webhooks and GraphQL are podcast-only |
| Own capture-replay built on Capri | PODCAST-ONLY |
| Auto-tags required vs optional dependencies | PODCAST-ONLY. The 2021 post's dependency DAG is about codegen (client, middleware, endpoint), not runtime criticality. |

**Discrepancy:** the 2020 post says 1,600 complex APIs; the 2021 post says 1,500+ migrated. These are likely different counts.

---

## 8. Mobile testing and dogfooding: DragonCrawl, bug reporting, network record/replay

**DragonCrawl:** "DragonCrawl: Generative AI for High-Quality Mobile Testing", Uber blog, 23 Apr 2024, Ali Zamani, Anam Hira and Juan Marcano (Developer Platform / Core Automation Platform).

- An LLM reads a text representation of the screen plus the test goal and picks the UI action. No fixed script.
- **Model:** MPNet base, about 110M parameters, 768-dimension embeddings. Precision@1 is 0.9723. Alternatives tried: T5 11B, RoBERTa and others.
- In CI since about Oct 2023. As of Jan 2024 it runs the core trip flow nightly in 5 cities and gates Rider and Driver Android releases.
- Results:
  - Blocked **10 high-priority bugs** in 3 months.
  - 99%+ stability in Nov–Dec 2023.
  - Completed trips in **85 of 89** top cities without code changes.
  - Ran on 3 device types and 3 OS versions.
- Before it, engineers spent 30–40% of their time on test maintenance.
- Rider/driver matching problems were fixed by tuning fake GPS locations. This connects to the podcast's "mock the location on the device".
- **Contradiction:** a 2025 conference speaker bio claims 11 P0 bugs and $25M saved. Uber's post says 10 high-priority bugs and no dollar figure.

**Employee dogfooding / bug reporting (history, CONFIRMED):**

- "The Uber Engineering Tech Stack, Part I: The Foundation", 19 Jul 2016, Lucie Lozinski. Employees run a beta version of the apps. An "app feedback reporter" turns any screenshot taken in the app into a prompt to file a Phabricator bug task.
  - The same post names **Hailstorm**, which "drives integration tests and simulates peak load during off-peak times", and **uDestroy**, which breaks things on purpose. This is the only primary mention of Hailstorm found.
- Gergely Orosz's "Continuous Testing at Scale" slides (Uber mobile, not fetched) show the flow: dogfooding, bug reporter, Phabricator ticket, triage.
- **Network record/replay for mobile:** At Scale 2016 talk abstract ("Octopus takes on the Uber challenge", 2 Sep 2016). Uber "implemented network record/replay and scenario-based testing for iOS/Android so its tests would run reliably on CI". The speaker listing shows Jay Ayres with a TripAdvisor affiliation, which may be stale. The related Uber blog post "Rescued by Octopus" (2015, Bian Jiang) covers cross-device coordination of rider and driver apps, not network mocks.

**Wisdom and DebugAssist (2025–26):**

- **Wisdom:** named on the Pragmatic Engineer show page as a daily tool (with DevPods, Code Inbox and Slate), without a description. These details are **PODCAST-ONLY**:
  - Employee bug reports from beta apps.
  - AI routing to the owning team.
  - Captured logs, analytics, network requests and feature flags.
  - Reproduction steps reconstructed from the screens visited.
  - Expected vs observed behavior.
  - Location mocking.
  - "Network-response replay on a test device" was not found in the transcript passages read.
- **DebugAssist:** **PARTLY CONFIRMED** by an Uber engineer's public talk abstract.
  - "MCP-Powered Crash Investigation: How 11 MCP Servers Help an AI Agent Debug Production Issues at Uber", Kriti Dangi (Senior SWE, Uber), MCPCon Japan, 11 Sep 2026.
  - Built on **LangGraph** with **11 MCP servers**, 5 plugins and parallel subagents. Tools include Sourcegraph, crash analytics, Jira, feature flags, Jaeger and logging.
  - About **30 minutes from alert to reviewable PR**, against 15 days typical. It writes the fix, validates it in a loop and opens the PR.
  - Caught a crash at 5% rollout and shipped the fix the same day. Traced a battery-drain report to a hot loop.
  - Domain knowledge lives in markdown skill files in a plugin marketplace.
  - **5,000 RCAs/month across 6 languages.** Acceptance rate rose **from 5% to 30%**.
- **Contradictions:**
  1. A secondary write-up of a Perfology talk by the same engineer says **~9,000 issues/month**; the abstract says 5,000 RCAs/month.
  2. The podcast describes DebugAssist doing RCA and **handing off to Minion** to create the PR and attach it to Jira. The talk abstract says DebugAssist **writes the fix and opens the PR itself**. These may be two paths (mobile crashes vs dogfood bugs), or the architecture may have changed.
- Uber's "Running a Software Factory Efficiently at Uber Scale" (27 Aug 2026, Medisetty) confirms only that managed agents are "debugging incoming bugs" and "triaging on-call alerts", and that metrics include "alerts triaged" and "cost per alert". It gives no figures for those, and names no Slate, Capri, Wisdom or DebugAssist.

---

## 9. On-call and incident tooling

**Genie:** "Genie: Uber's Gen AI On-Call Copilot", Uber blog, 10 Oct 2024. Byline: Nicholas Marcott, Eduards Sidorovics and Paarth Chothani; the "written by" list adds Xiyuan Feng, Chun Zhu, Meghana Somasundara, Kailiang Fu and Jonathan Li.

- A RAG Slack bot answering questions in on-call/support channels, drawing on Engwiki and internal Stack Overflow. It cites its sources and can escalate to a human on-call.
- **Pipeline:** Spark ETL, OpenAI embeddings, the **Sia** vector DB and **Terrablob** storage. Requests carry a UUID through Michelangelo Gateway for cost tracking.
- Launched Sep 2023. About 45,000 questions per month across channels. Live in **154 channels**, with 70,000+ questions answered, **48.9% helpfulness** and about **13,000 engineering hours saved**.
- It is Q&A, not RCA. The post describes no debugging or root-cause capability. It is a predecessor of DebugAssist only in the "agent on the on-call path" sense.

**Other:** Uber's "Solving the Identity Crisis for AI Agents" post uses an on-call chain as its example: an Investigation Agent hands off to a Monitoring Agent, which opens a PR. Surfaced in search, not fetched. Worth reading for the identity/audit angle.

---

## 10. Industry comparisons

| Pattern | Uber | Comparable |
| --- | --- | --- |
| Request-level isolation in a shared environment via propagated metadata | SLATE / BITS (production; Jaeger→OTel baggage `request-tenancy`, host-routing-agent) | **Lyft staging overrides** (shared *staging*; OpenTracing baggage; Envoy filter); **Signadot** sandboxes (`baggage`/`tracestate` key `sd-routing-key`; legacy `uberctx-sd-routing-key`) |
| Baseline-vs-candidate comparison to separate noise from regressions | BITS placebo runs; podcast agent A/B main vs branch; MatchGuard before/after | **Twitter Diffy** (primary, secondary, candidate) |
| Capture production, replay pre-production | Ballast/Shadower (BPF/eBPF, load); Capri (podcast; middleware, downstream capture) | **Google**: Chang Seo Park, "Automatic Prevention of Accidents in Production" (AST 2020) |
| Pre-production performance gating at fleet scale | Ballast in canary | **Meta ServiceLab** (OSDI '24 Best Paper) |

### Lyft staging overrides

Lyft's Part 3 post on eng.lyft.com, "Scaling productivity on microservices at Lyft (Part 3): Extending our Envoy mesh with staging overrides", returned HTTP 403 to fetches. Facts below are verified via the InfoQ summary ("Scaling and Automating Microservice Testing at Lyft", 31 Mar 2022, Vasco Veloso) and the search snippet of the Lyft post.

- Launched by DevInfra in 2021. It replaced the per-developer **Onebox** environments.
- **Offloaded deployments:** instances in shared staging that are *not registered* in service discovery. Engineers create them from PRs with a GitHub bot.
- Override metadata is encoded as **OpenTracing baggage** and carried end to end. A modified Envoy HTTP filter reroutes to the offloaded instance.
- **Part 4** (acceptance testing): a small, centralized set of acceptance tests runs in staging after each deploy and gates production. Thousands of integration tests were removed or converted to unit tests, with no measurable rise in production bugs.
- **Key difference from Uber:** Lyft isolates within **staging**. Uber's SLATE/BITS isolate within **production**, with production dependencies by default.

### Signadot

From the "Set up Header Propagation" docs page and the "How Uber & DoorDash empower developers to preview every code change in production" blog post (23 Jun 2023, Nica Mellifera; vendor content).

- A sandbox forks only the changed services. Everything else hits the shared baseline.
- Routing key: `sd-routing-key` inside the OTel `baggage` and `tracestate` headers. These propagate automatically with OTel instrumentation.
- Legacy defaults before operator v0.19.1 were `uberctx-sd-routing-key` (Jaeger) and `ot-baggage-sd-routing-key`.
- Every service must propagate headers from inbound to outbound requests. Message queues use the same headers.
- The blog contrasts Uber (SUTs in the cluster) with DoorDash (services on dev laptops, connected via Signadot, with OTel baggage). It notes DoorDash rejected Telepresence because it conflicted with their Envoy mesh.
- The BITS search snippet attributing "71% fewer incidents" is confirmed in Uber's own 2024 post, so no vendor-only figure needs flagging there.

### Twitter Diffy

"Diffy: Testing services without writing tests" (Twitter blog, 2015). The original URL redirects to blog.x.com, which returned 403. Facts verified via the InfoQ 2015 summary and search snippets; treat as secondary.

- A proxy multicasts each request to a **candidate**, a **primary** and a **secondary**. The primary/secondary diff measures non-determinism, which filters noise from the candidate diff.
- Written in Scala under Apache 2.0. Now archived; maintained as the Opendiffy fork.
- Closest public analogue to MatchGuard's before/after delta over captured traffic.

### Google

"Automatic Prevention of Accidents in Production", Chang Seo Park, Automated Software Testing 2020 (research.google/pubs/pub49455).

- A pre-production environment where inter-server traffic is reconfigured dynamically.
- **Sampled production requests are replayed** to cover corner cases without hand-written tests.
- Handles data-mutating requests and validates back-end rewrites.

### Meta

"ServiceLab: Preventing Tiny Performance Regressions at Hyperscale through Pre-Production Testing", Chow et al., OSDI '24 (Best Paper).

- Detects regressions as small as 0.01%. The median detected regression is 0.14% on a serverless platform of more than 500K machines.
- Contributions: variance study (kernel, CPU, datacenter) and statistical detection. Seven years of operation.
- The abstract does **not** describe traffic record/replay. Use it as a perf-gating comparison only.
- No Meta primary source on functional record/replay was found.

---

## 11. Summary of podcast-claim verification

| Claim | Status |
| --- | --- |
| Slate exists; ephemeral, branch deploys, test-account association, baggage routing | CONFIRMED (2022) |
| Slate exposed to agents via MCP/CLI; agent-browser A/B; PR evidence | PODCAST-ONLY (secondary echoes only) |
| Capri, MatchGuard, dimension tagging, replay one session on Slate | PODCAST-ONLY (pattern confirmed via Ballast/Shadower/multitenancy) |
| Deputy, Cerberus | PODCAST-ONLY; guest and host describe them differently |
| Jaeger baggage as routing substrate | CONFIRMED; date given in podcast is off |
| Edge Gateway in Go, RTAPI successor | CONFIRMED |
| Edge Gateway GraphQL/webhooks, Capri-based replay, required/optional dependency tags | PODCAST-ONLY |
| Wisdom dogfood bug reports with telemetry | Name CONFIRMED (show page); details PODCAST-ONLY; lineage CONFIRMED (2016 feedback reporter) |
| DebugAssist managed RCA agent | CONFIRMED by Uber engineer's talk abstract (Sep 2026); hand-off-to-Minion detail differs |
| Service count "4,500–5,000" (Gergely outro) | Not checked here. Show page: "about the same number in 2026 as in 2019". Uber posts: "thousands"; 2,200+ in 2019. |

---

## Sources

All fetched 20 Oct 2026 unless noted.

### Uber primary

1. Simplifying Developer Testing Through SLATE. Ankit Srivastava, Alok Srivastava, Rohan Rathi. 20 Oct 2022. https://www.uber.com/blog/simplifying-developer-testing-through-slate
2. Shifting E2E Testing Left at Uber. "Uber". 22 Aug 2024. https://www.uber.com/blog/shifting-e2e-testing-left
3. Why We Leverage Multi-tenancy in Uber's Microservice Architecture. Amit Gud. 11 Mar 2020. https://www.uber.com/blog/multitenancy-microservice-architecture/
4. Evolving Distributed Tracing at Uber Engineering. Yuri Shkuro. 2 Feb 2017. https://www.uber.com/blog/distributed-tracing/
5. Introducing Ballast: An Adaptive Load Test Framework. Minglei Wang, Cristian Velazquez. 1 Mar 2022. https://www.uber.com/blog/introducing-ballast-an-adaptive-load-test-framework/
6. Introducing Shadower: A Minimalistic Load Testing Tool. Cristian Velazquez. 30 Jun 2022. https://www.uber.com/rs/en/blog/introducing-shadower-a-minimalistic-load-testing-tool/
7. Designing Edge Gateway, Uber's API Lifecycle Management Platform. Pavel Astakhov, Madan Thangavelu, Uday Kiran Medisetty. 18 Aug 2020. https://www.uber.com/blog/gatewayuberapi/
8. The Architecture of Uber's API gateway. Madan Thangavelu, Abhishek Parwal, Rohit Patali. 19 May 2021. https://www.uber.com/blog/architecture-api-gateway/
9. DragonCrawl: Generative AI for High-Quality Mobile Testing. Ali Zamani, Anam Hira, Juan Marcano. 23 Apr 2024. https://www.uber.com/blog/generative-ai-for-high-quality-mobile-testing/
10. The Uber Engineering Tech Stack, Part I: The Foundation. Lucie Lozinski. 19 Jul 2016. https://www.uber.com/us/en/blog/tech-stack-part-one-foundation/
11. Genie: Uber's Gen AI On-Call Copilot. Marcott, Sidorovics, Chothani et al. 10 Oct 2024. https://www.uber.com/blog/genie-ubers-gen-ai-on-call-copilot/
12. Running a Software Factory Efficiently at Uber Scale. Uday Kiran Medisetty. 27 Aug 2026. https://www.uber.com/us/en/blog/efficient-software-factory/
13. Kriti Dangi, "MCP-Powered Crash Investigation: How 11 MCP Servers Help an AI Agent Debug Production Issues at Uber". MCPCon Japan. 11 Sep 2026. https://agntconmcpconjapan26.sched.com/2026-09-11/list/descriptions/type/MCPCon
14. "Octopus takes on the Uber challenge". At Scale conference abstract. 2 Sep 2016. https://atscaleconference.com/?p=1028
15. Rescued by Octopus. Bian Jiang. 2015. https://www.uber.com/blog/rescued-by-octopus/ (search snippet only, not fetched)
16. Solving the Identity Crisis for AI Agents. https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/ (search snippet only, not fetched)

### Podcast

17. Uber's AI infra, from the inside. The Pragmatic Engineer. 14 Oct 2026. https://newsletter.pragmaticengineer.com/p/ubers-ai-infra-from-the-inside (show page fetched; transcript at `_input/pragmatic-engineer-podcast/transcript.txt`)

### Industry and secondary

18. Lyft, "Scaling productivity on microservices at Lyft (Part 3): Extending our Envoy mesh with staging overrides". https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-3-extending-our-envoy-mesh-with-staging-fdaafafca82f (HTTP 403 on fetch; verified via source 19)
19. InfoQ, "Scaling and Automating Microservice Testing at Lyft". Vasco Veloso. 31 Mar 2022. https://www.infoq.com/news/2022/03/scaling-testing-acceptance-lyft/
20. Signadot docs, "Set up Header Propagation". https://signadot.com/docs/guides/set-up-context-propagation
21. Signadot, "How Uber & DoorDash empower developers to preview every code change in production". Nica Mellifera. 23 Jun 2023. https://signadot.com/blog/how-uber-and-doordash-enable-developers-to-test-in-production
22. Twitter, "Diffy: Testing services without writing tests". 2015. https://blog.twitter.com/2015/diffy-testing-services-without-writing-tests (redirects to blog.x.com, 403; facts via https://www.infoq.com/news/2015/09/twitter-diffy and search snippets, not fetched)
23. Chang Seo Park, "Automatic Prevention of Accidents in Production". AST 2020. https://research.google/pubs/pub49455/
24. Chow et al., "ServiceLab: Preventing Tiny Performance Regressions at Hyperscale through Pre-Production Testing". OSDI '24. https://www.usenix.org/conference/osdi24/presentation/chow
