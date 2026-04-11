#!/usr/bin/env python3
"""カード合成スクリプト: 絵柄画像 + 枠テンプレート → 完成カード"""
from PIL import Image
import sys, os

def compose(art_path, frame_path, output_path, target_w=896, target_h=1280):
    frame = Image.open(frame_path).convert('RGBA')
    art = Image.open(art_path).convert('RGBA')

    frame = frame.resize((target_w, target_h), Image.LANCZOS)

    # Build mask: detect the content hole (white area) in the frame
    # Use flood-fill from center to find connected white region
    pixels = frame.load()
    mask = Image.new('L', (target_w, target_h), 0)  # 0 = frame, 255 = hole
    mask_px = mask.load()

    # Flood fill from center (which is definitely in the white hole)
    from collections import deque
    visited = set()
    queue = deque()
    cx, cy = target_w // 2, target_h // 2
    queue.append((cx, cy))
    visited.add((cx, cy))

    while queue:
        x, y = queue.popleft()
        r, g, b, a = pixels[x, y]
        if r > 220 and g > 220 and b > 220:
            mask_px[x, y] = 255
            for nx, ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0 <= nx < target_w and 0 <= ny < target_h and (nx,ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    # Art only shows through the hole; frame covers everything else
    art_resized = art.resize((target_w, target_h), Image.LANCZOS)

    # Start with frame background color for non-hole areas
    card = Image.new('RGBA', (target_w, target_h), (0, 0, 0, 255))

    # Paste art only where mask is white (the hole)
    card.paste(art_resized, (0, 0), mask)

    # Paste frame on top (frame's own pixels cover non-hole areas)
    # Make the hole area transparent in frame so art shows through
    frame_with_hole = frame.copy()
    fh_px = frame_with_hole.load()
    for y in range(target_h):
        for x in range(target_w):
            if mask_px[x, y] == 255:
                fh_px[x, y] = (0, 0, 0, 0)
    card.paste(frame_with_hole, (0, 0), frame_with_hole)

    card.convert('RGB').save(output_path, quality=95)
    print(f"OK: {output_path} ({os.path.getsize(output_path)//1024}KB)")

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python3 compose_card.py <art.png> <frame.png> <output.png>")
        sys.exit(1)
    compose(sys.argv[1], sys.argv[2], sys.argv[3])
