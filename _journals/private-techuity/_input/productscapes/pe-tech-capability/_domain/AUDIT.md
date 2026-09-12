# Balance audit: pe-tech-capability

Reviewed: 11 September 2026. Integrity: **pass**.

The authored model follows [INPUT.md](INPUT.md) and the boundary, evidence, and
assumptions in [DOMAIN.md](DOMAIN.md). It is a complete proposal model, not an
inventory of an implemented Vortex capability.

## Authored coverage

| Artifact | Count and coverage |
|---|---|
| Source JSON | 14 authored files; no scaffold tokens or unauthored collections |
| Customers | 3 groups, all 8 roles named in the input |
| Jobs and adoption | 16 jobs, 8 journeys using the six prescribed adoption stages |
| KPI pyramids | 16 pyramids, 144 nodes, 80 measurable leaves with null baselines |
| Customer strategy | Distinct year 1, 3, and 5 focus for each persona |
| Product offerings | 11 connected services/artifacts under Technology Value Creation Platform |
| Deployment | 1 proposed permissioned runtime boundary and 4 audience/workspace surfaces |
| Product bricks | 26 across Invest, Align, Accelerate, Learn, Scale, and Exit |
| Modules | 91 across all six permitted architectural layers |
| Outcome streams | 14 streams with 56 steps, decision facts, frictions, and capability references |
| Data | 26 logical records, 7 proposed store boundaries, explicit accountability |
| Teams | 5 logical responsibility areas; actual headcount is deliberately unspecified |
| Insights | 11 insights, 6 sources: the supplied brief and 5 verified public pages |
| Customer relations | 12 directed, scoped evidence and decision handoffs |
| Peers and alternatives | 3 sourced offerings, distinguished as a peer model or service alternative |
| Residuality | 6 hypothetical candidate stressors; no claimed implementation or survival tests |
| Introduction | Ready beginner tutorial with a fictional complete case and application questions |
| Icons | Custom domain mark, 26 capability symbols, 14 workflow symbols, and 144 KPI icons; 11 product offerings reuse their primary capability symbols; configured customer portraits retained |

All ten input accelerators are represented. Each includes the diagnostic,
contextual benchmark or explicit absence, decision framework, recommended actions,
and outcome review. The assessment preserves all seven dimensions. The thesis
preserves the one-page contract. The 100-day handoff retains three to five accepted
priorities and the original findings, with other work visible in a backlog.

## Density compared with the reference

Counts were read from the current `ride-sharing-marketplace` source model, rather
than inferred from a target quota.

| Dimension | This domain | Ride-sharing reference | Interpretation |
|---|---:|---:|---|
| Personas | 8 | 4 | Separate investment, execution, governance, exit, and LP decisions matter |
| Bricks | 26 | 20 | Includes the ten accelerators and the shared decision/evidence infrastructure |
| Data assets | 26 | 17 | Distinct logical decision records, not 26 physical databases |
| Teams | 5 | 24 | Shared responsibility areas fit a specialist operating capability |
| Products | 11 | 3 | Named service outputs with distinct users; not 11 separately sold applications |
| Insights | 11 | 8 | The brief is the primary design basis, with limited public contextual research |
| Competitors/alternatives | 3 | 11 | Focused peer/service comparison; no padding with unrelated investment firms |

## Traceability and realism

- Every customer has two jobs, an adoption journey, both KPI pyramids, strategy
  horizons, at least one offering, and a responsible team.
- Every job step references a real stream with the correct display name. Its
  stream has substantive capability overlap with the customer's offerings; the
  shared access-control brick alone is not counted as outcome coverage.
- Every brick is used by a stream, connected to at least one product through
  deployment, and assigned to exactly one accountable team. There are no orphan
  bricks or duplicate primary ownership assignments.
- Every logical data asset is used by a brick, has a real team owner, and refers
  to valid stores and derivation sources. A capability's primary record and its
  accountable team agree.
- Source, insight, customer, job, KPI, journey, relationship, stream, deployment,
  module, and team references resolve. The committee thesis offering includes
  the value scorecard needed to revisit earlier decisions.
- All pyramids fan out. Four operational customer pyramids have four levels;
  twelve governance/business trees have three levels to avoid artificial causal
  precision. All 80 leaves have units and null current values. No single-child
  chains, duplicate persona KPI IDs, or unresolved strategy/team metric names remain.
