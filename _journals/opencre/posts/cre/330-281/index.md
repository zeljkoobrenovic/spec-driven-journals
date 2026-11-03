---
id: "CRE-330-281"
title: "Use least privilege OS accounts for system (components)"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-330-281
excerpt: "CRE 330-281 · in Technical application security controls › Technical application access control › Minimize permissions · 11 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Proactive Controls, PCI DSS
---
> **CRE**: [330-281](https://opencre.org/cre/330-281)
>
> **Part of**: [[cre-636-660]] › [[cre-724-770]] › [[cre-123-124]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-proactive-controls]], [[standard-pci-dss]]

## Related CREs

- [[cre-286-500]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.2.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v12-authentication-architecture) | Verify the use of unique or special low-privilege operating system accounts for all application components, services, and servers. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [69](https://capec.mitre.org/data/definitions/69.html) | Target Programs with Elevated Privileges | automatic |
| [104](https://capec.mitre.org/data/definitions/104.html) | Cross Zone Scripting | automatic |
| [470](https://capec.mitre.org/data/definitions/470.html) | Expanding Control over the Operating System from the Database | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [250](https://cwe.mitre.org/data/definitions/250.html) | Execution with Unnecessary Privileges | curated |

More: [[standard-cwe]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C3](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c3-secure-database-access.html) | curated |

More: [[standard-owasp-proactive-controls]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 7.2.5 | All application and system accounts and related access privileges are assigned and managed as follows: () Based on the least privileges necessary for the operability of the system or application. () Access is limited to the systems, applications, or processes that specifically require their use. (CUSTOMIZED APPROACH OBJECTIVE): Access rights granted to application and system accounts are limited to only the access needed for the operability of that application or system. (APPLICABILITY NOTES): This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| 8.2.7 | Accounts used by third parties to access, support, or maintain system components via remote access are managed as follows: () Enabled only during the time period needed and disabled when not in use. () Use is monitored for unexpected activity. (CUSTOMIZED APPROACH OBJECTIVE): Third party remote access cannot be used except where specifically authorized and use is overseen by management. | automatic |
| 8.6.1 | If accounts used by systems or applications can be used for interactive login, they are managed as follows: () Interactive use is prevented unless needed for an exceptional circumstance. () Interactive use is limited to the time needed for the exceptional circumstance. () Business justification for interactive use is documented. () Interactive use is explicitly approved by management. () Individual user identity is confirmed before access to account is granted. () Every action taken is attributable to an individual user. (CUSTOMIZED APPROACH OBJECTIVE): When used interactively, all actions with accounts designated as system or application accounts are authorized and attributable to an individual person. (APPLICABILITY NOTES): This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| 11.3.1.2 | Internal vulnerability scans are performed via authenticated scanning as follows: () Systems that are unable to accept credentials for authenticated scanning are documented. () Sufficient privileges are used for those systems that accept credentials for scanning. () If accounts used for authenticated scanning can be used for interactive login, they are managed in accordance with Requirement 8.2.2. (CUSTOMIZED APPROACH OBJECTIVE): Automated tools used to detect vulnerabilities can detect vulnerabilities local to each system, which are not visible remotely. (APPLICABILITY NOTES): The authenticated scanning tools can be either host-based or network-based. “Sufficient” privileges are those needed to access system resources such that a thorough scan can be conducted that detects known vulnerabilities. This requirement does not apply to system components that cannot accept credentials for scanning. Examples of systems that may not accept credentials for scanning include some network and security appliances, mainframes, and containers. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| A3.4.1 | User accounts and access privileges to inscope system components are reviewed at least once every six months to ensure user accounts and access privileges remain appropriate based on job function, and that all access is authorized. PCI DSS Reference: Requirement 7 (CUSTOMIZED APPROACH OBJECTIVE): This requirement is not eligible for the customized approach. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [330-281](https://opencre.org/cre/330-281). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
