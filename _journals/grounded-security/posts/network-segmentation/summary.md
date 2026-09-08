---
timetoread: "2 min read"
---

Segmentation in my organization is **least privilege applied to traffic**: systems separated by risk, function, sensitivity, and business need, with default-deny between segments and every approved flow documented. Every other defense reduces the probability of compromise; segmentation reduces its price — the attacker who lands inside wins a compartment, not the estate. The test the design is held to, from the chapter's own final review: each segment can communicate only with the systems it legitimately needs, and prohibited traffic is proven blocked, not assumed.

**What changes**

* **Segments are designed, not inherited.** The topology and trust boundaries are documented and systems needing separation identified — dev/test apart from production, guests apart from corporate, regulated data in dedicated zones with extra monitoring mapped to PCI DSS and HIPAA where applicable.
* **Boundaries become default-deny.** Approved flows are documented allow-list style and pruned on review; ACLs are specific — source, destination, port, protocol — with no ANY-ANY rules; the DMZ admits only required inbound ports and cannot talk freely inward; VLANs are used with ACLs and hopping protections but never trusted as walls.
* **Admission is earned.** NAC and 802.1X authenticate devices and validate posture before the jack gives them anything; unknown and noncompliant devices land in quarantine; guests get captive-portal, internet-only access; vendor equipment is scanned before it touches production.
* **Remote access and applications get the same scoping.** VPN access exists on business need, reaches only required resources, and dies when the need does — split tunneling deliberately evaluated. Web tiers are separated from databases, TLS keys stay off public-facing servers, and tier-to-tier traffic is restricted to required ports.
* **People are segmented like packets.** Dev and prod responsibilities separated, transaction creation split from approval, RBAC with regular reviews, generic admin accounts disabled and alerted on, and administrators holding separate standard and privileged accounts.
* **The design is proven, continuously.** Boundary traffic is logged and flow-analyzed, configurations reviewed, diagrams kept current — and prohibited traffic is actually attempted and actually blocked, with the design reassessed whenever the business changes.

**What it costs**

* Real design and migration work upfront, and an approval path for new inter-segment flows that adds friction by intent — a defect to fix when slow, never a reason to flatten the network.
* The verification loop recurs: testing, rule pruning, and documentation are standing work, not a rollout.
* Some legitimate workflows get slower until their flows are documented — the price of an allow-list that means something.

**What we are not doing**

* Not hardening the firewalls and switches that enforce the boundaries — that is [[network-security]].
* Not building the detection layer that watches boundary traffic — that is [[ids-ips]].
* Not prescribing a topology, zone count, or microsegmentation product — the design is ours; the test it must pass is not.

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the full working checklist and the chapter's Final Review. Grounded in the Network Segmentation chapter of the* Defensive Security Handbook*.*
