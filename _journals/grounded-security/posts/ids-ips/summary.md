---
timetoread: "2 min read"
---

My organization treats intrusion detection as a capability it operates, not a product it bought. **An IDS detects, logs, and alerts; an IPS detects and actively blocks** — and the two are governed separately, with blocking enabled only where false positives are understood. Coverage is layered across network sensors, host monitoring, honeypots, and cloud-native detection; placement follows the threat model; encrypted traffic is named honestly as a visibility limit; and tuning is standing work. The test the layer is held to: logs and alerts only provide value when someone reviews them and knows how to respond.

**What changes**

* **Detection and prevention are held apart.** Visibility and alerting come first, everywhere it matters; inline blocking is a separate, deliberate step taken only where traffic is well understood — because an IDS false positive costs an analyst minutes while an IPS false positive blocks legitimate business in real time.
* **Coverage becomes layered by design.** Network sensors (Snort, Suricata, or Zeek, chosen per environment) watch the wire; host-based monitoring with file integrity checking and queryable endpoint state watches what the network cannot see; isolated, monitored honeypots provide cheap high-signal tripwires; each layer covers another's blind spot.
* **Placement becomes a threat-model decision.** Sensors sit at choke points — internet edge, DMZ, and crucially the interior, because perimeter-only monitoring misses lateral movement. The question "which traffic can none of our sensors see?" is asked before an incident asks it for us.
* **Alert management becomes engineering.** Noisy rules are tuned — thresholds, ranges, exclusions — or demoted to log-only, never simply disabled; low-priority events are logged rather than alerted; alert fatigue is treated as a pipeline defect, not analyst weakness; every alert queue has a named owner.
* **Cloud detection adapts to cloud dynamics.** Monitoring integrates with orchestration and workload lifecycles, and the provider-native services — GuardDuty and CloudTrail, Defender and Sentinel, Event Threat Detection and Security Command Center — are put to work rather than replicated around.

**What it costs**

* Internal and DMZ sensor coverage, not just the perimeter — more monitoring points, more traffic to process.
* Continuous tuning is standing work; the alert pipeline is never "done."
* SSL/TLS inspection, where chosen, carries performance overhead and privacy, compliance, and legal weight that must be deliberately accepted.

**What we are not doing**

* Not enabling automatic blocking by default — prevention is earned per traffic class, not switched on at install.
* Not mandating tools — Snort, Suricata, Zeek, and OSSEC are the chapter's worked examples; the commitments are capability-level.
* Not building the log pipeline or the response process here — collection and correlation live in [[logging-and-monitoring]], and what happens after a real alert lives in [[incident-response]].

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the full working checklist, from IDS/IPS concepts through placement, tuning, and encrypted traffic. Grounded in the Understanding IDSs and IPSs chapter of the* Defensive Security Handbook*.*
