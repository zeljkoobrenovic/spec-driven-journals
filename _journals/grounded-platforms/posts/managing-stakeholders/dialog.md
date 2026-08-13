---
timetoread: "8 min listen"
---

## Isn't This Just Politics?

**Ben:** Give it to me straight. You've written a whole record about managing stakeholders. Isn't that a polite word for office politics — the thing good engineers are supposed to be too busy building for?

**Ana:** That framing is exactly what the record exists to kill. A platform team does not set its own budget, grant its own mandate, or vote on its own survival in a downturn. Those decisions are made by people outside the team, based on what they believe about it. Managing those beliefs deliberately isn't a distraction from platform work — it's the part of platform work that keeps the rest funded.

**Ben:** But "managing beliefs" sounds like spin. If the platform is good, won't the work speak for itself?

**Ana:** It matters enormously whether your team is considered indispensable or "nice to have," and whether a powerful stakeholder strongly dislikes you — that's Fournier and Nowland's blunt framing, and no amount of good engineering answers those questions by itself. And most of what looks like politics is just perspective. When a stakeholder disagrees with me, they're usually optimizing for a different part of the business, not playing games. Understanding their goals, pressures, and incentives is the job.

**Ben:** Fine, but every leader already talks to stakeholders. What does this record actually change?

**Ana:** It changes *when* the work happens. The load-bearing idea is an asymmetry: trust is built in the calm and spent in the storm. The moment you need a stakeholder's goodwill — an escalation, an incident, a budget review — is precisely the moment you can no longer build it. Every discipline in the record is cheap when things are calm and decisive when they're not.

## The Grid

**Ben:** You map people on a power–interest grid. That feels cold. Reducing colleagues to quadrants?

**Ana:** It's the opposite of cold — it's honest about scarcity. An earnest leader tries to keep every stakeholder equally happy and ends up with a meeting cadence that cannot scale and no deep relationships anywhere. That's the flat-cadence anti-pattern: identical 1:1s with everyone until the calendar collapses and the important relationships get the same scraps as the unimportant ones.

**Ben:** So who gets the time?

**Ana:** High power, high interest — manage closely, roughly monthly 1:1s. High power, low interest — keep satisfied, quarterly. Low power, high interest — keep informed. Low power, low interest — monitor. And when individual 1:1s stop scaling, an interlock forum or advisory board. The point isn't the labels; it's that relationship time flows deliberately instead of to whoever shouts loudest.

**Ben:** And the grid you drew last year?

**Ana:** Is a wrong map. Reorganizations and shifting priorities move people between quadrants. Relationship time allocated by last year's map is misallocated — so the map gets revisited, including the informal one: who has the ear of senior leadership, which teams are considered indispensable, who's loudest and most respected.

**Ben:** Here's my sharper objection. All this pre-crisis relationship-building — how do you know it pays off? It's cost now for a hypothetical later.

**Ana:** Ask anyone who's lived the escalation-day introduction: meeting a powerful stakeholder for the first time in the meeting where they're already angry. The relationship needed to defuse that escalation was never built, and it cannot be built in that room. That's the whole asymmetry made concrete. The record's revisit condition even names it — if an escalation reaches senior leadership from a stakeholder we had no active relationship with, the model failed and gets rewritten.

## Talking at the Right Altitude

**Ben:** Let's talk communication. Engineers are told to be transparent. You seem to be saying — send less?

**Ana:** Send the right altitude. Decide the takeaway first, then lead with outcomes, impact, risks, decisions, and next steps. Detail on request. Over-communication has the same failure mode as silence: when everything is sent, the important signal is lost. That's the firehose update — mistaking volume for transparency. And a stakeholder drowning in operational detail is being invited to micromanage.

**Ben:** But when a stakeholder loses confidence, the instinct is to show them the architecture. Prove the system is sound.

**Ana:** And it never works. Stakeholders don't distrust a platform because they lack diagrams, and no quantity of engineering detail repairs a relationship problem. A confidence problem needs outcomes and owners, not a deep-dive. Make the business impact visible rather than assuming it's understood — this connects straight to [[what-is-platform-engineering]]: the framing stakeholders need starts from why the platform exists at all.

**Ben:** What about when things are going badly? The temptation is to go quiet until you have good news.

**Ana:** The record says the opposite: turn communication up when reliability, delivery, cost, or confidence deteriorates — and keep it up until the rough patch has genuinely passed. What's happening, what's being done, owners, timelines, next update. Operational rough patches are exactly what [[operating-platforms]] deals with, and this discipline is written for those moments. Hiding problems behind a polished summary is how transparency dies precisely when it's worth most.

