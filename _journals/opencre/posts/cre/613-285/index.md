---
id: "CRE-613-285"
title: "Supply chain management"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-613-285
excerpt: "CRE 613-285 · in Development processes for security · 5 sub-requirements · 27 mappings to 4 standards and tools."
tags: ISO 27001, NIST 800-53 v5, NIST SSDF, SAMM
---
> **CRE**: [613-285](https://opencre.org/cre/613-285)
>
> **Part of**: [[cre-616-305]]
>
> **Maps to**: [[standard-iso-27001]], [[standard-nist-800-53-v5]], [[standard-nist-ssdf]], [[standard-samm]]

## Where It Sits

---begin mermaid---
graph LR
  n616305["Development processes for security"] --> n613285["Supply chain management"]
  n613285 --> n613287["Dependency integrity"]
  n613285 --> n613286["Dependency management"]
  n613285 --> n673475["Disallow unsupported/deprecated client-side t…"]
  n613285 --> n154031["Harden application by excluding unwanted func…"]
  n613285 --> n462245["Remove unnecessary elements from external com…"]
  style n613285 stroke-width:3px
---end mermaid---

## Contains

- [[cre-613-287]] — 7 more below
- [[cre-613-286]] — 3 more below
- [[cre-673-475]]
- [[cre-154-031]]
- [[cre-462-245]]

## Related CREs

- [[cre-307-507]]
- [[cre-424-242]]
- [[cre-307-242]]
- [[cre-433-442]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ISO 27001

| ID | Section | Link |
| --- | --- | --- |
| 5.19 | Information security in supplier relationships | curated |
| 5.20 | Addressing information security within supplier agreements | curated |
| 5.21 | Managing information security in the information and communication technology (ICT) supply chain | curated |
| 5.22 | Monitoring, review and change management of supplier services | curated |
| 5.23 | Information security for use of cloud services | curated |
| 8.30 | Outsourced development | curated |

More: [[standard-iso-27001]]

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [PM-30 Supply Chain Risk Management Strategy](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=PM-30) | curated |
|  | [SA-1 Policy and Procedures](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SA-1) | curated |
|  | [SA-4 Acquisition Process](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SA-4) | curated |
|  | [SA-9 External System Services](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SA-9) | curated |
|  | [SA-22 Unsupported System Components](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SA-22) | curated |
|  | [SR-1 Policy and Procedures](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SR-1) | curated |
|  | [SR-2 Supply Chain Risk Management Plan](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SR-2) | curated |
|  | [SR-3 Supply Chain Controls and Processes](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SR-3) | curated |
|  | [SR-4 Provenance](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SR-4) | curated |
|  | [SR-5 Acquisition Strategies, Tools, and Methods](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SR-5) | curated |
|  | [SR-6 Supplier Assessments and Reviews](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SR-6) | curated |
|  | [SR-7 Supply Chain Operations Security](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SR-7) | curated |
|  | [SR-8 Notification Agreements](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SR-8) | curated |
|  | [SR-9 Tamper Resistance and Detection](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SR-9) | curated |
|  | [SR-10 Inspection of Systems or Components](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SR-10) | curated |
|  | [SR-11 Component Authenticity](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SR-11) | curated |
|  | [SR-12 Component Disposal](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SR-12) | curated |

More: [[standard-nist-800-53-v5]]

### NIST SSDF

| ID | Section | Link |
| --- | --- | --- |
| PO.1.3 | Communicate requirements to all third parties who will provide commercial software components to the organization for reuse by the organization’s own software. (Formerly PW.3.1) | curated |
| PW.4.1 | Acquire and maintain well-secured software components (e.g., software libraries, modules, middleware, frameworks) from commercial, open- source, and other third-party developers for use by the organization’s software. | curated |
| PW.4.4 | Verify that acquired commercial, open-source, and all other third-party software components comply with the requirements, as defined by the organization, throughout their life cycles | curated |

More: [[standard-nist-ssdf]]

### SAMM

| ID | Section | Link |
| --- | --- | --- |
| [D-SR-B](https://owaspsamm.org/model/design/security-requirements/stream-b) | Supplier security | curated |

More: [[standard-samm]]

## Source

Generated from the OpenCRE catalogue entry [613-285](https://opencre.org/cre/613-285). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
