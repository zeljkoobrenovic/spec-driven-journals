---
id: "CRE-513-183"
title: "Error handling"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-513-183
excerpt: "CRE 513-183 · in Technical application security controls › Logging and error handling · 3 sub-requirements · 2 mappings to 2 standards and tools."
tags: OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG)
---
> **CRE**: [513-183](https://opencre.org/cre/513-183)
>
> **Part of**: [[cre-636-660]] › [[cre-842-876]]
>
> **Maps to**: [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]]

## Where It Sits

---begin mermaid---
graph LR
  n842876["Logging and error handling"] --> n513183["Error handling"]
  n513183 --> n612435["Show generic message for security exceptions…"]
  n513183 --> n118602["Use a standard last-resort error handler for…"]
  n513183 --> n863636["Use exception handling uniformly"]
  style n513183 stroke-width:3px
---end mermaid---

## Contains

- [[cre-612-435]]
- [[cre-118-602]]
- [[cre-863-636]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Error Handling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-ERRH-02](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/02-Testing_for_Stack_Traces.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

## Source

Generated from the OpenCRE catalogue entry [513-183](https://opencre.org/cre/513-183). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
