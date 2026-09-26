#!/usr/bin/env python3.11
"""Render Figure 1 of 23-anatomy-of-a-layoff as a chart plotted from the cash model.

In-depth review 23 September 2026, finding LAY-001: the Gemini illustration
started all three lines together, showed no November bridge receipt, crossed
the reserve in December for the no-bridge case and flattened the plan's line
after February. This authored SVG is plotted from the same month-end
arithmetic as the article's cash table, so every point is exact; Playwright
(python3.11) rasterizes it to the existing JPEG path. The replaced image is
archived under `_research/discarded-illustration-variants/`.

Model: cash at month end = previous cash + funding received - burn before R2
+ R2 saving - R2 one-off cost. Opening cash €1.0m on 1 October; burn €200,000
in October and €150,000 from November (R1); bridge €600,000 received in
November. Reserve-crossing points assume even spending within the month.

Usage: python3.11 render-cash-chart-anatomy-of-a-layoff-20260923.py [--out PATH]
"""
from __future__ import annotations
import argparse, hashlib
from html import escape
from pathlib import Path

J = Path(__file__).resolve().parents[1]
POST = J / 'posts/23-anatomy-of-a-layoff'
ASSET = POST / 'assets/images/24-anatomy-of-a-layoff/cash-by-date-under-three-plans.jpeg'
ARCHIVE = J / '_research/discarded-illustration-variants'

IVORY, INK, TEAL, OCHRE, MUTED, GRID = '#f6f1e6', '#24394a', '#2f7a74', '#b8791f', '#6b7c84', '#ddd5c4'
W, H = 1600, 1000
L, R, T, B = 210, 60, 70, 150          # plot margins
YMAX = 1300                            # € thousands
MONTHS = ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
XMAX = 11                              # x = 0 is 1 October; x = k is the end of MONTHS[k-1] (a month boundary)

BURN = [200, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150]
FUND = [0, 600, 0, 0, 0, 0, 0, 0, 0, 0, 0]
SAVE = [0, 0, 20, 45, 63.5, 63.5, 72, 72, 72, 72, 72]
ONE_OFF = [0, 30, 45, 32, 0, 13, 0, 0, 0, 0, 0]


def series(bridge: bool, r2: bool) -> list[float]:
    cash, out = 1000.0, [1000.0]
    for k in range(len(MONTHS)):
        cash += (FUND[k] if bridge else 0) - BURN[k] + ((SAVE[k] - ONE_OFF[k]) if r2 else 0)
        out.append(cash)
    return out


def crossing(values: list[float], level: float = 400) -> float:
    for k in range(1, len(values)):
        if values[k - 1] >= level > values[k]:
            return k - 1 + (values[k - 1] - level) / (values[k - 1] - values[k])
    raise ValueError('no crossing')


PLAN, NO_R2, NO_BRIDGE = series(True, True), series(True, False), series(False, True)
# The article's table and text; fail loudly if the model drifts from them.
assert [PLAN[i] for i in (1, 2, 3, 4, 9, 10)] == [800, 1220, 1045, 908, 488, 410]
assert [NO_R2[i] for i in (2, 3, 9)] == [1250, 1100, 200]
assert [NO_BRIDGE[i] for i in (3, 4)] == [445, 308]


def px(x: float) -> float:
    return L + x * (W - L - R) / XMAX


def py(y: float) -> float:
    return T + (YMAX - y) * (H - T - B) / YMAX


def path(points: list[tuple[float, float]]) -> str:
    return 'M' + ' L'.join(f'{px(x):.1f} {py(y):.1f}' for x, y in points)


def text(x, y, words, size=30, color=INK, weight=400, anchor='start'):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{escape(words)}</text>')


def dot(x, y, color, r=8):
    return f'<circle cx="{px(x):.1f}" cy="{py(y):.1f}" r="{r}" fill="{color}" stroke="{IVORY}" stroke-width="3"/>'


