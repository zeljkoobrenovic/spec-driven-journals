---
timetoread: "2 min read"
---

The database is where a security failure becomes the headline, so my organization **protects data where it lives**. Every critical database is known, classified, and owned; access is least privilege with privileged accounts logged and reviewed; encryption covers rest, transit, and backups with keys stored separately; injection, credential attacks, and insiders are all planned for; backups restore on a tested clock; and cloud databases meet the same bar as on-premises ones. The test, straight from the chapter: five questions — what data, who accesses it and why, how it is protected, how misuse would be detected, how fast we recover — answered clearly for every critical database, or we have a governance gap.

**What changes**

* **The data estate gets mapped and classified.** Where critical and sensitive data lives, which technologies run it — relational, NoSQL, cloud-managed, serverless — which databases are business-critical, and who owns each one. The highest-risk databases get the strongest protection.
* **Access tightens to least privilege.** Application accounts lose admin rights — an injection attack inherits every privilege the app account holds — administrative access requires strong authentication, shared admin accounts go away, departures are removed promptly, and privileged activity is logged, monitored, and periodically reviewed.
* **Encryption and secrets become disciplined.** At rest, in transit, and in backups, with keys stored separately from data, rotated, and owned; passwords hashed and salted, never plaintext; credentials never hardcoded — a centralized secrets manager with rotation that does not break operations.
* **Every attack mode gets a plan.** Parameterized queries and tested code against injection; MFA, lockout, and failure monitoring against credential attacks; job-based access, separation of duties, export controls, and role-change reviews against insiders — malicious and accidental alike; no public endpoints, secured copies, and bulk-download monitoring against exfiltration.
* **Operations get a clock and an owner.** Hardening against CIS Benchmarks and DISA STIGs, defined patch timelines with compensating controls, logs forwarded to the SIEM with a named alert owner, and backups that are encrypted, attacker-resistant, and restore-tested with defined RTO and RPO.
* **Governance makes it durable.** Documented standards with minimum requirements, periodic reviews, documented and approved exceptions, management-level risk tracking, database breaches inside the incident-response plan, and acquisitions and vendors held to the same scrutiny.

**What it costs**

* Least privilege and secrets migration mean reworking applications that connected as admin with hardcoded strings — deliberate, paid-down debt.
* Restore testing, privileged-access reviews, and configuration reviews are recurring work, not one-time projects.
* Governance overhead — owners, standards, exception approvals — is the price of controls that survive staff turnover.

**What we are not doing**

* Not mandating platforms — MySQL, PostgreSQL, SQL Server, and MongoDB are the worked examples; the commitments are capability-level.
* Not building the organization-wide identity model here — that is [[authentication]].
* Not covering secure coding practice in full — that is [[secure-software-development]].
* Not designing the cloud estate — that is [[cloud-infrastructure]].

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries the full working checklist, the seventeen closing questions, and the five-question priority reminder. Grounded in the Databases chapter of the* Defensive Security Handbook *(Brotherston, Berlin, and Reyor).*
