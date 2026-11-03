---
id: "CRE-577-260"
title: "Enforce integrity check for externally hosted assets (eg SRI)"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-577-260
excerpt: "CRE 577-260 · in Development processes for security › Supply chain management › Dependency integrity · 24 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, PCI DSS, ZAP Rule
---
> **CRE**: [577-260](https://opencre.org/cre/577-260)
>
> **Part of**: [[cre-616-305]] › [[cre-613-285]] › [[cre-613-287]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-pci-dss]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V14.2.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x22-V14-Config.md#v142-dependency) | Verify that if application assets, such as JavaScript libraries, CSS or web fonts, are hosted externally on a Content Delivery Network (CDN) or external provider, Subresource Integrity (SRI) is used to validate the integrity of the asset. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [175](https://capec.mitre.org/data/definitions/175.html) | Code Inclusion | automatic |
| [201](https://capec.mitre.org/data/definitions/201.html) | Serialized Data External Linking | automatic |
| [228](https://capec.mitre.org/data/definitions/228.html) | DTD Injection | automatic |
| [251](https://capec.mitre.org/data/definitions/251.html) | Local Code Inclusion | automatic |
| [252](https://capec.mitre.org/data/definitions/252.html) | PHP Local File Inclusion | automatic |
| [253](https://capec.mitre.org/data/definitions/253.html) | Remote Code Inclusion | automatic |
| [263](https://capec.mitre.org/data/definitions/263.html) | Force Use of Corrupted Files | automatic |
| [538](https://capec.mitre.org/data/definitions/538.html) | Open-Source Library Manipulation | automatic |
| [549](https://capec.mitre.org/data/definitions/549.html) | Local Execution of Code | automatic |
| [640](https://capec.mitre.org/data/definitions/640.html) | Inclusion of Code in Existing Process | automatic |
| [660](https://capec.mitre.org/data/definitions/660.html) | Root/Jailbreak Detection Evasion via Hooking | automatic |
| [695](https://capec.mitre.org/data/definitions/695.html) | Repo Jacking | automatic |
| [698](https://capec.mitre.org/data/definitions/698.html) | Install Malicious Extension | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [829](https://cwe.mitre.org/data/definitions/829.html) | Inclusion of Functionality from Untrusted Control Sphere | curated |
| [98](https://cwe.mitre.org/data/definitions/98.html) | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') | automatic |
| [827](https://cwe.mitre.org/data/definitions/827.html) | Improper Control of Document Type Definition | automatic |
| [830](https://cwe.mitre.org/data/definitions/830.html) | Inclusion of Web Functionality from an Untrusted Source | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) | curated |
|  | [Vulnerable Dependency Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 6.4.3 | All payment page scripts that are loaded and executed in the consumer’s browser are managed as follows: () A method is implemented to confirm that each script is authorized. () A method is implemented to assure the integrity of each script. () An inventory of all scripts is maintained with written justification as to why each is necessary. (CUSTOMIZED APPROACH OBJECTIVE): Unauthorized code cannot be present in the payment page as it is rendered in the consumer’s browser. (APPLICABILITY NOTES): This requirement applies to all scripts loaded from the entity’s environment and scripts loaded from third and fourth parties. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |

More: [[standard-pci-dss]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10017](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CrossDomainScriptInclusionScanRule.java) | Cross-Domain JavaScript Source File Inclusion | automatic |
| [10115-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/PolyfillCdnScriptScanRule.java) | Script Served From Malicious Domain (polyfill) | automatic |
| [10115-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/PolyfillCdnScriptScanRule.java) | Script Served From Malicious Domain (polyfill) | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [577-260](https://opencre.org/cre/577-260). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
