#!/usr/bin/env python3
"""gen_ultimate.py — ULTIMATE: The Crystarium / Crystal Tower (bird's-eye view at night)

Top-down perspective of The Crystarium, the last bastion of civilization
in The First (FF14 Shadowbringers). The Crystal Tower rises from the city
center, radiating light across the night landscape. Everything is drawn
as seen from directly above — rooftops, plazas, streets, and the tower
as a glowing octagonal shape.

viewBox: 0 0 400 600
Target: 250+ SVG elements, graphic-recording / hand-drawn sketch style
"""
import re as _re, math, random as _rnd

_r = _rnd.Random(42)

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    html = f.read()

parts = []
def A(s): parts.append(s)

# ═══════════════════════════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════════════════════════

def wobble_path(points, closed=False, jitter=1.2):
    """Convert list of (x,y) tuples into a slightly wobbly SVG path string."""
    if len(points) < 2:
        return ''
    segs = [f'M{points[0][0]:.1f},{points[0][1]:.1f}']
    for i in range(1, len(points)):
        x0, y0 = points[i-1]
        x1, y1 = points[i]
        mx = (x0 + x1) / 2 + _r.uniform(-jitter, jitter)
        my = (y0 + y1) / 2 + _r.uniform(-jitter, jitter)
        segs.append(f'Q{mx:.1f},{my:.1f} {x1:.1f},{y1:.1f}')
    if closed:
        x0, y0 = points[-1]
        x1, y1 = points[0]
        mx = (x0 + x1) / 2 + _r.uniform(-jitter, jitter)
        my = (y0 + y1) / 2 + _r.uniform(-jitter, jitter)
        segs.append(f'Q{mx:.1f},{my:.1f} {x1:.1f},{y1:.1f}')
        segs.append('Z')
    return ' '.join(segs)

def wobble_rect(x, y, w, h, jitter=1.0):
    """Wobbly rectangle (hand-drawn feel)."""
    return wobble_path([
        (x, y), (x+w, y), (x+w, y+h), (x, y+h)
    ], closed=True, jitter=jitter)

def wobble_ellipse(cx, cy, rx, ry, n=16, jitter=0.8):
    """Wobbly ellipse approximation."""
    pts = []
    for i in range(n):
        ang = 2 * math.pi * i / n
        rf = 1.0 + _r.uniform(-0.06, 0.06)
        pts.append((cx + rx * rf * math.cos(ang), cy + ry * rf * math.sin(ang)))
    return wobble_path(pts, closed=True, jitter=jitter)

def wobble_line(x1, y1, x2, y2, jitter=0.8):
    """Wobbly line between two points."""
    return wobble_path([(x1, y1), (x2, y2)], jitter=jitter)

def wobble_polygon(pts, jitter=1.0):
    """Wobbly polygon from list of (x,y) tuples."""
    return wobble_path(pts, closed=True, jitter=jitter)

def octagon(cx, cy, r, rotation=0):
    """Return list of 8 points forming an octagon."""
    pts = []
    for i in range(8):
        ang = math.radians(rotation + i * 45)
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return pts

def hexagon(cx, cy, r, rotation=0):
    """Return list of 6 points forming a hexagon."""
    pts = []
    for i in range(6):
        ang = math.radians(rotation + i * 60)
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return pts

# ═══════════════════════════════════════════════════════════════════════════
#  SVG OPEN + DEFS (gradients & filters)
# ═══════════════════════════════════════════════════════════════════════════
A('<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"><defs>')

# --- Sky gradient (deep indigo night) ---
A('<radialGradient id="uSky" cx="50%" cy="42%" r="68%">'
  '<stop offset="0%"   stop-color="#0A0828" stop-opacity="1"/>'
  '<stop offset="45%"  stop-color="#06031C" stop-opacity="1"/>'
  '<stop offset="100%" stop-color="#020110" stop-opacity="1"/>'
  '</radialGradient>')

# --- Crystal Tower central glow (top-down: bright center fading outward) ---
A('<radialGradient id="uTowerGlow" cx="50%" cy="42%" r="30%">'
  '<stop offset="0%"   stop-color="#B8DCFF" stop-opacity="0.95"/>'
  '<stop offset="18%"  stop-color="#88B8FF" stop-opacity="0.72"/>'
  '<stop offset="38%"  stop-color="#60A0FF" stop-opacity="0.42"/>'
  '<stop offset="60%"  stop-color="#3868C0" stop-opacity="0.18"/>'
  '<stop offset="80%"  stop-color="#1A3080" stop-opacity="0.06"/>'
  '<stop offset="100%" stop-color="#0C1840" stop-opacity="0"/>'
  '</radialGradient>')

# --- Tower inner glow (intense white-blue core) ---
A('<radialGradient id="uTowerCore" cx="50%" cy="42%" r="12%">'
  '<stop offset="0%"   stop-color="#FFFFFF" stop-opacity="0.98"/>'
  '<stop offset="30%"  stop-color="#D8F0FF" stop-opacity="0.85"/>'
  '<stop offset="60%"  stop-color="#88C0FF" stop-opacity="0.55"/>'
  '<stop offset="100%" stop-color="#4878D0" stop-opacity="0.20"/>'
  '</radialGradient>')

# --- Energy ring gradient ---
A('<radialGradient id="uRingGrad" cx="50%" cy="42%" r="45%">'
  '<stop offset="0%"   stop-color="#A060FF" stop-opacity="0"/>'
  '<stop offset="70%"  stop-color="#A060FF" stop-opacity="0.15"/>'
  '<stop offset="85%"  stop-color="#8040E0" stop-opacity="0.30"/>'
  '<stop offset="100%" stop-color="#6030B0" stop-opacity="0"/>'
  '</radialGradient>')

# --- Crystal shard glow ---
A('<radialGradient id="uCrystalGlow" cx="50%" cy="50%" r="50%">'
  '<stop offset="0%"   stop-color="#B8DCFF" stop-opacity="0.80"/>'
  '<stop offset="50%"  stop-color="#60A0FF" stop-opacity="0.35"/>'
  '<stop offset="100%" stop-color="#3060C0" stop-opacity="0"/>'
  '</radialGradient>')

# --- Sandstone building fill ---
A('<linearGradient id="uSand" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#C8A870"/>'
  '<stop offset="50%"  stop-color="#B09858"/>'
  '<stop offset="100%" stop-color="#A08848"/>'
  '</linearGradient>')

# --- Sandstone shadow variant ---
A('<linearGradient id="uSandS" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#9A8050"/>'
  '<stop offset="100%" stop-color="#7A6840"/>'
  '</linearGradient>')

# --- Iron framing ---
A('<linearGradient id="uIron" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#181820"/>'
  '<stop offset="100%" stop-color="#0A0F1E"/>'
  '</linearGradient>')

# --- Plaza stone ---
A('<linearGradient id="uPlaza" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#1A1828"/>'
  '<stop offset="100%" stop-color="#252038"/>'
  '</linearGradient>')

# --- Lantern glow ---
A('<radialGradient id="uLantern" cx="50%" cy="50%" r="50%">'
  '<stop offset="0%"   stop-color="#FFE888" stop-opacity="0.90"/>'
  '<stop offset="30%"  stop-color="#FFC030" stop-opacity="0.55"/>'
  '<stop offset="70%"  stop-color="#FFB020" stop-opacity="0.18"/>'
  '<stop offset="100%" stop-color="#FF8800" stop-opacity="0"/>'
  '</radialGradient>')

# --- Forest gradient ---
A('<radialGradient id="uForest" cx="50%" cy="50%" r="50%">'
  '<stop offset="0%"   stop-color="#3A1848" stop-opacity="0.90"/>'
  '<stop offset="100%" stop-color="#2A1040" stop-opacity="0.95"/>'
  '</radialGradient>')

# --- Nebula wash 1 ---
A('<radialGradient id="uNeb1" cx="25%" cy="20%" r="35%">'
  '<stop offset="0%"   stop-color="#3A1868" stop-opacity="0.22"/>'
  '<stop offset="100%" stop-color="#1A0838" stop-opacity="0"/>'
  '</radialGradient>')

# --- Nebula wash 2 ---
A('<radialGradient id="uNeb2" cx="75%" cy="30%" r="30%">'
  '<stop offset="0%"   stop-color="#182858" stop-opacity="0.18"/>'
  '<stop offset="100%" stop-color="#0A1030" stop-opacity="0"/>'
  '</radialGradient>')

