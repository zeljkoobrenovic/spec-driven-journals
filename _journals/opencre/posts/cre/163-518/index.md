---
id: "CRE-163-518"
title: "Check uploaded archives for decompression attacks (eg zip bombs)"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-163-518
excerpt: "CRE 163-518 · in Technical application security controls › Input and output protection › File handling › File upload · 3 mappings to 3 standards and tools."
tags: ASVS, CWE, OWASP Cheat Sheets
---
> **CRE**: [163-518](https://opencre.org/cre/163-518)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-130-550]] › [[cre-621-287]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-owasp-cheat-sheets]]

## Related CREs

- [[cre-623-550]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V12.1.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x20-V12-Files-Resources.md#v121-file-upload) | Verify that the application checks compressed files (e.g. zip, gz, docx, odt) against maximum allowed uncompressed size and against maximum number of files before uncompressing the file. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [409](https://cwe.mitre.org/data/definitions/409.html) | Improper Handling of Highly Compressed Data (Data Amplification) | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

## Source

Generated from the OpenCRE catalogue entry [163-518](https://opencre.org/cre/163-518). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
