#!/usr/bin/env python3
"""gen_extreme.py — Radz-at-Han graphic-recording style (hand-drawn sketch on cream paper)."""
import re, math, random

random.seed(45)

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

def wave_line(y, x_start, x_end, amplitude=4, freq=25):
    pts = []
    for x in range(x_start, x_end + 1, freq):
        pts.append((x, y + random.uniform(-amplitude, amplitude)))
    return wobble_path(pts)

def dome(cx, cy, rx, ry):
    return f'M{cx-rx},{cy} Q{cx-rx},{cy-ry*1.6} {cx},{cy-ry} Q{cx+rx},{cy-ry*1.6} {cx+rx},{cy}'

# ── Build SVG ───────────────────────────────────────────────────────────
P = []
A = P.append

W, H = 400, 600
PAPER = '#F2E8E6'     # cream with coral tint
OUTLINE = '#2A2A2A'
SW = 2.5
SW_BOLD = 3.5

A(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">')

# ── Paper background ──
A(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')

# ── Ocean (upper area, flat turquoise) ──
sea_y = 130
A(f'<rect width="{W}" height="{sea_y}" fill="#60C8C8" opacity="0.3"/>')
# Wave lines
for wy in range(30, sea_y, 22):
    A(f'<path d="{wave_line(wy, 0, W, 3, 18)}" stroke="#40A0B0" stroke-width="1.2" fill="none" opacity="0.25"/>')

# ── Bunting flags (top area, colorful triangles on a line — perfect for graphic recording!) ──
bunting_colors = ['#E05050', '#F0A030', '#3090E0', '#40B868', '#D060C0', '#E8C020']
# String 1 — across the top
by1 = 15
A(f'<path d="M0,{by1} Q200,{by1+8} {W},{by1}" stroke="{OUTLINE}" stroke-width="1.2" fill="none" opacity="0.4"/>')
for bx in range(15, W, 22):
    color = random.choice(bunting_colors)
    A(f'<path d="M{bx-6},{by1} L{bx},{by1+10} L{bx+6},{by1}" '
      f'fill="{color}" stroke="{OUTLINE}" stroke-width="0.7" opacity="0.55"/>')
# String 2 — slightly lower
by2 = 55
A(f'<path d="M20,{by2} Q200,{by2+10} {W-20},{by2}" stroke="{OUTLINE}" stroke-width="1" fill="none" opacity="0.3"/>')
for bx in range(30, W-20, 28):
    color = random.choice(bunting_colors)
    A(f'<path d="M{bx-5},{by2} L{bx},{by2+9} L{bx+5},{by2}" '
      f'fill="{color}" stroke="{OUTLINE}" stroke-width="0.6" opacity="0.45"/>')

# ── Left palm tree ──
palm_x, palm_y = 35, 180
# Trunk (curved)
A(f'<path d="M{palm_x},{palm_y+200} Q{palm_x-10},{palm_y+100} {palm_x+5},{palm_y}" '
  f'stroke="#8B6840" stroke-width="{SW_BOLD}" fill="none" stroke-linecap="round" opacity="0.7"/>')
# Fronds (fan shapes)
for angle in [-70, -35, 0, 35, 70]:
    rad = math.radians(angle - 90)
    fx = palm_x + 5 + 40 * math.cos(rad)
    fy = palm_y + 40 * math.sin(rad)
    A(f'<path d="M{palm_x+5},{palm_y} Q{palm_x + 20*math.cos(rad):.0f},{palm_y + 20*math.sin(rad):.0f} {fx:.0f},{fy:.0f}" '
      f'stroke="#48A048" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.6"/>')

# ── Right palm tree ──
palm_x2 = 370
A(f'<path d="M{palm_x2},{palm_y+180} Q{palm_x2+8},{palm_y+90} {palm_x2-3},{palm_y+10}" '
  f'stroke="#8B6840" stroke-width="{SW_BOLD}" fill="none" stroke-linecap="round" opacity="0.65"/>')
for angle in [-70, -35, 0, 35, 70]:
    rad = math.radians(angle - 90)
    fx = palm_x2 - 3 + 35 * math.cos(rad)
    fy = palm_y + 10 + 35 * math.sin(rad)
    A(f'<path d="M{palm_x2-3},{palm_y+10} Q{palm_x2 + 18*math.cos(rad):.0f},{palm_y + 10 + 18*math.sin(rad):.0f} {fx:.0f},{fy:.0f}" '
      f'stroke="#48A048" stroke-width="2.2" fill="none" stroke-linecap="round" opacity="0.55"/>')

# ── Market awnings (colorful flat rectangles, left and right upper area) ──
awning_colors = ['#E05050', '#F0A030', '#3090E0', '#40B868']
# Left awnings
for i, (ax, ay, aw, ah) in enumerate([(5, 150, 45, 18), (10, 200, 40, 16), (0, 250, 50, 15)]):
    color = awning_colors[i % len(awning_colors)]
    A(f'<path d="{wobble_path([(ax, ay), (ax+aw, ay-3), (ax+aw, ay+ah-3), (ax, ay+ah)])}" '
      f'fill="{color}" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.5"/>')
    # Scalloped edge
    for sx in range(ax+5, ax+aw, 8):
        A(f'<path d="M{sx},{ay+ah} Q{sx+4},{ay+ah+4} {sx+8},{ay+ah}" '
          f'stroke="{color}" stroke-width="1.2" fill="none" opacity="0.4"/>')

# Right awnings
for i, (ax, ay, aw, ah) in enumerate([(355, 160, 45, 17), (360, 215, 40, 15), (350, 265, 50, 16)]):
    color = awning_colors[(i+2) % len(awning_colors)]
    A(f'<path d="{wobble_path([(ax, ay), (ax+aw, ay-2), (ax+aw, ay+ah-2), (ax, ay+ah)])}" '
      f'fill="{color}" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.5"/>')
    for sx in range(ax+5, ax+aw, 8):
        A(f'<path d="M{sx},{ay+ah} Q{sx+4},{ay+ah+4} {sx+8},{ay+ah}" '
          f'stroke="{color}" stroke-width="1.2" fill="none" opacity="0.4"/>')

# ── Meghaduta Palace dome (upper center) ──
A(f'<path d="{dome(200, 100, 35, 28)}" fill="#3878C0" stroke="{OUTLINE}" stroke-width="{SW}" opacity="0.5"/>')
# Palace body
A(f'<path d="{wobble_path([(165, 100), (165, 135), (235, 135), (235, 100)])}" '
  f'fill="#E8D8B0" stroke="{OUTLINE}" stroke-width="1.8" opacity="0.45"/>')
# Gold finial
A(f'<circle cx="200" cy="70" r="3" fill="#D8A830" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.5"/>')
A(f'<line x1="200" y1="73" x2="200" y2="100" stroke="#D8A830" stroke-width="1.2" opacity="0.45"/>')

# ── Minaret (left of palace) ──
A(f'<path d="{wobble_path([(155, 135), (156, 65), (162, 65), (163, 135)])}" '
  f'fill="#E8D8B0" stroke="{OUTLINE}" stroke-width="1.8" opacity="0.45"/>')
A(f'<path d="M154,65 L159,52 L164,65" fill="#D8A830" stroke="{OUTLINE}" stroke-width="1" opacity="0.45"/>')

# ── Minaret (right of palace) ──
A(f'<path d="{wobble_path([(237, 135), (238, 70), (244, 70), (245, 135)])}" '
  f'fill="#E8D8B0" stroke="{OUTLINE}" stroke-width="1.8" opacity="0.45"/>')
A(f'<path d="M236,70 L241,57 L246,70" fill="#D8A830" stroke="{OUTLINE}" stroke-width="1" opacity="0.45"/>')

# ── Stone plaza line ──
plaza_y = 340
A(f'<path d="{wave_line(plaza_y, 0, W, 2, 30)}" stroke="#C8B090" stroke-width="1.5" fill="none" opacity="0.3"/>')

# ── Mosaic medallion doodle (center floor) ──
A(f'<circle cx="200" cy="{plaza_y+20}" r="12" fill="none" stroke="#C8A060" stroke-width="1.2" opacity="0.2"/>')
A(f'<circle cx="200" cy="{plaza_y+20}" r="6" fill="#E8C870" stroke="none" opacity="0.15"/>')

# ── Alchemical brazier (left side) ──
br_x, br_y = 60, 310
A(f'<path d="{wobble_path([(br_x-7, br_y+15), (br_x-5, br_y), (br_x+5, br_y), (br_x+7, br_y+15)])}" '
  f'fill="#C8B080" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.45"/>')
A(f'<path d="M{br_x},{br_y-12} Q{br_x+6},{br_y-4} {br_x},{br_y} Q{br_x-6},{br_y-4} {br_x},{br_y-12}" '
  f'fill="#E88030" stroke="{OUTLINE}" stroke-width="1.2" opacity="0.5"/>')

# ── Hanging lamp doodle (right side) ──
lamp_x, lamp_y = 350, 300
A(f'<line x1="{lamp_x}" y1="{lamp_y-15}" x2="{lamp_x}" y2="{lamp_y}" stroke="{OUTLINE}" stroke-width="1" opacity="0.35"/>')
A(f'<path d="M{lamp_x-5},{lamp_y} Q{lamp_x},{lamp_y+8} {lamp_x+5},{lamp_y}" '
  f'fill="#F0C840" stroke="{OUTLINE}" stroke-width="1" opacity="0.4"/>')
A(f'<circle cx="{lamp_x}" cy="{lamp_y+3}" r="2" fill="#FFE060" opacity="0.5"/>')

# ── Seagulls / tropical birds ──
for (gx, gy) in [(90, 20), (270, 35), (180, 45)]:
    gw = random.uniform(6, 10)
    A(f'<path d="M{gx-gw},{gy+2} Q{gx},{gy-2} {gx+gw},{gy+2}" '
      f'stroke="{OUTLINE}" stroke-width="1.2" fill="none" opacity="0.3"/>')

# ── Water sparkle dots (ocean area) ──
for _ in range(8):
    wx = random.randint(60, 340)
    wy = random.randint(20, sea_y-15)
    A(f'<circle cx="{wx}" cy="{wy}" r="1.2" fill="#80D0D0" opacity="0.45"/>')

# ── Flower box doodle (on awning) ──
for fx in [20, 370]:
    fy = 235
    for i in range(3):
        color = random.choice(['#E06080', '#F0A050', '#D070C0'])
        A(f'<circle cx="{fx + i*7}" cy="{fy}" r="2.5" fill="{color}" stroke="{OUTLINE}" stroke-width="0.6" opacity="0.4"/>')

A('</svg>')

EXTREME = ''.join(P)

# ── Inject into stage.html ───────────────────────────────────────────────
pattern = r"(if\(diff==='EXTREME'\) return ')(.*?)(';)"
replacement = r"\g<1>" + EXTREME.replace('\\', '\\\\') + r"\g<3>"
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

assert new_content != content, "Injection failed — pattern not matched"
print(f"EXTREME SVG: {len(EXTREME):,} chars injected OK")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("stage.html written.")