# --- Nebula wash 3 ---
A('<radialGradient id="uNeb3" cx="60%" cy="65%" r="40%">'
  '<stop offset="0%"   stop-color="#281050" stop-opacity="0.15"/>'
  '<stop offset="100%" stop-color="#100828" stop-opacity="0"/>'
  '</radialGradient>')

# --- Water ripple gradient ---
A('<radialGradient id="uWater" cx="50%" cy="50%" r="50%">'
  '<stop offset="0%"   stop-color="#60A0FF" stop-opacity="0.50"/>'
  '<stop offset="50%"  stop-color="#4080D0" stop-opacity="0.30"/>'
  '<stop offset="100%" stop-color="#2060A0" stop-opacity="0.10"/>'
  '</radialGradient>')

# --- Vignette ---
A('<radialGradient id="uVig" cx="50%" cy="42%" r="72%">'
  '<stop offset="55%"  stop-color="#000000" stop-opacity="0"/>'
  '<stop offset="100%" stop-color="#010108" stop-opacity="0.82"/>'
  '</radialGradient>')

# --- Crystal vein glow ---
A('<linearGradient id="uVein" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#A060FF" stop-opacity="0"/>'
  '<stop offset="50%"  stop-color="#A060FF" stop-opacity="0.60"/>'
  '<stop offset="100%" stop-color="#A060FF" stop-opacity="0"/>'
  '</linearGradient>')

# --- Light beam gradient (radial from tower center) ---
A('<linearGradient id="uBeam" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#88B8FF" stop-opacity="0.35"/>'
  '<stop offset="100%" stop-color="#88B8FF" stop-opacity="0"/>'
  '</linearGradient>')

# --- Glow filter for crystal effects ---
A('<filter id="uGlowF" x="-50%" y="-50%" width="200%" height="200%">'
  '<feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur"/>'
  '<feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>'
  '</filter>')

# --- Soft glow filter ---
A('<filter id="uSoftGlow" x="-50%" y="-50%" width="200%" height="200%">'
  '<feGaussianBlur in="SourceGraphic" stdDeviation="6"/>'
  '</filter>')

A('</defs>')

# ═══════════════════════════════════════════════════════════════════════════
#  LAYER 1 — BASE SKY (deep indigo night)
# ═══════════════════════════════════════════════════════════════════════════

# Base fill
A('<rect width="400" height="600" fill="#020110"/>')
A('<rect width="400" height="600" fill="url(#uSky)"/>')

# Nebula wash areas (semi-transparent purple/blue patches)
A('<rect width="400" height="600" fill="url(#uNeb1)"/>')
A('<rect width="400" height="600" fill="url(#uNeb2)"/>')
A('<rect width="400" height="600" fill="url(#uNeb3)"/>')

# Additional nebula patches (wobbly shapes for hand-drawn feel)
nebula_patches = [
    (80, 90, 60, 45, '#2A1058', 0.12),
    (320, 140, 50, 35, '#1A2050', 0.10),
    (200, 60, 70, 40, '#221848', 0.08),
    (50, 400, 55, 40, '#1E1045', 0.10),
    (350, 450, 45, 35, '#182048', 0.09),
    (150, 500, 60, 30, '#201448', 0.07),
]
for nx, ny, nrx, nry, nc, nop in nebula_patches:
    A(f'<path d="{wobble_ellipse(nx, ny, nrx, nry, 12, 2.0)}" fill="{nc}" opacity="{nop}"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  DENSE STARFIELD (180 small + 30 medium + 12 bright stars = 222 stars)
# ═══════════════════════════════════════════════════════════════════════════

# Small stars (faint, scattered everywhere)
for _ in range(180):
    sx = _r.uniform(0, 400)
    sy = _r.uniform(0, 600)
    sr = _r.uniform(0.3, 0.9)
    sop = _r.uniform(0.25, 0.75)
    sc = _r.choice(['#FFFFFF', '#FFFFFF', '#B0D0FF', '#F0F4FF', '#FFF8F0'])
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr:.1f}" fill="{sc}" opacity="{sop:.2f}"/>')

# Medium stars (with subtle glow halo)
for _ in range(30):
    sx = _r.uniform(0, 400)
    sy = _r.uniform(0, 600)
    sr = _r.uniform(0.9, 1.6)
    sop = _r.uniform(0.55, 0.90)
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr:.1f}" fill="#FFFFFF" opacity="{sop:.2f}"/>')
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr*2.5:.1f}" fill="#B0D0FF" opacity="{sop*0.10:.2f}"/>')

