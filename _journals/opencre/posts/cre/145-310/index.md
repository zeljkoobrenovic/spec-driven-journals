---
id: "CRE-145-310"
title: "Sanitize, disable, or sandbox untrusted SVG scriptable content"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-145-310
excerpt: "CRE 145-310 · in Technical application security controls › Input and output protection › Sanitization and sandboxing · 9 mappings to 3 standards and tools."
tags: ASVS, CWE, OWASP Cheat Sheets
---
> **CRE**: [145-310](https://opencre.org/cre/145-310)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-764-765]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-owasp-cheat-sheets]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.2.7](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v52-sanitization-and-sandboxing) | Verify that the application sanitizes, disables, or sandboxes user-supplied Scalable Vector Graphics (SVG) scriptable content, especially as they relate to XSS resulting from inline scripts, and foreignObject. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [159](https://cwe.mitre.org/data/definitions/159.html) | Improper Handling of Invalid Use of Special Elements | curated |
| [166](https://cwe.mitre.org/data/definitions/166.html) | Improper Handling of Missing Special Element | automatic |
| [167](https://cwe.mitre.org/data/definitions/167.html) | Improper Handling of Additional Special Element | automatic |
| [168](https://cwe.mitre.org/data/definitions/168.html) | Improper Handling of Inconsistent Special Elements | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) | curated |
|  | [DOM based XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html) | curated |
|  | [Server Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html) | curated |
|  | [Unvalidated Redirects and Forwards Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

## Source

Generated from the OpenCRE catalogue entry [145-310](https://opencre.org/cre/145-310). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
