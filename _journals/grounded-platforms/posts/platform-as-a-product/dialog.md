---
timetoread: "8 min listen"
---

## The Captive-Audience Trap

**Ben:** Here's my problem with "platform as a product". Our platform is mandated. Usage is at a hundred percent. Every dashboard is green. What exactly would product discipline add that we don't already have?

**Ana:** That's precisely the trap. An external product that stops serving its customers loses them and knows it immediately. An internal platform with mandated usage can fail for years while its dashboards look fine — usage stays high because there is no alternative. Until suddenly there is one, built in anger by a customer team. Fournier and Nowland's sharpest warning in the whole chapter is exactly this: do not interpret mandatory usage as proof of success.

**Ben:** "Built in anger" — you mean shadow platforms.

**Ana:** Yes. Dissatisfied internal teams will eventually build competing solutions. That's why a captive audience is a risk, not a moat. The whole discipline of treating internal engineers as customers exists to surface the dissatisfaction that captivity hides. My one-line test: a platform that customers would not choose if they had a choice is not done — it's failing slowly.

**Ben:** So what does "treating engineers as customers" actually mean beyond a values slide?

**Ana:** Concrete practices. The team can name its customer segments. It observes real workflows, pain points, and workarounds — not what customers say they want, but how they actually work. Regular interviews. Engineers participate in customer support and hear the research directly, because customer empathy is everyone's job, not a PM monopoly. And goals include adoption, satisfaction, and productivity — customer outcomes, not shipping milestones.

## Escaping the Feature Shop

**Ben:** Let me flip it, though. Isn't the responsive thing to build what customers ask for? Team A wants a flag, team B wants a framework supported. Saying no sounds like arrogance.

**Ana:** Building each request as specified is how you become a feature shop — a growing backlog of bespoke work only the platform team can implement, serving whoever asks loudest. What customers say they want and what they need are different products. The product move is to separate the underlying problem from the proposed solution, find the need shared across teams, and build the reusable, self-service capability. Feature requests are signals for product opportunities, not a work queue.

**Ben:** And the loudest team? Usually it's also the biggest, so it has a claim.

**Ana:** It has a claim, not the design pen. Loudest-team design — shaping the platform around the largest or most influential customer while everyone else's workflows go unobserved — is a named anti-pattern. You read metrics and requests with the captive-audience caveat in mind and deliberately design beyond that one team.

**Ben:** Where do good platform products come from, then, if not the request queue?

**Ana:** Often from inside. Promising platform products frequently start as tools internal teams already built and love — you generalize from proof. Then discipline: prototype with a partner team, seriously consider buying instead of building, and — this is the part everyone skips — validate internal product–market fit with real commitments. And sometimes the best move is rethinking the problem entirely: eliminate the task or operate it centrally, rather than making everyone's copy of it slightly easier.

## Validation and the Change Budget

**Ben:** "Real commitments." Distinguish that from what teams do now, which is nodding in a roadmap review.

**Ana:** Hypothetical validation is the anti-pattern: counting enthusiastic meetings as demand. Real validation is a startup's bar — named customer segments, alpha customers willing to commit actual time, effort, or budget. Internal platforms fail most expensively at adoption: the product works, and nobody moves. So the fit gets proven before serious investment, not after.

**Ben:** You also fold migration cost into that decision, which seems odd. Migration is a launch problem, surely — you build the thing, then figure out how people get there.

**Ana:** That's migration as an afterthought, and it's how the customer-side migration turns out to be more expensive than the product. The chapter's most underrated instruction is to include migration cost in the decision of whether a product is worth building at all: onboarding effort, compatibility problems, hidden dependencies, a clear path off the old product. And no new generation launches without a retirement plan for the old one — multiple live generations without one is a debt.

**Ben:** Suppose the new thing is genuinely, technically better. Adoption should take care of itself.

**Ana:** Never assume adoption just because something is technically better. Customers have a change budget — a finite capacity to absorb change per year, shared with everything else the organization is doing. A better product landing in a year already full of migrations will be rationally ignored. So you coordinate launches, prioritize offerings with enough immediate benefit to justify the switch, and market the platform internally so teams know an offering exists before they build their own. That's not polish; that's how a platform stays welcome.

## Measuring What Matters

**Ben:** Metrics. My platform team reports rising adoption and request volume every quarter. You're going to tell me that's worthless.

**Ana:** Not worthless — flattering. Activity metrics flatter; impact metrics steer. Request counts and adoption curves can all rise while customers get no faster. The discipline is to write down the hypothesis — this platform work causes that customer outcome — identify the intermediate signals, and check whether reality agrees. Guardrail metrics stop one number improving at another's expense, and surveys confirm the numbers still mean what you think they mean.

**Ben:** And when the evidence says the beloved initiative isn't working?

**Ana:** Then the strategy changes — not the metric. That's the expensive honesty in this record. Features get defined by the customer outcomes they should create, not by prescriptive specs, so there's always something falsifiable to check.

**Ben:** Where does reliability sit in this? Ops has its own record, doesn't it?

**Ana:** The machinery does — on-call, support, operational feedback all live in [[operating-platforms]]. What belongs here is the product framing: reliability is part of the product experience, and instability is a product defect. Trust is the platform's real currency — customers burned by an unstable offering will reject the next valuable one. Every launch is priced in the trust earned or lost by the last. Hence the rule: no new features on an unreliable foundation.

**Ben:** One more failure mode I've seen: the platform PM who's really a ticket administrator.

**Ana:** PM as backlog admin — the org chart says product, the behavior says feature shop. The healthy split: product managers own customer problems, outcomes, and strategy; engineering managers own execution; engineers keep shaping solutions rather than implementing specifications. Collapse any of that and you get a platform nobody would choose.

## The Boundaries and the Bar

**Ben:** Wrap it up. What is this record explicitly not claiming?

**Ana:** Four boundaries. It's not the whole pillar model — that's [[four-pillars]]; this unpacks the "curated product" pillar into the full operating discipline. It's not the operational machinery — that's [[operating-platforms]]. The roadmap appears here as a product artifact, but the planning mechanics live in [[planning-and-delivery]]. And it's not a tooling or vendor recommendation — the discipline matters, not which developer portal you buy. One more nuance: I'm not saying mandates are never legitimate. Sometimes they are. They're just never evidence of product success.

**Ben:** And what makes you reopen the record?

**Ana:** Three alarms. A customer team builds a competing solution to a mandated platform — the captive-audience alarm going off. Platform backlogs filling with bespoke single-team requests — the feature shop reasserting itself. Or a significant investment reaching build without surviving the final pre-investment review in the Checklist tab. Day to day, the bar is simpler: every platform team can name its customers, has observed real workflows recently, can state the impact hypothesis behind its roadmap — and "we have a captive audience" is never accepted as an adoption strategy.