- Coaching, candidates, company evidence, peer learning, and buyer/LP claims have
  explicit disclosure boundaries. Company and fund authorities retain their
  decisions; proposed modules and teams do not imply actual deployed systems or staffing.
- Competition contains no business statistics needing invented periods, scope,
  or sources. Public source observations and proposed implications are separate.
- The illustrative investment and onboarding figures in the input are not seeded
  as company baselines, targets, or realized results.

## P1 — realism or traceability breaks

None found after validation, the cross-artifact review, and browser checks.

## P2 — implementation evidence to obtain

These are explicit limits of a proposal, not unfilled source artifacts:

- Confirm actual sponsor, company decision rights, role capacity, specialist funding,
  and confidentiality arrangements before assigning real work. Update through
  `set-domain-strategy` and `edit-teams` when evidence is available.
- Establish approved company measurements, periods, baselines, compatible cohorts,
  and contribution-review rules before setting targets or drawing comparisons.
  Use `edit-customers` and `edit-data-assets` for the verified definitions.
- Confirm systems, access grants, retention, residency, disclosure authority, and
  any integration contracts before implementation. Use `edit-products`,
  `edit-product-bricks`, and `edit-data-assets` to replace proposed boundaries.

## Presentation

The domain mark and all 40 capability/workflow symbols were generated with Codex
built-in image generation. The 11 product offerings use matching capability icons.
The selected customer portraits remain seven JPEGs and the existing CTO PNG;
seven additional PNG portraits are preserved as alternatives. The full
[prompt set](ICON-PROMPTS.md) records the generation requests and product mapping.
An [icon preview](ICON-PREVIEW.html) shows the 41 monochrome symbols at 110 pixels.

All 49 source PNGs from the initial icon set decode successfully; original
image-tool files are retained separately. The nearshore and integration symbols
use the current transparent variants. The generated site includes byte-identical
copies of the current source assets and all 11 product icons. All eight configured
portrait references resolve.

All 144 KPI nodes have distinct generated icons and explicit `icon` references.
The [KPI icon preview](KPI-ICON-PREVIEW.html) shows each image at the customer
pages' 50-pixel display size. Image decoding and source-to-published file checks
pass. Comparing customer data before and after KPI completion confirms that only
KPI icon references changed; portraits, definitions, values, and relationships
were preserved.

## Verification

Commands run from `productscape-examples`:

```sh
python3 productscapes.py validate pe-tech-capability --strict-ids
python3 productscapes.py check-kpis pe-tech-capability
python3 productscapes.py build pe-tech-capability
```

Strict validation and KPI checks pass. The selected domain builds successfully;
section builds also verified the authored tutorial and final capability ordering.
The generated site contains **106 HTML pages**.

A headless Chromium pass opened every page through a local static server: **106
pages, zero JavaScript errors, zero HTTP resource failures, zero broken local links,
and zero empty pages**. Interactive checks opened the CTO jobs, journeys, KPIs,
product vision, and insights tabs. The tutorial walkthrough and answer disclosures
worked; domain home and tutorial fit a 390-pixel viewport without horizontal overflow.
Wide and narrow screenshots were reviewed. The full 106-page browser pass was
repeated after installing the custom icons, with the same clean result. The complete
41-symbol preview was also reviewed at the site's 110-pixel display size.

After KPI icon generation completed, the customer section was rebuilt with
`python3 productscapes.py build pe-tech-capability --sections customers`. Strict
validation and KPI checks passed. A focused Chromium check opened all eight
personas' KPI tabs and matched all **144 loaded images** to their configured
filenames, with zero fallback icons, HTTP failures, or JavaScript errors. All
eight persona icon galleries were visually reviewed.

The supplied `INPUT.md` content is unchanged from the start of this task. Its
SHA-256 is `7c6beed7b01b7e9352e426b41e0dab6c7b55f904626e0adab075b2ab8c41ac18`.
Changes are limited to this domain's sources and generated pages plus its entry
in `docs/index.html`; the pre-existing staged/unstaged input state was preserved.

Overall: a complete, connected proposal with explicit implementation assumptions
and a working static site.
