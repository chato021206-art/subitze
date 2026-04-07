#!/usr/bin/env python3
"""gen_extreme.py — EXTREME background: Radz-at-Han / Thavnair (FF14 Endwalker).
The tiered island city-state — cobalt domes, gold minarets, market terraces,
harbour ocean, alchemical fires, the great Meghaduta palace.
"""
import re as _re, math

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    html = f.read()

parts = []
def A(s): parts.append(s)

# ─────────────────────────────────────────────────────────────────────────────
#  SVG HEADER
# ─────────────────────────────────────────────────────────────────────────────
A('<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"><defs>')

# Sky: azure blue (sunny Thavnair coast)
A('<linearGradient id="rSky" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#1890D8"/>'
  '<stop offset="28%"  stop-color="#38A8E8"/>'
  '<stop offset="58%"  stop-color="#68C4F4"/>'
  '<stop offset="82%"  stop-color="#98D8F8"/>'
  '<stop offset="100%" stop-color="#C0E8FF"/>'
  '</linearGradient>')

# Sun warm glow (upper right)
A('<radialGradient id="rSun" cx="82%" cy="8%" r="55%">'
  '<stop offset="0%"   stop-color="#FFFAE0" stop-opacity="0.85"/>'
  '<stop offset="12%"  stop-color="#FFE890" stop-opacity="0.55"/>'
  '<stop offset="30%"  stop-color="#FFD060" stop-opacity="0.28"/>'
  '<stop offset="55%"  stop-color="#FFC040" stop-opacity="0.10"/>'
  '<stop offset="100%" stop-color="#F8A800" stop-opacity="0"/>'
  '</radialGradient>')

# Ocean / harbour (deep teal-blue)
A('<linearGradient id="rOcean" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#1878B0"/>'
  '<stop offset="45%"  stop-color="#1060908"/>'
  '<stop offset="100%" stop-color="#0A4868"/>'
  '</linearGradient>')

# Ocean shimmer radial (sun reflection on water)
A('<radialGradient id="rOceanShim" cx="70%" cy="20%" r="55%">'
  '<stop offset="0%"   stop-color="#80D8F8" stop-opacity="0.45"/>'
  '<stop offset="40%"  stop-color="#40B0D8" stop-opacity="0.18"/>'
  '<stop offset="100%" stop-color="#1878B0" stop-opacity="0"/>'
  '</radialGradient>')

# Sandstone cliff / city wall (warm ochre)
A('<linearGradient id="rCliffL" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#705828"/>'
  '<stop offset="40%"  stop-color="#A88040"/>'
  '<stop offset="75%"  stop-color="#D0A860"/>'
  '<stop offset="100%" stop-color="#E0B870"/>'
  '</linearGradient>')

A('<linearGradient id="rCliffR" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#E0B870"/>'
  '<stop offset="25%"  stop-color="#D0A860"/>'
  '<stop offset="60%"  stop-color="#A88040"/>'
  '<stop offset="100%" stop-color="#705828"/>'
  '</linearGradient>')

# Building face (warm sandstone, slightly lighter)
A('<linearGradient id="rBldg" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#E8C878"/>'
  '<stop offset="40%"  stop-color="#D4B060"/>'
  '<stop offset="80%"  stop-color="#B89040"/>'
  '<stop offset="100%" stop-color="#9A7830"/>'
  '</linearGradient>')

# Building shadow face
A('<linearGradient id="rBldgSh" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#B89848"/>'
  '<stop offset="50%"  stop-color="#987830"/>'
  '<stop offset="100%" stop-color="#786018"/>'
  '</linearGradient>')

# Cobalt-blue dome (the most distinctive Radz-at-Han feature)
A('<radialGradient id="rDome" cx="38%" cy="30%" r="65%">'
  '<stop offset="0%"   stop-color="#80C0F8"/>'
  '<stop offset="28%"  stop-color="#3890E0"/>'
  '<stop offset="58%"  stop-color="#1A68C0"/>'
  '<stop offset="85%"  stop-color="#0E4898"/>'
  '<stop offset="100%" stop-color="#083070"/>'
  '</radialGradient>')

# Gold trim / minaret gold
A('<linearGradient id="rGold" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FFF0A0"/>'
  '<stop offset="30%"  stop-color="#F0C030"/>'
  '<stop offset="65%"  stop-color="#C89818"/>'
  '<stop offset="100%" stop-color="#906808"/>'
  '</linearGradient>')

# Minaret shaft
A('<linearGradient id="rMinaret" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#A88038"/>'
  '<stop offset="35%"  stop-color="#E0B860"/>'
  '<stop offset="70%"  stop-color="#F8D880"/>'
  '<stop offset="100%" stop-color="#D0A050"/>'
  '</linearGradient>')

# Tile / terrace floor
A('<linearGradient id="rTile" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#D8C888"/>'
  '<stop offset="50%"  stop-color="#C0A860"/>'
  '<stop offset="100%" stop-color="#A08840"/>'
  '</linearGradient>')

# Ground plaza (stone, warm)
A('<linearGradient id="rGnd" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#C8A850"/>'
  '<stop offset="40%"  stop-color="#B09040"/>'
  '<stop offset="100%" stop-color="#907030"/>'
  '</linearGradient>')

# Meghaduta palace (centre background) — richer sandstone
A('<linearGradient id="rPalace" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#F0D890"/>'
  '<stop offset="40%"  stop-color="#E0C070"/>'
  '<stop offset="80%"  stop-color="#C8A050"/>'
  '<stop offset="100%" stop-color="#A88030"/>'
  '</linearGradient>')

# Gate pillar L
A('<linearGradient id="rGateL" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#705820"/>'
  '<stop offset="35%"  stop-color="#C09840"/>'
  '<stop offset="68%"  stop-color="#E8C068"/>'
  '<stop offset="100%" stop-color="#D8B058"/>'
  '</linearGradient>')

# Gate pillar R
A('<linearGradient id="rGateR" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#D8B058"/>'
  '<stop offset="32%"  stop-color="#E8C068"/>'
  '<stop offset="65%"  stop-color="#C09840"/>'
  '<stop offset="100%" stop-color="#705820"/>'
  '</linearGradient>')

