#!/usr/bin/env python3
"""gen_ultimate.py — ULTIMATE background: The Crystarium (FF14 Shadowbringers)
Visual accuracy targets:
  - Sky: deep purple-indigo NIGHT sky, dense stars (The First = eternal night/Source-less sun)
  - Crystal Tower: massive glowing white-blue crystal spire rising center-background
  - Architecture: warm grey stone buildings with crystal/blue-light accents, warm lanterns
  - Floating crystal shards drifting in sky
  - Multi-tier city platform structure
  - Blue-white aether glow from Crystal Tower illuminating everything
  - Stage 5: The Exedra — grand fountain plaza with glowing crystal centerpiece
  - Stage 10: Main gate arch with Crystal Tower visible through it
"""
import re as _re, math

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    html = f.read()

parts = []
def A(s): parts.append(s)

# ─────────────────────────────────────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def star(sx, sy, r=1.2, op=0.90):
    return (f'<circle cx="{sx}" cy="{sy}" r="{r}" fill="#FFFFFF" opacity="{op}"/>'
            f'<circle cx="{sx}" cy="{sy}" r="{r*2.2:.1f}" fill="#C0D8FF" opacity="{op*0.12:.2f}"/>')

def crystal_shard(cx, cy, w, h, angle=0, col='#A8D8FF', op=0.75):
    """Floating crystal shard — diamond/hexagonal shape."""
    pts = (f'{cx},{cy-h/2} {cx+w/2},{cy-h*0.1} '
           f'{cx+w*0.3},{cy+h/2} {cx-w*0.3},{cy+h/2} '
           f'{cx-w/2},{cy-h*0.1}')
    return (f'<polygon points="{pts}" fill="{col}" opacity="{op}" '
            f'transform="rotate({angle},{cx},{cy})"/>'
            f'<polygon points="{pts}" fill="#FFFFFF" opacity="{op*0.25:.2f}" '
            f'transform="rotate({angle},{cx},{cy}) scale(0.5)" '
            f'transform-origin="{cx} {cy}"/>')

def lantern(lx, ly, w=7, h=10):
    """Warm lantern on a post."""
    out = []
    # Post
    out.append(f'<line x1="{lx}" y1="{ly}" x2="{lx}" y2="{ly-28}" '
               f'stroke="#706050" stroke-width="2.5"/>')
    # Lantern body
    out.append(f'<rect x="{lx-w//2}" y="{ly-28-h}" width="{w}" height="{h}" '
               f'fill="#403020" rx="1" opacity="0.90"/>')
    # Warm glow inside
    out.append(f'<rect x="{lx-w//2+1}" y="{ly-28-h+1}" width="{w-2}" height="{h-2}" '
               f'fill="#FFD060" rx="1" opacity="0.85"/>')
    # Glow halo
    out.append(f'<ellipse cx="{lx}" cy="{ly-28-h//2}" rx="{w*1.8:.0f}" ry="{h*1.5:.0f}" '
               f'fill="#FFB820" opacity="0.18"/>')
    out.append(f'<ellipse cx="{lx}" cy="{ly-28-h//2}" rx="{w*3.5:.0f}" ry="{h*2.8:.0f}" '
               f'fill="#FF9010" opacity="0.07"/>')
    # Cap top
    out.append(f'<rect x="{lx-w//2-1}" y="{ly-28-h-2}" width="{w+2}" height="3" '
               f'fill="#504030" rx="1" opacity="0.90"/>')
    return ''.join(out)

# ─────────────────────────────────────────────────────────────────────────────
#  GRADIENTS
# ─────────────────────────────────────────────────────────────────────────────
A('<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"><defs>')

# Night sky: deep indigo-purple (The First, eternal night)
A('<linearGradient id="cSky" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#0A0520"/>'   # near-black indigo zenith
  '<stop offset="20%"  stop-color="#120830"/>'   # deep violet
  '<stop offset="42%"  stop-color="#1A1045"/>'   # dark purple-blue
  '<stop offset="65%"  stop-color="#201458"/>'   # indigo
  '<stop offset="82%"  stop-color="#251A6A"/>'   # lighter indigo near horizon
  '<stop offset="100%" stop-color="#2C2278"/>'   # horizon glow
  '</linearGradient>')

# Crystal Tower central glow (blue-white radial from tower base)
A('<radialGradient id="cTowerGlow" cx="50%" cy="35%" r="60%">'
  '<stop offset="0%"   stop-color="#C8EEFF" stop-opacity="0.85"/>'
  '<stop offset="12%"  stop-color="#90D0FF" stop-opacity="0.60"/>'
  '<stop offset="30%"  stop-color="#5098E0" stop-opacity="0.30"/>'
  '<stop offset="55%"  stop-color="#3060A8" stop-opacity="0.10"/>'
  '<stop offset="80%"  stop-color="#182880" stop-opacity="0.03"/>'
  '<stop offset="100%" stop-color="#101840" stop-opacity="0"/>'
  '</radialGradient>')

# Horizon aether glow (blue-teal at base of tower/city)
A('<radialGradient id="cHorizonGlow" cx="50%" cy="78%" r="58%">'
  '<stop offset="0%"   stop-color="#80C8FF" stop-opacity="0.45"/>'
  '<stop offset="30%"  stop-color="#4090D8" stop-opacity="0.20"/>'
  '<stop offset="60%"  stop-color="#204898" stop-opacity="0.07"/>'
  '<stop offset="100%" stop-color="#101840" stop-opacity="0"/>'
  '</radialGradient>')

# Crystal Tower body (white-blue, luminous)
A('<linearGradient id="cTower" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#98C8F8"/>'
  '<stop offset="22%"  stop-color="#C8E8FF"/>'
  '<stop offset="48%"  stop-color="#F0F8FF"/>'
  '<stop offset="72%"  stop-color="#C8E8FF"/>'
  '<stop offset="100%" stop-color="#88B8E8"/>'
  '</linearGradient>')

A('<linearGradient id="cTowerV" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FFFFFF"/>'
  '<stop offset="25%"  stop-color="#E0F0FF"/>'
  '<stop offset="55%"  stop-color="#B0D8FF"/>'
  '<stop offset="85%"  stop-color="#80B8F0"/>'
  '<stop offset="100%" stop-color="#60A0E0"/>'
  '</linearGradient>')

