#!/usr/bin/env python3
"""EASY SVG — Gridania-style sacred forest (FF14 inspired). No center path."""
import re

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

def J(*parts):
    return ''.join(parts)

# ═══════════════════════════════════════════════════════════════════════
#  EASY  聖なる森  Gridania-style Sacred Forest  — MASTERPIECE
#  ・The Twelveswood: ancient trees, filtered amber light, elementals
#  ・Massive canopy overhead, mossy roots, glowing teal spirits
#  ・Stage5 (y≈235, x=200+52): 精霊の祠 Spirit Shrine + elemental orb
#  ・Stage10 (y≈531, x=200) ×1.5: グリダニア門 Gridanian Wooden Gate
# ═══════════════════════════════════════════════════════════════════════

EASY = J(
    '<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">',
    '<defs>',

    # Forest atmosphere — warm amber light filtered through dense canopy
    '<linearGradient id="eSky" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#101808"/>',
    '<stop offset="22%" stop-color="#1C2C0C"/>',
    '<stop offset="50%" stop-color="#2C4A14"/>',
    '<stop offset="78%" stop-color="#3A5C1C"/>',
    '<stop offset="100%" stop-color="#4A6C22"/>',
    '</linearGradient>',

    # Central golden light shaft from canopy opening
    '<radialGradient id="eShaft" cx="50%" cy="5%" r="65%">',
    '<stop offset="0%" stop-color="#D8A820" stop-opacity="0.60"/>',
    '<stop offset="30%" stop-color="#C09018" stop-opacity="0.30"/>',
    '<stop offset="65%" stop-color="#907010" stop-opacity="0.10"/>',
    '<stop offset="100%" stop-color="#907010" stop-opacity="0"/>',
    '</radialGradient>',

    # Warm ambient side glow
    '<radialGradient id="eAmb" cx="65%" cy="42%" r="48%">',
    '<stop offset="0%" stop-color="#B89020" stop-opacity="0.18"/>',
    '<stop offset="100%" stop-color="#B89020" stop-opacity="0"/>',
    '</radialGradient>',

    # Ground — dark, rich mossy forest floor
    '<linearGradient id="eGnd" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#284E10"/>',
    '<stop offset="45%" stop-color="#1C3C0C"/>',
    '<stop offset="100%" stop-color="#0C1E06"/>',
    '</linearGradient>',

    # Ancient tree trunk (dark, textured)
    '<linearGradient id="eTrunk" x1="0" y1="0" x2="1" y2="0">',
    '<stop offset="0%" stop-color="#140E04"/>',
    '<stop offset="25%" stop-color="#382210"/>',
    '<stop offset="60%" stop-color="#281808"/>',
    '<stop offset="100%" stop-color="#100804"/>',
    '</linearGradient>',

    # Elemental / spirit glow (teal-cyan)
    '<radialGradient id="eElem" cx="50%" cy="50%" r="50%">',
    '<stop offset="0%" stop-color="#90FFE8" stop-opacity="0.95"/>',
    '<stop offset="38%" stop-color="#40C8A0" stop-opacity="0.75"/>',
    '<stop offset="100%" stop-color="#18A080" stop-opacity="0"/>',
    '</radialGradient>',

    # Wooden gate gradient
    '<linearGradient id="eWood" x1="0" y1="0" x2="1" y2="0">',
    '<stop offset="0%" stop-color="#221408"/>',
    '<stop offset="35%" stop-color="#543A18"/>',
    '<stop offset="75%" stop-color="#3C2810"/>',
    '<stop offset="100%" stop-color="#1A0E04"/>',
    '</linearGradient>',

    # Gate top beam
    '<linearGradient id="eBeam" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#644220"/>',
    '<stop offset="55%" stop-color="#482E10"/>',
    '<stop offset="100%" stop-color="#301C08"/>',
    '</linearGradient>',

    # Ground mist
    '<linearGradient id="eMist" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#3A7028" stop-opacity="0"/>',
    '<stop offset="45%" stop-color="#2E5820" stop-opacity="0.20"/>',
    '<stop offset="100%" stop-color="#1E3C10" stop-opacity="0.42"/>',
    '</linearGradient>',

    # Canopy darkness overlay (top)
    '<linearGradient id="eCanopy" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#080F04" stop-opacity="0.92"/>',
    '<stop offset="38%" stop-color="#0A1406" stop-opacity="0.45"/>',
    '<stop offset="100%" stop-color="#0A1406" stop-opacity="0"/>',
    '</linearGradient>',

    '</defs>',

    # ── BASE FILL ─────────────────────────────────────────────
    '<rect width="400" height="600" fill="url(#eSky)"/>',
    '<rect width="400" height="600" fill="url(#eShaft)"/>',
    '<rect width="400" height="600" fill="url(#eAmb)"/>',
    '<rect x="0" y="375" width="400" height="225" fill="url(#eGnd)"/>',

    # ── CANOPY — dark overhanging branches & leaves ───────────
    '<ellipse cx="50"  cy="-28" rx="105" ry="85" fill="#0A1206" opacity="0.93"/>',
    '<ellipse cx="200" cy="-38" rx="140" ry="78" fill="#0C1608" opacity="0.88"/>',
    '<ellipse cx="355" cy="-22" rx="115" ry="88" fill="#0A1206" opacity="0.91"/>',
    '<ellipse cx="-10" cy="24"  rx="88"  ry="66" fill="#081004" opacity="0.84"/>',
    '<ellipse cx="410" cy="18"  rx="92"  ry="70" fill="#081004" opacity="0.82"/>',
    '<ellipse cx="115" cy="8"   rx="95"  ry="60" fill="#0E1606" opacity="0.80"/>',
    '<ellipse cx="288" cy="4"   rx="100" ry="62" fill="#0E1606" opacity="0.78"/>',
    '<ellipse cx="200" cy="38"  rx="75"  ry="45" fill="#101808" opacity="0.62"/>',
    # Canopy gradient overlay
    '<rect width="400" height="210" fill="url(#eCanopy)"/>',

    # ── VOLUMETRIC LIGHT SHAFTS ───────────────────────────────
    '<polygon points="172,0 228,0 275,330 125,330" fill="#D0A020" opacity="0.055"/>',
    '<polygon points="186,0 214,0 246,260 154,260" fill="#E0B828" opacity="0.048"/>',
    '<polygon points="55,0  95,0  175,400 -15,400" fill="#C09820" opacity="0.038"/>',
    '<polygon points="305,0 345,0 425,400 225,400" fill="#C09820" opacity="0.038"/>',
    '<polygon points="135,0 160,0 220,320  95,320" fill="#C8A020" opacity="0.030"/>',

    # ── FAR BACKGROUND TREES ─────────────────────────────────
    '<rect x="15"  y="110" width="24" height="295" fill="#182808" opacity="0.68"/>',
    '<ellipse cx="27"  cy="98"  rx="40" ry="56" fill="#1C3010" opacity="0.63"/>',
    '<ellipse cx="27"  cy="66"  rx="28" ry="40" fill="#203412" opacity="0.58"/>',

    '<rect x="362" y="108" width="24" height="298" fill="#182808" opacity="0.66"/>',
    '<ellipse cx="374" cy="96"  rx="40" ry="56" fill="#1C3010" opacity="0.61"/>',
    '<ellipse cx="374" cy="64"  rx="28" ry="40" fill="#203412" opacity="0.56"/>',

    '<rect x="52"  y="148" width="15" height="252" fill="#182808" opacity="0.58"/>',
    '<ellipse cx="59"  cy="138" rx="26" ry="36" fill="#1E2E0E" opacity="0.54"/>',

    '<rect x="333" y="145" width="15" height="255" fill="#182808" opacity="0.56"/>',
    '<ellipse cx="340" cy="135" rx="26" ry="36" fill="#1E2E0E" opacity="0.52"/>',

    '<rect x="192" y="158" width="12" height="235" fill="#162408" opacity="0.44"/>',
    '<ellipse cx="198" cy="149" rx="20" ry="28" fill="#1C2C0A" opacity="0.40"/>',

    # ── FLOATING GOLDEN SPORES ───────────────────────────────
    '<circle cx="142" cy="175" r="2.2" fill="#E4C840" opacity="0.72"/>',
    '<circle cx="262" cy="152" r="1.8" fill="#DCC038" opacity="0.68"/>',
    '<circle cx="318" cy="204" r="2.4" fill="#ECD048" opacity="0.62"/>',
    '<circle cx="78"  cy="234" r="1.6" fill="#D4B430" opacity="0.65"/>',
    '<circle cx="188" cy="128" r="2.0" fill="#E4C840" opacity="0.56"/>',
    '<circle cx="348" cy="166" r="1.5" fill="#DCB430" opacity="0.60"/>',
    '<circle cx="108" cy="298" r="1.8" fill="#CCAC28" opacity="0.58"/>',
    '<circle cx="292" cy="278" r="2.0" fill="#D4B430" opacity="0.54"/>',
    '<circle cx="228" cy="338" r="1.4" fill="#CCAC28" opacity="0.50"/>',
    '<circle cx="62"  cy="352" r="1.6" fill="#C8A824" opacity="0.48"/>',
    '<circle cx="355" cy="342" r="1.4" fill="#C8A824" opacity="0.46"/>',

    # ── TEAL ELEMENTAL SPARKS ─────────────────────────────────
    '<circle cx="168" cy="208" r="1.6" fill="#68E8C0" opacity="0.78"/>',
    '<circle cx="244" cy="186" r="1.8" fill="#58D8B0" opacity="0.72"/>',
    '<circle cx="128" cy="338" r="1.4" fill="#48C8A0" opacity="0.68"/>',
    '<circle cx="308" cy="318" r="1.6" fill="#58D8B0" opacity="0.62"/>',
    '<circle cx="202" cy="272" r="1.2" fill="#68E8C0" opacity="0.70"/>',
    '<circle cx="82"  cy="408" r="1.3" fill="#48C0A0" opacity="0.58"/>',
    '<circle cx="330" cy="398" r="1.2" fill="#48C0A0" opacity="0.54"/>',

    # ── MID TREES (detailed, with roots & moss) ───────────────
    # Left mid tree
    '<rect x="102" y="245" width="22" height="205" fill="url(#eTrunk)"/>',
    '<path d="M102,420 Q82,398 62,426 Q82,408 102,432" fill="#1A1006" opacity="0.82"/>',
    '<path d="M124,420 Q148,400 162,424 Q144,410 124,432" fill="#1A1006" opacity="0.76"/>',
    '<path d="M102,460 Q80,442 64,462 Q84,448 102,468" fill="#161004" opacity="0.68"/>',
    '<ellipse cx="113" cy="224" rx="46" ry="58" fill="#1E4410" opacity="0.90"/>',
    '<ellipse cx="113" cy="188" rx="33" ry="42" fill="#26520E" opacity="0.87"/>',
    '<ellipse cx="113" cy="160" rx="22" ry="28" fill="#2C5C12" opacity="0.83"/>',
    '<ellipse cx="113" cy="140" rx="14" ry="18" fill="#326414" opacity="0.76"/>',
    # Moss on trunk
    '<ellipse cx="108" cy="305" rx="13" ry="5"   fill="#1A4C08" opacity="0.68"/>',
    '<ellipse cx="118" cy="340" rx="11" ry="4"   fill="#184808" opacity="0.62"/>',
    '<ellipse cx="106" cy="375" rx="9"  ry="3.5" fill="#184008" opacity="0.56"/>',

    # Right mid tree
    '<rect x="278" y="243" width="22" height="207" fill="url(#eTrunk)"/>',
    '<path d="M278,420 Q258,398 238,426 Q258,408 278,432" fill="#1A1006" opacity="0.80"/>',
    '<path d="M300,420 Q324,400 338,424 Q320,410 300,432" fill="#1A1006" opacity="0.74"/>',
    '<path d="M278,460 Q256,442 240,462 Q260,448 278,468" fill="#161004" opacity="0.66"/>',
    '<ellipse cx="289" cy="222" rx="46" ry="58" fill="#1E4410" opacity="0.88"/>',
    '<ellipse cx="289" cy="186" rx="33" ry="42" fill="#26520E" opacity="0.85"/>',
    '<ellipse cx="289" cy="158" rx="22" ry="28" fill="#2C5C12" opacity="0.81"/>',
    '<ellipse cx="289" cy="138" rx="14" ry="18" fill="#326414" opacity="0.74"/>',
    '<ellipse cx="284" cy="303" rx="13" ry="5"   fill="#1A4C08" opacity="0.66"/>',
    '<ellipse cx="294" cy="338" rx="11" ry="4"   fill="#184808" opacity="0.60"/>',
    '<ellipse cx="282" cy="373" rx="9"  ry="3.5" fill="#184008" opacity="0.54"/>',

    # ── GLOWING MOSS GROUND PATCHES ──────────────────────────
    '<ellipse cx="45"  cy="388" rx="52" ry="16" fill="#224C0E" opacity="0.68"/>',
    '<ellipse cx="158" cy="398" rx="38" ry="11" fill="#1E4A0C" opacity="0.60"/>',
    '<ellipse cx="312" cy="394" rx="42" ry="13" fill="#224C0E" opacity="0.64"/>',
    '<ellipse cx="376" cy="402" rx="36" ry="10" fill="#204A0C" opacity="0.58"/>',
    '<ellipse cx="220" cy="410" rx="28" ry="8"  fill="#1A4208" opacity="0.50"/>',

    # ── FERNS ────────────────────────────────────────────────
    # Left cluster
    '<path d="M28,452 Q8,430 -2,418"  stroke="#284E0E" stroke-width="3.0" fill="none" stroke-linecap="round"/>',
    '<path d="M28,452 Q14,426 4,410"  stroke="#264C0C" stroke-width="2.6" fill="none" stroke-linecap="round"/>',
    '<path d="M28,452 Q36,428 34,412" stroke="#2A5010" stroke-width="2.6" fill="none" stroke-linecap="round"/>',
    '<path d="M28,452 Q44,432 50,418" stroke="#284E0E" stroke-width="2.6" fill="none" stroke-linecap="round"/>',
    '<ellipse cx="-1"  cy="417" rx="9" ry="5.5" fill="#265010" opacity="0.76" transform="rotate(-22,-1,417)"/>',
    '<ellipse cx="34"  cy="410" rx="8" ry="5"   fill="#2A5412" opacity="0.72" transform="rotate(10,34,410)"/>',
    '<ellipse cx="51"  cy="416" rx="8" ry="5"   fill="#265010" opacity="0.70" transform="rotate(26,51,416)"/>',

    # Right cluster
    '<path d="M372,450 Q392,428 402,416" stroke="#284E0E" stroke-width="3.0" fill="none" stroke-linecap="round"/>',
    '<path d="M372,450 Q386,424 396,408" stroke="#264C0C" stroke-width="2.6" fill="none" stroke-linecap="round"/>',
    '<path d="M372,450 Q364,426 366,410" stroke="#2A5010" stroke-width="2.6" fill="none" stroke-linecap="round"/>',
    '<path d="M372,450 Q356,430 350,416" stroke="#284E0E" stroke-width="2.6" fill="none" stroke-linecap="round"/>',
    '<ellipse cx="403" cy="414" rx="9" ry="5.5" fill="#265010" opacity="0.74" transform="rotate(22,403,414)"/>',
    '<ellipse cx="366" cy="408" rx="8" ry="5"   fill="#2A5412" opacity="0.70" transform="rotate(-10,366,408)"/>',
    '<ellipse cx="348" cy="414" rx="8" ry="5"   fill="#265010" opacity="0.68" transform="rotate(-26,348,414)"/>',

    # Mid ferns
    '<path d="M176,432 Q160,415 148,404" stroke="#285810" stroke-width="2.2" fill="none" stroke-linecap="round"/>',
    '<path d="M176,432 Q180,414 178,402" stroke="#2A5A12" stroke-width="2.2" fill="none" stroke-linecap="round"/>',
    '<path d="M176,432 Q190,416 198,404" stroke="#285810" stroke-width="2.2" fill="none" stroke-linecap="round"/>',
    '<path d="M242,436 Q228,418 218,406" stroke="#285810" stroke-width="2.2" fill="none" stroke-linecap="round"/>',
    '<path d="M242,436 Q254,420 262,408" stroke="#2A5A12" stroke-width="2.2" fill="none" stroke-linecap="round"/>',

    # Small mushrooms
    '<ellipse cx="152" cy="460" rx="5"   ry="2.8" fill="#8A6838" opacity="0.74"/>',
    '<rect    x="154"  y="452"  width="3" height="9"  fill="#6A5028" opacity="0.70"/>',
    '<ellipse cx="258" cy="463" rx="4.5" ry="2.5" fill="#8A6838" opacity="0.70"/>',
    '<rect    x="260"  y="456"  width="3" height="8"  fill="#6A5028" opacity="0.66"/>',

    # ══════════════════════════════════════════════════════════════════
    #  STAGE 5 SPECIAL: 精霊の祠 Spirit Shrine  (x=200+52, y≈235)
    # ══════════════════════════════════════════════════════════════════
    '<g transform="translate(52,0)">',
    # Stone base platform
    '<ellipse cx="200" cy="292" rx="26" ry="7"   fill="#40C8A0" opacity="0.18"/>',
    '<rect    x="182"  y="278"  width="36" height="15" fill="#283C1A" rx="3"/>',
    '<rect    x="179"  y="287"  width="42" height="6"  fill="#1E2E12" rx="2"/>',
    # Stone texture
    '<path d="M184,281 L216,281" stroke="#364C22" stroke-width="0.9" opacity="0.55"/>',
    '<path d="M182,285 L220,285" stroke="#2E4018" stroke-width="0.9" opacity="0.48"/>',
    '<rect x="185" y="280" width="10" height="3" fill="#3A5020" opacity="0.30"/>',
    '<rect x="204" y="283" width="12" height="3" fill="#344818" opacity="0.28"/>',
    # Wooden totem pole
    '<rect x="194" y="238" width="12" height="42" fill="url(#eWood)" rx="3"/>',
    '<rect x="195" y="239" width="4"  height="40" fill="#6A4828" opacity="0.28"/>',
    # Carved markings
    '<path d="M196,250 Q200,246 204,250" stroke="#100802" stroke-width="1.4" fill="none" opacity="0.70"/>',
    '<path d="M196,258 L204,258"         stroke="#100802" stroke-width="1.0" fill="none" opacity="0.60"/>',
    '<path d="M197,265 Q200,268 203,265" stroke="#100802" stroke-width="1.2" fill="none" opacity="0.55"/>',
    # Top ornament cap
    '<ellipse cx="200" cy="237" rx="7"   ry="4.5" fill="#3A2810"/>',
    '<ellipse cx="200" cy="235" rx="5"   ry="3"   fill="#504030"/>',
    '<path d="M196,235 L200,228 L204,235" fill="#2E1E0C" opacity="0.80"/>',
    # Elemental spirit orb (floating, teal glow)
    '<ellipse cx="200" cy="214" rx="22"  ry="22"  fill="url(#eElem)" opacity="0.52"/>',
    '<ellipse cx="200" cy="214" rx="13"  ry="13"  fill="url(#eElem)" opacity="0.65"/>',
    '<circle  cx="200" cy="214" r="8"            fill="#B0FFE8" opacity="0.92"/>',
    '<circle  cx="200" cy="214" r="5"            fill="#D8FFF4" opacity="0.98"/>',
    '<circle  cx="197" cy="211" r="2.2"          fill="#FFFFFF" opacity="0.88"/>',
    # Orbiting sparks
    '<circle cx="190" cy="224" r="2.2" fill="#68E8C0" opacity="0.75"/>',
    '<circle cx="210" cy="220" r="2.0" fill="#58D8B0" opacity="0.70"/>',
    '<circle cx="193" cy="203" r="1.6" fill="#78F0C8" opacity="0.65"/>',
    '<circle cx="208" cy="207" r="1.4" fill="#68E0B8" opacity="0.60"/>',
    '<circle cx="186" cy="212" r="1.2" fill="#78F0C8" opacity="0.55"/>',
    '<circle cx="214" cy="215" r="1.0" fill="#58D8B0" opacity="0.52"/>',
    # Tether line from orb to totem
    '<line x1="200" y1="222" x2="200" y2="237" stroke="#58E0B8" stroke-width="1.4" opacity="0.42"/>',
    # Offering crystals flanking base
    '<polygon points="180,284 183,275 186,284" fill="#48D0A8" opacity="0.72"/>',
    '<polygon points="214,283 217,274 220,283" fill="#48D0A8" opacity="0.68"/>',
    '<circle  cx="183" cy="273" r="2.0" fill="#90FFE0" opacity="0.80"/>',
    '<circle  cx="217" cy="272" r="2.0" fill="#90FFE0" opacity="0.76"/>',
    '<ellipse cx="183" cy="278" rx="4"  ry="2.5" fill="url(#eElem)" opacity="0.35"/>',
    '<ellipse cx="217" cy="278" rx="4"  ry="2.5" fill="url(#eElem)" opacity="0.32"/>',
    '</g>',

    # ── NEAR-MID TREES ────────────────────────────────────────
    # Left
    '<rect x="54"  y="308" width="16" height="202" fill="#251508"/>',
    '<ellipse cx="62"  cy="293" rx="34" ry="46" fill="#1C3E0E" opacity="0.92"/>',
    '<ellipse cx="62"  cy="262" rx="24" ry="32" fill="#224A12" opacity="0.88"/>',
    '<ellipse cx="62"  cy="242" rx="15" ry="20" fill="#285614" opacity="0.84"/>',
    '<ellipse cx="58"  cy="354" rx="10" ry="4"  fill="#1A4A08" opacity="0.66"/>',
    # Right
    '<rect x="333" y="306" width="16" height="204" fill="#251508"/>',
    '<ellipse cx="341" cy="291" rx="34" ry="46" fill="#1C3E0E" opacity="0.90"/>',
    '<ellipse cx="341" cy="260" rx="24" ry="32" fill="#224A12" opacity="0.86"/>',
    '<ellipse cx="341" cy="240" rx="15" ry="20" fill="#285614" opacity="0.82"/>',
    '<ellipse cx="337" cy="352" rx="10" ry="4"  fill="#1A4A08" opacity="0.64"/>',

    # ══════════════════════════════════════════════════════════════════
    #  STAGE 10 SPECIAL: グリダニア門 Gridanian Gate  (x=200, y≈531) ×1.5
    # ══════════════════════════════════════════════════════════════════
    '<g transform="translate(200,531) scale(1.5) translate(-200,-531)">',
    # Ground shadow
    '<ellipse cx="200" cy="576" rx="56" ry="11" fill="#0C1A06" opacity="0.58"/>',
    '<ellipse cx="200" cy="570" rx="40" ry="7"  fill="#284E10" opacity="0.28"/>',

    # LEFT POST — ancient carved wood
    '<rect x="155" y="502" width="20" height="72" fill="url(#eWood)" rx="4"/>',
    '<rect x="156" y="503" width="6"  height="70" fill="#6A4828" opacity="0.22"/>',
    # Carved spirals (Gridanian motif)
    '<path d="M157,516 Q163,512 173,516" stroke="#0E0602" stroke-width="1.3" fill="none" opacity="0.60"/>',
    '<path d="M157,528 Q163,524 173,528" stroke="#0E0602" stroke-width="1.3" fill="none" opacity="0.55"/>',
    '<path d="M157,540 Q163,536 173,540" stroke="#0E0602" stroke-width="1.3" fill="none" opacity="0.50"/>',
    '<path d="M157,552 Q163,548 173,552" stroke="#0E0602" stroke-width="1.1" fill="none" opacity="0.42"/>',
    # Post cap
    '<rect    x="150" y="498" width="28" height="7"   fill="#382010" rx="2"/>',
    '<ellipse cx="164" cy="498" rx="14"  ry="3.8" fill="#483018" opacity="0.62"/>',

    # RIGHT POST
    '<rect x="225" y="502" width="20" height="72" fill="url(#eWood)" rx="4"/>',
    '<rect x="226" y="503" width="6"  height="70" fill="#6A4828" opacity="0.22"/>',
    '<path d="M227,516 Q233,512 243,516" stroke="#0E0602" stroke-width="1.3" fill="none" opacity="0.60"/>',
    '<path d="M227,528 Q233,524 243,528" stroke="#0E0602" stroke-width="1.3" fill="none" opacity="0.55"/>',
    '<path d="M227,540 Q233,536 243,540" stroke="#0E0602" stroke-width="1.3" fill="none" opacity="0.50"/>',
    '<path d="M227,552 Q233,548 243,552" stroke="#0E0602" stroke-width="1.1" fill="none" opacity="0.42"/>',
    '<rect    x="222" y="498" width="28" height="7"   fill="#382010" rx="2"/>',
    '<ellipse cx="236" cy="498" rx="14"  ry="3.8" fill="#483018" opacity="0.62"/>',

    # CURVED TOP BEAM (Gridanian arch style)
    '<path d="M148,502 Q200,470 252,502" stroke="#1C0E04" stroke-width="15" fill="none" stroke-linecap="round"/>',
    '<path d="M148,502 Q200,470 252,502" stroke="url(#eBeam)" stroke-width="12" fill="none" stroke-linecap="round"/>',
    '<path d="M150,503 Q200,472 250,503" stroke="#7A5230" stroke-width="4.5" fill="none" stroke-linecap="round" opacity="0.30"/>',
    '<path d="M151,502 Q200,473 249,502" stroke="#1A0C04" stroke-width="1.5" fill="none" opacity="0.22"/>',
    # Second horizontal crossbar
    '<rect x="150" y="516" width="100" height="8" fill="#3A2010" rx="2"/>',
    '<rect x="152" y="517" width="40"  height="3" fill="#5A3820" opacity="0.38"/>',

    # VINES — left post
    '<path d="M155,555 Q146,540 148,525 Q143,512 150,502" stroke="#245010" stroke-width="2.8" fill="none" stroke-linecap="round"/>',
    '<ellipse cx="145" cy="538" rx="7"   ry="5"   fill="#2C5A12" transform="rotate(-24,145,538)"/>',
    '<ellipse cx="148" cy="522" rx="6.5" ry="4.5" fill="#326018" transform="rotate(-10,148,522)"/>',
    '<ellipse cx="149" cy="504" rx="5.5" ry="4"   fill="#2C5A12" transform="rotate(8,149,504)"/>',
    '<circle  cx="145" cy="540" r="2.8"            fill="#9AD828" opacity="0.82"/>',
    '<circle  cx="149" cy="523" r="2.4"            fill="#88C830" opacity="0.76"/>',

    # VINES — right post
    '<path d="M245,555 Q254,540 252,525 Q257,512 250,502" stroke="#245010" stroke-width="2.8" fill="none" stroke-linecap="round"/>',
    '<ellipse cx="255" cy="538" rx="7"   ry="5"   fill="#2C5A12" transform="rotate(24,255,538)"/>',
    '<ellipse cx="252" cy="522" rx="6.5" ry="4.5" fill="#326018" transform="rotate(10,252,522)"/>',
    '<ellipse cx="251" cy="504" rx="5.5" ry="4"   fill="#2C5A12" transform="rotate(-8,251,504)"/>',
    '<circle  cx="255" cy="540" r="2.8"            fill="#9AD828" opacity="0.80"/>',
    '<circle  cx="252" cy="523" r="2.4"            fill="#88C830" opacity="0.74"/>',

    # HANGING ARCH VINES
    '<ellipse cx="174" cy="482" rx="6.5" ry="4.5" fill="#285A10" transform="rotate(-38,174,482)"/>',
    '<ellipse cx="200" cy="473" rx="7.5" ry="5"   fill="#306018"/>',
    '<ellipse cx="226" cy="482" rx="6.5" ry="4.5" fill="#285A10" transform="rotate(38,226,482)"/>',
    '<circle  cx="174" cy="482" r="3.2"            fill="#96D030" opacity="0.84"/>',
    '<circle  cx="200" cy="472" r="3.8"            fill="#A4DC38" opacity="0.88"/>',
    '<circle  cx="226" cy="482" r="3.2"            fill="#96D030" opacity="0.82"/>',

    # GLOWING ELEMENTAL CRYSTALS on gate posts
    '<polygon points="161,492 164,482 167,492" fill="#48D0A8" opacity="0.82"/>',
    '<circle  cx="164" cy="480" r="2.8"         fill="#90FFE0" opacity="0.88"/>',
    '<ellipse cx="164" cy="486" rx="5.5" ry="3.2" fill="url(#eElem)" opacity="0.40"/>',

    '<polygon points="233,492 236,482 239,492" fill="#48D0A8" opacity="0.80"/>',
    '<circle  cx="236" cy="480" r="2.8"         fill="#90FFE0" opacity="0.85"/>',
    '<ellipse cx="236" cy="486" rx="5.5" ry="3.2" fill="url(#eElem)" opacity="0.38"/>',

    # CENTER AETHERYTE SHARD (top of arch)
    '<polygon points="196,490 200,479 204,490" fill="#68E0B8" opacity="0.75"/>',
    '<circle  cx="200" cy="477" r="3.5"         fill="#B0FFE8" opacity="0.90"/>',
    '<ellipse cx="200" cy="485" rx="7" ry="4"   fill="url(#eElem)" opacity="0.32"/>',

    '</g>',

    # ── FOREGROUND GIANT TREES ────────────────────────────────
    # Left — massive ancient tree with visible root system
    '<rect x="-10" y="415" width="34" height="185" fill="url(#eTrunk)"/>',
    '<path d="M-10,498 Q-32,472 -44,496 Q-24,476 -10,502" fill="#160E04" opacity="0.88"/>',
    '<path d="M24,498  Q50,472  64,494  Q44,476  24,502"  fill="#160E04" opacity="0.82"/>',
    '<path d="M0,545   Q-24,524 -36,548 Q-16,528  0,552"  fill="#120C04" opacity="0.75"/>',
    '<path d="M14,548  Q38,528  50,550  Q30,532  14,555"  fill="#120C04" opacity="0.72"/>',
    # Canopy
    '<ellipse cx="7"   cy="392" rx="70" ry="55" fill="#183808" opacity="0.98"/>',
    '<ellipse cx="7"   cy="358" rx="52" ry="40" fill="#1C4410" opacity="0.96"/>',
    '<ellipse cx="7"   cy="330" rx="38" ry="28" fill="#224C12" opacity="0.93"/>',
    '<ellipse cx="7"   cy="308" rx="25" ry="18" fill="#285414" opacity="0.88"/>',
    '<ellipse cx="7"   cy="292" rx="15" ry="10" fill="#2E5C16" opacity="0.82"/>',
    # Moss on trunk
    '<ellipse cx="2"   cy="452" rx="16" ry="6"  fill="#184808" opacity="0.72"/>',
    '<ellipse cx="12"  cy="478" rx="13" ry="5"  fill="#163C08" opacity="0.66"/>',
    # Lower canopy skirt (covers trunk edges)
    '<ellipse cx="-2"  cy="485" rx="65" ry="26" fill="#142C08"/>',
    '<ellipse cx="-10" cy="528" rx="60" ry="23" fill="#122A06"/>',
    '<ellipse cx="-2"  cy="570" rx="57" ry="21" fill="#142C08"/>',
    '<ellipse cx="-10" cy="608" rx="54" ry="19" fill="#163008"/>',

    # Right — massive ancient tree
    '<rect x="376" y="415" width="34" height="185" fill="url(#eTrunk)"/>',
    '<path d="M410,498 Q432,472 444,496 Q424,476 410,502" fill="#160E04" opacity="0.86"/>',
    '<path d="M376,498 Q350,472 336,494 Q356,476 376,502" fill="#160E04" opacity="0.80"/>',
    '<path d="M400,545 Q424,524 436,548 Q416,528 400,552" fill="#120C04" opacity="0.73"/>',
    '<path d="M386,548 Q362,528 350,550 Q370,532 386,555" fill="#120C04" opacity="0.70"/>',
    '<ellipse cx="393" cy="392" rx="70" ry="55" fill="#183808" opacity="0.96"/>',
    '<ellipse cx="393" cy="358" rx="52" ry="40" fill="#1C4410" opacity="0.94"/>',
    '<ellipse cx="393" cy="330" rx="38" ry="28" fill="#224C12" opacity="0.91"/>',
    '<ellipse cx="393" cy="308" rx="25" ry="18" fill="#285414" opacity="0.86"/>',
    '<ellipse cx="393" cy="292" rx="15" ry="10" fill="#2E5C16" opacity="0.80"/>',
    '<ellipse cx="388" cy="452" rx="16" ry="6"  fill="#184808" opacity="0.70"/>',
    '<ellipse cx="398" cy="478" rx="13" ry="5"  fill="#163C08" opacity="0.64"/>',
    '<ellipse cx="402" cy="485" rx="65" ry="26" fill="#142C08"/>',
    '<ellipse cx="410" cy="528" rx="60" ry="23" fill="#122A06"/>',
    '<ellipse cx="402" cy="570" rx="57" ry="21" fill="#142C08"/>',
    '<ellipse cx="410" cy="608" rx="54" ry="19" fill="#163008"/>',

    # ── GROUND MIST ───────────────────────────────────────────
    '<rect y="558" width="400" height="42" fill="url(#eMist)" opacity="0.78"/>',
    '<rect y="582" width="400" height="18" fill="#1E3C0C" opacity="0.14"/>',

    '</svg>',
)

# ── inject helper ─────────────────────────────────────────────────────
def inject(html, diff, svg_str):
    pattern = rf"(if\(diff==='{diff}'\) return ')(.*?)(';)"
    def replacer(m):
        return m.group(1) + svg_str + m.group(3)
    new_html = re.sub(pattern, replacer, html, flags=re.DOTALL)
    return new_html

content = inject(content, 'EASY', EASY)

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('EASY injected OK —', len(EASY), 'chars')
