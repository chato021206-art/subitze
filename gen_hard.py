#!/usr/bin/env python3
"""gen_hard.py — Thanalan / Ul'dah masterpiece (FF14, burning desert)."""
import re, math

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

P = []
A = P.append

A('<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">')

# ── DEFS ────────────────────────────────────────────────────────────────
A('<defs>')

# Desert sky — cerulean blue to blazing amber at horizon
A('<linearGradient id="hSky" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#001E60"/>'
  '<stop offset="18%"  stop-color="#0840A8"/>'
  '<stop offset="40%"  stop-color="#2870D8"/>'
  '<stop offset="62%"  stop-color="#78A8E0"/>'
  '<stop offset="78%"  stop-color="#C89848"/>'
  '<stop offset="90%"  stop-color="#D8A030"/>'
  '<stop offset="100%" stop-color="#C07818"/>'
  '</linearGradient>')

# Sun — blazing white-hot, upper center-right
A('<radialGradient id="hSun" cx="68%" cy="10%" r="45%">'
  '<stop offset="0%"   stop-color="#FFFEF0" stop-opacity="0.95"/>'
  '<stop offset="18%"  stop-color="#FFF080" stop-opacity="0.60"/>'
  '<stop offset="42%"  stop-color="#FFD040" stop-opacity="0.25"/>'
  '<stop offset="100%" stop-color="#FFD040" stop-opacity="0"/>'
  '</radialGradient>')

# Heat shimmer overlay (horizon glow)
A('<linearGradient id="hHeat" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#E8B040" stop-opacity="0"/>'
  '<stop offset="100%" stop-color="#F0C060" stop-opacity="0.55"/>'
  '</linearGradient>')

# Mesa / sandstone cliff — burnt orange-red
A('<linearGradient id="hMesa" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#D05820"/>'
  '<stop offset="22%"  stop-color="#C04818"/>'
  '<stop offset="50%"  stop-color="#A83810"/>'
  '<stop offset="78%"  stop-color="#8A2C0A"/>'
  '<stop offset="100%" stop-color="#6A2008"/>'
  '</linearGradient>')

# Mesa top surface (slightly cooler)
A('<linearGradient id="hMesaTop" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#E87840"/>'
  '<stop offset="100%" stop-color="#C05820"/>'
  '</linearGradient>')

# Left cliff shadow (left edge)
A('<linearGradient id="hMesaSh" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#200802" stop-opacity="0.62"/>'
  '<stop offset="50%"  stop-color="#200802" stop-opacity="0.20"/>'
  '<stop offset="100%" stop-color="#200802" stop-opacity="0"/>'
  '</linearGradient>')

# Right cliff shadow (right edge)
A('<linearGradient id="hMesaShr" x1="1" y1="0" x2="0" y2="0">'
  '<stop offset="0%"   stop-color="#200802" stop-opacity="0.58"/>'
  '<stop offset="50%"  stop-color="#200802" stop-opacity="0.16"/>'
  '<stop offset="100%" stop-color="#200802" stop-opacity="0"/>'
  '</linearGradient>')

# Ul'dah sandstone building (cream/ivory)
A('<linearGradient id="hBldg" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#F4DFA8"/>'
  '<stop offset="40%"  stop-color="#DECA88"/>'
  '<stop offset="100%" stop-color="#C4A860"/>'
  '</linearGradient>')

# Building shadow side
A('<linearGradient id="hBldgS" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#C8AA68"/>'
  '<stop offset="100%" stop-color="#E8CC88"/>'
  '</linearGradient>')

# Ul'dah dome (iconic teal-viridian)
A('<radialGradient id="hDome" cx="35%" cy="30%" r="60%">'
  '<stop offset="0%"   stop-color="#62B0A0"/>'
  '<stop offset="50%"  stop-color="#3A9080"/>'
  '<stop offset="100%" stop-color="#286860"/>'
  '</radialGradient>')

# Gold / brass trim
A('<linearGradient id="hGold" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#E8B030"/>'
  '<stop offset="50%"  stop-color="#C89020"/>'
  '<stop offset="100%" stop-color="#A87010"/>'
  '</linearGradient>')

# Desert sand floor
A('<linearGradient id="hSand" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#D89830"/>'
  '<stop offset="35%"  stop-color="#C08020"/>'
  '<stop offset="70%"  stop-color="#A86818"/>'
  '<stop offset="100%" stop-color="#8A5010"/>'
  '</linearGradient>')

# Gate pillar (lit side)
A('<linearGradient id="hGateL" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#F0D898"/>'
  '<stop offset="40%"  stop-color="#D8BC78"/>'
  '<stop offset="100%" stop-color="#B09050"/>'
  '</linearGradient>')

# Gate arch fill
A('<linearGradient id="hGate" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#DCC070"/>'
  '<stop offset="50%"  stop-color="#BEA050"/>'
  '<stop offset="100%" stop-color="#8C7030"/>'
  '</linearGradient>')

# Gate dome cap
A('<radialGradient id="hGateDome" cx="35%" cy="30%" r="65%">'
  '<stop offset="0%"   stop-color="#5AB0A0"/>'
  '<stop offset="55%"  stop-color="#388880"/>'
  '<stop offset="100%" stop-color="#246060"/>'
  '</radialGradient>')

# Stone ruins / columns
A('<linearGradient id="hRuin" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#9A8460"/>'
  '<stop offset="50%"  stop-color="#7A6440"/>'
  '<stop offset="100%" stop-color="#5A4828"/>'
  '</linearGradient>')

# Brazier flame
A('<radialGradient id="hFlame" cx="50%" cy="80%" r="60%">'
  '<stop offset="0%"   stop-color="#FFEE80" stop-opacity="0.90"/>'
  '<stop offset="40%"  stop-color="#FF9020" stop-opacity="0.70"/>'
  '<stop offset="100%" stop-color="#CC4408" stop-opacity="0"/>'
  '</radialGradient>')

# Foreground rock
A('<linearGradient id="hRock" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#B04020"/>'
  '<stop offset="50%"  stop-color="#8C2E10"/>'
  '<stop offset="100%" stop-color="#5A1C08"/>'
  '</linearGradient>')

A('</defs>')

# ═══ SKY ══════════════════════════════════════════════════════════════
A('<rect width="400" height="600" fill="url(#hSky)"/>')
A('<rect width="400" height="600" fill="url(#hSun)"/>')
# Heat haze bands near horizon
A('<rect y="108" width="400" height="38" fill="url(#hHeat)"/>')
A('<rect y="118" width="400" height="18" fill="#F0C060" opacity="0.18"/>')

