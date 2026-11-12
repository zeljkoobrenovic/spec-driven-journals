"""Regenerate the header logos of LISTED as simple cartoon scenes, in the style of ORDERED
(commerce-platform-architecture/_research/tools/visual_layer.py).

Usage: python3 regen_logos.py [--workers N] [folder ...]   # default: every folder in SCENES

The first logos were drawn from title + excerpt and came out as dense infographic boards
with a headline and many labels. Here each page gets one hand-written scene with at most
three short labels. Before a logo is overwritten for the first time, the current file is
kept beside it as logo-infographic.jpeg. Writes posts/<folder>/assets/images/<folder>/logo.jpeg;
front matter is not touched (the logo path stays the same).
"""
import concurrent.futures
import os
import pathlib
import shutil
import sys

REPO = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / "_wiring"))
import generate_logos as g  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]
BACKUP = "logo-infographic.jpeg"

# Hand-written scenes: no real company names, brands, logos or real people.
SCENES = {
    'introduction': "a reader standing at the start of a winding road through a small town of market stalls, each stall with a noticeboard of item cards, where buyers and sellers meet and shake hands; labels 'Supply', 'Demand', 'Match'",
    'where-listing-systems-go-wrong': "a large public noticeboard in a town square where some cards have faded, some are duplicated, one has fallen to the ground, and a puzzled buyer looks at an empty spot; labels 'Stale', 'Duplicate', 'Lost'",
    'meet-veldmark': "a friendly modern headquarters building with four doors side by side, one with a sofa in the window for general classifieds, one with a car, one with a house and one with a laptop for an agent office, all on one shared foundation; label 'One platform'",
    'part-1-intro': "a busy town market square seen from above, with stalls for cars, houses and second-hand goods, buyers walking between them and a noticeboard at the centre; labels 'Buyers', 'Sellers'",
    '01-marketplace-taxonomy': "four doors in a row, each opening a step further into a deal: a noticeboard with a speech bubble, a handshake, a card terminal with a euro sign, and a delivery van at a front door; labels 'Contact', 'Lead', 'Payment'",
    '02-liquidity-and-network-effects': "a lively local market square where buyers and sellers are drawn together like water flowing between two connected pools, with a small water gauge showing the level; labels 'Buyers', 'Sellers', 'Liquidity'",
    '03-industry-evolution': "a road that starts at a newspaper page of small classified ads, passes a desktop computer, then a phone, and ends at a group of connected office buildings; labels 'Print', 'Online', 'Portfolio'",
    '04-business-capabilities': "a city map seen from above where each district is a marketplace capability drawn as a simple building: a listing workshop, a search lighthouse, a trust police station, a message post office and a bank, joined by roads; label 'Capability map'",
    '05-bounded-contexts': "one item card on a table being looked at by several specialists at separate desks with their own glasses and folders, a search clerk, a trust inspector, a billing clerk and an analyst, each seeing it differently; labels 'Search', 'Trust', 'Billing'",
    '06-vertical-requirements': "three different lanes on one shared road: a car on a garage ramp, a house with a for-sale board and a sofa in a living room, each with a different set of inspection tools beside it; labels 'Cars', 'Homes', 'Goods'",
    'part-2-intro': "one large item card pinned at the centre of a workbench, with a category folder, an attribute ruler, a camera, a location pin and a seller's name tag laid around it; label 'The listing'",
    '07-listing-aggregate': "a single item card moving along a short track of stations, draft, live, paused, sold, with a guard holding a rulebook beside it; labels 'Draft', 'Live', 'Sold'",
    '08-categories-and-taxonomies': "a gardener carefully pruning and re-grafting a tidy tree whose branches carry small labelled boxes for vehicles, property and goods, with a few leaves being moved to a new branch; labels 'Vehicles', 'Property', 'Goods'",
    '09-attribute-schemas': "a tidy wall of drawers like a dictionary cabinet, each drawer labelled with a simple icon for colour, size, mileage or rooms, and a clerk checking an item card against a template; labels 'Dictionary', 'Valid'",
    '10-media-pipeline': "a seller's phone sending a photo along a conveyor belt through a cleaning station, a resizing station that makes small, medium and large copies and an inspector with a magnifying glass, ending on many screens; labels 'Upload', 'Resize', 'Serve'",
    '11-location-and-geo': "a map on a table with a precise pin for a house hidden under a small privacy cloud, and a larger soft circle shown to the public around it; labels 'Precise', 'Public'",
    '12-sellers-and-accounts': "three kinds of sellers standing side by side at a counter: a private person with one sofa, a car dealer in front of a small showroom and an estate agent with a folder of houses, each holding a different badge without text; labels 'Private', 'Dealer', 'Agency'",
    'part-3-intro': "goods arriving at a marketplace building through several doors, a person carrying a phone, a truck from a dealer and a paper stack from an agency, and leaving as tidy item cards on a noticeboard; labels 'In', 'Clean', 'Live'",
    '13-listing-ingestion': "a building with three entrances, a small front door for a person with a phone, a service door for a laptop and a loading dock for a truck of boxes, all leading to one inspection desk; labels 'Form', 'API', 'Feed'",
    '14-normalization-and-enrichment': "a workshop where messy handwritten notes enter a machine and come out as neat, uniform item cards, while a worker adds small extra stickers with facts to each card; labels 'Raw', 'Clean', 'Enriched'",
    '15-entity-resolution': "three photos of the same house pinned on a board by three different agents, with a detective joining them by a single string to one house model on the table; labels 'Same house', 'Cluster'",
    '16-publication-pipeline': "a seller pressing a big publish button on a phone, a short checkpoint gate with a guard, and then the item card being copied by messengers to a search shelf, a map and an alert bell; labels 'Publish', 'Check', 'Visible'",
    '17-professional-seller-tooling': "a car dealer at a desk in a showroom, using a large generic screen with simple bar charts and a list of cars, with a stack of enquiry envelopes and a euro coin pile beside them; labels 'Stock', 'Leads', 'Spend'",
    'part-4-intro': "a buyer with a lantern walking into a large hall of shelves of item cards that keep changing, while signposts, a map and a bell point the way; labels 'Search', 'Map', 'Alert'",
    '18-search-architecture': "a librarian quickly updating a large card catalog from a stream of item cards arriving on a conveyor belt, while buyers flip through drawers using filter tabs; labels 'Index', 'Filters', 'Fresh'",
    '19-query-understanding': "a buyer saying a few words into a speech bubble, and a friendly interpreter turning them into a neat set of filter cards, category, price and place, which slot into a search machine; labels 'Words', 'Filters'",
    '20-ranking': "a referee arranging item cards on a podium in order, balancing a relevance scale on one side and a small paid ribbon on the other, while both a buyer and a seller watch; labels 'Relevant', 'Fresh', 'Fair'",
    '21-recommendations': "a friendly shop assistant handing a buyer a few item cards picked from a moving conveyor where some cards are freshly added and others already marked sold; labels 'New', 'For you'",
    '22-map-search': "a buyer drawing a shape with a finger on a large city map spread on a table, with house pins grouped into clusters and a dotted commute line to an office; labels 'Draw', 'Commute'",
    '23-saved-searches-and-alerts': "a buyer sleeping peacefully while a small robot watches a stream of new item cards, catches one that matches a saved search note and rings a bell next to the buyer's phone; labels 'Saved search', 'Alert'",
    'part-5-intro': "a friendly town marketplace protected by a gate with a calm guard, a shield over the noticeboard and a buyer and a seller shaking hands safely; labels 'Trust', 'Safe'",
    '24-trust-and-safety-architecture': "a control room desk where one inspector receives item cards, messages and user profiles on one conveyor, checks them against a rulebook and stamps them with a single decision stamp; labels 'Policy', 'Decision', 'Enforce'",
    '25-fraud-prevention': "a detective with a magnifying glass at a marketplace noticeboard spotting a fake item card with a copied photo and a too-cheap price tag in euros, while a shady figure slips away; labels 'Fake', 'Blocked'",
    '26-identity-and-verification': "a counter with three simple checkpoints: a person showing an ID card, a phone with a padlock, and a business owner showing a registered company folder; labels 'Person', 'Login', 'Business'",
    '27-marketplace-regulation': "a marketplace building with a calm official holding a rulebook and a clipboard, receiving a neat folder of reports from the marketplace staff, with a set of balance scales beside them; labels 'Rules', 'Report'",
    'part-6-intro': "a path from a speech bubble between a buyer and a seller, to a handshake, to a cash register with euro coins at the end; labels 'Contact', 'Deal', 'Revenue'",
    '28-messaging-and-leads': "a buyer and a seller exchanging letters through a post office window where a careful clerk checks each envelope for danger, while a dealer files the letters into a lead folder; labels 'Message', 'Lead'",
    '29-transactions-and-payments': "a buyer paying with a card into a secure safe that holds the euro coins until a parcel arrives by van at the buyer's door, then the safe opens toward the seller; labels 'Pay', 'Ship', 'Protected'",
    '30-monetization-models': "a market stall owner looking at a board of different ways to pay the market, a ticket for a listing, a spotlight for visibility and a small ad poster, each with a euro sign; labels 'Listing', 'Visibility', 'Ads', each used once",
    '31-products-and-entitlements': "a shop counter with a menu board of packages, a menu board of three package boxes showing only euro signs and no amounts, a clerk handing a seller a ticket booklet of bumps and a ledger book on the side ticking off used tickets; labels 'Package', 'Bump', 'Quota'",
    '32-advertising-platforms': "a marketplace page shown as a large shop window where a few tasteful ad posters and one sponsored item card sit beside ordinary item cards, with a privacy curtain at the side; labels 'Display', 'Sponsored'",
    'part-7-intro': "the cross-section of a building where the visible shop floor with noticeboards rests on a sturdy engine room of pipes, conveyor belts and storage tanks underneath; labels 'Surface', 'Platform'",
    '33-event-driven-listings': "one central conveyor belt carrying plain envelopes away from a listing office, with several departments, search, trust, alerts and analytics, each picking copies off the same belt; label 'Event stream'",
    '34-listing-data-management': "one original record locked in a safe in the middle of a room, with several labelled copies on shelves around it, each with a small clock showing how fresh it is; labels 'Original', 'Copy'",
    '35-web-and-seo-architecture': "a big friendly web crawler spider walking along neat signposted streets of web pages with item cards in the windows, while a phone and a laptop show the same pages; labels 'Pages', 'Crawl'",
    '36-data-platform': "a calm lake fed by many small streams of event envelopes, with tidy jars of labelled data products on a shelf by the shore and an analyst taking one; labels 'Events', 'Lake', 'Products'",
    '37-experimentation': "a scientist in a lab coat splitting a small crowd of buyers and sellers into two groups behind two doors labelled A and B, with a balance scale comparing the results; labels 'A', 'B'",
    '38-ml-platform': "a tidy workshop with a single assembly line where model gears are trained, tested, packed and placed into a marketplace machine, with a watchful mechanic monitoring a gauge; labels 'Train', 'Serve', 'Monitor'",
    '39-multi-country-platforms': "one shared building foundation supporting several houses in different colours and roof shapes, each with a small country flag without symbols and its own shop sign without text; labels 'Shared', 'Local'",
    '40-reliability-and-scale': "a marketplace building on a Sunday evening with a big crowd of buyers queuing at the door, while engineers open extra counters and dim lights in optional rooms to keep the main hall running; labels 'Peak', 'Steady'",
    'part-8-intro': "an architect standing on a balcony looking over a small group of connected marketplace buildings, holding a rolled plan and a compass; labels 'Agenda', 'Group'",
    '41-platform-consolidation': "several small, differently built houses being joined onto one shared foundation, starting with the underground pipes and wires while the shop fronts stay as they are; labels 'Merge', 'Foundation'",
    '42-organizing-marketplace-engineering': "a large org board on a wall where each team card is connected by one string to exactly one building block of the marketplace, with a few teams standing in front of their blocks; labels 'Team', 'Owner'",
    '43-modernization-and-migration': "mechanics replacing a jet engine on a plane while it keeps flying above the clouds, with passengers calmly reading item cards in the cabin windows; labels 'Old', 'New'",
    '44-ai-in-listing-systems': "a friendly robot assistant helping a seller write a neat item card from a messy photo and a few spoken words, while a guard with a rulebook watches beside it; labels 'Assist', 'Guard'",
    '45-long-term-evolution': "a marketplace building being renovated room by room over several seasons, with spring, summer, autumn and winter trees outside, and an architect swapping one module for another; labels 'Replace', 'Evolve'",
    'part-9-intro': "a reader in a library looking at six open case folders on a long table, each with a simple drawing of a building, a car or a house on its cover; labels 'Cases', 'Lessons'",
    '46-case-adevinta': "a pendulum swinging between many separate small market stalls on one side and one big shared market hall on the other, with an architect watching it; labels 'Separate', 'Shared'",
    '47-case-olx': "a map of the world with many market flags being pulled in until only a few strong local markets remain, while a car is being carried out of one of them; labels 'Many', 'Few'",
    '48-case-ebay-classifieds': "a large parent ship towing a fleet of small local boats, each with its own sail, and one boat later sailing away on its own; labels 'Parent', 'Local'",
    '49-case-aviv': "several national house-shaped buildings being moved onto one shared European foundation, with a shared valuation scale in the middle; labels 'Homes', 'Shared'",
    '50-case-property-portals': "an estate agent and a valuer side by side looking at a house, one holding an estimate card and the other holding a stack of euro coins kept behind a rope; labels 'Estimate', 'Commit'",
    '51-case-automotive': "a car on a garage ramp scanned by a mechanic whose tablet fills in the car's details automatically, while a dealer at the side holds a price tag in euros; labels 'Car', 'Dealer', 'Price'",
    'toolkit': "an open toolbox on a workbench with neat templates, a ruler, a map, a checklist and a decision notebook inside; label 'Field kit'",
    'glossary': "an open dictionary on a desk with small item card bookmarks sticking out and a magnifying glass resting on a page; label 'Glossary'",
    'bibliography': "a tidy bookshelf with books, reports and papers, and a reader pulling one out with an index card tied to it by a string; label 'Sources'",
}

