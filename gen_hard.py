#!/usr/bin/env python3
"""HARD SVG masterpiece - Deep Dark Forest with Winding River."""
import re

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

def J(*parts):
    return ''.join(parts)

# ═══════════════════════════════════════════════════════════════════════
#  HARD  深い森  Deep Dark Forest  — MASTERPIECE
#  ・道なし（蛇行する川をpath要素で表現）
#  ・暗い深緑の密林、岩、霧、松の木、苔
#  ・Stage5 (y≈235, x=200): 大きな焚き火（丸太＋炎グロー）
#  ・Stage10 (y≈531, x=200): 滝＋洞窟入口（岩）
# ═══════════════════════════════════════════════════════════════════════

HARD = J(
    '<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">',
    '<defs>',

    # Sky — stormy dark teal, barely any sky visible
    '<linearGradient id="hSky" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#0C1E18"/>',
    '<stop offset="38%" stop-color="#102A20"/>',
    '<stop offset="72%" stop-color="#163424"/>',
    '<stop offset="100%" stop-color="#1A3C28"/>',
    '</linearGradient>',

    # Ground — dark mossy forest floor
    '<linearGradient id="hGnd" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#1C4A20"/>',
    '<stop offset="45%" stop-color="#143A18"/>',
    '<stop offset="100%" stop-color="#0A2410"/>',
    '</linearGradient>',

    # River water — dark teal
    '<linearGradient id="hRiv" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#2A6878"/>',
    '<stop offset="50%" stop-color="#1E5468"/>',
    '<stop offset="100%" stop-color="#163C50"/>',
    '</linearGradient>',

    # Campfire glow (radial, centered at stage5)
    '<radialGradient id="hFire" cx="50%" cy="50%" r="50%">',
    '<stop offset="0%" stop-color="#FF9020" stop-opacity="0.82"/>',
    '<stop offset="40%" stop-color="#FF6000" stop-opacity="0.40"/>',
    '<stop offset="70%" stop-color="#FF4000" stop-opacity="0.16"/>',
    '<stop offset="100%" stop-color="#FF4000" stop-opacity="0"/>',
    '</radialGradient>',

    # Cave/waterfall glow (subtle blue-white)
    '<radialGradient id="hWfall" cx="50%" cy="20%" r="60%">',
    '<stop offset="0%" stop-color="#A8DCF0" stop-opacity="0.55"/>',
    '<stop offset="100%" stop-color="#A8DCF0" stop-opacity="0"/>',
    '</radialGradient>',

    # Ground mist
    '<linearGradient id="hMist" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#8ABCB0" stop-opacity="0"/>',
    '<stop offset="60%" stop-color="#8ABCB0" stop-opacity="0.10"/>',
    '<stop offset="100%" stop-color="#8ABCB0" stop-opacity="0.28"/>',
    '</linearGradient>',

    # Depth overlay
    '<linearGradient id="hDpth" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#030E06" stop-opacity="0.72"/>',
    '<stop offset="18%" stop-color="#030E06" stop-opacity="0.06"/>',
    '<stop offset="100%" stop-color="#030E06" stop-opacity="0"/>',
    '</linearGradient>',

    # Rock gradient
    '<linearGradient id="hRock" x1="0" y1="0" x2="1" y2="1">',
    '<stop offset="0%" stop-color="#5A5A54"/>',
    '<stop offset="60%" stop-color="#3C3C38"/>',
    '<stop offset="100%" stop-color="#282824"/>',
    '</linearGradient>',

    # Pine tree gradient (dark)
    '<linearGradient id="hPine" x1="0" y1="0" x2="1" y2="0">',
    '<stop offset="0%" stop-color="#0C2A10"/>',
    '<stop offset="40%" stop-color="#183820"/>',
    '<stop offset="100%" stop-color="#0C2A10"/>',
    '</linearGradient>',

    '</defs>',

    # ── BASE LAYERS ──────────────────────────────────────────────────
    '<rect width="400" height="600" fill="url(#hSky)"/>',
    '<rect y="95" width="400" height="505" fill="url(#hGnd)"/>',

    # ── STORM CLOUDS (dark, oppressive) ──────────────────────────────
    '<ellipse cx="80" cy="28" rx="72" ry="22" fill="#1A2820" opacity="0.90"/>',
    '<ellipse cx="44" cy="32" rx="36" ry="16" fill="#162018" opacity="0.86"/>',
    '<ellipse cx="116" cy="33" rx="38" ry="17" fill="#1A2820" opacity="0.84"/>',
    '<ellipse cx="280" cy="20" rx="80" ry="25" fill="#182620" opacity="0.88"/>',
    '<ellipse cx="240" cy="24" rx="42" ry="18" fill="#142018" opacity="0.84"/>',
    '<ellipse cx="320" cy="22" rx="46" ry="19" fill="#1A2C20" opacity="0.84"/>',
    '<ellipse cx="200" cy="14" rx="30" ry="12" fill="#102018" opacity="0.76"/>',
    # Cloud undersides (slightly lighter)
    '<ellipse cx="80" cy="44" rx="68" ry="12" fill="#243A2C" opacity="0.50"/>',
    '<ellipse cx="280" cy="38" rx="76" ry="11" fill="#243A2C" opacity="0.48"/>',

    # ── DEPTH OVERLAY ────────────────────────────────────────────────
    '<rect width="400" height="600" fill="url(#hDpth)"/>',

    # ── ROLLING DARK HILLS (horizon) ─────────────────────────────────
    '<ellipse cx="60" cy="128" rx="130" ry="45" fill="#163A1C" opacity="0.82"/>',
    '<ellipse cx="220" cy="120" rx="160" ry="50" fill="#123416" opacity="0.76"/>',
    '<ellipse cx="374" cy="130" rx="135" ry="44" fill="#163A1C" opacity="0.80"/>',
    '<ellipse cx="150" cy="135" rx="95" ry="36" fill="#1A4020" opacity="0.62"/>',

    # ── LAYER 2: HORIZON PINE SILHOUETTES ────────────────────────────
    # Far left pines (triangular)
    '<polygon points="10,100 16,78 22,100" fill="#0C2010" opacity="0.92"/>',
    '<polygon points="20,102 27,76 34,102" fill="#0E2412" opacity="0.90"/>',
    '<polygon points="32,100 40,72 48,100" fill="#0C2010" opacity="0.92"/>',
    # Center-left pines
    '<polygon points="88,102 94,80 100,102" fill="#0C2010" opacity="0.90"/>',
    '<polygon points="98,100 105,75 112,100" fill="#0E2412" opacity="0.88"/>',
    # Center pines
    '<polygon points="172,102 178,80 184,102" fill="#0C2010" opacity="0.90"/>',
    '<polygon points="184,100 192,74 200,100" fill="#0E2412" opacity="0.88"/>',
    # Center-right pines
    '<polygon points="250,102 257,78 264,102" fill="#0C2010" opacity="0.90"/>',
    '<polygon points="262,100 269,76 276,100" fill="#0E2412" opacity="0.88"/>',
    # Right pines
    '<polygon points="330,102 337,78 344,102" fill="#0C2010" opacity="0.90"/>',
    '<polygon points="348,100 356,74 364,100" fill="#0E2412" opacity="0.88"/>',
    '<polygon points="370,102 378,76 386,102" fill="#0C2010" opacity="0.90"/>',

    # ── LAYER 3: FAR TREES (pines + deciduous mixed) ──────────────────
    # Far-left pine cluster
    '<polygon points="2,138 12,100 22,138" fill="#102818" opacity="0.94"/>',
    '<polygon points="12,135 24,92 36,135" fill="#143020" opacity="0.92"/>',
    '<polygon points="6,130 18,86 30,130" fill="#0E2416" opacity="0.94"/>',
    # Far-left deciduous
    '<rect x="34" y="124" width="2.5" height="30" fill="#0A1E0C"/>',
    '<ellipse cx="35.25" cy="120" rx="11" ry="10" fill="#163820" opacity="0.92"/>',
    '<ellipse cx="35.25" cy="112" rx="8" ry="7" fill="#1C4428" opacity="0.90"/>',
    # Center-left pines (taller)
    '<polygon points="72,142 84,96 96,142" fill="#102818" opacity="0.92"/>',
    '<polygon points="86,138 100,90 114,138" fill="#143020" opacity="0.90"/>',
    # Center-left deciduous
    '<rect x="116" y="120" width="2.4" height="34" fill="#0A1E0C"/>',
    '<ellipse cx="117.2" cy="116" rx="12" ry="10.5" fill="#163820" opacity="0.92"/>',
    '<ellipse cx="117.2" cy="107" rx="8.5" ry="7.5" fill="#1C4428" opacity="0.90"/>',
    # Center pines
    '<polygon points="148,140 162,90 176,140" fill="#102818" opacity="0.92"/>',
    # Center-right pines
    '<polygon points="218,140 232,92 246,140" fill="#102818" opacity="0.92"/>',
    '<polygon points="236,138 250,94 264,138" fill="#143020" opacity="0.90"/>',
    # Center-right deciduous
    '<rect x="268" y="120" width="2.4" height="34" fill="#0A1E0C"/>',
    '<ellipse cx="269.2" cy="116" rx="12" ry="10.5" fill="#163820" opacity="0.92"/>',
    '<ellipse cx="269.2" cy="107" rx="8.5" ry="7.5" fill="#1C4428" opacity="0.90"/>',
    # Far-right pines
    '<polygon points="306,142 320,96 334,142" fill="#102818" opacity="0.92"/>',
    '<polygon points="330,138 344,90 358,138" fill="#143020" opacity="0.90"/>',
    # Far-right deciduous
    '<rect x="358" y="124" width="2.5" height="30" fill="#0A1E0C"/>',
    '<ellipse cx="359.25" cy="120" rx="11" ry="10" fill="#163820" opacity="0.92"/>',
    '<ellipse cx="359.25" cy="112" rx="8" ry="7" fill="#1C4428" opacity="0.90"/>',
    '<polygon points="368,138 380,96 392,138" fill="#102818" opacity="0.94"/>',
    '<polygon points="380,140 394,94 400,140" fill="#0E2416" opacity="0.96"/>',

    # ── WINDING RIVER (path element, not polygon) ─────────────────────
    # River shadow/depth
    '<path d="M218,0 Q208,30 214,65 Q220,100 204,140 Q188,180 196,218 Q204,258 186,298 Q168,338 180,378 Q192,418 174,458 Q156,498 168,540 Q178,572 172,600" stroke="#102830" stroke-width="58" fill="none" stroke-linecap="round"/>',
    # River main water
    '<path d="M218,0 Q208,30 214,65 Q220,100 204,140 Q188,180 196,218 Q204,258 186,298 Q168,338 180,378 Q192,418 174,458 Q156,498 168,540 Q178,572 172,600" stroke="#1E5868" stroke-width="48" fill="none" stroke-linecap="round"/>',
    # River surface (lighter teal)
    '<path d="M218,0 Q208,30 214,65 Q220,100 204,140 Q188,180 196,218 Q204,258 186,298 Q168,338 180,378 Q192,418 174,458 Q156,498 168,540 Q178,572 172,600" stroke="#2A7090" stroke-width="36" fill="none" stroke-linecap="round"/>',
    # River highlight (center shimmer)
    '<path d="M216,0 Q206,32 212,68 Q218,104 202,144 Q186,184 194,222 Q202,262 184,302 Q166,342 178,382 Q190,422 172,462 Q154,502 166,542 Q176,574 170,600" stroke="#4A9EB8" stroke-width="12" fill="none" stroke-linecap="round" opacity="0.55"/>',
    # Rapids (white foam at bends)
    '<path d="M204,140 Q196,148 200,156" stroke="#C8E8F0" stroke-width="6" fill="none" stroke-linecap="round" opacity="0.60"/>',
    '<path d="M186,296 Q178,304 182,312" stroke="#C8E8F0" stroke-width="6" fill="none" stroke-linecap="round" opacity="0.60"/>',
    '<path d="M174,456 Q166,464 170,472" stroke="#C8E8F0" stroke-width="6" fill="none" stroke-linecap="round" opacity="0.60"/>',
    # River ripples (short dashes)
    '<path d="M210,40 Q206,45 212,50" stroke="#5AAAC0" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.45"/>',
    '<path d="M198,170 Q194,176 200,182" stroke="#5AAAC0" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.45"/>',
    '<path d="M182,340 Q178,346 184,352" stroke="#5AAAC0" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.45"/>',

    # ── ROCKS & BOULDERS (scattered) ──────────────────────────────────
    # Left bank rocks (near river)
    '<ellipse cx="168" cy="155" rx="14" ry="9" fill="url(#hRock)"/>',
    '<ellipse cx="158" cy="160" rx="10" ry="7" fill="#484844"/>',
    '<ellipse cx="178" cy="162" rx="8" ry="6" fill="#3C3C38"/>',
    # Moss on rocks
    '<ellipse cx="165" cy="151" rx="6" ry="3" fill="#2A5C28" opacity="0.68"/>',
    '<ellipse cx="175" cy="157" rx="5" ry="2.5" fill="#2A5C28" opacity="0.60"/>',

    # Right side rocks
    '<ellipse cx="278" cy="320" rx="18" ry="12" fill="url(#hRock)"/>',
    '<ellipse cx="265" cy="326" rx="12" ry="8" fill="#484844"/>',
    '<ellipse cx="290" cy="328" rx="10" ry="7" fill="#3C3C38"/>',
    # Moss
    '<ellipse cx="274" cy="315" rx="8" ry="4" fill="#2A5C28" opacity="0.65"/>',

    # Near-river rocks (left of river bend)
    '<ellipse cx="230" cy="290" rx="12" ry="8" fill="url(#hRock)"/>',
    '<ellipse cx="222" cy="295" rx="8" ry="5.5" fill="#484844"/>',
    # Moss
    '<ellipse cx="227" cy="286" rx="5" ry="2.5" fill="#2A5C28" opacity="0.60"/>',

    # Small pebbles near river
    '<ellipse cx="240" cy="180" rx="6" ry="4" fill="#505050"/>',
    '<ellipse cx="232" cy="185" rx="4" ry="3" fill="#484844"/>',
    '<ellipse cx="158" cy="420" rx="7" ry="4.5" fill="#505050"/>',
    '<ellipse cx="150" cy="425" rx="5" ry="3" fill="#484844"/>',

    # ── GLOWING MUSHROOMS (scattered) ────────────────────────────────
    # Left side mushrooms
    '<ellipse cx="62" cy="350" rx="7" ry="3.5" fill="#D04080" opacity="0.90"/>',
    '<rect x="59.5" y="350" width="5" height="9" fill="#A03060" opacity="0.85"/>',
    '<ellipse cx="62" cy="350" rx="4" ry="1.5" fill="#FF88B8" opacity="0.50"/>',
    # Glow
    '<ellipse cx="62" cy="352" rx="12" ry="8" fill="#FF60A0" opacity="0.20"/>',

    '<ellipse cx="80" cy="480" rx="6" ry="3" fill="#D04080" opacity="0.88"/>',
    '<rect x="77.5" y="480" width="5" height="8" fill="#A03060" opacity="0.82"/>',
    '<ellipse cx="80" cy="480" rx="3.5" ry="1.2" fill="#FF88B8" opacity="0.48"/>',
    '<ellipse cx="80" cy="482" rx="10" ry="6" fill="#FF60A0" opacity="0.18"/>',

    # Right side mushrooms
    '<ellipse cx="338" cy="380" rx="7" ry="3.5" fill="#D04080" opacity="0.90"/>',
    '<rect x="335" y="380" width="6" height="9" fill="#A03060" opacity="0.85"/>',
    '<ellipse cx="338" cy="380" rx="4" ry="1.5" fill="#FF88B8" opacity="0.50"/>',
    '<ellipse cx="338" cy="382" rx="12" ry="8" fill="#FF60A0" opacity="0.20"/>',

    '<ellipse cx="312" cy="500" rx="5.5" ry="2.8" fill="#C03870" opacity="0.88"/>',
    '<rect x="309.5" y="500" width="5" height="8" fill="#903060" opacity="0.82"/>',
    '<ellipse cx="312" cy="500" rx="3" ry="1.2" fill="#FF80B0" opacity="0.48"/>',

    # ── LAYER 4: MID FOREST TREES ─────────────────────────────────────
    # Left large pines
    '<polygon points="-6,228 12,158 30,228" fill="url(#hPine)" opacity="0.96"/>',
    '<polygon points="22,222 42,148 62,222" fill="#102818" opacity="0.95"/>',
    '<polygon points="6,218 28,140 50,218" fill="#0E2416" opacity="0.95"/>',
    # Left-center pine
    '<polygon points="68,232 86,164 104,232" fill="#102818" opacity="0.93"/>',
    '<rect x="86" y="224" width="5" height="35" fill="#081408"/>',
    # Center-left deciduous
    '<rect x="112" y="190" width="5" height="55" fill="#081408"/>',
    '<ellipse cx="114.5" cy="183" rx="20" ry="16" fill="#183A1E" opacity="0.95"/>',
    '<ellipse cx="114.5" cy="170" rx="14" ry="11" fill="#204A28" opacity="0.93"/>',
    '<ellipse cx="114.5" cy="160" rx="9" ry="7" fill="#285C30" opacity="0.90"/>',

    # Right-center deciduous (avoid stage 5 at y=235, x=200)
    '<rect x="280" y="190" width="5" height="55" fill="#081408"/>',
    '<ellipse cx="282.5" cy="183" rx="20" ry="16" fill="#183A1E" opacity="0.95"/>',
    '<ellipse cx="282.5" cy="170" rx="14" ry="11" fill="#204A28" opacity="0.93"/>',
    '<ellipse cx="282.5" cy="160" rx="9" ry="7" fill="#285C30" opacity="0.90"/>',
    # Right pines
    '<polygon points="296,232 316,158 336,232" fill="#102818" opacity="0.95"/>',
    '<polygon points="326,228 346,152 366,228" fill="#0E2416" opacity="0.95"/>',
    '<polygon points="358,230 378,156 398,230" fill="#102818" opacity="0.96"/>',
    '<rect x="316" y="224" width="5" height="35" fill="#081408"/>',
    '<rect x="346" y="222" width="5" height="36" fill="#081408"/>',

    # ══════════════════════════════════════════════════════════════════
    #  STAGE 5 SPECIAL: 大きな焚き火  Campfire  (右岸 x≈252, y≈235)
    # ══════════════════════════════════════════════════════════════════
    # Shift entire campfire to right bank (+52 from river center)
    '<g transform="translate(52,0)">',
    # Campfire glow circle (wide warm radial)
    '<ellipse cx="200" cy="255" rx="55" ry="32" fill="#FF8020" opacity="0.18"/>',
    '<ellipse cx="200" cy="258" rx="38" ry="22" fill="#FF6000" opacity="0.22"/>',
    '<ellipse cx="200" cy="260" rx="24" ry="14" fill="#FF4800" opacity="0.25"/>',
    # Ground glow (lit earth)
    '<ellipse cx="200" cy="268" rx="28" ry="8" fill="#FF8020" opacity="0.28"/>',
    # Log ring (3 crossing logs)
    '<rect x="176" y="260" width="48" height="7" fill="#3A2010" rx="3" transform="rotate(-18,200,263)"/>',
    '<rect x="176" y="260" width="48" height="7" fill="#3A2010" rx="3" transform="rotate(18,200,263)"/>',
    '<rect x="176" y="260" width="48" height="7" fill="#2A1808" rx="3"/>',
    # Log texture lines
    '<path d="M178,265 Q188,263 198,264" stroke="#5A3010" stroke-width="0.8" fill="none" opacity="0.50"/>',
    '<path d="M202,264 Q212,263 222,265" stroke="#5A3010" stroke-width="0.8" fill="none" opacity="0.50"/>',
    # Ember bed
    '<ellipse cx="200" cy="268" rx="18" ry="5" fill="#FF4000" opacity="0.75"/>',
    '<ellipse cx="200" cy="268" rx="12" ry="3.5" fill="#FF7000" opacity="0.85"/>',
    # Embers (glowing dots)
    '<circle cx="196" cy="265" r="1.5" fill="#FF8020" opacity="0.90"/>',
    '<circle cx="204" cy="264" r="1.5" fill="#FFA030" opacity="0.88"/>',
    '<circle cx="200" cy="262" r="1.2" fill="#FFB040" opacity="0.85"/>',
    '<circle cx="193" cy="260" r="1" fill="#FF6010" opacity="0.80"/>',
    '<circle cx="208" cy="260" r="1" fill="#FF6010" opacity="0.80"/>',
    # Flames — back layer (dark orange)
    '<path d="M192,262 Q188,250 194,240 Q196,230 190,218 Q196,228 200,238 Q203,226 198,212 Q205,224 202,238 Q208,226 204,214 Q212,228 206,242 Q212,252 208,262" fill="#FF4800" opacity="0.88"/>',
    # Flames — mid layer (orange)
    '<path d="M194,262 Q190,248 197,237 Q199,226 194,216 Q200,227 201,240 Q205,227 201,215 Q208,228 204,240 Q210,250 206,262" fill="#FF7010" opacity="0.90"/>',
    # Flames — front layer (yellow-orange)
    '<path d="M196,262 Q192,250 198,240 Q201,230 198,222 Q203,232 202,244 Q206,234 203,222 Q209,234 206,244 Q210,252 206,262" fill="#FFA020" opacity="0.85"/>',
    # Flame tips (bright yellow)
    '<path d="M198,252 Q197,242 200,234 Q202,242 201,252" fill="#FFD040" opacity="0.82"/>',
    '<path d="M200,248 Q199,240 201,234 Q203,240 202,248" fill="#FFE870" opacity="0.78"/>',
    # Sparks
    '<circle cx="196" cy="228" r="1.2" fill="#FFE060" opacity="0.80"/>',
    '<circle cx="205" cy="224" r="1" fill="#FFE060" opacity="0.76"/>',
    '<circle cx="192" cy="220" r="0.9" fill="#FFC040" opacity="0.72"/>',
    '<circle cx="210" cy="218" r="0.9" fill="#FFC040" opacity="0.70"/>',
    '<circle cx="200" cy="214" r="1.1" fill="#FFE060" opacity="0.78"/>',
    # Smoke (dark wisp)
    '<path d="M200,212 Q196,202 200,192 Q204,182 200,172" stroke="#2A3028" stroke-width="4" fill="none" stroke-linecap="round" opacity="0.50"/>',
    '<path d="M200,212 Q204,200 202,188" stroke="#2A3028" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.35"/>',
    # Stones around fire pit
    '<ellipse cx="182" cy="270" rx="6" ry="3.5" fill="#484840"/>',
    '<ellipse cx="200" cy="274" rx="6" ry="3" fill="#484840"/>',
    '<ellipse cx="218" cy="270" rx="6" ry="3.5" fill="#484840"/>',
    '<ellipse cx="188" cy="273" rx="4.5" ry="2.8" fill="#3C3C38"/>',
    '<ellipse cx="212" cy="273" rx="4.5" ry="2.8" fill="#3C3C38"/>',
    # Ground illuminated by fire (warm circle)
    '<ellipse cx="200" cy="280" rx="42" ry="15" fill="#FF6010" opacity="0.12"/>',
    '</g>',

    # ── LAYER 5: NEAR-MID TREES ────────────────────────────────────────
    # Far-left pine (large)
    '<polygon points="-8,350 18,254 44,350" fill="url(#hPine)" opacity="0.98"/>',
    '<rect x="15" y="340" width="7" height="75" fill="#060E08"/>',
    # Second-left pines
    '<polygon points="36,348 64,250 92,348" fill="#0E2414" opacity="0.96"/>',
    '<rect x="61" y="338" width="7" height="72" fill="#060E08"/>',
    # Left deciduous (near)
    '<rect x="118" y="318" width="7.5" height="98" fill="#081008"/>',
    '<ellipse cx="121.75" cy="307" rx="30" ry="23" fill="#163A1E" opacity="0.98"/>',
    '<ellipse cx="121.75" cy="288" rx="20" ry="16" fill="#1E4C28" opacity="0.96"/>',
    '<ellipse cx="121.75" cy="274" rx="13" ry="10" fill="#265E30" opacity="0.93"/>',
    # Right deciduous (near)
    '<rect x="274" y="318" width="7.5" height="98" fill="#081008"/>',
    '<ellipse cx="277.75" cy="307" rx="30" ry="23" fill="#163A1E" opacity="0.98"/>',
    '<ellipse cx="277.75" cy="288" rx="20" ry="16" fill="#1E4C28" opacity="0.96"/>',
    '<ellipse cx="277.75" cy="274" rx="13" ry="10" fill="#265E30" opacity="0.93"/>',
    # Second-right pines
    '<polygon points="304,348 332,250 360,348" fill="#0E2414" opacity="0.96"/>',
    '<rect x="329" y="338" width="7" height="72" fill="#060E08"/>',
    # Far-right pine (large)
    '<polygon points="356,350 382,254 408,350" fill="url(#hPine)" opacity="0.98"/>',
    '<rect x="379" y="340" width="7" height="75" fill="#060E08"/>',

    # ── FOREST FLOOR DETAILS ──────────────────────────────────────────
    # Ferns (left side)
    '<path d="M48,440 Q38,428 30,418" stroke="#1E4E1A" stroke-width="2.8" fill="none" stroke-linecap="round"/>',
    '<path d="M48,440 Q42,426 36,414" stroke="#244E20" stroke-width="1.8" fill="none" stroke-linecap="round" opacity="0.80"/>',
    '<path d="M48,440 Q55,428 62,420" stroke="#1E4E1A" stroke-width="2.8" fill="none" stroke-linecap="round"/>',
    '<path d="M48,440 Q56,426 63,416" stroke="#244E20" stroke-width="1.8" fill="none" stroke-linecap="round" opacity="0.80"/>',
    '<path d="M48,440 Q46,424 47,410" stroke="#1E4E1A" stroke-width="2.5" fill="none" stroke-linecap="round"/>',
    # Ferns (right side)
    '<path d="M352,460 Q342,448 334,438" stroke="#1E4E1A" stroke-width="2.8" fill="none" stroke-linecap="round"/>',
    '<path d="M352,460 Q360,448 367,440" stroke="#1E4E1A" stroke-width="2.8" fill="none" stroke-linecap="round"/>',
    '<path d="M352,460 Q350,444 351,430" stroke="#1E4E1A" stroke-width="2.5" fill="none" stroke-linecap="round"/>',

    # Fallen log (left)
    '<rect x="55" y="485" width="80" height="10" fill="#2A1A0C" rx="4" transform="rotate(-8,95,490)"/>',
    '<rect x="56" y="485" width="30" height="4" fill="#382210" rx="2" transform="rotate(-8,71,487)" opacity="0.60"/>',
    '<ellipse cx="55" cy="489" rx="6" ry="5" fill="#241808"/>',
    '<ellipse cx="135" cy="481" rx="6" ry="5" fill="#241808" transform="rotate(-8,135,481)"/>',
    # Moss on log
    '<ellipse cx="85" cy="484" rx="14" ry="4" fill="#2A5820" opacity="0.60" transform="rotate(-8,85,484)"/>',

    # Fallen log (right)
    '<rect x="265" y="510" width="75" height="9" fill="#2A1A0C" rx="4" transform="rotate(6,302,514)"/>',
    '<ellipse cx="265" cy="513" rx="5" ry="4.5" fill="#241808"/>',
    '<ellipse cx="340" cy="516" rx="5" ry="4.5" fill="#241808" transform="rotate(6,340,516)"/>',
    '<ellipse cx="295" cy="510" rx="12" ry="3.5" fill="#2A5820" opacity="0.58" transform="rotate(6,295,510)"/>',

    # ══════════════════════════════════════════════════════════════════
    #  STAGE 10 SPECIAL: 滝＋洞窟  Waterfall + Cave  (x=200, y≈531)
    # ══════════════════════════════════════════════════════════════════
    '<g transform="translate(200,531) scale(1.5) translate(-200,-531)">',
    # Rocky cliff face behind cave
    '<ellipse cx="200" cy="510" rx="52" ry="38" fill="#3C3C38"/>',
    '<ellipse cx="200" cy="514" rx="48" ry="34" fill="#464640"/>',
    '<ellipse cx="200" cy="518" rx="44" ry="30" fill="#424240"/>',
    # Cliff rock texture
    '<path d="M160,498 Q172,492 182,498 Q190,494 198,498" stroke="#505050" stroke-width="2" fill="none" opacity="0.45"/>',
    '<path d="M202,496 Q210,492 220,497 Q230,493 240,498" stroke="#505050" stroke-width="2" fill="none" opacity="0.45"/>',
    '<path d="M162,508 Q174,504 186,508 Q194,505 200,508" stroke="#484848" stroke-width="1.5" fill="none" opacity="0.40"/>',
    '<path d="M200,507 Q206,504 218,508 Q228,505 238,508" stroke="#484848" stroke-width="1.5" fill="none" opacity="0.40"/>',
    # Moss on cliff
    '<ellipse cx="168" cy="504" rx="10" ry="5" fill="#264E1E" opacity="0.65"/>',
    '<ellipse cx="232" cy="506" rx="9" ry="4.5" fill="#264E1E" opacity="0.60"/>',
    '<ellipse cx="200" cy="498" rx="8" ry="4" fill="#264E1E" opacity="0.55"/>',

    # Cave opening (dark ellipse)
    '<ellipse cx="200" cy="530" rx="28" ry="22" fill="#080C0A"/>',
    '<ellipse cx="200" cy="532" rx="24" ry="19" fill="#060A08"/>',
    '<ellipse cx="200" cy="534" rx="20" ry="16" fill="#040806"/>',
    # Cave inner glow (mysterious blue-green)
    '<ellipse cx="200" cy="534" rx="14" ry="10" fill="#0C3028" opacity="0.70"/>',
    '<ellipse cx="200" cy="536" rx="8" ry="6" fill="#1A5040" opacity="0.55"/>',
    # Cave rim stones (arch-like)
    '<path d="M172,530 Q200,506 228,530" stroke="#3C3C38" stroke-width="6" fill="none" stroke-linecap="round"/>',
    '<path d="M172,530 Q200,508 228,530" stroke="#505050" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.50"/>',

    # Waterfall (left of cave, flowing down cliff)
    # Main fall stream
    '<path d="M178,490 Q174,500 176,510 Q178,520 174,530 Q170,540 172,552" stroke="#A8D8E8" stroke-width="10" fill="none" stroke-linecap="round" opacity="0.72"/>',
    '<path d="M178,490 Q174,500 176,510 Q178,520 174,530 Q170,540 172,552" stroke="#C8EEF8" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.58"/>',
    # Waterfall spray streams
    '<path d="M181,492 Q177,502 179,514 Q181,524 177,534" stroke="#B8E2F0" stroke-width="4" fill="none" stroke-linecap="round" opacity="0.50"/>',
    '<path d="M175,494 Q171,505 173,516" stroke="#C0E8F4" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.42"/>',
    # Waterfall mist pool at base
    '<ellipse cx="172" cy="555" rx="18" ry="7" fill="#A8D8E8" opacity="0.48"/>',
    '<ellipse cx="172" cy="555" rx="10" ry="4" fill="#C8EEF8" opacity="0.55"/>',
    # Waterfall glow
    '<ellipse cx="178" cy="520" rx="18" ry="30" fill="url(#hWfall)" opacity="0.70"/>',

    # Cliff base rocks
    '<ellipse cx="152" cy="548" rx="16" ry="10" fill="#3C3C38"/>',
    '<ellipse cx="145" cy="552" rx="10" ry="7" fill="#484840"/>',
    '<ellipse cx="162" cy="554" rx="9" ry="6" fill="#3A3A36"/>',
    '<ellipse cx="248" cy="546" rx="15" ry="9" fill="#3C3C38"/>',
    '<ellipse cx="258" cy="550" rx="10" ry="7" fill="#484840"/>',
    # Rock moss
    '<ellipse cx="150" cy="544" rx="7" ry="3.5" fill="#264E1E" opacity="0.62"/>',
    '<ellipse cx="252" cy="542" rx="6" ry="3" fill="#264E1E" opacity="0.58"/>',
    '</g>',

    # ── GROUND MIST OVERLAY ───────────────────────────────────────────
    '<rect y="480" width="400" height="120" fill="url(#hMist)" opacity="0.75"/>',
    '<rect y="550" width="400" height="50" fill="#8ABCB0" opacity="0.10"/>',

    # ── LAYER 6: FOREGROUND GIANT PINES ──────────────────────────────
    # Left giant pine
    '<polygon points="-20,600 16,440 52,600" fill="#0A1E10" opacity="0.99"/>',
    '<polygon points="-10,590 16,460 42,590" fill="#122818" opacity="0.95"/>',
    '<polygon points="0,580 16,480 32,580" fill="#183020" opacity="0.90"/>',
    '<rect x="12" y="580" width="9" height="20" fill="#060E06"/>',
    # Left canopy skirt (covers trunk base)
    '<ellipse cx="16" cy="595" rx="46" ry="18" fill="#0E2214"/>',
    '<ellipse cx="0" cy="605" rx="38" ry="15" fill="#0A1E10"/>',

    # Right giant pine
    '<polygon points="348,600 384,440 420,600" fill="#0A1E10" opacity="0.99"/>',
    '<polygon points="358,590 384,460 410,590" fill="#122818" opacity="0.95"/>',
    '<polygon points="368,580 384,480 400,580" fill="#183020" opacity="0.90"/>',
    '<rect x="379" y="580" width="9" height="20" fill="#060E06"/>',
    # Right canopy skirt
    '<ellipse cx="384" cy="595" rx="46" ry="18" fill="#0E2214"/>',
    '<ellipse cx="400" cy="605" rx="38" ry="15" fill="#0A1E10"/>',

    '</svg>',
)

# ── inject helper ─────────────────────────────────────────────────────
def inject(html, diff, svg_str):
    pattern = rf"(if\(diff==='{diff}'\) return ')(.*?)(';)"
    def replacer(m):
        return m.group(1) + svg_str + m.group(3)
    new_html = re.sub(pattern, replacer, html, flags=re.DOTALL)
    return new_html

content = inject(content, 'HARD', HARD)

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('HARD injected OK —', len(HARD), 'chars')
