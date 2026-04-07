#!/usr/bin/env python3
"""gen_ultimate.py — ULTIMATE background: Elpis (FF14 Endwalker) v3
Accuracy targets from research:
  - Sky: BRIGHT CLEAR BLUE (daylight, visible sun, perfect summer day — NOT purple/amber)
  - Architecture: RED BRICK + cream stone accents (Amaurotine in actual light)
  - Elpis Stone Pillars: tall cylindrical columns crowned with lush greenery
  - Elpis Flowers: bioluminescent alien bell-tulip blooms, color shifts by emotion
    (purple=sadness/Hermes, blue=deep feeling, gold=joy, white=neutral, azure=loyalty)
  - Cloud sea visible below/around floating islands (defining compositional feature)
  - Floating islands each isolated, connected by Propylaea (teleporter pads)
  - Noetophoreon reference: single large tree with purple/violet leaves
  - Ktisis Hyperboreia: massive monolithic research building facade (background)
  - Stage 5: Creation/research area with glowing prototype orb
  - Stage 10: Propylaea (grand teleporter arch structure with energy shimmer)
"""
import re as _re, math

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    html = f.read()

parts = []
def A(s): parts.append(s)

# ─────────────────────────────────────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def cloud(cx, cy, rx, ry, op=0.90):
    """Soft fluffy cloud made of overlapping ellipses."""
    out = []
    bumps = [
        (cx, cy, rx, ry),
        (cx - rx*0.38, cy + ry*0.25, rx*0.65, ry*0.75),
        (cx + rx*0.38, cy + ry*0.25, rx*0.65, ry*0.75),
        (cx - rx*0.20, cy + ry*0.40, rx*0.80, ry*0.62),
        (cx + rx*0.18, cy - ry*0.18, rx*0.55, ry*0.60),
    ]
    for bx, by, brx, bry in bumps:
        out.append(f'<ellipse cx="{bx:.1f}" cy="{by:.1f}" rx="{brx:.1f}" ry="{bry:.1f}" '
                   f'fill="url(#eCloud)" opacity="{op:.2f}"/>')
    return ''.join(out)

def elpis_flower(fx, fy, glow_col, inner_col, stem_h=55, size=10):
    """Iconic Elpis bioluminescent flower: curved stem + alien bell-bloom with soft glow.
    Color varies by emotion: purple=sadness, blue=deep feeling, gold=joy,
    white=neutral, azure=loyalty, yellow=happiness."""
    out = []
    bx = fx + 3; by = fy - stem_h
    # Curved stem (slightly arching)
    out.append(f'<path d="M{fx},{fy} Q{fx-6},{fy-stem_h*0.55:.0f} {bx},{by}" '
               f'fill="none" stroke="#2A7818" stroke-width="3.5" stroke-linecap="round"/>')
    # Small leaves along stem
    for leaf_frac, leaf_side in [(0.35, -1), (0.60, 1)]:
        lx = fx + (bx-fx)*leaf_frac - leaf_side*3
        ly = fy - stem_h * leaf_frac
        lx2 = lx + leaf_side * 14
        out.append(f'<path d="M{lx:.0f},{ly:.0f} Q{lx2:.0f},{ly-10:.0f} {lx2-leaf_side*5:.0f},{ly-20:.0f} '
                   f'Q{lx:.0f},{ly-12:.0f} {lx:.0f},{ly:.0f}" fill="#3A9028" opacity="0.80"/>')
    # Outer glow halos (bioluminescence)
    out.append(f'<circle cx="{bx}" cy="{by}" r="{size*2.8:.1f}" fill="{glow_col}" opacity="0.08"/>')
    out.append(f'<circle cx="{bx}" cy="{by}" r="{size*2.0:.1f}" fill="{glow_col}" opacity="0.15"/>')
    out.append(f'<circle cx="{bx}" cy="{by}" r="{size*1.4:.1f}" fill="{glow_col}" opacity="0.25"/>')
    # Calyx (green sepal cup under bloom)
    out.append(f'<ellipse cx="{bx}" cy="{by+size*0.55:.1f}" rx="{size*0.60:.1f}" ry="{size*0.30:.1f}" '
               f'fill="#2A7818" opacity="0.88"/>')
    # Outer petals — 5 bell-shaped drooping petals (alien, elongated)
    for i in range(5):
        ang = math.radians(i * 72 + 36)
        px = bx + math.cos(ang) * size * 0.78
        py = by + math.sin(ang) * size * 0.55 + size * 0.35
        out.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{size*0.42:.1f}" ry="{size*0.85:.1f}" '
                   f'fill="{glow_col}" opacity="0.78" '
                   f'transform="rotate({i*72+36},{px:.1f},{py:.1f})"/>')
    # Inner petals (shorter, brighter)
    for i in range(5):
        ang = math.radians(i * 72)
        px = bx + math.cos(ang) * size * 0.42
        py = by + math.sin(ang) * size * 0.35 + size * 0.10
        out.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{size*0.28:.1f}" ry="{size*0.55:.1f}" '
                   f'fill="{inner_col}" opacity="0.85" '
                   f'transform="rotate({i*72},{px:.1f},{py:.1f})"/>')
    # Central glowing cup / pistil
    out.append(f'<ellipse cx="{bx}" cy="{by+size*0.15:.1f}" rx="{size*0.52:.1f}" ry="{size*0.42:.1f}" '
               f'fill="{inner_col}" opacity="0.92"/>')
    out.append(f'<circle cx="{bx}" cy="{by}" r="{size*0.28:.1f}" fill="#FFFFFF" opacity="0.85"/>')
    return ''.join(out)