# ── Cirrus clouds (thin wisps, high altitude desert sky) ───────────────
for pts, sw, op in [
    ('M20,28 Q80,22 140,28 Q180,24 220,30',  2.0, 0.38),
    ('M30,36 Q70,30 100,36 Q128,32 150,38',  1.5, 0.28),
    ('M200,18 Q260,12 320,18 Q360,15 390,20', 2.2, 0.42),
    ('M220,28 Q270,22 310,28 Q345,25 380,30', 1.6, 0.32),
    ('M80,46 Q130,40 180,46',                 1.4, 0.28),
    ('M240,42 Q290,36 340,42',                1.4, 0.26),
    ('M10,54 Q60,50 100,54',                  1.2, 0.22),
    ('M300,50 Q350,46 400,50',                1.2, 0.20),
]:
    A(f'<path d="{pts}" stroke="#E8E4D8" stroke-width="{sw}" fill="none" opacity="{op}"/>')

# ═══ DISTANT BACKGROUND MESAS ═════════════════════════════════════════
# Furthest layer (smallest, most atmospheric — almost colour of sky)
A('<polygon points="110,148 140,108 175,118 200,100 225,115 265,106 296,120 310,148" '
  'fill="#B05828" opacity="0.42"/>')
A('<polygon points="115,148 142,116 168,126 185,110 210,120 240,109 268,122 298,148" '
  'fill="#C86030" opacity="0.28"/>')
# Mid-distance mesas (a bit more saturated, larger)
A('<polygon points="82,158 110,118 136,128 158,110 172,118 182,158" fill="#A84820" opacity="0.55"/>')
A('<polygon points="218,158 232,112 252,122 270,108 292,120 316,158" fill="#A84820" opacity="0.52"/>')
# Strata on distant mesas
for y, op in [(128,0.30),(138,0.26),(148,0.22)]:
    A(f'<line x1="82" y1="{y}" x2="182" y2="{y}" stroke="#8A3810" stroke-width="1.2" opacity="{op}"/>')
    A(f'<line x1="218" y1="{y}" x2="316" y2="{y}" stroke="#8A3810" stroke-width="1.2" opacity="{op}"/>')

# ═══ LEFT SANDSTONE CLIFF / MESA ══════════════════════════════════════
# Main cliff body (flat-topped mesa)
A('<polygon points="0,0 0,600 100,600 100,350 140,158 140,0" fill="url(#hMesa)"/>')
# Top surface (slightly separate colour)
A('<rect x="0" y="0" width="140" height="8" fill="url(#hMesaTop)" opacity="0.85"/>')
# Left edge deep shadow
A('<polygon points="0,0 0,600 18,600 18,0" fill="#180802" opacity="0.50"/>')
# Inner face shadow overlay
A('<polygon points="0,0 140,158 100,350 100,600 115,600 115,358 148,164 148,0" '
  'fill="#5A2008" opacity="0.32"/>')
# Cliff face right-edge shadow
A('<rect x="132" y="0" width="8" height="158" fill="#2A1004" opacity="0.40"/>')

# Strata bands across cliff face (horizontal geological layers)
strata_L = [
    (28, '#E07848', 4, 0.70), (52, '#8A3010', 3, 0.55),
    (72, '#D06838', 5, 0.65), (90, '#6A2008', 2.5, 0.52),
    (108,'#C05828', 4, 0.62), (124,'#9A3818', 3, 0.58),
    (140,'#804020', 3.5, 0.50), (155,'#A84A20', 3, 0.48),
]
for sy, col, sw, op in strata_L:
    # Clip strata to the cliff face polygon
    x2 = min(140, max(0, int(140 - (sy / 158.0) * 0)))  # left edge always 0
    A(f'<line x1="0" y1="{sy}" x2="{x2}" y2="{sy}" stroke="{col}" stroke-width="{sw}" opacity="{op}"/>')
# Below the top edge, strata go diagonally with the cliff face
for sy, col, sw, op in [(175,'#C05020',3,0.42),(200,'#904018',2.5,0.38),(230,'#7A3010',2,0.35),(265,'#904020',2.5,0.38),(305,'#7A3010',2,0.33)]:
    # At this y, the right edge of the cliff face is:
    x2 = int(140 - (sy - 158) * (40 / 192.0))  # from 140 at y=158 to 100 at y=350
    x2 = max(100, x2)
    A(f'<line x1="0" y1="{sy}" x2="{x2}" y2="{sy}" stroke="{col}" stroke-width="{sw}" opacity="{op}"/>')

# Wind erosion grooves (diagonal marks on cliff face)
A('<path d="M30,60 Q50,80 40,110 Q30,140 45,165" stroke="#6A2008" stroke-width="2" fill="none" opacity="0.38"/>')
A('<path d="M70,80 Q90,105 80,135 Q72,158 85,180" stroke="#5A1C08" stroke-width="1.5" fill="none" opacity="0.32"/>')
A('<path d="M105,110 Q118,130 112,155 Q108,172 114,192" stroke="#601C08" stroke-width="1.2" fill="none" opacity="0.28"/>')

# ═══ LEFT CLIFF TOP — UL'DAH CITY ════════════════════════════════════
# City wall / rampart along cliff edge
A('<rect x="0"  y="148" width="140" height="14" fill="#D4B878" rx="1"/>')
A('<rect x="0"  y="144" width="140" height="6"  fill="#E8CC88" opacity="0.80"/>')
# Merlons (battlements)
for bx in range(2, 138, 10):
    A(f'<rect x="{bx}" y="136" width="7" height="10" fill="#DCC070" rx="1"/>')
# Gold band on rampart
A('<rect x="0" y="160" width="140" height="3" fill="url(#hGold)" opacity="0.55"/>')

# ── MAIN DOME — Ul'dah's iconic building ───────────────────────────────
# Drum (cylindrical base)
A('<rect x="18" y="90"  width="52" height="58" fill="url(#hBldg)" rx="2"/>')
A('<rect x="16" y="88"  width="56" height="6"  fill="#C8A868" rx="1"/>')
# Dome itself
A('<ellipse cx="44" cy="90" rx="26" ry="26" fill="url(#hDome)"/>')
A('<ellipse cx="44" cy="90" rx="26" ry="14" fill="url(#hDome)" opacity="0.70"/>')
# Dome highlight
A('<ellipse cx="40" cy="78" rx="10" ry="8"  fill="#80D0C0" opacity="0.42"/>')
# Dome gold finial
A('<ellipse cx="44" cy="64" rx="4"  ry="4"  fill="url(#hGold)"/>')
A('<rect x="42"  y="58"  width="4"  height="8"  fill="url(#hGold)"/>')
A('<ellipse cx="44" cy="57" rx="6"  ry="3"  fill="url(#hGold)"/>')
# Drum windows (arched)
A('<rect x="22"  y="98"  width="10" height="14" fill="#A0C8E8" rx="4" opacity="0.78"/>')
A('<rect x="38"  y="98"  width="10" height="14" fill="#A8D0F0" rx="4" opacity="0.74"/>')
A('<rect x="54"  y="98"  width="10" height="14" fill="#A0C8E8" rx="4" opacity="0.78"/>')
# Gold trim bands on drum
A('<rect x="16"  y="120" width="56" height="4"  fill="url(#hGold)" opacity="0.60"/>')
A('<rect x="16"  y="130" width="56" height="3"  fill="url(#hGold)" opacity="0.48"/>')
# Drum stone courses
for y in [96, 104, 112, 118, 124, 130, 136, 142]:
    A(f'<line x1="18" y1="{y}" x2="70" y2="{y}" stroke="#B89050" stroke-width="0.8" opacity="0.30"/>')

