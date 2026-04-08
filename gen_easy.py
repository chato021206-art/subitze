#!/usr/bin/env python3
"""gen_easy.py — Gridania graphic-recording style (hand-drawn sketch on cream paper)."""
import re, math, random

random.seed(42)  # reproducible wobble

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── Wobble helper: slightly irregular hand-drawn lines ──────────────────
def wobble_path(points, closed=False):
    """Convert list of (x,y) tuples into a slightly wobbly SVG path string."""
    if len(points) < 2:
        return ''
    segs = [f'M{points[0][0]:.1f},{points[0][1]:.1f}']
    for i in range(1, len(points)):
        x0, y0 = points[i-1]
        x1, y1 = points[i]
        # midpoint with slight random offset for hand-drawn feel
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

def cloud_canopy(cx, cy, rx, ry, bumps=7):
    """Generate a cloud-like canopy shape (bumpy ellipse)."""
    pts = []
    for i in range(bumps * 2):
        angle = math.pi * 2 * i / (bumps * 2)
        r_factor = 1.0 + random.uniform(-0.12, 0.15)
        x = cx + rx * r_factor * math.cos(angle)
        y = cy + ry * r_factor * math.sin(angle)
        pts.append((x, y))
    return wobble_path(pts, closed=True)

def sparkle(cx, cy, size=4):
    """Simple 4-point sparkle doodle."""
    s = size
    return (f'<line x1="{cx}" y1="{cy-s}" x2="{cx}" y2="{cy+s}" stroke="#40B0A0" stroke-width="1.5" stroke-linecap="round" opacity="0.7"/>'
            f'<line x1="{cx-s}" y1="{cy}" x2="{cx+s}" y2="{cy}" stroke="#40B0A0" stroke-width="1.5" stroke-linecap="round" opacity="0.7"/>')

# ── Build SVG ───────────────────────────────────────────────────────────
P = []
A = P.append

W, H = 400, 600
PAPER = '#F0EDE0'     # cream with green tint
PAPER2 = '#E8EDDA'    # slightly greener cream
OUTLINE = '#2A2A2A'
SW = 2.5              # standard stroke width
SW_BOLD = 3.5