def elpis_pillar(px, py, h=90, w=16):
    """Elpis Stone Pillar: cylindrical ancient column crowned with lush greenery."""
    out = []
    # Base plinth
    out.append(f'<rect x="{px-w//2-4}" y="{py-8}" width="{w+8}" height="10" '
               f'fill="url(#eStone)" rx="2" opacity="0.90"/>')
    # Column body (slight taper)
    out.append(f'<rect x="{px-w//2}" y="{py-8-h}" width="{w}" height="{h}" '
               f'fill="url(#eStone)" rx="4" opacity="0.95"/>')
    # Shadow side
    out.append(f'<rect x="{px+w//2-4}" y="{py-8-h}" width="4" height="{h}" '
               f'fill="#A09080" rx="2" opacity="0.40"/>')
    # Capital (flared top)
    out.append(f'<rect x="{px-w//2-5}" y="{py-8-h-6}" width="{w+10}" height="8" '
               f'fill="url(#eStone)" rx="2" opacity="0.92"/>')
    # Gold band on capital
    out.append(f'<rect x="{px-w//2-5}" y="{py-8-h-9}" width="{w+10}" height="3" '
               f'fill="url(#eGold)" opacity="0.72"/>')
    # Lush greenery crown atop column
    crown_cx = px; crown_cy = py - 8 - h - 12
    for bmp_off, bmp_r, bmp_op in [
        (0, w*0.85, 0.90), (-w*0.50, w*0.65, 0.82), (w*0.50, w*0.65, 0.82),
        (-w*0.25, w*0.70, 0.78), (w*0.25, w*0.68, 0.80),
    ]:
        out.append(f'<circle cx="{crown_cx+bmp_off:.1f}" cy="{crown_cy:.0f}" r="{bmp_r:.1f}" '
                   f'fill="#3A9020" opacity="{bmp_op:.2f}"/>')
    # Brighter highlight on greenery
    out.append(f'<ellipse cx="{crown_cx-w*0.15:.1f}" cy="{crown_cy-w*0.18:.1f}" '
               f'rx="{w*0.38:.1f}" ry="{w*0.28:.1f}" fill="#58B038" opacity="0.65"/>')
    return ''.join(out)

def amaurotine_building(bx, by, bw, bh, side='left'):
    """Amaurotine research hall: red brick body with cream stone trim/columns,
    arched windows, roof garden. Side determines shadow direction."""
    out = []
    # Main brick body
    out.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" '
               f'fill="url(#eBrick)" rx="3" opacity="0.95"/>')
    # Cream stone facade strips (horizontal band courses every ~15%)
    for band_frac in [0.12, 0.28, 0.48, 0.68, 0.85]:
        bby = by + bh * band_frac
        out.append(f'<rect x="{bx-2}" y="{bby:.0f}" width="{bw+4}" height="{max(3,bh*0.04):.0f}" '
                   f'fill="url(#eStone)" opacity="0.70"/>')
    # Shadow on inner edge (depth)
    sw = bw * 0.10
    sx = bx + bw - sw if side == 'left' else bx
    out.append(f'<rect x="{sx:.0f}" y="{by}" width="{sw:.0f}" height="{bh}" '
               f'fill="#603020" opacity="0.30" rx="2"/>')
    # Arched windows (cream surround, warm amber interior)
    ww = bw * 0.28; wh = bh * 0.12
    for row in range(3):
        wy = by + bh * (0.20 + row * 0.24)
        wx = bx + bw * 0.36
        # Cream window surround
        out.append(f'<rect x="{wx-3:.0f}" y="{wy-3:.0f}" width="{ww+6:.0f}" height="{wh+5:.0f}" '
                   f'fill="url(#eStone)" rx="{ww*0.5:.0f}" opacity="0.80"/>')
        # Amber glass
        out.append(f'<rect x="{wx:.0f}" y="{wy:.0f}" width="{ww:.0f}" height="{wh:.0f}" '
                   f'fill="#FFD890" rx="{ww*0.45:.0f}" opacity="0.72"/>')
        # Warm light leak
        out.append(f'<ellipse cx="{wx+ww/2:.0f}" cy="{wy+wh/2:.0f}" '
                   f'rx="{ww*0.4:.0f}" ry="{wh*0.35:.0f}" fill="#FFE8B0" opacity="0.45"/>')
    # Roof garden (greenery at top)
    roof_y = by - 4
    for rg_off, rg_r in [(-bw*0.30, bw*0.22), (0, bw*0.26), (bw*0.30, bw*0.22),
                          (-bw*0.50, bw*0.16), (bw*0.50, bw*0.16)]:
        out.append(f'<circle cx="{bx+bw/2+rg_off:.1f}" cy="{roof_y:.0f}" r="{rg_r:.1f}" '
                   f'fill="#3A9020" opacity="0.88"/>')
    # Roof parapet (cream crenellation)
    out.append(f'<rect x="{bx-3}" y="{by-6}" width="{bw+6}" height="7" '
               f'fill="url(#eStone)" rx="2" opacity="0.82"/>')
    return ''.join(out)

def floating_island(ix, iy, iw, ih, tree_col='#2A8020', purple_tree=False):
    """Floating island with stone underbelly, grass cap, and trees."""
    out = []
    # Rocky underbelly
    out.append(f'<ellipse cx="{ix:.0f}" cy="{iy+ih*0.60:.0f}" rx="{iw/2:.0f}" ry="{ih*0.48:.0f}" '
               f'fill="#9A8870" opacity="0.92"/>')
    out.append(f'<ellipse cx="{ix:.0f}" cy="{iy+ih*0.60:.0f}" rx="{iw/2*0.78:.0f}" ry="{ih*0.36:.0f}" '
               f'fill="#B8A890" opacity="0.72"/>')
    # Soil layer
    out.append(f'<ellipse cx="{ix:.0f}" cy="{iy+ih*0.16:.0f}" rx="{iw/2+1:.0f}" ry="{ih*0.22:.0f}" '
               f'fill="#5A3818" opacity="0.80"/>')
    # Grass cap
    out.append(f'<ellipse cx="{ix:.0f}" cy="{iy+ih*0.10:.0f}" rx="{iw/2+2:.0f}" ry="{ih*0.20:.0f}" '
               f'fill="#4A9838" opacity="0.95"/>')
    out.append(f'<ellipse cx="{ix:.0f}" cy="{iy+ih*0.06:.0f}" rx="{iw/2:.0f}" ry="{ih*0.14:.0f}" '
               f'fill="#5AB040" opacity="0.85"/>')
    # Trees on island
    tc = '#6030A0' if purple_tree else tree_col
    lc = '#3A2870' if purple_tree else '#2A7018'
    offsets = [(-iw*0.28, ih*0.72, 1.0), (0, ih*0.88, 1.2), (iw*0.25, ih*0.65, 0.9)]
    for tx_off, th, tscale in offsets:
        tx2 = ix + tx_off; ty2 = iy + ih * 0.06
        out.append(f'<line x1="{tx2:.0f}" y1="{ty2:.0f}" x2="{tx2:.0f}" y2="{ty2-th*tscale:.0f}" '
                   f'stroke="#5A3A18" stroke-width="{2.5*tscale:.1f}"/>')
        out.append(f'<ellipse cx="{tx2:.0f}" cy="{ty2-th*tscale:.0f}" '
                   f'rx="{th*0.42*tscale:.0f}" ry="{th*0.35*tscale:.0f}" '
                   f'fill="{tc}" opacity="0.90"/>')
        if purple_tree:
            # Extra leaf spread for the Noetophoreon purple tree
            out.append(f'<ellipse cx="{tx2-th*0.20*tscale:.0f}" cy="{ty2-th*tscale+th*0.12:.0f}" '
                       f'rx="{th*0.30*tscale:.0f}" ry="{th*0.22*tscale:.0f}" '
                       f'fill="{tc}" opacity="0.75"/>')
    return ''.join(out)

