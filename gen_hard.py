#!/usr/bin/env python3
"""gen_hard.py — Ul'dah / Thanalan graphic-recording style (hand-drawn sketch on cream paper)."""
import re, math, random

random.seed(44)

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── Wobble helpers ──────────────────────────────────────────────────────
def wobble_path(points, closed=False):
    if len(points) < 2:
        return ''
    segs = [f'M{points[0][0]:.1f},{points[0][1]:.1f}']
    for i in range(1, len(points)):
        x0, y0 = points[i-1]
        x1, y1 = points[i]
        mx = (x0 + x1) / 2 + random.uniform(-1.5, 1.5)
        my = (y0 + y1) / 2 + random.uniform(-1.5, 1.5)
        segs.append(f'Q{mx:.1f},{my:.1f} {x1:.1f},{y1:.1f}')
    if closed:
        x0, y0 = points[-1]
        x1, y1 = points[0]
        mx = (x0 + x1) / 2 + random.uniform(-1.5, 1.5)
        my = (y0 + y1) / 2 + random.uniform(-1.5, 1.5)
        segs.append(f'Q{mx:.1f},{my:.1f} {x1:.1f},{y1:.1f}')
        segs.append('Z')
    return ' '.join(segs)

def dome(cx, cy, rx, ry):
    """Simple semicircle dome."""
    return f'M{cx-rx},{cy} Q{cx-rx},{cy-ry*1.6} {cx},{cy-ry} Q{cx+rx},{cy-ry*1.6} {cx+rx},{cy}'

# ── Build SVG ───────────────────────────────────────────────────────────
P = []
A = P.append

W, H = 400, 600
PAPER = '#F2ECE0'     # cream with amber tint
PAPER2 = '#EDE4D0'    # warm sandy wash
OUTLINE = '#2A2A2A'
SW = 2.5
SW_BOLD = 3.5