# ── LEFT MINARET 1 (tall, thin tower) ─────────────────────────────────
A('<rect x="82"  y="72"  width="14" height="82" fill="url(#hBldg)" rx="1"/>')
A('<rect x="80"  y="70"  width="18" height="5"  fill="#C8A868" rx="1"/>')
# Minaret pointed cap
A('<polygon points="80,72 100,72 89,52" fill="url(#hGold)"/>')
A('<polygon points="82,72 98,72 89,56" fill="#FFD050" opacity="0.50"/>')
# Balcony
A('<rect x="78"  y="108" width="22" height="5"  fill="#D4B870" rx="1"/>')
A('<rect x="77"  y="112" width="24" height="3"  fill="url(#hGold)" opacity="0.52"/>')
# Windows
A('<rect x="86"  y="80"  width="6"  height="9"  fill="#A8C8E8" rx="2" opacity="0.72"/>')
A('<rect x="86"  y="96"  width="6"  height="8"  fill="#A0C0E0" rx="2" opacity="0.66"/>')
A('<rect x="86"  y="120" width="6"  height="8"  fill="#A0C0E0" rx="2" opacity="0.60"/>')
# Stone courses
for y in [80, 90, 100, 108, 116, 125, 134]:
    A(f'<line x1="82" y1="{y}" x2="96" y2="{y}" stroke="#B89050" stroke-width="0.7" opacity="0.28"/>')

# ── LEFT MINARET 2 (shorter) ─────────────────────────────────────────
A('<rect x="106" y="86"  width="12" height="68" fill="#EAD598" rx="1"/>')
A('<rect x="104" y="84"  width="16" height="5"  fill="#C8A868" rx="1"/>')
A('<polygon points="104,86 120,86 112,68" fill="url(#hGold)"/>')
A('<polygon points="106,86 118,86 112,71" fill="#FFD050" opacity="0.48"/>')
A('<rect x="109"  y="94"  width="6"  height="8"  fill="#A0C0E0" rx="2" opacity="0.68"/>')
A('<rect x="109"  y="108" width="6"  height="7"  fill="#A0C0E0" rx="2" opacity="0.62"/>')
A('<rect x="103" y="118" width="18" height="4"  fill="#D4B870" rx="1"/>')

# ── CONNECTING BUILDINGS ─────────────────────────────────────────────
# Large sandstone hall behind towers
A('<rect x="0"   y="102" width="22" height="62" fill="#D8C280" rx="1"/>')
A('<rect x="0"   y="100" width="22" height="5"  fill="#C4A868" rx="1"/>')
A('<rect x="4"   y="108" width="7"  height="10" fill="#A0C0E0" rx="2" opacity="0.66"/>')
A('<rect x="4"   y="124" width="7"  height="9"  fill="#A0C0E0" rx="2" opacity="0.60"/>')
for bx in [0, 6, 12, 18]:
    A(f'<rect x="{bx}" y="96" width="5" height="7" fill="#C4A868" rx="1"/>')

# ── UL'DAH WALL DETAILS ───────────────────────────────────────────────
# Flag/standard (gold)
A('<rect x="122" y="108" width="3"  height="28" fill="#8A6028" opacity="0.80"/>')
A('<polygon points="125,108 138,114 125,120" fill="#C89020" opacity="0.88"/>')
A('<polygon points="125,108 138,114 125,120" fill="none" stroke="#FFD040" stroke-width="0.8" opacity="0.60"/>')
# Arched gate in city wall
A('<rect x="58"  y="138" width="18" height="24" fill="#C8A060" rx="8" opacity="0.80"/>')
A('<rect x="61"  y="140" width="12" height="20" fill="#5A3010" rx="6" opacity="0.60"/>')

# ═══ RIGHT SANDSTONE CLIFF / MESA ═════════════════════════════════════
A('<polygon points="400,0 400,600 300,600 300,345 260,150 260,0" fill="url(#hMesa)"/>')
A('<rect x="260" y="0"  width="140" height="8"  fill="url(#hMesaTop)" opacity="0.85"/>')
A('<polygon points="400,0 400,600 382,600 382,0" fill="#180802" opacity="0.48"/>')
A('<polygon points="400,0 260,150 300,345 300,600 285,600 285,352 252,158 252,0" '
  'fill="#5A2008" opacity="0.28"/>')
A('<rect x="260" y="0"  width="8"   height="150" fill="#2A1004" opacity="0.38"/>')

# Right cliff strata
for sy, col, sw, op in strata_L:
    A(f'<line x1="260" y1="{sy}" x2="400" y2="{sy}" stroke="{col}" stroke-width="{sw}" opacity="{op}"/>')
for sy, col, sw, op in [(175,'#C05020',3,0.40),(200,'#904018',2.5,0.36),(230,'#7A3010',2,0.33),(265,'#904020',2.5,0.36),(305,'#7A3010',2,0.31)]:
    x1 = int(260 + (sy - 150) * (40 / 195.0))
    x1 = min(300, x1)
    A(f'<line x1="{x1}" y1="{sy}" x2="400" y2="{sy}" stroke="{col}" stroke-width="{sw}" opacity="{op}"/>')
A('<path d="M370,58 Q350,82 360,114 Q370,142 355,165" stroke="#6A2008" stroke-width="2"   fill="none" opacity="0.36"/>')
A('<path d="M328,80 Q310,108 320,138 Q328,160 316,184"  stroke="#5A1C08" stroke-width="1.5" fill="none" opacity="0.30"/>')
A('<path d="M288,110 Q282,132 286,156 Q290,175 282,196"  stroke="#601C08" stroke-width="1.2" fill="none" opacity="0.26"/>')