# ─────────────────────────────────────────────────────────────────────────────
#  GRADIENTS
# ─────────────────────────────────────────────────────────────────────────────
A('<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"><defs>')

# SKY: BRIGHT CLEAR BLUE (daylight — Elpis has a perfect clear blue sky with visible sun)
A('<linearGradient id="eSky" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#1848B8"/>'   # deep sky blue zenith
  '<stop offset="18%"  stop-color="#2A68D8"/>'   # vivid sky blue
  '<stop offset="38%"  stop-color="#4090E8"/>'   # mid sky blue
  '<stop offset="60%"  stop-color="#68B0F0"/>'   # lighter blue
  '<stop offset="80%"  stop-color="#90CAF5"/>'   # pale horizon blue
  '<stop offset="100%" stop-color="#B8DCF8"/>'   # bright horizon
  '</linearGradient>')

# Sun glow (warm radial, upper-left area)
A('<radialGradient id="eSun" cx="30%" cy="8%" r="55%">'
  '<stop offset="0%"   stop-color="#FFFCE0" stop-opacity="1.00"/>'
  '<stop offset="8%"   stop-color="#FFF5A0" stop-opacity="0.90"/>'
  '<stop offset="22%"  stop-color="#FFE870" stop-opacity="0.55"/>'
  '<stop offset="42%"  stop-color="#FFD848" stop-opacity="0.22"/>'
  '<stop offset="68%"  stop-color="#F8C820" stop-opacity="0.06"/>'
  '<stop offset="100%" stop-color="#E0A000" stop-opacity="0"/>'
  '</radialGradient>')

# Cloud (bright white, sunlit)
A('<radialGradient id="eCloud" cx="40%" cy="35%" r="62%">'
  '<stop offset="0%"   stop-color="#FFFFFF"  stop-opacity="0.98"/>'
  '<stop offset="35%"  stop-color="#F5F8FF"  stop-opacity="0.90"/>'
  '<stop offset="65%"  stop-color="#EAF0FF"  stop-opacity="0.68"/>'
  '<stop offset="100%" stop-color="#D8E8FF"  stop-opacity="0"/>'
  '</radialGradient>')

# Cloud sea (below islands — white expanse)
A('<linearGradient id="eCloudSea" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FAFCFF" stop-opacity="0.90"/>'
  '<stop offset="40%"  stop-color="#EEF4FF" stop-opacity="0.80"/>'
  '<stop offset="100%" stop-color="#D8E8FF" stop-opacity="0.95"/>'
  '</linearGradient>')

# Red brick (Amaurotine in daylight — warm brick with reddish tone)
A('<linearGradient id="eBrick" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#C86848"/>'
  '<stop offset="30%"  stop-color="#B85838"/>'
  '<stop offset="65%"  stop-color="#A04A2A"/>'
  '<stop offset="100%" stop-color="#8A3A20"/>'
  '</linearGradient>')

# Cream/pale stone accents (column, trim, window surrounds)
A('<linearGradient id="eStone" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#EDE5C8"/>'
  '<stop offset="40%"  stop-color="#DDD5B8"/>'
  '<stop offset="100%" stop-color="#C8C0A0"/>'
  '</linearGradient>')

# Gold trim
A('<linearGradient id="eGold" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FFF8C0"/>'
  '<stop offset="35%"  stop-color="#E8C840"/>'
  '<stop offset="70%"  stop-color="#C0A020"/>'
  '<stop offset="100%" stop-color="#907808"/>'
  '</linearGradient>')

# Lush green ground (island surface)
A('<linearGradient id="eGnd" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#4EA838"/>'
  '<stop offset="30%"  stop-color="#3A8828"/>'
  '<stop offset="65%"  stop-color="#246A18"/>'
  '<stop offset="100%" stop-color="#164A10"/>'
  '</linearGradient>')

# Purple tree leaves (Noetophoreon — the iconic island with purple tree)
A('<radialGradient id="ePurpleTree" cx="45%" cy="35%" r="60%">'
  '<stop offset="0%"   stop-color="#C890E8"/>'
  '<stop offset="45%"  stop-color="#9050C0"/>'
  '<stop offset="100%" stop-color="#601890"/>'
  '</radialGradient>')

# Propylaea (gate) aether energy field
A('<linearGradient id="eGateField" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#C0FFEE" stop-opacity="0.05"/>'
  '<stop offset="25%"  stop-color="#80F0D8" stop-opacity="0.30"/>'
  '<stop offset="50%"  stop-color="#50E8C8" stop-opacity="0.42"/>'
  '<stop offset="75%"  stop-color="#80F0D8" stop-opacity="0.28"/>'
  '<stop offset="100%" stop-color="#C0FFEE" stop-opacity="0.05"/>'
  '</linearGradient>')

# Propylaea pad (circular teleporter)
A('<radialGradient id="ePad" cx="50%" cy="45%" r="55%">'
  '<stop offset="0%"   stop-color="#C0FFF0" stop-opacity="0.80"/>'
  '<stop offset="35%"  stop-color="#60E8D0" stop-opacity="0.65"/>'
  '<stop offset="70%"  stop-color="#20C0A8" stop-opacity="0.50"/>'
  '<stop offset="100%" stop-color="#0A9080" stop-opacity="0.40"/>'
  '</radialGradient>')

# Creation orb
A('<radialGradient id="eOrb" cx="38%" cy="32%" r="62%">'
  '<stop offset="0%"   stop-color="#FFFFFF"  stop-opacity="1.00"/>'
  '<stop offset="18%"  stop-color="#C0F8E8"  stop-opacity="0.95"/>'
  '<stop offset="48%"  stop-color="#58D0C0"  stop-opacity="0.90"/>'
  '<stop offset="80%"  stop-color="#18A0A8"  stop-opacity="0.93"/>'
  '<stop offset="100%" stop-color="#0A6880"  stop-opacity="0.96"/>'
  '</radialGradient>')