def build() -> str:
    body = []
    # Band: months in which R2's leaving costs are paid (November to March).
    body.append(f'<rect x="{px(1):.1f}" y="{T}" width="{px(6) - px(1):.1f}" height="{py(0) - T:.1f}" fill="#efe6d2"/>')
    body.append(text((px(1) + px(6)) / 2, py(0) - 18, 'R2 leaving costs paid, Nov to Mar', 26, MUTED, 400, 'middle'))
    # Grid and y labels.
    for y in range(0, YMAX + 1, 200):
        body.append(f'<path d="M{L} {py(y):.1f} H{W - R}" stroke="{GRID}" stroke-width="1.5"/>')
        body.append(text(L - 16, py(y) + 10, f'€{y * 1000:,}', 28, MUTED, 400, 'end'))
    # X axis: ticks at month boundaries, month names centred on each month's span.
    for k in range(0, XMAX + 1):
        body.append(f'<path d="M{px(k):.1f} {py(0):.1f} v12" stroke="{INK}" stroke-width="2"/>')
    for k, m in enumerate(MONTHS):
        body.append(text(px(k + 0.5), py(0) + 44, m, 28, INK, 400, 'middle'))
    body.append(text((L + W - R) / 2, H - 40, 'Cash on 1 October, then at the end of each month', 28, MUTED, 400, 'middle'))
    body.append(f'<path d="M{L} {py(0):.1f} H{W - R}" stroke="{INK}" stroke-width="2"/>')
    # 30 June marker (the condition's date).
    body.append(f'<path d="M{px(9):.1f} {T} V{py(0):.1f}" stroke="{INK}" stroke-width="2" stroke-dasharray="3 7"/>')
    body.append(text(px(9) + 12, T + 30, '30 June:', 26, INK, 700))
    body.append(text(px(9) + 12, T + 62, 'condition date', 26, INK, 400))
    # Reserve line.
    body.append(f'<path d="M{L} {py(400):.1f} H{W - R}" stroke="{INK}" stroke-width="3" stroke-dasharray="14 10"/>')
    body.append(text(W - R, py(400) + 38, 'Reserve €400,000', 30, INK, 700, 'end'))

    # Series 3: R2 without the bridge, to the end of March.
    nb = [(k, NO_BRIDGE[k]) for k in range(0, 7)]
    body.append(f'<path d="{path(nb)}" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linejoin="round"/>')
    xc = crossing(NO_BRIDGE)
    body.append(dot(xc, 400, MUTED, 10))
    body.append(text(px(3) - 30, py(270), 'R2, no bridge:', 28, MUTED, 700, 'end'))
    body.append(text(px(3) - 30, py(270) + 34, 'below reserve', 28, MUTED, 400, 'end'))
    body.append(text(px(3) - 30, py(270) + 68, 'about 10 Jan', 28, MUTED, 400, 'end'))

    # Series 2: bridge without R2 (comparison: fails the condition), to 30 June.
    b1 = [(k, NO_R2[k]) for k in range(0, 10)]
    body.append(f'<path d="{path(b1)}" fill="none" stroke="{OCHRE}" stroke-width="6" stroke-dasharray="18 10" stroke-linejoin="round"/>')
    body.append(dot(crossing(NO_R2), 400, OCHRE, 10))
    body.append(dot(9, NO_R2[9], OCHRE))
    body.append(text(px(9) + 18, py(NO_R2[9]) + 10, '€200,000', 28, OCHRE, 700))
    body.append(text(px(5.2), py(1010), 'Bridge, no R2: a comparison that', 28, OCHRE, 700))
    body.append(text(px(5.2), py(1010) + 34, 'fails the condition; reserve about 20 May', 28, OCHRE, 400))

    # Series 1: the plan, bridge and R2, to the reserve crossing in early August.
    xp = crossing(PLAN)
    plan = [(k, PLAN[k]) for k in range(0, 11)] + [(xp, 400)]
    body.append(f'<path d="{path(plan)}" fill="none" stroke="{TEAL}" stroke-width="8" stroke-linejoin="round"/>')
    body.append(dot(xp, 400, TEAL, 11))
    body.append(dot(2, PLAN[2], TEAL))
    body.append(dot(9, PLAN[9], TEAL))
    body.append(text(px(2) + 18, py(PLAN[2]) - 22, 'Bridge €600,000 received in November', 28, INK, 700))
    body.append(text(px(9) + 18, py(PLAN[9]) - 12, '€488,000', 30, TEAL, 700))
    body.append(text(px(9) + 14, py(860), 'Bridge + R2', 30, TEAL, 700))
    body.append(text(px(9) + 14, py(860) + 36, '(the plan):', 30, TEAL, 700))
    body.append(text(px(9) + 14, py(860) + 72, 'reserve early Aug', 30, TEAL, 400))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<rect width="{W}" height="{H}" fill="{IVORY}"/>' + ''.join(body) + '</svg>')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=None)
    args = ap.parse_args()
    from playwright.sync_api import sync_playwright
    svg = build()
    out = Path(args.out) if args.out else ASSET
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': W, 'height': H})
        page.set_content(f'<html><body style="margin:0">{svg}</body></html>')
        png = page.screenshot(clip={'x': 0, 'y': 0, 'width': W, 'height': H})
        browser.close()
    from io import BytesIO
    from PIL import Image
    buf = BytesIO()
    Image.open(BytesIO(png)).convert('RGB').save(buf, 'JPEG', quality=92)
    data = buf.getvalue()
    if out == ASSET and ASSET.exists():
        previous = ASSET.read_bytes()
        ARCHIVE.mkdir(exist_ok=True)
        (ARCHIVE / f'23-anatomy-of-a-layoff-cash-by-date-{hashlib.sha256(previous).hexdigest()[:12]}.jpeg').write_bytes(previous)
    out.write_bytes(data)
    (out.with_suffix('.svg') if out != ASSET else Path('/tmp/anatomy-cash-chart.svg')).write_text(svg)
    print('written', out, hashlib.sha256(data).hexdigest())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
