#!/usr/bin/env python3
"""gen_normal.py — Limsa Lominsa / Harbor Town — bird's-eye graphic-recording style.

Generates a dense (~200+ elements) top-down SVG background of a harbor town
with hand-drawn wobble lines on cream paper.
"""
import re, math, random

random.seed(43)  # reproducible wobble

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── Wobble helpers ─────────────────────────────────────────────────────
def wobble_path(points, closed=False):
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
    """Return a wobble_path for a rectangle (top-down rooftop, crate, etc.)."""
    return wobble_path([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], closed=True)


def wobble_circle(cx, cy, r, n=10):
    """Approximate a wobbly circle with n points."""
    pts = []
    for i in range(n):
        a = math.pi * 2 * i / n
        rf = r * (1.0 + random.uniform(-0.08, 0.08))
        pts.append((cx + rf * math.cos(a), cy + rf * math.sin(a)))
    return wobble_path(pts, closed=True)


def wave_line(y, x_start, x_end, amplitude=4, freq=20):
    pts = []
    x = x_start
    while x <= x_end:
        pts.append((x, y + random.uniform(-amplitude, amplitude)))
        x += freq + random.randint(-3, 3)
    return wobble_path(pts)


# ── Build SVG ──────────────────────────────────────────────────────────
P = []
A = P.append

W, H = 400, 600

# Palette
PAPER     = '#EDF0E8'
OCEAN1    = '#88C0E0'
OCEAN2    = '#6090B0'
OCEAN3    = '#B0D8F0'
STONE1    = '#D8C8A0'
STONE2    = '#C8B898'
WOOD1     = '#C8A870'
WOOD2     = '#A08050'
ROOF1     = '#C08850'
ROOF2     = '#B07840'
ROOF3     = '#D0A068'
STREET1   = '#D4C8B0'
STREET2   = '#C8BC9C'
LIGHTHOUSE_GLOW = '#FFD040'
OUTLINE   = '#2A2A2A'
GREEN     = '#8AB870'
GREEN2    = '#6A9850'
SAND      = '#E8D8B0'

SW = 2.2
SW_BOLD = 3.0

