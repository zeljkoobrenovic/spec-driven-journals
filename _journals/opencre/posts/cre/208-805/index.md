---
id: "CRE-208-805"
title: "Disable debug mode in production"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-208-805
excerpt: "CRE 208-805 · in Technical application security controls › Input and output protection › Prevent security disclosure · 33 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, PCI DSS, ZAP Rule
---
> **CRE**: [208-805](https://opencre.org/cre/208-805)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-308-515]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-pci-dss]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V14.3.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x22-V14-Config.md#v143-unintended-security-disclosure) | Verify that web or application server and application framework debug modes are disabled in production to eliminate debug features, developer consoles, and unintended security disclosures. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [170](https://capec.mitre.org/data/definitions/170.html) | Web Application Fingerprinting | automatic |
| [694](https://capec.mitre.org/data/definitions/694.html) | System Location Discovery | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [497](https://cwe.mitre.org/data/definitions/497.html) | Exposure of Sensitive System Information to an Unauthorized Control Sphere | curated |
| [214](https://cwe.mitre.org/data/definitions/214.html) | Invocation of Process Using Visible Sensitive Information | automatic |
| [548](https://cwe.mitre.org/data/definitions/548.html) | Exposure of Information Through Directory Listing | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Error Handling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 6.5.6 | Test data and test accounts are removed from system components before the system goes into production. (CUSTOMIZED APPROACH OBJECTIVE): Test data and test accounts cannot exist in production environments. | automatic |

More: [[standard-pci-dss]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [0](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/DirectoryBrowsingScanRule.java) | Directory Browsing | automatic |
| [2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InfoPrivateAddressDisclosureScanRule.java) | Private IP Disclosure | automatic |
| [10009](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/InPageBannerInfoLeakScanRule.java) | In Page Banner Information Leak | automatic |
| [10033](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/DirectoryBrowsingScanRule.java) | Directory Browsing | automatic |
| [10036-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/ServerHeaderInfoLeakScanRule.java) | Server Leaks its Webserver Application via \Server\ HTTP Response Header Field | automatic |
| [10036-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/ServerHeaderInfoLeakScanRule.java) | Server Leaks Version Information via \Server\ HTTP Response Header Field | automatic |
| [10037](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/XPoweredByHeaderInfoLeakScanRule.java) | Server Leaks Information via \X-Powered-By\ HTTP Response Header Field(s) | automatic |
| [10039](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/XBackendServerInformationLeakScanRule.java) | X-Backend-Server Header Information Leak | automatic |
| [10096](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/TimestampDisclosureScanRule.java) | Timestamp Disclosure - Unix | automatic |
| [10097-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - LanMan / DES | automatic |
| [10097-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - Kerberos AFS DES | automatic |
| [10097-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - OpenBSD Blowfish | automatic |
| [10097-4](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - MD5 Crypt | automatic |
| [10097-5](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - SHA-256 Crypt | automatic |
| [10097-6](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - SHA-512 Crypt | automatic |
| [10097-7](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - BCrypt | automatic |
| [10097-8](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - NTLM | automatic |
| [10097-9](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - Salted SHA-1 | automatic |
| [10097-10](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - SHA-512 | automatic |
| [10097-11](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - SHA-384 | automatic |
| [10097-12](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - SHA-256 | automatic |
| [10097-13](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - SHA-224 | automatic |
| [10097-14](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - SHA-1 | automatic |
| [10097-15](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - LanMan | automatic |
| [10097-16](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/HashDisclosureScanRule.java) | Hash Disclosure - MD4 / MD5 | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [208-805](https://opencre.org/cre/208-805). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
