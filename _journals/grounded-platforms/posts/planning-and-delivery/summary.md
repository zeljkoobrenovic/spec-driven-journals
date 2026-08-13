---
timetoread: "2 min read"
---

Platform planning is honest capacity accounting, and platform delivery is honest communication about what that capacity produced. In my organization no long-running project starts without a written proposal that nails the problem, the options, and what "done" looks like; the roadmap is built bottom-up from all four real consumers of capacity; and launch is not the finish line — adoption is.

**What changes**

* **Proposals gate long projects.** Before a long-running project starts: current situation, constraints, the problem being solved, realistic options with trade-offs, the chosen solution and why, a measurable definition of "done" — and buy-in from engineering leads, product, and stakeholders secured before the first commit, not discovered at launch.
* **The roadmap admits all four kinds of work.** Features, KTLO (keep the lights on), mandates from leadership, and system improvements all appear in the plan, because a plan that only lists features is a plan to disappoint. KTLO is estimated from historical data and capped near 40% of capacity — breach the cap and burden-reduction work jumps the queue. Mandates are listed and costed separately, with early escalation when the load exceeds realistic capacity.
* **Heuristics keep the plan honest, not entitled.** Roughly 70/20/10 across core work, adjacent innovation, and transformation — as a discussion tool; system-improvement projects near three developer-months; real slack for the unplanned.
* **Adoption is project work.** Long projects break into value-bearing milestones — monthly in the first year, quarterly later — with migration, testing, enablement, and adoption metrics inside the milestone plan. Launch is a milestone, not the goal.
* **Delivery is narrated.** Biweekly wins and challenges — short bold summary, then situation, action, result — rewritten for the audience that reads them, focused on outcomes rather than ticket counts, with challenges treated as useful information rather than confessions.

**What it costs**

* Writing and reviewing proposals slows the start of long projects — deliberately; that friction is cheap insurance against multi-year projects that were never quite about anything.
* Honest accounting means telling stakeholders that features get only the capacity left after KTLO, mandates, and improvements — a smaller, truer number than a feature-only plan promises.
* The wins-and-challenges rhythm is real recurring work for managers, and it is retired or reshaped the moment it degrades into bureaucracy nobody reads.

**What we are not doing**

* Not deciding what to build — direction comes from [[platform-as-a-product]]; this record turns direction into a plan that survives contact with capacity.
* Not the operating model behind the KTLO line — on-call, support, and incident response live in [[operating-platforms]].
* Not the special case of foundational rewrites — [[rearchitecting-platforms]] inherits this discipline and adds its own gates. And not a project-management methodology: no sprint mechanics, no estimation poker, no tooling prescriptions.

*The Article tab carries the rationale and anti-patterns; the Checklist tab is the runnable version — proposal review, roadmap construction, KTLO estimation, and the wins-and-challenges process.*
