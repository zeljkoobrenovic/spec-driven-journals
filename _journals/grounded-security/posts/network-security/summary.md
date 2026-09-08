---
timetoread: "2 min read"
---

The network my organization runs on is not trusted by default — every router, switch, access point, firewall, and VPN appliance is **inventoried, hardened, patched, and watched**. Defaults die on arrival, every open port earns its place, the management plane is isolated and individually accountable, and traffic is filtered outbound as strictly as inbound. The test the estate is held to: hardening is proven by a scan, not asserted in a diagram — and re-proven after every change.

**What changes**

* **Device operations become a controlled cycle.** A complete inventory, CIS-style baselines, tracked vendor advisories, and a patch process with verified firmware, configuration backups, documented rollback, change control, and post-upgrade testing — no more heroic midnight upgrades from memory.
* **The management plane gets crown-jewel treatment.** SNMPv3 with defaults dead, encrypted management protocols only, a dedicated management network never exposed to the internet, a hardened MFA-protected bastion as the entry point, and individual centrally authenticated admin accounts with separation of duties — shared logins end.
* **Configuration becomes code.** Templates in version control, peer review and change control on every change, automated changes tested before production, and secrets in a dedicated store — never in a repository.
* **Traffic is controlled in both directions and both protocols.** Segmentation separates sensitive, management, public-facing, and IoT traffic; egress is filtered with denials logged and read, because outbound control is what makes exfiltration hard; IPv6 gets IPv4-equivalent policy, filtering, and monitoring — including its tunneling mechanisms.
* **The soft edges get the hardest watch.** Wireless runs WPA2-AES minimum and WPA3 preferred with rogue and evil-twin AP detection; IoT is inventoried, patched, and segregated; layer 2 is defended with port security, DHCP snooping, and Dynamic ARP Inspection; VPN appliances are patched aggressively, MFA-protected, and their logins watched for anomalies; DDoS amplifiers are closed and a response plan exists.
* **Verification becomes standing work.** Central logs, alerts on reboots and new listening services, egress-denial review, periodic vulnerability scans — and periodic revalidation that hardened configurations are still hardened, because hardening decays.

**What it costs**

* Real engineering time for the inventory, baselining, and configuration-as-code migration — and recurring time for the scan-and-revalidate loop, which never finishes.
* Change-control discipline slows individual device changes deliberately; the bastion path adds a hop to every administrative session.
* Some legacy devices will fail the secure-management bar and must be replaced, or their risk formally accepted in writing with an owner and an end date.

**What we are not doing**

* Not designing the segmentation architecture itself — zones, DMZ, and NAC live in [[network-segmentation]].
* Not building the detection layer — that is [[ids-ips]], fed by this record's logs.
* Not mandating vendors — the commitments hold for any estate, hardware or virtual.

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries all twenty-one practice areas and the chapter's Final Review. Grounded in the Network Security chapter of the* Defensive Security Handbook*.*
