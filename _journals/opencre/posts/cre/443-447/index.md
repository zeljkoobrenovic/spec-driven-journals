---
id: "CRE-443-447"
title: "Log access control decisions"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-443-447
excerpt: "CRE 443-447 · in Technical application security controls › Logging and error handling › Log relevant · 81 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, PCI DSS, ZAP Rule
---
> **CRE**: [443-447](https://opencre.org/cre/443-447)
>
> **Part of**: [[cre-636-660]] › [[cre-842-876]] › [[cre-402-706]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-pci-dss]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V7.2.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x15-V7-Error-Logging.md#v72-log-processing) | Verify that all access control decisions can be logged and all failed decisions are logged. This should include requests with relevant metadata needed for security investigations. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [1](https://capec.mitre.org/data/definitions/1.html) | Accessing Functionality Not Properly Constrained by ACLs | automatic |
| [13](https://capec.mitre.org/data/definitions/13.html) | Subverting Environment Variable Values | automatic |
| [17](https://capec.mitre.org/data/definitions/17.html) | Using Malicious Files | automatic |
| [39](https://capec.mitre.org/data/definitions/39.html) | Manipulating Opaque Client-based Data Tokens | automatic |
| [45](https://capec.mitre.org/data/definitions/45.html) | Buffer Overflow via Symbolic Links | automatic |
| [51](https://capec.mitre.org/data/definitions/51.html) | Poison Web Service Registry | automatic |
| [59](https://capec.mitre.org/data/definitions/59.html) | Session Credential Falsification through Prediction | automatic |
| [60](https://capec.mitre.org/data/definitions/60.html) | Reusing Session IDs (aka Session Replay) | automatic |
| [76](https://capec.mitre.org/data/definitions/76.html) | Manipulating Web Input to File System Calls | automatic |
| [77](https://capec.mitre.org/data/definitions/77.html) | Manipulating User-Controlled Variables | automatic |
| [87](https://capec.mitre.org/data/definitions/87.html) | Forceful Browsing | automatic |
| [104](https://capec.mitre.org/data/definitions/104.html) | Cross Zone Scripting | automatic |
| [127](https://capec.mitre.org/data/definitions/127.html) | Directory Indexing | automatic |
| [180](https://capec.mitre.org/data/definitions/180.html) | Exploiting Incorrectly Configured Access Control Security Levels | automatic |
| [402](https://capec.mitre.org/data/definitions/402.html) | Bypassing ATA Password Security | automatic |
| [624](https://capec.mitre.org/data/definitions/624.html) | Hardware Fault Injection | automatic |
| [625](https://capec.mitre.org/data/definitions/625.html) | Mobile Device Fault Injection | automatic |
| [647](https://capec.mitre.org/data/definitions/647.html) | Collect Data from Registries | automatic |
| [668](https://capec.mitre.org/data/definitions/668.html) | Key Negotiation of Bluetooth Attack (KNOB) | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [285](https://cwe.mitre.org/data/definitions/285.html) | Improper Authorization | curated |
| [41](https://cwe.mitre.org/data/definitions/41.html) | Improper Resolution of Path Equivalence | automatic |
| [42](https://cwe.mitre.org/data/definitions/42.html) | Path Equivalence: 'filename.' (Trailing Dot) | automatic |
| [43](https://cwe.mitre.org/data/definitions/43.html) | Path Equivalence: 'filename....' (Multiple Trailing Dot) | automatic |
| [44](https://cwe.mitre.org/data/definitions/44.html) | Path Equivalence: 'file.name' (Internal Dot) | automatic |
| [45](https://cwe.mitre.org/data/definitions/45.html) | Path Equivalence: 'file...name' (Multiple Internal Dot) | automatic |
| [46](https://cwe.mitre.org/data/definitions/46.html) | Path Equivalence: 'filename ' (Trailing Space) | automatic |
| [47](https://cwe.mitre.org/data/definitions/47.html) | Path Equivalence: ' filename' (Leading Space) | automatic |
| [48](https://cwe.mitre.org/data/definitions/48.html) | Path Equivalence: 'file name' (Internal Whitespace) | automatic |
| [49](https://cwe.mitre.org/data/definitions/49.html) | Path Equivalence: 'filename/' (Trailing Slash) | automatic |
| [50](https://cwe.mitre.org/data/definitions/50.html) | Path Equivalence: '//multiple/leading/slash' | automatic |
| [51](https://cwe.mitre.org/data/definitions/51.html) | Path Equivalence: '/multiple//internal/slash' | automatic |
| [52](https://cwe.mitre.org/data/definitions/52.html) | Path Equivalence: '/multiple/trailing/slash//' | automatic |
| [53](https://cwe.mitre.org/data/definitions/53.html) | Path Equivalence: '\multiple\\internal\backslash' | automatic |
| [54](https://cwe.mitre.org/data/definitions/54.html) | Path Equivalence: 'filedir\' (Trailing Backslash) | automatic |
| [55](https://cwe.mitre.org/data/definitions/55.html) | Path Equivalence: '/./' (Single Dot Directory) | automatic |
| [56](https://cwe.mitre.org/data/definitions/56.html) | Path Equivalence: 'filedir*' (Wildcard) | automatic |
| [57](https://cwe.mitre.org/data/definitions/57.html) | Path Equivalence: 'fakedir/../realdir/filename' | automatic |
| [58](https://cwe.mitre.org/data/definitions/58.html) | Path Equivalence: Windows 8.3 Filename | automatic |
| [202](https://cwe.mitre.org/data/definitions/202.html) | Exposure of Sensitive Information Through Data Queries | automatic |
| [219](https://cwe.mitre.org/data/definitions/219.html) | Storage of File with Sensitive Data Under Web Root | automatic |
| [220](https://cwe.mitre.org/data/definitions/220.html) | Storage of File With Sensitive Data Under FTP Root | automatic |
| [276](https://cwe.mitre.org/data/definitions/276.html) | Incorrect Default Permissions | automatic |
| [277](https://cwe.mitre.org/data/definitions/277.html) | Insecure Inherited Permissions | automatic |
| [278](https://cwe.mitre.org/data/definitions/278.html) | Insecure Preserved Inherited Permissions | automatic |
| [279](https://cwe.mitre.org/data/definitions/279.html) | Incorrect Execution-Assigned Permissions | automatic |
| [281](https://cwe.mitre.org/data/definitions/281.html) | Improper Preservation of Permissions | automatic |
| [424](https://cwe.mitre.org/data/definitions/424.html) | Improper Protection of Alternate Path | automatic |
| [425](https://cwe.mitre.org/data/definitions/425.html) | Direct Request ('Forced Browsing') | automatic |
| [433](https://cwe.mitre.org/data/definitions/433.html) | Unparsed Raw Web Content Delivery | automatic |
| [527](https://cwe.mitre.org/data/definitions/527.html) | Exposure of Version-Control Repository to an Unauthorized Control Sphere | automatic |
| [528](https://cwe.mitre.org/data/definitions/528.html) | Exposure of Core Dump File to an Unauthorized Control Sphere | automatic |
| [529](https://cwe.mitre.org/data/definitions/529.html) | Exposure of Access Control List Files to an Unauthorized Control Sphere | automatic |
| [530](https://cwe.mitre.org/data/definitions/530.html) | Exposure of Backup File to an Unauthorized Control Sphere | automatic |
| [539](https://cwe.mitre.org/data/definitions/539.html) | Use of Persistent Cookies Containing Sensitive Information | automatic |
| [551](https://cwe.mitre.org/data/definitions/551.html) | Incorrect Behavior Order: Authorization Before Parsing and Canonicalization | automatic |
| [552](https://cwe.mitre.org/data/definitions/552.html) | Files or Directories Accessible to External Parties | automatic |
| [553](https://cwe.mitre.org/data/definitions/553.html) | Command Shell in Externally Accessible Directory | automatic |
| [566](https://cwe.mitre.org/data/definitions/566.html) | Authorization Bypass Through User-Controlled SQL Primary Key | automatic |
| [612](https://cwe.mitre.org/data/definitions/612.html) | Improper Authorization of Index Containing Sensitive Information | automatic |
| [638](https://cwe.mitre.org/data/definitions/638.html) | Not Using Complete Mediation | automatic |
| [639](https://cwe.mitre.org/data/definitions/639.html) | Authorization Bypass Through User-Controlled Key | automatic |
| [647](https://cwe.mitre.org/data/definitions/647.html) | Use of Non-Canonical URL Paths for Authorization Decisions | automatic |
| [732](https://cwe.mitre.org/data/definitions/732.html) | Incorrect Permission Assignment for Critical Resource | automatic |
| [766](https://cwe.mitre.org/data/definitions/766.html) | Critical Data Element Declared Public | automatic |
| [804](https://cwe.mitre.org/data/definitions/804.html) | Guessable CAPTCHA | automatic |
| [862](https://cwe.mitre.org/data/definitions/862.html) | Missing Authorization | automatic |
| [863](https://cwe.mitre.org/data/definitions/863.html) | Incorrect Authorization | automatic |
| [926](https://cwe.mitre.org/data/definitions/926.html) | Improper Export of Android Application Components | automatic |
| [927](https://cwe.mitre.org/data/definitions/927.html) | Use of Implicit Intent for Sensitive Communication | automatic |
| [939](https://cwe.mitre.org/data/definitions/939.html) | Improper Authorization in Handler for Custom URL Scheme | automatic |
| [942](https://cwe.mitre.org/data/definitions/942.html) | Permissive Cross-domain Security Policy with Untrusted Domains | automatic |
| [1004](https://cwe.mitre.org/data/definitions/1004.html) | Sensitive Cookie Without 'HttpOnly' Flag | automatic |
| [1230](https://cwe.mitre.org/data/definitions/1230.html) | Exposure of Sensitive Information Through Metadata | automatic |
| [1244](https://cwe.mitre.org/data/definitions/1244.html) | Internal Asset Exposed to Unsafe Debug Access Level or State | automatic |
| [1256](https://cwe.mitre.org/data/definitions/1256.html) | Improper Restriction of Software Interfaces to Hardware Features | automatic |
| [1297](https://cwe.mitre.org/data/definitions/1297.html) | Unprotected Confidential Information on Device is Accessible by OSAT Vendors | automatic |
| [1314](https://cwe.mitre.org/data/definitions/1314.html) | Missing Write Protection for Parametric Data Values | automatic |
| [1328](https://cwe.mitre.org/data/definitions/1328.html) | Security Version Number Mutable to Older Versions | automatic |

More: [[standard-cwe]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 10.2.1.3 | Audit logs capture all access to audit logs. (CUSTOMIZED APPROACH OBJECTIVE): Records of all access to audit logs are captured. | automatic |

More: [[standard-pci-dss]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [90034](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CloudMetadataScanRule.java) | Cloud Metadata Potentially Exposed | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [443-447](https://opencre.org/cre/443-447). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
