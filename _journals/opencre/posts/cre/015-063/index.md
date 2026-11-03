---
id: "CRE-015-063"
title: "Log access to sensitive data"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-015-063
excerpt: "CRE 015-063 · in Technical application security controls › Logging and error handling › Log relevant · 13 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, PCI DSS, ZAP Rule
---
> **CRE**: [015-063](https://opencre.org/cre/015-063)
>
> **Part of**: [[cre-636-660]] › [[cre-842-876]] › [[cre-402-706]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-pci-dss]], [[standard-zap-rule]]

## Related CREs

- [[cre-843-841]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V8.3.5](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x16-V8-Data-Protection.md#v83-sensitive-private-data) | Verify accessing sensitive data is audited (without logging the sensitive data itself), if the data is collected under relevant data protection directives or where logging of access is required. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [215](https://capec.mitre.org/data/definitions/215.html) | Fuzzing for application mapping | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [532](https://cwe.mitre.org/data/definitions/532.html) | Insertion of Sensitive Information into Log File | curated |

More: [[standard-cwe]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 9.2.1.1 | Individual physical access to sensitive areas within the CDE is monitored with either video cameras or physical access control mechanisms (or both) as follows: () Entry and exit points to/from sensitive areas within the CDE are monitored. () Monitoring devices or mechanisms are protected from tampering or disabling. () Collected data is reviewed and correlated with other entries. () Collected data is stored for at least three months, unless otherwise restricted by law. (CUSTOMIZED APPROACH OBJECTIVE): Trusted, verifiable records are maintained of individual physical entry to, and exit from, sensitive areas. | automatic |
| 9.3.4 | A visitor log is used to maintain a physical record of visitor activity within the facility and within sensitive areas, including: () The visitor’s name and the organization represented. () The date and time of the visit. () The name of the personnel authorizing physical access. () Retaining the log for at least three months, unless otherwise restricted by law. (CUSTOMIZED APPROACH OBJECTIVE): Records of visitor access that enable the identification of individuals are maintained. | automatic |
| 10.1 | Processes and mechanisms for logging and monitoring all access to system components and cardholder data are defined and documented. | automatic |
| 10.2.1.1 | Audit logs capture all individual user access to cardholder data. (CUSTOMIZED APPROACH OBJECTIVE): Records of all individual user access to cardholder data are captured. | automatic |
| 10.2.1.2 | Audit logs capture all actions taken by any individual with administrative access, including any interactive use of application or system accounts. (CUSTOMIZED APPROACH OBJECTIVE): Records of all actions performed by individuals with elevated privileges are captured. | automatic |
| 10.2.1.4 | Audit logs capture all invalid logical access attempts. (CUSTOMIZED APPROACH OBJECTIVE): Records of all invalid access attempts are captured. | automatic |
| 10.2.1.5 | Audit logs capture all changes to identification and authentication credentials including, but not limited to: () Creation of new accounts. () Elevation of privileges. () All changes, additions, or deletions to accounts with administrative access. (CUSTOMIZED APPROACH OBJECTIVE): Records of all changes to identification and authentication credentials are captured. | automatic |
| 10.3.1 | Read access to audit logs files is limited to those with a job-related need. (CUSTOMIZED APPROACH OBJECTIVE): Stored activity records cannot be accessed by unauthorized personnel. | automatic |
| 10.6.3 | Time synchronization settings and data are protected as follows: () Access to time data is restricted to only personnel with a business need. () Any changes to time settings on critical systems are logged, monitored, and reviewed. (CUSTOMIZED APPROACH OBJECTIVE): System time settings cannot be modified by unauthorized personnel. | automatic |

More: [[standard-pci-dss]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10052](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/XChromeLoggerDataInfoLeakScanRule.java) | X-ChromeLogger-Data (XCOLD) Header Information Leak | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [015-063](https://opencre.org/cre/015-063). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
