---
id: "CRE-737-086"
title: "Ignore/at least validate  filename metadata from untrusted origin (local file context, eg LFI)"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-737-086
excerpt: "CRE 737-086 · in Technical application security controls › Input and output protection › File handling › File execution · 12 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Web Security Testing Guide (WSTG)
---
> **CRE**: [737-086](https://opencre.org/cre/737-086)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-130-550]] › [[cre-451-082]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-web-security-testing-guide-wstg]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V12.3.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x20-V12-Files-Resources.md#v123-file-execution) | Verify that user-submitted filename metadata is validated or ignored to prevent the disclosure, creation, updating or removal of local files (LFI). | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [13](https://capec.mitre.org/data/definitions/13.html) | Subverting Environment Variable Values | automatic |
| [64](https://capec.mitre.org/data/definitions/64.html) | Using Slashes and URL Encoding Combined to Bypass Validation Logic | automatic |
| [72](https://capec.mitre.org/data/definitions/72.html) | URL Encoding | automatic |
| [76](https://capec.mitre.org/data/definitions/76.html) | Manipulating Web Input to File System Calls | automatic |
| [78](https://capec.mitre.org/data/definitions/78.html) | Using Escaped Slashes in Alternate Encoding | automatic |
| [79](https://capec.mitre.org/data/definitions/79.html) | Using Slashes in Alternate Encoding | automatic |
| [80](https://capec.mitre.org/data/definitions/80.html) | Using UTF-8 Encoding to Bypass Validation Logic | automatic |
| [267](https://capec.mitre.org/data/definitions/267.html) | Leverage Alternate Encoding | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [73](https://cwe.mitre.org/data/definitions/73.html) | External Control of File Name or Path | curated |
| [114](https://cwe.mitre.org/data/definitions/114.html) | Process Control | automatic |

More: [[standard-cwe]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-ATHZ-01](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/05-Authorization_Testing/01-Testing_Directory_Traversal_File_Include.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

## Source

Generated from the OpenCRE catalogue entry [737-086](https://opencre.org/cre/737-086). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
