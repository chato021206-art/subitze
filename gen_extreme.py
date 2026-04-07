#!/usr/bin/env python3
"""gen_extreme.py — EXTREME background: The Crystarium (FF14 Shadowbringers)."""
import re, math

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    html = f.read()

parts = []
def A(s): parts.append(s)

# ─────────────────────────────────────────────────────────────────────────────
#  SVG HEADER
# ─────────────────────────────────────────────────────────────────────────────
A('<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"><defs>')

# Sky: deep indigo/violet night (The First — perpetual dusk)
A('<linearGradient id="cSky" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#04020E"/>'
  '<stop offset="20%"  stop-color="#08051A"/>'
  '<stop offset="45%"  stop-color="#100A2C"/>'
  '<stop offset="70%"  stop-color="#180F3E"/>'
  '<stop offset="100%" stop-color="#201450"/>'
  '</linearGradient>')

# Crystal Tower central glow bloom
A('<radialGradient id="cTowerGlow" cx="50%" cy="5%" r="60%">'
  '<stop offset="0%"   stop-color="#A8D8FF" stop-opacity="0.55"/>'
  '<stop offset="18%"  stop-color="#80B0F0" stop-opacity="0.30"/>'
  '<stop offset="40%"  stop-color="#6090D8" stop-opacity="0.12"/>'
  '<stop offset="65%"  stop-color="#4060A8" stop-opacity="0.04"/>'
  '<stop offset="100%" stop-color="#203080" stop-opacity="0"/>'
  '</radialGradient>')

# Crystal Tower faceted surface (cool icy blue-white)
A('<linearGradient id="cTower" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#7AB0D8"/>'
  '<stop offset="20%"  stop-color="#B8D8F8"/>'
  '<stop offset="42%"  stop-color="#E8F6FF"/>'
  '<stop offset="58%"  stop-color="#FFFFFF"/>'
  '<stop offset="78%"  stop-color="#C0DCF8"/>'
  '<stop offset="100%" stop-color="#80A8CC"/>'
  '</linearGradient>')

# Crystal Tower inner luminescence
A('<radialGradient id="cTowerInner" cx="50%" cy="40%" r="55%">'
  '<stop offset="0%"   stop-color="#FFFFFF"  stop-opacity="0.88"/>'
  '<stop offset="30%"  stop-color="#D0ECFF"  stop-opacity="0.55"/>'
  '<stop offset="60%"  stop-color="#90C0EE"  stop-opacity="0.20"/>'
  '<stop offset="100%" stop-color="#6090D0"  stop-opacity="0"/>'
  '</radialGradient>')

# City-wall stone (left cliff)
A('<linearGradient id="cCliffL" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#3C3028"/>'
  '<stop offset="45%"  stop-color="#6A5848"/>'
  '<stop offset="80%"  stop-color="#988070"/>'
  '<stop offset="100%" stop-color="#B09880"/>'
  '</linearGradient>')

# City-wall stone (right cliff)
A('<linearGradient id="cCliffR" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#B09880"/>'
  '<stop offset="20%"  stop-color="#988070"/>'
  '<stop offset="55%"  stop-color="#6A5848"/>'
  '<stop offset="100%" stop-color="#3C3028"/>'
  '</linearGradient>')

# Wall-top stone (lighter)
A('<linearGradient id="cWallTop" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#D0BEA8"/>'
  '<stop offset="50%"  stop-color="#B0A090"/>'
  '<stop offset="100%" stop-color="#907868"/>'
  '</linearGradient>')

# Crystal formation — teal/azure
A('<linearGradient id="cXtalB" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#C8F4FF"/>'
  '<stop offset="30%"  stop-color="#60C8E8"/>'
  '<stop offset="65%"  stop-color="#1890B8"/>'
  '<stop offset="100%" stop-color="#0A5878"/>'
  '</linearGradient>')

# Crystal formation — violet/purple
A('<linearGradient id="cXtalP" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#E8D0FF"/>'
  '<stop offset="30%"  stop-color="#A870E8"/>'
  '<stop offset="65%"  stop-color="#6030B8"/>'
  '<stop offset="100%" stop-color="#301880"/>'
  '</linearGradient>')

# Crystal formation — gold/amber (rare)
A('<linearGradient id="cXtalG" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FFF0B0"/>'
  '<stop offset="40%"  stop-color="#E8B828"/>'
  '<stop offset="80%"  stop-color="#A07010"/>'
  '<stop offset="100%" stop-color="#604008"/>'
  '</linearGradient>')

# Aetheryte crystal gradient
A('<linearGradient id="cAetheryte" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#E0FFFF"/>'
  '<stop offset="28%"  stop-color="#80EEF8"/>'
  '<stop offset="62%"  stop-color="#20C0D8"/>'
  '<stop offset="100%" stop-color="#0880A0"/>'
  '</linearGradient>')

# Aether glow (teal radial halo)
A('<radialGradient id="cAetherGlow" cx="50%" cy="50%" r="50%">'
  '<stop offset="0%"   stop-color="#40F0E8" stop-opacity="0.75"/>'
  '<stop offset="38%"  stop-color="#20C0B8" stop-opacity="0.38"/>'
  '<stop offset="68%"  stop-color="#10A098" stop-opacity="0.12"/>'
  '<stop offset="100%" stop-color="#008070" stop-opacity="0"/>'
  '</radialGradient>')

# Gate pillar L
A('<linearGradient id="cGateL" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#3C3028"/>'
  '<stop offset="35%"  stop-color="#8A7868"/>'
  '<stop offset="65%"  stop-color="#C0AE9A"/>'
  '<stop offset="100%" stop-color="#A09080"/>'
  '</linearGradient>')

# Gate pillar R
A('<linearGradient id="cGateR" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#A09080"/>'
  '<stop offset="35%"  stop-color="#C0AE9A"/>'
  '<stop offset="65%"  stop-color="#8A7868"/>'
  '<stop offset="100%" stop-color="#3C3028"/>'
  '</linearGradient>')

