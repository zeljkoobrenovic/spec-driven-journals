---
id: "CRE-547-283"
title: "Protect against LFI / RFI"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-547-283
excerpt: "CRE 547-283 · in Technical application security controls › Input and output protection › Output encoding and injection prevention · 25 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [547-283](https://opencre.org/cre/547-283)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-161-451]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.3.9](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v53-output-encoding-and-injection-prevention) | Verify that the application protects against Local File Inclusion (LFI) or Remote File Inclusion (RFI) attacks. | curated |

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
|  | [File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) | curated |
|  | [Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html) | curated |
|  | [Injection Prevention in Java Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_in_Java_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-INPV-11](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11-Testing_for_Code_Injection.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10017](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CrossDomainScriptInclusionScanRule.java) | Cross-Domain JavaScript Source File Inclusion | automatic |
| [10115-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/PolyfillCdnScriptScanRule.java) | Script Served From Malicious Domain (polyfill) | automatic |
| [10115-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/PolyfillCdnScriptScanRule.java) | Script Served From Malicious Domain (polyfill) | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [547-283](https://opencre.org/cre/547-283). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
