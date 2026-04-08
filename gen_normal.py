#!/usr/bin/env python3
"""gen_normal.py — Limsa Lominsa graphic-recording style (hand-drawn sketch on cream paper)."""
import re, math, random

random.seed(43)  # reproducible wobble

with open('/Users/hirokazukataoka/subitze/stage.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── Wobble helper ───────────────────────────────────────────────────────
def wobble_path(points, closed=False):
    if len(points) < 2:
        return ''
    segs = [f'M{points[0][0]:.1f},{points[0][1]:.1f}']
    for i in range(1, len(points)):
        x0, y0 = points[i-1]
        x1, y1 = points[i]
        mx = (x0 + x1) / 2 + random.uniform(-1.5, 1.5)
        my = (y0 + y1) / 2 + random.uniform(-1.5, 1.5)
        segs.append(f'Q{mx:.1f},{my:.1f} {x1:.1f},{y1:.1f}')
    if closed:
        x0, y0 = points[-1]
        x1, y1 = points[0]
        mx = (x0 + x1) / 2 + random.uniform(-1.5, 1.5)
        my = (y0 + y1) / 2 + random.uniform(-1.5, 1.5)
        segs.append(f'Q{mx:.1f},{my:.1f} {x1:.1f},{y1:.1f}')
        segs.append('Z')
    return ' '.join(segs)

def wave_line(y, x_start, x_end, amplitude=4, freq=25):
    """Generate a wavy horizontal line."""
    pts = []
    for x in range(x_start, x_end + 1, freq):
        pts.append((x, y + random.uniform(-amplitude, amplitude)))
    return wobble_path(pts)

# ── Build SVG ───────────────────────────────────────────────────────────
P = []
A = P.append

W, H = 400, 600
PAPER = '#EDF0E8'     # cream with blue tint
PAPER2 = '#E0E8F0'    # slightly bluer
OUTLINE = '#2A2A2A'
SW = 2.5
SW_BOLD = 3.5

A(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">')

# ── Paper background ──
A(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')

# ── Ocean area (upper portion, flat blue) ──
sea_y = 180
A(f'<rect width="{W}" height="{sea_y}" fill="#88C0E0" opacity="0.35"/>')
# Horizon line
A(f'<line x1="0" y1="{sea_y}" x2="{W}" y2="{sea_y}" stroke="#6090B0" stroke-width="1.5" opacity="0.4"/>')
# Wave lines
for wy in range(40, sea_y, 30):
    A(f'<path d="{wave_line(wy, 0, W, 3, 20)}" stroke="#6090B0" stroke-width="1.2" fill="none" opacity="0.3"/>')

# ── Sky area (very subtle) ──
A(f'<rect width="{W}" height="40" fill="{PAPER2}" opacity="0.3"/>')

# ── Clouds (simple fluffy outlines) ──
for (cx, cy, crx, cry) in [(80, 22, 30, 12), (280, 30, 35, 14), (180, 15, 22, 9)]:
    bumps = 6
    pts = []
    for i in range(bumps * 2):
        angle = math.pi * 2 * i / (bumps * 2)
        r_f = 1.0 + random.uniform(-0.1, 0.12)
        pts.append((cx + crx * r_f * math.cos(angle), cy + cry * r_f * math.sin(angle)))
    A(f'<path d="{wobble_path(pts, True)}" fill="white" stroke="{OUTLINE}" stroke-width="1.2" opacity="0.4"/>')

# ── Left cliff (limestone, tall angular shape) ──
cliff_l = [(0, sea_y), (0, 100), (15, 85), (45, 95), (70, 110), (85, sea_y+40), (60, sea_y+80), (0, sea_y+60)]
A(f'<path d="{wobble_path(cliff_l, True)}" fill="#D8C8A0" stroke="{OUTLINE}" stroke-width="{SW_BOLD}" opacity="0.8"/>')
# Strata lines
for sy in range(105, sea_y+50, 18):
    A(f'<line x1="5" y1="{sy}" x2="{55 + random.randint(-5,5)}" y2="{sy+random.randint(-2,2)}" '
      f'stroke="#B0A080" stroke-width="1" opacity="0.4"/>')

# ── Right cliff ──
cliff_r = [(W, sea_y), (W, 120), (380, 105), (355, 115), (335, 130), (320, sea_y+30), (345, sea_y+70), (W, sea_y+50)]
A(f'<path d="{wobble_path(cliff_r, True)}" fill="#D8C8A0" stroke="{OUTLINE}" stroke-width="{SW_BOLD}" opacity="0.8"/>')
for sy in range(120, sea_y+40, 18):
    A(f'<line x1="{W-5}" y1="{sy}" x2="{350 + random.randint(-5,5)}" y2="{sy+random.randint(-2,2)}" '
      f'stroke="#B0A080" stroke-width="1" opacity="0.4"/>')

# ── Lighthouse (on left cliff) ──
lh_x, lh_y = 30, 70
A(f'<path d="{wobble_path([(lh_x-8, 100), (lh_x-6, lh_y), (lh_x+6, lh_y), (lh_x+8, 100)])}" '
  f'fill="#F0E8D8" stroke="{OUTLINE}" stroke-width="{SW}" opacity="0.85"/>')
# Light room
A(f'<path d="{wobble_path([(lh_x-7, lh_y), (lh_x-5, lh_y-8), (lh_x+5, lh_y-8), (lh_x+7, lh_y)])}" '
  f'fill="#E0D8C0" stroke="{OUTLINE}" stroke-width="1.8" opacity="0.85"/>')
# Roof
A(f'<path d="M{lh_x-6},{lh_y-8} L{lh_x},{lh_y-16} L{lh_x+6},{lh_y-8}" '
  f'fill="#C85040" stroke="{OUTLINE}" stroke-width="1.8" opacity="0.85"/>')
# Light glow (simple yellow star)
A(f'<circle cx="{lh_x}" cy="{lh_y-5}" r="3" fill="#FFD040" stroke="none" opacity="0.7"/>')
A(f'<line x1="{lh_x-7}" y1="{lh_y-5}" x2="{lh_x+7}" y2="{lh_y-5}" stroke="#FFD040" stroke-width="1" opacity="0.5"/>')
A(f'<line x1="{lh_x}" y1="{lh_y-12}" x2="{lh_x}" y2="{lh_y+2}" stroke="#FFD040" stroke-width="1" opacity="0.5"/>')

# ── Tower on right cliff ──
tw_x = 370
A(f'<path d="{wobble_path([(tw_x-10, 120), (tw_x-8, 75), (tw_x+8, 75), (tw_x+10, 120)])}" '
  f'fill="#E8DCC8" stroke="{OUTLINE}" stroke-width="{SW}" opacity="0.75"/>')
A(f'<path d="M{tw_x-9},{75} L{tw_x},{62} L{tw_x+9},{75}" '
  f'fill="#C08040" stroke="{OUTLINE}" stroke-width="1.8" opacity="0.75"/>')
# Window
A(f'<rect x="{tw_x-3}" y="88" width="6" height="8" rx="1" fill="#6090B0" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.6"/>')

# ── Bridge arch (connecting cliffs, upper-mid area) ──
bridge_y = sea_y + 15
A(f'<path d="M75,{bridge_y-5} Q200,{bridge_y-45} 325,{bridge_y-5}" '
  f'stroke="{OUTLINE}" stroke-width="{SW_BOLD}" fill="none" opacity="0.55"/>')
A(f'<path d="M75,{bridge_y+3} Q200,{bridge_y-37} 325,{bridge_y+3}" '
  f'stroke="{OUTLINE}" stroke-width="1.5" fill="none" opacity="0.3"/>')

# ── Ships (upper area, simple sail + hull) ──
# Ship 1 (left)
sx1, sy1 = 130, 130
A(f'<path d="M{sx1-15},{sy1} Q{sx1},{sy1+8} {sx1+15},{sy1}" stroke="{OUTLINE}" stroke-width="2" fill="#C8A870" opacity="0.6"/>')
A(f'<line x1="{sx1}" y1="{sy1}" x2="{sx1}" y2="{sy1-25}" stroke="#8B6840" stroke-width="1.5" opacity="0.6"/>')
A(f'<path d="M{sx1},{sy1-25} L{sx1+12},{sy1-10} L{sx1},{sy1-8}" fill="#F0E0D0" stroke="{OUTLINE}" stroke-width="1.2" opacity="0.5"/>')
# Ship 2 (right, smaller)
sx2, sy2 = 280, 145
A(f'<path d="M{sx2-10},{sy2} Q{sx2},{sy2+5} {sx2+10},{sy2}" stroke="{OUTLINE}" stroke-width="1.5" fill="#C8A870" opacity="0.45"/>')
A(f'<line x1="{sx2}" y1="{sy2}" x2="{sx2}" y2="{sy2-18}" stroke="#8B6840" stroke-width="1.2" opacity="0.45"/>')
A(f'<path d="M{sx2},{sy2-18} L{sx2+8},{sy2-8} L{sx2},{sy2-6}" fill="#F0E0D0" stroke="{OUTLINE}" stroke-width="1" opacity="0.4"/>')

# ── Harbor/dock area (lower portion) ──
dock_y = 350
# Stone quay (left)
A(f'<path d="{wobble_path([(0, dock_y), (0, dock_y-20), (90, dock_y-25), (95, dock_y+5), (0, dock_y+10)])}" '
  f'fill="#C8B898" stroke="{OUTLINE}" stroke-width="2" opacity="0.5"/>')
# Stone quay (right)
A(f'<path d="{wobble_path([(W, dock_y), (W, dock_y-18), (315, dock_y-22), (310, dock_y+5), (W, dock_y+8)])}" '
  f'fill="#C8B898" stroke="{OUTLINE}" stroke-width="2" opacity="0.5"/>')

# ── Bollards (dock detail) ──
for bx in [20, 55, 350, 380]:
    A(f'<rect x="{bx-3}" y="{dock_y-30}" width="6" height="10" rx="1" fill="#A09078" stroke="{OUTLINE}" stroke-width="1" opacity="0.5"/>')

# ── Barrels doodle (right dock) ──
for (bx, by) in [(340, dock_y-28), (355, dock_y-30)]:
    A(f'<ellipse cx="{bx}" cy="{by}" rx="7" ry="5" fill="#C8A060" stroke="{OUTLINE}" stroke-width="1.2" opacity="0.45"/>')
    A(f'<line x1="{bx-5}" y1="{by}" x2="{bx+5}" y2="{by}" stroke="#8B6840" stroke-width="0.8" opacity="0.4"/>')

# ── Seagull V-shapes ──
for (gx, gy) in [(100, 45), (190, 55), (310, 38), (250, 62)]:
    gw = random.uniform(7, 11)
    A(f'<path d="M{gx-gw},{gy+3} Q{gx},{gy-2} {gx+gw},{gy+3}" '
      f'stroke="{OUTLINE}" stroke-width="1.3" fill="none" opacity="0.35"/>')

# ── Anchor doodle (right dock decoration) ──
anc_x, anc_y = 375, dock_y - 45
A(f'<line x1="{anc_x}" y1="{anc_y}" x2="{anc_x}" y2="{anc_y+14}" stroke="#607080" stroke-width="1.8" opacity="0.4"/>')
A(f'<path d="M{anc_x-6},{anc_y+14} Q{anc_x},{anc_y+18} {anc_x+6},{anc_y+14}" stroke="#607080" stroke-width="1.5" fill="none" opacity="0.4"/>')
A(f'<line x1="{anc_x-5}" y1="{anc_y+2}" x2="{anc_x+5}" y2="{anc_y+2}" stroke="#607080" stroke-width="1.5" opacity="0.4"/>')
A(f'<circle cx="{anc_x}" cy="{anc_y-2}" r="2.5" fill="none" stroke="#607080" stroke-width="1.2" opacity="0.4"/>')

# ── Rope coil doodle (left dock) ──
A(f'<circle cx="75" cy="{dock_y-28}" r="6" fill="none" stroke="#A08860" stroke-width="1.8" opacity="0.35"/>')
A(f'<circle cx="75" cy="{dock_y-28}" r="3" fill="none" stroke="#A08860" stroke-width="1.2" opacity="0.3"/>')

# ── Maelstrom banner (small, on tower) ──
ban_x, ban_y = tw_x + 2, 80
A(f'<line x1="{ban_x}" y1="{ban_y}" x2="{ban_x}" y2="{ban_y+18}" stroke="#8B6840" stroke-width="1" opacity="0.5"/>')
A(f'<path d="M{ban_x},{ban_y+3} L{ban_x+10},{ban_y+7} L{ban_x},{ban_y+15}" fill="#C85040" stroke="{OUTLINE}" stroke-width="0.8" opacity="0.45"/>')

# ── Water sparkle dots ──
for i in range(12):
    wx = random.randint(80, 320)
    wy = random.randint(20, sea_y - 10)
    A(f'<circle cx="{wx}" cy="{wy}" r="1" fill="#B0D8F0" opacity="0.5"/>')

# ── Lower area — keep mostly clear for game elements ──
# Just a subtle stone texture line
A(f'<path d="{wave_line(480, 0, W, 2, 30)}" stroke="#C0B898" stroke-width="1" fill="none" opacity="0.2"/>')

A('</svg>')

NORMAL = ''.join(P)

# ── Inject into stage.html ───────────────────────────────────────────────
pattern = r"(if\(diff==='NORMAL'\) return ')(.*?)(';)"
replacement = r"\g<1>" + NORMAL.replace('\\', '\\\\') + r"\g<3>"
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

assert new_content != content, "Injection failed — pattern not matched"
print(f"NORMAL SVG: {len(NORMAL):,} chars injected OK")

with open('/Users/hirokazukataoka/subitze/stage.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("stage.html written.")
