---
id: "CRE-538-446"
title: "Sanitize unstructured data"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-538-446
excerpt: "CRE 538-446 · in Technical application security controls › Input and output protection › Sanitization and sandboxing · 69 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG)
---
> **CRE**: [538-446](https://opencre.org/cre/538-446)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-764-765]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.2.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v52-sanitization-and-sandboxing) | Verify that unstructured data is sanitized to enforce safety measures such as allowed characters and length. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [15](https://capec.mitre.org/data/definitions/15.html) | Command Delimiters | automatic |
| [34](https://capec.mitre.org/data/definitions/34.html) | HTTP Response Splitting | automatic |
| [41](https://capec.mitre.org/data/definitions/41.html) | Using Meta-characters in E-mail Headers to Inject Malicious Payloads | automatic |
| [52](https://capec.mitre.org/data/definitions/52.html) | Embedding NULL Bytes | automatic |
| [53](https://capec.mitre.org/data/definitions/53.html) | Postfix, Null Terminate, and Backslash | automatic |
| [81](https://capec.mitre.org/data/definitions/81.html) | Web Server Logs Tampering | automatic |
| [93](https://capec.mitre.org/data/definitions/93.html) | Log Injection-Tampering-Forging | automatic |
| [105](https://capec.mitre.org/data/definitions/105.html) | HTTP Request Splitting | automatic |
| [134](https://capec.mitre.org/data/definitions/134.html) | Email Injection | automatic |
| [460](https://capec.mitre.org/data/definitions/460.html) | HTTP Parameter Pollution (HPP) | automatic |
| [468](https://capec.mitre.org/data/definitions/468.html) | Generic Cross-Browser Cross-Domain Theft | automatic |
| [635](https://capec.mitre.org/data/definitions/635.html) | Alternative Execution Due to Deceptive Filenames | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [138](https://cwe.mitre.org/data/definitions/138.html) | Improper Neutralization of Special Elements | curated |
| [37](https://cwe.mitre.org/data/definitions/37.html) | Path Traversal: '/absolute/pathname/here' | automatic |
| [42](https://cwe.mitre.org/data/definitions/42.html) | Path Equivalence: 'filename.' (Trailing Dot) | automatic |
| [43](https://cwe.mitre.org/data/definitions/43.html) | Path Equivalence: 'filename....' (Multiple Trailing Dot) | automatic |
| [45](https://cwe.mitre.org/data/definitions/45.html) | Path Equivalence: 'file...name' (Multiple Internal Dot) | automatic |
| [46](https://cwe.mitre.org/data/definitions/46.html) | Path Equivalence: 'filename ' (Trailing Space) | automatic |
| [49](https://cwe.mitre.org/data/definitions/49.html) | Path Equivalence: 'filename/' (Trailing Slash) | automatic |
| [50](https://cwe.mitre.org/data/definitions/50.html) | Path Equivalence: '//multiple/leading/slash' | automatic |
| [52](https://cwe.mitre.org/data/definitions/52.html) | Path Equivalence: '/multiple/trailing/slash//' | automatic |
| [53](https://cwe.mitre.org/data/definitions/53.html) | Path Equivalence: '\multiple\\internal\backslash' | automatic |
| [54](https://cwe.mitre.org/data/definitions/54.html) | Path Equivalence: 'filedir\' (Trailing Backslash) | automatic |
| [56](https://cwe.mitre.org/data/definitions/56.html) | Path Equivalence: 'filedir*' (Wildcard) | automatic |
| [140](https://cwe.mitre.org/data/definitions/140.html) | Improper Neutralization of Delimiters | automatic |
| [141](https://cwe.mitre.org/data/definitions/141.html) | Improper Neutralization of Parameter/Argument Delimiters | automatic |
| [142](https://cwe.mitre.org/data/definitions/142.html) | Improper Neutralization of Value Delimiters | automatic |
| [143](https://cwe.mitre.org/data/definitions/143.html) | Improper Neutralization of Record Delimiters | automatic |
| [144](https://cwe.mitre.org/data/definitions/144.html) | Improper Neutralization of Line Delimiters | automatic |
| [145](https://cwe.mitre.org/data/definitions/145.html) | Improper Neutralization of Section Delimiters | automatic |
| [146](https://cwe.mitre.org/data/definitions/146.html) | Improper Neutralization of Expression/Command Delimiters | automatic |
| [147](https://cwe.mitre.org/data/definitions/147.html) | Improper Neutralization of Input Terminators | automatic |
| [148](https://cwe.mitre.org/data/definitions/148.html) | Improper Neutralization of Input Leaders | automatic |
| [149](https://cwe.mitre.org/data/definitions/149.html) | Improper Neutralization of Quoting Syntax | automatic |
| [150](https://cwe.mitre.org/data/definitions/150.html) | Improper Neutralization of Escape, Meta, or Control Sequences | automatic |
| [151](https://cwe.mitre.org/data/definitions/151.html) | Improper Neutralization of Comment Delimiters | automatic |
| [152](https://cwe.mitre.org/data/definitions/152.html) | Improper Neutralization of Macro Symbols | automatic |
| [153](https://cwe.mitre.org/data/definitions/153.html) | Improper Neutralization of Substitution Characters | automatic |
| [154](https://cwe.mitre.org/data/definitions/154.html) | Improper Neutralization of Variable Name Delimiters | automatic |
| [155](https://cwe.mitre.org/data/definitions/155.html) | Improper Neutralization of Wildcards or Matching Symbols | automatic |
| [156](https://cwe.mitre.org/data/definitions/156.html) | Improper Neutralization of Whitespace | automatic |
| [157](https://cwe.mitre.org/data/definitions/157.html) | Failure to Sanitize Paired Delimiters | automatic |
| [158](https://cwe.mitre.org/data/definitions/158.html) | Improper Neutralization of Null Byte or NUL Character | automatic |
| [159](https://cwe.mitre.org/data/definitions/159.html) | Improper Handling of Invalid Use of Special Elements | automatic |
| [160](https://cwe.mitre.org/data/definitions/160.html) | Improper Neutralization of Leading Special Elements | automatic |
| [161](https://cwe.mitre.org/data/definitions/161.html) | Improper Neutralization of Multiple Leading Special Elements | automatic |
| [162](https://cwe.mitre.org/data/definitions/162.html) | Improper Neutralization of Trailing Special Elements | automatic |
| [163](https://cwe.mitre.org/data/definitions/163.html) | Improper Neutralization of Multiple Trailing Special Elements | automatic |
| [164](https://cwe.mitre.org/data/definitions/164.html) | Improper Neutralization of Internal Special Elements | automatic |
| [165](https://cwe.mitre.org/data/definitions/165.html) | Improper Neutralization of Multiple Internal Special Elements | automatic |
| [166](https://cwe.mitre.org/data/definitions/166.html) | Improper Handling of Missing Special Element | automatic |
| [167](https://cwe.mitre.org/data/definitions/167.html) | Improper Handling of Additional Special Element | automatic |
| [168](https://cwe.mitre.org/data/definitions/168.html) | Improper Handling of Inconsistent Special Elements | automatic |
| [464](https://cwe.mitre.org/data/definitions/464.html) | Addition of Data Structure Sentinel | automatic |
| [626](https://cwe.mitre.org/data/definitions/626.html) | Null Byte Interaction Error (Poison Null Byte) | automatic |
| [790](https://cwe.mitre.org/data/definitions/790.html) | Improper Filtering of Special Elements | automatic |
| [791](https://cwe.mitre.org/data/definitions/791.html) | Incomplete Filtering of Special Elements | automatic |
| [792](https://cwe.mitre.org/data/definitions/792.html) | Incomplete Filtering of One or More Instances of Special Elements | automatic |
| [793](https://cwe.mitre.org/data/definitions/793.html) | Only Filtering One Instance of a Special Element | automatic |
| [794](https://cwe.mitre.org/data/definitions/794.html) | Incomplete Filtering of Multiple Instances of Special Elements | automatic |
| [795](https://cwe.mitre.org/data/definitions/795.html) | Only Filtering Special Elements at a Specified Location | automatic |
| [796](https://cwe.mitre.org/data/definitions/796.html) | Only Filtering Special Elements Relative to a Marker | automatic |
| [797](https://cwe.mitre.org/data/definitions/797.html) | Only Filtering Special Elements at an Absolute Position | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) | curated |
|  | [DOM based XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html) | curated |
|  | [Server Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html) | curated |
|  | [Unvalidated Redirects and Forwards Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-INPV-00](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

## Source

Generated from the OpenCRE catalogue entry [538-446](https://opencre.org/cre/538-446). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