A(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">')

# =====================================================================
# LAYER 1 — Water & Land
# =====================================================================

# Paper base
A(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')

# --- Coastline definition ---
# Ocean occupies top + left; land occupies lower-right.
# The coastline runs roughly from top-right to bottom-left.
coast_pts = [
    (400, 0),   # start top-right corner
    (350, 30),
    (310, 80),
    (280, 130),
    (240, 170),
    (210, 220),
    (175, 270),
    (150, 310),
    (130, 350),
    (105, 400),
    (80, 450),
    (50, 510),
    (30, 560),
    (0, 600),   # end bottom-left corner
]

# Water fill — polygon covering top-left region
water_poly = [(0, 0), (400, 0)] + coast_pts + [(0, 600)]
A(f'<path d="{wobble_path(water_poly, closed=True)}" fill="{OCEAN1}" opacity="0.30"/>')

# Deeper water zone (inner, darker)
deep_pts = [(0, 0), (300, 0), (260, 60), (220, 120), (180, 180),
            (140, 240), (100, 310), (60, 400), (30, 480), (0, 550)]
A(f'<path d="{wobble_path(deep_pts, closed=True)}" fill="{OCEAN2}" opacity="0.15"/>')

# --- Dense wave line patterns (30+ lines) ---
for i in range(35):
    wy = random.randint(10, 590)
    # Only draw in water zone — approximate check
    x_coast = max(0, 400 - wy * 0.65 - random.randint(-20, 20))
    x_start = random.randint(0, max(0, int(x_coast) - 80))
    x_end = min(int(x_coast), 400)
    if x_end - x_start < 30:
        continue
    amp = random.uniform(1.5, 3.5)
    A(f'<path d="{wave_line(wy, x_start, x_end, amp, random.randint(15, 25))}" '
      f'stroke="{OCEAN2}" stroke-width="{random.uniform(0.8, 1.4):.1f}" fill="none" opacity="{random.uniform(0.2, 0.4):.2f}"/>')

# --- Rocky coastline (bold, irregular) ---
coast_wobble = [(x + random.uniform(-4, 4), y + random.uniform(-4, 4)) for x, y in coast_pts]
A(f'<path d="{wobble_path(coast_wobble)}" stroke="{OUTLINE}" stroke-width="{SW_BOLD}" fill="none" opacity="0.6"/>')

# Secondary coastline texture line
coast_inner = [(x - 6 + random.uniform(-2, 2), y + 3 + random.uniform(-2, 2)) for x, y in coast_pts]
A(f'<path d="{wobble_path(coast_inner)}" stroke="{STONE2}" stroke-width="1.5" fill="none" opacity="0.35"/>')

# --- Sandy beaches (thin tan strips along coast) ---
for i in range(0, len(coast_pts) - 1, 2):
    x1, y1 = coast_pts[i]
    x2, y2 = coast_pts[i + 1]
    bx = (x1 + x2) / 2 + random.uniform(3, 8)
    by = (y1 + y2) / 2 + random.uniform(3, 8)
    bw = random.uniform(15, 30)
    bh = random.uniform(6, 12)
    pts = [(bx, by), (bx + bw, by + 2), (bx + bw - 3, by + bh), (bx - 2, by + bh - 1)]
    A(f'<path d="{wobble_path(pts, True)}" fill="{SAND}" stroke="none" opacity="0.5"/>')

# --- Wave foam lines along coastline ---
for i in range(len(coast_pts) - 1):
    x1, y1 = coast_pts[i]
    x2, y2 = coast_pts[i + 1]
    mx = (x1 + x2) / 2 - 8 + random.uniform(-3, 3)
    my = (y1 + y2) / 2 + random.uniform(-3, 3)
    foam_pts = [(x1 - 5, y1), (mx, my), (x2 - 5, y2)]
    A(f'<path d="{wobble_path(foam_pts)}" stroke="white" stroke-width="{random.uniform(1.0, 2.0):.1f}" fill="none" opacity="0.4"/>')

# --- Land cobblestone texture (dots on land area) ---
for _ in range(60):
    lx = random.randint(50, 395)
    ly = random.randint(10, 595)
    # Check if in land zone (right of coastline)
    coast_x_at_y = max(0, 400 - ly * 0.65)
    if lx > coast_x_at_y + 20:
        r = random.uniform(0.8, 1.5)
        A(f'<circle cx="{lx}" cy="{ly}" r="{r:.1f}" fill="{STONE2}" opacity="{random.uniform(0.15, 0.3):.2f}"/>')

# --- Stone wall lines on land ---
wall_segments = [
    [(280, 100), (320, 160), (340, 250)],
    [(200, 280), (250, 330), (280, 400)],
    [(310, 300), (350, 350), (370, 420)],
    [(150, 380), (180, 430), (170, 500)],
    [(250, 450), (300, 480), (350, 520)],
]
for seg in wall_segments:
    A(f'<path d="{wobble_path(seg)}" stroke="{STONE2}" stroke-width="1.5" fill="none" opacity="0.3"/>')


# =====================================================================
# LAYER 2 — Docks & Piers (top-down wooden rectangles extending into water)
# =====================================================================

dock_data = [
    # (land_x, land_y, angle_deg, length, width)
    (270, 140, -135, 55, 12),   # pier 1 — upper
    (230, 200, -140, 50, 10),   # pier 2
    (190, 260, -130, 60, 14),   # pier 3 — main dock
    (155, 330, -125, 45, 10),   # pier 4
    (120, 400, -130, 50, 11),   # pier 5
]

for dx, dy, angle_deg, length, width in dock_data:
    rad = math.radians(angle_deg)
    # Four corners of the pier rectangle
    cos_a, sin_a = math.cos(rad), math.sin(rad)
    perp_x, perp_y = -sin_a * width / 2, cos_a * width / 2
    ex, ey = dx + cos_a * length, dy + sin_a * length

    corners = [
        (dx - perp_x, dy - perp_y),
        (ex - perp_x, ey - perp_y),
        (ex + perp_x, ey + perp_y),
        (dx + perp_x, dy + perp_y),
    ]
    A(f'<path d="{wobble_path(corners, True)}" fill="{WOOD1}" stroke="{OUTLINE}" stroke-width="1.8" opacity="0.65"/>')

    # Dock planking lines (parallel thin lines)
    for t in [0.2, 0.4, 0.6, 0.8]:
        px1 = dx + perp_x * (2 * t - 1)
        py1 = dy + perp_y * (2 * t - 1)
        px2 = ex + perp_x * (2 * t - 1)
        py2 = ey + perp_y * (2 * t - 1)
        A(f'<path d="{wobble_path([(px1, py1), (px2, py2)])}" '
          f'stroke="{WOOD2}" stroke-width="0.7" fill="none" opacity="0.4"/>')

    # Bollards on docks (small circles at end and sides)
    for bt in [0.15, 0.5, 0.85]:
        bx = dx + cos_a * length * bt + perp_x * 0.8
        by = dy + sin_a * length * bt + perp_y * 0.8
        A(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="2" fill="{WOOD2}" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.55"/>')

    # Rope coil on one dock (concentric circles)
    if random.random() < 0.5:
        rcx = dx + cos_a * length * 0.3
        rcy = dy + sin_a * length * 0.3
        A(f'<circle cx="{rcx:.1f}" cy="{rcy:.1f}" r="4" fill="none" stroke="#A08860" stroke-width="1.2" opacity="0.4"/>')
        A(f'<circle cx="{rcx:.1f}" cy="{rcy:.1f}" r="2" fill="none" stroke="#A08860" stroke-width="0.8" opacity="0.35"/>')

# Barrels and crates on docks
barrel_positions = [
    (255, 150), (258, 155), (220, 210), (185, 265), (190, 270),
    (195, 255), (148, 335), (115, 405), (110, 410),
    (260, 145), (225, 205), (152, 325),
]
for bx, by in barrel_positions:
    if random.random() < 0.5:
        # Barrel (circle from above)
        r = random.uniform(2.5, 4)
        A(f'<circle cx="{bx}" cy="{by}" r="{r:.1f}" fill="{WOOD1}" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.5"/>')
        A(f'<line x1="{bx - r + 0.5}" y1="{by}" x2="{bx + r - 0.5}" y2="{by}" stroke="{WOOD2}" stroke-width="0.5" opacity="0.4"/>')
    else:
        # Crate (square from above)
        s = random.uniform(4, 6)
        A(f'<path d="{wobble_rect(bx - s / 2, by - s / 2, s, s)}" fill="{WOOD2}" stroke="{OUTLINE}" stroke-width="0.7" opacity="0.45"/>')

# Fishing net mesh pattern on pier 3
net_x, net_y = 170, 240
for ni in range(5):
    for nj in range(3):
        nx = net_x + ni * 5 + random.uniform(-0.5, 0.5)
        ny = net_y + nj * 5 + random.uniform(-0.5, 0.5)
        A(f'<path d="M{nx:.1f},{ny:.1f} l3,3 m-3,0 l3,-3" stroke="#8A7A60" stroke-width="0.5" fill="none" opacity="0.3"/>')


# =====================================================================
# LAYER 3 — Ships & Boats (top-down view)
# =====================================================================

# --- Large ships (elongated hull outlines from above, with deck details) ---
large_ships = [
    # (cx, cy, angle_deg, hull_len, hull_w)
    (180, 100, -50, 45, 14),
    (100, 200, -30, 50, 16),
    (60, 350, -20, 40, 12),
]

for scx, scy, sa_deg, slen, sw in large_ships:
    sa = math.radians(sa_deg)
    cos_s, sin_s = math.cos(sa), math.sin(sa)

    # Pointed hull (elongated oval, pointed at bow)
    bow_x = scx + cos_s * slen / 2
    bow_y = scy + sin_s * slen / 2
    stern_x = scx - cos_s * slen / 2
    stern_y = scy - sin_s * slen / 2
    perp_sx, perp_sy = -sin_s * sw / 2, cos_s * sw / 2

    hull_pts = [
        (bow_x, bow_y),  # bow tip
        (scx + cos_s * slen * 0.15 + perp_sx, scy + sin_s * slen * 0.15 + perp_sy),
        (stern_x + perp_sx * 0.7, stern_y + perp_sy * 0.7),
        (stern_x, stern_y),  # stern
        (stern_x - perp_sx * 0.7, stern_y - perp_sy * 0.7),
        (scx + cos_s * slen * 0.15 - perp_sx, scy + sin_s * slen * 0.15 - perp_sy),
    ]
    A(f'<path d="{wobble_path(hull_pts, True)}" fill="{WOOD1}" stroke="{OUTLINE}" stroke-width="2" opacity="0.6"/>')

    # Mast dots (2-3 dots along center line)
    for mt in [0.0, 0.3, -0.25]:
        mx = scx + cos_s * slen * mt
        my = scy + sin_s * slen * mt
        A(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="2" fill="{WOOD2}" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.5"/>')

    # Deck line (center line)
    A(f'<path d="{wobble_path([(stern_x, stern_y), (bow_x, bow_y)])}" '
      f'stroke="{WOOD2}" stroke-width="0.8" fill="none" opacity="0.35"/>')

    # Cross-deck lines
    for ct in [-0.2, 0.0, 0.2]:
        cx_ = scx + cos_s * slen * ct
        cy_ = scy + sin_s * slen * ct
        A(f'<path d="{wobble_path([(cx_ + perp_sx * 0.6, cy_ + perp_sy * 0.6), (cx_ - perp_sx * 0.6, cy_ - perp_sy * 0.6)])}" '
          f'stroke="{WOOD2}" stroke-width="0.5" fill="none" opacity="0.3"/>')

    # Wake (V-shaped ripple lines behind ship / stern)
    for wi in range(1, 4):
        wake_spread = wi * 5
        wake_dist = wi * 8
        w1x = stern_x - cos_s * wake_dist + perp_sx * wake_spread / sw * 2
        w1y = stern_y - sin_s * wake_dist + perp_sy * wake_spread / sw * 2
        w2x = stern_x - cos_s * wake_dist - perp_sx * wake_spread / sw * 2
        w2y = stern_y - sin_s * wake_dist - perp_sy * wake_spread / sw * 2
        A(f'<path d="{wobble_path([(stern_x, stern_y), (w1x, w1y)])}" '
          f'stroke="{OCEAN3}" stroke-width="0.8" fill="none" opacity="{0.3 - wi * 0.05:.2f}"/>')
        A(f'<path d="{wobble_path([(stern_x, stern_y), (w2x, w2y)])}" '
          f'stroke="{OCEAN3}" stroke-width="0.8" fill="none" opacity="{0.3 - wi * 0.05:.2f}"/>')

    # Anchor chain (dotted line from bow to nearby dock area)
    chain_end_x = bow_x + random.uniform(10, 25)
    chain_end_y = bow_y + random.uniform(5, 15)
    A(f'<line x1="{bow_x:.1f}" y1="{bow_y:.1f}" x2="{chain_end_x:.1f}" y2="{chain_end_y:.1f}" '
      f'stroke="#607080" stroke-width="1" stroke-dasharray="2,3" fill="none" opacity="0.35"/>')

# --- Small fishing boats (simple oval/pointed outlines) ---
small_boats = [
    (140, 60, -40, 16, 6),
    (50, 160, -10, 14, 5),
    (90, 290, -25, 15, 5),
    (35, 440, 5, 13, 5),
    (70, 500, -15, 12, 5),
]

for bx, by, ba_deg, bl, bw in small_boats:
    ba = math.radians(ba_deg)
    cos_b, sin_b = math.cos(ba), math.sin(ba)
    bow = (bx + cos_b * bl / 2, by + sin_b * bl / 2)
    stern = (bx - cos_b * bl / 2, by - sin_b * bl / 2)
    p_bx, p_by = -sin_b * bw / 2, cos_b * bw / 2

    boat_pts = [
        bow,
        (bx + p_bx, by + p_by),
        (stern[0] + p_bx * 0.5, stern[1] + p_by * 0.5),
        stern,
        (stern[0] - p_bx * 0.5, stern[1] - p_by * 0.5),
        (bx - p_bx, by - p_by),
    ]
    A(f'<path d="{wobble_path(boat_pts, True)}" fill="{WOOD1}" stroke="{OUTLINE}" stroke-width="1.2" opacity="0.45"/>')

    # Seat line
    A(f'<path d="{wobble_path([(bx + p_bx * 0.5, by + p_by * 0.5), (bx - p_bx * 0.5, by - p_by * 0.5)])}" '
      f'stroke="{WOOD2}" stroke-width="0.6" fill="none" opacity="0.3"/>')

    # Small wake
    w_ex = stern[0] - cos_b * 6
    w_ey = stern[1] - sin_b * 6
    A(f'<path d="{wobble_path([stern, (w_ex + p_bx * 0.3, w_ey + p_by * 0.3)])}" '
      f'stroke="{OCEAN3}" stroke-width="0.6" fill="none" opacity="0.2"/>')
    A(f'<path d="{wobble_path([stern, (w_ex - p_bx * 0.3, w_ey - p_by * 0.3)])}" '
      f'stroke="{OCEAN3}" stroke-width="0.6" fill="none" opacity="0.2"/>')


# =====================================================================
# LAYER 4 — Buildings (rooftops from above, on the LAND side)
# =====================================================================

# --- Building rooftops ---
buildings = [
    # (x, y, w, h, roof_color, has_ridge)
    (300, 60, 25, 18, ROOF1, True),
    (335, 55, 20, 15, ROOF2, True),
    (360, 70, 18, 22, ROOF3, False),
    (340, 95, 22, 16, ROOF1, True),
    (310, 110, 15, 20, ROOF2, True),
    (330, 125, 18, 14, ROOF3, True),
    (355, 130, 20, 20, ROOF1, False),
    (380, 110, 18, 25, ROOF2, True),
    (285, 160, 20, 16, ROOF3, True),
    (305, 175, 22, 18, ROOF1, True),
    (330, 165, 16, 16, ROOF2, False),
    (250, 220, 24, 18, ROOF3, True),
    (278, 230, 18, 15, ROOF1, True),
    (300, 240, 20, 20, ROOF2, True),
    (330, 230, 25, 14, ROOF3, True),
    (355, 240, 16, 18, ROOF1, False),
    (220, 300, 22, 16, ROOF2, True),
    (245, 310, 18, 20, ROOF1, True),
    (270, 320, 20, 15, ROOF3, True),
    (295, 305, 24, 18, ROOF2, True),
    (320, 320, 16, 22, ROOF1, True),
    (345, 310, 22, 16, ROOF3, False),
    (200, 370, 18, 18, ROOF1, True),
    (225, 380, 20, 14, ROOF2, True),
    (250, 395, 22, 20, ROOF3, True),
    (280, 380, 18, 16, ROOF1, True),
    (305, 390, 20, 18, ROOF2, False),
    (335, 385, 24, 20, ROOF3, True),
    (360, 375, 16, 22, ROOF1, True),
    (175, 440, 20, 16, ROOF2, True),
    (200, 450, 22, 18, ROOF1, True),
    (230, 460, 18, 14, ROOF3, True),
    (260, 445, 20, 20, ROOF2, True),
    (290, 455, 24, 16, ROOF1, False),
    (320, 440, 18, 22, ROOF3, True),
    (350, 450, 20, 18, ROOF2, True),
    (160, 510, 18, 16, ROOF1, True),
    (185, 520, 22, 14, ROOF3, True),
    (215, 530, 20, 18, ROOF2, True),
    (250, 520, 24, 16, ROOF1, True),
    (280, 530, 18, 20, ROOF3, False),
    (310, 515, 22, 18, ROOF2, True),
    (340, 525, 20, 14, ROOF1, True),
    (365, 510, 16, 20, ROOF3, True),
    (145, 570, 20, 18, ROOF2, True),
    (175, 580, 18, 14, ROOF1, True),
]

for bx, by, bw, bh, color, has_ridge in buildings:
    # Rooftop rectangle
    A(f'<path d="{wobble_rect(bx, by, bw, bh)}" fill="{color}" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.6"/>')

    # Ridge line (peaked roof)
    if has_ridge:
        if bw > bh:
            # Horizontal ridge
            A(f'<path d="{wobble_path([(bx + 2, by + bh / 2), (bx + bw - 2, by + bh / 2)])}" '
              f'stroke="{OUTLINE}" stroke-width="0.8" fill="none" opacity="0.35"/>')
        else:
            # Vertical ridge
            A(f'<path d="{wobble_path([(bx + bw / 2, by + 2), (bx + bw / 2, by + bh - 2)])}" '
              f'stroke="{OUTLINE}" stroke-width="0.8" fill="none" opacity="0.35"/>')

    # Chimney (tiny square on some roofs)
    if random.random() < 0.4:
        cx_ = bx + random.uniform(3, bw - 5)
        cy_ = by + random.uniform(2, bh - 4)
        A(f'<rect x="{cx_:.1f}" y="{cy_:.1f}" width="3" height="3" fill="#888" stroke="{OUTLINE}" stroke-width="0.5" opacity="0.4"/>')

    # Rooftop garden (small green rectangle on some roofs)
    if random.random() < 0.2:
        gx = bx + random.uniform(2, bw - 8)
        gy = by + random.uniform(2, bh - 6)
        gw = random.uniform(4, 7)
        gh = random.uniform(3, 5)
        A(f'<rect x="{gx:.1f}" y="{gy:.1f}" width="{gw:.1f}" height="{gh:.1f}" rx="1" '
          f'fill="{GREEN}" stroke="none" opacity="0.35"/>')

    # Flag/banner dot on some buildings
    if random.random() < 0.25:
        fx = bx + bw / 2 + random.uniform(-2, 2)
        fy = by + random.uniform(-1, 2)
        A(f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="1.5" fill="#C85040" stroke="none" opacity="0.5"/>')
        A(f'<line x1="{fx:.1f}" y1="{fy:.1f}" x2="{fx:.1f}" y2="{fy - 4:.1f}" stroke="#8B6840" stroke-width="0.6" opacity="0.4"/>')


# --- Lighthouse from above (distinctive circle with radiating light rays) ---
lh_cx, lh_cy = 355, 42
A(f'<path d="{wobble_circle(lh_cx, lh_cy, 10, 12)}" fill="white" stroke="{OUTLINE}" stroke-width="2" opacity="0.75"/>')
A(f'<path d="{wobble_circle(lh_cx, lh_cy, 6, 8)}" fill="{LIGHTHOUSE_GLOW}" stroke="{OUTLINE}" stroke-width="1" opacity="0.6"/>')
A(f'<circle cx="{lh_cx}" cy="{lh_cy}" r="2.5" fill="{LIGHTHOUSE_GLOW}" stroke="none" opacity="0.8"/>')

# Radiating light rays
for ri in range(12):
    ra = math.pi * 2 * ri / 12
    r_inner = 11
    r_outer = 20 + random.uniform(-2, 4)
    rx1 = lh_cx + r_inner * math.cos(ra)
    ry1 = lh_cy + r_inner * math.sin(ra)
    rx2 = lh_cx + r_outer * math.cos(ra)
    ry2 = lh_cy + r_outer * math.sin(ra)
    A(f'<line x1="{rx1:.1f}" y1="{ry1:.1f}" x2="{rx2:.1f}" y2="{ry2:.1f}" '
      f'stroke="{LIGHTHOUSE_GLOW}" stroke-width="1.2" opacity="0.35"/>')

# --- Large tower/fort rooftop (bigger rectangle with battlements) ---
fort_x, fort_y, fort_w, fort_h = 365, 140, 30, 35
A(f'<path d="{wobble_rect(fort_x, fort_y, fort_w, fort_h)}" fill="{STONE1}" stroke="{OUTLINE}" stroke-width="2.5" opacity="0.6"/>')

# Battlements (small squares along edges)
for bi in range(6):
    batt_x = fort_x + bi * (fort_w / 5) - 1
    A(f'<rect x="{batt_x:.1f}" y="{fort_y - 2:.1f}" width="3" height="3" fill="{STONE2}" stroke="{OUTLINE}" stroke-width="0.6" opacity="0.4"/>')
for bi in range(6):
    batt_y = fort_y + bi * (fort_h / 5) - 1
    A(f'<rect x="{fort_x + fort_w - 1:.1f}" y="{batt_y:.1f}" width="3" height="3" fill="{STONE2}" stroke="{OUTLINE}" stroke-width="0.6" opacity="0.4"/>')

# Inner courtyard
A(f'<path d="{wobble_rect(fort_x + 6, fort_y + 6, fort_w - 12, fort_h - 12)}" '
  f'fill="{STREET1}" stroke="{OUTLINE}" stroke-width="0.8" fill-opacity="0.4" opacity="0.5"/>')

# --- Bridge from above (rectangular strip connecting two areas) ---
bridge_pts = [(240, 185), (265, 172), (290, 160), (315, 150)]
bridge_w = 8
for i in range(len(bridge_pts) - 1):
    x1, y1 = bridge_pts[i]
    x2, y2 = bridge_pts[i + 1]
    dx_ = x2 - x1
    dy_ = y2 - y1
    ln = math.sqrt(dx_ ** 2 + dy_ ** 2)
    nx, ny = -dy_ / ln * bridge_w / 2, dx_ / ln * bridge_w / 2
    seg = [(x1 + nx, y1 + ny), (x2 + nx, y2 + ny), (x2 - nx, y2 - ny), (x1 - nx, y1 - ny)]
    A(f'<path d="{wobble_path(seg, True)}" fill="{STONE1}" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.55"/>')
# Bridge railing lines
for side in [1, -1]:
    rail_pts = []
    for x, y in bridge_pts:
        dx_ = 1
        dy_ = -0.5
        ln = math.sqrt(dx_ ** 2 + dy_ ** 2)
        rail_pts.append((x + side * (-dy_ / ln * bridge_w / 2), y + side * (dx_ / ln * bridge_w / 2)))
    A(f'<path d="{wobble_path(rail_pts)}" stroke="{OUTLINE}" stroke-width="0.8" fill="none" opacity="0.35"/>')

# --- Covered market area (larger rectangle with stall divisions inside) ---
mkt_x, mkt_y, mkt_w, mkt_h = 260, 350, 35, 25
A(f'<path d="{wobble_rect(mkt_x, mkt_y, mkt_w, mkt_h)}" fill="{ROOF3}" stroke="{OUTLINE}" stroke-width="2" opacity="0.55"/>')

# Stall divisions
for si in range(1, 5):
    sx_ = mkt_x + si * (mkt_w / 5)
    A(f'<path d="{wobble_path([(sx_, mkt_y + 2), (sx_, mkt_y + mkt_h - 2)])}" '
      f'stroke="{OUTLINE}" stroke-width="0.6" fill="none" opacity="0.3"/>')
for si in range(1, 3):
    sy_ = mkt_y + si * (mkt_h / 3)
    A(f'<path d="{wobble_path([(mkt_x + 2, sy_), (mkt_x + mkt_w - 2, sy_)])}" '
      f'stroke="{OUTLINE}" stroke-width="0.6" fill="none" opacity="0.3"/>')


# =====================================================================
# LAYER 5 — Streets & Plazas
# =====================================================================

# --- Winding streets between buildings (light tan strips with dot pattern) ---
street_paths = [
    # Vertical main street
    [(320, 50), (310, 100), (295, 160), (280, 210), (265, 270), (250, 330), (235, 390), (220, 450), (200, 520), (180, 580)],
    # Horizontal streets
    [(280, 140), (310, 140), (340, 135), (370, 130)],
    [(250, 230), (280, 228), (310, 225), (340, 230), (370, 240)],
    [(220, 320), (260, 315), (300, 310), (340, 315), (380, 320)],
    [(195, 410), (230, 405), (270, 400), (310, 395), (350, 400), (390, 410)],
    [(170, 500), (210, 495), (250, 490), (290, 500), (330, 505), (370, 510)],
    # Diagonal connectors
    [(335, 100), (350, 130), (360, 160)],
    [(300, 250), (325, 280), (340, 310)],
    [(270, 400), (295, 430), (310, 460)],
]

for street in street_paths:
    # Draw street as a series of connected segments with width
    for i in range(len(street) - 1):
        x1, y1 = street[i]
        x2, y2 = street[i + 1]
        dx_ = x2 - x1
        dy_ = y2 - y1
        ln = max(math.sqrt(dx_ ** 2 + dy_ ** 2), 0.1)
        sw_ = 6  # street width
        nx, ny = -dy_ / ln * sw_ / 2, dx_ / ln * sw_ / 2
        seg = [(x1 + nx, y1 + ny), (x2 + nx, y2 + ny), (x2 - nx, y2 - ny), (x1 - nx, y1 - ny)]
        A(f'<path d="{wobble_path(seg, True)}" fill="{STREET1}" stroke="none" opacity="0.4"/>')

    # Street edge lines
    A(f'<path d="{wobble_path(street)}" stroke="{STREET2}" stroke-width="0.6" fill="none" opacity="0.3"/>')

    # Cobblestone dots along street
    for pt in street:
        for _ in range(3):
            cx_ = pt[0] + random.uniform(-4, 4)
            cy_ = pt[1] + random.uniform(-3, 3)
            A(f'<circle cx="{cx_:.1f}" cy="{cy_:.1f}" r="0.7" fill="{STONE2}" opacity="0.25"/>')

# --- Central plaza (larger open area with mosaic circle pattern) ---
plaza_cx, plaza_cy = 305, 270
plaza_r = 18
A(f'<path d="{wobble_circle(plaza_cx, plaza_cy, plaza_r, 14)}" fill="{STREET1}" stroke="{OUTLINE}" stroke-width="1.2" opacity="0.4"/>')

# Mosaic concentric circles
for pr in [14, 10, 6]:
    A(f'<path d="{wobble_circle(plaza_cx, plaza_cy, pr, 10)}" fill="none" stroke="{STONE2}" stroke-width="0.8" opacity="0.3"/>')

# Mosaic radial lines
for ri in range(8):
    ra = math.pi * 2 * ri / 8
    A(f'<line x1="{plaza_cx + 6 * math.cos(ra):.1f}" y1="{plaza_cy + 6 * math.sin(ra):.1f}" '
      f'x2="{plaza_cx + plaza_r * math.cos(ra):.1f}" y2="{plaza_cy + plaza_r * math.sin(ra):.1f}" '
      f'stroke="{STONE2}" stroke-width="0.6" opacity="0.25"/>')

# Central fountain circle
A(f'<path d="{wobble_circle(plaza_cx, plaza_cy, 3, 8)}" fill="{OCEAN3}" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.45"/>')

# --- Steps/stairs (parallel horizontal lines, connecting levels) ---
stair_groups = [
    (290, 155, 12, 0),     # near bridge
    (240, 280, 10, 15),
    (210, 360, 12, 10),
    (180, 470, 10, 5),
]
for sx_, sy_, sw_, sa_ in stair_groups:
    for si in range(4):
        lx1 = sx_ + si * 0.5
        ly_ = sy_ + si * 3
        A(f'<line x1="{lx1}" y1="{ly_}" x2="{lx1 + sw_}" y2="{ly_ + sa_ * 0.1:.1f}" '
          f'stroke="{OUTLINE}" stroke-width="0.8" opacity="0.3"/>')

# --- Street lanterns (small dots along streets) ---
lantern_positions = [
    (308, 90), (292, 180), (278, 240), (263, 300), (248, 360),
    (232, 420), (218, 480), (305, 140), (335, 228), (305, 315),
    (265, 400), (230, 495), (350, 130), (330, 280), (310, 460),
]
for lx, ly in lantern_positions:
    A(f'<circle cx="{lx}" cy="{ly}" r="1.5" fill="{LIGHTHOUSE_GLOW}" stroke="{OUTLINE}" stroke-width="0.5" opacity="0.45"/>')
    # Tiny glow
    A(f'<circle cx="{lx}" cy="{ly}" r="3" fill="{LIGHTHOUSE_GLOW}" stroke="none" opacity="0.1"/>')


# =====================================================================
# LAYER 6 — Details & Decorations
# =====================================================================

# --- Seagull shadows (tiny V shapes) ---
seagull_positions = [
    (80, 50), (160, 35), (30, 120), (120, 150), (50, 250),
    (90, 380), (40, 480), (200, 100), (25, 560), (110, 450),
    (65, 320), (150, 520),
]
for gx, gy in seagull_positions:
    gw = random.uniform(4, 7)
    ga = random.uniform(-0.3, 0.3)  # slight rotation
    A(f'<path d="M{gx - gw:.1f},{gy + 2:.1f} Q{gx:.1f},{gy - 1:.1f} {gx + gw:.1f},{gy + 2:.1f}" '
      f'stroke="{OUTLINE}" stroke-width="1" fill="none" opacity="0.3"/>')

# --- Barrel/crate clusters on streets ---
street_stuff = [
    (300, 100), (285, 200), (270, 280), (240, 350), (225, 420),
    (210, 490), (350, 230), (330, 310), (310, 400),
]
for sx_, sy_ in street_stuff:
    if random.random() < 0.5:
        s = random.uniform(2.5, 4)
        A(f'<rect x="{sx_:.1f}" y="{sy_:.1f}" width="{s:.1f}" height="{s:.1f}" '
          f'fill="{WOOD2}" stroke="{OUTLINE}" stroke-width="0.5" opacity="0.35"/>')
    else:
        A(f'<circle cx="{sx_}" cy="{sy_}" r="{random.uniform(2, 3):.1f}" '
          f'fill="{WOOD1}" stroke="{OUTLINE}" stroke-width="0.5" opacity="0.35"/>')

# --- Anchor doodle decoration (on a dock area) ---
anc_x, anc_y = 200, 245
A(f'<line x1="{anc_x}" y1="{anc_y}" x2="{anc_x}" y2="{anc_y + 10}" stroke="#607080" stroke-width="1.5" opacity="0.35"/>')
A(f'<path d="M{anc_x - 5},{anc_y + 10} Q{anc_x},{anc_y + 14} {anc_x + 5},{anc_y + 10}" stroke="#607080" stroke-width="1.2" fill="none" opacity="0.35"/>')
A(f'<line x1="{anc_x - 4}" y1="{anc_y + 2}" x2="{anc_x + 4}" y2="{anc_y + 2}" stroke="#607080" stroke-width="1.2" opacity="0.35"/>')
A(f'<circle cx="{anc_x}" cy="{anc_y - 2}" r="2" fill="none" stroke="#607080" stroke-width="1" opacity="0.35"/>')

# Second anchor decoration
anc2_x, anc2_y = 130, 370
A(f'<line x1="{anc2_x}" y1="{anc2_y}" x2="{anc2_x}" y2="{anc2_y + 8}" stroke="#607080" stroke-width="1.2" opacity="0.3"/>')
A(f'<path d="M{anc2_x - 4},{anc2_y + 8} Q{anc2_x},{anc2_y + 11} {anc2_x + 4},{anc2_y + 8}" stroke="#607080" stroke-width="1" fill="none" opacity="0.3"/>')
A(f'<line x1="{anc2_x - 3}" y1="{anc2_y + 1}" x2="{anc2_x + 3}" y2="{anc2_y + 1}" stroke="#607080" stroke-width="1" opacity="0.3"/>')
A(f'<circle cx="{anc2_x}" cy="{anc2_y - 1.5}" r="1.5" fill="none" stroke="#607080" stroke-width="0.8" opacity="0.3"/>')

# --- Water sparkle dots (25+) ---
for _ in range(30):
    wx = random.randint(5, 350)
    wy = random.randint(5, 590)
    coast_x_at_y = max(0, 400 - wy * 0.65)
    if wx < coast_x_at_y - 5:
        r = random.uniform(0.6, 1.2)
        A(f'<circle cx="{wx}" cy="{wy}" r="{r:.1f}" fill="{OCEAN3}" opacity="{random.uniform(0.3, 0.55):.2f}"/>')

# --- Small garden patches between buildings ---
garden_patches = [
    (325, 90, 8, 6), (315, 200, 10, 5), (290, 290, 7, 8),
    (260, 370, 9, 6), (240, 435, 8, 7), (310, 470, 10, 5),
    (210, 510, 7, 6), (350, 360, 6, 8), (270, 470, 8, 5),
]
for gx, gy, gw, gh in garden_patches:
    A(f'<path d="{wobble_rect(gx, gy, gw, gh)}" fill="{GREEN}" stroke="none" opacity="0.25"/>')
    # Tiny tree dots
    for _ in range(random.randint(2, 4)):
        tx = gx + random.uniform(1, gw - 1)
        ty = gy + random.uniform(1, gh - 1)
        A(f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="{random.uniform(1.2, 2.0):.1f}" fill="{GREEN2}" stroke="none" opacity="0.3"/>')

# --- Additional water detail: current/flow lines ---
for _ in range(10):
    wy = random.randint(50, 550)
    coast_x_at_y = max(0, 400 - wy * 0.65)
    wx_start = random.randint(5, max(10, int(coast_x_at_y) - 60))
    wx_end = min(wx_start + random.randint(20, 50), int(coast_x_at_y) - 5)
    if wx_end > wx_start + 10:
        pts = [(wx_start, wy)]
        for _ in range(3):
            pts.append((pts[-1][0] + random.uniform(8, 15), wy + random.uniform(-2, 2)))
        A(f'<path d="{wobble_path(pts)}" stroke="{OCEAN2}" stroke-width="0.6" fill="none" opacity="0.2"/>')

# --- Compass rose doodle (small, in water area) ---
comp_x, comp_y = 40, 55
comp_r = 8
for ci in range(4):
    ca = math.pi / 2 * ci
    A(f'<line x1="{comp_x:.1f}" y1="{comp_y:.1f}" '
      f'x2="{comp_x + comp_r * math.cos(ca):.1f}" y2="{comp_y + comp_r * math.sin(ca):.1f}" '
      f'stroke="{OUTLINE}" stroke-width="0.8" opacity="0.25"/>')
for ci in range(4):
    ca = math.pi / 4 + math.pi / 2 * ci
    A(f'<line x1="{comp_x:.1f}" y1="{comp_y:.1f}" '
      f'x2="{comp_x + comp_r * 0.6 * math.cos(ca):.1f}" y2="{comp_y + comp_r * 0.6 * math.sin(ca):.1f}" '
      f'stroke="{OUTLINE}" stroke-width="0.5" opacity="0.2"/>')
A(f'<circle cx="{comp_x}" cy="{comp_y}" r="1.5" fill="{OUTLINE}" stroke="none" opacity="0.2"/>')
# N marker
A(f'<circle cx="{comp_x}" cy="{comp_y - comp_r - 2}" r="1" fill="{OUTLINE}" opacity="0.2"/>')

# --- Buoy markers in water ---
buoy_positions = [(120, 80), (80, 170), (55, 290), (30, 400)]
for bx_, by_ in buoy_positions:
    A(f'<circle cx="{bx_}" cy="{by_}" r="2.5" fill="#C85040" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.4"/>')
    A(f'<circle cx="{bx_}" cy="{by_}" r="4.5" fill="none" stroke="#C85040" stroke-width="0.5" opacity="0.2"/>')

# --- Final paper texture: faint grid overlay ---
for gx_ in range(0, W, 40):
    A(f'<line x1="{gx_}" y1="0" x2="{gx_}" y2="{H}" stroke="#C8C8C0" stroke-width="0.3" opacity="0.12"/>')
for gy_ in range(0, H, 40):
    A(f'<line x1="0" y1="{gy_}" x2="{W}" y2="{gy_}" stroke="#C8C8C0" stroke-width="0.3" opacity="0.12"/>')

A('</svg>')

NORMAL = ''.join(P)

# ── Count elements for verification ──
elem_count = NORMAL.count('<') - NORMAL.count('</') - 1  # -1 for <svg>
print(f"NORMAL SVG element count: ~{elem_count}")

# ── Inject into stage.html ─────────────────────────────────────────────
pattern = r"(if\(diff==='NORMAL'\) return ')(.*?)(';)"
replacement = r"\g<1>" + NORMAL.replace('\\', '\\\\') + r"\g<3>"
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

assert new_content != content, "Injection failed — pattern not matched"
print(f"NORMAL SVG: {len(NORMAL):,} chars injected OK")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("stage.html written.")
