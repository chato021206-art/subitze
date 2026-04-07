#!/usr/bin/env python3
"""gen_extreme.py — EXTREME: Radz-at-Han / Thavnair (FF14 Endwalker) — VIVID edition.
Cobalt domes, gold minarets, tropical palms, market awnings, bunting flags,
colourful tile mosaics, flower terraces, alchemical brazier, grand Hannish gate.
"""
import re as _re, math

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    html = f.read()

parts = []
def A(s): parts.append(s)

# ─────────────────────────────────────────────────────────────────────────────
#  GRADIENTS
# ─────────────────────────────────────────────────────────────────────────────
A('<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"><defs>')

A('<linearGradient id="rSky" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#0E78C8"/>'
  '<stop offset="30%"  stop-color="#2898E0"/>'
  '<stop offset="65%"  stop-color="#58C0F0"/>'
  '<stop offset="100%" stop-color="#A0DEFF"/>'
  '</linearGradient>')

A('<radialGradient id="rSun" cx="82%" cy="8%" r="55%">'
  '<stop offset="0%"   stop-color="#FFFAE0" stop-opacity="0.90"/>'
  '<stop offset="14%"  stop-color="#FFE890" stop-opacity="0.58"/>'
  '<stop offset="32%"  stop-color="#FFD060" stop-opacity="0.28"/>'
  '<stop offset="100%" stop-color="#F8A800" stop-opacity="0"/>'
  '</radialGradient>')

# Bright turquoise ocean
A('<linearGradient id="rOcean" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#18A8D8"/>'
  '<stop offset="50%"  stop-color="#0E80B8"/>'
  '<stop offset="100%" stop-color="#085888"/>'
  '</linearGradient>')

A('<radialGradient id="rOceanShim" cx="70%" cy="20%" r="55%">'
  '<stop offset="0%"   stop-color="#90E8FF" stop-opacity="0.55"/>'
  '<stop offset="45%"  stop-color="#40C0E0" stop-opacity="0.22"/>'
  '<stop offset="100%" stop-color="#1880B8" stop-opacity="0"/>'
  '</radialGradient>')

A('<linearGradient id="rCliffL" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#6A5220"/>'
  '<stop offset="42%"  stop-color="#A87838"/>'
  '<stop offset="78%"  stop-color="#D0A050"/>'
  '<stop offset="100%" stop-color="#E0B060"/>'
  '</linearGradient>')

A('<linearGradient id="rCliffR" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#E0B060"/>'
  '<stop offset="22%"  stop-color="#D0A050"/>'
  '<stop offset="58%"  stop-color="#A87838"/>'
  '<stop offset="100%" stop-color="#6A5220"/>'
  '</linearGradient>')

A('<linearGradient id="rBldg" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#F0D080"/>'
  '<stop offset="45%"  stop-color="#D8B060"/>'
  '<stop offset="100%" stop-color="#B09040"/>'
  '</linearGradient>')

A('<linearGradient id="rBldgSh" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#C09848"/>'
  '<stop offset="55%"  stop-color="#9A7830"/>'
  '<stop offset="100%" stop-color="#786018"/>'
  '</linearGradient>')

# Vivid cobalt dome
A('<radialGradient id="rDome" cx="35%" cy="28%" r="65%">'
  '<stop offset="0%"   stop-color="#90C8FF"/>'
  '<stop offset="25%"  stop-color="#3890F0"/>'
  '<stop offset="55%"  stop-color="#1458C8"/>'
  '<stop offset="85%"  stop-color="#0A38908"/>'
  '<stop offset="100%" stop-color="#082870"/>'
  '</radialGradient>')

A('<linearGradient id="rGold" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FFF8A0"/>'
  '<stop offset="32%"  stop-color="#F0C030"/>'
  '<stop offset="68%"  stop-color="#C89818"/>'
  '<stop offset="100%" stop-color="#906808"/>'
  '</linearGradient>')

A('<linearGradient id="rMinaret" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#A88030"/>'
  '<stop offset="38%"  stop-color="#E8C060"/>'
  '<stop offset="70%"  stop-color="#F8E080"/>'
  '<stop offset="100%" stop-color="#D0A050"/>'
  '</linearGradient>')

# Tropical foliage
A('<linearGradient id="rPalm" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#60C830"/>'
  '<stop offset="45%"  stop-color="#3A9818"/>'
  '<stop offset="100%" stop-color="#206008"/>'
  '</linearGradient>')

A('<linearGradient id="rGnd" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#D0A848"/>'
  '<stop offset="45%"  stop-color="#B89030"/>'
  '<stop offset="100%" stop-color="#907020"/>'
  '</linearGradient>')

A('<linearGradient id="rPalace" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#F8E098"/>'
  '<stop offset="42%"  stop-color="#E8C870"/>'
  '<stop offset="100%" stop-color="#C8A050"/>'
  '</linearGradient>')

A('<linearGradient id="rGateL" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#705820"/>'
  '<stop offset="38%"  stop-color="#C09840"/>'
  '<stop offset="70%"  stop-color="#E8C068"/>'
  '<stop offset="100%" stop-color="#D8B058"/>'
  '</linearGradient>')

A('<linearGradient id="rGateR" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#D8B058"/>'
  '<stop offset="30%"  stop-color="#E8C068"/>'
  '<stop offset="62%"  stop-color="#C09840"/>'
  '<stop offset="100%" stop-color="#705820"/>'
  '</linearGradient>')

A('<radialGradient id="rFlame" cx="50%" cy="70%" r="55%">'
  '<stop offset="0%"   stop-color="#FFFFFF"  stop-opacity="0.92"/>'
  '<stop offset="20%"  stop-color="#FFF080"  stop-opacity="0.85"/>'
  '<stop offset="45%"  stop-color="#FF9010"  stop-opacity="0.65"/>'
  '<stop offset="72%"  stop-color="#FF4800"  stop-opacity="0.35"/>'
  '<stop offset="100%" stop-color="#CC2000"  stop-opacity="0"/>'
  '</radialGradient>')

A('<linearGradient id="rHaze" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#D8A030" stop-opacity="0"/>'
  '<stop offset="60%"  stop-color="#C89028" stop-opacity="0.06"/>'
  '<stop offset="100%" stop-color="#B07818" stop-opacity="0.18"/>'
  '</linearGradient>')

A('<linearGradient id="rVig" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#061018" stop-opacity="0.70"/>'
  '<stop offset="18%"  stop-color="#061018" stop-opacity="0.04"/>'
  '<stop offset="100%" stop-color="#061018" stop-opacity="0"/>'
  '</linearGradient>')

A('</defs>')

