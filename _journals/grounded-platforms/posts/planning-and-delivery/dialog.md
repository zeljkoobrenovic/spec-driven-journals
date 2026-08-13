---
timetoread: "8 min listen"
---

## The Plan That Only Lists Features

**Ben:** Blunt question to start. Planning records are usually where good intentions go to die — every team says "we plan honestly." What does this record actually forbid?

**Ana:** It forbids the most popular platform plan in existence: the one that budgets 100% of capacity for features and then delivers 60% of it. Platform teams carry four kinds of work whether the plan admits it or not — features, keep-the-lights-on work, mandates from leadership, and system improvements. A plan that only lists features doesn't make the other three disappear; it makes them invisible, unfunded, and late. And then the team looks slow when reality collects its tax.

**Ben:** So the fix is a spreadsheet with four rows? That seems thin for a whole record.

**Ana:** The four categories are the visible part. The discipline is that the roadmap is built bottom-up from all four, with numbers attached. KTLO gets estimated from historical data — last period's on-call, support, and remediation load, with one-time events stripped out — and it's held near 40% of capacity. Mandates get listed separately and costed at their actual engineering price. What's left is what features and improvements can honestly claim.

**Ben:** Forty percent for keeping the lights on sounds enormous. If my team told me KTLO was eating 40%, I'd say they have a quality problem, not a planning problem.

**Ana:** You might be right — and the cap is what tells you. Forty is a ceiling, not an entitlement. When KTLO breaches it, the record's rule kicks in: work that reduces operational burden jumps the queue. The number turns a slow suffocation into a visible trigger. Without measuring it, KTLO just grows silently in the space nobody is watching, and the plan is fiction from day one.

**Ben:** And mandates — compliance, migrations, the CEO's integration project. Teams usually just absorb those. Why make a ceremony of costing them?

**Ana:** Because the silent mandate tax is one of the classic failure modes: the team absorbs the compliance work and the migration without surfacing the cost, and then gets held to the original roadmap anyway. Costing mandates explicitly does two things — it makes the trade-off visible to the people issuing the mandates, and it gives you grounds to escalate early when the mandate load exceeds realistic capacity. Sometimes the mandate gets removed or delayed. That conversation can only happen if there's a number on the table.

## Proposals Before Projects

**Ben:** Let's talk about the proposal requirement, because "write a document before you start" is where engineers roll their eyes. Isn't this just process for its own sake?

**Ana:** The expensive platform failures I've seen were not defeated by technical difficulty. They drifted — because nobody could state crisply what problem was being solved and what "done" meant. A multi-year project that was never quite about anything is the most expensive failure mode there is. The proposal — problem before solution, options with trade-offs, measurable success criteria, early milestones — is cheap insurance against exactly that. And there's a diagnostic in it: if the problem isn't clear enough to write a concrete proposal, it isn't clear enough to staff.

**Ben:** Every bug fix needs a signed document now?

**Ana:** No — long-running projects only. That's an explicit boundary in the record. This is the gate for multi-quarter commitments, not for tasks.

**Ben:** Fine. But the buy-in part worries me. "Resolve major disagreements before implementation" sounds like a recipe for endless pre-alignment meetings while nothing ships.

**Ana:** The alternative is worse: discovering the disagreement at launch, after the money is spent. The review is with a specific set of people — engineering leads, product management, the stakeholders who'll live with the result — and it ends. What it buys you is a project that doesn't get relitigated every quarter, because the argument happened once, on paper, before the first commit.

**Ben:** And then the classic move: hire a project manager to keep the thing on rails.

**Ana:** At the right moment, yes — PMs join when coordination risk becomes substantial: firm deadlines, many dependencies, real scheduling bureaucracy. What a PM can never do is compensate for unclear technical planning. Nobody can. If the technical plan is mush, adding a project manager gives you well-organized mush.

## Launch Is the Middle

**Ben:** Now the claim I most want to poke: "launch is not the finish line — adoption is." Isn't adoption the customers' job? We build the platform, we announce it, teams migrate when they're ready.

**Ana:** That's the anti-pattern the record names first: launch as the finish line. You declare victory when the platform ships, and then adoption flatlines — because migration was "the customers' problem" and nobody was staffed to help them move. A platform nobody migrates to is a cost, not an asset. So adoption work is inside the project plan: early adopters identified and actually talked to before we assume they'll come, documentation and enablement planned, adoption metrics defined, customer migration treated as a first-class dependency and staffed like one. The sharpest planning question isn't "when do we ship?" — it's "who moves, when, and who does the work of moving them?"

**Ben:** You also want monthly milestones in year one. For platform work? Some of this is foundational — there's genuinely nothing to show for months.

**Ana:** "Nothing to show for months" is precisely the condition the record refuses, because it's unfalsifiable. A multi-year effort measured only by technical completion can be "on track" for two years and deliver nothing — that's the two-year dark period, and it's unprotectable when budgets tighten. Monthly milestones in year one, quarterly later, and each one delivers something a customer or the business can see. And value is defined broadly — a completed migration or a retired system is value, not just shipped features. Milestones are where reality gets a vote: scope creep becomes visible, dead ends surface early, and open-ended slogs can be stopped instead of quietly renewed.

**Ben:** One escape hatch teams love: innersourcing. "We deprioritized your feature, but feel free to contribute it." Doesn't that square the capacity circle?

**Ana:** It's an escape hatch, and the record is cautious about it for a reason: the platform team still owns every contributed line — review, maintenance, support, forever. Contribution models are fine selectively, with clear rules. What they can never be is a substitute for the honest prioritization conversation with the customer. "Build it yourself" is not a roadmap answer.

## Narrating the Invisible

**Ben:** Last piece — the biweekly wins and challenges. Status reporting is the most theater-prone ritual in engineering. Why is yours different?

**Ana:** Because platform work is invisible when it works — nobody notices the infrastructure that didn't fail. Narration is part of delivery, not decoration on it. The format keeps it honest: each win or challenge is a short bold summary, then situation, action, result — rewritten so the intended audience actually understands it, focused on outcomes and impact. Story-point status is the named anti-pattern: reporting ticket counts and velocity to executives who needed to hear what changed for customers and why it matters.

**Ben:** And challenges? In most orgs, reporting a challenge upward is reporting a confession.

**Ana:** Here it's information. Surfacing a blocking dependency early is delivery work — with one rule of decency attached: the partner team hears it from us before they read it in a report. No public ambushes. And the process itself is on notice: when wins-and-challenges stops producing useful information, the format changes. The record's own revisit conditions say so — if it degrades into bureaucracy nobody reads, it goes.

**Ben:** Close it out. What is this record explicitly not?

**Ana:** Four boundaries. It doesn't decide what to build — that's [[platform-as-a-product]]; this record turns direction into a plan that survives contact with capacity. It doesn't define the operating model behind the KTLO line — on-call and support live in [[operating-platforms]]. It doesn't govern foundational rewrites — [[rearchitecting-platforms]] inherits the milestone and migration discipline and adds its own gates. And it's not a project-management methodology — no sprint mechanics, no estimation poker, no tool mandates.

**Ben:** And the one-sentence test of whether a team is living it?

**Ana:** Every stakeholder gets a biweekly update they can actually understand, and every plan shows all four kinds of work with KTLO as a number — because "I did not know that was happening" is a planning failure, and we treat it as one.
