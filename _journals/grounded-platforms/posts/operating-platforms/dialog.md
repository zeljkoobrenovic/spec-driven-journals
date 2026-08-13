---
timetoread: "8 min listen"
---

## Why the Builders Carry the Pager

**Ben:** Give me the blunt version. Every engineering leader says "operations matters." Why does this need to be a record with numbers in it, rather than a poster on the wall?

**Ana:** Because the poster version is exactly what fails. The record says operational work is a core part of platform engineering — not an interruption to it — and then it puts numbers on that claim so nobody can quietly walk it back. Three practices every platform team owns: on-call, user support, and operational feedback. And one rule about limits: operational load is measured and bounded. A platform whose operational load is unmeasured is a platform whose stability is unmanaged.

**Ben:** Start with on-call, then, because that's where I'd push back first. Why should the engineers who build the platform also carry the pager? The whole industry built SRE teams precisely so builders could build.

**Ana:** Platform failures cross layers — that's the core of it. An incident might live in our internal code, in an OSS dependency, in a vendor system, or in the seams between them. A separate operations team without deep platform context can't diagnose across those layers; it can only escalate. So you've added a hop of latency to every single incident and learned nothing. The merged DevOps rotation — software developers and systems engineers in the same rotation — shortens diagnosis, and it does something subtler: the pain of operating bad software lands on the people best positioned to fix it.

**Ben:** That sounds noble until it's 3 a.m. for the fourth night running. Engineers burn out on pagers. Isn't the humane move to shield them?

**Ana:** The humane move is to bound the load, not to relocate it. That's why the numbers exist: each engineer on-call at most one week in four, ideally one in six to eight, and fewer than five meaningful pages per engineer per week. Those aren't aspirations — they're tripwires.

**Ben:** And when a team blows through five pages a week? Because they will.

**Ana:** Then we've learned something important: that team is not understaffed for on-call, it's operating an unstable platform. The breach is a platform-stability problem, and stability work then outranks new features. That reframe is the whole discipline.

## The Pager Is a Stability Metric

**Ben:** Here's the cheaper fix every company reaches for: pay people more for on-call. Compensate the pain. What's wrong with that?

**Ana:** It treats the symptom and preserves the disease. The record is explicit — fairness first means reducing unnecessary after-hours work before compensating for it. Extra pay is never a substitute for fixing unsustainable load. If you pay people to absorb a broken pager, you've bought yourself a dashboard that says everything is fine while the platform rots underneath it.

**Ben:** What about a secondary rotation? Put a second layer in front of the team to soak up the noise.

**Ana:** Depends what the secondary does. A secondary that exists only to forward pages to the primary team is latency dressed up as coverage — we avoid those. What we do instead is attack the noise itself: hunt down false alarms, review noisy alerts after deployments and batch jobs, keep every alert tied to real customer or business impact. Alerts have to earn their noise.

**Ben:** Okay, one more on this thread. Five pages a week, one week in four — those numbers came out of a book. Why should I trust them in my organization?

**Ana:** Because their function isn't precision, it's forcing measurement. The record grounds them in Fournier and Nowland's *Platform Engineering*, and the point is diagnostic: any team that can state its pages-per-engineer-per-week number is a team whose stability is being managed. A team that can't state the number is the actual problem, whatever the number would have been.

## Support Is a Sensor, Not a Tax

**Ben:** Let's do support. My instinct — and I think most managers' instinct — is to route support away from engineers so they can focus on real work. You're telling me that's wrong?

**Ana:** Exactly wrong, and it's the anti-pattern I'd flag first. Support is where usability problems, confusing abstractions, and missing capabilities announce themselves. A repeated support question is a documentation or product defect with a name and a frequency. Shield engineers completely and nobody who builds the platform has heard a user question in months — empathy, usability signal, and product insight quietly die.

**Ben:** But unstructured support is a nightmare. Engineers drowning in "how do I" questions while real incidents wait.

**Ana:** Which is why the record structures it instead of routing it away. Requests get categorized — production troubleshooting, bugs, help using the platform, feature requests, reviews, design questions — with defined service levels, a crisp definition of what counts as a critical incident, and clarity on when users may actually page the team. Urgency is tied to business impact, not to how loudly someone asks.

**Ben:** And the pager question — does a help request ride the same channel as an outage?

**Ana:** No, and that separation is load-bearing. When help requests and pages share a channel, one of two things happens: everything becomes urgent and the rotation burns, or nothing is urgent and real incidents drown in questions. So critical after-hours incidents stay on the on-call rotation, and noncritical volume moves to a business-hours support rotation. Both are tracked, because the total matters: when operational work consumes roughly half of engineering capacity, we reassess staffing rather than quietly absorbing it.

**Ben:** Reassess how? Hire support specialists? Because that sounds like the shielding you just argued against.

**Ana:** It's a scaling move, not a shield — the distinction is whether feedback keeps flowing. Support specialists, coverage for distant time zones, even a Tier 1 support organization at real scale — all legitimate. But engineers keep hearing users directly, and even Tier 1 runs regular feedback sessions back to the platform team. The failure mode isn't specialists existing; it's specialists becoming a wall. And the standing rule everywhere: eliminate repeated questions — convert them into documentation, diagnostics, or product changes — rather than answering the same one every week forever.

## Closing the Loop

**Ben:** Third practice — operational feedback. Honestly, this is where I expect the least. Every org has SLO dashboards and weekly ops reviews, and most of them are wallpaper.

**Ana:** Most of them are wallpaper because they optimize for coverage instead of meaning. The record goes the other way: a handful of meaningful customer-facing SLOs — few enough that a breach actually alarms someone — with broader internal SLOs for coverage underneath. SLO sprawl is an anti-pattern by name: dozens of customer-facing SLOs, each individually defensible, collectively hiding whether the platform is healthy.

**Ben:** And how do you find out you're failing before a user files a ticket?

**Ana:** Synthetic monitoring that exercises end-to-end customer workflows — not individual components, whole journeys — so failures surface before customers report them. Plus change management on every production change, documented, reviewed, and tested. That one's scaffolding, not permanent bureaucracy: it holds until safe automation is mature enough to earn trust.

**Ben:** So walk me through the review that supposedly isn't theater.

**Ana:** A lightweight weekly operational review per team — thirty to sixty minutes over pages, support issues, postmortems, production changes, and the SLOs — plus organization-level reviews of the highest-impact incidents, with leaders actually in the room. The test isn't whether the meeting happens; it's whether it changes anything. Postmortem actions tracked to completion, recurring pages investigated to root cause, support trends turned into engineering priorities. Every platform team here should be able to point to an engineering priority that operational feedback changed this quarter. A review that never changes a priority is process theater — rigor's costume without its function — and we'd rather kill the meeting than keep the costume.

**Ben:** Close it out. What is this record *not* claiming? Because "the builders operate it" could be read as "no ops help, ever, for anyone."

**Ana:** Three boundaries. This isn't [[platform-as-a-product]] — that record makes reliability part of the product promise; this one is the operational machinery that keeps the promise. It isn't the staffing model — support specialists show up here only as a scaling move, and the full hiring picture lives in [[building-platform-teams]]. And it isn't an incident-management runbook or a tooling guide — it sets the practices and the limits, not the pager vendor. As for revisiting: if pager load stays above five meaningful pages a week for more than a quarter despite stability work, or reviews stop changing priorities, the record itself goes back on the table.

**Ben:** One sentence, for the leader skimming this.

**Ana:** Measure the operational load, bound it, and treat every breach as the platform telling you where to invest next — the pager is a stability metric wearing a beeper.
