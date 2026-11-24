"""Generate project cover SVGs in the banner's flat palette (no gradients).

Writes assets/{slidesnap,ccrm,ossaudit}-{light,dark}.svg.
Colours come from tools/make_banner.py so covers always match the banner.

Run from the repo root:  python3 tools/make_covers.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_banner import MONO, OUT, SANS, THEMES  # noqa: E402

GRID = {"light": "#f3e8da", "dark": "#2a211c"}

STYLE = """
  .grow{transform-box:fill-box;transform-origin:left;animation:grow 4s ease-in-out infinite}
  .grow.d1{animation-delay:-.6s}.grow.d2{animation-delay:-1.2s}.grow.d3{animation-delay:-1.8s}
  @keyframes grow{0%,100%{transform:scaleX(.3)}50%{transform:scaleX(1)}}
  .caret{animation:blink 1.1s steps(1) infinite}
  @keyframes blink{50%{opacity:0}}
  .play{animation:play 6s linear infinite}
  @keyframes play{from{transform:translateX(0)}to{transform:translateX(250px)}}
  .flash{animation:flash 6s steps(1) infinite;opacity:0}
  .flash.f2{animation-delay:-4s}.flash.f3{animation-delay:-2s}
  @keyframes flash{0%{opacity:1}12%,100%{opacity:0}}
  .pulse{animation:pulse 2.4s ease-in-out infinite}
  @keyframes pulse{0%,100%{opacity:.35}50%{opacity:1}}
  @media (prefers-reduced-motion:reduce){*{animation:none!important}.flash{opacity:0}}
"""


def shell(t, mode, title, kicker, sub, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="640" height="360" viewBox="0 0 640 360" role="img" aria-label="{title}: {sub}">
<style>{STYLE}</style>
<defs><pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="{GRID[mode]}" stroke-width="1"/></pattern></defs>
<rect width="640" height="360" rx="14" fill="{t['bg']}"/>
<rect width="640" height="360" rx="14" fill="url(#grid)"/>
<text x="36" y="44" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{t['amber']}">{kicker}</text>
<text x="34" y="86" font-family="{SANS}" font-size="38" font-weight="800" letter-spacing="-1" fill="{t['ink']}">{title}<tspan fill="{t['amber']}">.</tspan></text>
<text x="36" y="112" font-family="{MONO}" font-size="13" fill="{t['muted']}">{sub}</text>
{body}
<rect x=".75" y=".75" width="638.5" height="358.5" rx="14" fill="none" stroke="{t['line']}" stroke-width="1.5"/>
</svg>
"""


def window_chrome(t, x, y, w, h, title=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{t["screen"]}" stroke="{t["lid"]}" stroke-width="2"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="24" rx="10" fill="{t["lid"]}"/>'
            f'<rect x="{x}" y="{y + 14}" width="{w}" height="10" fill="{t["lid"]}"/>'
            f'<circle cx="{x + 16}" cy="{y + 12}" r="4" fill="{t["amber"]}"/>'
            f'<circle cx="{x + 30}" cy="{y + 12}" r="4" fill="{t["apricot"]}"/>'
            f'<circle cx="{x + 44}" cy="{y + 12}" r="4" fill="{t["teal"]}"/>'
            f'<text x="{x + w / 2}" y="{y + 16}" text-anchor="middle" font-family="{MONO}" font-size="10" fill="{t["code_muted"]}">{title}</text>')