# ─────────────────────────────────────────────────────────────────────────────
#  SKY + SUN
# ─────────────────────────────────────────────────────────────────────────────
A('<rect width="400" height="600" fill="url(#rSky)"/>')
A('<rect width="400" height="600" fill="url(#rSun)"/>')
A('<circle cx="328" cy="48" r="40" fill="#FFE030" opacity="0.15"/>')
A('<circle cx="328" cy="48" r="26" fill="#FFF060" opacity="0.28"/>')
A('<circle cx="328" cy="48" r="16" fill="#FFF8A0" opacity="0.82"/>')
A('<circle cx="328" cy="48" r="10" fill="#FFFFFF"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  CLOUDS (vivid white)
# ─────────────────────────────────────────────────────────────────────────────
for cx,cy,cw,ch,op in [(56,36,78,24,0.85),(42,46,50,18,0.75),(185,26,92,28,0.80),
                        (170,38,58,20,0.72),(288,40,72,22,0.70)]:
    A(f'<ellipse cx="{cx}" cy="{cy}" rx="{cw//2}" ry="{ch//2}" fill="#FFFFFF" opacity="{op}"/>')
    A(f'<ellipse cx="{cx-cw//5}" cy="{cy+ch//4}" rx="{cw//3}" ry="{ch//3}" fill="#FFFFFF" opacity="{op*0.88:.2f}"/>')
    A(f'<ellipse cx="{cx+cw//5}" cy="{cy+ch//4}" rx="{cw//4}" ry="{ch//3}" fill="#FFFFFF" opacity="{op*0.80:.2f}"/>')
    A(f'<ellipse cx="{cx}" cy="{cy+ch//2-2}" rx="{cw//2}" ry="5" fill="#C0D8F0" opacity="{op*0.28:.2f}"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  OCEAN / HARBOUR
# ─────────────────────────────────────────────────────────────────────────────
A('<rect x="136" y="0" width="128" height="340" fill="url(#rOcean)"/>')
A('<rect x="136" y="0" width="128" height="340" fill="url(#rOceanShim)"/>')

for wp in ["M136,78  Q152,74 170,78 Q190,82 210,78 Q230,74 264,78",
           "M136,105 Q158,101 180,105 Q202,109 224,105 Q248,101 264,105",
           "M136,136 Q162,132 186,136 Q210,140 234,136 Q254,132 264,136",
           "M136,172 Q164,168 190,172 Q216,176 242,172 Q258,168 264,172",
           "M136,214 Q165,210 192,214 Q218,218 244,214 Q260,210 264,214"]:
    A(f'<path d="{wp}" stroke="#80D8F0" stroke-width="1.4" fill="none" opacity="0.55"/>')
    A(f'<path d="{wp}" stroke="#E0F8FF" stroke-width="0.5" fill="none" opacity="0.60"/>')

# Sun shimmer
A('<path d="M240,55 Q252,110 250,195 Q248,250 246,295" stroke="#FFFFFF" stroke-width="5" fill="none" opacity="0.14"/>')
A('<path d="M242,55 Q254,110 252,195 Q250,250 248,295" stroke="#FFFFFF" stroke-width="1.5" fill="none" opacity="0.22"/>')

# Island silhouette
A('<polygon points="136,210 150,148 172,118 194,132 200,118 206,132 228,116 252,148 264,210" fill="#0A5070" opacity="0.65"/>')

# Distant ship
A('<rect x="170" y="200" width="22" height="5" fill="#4A3818" opacity="0.65"/>')
A('<rect x="179" y="185" width="2.5" height="16" fill="#382808" opacity="0.65"/>')
A('<polygon points="180,185 188,194 180,196" fill="#7A6030" opacity="0.60"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  MEGHADUTA PALACE (centre background)
# ─────────────────────────────────────────────────────────────────────────────
A('<rect x="154" y="244" width="92" height="96" fill="url(#rPalace)" rx="2"/>')
A('<rect x="154" y="244" width="92" height="4"  fill="#FFF0A0" opacity="0.55"/>')
A('<rect x="154" y="244" width="10" height="96" fill="#000000" opacity="0.12"/>')
# Windows
for wx in [162,178,194,210,226]:
    A(f'<rect x="{wx}" y="262" width="9" height="14" fill="#B08030" opacity="0.55" rx="3"/>')
# Central dome
A('<ellipse cx="200" cy="244" rx="28" ry="20" fill="url(#rDome)"/>')
A('<ellipse cx="200" cy="238" rx="18" ry="10" fill="#5898F8" opacity="0.55"/>')
A('<ellipse cx="196" cy="234" rx="6"  ry="4"  fill="#A8D8FF" opacity="0.50"/>')
A('<line x1="200" y1="224" x2="200" y2="212" stroke="#E8C030" stroke-width="2.8"/>')
A('<circle cx="200" cy="210" r="4.5" fill="url(#rGold)"/>')
A('<circle cx="200" cy="210" r="2"   fill="#FFFFFF" opacity="0.80"/>')
# Side wings
A('<rect x="136" y="272" width="22" height="68" fill="url(#rBldg)" rx="2"/>')
A('<rect x="242" y="272" width="22" height="68" fill="url(#rBldg)" rx="2"/>')
A('<ellipse cx="147" cy="272" rx="11" ry="8" fill="url(#rDome)"/>')
A('<ellipse cx="253" cy="272" rx="11" ry="8" fill="url(#rDome)"/>')
for fx in [147,253]:
    A(f'<line x1="{fx}" y1="264" x2="{fx}" y2="257" stroke="#E8C030" stroke-width="2.2"/>')
    A(f'<circle cx="{fx}" cy="255" r="3.5" fill="url(#rGold)"/>')
# Palace parapet
A('<rect x="153" y="334" width="94" height="8" fill="#E8C878" rx="1"/>')
A('<rect x="153" y="334" width="94" height="2" fill="#FFF8A0" opacity="0.50"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  LEFT CLIFF — WESTERN DISTRICT
# ─────────────────────────────────────────────────────────────────────────────
A('<polygon points="0,0 0,600 136,600 136,305 112,215 86,125 56,48 22,0" fill="url(#rCliffL)"/>')
for sy in [100,140,180,220,265,310,360,410,460,510]:
    A(f'<line x1="0" y1="{sy}" x2="112" y2="{sy}" stroke="#705820" stroke-width="1.0" opacity="0.32"/>')
for sx in [22,50,80,108]:
    A(f'<line x1="{sx}" y1="88" x2="{sx}" y2="600" stroke="#604818" stroke-width="0.7" opacity="0.25"/>')
A('<polygon points="0,0 0,600 18,600 18,450 12,340 6,220 0,0" fill="#000000" opacity="0.20"/>')

# ── Left minaret ──────────────────────────────────────────────────────────────
A('<rect x="64" y="34" width="18" height="100" fill="url(#rMinaret)" rx="3"/>')
A('<rect x="64" y="34" width="5"  height="100" fill="#000000" opacity="0.12"/>')
for my in [58,78,98]:
    A(f'<ellipse cx="73" cy="{my}" rx="14" ry="4" fill="#D0A050" opacity="0.75"/>')
    A(f'<ellipse cx="73" cy="{my}" rx="12" ry="2" fill="#F0C860" opacity="0.60"/>')
A('<ellipse cx="73" cy="34" rx="13" ry="10" fill="url(#rDome)"/>')
A('<ellipse cx="73" cy="30" rx="9"  ry="6"  fill="#5898F8" opacity="0.70"/>')
A('<ellipse cx="71" cy="28" rx="3"  ry="2"  fill="#B0D8FF" opacity="0.55"/>')
A('<line x1="73" y1="24" x2="73" y2="12" stroke="#E8C030" stroke-width="3.5"/>')
A('<line x1="73" y1="24" x2="73" y2="12" stroke="#FFF080" stroke-width="1.4" opacity="0.72"/>')
A('<circle cx="73" cy="10" r="5" fill="url(#rGold)"/>')
A('<circle cx="73" cy="10" r="2.5" fill="#FFFFFF" opacity="0.65"/>')

# ── Left main building ─────────────────────────────────────────────────────────
A('<rect x="14" y="104" width="64" height="120" fill="url(#rBldg)" rx="2"/>')
A('<rect x="14" y="104" width="64" height="4"   fill="#FFF0A0" opacity="0.45"/>')
A('<rect x="14" y="104" width="8"  height="120" fill="#000000" opacity="0.12"/>')
A('<ellipse cx="46" cy="104" rx="26" ry="18" fill="url(#rDome)"/>')
A('<ellipse cx="46" cy="99"  rx="17" ry="10" fill="#5898F8" opacity="0.60"/>')
A('<ellipse cx="43" cy="96"  rx="5"  ry="3"  fill="#B0D8FF" opacity="0.50"/>')
A('<line x1="46" y1="86" x2="46" y2="74" stroke="#E8C030" stroke-width="2.8"/>')
A('<circle cx="46" cy="72" r="4.5" fill="url(#rGold)"/>')

# Arched windows (amber glow)
for wx in [22,40,58]:
    A(f'<rect x="{wx}" y="122" width="10" height="20" fill="#FF9820" opacity="0.45" rx="4"/>')
    A(f'<ellipse cx="{wx+5}" cy="122" rx="5" ry="4" fill="#FF9820" opacity="0.45"/>')
    A(f'<rect x="{wx}" y="138" width="10" height="6"  fill="#604020" opacity="0.40" rx="2"/>')

# ── COLOURFUL TILE MOSAIC BAND on left building ───────────────────────────────
tile_colors = ['#2878C8','#D02818','#E8C030','#18A840','#C828A0','#E87010','#FFFFFF']
for ti, tx in enumerate(range(16, 76, 8)):
    col = tile_colors[ti % len(tile_colors)]
    A(f'<rect x="{tx}" y="216" width="7" height="7" fill="{col}" opacity="0.80" rx="1"/>')
A('<rect x="14" y="214" width="64" height="11" fill="#302010" opacity="0.20"/>')

# Smaller tile row
tile2 = ['#FF4040','#40C840','#4040FF','#FFD030','#FF40B0','#40E0D0']
for ti, tx in enumerate(range(16, 76, 10)):
    col = tile2[ti % len(tile2)]
    A(f'<circle cx="{tx+3}" cy="228" r="3.5" fill="{col}" opacity="0.70"/>')

# ── LEFT MARKET TERRACE (BIG COLOURFUL AWNINGS) ───────────────────────────────
A('<rect x="0" y="238" width="80" height="88" fill="url(#rBldgSh)" rx="1"/>')
# Large, vivid awning stripes — the main colour feature
awning_spec = [
    (0,  '#E82020', '#FF6060'),  # red
    (14, '#1870C8', '#60B0FF'),  # blue
    (28, '#20A830', '#60E060'),  # green
    (42, '#D89010', '#FFD040'),  # gold/yellow
    (56, '#902098', '#D060E0'),  # purple
    (70, '#D85010', '#FF8040'),  # orange
]
for ax, c1, c2 in awning_spec:
    if ax + 12 > 80: break
    A(f'<rect x="{ax}" y="238" width="12" height="16" fill="{c1}" opacity="0.90" rx="1"/>')
    A(f'<rect x="{ax}" y="238" width="12" height="6"  fill="{c2}" opacity="0.70" rx="1"/>')
    A(f'<rect x="{ax}" y="250" width="12" height="4"  fill="{c1}" opacity="0.60"/>')

# Market stall goods
for sx in [10,26,42,58]:
    A(f'<rect x="{sx}" y="268" width="12" height="16" fill="#C09040" opacity="0.60" rx="1"/>')
    A(f'<rect x="{sx}" y="282" width="12" height="5"  fill="#A07030" opacity="0.50" rx="1"/>')
# Flower boxes on terrace ledge
for fx, fc in [(6,'#E82020'),(20,'#FF8010'),(34,'#FFD020'),(50,'#E82070'),(65,'#40C020')]:
    A(f'<ellipse cx="{fx+4}" cy="238" rx="6" ry="3" fill="#6A4010" opacity="0.60"/>')
    for dk in [-3,0,3]:
        A(f'<circle cx="{fx+4+dk}" cy="235" r="3" fill="{fc}" opacity="0.85"/>')
        A(f'<circle cx="{fx+4+dk}" cy="235" r="1.5" fill="#FFFFFF" opacity="0.30"/>')

# ── Left lower tier with colourful banners ──────────────────────────────────────
A('<rect x="0" y="334" width="90" height="86" fill="#986830"/>')
A('<rect x="0" y="334" width="90" height="3"  fill="#D0A040" opacity="0.60"/>')
# Crenellations
for ci in range(0, 90, 14):
    A(f'<rect x="{ci+2}" y="330" width="8" height="10" fill="url(#rBldg)" rx="1"/>')
    A(f'<rect x="{ci+2}" y="330" width="8" height="2"  fill="#FFD060" opacity="0.45"/>')
# Arched doorway
A('<rect x="16" y="352" width="22" height="38" fill="#301808" opacity="0.70" rx="8"/>')
A('<ellipse cx="27" cy="352" rx="11" ry="6" fill="#301808" opacity="0.70"/>')

# Banners — vivid, multi-colour, large
banner_spec_l = [
    (4,  '#E82020', '#FFD030'),  # red+gold
    (18, '#1858C8', '#FFD030'),  # blue+gold
    (34, '#20A830', '#FFD030'),  # green+gold
    (50, '#D89010', '#FFFFFF'),  # gold+white
    (64, '#902098', '#FFD030'),  # purple+gold
    (78, '#D85010', '#FFD030'),  # orange+gold
]
for bx, bc, tc in banner_spec_l:
    A(f'<rect x="{bx}" y="334" width="12" height="26" fill="{bc}" opacity="0.90"/>')
    A(f'<rect x="{bx}" y="334" width="12" height="4"  fill="{tc}" opacity="0.80"/>')
    A(f'<rect x="{bx}" y="356" width="12" height="4"  fill="{tc}" opacity="0.70"/>')
    # Triangle bottom fringe
    A(f'<polygon points="{bx},{360} {bx+6},{366} {bx+12},{360}" fill="{bc}" opacity="0.80"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  RIGHT CLIFF — EASTERN DISTRICT
# ─────────────────────────────────────────────────────────────────────────────
A('<polygon points="400,0 400,600 264,600 264,305 288,215 314,125 344,48 378,0" fill="url(#rCliffR)"/>')
for sy in [100,140,180,220,265,310,360,410,460,510]:
    A(f'<line x1="288" y1="{sy}" x2="400" y2="{sy}" stroke="#705820" stroke-width="1.0" opacity="0.32"/>')
for sx in [292,322,352,380]:
    A(f'<line x1="{sx}" y1="88" x2="{sx}" y2="600" stroke="#604818" stroke-width="0.7" opacity="0.25"/>')
A('<polygon points="400,0 400,600 382,600 382,450 388,340 394,220 400,0" fill="#000000" opacity="0.20"/>')

# Right minaret
A('<rect x="318" y="34" width="18" height="100" fill="url(#rMinaret)" rx="3"/>')
A('<rect x="331" y="34" width="5"  height="100" fill="#000000" opacity="0.12"/>')
for my in [58,78,98]:
    A(f'<ellipse cx="327" cy="{my}" rx="14" ry="4" fill="#D0A050" opacity="0.75"/>')
    A(f'<ellipse cx="327" cy="{my}" rx="12" ry="2" fill="#F0C860" opacity="0.60"/>')
A('<ellipse cx="327" cy="34" rx="13" ry="10" fill="url(#rDome)"/>')
A('<ellipse cx="327" cy="30" rx="9"  ry="6"  fill="#5898F8" opacity="0.70"/>')
A('<ellipse cx="329" cy="28" rx="3"  ry="2"  fill="#B0D8FF" opacity="0.55"/>')
A('<line x1="327" y1="24" x2="327" y2="12" stroke="#E8C030" stroke-width="3.5"/>')
A('<line x1="327" y1="24" x2="327" y2="12" stroke="#FFF080" stroke-width="1.4" opacity="0.72"/>')
A('<circle cx="327" cy="10" r="5" fill="url(#rGold)"/>')
A('<circle cx="327" cy="10" r="2.5" fill="#FFFFFF" opacity="0.65"/>')

# Right main building
A('<rect x="322" y="104" width="64" height="120" fill="url(#rBldg)" rx="2"/>')
A('<rect x="322" y="104" width="64" height="4"   fill="#FFF0A0" opacity="0.45"/>')
A('<rect x="378" y="104" width="8"  height="120" fill="#000000" opacity="0.12"/>')
A('<ellipse cx="354" cy="104" rx="26" ry="18" fill="url(#rDome)"/>')
A('<ellipse cx="354" cy="99"  rx="17" ry="10" fill="#5898F8" opacity="0.60"/>')
A('<ellipse cx="357" cy="96"  rx="5"  ry="3"  fill="#B0D8FF" opacity="0.50"/>')
A('<line x1="354" y1="86" x2="354" y2="74" stroke="#E8C030" stroke-width="2.8"/>')
A('<circle cx="354" cy="72" r="4.5" fill="url(#rGold)"/>')
for wx in [330,348,366]:
    A(f'<rect x="{wx}" y="122" width="10" height="20" fill="#FF9820" opacity="0.45" rx="4"/>')
    A(f'<ellipse cx="{wx+5}" cy="122" rx="5" ry="4" fill="#FF9820" opacity="0.45"/>')
    A(f'<rect x="{wx}" y="138" width="10" height="6"  fill="#604020" opacity="0.40" rx="2"/>')

# Right tile mosaic band
for ti, tx in enumerate(range(324, 384, 8)):
    col = tile_colors[ti % len(tile_colors)]
    A(f'<rect x="{tx}" y="216" width="7" height="7" fill="{col}" opacity="0.80" rx="1"/>')
A('<rect x="322" y="214" width="64" height="11" fill="#302010" opacity="0.20"/>')
for ti, tx in enumerate(range(324, 384, 10)):
    col = tile2[ti % len(tile2)]
    A(f'<circle cx="{tx+3}" cy="228" r="3.5" fill="{col}" opacity="0.70"/>')

# Right market terrace
A('<rect x="320" y="238" width="80" height="88" fill="url(#rBldgSh)" rx="1"/>')
for ax, c1, c2 in awning_spec:
    if ax + 12 > 80: break
    rx = 320 + ax
    A(f'<rect x="{rx}" y="238" width="12" height="16" fill="{c1}" opacity="0.90" rx="1"/>')
    A(f'<rect x="{rx}" y="238" width="12" height="6"  fill="{c2}" opacity="0.70" rx="1"/>')
    A(f'<rect x="{rx}" y="250" width="12" height="4"  fill="{c1}" opacity="0.60"/>')
for sx in [330,346,362,378]:
    A(f'<rect x="{sx}" y="268" width="12" height="16" fill="#C09040" opacity="0.60" rx="1"/>')
    A(f'<rect x="{sx}" y="282" width="12" height="5"  fill="#A07030" opacity="0.50" rx="1"/>')
for fx, fc in [(326,'#40C020'),(340,'#E82020'),(354,'#FF8010'),(368,'#FFD020'),(382,'#E82070')]:
    A(f'<ellipse cx="{fx+4}" cy="238" rx="6" ry="3" fill="#6A4010" opacity="0.60"/>')
    for dk in [-3,0,3]:
        A(f'<circle cx="{fx+4+dk}" cy="235" r="3" fill="{fc}" opacity="0.85"/>')
        A(f'<circle cx="{fx+4+dk}" cy="235" r="1.5" fill="#FFFFFF" opacity="0.30"/>')

# Right lower tier with banners
A('<rect x="310" y="334" width="90" height="86" fill="#986830"/>')
A('<rect x="310" y="334" width="90" height="3"  fill="#D0A040" opacity="0.60"/>')
for ci in range(0, 90, 14):
    A(f'<rect x="{310+ci+2}" y="330" width="8" height="10" fill="url(#rBldg)" rx="1"/>')
    A(f'<rect x="{310+ci+2}" y="330" width="8" height="2"  fill="#FFD060" opacity="0.45"/>')
A('<rect x="362" y="352" width="22" height="38" fill="#301808" opacity="0.70" rx="8"/>')
A('<ellipse cx="373" cy="352" rx="11" ry="6" fill="#301808" opacity="0.70"/>')
for bx, bc, tc in [(312,'#D85010','#FFD030'),(326,'#902098','#FFD030'),
                   (342,'#E82020','#FFD030'),(358,'#1858C8','#FFFFFF'),
                   (374,'#20A830','#FFD030'),(388,'#D89010','#FFFFFF')]:
    A(f'<rect x="{bx}" y="334" width="12" height="26" fill="{bc}" opacity="0.90"/>')
    A(f'<rect x="{bx}" y="334" width="12" height="4"  fill="{tc}" opacity="0.80"/>')
    A(f'<rect x="{bx}" y="356" width="12" height="4"  fill="{tc}" opacity="0.70"/>')
    A(f'<polygon points="{bx},{360} {bx+6},{366} {bx+12},{360}" fill="{bc}" opacity="0.80"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  BUNTING STRINGS (colourful triangular flags strung between buildings)
# ─────────────────────────────────────────────────────────────────────────────
bunting_colors = ['#E82020','#F09010','#E8D010','#20B030','#1868C8','#9020A8','#D82080']
def bunting(x1,y1,x2,y2,n_flags,sag=12):
    """Draw a string of hanging triangle flags from (x1,y1) to (x2,y2)."""
    A(f'<path d="M{x1},{y1} Q{(x1+x2)//2},{(y1+y2)//2+sag} {x2},{y2}" '
      f'stroke="#C09030" stroke-width="0.9" fill="none" opacity="0.60"/>')
    for i in range(n_flags):
        t = (i + 0.5) / n_flags
        # Catenary approximation
        cx = x1 + (x2-x1)*t
        sag_t = sag * 4*t*(1-t)
        cy = y1 + (y2-y1)*t + sag_t
        col = bunting_colors[i % len(bunting_colors)]
        A(f'<polygon points="{cx-5},{cy} {cx+5},{cy} {cx},{cy+10}" fill="{col}" opacity="0.88"/>')

# Bunting across the gap (over the ocean)
bunting(82, 148, 138, 162, 7, sag=18)
bunting(264, 162, 318, 148, 7, sag=18)
bunting(82, 190, 138, 200, 6, sag=14)
bunting(264, 200, 318, 190, 6, sag=14)
# Cross-city bunting on terraces
bunting(0, 238, 80, 244, 5, sag=8)
bunting(320, 244, 400, 238, 5, sag=8)
bunting(0, 334, 88, 338, 6, sag=6)
bunting(312, 338, 400, 334, 6, sag=6)

# ─────────────────────────────────────────────────────────────────────────────
#  PALM TREES (tropical — left and right flanking the ocean gap)
# ─────────────────────────────────────────────────────────────────────────────
def palm_tree(tx, ty, height, lean=0):
    """Draw a stylised palm tree. lean: positive = lean right."""
    tip_x = tx + lean
    tip_y = ty - height
    # Trunk (curved)
    A(f'<path d="M{tx},{ty} Q{tx+lean*0.4:.0f},{ty-height*0.55:.0f} {tip_x},{tip_y}" '
      f'stroke="#7A5018" stroke-width="7" fill="none" stroke-linecap="round"/>')
    A(f'<path d="M{tx},{ty} Q{tx+lean*0.4:.0f},{ty-height*0.55:.0f} {tip_x},{tip_y}" '
      f'stroke="#9A6820" stroke-width="4" fill="none" stroke-linecap="round"/>')
    A(f'<path d="M{tx},{ty} Q{tx+lean*0.4:.0f},{ty-height*0.55:.0f} {tip_x},{tip_y}" '
      f'stroke="#C49040" stroke-width="1.5" fill="none" stroke-linecap="round" opacity="0.50"/>')
    # Bark rings
    for ri in range(3, int(height), int(height/5)):
        t = ri / height
        bx = tx + lean * 0.4 * 2*t*(1-t) + lean * t  # rough bezier approx
        by = ty - ri
        A(f'<ellipse cx="{bx:.0f}" cy="{by}" rx="4" ry="1.5" fill="#604010" opacity="0.35"/>')
    # Fronds (6 directions)
    frond_angs = [-80,-55,-30,-10,15,40,70]
    frond_lens = [32,38,42,40,38,34,28]
    for fa, fl in zip(frond_angs, frond_lens):
        rad = math.radians(fa - 90)  # -90 so 0 is upward
        ex = tip_x + fl * math.cos(rad)
        ey = tip_y + fl * math.sin(rad)
        mx = tip_x + fl*0.5 * math.cos(rad) + 8*math.sin(rad)*(1 if fa>0 else -1)
        my = tip_y + fl*0.5 * math.sin(rad) - 4
        A(f'<path d="M{tip_x},{tip_y} Q{mx:.0f},{my:.0f} {ex:.0f},{ey:.0f}" '
          f'stroke="url(#rPalm)" stroke-width="3.5" fill="none" stroke-linecap="round"/>')
        A(f'<path d="M{tip_x},{tip_y} Q{mx:.0f},{my:.0f} {ex:.0f},{ey:.0f}" '
          f'stroke="#90E840" stroke-width="1.0" fill="none" stroke-linecap="round" opacity="0.50"/>')
    # Coconuts
    for ca in [-20, 10, 40]:
        crad = math.radians(ca - 90)
        cxp = tip_x + 8*math.cos(crad); cyp = tip_y + 8*math.sin(crad)
        A(f'<circle cx="{cxp:.0f}" cy="{cyp:.0f}" r="4" fill="#806020" opacity="0.85"/>')

# Left palm trees (flanking the ocean gap)
palm_tree(110, 340, 95, lean=-12)
palm_tree(126, 348, 80, lean=-8)
# Right palm trees
palm_tree(290, 348, 80, lean=8)
palm_tree(274, 340, 95, lean=12)
# Lower foreground palms
palm_tree(104, 460, 70, lean=-6)
palm_tree(296, 460, 70, lean=6)

# ─────────────────────────────────────────────────────────────────────────────
#  GROUND PLAZA (warm stone + colourful mosaic)
# ─────────────────────────────────────────────────────────────────────────────
A('<rect x="0" y="340" width="400" height="260" fill="url(#rGnd)"/>')
for gx in range(0,401,30):
    A(f'<line x1="{gx}" y1="340" x2="{gx}" y2="600" stroke="#786018" stroke-width="0.8" opacity="0.40"/>')
for gy in range(340,601,25):
    A(f'<line x1="0" y1="{gy}" x2="400" y2="{gy}" stroke="#786018" stroke-width="0.8" opacity="0.40"/>')

# Central octagonal mosaic medallion — vivid tiles
A('<circle cx="200" cy="468" r="50" fill="#C0A040" opacity="0.28"/>')
A('<circle cx="200" cy="468" r="42" fill="#D0B050" opacity="0.24"/>')
mosaic_rings = [
    (36, tile_colors,  4, 0.72),
    (28, tile2,        3, 0.68),
    (18, tile_colors,  3, 0.65),
]
for radius, colors, rdot, op in mosaic_rings:
    n = max(6, int(2*math.pi*radius/10))
    for i in range(n):
        ang = math.radians(i * 360/n)
        mx = 200 + radius*math.cos(ang); my = 468 + radius*math.sin(ang)
        col = colors[i % len(colors)]
        A(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="{rdot}" fill="{col}" opacity="{op}"/>')
# Spoke lines
for ang_m in range(0,360,45):
    rm = math.radians(ang_m)
    A(f'<line x1="200" y1="468" x2="{200+42*math.cos(rm):.0f}" y2="{468+42*math.sin(rm):.0f}" '
      f'stroke="#A08028" stroke-width="0.7" opacity="0.40"/>')
A('<circle cx="200" cy="468" r="6" fill="#E8C030" opacity="0.60"/>')

# Water channel
A('<path d="M200,340 Q200,420 200,500 Q200,550 200,600" stroke="#1898D0" stroke-width="9" fill="none" opacity="0.32"/>')
A('<path d="M200,340 Q200,420 200,500 Q200,550 200,600" stroke="#60C8F0" stroke-width="3.5" fill="none" opacity="0.50"/>')
A('<path d="M200,340 Q200,420 200,500 Q200,550 200,600" stroke="#C0F0FF" stroke-width="1.0" fill="none" opacity="0.55"/>')
A('<path d="M0,468 Q100,458 200,468 Q300,478 400,468" stroke="#1898D0" stroke-width="7" fill="none" opacity="0.28"/>')
A('<path d="M0,468 Q100,458 200,468 Q300,478 400,468" stroke="#60C8F0" stroke-width="2.8" fill="none" opacity="0.45"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  FOREGROUND TOWERS (close, partial)
# ─────────────────────────────────────────────────────────────────────────────
A('<rect x="0" y="398" width="32" height="202" fill="#A07830" rx="2"/>')
A('<rect x="0" y="398" width="10" height="202" fill="#000000" opacity="0.15"/>')
A('<rect x="0" y="398" width="32" height="4"   fill="#D0A040" opacity="0.65"/>')
A('<rect x="0" y="440" width="32" height="9"   fill="#E0A830" opacity="0.60"/>')
for tx in range(2,32,8):
    A(f'<circle cx="{tx}" cy="444" r="2.8" fill="#C08020" opacity="0.65"/>')
A('<rect x="6" y="414" width="16" height="20" fill="#FF9820" opacity="0.42" rx="4"/>')
A('<ellipse cx="14" cy="414" rx="8" ry="5" fill="#FF9820" opacity="0.42"/>')

A('<rect x="368" y="398" width="32" height="202" fill="#A07830" rx="2"/>')
A('<rect x="390" y="398" width="10" height="202" fill="#000000" opacity="0.15"/>')
A('<rect x="368" y="398" width="32" height="4"   fill="#D0A040" opacity="0.65"/>')
A('<rect x="368" y="440" width="32" height="9"   fill="#E0A830" opacity="0.60"/>')
for tx in range(370,400,8):
    A(f'<circle cx="{tx}" cy="444" r="2.8" fill="#C08020" opacity="0.65"/>')
A('<rect x="378" y="414" width="16" height="20" fill="#FF9820" opacity="0.42" rx="4"/>')
A('<ellipse cx="386" cy="414" rx="8" ry="5" fill="#FF9820" opacity="0.42"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  STAGE 5 — ALCHEMICAL BRAZIER (translate +52)
# ─────────────────────────────────────────────────────────────────────────────
A('<g transform="translate(52,0)">')
A('<ellipse cx="200" cy="252" rx="62" ry="42" fill="url(#rFlame)" opacity="0.26"/>')
A('<ellipse cx="200" cy="260" rx="42" ry="28" fill="#FF8010" opacity="0.15"/>')

# Pedestal (colourful tile inlays)
A('<rect x="176" y="285" width="48" height="8"  fill="#C09840" rx="2"/>')
A('<rect x="180" y="278" width="40" height="7"  fill="#D0A850" rx="2"/>')
A('<rect x="184" y="272" width="32" height="6"  fill="#E0B860" rx="2"/>')
A('<rect x="176" y="285" width="48" height="2"  fill="#F0D070" opacity="0.55"/>')
A('<rect x="180" y="278" width="40" height="2"  fill="#F0C858" opacity="0.50"/>')
# Tile dots on pedestal
for ti, tx in enumerate(range(179,223,11)):
    col = tile_colors[ti % len(tile_colors)]
    A(f'<circle cx="{tx}" cy="281" r="3" fill="{col}" opacity="0.75"/>')

# Brazier bowl
A('<ellipse cx="200" cy="272" rx="22" ry="10" fill="#4A3010"/>')
A('<ellipse cx="200" cy="270" rx="20" ry="8"  fill="#6A4818"/>')
A('<ellipse cx="200" cy="268" rx="18" ry="6"  fill="#806028"/>')
A('<ellipse cx="200" cy="263" rx="22" ry="5"  fill="#C89820"/>')
A('<ellipse cx="200" cy="262" rx="20" ry="3.5" fill="#E8B828"/>')
A('<ellipse cx="200" cy="261" rx="18" ry="2"  fill="#FFF060" opacity="0.72"/>')
A('<path d="M184,272 L178,290" stroke="#403008" stroke-width="4" stroke-linecap="round"/>')
A('<path d="M200,275 L200,292" stroke="#403008" stroke-width="4" stroke-linecap="round"/>')
A('<path d="M216,272 L222,290" stroke="#403008" stroke-width="4" stroke-linecap="round"/>')
A('<ellipse cx="178" cy="291" rx="5" ry="2" fill="#302408"/>')
A('<ellipse cx="200" cy="293" rx="5" ry="2" fill="#302408"/>')
A('<ellipse cx="222" cy="291" rx="5" ry="2" fill="#302408"/>')

# Flame (multi-layer, tall)
for fp,fc,fo in [
    ("M186,262 Q178,245 186,228 Q190,212 182,196 Q190,210 196,226 Q198,208 194,192 "
     "Q203,207 200,228 Q204,207 200,192 Q208,208 206,226 Q210,210 214,196 "
     "Q210,214 218,228 Q222,248 214,262","#AA2000",0.82),
    ("M188,262 Q182,246 190,230 Q194,214 190,200 Q198,214 196,232 Q200,216 198,200 "
     "Q207,216 204,232 Q208,216 210,200 Q214,218 210,232 Q214,248 212,262","#FF4800",0.88),
    ("M191,262 Q186,247 194,232 Q198,218 196,206 Q203,220 200,236 Q204,222 202,208 "
     "Q210,224 206,238 Q210,250 208,262","#FF8010",0.86),
    ("M194,262 Q190,248 197,235 Q201,224 200,214 Q204,226 202,240 "
     "Q206,230 204,218 Q210,232 207,244 Q210,254 208,262","#FFB028",0.83),
    ("M198,256 Q195,242 200,232 Q204,242 202,256","#FFD840",0.86),
    ("M199,250 Q197,238 200,229 Q202,238 202,250","#FFF060",0.82),
    ("M200,244 Q198,234 200,226 Q202,234 201,244","#FFFFFF",0.65),
]:
    A(f'<path d="{fp}" fill="{fc}" opacity="{fo}"/>')

for ex,ey,er,eo in [(194,224,1.5,0.85),(207,218,1.2,0.80),(200,210,1.5,0.82),
                    (190,208,1.0,0.75),(211,205,1.0,0.72),(196,198,0.9,0.68),
                    (204,195,0.9,0.65),(200,188,1.2,0.70)]:
    A(f'<circle cx="{ex}" cy="{ey}" r="{er}" fill="#FFC030" opacity="{eo}"/>')
A('</g>')

# ─────────────────────────────────────────────────────────────────────────────
#  STAGE 10 — GREAT HANNISH GATE (scale 1.5×, center y=531)
# ─────────────────────────────────────────────────────────────────────────────
A('<g transform="translate(200,531) scale(1.5) translate(-200,-531)">')
A('<ellipse cx="200" cy="530" rx="88" ry="54" fill="#FF9020" opacity="0.08"/>')

# LEFT MINARET
A('<rect x="142" y="468" width="22" height="92" fill="url(#rGateL)" rx="3"/>')
A('<rect x="142" y="468" width="6"  height="92" fill="#000000" opacity="0.14"/>')
for my in [486,502,518]:
    A(f'<ellipse cx="153" cy="{my}" rx="15" ry="4" fill="#D0A050" opacity="0.72"/>')
    A(f'<ellipse cx="153" cy="{my}" rx="13" ry="2" fill="#F0C860" opacity="0.58"/>')
for wy in [476,492,508]:
    A(f'<rect x="150" y="{wy}" width="6" height="10" fill="#301808" opacity="0.60" rx="2"/>')
A('<ellipse cx="153" cy="468" rx="16" ry="12" fill="url(#rDome)"/>')
A('<ellipse cx="153" cy="464" rx="11" ry="7"  fill="#5898F8" opacity="0.68"/>')
A('<ellipse cx="151" cy="461" rx="3"  ry="2"  fill="#B0D8FF" opacity="0.55"/>')
A('<line x1="153" y1="456" x2="153" y2="445" stroke="#E8C030" stroke-width="4"/>')
A('<line x1="153" y1="456" x2="153" y2="445" stroke="#FFF080" stroke-width="1.6" opacity="0.72"/>')
A('<circle cx="153" cy="443" r="5.5" fill="url(#rGold)"/>')
A('<circle cx="153" cy="443" r="2.5" fill="#FFFFFF" opacity="0.68"/>')

# RIGHT MINARET
A('<rect x="236" y="468" width="22" height="92" fill="url(#rGateR)" rx="3"/>')
A('<rect x="252" y="468" width="6"  height="92" fill="#000000" opacity="0.14"/>')
for my in [486,502,518]:
    A(f'<ellipse cx="247" cy="{my}" rx="15" ry="4" fill="#D0A050" opacity="0.72"/>')
    A(f'<ellipse cx="247" cy="{my}" rx="13" ry="2" fill="#F0C860" opacity="0.58"/>')
for wy in [476,492,508]:
    A(f'<rect x="244" y="{wy}" width="6" height="10" fill="#301808" opacity="0.60" rx="2"/>')
A('<ellipse cx="247" cy="468" rx="16" ry="12" fill="url(#rDome)"/>')
A('<ellipse cx="247" cy="464" rx="11" ry="7"  fill="#5898F8" opacity="0.68"/>')
A('<ellipse cx="249" cy="461" rx="3"  ry="2"  fill="#B0D8FF" opacity="0.55"/>')
A('<line x1="247" y1="456" x2="247" y2="445" stroke="#E8C030" stroke-width="4"/>')
A('<line x1="247" y1="456" x2="247" y2="445" stroke="#FFF080" stroke-width="1.6" opacity="0.72"/>')
A('<circle cx="247" cy="443" r="5.5" fill="url(#rGold)"/>')
A('<circle cx="247" cy="443" r="2.5" fill="#FFFFFF" opacity="0.68"/>')

# CONNECTING WALL
A('<rect x="164" y="490" width="72" height="68" fill="url(#rGateL)" rx="2"/>')
A('<rect x="164" y="490" width="10" height="68" fill="#000000" opacity="0.12"/>')
# Colourful tile bands on gate wall
for ti, tx in enumerate(range(166,234,9)):
    col = tile_colors[ti % len(tile_colors)]
    A(f'<rect x="{tx}" y="491" width="7" height="5" fill="{col}" opacity="0.75" rx="1"/>')
A('<rect x="164" y="553" width="72" height="5" fill="#E8C030" opacity="0.60"/>')
# Tile pattern on lower wall
for ty2 in [500,512,524,536]:
    for ti, tx in enumerate(range(168,232,12)):
        col = tile2[ti % len(tile2)]
        A(f'<rect x="{tx}" y="{ty2}" width="8" height="8" fill="{col}" opacity="0.40" rx="1"/>')

# CENTRAL LARGE DOME
A('<ellipse cx="200" cy="490" rx="34" ry="24" fill="url(#rDome)"/>')
A('<ellipse cx="200" cy="484" rx="23" ry="14" fill="#4888F0" opacity="0.62"/>')
A('<ellipse cx="197" cy="480" rx="7"  ry="4"  fill="#90C0FF" opacity="0.52"/>')
A('<ellipse cx="200" cy="490" rx="34" ry="6"  fill="none" stroke="#E8C030" stroke-width="3"/>')
A('<ellipse cx="200" cy="490" rx="34" ry="6"  fill="none" stroke="#FFF080" stroke-width="0.9" opacity="0.62"/>')
A('<line x1="200" y1="466" x2="200" y2="453" stroke="#E8C030" stroke-width="4"/>')
A('<line x1="200" y1="466" x2="200" y2="453" stroke="#FFF080" stroke-width="1.6" opacity="0.72"/>')
A('<circle cx="200" cy="451" r="6.5" fill="url(#rGold)"/>')
A('<circle cx="200" cy="451" r="3"   fill="#FFFFFF" opacity="0.72"/>')

# GATE ARCH (Hannish pointed)
A('<path d="M164,530 Q164,502 200,494 Q236,502 236,530" '
  'fill="none" stroke="#C0A040" stroke-width="15"/>')
A('<path d="M168,530 Q168,506 200,499 Q232,506 232,530" '
  'fill="none" stroke="#E8C878" stroke-width="4.5" opacity="0.52"/>')
A('<path d="M170,529 Q170,508 200,502 Q230,508 230,529" '
  'fill="none" stroke="#E8C030" stroke-width="2.2" opacity="0.72"/>')
A('<path d="M170,529 Q170,508 200,502 Q230,508 230,529" '
  'fill="none" stroke="#FFF080" stroke-width="0.7" opacity="0.62"/>')

for angle_deg in [208,222,236,250,264,278,292,306,320]:
    ang = math.radians(angle_deg)
    x_o = 200+38*math.cos(ang); y_o = 530+38*math.sin(ang)
    x_i = 200+23*math.cos(ang); y_i = 530+23*math.sin(ang)
    A(f'<line x1="{x_i:.1f}" y1="{y_i:.1f}" x2="{x_o:.1f}" y2="{y_o:.1f}" '
      f'stroke="#786020" stroke-width="1.0" opacity="0.58"/>')

# Keystone — vivid sun motif
A('<circle cx="200" cy="494" r="10" fill="#E8C030" stroke="#FFF080" stroke-width="2"/>')
for ang_k in range(0,360,45):
    rk = math.radians(ang_k)
    A(f'<line x1="{200+4*math.cos(rk):.1f}" y1="{494+4*math.sin(rk):.1f}" '
      f'x2="{200+8.5*math.cos(rk):.1f}" y2="{494+8.5*math.sin(rk):.1f}" '
      f'stroke="#FFFFFF" stroke-width="1.4" opacity="0.88"/>')
A('<circle cx="200" cy="494" r="3.5" fill="#FFFFFF" opacity="0.85"/>')

# BUNTING across gate arch
bunting_g = ['#E82020','#F09010','#E8D010','#20B030','#1868C8','#9020A8']
for i in range(8):
    t = (i+0.5)/8
    ang = math.radians(208 + (320-208)*t)
    bx = 200 + 38*math.cos(ang); by = 530 + 38*math.sin(ang)
    col = bunting_g[i % len(bunting_g)]
    A(f'<polygon points="{bx-4:.1f},{by:.1f} {bx+4:.1f},{by:.1f} {bx:.1f},{by+9:.1f}" '
      f'fill="{col}" opacity="0.88"/>')

# GATE DOORS
A('<rect x="168" y="530" width="30" height="28" fill="#2A1808" rx="1"/>')
A('<rect x="168" y="530" width="6"  height="28" fill="#3C2410" opacity="0.50"/>')
for sy in [534,544,554]:
    A(f'<rect x="168" y="{sy}" width="30" height="2.5" fill="#484030" opacity="0.72"/>')
for sy2 in [531,537,543,549,555]:
    for sx in [171,176,181,186,191]:
        A(f'<circle cx="{sx}" cy="{sy2}" r="1.4" fill="#808880" opacity="0.78"/>')
A('<rect x="172" y="532" width="10" height="10" fill="#1A0C04" rx="1"/>')
A('<rect x="184" y="532" width="10" height="10" fill="#1A0C04" rx="1"/>')
A('<rect x="172" y="546" width="22" height="10" fill="#1A0C04" rx="1"/>')

A('<rect x="202" y="530" width="30" height="28" fill="#2A1808" rx="1"/>')
A('<rect x="226" y="530" width="6"  height="28" fill="#3C2410" opacity="0.50"/>')
for sy in [534,544,554]:
    A(f'<rect x="202" y="{sy}" width="30" height="2.5" fill="#484030" opacity="0.72"/>')
for sy2 in [531,537,543,549,555]:
    for sx in [211,216,221,226,231]:
        A(f'<circle cx="{sx}" cy="{sy2}" r="1.4" fill="#808880" opacity="0.78"/>')
A('<rect x="206" y="532" width="10" height="10" fill="#1A0C04" rx="1"/>')
A('<rect x="218" y="532" width="10" height="10" fill="#1A0C04" rx="1"/>')
A('<rect x="206" y="546" width="22" height="10" fill="#1A0C04" rx="1"/>')
A('<line x1="200" y1="530" x2="200" y2="558" stroke="#181008" stroke-width="2" opacity="0.82"/>')

# Hanging lamps (3 vivid amber)
for lx in [172,200,228]:
    A(f'<line x1="{lx}" y1="490" x2="{lx}" y2="508" stroke="#806028" stroke-width="1.4" opacity="0.68"/>')
    A(f'<ellipse cx="{lx}" cy="512" rx="5.5" ry="7.5" fill="#804010" opacity="0.82"/>')
    A(f'<ellipse cx="{lx}" cy="507" rx="5.5" ry="2"   fill="#C06018" opacity="0.72"/>')
    A(f'<circle  cx="{lx}" cy="512" r="4"   fill="#FFD040" opacity="0.88"/>')
    A(f'<ellipse cx="{lx}" cy="515" rx="10" ry="6" fill="#FF9020" opacity="0.28"/>')

# Gate bunting strings between minarets
bunting(142, 490, 164, 496, 4, sag=6)
bunting(236, 496, 258, 490, 4, sag=6)

# Gate base
A('<rect x="158" y="558" width="84" height="8" fill="#B09030" rx="2"/>')
A('<rect x="158" y="558" width="84" height="2" fill="#E0C040" opacity="0.45"/>')

A('</g>')

# ─────────────────────────────────────────────────────────────────────────────
#  ATMOSPHERE + SEAGULLS
# ─────────────────────────────────────────────────────────────────────────────
A('<rect y="488" width="400" height="112" fill="url(#rHaze)" opacity="0.90"/>')
A('<rect y="562" width="400" height="38"  fill="#D0A030" opacity="0.06"/>')
A('<rect width="400" height="600" fill="url(#rVig)"/>')

for bx,by in [(148,60),(172,52),(196,66),(220,56),(244,70),(268,58)]:
    A(f'<path d="M{bx},{by} Q{bx+5},{by-5} {bx+10},{by}" stroke="#FFFFFF" stroke-width="1.6" fill="none" opacity="0.72"/>')
    A(f'<path d="M{bx+10},{by} Q{bx+15},{by-5} {bx+20},{by}" stroke="#FFFFFF" stroke-width="1.6" fill="none" opacity="0.72"/>')

A('</svg>')

# ─────────────────────────────────────────────────────────────────────────────
#  VALIDATE + INJECT
# ─────────────────────────────────────────────────────────────────────────────
svg = ''.join(parts)
print(f'EXTREME SVG: {len(svg):,} chars')

ro = len(_re.findall(r'<radialGradient', svg))
rc = len(_re.findall(r'</radialGradient', svg))
lo = len(_re.findall(r'<linearGradient', svg))
lc = len(_re.findall(r'</linearGradient', svg))
print(f'  radialGradient: {ro}/{rc}  linearGradient: {lo}/{lc}')
if ro!=rc: raise RuntimeError(f'radialGradient mismatch')
if lo!=lc: raise RuntimeError(f'linearGradient mismatch')
if svg.count("'"): raise RuntimeError('Single quote in SVG!')

# Parse-check with DOMParser simulation (check for obvious XML errors)
import xml.etree.ElementTree as ET
try:
    ET.fromstring(svg)
    print('  XML parse: OK')
except ET.ParseError as e:
    raise RuntimeError(f'XML parse error: {e}')

html2 = html
for old, new in [
    ('.map-scroll[data-diff="EXTREME"] { background: #4B5041; }',
     '.map-scroll[data-diff="EXTREME"] { background: #1890D8; }'),
    ('.map-scroll[data-diff="EXTREME"] { background: #1890D8; }',
     '.map-scroll[data-diff="EXTREME"] { background: #1890D8; }'),
    ('#game-view[data-diff="EXTREME"] { background: rgb(75,80,65); }',
     '#game-view[data-diff="EXTREME"] { background: rgb(24,144,216); }'),
]:
    html2 = html2.replace(old, new)

pattern = r"(if\(diff==='EXTREME'\) return ')(.*?)(';)"
repl = lambda m: m.group(1) + svg + m.group(3)
new_html, n = _re.subn(pattern, repl, html2, flags=_re.DOTALL)
if n == 0: raise RuntimeError("EXTREME pattern not found")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print(f'stage.html written. ({n} replacement)')
