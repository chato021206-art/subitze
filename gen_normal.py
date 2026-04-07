#!/usr/bin/env python3
"""gen_normal.py — Limsa Lominsa masterpiece (FF14 quality)."""
import re

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

P = []
A = P.append

A('<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">')

# ── DEFS ────────────────────────────────────────────────────────────────
A('<defs>')
# Sky — deep La Noscea cerulean
A('<linearGradient id="nSky" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#001878"/>'
  '<stop offset="16%"  stop-color="#0A3CB4"/>'
  '<stop offset="36%"  stop-color="#2870DC"/>'
  '<stop offset="60%"  stop-color="#5498EC"/>'
  '<stop offset="80%"  stop-color="#80C0F4"/>'
  '<stop offset="100%" stop-color="#B0DCF8"/>'
  '</linearGradient>')
# Deep ocean
A('<linearGradient id="nSea" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#052048"/>'
  '<stop offset="28%"  stop-color="#0A3878"/>'
  '<stop offset="60%"  stop-color="#1460A8"/>'
  '<stop offset="100%" stop-color="#2274C4"/>'
  '</linearGradient>')
# Sun glare — upper right warm glow
A('<radialGradient id="nSun" cx="82%" cy="12%" r="52%">'
  '<stop offset="0%"   stop-color="#FFFCE8" stop-opacity="0.92"/>'
  '<stop offset="22%"  stop-color="#FFE878" stop-opacity="0.52"/>'
  '<stop offset="52%"  stop-color="#FFCC40" stop-opacity="0.20"/>'
  '<stop offset="100%" stop-color="#FFCC40" stop-opacity="0"/>'
  '</radialGradient>')
# Ocean shimmer (sun path on water)
A('<radialGradient id="nShimmer" cx="72%" cy="8%" r="68%">'
  '<stop offset="0%"   stop-color="#B0E0FF" stop-opacity="0.60"/>'
  '<stop offset="40%"  stop-color="#88CCF8" stop-opacity="0.30"/>'
  '<stop offset="100%" stop-color="#88CCF8" stop-opacity="0"/>'
  '</radialGradient>')
# Horizon atmospheric haze
A('<linearGradient id="nHaze" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#C0E4FF" stop-opacity="0"/>'
  '<stop offset="100%" stop-color="#C8E8FF" stop-opacity="0.70"/>'
  '</linearGradient>')
# Limestone cliff — warm tan/ochre
A('<linearGradient id="nCliff" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#ECD48C"/>'
  '<stop offset="25%"  stop-color="#D4B86C"/>'
  '<stop offset="55%"  stop-color="#B09448"/>'
  '<stop offset="80%"  stop-color="#8A7028"/>'
  '<stop offset="100%" stop-color="#6A5018"/>'
  '</linearGradient>')
# Left cliff shadow
A('<linearGradient id="nCliffSh" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#1E1002" stop-opacity="0.58"/>'
  '<stop offset="45%"  stop-color="#1E1002" stop-opacity="0.20"/>'
  '<stop offset="100%" stop-color="#1E1002" stop-opacity="0"/>'
  '</linearGradient>')
# Right cliff shadow
A('<linearGradient id="nCliffShr" x1="1" y1="0" x2="0" y2="0">'
  '<stop offset="0%"   stop-color="#1E1002" stop-opacity="0.52"/>'
  '<stop offset="45%"  stop-color="#1E1002" stop-opacity="0.18"/>'
  '<stop offset="100%" stop-color="#1E1002" stop-opacity="0"/>'
  '</linearGradient>')
# Stone building (lit face)
A('<linearGradient id="nBldg" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#F4DC9C"/>'
  '<stop offset="40%"  stop-color="#DCC078"/>'
  '<stop offset="100%" stop-color="#B8A050"/>'
  '</linearGradient>')
# Gate gradient
A('<linearGradient id="nGate" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#DCC078"/>'
  '<stop offset="48%"  stop-color="#C0A050"/>'
  '<stop offset="100%" stop-color="#8A7028"/>'
  '</linearGradient>')
# Gate left pillar (sunlit side)
A('<linearGradient id="nGateL" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0%"   stop-color="#F4D080"/>'
  '<stop offset="38%"  stop-color="#D8B05C"/>'
  '<stop offset="100%" stop-color="#A07C34"/>'
  '</linearGradient>')
# Foreground tower/wall
A('<linearGradient id="nWall" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#EED090"/>'
  '<stop offset="38%"  stop-color="#D4B468"/>'
  '<stop offset="100%" stop-color="#9E7C3C"/>'
  '</linearGradient>')
# Plaza stone ground
A('<linearGradient id="nGnd" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#CEB068"/>'
  '<stop offset="35%"  stop-color="#AC8840"/>'
  '<stop offset="100%" stop-color="#7C5C1E"/>'
  '</linearGradient>')
# Dock stone
A('<linearGradient id="nDock" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%"   stop-color="#CCAC6C"/>'
  '<stop offset="100%" stop-color="#A48844"/>'
  '</linearGradient>')
# Sail
A('<linearGradient id="nSail" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0%"   stop-color="#F8F0DC"/>'
  '<stop offset="100%" stop-color="#DACCA8"/>'
  '</linearGradient>')
A('</defs>')

# ═══ SKY ════════════════════════════════════════════════════════════════
A('<rect width="400" height="600" fill="url(#nSky)"/>')
A('<rect width="400" height="600" fill="url(#nSun)"/>')
# Horizon haze band
A('<rect y="100" width="400" height="28" fill="url(#nHaze)"/>')

# ═══ CLOUDS ═════════════════════════════════════════════════════════════
# Large left cloud bank (volumetric cumulus with shadow belly)
A('<ellipse cx="58"  cy="27"  rx="62" ry="29" fill="white" opacity="0.96"/>')
A('<ellipse cx="36"  cy="40"  rx="38" ry="22" fill="white" opacity="0.92"/>')
A('<ellipse cx="84"  cy="43"  rx="44" ry="21" fill="white" opacity="0.90"/>')
A('<ellipse cx="58"  cy="52"  rx="58" ry="16" fill="#F2F0EC" opacity="0.84"/>')
A('<ellipse cx="26"  cy="54"  rx="22" ry="9"  fill="#E8E6E0" opacity="0.58"/>')
A('<ellipse cx="92"  cy="56"  rx="20" ry="7"  fill="#EDEDEA" opacity="0.54"/>')
# Shadow underbelly (grey-blue)
A('<ellipse cx="58"  cy="54"  rx="52" ry="11" fill="#B8C8D8" opacity="0.30"/>')

# Medium right cloud
A('<ellipse cx="322" cy="20"  rx="56" ry="24" fill="white" opacity="0.92"/>')
A('<ellipse cx="300" cy="31"  rx="34" ry="18" fill="white" opacity="0.88"/>')
A('<ellipse cx="346" cy="33"  rx="36" ry="16" fill="white" opacity="0.86"/>')
A('<ellipse cx="322" cy="39"  rx="50" ry="13" fill="#F0EEE8" opacity="0.78"/>')
A('<ellipse cx="322" cy="41"  rx="44" ry="8"  fill="#C8D4E0" opacity="0.26"/>')

