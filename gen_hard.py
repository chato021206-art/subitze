#!/usr/bin/env python3
"""gen_hard.py — Ul'dah / Thanalan Desert City, bird's-eye graphic-recording style.

Top-down view of an extremely dense desert trade city with 200+ SVG elements.
Graphic recording / hand-drawn sketch aesthetic on cream paper.
"""
import re, math, random

random.seed(44)

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── Wobble helpers ──────────────────────────────────────────────────────
def wobble_path(points, closed=False):
    """Generate a hand-drawn wobbly path through points."""
    if len(points) < 2:
        return ''
    segs = [f'M{points[0][0]:.1f},{points[0][1]:.1f}']
    for i in range(1, len(points)):
        x0, y0 = points[i - 1]
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


def wobble_rect(x, y, w, h):
    """Return wobble_path points for a rectangle."""
    return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]


def wobble_circle_path(cx, cy, r, n=12):
    """Approximate a circle with wobbly polygon."""
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        rr = r + random.uniform(-r * 0.08, r * 0.08)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return wobble_path(pts, closed=True)


def wobble_ellipse_path(cx, cy, rx, ry, n=12):
    """Approximate an ellipse with wobbly polygon."""
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        rrx = rx + random.uniform(-rx * 0.07, rx * 0.07)
        rry = ry + random.uniform(-ry * 0.07, ry * 0.07)
        pts.append((cx + rrx * math.cos(a), cy + rry * math.sin(a)))
    return wobble_path(pts, closed=True)


def wobble_polygon(cx, cy, r, sides, irregularity=0.15):
    """Irregular polygon for rocks, plazas, etc."""
    pts = []
    for i in range(sides):
        a = 2 * math.pi * i / sides + random.uniform(-0.2, 0.2)
        rr = r * random.uniform(1 - irregularity, 1 + irregularity)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return wobble_path(pts, closed=True)


def wobble_star(cx, cy, r_outer, r_inner, points_n):
    """Star shape for decorative elements."""
    pts = []
    for i in range(points_n * 2):
        a = math.pi * i / points_n - math.pi / 2
        r = r_outer if i % 2 == 0 else r_inner
        r += random.uniform(-r * 0.05, r * 0.05)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return wobble_path(pts, closed=True)


# ── Build SVG ───────────────────────────────────────────────────────────
P = []
A = P.append
elem_count = 0

def add(s):
    global elem_count
    P.append(s)
    # Count approximate SVG elements
    for tag in ['<path', '<circle', '<ellipse', '<rect', '<line', '<polygon']:
        elem_count += s.count(tag)

W, H = 400, 600

# Color palette
PAPER = '#F2ECE0'
PAPER2 = '#EDE4D0'
SAND1 = '#E8D8B8'
SAND2 = '#D8C8A0'
SAND3 = '#C8B888'
SAND4 = '#B8A878'
DOME_TEAL = '#48A8A0'
DOME_TEAL2 = '#3A9890'
DOME_TEAL3 = '#5AB8B0'
WALL = '#D0B880'
WALL2 = '#C0A060'
WALL3 = '#A89050'
GOLD = '#D8A830'
GOLD2 = '#C8981F'
GOLD3 = '#E8C040'
MESA = '#D07030'
MESA2 = '#B05820'
MESA3 = '#C06028'
FLAME = '#E88030'
FLAME2 = '#F0C040'
FLAME3 = '#F8D860'
OUTLINE = '#2A2A2A'
STREET = '#D8C8A0'
PLAZA = '#C8B888'
GARDEN = '#7BA858'
GARDEN2 = '#5A8838'
GARDEN3 = '#8CC068'
WATER = '#68B8D0'
WATER2 = '#88C8D8'
WATER3 = '#4898B0'
SHADOW = '#B8A880'
SHADOW2 = '#A09070'
ROOF_TAN = '#D8C090'
ROOF_OCHRE = '#C8A860'
CARPET_RED = '#C83030'
CARPET_BLUE = '#3868A0'
CARPET_PURPLE = '#A04890'

SW = 2.0
SW_BOLD = 3.0
SW_THIN = 1.2
SW_HAIR = 0.7
SW_MICRO = 0.4

