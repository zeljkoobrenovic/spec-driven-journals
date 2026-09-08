---
timetoread: "2 min read"
---

My organization runs its Windows estate as **one security system, not a fleet of servers** — and the real boundary of that system is the Active Directory forest, not the domain. Nothing unsupported stays on the network without an approved exception and isolation; patching is central and covers the third-party software attackers actually exploit; domain controllers get crown-jewel treatment with a tested compromise-recovery plan; privilege is minimized and individually attributable; and the security baseline is enforced through Group Policy, not documented in a binder. The test the estate is held to: every privileged action is attributable to a named person, and a compromised domain controller has a documented, tested path back.

**What changes**

* **Legacy becomes a signed risk decision.** Unsupported Windows is upgraded or removed; what must remain is isolated on dedicated VLANs or air-gapped, its business risk documented and communicated, with a migration plan and an approved exception — no quiet XP boxes on the flat network.
* **File shares stop leaking.** SMB shares are inventoried, scanned for exposure, reviewed for sensitive data, and pruned; share and NTFS permissions are both restricted and periodically re-audited.
* **The boundary moves to the forest.** Domains are treated as administrative containers, not security boundaries; every cross-forest and cross-domain trust is documented, minimized, made one-way where possible, and restricted with SID filtering and selective authentication where warranted — hybrid directories included.
* **Domain controllers become crown jewels.** Dedicated, never dual-purpose, physically secured, TPM-backed and encrypted, logon-restricted — with a documented compromise-response plan that honestly contemplates rebuilding the forest.
* **Privilege becomes attributable.** Domain Admins membership is minimized and reviewed; service accounts are dedicated, least-privileged, and non-interactive; local administrator passwords are unique per machine via LAPS or equivalent; shared accounts are eliminated or documented, monitored, and re-challenged.
* **The baseline enforces itself.** Group Policy carries the security settings, built from recognized NIST/Microsoft baselines, tested before broad deployment, audited for conflicts — and newly joined machines land in managed OUs with baseline policies applied immediately.
* **Detection and recovery are exercised.** AD security logs are centrally collected and actually reviewed — privileged activity, group changes, trusts, GPOs, unusual SMB access — and AD backups are tested, restoration rehearsed, and backup systems protected from ordinary administrative compromise.

**What it costs**

* Privilege minimization, LAPS, and separate admin accounts add friction to administration — accepted deliberately, because attribution is what monitoring and forensics stand on.
* Trust reviews, GPO audits, share re-audits, and restoration tests are standing work on a cadence, not one-time cleanups.
* Isolating and exception-tracking legacy systems forces uncomfortable conversations with the business — that is the point.

**What we are not doing**

* Not forbidding legacy or multi-forest designs — naming, isolating, and owning them.
* Not treating this as all of identity — password policy, MFA, and credential hygiene live in [[authentication]].
* Not watching the logs here — central review disciplines live in [[logging-and-monitoring]], and tested-restore practice in [[disaster-recovery]].

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the full working checklist and final review. Grounded in the Microsoft Windows Infrastructure chapter of the* Defensive Security Handbook*.*