# Gate arch stone
A('<linearGradient id="cGateArch" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#C8B8A8"/>'
  '<stop offset="50%"  stop-color="#A09080"/>'
  '<stop offset="100%" stop-color="#706050"/>'
  '</linearGradient>')

# Gate door (dark wood)
A('<linearGradient id="cDoor" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#1A100A"/>'
  '<stop offset="35%"  stop-color="#2C1E14"/>'
  '<stop offset="65%"  stop-color="#261810"/>'
  '<stop offset="100%" stop-color="#180C08"/>'
  '</linearGradient>')

# Lantern amber glow
A('<radialGradient id="cLantern" cx="50%" cy="40%" r="55%">'
  '<stop offset="0%"   stop-color="#FFE060" stop-opacity="0.90"/>'
  '<stop offset="30%"  stop-color="#FFA028" stop-opacity="0.48"/>'
  '<stop offset="60%"  stop-color="#FF6808" stop-opacity="0.16"/>'
  '<stop offset="100%" stop-color="#FF4000" stop-opacity="0"/>'
  '</radialGradient>')

# Ground stone plaza
A('<linearGradient id="cGnd" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#3C3428"/>'
  '<stop offset="40%"  stop-color="#2C2418"/>'
  '<stop offset="100%" stop-color="#1C140C"/>'
  '</linearGradient>')

# Aether vein glow (radial)
A('<radialGradient id="cVein" cx="50%" cy="50%" r="50%">'
  '<stop offset="0%"   stop-color="#30D8C8" stop-opacity="0.55"/>'
  '<stop offset="50%"  stop-color="#18B0A0" stop-opacity="0.22"/>'
  '<stop offset="100%" stop-color="#089080" stop-opacity="0"/>'
  '</radialGradient>')

# Bottom mist (atmospheric depth)
A('<linearGradient id="cMist" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#3050A8" stop-opacity="0"/>'
  '<stop offset="55%"  stop-color="#304098" stop-opacity="0.07"/>'
  '<stop offset="100%" stop-color="#203080" stop-opacity="0.22"/>'
  '</linearGradient>')

# Top vignette
A('<linearGradient id="cVig" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#030210" stop-opacity="0.80"/>'
  '<stop offset="22%"  stop-color="#030210" stop-opacity="0.05"/>'
  '<stop offset="100%" stop-color="#030210" stop-opacity="0"/>'
  '</linearGradient>')

# Crystal pendant gradient
A('<linearGradient id="cPendant" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#D0EEFF"/>'
  '<stop offset="50%"  stop-color="#70B8E0"/>'
  '<stop offset="100%" stop-color="#3080B0"/>'
  '</linearGradient>')

A('</defs>')

