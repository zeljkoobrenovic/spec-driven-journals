---
timetoread: "2 min read"
---

A platform rearchitecture is a business investment, not a technical adventure, and I gate it like one. It starts only when the current architecture genuinely constrains feature delivery, reliability, security, or efficiency; it is planned on a 3–5-year horizon but must put something valuable into production every 12 months; and it is stopped, revised, or delayed without shame when the evidence no longer supports the hypothesis.

**What changes**

* **Four gates govern every rearchitecture**: a genuine constraint that incremental improvement cannot fix, a full go/no-go review before work starts, a valuable production deliverable every 12 months, and an annual review with a real stop option.
* **Incremental beats "v2".** We rearchitect the platform in place unless there is a compelling, argued reason to build a separate system — and we never combine a new-product bet with a major redesign if it can be avoided. Maturity and mindset are matched first: scrappy, scalable, or robust platform; pioneer, settler, or town-planner moment.
* **Every phase carries three levels of success** — an audacious goal, a valuable fallback, and a production proof serving real load for a real customer — so the effort cannot have a zero year. Transition guardrails hold throughout: backward compatibility by default, strong testing, stable lower environments, gradual canary-style rollouts.
* **Migration costs are counted before commitment** — every user group that must move, the consumer teams' effort, dual-running, data migration, SDK and support work — and confirmed smaller than the expected business value. The build effort is the visible tip; migration is usually the larger half of the bill, paid by other people.
* **Security is built in by design and by default**: protections that do not depend on human behavior, hazards eliminated architecturally, and paved paths that make the safest option the easiest option.

**What it costs**

* Leadership commitment that survives reorganizations and changing priorities — approval in one budget meeting is not commitment; protection is the test. If the case is not yet strong, we wait.
* Staffing keeps long-tenured context in the loop rather than handing the rewrite to enthusiastic new hires; ownership transfers only after the relationship is built.
* The annual review means being genuinely willing to stop — sunk cost is never a reason to continue.

**What we are not doing**

* Not restating [[planning-and-delivery]] — the milestone and migration discipline is inherited from there; this record adds the extra gates a foundational rewrite demands.
* Not a technology-selection guide — the record constrains how OSS and vendor bets are evaluated (ecosystem trajectory, 5–10-year viability), not which technologies to pick.
* Not an application-rewrite playbook — the scope is platforms with a broad developer base and migration obligations.

*The Article tab carries the rationale and anti-patterns; the Checklist tab is the runnable version — the go/no-go review, architecture-goal worksheets, guardrails, and the annual review.*
