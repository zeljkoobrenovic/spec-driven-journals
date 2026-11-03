---
id: "CRE-411-684"
title: "Manual code review"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-411-684
excerpt: "CRE 411-684 · in Development processes for security › Verification · 4 mappings to 2 standards and tools."
tags: NIST SSDF, PCI DSS
---
> **CRE**: [411-684](https://opencre.org/cre/411-684)
>
> **Part of**: [[cre-616-305]] › [[cre-433-442]]
>
> **Maps to**: [[standard-nist-ssdf]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### NIST SSDF

| ID | Section | Link |
| --- | --- | --- |
| PW.7.1 | Determine whether code review (a person looks directly at the code to find issues) and/or code analysis (tools are used to find issues in code, either in a fully automated way or in conjunction with a person) should be used, as defined by the organization. | curated |
| PW.7.2 | Perform the code review and/or code analysis based on the organization’s secure coding standards, and record and triage all discovered issues and recommended remediations in the development team’s workflow or issue tracking system. | curated |

More: [[standard-nist-ssdf]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 6.2.3 | Bespoke and custom software is reviewed prior to being released into production or to customers, to identify and correct potential coding vulnerabilities, as follows: () Code reviews ensure code is developed according to secure coding guidelines. () Code reviews look for both existing and emerging software vulnerabilities. () Appropriate corrections are implemented prior to release. (CUSTOMIZED APPROACH OBJECTIVE): Bespoke and custom software cannot be exploited via coding vulnerabilities. (APPLICABILITY NOTES): This requirement for code reviews applies to all bespoke and custom software (both internal and public-facing), as part of the system development lifecycle. Public-facing web applications are also subject to additional controls, to address ongoing threats and vulnerabilities after implementation, as defined at PCI DSS Requirement 6.4. Code reviews may be performed using either manual or automated processes, or a combination of both. | automatic |
| 6.2.3.1 | If manual code reviews are performed for bespoke and custom software prior to release to production, code changes are: () Reviewed by individuals other than the originating code author, and who are knowledgeable about code-review techniques and secure coding practices. () Reviewed and approved by management prior to release. (CUSTOMIZED APPROACH OBJECTIVE): The manual code review process cannot be bypassed and is effective at discovering security vulnerabilities. (APPLICABILITY NOTES): Manual code reviews can be conducted by knowledgeable internal personnel or knowledgeable third-party personnel. An individual that has been formally granted accountability for release control and who is neither the original code author nor the code reviewer fulfills the criteria of being management. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [411-684](https://opencre.org/cre/411-684). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
