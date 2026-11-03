---
id: "CRE-777-470"
title: "Ignore/block execution logic from untrusted sources"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-777-470
excerpt: "CRE 777-470 · in Technical application security controls › Input and output protection › File handling › File execution · 21 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, ZAP Rule
---
> **CRE**: [777-470](https://opencre.org/cre/777-470)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-130-550]] › [[cre-451-082]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V12.3.6](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x20-V12-Files-Resources.md#v123-file-execution) | Verify that the application does not include and execute functionality from untrusted sources, such as unverified content distribution networks, JavaScript libraries, node npm libraries, or server-side DLLs. | curated |

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

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10017](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CrossDomainScriptInclusionScanRule.java) | Cross-Domain JavaScript Source File Inclusion | automatic |
| [10115-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/PolyfillCdnScriptScanRule.java) | Script Served From Malicious Domain (polyfill) | automatic |
| [10115-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/PolyfillCdnScriptScanRule.java) | Script Served From Malicious Domain (polyfill) | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [777-470](https://opencre.org/cre/777-470). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
