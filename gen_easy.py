#!/usr/bin/env python3
"""gen_easy.py — Gridania masterpiece (FF14 quality, sacred ancient forest)."""
import re

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

P = []
A = P.append

A('<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">')

# ── DEFS ────────────────────────────────────────────────────────────────
A('<defs>')

# Forest atmosphere — near-black canopy ceiling to deep forest green floor
A('<linearGradient id="eSky" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#030804"/>'
  '<stop offset="14%"  stop-color="#060E06"/>'
  '<stop offset="32%"  stop-color="#0A1A08"/>'
  '<stop offset="54%"  stop-color="#102410"/>'
  '<stop offset="76%"  stop-color="#182E0E"/>'
  '<stop offset="100%" stop-color="#1E3A10"/>'
  '</linearGradient>')

# Amber radial light — canopy shaft source (upper center)
A('<radialGradient id="eShaft" cx="50%" cy="0%" r="70%">'
  '<stop offset="0%"   stop-color="#C88010" stop-opacity="0.55"/>'
  '<stop offset="30%"  stop-color="#B07010" stop-opacity="0.25"/>'
  '<stop offset="65%"  stop-color="#906010" stop-opacity="0.08"/>'
  '<stop offset="100%" stop-color="#906010" stop-opacity="0"/>'
  '</radialGradient>')

# Tree trunk — near-black warm brown
A('<linearGradient id="eTrunk" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#0E0702"/>'
  '<stop offset="25%"  stop-color="#1E1006"/>'
  '<stop offset="55%"  stop-color="#2A1A0A"/>'
  '<stop offset="78%"  stop-color="#1E1208"/>'
  '<stop offset="100%" stop-color="#0E0804"/>'
  '</linearGradient>')

# Tree trunk right (reversed lighting)
A('<linearGradient id="eTrunkR" x1="1" y1="0" x2="0" y2="0">'
  '<stop offset="0%"   stop-color="#0E0702"/>'
  '<stop offset="25%"  stop-color="#1E1006"/>'
  '<stop offset="55%"  stop-color="#2A1A0A"/>'
  '<stop offset="78%"  stop-color="#1E1208"/>'
  '<stop offset="100%" stop-color="#0E0804"/>'
  '</linearGradient>')

# Mid-ground trunk (slightly lighter = farther away)
A('<linearGradient id="eTrunkM" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#141006"/>'
  '<stop offset="40%"  stop-color="#281A0C"/>'
  '<stop offset="100%" stop-color="#180E08"/>'
  '</linearGradient>')

# Elemental glow — teal aether
A('<radialGradient id="eElem" cx="50%" cy="50%" r="50%">'
  '<stop offset="0%"   stop-color="#80FFE8" stop-opacity="0.90"/>'
  '<stop offset="40%"  stop-color="#20D0A8" stop-opacity="0.55"/>'
  '<stop offset="100%" stop-color="#10B890" stop-opacity="0"/>'
  '</radialGradient>')

# Elemental haze (large ambient teal glow on ground)
A('<radialGradient id="eElemHaze" cx="50%" cy="50%" r="50%">'
  '<stop offset="0%"   stop-color="#20D0A0" stop-opacity="0.22"/>'
  '<stop offset="100%" stop-color="#20D0A0" stop-opacity="0"/>'
  '</radialGradient>')

# Mossy forest floor
A('<linearGradient id="eGnd" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#1E3A10"/>'
  '<stop offset="35%"  stop-color="#162E0C"/>'
  '<stop offset="70%"  stop-color="#102208"/>'
  '<stop offset="100%" stop-color="#0C1C06"/>'
  '</linearGradient>')

# Dappled light patch on ground
A('<radialGradient id="eDapple" cx="50%" cy="50%" r="50%">'
  '<stop offset="0%"   stop-color="#6A9020" stop-opacity="0.55"/>'
  '<stop offset="50%"  stop-color="#4A7018" stop-opacity="0.25"/>'
  '<stop offset="100%" stop-color="#4A7018" stop-opacity="0"/>'
  '</radialGradient>')

# Platform/wooden architecture
A('<linearGradient id="eWood" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#5A3818"/>'
  '<stop offset="45%"  stop-color="#422A10"/>'
  '<stop offset="100%" stop-color="#2E1C08"/>'
  '</linearGradient>')

# Gridanian gate wood (warmer, older)
A('<linearGradient id="eGate" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#4A2C10"/>'
  '<stop offset="50%"  stop-color="#361E0A"/>'
  '<stop offset="100%" stop-color="#200E04"/>'
  '</linearGradient>')

# Gate left post (side-lit)
A('<linearGradient id="eGateL" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#5A3818"/>'
  '<stop offset="40%"  stop-color="#422A10"/>'
  '<stop offset="100%" stop-color="#2A1808"/>'
  '</linearGradient>')

# Stream/water glow
A('<linearGradient id="eStream" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#18A888"/>'
  '<stop offset="50%"  stop-color="#10907A"/>'
  '<stop offset="100%" stop-color="#0A7060"/>'
  '</linearGradient>')

# Aetheryte crystal
A('<linearGradient id="eAether" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#A0F0FF"/>'
  '<stop offset="40%"  stop-color="#40D0F0"/>'
  '<stop offset="100%" stop-color="#10A8CC"/>'
  '</linearGradient>')

# Stone (ruins, path)
A('<linearGradient id="eStone" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#504838"/>'
  '<stop offset="100%" stop-color="#342E22"/>'
  '</linearGradient>')

A('</defs>')

# ═══ BASE ATMOSPHERE ═════════════════════════════════════════════════════
# Deep forest atmosphere gradient (full background)
A('<rect width="400" height="600" fill="url(#eSky)"/>')
# Canopy amber radial warmth from above
A('<rect width="400" height="600" fill="url(#eShaft)"/>')

# ═══ AMBIENT LIGHT SHAFTS (volumetric, subtle) ════════════════════════
# These simulate light filtering through breaks in the canopy
A('<polygon points="180,0 220,0 300,600 100,600" fill="#B87808" opacity="0.030"/>')
A('<polygon points="155,0 185,0 230,600 90,600"  fill="#C08010" opacity="0.025"/>')
A('<polygon points="210,0 245,0 320,600 180,600" fill="#B07008" opacity="0.022"/>')
A('<polygon points="130,0 160,0 200,600 50,600"  fill="#A06808" opacity="0.018"/>')
A('<polygon points="240,0 270,0 340,600 220,600" fill="#A06808" opacity="0.018"/>')
A('<polygon points="170,0 200,0 250,600 120,600" fill="#D09020" opacity="0.020"/>')
A('<polygon points="195,0 220,0 275,600 155,600" fill="#C88018" opacity="0.022"/>')

