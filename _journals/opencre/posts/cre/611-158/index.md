---
id: "CRE-611-158"
title: "Use static analysis tooling to detect potentially malicious actions"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-611-158
excerpt: "CRE 611-158 · in Development processes for security › Verification › Automated static security analysis of code and configuration · 8 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, ZAP Rule
---
> **CRE**: [611-158](https://opencre.org/cre/611-158)
>
> **Part of**: [[cre-616-305]] › [[cre-433-442]] › [[cre-832-555]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V10.1.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x18-V10-Malicious.md#v101-code-integrity) | Verify that a code analysis tool is in use that can detect potentially malicious code, such as time functions, unsafe file operations and network connections. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [500](https://capec.mitre.org/data/definitions/500.html) | WebView Injection | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [749](https://cwe.mitre.org/data/definitions/749.html) | Exposed Dangerous Method or Function | curated |
| [618](https://cwe.mitre.org/data/definitions/618.html) | Exposed Unsafe ActiveX Method | automatic |
| [782](https://cwe.mitre.org/data/definitions/782.html) | Exposed IOCTL with Insufficient Access Control | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Third Party Javascript Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10110](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesBeta/src/main/java/org/zaproxy/zap/extension/pscanrulesBeta/JsFunctionScanRule.java) | Dangerous JS Functions | automatic |
| [90028](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/InsecureHttpMethodScanRule.java) | Insecure HTTP Method | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [611-158](https://opencre.org/cre/611-158). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
