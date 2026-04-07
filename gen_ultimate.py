#!/usr/bin/env python3
"""gen_ultimate.py — ULTIMATE background: Elpis (FF14 Endwalker).
The ancient garden of creation — 12,000 years in the past.
Warm lavender-gold sky, Amaurotine marble research halls, impossible
fantastical flora, glowing aether motes, floating islands, creation altar.
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

# Sky: deep violet → rose-lavender → warm coral → gold horizon
A('<linearGradient id="eSky" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#2A0848"/>'
  '<stop offset="18%"  stop-color="#601868"/>'
  '<stop offset="38%"  stop-color="#A04888"/>'
  '<stop offset="58%"  stop-color="#D0709A"/>'
  '<stop offset="78%"  stop-color="#E89868"/>'
  '<stop offset="100%" stop-color="#F8C870"/>'
  '</linearGradient>')

# Ethereal light bloom (warm upper-center — Elpis has no harsh sun, just diffuse warm light)
A('<radialGradient id="eLight" cx="42%" cy="10%" r="65%">'
  '<stop offset="0%"   stop-color="#FFE8C0" stop-opacity="0.72"/>'
  '<stop offset="20%"  stop-color="#F8C898" stop-opacity="0.45"/>'
  '<stop offset="45%"  stop-color="#E8A070" stop-opacity="0.20"/>'
  '<stop offset="72%"  stop-color="#D07888" stop-opacity="0.06"/>'
  '<stop offset="100%" stop-color="#A85080" stop-opacity="0"/>'
  '</radialGradient>')

# Aether horizon glow (teal-gold near ground)
A('<radialGradient id="eHorizon" cx="50%" cy="85%" r="60%">'
  '<stop offset="0%"   stop-color="#80F0D0" stop-opacity="0.40"/>'
  '<stop offset="35%"  stop-color="#40C8A8" stop-opacity="0.18"/>'
  '<stop offset="68%"  stop-color="#20A888" stop-opacity="0.06"/>'
  '<stop offset="100%" stop-color="#108060" stop-opacity="0"/>'
  '</radialGradient>')

# Amaurotine marble (ivory-white)
A('<linearGradient id="eMarble" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FAFAF5"/>'
  '<stop offset="35%"  stop-color="#EEEAE0"/>'
  '<stop offset="70%"  stop-color="#DDD8CC"/>'
  '<stop offset="100%" stop-color="#C8C4B8"/>'
  '</linearGradient>')

# Marble shadow side
A('<linearGradient id="eMarbleSh" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#C0BCAF"/>'
  '<stop offset="40%"  stop-color="#D8D5C8"/>'
  '<stop offset="100%" stop-color="#EEEAE0"/>'
  '</linearGradient>')

# Marble cliff face (warm stone, slightly darker)
A('<linearGradient id="eCliffL" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#8C8478"/>'
  '<stop offset="40%"  stop-color="#B8B0A0"/>'
  '<stop offset="75%"  stop-color="#D8D0C0"/>'
  '<stop offset="100%" stop-color="#E8E0D0"/>'
  '</linearGradient>')

A('<linearGradient id="eCliffR" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#E8E0D0"/>'
  '<stop offset="25%"  stop-color="#D8D0C0"/>'
  '<stop offset="60%"  stop-color="#B8B0A0"/>'
  '<stop offset="100%" stop-color="#8C8478"/>'
  '</linearGradient>')

# Gold trim (Amaurotine gold-brass)
A('<linearGradient id="eGold" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#FFF8C0"/>'
  '<stop offset="30%"  stop-color="#E8D050"/>'
  '<stop offset="65%"  stop-color="#C0A820"/>'
  '<stop offset="100%" stop-color="#907808"/>'
  '</linearGradient>')

# Lush meadow ground
A('<linearGradient id="eGnd" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#3A8838"/>'
  '<stop offset="35%"  stop-color="#287028"/>'
  '<stop offset="70%"  stop-color="#1A5818"/>'
  '<stop offset="100%" stop-color="#0E4010"/>'
  '</linearGradient>')

# Distant rolling hills (lighter green, atmospheric)
A('<linearGradient id="eHills" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#608060" stop-opacity="0.70"/>'
  '<stop offset="100%" stop-color="#3A6038" stop-opacity="0.90"/>'
  '</linearGradient>')

# Flower petal — crimson
A('<radialGradient id="eFlCrim" cx="40%" cy="30%" r="60%">'
  '<stop offset="0%"   stop-color="#FF9090"/>'
  '<stop offset="45%"  stop-color="#E82838"/>'
  '<stop offset="100%" stop-color="#980818"/>'
  '</radialGradient>')

# Flower petal — violet
A('<radialGradient id="eFlVio" cx="40%" cy="30%" r="60%">'
  '<stop offset="0%"   stop-color="#E0A0FF"/>'
  '<stop offset="45%"  stop-color="#9828D8"/>'
  '<stop offset="100%" stop-color="#501088"/>'
  '</radialGradient>')

# Flower petal — teal
A('<radialGradient id="eFlTeal" cx="40%" cy="30%" r="60%">'
  '<stop offset="0%"   stop-color="#A0F8F0"/>'
  '<stop offset="45%"  stop-color="#18C0A8"/>'
  '<stop offset="100%" stop-color="#0A7868"/>'
  '</radialGradient>')

# Flower petal — gold
A('<radialGradient id="eFlGold" cx="40%" cy="30%" r="60%">'
  '<stop offset="0%"   stop-color="#FFF8A0"/>'
  '<stop offset="45%"  stop-color="#F0C020"/>'
  '<stop offset="100%" stop-color="#A07808"/>'
  '</radialGradient>')

# Flower petal — pink
A('<radialGradient id="eFlPink" cx="40%" cy="30%" r="60%">'
  '<stop offset="0%"   stop-color="#FFC0E8"/>'
  '<stop offset="45%"  stop-color="#F040A0"/>'
  '<stop offset="100%" stop-color="#980860"/>'
  '</radialGradient>')

# Flower petal — orange
A('<radialGradient id="eFlOrng" cx="40%" cy="30%" r="60%">'
  '<stop offset="0%"   stop-color="#FFD080"/>'
  '<stop offset="45%"  stop-color="#F07010"/>'
  '<stop offset="100%" stop-color="#984000"/>'
  '</radialGradient>')

# Aether glow (pink-teal)
A('<radialGradient id="eAether" cx="50%" cy="50%" r="50%">'
  '<stop offset="0%"   stop-color="#E0A8FF" stop-opacity="0.80"/>'
  '<stop offset="38%"  stop-color="#A060D8" stop-opacity="0.38"/>'
  '<stop offset="70%"  stop-color="#6030A8" stop-opacity="0.12"/>'
  '<stop offset="100%" stop-color="#401888" stop-opacity="0"/>'
  '</radialGradient>')

# Creation orb (Stage 5) — swirling teal-gold prototype
A('<radialGradient id="eOrb" cx="38%" cy="32%" r="60%">'
  '<stop offset="0%"   stop-color="#FFFFFF"  stop-opacity="0.95"/>'
  '<stop offset="18%"  stop-color="#C8F8F0"  stop-opacity="0.90"/>'
  '<stop offset="40%"  stop-color="#60D8C0"  stop-opacity="0.80"/>'
  '<stop offset="65%"  stop-color="#20A890"  stop-opacity="0.65"/>'
  '<stop offset="85%"  stop-color="#108060"  stop-opacity="0.45"/>'
  '<stop offset="100%" stop-color="#0A5840"  stop-opacity="0.30"/>'
  '</radialGradient>')

# Aether field inside gate (Stage 10)
A('<radialGradient id="eGateField" cx="50%" cy="50%" r="50%">'
  '<stop offset="0%"   stop-color="#D0A8FF" stop-opacity="0.55"/>'
  '<stop offset="38%"  stop-color="#9060E0" stop-opacity="0.28"/>'
  '<stop offset="70%"  stop-color="#6038C0" stop-opacity="0.10"/>'
  '<stop offset="100%" stop-color="#402090" stop-opacity="0"/>'
  '</radialGradient>')

# Gate column
A('<linearGradient id="eColumn" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#B8B5AF"/>'
  '<stop offset="22%"  stop-color="#EEEAE0"/>'
  '<stop offset="50%"  stop-color="#FEFCF8"/>'
  '<stop offset="78%"  stop-color="#E8E5DC"/>'
  '<stop offset="100%" stop-color="#C8C5BC"/>'
  '</linearGradient>')

# Water/lily pond
A('<linearGradient id="ePond" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#60C8E8"/>'
  '<stop offset="50%"  stop-color="#3898C0"/>'
  '<stop offset="100%" stop-color="#186898"/>'
  '</linearGradient>')

# Top vignette
A('<linearGradient id="eVig" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#180828" stop-opacity="0.82"/>'
  '<stop offset="18%"  stop-color="#180828" stop-opacity="0.05"/>'
  '<stop offset="100%" stop-color="#180828" stop-opacity="0"/>'
  '</linearGradient>')

# Bottom atmospheric haze
A('<linearGradient id="eHaze" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#C080D0" stop-opacity="0"/>'
  '<stop offset="60%"  stop-color="#A060B8" stop-opacity="0.06"/>'
  '<stop offset="100%" stop-color="#804898" stop-opacity="0.22"/>'
  '</linearGradient>')

A('</defs>')

# ─────────────────────────────────────────────────────────────────────────────
#  1. SKY LAYERS
# ─────────────────────────────────────────────────────────────────────────────
A('<rect width="400" height="600" fill="url(#eSky)"/>')
A('<rect width="400" height="600" fill="url(#eLight)"/>')
A('<rect width="400" height="600" fill="url(#eHorizon)"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  2. DISTANT FLOATING ISLANDS (Elpis has floating landmasses in the sky)
# ─────────────────────────────────────────────────────────────────────────────
# Far left island
A('<ellipse cx="54"  cy="90" rx="44" ry="14" fill="#7A6888" opacity="0.55"/>')
A('<ellipse cx="54"  cy="84" rx="38" ry="10" fill="#9888A8" opacity="0.50"/>')
A('<ellipse cx="54"  cy="80" rx="32" ry="7"  fill="#B0A0C0" opacity="0.45"/>')
# Trees on far left island
for tx, th in [(36,18),(46,22),(58,18),(68,16),(76,20)]:
    A(f'<ellipse cx="{tx}" cy="{80-th}" rx="5" ry="{th//2}" fill="#607858" opacity="0.65"/>')
    A(f'<rect x="{tx-1}" y="{80-th//2}" width="2" height="{th//2}" fill="#402010" opacity="0.55"/>')

# Far right island
A('<ellipse cx="342" cy="82" rx="48" ry="14" fill="#7A6888" opacity="0.52"/>')
A('<ellipse cx="342" cy="76" rx="40" ry="10" fill="#9888A8" opacity="0.48"/>')
A('<ellipse cx="342" cy="72" rx="34" ry="7"  fill="#B0A0C0" opacity="0.42"/>')
for tx, th in [(320,16),(332,20),(344,18),(356,22),(368,16)]:
    A(f'<ellipse cx="{tx}" cy="{72-th}" rx="5" ry="{th//2}" fill="#607858" opacity="0.62"/>')
    A(f'<rect x="{tx-1}" y="{72-th//2}" width="2" height="{th//2}" fill="#402010" opacity="0.52"/>')

# Mid-sky tiny island fragment (very distant)
A('<ellipse cx="200" cy="62" rx="22" ry="7"  fill="#A898B8" opacity="0.38"/>')
A('<ellipse cx="200" cy="58" rx="16" ry="4"  fill="#C0B0D0" opacity="0.35"/>')
# Small Amaurotine structure on distant island
A('<rect x="194" y="50" width="12" height="8" fill="#D8D8D0" opacity="0.35" rx="1"/>')
A('<rect x="196" y="47" width="8"  height="3" fill="#E8E0C8" opacity="0.32"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  3. FANTASTICAL CLOUDS (pinkish-white, billowing)
# ─────────────────────────────────────────────────────────────────────────────
clouds = [
    (62,  38, 82, 28, '#FFE8F0', 0.82), (46,  48, 54, 18, '#FFD8E8', 0.72),
    (190, 30, 96, 32, '#FFF0F8', 0.80), (174, 42, 60, 20, '#FFE0F0', 0.70),
    (310, 36, 74, 24, '#FFE8F8', 0.75), (292, 48, 48, 16, '#FFD8E8', 0.65),
]
for cx, cy, cw, ch, col, op in clouds:
    A(f'<ellipse cx="{cx}" cy="{cy}" rx="{cw//2}" ry="{ch//2}" fill="{col}" opacity="{op}"/>')
    A(f'<ellipse cx="{cx-cw//5}" cy="{cy+ch//4}" rx="{cw//3}" ry="{ch//3}" fill="{col}" opacity="{op*0.85:.2f}"/>')
    A(f'<ellipse cx="{cx+cw//5}" cy="{cy+ch//4}" rx="{cw//4}" ry="{ch//3}" fill="{col}" opacity="{op*0.78:.2f}"/>')
    A(f'<ellipse cx="{cx}" cy="{cy+ch//2-2}" rx="{cw//2}" ry="5" fill="#C080A0" opacity="{op*0.22:.2f}"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  4. AETHER MOTES (background, scattered in sky)
# ─────────────────────────────────────────────────────────────────────────────
motes = [
    # Pink motes
    (22,20,1.4,'#FFA0C8',0.82),(58,12,1.0,'#FFB0D8',0.76),(95,24,1.3,'#FF90C0',0.80),
    (138,14,1.0,'#FFB0D8',0.74),(175,26,1.4,'#FFA0C8',0.80),(220,16,1.0,'#FFB0D8',0.72),
    (258,28,1.3,'#FF90C0',0.78),(296,18,1.0,'#FFB0D8',0.74),(336,24,1.4,'#FFA0C8',0.80),
    (378,14,1.0,'#FFB0D8',0.72),(388,30,0.9,'#FF90C0',0.68),
    # Teal motes
    (36,44,1.2,'#80F0D8',0.78),(72,36,0.9,'#60E8C8',0.72),(112,48,1.2,'#80F0D8',0.76),
    (152,38,0.9,'#60E8C8',0.70),(190,50,1.1,'#80F0D8',0.74),(228,40,0.9,'#60E8C8',0.70),
    (265,52,1.2,'#80F0D8',0.74),(305,42,0.9,'#60E8C8',0.68),(344,50,1.1,'#80F0D8',0.72),
    (380,44,0.9,'#60E8C8',0.68),
    # Gold motes
    (16,60,1.0,'#FFE890',0.70),(50,56,0.8,'#FFD870',0.66),(88,64,1.0,'#FFE890',0.68),
    (128,58,0.8,'#FFD870',0.64),(165,66,1.0,'#FFE890',0.68),(205,58,0.8,'#FFD870',0.62),
    (245,66,0.9,'#FFE890',0.66),(283,60,0.8,'#FFD870',0.62),(322,68,1.0,'#FFE890',0.66),
    (362,60,0.8,'#FFD870',0.62),(395,68,0.7,'#FFE890',0.60),
    # Violet motes
    (42,74,0.9,'#D090FF',0.65),(80,70,0.7,'#C080F0',0.60),(118,76,0.9,'#D090FF',0.63),
    (158,72,0.7,'#C080F0',0.58),(198,78,0.9,'#D090FF',0.62),(238,74,0.7,'#C080F0',0.58),
    (278,78,0.8,'#D090FF',0.60),(316,74,0.7,'#C080F0',0.56),(355,80,0.8,'#D090FF',0.60),
]
for mx, my, mr, col, op in motes:
    A(f'<circle cx="{mx}" cy="{my}" r="{mr}" fill="{col}" opacity="{op}"/>')
    if mr > 1.0:
        A(f'<circle cx="{mx}" cy="{my}" r="{mr*2.2:.1f}" fill="{col}" opacity="{op*0.16:.2f}"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  5. DISTANT HILLS (rolling green, seen in ocean gap)
# ─────────────────────────────────────────────────────────────────────────────
A('<ellipse cx="200" cy="320" rx="100" ry="60" fill="url(#eHills)" opacity="0.82"/>')
A('<ellipse cx="158" cy="330" rx="80"  ry="50" fill="#507050" opacity="0.70"/>')
A('<ellipse cx="242" cy="325" rx="85"  ry="52" fill="#587858" opacity="0.68"/>')
A('<ellipse cx="200" cy="338" rx="68"  ry="38" fill="#3A6038" opacity="0.75"/>')
# Distant Amaurotine tower visible on hilltop
A('<rect x="192" y="270" width="16" height="52" fill="#E8E4DC" opacity="0.55" rx="2"/>')
A('<ellipse cx="200" cy="270" rx="10" ry="8"  fill="#F0ECD8" opacity="0.52"/>')
A('<line x1="200" y1="262" x2="200" y2="254" stroke="#D8C848" stroke-width="2" opacity="0.50"/>')
A('<circle cx="200" cy="252" r="4"   fill="#E8C848" opacity="0.55"/>')

# Lily pond / aether stream (visible in gap, foreground of hills)
A('<ellipse cx="200" cy="350" rx="55" ry="18" fill="url(#ePond)" opacity="0.65"/>')
A('<ellipse cx="200" cy="348" rx="50" ry="12" fill="#80D8F0" opacity="0.30"/>')
# Lily pads
for lx, ly, lr in [(178,348,8),(192,354,6),(210,346,7),(222,352,5),(200,360,6)]:
    A(f'<ellipse cx="{lx}" cy="{ly}" rx="{lr}" ry="{lr//2+1}" fill="#2A8028" opacity="0.70"/>')
    A(f'<ellipse cx="{lx}" cy="{ly}" rx="{lr//2}" ry="{lr//3}" fill="#38A030" opacity="0.50"/>')
# Lily flowers on pond
for lx, ly, col in [(180,345,'#FF8090'),(208,344,'#FFFFFF'),(222,350,'#FFD040')]:
    for ang in range(0, 360, 72):
        rad = math.radians(ang)
        px = lx + 4*math.cos(rad); py = ly + 3*math.sin(rad)
        A(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="3" ry="2" fill="{col}" opacity="0.85"/>')
    A(f'<circle cx="{lx}" cy="{ly}" r="2" fill="#FFE870" opacity="0.90"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  6. LEFT CLIFF — AMAUROTINE RESEARCH HALL
# ─────────────────────────────────────────────────────────────────────────────
A('<polygon points="0,0 0,600 138,600 138,312 116,220 90,130 60,56 28,0" fill="url(#eCliffL)"/>')

# Rock strata (subtle)
for sy in [120,168,216,264,312,360,408,456,504]:
    A(f'<line x1="0" y1="{sy}" x2="116" y2="{sy}" stroke="#909888" stroke-width="0.8" opacity="0.28"/>')
# Block joints
for sx in [26,56,88,116]:
    A(f'<line x1="{sx}" y1="100" x2="{sx}" y2="600" stroke="#808878" stroke-width="0.6" opacity="0.22"/>')
# Left edge shadow
A('<polygon points="0,0 0,600 16,600 16,440 10,320 4,200 0,0" fill="#000000" opacity="0.18"/>')

# ── Amaurotine Observation Spire ─────────────────────────────────────────────
# The tall angular spire characteristic of Amaurot/Elpis
A('<polygon points="72,0 76,0 88,130 84,130 78,130 62,130" fill="url(#eMarble)"/>')
A('<polygon points="72,0 68,0 62,130 72,130" fill="#D0CECC" opacity="0.50"/>')
# Spire tip crystal (aether crystal cap)
A('<polygon points="74,0 78,0 82,12 70,12" fill="#C0F0E8" opacity="0.80"/>')
A('<polygon points="74,0 78,0 80,6  72,6"  fill="#E0FFFC" opacity="0.65"/>')
# Gold ring bands on spire
for yb in [28, 52, 76, 100]:
    A(f'<rect x="63" y="{yb}" width="22" height="3" fill="url(#eGold)" rx="1"/>')
    A(f'<rect x="63" y="{yb}" width="22" height="1" fill="#FFFFFF" opacity="0.55"/>')
# Aether conduit lines on spire face
A('<line x1="76" y1="12" x2="76" y2="130" stroke="#80F0D8" stroke-width="1.2" opacity="0.45"/>')
A('<line x1="76" y1="12" x2="76" y2="130" stroke="#C0FFE8" stroke-width="0.5" opacity="0.55"/>')

# ── Main Research Hall (left) ─────────────────────────────────────────────────
A('<rect x="10" y="112" width="72" height="128" fill="url(#eMarble)" rx="2"/>')
A('<rect x="10" y="112" width="72" height="4"   fill="#FFFFFF" opacity="0.60"/>')
# Hall shadow (left side dark)
A('<rect x="10" y="112" width="10" height="128" fill="#000000" opacity="0.10"/>')

# Facade columns (Amaurotine pilasters — flat, rectangular with gold caps)
for cx in [16, 34, 52, 72]:
    A(f'<rect x="{cx}" y="110" width="7" height="132" fill="#F0EEE8" opacity="0.60" rx="1"/>')
    A(f'<rect x="{cx}" y="110" width="7" height="3"   fill="url(#eGold)" rx="1"/>')
    A(f'<rect x="{cx}" y="238" width="7" height="3"   fill="url(#eGold)" rx="1"/>')

# Frieze band (Amaurotine inscription — horizontal decorative band)
A('<rect x="10" y="200" width="72" height="12" fill="#E8E4D8" opacity="0.70"/>')
A('<rect x="10" y="200" width="72" height="2"  fill="#E8D060" opacity="0.55"/>')
A('<rect x="10" y="210" width="72" height="2"  fill="#E8D060" opacity="0.50"/>')
# Inscription marks (stylised Amaurotine runes — horizontal dashes)
for rx in range(14, 80, 7):
    A(f'<rect x="{rx}" y="203" width="4" height="1.5" fill="#C8C0A8" opacity="0.65"/>')
    A(f'<rect x="{rx}" y="206" width="3" height="1.2" fill="#C8C0A8" opacity="0.55"/>')

# Arched windows (wide, Amaurotine segmental arch)
for wx in [18, 44, 62]:
    # Window frame
    A(f'<rect x="{wx}" y="138" width="14" height="24" fill="#1A0828" opacity="0.72" rx="3"/>')
    A(f'<ellipse cx="{wx+7}" cy="138" rx="7" ry="5" fill="#1A0828" opacity="0.72"/>')
    # Window amber glow (interior light)
    A(f'<rect x="{wx+1}" y="138" width="12" height="22" fill="#FFB840" opacity="0.32" rx="2"/>')
    A(f'<ellipse cx="{wx+7}" cy="138" rx="6" ry="4" fill="#FFB840" opacity="0.32"/>')
    # Window highlight
    A(f'<rect x="{wx+2}" y="140" width="4" height="8" fill="#FFF0C0" opacity="0.22" rx="1"/>')

# ── FLOWERING VINE OVERGROWTH on left hall ────────────────────────────────────
# Main vine stems climbing the wall
vine_paths_l = [
    "M10,240 Q18,220 14,196 Q10,172 18,148 Q22,132 20,112",
    "M30,240 Q26,218 32,196 Q36,170 28,148 Q24,130 30,112",
    "M55,240 Q60,215 56,192 Q52,168 58,144 Q62,128 58,112",
    "M75,240 Q72,215 78,190 Q80,165 74,142 Q70,126 76,112",
]
for vp in vine_paths_l:
    A(f'<path d="{vp}" stroke="#2A7020" stroke-width="2.5" fill="none" opacity="0.75"/>')
    A(f'<path d="{vp}" stroke="#3A9028" stroke-width="1.0" fill="none" opacity="0.55"/>')

# Leaf clusters on vines
leaf_pos_l = [(12,224),(16,200),(12,172),(20,148),(20,125),
              (30,220),(34,196),(28,168),(26,145),(32,118),
              (58,218),(54,190),(60,165),(56,140),(60,118),
              (74,218),(78,190),(72,165),(76,140),(74,118)]
for lx, ly in leaf_pos_l:
    for ang in [0, 40, -40]:
        rad = math.radians(ang - 30)
        ex = lx + 9*math.cos(rad); ey = ly + 6*math.sin(rad)
        A(f'<ellipse cx="{(lx+ex)/2:.1f}" cy="{(ly+ey)/2:.1f}" rx="6" ry="3" '
          f'fill="#2A8020" opacity="0.72" transform="rotate({ang-30},{(lx+ex)/2:.1f},{(ly+ey)/2:.1f})"/>')

# Rose flowers on vines (crimson and pink)
rose_pos_l = [(14,215),(12,178),(22,152),(34,202),(28,160),(26,130),
              (60,210),(56,175),(62,148),(76,205),(72,170),(74,128)]
for i, (rx2, ry2) in enumerate(rose_pos_l):
    col = '#E82838' if i % 3 == 0 else ('#F050A0' if i % 3 == 1 else '#FFB0C8')
    for ang in range(0, 360, 72):
        rad = math.radians(ang)
        px = rx2 + 4.5*math.cos(rad); py = ry2 + 4.5*math.sin(rad)
        A(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="3.5" ry="2.5" fill="{col}" opacity="0.88" '
          f'transform="rotate({ang},{px:.1f},{py:.1f})"/>')
    A(f'<circle cx="{rx2}" cy="{ry2}" r="2.5" fill="#FFE870" opacity="0.90"/>')

# ── Left garden terrace / planter ─────────────────────────────────────────────
A('<rect x="0" y="244" width="82" height="72" fill="#7A7868" rx="1"/>')
A('<rect x="0" y="244" width="82" height="3"  fill="#B0AE98" opacity="0.65"/>')
A('<rect x="0" y="312" width="82" height="3"  fill="#706858" opacity="0.50"/>')
# Terrace plant boxes
A('<rect x="4"  y="264" width="28" height="16" fill="#2A6020" opacity="0.80" rx="2"/>')
A('<rect x="38" y="268" width="24" height="14" fill="#2A6020" opacity="0.75" rx="2"/>')
A('<rect x="66" y="265" width="16" height="16" fill="#2A6020" opacity="0.78" rx="2"/>')
# Flowers in terrace boxes
for fx, fy, fc in [(10,260,'#F040A0'),(18,258,'#FF9820'),(26,260,'#E02838'),
                   (44,264,'#9030D0'),(52,262,'#FFD020'),(68,261,'#18C0A8'),
                   (76,259,'#F050A0')]:
    for ang in range(0, 360, 72):
        rad = math.radians(ang)
        px = fx + 4*math.cos(rad); py = fy + 3*math.sin(rad)
        A(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="3" ry="2" fill="{fc}" opacity="0.88"/>')
    A(f'<circle cx="{fx}" cy="{fy}" r="2" fill="#FFE870" opacity="0.85"/>')

# ── Amaurotine lower archive ───────────────────────────────────────────────────
A('<rect x="0" y="320" width="92" height="88" fill="url(#eMarbleSh)" rx="1"/>')
A('<rect x="0" y="320" width="92" height="3"  fill="#E8E0C8" opacity="0.55"/>')
# Windows with warm glow
for wx in [8, 28, 50, 70]:
    A(f'<rect x="{wx}" y="338" width="12" height="18" fill="#FF9820" opacity="0.40" rx="3"/>')
    A(f'<rect x="{wx}" y="350" width="12" height="6"  fill="#FF7010" opacity="0.30" rx="2"/>')
# Gold trim band
A('<rect x="0" y="402" width="92" height="6"  fill="url(#eGold)" rx="1"/>')
A('<rect x="0" y="402" width="92" height="2"  fill="#FFFFFF" opacity="0.40"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  7. RIGHT CLIFF — AMAUROTINE DATA ARCHIVE
# ─────────────────────────────────────────────────────────────────────────────
A('<polygon points="400,0 400,600 262,600 262,312 284,220 310,130 340,56 372,0" fill="url(#eCliffR)"/>')
for sy in [120,168,216,264,312,360,408,456,504]:
    A(f'<line x1="284" y1="{sy}" x2="400" y2="{sy}" stroke="#909888" stroke-width="0.8" opacity="0.28"/>')
for sx in [284,312,342,372]:
    A(f'<line x1="{sx}" y1="100" x2="{sx}" y2="600" stroke="#808878" stroke-width="0.6" opacity="0.22"/>')
A('<polygon points="400,0 400,600 384,600 384,440 390,320 396,200 400,0" fill="#000000" opacity="0.18"/>')

# Right spire
A('<polygon points="322,0 326,0 338,130 324,130 320,130 316,130" fill="url(#eMarble)"/>')
A('<polygon points="326,0 330,0 338,130 326,130" fill="#D0CECC" opacity="0.50"/>')
A('<polygon points="322,0 326,0 330,12 318,12" fill="#C0F0E8" opacity="0.80"/>')
A('<polygon points="322,0 326,0 328,6  320,6"  fill="#E0FFFC" opacity="0.65"/>')
for yb in [28,52,76,100]:
    A(f'<rect x="315" y="{yb}" width="22" height="3" fill="url(#eGold)" rx="1"/>')
    A(f'<rect x="315" y="{yb}" width="22" height="1" fill="#FFFFFF" opacity="0.55"/>')
A('<line x1="324" y1="12" x2="324" y2="130" stroke="#80F0D8" stroke-width="1.2" opacity="0.45"/>')
A('<line x1="324" y1="12" x2="324" y2="130" stroke="#C0FFE8" stroke-width="0.5" opacity="0.55"/>')

# Right main research hall
A('<rect x="318" y="112" width="72" height="128" fill="url(#eMarble)" rx="2"/>')
A('<rect x="318" y="112" width="72" height="4"   fill="#FFFFFF" opacity="0.60"/>')
A('<rect x="380" y="112" width="10" height="128" fill="#000000" opacity="0.10"/>')
for cx in [320,338,358,377]:
    A(f'<rect x="{cx}" y="110" width="7" height="132" fill="#F0EEE8" opacity="0.60" rx="1"/>')
    A(f'<rect x="{cx}" y="110" width="7" height="3"   fill="url(#eGold)" rx="1"/>')
    A(f'<rect x="{cx}" y="238" width="7" height="3"   fill="url(#eGold)" rx="1"/>')
A('<rect x="318" y="200" width="72" height="12" fill="#E8E4D8" opacity="0.70"/>')
A('<rect x="318" y="200" width="72" height="2"  fill="#E8D060" opacity="0.55"/>')
A('<rect x="318" y="210" width="72" height="2"  fill="#E8D060" opacity="0.50"/>')
for rx in range(322, 388, 7):
    A(f'<rect x="{rx}" y="203" width="4" height="1.5" fill="#C8C0A8" opacity="0.65"/>')
    A(f'<rect x="{rx}" y="206" width="3" height="1.2" fill="#C8C0A8" opacity="0.55"/>')
for wx in [326,350,368]:
    A(f'<rect x="{wx}" y="138" width="14" height="24" fill="#1A0828" opacity="0.72" rx="3"/>')
    A(f'<ellipse cx="{wx+7}" cy="138" rx="7" ry="5" fill="#1A0828" opacity="0.72"/>')
    A(f'<rect x="{wx+1}" y="138" width="12" height="22" fill="#FFB840" opacity="0.32" rx="2"/>')
    A(f'<ellipse cx="{wx+7}" cy="138" rx="6" ry="4" fill="#FFB840" opacity="0.32"/>')
    A(f'<rect x="{wx+2}" y="140" width="4" height="8" fill="#FFF0C0" opacity="0.22" rx="1"/>')

# Vine overgrowth on right hall
vine_paths_r = [
    "M390,240 Q382,220 386,196 Q390,172 382,148 Q378,132 380,112",
    "M370,240 Q374,218 368,196 Q364,170 372,148 Q376,130 370,112",
    "M345,240 Q340,215 344,192 Q348,168 342,144 Q338,128 342,112",
    "M325,240 Q328,215 322,190 Q320,165 326,142 Q330,126 324,112",
]
for vp in vine_paths_r:
    A(f'<path d="{vp}" stroke="#2A7020" stroke-width="2.5" fill="none" opacity="0.75"/>')
    A(f'<path d="{vp}" stroke="#3A9028" stroke-width="1.0" fill="none" opacity="0.55"/>')

leaf_pos_r = [(388,224),(384,200),(388,172),(380,148),(380,125),
              (370,220),(366,196),(372,168),(374,145),(368,118),
              (342,218),(346,190),(340,165),(344,140),(340,118),
              (326,218),(322,190),(328,165),(324,140),(326,118)]
for lx, ly in leaf_pos_r:
    for ang in [0, 40, -40]:
        rad = math.radians(ang - 30)
        ex = lx + 9*math.cos(rad); ey = ly + 6*math.sin(rad)
        A(f'<ellipse cx="{(lx+ex)/2:.1f}" cy="{(ly+ey)/2:.1f}" rx="6" ry="3" '
          f'fill="#2A8020" opacity="0.72" transform="rotate({ang-30},{(lx+ex)/2:.1f},{(ly+ey)/2:.1f})"/>')

rose_pos_r = [(386,215),(388,178),(378,152),(366,202),(372,160),(374,130),
              (340,210),(344,175),(342,148),(324,205),(328,170),(326,128)]
for i, (rx2, ry2) in enumerate(rose_pos_r):
    col = '#9030D0' if i % 3 == 0 else ('#18C0A8' if i % 3 == 1 else '#FFB0C8')
    for ang in range(0, 360, 72):
        rad = math.radians(ang)
        px = rx2 + 4.5*math.cos(rad); py = ry2 + 4.5*math.sin(rad)
        A(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="3.5" ry="2.5" fill="{col}" opacity="0.88" '
          f'transform="rotate({ang},{px:.1f},{py:.1f})"/>')
    A(f'<circle cx="{rx2}" cy="{ry2}" r="2.5" fill="#FFE870" opacity="0.90"/>')

# Right garden terrace
A('<rect x="318" y="244" width="82" height="72" fill="#7A7868" rx="1"/>')
A('<rect x="318" y="244" width="82" height="3"  fill="#B0AE98" opacity="0.65"/>')
A('<rect x="318" y="264" width="28" height="16" fill="#2A6020" opacity="0.80" rx="2"/>')
A('<rect x="350" y="268" width="24" height="14" fill="#2A6020" opacity="0.75" rx="2"/>')
A('<rect x="378" y="265" width="16" height="16" fill="#2A6020" opacity="0.78" rx="2"/>')
for fx, fy, fc in [(324,260,'#18C0A8'),(332,258,'#FFD020'),(340,260,'#9030D0'),
                   (356,264,'#F040A0'),(364,262,'#E02838'),(380,261,'#FF9820'),
                   (388,259,'#2878D8')]:
    for ang in range(0, 360, 72):
        rad = math.radians(ang)
        px = fx + 4*math.cos(rad); py = fy + 3*math.sin(rad)
        A(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="3" ry="2" fill="{fc}" opacity="0.88"/>')
    A(f'<circle cx="{fx}" cy="{fy}" r="2" fill="#FFE870" opacity="0.85"/>')

# Right lower archive
A('<rect x="308" y="320" width="92" height="88" fill="url(#eMarbleSh)" rx="1"/>')
A('<rect x="308" y="320" width="92" height="3"  fill="#E8E0C8" opacity="0.55"/>')
for wx in [318,340,360,380]:
    A(f'<rect x="{wx}" y="338" width="12" height="18" fill="#FF9820" opacity="0.40" rx="3"/>')
    A(f'<rect x="{wx}" y="350" width="12" height="6"  fill="#FF7010" opacity="0.30" rx="2"/>')
A('<rect x="308" y="402" width="92" height="6"  fill="url(#eGold)" rx="1"/>')
A('<rect x="308" y="402" width="92" height="2"  fill="#FFFFFF" opacity="0.40"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  8. GROUND — LUSH MEADOW WITH STONE PATH
# ─────────────────────────────────────────────────────────────────────────────
A('<rect x="0" y="344" width="400" height="256" fill="url(#eGnd)"/>')

# Stone path (ancient, mossy)
A('<path d="M200,344 Q198,400 200,450 Q202,500 200,560 Q200,580 200,600" '
  'stroke="#A8A090" stroke-width="36" fill="none" opacity="0.50"/>')
A('<path d="M200,344 Q198,400 200,450 Q202,500 200,560 Q200,580 200,600" '
  'stroke="#C0BAA8" stroke-width="30" fill="none" opacity="0.40"/>')
# Path stones
for py in range(350, 600, 22):
    pw = max(12, 30 - abs(py - 472)//20)
    for dx in [-10, 0, 10]:
        A(f'<rect x="{200+dx-pw//4}" y="{py}" width="{pw//2}" height="10" '
          f'fill="#B8B4A8" opacity="0.55" rx="2"/>')
# Path moss
for py in range(354, 600, 30):
    A(f'<ellipse cx="196" cy="{py}" rx="3" ry="2" fill="#2A7820" opacity="0.50"/>')
    A(f'<ellipse cx="204" cy="{py+8}" rx="2.5" ry="1.8" fill="#2A7820" opacity="0.45"/>')

# Wildflower meadow (both sides of path)
def wildflower(fx, fy, fc, size=4):
    for ang in range(0, 360, 60):
        rad = math.radians(ang)
        px = fx + size*math.cos(rad); py = fy + size*math.sin(rad)
        A(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{size*0.75:.1f}" ry="{size*0.5:.1f}" fill="{fc}" opacity="0.88" '
          f'transform="rotate({ang},{px:.1f},{py:.1f})"/>')
    A(f'<circle cx="{fx}" cy="{fy}" r="{size*0.45:.1f}" fill="#FFE870" opacity="0.92"/>')

# Left meadow flowers
meadow_l = [
    (32,362,'#F040A0',5),(52,374,'#E02838',4),(18,380,'#9030D0',4.5),(70,368,'#FF9820',4),
    (38,392,'#18C0A8',4),(55,400,'#F040A0',3.5),(22,398,'#FFD020',4),(68,390,'#E02838',3.5),
    (40,415,'#9030D0',4),(56,422,'#18C0A8',3.5),(24,420,'#F040A0',4),(72,410,'#FF9820',3.5),
    (35,440,'#E02838',4.5),(58,448,'#9030D0',4),(20,444,'#18C0A8',3.5),(70,436,'#FFD020',4),
    (42,465,'#F040A0',4),(60,472,'#E02838',3.5),(26,470,'#FF9820',4),(74,462,'#9030D0',3.5),
    (38,490,'#18C0A8',4),(54,498,'#F040A0',3.5),(18,494,'#E02838',4),(68,488,'#FFD020',3.5),
    (44,515,'#9030D0',4.5),(62,522,'#18C0A8',4),(28,518,'#F040A0',3.5),(72,510,'#E02838',4),
    (36,540,'#FFD020',4),(55,548,'#9030D0',3.5),(22,544,'#18C0A8',4),(70,536,'#F040A0',3.5),
    (8,360,'#18C0A8',3.5),(10,390,'#E02838',3),(8,420,'#F040A0',3.5),(10,450,'#FFD020',3),
    (8,480,'#9030D0',3.5),(10,510,'#18C0A8',3),
]
for fx, fy, fc, sz in meadow_l:
    wildflower(fx, fy, fc, sz)
    # Stem
    A(f'<line x1="{fx}" y1="{fy}" x2="{fx+1:.0f}" y2="{fy+8}" stroke="#2A7020" stroke-width="1.2" opacity="0.60"/>')

# Right meadow flowers
meadow_r = [
    (368,362,'#E02838',5),(348,374,'#9030D0',4),(382,380,'#F040A0',4.5),(330,368,'#18C0A8',4),
    (362,392,'#FFD020',4),(345,400,'#E02838',3.5),(378,398,'#9030D0',4),(332,390,'#F040A0',3.5),
    (360,415,'#18C0A8',4),(344,422,'#FFD020',3.5),(376,420,'#E02838',4),(328,410,'#9030D0',3.5),
    (365,440,'#F040A0',4.5),(342,448,'#18C0A8',4),(380,444,'#FFD020',3.5),(330,436,'#E02838',4),
    (358,465,'#9030D0',4),(340,472,'#F040A0',3.5),(374,470,'#18C0A8',4),(326,462,'#FFD020',3.5),
    (362,490,'#E02838',4),(346,498,'#9030D0',3.5),(382,494,'#F040A0',4),(332,488,'#18C0A8',3.5),
    (356,515,'#FFD020',4.5),(338,522,'#E02838',4),(372,518,'#9030D0',3.5),(328,510,'#F040A0',4),
    (364,540,'#18C0A8',4),(345,548,'#FFD020',3.5),(378,544,'#E02838',4),(330,536,'#9030D0',3.5),
    (392,360,'#E02838',3.5),(390,390,'#9030D0',3),(392,420,'#F040A0',3.5),(390,450,'#18C0A8',3),
    (392,480,'#FFD020',3.5),(390,510,'#E02838',3),
]
for fx, fy, fc, sz in meadow_r:
    wildflower(fx, fy, fc, sz)
    A(f'<line x1="{fx}" y1="{fy}" x2="{fx-1:.0f}" y2="{fy+8}" stroke="#2A7020" stroke-width="1.2" opacity="0.60"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  9. FANTASTICAL GIANT FLOWERS (signature Elpis element — impossible scale)
# ─────────────────────────────────────────────────────────────────────────────
def giant_flower(cx, base_y, petal_r, center_r, petal_col, center_col, n_petals=6, stem_h=60):
    # Stem
    A(f'<line x1="{cx}" y1="{base_y}" x2="{cx+2}" y2="{base_y-stem_h}" '
      f'stroke="#1A7018" stroke-width="6" stroke-linecap="round"/>')
    A(f'<line x1="{cx}" y1="{base_y}" x2="{cx+2}" y2="{base_y-stem_h}" '
      f'stroke="#2A9828" stroke-width="3" stroke-linecap="round" opacity="0.60"/>')
    # Leaves on stem
    for li, ly_off in enumerate([stem_h*0.4, stem_h*0.7]):
        side = 1 if li % 2 == 0 else -1
        lx = cx + 2 + side * 18; ly = base_y - ly_off
        A(f'<ellipse cx="{(cx+2+lx)/2:.1f}" cy="{ly:.1f}" rx="12" ry="5" '
          f'fill="#228020" opacity="0.78" transform="rotate({side*-30},{(cx+2+lx)/2:.1f},{ly:.1f})"/>')
    # Flower head center y
    hy = base_y - stem_h
    # Petals
    for pi in range(n_petals):
        ang = math.radians(pi * 360 / n_petals)
        px = cx + 2 + (petal_r*0.65)*math.cos(ang)
        py = hy + (petal_r*0.65)*math.sin(ang)
        A(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{petal_r}" ry="{petal_r*0.45:.1f}" '
          f'fill="url(#{petal_col})" opacity="0.90" '
          f'transform="rotate({pi*360//n_petals},{px:.1f},{py:.1f})"/>')
    # Inner petal layer (slightly smaller, offset)
    for pi in range(n_petals):
        ang = math.radians(pi * 360/n_petals + 30)
        px = cx + 2 + (petal_r*0.45)*math.cos(ang)
        py = hy + (petal_r*0.45)*math.sin(ang)
        A(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{petal_r*0.65:.1f}" ry="{petal_r*0.32:.1f}" '
          f'fill="url(#{petal_col})" opacity="0.70" '
          f'transform="rotate({pi*360//n_petals+30},{px:.1f},{py:.1f})"/>')
    # Center disk
    A(f'<circle cx="{cx+2}" cy="{hy}" r="{center_r}" fill="{center_col}" opacity="0.95"/>')
    A(f'<circle cx="{cx+2}" cy="{hy}" r="{center_r*0.6:.1f}" fill="#FFE870" opacity="0.88"/>')
    # Aether glow around flower
    A(f'<circle cx="{cx+2}" cy="{hy}" r="{petal_r*1.6:.1f}" fill="url(#eAether)" opacity="0.20"/>')

# Left giant flowers (flanking the path, against the cliff base)
giant_flower(28,  345, 22, 10, 'eFlCrim', '#FF3050', n_petals=6, stem_h=58)
giant_flower(72,  345, 18, 8,  'eFlVio',  '#C040E8', n_petals=5, stem_h=48)
giant_flower(108, 345, 20, 9,  'eFlTeal', '#20D8B8', n_petals=7, stem_h=55)
giant_flower(14,  380, 16, 7,  'eFlGold', '#F0C020', n_petals=6, stem_h=40)
giant_flower(58,  376, 18, 8,  'eFlPink', '#F050A0', n_petals=5, stem_h=45)
giant_flower(92,  370, 14, 6,  'eFlOrng', '#F07020', n_petals=6, stem_h=38)

# Right giant flowers
giant_flower(372, 345, 22, 10, 'eFlVio',  '#A030D8', n_petals=6, stem_h=58)
giant_flower(328, 345, 18, 8,  'eFlCrim', '#E82840', n_petals=5, stem_h=48)
giant_flower(292, 345, 20, 9,  'eFlGold', '#F0C020', n_petals=7, stem_h=55)
giant_flower(386, 380, 16, 7,  'eFlTeal', '#20C8A8', n_petals=6, stem_h=40)
giant_flower(342, 376, 18, 8,  'eFlOrng', '#F07020', n_petals=5, stem_h=45)
giant_flower(308, 370, 14, 6,  'eFlPink', '#F050A0', n_petals=6, stem_h=38)

# ─────────────────────────────────────────────────────────────────────────────
#  10. STAGE 5 — CREATION ALTAR (translate +52, y≈235)
#  Circular Amaurotine platform with a glowing prototype creature orb
# ─────────────────────────────────────────────────────────────────────────────
A('<g transform="translate(52,0)">')

# Altar ambient aether field
A('<ellipse cx="200" cy="252" rx="72" ry="46" fill="url(#eAether)" opacity="0.38"/>')
A('<ellipse cx="200" cy="252" rx="50" ry="32" fill="#C080F8" opacity="0.12"/>')

# ── Stepped circular platform ─────────────────────────────────────────────────
# 3-tier circular stone platform
A('<ellipse cx="200" cy="294" rx="44" ry="10" fill="#B0ACA0" opacity="0.80"/>')
A('<ellipse cx="200" cy="290" rx="44" ry="10" fill="#C8C4B8"/>')
A('<ellipse cx="200" cy="288" rx="44" ry="4"  fill="#E8E4D8" opacity="0.60"/>')
A('<rect x="156" y="284" width="88" height="8" fill="#C8C4B8" rx="2"/>')
A('<rect x="156" y="284" width="88" height="2" fill="#EEEAE0" opacity="0.55"/>')

A('<ellipse cx="200" cy="282" rx="35" ry="8"  fill="#B8B4A8" opacity="0.80"/>')
A('<ellipse cx="200" cy="278" rx="35" ry="8"  fill="#D0CCC0"/>')
A('<rect x="165" y="274" width="70" height="8" fill="#D0CCC0" rx="2"/>')
A('<rect x="165" y="274" width="70" height="2" fill="#EEEAE0" opacity="0.50"/>')

A('<ellipse cx="200" cy="272" rx="26" ry="6"  fill="#C0BCB0" opacity="0.80"/>')
A('<ellipse cx="200" cy="268" rx="26" ry="6"  fill="#D8D4C8"/>')
A('<rect x="174" y="264" width="52" height="8" fill="#D8D4C8" rx="2"/>')
A('<rect x="174" y="264" width="52" height="2" fill="#EEEAE0" opacity="0.50"/>')

# Inscription runes on platform rim
for ang_i in range(0, 360, 30):
    rad_i = math.radians(ang_i)
    ix = 200 + 38*math.cos(rad_i); iy = 290 + 8*math.sin(rad_i)
    A(f'<rect x="{ix-2:.1f}" y="{iy-1.5:.1f}" width="4" height="1.5" '
      f'fill="url(#eGold)" opacity="0.60" rx="0.5"/>')

# Gold trim rings
A('<ellipse cx="200" cy="290" rx="44" ry="4"  fill="none" stroke="url(#eGold)" stroke-width="2"/>')
A('<ellipse cx="200" cy="278" rx="35" ry="3.5" fill="none" stroke="url(#eGold)" stroke-width="1.5"/>')
A('<ellipse cx="200" cy="268" rx="26" ry="3"  fill="none" stroke="url(#eGold)" stroke-width="1.5"/>')

# Central column rising from platform
A('<rect x="196" y="244" width="8" height="24" fill="url(#eColumn)" rx="3"/>')
A('<rect x="196" y="244" width="8" height="2"  fill="#FFFFFF" opacity="0.60"/>')
A('<rect x="196" y="264" width="8" height="4"  fill="url(#eGold)" rx="1"/>')
# Column aether conduit
A('<rect x="199" y="246" width="2" height="20" fill="#80F0D8" opacity="0.55" rx="1"/>')

# ── CREATION PROTOTYPE ORB ────────────────────────────────────────────────────
# The orb: a glowing sphere containing a new creature being designed
# Outer corona halos
A('<circle cx="200" cy="238" r="32" fill="url(#eAether)" opacity="0.35"/>')
A('<circle cx="200" cy="238" r="24" fill="#A060D0" opacity="0.18"/>')
# Main orb sphere
A('<circle cx="200" cy="238" r="18" fill="url(#eOrb)"/>')
# Orb interior swirl (creature prototype shape)
A('<ellipse cx="198" cy="236" rx="8" ry="5" fill="#C8F8F0" opacity="0.60" transform="rotate(-20,198,236)"/>')
A('<ellipse cx="204" cy="240" rx="5" ry="8" fill="#E0D0FF" opacity="0.50" transform="rotate(15,204,240)"/>')
A('<circle cx="200" cy="238" r="4" fill="#FFFFFF" opacity="0.75"/>')
A('<ellipse cx="196" cy="234" rx="3" ry="2" fill="#FFFFFF" opacity="0.60"/>')
# Orb bright highlight
A('<ellipse cx="195" cy="232" rx="5" ry="3" fill="#FFFFFF" opacity="0.45"/>')
# Orb glass edge
A('<circle cx="200" cy="238" r="18" fill="none" stroke="#D0F0FF" stroke-width="1.5" opacity="0.70"/>')
A('<circle cx="200" cy="238" r="20" fill="none" stroke="#A0D0F8" stroke-width="0.8" opacity="0.50"/>')

# Orbiting aether sparks (multi-colour — Elpis is all colours)
spark_colors = ['#FF80C0','#80F0D8','#FFE070','#D080FF','#FF9040','#60C0FF']
for i, ang in enumerate(range(0, 360, 60)):
    rad = math.radians(ang)
    sx = 200 + 26*math.cos(rad); sy = 238 + 16*math.sin(rad)
    col = spark_colors[i % len(spark_colors)]
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="2.2" fill="{col}" opacity="0.88"/>')
    A(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="4.5" fill="{col}" opacity="0.22"/>')
# Outer orbit ring
A('<ellipse cx="200" cy="238" rx="26" ry="16" fill="none" stroke="#C0A8FF" stroke-width="0.8" opacity="0.40"/>')

# Aether beams radiating upward from orb
for ba in [-30, -15, 0, 15, 30]:
    rad = math.radians(ba - 90)
    bx = 200 + 60*math.cos(rad); by = 238 + 60*math.sin(rad)
    op = max(0.05, 0.38 - abs(ba)*0.01)
    A(f'<line x1="200" y1="220" x2="{bx:.0f}" y2="{by:.0f}" '
      f'stroke="#E0C8FF" stroke-width="1.2" opacity="{op:.2f}"/>')

# Ground echo glow
A('<ellipse cx="200" cy="295" rx="40" ry="7" fill="#9060D0" opacity="0.22"/>')
A('</g>')

# ─────────────────────────────────────────────────────────────────────────────
#  11. STAGE 10 — ELPIS GRAND ENTRANCE GATE (scale 1.5×, center y=531)
#  Two massive Amaurotine columns, wide floral arch, aether barrier
# ─────────────────────────────────────────────────────────────────────────────
A('<g transform="translate(200,531) scale(1.5) translate(-200,-531)">')

# Gate ambient glow
A('<ellipse cx="200" cy="522" rx="92" ry="56" fill="url(#eAether)" opacity="0.22"/>')
A('<ellipse cx="200" cy="522" rx="60" ry="38" fill="#C080F8" opacity="0.10"/>')

# ── LEFT COLUMN ───────────────────────────────────────────────────────────────
# Main column shaft (cylindrical Amaurotine — vertical fluted rectangle)
A('<rect x="146" y="483" width="28" height="74" fill="url(#eColumn)" rx="4"/>')
# Column shadow flutes (vertical lines)
for fx in [150, 156, 162, 168]:
    A(f'<line x1="{fx}" y1="483" x2="{fx}" y2="557" stroke="#C0BCAE" stroke-width="1.2" opacity="0.40"/>')
# Column highlight
A('<rect x="147" y="483" width="6"  height="74" fill="#FFFFFF" opacity="0.20"/>')
# Gold capital (top)
A('<rect x="143" y="483" width="34" height="6"  fill="url(#eGold)" rx="2"/>')
A('<rect x="143" y="483" width="34" height="2"  fill="#FFFFFF" opacity="0.55"/>')
# Gold base
A('<rect x="143" y="554" width="34" height="6"  fill="url(#eGold)" rx="2"/>')
A('<rect x="143" y="557" width="34" height="2"  fill="#C0A020" opacity="0.55"/>')
# Gold band at mid column
A('<rect x="144" y="518" width="32" height="4"  fill="url(#eGold)" rx="1"/>')
# Column inscription panel
A('<rect x="150" y="494" width="18" height="20" fill="#F0EDE4" opacity="0.40" rx="2"/>')
for ri in range(496, 514, 4):
    A(f'<rect x="152" y="{ri}" width="14" height="1.5" fill="#C8C0A0" opacity="0.55"/>')
# Crenellations atop column
for ci in range(5):
    A(f'<rect x="{145+ci*6}" y="477" width="4" height="8" fill="url(#eMarble)" rx="1"/>')
    A(f'<rect x="{145+ci*6}" y="477" width="4" height="1.5" fill="#FFFFFF" opacity="0.50"/>')

# ── RIGHT COLUMN ──────────────────────────────────────────────────────────────
A('<rect x="226" y="483" width="28" height="74" fill="url(#eColumn)" rx="4"/>')
for fx in [230, 236, 242, 248]:
    A(f'<line x1="{fx}" y1="483" x2="{fx}" y2="557" stroke="#C0BCAE" stroke-width="1.2" opacity="0.40"/>')
A('<rect x="247" y="483" width="6"  height="74" fill="#000000" opacity="0.12"/>')
A('<rect x="223" y="483" width="34" height="6"  fill="url(#eGold)" rx="2"/>')
A('<rect x="223" y="483" width="34" height="2"  fill="#FFFFFF" opacity="0.55"/>')
A('<rect x="223" y="554" width="34" height="6"  fill="url(#eGold)" rx="2"/>')
A('<rect x="223" y="557" width="34" height="2"  fill="#C0A020" opacity="0.55"/>')
A('<rect x="224" y="518" width="32" height="4"  fill="url(#eGold)" rx="1"/>')
A('<rect x="232" y="494" width="18" height="20" fill="#F0EDE4" opacity="0.40" rx="2"/>')
for ri in range(496, 514, 4):
    A(f'<rect x="234" y="{ri}" width="14" height="1.5" fill="#C8C0A0" opacity="0.55"/>')
for ci in range(5):
    A(f'<rect x="{225+ci*6}" y="477" width="4" height="8" fill="url(#eMarble)" rx="1"/>')
    A(f'<rect x="{225+ci*6}" y="477" width="4" height="1.5" fill="#FFFFFF" opacity="0.50"/>')

# ── ARCH (wide, Amaurotine segmental — broad and flowing) ────────────────────
# Arch body (thick, ivory marble)
A('<path d="M146,532 Q146,486 200,476 Q254,486 254,532" '
  'fill="none" stroke="#DEDAD2" stroke-width="18"/>')
# Arch inner edge (lighter)
A('<path d="M150,532 Q150,492 200,483 Q250,492 250,532" '
  'fill="none" stroke="#F8F5EE" stroke-width="4" opacity="0.55"/>')
# Gold trim along arch
A('<path d="M153,531 Q153,495 200,487 Q247,495 247,531" '
  'fill="none" stroke="#E8D050" stroke-width="2.5" opacity="0.72"/>')
A('<path d="M153,531 Q153,495 200,487 Q247,495 247,531" '
  'fill="none" stroke="#FFF8A0" stroke-width="0.8" opacity="0.65"/>')

# Voussoir (arch stone joints)
for angle_deg in [206, 220, 234, 248, 264, 278, 292, 306, 320]:
    ang = math.radians(angle_deg)
    x_o = 200 + 54*math.cos(ang); y_o = 532 + 46*math.sin(ang)
    x_i = 200 + 36*math.cos(ang); y_i = 532 + 31*math.sin(ang)
    A(f'<line x1="{x_i:.1f}" y1="{y_i:.1f}" x2="{x_o:.1f}" y2="{y_o:.1f}" '
      f'stroke="#C8C4B8" stroke-width="1.0" opacity="0.55"/>')

# Keystone — Amaurotine sunflower motif (the ancients revered creation)
A('<circle cx="200" cy="476" r="11" fill="#EEEAE0" stroke="url(#eGold)" stroke-width="2.5"/>')
for ang_k in range(0, 360, 40):
    rk = math.radians(ang_k)
    A(f'<line x1="{200+4*math.cos(rk):.1f}" y1="{476+4*math.sin(rk):.1f}" '
      f'x2="{200+9*math.cos(rk):.1f}" y2="{476+9*math.sin(rk):.1f}" '
      f'stroke="#E8C840" stroke-width="1.4" opacity="0.90"/>')
A('<circle cx="200" cy="476" r="4" fill="#F0C830" opacity="0.92"/>')
A('<circle cx="200" cy="476" r="2" fill="#FFFFFF"  opacity="0.80"/>')

# ── FLOWERING VINES ON ARCH ───────────────────────────────────────────────────
# Climbing roses/flowers on the arch
arch_flower_data = []
for i in range(14):
    t = (i+0.5) / 14
    ang = math.radians(206 + (320-206)*t)
    fx = 200 + 54*math.cos(ang); fy = 532 + 46*math.sin(ang)
    col_idx = i % 5
    cols = ['#E82838','#F040A0','#9030D0','#18C0A8','#FF9820']
    arch_flower_data.append((fx, fy, cols[col_idx]))

for fx, fy, fc in arch_flower_data:
    for ang in range(0, 360, 72):
        rad = math.radians(ang)
        px = fx + 3.5*math.cos(rad); py = fy + 3.5*math.sin(rad)
        A(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="3" ry="2" fill="{fc}" opacity="0.85" '
          f'transform="rotate({ang},{px:.1f},{py:.1f})"/>')
    A(f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="2" fill="#FFE870" opacity="0.88"/>')
    # Leaf
    lx = fx + 7; ly = fy + 4
    A(f'<ellipse cx="{lx:.1f}" cy="{ly:.1f}" rx="5" ry="2.5" fill="#2A7820" opacity="0.70" '
      f'transform="rotate(-25,{lx:.1f},{ly:.1f})"/>')

# ── AETHER BARRIER INSIDE ARCH ────────────────────────────────────────────────
# Soft glowing field (portal-like shimmer)
A('<path d="M150,532 Q150,492 200,483 Q250,492 250,532 L150,532" '
  'fill="url(#eGateField)" opacity="0.50"/>')
# Vertical shimmer columns
for bx in [158, 167, 176, 185, 200, 215, 224, 233, 242]:
    h = 46 if bx == 200 else (42 if abs(bx-200) < 18 else 36)
    top_y = 558 - h
    A(f'<rect x="{bx-1}" y="{top_y}" width="2" height="{h}" fill="#D0B0FF" opacity="0.30" rx="1"/>')
    A(f'<rect x="{bx-0.5}" y="{top_y}" width="1" height="{h}" fill="#F0E0FF" opacity="0.40" rx="1"/>')
# Central shimmer line
A('<rect x="152" y="520" width="96" height="1.5" fill="#E0C8FF" opacity="0.60" rx="1"/>')

# ── FLANKING FLOWER BUSHES ────────────────────────────────────────────────────
# Left bush
for bx, by, bc in [(132,536,'#E02838'),(126,542,'#F040A0'),(134,548,'#9030D0'),
                   (122,538,'#18C0A8'),(130,554,'#FFD020'),(136,544,'#FF9820')]:
    for ang in range(0, 360, 60):
        rad = math.radians(ang)
        px = bx + 5*math.cos(rad); py = by + 4*math.sin(rad)
        A(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="4" ry="3" fill="{bc}" opacity="0.85"/>')
    A(f'<circle cx="{bx}" cy="{by}" r="2.5" fill="#FFE870" opacity="0.88"/>')
# Left bush leaves
A('<ellipse cx="128" cy="546" rx="16" ry="10" fill="#1A6018" opacity="0.72"/>')
A('<ellipse cx="136" cy="552" rx="12" ry="8"  fill="#226820" opacity="0.68"/>')

# Right bush
for bx, by, bc in [(268,536,'#9030D0'),(274,542,'#18C0A8'),(266,548,'#E02838'),
                   (278,538,'#FFD020'),(270,554,'#F040A0'),(264,544,'#FF9820')]:
    for ang in range(0, 360, 60):
        rad = math.radians(ang)
        px = bx + 5*math.cos(rad); py = by + 4*math.sin(rad)
        A(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="4" ry="3" fill="{bc}" opacity="0.85"/>')
    A(f'<circle cx="{bx}" cy="{by}" r="2.5" fill="#FFE870" opacity="0.88"/>')
A('<ellipse cx="272" cy="546" rx="16" ry="10" fill="#1A6018" opacity="0.72"/>')
A('<ellipse cx="264" cy="552" rx="12" ry="8"  fill="#226820" opacity="0.68"/>')

# Gate threshold stone
A('<rect x="143" y="558" width="114" height="6" fill="#C8C4B8" rx="2"/>')
A('<rect x="143" y="558" width="114" height="2" fill="#E8E4D8" opacity="0.55"/>')
# Gold trim on threshold
A('<rect x="143" y="562" width="114" height="2" fill="url(#eGold)" rx="1"/>')

# Ground aether echo
A('<ellipse cx="200" cy="564" rx="60" ry="10" fill="#A060D0" opacity="0.22"/>')
A('<ellipse cx="200" cy="564" rx="38" ry="5"  fill="#C090F8" opacity="0.28"/>')

A('</g>')

# ─────────────────────────────────────────────────────────────────────────────
#  12. FOREGROUND DEPTH ELEMENTS
# ─────────────────────────────────────────────────────────────────────────────
# Very close foreground flowers (giant, partially cropped)
giant_flower(4,   580, 28, 12, 'eFlCrim', '#FF3050', n_petals=6, stem_h=70)
giant_flower(396, 580, 26, 11, 'eFlVio',  '#B040E0', n_petals=5, stem_h=65)
giant_flower(18,  574, 22, 9,  'eFlTeal', '#20D0B8', n_petals=7, stem_h=55)
giant_flower(382, 574, 20, 8,  'eFlGold', '#F0C020', n_petals=6, stem_h=52)

# Foreground tall grass tufts
for gx in range(0, 401, 18):
    for blade in range(3):
        bx = gx + blade*6 - 6
        by = 600
        A(f'<path d="M{bx},{by} Q{bx+3},{by-28} {bx+1},{by-42}" '
          f'stroke="#2A7820" stroke-width="2.2" fill="none" stroke-linecap="round" opacity="0.62"/>')
        A(f'<path d="M{bx},{by} Q{bx+3},{by-28} {bx+1},{by-42}" '
          f'stroke="#3A9828" stroke-width="0.8" fill="none" stroke-linecap="round" opacity="0.45"/>')

# ─────────────────────────────────────────────────────────────────────────────
#  13. ATMOSPHERE OVERLAYS
# ─────────────────────────────────────────────────────────────────────────────
# Bottom atmospheric haze
A('<rect y="488" width="400" height="112" fill="url(#eHaze)" opacity="0.85"/>')
# Soft aether wisps mid-air
wisps = [(48,320,2.2,1.4,'#FFA0C8',0.75),(92,306,1.8,1.2,'#80F0D8',0.72),
         (144,298,2.0,1.3,'#FFE070',0.70),(168,318,1.6,1.1,'#D080FF',0.68),
         (232,310,2.0,1.3,'#80F0D8',0.70),(256,302,1.8,1.2,'#FFA0C8',0.68),
         (310,318,2.2,1.4,'#FFE070',0.72),(352,306,1.8,1.2,'#D080FF',0.70),
         (40,448,1.8,1.2,'#FFA0C8',0.65),(110,462,2.0,1.3,'#80F0D8',0.68),
         (200,440,2.5,1.6,'#D080FF',0.72),(290,455,2.0,1.3,'#FFE070',0.66),(360,448,1.8,1.2,'#FFA0C8',0.62)]
for wx,wy,wr,wh,wc,op in wisps:
    A(f'<ellipse cx="{wx}" cy="{wy}" rx="{wr}" ry="{wh}" fill="{wc}" opacity="{op}"/>')
    A(f'<ellipse cx="{wx}" cy="{wy}" rx="{wr*2.8:.1f}" ry="{wh*2.8:.1f}" fill="{wc}" opacity="{op*0.16:.2f}"/>')

# Top vignette
A('<rect width="400" height="600" fill="url(#eVig)"/>')

# Ethereal light shafts (very faint, from upper-left)
for ang in [-35, -22, -12, -4, 4, 12]:
    rad = math.radians(ang - 90)
    lx = 168 + 350*math.cos(rad); ly = 40 + 350*math.sin(rad)
    op = max(0.005, 0.048 - abs(ang)*0.002)
    sw = max(0.5, 2.0 - abs(ang)*0.06)
    A(f'<line x1="168" y1="40" x2="{lx:.0f}" y2="{ly:.0f}" '
      f'stroke="#FFD8A0" stroke-width="{sw:.1f}" opacity="{op:.3f}"/>')

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

# Check for backticks or single quotes (both would break injection)
if svg.count('`'): raise RuntimeError('Backtick in SVG!')
if svg.count("'"): raise RuntimeError('Single quote in SVG!')

# XML validation
import xml.etree.ElementTree as ET
try:
    ET.fromstring(svg)
    print('  XML parse: OK')
except ET.ParseError as e:
    raise RuntimeError(f'XML parse error: {e}')

# ULTIMATE uses backtick template literal — different injection pattern
# Also fix CSS fallback color for ULTIMATE
html2 = html
for old, new in [
    ('.map-scroll[data-diff="ULTIMATE"] { background: #4B5041; }',
     '.map-scroll[data-diff="ULTIMATE"] { background: #601868; }'),
    ('#game-view[data-diff="ULTIMATE"] { background: rgb(210,228,255); }',
     '#game-view[data-diff="ULTIMATE"] { background: rgb(96,24,104); }'),
]:
    if old in html2:
        html2 = html2.replace(old, new)
        print(f'  Replaced CSS: {old[:50]}...')

# ULTIMATE uses backtick: if(diff==='ULTIMATE') return `...`;
pattern = r"(if\(diff===.ULTIMATE.\) return \`)(.*?)(\`;)"
repl = lambda m: m.group(1) + svg + m.group(3)
new_html, n = _re.subn(pattern, repl, html2, flags=_re.DOTALL)
if n == 0:
    raise RuntimeError("ULTIMATE pattern not found in stage.html")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print(f'stage.html written. ({n} replacement)')
