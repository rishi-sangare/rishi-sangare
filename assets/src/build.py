"""Generates the animated profile SVGs (dark + light) into ../

Run: python3 assets/src/build.py
"""
import random
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"

THEMES = {
    "dark": dict(bg="#0d1117", panel="#161b22", border="#30363d", ink="#e6edf3", ink2="#9da7b3",
                 ink3="#6e7681", c1="#22d3ee", c2="#a78bfa", c3="#3fb950", c4="#f0b429", slab=0.16, star="#c9d1d9"),
    "light": dict(bg="#ffffff", panel="#f6f8fa", border="#d0d7de", ink="#1f2328", ink2="#59636e",
                  ink3="#818b98", c1="#0891b2", c2="#7c3aed", c3="#1a7f37", c4="#b7791f", slab=0.10, star="#8c959f"),
}


def svg(w, h, body, t, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>'
            f'<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{t["c1"]}"/>'
            f'<stop offset="1" stop-color="{t["c2"]}"/></linearGradient></defs>{body}</svg>')


def text(x, y, s, size, fill, weight=400, family=FONT, anchor="start", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" {extra}>{escape(s)}</text>')


def reveal(attr, frm, to, delay, dur=0.6):
    """Animate attr from frm to to after `delay`, always starting at t=0 so the static
    value (to) shows wherever SMIL doesn't run, and nothing waits on a delayed begin."""
    total = delay + dur
    if delay <= 0:
        return f'values="{frm};{to}" keyTimes="0;1" dur="{dur}s"'
    k = delay / total
    return f'values="{frm};{frm};{to}" keyTimes="0;{k:.3f};1" dur="{total:.2f}s"'


def fade_in(i, base=0.0, step=0.12):
    # Text stays static on purpose: if a renderer pauses the SMIL timeline, animated
    # reveals would leave the content invisible. Only decoration moves.
    return ""


def chip(x, y, label, t, color=None):
    w = len(label) * 7.4 + 22
    c = color or t["ink2"]
    return (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="26" rx="13" fill="{t["panel"]}" stroke="{t["border"]}"/>'
            + text(x + w / 2, y + 17.5, label, 12.5, c, 500, MONO, "middle")), w


# ---------------------------------------------------------------- hero
def hero(t):
    W, H = 1280, 400
    rnd = random.Random(7)
    b = [f'<rect width="{W}" height="{H}" rx="16" fill="{t["bg"]}"/>']
    # stars
    for _ in range(46):
        x, y = rnd.uniform(20, W - 20), rnd.uniform(14, 190)
        r = rnd.choice([0.8, 1, 1.2, 1.5])
        d = rnd.uniform(2.5, 6)
        b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{t["star"]}" opacity="0.2">'
                 f'<animate attributeName="opacity" values="0.15;0.85;0.15" dur="{d:.1f}s" '
                 f'begin="{rnd.uniform(0, 4):.1f}s" repeatCount="indefinite"/></circle>')
    # perspective grid floor (right side), faded towards the text with a mask
    VPx, VPy = 960, 214
    b.append(f'<defs><linearGradient id="fade" x1="0" x2="1"><stop offset="0.38" stop-color="#fff" stop-opacity="0"/>'
             f'<stop offset="0.62" stop-color="#fff" stop-opacity="1"/></linearGradient>'
             f'<linearGradient id="fadev" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
             f'<stop offset="0.35" stop-color="#fff" stop-opacity="1"/></linearGradient>'
             f'<mask id="gm"><rect x="0" y="{VPy}" width="{W}" height="{H - VPy}" fill="url(#fade)"/></mask>'
             f'<mask id="gmv"><rect x="0" y="{VPy}" width="{W}" height="{H - VPy}" fill="url(#fadev)"/></mask>'
             f'<clipPath id="hc"><rect width="{W}" height="{H}" rx="16"/></clipPath></defs>')
    g = [f'<g clip-path="url(#hc)" mask="url(#gm)"><g mask="url(#gmv)" stroke="{t["c1"]}" stroke-width="1" opacity="0.55">']
    for k in range(-14, 15):
        x2 = VPx + k * 95
        g.append(f'<line x1="{VPx}" y1="{VPy}" x2="{x2}" y2="{H + 40}"/>')
    for i in range(7):  # horizontal lines rushing towards the viewer
        g.append(f'<line x1="0" x2="{W}" y1="{VPy}" y2="{VPy}">'
                 f'<animate attributeName="y1" values="{VPy};{H + 10}" dur="3.5s" begin="{i * 0.5:.1f}s" '
                 f'repeatCount="indefinite" calcMode="spline" keySplines="0.55 0 1 1" keyTimes="0;1"/>'
                 f'<animate attributeName="y2" values="{VPy};{H + 10}" dur="3.5s" begin="{i * 0.5:.1f}s" '
                 f'repeatCount="indefinite" calcMode="spline" keySplines="0.55 0 1 1" keyTimes="0;1"/></line>')
    g.append('</g></g>')
    b += g
    # horizon glow
    b.append(f'<line x1="560" x2="{W}" y1="{VPy}" y2="{VPy}" stroke="url(#g)" stroke-width="1.5" opacity="0.9"/>')

    # isometric stack: four floating layers
    cx, w, h, d = 1000, 230, 115, 14
    layers = [("evals · golden sets", t["c2"]), ("llm orchestration", t["c1"]),
              ("search · retrieval", t["c3"]), ("infra · ci/cd", t["c4"])]
    ys = [92, 148, 204, 260]
    stack = []
    for idx in reversed(range(4)):
        cy = ys[idx]
        label, col = layers[idx]
        top = f"{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}"
        left = f"{cx - w / 2},{cy} {cx},{cy + h / 2} {cx},{cy + h / 2 + d} {cx - w / 2},{cy + d}"
        right = f"{cx + w / 2},{cy} {cx},{cy + h / 2} {cx},{cy + h / 2 + d} {cx + w / 2},{cy + d}"
        bob = (f'<animateTransform attributeName="transform" type="translate" values="0 0;0 -5;0 0" '
               f'dur="4s" begin="{idx * 0.35:.2f}s" repeatCount="indefinite" calcMode="spline" '
               f'keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>')
        stack.append(
            f'<g>{bob}'
            f'<polygon points="{left}" fill="{col}" opacity="{t["slab"] + 0.22}"/>'
            f'<polygon points="{right}" fill="{col}" opacity="{t["slab"] + 0.12}"/>'
            f'<polygon points="{top}" fill="{t["bg"]}"/>'
            f'<polygon points="{top}" fill="{col}" fill-opacity="{t["slab"]}" stroke="{col}" stroke-width="1.5"/>'
            f'<line x1="{cx - w / 2 - 6}" y1="{cy}" x2="{cx - w / 2 - 34}" y2="{cy}" stroke="{col}" stroke-width="1" opacity="0.8"/>'
            + text(cx - w / 2 - 40, cy + 4, label, 12.5, col, 600, MONO, "end")
            + '</g>')
    b += stack
    # data packet falling through the layers
    b.append(f'<circle cx="{cx}" r="5" fill="{t["c1"]}"><animate attributeName="cy" values="40;{ys[-1] + 10}" '
             f'dur="2.4s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;1;0" '
             f'keyTimes="0;0.1;0.85;1" dur="2.4s" repeatCount="indefinite"/></circle>')
    b.append(f'<circle cx="{cx}" r="12" fill="{t["c1"]}" opacity="0.18"><animate attributeName="cy" values="40;{ys[-1] + 10}" '
             f'dur="2.4s" repeatCount="indefinite"/></circle>')

    # left: text block
    L = 64
    b.append(f'<g>{fade_in(0)}' + text(L, 92, "~/rishi $ whoami", 15, t["c3"], 600, MONO)
             + f'<rect x="{L + 150}" y="80" width="9" height="16" fill="{t["c3"]}"><animate attributeName="opacity" '
               f'values="1;0;1" dur="1s" repeatCount="indefinite" calcMode="discrete"/></rect></g>')
    b.append(f'<g>{fade_in(1)}' + text(L, 162, "Rishi Sangare", 64, "url(#g)", 750, FONT,
                                                   extra='letter-spacing="-1.5"') + '</g>')
    b.append(f'<g>{fade_in(2)}' + text(L, 206, "AI / LLM Systems Engineer", 26, t["ink"], 600) + '</g>')
    tag = "I ship LLM products to production, and prove they work."
    b.append(f'<clipPath id="type"><rect x="{L}" y="226" width="560" height="34"/></clipPath>'
             f'<g clip-path="url(#type)">' + text(L, 250, tag, 18, t["ink2"]) + '</g>')
    x = L
    chips = []
    for i, c in enumerate(["Python", "FastAPI", "Elasticsearch", "LLM evals", "TypeScript", "Supabase"]):
        s, w_ = chip(x, 280, c, t)
        chips.append(f'<g>{fade_in(i, 1.6, 0.08)}{s}</g>')
        x += w_ + 8
    b += chips
    b.append(f'<g>{fade_in(0, 2.3)}'
             f'<circle cx="{L + 5}" cy="345" r="4.5" fill="{t["c3"]}"><animate attributeName="r" values="4.5;6.5;4.5" '
             f'dur="1.6s" repeatCount="indefinite"/></circle>'
             + text(L + 18, 350, "Open to full-time remote roles  ·  Mumbai, India  ·  works US hours", 14, t["ink2"], 500)
             + '</g>')
    return svg(W, H, "".join(b), t, "Rishi Sangare, AI / LLM Systems Engineer")


