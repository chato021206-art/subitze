#!/usr/bin/env python3
"""gen_ultimate.py — ULTIMATE: The Crystarium (FF14 Shadowbringers) — complete rebuild
Quality-first, accurate to in-game visuals.

Key references:
  Sky   : near-black indigo zenith → dense stars (restored night, The First)
  Tower : "gleaming spear of crystal" — luminous pale blue-white, faceted,
          reflective, ring-banded, dominates entire composition
  Arch. : sandstone/tan stone + wrought black iron + crystal panel inlays
          ecletic melting-pot (Lominsan/Ul'dahn/Ishgardian refugee styles)
  Rotunda: "elegant black iron and sheets of shimmering crystal" — domed,
            iron-ribbed, first landmark visitors encounter
  Forest : Lakeland's vibrant purple forest on all horizons
  Lights : warm amber lanterns (added when night first returned in 100 yrs)
  Stage 5 : The Exedra — grand crystal fountain, iconic gathering plaza
  Stage 10: Main Crystarium gate — iron+stone twin towers, tower behind arch
"""
import re as _re, math
import random as _rand
_rnd = _rand.Random(137)

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    html = f.read()

parts = []
def A(s): parts.append(s)

# ═════════════════════════════════════════════════════════════════════════════
#  HELPER FUNCTIONS
# ═════════════════════════════════════════════════════════════════════════════

def sparkle(sx, sy, r=1.2, op=0.90, col='#FFFFFF', glow_col='#B0D0FF'):
    """Star with optional 4-point sparkle cross."""
    out = f'<circle cx="{sx}" cy="{sy}" r="{r}" fill="{col}" opacity="{op}"/>'
    if r > 1.6:
        out += (f'<circle cx="{sx}" cy="{sy}" r="{r*2.5:.1f}" fill="{glow_col}" opacity="{op*0.15:.2f}"/>')
        for ang in [0, 90, 180, 270]:
            rad = math.radians(ang)
            ex = sx + math.cos(rad)*r*4; ey = sy + math.sin(rad)*r*4
            out += (f'<line x1="{sx}" y1="{sy}" x2="{ex:.1f}" y2="{ey:.1f}" '
                    f'stroke="{col}" stroke-width="0.6" opacity="{op*0.45:.2f}"/>')
    return out

def crystal_shard(cx, cy, w, h, angle=0, col='#B8DCFF', op=0.78):
    """Floating crystal shard — elongated hexagonal."""
    hw = w/2; hh = h/2
    pts = (f'{cx:.1f},{cy-hh:.1f} {cx+hw:.1f},{cy-hh*0.25:.1f} '
           f'{cx+hw*0.65:.1f},{cy+hh:.1f} {cx-hw*0.65:.1f},{cy+hh:.1f} '
           f'{cx-hw:.1f},{cy-hh*0.25:.1f}')
    out  = (f'<polygon points="{pts}" fill="{col}" opacity="{op}" '
            f'transform="rotate({angle},{cx:.1f},{cy:.1f})"/>')
    # Inner highlight streak
    ang_r = math.radians(angle - 90)
    hx1 = cx + math.cos(ang_r - 0.3)*hw*0.25; hy1 = cy + math.sin(ang_r - 0.3)*hh*0.75
    hx2 = cx + math.cos(ang_r)*hw*0.10;       hy2 = cy + math.sin(ang_r)*hh*0.35
    out += (f'<line x1="{hx1:.1f}" y1="{hy1:.1f}" x2="{hx2:.1f}" y2="{hy2:.1f}" '
            f'stroke="#FFFFFF" stroke-width="1.8" opacity="{op*0.60:.2f}" '
            f'transform="rotate({angle},{cx:.1f},{cy:.1f})"/>')
    # Soft glow
    out += (f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{w:.0f}" ry="{h*0.5:.0f}" '
            f'fill="{col}" opacity="{op*0.12:.2f}"/>')
    return out

def lantern_post(lx, ly, h=30, lamp_w=9, lamp_h=12):
    """Warm amber lantern on iron post."""
    out = []
    # Post (black iron)
    out.append(f'<line x1="{lx}" y1="{ly}" x2="{lx}" y2="{ly-h}" '
               f'stroke="#1C1A28" stroke-width="3"/>')
    # Arm bracket
    out.append(f'<line x1="{lx}" y1="{ly-h+8}" x2="{lx+6}" y2="{ly-h+2}" '
               f'stroke="#1C1A28" stroke-width="2"/>')
    # Lantern cage (black iron)
    lox = lx - lamp_w//2; loy = ly - h - lamp_h
    out.append(f'<rect x="{lox}" y="{loy}" width="{lamp_w}" height="{lamp_h}" '
               f'fill="#18181E" rx="1" opacity="0.95"/>')
    # Glass panels (warm amber)
    out.append(f'<rect x="{lox+1}" y="{loy+1}" width="{lamp_w-2}" height="{lamp_h-3}" '
               f'fill="#FFC030" rx="1" opacity="0.88"/>')
    out.append(f'<rect x="{lox+2}" y="{loy+2}" width="{lamp_w//2}" height="{lamp_h//2}" '
               f'fill="#FFE080" opacity="0.55"/>')
    # Glow halos
    gcx = lx; gcy = ly - h - lamp_h//2
    out.append(f'<ellipse cx="{gcx}" cy="{gcy}" rx="{lamp_w*1.8:.0f}" ry="{lamp_h*1.4:.0f}" '
               f'fill="#FFB020" opacity="0.22"/>')
    out.append(f'<ellipse cx="{gcx}" cy="{gcy}" rx="{lamp_w*3.5:.0f}" ry="{lamp_h*2.8:.0f}" '
               f'fill="#FF8800" opacity="0.08"/>')
    # Cap
    out.append(f'<rect x="{lox-2}" y="{loy-3}" width="{lamp_w+4}" height="4" '
               f'fill="#18181E" rx="1"/>')
    # Base finial
    out.append(f'<circle cx="{lx}" cy="{ly-h}" r="3" fill="#18181E"/>')
    return ''.join(out)

def iron_window(wx, wy, ww, wh, glow_op=0.65):
    """Black iron window frame with crystal-blue glow inside."""
    out = []
    # Dark recess
    out.append(f'<rect x="{wx:.0f}" y="{wy:.0f}" width="{ww:.0f}" height="{wh:.0f}" '
               f'fill="#0C1020" rx="{ww*0.42:.0f}" opacity="0.92"/>')
    # Crystal blue fill
    out.append(f'<rect x="{wx+1.5:.0f}" y="{wy+1.5:.0f}" width="{ww-3:.0f}" height="{wh-3:.0f}" '
               f'fill="#5AB0F0" rx="{ww*0.38:.0f}" opacity="{glow_op:.2f}"/>')
    # Inner bright highlight
    out.append(f'<ellipse cx="{wx+ww*0.38:.0f}" cy="{wy+wh*0.30:.0f}" '
               f'rx="{ww*0.25:.0f}" ry="{wh*0.22:.0f}" fill="#A0D8FF" opacity="0.45"/>')
    # Iron frame
    out.append(f'<rect x="{wx:.0f}" y="{wy:.0f}" width="{ww:.0f}" height="{wh:.0f}" '
               f'fill="none" stroke="#18181E" stroke-width="2.0" rx="{ww*0.42:.0f}" opacity="0.88"/>')
    # Glow halo outside
    out.append(f'<ellipse cx="{wx+ww/2:.0f}" cy="{wy+wh/2:.0f}" '
               f'rx="{ww*0.80:.0f}" ry="{wh*0.80:.0f}" fill="#3880D0" opacity="0.12"/>')
    return ''.join(out)

def iron_divider(x1, y1, x2, y2, sw=2.5, op=0.82):
    """Black iron structural divider / trim."""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="#18181E" stroke-width="{sw}" opacity="{op}"/>')

# ═════════════════════════════════════════════════════════════════════════════
#  GRADIENTS & DEFS
# ═════════════════════════════════════════════════════════════════════════════
A('<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"><defs>')

# ── Sky ──────────────────────────────────────────────────────────────────────
A('<linearGradient id="gSky" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#03010F"/>'   # near-black zenith
  '<stop offset="14%"  stop-color="#070420"/>'   # deep indigo
  '<stop offset="30%"  stop-color="#0C0830"/>'   # rich purple-blue
  '<stop offset="52%"  stop-color="#130E48"/>'   # indigo
  '<stop offset="72%"  stop-color="#1A1558"/>'   # purple-indigo horizon
  '<stop offset="88%"  stop-color="#201B6A"/>'   # near-horizon slight blue
  '<stop offset="100%" stop-color="#251E78"/>'   # brightest horizon
  '</linearGradient>')