# ─────────────────────────────────────────────────────────────────────────────
#  1. SKY + GLOW
# ─────────────────────────────────────────────────────────────────────────────
A('<rect width="400" height="600" fill="url(#cSky)"/>')
A('<rect width="400" height="600" fill="url(#cTowerGlow)"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  2. STARS
# ─────────────────────────────────────────────────────────────────────────────
stars = [
    (12,8,1.4,'#FFFFFF',0.94),(42,4,1.6,'#EEF4FF',0.90),(78,14,1.2,'#FFFFFF',0.88),
    (118,6,1.4,'#F0F4FF',0.92),(155,18,1.0,'#E8F0FF',0.84),(202,8,1.5,'#FFFFFF',0.90),
    (238,22,1.2,'#F0F6FF',0.86),(270,10,1.0,'#EEF4FF',0.82),(30,36,1.1,'#FFFFFF',0.82),
    (68,28,0.9,'#E0ECFF',0.76),(102,42,1.1,'#F0F4FF',0.80),(145,32,0.9,'#EEF4FF',0.78),
    (178,44,1.0,'#FFFFFF',0.78),(218,36,0.8,'#E8F0FF',0.72),(252,16,0.8,'#F0F6FF',0.74),
    (285,38,0.9,'#EEF4FF',0.76),(312,12,1.0,'#FFFFFF',0.82),(340,28,0.9,'#EEF4FF',0.78),
    (368,8,1.2,'#FFFFFF',0.86),(390,22,1.0,'#F0F4FF',0.80),(22,52,0.7,'#C8D8FF',0.64),
    (55,58,0.7,'#C8D8FF',0.62),(88,50,0.6,'#D0E0FF',0.60),(130,54,0.8,'#FFFFFF',0.72),
    (165,60,0.7,'#C8D8FF',0.62),(205,52,0.6,'#D0E0FF',0.60),(242,56,0.7,'#C8D8FF',0.62),
    (278,50,0.6,'#D0E0FF',0.58),(315,58,0.7,'#C8D8FF',0.60),(352,44,0.6,'#D0E0FF',0.60),
    (385,52,0.7,'#C8D8FF',0.62),(10,68,0.6,'#A0B8E0',0.52),(48,72,0.5,'#A0B8E0',0.50),
    (88,68,0.6,'#B0C8E8',0.54),(128,74,0.5,'#A0B8E0',0.50),(170,70,0.5,'#A0B8E0',0.48),
    (96,30,1.0,'#A8D0F8',0.70),(184,26,0.9,'#A8D0F8',0.68),(300,20,0.8,'#A0C8F8',0.65),
    (360,36,0.7,'#A8D0F8',0.62),(140,48,0.7,'#B0D4FF',0.60),(260,44,0.7,'#A8D0F8',0.58),
]
for cx,cy,r,col,op in stars:
    A(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" opacity="{op}"/>')

# Nebula wisps behind the tower
A('<ellipse cx="200" cy="80" rx="90" ry="50" fill="#3040A0" opacity="0.12"/>')
A('<ellipse cx="200" cy="60" rx="60" ry="32" fill="#4050C0" opacity="0.08"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  3. CRYSTAL TOWER (central background spire)
# ─────────────────────────────────────────────────────────────────────────────
# Outer glow halos
A('<ellipse cx="200" cy="120" rx="48" ry="80" fill="#6090D8" opacity="0.10"/>')
A('<ellipse cx="200" cy="100" rx="32" ry="60" fill="#80B0F0" opacity="0.14"/>')

# Leftmost facet (shadow)
A('<polygon points="174,0 178,0 190,340 182,340" fill="#6890B8" opacity="0.72"/>')
# Main center facet (bright)
A('<polygon points="178,0 222,0 214,340 186,340" fill="url(#cTower)"/>')
# Right facet (mid-tone)
A('<polygon points="222,0 226,0 218,340 214,340" fill="#90B8D8" opacity="0.80"/>')
# Inner luminescence overlay
A('<polygon points="178,0 222,0 214,340 186,340" fill="url(#cTowerInner)" opacity="0.70"/>')

# Horizontal ring bands
for yb, wd in [(40,44),(80,42),(120,40),(160,38),(200,36),(240,34),(280,32)]:
    xl = 200 - wd//2
    A(f'<rect x="{xl}" y="{yb}" width="{wd}" height="3.5" fill="#C8E8FF" opacity="0.55" rx="1"/>')
    A(f'<rect x="{xl}" y="{yb}" width="{wd}" height="1.5" fill="#FFFFFF" opacity="0.60"/>')

# Facet seam lines
A('<line x1="186" y1="0" x2="186" y2="340" stroke="#9AC0E0" stroke-width="0.8" opacity="0.45"/>')
A('<line x1="200" y1="0" x2="200" y2="340" stroke="#FFFFFF"  stroke-width="0.8" opacity="0.30"/>')
A('<line x1="214" y1="0" x2="214" y2="340" stroke="#9AC0E0" stroke-width="0.8" opacity="0.45"/>')

# Glow corona at tower base
A('<ellipse cx="200" cy="338" rx="20" ry="6" fill="#60C0FF" opacity="0.40"/>')
A('<ellipse cx="200" cy="338" rx="14" ry="4" fill="#A0E0FF" opacity="0.55"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  4. DISTANT CITY SILHOUETTES
# ─────────────────────────────────────────────────────────────────────────────
A('<rect x="20" y="68" width="12" height="60" fill="#0C0A22" opacity="0.80" rx="2"/>')
A('<polygon points="20,68 26,54 32,68" fill="#0E0C24" opacity="0.75"/>')
A('<rect x="22" y="80" width="8" height="5" fill="#80B0F0" opacity="0.22"/>')
A('<rect x="48" y="72" width="10" height="52" fill="#0C0A22" opacity="0.75" rx="2"/>')
A('<polygon points="48,72 53,60 58,72" fill="#0E0C24" opacity="0.70"/>')
A('<rect x="340" y="70" width="12" height="56" fill="#0C0A22" opacity="0.78" rx="2"/>')
A('<polygon points="340,70 346,56 352,70" fill="#0E0C24" opacity="0.74"/>')
A('<rect x="342" y="82" width="8" height="5" fill="#80B0F0" opacity="0.20"/>')
A('<rect x="365" y="75" width="10" height="48" fill="#0C0A22" opacity="0.72" rx="2"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  5. LEFT CLIFF — CRYSTARIUM CITY WALL
# ─────────────────────────────────────────────────────────────────────────────
A('<polygon points="0,0 0,600 142,600 142,310 124,228 106,148 84,80 56,0" fill="url(#cCliffL)"/>')

# Wall face details: horizontal strata lines
for sy in [120, 160, 200, 240, 280, 320, 360, 400, 440, 480]:
    A(f'<line x1="0" y1="{sy}" x2="120" y2="{sy}" stroke="#302018" stroke-width="1.0" opacity="0.35"/>')
for sx in [20, 44, 68, 92, 116]:
    A(f'<line x1="{sx}" y1="120" x2="{sx}" y2="600" stroke="#282010" stroke-width="0.8" opacity="0.30"/>')

# Shadow on left edge
A('<polygon points="0,0 0,600 24,600 24,400 18,300 12,200 6,100 0,0" fill="#000000" opacity="0.25"/>')

# Wall crenellations
for cx, cy in [(60,44),(76,56),(92,68),(108,82),(124,96)]:
    A(f'<rect x="{cx-5}" y="{cy-14}" width="10" height="14" fill="url(#cWallTop)" rx="1"/>')
    A(f'<rect x="{cx-5}" y="{cy-14}" width="10" height="2" fill="#D0C0A8" opacity="0.50"/>')

# Tower 1 — tall round tower near cliff edge
A('<rect x="72" y="68" width="24" height="80" fill="#8A7A6A" rx="4"/>')
A('<rect x="72" y="68" width="24" height="3"  fill="#C0B09A"/>')
A('<polygon points="72,68 84,50 96,68" fill="#A09080"/>')
A('<circle cx="84" cy="60" r="3" fill="#60A0D8" opacity="0.60"/>')
for ws in [78, 86]:
    A(f'<rect x="{ws}" y="82" width="4" height="10" fill="#100808" opacity="0.70" rx="1"/>')
    A(f'<rect x="{ws}" y="100" width="4" height="10" fill="#100808" opacity="0.70" rx="1"/>')
A('<rect x="80" y="118" width="8" height="20" fill="#3090C0" opacity="0.45" rx="2"/>')
A('<rect x="81" y="119" width="6" height="18" fill="#70D0F0" opacity="0.30" rx="1"/>')

# Wide building with arched windows
A('<rect x="24" y="132" width="52" height="120" fill="#786858" rx="2"/>')
A('<rect x="24" y="132" width="52" height="4"   fill="#B0A090"/>')
for wx in [32, 48, 60]:
    A(f'<rect x="{wx}" y="148" width="8" height="14" fill="#FFA030" opacity="0.55" rx="3"/>')
    A(f'<rect x="{wx}" y="160" width="8" height="5"  fill="#604020" opacity="0.60"/>')
A('<rect x="36" y="130" width="6" height="24" fill="url(#cXtalB)" opacity="0.60" rx="1"/>')
A('<rect x="52" y="130" width="6" height="24" fill="url(#cXtalB)" opacity="0.55" rx="1"/>')

# Terrace building
A('<rect x="0" y="252" width="60" height="80" fill="#6A5A48"/>')
A('<rect x="0" y="252" width="60" height="3"  fill="#B0A088"/>')
for wx in [8, 24, 40]:
    A(f'<rect x="{wx}" y="268" width="10" height="14" fill="#FFA040" opacity="0.48" rx="2"/>')
A('<ellipse cx="30" cy="258" rx="16" ry="8" fill="url(#cLantern)" opacity="0.70"/>')
A('<ellipse cx="30" cy="260" rx="5"  ry="4" fill="#FFE070" opacity="0.90"/>')
A('<rect x="28" y="256" width="4" height="10" fill="#604020" opacity="0.60"/>')

# Lower terrace wall
A('<rect x="0" y="340" width="70" height="100" fill="#5E4E3C"/>')
A('<rect x="0" y="340" width="70" height="3"   fill="#A89878"/>')
A('<polygon points="16,340 20,318 24,340" fill="url(#cXtalB)" opacity="0.70"/>')
A('<polygon points="22,340 25,322 28,340" fill="url(#cXtalP)" opacity="0.65"/>')
A('<polygon points="28,340 31,326 34,340" fill="url(#cXtalB)" opacity="0.60"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  6. RIGHT CLIFF — CRYSTARIUM CITY WALL
# ─────────────────────────────────────────────────────────────────────────────
A('<polygon points="400,0 400,600 258,600 258,310 276,228 294,148 316,80 344,0" fill="url(#cCliffR)"/>')

for sy in [120, 160, 200, 240, 280, 320, 360, 400, 440, 480]:
    A(f'<line x1="280" y1="{sy}" x2="400" y2="{sy}" stroke="#302018" stroke-width="1.0" opacity="0.35"/>')
for sx in [280, 306, 330, 356, 380]:
    A(f'<line x1="{sx}" y1="120" x2="{sx}" y2="600" stroke="#282010" stroke-width="0.8" opacity="0.30"/>')

A('<polygon points="400,0 400,600 376,600 376,400 382,300 388,200 394,100 400,0" fill="#000000" opacity="0.25"/>')

for cx, cy in [(276,96),(292,82),(308,68),(324,56),(340,44)]:
    A(f'<rect x="{cx-5}" y="{cy-14}" width="10" height="14" fill="url(#cWallTop)" rx="1"/>')
    A(f'<rect x="{cx-5}" y="{cy-14}" width="10" height="2" fill="#D0C0A8" opacity="0.50"/>')

# Tower 1 — right
A('<rect x="304" y="68" width="24" height="80" fill="#8A7A6A" rx="4"/>')
A('<rect x="304" y="68" width="24" height="3"  fill="#C0B09A"/>')
A('<polygon points="304,68 316,50 328,68" fill="#A09080"/>')
A('<circle cx="316" cy="60" r="3" fill="#60A0D8" opacity="0.60"/>')
for ws in [310, 318]:
    A(f'<rect x="{ws}" y="82" width="4" height="10" fill="#100808" opacity="0.70" rx="1"/>')
    A(f'<rect x="{ws}" y="100" width="4" height="10" fill="#100808" opacity="0.70" rx="1"/>')
A('<rect x="312" y="118" width="8" height="20" fill="#3090C0" opacity="0.45" rx="2"/>')
A('<rect x="313" y="119" width="6" height="18" fill="#70D0F0" opacity="0.30" rx="1"/>')

A('<rect x="324" y="132" width="52" height="120" fill="#786858" rx="2"/>')
A('<rect x="324" y="132" width="52" height="4"   fill="#B0A090"/>')
for wx in [332, 348, 360]:
    A(f'<rect x="{wx}" y="148" width="8" height="14" fill="#FFA030" opacity="0.55" rx="3"/>')
    A(f'<rect x="{wx}" y="160" width="8" height="5"  fill="#604020" opacity="0.60"/>')
A('<rect x="338" y="130" width="6" height="24" fill="url(#cXtalB)" opacity="0.60" rx="1"/>')
A('<rect x="354" y="130" width="6" height="24" fill="url(#cXtalB)" opacity="0.55" rx="1"/>')

A('<rect x="340" y="252" width="60" height="80" fill="#6A5A48"/>')
A('<rect x="340" y="252" width="60" height="3"  fill="#B0A088"/>')
for wx in [352, 368, 384]:
    A(f'<rect x="{wx}" y="268" width="10" height="14" fill="#FFA040" opacity="0.48" rx="2"/>')
A('<ellipse cx="370" cy="258" rx="16" ry="8" fill="url(#cLantern)" opacity="0.70"/>')
A('<ellipse cx="370" cy="260" rx="5"  ry="4" fill="#FFE070" opacity="0.90"/>')
A('<rect x="368" y="256" width="4" height="10" fill="#604020" opacity="0.60"/>')

A('<rect x="330" y="340" width="70" height="100" fill="#5E4E3C"/>')
A('<rect x="330" y="340" width="70" height="3"   fill="#A89878"/>')
A('<polygon points="366,340 370,318 374,340" fill="url(#cXtalB)" opacity="0.70"/>')
A('<polygon points="372,340 375,322 378,340" fill="url(#cXtalP)" opacity="0.65"/>')
A('<polygon points="378,340 381,326 384,340" fill="url(#cXtalB)" opacity="0.60"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  7. PLAZA / GROUND
# ─────────────────────────────────────────────────────────────────────────────
A('<rect x="0" y="338" width="400" height="262" fill="url(#cGnd)"/>')

for gx in range(0, 401, 28):
    A(f'<line x1="{gx}" y1="338" x2="{gx}" y2="600" stroke="#2A2010" stroke-width="0.7" opacity="0.40"/>')
for gy in range(338, 601, 24):
    A(f'<line x1="0" y1="{gy}" x2="400" y2="{gy}" stroke="#2A2010" stroke-width="0.7" opacity="0.40"/>')

# Crystal vein lines glowing in the stone
vein_paths = [
    "M0,380 Q60,370 100,390 Q150,410 200,385 Q250,360 300,380 Q360,400 400,375",
    "M0,420 Q80,410 140,430 Q190,448 240,420 Q300,395 400,415",
    "M60,338 Q90,360 110,400 Q120,440 115,480",
    "M340,338 Q310,360 290,400 Q280,440 285,480",
    "M180,338 Q195,365 190,395 Q185,425 200,460",
]
for vp in vein_paths:
    A(f'<path d="{vp}" stroke="#20D0C0" stroke-width="1.8" fill="none" opacity="0.35"/>')
    A(f'<path d="{vp}" stroke="#60F8F0" stroke-width="0.7" fill="none" opacity="0.50"/>')

vein_glows = [(100,390),(200,385),(300,380),(140,430),(240,420),(110,450),(290,440),(190,420)]
for gx, gy in vein_glows:
    A(f'<ellipse cx="{gx}" cy="{gy}" rx="18" ry="8" fill="url(#cVein)" opacity="0.35"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  8. CRYSTAL FORMATIONS
# ─────────────────────────────────────────────────────────────────────────────
def crystal_cluster(cx, base_y, crystals, grad, base_op=0.85):
    for dx, height, w, op_mult in crystals:
        x = cx + dx
        hw = w / 2
        pts = f"{x-hw},{base_y} {x},{base_y-height} {x+hw},{base_y}"
        A(f'<polygon points="{pts}" fill="url(#{grad})" opacity="{base_op*op_mult:.2f}"/>')
        A(f'<line x1="{x}" y1="{base_y}" x2="{x-hw*0.3:.1f}" y2="{base_y-height*0.7:.1f}" '
          f'stroke="#C0F0FF" stroke-width="0.8" opacity="0.45"/>')

crystal_cluster(52,  348, [(-18,52,14,1.0),(-8,68,18,0.95),(4,45,12,0.90),(14,72,20,1.0),(24,40,10,0.85)], 'cXtalB')
crystal_cluster(88,  342, [(-8,35,10,0.90),(2,48,14,1.0),(12,32,10,0.88)], 'cXtalP')
crystal_cluster(348, 348, [(-24,40,10,0.85),(-14,72,20,1.0),(-4,45,12,0.90),(8,68,18,0.95),(18,52,14,1.0)], 'cXtalB')
crystal_cluster(312, 342, [(-12,32,10,0.88),(-2,48,14,1.0),(8,35,10,0.90)], 'cXtalP')
crystal_cluster(22,  360, [(-6,38,10,0.90),(4,52,14,1.0),(14,30,8,0.85)], 'cXtalG')
crystal_cluster(30,  440, [(-4,28,8,0.80),(6,40,12,0.90),(16,24,8,0.78)], 'cXtalB', 0.70)
crystal_cluster(370, 440, [(-16,24,8,0.78),(-6,40,12,0.90),(4,28,8,0.80)], 'cXtalP', 0.70)

# ─────────────────────────────────────────────────────────────────────────────
#  9. FLOATING AETHER WISPS
# ─────────────────────────────────────────────────────────────────────────────
wisps_teal = [
    (58,320,3.0,2.0,0.85),(92,356,2.5,1.8,0.78),(136,298,2.0,1.5,0.72),
    (172,332,2.5,1.8,0.76),(240,310,2.0,1.5,0.74),(288,344,3.0,2.0,0.82),
    (326,302,2.5,1.8,0.76),(364,338,2.0,1.5,0.70),(44,470,2.0,1.5,0.68),
    (108,490,2.5,1.8,0.72),(200,458,3.0,2.2,0.80),(296,482,2.5,1.8,0.70),
    (352,468,2.0,1.5,0.65),
]
for wx,wy,wr,wr2,op in wisps_teal:
    A(f'<ellipse cx="{wx}" cy="{wy}" rx="{wr}" ry="{wr2}" fill="#30F0E0" opacity="{op}"/>')
    A(f'<ellipse cx="{wx}" cy="{wy}" rx="{wr*2.5:.1f}" ry="{wr2*2.5:.1f}" fill="#10C0B0" opacity="0.22"/>')

wisps_purple = [
    (70,348,2.5,1.8,0.80),(118,376,2.0,1.5,0.72),(156,412,2.5,1.8,0.76),
    (248,388,2.0,1.5,0.72),(300,416,2.5,1.8,0.78),(338,374,2.0,1.5,0.70),
]
for wx,wy,wr,wr2,op in wisps_purple:
    A(f'<ellipse cx="{wx}" cy="{wy}" rx="{wr}" ry="{wr2}" fill="#C070FF" opacity="{op}"/>')
    A(f'<ellipse cx="{wx}" cy="{wy}" rx="{wr*2.2:.1f}" ry="{wr2*2.2:.1f}" fill="#9040D0" opacity="0.20"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  10. BANNERS, LANTERNS, PENDANTS
# ─────────────────────────────────────────────────────────────────────────────
# Left wall banners
for bx, by in [(18, 200), (42, 230), (66, 264)]:
    A(f'<rect x="{bx}" y="{by}" width="14" height="24" fill="#1C1450" opacity="0.92"/>')
    A(f'<rect x="{bx}" y="{by}" width="14" height="3"  fill="#D0A828" opacity="0.80"/>')
    A(f'<rect x="{bx}" y="{by+20}" width="14" height="3" fill="#D0A828" opacity="0.70"/>')
    A(f'<polygon points="{bx+7},{by+6} {bx+4},{by+16} {bx+10},{by+16}" fill="#60C0F0" opacity="0.55"/>')

# Right wall banners
for bx, by in [(378, 200), (354, 230), (330, 264)]:
    A(f'<rect x="{bx}" y="{by}" width="14" height="24" fill="#1C1450" opacity="0.92"/>')
    A(f'<rect x="{bx}" y="{by}" width="14" height="3"  fill="#D0A828" opacity="0.80"/>')
    A(f'<rect x="{bx}" y="{by+20}" width="14" height="3" fill="#D0A828" opacity="0.70"/>')
    A(f'<polygon points="{bx+7},{by+6} {bx+4},{by+16} {bx+10},{by+16}" fill="#60C0F0" opacity="0.55"/>')

# Left wall lanterns
for lx, ly in [(30, 196), (56, 228), (80, 258)]:
    A(f'<ellipse cx="{lx}" cy="{ly}" rx="12" ry="6" fill="url(#cLantern)" opacity="0.65"/>')
    A(f'<circle  cx="{lx}" cy="{ly}" r="4" fill="#FFE070" opacity="0.88"/>')
    A(f'<rect x="{lx-1}" y="{ly-6}" width="2" height="6" fill="#403020" opacity="0.60"/>')

# Right wall lanterns
for lx, ly in [(370, 196), (344, 228), (320, 258)]:
    A(f'<ellipse cx="{lx}" cy="{ly}" rx="12" ry="6" fill="url(#cLantern)" opacity="0.65"/>')
    A(f'<circle  cx="{lx}" cy="{ly}" r="4" fill="#FFE070" opacity="0.88"/>')
    A(f'<rect x="{lx-1}" y="{ly-6}" width="2" height="6" fill="#403020" opacity="0.60"/>')

# Crystal pendant chains (signature Crystarium detail)
pendant_data_l = [(36,170,22),(54,186,28),(70,200,20),(86,218,32),(110,236,26)]
for px, py, plen in pendant_data_l:
    A(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{py+plen}" stroke="#9090A8" stroke-width="0.8" opacity="0.60"/>')
    A(f'<ellipse cx="{px}" cy="{py+plen+5}" rx="4" ry="7" fill="url(#cPendant)" opacity="0.80"/>')
    A(f'<ellipse cx="{px}" cy="{py+plen+3}" rx="2" ry="2" fill="#E0F8FF" opacity="0.70"/>')
    A(f'<ellipse cx="{px}" cy="{py+plen+5}" rx="5" ry="8" fill="#60B8E8" opacity="0.18"/>')

pendant_data_r = [(364,170,22),(346,186,28),(330,200,20),(314,218,32),(290,236,26)]
for px, py, plen in pendant_data_r:
    A(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{py+plen}" stroke="#9090A8" stroke-width="0.8" opacity="0.60"/>')
    A(f'<ellipse cx="{px}" cy="{py+plen+5}" rx="4" ry="7" fill="url(#cPendant)" opacity="0.80"/>')
    A(f'<ellipse cx="{px}" cy="{py+plen+3}" rx="2" ry="2" fill="#E0F8FF" opacity="0.70"/>')
    A(f'<ellipse cx="{px}" cy="{py+plen+5}" rx="5" ry="8" fill="#60B8E8" opacity="0.18"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  11. STAGE 5 — AETHERYTE SHARD (translate +52, visible at y≈235)
# ─────────────────────────────────────────────────────────────────────────────
A('<g transform="translate(52,0)">')

# Aether glow halo
A('<ellipse cx="200" cy="260" rx="66" ry="38" fill="url(#cAetherGlow)" opacity="0.40"/>')
A('<ellipse cx="200" cy="260" rx="44" ry="26" fill="#20D0C8" opacity="0.18"/>')

# Stone plinth (3-tier)
A('<rect x="178" y="280" width="44" height="8"  fill="#706050" rx="2"/>')
A('<rect x="182" y="272" width="36" height="8"  fill="#806A58" rx="2"/>')
A('<rect x="186" y="265" width="28" height="7"  fill="#907868" rx="2"/>')
A('<rect x="178" y="280" width="44" height="2"  fill="#A09080" opacity="0.50"/>')
A('<rect x="182" y="272" width="36" height="2"  fill="#A89878" opacity="0.45"/>')

# Main Aetheryte crystal (faceted hexagon shape)
axy = [(200,240),(180,258),(184,276),(200,280),(216,276),(220,258)]
pts_main = " ".join(f"{x},{y}" for x,y in axy)
A(f'<polygon points="{pts_main}" fill="url(#cAetheryte)"/>')
A(f'<polygon points="{pts_main}" fill="url(#cTowerInner)" opacity="0.55"/>')
A('<polygon points="200,240 180,258 184,276 200,268" fill="#1A80A0" opacity="0.60"/>')
A('<polygon points="200,240 220,258 216,276 200,268" fill="#C0F0FF" opacity="0.50"/>')
A('<line x1="200" y1="240" x2="200" y2="280" stroke="#FFFFFF" stroke-width="0.8" opacity="0.55"/>')
A('<line x1="180" y1="258" x2="220" y2="258" stroke="#A0E8F8" stroke-width="0.7" opacity="0.40"/>')

# Flanking smaller shards
A('<polygon points="178,264 168,250 174,278" fill="url(#cXtalB)" opacity="0.80"/>')
A('<line x1="168" y1="250" x2="172" y2="264" stroke="#C0F0FF" stroke-width="0.6" opacity="0.45"/>')
A('<polygon points="222,264 232,250 226,278" fill="url(#cXtalB)" opacity="0.80"/>')
A('<line x1="232" y1="250" x2="228" y2="264" stroke="#C0F0FF" stroke-width="0.6" opacity="0.45"/>')
A('<polygon points="188,278 184,264 192,278" fill="url(#cXtalP)" opacity="0.75"/>')
A('<polygon points="212,278 208,264 216,278" fill="url(#cXtalP)" opacity="0.75"/>')

# Aetheryte registration glow
A('<circle cx="200" cy="260" r="6"  fill="#A0F0F8" opacity="0.80"/>')
A('<circle cx="200" cy="260" r="10" fill="#40D0E0" opacity="0.30"/>')
A('<circle cx="200" cy="260" r="16" fill="#20B0C0" opacity="0.14"/>')

# Orbiting aether sparks
for ang in range(0, 360, 45):
    rad = math.radians(ang)
    sx = 200 + 22 * math.cos(rad)
    sy = 260 + 14 * math.sin(rad)
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="1.6" fill="#40F0E8" opacity="0.75"/>')
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="3.0" fill="#20D0C8" opacity="0.22"/>')

A('<ellipse cx="200" cy="284" rx="36" ry="8" fill="#20D0C0" opacity="0.28"/>')
A('</g>')

# ─────────────────────────────────────────────────────────────────────────────
#  12. STAGE 10 — CRYSTARIUM MAIN GATE (scale 1.5×, center y=531)
# ─────────────────────────────────────────────────────────────────────────────
A('<g transform="translate(200,531) scale(1.5) translate(-200,-531)">')

# Gate aura
A('<ellipse cx="200" cy="531" rx="90" ry="52" fill="url(#cAetherGlow)" opacity="0.22"/>')
A('<ellipse cx="200" cy="531" rx="60" ry="36" fill="#40D0C8" opacity="0.10"/>')

# LEFT PILLAR
A('<rect x="148" y="487" width="28" height="70" fill="url(#cGateL)" rx="2"/>')
A('<rect x="149" y="487" width="7"  height="70" fill="#D0C0B0" opacity="0.30"/>')
A('<rect x="160" y="494" width="8"  height="50" fill="url(#cXtalB)" opacity="0.50" rx="2"/>')
A('<rect x="161" y="495" width="6"  height="48" fill="#80E8FF" opacity="0.28" rx="1"/>')
A('<rect x="147" y="487" width="30" height="4"  fill="#D0A828" rx="1"/>')
A('<rect x="147" y="552" width="30" height="4"  fill="#D0A828" rx="1"/>')
A('<rect x="147" y="520" width="30" height="3"  fill="#D0A828" opacity="0.60" rx="1"/>')
for ci in range(5):
    A(f'<rect x="{149+ci*6}" y="483" width="4" height="7" fill="url(#cWallTop)" rx="1"/>')

# RIGHT PILLAR
A('<rect x="224" y="487" width="28" height="70" fill="url(#cGateR)" rx="2"/>')
A('<rect x="244" y="487" width="7"  height="70" fill="#D0C0B0" opacity="0.30"/>')
A('<rect x="232" y="494" width="8"  height="50" fill="url(#cXtalB)" opacity="0.50" rx="2"/>')
A('<rect x="233" y="495" width="6"  height="48" fill="#80E8FF" opacity="0.28" rx="1"/>')
A('<rect x="223" y="487" width="30" height="4"  fill="#D0A828" rx="1"/>')
A('<rect x="223" y="552" width="30" height="4"  fill="#D0A828" rx="1"/>')
A('<rect x="223" y="520" width="30" height="3"  fill="#D0A828" opacity="0.60" rx="1"/>')
for ci in range(5):
    A(f'<rect x="{225+ci*6}" y="483" width="4" height="7" fill="url(#cWallTop)" rx="1"/>')

# ARCH
A('<path d="M148,520 Q148,490 200,482 Q252,490 252,520" '
  'fill="none" stroke="url(#cGateArch)" stroke-width="14"/>')
A('<path d="M152,520 Q152,494 200,487 Q248,494 248,520" '
  'fill="none" stroke="#C0AE9A" stroke-width="4" opacity="0.45"/>')
A('<path d="M155,519 Q155,497 200,490 Q245,497 245,519" '
  'fill="none" stroke="#40D0C8" stroke-width="2.5" opacity="0.55"/>')
A('<path d="M155,519 Q155,497 200,490 Q245,497 245,519" '
  'fill="none" stroke="#80F0EE" stroke-width="0.8" opacity="0.65"/>')

# Voussoir joints
for angle_deg in [210, 225, 240, 255, 270, 285, 300, 315, 330]:
    ang = math.radians(angle_deg)
    x_o = 200 + 52 * math.cos(ang)
    y_o = 520 + 38 * math.sin(ang)
    x_i = 200 + 39 * math.cos(ang)
    y_i = 520 + 25 * math.sin(ang)
    A(f'<line x1="{x_i:.1f}" y1="{y_i:.1f}" x2="{x_o:.1f}" y2="{y_o:.1f}" '
      f'stroke="#584838" stroke-width="1.0" opacity="0.60"/>')

# Keystone — crystal motif
A('<circle cx="200" cy="482" r="8" fill="#1A1840" stroke="#D0A828" stroke-width="2"/>')
A('<polygon points="200,474 196,483 204,483" fill="#60D0F0" opacity="0.85"/>')
A('<circle cx="200" cy="482" r="4" fill="#A0E8FF" opacity="0.80"/>')
A('<circle cx="200" cy="482" r="6" fill="#60C0E0" opacity="0.30"/>')

# Hanging crystal pendants from arch
for px, py_top, plen in [(186,495,18),(200,490,22),(214,495,18)]:
    A(f'<line x1="{px}" y1="{py_top}" x2="{px}" y2="{py_top+plen}" '
      f'stroke="#9090B8" stroke-width="0.9" opacity="0.65"/>')
    A(f'<ellipse cx="{px}" cy="{py_top+plen+5}" rx="4" ry="7" fill="url(#cPendant)" opacity="0.85"/>')
    A(f'<ellipse cx="{px}" cy="{py_top+plen+3}" rx="2" ry="2" fill="#E0FAFF" opacity="0.75"/>')
    A(f'<ellipse cx="{px}" cy="{py_top+plen+5}" rx="5" ry="8" fill="#50A8D8" opacity="0.20"/>')

# GATE DOORS
A('<rect x="152" y="520" width="46" height="37" fill="url(#cDoor)" rx="1"/>')
A('<rect x="152" y="520" width="6"  height="37" fill="#3C2818" opacity="0.50"/>')
A('<rect x="158" y="524" width="18" height="14" fill="#120C08" rx="1"/>')
A('<rect x="158" y="540" width="18" height="14" fill="#120C08" rx="1"/>')
for sy in [526, 530, 534, 538, 542, 546, 550]:
    for sx in [161, 166, 171]:
        A(f'<circle cx="{sx}" cy="{sy}" r="1.2" fill="#606878" opacity="0.75"/>')
A('<rect x="162" y="525" width="10" height="12" fill="#60C0E0" opacity="0.25" rx="1"/>')

A('<rect x="202" y="520" width="46" height="37" fill="url(#cDoor)" rx="1"/>')
A('<rect x="242" y="520" width="6"  height="37" fill="#3C2818" opacity="0.50"/>')
A('<rect x="224" y="524" width="18" height="14" fill="#120C08" rx="1"/>')
A('<rect x="224" y="540" width="18" height="14" fill="#120C08" rx="1"/>')
for sy in [526, 530, 534, 538, 542, 546, 550]:
    for sx in [227, 232, 237]:
        A(f'<circle cx="{sx}" cy="{sy}" r="1.2" fill="#606878" opacity="0.75"/>')
A('<rect x="228" y="525" width="10" height="12" fill="#60C0E0" opacity="0.25" rx="1"/>')
A('<line x1="200" y1="520" x2="200" y2="557" stroke="#303028" stroke-width="1.5" opacity="0.70"/>')

# Flanking crystal pillars
A('<polygon points="136,520 140,490 144,520" fill="url(#cXtalB)" opacity="0.80"/>')
A('<polygon points="138,520 142,494 146,520" fill="#C0F0FF" opacity="0.30"/>')
A('<ellipse cx="141" cy="520" rx="8" ry="3" fill="#20C0D0" opacity="0.45"/>')
A('<ellipse cx="141" cy="518" rx="4" ry="6" fill="url(#cAetherGlow)" opacity="0.50"/>')
A('<polygon points="256,520 260,490 264,520" fill="url(#cXtalB)" opacity="0.80"/>')
A('<polygon points="254,520 258,494 262,520" fill="#C0F0FF" opacity="0.30"/>')
A('<ellipse cx="260" cy="520" rx="8" ry="3" fill="#20C0D0" opacity="0.45"/>')
A('<ellipse cx="260" cy="518" rx="4" ry="6" fill="url(#cAetherGlow)" opacity="0.50"/>')

# Gate ground aether
A('<ellipse cx="200" cy="557" rx="55" ry="12" fill="#18B0A8" opacity="0.25"/>')
A('<ellipse cx="200" cy="557" rx="35" ry="7"  fill="#30D0C8" opacity="0.30"/>')

A('</g>')

# ─────────────────────────────────────────────────────────────────────────────
#  13. FOREGROUND ELEMENTS
# ─────────────────────────────────────────────────────────────────────────────
crystal_cluster(18, 570, [(-4,55,14,1.0),(8,70,18,0.95),(20,48,12,0.88)], 'cXtalB', 0.80)
crystal_cluster(382, 570, [(-20,48,12,0.88),(-8,70,18,0.95),(4,55,14,1.0)], 'cXtalP', 0.80)

A('<polygon points="0,520 8,440 24,520" fill="url(#cXtalB)" opacity="0.72"/>')
A('<polygon points="0,520 6,450 14,520" fill="#A0E8FF" opacity="0.30"/>')
A('<polygon points="380,520 392,440 400,520" fill="url(#cXtalP)" opacity="0.70"/>')
A('<polygon points="386,520 394,452 400,520" fill="#D0C0FF" opacity="0.28"/>')

for bx in range(0, 120, 16):
    ht = 12 + (bx % 24)
    A(f'<polygon points="{bx+2},{440} {bx+6},{440-ht} {bx+10},{440}" fill="url(#cXtalB)" opacity="0.45"/>')
for bx in range(280, 400, 16):
    ht = 12 + (bx % 24)
    A(f'<polygon points="{bx+2},{440} {bx+6},{440-ht} {bx+10},{440}" fill="url(#cXtalP)" opacity="0.40"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  14. ATMOSPHERE OVERLAYS
# ─────────────────────────────────────────────────────────────────────────────
A('<rect y="490" width="400" height="110" fill="url(#cMist)" opacity="0.85"/>')
A('<ellipse cx="200" cy="595" rx="200" ry="20" fill="#283070" opacity="0.15"/>')
A('<rect width="400" height="600" fill="url(#cVig)"/>')

# Crystal Tower light rays (very subtle)
for ang in [-22, -12, -5, 0, 5, 12, 22]:
    rad = math.radians(90 + ang)
    lx = 200 + 300 * math.cos(rad)
    ly = 300 * math.sin(rad)
    op = max(0.001, 0.06 - abs(ang) * 0.002)
    sw = max(0.1, 1.5 - abs(ang) * 0.04)
    A(f'<line x1="200" y1="0" x2="{lx:.0f}" y2="{ly:.0f}" '
      f'stroke="#A0D0FF" stroke-width="{sw:.1f}" opacity="{op:.3f}"/>')

A('</svg>')

# ─────────────────────────────────────────────────────────────────────────────
#  INJECT INTO stage.html
# ─────────────────────────────────────────────────────────────────────────────
svg = ''.join(parts)
print(f'EXTREME SVG: {len(svg):,} chars')

# Validate: check gradient tag balance
import re as _re
ro = len(_re.findall(r'<radialGradient', svg))
rc = len(_re.findall(r'</radialGradient', svg))
lo = len(_re.findall(r'<linearGradient', svg))
lc = len(_re.findall(r'</linearGradient', svg))
print(f'  radialGradient: {ro} open, {rc} close')
print(f'  linearGradient: {lo} open, {lc} close')
if ro != rc or lo != lc:
    raise RuntimeError(f'Gradient tag mismatch! Aborting.')

pattern = r"(if\(diff==='EXTREME'\) return ')(.*?)(';)"
repl = lambda m: m.group(1) + svg + m.group(3)
new_html, n = _re.subn(pattern, repl, html, flags=_re.DOTALL)
if n == 0:
    raise RuntimeError("EXTREME pattern not found in stage.html")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print(f'stage.html written. ({n} replacement)')