A(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">')

# ── Paper background ──
A(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
# Subtle green wash in upper area
A(f'<rect width="{W}" height="280" fill="{PAPER2}" opacity="0.5"/>')

# ── Ground line (gentle wavy grass line across) ──
ground_y = 430
gnd_pts = [(0, ground_y)]
for x in range(20, W+1, 20):
    gnd_pts.append((x, ground_y + random.uniform(-3, 3)))
A(f'<path d="{wobble_path(gnd_pts)}" stroke="#6B8E4E" stroke-width="2" fill="none" opacity="0.5"/>')
# Grass fill below ground line
A(f'<rect y="{ground_y}" width="{W}" height="{H - ground_y}" fill="#D4E4C0" opacity="0.35"/>')

# ── Large left tree (Gridania sacred tree) ──
# Trunk
tx, tw = 45, 38
A(f'<path d="{wobble_path([(tx-tw//2, ground_y), (tx-tw//2, 80), (tx+tw//2, 65), (tx+tw//2, ground_y)])}" '
  f'fill="#8B6840" stroke="{OUTLINE}" stroke-width="{SW_BOLD}" opacity="0.9"/>')
# Canopy - large cloud shape
A(f'<path d="{cloud_canopy(tx, 90, 65, 55, 9)}" '
  f'fill="#6BA854" stroke="{OUTLINE}" stroke-width="{SW}" opacity="0.85"/>')
# Inner canopy highlight
A(f'<path d="{cloud_canopy(tx-8, 80, 35, 28, 6)}" '
  f'fill="#8CC870" stroke="none" opacity="0.4"/>')

# ── Large right tree ──
tx2 = 360
A(f'<path d="{wobble_path([(tx2-tw//2, ground_y), (tx2-tw//2, 100), (tx2+tw//2, 85), (tx2+tw//2, ground_y)])}" '
  f'fill="#8B6840" stroke="{OUTLINE}" stroke-width="{SW_BOLD}" opacity="0.9"/>')
A(f'<path d="{cloud_canopy(tx2, 105, 60, 50, 8)}" '
  f'fill="#6BA854" stroke="{OUTLINE}" stroke-width="{SW}" opacity="0.85"/>')
A(f'<path d="{cloud_canopy(tx2+5, 95, 30, 25, 6)}" '
  f'fill="#8CC870" stroke="none" opacity="0.4"/>')

# ── Medium background trees (far, lighter) ──
for (bx, by, brx, bry) in [(110, 155, 30, 25), (300, 140, 28, 22), (170, 170, 22, 18)]:
    A(f'<rect x="{bx-4}" y="{by+bry-5}" width="8" height="{ground_y - by - bry + 5}" '
      f'fill="#A08860" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.5"/>')
    A(f'<path d="{cloud_canopy(bx, by, brx, bry, 6)}" '
      f'fill="#88B868" stroke="{OUTLINE}" stroke-width="1.8" opacity="0.5"/>')

# ── Torii gate (shrine, upper area) ──
torii_x, torii_y = 200, 52
A(f'<line x1="{torii_x-30}" y1="{torii_y+40}" x2="{torii_x-30}" y2="{torii_y}" '
  f'stroke="#C85040" stroke-width="{SW_BOLD}" stroke-linecap="round"/>')
A(f'<line x1="{torii_x+30}" y1="{torii_y+40}" x2="{torii_x+30}" y2="{torii_y}" '
  f'stroke="#C85040" stroke-width="{SW_BOLD}" stroke-linecap="round"/>')
# Top beam (kasagi) - slightly curved
A(f'<path d="M{torii_x-38},{torii_y} Q{torii_x},{torii_y-5} {torii_x+38},{torii_y}" '
  f'stroke="#C85040" stroke-width="{SW_BOLD+1}" fill="none" stroke-linecap="round"/>')
# Lower beam (nuki)
A(f'<line x1="{torii_x-28}" y1="{torii_y+14}" x2="{torii_x+28}" y2="{torii_y+14}" '
  f'stroke="#C85040" stroke-width="{SW}" stroke-linecap="round"/>')

# ── Wooden platform (left side, mid area) ──
plat_y = 280
A(f'<path d="{wobble_path([(8, plat_y), (8, plat_y-18), (85, plat_y-22), (85, plat_y)])}" '
  f'fill="#C8A870" stroke="{OUTLINE}" stroke-width="1.8" opacity="0.6"/>')
# Railing posts
for px in [15, 40, 65]:
    A(f'<line x1="{px}" y1="{plat_y-22}" x2="{px}" y2="{plat_y-38}" '
      f'stroke="#A08050" stroke-width="1.8" stroke-linecap="round" opacity="0.6"/>')
A(f'<line x1="12" y1="{plat_y-35}" x2="70" y2="{plat_y-37}" '
  f'stroke="#A08050" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>')

# ── Wooden platform (right side) ──
A(f'<path d="{wobble_path([(320, plat_y+15), (320, plat_y-3), (395, plat_y-7), (395, plat_y+15)])}" '
  f'fill="#C8A870" stroke="{OUTLINE}" stroke-width="1.8" opacity="0.6"/>')

# ── Aether sparkles (teal doodles scattered) ──
sparkle_positions = [(25, 200), (75, 340), (90, 270), (310, 300), (340, 220), (370, 380), (55, 410), (350, 415)]
for sx, sy in sparkle_positions:
    size = random.uniform(3, 5.5)
    A(sparkle(sx, sy, size))

# ── Small wildflower doodles along ground ──
flower_colors = ['#E8A040', '#E06080', '#D070C0', '#60A0E0']
for fx in range(15, W, 28):
    if 120 < fx < 280:
        continue  # keep center clear
    fy = ground_y + random.uniform(-5, 2)
    color = random.choice(flower_colors)
    stem_h = random.uniform(10, 18)
    A(f'<line x1="{fx}" y1="{fy}" x2="{fx}" y2="{fy - stem_h}" '
      f'stroke="#5A8040" stroke-width="1.2" stroke-linecap="round" opacity="0.6"/>')
    A(f'<circle cx="{fx}" cy="{fy - stem_h}" r="{random.uniform(2.5, 4)}" '
      f'fill="{color}" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.65"/>')

# ── Bird V-shapes (upper area) ──
for (bx, by) in [(90, 30), (160, 18), (310, 25), (250, 40)]:
    bw = random.uniform(6, 10)
    A(f'<path d="M{bx-bw},{by+3} Q{bx},{by-2} {bx+bw},{by+3}" '
      f'stroke="{OUTLINE}" stroke-width="1.2" fill="none" opacity="0.4"/>')

# ── Small leaf doodles on trees ──
for (lx, ly) in [(30, 180), (55, 220), (20, 310), (370, 200), (350, 280), (380, 340)]:
    angle = random.uniform(0, math.pi)
    dx = 6 * math.cos(angle)
    dy = 6 * math.sin(angle)
    A(f'<path d="M{lx},{ly} Q{lx+dx},{ly-dy} {lx+dx*2},{ly}" '
      f'stroke="#5A9040" stroke-width="1.5" fill="none" opacity="0.45"/>')

# ── Tiny mushroom doodle (forest floor accent) ──
for (mx, my) in [(70, ground_y + 8), (340, ground_y + 6)]:
    A(f'<line x1="{mx}" y1="{my}" x2="{mx}" y2="{my-7}" stroke="#A08060" stroke-width="1.5" opacity="0.5"/>')
    A(f'<path d="M{mx-5},{my-7} Q{mx},{my-13} {mx+5},{my-7}" fill="#D06040" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.5"/>')

# ── Small squirrel doodle (right side) ──
sq_x, sq_y = 330, ground_y - 5
A(f'<ellipse cx="{sq_x}" cy="{sq_y}" rx="5" ry="4" fill="#C09060" stroke="{OUTLINE}" stroke-width="1" opacity="0.5"/>')
A(f'<circle cx="{sq_x-4}" cy="{sq_y-4}" r="3" fill="#C09060" stroke="{OUTLINE}" stroke-width="1" opacity="0.5"/>')
A(f'<path d="M{sq_x+3},{sq_y-2} Q{sq_x+10},{sq_y-12} {sq_x+5},{sq_y-6}" stroke="#C09060" stroke-width="1.5" fill="none" opacity="0.5"/>')

A('</svg>')

EASY = ''.join(P)

# ── Inject into stage.html ───────────────────────────────────────────────
pattern = r"(if\(diff==='EASY'\) return ')(.*?)(';)"
replacement = r"\g<1>" + EASY.replace('\\', '\\\\') + r"\g<3>"
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

assert new_content != content, "Injection failed — pattern not matched"
print(f"EASY SVG: {len(EASY):,} chars injected OK")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("stage.html written.")
