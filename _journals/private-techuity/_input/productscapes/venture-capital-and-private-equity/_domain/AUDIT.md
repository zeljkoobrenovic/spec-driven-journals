# Balance audit: venture-capital-and-private-equity

Reviewed: 8 September 2026. Integrity: **pass**.

This is a complete example model of investment partnerships as products, informed
by public Vortex material. It is not an inventory of Vortex's actual software,
staffing, private fund agreements, or measured performance. Evidence boundaries
and open questions are in [DOMAIN.md](DOMAIN.md).

## Method and structural reference

Used the toolkit's `new-product-domain`, `set-domain-strategy`, customer, brick,
stream, data-asset, product, team, competition, validation, and balance-audit skills.
Toolkit schemas and the empty domain starter established the contracts. The
existing `bi-dashboard-extensions-platform` provided examples of customer relations
and team charter syntax; no company facts or staffing were copied. The
`ride-sharing-marketplace` domain supplied the density comparison below.

| Artifact | New domain | Ride-sharing reference |
|---|---:|---:|
| Customer groups / personas | 4 / 5 | 4 / 4 |
| Jobs to be done | 11 | 8 |
| Adoption journeys | 5 | 6 |
| Product bricks | 23 | 20 |
| Layered modules | 101 | 118 |
| Outcome streams | 10 | 10 |
| Data assets | 23 | 17 |
| Products | 5 | 3 |
| Responsibility teams | 5 | 24 |
| Competitive landscape entries | 8 | 11 |
| Sourced insights | 11 | 8 |

Additional authored content: 5 logical stores, 6 delivery channels, 9 customer
relations, 4 hypothetical stressors, and 152 KPI nodes in 10 pyramids. The landscape
contains seven external players and one clearly labeled Vortex reference row.

## P1 — realism and traceability

No unresolved P1 findings.

- Every persona has substantive jobs, a six-stage adoption journey, both KPI
  pyramids, distinct 1/3/5-year horizons, a primary product, and a serving team.
  Journey narratives describe adopting the partnership or internal workbench.
  For investment products, trial means bounded evaluation of the relationship or
  service; no trial investment or assumed redemption right is introduced.
- All 23 bricks occur in streams and deployments and have exactly one primary
  owning team. All 23 data assets have an owning team and one accountable
  record-owning brick, with matching ownership. Stores, stewards, and derivations
  resolve. Product deployment mappings also cover transitive brick dependencies;
  this does not grant end customers access to internal capabilities.
- Stream-level dependencies match their flow steps. JTBD references and names,
  product/customer names, insight/customer/job/KPI references, team dependencies,
  and stressor impacts resolve. All 11 insights identify sources and distinguish
  the public observation from its modeling implication.
- All KPI trees fan out, with no single-child nodes; every metric has a unit and
  definition. The 82 terminal measurements are null, not invented baselines.
  All strategy KPI names and team charter metrics resolve to the relevant
  customer definitions. Investor measures explicitly distinguish DPI, TVPI,
  net IRR, unrealized value, and actual cash. Management economic measures refer
  to the portfolio company rather than incorrectly treating its revenue as
  manager revenue.
- Source-backed competition statistics preserve metric, value, reporting or
  observation period, scope, source title, and official URL. AUM, capital raised,
  transaction counts, ticket sizes, and software customer counts are not treated
  as comparable market shares. No reported gross growth or value-creation figure
  is presented as an LP net return.

## P2 — intentional scope and unverified operating details

The five teams represent shared responsibilities at a specialist manager, including
external administration and specialist support. Copying the reference domain's
24-team structure would be inappropriate. Staffing and group leadership counts
are unspecified; unknown headcounts are not represented as zero.

The 23 bricks describe bounded business capabilities. Their 101 modules distribute
across UI (23), interfaces (23), durable services (23), integration (20), workers
(9), and stateless analysis (3), connected by 43 explicit brick dependencies.
Configured tools and assisted workflows can implement multiple bricks together;
the model does not call for 23 bespoke deployed services. Valuation, investment,
company governance, and payment authority remain distinct.

The growth-founder path reflects a public high-growth portfolio category.
Availability for new investments, minority terms, investor eligibility, fees,
fundraising status, co-investment rights, actual reporting cadence, providers'
private functionality, and infrastructure remain unverified. Fund-specific
sustainability and geography boundaries are retained. Operationalizing this model
would require private mandate and process evidence, baseline measurements, and
confirmed data-governance schedules; those gaps are explicit rather than populated
with fictitious values.

## P3 — presentation and generated documentation

The current domain build contains 93 generated HTML pages under
`docs/vortexcp/venture-capital-and-private-equity/`, with its entry point at
`start/index.html`. The main `docs/index.html` includes the new domain. All 23
product bricks have dedicated monochrome PNG icons with transparent backgrounds,
authored with the imagegen skill and built-in image generation tool. Source assets
live in `product-bricks/icons/`; the generation prompts and asset mapping are in
[BRICK-ICONS.md](BRICK-ICONS.md). All images passed PNG integrity and transparency
checks and a visual review. They are capability illustrations, not Vortex brand
marks or private screenshots.

All 715 static local link and asset references resolve. Browser checks across 14
representative index and detail pages found no JavaScript errors, broken rendered
links, or broken images. All 23 brick cards load their dedicated icon filenames,
and generated icons match the source PNGs byte for byte. Team filtering works,
and unspecified headcounts display
as not set. A small toolkit renderer correction preserves missing and null staffing
through team/group totals while retaining an explicit zero as zero. The earlier
documentation update passed all 13 toolkit tests, including a regression covering
unknown, zero, known, and nested totals.

## Validation

Run from `productscape-examples`:

```sh
PRODUCTSCAPES_ALLOW_UNPINNED=1 python3 productscapes.py validate venture-capital-and-private-equity --strict-ids
PRODUCTSCAPES_ALLOW_UNPINNED=1 python3 productscapes.py check-kpis venture-capital-and-private-equity
PRODUCTSCAPES_ALLOW_UNPINNED=1 python3 productscapes.py build venture-capital-and-private-equity
```

Validation, KPI checks, and the documentation build pass. The validator checks
13 JSON files and 23 bricks. A separate read-only
audit checked coverage, exact ownership, product dependency closure, name joins,
KPI definitions and unknown baselines, stream/flow consistency, statistic source
fields, and stressor targets; it found no errors.

The examples project was already pinned to toolkit `a5c2dad`, while the local
toolkit checkout was `5c7c353`. Its documented unpinned override was used without
changing the project pin or checking out another revision. The skill validators
and JSON schemas have no changes between those revisions. The build also includes
the local team-renderer correction described above. Changes in the examples project
are confined to the new domain's source and generated documentation, plus its entry
in the main site index.

Overall: a mature, connected example at the chosen scope, with public evidence
separated from proposed implementation and private operating details.
