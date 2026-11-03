---
id: "CRE-402-706"
title: "Log relevant"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-402-706
excerpt: "CRE 402-706 · in Technical application security controls › Logging and error handling · 5 sub-requirements · 5 mappings to 4 standards and tools."
tags: NIST 800-53 v5, OWASP Cheat Sheets, OWASP Top 10 2021, OWASP Web Security Testing Guide (WSTG)
---
> **CRE**: [402-706](https://opencre.org/cre/402-706)
>
> **Part of**: [[cre-636-660]] › [[cre-842-876]]
>
> **Maps to**: [[standard-nist-800-53-v5]], [[standard-owasp-cheat-sheets]], [[standard-owasp-top-10-2021]], [[standard-owasp-web-security-testing-guide-wstg]]

## Where It Sits

---begin mermaid---
graph LR
  n842876["Logging and error handling"] --> n402706["Log relevant"]
  n402706 --> n443447["Log access control decisions"]
  n402706 --> n015063["Log access to sensitive data"]
  n402706 --> n184284["Log all security relevant events"]
  n402706 --> n841710["Log authentication decisions without exposing…"]
  n402706 --> n555048["Log events sufficiently to recreate their order"]
  style n402706 stroke-width:3px
---end mermaid---

## Contains

- [[cre-443-447]]
- [[cre-015-063]]
- [[cre-184-284]]
- [[cre-841-710]]
- [[cre-555-048]]

## Related CREs

- [[cre-113-133]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [AU-2 Event Logging](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AU-2) | curated |
|  | [AU-3 Content of Audit Records](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AU-3) | curated |

More: [[standard-nist-800-53-v5]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Top 10 2021

| ID | Section | Link |
| --- | --- | --- |
| [A09](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/) | Logging and Monitoring Failures | curated |

More: [[standard-owasp-top-10-2021]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CONF-02](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/02-Test_Application_Platform_Configuration.html#logging) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

## Source

Generated from the OpenCRE catalogue entry [402-706](https://opencre.org/cre/402-706). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
