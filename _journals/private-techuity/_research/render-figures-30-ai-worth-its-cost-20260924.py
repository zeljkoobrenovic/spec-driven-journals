#!/usr/bin/env python3.11
"""Render Figures 1 and 3 of 30-ai-worth-its-cost from numeric coordinates.

In-depth review 24 September 2026, round 2, finding AIC-015: the Gemini renders
of the bridge chart and the commitment-floor figure carried correct labels but
inconsistent geometry (the April bar about 10% tall against the other bars; the
€3,900 floor placed too near €5,200 although it is 600 above €3,300 and 1,300
below €5,200). Two re-rolls in round 1 were worse. As for the layoff chapter's
cash chart (render-cash-chart-anatomy-of-a-layoff-20260923.py), both figures are
authored SVG plotted from the article's figures and rasterized with Playwright
(python3.11), so every height is proportional on one scale.

Bridge: €1,400 + €2,644 (usage) + €3,236 (construction) − €1,456 (rates) = €5,824.
Floor: range €3,300 / €5,200 / €7,600 a month at list price; floors B €3,900,
C €2,400; stress case €2,000.

Usage: python3.11 render-figures-30-ai-worth-its-cost-20260924.py [--out-dir DIR]
Writes <out-dir>/usage-construction-rates-bridge.jpeg and
<out-dir>/commitment-floor-against-demand-range.jpeg (default /tmp/aic-figures);
install with regen-figures-30-ai-worth-its-cost-20260924-r2.py --accept.

Round 4 (AIC-020): the Option B and stress-case labels are lettered in dark ink (their amber
lines stay), because amber lettering on the teal band measured about 1.3:1 and vanished at
phone width; floor labels are 40 px. Installed with ...-r4.py --accept fig3.
"""
from __future__ import annotations
import argparse, hashlib
from html import escape
from io import BytesIO
from pathlib import Path

IVORY, INK, TEAL, OCHRE, MUTED = '#f8f5ec', '#1e2b4a', '#8fbfb8', '#dca346', '#5d6b7a'
W, H = 1600, 900
FONT = "font-family=\"'Helvetica Neue', Helvetica, Arial, sans-serif\""


def text(x, y, words, size=34, color=INK, weight=400, anchor='start'):
    return (f'<text x="{x:.1f}" y="{y:.1f}" {FONT} font-size="{size}" font-weight="{weight}" '
            f'fill="{color}" text-anchor="{anchor}">{escape(words)}</text>')


