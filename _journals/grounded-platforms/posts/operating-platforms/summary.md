---
timetoread: "2 min read"
---

Operational work is a core part of platform engineering in my organization, not an interruption to it: the engineers who build a platform operate it. Every platform team owns three practices — on-call, user support, and operational feedback — and operational load is a managed quantity with explicit numbers, because a platform whose operational load is unmeasured is a platform whose stability is unmanaged.

**What changes**

* **On-call is a merged DevOps rotation** with 24×7 coverage where the business needs it — software developers and systems engineers together, with enough platform expertise to diagnose issues across internal code, OSS, vendors, and integrations. No handing the pager to a separate ops team that can only escalate.
* **On-call load has hard numbers**: each engineer on-call at most one week in four (ideally one in six to eight), and fewer than five meaningful pages per engineer per week. A sustained breach is treated as a platform-stability problem — stability work then outranks new features. Alerts stay tied to business impact, false alarms are hunted down, and fairness comes before compensation: extra pay never substitutes for fixing unsustainable load.
* **Support is structured and separated.** Requests are categorized with defined service levels and a crisp critical-incident definition; noncritical support moves to a business-hours rotation so real incidents stay on the pager. Engineers keep hearing users directly — repeated questions are product and documentation signals, not noise to route away.
* **Operational signals close the loop.** A handful of meaningful customer-facing SLOs (with broader internal ones), change management on every production change until automation earns trust, synthetic monitoring that catches failures before customers report them, and weekly plus organization-level operational reviews that actually change engineering priorities.

**What it costs**

* Platform engineers carry the pager and do support — that is the price of the fastest diagnosis and the strongest product signal, and the load limits exist to keep it sustainable.
* When the on-call numbers breach, feature work yields to stability work; when operations consume roughly half of engineering capacity, staffing is reassessed rather than absorbed.
* SLO discipline, synthetic monitoring, and the review cadence take real, ongoing engineering capacity — reviews that change nothing are process theater, and we refuse them.

**What we are not doing**

* Not restating [[platform-as-a-product]] — that record treats reliability as part of the product promise; this one is the operational machinery that keeps it.
* Not the staffing model — support specialists appear here only as a scaling move; the full hiring picture lives in [[building-platform-teams]].
* Not an incident-management runbook or a tooling guide — this record sets the practices and the limits, not the pager vendor.

*The Article tab carries the rationale and anti-patterns; the Checklist tab is the runnable version — on-call limits, support levels, SLO discipline, review cadence, and the quick health check.*
