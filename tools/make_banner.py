"""Generate the profile banner (assets/banner-light.svg, assets/banner-dark.svg).

A flat-colour desk scene: code on the laptop, and a cat at the gamepad playing
a little endless-runner on the monitor (the hero is a pixel cat, naturally).
Light mode is daytime (sun), dark mode is night (moon and stars). No gradients.

Run from the repo root:  python3 tools/make_banner.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"

SANS = "'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'DejaVu Sans Mono', monospace"

THEMES = {
    "light": dict(
        bg="#fdf8f1", ink="#2b211c", muted="#7a6a5f", line="#eadfce",
        amber="#ea580c", apricot="#f59e0b", deep="#7c2d12", teal="#0f8a7e",
        desk="#ecd9c0", desk_edge="#dcc19f",
        lid="#3b2f2a", screen="#211a16", code="#f7efe6", code_muted="#9b8b80",
        cat="#8a8f9c", cat_dark="#676b77", belly="#efece7", cat_eye="#2b211c",
        game_bg="#2a211c", game_ground="#f59e0b", sky="#fde7cf", frame="#dcc19f", night=False,
    ),
    "dark": dict(
        bg="#1f1814", ink="#f7efe6", muted="#b3a497", line="#3a2e27",
        amber="#fb923c", apricot="#fbbf24", deep="#fdba74", teal="#5fc4b8",
        desk="#2e241e", desk_edge="#3d3129",
        lid="#4a3b33", screen="#120e0b", code="#f7efe6", code_muted="#8e7f74",
        cat="#9aa0ad", cat_dark="#737885", belly="#eeeae4", cat_eye="#1f1814",
        game_bg="#120e0b", game_ground="#fbbf24", sky="#2b2240", frame="#3d3129", night=True,
    ),
}

STYLE = """
  .caret{animation:blink 1.1s steps(1) infinite}
  @keyframes blink{50%{opacity:0}}
  .type{transform-box:fill-box;transform-origin:right;animation:type 9s steps(14) infinite}
  .l2{animation-name:type2}.l3{animation-name:type3}.l4{animation-name:type4}.l5{animation-name:type5}
  @keyframes type {0%{transform:scaleX(1)}7%,92%{transform:scaleX(0)}100%{transform:scaleX(1)}}
  @keyframes type2{0%,7%{transform:scaleX(1)}20%,92%{transform:scaleX(0)}100%{transform:scaleX(1)}}
  @keyframes type3{0%,20%{transform:scaleX(1)}31%,92%{transform:scaleX(0)}100%{transform:scaleX(1)}}
  @keyframes type4{0%,31%{transform:scaleX(1)}40%,92%{transform:scaleX(0)}100%{transform:scaleX(1)}}
  @keyframes type5{0%,40%{transform:scaleX(1)}43%,92%{transform:scaleX(0)}100%{transform:scaleX(1)}}
  .scroll{animation:scroll 2.4s linear infinite}
  @keyframes scroll{from{transform:translateX(0)}to{transform:translateX(-220px)}}
  .scroll-slow{animation:scroll 9.6s linear infinite}
  .hero{animation:jump 2.4s infinite}
  @keyframes jump{0%,58%,90%,100%{transform:translateY(0);animation-timing-function:ease-out}
    74%{transform:translateY(-40px);animation-timing-function:ease-in}}
  .press{animation:press 2.4s infinite}
  @keyframes press{0%,54%,66%,100%{transform:translateY(0)}57%,62%{transform:translateY(2.5px)}}
  .btn{animation:btn 2.4s steps(1) infinite}
  @keyframes btn{0%,56%,66%,100%{opacity:0}57%{opacity:1}}
  .score{animation:blink 2.4s steps(1) infinite}
  .tail{transform-origin:1140px 286px;animation:tail 2.8s ease-in-out infinite}
  @keyframes tail{0%,100%{transform:rotate(0)}50%{transform:rotate(-12deg)}}
  .blink{transform-box:fill-box;transform-origin:center;animation:eyes 5s infinite}
  @keyframes eyes{0%,94%,100%{transform:scaleY(1)}96%{transform:scaleY(.1)}}
  .twinkle{animation:twinkle 3s ease-in-out infinite}
  .twinkle.t2{animation-delay:-1s}.twinkle.t3{animation-delay:-2s}
  @keyframes twinkle{0%,100%{opacity:.25}50%{opacity:1}}
  @media (prefers-reduced-motion:reduce){*{animation:none!important}.type{transform:scaleX(0)}.btn{opacity:0}}
