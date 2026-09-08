---
status: accepted
revised: 2026-08-22
---

# Spec: Industry Compliance Standards and Frameworks

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix how my organization relates to compliance: as the floor, never the
program. The post turns the Industry Compliance Standards and Frameworks
chapter checklist of the *Defensive Security Handbook* into an operating
record: compliance standards are minimum requirements, and an organization
can be compliant and still be weak; regulatory compliance standards and
security frameworks are different instruments and are never confused; for
every regulated data type we hold, we can name the regulation that governs
it — FERPA for student records, GLBA for nonpublic personal information,
HIPAA for ePHI, PCI DSS for cardholder data, SOX for financial-reporting
controls; frameworks — CIS, CSA CCM, COSO, COBIT, the ISO 27000 series,
MITRE ATT&CK, NIST CSF — are used to build the program that compliance
merely attests; and the structural risks of regulated industries (financial,
government, healthcare) are understood, including CMMC, DoD Impact Levels,
FedRAMP, and FISMA on the government side and HITRUST on the healthcare
side. The load-bearing test: being compliant is never mistaken for being
secure — effective security combines compliance requirements with
established frameworks and security best practices.

## Audience

Security and engineering leaders in my organization who own the compliance
posture (so they know the literacy bar I hold them to); compliance officers
coordinating regulatory requirements; peer executives who need to reason
about audits, certifications, and regulated data without confusing the map
layers. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states compliance-as-floor, the
      law/standard/framework distinction, the data-to-regulation mapping,
      and the test: compliant is never mistaken for secure.
- [x] **Core concepts survive** — compliance standards as minimum
      requirements, not complete security programs; compliant-yet-weak as a
      real state; regulatory standards versus security frameworks;
      variation by industry, country, and governing body; the coordinating
      role of compliance officers; administrative, technical, and physical
      controls.
- [x] **The regulation map survives** — FERPA (student education records,
      education records versus directory information, consent contents,
      limited cybersecurity specifics); GLBA (financial institutions, NPI,
      the safeguards and the named control set, third-party obligations,
      FTC/FDIC/Fed/OCC enforcement); HIPAA (ePHI, covered organizations,
      the safeguard categories, required versus addressable specifications,
      risk assessment, HHS/FTC reporting, civil and criminal penalties);
      PCI DSS (cardholder data, PCI SSC, cardholder-data examples,
      consequences of failing validation); SOX (2002, corporate governance
      and financial reporting, Sections 302 and 404, COSO/COBIT support).
- [x] **The framework shelf survives** — CIS benchmarks and hardening
      guidance; CSA's Cloud Controls Matrix mapped to compliance standards;
      COSO's risk/controls/fraud guidance and its SOX association; COBIT's
      ISACA origin and four domains; the ISO 27000 series and the ISMS
      concept with the purpose of 27001–27006; MITRE ATT&CK's tactics,
      techniques, and procedures across enterprise, cloud, mobile, and ICS;
      NIST CSF's Core, Profiles, and Implementation Tiers.
- [x] **Regulated-industry context survives** — financial-sector risks
      (account takeover, third-party processor breaches, skimming, POS,
      mobile and internet banking, supply chain, legacy systems);
      government challenges and programs (CMMC's tiered model and the
      defense supply chain, DoD Impact Levels, FedRAMP and NIST SP 800-53,
      FISMA); healthcare's sensitive data, legacy medical systems, patching
      challenges, HIPAA penalty exposure, and HITRUST CSF as a harmonized
      framework.
- [x] **Final review survives as the completion check** — the literacy
      test: distinguishing law, standard, and framework; matching each
      regulation to its industry and data; explaining each framework's
      purpose; naming the government programs; explaining why finance,
      government, and healthcare are heavily regulated; and the closing
      commitments that compliant does not mean secure and that effective
      security combines compliance, frameworks, and practice.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* chapter checklist and the standards and frameworks the
      chapter itself names.

## Non-goals

- Not [[security-program]] — the program that compliance attests is built
  there; this record keeps the attestation from being mistaken for the
  program.
- Not [[policies]] and not [[standards-and-procedures]] — the documents
  that satisfy compliance obligations live there; this record decides which
  obligations apply.
- Not [[asset-management]] — knowing where regulated data lives is that
  record's job; this record names which regulation governs it once found.
- Not [[cloud-infrastructure]] — cloud control implementation lives there;
  this record covers the frameworks (CCM, FedRAMP) that shape it.
- Not a legal opinion — the record fixes executive literacy and operating
  posture; counsel interprets the statutes.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic (added later with the journal's visual
      layer)

## Open questions

- None.

## Decision log

- **2026-08-22** — Grounded in the Industry Compliance Standards and
  Frameworks chapter checklist of the *Defensive Security Handbook*
  (Brotherston, Berlin, Reyor), read through a practitioner-executive lens,
  as with every record in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 08 _ Industry Compliance Standards and Frameworks.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the final review.
- **External**
  - *Defensive Security Handbook*, 2nd edition (Lee Brotherston, Amanda
    Berlin, William F. Reyor III; O'Reilly) — the Industry Compliance
    Standards and Frameworks chapter.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
