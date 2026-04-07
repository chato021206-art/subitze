#!/usr/bin/env python3
"""gen_ultimate.py — ULTIMATE background: Elpis (FF14 Endwalker).
Ancient garden of creation — 12,000 years before the present age.

Key visual accuracy targets:
  - Sky: warm golden-hour palette (soft periwinkle→rose→peach→amber gold)
         NOT dark purple — Elpis feels like eternal sunset paradise
  - Floating islands with vegetation in upper sky (signature Elpis element)
  - Amaurotine Research Halls: smooth ivory-marble towers, gold trim bands,
    rounded domes, crystal spires — geometric/art-deco NOT Gothic spires
  - Lush green meadow with wildflowers + oversized fantastical flowers
  - Lily pond in mid-ground
  - Soft pink-white clouds
  - Stage 5: Creation Altar with glowing prototype creature orb
  - Stage 10: Grand Amaurotine arch gate
"""
import re as _re, math

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    html = f.read()

parts = []
def A(s): parts.append(s)

# ─────────────────────────────────────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def wildflower(fx, fy, fc, size=4.5, fc2='#FFFFFF'):
    """6-petal wildflower with center disk."""
    petals = []
    for i in range(6):
        ang = math.radians(i * 60)
        px = fx + math.cos(ang) * size * 1.15
        py = fy + math.sin(ang) * size * 1.15
        petals.append(
            f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{size:.1f}" ry="{size*0.55:.1f}" '
            f'fill="{fc}" opacity="0.92" '
            f'transform="rotate({i*60},{px:.1f},{py:.1f})"/>'
        )
    return ''.join(petals) + f'<circle cx="{fx}" cy="{fy}" r="{size*0.45:.1f}" fill="{fc2}" opacity="0.96"/>'

def giant_flower(cx, base_y, petal_r, center_r, petal_col, center_col,
                 n_petals=7, stem_h=60, leaf_col='#2A7020'):
    """Giant fantastical flower: stem + leaves + petals + glowing center."""
    out = []
    stem_x = cx
    stem_top_y = base_y - stem_h
    # Stem
    out.append(f'<line x1="{stem_x}" y1="{base_y}" x2="{stem_x}" y2="{stem_top_y}" '
               f'stroke="{leaf_col}" stroke-width="4.5" stroke-linecap="round"/>')
    # Two leaves
    for side in [-1, 1]:
        lx = stem_x + side * petal_r * 0.8
        ly = base_y - stem_h * 0.45
        out.append(f'<path d="M{stem_x},{ly} Q{lx},{ly-14} {lx-side*6},{ly-28} Q{stem_x},{ly-18} {stem_x},{ly}" '
                   f'fill="{leaf_col}" opacity="0.88"/>')
    cy = stem_top_y
    # Outer petals (slightly darker)
    for i in range(n_petals):
        ang = math.radians(i * 360 / n_petals + 10)
        px = cx + math.cos(ang) * petal_r * 1.22
        py = cy + math.sin(ang) * petal_r * 1.22
        out.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{petal_r:.1f}" ry="{petal_r*0.48:.1f}" '
                   f'fill="{petal_col}" opacity="0.60" '
                   f'transform="rotate({i*360//n_petals+10},{px:.1f},{py:.1f})"/>')
    # Inner petals
    for i in range(n_petals):
        ang = math.radians(i * 360 / n_petals)
        px = cx + math.cos(ang) * petal_r
        py = cy + math.sin(ang) * petal_r
        out.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{petal_r:.1f}" ry="{petal_r*0.42:.1f}" '
                   f'fill="{petal_col}" opacity="0.90" '
                   f'transform="rotate({i*360//n_petals},{px:.1f},{py:.1f})"/>')
    # Center disk glow
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{center_r*1.6:.1f}" fill="{center_col}" opacity="0.28"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{center_r:.1f}" fill="{center_col}" opacity="0.96"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{center_r*0.5:.1f}" fill="#FFFFF0" opacity="0.85"/>')
    return ''.join(out)

def amaurotine_tower(tx, ty, w, h, side='left'):
    """Amaurotine research hall: smooth ivory tower with rounded dome top,
       gold trim bands, arched windows, crystal spire.
       side: 'left' (light from right) or 'right' (light from left)."""
    out = []
    grad = 'eMarble' if side == 'left' else 'eMarbleSh'
    shad = 'eMarbleSh' if side == 'left' else 'eMarble'
    # Main body
    out.append(f'<rect x="{tx}" y="{ty+h*0.12:.0f}" width="{w}" height="{h*0.88:.0f}" '
               f'fill="url(#{grad})" rx="3"/>')
    # Shadow strip on inner edge
    sw = w * 0.12
    sx = tx + w - sw if side == 'left' else tx
    out.append(f'<rect x="{sx:.0f}" y="{ty+h*0.12:.0f}" width="{sw:.0f}" height="{h*0.88:.0f}" '
               f'fill="url(#{shad})" rx="2" opacity="0.45"/>')
    # Dome top (rounded)
    dome_cx = tx + w / 2
    dome_cy = ty + h * 0.14
    dome_rx = w / 2 + 2
    dome_ry = h * 0.13
    out.append(f'<ellipse cx="{dome_cx:.0f}" cy="{dome_cy:.0f}" rx="{dome_rx:.0f}" ry="{dome_ry:.0f}" '
               f'fill="url(#{grad})"/>')
    # Gold trim bands (3 evenly spaced)
    for band_frac in [0.20, 0.45, 0.68]:
        by = ty + h * band_frac
        out.append(f'<rect x="{tx-1}" y="{by:.0f}" width="{w+2}" height="{max(3,h*0.028):.0f}" '
                   f'fill="url(#eGold)" opacity="0.88"/>')
    # Gold dome ring
    out.append(f'<ellipse cx="{dome_cx:.0f}" cy="{ty+h*0.12+3:.0f}" rx="{dome_rx:.0f}" ry="{max(3,h*0.025):.0f}" '
               f'fill="url(#eGold)" opacity="0.80"/>')
    # Arched windows (3 rows)
    ww = w * 0.30
    wh = h * 0.095
    for row in range(3):
        wy = ty + h * (0.26 + row * 0.22)
        wx = tx + w * 0.35
        # Window recess
        out.append(f'<rect x="{wx:.0f}" y="{wy:.0f}" width="{ww:.0f}" height="{wh:.0f}" '
                   f'fill="#A08860" rx="{ww*0.4:.0f}" opacity="0.55"/>')
        # Amber glow
        out.append(f'<rect x="{wx+1:.0f}" y="{wy+1:.0f}" width="{ww-2:.0f}" height="{wh-2:.0f}" '
                   f'fill="#FFE090" rx="{ww*0.38:.0f}" opacity="0.60"/>')
    # Crystal spire at top
    spire_h = h * 0.14
    out.append(f'<polygon points="{dome_cx:.0f},{ty:.0f} {dome_cx-5:.0f},{ty+spire_h:.0f} {dome_cx+5:.0f},{ty+spire_h:.0f}" '
               f'fill="#C0E8FF" opacity="0.90"/>')
    out.append(f'<polygon points="{dome_cx:.0f},{ty:.0f} {dome_cx-5:.0f},{ty+spire_h:.0f} {dome_cx+5:.0f},{ty+spire_h:.0f}" '
               f'fill="url(#eCrystal)" opacity="0.70"/>')
    # Gold spire base band
    out.append(f'<rect x="{dome_cx-5:.0f}" y="{ty+spire_h:.0f}" width="10" height="{max(2,h*0.018):.0f}" '
               f'fill="url(#eGold)" opacity="0.85"/>')
    # Inscription panel (below dome)
    px = tx + w * 0.15
    py = ty + h * 0.15
    ph = h * 0.065
    pw = w * 0.70
    out.append(f'<rect x="{px:.0f}" y="{py:.0f}" width="{pw:.0f}" height="{ph:.0f}" '
               f'fill="#E8E0C8" rx="2" opacity="0.60"/>')
    # Rune dashes
    for ri in range(6):
        rx2 = px + pw * 0.10 + ri * pw * 0.135
        out.append(f'<rect x="{rx2:.0f}" y="{py+ph*0.30:.0f}" width="{pw*0.07:.0f}" height="{ph*0.40:.0f}" '
                   f'fill="#806040" rx="1" opacity="0.55"/>')
    return ''.join(out)

