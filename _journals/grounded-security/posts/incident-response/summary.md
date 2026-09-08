---
timetoread: "2 min read"
---

When my organization suspects a security incident, the response is a **practiced discipline, not an improvisation**. Preparation — definitions, roles, external contracts, forensic tooling — is finished in peacetime; suspected incidents are escalated early; declaration formally names an incident manager and starts the activity log; evidence is preserved before remediation destroys it; containment, eradication, and recovery are distinct, confirmed gates; communications run from one authoritative source; and no incident closes without a review whose corrective actions have owners and deadlines. The test: the engineer who suspects a compromise at 2 a.m. knows exactly whom to call — and is thanked for a false positive, never punished for escalating.

**What changes**

* **Preparation moves ahead of the incident.** What qualifies as an incident, severity levels, declaration authority, incident-manager candidates, communication roles, and contracts with external responders are all settled before anything burns — and logging retention, EDR coverage, isolation methods, and forensic tool access are verified in peacetime.
* **Escalation becomes cheap and fast.** Everyone knows how to report a suspicion, and the standing rule prefers an early false positive to a late certainty; the reporting culture, not the tooling, decides whether we learn of a breach in hours or months.
* **Every incident gets a commander and a log.** Formal declaration assigns an incident manager, records the start time, and opens the activity log; a war room with explicit decision authority, task owners, a scheduled update cadence, and shifts for long incidents replaces the swarm.
* **Evidence outranks the quick fix.** Original logs, snapshots, memory, and disk images are preserved — with hashes and chain of custody — before destructive remediation; investigation correlates logs, endpoints, disk, memory, and network into one timeline.
* **Containment, eradication, and recovery are gated.** Containment weighs attacker awareness and service impact; eradication removes persistence, rotates every exposed secret, rebuilds where trust cannot be restored, and hunts the compromise environment-wide; recovery restores from trusted sources, monitors closely, and needs explicit approval.
* **Every incident improves the program.** A blameless review shortly after closure produces a timeline, a root cause, and corrective actions with owners and deadlines, tracked to completion.

**What it costs**

* Standing peacetime investment: retained and tamper-protected logs, EDR coverage, pre-signed retainers with external specialists, and periodically tested forensic access.
* Evidence discipline slows the most tempting quick fixes — deliberately.
* Reviews, drills, and tabletop exercises are recurring work, not a one-time setup.

**What we are not doing**

* Not turning every escalation into a declared incident — validation and severity triage still gate declaration.
* Not running disaster recovery here — when destruction outruns infiltration, this record hands off to [[disaster-recovery]].
* Not covering the phishing on-ramp in depth — the everyone-reports culture for that lives in [[phishing-response]], and the telemetry this record presumes lives in [[logging-and-monitoring]].

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the full lifecycle from preparation to final verification. Grounded in the Incident Response chapter of the* Defensive Security Handbook*.*
