#!/usr/bin/env python3
"""Generate index-card icons and hero logos for OpenCRE CRE pages.

Usage: GEMINI_API_KEY=... python3 generate_visuals.py [cre-id ...]   # default: every id in SUBJECTS
       python3 generate_visuals.py --print <cre-id>                    # show the visual-summary prompt

Icons show at 100 x 100 px on the index, so each CRE gets one hand-picked
bold object (the stock title+excerpt prompt draws noise at that size).
Logos are detailed visual summaries (explainer boards, like the LISTED
journal's headers) whose prompt is built from the CRE data: its place in the
tree, sub-requirements, related CREs, mapped standard sections and the
weaknesses it prevents. An earlier, simpler one-scene image per CRE is kept as
logo-scene.jpeg (not referenced by the pages). Images are written to the
journal-level assets/ folder, outside the generated post folders:

    assets/icons/cre-<id>.png
    assets/images/cre-<id>/logo.jpeg          (visual summary, shown on the page)
    assets/images/cre-<id>/logo-scene.jpeg    (simple scene, kept)

Existing files are skipped; delete one to regenerate it. generate_journal.py
adds icon:/logo: front matter for every file present, so run it (and
_wiring/build.py) afterwards.
"""
import concurrent.futures
import itertools
import os
import pathlib
import re
import sys

JOURNAL = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(JOURNAL.parent.parent / "_wiring"))
import generate_icons as icons  # noqa: E402
import generate_logos as logos  # noqa: E402
from generate_journal import Model, load_cres  # noqa: E402

ICON_STYLE = (
    "A single bold pictogram icon, like a road sign or an app icon glyph, designed to stay legible at 64 x 64 pixels. "
    "Exactly one object and nothing else: no secondary symbol, no badge, no small inset. "
    "The object is centered and fills about 75% of the square canvas. Very thick, uniform black strokes "
    "(about 6% of the canvas width) with rounded ends, large simple geometric shapes, no small details, no fine "
    "lines, no background scene, no frame or border. Pure black on a plain white background, no shading, "
    "no gradients, no color. No text, letters, digits or labels. Subject: "
)

LOGO_STYLE = (
    "A wide editorial illustration for an article about one software security requirement. "
    "Flat vector style, crisp outlines, minimal shading, plain light background, generous margins. "
    "Disciplined palette: deep blue, teal, green, with one orange accent. "
    "One clear scene with a single focal point, a few simple people or objects at most. "
    "No text, no letters, no labels, no logos, no screenshots full of text. "
    "No photorealism, no 3D render, no fantasy elements, no hooded hackers, no glowing binary rain. Scene: "
)

SUMMARY_STYLE = (
    "Draw a detailed infographic that summarises one software security requirement on a single wide page. "
    "Layout: the requirement's name as a bold title at the top; three to five labelled panels below it, joined by arrows "
    "into a left-to-right story (what goes wrong, what the requirement asks for and how its parts fit together, what good "
    "looks like) — give each panel its own short heading taken from the content, not these descriptions; a coloured strip at the bottom that starts with the words \"Key principle:\" followed by one short rule. "
    "Inside the panels use small flat icons and simple pictures: servers, browser windows, phones, documents, locks, people. "
    "Flat vector cartoon style, crisp outlines, minimal shading, light background, blue, teal, green and orange accents, "
    "generous margins so nothing touches the edges.\n"
    "Text rules, which matter most:\n"
    "- Every word in the picture is copied from the CONTENT section below or is a plain everyday word (Risk, Request, "
    "Server, User, Login, Reset, Allowed, Blocked). Spell every word exactly; prefer fewer, larger labels to many small ones.\n"
    "- Keep label text short: panel headings of two to five words, at most about forty words of labels outside the title "
    "and the key principle. Mock screens show blank lines or dots, not invented words or codes.\n"
    "- Never print any words from these instructions: not the words layout, panel, strip, side, content, substance, "
    "infographic, board, fragment, artifact, plain text, catalogue, tag, or any colour name.\n"
    "- Standard names (ASVS, CWE, NIST and so on) appear only as small text tags: no logos, emblems or brand marks of "
    "OWASP, NIST, ISO, MITRE, PCI or any vendor, and no social-media or app brand icons. No id numbers, dates or URLs.\n"
    "- An attacker, if shown, is a plain grey person figure with no mask or hood. "
    "No photorealism, no 3D render, no fantasy elements, no dense text poster.\n"
)