## The Promise That Nobody Wrote Down

**Ben:** Now the commitment tracking — private notes, written follow-ups, reviewing what's outstanding. Honestly, it sounds bureaucratic. Do I need a ledger to have a conversation?

**Ana:** A private note and a short follow-up are enough — the record explicitly rejects bureaucratizing every conversation. But think about the uncaptured promise: a corridor "we'll look into it" that the stakeholder remembers as a commitment and the team never heard about. Six months later that's not a misunderstanding, it's evidence you don't keep your word. The written follow-up also invites correction — the stakeholder gets to fix your understanding before it hardens into a broken promise.

**Ben:** And the loop-closing?

**Ana:** Review outstanding commitments regularly, and close the loop when work completes, slips, or changes. Concretely: for every important stakeholder I can name what they care about, when we last spoke, and what I currently owe them. Commitments live in writing, not in memory.

## Yes, No, and Not Yet

**Ben:** Let's get to the hard part. A powerful stakeholder wants something that isn't on your roadmap. The realist in me says: you'll say yes. Everyone says yes to power.

**Ana:** And that's the soft yes — accepting every request to avoid conflict, then failing to deliver on the accumulated pile. It converts short-term comfort into long-term distrust. A platform that never says no is a feature factory with no strategy. But the defensive no is just as destructive — that's the fortress. The record's alternative is structure.

**Ben:** Which means what, mechanically?

**Ana:** First, understand the underlying business need — without assuming the existing roadmap is automatically right. Then look for the yes with compromises: a smaller first version that solves the most important need, limited scope, negotiated timing, maybe contributed engineering effort from the requesting team, with explicit boundaries of what is and isn't included. The planning mechanics behind those trade-offs live in [[planning-and-delivery]]; this record governs how they're negotiated.

**Ben:** And when the answer really is no?

**Ana:** Then say whether it's *no* or *not yet*, explain the constraint in the stakeholder's terms, and offer an alternative. A no delivered that way is a disagreement about priorities, not a rejection of the person — and it survives. One more rule: if a request is technically infeasible, say so. Dressing an impossibility up as "not prioritized this quarter" — the disguised no — just buys the same fight next quarter.

**Ben:** And if you don't have the authority to make the no stick?

**Ana:** Escalate for backup. Asking your manager to help hold a line is not weakness; it's how the line holds without the relationship breaking.

## Shadow Platforms and the Budget Storm

**Ben:** Suppose you discover another team quietly building its own version of your platform. Turf violation? Most leaders would fight it.

**Ana:** And lose the early-warning signal and the relationship in one move. A shadow platform is feedback, not treason. Something drove it — urgency my platform couldn't meet, novel demand, poor collaboration, cost disagreement, or engineers who simply want to build. Each driver has a different right response: partner, learn, absorb, occasionally clean up. None of them is reflexive suppression.

**Ben:** Last storm, then: the budget review. The CFO wants cuts. What does prepared look like?

**Ana:** Three things, all done in advance. Work grouped into team-sized chunks leadership can actually evaluate — not person-by-person activity lists with false precision. Platform work connected to protected business outcomes, because roadmaps alone won't justify the team in a downturn. And my own cut proposal, ready before executives make one for me. Budget-season passivity — walking in with a roadmap and hope — is how you lose the work that mattered most. Defending every project equally reads as not understanding the seriousness of the situation.

**Ben:** That's a grim exercise to run when nothing's wrong.

**Ana:** It's the cheapest insurance the record buys. At any moment — not just in budget season — I can answer: what would I protect, reduce, or stop if the budget tightened tomorrow?

## What This Record Is Not

**Ben:** Close it out. What are you explicitly not claiming?

**Ana:** Three boundaries. This is not the product discipline — discovering what customers need and shaping the roadmap is [[platform-as-a-product]]; this record covers the relationships and negotiations around that roadmap. It's not planning mechanics — those live in [[planning-and-delivery]]. And it's not a communication style guide — the postures and disciplines are fixed, but templates and update formats stay team choices.

**Ben:** And when do you revisit it?

**Ana:** If an escalation arrives from a stakeholder we had no relationship with, if uncaptured commitments keep surfacing, or if a budget cycle catches us without a defensible view of what to protect, reduce, or stop. Those are the three ways the calm work turns out not to have been done. The whole record in one line: build the relationships, capture the commitments, and know your own cuts — before the storm, because during it is too late.