# Bright named stars (with 4-point rays)
bright_stars = [
    (18, 25, 1.8), (72, 48, 2.0), (135, 18, 2.2), (198, 8, 1.9),
    (265, 32, 2.1), (338, 22, 2.3), (385, 55, 1.7), (52, 560, 1.6),
    (160, 580, 1.5), (310, 570, 1.8), (390, 540, 1.4), (28, 480, 1.6),
]
for bsx, bsy, bsr in bright_stars:
    bsop = _r.uniform(0.85, 0.98)
    A(f'<circle cx="{bsx}" cy="{bsy}" r="{bsr}" fill="#FFFFFF" opacity="{bsop:.2f}"/>')
    A(f'<circle cx="{bsx}" cy="{bsy}" r="{bsr*3:.1f}" fill="#B0D0FF" opacity="{bsop*0.12:.2f}"/>')
    for sa in (0, 90):
        rad = math.radians(sa)
        ex = bsx + math.cos(rad) * bsr * 5
        ey = bsy + math.sin(rad) * bsr * 5
        A(f'<line x1="{bsx}" y1="{bsy}" x2="{ex:.1f}" y2="{ey:.1f}" '
          f'stroke="#FFFFFF" stroke-width="0.5" opacity="{bsop*0.35:.2f}"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  LAYER 5 — STREETS & PLAZA (drawn first, underneath buildings)
#  Bird's-eye: dark stone tiles, crystal veins, winding streets
# ═══════════════════════════════════════════════════════════════════════════

# Main plaza area (central, around tower)
A(f'<path d="{wobble_ellipse(200, 250, 160, 130, 20, 1.5)}" fill="#1A1828" opacity="0.85"/>')
A(f'<path d="{wobble_ellipse(200, 250, 140, 115, 18, 1.2)}" fill="#1E1C30" opacity="0.70"/>')

# Tile grid pattern (subtle lines forming plaza tiles)
# Horizontal tile lines
for ty in range(135, 580, 18):
    x_start = max(0, 200 - 180 + abs(ty - 250) * 0.3)
    x_end = min(400, 200 + 180 - abs(ty - 250) * 0.3)
    if x_start < x_end:
        A(f'<path d="{wobble_line(x_start, ty, x_end, ty, 0.5)}" '
          f'stroke="#252038" stroke-width="0.6" fill="none" opacity="0.35"/>')
# Vertical tile lines
for tx in range(30, 400, 18):
    y_start = max(100, 250 - 130 + abs(tx - 200) * 0.5)
    y_end = min(580, 250 + 130 - abs(tx - 200) * 0.3 + 200)
    if y_start < y_end:
        A(f'<path d="{wobble_line(tx, y_start, tx, y_end, 0.5)}" '
          f'stroke="#252038" stroke-width="0.5" fill="none" opacity="0.30"/>')

# Steps / staircases (parallel lines - 4 staircase areas)
staircase_data = [
    (130, 180, 170, 180, 5),   # north-west stairs
    (230, 180, 270, 180, 5),   # north-east stairs
    (120, 350, 160, 350, 6),   # south-west stairs
    (240, 350, 280, 350, 6),   # south-east stairs
]
for sx1, sy1, sx2, sy2, n_steps in staircase_data:
    for si in range(n_steps):
        offset = si * 4
        A(f'<path d="{wobble_line(sx1, sy1+offset, sx2, sy1+offset, 0.4)}" '
          f'stroke="#303048" stroke-width="1.2" fill="none" opacity="0.50"/>')

# Winding streets between buildings (darker paths)
streets = [
    # Main north-south avenue
    "M200,100 Q198,160 200,250 Q202,340 200,500",
    # East-west cross street
    "M40,260 Q120,255 200,250 Q280,255 360,260",
    # Diagonal approach roads
    "M60,140 Q100,180 140,210",
    "M340,140 Q300,180 260,210",
    # Southern streets
    "M80,380 Q140,370 180,350",
    "M320,380 Q260,370 220,350",
    # Outer ring path
    "M50,200 Q60,300 80,380 Q120,440 200,460 Q280,440 320,380 Q340,300 350,200",
]
for sp in streets:
    A(f'<path d="{sp}" fill="none" stroke="#0E0C18" stroke-width="10" opacity="0.50" stroke-linecap="round"/>')
    A(f'<path d="{sp}" fill="none" stroke="#141220" stroke-width="6" opacity="0.35" stroke-linecap="round"/>')

# Small gardens / planter boxes (dark green patches)
garden_data = [
    (85, 210, 12, 8), (315, 210, 12, 8), (90, 330, 10, 7),
    (310, 330, 10, 7), (150, 400, 14, 9), (250, 400, 14, 9),
    (70, 280, 8, 6), (330, 280, 8, 6), (170, 460, 11, 7),
    (230, 460, 11, 7), (50, 350, 9, 6), (350, 350, 9, 6),
]
for gx, gy, grx, gry in garden_data:
    A(f'<path d="{wobble_ellipse(gx, gy, grx, gry, 8, 0.8)}" fill="#142818" opacity="0.65"/>')
    A(f'<path d="{wobble_ellipse(gx, gy, grx-2, gry-2, 8, 0.6)}" fill="#1A3420" opacity="0.45"/>')
    # Tiny plant dots
    for _ in range(3):
        px = gx + _r.uniform(-grx*0.6, grx*0.6)
        py = gy + _r.uniform(-gry*0.6, gry*0.6)
        A(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="1.2" fill="#284828" opacity="0.55"/>')

# Crystal vein channels (glowing lines running through ground)
vein_paths = [
    ("M200,250 L200,100", 0.45),
    ("M200,250 L200,500", 0.40),
    ("M200,250 L40,250",  0.35),
    ("M200,250 L360,250", 0.35),
    ("M200,250 L80,140",  0.25),
    ("M200,250 L320,140", 0.25),
    ("M200,250 L80,380",  0.25),
    ("M200,250 L320,380", 0.25),
    ("M200,250 Q150,200 60,170", 0.20),
    ("M200,250 Q250,200 340,170", 0.20),
    ("M200,250 Q150,310 60,350", 0.20),
    ("M200,250 Q250,310 340,350", 0.20),
]
for vp, vop in vein_paths:
    A(f'<path d="{vp}" fill="none" stroke="#A060FF" stroke-width="2.0" opacity="{vop*0.30:.2f}" stroke-linecap="round"/>')
    A(f'<path d="{vp}" fill="none" stroke="#B8DCFF" stroke-width="0.8" opacity="{vop:.2f}" stroke-linecap="round"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  LAYER 4 — BUILDINGS (rooftops from above, bird's-eye)
# ═══════════════════════════════════════════════════════════════════════════

def building_rooftop(bx, by, bw, bh, angle=0, sand='url(#uSand)', iron_color='#181820'):
    """Draw a building rooftop from bird's-eye view.
    Sandstone base with iron framework lines visible on top."""
    out = []
    # Main rooftop shape (wobbly rectangle)
    pts = [
        (bx, by), (bx+bw, by), (bx+bw, by+bh), (bx, by+bh)
    ]
    if angle != 0:
        # Rotate points around center
        cx, cy = bx + bw/2, by + bh/2
        rad = math.radians(angle)
        rotated = []
        for px, py in pts:
            dx, dy = px - cx, py - cy
            rx = dx * math.cos(rad) - dy * math.sin(rad) + cx
            ry = dx * math.sin(rad) + dy * math.cos(rad) + cy
            rotated.append((rx, ry))
        pts = rotated
    path = wobble_polygon(pts, jitter=0.8)

    # Shadow (offset slightly)
    shadow_pts = [(px+2, py+2) for px, py in pts]
    out.append(f'<path d="{wobble_polygon(shadow_pts, 0.6)}" fill="#08060E" opacity="0.40"/>')

    # Main sandstone fill
    out.append(f'<path d="{path}" fill="{sand}" opacity="0.88"/>')

    # Iron framework (cross beams visible on rooftop)
    cx, cy = sum(p[0] for p in pts)/4, sum(p[1] for p in pts)/4
    # Horizontal beam
    mid_l = ((pts[0][0]+pts[3][0])/2, (pts[0][1]+pts[3][1])/2)
    mid_r = ((pts[1][0]+pts[2][0])/2, (pts[1][1]+pts[2][1])/2)
    out.append(f'<path d="{wobble_line(mid_l[0], mid_l[1], mid_r[0], mid_r[1], 0.5)}" '
               f'stroke="{iron_color}" stroke-width="1.8" fill="none" opacity="0.65"/>')
    # Vertical beam
    mid_t = ((pts[0][0]+pts[1][0])/2, (pts[0][1]+pts[1][1])/2)
    mid_b = ((pts[2][0]+pts[3][0])/2, (pts[2][1]+pts[3][1])/2)
    out.append(f'<path d="{wobble_line(mid_t[0], mid_t[1], mid_b[0], mid_b[1], 0.5)}" '
               f'stroke="{iron_color}" stroke-width="1.8" fill="none" opacity="0.65"/>')
    # Diagonal braces
    out.append(f'<path d="{wobble_line(pts[0][0], pts[0][1], pts[2][0], pts[2][1], 0.4)}" '
               f'stroke="{iron_color}" stroke-width="1.0" fill="none" opacity="0.35"/>')
    out.append(f'<path d="{wobble_line(pts[1][0], pts[1][1], pts[3][0], pts[3][1], 0.4)}" '
               f'stroke="{iron_color}" stroke-width="1.0" fill="none" opacity="0.35"/>')

    # Outline
    out.append(f'<path d="{path}" fill="none" stroke="{iron_color}" stroke-width="1.5" opacity="0.75"/>')

    # Glowing windows (tiny cyan dots on roof)
    n_windows = max(1, int(bw * bh / 200))
    for _ in range(n_windows):
        wx = _r.uniform(min(p[0] for p in pts)+4, max(p[0] for p in pts)-4)
        wy = _r.uniform(min(p[1] for p in pts)+4, max(p[1] for p in pts)-4)
        wc = _r.choice(['#58AFF0', '#A8D8FF', '#78C8FF'])
        wop = _r.uniform(0.45, 0.75)
        out.append(f'<circle cx="{wx:.1f}" cy="{wy:.1f}" r="1.5" fill="{wc}" opacity="{wop:.2f}"/>')
        out.append(f'<circle cx="{wx:.1f}" cy="{wy:.1f}" r="3.5" fill="{wc}" opacity="{wop*0.15:.2f}"/>')

    return ''.join(out)

def building_with_balcony(bx, by, bw, bh, balcony_side='S', angle=0):
    """Building with a small balcony/terrace extending from one side."""
    out = []
    out.append(building_rooftop(bx, by, bw, bh, angle))
    # Balcony platform
    if balcony_side == 'S':
        out.append(f'<path d="{wobble_rect(bx+bw*0.3, by+bh, bw*0.4, 5, 0.5)}" '
                   f'fill="#B09858" opacity="0.70" stroke="#181820" stroke-width="0.8"/>')
    elif balcony_side == 'N':
        out.append(f'<path d="{wobble_rect(bx+bw*0.3, by-5, bw*0.4, 5, 0.5)}" '
                   f'fill="#B09858" opacity="0.70" stroke="#181820" stroke-width="0.8"/>')
    elif balcony_side == 'E':
        out.append(f'<path d="{wobble_rect(bx+bw, by+bh*0.3, 5, bh*0.4, 0.5)}" '
                   f'fill="#B09858" opacity="0.70" stroke="#181820" stroke-width="0.8"/>')
    elif balcony_side == 'W':
        out.append(f'<path d="{wobble_rect(bx-5, by+bh*0.3, 5, bh*0.4, 0.5)}" '
                   f'fill="#B09858" opacity="0.70" stroke="#181820" stroke-width="0.8"/>')
    return ''.join(out)

# --- Place 28 building rooftops around the city ---

# Northern building cluster (above tower)
buildings = [
    # (x, y, w, h, angle, has_balcony, balcony_side)
    # NW cluster
    (18, 68, 38, 28, 5, True, 'E'),
    (22, 102, 32, 22, -3, False, ''),
    (62, 78, 28, 35, 8, True, 'S'),
    (58, 120, 35, 24, -5, False, ''),
    # NE cluster
    (310, 72, 36, 30, -6, True, 'W'),
    (315, 108, 30, 22, 4, False, ''),
    (352, 82, 32, 28, -4, True, 'S'),
    (348, 118, 28, 20, 7, False, ''),
    # West buildings (flanking tower)
    (15, 168, 45, 32, 3, True, 'E'),
    (20, 208, 40, 28, -4, True, 'E'),
    (25, 242, 42, 30, 2, False, ''),
    (18, 280, 38, 25, -3, True, 'E'),
    (30, 312, 35, 22, 5, False, ''),
    # East buildings (flanking tower)
    (338, 168, 45, 30, -3, True, 'W'),
    (340, 206, 42, 28, 4, True, 'W'),
    (335, 242, 40, 32, -2, False, ''),
    (342, 282, 38, 24, 3, True, 'W'),
    (332, 314, 36, 22, -5, False, ''),
    # Southern buildings
    (40, 380, 35, 28, 6, True, 'N'),
    (82, 390, 30, 24, -4, False, ''),
    (128, 385, 32, 26, 3, True, 'N'),
    (260, 385, 34, 26, -3, True, 'N'),
    (305, 390, 28, 24, 5, False, ''),
    (342, 380, 36, 28, -6, True, 'N'),
    # Far south
    (60, 440, 30, 22, 4, False, ''),
    (110, 450, 28, 20, -3, True, 'N'),
    (270, 450, 30, 22, 3, True, 'N'),
    (320, 440, 32, 24, -4, False, ''),
]

for bdata in buildings:
    bx, by, bw, bh, angle, has_bal, bal_side = bdata
    if has_bal:
        A(building_with_balcony(bx, by, bw, bh, bal_side, angle))
    else:
        A(building_rooftop(bx, by, bw, bh, angle))

# Banner/flag indicators on some buildings (small triangles)
banner_buildings = [
    (37, 68, '#C83030'), (78, 78, '#3060A0'), (328, 72, '#C8A030'),
    (37, 168, '#3060A0'), (360, 168, '#C83030'), (60, 380, '#A03060'),
    (355, 380, '#3060A0'), (140, 385, '#C8A030'),
]
for bfx, bfy, bfc in banner_buildings:
    A(f'<polygon points="{bfx},{bfy} {bfx+5},{bfy-3} {bfx+5},{bfy+3}" '
      f'fill="{bfc}" opacity="0.60" stroke="#181820" stroke-width="0.5"/>')
    # Tiny flag pole (dot from above)
    A(f'<circle cx="{bfx}" cy="{bfy}" r="1" fill="#181820" opacity="0.80"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  THE ROTUNDA DOME (large circle with architectural detail, from above)
#  Located at roughly (100, 300)
# ═══════════════════════════════════════════════════════════════════════════

rot_cx, rot_cy, rot_r = 100, 300, 35

# Outer steps (concentric circles)
for si in range(3):
    sr = rot_r + 12 - si * 4
    A(f'<path d="{wobble_ellipse(rot_cx, rot_cy, sr, sr, 20, 0.6)}" '
      f'fill="#C8A870" opacity="{0.50 + si*0.10}" stroke="#181820" stroke-width="1.0"/>')

# Dome body (dark iron dome seen from above)
A(f'<path d="{wobble_ellipse(rot_cx, rot_cy, rot_r, rot_r, 24, 0.5)}" '
  f'fill="#0C1020" opacity="0.92" stroke="#181820" stroke-width="2.0"/>')

# Iron ribs radiating from center (dome structural ribs)
for ri in range(12):
    ang = math.radians(ri * 30)
    ex = rot_cx + math.cos(ang) * rot_r
    ey = rot_cy + math.sin(ang) * rot_r
    A(f'<path d="{wobble_line(rot_cx, rot_cy, ex, ey, 0.4)}" '
      f'stroke="#181820" stroke-width="2.0" fill="none" opacity="0.80"/>')

# Concentric ring details on dome
for rr_frac in (0.35, 0.65, 0.90):
    rr = rot_r * rr_frac
    A(f'<path d="{wobble_ellipse(rot_cx, rot_cy, rr, rr, 16, 0.4)}" '
      f'fill="none" stroke="#282838" stroke-width="1.2" opacity="0.60"/>')

# Crystal panel sections (between ribs, shimmering)
for ri in range(12):
    ang1 = math.radians(ri * 30 + 5)
    ang2 = math.radians(ri * 30 + 25)
    mid_r = rot_r * 0.55
    mx = rot_cx + math.cos((ang1+ang2)/2) * mid_r
    my = rot_cy + math.sin((ang1+ang2)/2) * mid_r
    cop = _r.uniform(0.10, 0.25)
    A(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="4" fill="#58AFF0" opacity="{cop:.2f}"/>')

# Oculus (center hole/lantern of dome)
A(f'<circle cx="{rot_cx}" cy="{rot_cy}" r="6" fill="#B8DCFF" opacity="0.75"/>')
A(f'<circle cx="{rot_cx}" cy="{rot_cy}" r="3" fill="#FFFFFF" opacity="0.90"/>')
A(f'<circle cx="{rot_cx}" cy="{rot_cy}" r="12" fill="#60A0FF" opacity="0.15"/>')

# Finial (tiny crystal spire tip visible from above as bright dot)
A(f'<circle cx="{rot_cx}" cy="{rot_cy}" r="2" fill="#FFFFFF" opacity="0.95"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  THE EXEDRA FOUNTAIN (circle with water pattern, bird's-eye)
#  Located at roughly (300, 310)
# ═══════════════════════════════════════════════════════════════════════════

ftn_cx, ftn_cy, ftn_r = 300, 310, 28

# Outer basin rim (sandstone)
A(f'<path d="{wobble_ellipse(ftn_cx, ftn_cy, ftn_r+6, ftn_r+6, 20, 0.5)}" '
  f'fill="#C8A870" opacity="0.80" stroke="#181820" stroke-width="1.5"/>')

# Water surface
A(f'<path d="{wobble_ellipse(ftn_cx, ftn_cy, ftn_r, ftn_r, 20, 0.4)}" '
  f'fill="url(#uWater)" opacity="0.75"/>')

# Concentric water ripples
for wr_frac in (0.30, 0.50, 0.70, 0.85, 0.95):
    wr = ftn_r * wr_frac
    wop = 0.20 + (1.0 - wr_frac) * 0.25
    A(f'<path d="{wobble_ellipse(ftn_cx, ftn_cy, wr, wr, 14, 0.3)}" '
      f'fill="none" stroke="#88C8FF" stroke-width="0.8" opacity="{wop:.2f}"/>')

# Central fountain jet (seen from above as bright dot with spray pattern)
A(f'<circle cx="{ftn_cx}" cy="{ftn_cy}" r="4" fill="#C0E8FF" opacity="0.85"/>')
A(f'<circle cx="{ftn_cx}" cy="{ftn_cy}" r="2" fill="#FFFFFF" opacity="0.95"/>')
# Spray droplets radiating outward
for si in range(8):
    sang = math.radians(si * 45 + _r.uniform(-5, 5))
    sdist = _r.uniform(8, 18)
    sdx = ftn_cx + math.cos(sang) * sdist
    sdy = ftn_cy + math.sin(sang) * sdist
    A(f'<circle cx="{sdx:.1f}" cy="{sdy:.1f}" r="1" fill="#A8E0FF" opacity="0.55"/>')

# Iron bracket pins around fountain rim
for bi in range(8):
    bang = math.radians(bi * 45)
    bpx = ftn_cx + math.cos(bang) * (ftn_r + 4)
    bpy = ftn_cy + math.sin(bang) * (ftn_r + 4)
    A(f'<circle cx="{bpx:.1f}" cy="{bpy:.1f}" r="1.5" fill="#181820" opacity="0.75"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  MAIN GATE (thick arch shape from above)
#  Located at south of the city, around (200, 470)
# ═══════════════════════════════════════════════════════════════════════════

gate_cx, gate_cy = 200, 470

# Gate towers (two thick rectangles)
A(f'<path d="{wobble_rect(gate_cx-35, gate_cy-10, 18, 24, 0.8)}" '
  f'fill="url(#uSand)" opacity="0.90" stroke="#181820" stroke-width="1.8"/>')
A(f'<path d="{wobble_rect(gate_cx+17, gate_cy-10, 18, 24, 0.8)}" '
  f'fill="url(#uSand)" opacity="0.90" stroke="#181820" stroke-width="1.8"/>')

# Iron framing on gate towers
for gox in [gate_cx-35, gate_cx+17]:
    # Cross iron beams
    A(f'<path d="{wobble_line(gox+2, gate_cy-8, gox+16, gate_cy+12, 0.3)}" '
      f'stroke="#181820" stroke-width="1.2" fill="none" opacity="0.55"/>')
    A(f'<path d="{wobble_line(gox+16, gate_cy-8, gox+2, gate_cy+12, 0.3)}" '
      f'stroke="#181820" stroke-width="1.2" fill="none" opacity="0.55"/>')

# Arch between towers (thick curve from above - appears as dark gap)
A(f'<path d="M{gate_cx-17},{gate_cy-2} Q{gate_cx},{gate_cy-14} {gate_cx+17},{gate_cy-2}" '
  f'fill="none" stroke="url(#uSand)" stroke-width="8" opacity="0.85"/>')
A(f'<path d="M{gate_cx-17},{gate_cy-2} Q{gate_cx},{gate_cy-14} {gate_cx+17},{gate_cy-2}" '
  f'fill="none" stroke="#181820" stroke-width="2" opacity="0.70"/>')

# Dark opening beneath arch
A(f'<path d="M{gate_cx-14},{gate_cy+2} Q{gate_cx},{gate_cy-8} {gate_cx+14},{gate_cy+2} Z" '
  f'fill="#06031C" opacity="0.80"/>')

# Crystal keystone on arch (bright dot at center top)
A(f'<circle cx="{gate_cx}" cy="{gate_cy-10}" r="3" fill="#B8DCFF" opacity="0.80"/>')
A(f'<circle cx="{gate_cx}" cy="{gate_cy-10}" r="6" fill="#60A0FF" opacity="0.20"/>')

# Gate lanterns (amber dots at tower corners)
for glx, gly in [(gate_cx-38, gate_cy-12), (gate_cx-38, gate_cy+16),
                  (gate_cx+38, gate_cy-12), (gate_cx+38, gate_cy+16)]:
    A(f'<circle cx="{glx}" cy="{gly}" r="2.5" fill="#FFC030" opacity="0.80"/>')
    A(f'<circle cx="{glx}" cy="{gly}" r="6" fill="#FFB020" opacity="0.18"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  SANDSTONE WALL TEXTURES (warm tan detail lines on buildings)
#  Additional architectural detail pass
# ═══════════════════════════════════════════════════════════════════════════

# Sandstone texture lines on larger buildings (subtle hatching)
texture_buildings = [
    (18, 68, 38, 28), (62, 78, 28, 35), (310, 72, 36, 30),
    (15, 168, 45, 32), (338, 168, 45, 30), (40, 380, 35, 28),
    (342, 380, 36, 28),
]
for tbx, tby, tbw, tbh in texture_buildings:
    # Subtle horizontal texture lines
    for ti in range(3):
        ty_off = tby + tbh * (0.25 + ti * 0.25)
        A(f'<path d="{wobble_line(tbx+2, ty_off, tbx+tbw-2, ty_off, 0.3)}" '
          f'stroke="#A08848" stroke-width="0.5" fill="none" opacity="0.25"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  LAYER 2 — CRYSTAL TOWER (CENTER, the most prominent feature)
#  Bird's-eye: large glowing octagonal shape at center
# ═══════════════════════════════════════════════════════════════════════════

TCX, TCY = 200, 250  # Tower center position

# ── Intense glow halo (outermost, very large, semi-transparent) ──
A(f'<circle cx="{TCX}" cy="{TCY}" r="160" fill="#3060C0" opacity="0.04" filter="url(#uSoftGlow)"/>')
A(f'<circle cx="{TCX}" cy="{TCY}" r="120" fill="#4878D0" opacity="0.06" filter="url(#uSoftGlow)"/>')
A(f'<circle cx="{TCX}" cy="{TCY}" r="85" fill="#60A0FF" opacity="0.10" filter="url(#uSoftGlow)"/>')

# ── Light beams emanating outward (16 radial lines with gradient opacity) ──
for bi in range(16):
    b_ang = math.radians(bi * 22.5 + _r.uniform(-3, 3))
    b_len = _r.uniform(140, 220)
    bex = TCX + math.cos(b_ang) * b_len
    bey = TCY + math.sin(b_ang) * b_len
    b_op = _r.uniform(0.03, 0.08)
    b_sw = _r.uniform(1.5, 4.0)
    A(f'<line x1="{TCX}" y1="{TCY}" x2="{bex:.1f}" y2="{bey:.1f}" '
      f'stroke="#88B8FF" stroke-width="{b_sw:.1f}" opacity="{b_op:.3f}" stroke-linecap="round"/>')

# ── Radiating energy rings (concentric circles with glow) ──
energy_rings = [
    (70, 1.0, '#8040E0', 0.12),
    (55, 1.2, '#A060FF', 0.16),
    (42, 1.5, '#60A0FF', 0.22),
    (32, 1.8, '#88B8FF', 0.28),
    (24, 2.0, '#B8DCFF', 0.35),
]
for er_r, er_sw, er_c, er_op in energy_rings:
    A(f'<path d="{wobble_ellipse(TCX, TCY, er_r, er_r, 24, 0.6)}" '
      f'fill="none" stroke="{er_c}" stroke-width="{er_sw}" opacity="{er_op:.2f}"/>')
    # Faint glow version (wider, more transparent)
    A(f'<path d="{wobble_ellipse(TCX, TCY, er_r, er_r, 20, 0.8)}" '
      f'fill="none" stroke="{er_c}" stroke-width="{er_sw*3:.1f}" opacity="{er_op*0.20:.3f}"/>')

# ── Tower octagonal shape (main body from above) ──
tower_r = 18  # Octagon outer radius

# Outer glow ring
oct_outer = octagon(TCX, TCY, tower_r + 8, rotation=22.5)
A(f'<path d="{wobble_polygon(oct_outer, 0.5)}" fill="#60A0FF" opacity="0.25"/>')

# Main octagonal body
oct_main = octagon(TCX, TCY, tower_r, rotation=22.5)
A(f'<path d="{wobble_polygon(oct_main, 0.4)}" fill="#B8DCFF" opacity="0.90" '
  f'stroke="#88B8FF" stroke-width="2"/>')

# Inner crystal facet pattern (geometric lines within the tower shape)
# Facet lines from each vertex to center
for pt in oct_main:
    A(f'<path d="{wobble_line(pt[0], pt[1], TCX, TCY, 0.3)}" '
      f'stroke="#FFFFFF" stroke-width="0.8" fill="none" opacity="0.50"/>')

# Inner octagonal rings (nested)
for inner_frac in (0.65, 0.35):
    inner_r = tower_r * inner_frac
    oct_inner = octagon(TCX, TCY, inner_r, rotation=22.5)
    A(f'<path d="{wobble_polygon(oct_inner, 0.3)}" fill="none" '
      f'stroke="#FFFFFF" stroke-width="1.0" opacity="0.55"/>')

# Additional facet lines (connecting midpoints of edges to inner ring)
for i in range(8):
    p1 = oct_main[i]
    p2 = oct_main[(i+1) % 8]
    mid = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
    inner_p = octagon(TCX, TCY, tower_r * 0.35, rotation=22.5)[i]
    A(f'<path d="{wobble_line(mid[0], mid[1], inner_p[0], inner_p[1], 0.2)}" '
      f'stroke="#D0ECFF" stroke-width="0.6" fill="none" opacity="0.40"/>')

# Central bright core
A(f'<circle cx="{TCX}" cy="{TCY}" r="6" fill="#FFFFFF" opacity="0.95"/>')
A(f'<circle cx="{TCX}" cy="{TCY}" r="4" fill="#FFFFFF" opacity="1.0"/>')
A(f'<circle cx="{TCX}" cy="{TCY}" r="10" fill="#D0ECFF" opacity="0.50"/>')

# Secondary highlight flares (cross-shaped from center)
for fa in (0, 45, 90, 135):
    frad = math.radians(fa)
    fex = TCX + math.cos(frad) * 28
    fey = TCY + math.sin(frad) * 28
    fex2 = TCX - math.cos(frad) * 28
    fey2 = TCY - math.sin(frad) * 28
    fop = 0.12 if fa % 90 == 0 else 0.06
    A(f'<line x1="{fex:.1f}" y1="{fey:.1f}" x2="{fex2:.1f}" y2="{fey2:.1f}" '
      f'stroke="#FFFFFF" stroke-width="1.5" opacity="{fop}"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  LAYER 3 — FLOATING CRYSTALS (scattered around the tower)
# ═══════════════════════════════════════════════════════════════════════════

def floating_crystal(cx, cy, size, angle=0, color='#B8DCFF', opacity=0.70):
    """Draw a floating crystal shard (diamond/kite shape from above with shadow)."""
    out = []
    hw = size * 0.5
    hh = size * 0.8

    # Diamond/kite shape points
    pts = [
        (cx, cy - hh),        # top
        (cx + hw, cy),        # right
        (cx, cy + hh * 0.6),  # bottom (shorter)
        (cx - hw, cy),        # left
    ]

    # Rotate if needed
    if angle != 0:
        rad = math.radians(angle)
        rotated = []
        for px, py in pts:
            dx, dy = px - cx, py - cy
            rx = dx * math.cos(rad) - dy * math.sin(rad) + cx
            ry = dx * math.sin(rad) + dy * math.cos(rad) + cy
            rotated.append((rx, ry))
        pts = rotated

    # Shadow/glow below shard
    out.append(f'<ellipse cx="{cx}" cy="{cy+2}" rx="{size*0.8:.1f}" ry="{size*0.4:.1f}" '
               f'fill="{color}" opacity="{opacity*0.12:.2f}"/>')

    # Crystal body
    out.append(f'<path d="{wobble_polygon(pts, 0.4)}" fill="{color}" opacity="{opacity:.2f}" '
               f'stroke="#FFFFFF" stroke-width="0.8"/>')

    # Inner facet line (center line)
    out.append(f'<path d="{wobble_line(pts[0][0], pts[0][1], pts[2][0], pts[2][1], 0.2)}" '
               f'stroke="#FFFFFF" stroke-width="0.6" fill="none" opacity="{opacity*0.50:.2f}"/>')

    # Bright highlight spot
    out.append(f'<circle cx="{cx}" cy="{cy-hh*0.3:.1f}" r="1.5" fill="#FFFFFF" opacity="{opacity*0.60:.2f}"/>')

    return ''.join(out)

# 12 floating crystal shards at various positions
crystal_shards = [
    # (cx, cy, size, angle, color, opacity)
    (145, 175, 14, 25,  '#B8DCFF', 0.75),
    (255, 175, 12, -20, '#A8D0FF', 0.70),
    (125, 215, 10, 35,  '#C8E8FF', 0.65),
    (275, 215, 11, -30, '#90C8FF', 0.68),
    (160, 310, 13, 15,  '#B8DCFF', 0.72),
    (240, 310, 10, -25, '#A0D0FF', 0.66),
    (105, 270, 9,  40,  '#D0EEFF', 0.60),
    (295, 270, 12, -15, '#B0D8FF', 0.72),
    (170, 140, 8,  -10, '#C0E4FF', 0.58),
    (230, 140, 9,  20,  '#A8D4FF', 0.62),
    (140, 360, 7,  30,  '#D0EEFF', 0.55),
    (260, 360, 8,  -35, '#C8E4FF', 0.58),
]

for cd in crystal_shards:
    A(floating_crystal(*cd))

# Energy lines connecting some crystals to the tower
crystal_connections = [
    (145, 175), (255, 175), (160, 310), (240, 310),
    (125, 215), (275, 215), (105, 270), (295, 270),
]
for ccx, ccy in crystal_connections:
    cop = _r.uniform(0.06, 0.14)
    A(f'<line x1="{ccx}" y1="{ccy}" x2="{TCX}" y2="{TCY}" '
      f'stroke="#A060FF" stroke-width="0.8" opacity="{cop:.2f}" stroke-dasharray="3,4"/>')

# Small crystal dust particles (tiny bright dots scattered)
for _ in range(40):
    dx = _r.uniform(100, 300)
    dy = _r.uniform(140, 370)
    dr = _r.uniform(0.4, 1.0)
    dop = _r.uniform(0.30, 0.70)
    dc = _r.choice(['#B8DCFF', '#FFFFFF', '#A060FF', '#88B8FF'])
    A(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="{dr:.1f}" fill="{dc}" opacity="{dop:.2f}"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  LAYER 6 — LIGHTING & DETAILS
# ═══════════════════════════════════════════════════════════════════════════

# --- Street lanterns (25+ amber glow dots along streets) ---
lantern_positions = [
    # Along main north-south avenue
    (195, 150), (205, 180), (195, 210), (205, 290),
    (195, 320), (205, 350), (195, 380), (205, 410),
    (195, 440), (205, 490), (195, 520),
    # Along east-west cross street
    (100, 255), (130, 252), (160, 250), (240, 250),
    (270, 252), (300, 258), (340, 262),
    # Outer ring path
    (65, 220), (55, 280), (70, 340), (110, 400),
    (330, 220), (345, 280), (330, 340), (290, 400),
    # Near buildings
    (55, 90), (350, 90), (45, 170), (355, 170),
]

for lx, ly in lantern_positions:
    # Lantern body (small dot)
    A(f'<circle cx="{lx}" cy="{ly}" r="2" fill="#FFC030" opacity="0.85"/>')
    # Inner bright core
    A(f'<circle cx="{lx}" cy="{ly}" r="1" fill="#FFE888" opacity="0.95"/>')
    # Warm amber glow halo
    A(f'<circle cx="{lx}" cy="{ly}" r="7" fill="#FFB020" opacity="0.18"/>')
    A(f'<circle cx="{lx}" cy="{ly}" r="14" fill="#FF8800" opacity="0.06"/>')

# --- Iron lamp fixtures on buildings (small dark rectangles with glow) ---
lamp_fixture_data = [
    (52, 72), (76, 82), (322, 76), (366, 86),
    (55, 172), (50, 212), (352, 172), (356, 210),
    (55, 384), (355, 384), (90, 394), (310, 394),
]
for lfx, lfy in lamp_fixture_data:
    A(f'<rect x="{lfx-2}" y="{lfy-1}" width="4" height="3" fill="#181820" rx="0.5" opacity="0.75"/>')
    A(f'<circle cx="{lfx}" cy="{lfy}" r="3" fill="#FFC030" opacity="0.30"/>')

# --- Purple Lakeland forest patches at edges ---
# Top-left forest
forest_patches_tl = [
    (15, 30, 18, 14), (35, 20, 16, 12), (5, 45, 14, 11),
    (28, 48, 12, 10), (50, 35, 15, 12), (8, 18, 12, 9),
]
for fx, fy, frx, fry in forest_patches_tl:
    A(f'<path d="{wobble_ellipse(fx, fy, frx, fry, 10, 1.0)}" fill="#3A1848" opacity="0.82"/>')
    A(f'<path d="{wobble_ellipse(fx-2, fy-2, frx*0.6, fry*0.6, 8, 0.6)}" fill="#4A2058" opacity="0.50"/>')

# Top-right forest
forest_patches_tr = [
    (385, 30, 18, 14), (365, 22, 16, 12), (395, 48, 14, 11),
    (372, 50, 12, 10), (350, 38, 15, 12), (392, 18, 12, 9),
]
for fx, fy, frx, fry in forest_patches_tr:
    A(f'<path d="{wobble_ellipse(fx, fy, frx, fry, 10, 1.0)}" fill="#3A1848" opacity="0.82"/>')
    A(f'<path d="{wobble_ellipse(fx+2, fy-2, frx*0.6, fry*0.6, 8, 0.6)}" fill="#4A2058" opacity="0.50"/>')

# Bottom-left forest
forest_patches_bl = [
    (12, 530, 16, 13), (30, 545, 14, 11), (8, 560, 18, 12),
    (45, 555, 12, 10), (22, 575, 15, 10), (5, 590, 14, 9),
]
for fx, fy, frx, fry in forest_patches_bl:
    A(f'<path d="{wobble_ellipse(fx, fy, frx, fry, 10, 1.0)}" fill="#2A1040" opacity="0.85"/>')
    A(f'<path d="{wobble_ellipse(fx-1, fy-2, frx*0.55, fry*0.55, 8, 0.6)}" fill="#3A1848" opacity="0.50"/>')

# Bottom-right forest
forest_patches_br = [
    (388, 530, 16, 13), (370, 548, 14, 11), (392, 565, 18, 12),
    (355, 558, 12, 10), (378, 578, 15, 10), (395, 592, 14, 9),
]
for fx, fy, frx, fry in forest_patches_br:
    A(f'<path d="{wobble_ellipse(fx, fy, frx, fry, 10, 1.0)}" fill="#2A1040" opacity="0.85"/>')
    A(f'<path d="{wobble_ellipse(fx+1, fy-2, frx*0.55, fry*0.55, 8, 0.6)}" fill="#3A1848" opacity="0.50"/>')

# Left edge forest strip
for fi in range(8):
    fy = 60 + fi * 62
    fx = _r.uniform(2, 18)
    frx = _r.uniform(10, 16)
    fry = _r.uniform(8, 14)
    A(f'<path d="{wobble_ellipse(fx, fy, frx, fry, 10, 1.0)}" fill="#3A1848" opacity="0.75"/>')

# Right edge forest strip
for fi in range(8):
    fy = 60 + fi * 62
    fx = _r.uniform(382, 398)
    frx = _r.uniform(10, 16)
    fry = _r.uniform(8, 14)
    A(f'<path d="{wobble_ellipse(fx, fy, frx, fry, 10, 1.0)}" fill="#3A1848" opacity="0.75"/>')

# --- Crystal energy sparkles throughout ---
for _ in range(30):
    spx = _r.uniform(50, 350)
    spy = _r.uniform(100, 500)
    spr = _r.uniform(0.5, 1.2)
    spop = _r.uniform(0.20, 0.55)
    spc = _r.choice(['#B8DCFF', '#A060FF', '#88B8FF', '#FFFFFF'])
    A(f'<circle cx="{spx:.1f}" cy="{spy:.1f}" r="{spr:.1f}" fill="{spc}" opacity="{spop:.2f}"/>')

# --- People-scale dots on streets (tiny, very subtle) ---
people_positions = [
    (192, 200), (208, 220), (188, 340), (212, 360),
    (185, 420), (215, 400), (170, 250), (230, 250),
    (140, 255), (260, 255), (195, 480), (205, 460),
    (100, 260), (300, 260), (115, 390), (285, 390),
    (155, 260), (245, 260), (180, 300), (220, 300),
]
for ppx, ppy in people_positions:
    A(f'<circle cx="{ppx}" cy="{ppy}" r="1.0" fill="#C8A870" opacity="0.25"/>')

# --- Moonlight reflections on crystals (subtle bright spots) ---
moon_reflections = [
    (TCX-5, TCY-8, 3, 0.15),
    (TCX+12, TCY-3, 2, 0.12),
    (145, 173, 2, 0.10),
    (255, 173, 2, 0.10),
    (rot_cx-3, rot_cy-5, 2.5, 0.10),
    (ftn_cx+5, ftn_cy-8, 2, 0.12),
]
for mrx, mry, mrr, mrop in moon_reflections:
    A(f'<circle cx="{mrx}" cy="{mry}" r="{mrr}" fill="#FFFFFF" opacity="{mrop}"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  ADDITIONAL DETAIL — extra building rooftops for density
# ═══════════════════════════════════════════════════════════════════════════

# Small ancillary structures (sheds, small rooftops)
small_buildings = [
    (98, 130, 18, 14, 5), (285, 130, 16, 12, -8),
    (42, 150, 15, 12, 3), (350, 150, 14, 11, -4),
    (30, 350, 16, 13, 7), (360, 350, 15, 12, -6),
    (95, 420, 14, 11, -3), (300, 420, 16, 12, 4),
    (160, 420, 12, 10, 2), (235, 420, 14, 11, -5),
    (75, 470, 13, 10, 6), (315, 470, 14, 11, -4),
]
for sbx, sby, sbw, sbh, sba in small_buildings:
    pts = [(sbx, sby), (sbx+sbw, sby), (sbx+sbw, sby+sbh), (sbx, sby+sbh)]
    if sba != 0:
        cx, cy = sbx + sbw/2, sby + sbh/2
        rad = math.radians(sba)
        pts = [(
            (px-cx)*math.cos(rad) - (py-cy)*math.sin(rad) + cx,
            (px-cx)*math.sin(rad) + (py-cy)*math.cos(rad) + cy
        ) for px, py in pts]
    # Shadow
    A(f'<path d="{wobble_polygon([(px+1.5, py+1.5) for px,py in pts], 0.5)}" '
      f'fill="#08060E" opacity="0.35"/>')
    # Body
    A(f'<path d="{wobble_polygon(pts, 0.6)}" fill="url(#uSandS)" opacity="0.80" '
      f'stroke="#181820" stroke-width="1.0"/>')
    # Iron cross
    cx2, cy2 = sum(p[0] for p in pts)/4, sum(p[1] for p in pts)/4
    A(f'<path d="{wobble_line(pts[0][0], pts[0][1], pts[2][0], pts[2][1], 0.3)}" '
      f'stroke="#181820" stroke-width="0.8" fill="none" opacity="0.40"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  MORE CRYSTAL VEIN CHANNELS (glowing blue/purple lines in ground)
# ═══════════════════════════════════════════════════════════════════════════

# Secondary vein network (thinner, more distributed)
secondary_veins = [
    "M50,200 Q80,230 120,240",
    "M350,200 Q320,230 280,240",
    "M80,350 Q120,340 160,320",
    "M320,350 Q280,340 240,320",
    "M100,420 Q150,430 200,425",
    "M300,420 Q250,430 200,425",
    "M60,160 Q90,180 130,195",
    "M340,160 Q310,180 270,195",
    "M150,480 Q175,470 200,465",
    "M250,480 Q225,470 200,465",
]
for svp in secondary_veins:
    sv_op = _r.uniform(0.08, 0.18)
    A(f'<path d="{svp}" fill="none" stroke="#8040E0" stroke-width="1.2" opacity="{sv_op:.2f}" stroke-linecap="round"/>')
    A(f'<path d="{svp}" fill="none" stroke="#B8DCFF" stroke-width="0.4" opacity="{sv_op*1.5:.2f}" stroke-linecap="round"/>')

# Vein intersection glow points
vein_nodes = [
    (120, 240), (280, 240), (160, 320), (240, 320),
    (130, 195), (270, 195), (200, 425), (200, 465),
]
for vnx, vny in vein_nodes:
    A(f'<circle cx="{vnx}" cy="{vny}" r="2.5" fill="#A060FF" opacity="0.25"/>')
    A(f'<circle cx="{vnx}" cy="{vny}" r="5" fill="#8040E0" opacity="0.08"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  ADDITIONAL FLOATING ELEMENTS — crystal dust, energy wisps
# ═══════════════════════════════════════════════════════════════════════════

# Energy wisps (tiny curved lines near tower)
for _ in range(15):
    wx = TCX + _r.uniform(-80, 80)
    wy = TCY + _r.uniform(-80, 80)
    wlen = _r.uniform(5, 12)
    wang = _r.uniform(0, 360)
    wrad = math.radians(wang)
    wex = wx + math.cos(wrad) * wlen
    wey = wy + math.sin(wrad) * wlen
    wmx = (wx + wex)/2 + _r.uniform(-3, 3)
    wmy = (wy + wey)/2 + _r.uniform(-3, 3)
    wop = _r.uniform(0.10, 0.28)
    A(f'<path d="M{wx:.1f},{wy:.1f} Q{wmx:.1f},{wmy:.1f} {wex:.1f},{wey:.1f}" '
      f'fill="none" stroke="#A060FF" stroke-width="0.8" opacity="{wop:.2f}" stroke-linecap="round"/>')

# Additional tiny crystal fragments floating (smaller than shards)
for _ in range(20):
    cfx = _r.uniform(60, 340)
    cfy = _r.uniform(120, 480)
    cfs = _r.uniform(2, 4)
    cfa = _r.uniform(0, 360)
    cfop = _r.uniform(0.25, 0.50)
    cfc = _r.choice(['#B8DCFF', '#A060FF', '#88B8FF'])
    # Tiny diamond
    cfrad = math.radians(cfa)
    p1 = (cfx, cfy - cfs)
    p2 = (cfx + cfs*0.6, cfy)
    p3 = (cfx, cfy + cfs*0.5)
    p4 = (cfx - cfs*0.6, cfy)
    A(f'<polygon points="{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} '
      f'{p3[0]:.1f},{p3[1]:.1f} {p4[0]:.1f},{p4[1]:.1f}" '
      f'fill="{cfc}" opacity="{cfop:.2f}"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  ARCHITECTURAL DETAILS — wall sections between buildings (from above)
# ═══════════════════════════════════════════════════════════════════════════

# Low walls connecting some buildings (visible as thin lines from above)
wall_segments = [
    (56, 95, 62, 118),    # NW buildings connected
    (90, 100, 95, 128),
    (340, 98, 338, 118),  # NE buildings connected
    (308, 102, 315, 128),
    (58, 200, 58, 240),   # West wall
    (342, 200, 342, 240), # East wall
    (78, 385, 128, 385),  # South wall segment
    (260, 385, 310, 385),
]
for wx1, wy1, wx2, wy2 in wall_segments:
    A(f'<path d="{wobble_line(wx1, wy1, wx2, wy2, 0.5)}" '
      f'stroke="#A08848" stroke-width="2.5" fill="none" opacity="0.55"/>')
    A(f'<path d="{wobble_line(wx1, wy1, wx2, wy2, 0.3)}" '
      f'stroke="#181820" stroke-width="0.8" fill="none" opacity="0.40"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  ADDITIONAL ROOFTOP DETAILS — chimneys, vents, etc.
# ═══════════════════════════════════════════════════════════════════════════

# Chimneys (small squares on some building rooftops)
chimney_positions = [
    (30, 74), (72, 85), (320, 78), (360, 88),
    (28, 174), (50, 214), (350, 174), (370, 212),
    (50, 386), (354, 386), (92, 396), (312, 396),
    (68, 446), (118, 456), (278, 456), (328, 446),
]
for chx, chy in chimney_positions:
    A(f'<rect x="{chx-2}" y="{chy-2}" width="4" height="4" fill="#282830" rx="0.5" opacity="0.70"/>')
    # Faint warm glow from chimney
    A(f'<circle cx="{chx}" cy="{chy}" r="2" fill="#FFC030" opacity="0.12"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  WATER/FOUNTAIN AREA — additional small fountain/pond
# ═══════════════════════════════════════════════════════════════════════════

# Small decorative pond near the Rotunda
pond_cx, pond_cy = 130, 340
pond_r = 10
A(f'<path d="{wobble_ellipse(pond_cx, pond_cy, pond_r+3, pond_r+2, 12, 0.4)}" '
  f'fill="#C8A870" opacity="0.60" stroke="#181820" stroke-width="0.8"/>')
A(f'<path d="{wobble_ellipse(pond_cx, pond_cy, pond_r, pond_r-1, 12, 0.3)}" '
  f'fill="#2060A0" opacity="0.45"/>')
for wr in (0.4, 0.7, 0.9):
    A(f'<path d="{wobble_ellipse(pond_cx, pond_cy, pond_r*wr, (pond_r-1)*wr, 10, 0.2)}" '
      f'fill="none" stroke="#68B0E0" stroke-width="0.5" opacity="0.30"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  TOWER PLATFORM — circular raised area around the Crystal Tower
# ═══════════════════════════════════════════════════════════════════════════

# Raised circular platform (seen as concentric rings from above)
for pi, (pr, pop, pc) in enumerate([
    (50, 0.20, '#252038'),
    (45, 0.25, '#1E1C30'),
    (40, 0.18, '#282840'),
]):
    A(f'<path d="{wobble_ellipse(TCX, TCY, pr, pr, 20, 0.5)}" '
      f'fill="none" stroke="{pc}" stroke-width="2.0" opacity="{pop}"/>')

# Decorative railing around tower platform (small regularly-spaced dots)
railing_r = 48
for ri in range(24):
    rang = math.radians(ri * 15)
    rpx = TCX + math.cos(rang) * railing_r
    rpy = TCY + math.sin(rang) * railing_r
    A(f'<circle cx="{rpx:.1f}" cy="{rpy:.1f}" r="1.0" fill="#C8A870" opacity="0.45"/>')

# Small iron bollards along the railing
for ri in range(8):
    rang = math.radians(ri * 45)
    rpx = TCX + math.cos(rang) * railing_r
    rpy = TCY + math.sin(rang) * railing_r
    A(f'<circle cx="{rpx:.1f}" cy="{rpy:.1f}" r="2.0" fill="#181820" opacity="0.60"/>')
    A(f'<circle cx="{rpx:.1f}" cy="{rpy:.1f}" r="1.0" fill="#88B8FF" opacity="0.35"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  FINAL ATMOSPHERE LAYERS
# ═══════════════════════════════════════════════════════════════════════════

# Tower glow overlay (adds overall crystal light to scene)
A(f'<rect width="400" height="600" fill="url(#uTowerGlow)"/>')

# Edge vignette
A('<rect width="400" height="600" fill="url(#uVig)"/>')

# Final crystal sparkle layer (on top of everything)
for _ in range(15):
    fsx = _r.uniform(120, 280)
    fsy = _r.uniform(170, 340)
    fsr = _r.uniform(0.3, 0.8)
    fsop = _r.uniform(0.40, 0.80)
    A(f'<circle cx="{fsx:.1f}" cy="{fsy:.1f}" r="{fsr:.1f}" fill="#FFFFFF" opacity="{fsop:.2f}"/>')

# Close SVG
A('</svg>')

# ═══════════════════════════════════════════════════════════════════════════
#  VALIDATE + INJECT
# ═══════════════════════════════════════════════════════════════════════════
svg = ''.join(parts)
print(f'ULTIMATE SVG: {len(svg):,} chars')

# Count elements
import xml.etree.ElementTree as ET
try:
    root = ET.fromstring(svg)
    elem_count = sum(1 for _ in root.iter()) - 1  # subtract root
    print(f'  SVG elements: {elem_count}')
    print('  XML parse: OK')
except ET.ParseError as e:
    raise RuntimeError(f'XML parse error: {e}')

# Gradient balance check
ro = len(_re.findall(r'<radialGradient', svg)); rc = len(_re.findall(r'</radialGradient', svg))
lo = len(_re.findall(r'<linearGradient', svg)); lc = len(_re.findall(r'</linearGradient', svg))
fo = len(_re.findall(r'<filter ', svg)); fc = len(_re.findall(r'</filter', svg))
print(f'  radialGradient: {ro}/{rc}  linearGradient: {lo}/{lc}  filter: {fo}/{fc}')
if ro != rc: raise RuntimeError(f'radialGradient mismatch: {ro}/{rc}')
if lo != lc: raise RuntimeError(f'linearGradient mismatch: {lo}/{lc}')
if fo != fc: raise RuntimeError(f'filter mismatch: {fo}/{fc}')

if svg.count('`'): raise RuntimeError('Backtick in SVG!')
if svg.count("'"): raise RuntimeError("Single quote in SVG!")

# CSS adjustments
html2 = html
for old, new in [
    ('#game-view[data-diff="ULTIMATE"] { background: rgb(3,1,15); }',
     '#game-view[data-diff="ULTIMATE"] { background: rgb(2,1,16); }'),
    ('#game-view[data-diff="ULTIMATE"] { background: rgb(2,1,10); }',
     '#game-view[data-diff="ULTIMATE"] { background: rgb(2,1,16); }'),
    ('.map-scroll[data-diff="ULTIMATE"] { background: #03010F; }',
     '.map-scroll[data-diff="ULTIMATE"] { background: #020110; }'),
    ('.map-scroll[data-diff="ULTIMATE"] { background: #020108; }',
     '.map-scroll[data-diff="ULTIMATE"] { background: #020110; }'),
]:
    if old in html2:
        html2 = html2.replace(old, new)
        print(f'  CSS: {old[:55]}')

pattern = r"(if\(diff===.ULTIMATE.\) return \`)(.*?)(\`;)"
repl = lambda m: m.group(1) + svg + m.group(3)
new_html, n = _re.subn(pattern, repl, html2, flags=_re.DOTALL)
if n == 0: raise RuntimeError("ULTIMATE pattern not found!")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f'  Injected into stage.html ({n} replacement)')
print('Done!')
