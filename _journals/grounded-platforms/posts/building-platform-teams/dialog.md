---
timetoread: "8 min listen"
---

## Why Composition Comes First

**Ben:** Straight question. I need a platform team; there are strong engineers on the market. Why isn't this just "hire good people and get out of the way"?

**Ana:** Because platform teams fail from imbalance more often than from lack of talent. That's the central observation in Fournier and Nowland's chapter. Platform work has two ingredients — building software and operating systems — and they come with different instincts. A team dominated by either instinct develops a characteristic pathology. So composition is the first decision, not an emergent property of whoever happened to apply.

**Ben:** "Characteristic pathology" — go on. What does a team of pure operations instincts actually look like?

**Ana:** The "too much systems" culture. Years of automation, templates, one-off tools, and an ever-growing rulebook of manual process. Busy work that manages complexity without ever removing it. Glue that never becomes a platform. And there's a sharp tell: watch what happens when something breaks. A platform team improves the platform. A glue team blames the user.

**Ben:** And the mirror image?

**Ana:** The "too much development" culture — architecture nobody can operate. Maintenance is beneath the team, technical debt is "someone else's code", reliability is a tax on the interesting work. A platform is a promise that other teams can build on, and a team that prioritizes new architecture over keeping that promise is spending its customers' trust to entertain itself.

**Ben:** So the fix is a fifty-fifty org chart? That sounds mechanical.

**Ana:** The fix is a deliberate mix — people who can write substantial production code alongside people with broad systems and operational expertise — plus one cultural rule that does most of the work: both kinds of work are treated as equally valuable. The moment one becomes the prestige track, the team starts losing the other. That's prestige-track drift: quietly reward feature development over operational work and every systems engineer either converts or leaves.

## Specialists, Reliability, and the Need Bar

**Ben:** What about depth? Real platforms hit networking, storage, performance problems. Shouldn't I stock up on specialists while I can get them?

**Ana:** That's the specialist zoo — deep experts hired speculatively, far from the systems that need them, unable to contribute outside their specialty. Headcount spent on depth nobody asked for. The rule is demonstrated need: specialists stay few, stay close to the systems that need them, and contribute beyond their specialty.

**Ben:** Same for reliability? Everyone slaps "SRE" on the job ads now.

**Ana:** And that's the failure — "reliability engineer" as a relabeling of whoever does systems work. In this record, reliability engineering is a specialized role with a clear mandate and real reach, added where reliability is a genuine organizational need. Not a catch-all label.

**Ben:** And the need bar applies beyond engineers, I take it.

**Ana:** All the way up. Platform-aware PMs when the platform is big enough — product-minded and staff engineers fill the gap before that. TPMs only when coordination complexity genuinely requires them. Developer advocates, technical writers, support engineers — same bar. The anti-pattern there is the disconnected evangelist: an internal advocate role with no delivery responsibility, whose influence evaporates because it costs nothing.

## Interviewing for the Actual Job

**Ben:** Let me push on hiring. We have a calibrated interview loop that works — algorithms, application design, behavioral. Why can't platform candidates go through the same pipeline?

**Ana:** Because a standard loop selects for the wrong job. Borrow application engineering's loop — abstract coding plus application design — and it will happily pass candidates who can't do platform work and fail candidates who excel at it. Then you wonder why the new hires can't operate anything.

**Ben:** So what does the platform loop look like?

**Ana:** It mirrors the job. Platform design, not only application design. An inverted design interview — the candidate walks through a real system they built and defends its tradeoffs, which you can't fake with rehearsed patterns. Coding exercises that open conversations about testing, error handling, observability, scaling. A behavioral round on incidents and ambiguity — staying effective when things are on fire. And customer empathy assessed explicitly.

**Ben:** Empathy in an interview loop sounds soft. How do you actually test it?

**Ana:** With evidence, not vibes. Has the candidate helped users understand a system? Changed what they built because of feedback? Can they absorb a frustrated user without turning dismissive? It matters because a platform team's users are engineers, which tempts platform engineers to treat them as peers who should simply read the code. A users-are-the-problem culture loses its customers to shadow platforms no matter how good its technology is. Internal users are customers, full stop.

**Ben:** One caution on bespoke loops, though — doesn't customization make interviews inconsistent?

**Ana:** If you skip the discipline, yes. That's why interviewers are trained and calibrated before the format ships. A bespoke loop run inconsistently is worse than a generic one.

## Ladders, Promotion, and What Gets Rewarded

**Ben:** Now the part nobody wants to touch: careers. If systems generalists are so valuable, don't they need their own ladder? Their own level matrix, their own hiring standard?

**Ana:** Tempting, and mostly wrong. A ladder per specialty fragments evaluation until no one can compare impact across the team. Ladders stay shared where practical — with at most one systems-oriented addition if truly needed. What changes is the evidence, not the ladder: promotion cases built from adopted tools, high-quality customer interactions, incident leadership, reduced operational burden.

**Ben:** Because if the evidence is lines of code and launches —

**Ana:** — engineers rationally abandon support, operations, and usability. Which is exactly the work the platform's customers feel most. Careers must reward what the platform needs, or the team will stop doing it. And broad systems engineers get a path that lets them stay broad — no forced specialization to earn a promotion.

**Ben:** What about the managers running all this?

**Ana:** Same logic one level up. Managers who have operated business-critical systems, who defend a deliberate delivery pace with business criticality and risk rather than apologizing for it, and who know when to inspect and when to trust. And balance itself is an explicit leadership responsibility: one shared roadmap, consolidated prioritization across development and operational work, no "software versus operations" split inside the team — and partner teams appreciated publicly, never blamed.

## What This Record Doesn't Cover

**Ben:** Close it out. What is this record explicitly not doing?

**Ana:** Four boundaries. It doesn't decide when a platform team is justified or what it does first — that's [[getting-started]]. It doesn't define the operational discipline itself — that's [[operating-platforms]]; this record staffs the team so it can carry that discipline. It's not the full product operating mode — that's [[platform-as-a-product]]; here I only cover the product roles and product-minded staffing that support it. And it's not a compensation or leveling policy — ladders and pay bands stay with the wider organization; this record only constrains how platform work is evaluated within them.

**Ben:** And the revisit conditions? What tells you the staffing model is drifting?

**Ana:** Three signals, one per failure mode. If the team's output drifts toward scripts and glue rather than a real platform product — the "too much systems" signal. If operational work stops appearing in promotion cases — that's "too much development" reaching the ladder. And if support interactions show a team blaming its users instead of improving the platform. The concrete test for any team I'm accountable for: I can point at people who write substantial production code, people who can operate and debug complex systems, and evidence that both get promoted. When a user struggles, the default response is a platform improvement — not a lecture.
