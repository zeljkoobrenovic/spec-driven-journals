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
    "shading, no gradients, no color. No text, letters, digits or labels. No logos or brand badges. Subject: "
)

SUBJECTS = {
    "introduction": "an open book",
    "meet-veldmark": "a simple office building",
    "where-listing-systems-go-wrong": "a warning triangle with an exclamation mark",
    "part-1-intro": "a shopping basket",
    "part-2-intro": "a blank price tag",
    "part-3-intro": "a cardboard box",
    "part-4-intro": "a magnifying glass",
    "part-5-intro": "a shield",
    "part-6-intro": "a stack of coins",
    "part-7-intro": "a gear wheel",
    "part-8-intro": "a compass",
    "part-9-intro": "a hammer",
    "01-marketplace-taxonomy": "a shop storefront with an awning",
    "02-liquidity-and-network-effects": "a water drop",
    "03-industry-evolution": "a folded newspaper",
    "04-business-capabilities": "a puzzle piece",
    "05-bounded-contexts": "three overlapping circles drawn as thick outlines",
    "06-vertical-requirements": "a house",
    "07-listing-aggregate": "an index card with a folded corner",
    "08-categories-and-taxonomies": "a tree",
    "09-attribute-schemas": "a clipboard",
    "10-media-pipeline": "a camera",
    "11-location-and-geo": "a map pin",
    "12-sellers-and-accounts": "a person silhouette head and shoulders",
    "13-listing-ingestion": "an open door",
    "14-normalization-and-enrichment": "a magic wand",
    "15-entity-resolution": "two overlapping squares",
    "16-publication-pipeline": "a paper plane",
    "17-professional-seller-tooling": "a toolbox",
    "18-search-architecture": "a filing cabinet",
    "19-query-understanding": "a speech bubble with a question mark",
    "20-ranking": "a podium with three steps",
    "21-recommendations": "a thumbs-up hand",
    "22-map-search": "a folded map",
    "23-saved-searches-and-alerts": "a bell",
    "24-trust-and-safety-architecture": "a lighthouse",
    "25-fraud-prevention": "a fishing hook",
    "26-identity-and-verification": "a fingerprint",
    "27-marketplace-regulation": "a balance scale",
    "28-messaging-and-leads": "an envelope",
    "29-transactions-and-payments": "a credit card",
    "30-monetization-models": "a piggy bank",
    "31-products-and-entitlements": "a gift box with a bow",
    "32-advertising-platforms": "a megaphone",
    "33-event-driven-listings": "a lightning bolt",
    "34-listing-data-management": "a database cylinder",
    "35-web-and-seo-architecture": "a globe",
    "36-data-platform": "a bar chart with three bars",
    "37-experimentation": "a laboratory flask",
    "38-ml-platform": "a simple robot head",
    "39-multi-country-platforms": "a flag on a pole",
    "40-reliability-and-scale": "a speedometer gauge",
    "41-platform-consolidation": "two arrows merging into one",
    "42-organizing-marketplace-engineering": "a simple org chart of three linked boxes",
    "43-modernization-and-migration": "an airplane",
    "44-ai-in-listing-systems": "a sparkle star with four points",
    "45-long-term-evolution": "an hourglass",
    "46-case-adevinta": "a stack of building blocks",
    "47-case-olx": "a signpost with two arrows pointing different ways",
    "48-case-ebay-classifieds": "a handshake",
    "49-case-aviv": "a key",
    "50-case-property-portals": "an apartment building",
    "51-case-automotive": "a simple car seen from the side",
    "bibliography": "a stack of three books",
    "glossary": "a bookmark ribbon",
    "toolkit": "a wrench",
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
