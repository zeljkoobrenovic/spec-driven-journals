---
id: "CRE-248-646"
title: "Disable insecure SSL/TLS versions"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-248-646
excerpt: "CRE 248-646 · in Technical application security controls › Secure communication › TLS · 14 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [248-646](https://opencre.org/cre/248-646)
>
> **Part of**: [[cre-636-660]] › [[cre-278-646]] › [[cre-228-551]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Related CREs

- [[cre-170-772]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V9.1.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x17-V9-Communications.md#v91-client-communication-security) | Verify that only the latest recommended versions of the TLS protocol are enabled, such as TLS 1.2 and TLS 1.3. The latest version of the TLS protocol should be the preferred option. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [20](https://capec.mitre.org/data/definitions/20.html) | Encryption Brute Forcing | automatic |
| [112](https://capec.mitre.org/data/definitions/112.html) | Brute Force | automatic |
| [192](https://capec.mitre.org/data/definitions/192.html) | Protocol Analysis | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [326](https://cwe.mitre.org/data/definitions/326.html) | Inadequate Encryption Strength | curated |
| [328](https://cwe.mitre.org/data/definitions/328.html) | Use of Weak Hash | automatic |
| [759](https://cwe.mitre.org/data/definitions/759.html) | Use of a One-Way Hash without a Salt | automatic |
| [760](https://cwe.mitre.org/data/definitions/760.html) | Use of a One-Way Hash with a Predictable Salt | automatic |
| [916](https://cwe.mitre.org/data/definitions/916.html) | Use of Password Hash With Insufficient Computational Effort | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [HTTP Strict Transport Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html) | curated |
|  | [TLS Cipher String Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html) | curated |
|  | [Transport Layer Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CRYP-01](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/01-Testing_for_Weak_SSL_TLS_Ciphers_Insufficient_Transport_Layer_Protection.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10105-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InsecureAuthenticationScanRule.java) | Weak Authentication Method | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [248-646](https://opencre.org/cre/248-646). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