def slidesnap(mode):
    t = THEMES[mode]
    # tilted projector screen inside a video frame
    vx, vy, vw, vh = 36, 138, 250, 150
    body = [
        f'<rect x="{vx}" y="{vy}" width="{vw}" height="{vh}" rx="8" fill="{t["screen"]}"/>',
        # skewed slide on the wall (camera tilt)
        f'<polygon points="{vx + 38},{vy + 22} {vx + 214},{vy + 14} {vx + 222},{vy + 112} {vx + 30},{vy + 118}" fill="{t["bg"]}" opacity=".92"/>',
        f'<polygon points="{vx + 38},{vy + 22} {vx + 214},{vy + 14} {vx + 222},{vy + 112} {vx + 30},{vy + 118}" fill="none" stroke="{t["amber"]}" stroke-width="2" stroke-dasharray="5 4"/>',
    ]
    for i, (w, col) in enumerate(((110, t["ink"]), (140, t["muted"]), (120, t["muted"]), (90, t["muted"]))):
        y0 = vy + 36 + i * 18
        body.append(f'<rect x="{vx + 52}" y="{y0}" width="{w}" height="{9 if i == 0 else 6}" rx="3" fill="{col}" opacity="{1 if i == 0 else .6}" transform="rotate(-2.5 {vx + 52} {y0})"/>')
    for cx, cy in ((vx + 38, vy + 22), (vx + 214, vy + 14), (vx + 222, vy + 112), (vx + 30, vy + 118)):
        body.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{t["amber"]}"/>')
    # presenter silhouette
    body.append(f'<circle cx="{vx + 228}" cy="{vy + 86}" r="11" fill="{t["lid"]}"/><path d="M{vx + 208} {vy + vh} q0 -44 20 -44 q20 0 20 44 z" fill="{t["lid"]}"/>')
    # timeline with slide cuts + playhead
    ty = vy + vh + 22
    body.append(f'<rect x="{vx}" y="{ty}" width="{vw}" height="6" rx="3" fill="{t["line"]}"/>')
    for k, cut in enumerate((60, 140, 205)):
        body.append(f'<rect x="{vx + cut - 1}" y="{ty - 6}" width="3" height="18" rx="1.5" fill="{t["teal"]}"/>')
        body.append(f'<rect class="flash f{k + 1}" x="{vx + cut - 5}" y="{ty - 10}" width="11" height="26" rx="4" fill="none" stroke="{t["apricot"]}" stroke-width="2"/>')
    body.append(f'<g class="play"><rect x="{vx - 2}" y="{ty - 8}" width="4" height="22" rx="2" fill="{t["amber"]}"/></g>')
    body.append(f'<text x="{vx}" y="{ty + 28}" font-family="{MONO}" font-size="10.5" fill="{t["muted"]}">SSIM + frame diff → slide cuts</text>')
    # arrow
    body.append(f'<path d="M304 214 h56 m-9 -8 l9 8 l-9 8" fill="none" stroke="{t["teal"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    body.append(f'<text x="332" y="202" text-anchor="middle" font-family="{MONO}" font-size="10.5" fill="{t["muted"]}">rectify</text>')
    body.append(f'<text x="332" y="240" text-anchor="middle" font-family="{MONO}" font-size="10.5" fill="{t["muted"]}">+ OCR</text>')
    # output stack: PDF + PPTX pages
    for i, (label, col) in enumerate((("PPTX", t["apricot"]), ("PDF", t["amber"]))):
        px, py = 392 + i * 26, 140 + i * 22
        body.append(f'<rect x="{px}" y="{py}" width="196" height="128" rx="8" fill="{t["bg"]}" stroke="{t["lid"]}" stroke-width="2"/>')
        body.append(f'<rect x="{px + 14}" y="{py + 16}" width="96" height="9" rx="3" fill="{t["ink"]}"/>')
        for j, w in enumerate((150, 128, 140, 100)):
            body.append(f'<rect x="{px + 14}" y="{py + 36 + j * 16}" width="{w}" height="6" rx="3" fill="{t["muted"]}" opacity=".55"/>')
        body.append(f'<rect x="{px + 150}" y="{py + 10}" width="38" height="18" rx="9" fill="{col}"/>')
        body.append(f'<text x="{px + 169}" y="{py + 23}" text-anchor="middle" font-family="{MONO}" font-size="10" font-weight="700" fill="{t["bg"]}">{label}</text>')
    # highlighted "searchable" word on the PDF page
    body.append(f'<rect class="pulse" x="432" y="196" width="60" height="12" rx="3" fill="{t["apricot"]}" opacity=".6"/>')
    body.append(f'<text x="392" y="318" font-family="{MONO}" font-size="10.5" fill="{t["muted"]}">searchable · bookmarked · editable</text>')
    svg = shell(t, mode, "SlideSnap", "COMPUTER VISION · PYTHON",
                "lecture video → searchable slide PDF &amp; PPTX", "\n".join(body))
    (OUT / f"slidesnap-{mode}.svg").write_text(svg)


def ccrm(mode):
    t = THEMES[mode]
    x, y, w, h = 36, 132, 300, 200
    menu = [("=== CCRM ===", t["apricot"]), ("1. Manage Students", t["code"]), ("2. Manage Courses", t["code"]),
            ("3. Enrollment &amp; Grades", t["code"]), ("4. Import / Export CSV", t["code"]),
            ("5. Transcripts &amp; Reports", t["code"]), ("0. Exit", t["code_muted"])]
    body = [window_chrome(t, x, y, w, h, "edu.ccrm.cli.Main")]
    for i, (line, col) in enumerate(menu):
        body.append(f'<text x="{x + 16}" y="{y + 48 + i * 19}" font-family="{MONO}" font-size="11.5" fill="{col}">{line}</text>')
    body.append(f'<rect x="{x + 10}" y="{y + 92}" width="{w - 20}" height="19" rx="3" fill="{t["amber"]}" opacity=".22"/>')
    body.append(f'<text x="{x + 16}" y="{y + 186}" font-family="{MONO}" font-size="11.5" fill="{t["teal"]}">ccrm&gt; 3<tspan class="caret" fill="{t["amber"]}">▍</tspan></text>')

    # mini class diagram
    def box(bx, by, name, sub=None, accent=False):
        bw = 116
        hh = 40 if sub else 28
        out = [f'<rect x="{bx}" y="{by}" width="{bw}" height="{hh}" rx="6" fill="{t["bg"]}" stroke="{t["amber"] if accent else t["lid"]}" stroke-width="2"/>',
               f'<text x="{bx + bw / 2}" y="{by + 18}" text-anchor="middle" font-family="{MONO}" font-size="11.5" font-weight="700" fill="{t["ink"]}">{name}</text>']
        if sub:
            out.append(f'<text x="{bx + bw / 2}" y="{by + 32}" text-anchor="middle" font-family="{MONO}" font-size="9.5" font-style="italic" fill="{t["muted"]}">{sub}</text>')
        return "".join(out)

    body += [
        box(432, 132, "Person", "«abstract»", accent=True),
        box(366, 214, "Student"), box(500, 214, "Instructor"),
        f'<path d="M424 214 V194 H558 V214 M490 194 V182" fill="none" stroke="{t["lid"]}" stroke-width="2"/>',
        f'<path d="M482 182 l8 -10 l8 10 z" fill="{t["bg"]}" stroke="{t["lid"]}" stroke-width="2"/>',
        box(366, 290, "Enrollment"), box(500, 290, "Course"),
        f'<path d="M424 242 V290" stroke="{t["teal"]}" stroke-width="2" stroke-dasharray="4 3"/>',
        f'<path d="M482 304 H500" stroke="{t["teal"]}" stroke-width="2" stroke-dasharray="4 3"/>',
    ]
    svg = shell(t, mode, "CCRM", "JAVA · OOP", "campus course &amp; records manager", "\n".join(body))
    (OUT / f"ccrm-{mode}.svg").write_text(svg)


def ossaudit(mode):
    t = THEMES[mode]
    x, y, w, h = 36, 132, 568, 200
    body = [window_chrome(t, x, y, w, h, "bash · oss-audit")]
    lines = [
        (f'<tspan fill="{t["teal"]}">$</tspan> ./2_package_inspector.sh', None),
        (f'git <tspan fill="{t["teal"]}">✓ installed</tspan>  ·  license: <tspan fill="{t["apricot"]}">GPL v2</tspan>', None),
        (f'<tspan fill="{t["teal"]}">$</tspan> ./3_disk_auditor.sh', None),
    ]
    for i, (ln, _) in enumerate(lines):
        body.append(f'<text x="{x + 16}" y="{y + 48 + i * 20}" font-family="{MONO}" font-size="12" fill="{t["code"]}">{ln}</text>')
    bars = [("/etc", 130, ""), ("/var", 200, "d1"), ("/home", 260, "d2"), ("/usr", 320, "d3")]
    for i, (d, bw, cls) in enumerate(bars):
        by = y + 100 + i * 18
        body.append(f'<text x="{x + 16}" y="{by + 10}" font-family="{MONO}" font-size="11.5" fill="{t["code_muted"]}">{d}</text>')
        body.append(f'<rect class="grow {cls}" x="{x + 76}" y="{by}" width="{bw}" height="12" rx="3" fill="{t["amber"] if i % 2 else t["apricot"]}"/>')
    body.append(f'<text x="{x + 16}" y="{y + h - 8}" font-family="{MONO}" font-size="12" fill="{t["teal"]}">$<tspan class="caret" fill="{t["amber"]}"> ▍</tspan></text>')
    # script tabs on the right edge
    for i, name in enumerate(("1 identity", "2 packages", "3 disk", "4 logs", "5 manifesto")):
        ty = y + 36 + i * 30
        active = i == 2
        body.append(f'<rect x="{x + w - 128}" y="{ty}" width="112" height="22" rx="11" fill="{t["amber"] if active else t["lid"]}"/>')
        body.append(f'<text x="{x + w - 72}" y="{ty + 15}" text-anchor="middle" font-family="{MONO}" font-size="10.5" fill="{t["bg"] if active else t["code"]}">{name}</text>')
    svg = shell(t, mode, "OSS Audit", "SHELL · OPEN SOURCE",
                "five bash scripts auditing git (GPL v2) on Linux", "\n".join(body))
    (OUT / f"ossaudit-{mode}.svg").write_text(svg)


if __name__ == "__main__":
    for mode in ("light", "dark"):
        slidesnap(mode)
        ccrm(mode)
        ossaudit(mode)
    print("wrote covers to", OUT)
