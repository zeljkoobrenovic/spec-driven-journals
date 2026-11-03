---
id: "CRE-543-512"
title: "Verify content-type for REST services"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-543-512
excerpt: "CRE 543-512 · in Technical application security controls › Input and output protection › API/web services › RESTful · 19 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, ZAP Rule
---
> **CRE**: [543-512](https://opencre.org/cre/543-512)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-118-110]] › [[cre-071-288]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V13.2.5](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x21-V13-API.md#v132-restful-web-service) | Verify that REST services explicitly check the incoming Content-Type to be the expected one, such as application/xml or application/json. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [34](https://capec.mitre.org/data/definitions/34.html) | HTTP Response Splitting | automatic |
| [105](https://capec.mitre.org/data/definitions/105.html) | HTTP Request Splitting | automatic |
| [273](https://capec.mitre.org/data/definitions/273.html) | HTTP Response Smuggling | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [436](https://cwe.mitre.org/data/definitions/436.html) | Interpretation Conflict | curated |
| [86](https://cwe.mitre.org/data/definitions/86.html) | Improper Neutralization of Invalid Characters in Identifiers in Web Pages | automatic |
| [113](https://cwe.mitre.org/data/definitions/113.html) | Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Request/Response Splitting') | automatic |
| [115](https://cwe.mitre.org/data/definitions/115.html) | Misinterpretation of Input | automatic |
| [437](https://cwe.mitre.org/data/definitions/437.html) | Incomplete Model of Endpoint Features | automatic |
| [444](https://cwe.mitre.org/data/definitions/444.html) | Inconsistent Interpretation of HTTP Requests ('HTTP Request/Response Smuggling') | automatic |
| [626](https://cwe.mitre.org/data/definitions/626.html) | Null Byte Interaction Error (Poison Null Byte) | automatic |
| [650](https://cwe.mitre.org/data/definitions/650.html) | Trusting HTTP Permission Methods on the Server Side | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) | curated |
|  | [REST Assessment Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Assessment_Cheat_Sheet.html) | curated |
|  | [REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [90011-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CharsetMismatchScanRule.java) | Charset Mismatch (Header Versus Meta Content-Type Charset) | automatic |
| [90011-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CharsetMismatchScanRule.java) | Charset Mismatch (Header Versus Meta Charset) | automatic |
| [90011-3](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CharsetMismatchScanRule.java) | Charset Mismatch (Meta Charset Versus Meta Content-Type Charset) | automatic |
| [90011-4](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/CharsetMismatchScanRule.java) | Charset Mismatch | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [543-512](https://opencre.org/cre/543-512). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