A(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">')

# ── Paper background ──
A(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
# Warm sandy wash in lower area
A(f'<rect y="320" width="{W}" height="{H-320}" fill="{PAPER2}" opacity="0.5"/>')

# ── Desert ground line ──
ground_y = 400
gnd_pts = [(0, ground_y)]
for x in range(25, W+1, 25):
    gnd_pts.append((x, ground_y + random.uniform(-2, 2)))
A(f'<path d="{wobble_path(gnd_pts)}" stroke="#C8A060" stroke-width="1.5" fill="none" opacity="0.5"/>')
# Sand fill below
A(f'<rect y="{ground_y}" width="{W}" height="{H-ground_y}" fill="#E8D8B8" opacity="0.3"/>')

# ── Left mesa (burnt orange angular cliff) ──
mesa_l = [(0, 180), (0, 60), (30, 45), (65, 55), (80, 75), (90, 180)]
A(f'<path d="{wobble_path(mesa_l, True)}" fill="#D07030" stroke="{OUTLINE}" stroke-width="{SW_BOLD}" opacity="0.75"/>')
# Strata bands
for sy in range(60, 170, 22):
    A(f'<line x1="5" y1="{sy}" x2="{70+random.randint(-8,8)}" y2="{sy+random.randint(-2,2)}" '
      f'stroke="#B05820" stroke-width="1" opacity="0.35"/>')

# ── Right mesa ──
mesa_r = [(W, 160), (W, 75), (365, 55), (340, 65), (320, 85), (310, 160)]
A(f'<path d="{wobble_path(mesa_r, True)}" fill="#D07030" stroke="{OUTLINE}" stroke-width="{SW_BOLD}" opacity="0.75"/>')
for sy in range(70, 150, 22):
    A(f'<line x1="{W-5}" y1="{sy}" x2="{335+random.randint(-8,8)}" y2="{sy+random.randint(-2,2)}" '
      f'stroke="#B05820" stroke-width="1" opacity="0.35"/>')

# ── Teal dome (Ul'dah signature, upper center-left) ──
A(f'<path d="{dome(140, 130, 30, 25)}" fill="#48A8A0" stroke="{OUTLINE}" stroke-width="{SW}" opacity="0.7"/>')
# Base rectangle
A(f'<path d="{wobble_path([(110, 130), (110, 160), (170, 160), (170, 130)])}" '
  f'fill="#E8D8B0" stroke="{OUTLINE}" stroke-width="1.8" opacity="0.6"/>')
# Window
A(f'<path d="M135,138 Q140,133 145,138 L145,150 L135,150 Z" fill="#48A8A0" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.5"/>')

# ── Smaller dome (right side) ──
A(f'<path d="{dome(300, 110, 20, 16)}" fill="#48A8A0" stroke="{OUTLINE}" stroke-width="2" opacity="0.55"/>')
A(f'<path d="{wobble_path([(280, 110), (280, 135), (320, 135), (320, 110)])}" '
  f'fill="#E8D8B0" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.5"/>')

# ── Left minaret ──
mn_x = 70
A(f'<path d="{wobble_path([(mn_x-5, 180), (mn_x-4, 50), (mn_x+4, 50), (mn_x+5, 180)])}" '
  f'fill="#E8D8B0" stroke="{OUTLINE}" stroke-width="{SW}" opacity="0.7"/>')
# Pointed cap
A(f'<path d="M{mn_x-6},{50} L{mn_x},{35} L{mn_x+6},{50}" fill="#D8A830" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.7"/>')
# Balcony band
A(f'<line x1="{mn_x-7}" y1="75" x2="{mn_x+7}" y2="75" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.5"/>')

# ── Right minaret ──
mn_x2 = 345
A(f'<path d="{wobble_path([(mn_x2-4, 160), (mn_x2-3, 60), (mn_x2+3, 60), (mn_x2+4, 160)])}" '
  f'fill="#E8D8B0" stroke="{OUTLINE}" stroke-width="2" opacity="0.6"/>')
A(f'<path d="M{mn_x2-5},{60} L{mn_x2},{47} L{mn_x2+5},{60}" fill="#D8A830" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.6"/>')

# ── Gold standard/flag on left minaret ──
A(f'<line x1="{mn_x}" y1="35" x2="{mn_x}" y2="22" stroke="#C8A030" stroke-width="1.2" opacity="0.6"/>')
A(f'<path d="M{mn_x},{22} L{mn_x+9},{26} L{mn_x},{30}" fill="#D8A830" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.55"/>')

# ── Ancient ruins (desert floor, left) ──
# Fallen column
A(f'<path d="{wobble_path([(15, ground_y-2), (15, ground_y-8), (55, ground_y-10), (55, ground_y-4)])}" '
  f'fill="#D8C8A0" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.4"/>')
# Column drum
A(f'<ellipse cx="60" cy="{ground_y-7}" rx="5" ry="7" fill="#D8C8A0" stroke="{OUTLINE}" stroke-width="1" opacity="0.4"/>')

# ── Broken arch (right side) ──
A(f'<path d="M330,{ground_y-5} L330,{ground_y-35} Q345,{ground_y-48} 360,{ground_y-35}" '
  f'stroke="{OUTLINE}" stroke-width="2" fill="none" opacity="0.35"/>')
A(f'<line x1="360" y1="{ground_y-35}" x2="360" y2="{ground_y-18}" stroke="{OUTLINE}" stroke-width="2" opacity="0.3"/>')

# ── Eternal flame (center-ish, iconic Ul'dah element) ──
fl_x, fl_y = 200, 190
# Pedestal
A(f'<path d="{wobble_path([(fl_x-8, 210), (fl_x-6, 195), (fl_x+6, 195), (fl_x+8, 210)])}" '
  f'fill="#C8B888" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.6"/>')
# Flame (teardrop)
A(f'<path d="M{fl_x},{fl_y-18} Q{fl_x+10},{fl_y-5} {fl_x},{fl_y+2} Q{fl_x-10},{fl_y-5} {fl_x},{fl_y-18}" '
  f'fill="#E88030" stroke="{OUTLINE}" stroke-width="1.8" opacity="0.7"/>')
# Inner flame
A(f'<path d="M{fl_x},{fl_y-12} Q{fl_x+5},{fl_y-4} {fl_x},{fl_y} Q{fl_x-5},{fl_y-4} {fl_x},{fl_y-12}" '
  f'fill="#F0C040" stroke="none" opacity="0.6"/>')

# ── Desert scrub (sparse vegetation doodles) ──
for (sx, sy) in [(25, ground_y-3), (95, ground_y-1), (310, ground_y-2), (380, ground_y-4)]:
    bw = random.uniform(5, 9)
    A(f'<path d="M{sx-bw},{sy} Q{sx-bw/2},{sy-8} {sx},{sy-2} Q{sx+bw/2},{sy-8} {sx+bw},{sy}" '
      f'stroke="#8B9848" stroke-width="1.5" fill="none" opacity="0.4"/>')

# ── Sand dune ripples (subtle, lower area) ──
for dy in range(ground_y + 10, ground_y + 50, 15):
    pts = [(x, dy + random.uniform(-1.5, 1.5)) for x in range(0, W+1, 30)]
    A(f'<path d="{wobble_path(pts)}" stroke="#D0B880" stroke-width="0.8" fill="none" opacity="0.25"/>')

# ── Cracked earth texture (subtle) ──
for _ in range(5):
    cx = random.randint(100, 300)
    cy = random.randint(ground_y + 5, ground_y + 40)
    A(f'<path d="M{cx},{cy} L{cx+random.randint(-12,12)},{cy+random.randint(-8,8)}" '
      f'stroke="#B8A070" stroke-width="0.7" fill="none" opacity="0.2"/>')

# ── Small sun doodle (upper right) ──
sun_x, sun_y = 340, 25
A(f'<circle cx="{sun_x}" cy="{sun_y}" r="10" fill="#F0C840" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.4"/>')
for angle in range(0, 360, 45):
    rad = math.radians(angle)
    x1 = sun_x + 13 * math.cos(rad)
    y1 = sun_y + 13 * math.sin(rad)
    x2 = sun_x + 18 * math.cos(rad)
    y2 = sun_y + 18 * math.sin(rad)
    A(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
      f'stroke="#F0C840" stroke-width="1.2" stroke-linecap="round" opacity="0.35"/>')

# ── Bird silhouettes ──
for (bx, by) in [(120, 30), (230, 20), (290, 35)]:
    bw = random.uniform(6, 9)
    A(f'<path d="M{bx-bw},{by+2} Q{bx},{by-2} {bx+bw},{by+2}" '
      f'stroke="{OUTLINE}" stroke-width="1.2" fill="none" opacity="0.3"/>')

A('</svg>')

HARD = ''.join(P)

# ── Inject into stage.html ───────────────────────────────────────────────
pattern = r"(if\(diff==='HARD'\) return ')(.*?)(';)"
replacement = r"\g<1>" + HARD.replace('\\', '\\\\') + r"\g<3>"
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

assert new_content != content, "Injection failed — pattern not matched"
print(f"HARD SVG: {len(HARD):,} chars injected OK")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("stage.html written.")
