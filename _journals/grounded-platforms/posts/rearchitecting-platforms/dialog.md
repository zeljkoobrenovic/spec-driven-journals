---
timetoread: "8 min listen"
---

## The Rewrite Urge

**Ben:** Let's start where every rearchitecture actually starts: an engineer looks at the codebase and says "this is unmaintainable, we need to rebuild it." Why isn't that enough?

**Ana:** Because "unmaintainable" is usually an aesthetic judgment, and this record refuses aesthetic judgments as triggers. A rearchitecture starts only when the current architecture genuinely constrains one of four things: feature delivery, reliability, security, or efficiency — and beyond what incremental improvement can fix. Age is not a constraint. Unfashionable is not a constraint. The resume-driven rewrite — justified by the new stack everyone is hiring for rather than a constraint anyone can name — is the first anti-pattern on the list.

**Ben:** But sometimes the code really is the problem.

**Ana:** Then you can name the constraint, demonstrate it, and show that incremental work can't fix it — and you're through the first gate. The point isn't that rewrites never happen; it's that the burden of proof sits on the rewrite. Most rewrite urges exit at that first check, and they should.

**Ben:** Fine, gate one. What's the framing behind the rest?

**Ana:** One sentence: a rearchitecture is a business investment, not a technical adventure, and it's gated like one. Four gates total — a genuine constraint, a full go/no-go review before work starts, a valuable production deliverable every 12 months, and an annual review with a real stop option. What's telling is that the gates are mostly not technical. The graveyard of platform rewrites isn't full of bad designs; it's full of good designs that lost their funding in year two, their sponsors in a reorganization, or their customers to an uncounted migration bill. Rearchitectures fail organizationally more often than technically.

## Why Not Just Build v2?

**Ben:** Here's the seductive option, though. Don't touch the legacy system — build the clean v2 next to it, migrate everyone when it's ready. Greenfield speed, no legacy constraints. Why does the record prefer grinding through an incremental rebuild?

**Ana:** Because I've seen what the v2 promise actually delivers: two platforms to operate, a migration cliff nobody climbs, and a team split between the past and the future. That's the v2 island. Rebuilding in place is less glamorous and more survivable — every step ships, every step is testable against real load, and there is never a moment where the business depends on a big bang landing.

**Ben:** Never a separate system? That's absolutist.

**Ana:** Not never — "unless there is a compelling reason otherwise." But it must be argued, not assumed. And one combination is close to forbidden: a new-product bet and a major redesign in the same project. Each is risky alone; together the failure modes multiply.

**Ben:** The 12-month rule is where I'd push hardest. This is foundational work — storage layers, control planes. Demanding production value every year sounds like it forces theater deliverables.

**Ana:** The record actually names that risk in its own revisit conditions — if the 12-month rule starts producing theater that demonstrates nothing about the architecture, the record itself gets revisited. But here's why the rule stays: a multi-year rearchitecture that goes dark is a standing invitation to be cancelled, and deserves to be — because it's also epistemically dark. Nothing in production means nothing has been learned about whether the new architecture actually works. So every major phase carries three levels of success: an audacious goal, a valuable fallback, and a production proof — new components serving real load for a real customer. The effort cannot have a zero year. Even the worst case leaves real components carrying real traffic, which is both engineering evidence and political capital.

**Ben:** And if no phase can produce production value within 12 months?

**Ana:** Then the architecture itself gets reassessed. That's not a bug in the rule — that's the rule working. An architecture that can't be delivered incrementally is telling you something about its risk profile.

## The Bill Nobody Counts

**Ben:** Migration costs. Every business case I've seen counts the platform team's headcount and calls it the cost. You're saying that's half the bill?

**Ana:** Usually the smaller half — and it's paid by other people, which is exactly why it goes uncounted. The platform team builds the new system; the consumer teams pay the migration tax: their engineering effort, retraining, running old and new simultaneously, data migration, SDK and tooling changes, support load. A business case built on the building team's effort alone gets discovered to be half the true cost when consumer teams present their bill — after commitment, when it's too late to say no. So the go/no-go review demands the honest number up front, confirmed to be smaller than the expected business value. That's what separates an investment case from a pitch.

**Ben:** The go/no-go also wants "leadership commitment that survives reorganizations." Come on — nobody can promise that. Sponsors leave, budgets tighten.

**Ana:** Which is why the record treats protection, not approval, as the test. Approval in one budget meeting is easy; the question asked before starting is whether leadership is prepared to fund and protect this effort through reorgs and shifting priorities. If the answer is shaky, the record's answer is: wait. An unprotected rearchitecture that gets orphaned mid-migration leaves you the worst of both worlds — half the estate on each architecture, indefinitely. Starting later beats stopping in the middle.

**Ben:** There's a people clause in here too, and it's counterintuitive. The instinct on a rewrite is to give it to fresh eyes — new hires, unburdened by history. The record says don't?

**Ana:** It says the people who know why the old system is shaped that way are the asset, not the obstacle. Handing the rewrite to enthusiastic newcomers — unaware of the constraints that history encodes — is how organizations pay twice for the same lessons. The balance is explicit: new hires challenge assumptions, long-tenured engineers carry the context, and ownership transfers only after the relationship between them is built. Same discipline for pioneer teams: they may run ahead of the platform, but with an explicit integration path — so the experiment never hardens into a permanent shadow platform that duplicates the thing it was meant to feed.

## Stopping Without Shame

**Ben:** Security gets its own section in this record, which surprised me. Isn't that orthogonal to rearchitecting?

**Ana:** It's the opposite of orthogonal — the rearchitecture is the rare moment when security can move from human vigilance into structure. Hazards eliminated rather than documented, protections that don't depend on anyone remembering anything, and paved paths where the safest option is the easiest option. Bolt a security review onto a finished design and you've forfeited exactly the leverage the rewrite existed to create. Security by design and by default, or you've wasted the one chance you get.

**Ben:** Now the hardest gate. The annual review with a stop option. Three years in, fifty engineer-years spent — nobody stops that project. The sunk cost is a gravitational field.

**Ana:** Which is why the question is institutionalized instead of left to courage. Once a year, in writing: would we still start this project knowing what we now know? Goals reassessed, real improvements measured against the promises, old architecture retired as customers migrate. And when the evidence no longer supports the hypothesis, the work is stopped, revised, or delayed — without shame. That last part is load-bearing: the zombie project, kept alive by sunk cost and the awkwardness of stopping, is an anti-pattern precisely because stopping is treated as failure rather than as the review doing its job. The 12-month wins make this tractable, by the way — stopping never means writing off everything, because every completed phase left components in production.

**Ben:** Close us out. What does this record explicitly not cover?

**Ana:** Three boundaries. It's not [[planning-and-delivery]] — the milestone and migration discipline is inherited from there; this record adds the extra gates a foundational rewrite demands. It's not a technology-selection guide — it constrains how major OSS and vendor bets are evaluated, ecosystem trajectory and 5–10-year viability rather than fashion, but it won't pick your database. And it's not an application-rewrite playbook — the scope is platforms, with a broad developer base and migration obligations on consumer teams.

**Ben:** And the one-liner for the architect drafting the proposal?

**Ana:** Bring me a constraint, a costed migration bill, a customer who's committed, and a plan that puts value in production every 12 months — and be ready, once a year, to argue that we'd still start it today.