# ═══ RIGHT CLIFF TOP — UL'DAH CITY ═══════════════════════════════════
A('<rect x="260" y="140" width="140" height="14" fill="#D4B878" rx="1"/>')
A('<rect x="260" y="136" width="140" height="6"  fill="#E8CC88" opacity="0.78"/>')
for bx in range(262, 398, 10):
    A(f'<rect x="{bx}" y="128" width="7" height="10" fill="#DCC070" rx="1"/>')
A('<rect x="260" y="152" width="140" height="3" fill="url(#hGold)" opacity="0.52"/>')

# ── RIGHT MAIN TOWER (square, with dome) ────────────────────────────
A('<rect x="266" y="84"  width="44" height="60" fill="url(#hBldg)" rx="1"/>')
A('<rect x="264" y="82"  width="48" height="6"  fill="#C8A868" rx="1"/>')
A('<ellipse cx="288" cy="84" rx="22" ry="22" fill="url(#hDome)"/>')
A('<ellipse cx="288" cy="84" rx="22" ry="12" fill="url(#hDome)" opacity="0.65"/>')
A('<ellipse cx="285" cy="74" rx="8"  ry="6"  fill="#80D0C0" opacity="0.40"/>')
A('<ellipse cx="288" cy="62" rx="3.5" ry="3.5" fill="url(#hGold)"/>')
A('<rect x="286" y="56"  width="4"  height="8"  fill="url(#hGold)"/>')
A('<ellipse cx="288" cy="55" rx="5"  ry="2.5" fill="url(#hGold)"/>')
for bx, by in [(270,92),(282,92),(296,92)]:
    A(f'<rect x="{bx}" y="{by}" width="8" height="12" fill="#A8C8E8" rx="4" opacity="0.74"/>')
A('<rect x="264" y="112" width="48" height="4"  fill="url(#hGold)" opacity="0.58"/>')
A('<rect x="264" y="122" width="48" height="3"  fill="url(#hGold)" opacity="0.46"/>')
for y in [90, 98, 106, 112, 118, 126, 132, 138]:
    A(f'<line x1="266" y1="{y}" x2="310" y2="{y}" stroke="#B89050" stroke-width="0.8" opacity="0.28"/>')

# ── RIGHT MINARET 1 ──────────────────────────────────────────────────
A('<rect x="316" y="78"  width="14" height="76" fill="url(#hBldg)" rx="1"/>')
A('<rect x="314" y="76"  width="18" height="5"  fill="#C8A868" rx="1"/>')
A('<polygon points="314,78 332,78 323,58" fill="url(#hGold)"/>')
A('<polygon points="316,78 330,78 323,62" fill="#FFD050" opacity="0.48"/>')
A('<rect x="312" y="112" width="22" height="5"  fill="#D4B870" rx="1"/>')
A('<rect x="312" y="116" width="22" height="3"  fill="url(#hGold)" opacity="0.50"/>')
A('<rect x="320" y="86"  width="6"  height="8"  fill="#A8C8E8" rx="2" opacity="0.70"/>')
A('<rect x="320" y="100" width="6"  height="7"  fill="#A0C0E0" rx="2" opacity="0.64"/>')
A('<rect x="320" y="122" width="6"  height="7"  fill="#A0C0E0" rx="2" opacity="0.58"/>')

# ── RIGHT MINARET 2 ──────────────────────────────────────────────────
A('<rect x="340" y="90"  width="12" height="64" fill="#EAD598" rx="1"/>')
A('<rect x="338" y="88"  width="16" height="5"  fill="#C8A868" rx="1"/>')
A('<polygon points="338,90 354,90 346,72" fill="url(#hGold)"/>')
A('<rect x="343" y="98"  width="5"  height="7"  fill="#A0C0E0" rx="2" opacity="0.66"/>')
A('<rect x="343" y="112" width="5"  height="6"  fill="#A0C0E0" rx="2" opacity="0.60"/>')

# ── RIGHT WALL DETAILS ────────────────────────────────────────────────
A('<rect x="362" y="104" width="22" height="58" fill="#D8C280" rx="1"/>')
A('<rect x="362" y="102" width="22" height="5"  fill="#C4A868" rx="1"/>')
A('<rect x="366" y="110" width="7"  height="9"  fill="#A0C0E0" rx="2" opacity="0.64"/>')
A('<rect x="366" y="124" width="7"  height="8"  fill="#A0C0E0" rx="2" opacity="0.58"/>')
# Flag
A('<rect x="276" y="104" width="3"  height="28" fill="#8A6028" opacity="0.78"/>')
A('<polygon points="279,104 292,110 279,116" fill="#C89020" opacity="0.86"/>')
# Arched gate in right city wall
A('<rect x="324" y="130" width="18" height="22" fill="#C8A060" rx="8" opacity="0.78"/>')
A('<rect x="327" y="132" width="12" height="18" fill="#5A3010" rx="6" opacity="0.58"/>')

# ═══ DESERT FLOOR ═════════════════════════════════════════════════════
A('<rect y="340" width="400" height="260" fill="url(#hSand)"/>')
# Sand dune ripple lines
A('<g stroke="#B87820" stroke-width="1.0" opacity="0.30">')
for y in range(355, 601, 14):
    A(f'<path d="M0,{y} Q80,{y-5} 160,{y} Q240,{y+5} 320,{y} Q360,{y-3} 400,{y}"/>')
A('</g>')
# Dune crest highlights
for y, op in [(348,0.28),(370,0.24),(396,0.20),(425,0.18),(458,0.16),(490,0.14)]:
    A(f'<path d="M0,{y} Q100,{y-6} 200,{y} Q300,{y+6} 400,{y}" stroke="#E8B840" stroke-width="1.5" fill="none" opacity="{op}"/>')
# Cracked earth texture (center, where it's driest)
A('<g stroke="#8A5818" stroke-width="0.8" opacity="0.22">')
for cx, cy in [(140,380),(180,410),(220,390),(160,440),(240,460),(200,500),(130,520),(270,510)]:
    for ang in [0, 60, 120]:
        rad = math.radians(ang)
        A(f'<line x1="{cx}" y1="{cy}" x2="{cx+int(18*math.cos(rad))}" y2="{cy+int(18*math.sin(rad))}"/>')