def floating_island(ix, iy, iw, ih, trees=True, tree_col='#2A7020'):
    """Small floating island: bottom stone, top grass, optional trees."""
    out = []
    # Stone underside (rounded bottom)
    out.append(f'<ellipse cx="{ix:.0f}" cy="{iy+ih*0.55:.0f}" rx="{iw/2:.0f}" ry="{ih*0.50:.0f}" '
               f'fill="#9A9080" opacity="0.90"/>')
    out.append(f'<ellipse cx="{ix:.0f}" cy="{iy+ih*0.55:.0f}" rx="{iw/2*0.85:.0f}" ry="{ih*0.40:.0f}" '
               f'fill="#B8AFA0" opacity="0.75"/>')
    # Top grass cap
    out.append(f'<ellipse cx="{ix:.0f}" cy="{iy+ih*0.15:.0f}" rx="{iw/2+2:.0f}" ry="{ih*0.22:.0f}" '
               f'fill="#4A9840" opacity="0.92"/>')
    out.append(f'<ellipse cx="{ix:.0f}" cy="{iy+ih*0.12:.0f}" rx="{iw/2:.0f}" ry="{ih*0.15:.0f}" '
               f'fill="#5AB050" opacity="0.85"/>')
    if trees:
        # Small trees on island
        for tx_off, th in [(-iw*0.22, ih*0.55), (0, ih*0.70), (iw*0.20, ih*0.48)]:
            tx2 = ix + tx_off
            ty2 = iy + ih * 0.05
            out.append(f'<line x1="{tx2:.0f}" y1="{ty2:.0f}" x2="{tx2:.0f}" y2="{ty2-th:.0f}" '
                       f'stroke="#5A3A18" stroke-width="2.5"/>')
            out.append(f'<ellipse cx="{tx2:.0f}" cy="{ty2-th:.0f}" rx="{th*0.38:.0f}" ry="{th*0.32:.0f}" '
                       f'fill="{tree_col}" opacity="0.88"/>')
    return ''.join(out)

# ─────────────────────────────────────────────────────────────────────────────
#  GRADIENTS
# ─────────────────────────────────────────────────────────────────────────────
A('<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"><defs>')

# Sky: warm golden-hour (NOT dark purple — Elpis is eternal warm twilight paradise)
A('<linearGradient id="eSky" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#3850A8"/>'   # soft periwinkle-indigo
  '<stop offset="16%"  stop-color="#6C60B8"/>'   # warm violet (lighter)
  '<stop offset="32%"  stop-color="#A87898"/>'   # mauve-rose
  '<stop offset="50%"  stop-color="#D09070"/>'   # warm peach
  '<stop offset="68%"  stop-color="#E8B858"/>'   # amber-peach
  '<stop offset="84%"  stop-color="#F5CE50"/>'   # warm gold
  '<stop offset="100%" stop-color="#F8DC80"/>'   # bright horizon gold
  '</linearGradient>')

# Warm ethereal light bloom (upper center — no harsh sun, diffuse warm light)
A('<radialGradient id="eLight" cx="50%" cy="8%" r="70%">'
  '<stop offset="0%"   stop-color="#FFEEC0" stop-opacity="0.82"/>'
  '<stop offset="22%"  stop-color="#F8D098" stop-opacity="0.50"/>'
  '<stop offset="50%"  stop-color="#E8A870" stop-opacity="0.20"/>'
  '<stop offset="80%"  stop-color="#C07888" stop-opacity="0.05"/>'
  '<stop offset="100%" stop-color="#9050A0" stop-opacity="0"/>'
  '</radialGradient>')

# Aether shimmer (teal-gold near ground level — the aether of creation)
A('<radialGradient id="eAether" cx="50%" cy="90%" r="55%">'
  '<stop offset="0%"   stop-color="#60E8C0" stop-opacity="0.30"/>'
  '<stop offset="40%"  stop-color="#30B898" stop-opacity="0.12"/>'
  '<stop offset="75%"  stop-color="#108870" stop-opacity="0.04"/>'
  '<stop offset="100%" stop-color="#106050" stop-opacity="0"/>'
  '</radialGradient>')

# Amaurotine ivory marble (lit side)
A('<linearGradient id="eMarble" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#F8F6EE"/>'
  '<stop offset="30%"  stop-color="#EFEBE0"/>'
  '<stop offset="65%"  stop-color="#E2DDD0"/>'
  '<stop offset="100%" stop-color="#D0CCBF"/>'
  '</linearGradient>')

# Marble shadow side
A('<linearGradient id="eMarbleSh" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#C8C3B5"/>'
  '<stop offset="35%"  stop-color="#DDDAD0"/>'
  '<stop offset="100%" stop-color="#F2EEE5"/>'
  '</linearGradient>')

# Marble vertical shading
A('<linearGradient id="eMarbleV" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FAFAF2"/>'
  '<stop offset="50%"  stop-color="#EEEADF"/>'
  '<stop offset="100%" stop-color="#D8D3C5"/>'
  '</linearGradient>')

