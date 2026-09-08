---
timetoread: "9 min listen"
---

## Storage or Capability

**Ben:** Let me open with the CFO's question, because someone has to. We already pay for a SIEM. The logs go in, the dashboard is green, the auditor is happy. What exactly is this record adding beyond "keep doing that, but with more ceremony"?

**Ana:** The record's opening claim is that what you just described might be storage, not capability. Logging exists to answer the questions an incident will ask — who touched this host, what did that process spawn, where did the data go — under time pressure, at three in the morning. A SIEM that ingests terabytes and answers none of those questions is a log warehouse with a security logo on it. The record's whole architecture follows from that: design from risk backwards, keep alerts actionable, and prove — don't assume — that detections fire.

**Ben:** "Design from risk backwards" sounds like consulting language. What does it mean on a Tuesday?

**Ana:** It means the first artifacts are not data pipelines. They're a coverage scope, the compliance requirements that constrain logging, a list of the organization's highest-risk and highest-value systems, and explicit use cases — the attacks the SIEM should detect, mapped to something like MITRE ATT&CK or the Cyber Kill Chain. Then collection follows the design: start with high-value log sources, expand over time. The chapter is refreshingly blunt that not every event is equally important — treating them as if they were is how you get a SIEM that is expensive, slow, and unread.

**Ben:** But every incident retrospective ever written says "if only we'd kept those logs." Doesn't collect-less mean answer-less later?

**Ana:** That tension is real, and the record makes it a conscious decision instead of an accident. Storage, indexing, transmission, and licensing all scale with volume; analyst attention scales with none of them. So the collect-all-versus-collect-needed question gets decided deliberately, against cost, and written down — there's a Record of Authority defining where logs are stored and for how long. You can absolutely decide to keep more of something cheap and quiet. What you can't do is drift into a default and call it a strategy. And one thing is non-negotiable: logs are stored centrally, not only on the systems that generate them, because attackers delete local logs. Evidence that lives solely on the compromised host is evidence held by the adversary.

## The Alert Someone Can Act On

**Ben:** Alerting. Every SOC I've seen drowns. Hundreds of alerts a day, analysts bulk-acknowledging. Your record says "keep alerts focused, useful, and actionable" — everyone says that. What's the enforcement mechanism?

**Ana:** The chapter's closing requirement, which I think is the sharpest line in it: analysts know how to investigate every alert that is enabled. That's a testable bar. Pick any alert in the console and ask, "when this fires, what does the analyst do?" No answer means the alert either gets a playbook or gets disabled. An alert nobody can investigate is noise with a severity label — and alert fatigue isn't an annoyance, it's the actual mechanism by which real intrusions scroll past unread.

**Ben:** And the opposite failure? Quiet dashboards that are quiet because nothing is being detected?

**Ana:** The record hunts both directions. False positives get tuned down — and consistently noisy rules get removed or fixed, not tolerated. False negatives get actively tested: reproduce known suspicious behavior and check whether anything noticed. Plus the audit layer — verify expected events are actually being logged, check all endpoints are sending, compare log volume against historical baselines. A volume drop nobody investigates usually means a third of the fleet silently stopped reporting months ago.

## Following the Attacker's Path

**Ben:** The coverage list is enormous — Windows internals, authentication, applications, three cloud providers, databases, DNS, EDR, IDS, proxies, account changes. Is this "log everything" sneaking back in through the side door?

**Ana:** No — it's breadth of *domains*, not volume of everything. The list mirrors how an intrusion actually moves: a phished credential shows up in authentication logs, a payload as a process creation on an endpoint, its callout as a DNS query to a strange domain, lateral movement in network connections, escalation as an addition to Domain Admins, exfiltration as an unusually large database query and a long low-bandwidth outbound connection. Each domain is a place the attack becomes visible. A gap in any one of them is a corridor the attacker walks down unrecorded — every other camera can be perfect and you still lose the trail.

**Ben:** You keep bringing up DNS. Why does name resolution deserve its own monitoring section?

**Ana:** Because nearly everything an attacker does resolves a name first — command-and-control, exfiltration endpoints, staging domains. That makes DNS one of the cheapest, widest sensors the organization owns. The record wants queries and responses logged with enough context to tie them to the right endpoint, and endpoint telemetry that associates DNS requests with the originating process — checked for malicious domains, C2 patterns, and the algorithmically generated domains malware uses.

**Ben:** And cloud? The providers log plenty on their own.

**Ana:** They log — for their half of the shared-responsibility model, with their default retention, in their console. The record's requirements: understand that model, ensure administrative and API activity is actually logged, centralize cloud logs with the rest of the monitoring environment, retain them appropriately, and alert on unexpected configuration and access changes. The anti-pattern is discovering during an incident that the audit trail you assumed existed expired under a default setting nobody read.

## Proving It Fires

**Ben:** Now the part I find most suspicious: "detections are tested, not trusted." You install a respected ruleset, the vendor tested it, the community tested it. Why is my team re-testing someone else's rules?

**Ana:** Because community rules encode someone else's environment. Between "we forward those logs" and "we would catch that attack" sits a chain of silent failure modes — the event not logged because of a config default, the forwarder broken, the rule keyed to a path your systems don't use, the alert routed to a dead channel. The only way to know the chain works is to pull it: reproduce the malicious behavior in a controlled environment, confirm the log data appears, confirm the alert fires. The record applies that to every imported or newly created rule — Sigma rules included, which it otherwise likes as a portable format — and again after every major configuration or infrastructure change, because yesterday's confirmed detection quietly dies in today's migration.

**Ben:** That's a lot of standing work. Reproduce behaviors, tabletops, full logging audits, retests...

**Ana:** It is — and the record says to automate the repeatable tests where practical, which turns detection testing into something like CI for the SOC. The alternative isn't less work; it's the same discovery made during a real incident, at maximum cost. And this is where [[osint-purple-teaming]] connects: that record runs the same discipline end to end with a live red team, and its findings — the technique that generated no alert, the logs too thin to investigate — are precisely this estate's gap list.

**Ben:** Where does ATT&CK mapping fit? I've seen teams treat the matrix like a bingo card.

**Ana:** The record uses it for one thing: turning "we monitor a lot" into "here is what we cannot see." Map your important detections to tactics and techniques and the holes get names — then the next detection you build is the one covering the highest-risk uncovered technique, not the easiest one to write. The bingo-card failure is real, which is why the record anchors use cases in threat models built from the organization's actual significant risks, not in matrix completeness.

## The Estate That Decays

**Ben:** Last objection. Suppose we do all of it — designed, covered, tested. Are we done?

**Ana:** The SIEM decays by default — that's the record's final argument. New systems get added, software gets deployed, traffic patterns shift, threats evolve, and each change silently invalidates some detection or baseline. A SIEM tuned once at installation is a museum of the environment as it existed that quarter. So maintenance is the product: configuration reviewed regularly, detections updated with new systems and new threats, alerts retuned as normal behavior changes, noisy rules pruned, retention and capacity reviewed, every change documented, and coverage periodically reassessed against organizational risk.

**Ben:** All right. My concession: this record isn't about logging at all. It's about honesty — writing down what you chose to see, proving the alarm actually rings, and refusing to keep any alert you can't act on. The dashboards were never the point; the answers at three a.m. are.

**Ana:** That's the record. Design from risk, centralize the evidence, keep the alerts human-sized, and test the whole chain — because the worst hour is the wrong time to find out the cameras were off.