SUFFIX = (
    " Brand rules: draw no logos, brand marks or badges, and write no company, product, cloud or software names anywhere. Show software as generic unbranded screens, databases as plain cylinders, servers "
    "as plain boxes. People are generic professionals, never real people. Money, if shown, is in euros: use the euro "
    "sign on every coin, bill, bag and price, never a dollar sign. Keep any text to a few short generic words, correctly spelled; any headline is at most six short words. "
    "These drawing instructions are not content: never print style or layout words such as 'business explainer "
    "board', 'infographic board', 'flat vector', 'lightweight UI fragment', 'dashboard fragment', 'abstract shape' "
    "or 'style' anywhere in the image. "
    "Make it a header illustration, not an infographic: one clear scene or metaphor, mostly pictures. Use no numbers, "
    "digits, dates, percentages or months anywhere, no tables, no lists, no square-bracket text, and at most five "
    "short labels of one to three words each."
)


def prompt(folder, corrections=""):
    p = (
        "Create a wide 16:9 header illustration for a chapter of a book on listing marketplace architecture: "
        + SCENES[folder]
        + ". Draw it as a clean flat cartoon scene with crisp outlines and minimal shading, light background, "
        "disciplined blue, teal, green and orange accents, generous margins. No title, headline, banner or caption anywhere, "
        "especially not at the top and never the words listing marketplace architecture; the only words in the image are the "
        "quoted labels, each written once and without quotation marks." + SUFFIX
    )
    return p + (f" Corrections: {corrections}" if corrections else "")


def logo(folder, corrections=""):
    out = ROOT / "posts" / folder / "assets" / "images" / folder / "logo.jpeg"
    out.parent.mkdir(parents=True, exist_ok=True)
    backup = out.with_name(BACKUP)
    if out.exists() and not backup.exists():
        shutil.copy2(out, backup)
    err = ""
    for _ in range(3):
        try:
            out.write_bytes(g.call_gemini_image(os.environ["GEMINI_API_KEY"], prompt(folder, corrections)))
            return f"ok {folder}"
        except Exception as e:  # noqa: BLE001
            err = str(e)[:100]
    return f"FAIL {folder}: {err}"


def main(argv):
    workers = 6
    if argv[:1] == ["--workers"]:
        workers, argv = int(argv[1]), argv[2:]
    folders = argv or list(SCENES)
    unknown = [f for f in folders if f not in SCENES]
    if unknown:
        sys.exit(f"unknown folders: {unknown}")
    with concurrent.futures.ThreadPoolExecutor(workers) as ex:
        for line in ex.map(logo, folders):
            print(line, flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