# ── Crystal Tower ────────────────────────────────────────────────────────────
# Main tower glow (massive radial, blue-white, spreads across whole scene)
A('<radialGradient id="gTowerGlow" cx="50%" cy="28%" r="68%">'
  '<stop offset="0%"   stop-color="#D8F0FF" stop-opacity="0.92"/>'
  '<stop offset="10%"  stop-color="#A8D8FF" stop-opacity="0.68"/>'
  '<stop offset="26%"  stop-color="#70B0FF" stop-opacity="0.38"/>'
  '<stop offset="48%"  stop-color="#4080E0" stop-opacity="0.14"/>'
  '<stop offset="70%"  stop-color="#2050A0" stop-opacity="0.04"/>'
  '<stop offset="100%" stop-color="#102060" stop-opacity="0"/>'
  '</radialGradient>')

# Tower body — lit face (ice-white with blue depth)
A('<linearGradient id="gTowerFace" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#90C8F8"/>'
  '<stop offset="20%"  stop-color="#C8E8FF"/>'
  '<stop offset="42%"  stop-color="#F8FDFF"/>'
  '<stop offset="62%"  stop-color="#E0F2FF"/>'
  '<stop offset="82%"  stop-color="#B0D8F8"/>'
  '<stop offset="100%" stop-color="#78B0E8"/>'
  '</linearGradient>')

# Tower vertical gradient (bright tip → deeper base)
A('<linearGradient id="gTowerVert" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FFFFFF"/>'
  '<stop offset="18%"  stop-color="#ECF8FF"/>'
  '<stop offset="42%"  stop-color="#C8E4FF"/>'
  '<stop offset="68%"  stop-color="#90C0F0"/>'
  '<stop offset="88%"  stop-color="#6098D8"/>'
  '<stop offset="100%" stop-color="#4878C0"/>'
  '</linearGradient>')

# Crystal ring bands on tower
A('<linearGradient id="gRing" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FFFFFF"/>'
  '<stop offset="30%"  stop-color="#C0E8FF"/>'
  '<stop offset="70%"  stop-color="#80C0F8"/>'
  '<stop offset="100%" stop-color="#50A0E8"/>'
  '</linearGradient>')

# Tower base horizon glow
A('<radialGradient id="gBaseGlow" cx="50%" cy="78%" r="52%">'
  '<stop offset="0%"   stop-color="#90C8FF" stop-opacity="0.55"/>'
  '<stop offset="35%"  stop-color="#5898E8" stop-opacity="0.22"/>'
  '<stop offset="68%"  stop-color="#2858A8" stop-opacity="0.06"/>'
  '<stop offset="100%" stop-color="#102040" stop-opacity="0"/>'
  '</radialGradient>')

# ── Architecture ─────────────────────────────────────────────────────────────
# Sandstone — lit side (warm tan-beige, The First crystal tower tinges blue)
A('<linearGradient id="gSandLit" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#C8B888"/>'
  '<stop offset="32%"  stop-color="#B8A878"/>'
  '<stop offset="65%"  stop-color="#A09060"/>'
  '<stop offset="100%" stop-color="#887848"/>'
  '</linearGradient>')

# Sandstone — shadow side (slightly cooler from tower glow)
A('<linearGradient id="gSandSh" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#A8A898"/>'
  '<stop offset="40%"  stop-color="#989080"/>'
  '<stop offset="100%" stop-color="#807868"/>'
  '</linearGradient>')

# Black iron (structural framing, Rotunda skeleton, window frames, trim)
A('<linearGradient id="gIron" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#2E2C3C"/>'
  '<stop offset="50%"  stop-color="#1E1C2A"/>'
  '<stop offset="100%" stop-color="#141220"/>'
  '</linearGradient>')

# Crystal panel (Rotunda dome panels, windows — shimmering with tower glow)
A('<linearGradient id="gCrystalPanel" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#FFFFFF" stop-opacity="0.90"/>'
  '<stop offset="22%"  stop-color="#C8EAFF" stop-opacity="0.80"/>'
  '<stop offset="55%"  stop-color="#78B8F0" stop-opacity="0.65"/>'
  '<stop offset="100%" stop-color="#4088D0" stop-opacity="0.50"/>'
  '</linearGradient>')

# Ground — dark stone plaza (blue-tinted from tower glow)
A('<linearGradient id="gGround" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#252838"/>'
  '<stop offset="30%"  stop-color="#1E2030"/>'
  '<stop offset="65%"  stop-color="#161828"/>'
  '<stop offset="100%" stop-color="#0E1020"/>'
  '</linearGradient>')

# Lakeland purple forest (Lakeland's vibrant purple vegetation)
A('<linearGradient id="gForest" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#4A2090" stop-opacity="0.55"/>'
  '<stop offset="45%"  stop-color="#351860" stop-opacity="0.78"/>'
  '<stop offset="100%" stop-color="#200C40" stop-opacity="0.90"/>'
  '</linearGradient>')

# Fountain water (crystal blue-teal)
A('<radialGradient id="gFountain" cx="50%" cy="35%" r="60%">'
  '<stop offset="0%"   stop-color="#B0E0FF" stop-opacity="0.95"/>'
  '<stop offset="40%"  stop-color="#60B8F0" stop-opacity="0.82"/>'
  '<stop offset="100%" stop-color="#2878C0" stop-opacity="0.72"/>'
  '</radialGradient>')

# Creation orb (fountain crystal centerpiece glow)
A('<radialGradient id="gCrystalOrb" cx="38%" cy="28%" r="65%">'
  '<stop offset="0%"   stop-color="#FFFFFF" stop-opacity="1.00"/>'
  '<stop offset="22%"  stop-color="#D0EEFF" stop-opacity="0.95"/>'
  '<stop offset="50%"  stop-color="#80C8FF" stop-opacity="0.88"/>'
  '<stop offset="80%"  stop-color="#3888E0" stop-opacity="0.90"/>'
  '<stop offset="100%" stop-color="#1858B0" stop-opacity="0.95"/>'
  '</radialGradient>')

# Gate aether shimmer (Crystal Tower energy visible through arch)
A('<linearGradient id="gGateShimmer" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#80C8FF" stop-opacity="0.08"/>'
  '<stop offset="28%"  stop-color="#60B0FF" stop-opacity="0.32"/>'
  '<stop offset="52%"  stop-color="#50A8FF" stop-opacity="0.45"/>'
  '<stop offset="76%"  stop-color="#60B0FF" stop-opacity="0.28"/>'
  '<stop offset="100%" stop-color="#80C8FF" stop-opacity="0.06"/>'
  '</linearGradient>')

# Bottom depth haze
A('<linearGradient id="gHaze" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#0E1020" stop-opacity="0"/>'
  '<stop offset="48%"  stop-color="#0A0C18" stop-opacity="0.32"/>'
  '<stop offset="100%" stop-color="#060810" stop-opacity="0.75"/>'
  '</linearGradient>')

# Edge vignette
A('<radialGradient id="gVig" cx="50%" cy="15%" r="92%">'
  '<stop offset="50%"  stop-color="#000000" stop-opacity="0"/>'
  '<stop offset="100%" stop-color="#020108" stop-opacity="0.72"/>'
  '</radialGradient>')

# Crystal pillar
A('<linearGradient id="gPillar" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#2A2838"/>'
  '<stop offset="35%"  stop-color="#353448"/>'
  '<stop offset="65%"  stop-color="#2A2838"/>'
  '<stop offset="100%" stop-color="#1E1C28"/>'
  '</linearGradient>')

A('</defs>')

# ═════════════════════════════════════════════════════════════════════════════
#  1. NIGHT SKY
# ═════════════════════════════════════════════════════════════════════════════
A('<rect width="400" height="600" fill="url(#gSky)"/>')

# ═════════════════════════════════════════════════════════════════════════════
#  2. STARS — dense field (restored for first time in 100 years)
# ═════════════════════════════════════════════════════════════════════════════
# Background micro-stars (tiny, dense)
for _ in range(260):
    sx = _rnd.uniform(0, 400); sy = _rnd.uniform(0, 280)
    sr = _rnd.uniform(0.45, 1.35); sop = _rnd.uniform(0.40, 0.88)
    # slight color variation: pure white, cool blue-white, warm white
    sc = _rnd.choice(['#FFFFFF','#FFFFFF','#E8F0FF','#F0F8FF','#FFF8F0'])
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr:.1f}" fill="{sc}" opacity="{sop:.2f}"/>')

# Mid-size stars with halos
for _ in range(55):
    sx = _rnd.uniform(0, 400); sy = _rnd.uniform(0, 270)
    sr = _rnd.uniform(1.3, 2.0); sop = _rnd.uniform(0.65, 0.92)
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr:.1f}" fill="#FFFFFF" opacity="{sop:.2f}"/>')
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr*2.8:.1f}" fill="#B8D0FF" opacity="{sop*0.10:.2f}"/>')