# Distant scattered cloud wisps
A('<ellipse cx="174" cy="14"  rx="32" ry="10" fill="white" opacity="0.68"/>')
A('<ellipse cx="220" cy="8"   rx="24" ry="7"  fill="white" opacity="0.58"/>')
A('<ellipse cx="260" cy="18"  rx="20" ry="6"  fill="white" opacity="0.50"/>')
A('<ellipse cx="142" cy="28"  rx="16" ry="5"  fill="white" opacity="0.40"/>')
A('<ellipse cx="292" cy="44"  rx="14" ry="4"  fill="white" opacity="0.36"/>')

# ═══ SEAGULLS ═══════════════════════════════════════════════════════════
A('<path d="M68,72 Q75,65 82,72"   stroke="#607888" stroke-width="1.9" fill="none"/>')
A('<path d="M84,60 Q92,52 100,60"  stroke="#607888" stroke-width="1.9" fill="none"/>')
A('<path d="M240,56 Q248,49 256,56" stroke="#7090A0" stroke-width="1.7" fill="none"/>')
A('<path d="M262,68 Q269,62 276,68" stroke="#8098A8" stroke-width="1.6" fill="none"/>')
A('<path d="M158,82 Q165,75 172,82" stroke="#8098A8" stroke-width="1.5" fill="none"/>')
A('<path d="M358,44 Q365,38 372,44" stroke="#607888" stroke-width="1.5" fill="none"/>')
A('<path d="M338,64 Q344,58 350,64" stroke="#7090A0" stroke-width="1.4" fill="none"/>')
A('<path d="M122,96 Q128,90 134,96" stroke="#8098A8" stroke-width="1.3" fill="none"/>')

# ═══ OCEAN ══════════════════════════════════════════════════════════════
A('<rect y="112" width="400" height="172" fill="url(#nSea)"/>')
A('<rect y="112" width="400" height="172" fill="url(#nShimmer)"/>')
# Horizon bright line
A('<rect y="110" width="400" height="6" fill="#C8E8FF" opacity="0.55"/>')
# Waves (subtle horizontal paths)
for oy, sw, op in [(138,1.3,0.42),(162,1.2,0.36),(188,1.1,0.31),(216,1.0,0.27),(244,0.9,0.23)]:
    A(f'<path d="M0,{oy} Q50,{oy-5} 100,{oy} Q150,{oy+5} 200,{oy} Q250,{oy-5} 300,{oy} Q350,{oy+5} 400,{oy}" '
      f'stroke="#3898C8" stroke-width="{sw}" fill="none" opacity="{op}"/>')
