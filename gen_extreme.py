#!/usr/bin/env python3
"""gen_extreme.py — Radz-at-Han Tropical Bazaar: bird's-eye view graphic-recording style.

Generates an extremely dense (~200+ elements) hand-drawn sketch SVG background
depicting a tropical island bazaar seen from directly above.
Theme: Radz-at-Han (FF14 inspired).
"""
import re, math, random

random.seed(45)

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── Wobble helpers ──────────────────────────────────────────────────────
def wobble_path(points, closed=False):
    """Create a hand-drawn wobbly path through points."""
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

def wobble_circle(cx, cy, r, n=12):
    """Create a wobbly circle (hand-drawn) with n segments."""
    pts = []
    for i in range(n):
        angle = 2 * math.pi * i / n
        rr = r + random.uniform(-r*0.08, r*0.08)
        pts.append((cx + rr * math.cos(angle), cy + rr * math.sin(angle)))
    return wobble_path(pts, closed=True)

def wobble_rect(x, y, w, h):
    """Create a wobbly rectangle."""
    return wobble_path([
        (x + random.uniform(-0.5, 0.5), y + random.uniform(-0.5, 0.5)),
        (x + w + random.uniform(-0.5, 0.5), y + random.uniform(-0.5, 0.5)),
        (x + w + random.uniform(-0.5, 0.5), y + h + random.uniform(-0.5, 0.5)),
        (x + random.uniform(-0.5, 0.5), y + h + random.uniform(-0.5, 0.5)),
    ], closed=True)

def wobble_ellipse(cx, cy, rx, ry, n=16):
    """Create a wobbly ellipse."""
    pts = []
    for i in range(n):
        angle = 2 * math.pi * i / n
        rr_x = rx + random.uniform(-rx*0.06, rx*0.06)
        rr_y = ry + random.uniform(-ry*0.06, ry*0.06)
        pts.append((cx + rr_x * math.cos(angle), cy + rr_y * math.sin(angle)))
    return wobble_path(pts, closed=True)

def wave_line(y, x_start, x_end, amplitude=4, freq=18):
    """Create a wavy line."""
    pts = []
    for x in range(x_start, x_end + 1, freq):
        pts.append((x, y + random.uniform(-amplitude, amplitude)))
    return wobble_path(pts)

def concentric_rings(cx, cy, r_start, r_end, n_rings, fill_colors, stroke, sw, opacity):
    """Generate concentric ornamental rings."""
    elems = []
    for i in range(n_rings):
        t = i / max(n_rings - 1, 1)
        r = r_start + (r_end - r_start) * t
        color = fill_colors[i % len(fill_colors)]
        elems.append(f'<path d="{wobble_circle(cx, cy, r)}" fill="none" stroke="{color}" stroke-width="{sw}" opacity="{opacity}"/>')
    return elems

def palm_canopy(cx, cy, size, n_fronds=7):
    """Draw a palm tree canopy from above (star/fan radiating fronds)."""
    elems = []
    for i in range(n_fronds):
        angle = 2 * math.pi * i / n_fronds + random.uniform(-0.15, 0.15)
        length = size + random.uniform(-size*0.2, size*0.15)
        ex = cx + length * math.cos(angle)
        ey = cy + length * math.sin(angle)
        # Control point for curve
        cp_angle = angle + random.uniform(-0.3, 0.3)
        cp_dist = length * 0.6
        cpx = cx + cp_dist * math.cos(cp_angle)
        cpy = cy + cp_dist * math.sin(cp_angle)
        elems.append(f'<path d="M{cx:.1f},{cy:.1f} Q{cpx:.1f},{cpy:.1f} {ex:.1f},{ey:.1f}" '
                     f'stroke="#48A048" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.55"/>')
        # Secondary frond lines
        ex2 = cx + length * 0.85 * math.cos(angle + 0.15)
        ey2 = cy + length * 0.85 * math.sin(angle + 0.15)
        elems.append(f'<path d="M{cx:.1f},{cy:.1f} Q{cpx+2:.1f},{cpy+2:.1f} {ex2:.1f},{ey2:.1f}" '
                     f'stroke="#389038" stroke-width="1.5" fill="none" stroke-linecap="round" opacity="0.4"/>')
    # Central trunk circle
    elems.append(f'<circle cx="{cx}" cy="{cy}" r="{size*0.12}" fill="#8B6840" stroke="#2A2A2A" stroke-width="1" opacity="0.6"/>')
    return elems

# ── Build SVG ───────────────────────────────────────────────────────────
P = []
A = P.append

W, H = 400, 600
PAPER = '#F2E8E6'
OUTLINE = '#2A2A2A'
SW = 2.0
SW_BOLD = 3.0