# Bright sparkle stars with cross-flare
bright = [(28,22,2.2,0.98),(355,18,2.4,0.97),(82,45,1.9,0.94),
          (185,14,2.6,0.99),(295,38,2.1,0.96),(138,28,1.8,0.92),
          (322,55,2.0,0.95),(52,68,1.7,0.90),(248,24,2.3,0.97),
          (390,42,1.8,0.92),(168,58,1.9,0.91),(310,18,2.0,0.95)]
for bsx, bsy, bsr, bsop in bright:
    A(sparkle(bsx, bsy, bsr, bsop, '#FFFFFF', '#B0D0FF'))

# ═════════════════════════════════════════════════════════════════════════════
#  3. CRYSTAL TOWER — "a gleaming spear of crystal pointed at the heavens"
#     Luminous pale blue-white, faceted, reflective, completely dominant
# ═════════════════════════════════════════════════════════════════════════════
# Massive glow radiating across scene
A('<rect width="400" height="600" fill="url(#gTowerGlow)"/>')
A('<rect width="400" height="600" fill="url(#gBaseGlow)"/>')

T = 200  # tower center x
# Tower geometry: tip→base widths at various y-levels
# y=0 → tip (single point)
# y=28 → 18px wide
# y=80 → 44px wide
# y=160 → 62px wide
# y=245 → 76px wide
# y=280 → 90px (base skirt flare)

# Far secondary spires (background, behind main tower — multi-spired look)
for sp_off, sp_w, sp_h in [(-28, 8, 210), (28, 8, 200), (-50, 6, 160), (50, 6, 150)]:
    sp_cx = T + sp_off
    A(f'<polygon points="{sp_cx},{8:.0f} {sp_cx+sp_w},{8+sp_h*0.3:.0f} '
      f'{sp_cx+sp_w*0.7},{8+sp_h:.0f} {sp_cx-sp_w*0.7},{8+sp_h:.0f} {sp_cx-sp_w},{8+sp_h*0.3:.0f}" '
      f'fill="url(#gTowerFace)" opacity="0.38"/>')

# Main tower shaft (main polygon, full height)
A(f'<polygon points="{T},1 {T+20},30 {T+30},80 {T+36},160 {T+40},245 '
  f'{T+46},282 {T},288 {T-46},282 {T-40},245 {T-36},160 {T-30},80 {T-20},30" '
  f'fill="url(#gTowerVert)" opacity="0.92"/>')

# Left face panel (slightly darker — side lighting)
A(f'<polygon points="{T-20},30 {T-36},160 {T-40},245 {T-46},282 {T},288 {T},30" '
  f'fill="#80B8E8" opacity="0.28"/>')
# Right face panel
A(f'<polygon points="{T+20},30 {T+36},160 {T+40},245 {T+46},282 {T},288 {T},30" '
  f'fill="#C8E8FF" opacity="0.18"/>')

# Vertical highlight streaks (faceted crystal surface)
for vx_off, vw, vop in [
    (0, 5, 0.88),(-7, 2.5, 0.62),(9, 2.5, 0.58),(-18, 1.5, 0.32),(20, 1.5, 0.30)
]:
    A(f'<rect x="{T+vx_off-vw/2:.1f}" y="1" width="{vw}" height="288" '
      f'fill="#FFFFFF" opacity="{vop}" rx="1"/>')

# Tower tip — brilliant white needle
A(f'<polygon points="{T},1 {T+12},32 {T-12},32" fill="#FFFFFF" opacity="0.98"/>')
A(f'<polygon points="{T},1 {T+7},22 {T-7},22" fill="#FFFFFF" opacity="0.80"/>')
# Tip glow burst
A(f'<circle cx="{T}" cy="5" r="10" fill="#FFFFFF" opacity="0.40"/>')
A(f'<circle cx="{T}" cy="5" r="22" fill="#C0E8FF" opacity="0.18"/>')
A(f'<circle cx="{T}" cy="5" r="40" fill="#90C8FF" opacity="0.07"/>')

# Crystal ring bands (horizontal, at regular intervals — iconic Crystal Tower look)
rings = [(40,  7,  0.88), (90,  6,  0.80), (145, 5.5,0.74),
         (198, 5,  0.68), (245, 4.5,0.62), (278, 4,  0.55)]
for ry, rh, rop in rings:
    # Width at that y-level (linear interpolation)
    frac = ry / 288
    rw = 18 + frac * 28   # half-width
    A(f'<rect x="{T-rw-4:.0f}" y="{ry}" width="{(rw+4)*2:.0f}" height="{rh}" '
      f'fill="url(#gRing)" rx="2" opacity="{rop:.2f}"/>')
    # Ring edge glow
    A(f'<ellipse cx="{T}" cy="{ry+rh/2:.1f}" rx="{rw+18:.0f}" ry="{rh+4:.0f}" '
      f'fill="#78B8FF" opacity="{rop*0.22:.2f}"/>')

# Tower base — flared crystal skirt merging into city platform
A(f'<polygon points="{T-46},282 {T-90},302 {T-92},312 {T},318 '
  f'{T+92},312 {T+90},302 {T+46},282" '
  f'fill="url(#gTowerVert)" opacity="0.65"/>')
# Base glow
A(f'<ellipse cx="{T}" cy="308" rx="95" ry="22" fill="#B8E0FF" opacity="0.55"/>')
A(f'<ellipse cx="{T}" cy="308" rx="72" ry="14" fill="#D8F0FF" opacity="0.72"/>')
A(f'<ellipse cx="{T}" cy="308" rx="44" ry="8" fill="#FFFFFF" opacity="0.85"/>')

# ═════════════════════════════════════════════════════════════════════════════
#  4. FLOATING CRYSTAL SHARDS (drifting around the tower in the night air)
# ═════════════════════════════════════════════════════════════════════════════
shards = [
    # cx, cy, w, h, angle, col, op
    (52,  110, 14, 36, -22, '#A8D0FF', 0.78),
    (75,  145, 9,  22, 18,  '#C8E8FF', 0.70),
    (42,  80,  7,  18, -38, '#D0EEFF', 0.65),
    (62,  178, 6,  16, 28,  '#B8DCFF', 0.60),
    (88,  132, 11, 26, -12, '#C0E4FF', 0.72),
    (340, 118, 15, 38, 24,  '#A0CCFF', 0.76),
    (362, 90,  9,  24, -18, '#C8E8FF', 0.68),
    (320, 152, 8,  20, 35,  '#B8DCFF', 0.62),
    (348, 180, 6,  15, -28, '#D0EEFF', 0.58),
    (310, 96,  12, 28, 15,  '#B0D8FF', 0.70),
    (138, 58,  10, 25, -8,  '#C0E0FF', 0.65),
    (258, 64,  11, 28, 20,  '#B8DCFF', 0.67),
    (112, 88,  7,  16, 44,  '#D8EEFF', 0.55),
    (288, 82,  8,  18, -30, '#C8E4FF', 0.60),
    (158, 44,  9,  20, -5,  '#A8D4FF', 0.62),
    (240, 48,  8,  19, 14,  '#C0E0FF', 0.60),
    (105, 168, 6,  14, -20, '#D0ECFF', 0.52),
    (295, 170, 7,  16, 25,  '#C8E4FF', 0.54),
]
for scx,scy,sw,sh,sang,scol,sop in shards:
    A(crystal_shard(scx, scy, sw, sh, sang, scol, sop))

# ═════════════════════════════════════════════════════════════════════════════
#  5. LAKELAND PURPLE FORESTS (vibrant purple vegetation on all horizons)
# ═════════════════════════════════════════════════════════════════════════════
# Left forest — undulating canopy silhouette
A('<path d="M0,275 Q10,252 24,262 Q36,242 52,258 Q66,236 84,254 '
  'Q98,230 116,248 Q130,235 148,252 L148,290 L0,290 Z" '
  'fill="#3C1870" opacity="0.80"/>')
A('<path d="M0,280 Q14,260 30,270 Q48,250 68,265 Q84,246 102,260 '
  'Q118,250 136,264 L136,290 L0,290 Z" '
  'fill="#2A1050" opacity="0.60"/>')
# Left canopy bumps (detailed tree crowns)
lt = [(16,258,11),(36,248,13),(58,244,12),(78,248,14),(100,240,12),(120,246,11),(140,252,10)]
for tx,ty,tr in lt:
    A(f'<ellipse cx="{tx}" cy="{ty}" rx="{tr}" ry="{int(tr*0.72)}" fill="#4A2090" opacity="0.88"/>')
    A(f'<ellipse cx="{tx-2}" cy="{ty-3}" rx="{int(tr*0.55)}" ry="{int(tr*0.42)}" fill="#5C28A8" opacity="0.65"/>')
