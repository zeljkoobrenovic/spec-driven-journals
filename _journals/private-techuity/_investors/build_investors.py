#!/usr/bin/env python3
"""Build investors.json: curated investor metadata + verified links + downloaded logos.

Standard library only. Run from anywhere:
    python3 _journals/private-techuity/_investors/build_investors.py              # fetch + json + html
    python3 _journals/private-techuity/_investors/build_investors.py --html-only  # re-render html from json

Seed data lives in SEED below. Figures marked *_approx are rounded public
figures from firm reports/press (as_of year given) — verify before citing.
"""
import html.parser
import json
import re
import ssl
import sys
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
JOURNAL = HERE.parent
LOGOS = HERE / "logos"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"

# type: buyout | growth | venture | corporate-venture | multi-strategy | sovereign-wealth
SEED = [
    # --- Private equity / buyout (tech-focused or large tech practice) ---
    dict(id="hg", name="Hg", type="buyout", hq="London, UK", founded=2000,
         aum_approx="~$70bn", aum_as_of=2024, stages=["buyout", "growth"],
         focus="European and transatlantic software and tech-enabled services; majority and minority stakes.",
         notable_examples=["Visma", "TeamSystem", "IRIS Software", "Access Group", "IFS"],
         website="https://hgcapital.com", portfolio="https://hgcapital.com/portfolio",
         aliases=["Hg", "HgCapital", "Hg Capital"]),
    dict(id="kkr", name="KKR", type="multi-strategy", hq="New York, USA", founded=1976,
         aum_approx="~$640bn", aum_as_of=2025, stages=["buyout", "growth", "infrastructure", "credit"],
         focus="Global multi-asset investor; large technology buyout and tech growth practice.",
         notable_examples=["Visma (historic)", "Toys \"R\" Us (historic, with Bain & Vornado)", "BMC Software", "Kokusai Electric"],
         website="https://www.kkr.com", portfolio="https://www.kkr.com/invest/portfolio",
         aliases=["KKR", "Kohlberg Kravis Roberts"]),
    dict(id="blackstone", name="Blackstone", type="multi-strategy", hq="New York, USA", founded=1985,
         aum_approx="~$1.2tn", aum_as_of=2025, stages=["buyout", "growth", "real estate", "credit"],
         focus="World's largest alternative asset manager; corporate PE, growth equity and real estate.",
         notable_examples=["Hilton (historic)", "Cvent", "Bumble", "Refinitiv (historic)"],
         website="https://www.blackstone.com", portfolio="https://www.blackstone.com/our-businesses/private-equity/",
         aliases=["Blackstone"]),
    dict(id="hellman-friedman", name="Hellman & Friedman", type="buyout", hq="San Francisco, USA", founded=1984,
         aum_approx="~$100bn+", aum_as_of=2024, stages=["buyout"],
         focus="Large-cap buyouts in software, financial services, healthcare and consumer.",
         notable_examples=["TeamSystem (majority owner since 2016)", "Genesys", "Checkmarx"],
         website="https://hf.com", portfolio="https://hf.com/portfolio/",
         aliases=["Hellman & Friedman", "H&F"]),
    dict(id="silver-lake", name="Silver Lake", type="buyout", hq="Menlo Park, USA", founded=1999,
         aum_approx="~$100bn", aum_as_of=2024, stages=["buyout", "growth"],
         focus="Technology-focused large-scale investing.",
         notable_examples=["Skype (historic)", "TeamSystem (minority, €600m)", "Dell", "Endeavor", "Qualtrics"],
         website="https://www.silverlake.com", portfolio="https://www.silverlake.com/portfolio/",
         aliases=["Silver Lake"]),
    dict(id="bain-capital", name="Bain Capital", type="multi-strategy", hq="Boston, USA", founded=1984,
         aum_approx="~$185bn", aum_as_of=2024, stages=["buyout", "growth", "venture", "credit"],
         focus="Multi-asset investor with dedicated tech buyout and venture (Bain Capital Ventures) arms.",
         notable_examples=["Toys \"R\" Us (historic)", "Kioxia", "Zellis", "Rocket Software"],
         website="https://www.baincapital.com", portfolio=None,
         aliases=["Bain Capital"]),
    dict(id="cinven", name="Cinven", type="buyout", hq="London, UK", founded=1977,
         aum_approx="~€40bn", aum_as_of=2024, stages=["buyout"],
         focus="European buyouts across TMT, business services, healthcare and financial services.",
         notable_examples=["Visma (partial exit 2017)", "idealista", "Synlab (historic)"],
         website="https://www.cinven.com", portfolio="https://www.cinven.com/portfolio/",
         aliases=["Cinven"]),
    dict(id="cvc", name="CVC Capital Partners", type="multi-strategy", hq="Luxembourg / London", founded=1981,
         aum_approx="~€200bn", aum_as_of=2024, stages=["buyout", "growth", "credit", "secondaries"],
         focus="European and Asian buyouts; separate growth (tech) strategy.",
         notable_examples=["Formula One (historic)", "Petco", "Ethniki", "Unilever Tea (ekaterra)"],
         website="https://www.cvc.com", portfolio="https://www.cvc.com/portfolio/our-portfolio/",
         aliases=["CVC Capital Partners"]),
    dict(id="tpg", name="TPG", type="multi-strategy", hq="Fort Worth / San Francisco, USA", founded=1992,
         aum_approx="~$240bn", aum_as_of=2025, stages=["buyout", "growth", "impact", "credit"],
         focus="Global PE with TPG Capital, TPG Growth and TPG Rise; major tech practice.",
         notable_examples=["Visma (co-investor)", "McAfee (historic)", "Nextracker (TPG Rise, historic)", "Wind River (historic)"],
         website="https://www.tpg.com", portfolio="https://www.tpg.com/portfolio",
         aliases=["TPG"]),
    dict(id="vista", name="Vista Equity Partners", type="buyout", hq="Austin, USA", founded=2000,
         aum_approx="~$100bn", aum_as_of=2024, stages=["buyout", "growth", "credit"],
         focus="Enterprise software exclusively; known for a codified operating playbook.",
         notable_examples=["Datto (historic)", "Cvent (historic)", "Ping Identity (historic)", "Duck Creek"],
         website="https://www.vistaequitypartners.com", portfolio="https://www.vistaequitypartners.com/companies/",
         aliases=["Vista Equity", "Vista Equity Partners"]),
    dict(id="thoma-bravo", name="Thoma Bravo", type="buyout", hq="Chicago / San Francisco, USA", founded=2008,
         aum_approx="~$180bn", aum_as_of=2025, stages=["buyout", "growth", "credit"],
         focus="Software and technology buyouts; the largest software-focused PE firm.",
         notable_examples=["SailPoint", "Proofpoint", "Darktrace", "Instructure (historic)"],
         website="https://www.thomabravo.com", portfolio="https://www.thomabravo.com/companies",
         aliases=["Thoma Bravo"]),
    dict(id="eqt", name="EQT", type="multi-strategy", hq="Stockholm, Sweden", founded=1994,
         aum_approx="~€270bn", aum_as_of=2025, stages=["buyout", "growth", "venture", "infrastructure"],
         focus="Nordic-rooted global investor with thematic, digitisation-led ownership model.",
         notable_examples=["IFS (with Hg)", "SUSE", "Acronis"],
         website="https://eqtgroup.com", portfolio="https://eqtgroup.com/current-portfolio/",
         aliases=["EQT"]),
    dict(id="permira", name="Permira", type="buyout", hq="London, UK", founded=1985,
         aum_approx="~€80bn", aum_as_of=2024, stages=["buyout", "growth", "credit"],
         focus="European and US buyouts and growth equity; strong technology sector.",
         notable_examples=["Squarespace", "Genesys", "Mimecast", "Informatica (historic)"],
         website="https://www.permira.com", portfolio="https://www.permira.com/portfolio",
         aliases=["Permira"]),
    dict(id="advent", name="Advent International", type="buyout", hq="Boston, USA", founded=1984,
         aum_approx="~$90bn", aum_as_of=2024, stages=["buyout", "growth"],
         focus="Global buyouts across business services, healthcare, industrials, retail and technology.",
         notable_examples=["Maxar", "Nexi", "Definitive Healthcare", "Zentiva"],
         website="https://www.adventinternational.com", portfolio="https://www.adventinternational.com/portfolio/",
         aliases=["Advent International"]),
    dict(id="warburg-pincus", name="Warburg Pincus", type="growth", hq="New York, USA", founded=1966,
         aum_approx="~$85bn", aum_as_of=2024, stages=["growth", "buyout"],
         focus="Growth-oriented global PE across technology, financial services, healthcare.",
         notable_examples=["Ant Group", "Bharti Airtel (historic)"],
         website="https://warburgpincus.com", portfolio="https://warburgpincus.com/investments/",
         aliases=["Warburg Pincus"]),
    dict(id="francisco-partners", name="Francisco Partners", type="buyout", hq="San Francisco, USA", founded=1999,
         aum_approx="~$45bn", aum_as_of=2024, stages=["buyout", "growth", "credit"],
         focus="Technology and tech-enabled businesses, including carve-outs.",
         notable_examples=["Jamf", "Forcepoint", "The Weather Company", "New Relic"],
         website="https://www.franciscopartners.com", portfolio="https://www.franciscopartners.com/investments",
         aliases=["Francisco Partners"]),
    dict(id="carlyle", name="The Carlyle Group", type="multi-strategy", hq="Washington, D.C., USA", founded=1987,
         aum_approx="~$440bn", aum_as_of=2025, stages=["buyout", "growth", "credit", "infrastructure"],
         focus="Global multi-asset manager with corporate PE, including technology.",
         notable_examples=["ManTech", "Veritas (historic)", "Beautycounter (historic)"],
         website="https://www.carlyle.com", portfolio="https://www.carlyle.com/portfolio",
         aliases=["Carlyle"]),
    dict(id="apax", name="Apax Partners", type="buyout", hq="London, UK", founded=1969,
         aum_approx="~$75bn", aum_as_of=2024, stages=["buyout", "growth", "digital"],
         focus="Tech, services, healthcare and internet/consumer; dedicated Apax Digital growth fund.",
         notable_examples=["Trade Me", "ThoughtWorks (historic)", "idealista (historic)", "Paycor (historic)"],
         website="https://www.apax.com", portfolio="https://www.apax.com/all-investments-listed-alphabetically/",
         aliases=["Apax"]),
    dict(id="nordic-capital", name="Nordic Capital", type="buyout", hq="Stockholm, Sweden", founded=1989,
         aum_approx="~€30bn", aum_as_of=2024, stages=["buyout"],
         focus="Healthcare, technology & payments, financial services in Europe and North America.",
         notable_examples=["Trustly", "Macrobond", "Signicat"],
         website="https://www.nordiccapital.com", portfolio="https://www.nordiccapital.com/portfolio/",
         aliases=["Nordic Capital"]),
    dict(id="bridgepoint", name="Bridgepoint", type="buyout", hq="London, UK", founded=2000,
         aum_approx="~€65bn", aum_as_of=2024, stages=["buyout", "growth", "credit"],
         focus="European mid-market buyouts and growth; publicly listed manager.",
         notable_examples=["Kyriba (historic)", "Calyx", "PEI Media", "Qualitest"],
         website="https://www.bridgepointgroup.com", portfolio="https://www.bridgepointgroup.com/our-portfolio",
         aliases=["Bridgepoint"]),
    dict(id="apollo", name="Apollo Global Management", type="multi-strategy", hq="New York, USA", founded=1990,
         aum_approx="~$800bn", aum_as_of=2025, stages=["buyout", "credit", "hybrid"],
         focus="Credit-heavy alternative manager; large-cap and distressed PE.",
         notable_examples=["Yahoo", "ADT", "Tenneco"],
         website="https://www.apollo.com", portfolio="https://www.apollo.com/strategies/asset-management/equity/private-equity",
         aliases=["Apollo Global", "Apollo Global Management"]),
    dict(id="icg", name="ICG (Intermediate Capital Group)", type="multi-strategy", hq="London, UK", founded=1989,
         aum_approx="~$100bn", aum_as_of=2024, stages=["buyout", "credit", "infrastructure", "secondaries"],
         focus="Listed alternative manager spanning structured and private equity, private debt and real assets.",
         notable_examples=["Visma (co-investor)"],
         website="https://www.icgam.com", portfolio=None,
         aliases=["ICG"]),
    dict(id="montagu", name="Montagu Private Equity", type="buyout", hq="London, UK", founded=1968,
         aum_approx="~€15bn", aum_as_of=2024, stages=["buyout"],
         focus="European mid-market buyouts in software, healthcare data and business-critical services.",
         notable_examples=["Visma (co-investor)"],
         website="https://www.montagu.com", portfolio="https://www.montagu.com/portfolio",
         aliases=["Montagu"]),
    dict(id="gic", name="GIC", type="sovereign-wealth", hq="Singapore", founded=1981,
         aum_approx="undisclosed (estimated >$700bn)", aum_as_of=None, stages=["direct PE", "fund LP", "growth"],
         focus="Singapore's sovereign wealth fund; invests as LP in PE funds and directly alongside sponsors.",
         notable_examples=["Visma (co-investor)"],
         website="https://www.gic.com.sg", portfolio=None,
         aliases=["GIC"]),
    # --- Growth equity ---
    dict(id="insight-partners", name="Insight Partners", type="growth", hq="New York, USA", founded=1995,
         aum_approx="~$90bn", aum_as_of=2024, stages=["venture", "growth", "buyout"],
         focus="Software ScaleUp investing from early growth to buyout; Insight Onsite operator team.",
         notable_examples=["Wiz", "Monday.com", "Veeam", "Checkmarx (historic)"],
         website="https://www.insightpartners.com", portfolio="https://www.insightpartners.com/portfolio/",
         aliases=["Insight Partners"]),
    dict(id="general-atlantic", name="General Atlantic", type="growth", hq="New York, USA", founded=1980,
         aum_approx="~$100bn", aum_as_of=2025, stages=["growth"],
         focus="Global growth equity in technology, financial services, healthcare, consumer.",
         notable_examples=["Airbnb (historic)", "ByteDance", "Squarespace (historic)", "Doctolib"],
         website="https://www.generalatlantic.com", portfolio="https://www.generalatlantic.com/portfolio/",
         aliases=["General Atlantic"]),
    dict(id="summit-partners", name="Summit Partners", type="growth", hq="Boston, USA", founded=1984,
         aum_approx="~$45bn", aum_as_of=2024, stages=["growth", "credit"],
         focus="Growth equity for profitable, founder-led companies in tech, healthcare and services.",
         notable_examples=["Avast (historic)", "Ubiquiti (historic)"],
         website="https://www.summitpartners.com", portfolio="https://www.summitpartners.com/companies",
         aliases=["Summit Partners"]),
    dict(id="ta-associates", name="TA Associates", type="growth", hq="Boston, USA", founded=1968,
         aum_approx="~$65bn", aum_as_of=2024, stages=["growth", "buyout"],
         focus="Growth-oriented PE in technology, healthcare, financial and business services.",
         notable_examples=["Aptean", "Idera", "Netsmart"],
         website="https://www.ta.com", portfolio="https://www.ta.com/portfolio/",
         aliases=["TA Associates"]),
    dict(id="tiger-global", name="Tiger Global Management", type="growth", hq="New York, USA", founded=2001,
         aum_approx="~$50bn", aum_as_of=2024, stages=["venture", "growth", "public equity"],
         focus="Crossover investor; fast, high-volume growth rounds in the 2020–2021 cycle.",
         notable_examples=["Checkout.com", "Flipkart (historic)", "Facebook (historic)"],
         website="https://www.tigerglobal.com", portfolio=None,
         aliases=["Tiger Global"]),
    dict(id="softbank-vision-fund", name="SoftBank Vision Fund", type="growth", hq="Tokyo / London", founded=2017,
         aum_approx="~$100bn fund I + ~$56bn fund II (committed)", aum_as_of=2023, stages=["growth", "late venture"],
         focus="Mega-round late-stage tech investing, backed by SoftBank Group.",
         notable_examples=["ByteDance", "Coupang", "DoorDash (historic)", "WeWork (historic)"],
         website="https://visionfund.com", portfolio="https://visionfund.com/portfolio",
         aliases=["SoftBank", "Vision Fund"]),
    # --- Venture capital ---
    dict(id="a16z", name="Andreessen Horowitz (a16z)", type="venture", hq="Menlo Park, USA", founded=2009,
         aum_approx="~$45bn", aum_as_of=2024, stages=["seed", "venture", "growth"],
         focus="Stage-agnostic venture with a large in-house platform team; software, bio, crypto, AI.",
         notable_examples=["Skype (early investor)", "GitHub (historic)", "Databricks", "Coinbase"],
         website="https://a16z.com", portfolio="https://a16z.com/portfolio/",
         aliases=["Andreessen Horowitz", "a16z"]),
    dict(id="sequoia", name="Sequoia Capital", type="venture", hq="Menlo Park, USA", founded=1972,
         aum_approx="n/a (evergreen fund structure)", aum_as_of=None, stages=["seed", "venture", "growth"],
         focus="Seed-to-growth venture; US/Europe (HongShan and Peak XV spun out in 2023–24).",
         notable_examples=["Apple (historic)", "Google (historic)", "Stripe", "Klarna"],
         website="https://www.sequoiacap.com", portfolio="https://www.sequoiacap.com/our-companies/",
         aliases=["Sequoia"]),
    dict(id="accel", name="Accel", type="venture", hq="Palo Alto, USA / London, UK", founded=1983,
         aum_approx="n/a", aum_as_of=None, stages=["seed", "venture", "growth"],
         focus="Early and growth venture in the US, Europe and India.",
         notable_examples=["Facebook (historic)", "Slack (historic)", "Spotify", "Atlassian"],
         website="https://www.accel.com", portfolio="https://www.accel.com/relationships",
         aliases=["Accel"]),
    dict(id="index-ventures", name="Index Ventures", type="venture", hq="London, UK / San Francisco, USA", founded=1996,
         aum_approx="n/a", aum_as_of=None, stages=["seed", "venture", "growth"],
         focus="Transatlantic venture; publishes widely used option-plan guidance (OptionPlan).",
         notable_examples=["Skype (early investor)", "Revolut", "Figma", "Adyen"],
         website="https://www.indexventures.com", portfolio="https://www.indexventures.com/companies/",
         aliases=["Index Ventures"]),
    dict(id="balderton", name="Balderton Capital", type="venture", hq="London, UK", founded=2000,
         aum_approx="~$4bn+", aum_as_of=2024, stages=["seed", "series A", "growth"],
         focus="European early-stage and growth venture; publishes employee-equity guidance.",
         notable_examples=["Revolut", "Wayve", "GoCardless"],
         website="https://www.balderton.com", portfolio="https://www.balderton.com/companies/",
         aliases=["Balderton"]),
    dict(id="atomico", name="Atomico", type="venture", hq="London, UK", founded=2006,
         aum_approx="~$5bn+", aum_as_of=2024, stages=["series A", "growth"],
         focus="European tech venture founded by Skype co-founder Niklas Zennström; State of European Tech report.",
         notable_examples=["Klarna", "Lilium", "Graphcore", "Supercell (historic)"],
         website="https://atomico.com", portfolio="https://atomico.com/portfolio",
         aliases=["Atomico"]),
    dict(id="lightspeed", name="Lightspeed Venture Partners", type="venture", hq="Menlo Park, USA", founded=2000,
         aum_approx="~$25bn+", aum_as_of=2024, stages=["seed", "venture", "growth"],
         focus="Multi-stage venture in enterprise, consumer, fintech and AI.",
         notable_examples=["Snap", "Mistral AI", "Rubrik", "Nutanix"],
         website="https://lsvp.com", portfolio="https://lsvp.com/portfolio/",
         aliases=["Lightspeed Venture"]),
    dict(id="benchmark", name="Benchmark", type="venture", hq="San Francisco, USA", founded=1995,
         aum_approx="n/a (small fixed-size funds)", aum_as_of=None, stages=["series A"],
         focus="Equal-partnership early-stage venture with deliberately small funds.",
         notable_examples=["eBay (historic)", "Uber (historic)", "Twitter (historic)", "Snap"],
         website="https://www.benchmark.com", portfolio=None,
         aliases=["Benchmark Capital"]),
    dict(id="kleiner-perkins", name="Kleiner Perkins", type="venture", hq="Menlo Park, USA", founded=1972,
         aum_approx="n/a", aum_as_of=None, stages=["seed", "venture", "growth"],
         focus="Early venture and KP Select growth funds.",
         notable_examples=["Google (historic)", "Amazon (historic)", "Figma", "Rippling"],
         website="https://www.kleinerperkins.com", portfolio="https://www.kleinerperkins.com/partnerships/",
         aliases=["Kleiner Perkins"]),
    dict(id="greylock", name="Greylock", type="venture", hq="Menlo Park, USA", founded=1965,
         aum_approx="n/a", aum_as_of=None, stages=["seed", "series A"],
         focus="Early-stage enterprise and consumer software; Blitzscaling authors.",
         notable_examples=["LinkedIn (historic)", "Airbnb (historic)", "Palo Alto Networks (historic)", "Figma"],
         website="https://greylock.com", portfolio="https://greylock.com/portfolio/",
         aliases=["Greylock"]),
    dict(id="northzone", name="Northzone", type="venture", hq="Stockholm / London", founded=1996,
         aum_approx="~€3bn+", aum_as_of=2024, stages=["seed", "series A", "growth"],
         focus="European early-stage venture.",
         notable_examples=["Spotify (early investor)", "Klarna", "Trustpilot", "Personio"],
         website="https://northzone.com", portfolio="https://northzone.com/portfolio",
         aliases=["Northzone"]),
    dict(id="creandum", name="Creandum", type="venture", hq="Stockholm, Sweden", founded=2003,
         aum_approx="~€1.5bn+", aum_as_of=2024, stages=["seed", "series A"],
         focus="European seed and early-stage venture.",
         notable_examples=["Spotify (first investor)", "Klarna", "Kahoot!", "Pleo"],
         website="https://creandum.com", portfolio="https://creandum.com/commitments/",
         aliases=["Creandum"]),
    dict(id="battery-ventures", name="Battery Ventures", type="venture", hq="Boston, USA", founded=1983,
         aum_approx="~$13bn+", aum_as_of=2024, stages=["venture", "growth", "buyout"],
         focus="Technology investing across venture, growth and buyouts; publishes the OpenCloud report.",
         notable_examples=["Coupa (historic)"],
         website="https://www.battery.com", portfolio="https://www.battery.com/list-of-all-companies/",
         aliases=["Battery Ventures"]),
    # --- Corporate venture ---
    dict(id="gv", name="GV (Google Ventures)", type="corporate-venture", hq="Mountain View, USA", founded=2009,
         aum_approx="~$10bn", aum_as_of=2024, stages=["seed", "venture", "growth"],
         focus="Alphabet's venture arm; life sciences and technology.",
         notable_examples=["Uber (historic)", "Slack (historic)", "GitLab", "Stripe"],
         website="https://www.gv.com", portfolio="https://www.gv.com/portfolio/",
         aliases=["GV", "Google Ventures"]),
    dict(id="intel-capital", name="Intel Capital", type="corporate-venture", hq="Santa Clara, USA", founded=1991,
         aum_approx="n/a", aum_as_of=None, stages=["seed", "venture", "growth"],
         focus="Intel's venture arm; silicon, cloud infrastructure, devices, AI.",
         notable_examples=["VMware (historic)", "Cloudera (historic)", "SambaNova", "Anyscale"],
         website="https://www.intelcapital.com", portfolio="https://www.intelcapital.com/portfolio/",
         aliases=["Intel Capital"]),
    dict(id="salesforce-ventures", name="Salesforce Ventures", type="corporate-venture", hq="San Francisco, USA", founded=2009,
         aum_approx="n/a", aum_as_of=None, stages=["venture", "growth"],
         focus="Salesforce's investment arm; enterprise software and AI, often with a strategic partnership.",
         notable_examples=["Anthropic", "Snowflake (historic)", "Zoom (historic)", "Hugging Face"],
         website="https://salesforceventures.com", portfolio="https://salesforceventures.com/portfolio/",
         aliases=["Salesforce Ventures"]),
    dict(id="m12", name="M12 (Microsoft)", type="corporate-venture", hq="Redmond, USA", founded=2016,
         aum_approx="n/a", aum_as_of=None, stages=["series A", "series B"],
         focus="Microsoft's venture fund; enterprise software, AI, security.",
         notable_examples=["Icertis", "Innovaccer"],
         website="https://m12.vc", portfolio="https://m12.vc/portfolio/",
         aliases=["M12"]),
]


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return r.status, r.geturl(), r.headers.get("Content-Type", ""), r.read()


