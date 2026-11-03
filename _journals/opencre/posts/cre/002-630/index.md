---
id: "CRE-002-630"
title: "Generate a new session token after authentication"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-002-630
excerpt: "CRE 002-630 · in Technical application security controls › Session management › Session token generation · 15 mappings to 9 standards and tools."
tags: ASVS, CAPEC, CWE, NIST 800-53 v5, NIST 800-63, OWASP Cheat Sheets, OWASP Proactive Controls, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [002-630](https://opencre.org/cre/002-630)
>
> **Part of**: [[cre-636-660]] › [[cre-177-260]] › [[cre-716-526]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-nist-800-53-v5]], [[standard-nist-800-63]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V3.2.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V3-Session-management.md#v32-session-binding) | Verify the application generates a new session token on user authentication. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [21](https://capec.mitre.org/data/definitions/21.html) | Exploitation of Trusted Identifiers | automatic |
| [31](https://capec.mitre.org/data/definitions/31.html) | Accessing/Intercepting/Modifying HTTP Cookies | automatic |
| [39](https://capec.mitre.org/data/definitions/39.html) | Manipulating Opaque Client-based Data Tokens | automatic |
| [59](https://capec.mitre.org/data/definitions/59.html) | Session Credential Falsification through Prediction | automatic |
| [60](https://capec.mitre.org/data/definitions/60.html) | Reusing Session IDs (aka Session Replay) | automatic |
| [61](https://capec.mitre.org/data/definitions/61.html) | Session Fixation | automatic |
| [196](https://capec.mitre.org/data/definitions/196.html) | Session Credential Falsification through Forging | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [384](https://cwe.mitre.org/data/definitions/384.html) | Session Fixation | curated |

More: [[standard-cwe]]

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [SC-23(3)](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SC-23) | curated |

More: [[standard-nist-800-53-v5]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 7.1 | curated |

More: [[standard-nist-800-63]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C6](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c6-implement-digital-identity.html) | curated |

More: [[standard-owasp-proactive-controls]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-SESS-03](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/03-Testing_for_Session_Fixation.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [40013](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/SessionFixationScanRule.java) | Session Fixation | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [002-630](https://opencre.org/cre/002-630). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
