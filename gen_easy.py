#!/usr/bin/env python3
"""gen_easy.py — Gridania / Sacred Forest: bird's-eye graphic-recording style.

Extremely dense top-down illustration (200+ SVG elements).
Hand-drawn wobbly lines on cream paper texture.
"""
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
    """Generate a cloud-like canopy shape (bumpy ellipse) for top-down trees."""
    pts = []
    for i in range(bumps * 2):
        angle = math.pi * 2 * i / (bumps * 2)
        r_factor = 1.0 + random.uniform(-0.15, 0.18)
        x = cx + rx * r_factor * math.cos(angle)
        y = cy + ry * r_factor * math.sin(angle)
        pts.append((x, y))
    return wobble_path(pts, closed=True)


def wobble_circle(cx, cy, r, bumps=8):
    """A slightly wobbly circle (for stones, stumps, etc)."""
    pts = []
    for i in range(bumps):
        angle = math.pi * 2 * i / bumps
        rf = r * (1.0 + random.uniform(-0.1, 0.1))
        pts.append((cx + rf * math.cos(angle), cy + rf * math.sin(angle)))
    return wobble_path(pts, closed=True)


def wobble_ellipse(cx, cy, rx, ry, bumps=10):
    """A wobbly ellipse."""
    pts = []
    for i in range(bumps):
        angle = math.pi * 2 * i / bumps
        rxf = rx * (1.0 + random.uniform(-0.1, 0.1))
        ryf = ry * (1.0 + random.uniform(-0.1, 0.1))
        pts.append((cx + rxf * math.cos(angle), cy + ryf * math.sin(angle)))
    return wobble_path(pts, closed=True)


def wobble_rect(x, y, w, h):
    """A wobbly rectangle from top-left corner."""
    pts = [
        (x + random.uniform(-1, 1), y + random.uniform(-1, 1)),
        (x + w + random.uniform(-1, 1), y + random.uniform(-1, 1)),
        (x + w + random.uniform(-1, 1), y + h + random.uniform(-1, 1)),
        (x + random.uniform(-1, 1), y + h + random.uniform(-1, 1)),
    ]
    return wobble_path(pts, closed=True)


# ── Build SVG ───────────────────────────────────────────────────────────
P = []
A = P.append

W, H = 400, 600
PAPER = '#F0EDE0'
OUTLINE = '#2A2A2A'
SW = 2.0
SW_BOLD = 3.0

# Color palettes
GREENS = ['#4A8838', '#6BA854', '#8CC870', '#3A6828', '#2D5420']
DARK_GREENS = ['#2D5420', '#3A6828', '#325A22']
MID_GREENS = ['#4A8838', '#6BA854', '#508C40']
LIGHT_GREENS = ['#8CC870', '#9AD880', '#A0E088']
BROWNS = ['#8B6840', '#A08050', '#6B5030']
PATH_COLORS = ['#C8B090', '#D4C4A0']
STREAM_COLORS = ['#60A8C8', '#88C0D8']
FLOWER_COLORS = ['#E8A040', '#E06080', '#D070C0', '#60A0E0', '#F0D060']

