#!/usr/bin/env python3
"""gen_ultimate.py — ULTIMATE: The Crystarium (FF14 Shadowbringers) — v5 precision rebuild

Exact stage node SVG coordinates (scrollW=520, scrollH=1370, viewBox 0 0 400 600):
  Stage 5  center: SVG (200, 166)  — node 84×84 DOM → ≈ 65×37 SVG units
  Stage 10 center: SVG (200, 336)  — node 96×96 DOM → ≈ 74×42 SVG units

Composition layout:
  y   0-275 : Night sky, dense stars, Crystal Tower (tip y≈5 → base skirt y≈278)
  y 145-195 : [STAGE 5] Exedra Fountain — centered at (200,166)
  y 150-275 : Left/right sandstone+iron buildings
  y 258-278 : Lakeland purple forest horizon
  y 275-600 : Dark stone plaza (tiles, crystal vein channels, lanterns, pillars)
  y 310-365 : [STAGE 10] Crystarium Main Gate — arch framing node at (200,336)
  y 245-340 : The Rotunda (dome structure, stage-right of path)
  Floating crystal shards: y 40-200
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
def star4(sx, sy, r, op, col='#FFFFFF', gc='#B0D0FF'):
    s  = f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{r:.1f}" fill="{col}" opacity="{op:.2f}"/>'
    if r > 1.5:
        s += f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{r*2.8:.1f}" fill="{gc}" opacity="{op*0.12:.2f}"/>'
        for a in (0, 90, 180, 270):
            rad = math.radians(a)
            ex = sx + math.cos(rad)*r*4.5; ey = sy + math.sin(rad)*r*4.5
            s += (f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" '
                  f'stroke="{col}" stroke-width="0.5" opacity="{op*0.42:.2f}"/>')
    return s

def shard(cx, cy, w, h, ang=0, col='#B8DCFF', op=0.76):
    hw=w/2; hh=h/2
    pts=(f'{cx:.1f},{cy-hh:.1f} {cx+hw:.1f},{cy-hh*0.22:.1f} '
         f'{cx+hw*0.62:.1f},{cy+hh:.1f} {cx-hw*0.62:.1f},{cy+hh:.1f} '
         f'{cx-hw:.1f},{cy-hh*0.22:.1f}')
    r  = f'<polygon points="{pts}" fill="{col}" opacity="{op}" transform="rotate({ang},{cx:.1f},{cy:.1f})"/>'
    # highlight
    ar = math.radians(ang-90)
    hx1=cx+math.cos(ar-0.35)*hw*0.28; hy1=cy+math.sin(ar-0.35)*hh*0.80
    hx2=cx+math.cos(ar)*hw*0.10;      hy2=cy+math.sin(ar)*hh*0.32
    r += (f'<line x1="{hx1:.1f}" y1="{hy1:.1f}" x2="{hx2:.1f}" y2="{hy2:.1f}" '
          f'stroke="#FFFFFF" stroke-width="1.8" opacity="{op*0.55:.2f}" '
          f'transform="rotate({ang},{cx:.1f},{cy:.1f})"/>')
    r += f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{w:.0f}" ry="{h*0.48:.0f}" fill="{col}" opacity="{op*0.10:.2f}"/>'
    return r

def lamp(lx, ly, h=30):
    lx=int(lx); ly=int(ly)
    out=[]
    out.append(f'<line x1="{lx}" y1="{ly}" x2="{lx}" y2="{ly-h}" stroke="#181820" stroke-width="2.8"/>')
    # bracket arm
    out.append(f'<line x1="{lx}" y1="{ly-h+7}" x2="{lx+5}" y2="{ly-h+1}" stroke="#181820" stroke-width="1.8"/>')
    # finial ball
    out.append(f'<circle cx="{lx}" cy="{ly-h}" r="2.5" fill="#181820"/>')
    # cage
    bx=lx-4; by=ly-h-11
    out.append(f'<rect x="{bx}" y="{by}" width="8" height="11" fill="#141418" rx="1"/>')
    # glass warm amber
    out.append(f'<rect x="{bx+1}" y="{by+1}" width="6" height="9" fill="#FFC030" rx="1" opacity="0.90"/>')
    out.append(f'<rect x="{bx+2}" y="{by+1}" width="3" height="4" fill="#FFE888" opacity="0.55"/>')
    # cap
    out.append(f'<rect x="{bx-1}" y="{by-3}" width="10" height="4" fill="#181820" rx="1"/>')
    # glow halos
    gcx=lx; gcy=ly-h-6
    out.append(f'<ellipse cx="{gcx}" cy="{gcy}" rx="14" ry="12" fill="#FFB020" opacity="0.20"/>')
    out.append(f'<ellipse cx="{gcx}" cy="{gcy}" rx="28" ry="24" fill="#FF8800" opacity="0.07"/>')
    return ''.join(out)

def iron_win(wx, wy, ww, wh, op=0.65):
    wx=int(wx); wy=int(wy); ww=int(ww); wh=int(wh)
    rr=int(ww*0.44)
    out=(f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" fill="#0A0F1E" rx="{rr}" opacity="0.93"/>'
         f'<rect x="{wx+2}" y="{wy+2}" width="{ww-4}" height="{wh-4}" fill="#58AFF0" rx="{rr}" opacity="{op:.2f}"/>'
         f'<ellipse cx="{wx+int(ww*0.38)}" cy="{wy+int(wh*0.28)}" '
         f'rx="{int(ww*0.25)}" ry="{int(wh*0.22)}" fill="#A8D8FF" opacity="0.42"/>'
         f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" fill="none" '
         f'stroke="#181820" stroke-width="2" rx="{rr}" opacity="0.85"/>'
         f'<ellipse cx="{wx+ww//2}" cy="{wy+wh//2}" rx="{int(ww*0.75)}" ry="{int(wh*0.75)}" '
         f'fill="#3880D0" opacity="0.10"/>')
    return out

# ═══════════════════════════════════════════════════════════════════════════
#  GRADIENTS
# ═══════════════════════════════════════════════════════════════════════════
A('<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"><defs>')

# Sky — near-black indigo (restored night of The First)
A('<linearGradient id="gSky" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#020110"/>'
  '<stop offset="16%"  stop-color="#06031C"/>'
  '<stop offset="34%"  stop-color="#0B0728"/>'
  '<stop offset="55%"  stop-color="#110C3A"/>'
  '<stop offset="75%"  stop-color="#171150"/>'
  '<stop offset="90%"  stop-color="#1C1660"/>'
  '<stop offset="100%" stop-color="#201A6E"/>'
  '</linearGradient>')

# Crystal Tower — glow spread (illuminates entire scene)
A('<radialGradient id="gTGlow" cx="50%" cy="22%" r="72%">'
  '<stop offset="0%"   stop-color="#D0ECFF" stop-opacity="0.95"/>'
  '<stop offset="10%"  stop-color="#A0D0FF" stop-opacity="0.70"/>'
  '<stop offset="25%"  stop-color="#68B0FF" stop-opacity="0.38"/>'
  '<stop offset="48%"  stop-color="#3868E0" stop-opacity="0.13"/>'
  '<stop offset="72%"  stop-color="#1A3890" stop-opacity="0.04"/>'
  '<stop offset="100%" stop-color="#0C1840" stop-opacity="0"/>'
  '</radialGradient>')

# Tower base horizon glow
A('<radialGradient id="gTBase" cx="50%" cy="80%" r="55%">'
  '<stop offset="0%"   stop-color="#88C0FF" stop-opacity="0.52"/>'
  '<stop offset="38%"  stop-color="#5090E8" stop-opacity="0.18"/>'
  '<stop offset="70%"  stop-color="#2050A0" stop-opacity="0.05"/>'
  '<stop offset="100%" stop-color="#0C1840" stop-opacity="0"/>'
  '</radialGradient>')

# Tower body (face — ice white)
A('<linearGradient id="gTFace" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#88C4F8"/>'
  '<stop offset="20%"  stop-color="#C4E6FF"/>'
  '<stop offset="44%"  stop-color="#F8FDFF"/>'
  '<stop offset="68%"  stop-color="#DCF0FF"/>'
  '<stop offset="88%"  stop-color="#A8D4F8"/>'
  '<stop offset="100%" stop-color="#78B0E8"/>'
  '</linearGradient>')

# Tower vertical (bright tip → deeper base)
A('<linearGradient id="gTVert" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FFFFFF"/>'
  '<stop offset="15%"  stop-color="#EEF8FF"/>'
  '<stop offset="38%"  stop-color="#C0E0FF"/>'
  '<stop offset="62%"  stop-color="#88C0F0"/>'
  '<stop offset="82%"  stop-color="#58A0D8"/>'
  '<stop offset="100%" stop-color="#3878C0"/>'
  '</linearGradient>')

# Ring bands on tower
A('<linearGradient id="gRing" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FFFFFF"/>'
  '<stop offset="28%"  stop-color="#C8EAFF"/>'
  '<stop offset="62%"  stop-color="#80C0F8"/>'
  '<stop offset="100%" stop-color="#4898E8"/>'
  '</linearGradient>')

# Crystal panel (Rotunda dome, windows)
A('<linearGradient id="gCPanel" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#FFFFFF" stop-opacity="0.92"/>'
  '<stop offset="22%"  stop-color="#C8EAFF" stop-opacity="0.80"/>'
  '<stop offset="55%"  stop-color="#78B8F0" stop-opacity="0.62"/>'
  '<stop offset="100%" stop-color="#3888D0" stop-opacity="0.45"/>'
  '</linearGradient>')

# Sandstone lit (main building material)
A('<linearGradient id="gSandL" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#CCB888"/>'
  '<stop offset="35%"  stop-color="#BAA878"/>'
  '<stop offset="68%"  stop-color="#A09060"/>'
  '<stop offset="100%" stop-color="#887848"/>'
  '</linearGradient>')

# Sandstone shadow
A('<linearGradient id="gSandS" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#AAAA98"/>'
  '<stop offset="42%"  stop-color="#989080"/>'
  '<stop offset="100%" stop-color="#807868"/>'
  '</linearGradient>')

# Black iron (structural framing)
A('<linearGradient id="gIron" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#2C2A3A"/>'
  '<stop offset="50%"  stop-color="#1C1A28"/>'
  '<stop offset="100%" stop-color="#12101E"/>'
  '</linearGradient>')

# Ground — dark stone plaza
A('<linearGradient id="gGnd" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#222538"/>'
  '<stop offset="32%"  stop-color="#1C1E30"/>'
  '<stop offset="65%"  stop-color="#141628"/>'
  '<stop offset="100%" stop-color="#0C0E1E"/>'
  '</linearGradient>')

# Purple forest (Lakeland)
A('<linearGradient id="gForest" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#481890" stop-opacity="0.55"/>'
  '<stop offset="50%"  stop-color="#321060" stop-opacity="0.80"/>'
  '<stop offset="100%" stop-color="#1E0840" stop-opacity="0.92"/>'
  '</linearGradient>')

# Fountain water
A('<radialGradient id="gWater" cx="50%" cy="32%" r="62%">'
  '<stop offset="0%"   stop-color="#B4E2FF" stop-opacity="0.96"/>'
  '<stop offset="42%"  stop-color="#62B8F0" stop-opacity="0.82"/>'
  '<stop offset="100%" stop-color="#2878C0" stop-opacity="0.70"/>'
  '</radialGradient>')

# Gate energy shimmer (Crystal Tower through arch)
A('<linearGradient id="gShimmer" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#80C8FF" stop-opacity="0.06"/>'
  '<stop offset="28%"  stop-color="#58B0FF" stop-opacity="0.30"/>'
  '<stop offset="52%"  stop-color="#48A8FF" stop-opacity="0.44"/>'
  '<stop offset="76%"  stop-color="#58B0FF" stop-opacity="0.26"/>'
  '<stop offset="100%" stop-color="#80C8FF" stop-opacity="0.05"/>'
  '</linearGradient>')

# Bottom haze
A('<linearGradient id="gHaze" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#0C0E1E" stop-opacity="0"/>'
  '<stop offset="50%"  stop-color="#080A16" stop-opacity="0.35"/>'
  '<stop offset="100%" stop-color="#040610" stop-opacity="0.80"/>'
  '</linearGradient>')

# Edge vignette
A('<radialGradient id="gVig" cx="50%" cy="12%" r="94%">'
  '<stop offset="50%"  stop-color="#000000" stop-opacity="0"/>'
  '<stop offset="100%" stop-color="#010108" stop-opacity="0.74"/>'
  '</radialGradient>')

# Pillar shaft
A('<linearGradient id="gPillar" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#28263A"/>'
  '<stop offset="38%"  stop-color="#343248"/>'
  '<stop offset="62%"  stop-color="#2A2838"/>'
  '<stop offset="100%" stop-color="#1C1A28"/>'
  '</linearGradient>')

A('</defs>')

# ═══════════════════════════════════════════════════════════════════════════
#  1. SKY
# ═══════════════════════════════════════════════════════════════════════════
A('<rect width="400" height="600" fill="url(#gSky)"/>')
A('<rect width="400" height="600" fill="url(#gTGlow)"/>')
A('<rect width="400" height="600" fill="url(#gTBase)"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  2. STARS
# ═══════════════════════════════════════════════════════════════════════════
for _ in range(240):
    sx=_r.uniform(0,400); sy=_r.uniform(0,268)
    sr=_r.uniform(0.45,1.30); sop=_r.uniform(0.38,0.88)
    sc=_r.choice(['#FFFFFF','#FFFFFF','#EEF4FF','#F4F8FF','#FFF8F0'])
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr:.1f}" fill="{sc}" opacity="{sop:.2f}"/>')
for _ in range(48):
    sx=_r.uniform(0,400); sy=_r.uniform(0,260)
    sr=_r.uniform(1.25,1.95); sop=_r.uniform(0.62,0.92)
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr:.1f}" fill="#FFFFFF" opacity="{sop:.2f}"/>')
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr*2.8:.1f}" fill="#B8D0FF" opacity="{sop*0.10:.2f}"/>')
for bsx,bsy,bsr,bsop in [(25,20,2.2,0.98),(352,15,2.4,0.97),(78,42,1.9,0.94),
    (186,12,2.5,0.99),(292,36,2.1,0.96),(132,25,1.8,0.92),
    (318,52,2.0,0.95),(55,65,1.7,0.90),(248,20,2.3,0.97),
    (388,40,1.8,0.92),(162,55,1.9,0.91),(308,16,2.0,0.95)]:
    A(star4(bsx, bsy, bsr, bsop))

# ═══════════════════════════════════════════════════════════════════════════
#  3. CRYSTAL TOWER — "a gleaming spear of crystal pointed at the heavens"
#     Tip at (200,4), base skirt at y≈278. Stage 5 at y=166 is tower midpoint.
# ═══════════════════════════════════════════════════════════════════════════
T = 200  # center x

# Width function: tower half-width at SVG y
def tw(y):
    return max(2, 3 + y * 0.275)   # 2px at tip → ~80px half at base

# Background secondary spires (multi-spired Crystal Tower look)
for sp_off, sp_w, sp_h, sp_op in [
    (-32, 7, 215, 0.35), (32, 7, 205, 0.35),
    (-55, 5, 165, 0.25), (55, 5, 155, 0.25),
    (-72, 3, 120, 0.18), (72, 3, 112, 0.18),
]:
    scx = T + sp_off
    A(f'<polygon points="{scx},{10-sp_w//3:.0f} '
      f'{scx+sp_w},{10+sp_h*0.28:.0f} '
      f'{scx+sp_w*0.7},{10+sp_h:.0f} '
      f'{scx-sp_w*0.7},{10+sp_h:.0f} '
      f'{scx-sp_w},{10+sp_h*0.28:.0f}" '
      f'fill="url(#gTVert)" opacity="{sp_op}"/>')

# Main tower shaft
pts_r = ' '.join(f'{T+tw(y):.0f},{y}' for y in range(278, -1, -22))
pts_l = ' '.join(f'{T-tw(y):.0f},{y}' for y in range(0, 279, 22))
A(f'<polygon points="{T},3 {pts_r} {pts_l}" fill="url(#gTVert)" opacity="0.92"/>')

# Face shading (left/right panels)
A(f'<polygon points="{T},3 '
  f'{T+tw(60):.0f},60 {T+tw(130):.0f},130 {T+tw(200):.0f},200 {T+tw(278):.0f},278 '
  f'{T},278" fill="#B8D8F8" opacity="0.20"/>')
A(f'<polygon points="{T},3 '
  f'{T-tw(60):.0f},60 {T-tw(130):.0f},130 {T-tw(200):.0f},200 {T-tw(278):.0f},278 '
  f'{T},278" fill="#183060" opacity="0.14"/>')

# Vertical highlight streaks (crystal facets)
for vx_off, vw, vop in [(0,5,0.88),(-8,2.5,0.62),(10,2.5,0.56),(-20,1.5,0.30),(22,1.5,0.28)]:
    A(f'<rect x="{T+vx_off-vw/2:.1f}" y="3" width="{vw}" height="276" fill="#FFFFFF" opacity="{vop}" rx="1"/>')

# Needle tip
A(f'<polygon points="{T},3 {T+14},34 {T-14},34" fill="#FFFFFF" opacity="0.98"/>')
A(f'<polygon points="{T},3 {T+8},22 {T-8},22" fill="#FFFFFF" opacity="0.82"/>')
# Tip glow burst
A(f'<circle cx="{T}" cy="6" r="12" fill="#FFFFFF" opacity="0.38"/>')
A(f'<circle cx="{T}" cy="6" r="26" fill="#C0E8FF" opacity="0.16"/>')
A(f'<circle cx="{T}" cy="6" r="48" fill="#90C8FF" opacity="0.06"/>')

# Crystal ring bands (prominent horizontal bands — iconic Crystal Tower feature)
# Positions tuned to NOT overlap stage 5 object (y=166) and look natural
for ry, rh, rop in [(35,7,0.88),(80,6,0.82),(128,5.5,0.75),(210,5,0.65),(258,4.5,0.56)]:
    hw = tw(ry) + 5
    A(f'<rect x="{T-hw:.0f}" y="{ry}" width="{hw*2:.0f}" height="{rh}" fill="url(#gRing)" rx="2" opacity="{rop}"/>')
    A(f'<ellipse cx="{T}" cy="{ry+rh/2:.1f}" rx="{hw+18:.0f}" ry="{rh+4:.0f}" fill="#78B8FF" opacity="{rop*0.20:.2f}"/>')

# Tower base skirt + glow
bw = tw(278)
A(f'<polygon points="{T-bw:.0f},278 {T-bw-44},298 {T-bw-46},308 '
  f'{T},315 {T+bw+46},308 {T+bw+44},298 {T+bw:.0f},278" '
  f'fill="url(#gTVert)" opacity="0.60"/>')
A(f'<ellipse cx="{T}" cy="308" rx="98" ry="22" fill="#B8E0FF" opacity="0.52"/>')
A(f'<ellipse cx="{T}" cy="308" rx="72" ry="14" fill="#D8F0FF" opacity="0.70"/>')
A(f'<ellipse cx="{T}" cy="308" rx="42" ry="8" fill="#FFFFFF" opacity="0.82"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  4. FLOATING CRYSTAL SHARDS (sky, y 40-205, avoid stage 5 area y 148-185)
# ═══════════════════════════════════════════════════════════════════════════
shards_data = [
    (52,  108, 14, 36, -22, '#A8D0FF', 0.78),
    (75,  142, 9,  22, 18,  '#C8E8FF', 0.70),
    (42,  78,  7,  18, -38, '#D0EEFF', 0.65),
    (88,  128, 12, 28, -12, '#C0E4FF', 0.72),
    (62,  195, 6,  14, 28,  '#B8DCFF', 0.58),
    (345, 115, 15, 38, 24,  '#A0CCFF', 0.76),
    (362, 88,  9,  24, -18, '#C8E8FF', 0.68),
    (322, 148, 8,  20, 35,  '#B8DCFF', 0.62),
    (348, 188, 6,  15, -28, '#D0EEFF', 0.56),
    (308, 94,  12, 28, 15,  '#B0D8FF', 0.70),
    (136, 55,  10, 24, -8,  '#C0E0FF', 0.64),
    (258, 62,  11, 27, 20,  '#B8DCFF', 0.66),
    (112, 85,  7,  16, 44,  '#D8EEFF', 0.54),
    (285, 80,  8,  18, -30, '#C8E4FF', 0.60),
    (158, 42,  9,  20, -5,  '#A8D4FF', 0.62),
    (240, 46,  8,  18, 14,  '#C0E0FF', 0.58),
    (105, 200, 6,  13, -18, '#D0ECFF', 0.50),
    (292, 198, 7,  15, 25,  '#C8E4FF', 0.52),
]
for d in shards_data:
    A(shard(*d))

# ═══════════════════════════════════════════════════════════════════════════
#  5. LAKELAND PURPLE FOREST (y 255-278)
# ═══════════════════════════════════════════════════════════════════════════
# Left forest
A('<path d="M0,272 Q12,252 28,262 Q44,240 62,257 Q78,234 98,252 '
  'Q114,232 132,248 Q146,236 154,252 L154,282 L0,282 Z" fill="#3E1872" opacity="0.82"/>')
A('<path d="M0,278 Q18,260 36,270 Q54,250 74,264 Q90,248 108,262 '
  'Q124,252 140,265 L140,282 L0,282 Z" fill="#280E50" opacity="0.62"/>')
for tx,ty,tr in [(14,256,11),(34,246,13),(56,242,12),(76,246,14),(98,240,12),(118,244,11),(140,250,10)]:
    A(f'<ellipse cx="{tx}" cy="{ty}" rx="{tr}" ry="{int(tr*0.72)}" fill="#4C2298" opacity="0.90"/>')
    A(f'<ellipse cx="{tx-2}" cy="{ty-4}" rx="{int(tr*0.56)}" ry="{int(tr*0.44)}" fill="#5E2AAA" opacity="0.65"/>')
# Right forest
A('<path d="M246,282 L246,252 Q264,234 284,250 Q300,232 320,248 '
  'Q336,232 356,250 Q370,240 388,256 Q396,250 400,256 L400,282 Z" fill="#3E1872" opacity="0.82"/>')
A('<path d="M260,282 L260,264 Q278,248 298,262 Q316,246 336,262 '
  'Q354,252 374,268 L400,272 L400,282 Z" fill="#280E50" opacity="0.62"/>')
for tx,ty,tr in [(262,250,11),(284,242,13),(306,236,12),(326,242,14),(348,238,12),(368,246,11),(388,252,10)]:
    A(f'<ellipse cx="{tx}" cy="{ty}" rx="{tr}" ry="{int(tr*0.72)}" fill="#4C2298" opacity="0.90"/>')
    A(f'<ellipse cx="{tx+2}" cy="{ty-4}" rx="{int(tr*0.56)}" ry="{int(tr*0.44)}" fill="#5E2AAA" opacity="0.65"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  6. LEFT & RIGHT BUILDING WINGS (sandstone + black iron, y 145-278)
# ═══════════════════════════════════════════════════════════════════════════
def wing(bx, by, bw, bh, side='L'):
    G = 'gSandL' if side=='L' else 'gSandS'
    Gs= 'gSandS' if side=='L' else 'gSandL'
    out=[]
    # Sub-building behind
    sbx = bx+4 if side=='L' else bx-4
    sbw = int(bw*0.68); sbh = int(bh*0.75)
    out.append(f'<rect x="{sbx}" y="{by+bh-sbh}" width="{sbw}" height="{sbh}" fill="url(#{Gs})" rx="2" opacity="0.85"/>')
    out.append(f'<line x1="{sbx-1}" y1="{by+bh-sbh}" x2="{sbx+sbw+1}" y2="{by+bh-sbh}" stroke="#181820" stroke-width="3" opacity="0.78"/>')
    # Main body
    out.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="url(#{G})" rx="2" opacity="0.95"/>')
    # Iron pilasters (vertical strips)
    n_pil = max(3, bw//22)
    for pi in range(n_pil+1):
        px2 = bx + pi*(bw/n_pil)
        out.append(f'<rect x="{px2-2.5:.0f}" y="{by}" width="5" height="{bh}" fill="url(#gIron)" rx="1" opacity="0.70"/>')
    # Iron horizontal band courses
    for frac in [0.0, 0.20, 0.42, 0.64, 0.84]:
        by2 = by + bh*frac
        out.append(f'<rect x="{bx-2}" y="{by2:.0f}" width="{bw+4}" height="4" fill="url(#gIron)" rx="1" opacity="0.68"/>')
    # Crystal-glow windows (3 rows)
    ww=int(bw*0.28); wh=int(bh*0.11)
    for row in range(3):
        wy2=int(by + bh*(0.15+row*0.26))
        wx2=int(bx + (bw-ww)*0.50)
        out.append(iron_win(wx2, wy2, ww, wh, 0.62))
    # Crenellated parapet
    mx=bx+3
    while mx < bx+bw-6:
        out.append(f'<rect x="{mx:.0f}" y="{by-9}" width="6" height="11" fill="url(#gIron)" rx="1" opacity="0.82"/>')
        mx += 10
    out.append(f'<line x1="{bx-2}" y1="{by-9}" x2="{bx+bw+2}" y2="{by-9}" stroke="url(#gRing)" stroke-width="2" opacity="0.45"/>')
    # Corner crystal turrets
    for tx2 in [bx+7, bx+bw-7]:
        out.append(f'<polygon points="{tx2},{by-9-16} {tx2+5},{by-9} {tx2-5},{by-9}" fill="url(#gRing)" opacity="0.82"/>')
        out.append(f'<ellipse cx="{tx2}" cy="{by-9-10}" rx="6" ry="6" fill="#50A8F0" opacity="0.14"/>')
    return ''.join(out)

A(wing(bx=-14, by=148, bw=105, bh=132, side='L'))
A(wing(bx=309, by=148, bw=105, bh=132, side='R'))

# Building wall lanterns
for lx2,ly2 in [(18,200),(18,248),(382,200),(382,248)]:
    A(lamp(lx2, ly2, h=18))

# ═══════════════════════════════════════════════════════════════════════════
#  7. DISTANT CITY SKYLINE (behind buildings, y 248-278)
# ═══════════════════════════════════════════════════════════════════════════
A('<path d="M0,252 L0,272 L16,272 L16,256 L26,256 L26,268 L38,268 '
  'L38,250 L50,250 L50,264 L60,264 L60,254 L70,254 L70,262 '
  'L78,262 L78,252 L90,252 L90,262 L100,262 L100,254" '
  'fill="url(#gSandS)" opacity="0.65"/>')
A('<path d="M300,254 L300,262 L310,262 L310,252 L320,252 L320,262 '
  'L330,262 L330,252 L342,252 L342,264 L352,264 L352,254 '
  'L362,254 L362,268 L374,268 L374,256 L384,256 L384,272 L400,272 L400,252" '
  'fill="url(#gSandS)" opacity="0.65"/>')
# Tiny amber windows on distant buildings
for wx2,wy2 in [(22,257),(46,254),(66,258),(84,256),
                (312,256),(334,256),(356,258),(376,260)]:
    A(f'<rect x="{wx2}" y="{wy2}" width="5" height="4" fill="#FFC030" rx="1" opacity="0.60"/>')
# Iron roofline
A('<line x1="0" y1="252" x2="100" y2="252" stroke="#181820" stroke-width="2" opacity="0.72"/>')
A('<line x1="300" y1="252" x2="400" y2="252" stroke="#181820" stroke-width="2" opacity="0.72"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  8. GROUND PLAZA (dark stone, y 278-600)
# ═══════════════════════════════════════════════════════════════════════════
A('<rect y="278" width="400" height="322" fill="url(#gGnd)"/>')
# Crystal-lit platform edge
A('<rect y="276" width="400" height="4" fill="url(#gRing)" opacity="0.35"/>')
A('<ellipse cx="200" cy="278" rx="200" ry="7" fill="#5898E0" opacity="0.16"/>')
# Tile grid
for ty2 in range(285, 600, 26):
    A(f'<line x1="0" y1="{ty2}" x2="400" y2="{ty2}" stroke="#1A1C2C" stroke-width="1.2" opacity="0.46"/>')
for tx2 in range(0, 401, 28):
    A(f'<line x1="{tx2}" y1="278" x2="{tx2}" y2="600" stroke="#1A1C2C" stroke-width="0.9" opacity="0.36"/>')
# Crystal aether veins in floor
for vpath, vop in [
    ("M200,278 Q193,310 186,360 L180,430 L177,520 L175,600", 0.38),
    ("M200,278 Q207,310 214,360 L220,430 L223,520 L225,600", 0.38),
    ("M200,278 Q182,305 165,330 L142,370 L115,420",          0.24),
    ("M200,278 Q218,305 235,330 L258,370 L285,420",          0.24),
]:
    A(f'<path d="{vpath}" fill="none" stroke="#3878C8" stroke-width="2.5" opacity="{vop*0.40:.2f}"/>')
    A(f'<path d="{vpath}" fill="none" stroke="#88C8FF" stroke-width="0.7" opacity="{vop:.2f}"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  9. CRYSTAL PILLARS (flanking path, y 285-380)
# ═══════════════════════════════════════════════════════════════════════════
def xpillar(px, py, h=75, w=12):
    out=[]
    # stone base plinth
    out.append(f'<rect x="{px-w//2-4}" y="{py-10}" width="{w+8}" height="12" fill="url(#gSandS)" rx="2" opacity="0.88"/>')
    out.append(f'<line x1="{px-w//2-5}" y1="{py-10}" x2="{px+w//2+5}" y2="{py-10}" stroke="#181820" stroke-width="2.5" opacity="0.72"/>')
    # shaft
    out.append(f'<rect x="{px-w//2}" y="{py-10-h}" width="{w}" height="{h}" fill="url(#gPillar)" rx="2" opacity="0.92"/>')
    out.append(f'<rect x="{px-w//2}" y="{py-10-h}" width="3" height="{h}" fill="url(#gIron)" opacity="0.55"/>')
    out.append(f'<rect x="{px+w//2-3}" y="{py-10-h}" width="3" height="{h}" fill="url(#gIron)" opacity="0.55"/>')
    # iron capital ring
    out.append(f'<rect x="{px-w//2-5}" y="{py-10-h-4}" width="{w+10}" height="5" fill="url(#gIron)" rx="1" opacity="0.80"/>')
    # crystal shard cap
    A_pts=f'{px},{py-10-h-20} {px+w//2+4},{py-10-h-2} {px-w//2-4},{py-10-h-2}'
    out.append(f'<polygon points="{A_pts}" fill="url(#gRing)" opacity="0.88"/>')
    out.append(f'<polygon points="{A_pts}" fill="url(#gCPanel)" opacity="0.40"/>')
    # highlight
    out.append(f'<line x1="{px-2}" y1="{py-10-h-18}" x2="{px-2}" y2="{py-12}" stroke="#FFFFFF" stroke-width="1.2" opacity="0.20"/>')
    # glow
    out.append(f'<ellipse cx="{px}" cy="{py-10-h-10}" rx="{w+5:.0f}" ry="15" fill="#60B0F0" opacity="0.22"/>')
    out.append(f'<ellipse cx="{px}" cy="{py-10-h-10}" rx="{w*2:.0f}" ry="28" fill="#4090D8" opacity="0.08"/>')
    return ''.join(out)

A(xpillar(80,  418, h=70, w=14))
A(xpillar(108, 404, h=60, w=12))
A(xpillar(136, 392, h=52, w=11))
A(xpillar(320, 418, h=70, w=14))
A(xpillar(292, 404, h=60, w=12))
A(xpillar(264, 392, h=52, w=11))

# ═══════════════════════════════════════════════════════════════════════════
#  10. THE ROTUNDA — left of path (y 248-340)
#      "Elegant black iron and sheets of shimmering crystal" — domed hall
# ═══════════════════════════════════════════════════════════════════════════
rx0=88;  rot_base=340
drum_h=50; drum_r=40

# Steps
for si,(sw2,sh2) in enumerate([(96,8),(78,7),(62,6)]):
    sy2=rot_base-si*7
    A(f'<rect x="{rx0-sw2//2}" y="{sy2-sh2}" width="{sw2}" height="{sh2}" fill="url(#gSandL)" rx="2" opacity="0.86"/>')
    A(f'<line x1="{rx0-sw2//2-1}" y1="{sy2-sh2}" x2="{rx0+sw2//2+1}" y2="{sy2-sh2}" stroke="#181820" stroke-width="2" opacity="0.70"/>')

# Drum
drum_y = rot_base - 22
A(f'<rect x="{rx0-drum_r}" y="{drum_y-drum_h}" width="{drum_r*2}" height="{drum_h}" fill="url(#gSandL)" rx="3" opacity="0.93"/>')
# Pilasters
for pi in range(5):
    px2=rx0-drum_r+pi*(drum_r*2/4)
    A(f'<rect x="{px2-2.5:.0f}" y="{drum_y-drum_h}" width="5" height="{drum_h}" fill="url(#gIron)" rx="1" opacity="0.72"/>')
# Entablature
A(f'<rect x="{rx0-drum_r-3}" y="{drum_y-drum_h-7}" width="{drum_r*2+6}" height="9" fill="url(#gIron)" rx="1" opacity="0.88"/>')
A(f'<rect x="{rx0-drum_r+3}" y="{drum_y-drum_h-5}" width="{(drum_r-3)*2}" height="5" fill="url(#gCPanel)" rx="1" opacity="0.40"/>')
# Windows
for wi in range(3):
    wx2=rx0-22+wi*22; wy2=drum_y-drum_h+drum_h*0.20
    A(iron_win(int(wx2), int(wy2), 12, int(drum_h*0.50), 0.58))

# Dome base ring
dome_cy=drum_y-drum_h-7; dome_rx=drum_r+4; dome_ry=36
A(f'<rect x="{rx0-dome_rx-2}" y="{dome_cy-4}" width="{(dome_rx+2)*2}" height="6" fill="url(#gIron)" rx="1" opacity="0.90"/>')
A(f'<rect x="{rx0-dome_rx-2}" y="{dome_cy-6}" width="{(dome_rx+2)*2}" height="3" fill="url(#gRing)" rx="1" opacity="0.45"/>')

# Dome body
A(f'<ellipse cx="{rx0}" cy="{dome_cy}" rx="{dome_rx}" ry="{dome_ry}" fill="#0C1828" opacity="0.88"/>')
A(f'<ellipse cx="{rx0}" cy="{dome_cy}" rx="{dome_rx}" ry="{dome_ry}" fill="url(#gTGlow)" opacity="0.52"/>')
A(f'<ellipse cx="{rx0}" cy="{dome_cy}" rx="{dome_rx}" ry="{dome_ry}" fill="url(#gCPanel)" opacity="0.28"/>')
# Highlight
A(f'<ellipse cx="{rx0-12}" cy="{dome_cy-16}" rx="{int(dome_rx*0.38)}" ry="{int(dome_ry*0.28)}" fill="#A8D8FF" opacity="0.30"/>')
# Iron ribs
for ri in range(8):
    ang=math.radians(ri*22.5)
    ex=rx0+math.cos(ang)*dome_rx; ey=dome_cy+math.sin(ang)*dome_ry
    A(f'<line x1="{rx0}" y1="{dome_cy-dome_ry}" x2="{ex:.0f}" y2="{ey:.0f}" stroke="#181820" stroke-width="2.8" opacity="0.85"/>')
# Oculus + finial
A(f'<circle cx="{rx0}" cy="{dome_cy-dome_ry}" r="7" fill="url(#gIron)" opacity="0.90"/>')
A(f'<circle cx="{rx0}" cy="{dome_cy-dome_ry}" r="4" fill="url(#gRing)" opacity="0.82"/>')
fin_y=dome_cy-dome_ry-8
A(f'<polygon points="{rx0},{fin_y-20} {rx0+7},{fin_y} {rx0-7},{fin_y}" fill="url(#gRing)" opacity="0.90"/>')
A(f'<polygon points="{rx0},{fin_y-20} {rx0+4},{fin_y-10} {rx0-4},{fin_y-10}" fill="#FFFFFF" opacity="0.75"/>')
A(f'<circle cx="{rx0}" cy="{fin_y-12}" r="7" fill="#80C8FF" opacity="0.20"/>')
# Base collar
A(f'<ellipse cx="{rx0}" cy="{dome_cy}" rx="{dome_rx+2}" ry="7" fill="url(#gIron)" opacity="0.88"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  STAGE 5 OBJECT — THE EXEDRA FOUNTAIN  (centered at SVG 200, 166)
#  Crystal fountain basin + pedestal + glowing crystal obelisk
# ═══════════════════════════════════════════════════════════════════════════
# Target: node center at (200, 166). Object spans y ≈ 120-188.

FC = 200   # fountain center x
FB = 182   # fountain base (lower basin bottom)

# ── lower basin (wide circular pool) ──
A(f'<ellipse cx="{FC}" cy="{FB}" rx="52" ry="13" fill="#080E1C" opacity="0.88"/>')
A(f'<ellipse cx="{FC}" cy="{FB}" rx="52" ry="13" fill="url(#gWater)" opacity="0.58"/>')
# Water reflections
A(f'<ellipse cx="{FC-12}" cy="{FB-3}" rx="18" ry="5" fill="#C0E8FF" opacity="0.25"/>')
for rr in (0.55, 0.75, 0.92):
    A(f'<ellipse cx="{FC}" cy="{FB}" rx="{52*rr:.0f}" ry="{13*rr:.0f}" fill="none" stroke="#68C0FF" stroke-width="1.2" opacity="0.32"/>')
# Basin wall (sandstone + iron)
A(f'<rect x="{FC-54}" y="{FB-12}" width="108" height="12" fill="url(#gSandL)" rx="2" opacity="0.90"/>')
A(f'<ellipse cx="{FC}" cy="{FB-12}" rx="54" ry="8" fill="url(#gSandL)" opacity="0.90"/>')
A(f'<line x1="{FC-55}" y1="{FB-12}" x2="{FC+55}" y2="{FB-12}" stroke="#181820" stroke-width="2.5" opacity="0.75"/>')
A(f'<ellipse cx="{FC}" cy="{FB-12}" rx="54" ry="8" fill="none" stroke="url(#gRing)" stroke-width="2" opacity="0.45"/>')
# Iron bracket pins around basin
for bi in range(6):
    bang=math.radians(bi*60)
    bx2=FC+math.cos(bang)*50; by2=FB+math.sin(bang)*13-12
    A(f'<circle cx="{bx2:.0f}" cy="{by2:.0f}" r="2.8" fill="url(#gIron)" opacity="0.80"/>')

# ── pedestal column ──
A(f'<rect x="{FC-7}" y="{FB-68}" width="14" height="56" fill="url(#gSandL)" rx="3" opacity="0.92"/>')
A(f'<line x1="{FC-8}" y1="{FB-68}" x2="{FC+8}" y2="{FB-68}" stroke="#181820" stroke-width="2.5" opacity="0.72"/>')
A(f'<line x1="{FC-8}" y1="{FB-13}" x2="{FC+8}" y2="{FB-13}" stroke="#181820" stroke-width="2.5" opacity="0.72"/>')
# Iron fluting on column
for fl in (-3, 0, 3):
    A(f'<line x1="{FC+fl}" y1="{FB-68}" x2="{FC+fl}" y2="{FB-14}" stroke="#181820" stroke-width="1.2" opacity="0.38"/>')

# ── upper basin (elevated) ──
A(f'<ellipse cx="{FC}" cy="{FB-70}" rx="26" ry="7" fill="#080E1C" opacity="0.88"/>')
A(f'<ellipse cx="{FC}" cy="{FB-70}" rx="26" ry="7" fill="url(#gWater)" opacity="0.52"/>')
A(f'<rect x="{FC-28}" y="{FB-78}" width="56" height="8" fill="url(#gSandL)" rx="2" opacity="0.90"/>')
A(f'<ellipse cx="{FC}" cy="{FB-78}" rx="28" ry="7" fill="url(#gSandL)" opacity="0.90"/>')
A(f'<line x1="{FC-29}" y1="{FB-78}" x2="{FC+29}" y2="{FB-78}" stroke="#181820" stroke-width="2" opacity="0.70"/>')
A(f'<ellipse cx="{FC}" cy="{FB-78}" rx="28" ry="7" fill="none" stroke="url(#gRing)" stroke-width="1.8" opacity="0.45"/>')

# ── crystal obelisk (the glowing centerpiece) ──
# Node center at y=166. Obelisk tip at y=124, body to y=170.
# The node (y=166) is right at the widest part of the obelisk.
A(f'<polygon points="{FC},{FB-116} {FC+13},{FB-78} {FC-13},{FB-78}" fill="url(#gTVert)" opacity="0.92"/>')
A(f'<polygon points="{FC},{FB-116} {FC+8},{FB-96} {FC-8},{FB-96}" fill="#FFFFFF" opacity="0.72"/>')
# Facet highlight
A(f'<line x1="{FC+2}" y1="{FB-114}" x2="{FC+2}" y2="{FB-80}" stroke="#FFFFFF" stroke-width="1.5" opacity="0.52"/>')
# Crystal ring bands on obelisk (smaller mirror of tower)
for oby, obh in [(FB-106, 2.5), (FB-92, 2.5), (FB-88, 2)]:
    A(f'<rect x="{FC-10}" y="{oby}" width="20" height="{obh}" fill="url(#gRing)" opacity="0.72"/>')
# Multi-layer glow
A(f'<ellipse cx="{FC}" cy="{FB-98}" rx="28" ry="28" fill="#58B0FF" opacity="0.13"/>')
A(f'<ellipse cx="{FC}" cy="{FB-98}" rx="18" ry="20" fill="#88D0FF" opacity="0.20"/>')
A(f'<ellipse cx="{FC}" cy="{FB-102}" rx="9" ry="12" fill="#C0EAFF" opacity="0.38"/>')
A(f'<circle cx="{FC}" cy="{FB-114}" r="5" fill="#FFFFFF" opacity="0.92"/>')
# Orbiting crystal facets
for si in range(4):
    srad=math.radians(si*90)
    sox=FC+math.cos(srad)*22; soy=FB-98+math.sin(srad)*9
    A(f'<polygon points="{sox:.0f},{soy-8:.0f} {sox+5:.0f},{soy:.0f} {sox-5:.0f},{soy:.0f}" fill="url(#gRing)" opacity="0.70"/>')
    A(f'<circle cx="{sox:.0f}" cy="{soy-4:.0f}" r="3" fill="#90D0FF" opacity="0.28"/>')
# Water jets
for jang in (-50, -22, 0, 22, 50):
    jrad=math.radians(jang-90)
    jex=FC+math.cos(jrad)*36; jey=FB-78+math.sin(jrad)*28
    A(f'<path d="M{FC},{FB-78} Q{FC+math.cos(jrad)*18:.0f},{FB-78+math.sin(jrad)*12:.0f} {jex:.0f},{jey:.0f}" '
      f'fill="none" stroke="#88D0FF" stroke-width="2.0" opacity="0.48" stroke-linecap="round"/>')
    A(f'<circle cx="{jex:.0f}" cy="{jey:.0f}" r="2" fill="#A8E0FF" opacity="0.48"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  STAGE 10 OBJECT — MAIN CRYSTARIUM GATE  (centered at SVG 200, 336)
#  Twin iron-stone towers + arch + Crystal Tower visible through gate opening
# ═══════════════════════════════════════════════════════════════════════════
# Target: node center at (200, 336). Gate spans y ≈ 278-368.
# Arch opening: peak y≈296, base y≈344. Node (200,336) is inside arch.

GX = 200; GB = 362   # gate base y (threshold/platform)

# ── threshold platform ──
A(f'<rect x="{GX-82}" y="{GB-8}" width="164" height="12" fill="url(#gSandL)" rx="2" opacity="0.92"/>')
A(f'<line x1="{GX-83}" y1="{GB-8}" x2="{GX+83}" y2="{GB-8}" stroke="#181820" stroke-width="3" opacity="0.80"/>')
# Crystal inlay
A(f'<rect x="{GX-72}" y="{GB-5}" width="144" height="3.5" fill="url(#gRing)" rx="1" opacity="0.32"/>')
# Iron bracket pins
for ti in range(8):
    A(f'<rect x="{GX-66+ti*18}" y="{GB-7}" width="10" height="4" fill="url(#gIron)" rx="1" opacity="0.52"/>')

# ── left column tower ──
CW=28; CH=128
A(f'<rect x="{GX-86}" y="{GB-8-CH}" width="{CW}" height="{CH}" fill="url(#gSandL)" rx="2" opacity="0.95"/>')
# Pilasters
for pi in range(3):
    px2=GX-86+pi*CW/2
    A(f'<rect x="{px2:.0f}" y="{GB-8-CH}" width="5" height="{CH}" fill="url(#gIron)" rx="1" opacity="0.62"/>')
# Band courses
for frac in (0.16, 0.38, 0.60, 0.82):
    by2=GB-8-CH+CH*frac
    A(f'<rect x="{GX-88}" y="{by2:.0f}" width="{CW+4}" height="5" fill="url(#gIron)" rx="1" opacity="0.68"/>')
# Crystal window
A(iron_win(GX-80, int(GB-8-CH+CH*0.32), 16, 22, 0.72))
# Capital (crenellation)
A(f'<rect x="{GX-90}" y="{GB-8-CH-10}" width="{CW+8}" height="12" fill="url(#gIron)" rx="1" opacity="0.90"/>')
A(f'<rect x="{GX-90}" y="{GB-8-CH-13}" width="{CW+8}" height="4" fill="url(#gRing)" rx="1" opacity="0.52"/>')
# Crystal spire
A(f'<polygon points="{GX-72},{GB-8-CH-34} {GX-64},{GB-8-CH-10} {GX-80},{GB-8-CH-10}" fill="url(#gRing)" opacity="0.88"/>')
A(f'<polygon points="{GX-72},{GB-8-CH-34} {GX-68},{GB-8-CH-20} {GX-76},{GB-8-CH-20}" fill="#FFFFFF" opacity="0.68"/>')
A(f'<ellipse cx="{GX-72}" cy="{GB-8-CH-22}" rx="9" ry="9" fill="#50A8F0" opacity="0.16"/>')
# Lanterns
A(lamp(GX-78, GB-10, h=20))
A(lamp(GX-100, GB-8, h=24))

# ── right column tower ──
A(f'<rect x="{GX+58}" y="{GB-8-CH}" width="{CW}" height="{CH}" fill="url(#gSandS)" rx="2" opacity="0.95"/>')
for pi in range(3):
    px2=GX+58+pi*CW/2
    A(f'<rect x="{px2:.0f}" y="{GB-8-CH}" width="5" height="{CH}" fill="url(#gIron)" rx="1" opacity="0.62"/>')
for frac in (0.16, 0.38, 0.60, 0.82):
    by2=GB-8-CH+CH*frac
    A(f'<rect x="{GX+56}" y="{by2:.0f}" width="{CW+4}" height="5" fill="url(#gIron)" rx="1" opacity="0.68"/>')
A(iron_win(GX+64, int(GB-8-CH+CH*0.32), 16, 22, 0.72))
A(f'<rect x="{GX+54}" y="{GB-8-CH-10}" width="{CW+8}" height="12" fill="url(#gIron)" rx="1" opacity="0.90"/>')
A(f'<rect x="{GX+54}" y="{GB-8-CH-13}" width="{CW+8}" height="4" fill="url(#gRing)" rx="1" opacity="0.52"/>')
A(f'<polygon points="{GX+72},{GB-8-CH-34} {GX+80},{GB-8-CH-10} {GX+64},{GB-8-CH-10}" fill="url(#gRing)" opacity="0.88"/>')
A(f'<polygon points="{GX+72},{GB-8-CH-34} {GX+76},{GB-8-CH-20} {GX+68},{GB-8-CH-20}" fill="#FFFFFF" opacity="0.68"/>')
A(f'<ellipse cx="{GX+72}" cy="{GB-8-CH-22}" rx="9" ry="9" fill="#50A8F0" opacity="0.16"/>')
A(lamp(GX+78, GB-10, h=20))
A(lamp(GX+100, GB-8, h=24))

# ── arch ──
# Arch spans from x=GX-58 to GX+58 (inside columns), peak at y=296
arch_lx=GX-58; arch_rx=GX+58
arch_bY=GB-8-CH+28    # where arch starts on column sides
arch_pY=arch_bY-52    # arch peak y

# Night sky inside arch
A(f'<path d="M{arch_lx+10},{arch_bY} C{arch_lx+10},{arch_pY+10} {arch_rx-10},{arch_pY+10} {arch_rx-10},{arch_bY} Z" '
  f'fill="#030110" opacity="0.90"/>')
# Stars through arch
for _ in range(20):
    asx=_r.uniform(arch_lx+14, arch_rx-14)
    asy=_r.uniform(arch_pY+14, arch_bY-4)
    A(f'<circle cx="{asx:.0f}" cy="{asy:.0f}" r="{_r.uniform(0.5,1.3):.1f}" fill="#FFFFFF" opacity="{_r.uniform(0.38,0.82):.2f}"/>')
# Mini Crystal Tower silhouette through arch
mt_tip=arch_pY+10
A(f'<polygon points="{GX},{mt_tip} {GX+22},{arch_bY-5} {GX-22},{arch_bY-5}" fill="url(#gTVert)" opacity="0.60"/>')
A(f'<polygon points="{GX},{mt_tip} {GX+10},{mt_tip+22} {GX-10},{mt_tip+22}" fill="#EEF8FF" opacity="0.76"/>')
A(f'<ellipse cx="{GX}" cy="{mt_tip+12}" rx="24" ry="5" fill="#80C8FF" opacity="0.38"/>')
# Aether shimmer overlay
A(f'<path d="M{arch_lx+10},{arch_bY} C{arch_lx+10},{arch_pY+10} {arch_rx-10},{arch_pY+10} {arch_rx-10},{arch_bY} Z" '
  f'fill="url(#gShimmer)" opacity="0.88"/>')
for vi in range(5):
    vx2=arch_lx+12+vi*19
    A(f'<line x1="{vx2}" y1="{arch_pY+12}" x2="{vx2}" y2="{arch_bY}" stroke="#80C8FF" stroke-width="1.0" opacity="0.18"/>')

# Arch stone body
A(f'<path d="M{arch_lx},{arch_bY} C{arch_lx},{arch_pY} {arch_rx},{arch_pY} {arch_rx},{arch_bY}" '
  f'fill="none" stroke="url(#gSandL)" stroke-width="22" stroke-linecap="butt" opacity="0.95"/>')
A(f'<path d="M{arch_lx-5},{arch_bY} C{arch_lx-5},{arch_pY-7} {arch_rx+5},{arch_pY-7} {arch_rx+5},{arch_bY}" '
  f'fill="none" stroke="url(#gIron)" stroke-width="5" stroke-linecap="butt" opacity="0.84"/>')
A(f'<path d="M{arch_lx+10},{arch_bY} C{arch_lx+10},{arch_pY+10} {arch_rx-10},{arch_pY+10} {arch_rx-10},{arch_bY}" '
  f'fill="none" stroke="url(#gRing)" stroke-width="2" stroke-linecap="butt" opacity="0.50"/>')
# Voussoir joints
for ji in range(7):
    t=(ji+1)/8.0
    bx2=(1-t)**2*arch_lx+2*(1-t)*t*GX+t**2*arch_rx
    by2=(1-t)**2*arch_bY +2*(1-t)*t*arch_pY+t**2*arch_bY
    tdx=2*(1-t)*(GX-arch_lx)+2*t*(arch_rx-GX)
    tdy=2*(1-t)*(arch_pY-arch_bY)+2*t*(arch_bY-arch_pY)
    tlen=math.hypot(tdx,tdy) or 1
    nx=-tdy/tlen*13; ny=tdx/tlen*13
    A(f'<line x1="{bx2-nx*0.3:.1f}" y1="{by2-ny*0.3:.1f}" x2="{bx2+nx:.1f}" y2="{by2+ny:.1f}" '
      f'stroke="#181820" stroke-width="1.5" opacity="0.50"/>')
# Keystone
ks_cy=arch_pY-2
A(f'<ellipse cx="{GX}" cy="{ks_cy}" rx="15" ry="11" fill="url(#gIron)" opacity="0.92"/>')
A(f'<polygon points="{GX},{ks_cy-15} {GX+8},{ks_cy+1} {GX-8},{ks_cy+1}" fill="url(#gRing)" opacity="0.90"/>')
A(f'<polygon points="{GX},{ks_cy-15} {GX+5},{ks_cy-7} {GX-5},{ks_cy-7}" fill="#FFFFFF" opacity="0.70"/>')
A(f'<ellipse cx="{GX}" cy="{ks_cy-6}" rx="8" ry="8" fill="#60B0FF" opacity="0.20"/>')
# Crystal accents at gate base
for gfx,gfs in [(GX-96,-1),(GX+96,1)]:
    A(f'<polygon points="{gfx},{GB-30} {gfx+gfs*7},{GB-6} {gfx-gfs*7},{GB-6}" fill="url(#gRing)" opacity="0.70"/>')
    A(f'<ellipse cx="{gfx}" cy="{GB-22}" rx="8" ry="12" fill="#60A8F0" opacity="0.15"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  11. STREET LANTERNS (plaza)
# ═══════════════════════════════════════════════════════════════════════════
for lx2,ly2,lh in [
    (48,438,32),(86,424,28),(124,438,30),(158,448,26),
    (352,438,32),(314,424,28),(276,438,30),(242,448,26),
    (32,518,28),(68,528,26),(106,518,28),(148,530,24),
    (368,518,28),(332,528,26),(294,518,28),(252,530,24),
]:
    A(lamp(lx2, ly2, lh))

# ═══════════════════════════════════════════════════════════════════════════
#  12. CENTRAL PATH
# ═══════════════════════════════════════════════════════════════════════════
A('<path d="M172,600 L176,540 L179,480 L182,425 L184,385 L186,355 L187,320 L188,282" '
  'fill="none" stroke="#20223A" stroke-width="28" stroke-linecap="round" opacity="0.82"/>')
A('<path d="M172,600 L176,540 L179,480 L182,425 L184,385 L186,355 L187,320 L188,282" '
  'fill="none" stroke="#303248" stroke-width="22" stroke-linecap="round" opacity="0.60"/>')
# Flagstone lines
for pjy in (292,318,348,378,408,438,468,500,538):
    A(f'<line x1="170" y1="{pjy}" x2="194" y2="{pjy}" stroke="#181828" stroke-width="1.5" opacity="0.52"/>')
# Crystal vein along path
A('<path d="M180,600 L183,540 L185,480 L186,425 L187,385 L188,355 L189,320 L189,282" '
  'fill="none" stroke="#5898D8" stroke-width="1.2" opacity="0.30"/>')

# ═══════════════════════════════════════════════════════════════════════════
#  13. ATMOSPHERE
# ═══════════════════════════════════════════════════════════════════════════
# Ground haze
A('<rect y="515" width="400" height="85" fill="url(#gHaze)" opacity="0.70"/>')

# Crystal Tower light shafts (faint blue rays from base)
for lang in (-60,-38,-20,-7,0,7,20,38,60):
    lrad=math.radians(lang-90)
    llx=T+math.cos(lrad)*500; lly=300+math.sin(lrad)*500
    lop=max(0.006, 0.052-abs(lang)*0.0004)
    lsw=max(0.4, 2.2-abs(lang)*0.028)
    A(f'<line x1="{T}" y1="300" x2="{llx:.0f}" y2="{lly:.0f}" '
      f'stroke="#78B8FF" stroke-width="{lsw:.1f}" opacity="{lop:.3f}"/>')

# Crystal dust motes
for mx,my,mc,mop in [
    (50,182,'#90C8FF',0.62),(95,168,'#C0E0FF',0.55),
    (148,152,'#80B8F0',0.58),(182,175,'#A0D0FF',0.50),
    (222,160,'#C0E0FF',0.55),(268,148,'#80C0FF',0.58),
    (315,168,'#90C8FF',0.54),(352,155,'#A0D0FF',0.58),
    (40,238,'#80B8F0',0.46),(125,228,'#C0E0FF',0.50),
    (282,232,'#90C8FF',0.50),(360,222,'#80C0FF',0.46),
]:
    A(f'<ellipse cx="{mx}" cy="{my}" rx="1.8" ry="1.1" fill="{mc}" opacity="{mop}"/>')
    A(f'<ellipse cx="{mx}" cy="{my}" rx="5.5" ry="3.5" fill="{mc}" opacity="{mop*0.08:.2f}"/>')

# Vignette
A('<rect width="400" height="600" fill="url(#gVig)"/>')
A('</svg>')

# ═══════════════════════════════════════════════════════════════════════════
#  VALIDATE + INJECT
# ═══════════════════════════════════════════════════════════════════════════
svg = ''.join(parts)
print(f'ULTIMATE SVG: {len(svg):,} chars')

ro=len(_re.findall(r'<radialGradient', svg)); rc=len(_re.findall(r'</radialGradient', svg))
lo=len(_re.findall(r'<linearGradient', svg)); lc=len(_re.findall(r'</linearGradient', svg))
print(f'  radialGradient: {ro}/{rc}  linearGradient: {lo}/{lc}')
if ro!=rc: raise RuntimeError(f'radialGradient mismatch: {ro}/{rc}')
if lo!=lc: raise RuntimeError(f'linearGradient mismatch: {lo}/{lc}')

if svg.count('`'): raise RuntimeError('Backtick in SVG!')
if svg.count("'"): raise RuntimeError("Single quote in SVG!")

import xml.etree.ElementTree as ET
try:
    ET.fromstring(svg)
    print('  XML parse: OK')
except ET.ParseError as e:
    raise RuntimeError(f'XML parse error: {e}')

html2 = html
for old, new in [
    ('#game-view[data-diff="ULTIMATE"] { background: rgb(3,1,15); }',
     '#game-view[data-diff="ULTIMATE"] { background: rgb(2,1,10); }'),
    ('.map-scroll[data-diff="ULTIMATE"] { background: #03010F; }',
     '.map-scroll[data-diff="ULTIMATE"] { background: #020108; }'),
]:
    if old in html2:
        html2=html2.replace(old,new); print(f'  CSS: {old[:55]}')

pattern = r"(if\(diff===.ULTIMATE.\) return \`)(.*?)(\`;)"
repl    = lambda m: m.group(1) + svg + m.group(3)
new_html, n = _re.subn(pattern, repl, html2, flags=_re.DOTALL)
if n==0: raise RuntimeError("ULTIMATE pattern not found!")

with open('/Users/hirokazukataoka/subitze/stage.html','w',encoding='utf-8') as f:
    f.write(new_html)
print(f'stage.html written. ({n} replacement)')