A(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">')

# ══════════════════════════════════════════════════════════════════════════
# LAYER 1 — Ground / Base / Paper Texture
# ══════════════════════════════════════════════════════════════════════════

# Cream paper base
add(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')

# Warm amber wash zones (large irregular patches for paper feel)
wash_zones = [
    (30, 50, 140, 100), (220, 30, 160, 90),
    (10, 400, 180, 120), (200, 450, 190, 140),
    (80, 200, 240, 180), (50, 300, 100, 80),
    (300, 300, 90, 70), (160, 520, 120, 60),
    (20, 150, 80, 60), (320, 150, 70, 60),
]
for wx, wy, ww, wh in wash_zones:
    op = random.uniform(0.06, 0.14)
    add(f'<path d="{wobble_ellipse_path(wx + ww/2, wy + wh/2, ww/2, wh/2, 16)}" '
        f'fill="{SAND1}" opacity="{op:.2f}"/>')

# Secondary warm spots (ochre tint)
for _ in range(6):
    wx = random.uniform(30, 370)
    wy = random.uniform(30, 570)
    wr = random.uniform(30, 60)
    add(f'<path d="{wobble_circle_path(wx, wy, wr, 10)}" '
        f'fill="{WALL}" opacity="{random.uniform(0.03, 0.07):.2f}"/>')

# Sand-colored ground fill
add(f'<rect width="{W}" height="{H}" fill="{SAND2}" opacity="0.10"/>')

# Paper grain texture (tiny stipple dots)
for _ in range(80):
    dx = random.uniform(5, 395)
    dy = random.uniform(5, 595)
    dr = random.uniform(0.3, 1.0)
    add(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="{dr:.1f}" '
        f'fill="{SAND3}" opacity="{random.uniform(0.04, 0.12):.2f}"/>')

# Dune ripple textures across the whole canvas (subtle wavy parallel lines)
for dy in range(15, H, 28):
    y_offset = random.uniform(-5, 5)
    pts = [(x, dy + y_offset + random.uniform(-2, 2) + 3 * math.sin(x / 45))
           for x in range(0, W + 1, 20)]
    op = random.uniform(0.05, 0.10)
    add(f'<path d="{wobble_path(pts)}" stroke="{SAND3}" stroke-width="0.5" fill="none" opacity="{op:.2f}"/>')

# Ground zone differentiation: stone plaza zones (darker patches)
plaza_zones = [
    (160, 260, 80, 80), (70, 130, 50, 40), (280, 130, 50, 40),
    (90, 470, 40, 35), (270, 470, 40, 35),
]
for pzx, pzy, pzw, pzh in plaza_zones:
    add(f'<path d="{wobble_ellipse_path(pzx + pzw/2, pzy + pzh/2, pzw/2, pzh/2, 12)}" '
        f'fill="{SAND4}" opacity="0.08"/>')

# Packed-earth street zones (tan strips — drawn before walls/buildings)
streets = [
    # Horizontal main avenue
    [(20, 288), (120, 290), (200, 292), (280, 290), (380, 288)],
    [(20, 312), (120, 310), (200, 308), (280, 310), (380, 312)],
    # Vertical main boulevard
    [(188, 20), (190, 150), (192, 300), (190, 450), (188, 580)],
    [(212, 20), (210, 150), (208, 300), (210, 450), (212, 580)],
    # Diagonal bazaar (NW)
    [(40, 145), (80, 185), (130, 235), (165, 265)],
    [(52, 150), (90, 190), (138, 240), (172, 268)],
    # Diagonal bazaar (NE)
    [(360, 145), (320, 185), (270, 235), (235, 265)],
    [(348, 150), (310, 190), (262, 240), (228, 268)],
    # Winding secondary streets (south)
    [(30, 430), (100, 420), (180, 415), (260, 420), (340, 430), (380, 435)],
    [(30, 448), (100, 438), (180, 433), (260, 438), (340, 448), (380, 453)],
    # East-west mid-street (north district)
    [(30, 170), (100, 172), (170, 175), (230, 174), (300, 172), (370, 170)],
    [(30, 182), (100, 184), (170, 186), (230, 185), (300, 183), (370, 182)],
    # Winding alleys
    [(130, 320), (140, 370), (145, 410)],
    [(260, 320), (255, 370), (258, 410)],
    [(60, 250), (65, 300), (70, 350)],
    [(335, 250), (332, 300), (330, 350)],
]
for st in streets:
    add(f'<path d="{wobble_path(st)}" stroke="{STREET}" stroke-width="2.5" fill="none" opacity="0.25"/>')


# ══════════════════════════════════════════════════════════════════════════
# LAYER 2 — City Walls & Layout (top-down)
# ══════════════════════════════════════════════════════════════════════════

# Outer city wall — large irregular octagonal/rectangular shape
wall_outer = [
    (25, 30), (100, 24), (180, 22), (220, 22), (300, 24), (375, 30),
    (385, 40), (390, 120), (392, 200), (390, 300),
    (392, 400), (390, 500), (385, 560), (382, 570),
    (300, 576), (220, 578), (180, 578), (100, 576),
    (25, 570), (18, 560), (14, 500), (12, 400),
    (14, 300), (12, 200), (14, 120), (18, 40),
]
# Outer wall line (thick, bold outline)
add(f'<path d="{wobble_path(wall_outer, True)}" fill="none" stroke="{WALL2}" stroke-width="{SW_BOLD + 1.5}" opacity="0.55"/>')
# Wall fill (subtle)
add(f'<path d="{wobble_path(wall_outer, True)}" fill="{WALL}" opacity="0.06"/>')
# Wall walkway (inner double line)
wall_inner = [(x + (200 - x) * 0.035, y + (300 - y) * 0.035) for x, y in wall_outer]
add(f'<path d="{wobble_path(wall_inner, True)}" fill="none" stroke="{WALL}" stroke-width="{SW}" opacity="0.35"/>')

# Wall towers (small square protrusions along walls) — top-down squares
tower_positions = [
    (25, 30), (100, 25), (180, 22), (300, 24), (375, 30),
    (388, 120), (392, 200), (390, 300), (392, 400), (390, 500), (385, 560),
    (300, 575), (220, 578), (180, 578), (100, 576),
    (25, 570), (14, 480), (12, 380), (12, 280), (13, 180), (16, 80),
]
for tx, ty in tower_positions:
    tw = random.uniform(8, 13)
    # Tower shadow
    add(f'<path d="{wobble_path(wobble_rect(tx - tw/2 + 2, ty - tw/2 + 2, tw, tw), True)}" '
        f'fill="{SHADOW}" opacity="0.08"/>')
    # Tower body
    add(f'<path d="{wobble_path(wobble_rect(tx - tw/2, ty - tw/2, tw, tw), True)}" '
        f'fill="{WALL}" stroke="{OUTLINE}" stroke-width="{SW_THIN}" opacity="0.5"/>')
    # Tower center dot
    add(f'<circle cx="{tx}" cy="{ty}" r="1.2" fill="{WALL3}" opacity="0.3"/>')

# Crenellations along outer wall
for i in range(len(wall_outer)):
    x0, y0 = wall_outer[i]
    x1, y1 = wall_outer[(i + 1) % len(wall_outer)]
    dist = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
    n_cren = int(dist / 12)
    for j in range(n_cren):
        t = (j + 0.5) / max(n_cren, 1)
        cx_ = x0 + t * (x1 - x0)
        cy_ = y0 + t * (y1 - y0)
        add(f'<rect x="{cx_ - 1.2:.1f}" y="{cy_ - 1.2:.1f}" width="2.4" height="2.4" '
            f'fill="{WALL2}" stroke="{OUTLINE}" stroke-width="0.25" opacity="0.18"/>')

# Inner wall sections dividing districts
# Northern district wall
inner_wall_n = [(30, 178), (80, 174), (140, 176), (200, 178), (260, 175), (320, 174), (370, 178)]
add(f'<path d="{wobble_path(inner_wall_n)}" stroke="{WALL2}" stroke-width="{SW + 0.8}" fill="none" opacity="0.42"/>')
# Inner wall walkway
inner_wall_n2 = [(x, y + 4) for x, y in inner_wall_n]
add(f'<path d="{wobble_path(inner_wall_n2)}" stroke="{WALL}" stroke-width="{SW_THIN}" fill="none" opacity="0.25"/>')

# Southern district wall
inner_wall_s = [(30, 438), (80, 434), (140, 436), (200, 438), (260, 435), (320, 434), (370, 438)]
add(f'<path d="{wobble_path(inner_wall_s)}" stroke="{WALL2}" stroke-width="{SW + 0.8}" fill="none" opacity="0.42"/>')
inner_wall_s2 = [(x, y + 4) for x, y in inner_wall_s]
add(f'<path d="{wobble_path(inner_wall_s2)}" stroke="{WALL}" stroke-width="{SW_THIN}" fill="none" opacity="0.25"/>')

# Mid-district divider (east-west, lighter)
inner_wall_m = [(130, 340), (170, 338), (230, 338), (270, 340)]
add(f'<path d="{wobble_path(inner_wall_m)}" stroke="{WALL}" stroke-width="{SW}" fill="none" opacity="0.25"/>')

# Main gate openings
# South gate (gap in wall with flanking towers)
gate_y = 578
for gx in [175, 213]:
    add(f'<path d="{wobble_path(wobble_rect(gx, gate_y - 9, 13, 18), True)}" '
        f'fill="{WALL2}" stroke="{OUTLINE}" stroke-width="{SW}" opacity="0.6"/>')
    add(f'<circle cx="{gx + 6.5}" cy="{gate_y}" r="2.5" fill="{GOLD}" opacity="0.3"/>')
# Gate road
add(f'<path d="{wobble_path([(190, 578), (190, 600)])}" stroke="{SAND2}" stroke-width="5" fill="none" opacity="0.35"/>')
add(f'<path d="{wobble_path([(210, 578), (210, 600)])}" stroke="{SAND2}" stroke-width="5" fill="none" opacity="0.35"/>')

# North gate
for gx in [175, 213]:
    add(f'<path d="{wobble_path(wobble_rect(gx, 14, 13, 16), True)}" '
        f'fill="{WALL2}" stroke="{OUTLINE}" stroke-width="{SW}" opacity="0.6"/>')
    add(f'<circle cx="{gx + 6.5}" cy="{22}" r="2.5" fill="{GOLD}" opacity="0.3"/>')

# East gate (small)
add(f'<path d="{wobble_path(wobble_rect(386, 290, 14, 12), True)}" '
    f'fill="{WALL2}" stroke="{OUTLINE}" stroke-width="{SW_THIN}" opacity="0.5"/>')
add(f'<path d="{wobble_path(wobble_rect(386, 306, 14, 12), True)}" '
    f'fill="{WALL2}" stroke="{OUTLINE}" stroke-width="{SW_THIN}" opacity="0.5"/>')

# West gate (small)
add(f'<path d="{wobble_path(wobble_rect(4, 290, 14, 12), True)}" '
    f'fill="{WALL2}" stroke="{OUTLINE}" stroke-width="{SW_THIN}" opacity="0.5"/>')
add(f'<path d="{wobble_path(wobble_rect(4, 306, 14, 12), True)}" '
    f'fill="{WALL2}" stroke="{OUTLINE}" stroke-width="{SW_THIN}" opacity="0.5"/>')


# ══════════════════════════════════════════════════════════════════════════
# LAYER 3 — Buildings (rooftops from above)
# ══════════════════════════════════════════════════════════════════════════

# --- Palace compound (center-north, largest dome + surrounding structures) ---
palace_cx, palace_cy = 200, 100
# Palace grounds outline (courtyard)
palace_pts = wobble_rect(140, 48, 120, 105)
add(f'<path d="{wobble_path(palace_pts, True)}" '
    f'fill="{SAND1}" stroke="{WALL2}" stroke-width="{SW + 0.5}" opacity="0.28"/>')
# Inner courtyard
add(f'<path d="{wobble_path(wobble_rect(155, 62, 90, 76), True)}" '
    f'fill="{SAND2}" stroke="{WALL}" stroke-width="{SW_HAIR}" opacity="0.15"/>')

# Main palace dome (large)
add(f'<path d="{wobble_circle_path(palace_cx, palace_cy, 30)}" '
    f'fill="{DOME_TEAL}" stroke="{OUTLINE}" stroke-width="{SW_BOLD}" opacity="0.72"/>')
# Concentric ring details
for ring_r, ring_op in [(22, 0.4), (14, 0.3), (7, 0.25)]:
    add(f'<path d="{wobble_circle_path(palace_cx, palace_cy, ring_r)}" '
        f'fill="none" stroke="{OUTLINE}" stroke-width="{SW_HAIR}" opacity="{ring_op}"/>')
# Palace dome center pip (gold finial)
add(f'<circle cx="{palace_cx}" cy="{palace_cy}" r="4" fill="{GOLD}" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.7"/>')
add(f'<circle cx="{palace_cx}" cy="{palace_cy}" r="2" fill="{GOLD3}" opacity="0.5"/>')

# Surrounding palace buildings (wings and annexes)
palace_wings = [
    (-42, -25, 20, 28), (35, -20, 22, 25), (-40, 22, 24, 20), (32, 25, 20, 22),
    (-25, -40, 16, 14), (22, -40, 16, 14), (-42, 0, 14, 16), (40, 0, 14, 16),
    (-15, 38, 30, 12), (0, -42, 20, 10),
]
for dx, dy, pw, ph in palace_wings:
    add(f'<path d="{wobble_path(wobble_rect(palace_cx + dx, palace_cy + dy, pw, ph), True)}" '
        f'fill="{SAND1}" stroke="{OUTLINE}" stroke-width="{SW_THIN}" opacity="0.48"/>')

# Palace garden courtyard features
add(f'<path d="{wobble_circle_path(palace_cx - 30, palace_cy - 30, 5)}" '
    f'fill="{GARDEN}" stroke="none" opacity="0.2"/>')
add(f'<path d="{wobble_circle_path(palace_cx + 30, palace_cy - 30, 5)}" '
    f'fill="{GARDEN}" stroke="none" opacity="0.2"/>')

# --- Large teal dome rooftops (10 scattered through city) ---
large_domes = [
    (75, 80, 18), (320, 75, 17), (110, 240, 20),
    (295, 235, 18), (65, 350, 19), (335, 350, 17),
    (140, 480, 16), (275, 485, 18),
    (80, 500, 15), (320, 500, 14),
]
for dcx, dcy, dr in large_domes:
    # Shadow
    add(f'<path d="{wobble_circle_path(dcx + 3, dcy + 3, dr)}" '
        f'fill="{SHADOW}" opacity="0.13"/>')
    # Dome
    add(f'<path d="{wobble_circle_path(dcx, dcy, dr)}" '
        f'fill="{DOME_TEAL}" stroke="{OUTLINE}" stroke-width="{SW}" opacity="0.62"/>')
    # Concentric ring
    add(f'<path d="{wobble_circle_path(dcx, dcy, dr * 0.6)}" '
        f'fill="none" stroke="{OUTLINE}" stroke-width="{SW_HAIR}" opacity="0.3"/>')
    # Inner ring
    add(f'<path d="{wobble_circle_path(dcx, dcy, dr * 0.3)}" '
        f'fill="none" stroke="{OUTLINE}" stroke-width="{SW_MICRO}" opacity="0.2"/>')
    # Center pip
    add(f'<circle cx="{dcx}" cy="{dcy}" r="2" fill="{GOLD}" opacity="0.55"/>')

# --- Smaller domes (8) ---
small_domes = [
    (52, 140, 10), (348, 140, 11), (240, 195, 9),
    (160, 350, 10), (245, 380, 11), (95, 505, 9),
    (170, 220, 8), (230, 220, 8),
]
for dcx, dcy, dr in small_domes:
    add(f'<path d="{wobble_circle_path(dcx, dcy, dr)}" '
        f'fill="{DOME_TEAL2}" stroke="{OUTLINE}" stroke-width="{SW_THIN}" opacity="0.52"/>')
    add(f'<path d="{wobble_circle_path(dcx, dcy, dr * 0.5)}" '
        f'fill="none" stroke="{OUTLINE}" stroke-width="{SW_MICRO}" opacity="0.2"/>')
    add(f'<circle cx="{dcx}" cy="{dcy}" r="1.5" fill="{GOLD2}" opacity="0.45"/>')

# --- Minaret tops (6, seen from above: small circle with radiating lines) ---
minarets = [
    (90, 92, 5), (315, 90, 5), (155, 462, 4.5), (252, 458, 4.5),
    (140, 105, 4), (260, 105, 4),
]
for mcx, mcy, mr in minarets:
    # Radiating lines (sunburst from above)
    for angle in range(0, 360, 40):
        rad = math.radians(angle + random.uniform(-5, 5))
        x1 = mcx + (mr + 2) * math.cos(rad)
        y1 = mcy + (mr + 2) * math.sin(rad)
        x2 = mcx + (mr + 7) * math.cos(rad)
        y2 = mcy + (mr + 7) * math.sin(rad)
        add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{GOLD}" stroke-width="0.7" opacity="0.4"/>')
    # Circle base
    add(f'<path d="{wobble_circle_path(mcx, mcy, mr)}" '
        f'fill="{GOLD}" stroke="{OUTLINE}" stroke-width="{SW_THIN}" opacity="0.62"/>')
    # Center point (spire top)
    add(f'<circle cx="{mcx}" cy="{mcy}" r="1.3" fill="{OUTLINE}" opacity="0.45"/>')
    # Gold flag/standard (tiny triangle)
    flag_angle = random.uniform(0, 2 * math.pi)
    fx = mcx + (mr + 7) * math.cos(flag_angle)
    fy = mcy + (mr + 7) * math.sin(flag_angle)
    add(f'<path d="M{fx:.1f},{fy - 2:.1f} L{fx + 5:.1f},{fy:.1f} L{fx:.1f},{fy + 2:.1f}Z" '
        f'fill="{GOLD}" stroke="{OUTLINE}" stroke-width="0.4" opacity="0.45"/>')

# --- Rectangular flat-roofed buildings (25+) ---
flat_buildings = [
    # Along north wall
    (32, 42, 24, 30), (120, 48, 18, 24), (260, 50, 20, 22),
    (350, 42, 26, 32),
    # West side
    (32, 192, 28, 22), (35, 252, 30, 24), (30, 370, 22, 28),
    (35, 530, 28, 22), (32, 455, 20, 25),
    # East side
    (342, 192, 24, 26), (338, 255, 28, 22), (345, 375, 22, 26),
    (340, 525, 25, 24), (342, 458, 20, 22),
    # Central area
    (115, 192, 22, 18), (258, 192, 22, 18),
    (95, 280, 24, 20), (278, 280, 22, 18),
    (220, 340, 18, 22), (125, 400, 22, 18),
    (275, 400, 22, 20), (175, 530, 26, 18),
    # Extra density
    (60, 120, 18, 16), (320, 120, 16, 18),
    (150, 360, 16, 14), (240, 360, 14, 16),
    (70, 455, 18, 16), (310, 455, 16, 18),
]
for bx, by, bw, bh in flat_buildings:
    # Shadow
    add(f'<path d="{wobble_path(wobble_rect(bx + 2, by + 2, bw, bh), True)}" '
        f'fill="{SHADOW}" opacity="0.10"/>')
    # Building
    fill = random.choice([SAND1, ROOF_TAN, ROOF_OCHRE])
    add(f'<path d="{wobble_path(wobble_rect(bx, by, bw, bh), True)}" '
        f'fill="{fill}" stroke="{OUTLINE}" stroke-width="{SW_THIN}" opacity="0.52"/>')
    # Roof detail: internal lines
    if random.random() > 0.3:
        # Horizontal roof line
        add(f'<line x1="{bx + 3}" y1="{by + bh/2:.0f}" x2="{bx + bw - 3}" y2="{by + bh/2:.0f}" '
            f'stroke="{OUTLINE}" stroke-width="0.4" opacity="0.18"/>')
    if random.random() > 0.5:
        # Cross line
        add(f'<line x1="{bx + bw/2:.0f}" y1="{by + 3}" x2="{bx + bw/2:.0f}" y2="{by + bh - 3}" '
            f'stroke="{OUTLINE}" stroke-width="0.4" opacity="0.15"/>')
    # Doorway mark
    side = random.randint(0, 3)
    if side == 0:
        dx, dy = bx + bw / 2, by
    elif side == 1:
        dx, dy = bx + bw, by + bh / 2
    elif side == 2:
        dx, dy = bx + bw / 2, by + bh
    else:
        dx, dy = bx, by + bh / 2
    add(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="1" fill="{OUTLINE}" opacity="0.22"/>')

# --- Market arcade rooftops (long rectangles with stall divisions) ---
arcades = [
    (55, 280, 85, 12), (260, 280, 75, 12),
    (55, 420, 65, 10), (280, 420, 65, 10),
    (55, 172, 60, 9), (285, 172, 60, 9),
    (135, 338, 20, 50), (245, 338, 20, 50),
]
for ax, ay, aw, ah in arcades:
    add(f'<path d="{wobble_path(wobble_rect(ax, ay, aw, ah), True)}" '
        f'fill="{SAND3}" stroke="{OUTLINE}" stroke-width="{SW_THIN}" opacity="0.45"/>')
    # Stall dividers
    if aw > ah:
        for sx in range(int(ax) + 8, int(ax + aw), 8):
            add(f'<line x1="{sx}" y1="{ay}" x2="{sx}" y2="{ay + ah}" '
                f'stroke="{OUTLINE}" stroke-width="0.4" opacity="0.25"/>')
    else:
        for sy in range(int(ay) + 8, int(ay + ah), 8):
            add(f'<line x1="{ax}" y1="{sy}" x2="{ax + aw}" y2="{sy}" '
                f'stroke="{OUTLINE}" stroke-width="0.4" opacity="0.25"/>')


# ══════════════════════════════════════════════════════════════════════════
# LAYER 4 — Streets, Markets & Public Spaces
# ══════════════════════════════════════════════════════════════════════════

# Central ceremonial plaza with eternal flame
plaza_cx, plaza_cy = 200, 300
# Plaza stone floor
add(f'<path d="{wobble_polygon(plaza_cx, plaza_cy, 38, 8, 0.08)}" '
    f'fill="{PLAZA}" stroke="{OUTLINE}" stroke-width="{SW}" opacity="0.32"/>')
# Concentric plaza rings (stone inlay pattern)
for ring_r, ring_op in [(30, 0.25), (22, 0.2), (14, 0.18)]:
    add(f'<path d="{wobble_circle_path(plaza_cx, plaza_cy, ring_r, 14)}" '
        f'fill="none" stroke="{WALL2}" stroke-width="{SW_HAIR}" opacity="{ring_op}"/>')
# Radial lines from center (star pattern in floor)
for angle in range(0, 360, 30):
    rad = math.radians(angle)
    x2 = plaza_cx + 30 * math.cos(rad)
    y2 = plaza_cy + 30 * math.sin(rad)
    add(f'<line x1="{plaza_cx}" y1="{plaza_cy}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{WALL2}" stroke-width="0.4" fill="none" opacity="0.12"/>')
# Cobblestones around plaza
for _ in range(20):
    angle = random.uniform(0, 2 * math.pi)
    dist = random.uniform(20, 36)
    sx = plaza_cx + dist * math.cos(angle)
    sy = plaza_cy + dist * math.sin(angle)
    sr = random.uniform(1.5, 3)
    add(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr:.1f}" '
        f'fill="none" stroke="{WALL2}" stroke-width="0.3" opacity="0.15"/>')

# Eternal flame in plaza center
add(f'<circle cx="{plaza_cx}" cy="{plaza_cy}" r="16" fill="{FLAME}" opacity="0.06"/>')  # outer glow
add(f'<path d="{wobble_circle_path(plaza_cx, plaza_cy, 9)}" '
    f'fill="{FLAME}" stroke="{OUTLINE}" stroke-width="{SW_THIN}" opacity="0.65"/>')
add(f'<path d="{wobble_circle_path(plaza_cx, plaza_cy, 6)}" '
    f'fill="{FLAME2}" stroke="none" opacity="0.55"/>')
add(f'<circle cx="{plaza_cx}" cy="{plaza_cy}" r="3" fill="{FLAME3}" opacity="0.5"/>')
add(f'<circle cx="{plaza_cx}" cy="{plaza_cy}" r="1.5" fill="#FFF8E0" opacity="0.45"/>')

# Market stalls in rows (colorful small rectangles along streets)
stall_colors = ['#C85040', '#D8A830', '#48A8A0', '#A06830', '#D07840', '#8B6838',
                '#B03838', '#886838', '#408080', '#C87830']

# Along east-west avenue (both sides)
for sx in range(45, 180, 10):
    c = random.choice(stall_colors)
    sh = random.uniform(4, 7)
    add(f'<rect x="{sx}" y="{290 - sh:.1f}" width="7" height="{sh:.1f}" rx="0.5" '
        f'fill="{c}" stroke="{OUTLINE}" stroke-width="0.4" opacity="0.42"/>')
for sx in range(220, 375, 10):
    c = random.choice(stall_colors)
    sh = random.uniform(4, 7)
    add(f'<rect x="{sx}" y="{312}" width="7" height="{sh:.1f}" rx="0.5" '
        f'fill="{c}" stroke="{OUTLINE}" stroke-width="0.4" opacity="0.42"/>')

# Along north-south boulevard (both sides)
for sy in range(45, 175, 12):
    c = random.choice(stall_colors)
    sw_ = random.uniform(4, 7)
    add(f'<rect x="{212}" y="{sy}" width="{sw_:.1f}" height="7" rx="0.5" '
        f'fill="{c}" stroke="{OUTLINE}" stroke-width="0.4" opacity="0.38"/>')
for sy in range(330, 565, 12):
    c = random.choice(stall_colors)
    sw_ = random.uniform(4, 7)
    add(f'<rect x="{184 - sw_:.1f}" y="{sy}" width="{sw_:.1f}" height="7" rx="0.5" '
        f'fill="{c}" stroke="{OUTLINE}" stroke-width="0.4" opacity="0.38"/>')

# Along north district street
for sx in range(55, 165, 11):
    c = random.choice(stall_colors)
    sh = random.uniform(3, 5)
    add(f'<rect x="{sx}" y="{173 - sh:.1f}" width="6" height="{sh:.1f}" rx="0.5" '
        f'fill="{c}" stroke="{OUTLINE}" stroke-width="0.3" opacity="0.35"/>')

# Along south district street
for sx in range(55, 175, 11):
    c = random.choice(stall_colors)
    sh = random.uniform(3, 5)
    add(f'<rect x="{sx}" y="{450}" width="6" height="{sh:.1f}" rx="0.5" '
        f'fill="{c}" stroke="{OUTLINE}" stroke-width="0.3" opacity="0.35"/>')
for sx in range(265, 370, 11):
    c = random.choice(stall_colors)
    sh = random.uniform(3, 5)
    add(f'<rect x="{sx}" y="{450}" width="6" height="{sh:.1f}" rx="0.5" '
        f'fill="{c}" stroke="{OUTLINE}" stroke-width="0.3" opacity="0.35"/>')

# Carpet / rug displays (tiny patterned rectangles — very detailed)
carpet_colors = ['#C83030', '#D06828', '#A04890', '#D8A020', '#3898A0',
                 '#883060', '#B06020', '#285888']
carpet_spots = [
    (68, 300), (82, 306), (98, 298), (112, 308),
    (278, 295), (296, 304), (315, 298), (332, 307),
    (148, 248), (168, 244), (232, 248), (252, 244),
    (75, 175), (90, 178), (310, 175), (325, 178),
    (148, 425), (165, 430), (235, 425), (252, 430),
    (180, 350), (220, 350),
]
for cpx, cpy in carpet_spots:
    cw = random.uniform(5, 10)
    ch = random.uniform(3, 7)
    c = random.choice(carpet_colors)
    add(f'<rect x="{cpx}" y="{cpy}" width="{cw:.1f}" height="{ch:.1f}" rx="0.5" '
        f'fill="{c}" stroke="{OUTLINE}" stroke-width="0.35" opacity="0.38"/>')
    # Pattern stripe on carpet
    add(f'<line x1="{cpx + 1}" y1="{cpy + ch/2:.1f}" x2="{cpx + cw - 1:.1f}" y2="{cpy + ch/2:.1f}" '
        f'stroke="#FFF8E0" stroke-width="0.4" opacity="0.25"/>')
    # Edge detail
    if random.random() > 0.5:
        add(f'<line x1="{cpx + cw/2:.1f}" y1="{cpy + 1:.1f}" x2="{cpx + cw/2:.1f}" y2="{cpy + ch - 1:.1f}" '
            f'stroke="#FFF8E0" stroke-width="0.3" opacity="0.2"/>')

# Fountain / oasis pool (north district - main)
ftn_cx, ftn_cy = 200, 215
add(f'<path d="{wobble_circle_path(ftn_cx, ftn_cy, 16, 14)}" '
    f'fill="{WATER}" stroke="{OUTLINE}" stroke-width="{SW_THIN}" opacity="0.48"/>')
add(f'<path d="{wobble_circle_path(ftn_cx, ftn_cy, 11, 12)}" '
    f'fill="{WATER2}" stroke="none" opacity="0.32"/>')
add(f'<path d="{wobble_circle_path(ftn_cx, ftn_cy, 5, 8)}" '
    f'fill="{WATER3}" stroke="none" opacity="0.2"/>')
add(f'<circle cx="{ftn_cx}" cy="{ftn_cy}" r="2.5" fill="#FFF" opacity="0.25"/>')

# Second fountain (south district)
ftn2_cx, ftn2_cy = 200, 500
add(f'<path d="{wobble_circle_path(ftn2_cx, ftn2_cy, 12, 12)}" '
    f'fill="{WATER}" stroke="{OUTLINE}" stroke-width="{SW_HAIR}" opacity="0.4"/>')
add(f'<path d="{wobble_circle_path(ftn2_cx, ftn2_cy, 7, 10)}" '
    f'fill="{WATER2}" stroke="none" opacity="0.28"/>')
add(f'<circle cx="{ftn2_cx}" cy="{ftn2_cy}" r="2" fill="#FFF" opacity="0.2"/>')

# Third small pool (east gardens)
ftn3_cx, ftn3_cy = 310, 300
add(f'<path d="{wobble_ellipse_path(ftn3_cx, ftn3_cy, 8, 6, 10)}" '
    f'fill="{WATER}" stroke="{OUTLINE}" stroke-width="{SW_MICRO}" opacity="0.35"/>')

# Steps connecting elevated sections (hatched rectangles)
steps_locations = [
    (186, 175, 28, 7), (186, 435, 28, 7),
    (118, 286, 7, 28), (275, 286, 7, 28),
    (186, 336, 28, 6), (120, 435, 7, 20), (273, 435, 7, 20),
    (186, 48, 28, 6), (186, 148, 28, 6),
]
for stx, sty, stw, sth in steps_locations:
    add(f'<path d="{wobble_path(wobble_rect(stx, sty, stw, sth), True)}" '
        f'fill="{SAND2}" stroke="{OUTLINE}" stroke-width="{SW_HAIR}" opacity="0.38"/>')
    # Step lines
    if stw > sth:
        for i in range(1, 4):
            lx = stx + stw * i / 4
            add(f'<line x1="{lx:.1f}" y1="{sty}" x2="{lx:.1f}" y2="{sty + sth}" '
                f'stroke="{OUTLINE}" stroke-width="0.35" opacity="0.22"/>')
    else:
        for i in range(1, 4):
            ly = sty + sth * i / 4
            add(f'<line x1="{stx}" y1="{ly:.1f}" x2="{stx + stw}" y2="{ly:.1f}" '
                f'stroke="{OUTLINE}" stroke-width="0.35" opacity="0.22"/>')


# ══════════════════════════════════════════════════════════════════════════
# LAYER 5 — Desert Landscape (outside walls & open areas)
# ══════════════════════════════════════════════════════════════════════════

# Scattered palm tree tops from above (star/fan shapes)
palms = [
    (42, 485), (62, 515), (350, 485), (368, 510),
    (42, 158), (362, 162), (195, 225), (205, 225),
    (28, 555), (372, 555), (95, 555), (305, 555),
    (145, 508), (258, 512), (310, 310), (90, 310),
    (200, 45), (55, 350), (345, 355),
]
for px, py in palms:
    n_fronds = random.randint(5, 8)
    frond_len = random.uniform(7, 13)
    for fi in range(n_fronds):
        angle = 2 * math.pi * fi / n_fronds + random.uniform(-0.3, 0.3)
        fx = px + frond_len * math.cos(angle)
        fy = py + frond_len * math.sin(angle)
        # Frond with slight curve
        mx = px + frond_len * 0.6 * math.cos(angle + 0.15)
        my = py + frond_len * 0.6 * math.sin(angle + 0.15)
        add(f'<path d="M{px},{py} Q{mx:.1f},{my:.1f} {fx:.1f},{fy:.1f}" '
            f'stroke="{GARDEN}" stroke-width="1.6" stroke-linecap="round" fill="none" opacity="0.45"/>')
    # Trunk center
    add(f'<circle cx="{px}" cy="{py}" r="2.2" fill="{GARDEN2}" stroke="{OUTLINE}" stroke-width="0.5" opacity="0.45"/>')

# Cactus clusters from above (small star shapes)
cacti = [
    (28, 38), (372, 38), (28, 575), (372, 575),
    (52, 442), (348, 445), (98, 155), (302, 158),
    (40, 300), (360, 300), (150, 570), (250, 570),
]
for ccx, ccy in cacti:
    arms = random.randint(3, 5)
    arm_len = random.uniform(3, 6)
    for ai in range(arms):
        angle = 2 * math.pi * ai / arms + random.uniform(-0.25, 0.25)
        ex = ccx + arm_len * math.cos(angle)
        ey = ccy + arm_len * math.sin(angle)
        add(f'<line x1="{ccx}" y1="{ccy}" x2="{ex:.1f}" y2="{ey:.1f}" '
            f'stroke="{GARDEN2}" stroke-width="1.5" stroke-linecap="round" opacity="0.38"/>')
    add(f'<circle cx="{ccx}" cy="{ccy}" r="1.5" fill="{GARDEN2}" opacity="0.35"/>')

# Ancient column ruins (circles for column bases, lines for fallen columns)
ruin_columns = [
    (52, 200, 4), (58, 215, 3.5), (68, 208, 3), (48, 210, 2.5),
    (338, 382, 4), (348, 392, 3.5), (355, 378, 3), (342, 398, 2.5),
    (70, 470, 3), (75, 478, 2.8),
]
for rx, ry, rr in ruin_columns:
    add(f'<path d="{wobble_circle_path(rx, ry, rr)}" '
        f'fill="{SAND2}" stroke="{OUTLINE}" stroke-width="{SW_HAIR}" opacity="0.32"/>')
# Fallen columns (lines for toppled)
fallen_cols = [
    ((55, 218), (78, 228)), ((345, 395), (368, 402)),
    ((50, 205), (42, 220)), ((72, 475), (88, 482)),
]
for (x1, y1), (x2, y2) in fallen_cols:
    add(f'<path d="{wobble_path([(x1, y1), (x2, y2)])}" '
        f'stroke="{SAND3}" stroke-width="2.8" stroke-linecap="round" fill="none" opacity="0.25"/>')

# Rock outcroppings (irregular brown shapes)
rocks = [
    (32, 100, 14, 9), (362, 108, 12, 8),
    (32, 480, 16, 10), (358, 478, 13, 9),
    (172, 562, 10, 7), (228, 565, 11, 6),
    (20, 250, 8, 6), (378, 250, 9, 7),
    (100, 32, 8, 6), (300, 32, 7, 5),
]
for rx, ry, rw, rh in rocks:
    n = random.randint(5, 8)
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        pts.append((rx + rw * 0.5 * math.cos(a) * random.uniform(0.5, 1.0),
                     ry + rh * 0.5 * math.sin(a) * random.uniform(0.5, 1.0)))
    add(f'<path d="{wobble_path(pts, True)}" '
        f'fill="{MESA}" stroke="{OUTLINE}" stroke-width="{SW_HAIR}" opacity="0.3"/>')
    # Highlight streak
    add(f'<path d="{wobble_path(pts[:3])}" '
        f'fill="none" stroke="{MESA2}" stroke-width="0.5" opacity="0.2"/>')

# Dried riverbed (winding tan depression, east side)
riverbed = [
    (388, 230), (375, 260), (365, 295), (360, 330),
    (365, 365), (358, 400), (362, 440), (355, 478),
]
add(f'<path d="{wobble_path(riverbed)}" stroke="{SAND3}" stroke-width="7" fill="none" opacity="0.18"/>')
add(f'<path d="{wobble_path(riverbed)}" stroke="{SAND2}" stroke-width="3.5" fill="none" opacity="0.12"/>')
# Dried riverbed cracking
for i in range(len(riverbed) - 1):
    mx = (riverbed[i][0] + riverbed[i+1][0]) / 2 + random.uniform(-5, 5)
    my = (riverbed[i][1] + riverbed[i+1][1]) / 2
    add(f'<line x1="{mx - 3:.1f}" y1="{my:.1f}" x2="{mx + 3:.1f}" y2="{my:.1f}" '
        f'stroke="{SAND4}" stroke-width="0.4" opacity="0.15"/>')

# Second dried riverbed (west approach)
riverbed2 = [
    (12, 350), (25, 380), (20, 410), (15, 445),
]
add(f'<path d="{wobble_path(riverbed2)}" stroke="{SAND3}" stroke-width="5" fill="none" opacity="0.14"/>')


# ══════════════════════════════════════════════════════════════════════════
# LAYER 6 — Details (dense, many small elements)
# ══════════════════════════════════════════════════════════════════════════

# --- Eternal flame / braziers (orange dots with glow) ---
brazier_spots = [
    (100, 290), (300, 290), (200, 180), (200, 440),
    (118, 178), (282, 178), (118, 438), (282, 438),
    (52, 290), (348, 290), (200, 58), (200, 542),
    (80, 178), (320, 178), (80, 438), (320, 438),
    (150, 290), (250, 290), (200, 245), (200, 360),
]
for bx, by in brazier_spots:
    add(f'<circle cx="{bx}" cy="{by}" r="5" fill="{FLAME}" opacity="0.06"/>')  # glow
    add(f'<circle cx="{bx}" cy="{by}" r="2.5" fill="{FLAME}" stroke="{OUTLINE}" '
        f'stroke-width="0.5" opacity="0.5"/>')
    add(f'<circle cx="{bx}" cy="{by}" r="1" fill="{FLAME2}" opacity="0.4"/>')

# --- Street lanterns along paths ---
lantern_spots = [
    (184, 248), (216, 248), (184, 352), (216, 352),
    (148, 295), (252, 295), (148, 305), (252, 305),
    (184, 148), (216, 148), (184, 452), (216, 452),
    (184, 198), (216, 198), (184, 402), (216, 402),
    (100, 178), (300, 178), (100, 438), (300, 438),
]
for lx, ly in lantern_spots:
    add(f'<circle cx="{lx}" cy="{ly}" r="1.5" fill="{FLAME2}" stroke="{OUTLINE}" '
        f'stroke-width="0.35" opacity="0.45"/>')

# --- Pottery / jar clusters (tiny circles) ---
pottery_clusters = [
    (72, 310), (128, 322), (268, 310), (328, 318),
    (78, 248), (322, 252), (148, 468), (252, 472),
    (88, 412), (312, 418), (200, 155), (145, 140),
    (255, 140), (70, 520), (330, 520),
]
for pcx, pcy in pottery_clusters:
    for _ in range(random.randint(3, 6)):
        jx = pcx + random.uniform(-6, 6)
        jy = pcy + random.uniform(-5, 5)
        jr = random.uniform(0.8, 2.2)
        c = random.choice([MESA, MESA2, MESA3])
        add(f'<circle cx="{jx:.1f}" cy="{jy:.1f}" r="{jr:.1f}" '
            f'fill="{c}" stroke="{OUTLINE}" stroke-width="0.25" opacity="0.32"/>')

# --- Small oasis garden patches (near fountains and along walls) ---
garden_patches = [
    (188, 225, 8, 6), (212, 222, 7, 5), (193, 208, 6, 5),
    (190, 505, 7, 5), (210, 508, 6, 4),
    (305, 305, 6, 5), (315, 295, 5, 4),
    (85, 315, 5, 4), (75, 305, 6, 5),
    (195, 50, 8, 5), (205, 52, 7, 4),
]
for gx, gy, gw, gh in garden_patches:
    add(f'<path d="{wobble_ellipse_path(gx, gy, gw, gh, 8)}" '
        f'fill="{GARDEN}" stroke="none" opacity="0.22"/>')
    # Tiny leaf details
    for _ in range(random.randint(2, 4)):
        lx = gx + random.uniform(-gw * 0.6, gw * 0.6)
        ly = gy + random.uniform(-gh * 0.6, gh * 0.6)
        add(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="0.8" fill="{GARDEN3}" opacity="0.18"/>')

# --- Camel caravan from above (row of small ovals with shadows) ---
# South caravan
caravan_y = 562
for ci in range(6):
    cx_ = 215 + ci * 15
    cy_ = caravan_y + random.uniform(-2, 2)
    add(f'<ellipse cx="{cx_ + 2}" cy="{cy_ + 2}" rx="5" ry="3" fill="{SHADOW}" opacity="0.12"/>')
    add(f'<ellipse cx="{cx_}" cy="{cy_}" rx="5" ry="3" fill="{SAND3}" '
        f'stroke="{OUTLINE}" stroke-width="0.5" opacity="0.42"/>')
    # Head dot
    add(f'<circle cx="{cx_ + 4}" cy="{cy_}" r="1" fill="{SAND4}" opacity="0.3"/>')

# North caravan
for ci in range(5):
    cx_ = 165 + ci * 14
    cy_ = 34 + random.uniform(-1, 1)
    add(f'<ellipse cx="{cx_ + 2}" cy="{cy_ + 2}" rx="4.5" ry="2.5" fill="{SHADOW}" opacity="0.10"/>')
    add(f'<ellipse cx="{cx_}" cy="{cy_}" rx="4.5" ry="2.5" fill="{SAND3}" '
        f'stroke="{OUTLINE}" stroke-width="0.4" opacity="0.38"/>')

# West caravan (entering west gate)
for ci in range(4):
    cx_ = 8 + ci * 12
    cy_ = 298 + random.uniform(-1, 1)
    add(f'<ellipse cx="{cx_ + 1}" cy="{cy_ + 1}" rx="3.5" ry="5" fill="{SHADOW}" opacity="0.08"/>')
    add(f'<ellipse cx="{cx_}" cy="{cy_}" rx="3.5" ry="5" fill="{SAND3}" '
        f'stroke="{OUTLINE}" stroke-width="0.4" opacity="0.35"/>')

# --- Sand texture dots (scattered randomly, more dense) ---
for _ in range(90):
    dx = random.uniform(15, 385)
    dy = random.uniform(15, 585)
    dr = random.uniform(0.2, 0.9)
    add(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="{dr:.1f}" '
        f'fill="{SAND3}" opacity="{random.uniform(0.06, 0.2):.2f}"/>')

# --- Bird shadows (V shapes) ---
birds = [
    (78, 42), (158, 28), (248, 22), (322, 38), (200, 558),
    (58, 300), (342, 312), (138, 138), (262, 148),
    (108, 470), (292, 475), (55, 210), (345, 215),
    (175, 555), (225, 552),
]
for bx, by in birds:
    bw = random.uniform(4, 8)
    add(f'<path d="M{bx - bw:.1f},{by + 2:.1f} Q{bx:.1f},{by - 2:.1f} {bx + bw:.1f},{by + 2:.1f}" '
        f'stroke="{OUTLINE}" stroke-width="0.8" fill="none" opacity="0.15"/>')

# --- Cracked earth patterns (in dry areas outside walls and riverbeds) ---
crack_zones = [
    (48, 462), (342, 458), (48, 540), (342, 542),
    (98, 562), (302, 565), (200, 578),
    (25, 360), (375, 365), (25, 240), (375, 238),
    (150, 580), (250, 580),
]
for crx, cry in crack_zones:
    # Main crack line
    cx2 = crx + random.uniform(-15, 15)
    cy2 = cry + random.uniform(-10, 10)
    add(f'<path d="{wobble_path([(crx, cry), (cx2, cy2)])}" '
        f'stroke="{SAND4}" stroke-width="0.5" fill="none" opacity="0.18"/>')
    # Branch 1
    cx3 = cx2 + random.uniform(-8, 8)
    cy3 = cy2 + random.uniform(-6, 6)
    add(f'<path d="{wobble_path([(cx2, cy2), (cx3, cy3)])}" '
        f'stroke="{SAND4}" stroke-width="0.35" fill="none" opacity="0.12"/>')
    # Branch 2
    cx4 = cx2 + random.uniform(-6, 6)
    cy4 = cy2 + random.uniform(-5, 5)
    add(f'<path d="{wobble_path([(cx2, cy2), (cx4, cy4)])}" '
        f'stroke="{SAND4}" stroke-width="0.25" fill="none" opacity="0.10"/>')

# --- Awning shadows along market streets ---
for sx in range(50, 175, 12):
    add(f'<rect x="{sx}" y="{284}" width="8" height="3" fill="{SHADOW}" opacity="0.08" rx="0.5"/>')
for sx in range(225, 370, 12):
    add(f'<rect x="{sx}" y="{314}" width="8" height="3" fill="{SHADOW}" opacity="0.08" rx="0.5"/>')
for sy in range(50, 175, 12):
    add(f'<rect x="{218}" y="{sy}" width="3" height="8" fill="{SHADOW}" opacity="0.07" rx="0.5"/>')

# --- Well / water access points ---
wells = [(98, 372), (302, 368), (148, 148), (252, 148), (200, 265)]
for wx, wy in wells:
    add(f'<path d="{wobble_circle_path(wx, wy, 4.5)}" '
        f'fill="{WATER}" stroke="{OUTLINE}" stroke-width="0.5" opacity="0.32"/>')
    add(f'<circle cx="{wx}" cy="{wy}" r="1.8" fill="{WATER2}" opacity="0.22"/>')
    # Well rim (inner circle)
    add(f'<path d="{wobble_circle_path(wx, wy, 3)}" '
        f'fill="none" stroke="{OUTLINE}" stroke-width="0.3" opacity="0.15"/>')

# --- Cross-hatching on some building roofs for texture ---
hatch_indices = [0, 3, 6, 10, 14, 18, 22, 25]
for idx in hatch_indices:
    if idx < len(flat_buildings):
        hx, hy, hw, hh = flat_buildings[idx]
        for i in range(0, hw + hh, 4):
            x1 = hx + min(i, hw)
            y1 = hy + max(0, i - hw)
            x2 = hx + max(0, i - hh)
            y2 = hy + min(i, hh)
            add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                f'stroke="{OUTLINE}" stroke-width="0.25" opacity="0.05"/>')

# --- Trade goods: amphora / barrel clusters ---
goods = [(82, 295), (318, 295), (88, 432), (312, 428),
         (155, 302), (248, 302), (72, 175), (328, 175)]
for gx, gy in goods:
    for _ in range(random.randint(2, 5)):
        ax = gx + random.uniform(-7, 7)
        ay = gy + random.uniform(-5, 5)
        add(f'<ellipse cx="{ax:.1f}" cy="{ay:.1f}" rx="2" ry="1.5" '
            f'fill="{MESA2}" stroke="{OUTLINE}" stroke-width="0.25" opacity="0.28"/>')

# --- Compass rose (upper-left corner) ---
comp_x, comp_y = 30, 22
comp_r = 9
for angle in [0, 90, 180, 270]:
    rad = math.radians(angle)
    ix = comp_x + comp_r * math.cos(rad)
    iy = comp_y + comp_r * math.sin(rad)
    add(f'<line x1="{comp_x}" y1="{comp_y}" x2="{ix:.1f}" y2="{iy:.1f}" '
        f'stroke="{OUTLINE}" stroke-width="0.7" opacity="0.18"/>')
# Diagonal lines
for angle in [45, 135, 225, 315]:
    rad = math.radians(angle)
    ix = comp_x + (comp_r - 2) * math.cos(rad)
    iy = comp_y + (comp_r - 2) * math.sin(rad)
    add(f'<line x1="{comp_x}" y1="{comp_y}" x2="{ix:.1f}" y2="{iy:.1f}" '
        f'stroke="{OUTLINE}" stroke-width="0.4" opacity="0.12"/>')
# N arrow emphasis
add(f'<path d="M{comp_x},{comp_y - comp_r} L{comp_x - 2.5},{comp_y - comp_r + 5} '
    f'L{comp_x + 2.5},{comp_y - comp_r + 5}Z" fill="{OUTLINE}" opacity="0.18"/>')

# --- Scattered coin/treasure marks (gold Ul'dah!) ---
for _ in range(12):
    tx = random.uniform(50, 350)
    ty = random.uniform(180, 420)
    add(f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="1.2" fill="{GOLD}" stroke="{OUTLINE}" '
        f'stroke-width="0.25" opacity="0.28"/>')

# --- Diagonal hatching in shadow areas for sketch feel ---
shadow_zones = [(155, 108, 32, 28), (268, 232, 22, 18), (60, 342, 18, 15), (315, 345, 20, 16)]
for sx, sy, sw, sh in shadow_zones:
    for i in range(0, sw + sh, 3):
        x1 = sx + min(i, sw)
        y1 = sy + max(0, i - sw)
        x2 = sx + max(0, i - sh)
        y2 = sy + min(i, sh)
        add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{OUTLINE}" stroke-width="0.25" opacity="0.04"/>')

# --- Dense dune ripples in open areas outside walls ---
open_areas = [
    (2, 2, 20, 28), (380, 2, 18, 28), (2, 572, 20, 26), (380, 572, 18, 26),
    (2, 200, 12, 80), (388, 200, 10, 80),
]
for ox, oy, ow, oh in open_areas:
    for i in range(0, oh, 6):
        y = oy + i
        pts = [(ox + j * 4, y + random.uniform(-0.8, 0.8)) for j in range(int(ow / 4) + 1)]
        add(f'<path d="{wobble_path(pts)}" stroke="{SAND3}" stroke-width="0.4" fill="none" opacity="0.12"/>')

# --- Tiny window dots on larger buildings ---
for bx, by, bw, bh in flat_buildings:
    if bw > 18 and bh > 18:
        n_windows = random.randint(2, 4)
        for _ in range(n_windows):
            wx = bx + random.uniform(3, bw - 3)
            wy = by + random.uniform(3, bh - 3)
            add(f'<circle cx="{wx:.1f}" cy="{wy:.1f}" r="0.6" fill="{OUTLINE}" opacity="0.12"/>')

# --- Decorative mosaic patterns at city gates ---
for gate_cx, gate_cy in [(200, 578), (200, 22)]:
    for i in range(5):
        angle = random.uniform(0, 2 * math.pi)
        dist = random.uniform(3, 10)
        mx = gate_cx + dist * math.cos(angle)
        my = gate_cy + dist * math.sin(angle)
        add(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="0.8" '
            f'fill="{random.choice([GOLD, DOME_TEAL, CARPET_RED])}" opacity="0.2"/>')

# --- Smoke wisps from braziers (wiggly lines going up/outward) ---
smoke_braziers = [(200, 300), (100, 290), (300, 290), (200, 440)]
for sx, sy in smoke_braziers:
    pts = [(sx + random.uniform(-2, 2), sy - i * 4 + random.uniform(-1.5, 1.5)) for i in range(4)]
    add(f'<path d="{wobble_path(pts)}" stroke="{SHADOW}" stroke-width="0.6" fill="none" opacity="0.08"/>')

# --- Sand dune crescents in desert areas ---
dune_crescents = [
    (25, 520, 20), (375, 520, 18), (25, 55, 15), (375, 55, 16),
    (100, 580, 12), (300, 580, 14),
]
for dcx, dcy, dr in dune_crescents:
    # Draw a crescent arc
    add(f'<path d="M{dcx - dr:.1f},{dcy} '
        f'A{dr},{dr * 0.6} 0 0 1 {dcx + dr:.1f},{dcy}" '
        f'stroke="{SAND4}" stroke-width="0.8" fill="none" opacity="0.15"/>')

# --- Tiny flag pennants on minarets and towers (additional) ---
pennant_positions = [(90, 85), (315, 83), (155, 455), (252, 451), (200, 68)]
for px, py in pennant_positions:
    # Flagpole line
    add(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{py - 8}" '
        f'stroke="{OUTLINE}" stroke-width="0.5" opacity="0.25"/>')
    # Pennant triangle
    add(f'<path d="M{px},{py - 8} L{px + 5},{py - 6} L{px},{py - 4}Z" '
        f'fill="{random.choice([GOLD, CARPET_RED, DOME_TEAL])}" stroke="{OUTLINE}" '
        f'stroke-width="0.3" opacity="0.35"/>')

# --- Wheel ruts / cart tracks on main roads ---
for y in [292, 308]:
    pts = [(x, y + random.uniform(-0.5, 0.5)) for x in range(30, 380, 15)]
    add(f'<path d="{wobble_path(pts)}" stroke="{SAND4}" stroke-width="0.4" fill="none" opacity="0.08"/>')
for x in [192, 208]:
    pts = [(x + random.uniform(-0.5, 0.5), y) for y in range(30, 580, 15)]
    add(f'<path d="{wobble_path(pts)}" stroke="{SAND4}" stroke-width="0.4" fill="none" opacity="0.08"/>')

# --- Scatter extra decorative circles along walls (bollards / posts) ---
for i in range(0, len(wall_inner) - 1, 2):
    x0, y0 = wall_inner[i]
    x1, y1 = wall_inner[(i + 1) % len(wall_inner)]
    mx = (x0 + x1) / 2
    my = (y0 + y1) / 2
    add(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="1" fill="{WALL3}" opacity="0.15"/>')

# --- Final atmosphere: subtle radial glow from eternal flame ---
add(f'<circle cx="{plaza_cx}" cy="{plaza_cy}" r="50" fill="{FLAME}" opacity="0.02"/>')

A('</svg>')

HARD = ''.join(P)

print(f"HARD SVG: ~{elem_count} drawn elements")

# ── Inject into stage.html ───────────────────────────────────────────────
pattern = r"(if\(diff==='HARD'\) return ')(.*?)(';)"
replacement = r"\g<1>" + HARD.replace('\\', '\\\\') + r"\g<3>"
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

assert new_content != content, "Injection failed — pattern not matched"
print(f"HARD SVG: {len(HARD):,} chars injected OK")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("stage.html written.")
