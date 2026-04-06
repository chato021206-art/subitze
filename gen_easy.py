#!/usr/bin/env python3
"""EASY SVG masterpiece - Spring Meadow. No center path. Full-width nature."""
import re

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

def J(*parts):
    return ''.join(parts)

# ═══════════════════════════════════════════════════════════════════════
#  EASY  春の野原  Golden Spring Meadow  — MASTERPIECE
#  ・中央の道なし（全幅を自然で覆う）
#  ・空、雲、太陽光、6層の木々、野草、蝶、兎、鳥
#  ・Stage5 (y≈235, x=200): 桜の木
#  ・Stage10 (y≈531, x=200): 花のアーチゲート
# ═══════════════════════════════════════════════════════════════════════

EASY = J(
    '<svg viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">',
    '<defs>',

    # Sky gradient: cornflower blue → pale → horizon green
    '<linearGradient id="eSky" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#5AB0EC"/>',
    '<stop offset="40%" stop-color="#90CCF4"/>',
    '<stop offset="72%" stop-color="#C8E8F8"/>',
    '<stop offset="100%" stop-color="#D8F2C0"/>',
    '</linearGradient>',

    # Ground gradient: lush green → dark green
    '<linearGradient id="eGnd" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#4ACC40"/>',
    '<stop offset="45%" stop-color="#34A030"/>',
    '<stop offset="100%" stop-color="#1A5C18"/>',
    '</linearGradient>',

    # Sun glow (top-right radial)
    '<radialGradient id="eSun" cx="82%" cy="5%" r="42%">',
    '<stop offset="0%" stop-color="#FFF8C0" stop-opacity="0.88"/>',
    '<stop offset="38%" stop-color="#FFE860" stop-opacity="0.30"/>',
    '<stop offset="100%" stop-color="#FFF8C0" stop-opacity="0"/>',
    '</radialGradient>',

    # Ambient ground warmth (center-bottom)
    '<radialGradient id="eWarm" cx="50%" cy="85%" r="50%">',
    '<stop offset="0%" stop-color="#D8F060" stop-opacity="0.14"/>',
    '<stop offset="100%" stop-color="#D8F060" stop-opacity="0"/>',
    '</radialGradient>',

    # Depth fog (very top — forest shadow)
    '<linearGradient id="eDpth" x1="0" y1="0" x2="0" y2="1">',
    '<stop offset="0%" stop-color="#041A04" stop-opacity="0.58"/>',
    '<stop offset="16%" stop-color="#041A04" stop-opacity="0.04"/>',
    '<stop offset="100%" stop-color="#041A04" stop-opacity="0"/>',
    '</linearGradient>',

    # Cherry blossom petal gradient
    '<radialGradient id="ePetal" cx="40%" cy="35%" r="65%">',
    '<stop offset="0%" stop-color="#FFE0F0"/>',
    '<stop offset="100%" stop-color="#FF88BC"/>',
    '</radialGradient>',

    # Gate wood gradient
    '<linearGradient id="eGate" x1="0" y1="0" x2="1" y2="0">',
    '<stop offset="0%" stop-color="#6A4820"/>',
    '<stop offset="35%" stop-color="#9A7040"/>',
    '<stop offset="100%" stop-color="#6A4820"/>',
    '</linearGradient>',

    '</defs>',

    # ── SKY & GROUND BASE ────────────────────────────────────────────
    '<rect width="400" height="600" fill="url(#eSky)"/>',
    '<rect y="115" width="400" height="485" fill="url(#eGnd)"/>',

    # ── CLOUDS ───────────────────────────────────────────────────────
    # Cloud A (left)
    '<ellipse cx="82" cy="34" rx="42" ry="15" fill="#FFFFFF" opacity="0.88"/>',
    '<ellipse cx="56" cy="37" rx="24" ry="12" fill="#FFFFFF" opacity="0.82"/>',
    '<ellipse cx="108" cy="38" rx="22" ry="11" fill="#FFFFFF" opacity="0.80"/>',
    '<ellipse cx="82" cy="29" rx="26" ry="10" fill="#FFFFFF" opacity="0.70"/>',
    # Cloud B (right-center)
    '<ellipse cx="268" cy="20" rx="48" ry="17" fill="#FFFFFF" opacity="0.84"/>',
    '<ellipse cx="238" cy="24" rx="26" ry="13" fill="#FFFFFF" opacity="0.78"/>',
    '<ellipse cx="298" cy="23" rx="28" ry="13" fill="#FFFFFF" opacity="0.78"/>',
    # Cloud C (small, far)
    '<ellipse cx="178" cy="12" rx="22" ry="8" fill="#FFFFFF" opacity="0.65"/>',

    # ── SUN GLOW OVERLAY ─────────────────────────────────────────────
    '<rect width="400" height="600" fill="url(#eSun)"/>',

    # ── ROLLING HILLS (horizon backdrop) ─────────────────────────────
    '<ellipse cx="55" cy="148" rx="115" ry="40" fill="#52CC4C" opacity="0.78"/>',
    '<ellipse cx="215" cy="142" rx="148" ry="46" fill="#4EC846" opacity="0.72"/>',
    '<ellipse cx="368" cy="150" rx="120" ry="38" fill="#56CE50" opacity="0.76"/>',
    '<ellipse cx="150" cy="155" rx="80" ry="30" fill="#58D054" opacity="0.60"/>',
    '<ellipse cx="310" cy="158" rx="75" ry="28" fill="#4CC848" opacity="0.58"/>',

    # Ground warmth overlay
    '<rect y="115" width="400" height="485" fill="url(#eWarm)"/>',
    # Depth fog overlay
    '<rect width="400" height="600" fill="url(#eDpth)"/>',

    # ── BIRDS (sky) ───────────────────────────────────────────────────
    '<path d="M46,30 Q51,25 56,30" stroke="#2A5820" stroke-width="1.4" fill="none"/>',
    '<path d="M61,24 Q66,19 71,24" stroke="#2A5820" stroke-width="1.2" fill="none"/>',
    '<path d="M168,12 Q173,7 178,12" stroke="#2A5820" stroke-width="1.1" fill="none"/>',
    '<path d="M288,16 Q293,11 298,16" stroke="#2A5820" stroke-width="1.2" fill="none"/>',
    '<path d="M306,28 Q311,23 316,28" stroke="#2A5820" stroke-width="1.4" fill="none"/>',

    # ── LAYER 1: HORIZON MICRO-TREES (y≈115-122) ─────────────────────
    '<circle cx="28" cy="118" r="5" fill="#1A5010" opacity="0.76"/>',
    '<circle cx="42" cy="116" r="4" fill="#1E5814" opacity="0.72"/>',
    '<circle cx="128" cy="118" r="5.5" fill="#1A5010" opacity="0.74"/>',
    '<circle cx="200" cy="117" r="4.5" fill="#1C5412" opacity="0.70"/>',
    '<circle cx="278" cy="118" r="5" fill="#1A5010" opacity="0.74"/>',
    '<circle cx="362" cy="117" r="5.5" fill="#1E5814" opacity="0.72"/>',
    '<circle cx="380" cy="119" r="4" fill="#1A5010" opacity="0.70"/>',

    # ── LAYER 2: VERY FAR TREES (y≈105-135) ──────────────────────────
    # Left side
    '<rect x="16" y="108" width="1.8" height="22" fill="#112606"/>',
    '<circle cx="16.9" cy="107" r="7.5" fill="#1C5414" opacity="0.92"/>',
    '<circle cx="16.9" cy="100" r="5.8" fill="#256220" opacity="0.90"/>',
    '<rect x="36" y="111" width="1.5" height="19" fill="#112606"/>',
    '<circle cx="36.75" cy="110" r="6.2" fill="#1A5010" opacity="0.90"/>',
    '<circle cx="36.75" cy="104" r="4.8" fill="#235C1C" opacity="0.88"/>',
    # Center-left far
    '<rect x="112" y="109" width="1.8" height="21" fill="#112606"/>',
    '<circle cx="112.9" cy="108" r="7" fill="#1C5414" opacity="0.90"/>',
    '<circle cx="112.9" cy="101" r="5.5" fill="#256020" opacity="0.88"/>',
    # Center far (slightly off-center)
    '<rect x="188" y="110" width="1.6" height="20" fill="#112606"/>',
    '<circle cx="188.8" cy="109" r="6.5" fill="#1A5010" opacity="0.88"/>',
    '<circle cx="188.8" cy="103" r="5" fill="#235C1C" opacity="0.86"/>',
    # Center-right far
    '<rect x="268" y="109" width="1.8" height="21" fill="#112606"/>',
    '<circle cx="268.9" cy="108" r="7" fill="#1C5414" opacity="0.90"/>',
    '<circle cx="268.9" cy="101" r="5.5" fill="#256020" opacity="0.88"/>',
    # Right side
    '<rect x="344" y="108" width="1.8" height="22" fill="#112606"/>',
    '<circle cx="344.9" cy="107" r="7.5" fill="#1C5414" opacity="0.92"/>',
    '<circle cx="344.9" cy="100" r="5.8" fill="#256220" opacity="0.90"/>',
    '<rect x="368" y="111" width="1.5" height="19" fill="#112606"/>',
    '<circle cx="368.75" cy="110" r="6.2" fill="#1A5010" opacity="0.90"/>',
    '<circle cx="368.75" cy="104" r="4.8" fill="#235C1C" opacity="0.88"/>',

    # ── LAYER 3: FAR TREES (y≈120-160) ───────────────────────────────
    # Far-left cluster
    '<rect x="4" y="128" width="2.6" height="32" fill="#162C0A"/>',
    '<circle cx="5.3" cy="125" r="10.5" fill="#246820" opacity="0.94"/>',
    '<circle cx="5.3" cy="115" r="8" fill="#2E7828" opacity="0.92"/>',
    '<circle cx="5.3" cy="108" r="5.5" fill="#388A32" opacity="0.88"/>',
    '<rect x="24" y="131" width="2.3" height="29" fill="#162C0A"/>',
    '<circle cx="25.15" cy="128" r="9.5" fill="#226418" opacity="0.92"/>',
    '<circle cx="25.15" cy="119" r="7" fill="#2C7222" opacity="0.90"/>',
    # Far center-left
    '<rect x="86" y="130" width="2.5" height="30" fill="#162C0A"/>',
    '<circle cx="87.25" cy="127" r="10" fill="#246820" opacity="0.92"/>',
    '<circle cx="87.25" cy="118" r="7.5" fill="#2E7828" opacity="0.90"/>',
    # Far center (y≈132, x=175 — offset from stage5 center)
    '<rect x="172" y="132" width="2.3" height="28" fill="#162C0A"/>',
    '<circle cx="173.15" cy="129" r="9.5" fill="#226418" opacity="0.90"/>',
    '<circle cx="173.15" cy="120" r="7" fill="#2C7222" opacity="0.88"/>',
    # Far center-right
    '<rect x="252" y="130" width="2.5" height="30" fill="#162C0A"/>',
    '<circle cx="253.25" cy="127" r="10" fill="#246820" opacity="0.92"/>',
    '<circle cx="253.25" cy="118" r="7.5" fill="#2E7828" opacity="0.90"/>',
    # Far-right cluster
    '<rect x="368" y="128" width="2.6" height="32" fill="#162C0A"/>',
    '<circle cx="369.3" cy="125" r="10.5" fill="#246820" opacity="0.94"/>',
    '<circle cx="369.3" cy="115" r="8" fill="#2E7828" opacity="0.92"/>',
    '<circle cx="369.3" cy="108" r="5.5" fill="#388A32" opacity="0.88"/>',
    '<rect x="387" y="131" width="2.3" height="29" fill="#162C0A"/>',
    '<circle cx="388.15" cy="128" r="9.5" fill="#226418" opacity="0.92"/>',
    '<circle cx="388.15" cy="119" r="7" fill="#2C7222" opacity="0.90"/>',

    # ── LAYER 4: MID-DISTANCE TREES (y≈170-230) ───────────────────────
    # Left pair
    '<rect x="6" y="174" width="4.2" height="55" fill="#182C08"/>',
    '<ellipse cx="8.1" cy="170" rx="16" ry="13" fill="#2C7020" opacity="0.96"/>',
    '<ellipse cx="8.1" cy="159" rx="11.5" ry="9.5" fill="#369028" opacity="0.94"/>',
    '<ellipse cx="8.1" cy="151" rx="7.5" ry="6" fill="#44A032" opacity="0.90"/>',
    '<rect x="36" y="178" width="3.8" height="50" fill="#182C08"/>',
    '<ellipse cx="37.9" cy="174" rx="14.5" ry="12" fill="#286C1C" opacity="0.94"/>',
    '<ellipse cx="37.9" cy="164" rx="10.5" ry="8.5" fill="#348A26" opacity="0.92"/>',
    '<ellipse cx="37.9" cy="157" rx="6.8" ry="5.5" fill="#40A030" opacity="0.88"/>',
    # Center-left mid (x≈105)
    '<rect x="103" y="177" width="4" height="52" fill="#182C08"/>',
    '<ellipse cx="105" cy="173" rx="15.5" ry="12.5" fill="#2A6E1E" opacity="0.94"/>',
    '<ellipse cx="105" cy="163" rx="11" ry="9" fill="#368C28" opacity="0.92"/>',
    '<ellipse cx="105" cy="155" rx="7.2" ry="5.8" fill="#44A032" opacity="0.88"/>',
    # Center-right mid (x≈295 — away from stage5)
    '<rect x="291" y="177" width="4" height="52" fill="#182C08"/>',
    '<ellipse cx="293" cy="173" rx="15.5" ry="12.5" fill="#2A6E1E" opacity="0.94"/>',
    '<ellipse cx="293" cy="163" rx="11" ry="9" fill="#368C28" opacity="0.92"/>',
    '<ellipse cx="293" cy="155" rx="7.2" ry="5.8" fill="#44A032" opacity="0.88"/>',
    # Right pair
    '<rect x="349" y="174" width="4.2" height="55" fill="#182C08"/>',
    '<ellipse cx="351.1" cy="170" rx="16" ry="13" fill="#2C7020" opacity="0.96"/>',
    '<ellipse cx="351.1" cy="159" rx="11.5" ry="9.5" fill="#369028" opacity="0.94"/>',
    '<ellipse cx="351.1" cy="151" rx="7.5" ry="6" fill="#44A032" opacity="0.90"/>',
    '<rect x="372" y="178" width="3.8" height="50" fill="#182C08"/>',
    '<ellipse cx="373.9" cy="174" rx="14.5" ry="12" fill="#286C1C" opacity="0.94"/>',
    '<ellipse cx="373.9" cy="164" rx="10.5" ry="8.5" fill="#348A26" opacity="0.92"/>',
    '<ellipse cx="373.9" cy="157" rx="6.8" ry="5.5" fill="#40A030" opacity="0.88"/>',

    # ══════════════════════════════════════════════════════════════════
    #  STAGE 5 SPECIAL: 桜の木 Cherry Blossom Tree  (x=200, y≈235)
    # ══════════════════════════════════════════════════════════════════
    '<g transform="translate(52,0)">',
    # Ground shadow under tree
    '<ellipse cx="200" cy="298" rx="24" ry="8" fill="#1A5010" opacity="0.35"/>',
    # Main trunk
    '<rect x="195" y="248" width="10" height="52" fill="#5A3818" rx="4"/>',
    # Trunk grain
    '<path d="M197,255 Q199,263 197,274 Q200,281 198,292" stroke="#7A5030" stroke-width="1.3" fill="none" opacity="0.45"/>',
    # Primary branches
    '<path d="M200,262 Q184,248 173,234" stroke="#5A3818" stroke-width="5" fill="none" stroke-linecap="round"/>',
    '<path d="M200,262 Q216,248 227,234" stroke="#5A3818" stroke-width="5" fill="none" stroke-linecap="round"/>',
    '<path d="M200,256 Q191,240 185,224" stroke="#5A3818" stroke-width="3.5" fill="none" stroke-linecap="round"/>',
    # Secondary branches
    '<path d="M173,234 Q165,226 160,218" stroke="#5A3818" stroke-width="2.8" fill="none" stroke-linecap="round"/>',
    '<path d="M227,234 Q235,226 240,218" stroke="#5A3818" stroke-width="2.8" fill="none" stroke-linecap="round"/>',
    '<path d="M185,224 Q179,215 176,206" stroke="#5A3818" stroke-width="2.2" fill="none" stroke-linecap="round"/>',
    # Blossom clouds — base layer
    '<ellipse cx="200" cy="220" rx="32" ry="24" fill="#FFAACC" opacity="0.95"/>',
    '<ellipse cx="174" cy="232" rx="20" ry="16" fill="#FF9EC4" opacity="0.93"/>',
    '<ellipse cx="226" cy="232" rx="20" ry="16" fill="#FF9EC4" opacity="0.93"/>',
    '<ellipse cx="200" cy="202" rx="22" ry="17" fill="#FFB8D8" opacity="0.91"/>',
    # Blossom clouds — mid layer
    '<ellipse cx="180" cy="216" rx="14" ry="12" fill="#FFBCDC" opacity="0.87"/>',
    '<ellipse cx="220" cy="216" rx="14" ry="12" fill="#FFBCDC" opacity="0.87"/>',
    '<ellipse cx="162" cy="224" rx="11" ry="9.5" fill="#FFB0D0" opacity="0.83"/>',
    '<ellipse cx="238" cy="224" rx="11" ry="9.5" fill="#FFB0D0" opacity="0.83"/>',
    '<ellipse cx="200" cy="192" rx="14" ry="10.5" fill="#FFCCE4" opacity="0.78"/>',
    # Blossom clouds — highlight top
    '<ellipse cx="200" cy="212" rx="16" ry="11" fill="#FFD8EC" opacity="0.48"/>',
    '<ellipse cx="195" cy="205" rx="9" ry="7" fill="#FFE8F4" opacity="0.42"/>',
    # Individual blossom detail
    '<circle cx="200" cy="206" r="4" fill="#FFE8F4" opacity="0.90"/>',
    '<circle cx="188" cy="220" r="3.5" fill="#FFE4F0" opacity="0.84"/>',
    '<circle cx="212" cy="220" r="3.5" fill="#FFE4F0" opacity="0.84"/>',
    '<circle cx="177" cy="228" r="3" fill="#FFE0EC" opacity="0.80"/>',
    '<circle cx="223" cy="228" r="3" fill="#FFE0EC" opacity="0.80"/>',
    # Falling petals
    '<ellipse cx="216" cy="257" rx="3.5" ry="2.5" fill="#FFB8D8" opacity="0.82" transform="rotate(-30,216,257)"/>',
    '<ellipse cx="186" cy="264" rx="3.5" ry="2.5" fill="#FFB8D8" opacity="0.78" transform="rotate(22,186,264)"/>',
    '<ellipse cx="232" cy="246" rx="3" ry="2.2" fill="#FFB8D8" opacity="0.72" transform="rotate(-45,232,246)"/>',
    '<ellipse cx="170" cy="252" rx="3" ry="2.2" fill="#FFB8D8" opacity="0.72" transform="rotate(16,170,252)"/>',
    '<ellipse cx="224" cy="270" rx="2.8" ry="2" fill="#FFB8D8" opacity="0.66" transform="rotate(-20,224,270)"/>',
    '<ellipse cx="176" cy="275" rx="2.8" ry="2" fill="#FFB8D8" opacity="0.66" transform="rotate(32,176,275)"/>',
    '<ellipse cx="240" cy="258" rx="2.5" ry="1.8" fill="#FFB8D8" opacity="0.60" transform="rotate(-55,240,258)"/>',
    '<ellipse cx="162" cy="265" rx="2.5" ry="1.8" fill="#FFB8D8" opacity="0.58" transform="rotate(10,162,265)"/>',
    '</g>',

    # ── LAYER 5: NEAR-MID TREES (y≈285-380) ─────────────────────────
    # Far-left cluster (large)
    '<rect x="10" y="292" width="7.5" height="90" fill="#22300A"/>',
    '<ellipse cx="13.75" cy="283" rx="28" ry="23" fill="#27691D" opacity="0.97"/>',
    '<ellipse cx="13.75" cy="264" rx="20" ry="16" fill="#348A28" opacity="0.95"/>',
    '<ellipse cx="13.75" cy="251" rx="13" ry="10" fill="#42A030" opacity="0.92"/>',
    '<rect x="50" y="298" width="6.5" height="84" fill="#142408"/>',
    '<ellipse cx="53.25" cy="290" rx="24" ry="20" fill="#256518" opacity="0.95"/>',
    '<ellipse cx="53.25" cy="273" rx="16.5" ry="14" fill="#338226" opacity="0.93"/>',
    '<ellipse cx="53.25" cy="261" rx="11" ry="8.5" fill="#3E9C2E" opacity="0.90"/>',
    # Left-center near-mid (x≈130)
    '<rect x="128" y="300" width="6" height="80" fill="#142408"/>',
    '<ellipse cx="131" cy="292" rx="22" ry="18" fill="#256A1C" opacity="0.95"/>',
    '<ellipse cx="131" cy="276" rx="15.5" ry="12.5" fill="#32861E" opacity="0.93"/>',
    '<ellipse cx="131" cy="265" rx="10.5" ry="8" fill="#3EA028" opacity="0.90"/>',
    # Right-center near-mid (x≈270 — not blocking stage10 at x=200,y=531)
    '<rect x="266" y="300" width="6" height="80" fill="#142408"/>',
    '<ellipse cx="269" cy="292" rx="22" ry="18" fill="#256A1C" opacity="0.95"/>',
    '<ellipse cx="269" cy="276" rx="15.5" ry="12.5" fill="#32861E" opacity="0.93"/>',
    '<ellipse cx="269" cy="265" rx="10.5" ry="8" fill="#3EA028" opacity="0.90"/>',
    # Far-right cluster (large)
    '<rect x="337" y="292" width="7.5" height="90" fill="#22300A"/>',
    '<ellipse cx="340.75" cy="283" rx="28" ry="23" fill="#27691D" opacity="0.97"/>',
    '<ellipse cx="340.75" cy="264" rx="20" ry="16" fill="#348A28" opacity="0.95"/>',
    '<ellipse cx="340.75" cy="251" rx="13" ry="10" fill="#42A030" opacity="0.92"/>',
    '<rect x="368" y="298" width="6.5" height="84" fill="#142408"/>',
    '<ellipse cx="371.25" cy="290" rx="24" ry="20" fill="#256518" opacity="0.95"/>',
    '<ellipse cx="371.25" cy="273" rx="16.5" ry="14" fill="#338226" opacity="0.93"/>',
    '<ellipse cx="371.25" cy="261" rx="11" ry="8.5" fill="#3E9C2E" opacity="0.90"/>',

    # ── WILDFLOWER FIELD (mid-zone) ───────────────────────────────────
    # Yellow dandelions
    '<circle cx="82" cy="398" r="5" fill="#FFE030"/>',
    '<circle cx="79" cy="392" r="3.8" fill="#FFD020"/>',
    '<circle cx="85" cy="391" r="3.8" fill="#FFE030"/>',
    '<rect x="83" y="398" width="1.2" height="14" fill="#3A7A20"/>',
    '<circle cx="162" cy="418" r="4.5" fill="#FFE030"/>',
    '<rect x="163" y="418" width="1.2" height="13" fill="#3A7A20"/>',
    '<circle cx="328" cy="404" r="4.8" fill="#FFD820"/>',
    '<rect x="329" y="404" width="1.2" height="13" fill="#3A7A20"/>',
    # Pink daisies
    '<circle cx="118" cy="378" r="6" fill="#FF8AB4"/>',
    '<circle cx="118" cy="378" r="2.6" fill="#FFE870"/>',
    '<rect x="119" y="384" width="1.2" height="14" fill="#3A7820"/>',
    '<circle cx="258" cy="388" r="5.5" fill="#FF8AB4"/>',
    '<circle cx="258" cy="388" r="2.4" fill="#FFE870"/>',
    '<circle cx="308" cy="374" r="6" fill="#FF9AC0"/>',
    '<circle cx="308" cy="374" r="2.6" fill="#FFE870"/>',
    # Purple lavender clusters
    '<ellipse cx="64" cy="448" rx="5.5" ry="3.2" fill="#B870E0" opacity="0.90"/>',
    '<ellipse cx="64" cy="443" rx="5" ry="3" fill="#A860CC" opacity="0.86"/>',
    '<rect x="63.5" y="448" width="1.2" height="16" fill="#3A6A20"/>',
    '<ellipse cx="338" cy="438" rx="5.5" ry="3.2" fill="#B870E0" opacity="0.90"/>',
    '<ellipse cx="338" cy="433" rx="5" ry="3" fill="#A860CC" opacity="0.86"/>',
    '<rect x="337.5" y="438" width="1.2" height="16" fill="#3A6A20"/>',
    # Red poppies
    '<circle cx="210" cy="358" r="6" fill="#E83028"/>',
    '<circle cx="210" cy="358" r="2.2" fill="#220808"/>',
    '<rect x="211" y="364" width="1.2" height="15" fill="#3A7820"/>',
    '<circle cx="148" cy="370" r="5.5" fill="#E82820"/>',
    '<circle cx="148" cy="370" r="2" fill="#220808"/>',
    # White daisies
    '<circle cx="174" cy="438" r="5.5" fill="#FFFFFF" opacity="0.94"/>',
    '<circle cx="174" cy="438" r="2.4" fill="#FFE860"/>',
    '<circle cx="238" cy="428" r="5" fill="#FFFFFF" opacity="0.92"/>',
    '<circle cx="238" cy="428" r="2.2" fill="#FFE860"/>',
    # Orange flowers
    '<circle cx="188" cy="410" r="5" fill="#FF8830"/>',
    '<circle cx="188" cy="410" r="2" fill="#FFE060"/>',

    # ── BUTTERFLY (upper-right of stage 5) ───────────────────────────
    # Upper wings
    '<path d="M250,226 Q263,214 272,224 Q263,234 250,226" fill="#FF8AC8" opacity="0.90"/>',
    '<path d="M250,226 Q237,214 228,224 Q237,234 250,226" fill="#FF6CB0" opacity="0.90"/>',
    # Lower wings
    '<path d="M250,231 Q263,243 270,235 Q263,227 250,231" fill="#FFA4D0" opacity="0.76"/>',
    '<path d="M250,231 Q237,243 230,235 Q237,227 250,231" fill="#FFA4D0" opacity="0.76"/>',
    # Wing pattern
    '<circle cx="258" cy="222" r="3.5" fill="#FFD8EC" opacity="0.60"/>',
    '<circle cx="242" cy="222" r="3.5" fill="#FFD8EC" opacity="0.60"/>',
    # Body & antennae
    '<circle cx="250" cy="228" r="2" fill="#5A2010"/>',
    '<line x1="246.5" y1="226" x2="241" y2="219" stroke="#5A2010" stroke-width="0.9"/>',
    '<line x1="253.5" y1="226" x2="259" y2="219" stroke="#5A2010" stroke-width="0.9"/>',
    '<circle cx="240.5" cy="218.5" r="1.2" fill="#5A2010"/>',
    '<circle cx="259.5" cy="218.5" r="1.2" fill="#5A2010"/>',

    # ── RABBIT (right side) ───────────────────────────────────────────
    '<ellipse cx="302" cy="550" rx="10" ry="8" fill="#EAE2D2"/>',
    '<ellipse cx="304" cy="540" rx="6.5" ry="5" fill="#E2DAC8"/>',
    # Ears
    '<ellipse cx="301" cy="532" rx="2.5" ry="7" fill="#E2DAC8"/>',
    '<ellipse cx="307" cy="533" rx="2.5" ry="7" fill="#E2DAC8"/>',
    '<ellipse cx="301" cy="532" rx="1.2" ry="5" fill="#FFB8C4" opacity="0.65"/>',
    '<ellipse cx="307" cy="533" rx="1.2" ry="5" fill="#FFB8C4" opacity="0.65"/>',
    # Face
    '<circle cx="305" cy="541" r="1" fill="#FF8898"/>',
    '<circle cx="303" cy="540.5" r="1.4" fill="#1A0808" opacity="0.88"/>',
    '<circle cx="303.6" cy="540" r="0.5" fill="#FFFFFF"/>',
    # Feet
    '<ellipse cx="296" cy="557" rx="5.5" ry="2.8" fill="#EAE2D2"/>',
    '<ellipse cx="308" cy="557" rx="5.5" ry="2.8" fill="#EAE2D2"/>',

    # ══════════════════════════════════════════════════════════════════
    #  STAGE 10 SPECIAL: 花のアーチゲート Flower Gate  (x=200, y≈531)
    # ══════════════════════════════════════════════════════════════════
    '<g transform="translate(200,531) scale(1.5) translate(-200,-531)">',
    # Ground shadow
    '<ellipse cx="200" cy="564" rx="40" ry="7" fill="#1A5010" opacity="0.32"/>',
    # Left post
    '<rect x="166" y="510" width="13" height="57" fill="url(#eGate)" rx="4"/>',
    '<rect x="168" y="510" width="5" height="57" fill="#B09060" rx="2" opacity="0.38"/>',
    # Right post
    '<rect x="221" y="510" width="13" height="57" fill="url(#eGate)" rx="4"/>',
    '<rect x="223" y="510" width="5" height="57" fill="#B09060" rx="2" opacity="0.38"/>',
    # Main arch
    '<path d="M166,523 Q200,493 234,523" stroke="#6A4820" stroke-width="10" fill="none" stroke-linecap="round"/>',
    '<path d="M167,524 Q200,495 233,524" stroke="#9A7848" stroke-width="4.5" fill="none" stroke-linecap="round" opacity="0.42"/>',
    # Cross-bar accent
    '<rect x="163" y="530" width="74" height="5" fill="#6A4820" rx="2" opacity="0.30"/>',
    # Hanging vines
    '<path d="M182,507 Q179,518 182,527" stroke="#3A8820" stroke-width="2.5" fill="none" stroke-linecap="round"/>',
    '<path d="M200,497 Q200,511 200,520" stroke="#3A8820" stroke-width="2.5" fill="none" stroke-linecap="round"/>',
    '<path d="M218,507 Q221,518 218,527" stroke="#3A8820" stroke-width="2.5" fill="none" stroke-linecap="round"/>',
    # Leaf clusters
    '<ellipse cx="182" cy="515" rx="6" ry="4" fill="#3A8820" transform="rotate(-18,182,515)"/>',
    '<ellipse cx="200" cy="508" rx="6" ry="4" fill="#3A8820"/>',
    '<ellipse cx="218" cy="515" rx="6" ry="4" fill="#3A8820" transform="rotate(18,218,515)"/>',
    # Extra leaf detail
    '<ellipse cx="192" cy="503" rx="4.5" ry="3" fill="#46A02A" transform="rotate(-10,192,503)"/>',
    '<ellipse cx="208" cy="503" rx="4.5" ry="3" fill="#46A02A" transform="rotate(10,208,503)"/>',
    # Arch flowers — primary
    '<circle cx="166" cy="523" r="9" fill="#FF587A"/>',
    '<circle cx="166" cy="523" r="4" fill="#FFE870"/>',
    '<circle cx="181" cy="506" r="8" fill="#FFD700"/>',
    '<circle cx="181" cy="506" r="3.5" fill="#FF8820"/>',
    '<circle cx="200" cy="494" r="10" fill="#FF78A8"/>',
    '<circle cx="200" cy="494" r="4.5" fill="#FFE870"/>',
    '<circle cx="219" cy="506" r="8" fill="#FFD700"/>',
    '<circle cx="219" cy="506" r="3.5" fill="#FF8820"/>',
    '<circle cx="234" cy="523" r="9" fill="#FF587A"/>',
    '<circle cx="234" cy="523" r="4" fill="#FFE870"/>',
    # Flower petals detail (left main)
    '<circle cx="172" cy="523" r="3.2" fill="#FF9DC8" opacity="0.72"/>',
    '<circle cx="160" cy="523" r="3.2" fill="#FF9DC8" opacity="0.72"/>',
    '<circle cx="166" cy="517" r="3.2" fill="#FF9DC8" opacity="0.72"/>',
    '<circle cx="166" cy="529" r="3.2" fill="#FF9DC8" opacity="0.72"/>',
    # Flower petals detail (right main)
    '<circle cx="240" cy="523" r="3.2" fill="#FF9DC8" opacity="0.72"/>',
    '<circle cx="228" cy="523" r="3.2" fill="#FF9DC8" opacity="0.72"/>',
    '<circle cx="234" cy="517" r="3.2" fill="#FF9DC8" opacity="0.72"/>',
    '<circle cx="234" cy="529" r="3.2" fill="#FF9DC8" opacity="0.72"/>',
    # Post-climbing flowers
    '<circle cx="172" cy="548" r="5.5" fill="#FF8AB4"/>',
    '<circle cx="172" cy="548" r="2.2" fill="#FFE870"/>',
    '<circle cx="228" cy="548" r="5.5" fill="#FF8AB4"/>',
    '<circle cx="228" cy="548" r="2.2" fill="#FFE870"/>',
    # Fallen petals below gate
    '<ellipse cx="188" cy="568" rx="3" ry="2" fill="#FFB8D4" opacity="0.68" transform="rotate(-15,188,568)"/>',
    '<ellipse cx="212" cy="570" rx="3" ry="2" fill="#FFB8D4" opacity="0.65" transform="rotate(20,212,570)"/>',
    '</g>',

    # ── GRASS TUFTS & GROUND DETAIL ───────────────────────────────────
    '<path d="M28,478 Q30,465 32,457 Q34,465 36,478" fill="#2A7018" opacity="0.82"/>',
    '<path d="M142,462 Q144,450 146,442 Q148,450 150,462" fill="#2A7018" opacity="0.82"/>',
    '<path d="M282,468 Q284,456 286,448 Q288,456 290,468" fill="#2A7018" opacity="0.82"/>',
    '<path d="M378,473 Q380,461 382,453 Q384,461 386,473" fill="#2A7018" opacity="0.82"/>',
    # Scattered base flowers
    '<circle cx="44" cy="552" r="4.5" fill="#FFE030"/>',
    '<circle cx="100" cy="546" r="4.5" fill="#FF8AB4"/>',
    '<circle cx="155" cy="556" r="4" fill="#FF8AB4"/>',
    '<circle cx="230" cy="556" r="4.5" fill="#FFFFFF" opacity="0.93"/>',
    '<circle cx="230" cy="556" r="2" fill="#FFE860"/>',
    '<circle cx="285" cy="548" r="4.5" fill="#FFE030"/>',
    '<circle cx="356" cy="552" r="4" fill="#FF8AB4"/>',

    # ── LAYER 6: FOREGROUND LARGE TREES ──────────────────────────────
    # Left — trunk only visible between lower canopy layers
    '<rect x="0" y="455" width="18" height="145" fill="#3A2210"/>',
    # Canopy — top to bottom layers
    '<ellipse cx="9" cy="430" rx="54" ry="42" fill="#23671B" opacity="0.99"/>',
    '<ellipse cx="9" cy="403" rx="38" ry="30" fill="#30842A" opacity="0.97"/>',
    '<ellipse cx="9" cy="380" rx="25" ry="18" fill="#3CA030" opacity="0.95"/>',
    '<ellipse cx="9" cy="363" rx="16" ry="11" fill="#48B034" opacity="0.90"/>',
    # Lower canopy skirt — fully covers trunk below canopy
    '<ellipse cx="9" cy="480" rx="58" ry="28" fill="#25701F"/>',
    '<ellipse cx="9" cy="528" rx="55" ry="22" fill="#236A1C"/>',
    '<ellipse cx="9" cy="572" rx="52" ry="20" fill="#226418"/>',
    '<ellipse cx="9" cy="600" rx="50" ry="16" fill="#2A7020"/>',
    # Right — trunk only visible between lower canopy layers
    '<rect x="382" y="457" width="18" height="143" fill="#3A2210"/>',
    # Canopy — top to bottom layers
    '<ellipse cx="391" cy="430" rx="54" ry="42" fill="#23671B" opacity="0.99"/>',
    '<ellipse cx="391" cy="403" rx="38" ry="30" fill="#30842A" opacity="0.97"/>',
    '<ellipse cx="391" cy="380" rx="25" ry="18" fill="#3CA030" opacity="0.95"/>',
    '<ellipse cx="391" cy="363" rx="16" ry="11" fill="#48B034" opacity="0.90"/>',
    # Lower canopy skirt — fully covers trunk below canopy
    '<ellipse cx="391" cy="480" rx="58" ry="28" fill="#25701F"/>',
    '<ellipse cx="391" cy="528" rx="55" ry="22" fill="#236A1C"/>',
    '<ellipse cx="391" cy="572" rx="52" ry="20" fill="#226418"/>',
    '<ellipse cx="391" cy="600" rx="50" ry="16" fill="#2A7020"/>',

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