"""


def window(t):
    x, y = 668, 34
    parts = [f'<rect x="{x}" y="{y}" width="92" height="84" rx="8" fill="{t["sky"]}" stroke="{t["frame"]}" stroke-width="5"/>']
    if t["night"]:
        parts += [
            f'<circle cx="{x + 62}" cy="{y + 30}" r="15" fill="{t["apricot"]}"/>',
            f'<circle cx="{x + 70}" cy="{y + 24}" r="13" fill="{t["sky"]}"/>',
            f'<circle class="twinkle" cx="{x + 20}" cy="{y + 22}" r="2" fill="{t["ink"]}"/>',
            f'<circle class="twinkle t2" cx="{x + 34}" cy="{y + 60}" r="1.6" fill="{t["ink"]}"/>',
            f'<circle class="twinkle t3" cx="{x + 74}" cy="{y + 66}" r="1.8" fill="{t["ink"]}"/>',
        ]
    else:
        parts += [
            f'<circle cx="{x + 58}" cy="{y + 32}" r="15" fill="{t["apricot"]}"/>',
            f'<rect x="{x + 10}" y="{y + 56}" width="34" height="10" rx="5" fill="#ffffff" opacity=".95"/>',
            f'<rect x="{x + 20}" y="{y + 50}" width="18" height="10" rx="5" fill="#ffffff" opacity=".95"/>',
        ]
    parts += [
        f'<line x1="{x + 46}" y1="{y}" x2="{x + 46}" y2="{y + 84}" stroke="{t["frame"]}" stroke-width="4"/>',
        f'<line x1="{x}" y1="{y + 42}" x2="{x + 92}" y2="{y + 42}" stroke="{t["frame"]}" stroke-width="4"/>',
    ]
    return "\n  ".join(parts)


def laptop(t):
    c = t
    lines = [
        (176, [("const", c["amber"]), (" suhail = {", c["code"])]),
        (194, [("  sees: ", c["code"]), ('"pixels"', c["teal"]), (",", c["code"])]),
        (212, [("  plays: ", c["code"]), ('"games"', c["teal"]), (",", c["code"])]),
        (230, [("  coop: ", c["code"]), ('"the cat"', c["teal"]), (",", c["code"])]),
        (248, [("};", c["code"])]),
    ]
    widths = [140, 110, 110, 124, 16]
    out = [
        f'<rect x="584" y="146" width="256" height="140" rx="10" fill="{c["lid"]}"/>',
        f'<rect x="594" y="156" width="236" height="118" rx="4" fill="{c["screen"]}"/>',
    ]
    for i, ((y, spans), w) in enumerate(zip(lines, widths), start=1):
        tsp = "".join(f'<tspan fill="{col}">{txt}</tspan>' for txt, col in spans)
        out.append(f'<text x="606" y="{y}" font-family="{MONO}" font-size="10.5" xml:space="preserve">{tsp}</text>')
        out.append(f'<rect class="type l{i}" x="604" y="{y - 11}" width="{w}" height="15" fill="{c["screen"]}"/>')
    out.append(f'<text x="606" y="266" font-family="{MONO}" font-size="10.5" fill="{c["code_muted"]}">// one more level<tspan class="caret" fill="{c["amber"]}">▍</tspan></text>')
    out.append(f'<path d="M570 286 H854 L846 296 H578 Z" fill="{c["lid"]}"/>')
    out.append(f'<rect x="688" y="286" width="48" height="4" rx="2" fill="{c["screen"]}"/>')
    return "\n  ".join(out)


def pixel_cat(x, y, body, ear, eye, u=1.5):
    """A pixel-art cat (14x12 grid units of size u), top-left at (x, y)."""
    def px(gx, gy, w, h, fill):
        return f'<rect x="{x + gx * u}" y="{y + gy * u}" width="{w * u}" height="{h * u}" fill="{fill}"/>'
    return (px(0, 3, 14, 9, body) + px(0, 0, 3, 3, ear) + px(11, 0, 3, 3, ear)
            + px(9, 5, 2, 2, eye) + px(-4, 4, 4, 2, body) + px(2, 12, 2, 2, body) + px(10, 12, 2, 2, body))


def monitor(t):
    c = t
    sx, sy, sw, sh = 876, 128, 184, 108     # screen
    ground = sy + sh - 16
    crates, coins = [], []
    # two copies 220px apart so the scroll loops seamlessly
    for k in (0, 220):
        bx = sx + sw + 10 + k
        crates.append(f'<rect x="{bx}" y="{ground - 18}" width="18" height="18" fill="{c["amber"]}"/>'
                      f'<path d="M{bx} {ground - 18} l18 18 M{bx + 18} {ground - 18} l-18 18" stroke="{c["deep"]}" stroke-width="2"/>'
                      f'<rect x="{bx}" y="{ground - 18}" width="18" height="18" fill="none" stroke="{c["deep"]}" stroke-width="2"/>')
        for i, cx in enumerate((bx - 70, bx - 52)):
            coins.append(f'<rect x="{cx}" y="{ground - 44 - 8 * i}" width="7" height="7" fill="{c["apricot"]}"/>')
    clouds = []
    for k in (0, 220):
        for cx, cy in ((sx + 30 + k, sy + 26), (sx + 130 + k, sy + 18)):
            clouds.append(f'<rect x="{cx}" y="{cy}" width="18" height="4" fill="{c["muted"]}" opacity=".45"/>'
                          f'<rect x="{cx + 4}" y="{cy - 4}" width="10" height="4" fill="{c["muted"]}" opacity=".45"/>')
    hills = []
    for k in (0, 220):
        for hx, hw, hh in ((sx + 10 + k, 60, 22), (sx + 90 + k, 80, 34), (sx + 175 + k, 40, 16)):
            for step in range(0, hh, 6):
                hills.append(f'<rect x="{hx + step}" y="{ground - 6 - step}" width="{hw - 2 * step}" height="6" fill="{c["deep"]}" opacity=".35"/>')
    ground_ticks = "".join(f'<rect x="{sx + k}" y="{ground + 5}" width="6" height="2" fill="{c["deep"]}" opacity=".7"/>'
                           for k in range(0, 440, 22))
    return "\n  ".join([
        # stand
        f'<rect x="{sx + sw / 2 - 9}" y="{sy + sh + 10}" width="18" height="40" fill="{c["lid"]}"/>',
        f'<rect x="{sx + sw / 2 - 36}" y="290" width="72" height="7" rx="3" fill="{c["lid"]}"/>',
        # bezel + screen
        f'<rect x="{sx - 10}" y="{sy - 10}" width="{sw + 20}" height="{sh + 20}" rx="10" fill="{c["lid"]}"/>',
        f'<clipPath id="gamescreen"><rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="3"/></clipPath>',
        f'<g clip-path="url(#gamescreen)">',
        f'  <rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" fill="{c["game_bg"]}"/>',
        f'  <g class="scroll-slow">{"".join(clouds)}{"".join(hills)}</g>',
        f'  <rect x="{sx}" y="{ground}" width="{sw}" height="{sh}" fill="{c["deep"]}" opacity=".3"/>',
        f'  <rect x="{sx}" y="{ground}" width="{sw}" height="3" fill="{c["game_ground"]}"/>',
        f'  <g class="scroll">{ground_ticks}{"".join(coins)}{"".join(crates)}</g>',
        f'  <g class="hero">{pixel_cat(sx + 34, ground - 21, c["cat"], c["cat"], c["game_bg"])}</g>',
        f'  <text x="{sx + 8}" y="{sy + 14}" font-family="{MONO}" font-size="9" fill="{c["code"]}">SCORE 04210</text>',
        f'  <text x="{sx + sw - 8}" y="{sy + 14}" text-anchor="end" font-family="{MONO}" font-size="9" fill="{c["apricot"]}">♥♥♥</text>',
        f'</g>',
        f'<circle cx="{sx + sw - 4}" cy="{sy + sh + 5}" r="2" fill="{c["teal"]}"/>',
    ])


def cat_and_pad(t):
    c = t
    cx = 1112
    return "\n  ".join([
        # cable from gamepad to monitor
        f'<path d="M1060 284 C1050 300 1010 300 984 290" fill="none" stroke="{c["lid"]}" stroke-width="2.5"/>',
        # tail
        f'<path class="tail" d="M1140 286 C1180 286 1186 246 1166 222" fill="none" stroke="{c["cat"]}" stroke-width="11" stroke-linecap="round"/>',
        # body
        f'<ellipse cx="{cx}" cy="250" rx="38" ry="46" fill="{c["cat"]}"/>',
        f'<ellipse cx="{cx}" cy="262" rx="18" ry="26" fill="{c["belly"]}"/>',
        f'<path d="M{cx + 20} 226 q8 3 14 -1 M{cx + 22} 242 q8 3 14 -1" fill="none" stroke="{c["cat_dark"]}" stroke-width="4" stroke-linecap="round"/>',
        # head
        f'<path d="M{cx - 24} 176 L{cx - 30} 140 L{cx - 4} 162 Z" fill="{c["cat"]}"/>',
        f'<path d="M{cx + 24} 176 L{cx + 30} 140 L{cx + 4} 162 Z" fill="{c["cat"]}"/>',
        f'<path d="M{cx - 23} 170 L{cx - 26} 150 L{cx - 11} 163 Z" fill="{c["amber"]}" opacity=".55"/>',
        f'<path d="M{cx + 23} 170 L{cx + 26} 150 L{cx + 11} 163 Z" fill="{c["amber"]}" opacity=".55"/>',
        f'<circle cx="{cx}" cy="190" r="31" fill="{c["cat"]}"/>',
        f'<path d="M{cx - 8} 163 v9 M{cx} 161 v10 M{cx + 8} 163 v9" stroke="{c["cat_dark"]}" stroke-width="3.5" stroke-linecap="round"/>',
        # eyes look left at the screen
        f'<ellipse cx="{cx - 11}" cy="190" rx="5.5" ry="6" fill="{c["belly"]}"/>',
        f'<ellipse cx="{cx + 11}" cy="190" rx="5.5" ry="6" fill="{c["belly"]}"/>',
        f'<ellipse class="blink" cx="{cx - 14}" cy="190" rx="3" ry="4.5" fill="{c["cat_eye"]}"/>',
        f'<ellipse class="blink" cx="{cx + 8}" cy="190" rx="3" ry="4.5" fill="{c["cat_eye"]}"/>',
        f'<path d="M{cx - 4} 200 h8 l-4 5 z" fill="{c["amber"]}"/>',
        f'<path d="M{cx} 205 q-4 5 -9 3 M{cx} 205 q4 5 9 3" fill="none" stroke="{c["cat_eye"]}" stroke-width="1.6" stroke-linecap="round"/>',
        f'<path d="M{cx - 20} 200 h-20 M{cx - 20} 205 l-18 4 M{cx + 20} 200 h20 M{cx + 20} 205 l18 4" stroke="{c["cat_eye"]}" stroke-width="1.3" stroke-linecap="round" opacity=".6"/>',
        # gamepad on the desk
        f'<rect x="1046" y="270" width="70" height="24" rx="12" fill="{c["lid"]}"/>',
        f'<path d="M1060 278 v8 M1056 282 h8" stroke="{c["code"]}" stroke-width="3" stroke-linecap="round"/>',
        f'<circle cx="1098" cy="279" r="3.2" fill="{c["teal"]}"/>',
        f'<circle cx="1105" cy="285" r="3.2" fill="{c["amber"]}"/>',
        f'<circle class="btn" cx="1105" cy="285" r="6" fill="none" stroke="{c["apricot"]}" stroke-width="2"/>',
        # paws on the pad: right paw presses jump in sync with the game
        f'<ellipse cx="1068" cy="270" rx="10" ry="7" fill="{c["cat"]}"/>',
        f'<g class="press"><ellipse cx="1102" cy="270" rx="10" ry="7" fill="{c["cat"]}"/>'
        f'<path d="M1096 271 v3 M1102 272 v3 M1108 271 v3" stroke="{c["cat_dark"]}" stroke-width="1.5" stroke-linecap="round"/></g>',
    ])


def banner(name, t):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="340" viewBox="0 0 1200 340" role="img" aria-labelledby="t d">
<title id="t">Suhail: code, games and a cat on co-op</title>
<desc id="d">A desk scene: a laptop with code, and a grey cat at a gamepad playing a pixel endless-runner on a monitor.</desc>
<style>{STYLE}</style>
<defs><clipPath id="frame"><rect x="1" y="1" width="1198" height="338" rx="22"/></clipPath></defs>
<g clip-path="url(#frame)">
  <rect width="1200" height="340" fill="{t['bg']}"/>
  {window(t)}
  <rect x="566" y="300" width="16" height="44" fill="{t['desk_edge']}"/>
  <rect x="524" y="296" width="700" height="18" rx="9" fill="{t['desk']}"/>
  <rect x="524" y="309" width="700" height="5" fill="{t['desk_edge']}"/>
</g>
<rect x="1" y="1" width="1198" height="338" rx="22" fill="none" stroke="{t['line']}" stroke-width="1.5"/>

<text x="64" y="96" font-family="{MONO}" font-size="16" fill="{t['muted']}">&gt; player one, ready. i'm<tspan class="caret" fill="{t['amber']}"> ▍</tspan></text>
<text x="60" y="172" font-family="{SANS}" font-size="76" font-weight="800" letter-spacing="-2" fill="{t['ink']}">Suhail<tspan fill="{t['amber']}">.</tspan></text>
<g fill="{t['apricot']}"><rect x="66" y="186" width="10" height="10"/><rect x="82" y="186" width="10" height="10"/><rect x="98" y="186" width="10" height="10"/><rect x="114" y="186" width="10" height="10" fill="{t['amber']}"/></g>
<text x="64" y="232" font-family="{SANS}" font-size="22" fill="{t['ink']}">I build systems that learn to <tspan font-style="italic" fill="{t['amber']}">see</tspan>.</text>
<text x="64" y="270" font-family="{MONO}" font-size="15" fill="{t['muted']}">CS undergrad  ·  VIT Bhopal  ·  CV + core systems</text>
<text x="64" y="300" font-family="{SANS}" font-size="15" font-style="italic" fill="{t['muted']}">code by day, games by night, and a cat on co-op</text>

<g>
  {laptop(t)}
  {monitor(t)}
  {cat_and_pad(t)}
</g>
</svg>
"""
    (OUT / name).write_text(svg)


if __name__ == "__main__":
    banner("banner-light.svg", THEMES["light"])
    banner("banner-dark.svg", THEMES["dark"])
    print("wrote", OUT / "banner-light.svg", OUT / "banner-dark.svg")