# ═══ DISTANT BACKGROUND TREES (farthest layer, smallest) ══════════════
# These appear between the mid-ground and near trees
A('<rect x="148" y="0"   width="18" height="600" fill="#14100A" opacity="0.80"/>')
A('<rect x="218" y="0"   width="14" height="600" fill="#141008" opacity="0.72"/>')
A('<rect x="172" y="30"  width="12" height="570" fill="#100E08" opacity="0.65"/>')
A('<rect x="244" y="20"  width="15" height="580" fill="#12100A" opacity="0.68"/>')

# ═══ CANOPY OVERHEAD ══════════════════════════════════════════════════
# Massive leaf-cluster ellipses forming the dense canopy ceiling
# Lowest layer (darkest, closest to viewer visually = highest z but low in y)
A('<ellipse cx="50"  cy="0"   rx="110" ry="55"  fill="#060E06" opacity="0.96"/>')
A('<ellipse cx="160" cy="-10" rx="90"  ry="45"  fill="#050D05" opacity="0.94"/>')
A('<ellipse cx="270" cy="-5"  rx="100" ry="50"  fill="#06100A" opacity="0.95"/>')
A('<ellipse cx="380" cy="0"   rx="105" ry="52"  fill="#060E06" opacity="0.96"/>')
# Second layer
A('<ellipse cx="0"   cy="20"  rx="80"  ry="44"  fill="#081408" opacity="0.90"/>')
A('<ellipse cx="110" cy="15"  rx="88"  ry="46"  fill="#091608" opacity="0.88"/>')
A('<ellipse cx="200" cy="8"   rx="95"  ry="42"  fill="#081208" opacity="0.92"/>')
A('<ellipse cx="300" cy="12"  rx="92"  ry="48"  fill="#091608" opacity="0.90"/>')
A('<ellipse cx="400" cy="18"  rx="85"  ry="44"  fill="#081408" opacity="0.88"/>')
# Third layer (slightly lighter, more varied)
A('<ellipse cx="30"  cy="48"  rx="75"  ry="38"  fill="#0C1E0C" opacity="0.85"/>')
A('<ellipse cx="130" cy="40"  rx="85"  ry="42"  fill="#0E2210" opacity="0.82"/>')
A('<ellipse cx="230" cy="35"  rx="80"  ry="40"  fill="#0C1E0C" opacity="0.84"/>')
A('<ellipse cx="335" cy="44"  rx="78"  ry="38"  fill="#0E2210" opacity="0.82"/>')
A('<ellipse cx="400" cy="52"  rx="72"  ry="36"  fill="#0C1A0A" opacity="0.80"/>')
# Fourth layer (canopy underside, some green showing)
A('<ellipse cx="70"  cy="68"  rx="65"  ry="30"  fill="#122410" opacity="0.75"/>')
A('<ellipse cx="185" cy="58"  rx="72"  ry="32"  fill="#142810" opacity="0.72"/>')
A('<ellipse cx="290" cy="64"  rx="68"  ry="31"  fill="#122410" opacity="0.74"/>')
A('<ellipse cx="390" cy="72"  rx="60"  ry="28"  fill="#102210" opacity="0.70"/>')
# Accent leaf clusters (slight green tint where more light filters)
A('<ellipse cx="200" cy="72"  rx="48"  ry="22"  fill="#182E10" opacity="0.58"/>')
A('<ellipse cx="100" cy="82"  rx="42"  ry="18"  fill="#1A3012" opacity="0.52"/>')
A('<ellipse cx="310" cy="78"  rx="44"  ry="20"  fill="#1A3012" opacity="0.54"/>')

# ═══ LEFT FOREGROUND TRUNK (massive, closest) ═════════════════════════
# Main trunk body — slightly irregular polygon for organic feel
A('<polygon points="0,0 0,600 56,600 60,450 52,300 58,150 52,0" fill="url(#eTrunk)"/>')
# Left edge shadow
A('<polygon points="0,0 0,600 12,600 12,0" fill="#040302" opacity="0.60"/>')
# Right edge highlight strip (tiny bit of light hitting edge)
A('<rect x="50" y="0" width="8" height="600" fill="#3A2210" opacity="0.30"/>')
# Bark texture — vertical undulating lines
for yx in [(0,10,5),(60,8,3),(120,12,4),(180,9,5),(240,11,3),(300,8,4),(360,12,5),(420,10,3),(480,9,4),(540,11,5)]:
    y0, dx, w = yx
    A(f'<path d="M{18+dx},{y0} Q{22},{y0+15} {18+dx},{y0+30}" stroke="#0A0604" stroke-width="{w*0.3:.1f}" fill="none" opacity="0.42"/>')
# Horizontal bark cracks
for y in [80, 155, 240, 335, 420, 510]:
    A(f'<path d="M8,{y} Q22,{y+3} 38,{y} Q50,{y-2} 58,{y}" stroke="#0C0806" stroke-width="1.8" fill="none" opacity="0.40"/>')
# Moss patches (green, on lit side of trunk)
A('<ellipse cx="48" cy="230" rx="10" ry="22" fill="#2A4A10" opacity="0.50"/>')
A('<ellipse cx="52" cy="290" rx="8"  ry="16" fill="#284810" opacity="0.44"/>')
A('<ellipse cx="46" cy="370" rx="9"  ry="18" fill="#2C4C12" opacity="0.48"/>')
A('<ellipse cx="50" cy="450" rx="7"  ry="14" fill="#284810" opacity="0.42"/>')

# ═══ LEFT MID TRUNK ═══════════════════════════════════════════════════
A('<polygon points="58,0 58,600 100,600 104,420 98,270 106,130 100,0" fill="url(#eTrunkM)"/>')
A('<rect x="98" y="0" width="6" height="600" fill="#0E0B06" opacity="0.35"/>')
for y in [110, 205, 310, 415, 520]:
    A(f'<path d="M64,{y} Q76,{y+2} 88,{y} Q98,{y-1} 104,{y}" stroke="#0C0908" stroke-width="1.4" fill="none" opacity="0.34"/>')
# Moss
A('<ellipse cx="96" cy="200" rx="8"  ry="18" fill="#284810" opacity="0.42"/>')
A('<ellipse cx="98" cy="310" rx="6"  ry="12" fill="#2A4A10" opacity="0.38"/>')
A('<ellipse cx="96" cy="430" rx="7"  ry="15" fill="#264610" opacity="0.36"/>')

# ═══ RIGHT FOREGROUND TRUNK (massive) ════════════════════════════════
A('<polygon points="400,0 400,600 344,600 340,440 348,290 342,140 348,0" fill="url(#eTrunkR)"/>')
A('<polygon points="400,0 400,600 388,600 388,0" fill="#040302" opacity="0.58"/>')
A('<rect x="342" y="0" width="8" height="600" fill="#3A2210" opacity="0.28"/>')
for y in [70, 160, 255, 350, 445, 535]:
    A(f'<path d="M348,{y} Q358,{y+3} 374,{y} Q386,{y-2} 396,{y}" stroke="#0C0806" stroke-width="1.8" fill="none" opacity="0.40"/>')