def _short(s, n=160):
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def summary_prompt(m, cid):
    """Infographic prompt built from the CRE's own data."""
    lines = [SUMMARY_STYLE, "CONTENT", f"Title: {m.name(cid)}"]
    path = m.path(cid)
    if path:
        lines.append("Part of: " + " > ".join(m.name(p) for p in path) + " (context only; at most a small breadcrumb)")
    kids = m.children[cid]
    if kids:
        lines.append("Its parts (each one a card or panel):")
        for k in kids[:12]:
            grand = [m.name(g) for g in m.children[k][:3 if len(kids) > 3 else 5]]
            lines.append(f"- {m.name(k)}" + (f" — includes: {'; '.join(grand)}" if grand else ""))
    groups = m.std_links(cid)
    threats = [d.get("section") for n in ("CWE", "CAPEC") for d, _k in groups.get(n, [])]
    if threats:
        lines.append("What goes wrong without it: " + "; ".join(_short(t, 60) for t in threats[:5]))
    per_std = [[f"- {name}: {_short(doc['section'])}" for doc, kind in groups[name]
                if kind == "curated" and re.search(r"[a-z]{3}", doc.get("section") or "", re.I)]
               for name in sorted(groups, key=str.lower) if name not in ("CWE", "CAPEC")]
    says = [row for tier in itertools.zip_longest(*per_std) for row in tier if row]  # round-robin across standards
    if says:
        lines.append("What the standards ask (paraphrase into short labels, with the standard name in a small label beside each):")
        lines += says[:6]
    related = sorted(set(m.related[cid]), key=lambda k: m.name(k).lower())
    if related:
        lines.append("See also: " + "; ".join(m.name(k) for k in related[:4]))
    if not kids and not says:
        lines.append("Show the risk this requirement addresses, the control it asks for, and the safe outcome.")
    lines.append("Key principle: write one short sentence that states this requirement as a rule.")
    return "\n".join(lines)


# cre id -> (icon subject, simple logo scene)
SUBJECTS = {
    "636-660": ("a shield",
                "a web application drawn as a simple browser window standing behind a large shield, with small arrows bouncing off the shield"),
    "546-564": ("a sewing needle with a thick thread looping once",
                "one long teal thread weaving through five different building blocks of a software system, tying them together"),
    "616-305": ("a wrench",
                "a small software team at a conveyor belt where code blocks pass through design, build, test and review stations, each with a small shield"),
    "567-755": ("a classical government building with columns",
                "a round table meeting where three people review a large rulebook and a risk chart, a shield emblem on the wall"),
    "862-452": ("a lighthouse",
                "an operations room at night with one engineer watching a large monitoring screen, a lighthouse beam visible through the window"),
    "633-428": ("a key",
                "a person approaching a large door that checks a key card, a password and a phone at the same time"),
    "270-568": ("a fingerprint",
                "a cutaway of a lock mechanism with several interchangeable cylinders: a password, a fingerprint and a hardware key"),
    "146-556": ("an equals sign made of two thick bars",
                "several different doors into the same building, each with an identical lock"),
    "576-042": ("a dumbbell",
                "a row of entry gates where the gate guarding the vault is visibly as strong as the front gate, no weak side door"),
    "278-413": ("two hands shaking",
                "two server boxes shaking hands, each showing an identity badge to the other"),
    "585-408": ("a die showing five pips",
                "a server tossing a fresh random die to a client, who must send it back signed"),
    "287-251": ("a snowflake",
                "a machine printing long unique random tickets, none of them the same, falling into a bin"),
    "002-801": ("an award rosette ribbon",
                "a shelf of cryptographic tools where only a few carry a green approval seal and an engineer picks one of those"),
    "520-617": ("a life ring",
                "a person locked out of a door being handed a new key through a secure counter after showing an ID"),
    "543-621": ("an eye crossed out by one thick diagonal bar",
                "a password reset screen that shows a blank masked field while a curious onlooker sees nothing"),
    "772-358": ("a large question mark",
                "a security question card being dropped into a recycling bin, replaced by a hardware key on the desk"),
    "358-860": ("a passport booklet",
                "a person at a counter showing a passport to recover a lost phone authenticator, a clerk checking it carefully"),
    "270-634": ("a padlock",
                "a password travelling from a laptop to a server inside a sealed armoured capsule along a cable"),
    "581-525": ("a boomerang",
                "a forgot-password flow drawn as a safe path: a time-limited token in an envelope going only to the account owner's inbox"),
    "789-320": ("a door with a round knob",
                "a calm login gate with a rate limiter turnstile, an attacker queue blocked behind it while one user walks through"),
}


def one(cid, m):
    icon_subject, scene = SUBJECTS[cid]
    slug = f"cre-{cid}"
    images = JOURNAL / "assets" / "images" / slug
    jobs = [
        (JOURNAL / "assets" / "icons" / f"{slug}.png", icons.call_gemini_image, ICON_STYLE + icon_subject + "."),
        (images / "logo-scene.jpeg", logos.call_gemini_image, LOGO_STYLE + scene + "."),
        (images / "logo.jpeg", logos.call_gemini_image, summary_prompt(m, cid)),
    ]
    results = []
    for out, call, prompt in jobs:
        if out.exists():
            results.append(f"skip {out.name}")
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        err = ""
        for _attempt in range(3):
            try:
                out.write_bytes(call(os.environ["GEMINI_API_KEY"], prompt))
                results.append(f"ok {out.name}")
                break
            except RuntimeError as e:
                err = str(e)[:80]
        else:
            results.append(f"FAIL {out.name}: {err}")
    return f"{cid}: " + ", ".join(results)


if __name__ == "__main__":
    if sys.argv[1:2] == ["--print"]:
        print(summary_prompt(Model(load_cres()), sys.argv[2]))
        sys.exit()
    ids = sys.argv[1:] or list(SUBJECTS)
    model = Model(load_cres())
    with concurrent.futures.ThreadPoolExecutor(6) as ex:
        for r in ex.map(lambda c: one(c, model), ids):
            print(r, flush=True)
