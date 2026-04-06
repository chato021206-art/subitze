#!/usr/bin/env python3
"""NORMAL SVG masterpiece - Summer Countryside. No center path. Full-width nature."""
import re

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

def J(*parts):
    return ''.join(parts)

# ═══════════════════════════════════════════════════════════════════════
#  NORMAL  夏の田舎  Summer Countryside  — MASTERPIECE
#  ・道なし（全幅を夏の田園で覆う）
#  ・空、積乱雲、木漏れ日、広大な緑、ひまわり、麦畑、木柵、遠くの農家
#  ・Stage5 (y≈235, x=200): 石の井戸
#  ・Stage10 (y≈531, x=200): 石のアーチ門（ツタ付き）
# ═══════════════════════════════════════════════════════════════════════

NORMAL = J(
    '<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">',
    '<defs>',

    # Sky: deep summer blue
    '<linearGradient id="nSky" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#2E7ED4"/>',
    '<stop offset="42%" stop-color="#5EA8E8"/>',
    '<stop offset="76%" stop-color="#9CCEF4"/>',
    '<stop offset="100%" stop-color="#C8E8C0"/>',
    '</linearGradient>',

    # Ground: rich midsummer green
    '<linearGradient id="nGnd" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#3CAC34"/>',
    '<stop offset="50%" stop-color="#248A20"/>',
    '<stop offset="100%" stop-color="#14521A"/>',
    '</linearGradient>',

    # Sun radial (upper-left this time)
    '<radialGradient id="nSun" cx="22%" cy="7%" r="38%">',
    '<stop offset="0%" stop-color="#FFF4A0" stop-opacity="0.84"/>',
    '<stop offset="40%" stop-color="#FFE850" stop-opacity="0.26"/>',
    '<stop offset="100%" stop-color="#FFF4A0" stop-opacity="0"/>',
    '</radialGradient>',

    # Wheat field gradient
    '<linearGradient id="nWheat" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#D4A830"/>',
    '<stop offset="100%" stop-color="#A87820"/>',
    '</linearGradient>',

    # Stone gradient for well/gate
    '<linearGradient id="nStone" x1="0" y1="0" x2="1" y2="1">',
    '<stop offset="0%" stop-color="#B0A898"/>',
    '<stop offset="50%" stop-color="#888078"/>',
    '<stop offset="100%" stop-color="#706860"/>',
    '</linearGradient>',

    # Depth fog
    '<linearGradient id="nDpth" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#041A04" stop-opacity="0.62"/>',
    '<stop offset="17%" stop-color="#041A04" stop-opacity="0.04"/>',
    '<stop offset="100%" stop-color="#041A04" stop-opacity="0"/>',
    '</linearGradient>',

    # Ground warmth
    '<radialGradient id="nWarm" cx="50%" cy="75%" r="52%">',
    '<stop offset="0%" stop-color="#C8E440" stop-opacity="0.13"/>',
    '<stop offset="100%" stop-color="#C8E440" stop-opacity="0"/>',
    '</radialGradient>',

    '</defs>',

    # ── SKY & GROUND ─────────────────────────────────────────────────
    '<rect width="400" height="600" fill="url(#nSky)"/>',
    '<rect y="118" width="400" height="482" fill="url(#nGnd)"/>',

    # ── CUMULUS CLOUDS ────────────────────────────────────────────────
    # Cloud A (right, large — summer cumulus)
    '<ellipse cx="310" cy="30" rx="52" ry="20" fill="#FFFFFF" opacity="0.92"/>',
    '<ellipse cx="280" cy="34" rx="28" ry="15" fill="#FFFFFF" opacity="0.88"/>',
    '<ellipse cx="342" cy="33" rx="30" ry="16" fill="#FFFFFF" opacity="0.86"/>',
    '<ellipse cx="310" cy="22" rx="34" ry="14" fill="#FFFFFF" opacity="0.78"/>',
    # Cloud shadow (bottom tint)
    '<ellipse cx="310" cy="40" rx="52" ry="10" fill="#C8D8E8" opacity="0.30"/>',
    # Cloud B (left, medium)
    '<ellipse cx="70" cy="24" rx="38" ry="14" fill="#FFFFFF" opacity="0.88"/>',
    '<ellipse cx="48" cy="27" rx="20" ry="11" fill="#FFFFFF" opacity="0.82"/>',
    '<ellipse cx="94" cy="26" rx="22" ry="12" fill="#FFFFFF" opacity="0.82"/>',
    # Cloud C (far center)
    '<ellipse cx="190" cy="14" rx="24" ry="9" fill="#FFFFFF" opacity="0.70"/>',

    # ── SUN & OVERLAYS ───────────────────────────────────────────────
    '<rect width="400" height="600" fill="url(#nSun)"/>',
    '<rect y="118" width="400" height="482" fill="url(#nWarm)"/>',
    '<rect width="400" height="600" fill="url(#nDpth)"/>',

    # ── ROLLING HILLS ────────────────────────────────────────────────
    '<ellipse cx="60" cy="152" rx="125" ry="44" fill="#40B038" opacity="0.76"/>',
    '<ellipse cx="220" cy="145" rx="155" ry="50" fill="#3CA832" opacity="0.70"/>',
    '<ellipse cx="374" cy="154" rx="130" ry="42" fill="#44B43C" opacity="0.74"/>',
    '<ellipse cx="155" cy="158" rx="90" ry="34" fill="#48BC40" opacity="0.58"/>',
    '<ellipse cx="310" cy="160" rx="80" ry="30" fill="#3EA836" opacity="0.56"/>',

    # ── BIRDS ────────────────────────────────────────────────────────
    '<path d="M32,22 Q37,17 42,22" stroke="#1A4A30" stroke-width="1.4" fill="none"/>',
    '<path d="M52,15 Q57,10 62,15" stroke="#1A4A30" stroke-width="1.2" fill="none"/>',
    '<path d="M148,10 Q153,5 158,10" stroke="#1A4A30" stroke-width="1.1" fill="none"/>',
    '<path d="M350,14 Q355,9 360,14" stroke="#1A4A30" stroke-width="1.2" fill="none"/>',
    '<path d="M370,26 Q375,21 380,26" stroke="#1A4A30" stroke-width="1.3" fill="none"/>',

    # ── DISTANT FARMHOUSE SILHOUETTE (y≈120-145, right side x≈295) ──
    # House body
    '<rect x="290" y="132" width="26" height="18" fill="#7A6858" opacity="0.82"/>',
    # Roof
    '<polygon points="288,132 303,120 320,132" fill="#5A3820" opacity="0.82"/>',
    # Chimney
    '<rect x="310" y="124" width="4" height="8" fill="#5A3820" opacity="0.78"/>',
    # Windows (lit)
    '<rect x="294" y="137" width="5" height="5" fill="#FFE0A0" opacity="0.70"/>',
    '<rect x="303" y="137" width="5" height="5" fill="#FFE0A0" opacity="0.68"/>',
    # Door
    '<rect x="298" y="143" width="5" height="7" fill="#4A3020" opacity="0.72"/>',
    # Barn (left of house)
    '<rect x="268" y="136" width="18" height="14" fill="#6A4828" opacity="0.76"/>',
    '<polygon points="266,136 277,126 288,136" fill="#4A2C12" opacity="0.76"/>',
    # Silo
    '<rect x="254" y="133" width="8" height="17" fill="#887060" opacity="0.70"/>',
    '<ellipse cx="258" cy="133" rx="4" ry="2" fill="#706050" opacity="0.72"/>',

    # ── LAYER 2: HORIZON MICRO-TREES (y≈118-124) ─────────────────────
    '<circle cx="20" cy="120" r="5.5" fill="#185A18" opacity="0.78"/>',
    '<circle cx="35" cy="118" r="4.5" fill="#1C6020" opacity="0.74"/>',
    '<circle cx="108" cy="120" r="5" fill="#185A18" opacity="0.74"/>',
    '<circle cx="200" cy="118" r="4" fill="#1A5A1C" opacity="0.70"/>',
    '<circle cx="248" cy="119" r="5" fill="#185A18" opacity="0.72"/>',
    '<circle cx="352" cy="118" r="5.5" fill="#1C6020" opacity="0.74"/>',
    '<circle cx="372" cy="120" r="4" fill="#185A18" opacity="0.72"/>',

    # ── LAYER 2: VERY FAR TREES ───────────────────────────────────────
    '<rect x="14" y="110" width="1.8" height="22" fill="#112A08"/>',
    '<circle cx="14.9" cy="109" r="7.5" fill="#1C5C18" opacity="0.92"/>',
    '<circle cx="14.9" cy="102" r="5.8" fill="#246422" opacity="0.90"/>',
    '<rect x="34" y="112" width="1.5" height="18" fill="#112A08"/>',
    '<circle cx="34.75" cy="111" r="6" fill="#1A5818" opacity="0.90"/>',
    '<circle cx="34.75" cy="105" r="4.5" fill="#226020" opacity="0.88"/>',
    # Center-left
    '<rect x="98" y="111" width="1.8" height="21" fill="#112A08"/>',
    '<circle cx="98.9" cy="110" r="7" fill="#1C5C18" opacity="0.90"/>',
    '<circle cx="98.9" cy="103" r="5.5" fill="#246422" opacity="0.88"/>',
    # Center-right
    '<rect x="244" y="112" width="1.8" height="20" fill="#112A08"/>',
    '<circle cx="244.9" cy="111" r="7" fill="#1C5C18" opacity="0.90"/>',
    '<circle cx="244.9" cy="104" r="5.5" fill="#246422" opacity="0.88"/>',
    # Right
    '<rect x="356" y="110" width="1.8" height="22" fill="#112A08"/>',
    '<circle cx="356.9" cy="109" r="7.5" fill="#1C5C18" opacity="0.92"/>',
    '<circle cx="356.9" cy="102" r="5.8" fill="#246422" opacity="0.90"/>',
    '<rect x="378" y="112" width="1.5" height="18" fill="#112A08"/>',
    '<circle cx="378.75" cy="111" r="6" fill="#1A5818" opacity="0.90"/>',
    '<circle cx="378.75" cy="105" r="4.5" fill="#226020" opacity="0.88"/>',

    # ── LAYER 3: FAR TREES (oak silhouettes, wider crowns) ────────────
    # Left cluster
    '<rect x="4" y="130" width="2.6" height="32" fill="#162C0A"/>',
    '<ellipse cx="5.3" cy="126" rx="12" ry="10" fill="#246820" opacity="0.94"/>',
    '<ellipse cx="5.3" cy="118" rx="9" ry="7.5" fill="#2E7828" opacity="0.92"/>',
    '<rect x="24" y="133" width="2.3" height="28" fill="#162C0A"/>',
    '<ellipse cx="25.15" cy="129" rx="11" ry="9" fill="#226418" opacity="0.92"/>',
    '<ellipse cx="25.15" cy="122" rx="8" ry="6.5" fill="#2C7222" opacity="0.90"/>',
    # Center-left
    '<rect x="80" y="131" width="2.5" height="30" fill="#162C0A"/>',
    '<ellipse cx="81.25" cy="127" rx="12" ry="10" fill="#246820" opacity="0.92"/>',
    '<ellipse cx="81.25" cy="119" rx="9" ry="7" fill="#2E7828" opacity="0.90"/>',
    # Center (poplar - tall & thin)
    '<rect x="174" y="120" width="2" height="42" fill="#162C0A"/>',
    '<ellipse cx="175" cy="117" rx="5.5" ry="12" fill="#1E6418" opacity="0.92"/>',
    '<ellipse cx="175" cy="107" rx="4" ry="9" fill="#267020" opacity="0.90"/>',
    # Center-right
    '<rect x="268" y="131" width="2.5" height="30" fill="#162C0A"/>',
    '<ellipse cx="269.25" cy="127" rx="12" ry="10" fill="#246820" opacity="0.92"/>',
    '<ellipse cx="269.25" cy="119" rx="9" ry="7" fill="#2E7828" opacity="0.90"/>',
    # Right cluster
    '<rect x="362" y="130" width="2.6" height="32" fill="#162C0A"/>',
    '<ellipse cx="363.3" cy="126" rx="12" ry="10" fill="#246820" opacity="0.94"/>',
    '<ellipse cx="363.3" cy="118" rx="9" ry="7.5" fill="#2E7828" opacity="0.92"/>',
    '<rect x="382" y="133" width="2.3" height="28" fill="#162C0A"/>',
    '<ellipse cx="383.15" cy="129" rx="11" ry="9" fill="#226418" opacity="0.92"/>',
    '<ellipse cx="383.15" cy="122" rx="8" ry="6.5" fill="#2C7222" opacity="0.90"/>',

    # ── WHEAT FIELD PATCH (y≈165-195, center-left, x≈55-145) ────────
    # Field base
    '<rect x="55" y="168" width="90" height="30" fill="url(#nWheat)" opacity="0.78" rx="2"/>',
    # Wheat stalks (dense fine lines)
    '<line x1="62" y1="195" x2="62" y2="170" stroke="#C09820" stroke-width="1.0" opacity="0.70"/>',
    '<line x1="68" y1="195" x2="68" y2="168" stroke="#C8A020" stroke-width="1.0" opacity="0.70"/>',
    '<line x1="74" y1="195" x2="74" y2="170" stroke="#C09820" stroke-width="1.0" opacity="0.68"/>',
    '<line x1="80" y1="195" x2="80" y2="168" stroke="#C8A020" stroke-width="1.0" opacity="0.68"/>',
    '<line x1="86" y1="195" x2="86" y2="170" stroke="#C09820" stroke-width="1.0" opacity="0.68"/>',
    '<line x1="92" y1="195" x2="92" y2="168" stroke="#C8A020" stroke-width="1.0" opacity="0.68"/>',
    '<line x1="98" y1="195" x2="98" y2="170" stroke="#C09820" stroke-width="1.0" opacity="0.68"/>',
    '<line x1="104" y1="195" x2="104" y2="168" stroke="#C8A020" stroke-width="1.0" opacity="0.68"/>',
    '<line x1="110" y1="195" x2="110" y2="170" stroke="#C09820" stroke-width="1.0" opacity="0.68"/>',
    '<line x1="116" y1="195" x2="116" y2="168" stroke="#C8A020" stroke-width="1.0" opacity="0.68"/>',
    '<line x1="122" y1="195" x2="122" y2="170" stroke="#C09820" stroke-width="1.0" opacity="0.68"/>',
    '<line x1="128" y1="195" x2="128" y2="168" stroke="#C8A020" stroke-width="1.0" opacity="0.70"/>',
    '<line x1="134" y1="195" x2="134" y2="170" stroke="#C09820" stroke-width="1.0" opacity="0.70"/>',
    '<line x1="140" y1="195" x2="140" y2="168" stroke="#C8A020" stroke-width="1.0" opacity="0.70"/>',
    # Wheat heads
    '<ellipse cx="62" cy="170" rx="2.5" ry="4.5" fill="#E8C030" opacity="0.85"/>',
    '<ellipse cx="68" cy="168" rx="2.5" ry="4.5" fill="#D8B028" opacity="0.85"/>',
    '<ellipse cx="74" cy="170" rx="2.5" ry="4.5" fill="#E8C030" opacity="0.82"/>',
    '<ellipse cx="80" cy="168" rx="2.5" ry="4.5" fill="#D8B028" opacity="0.82"/>',
    '<ellipse cx="86" cy="170" rx="2.5" ry="4.5" fill="#E8C030" opacity="0.82"/>',
    '<ellipse cx="92" cy="168" rx="2.5" ry="4.5" fill="#D8B028" opacity="0.82"/>',
    '<ellipse cx="98" cy="170" rx="2.5" ry="4.5" fill="#E8C030" opacity="0.82"/>',
    '<ellipse cx="104" cy="168" rx="2.5" ry="4.5" fill="#D8B028" opacity="0.82"/>',
    '<ellipse cx="110" cy="170" rx="2.5" ry="4.5" fill="#E8C030" opacity="0.82"/>',
    '<ellipse cx="116" cy="168" rx="2.5" ry="4.5" fill="#D8B028" opacity="0.82"/>',
    '<ellipse cx="122" cy="170" rx="2.5" ry="4.5" fill="#E8C030" opacity="0.82"/>',
    '<ellipse cx="128" cy="168" rx="2.5" ry="4.5" fill="#D8B028" opacity="0.85"/>',
    '<ellipse cx="134" cy="170" rx="2.5" ry="4.5" fill="#E8C030" opacity="0.85"/>',
    '<ellipse cx="140" cy="168" rx="2.5" ry="4.5" fill="#D8B028" opacity="0.85"/>',

    # ── LAYER 4: MID-DISTANCE OAKS ────────────────────────────────────
    # Left (wide oak crowns)
    '<rect x="6" y="176" width="4.5" height="54" fill="#182E08"/>',
    '<ellipse cx="8.25" cy="171" rx="20" ry="14" fill="#2E7020" opacity="0.96"/>',
    '<ellipse cx="8.25" cy="161" rx="14" ry="10" fill="#389028" opacity="0.94"/>',
    '<ellipse cx="-2" cy="174" rx="12" ry="9" fill="#2A6C1C" opacity="0.88"/>',
    '<ellipse cx="18" cy="175" rx="12" ry="9" fill="#2A6C1C" opacity="0.88"/>',
    '<rect x="40" y="180" width="4" height="50" fill="#182E08"/>',
    '<ellipse cx="42" cy="175" rx="17" ry="12" fill="#2A6A1C" opacity="0.94"/>',
    '<ellipse cx="42" cy="166" rx="12" ry="8.5" fill="#348826" opacity="0.92"/>',
    # Left-center poplar (tall)
    '<rect x="118" y="162" width="3" height="68" fill="#182E08"/>',
    '<ellipse cx="119.5" cy="158" rx="7" ry="16" fill="#226A1E" opacity="0.94"/>',
    '<ellipse cx="119.5" cy="145" rx="5.5" ry="12" fill="#2C8024" opacity="0.92"/>',
    # Right-center oak
    '<rect x="280" y="178" width="4.2" height="52" fill="#182E08"/>',
    '<ellipse cx="282.1" cy="173" rx="19" ry="13" fill="#2E7020" opacity="0.94"/>',
    '<ellipse cx="282.1" cy="163" rx="13" ry="9.5" fill="#389028" opacity="0.92"/>',
    '<ellipse cx="272" cy="177" rx="11" ry="8" fill="#2A6A1C" opacity="0.86"/>',
    '<ellipse cx="292" cy="177" rx="11" ry="8" fill="#2A6A1C" opacity="0.86"/>',
    # Right poplar
    '<rect x="338" y="163" width="3" height="66" fill="#182E08"/>',
    '<ellipse cx="339.5" cy="159" rx="7" ry="16" fill="#226A1E" opacity="0.94"/>',
    '<ellipse cx="339.5" cy="146" rx="5.5" ry="12" fill="#2C8024" opacity="0.92"/>',
    # Right oak pair
    '<rect x="348" y="176" width="4.5" height="54" fill="#182E08"/>',
    '<ellipse cx="350.25" cy="171" rx="20" ry="14" fill="#2E7020" opacity="0.96"/>',
    '<ellipse cx="350.25" cy="161" rx="14" ry="10" fill="#389028" opacity="0.94"/>',
    '<rect x="376" y="180" width="4" height="50" fill="#182E08"/>',
    '<ellipse cx="378" cy="175" rx="17" ry="12" fill="#2A6A1C" opacity="0.94"/>',
    '<ellipse cx="378" cy="166" rx="12" ry="8.5" fill="#348826" opacity="0.92"/>',

    # ── WOODEN FENCE (horizontal, y≈200) ─────────────────────────────
    # Posts (every 38px across width, receding)
    '<rect x="0"   y="196" width="5" height="22" fill="#7A5028" rx="1"/>',
    '<rect x="38"  y="196" width="5" height="22" fill="#7A5028" rx="1"/>',
    '<rect x="76"  y="196" width="5" height="22" fill="#7A5028" rx="1"/>',
    '<rect x="114" y="196" width="5" height="22" fill="#7A5028" rx="1"/>',
    '<rect x="152" y="196" width="5" height="22" fill="#7A5028" rx="1"/>',
    '<rect x="190" y="196" width="5" height="22" fill="#7A5028" rx="1"/>',
    '<rect x="228" y="196" width="5" height="22" fill="#7A5028" rx="1"/>',
    '<rect x="266" y="196" width="5" height="22" fill="#7A5028" rx="1"/>',
    '<rect x="304" y="196" width="5" height="22" fill="#7A5028" rx="1"/>',
    '<rect x="342" y="196" width="5" height="22" fill="#7A5028" rx="1"/>',
    '<rect x="380" y="196" width="5" height="22" fill="#7A5028" rx="1"/>',
    # Horizontal rails
    '<rect x="0" y="200" width="400" height="3.5" fill="#8A6030" opacity="0.88" rx="1"/>',
    '<rect x="0" y="210" width="400" height="3.5" fill="#8A6030" opacity="0.84" rx="1"/>',
    # Rail highlights
    '<rect x="0" y="200" width="400" height="1.2" fill="#B08040" opacity="0.38"/>',
    '<rect x="0" y="210" width="400" height="1.2" fill="#B08040" opacity="0.35"/>',

    # ══════════════════════════════════════════════════════════════════
    #  STAGE 5 SPECIAL: 石の井戸  Stone Well  (x=200, y≈235)
    # ══════════════════════════════════════════════════════════════════
    '<g transform="translate(52,0)">',
    # Ground shadow
    '<ellipse cx="200" cy="290" rx="22" ry="7" fill="#145A14" opacity="0.38"/>',
    # Well base (stone cylinder, front face)
    '<ellipse cx="200" cy="278" rx="18" ry="7" fill="url(#nStone)"/>',
    '<rect x="182" y="249" width="36" height="30" fill="#888078"/>',
    '<ellipse cx="200" cy="249" rx="18" ry="7" fill="#A09888"/>',
    # Stone texture on well body
    '<rect x="182" y="254" width="36" height="2" fill="#706860" opacity="0.35"/>',
    '<rect x="182" y="261" width="36" height="2" fill="#706860" opacity="0.35"/>',
    '<rect x="182" y="268" width="36" height="2" fill="#706860" opacity="0.35"/>',
    '<rect x="182" y="256" width="12" height="4" fill="#808070" opacity="0.30"/>',
    '<rect x="198" y="258" width="14" height="4" fill="#808070" opacity="0.28"/>',
    '<rect x="184" y="263" width="16" height="4" fill="#808070" opacity="0.28"/>',
    '<rect x="204" y="265" width="12" height="4" fill="#808070" opacity="0.28"/>',
    '<rect x="184" y="270" width="10" height="4" fill="#808070" opacity="0.28"/>',
    '<rect x="200" y="272" width="14" height="4" fill="#808070" opacity="0.28"/>',
    # Well frame — left post
    '<rect x="188" y="224" width="5" height="28" fill="#5A3818" rx="2"/>',
    # Well frame — right post
    '<rect x="207" y="224" width="5" height="28" fill="#5A3818" rx="2"/>',
    # Well frame — top beam
    '<rect x="186" y="222" width="28" height="5" fill="#6A4820" rx="2"/>',
    '<rect x="187" y="222" width="10" height="2" fill="#8A6030" opacity="0.40"/>',
    # Axle
    '<rect x="195" y="221" width="10" height="4" fill="#4A2810" rx="1"/>',
    # Rope
    '<line x1="200" y1="225" x2="200" y2="248" stroke="#8A7050" stroke-width="1.8"/>',
    '<line x1="200" y1="225" x2="202" y2="248" stroke="#A08860" stroke-width="0.8" opacity="0.50"/>',
    # Bucket
    '<rect x="193" y="248" width="14" height="11" fill="#6A5030" rx="2"/>',
    '<ellipse cx="200" cy="248" rx="7" ry="2.5" fill="#7A6040"/>',
    '<ellipse cx="200" cy="259" rx="7" ry="2.5" fill="#5A4020"/>',
    # Bucket handle
    '<path d="M193,250 Q186,245 193,240" stroke="#4A3010" stroke-width="1.5" fill="none" stroke-linecap="round"/>',
    # Water shimmer inside bucket top
    '<ellipse cx="200" cy="249" rx="5.5" ry="1.8" fill="#80C8F0" opacity="0.55"/>',
    # Moss on well
    '<ellipse cx="184" cy="272" rx="4" ry="2.5" fill="#3A8020" opacity="0.62"/>',
    '<ellipse cx="216" cy="268" rx="3.5" ry="2" fill="#3A8020" opacity="0.58"/>',
    # Flowers near well base
    '<circle cx="178" cy="282" r="4" fill="#FF8AB4"/>',
    '<circle cx="178" cy="282" r="1.8" fill="#FFE870"/>',
    '<circle cx="222" cy="280" r="3.5" fill="#FFD700"/>',
    '</g>',

    # ── LAYER 5: NEAR-MID OAKS ────────────────────────────────────────
    # Left large oak
    '<rect x="10" y="290" width="7.5" height="88" fill="#1A2E08"/>',
    '<ellipse cx="13.75" cy="280" rx="32" ry="24" fill="#287020" opacity="0.97"/>',
    '<ellipse cx="13.75" cy="262" rx="22" ry="17" fill="#349030" opacity="0.95"/>',
    '<ellipse cx="13.75" cy="249" rx="14" ry="11" fill="#42A838" opacity="0.92"/>',
    '<ellipse cx="-2" cy="288" rx="18" ry="14" fill="#246A1C" opacity="0.90"/>',
    '<ellipse cx="30" cy="284" rx="18" ry="13" fill="#246A1C" opacity="0.90"/>',
    # Left mid-oak
    '<rect x="52" y="296" width="6" height="82" fill="#1A2E08"/>',
    '<ellipse cx="55" cy="287" rx="26" ry="20" fill="#267018" opacity="0.95"/>',
    '<ellipse cx="55" cy="271" rx="18" ry="14" fill="#328A26" opacity="0.93"/>',
    '<ellipse cx="55" cy="260" rx="12" ry="9" fill="#3EA032" opacity="0.90"/>',
    # Center-left oak (x≈130)
    '<rect x="127" y="298" width="5.5" height="78" fill="#1A2E08"/>',
    '<ellipse cx="129.75" cy="289" rx="24" ry="19" fill="#267018" opacity="0.95"/>',
    '<ellipse cx="129.75" cy="273" rx="17" ry="13" fill="#32882A" opacity="0.93"/>',
    '<ellipse cx="129.75" cy="262" rx="11" ry="8.5" fill="#3EA030" opacity="0.90"/>',
    # Right-center oak (x≈268)
    '<rect x="266" y="298" width="5.5" height="78" fill="#1A2E08"/>',
    '<ellipse cx="268.75" cy="289" rx="24" ry="19" fill="#267018" opacity="0.95"/>',
    '<ellipse cx="268.75" cy="273" rx="17" ry="13" fill="#32882A" opacity="0.93"/>',
    '<ellipse cx="268.75" cy="262" rx="11" ry="8.5" fill="#3EA030" opacity="0.90"/>',
    # Right mid-oak
    '<rect x="340" y="296" width="6" height="82" fill="#1A2E08"/>',
    '<ellipse cx="343" cy="287" rx="26" ry="20" fill="#267018" opacity="0.95"/>',
    '<ellipse cx="343" cy="271" rx="18" ry="14" fill="#328A26" opacity="0.93"/>',
    '<ellipse cx="343" cy="260" rx="12" ry="9" fill="#3EA032" opacity="0.90"/>',
    # Right large oak
    '<rect x="376" y="290" width="7.5" height="88" fill="#1A2E08"/>',
    '<ellipse cx="379.75" cy="280" rx="32" ry="24" fill="#287020" opacity="0.97"/>',
    '<ellipse cx="379.75" cy="262" rx="22" ry="17" fill="#349030" opacity="0.95"/>',
    '<ellipse cx="379.75" cy="249" rx="14" ry="11" fill="#42A838" opacity="0.92"/>',
    '<ellipse cx="366" cy="288" rx="18" ry="14" fill="#246A1C" opacity="0.90"/>',
    '<ellipse cx="395" cy="284" rx="18" ry="13" fill="#246A1C" opacity="0.90"/>',

    # ── SUNFLOWER CLUSTERS ────────────────────────────────────────────
    # Sunflower function: center x, base y
    # Left cluster (x≈75, y≈395)
    '<rect x="73.5" y="378" width="3" height="42" fill="#3A7020"/>',
    '<circle cx="75" cy="374" r="9" fill="#FFD700"/>',
    '<circle cx="75" cy="374" r="4.5" fill="#6A3010"/>',
    '<rect x="55.5" y="388" width="2.5" height="32" fill="#3A7020"/>',
    '<circle cx="56.8" cy="384" r="7.5" fill="#FFD700"/>',
    '<circle cx="56.8" cy="384" r="3.8" fill="#6A3010"/>',
    '<rect x="90.5" y="390" width="2.5" height="30" fill="#3A7020"/>',
    '<circle cx="91.8" cy="386" r="7" fill="#FFD700"/>',
    '<circle cx="91.8" cy="386" r="3.5" fill="#6A3010"/>',
    # Sunflower petal rings (left cluster)
    '<circle cx="75" cy="364" r="3.5" fill="#FFA820" opacity="0.82"/>',
    '<circle cx="75" cy="384" r="3.5" fill="#FFA820" opacity="0.82"/>',
    '<circle cx="65" cy="374" r="3.5" fill="#FFA820" opacity="0.82"/>',
    '<circle cx="85" cy="374" r="3.5" fill="#FFA820" opacity="0.82"/>',
    '<circle cx="68" cy="367" r="3" fill="#FFB830" opacity="0.78"/>',
    '<circle cx="82" cy="367" r="3" fill="#FFB830" opacity="0.78"/>',
    '<circle cx="68" cy="381" r="3" fill="#FFB830" opacity="0.78"/>',
    '<circle cx="82" cy="381" r="3" fill="#FFB830" opacity="0.78"/>',
    # Sunflower leaves
    '<ellipse cx="68" cy="400" rx="8" ry="4" fill="#3A8020" transform="rotate(-25,68,400)"/>',
    '<ellipse cx="82" cy="405" rx="8" ry="4" fill="#3A8020" transform="rotate(25,82,405)"/>',

    # Right sunflower cluster (x≈325, y≈390)
    '<rect x="323.5" y="382" width="3" height="38" fill="#3A7020"/>',
    '<circle cx="325" cy="378" r="9" fill="#FFD700"/>',
    '<circle cx="325" cy="378" r="4.5" fill="#6A3010"/>',
    '<rect x="308.5" y="392" width="2.5" height="28" fill="#3A7020"/>',
    '<circle cx="309.8" cy="388" r="7.5" fill="#FFD700"/>',
    '<circle cx="309.8" cy="388" r="3.8" fill="#6A3010"/>',
    '<rect x="339.5" y="390" width="2.5" height="30" fill="#3A7020"/>',
    '<circle cx="340.8" cy="386" r="7" fill="#FFD700"/>',
    '<circle cx="340.8" cy="386" r="3.5" fill="#6A3010"/>',
    # Petals right cluster
    '<circle cx="325" cy="368" r="3.5" fill="#FFA820" opacity="0.82"/>',
    '<circle cx="325" cy="388" r="3.5" fill="#FFA820" opacity="0.82"/>',
    '<circle cx="315" cy="378" r="3.5" fill="#FFA820" opacity="0.82"/>',
    '<circle cx="335" cy="378" r="3.5" fill="#FFA820" opacity="0.82"/>',
    '<circle cx="318" cy="371" r="3" fill="#FFB830" opacity="0.78"/>',
    '<circle cx="332" cy="371" r="3" fill="#FFB830" opacity="0.78"/>',
    '<circle cx="318" cy="385" r="3" fill="#FFB830" opacity="0.78"/>',
    '<circle cx="332" cy="385" r="3" fill="#FFB830" opacity="0.78"/>',

    # ── SCATTERED FIELD FLOWERS ───────────────────────────────────────
    '<circle cx="154" cy="350" r="4.5" fill="#FF8AB4"/>',
    '<circle cx="154" cy="350" r="2" fill="#FFE870"/>',
    '<circle cx="240" cy="360" r="4.5" fill="#FFFFFF" opacity="0.92"/>',
    '<circle cx="240" cy="360" r="2" fill="#FFE860"/>',
    '<circle cx="180" cy="445" r="4" fill="#FFD700"/>',
    '<circle cx="225" cy="452" r="4" fill="#FF8AB4"/>',
    '<circle cx="105" cy="472" r="4.5" fill="#FFD700"/>',
    '<circle cx="355" cy="465" r="4" fill="#FF8AB4"/>',
    '<circle cx="290" cy="470" r="4.5" fill="#FFFFFF" opacity="0.90"/>',
    '<circle cx="290" cy="470" r="2" fill="#FFE860"/>',
    # Clover patches
    '<circle cx="160" cy="510" r="3.5" fill="#50C038" opacity="0.80"/>',
    '<circle cx="165" cy="506" r="3" fill="#48B830" opacity="0.78"/>',
    '<circle cx="155" cy="506" r="3" fill="#48B830" opacity="0.78"/>',
    '<circle cx="310" cy="515" r="3.5" fill="#50C038" opacity="0.80"/>',
    '<circle cx="315" cy="511" r="3" fill="#48B830" opacity="0.78"/>',
    '<circle cx="305" cy="511" r="3" fill="#48B830" opacity="0.78"/>',

    # ── GRASS TUFTS ───────────────────────────────────────────────────
    '<path d="M26,476 Q28,463 30,455 Q32,463 34,476" fill="#267018" opacity="0.82"/>',
    '<path d="M148,462 Q150,450 152,443 Q154,450 156,462" fill="#267018" opacity="0.82"/>',
    '<path d="M280,468 Q282,456 284,448 Q286,456 288,468" fill="#267018" opacity="0.82"/>',
    '<path d="M376,473 Q378,461 380,453 Q382,461 384,473" fill="#267018" opacity="0.82"/>',

    # ── COW SILHOUETTE (y≈430, x≈220) ────────────────────────────────
    # Body
    '<ellipse cx="228" cy="430" rx="20" ry="12" fill="#E8E0D0"/>',
    # Head
    '<ellipse cx="248" cy="426" rx="9" ry="7" fill="#E0D8C8"/>',
    # Snout
    '<ellipse cx="256" cy="428" rx="4.5" ry="3.5" fill="#D0C8B8"/>',
    # Nostrils
    '<circle cx="254" cy="428" r="1" fill="#B0A898"/>',
    '<circle cx="258" cy="428" r="1" fill="#B0A898"/>',
    # Eye
    '<circle cx="250" cy="424" r="1.2" fill="#2A1808"/>',
    # Ear
    '<ellipse cx="247" cy="419" rx="3" ry="2" fill="#D8C8B0"/>',
    # Legs
    '<rect x="214" y="440" width="4" height="12" fill="#D0C8B8" rx="1"/>',
    '<rect x="222" y="440" width="4" height="12" fill="#D0C8B8" rx="1"/>',
    '<rect x="232" y="440" width="4" height="12" fill="#D0C8B8" rx="1"/>',
    '<rect x="240" y="440" width="4" height="12" fill="#D0C8B8" rx="1"/>',
    # Tail
    '<path d="M209,430 Q203,425 204,420" stroke="#C8C0B0" stroke-width="2" fill="none" stroke-linecap="round"/>',
    # Spots
    '<ellipse cx="220" cy="426" rx="6" ry="5" fill="#2A2010" opacity="0.38"/>',
    '<ellipse cx="232" cy="432" rx="5" ry="4" fill="#2A2010" opacity="0.32"/>',
    # Udder
    '<ellipse cx="228" cy="441" rx="8" ry="3.5" fill="#F0A8A0" opacity="0.72"/>',

    # ══════════════════════════════════════════════════════════════════
    #  STAGE 10 SPECIAL: 石のアーチ門 Stone Gate  (x=200, y≈531)
    # ══════════════════════════════════════════════════════════════════
    '<g transform="translate(200,531) scale(1.5) translate(-200,-531)">',
    # Ground shadow
    '<ellipse cx="200" cy="565" rx="45" ry="8" fill="#145A14" opacity="0.35"/>',

    # Left stone pillar
    '<rect x="163" y="504" width="20" height="62" fill="#888078" rx="3"/>',
    # Left pillar stones
    '<rect x="163" y="508" width="20" height="7" fill="#989080" opacity="0.55"/>',
    '<rect x="163" y="518" width="20" height="7" fill="#7A7068" opacity="0.45"/>',
    '<rect x="163" y="528" width="20" height="7" fill="#989080" opacity="0.50"/>',
    '<rect x="163" y="538" width="20" height="7" fill="#7A7068" opacity="0.45"/>',
    '<rect x="163" y="548" width="20" height="7" fill="#989080" opacity="0.50"/>',
    # Left pillar cap
    '<rect x="160" y="501" width="26" height="6" fill="#707068" rx="2"/>',
    '<ellipse cx="173" cy="501" rx="13" ry="3" fill="#888080" opacity="0.60"/>',
    # Left pillar highlight
    '<rect x="165" y="504" width="5" height="62" fill="#A09888" opacity="0.28"/>',

    # Right stone pillar
    '<rect x="217" y="504" width="20" height="62" fill="#888078" rx="3"/>',
    # Right pillar stones
    '<rect x="217" y="508" width="20" height="7" fill="#989080" opacity="0.55"/>',
    '<rect x="217" y="518" width="20" height="7" fill="#7A7068" opacity="0.45"/>',
    '<rect x="217" y="528" width="20" height="7" fill="#989080" opacity="0.50"/>',
    '<rect x="217" y="538" width="20" height="7" fill="#7A7068" opacity="0.45"/>',
    '<rect x="217" y="548" width="20" height="7" fill="#989080" opacity="0.50"/>',
    # Right pillar cap
    '<rect x="214" y="501" width="26" height="6" fill="#707068" rx="2"/>',
    '<ellipse cx="227" cy="501" rx="13" ry="3" fill="#888080" opacity="0.60"/>',
    # Right pillar highlight
    '<rect x="219" y="504" width="5" height="62" fill="#A09888" opacity="0.28"/>',

    # Stone arch (keystones)
    '<path d="M163,510 Q200,478 237,510" stroke="#707068" stroke-width="12" fill="none" stroke-linecap="butt"/>',
    '<path d="M163,510 Q200,478 237,510" stroke="#888078" stroke-width="9" fill="none" stroke-linecap="butt"/>',
    # Arch highlight
    '<path d="M164,511 Q200,480 236,511" stroke="#A09888" stroke-width="3.5" fill="none" stroke-linecap="butt" opacity="0.40"/>',
    # Keystone (center top of arch)
    '<path d="M196,479 Q200,474 204,479 L202,488 L198,488 Z" fill="#706860"/>',

    # Ivy on left pillar
    '<path d="M163,540 Q158,530 161,520 Q156,510 160,502" stroke="#2E7020" stroke-width="2.5" fill="none" stroke-linecap="round"/>',
    '<ellipse cx="158" cy="528" rx="5.5" ry="4" fill="#3A8028" transform="rotate(-20,158,528)"/>',
    '<ellipse cx="161" cy="515" rx="5" ry="3.5" fill="#428A30" transform="rotate(-10,161,515)"/>',
    '<ellipse cx="160" cy="504" rx="4.5" ry="3" fill="#3A8028" transform="rotate(5,160,504)"/>',

    # Ivy on right pillar
    '<path d="M237,540 Q242,530 239,520 Q244,510 240,502" stroke="#2E7020" stroke-width="2.5" fill="none" stroke-linecap="round"/>',
    '<ellipse cx="242" cy="528" rx="5.5" ry="4" fill="#3A8028" transform="rotate(20,242,528)"/>',
    '<ellipse cx="239" cy="515" rx="5" ry="3.5" fill="#428A30" transform="rotate(10,239,515)"/>',
    '<ellipse cx="240" cy="504" rx="4.5" ry="3" fill="#3A8028" transform="rotate(-5,240,504)"/>',

    # Ivy on arch
    '<ellipse cx="182" cy="490" rx="5" ry="3.5" fill="#3A8028" transform="rotate(-35,182,490)"/>',
    '<ellipse cx="200" cy="480" rx="5.5" ry="3.8" fill="#428A30"/>',
    '<ellipse cx="218" cy="490" rx="5" ry="3.5" fill="#3A8028" transform="rotate(35,218,490)"/>',
    # Small flowers on ivy
    '<circle cx="160" cy="507" r="2.5" fill="#FFE870"/>',
    '<circle cx="200" cy="479" r="2.8" fill="#FFFFFF" opacity="0.88"/>',
    '<circle cx="240" cy="507" r="2.5" fill="#FFE870"/>',
    '</g>',

    # ── LAYER 6: FOREGROUND LARGE OAKS ───────────────────────────────
    # Left oak
    '<rect x="0" y="458" width="18" height="142" fill="#3A2210"/>',
    # Canopy layers
    '<ellipse cx="9" cy="440" rx="56" ry="42" fill="#236A1E" opacity="0.99"/>',
    '<ellipse cx="9" cy="414" rx="40" ry="30" fill="#2E8828" opacity="0.97"/>',
    '<ellipse cx="9" cy="392" rx="27" ry="19" fill="#3AA030" opacity="0.95"/>',
    '<ellipse cx="9" cy="374" rx="18" ry="12" fill="#48B034" opacity="0.90"/>',
    # Wide lower skirt (oak canopy drops low)
    '<ellipse cx="9" cy="488" rx="60" ry="26" fill="#226018"/>',
    '<ellipse cx="9" cy="534" rx="56" ry="22" fill="#205C16"/>',
    '<ellipse cx="9" cy="576" rx="54" ry="20" fill="#235E18"/>',
    '<ellipse cx="9" cy="604" rx="52" ry="18" fill="#266420"/>',
    # Right oak
    '<rect x="382" y="458" width="18" height="142" fill="#3A2210"/>',
    '<ellipse cx="391" cy="440" rx="56" ry="42" fill="#236A1E" opacity="0.99"/>',
    '<ellipse cx="391" cy="414" rx="40" ry="30" fill="#2E8828" opacity="0.97"/>',
    '<ellipse cx="391" cy="392" rx="27" ry="19" fill="#3AA030" opacity="0.95"/>',
    '<ellipse cx="391" cy="374" rx="18" ry="12" fill="#48B034" opacity="0.90"/>',
    '<ellipse cx="391" cy="488" rx="60" ry="26" fill="#226018"/>',
    '<ellipse cx="391" cy="534" rx="56" ry="22" fill="#205C16"/>',
    '<ellipse cx="391" cy="576" rx="54" ry="20" fill="#235E18"/>',
    '<ellipse cx="391" cy="604" rx="52" ry="18" fill="#266420"/>',

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
