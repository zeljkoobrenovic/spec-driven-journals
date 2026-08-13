---
timetoread: "8 min listen"
---

## Features Are Spend, Adoption Is Earnings

**Ben:** Blunt version first. Our platform team shipped forty capabilities this year. That's growth, right? Why do I need a "growth model" beyond a healthy release cadence?

**Ana:** Because a platform grows adoption, not functionality — and those forty capabilities tell me nothing until you show me the usage curve. Features are what we spend; adoption is what we earn. A roadmap that celebrates shipped capabilities while usage stays flat is a platform in denial. That's the feature-count victory lap, and it's the first anti-pattern in the record.

**Ben:** Harsh. But internal platforms aren't consumer apps — you can just mandate usage and skip the whole adoption game.

**Ana:** You can, and then you've blinded yourself. A mandated platform learns nothing: the usage numbers say "compliance," not "value." Voluntary adoption is the only honest signal a platform gets — which is why the record's premise is voluntary adoption throughout, and why mandate policy is explicitly out of scope. It's [[understanding-platforms]]' harmonization-over-standardization frame, applied to growth.

**Ben:** So if adoption is the metric, what are the levers?

**Ana:** Three dimensions, kept in balance. Reach — which user groups, business units, geographies actually adopt. Breadth — whether the platform covers the right portions of the problem space. Depth — whether the key capabilities are complete, integrated, automated, polished. The discipline is balancing them, because maximizing any one while the others starve is how platforms fail.

## The Perfect Platform for One Customer

**Ben:** Let me defend the depth-first strategy, because every platform team I know runs it. Your biggest customer has sophisticated needs. Serve them brilliantly, and the reference case sells the platform to everyone else.

**Ana:** That's the most seductive failure in the chapter, and the most common one I've seen: building the perfect platform for one customer before gaining broader adoption. It feels like customer obsession. What it actually does is quietly convert the platform team into a professional-services team for one account — and make the platform expensive, confusing, or intimidating for every other potential adopter.

**Ben:** So you'd tell that big customer no?

**Ana:** I'd tell them a principled no or a scoped yes, through triage — we'll get there. But first the lifecycle, because "which dimension gets investment" depends on the phase. Explore: cheap experiments testing whether users actually *value* the platform — not whether the technology works; those are different tests, and passing the second while failing the first is how prototypes get promoted into failures. Expand: remove adoption obstacles — better self-service, less manual support, high-quality documentation. Extract: adoption is established, improve the economics, benefit from scale.

**Ben:** And the team just rides along through all three phases?

**Ana:** No — that's the overlooked item. Between phases we explicitly reassess whether the team, its skills, and its leadership still match the phase. The people who excel at exploring are not automatically the people who excel at extracting. Skipping that conversation is how a platform outgrows its own leadership without anyone deciding anything.

## The First Hour

**Ben:** You claim a platform's fate is set in the new user's first hour. That's marketing-speak for "make a nice tutorial," no?

**Ana:** It's engineering work, not marketing. A prospective user who hits a wall of unfamiliar concepts, long parameter lists, and silent failures doesn't file a feature request — they go back to what they know, and you never hear about it. So the on-ramp is a first-class feature: measure the initial learning effort, minimize the cliff, build on concepts users already know, default the complicated parameters, template the common cases, and give useful feedback when things fail.

**Ben:** Fine, but powerful tools have learning curves. Some onboarding pain is the price of capability.

**Ana:** The powerful platform nobody starts using grows nothing — that's the direct answer. And the record's sharper point is about what happens *after* the first hour: the hockey-stick experience. Demos beautifully, tutorial case works in minutes — then the first slightly advanced need requires a week and an expert. That curve loses users at the worst possible moment, precisely when they were becoming committed.

**Ben:** What flattens the hockey stick?

**Ana:** Simple tasks easy, complex tasks possible, and painless gear-shifts between them — plus escape hatches for when platform constraints are genuinely reached. Most of that machinery — the defaults, the templates, the abstractions that actually reduce cognitive load — is built in [[implementing-platforms]]. This record is what makes that machinery a growth strategy: we measure time-to-first-useful-result for new users and treat regressions as bugs.

## Triage, and the Biased Sample

**Ben:** Now the roadmap. "Triage function" sounds like a bureaucratic way of ignoring customers.

**Ana:** It's the opposite of ignoring — it's evaluating every request on two axes: business impact and roadmap fit. High-impact requests that fit get prioritized. Low-impact fits go to the backlog by capacity. And here's the interesting quadrant: high-impact requests that *challenge* the strategy get investigated — neither reflexively accepted nor reflexively refused, because they might be telling you the strategy is wrong. That fit test only works because there's a [[platform-strategy]] to test against — without it, triage collapses into taste.

**Ben:** And the low-impact misfits?

**Ana:** Declined — with the principles explained. That clause carries the whole system. An unexplained no spends trust; a principled no builds it, because the customer learns how the platform decides, not just what it decided. Do that against a published, credible roadmap and the whole thing turns from private judgment into a visible contract.

**Ben:** Still, "listen to your users" is product management 101. Why all the hedging about feedback?

**Ana:** Because existing users are a biased sample — that's the trap in 101. The people already on the platform are, by definition, the people the platform already fits. Roadmap by feature poll optimizes for the converted and never discovers why non-users stay away — and the non-users are the actual growth frontier. So we approach users with hypotheses and options rather than polls, measure outcomes rather than platform activity, and deliberately study the people who *didn't* adopt.

## Scaling Down

**Ben:** Last objection. Tiers and slices — different offerings for different customers — sounds like fragmentation with a strategy name. One platform, one offering, keep it simple.

**Ana:** Everything-or-nothing is an adoption tax. Small teams that must swallow the full platform's cost and complexity never start — and never grow into the customers who'd want the whole thing. Vertical tiers let operational qualities like performance, security, and scalability vary for different budgets; horizontal slices serve customers who need only part of the platform. Each is defined around a clear use case with the trade-offs communicated.

**Ben:** And the fork risk?

**Ana:** Handled by the one hard constraint: the underlying assets stay shared. Tiers and slices are differently sized portions of one platform, not per-tier stacks. Duplicated stacks are exactly the anti-pattern; done right, scaling down is a growth strategy — a smoother entry for customers who may grow later, which is what adoption-first wants.

## What We're Not Saying

**Ben:** Close it out. Fences?

**Ana:** Four. This isn't the product operating mode itself — [[platform-as-a-product]] establishes that; this is the growth discipline inside it. It isn't the self-service machinery — that's [[implementing-platforms]]. It isn't the definition of success — [[platform-success]] owns that; this is the path there. And it isn't a mandate policy — voluntary adoption is the premise, not a fallback.

**Ben:** Revisit conditions?

**Ana:** Three tripwires. Adoption plateaus while the feature list keeps growing — we're optimizing the wrong dimension. The team's calendar shows it operating as a delivery arm for one customer — professional-services drift. Or new-user time-to-first-useful-result trends up for two consecutive quarters — the on-ramp is eroding.

**Ben:** One sentence.

**Ana:** Nobody has to use an internal platform — so grow it like a product: balance reach, breadth, and depth, win the first hour, say principled nos, and give every customer an appropriately sized way in.
