---
id: "CRE-267-468"
title: "Encrypt financial data at rest"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-267-468
excerpt: "CRE 267-468 · in Technical application security controls › Secure data storage › Encrypt data at rest › Securely store regulated data · 40 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [267-468](https://opencre.org/cre/267-468)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-400-007]] › [[cre-275-483]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V6.1.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x14-V6-Cryptography.md#v61-data-classification) | Verify that regulated financial data is stored encrypted while at rest, such as financial accounts, defaults or credit history, tax records, pay history, beneficiaries, or de-anonymized market or research records. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [31](https://capec.mitre.org/data/definitions/31.html) | Accessing/Intercepting/Modifying HTTP Cookies | automatic |
| [37](https://capec.mitre.org/data/definitions/37.html) | Retrieve Embedded Sensitive Data | automatic |
| [65](https://capec.mitre.org/data/definitions/65.html) | Sniff Application Code | automatic |
| [157](https://capec.mitre.org/data/definitions/157.html) | Sniffing Attacks | automatic |
| [158](https://capec.mitre.org/data/definitions/158.html) | Sniffing Network Traffic | automatic |
| [204](https://capec.mitre.org/data/definitions/204.html) | Lifting Sensitive Data Embedded in Cache | automatic |
| [383](https://capec.mitre.org/data/definitions/383.html) | Harvesting Information via API Event Monitoring | automatic |
| [384](https://capec.mitre.org/data/definitions/384.html) | Application API Message Manipulation via Man-in-the-Middle | automatic |
| [385](https://capec.mitre.org/data/definitions/385.html) | Transaction or Event Tampering via Application API Manipulation | automatic |
| [386](https://capec.mitre.org/data/definitions/386.html) | Application API Navigation Remapping | automatic |
| [387](https://capec.mitre.org/data/definitions/387.html) | Navigation Remapping To Propagate Malicious Content | automatic |
| [388](https://capec.mitre.org/data/definitions/388.html) | Application API Button Hijacking | automatic |
| [477](https://capec.mitre.org/data/definitions/477.html) | Signature Spoofing by Mixing Signed and Unsigned Content | automatic |
| [609](https://capec.mitre.org/data/definitions/609.html) | Cellular Traffic Intercept | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [311](https://cwe.mitre.org/data/definitions/311.html) | Missing Encryption of Sensitive Data | curated |
| [5](https://cwe.mitre.org/data/definitions/5.html) | J2EE Misconfiguration: Data Transmission Without Encryption | automatic |
| [312](https://cwe.mitre.org/data/definitions/312.html) | Cleartext Storage of Sensitive Information | automatic |
| [313](https://cwe.mitre.org/data/definitions/313.html) | Cleartext Storage in a File or on Disk | automatic |
| [314](https://cwe.mitre.org/data/definitions/314.html) | Cleartext Storage in the Registry | automatic |
| [315](https://cwe.mitre.org/data/definitions/315.html) | Cleartext Storage of Sensitive Information in a Cookie | automatic |
| [316](https://cwe.mitre.org/data/definitions/316.html) | Cleartext Storage of Sensitive Information in Memory | automatic |
| [317](https://cwe.mitre.org/data/definitions/317.html) | Cleartext Storage of Sensitive Information in GUI | automatic |
| [318](https://cwe.mitre.org/data/definitions/318.html) | Cleartext Storage of Sensitive Information in Executable | automatic |
| [319](https://cwe.mitre.org/data/definitions/319.html) | Cleartext Transmission of Sensitive Information | automatic |
| [526](https://cwe.mitre.org/data/definitions/526.html) | Cleartext Storage of Sensitive Information in an Environment Variable | automatic |
| [614](https://cwe.mitre.org/data/definitions/614.html) | Sensitive Cookie in HTTPS Session Without 'Secure' Attribute | automatic |
| [1428](https://cwe.mitre.org/data/definitions/1428.html) | Reliance on HTTP instead of HTTPS | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Abuse Case Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html) | curated |
|  | [User Privacy Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CRYP-04](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/04-Testing_for_Weak_Encryption.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10040](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/MixedContentScanRule.java) | Secure Pages Include Mixed Content | automatic |
| [10047](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/HttpsAsHttpScanRule.java) | HTTPS Content Available via HTTP | automatic |
| [10106](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/HttpOnlySiteScanRule.java) | HTTP Only Site | automatic |
| [10205-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/httpsInfo/src/main/java/org/zaproxy/zap/extension/httpsinfo/HttpsConfigScanRule.java) | HTTPS Configuration | automatic |
| [10205-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/httpsInfo/src/main/java/org/zaproxy/zap/extension/httpsinfo/HttpsConfigScanRule.java) | HTTPS Security Configuration Issues | automatic |
| [100006](https://github.com/zaproxy/community-scripts/blob/main/passive/f5_bigip_cookie_internal_ip.js) | Information Disclosure - IP Exposed via F5 BIG-IP Persistence Cookie | automatic |
| [100007](https://github.com/zaproxy/community-scripts/blob/main/passive/find%20base64%20strings.js) | Information Disclosure - Base64-encoded String | automatic |
| [100008](https://github.com/zaproxy/community-scripts/blob/main/passive/Find%20Credit%20Cards.js) | Information Disclosure - Credit Card Number | automatic |
| [100009](https://github.com/zaproxy/community-scripts/blob/main/passive/Find%20Emails.js) | Information Disclosure - Email Addresses | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [267-468](https://opencre.org/cre/267-468). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
