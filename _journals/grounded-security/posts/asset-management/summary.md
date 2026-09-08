---
timetoread: "2 min read"
---

My organization cannot defend what it does not know it has — so **asset management is an ongoing security program, not a one-time inventory exercise**. One authoritative system is the source of truth; every asset carries an owner, a criticality, and a risk rating; the lifecycle runs from procurement to verified destruction; and automated discovery is validated before it is trusted. The test the program is held to: the inventory answers security questions in minutes — which assets a new vulnerability affects, who owns a critical system, what faces the internet — and it is actively used for security decisions, not simply maintained as documentation.

**What changes**

* **One system becomes the place arguments end.** A single authoritative inventory — sized honestly to the organization, replaced before it breaks — with defined write access, backups, version history, and every team knowing it is the official source.
* **Every asset gets an owner and a value.** Owners and custodians on every asset and every service account; criticality and risk ratings that actually drive patching, remediation, monitoring, incident response, backup, and access-review priorities.
* **Coverage becomes complete.** Network equipment, servers, endpoints, users and accounts, applications with their data flows, cloud assets (including IAM policies, secrets, and internet-exposed resources), and certificates and domains with expiration alerts and dangling-DNS review.
* **The lifecycle gets security at its edges.** Deployment means default credentials replaced, patched, scanned, and encrypted before production; decommissioning means access revoked, records removed, data destroyed by an approved method, and destruction verified and documented.
* **Automation feeds the register; humans keep it honest.** Discovery from ARP, DHCP, scanning, SNMP, and cloud APIs; integrations with vulnerability, endpoint, IAM, and IaC data; alerts on expirations and unknown devices — with automated data validated before being treated as authoritative, and unmanaged assets investigated as process failures.

**What it costs**

* Standing review work — monthly discoveries and expirations, quarterly reconciliation of sources and privileged accounts, an annual full review — is permanent overhead, accepted because a stale inventory is worse than none: it lies with confidence.
* Interviewing business and data owners takes real cross-department time; the inventory has to reflect what the business knows, not just what the scanner sees.
* Disposal discipline (approved destruction, verification, certificates) is slower than the dumpster — deliberately.

**What we are not doing**

* Not mandating a CMDB product — a spreadsheet can be the honest answer for a small environment, with a planned migration.
* Not running the scan-triage-remediate loop here — that is [[vulnerability-management]], which consumes this record's criticality data.
* Not hardening the assets themselves — that is [[endpoints]], [[cloud-infrastructure]], and the rest of the estate section.

*The Article tab carries the rationale and anti-patterns; the Checklist tab carries all thirty-two sections through the final program validation. Grounded in the "Asset Management and Documentation" chapter of the* Defensive Security Handbook*.*