A('<ellipse cx="352" cy="210" rx="10" ry="22" fill="#2A4A10" opacity="0.50"/>')
A('<ellipse cx="348" cy="320" rx="8"  ry="17" fill="#284810" opacity="0.44"/>')
A('<ellipse cx="352" cy="430" rx="9"  ry="18" fill="#2C4C12" opacity="0.46"/>')

# ═══ RIGHT MID TRUNK ══════════════════════════════════════════════════
A('<polygon points="342,0 342,600 300,600 296,410 302,260 296,120 302,0" fill="url(#eTrunkM)"/>')
A('<rect x="296" y="0" width="6" height="600" fill="#0E0B06" opacity="0.32"/>')
for y in [100, 200, 305, 410, 515]:
    A(f'<path d="M298,{y} Q308,{y+2} 320,{y} Q332,{y-1} 340,{y}" stroke="#0C0908" stroke-width="1.4" fill="none" opacity="0.32"/>')
A('<ellipse cx="304" cy="185" rx="8"  ry="18" fill="#284810" opacity="0.40"/>')
A('<ellipse cx="302" cy="295" rx="6"  ry="13" fill="#2A4A10" opacity="0.36"/>')
A('<ellipse cx="304" cy="415" rx="7"  ry="15" fill="#264610" opacity="0.34"/>')

# ═══ CITY ON TREE PLATFORMS ════════════════════════════════════════════
# The wooden city of Gridania — built on platforms among the canopy
# LEFT PLATFORM (y≈128-142)
A('<rect x="60"  y="128" width="140" height="16" fill="url(#eWood)" rx="2"/>')
A('<rect x="60"  y="126" width="140" height="5"  fill="#6A4428" opacity="0.70"/>')
A('<rect x="60"  y="142" width="140" height="4"  fill="#1A1008" opacity="0.55"/>')
# Platform plank lines
for x in range(64, 198, 12):
    A(f'<line x1="{x}" y1="128" x2="{x}" y2="144" stroke="#200E06" stroke-width="0.8" opacity="0.35"/>')

# LEFT BUILDINGS on platform
# Building 1 — curved-roof Gridanian hall
A('<rect x="68"  y="92"  width="42" height="38" fill="#3A2210" rx="1"/>')
A('<polygon points="64,94 116,94 90,70" fill="#2A4810"/>')         # leaf/thatch roof
A('<polygon points="66,94 114,94 90,72" fill="#3A6018" opacity="0.60"/>')
# Windows (warm lantern glow)
A('<rect x="74"  y="100" width="8"  height="10" fill="#D09820" rx="2" opacity="0.70"/>')
A('<rect x="88"  y="100" width="8"  height="10" fill="#C88818" rx="2" opacity="0.65"/>')
A('<rect x="102" y="100" width="8"  height="10" fill="#D09820" rx="2" opacity="0.68"/>')
# Lantern hanging outside
A('<line x1="86" y1="88" x2="86" y2="96" stroke="#4A3018" stroke-width="1.5" opacity="0.80"/>')
A('<ellipse cx="86" cy="98" rx="5"  ry="7"   fill="#E0A020" opacity="0.72"/>')
A('<ellipse cx="86" cy="98" rx="3"  ry="4.5" fill="#FFE060" opacity="0.55"/>')
A('<ellipse cx="86" cy="100" rx="5" ry="3"   fill="#C08010" opacity="0.38"/>')

# Building 2 — smaller watch post
A('<rect x="118" y="102" width="28" height="28" fill="#362014" rx="1"/>')
A('<polygon points="114,104 150,104 132,86" fill="#2A4810"/>')
A('<polygon points="116,104 148,104 132,88" fill="#3A6018" opacity="0.58"/>')
A('<rect x="124" y="108" width="7"  height="9"  fill="#D09820" rx="2" opacity="0.65"/>')
A('<rect x="136" y="108" width="7"  height="9"  fill="#D09820" rx="2" opacity="0.65"/>')

# Building 3 — curved tower element
A('<rect x="154" y="95"  width="34" height="35" fill="#3A2210" rx="1"/>')
A('<ellipse cx="171" cy="95" rx="17" ry="8" fill="#2E4A14"/>')     # rounded roof
A('<ellipse cx="171" cy="90" rx="12" ry="6" fill="#406020" opacity="0.65"/>')
A('<rect x="162" y="100" width="8"  height="11" fill="#C88818" rx="2" opacity="0.68"/>')
A('<rect x="177" y="100" width="8"  height="11" fill="#D09820" rx="2" opacity="0.70"/>')
# Lantern
A('<line x1="176" y1="88" x2="176" y2="96" stroke="#4A3018" stroke-width="1.5" opacity="0.78"/>')
A('<ellipse cx="176" cy="98" rx="4.5" ry="6.5" fill="#E0A020" opacity="0.70"/>')
A('<ellipse cx="176" cy="98" rx="2.5" ry="4"   fill="#FFE060" opacity="0.52"/>')

# RIGHT PLATFORM (y≈112-126)
A('<rect x="200" y="112" width="140" height="16" fill="url(#eWood)" rx="2"/>')
A('<rect x="200" y="110" width="140" height="5"  fill="#6A4428" opacity="0.68"/>')
A('<rect x="200" y="128" width="140" height="4"  fill="#1A1008" opacity="0.52"/>')
for x in range(204, 338, 12):
    A(f'<line x1="{x}" y1="112" x2="{x}" y2="128" stroke="#200E06" stroke-width="0.8" opacity="0.32"/>')

# RIGHT BUILDINGS on platform
# Building 4 — main circular tower
A('<rect x="206" y="76"  width="36" height="38" fill="#3C2412" rx="1"/>')
A('<ellipse cx="224" cy="76" rx="18" ry="9" fill="#2A4810"/>')
A('<ellipse cx="224" cy="70" rx="14" ry="7" fill="#3A6018" opacity="0.62"/>')
# Lanterns on tower
for lx, ly in [(212,72),(236,70)]:
    A(f'<line x1="{lx}" y1="{ly}" x2="{lx}" y2="{ly+8}" stroke="#4A3018" stroke-width="1.4" opacity="0.78"/>')
    A(f'<ellipse cx="{lx}" cy="{ly+10}" rx="4" ry="6" fill="#E0A020" opacity="0.68"/>')
    A(f'<ellipse cx="{lx}" cy="{ly+10}" rx="2.5" ry="3.5" fill="#FFE060" opacity="0.50"/>')
A('<rect x="215" y="84"  width="8"  height="10" fill="#C88818" rx="2" opacity="0.66"/>')
A('<rect x="228" y="84"  width="8"  height="10" fill="#D09820" rx="2" opacity="0.68"/>')