# Sun shimmer streak on water
A('<path d="M310,115 L345,165 L370,285" stroke="#C0E8FF" stroke-width="24" fill="none" opacity="0.16" stroke-linecap="round"/>')
# Water sparkles
for cx, cy, r, op in [(96,148,2.2,0.65),(204,136,2.5,0.60),(310,158,2.0,0.57),
                       (56,182,1.7,0.52),(354,172,2.1,0.54),(148,206,1.9,0.48),
                       (328,196,1.7,0.46),(224,228,2.2,0.44),(78,248,1.5,0.40)]:
    A(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#C0E8FF" opacity="{op}"/>')

# ═══ DISTANT GALLEONS ═══════════════════════════════════════════════════
# Left galleon (small, far)
A('<rect x="18"  y="136" width="50" height="9"  fill="#3A2210" rx="2" opacity="0.72"/>')
A('<rect x="34"  y="110" width="4"  height="28" fill="#2C1808" opacity="0.70"/>')
A('<polygon points="34,112 50,134 34,134" fill="url(#nSail)" opacity="0.74"/>')
A('<polygon points="38,116 58,134 38,134" fill="#EEE8D4" opacity="0.66"/>')
A('<rect x="54"  y="120" width="3"  height="16" fill="#2C1808" opacity="0.66"/>')
A('<polygon points="54,122 65,134 54,134" fill="#EAE4D0" opacity="0.62"/>')
A('<rect x="34"  y="107" width="8"  height="5"  fill="#B01818" opacity="0.72"/>')
# Right galleon
A('<rect x="326" y="144" width="56" height="9"  fill="#3A2210" rx="2" opacity="0.66"/>')
A('<rect x="344" y="118" width="4"  height="28" fill="#2C1808" opacity="0.63"/>')
A('<polygon points="344,120 360,142 344,142" fill="url(#nSail)" opacity="0.68"/>')
A('<polygon points="348,124 366,142 348,142" fill="#E4DEC8" opacity="0.60"/>')
A('<rect x="362" y="126" width="3"  height="18" fill="#2C1808" opacity="0.62"/>')
A('<polygon points="362,128 373,142 362,142" fill="#EAE4D0" opacity="0.57"/>')
A('<rect x="344" y="115" width="7"  height="4"  fill="#B01818" opacity="0.67"/>')

# ═══ LEFT CLIFF ═════════════════════════════════════════════════════════
A('<polygon points="0,112 0,600 148,600 148,268 108,200 52,130 0,112" fill="url(#nCliff)"/>')
# Left shadow strip
A('<polygon points="0,112 0,600 22,600 22,234 0,122" fill="#1C0E02" opacity="0.44"/>')
# Depth layer
A('<polygon points="0,112 52,130 108,200 148,268 148,600 132,600 132,276 100,212 50,142 0,126" fill="#5A3A14" opacity="0.26"/>')
# Rock strata — horizontal texture lines across cliff face
for y, op in [(136,0.38),(154,0.33),(174,0.30),(198,0.27),(224,0.24),(250,0.22),(272,0.20)]:
    x1 = max(0, (y - 112) // 4)
    x2 = min(148, (y - 112) // 2 + 10)
    A(f'<path d="M{x1},{y} Q{(x1+x2)//2},{y-4} {x2},{y}" stroke="#7A5020" stroke-width="1.8" fill="none" opacity="{op}"/>')
for y, op in [(146,0.22),(166,0.20),(186,0.18),(210,0.17),(236,0.16),(260,0.15)]:
    x1 = max(0, (y - 112) // 5)
    x2 = min(148, (y - 112) // 3 + 6)
    A(f'<path d="M{x1},{y} Q{(x1+x2)//2},{y-2} {x2},{y}" stroke="#6A4210" stroke-width="0.9" fill="none" opacity="{op}"/>')
# Vertical crevices
A('<path d="M28,132 Q32,157 30,182 Q28,212 34,244" stroke="#3A1E04" stroke-width="1.5" fill="none" opacity="0.35"/>')
A('<path d="M88,166 Q92,190 90,216" stroke="#3A1E04" stroke-width="1.2" fill="none" opacity="0.28"/>')
# Cliff-top scrub vegetation
A('<ellipse cx="20"  cy="238" rx="18" ry="7"  fill="#385E18" opacity="0.62"/>')
A('<ellipse cx="54"  cy="252" rx="24" ry="8"  fill="#406620" opacity="0.58"/>')
A('<ellipse cx="92"  cy="265" rx="18" ry="6"  fill="#385E18" opacity="0.54"/>')
A('<ellipse cx="122" cy="278" rx="14" ry="5"  fill="#406620" opacity="0.50"/>')
A('<ellipse cx="144" cy="288" rx="10" ry="4"  fill="#385E18" opacity="0.44"/>')

# ═══ LEFT CLIFF CITY ════════════════════════════════════════════════════
# ── Lighthouse / Maelstrom Watchtower (tallest, far-left) ──────────────
A('<rect x="8"  y="118" width="26" height="6"  fill="#B09040" rx="1" opacity="0.90"/>')  # base
A('<polygon points="9,68 10,118 33,118 34,68" fill="url(#nBldg)"/>')                     # shaft (slightly tapered)
A('<rect x="6"  y="58"  width="30" height="12" fill="#C8A860" rx="2"/>')                 # lamp room
A('<rect x="4"  y="54"  width="34" height="6"  fill="#B09040" rx="2"/>')                 # cap
# Lamp room windows
A('<rect x="9"  y="60"  width="7"  height="9"  fill="#B8D0FF" rx="2" opacity="0.84"/>')
A('<rect x="26" y="60"  width="7"  height="9"  fill="#B8D0FF" rx="2" opacity="0.82"/>')
# Light glow
A('<ellipse cx="21" cy="65" rx="11" ry="9"  fill="#FFE880" opacity="0.40"/>')
A('<ellipse cx="21" cy="65" rx="5"  ry="4"  fill="#FFFCC0" opacity="0.68"/>')
# Top battlements
for bx in [4, 10, 16, 22, 28]:
    A(f'<rect x="{bx}" y="48" width="5" height="8" fill="#B09040" rx="1"/>')
# Tower windows (arched)
A('<rect x="13" y="76"  width="8"  height="11" fill="#1840A0" rx="3" opacity="0.76"/>')
A('<rect x="13" y="92"  width="8"  height="10" fill="#1840A0" rx="3" opacity="0.68"/>')
A('<rect x="13" y="107" width="8"  height="9"  fill="#1840A0" rx="3" opacity="0.58"/>')
# Stone courses
for y in [82, 92, 102, 112, 118]:
    A(f'<line x1="9" y1="{y}" x2="34" y2="{y}" stroke="#9A7828" stroke-width="0.9" opacity="0.34"/>')
# Maelstrom banner
A('<rect x="34" y="56" width="15" height="24" fill="#A01818" rx="1" opacity="0.92"/>')
A('<polygon points="34,80 49,80 49,85 41,90 34,85" fill="#880808" opacity="0.76"/>')
A('<line x1="34" y1="68" x2="49" y2="68" stroke="#CC3828" stroke-width="1.3" opacity="0.68"/>')

# ── Round tower ────────────────────────────────────────────────────────
A('<rect x="50" y="78"  width="26" height="46" fill="url(#nBldg)" rx="13"/>')
A('<ellipse cx="63" cy="78"  rx="13" ry="5"  fill="#D0B870"/>')
A('<ellipse cx="63" cy="124" rx="13" ry="4"  fill="#C0A860" opacity="0.68"/>')
# Conical roof
A('<polygon points="50,80 76,80 63,60" fill="#7A6028"/>')
A('<polygon points="52,80 74,80 63,63" fill="#8A7030" opacity="0.58"/>')
for bx in [50, 56, 62, 68, 74]:
    A(f'<rect x="{bx}" y="76" width="5" height="6" fill="#C0A050" rx="1"/>')
A('<rect x="59" y="88"  width="8" height="11" fill="#1840A0" rx="3" opacity="0.74"/>')
A('<rect x="59" y="105" width="8" height="9"  fill="#1848B0" rx="3" opacity="0.64"/>')
for y in [88, 98, 108, 118]:
    A(f'<line x1="52" y1="{y}" x2="74" y2="{y}" stroke="#9A7828" stroke-width="0.8" opacity="0.28"/>')

# ── Main city hall (large rectangular building) ─────────────────────────
A('<rect x="76" y="80"  width="42" height="52" fill="url(#nBldg)" rx="1"/>')
A('<rect x="74" y="78"  width="46" height="6"  fill="#BEA050" rx="1"/>')
# Arched windows, two rows
for bx in [80, 92, 104]:
    A(f'<rect x="{bx}" y="86" width="8" height="13" fill="#1840A0" rx="4" opacity="0.74"/>')
for bx in [80, 92, 104]:
    A(f'<rect x="{bx}" y="105" width="8" height="10" fill="#1848B0" rx="3" opacity="0.64"/>')
for bx in [80, 92, 104]:
    A(f'<rect x="{bx}" y="121" width="8" height="9" fill="#1848B0" rx="3" opacity="0.54"/>')
# Battlements
for bx in [74, 80, 86, 92, 98, 104, 110, 116]:
    A(f'<rect x="{bx}" y="72" width="5" height="8" fill="#BEA050" rx="1"/>')
# Stone courses
for y in [90, 100, 110, 120]:
    A(f'<line x1="76" y1="{y}" x2="118" y2="{y}" stroke="#9A7828" stroke-width="0.8" opacity="0.26"/>')

# ── Small corner tower ─────────────────────────────────────────────────
A('<rect x="118" y="90"  width="20" height="38" fill="#DCBE78" rx="1"/>')
A('<rect x="116" y="88"  width="24" height="5"  fill="#C0A050" rx="1"/>')
A('<rect x="121" y="96"  width="7"  height="10" fill="#1840A0" rx="3" opacity="0.68"/>')
A('<rect x="130" y="96"  width="7"  height="10" fill="#1840A0" rx="3" opacity="0.68"/>')
for bx in [116, 122, 128, 134]:
    A(f'<rect x="{bx}" y="83" width="5" height="6" fill="#C0A050" rx="1"/>')
for y in [96, 106, 116]:
    A(f'<line x1="118" y1="{y}" x2="138" y2="{y}" stroke="#9A7828" stroke-width="0.8" opacity="0.26"/>')

# ── Connecting city wall ───────────────────────────────────────────────
A('<rect x="36"  y="118" width="40" height="14" fill="#CEAC68" rx="1"/>')
A('<rect x="36"  y="114" width="40" height="6"  fill="#BEAA5C"/>')
for bx in range(38, 74, 6):
    A(f'<rect x="{bx}" y="109" width="5" height="6" fill="#BEAA5C" rx="1"/>')
A('<rect x="138" y="126" width="12" height="8"  fill="#CEAC68" rx="1"/>')
for bx in [138, 144]:
    A(f'<rect x="{bx}" y="121" width="5" height="6" fill="#C0AA58" rx="1"/>')

# ── Lookout platform (far left edge of cliff) ─────────────────────────
A('<rect x="0"  y="132" width="16" height="8"  fill="#C8A460" rx="1" opacity="0.88"/>')
A('<rect x="0"  y="128" width="20" height="5"  fill="#B89450" rx="1" opacity="0.82"/>')
for bx in [0, 5, 10, 15]:
    A(f'<rect x="{bx}" y="123" width="4" height="6" fill="#B89450" rx="1" opacity="0.80"/>')

# ═══ RIGHT CLIFF ════════════════════════════════════════════════════════
A('<polygon points="400,108 400,600 252,600 252,260 292,192 348,126 400,108" fill="url(#nCliff)"/>')
A('<polygon points="400,108 400,128 378,600 366,600 366,234 400,120" fill="#1C0E02" opacity="0.40"/>')
A('<polygon points="400,108 348,126 292,192 252,260 252,600 268,600 268,268 302,204 350,138 400,120" fill="#5A3A14" opacity="0.22"/>')
# Right cliff strata
for y, op in [(132,0.36),(152,0.32),(172,0.29),(196,0.26),(222,0.23),(250,0.21),(274,0.19)]:
    x1 = max(252, 400 - (y - 108) // 2 - 34)
    x2 = min(400, 400 - (y - 108) // 6)
    A(f'<path d="M{x1},{y} Q{(x1+x2)//2},{y-4} {x2},{y}" stroke="#7A5020" stroke-width="1.8" fill="none" opacity="{op}"/>')
for y, op in [(142,0.21),(164,0.19),(186,0.17),(212,0.16),(238,0.15),(264,0.14)]:
    x1 = max(252, 400 - (y - 108) // 4 - 10)
    A(f'<path d="M{x1},{y} Q{(x1+400)//2},{y-2} 400,{y}" stroke="#6A4210" stroke-width="0.9" fill="none" opacity="{op}"/>')
# Right cliff crevices
A('<path d="M372,130 Q368,157 370,184 Q372,212 368,244" stroke="#3A1E04" stroke-width="1.5" fill="none" opacity="0.32"/>')
A('<path d="M308,172 Q312,197 310,224" stroke="#3A1E04" stroke-width="1.2" fill="none" opacity="0.26"/>')
# Right cliff vegetation
A('<ellipse cx="268" cy="228" rx="16" ry="6"  fill="#385E18" opacity="0.58"/>')
A('<ellipse cx="308" cy="242" rx="22" ry="7"  fill="#406620" opacity="0.54"/>')
A('<ellipse cx="350" cy="256" rx="16" ry="5"  fill="#385E18" opacity="0.50"/>')
A('<ellipse cx="382" cy="270" rx="12" ry="4"  fill="#406620" opacity="0.44"/>')

# ═══ RIGHT CLIFF CITY ═══════════════════════════════════════════════════
# ── Maelstrom tower (right cliff, main tower) ──────────────────────────
A('<rect x="332" y="70"  width="30" height="58" fill="url(#nBldg)" rx="15"/>')
A('<ellipse cx="347" cy="70"  rx="15" ry="5"  fill="#D4BC70"/>')
A('<ellipse cx="347" cy="128" rx="15" ry="4"  fill="#C8B060" opacity="0.65"/>')
A('<polygon points="332,72 362,72 347,50" fill="#7A6028"/>')
A('<polygon points="334,72 360,72 347,54" fill="#8A7030" opacity="0.57"/>')
for bx in [332, 338, 344, 350, 356]:
    A(f'<rect x="{bx}" y="66" width="5" height="7" fill="#C4A04C" rx="1"/>')
A('<rect x="343" y="80"  width="8" height="11" fill="#1840A0" rx="3" opacity="0.76"/>')
A('<rect x="343" y="97"  width="8" height="10" fill="#1848B0" rx="3" opacity="0.66"/>')
A('<rect x="343" y="113" width="8" height="9"  fill="#1840A0" rx="3" opacity="0.56"/>')
for y in [86, 96, 106, 116, 124]:
    A(f'<line x1="334" y1="{y}" x2="360" y2="{y}" stroke="#9A7828" stroke-width="0.8" opacity="0.28"/>')
# Maelstrom banner on right tower
A('<rect x="362" y="58"  width="15" height="26" fill="#A01818" rx="1" opacity="0.88"/>')
A('<polygon points="362,84 377,84 377,90 369,95 362,90" fill="#880808" opacity="0.74"/>')
A('<line x1="362" y1="71" x2="377" y2="71" stroke="#CC3828" stroke-width="1.3" opacity="0.65"/>')

# ── Right main building ────────────────────────────────────────────────
A('<rect x="272" y="84"  width="40" height="48" fill="url(#nBldg)" rx="1"/>')
A('<rect x="270" y="82"  width="44" height="5"  fill="#BEAA50" rx="1"/>')
for bx in [276, 288, 300]:
    A(f'<rect x="{bx}" y="90" width="8" height="12" fill="#1840A0" rx="4" opacity="0.72"/>')
for bx in [276, 288, 300]:
    A(f'<rect x="{bx}" y="108" width="8" height="10" fill="#1848B0" rx="3" opacity="0.62"/>')
for bx in [270, 276, 282, 288, 294, 300, 306]:
    A(f'<rect x="{bx}" y="76" width="5" height="7" fill="#BEAA50" rx="1"/>')
for y in [94, 104, 114, 124]:
    A(f'<line x1="272" y1="{y}" x2="312" y2="{y}" stroke="#9A7828" stroke-width="0.8" opacity="0.24"/>')

# ── Right small tower ──────────────────────────────────────────────────
A('<rect x="252" y="94"  width="20" height="36" fill="#DCBE78" rx="1"/>')
A('<rect x="250" y="92"  width="24" height="5"  fill="#C0A050" rx="1"/>')
A('<rect x="255" y="100" width="7"  height="10" fill="#1840A0" rx="3" opacity="0.66"/>')
A('<rect x="264" y="100" width="7"  height="10" fill="#1840A0" rx="3" opacity="0.66"/>')
for bx in [250, 256, 262, 268]:
    A(f'<rect x="{bx}" y="87" width="5" height="6" fill="#C0A050" rx="1"/>')

# ── Right connecting wall ──────────────────────────────────────────────
A('<rect x="320" y="122" width="36" height="12" fill="#CEAC68" rx="1"/>')
A('<rect x="320" y="118" width="36" height="6"  fill="#BEAA5C"/>')
for bx in range(322, 354, 6):
    A(f'<rect x="{bx}" y="113" width="5" height="6" fill="#BEAA5C" rx="1"/>')

# ═══ STONE ARCH BRIDGE ══════════════════════════════════════════════════
# The iconic elevated stone walkway connecting the two cliff cities
A('<path d="M76,136 Q118,114 200,108 Q282,114 324,130" '
  'stroke="#3A2408" stroke-width="22" fill="none" stroke-linecap="butt" opacity="0.90"/>')
A('<path d="M76,136 Q118,114 200,108 Q282,114 324,130" '
  'stroke="url(#nGate)" stroke-width="17" fill="none" stroke-linecap="butt"/>')
A('<path d="M78,133 Q118,111 200,105 Q282,111 322,127" '
  'stroke="#E8CC78" stroke-width="3.5" fill="none" stroke-linecap="butt" opacity="0.34"/>')
A('<path d="M78,138 Q118,118 200,112 Q282,118 322,132" '
  'stroke="#1E1006" stroke-width="5" fill="none" stroke-linecap="butt" opacity="0.48"/>')
# Voussoir joints
for t in range(1, 8):
    frac = t / 8.0
    bx = int(76 + frac * (324 - 76))
    by = int(136 - 28 * 4 * frac * (1 - frac))
    bx2 = bx + int(5 * (frac - 0.5) * 2)
    by2 = by - 15
    A(f'<line x1="{bx}" y1="{by}" x2="{bx2}" y2="{by2}" stroke="#3A2408" stroke-width="2" opacity="0.36"/>')
# Bridge top battlements
for t in range(0, 9):
    frac = t / 8.0
    bx = int(76 + frac * (324 - 76))
    by = int(136 - 28 * 4 * frac * (1 - frac)) - 11
    A(f'<rect x="{bx-3}" y="{by-7}" width="5" height="7" fill="#C8A860" rx="1" opacity="0.68"/>')

# ═══ HARBOR / DOCK ══════════════════════════════════════════════════════
A('<rect y="280" width="400" height="74" fill="url(#nDock)"/>')
A('<rect y="278" width="400" height="7"  fill="#D4B86C" opacity="0.86"/>')
A('<rect y="280" width="400" height="3"  fill="#E8CC80" opacity="0.42"/>')
# Stone coursing
for y in range(294, 354, 14):
    A(f'<line x1="0" y1="{y}" x2="400" y2="{y}" stroke="#8A6A28" stroke-width="1.2" opacity="0.30"/>')
for x in range(0, 401, 38):
    A(f'<line x1="{x}" y1="280" x2="{x}" y2="354" stroke="#8A6A28" stroke-width="0.8" opacity="0.22"/>')
# Mooring bollards
for bx in [28, 90, 164, 236, 310, 372]:
    A(f'<rect x="{bx-5}" y="286" width="10" height="10" fill="#6A5228" rx="3"/>')
    A(f'<ellipse cx="{bx}" cy="286" rx="6"  ry="2.5" fill="#806038"/>')
    A(f'<ellipse cx="{bx}" cy="296" rx="6"  ry="2"   fill="#583E18"/>')
    A(f'<rect x="{bx-1}" y="282" width="2"  height="4"  fill="#9A7240" opacity="0.55"/>')
# Rope coils
A('<path d="M52,308 Q64,304 76,308 Q64,312 52,308" stroke="#8A6030" stroke-width="2.8" fill="none" opacity="0.64"/>')
A('<path d="M55,309 Q64,306 73,309" stroke="#6A4820" stroke-width="1.5" fill="none" opacity="0.48"/>')
A('<path d="M296,306 Q310,302 324,306 Q310,310 296,306" stroke="#8A6030" stroke-width="2.5" fill="none" opacity="0.60"/>')
# Dock ship mast (docked vessel)
A('<rect x="192" y="214" width="5"  height="70" fill="#3A2410" rx="1" opacity="0.76"/>')
A('<rect x="186" y="228" width="18" height="3"  fill="#4A3018" rx="1" opacity="0.68"/>')
A('<polygon points="186,231 197,218 197,231" fill="url(#nSail)" opacity="0.54"/>')
A('<polygon points="197,221 203,231 197,231" fill="#DED8C4" opacity="0.50"/>')
A('<rect x="174" y="278" width="50" height="6"  fill="#3A2210" rx="2" opacity="0.66"/>')
A('<polygon points="174,278 176,288 222,288 224,278" fill="#3A2210" opacity="0.56"/>')
# Left barrels
A('<ellipse cx="116" cy="320" rx="12" ry="9"  fill="#6A3E18"/>')
A('<ellipse cx="116" cy="311" rx="12" ry="3.5" fill="#7A4E22"/>')
A('<ellipse cx="116" cy="329" rx="12" ry="3.5" fill="#7A4E22"/>')
A('<rect x="104" y="311" width="5"  height="18" fill="#906028" opacity="0.55"/>')
A('<rect x="119" y="311" width="5"  height="18" fill="#6A4018" opacity="0.38"/>')
A('<ellipse cx="140" cy="316" rx="10" ry="7"  fill="#6A3E18"/>')
A('<ellipse cx="140" cy="309" rx="10" ry="3"  fill="#7A4E22"/>')
A('<ellipse cx="140" cy="323" rx="10" ry="3"  fill="#7A4E22"/>')
A('<rect x="130" y="309" width="4"  height="14" fill="#906028" opacity="0.50"/>')
# Right barrels
A('<ellipse cx="280" cy="318" rx="12" ry="9"  fill="#6A3E18"/>')
A('<ellipse cx="280" cy="309" rx="12" ry="3.5" fill="#7A4E22"/>')
A('<ellipse cx="280" cy="327" rx="12" ry="3.5" fill="#7A4E22"/>')
A('<rect x="268" y="309" width="5"  height="18" fill="#906028" opacity="0.52"/>')
A('<ellipse cx="305" cy="314" rx="9"  ry="7"   fill="#6A3E18"/>')
A('<ellipse cx="305" cy="307" rx="9"  ry="2.8" fill="#7A4E22"/>')
A('<ellipse cx="305" cy="321" rx="9"  ry="2.8" fill="#7A4E22"/>')
# Iron cleats
A('<rect x="196" y="288" width="10" height="7" fill="#484040" rx="2"/>')
A('<rect x="198" y="284" width="4"  height="5" fill="#383030" rx="1"/>')
A('<rect x="340" y="288" width="10" height="7" fill="#484040" rx="2"/>')
A('<rect x="342" y="284" width="4"  height="5" fill="#383030" rx="1"/>')

# ═══ LEFT FOREGROUND TOWER ══════════════════════════════════════════════
A('<rect x="0"  y="254" width="72" height="346" fill="url(#nWall)"/>')
A('<rect x="0"  y="254" width="16" height="346" fill="#1E1002" opacity="0.44"/>')
A('<rect x="58" y="254" width="14" height="346" fill="#1E1002" opacity="0.20"/>')
for y in range(268, 601, 18):
    A(f'<rect x="0" y="{y}" width="72" height="7" fill="#A07E34" opacity="0.20"/>')
A('<line x1="36" y1="254" x2="36" y2="600" stroke="#8A6A28" stroke-width="0.7" opacity="0.20"/>')
# Battlements
A('<rect x="0"  y="240" width="72" height="16" fill="#D8B86C" rx="1"/>')
A('<rect x="0"  y="236" width="72" height="6"  fill="#C8A858" opacity="0.82"/>')
for bx in range(0, 70, 9):
    A(f'<rect x="{bx}" y="226" width="7" height="12" fill="#D0B060" rx="1"/>')
# Arrow slits
for wy, h in [(280,28),(326,26),(372,24),(418,22)]:
    A(f'<rect x="18" y="{wy}" width="20" height="{h}" fill="#18389A" rx="8" opacity="0.76"/>')
    A(f'<rect x="21" y="{wy+2}" width="6" height="{h-4}" fill="#3050B8" rx="3" opacity="0.44"/>')
    A(f'<rect x="29" y="{wy+2}" width="6" height="{h-4}" fill="#2848B0" rx="3" opacity="0.34"/>')
A('<rect x="24" y="464" width="10" height="18" fill="#18389A" rx="4" opacity="0.60"/>')
# Maelstrom banner
A('<rect x="50" y="258" width="16" height="30" fill="#A01818" rx="1" opacity="0.92"/>')
A('<polygon points="50,288 66,288 66,294 58,299 50,294" fill="#880808" opacity="0.76"/>')
A('<line x1="50" y1="273" x2="66" y2="273" stroke="#CC3828" stroke-width="1.3" opacity="0.68"/>')
A('<line x1="58" y1="262" x2="58" y2="272" stroke="#E04040" stroke-width="1.5" opacity="0.52"/>')
A('<path d="M54,264 Q58,262 62,264" stroke="#E04040" stroke-width="1.1" fill="none" opacity="0.48"/>')
A('<path d="M55,270 Q58,273 61,270" stroke="#E04040" stroke-width="1.1" fill="none" opacity="0.45"/>')
# Molding strips
A('<rect x="0" y="240" width="72" height="3" fill="#C0A050" opacity="0.58"/>')
A('<rect x="0" y="254" width="72" height="3" fill="#B89040" opacity="0.48"/>')

# ═══ RIGHT FOREGROUND TOWER ═════════════════════════════════════════════
A('<rect x="328" y="240" width="72" height="360" fill="url(#nWall)"/>')
A('<rect x="384" y="240" width="16" height="360" fill="#1E1002" opacity="0.40"/>')
A('<rect x="328" y="240" width="14" height="360" fill="#1E1002" opacity="0.18"/>')
for y in range(254, 601, 18):
    A(f'<rect x="328" y="{y}" width="72" height="7" fill="#A07E34" opacity="0.20"/>')
A('<line x1="364" y1="240" x2="364" y2="600" stroke="#8A6A28" stroke-width="0.7" opacity="0.18"/>')
A('<rect x="328" y="226" width="72" height="16" fill="#D8B86C" rx="1"/>')
A('<rect x="328" y="222" width="72" height="6"  fill="#C8A858" opacity="0.80"/>')
for bx in range(329, 398, 9):
    A(f'<rect x="{bx}" y="212" width="7" height="12" fill="#D0B060" rx="1"/>')
for wy, h in [(266,28),(312,26),(358,24),(404,22)]:
    A(f'<rect x="362" y="{wy}" width="20" height="{h}" fill="#18389A" rx="8" opacity="0.76"/>')
    A(f'<rect x="365" y="{wy+2}" width="6" height="{h-4}" fill="#3050B8" rx="3" opacity="0.44"/>')
    A(f'<rect x="373" y="{wy+2}" width="6" height="{h-4}" fill="#2848B0" rx="3" opacity="0.34"/>')
A('<rect x="366" y="450" width="10" height="18" fill="#18389A" rx="4" opacity="0.60"/>')
A('<rect x="334" y="244" width="16" height="30" fill="#A01818" rx="1" opacity="0.90"/>')
A('<polygon points="334,274 350,274 350,280 342,285 334,280" fill="#880808" opacity="0.74"/>')
A('<line x1="334" y1="259" x2="350" y2="259" stroke="#CC3828" stroke-width="1.3" opacity="0.66"/>')
A('<line x1="342" y1="248" x2="342" y2="258" stroke="#E04040" stroke-width="1.5" opacity="0.50"/>')
A('<path d="M338,250 Q342,248 346,250" stroke="#E04040" stroke-width="1.1" fill="none" opacity="0.46"/>')
A('<path d="M339,256 Q342,259 345,256" stroke="#E04040" stroke-width="1.1" fill="none" opacity="0.43"/>')
A('<rect x="328" y="226" width="72" height="3" fill="#C0A050" opacity="0.55"/>')
A('<rect x="328" y="240" width="72" height="3" fill="#B89040" opacity="0.45"/>')

# ═══ PLAZA / STONE GROUND ═══════════════════════════════════════════════
A('<rect y="354" width="400" height="246" fill="url(#nGnd)"/>')
A('<g stroke="#806028" stroke-width="0.9" opacity="0.30">')
for y in range(372, 601, 24):
    A(f'<line x1="0" y1="{y}" x2="400" y2="{y}"/>')
for x in range(0, 401, 44):
    A(f'<line x1="{x}" y1="354" x2="{x}" y2="600"/>')
A('</g>')
# Worn tile accents
for cx, cy, rx, ry, op in [(72,390,16,5,0.18),(200,424,14,4.5,0.15),(334,398,15,5,0.17),
                             (140,454,12,4,0.14),(268,472,12,4,0.14)]:
    A(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#6A4010" opacity="{op}"/>')

# ═══ STAGE 5 — Ship Wheel + Anchor (translate +52) ══════════════════════
A('<g transform="translate(52,0)">')
# Wall-mount bracket
A('<rect x="183" y="232" width="34" height="5"  fill="#4A4040" rx="2"/>')
A('<rect x="184" y="232" width="12" height="2"  fill="#686060" opacity="0.44"/>')
# Axle post
A('<rect x="197" y="218" width="6"  height="54" fill="#4A4040" rx="2"/>')
A('<rect x="198" y="219" width="2"  height="52" fill="#686060" opacity="0.40"/>')
# Chain/rope hanging at bottom (anchor chains)
A('<path d="M197,282 Q182,276 178,268 Q178,260 186,257" stroke="#484840" stroke-width="5.5" fill="none" stroke-linecap="round"/>')
A('<path d="M203,282 Q218,276 222,268 Q222,260 214,257" stroke="#484840" stroke-width="5.5" fill="none" stroke-linecap="round"/>')
A('<path d="M178,268 Q174,262 172,265" stroke="#484840" stroke-width="5.5" fill="none" stroke-linecap="round"/>')
A('<path d="M222,268 Q226,262 228,265" stroke="#484840" stroke-width="5.5" fill="none" stroke-linecap="round"/>')
A('<path d="M197,282 Q183,277 179,269 Q179,261 187,258" stroke="#686860" stroke-width="2.0" fill="none" stroke-linecap="round" opacity="0.42"/>')
# Outer rim (double ring)
A('<circle cx="200" cy="245" r="31" fill="none" stroke="#7A5028" stroke-width="6.5"/>')
A('<circle cx="200" cy="245" r="31" fill="none" stroke="#C49040" stroke-width="2.5" opacity="0.55"/>')
A('<circle cx="200" cy="245" r="28" fill="none" stroke="#5A3C18" stroke-width="1.5" opacity="0.38"/>')
# Inner hub
A('<circle cx="200" cy="245" r="14" fill="#6A3E18"/>')
A('<circle cx="200" cy="245" r="14" fill="none" stroke="#A87030" stroke-width="2.5" opacity="0.74"/>')
# Center boss
A('<circle cx="200" cy="245" r="7"  fill="#8A5820"/>')
A('<circle cx="200" cy="245" r="4"  fill="#A07030" opacity="0.65"/>')
A('<circle cx="200" cy="245" r="2"  fill="#C0A040" opacity="0.50"/>')
# 8 spokes
A('<g stroke="#7A5028" stroke-width="3.8" stroke-linecap="round">'
  '<line x1="200" y1="214" x2="200" y2="231"/>'
  '<line x1="200" y1="259" x2="200" y2="276"/>'
  '<line x1="169" y1="245" x2="186" y2="245"/>'
  '<line x1="214" y1="245" x2="231" y2="245"/>'
  '<line x1="178" y1="223" x2="189" y2="234"/>'
  '<line x1="211" y1="256" x2="222" y2="267"/>'
  '<line x1="222" y1="223" x2="211" y2="234"/>'
  '<line x1="178" y1="256" x2="189" y2="267"/>'
  '</g>')
# Spoke highlight
A('<g stroke="#C09840" stroke-width="1.6" stroke-linecap="round" opacity="0.50">'
  '<line x1="200" y1="214" x2="200" y2="231"/>'
  '<line x1="200" y1="259" x2="200" y2="276"/>'
  '<line x1="169" y1="245" x2="186" y2="245"/>'
  '<line x1="214" y1="245" x2="231" y2="245"/>'
  '</g>')
# 8 handle pegs on rim
A('<g fill="#6A3E18">'
  '<circle cx="200" cy="212" r="5.0"/>'
  '<circle cx="200" cy="278" r="5.0"/>'
  '<circle cx="167" cy="245" r="5.0"/>'
  '<circle cx="233" cy="245" r="5.0"/>'
  '<circle cx="178" cy="221" r="4.5"/>'
  '<circle cx="222" cy="269" r="4.5"/>'
  '<circle cx="222" cy="221" r="4.5"/>'
  '<circle cx="178" cy="269" r="4.5"/>'
  '</g>')
# Peg highlights
A('<g fill="#A07030" opacity="0.46">'
  '<circle cx="200" cy="212" r="2.5"/>'
  '<circle cx="233" cy="245" r="2.5"/>'
  '<circle cx="222" cy="221" r="2.0"/>'
  '</g>')
# Anchor below wheel
A('<ellipse cx="202" cy="288" rx="9"  ry="4"   fill="#484840"/>')      # ring at top
A('<rect x="199" y="288" width="5"  height="20" fill="#484840" rx="1"/>')  # shank
A('<path d="M188,296 Q198,293 202,300 Q206,293 216,296" stroke="#484840" stroke-width="4" fill="none" stroke-linecap="round"/>')  # arms
A('<ellipse cx="188" cy="297" rx="3.5" ry="2.5" fill="#484840"/>')     # left fluke
A('<ellipse cx="216" cy="297" rx="3.5" ry="2.5" fill="#484840"/>')     # right fluke
A('<rect x="194" y="284" width="16" height="3"  fill="#484840" rx="1"/>')  # stock
A('<ellipse cx="202" cy="286" rx="5"  ry="2"   fill="none" stroke="#585858" stroke-width="1.5" opacity="0.60"/>')
A('</g>')  # end translate(52,0)

# ═══ STAGE 10 — Limsan Grand Gate (×1.5) ════════════════════════════════
A('<g transform="translate(200,531) scale(1.5) translate(-200,-531)">')
# Ground shadow
A('<ellipse cx="200" cy="580" rx="74" ry="14" fill="#2C1C04" opacity="0.50"/>')

# ── Left pillar ──────────────────────────────────────────────────────
A('<rect x="136" y="476" width="38" height="96" fill="url(#nGateL)" rx="2"/>')
for cy in range(484, 572, 10):
    A(f'<rect x="136" y="{cy}" width="38" height="5" fill="#8A6030" opacity="0.28"/>')
A('<rect x="138" y="476" width="8"  height="96" fill="#F0CC80" opacity="0.18"/>')
A('<rect x="166" y="476" width="8"  height="96" fill="#2A1804" opacity="0.30"/>')
A('<rect x="132" y="468" width="46" height="10" fill="#A07C34" rx="2"/>')
A('<rect x="128" y="462" width="54" height="8"  fill="#B88E40" rx="2"/>')
for bx in [130, 139, 148, 157, 166]:
    A(f'<rect x="{bx}" y="452" width="8" height="12" fill="#B08438" rx="1"/>')

# ── Left brazier ─────────────────────────────────────────────────────
A('<rect x="150" y="450" width="11" height="18" fill="#5A3C18" rx="3"/>')
A('<ellipse cx="155" cy="449" rx="9"   ry="5"   fill="#4A3010"/>')
A('<ellipse cx="155" cy="443" rx="7"   ry="9"   fill="#FF8820" opacity="0.92"/>')
A('<ellipse cx="155" cy="437" rx="5"   ry="6.5" fill="#FFB040" opacity="0.88"/>')
A('<ellipse cx="155" cy="432" rx="3.5" ry="4.5" fill="#FFE060" opacity="0.84"/>')
A('<ellipse cx="154" cy="428" rx="2"   ry="3"   fill="#FFFFFF"  opacity="0.52"/>')
A('<ellipse cx="148" cy="448" rx="14"  ry="10"  fill="#FF9030" opacity="0.14"/>')

# ── Right pillar ─────────────────────────────────────────────────────
A('<rect x="226" y="476" width="38" height="96" fill="url(#nGate)" rx="2"/>')
for cy in range(484, 572, 10):
    A(f'<rect x="226" y="{cy}" width="38" height="5" fill="#886030" opacity="0.28"/>')
A('<rect x="228" y="476" width="8"  height="96" fill="#E8C870" opacity="0.14"/>')
A('<rect x="256" y="476" width="8"  height="96" fill="#2A1804" opacity="0.26"/>')
A('<rect x="222" y="468" width="46" height="10" fill="#9A7A32" rx="2"/>')
A('<rect x="218" y="462" width="54" height="8"  fill="#B08840" rx="2"/>')
for bx in [220, 229, 238, 247, 256]:
    A(f'<rect x="{bx}" y="452" width="8" height="12" fill="#B08438" rx="1"/>')

# ── Right brazier ────────────────────────────────────────────────────
A('<rect x="239" y="450" width="11" height="18" fill="#5A3C18" rx="3"/>')
A('<ellipse cx="245" cy="449" rx="9"   ry="5"   fill="#4A3010"/>')
A('<ellipse cx="245" cy="443" rx="7"   ry="9"   fill="#FF8820" opacity="0.89"/>')
A('<ellipse cx="245" cy="437" rx="5"   ry="6.5" fill="#FFB040" opacity="0.85"/>')
A('<ellipse cx="245" cy="432" rx="3.5" ry="4.5" fill="#FFE060" opacity="0.81"/>')
A('<ellipse cx="244" cy="428" rx="2"   ry="3"   fill="#FFFFFF"  opacity="0.50"/>')
A('<ellipse cx="252" cy="448" rx="14"  ry="10"  fill="#FF9030" opacity="0.12"/>')

# ── Main arch ────────────────────────────────────────────────────────
A('<path d="M134,502 Q200,450 266,502" stroke="#3A2408" stroke-width="24" fill="none" stroke-linecap="butt"/>')
A('<path d="M134,502 Q200,450 266,502" stroke="url(#nGate)" stroke-width="19" fill="none" stroke-linecap="butt"/>')
A('<path d="M136,500 Q200,452 264,500" stroke="#E8CC70" stroke-width="4" fill="none" stroke-linecap="butt" opacity="0.32"/>')
A('<path d="M148,502 Q200,458 252,502" stroke="#1E1006" stroke-width="5" fill="none" stroke-linecap="butt" opacity="0.52"/>')
# Voussoir joints (stone arch joints)
for x1, y1, x2, y2 in [
    (149,494, 157,479),(163,477, 169,462),(179,466, 182,451),
    (195,461, 196,446),(200,460, 200,444),(205,461, 204,446),
    (221,466, 218,451),(237,477, 231,462),(251,494, 243,479)
]:
    A(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#3A2408" stroke-width="2" opacity="0.38"/>')

# ── Keystone (anchor symbol) ──────────────────────────────────────────
A('<polygon points="193,454 200,442 207,454 205,462 195,462" fill="#9A7C32"/>')
A('<polygon points="194,455 200,445 206,455 204,461 196,461" fill="#C4A840" opacity="0.50"/>')
A('<circle cx="200" cy="454" r="4" fill="#4A3010" opacity="0.82"/>')
A('<line x1="200" y1="449" x2="200" y2="459" stroke="#3A2408" stroke-width="1.6" opacity="0.72"/>')
A('<path d="M196,451 Q200,449 204,451" stroke="#3A2408" stroke-width="1.1" fill="none" opacity="0.62"/>')
A('<path d="M197,457 Q200,460 203,457" stroke="#3A2408" stroke-width="1.1" fill="none" opacity="0.58"/>')

# ── Portcullis ───────────────────────────────────────────────────────
A('<rect x="148" y="500" width="104" height="7" fill="#5A4820" opacity="0.68"/>')
A('<rect x="150" y="501" width="32"  height="2" fill="#A07830" opacity="0.38"/>')
A('<g stroke="#242424" stroke-width="3.2" opacity="0.58">'
  '<line x1="162" y1="507" x2="162" y2="572"/>'
  '<line x1="176" y1="507" x2="176" y2="572"/>'
  '<line x1="190" y1="507" x2="190" y2="572"/>'
  '<line x1="204" y1="507" x2="204" y2="572"/>'
  '<line x1="218" y1="507" x2="218" y2="572"/>'
  '<line x1="232" y1="507" x2="232" y2="572"/>'
  '</g>')
A('<g stroke="#484848" stroke-width="1.0" opacity="0.34">'
  '<line x1="163" y1="507" x2="163" y2="572"/>'
  '<line x1="177" y1="507" x2="177" y2="572"/>'
  '<line x1="191" y1="507" x2="191" y2="572"/>'
  '<line x1="205" y1="507" x2="205" y2="572"/>'
  '</g>')
A('<g fill="#202020" opacity="0.60">'
  '<polygon points="159,572 162,582 165,572"/>'
  '<polygon points="173,572 176,582 179,572"/>'
  '<polygon points="187,572 190,582 193,572"/>'
  '<polygon points="201,572 204,582 207,572"/>'
  '<polygon points="215,572 218,582 221,572"/>'
  '<polygon points="229,572 232,582 235,572"/>'
  '</g>')
A('<g stroke="#282828" stroke-width="2.2" opacity="0.42">'
  '<line x1="148" y1="524" x2="252" y2="524"/>'
  '<line x1="148" y1="546" x2="252" y2="546"/>'
  '<line x1="148" y1="565" x2="252" y2="565"/>'
  '</g>')
# Lifting chains
A('<line x1="162" y1="500" x2="154" y2="472" stroke="#484040" stroke-width="2" opacity="0.52"/>')
A('<line x1="238" y1="500" x2="246" y2="472" stroke="#484040" stroke-width="2" opacity="0.52"/>')

# ── Left Maelstrom banner ─────────────────────────────────────────────
A('<rect x="120" y="476" width="16" height="32" fill="#A01818" rx="1" opacity="0.92"/>')
A('<polygon points="120,508 136,508 136,514 128,519 120,514" fill="#880808" opacity="0.76"/>')
A('<line x1="120" y1="492" x2="136" y2="492" stroke="#CC3828" stroke-width="1.4" opacity="0.68"/>')
A('<line x1="128" y1="479" x2="128" y2="490" stroke="#E04040" stroke-width="1.6" opacity="0.55"/>')
A('<path d="M124,481 Q128,479 132,481" stroke="#E04040" stroke-width="1.1" fill="none" opacity="0.50"/>')
A('<path d="M125,488 Q128,491 131,488" stroke="#E04040" stroke-width="1.1" fill="none" opacity="0.46"/>')

# ── Right Maelstrom banner ────────────────────────────────────────────
A('<rect x="264" y="476" width="16" height="32" fill="#A01818" rx="1" opacity="0.89"/>')
A('<polygon points="264,508 280,508 280,514 272,519 264,514" fill="#880808" opacity="0.74"/>')
A('<line x1="264" y1="492" x2="280" y2="492" stroke="#CC3828" stroke-width="1.4" opacity="0.65"/>')
A('<line x1="272" y1="479" x2="272" y2="490" stroke="#E04040" stroke-width="1.6" opacity="0.52"/>')
A('<path d="M268,481 Q272,479 276,481" stroke="#E04040" stroke-width="1.1" fill="none" opacity="0.48"/>')
A('<path d="M269,488 Q272,491 275,488" stroke="#E04040" stroke-width="1.1" fill="none" opacity="0.44"/>')

A('</g>')  # end scale group

# ═══ ATMOSPHERIC OVERLAYS ═══════════════════════════════════════════════
# Water mist at cliff base / dock edge
A('<rect y="280" width="400" height="16" fill="#C8E8FF" opacity="0.13"/>')
# Ground mist (near bottom)
A('<rect y="580" width="400" height="20" fill="#C8B080" opacity="0.22"/>')

A('</svg>')

NORMAL = ''.join(P)

# ── Inject into stage.html ───────────────────────────────────────────────
pattern = r"(if\(diff==='NORMAL'\) return ')(.*?)(';)"
replacement = r"\g<1>" + NORMAL.replace('\\', '\\\\') + r"\g<3>"
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

assert new_content != content, "Injection failed — pattern not matched"
assert "nSky" in new_content, "SVG missing in output"
print(f"NORMAL SVG: {len(NORMAL):,} chars injected OK")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("stage.html written.")