# Alchemical flame (Stage 5 eternal brazier)
A('<radialGradient id="rFlame" cx="50%" cy="70%" r="55%">'
  '<stop offset="0%"   stop-color="#FFFFFF" stop-opacity="0.92"/>'
  '<stop offset="20%"  stop-color="#FFF080" stop-opacity="0.85"/>'
  '<stop offset="45%"  stop-color="#FF9010" stop-opacity="0.65"/>'
  '<stop offset="72%"  stop-color="#FF4800" stop-opacity="0.35"/>'
  '<stop offset="100%" stop-color="#CC2000" stop-opacity="0"/>'
  '</radialGradient>')

# Bottom haze (warm horizon)
A('<linearGradient id="rHaze" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#D8A030" stop-opacity="0"/>'
  '<stop offset="55%"  stop-color="#C89028" stop-opacity="0.06"/>'
  '<stop offset="100%" stop-color="#B07818" stop-opacity="0.20"/>'
  '</linearGradient>')

# Top vignette
A('<linearGradient id="rVig" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#061018" stop-opacity="0.70"/>'
  '<stop offset="18%"  stop-color="#061018" stop-opacity="0.04"/>'
  '<stop offset="100%" stop-color="#061018" stop-opacity="0"/>'
  '</linearGradient>')

A('</defs>')

# ─────────────────────────────────────────────────────────────────────────────
#  1. SKY + SUN
# ─────────────────────────────────────────────────────────────────────────────
A('<rect width="400" height="600" fill="url(#rSky)"/>')
A('<rect width="400" height="600" fill="url(#rSun)"/>')

