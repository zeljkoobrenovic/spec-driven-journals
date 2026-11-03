---
id: "CRE-831-563"
title: "Avoid deserialization logic"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-831-563
excerpt: "CRE 831-563 · in Technical application security controls › Input and output protection › Deserialization Prevention · 7 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, ZAP Rule
---
> **CRE**: [831-563](https://opencre.org/cre/831-563)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-836-068]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.5.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v55-deserialization-prevention) | Verify that deserialization of untrusted data is avoided or is protected in both custom code and third-party libraries (such as JSON, XML and YAML parsers). | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [586](https://capec.mitre.org/data/definitions/586.html) | Object Injection | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [502](https://cwe.mitre.org/data/definitions/502.html) | Deserialization of Untrusted Data | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Deserialization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html) | curated |
|  | [XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html) | curated |
|  | [XML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [90002](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/JsoScanRule.java) | Java Serialization Object | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [831-563](https://opencre.org/cre/831-563). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