A('</g>')
# Sand color variation patches
for cx, cy, rx, ry, op in [(80,380,50,18,0.22),(200,420,70,20,0.18),(330,388,55,16,0.20),
                             (130,470,48,15,0.18),(270,490,52,16,0.16),(200,540,65,18,0.15)]:
    A(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#A86818" opacity="{op}"/>')

# ═══ CANYON WALLS (cliff faces visible from below) ════════════════════
# Below the main cliff body, the inner cliff face continues as foreground walls
# Left canyon wall (foreground)
A('<rect x="0"   y="0"   width="68" height="600" fill="url(#hRock)"/>')
A('<rect x="0"   y="0"   width="14" height="600" fill="#180802" opacity="0.48"/>')
A('<rect x="56"  y="0"   width="12" height="600" fill="#280C04" opacity="0.35"/>')
# Left wall strata
for y in range(0, 601, 22):
    A(f'<rect x="0" y="{y}" width="68" height="10" fill="#C04C20" opacity="0.18"/>')
A('<line x1="34" y1="0" x2="34" y2="600" stroke="#5A2008" stroke-width="1" opacity="0.22"/>')
# Left wall rock surface grooves
for y, op in [(55,0.38),(130,0.34),(215,0.30),(305,0.27),(400,0.25),(500,0.22)]:
    A(f'<path d="M10,{y} Q24,{y+4} 40,{y} Q52,{y-3} 65,{y}" stroke="#6A2808" stroke-width="2" fill="none" opacity="{op}"/>')
# Left wall desert lichen / mineral streaks
A('<path d="M0,200 Q18,210 14,260 Q10,310 20,370" stroke="#8A6030" stroke-width="3" fill="none" opacity="0.25"/>')
A('<path d="M30,180 Q44,195 40,240 Q36,280 48,330" stroke="#7A5020" stroke-width="2" fill="none" opacity="0.20"/>')

# Right canyon wall (foreground)
A('<rect x="332" y="0"   width="68" height="600" fill="url(#hRock)"/>')
A('<rect x="386" y="0"   width="14" height="600" fill="#180802" opacity="0.45"/>')
A('<rect x="332" y="0"   width="12" height="600" fill="#280C04" opacity="0.32"/>')
for y in range(0, 601, 22):
    A(f'<rect x="332" y="{y}" width="68" height="10" fill="#C04C20" opacity="0.18"/>')
A('<line x1="366" y1="0" x2="366" y2="600" stroke="#5A2008" stroke-width="1" opacity="0.20"/>')
for y, op in [(65,0.36),(145,0.32),(230,0.28),(320,0.25),(415,0.23),(510,0.20)]:
    A(f'<path d="M335,{y} Q348,{y+4} 362,{y} Q376,{y-3} 397,{y}" stroke="#6A2808" stroke-width="2" fill="none" opacity="{op}"/>')
A('<path d="M400,210 Q382,222 386,275 Q390,325 380,385" stroke="#8A6030" stroke-width="3" fill="none" opacity="0.23"/>')

# Crenellated tops on canyon walls
A('<rect x="0"   y="148" width="68" height="14" fill="#D4B070" rx="1" opacity="0.90"/>')
for bx in range(0, 66, 9):
    A(f'<rect x="{bx}" y="136" width="7" height="14" fill="#D0AC60" rx="1" opacity="0.88"/>')
A('<rect x="0"   y="162" width="68" height="3"  fill="url(#hGold)" opacity="0.48"/>')

A('<rect x="332" y="136" width="68" height="14" fill="#D4B070" rx="1" opacity="0.88"/>')
for bx in range(333, 398, 9):
    A(f'<rect x="{bx}" y="124" width="7" height="14" fill="#D0AC60" rx="1" opacity="0.86"/>')
A('<rect x="332" y="150" width="68" height="3"  fill="url(#hGold)" opacity="0.46"/>')

# ═══ ANCIENT RUINS ON DESERT FLOOR ════════════════════════════════════
# Fallen Belah'dian columns and archway fragments
# Tall standing columns
for cx, cy_base, h, w in [(102,358,68,12),(118,362,52,10),(282,354,72,12),(298,360,48,10)]:
    A(f'<rect x="{cx-w//2}" y="{cy_base-h}" width="{w}" height="{h}" fill="url(#hRuin)" rx="1"/>')
    A(f'<rect x="{cx-w//2-2}" y="{cy_base-h}" width="{w+4}" height="7" fill="#A8906A" rx="1"/>')  # capital
    A(f'<rect x="{cx-w//2-2}" y="{cy_base-6}" width="{w+4}" height="6" fill="#A8906A" rx="1"/>')  # base
    # Column fluting
    for fx in [cx-3, cx, cx+3]:
        A(f'<line x1="{fx}" y1="{cy_base-h+7}" x2="{fx}" y2="{cy_base-6}" stroke="#6A5030" stroke-width="0.8" opacity="0.30"/>')

# Broken arch fragment (center-left)
A('<path d="M108,358 Q130,316 152,358" stroke="#8A7050" stroke-width="12" fill="none" stroke-linecap="butt" opacity="0.72"/>')
A('<path d="M108,358 Q130,316 152,358" stroke="url(#hRuin)" stroke-width="8"  fill="none" stroke-linecap="butt"/>')
A('<path d="M110,356 Q130,318 150,356" stroke="#A89068" stroke-width="2"  fill="none" stroke-linecap="butt" opacity="0.35"/>')

# Broken arch right side
A('<path d="M248,354 Q270,310 292,354" stroke="#8A7050" stroke-width="12" fill="none" stroke-linecap="butt" opacity="0.68"/>')
A('<path d="M248,354 Q270,310 292,354" stroke="url(#hRuin)" stroke-width="8"  fill="none" stroke-linecap="butt"/>')

# Fallen column (horizontal)
A('<rect x="110" y="400" width="60" height="10" fill="url(#hRuin)" rx="3" opacity="0.70"/>')
A('<rect x="108" y="399" width="64" height="4"  fill="#A8906A" rx="2" opacity="0.48"/>')
# Column drum sections
for x in [110, 132, 154]:
    A(f'<line x1="{x}" y1="400" x2="{x}" y2="410" stroke="#6A5030" stroke-width="1.2" opacity="0.38"/>')

A('<rect x="230" y="408" width="58" height="9"  fill="url(#hRuin)" rx="3" opacity="0.66"/>')
A('<rect x="228" y="407" width="62" height="4"  fill="#A8906A" rx="2" opacity="0.45"/>')

# Stone block rubble
for rx, ry, rw, rh, op in [(130,430,18,8,0.54),(155,438,12,6,0.48),(245,432,16,7,0.52),(270,440,10,6,0.46),
                             (160,470,14,6,0.44),(220,476,16,7,0.46),(190,500,18,8,0.40),(200,528,12,6,0.38)]:
    A(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" fill="url(#hRuin)" rx="1" opacity="{op}"/>')

# ═══ DESERT SCRUB VEGETATION ════════════════════════════════════════
# Dry desert plants (hardy scrub that survives Thanalan heat)
def desert_scrub(ax, ay, scale=1.0):
    parts = []
    # Main stems
    for ang, ln in [(-80,22),(-50,28),(-20,32),(10,30),(40,26),(70,20)]:
        rad = math.radians(ang)
        ex = ax + int(math.cos(rad) * ln * scale)
        ey = ay + int(math.sin(rad) * ln * scale * 0.6)
        parts.append(f'<path d="M{ax},{ay} Q{ax+int(math.cos(rad)*ln*scale*0.5)},{ay-int(8*scale)},{ex},{ey}" '
                     f'stroke="#6A6028" stroke-width="{1.4*scale:.1f}" fill="none" opacity="0.68"/>')
        # Leaf tip
        if abs(ang) < 60:
            parts.append(f'<ellipse cx="{ex}" cy="{ey}" rx="{int(3*scale)}" ry="{int(2*scale)}" fill="#585820" opacity="0.60"/>')
    return ''.join(parts)

# Left side scrub
A(desert_scrub(76, 366, 0.85))
A(desert_scrub(90, 380, 0.72))
A(desert_scrub(78, 430, 0.78))
A(desert_scrub(86, 490, 0.70))
# Right side scrub
A(desert_scrub(324, 370, 0.85))
A(desert_scrub(312, 388, 0.72))
A(desert_scrub(318, 438, 0.78))
A(desert_scrub(310, 496, 0.70))
# Center/midground scrub
A(desert_scrub(126, 448, 0.60))
A(desert_scrub(278, 454, 0.62))
A(desert_scrub(164, 510, 0.55))
A(desert_scrub(244, 516, 0.58))
# Small dust-hardy shrubs (ellipses)
for cx, cy, rx, ry, op in [(98,368,12,5,0.42),(86,428,10,4,0.38),(312,374,11,4,0.40),(322,432,10,4,0.36),
                             (138,456,8,3,0.35),(262,462,9,3,0.34),(176,524,8,3,0.32),(228,530,7,3,0.30)]:
    A(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#545824" opacity="{op}"/>')

# ═══ STAGE 5 — Desert Eternal Flame / Nald'thal Beacon (translate +52) ═
A('<g transform="translate(52,0)">')

# Tiered stone pedestal base
A('<rect x="183" y="275" width="34" height="8"  fill="url(#hRuin)" rx="1" opacity="0.90"/>')
A('<rect x="187" y="267" width="26" height="10" fill="#A08860" rx="1" opacity="0.85"/>')
A('<rect x="190" y="260" width="20" height="9"  fill="#B09470" rx="1" opacity="0.80"/>')
A('<rect x="193" y="255" width="14" height="7"  fill="#C0A278" rx="1" opacity="0.76"/>')
# Pedestal carved band (Ul'dahn inscription)
A('<rect x="184" y="276" width="32" height="2"  fill="url(#hGold)" opacity="0.50"/>')
A('<rect x="188" y="268" width="24" height="2"  fill="url(#hGold)" opacity="0.44"/>')
# Rune marks on pedestal
for rx, ry in [(188,272),(196,272),(204,272),(212,272)]:
    A(f'<rect x="{rx}" y="{ry}" width="3" height="2" fill="#A07020" opacity="0.50"/>')

# Iron brazier stand
A('<rect x="197" y="234" width="6"  height="24" fill="#383028" rx="1"/>')
A('<rect x="197" y="234" width="2"  height="24" fill="#504840" opacity="0.40"/>')
# Brazier legs (3 prongs splaying outward at bottom)
A('<path d="M200,256 Q190,262 184,268" stroke="#383028" stroke-width="4" fill="none" stroke-linecap="round"/>')
A('<path d="M200,256 Q200,264 200,272" stroke="#383028" stroke-width="4" fill="none" stroke-linecap="round"/>')
A('<path d="M200,256 Q210,262 216,268" stroke="#383028" stroke-width="4" fill="none" stroke-linecap="round"/>')
# Leg tips (ball feet)
A('<circle cx="184" cy="268" r="3" fill="#504840"/>')
A('<circle cx="200" cy="272" r="3" fill="#504840"/>')
A('<circle cx="216" cy="268" r="3" fill="#504840"/>')
# Brazier bowl
A('<ellipse cx="200" cy="232" rx="18" ry="8"  fill="#3A3028"/>')
A('<ellipse cx="200" cy="228" rx="18" ry="8"  fill="#484038"/>')
A('<ellipse cx="200" cy="226" rx="16" ry="6"  fill="#282018"/>')
# Gold rim on bowl
A('<ellipse cx="200" cy="228" rx="18" ry="8"  fill="none" stroke="#C08018" stroke-width="2" opacity="0.65"/>')
A('<ellipse cx="200" cy="224" rx="16" ry="6"  fill="none" stroke="#E0A020" stroke-width="1.2" opacity="0.50"/>')

# ETERNAL FLAME (large, dramatic)
# Outer glow halo
A('<ellipse cx="200" cy="195" rx="44" ry="50" fill="url(#hFlame)" opacity="0.55"/>')
A('<ellipse cx="200" cy="200" rx="30" ry="38" fill="#FF7010" opacity="0.22"/>')
# Main flame body (layered ellipses forming flame shape)
A('<ellipse cx="200" cy="218" rx="14" ry="20" fill="#FF8818" opacity="0.90"/>')
A('<ellipse cx="200" cy="210" rx="11" ry="18" fill="#FFA020" opacity="0.88"/>')
A('<ellipse cx="200" cy="202" rx="9"  ry="16" fill="#FFB830" opacity="0.85"/>')
A('<ellipse cx="200" cy="194" rx="7"  ry="14" fill="#FFD040" opacity="0.82"/>')
A('<ellipse cx="200" cy="186" rx="5"  ry="11" fill="#FFE858" opacity="0.80"/>')
A('<ellipse cx="200" cy="178" rx="3.5" ry="8" fill="#FFF070" opacity="0.78"/>')
# Flame tendrils (licking sides)
A('<path d="M192,222 Q184,210 188,196 Q192,182 186,172" stroke="#FF8818" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.65"/>')
A('<path d="M208,222 Q216,208 212,194 Q208,180 214,170" stroke="#FF8818" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.62"/>')
A('<path d="M196,218 Q190,200 194,184 Q198,168 192,158" stroke="#FFA020" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.52"/>')
A('<path d="M204,218 Q210,200 206,184 Q202,168 208,156" stroke="#FFA020" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.50"/>')
# Inner bright core
A('<ellipse cx="200" cy="212" rx="6"  ry="10" fill="#FFFAE0" opacity="0.75"/>')
A('<ellipse cx="200" cy="210" rx="3"  ry="6"  fill="#FFFFFF"  opacity="0.50"/>')
# Flame glow on pedestal / ground
A('<ellipse cx="200" cy="270" rx="30" ry="8"  fill="#FF9020" opacity="0.22"/>')
A('<ellipse cx="200" cy="278" rx="22" ry="5"  fill="#FFB040" opacity="0.16"/>')
# Floating embers
for ex, ey, er, eop in [(192,168,1.8,0.68),(206,162,2.0,0.72),(196,155,1.6,0.60),
                          (204,175,1.4,0.55),(188,178,1.8,0.62),(212,180,1.6,0.58)]:
    A(f'<circle cx="{ex}" cy="{ey}" r="{er}" fill="#FF8020" opacity="{eop}"/>')
    A(f'<circle cx="{ex}" cy="{ey}" r="{er*0.5:.1f}" fill="#FFE040" opacity="{eop*0.7:.2f}"/>')

A('</g>')  # end translate(52,0)

# ═══ STAGE 10 — Ul'dah Grand Gate (×1.5) ════════════════════════════
A('<g transform="translate(200,531) scale(1.5) translate(-200,-531)">')

# Gate shadow on sand
A('<ellipse cx="200" cy="578" rx="76" ry="14" fill="#4A2808" opacity="0.55"/>')

# ── LEFT PILLAR ──────────────────────────────────────────────────────
A('<rect x="134" y="470" width="40" height="102" fill="url(#hGateL)" rx="2"/>')
# Stone courses
for y in range(478, 572, 10):
    A(f'<rect x="134" y="{y}" width="40" height="5" fill="#C8A060" opacity="0.25"/>')
# Lit edge highlight
A('<rect x="136" y="470" width="8"  height="102" fill="#FAE8A8" opacity="0.20"/>')
# Shadow edge
A('<rect x="166" y="470" width="8"  height="102" fill="#2A1A04" opacity="0.28"/>')
# Gold trim bands (Ul'dahn decorative banding)
for y in [478, 498, 518, 538, 558]:
    A(f'<rect x="132" y="{y}" width="44" height="4" fill="url(#hGold)" rx="1" opacity="0.60"/>')
# Carved panel (inscriptions)
A('<rect x="140" y="484" width="28" height="46" fill="#C8A858" rx="1" opacity="0.30"/>')
for ry in [488, 496, 504, 512, 520]:
    A(f'<rect x="144" y="{ry}" width="20" height="2" fill="#B89040" opacity="0.42"/>')
    A(f'<rect x="148" y="{ry-4}" width="8"  height="3" fill="#A07828" opacity="0.35"/>')
# Pillar cap (two layers — onion dome)
A('<rect x="130" y="462" width="48" height="10" fill="#D4B070" rx="2"/>')
A('<rect x="126" y="456" width="56" height="8"  fill="#E0BC78" rx="2"/>')
# ONION DOME cap on pillar top
A('<ellipse cx="154" cy="442" rx="20" ry="20" fill="url(#hGateDome)"/>')
A('<ellipse cx="154" cy="428" rx="12" ry="18" fill="url(#hGateDome)" opacity="0.75"/>')
A('<ellipse cx="154" cy="422" rx="8"  ry="12" fill="#62B0A0" opacity="0.60"/>')
# Dome finial
A('<rect x="152" y="408" width="4"  height="15" fill="url(#hGold)"/>')
A('<ellipse cx="154" cy="407" rx="6"  ry="3"   fill="url(#hGold)"/>')
A('<ellipse cx="154" cy="404" rx="3"  ry="3"   fill="#FFD050" opacity="0.70"/>')
# Dome highlight
A('<ellipse cx="150" cy="430" rx="6"  ry="8"   fill="#80D0C0" opacity="0.40"/>')

# ── RIGHT PILLAR ─────────────────────────────────────────────────────
A('<rect x="226" y="470" width="40" height="102" fill="url(#hGate)" rx="2"/>')
for y in range(478, 572, 10):
    A(f'<rect x="226" y="{y}" width="40" height="5" fill="#C8A060" opacity="0.25"/>')
A('<rect x="228" y="470" width="8"  height="102" fill="#FAE8A8" opacity="0.15"/>')
A('<rect x="258" y="470" width="8"  height="102" fill="#2A1A04" opacity="0.25"/>')
for y in [478, 498, 518, 538, 558]:
    A(f'<rect x="224" y="{y}" width="44" height="4" fill="url(#hGold)" rx="1" opacity="0.58"/>')
A('<rect x="232" y="484" width="28" height="46" fill="#C8A858" rx="1" opacity="0.28"/>')
for ry in [488, 496, 504, 512, 520]:
    A(f'<rect x="236" y="{ry}" width="20" height="2" fill="#B89040" opacity="0.40"/>')
    A(f'<rect x="240" y="{ry-4}" width="8"  height="3" fill="#A07828" opacity="0.32"/>')
A('<rect x="222" y="462" width="48" height="10" fill="#D4B070" rx="2"/>')
A('<rect x="218" y="456" width="56" height="8"  fill="#E0BC78" rx="2"/>')
# Right onion dome cap
A('<ellipse cx="246" cy="442" rx="20" ry="20" fill="url(#hGateDome)"/>')
A('<ellipse cx="246" cy="428" rx="12" ry="18" fill="url(#hGateDome)" opacity="0.75"/>')
A('<ellipse cx="246" cy="422" rx="8"  ry="12" fill="#62B0A0" opacity="0.58"/>')
A('<rect x="244" y="408" width="4"  height="15" fill="url(#hGold)"/>')
A('<ellipse cx="246" cy="407" rx="6"  ry="3"   fill="url(#hGold)"/>')
A('<ellipse cx="246" cy="404" rx="3"  ry="3"   fill="#FFD050" opacity="0.68"/>')
A('<ellipse cx="242" cy="430" rx="6"  ry="8"   fill="#80D0C0" opacity="0.38"/>')

# ── MAIN POINTED ARCH (Mamluk/Ul'dahn style) ─────────────────────────
# Outer silhouette (dark, thick)
A('<path d="M132,498 Q154,444 200,434 Q246,444 268,498" stroke="#2A1A04" stroke-width="26" fill="none" stroke-linecap="butt"/>')
# Arch face (gradient stone)
A('<path d="M132,498 Q154,444 200,434 Q246,444 268,498" stroke="url(#hGate)" stroke-width="21" fill="none" stroke-linecap="butt"/>')
# Arch highlight (sun-lit top edge)
A('<path d="M134,496 Q155,446 200,436 Q245,446 266,496" stroke="#F0DC98" stroke-width="4.5" fill="none" stroke-linecap="butt" opacity="0.36"/>')
# Inner arch shadow
A('<path d="M146,498 Q166,450 200,442 Q234,450 254,498" stroke="#1A1002" stroke-width="6"   fill="none" stroke-linecap="butt" opacity="0.55"/>')
# Gold trim lines on arch (decorative banding)
A('<path d="M134,496 Q155,446 200,436 Q245,446 266,496" stroke="#C89020" stroke-width="2.2" fill="none" stroke-linecap="butt" opacity="0.52"/>')
A('<path d="M140,497 Q160,448 200,439 Q240,448 260,497" stroke="#C89020" stroke-width="1.2" fill="none" stroke-linecap="butt" opacity="0.35"/>')

# Voussoir joints (stone arch joints)
for x1, y1, x2, y2 in [
    (147,492, 155,476),(162,475, 168,460),(175,463, 178,448),
    (190,447, 191,432),(200,445, 200,430),(210,447, 209,432),
    (225,463, 222,448),(238,475, 232,460),(253,492, 245,476)
]:
    A(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#2A1A04" stroke-width="2.2" opacity="0.40"/>')

# ── KEYSTONE — Nald'thal sun/coin emblem ─────────────────────────────
A('<polygon points="193,436 200,422 207,436 205,446 195,446" fill="#C8A840"/>')
A('<polygon points="194,437 200,425 206,437 204,445 196,445" fill="#F0D060" opacity="0.52"/>')
A('<circle cx="200" cy="436" r="5.5" fill="#D4A028" opacity="0.88"/>')
A('<circle cx="200" cy="436" r="3.5" fill="#FFE050" opacity="0.80"/>')
A('<circle cx="200" cy="436" r="1.5" fill="#FFFAE0" opacity="0.90"/>')
# Sun rays from emblem
A('<g stroke="#E8B030" stroke-width="1.2" opacity="0.55">'
  '<line x1="200" y1="428" x2="200" y2="424"/>'
  '<line x1="200" y1="444" x2="200" y2="448"/>'
  '<line x1="192" y1="436" x2="188" y2="436"/>'
  '<line x1="208" y1="436" x2="212" y2="436"/>'
  '<line x1="194" y1="430" x2="191" y2="427"/>'
  '<line x1="206" y1="442" x2="209" y2="445"/>'
  '<line x1="206" y1="430" x2="209" y2="427"/>'
  '<line x1="194" y1="442" x2="191" y2="445"/>'
  '</g>')

# ── GATE DOORS (iron-reinforced wood) ────────────────────────────────
# Left door
A('<polygon points="146,498 200,445 200,572 146,572" fill="#3A2810" opacity="0.82"/>')
A('<polygon points="148,497 200,447 200,570 148,570" fill="#4A3820" opacity="0.35"/>')
# Right door
A('<polygon points="254,498 200,445 200,572 254,572" fill="#2E2008" opacity="0.82"/>')
# Door reinforcement bars (horizontal iron bands)
A('<g stroke="#282018" stroke-width="4" opacity="0.60">'
  '<line x1="148" y1="508" x2="200" y2="494"/>'
  '<line x1="148" y1="528" x2="200" y2="516"/>'
  '<line x1="148" y1="548" x2="200" y2="538"/>'
  '<line x1="148" y1="568" x2="200" y2="560"/>'
  '</g>')
A('<g stroke="#282018" stroke-width="4" opacity="0.56">'
  '<line x1="252" y1="508" x2="200" y2="494"/>'
  '<line x1="252" y1="528" x2="200" y2="516"/>'
  '<line x1="252" y1="548" x2="200" y2="538"/>'
  '<line x1="252" y1="568" x2="200" y2="560"/>'
  '</g>')
# Iron studs on doors
for dy in [502, 518, 534, 550, 566]:
    for dx in [158, 172, 186]:
        A(f'<circle cx="{dx}" cy="{dy}" r="2.5" fill="#484030" opacity="0.60"/>')
    for dx in [214, 228, 242]:
        A(f'<circle cx="{dx}" cy="{dy}" r="2.5" fill="#403828" opacity="0.56"/>')

# ── Flanking torch pillars ────────────────────────────────────────────
# Left torch
A('<rect x="118" y="476" width="12" height="36" fill="#A08050" rx="1" opacity="0.80"/>')
A('<rect x="116" y="510" width="16" height="8"  fill="#8A6838" rx="2" opacity="0.72"/>')
A('<ellipse cx="124" cy="509" rx="9"   ry="4.5" fill="#7A5828"/>')
A('<ellipse cx="124" cy="504" rx="7"   ry="8"   fill="#FF8820" opacity="0.88"/>')
A('<ellipse cx="124" cy="499" rx="5"   ry="6"   fill="#FFA830" opacity="0.84"/>')
A('<ellipse cx="124" cy="494" rx="3.5" ry="4.5" fill="#FFD050" opacity="0.80"/>')
A('<ellipse cx="123" cy="491" rx="2"   ry="3"   fill="#FFFAE0" opacity="0.60"/>')
A('<ellipse cx="118" cy="508" rx="12"  ry="8"   fill="#FF8820" opacity="0.16"/>')
# Right torch
A('<rect x="270" y="476" width="12" height="36" fill="#A08050" rx="1" opacity="0.78"/>')
A('<rect x="268" y="510" width="16" height="8"  fill="#8A6838" rx="2" opacity="0.70"/>')
A('<ellipse cx="276" cy="509" rx="9"   ry="4.5" fill="#7A5828"/>')
A('<ellipse cx="276" cy="504" rx="7"   ry="8"   fill="#FF8820" opacity="0.85"/>')
A('<ellipse cx="276" cy="499" rx="5"   ry="6"   fill="#FFA830" opacity="0.81"/>')
A('<ellipse cx="276" cy="494" rx="3.5" ry="4.5" fill="#FFD050" opacity="0.77"/>')
A('<ellipse cx="275" cy="491" rx="2"   ry="3"   fill="#FFFAE0" opacity="0.58"/>')
A('<ellipse cx="282" cy="508" rx="12"  ry="8"   fill="#FF8820" opacity="0.14"/>')

A('</g>')  # end scale group

# ═══ HEAT SHIMMER OVERLAY (desert floor atmosphere) ════════════════
# Subtle warm glow rising from hot sand
A('<rect y="530" width="400" height="70" fill="#D08020" opacity="0.10"/>')
A('<rect y="560" width="400" height="40" fill="#C07010" opacity="0.14"/>')

A('</svg>')

HARD = ''.join(P)

# ── Inject into stage.html ───────────────────────────────────────────────
pattern = r"(if\(diff==='HARD'\) return ')(.*?)(';)"
replacement = r"\g<1>" + HARD.replace('\\', '\\\\') + r"\g<3>"
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

assert new_content != content, "Injection failed — pattern not matched"
assert "hSky" in new_content, "SVG missing in output"
print(f"HARD SVG: {len(HARD):,} chars injected OK")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("stage.html written.")
