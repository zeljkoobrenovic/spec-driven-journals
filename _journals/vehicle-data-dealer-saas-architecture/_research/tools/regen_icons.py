"""Regenerate the book's index-card icons as single bold objects legible at 100 x 100 px.

Usage: python3 regen_icons.py [folder ...]      # default: every folder in SUBJECTS

The stock _wiring/generate_icons.py prompt passes title + excerpt, which makes the
model draw a whole chapter (flowcharts, several cars) that turns to noise at card
size. Here each page gets one hand-picked subject. Writes
posts/<folder>/assets/icons/<folder>.png; front matter is not touched.
"""
import concurrent.futures
import os
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / "_wiring"))
import generate_icons as g  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]

STYLE = (
    "A single bold pictogram icon, like a road sign or an app icon glyph, designed to stay legible at 64 x 64 pixels. "
    "Exactly one object and nothing else: no secondary symbol, no badge, no small inset, no arrow unless the subject is an arrow. "
    "The object is centered and fills about 75% of the square canvas. Very thick, uniform black strokes "
    "(about 6% of the canvas width) with rounded ends, large simple geometric shapes, no small details, no fine "
    "lines, no tiny parts, no background scene, no frame or border. Pure black on a plain white background, no "
    "shading, no gradients, no color. No text, letters, digits or labels. No logos, brand badges or real "
    "car-maker shapes; cars are a generic simple side- or front-view silhouette. Subject: "
)

SUBJECTS = {
    "introduction": "an open book",
    "where-vehicle-platforms-go-wrong": "a warning triangle with an exclamation mark",
    "meet-axleby": "a simple office building",
    "part-1-intro": "a compass",
    "part-2-intro": "a fingerprint",
    "part-3-intro": "a speedometer gauge",
    "part-4-intro": "a steering wheel",
    "part-5-intro": "a building divided into three stacked floors",
    "part-6-intro": "a power plug",
    "part-7-intro": "a gear wheel",
    "part-8-intro": "a winding road drawn as one thick S-shaped band with a dashed center line",
    "part-9-intro": "a signpost with two arrows pointing different ways",
    "part-10-intro": "a magnifying glass",
    "01-vehicle-data-ecosystem": "a simple car seen from the side",
    "02-dealer-and-data-economics": "a stack of coins",
    "03-vehicle-capability-map": "a folded map",
    "04-vehicle-bounded-contexts": "three overlapping circles drawn as thick outlines",
    "05-vehicle-identity": "a large barcode made of six thick vertical bars",
    "06-registers-and-official-data": "a classical government building with columns",
    "07-specification-and-equipment": "a wrench crossed with a ruler",
    "08-vehicle-history": "a clock face with a counter-clockwise arrow around it",
    "09-ingestion-and-entity-resolution": "a funnel",
    "10-provenance-and-data-quality": "a rubber stamp",
    "11-market-data": "a bar chart with three bars",
    "12-valuation-engine": "a price tag",
    "13-condition-and-damage": "a large adhesive bandage",
    "14-ev-battery-health": "a battery with a lightning bolt",
    "15-connected-vehicle-data": "a radio antenna emitting three arcs",
    "16-vehicle-acquisition": "two hands shaking",
    "17-inventory-and-vehicle-dossier": "a folder",
    "18-used-car-pricing": "a downward-pointing arrow",
    "19-merchandising": "a camera",
    "20-listing-syndication": "a megaphone",
    "21-leads-and-crm": "an envelope",
    "22-deals-and-sales-documents": "a fountain pen",
    "23-registration-and-trade-services": "a blank rectangular number plate",
    "24-dms-integration": "two puzzle pieces fitting together",
    "25-b2b-trade-and-remarketing": "an auction gavel",
    "26-tenancy-and-dealer-groups": "an apartment block",
    "27-identity-access-and-entitlements": "a padlock",
    "28-onboarding-and-configuration": "a large toggle switch in the on position",
    "29-billing-and-metering": "a receipt",
    "30-data-licensing-and-governance": "a shield",
    "31-vehicle-data-apis": "a pair of curly braces",
    "32-events-webhooks-and-sync": "a bell",
    "33-data-products-and-insights": "a light bulb",
    "34-consumer-vehicle-checks": "a check mark inside a circle",
    "35-reliability-and-dependencies": "a life ring",
    "36-scale-and-cost": "a balance scale",
    "37-observability-and-data-operations": "an eye",
    "38-vehicle-platform-security": "a keyhole",
    "39-privacy-and-retention": "an eraser",
    "40-journey-inventory-to-portal": "a car seen from the front",
    "41-journey-data-correction": "a pencil",
    "42-journey-lead-to-dms": "a paper plane",
    "43-journey-sale-to-registration": "a checkered finish flag on a pole, the checks drawn as six large squares",
    "44-build-buy-or-partner": "a fork in a road",
    "45-one-platform-from-many-products": "a stack of three layers",
    "46-organizing-engineering": "one simple person silhouette",
    "47-modernizing-the-platform": "a hammer",
    "48-ai-in-dealer-workflows": "a friendly robot head seen from the front: a rounded square face with two large round eyes and one short antenna on top",
    "49-evolving-the-vehicle-platform": "a sprouting plant",
    "50-case-cox-automotive": "a globe",
    "51-case-cdk-global": "a computer monitor",
    "52-case-auto-trader-uk": "a smartphone",
    "53-case-vwe": "a windmill",
    "toolkit": "a toolbox",
    "glossary": "a large letter-free speech bubble",
    "bibliography": "a stack of three books",
    "domain-coverage": "a checklist with three check marks",
}


def one(folder: str) -> str:
    out = ROOT / "posts" / folder / "assets" / "icons" / f"{folder}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(3):
        try:
            out.write_bytes(g.call_gemini_image(os.environ["GEMINI_API_KEY"], STYLE + SUBJECTS[folder] + "."))
            return f"ok {folder}"
        except RuntimeError as e:
            err = str(e)[:80]
    return f"FAIL {folder}: {err}"


if __name__ == "__main__":
    folders = sys.argv[1:] or list(SUBJECTS)
    with concurrent.futures.ThreadPoolExecutor(6) as ex:
        for r in ex.map(one, folders):
            print(r, flush=True)