# ---------------------------------------------------------------- stats
STATS = [
    ("372", "pull requests authored", "338 merged"),
    ("253K+", "CRM records migrated", "0 missing, 99.97% exact"),
    ("0.19→0.57", "recall@10 after eval rebuild", "same model, honest metric"),
    ("24", "models in an LLM bake-off", "3,162 live turns"),
    ("4", "production AI products", "built, shipped, operated"),
]


def stats(t):
    W, H, n, gap, m = 1280, 140, 5, 14, 0
    tw = (W - 2 * m - gap * (n - 1)) / n
    b = []
    for i, (num, l1, l2) in enumerate(STATS):
        x = m + i * (tw + gap)
        size = 36 if len(num) <= 5 else 30
        b.append(f'<g>{fade_in(i, 0.1, 0.15)}'
                 f'<rect x="{x + .5:.1f}" y="10.5" width="{tw - 1:.1f}" height="{H - 21}" rx="12" fill="{t["panel"]}" stroke="{t["border"]}"/>'
                 f'<rect x="{x + 18:.1f}" y="10.5" width="{tw - 36:.0f}" height="3" rx="1.5" fill="url(#g)">'
                 f'<animate attributeName="width" {reveal("w", 0, round(tw - 36), 0.4 + i * 0.15, 1)} fill="freeze"/></rect>'
                 + text(x + 20, 62, num, size, "url(#g)", 750, FONT, extra='letter-spacing="-0.5"')
                 + text(x + 20, 90, l1, 14, t["ink"], 600)
                 + text(x + 20, 111, l2, 12.5, t["ink3"], 500, MONO) + '</g>')
    return svg(W, H, "".join(b), t, "Highlights: 372 PRs, 253K records migrated, recall 0.19 to 0.57, 24-model bake-off, 4 products")


