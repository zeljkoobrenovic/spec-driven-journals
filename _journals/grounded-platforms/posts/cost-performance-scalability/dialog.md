---
timetoread: "8 min listen"
---

## The Bill Nobody Owns

**Ben:** Blunt version first. Every organization already has someone yelling about the cloud bill — usually finance, usually in the last week of the quarter. Why does cost need to be a *platform capability* with its own record?

**Ana:** Because the yelling proves the point. An organization with one cloud invoice has exactly one team that cares about cost, and it's the team least able to fix it. The record's first structural move is attribution: cloud-native cost reporting plus OpenCost on the clusters, consistent labels — team, cost center, business unit, application — on every namespace and deployment, dashboards, and showback or chargeback. That turns one enormous invoice into hundreds of small, ownable numbers. The team that sees its own number is the team that fixes it.

**Ben:** And the "performance and scalability" part of the title? That reads like three chapters stapled together.

**Ana:** It's one discipline, deliberately. The chapter's very first step is not a savings measure — it's defining availability and performance SLOs, naming acceptable latency, throughput, and downtime, and calculating what meeting each SLO costs. Cost work without SLOs is just a smaller number. A cheaper platform that misses its latency target hasn't been optimized — it's been broken at a discount.

**Ben:** So no cost cutting before the SLOs are on the table.

**Ana:** None. And the same clause kills the lowest-price reflex: the question is never "what's cheapest," it's "what's the cheapest way to meet the SLO the business actually needs." Infrastructure spend gets justified by business value, not by being the smallest line item on the menu.

## The Loop, Not the Project

**Ben:** Fine — attribution and SLOs. But every company I've seen runs a big cost-optimization project once a year, saves twenty percent, and moves on. What's wrong with that?

**Ana:** The record names it as an anti-pattern: the savings project. A one-time drive produces a one-time saving, and the waste grows back, because the forces that created it — fear-sized resource requests, unlabeled workloads, unwatched autoscalers — are all still there. The capability is a standing loop: baseline, rightsize, scale, buy capacity at the right price, measure, repeat.

**Ben:** Walk me through one turn of it.

**Ana:** You pick the workload, record its current hourly and monthly cost, and set a measurable reduction target — before touching anything. Then you profile: actual CPU and memory usage, peak periods, whether the peaks even coincide, and the gap between what the workload uses and what it requests. That gap is usually the whole story — requests sized by fear, provisioned for a combined peak that telemetry shows never happens.

**Ben:** And then you cut the requests.

**Ana:** With reasonable headroom — the target is fit, not asphyxiation. And rightsizing goes past requests: you determine whether the workload is CPU-bound, memory-bound, I/O-bound, or storage-bound, and match the instance category to that — compute-optimized for CPU-heavy, memory-optimized for memory-heavy, or automated instance selection with Karpenter so node shapes follow workload profiles without a human in the loop.

**Ben:** Why insist on the baseline ceremony? Engineers can usually spot an oversized deployment on sight.

**Ana:** Because the baseline is what separates optimization from guessing. Without a recorded starting cost and a re-verification at the end, "we cut this workload thirty percent" is a story, not a fact. The record's closing line in practice: a cost story without a baseline is an anecdote. The handbook even ships the loop as a worked exercise — baseline, thirty-percent target, one week of profiling, rightsize, load-test, measure after two weeks, document, share with the platform team. That exercise is in the Checklist tab near-verbatim.

## Autoscaling You Can Trust

**Ben:** Autoscaling. My skeptical take: HPA is a checkbox everyone ticks and nobody tests, and the first traffic spike turns it into a flapping disaster.

**Ana:** The record agrees with the diagnosis and prescribes the opposite of the checkbox. HPA goes only on workloads that actually benefit from extra replicas, with sensible minimum and maximum replica counts, utilization targets, safe scale-up and scale-down behavior, and stabilization windows precisely against the thrash you're describing. And then the load-bearing clause: it's tested under generated load, and the test verifies that scaling maintains the SLO. Autoscaling is a performance instrument before it's a savings instrument. Untested, you don't have autoscaling — you have hope.

**Ben:** CPU utilization is a lousy signal for plenty of services, though.

**Ana:** Which is why the record keeps custom business-level metrics in scope — requests per second, queue depth, active sessions — for the workloads where CPU is the wrong dial.

