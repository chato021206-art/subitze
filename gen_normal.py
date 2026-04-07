#!/usr/bin/env python3
"""NORMAL SVG — Limsa Lominsa-style coastal city (FF14 inspired). No center path."""
import re

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

def J(*parts):
    return ''.join(parts)

# ═══════════════════════════════════════════════════════════════════════
#  NORMAL  海賊都市  Limsa Lominsa — MASTERPIECE
#  ・La Noscea: sea cliffs, azure ocean, warm sandstone, sails
#  ・Towering limestone bluffs, stone arches, distant galleons
#  ・Stage5 (y≈235, x=200+52): 錨と舵 Ship Wheel + Anchor
#  ・Stage10 (y≈531, x=200) ×1.5: リムサ門 Limsan Stone Gate
# ═══════════════════════════════════════════════════════════════════════

NORMAL = J(
    '<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">',
    '<defs>',

    # Sky — La Noscea's brilliant azure
    '<linearGradient id="nSky" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%"   stop-color="#1868C8"/>',
    '<stop offset="28%"  stop-color="#2E82DC"/>',
    '<stop offset="60%"  stop-color="#5AAAE8"/>',
    '<stop offset="88%"  stop-color="#88C8F0"/>',
    '<stop offset="100%" stop-color="#B0DCF8"/>',
    '</linearGradient>',

    # Ocean — deep teal blue
    '<linearGradient id="nSea" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%"   stop-color="#1A6CA0"/>',
    '<stop offset="40%"  stop-color="#135880"/>',
    '<stop offset="100%" stop-color="#0A3A58"/>',
    '</linearGradient>',

    # Ocean shimmer (radial highlight)
    '<radialGradient id="nSeaShim" cx="50%" cy="15%" r="55%">',
    '<stop offset="0%"   stop-color="#60C0E8" stop-opacity="0.35"/>',
    '<stop offset="100%" stop-color="#60C0E8" stop-opacity="0"/>',
    '</radialGradient>',

    # Limestone cliff
    '<linearGradient id="nCliff" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%"   stop-color="#C8A870"/>',
    '<stop offset="40%"  stop-color="#B89458"/>',
    '<stop offset="100%" stop-color="#906830"/>',
    '</linearGradient>',

    # Cliff shadow side
    '<linearGradient id="nCliffS" x1="0" y1="0" x2="1" y2="0">',
    '<stop offset="0%"   stop-color="#5A3C14"/>',
    '<stop offset="40%"  stop-color="#7A5428"/>',
    '<stop offset="100%" stop-color="#604020"/>',
    '</linearGradient>',

    # Sandstone wall
    '<linearGradient id="nWall" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%"   stop-color="#D4B078"/>',
    '<stop offset="50%"  stop-color="#C09858"/>',
    '<stop offset="100%" stop-color="#A07840"/>',
    '</linearGradient>',

    # Gate stone
    '<linearGradient id="nGate" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%"   stop-color="#B89860"/>',
    '<stop offset="55%"  stop-color="#A07840"/>',
    '<stop offset="100%" stop-color="#7A5A28"/>',
    '</linearGradient>',

    # Gate left side lit
    '<linearGradient id="nGateL" x1="0" y1="0" x2="1" y2="0">',
    '<stop offset="0%"   stop-color="#C8A868"/>',
    '<stop offset="60%"  stop-color="#A88040"/>',
    '<stop offset="100%" stop-color="#806028"/>',
    '</linearGradient>',

    # White sail
    '<linearGradient id="nSail" x1="0" y1="0" x2="1" y2="1">',
    '<stop offset="0%"   stop-color="#F0ECD8"/>',
    '<stop offset="100%" stop-color="#C8C0A0"/>',
    '</linearGradient>',

    # Sun glare on horizon
    '<radialGradient id="nSun" cx="75%" cy="38%" r="35%">',
    '<stop offset="0%"   stop-color="#FFFCE0" stop-opacity="0.68"/>',
    '<stop offset="40%"  stop-color="#FFE880" stop-opacity="0.28"/>',
    '<stop offset="100%" stop-color="#FFD040" stop-opacity="0"/>',
    '</radialGradient>',

    # Ground — stone plaza / dock
    '<linearGradient id="nGnd" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%"   stop-color="#9A7A48"/>',
    '<stop offset="45%"  stop-color="#7A5C30"/>',
    '<stop offset="100%" stop-color="#503C18"/>',
    '</linearGradient>',

    # Water glow filter
    '<filter id="nWaterF" x="-20%" y="-20%" width="140%" height="140%">',
    '<feGaussianBlur stdDeviation="2.5" result="b"/>',
    '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>',
    '</filter>',

    '</defs>',

    # ── SKY ──────────────────────────────────────────────────
    '<rect width="400" height="600" fill="url(#nSky)"/>',
    '<rect width="400" height="600" fill="url(#nSun)"/>',

    # ── CLOUDS ───────────────────────────────────────────────
    # Large cumulus left
    '<ellipse cx="62"  cy="48"  rx="52" ry="22" fill="#FFF" opacity="0.88"/>',
    '<ellipse cx="44"  cy="56"  rx="32" ry="16" fill="#FFF" opacity="0.82"/>',
    '<ellipse cx="84"  cy="56"  rx="34" ry="14" fill="#FFF" opacity="0.80"/>',
    '<ellipse cx="62"  cy="64"  rx="46" ry="10" fill="#F0EDE4" opacity="0.72"/>',
    # Smaller right
    '<ellipse cx="310" cy="36"  rx="44" ry="18" fill="#FFF" opacity="0.84"/>',
    '<ellipse cx="290" cy="44"  rx="28" ry="13" fill="#FFF" opacity="0.78"/>',
    '<ellipse cx="332" cy="44"  rx="30" ry="12" fill="#FFF" opacity="0.76"/>',
    # Wispy mid
    '<ellipse cx="172" cy="28"  rx="36" ry="10" fill="#FFF" opacity="0.62"/>',
    '<ellipse cx="210" cy="22"  rx="26" ry="8"  fill="#FFF" opacity="0.54"/>',

    # ── SEAGULLS ─────────────────────────────────────────────
    '<path d="M58,88 Q64,82 70,88"  stroke="#8898B0" stroke-width="1.8" fill="none"/>',
    '<path d="M72,78 Q79,71 86,78"  stroke="#8898B0" stroke-width="1.8" fill="none"/>',
    '<path d="M238,64 Q244,58 250,64" stroke="#8898B0" stroke-width="1.6" fill="none"/>',
    '<path d="M256,74 Q261,68 266,74" stroke="#9AAABE" stroke-width="1.5" fill="none"/>',
    '<path d="M148,104 Q154,98 160,104" stroke="#9AAABE" stroke-width="1.5" fill="none"/>',
    '<path d="M342,58 Q348,52 354,58" stroke="#8898B0" stroke-width="1.5" fill="none"/>',

    # ── DISTANT OCEAN ─────────────────────────────────────────
    '<rect y="138" width="400" height="188" fill="url(#nSea)"/>',
    '<rect y="138" width="400" height="188" fill="url(#nSeaShim)"/>',
    # Horizon line shimmer
    '<rect y="136" width="400" height="5" fill="#C8E8F8" opacity="0.38"/>',
    # Wave streaks
    '<path d="M0,162 Q40,157 80,162 Q120,167 160,162 Q200,157 240,162 Q280,167 320,162 Q360,157 400,162" stroke="#3898C8" stroke-width="1.4" fill="none" opacity="0.48"/>',
    '<path d="M0,185 Q50,180 100,185 Q150,190 200,185 Q250,180 300,185 Q350,190 400,185" stroke="#3088B8" stroke-width="1.2" fill="none" opacity="0.40"/>',
    '<path d="M0,210 Q60,205 120,210 Q180,215 240,210 Q300,205 360,210 Q380,213 400,210" stroke="#2878A8" stroke-width="1.1" fill="none" opacity="0.35"/>',
    '<path d="M0,238 Q80,233 160,238 Q240,243 320,238 Q360,235 400,238" stroke="#206898" stroke-width="1.0" fill="none" opacity="0.30"/>',
    # Water sparkles
    '<circle cx="88"  cy="170" r="1.8" fill="#A8E0F8" opacity="0.62"/>',
    '<circle cx="192" cy="158" r="2.2" fill="#B8E8FF" opacity="0.58"/>',
    '<circle cx="288" cy="178" r="1.6" fill="#A0D8F0" opacity="0.55"/>',
    '<circle cx="52"  cy="202" r="1.4" fill="#A8E0F8" opacity="0.50"/>',
    '<circle cx="348" cy="192" r="1.8" fill="#B0E4F8" opacity="0.52"/>',
    '<circle cx="148" cy="222" r="1.6" fill="#98D8F0" opacity="0.46"/>',
    '<circle cx="330" cy="218" r="1.4" fill="#A0DCF4" opacity="0.44"/>',

    # ── DISTANT GALLEONS ─────────────────────────────────────
    # Ship 1 (left, far)
    '<rect x="28"  y="146" width="52" height="10" fill="#4A3018" rx="2" opacity="0.72"/>',
    '<rect x="44"  y="122" width="4"  height="26" fill="#382010" opacity="0.70"/>',
    '<polygon points="44,124 58,144 44,144" fill="url(#nSail)" opacity="0.76"/>',
    '<polygon points="48,128 66,144 48,144" fill="url(#nSail)" opacity="0.68"/>',
    '<rect x="60"  y="130" width="3"  height="18" fill="#382010" opacity="0.68"/>',
    '<polygon points="60,132 72,144 60,144" fill="#E8E4D0" opacity="0.65"/>',
    # Ship 2 (right, farther)
    '<rect x="318" y="150" width="58" height="9"  fill="#4A3018" rx="2" opacity="0.65"/>',
    '<rect x="336" y="128" width="4"  height="24" fill="#382010" opacity="0.63"/>',
    '<polygon points="336,130 350,150 336,150" fill="url(#nSail)" opacity="0.68"/>',
    '<polygon points="340,134 358,150 340,150" fill="#E0DCC8" opacity="0.60"/>',
    '<rect x="352" y="134" width="3"  height="18" fill="#382010" opacity="0.62"/>',
    '<polygon points="352,136 364,150 352,150" fill="#E8E4D0" opacity="0.58"/>',

    # ── LIMESTONE CLIFFS & CITY SILHOUETTE ────────────────────
    # Far cliff (center-back city silhouette)
    '<polygon points="88,138 180,68 260,60 340,72 380,138" fill="#B89060" opacity="0.52"/>',
    '<polygon points="88,138 120,108 160,88 200,76 240,80 280,92 320,104 356,118 380,138" fill="#C8A070" opacity="0.44"/>',
    # Tower tops (city on the cliff)
    '<rect x="128" y="72" width="10" height="30" fill="#A07838" opacity="0.56"/>',
    '<rect x="125" y="70" width="16" height="5"  fill="#8A6028" opacity="0.54"/>',
    '<rect x="180" y="60" width="14" height="28" fill="#A87E3E" opacity="0.60"/>',
    '<rect x="177" y="58" width="20" height="5"  fill="#8A6028" opacity="0.58"/>',
    '<rect x="226" y="64" width="12" height="26" fill="#A07838" opacity="0.56"/>',
    '<rect x="223" y="62" width="18" height="5"  fill="#886228" opacity="0.54"/>',
    '<rect x="272" y="72" width="11" height="28" fill="#9C7434" opacity="0.52"/>',
    '<rect x="269" y="70" width="17" height="5"  fill="#846024" opacity="0.50"/>',
    # City wall parapet
    '<rect x="108" y="94" width="200" height="8" fill="#B08848" opacity="0.46"/>',
    '<rect x="116" y="90" width="8"   height="6" fill="#B08848" opacity="0.42"/>',
    '<rect x="136" y="90" width="8"   height="6" fill="#B08848" opacity="0.40"/>',
    '<rect x="156" y="90" width="8"   height="6" fill="#B08848" opacity="0.42"/>',
    '<rect x="176" y="90" width="8"   height="6" fill="#B08848" opacity="0.40"/>',
    '<rect x="206" y="90" width="8"   height="6" fill="#B08848" opacity="0.40"/>',
    '<rect x="226" y="90" width="8"   height="6" fill="#B08848" opacity="0.38"/>',
    '<rect x="246" y="90" width="8"   height="6" fill="#B08848" opacity="0.40"/>',
    '<rect x="276" y="90" width="8"   height="6" fill="#B08848" opacity="0.38"/>',

    # Main foreground cliff face (left)
    '<polygon points="0,326 0,600 148,600 148,280 80,200 0,200" fill="url(#nCliff)"/>',
    '<polygon points="0,200 0,600 40,600 40,240 0,200" fill="url(#nCliffS)" opacity="0.55"/>',
    # Cliff texture lines
    '<path d="M8,240 Q28,232 52,238 Q72,244 90,236 Q110,228 130,234" stroke="#906A30" stroke-width="1.8" fill="none" opacity="0.40"/>',
    '<path d="M4,278 Q30,270 58,276 Q84,282 110,272 Q134,264 148,270" stroke="#806020" stroke-width="1.6" fill="none" opacity="0.38"/>',
    '<path d="M0,318 Q32,310 64,316 Q96,322 128,312 Q144,308 148,310" stroke="#704C18" stroke-width="1.5" fill="none" opacity="0.35"/>',
    # Cliff moss/lichen patches
    '<ellipse cx="22"  cy="248" rx="16" ry="6"  fill="#4A6818" opacity="0.44"/>',
    '<ellipse cx="78"  cy="262" rx="20" ry="7"  fill="#486218" opacity="0.40"/>',
    '<ellipse cx="122" cy="296" rx="14" ry="5"  fill="#4A6018" opacity="0.38"/>',
    '<ellipse cx="48"  cy="308" rx="12" ry="4.5" fill="#486018" opacity="0.36"/>',

    # Main foreground cliff face (right)
    '<polygon points="400,310 400,600 252,600 252,268 320,186 400,186" fill="url(#nCliff)"/>',
    '<polygon points="400,186 400,600 360,600 360,224 400,186" fill="url(#nCliffS)" opacity="0.48"/>',
    # Cliff texture lines
    '<path d="M268,224 Q292,216 316,222 Q338,228 358,220 Q376,214 400,218" stroke="#906A30" stroke-width="1.8" fill="none" opacity="0.40"/>',
    '<path d="M256,268 Q280,260 304,266 Q328,272 352,262 Q376,254 400,258" stroke="#806020" stroke-width="1.6" fill="none" opacity="0.38"/>',
    '<path d="M252,310 Q276,302 302,308 Q326,314 352,304 Q376,296 400,300" stroke="#704C18" stroke-width="1.5" fill="none" opacity="0.35"/>',
    '<ellipse cx="278" cy="242" rx="16" ry="6"  fill="#4A6818" opacity="0.44"/>',
    '<ellipse cx="322" cy="256" rx="18" ry="6"  fill="#486218" opacity="0.40"/>',
    '<ellipse cx="368" cy="282" rx="14" ry="5"  fill="#4A6018" opacity="0.38"/>',
    '<ellipse cx="340" cy="308" rx="12" ry="4.5" fill="#486018" opacity="0.36"/>',

    # ── STONE PLAZA / DOCK FLOOR ─────────────────────────────
    '<rect y="326" width="400" height="274" fill="url(#nGnd)"/>',
    # Stone tile grid
    '<g stroke="#604020" stroke-width="0.7" opacity="0.25">',
    '<line x1="0" y1="348" x2="400" y2="348"/>',
    '<line x1="0" y1="374" x2="400" y2="374"/>',
    '<line x1="0" y1="400" x2="400" y2="400"/>',
    '<line x1="0" y1="428" x2="400" y2="428"/>',
    '<line x1="0" y1="458" x2="400" y2="458"/>',
    '<line x1="66" y1="326" x2="66" y2="600"/>',
    '<line x1="133" y1="326" x2="133" y2="600"/>',
    '<line x1="200" y1="326" x2="200" y2="600"/>',
    '<line x1="267" y1="326" x2="267" y2="600"/>',
    '<line x1="334" y1="326" x2="334" y2="600"/>',
    '</g>',
    # Worn stone marks
    '<ellipse cx="68"  cy="362" rx="12" ry="4"  fill="#503018" opacity="0.22"/>',
    '<ellipse cx="192" cy="410" rx="10" ry="3.5" fill="#503018" opacity="0.18"/>',
    '<ellipse cx="338" cy="368" rx="11" ry="4"  fill="#503018" opacity="0.20"/>',

    # ── STONE ARCH / WALL STRUCTURES LEFT ────────────────────
    # Left tower base
    '<rect x="0"   y="264" width="56" height="336" fill="url(#nWall)"/>',
    '<rect x="0"   y="264" width="12" height="336" fill="#7A5428" opacity="0.35"/>',
    # Stone block texture
    '<rect x="0"   y="272" width="56" height="9"  fill="#A07030" opacity="0.30"/>',
    '<rect x="0"   y="294" width="56" height="9"  fill="#A07030" opacity="0.28"/>',
    '<rect x="0"   y="316" width="56" height="9"  fill="#A07030" opacity="0.28"/>',
    '<rect x="0"   y="338" width="56" height="9"  fill="#A07030" opacity="0.26"/>',
    '<rect x="0"   y="362" width="56" height="9"  fill="#A07030" opacity="0.24"/>',
    '<rect x="0"   y="388" width="56" height="9"  fill="#A07030" opacity="0.24"/>',
    # Window
    '<rect x="12"  y="298" width="20" height="28" fill="#2040A0" rx="9" opacity="0.70"/>',
    '<rect x="14"  y="300" width="8"  height="24" fill="#4060C0" rx="4" opacity="0.48"/>',
    '<rect x="22"  y="300" width="8"  height="24" fill="#3858B8" rx="4" opacity="0.38"/>',
    # Parapet top
    '<rect x="0"   y="252" width="56" height="14" fill="#9A7240" rx="1"/>',
    '<rect x="4"   y="244" width="10" height="10" fill="#9A7240" rx="1"/>',
    '<rect x="20"  y="244" width="10" height="10" fill="#9A7240" rx="1"/>',
    '<rect x="36"  y="244" width="10" height="10" fill="#9A7240" rx="1"/>',

    # ── STONE ARCH / WALL STRUCTURES RIGHT ───────────────────
    '<rect x="344" y="252" width="56" height="348" fill="url(#nWall)"/>',
    '<rect x="388" y="252" width="12" height="348" fill="#7A5428" opacity="0.30"/>',
    '<rect x="344" y="260" width="56" height="9"  fill="#A07030" opacity="0.30"/>',
    '<rect x="344" y="282" width="56" height="9"  fill="#A07030" opacity="0.28"/>',
    '<rect x="344" y="304" width="56" height="9"  fill="#A07030" opacity="0.28"/>',
    '<rect x="344" y="326" width="56" height="9"  fill="#A07030" opacity="0.26"/>',
    '<rect x="344" y="350" width="56" height="9"  fill="#A07030" opacity="0.24"/>',
    '<rect x="344" y="376" width="56" height="9"  fill="#A07030" opacity="0.24"/>',
    '<rect x="368" y="286" width="20" height="28" fill="#2040A0" rx="9" opacity="0.70"/>',
    '<rect x="370" y="288" width="8"  height="24" fill="#4060C0" rx="4" opacity="0.48"/>',
    '<rect x="378" y="288" width="8"  height="24" fill="#3858B8" rx="4" opacity="0.38"/>',
    '<rect x="344" y="240" width="56" height="14" fill="#9A7240" rx="1"/>',
    '<rect x="346" y="232" width="10" height="10" fill="#9A7240" rx="1"/>',
    '<rect x="362" y="232" width="10" height="10" fill="#9A7240" rx="1"/>',
    '<rect x="378" y="232" width="10" height="10" fill="#9A7240" rx="1"/>',

    # Rope + barrels on dock
    '<path d="M64,442 Q100,438 136,442" stroke="#7A5028" stroke-width="3.0" fill="none" stroke-linecap="round"/>',
    '<path d="M64,444 Q100,440 136,444" stroke="#5A3818" stroke-width="1.5" fill="none" stroke-linecap="round" opacity="0.50"/>',
    '<ellipse cx="86"  cy="458" rx="13" ry="10" fill="#6A4018"/>',
    '<ellipse cx="86"  cy="448" rx="13" ry="4"  fill="#7A5020"/>',
    '<ellipse cx="86"  cy="468" rx="13" ry="4"  fill="#7A5020"/>',
    '<rect    x="74"   y="448"  width="4" height="20" fill="#905E28" opacity="0.55"/>',
    '<ellipse cx="108" cy="462" rx="11" ry="9"  fill="#6A4018"/>',
    '<ellipse cx="108" cy="453" rx="11" ry="3.5" fill="#7A5020"/>',
    '<ellipse cx="108" cy="471" rx="11" ry="3.5" fill="#7A5020"/>',
    '<rect    x="97"   y="453"  width="4" height="18" fill="#905E28" opacity="0.52"/>',

    # Rope coil right side
    '<path d="M270,448 Q300,444 330,448" stroke="#7A5028" stroke-width="2.8" fill="none" stroke-linecap="round"/>',
    '<ellipse cx="288" cy="462" rx="12" ry="9"  fill="#6A4018"/>',
    '<ellipse cx="288" cy="453" rx="12" ry="3.5" fill="#7A5020"/>',
    '<ellipse cx="288" cy="471" rx="12" ry="3.5" fill="#7A5020"/>',
    '<rect    x="277"  y="453"  width="4" height="18" fill="#905E28" opacity="0.50"/>',

    # ══════════════════════════════════════════════════════════════════
    #  STAGE 5 SPECIAL: 錨と舵輪  Anchor + Ship Wheel  (x=200+52, y≈235)
    # ══════════════════════════════════════════════════════════════════
    '<g transform="translate(52,0)">',
    # Stone pedestal base
    '<rect    x="184" y="280" width="32" height="12" fill="#8A6838" rx="3"/>',
    '<ellipse cx="200" cy="280" rx="16"  ry="4.5"   fill="#9A7848"/>',
    # Anchor chain loop on floor
    '<ellipse cx="200" cy="294" rx="18"  ry="5"     fill="none" stroke="#604820" stroke-width="3.5" opacity="0.60"/>',
    '<ellipse cx="200" cy="294" rx="18"  ry="5"     fill="none" stroke="#806038" stroke-width="1.5" opacity="0.38"/>',
    # Anchor shaft
    '<rect    x="197" y="222" width="6"  height="60" fill="#4A4848" rx="2"/>',
    '<rect    x="198" y="223" width="2"  height="58" fill="#706868" opacity="0.45"/>',
    # Anchor ring (top)
    '<circle  cx="200" cy="218" r="9"    fill="none" stroke="#4A4848" stroke-width="5.5"/>',
    '<circle  cx="200" cy="218" r="9"    fill="none" stroke="#686868" stroke-width="2.5" opacity="0.50"/>',
    # Anchor crossbar
    '<rect    x="183" y="232" width="34" height="5.5" fill="#4A4848" rx="2"/>',
    '<rect    x="184" y="232" width="12" height="2"  fill="#686868" opacity="0.48"/>',
    # Anchor flukes (bottom)
    '<path d="M197,280 Q182,275 178,268 Q178,260 186,258" stroke="#4A4848" stroke-width="5" fill="none" stroke-linecap="round"/>',
    '<path d="M203,280 Q218,275 222,268 Q222,260 214,258" stroke="#4A4848" stroke-width="5" fill="none" stroke-linecap="round"/>',
    '<path d="M178,268 Q174,262 172,265" stroke="#4A4848" stroke-width="5" fill="none" stroke-linecap="round"/>',
    '<path d="M222,268 Q226,262 228,265" stroke="#4A4848" stroke-width="5" fill="none" stroke-linecap="round"/>',
    '<path d="M178,268 Q174,262 172,265" stroke="#686868" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.48"/>',
    '<path d="M222,268 Q226,262 228,265" stroke="#686868" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.48"/>',
    # Ship's wheel (overlapping anchor)
    '<circle  cx="200" cy="240" r="28"   fill="none" stroke="#7A5028" stroke-width="5.5"/>',
    '<circle  cx="200" cy="240" r="28"   fill="none" stroke="#B08040" stroke-width="2.5" opacity="0.60"/>',
    '<circle  cx="200" cy="240" r="14"   fill="#6A4018"/>',
    '<circle  cx="200" cy="240" r="14"   fill="none" stroke="#A07030" stroke-width="2.5" opacity="0.70"/>',
    '<circle  cx="200" cy="240" r="7"    fill="#8A5820"/>',
    # Spokes (8)
    '<g stroke="#7A5028" stroke-width="3.5" stroke-linecap="round">',
    '<line x1="200" y1="212" x2="200" y2="226"/>',
    '<line x1="200" y1="254" x2="200" y2="268"/>',
    '<line x1="172" y1="240" x2="186" y2="240"/>',
    '<line x1="214" y1="240" x2="228" y2="240"/>',
    '<line x1="180" y1="220" x2="190" y2="230"/>',
    '<line x1="210" y1="250" x2="220" y2="260"/>',
    '<line x1="220" y1="220" x2="210" y2="230"/>',
    '<line x1="180" y1="250" x2="190" y2="260"/>',
    '</g>',
    # Spoke highlight
    '<g stroke="#B08040" stroke-width="1.5" stroke-linecap="round" opacity="0.48">',
    '<line x1="200" y1="212" x2="200" y2="226"/>',
    '<line x1="200" y1="254" x2="200" y2="268"/>',
    '<line x1="172" y1="240" x2="186" y2="240"/>',
    '<line x1="214" y1="240" x2="228" y2="240"/>',
    '</g>',
    # Wheel handle pegs (8)
    '<g fill="#6A4018">',
    '<circle cx="200" cy="210" r="4.5"/>',
    '<circle cx="200" cy="270" r="4.5"/>',
    '<circle cx="170" cy="240" r="4.5"/>',
    '<circle cx="230" cy="240" r="4.5"/>',
    '<circle cx="179" cy="219" r="4.0"/>',
    '<circle cx="221" cy="261" r="4.0"/>',
    '<circle cx="221" cy="219" r="4.0"/>',
    '<circle cx="179" cy="261" r="4.0"/>',
    '</g>',
    '</g>',

    # ── DOCK ACCENT DETAILS ───────────────────────────────────
    # Iron cleat / mooring
    '<rect x="64"  y="338" width="22" height="6" fill="#5A5050" rx="2"/>',
    '<rect x="60"  y="336" width="6"  height="10" fill="#4A4040" rx="1"/>',
    '<rect x="80"  y="336" width="6"  height="10" fill="#4A4040" rx="1"/>',
    '<rect x="316" y="338" width="22" height="6" fill="#5A5050" rx="2"/>',
    '<rect x="312" y="336" width="6"  height="10" fill="#4A4040" rx="1"/>',
    '<rect x="332" y="336" width="6"  height="10" fill="#4A4040" rx="1"/>',

    # ══════════════════════════════════════════════════════════════════
    #  STAGE 10: リムサ正門 Limsan Main Gate  (x=200, y≈531) ×1.5
    # ══════════════════════════════════════════════════════════════════
    '<g transform="translate(200,531) scale(1.5) translate(-200,-531)">',
    # Ground shadow
    '<ellipse cx="200" cy="578" rx="60" ry="12" fill="#3C2808" opacity="0.52"/>',

    # LEFT PILLAR
    '<rect x="150" y="490" width="30" height="82" fill="url(#nGateL)" rx="2"/>',
    # Stone courses
    '<rect x="150" y="497" width="30" height="7"  fill="#886030" opacity="0.40"/>',
    '<rect x="150" y="511" width="30" height="7"  fill="#704E1E" opacity="0.35"/>',
    '<rect x="150" y="525" width="30" height="7"  fill="#886030" opacity="0.38"/>',
    '<rect x="150" y="539" width="30" height="7"  fill="#704E1E" opacity="0.35"/>',
    '<rect x="150" y="553" width="30" height="7"  fill="#886030" opacity="0.36"/>',
    '<rect x="150" y="567" width="30" height="7"  fill="#704E1E" opacity="0.33"/>',
    # Pillar highlight
    '<rect x="152" y="490" width="7"  height="82" fill="#C8A060" opacity="0.20"/>',
    # Pillar cap
    '<rect x="146" y="484" width="38" height="8"  fill="#7A5828" rx="2"/>',
    '<rect x="143" y="480" width="44" height="6"  fill="#8A6830" rx="2"/>',
    # Flame brazier on cap
    '<rect x="160" y="466" width="8"  height="16" fill="#5A3C18" rx="2"/>',
    '<ellipse cx="164" cy="465" rx="7" ry="4.5"   fill="#4A3010"/>',
    '<ellipse cx="164" cy="460" rx="5.5" ry="7.5" fill="#FF8820" opacity="0.88"/>',
    '<ellipse cx="164" cy="456" rx="3.5" ry="5"   fill="#FFB840" opacity="0.82"/>',
    '<ellipse cx="163" cy="453" rx="2.5" ry="3.5" fill="#FFE060" opacity="0.78"/>',

    # RIGHT PILLAR
    '<rect x="220" y="490" width="30" height="82" fill="url(#nGate)" rx="2"/>',
    '<rect x="220" y="497" width="30" height="7"  fill="#886030" opacity="0.40"/>',
    '<rect x="220" y="511" width="30" height="7"  fill="#704E1E" opacity="0.35"/>',
    '<rect x="220" y="525" width="30" height="7"  fill="#886030" opacity="0.38"/>',
    '<rect x="220" y="539" width="30" height="7"  fill="#704E1E" opacity="0.35"/>',
    '<rect x="220" y="553" width="30" height="7"  fill="#886030" opacity="0.36"/>',
    '<rect x="220" y="567" width="30" height="7"  fill="#704E1E" opacity="0.33"/>',
    '<rect x="222" y="490" width="7"  height="82" fill="#C8A060" opacity="0.16"/>',
    '<rect x="214" y="484" width="38" height="8"  fill="#7A5828" rx="2"/>',
    '<rect x="213" y="480" width="44" height="6"  fill="#8A6830" rx="2"/>',
    '<rect x="232" y="466" width="8"  height="16" fill="#5A3C18" rx="2"/>',
    '<ellipse cx="236" cy="465" rx="7"   ry="4.5" fill="#4A3010"/>',
    '<ellipse cx="236" cy="460" rx="5.5" ry="7.5" fill="#FF8820" opacity="0.85"/>',
    '<ellipse cx="236" cy="456" rx="3.5" ry="5"   fill="#FFB840" opacity="0.80"/>',
    '<ellipse cx="235" cy="453" rx="2.5" ry="3.5" fill="#FFE060" opacity="0.75"/>',

    # ARCH (semicircular, Limsan style)
    '<path d="M148,498 Q200,458 252,498" stroke="#5A3C10" stroke-width="20" fill="none" stroke-linecap="butt"/>',
    '<path d="M148,498 Q200,458 252,498" stroke="url(#nGate)" stroke-width="16" fill="none" stroke-linecap="butt"/>',
    '<path d="M150,498 Q200,460 250,498" stroke="#C8A060" stroke-width="4"  fill="none" stroke-linecap="butt" opacity="0.30"/>',
    # Arch stone joints
    '<path d="M170,486 Q174,478 180,474" stroke="#5A3C10" stroke-width="1.5" fill="none" opacity="0.48"/>',
    '<path d="M192,462 Q196,460 200,459" stroke="#5A3C10" stroke-width="1.5" fill="none" opacity="0.45"/>',
    '<path d="M220,486 Q216,478 210,474" stroke="#5A3C10" stroke-width="1.5" fill="none" opacity="0.48"/>',
    # Keystone
    '<polygon points="194,460 200,452 206,460 204,468 196,468" fill="#8A6830"/>',
    '<polygon points="195,461 200,454 205,461 203,467 197,467" fill="#A08040" opacity="0.55"/>',
    # Maelstrom emblem (simplified anchor silhouette on keystone)
    '<circle  cx="200" cy="462" r="3.5" fill="#5A3C10" opacity="0.75"/>',
    '<line x1="200" y1="458" x2="200" y2="466" stroke="#3A2408" stroke-width="1.5" opacity="0.70"/>',

    # Secondary arch / portcullis frame
    '<rect x="152" y="496" width="96" height="6"  fill="#6A4C20" opacity="0.60"/>',
    '<rect x="154" y="497" width="30" height="2"  fill="#A07830" opacity="0.35"/>',

    # Portcullis bars (iron gate)
    '<g stroke="#303030" stroke-width="2.8" opacity="0.50">',
    '<line x1="164" y1="502" x2="164" y2="572"/>',
    '<line x1="178" y1="502" x2="178" y2="572"/>',
    '<line x1="192" y1="502" x2="192" y2="572"/>',
    '<line x1="206" y1="502" x2="206" y2="572"/>',
    '<line x1="220" y1="502" x2="220" y2="572"/>',
    '<line x1="234" y1="502" x2="234" y2="572"/>',
    '</g>',
    '<g stroke="#303030" stroke-width="2" opacity="0.38">',
    '<line x1="152" y1="522" x2="248" y2="522"/>',
    '<line x1="152" y1="542" x2="248" y2="542"/>',
    '<line x1="152" y1="562" x2="248" y2="562"/>',
    '</g>',
    # Portcullis spikes
    '<g fill="#282828" opacity="0.52">',
    '<polygon points="162,572 164,580 166,572"/>',
    '<polygon points="176,572 178,580 180,572"/>',
    '<polygon points="190,572 192,580 194,572"/>',
    '<polygon points="204,572 206,580 208,572"/>',
    '<polygon points="218,572 220,580 222,572"/>',
    '<polygon points="232,572 234,580 236,572"/>',
    '</g>',

    # Maelstrom banner (left)
    '<rect x="134" y="490" width="12" height="22" fill="#A01820" rx="1" opacity="0.82"/>',
    '<polygon points="134,512 140,518 146,512" fill="#A01820" opacity="0.82"/>',
    '<line x1="134" y1="504" x2="146" y2="504" stroke="#D04030" stroke-width="1.2" opacity="0.60"/>',
    # Maelstrom banner (right)
    '<rect x="254" y="490" width="12" height="22" fill="#A01820" rx="1" opacity="0.82"/>',
    '<polygon points="254,512 260,518 266,512" fill="#A01820" opacity="0.82"/>',
    '<line x1="254" y1="504" x2="266" y2="504" stroke="#D04030" stroke-width="1.2" opacity="0.60"/>',

    '</g>',

    # ── CLIFF-TOP VEGETATION ─────────────────────────────────
    # Low scrub on left cliff
    '<ellipse cx="22"  cy="264" rx="24" ry="10" fill="#3A6018" opacity="0.68"/>',
    '<ellipse cx="44"  cy="256" rx="18" ry="8"  fill="#426820" opacity="0.64"/>',
    '<ellipse cx="10"  cy="256" rx="14" ry="6"  fill="#3A5E18" opacity="0.60"/>',
    # Right cliff scrub
    '<ellipse cx="378" cy="252" rx="24" ry="10" fill="#3A6018" opacity="0.66"/>',
    '<ellipse cx="356" cy="244" rx="18" ry="8"  fill="#426820" opacity="0.62"/>',
    '<ellipse cx="390" cy="244" rx="14" ry="6"  fill="#3A5E18" opacity="0.58"/>',

    '</svg>',
)

# ── inject helper ─────────────────────────────────────────────────────
def inject(html, diff, svg_str):
    pattern = rf"(if\(diff==='{diff}'\) return ')(.*?)(';)"
    def replacer(m):
        return m.group(1) + svg_str + m.group(3)
    new_html = re.sub(pattern, replacer, html, flags=re.DOTALL)
    return new_html

content = inject(content, 'NORMAL', NORMAL)

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('NORMAL injected OK —', len(NORMAL), 'chars')