# ---------------------------------------------------------------- pipeline
def pipeline(t):
    W, H = 1280, 330
    nodes = [("REQUEST", "JD or candidate", "EN / JA", t["ink2"]),
             ("CLARIFY", "3-turn LLM dialog", "bad questions 85%→0%", t["c2"]),
             ("RETRIEVE", "Elasticsearch + filters", "recall@10 0.19→0.57", t["c3"]),
             ("EVALUATE", "parallel LLM judges", "Cerebras + fallback", t["c1"]),
             ("DELIVER", "ranked + HMAC webhook", "idempotent sessions", t["c4"])]
    bw, bh, y, gap = 212, 92, 70, 50
    x0 = (W - (5 * bw + 4 * gap)) / 2
    b = [f'<rect width="{W}" height="{H}" rx="16" fill="{t["bg"]}" stroke="{t["border"]}"/>',
         text(32, 40, "PRODUCTION · LLM candidate ↔ job matching for a Japanese recruiting platform", 13, t["ink3"], 600, MONO)]
    centers = [(x0 + i * (bw + gap) + bw / 2, y + bh / 2) for i in range(5)]
    p0, p4 = centers[0], centers[-1]
    path = f"M{p0[0]:.1f} {p0[1]} L{p4[0]:.1f} {p4[1]}"
    for i, col in enumerate([t["c1"], t["c2"], t["c3"]]):
        b.append(f'<circle r="5" fill="{col}" opacity="0"><animateMotion path="{path}" dur="4.5s" begin="{i * 1.5}s" repeatCount="indefinite"/>'
                 f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.05;0.9;1" dur="4.5s" begin="{i * 1.5}s" repeatCount="indefinite"/></circle>')
    for i, (k, l1, l2, col) in enumerate(nodes):
        x = x0 + i * (bw + gap)
        b.append(f'<g>{fade_in(i, 0.1, 0.15)}'
                 f'<rect x="{x:.1f}" y="{y}" width="{bw}" height="{bh}" rx="12" fill="{t["panel"]}" stroke="{col}" stroke-width="1.5"/>'
                 + text(x + 16, y + 26, k, 12, col, 700, MONO, extra='letter-spacing="1.5"')
                 + text(x + 16, y + 52, l1, 15, t["ink"], 600)
                 + text(x + 16, y + 74, l2, 12.5, t["ink2"], 500, MONO) + '</g>')
        if i < 4:
            ax = x + bw + 6
            b.append(f'<path d="M{ax:.1f} {y + bh / 2} h{gap - 14}" stroke="{t["border"]}" stroke-width="2"/>'
                     f'<path d="M{ax + gap - 18:.1f} {y + bh / 2 - 5} l6 5 l-6 5" fill="none" stroke="{t["ink3"]}" stroke-width="2"/>')
    # eval harness loop
    ey = 232
    ex1, ex2 = centers[1][0] - bw / 2, centers[3][0] + bw / 2
    b.append(f'<g>{fade_in(0, 0.9)}'
             f'<rect x="{ex1:.1f}" y="{ey}" width="{ex2 - ex1:.1f}" height="64" rx="12" fill="none" stroke="url(#g)" stroke-width="1.5" stroke-dasharray="6 6">'
             f'<animate attributeName="stroke-dashoffset" from="0" to="-24" dur="1.2s" repeatCount="indefinite"/></rect>'
             + text((ex1 + ex2) / 2, ey + 27, "EVAL HARNESS", 12, t["c2"], 700, MONO, "middle", 'letter-spacing="1.5"')
             + text((ex1 + ex2) / 2, ey + 49, "golden sets · recall@k / MRR · LLM-as-judge · bias probes · cost per search", 13.5, t["ink2"], 500, FONT, "middle")
             + '</g>')
    for c in centers[1:4]:
        b.append(f'<line x1="{c[0]:.1f}" y1="{y + bh + 4}" x2="{c[0]:.1f}" y2="{ey - 4}" stroke="{t["ink3"]}" stroke-width="1.5" stroke-dasharray="3 5">'
                 f'<animate attributeName="stroke-dashoffset" from="0" to="16" dur="0.8s" repeatCount="indefinite"/></line>')
    return svg(W, H, "".join(b), t, "LLM matching pipeline: request, clarify, retrieve, evaluate, deliver, with an eval harness")


# ---------------------------------------------------------------- project cards
CARDS = {
    "card-refinecv": ("RefineCV", "B2B CV-formatting SaaS · co-lead engineer",
                      "435 commits · 203 PRs in 5 months",
                      "Closed a cross-tenant authz flaw across 63 call sites",
                      ["FastAPI", "React 19", "Supabase", "WeasyPrint"], "c1"),
    "card-copilot": ("Recruiter Copilot", "AI candidate scoring on LinkedIn · Chrome Web Store",
                     "11 releases · 400+ installs · 847 tests",
                     "Fixed a cross-account RLS leak and a billing exploit",
                     ["Chrome MV3", "Supabase Edge", "LLM scoring"], "c2"),
    "card-migration": ("CRM Migration", "18 GB keyless SQL Server → REST-only CRM · sole engineer",
                       "253,541 activities · 36,661 people · 0 missing",
                       "Found a platform concurrency bug creating ghost rows",
                       ["Node.js", "SQL Server", "Idempotent ETL"], "c3"),
    "card-cosmeon": ("COSMEON FS-LITE", "Orbital file system simulator · open source",
                     "Reed-Solomon across 6 LEO satellites",
                     "Contact Graph Routing, Merkle checks, DTN, live viz",
                     ["TypeScript", "React", "WebSockets"], "c4"),
}


def card(t, key):
    name, sub, metric, hl, tags, ck = CARDS[key]
    col = t[ck]
    W, H = 620, 200
    b = [f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="{t["panel"]}" stroke="{t["border"]}"/>',
         f'<rect x="0" y="22" width="4" height="{H - 44}" rx="2" fill="{col}"><animate attributeName="height" {reveal("h", 0, H - 44, 0, 0.9)} fill="freeze"/></rect>',
         f'<circle cx="{W - 30}" cy="32" r="5" fill="{col}"><animate attributeName="opacity" values="1;0.25;1" dur="2s" repeatCount="indefinite"/></circle>',
         text(28, 46, name, 24, t["ink"], 700),
         text(28, 72, sub, 14, t["ink2"], 500),
         text(28, 108, metric, 15, col, 650, MONO),
         text(28, 134, hl, 14, t["ink"], 500)]
    x = 28
    for tag in tags:
        s, w_ = chip(x, 154, tag, t)
        b.append(s)
        x += w_ + 8
    return svg(W, H, "".join(b), t, f"{name}: {sub}")


def main():
    for mode, t in THEMES.items():
        (OUT / f"hero-{mode}.svg").write_text(hero(t))
        (OUT / f"stats-{mode}.svg").write_text(stats(t))
        (OUT / f"pipeline-{mode}.svg").write_text(pipeline(t))
        for key in CARDS:
            (OUT / f"{key}-{mode}.svg").write_text(card(t, key))
    print("written to", OUT)


if __name__ == "__main__":
    main()