# Stone buildings (warm grey, lit by crystal tower glow)
A('<linearGradient id="cStone" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#C8B890"/>'   # warm sandstone (Crystarium primary material)
  '<stop offset="35%"  stop-color="#B0A07A"/>'
  '<stop offset="70%"  stop-color="#908060"/>'
  '<stop offset="100%" stop-color="#706048"/>'
  '</linearGradient>')

# Stone lit by crystal tower blue glow (slightly cooler/blue-tinted face)
A('<linearGradient id="cStoneLit" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#A8B8C8"/>'   # crystal-blue lit face
  '<stop offset="30%"  stop-color="#B8AA88"/>'   # transitions to sandstone
  '<stop offset="100%" stop-color="#A09070"/>'
  '</linearGradient>')

# Ground / city platform (dark stone, crystal-glow lit)
A('<linearGradient id="cGnd" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#303848"/>'
  '<stop offset="35%"  stop-color="#252E3C"/>'
  '<stop offset="70%"  stop-color="#1A2230"/>'
  '<stop offset="100%" stop-color="#101820"/>'
  '</linearGradient>')

# Crystal accent (glowing blue crystal elements in architecture)
A('<linearGradient id="cCrystal" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FFFFFF"/>'
  '<stop offset="25%"  stop-color="#C0E8FF"/>'
  '<stop offset="55%"  stop-color="#80C0F0"/>'
  '<stop offset="100%" stop-color="#4090D0"/>'
  '</linearGradient>')

# Shard crystals (floating)
A('<linearGradient id="cShard" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#FFFFFF" stop-opacity="0.95"/>'
  '<stop offset="30%"  stop-color="#B8DCFF" stop-opacity="0.85"/>'
  '<stop offset="70%"  stop-color="#78B0F0" stop-opacity="0.75"/>'
  '<stop offset="100%" stop-color="#4888D8" stop-opacity="0.65"/>'
  '</linearGradient>')

# Fountain water (crystal blue)
A('<radialGradient id="cFountain" cx="50%" cy="30%" r="60%">'
  '<stop offset="0%"   stop-color="#A0E0FF" stop-opacity="0.92"/>'
  '<stop offset="40%"  stop-color="#60B8F0" stop-opacity="0.80"/>'
  '<stop offset="100%" stop-color="#3080C0" stop-opacity="0.70"/>'
  '</radialGradient>')

# Gate / dark iron framework (black iron is prominent in Crystarium — Rotunda material)
A('<linearGradient id="cGate" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#3A3A48"/>'   # matte black iron
  '<stop offset="50%"  stop-color="#2A2A38"/>'
  '<stop offset="100%" stop-color="#1E1E2C"/>'
  '</linearGradient>')

# Iron with sandstone base (mixed material — most Crystarium structural elements)
A('<linearGradient id="cIronSand" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#B0A080"/>'   # sandstone top
  '<stop offset="40%"  stop-color="#888070"/>'   # mid blend
  '<stop offset="100%" stop-color="#303040"/>'   # iron base
  '</linearGradient>')

# Purple forest horizon (Lakeland surroundings — deep purple vegetation)
A('<linearGradient id="cForest" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#3A1860" stop-opacity="0.60"/>'
  '<stop offset="55%"  stop-color="#2A1050" stop-opacity="0.80"/>'
  '<stop offset="100%" stop-color="#1A0838" stop-opacity="0.90"/>'
  '</linearGradient>')

# Vignette
A('<radialGradient id="cVig" cx="50%" cy="20%" r="90%">'
  '<stop offset="52%"  stop-color="#000000" stop-opacity="0"/>'
  '<stop offset="100%" stop-color="#060210" stop-opacity="0.70"/>'
  '</radialGradient>')

# Ground depth haze
A('<linearGradient id="cHaze" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#101828" stop-opacity="0"/>'
  '<stop offset="50%"  stop-color="#0C1420" stop-opacity="0.35"/>'
  '<stop offset="100%" stop-color="#080E18" stop-opacity="0.75"/>'
  '</linearGradient>')

A('</defs>')

# ─────────────────────────────────────────────────────────────────────────────
#  1. NIGHT SKY (deep indigo-purple — The First, eternal night)
# ─────────────────────────────────────────────────────────────────────────────
A('<rect width="400" height="600" fill="url(#cSky)"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  2. STARS (dense field — The First has no sun, stars always visible)
# ─────────────────────────────────────────────────────────────────────────────
import random
rng = random.Random(42)
for _ in range(280):
    sx = rng.uniform(0, 400)
    sy = rng.uniform(0, 260)
    sr = rng.uniform(0.5, 1.8)
    sop = rng.uniform(0.45, 0.95)
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr:.1f}" fill="#FFFFFF" opacity="{sop:.2f}"/>')
    if rng.random() < 0.18:
        A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr*2.8:.1f}" fill="#B8D0FF" opacity="{sop*0.12:.2f}"/>')

# A few brighter star clusters
bright_stars = [(38,28,2.2,0.98),(195,18,2.5,0.99),(310,35,1.9,0.96),
                (85,52,2.0,0.95),(260,48,2.1,0.97),(145,30,1.8,0.92),
                (360,22,2.3,0.98),(60,80,1.7,0.90),(330,75,2.0,0.94)]
