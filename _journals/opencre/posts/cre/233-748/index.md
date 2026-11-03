---
id: "CRE-233-748"
title: "Configuration hardening"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-233-748
excerpt: "CRE 233-748 · in Technical application security controls · 3 sub-requirements · 34 mappings to 3 standards and tools."
tags: DevSecOps Maturity Model (DSOMM), PCI DSS, SAMM
---
> **CRE**: [233-748](https://opencre.org/cre/233-748)
>
> **Part of**: [[cre-636-660]]
>
> **Maps to**: [[standard-devsecops-maturity-model-dsomm]], [[standard-pci-dss]], [[standard-samm]]

## Where It Sits

---begin mermaid---
graph LR
  n636660["Technical application security controls"] --> n233748["Configuration hardening"]
  n233748 --> n636347["HTTP security headers"]
  n233748 --> n180488["Proper Configuration for all applications and…"]
  n233748 --> n814322["Whitelist data sources and sinks"]
  style n233748 stroke-width:3px
---end mermaid---

## Contains

- [[cre-636-347]] — 7 more below
- [[cre-180-488]]
- [[cre-814-322]]

## Related CREs

- [[cre-486-813]]
- [[cre-473-177]]
- [[cre-850-376]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### DevSecOps Maturity Model (DSOMM)

| ID | Section | Link |
| --- | --- | --- |
| [0de465a6-55a7-4343-af79-948bb5ff10ba](https://dsomm.owasp.org/activity-description?uuid=0de465a6-55a7-4343-af79-948bb5ff10ba) | Deployment: Evaluation of the trust of used components | automatic |
| [3a94d55e-fd82-4996-9eb3-20d23ff2a873](https://dsomm.owasp.org/activity-description?uuid=3a94d55e-fd82-4996-9eb3-20d23ff2a873) | Infrastructure Hardening: Applications are running in virtualized environments | automatic |
| [4ce24abd-8ba6-494c-828d-4d193e28e4a1](https://dsomm.owasp.org/activity-description?uuid=4ce24abd-8ba6-494c-828d-4d193e28e4a1) | Infrastructure Hardening: Isolated networks for virtual environments | automatic |
| [6df508ef-86fc-4c22-bd9f-646c3127ce7d](https://dsomm.owasp.org/activity-description?uuid=6df508ef-86fc-4c22-bd9f-646c3127ce7d) | Infrastructure Hardening: Filter outgoing traffic | automatic |
| [8b994601-575e-4ea5-b228-accb18c8e514](https://dsomm.owasp.org/activity-description?uuid=8b994601-575e-4ea5-b228-accb18c8e514) | Infrastructure Hardening: Infrastructure as Code | automatic |
| [11b3848e-e931-4146-a35d-35409ada24ee](https://dsomm.owasp.org/activity-description?uuid=11b3848e-e931-4146-a35d-35409ada24ee) | Infrastructure Hardening: Usage of security by default for components | automatic |
| [48e92bb1-fdba-40e8-b6c2-35de0d431833](https://dsomm.owasp.org/activity-description?uuid=48e92bb1-fdba-40e8-b6c2-35de0d431833) | Infrastructure Hardening: Immutable infrastructure | automatic |
| [070bb14b-e04a-4f3d-896a-a08eba7a35f9](https://dsomm.owasp.org/activity-description?uuid=070bb14b-e04a-4f3d-896a-a08eba7a35f9) | Infrastructure Hardening: Role based authentication and authorization | automatic |
| [82e499d1-f463-4a4b-be90-68812a874af6](https://dsomm.owasp.org/activity-description?uuid=82e499d1-f463-4a4b-be90-68812a874af6) | Infrastructure Hardening: Simple access control for systems | automatic |
| [363a3eea-baf9-4010-88ca-bb8186a2989d](https://dsomm.owasp.org/activity-description?uuid=363a3eea-baf9-4010-88ca-bb8186a2989d) | Development and Source Control: .gitignore | automatic |
| [598e9f13-1ac8-4a01-b85e-8fab93ee81de](https://dsomm.owasp.org/activity-description?uuid=598e9f13-1ac8-4a01-b85e-8fab93ee81de) | Infrastructure Hardening: MFA | automatic |
| [760f1056-b0ee-4f22-a35b-f65446f944ca](https://dsomm.owasp.org/activity-description?uuid=760f1056-b0ee-4f22-a35b-f65446f944ca) | Infrastructure Hardening: Virtual environments are limited | automatic |
| [5992c38c-8597-4035-89db-d15820d81c3a](https://dsomm.owasp.org/activity-description?uuid=5992c38c-8597-4035-89db-d15820d81c3a) | Infrastructure Hardening: Baseline Hardening of the environment | automatic |
| [8098e416-e1ed-4ae4-a561-83efbe76bf57](https://dsomm.owasp.org/activity-description?uuid=8098e416-e1ed-4ae4-a561-83efbe76bf57) | Infrastructure Hardening: MFA for admins | automatic |
| [29318d60-18ce-4526-80ea-f5928e49f639](https://dsomm.owasp.org/activity-description?uuid=29318d60-18ce-4526-80ea-f5928e49f639) | Application Hardening: Secure headers | automatic |
| [066084c6-1135-4635-9cc5-9e75c7c5459f](https://dsomm.owasp.org/activity-description?uuid=066084c6-1135-4635-9cc5-9e75c7c5459f) | Development and Source Control: Version control | automatic |
| [a86c1fbc-28fd-4610-89a3-a7f73acfe45f](https://dsomm.owasp.org/activity-description?uuid=a86c1fbc-28fd-4610-89a3-a7f73acfe45f) | Application Hardening: Containers are running as non-root | automatic |
| [ac8730a2-ccc0-465c-9550-d91edae9d5ee](https://dsomm.owasp.org/activity-description?uuid=ac8730a2-ccc0-465c-9550-d91edae9d5ee) | Development and Source Control: Require status checks to pass | automatic |
| [bfdacb52-1e3f-431d-ae72-d844a5e86415](https://dsomm.owasp.org/activity-description?uuid=bfdacb52-1e3f-431d-ae72-d844a5e86415) | Infrastructure Hardening: Usage of test and production environments | automatic |
| [c7d99b18-c3e1-4d22-b2e3-9aa9146c0b17](https://dsomm.owasp.org/activity-description?uuid=c7d99b18-c3e1-4d22-b2e3-9aa9146c0b17) | Development and Source Control: Block force pushes | automatic |
| [dcf9601b-b4f2-4e25-9143-e39af75f7c33](https://dsomm.owasp.org/activity-description?uuid=dcf9601b-b4f2-4e25-9143-e39af75f7c33) | Infrastructure Hardening: Hardening of the Environment | automatic |
| [e14de741-94b3-447c-8b07-eea947d82e61](https://dsomm.owasp.org/activity-description?uuid=e14de741-94b3-447c-8b07-eea947d82e61) | Infrastructure Hardening: Production near environments are used by developers | automatic |
| [e5386abf-9154-4752-a1a8-c3a8900f732d](https://dsomm.owasp.org/activity-description?uuid=e5386abf-9154-4752-a1a8-c3a8900f732d) | Infrastructure Hardening: Limitation of system events | automatic |
| [e7598ac4-b082-4e56-b7df-e2c6b426a5e2](https://dsomm.owasp.org/activity-description?uuid=e7598ac4-b082-4e56-b7df-e2c6b426a5e2) | Development and Source Control: Require a PR before merging | automatic |
| [ea6f69f7-54a5-4922-ac15-a77ff0c16162](https://dsomm.owasp.org/activity-description?uuid=ea6f69f7-54a5-4922-ac15-a77ff0c16162) | Development and Source Control: Dismiss stale PR approvals | automatic |
| [f0e01814-3b88-4bd0-a3a9-f91db001d20b](https://dsomm.owasp.org/activity-description?uuid=f0e01814-3b88-4bd0-a3a9-f91db001d20b) | Infrastructure Hardening: WAF baseline | automatic |
| [f0e01814-3b88-4bd0-a3a9-f91db001d20b-advanced](https://dsomm.owasp.org/activity-description?uuid=f0e01814-3b88-4bd0-a3a9-f91db001d20b-advanced) | Infrastructure Hardening: WAF Advanced | automatic |
| [f0e01814-3b88-4bd0-a3a9-f91db001d20b-medium](https://dsomm.owasp.org/activity-description?uuid=f0e01814-3b88-4bd0-a3a9-f91db001d20b-medium) | Infrastructure Hardening: WAF medium | automatic |
| [f8e80f18-2503-4e3e-b3bc-7f67bb28defe](https://dsomm.owasp.org/activity-description?uuid=f8e80f18-2503-4e3e-b3bc-7f67bb28defe) | Infrastructure Hardening: Usage of a chaos technology | automatic |

More: [[standard-devsecops-maturity-model-dsomm]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 1.2.1 | Configuration standards for NSC rulesets are: () Defined. () Implemented. () Maintained. (CUSTOMIZED APPROACH OBJECTIVE): The way that NSCs are configured and operate are defined and consistently applied. | automatic |
| 1.2.8 | Configuration files for NSCs are: () Secured from unauthorized access. () Kept consistent with active network configurations. (CUSTOMIZED APPROACH OBJECTIVE): NSCs cannot be defined or modified using untrusted configuration objects (including files). (APPLICABILITY NOTES): Any file or setting used to configure or synchronize NSCs is considered to be a “configuration file.” This includes files, automated and system-based controls, scripts, settings, infrastructure as code, or other parameters that are backed up, archived, or stored remotely. | automatic |
| 2.2.1 | Configuration standards are developed, implemented, and maintained to: () Cover all system components. () Address all known security vulnerabilities. () Be consistent with industry-accepted system hardening standards or vendor hardening recommendations. () Be updated as new vulnerability issues are identified, as defined in Requirement 6.3.1. () Be applied when new systems are configured and verified as in place before or immediately after a system component is connected to a production environment. (CUSTOMIZED APPROACH OBJECTIVE): All system components are configured securely and consistently and in accordance with industryaccepted hardening standards or vendor recommendations. | automatic |
| 2.2.6 | System security parameters are configured to prevent misuse. (CUSTOMIZED APPROACH OBJECTIVE): System components cannot be compromised because of incorrect security parameter configuration. | automatic |

More: [[standard-pci-dss]]

### SAMM

| ID | Section | Link |
| --- | --- | --- |
| [O-EM-A](https://owaspsamm.org/model/operations/environment-management/stream-a) | Configuration Hardening | curated |

More: [[standard-samm]]

## Source

Generated from the OpenCRE catalogue entry [233-748](https://opencre.org/cre/233-748). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
