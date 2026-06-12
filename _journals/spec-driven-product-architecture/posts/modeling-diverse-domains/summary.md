---
timetoread: 2 min
---

Diverse product-domain examples are part of the method, not demo filler. The repository models many domains — ride sharing, public cloud, premium airlines, audio streaming, freight logistics, and more — because variety is what teaches AI agents which modeling structures are reusable and which product details must stay specific to the domain.

The underlying problem is how agents learn from examples. If every example is the same kind of product, an agent learns a narrow pattern and over-applies it. If every example uses a different structure, there is no stable model to follow. The example set therefore has to show both consistency and variation at once.

**What changes**

- The modeling language stays stable across domains — customer groups, jobs to be done, journeys, KPI pyramids, capabilities, product bricks, data assets, teams, and evidence — so structure transfers from mature domains to new ones without copying their business content.
- The domain story stays different: a ride-sharing marketplace, a public cloud platform, and a long-haul airline must not end up with the same capabilities under different names. The reusable model asks the same questions; each domain answers them differently.
- Domain **archetypes** (marketplaces, platforms, regulated or operational services, enterprise systems, consumer subscription products) guide which existing examples an agent should inspect when modeling something new.
- Mature examples calibrate depth and quality: they show what "good enough" looks like — KPI trees with specific leaves, bricks with modules and dependencies, teams that plausibly own them — instead of a shallow generic skeleton.
- Every representative generated domain page is paired with its GitHub source specification folder, so readers and agents can jump from publication back to the authored model.

**What it costs**

- A living example set drifts: file names, schemas, and generator expectations evolve, so agents must inspect which domains look current and which fields are legacy before editing — copying an old pattern blindly preserves drift.
- Variation resists templating. Keeping domains genuinely different takes deliberate effort; the easy failure mode is standardizing every product story into mush.

**What we are not doing**

- No deep comparison of all existing domains, and no ranking of domains by maturity.
- No external market analysis for individual domains — the examples model structure, not market research.

The Article tab walks the reusable-versus-specific split, the archetypes, the depth calibration, and the full table of example domains with their source folders. [[ai-agents-as-product-architecture-authors]] covers how agents use these examples when authoring; [[evidence-validation-and-publishing]] closes the series on keeping the pattern library trustworthy.