A(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">')

# ═══════════════════════════════════════════════════════════════════════
# LAYER 1: GROUND / BASE
# ═══════════════════════════════════════════════════════════════════════

# Paper background
A(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')

# --- Green wash zones (forest floor visible from above) ---
wash_zones = [
    (0, 0, 180, 250, '#D8E8C8', 0.4),
    (150, 100, 250, 300, '#D0E4C0', 0.35),
    (250, 0, 150, 200, '#D4E6C4', 0.38),
    (0, 300, 200, 200, '#CCE0B8', 0.32),
    (200, 350, 200, 250, '#D2E6C0', 0.36),
    (50, 200, 300, 150, '#C8DEB4', 0.25),
]
for wx, wy, ww, wh, wc, wo in wash_zones:
    A(f'<path d="{wobble_ellipse(wx + ww/2, wy + wh/2, ww/2, wh/2, 12)}" '
      f'fill="{wc}" opacity="{wo}"/>')

# --- Small clearings (lighter green patches) ---
clearings = [
    (120, 180, 35, 28), (280, 120, 30, 25), (200, 350, 40, 30),
    (60, 420, 25, 20), (330, 450, 30, 22),
]
for clx, cly, clrx, clry in clearings:
    A(f'<path d="{wobble_ellipse(clx, cly, clrx, clry, 8)}" '
      f'fill="#E0ECD0" opacity="0.5"/>')

# --- Dirt / stone paths winding through the forest (top-down) ---
# Main path (goes roughly from bottom-center up and curves left)
main_path_pts = [
    (200, 600), (195, 570), (188, 540), (180, 510), (170, 480),
    (155, 450), (140, 420), (130, 390), (125, 360), (128, 330),
    (135, 300), (145, 270), (155, 240), (160, 210), (158, 180),
    (150, 150), (140, 120), (135, 90), (140, 60), (150, 30), (155, 0),
]
# Draw path as a thick wobbly strip
for offset in [-10, 10]:
    side_pts = [(x + offset + random.uniform(-2, 2), y + random.uniform(-1, 1))
                for x, y in main_path_pts]
    A(f'<path d="{wobble_path(side_pts)}" stroke="#B8A078" stroke-width="1.2" fill="none" opacity="0.5"/>')
# Fill between with tan color
path_fill_pts = []
for x, y in main_path_pts:
    path_fill_pts.append((x + random.uniform(-8, -6), y))
for x, y in reversed(main_path_pts):
    path_fill_pts.append((x + random.uniform(6, 8), y))
A(f'<path d="{wobble_path(path_fill_pts, closed=True)}" fill="#C8B090" opacity="0.6" stroke="none"/>')

# Secondary path (branches right from main)
sec_path_pts = [
    (145, 270), (160, 265), (180, 260), (210, 258), (240, 260),
    (270, 265), (300, 275), (330, 290), (355, 310), (375, 330),
    (390, 350), (400, 370),
]
sec_fill = []
for x, y in sec_path_pts:
    sec_fill.append((x + random.uniform(-6, -4), y + random.uniform(-5, -3)))
for x, y in reversed(sec_path_pts):
    sec_fill.append((x + random.uniform(4, 6), y + random.uniform(3, 5)))
A(f'<path d="{wobble_path(sec_fill, closed=True)}" fill="#D4C4A0" opacity="0.55" stroke="none"/>')
for offset in [-6, 6]:
    side = [(x + random.uniform(-1, 1), y + offset + random.uniform(-1, 1))
            for x, y in sec_path_pts]
    A(f'<path d="{wobble_path(side)}" stroke="#B8A078" stroke-width="1" fill="none" opacity="0.4"/>')

# Small path (branches left near bottom)
small_path_pts = [
    (170, 480), (145, 475), (120, 468), (90, 460), (60, 455),
    (30, 452), (0, 450),
]
sm_fill = []
for x, y in small_path_pts:
    sm_fill.append((x + random.uniform(-1, 1), y - 5 + random.uniform(-1, 1)))
for x, y in reversed(small_path_pts):
    sm_fill.append((x + random.uniform(-1, 1), y + 5 + random.uniform(-1, 1)))
A(f'<path d="{wobble_path(sm_fill, closed=True)}" fill="#C8B090" opacity="0.5" stroke="none"/>')

# --- Stone stepping path (row of small circles along a diagonal) ---
step_stones = [
    (250, 400), (260, 390), (272, 382), (285, 375), (298, 370),
    (312, 365), (325, 362), (340, 360), (355, 358),
]
for sx, sy in step_stones:
    r = random.uniform(3.5, 5.5)
    A(f'<path d="{wobble_circle(sx, sy, r, 6)}" fill="#C0B498" stroke="{OUTLINE}" '
      f'stroke-width="0.8" opacity="0.6"/>')

# --- Winding stream / river (top-down, blue) ---
stream_center = [
    (0, 200), (30, 195), (60, 188), (90, 185), (120, 190),
    (150, 200), (175, 215), (195, 235), (210, 260), (220, 290),
    (228, 320), (235, 350), (245, 380), (260, 405), (280, 425),
    (305, 440), (335, 448), (365, 450), (400, 448),
]
# Stream fill (wider)
stream_left = [(x + random.uniform(-1, 1), y - 10 + random.uniform(-2, 2))
               for x, y in stream_center]
stream_right = [(x + random.uniform(-1, 1), y + 10 + random.uniform(-2, 2))
                for x, y in reversed(stream_center)]
A(f'<path d="{wobble_path(stream_left + stream_right, closed=True)}" '
  f'fill="#88C0D8" opacity="0.45" stroke="none"/>')
# Stream banks
for offset, color in [(-10, '#60A8C8'), (10, '#60A8C8')]:
    bank = [(x + random.uniform(-1.5, 1.5), y + offset + random.uniform(-1.5, 1.5))
            for x, y in stream_center]
    A(f'<path d="{wobble_path(bank)}" stroke="{color}" stroke-width="1.8" fill="none" opacity="0.6"/>')
# Ripple lines inside stream
for i in range(0, len(stream_center) - 1, 2):
    x, y = stream_center[i]
    rlen = random.uniform(8, 14)
    A(f'<line x1="{x - rlen/2}" y1="{y}" x2="{x + rlen/2}" y2="{y}" '
      f'stroke="#A0D4E8" stroke-width="1" stroke-linecap="round" opacity="0.5"/>')

# ═══════════════════════════════════════════════════════════════════════
# LAYER 2: TREES (bird's-eye canopies - DENSEST LAYER)
# ═══════════════════════════════════════════════════════════════════════

# Tree data: (cx, cy, canopy_rx, canopy_ry, color_idx, bumps)
# Large trees (30-40)
large_trees = [
    (25, 35, 28, 25), (75, 25, 32, 28), (15, 95, 30, 26),
    (60, 80, 26, 24), (5, 160, 27, 24), (50, 150, 30, 28),
    (20, 230, 28, 25), (65, 220, 25, 23), (10, 310, 30, 27),
    (55, 340, 28, 26), (25, 400, 26, 24), (70, 440, 30, 28),
    (15, 510, 28, 25), (60, 520, 26, 24), (30, 570, 30, 27),
    # Right edge
    (375, 40, 30, 26), (340, 55, 28, 25), (385, 110, 27, 24),
    (350, 130, 30, 28), (380, 190, 28, 26), (345, 210, 26, 24),
    (390, 270, 30, 27), (355, 300, 28, 25), (375, 400, 26, 24),
    (340, 420, 30, 28), (385, 480, 28, 25), (350, 500, 27, 24),
    (375, 560, 30, 27), (340, 580, 28, 26),
    # Interior large
    (110, 60, 26, 24), (290, 70, 28, 25), (100, 140, 25, 23),
    (300, 160, 27, 25), (95, 520, 26, 24), (310, 520, 28, 26),
    (200, 50, 24, 22), (250, 500, 26, 24),
]

# Medium trees (20+)
medium_trees = [
    (105, 310, 18, 16), (290, 340, 20, 18), (180, 130, 19, 17),
    (230, 100, 17, 16), (270, 200, 20, 18), (100, 250, 18, 16),
    (310, 250, 19, 17), (180, 440, 20, 18), (230, 460, 18, 16),
    (320, 380, 17, 16), (85, 380, 19, 17), (160, 550, 18, 16),
    (280, 560, 20, 18), (140, 40, 17, 15), (260, 30, 18, 16),
    (330, 160, 19, 17), (70, 290, 17, 16), (200, 160, 18, 16),
    (120, 470, 19, 17), (350, 340, 17, 16), (40, 480, 18, 16),
    (390, 540, 17, 15),
]

# Small/young trees (15+)
small_trees = [
    (130, 200, 11, 10), (250, 180, 12, 11), (170, 320, 10, 9),
    (230, 340, 11, 10), (190, 490, 12, 11), (270, 470, 10, 9),
    (110, 430, 11, 10), (320, 430, 12, 11), (160, 100, 10, 9),
    (240, 140, 11, 10), (90, 200, 10, 9), (330, 230, 11, 10),
    (200, 580, 12, 11), (360, 470, 10, 9), (30, 350, 11, 10),
    (280, 300, 10, 9), (370, 150, 11, 10),
]

# Draw all trees: shadow first, then canopy, then optional trunk dot
def draw_tree(cx, cy, rx, ry, size_class='large'):
    """Draw a single tree canopy from above with shadow."""
    # Pick color based on size
    if size_class == 'large':
        fill = random.choice(MID_GREENS + DARK_GREENS)
        highlight = random.choice(LIGHT_GREENS)
        bumps = random.randint(8, 12)
        outline_w = 2.0
        shadow_off = random.uniform(3, 5)
    elif size_class == 'medium':
        fill = random.choice(MID_GREENS)
        highlight = random.choice(LIGHT_GREENS)
        bumps = random.randint(6, 9)
        outline_w = 1.6
        shadow_off = random.uniform(2, 4)
    else:
        fill = random.choice(LIGHT_GREENS + MID_GREENS)
        highlight = random.choice(LIGHT_GREENS)
        bumps = random.randint(5, 7)
        outline_w = 1.2
        shadow_off = random.uniform(1.5, 3)

    # Shadow (offset, darker)
    A(f'<path d="{cloud_canopy(cx + shadow_off, cy + shadow_off, rx, ry, bumps)}" '
      f'fill="#1A3010" opacity="0.15" stroke="none"/>')
    # Main canopy
    A(f'<path d="{cloud_canopy(cx, cy, rx, ry, bumps)}" '
      f'fill="{fill}" stroke="{OUTLINE}" stroke-width="{outline_w}" opacity="0.85"/>')
    # Inner highlight blob
    hx = cx + random.uniform(-rx*0.3, rx*0.2)
    hy = cy + random.uniform(-ry*0.3, ry*0.2)
    A(f'<path d="{cloud_canopy(hx, hy, rx*0.5, ry*0.5, max(4, bumps-3))}" '
      f'fill="{highlight}" stroke="none" opacity="0.35"/>')
    # Trunk dot (visible through canopy gap, some trees only)
    if random.random() < 0.4:
        tr = random.uniform(2, 3.5) if size_class == 'large' else random.uniform(1.5, 2.5)
        A(f'<circle cx="{cx + random.uniform(-2, 2)}" cy="{cy + random.uniform(-2, 2)}" r="{tr}" '
          f'fill="#6B5030" opacity="0.5"/>')

# Draw in order: large (back), medium, small (front)
for cx, cy, rx, ry in large_trees:
    draw_tree(cx, cy, rx, ry, 'large')

for cx, cy, rx, ry in medium_trees:
    draw_tree(cx, cy, rx, ry, 'medium')

for cx, cy, rx, ry in small_trees:
    draw_tree(cx, cy, rx, ry, 'small')

# ═══════════════════════════════════════════════════════════════════════
# LAYER 3: STRUCTURES & FEATURES (seen from above)
# ═══════════════════════════════════════════════════════════════════════

# --- Torii gates (seen from above: two post dots + bar between) ---
torii_gates = [(150, 155, 0.3), (270, 265, -0.2), (135, 400, 0.5)]
for tx, ty, angle in torii_gates:
    ca, sa = math.cos(angle), math.sin(angle)
    # Two post dots (red circles)
    post_dist = 12
    p1x, p1y = tx - post_dist * ca, ty - post_dist * sa
    p2x, p2y = tx + post_dist * ca, ty + post_dist * sa
    A(f'<circle cx="{p1x:.1f}" cy="{p1y:.1f}" r="3" fill="#C85040" stroke="{OUTLINE}" stroke-width="1.2"/>')
    A(f'<circle cx="{p2x:.1f}" cy="{p2y:.1f}" r="3" fill="#C85040" stroke="{OUTLINE}" stroke-width="1.2"/>')
    # Cross beam (top bar connecting posts)
    bx1, by1 = tx - (post_dist + 5) * ca, ty - (post_dist + 5) * sa
    bx2, by2 = tx + (post_dist + 5) * ca, ty + (post_dist + 5) * sa
    A(f'<line x1="{bx1:.1f}" y1="{by1:.1f}" x2="{bx2:.1f}" y2="{by2:.1f}" '
      f'stroke="#C85040" stroke-width="3" stroke-linecap="round" opacity="0.85"/>')
    # Inner beam
    A(f'<line x1="{p1x:.1f}" y1="{p1y:.1f}" x2="{p2x:.1f}" y2="{p2y:.1f}" '
      f'stroke="#B04838" stroke-width="2" stroke-linecap="round" opacity="0.7"/>')

# --- Small shrine building (top-down footprint) ---
shrine_x, shrine_y = 275, 155
# Base platform
A(f'<path d="{wobble_rect(shrine_x - 18, shrine_y - 14, 36, 28)}" '
  f'fill="#C8A870" stroke="{OUTLINE}" stroke-width="1.8" opacity="0.75"/>')
# Inner area (slightly darker)
A(f'<path d="{wobble_rect(shrine_x - 12, shrine_y - 9, 24, 18)}" '
  f'fill="#B89860" stroke="{OUTLINE}" stroke-width="1.2" opacity="0.6"/>')
# Roof ridge line (peaked)
A(f'<line x1="{shrine_x}" y1="{shrine_y - 16}" x2="{shrine_x}" y2="{shrine_y + 16}" '
  f'stroke="{OUTLINE}" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>')
# Roof edges
A(f'<line x1="{shrine_x - 20}" y1="{shrine_y}" x2="{shrine_x}" y2="{shrine_y - 16}" '
  f'stroke="{OUTLINE}" stroke-width="1" opacity="0.4"/>')
A(f'<line x1="{shrine_x + 20}" y1="{shrine_y}" x2="{shrine_x}" y2="{shrine_y - 16}" '
  f'stroke="{OUTLINE}" stroke-width="1" opacity="0.4"/>')

# --- Bridges over stream (rectangular platforms from above) ---
bridges = [
    (90, 185, 22, 12, 0.1),   # near top-left stream
    (210, 255, 18, 10, 0.4),   # mid stream
    (280, 425, 20, 11, -0.1),  # lower stream
]
for bx, by, bw, bh, ba in bridges:
    # Bridge deck
    ca, sa = math.cos(ba), math.sin(ba)
    corners = [
        (bx - bw/2*ca + bh/2*sa, by - bw/2*sa - bh/2*ca),
        (bx + bw/2*ca + bh/2*sa, by + bw/2*sa - bh/2*ca),
        (bx + bw/2*ca - bh/2*sa, by + bw/2*sa + bh/2*ca),
        (bx - bw/2*ca - bh/2*sa, by - bw/2*sa + bh/2*ca),
    ]
    A(f'<path d="{wobble_path(corners, closed=True)}" '
      f'fill="#C8A870" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.8"/>')
    # Plank lines
    for t in [0.3, 0.5, 0.7]:
        lx = bx + (t - 0.5) * bw * ca
        ly = by + (t - 0.5) * bw * sa
        A(f'<line x1="{lx - bh/2*sa:.1f}" y1="{ly + bh/2*ca:.1f}" '
          f'x2="{lx + bh/2*sa:.1f}" y2="{ly - bh/2*ca:.1f}" '
          f'stroke="#A08050" stroke-width="0.8" opacity="0.5"/>')

# --- Wooden platforms / decks ---
platforms = [
    (70, 290, 30, 22),
    (320, 310, 28, 20),
    (190, 395, 24, 18),
]
for px, py, pw, ph in platforms:
    A(f'<path d="{wobble_rect(px - pw/2, py - ph/2, pw, ph)}" '
      f'fill="#C8A870" stroke="{OUTLINE}" stroke-width="1.5" opacity="0.65"/>')
    # Plank lines
    for i in range(3):
        ly = py - ph/2 + ph * (i + 1) / 4
        A(f'<line x1="{px - pw/2 + 2}" y1="{ly}" x2="{px + pw/2 - 2}" y2="{ly}" '
          f'stroke="#A08050" stroke-width="0.7" opacity="0.4"/>')

# --- Lantern posts (small circles with glow, from above) ---
lanterns = [
    (140, 160), (265, 270), (135, 395), (180, 270), (315, 320),
    (195, 130), (250, 410), (85, 455), (355, 380),
]
for lx, ly in lanterns:
    # Glow
    A(f'<circle cx="{lx}" cy="{ly}" r="6" fill="#F0D870" opacity="0.2"/>')
    A(f'<circle cx="{lx}" cy="{ly}" r="3.5" fill="#F0D870" opacity="0.3"/>')
    # Post (dark dot)
    A(f'<circle cx="{lx}" cy="{ly}" r="2" fill="#8B6840" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.7"/>')

# ═══════════════════════════════════════════════════════════════════════
# LAYER 4: GROUND DETAILS
# ═══════════════════════════════════════════════════════════════════════

# --- Wildflower clusters (groups of 3-5 tiny dots) ---
flower_clusters = [
    (115, 175), (125, 195), (245, 180), (255, 195), (175, 330),
    (225, 345), (195, 500), (265, 480), (105, 440), (330, 440),
    (155, 560), (280, 565), (90, 105), (310, 90), (165, 70),
    (240, 55), (85, 350), (345, 270), (200, 240), (295, 385),
    (70, 530), (360, 530), (120, 250), (295, 200), (180, 390),
]
for fcx, fcy in flower_clusters:
    n = random.randint(3, 5)
    color = random.choice(FLOWER_COLORS)
    for _ in range(n):
        dx = random.uniform(-6, 6)
        dy = random.uniform(-6, 6)
        r = random.uniform(1.5, 3)
        A(f'<circle cx="{fcx + dx:.1f}" cy="{fcy + dy:.1f}" r="{r:.1f}" '
          f'fill="{color}" stroke="{OUTLINE}" stroke-width="0.5" opacity="0.6"/>')

# --- Mushroom fairy rings (circles of tiny dots) ---
fairy_rings = [(120, 185, 12), (270, 480, 14), (200, 345, 10), (330, 160, 11)]
for frx, fry, frr in fairy_rings:
    n_mushrooms = random.randint(7, 10)
    for i in range(n_mushrooms):
        angle = math.pi * 2 * i / n_mushrooms
        mx = frx + frr * math.cos(angle) + random.uniform(-1, 1)
        my = fry + frr * math.sin(angle) + random.uniform(-1, 1)
        # Tiny mushroom cap (red/brown dot)
        cap_color = random.choice(['#D06040', '#C07050', '#B86848'])
        A(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="1.8" '
          f'fill="{cap_color}" stroke="{OUTLINE}" stroke-width="0.5" opacity="0.55"/>')

# --- Fern clusters (small radiating lines) ---
ferns = [
    (80, 170), (310, 180), (130, 290), (280, 310), (170, 450),
    (240, 430), (90, 500), (340, 510), (55, 260), (360, 260),
    (200, 110), (160, 370), (250, 370), (40, 130), (370, 100),
]
for fx, fy in ferns:
    n_fronds = random.randint(5, 8)
    for i in range(n_fronds):
        angle = math.pi * 2 * i / n_fronds + random.uniform(-0.3, 0.3)
        length = random.uniform(5, 10)
        ex = fx + length * math.cos(angle)
        ey = fy + length * math.sin(angle)
        A(f'<line x1="{fx}" y1="{fy}" x2="{ex:.1f}" y2="{ey:.1f}" '
          f'stroke="#5A8840" stroke-width="1" stroke-linecap="round" opacity="0.45"/>')

# --- Fallen logs (short thick brown lines from above) ---
fallen_logs = [
    (95, 230, 20, 0.8), (285, 290, 22, -0.5), (175, 510, 18, 1.2),
    (250, 540, 20, 0.3), (60, 380, 16, -0.7), (350, 360, 19, 0.9),
    (140, 470, 17, -0.4), (310, 470, 21, 0.6),
]
for lx, ly, ll, la in fallen_logs:
    ex = lx + ll * math.cos(la)
    ey = ly + ll * math.sin(la)
    A(f'<line x1="{lx}" y1="{ly}" x2="{ex:.1f}" y2="{ey:.1f}" '
      f'stroke="#8B6840" stroke-width="3.5" stroke-linecap="round" opacity="0.55"/>')
    A(f'<line x1="{lx}" y1="{ly}" x2="{ex:.1f}" y2="{ey:.1f}" '
      f'stroke="#A08050" stroke-width="1.5" stroke-linecap="round" opacity="0.35"/>')

# --- Tree stumps (concentric circles from above) ---
stumps = [(105, 215, 5), (295, 275, 4.5), (180, 475, 5.5), (250, 200, 4), (340, 500, 5)]
for sx, sy, sr in stumps:
    A(f'<path d="{wobble_circle(sx, sy, sr, 8)}" fill="#C0A070" stroke="{OUTLINE}" '
      f'stroke-width="1.2" opacity="0.6"/>')
    A(f'<path d="{wobble_circle(sx, sy, sr * 0.5, 6)}" fill="#A08858" stroke="{OUTLINE}" '
      f'stroke-width="0.8" opacity="0.5"/>')
    # Growth rings
    A(f'<path d="{wobble_circle(sx, sy, sr * 0.75, 7)}" fill="none" stroke="#A08858" '
      f'stroke-width="0.6" opacity="0.35"/>')

# --- Moss patches (irregular green blobs) ---
moss_patches = [
    (80, 200, 8, 6), (300, 240, 10, 7), (160, 420, 9, 6),
    (240, 410, 7, 5), (120, 360, 8, 6), (280, 380, 10, 7),
    (50, 300, 7, 5), (365, 300, 8, 6), (200, 530, 9, 7),
    (150, 260, 7, 5), (260, 220, 8, 6), (330, 550, 7, 5),
]
for mx, my, mrx, mry in moss_patches:
    A(f'<path d="{wobble_ellipse(mx, my, mrx, mry, 6)}" '
      f'fill="#6BA854" opacity="0.25" stroke="none"/>')

# --- Small rocks/stones scattered ---
rocks = [
    (115, 165), (260, 175), (175, 310), (215, 335), (130, 405),
    (305, 395), (180, 550), (250, 555), (75, 250), (340, 255),
    (95, 450), (330, 455), (165, 145), (245, 105), (55, 50),
    (355, 55), (200, 220), (280, 430), (110, 535), (310, 545),
    (40, 185), (375, 225), (150, 500), (265, 510),
]
for rx, ry in rocks:
    rr = random.uniform(2, 4)
    A(f'<path d="{wobble_circle(rx, ry, rr, 5)}" fill="#B0A890" stroke="{OUTLINE}" '
      f'stroke-width="0.6" opacity="0.45"/>')

# --- Leaf scatter on paths ---
leaf_positions = [
    (190, 560), (185, 520), (175, 470), (165, 430), (145, 380),
    (135, 340), (140, 300), (155, 250), (160, 200), (155, 170),
    (145, 120), (140, 80), (150, 40),
    # secondary path
    (180, 265), (210, 260), (245, 265), (280, 275), (320, 295),
    (350, 320), (380, 345),
]
for lx, ly in leaf_positions:
    # Scatter 1-3 tiny leaves near each point
    for _ in range(random.randint(1, 3)):
        dx, dy = random.uniform(-8, 8), random.uniform(-5, 5)
        angle = random.uniform(0, math.pi * 2)
        size = random.uniform(2.5, 4)
        ex = lx + dx + size * math.cos(angle)
        ey = ly + dy + size * math.sin(angle)
        leaf_col = random.choice(['#6BA854', '#8CC870', '#4A8838', '#C8A040'])
        A(f'<path d="M{lx+dx:.1f},{ly+dy:.1f} Q{(lx+dx+ex)/2+random.uniform(-1,1):.1f},'
          f'{(ly+dy+ey)/2-2:.1f} {ex:.1f},{ey:.1f}" '
          f'stroke="{leaf_col}" stroke-width="1.2" fill="none" opacity="0.4" stroke-linecap="round"/>')

# ═══════════════════════════════════════════════════════════════════════
# LAYER 5: WILDLIFE & EFFECTS
# ═══════════════════════════════════════════════════════════════════════

# --- Deer silhouettes (tiny, from above: oval body + dot head) ---
deer = [(190, 190, 0.5), (270, 360, -0.3), (110, 410, 0.8), (310, 140, -0.6)]
for dx, dy, da in deer:
    ca, sa = math.cos(da), math.sin(da)
    # Body (oval)
    A(f'<ellipse cx="{dx}" cy="{dy}" rx="5" ry="3" '
      f'transform="rotate({math.degrees(da):.1f},{dx},{dy})" '
      f'fill="#8B6840" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.45"/>')
    # Head (dot offset from body)
    hx = dx + 6 * ca
    hy = dy + 6 * sa
    A(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="2" '
      f'fill="#8B6840" stroke="{OUTLINE}" stroke-width="0.6" opacity="0.45"/>')
    # Tiny leg dots
    for s in [-1, 1]:
        for t in [-0.3, 0.3]:
            legx = dx + t * 4 * ca - s * 2 * sa
            legy = dy + t * 4 * sa + s * 2 * ca
            A(f'<circle cx="{legx:.1f}" cy="{legy:.1f}" r="0.8" fill="#6B5030" opacity="0.35"/>')

# --- Rabbits (small circles from above) ---
rabbits = [(220, 300, 0.2), (140, 240, -0.8), (310, 450, 1.0)]
for rx, ry, ra in rabbits:
    ca, sa = math.cos(ra), math.sin(ra)
    # Body
    A(f'<ellipse cx="{rx}" cy="{ry}" rx="3.5" ry="2.5" '
      f'transform="rotate({math.degrees(ra):.1f},{rx},{ry})" '
      f'fill="#C0A880" stroke="{OUTLINE}" stroke-width="0.6" opacity="0.4"/>')
    # Head
    hx = rx + 4 * ca
    hy = ry + 4 * sa
    A(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="2" '
      f'fill="#C0A880" stroke="{OUTLINE}" stroke-width="0.6" opacity="0.4"/>')
    # Ears (two tiny ovals)
    for s in [-1, 1]:
        earx = hx + 2 * ca - s * 1.5 * sa
        eary = hy + 2 * sa + s * 1.5 * ca
        A(f'<ellipse cx="{earx:.1f}" cy="{eary:.1f}" rx="1" ry="2" '
          f'transform="rotate({math.degrees(ra):.1f},{earx:.1f},{eary:.1f})" '
          f'fill="#C0A880" stroke="{OUTLINE}" stroke-width="0.4" opacity="0.35"/>')

# --- Firefly / aether sparkles (teal dots with glow) ---
fireflies = [
    (130, 170), (175, 225), (220, 280), (160, 350), (250, 390),
    (110, 460), (300, 420), (190, 530), (270, 540), (90, 300),
    (340, 280), (200, 100), (260, 150), (80, 120), (370, 130),
    (145, 490), (320, 500), (50, 420), (380, 430), (230, 50),
]
for fx, fy in fireflies:
    # Outer glow
    A(f'<circle cx="{fx}" cy="{fy}" r="5" fill="#40C8B0" opacity="0.1"/>')
    # Inner glow
    A(f'<circle cx="{fx}" cy="{fy}" r="2.5" fill="#60E8D0" opacity="0.2"/>')
    # Core dot
    A(f'<circle cx="{fx}" cy="{fy}" r="1.2" fill="#80FFE0" opacity="0.5"/>')

# --- Bird shadows on the ground (tiny V shapes) ---
bird_shadows = [
    (95, 55), (175, 35), (310, 45), (255, 70), (140, 90),
    (200, 570), (280, 580), (110, 580), (350, 570), (50, 555),
]
for bx, by in bird_shadows:
    bw = random.uniform(4, 7)
    A(f'<path d="M{bx-bw},{by+2} Q{bx},{by-1} {bx+bw},{by+2}" '
      f'stroke="{OUTLINE}" stroke-width="1" fill="none" opacity="0.2"/>')

# --- Extra tiny details: texture dots on paths ---
for _ in range(20):
    # Scatter tiny dots along main path
    idx = random.randint(0, len(main_path_pts) - 1)
    px, py = main_path_pts[idx]
    dx, dy = random.uniform(-8, 8), random.uniform(-4, 4)
    A(f'<circle cx="{px + dx:.1f}" cy="{py + dy:.1f}" r="0.8" '
      f'fill="#A09070" opacity="0.3"/>')

# --- Paper texture (subtle cross-hatch marks) ---
for _ in range(30):
    tx = random.uniform(0, W)
    ty = random.uniform(0, H)
    tlen = random.uniform(3, 6)
    ta = random.uniform(0, math.pi)
    A(f'<line x1="{tx:.1f}" y1="{ty:.1f}" '
      f'x2="{tx + tlen * math.cos(ta):.1f}" y2="{ty + tlen * math.sin(ta):.1f}" '
      f'stroke="#C8C0B0" stroke-width="0.5" opacity="0.2"/>')

A('</svg>')

EASY = ''.join(P)

# ── Inject into stage.html ───────────────────────────────────────────────
pattern = r"(if\(diff==='NORMAL'\) return ')(.*?)(';)"
replacement = r"\g<1>" + EASY.replace('\\', '\\\\') + r"\g<3>"
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

assert new_content != content, "Injection failed — pattern not matched"
print(f"EASY SVG: {len(EASY):,} chars injected OK")
print(f"Total SVG elements: {EASY.count('<') - 1}")  # -1 for opening <svg>

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("stage.html written.")
