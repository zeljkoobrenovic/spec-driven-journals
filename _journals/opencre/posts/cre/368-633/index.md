---
id: "CRE-368-633"
title: "Enforce least privilege"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-368-633
excerpt: "CRE 368-633 · in Technical application security controls › Technical application access control › Minimize permissions · 97 mappings to 9 standards and tools."
tags: ASVS, CAPEC, CWE, ISO 27001, OWASP Cheat Sheets, OWASP Proactive Controls, OWASP Web Security Testing Guide (WSTG), PCI DSS, ZAP Rule
---
> **CRE**: [368-633](https://opencre.org/cre/368-633)
>
> **Part of**: [[cre-636-660]] › [[cre-724-770]] › [[cre-123-124]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-iso-27001]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-pci-dss]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V4.1.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V4-Access-Control.md#v41-general-access-control-design) | Verify that the principle of least privilege exists - users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. This implies protection against spoofing and elevation of privilege. ((C7)(https://owasp.org/www-project-proactive-controls/#div-numbering)) | curated |

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

### ISO 27001

| ID | Section | Link |
| --- | --- | --- |
| 8.2 | Privileged access rights | curated |

More: [[standard-iso-27001]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Access Control Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html) | curated |
|  | [Authorization Testing Automation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C7](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c7-enforce-access-controls.html) | curated |

More: [[standard-owasp-proactive-controls]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-IDNT-01](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/03-Identity_Management_Testing/01-Test_Role_Definitions.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 1.3.1 | Inbound traffic to the CDE is restricted as follows: () To only traffic that is necessary. () All other traffic is specifically denied. (CUSTOMIZED APPROACH OBJECTIVE): Unauthorized traffic cannot enter the CDE. | automatic |
| 1.3.2 | Outbound traffic from the CDE is restricted as follows: () To only traffic that is necessary. () All other traffic is specifically denied. (CUSTOMIZED APPROACH OBJECTIVE): Unauthorized traffic cannot leave the CDE. | automatic |
| 3.6.1.3 | Access to cleartext cryptographic key components is restricted to the fewest number of custodians necessary. (CUSTOMIZED APPROACH OBJECTIVE): Access to cleartext cryptographic key components is restricted to necessary personnel. | automatic |
| 6.5.3 | Pre-production environments are separated from production environments and the separation is enforced with access controls. (CUSTOMIZED APPROACH OBJECTIVE): Pre-production environments cannot introduce risks and vulnerabilities into production environments. | automatic |
| 7.2.2 | Access is assigned to users, including privileged users, based on: () Job classification and function. () Least privileges necessary to perform job responsibilities. (CUSTOMIZED APPROACH OBJECTIVE): Access to systems and data is limited to only the access needed to perform job functions, as defined in the related access roles. | automatic |
| 7.2.3 | Required privileges are approved by authorized personnel. (CUSTOMIZED APPROACH OBJECTIVE): Access privileges cannot be granted to users without appropriate, documented authorization. | automatic |
| 7.2.4 | All user accounts and related access privileges, including third-party/vendor accounts, are reviewed as follows: () At least once every six months. () To ensure user accounts and access remain appropriate based on job function. () Any inappropriate access is addressed. () Management acknowledges that access remains appropriate. (CUSTOMIZED APPROACH OBJECTIVE): Account privilege assignments are verified periodically by management as correct, and nonconformities are remediated. (APPLICABILITY NOTES): This requirement applies to all user accounts and related access privileges, including those used by personnel and third parties/vendors, and accounts used to access third-party cloud services. See Requirements 7.2.5 and 7.2.5.1 and 8.6.1 through 8.6.3 for controls for application and system accounts. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| 7.3.3 | The access control system(s) is set to “deny all” by default. (CUSTOMIZED APPROACH OBJECTIVE): Access rights and privileges are prohibited unless expressly permitted. | automatic |
| 8.3.3 | User identity is verified before modifying any authentication factor. (CUSTOMIZED APPROACH OBJECTIVE): Unauthorized individuals cannot gain system access by impersonating the identity of an authorized user. | automatic |
| A1.1.1 | Logical separation is implemented as follows: () The provider cannot access its customers’ environments without authorization. () Customers cannot access the provider’s environment without authorization. (CUSTOMIZED APPROACH OBJECTIVE): Customers cannot access the provider’s environment. The provider cannot access its customers’ environments without authorization. (APPLICABILITY NOTES): This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| A1.1.2 | Controls are implemented such that each customer only has permission to access its own cardholder data and CDE. (CUSTOMIZED APPROACH OBJECTIVE): Customers cannot access other customers’ environments. | automatic |
| A1.1.3 | Controls are implemented such that each customer can only access resources allocated to them. (CUSTOMIZED APPROACH OBJECTIVE): Customers cannot impact resources allocated to other customers. | automatic |

More: [[standard-pci-dss]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [90034](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CloudMetadataScanRule.java) | Cloud Metadata Potentially Exposed | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [368-633](https://opencre.org/cre/368-633). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