# Gold trim (Amaurotine brass-gold)
A('<linearGradient id="eGold" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FFF8C0"/>'
  '<stop offset="30%"  stop-color="#E8D048"/>'
  '<stop offset="65%"  stop-color="#BFA020"/>'
  '<stop offset="100%" stop-color="#907808"/>'
  '</linearGradient>')

# Crystal spire gradient
A('<linearGradient id="eCrystal" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#FFFFFF" stop-opacity="0.95"/>'
  '<stop offset="40%"  stop-color="#90D8FF" stop-opacity="0.80"/>'
  '<stop offset="100%" stop-color="#60B8F0" stop-opacity="0.50"/>'
  '</linearGradient>')

# Lush meadow ground
A('<linearGradient id="eGnd" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#4A9838"/>'
  '<stop offset="30%"  stop-color="#357025"/>'
  '<stop offset="65%"  stop-color="#205015"/>'
  '<stop offset="100%" stop-color="#143810"/>'
  '</linearGradient>')

# Distant rolling hills (warm atmospheric haze)
A('<linearGradient id="eHills" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#6A8860" stop-opacity="0.65"/>'
  '<stop offset="100%" stop-color="#3A6030" stop-opacity="0.88"/>'
  '</linearGradient>')

# Lily pond (reflective, warm sky colors)
A('<linearGradient id="ePond" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#9090D0" stop-opacity="0.80"/>'
  '<stop offset="40%"  stop-color="#7888C0" stop-opacity="0.88"/>'
  '<stop offset="100%" stop-color="#506090" stop-opacity="0.92"/>'
  '</linearGradient>')

# Flower petals - 6 colors for giant fantastical flowers
A('<radialGradient id="eFlCrim" cx="35%" cy="30%" r="65%">'
  '<stop offset="0%"   stop-color="#FF8898"/>'
  '<stop offset="45%"  stop-color="#E82040"/>'
  '<stop offset="100%" stop-color="#A81020"/>'
  '</radialGradient>')

A('<radialGradient id="eFlVio" cx="35%" cy="30%" r="65%">'
  '<stop offset="0%"   stop-color="#C080FF"/>'
  '<stop offset="45%"  stop-color="#8030D0"/>'
  '<stop offset="100%" stop-color="#5010A0"/>'
  '</radialGradient>')

A('<radialGradient id="eFlTeal" cx="35%" cy="30%" r="65%">'
  '<stop offset="0%"   stop-color="#60F0D0"/>'
  '<stop offset="45%"  stop-color="#10B890"/>'
  '<stop offset="100%" stop-color="#088060"/>'
  '</radialGradient>')

A('<radialGradient id="eFlGold" cx="35%" cy="30%" r="65%">'
  '<stop offset="0%"   stop-color="#FFE858"/>'
  '<stop offset="45%"  stop-color="#F0B810"/>'
  '<stop offset="100%" stop-color="#B88000"/>'
  '</radialGradient>')

A('<radialGradient id="eFlPink" cx="35%" cy="30%" r="65%">'
  '<stop offset="0%"   stop-color="#FFC0E8"/>'
  '<stop offset="45%"  stop-color="#F070B8"/>'
  '<stop offset="100%" stop-color="#C04088"/>'
  '</radialGradient>')

A('<radialGradient id="eFlOrng" cx="35%" cy="30%" r="65%">'
  '<stop offset="0%"   stop-color="#FFB850"/>'
  '<stop offset="45%"  stop-color="#F07010"/>'
  '<stop offset="100%" stop-color="#B84000"/>'
  '</radialGradient>')

# Creation orb (prototype creature aether sphere)
A('<radialGradient id="eOrb" cx="38%" cy="32%" r="62%">'
  '<stop offset="0%"   stop-color="#FFFFFF" stop-opacity="1.00"/>'
  '<stop offset="20%"  stop-color="#C0F8E8" stop-opacity="0.95"/>'
  '<stop offset="50%"  stop-color="#60D0C0" stop-opacity="0.88"/>'
  '<stop offset="80%"  stop-color="#20A0A8" stop-opacity="0.90"/>'
  '<stop offset="100%" stop-color="#1070C0" stop-opacity="0.95"/>'
  '</radialGradient>')

# Gate aether shimmer barrier (vertical)
A('<linearGradient id="eGateField" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#C0F0FF" stop-opacity="0.10"/>'
  '<stop offset="30%"  stop-color="#80E8D0" stop-opacity="0.28"/>'
  '<stop offset="55%"  stop-color="#60D8C0" stop-opacity="0.35"/>'
  '<stop offset="78%"  stop-color="#80E8D0" stop-opacity="0.22"/>'
  '<stop offset="100%" stop-color="#C0F0FF" stop-opacity="0.08"/>'
  '</linearGradient>')

# Vignette (top corners fade to periwinkle-violet)
A('<radialGradient id="eVig" cx="50%" cy="0%" r="100%">'
  '<stop offset="55%"  stop-color="#000000" stop-opacity="0"/>'
  '<stop offset="100%" stop-color="#20105A" stop-opacity="0.45"/>'
  '</radialGradient>')

# Atmospheric ground haze
A('<linearGradient id="eHaze" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#3A7030" stop-opacity="0"/>'
  '<stop offset="45%"  stop-color="#285020" stop-opacity="0.30"/>'
  '<stop offset="100%" stop-color="#183818" stop-opacity="0.70"/>'
  '</linearGradient>')

# Tall grass gradient (foreground)
A('<linearGradient id="eGrass" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#5AB040"/>'
  '<stop offset="55%"  stop-color="#3A8028"/>'
  '<stop offset="100%" stop-color="#205010"/>'
  '</linearGradient>')

# Stone path (mossy ancient stone)
A('<linearGradient id="ePath" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#A8A090"/>'
  '<stop offset="50%"  stop-color="#908880"/>'
  '<stop offset="100%" stop-color="#787068"/>'
  '</linearGradient>')

# Lily pad green
A('<radialGradient id="eLilyPad" cx="50%" cy="40%" r="55%">'
  '<stop offset="0%"   stop-color="#5AC840"/>'
  '<stop offset="60%"  stop-color="#30A020"/>'
  '<stop offset="100%" stop-color="#187010"/>'
  '</radialGradient>')

# Cloud (soft pink-white)
A('<radialGradient id="eCloud" cx="45%" cy="38%" r="58%">'
  '<stop offset="0%"   stop-color="#FFFFFF" stop-opacity="0.95"/>'
  '<stop offset="40%"  stop-color="#FFF0F5" stop-opacity="0.85"/>'
  '<stop offset="75%"  stop-color="#F8E0EE" stop-opacity="0.60"/>'
  '<stop offset="100%" stop-color="#F0C8E8" stop-opacity="0"/>'
  '</radialGradient>')