def check(url):
    if not url:
        return None
    try:
        status, final, _, _ = fetch(url)
        return {"status": status, "final_url": final}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "final_url": url}
    except Exception as e:  # noqa: BLE001
        return {"status": None, "error": type(e).__name__}


class LogoFinder(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.cands = []  # (score, url)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "link" and a.get("href"):
            rel = (a.get("rel") or "").lower()
            href = a["href"]
            if "apple-touch-icon" in rel:
                self.cands.append((60, href))
            elif "icon" in rel:
                self.cands.append((70 if href.lower().split("?")[0].endswith(".svg") else 30, href))
        elif tag == "img":
            src = a.get("src") or a.get("data-src") or ""
            blob = " ".join([src, a.get("alt", ""), a.get("class", ""), a.get("id", "")]).lower()
            if src and "logo" in blob and not src.startswith("data:"):
                self.cands.append((90 if src.lower().split("?")[0].endswith(".svg") else 80, src))
        elif tag == "meta" and (a.get("property") == "og:image" or a.get("name") == "og:image") and a.get("content"):
            self.cands.append((20, a["content"]))


EXT = {"image/svg+xml": ".svg", "image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp",
       "image/x-icon": ".ico", "image/vnd.microsoft.icon": ".ico", "image/gif": ".gif"}


# Homepages whose "logo" <img> is actually a portfolio company's, or unusable: use the favicon service.
FAVICON_ONLY = {"thoma-bravo", "insight-partners", "softbank-vision-fund", "index-ventures", "kleiner-perkins", "icg"}
# White/light logos that need a dark background to be visible.
DARK_BG = {"silver-lake", "eqt", "permira", "apollo", "balderton", "battery-ventures", "summit-partners"}


def save_logo(inv):
    """Try the site's own logo first (header <img>, svg icon, touch icon), then Google's favicon service."""
    tried = []
    try:
        if inv["id"] in FAVICON_ONLY:
            raise LookupError
        _, base, _, body = fetch(inv["website"])
        finder = LogoFinder()
        finder.feed(body.decode("utf-8", "replace"))
        for _, href in sorted(finder.cands, key=lambda c: -c[0]):
            tried.append(urllib.parse.urljoin(base, href))
    except Exception:  # noqa: BLE001
        pass
    domain = urllib.parse.urlparse(inv["website"]).netloc
    tried.append(f"https://www.google.com/s2/favicons?domain={domain}&sz=256")
    for url in tried:
        try:
            _, _, ctype, data = fetch(url)
        except Exception:  # noqa: BLE001
            continue
        ctype = ctype.split(";")[0].strip().lower()
        if ctype not in EXT or len(data) < 200:
            continue
        path = LOGOS / f"{inv['id']}{EXT[ctype]}"
        for old in LOGOS.glob(f"{inv['id']}.*"):
            old.unlink()
        path.write_bytes(data)
        kind = "favicon-service" if "google.com/s2" in url else "site"
        return {"file": f"logos/{path.name}", "source_url": url, "source": kind,
                "background": "dark" if inv["id"] in DARK_BG else "light"}
    return None


def book_mentions(inv):
    hits = []
    for md in sorted((JOURNAL / "posts").glob("*/index.md")):
        text = md.read_text(encoding="utf-8")
        m = re.search(r"^permalink:\s*(\S+)", text, re.M)
        if any(re.search(rf"(?<![\w-]){re.escape(a)}(?![\w-])", text) for a in inv["aliases"]):
            hits.append(m.group(1) if m else md.parent.name)
    return hits


def enrich(inv):
    out = dict(inv)
    aliases = out.pop("aliases")
    out["links"] = {"website": inv["website"], "portfolio": inv["portfolio"]}
    out.pop("website"); out.pop("portfolio")
    out["link_check"] = {k: check(v) for k, v in out["links"].items()}
    out["logo"] = save_logo(inv)
    out["mentioned_in_posts"] = book_mentions(inv)
    out["aliases"] = aliases
    return out


EUR_USD = 1.10  # rough conversion for comparing euro-reported AUM


def aum_usd_bn(text):
    """'~$70bn' -> 70, '~€40bn' -> 44, '~$1.2tn' -> 1200; sums multiple figures; None when not numeric."""
    total = 0.0
    for cur, num, unit in re.findall(r"([$€])\s*([\d.]+)\s*(bn|tn)", text or ""):
        v = float(num) * (1000 if unit == "tn" else 1) * (EUR_USD if cur == "€" else 1)
        total += v
    return round(total) or None


# Bare city names used in hq strings like "Stockholm / London".
CITY_COUNTRY = {"London": "UK", "Stockholm": "Sweden", "Tokyo": "Japan", "Luxembourg": "Luxembourg",
                "Singapore": "Singapore", "Chicago": "USA", "Fort Worth": "USA"}


def hq_countries(hq):
    """'Palo Alto, USA / London, UK' -> ['USA', 'UK']; first entry is the primary HQ."""
    out = []
    for part in (hq or "").split(" / "):
        part = part.strip()
        country = part.rsplit(", ", 1)[-1] if ", " in part else CITY_COUNTRY.get(part)
        if country and country not in out:
            out.append(country)
    return out


def add_numeric(doc):
    for inv in doc["investors"]:
        inv["aum_usd_bn"] = aum_usd_bn(inv.get("aum_approx"))
        inv["countries"] = hq_countries(inv.get("hq"))
    doc["aum_usd_bn_note"] = f"aum_usd_bn: aum_approx converted to USD billions (EUR at {EUR_USD}); null when not disclosed."
    return doc


def render_html(doc):
    """Embed the JSON into investors.template.html -> investors.html (logos referenced relatively)."""
    tpl = (HERE / "investors.template.html").read_text(encoding="utf-8")
    payload = json.dumps(doc, ensure_ascii=False).replace("</", "<\\/")
    (HERE / "investors.html").write_text(tpl.replace("__DATA_JSON__", payload), encoding="utf-8")


def main():
    if "--html-only" in sys.argv:
        doc = add_numeric(json.loads((HERE / "investors.json").read_text(encoding="utf-8")))
        (HERE / "investors.json").write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        render_html(doc)
        return
    LOGOS.mkdir(exist_ok=True)
    with ThreadPoolExecutor(8) as pool:
        investors = list(pool.map(enrich, SEED))
    doc = {
        "generated": date.today().isoformat(),
        "notes": "Curated list for the OWNED journal. notable_examples are illustrative, not exhaustive ('historic' = exited). aum_approx values are rounded public figures "
                 "(as of aum_as_of) and should be verified before citing. link_check records the HTTP "
                 "status at generation time; logo.source 'favicon-service' means the site logo could "
                 "not be fetched and a favicon was used instead.",
        "types": {
            "buyout": "Private equity firm acquiring control stakes, often with debt.",
            "growth": "Growth-equity / crossover investor taking minority stakes in scaling companies.",
            "venture": "Venture capital firm funding early- and mid-stage companies for minority stakes.",
            "corporate-venture": "Investment arm of an operating company, often with strategic aims.",
            "multi-strategy": "Alternative asset manager running PE alongside credit, real estate, etc.",
            "sovereign-wealth": "State-owned investor; fund LP and direct co-investor.",
        },
        "investors": investors,
    }
    add_numeric(doc)
    (HERE / "investors.json").write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    render_html(doc)
    bad = [(i["id"], k, c) for i in investors for k, c in i["link_check"].items() if c and c.get("status") != 200]
    nologo = [i["id"] for i in investors if not i["logo"]]
    fav = [i["id"] for i in investors if i["logo"] and i["logo"]["source"] != "site"]
    print(f"{len(investors)} investors; bad links: {bad}; no logo: {nologo}; favicon only: {fav}")


if __name__ == "__main__":
    main()