A(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">')

# ══════════════════════════════════════════════════════════════════════════
# LAYER 1 — WATER & LAND
# ══════════════════════════════════════════════════════════════════════════

# Paper base
A(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')

# Coral tint zones (subtle warm patches on land)
for _ in range(6):
    ztx = random.randint(20, 280)
    zty = random.randint(180, 560)
    ztr = random.randint(30, 60)
    A(f'<circle cx="{ztx}" cy="{zty}" r="{ztr}" fill="#F0D8D0" opacity="0.2"/>')

# Ocean area — top portion and right side (irregular coastline)
# Build coastline as a complex curve from top-left across to right side
coast_points = [
    (0, 170), (40, 155), (80, 165), (110, 145), (140, 160),
    (175, 140), (210, 148), (250, 130), (280, 142),
    (310, 120), (340, 135), (370, 110), (400, 125),
]
# Ocean fill: polygon from coastline up to top corners
ocean_pts = [(0, 0), (400, 0)] + list(reversed(coast_points))
A(f'<path d="{wobble_path(ocean_pts, closed=True)}" fill="#60C8C8" opacity="0.3"/>')

# Deeper ocean layer (upper portion)
deep_pts = [(0, 0), (400, 0), (400, 80), (350, 75), (300, 85), (250, 70),
            (200, 80), (150, 75), (100, 85), (50, 70), (0, 80)]
A(f'<path d="{wobble_path(deep_pts, closed=True)}" fill="#40A0B0" opacity="0.2"/>')

# Dense wave lines across ocean
for wy in range(12, 165, 10):
    x_end = W if wy < 100 else int(W - (wy - 100) * 0.8)
    A(f'<path d="{wave_line(wy, 0, max(x_end, 60), 2.5, 14)}" '
      f'stroke="#40A0B0" stroke-width="0.8" fill="none" opacity="{random.uniform(0.15, 0.3):.2f}"/>')

# Foam patterns along coastline
for i, (cx, cy) in enumerate(coast_points):
    for j in range(3):
        fx = cx + random.uniform(-12, 12)
        fy = cy + random.uniform(-8, 5)
        fr = random.uniform(2, 5)
        A(f'<path d="{wobble_circle(fx, fy, fr, 8)}" fill="none" '
          f'stroke="#80D8D8" stroke-width="0.7" opacity="0.3"/>')

# Sandy beach strip along coast
for i in range(len(coast_points) - 1):
    x1, y1 = coast_points[i]
    x2, y2 = coast_points[i+1]
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    A(f'<path d="M{x1},{y1+5} Q{mx},{my+8} {x2},{y2+5}" '
      f'stroke="#E8D0B8" stroke-width="6" fill="none" opacity="0.4" stroke-linecap="round"/>')

# Harbor basin (calmer water area, top-right)
harbor_cx, harbor_cy = 350, 60
A(f'<path d="{wobble_ellipse(harbor_cx, harbor_cy, 45, 35)}" fill="#60C8C8" opacity="0.2" '
  f'stroke="#40A0B0" stroke-width="1" />')
# Harbor walls
A(f'<path d="{wobble_path([(310, 30), (310, 90), (390, 90)])}" '
  f'stroke="#A09080" stroke-width="2.5" fill="none" opacity="0.4"/>')

# Water sparkle dots (dense)
for _ in range(25):
    wx = random.randint(10, 390)
    wy = random.randint(5, 130)
    A(f'<circle cx="{wx}" cy="{wy}" r="{random.uniform(0.8, 1.5):.1f}" fill="#80D8D8" opacity="{random.uniform(0.3, 0.55):.2f}"/>')

# Coral reef patterns near shore (underwater dotted patterns)
coral_colors = ['#E08080', '#F0A070', '#D07070', '#E09060']
for _ in range(15):
    rx = random.randint(50, 350)
    ry = random.randint(100, 155)
    A(f'<circle cx="{rx}" cy="{ry}" r="{random.uniform(1.5, 3.5):.1f}" '
      f'fill="{random.choice(coral_colors)}" opacity="0.25"/>')
for _ in range(8):
    rx = random.randint(80, 330)
    ry = random.randint(105, 145)
    rw = random.uniform(5, 12)
    A(f'<path d="{wobble_circle(rx, ry, rw, 6)}" fill="none" stroke="#D08060" stroke-width="0.7" opacity="0.2"/>')

# ══════════════════════════════════════════════════════════════════════════
# LAYER 2 — TERRACED ARCHITECTURE (rooftops from above)
# ══════════════════════════════════════════════════════════════════════════

# --- Large ornate palace dome (Meghaduta) ---
palace_cx, palace_cy = 160, 250
palace_r = 35
# Outer shadow
A(f'<path d="{wobble_circle(palace_cx+2, palace_cy+2, palace_r+3)}" fill="#C0B0A0" opacity="0.2"/>')
# Main dome
A(f'<path d="{wobble_circle(palace_cx, palace_cy, palace_r)}" fill="#3878C0" stroke="{OUTLINE}" stroke-width="{SW_BOLD}" opacity="0.45"/>')
# Concentric ornamental rings
for ring_data in concentric_rings(palace_cx, palace_cy, 8, 32, 6,
                                   ['#D8A830', '#3878C0', '#D8A830', '#E8D0B8', '#D8A830', '#3878C0'],
                                   '#D8A830', 1.0, 0.4):
    A(ring_data)
# Gold finial dot
A(f'<circle cx="{palace_cx}" cy="{palace_cy}" r="4" fill="#D8A830" stroke="{OUTLINE}" stroke-width="1" opacity="0.6"/>')
# Ornamental dots around dome
for i in range(12):
    angle = 2 * math.pi * i / 12
    dx = palace_cx + 28 * math.cos(angle)
    dy = palace_cy + 28 * math.sin(angle)
    A(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="1.5" fill="#D8A830" opacity="0.45"/>')

# --- Palace rectangular base (terraced) ---
A(f'<path d="{wobble_rect(120, 220, 80, 60)}" fill="#E8D8C0" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.35"/>')
# Stepped terrace lines
for ty in [225, 235, 265, 275]:
    A(f'<path d="{wobble_path([(122, ty), (198, ty)])}" stroke="#C8B8A0" stroke-width="0.8" fill="none" opacity="0.3"/>')

# --- Medium domes (6 total) ---
medium_domes = [
    (80, 300, 18, '#3878C0'),   # left residential
    (280, 220, 16, '#2868A8'),  # right near coast
    (100, 210, 14, '#3878C0'),  # upper left
    (240, 310, 15, '#2868A8'),  # central right
    (310, 280, 13, '#3878C0'),  # far right
    (180, 370, 17, '#2868A8'),  # lower center
]
for (dx, dy, dr, dcol) in medium_domes:
    # Shadow
    A(f'<path d="{wobble_circle(dx+1.5, dy+1.5, dr+1)}" fill="#B0A090" opacity="0.15"/>')
    # Dome
    A(f'<path d="{wobble_circle(dx, dy, dr)}" fill="{dcol}" stroke="{OUTLINE}" stroke-width="1.8" opacity="0.4"/>')
    # Inner ring
    A(f'<path d="{wobble_circle(dx, dy, dr*0.5)}" fill="none" stroke="#D8A830" stroke-width="0.8" opacity="0.35"/>')
    # Gold finial
    A(f'<circle cx="{dx}" cy="{dy}" r="2" fill="#D8A830" stroke="{OUTLINE}" stroke-width="0.6" opacity="0.5"/>')

# --- Minaret tops (3 total, small circles with radiating lines) ---
minarets = [(135, 215, 6), (195, 215, 5), (265, 265, 5.5)]
for (mx, my, mr) in minarets:
    A(f'<circle cx="{mx}" cy="{my}" r="{mr}" fill="#E8D8C0" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.45"/>')
    A(f'<circle cx="{mx}" cy="{my}" r="{mr*0.4:.1f}" fill="#D8A830" opacity="0.5"/>')
    # Radiating lines
    for i in range(8):
        angle = 2 * math.pi * i / 8
        lx = mx + (mr + 3) * math.cos(angle)
        ly = my + (mr + 3) * math.sin(angle)
        A(f'<line x1="{mx + mr*0.6*math.cos(angle):.1f}" y1="{my + mr*0.6*math.sin(angle):.1f}" '
          f'x2="{lx:.1f}" y2="{ly:.1f}" stroke="#D8A830" stroke-width="0.6" opacity="0.35"/>')

# --- Terraced building rooftops (stepped rectangles) ---
buildings = [
    (50, 260, 40, 30),  (55, 330, 35, 25),  (210, 200, 50, 30),
    (270, 240, 35, 35),  (300, 310, 40, 25),  (30, 350, 45, 25),
    (220, 350, 30, 35),  (330, 340, 35, 30),  (120, 340, 40, 25),
    (260, 170, 30, 25),  (340, 190, 40, 30),  (70, 380, 35, 28),
]
building_fills = ['#E8D8C0', '#E0D0B8', '#D8C8B0', '#E8E0D0']
for i, (bx, by, bw, bh) in enumerate(buildings):
    fill = building_fills[i % len(building_fills)]
    # Shadow offset
    A(f'<path d="{wobble_rect(bx+2, by+2, bw, bh)}" fill="#C0B0A0" opacity="0.15"/>')
    # Building
    A(f'<path d="{wobble_rect(bx, by, bw, bh)}" fill="{fill}" stroke="{OUTLINE}" stroke-width="1.2" opacity="0.4"/>')
    # Internal detail lines (terrace steps)
    for s in range(1, random.randint(2, 4)):
        sy = by + bh * s / 4
        A(f'<path d="{wobble_path([(bx+2, sy), (bx+bw-2, sy)])}" '
          f'stroke="#B8A890" stroke-width="0.6" fill="none" opacity="0.3"/>')

# --- Covered walkways connecting buildings ---
walkways = [
    ((90, 275), (120, 250)),  ((200, 255), (210, 220)),
    ((155, 345), (180, 375)),  ((265, 255), (300, 320)),
    ((100, 300), (120, 340)),  ((240, 320), (270, 240)),
    ((330, 310), (345, 345)),
]
for (wx1, wy1), (wx2, wy2) in walkways:
    # Narrow covered walkway
    dx = wx2 - wx1
    dy = wy2 - wy1
    length = math.sqrt(dx*dx + dy*dy)
    if length < 1:
        continue
    nx = -dy / length * 3  # perpendicular, half-width=3
    ny = dx / length * 3
    A(f'<path d="{wobble_path([(wx1+nx, wy1+ny), (wx2+nx, wy2+ny), (wx2-nx, wy2-ny), (wx1-nx, wy1-ny)], closed=True)}" '
      f'fill="#D8C8B0" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.3"/>')

# --- Arched bridge from above (curved strip over canal) ---
A(f'<path d="{wobble_path([(145, 430), (155, 425), (165, 428), (175, 425), (185, 430)])}" '
  f'stroke="#A09080" stroke-width="5" fill="none" opacity="0.4" stroke-linecap="round"/>')
A(f'<path d="{wobble_path([(145, 430), (155, 425), (165, 428), (175, 425), (185, 430)])}" '
  f'stroke="#E8D8C0" stroke-width="3" fill="none" opacity="0.35" stroke-linecap="round"/>')

# ══════════════════════════════════════════════════════════════════════════
# LAYER 3 — MARKET & BAZAAR
# ══════════════════════════════════════════════════════════════════════════

awning_colors = ['#E05050', '#F0A030', '#3090E0', '#40B868', '#D060C0', '#E8C020']

# --- Colorful awning/tent tops (many small rectangles in rows) ---
# Left market strip
for row in range(6):
    for col in range(3):
        ax = 15 + col * 22 + random.uniform(-2, 2)
        ay = 400 + row * 18 + random.uniform(-2, 2)
        aw = random.uniform(16, 20)
        ah = random.uniform(12, 15)
        color = random.choice(awning_colors)
        A(f'<path d="{wobble_rect(ax, ay, aw, ah)}" fill="{color}" stroke="{OUTLINE}" stroke-width="1" opacity="0.45"/>')
        # Stripe detail on awning
        for s in range(2):
            sy = ay + ah * (s+1) / 3
            A(f'<line x1="{ax+1}" y1="{sy:.1f}" x2="{ax+aw-1}" y2="{sy:.1f}" '
              f'stroke="white" stroke-width="0.5" opacity="0.25"/>')

# Right market strip
for row in range(5):
    for col in range(3):
        ax = 310 + col * 22 + random.uniform(-2, 2)
        ay = 380 + row * 20 + random.uniform(-2, 2)
        aw = random.uniform(16, 20)
        ah = random.uniform(12, 15)
        color = random.choice(awning_colors)
        A(f'<path d="{wobble_rect(ax, ay, aw, ah)}" fill="{color}" stroke="{OUTLINE}" stroke-width="1" opacity="0.45"/>')
        for s in range(2):
            sy = ay + ah * (s+1) / 3
            A(f'<line x1="{ax+1}" y1="{sy:.1f}" x2="{ax+aw-1}" y2="{sy:.1f}" '
              f'stroke="white" stroke-width="0.5" opacity="0.25"/>')

# Central market area
for row in range(3):
    for col in range(4):
        ax = 130 + col * 25 + random.uniform(-3, 3)
        ay = 290 + row * 18 + random.uniform(-2, 2)
        aw = random.uniform(18, 22)
        ah = random.uniform(13, 16)
        color = random.choice(awning_colors)
        A(f'<path d="{wobble_rect(ax, ay, aw, ah)}" fill="{color}" stroke="{OUTLINE}" stroke-width="1" opacity="0.4"/>')

# --- Spice market area (colored dot clusters) ---
spice_colors = ['#D8A020', '#A06030', '#D04030', '#E0A830', '#C07020']
spice_cx, spice_cy = 100, 430
for _ in range(20):
    sx = spice_cx + random.uniform(-20, 20)
    sy = spice_cy + random.uniform(-15, 15)
    sr = random.uniform(1.5, 3.5)
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr:.1f}" fill="{random.choice(spice_colors)}" opacity="0.5"/>')
# Spice bowls (small circles as containers)
for i in range(4):
    bx = spice_cx - 12 + i * 8
    by = spice_cy + random.uniform(-3, 3)
    A(f'<path d="{wobble_circle(bx, by, 4, 8)}" fill="none" stroke="#8B6840" stroke-width="0.8" opacity="0.35"/>')

# --- Flower market area (colorful dot clusters) ---
flower_colors = ['#E06080', '#D060C0', '#F0A050', '#F07090', '#A060D0', '#E0E040']
flower_cx, flower_cy = 340, 450
for _ in range(25):
    fx = flower_cx + random.uniform(-18, 18)
    fy = flower_cy + random.uniform(-18, 18)
    fr = random.uniform(1.5, 3)
    A(f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="{fr:.1f}" fill="{random.choice(flower_colors)}" opacity="0.5"/>')

# --- Alchemical workshop area ---
alch_cx, alch_cy = 290, 360
# Vessel outlines (flasks, pots)
for i in range(6):
    vx = alch_cx + random.uniform(-15, 15)
    vy = alch_cy + random.uniform(-12, 12)
    # Small vessel shape
    A(f'<path d="{wobble_path([(vx-3, vy+4), (vx-2, vy), (vx, vy-3), (vx+2, vy), (vx+3, vy+4)], closed=True)}" '
      f'fill="none" stroke="#8B6840" stroke-width="0.8" opacity="0.35"/>')
# Colored liquids
for _ in range(5):
    lx = alch_cx + random.uniform(-12, 12)
    ly = alch_cy + random.uniform(-8, 8)
    A(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="1.5" fill="{random.choice(["#40C080", "#8040D0", "#E0C040"])}" opacity="0.4"/>')

# --- Central fountain/plaza (ornate circle with mosaic pattern) ---
fountain_cx, fountain_cy = 180, 450
fountain_r = 18
# Outer plaza circle
A(f'<path d="{wobble_circle(fountain_cx, fountain_cy, fountain_r + 8)}" fill="#E8D0B8" stroke="#C8B090" stroke-width="1.2" opacity="0.35"/>')
# Fountain basin
A(f'<path d="{wobble_circle(fountain_cx, fountain_cy, fountain_r)}" fill="#80C8D0" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.4"/>')
# Inner ring
A(f'<path d="{wobble_circle(fountain_cx, fountain_cy, 10)}" fill="none" stroke="#D8A830" stroke-width="1" opacity="0.4"/>')
A(f'<path d="{wobble_circle(fountain_cx, fountain_cy, 5)}" fill="#60B8C0" stroke="#D8A830" stroke-width="0.8" opacity="0.45"/>')
# Center jet
A(f'<circle cx="{fountain_cx}" cy="{fountain_cy}" r="2" fill="#A0E0E0" opacity="0.5"/>')
# Mosaic dots around fountain
mosaic_colors = ['#3878C0', '#D8A830', '#E05050', '#40B868', '#D060C0']
for i in range(16):
    angle = 2 * math.pi * i / 16
    mx = fountain_cx + (fountain_r + 4) * math.cos(angle)
    my = fountain_cy + (fountain_r + 4) * math.sin(angle)
    A(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="1.2" fill="{mosaic_colors[i%5]}" opacity="0.4"/>')
# Additional mosaic ring
for i in range(24):
    angle = 2 * math.pi * i / 24
    mx = fountain_cx + (fountain_r - 3) * math.cos(angle)
    my = fountain_cy + (fountain_r - 3) * math.sin(angle)
    A(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="0.8" fill="{mosaic_colors[i%5]}" opacity="0.35"/>')

# ══════════════════════════════════════════════════════════════════════════
# LAYER 4 — VEGETATION
# ══════════════════════════════════════════════════════════════════════════

# --- Palm tree canopies from above (10 total) ---
palm_positions = [
    (30, 195, 22), (370, 190, 20), (15, 320, 18), (385, 310, 17),
    (55, 490, 20), (350, 500, 19), (200, 185, 16), (120, 480, 18),
    (260, 480, 17), (300, 170, 15),
]
for px, py, ps in palm_positions:
    for elem in palm_canopy(px, py, ps):
        A(elem)

# --- Tropical flower gardens (dense colorful dot clusters) ---
garden_centers = [(45, 440), (230, 490), (310, 500), (150, 520), (80, 550)]
for gcx, gcy in garden_centers:
    for _ in range(12):
        fx = gcx + random.uniform(-12, 12)
        fy = gcy + random.uniform(-10, 10)
        fr = random.uniform(1, 2.5)
        A(f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="{fr:.1f}" '
          f'fill="{random.choice(flower_colors)}" opacity="{random.uniform(0.35, 0.55):.2f}"/>')

# --- Terraced garden beds (green rectangles with plant dots) ---
garden_beds = [(48, 260, 22, 10), (280, 245, 18, 8), (320, 340, 20, 10),
               (110, 380, 25, 10), (230, 400, 20, 8)]
for gbx, gby, gbw, gbh in garden_beds:
    A(f'<path d="{wobble_rect(gbx, gby, gbw, gbh)}" fill="#48A048" stroke="#389038" stroke-width="0.8" opacity="0.3"/>')
    # Plant dots
    for _ in range(5):
        A(f'<circle cx="{gbx + random.uniform(2, gbw-2):.1f}" cy="{gby + random.uniform(2, gbh-2):.1f}" '
          f'r="1.2" fill="#389038" opacity="0.4"/>')

# --- Hanging garden areas (green patches on building edges) ---
for bx, by, bw, bh in buildings[:6]:
    if random.random() < 0.6:
        # Green fringe on one edge
        edge = random.choice(['top', 'right'])
        if edge == 'top':
            for j in range(4):
                hx = bx + bw * j / 4 + random.uniform(0, 5)
                hy = by + random.uniform(-3, 0)
                A(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="{random.uniform(1.5, 3):.1f}" fill="#48A048" opacity="0.3"/>')
        else:
            for j in range(3):
                hx = bx + bw + random.uniform(0, 3)
                hy = by + bh * j / 3 + random.uniform(0, 5)
                A(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="{random.uniform(1.5, 3):.1f}" fill="#48A048" opacity="0.3"/>')

# --- Fruit trees (smaller round green canopies with colored fruit dots) ---
fruit_trees = [(250, 390, 8), (140, 400, 9), (350, 420, 7), (60, 415, 8), (200, 540, 9)]
fruit_colors_list = ['#E05050', '#F0A030', '#E8C020', '#D060C0']
for ftx, fty, ftr in fruit_trees:
    A(f'<path d="{wobble_circle(ftx, fty, ftr)}" fill="#48A048" stroke="#389038" stroke-width="0.8" opacity="0.35"/>')
    # Fruit dots
    for _ in range(4):
        fdx = ftx + random.uniform(-ftr*0.6, ftr*0.6)
        fdy = fty + random.uniform(-ftr*0.6, ftr*0.6)
        A(f'<circle cx="{fdx:.1f}" cy="{fdy:.1f}" r="1.2" fill="{random.choice(fruit_colors_list)}" opacity="0.45"/>')

# ══════════════════════════════════════════════════════════════════════════
# LAYER 5 — STREETS & INFRASTRUCTURE
# ══════════════════════════════════════════════════════════════════════════

# --- Winding main street with mosaic patterns ---
main_street = [
    (0, 400), (40, 395), (80, 405), (120, 395), (160, 410),
    (200, 400), (240, 408), (280, 395), (320, 405), (360, 395), (400, 402),
]
# Street fill (wide tan strip)
for i in range(len(main_street) - 1):
    x1, y1 = main_street[i]
    x2, y2 = main_street[i+1]
    A(f'<path d="M{x1},{y1-6} L{x2},{y2-6} L{x2},{y2+6} L{x1},{y1+6}Z" '
      f'fill="#E8D0B8" opacity="0.35"/>')
# Street center line
A(f'<path d="{wobble_path(main_street)}" stroke="#D8C0A0" stroke-width="1" fill="none" opacity="0.3"/>')
# Mosaic dots along street
for (sx, sy) in main_street:
    for _ in range(3):
        mx = sx + random.uniform(-5, 5)
        my = sy + random.uniform(-4, 4)
        A(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="0.8" fill="{random.choice(mosaic_colors)}" opacity="0.3"/>')

# --- Secondary winding streets ---
sec_streets = [
    [(100, 200), (105, 240), (95, 280), (100, 320), (110, 360), (120, 395)],
    [(250, 190), (255, 230), (260, 270), (255, 310), (250, 350), (240, 400)],
    [(180, 280), (175, 320), (180, 360), (180, 400), (175, 440), (180, 480)],
]
for street in sec_streets:
    A(f'<path d="{wobble_path(street)}" stroke="#D8C0A0" stroke-width="5" fill="none" opacity="0.25" stroke-linecap="round"/>')
    A(f'<path d="{wobble_path(street)}" stroke="#E8D0B8" stroke-width="3" fill="none" opacity="0.2" stroke-linecap="round"/>')

# --- Canal/waterway running through city ---
canal = [
    (120, 410), (130, 420), (145, 425), (160, 430), (175, 432),
    (190, 430), (210, 435), (230, 432), (250, 435), (270, 430),
    (290, 432), (310, 428), (330, 430), (350, 425),
]
A(f'<path d="{wobble_path(canal)}" stroke="#60C8C8" stroke-width="6" fill="none" opacity="0.35" stroke-linecap="round"/>')
A(f'<path d="{wobble_path(canal)}" stroke="#80D8D8" stroke-width="2" fill="none" opacity="0.25" stroke-linecap="round"/>')
# Small wave lines in canal
for ci in range(0, len(canal)-1, 2):
    cx1, cy1 = canal[ci]
    cx2, cy2 = canal[min(ci+1, len(canal)-1)]
    cmx = (cx1 + cx2) / 2
    cmy = (cy1 + cy2) / 2
    A(f'<path d="M{cmx-4},{cmy} Q{cmx},{cmy-2} {cmx+4},{cmy}" '
      f'stroke="#40A0B0" stroke-width="0.6" fill="none" opacity="0.25"/>')

# --- Small bridges over canal ---
bridge_positions = [(160, 430), (230, 433), (300, 430)]
for bpx, bpy in bridge_positions:
    A(f'<path d="{wobble_path([(bpx-8, bpy-5), (bpx-4, bpy-7), (bpx+4, bpy-7), (bpx+8, bpy-5)])}" '
      f'stroke="#A09080" stroke-width="3" fill="none" opacity="0.4" stroke-linecap="round"/>')
    A(f'<path d="{wobble_path([(bpx-8, bpy+5), (bpx-4, bpy+7), (bpx+4, bpy+7), (bpx+8, bpy+5)])}" '
      f'stroke="#A09080" stroke-width="3" fill="none" opacity="0.4" stroke-linecap="round"/>')

# --- Stone staircases (parallel lines going up terraces) ---
staircase_positions = [(95, 260, 'v'), (255, 230, 'v'), (115, 340, 'v'), (330, 310, 'v')]
for stx, sty, direction in staircase_positions:
    for step in range(6):
        sy = sty + step * 3
        sw = 8
        A(f'<line x1="{stx}" y1="{sy}" x2="{stx+sw}" y2="{sy}" '
          f'stroke="#A09080" stroke-width="0.8" opacity="0.3"/>')

# --- Street lantern posts (dots along streets) ---
for street in sec_streets:
    for i in range(0, len(street), 2):
        lx, ly = street[i]
        A(f'<circle cx="{lx + random.uniform(-3, 3):.1f}" cy="{ly:.1f}" r="1.5" '
          f'fill="#F0C840" stroke="{OUTLINE}" stroke-width="0.5" opacity="0.35"/>')

# --- Bunting flag lines between buildings ---
bunting_pairs = [
    ((80, 300), (120, 290)),  ((210, 200), (270, 240)),
    ((50, 330), (100, 350)),  ((300, 310), (340, 340)),
    ((180, 370), (220, 350)),  ((30, 260), (80, 260)),
    ((240, 310), (290, 290)),
]
bunting_colors = ['#E05050', '#F0A030', '#3090E0', '#40B868', '#D060C0', '#E8C020']
for (bx1, by1), (bx2, by2) in bunting_pairs:
    # String line (sagging)
    mid_x = (bx1 + bx2) / 2
    mid_y = (by1 + by2) / 2 + 4  # sag
    A(f'<path d="M{bx1},{by1} Q{mid_x},{mid_y} {bx2},{by2}" '
      f'stroke="{OUTLINE}" stroke-width="0.6" fill="none" opacity="0.25"/>')
    # Triangle flags
    dx = bx2 - bx1
    dy = by2 - by1
    length = math.sqrt(dx*dx + dy*dy)
    n_flags = max(3, int(length / 10))
    for fi in range(n_flags):
        t = (fi + 0.5) / n_flags
        fx = bx1 + dx * t
        fy = by1 + dy * t + 4 * math.sin(math.pi * t)  # sag
        color = random.choice(bunting_colors)
        A(f'<path d="M{fx-2:.1f},{fy:.1f} L{fx:.1f},{fy+4:.1f} L{fx+2:.1f},{fy:.1f}" '
          f'fill="{color}" stroke="{OUTLINE}" stroke-width="0.4" opacity="0.4"/>')

# ══════════════════════════════════════════════════════════════════════════
# LAYER 6 — DETAILS
# ══════════════════════════════════════════════════════════════════════════

# --- Boats/ships in harbor (6 total, top-down outlines) ---
boats = [
    (330, 45, 12, 4, 0.1), (360, 70, 14, 5, -0.2), (375, 40, 10, 3, 0.3),
    (340, 85, 16, 5, 0.0), (315, 55, 8, 3, -0.15), (355, 25, 11, 4, 0.2),
]
for (bx, by, bl, bw, angle) in boats:
    # Boat hull (elongated ellipse from above)
    pts = []
    for i in range(10):
        a = 2 * math.pi * i / 10
        px = bl * math.cos(a) * 0.5
        py = bw * math.sin(a) * 0.5
        # Rotate
        rx = px * math.cos(angle) - py * math.sin(angle)
        ry = px * math.sin(angle) + py * math.cos(angle)
        pts.append((bx + rx, by + ry))
    A(f'<path d="{wobble_path(pts, closed=True)}" fill="#D8C0A0" stroke="{OUTLINE}" stroke-width="1" opacity="0.4"/>')
    # Mast dot
    A(f'<circle cx="{bx}" cy="{by}" r="1" fill="{OUTLINE}" opacity="0.35"/>')

# --- Fishing nets drying (mesh patterns) ---
net_positions = [(320, 100, 20, 15), (290, 125, 18, 12)]
for (nx, ny, nw, nh) in net_positions:
    for gx in range(0, nw, 4):
        A(f'<line x1="{nx+gx}" y1="{ny}" x2="{nx+gx}" y2="{ny+nh}" '
          f'stroke="#A09080" stroke-width="0.4" opacity="0.2"/>')
    for gy in range(0, nh, 4):
        A(f'<line x1="{nx}" y1="{ny+gy}" x2="{nx+nw}" y2="{ny+gy}" '
          f'stroke="#A09080" stroke-width="0.4" opacity="0.2"/>')

# --- Seagull/tropical bird shadows (V shapes, many) ---
bird_positions = [
    (70, 25), (200, 15), (300, 30), (140, 50), (250, 55),
    (50, 80), (350, 65), (180, 90), (90, 110), (280, 100),
    (160, 550), (240, 560), (80, 570),
]
for (gx, gy) in bird_positions:
    gw = random.uniform(4, 8)
    A(f'<path d="M{gx-gw},{gy+1.5} Q{gx},{gy-1.5} {gx+gw},{gy+1.5}" '
      f'stroke="{OUTLINE}" stroke-width="0.9" fill="none" opacity="0.25"/>')

# --- Ceramic pot clusters ---
pot_clusters = [(60, 370), (280, 380), (150, 465), (220, 460)]
for pcx, pcy in pot_clusters:
    for _ in range(4):
        px = pcx + random.uniform(-6, 6)
        py = pcy + random.uniform(-5, 5)
        pr = random.uniform(2, 3.5)
        A(f'<path d="{wobble_circle(px, py, pr, 8)}" fill="#C8A070" stroke="#8B6840" stroke-width="0.7" opacity="0.35"/>')
        A(f'<circle cx="{px}" cy="{py}" r="{pr*0.4:.1f}" fill="#8B6840" opacity="0.2"/>')

# --- Rug/textile displays (tiny patterned rectangles) ---
rug_positions = [(40, 415), (70, 440), (30, 460), (55, 470), (75, 415)]
rug_colors = ['#E05050', '#3090E0', '#D060C0', '#F0A030', '#40B868']
for i, (rx, ry) in enumerate(rug_positions):
    rw = random.uniform(8, 14)
    rh = random.uniform(5, 8)
    A(f'<path d="{wobble_rect(rx, ry, rw, rh)}" fill="{rug_colors[i % 5]}" stroke="{OUTLINE}" stroke-width="0.6" opacity="0.35"/>')
    # Pattern line
    A(f'<line x1="{rx+1}" y1="{ry+rh/2:.1f}" x2="{rx+rw-1}" y2="{ry+rh/2:.1f}" '
      f'stroke="white" stroke-width="0.5" opacity="0.25"/>')
    # Border dots
    A(f'<circle cx="{rx+rw/2:.1f}" cy="{ry+1}" r="0.6" fill="#D8A830" opacity="0.3"/>')
    A(f'<circle cx="{rx+rw/2:.1f}" cy="{ry+rh-1}" r="0.6" fill="#D8A830" opacity="0.3"/>')

# --- Alchemical brazier flames (scattered) ---
brazier_positions = [(60, 310), (290, 350), (170, 500), (100, 500)]
for brx, bry in brazier_positions:
    # Brazier base
    A(f'<path d="{wobble_circle(brx, bry, 4, 8)}" fill="#C8B080" stroke="{OUTLINE}" stroke-width="1" opacity="0.4"/>')
    # Flame
    A(f'<circle cx="{brx}" cy="{bry}" r="2" fill="#E88030" opacity="0.5"/>')
    # Glow
    A(f'<circle cx="{brx}" cy="{bry}" r="5" fill="#F0A030" opacity="0.12"/>')

# --- Hanging lamps between buildings ---
lamp_positions = [(130, 300), (220, 280), (170, 340), (270, 320), (100, 350), (320, 360)]
for lx, ly in lamp_positions:
    A(f'<line x1="{lx}" y1="{ly-5}" x2="{lx}" y2="{ly}" stroke="{OUTLINE}" stroke-width="0.6" opacity="0.25"/>')
    A(f'<path d="M{lx-2.5},{ly} Q{lx},{ly+4} {lx+2.5},{ly}" fill="#F0C840" stroke="{OUTLINE}" stroke-width="0.6" opacity="0.35"/>')
    A(f'<circle cx="{lx}" cy="{ly+2}" r="1" fill="#FFE060" opacity="0.4"/>')

# --- More water sparkle in harbor ---
for _ in range(12):
    wx = random.randint(310, 390)
    wy = random.randint(25, 85)
    A(f'<circle cx="{wx}" cy="{wy}" r="{random.uniform(0.6, 1.2):.1f}" fill="white" opacity="{random.uniform(0.2, 0.4):.2f}"/>')

# --- Scattered decorative details on buildings ---
for bx, by, bw, bh in buildings:
    # Window dots on some buildings
    if random.random() < 0.5:
        for wi in range(random.randint(2, 4)):
            wx = bx + bw * (wi + 1) / (random.randint(3, 5) + 1)
            wy = by + bh * 0.4 + random.uniform(-2, 2)
            A(f'<circle cx="{wx:.1f}" cy="{wy:.1f}" r="1" fill="{OUTLINE}" opacity="0.15"/>')

# --- Additional dense decorative dots for texture ---
# Paper grain texture (subtle)
for _ in range(30):
    tx = random.randint(0, W)
    ty = random.randint(170, H)
    A(f'<circle cx="{tx}" cy="{ty}" r="0.5" fill="#D0C0B0" opacity="0.15"/>')

# --- Lower portion: more buildings and paths for density ---
# Additional small structures
extra_buildings = [
    (10, 510, 30, 20), (50, 530, 25, 22), (100, 540, 28, 18),
    (160, 530, 32, 20), (220, 535, 25, 22), (280, 530, 30, 18),
    (330, 525, 28, 25), (370, 540, 30, 20),
]
for bx, by, bw, bh in extra_buildings:
    fill = random.choice(building_fills)
    A(f'<path d="{wobble_rect(bx, by, bw, bh)}" fill="{fill}" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.3"/>')
    # Roof detail
    A(f'<path d="{wobble_path([(bx+2, by+bh/2), (bx+bw-2, by+bh/2)])}" stroke="#B8A890" stroke-width="0.5" fill="none" opacity="0.25"/>')

# --- Additional awnings in lower area ---
for _ in range(8):
    ax = random.randint(10, 370)
    ay = random.randint(500, 570)
    aw = random.uniform(12, 18)
    ah = random.uniform(8, 12)
    color = random.choice(awning_colors)
    A(f'<path d="{wobble_rect(ax, ay, aw, ah)}" fill="{color}" stroke="{OUTLINE}" stroke-width="0.7" opacity="0.35"/>')

# --- Lower street ---
lower_street = [(0, 520), (50, 525), (100, 518), (150, 525), (200, 520),
                (250, 525), (300, 518), (350, 525), (400, 520)]
A(f'<path d="{wobble_path(lower_street)}" stroke="#D8C0A0" stroke-width="4" fill="none" opacity="0.2" stroke-linecap="round"/>')

# --- Second set of bunting at top ---
for by_base in [10, 50]:
    A(f'<path d="M0,{by_base} Q200,{by_base+8} {W},{by_base}" stroke="{OUTLINE}" stroke-width="0.8" fill="none" opacity="0.2"/>')
    for bx in range(12, W, 18):
        color = random.choice(bunting_colors)
        A(f'<path d="M{bx-4},{by_base} L{bx},{by_base+6} L{bx+4},{by_base}" '
          f'fill="{color}" stroke="{OUTLINE}" stroke-width="0.4" opacity="0.35"/>')

# --- Final border texture lines (sketch feel) ---
# Top and bottom subtle sketch borders
A(f'<path d="{wobble_path([(0, 2), (100, 3), (200, 1), (300, 3), (400, 2)])}" stroke="{OUTLINE}" stroke-width="0.5" fill="none" opacity="0.1"/>')
A(f'<path d="{wobble_path([(0, 598), (100, 597), (200, 599), (300, 597), (400, 598)])}" stroke="{OUTLINE}" stroke-width="0.5" fill="none" opacity="0.1"/>')

A('</svg>')

EXTREME = ''.join(P)
elem_count = EXTREME.count('<') - 1  # subtract closing </svg>

# ── Inject into stage.html ───────────────────────────────────────────────
pattern = r"(if\(diff==='EXTREME'\) return ')(.*?)(';)"
replacement = r"\g<1>" + EXTREME.replace('\\', '\\\\') + r"\g<3>"
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

assert new_content != content, "Injection failed — pattern not matched"
print(f"EXTREME SVG: {len(EXTREME):,} chars, ~{elem_count} elements injected OK")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("stage.html written.")
