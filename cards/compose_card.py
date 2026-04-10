#!/usr/bin/env python3
"""カード合成スクリプト: 絵柄画像 + 枠テンプレート → 完成カード"""
from PIL import Image
import sys, os

def compose(art_path, frame_path, output_path, target_w=896, target_h=1280):
    frame = Image.open(frame_path).convert('RGBA')
    art = Image.open(art_path).convert('RGBA')

    frame = frame.resize((target_w, target_h), Image.LANCZOS)

    # Make white/near-white pixels in frame transparent
    pixels = frame.load()
    for y in range(target_h):
        for x in range(target_w):
            r, g, b, a = pixels[x, y]
            if r > 230 and g > 230 and b > 230:
                pixels[x, y] = (r, g, b, 0)

    art_resized = art.resize((target_w, target_h), Image.LANCZOS)

    card = Image.new('RGBA', (target_w, target_h), (255, 255, 255, 255))
    card.paste(art_resized, (0, 0), art_resized)
    card.paste(frame, (0, 0), frame)

    card.convert('RGB').save(output_path, quality=95)
    print(f"OK: {output_path} ({os.path.getsize(output_path)//1024}KB)")

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python3 compose_card.py <art.png> <frame.png> <output.png>")
        sys.exit(1)
    compose(sys.argv[1], sys.argv[2], sys.argv[3])