# Altar platform (marble-white, simple)
A('<linearGradient id="eAltarV" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#F8F5EC"/>'
  '<stop offset="50%"  stop-color="#E8E3D5"/>'
  '<stop offset="100%" stop-color="#CEC8B5"/>'
  '</linearGradient>')

# Stone path
A('<linearGradient id="ePath" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#C0B8A0"/>'
  '<stop offset="55%"  stop-color="#A8A090"/>'
  '<stop offset="100%" stop-color="#888075"/>'
  '</linearGradient>')

# Atmospheric haze (base of image)
A('<linearGradient id="eHaze" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#204010" stop-opacity="0"/>'
  '<stop offset="45%"  stop-color="#1A3810" stop-opacity="0.28"/>'
  '<stop offset="100%" stop-color="#102808" stop-opacity="0.65"/>'
  '</linearGradient>')

# Vignette (edges darken subtly — sky blue version)
A('<radialGradient id="eVig" cx="50%" cy="10%" r="95%">'
  '<stop offset="58%"  stop-color="#000000" stop-opacity="0"/>'
  '<stop offset="100%" stop-color="#102050" stop-opacity="0.38"/>'
  '</radialGradient>')

# Grass gradient (tall foreground grass)
A('<linearGradient id="eGrass" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#60B840"/>'
  '<stop offset="55%"  stop-color="#3E8C28"/>'
  '<stop offset="100%" stop-color="#205010"/>'
  '</linearGradient>')

A('</defs>')

