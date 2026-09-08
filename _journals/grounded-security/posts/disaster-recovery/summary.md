---
timetoread: "2 min read"
---

My organization's disaster recovery starts from the business, not from the backup tool. Every critical system carries an **RPO and RTO that business owners agreed to and someone priced**; the recovery strategy is chosen per system against those targets; dependencies are mapped so no application promises a recovery time its authentication service cannot meet; failover and failback have documented steps and named authority; and the plan is tested without leaning on systems the disaster would have taken out — security controls intact throughout. The test: backups are proven by restoring them, and recovery is proven within the RTO — a backup that has never been restored is a hope, not a plan.

**What changes**

* **Recovery targets become business decisions.** Each critical system gets an RPO and RTO driven by business requirements, the cost of meeting each target is reviewed, business owners sign, and systems are ranked by impact — so the recovery order is decided before the disaster, not during it.
* **Strategy is fitted per system.** Physical backups (transport and restore time counted honestly into the RTO), warm standby, high availability with real spare capacity, alternate systems, and function reassignment each buy exactly the speed a system's targets demand; cloud-native recovery replicates across regions and rebuilds environments through verified infrastructure-as-code, with costs understood in normal and disaster modes.
* **Dependencies stop being surprises.** Network, DNS, identity, database, storage, and third-party dependencies are mapped, their RPO/RTO compatibility confirmed, and unrealistic promises corrected — a system's real RTO is the RTO of its slowest dependency.
* **Failover and failback become procedures.** Clear declaration criteria, named activation authority, exact steps with named actors, an emergency communication plan — and a failback path synchronized, approved, verified, and communicated with the same rigor.
* **Testing becomes honest.** Tabletop and technical exercises run without systems the simulated disaster would have removed; restores are performed, not assumed; RTO and RPO verified; every test debriefed into owned, deadlined corrective actions; major changes retested.
* **Security holds through the disaster.** Backup data carries production-comparable controls, replication is encrypted and authenticated, recovery systems stay patched and aligned, access stays least-privilege, and emergency access is revoked afterwards.

**What it costs**

* Standing spend on standby environments, replication, and secondary-site security — priced per system rather than avoided or gold-plated.
* Recurring test, restore, and debrief work; the plan is maintained, not filed.
* Business owners' time: targets, priorities, and periodic reviews need their signature, not IT's guess.

**What we are not doing**

* Not giving every system an aggressive target — tolerating slow recovery is a legitimate, priced decision.
* Not handling the live-adversary fight here — that is [[incident-response]]; ransomware hands off from there to this plan.
* Not defining the cloud platform or physical-site bar here — those live in [[cloud-infrastructure]] and [[physical-security]].

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries all fifteen sections from objectives to ongoing review. Grounded in the Disaster Recovery chapter of the* Defensive Security Handbook*.*