def svg(body: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<rect width="{W}" height="{H}" fill="{IVORY}"/>{body}</svg>')


def bridge() -> str:
    april, usage, construction, rates = 1400, 2644, 3236, -1456
    peak = april + usage + construction            # 7280
    august = peak + rates                          # 5824
    assert august == 5824
    base_y, top_y = 760, 120                       # baseline and the y of the peak
    scale = (base_y - top_y) / peak                # pixels per euro, one scale for every bar
    def y(v): return base_y - v * scale
    bw, gap, x0 = 170, 110, 170
    xs = [x0 + i * (bw + gap) for i in range(5)]
    b = []
    b.append('<defs><pattern id="hatch" patternUnits="userSpaceOnUse" width="14" height="14" patternTransform="rotate(45)">'
             f'<line x1="0" y1="0" x2="0" y2="14" stroke="{INK}" stroke-width="2"/></pattern></defs>')
    # bar 1: April, full bar
    b.append(f'<rect x="{xs[0]}" y="{y(april):.1f}" width="{bw}" height="{base_y - y(april):.1f}" fill="{INK}"/>')
    b.append(text(xs[0] + bw / 2, y(april) - 18, '€1,400', 36, INK, 700, 'middle'))
    # bar 2: usage, floating step
    b.append(f'<rect x="{xs[1]}" y="{y(april + usage):.1f}" width="{bw}" height="{usage * scale:.1f}" fill="{TEAL}" stroke="{INK}" stroke-width="3"/>')
    b.append(text(xs[1] + bw + 14, y(april + usage / 2) + 12, '+€2,644', 36, INK, 700))
    # bar 3: construction, floating step
    b.append(f'<rect x="{xs[2]}" y="{y(peak):.1f}" width="{bw}" height="{construction * scale:.1f}" fill="{OCHRE}" stroke="{INK}" stroke-width="3"/>')
    b.append(text(xs[2] + bw + 14, y(april + usage + construction / 2) + 12, '+€3,236', 36, INK, 700))
    # bar 4: rates, hatched drop with a downward arrow
    b.append(f'<rect x="{xs[3]}" y="{y(peak):.1f}" width="{bw}" height="{-rates * scale:.1f}" fill="url(#hatch)" stroke="{INK}" stroke-width="3"/>')
    ax = xs[3] + bw + 40
    b.append(f'<path d="M{ax} {y(peak) + 8:.1f} V{y(august) - 14:.1f}" stroke="{INK}" stroke-width="4"/>')
    b.append(f'<path d="M{ax - 12} {y(august) - 26:.1f} L{ax} {y(august) - 4:.1f} L{ax + 12} {y(august) - 26:.1f} Z" fill="{INK}"/>')
    b.append(text(ax + 22, y(peak) + 40, '−€1,456', 36, INK, 700))
    # bar 5: August, full bar
    b.append(f'<rect x="{xs[4]}" y="{y(august):.1f}" width="{bw}" height="{base_y - y(august):.1f}" fill="{INK}"/>')
    b.append(text(xs[4] + bw / 2, y(august) - 18, '€5,824', 36, INK, 700, 'middle'))
    # dashed connectors from each step's top to the start of the next
    for i, v in enumerate([april, april + usage, peak, august]):
        b.append(f'<path d="M{xs[i] + bw} {y(v):.1f} H{xs[i + 1]}" stroke="{INK}" stroke-width="2.5" stroke-dasharray="10 8"/>')
    # baseline and category labels
    b.append(f'<path d="M{xs[0] - 60} {base_y} H{xs[4] + bw + 60}" stroke="{INK}" stroke-width="4"/>')
    for x, w in zip(xs, ['April', 'Usage', 'Construction', 'Rates', 'August']):
        b.append(text(x + bw / 2, base_y + 58, w, 36, INK, 400, 'middle'))
    return svg(''.join(b))


def floor() -> str:
    low, expected, high, stress, floor_b, floor_c = 3300, 5200, 7600, 2000, 3900, 2400
    top_value = 8400
    base_y, top_y = 800, 150
    scale = (base_y - top_y) / top_value
    def y(v): return base_y - v * scale
    ax_x, right = 140, 1500
    b = []
    b.append('<defs><filter id="soft" x="-5%" y="-10%" width="110%" height="120%"><feGaussianBlur stdDeviation="6"/></filter></defs>')
    # heading
    b.append(text(W / 2 + 40, 66, 'Demand range 2028', 44, INK, 700, 'middle'))
    b.append(text(W / 2 + 40, 112, 'euros a month at list price', 34, INK, 400, 'middle'))
    # axis
    b.append(f'<path d="M{ax_x} {top_y - 40} V{base_y} H{right}" fill="none" stroke="{INK}" stroke-width="4"/>')
    # band low..high
    b.append(f'<rect x="{ax_x + 30}" y="{y(high):.1f}" width="{right - ax_x - 60}" height="{y(low) - y(high):.1f}" fill="{TEAL}" opacity="0.75" filter="url(#soft)"/>')
    b.append(text(W / 2 + 40, y(high) + 44, '€7,600 high', 32, INK, 700, 'middle'))
    b.append(text(ax_x + 60, y(low) - 12, '€3,300 low', 32, INK, 700))
    # expected dashed line
    b.append(f'<path d="M{ax_x + 30} {y(expected):.1f} H{right - 30}" stroke="{INK}" stroke-width="3" stroke-dasharray="14 10"/>')
    b.append(text(W / 2 + 40, y(expected) - 12, '€5,200 expected', 32, INK, 700, 'middle'))
    # floors: thick lines with a downward bracket at the right end
    def floor_line(v, color, label, label_x, anchor):
        b.append(f'<path d="M{ax_x + 30} {y(v):.1f} H{right - 30} v18" fill="none" stroke="{color}" stroke-width="9" stroke-linecap="square"/>')
        b.append(text(label_x, y(v) - 16, label, 40, INK, 700, anchor))
    floor_line(floor_b, OCHRE, 'Option B floor €3,900', right - 60, 'end')
    floor_line(floor_c, INK, 'Option C floor €2,400', right - 60, 'end')
    # check mark after the Option C label
    cx = right - 40
    b.append(f'<path d="M{cx} {y(floor_c) - 26} l10 12 l22 -30" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>')
    # stress case dashed line, label below it
    b.append(f'<path d="M{ax_x + 30} {y(stress):.1f} H{right - 30}" stroke="{OCHRE}" stroke-width="3" stroke-dasharray="14 10"/>')
    b.append(text(ax_x + 60, y(stress) + 44, '€2,000 stress case', 36, INK, 700))
    return svg(''.join(b))


def rasterize(markup: str) -> bytes:
    from playwright.sync_api import sync_playwright
    from PIL import Image
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': W, 'height': H})
        page.set_content(f'<html><body style="margin:0">{markup}</body></html>')
        png = page.screenshot(clip={'x': 0, 'y': 0, 'width': W, 'height': H})
        browser.close()
    buf = BytesIO()
    Image.open(BytesIO(png)).convert('RGB').save(buf, 'JPEG', quality=92)
    return buf.getvalue()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--out-dir', default='/tmp/aic-figures')
    args = ap.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in [('usage-construction-rates-bridge', bridge), ('commitment-floor-against-demand-range', floor)]:
        markup = fn()
        (out / f'{name}.svg').write_text(markup)
        data = rasterize(markup)
        (out / f'{name}.jpeg').write_bytes(data)
        print('written', out / f'{name}.jpeg', hashlib.sha256(data).hexdigest()[:12])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