# Sun disk (bright white-gold)
A('<circle cx="328" cy="48" r="36" fill="#FFD030" opacity="0.18"/>')
A('<circle cx="328" cy="48" r="24" fill="#FFE060" opacity="0.30"/>')
A('<circle cx="328" cy="48" r="16" fill="#FFF0A0" opacity="0.80"/>')
A('<circle cx="328" cy="48" r="12" fill="#FFF8D0" opacity="0.92"/>')
A('<circle cx="328" cy="48" r="8"  fill="#FFFFFF"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  2. CLOUDS (light, Mediterranean cumulus)
# ─────────────────────────────────────────────────────────────────────────────
clouds = [
    # (cx, cy, w, h, op)
    (56,  36, 72, 22, 0.78), (42,  44, 48, 16, 0.70),
    (180, 28, 88, 26, 0.75), (168, 38, 56, 18, 0.65),
    (290, 40, 68, 20, 0.65),
]
for cx, cy, cw, ch, op in clouds:
    A(f'<ellipse cx="{cx}" cy="{cy}" rx="{cw//2}" ry="{ch//2}" fill="#FFFFFF" opacity="{op}"/>')
    A(f'<ellipse cx="{cx-cw//5}" cy="{cy+ch//4}" rx="{cw//3}" ry="{ch//3}" fill="#FFFFFF" opacity="{op*0.88:.2f}"/>')
    A(f'<ellipse cx="{cx+cw//5}" cy="{cy+ch//4}" rx="{cw//4}" ry="{ch//3}" fill="#FFFFFF" opacity="{op*0.80:.2f}"/>')
    # Cloud shadow underbelly
    A(f'<ellipse cx="{cx}" cy="{cy+ch//2-2}" rx="{cw//2}" ry="5" fill="#B8D8F0" opacity="{op*0.30:.2f}"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  3. OCEAN / HARBOUR (visible in the gap between the cliffs)
# ─────────────────────────────────────────────────────────────────────────────
# Ocean fills the background gap
A('<rect x="136" y="0" width="128" height="340" fill="url(#rOcean)"/>')
A('<rect x="136" y="0" width="128" height="340" fill="url(#rOceanShim)"/>')

# Ocean wave highlights
wave_paths = [
    "M136,80  Q152,76 168,80 Q184,84 200,80 Q216,76 232,80 Q248,84 264,80",
    "M136,100 Q155,96 175,100 Q195,104 215,100 Q235,96 264,100",
    "M136,124 Q158,120 180,124 Q202,128 224,124 Q246,120 264,124",
    "M136,152 Q160,148 184,152 Q208,156 232,152 Q256,148 264,152",
    "M136,184 Q162,180 188,184 Q214,188 240,184 Q258,180 264,184",
]
for wp in wave_paths:
    A(f'<path d="{wp}" stroke="#60C0E8" stroke-width="1.2" fill="none" opacity="0.45"/>')
    A(f'<path d="{wp}" stroke="#C0E8FF" stroke-width="0.5" fill="none" opacity="0.55"/>')

# Sun shimmer streak on ocean
A('<path d="M240,60 Q250,100 248,180 Q246,230 244,280" stroke="#FFFFFF" stroke-width="4" fill="none" opacity="0.12"/>')
A('<path d="M242,60 Q252,100 250,180 Q248,230 246,280" stroke="#FFFFFF" stroke-width="1.5" fill="none" opacity="0.20"/>')

# Distant island / headland silhouette
A('<polygon points="136,200 148,148 168,120 192,132 200,120 208,132 228,118 252,148 264,200" fill="#1060808" opacity="0.60"/>')
A('<polygon points="136,200 148,152 170,124 190,136 200,124 210,136 230,122 252,152 264,200" fill="#106080" opacity="0.50"/>')

# Distant ship (small galleon silhouette on ocean)
A('<rect x="172" y="195" width="20" height="4"  fill="#4A3818" opacity="0.60"/>')
A('<rect x="180" y="182" width="2"  height="14" fill="#382808" opacity="0.60"/>')
A('<polygon points="181,182 188,190 181,192" fill="#7A6030" opacity="0.55"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  4. MEGHADUTA PALACE (centre background, above the ocean gap)
# ─────────────────────────────────────────────────────────────────────────────
# Palace base building
A('<rect x="156" y="240" width="88" height="100" fill="url(#rPalace)" rx="2"/>')
A('<rect x="156" y="240" width="88" height="4"   fill="#FFF0A0" opacity="0.50"/>')
# Palace shadow
A('<rect x="156" y="240" width="10" height="100" fill="#000000" opacity="0.12"/>')
# Palace windows
for wx in [164, 180, 196, 212, 228]:
    A(f'<rect x="{wx}" y="258" width="8" height="14" fill="#A88030" opacity="0.50" rx="3"/>')
    A(f'<rect x="{wx}" y="268" width="8" height="5"  fill="#604818" opacity="0.40" rx="1"/>')

# Palace central dome (Meghaduta)
A('<ellipse cx="200" cy="240" rx="26" ry="18" fill="url(#rDome)"/>')
A('<ellipse cx="200" cy="234" rx="18" ry="10" fill="#60A0E8" opacity="0.50"/>')
A('<ellipse cx="196" cy="230" rx="6"  ry="4"  fill="#A0D0FF" opacity="0.45"/>')
# Dome gold finial
A('<line x1="200" y1="222" x2="200" y2="212" stroke="#E8C030" stroke-width="2.5"/>')
A('<circle cx="200" cy="210" r="4" fill="url(#rGold)"/>')
A('<circle cx="200" cy="210" r="2" fill="#FFF080" opacity="0.80"/>')

# Palace side wings
A('<rect x="140" y="268" width="20" height="72" fill="url(#rBldg)" rx="2"/>')
A('<rect x="240" y="268" width="20" height="72" fill="url(#rBldg)" rx="2"/>')
# Wing domes (small)
A('<ellipse cx="150" cy="268" rx="10" ry="7" fill="url(#rDome)"/>')
A('<ellipse cx="250" cy="268" rx="10" ry="7" fill="url(#rDome)"/>')
# Wing finials
for fx in [150, 250]:
    A(f'<line x1="{fx}" y1="261" x2="{fx}" y2="255" stroke="#E8C030" stroke-width="2"/>')
    A(f'<circle cx="{fx}" cy="253" r="3" fill="url(#rGold)"/>')

# Palace parapet
A('<rect x="155" y="334" width="90" height="8" fill="#E8C878" rx="1"/>')
A('<rect x="155" y="334" width="90" height="2" fill="#FFF0A0" opacity="0.45"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  5. LEFT CLIFF — RADZ-AT-HAN WESTERN DISTRICT
# ─────────────────────────────────────────────────────────────────────────────
A('<polygon points="0,0 0,600 136,600 136,305 112,215 86,125 56,48 22,0" fill="url(#rCliffL)"/>')

# Rock strata on cliff face
for sy in [100, 140, 180, 220, 265, 310, 360, 410, 460, 510]:
    A(f'<line x1="0" y1="{sy}" x2="112" y2="{sy}" stroke="#705820" stroke-width="1.2" opacity="0.35"/>')
for sx in [22, 48, 76, 104]:
    A(f'<line x1="{sx}" y1="90" x2="{sx}" y2="600" stroke="#604818" stroke-width="0.8" opacity="0.28"/>')

# Shadow on left edge
A('<polygon points="0,0 0,600 18,600 18,450 12,340 6,220 0,0" fill="#000000" opacity="0.22"/>')

# ── Left minaret (tall, slender, gold cap) ─────────────────────────────────
A('<rect x="64" y="36" width="18" height="100" fill="url(#rMinaret)" rx="3"/>')
A('<rect x="64" y="36" width="5"  height="100" fill="#000000" opacity="0.12"/>')
# Minaret balcony rings (muqarnas)
for my in [60, 80, 100]:
    A(f'<ellipse cx="73" cy="{my}" rx="13" ry="4" fill="#D0A050" opacity="0.70"/>')
    A(f'<ellipse cx="73" cy="{my}" rx="11" ry="2" fill="#F0C060" opacity="0.55"/>')
# Minaret bulbous gold cap
A('<ellipse cx="73" cy="36" rx="12" ry="10" fill="url(#rDome)"/>')
A('<ellipse cx="73" cy="32" rx="8"  ry="6"  fill="#5090D8" opacity="0.65"/>')
A('<ellipse cx="71" cy="30" rx="3"  ry="2"  fill="#90C0F0" opacity="0.50"/>')
# Finial spire
A('<line x1="73" y1="26" x2="73" y2="14" stroke="#E8C030" stroke-width="3"/>')
A('<line x1="73" y1="26" x2="73" y2="14" stroke="#FFF080" stroke-width="1.2" opacity="0.70"/>')
A('<circle cx="73" cy="12" r="4.5" fill="url(#rGold)"/>')
A('<circle cx="73" cy="12" r="2.5" fill="#FFFFFF" opacity="0.60"/>')

# ── Main left civic building ─────────────────────────────────────────────────
A('<rect x="14" y="106" width="64" height="120" fill="url(#rBldg)" rx="2"/>')
A('<rect x="14" y="106" width="64" height="4"   fill="#FFF0A0" opacity="0.40"/>')
# Building shadow
A('<rect x="14" y="106" width="8"  height="120" fill="#000000" opacity="0.12"/>')
# Dome on building
A('<ellipse cx="46" cy="106" rx="24" ry="16" fill="url(#rDome)"/>')
A('<ellipse cx="46" cy="101" rx="16" ry="9"  fill="#5090D8" opacity="0.55"/>')
A('<ellipse cx="43" cy="98"  rx="5"  ry="3"  fill="#90C0F0" opacity="0.45"/>')
A('<line x1="46" y1="90"  x2="46" y2="80"  stroke="#E8C030" stroke-width="2.5"/>')
A('<circle cx="46" cy="78" r="4" fill="url(#rGold)"/>')
# Arched windows (Hannish style)
for wx in [22, 40, 58]:
    A(f'<rect x="{wx}" y="124" width="10" height="20" fill="#80501800" opacity="0.60" rx="4"/>')
    A(f'<rect x="{wx}" y="124" width="10" height="20" fill="#FFA030" opacity="0.30" rx="4"/>')
    A(f'<rect x="{wx}" y="140" width="10" height="6"  fill="#604020" opacity="0.40" rx="2"/>')
# Decorative tile frieze (geometric band)
A('<rect x="14" y="218" width="64" height="8" fill="#E0A830" opacity="0.60"/>')
# Tile pattern dots
for tx in range(18, 76, 8):
    A(f'<circle cx="{tx}" cy="222" r="2" fill="#C08020" opacity="0.60"/>')

# ── Left market terrace ────────────────────────────────────────────────────
A('<rect x="0" y="240" width="78" height="80" fill="url(#rBldgSh)" rx="1"/>')
A('<rect x="0" y="240" width="78" height="3"  fill="#E8C060" opacity="0.50"/>')
# Market awning strips (colorful canopies — Hannish market)
awning_colors = ['#D03030', '#30A830', '#2858C8', '#C87818', '#8020A0']
for ai, ax in enumerate(range(6, 74, 14)):
    col = awning_colors[ai % len(awning_colors)]
    A(f'<rect x="{ax}" y="240" width="10" height="6" fill="{col}" opacity="0.75" rx="1"/>')
# Market goods / stall
for sx in [12, 28, 44, 60]:
    A(f'<rect x="{sx}" y="258" width="10" height="14" fill="#C09040" opacity="0.55" rx="1"/>')
    A(f'<rect x="{sx}" y="270" width="10" height="4"  fill="#A07030" opacity="0.45" rx="1"/>')

# Lower stone tier
A('<rect x="0" y="330" width="88" height="90" fill="#986830"/>')
A('<rect x="0" y="330" width="88" height="3"  fill="#D0A040" opacity="0.55"/>')
# Decorative crenellations
for ci in range(0, 88, 14):
    A(f'<rect x="{ci+2}" y="326" width="8" height="10" fill="url(#rBldg)" rx="1"/>')
    A(f'<rect x="{ci+2}" y="326" width="8" height="2"  fill="#FFD060" opacity="0.40"/>')
# Arched doorway
A('<rect x="16" y="352" width="20" height="36" fill="#50300800" opacity="0.65" rx="8"/>')
A('<rect x="16" y="352" width="20" height="36" fill="#301808" opacity="0.65" rx="8"/>')
A('<ellipse cx="26" cy="352" rx="10" ry="6" fill="#301808" opacity="0.65"/>')
# Hanging banners (purple with gold trim — Hannish)
for bx in [8, 30, 52, 70]:
    A(f'<rect x="{bx}" y="330" width="10" height="22" fill="#702090" opacity="0.85"/>')
    A(f'<rect x="{bx}" y="330" width="10" height="3"  fill="#E8C030" opacity="0.75"/>')
    A(f'<rect x="{bx}" y="348" width="10" height="3"  fill="#E8C030" opacity="0.65"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  6. RIGHT CLIFF — RADZ-AT-HAN EASTERN DISTRICT
# ─────────────────────────────────────────────────────────────────────────────
A('<polygon points="400,0 400,600 264,600 264,305 288,215 314,125 344,48 378,0" fill="url(#rCliffR)"/>')

for sy in [100, 140, 180, 220, 265, 310, 360, 410, 460, 510]:
    A(f'<line x1="288" y1="{sy}" x2="400" y2="{sy}" stroke="#705820" stroke-width="1.2" opacity="0.35"/>')
for sx in [296, 322, 350, 378]:
    A(f'<line x1="{sx}" y1="90" x2="{sx}" y2="600" stroke="#604818" stroke-width="0.8" opacity="0.28"/>')

A('<polygon points="400,0 400,600 382,600 382,450 388,340 394,220 400,0" fill="#000000" opacity="0.22"/>')

# Right minaret
A('<rect x="318" y="36" width="18" height="100" fill="url(#rMinaret)" rx="3"/>')
A('<rect x="331" y="36" width="5"  height="100" fill="#000000" opacity="0.12"/>')
for my in [60, 80, 100]:
    A(f'<ellipse cx="327" cy="{my}" rx="13" ry="4" fill="#D0A050" opacity="0.70"/>')
    A(f'<ellipse cx="327" cy="{my}" rx="11" ry="2" fill="#F0C060" opacity="0.55"/>')
A('<ellipse cx="327" cy="36" rx="12" ry="10" fill="url(#rDome)"/>')
A('<ellipse cx="327" cy="32" rx="8"  ry="6"  fill="#5090D8" opacity="0.65"/>')
A('<ellipse cx="329" cy="30" rx="3"  ry="2"  fill="#90C0F0" opacity="0.50"/>')
A('<line x1="327" y1="26" x2="327" y2="14" stroke="#E8C030" stroke-width="3"/>')
A('<line x1="327" y1="26" x2="327" y2="14" stroke="#FFF080" stroke-width="1.2" opacity="0.70"/>')
A('<circle cx="327" cy="12" r="4.5" fill="url(#rGold)"/>')
A('<circle cx="327" cy="12" r="2.5" fill="#FFFFFF" opacity="0.60"/>')

# Right civic building
A('<rect x="322" y="106" width="64" height="120" fill="url(#rBldg)" rx="2"/>')
A('<rect x="322" y="106" width="64" height="4"   fill="#FFF0A0" opacity="0.40"/>')
A('<rect x="378" y="106" width="8"  height="120" fill="#000000" opacity="0.12"/>')
A('<ellipse cx="354" cy="106" rx="24" ry="16" fill="url(#rDome)"/>')
A('<ellipse cx="354" cy="101" rx="16" ry="9"  fill="#5090D8" opacity="0.55"/>')
A('<ellipse cx="357" cy="98"  rx="5"  ry="3"  fill="#90C0F0" opacity="0.45"/>')
A('<line x1="354" y1="90"  x2="354" y2="80"  stroke="#E8C030" stroke-width="2.5"/>')
A('<circle cx="354" cy="78" r="4" fill="url(#rGold)"/>')
for wx in [330, 348, 366]:
    A(f'<rect x="{wx}" y="124" width="10" height="20" fill="#FFA030" opacity="0.30" rx="4"/>')
    A(f'<rect x="{wx}" y="140" width="10" height="6"  fill="#604020" opacity="0.40" rx="2"/>')
A('<rect x="322" y="218" width="64" height="8" fill="#E0A830" opacity="0.60"/>')
for tx in range(326, 384, 8):
    A(f'<circle cx="{tx}" cy="222" r="2" fill="#C08020" opacity="0.60"/>')

# Right market terrace
A('<rect x="322" y="240" width="78" height="80" fill="url(#rBldgSh)" rx="1"/>')
A('<rect x="322" y="240" width="78" height="3"  fill="#E8C060" opacity="0.50"/>')
for ai, ax in enumerate(range(326, 394, 14)):
    col = awning_colors[ai % len(awning_colors)]
    A(f'<rect x="{ax}" y="240" width="10" height="6" fill="{col}" opacity="0.75" rx="1"/>')
for sx in [330, 346, 362, 378]:
    A(f'<rect x="{sx}" y="258" width="10" height="14" fill="#C09040" opacity="0.55" rx="1"/>')
    A(f'<rect x="{sx}" y="270" width="10" height="4"  fill="#A07030" opacity="0.45" rx="1"/>')

# Right lower stone tier
A('<rect x="312" y="330" width="88" height="90" fill="#986830"/>')
A('<rect x="312" y="330" width="88" height="3"  fill="#D0A040" opacity="0.55"/>')
for ci in range(0, 88, 14):
    A(f'<rect x="{312+ci+2}" y="326" width="8" height="10" fill="url(#rBldg)" rx="1"/>')
    A(f'<rect x="{312+ci+2}" y="326" width="8" height="2"  fill="#FFD060" opacity="0.40"/>')
A('<rect x="364" y="352" width="20" height="36" fill="#301808" opacity="0.65" rx="8"/>')
A('<ellipse cx="374" cy="352" rx="10" ry="6" fill="#301808" opacity="0.65"/>')
for bx in [322, 344, 366, 384]:
    A(f'<rect x="{bx}" y="330" width="10" height="22" fill="#702090" opacity="0.85"/>')
    A(f'<rect x="{bx}" y="330" width="10" height="3"  fill="#E8C030" opacity="0.75"/>')
    A(f'<rect x="{bx}" y="348" width="10" height="3"  fill="#E8C030" opacity="0.65"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  7. GROUND PLAZA (stone, warm ochre)
# ─────────────────────────────────────────────────────────────────────────────
A('<rect x="0" y="340" width="400" height="260" fill="url(#rGnd)"/>')

# Flagstone grid
for gx in range(0, 401, 30):
    A(f'<line x1="{gx}" y1="340" x2="{gx}" y2="600" stroke="#785818" stroke-width="0.8" opacity="0.40"/>')
for gy in range(340, 601, 25):
    A(f'<line x1="0" y1="{gy}" x2="400" y2="{gy}" stroke="#785818" stroke-width="0.8" opacity="0.40"/>')

# Central decorative mosaic (geometric tile pattern — Hannish style)
# Octagonal central medallion
A('<circle cx="200" cy="465" r="48" fill="#C09840" opacity="0.35"/>')
A('<circle cx="200" cy="465" r="40" fill="#D0A848" opacity="0.30"/>')
A('<circle cx="200" cy="465" r="30" fill="#E0B850" opacity="0.22"/>')
# Spoke lines
for ang_m in range(0, 360, 45):
    rm = math.radians(ang_m)
    A(f'<line x1="200" y1="465" x2="{200+40*math.cos(rm):.0f}" y2="{465+40*math.sin(rm):.0f}" '
      f'stroke="#B08030" stroke-width="0.8" opacity="0.45"/>')
# Corner tile diamonds
for ang_d in range(22, 360, 45):
    rd = math.radians(ang_d)
    ddx = 200 + 36*math.cos(rd); ddy = 465 + 36*math.sin(rd)
    A(f'<circle cx="{ddx:.1f}" cy="{ddy:.1f}" r="3" fill="#E8A820" opacity="0.50"/>')

# Fountain channel (water flows through plaza)
A('<path d="M200,340 Q200,380 200,420 Q200,460 200,510 Q200,550 200,600" '
  'stroke="#2878A8" stroke-width="8" fill="none" opacity="0.30"/>')
A('<path d="M200,340 Q200,380 200,420 Q200,460 200,510 Q200,550 200,600" '
  'stroke="#60A8D0" stroke-width="3" fill="none" opacity="0.45"/>')
A('<path d="M200,340 Q200,380 200,420 Q200,460 200,510 Q200,550 200,600" '
  'stroke="#C0E8FF" stroke-width="1" fill="none" opacity="0.50"/>')

# Cross-channel
A('<path d="M0,465 Q80,455 160,465 Q200,468 240,465 Q320,455 400,465" '
  'stroke="#2878A8" stroke-width="6" fill="none" opacity="0.28"/>')
A('<path d="M0,465 Q80,455 160,465 Q200,468 240,465 Q320,455 400,465" '
  'stroke="#60A8D0" stroke-width="2.5" fill="none" opacity="0.40"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  8. FOREGROUND TOWERS (close to camera, cut off at bottom)
# ─────────────────────────────────────────────────────────────────────────────
# Left foreground tower
A('<rect x="0" y="400" width="30" height="200" fill="#A07830" rx="2"/>')
A('<rect x="0" y="400" width="10" height="200" fill="#000000" opacity="0.15"/>')
A('<rect x="0" y="400" width="30" height="4"   fill="#D0A040" opacity="0.60"/>')
# Tower detail — tile band
A('<rect x="0" y="440" width="30" height="8" fill="#E0A830" opacity="0.55"/>')
for tx in range(2, 30, 8):
    A(f'<circle cx="{tx}" cy="444" r="2.5" fill="#C08020" opacity="0.60"/>')
# Tower window
A('<rect x="8" y="416" width="14" height="18" fill="#FF9020" opacity="0.40" rx="4"/>')
A('<ellipse cx="15" cy="416" rx="7" ry="4" fill="#FF9020" opacity="0.40"/>')

# Right foreground tower
A('<rect x="370" y="400" width="30" height="200" fill="#A07830" rx="2"/>')
A('<rect x="390" y="400" width="10" height="200" fill="#000000" opacity="0.15"/>')
A('<rect x="370" y="400" width="30" height="4"   fill="#D0A040" opacity="0.60"/>')
A('<rect x="370" y="440" width="30" height="8" fill="#E0A830" opacity="0.55"/>')
for tx in range(372, 400, 8):
    A(f'<circle cx="{tx}" cy="444" r="2.5" fill="#C08020" opacity="0.60"/>')
A('<rect x="378" y="416" width="14" height="18" fill="#FF9020" opacity="0.40" rx="4"/>')
A('<ellipse cx="385" cy="416" rx="7" ry="4" fill="#FF9020" opacity="0.40"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  9. STAGE 5 — ALCHEMICAL BRAZIER / ETERNAL FLAME (translate +52, y≈235)
#  Thavnair / Radz-at-Han: famous for alchemy. An eternal alchemical brazier.
# ─────────────────────────────────────────────────────────────────────────────
A('<g transform="translate(52,0)">')

# Flame ambient glow
A('<ellipse cx="200" cy="255" rx="60" ry="40" fill="url(#rFlame)" opacity="0.28"/>')
A('<ellipse cx="200" cy="262" rx="40" ry="26" fill="#FF8010" opacity="0.16"/>')

# Stone pedestal (tiered, ornate Hannish style)
A('<rect x="176" y="285" width="48" height="8"  fill="#C09840" rx="2"/>')
A('<rect x="180" y="278" width="40" height="7"  fill="#D0A850" rx="2"/>')
A('<rect x="184" y="272" width="32" height="6"  fill="#E0B860" rx="2"/>')
# Pedestal highlights
A('<rect x="176" y="285" width="48" height="2"  fill="#F0D070" opacity="0.55"/>')
A('<rect x="180" y="278" width="40" height="2"  fill="#F0C858" opacity="0.50"/>')
# Geometric tile band on pedestal
for tx in range(178, 224, 8):
    A(f'<circle cx="{tx}" cy="281" r="2.5" fill="#A08020" opacity="0.60"/>')

# Brazier bowl (iron/brass, ornate)
# Bowl body
A('<ellipse cx="200" cy="272" rx="22" ry="10" fill="#4A3010"/>')
A('<ellipse cx="200" cy="270" rx="20" ry="8"  fill="#6A4818"/>')
A('<ellipse cx="200" cy="268" rx="18" ry="6"  fill="#806028"/>')
# Bowl rim (gold-brass)
A('<ellipse cx="200" cy="263" rx="22" ry="5"  fill="#C89820"/>')
A('<ellipse cx="200" cy="262" rx="20" ry="3.5" fill="#E8B828"/>')
A('<ellipse cx="200" cy="261" rx="18" ry="2"  fill="#FFF060" opacity="0.70"/>')
# Brazier legs (three legs visible)
A('<path d="M184,272 L178,290" stroke="#403008" stroke-width="4" stroke-linecap="round"/>')
A('<path d="M200,275 L200,292" stroke="#403008" stroke-width="4" stroke-linecap="round"/>')
A('<path d="M216,272 L222,290" stroke="#403008" stroke-width="4" stroke-linecap="round"/>')
# Leg feet
A('<ellipse cx="178" cy="291" rx="5" ry="2" fill="#302408"/>')
A('<ellipse cx="200" cy="293" rx="5" ry="2" fill="#302408"/>')
A('<ellipse cx="222" cy="291" rx="5" ry="2" fill="#302408"/>')

# THE ALCHEMICAL FLAME — multi-layer, tall, vivid
flame_layers = [
    # (x_center, y_base, paths, fill, opacity)
    ("M186,262 Q178,245 186,228 Q190,212 182,196 Q190,210 196,226 "
     "Q198,208 194,192 Q203,207 200,228 Q204,207 200,192 "
     "Q208,208 206,226 Q210,210 214,196 Q210,214 218,228 "
     "Q222,248 214,262", "#AA2000", 0.82),
    ("M188,262 Q182,246 190,230 Q194,214 190,200 Q198,214 196,232 "
     "Q200,216 198,200 Q207,216 204,232 Q208,216 210,200 "
     "Q214,218 210,232 Q214,248 212,262", "#FF4800", 0.88),
    ("M191,262 Q186,247 194,232 Q198,218 196,206 Q203,220 200,236 "
     "Q204,222 202,208 Q210,224 206,238 Q210,250 208,262", "#FF8010", 0.86),
    ("M194,262 Q190,248 197,235 Q201,224 200,214 Q204,226 202,240 "
     "Q206,230 204,218 Q210,232 207,244 Q210,254 208,262", "#FFB028", 0.83),
    ("M198,256 Q195,242 200,232 Q204,242 202,256", "#FFD840", 0.86),
    ("M199,250 Q197,238 200,229 Q202,238 202,250", "#FFF060", 0.82),
    ("M200,244 Q198,234 200,226 Q202,234 201,244", "#FFFFFF",  0.65),
]
for fp, fc, fo in flame_layers:
    A(f'<path d="{fp}" fill="{fc}" opacity="{fo}"/>')

# Floating embers
embers = [(194,224,1.5,0.85),(207,218,1.2,0.80),(200,210,1.5,0.82),
          (190,208,1.0,0.75),(211,205,1.0,0.72),(196,198,0.9,0.68),
          (204,195,0.9,0.65),(200,188,1.2,0.70),(192,184,0.8,0.62),(208,182,0.8,0.60)]
for ex,ey,er,eo in embers:
    A(f'<circle cx="{ex}" cy="{ey}" r="{er}" fill="#FFC030" opacity="{eo}"/>')
    A(f'<circle cx="{ex}" cy="{ey}" r="{er*2:.1f}" fill="#FF8010" opacity="{eo*0.22:.2f}"/>')

A('</g>')

# ─────────────────────────────────────────────────────────────────────────────
#  10. STAGE 10 — RADZ-AT-HAN GREAT GATE (scale 1.5×, center y=531)
#  Twin minarets, large cobalt dome, ornate Hannish pointed arch
# ─────────────────────────────────────────────────────────────────────────────
A('<g transform="translate(200,531) scale(1.5) translate(-200,-531)">')

# Gate ambient glow (warm lamp light)
A('<ellipse cx="200" cy="530" rx="86" ry="52" fill="#FF9020" opacity="0.08"/>')

# ── LEFT MINARET ─────────────────────────────────────────────────────────────
# Shaft
A('<rect x="142" y="470" width="22" height="90" fill="url(#rGateL)" rx="3"/>')
A('<rect x="142" y="470" width="6"  height="90" fill="#000000" opacity="0.14"/>')
# Balcony rings
for my in [488, 504, 520]:
    A(f'<ellipse cx="153" cy="{my}" rx="15" ry="4" fill="#D0A050" opacity="0.70"/>')
    A(f'<ellipse cx="153" cy="{my}" rx="13" ry="2" fill="#F0C060" opacity="0.55"/>')
# Arrow slits
for wy in [478, 494, 510]:
    A(f'<rect x="150" y="{wy}" width="6" height="10" fill="#301808" opacity="0.60" rx="2"/>')
# Bulbous dome cap
A('<ellipse cx="153" cy="470" rx="15" ry="11" fill="url(#rDome)"/>')
A('<ellipse cx="153" cy="466" rx="10" ry="6"  fill="#5090D8" opacity="0.65"/>')
A('<ellipse cx="151" cy="463" rx="3"  ry="2"  fill="#90C0F0" opacity="0.50"/>')
# Gold finial
A('<line x1="153" y1="459" x2="153" y2="449" stroke="#E8C030" stroke-width="3.5"/>')
A('<line x1="153" y1="459" x2="153" y2="449" stroke="#FFF080" stroke-width="1.4" opacity="0.70"/>')
A('<circle cx="153" cy="447" r="5" fill="url(#rGold)"/>')
A('<circle cx="153" cy="447" r="2.5" fill="#FFFFFF" opacity="0.65"/>')

# ── RIGHT MINARET ─────────────────────────────────────────────────────────────
A('<rect x="236" y="470" width="22" height="90" fill="url(#rGateR)" rx="3"/>')
A('<rect x="252" y="470" width="6"  height="90" fill="#000000" opacity="0.14"/>')
for my in [488, 504, 520]:
    A(f'<ellipse cx="247" cy="{my}" rx="15" ry="4" fill="#D0A050" opacity="0.70"/>')
    A(f'<ellipse cx="247" cy="{my}" rx="13" ry="2" fill="#F0C060" opacity="0.55"/>')
for wy in [478, 494, 510]:
    A(f'<rect x="244" y="{wy}" width="6" height="10" fill="#301808" opacity="0.60" rx="2"/>')
A('<ellipse cx="247" cy="470" rx="15" ry="11" fill="url(#rDome)"/>')
A('<ellipse cx="247" cy="466" rx="10" ry="6"  fill="#5090D8" opacity="0.65"/>')
A('<ellipse cx="249" cy="463" rx="3"  ry="2"  fill="#90C0F0" opacity="0.50"/>')
A('<line x1="247" y1="459" x2="247" y2="449" stroke="#E8C030" stroke-width="3.5"/>')
A('<line x1="247" y1="459" x2="247" y2="449" stroke="#FFF080" stroke-width="1.4" opacity="0.70"/>')
A('<circle cx="247" cy="447" r="5" fill="url(#rGold)"/>')
A('<circle cx="247" cy="447" r="2.5" fill="#FFFFFF" opacity="0.65"/>')

# ── CONNECTING WALL + CENTRAL DOME ────────────────────────────────────────────
# Wall connecting the minarets
A('<rect x="164" y="492" width="72" height="66" fill="url(#rGateL)" rx="2"/>')
A('<rect x="164" y="492" width="10" height="66" fill="#000000" opacity="0.12"/>')
# Wall tile frieze
A('<rect x="164" y="492" width="72" height="5" fill="#E8C030" opacity="0.60"/>')
A('<rect x="164" y="553" width="72" height="5" fill="#E8C030" opacity="0.55"/>')
# Geometric tile pattern on wall face
for ty in [500, 515, 530, 545]:
    for tx in range(168, 232, 10):
        A(f'<rect x="{tx}" y="{ty}" width="6" height="6" fill="#B08028" opacity="0.35" rx="1"/>')

# Central large dome above the gate
A('<ellipse cx="200" cy="492" rx="32" ry="22" fill="url(#rDome)"/>')
A('<ellipse cx="200" cy="486" rx="22" ry="13" fill="#4888D8" opacity="0.60"/>')
A('<ellipse cx="197" cy="482" rx="7"  ry="4"  fill="#80B8F0" opacity="0.50"/>')
# Dome gold trim ring
A('<ellipse cx="200" cy="492" rx="32" ry="5"  fill="none" stroke="#E8C030" stroke-width="2.5"/>')
A('<ellipse cx="200" cy="492" rx="32" ry="5"  fill="none" stroke="#FFF080" stroke-width="0.8" opacity="0.60"/>')
# Dome finial
A('<line x1="200" y1="470" x2="200" y2="458" stroke="#E8C030" stroke-width="3.5"/>')
A('<line x1="200" y1="470" x2="200" y2="458" stroke="#FFF080" stroke-width="1.4" opacity="0.70"/>')
A('<circle cx="200" cy="456" r="6" fill="url(#rGold)"/>')
A('<circle cx="200" cy="456" r="3" fill="#FFFFFF" opacity="0.70"/>')

# ── GATE ARCH (Hannish pointed arch) ─────────────────────────────────────────
# Arch body
A('<path d="M164,530 Q164,504 200,496 Q236,504 236,530" '
  'fill="none" stroke="#C0A040" stroke-width="14"/>')
# Inner arch edge
A('<path d="M168,530 Q168,508 200,501 Q232,508 232,530" '
  'fill="none" stroke="#E8C878" stroke-width="4" opacity="0.50"/>')
# Gold trim along arch
A('<path d="M170,529 Q170,510 200,503 Q230,510 230,529" '
  'fill="none" stroke="#E8C030" stroke-width="2.0" opacity="0.70"/>')
A('<path d="M170,529 Q170,510 200,503 Q230,510 230,529" '
  'fill="none" stroke="#FFF080" stroke-width="0.6" opacity="0.60"/>')

# Arch voussoir joints (radiating lines)
for angle_deg in [208, 222, 236, 250, 264, 278, 292, 306, 320]:
    ang = math.radians(angle_deg)
    cx_a, cy_a = 200, 530
    ro = 36; ri = 22
    x_o = cx_a + ro*math.cos(ang); y_o = cy_a + ro*math.sin(ang)
    x_i = cx_a + ri*math.cos(ang); y_i = cy_a + ri*math.sin(ang)
    A(f'<line x1="{x_i:.1f}" y1="{y_i:.1f}" x2="{x_o:.1f}" y2="{y_o:.1f}" '
      f'stroke="#786020" stroke-width="0.9" opacity="0.55"/>')

# Keystone — Hannish sun motif
A('<circle cx="200" cy="496" r="9"  fill="#D0A830" stroke="#FFC830" stroke-width="2"/>')
for ang_k in range(0, 360, 45):
    rk = math.radians(ang_k)
    kx1 = 200 + 3.5*math.cos(rk); ky1 = 496 + 3.5*math.sin(rk)
    kx2 = 200 + 7.5*math.cos(rk); ky2 = 496 + 7.5*math.sin(rk)
    A(f'<line x1="{kx1:.1f}" y1="{ky1:.1f}" x2="{kx2:.1f}" y2="{ky2:.1f}" '
      f'stroke="#FFF060" stroke-width="1.0" opacity="0.85"/>')
A('<circle cx="200" cy="496" r="3" fill="#FFFFFF" opacity="0.80"/>')

# ── GATE DOORS (rich dark wood, iron-banded) ─────────────────────────────────
# Left door
A('<rect x="168" y="530" width="30" height="28" fill="#2A1808" rx="1"/>')
A('<rect x="168" y="530" width="6"  height="28" fill="#3C2410" opacity="0.50"/>')
# Horizontal iron bands
A('<rect x="168" y="534" width="30" height="2.5" fill="#484030" opacity="0.70"/>')
A('<rect x="168" y="544" width="30" height="2.5" fill="#484030" opacity="0.70"/>')
A('<rect x="168" y="554" width="30" height="2.5" fill="#484030" opacity="0.70"/>')
# Door studs
for sy in [531, 537, 543, 549, 555]:
    for sx in [171, 176, 181, 186, 191]:
        A(f'<circle cx="{sx}" cy="{sy}" r="1.4" fill="#808880" opacity="0.75"/>')
# Door panels
A('<rect x="172" y="532" width="10" height="10" fill="#1A0C04" rx="1"/>')
A('<rect x="184" y="532" width="10" height="10" fill="#1A0C04" rx="1"/>')
A('<rect x="172" y="546" width="22" height="10" fill="#1A0C04" rx="1"/>')

# Right door
A('<rect x="202" y="530" width="30" height="28" fill="#2A1808" rx="1"/>')
A('<rect x="226" y="530" width="6"  height="28" fill="#3C2410" opacity="0.50"/>')
A('<rect x="202" y="534" width="30" height="2.5" fill="#484030" opacity="0.70"/>')
A('<rect x="202" y="544" width="30" height="2.5" fill="#484030" opacity="0.70"/>')
A('<rect x="202" y="554" width="30" height="2.5" fill="#484030" opacity="0.70"/>')
for sy in [531, 537, 543, 549, 555]:
    for sx in [211, 216, 221, 226, 231]:
        A(f'<circle cx="{sx}" cy="{sy}" r="1.4" fill="#808880" opacity="0.75"/>')
A('<rect x="206" y="532" width="10" height="10" fill="#1A0C04" rx="1"/>')
A('<rect x="218" y="532" width="10" height="10" fill="#1A0C04" rx="1"/>')
A('<rect x="206" y="546" width="22" height="10" fill="#1A0C04" rx="1"/>')

# Door centre seam
A('<line x1="200" y1="530" x2="200" y2="558" stroke="#181008" stroke-width="2" opacity="0.80"/>')

# Hanging lamps at gate (amber)
for lx in [172, 200, 228]:
    A(f'<line x1="{lx}" y1="492" x2="{lx}" y2="508" stroke="#806028" stroke-width="1.2" opacity="0.65"/>')
    A(f'<ellipse cx="{lx}" cy="512" rx="5" ry="7" fill="#804010" opacity="0.80"/>')
    A(f'<ellipse cx="{lx}" cy="508" rx="5" ry="2" fill="#C06018" opacity="0.70"/>')
    A(f'<circle  cx="{lx}" cy="512" r="3.5" fill="#FFD040" opacity="0.85"/>')
    A(f'<ellipse cx="{lx}" cy="514" rx="8" ry="5" fill="#FF9020" opacity="0.25"/>')

# Gate base ground stone
A('<rect x="160" y="558" width="80" height="8" fill="#B09030" rx="2"/>')
A('<rect x="160" y="558" width="80" height="2" fill="#E0C040" opacity="0.40"/>')

A('</g>')

# ─────────────────────────────────────────────────────────────────────────────
#  11. ATMOSPHERE OVERLAYS
# ─────────────────────────────────────────────────────────────────────────────
# Bottom warm haze
A('<rect y="488" width="400" height="112" fill="url(#rHaze)" opacity="0.90"/>')
# Ground heat shimmer (very bottom)
A('<rect y="560" width="400" height="40" fill="#D0A030" opacity="0.06"/>')
# Top vignette
A('<rect width="400" height="600" fill="url(#rVig)"/>')

# Seagulls (3 pairs — coastal birds above the harbour)
seagulls = [(150,62),(174,54),(198,68),(222,58),(246,72),(270,60)]
for bx, by in seagulls:
    A(f'<path d="M{bx},{by} Q{bx+5},{by-5} {bx+10},{by}" '
      f'stroke="#FFFFFF" stroke-width="1.5" fill="none" opacity="0.70"/>')
    A(f'<path d="M{bx+10},{by} Q{bx+15},{by-5} {bx+20},{by}" '
      f'stroke="#FFFFFF" stroke-width="1.5" fill="none" opacity="0.70"/>')

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
print(f'  radialGradient: {ro} open, {rc} close')
print(f'  linearGradient: {lo} open, {lc} close')
if ro != rc:
    raise RuntimeError(f'radialGradient mismatch: {ro} vs {rc}')
if lo != lc:
    raise RuntimeError(f'linearGradient mismatch: {lo} vs {lc}')

sq = svg.count("'")
if sq:
    raise RuntimeError(f"Single quotes in SVG: {sq}")

# Also fix the CSS fallback color for EXTREME to match the warm sky
html2 = html
for old, new in [
    ('.map-scroll[data-diff="EXTREME"] { background: #4B5041; }',
     '.map-scroll[data-diff="EXTREME"] { background: #1890D8; }'),
    ('#game-view[data-diff="EXTREME"] { background: rgb(75,80,65); }',
     '#game-view[data-diff="EXTREME"] { background: rgb(24,144,216); }'),
]:
    if old in html2:
        html2 = html2.replace(old, new)

pattern = r"(if\(diff==='EXTREME'\) return ')(.*?)(';)"
repl = lambda m: m.group(1) + svg + m.group(3)
new_html, n = _re.subn(pattern, repl, html2, flags=_re.DOTALL)
if n == 0:
    raise RuntimeError("EXTREME pattern not found")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print(f'stage.html written. ({n} replacement)')