for bsx,bsy,bsr,bsop in bright_stars:
    A(star(bsx,bsy,bsr,bsop))
    # 4-point sparkle
    for sang in [0,90,180,270]:
        brad = math.radians(sang)
        A(f'<line x1="{bsx}" y1="{bsy}" '
          f'x2="{bsx+math.cos(brad)*bsr*3.5:.1f}" y2="{bsy+math.sin(brad)*bsr*3.5:.1f}" '
          f'stroke="#FFFFFF" stroke-width="0.5" opacity="{bsop*0.55:.2f}"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  3. CRYSTAL TOWER — massive central spire (the heart of the Crystarium)
#     White-blue luminous, many facets, rises from behind the city
# ─────────────────────────────────────────────────────────────────────────────
# Tower base glow (spreads across whole sky)
A('<rect width="400" height="600" fill="url(#cTowerGlow)"/>')
A('<rect width="400" height="600" fill="url(#cHorizonGlow)"/>')

# Main tower shaft (wide at base, tapers to sharp tip)
tower_cx = 200
# Far left spire panel
A(f'<polygon points="190,8 196,50 198,220 190,260 182,220 184,50" '
  f'fill="url(#cTower)" opacity="0.45"/>')
# Far right spire panel
A(f'<polygon points="210,8 214,50 218,220 210,260 202,220 204,50" '
  f'fill="url(#cTower)" opacity="0.45"/>')
# Main central tower shaft
A(f'<polygon points="{tower_cx},0 {tower_cx+22},40 {tower_cx+28},100 '
  f'{tower_cx+30},200 {tower_cx+26},260 {tower_cx},275 '
  f'{tower_cx-26},260 {tower_cx-30},200 {tower_cx-28},100 {tower_cx-22},40" '
  f'fill="url(#cTowerV)" opacity="0.88"/>')
# Tower tip
A(f'<polygon points="{tower_cx},0 {tower_cx+15},35 {tower_cx-15},35" '
  f'fill="#FFFFFF" opacity="0.95"/>')
# Tower facet highlights (vertical light bands)
for fx_off, fw, fop in [(-8,4,0.70),(0,5,0.88),(10,3,0.60),(-18,2,0.40),(20,2,0.38)]:
    A(f'<rect x="{tower_cx+fx_off-fw//2}" y="0" width="{fw}" height="275" '
      f'fill="#FFFFFF" opacity="{fop}" rx="2"/>')
# Horizontal crystal ring bands on tower
for ring_y, ring_h, ring_op in [(40,5,0.80),(90,4,0.72),(145,4,0.68),(200,4,0.60),(250,3,0.52)]:
    A(f'<rect x="{tower_cx-32}" y="{ring_y}" width="64" height="{ring_h}" '
      f'fill="url(#cCrystal)" opacity="{ring_op}" rx="2"/>')
    # Ring glow
    A(f'<ellipse cx="{tower_cx}" cy="{ring_y+ring_h//2}" rx="50" ry="{ring_h*2:.0f}" '
      f'fill="#80C8FF" opacity="{ring_op*0.18:.2f}"/>')
# Tower base crystal burst (where tower meets city level)
A(f'<ellipse cx="{tower_cx}" cy="275" rx="60" ry="18" fill="#C0E8FF" opacity="0.55"/>')
A(f'<ellipse cx="{tower_cx}" cy="275" rx="40" ry="12" fill="#E0F4FF" opacity="0.70"/>')
A(f'<ellipse cx="{tower_cx}" cy="275" rx="22" ry="7" fill="#FFFFFF" opacity="0.85"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  4. FLOATING CRYSTAL SHARDS (drift in the sky around the tower)
# ─────────────────────────────────────────────────────────────────────────────
shards = [
    # (cx, cy, w, h, angle, col, op)
    (55,  105, 12, 30, -20, '#B0D8FF', 0.72),
    (78,  138, 8,  20, 15,  '#D0EEFF', 0.65),
    (42,  78,  6,  16, -35, '#C8E8FF', 0.60),
    (340, 112, 14, 32, 22,  '#A8D0FF', 0.70),
    (362, 85,  8,  22, -15, '#D0EEFF', 0.65),
    (318, 140, 7,  18, 30,  '#C8E8FF', 0.58),
    (142, 62,  10, 24, -10, '#B8E0FF', 0.62),
    (255, 70,  12, 28, 18,  '#C0E0FF', 0.64),
    (118, 92,  6,  14, 40,  '#D8EEFF', 0.55),
    (285, 95,  7,  17, -25, '#C8E8FF', 0.58),
    (165, 48,  9,  20, -8,  '#B0DCFF', 0.60),
    (232, 52,  8,  18, 12,  '#C0E0FF', 0.58),
]
for scx, scy, sw, sh, sang, scol, sop in shards:
    # Shard body
    half_w = sw/2; half_h = sh/2
    pts = (f'{scx},{scy-half_h} {scx+half_w},{scy-half_h*0.2} '
           f'{scx+half_w*0.6},{scy+half_h} {scx-half_w*0.6},{scy+half_h} '
           f'{scx-half_w},{scy-half_h*0.2}')
    A(f'<polygon points="{pts}" fill="{scol}" opacity="{sop}" '
      f'transform="rotate({sang},{scx},{scy})"/>')
    # Highlight streak
    A(f'<line x1="{scx-sw*0.15:.1f}" y1="{scy-half_h*0.8:.1f}" '
      f'x2="{scx+sw*0.08:.1f}" y2="{scy+half_h*0.5:.1f}" '
      f'stroke="#FFFFFF" stroke-width="1.5" opacity="{sop*0.65:.2f}" '
      f'transform="rotate({sang},{scx},{scy})"/>')
    # Glow
    A(f'<ellipse cx="{scx}" cy="{scy}" rx="{sw:.0f}" ry="{sh*0.55:.0f}" '
      f'fill="#A0CCFF" opacity="{sop*0.15:.2f}"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  5. LAKELAND PURPLE FORESTS (surrounding landscape — deep violet vegetation)
#     Lakeland approaches have vibrant purple forest even under the tower glow
# ─────────────────────────────────────────────────────────────────────────────
# Left purple forest hills
A('<path d="M0,268 Q18,240 40,255 Q58,228 78,248 Q95,222 115,240 Q130,230 148,250 L148,278 L0,278 Z" '
  'fill="#3A1860" opacity="0.72"/>')
A('<path d="M0,274 Q22,252 48,262 Q68,240 90,256 Q108,244 128,260 L128,280 L0,280 Z" '
  'fill="#2A1050" opacity="0.55"/>')
# Tree bumps (purple canopy)
for tx2, ty2, tr in [(18,254,10),(40,244,12),(62,238,11),(85,240,13),(108,232,11),(130,242,10)]:
    A(f'<ellipse cx="{tx2}" cy="{ty2}" rx="{tr}" ry="{tr*0.75:.0f}" fill="#4A2080" opacity="0.82"/>')
    A(f'<ellipse cx="{tx2}" cy="{ty2}" rx="{tr*0.65:.0f}" ry="{tr*0.55:.0f}" fill="#5A2898" opacity="0.65"/>')

# Right purple forest hills
A('<path d="M252,278 L252,250 Q270,230 292,248 Q310,222 330,240 Q348,228 368,250 Q385,240 400,255 L400,278 Z" '
  'fill="#3A1860" opacity="0.72"/>')
A('<path d="M272,280 L272,260 Q290,244 312,258 Q330,244 352,262 Q370,252 400,268 L400,280 Z" '
  'fill="#2A1050" opacity="0.55"/>')
for tx2, ty2, tr in [(270,250,10),(292,240,12),(315,232,11),(338,240,13),(360,238,11),(382,248,10)]:
    A(f'<ellipse cx="{tx2}" cy="{ty2}" rx="{tr}" ry="{tr*0.75:.0f}" fill="#4A2080" opacity="0.82"/>')
    A(f'<ellipse cx="{tx2}" cy="{ty2}" rx="{tr*0.65:.0f}" ry="{tr*0.55:.0f}" fill="#5A2898" opacity="0.65"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  6. CITY PLATFORM / DISTANT BUILDINGS (background, lit by tower glow)
# ─────────────────────────────────────────────────────────────────────────────
# Background city skyline (sandstone buildings — warm beige/tan primary color)
A('<path d="M0,258 L0,275 L30,275 L30,258 L40,258 L40,270 L55,270 L55,252 '
  'L68,252 L68,265 L80,265 L80,258 L95,258 L95,268 L108,268 L108,255 '
  'L120,255 L120,270 L128,270 L128,258 '
  'M272,258 L272,270 L280,270 L280,258 L292,258 L292,266 L305,266 '
  'L305,254 L318,254 L318,268 L330,268 L330,258 L345,258 '
  'L345,270 L360,270 L360,258 L375,258 L375,265 L390,265 L390,258 L400,258 L400,275 L0,275" '
  'fill="url(#cStone)" opacity="0.82"/>')
# Black iron trim on rooflines
A('<path d="M0,258 L128,258 M272,258 L400,258" '
  'fill="none" stroke="#202030" stroke-width="2.5" opacity="0.80"/>')
# Crystal glow windows (small)
for bwx, bwy in [(38,262),(62,257),(90,262),(104,259),(292,262),(318,258),(340,262),(362,262)]:
    A(f'<rect x="{bwx}" y="{bwy}" width="5" height="4" fill="#80C8FF" rx="1" opacity="0.72"/>')
    A(f'<ellipse cx="{bwx+2}" cy="{bwy+2}" rx="5" ry="4" fill="#60A8F0" opacity="0.18"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  6. LEFT AND RIGHT MAIN BUILDINGS (Crystarium architecture)
#     Stone walls, crystal-trimmed arched windows, warm lanterns
# ─────────────────────────────────────────────────────────────────────────────
def crystarium_building(bx, by, bw, bh, side='left', n_windows=3):
    out = []
    grad = 'cStoneLit' if side == 'left' else 'cStone'
    # Main body
    out.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="url(#{grad})" rx="2" opacity="0.95"/>')
    # Crystal-blue trim at roofline
    out.append(f'<rect x="{bx-2}" y="{by-4}" width="{bw+4}" height="6" fill="url(#cCrystal)" rx="1" opacity="0.70"/>')
    # Crenellation / parapet
    for ci in range(int(bw//10)):
        cx2 = bx + ci*10 + 2
        out.append(f'<rect x="{cx2}" y="{by-10}" width="6" height="8" fill="url(#cGate)" rx="1" opacity="0.85"/>')
    # Arched windows with blue crystal glow
    ww = bw*0.28; wh = bh*0.14
    for row in range(n_windows):
        wy = by + bh*(0.18 + row*0.28)
        wx = bx + bw*0.36
        # Dark recess
        out.append(f'<rect x="{wx:.0f}" y="{wy:.0f}" width="{ww:.0f}" height="{wh:.0f}" '
                   f'fill="#101828" rx="{ww*0.45:.0f}" opacity="0.88"/>')
        # Crystal light inside window
        out.append(f'<rect x="{wx+2:.0f}" y="{wy+2:.0f}" width="{ww-4:.0f}" height="{wh-2:.0f}" '
                   f'fill="#60B8F0" rx="{ww*0.40:.0f}" opacity="0.55"/>')
        # Window glow halo
        out.append(f'<ellipse cx="{wx+ww/2:.0f}" cy="{wy+wh/2:.0f}" '
                   f'rx="{ww*0.7:.0f}" ry="{wh*0.8:.0f}" fill="#4090D8" opacity="0.18"/>')
    # Stone pilaster strips (vertical decoration)
    for pi in range(3):
        px2 = bx + bw*0.22*pi
        out.append(f'<rect x="{px2:.0f}" y="{by}" width="{bw*0.06:.0f}" height="{bh}" '
                   f'fill="#585870" rx="1" opacity="0.50"/>')
    return ''.join(out)

# Left wing (3 towers/sections)
A(crystarium_building(bx=-10, by=168, bw=92, bh=232, side='left',  n_windows=3))
A(crystarium_building(bx=-6,  by=215, bw=66, bh=175, side='left',  n_windows=2))
# Right wing
A(crystarium_building(bx=318, by=168, bw=92, bh=232, side='right', n_windows=3))
A(crystarium_building(bx=340, by=218, bw=66, bh=175, side='right', n_windows=2))

# ─────────────────────────────────────────────────────────────────────────────
#  6b. THE ROTUNDA — iconic domed entrance hall
#      "Elegant black iron and sheets of shimmering crystal" (Sightseeing Log)
#      This is the first structure visitors encounter — domed, grand, central
# ─────────────────────────────────────────────────────────────────────────────
rot_cx = 200; rot_base = 362

# Rotunda base platform (sandstone steps)
A(f'<rect x="{rot_cx-70}" y="{rot_base-12}" width="140" height="14" fill="url(#cStone)" rx="2" opacity="0.90"/>')
A(f'<rect x="{rot_cx-60}" y="{rot_base-20}" width="120" height="10" fill="url(#cStone)" rx="2" opacity="0.88"/>')
A(f'<rect x="{rot_cx-50}" y="{rot_base-26}" width="100" height="8" fill="url(#cStone)" rx="1" opacity="0.85"/>')
# Black iron base rings
for step_y in [rot_base-12, rot_base-20, rot_base-26]:
    A(f'<rect x="{rot_cx-72}" y="{step_y}" width="144" height="2" fill="#181820" opacity="0.70"/>')

# Rotunda drum (cylindrical body — sandstone with black iron pilaster strips)
drum_h = 52; drum_r = 48
A(f'<rect x="{rot_cx-drum_r}" y="{rot_base-26-drum_h}" width="{drum_r*2}" height="{drum_h}" '
  f'fill="url(#cStone)" rx="3" opacity="0.92"/>')
# Crystal windows in drum (8 around circumference — shown as 5 facing front)
for wi in range(5):
    wx2 = rot_cx - 34 + wi * 17
    wy2 = rot_base - 26 - drum_h + drum_h*0.28
    A(f'<rect x="{wx2:.0f}" y="{wy2:.0f}" width="8" height="{drum_h*0.45:.0f}" '
      f'fill="#1A2840" rx="3" opacity="0.88"/>')
    A(f'<rect x="{wx2+1:.0f}" y="{wy2+1:.0f}" width="6" height="{drum_h*0.43:.0f}" '
      f'fill="#70C0FF" rx="3" opacity="0.60"/>')
    A(f'<ellipse cx="{wx2+4:.0f}" cy="{wy2+drum_h*0.2:.0f}" rx="5" ry="{drum_h*0.18:.0f}" '
      f'fill="#A0D8FF" opacity="0.20"/>')
# Black iron pilaster strips
for pi in range(6):
    px2 = rot_cx - drum_r + pi * (drum_r*2/5)
    A(f'<rect x="{px2:.0f}" y="{rot_base-26-drum_h}" width="4" height="{drum_h}" '
      f'fill="#1C1C28" rx="1" opacity="0.72"/>')
# Iron entablature band (top of drum)
A(f'<rect x="{rot_cx-drum_r-2}" y="{rot_base-26-drum_h-6}" width="{drum_r*2+4}" height="8" '
  f'fill="#1E1E2C" rx="1" opacity="0.85"/>')
A(f'<rect x="{rot_cx-drum_r-2}" y="{rot_base-26-drum_h-8}" width="{drum_r*2+4}" height="3" '
  f'fill="url(#cCrystal)" opacity="0.55"/>')

# Dome (black iron ribs + crystal panels — the signature Rotunda look)
dome_cx = rot_cx; dome_cy = rot_base - 26 - drum_h - 6
dome_rx = drum_r + 4; dome_ry = 36
# Dome base ellipse (iron)
A(f'<ellipse cx="{dome_cx}" cy="{dome_cy}" rx="{dome_rx}" ry="{dome_ry}" fill="#1A1A28" opacity="0.88"/>')
# Crystal panel fill (shimmering — the crystal sheets)
A(f'<ellipse cx="{dome_cx}" cy="{dome_cy}" rx="{dome_rx}" ry="{dome_ry}" fill="#1E3850" opacity="0.60"/>')
A(f'<ellipse cx="{dome_cx}" cy="{dome_cy}" rx="{dome_rx}" ry="{dome_ry}" fill="url(#cTowerGlow)" opacity="0.45"/>')
# Dome highlight (blue-white shimmer of crystal sheets catching tower glow)
A(f'<ellipse cx="{dome_cx-12}" cy="{dome_cy-12}" rx="{dome_rx*0.40:.0f}" ry="{dome_ry*0.30:.0f}" '
  f'fill="#80C8FF" opacity="0.28"/>')
# Iron ribs (8 structural ribs radiating from top)
for ri in range(8):
    ang = math.radians(ri*22.5 - 90)
    rx2 = dome_cx + math.cos(ang)*dome_rx; ry2 = dome_cy + math.sin(ang)*dome_ry
    A(f'<line x1="{dome_cx}" y1="{dome_cy-dome_ry}" x2="{rx2:.0f}" y2="{ry2:.0f}" '
      f'stroke="#181820" stroke-width="2.5" opacity="0.80"/>')
# Dome lantern (crystal finial at apex)
A(f'<circle cx="{dome_cx}" cy="{dome_cy-dome_ry-2}" r="7" fill="#1C2835" opacity="0.90"/>')
A(f'<polygon points="{dome_cx},{dome_cy-dome_ry-18} {dome_cx+5},{dome_cy-dome_ry-4} {dome_cx-5},{dome_cy-dome_ry-4}" '
  f'fill="url(#cCrystal)" opacity="0.90"/>')
A(f'<circle cx="{dome_cx}" cy="{dome_cy-dome_ry-10}" r="4" fill="#80D8FF" opacity="0.70"/>')
A(f'<ellipse cx="{dome_cx}" cy="{dome_cy-dome_ry-10}" rx="12" ry="12" fill="#50A8F0" opacity="0.14"/>')
# Glow from Rotunda (crystal tower light reflecting off dome)
A(f'<ellipse cx="{dome_cx}" cy="{dome_cy}" rx="{dome_rx+20}" ry="{dome_ry+15}" '
  f'fill="#4080C0" opacity="0.06"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  7. GROUND PLATFORM (dark stone, central plaza)
# ─────────────────────────────────────────────────────────────────────────────
A('<rect y="362" width="400" height="238" fill="url(#cGnd)"/>')
# Platform edge highlight (crystal-lit ledge)
A('<rect y="360" width="400" height="5" fill="url(#cCrystal)" opacity="0.55"/>')
A('<ellipse cx="200" cy="362" rx="200" ry="8" fill="#60A8E0" opacity="0.22"/>')

# Stone tile pattern on ground
for ty in range(370, 600, 22):
    A(f'<line x1="0" y1="{ty}" x2="400" y2="{ty}" stroke="#283040" stroke-width="1.0" opacity="0.40"/>')
for tx in range(0, 401, 28):
    A(f'<line x1="{tx}" y1="362" x2="{tx}" y2="600" stroke="#283040" stroke-width="1.0" opacity="0.35"/>')

# Crystal vein lines in ground (aether channels)
vein_paths = [
    "M200,362 L180,420 L165,480 L168,600",
    "M200,362 L220,420 L235,480 L232,600",
    "M200,362 L145,390 L100,430 L60,480",
    "M200,362 L255,390 L300,430 L340,480",
]
for vp in vein_paths:
    A(f'<path d="{vp}" fill="none" stroke="#4088C8" stroke-width="1.5" opacity="0.30"/>')
    A(f'<path d="{vp}" fill="none" stroke="#80C8FF" stroke-width="0.6" opacity="0.45"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  8. LANTERNS (warm amber light — Crystarium street lanterns)
# ─────────────────────────────────────────────────────────────────────────────
lantern_positions = [
    (55, 430), (95, 418), (135, 430), (265, 430), (305, 418), (345, 430),
    (38, 500), (75, 510), (112, 500), (288, 500), (325, 510), (362, 500),
]
for lx, ly in lantern_positions:
    A(lantern(lx, ly))

# ─────────────────────────────────────────────────────────────────────────────
#  9. CRYSTAL PILLARS (flanking the central path — iconic Crystarium feature)
# ─────────────────────────────────────────────────────────────────────────────
def crystal_pillar(px, py, h=80, w=12):
    out = []
    # Stone base
    out.append(f'<rect x="{px-w//2-3}" y="{py-8}" width="{w+6}" height="10" fill="url(#cGate)" rx="2" opacity="0.90"/>')
    # Shaft
    out.append(f'<rect x="{px-w//2}" y="{py-8-h}" width="{w}" height="{h}" fill="url(#cGate)" rx="2" opacity="0.90"/>')
    # Crystal top
    A_pts = f'{px},{py-8-h-14} {px+w//2+2},{py-8-h} {px-w//2-2},{py-8-h}'
    out.append(f'<polygon points="{A_pts}" fill="url(#cCrystal)" opacity="0.85"/>')
    # Crystal glow
    out.append(f'<ellipse cx="{px}" cy="{py-8-h-6}" rx="{w*1.2:.0f}" ry="{12}" fill="#60B0F0" opacity="0.22"/>')
    out.append(f'<ellipse cx="{px}" cy="{py-8-h-6}" rx="{w*2.5:.0f}" ry="{22}" fill="#4080D0" opacity="0.08"/>')
    # Highlight
    out.append(f'<line x1="{px-2}" y1="{py-8-h-12}" x2="{px-2}" y2="{py-10}" '
               f'stroke="#FFFFFF" stroke-width="1.5" opacity="0.28"/>')
    return ''.join(out)

A(crystal_pillar(100, 418, h=72, w=13))
A(crystal_pillar(130, 406, h=62, w=11))
A(crystal_pillar(300, 410, h=70, w=13))
A(crystal_pillar(270, 418, h=62, w=11))
A(crystal_pillar(152, 388, h=52, w=10))
A(crystal_pillar(248, 388, h=52, w=10))

# ─────────────────────────────────────────────────────────────────────────────
#  10. STAGE 5 — The Exedra Fountain Plaza
#      Central glowing crystal fountain, the landmark gathering place
#      (shifted +52px in stage5 transform → design around x=148)
# ─────────────────────────────────────────────────────────────────────────────
fnt_cx = 148  # renders at 200 after +52 transform
fnt_base = 240

# Fountain basin (wide circular pool)
A(f'<ellipse cx="{fnt_cx}" cy="{fnt_base}" rx="50" ry="13" fill="#101828" opacity="0.90"/>')
A(f'<ellipse cx="{fnt_cx}" cy="{fnt_base}" rx="50" ry="13" fill="url(#cFountain)" opacity="0.60"/>')
# Water surface shimmer
A(f'<ellipse cx="{fnt_cx}" cy="{fnt_base}" rx="50" ry="13" fill="none" '
  f'stroke="#80D0FF" stroke-width="1.5" opacity="0.55"/>')
for rr in [0.62, 0.80]:
    A(f'<ellipse cx="{fnt_cx}" cy="{fnt_base}" rx="{50*rr:.0f}" ry="{13*rr:.0f}" '
      f'fill="none" stroke="#60B8F0" stroke-width="0.8" opacity="0.35"/>')

# Basin wall
A(f'<rect x="{fnt_cx-52}" y="{fnt_base-10}" width="104" height="10" fill="url(#cGate)" rx="2" opacity="0.88"/>')
A(f'<ellipse cx="{fnt_cx}" cy="{fnt_base-10}" rx="52" ry="8" fill="url(#cGate)" opacity="0.88"/>')
# Basin crystal trim
A(f'<ellipse cx="{fnt_cx}" cy="{fnt_base-10}" rx="52" ry="8" fill="none" '
  f'stroke="url(#cCrystal)" stroke-width="2" opacity="0.60"/>')

# Fountain pillar / central column
A(f'<rect x="{fnt_cx-5}" y="{fnt_base-68}" width="10" height="58" fill="url(#cGate)" rx="2" opacity="0.90"/>')
A(f'<rect x="{fnt_cx-5}" y="{fnt_base-68}" width="10" height="2.5" fill="url(#cCrystal)" opacity="0.70"/>')
A(f'<rect x="{fnt_cx-5}" y="{fnt_base-12}" width="10" height="2.5" fill="url(#cCrystal)" opacity="0.70"/>')

# Upper basin (smaller, elevated)
A(f'<ellipse cx="{fnt_cx}" cy="{fnt_base-70}" rx="24" ry="6.5" fill="#101828" opacity="0.90"/>')
A(f'<ellipse cx="{fnt_cx}" cy="{fnt_base-70}" rx="24" ry="6.5" fill="url(#cFountain)" opacity="0.55"/>')
A(f'<rect x="{fnt_cx-26}" y="{fnt_base-76}" width="52" height="6" fill="url(#cGate)" rx="2" opacity="0.88"/>')
A(f'<ellipse cx="{fnt_cx}" cy="{fnt_base-76}" rx="26" ry="6" fill="url(#cGate)" opacity="0.88"/>')

# Crystal centerpiece (glowing crystal spire on top of fountain)
A(f'<polygon points="{fnt_cx},{fnt_base-108} {fnt_cx+10},{fnt_base-76} {fnt_cx-10},{fnt_base-76}" '
  f'fill="url(#cCrystal)" opacity="0.90"/>')
A(f'<polygon points="{fnt_cx},{fnt_base-100} {fnt_cx+14},{fnt_base-78} {fnt_cx-14},{fnt_base-78}" '
  f'fill="url(#cTower)" opacity="0.55"/>')
# Crystal glow
A(f'<ellipse cx="{fnt_cx}" cy="{fnt_base-90}" rx="22" ry="22" fill="#60B8FF" opacity="0.18"/>')
A(f'<ellipse cx="{fnt_cx}" cy="{fnt_base-90}" rx="12" ry="14" fill="#A0D8FF" opacity="0.35"/>')
# Glow core
A(f'<circle cx="{fnt_cx}" cy="{fnt_base-95}" r="5" fill="#FFFFFF" opacity="0.90"/>')

# Water jets arcing from upper basin
for ang in [-65, -30, 0, 30, 65]:
    rad = math.radians(ang - 90)
    jlx = fnt_cx + math.cos(rad)*32; jly = fnt_base-76 + math.sin(rad)*32
    A(f'<path d="M{fnt_cx},{fnt_base-76} Q{fnt_cx+math.cos(rad)*18:.0f},{fnt_base-76+math.sin(rad)*10:.0f} {jlx:.0f},{jly:.0f}" '
      f'fill="none" stroke="#80D0FF" stroke-width="1.8" opacity="0.55" stroke-linecap="round"/>')

# Fountain mist / water droplets
for md in range(8):
    mang = math.radians(md*45)
    mx = fnt_cx + math.cos(mang)*38; my = fnt_base + math.sin(mang)*10
    A(f'<circle cx="{mx:.0f}" cy="{my:.0f}" r="1.5" fill="#A0DCFF" opacity="0.45"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  11. STAGE 10 — Main Crystarium Gate
#      Massive stone arch with Crystal Tower visible through it
#      Scale 1.5× at (200,531)
# ─────────────────────────────────────────────────────────────────────────────
gate_cx = 200; gate_base = 578

# Gate platform
A(f'<rect x="{gate_cx-78}" y="{gate_base-6}" width="156" height="12" fill="url(#cGate)" rx="2" opacity="0.92"/>')
A(f'<rect x="{gate_cx-78}" y="{gate_base-8}" width="156" height="3" fill="url(#cCrystal)" opacity="0.55"/>')
# Gate platform crystal inlays
for gi in range(8):
    A(f'<rect x="{gate_cx-68+gi*18}" y="{gate_base-6}" width="10" height="3" '
      f'fill="#4888D8" rx="1" opacity="0.50"/>')

# Left tower of gate
col_w = 26; col_h = 120
A(f'<rect x="{gate_cx-80}" y="{gate_base-6-col_h}" width="{col_w}" height="{col_h}" '
  f'fill="url(#cStoneLit)" rx="2" opacity="0.95"/>')
# Crystal trim bands on left tower
for band_frac in [0.16, 0.38, 0.60, 0.82]:
    by2 = gate_base - 6 - col_h + col_h*band_frac
    A(f'<rect x="{gate_cx-81}" y="{by2:.0f}" width="{col_w+2}" height="4" '
      f'fill="url(#cCrystal)" opacity="0.55"/>')
# Crystal window in left tower
A(f'<rect x="{gate_cx-72}" y="{gate_base-6-col_h+col_h*0.28:.0f}" width="10" height="16" '
  f'fill="#60B8F0" rx="4" opacity="0.72"/>')
A(f'<ellipse cx="{gate_cx-67}" cy="{gate_base-6-col_h+col_h*0.28+6:.0f}" rx="7" ry="10" '
  f'fill="#90D8FF" opacity="0.30"/>')
# Capital (crenellated top)
A(f'<rect x="{gate_cx-83}" y="{gate_base-6-col_h-8}" width="{col_w+6}" height="10" '
  f'fill="url(#cGate)" rx="1" opacity="0.92"/>')
A(f'<rect x="{gate_cx-83}" y="{gate_base-6-col_h-12}" width="{col_w+6}" height="5" '
  f'fill="url(#cCrystal)" opacity="0.62"/>')
# Crystal spire atop left tower
A(f'<polygon points="{gate_cx-67},{gate_base-6-col_h-28} {gate_cx-60},{gate_base-6-col_h-8} {gate_cx-74},{gate_base-6-col_h-8}" '
  f'fill="url(#cCrystal)" opacity="0.85"/>')
A(f'<ellipse cx="{gate_cx-67}" cy="{gate_base-6-col_h-18}" rx="8" ry="8" fill="#50A0E8" opacity="0.15"/>')

# Right tower (mirror)
A(f'<rect x="{gate_cx+54}" y="{gate_base-6-col_h}" width="{col_w}" height="{col_h}" '
  f'fill="url(#cStone)" rx="2" opacity="0.95"/>')
for band_frac in [0.16, 0.38, 0.60, 0.82]:
    by2 = gate_base - 6 - col_h + col_h*band_frac
    A(f'<rect x="{gate_cx+53}" y="{by2:.0f}" width="{col_w+2}" height="4" '
      f'fill="url(#cCrystal)" opacity="0.55"/>')
A(f'<rect x="{gate_cx+62}" y="{gate_base-6-col_h+col_h*0.28:.0f}" width="10" height="16" '
  f'fill="#60B8F0" rx="4" opacity="0.72"/>')
A(f'<ellipse cx="{gate_cx+67}" cy="{gate_base-6-col_h+col_h*0.28+6:.0f}" rx="7" ry="10" '
  f'fill="#90D8FF" opacity="0.30"/>')
A(f'<rect x="{gate_cx+77}" y="{gate_base-6-col_h-8}" width="{col_w+6}" height="10" '
  f'fill="url(#cGate)" rx="1" opacity="0.92"/>')
A(f'<rect x="{gate_cx+77}" y="{gate_base-6-col_h-12}" width="{col_w+6}" height="5" '
  f'fill="url(#cCrystal)" opacity="0.62"/>')
A(f'<polygon points="{gate_cx+67},{gate_base-6-col_h-28} {gate_cx+74},{gate_base-6-col_h-8} {gate_cx+60},{gate_base-6-col_h-8}" '
  f'fill="url(#cCrystal)" opacity="0.85"/>')
A(f'<ellipse cx="{gate_cx+67}" cy="{gate_base-6-col_h-18}" rx="8" ry="8" fill="#50A0E8" opacity="0.15"/>')

# Arch (broad Crystarium arch, stone with crystal trim)
arch_base_y = gate_base - 6 - col_h + 18
arch_peak_y = arch_base_y - 48
arch_lx = gate_cx - 54; arch_rx = gate_cx + 54

# Crystal Tower glimpse through arch opening (visible behind gate)
A(f'<path d="M{arch_lx+8},{arch_base_y} C{arch_lx+8},{arch_peak_y+8} '
  f'{arch_rx-8},{arch_peak_y+8} {arch_rx-8},{arch_base_y} Z" '
  f'fill="#0C1830" opacity="0.80"/>')
# Mini Crystal Tower silhouette visible through arch
mini_tower_y = arch_base_y - 5
A(f'<polygon points="{gate_cx},{arch_peak_y+8} {gate_cx+18},{mini_tower_y} {gate_cx-18},{mini_tower_y}" '
  f'fill="url(#cTowerV)" opacity="0.55"/>')
A(f'<polygon points="{gate_cx},{arch_peak_y+8} {gate_cx+8},{arch_peak_y+22} {gate_cx-8},{arch_peak_y+22}" '
  f'fill="#E0F4FF" opacity="0.70"/>')
A(f'<ellipse cx="{gate_cx}" cy="{arch_peak_y+14}" rx="16" ry="4" fill="#80C8FF" opacity="0.35"/>')

# Arch stone
A(f'<path d="M{arch_lx},{arch_base_y} C{arch_lx},{arch_peak_y} {arch_rx},{arch_peak_y} {arch_rx},{arch_base_y}" '
  f'fill="none" stroke="url(#cGate)" stroke-width="20" stroke-linecap="butt" opacity="0.95"/>')
# Crystal trim on arch (outer)
A(f'<path d="M{arch_lx-4},{arch_base_y} C{arch_lx-4},{arch_peak_y-6} {arch_rx+4},{arch_peak_y-6} {arch_rx+4},{arch_base_y}" '
  f'fill="none" stroke="url(#cCrystal)" stroke-width="3.5" stroke-linecap="butt" opacity="0.65"/>')
# Crystal trim on arch (inner)
A(f'<path d="M{arch_lx+8},{arch_base_y} C{arch_lx+8},{arch_peak_y+8} {arch_rx-8},{arch_peak_y+8} {arch_rx-8},{arch_base_y}" '
  f'fill="none" stroke="#4888D8" stroke-width="1.5" stroke-linecap="butt" opacity="0.45"/>')

# Voussoir joints
for ji in range(7):
    t = (ji+1)/8.0
    bx2 = (1-t)**2*arch_lx + 2*(1-t)*t*gate_cx + t**2*arch_rx
    by2 = (1-t)**2*arch_base_y + 2*(1-t)*t*arch_peak_y + t**2*arch_base_y
    tdx = 2*(1-t)*(gate_cx-arch_lx) + 2*t*(arch_rx-gate_cx)
    tdy = 2*(1-t)*(arch_peak_y-arch_base_y) + 2*t*(arch_base_y-arch_peak_y)
    tlen = math.hypot(tdx,tdy) or 1
    nx = -tdy/tlen*12; ny = tdx/tlen*12
    A(f'<line x1="{bx2-nx*0.3:.1f}" y1="{by2-ny*0.3:.1f}" x2="{bx2+nx:.1f}" y2="{by2+ny:.1f}" '
      f'stroke="#5070A0" stroke-width="1.2" opacity="0.45"/>')

# Keystone crystal
key_cy = arch_peak_y - 2
A(f'<ellipse cx="{gate_cx}" cy="{key_cy}" rx="13" ry="10" fill="url(#cGate)" opacity="0.90"/>')
A(f'<polygon points="{gate_cx},{key_cy-14} {gate_cx+8},{key_cy} {gate_cx-8},{key_cy}" '
  f'fill="url(#cCrystal)" opacity="0.88"/>')
A(f'<ellipse cx="{gate_cx}" cy="{key_cy-6}" rx="5" ry="5" fill="#80D0FF" opacity="0.50"/>')
# Crystal glow on keystone
A(f'<ellipse cx="{gate_cx}" cy="{key_cy-4}" rx="18" ry="14" fill="#4088D0" opacity="0.12"/>')

# Crystal accent elements flanking gate base
for gfx, gfside in [(gate_cx-92, -1), (gate_cx+92, 1)]:
    A(f'<polygon points="{gfx},{gate_base-30} {gfx+gfside*6},{gate_base-6} {gfx-gfside*6},{gate_base-6}" '
      f'fill="url(#cCrystal)" opacity="0.72"/>')
    A(f'<ellipse cx="{gfx}" cy="{gate_base-22}" rx="7" ry="12" fill="#60A8F0" opacity="0.18"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  12. ATMOSPHERE OVERLAYS
# ─────────────────────────────────────────────────────────────────────────────
# Ground depth haze
A('<rect y="508" width="400" height="92" fill="url(#cHaze)" opacity="0.68"/>')

# Crystal Tower light shafts (very faint rays from tower base)
for ang in [-55, -32, -15, 0, 15, 32, 55]:
    rad = math.radians(ang - 90)
    lx = 200 + 450*math.cos(rad); ly = 275 + 450*math.sin(rad)
    op = max(0.006, 0.048 - abs(ang)*0.0004)
    sw = max(0.4, 2.0 - abs(ang)*0.025)
    A(f'<line x1="200" y1="275" x2="{lx:.0f}" y2="{ly:.0f}" '
      f'stroke="#80C8FF" stroke-width="{sw:.1f}" opacity="{op:.3f}"/>')

# Floating crystal particle motes
motes = [(52,165,1.8,1.1,'#90C8FF',0.68),(90,148,1.5,1.0,'#C0E0FF',0.60),
         (140,138,1.8,1.1,'#80B8F0',0.62),(175,158,1.4,0.9,'#A0D0FF',0.55),
         (228,145,1.6,1.0,'#C0E0FF',0.60),(268,138,1.8,1.1,'#80C0FF',0.62),
         (315,152,1.5,1.0,'#90C8FF',0.58),(350,142,1.8,1.1,'#A0D0FF',0.62),
         (38,225,1.4,0.9,'#80B8F0',0.52),(118,218,1.6,1.0,'#C0E0FF',0.55),
         (282,220,1.6,1.0,'#90C8FF',0.55),(362,215,1.5,1.0,'#80C0FF',0.52)]
for mx,my,mrx,mry,mc,mop in motes:
    A(f'<ellipse cx="{mx}" cy="{my}" rx="{mrx}" ry="{mry}" fill="{mc}" opacity="{mop}"/>')
    A(f'<ellipse cx="{mx}" cy="{my}" rx="{mrx*3:.1f}" ry="{mry*3:.1f}" fill="{mc}" opacity="{mop*0.10:.2f}"/>')

# Top/edge vignette
A('<rect width="400" height="600" fill="url(#cVig)"/>')

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
    ('#game-view[data-diff="ULTIMATE"] { background: rgb(26,72,184); }',
     '#game-view[data-diff="ULTIMATE"] { background: rgb(10,5,32); }'),
    ('.map-scroll[data-diff="ULTIMATE"] { background: #601868; }',
     '.map-scroll[data-diff="ULTIMATE"] { background: #0A0520; }'),
]:
    if old in html2:
        html2 = html2.replace(old, new)
        print(f'  CSS: {old[:55]}')

pattern = r"(if\(diff===.ULTIMATE.\) return \`)(.*?)(\`;)"
repl = lambda m: m.group(1) + svg + m.group(3)
new_html, n = _re.subn(pattern, repl, html2, flags=_re.DOTALL)
if n == 0:
    raise RuntimeError("ULTIMATE pattern not found in stage.html")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print(f'stage.html written. ({n} replacement)')