A('</defs>')

# ─────────────────────────────────────────────────────────────────────────────
#  1. SKY BACKGROUND
# ─────────────────────────────────────────────────────────────────────────────
A('<rect width="400" height="600" fill="url(#eSky)"/>')
# Warm diffuse light bloom
A('<rect width="400" height="600" fill="url(#eLight)"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  2. FANTASTICAL CLOUDS (soft pink-white, Elpis style)
# ─────────────────────────────────────────────────────────────────────────────
clouds = [
    # (cx, cy, rx, ry, opacity)
    (68,  60, 52, 22, 0.82),
    (40,  70, 30, 14, 0.70),
    (100, 62, 28, 12, 0.68),
    (280, 48, 60, 24, 0.80),
    (240, 58, 36, 16, 0.72),
    (318, 56, 32, 14, 0.70),
    (190, 72, 44, 18, 0.65),
    (170, 80, 24, 10, 0.55),
]
for cx, cy, rx, ry, op in clouds:
    A(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="url(#eCloud)" opacity="{op}"/>')
    # Soft glow beneath
    A(f'<ellipse cx="{cx}" cy="{cy+ry*0.6:.0f}" rx="{rx*0.80:.0f}" ry="{ry*0.50:.0f}" '
      f'fill="#F0D0E8" opacity="{op*0.25:.2f}"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  3. FLOATING ISLANDS (signature Elpis visual)
# ─────────────────────────────────────────────────────────────────────────────
# Large island — upper left
A(floating_island(100, 102, 78, 32, trees=True, tree_col='#2A8020'))
# Medium island — upper right
A(floating_island(318, 84, 58, 26, trees=True, tree_col='#1E7018'))
# Small island — far right, slightly lower
A(floating_island(360, 130, 36, 16, trees=False))
# Tiny island — left side
A(floating_island(52, 145, 28, 13, trees=False))
# Very distant (tiny, faint) — far left upper
A(f'<ellipse cx="22" cy="90" rx="14" ry="5" fill="#7A9868" opacity="0.40"/>')
A(f'<ellipse cx="22" cy="87" rx="12" ry="4" fill="#5A8850" opacity="0.35"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  4. DISTANT BACKGROUND HILLS (below sky, above ground)
# ─────────────────────────────────────────────────────────────────────────────
A('<path d="M0,285 Q30,255 70,268 Q110,240 155,262 Q200,232 245,255 Q290,238 330,258 Q365,244 400,262 L400,310 L0,310 Z" '
  'fill="url(#eHills)" opacity="0.75"/>')
A('<path d="M0,295 Q40,272 85,283 Q130,258 175,275 Q215,252 258,270 Q300,255 345,272 Q375,260 400,270 L400,316 L0,316 Z" '
  'fill="#4A7040" opacity="0.38"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  5. AMAUROTINE RESEARCH HALLS (left and right cliffs/platforms)
# ─────────────────────────────────────────────────────────────────────────────
# Left tower cluster
# Main left tower (tall, prominent)
A(amaurotine_tower(tx=-12, ty=160, w=88, h=240, side='left'))
# Left secondary tower (slightly behind)
A(amaurotine_tower(tx=-8, ty=205, w=62, h=190, side='left'))

# Right tower cluster
A(amaurotine_tower(tx=324, ty=160, w=88, h=240, side='right'))
A(amaurotine_tower(tx=346, ty=208, w=62, h=188, side='right'))

# ─────────────────────────────────────────────────────────────────────────────
#  6. LILY POND (mid-ground, left-center)
# ─────────────────────────────────────────────────────────────────────────────
pond_cx = 148; pond_cy = 368; pond_rx = 52; pond_ry = 18
A(f'<ellipse cx="{pond_cx}" cy="{pond_cy}" rx="{pond_rx}" ry="{pond_ry}" fill="url(#ePond)"/>')
# Reflection shimmer
A(f'<ellipse cx="{pond_cx}" cy="{pond_cy}" rx="{pond_rx}" ry="{pond_ry}" '
  f'fill="#B0C8FF" opacity="0.18"/>')
# Lily pads
pads = [(120,362,9,4,0), (138,372,11,4.5,-15), (155,360,10,4,20),
        (170,368,8,3.5,-8), (182,375,9,4,30), (142,358,7,3.0,10)]
for lpx, lpy, lprx, lpry, lpa in pads:
    A(f'<ellipse cx="{lpx}" cy="{lpy}" rx="{lprx}" ry="{lpry}" '
      f'fill="url(#eLilyPad)" opacity="0.88" transform="rotate({lpa},{lpx},{lpy})"/>')
    # Pad notch
    A(f'<line x1="{lpx}" y1="{lpy}" x2="{lpx}" y2="{lpy-lprx*0.9:.0f}" '
      f'stroke="#187010" stroke-width="0.8" opacity="0.60"/>')
# Lily flowers on pads
lily_flowers = [(123,355,'#FFFFFF','#FFE878'), (157,356,'#FFB8D8','#FFE060'),
                (181,371,'#FFFFFF','#FFD050')]
for lfx, lfy, lfc, lfc2 in lily_flowers:
    A(wildflower(lfx, lfy, lfc, size=3.5, fc2=lfc2))
# Water ripple lines
for rr in [0.55, 0.75, 0.90]:
    A(f'<ellipse cx="{pond_cx}" cy="{pond_cy}" rx="{pond_rx*rr:.0f}" ry="{pond_ry*rr:.0f}" '
      f'fill="none" stroke="#8898D8" stroke-width="0.8" opacity="0.28"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  7. LUSH GREEN MEADOW
# ─────────────────────────────────────────────────────────────────────────────
A('<rect y="348" width="400" height="252" fill="url(#eGnd)"/>')
A('<rect width="400" height="600" fill="url(#eAether)"/>')

# Gentle meadow slope bumps
A('<path d="M0,358 Q50,340 120,352 Q180,338 240,350 Q310,336 370,348 Q390,342 400,350 L400,370 L0,370 Z" '
  'fill="#4A9038" opacity="0.60"/>')
A('<path d="M0,355 Q70,345 140,355 Q190,342 250,354 Q320,340 400,354 L400,362 L0,362 Z" '
  'fill="#58A040" opacity="0.40"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  8. ANCIENT STONE PATH
# ─────────────────────────────────────────────────────────────────────────────
# Main path from gate upward
path_pts = "M165,600 L170,540 L175,480 L178,420 L180,380 L182,355"
A(f'<path d="{path_pts}" fill="none" stroke="url(#ePath)" stroke-width="22" stroke-linecap="round" opacity="0.78"/>')
A(f'<path d="{path_pts}" fill="none" stroke="#C8C0A8" stroke-width="18" stroke-linecap="round" opacity="0.55"/>')
# Stone slab joints
for sy in [370, 400, 430, 460, 490, 520, 555]:
    A(f'<line x1="162" y1="{sy}" x2="188" y2="{sy}" stroke="#988870" stroke-width="1.2" opacity="0.45"/>')
# Mossy edges
A('<path d="M163,600 L168,540 L173,480 L176,420 L178,380 L180,355" '
  'fill="none" stroke="#358025" stroke-width="3" stroke-dasharray="6,5" opacity="0.38"/>')
A('<path d="M187,600 L192,540 L197,480 L200,420 L202,380 L204,355" '
  'fill="none" stroke="#358025" stroke-width="3" stroke-dasharray="5,6" opacity="0.38"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  9. WILDFLOWER MEADOW (scattered small flowers)
# ─────────────────────────────────────────────────────────────────────────────
flower_data = [
    # (x, y, color, center_color, size)
    (220,358,'#FF4060','#FFE040',3.8), (250,366,'#8040E0','#FFD040',3.5),
    (278,362,'#20C898','#FFF060',3.6), (300,370,'#FF9030','#FFFFFF',3.4),
    (316,358,'#FF60A8','#FFE870',3.7), (340,365,'#FF3848','#FFE040',3.5),
    (358,360,'#6040E8','#FFF080',3.8), (372,368,'#20C898','#FFE050',3.3),
    (385,358,'#FF8830','#FFFFFF',3.6), (395,366,'#FF50A8','#FFE870',3.4),
    (42,362,'#FF4060','#FFE040',3.8), (68,368,'#20C898','#FFF060',3.6),
    (88,360,'#8040E0','#FFD040',3.5), (108,366,'#FF9030','#FFFFFF',3.7),
    (126,358,'#FF60A8','#FFE870',3.8), (205,372,'#FF4848','#FFE050',3.4),
    (228,380,'#6040E8','#FFF080',3.5), (252,374,'#FFB820','#FFFFFF',3.6),
    (270,382,'#FF50A8','#FFE870',3.4), (292,376,'#20C898','#FFF060',3.7),
    (308,384,'#FF3848','#FFE040',3.8), (328,376,'#8040E0','#FFD040',3.5),
    (345,382,'#FF8830','#FFFFFF',3.6), (362,376,'#FF60A8','#FFE870',3.8),
    (44,374,'#6040E8','#FFF080',3.5), (70,380,'#FF4060','#FFE040',3.8),
    (94,374,'#FF9030','#FFFFFF',3.6), (118,382,'#20C898','#FFF060',3.7),
    (138,376,'#8040E0','#FFD040',3.4), (392,378,'#FF4060','#FFE040',3.7),
    (218,395,'#FF4060','#FFE040',3.2), (245,400,'#20C898','#FFF060',3.4),
    (268,395,'#6040E8','#FFF080',3.3), (55,393,'#FF8830','#FFFFFF',3.2),
    (80,400,'#FF60A8','#FFE870',3.4), (105,394,'#FF4848','#FFE050',3.3),
    (380,392,'#8040E0','#FFD040',3.2), (350,398,'#20C898','#FFF060',3.4),
]
for fx, fy, fc, fc2, fs in flower_data:
    A(wildflower(fx, fy, fc, size=fs, fc2=fc2))

# Grass tufts across meadow
grass_tufts = [
    (22,390,16), (55,398,14), (82,388,15), (115,396,13), (142,390,14),
    (212,388,13), (235,396,15), (258,390,14), (282,388,16), (305,394,13),
    (328,390,15), (352,396,14), (375,388,16), (392,394,13),
    (38,418,12), (72,422,14), (98,416,13), (155,420,12), (225,418,14),
    (248,422,13), (275,416,15), (302,420,12), (335,418,14), (365,422,13),
    (388,416,15),
]
for gx, gy, gh in grass_tufts:
    for goff in [-4, -1.5, 1.5, 4]:
        ang = math.radians(goff * 12 - 90)
        ex = gx + math.cos(ang) * gh
        ey = gy + math.sin(ang) * gh
        A(f'<line x1="{gx}" y1="{gy}" x2="{ex:.1f}" y2="{ey:.1f}" '
          f'stroke="url(#eGrass)" stroke-width="1.5" stroke-linecap="round" opacity="0.80"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  10. GIANT FANTASTICAL FLOWERS (Elpis signature flora)
# ─────────────────────────────────────────────────────────────────────────────
giant_configs = [
    # Left side (x, base_y, petal_r, center_r, petal_col, center_col, n_petals, stem_h)
    (32,  452, 20, 8, 'url(#eFlCrim)', '#FFE878', 7, 70),
    (68,  468, 16, 7, 'url(#eFlVio)',  '#FFFFA0', 6, 58),
    (100, 448, 22, 9, 'url(#eFlTeal)', '#FFD860', 8, 78),
    (38,  490, 14, 6, 'url(#eFlPink)', '#FFE0A0', 6, 52),
    (78,  510, 17, 7, 'url(#eFlGold)', '#FFFFFF', 7, 62),
    (110, 500, 13, 5, 'url(#eFlOrng)', '#FFF0C0', 6, 48),
    # Right side
    (292, 452, 22, 9, 'url(#eFlVio)',  '#FFE878', 7, 72),
    (328, 468, 18, 7, 'url(#eFlCrim)', '#FFFFA0', 6, 62),
    (362, 448, 20, 8, 'url(#eFlGold)', '#FFD860', 8, 76),
    (300, 488, 15, 6, 'url(#eFlTeal)', '#FFE0A0', 6, 55),
    (338, 506, 17, 7, 'url(#eFlPink)', '#FFFFFF', 7, 60),
    (368, 498, 13, 5, 'url(#eFlOrng)', '#FFF0C0', 6, 46),
]
for cfg in giant_configs:
    A(giant_flower(*cfg))

# ─────────────────────────────────────────────────────────────────────────────
#  11. STAGE 5 OBJECT — Creation Altar
#      Three-tier marble platform with glowing prototype creature orb
# ─────────────────────────────────────────────────────────────────────────────
# (shifted +52px right per stage5 transform)
alt_cx = 200 - 52    # = 148 → renders at 200 after transform
alt_base = 235

# Tier 3 (bottom, largest)
A(f'<ellipse cx="{alt_cx}" cy="{alt_base}" rx="50" ry="10" fill="url(#eMarbleV)" opacity="0.95"/>')
A(f'<rect x="{alt_cx-50}" y="{alt_base-14}" width="100" height="14" fill="url(#eMarbleV)" rx="3" opacity="0.92"/>')
A(f'<ellipse cx="{alt_cx}" cy="{alt_base-14}" rx="50" ry="9" fill="url(#eMarbleV)" opacity="0.88"/>')
A(f'<rect x="{alt_cx-50}" y="{alt_base-15}" width="100" height="3" fill="url(#eGold)" opacity="0.78"/>')

# Tier 2 (middle)
A(f'<ellipse cx="{alt_cx}" cy="{alt_base-18}" rx="35" ry="7.5" fill="url(#eMarbleV)" opacity="0.95"/>')
A(f'<rect x="{alt_cx-35}" y="{alt_base-31}" width="70" height="13" fill="url(#eMarbleV)" rx="2" opacity="0.92"/>')
A(f'<ellipse cx="{alt_cx}" cy="{alt_base-31}" rx="35" ry="7" fill="url(#eMarbleV)" opacity="0.88"/>')
A(f'<rect x="{alt_cx-35}" y="{alt_base-32}" width="70" height="2.5" fill="url(#eGold)" opacity="0.78"/>')

# Tier 1 (top, smallest)
A(f'<ellipse cx="{alt_cx}" cy="{alt_base-36}" rx="22" ry="5.5" fill="url(#eMarbleV)" opacity="0.95"/>')
A(f'<rect x="{alt_cx-22}" y="{alt_base-47}" width="44" height="11" fill="url(#eMarbleV)" rx="2" opacity="0.92"/>')
A(f'<ellipse cx="{alt_cx}" cy="{alt_base-47}" rx="22" ry="5" fill="url(#eMarbleV)" opacity="0.88"/>')
A(f'<rect x="{alt_cx-22}" y="{alt_base-48}" width="44" height="2" fill="url(#eGold)" opacity="0.80"/>')

# Rune inscriptions on tiers
for tier_y, tier_rx in [(alt_base-8, 42), (alt_base-24, 28), (alt_base-42, 16)]:
    for ri in range(5):
        ang = math.radians(ri * 72 + 18)
        rx2 = alt_cx + math.cos(ang) * tier_rx * 0.72
        ry2 = tier_y + math.sin(ang) * 2.5
        A(f'<rect x="{rx2-2.5:.1f}" y="{ry2-1:.1f}" width="5" height="2" '
          f'fill="#D0B840" rx="0.8" opacity="0.65"/>')

# Central pillar
A(f'<rect x="{alt_cx-6}" y="{alt_base-82}" width="12" height="36" fill="url(#eMarbleV)" rx="3" opacity="0.90"/>')
A(f'<rect x="{alt_cx-6}" y="{alt_base-82}" width="12" height="2" fill="url(#eGold)" opacity="0.78"/>')
A(f'<rect x="{alt_cx-6}" y="{alt_base-48}" width="12" height="2" fill="url(#eGold)" opacity="0.78"/>')

# Prototype creature orb (the heart of creation)
orb_cy = alt_base - 100
A(f'<circle cx="{alt_cx}" cy="{orb_cy}" r="24" fill="#60E8D8" opacity="0.15"/>')
A(f'<circle cx="{alt_cx}" cy="{orb_cy}" r="20" fill="#40D0C0" opacity="0.20"/>')
A(f'<circle cx="{alt_cx}" cy="{orb_cy}" r="17" fill="url(#eOrb)" opacity="0.95"/>')
# Interior creature shape (abstract swirl suggesting a forming creature)
A(f'<path d="M{alt_cx-5},{orb_cy-5} Q{alt_cx+5},{orb_cy-8} {alt_cx+7},{orb_cy} '
  f'Q{alt_cx+5},{orb_cy+6} {alt_cx-3},{orb_cy+5} Q{alt_cx-8},{orb_cy+2} {alt_cx-5},{orb_cy-5}" '
  f'fill="#FFFFFF" opacity="0.45"/>')
# Glass edge ring
A(f'<circle cx="{alt_cx}" cy="{orb_cy}" r="17" fill="none" stroke="#FFFFFF" stroke-width="1.2" opacity="0.55"/>')
A(f'<circle cx="{alt_cx}" cy="{orb_cy}" r="17" fill="none" stroke="#60E8D8" stroke-width="0.6" opacity="0.45"/>')
# Inner glow highlight
A(f'<circle cx="{alt_cx-5}" cy="{orb_cy-5}" r="5" fill="#FFFFFF" opacity="0.60"/>')

# Orbiting aether sparks (6 colors)
sparks = [('#FF90C0',0), ('#60F0D0',60), ('#FFE060',120),
          ('#B060FF',180), ('#FF8840',240), ('#60B0FF',300)]
for sc, sang in sparks:
    rad = math.radians(sang)
    sx = alt_cx + math.cos(rad) * 24
    sy = orb_cy + math.sin(rad) * 10
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="2.8" fill="{sc}" opacity="0.90"/>')
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="5.5" fill="{sc}" opacity="0.20"/>')

# Aether beams rising from orb
for bang in [-55, -28, 0, 28, 55]:
    brad = math.radians(bang - 90)
    bx = alt_cx + math.cos(brad) * 80
    by = orb_cy + math.sin(brad) * 80
    op = 0.045 - abs(bang) * 0.0003
    A(f'<line x1="{alt_cx}" y1="{orb_cy}" x2="{bx:.0f}" y2="{by:.0f}" '
      f'stroke="#80F0E0" stroke-width="1.5" opacity="{max(0.01,op):.3f}"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  12. STAGE 10 OBJECT — Grand Amaurotine Arch Gate
#      Scale 1.5× at center (200, 531) per stage10 transform
# ─────────────────────────────────────────────────────────────────────────────
# This renders at 1.5× scale centered on (200, 531),
# so design at natural size around cx=200, base ~575
gate_cx = 200; gate_base = 575

# Gate platform / threshold
A(f'<rect x="{gate_cx-70}" y="{gate_base-8}" width="140" height="12" fill="url(#eMarbleV)" rx="3" opacity="0.90"/>')
A(f'<rect x="{gate_cx-70}" y="{gate_base-10}" width="140" height="3" fill="url(#eGold)" opacity="0.80"/>')
# Gold threshold rune band
for ri in range(9):
    A(f'<rect x="{gate_cx-60+ri*14}" y="{gate_base-8}" width="7" height="3" '
      f'fill="#FFD840" rx="1" opacity="0.60"/>')

# Left column
col_w = 22; col_h = 115
A(f'<rect x="{gate_cx-70}" y="{gate_base-8-col_h}" width="{col_w}" height="{col_h}" fill="url(#eMarble)" rx="3" opacity="0.95"/>')
# Left column shadow
A(f'<rect x="{gate_cx-70+col_w-5}" y="{gate_base-8-col_h}" width="5" height="{col_h}" fill="url(#eMarbleSh)" rx="2" opacity="0.50"/>')
# Left column gold bands
for band_frac in [0.18, 0.42, 0.68, 0.88]:
    by2 = gate_base - 8 - col_h + col_h * band_frac
    A(f'<rect x="{gate_cx-71}" y="{by2:.0f}" width="{col_w+2}" height="4" fill="url(#eGold)" opacity="0.78"/>')
# Left capital (top flare)
A(f'<rect x="{gate_cx-74}" y="{gate_base-8-col_h-6}" width="{col_w+8}" height="8" fill="url(#eMarbleV)" rx="2" opacity="0.92"/>')
A(f'<rect x="{gate_cx-74}" y="{gate_base-8-col_h-8}" width="{col_w+8}" height="3" fill="url(#eGold)" opacity="0.80"/>')
# Left base plinth
A(f'<rect x="{gate_cx-74}" y="{gate_base-12}" width="{col_w+8}" height="6" fill="url(#eMarbleV)" rx="2" opacity="0.90"/>')
A(f'<rect x="{gate_cx-74}" y="{gate_base-14}" width="{col_w+8}" height="3" fill="url(#eGold)" opacity="0.75"/>')

# Right column (mirror)
A(f'<rect x="{gate_cx+48}" y="{gate_base-8-col_h}" width="{col_w}" height="{col_h}" fill="url(#eMarbleSh)" rx="3" opacity="0.92"/>')
A(f'<rect x="{gate_cx+48}" y="{gate_base-8-col_h}" width="5" height="{col_h}" fill="url(#eMarble)" opacity="0.50"/>')
for band_frac in [0.18, 0.42, 0.68, 0.88]:
    by2 = gate_base - 8 - col_h + col_h * band_frac
    A(f'<rect x="{gate_cx+47}" y="{by2:.0f}" width="{col_w+2}" height="4" fill="url(#eGold)" opacity="0.78"/>')
A(f'<rect x="{gate_cx+46}" y="{gate_base-8-col_h-6}" width="{col_w+8}" height="8" fill="url(#eMarbleV)" rx="2" opacity="0.92"/>')
A(f'<rect x="{gate_cx+46}" y="{gate_base-8-col_h-8}" width="{col_w+8}" height="3" fill="url(#eGold)" opacity="0.80"/>')
A(f'<rect x="{gate_cx+46}" y="{gate_base-12}" width="{col_w+8}" height="6" fill="url(#eMarbleV)" rx="2" opacity="0.90"/>')
A(f'<rect x="{gate_cx+46}" y="{gate_base-14}" width="{col_w+8}" height="3" fill="url(#eGold)" opacity="0.75"/>')

# Arch (smooth Amaurotine segmental arch — broad, not pointed)
arch_y_base = gate_base - 8 - col_h + 10   # top of columns + slight overlap
arch_top_y = arch_y_base - 42              # arch peak height
arch_left_x = gate_cx - 48
arch_right_x = gate_cx + 48
arch_mid_y = arch_y_base - 2

A(f'<path d="M{arch_left_x},{arch_mid_y} '
  f'C{arch_left_x},{arch_top_y} {arch_right_x},{arch_top_y} {arch_right_x},{arch_mid_y}" '
  f'fill="none" stroke="url(#eMarbleV)" stroke-width="16" stroke-linecap="butt" opacity="0.95"/>')
# Gold arch rim
A(f'<path d="M{arch_left_x-4},{arch_mid_y} '
  f'C{arch_left_x-4},{arch_top_y-5} {arch_right_x+4},{arch_top_y-5} {arch_right_x+4},{arch_mid_y}" '
  f'fill="none" stroke="url(#eGold)" stroke-width="3.5" stroke-linecap="butt" opacity="0.75"/>')
A(f'<path d="M{arch_left_x+10},{arch_mid_y} '
  f'C{arch_left_x+10},{arch_top_y+6} {arch_right_x-10},{arch_top_y+6} {arch_right_x-10},{arch_mid_y}" '
  f'fill="none" stroke="url(#eGold)" stroke-width="2" stroke-linecap="butt" opacity="0.55"/>')

# Voussoir joints on arch (7 joints)
for ji in range(7):
    t = (ji + 1) / 8.0
    # Bezier point on arch
    bx = (1-t)**2 * arch_left_x + 2*(1-t)*t * gate_cx + t**2 * arch_right_x
    by = (1-t)**2 * arch_mid_y + 2*(1-t)*t * arch_top_y + t**2 * arch_mid_y
    # Tangent direction
    tdx = 2*(1-t)*(gate_cx - arch_left_x) + 2*t*(arch_right_x - gate_cx)
    tdy = 2*(1-t)*(arch_top_y - arch_mid_y) + 2*t*(arch_mid_y - arch_top_y)
    tlen = math.hypot(tdx, tdy) or 1
    nx = -tdy / tlen * 10; ny = tdx / tlen * 10
    A(f'<line x1="{bx-nx*0.5:.1f}" y1="{by-ny*0.5:.1f}" x2="{bx+nx:.1f}" y2="{by+ny:.1f}" '
      f'stroke="#B09878" stroke-width="1.0" opacity="0.42"/>')

# Sunflower keystone
key_cx = gate_cx; key_cy = arch_top_y - 1
A(f'<circle cx="{key_cx}" cy="{key_cy}" r="9" fill="url(#eGold)" opacity="0.88"/>')
A(f'<circle cx="{key_cx}" cy="{key_cy}" r="5.5" fill="#FFE860" opacity="0.95"/>')
for ri in range(8):
    rang = math.radians(ri * 45)
    rsx = key_cx + math.cos(rang) * 9; rsy = key_cy + math.sin(rang) * 9
    rex = key_cx + math.cos(rang) * 13; rey = key_cy + math.sin(rang) * 13
    A(f'<line x1="{rsx:.1f}" y1="{rsy:.1f}" x2="{rex:.1f}" y2="{rey:.1f}" '
      f'stroke="#E8C820" stroke-width="2.2" stroke-linecap="round" opacity="0.78"/>')

# Aether shimmer barrier inside arch
barrier_top = arch_top_y + 4
barrier_bot = arch_mid_y + 2
barrier_w = (arch_right_x - arch_left_x) - 14
A(f'<rect x="{gate_cx - barrier_w//2}" y="{barrier_top:.0f}" width="{barrier_w}" '
  f'height="{barrier_bot - barrier_top:.0f}" fill="url(#eGateField)" rx="4" opacity="0.88"/>')
# Vertical shimmer columns
for vi in range(5):
    vx = gate_cx - barrier_w//2 + 4 + vi * (barrier_w - 8) // 4
    A(f'<line x1="{vx:.0f}" y1="{barrier_top:.0f}" x2="{vx:.0f}" y2="{barrier_bot:.0f}" '
      f'stroke="#80F0E0" stroke-width="1.0" opacity="0.25"/>')
# Horizontal scan line
scan_y = barrier_top + (barrier_bot - barrier_top) * 0.50
A(f'<line x1="{gate_cx - barrier_w//2:.0f}" y1="{scan_y:.0f}" '
  f'x2="{gate_cx + barrier_w//2:.0f}" y2="{scan_y:.0f}" '
  f'stroke="#C0FFF0" stroke-width="1.5" opacity="0.30"/>')

# Climbing flowers on arch (6 per side, colorful)
arch_flowers_left = [
    (arch_left_x - 2, arch_mid_y - 20, '#FF6090', '#FFE040', 4.0),
    (arch_left_x + 3, arch_mid_y - 45, '#60F0C0', '#FFE860', 3.6),
    (arch_left_x + 12, arch_mid_y - 70, '#FF90D0', '#FFFFFF', 3.8),
    (arch_left_x + 24, arch_mid_y - 88, '#E050FF', '#FFE840', 3.5),
    (arch_left_x + 38, arch_mid_y - 102, '#FF8040', '#FFFFA0', 3.7),
    (gate_cx - 18, arch_top_y - 2, '#40E0FF', '#FFE860', 3.4),
]
arch_flowers_right = [
    (arch_right_x + 2, arch_mid_y - 20, '#FFB840', '#FFFFFF', 4.0),
    (arch_right_x - 3, arch_mid_y - 45, '#A040FF', '#FFE860', 3.6),
    (arch_right_x - 12, arch_mid_y - 70, '#FF4060', '#FFF0A0', 3.8),
    (arch_right_x - 24, arch_mid_y - 88, '#40F0C0', '#FFE040', 3.5),
    (arch_right_x - 38, arch_mid_y - 102, '#FF90A8', '#FFFFA0', 3.7),
    (gate_cx + 18, arch_top_y - 2, '#FFD040', '#FFFFFF', 3.4),
]
for fx2, fy2, fc2, fcc2, fs2 in arch_flowers_left + arch_flowers_right:
    A(wildflower(fx2, fy2, fc2, size=fs2, fc2=fcc2))

# ─────────────────────────────────────────────────────────────────────────────
#  13. FOREGROUND GIANT FLOWERS (partially cropped at bottom)
# ─────────────────────────────────────────────────────────────────────────────
fg_giants = [
    (22,  580, 24, 10, 'url(#eFlCrim)', '#FFE878', 7, 55),
    (378, 580, 24, 10, 'url(#eFlVio)',  '#FFFFA0', 7, 55),
    (60,  590, 20, 8,  'url(#eFlTeal)', '#FFD860', 6, 48),
    (340, 590, 20, 8,  'url(#eFlGold)', '#FFFFFF', 6, 48),
]
for cfg in fg_giants:
    A(giant_flower(*cfg))

# ─────────────────────────────────────────────────────────────────────────────
#  14. ATMOSPHERE OVERLAYS
# ─────────────────────────────────────────────────────────────────────────────
# Bottom ground haze (depth)
A('<rect y="500" width="400" height="100" fill="url(#eHaze)" opacity="0.65"/>')

# Soft aether motes / wisps floating in air
motes = [
    (52,  200, 2.5, 1.5, '#FFC0E8', 0.70), (88,  185, 2.0, 1.3, '#80F0D0', 0.65),
    (140, 172, 2.2, 1.4, '#FFE870', 0.68), (175, 192, 1.8, 1.1, '#C080FF', 0.60),
    (225, 180, 2.0, 1.3, '#80F0D0', 0.65), (258, 168, 1.8, 1.2, '#FFC0E8', 0.62),
    (308, 188, 2.2, 1.4, '#FFE870', 0.68), (345, 175, 2.0, 1.3, '#C080FF', 0.65),
    (42,  290, 1.8, 1.2, '#FFC0E8', 0.58), (118, 278, 2.0, 1.3, '#80F0D0', 0.60),
    (202, 268, 2.5, 1.6, '#C080FF', 0.65), (285, 280, 2.0, 1.3, '#FFE870', 0.58),
    (358, 272, 1.8, 1.2, '#FFC0E8', 0.55),
]
for mx, my, mrx, mry, mc, mop in motes:
    A(f'<ellipse cx="{mx}" cy="{my}" rx="{mrx}" ry="{mry}" fill="{mc}" opacity="{mop}"/>')
    A(f'<ellipse cx="{mx}" cy="{my}" rx="{mrx*3:.1f}" ry="{mry*3:.1f}" fill="{mc}" opacity="{mop*0.12:.2f}"/>')

# Soft ethereal light shafts from upper center
for ang in [-42, -22, -8, 0, 8, 22, 42]:
    rad = math.radians(ang - 90)
    lx = 200 + 380 * math.cos(rad)
    ly = 15 + 380 * math.sin(rad)
    op = max(0.005, 0.055 - abs(ang) * 0.001)
    sw = max(0.5, 2.5 - abs(ang) * 0.04)
    A(f'<line x1="200" y1="15" x2="{lx:.0f}" y2="{ly:.0f}" '
      f'stroke="#FFE0A0" stroke-width="{sw:.1f}" opacity="{op:.3f}"/>')

# Top corner vignette
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

# Check for forbidden chars
if svg.count('`'): raise RuntimeError('Backtick in SVG!')
if svg.count("'"): raise RuntimeError('Single quote in SVG!')

# XML validation
import xml.etree.ElementTree as ET
try:
    ET.fromstring(svg)
    print('  XML parse: OK')
except ET.ParseError as e:
    raise RuntimeError(f'XML parse error: {e}')

# ── CSS fallback update ──────────────────────────────────────────────────────
html2 = html
# game-view background
for old, new in [
    ('#game-view[data-diff="ULTIMATE"] { background: rgb(96,24,104); }',
     '#game-view[data-diff="ULTIMATE"] { background: rgb(56,80,168); }'),
]:
    if old in html2:
        html2 = html2.replace(old, new)
        print(f'  Replaced CSS: {old[:60]}')

# ── Injection ────────────────────────────────────────────────────────────────
# ULTIMATE uses backtick template literal
pattern = r"(if\(diff===.ULTIMATE.\) return \`)(.*?)(\`;)"
repl = lambda m: m.group(1) + svg + m.group(3)
new_html, n = _re.subn(pattern, repl, html2, flags=_re.DOTALL)
if n == 0:
    raise RuntimeError("ULTIMATE pattern not found in stage.html")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print(f'stage.html written. ({n} replacement)')
