---
id: "CRE-527-034"
title: "Protect communication between application components"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-527-034
excerpt: "CRE 527-034 · in Technical application security controls › Secure communication › Communication encryption · 26 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Proactive Controls, ZAP Rule
---
> **CRE**: [527-034](https://opencre.org/cre/527-034)
>
> **Part of**: [[cre-636-660]] › [[cre-278-646]] › [[cre-435-702]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]], [[standard-zap-rule]]

## Related CREs

- [[cre-170-772]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.9.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v114-configuration-architecture) | Verify the application encrypts communications between components, particularly when these components are in different containers, systems, sites, or cloud providers. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [65](https://capec.mitre.org/data/definitions/65.html) | Sniff Application Code | automatic |
| [102](https://capec.mitre.org/data/definitions/102.html) | Session Sidejacking | automatic |
| [117](https://capec.mitre.org/data/definitions/117.html) | Interception | automatic |
| [383](https://capec.mitre.org/data/definitions/383.html) | Harvesting Information via API Event Monitoring | automatic |
| [477](https://capec.mitre.org/data/definitions/477.html) | Signature Spoofing by Mixing Signed and Unsigned Content | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [319](https://cwe.mitre.org/data/definitions/319.html) | Cleartext Transmission of Sensitive Information | curated |
| [5](https://cwe.mitre.org/data/definitions/5.html) | J2EE Misconfiguration: Data Transmission Without Encryption | automatic |
| [614](https://cwe.mitre.org/data/definitions/614.html) | Sensitive Cookie in HTTPS Session Without 'Secure' Attribute | automatic |
| [1428](https://cwe.mitre.org/data/definitions/1428.html) | Reliance on HTTP instead of HTTPS | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [TLS Cipher String Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html) | curated |
|  | [Transport Layer Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C3](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c3-secure-database-access.html) | curated |

More: [[standard-owasp-proactive-controls]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10011](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CookieSecureFlagScanRule.java) | Cookie Without Secure Flag | automatic |
| [10035-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/StrictTransportSecurityScanRule.java) | Strict-Transport-Security Header Not Set | automatic |
| [10035-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/StrictTransportSecurityScanRule.java) | Strict-Transport-Security Disabled | automatic |
| [10035-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/StrictTransportSecurityScanRule.java) | Strict-Transport-Security Multiple Header Entries (Non-compliant with Spec) | automatic |
| [10035-4](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/StrictTransportSecurityScanRule.java) | Strict-Transport-Security Header on Plain HTTP Response | automatic |
| [10035-5](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/StrictTransportSecurityScanRule.java) | Strict-Transport-Security Missing Max-Age (Non-compliant with Spec) | automatic |
| [10035-6](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/StrictTransportSecurityScanRule.java) | Strict-Transport-Security Defined via META (Non-compliant with Spec) | automatic |
| [10035-7](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/StrictTransportSecurityScanRule.java) | Strict-Transport-Security Max-Age Malformed (Non-compliant with Spec) | automatic |
| [10035-8](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/StrictTransportSecurityScanRule.java) | Strict-Transport-Security Malformed Content (Non-compliant with Spec) | automatic |
| [10041](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InsecureFormLoadScanRule.java) | HTTP to HTTPS Insecure Transition in Form Post | automatic |
| [10042](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InsecureFormPostScanRule.java) | HTTPS to HTTP Insecure Transition in Form Post | automatic |
| [10094-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesAlpha/src/main/java/org/zaproxy/zap/extension/pscanrulesAlpha/Base64Disclosure.java) | ASP.NET ViewState Disclosure | automatic |
| [10094-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrulesAlpha/src/main/java/org/zaproxy/zap/extension/pscanrulesAlpha/Base64Disclosure.java) | Base64 Disclosure | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [527-034](https://opencre.org/cre/527-034). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
