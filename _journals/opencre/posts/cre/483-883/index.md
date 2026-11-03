---
id: "CRE-483-883"
title: "When using stateless tokens, ensure cryptographically secure characteristics"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-483-883
excerpt: "CRE 483-883 · in Technical application security controls › Session management › Session integrity · 46 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [483-883](https://opencre.org/cre/483-883)
>
> **Part of**: [[cre-636-660]] › [[cre-177-260]] › [[cre-114-277]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V3.5.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V3-Session-management.md#v35-token-based-session-management) | Verify that stateless session tokens use digital signatures, encryption, and other countermeasures to protect against tampering, enveloping, replay, null cipher, and key substitution attacks. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [73](https://capec.mitre.org/data/definitions/73.html) | User-Controlled Filename | automatic |
| [75](https://capec.mitre.org/data/definitions/75.html) | Manipulating Writeable Configuration Files | automatic |
| [76](https://capec.mitre.org/data/definitions/76.html) | Manipulating Web Input to File System Calls | automatic |
| [85](https://capec.mitre.org/data/definitions/85.html) | AJAX Footprinting | automatic |
| [111](https://capec.mitre.org/data/definitions/111.html) | JSON Hijacking (aka JavaScript Hijacking) | automatic |
| [141](https://capec.mitre.org/data/definitions/141.html) | Cache Poisoning | automatic |
| [142](https://capec.mitre.org/data/definitions/142.html) | DNS Cache Poisoning | automatic |
| [148](https://capec.mitre.org/data/definitions/148.html) | Content Spoofing | automatic |
| [218](https://capec.mitre.org/data/definitions/218.html) | Spoofing of UDDI/ebXML Messages | automatic |
| [384](https://capec.mitre.org/data/definitions/384.html) | Application API Message Manipulation via Man-in-the-Middle | automatic |
| [385](https://capec.mitre.org/data/definitions/385.html) | Transaction or Event Tampering via Application API Manipulation | automatic |
| [386](https://capec.mitre.org/data/definitions/386.html) | Application API Navigation Remapping | automatic |
| [387](https://capec.mitre.org/data/definitions/387.html) | Navigation Remapping To Propagate Malicious Content | automatic |
| [388](https://capec.mitre.org/data/definitions/388.html) | Application API Button Hijacking | automatic |
| [463](https://capec.mitre.org/data/definitions/463.html) | Padding Oracle Crypto Attack | automatic |
| [665](https://capec.mitre.org/data/definitions/665.html) | Exploitation of Thunderbolt Protection Flaws | automatic |
| [701](https://capec.mitre.org/data/definitions/701.html) | Browser in the Middle (BiTM) | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [345](https://cwe.mitre.org/data/definitions/345.html) | Insufficient Verification of Data Authenticity | curated |
| [346](https://cwe.mitre.org/data/definitions/346.html) | Origin Validation Error | automatic |
| [347](https://cwe.mitre.org/data/definitions/347.html) | Improper Verification of Cryptographic Signature | automatic |
| [348](https://cwe.mitre.org/data/definitions/348.html) | Use of Less Trusted Source | automatic |
| [349](https://cwe.mitre.org/data/definitions/349.html) | Acceptance of Extraneous Untrusted Data With Trusted Data | automatic |
| [351](https://cwe.mitre.org/data/definitions/351.html) | Insufficient Type Distinction | automatic |
| [352](https://cwe.mitre.org/data/definitions/352.html) | Cross-Site Request Forgery (CSRF) | automatic |
| [353](https://cwe.mitre.org/data/definitions/353.html) | Missing Support for Integrity Check | automatic |
| [354](https://cwe.mitre.org/data/definitions/354.html) | Improper Validation of Integrity Check Value | automatic |
| [360](https://cwe.mitre.org/data/definitions/360.html) | Trust of System Event Data | automatic |
| [422](https://cwe.mitre.org/data/definitions/422.html) | Unprotected Windows Messaging Channel ('Shatter') | automatic |
| [494](https://cwe.mitre.org/data/definitions/494.html) | Download of Code Without Integrity Check | automatic |
| [616](https://cwe.mitre.org/data/definitions/616.html) | Incomplete Identification of Uploaded File Variables (PHP) | automatic |
| [646](https://cwe.mitre.org/data/definitions/646.html) | Reliance on File Name or Extension of Externally-Supplied File | automatic |
| [649](https://cwe.mitre.org/data/definitions/649.html) | Reliance on Obfuscation or Encryption of Security-Relevant Inputs without Integrity Checking | automatic |
| [924](https://cwe.mitre.org/data/definitions/924.html) | Improper Enforcement of Message Integrity During Transmission in a Communication Channel | automatic |
| [925](https://cwe.mitre.org/data/definitions/925.html) | Improper Verification of Intent by Broadcast Receiver | automatic |
| [939](https://cwe.mitre.org/data/definitions/939.html) | Improper Authorization in Handler for Custom URL Scheme | automatic |
| [940](https://cwe.mitre.org/data/definitions/940.html) | Improper Verification of Source of a Communication Channel | automatic |
| [1293](https://cwe.mitre.org/data/definitions/1293.html) | Missing Source Correlation of Multiple Independent Data | automatic |
| [1385](https://cwe.mitre.org/data/definitions/1385.html) | Missing Origin Validation in WebSockets | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [JSON Web Token for Java Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) | curated |
|  | [REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CRYP-04](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/04-Testing_for_Weak_Encryption.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10019-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/ContentTypeMissingScanRule.java) | Content-Type Header Missing | automatic |
| [10019-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/ContentTypeMissingScanRule.java) | Content-Type Header Empty | automatic |
| [40038](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/ForbiddenBypassScanRule.java) | Bypassing 403 | automatic |
| [90003](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/SubResourceIntegrityAttributeScanRule.java) | Sub Resource Integrity Attribute Missing | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [483-883](https://opencre.org/cre/483-883). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