# ─────────────────────────────────────────────────────────────────────────────
#  1. SKY BACKGROUND (bright clear blue — actual Elpis daylight)
# ─────────────────────────────────────────────────────────────────────────────
A('<rect width="400" height="600" fill="url(#eSky)"/>')
# Sun glow (upper-left, soft warm bloom — no harsh disc)
A('<rect width="400" height="600" fill="url(#eSun)"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  2. SKY CLOUDS (bright white daylight clouds)
# ─────────────────────────────────────────────────────────────────────────────
A(cloud(68,  58, 54, 22, 0.88))
A(cloud(42,  72, 30, 14, 0.75))
A(cloud(105, 62, 32, 14, 0.72))
A(cloud(270, 44, 62, 26, 0.86))
A(cloud(240, 58, 38, 16, 0.75))
A(cloud(320, 54, 36, 15, 0.72))
A(cloud(192, 76, 44, 18, 0.68))
A(cloud(155, 84, 26, 11, 0.58))
A(cloud(380, 70, 30, 13, 0.65))

# ─────────────────────────────────────────────────────────────────────────────
#  3. DISTANT FLOATING ISLANDS IN SKY
#     (Elpis zones are floating islands visible across the distance)
# ─────────────────────────────────────────────────────────────────────────────
# Far-left island — Noetophoreon reference (purple-leaf tree)
A(floating_island(75, 118, 68, 28, tree_col='#2A8020', purple_tree=True))
# Far-right island
A(floating_island(325, 100, 58, 25, tree_col='#1E7818'))
# Smaller distant islands
A(floating_island(190, 110, 42, 18, tree_col='#257020'))
A(floating_island(370, 140, 32, 14, tree_col='#2A7820'))
A(floating_island(42, 158, 26, 12, tree_col='#1A7010'))

# ─────────────────────────────────────────────────────────────────────────────
#  4. CLOUD SEA (below the floating island platform we stand on)
#     Visible on both sides — defining Elpis visual
# ─────────────────────────────────────────────────────────────────────────────
# Cloud sea fills mid-background
A('<rect x="0" y="268" width="400" height="80" fill="url(#eCloudSea)" opacity="0.88"/>')
# Cloud sea top edge (fluffy bumps)
cloud_sea_bumps = [
    (20, 272, 30, 12), (65, 265, 38, 14), (108, 270, 32, 11),
    (155, 262, 42, 16), (200, 268, 36, 13), (248, 260, 44, 17),
    (295, 266, 35, 13), (340, 262, 38, 15), (385, 270, 28, 11),
]
for bcx, bcy, brx, bry in cloud_sea_bumps:
    A(f'<ellipse cx="{bcx}" cy="{bcy}" rx="{brx}" ry="{bry}" fill="url(#eCloud)" opacity="0.85"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  5. KTISIS HYPERBOREIA — Distant monolithic research building (background)
#     Massive, angular, slightly hazy with atmospheric distance
# ─────────────────────────────────────────────────────────────────────────────
# Central distant building silhouette (just haze outline, far away)
A('<rect x="148" y="185" width="104" height="90" fill="#C0B8A0" rx="4" opacity="0.38"/>')
A('<rect x="163" y="170" width="74" height="30" fill="#C0B8A0" rx="3" opacity="0.30"/>')
A('<rect x="172" y="158" width="56" height="22" fill="#B8B0A0" rx="2" opacity="0.22"/>')
# Cream stone band courses on distant building
for dy in [185, 205, 228, 252]:
    A(f'<rect x="148" y="{dy}" width="104" height="4" fill="#DDD5B8" rx="1" opacity="0.25"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  6. AMAUROTINE RESEARCH HALLS (left and right — red brick + cream trim)
# ─────────────────────────────────────────────────────────────────────────────
# Left main building
A(amaurotine_building(bx=-14, by=172, bw=96, bh=228, side='left'))
# Left secondary (behind/smaller)
A(amaurotine_building(bx=-8, by=215, bw=68, bh=175, side='left'))

# Right main building
A(amaurotine_building(bx=318, by=172, bw=96, bh=228, side='right'))
# Right secondary
A(amaurotine_building(bx=340, by=218, bw=68, bh=175, side='right'))

# ─────────────────────────────────────────────────────────────────────────────
#  7. ELPIS STONE PILLARS (crowned with greenery — signature furnishing of zone)
# ─────────────────────────────────────────────────────────────────────────────
A(elpis_pillar(92,  390, h=95, w=18))
A(elpis_pillar(122, 378, h=82, w=16))
A(elpis_pillar(278, 382, h=88, w=17))
A(elpis_pillar(310, 392, h=96, w=18))
# Central pillars flanking path (smaller)
A(elpis_pillar(158, 360, h=70, w=14))
A(elpis_pillar(242, 360, h=70, w=14))

# ─────────────────────────────────────────────────────────────────────────────
#  8. LUSH GREEN ISLAND GROUND (the island platform we walk on)
# ─────────────────────────────────────────────────────────────────────────────
A('<rect y="340" width="400" height="260" fill="url(#eGnd)"/>')

# Gentle grass slope at ground edge
A('<path d="M0,346 Q50,328 120,340 Q180,325 240,338 Q305,322 370,336 Q390,328 400,336 L400,355 L0,355 Z" '
  'fill="#50A838" opacity="0.65"/>')
A('<path d="M0,342 Q80,332 155,342 Q205,328 255,340 Q320,325 400,340 L400,350 L0,350 Z" '
  'fill="#60B848" opacity="0.42"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  9. ANCIENT STONE PATH (mossy, down center)
# ─────────────────────────────────────────────────────────────────────────────
A('<path d="M168,600 L172,540 L176,480 L179,420 L181,375 L183,350" '
  'fill="none" stroke="url(#ePath)" stroke-width="22" stroke-linecap="round" opacity="0.80"/>')
A('<path d="M168,600 L172,540 L176,480 L179,420 L181,375 L183,350" '
  'fill="none" stroke="#CCC0A0" stroke-width="17" stroke-linecap="round" opacity="0.55"/>')
# Stone slab joints
for sy in [365, 392, 420, 450, 480, 512, 548]:
    A(f'<line x1="166" y1="{sy}" x2="190" y2="{sy}" stroke="#A09880" stroke-width="1.3" opacity="0.45"/>')
# Mossy path edges
A('<path d="M165,600 L169,540 L173,480 L176,420 L178,375 L180,350" '
  'fill="none" stroke="#3A8828" stroke-width="2.5" stroke-dasharray="5,5" opacity="0.35"/>')
A('<path d="M189,600 L193,540 L197,480 L200,420 L202,375 L204,350" '
  'fill="none" stroke="#3A8828" stroke-width="2.5" stroke-dasharray="5,5" opacity="0.35"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  10. ELPIS FLOWERS — the zone's most iconic element
#      Bioluminescent, emotion-color-linked, alien bell-tulip shape
#      Purple=Hermes sadness, Blue=deep feeling, Gold=joy,
#      White=neutral, Azure=loyalty, Yellow=happiness
# ─────────────────────────────────────────────────────────────────────────────
# Clusters left side
A(elpis_flower(30,  450, '#9040D0', '#C080FF', stem_h=60, size=11))  # purple (Hermes)
A(elpis_flower(58,  468, '#2060E0', '#70B0FF', stem_h=52, size=9))   # blue (deep feeling)
A(elpis_flower(88,  458, '#E8C020', '#FFF080', stem_h=64, size=12))  # gold (joy)
A(elpis_flower(45,  500, '#20A8D8', '#90E8FF', stem_h=48, size=9))   # azure (loyalty)
A(elpis_flower(72,  510, '#FFFBF0', '#FFFBE8', stem_h=44, size=8))   # white (neutral)
A(elpis_flower(100, 488, '#F0D020', '#FFF0A0', stem_h=56, size=10))  # yellow (happiness)
A(elpis_flower(24,  530, '#8030C0', '#B870FF', stem_h=50, size=9))   # purple
A(elpis_flower(112, 520, '#1850D0', '#5090FF', stem_h=46, size=8))   # blue

# Clusters right side
A(elpis_flower(302, 452, '#E8C020', '#FFF080', stem_h=62, size=12))  # gold
A(elpis_flower(330, 466, '#9040D0', '#C080FF', stem_h=54, size=10))  # purple
A(elpis_flower(358, 456, '#20A8D8', '#90E8FF', stem_h=60, size=11))  # azure
A(elpis_flower(315, 498, '#2060E0', '#70B0FF', stem_h=50, size=9))   # blue
A(elpis_flower(345, 510, '#FFFBF0', '#FFFBE8', stem_h=46, size=9))   # white
A(elpis_flower(372, 488, '#F0D020', '#FFF0A0', stem_h=58, size=10))  # yellow
A(elpis_flower(298, 530, '#8030C0', '#B870FF', stem_h=48, size=8))   # purple
A(elpis_flower(380, 522, '#E8C020', '#FFF080', stem_h=44, size=8))   # gold

# Scattered mid-ground flowers (near path)
A(elpis_flower(138, 412, '#9040D0', '#C080FF', stem_h=40, size=7))
A(elpis_flower(220, 408, '#20A8D8', '#90E8FF', stem_h=38, size=7))
A(elpis_flower(145, 438, '#E8C020', '#FFF080', stem_h=36, size=6))
A(elpis_flower(215, 440, '#FFFBF0', '#FFFBE8', stem_h=34, size=6))
A(elpis_flower(128, 460, '#2060E0', '#70B0FF', stem_h=42, size=7))
A(elpis_flower(232, 456, '#F0D020', '#FFF0A0', stem_h=40, size=7))

# ─────────────────────────────────────────────────────────────────────────────
#  11. STAGE 5 — Creation/Research Area with Prototype Orb
#      (shifted +52px in transform, design around x=148)
# ─────────────────────────────────────────────────────────────────────────────
alt_cx = 148   # renders at 200 after stage5 transform (+52)
alt_base = 235

# Three-tier circular research platform (clean marble)
for tier_rx, tier_h, tier_y_off in [(48, 12, 0), (33, 10, -15), (20, 8, -28)]:
    ty = alt_base - tier_y_off
    A(f'<ellipse cx="{alt_cx}" cy="{ty}" rx="{tier_rx}" ry="{tier_rx*0.24:.0f}" fill="url(#eAltarV)" opacity="0.92"/>')
    A(f'<rect x="{alt_cx-tier_rx}" y="{ty-tier_h}" width="{tier_rx*2}" height="{tier_h}" '
      f'fill="url(#eAltarV)" opacity="0.90"/>')
    A(f'<ellipse cx="{alt_cx}" cy="{ty-tier_h}" rx="{tier_rx}" ry="{tier_rx*0.22:.0f}" fill="url(#eAltarV)" opacity="0.88"/>')
    A(f'<ellipse cx="{alt_cx}" cy="{ty-tier_h}" rx="{tier_rx}" ry="{tier_rx*0.10:.0f}" fill="url(#eGold)" opacity="0.60"/>')
    # Rune inscriptions around tier
    for ri in range(5):
        ang = math.radians(ri * 72 + 20)
        rx2 = alt_cx + math.cos(ang) * tier_rx * 0.68
        ry2 = ty - 2 + math.sin(ang) * tier_rx * 0.12
        A(f'<ellipse cx="{rx2:.0f}" cy="{ry2:.0f}" rx="3.5" ry="1.5" fill="#C8B840" rx2="1" opacity="0.55"/>')

# Central pillar
A(f'<rect x="{alt_cx-5}" y="{alt_base-76}" width="10" height="32" fill="url(#eAltarV)" rx="2" opacity="0.90"/>')
A(f'<rect x="{alt_cx-5}" y="{alt_base-76}" width="10" height="2.5" fill="url(#eGold)" opacity="0.72"/>')
A(f'<rect x="{alt_cx-5}" y="{alt_base-46}" width="10" height="2.5" fill="url(#eGold)" opacity="0.72"/>')

# Prototype creature orb (heart of the creation ritual)
orb_cy = alt_base - 97
A(f'<circle cx="{alt_cx}" cy="{orb_cy}" r="26" fill="#50D8C8" opacity="0.12"/>')
A(f'<circle cx="{alt_cx}" cy="{orb_cy}" r="20" fill="#38C8B8" opacity="0.18"/>')
A(f'<circle cx="{alt_cx}" cy="{orb_cy}" r="16" fill="url(#eOrb)" opacity="0.95"/>')
# Interior form (abstract creature taking shape)
A(f'<path d="M{alt_cx-4},{orb_cy-4} Q{alt_cx+6},{orb_cy-8} {alt_cx+8},{orb_cy+1} '
  f'Q{alt_cx+4},{orb_cy+7} {alt_cx-3},{orb_cy+6} Q{alt_cx-9},{orb_cy+2} {alt_cx-4},{orb_cy-4}" '
  f'fill="#FFFFFF" opacity="0.42"/>')
# Glass ring
A(f'<circle cx="{alt_cx}" cy="{orb_cy}" r="16" fill="none" stroke="#FFFFFF" stroke-width="1.5" opacity="0.48"/>')
# Highlight
A(f'<circle cx="{alt_cx-5}" cy="{orb_cy-5}" r="5" fill="#FFFFFF" opacity="0.65"/>')
# Orbiting colored aether sparks (match Elpis flower colors)
for sc, sang in [('#C080FF',0),('#70B0FF',60),('#FFF080',120),('#90E8FF',180),('#FFFBE8',240),('#FFF0A0',300)]:
    rad = math.radians(sang)
    sx = alt_cx + math.cos(rad)*23; sy = orb_cy + math.sin(rad)*9
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="3" fill="{sc}" opacity="0.92"/>')
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="6" fill="{sc}" opacity="0.18"/>')
# Aether beams rising from orb
for bang in [-50, -25, 0, 25, 50]:
    brad = math.radians(bang - 90)
    bx2 = alt_cx + math.cos(brad)*85; by2 = orb_cy + math.sin(brad)*85
    op = 0.050 - abs(bang)*0.0004
    A(f'<line x1="{alt_cx}" y1="{orb_cy}" x2="{bx2:.0f}" y2="{by2:.0f}" '
      f'stroke="#80F0E0" stroke-width="1.5" opacity="{max(0.008,op):.3f}"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  12. STAGE 10 — PROPYLAEA (Grand Amaurotine Gate / Teleporter Structure)
#      Scale 1.5× centered on (200, 531). Design at natural size around x=200
# ─────────────────────────────────────────────────────────────────────────────
gate_cx = 200; gate_base = 580

# Ground platform / threshold
A(f'<rect x="{gate_cx-75}" y="{gate_base-8}" width="150" height="14" fill="url(#eStone)" rx="3" opacity="0.92"/>')
A(f'<rect x="{gate_cx-75}" y="{gate_base-10}" width="150" height="3" fill="url(#eGold)" opacity="0.78"/>')
# Threshold inscription
for ri in range(10):
    A(f'<rect x="{gate_cx-60+ri*13}" y="{gate_base-7}" width="7" height="3" '
      f'fill="#D8C840" rx="1" opacity="0.58"/>')

# Teleporter pad (circular glowing platform in threshold)
A(f'<ellipse cx="{gate_cx}" cy="{gate_base+2}" rx="42" ry="10" fill="url(#ePad)" opacity="0.85"/>')
A(f'<ellipse cx="{gate_cx}" cy="{gate_base+2}" rx="42" ry="10" fill="none" '
  f'stroke="#60F0E0" stroke-width="1.5" opacity="0.55"/>')
# Pad inner ring
A(f'<ellipse cx="{gate_cx}" cy="{gate_base+2}" rx="28" ry="6.5" fill="none" '
  f'stroke="#80FFF0" stroke-width="1.0" opacity="0.40"/>')

# Left column (red brick + cream trim, tall)
col_w = 24; col_h = 118
A(f'<rect x="{gate_cx-76}" y="{gate_base-8-col_h}" width="{col_w}" height="{col_h}" '
  f'fill="url(#eBrick)" rx="3" opacity="0.95"/>')
# Cream band courses on column
for band_frac in [0.15, 0.35, 0.56, 0.76, 0.92]:
    by2 = gate_base - 8 - col_h + col_h * band_frac
    A(f'<rect x="{gate_cx-77}" y="{by2:.0f}" width="{col_w+2}" height="4.5" '
      f'fill="url(#eStone)" opacity="0.72"/>')
# Capital (cream stone, flared)
A(f'<rect x="{gate_cx-80}" y="{gate_base-8-col_h-8}" width="{col_w+8}" height="10" '
  f'fill="url(#eStone)" rx="2" opacity="0.92"/>')
A(f'<rect x="{gate_cx-80}" y="{gate_base-8-col_h-11}" width="{col_w+8}" height="3.5" '
  f'fill="url(#eGold)" opacity="0.78"/>')
# Column base plinth
A(f'<rect x="{gate_cx-80}" y="{gate_base-12}" width="{col_w+8}" height="6" '
  f'fill="url(#eStone)" rx="2" opacity="0.90"/>')
A(f'<rect x="{gate_cx-80}" y="{gate_base-15}" width="{col_w+8}" height="3.5" '
  f'fill="url(#eGold)" opacity="0.75"/>')
# Greenery atop capital
A(f'<ellipse cx="{gate_cx-68}" cy="{gate_base-8-col_h-14}" rx="14" ry="8" fill="#3A9020" opacity="0.88"/>')
A(f'<ellipse cx="{gate_cx-72}" cy="{gate_base-8-col_h-16}" rx="9" ry="6" fill="#4AA830" opacity="0.80"/>')

# Right column (mirror)
A(f'<rect x="{gate_cx+52}" y="{gate_base-8-col_h}" width="{col_w}" height="{col_h}" '
  f'fill="url(#eBrick)" rx="3" opacity="0.92"/>')
for band_frac in [0.15, 0.35, 0.56, 0.76, 0.92]:
    by2 = gate_base - 8 - col_h + col_h * band_frac
    A(f'<rect x="{gate_cx+51}" y="{by2:.0f}" width="{col_w+2}" height="4.5" '
      f'fill="url(#eStone)" opacity="0.72"/>')
A(f'<rect x="{gate_cx+48}" y="{gate_base-8-col_h-8}" width="{col_w+8}" height="10" '
  f'fill="url(#eStone)" rx="2" opacity="0.92"/>')
A(f'<rect x="{gate_cx+48}" y="{gate_base-8-col_h-11}" width="{col_w+8}" height="3.5" '
  f'fill="url(#eGold)" opacity="0.78"/>')
A(f'<rect x="{gate_cx+48}" y="{gate_base-12}" width="{col_w+8}" height="6" '
  f'fill="url(#eStone)" rx="2" opacity="0.90"/>')
A(f'<rect x="{gate_cx+48}" y="{gate_base-15}" width="{col_w+8}" height="3.5" '
  f'fill="url(#eGold)" opacity="0.75"/>')
A(f'<ellipse cx="{gate_cx+68}" cy="{gate_base-8-col_h-14}" rx="14" ry="8" fill="#3A9020" opacity="0.88"/>')
A(f'<ellipse cx="{gate_cx+72}" cy="{gate_base-8-col_h-16}" rx="9" ry="6" fill="#4AA830" opacity="0.80"/>')

# Arch (smooth broad Amaurotine arch — NOT Gothic, smooth segmental)
arch_base_y = gate_base - 8 - col_h + 14
arch_peak_y = arch_base_y - 46
arch_lx = gate_cx - 52; arch_rx = gate_cx + 52

A(f'<path d="M{arch_lx},{arch_base_y} C{arch_lx},{arch_peak_y} {arch_rx},{arch_peak_y} {arch_rx},{arch_base_y}" '
  f'fill="none" stroke="url(#eBrick)" stroke-width="18" stroke-linecap="butt" opacity="0.95"/>')
# Cream stone arch trim (outer)
A(f'<path d="M{arch_lx-5},{arch_base_y} C{arch_lx-5},{arch_peak_y-7} {arch_rx+5},{arch_peak_y-7} {arch_rx+5},{arch_base_y}" '
  f'fill="none" stroke="url(#eStone)" stroke-width="4" stroke-linecap="butt" opacity="0.78"/>')
# Gold arch rim (inner)
A(f'<path d="M{arch_lx+8},{arch_base_y} C{arch_lx+8},{arch_peak_y+6} {arch_rx-8},{arch_peak_y+6} {arch_rx-8},{arch_base_y}" '
  f'fill="none" stroke="url(#eGold)" stroke-width="2.5" stroke-linecap="butt" opacity="0.60"/>')

# Voussoir joints on arch (7)
for ji in range(7):
    t = (ji + 1) / 8.0
    bx2 = (1-t)**2*arch_lx + 2*(1-t)*t*gate_cx + t**2*arch_rx
    by2 = (1-t)**2*arch_base_y + 2*(1-t)*t*arch_peak_y + t**2*arch_base_y
    tdx = 2*(1-t)*(gate_cx-arch_lx) + 2*t*(arch_rx-gate_cx)
    tdy = 2*(1-t)*(arch_peak_y-arch_base_y) + 2*t*(arch_base_y-arch_peak_y)
    tlen = math.hypot(tdx, tdy) or 1
    nx = -tdy/tlen*11; ny = tdx/tlen*11
    A(f'<line x1="{bx2-nx*0.4:.1f}" y1="{by2-ny*0.4:.1f}" x2="{bx2+nx:.1f}" y2="{by2+ny:.1f}" '
      f'stroke="#DDD0A8" stroke-width="1.2" opacity="0.48"/>')

# Cream keystone
key_cx = gate_cx; key_cy = arch_peak_y - 1
A(f'<ellipse cx="{key_cx}" cy="{key_cy}" rx="12" ry="9" fill="url(#eStone)" opacity="0.90"/>')
A(f'<ellipse cx="{key_cx}" cy="{key_cy}" rx="12" ry="9" fill="none" stroke="url(#eGold)" stroke-width="1.5" opacity="0.70"/>')
# Sunflower rays on keystone
for ri in range(8):
    rang = math.radians(ri*45)
    A(f'<line x1="{key_cx+math.cos(rang)*9:.1f}" y1="{key_cy+math.sin(rang)*7:.1f}" '
      f'x2="{key_cx+math.cos(rang)*14:.1f}" y2="{key_cy+math.sin(rang)*11:.1f}" '
      f'stroke="#E0C028" stroke-width="2" stroke-linecap="round" opacity="0.72"/>')
A(f'<circle cx="{key_cx}" cy="{key_cy}" r="5" fill="#FFE848" opacity="0.88"/>')

# Propylaea aether energy shimmer inside arch
barrier_top = arch_peak_y + 5; barrier_bot = arch_base_y + 2; barrier_w = 86
A(f'<rect x="{gate_cx-barrier_w//2}" y="{barrier_top:.0f}" width="{barrier_w}" '
  f'height="{barrier_bot-barrier_top:.0f}" fill="url(#eGateField)" rx="5" opacity="0.90"/>')
# Vertical shimmer lines
for vi in range(6):
    vx = gate_cx - barrier_w//2 + 5 + vi * (barrier_w-10) // 5
    A(f'<line x1="{vx:.0f}" y1="{barrier_top:.0f}" x2="{vx:.0f}" y2="{barrier_bot:.0f}" '
      f'stroke="#80F0E0" stroke-width="1.0" opacity="0.22"/>')
# Horizontal scan line (moving aether)
scan_y = barrier_top + (barrier_bot-barrier_top)*0.45
A(f'<line x1="{gate_cx-barrier_w//2:.0f}" y1="{scan_y:.0f}" '
  f'x2="{gate_cx+barrier_w//2:.0f}" y2="{scan_y:.0f}" '
  f'stroke="#BFFFF0" stroke-width="2" opacity="0.28"/>')

# Elpis flowers climbing columns (small ones at column base)
for fx2, fy2, gc, ic, sh, sz in [
    (gate_cx-84, gate_base-30, '#9040D0','#C080FF', 38, 7),
    (gate_cx-78, gate_base-58, '#E8C020','#FFF080', 32, 6),
    (gate_cx+84, gate_base-30, '#20A8D8','#90E8FF', 38, 7),
    (gate_cx+78, gate_base-58, '#FFFBF0','#FFFBE8', 32, 6),
]:
    A(elpis_flower(fx2, fy2, gc, ic, stem_h=sh, size=sz))

# ─────────────────────────────────────────────────────────────────────────────
#  13. GRASS TUFTS (foreground texture)
# ─────────────────────────────────────────────────────────────────────────────
tufts = [
    (22,398,15), (50,405,13), (80,398,14), (108,404,12), (130,396,13),
    (205,398,12), (228,406,14), (252,398,13), (278,404,15), (302,398,13),
    (325,406,14), (350,398,15), (374,404,13), (392,398,12),
    (38,422,11), (68,428,13), (96,422,12), (148,426,11), (222,424,13),
    (248,428,12), (272,422,14), (300,426,11), (332,424,13), (362,428,12),
]
for gx, gy, gh in tufts:
    for goff in [-4, -1.5, 1.5, 4]:
        ang = math.radians(goff * 12 - 90)
        ex = gx + math.cos(ang)*gh; ey = gy + math.sin(ang)*gh
        A(f'<line x1="{gx}" y1="{gy}" x2="{ex:.1f}" y2="{ey:.1f}" '
          f'stroke="url(#eGrass)" stroke-width="1.5" stroke-linecap="round" opacity="0.82"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  14. ATMOSPHERE OVERLAYS
# ─────────────────────────────────────────────────────────────────────────────
# Ground depth haze
A('<rect y="505" width="400" height="95" fill="url(#eHaze)" opacity="0.62"/>')

# Floating aether motes (Elpis flower glow colors drifting in air)
motes = [
    (55, 210, 2.2, 1.4, '#9040D0', 0.62), (95, 198, 2.0, 1.3, '#2060E0', 0.58),
    (145, 185, 2.2, 1.4, '#E8C020', 0.62), (182, 202, 1.8, 1.1, '#20A8D8', 0.55),
    (225, 192, 2.0, 1.3, '#FFFBF0', 0.58), (262, 180, 1.8, 1.2, '#9040D0', 0.55),
    (308, 196, 2.2, 1.4, '#E8C020', 0.62), (348, 186, 2.0, 1.3, '#2060E0', 0.58),
    (44,  295, 1.8, 1.2, '#20A8D8', 0.50), (122, 285, 2.0, 1.3, '#9040D0', 0.55),
    (205, 278, 2.4, 1.5, '#FFFBF0', 0.60), (285, 290, 2.0, 1.3, '#E8C020', 0.52),
    (358, 282, 1.8, 1.2, '#2060E0', 0.50),
]
for mx, my, mrx, mry, mc, mop in motes:
    A(f'<ellipse cx="{mx}" cy="{my}" rx="{mrx}" ry="{mry}" fill="{mc}" opacity="{mop}"/>')
    A(f'<ellipse cx="{mx}" cy="{my}" rx="{mrx*3.2:.1f}" ry="{mry*3.2:.1f}" fill="{mc}" opacity="{mop*0.10:.2f}"/>')

# Subtle sun light shafts (very faint, from upper-left where sun is)
for ang in [-48, -30, -14, -4, 6, 18, 35]:
    rad = math.radians(ang - 90)
    lx = 120 + 420*math.cos(rad); ly = 30 + 420*math.sin(rad)
    op = max(0.005, 0.038 - abs(ang+10)*0.0005)
    sw = max(0.4, 1.8 - abs(ang)*0.03)
    A(f'<line x1="120" y1="30" x2="{lx:.0f}" y2="{ly:.0f}" '
      f'stroke="#FFE890" stroke-width="{sw:.1f}" opacity="{op:.3f}"/>')

# Vignette (subtle edge darkening)
A('<rect width="400" height="600" fill="url(#eVig)"/>')

A('</svg>')

# ─────────────────────────────────────────────────────────────────────────────
#  VALIDATE + INJECT
# ─────────────────────────────────────────────────────────────────────────────
svg = ''.join(parts)
print(f'ULTIMATE SVG: {len(svg):,} chars')

ro = len(_re.findall(r'<radialGradient', svg))
rc = len(_re.findall(r'</radialGradient', svg))
lo = len(_re.findall(r'<linearGradient', svg))
lc = len(_re.findall(r'</linearGradient', svg))
print(f'  radialGradient: {ro}/{rc}  linearGradient: {lo}/{lc}')
if ro != rc: raise RuntimeError(f'radialGradient mismatch: {ro} vs {rc}')
if lo != lc: raise RuntimeError(f'linearGradient mismatch: {lo} vs {lc}')

if svg.count('`'): raise RuntimeError('Backtick in SVG!')
if svg.count("'"): raise RuntimeError('Single quote in SVG!')

import xml.etree.ElementTree as ET
try:
    ET.fromstring(svg)
    print('  XML parse: OK')
except ET.ParseError as e:
    raise RuntimeError(f'XML parse error: {e}')

# CSS fallback update
html2 = html
for old, new in [
    ('#game-view[data-diff="ULTIMATE"] { background: rgb(56,80,168); }',
     '#game-view[data-diff="ULTIMATE"] { background: rgb(26,72,184); }'),
]:
    if old in html2:
        html2 = html2.replace(old, new)
        print(f'  Replaced CSS: {old[:60]}')

# ULTIMATE uses backtick template literal
pattern = r"(if\(diff===.ULTIMATE.\) return \`)(.*?)(\`;)"
repl = lambda m: m.group(1) + svg + m.group(3)
new_html, n = _re.subn(pattern, repl, html2, flags=_re.DOTALL)
if n == 0:
    raise RuntimeError("ULTIMATE pattern not found in stage.html")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print(f'stage.html written. ({n} replacement)')