# Building 5 — connecting hall
A('<rect x="246" y="82"  width="50" height="32" fill="#382010" rx="1"/>')
A('<polygon points="242,84 300,84 271,62" fill="#284810"/>')
A('<polygon points="244,84 298,84 271,64" fill="#3A6018" opacity="0.60"/>')
A('<rect x="256" y="90"  width="8"  height="11" fill="#D09820" rx="2" opacity="0.65"/>')
A('<rect x="270" y="90"  width="8"  height="11" fill="#C88818" rx="2" opacity="0.62"/>')
A('<rect x="284" y="90"  width="8"  height="11" fill="#D09820" rx="2" opacity="0.65"/>')

# Building 6 — watchtower
A('<rect x="302" y="78"  width="28" height="36" fill="#3A2210" rx="1"/>')
A('<polygon points="298,80 334,80 316,60" fill="#2A4810"/>')
A('<polygon points="300,80 332,80 316,62" fill="#406020" opacity="0.60"/>')
A('<rect x="308" y="86"  width="7"  height="9"  fill="#D09820" rx="2" opacity="0.64"/>')
A('<rect x="320" y="86"  width="7"  height="9"  fill="#D09820" rx="2" opacity="0.64"/>')
# Lantern
A('<line x1="322" y1="74" x2="322" y2="82" stroke="#4A3018" stroke-width="1.4" opacity="0.76"/>')
A('<ellipse cx="322" cy="84" rx="4"  ry="6"   fill="#E0A020" opacity="0.66"/>')
A('<ellipse cx="322" cy="84" rx="2.5" ry="3.5" fill="#FFE060" opacity="0.48"/>')

# ─── ROPE BRIDGE between platforms ────────────────────────────────────
# Main cable ropes
A('<path d="M196,136 Q200,144 200,144" stroke="#5A3A18" stroke-width="3" fill="none" opacity="0.75" stroke-linecap="round"/>')
A('<path d="M198,128 Q202,140 202,144" stroke="#4A3012" stroke-width="2" fill="none" opacity="0.60" stroke-linecap="round"/>')
# Decorative rope spanning platforms (catenary curve)
A('<path d="M60,136 Q130,168 200,128" stroke="#5A3A18" stroke-width="2.5" fill="none" opacity="0.62"/>')
A('<path d="M62,138 Q132,170 202,130" stroke="#3A2210" stroke-width="1.2" fill="none" opacity="0.40"/>')
A('<path d="M200,122 Q270,164 340,118" stroke="#5A3A18" stroke-width="2.5" fill="none" opacity="0.60"/>')
A('<path d="M202,124 Q272,166 342,120" stroke="#3A2210" stroke-width="1.2" fill="none" opacity="0.38"/>')
# Vertical rope slats on bridge
for t in range(0, 9):
    frac = t / 8.0
    bx = int(60 + frac * (200 - 60))
    by = int(136 + 32 * 4 * frac * (1 - frac))  # catenary sag
    A(f'<line x1="{bx}" y1="136" x2="{bx}" y2="{by}" stroke="#4A3018" stroke-width="1.2" opacity="0.48"/>')
for t in range(0, 9):
    frac = t / 8.0
    bx = int(200 + frac * (340 - 200))
    by = int(122 + 42 * 4 * frac * (1 - frac))
    A(f'<line x1="{bx}" y1="122" x2="{bx}" y2="{by}" stroke="#4A3018" stroke-width="1.2" opacity="0.46"/>')

# Wall / city rampart behind buildings
A('<rect x="60"  y="138" width="140" height="20" fill="#2A1A0A" opacity="0.70"/>')
A('<rect x="200" y="124" width="140" height="18" fill="#2A1A0A" opacity="0.65"/>')

# ─── Mid-canopy foliage (below city level) ────────────────────────────
# Canopy continues lower, framing the city
A('<ellipse cx="0"   cy="95"  rx="80"  ry="40"  fill="#0A1808" opacity="0.78"/>')
A('<ellipse cx="80"  cy="106" rx="55"  ry="30"  fill="#0C1C0A" opacity="0.68"/>')
A('<ellipse cx="400" cy="92"  rx="78"  ry="38"  fill="#0A1808" opacity="0.76"/>')
A('<ellipse cx="320" cy="104" rx="58"  ry="32"  fill="#0C1C0A" opacity="0.66"/>')
A('<ellipse cx="190" cy="115" rx="52"  ry="24"  fill="#0E2010" opacity="0.58"/>')
A('<ellipse cx="210" cy="108" rx="44"  ry="20"  fill="#102210" opacity="0.54"/>')

# ═══ FOREST INTERIOR MID-GROUND ═══════════════════════════════════════
# This zone: y=140-320 — the space between platforms and ground
# Some additional mid-ground trunks visible behind the main ones
A('<rect x="118" y="150" width="20" height="450" fill="#1A1008" opacity="0.68"/>')
A('<rect x="262" y="140" width="18" height="460" fill="#181008" opacity="0.64"/>')
# Thin far background trunks
A('<rect x="132" y="160" width="8"  height="440" fill="#12100A" opacity="0.45"/>')
A('<rect x="248" y="155" width="7"  height="445" fill="#101008" opacity="0.42"/>')

# ─── Ground light dapple patches ───────────────────────────────────────
# Where light shafts hit the forest floor — creates pools of amber-green
A('<ellipse cx="172" cy="390" rx="42" ry="22" fill="url(#eDapple)"/>')
A('<ellipse cx="252" cy="340" rx="36" ry="18" fill="url(#eDapple)"/>')
A('<ellipse cx="130" cy="450" rx="30" ry="14" fill="url(#eDapple)"/>')
A('<ellipse cx="290" cy="470" rx="28" ry="12" fill="url(#eDapple)"/>')
A('<ellipse cx="200" cy="510" rx="24" ry="10" fill="url(#eDapple)"/>')
# Secondary brighter patches
A('<ellipse cx="168" cy="390" rx="18" ry="9"  fill="#5A8828" opacity="0.28"/>')
A('<ellipse cx="248" cy="340" rx="14" ry="7"  fill="#5A8828" opacity="0.25"/>')

# ═══ MOSS GROUND ══════════════════════════════════════════════════════
A('<rect y="305" width="400" height="295" fill="url(#eGnd)"/>')
# Ground surface texture lines
A('<g stroke="#1E3A10" stroke-width="1" opacity="0.35">')
for y in range(318, 601, 16):
    A(f'<path d="M0,{y} Q100,{y-3} 200,{y} Q300,{y+3} 400,{y}" />')
