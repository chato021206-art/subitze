#!/usr/bin/env python3
"""EXTREME SVG masterpiece - Night Forest with Moonlight. Bright enough to see."""
import re

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

def J(*parts):
    return ''.join(parts)

# ═══════════════════════════════════════════════════════════════════════
#  EXTREME  月夜の森  Moonlit Night Forest  — MASTERPIECE
#  ・道なし（全幅を夜の自然で覆う）
#  ・月＋月光、星空、木のシルエット（月光エッジ）、発光キノコ、蛍
#  ・Stage5 (y≈235, x=200): 大きな篝火（ボンファイア）
#  ・Stage10 (y≈531, x=200): 古代石祭壇（ルーン文字＋紫の光）
# ═══════════════════════════════════════════════════════════════════════

EXTREME = J(
    '<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">',
    '<defs>',

    # Sky — deep navy night
    '<linearGradient id="xSky" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#040818"/>',
    '<stop offset="35%" stop-color="#080C20"/>',
    '<stop offset="68%" stop-color="#0C1628"/>',
    '<stop offset="100%" stop-color="#101E28"/>',
    '</linearGradient>',

    # Ground — dark forest floor with moonlit tint
    '<linearGradient id="xGnd" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#1A3028"/>',
    '<stop offset="40%" stop-color="#122418"/>',
    '<stop offset="100%" stop-color="#0A1610"/>',
    '</linearGradient>',

    # Moon glow — large radial from upper-right
    '<radialGradient id="xMoon" cx="78%" cy="8%" r="55%">',
    '<stop offset="0%" stop-color="#EEF4FF" stop-opacity="0.72"/>',
    '<stop offset="18%" stop-color="#C8DCFF" stop-opacity="0.45"/>',
    '<stop offset="42%" stop-color="#A0C0F8" stop-opacity="0.18"/>',
    '<stop offset="70%" stop-color="#8090D8" stop-opacity="0.06"/>',
    '<stop offset="100%" stop-color="#6070C0" stop-opacity="0"/>',
    '</radialGradient>',

    # Ground moonlit center glow
    '<radialGradient id="xMoonGnd" cx="68%" cy="15%" r="70%">',
    '<stop offset="0%" stop-color="#B8D4FF" stop-opacity="0.22"/>',
    '<stop offset="55%" stop-color="#8090D0" stop-opacity="0.08"/>',
    '<stop offset="100%" stop-color="#8090D0" stop-opacity="0"/>',
    '</radialGradient>',

    # Bonfire glow (stage 5)
    '<radialGradient id="xBfire" cx="50%" cy="60%" r="50%">',
    '<stop offset="0%" stop-color="#FF9020" stop-opacity="0.90"/>',
    '<stop offset="35%" stop-color="#FF5800" stop-opacity="0.50"/>',
    '<stop offset="65%" stop-color="#FF3000" stop-opacity="0.20"/>',
    '<stop offset="100%" stop-color="#FF2000" stop-opacity="0"/>',
    '</radialGradient>',

    # Altar glow (stage 10 — purple)
    '<radialGradient id="xAltar" cx="50%" cy="40%" r="55%">',
    '<stop offset="0%" stop-color="#C060FF" stop-opacity="0.85"/>',
    '<stop offset="35%" stop-color="#8030D0" stop-opacity="0.45"/>',
    '<stop offset="65%" stop-color="#6020A0" stop-opacity="0.18"/>',
    '<stop offset="100%" stop-color="#400080" stop-opacity="0"/>',
    '</radialGradient>',

    # Ground mist
    '<linearGradient id="xMist" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#6090A8" stop-opacity="0"/>',
    '<stop offset="55%" stop-color="#6090A8" stop-opacity="0.08"/>',
    '<stop offset="100%" stop-color="#6090A8" stop-opacity="0.22"/>',
    '</linearGradient>',

    # Depth overlay (top)
    '<linearGradient id="xDpth" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#020608" stop-opacity="0.80"/>',
    '<stop offset="18%" stop-color="#020608" stop-opacity="0.06"/>',
    '<stop offset="100%" stop-color="#020608" stop-opacity="0"/>',
    '</linearGradient>',

    # Pine tree (moonlit edge)
    '<linearGradient id="xPine" x1="0" y1="0" x2="1" y2="0">',
    '<stop offset="0%" stop-color="#040E08"/>',
    '<stop offset="60%" stop-color="#081608"/>',
    '<stop offset="85%" stop-color="#1C3828"/>',
    '<stop offset="100%" stop-color="#2C5040"/>',
    '</linearGradient>',

    # Stone gradient for altar
    '<linearGradient id="xStone" x1="0" y1="0" x2="1" y2="1">',
    '<stop offset="0%" stop-color="#504858"/>',
    '<stop offset="55%" stop-color="#302830"/>',
    '<stop offset="100%" stop-color="#201820"/>',
    '</linearGradient>',

    '</defs>',

    # ── BASE ──────────────────────────────────────────────────────────
    '<rect width="400" height="600" fill="url(#xSky)"/>',
    '<rect y="105" width="400" height="495" fill="url(#xGnd)"/>',

    # ── STARS ─────────────────────────────────────────────────────────
    # Bright stars
    '<circle cx="22"  cy="12"  r="1.4" fill="#FFFFFF" opacity="0.92"/>',
    '<circle cx="58"  cy="6"   r="1.6" fill="#FFFFFF" opacity="0.90"/>',
    '<circle cx="96"  cy="18"  r="1.2" fill="#EEF4FF" opacity="0.86"/>',
    '<circle cx="130" cy="8"   r="1.4" fill="#FFFFFF" opacity="0.90"/>',
    '<circle cx="168" cy="20"  r="1.0" fill="#E8F0FF" opacity="0.82"/>',
    '<circle cx="210" cy="10"  r="1.6" fill="#FFFFFF" opacity="0.88"/>',
    '<circle cx="246" cy="24"  r="1.2" fill="#EEF4FF" opacity="0.85"/>',
    '<circle cx="148" cy="38"  r="1.0" fill="#E8F0FF" opacity="0.78"/>',
    '<circle cx="36"  cy="42"  r="1.2" fill="#FFFFFF" opacity="0.82"/>',
    '<circle cx="78"  cy="50"  r="1.0" fill="#E8F0FF" opacity="0.78"/>',
    '<circle cx="112" cy="55"  r="1.2" fill="#FFFFFF" opacity="0.80"/>',
    '<circle cx="185" cy="48"  r="1.0" fill="#E8F0FF" opacity="0.76"/>',
    '<circle cx="64"  cy="30"  r="0.8" fill="#FFFFFF" opacity="0.75"/>',
    '<circle cx="176" cy="32"  r="0.8" fill="#FFFFFF" opacity="0.74"/>',
    '<circle cx="52"  cy="62"  r="0.8" fill="#EEF4FF" opacity="0.70"/>',
    '<circle cx="140" cy="62"  r="0.9" fill="#FFFFFF" opacity="0.72"/>',
    # Tiny dim stars
    '<circle cx="18"  cy="52"  r="0.6" fill="#C8D8FF" opacity="0.62"/>',
    '<circle cx="88"  cy="38"  r="0.6" fill="#C8D8FF" opacity="0.60"/>',
    '<circle cx="156" cy="14"  r="0.6" fill="#C8D8FF" opacity="0.62"/>',
    '<circle cx="200" cy="40"  r="0.5" fill="#C8D8FF" opacity="0.58"/>',
    '<circle cx="225" cy="12"  r="0.5" fill="#C8D8FF" opacity="0.58"/>',

    # ── MOON (upper-right, full moon) ────────────────────────────────
    # Moon outer glow
    '<circle cx="316" cy="46"  r="42" fill="#C8DCFF" opacity="0.12"/>',
    '<circle cx="316" cy="46"  r="30" fill="#D8E8FF" opacity="0.22"/>',
    '<circle cx="316" cy="46"  r="22" fill="#E8F0FF" opacity="0.35"/>',
    # Moon disc
    '<circle cx="316" cy="46"  r="18" fill="#EEF6FF" opacity="0.92"/>',
    '<circle cx="316" cy="46"  r="16" fill="#F6FAFF"/>',
    # Moon craters (subtle)
    '<circle cx="310" cy="40"  r="3.5" fill="#E0ECFF" opacity="0.55"/>',
    '<circle cx="322" cy="52"  r="2.5" fill="#E0ECFF" opacity="0.48"/>',
    '<circle cx="318" cy="38"  r="2"   fill="#E0ECFF" opacity="0.42"/>',
    '<circle cx="308" cy="50"  r="2"   fill="#E0ECFF" opacity="0.40"/>',
    # Moon rim highlight
    '<circle cx="313" cy="43"  r="16"  fill="none" stroke="#FFFFFF" stroke-width="1.5" opacity="0.40"/>',

    # ── MOONLIGHT RAYS (shaft from moon downward) ────────────────────
    '<rect width="400" height="600" fill="url(#xMoon)"/>',
    '<rect y="105"  width="400" height="495" fill="url(#xMoonGnd)"/>',

    # ── DEPTH OVERLAY ────────────────────────────────────────────────
    '<rect width="400" height="600" fill="url(#xDpth)"/>',

    # ── ROLLING DARK HILLS ────────────────────────────────────────────
    '<ellipse cx="55"  cy="135" rx="130" ry="46" fill="#122A1C" opacity="0.85"/>',
    '<ellipse cx="215" cy="127" rx="155" ry="52" fill="#0E2418" opacity="0.80"/>',
    '<ellipse cx="372" cy="137" rx="132" ry="44" fill="#122A1C" opacity="0.82"/>',
    # Moonlit hill tops (bright edge)
    '<ellipse cx="215" cy="116" rx="155" ry="14" fill="#3A6858" opacity="0.30"/>',
    '<ellipse cx="372" cy="124" rx="132" ry="12" fill="#3A6858" opacity="0.25"/>',

    # ── LAYER 2: HORIZON PINE SILHOUETTES ────────────────────────────
    '<polygon points="8,106  14,84  20,106"  fill="#040C06" opacity="0.95"/>',
    '<polygon points="18,108 25,82  32,108"  fill="#060E08" opacity="0.93"/>',
    '<polygon points="30,106 38,80  46,106"  fill="#040C06" opacity="0.95"/>',
    # Moonlit right edges
    '<polygon points="44,106 52,78  54,106"  fill="#0E2818" opacity="0.88"/>',
    '<polygon points="86,108 93,82  100,108" fill="#040C06" opacity="0.93"/>',
    '<polygon points="98,106 106,79 114,106" fill="#060E08" opacity="0.91"/>',
    '<polygon points="168,108 175,82 182,108" fill="#040C06" opacity="0.93"/>',
    '<polygon points="248,108 255,80 262,108" fill="#040C06" opacity="0.93"/>',
    '<polygon points="262,106 270,78 278,106" fill="#0E2818" opacity="0.88"/>',
    '<polygon points="330,108 337,82 344,108" fill="#040C06" opacity="0.93"/>',
    '<polygon points="350,106 358,80 366,106" fill="#060E08" opacity="0.91"/>',
    '<polygon points="372,108 380,82 388,108" fill="#040C06" opacity="0.95"/>',

    # ── LAYER 3: FAR TREES (moonlit right edges) ──────────────────────
    # Far-left pines (moonlight catches right side)
    '<polygon points="0,142  14,100 28,142"  fill="#040E08" opacity="0.96"/>',
    '<polygon points="22,140 38,96  54,140"  fill="#081408" opacity="0.94"/>',
    # Moonlit edges on right side of pines
    '<polygon points="26,140 38,96  40,140"  fill="#1C4030" opacity="0.40"/>',
    '<polygon points="52,140 66,98  68,140"  fill="#1A3C2C" opacity="0.35"/>',
    # Far-left deciduous
    '<rect x="56"  y="122" width="2.5" height="34" fill="#040A06"/>',
    '<ellipse cx="57.25" cy="118" rx="12" ry="11" fill="#0E2414" opacity="0.95"/>',
    '<ellipse cx="57.25" cy="109" rx="9"  ry="8"  fill="#142C1A" opacity="0.92"/>',
    # Moonlit right edge of deciduous
    '<ellipse cx="63"   cy="116" rx="5"  ry="9"  fill="#2A5040" opacity="0.28"/>',
    # Center-left pines
    '<polygon points="76,144  90,100 104,144" fill="#040E08" opacity="0.94"/>',
    '<polygon points="102,140 118,96 134,140" fill="#081408" opacity="0.92"/>',
    '<polygon points="130,140 134,96 136,140" fill="#1C4030" opacity="0.36"/>',
    # Center deciduous
    '<rect x="142" y="120" width="2.4" height="36" fill="#040A06"/>',
    '<ellipse cx="143.2" cy="116" rx="13" ry="11" fill="#0E2414" opacity="0.95"/>',
    '<ellipse cx="143.2" cy="107" rx="9.5" ry="7.5" fill="#142C1A" opacity="0.92"/>',
    '<ellipse cx="150"   cy="114" rx="5"  ry="9"  fill="#2A5040" opacity="0.26"/>',
    # Center-right pines
    '<polygon points="228,144 244,100 260,144" fill="#040E08" opacity="0.94"/>',
    '<polygon points="258,140 274,96  290,140" fill="#081408" opacity="0.92"/>',
    '<polygon points="288,140 292,96  294,140" fill="#1C4030" opacity="0.36"/>',
    # Right deciduous
    '<rect x="294" y="120" width="2.4" height="36" fill="#040A06"/>',
    '<ellipse cx="295.2" cy="116" rx="13" ry="11" fill="#0E2414" opacity="0.95"/>',
    '<ellipse cx="295.2" cy="107" rx="9.5" ry="7.5" fill="#142C1A" opacity="0.92"/>',
    '<ellipse cx="302"   cy="114" rx="5"  ry="9"  fill="#2A5040" opacity="0.26"/>',
    # Far-right pines
    '<polygon points="314,142 330,100 346,142" fill="#040E08" opacity="0.96"/>',
    '<polygon points="342,140 358,96  374,140" fill="#081408" opacity="0.94"/>',
    '<polygon points="372,142 386,98  400,142" fill="#040E08" opacity="0.96"/>',
    '<polygon points="370,140 386,96  388,140" fill="#1C4030" opacity="0.38"/>',

    # ── LAYER 4: MID FOREST TREES ─────────────────────────────────────
    # Left large pines (moonlit right edges)
    '<polygon points="-8,236  14,164 36,236"  fill="url(#xPine)" opacity="0.98"/>',
    '<rect x="11"  y="226" width="6" height="36" fill="#030806"/>',
    '<polygon points="28,232  52,158 76,232"  fill="#040E08"    opacity="0.96"/>',
    '<rect x="49"  y="222" width="6" height="40" fill="#030806"/>',
    # Moonlit right edges of left pines
    '<polygon points="34,232 36,158 38,232" fill="#2A5040" opacity="0.32"/>',
    '<polygon points="74,232 76,158 78,232" fill="#2A5040" opacity="0.30"/>',
    # Left deciduous (near-mid)
    '<rect x="98"  y="190" width="5.5" height="58" fill="#030806"/>',
    '<ellipse cx="100.75" cy="182" rx="22" ry="17" fill="#102418" opacity="0.97"/>',
    '<ellipse cx="100.75" cy="168" rx="15" ry="12" fill="#183020" opacity="0.95"/>',
    '<ellipse cx="100.75" cy="157" rx="10" ry="8"  fill="#204028" opacity="0.92"/>',
    # Moonlit right edges
    '<ellipse cx="110"    cy="180" rx="8"  ry="14" fill="#2A5040" opacity="0.24"/>',
    # Right deciduous
    '<rect x="294" y="190" width="5.5" height="58" fill="#030806"/>',
    '<ellipse cx="296.75" cy="182" rx="22" ry="17" fill="#102418" opacity="0.97"/>',
    '<ellipse cx="296.75" cy="168" rx="15" ry="12" fill="#183020" opacity="0.95"/>',
    '<ellipse cx="296.75" cy="157" rx="10" ry="8"  fill="#204028" opacity="0.92"/>',
    '<ellipse cx="306"    cy="180" rx="8"  ry="14" fill="#2A5040" opacity="0.24"/>',
    # Right large pines
    '<polygon points="322,236 344,164 366,236" fill="url(#xPine)" opacity="0.98"/>',
    '<rect x="341" y="226" width="6" height="36" fill="#030806"/>',
    '<polygon points="360,232 384,158 408,232" fill="#040E08"    opacity="0.96"/>',
    '<polygon points="362,232 366,158 368,232" fill="#2A5040" opacity="0.30"/>',

    # ── GLOWING MUSHROOMS ────────────────────────────────────────────
    # Left side — teal glow
    '<ellipse cx="56"  cy="360" rx="8"  ry="4"  fill="#20B8A0" opacity="0.92"/>',
    '<rect    x="53"  y="360"  width="6" height="11" fill="#189080" opacity="0.88"/>',
    '<ellipse cx="56"  cy="360" rx="4.5" ry="1.8" fill="#80FFE8" opacity="0.55"/>',
    '<ellipse cx="56"  cy="364" rx="14" ry="9"   fill="#20D0B0" opacity="0.22"/>',
    '<ellipse cx="56"  cy="368" rx="20" ry="12"  fill="#10A890" opacity="0.12"/>',
    # Small companion
    '<ellipse cx="70"  cy="368" rx="5"  ry="2.5" fill="#20B8A0" opacity="0.82"/>',
    '<rect    x="68"  y="368"  width="4" height="8"  fill="#189080" opacity="0.78"/>',
    '<ellipse cx="70"  cy="368" rx="3"  ry="1.2" fill="#80FFE8" opacity="0.45"/>',

    # Right side — purple glow
    '<ellipse cx="340" cy="420" rx="8"  ry="4"  fill="#A040D0" opacity="0.92"/>',
    '<rect    x="337" y="420"  width="6" height="11" fill="#7828A0" opacity="0.88"/>',
    '<ellipse cx="340" cy="420" rx="4.5" ry="1.8" fill="#E090FF" opacity="0.55"/>',
    '<ellipse cx="340" cy="424" rx="14" ry="9"   fill="#A040D0" opacity="0.22"/>',
    '<ellipse cx="340" cy="428" rx="20" ry="12"  fill="#8020B0" opacity="0.12"/>',
    # Small companion
    '<ellipse cx="326" cy="428" rx="5"  ry="2.5" fill="#A040D0" opacity="0.82"/>',
    '<rect    x="324" y="428"  width="4" height="8"  fill="#7828A0" opacity="0.78"/>',
    '<ellipse cx="326" cy="428" rx="3"  ry="1.2" fill="#E090FF" opacity="0.45"/>',

    # Left lower mushroom (orange glow)
    '<ellipse cx="78"  cy="488" rx="7"  ry="3.5" fill="#D06020" opacity="0.90"/>',
    '<rect    x="75"  y="488"  width="5.5" height="10" fill="#A04010" opacity="0.86"/>',
    '<ellipse cx="78"  cy="488" rx="4"  ry="1.5" fill="#FFA060" opacity="0.50"/>',
    '<ellipse cx="78"  cy="492" rx="12" ry="8"   fill="#D06020" opacity="0.20"/>',

    # ── FIREFLIES (glowing dots) ──────────────────────────────────────
    '<circle cx="134" cy="310" r="2"   fill="#D0FF60" opacity="0.82"/>',
    '<circle cx="134" cy="310" r="4.5" fill="#A0E040" opacity="0.20"/>',
    '<circle cx="280" cy="340" r="2"   fill="#D0FF60" opacity="0.80"/>',
    '<circle cx="280" cy="340" r="4"   fill="#A0E040" opacity="0.18"/>',
    '<circle cx="88"  cy="460" r="1.8" fill="#C8FF50" opacity="0.78"/>',
    '<circle cx="88"  cy="460" r="4"   fill="#90D030" opacity="0.18"/>',
    '<circle cx="320" cy="480" r="2"   fill="#D0FF60" opacity="0.80"/>',
    '<circle cx="320" cy="480" r="4"   fill="#A0E040" opacity="0.18"/>',
    '<circle cx="160" cy="380" r="1.8" fill="#C8FF50" opacity="0.76"/>',
    '<circle cx="248" cy="420" r="1.8" fill="#D0FF60" opacity="0.76"/>',
    '<circle cx="58"  cy="540" r="1.8" fill="#C8FF50" opacity="0.72"/>',
    '<circle cx="342" cy="550" r="1.8" fill="#D0FF60" opacity="0.72"/>',

    # ══════════════════════════════════════════════════════════════════
    #  STAGE 5 SPECIAL: 大篝火  Giant Bonfire  (右側 x≈252, y≈235)
    # ══════════════════════════════════════════════════════════════════
    '<g transform="translate(52,0)">',
    # Wide ground glow circle
    '<ellipse cx="200" cy="268" rx="72" ry="36" fill="#FF6010" opacity="0.16"/>',
    '<ellipse cx="200" cy="268" rx="52" ry="25" fill="#FF7020" opacity="0.22"/>',
    '<ellipse cx="200" cy="270" rx="34" ry="16" fill="#FF8030" opacity="0.28"/>',
    # Log structure (3 large crossed logs)
    '<rect x="168" y="260" width="64" height="9" fill="#2E1608" rx="4" transform="rotate(-22,200,264)"/>',
    '<rect x="168" y="260" width="64" height="9" fill="#2E1608" rx="4" transform="rotate(22,200,264)"/>',
    '<rect x="168" y="258" width="64" height="9" fill="#241208" rx="4"/>',
    '<rect x="175" y="258" width="64" height="9" fill="#382010" rx="4" transform="rotate(-12,207,262)" opacity="0.70"/>',
    # Log texture
    '<path d="M172,267 Q183,264 195,265" stroke="#4A2810" stroke-width="1.0" fill="none" opacity="0.55"/>',
    '<path d="M205,265 Q217,264 228,267" stroke="#4A2810" stroke-width="1.0" fill="none" opacity="0.55"/>',
    # Ember bed
    '<ellipse cx="200" cy="270" rx="24" ry="6"  fill="#FF3800" opacity="0.80"/>',
    '<ellipse cx="200" cy="270" rx="16" ry="4"  fill="#FF6010" opacity="0.88"/>',
    '<ellipse cx="200" cy="270" rx="9"  ry="2.5" fill="#FF9020" opacity="0.92"/>',
    # Embers
    '<circle cx="194" cy="266" r="1.8" fill="#FF8020" opacity="0.92"/>',
    '<circle cx="205" cy="265" r="1.8" fill="#FFA030" opacity="0.90"/>',
    '<circle cx="200" cy="262" r="1.5" fill="#FFB040" opacity="0.88"/>',
    '<circle cx="190" cy="261" r="1.2" fill="#FF6010" opacity="0.84"/>',
    '<circle cx="210" cy="261" r="1.2" fill="#FF6010" opacity="0.84"/>',
    '<circle cx="197" cy="258" r="1"   fill="#FFC050" opacity="0.80"/>',
    '<circle cx="204" cy="258" r="1"   fill="#FFC050" opacity="0.80"/>',
    # Flames — back (dark red-orange, widest)
    '<path d="M185,263 Q178,248 186,234 Q190,220 182,206 Q190,218 196,232 Q198,216 193,200 Q202,215 200,234 Q204,216 200,200 Q208,216 206,232 Q208,218 215,204 Q212,220 210,234 Q216,220 214,206 Q218,218 216,232 Q222,248 215,263" fill="#CC2800" opacity="0.85"/>',
    # Flames — mid (orange)
    '<path d="M188,263 Q182,248 190,234 Q194,220 188,208 Q196,220 198,236 Q201,220 198,206 Q206,220 204,236 Q206,220 212,206 Q210,220 208,236 Q214,248 210,263" fill="#FF5000" opacity="0.90"/>',
    # Flames — front (bright orange)
    '<path d="M192,263 Q186,248 194,236 Q198,224 194,212 Q202,224 201,240 Q205,226 202,212 Q210,226 207,240 Q210,250 208,263" fill="#FF8020" opacity="0.88"/>',
    # Flames — inner bright
    '<path d="M196,263 Q190,248 197,238 Q201,228 198,218 Q204,228 202,242 Q206,232 204,220 Q210,232 207,244 Q210,252 207,263" fill="#FFAA30" opacity="0.84"/>',
    # Flame tips (yellow-white)
    '<path d="M199,254 Q197,242 200,232 Q203,242 201,254" fill="#FFD840" opacity="0.85"/>',
    '<path d="M200,248 Q198,238 201,230 Q203,238 202,248" fill="#FFF060" opacity="0.80"/>',
    '<path d="M200,242 Q199,234 201,228 Q202,234 202,242" fill="#FFFFFF"  opacity="0.60"/>',
    # Sparks flying up
    '<circle cx="194" cy="224" r="1.5" fill="#FFE060" opacity="0.84"/>',
    '<circle cx="207" cy="220" r="1.2" fill="#FFE060" opacity="0.80"/>',
    '<circle cx="199" cy="214" r="1.5" fill="#FFD040" opacity="0.82"/>',
    '<circle cx="192" cy="210" r="1.0" fill="#FFB030" opacity="0.76"/>',
    '<circle cx="210" cy="206" r="1.0" fill="#FFB030" opacity="0.74"/>',
    '<circle cx="200" cy="202" r="1.2" fill="#FFE060" opacity="0.78"/>',
    '<circle cx="196" cy="195" r="0.9" fill="#FFC040" opacity="0.68"/>',
    '<circle cx="205" cy="192" r="0.9" fill="#FFC040" opacity="0.66"/>',
    # Smoke (dark, curling)
    '<path d="M200,205 Q194,192 198,178 Q204,164 200,150" stroke="#1A2018" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.55"/>',
    '<path d="M200,205 Q206,190 204,174 Q202,160 206,148" stroke="#1A2018" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.38"/>',
    '<path d="M200,205 Q196,188 202,170" stroke="#242820" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.28"/>',
    # Stones around fire (moonlit)
    '<ellipse cx="180" cy="273" rx="7.5" ry="4"  fill="#404048"/>',
    '<ellipse cx="200" cy="277" rx="7"   ry="3.5" fill="#484850"/>',
    '<ellipse cx="220" cy="273" rx="7.5" ry="4"  fill="#404048"/>',
    '<ellipse cx="188" cy="275" rx="5"   ry="3"  fill="#383840"/>',
    '<ellipse cx="213" cy="275" rx="5"   ry="3"  fill="#383840"/>',
    # Stone moonlit edges
    '<ellipse cx="222" cy="272" rx="3"   ry="2"  fill="#7090A0" opacity="0.35"/>',
    '<ellipse cx="201" cy="275" rx="3"   ry="1.5" fill="#7090A0" opacity="0.30"/>',
    # Ground lit by bonfire
    '<ellipse cx="200" cy="286" rx="55" ry="18" fill="#FF6010" opacity="0.10"/>',
    '</g>',

    # ── LAYER 5: NEAR-MID TREES (large, moonlit) ──────────────────────
    # Far-left pine (giant)
    '<polygon points="-10,360 16,260 42,360"  fill="url(#xPine)" opacity="0.99"/>',
    '<rect x="13"  y="348" width="8" height="78" fill="#020606"/>',
    '<polygon points="40,358 44,260 46,358" fill="#2A5040" opacity="0.30"/>',
    # Second left pine
    '<polygon points="32,356  60,254  88,356"  fill="#040E08" opacity="0.97"/>',
    '<rect x="57"  y="344" width="7" height="82" fill="#020606"/>',
    # Left deciduous (large)
    '<rect x="106" y="308" width="8"  height="108" fill="#020606"/>',
    '<ellipse cx="110"    cy="296" rx="34" ry="26" fill="#0E2218" opacity="0.98"/>',
    '<ellipse cx="110"    cy="275" rx="23" ry="18" fill="#162C20" opacity="0.96"/>',
    '<ellipse cx="110"    cy="260" rx="15" ry="11" fill="#1E3C28" opacity="0.94"/>',
    # Moonlit right edge
    '<ellipse cx="124"    cy="294" rx="10" ry="22" fill="#2A5040" opacity="0.26"/>',
    # Right deciduous (large)
    '<rect x="286" y="308" width="8"  height="108" fill="#020606"/>',
    '<ellipse cx="290"    cy="296" rx="34" ry="26" fill="#0E2218" opacity="0.98"/>',
    '<ellipse cx="290"    cy="275" rx="23" ry="18" fill="#162C20" opacity="0.96"/>',
    '<ellipse cx="290"    cy="260" rx="15" ry="11" fill="#1E3C28" opacity="0.94"/>',
    '<ellipse cx="304"    cy="294" rx="10" ry="22" fill="#2A5040" opacity="0.26"/>',
    # Second right pine
    '<polygon points="310,356 340,254 370,356" fill="#040E08" opacity="0.97"/>',
    '<rect x="337" y="344" width="7" height="82" fill="#020606"/>',
    # Far-right pine (giant)
    '<polygon points="356,360 382,260 408,360" fill="url(#xPine)" opacity="0.99"/>',
    '<rect x="379" y="348" width="8" height="78" fill="#020606"/>',
    '<polygon points="354,358 358,260 360,358" fill="#2A5040" opacity="0.28"/>',

    # ── ROCKS (moonlit) ───────────────────────────────────────────────
    '<ellipse cx="58"  cy="455" rx="18" ry="12" fill="url(#xStone)"/>',
    '<ellipse cx="46"  cy="460" rx="12" ry="8"  fill="#383438"/>',
    '<ellipse cx="70"  cy="462" rx="10" ry="7"  fill="#2C282C"/>',
    # Moonlit top of rocks
    '<ellipse cx="60"  cy="447" rx="10" ry="4"  fill="#608090" opacity="0.30"/>',
    '<ellipse cx="348" cy="468" rx="16" ry="10" fill="url(#xStone)"/>',
    '<ellipse cx="338" cy="473" rx="11" ry="7"  fill="#383438"/>',
    '<ellipse cx="360" cy="474" rx="9"  ry="6"  fill="#2C282C"/>',
    '<ellipse cx="350" cy="460" rx="9"  ry="3.5" fill="#608090" opacity="0.28"/>',

    # ══════════════════════════════════════════════════════════════════
    #  STAGE 10 SPECIAL: 古代石祭壇  Ancient Stone Altar  (x=200, y≈531) ×1.5
    # ══════════════════════════════════════════════════════════════════
    # Scale 1.5× around altar center (200, 530)
    '<g transform="translate(200,530) scale(1.5) translate(-200,-530)">',
    # Wide altar glow (purple radial)
    '<ellipse cx="200" cy="530" rx="70" ry="40" fill="#6020A0" opacity="0.18"/>',
    '<ellipse cx="200" cy="534" rx="50" ry="28" fill="#8030C0" opacity="0.25"/>',
    '<ellipse cx="200" cy="538" rx="32" ry="18" fill="#A040E0" opacity="0.32"/>',
    # Ground glow
    '<ellipse cx="200" cy="558" rx="46" ry="14" fill="#7020B0" opacity="0.20"/>',

    # Outer standing stones (Stonehenge-like)
    '<rect x="156" y="504" width="14" height="48" fill="url(#xStone)" rx="2"/>',
    '<rect x="157" y="504" width="5"  height="48" fill="#504858" opacity="0.35"/>',
    '<rect x="230" y="504" width="14" height="48" fill="url(#xStone)" rx="2"/>',
    '<rect x="231" y="504" width="5"  height="48" fill="#504858" opacity="0.35"/>',
    # Moonlit top edges of outer stones
    '<rect x="156" y="503" width="14" height="3" fill="#8090A8" opacity="0.50"/>',
    '<rect x="230" y="503" width="14" height="3" fill="#8090A8" opacity="0.50"/>',
    # Lintel (horizontal stone across top)
    '<rect x="153" y="500" width="94" height="8" fill="#363038" rx="2"/>',
    '<rect x="154" y="500" width="94" height="3" fill="#686070" opacity="0.40"/>',
    # Inner stones (shorter)
    '<rect x="172" y="514" width="11" height="38" fill="#403840" rx="2"/>',
    '<rect x="217" y="514" width="11" height="38" fill="#403840" rx="2"/>',
    # Inner lintel
    '<rect x="169" y="510" width="62" height="7" fill="#302830" rx="2"/>',
    '<rect x="170" y="510" width="62" height="2.5" fill="#585060" opacity="0.38"/>',

    # Altar stone (flat slab in center)
    '<rect x="182" y="534" width="36" height="10" fill="#3A3040" rx="2"/>',
    '<rect x="183" y="534" width="36" height="3"  fill="#605860" opacity="0.42"/>',
    # Altar glow top surface
    '<rect x="184" y="535" width="32" height="6"  fill="#C060FF" opacity="0.28"/>',
    '<rect x="188" y="536" width="24" height="4"  fill="#D880FF" opacity="0.22"/>',

    # Rune markings on altar (glowing)
    '<path d="M192,538 L192,542 M190,540 L194,540" stroke="#C060FF" stroke-width="1.5" opacity="0.90"/>',
    '<path d="M200,537 L200,543 M198,538 L202,540 M198,542 L202,540" stroke="#C060FF" stroke-width="1.5" opacity="0.90"/>',
    '<path d="M208,538 L208,542 M206,539 L210,541 M206,541 L210,539" stroke="#C060FF" stroke-width="1.5" opacity="0.90"/>',
    # Rune markings on inner lintel
    '<path d="M185,513 L185,516 M183,514.5 L187,514.5" stroke="#A040E0" stroke-width="1.2" opacity="0.80"/>',
    '<path d="M200,512 L200,517 M198,513 L202,515 M198,516 L202,514" stroke="#A040E0" stroke-width="1.2" opacity="0.80"/>',
    '<path d="M215,513 L215,516 M213,514.5 L217,514.5" stroke="#A040E0" stroke-width="1.2" opacity="0.80"/>',

    # Stone surface cracks (weathered)
    '<path d="M160,518 Q164,522 162,528" stroke="#202020" stroke-width="1.0" fill="none" opacity="0.60"/>',
    '<path d="M232,520 Q236,524 234,530" stroke="#202020" stroke-width="1.0" fill="none" opacity="0.60"/>',
    '<path d="M186,540 Q190,538 194,540" stroke="#202020" stroke-width="0.8" fill="none" opacity="0.55"/>',

    # Floating rune orbs (mystical glow above altar)
    '<circle cx="186" cy="526" r="3.5" fill="#D060FF" opacity="0.80"/>',
    '<circle cx="186" cy="526" r="6"   fill="#A030E0" opacity="0.30"/>',
    '<circle cx="200" cy="520" r="4.5" fill="#E080FF" opacity="0.85"/>',
    '<circle cx="200" cy="520" r="9"   fill="#B040F0" opacity="0.28"/>',
    '<circle cx="214" cy="526" r="3.5" fill="#D060FF" opacity="0.80"/>',
    '<circle cx="214" cy="526" r="6"   fill="#A030E0" opacity="0.30"/>',

    # Altar base ground
    '<ellipse cx="200" cy="553" rx="40" ry="8" fill="#200A30" opacity="0.60"/>',
    # Altar base stones
    '<rect x="175" y="548" width="50" height="8" fill="#2A2030" rx="2"/>',
    '<rect x="172" y="554" width="56" height="5" fill="#201828" rx="2"/>',
    '</g>',

    # ── GROUND MIST OVERLAY ───────────────────────────────────────────
    '<rect y="490" width="400" height="110" fill="url(#xMist)" opacity="0.80"/>',
    '<rect y="555" width="400" height="45"  fill="#607090" opacity="0.08"/>',

    # ── LAYER 6: FOREGROUND GIANT PINES (moonlit) ─────────────────────
    # Left
    '<polygon points="-14,600 18,448 50,600"  fill="url(#xPine)" opacity="1.0"/>',
    '<polygon points="-2,600  18,468 38,600"  fill="#0A1C10"     opacity="0.90"/>',
    '<rect x="14"  y="580" width="9" height="20" fill="#020406"/>',
    # Moonlit right edge
    '<polygon points="48,600 50,448 54,600" fill="#2A5040" opacity="0.35"/>',
    # Lower skirt
    '<ellipse cx="18"  cy="598" rx="50" ry="18" fill="#081410"/>',
    '<ellipse cx="0"   cy="608" rx="40" ry="14" fill="#060E08"/>',
    # Right
    '<polygon points="350,600 382,448 414,600" fill="url(#xPine)" opacity="1.0"/>',
    '<polygon points="362,600 382,468 402,600" fill="#0A1C10"     opacity="0.90"/>',
    '<rect x="378" y="580" width="9" height="20" fill="#020406"/>',
    '<polygon points="346,600 350,448 352,600" fill="#2A5040" opacity="0.33"/>',
    '<ellipse cx="382" cy="598" rx="50" ry="18" fill="#081410"/>',
    '<ellipse cx="400" cy="608" rx="40" ry="14" fill="#060E08"/>',

    '</svg>',
)

# ── inject helper ─────────────────────────────────────────────────────
def inject(html, diff, svg_str):
    pattern = rf"(if\(diff==='{diff}'\) return ')(.*?)(';)"
    def replacer(m):
        return m.group(1) + svg_str + m.group(3)
    new_html = re.sub(pattern, replacer, html, flags=re.DOTALL)
    return new_html

content = inject(content, 'EXTREME', EXTREME)

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('EXTREME injected OK —', len(EXTREME), 'chars')