**Ben:** And VPA? Letting a robot resize production workloads sounds like a new outage category.

**Ana:** It is, if you skip the observation discipline. VPA runs in recommendation mode first — "off" mode — and watches realistic workload behavior long enough to mean something. You review the CPU and memory recommendations, Goldilocks if you want them inspectable, implement only the high-confidence ones, bound everything with minimum and maximum limits, and exclude containers that must not be touched — sidecars, classically. And whether HPA and VPA run together is an explicit decision, not an accident of two teams installing two controllers.

## Buying Capacity at the Right Price

**Ben:** Spot instances. The discount is enormous and so are the war stories. Where does the record land?

**Ana:** On stability classes. Capacity pricing follows workload stability, not the other way around. Stable baseline load runs on-demand or committed. Spot serves fault-tolerant workloads — with interruption handling configured, taints and tolerations where spot nodes need isolation, node affinity to prefer spot where it pays, and fallback to on-demand when the market moves. And there's an explicit never-list: business-critical single replicas, long-running jobs that can't tolerate interruption, highly latency-sensitive operations. The anti-pattern name is spot roulette — putting the wrong workload on spot because the discount looked good in a spreadsheet.

**Ben:** And committed-use discounts? Finance loves those.

**Ana:** Same bet, inverted. Commitments pay off on the true, predictable baseline — and only there. The record forbids overcommitting beyond that baseline and specifically keeps committed capacity away from variable development, test, batch, and emerging workloads. Commit those and you've converted a discount into a liability: steady-state prices for load that never became steady. The record calls it the commitment trap.

## Guardrails, Gates, and the Month-End Surprise

**Ben:** All of this is still voluntary, though. What stops one team's memory leak from eating the whole cluster's budget?

**Ana:** Governance by policy, not by convention. ResourceQuotas per team or namespace — CPU, memory, pod counts, persistent volume claims. LimitRanges per container, with default requests and limits and allowable minima and maxima. Workloads are required to declare CPU and memory requests, and all of it is enforced with policy-as-code — Kyverno or Gatekeeper in the reference stack. The machinery itself lives in [[policy-as-code]]; this record states what the machinery enforces. Without it you get the quota-free commons: one team's leak is everyone's capacity problem.

**Ben:** And when something slips through anyway?

**Ana:** Then the question is when you find out — and the record's answer is "before the invoice." A normal cost baseline, alerts on unexpected spikes, current spend compared against historical averages, thresholds tuned to real production behavior, and standing investigations into memory leaks and unexpectedly hungry CPU consumers. The anti-pattern is the month-end surprise: every spike discovered on the invoice, weeks after it started.

**Ben:** You said "before the invoice" — how early can you actually push the cost conversation?

**Ana:** Into the pull request. That's the CI/CD integration: estimate workload cost before production deployment, diff the new CPU and memory requests against the previous release, flag unusually large increases, require explicit approval for major ones, check namespace quotas during deployment and fail with a clear remediation message when the budget would be exceeded, put estimated monthly cost in the deployment metadata and PR summary, and compare post-deployment cost against the previous seven-day average. The engineer about to spend the money sees the number before spending it.

**Ben:** Careful, though — a pipeline that blocks every cost increase will just teach teams to route around it.

**Ana:** Agreed, and the record is explicit: major increases need approval, not prohibition. Growth that pays for itself is the point. And there's a matching revisit trigger — if teams start gaming quotas instead of negotiating them, the guardrails have become bureaucracy and need redesign, not more enforcement.

**Ben:** Close it out. What is this record explicitly not doing?

**Ana:** It's one capability of the reference implementation, scoped to its own chapter. The telemetry stack it rides on is [[observability-implementation]]; the pipeline it gates is [[cicd-as-a-platform-service]]; the enforcement engine is [[policy-as-code]]; the default quotas a new tenant starts with are [[self-service-onboarding]]. And the economics of the platform itself — cheaper per team as adoption grows — that's pillar three of [[four-pillars]]; this record is what makes that claim measurable. The test that runs through all of it: can any engineer see what their workload costs today — and does a bad cost decision get caught before month-end?

**Ben:** And if the answer is "we'll know when the invoice arrives"?

**Ana:** Then you don't have a cost capability. You have a subscription to surprises.