# Tiny distant trees (lighter, higher up — atmospheric)
for tx,ty,tr in [(8,272,6),(28,270,7),(50,268,6),(72,265,7),(95,262,6),(115,264,7),(138,266,5)]:
    A(f'<ellipse cx="{tx}" cy="{ty}" rx="{tr}" ry="{int(tr*0.60)}" fill="#5030A0" opacity="0.48"/>')

# Right forest
A('<path d="M252,290 L252,252 Q268,235 286,250 Q300,232 320,248 '
  'Q336,234 354,252 Q368,240 386,256 Q396,250 400,258 L400,290 Z" '
  'fill="#3C1870" opacity="0.80"/>')
A('<path d="M264,290 L264,264 Q280,248 298,262 Q316,248 336,264 '
  'Q354,252 374,268 L400,268 L400,290 Z" '
  'fill="#2A1050" opacity="0.60"/>')
rt = [(262,252,11),(282,244,13),(304,238,12),(324,244,14),(346,240,12),(366,248,11),(386,254,10)]
for tx,ty,tr in rt:
    A(f'<ellipse cx="{tx}" cy="{ty}" rx="{tr}" ry="{int(tr*0.72)}" fill="#4A2090" opacity="0.88"/>')
    A(f'<ellipse cx="{tx+2}" cy="{ty-3}" rx="{int(tr*0.55)}" ry="{int(tr*0.42)}" fill="#5C28A8" opacity="0.65"/>')
for tx,ty,tr in [(270,270,6),(290,266,7),(312,262,6),(334,264,7),(356,262,6),(378,268,6),(396,270,5)]:
    A(f'<ellipse cx="{tx}" cy="{ty}" rx="{tr}" ry="{int(tr*0.60)}" fill="#5030A0" opacity="0.48"/>')

# ═════════════════════════════════════════════════════════════════════════════
#  6. DISTANT CITY SKYLINE (sandstone buildings behind left/right towers)
# ═════════════════════════════════════════════════════════════════════════════
# Skyline — sandstone silhouette
A('<path d="M0,258 L0,278 L18,278 L18,262 L28,262 L28,272 L40,272 '
  'L40,255 L52,255 L52,268 L62,268 L62,258 L72,258 L72,265 '
  'L80,265 L80,255 L92,255 L92,265 L102,265 L102,258 L112,258 '
  'L112,268 L122,268 L122,258" '
  'fill="url(#gSandSh)" opacity="0.72"/>')
A('<path d="M278,258 L278,268 L288,268 L288,258 L298,258 L298,265 '
  'L308,265 L308,255 L318,255 L318,265 L328,265 L328,255 L340,255 '
  'L340,268 L350,268 L350,258 L362,258 L362,272 L372,272 '
  'L372,262 L382,262 L382,278 L400,278 L400,258" '
  'fill="url(#gSandSh)" opacity="0.72"/>')
# Amber-lit windows on distant buildings
for wx,wy in [(24,263),(48,260),(68,262),(86,259),(98,262),
              (290,260),(312,259),(330,260),(352,263),(370,265)]:
    A(f'<rect x="{wx}" y="{wy}" width="5" height="4" fill="#FFC030" rx="1" opacity="0.65"/>')
    A(f'<ellipse cx="{wx+2}" cy="{wy+2}" rx="5" ry="4" fill="#FF9010" opacity="0.10"/>')
# Black iron roofline trims
A('<line x1="0" y1="258" x2="122" y2="258" stroke="#18181E" stroke-width="2" opacity="0.75"/>')
A('<line x1="278" y1="258" x2="400" y2="258" stroke="#18181E" stroke-width="2" opacity="0.75"/>')