A('</g>')
# Ground color variation patches
A('<ellipse cx="80"  cy="338" rx="60" ry="18" fill="#243E10" opacity="0.38"/>')
A('<ellipse cx="200" cy="352" rx="80" ry="20" fill="#1C3A0C" opacity="0.32"/>')
A('<ellipse cx="320" cy="344" rx="55" ry="16" fill="#243E10" opacity="0.36"/>')
A('<ellipse cx="160" cy="440" rx="70" ry="18" fill="#1E360C" opacity="0.30"/>')
A('<ellipse cx="280" cy="480" rx="60" ry="16" fill="#243E10" opacity="0.28"/>')

# ═══ ANCIENT STONE RUINS / PATH ═══════════════════════════════════════
# Mossy stone slabs on forest floor (the sacred path)
for sx, sy, sw, sh, op in [
    (100,330, 56,10, 0.48),(168,338, 44,9, 0.42),(226,332, 52,10, 0.46),
    (90, 380, 40, 8, 0.40),(148,388, 60,9, 0.44),(220,384, 48, 8, 0.42),(280,390, 44,8, 0.38),
    (120,434, 50,8, 0.38),(185,440, 56,9, 0.40),(250,436, 48,8, 0.36),
]:
    A(f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" fill="url(#eStone)" rx="2" opacity="{op}"/>')
    A(f'<rect x="{sx+2}" y="{sy}" width="{sw-4}" height="3" fill="#6A6050" opacity="0.22"/>')

# ═══ STREAM (glowing elemental water) ═══════════════════════════════════
# A small glowing stream winds across the forest floor
A('<path d="M0,310 Q60,298 110,308 Q160,318 200,306 Q245,294 290,304 Q340,314 400,302" '
  'stroke="url(#eStream)" stroke-width="7" fill="none" opacity="0.72" stroke-linecap="round"/>')
A('<path d="M0,311 Q60,299 110,309 Q160,319 200,307 Q245,295 290,305 Q340,315 400,303" '
  'stroke="#30D4B0" stroke-width="3" fill="none" opacity="0.48" stroke-linecap="round"/>')
A('<path d="M0,310 Q60,298 110,308 Q160,318 200,306 Q245,294 290,304 Q340,314 400,302" '
  'stroke="#80FFE8" stroke-width="1.2" fill="none" opacity="0.32" stroke-linecap="round"/>')
# Stream sparkle points
for cx, cy, r, op in [(48,306,2.0,0.55),(112,310,1.8,0.50),(178,304,2.2,0.52),
                       (232,308,1.8,0.48),(298,306,2.0,0.50),(358,300,1.6,0.45)]:
    A(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#A0FFEE" opacity="{op}"/>')

# ═══ ROOT SYSTEMS (at base of large trunks) ═══════════════════════════
# Left foreground trunk roots
A('<path d="M0,560 Q20,540 40,555 Q50,560 56,580" stroke="#1A0E06" stroke-width="12" fill="none" stroke-linecap="round" opacity="0.85"/>')
A('<path d="M0,520 Q30,508 48,525 Q58,535 58,560" stroke="#1A0E06" stroke-width="10" fill="none" stroke-linecap="round" opacity="0.80"/>')
A('<path d="M0,480 Q25,472 44,488 Q54,498 54,530" stroke="#180C04" stroke-width="9"  fill="none" stroke-linecap="round" opacity="0.75"/>')
A('<path d="M0,580 Q22,575 44,582" stroke="#160C04" stroke-width="8"  fill="none" stroke-linecap="round" opacity="0.70"/>')
A('<path d="M20,590 Q35,586 58,596" stroke="#140A04" stroke-width="6"  fill="none" stroke-linecap="round" opacity="0.60"/>')
# Sub-roots from left mid trunk
A('<path d="M60,550 Q74,542 88,556 Q98,564 104,590"  stroke="#180E06" stroke-width="8"  fill="none" stroke-linecap="round" opacity="0.72"/>')
A('<path d="M62,580 Q78,572 96,582 Q104,588 106,600" stroke="#160C04" stroke-width="6"  fill="none" stroke-linecap="round" opacity="0.65"/>')

# Right foreground trunk roots
A('<path d="M400,555 Q380,538 360,552 Q350,558 344,578" stroke="#1A0E06" stroke-width="12" fill="none" stroke-linecap="round" opacity="0.85"/>')
A('<path d="M400,518 Q370,506 352,522 Q342,532 342,558" stroke="#1A0E06" stroke-width="10" fill="none" stroke-linecap="round" opacity="0.80"/>')
A('<path d="M400,478 Q375,470 356,486 Q346,496 346,528" stroke="#180C04" stroke-width="9"  fill="none" stroke-linecap="round" opacity="0.75"/>')
A('<path d="M400,578 Q378,572 356,580"                  stroke="#160C04" stroke-width="8"  fill="none" stroke-linecap="round" opacity="0.70"/>')
# Sub-roots from right mid trunk
A('<path d="M340,548 Q326,540 312,554 Q302,562 296,588" stroke="#180E06" stroke-width="8"  fill="none" stroke-linecap="round" opacity="0.70"/>')
A('<path d="M338,578 Q322,570 304,580 Q296,586 294,600" stroke="#160C04" stroke-width="6"  fill="none" stroke-linecap="round" opacity="0.62"/>')

# ═══ FERNS AND UNDERGROWTH ════════════════════════════════════════════
# Ground-level ferns — pairs of arching fronds with leaf clusters

def fern(ax, ay, scale=1.0, flip=False):
    """Generate fern fronds at position (ax, ay), scale, optional flip."""
    sign = -1 if flip else 1
    out = []
    for angle_deg, length, lw in [(-60, 40, 1.6), (-40, 50, 1.8), (-20, 58, 2.0),
                                    (0, 62, 2.2), (20, 56, 2.0), (40, 48, 1.8), (60, 38, 1.5)]:
        import math
        rad = math.radians(angle_deg * sign - 90)
        dx = int(math.cos(rad) * length * scale)
        dy = int(math.sin(rad) * length * scale)
        ex, ey = ax + dx, ay + dy
        # Frond stem
        out.append(f'<path d="M{ax},{ay} Q{ax+dx//2},{ay+dy//2-int(8*scale)},{ex},{ey}" '
                   f'stroke="#1E4210" stroke-width="{lw*scale:.1f}" fill="none" opacity="0.72"/>')
        # Leaf ellipses along frond
        for t in [0.45, 0.70, 0.90]:
            lx = int(ax + dx * t)
            ly = int(ay + dy * t - 3 * scale)
            lr = int(5 * scale * (1 - t * 0.3))
            out.append(f'<ellipse cx="{lx}" cy="{ly}" rx="{lr}" ry="{max(2,lr//2)}" '
                       f'fill="#264E14" opacity="0.68"/>')
    return ''.join(out)

import math
# Left ferns (clustered at tree bases and along ground)
A(fern(72,  318, 0.85))
A(fern(108, 328, 0.78, flip=True))
A(fern(80,  352, 0.72))
A(fern(116, 360, 0.80, flip=True))
A(fern(68,  410, 0.82))
A(fern(100, 420, 0.76, flip=True))
A(fern(84,  480, 0.70))
A(fern(120, 488, 0.74, flip=True))
# Right ferns
A(fern(328, 322, 0.85, flip=True))
A(fern(292, 332, 0.78))
A(fern(320, 356, 0.72, flip=True))
A(fern(284, 364, 0.80))
A(fern(332, 414, 0.82, flip=True))
A(fern(300, 424, 0.76))
A(fern(316, 484, 0.70, flip=True))
A(fern(280, 492, 0.74))
# Center ground ferns
A(fern(156, 340, 0.60))
A(fern(248, 348, 0.62, flip=True))
A(fern(140, 456, 0.55))
A(fern(262, 462, 0.58, flip=True))

# ─── Moss clumps ─────────────────────────────────────────────────────
for cx, cy, rx, ry, op in [
    (72,338,18,7,0.58),(116,350,14,6,0.52),(88,398,16,6,0.54),
    (328,342,18,7,0.56),(288,352,15,6,0.52),(316,402,14,6,0.50),
    (160,358,20,8,0.48),(244,364,18,7,0.46),(192,424,22,8,0.44),(216,430,16,6,0.42),
    (130,498,14,5,0.40),(272,502,15,5,0.40),(200,524,18,6,0.38),
]:
    A(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#2A5014" opacity="{op}"/>')
    A(f'<ellipse cx="{cx}" cy="{cy-2}" rx="{rx-3}" ry="{max(2,ry-2)}" fill="#385E1C" opacity="0.35"/>')

# ═══ ELEMENTAL AMBIENT GLOW ═══════════════════════════════════════════
# The forest elementals emit faint teal light in various spots
A('<ellipse cx="164" cy="310" rx="40" ry="30" fill="url(#eElemHaze)"/>')
A('<ellipse cx="250" cy="295" rx="35" ry="25" fill="url(#eElemHaze)"/>')
A('<ellipse cx="200" cy="420" rx="45" ry="28" fill="url(#eElemHaze)"/>')
A('<ellipse cx="200" cy="540" rx="38" ry="22" fill="url(#eElemHaze)"/>')
# Small elemental sparks (tiny teal circles floating)
for cx, cy, r, op in [
    (148,248,2.2,0.72),(176,218,1.6,0.60),(224,262,2.0,0.68),
    (138,320,1.8,0.58),(266,308,2.0,0.64),(192,368,1.6,0.55),
    (218,412,2.2,0.60),(158,480,1.8,0.52),(244,496,1.6,0.50),
    (200,340,2.5,0.65),(172,460,1.4,0.48),(228,450,1.6,0.50),
]:
    A(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#40E0C0" opacity="{op}"/>')

# ═══ GOLDEN SPORES (floating particles of light) ══════════════════════
for cx, cy, r, op in [
    (160,170,1.8,0.55),(200,150,2.0,0.60),(244,178,1.6,0.52),
    (136,220,1.4,0.48),(184,202,1.8,0.54),(228,192,1.6,0.50),
    (164,286,1.5,0.46),(212,272,1.8,0.52),(248,294,1.4,0.45),
    (152,360,1.4,0.42),(200,382,1.6,0.45),(256,372,1.4,0.42),
    (175,448,1.3,0.40),(214,436,1.5,0.42),(238,458,1.3,0.38),
]:
    A(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#D8A830" opacity="{op}"/>')

# ═══ STAGE 5 — Spirit Shrine + Elemental Orb (translate +52) ══════════
A('<g transform="translate(52,0)">')

# Shrine totem base (stone foundation)
A('<rect x="188" y="270" width="24" height="10" fill="url(#eStone)" rx="2" opacity="0.80"/>')
A('<rect x="186" y="278" width="28" height="6"  fill="#3A3028" opacity="0.65"/>')

# Totem post (dark carved wood)
A('<rect x="196" y="196" width="8"  height="76" fill="#2A1A0C" rx="2"/>')
A('<rect x="197" y="196" width="2"  height="76" fill="#4A3020" opacity="0.40"/>')
# Carved notches on totem
for y in [210, 225, 240, 255]:
    A(f'<rect x="194" y="{y}" width="12" height="3" fill="#1A1008" opacity="0.60" rx="1"/>')
    A(f'<rect x="194" y="{y}" width="12" height="1" fill="#5A4028" opacity="0.35"/>')

# Cross beam (torii-like horizontal piece)
A('<rect x="181" y="207" width="38" height="5"  fill="#2A1A0C" rx="1"/>')
A('<rect x="181" y="205" width="38" height="3"  fill="#3A2818" rx="1" opacity="0.55"/>')
A('<rect x="178" y="212" width="4"  height="6"  fill="#2A1A0C" rx="1" opacity="0.80"/>')
A('<rect x="218" y="212" width="4"  height="6"  fill="#2A1A0C" rx="1" opacity="0.80"/>')

# Upper perch / spirit platform
A('<rect x="186" y="196" width="28" height="5"  fill="#3A2818" rx="2" opacity="0.90"/>')
A('<rect x="184" y="193" width="32" height="4"  fill="#4A3822" rx="2" opacity="0.80"/>')

# Offering crystals (at base of totem)
for cx, cy, rx, ry, fc in [
    (191, 271, 3, 6, '#60D0FF'),(200, 269, 2.5, 5.5, '#80E8FF'),
    (209, 271, 3, 6, '#50C8F8'),(195, 268, 2, 4, '#A0F4FF'),
    (205, 267, 2, 4.5, '#70DCF8'),
]:
    A(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fc}" opacity="0.72"/>')
    A(f'<ellipse cx="{cx}" cy="{cy-2}" rx="{max(1,rx-1)}" ry="{max(1,ry-2)}" fill="#D0F8FF" opacity="0.40"/>')

# ELEMENTAL ORB (floating teal sphere above totem)
# Outer glow halo
A('<ellipse cx="200" cy="183" rx="28" ry="28" fill="url(#eElem)" opacity="0.70"/>')
A('<ellipse cx="200" cy="183" rx="20" ry="20" fill="#20D0A8" opacity="0.45"/>')
# Orb body
A('<circle cx="200" cy="183" r="12" fill="#18C0A0"/>')
A('<circle cx="200" cy="183" r="12" fill="none" stroke="#60EED8" stroke-width="2" opacity="0.80"/>')
A('<circle cx="200" cy="183" r="8"  fill="#28D8B0"/>')
# Inner bright core
A('<circle cx="200" cy="183" r="5"  fill="#80FFE8"/>')
A('<circle cx="200" cy="183" r="2.5" fill="#D0FFF4" opacity="0.90"/>')
# Orb highlight (lit from above by amber shaft)
A('<ellipse cx="197" cy="179" rx="4" ry="3"  fill="#FFFFFF" opacity="0.35"/>')
# Orbiting elemental sparks
for ang, dist, sr, sop in [(0,16,1.6,0.70),(45,18,1.4,0.65),(90,16,1.6,0.68),
                             (135,18,1.3,0.60),(180,16,1.5,0.65),(225,18,1.4,0.58),
                             (270,16,1.6,0.65),(315,18,1.3,0.60)]:
    rad = math.radians(ang)
    sx = 200 + dist * math.cos(rad)
    sy = 183 + dist * math.sin(rad)
    A(f'<circle cx="{sx:.0f}" cy="{sy:.0f}" r="{sr}" fill="#60FFE0" opacity="{sop}"/>')
# Connection line from orb to totem top (thin teal thread)
A('<line x1="200" y1="195" x2="200" y2="196" stroke="#30E0B8" stroke-width="1.8" opacity="0.65"/>')

# Hanging offering strips (like paper strips on shrine)
for hx, hy, fc in [(190,215,  '#C8A020'), (196,218, '#D0A820'), (204,215, '#B89018'),
                    (210,218,  '#C8A020'), (184,213, '#B08010')]:
    A(f'<line x1="{hx}" y1="{hy}" x2="{hx+1}" y2="{hy+14}" stroke="{fc}" stroke-width="2.5" opacity="0.68"/>')
    A(f'<line x1="{hx}" y1="{hy}" x2="{hx+1}" y2="{hy+14}" stroke="#FFE860" stroke-width="0.8" opacity="0.40"/>')

A('</g>')  # end translate(52,0)

# ═══ GROUND MIST (forest floor haze) ═════════════════════════════════
A('<rect y="290" width="400" height="30" fill="#204010" opacity="0.18"/>')
A('<path d="M0,305 Q50,298 100,305 Q150,312 200,305 Q250,298 300,305 Q350,312 400,305" '
  'stroke="#1E3C0E" stroke-width="20" fill="none" opacity="0.22"/>')

# ═══ STAGE 10 — Gridanian Sacred Gate (×1.5) ══════════════════════════
A('<g transform="translate(200,531) scale(1.5) translate(-200,-531)">')

# Gate shadow on ground
A('<ellipse cx="200" cy="580" rx="72" ry="14" fill="#0A0C04" opacity="0.65"/>')

# ── Left carved post ─────────────────────────────────────────────────
A('<rect x="142" y="466" width="30" height="106" fill="url(#eGateL)" rx="2"/>')
# Wood grain lines
for y in range(474, 572, 8):
    A(f'<path d="M144,{y} Q155,{y+2} 170,{y}" stroke="#1A0C04" stroke-width="1.2" fill="none" opacity="0.42"/>')
# Carved rune marks (elemental inscriptions)
for ry in [480, 498, 516, 534, 552]:
    A(f'<rect x="148" y="{ry}" width="16" height="2" fill="#3A2818" opacity="0.55"/>')
    A(f'<rect x="154" y="{ry-5}" width="6"  height="5" fill="#2A1A0A" opacity="0.50"/>')
# Left edge dark
A('<rect x="142" y="466" width="5" height="106" fill="#0A0804" opacity="0.50"/>')
# Glowing carved rune (teal accent)
A('<rect x="150" y="506" width="12" height="3"  fill="#20C898" opacity="0.45"/>')
A('<rect x="153" y="500" width="5"  height="6"  fill="#18B080" opacity="0.40"/>')
# Post cap
A('<rect x="138" y="460" width="38" height="8"  fill="#3A2810" rx="2"/>')
A('<rect x="134" y="454" width="46" height="7"  fill="#4A3418" rx="2"/>')
# Crenellated top
for bx in [136, 146, 156, 166]:
    A(f'<rect x="{bx}" y="444" width="9" height="12" fill="#3C2A10" rx="1"/>')

# Vines on left post (growing up, organic)
A('<path d="M170,572 Q165,540 170,510 Q175,480 168,460" stroke="#1E4010" stroke-width="3" fill="none" opacity="0.70"/>')
A('<path d="M172,572 Q178,548 172,520 Q166,492 174,470" stroke="#244A14" stroke-width="2" fill="none" opacity="0.55"/>')
for vx, vy in [(163,560),(169,535),(164,508),(171,482),(165,462)]:
    A(f'<ellipse cx="{vx}" cy="{vy}" rx="5" ry="3"  fill="#2A5012" opacity="0.68"/>')
    A(f'<ellipse cx="{vx}" cy="{vy}" rx="3" ry="2"  fill="#386018" opacity="0.48"/>')

# ── Right carved post ─────────────────────────────────────────────────
A('<rect x="228" y="466" width="30" height="106" fill="url(#eGate)" rx="2"/>')
for y in range(474, 572, 8):
    A(f'<path d="M230,{y} Q241,{y+2} 256,{y}" stroke="#1A0C04" stroke-width="1.2" fill="none" opacity="0.40"/>')
for ry in [480, 498, 516, 534, 552]:
    A(f'<rect x="234" y="{ry}" width="16" height="2" fill="#3A2818" opacity="0.52"/>')
    A(f'<rect x="240" y="{ry-5}" width="6"  height="5" fill="#2A1A0A" opacity="0.48"/>')
A('<rect x="253" y="466" width="5" height="106" fill="#0A0804" opacity="0.45"/>')
A('<rect x="234" y="506" width="12" height="3"  fill="#20C898" opacity="0.42"/>')
A('<rect x="242" y="500" width="5"  height="6"  fill="#18B080" opacity="0.38"/>')
A('<rect x="224" y="460" width="38" height="8"  fill="#3A2810" rx="2"/>')
A('<rect x="220" y="454" width="46" height="7"  fill="#4A3418" rx="2"/>')
for bx in [222, 232, 242, 252]:
    A(f'<rect x="{bx}" y="444" width="9" height="12" fill="#3C2A10" rx="1"/>')
# Vines on right post
A('<path d="M230,572 Q235,540 230,510 Q225,480 232,460" stroke="#1E4010" stroke-width="3" fill="none" opacity="0.68"/>')
A('<path d="M228,572 Q222,548 228,520 Q234,492 226,470" stroke="#244A14" stroke-width="2" fill="none" opacity="0.52"/>')
for vx, vy in [(237,560),(231,535),(236,508),(229,482),(235,462)]:
    A(f'<ellipse cx="{vx}" cy="{vy}" rx="5" ry="3"  fill="#2A5012" opacity="0.66"/>')
    A(f'<ellipse cx="{vx}" cy="{vy}" rx="3" ry="2"  fill="#386018" opacity="0.46"/>')

# ── Main wooden arch ─────────────────────────────────────────────────
# Outer silhouette
A('<path d="M140,490 Q200,434 260,490" stroke="#180E04" stroke-width="24" fill="none" stroke-linecap="butt"/>')
# Arch body (warm dark wood)
A('<path d="M140,490 Q200,434 260,490" stroke="url(#eGate)" stroke-width="19" fill="none" stroke-linecap="butt"/>')
# Arch highlight (top lit edge — amber from above)
A('<path d="M142,488 Q200,436 258,488" stroke="#6A4828" stroke-width="4" fill="none" stroke-linecap="butt" opacity="0.38"/>')
# Arch inner shadow
A('<path d="M152,490 Q200,442 248,490" stroke="#0A0604" stroke-width="5" fill="none" stroke-linecap="butt" opacity="0.55"/>')
# Carved joint lines on arch (wood segments)
for x1, y1, x2, y2 in [
    (152,484, 158,470),(166,470, 171,456),(180,461, 182,447),
    (196,444, 197,430),(200,443, 200,429),(204,444, 203,430),
    (218,461, 216,447),(234,470, 229,456),(248,484, 242,470)
]:
    A(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#1A0C04" stroke-width="2.2" opacity="0.45"/>')

# ── Arch decorative carvings (knots, leaf motifs) ─────────────────────
for ang, dist in [(0,24),(45,28),(90,26),(135,28),(180,24)]:
    rad = math.radians(ang - 90)  # -90 to center at top
    # Map along arch: interpolate
    t = ang / 180.0
    bx = int(140 + t * 120)
    # Height along arch (parabolic approximation)
    by = int(490 - 56 * 4 * t * (1 - t))
    A(f'<circle cx="{bx}" cy="{by}" r="4" fill="#3A2818" opacity="0.65"/>')
    A(f'<circle cx="{bx}" cy="{by}" r="2" fill="#20C898" opacity="0.40"/>')

# ── Keystone — elemental seal ─────────────────────────────────────────
A('<polygon points="192,440 200,428 208,440 206,450 194,450" fill="#2A1A0C"/>')
A('<polygon points="193,441 200,431 207,441 205,449 195,449" fill="#4A3820" opacity="0.55"/>')
# Elemental seal center (glowing teal circle)
A('<circle cx="200" cy="441" r="6"  fill="#18A888" opacity="0.80"/>')
A('<circle cx="200" cy="441" r="4"  fill="#30D4B0" opacity="0.70"/>')
A('<circle cx="200" cy="441" r="2"  fill="#88FFE8" opacity="0.85"/>')
# Seal rays
A('<g stroke="#20D0A8" stroke-width="1.2" opacity="0.50">'
  '<line x1="200" y1="432" x2="200" y2="428"/>'
  '<line x1="200" y1="450" x2="200" y2="454"/>'
  '<line x1="192" y1="441" x2="188" y2="441"/>'
  '<line x1="208" y1="441" x2="212" y2="441"/>'
  '</g>')

# ── AETHERYTE CRYSTAL SHARD (atop gate, glowing) ──────────────────────
A('<polygon points="196,422 200,408 204,422 202,432 198,432" fill="url(#eAether)" opacity="0.90"/>')
A('<polygon points="196,422 200,408 204,422 202,432 198,432" fill="none" stroke="#80F0FF" stroke-width="1.5" opacity="0.70"/>')
A('<ellipse cx="200" cy="420" rx="12" ry="8"  fill="#20D0F0" opacity="0.28"/>')
A('<ellipse cx="200" cy="416" rx="7"  ry="5"  fill="#80F8FF" opacity="0.35"/>')
A('<ellipse cx="200" cy="412" rx="4"  ry="3"  fill="#D0FFFF" opacity="0.55"/>')
# Crystal glow rays
A('<g stroke="#40E0FF" stroke-width="1.0" opacity="0.42">'
  '<line x1="200" y1="406" x2="200" y2="398"/>'
  '<line x1="194" y1="414" x2="188" y2="410"/>'
  '<line x1="206" y1="414" x2="212" y2="410"/>'
  '<line x1="192" y1="422" x2="184" y2="422"/>'
  '<line x1="208" y1="422" x2="216" y2="422"/>'
  '</g>')

# ── Vines over arch ──────────────────────────────────────────────────
A('<path d="M140,492 Q152,474 162,466" stroke="#1E4010" stroke-width="2.5" fill="none" opacity="0.65"/>')
A('<path d="M258,492 Q248,472 238,464" stroke="#1E4010" stroke-width="2.5" fill="none" opacity="0.62"/>')
A('<path d="M155,476 Q165,468 170,460" stroke="#244A14" stroke-width="1.5" fill="none" opacity="0.52"/>')
A('<path d="M246,476 Q236,466 232,458" stroke="#244A14" stroke-width="1.5" fill="none" opacity="0.50"/>')
for vx, vy in [(144,488),(150,476),(158,468),(242,488),(248,474),(240,466)]:
    A(f'<ellipse cx="{vx}" cy="{vy}" rx="5" ry="3"  fill="#2A5012" opacity="0.68"/>')
    A(f'<ellipse cx="{vx}" cy="{vy}" rx="3" ry="2"  fill="#386018" opacity="0.46"/>')

# ── Hanging lanterns from arch ────────────────────────────────────────
for lx, ly, rope_dy in [(172,466,18),(200,438,16),(228,466,18)]:
    A(f'<line x1="{lx}" y1="{ly}" x2="{lx}" y2="{ly+rope_dy}" stroke="#3A2810" stroke-width="1.5" opacity="0.75"/>')
    A(f'<ellipse cx="{lx}" cy="{ly+rope_dy+7}" rx="5"   ry="8"   fill="#C89018" opacity="0.82"/>')
    A(f'<ellipse cx="{lx}" cy="{ly+rope_dy+7}" rx="3.5" ry="5.5" fill="#F0B820" opacity="0.68"/>')
    A(f'<ellipse cx="{lx}" cy="{ly+rope_dy+7}" rx="2"   ry="3.5" fill="#FFE040" opacity="0.55"/>')
    A(f'<ellipse cx="{lx}" cy="{ly+rope_dy+14}" rx="5" ry="2"   fill="#A07010" opacity="0.50"/>')

A('</g>')  # end scale group

# ═══ FINAL ATMOSPHERE ════════════════════════════════════════════════
# Deep forest lower mist
A('<rect y="575" width="400" height="25" fill="#102008" opacity="0.55"/>')
A('<path d="M0,580 Q80,572 160,580 Q240,588 320,580 Q360,576 400,580" '
  'stroke="#1A3010" stroke-width="18" fill="none" opacity="0.35"/>')

A('</svg>')

EASY = ''.join(P)

# ── Inject into stage.html ───────────────────────────────────────────────
pattern = r"(if\(diff==='EASY'\) return ')(.*?)(';)"
replacement = r"\g<1>" + EASY.replace('\\', '\\\\') + r"\g<3>"
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

assert new_content != content, "Injection failed — pattern not matched"
assert "eSky" in new_content, "SVG missing in output"
print(f"EASY SVG: {len(EASY):,} chars injected OK")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("stage.html written.")
