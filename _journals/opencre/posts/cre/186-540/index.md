---
id: "CRE-186-540"
title: "Do not expose data through HTTP verb"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-186-540
excerpt: "CRE 186-540 · in Technical application security controls › Secure communication › Minimize communication · 24 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [186-540](https://opencre.org/cre/186-540)
>
> **Part of**: [[cre-636-660]] › [[cre-278-646]] › [[cre-341-076]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Related CREs

- [[cre-486-813]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V8.3.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x16-V8-Data-Protection.md#v83-sensitive-private-data) | Verify that sensitive data is sent to the server in the HTTP message body or headers, and that query string parameters from any HTTP verb do not contain sensitive data. | curated |

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

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CRYP-03](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/03-Testing_for_Sensitive_Information_Sent_via_Unencrypted_Channels.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

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

Generated from the OpenCRE catalogue entry [186-540](https://opencre.org/cre/186-540). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