# ═════════════════════════════════════════════════════════════════════════════
#  7. LEFT & RIGHT CRYSTARIUM BUILDING COMPLEXES
#     Sandstone body, black iron framing, crystal windows, eclectic styles
# ═════════════════════════════════════════════════════════════════════════════
def crystarium_wing(bx, by, bw, bh, side='L', sub_w=60, sub_h=170, sub_dx=0):
    """Full Crystarium building wing: main block + secondary + iron trim."""
    out = []
    grad = 'gSandLit' if side == 'L' else 'gSandSh'
    sg   = 'gSandSh'  if side == 'L' else 'gSandLit'

    # Secondary building (behind/beside)
    sbx = bx + sub_dx
    out.append(f'<rect x="{sbx}" y="{by+bh-sub_h}" width="{sub_w}" height="{sub_h}" '
               f'fill="url(#{sg})" rx="2" opacity="0.88"/>')
    # Sub-building black iron roofline
    out.append(iron_divider(sbx-1, by+bh-sub_h, sbx+sub_w+1, by+bh-sub_h, 3.0, 0.80))

    # Main building body
    out.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" '
               f'fill="url(#{grad})" rx="2" opacity="0.95"/>')

    # Black iron heavy vertical pilaster strips (Ishgardian Gothic influence)
    pilw = 5
    n_pil = max(2, int(bw // 22))
    for pi in range(n_pil + 1):
        px2 = bx + pi * (bw / n_pil)
        out.append(f'<rect x="{px2-pilw/2:.0f}" y="{by}" width="{pilw}" height="{bh}" '
                   f'fill="url(#gIron)" rx="1" opacity="0.72"/>')

    # Black iron horizontal band courses
    for band_frac in [0.0, 0.22, 0.44, 0.66, 0.88]:
        band_y = by + bh * band_frac
        out.append(f'<rect x="{bx-2}" y="{band_y:.0f}" width="{bw+4}" height="4.5" '
                   f'fill="url(#gIron)" rx="1" opacity="0.68"/>')

    # Crystal-glow windows (3 rows)
    ww = bw * 0.26; wh = bh * 0.12
    for row in range(3):
        wy2 = by + bh * (0.16 + row * 0.26)
        wx2 = bx + (bw - ww) * 0.50
        out.append(iron_window(wx2, wy2, ww, wh, 0.65))

    # Crenellated parapet (Ishgardian gothic roofline)
    merlon_w = 6; merlon_h = 10; gap = 4
    mx = bx + 4
    while mx < bx + bw - merlon_w:
        out.append(f'<rect x="{mx:.0f}" y="{by-merlon_h}" width="{merlon_w}" '
                   f'height="{merlon_h+2}" fill="url(#gIron)" rx="1" opacity="0.82"/>')
        mx += merlon_w + gap

    # Small crystal spire turrets at corners
    for tx2 in [bx + 8, bx + bw - 8]:
        out.append(f'<polygon points="{tx2},{by-merlon_h-16} {tx2+5},{by-merlon_h} {tx2-5},{by-merlon_h}" '
                   f'fill="url(#gRing)" opacity="0.80"/>')
        out.append(f'<ellipse cx="{tx2}" cy="{by-merlon_h-10}" rx="6" ry="6" '
                   f'fill="#50A8F0" opacity="0.15"/>')

    return ''.join(out)

# Left complex
A(crystarium_wing(bx=-12, by=165, bw=102, bh=235, side='L', sub_w=68, sub_h=180, sub_dx=8))
# Right complex (mirrored)
A(crystarium_wing(bx=310, by=165, bw=102, bh=235, side='R', sub_w=68, sub_h=180, sub_dx=22))

# Amber lanterns on building walls
for lx2, ly2 in [(22,240),(22,300),(22,360),(378,240),(378,300),(378,360)]:
    A(lantern_post(lx2, ly2, h=20, lamp_w=8, lamp_h=10))

# ═════════════════════════════════════════════════════════════════════════════
#  8. THE ROTUNDA — "elegant black iron and sheets of shimmering crystal"
#     The first landmark visitors see. Domed, grand, iron-ribbed crystal dome.
#     Located centrally where the Crystal Tower base meets the city.
# ═════════════════════════════════════════════════════════════════════════════
rot_cx = 200; rot_base = 368

# Grand sandstone staircase leading up to Rotunda (3 wide steps)
for step_i, (sw2, sh2) in enumerate([(130,10),(108,8),(86,7)]):
    sy2 = rot_base - step_i * 8
    A(f'<rect x="{rot_cx-sw2//2}" y="{sy2-sh2}" width="{sw2}" height="{sh2}" '
      f'fill="url(#gSandLit)" rx="2" opacity="0.88"/>')
    A(iron_divider(rot_cx-sw2//2-1, sy2-sh2, rot_cx+sw2//2+1, sy2-sh2, 2.5, 0.72))

# Drum platform base (sandstone with iron banding)
drum_base_y = rot_base - 30; drum_h = 58; drum_r = 52
A(f'<rect x="{rot_cx-drum_r}" y="{drum_base_y-drum_h}" width="{drum_r*2}" height="{drum_h}" '
  f'fill="url(#gSandLit)" rx="3" opacity="0.94"/>')
# Iron pilaster strips on drum (6 facing)
for pi in range(7):
    px2 = rot_cx - drum_r + pi * (drum_r * 2 / 6)
    A(f'<rect x="{px2-3:.0f}" y="{drum_base_y-drum_h}" width="6" height="{drum_h}" '
      f'fill="url(#gIron)" rx="1" opacity="0.78"/>')
# Iron entablature (bold horizontal divide)
A(f'<rect x="{rot_cx-drum_r-3}" y="{drum_base_y-drum_h-8}" width="{drum_r*2+6}" height="10" '
  f'fill="url(#gIron)" rx="1" opacity="0.88"/>')
# Crystal frieze inlay on entablature
A(f'<rect x="{rot_cx-drum_r+4}" y="{drum_base_y-drum_h-6}" width="{(drum_r-4)*2}" height="6" '
  f'fill="url(#gCrystalPanel)" rx="1" opacity="0.45"/>')
# Crystal windows in drum (5 visible arched windows)
for wi in range(5):
    wx2 = rot_cx - 36 + wi * 18
    wy2 = drum_base_y - drum_h + drum_h * 0.22
    A(iron_window(wx2, wy2, 10, drum_h * 0.52, 0.60))

# Dome base ring (iron ring joining drum to dome)
dome_base_y = drum_base_y - drum_h - 8
A(f'<rect x="{rot_cx-drum_r-4}" y="{dome_base_y-4}" width="{(drum_r+4)*2}" height="6" '
  f'fill="url(#gIron)" rx="1" opacity="0.90"/>')
A(f'<rect x="{rot_cx-drum_r-4}" y="{dome_base_y-6}" width="{(drum_r+4)*2}" height="3" '
  f'fill="url(#gRing)" rx="1" opacity="0.50"/>')

# THE DOME — hemispherical, black iron skeleton, crystal panels between ribs
dome_cx = rot_cx; dome_cy = dome_base_y
dome_rx = drum_r + 4; dome_ry = 42

# Crystal panel fill (the shimmering crystal sheets — reflected tower glow)
A(f'<ellipse cx="{dome_cx}" cy="{dome_cy}" rx="{dome_rx}" ry="{dome_ry}" '
  f'fill="#0E1C30" opacity="0.88"/>')
A(f'<ellipse cx="{dome_cx}" cy="{dome_cy}" rx="{dome_rx}" ry="{dome_ry}" '
  f'fill="url(#gTowerGlow)" opacity="0.55"/>')
# Panel shimmer (blue-crystal gleam)
A(f'<ellipse cx="{dome_cx}" cy="{dome_cy}" rx="{dome_rx}" ry="{dome_ry}" '
  f'fill="url(#gCrystalPanel)" opacity="0.30"/>')
# Dome highlight (specular reflection of Crystal Tower)
A(f'<ellipse cx="{dome_cx-14}" cy="{dome_cy-18}" rx="{dome_rx*0.38:.0f}" ry="{dome_ry*0.28:.0f}" '
  f'fill="#A8D8FF" opacity="0.32"/>')
A(f'<ellipse cx="{dome_cx-8}" cy="{dome_cy-24}" rx="{dome_rx*0.18:.0f}" ry="{dome_ry*0.15:.0f}" '
  f'fill="#FFFFFF" opacity="0.22"/>')

# Iron ribs (8 structural ribs — most visible in lower half)
n_ribs = 8
for ri in range(n_ribs):
    ang = math.radians(ri * 180 / n_ribs)
    tip_x = dome_cx; tip_y = dome_cy - dome_ry
    rim_x = dome_cx + math.cos(ang + math.pi/2) * dome_rx
    rim_y = dome_cy + math.sin(ang + math.pi/2) * dome_ry * 0.85
    A(f'<line x1="{tip_x}" y1="{tip_y}" x2="{rim_x:.0f}" y2="{rim_y:.0f}" '
      f'stroke="#18181E" stroke-width="3.0" opacity="0.85"/>')
    # Mirror rib
    rim_xm = dome_cx - math.cos(ang + math.pi/2) * dome_rx
    A(f'<line x1="{tip_x}" y1="{tip_y}" x2="{rim_xm:.0f}" y2="{rim_y:.0f}" '
      f'stroke="#18181E" stroke-width="3.0" opacity="0.85"/>')
# Oculus ring at dome apex
A(f'<circle cx="{dome_cx}" cy="{dome_cy-dome_ry}" r="8" fill="url(#gIron)" opacity="0.90"/>')
A(f'<circle cx="{dome_cx}" cy="{dome_cy-dome_ry}" r="5" fill="url(#gRing)" opacity="0.80"/>')
A(f'<circle cx="{dome_cx}" cy="{dome_cy-dome_ry}" r="2.5" fill="#FFFFFF" opacity="0.90"/>')

# Crystal finial spire (atop the oculus)
fin_base = dome_cy - dome_ry - 8
A(f'<polygon points="{dome_cx},{fin_base-22} {dome_cx+7},{fin_base} {dome_cx-7},{fin_base}" '
  f'fill="url(#gRing)" opacity="0.92"/>')
A(f'<polygon points="{dome_cx},{fin_base-22} {dome_cx+4},{fin_base-10} {dome_cx-4},{fin_base-10}" '
  f'fill="#FFFFFF" opacity="0.80"/>')
# Finial glow
A(f'<circle cx="{dome_cx}" cy="{fin_base-14}" r="8" fill="#80C8FF" opacity="0.22"/>')
A(f'<circle cx="{dome_cx}" cy="{fin_base-14}" r="16" fill="#50A0E8" opacity="0.08"/>')

# Iron base collar band
A(f'<ellipse cx="{dome_cx}" cy="{dome_cy}" rx="{dome_rx+2}" ry="8" '
  f'fill="url(#gIron)" opacity="0.88"/>')
A(f'<ellipse cx="{dome_cx}" cy="{dome_cy}" rx="{dome_rx+2}" ry="8" '
  f'fill="none" stroke="url(#gRing)" stroke-width="2" opacity="0.45"/>')

# Rotunda glow on ground
A(f'<ellipse cx="{dome_cx}" cy="{rot_base}" rx="80" ry="18" fill="#4888D8" opacity="0.10"/>')

# ═════════════════════════════════════════════════════════════════════════════
#  9. GROUND PLAZA — dark stone tiles, crystal vein channels
# ═════════════════════════════════════════════════════════════════════════════
A('<rect y="365" width="400" height="235" fill="url(#gGround)"/>')
# Platform top edge (crystal-lit ledge)
A('<rect y="363" width="400" height="4" fill="url(#gRing)" opacity="0.38"/>')
A('<ellipse cx="200" cy="365" rx="200" ry="6" fill="#5898E0" opacity="0.18"/>')

# Stone tile grid
for ty2 in range(372, 600, 24):
    A(f'<line x1="0" y1="{ty2}" x2="400" y2="{ty2}" stroke="#1C1E2E" stroke-width="1.2" opacity="0.48"/>')
for tx2 in range(0, 401, 26):
    A(f'<line x1="{tx2}" y1="365" x2="{tx2}" y2="600" stroke="#1C1E2E" stroke-width="1.0" opacity="0.38"/>')

# Crystal aether vein channels (glowing lines in the plaza floor)
vein_data = [
    ("M200,365 Q192,400 185,450 L178,530 L175,600", "#4888C8", 2.5, 0.38),
    ("M200,365 Q208,400 215,450 L222,530 L225,600", "#4888C8", 2.5, 0.38),
    ("M200,365 Q185,390 165,418 L138,460 L110,510", "#3878B8", 2.0, 0.28),
    ("M200,365 Q215,390 235,418 L262,460 L290,510", "#3878B8", 2.0, 0.28),
    ("M200,365 Q175,382 148,400 L108,428 L72,460",  "#2860A0", 1.5, 0.20),
    ("M200,365 Q225,382 252,400 L292,428 L328,460", "#2860A0", 1.5, 0.20),
]
for vpath, vcol, vsw, vop in vein_data:
    A(f'<path d="{vpath}" fill="none" stroke="{vcol}" stroke-width="{vsw*1.5}" opacity="{vop*0.45:.2f}"/>')
    A(f'<path d="{vpath}" fill="none" stroke="#90C8FF" stroke-width="{vsw*0.4:.1f}" opacity="{vop:.2f}"/>')

# ═════════════════════════════════════════════════════════════════════════════
#  10. CRYSTAL PILLARS — flanking the central path
# ═════════════════════════════════════════════════════════════════════════════
def xtal_pillar(px, py, h=80, w=13):
    out = []
    # Stone base
    out.append(f'<rect x="{px-w//2-4}" y="{py-10}" width="{w+8}" height="12" '
               f'fill="url(#gSandSh)" rx="2" opacity="0.90"/>')
    # Iron banding on base
    out.append(iron_divider(px-w//2-5, py-10, px+w//2+5, py-10, 2.5, 0.72))
    # Shaft (iron-cased stone)
    out.append(f'<rect x="{px-w//2}" y="{py-10-h}" width="{w}" height="{h}" '
               f'fill="url(#gPillar)" rx="2" opacity="0.92"/>')
    # Iron vertical strips on shaft
    out.append(f'<rect x="{px-w//2}" y="{py-10-h}" width="3" height="{h}" '
               f'fill="url(#gIron)" opacity="0.60"/>')
    out.append(f'<rect x="{px+w//2-3}" y="{py-10-h}" width="3" height="{h}" '
               f'fill="url(#gIron)" opacity="0.60"/>')
    # Crystal shard cap (glowing blue tip)
    pts = f'{px},{py-10-h-18} {px+w//2+3},{py-10-h} {px-w//2-3},{py-10-h}'
    out.append(f'<polygon points="{pts}" fill="url(#gRing)" opacity="0.88"/>')
    out.append(f'<polygon points="{pts}" fill="url(#gCrystalPanel)" opacity="0.45"/>')
    # Glow
    out.append(f'<ellipse cx="{px}" cy="{py-10-h-8}" rx="{w+4:.0f}" ry="14" '
               f'fill="#60B0F0" opacity="0.25"/>')
    out.append(f'<ellipse cx="{px}" cy="{py-10-h-8}" rx="{w*2:.0f}" ry="26" '
               f'fill="#4090D8" opacity="0.09"/>')
    # Highlight streak
    out.append(f'<line x1="{px-2}" y1="{py-10-h-15}" x2="{px-2}" y2="{py-12}" '
               f'stroke="#FFFFFF" stroke-width="1.2" opacity="0.22"/>')
    # Iron capital ring
    out.append(f'<rect x="{px-w//2-5}" y="{py-10-h-3}" width="{w+10}" height="5" '
               f'fill="url(#gIron)" rx="1" opacity="0.80"/>')
    return ''.join(out)

# Left pillars
A(xtal_pillar(82,  415, h=72, w=14))
A(xtal_pillar(112, 402, h=62, w=12))
A(xtal_pillar(140, 392, h=54, w=11))
# Right pillars
A(xtal_pillar(318, 415, h=72, w=14))
A(xtal_pillar(288, 402, h=62, w=12))
A(xtal_pillar(260, 392, h=54, w=11))

# ═════════════════════════════════════════════════════════════════════════════
#  11. STREET LANTERNS — warm amber, added when night first returned
# ═════════════════════════════════════════════════════════════════════════════
lantern_locs = [
    (50,432,32),(88,420,28),(126,432,30),
    (350,432,32),(312,420,28),(274,432,30),
    (35,505,28),(70,515,26),(108,505,28),
    (365,505,28),(330,515,26),(292,505,28),
]
for lx2, ly2, lh in lantern_locs:
    A(lantern_post(lx2, ly2, h=lh, lamp_w=9, lamp_h=12))

# ═════════════════════════════════════════════════════════════════════════════
#  12. CENTRAL STONE PATH (worn stone, faintly crystal-lit)
# ═════════════════════════════════════════════════════════════════════════════
A('<path d="M170,600 L174,540 L178,480 L181,430 L184,390 L186,368" '
  'fill="none" stroke="#2A2C3C" stroke-width="26" stroke-linecap="round" opacity="0.82"/>')
A('<path d="M170,600 L174,540 L178,480 L181,430 L184,390 L186,368" '
  'fill="none" stroke="#3A3C50" stroke-width="20" stroke-linecap="round" opacity="0.60"/>')
# Flagstone joints
for pjy in [374, 398, 424, 452, 480, 510, 545]:
    A(f'<line x1="168" y1="{pjy}" x2="192" y2="{pjy}" stroke="#1A1C2C" stroke-width="1.5" opacity="0.50"/>')
# Crystal vein along path centerline
A('<path d="M180,600 L182,540 L183,480 L184,430 L185,390 L186,368" '
  'fill="none" stroke="#5898D8" stroke-width="1.2" opacity="0.32"/>')

# ═════════════════════════════════════════════════════════════════════════════
#  13. STAGE 5 — THE EXEDRA FOUNTAIN
#      Circular grand plaza fountain, crystal centerpiece, iconic gathering spot
#      (design at x=148 — renders at 200 after stage5 +52px transform)
# ═════════════════════════════════════════════════════════════════════════════
fc = 148; fb = 240   # fountain center x, base y

# Outer basin rim (wide circular pool)
A(f'<ellipse cx="{fc}" cy="{fb}" rx="52" ry="14" fill="#0C1020" opacity="0.88"/>')
A(f'<ellipse cx="{fc}" cy="{fb}" rx="52" ry="14" fill="url(#gFountain)" opacity="0.58"/>')
# Water surface reflections of tower
A(f'<ellipse cx="{fc-10}" cy="{fb-3}" rx="18" ry="5" fill="#C0E8FF" opacity="0.28"/>')
# Water ring lines
for rr in [0.55, 0.75, 0.90]:
    A(f'<ellipse cx="{fc}" cy="{fb}" rx="{52*rr:.0f}" ry="{14*rr:.0f}" '
      f'fill="none" stroke="#70C0FF" stroke-width="1.2" opacity="0.35"/>')
# Basin wall (sandstone + iron trim)
A(f'<rect x="{fc-54}" y="{fb-13}" width="108" height="13" fill="url(#gSandLit)" rx="3" opacity="0.90"/>')
A(f'<ellipse cx="{fc}" cy="{fb-13}" rx="54" ry="9" fill="url(#gSandLit)" opacity="0.90"/>')
A(iron_divider(fc-55, fb-13, fc+55, fb-13, 2.5, 0.75))
# Crystal band inlay on basin rim
A(f'<ellipse cx="{fc}" cy="{fb-13}" rx="54" ry="9" fill="none" '
  f'stroke="url(#gRing)" stroke-width="2.5" opacity="0.50"/>')
# Basin detail: iron brackets
for bi in range(6):
    bang = math.radians(bi * 60)
    bx2 = fc + math.cos(bang)*50; by2 = fb + math.sin(bang)*13 - 13
    A(f'<circle cx="{bx2:.0f}" cy="{by2:.0f}" r="3" fill="url(#gIron)" opacity="0.80"/>')

# Central column / pedestal
A(f'<rect x="{fc-7}" y="{fb-72}" width="14" height="59" fill="url(#gSandLit)" rx="3" opacity="0.92"/>')
A(iron_divider(fc-8, fb-72, fc+8, fb-72, 2.5, 0.75))
A(iron_divider(fc-8, fb-14, fc+8, fb-14, 2.5, 0.75))
# Column iron fluting
for fl_off in [-3, 0, 3]:
    A(f'<line x1="{fc+fl_off}" y1="{fb-72}" x2="{fc+fl_off}" y2="{fb-15}" '
      f'stroke="#18181E" stroke-width="1.2" opacity="0.40"/>')

# Upper basin (elevated, smaller)
A(f'<ellipse cx="{fc}" cy="{fb-74}" rx="26" ry="7" fill="#0C1020" opacity="0.88"/>')
A(f'<ellipse cx="{fc}" cy="{fb-74}" rx="26" ry="7" fill="url(#gFountain)" opacity="0.55"/>')
A(f'<rect x="{fc-28}" y="{fb-82}" width="56" height="8" fill="url(#gSandLit)" rx="2" opacity="0.90"/>')
A(f'<ellipse cx="{fc}" cy="{fb-82}" rx="28" ry="7" fill="url(#gSandLit)" opacity="0.90"/>')
A(iron_divider(fc-29, fb-82, fc+29, fb-82, 2.0, 0.72))
A(f'<ellipse cx="{fc}" cy="{fb-82}" rx="28" ry="7" fill="none" '
  f'stroke="url(#gRing)" stroke-width="1.8" opacity="0.48"/>')

# Crystal centerpiece spire (THE iconic glowing crystal obelisk)
A(f'<polygon points="{fc},{fb-118} {fc+12},{fb-82} {fc-12},{fb-82}" '
  f'fill="url(#gTowerVert)" opacity="0.92"/>')
A(f'<polygon points="{fc},{fb-118} {fc+7},{fb-95} {fc-7},{fb-95}" '
  f'fill="#FFFFFF" opacity="0.70"/>')
# Facet highlight
A(f'<line x1="{fc+2}" y1="{fb-116}" x2="{fc+2}" y2="{fb-84}" '
  f'stroke="#FFFFFF" stroke-width="1.5" opacity="0.55"/>')
# Crystal glow (multi-layer)
A(f'<ellipse cx="{fc}" cy="{fb-102}" rx="24" ry="24" fill="#60B0FF" opacity="0.15"/>')
A(f'<ellipse cx="{fc}" cy="{fb-100}" rx="16" ry="18" fill="#90D0FF" opacity="0.22"/>')
A(f'<ellipse cx="{fc}" cy="{fb-104}" rx="8" ry="10" fill="#C0EAFF" opacity="0.40"/>')
A(f'<circle cx="{fc}" cy="{fb-116}" r="5" fill="#FFFFFF" opacity="0.92"/>')
# Orbiting crystal facets (smaller shards around main spire)
for si in range(4):
    sang = si * 90
    srad = math.radians(sang)
    sox = fc + math.cos(srad) * 20; soy = fb - 98 + math.sin(srad) * 8
    A(f'<polygon points="{sox:.0f},{soy-8:.0f} {sox+5:.0f},{soy:.0f} {sox-5:.0f},{soy:.0f}" '
      f'fill="url(#gRing)" opacity="0.72"/>')
    A(f'<circle cx="{sox:.0f}" cy="{soy-4:.0f}" r="3" fill="#90D0FF" opacity="0.30"/>')

# Water jets (arcing from upper basin outward)
for jang in [-55, -25, 0, 25, 55]:
    jrad = math.radians(jang - 90)
    jex = fc + math.cos(jrad)*36; jey = fb - 82 + math.sin(jrad)*28
    A(f'<path d="M{fc},{fb-82} Q{fc+math.cos(jrad)*18:.0f},{fb-82+math.sin(jrad)*12:.0f} {jex:.0f},{jey:.0f}" '
      f'fill="none" stroke="#90D0FF" stroke-width="2.0" opacity="0.50" stroke-linecap="round"/>')
    # Splash droplets
    A(f'<circle cx="{jex:.0f}" cy="{jey:.0f}" r="2" fill="#B0E0FF" opacity="0.50"/>')

# ═════════════════════════════════════════════════════════════════════════════
#  14. STAGE 10 — MAIN CRYSTARIUM GATE
#      Twin iron-stone towers flanking a grand arch. Crystal Tower visible
#      through arch opening. Scale 1.5× at (200,531).
# ═════════════════════════════════════════════════════════════════════════════
gx = 200; gb = 578   # gate center, base y

# Gate threshold platform (sandstone + iron trim)
A(f'<rect x="{gx-80}" y="{gb-8}" width="160" height="14" fill="url(#gSandLit)" rx="2" opacity="0.92"/>')
A(iron_divider(gx-81, gb-8, gx+81, gb-8, 3.0, 0.80))
# Crystal inlay in threshold
A(f'<rect x="{gx-70}" y="{gb-5}" width="140" height="4" fill="url(#gRing)" rx="1" opacity="0.35"/>')
# Threshold rune pattern (iron brackets)
for ti in range(8):
    A(f'<rect x="{gx-64+ti*18}" y="{gb-7}" width="10" height="4" '
      f'fill="url(#gIron)" rx="1" opacity="0.55"/>')

# Left tower
col_w = 28; col_h = 125
A(f'<rect x="{gx-84}" y="{gb-8-col_h}" width="{col_w}" height="{col_h}" '
  f'fill="url(#gSandLit)" rx="2" opacity="0.95"/>')
# Iron pilasters on left tower
for pi in range(3):
    px2 = gx - 84 + pi * col_w / 2
    A(f'<rect x="{px2:.0f}" y="{gb-8-col_h}" width="5" height="{col_h}" '
      f'fill="url(#gIron)" rx="1" opacity="0.65"/>')
# Iron band courses
for bfrac in [0.18, 0.40, 0.62, 0.82]:
    by2 = gb - 8 - col_h + col_h * bfrac
    A(f'<rect x="{gx-86}" y="{by2:.0f}" width="{col_w+4}" height="5" '
      f'fill="url(#gIron)" rx="1" opacity="0.70"/>')
# Crystal window in left tower
A(iron_window(gx-78, gb-8-col_h+col_h*0.30, 14, 20, 0.70))
# Left tower capital (iron crenellation)
A(f'<rect x="{gx-88}" y="{gb-8-col_h-10}" width="{col_w+8}" height="12" '
  f'fill="url(#gIron)" rx="1" opacity="0.90"/>')
A(f'<rect x="{gx-88}" y="{gb-8-col_h-13}" width="{col_w+8}" height="4" '
  f'fill="url(#gRing)" rx="1" opacity="0.55"/>')
# Left tower crystal spire
A(f'<polygon points="{gx-70},{gb-8-col_h-32} {gx-62},{gb-8-col_h-10} {gx-78},{gb-8-col_h-10}" '
  f'fill="url(#gRing)" opacity="0.88"/>')
A(f'<polygon points="{gx-70},{gb-8-col_h-32} {gx-66},{gb-8-col_h-18} {gx-74},{gb-8-col_h-18}" '
  f'fill="#FFFFFF" opacity="0.65"/>')
A(f'<ellipse cx="{gx-70}" cy="{gb-8-col_h-22}" rx="9" ry="9" fill="#50A8F0" opacity="0.18"/>')
# Left tower lanterns
A(lantern_post(gx-72, gb-12, h=18, lamp_w=7, lamp_h=9))
A(lantern_post(gx-96, gb-8, h=22, lamp_w=8, lamp_h=10))

# Right tower (mirror)
A(f'<rect x="{gx+56}" y="{gb-8-col_h}" width="{col_w}" height="{col_h}" '
  f'fill="url(#gSandSh)" rx="2" opacity="0.95"/>')
for pi in range(3):
    px2 = gx + 56 + pi * col_w / 2
    A(f'<rect x="{px2:.0f}" y="{gb-8-col_h}" width="5" height="{col_h}" '
      f'fill="url(#gIron)" rx="1" opacity="0.65"/>')
for bfrac in [0.18, 0.40, 0.62, 0.82]:
    by2 = gb - 8 - col_h + col_h * bfrac
    A(f'<rect x="{gx+54}" y="{by2:.0f}" width="{col_w+4}" height="5" '
      f'fill="url(#gIron)" rx="1" opacity="0.70"/>')
A(iron_window(gx+64, gb-8-col_h+col_h*0.30, 14, 20, 0.70))
A(f'<rect x="{gx+52}" y="{gb-8-col_h-10}" width="{col_w+8}" height="12" '
  f'fill="url(#gIron)" rx="1" opacity="0.90"/>')
A(f'<rect x="{gx+52}" y="{gb-8-col_h-13}" width="{col_w+8}" height="4" '
  f'fill="url(#gRing)" rx="1" opacity="0.55"/>')
A(f'<polygon points="{gx+70},{gb-8-col_h-32} {gx+78},{gb-8-col_h-10} {gx+62},{gb-8-col_h-10}" '
  f'fill="url(#gRing)" opacity="0.88"/>')
A(f'<polygon points="{gx+70},{gb-8-col_h-32} {gx+74},{gb-8-col_h-18} {gx+66},{gb-8-col_h-18}" '
  f'fill="#FFFFFF" opacity="0.65"/>')
A(f'<ellipse cx="{gx+70}" cy="{gb-8-col_h-22}" rx="9" ry="9" fill="#50A8F0" opacity="0.18"/>')
A(lantern_post(gx+72, gb-12, h=18, lamp_w=7, lamp_h=9))
A(lantern_post(gx+96, gb-8, h=22, lamp_w=8, lamp_h=10))

# Arch geometry
arch_base_y = gb - 8 - col_h + 20
arch_peak_y = arch_base_y - 52
arch_lx = gx - 56; arch_rx = gx + 56

# Crystal Tower glimpse through arch (night sky + tower silhouette)
A(f'<path d="M{arch_lx+10},{arch_base_y} '
  f'C{arch_lx+10},{arch_peak_y+10} {arch_rx-10},{arch_peak_y+10} {arch_rx-10},{arch_base_y} Z" '
  f'fill="#04020E" opacity="0.88"/>')
# Stars visible through arch
for _ in range(18):
    asx = _rnd.uniform(arch_lx+12, arch_rx-12)
    asy = _rnd.uniform(arch_peak_y+12, arch_base_y-5)
    A(f'<circle cx="{asx:.0f}" cy="{asy:.0f}" r="{_rnd.uniform(0.5,1.2):.1f}" '
      f'fill="#FFFFFF" opacity="{_rnd.uniform(0.4,0.85):.2f}"/>')
# Mini Crystal Tower visible through arch
mt_cx = gx; mt_tip_y = arch_peak_y + 12
A(f'<polygon points="{mt_cx},{mt_tip_y} {mt_cx+20},{arch_base_y-4} {mt_cx-20},{arch_base_y-4}" '
  f'fill="url(#gTowerVert)" opacity="0.62"/>')
A(f'<polygon points="{mt_cx},{mt_tip_y} {mt_cx+10},{mt_tip_y+24} {mt_cx-10},{mt_tip_y+24}" '
  f'fill="#E8F8FF" opacity="0.78"/>')
A(f'<ellipse cx="{mt_cx}" cy="{mt_tip_y+10}" rx="22" ry="5" fill="#80C8FF" opacity="0.40"/>')
# Aether shimmer from tower through arch
A(f'<path d="M{arch_lx+10},{arch_base_y} '
  f'C{arch_lx+10},{arch_peak_y+10} {arch_rx-10},{arch_peak_y+10} {arch_rx-10},{arch_base_y} Z" '
  f'fill="url(#gGateShimmer)" opacity="0.90"/>')
# Shimmer lines (vertical aether columns)
for vi in range(5):
    vx2 = arch_lx + 14 + vi * 18
    A(f'<line x1="{vx2}" y1="{arch_peak_y+12}" x2="{vx2}" y2="{arch_base_y}" '
      f'stroke="#80C8FF" stroke-width="1.0" opacity="0.20"/>')

# Arch stone body (iron + sandstone)
A(f'<path d="M{arch_lx},{arch_base_y} C{arch_lx},{arch_peak_y} {arch_rx},{arch_peak_y} {arch_rx},{arch_base_y}" '
  f'fill="none" stroke="url(#gSandLit)" stroke-width="22" stroke-linecap="butt" opacity="0.95"/>')
# Iron outer trim ring
A(f'<path d="M{arch_lx-5},{arch_base_y} C{arch_lx-5},{arch_peak_y-7} {arch_rx+5},{arch_peak_y-7} {arch_rx+5},{arch_base_y}" '
  f'fill="none" stroke="url(#gIron)" stroke-width="5" stroke-linecap="butt" opacity="0.85"/>')
# Crystal inner trim
A(f'<path d="M{arch_lx+10},{arch_base_y} C{arch_lx+10},{arch_peak_y+10} {arch_rx-10},{arch_peak_y+10} {arch_rx-10},{arch_base_y}" '
  f'fill="none" stroke="url(#gRing)" stroke-width="2" stroke-linecap="butt" opacity="0.55"/>')
# Iron keystone block
ks_cy = arch_peak_y - 2
A(f'<ellipse cx="{gx}" cy="{ks_cy}" rx="15" ry="11" fill="url(#gIron)" opacity="0.92"/>')
# Crystal keystone gem
A(f'<polygon points="{gx},{ks_cy-14} {gx+8},{ks_cy} {gx-8},{ks_cy}" '
  f'fill="url(#gRing)" opacity="0.90"/>')
A(f'<polygon points="{gx},{ks_cy-14} {gx+5},{ks_cy-7} {gx-5},{ks_cy-7}" '
  f'fill="#FFFFFF" opacity="0.70"/>')
A(f'<ellipse cx="{gx}" cy="{ks_cy-7}" rx="7" ry="7" fill="#60B0FF" opacity="0.22"/>')
# Voussoir joints (7 joints in arch)
for ji in range(7):
    t = (ji+1) / 8.0
    bx2 = (1-t)**2*arch_lx + 2*(1-t)*t*gx + t**2*arch_rx
    by2 = (1-t)**2*arch_base_y + 2*(1-t)*t*arch_peak_y + t**2*arch_base_y
    tdx = 2*(1-t)*(gx-arch_lx) + 2*t*(arch_rx-gx)
    tdy = 2*(1-t)*(arch_peak_y-arch_base_y) + 2*t*(arch_base_y-arch_peak_y)
    tlen = math.hypot(tdx,tdy) or 1
    nx = -tdy/tlen*13; ny = tdx/tlen*13
    A(f'<line x1="{bx2-nx*0.3:.1f}" y1="{by2-ny*0.3:.1f}" x2="{bx2+nx:.1f}" y2="{by2+ny:.1f}" '
      f'stroke="#18181E" stroke-width="1.5" opacity="0.50"/>')

# ═════════════════════════════════════════════════════════════════════════════
#  15. ATMOSPHERE
# ═════════════════════════════════════════════════════════════════════════════
# Ground depth haze
A('<rect y="510" width="400" height="90" fill="url(#gHaze)" opacity="0.72"/>')

# Crystal Tower light shafts (very faint blue rays radiating from tower base)
for lang in [-58, -38, -20, -6, 0, 6, 20, 38, 58]:
    lrad = math.radians(lang - 90)
    llx = T + math.cos(lrad)*480; lly = 300 + math.sin(lrad)*480
    lop = max(0.006, 0.055 - abs(lang)*0.0005)
    lsw = max(0.4, 2.2 - abs(lang)*0.030)
    A(f'<line x1="{T}" y1="300" x2="{llx:.0f}" y2="{lly:.0f}" '
      f'stroke="#78B8FF" stroke-width="{lsw:.1f}" opacity="{lop:.3f}"/>')

# Floating crystal dust motes
motes = [
    (50,185,2.0,1.2,'#90C8FF',0.65),(92,172,1.6,1.0,'#C0E0FF',0.58),
    (148,160,1.8,1.1,'#80B8F0',0.60),(180,180,1.5,0.9,'#A0D0FF',0.52),
    (228,168,1.7,1.0,'#C0E0FF',0.58),(268,158,1.8,1.1,'#80C0FF',0.60),
    (318,175,1.6,1.0,'#90C8FF',0.56),(355,163,1.8,1.1,'#A0D0FF',0.60),
    (38,238,1.5,0.9,'#80B8F0',0.48),(125,228,1.7,1.0,'#C0E0FF',0.52),
    (280,232,1.6,1.0,'#90C8FF',0.52),(362,225,1.5,0.9,'#80C0FF',0.48),
]
for mx,my,mrx,mry,mc,mop in motes:
    A(f'<ellipse cx="{mx}" cy="{my}" rx="{mrx}" ry="{mry}" fill="{mc}" opacity="{mop}"/>')
    A(f'<ellipse cx="{mx}" cy="{my}" rx="{mrx*3.5:.1f}" ry="{mry*3.5:.1f}" fill="{mc}" opacity="{mop*0.08:.2f}"/>')

# Vignette (subtle edge darkening)
A('<rect width="400" height="600" fill="url(#gVig)"/>')

A('</svg>')

# ═════════════════════════════════════════════════════════════════════════════
#  VALIDATE + INJECT
# ═════════════════════════════════════════════════════════════════════════════
svg = ''.join(parts)
print(f'ULTIMATE SVG: {len(svg):,} chars')

ro = len(_re.findall(r'<radialGradient', svg))
rc = len(_re.findall(r'</radialGradient', svg))
lo = len(_re.findall(r'<linearGradient', svg))
lc = len(_re.findall(r'</linearGradient', svg))
print(f'  radialGradient: {ro}/{rc}  linearGradient: {lo}/{lc}')
if ro != rc: raise RuntimeError(f'radialGradient mismatch: {ro} vs {rc}')
if lo != lc: raise RuntimeError(f'linearGradient mismatch: {lo} vs {lc}')

if svg.count('`'): raise RuntimeError('Backtick found in SVG!')
if svg.count("'"): raise RuntimeError('Single quote found in SVG!')

import xml.etree.ElementTree as ET
try:
    ET.fromstring(svg)
    print('  XML parse: OK')
except ET.ParseError as e:
    raise RuntimeError(f'XML parse error: {e}')

# CSS fallback
html2 = html
for old, new in [
    ('#game-view[data-diff="ULTIMATE"] { background: rgb(10,5,32); }',
     '#game-view[data-diff="ULTIMATE"] { background: rgb(3,1,15); }'),
    ('.map-scroll[data-diff="ULTIMATE"] { background: #0A0520; }',
     '.map-scroll[data-diff="ULTIMATE"] { background: #03010F; }'),
]:
    if old in html2:
        html2 = html2.replace(old, new)
        print(f'  CSS updated: {old[:55]}')

pattern = r"(if\(diff===.ULTIMATE.\) return \`)(.*?)(\`;)"
repl = lambda m: m.group(1) + svg + m.group(3)
new_html, n = _re.subn(pattern, repl, html2, flags=_re.DOTALL)
if n == 0:
    raise RuntimeError("ULTIMATE pattern not found in stage.html")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print(f'stage.html written. ({n} replacement)')
