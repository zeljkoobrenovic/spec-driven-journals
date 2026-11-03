---
id: "CRE-455-885"
title: "Credentials directives"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-455-885
excerpt: "CRE 455-885 · in Technical application security controls › Authentication · 8 sub-requirements · 4 mappings to 2 standards and tools."
tags: OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG)
---
> **CRE**: [455-885](https://opencre.org/cre/455-885)
>
> **Part of**: [[cre-636-660]] › [[cre-633-428]]
>
> **Maps to**: [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]]

## Where It Sits

---begin mermaid---
graph LR
  n633428["Authentication"] --> n455885["Credentials directives"]
  n455885 --> n158874["Allow long passwords"]
  n455885 --> n103707["Allow unicode in passwords"]
  n455885 --> n715681["Avoid password truncation, with exception of…"]
  n455885 --> n338370["Do not enforce password rotation rules or his…"]
  n455885 --> n807565["Do not limit character types for password com…"]
  n455885 --> n027555["Enforce user passwords are of sufficient mini…"]
  n455885 --> n604025["Provide a password strength meter"]
  n455885 --> n576651["Validate new passwords are not in commonly br…"]
  style n455885 stroke-width:3px
---end mermaid---

## Contains

- [[cre-158-874]]
- [[cre-103-707]]
- [[cre-715-681]]
- [[cre-338-370]]
- [[cre-807-565]]
- [[cre-027-555]]
- [[cre-604-025]]
- [[cre-576-651]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Choosing and Using Security Questions Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html) | curated |
|  | [Credential Stuffing Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html) | curated |
|  | [Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-ATHN-07](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/04-Authentication_Testing/07-Testing_for_Weak_Password_Policy.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

## Source

Generated from the OpenCRE catalogue entry [455-885](https://opencre.org/cre/455-885). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
