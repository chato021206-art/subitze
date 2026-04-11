#!/usr/bin/env python3
"""Generate EASY+ card images using Gemini Nano Banana 2."""
import urllib.request, json, os, ssl, base64, time, sys
from PIL import Image
from collections import deque

API_KEY = os.environ.get('GOOGLE_API_KEY', '')
MODEL = 'gemini-3.1-flash-image-preview'
CTX = ssl.create_default_context()

S = """Generate an image in anime mobile game card illustration style.
Super deformed cute chibi blob creature with extremely round soft body,
tiny stubby limbs, large sparkling anime eyes, rosy cheeks,
glossy skin with specular highlights. Digital painting, vibrant saturated colors.
Rich detailed background filling the ENTIRE image edge to edge.
No white borders or margins. Creature fills 55-60% of frame height, centered
with clear margins from edges. Portrait 3:4 aspect ratio.
No text, no frame, no border, no UI elements.

IMPORTANT: This is a "+" variant — an alternate color version of the base character.
The color scheme should be distinctly different from the original.

"""

# EASY+ コンセプト:「もうひとつの物語」
# 基本カードが「日常の一瞬」なら、+カードは「もしもの世界」
# 色はhue-rotate(200deg)に近い別配色で、場面も全く違う

CARDS = {
  'easy+_0': { 'frame': 'common', 'prompt': S + """Character: A mint-green/seafoam (NOT pink) slime jelly blob creature — same
species as the pink original but this is the rare green variant. Translucent
glossy mint-green gelatin body with tiny white bubbles inside. No ears, no fur.
Large sparkling emerald-green eyes with CLOVER-SHAPED highlights.

Story: This green variant of the slime has discovered a tiny flower growing
through a crack in the dock planks. It is carefully watering the flower with a
miniature watering can held in one gooey pseudopod, tilting its whole body to
pour. A small puddle of green goo beneath it is actually nurturing other sprouts.
The flower is blooming thanks to its care. Expression: gentle concentration.

Background: sunny seaside dock in spring. Flower boxes along the railing.
Seagulls perched on posts. Warm morning light. Small sprouts growing through
dock cracks. Peaceful nurturing atmosphere.""" },

  'easy+_1': { 'frame': 'common', 'prompt': S + """Character: A lavender/periwinkle-blue (NOT yellow) snail creature with a
shimmering silver-blue spiral shell. Same snail species but rare blue variant.
Large sparkling pale blue eyes with CLOUD-SHAPED highlights, half-closed in bliss.

Story: This blue snail has climbed all the way up to a fluffy cloud above the
sea and is using it as a bed. It is curled up sleeping peacefully, shell resting
on the cloud like a pillow. A dream bubble shows seashells. Tiny "Zzz" floats
above. One arm dangles off the cloud edge. The view below shows the ocean and
tiny harbor. Expression: blissful sleeping face.

Background: above the clouds at sunset. Fluffy white and pink clouds. The sun
sets on the horizon below. Tiny harbor visible far below through cloud gaps.
Golden-pink sky. Dreamy heavenly atmosphere.""" },

  'easy+_2': { 'frame': 'common', 'prompt': S + """Character: A magenta/hot-pink (NOT green) pufferfish creature — same species
but rare pink variant. Glossy magenta body with small rounded spines.
Large sparkling deep pink eyes with MISCHIEVOUS DIAMOND highlights and one
eye half-closed in a wink.

Story: Tables have turned! This pink pufferfish is now the PRANKSTER, hiding
behind a coral reef and about to shout "BOO!" at an unsuspecting passing fish.
It peeks out from behind the coral with a mischievous grin, one fin raised
ready to jump out. The target fish swims by unaware. The pufferfish is NOT
inflated — it's in stealth mode, compact and sneaky. Expression: devious wink.

Background: vibrant coral reef underwater scene. Colorful coral formations.
The unsuspecting fish swimming past. Tropical fish in background. Shafts of
sunlight from above. Playful underwater atmosphere.""" },

  'easy+_3': { 'frame': 'common', 'prompt': S + """Character: A sky-blue/cyan (NOT orange) starfish creature — same species but
rare blue variant. Glossy cool blue body with white arm-tip spots.
Large sparkling ice-blue eyes with SNOWFLAKE-SHAPED highlights.

Story: This blue starfish is having a beach campfire night. It sits beside a
small crackling campfire on the sand, roasting a marshmallow on a tiny stick.
The marshmallow is perfectly golden-brown and the starfish's eyes are fixated
on it with pure anticipation. A string of beach lights hangs behind.
Tiny crabs gather around the warmth. Expression: wide-eyed foodie excitement.

Background: nighttime beach with campfire. String lights between poles. Stars
visible in dark sky. Waves gently lapping. Warm fire glow contrasts cool night.
Marshmallow roasting. Cozy beach party atmosphere.""" },

  'easy+_4': { 'frame': 'uncommon', 'prompt': S + """Character: A warm orange/amber (NOT blue) fish-warrior creature — same species
but golden variant. Glossy sunset-orange body with a silver crown. Silver trident.
Large sparkling warm amber eyes with PEACEFUL ROUND highlights (not fierce).

Story: The fearsome harbor guardian's day off. Instead of fighting storms, this
golden variant is peacefully FISHING from the harbor rocks. A tiny fishing rod
in one fin, a bucket with one small fish beside it. It watches the bobber
floating on calm water with relaxed half-closed eyes. A straw sun hat sits
tilted on its head over the crown. Expression: total relaxation, zen peace.

Background: calm harbor on a lazy summer afternoon. Still water reflecting
blue sky. Fishing rod line extending into water. A bobber floating. Warm
golden sunlight. Peaceful lazy summer fishing atmosphere.""" },

  'easy+_5': { 'frame': 'common', 'prompt': S + """Character: A teal/turquoise (NOT black-red) ladybug creature — same species
but rare teal variant. Glossy dark teal body with a cyan shell with white dots.
Large sparkling golden eyes with BOOK-PAGE shaped highlights.

Story: Nighttime in the lighthouse keeper's room. This teal ladybug sits at a
tiny desk, reading a thick old book by warm lamplight. Round glasses perched
on its face. A cup of tea steams beside the book. Its antenna curve forward
as it concentrates. Stacks of books tower behind it. A warm reading lamp
casts a cozy golden circle of light. Expression: deep intellectual focus.

Background: cozy lighthouse interior at night. Warm lamp on desk. Bookshelves
on walls. A round window shows stars and the sea outside. Tea and cookies on
desk. Warm amber lamplight. Scholarly cozy atmosphere.""" },

  'easy+_6': { 'frame': 'common', 'prompt': S + """Character: A rose-pink/magenta (NOT teal) anglerfish creature — same species
but rare pink variant. Glossy warm pink body. Lure glows soft rose-pink.
Large sparkling pink eyes with WARM HEART highlights.

Story: A snowy winter day — this pink anglerfish is somehow on land, in snow!
It follows mysterious footprints in the fresh snow, its pink lure lighting the
way through gently falling snowflakes. The footprints lead toward a cozy cottage
with warm light in the windows. It looks determined and curious — tracking an
adventure. Snow dusts its round body. Expression: determined explorer face.

Background: snowy winter landscape with gentle snowfall. Fresh footprints in
white snow leading to a distant warm cottage. Pine trees dusted with snow.
Pink lure glow contrasts white snow. Magical winter adventure atmosphere.""" },

  'easy+_7': { 'frame': 'common', 'prompt': S + """Character: A warm yellow-green/chartreuse (NOT lavender) jellyfish creature —
same species but rare golden variant. Translucent warm yellow-gold dome.
Large sparkling golden eyes with SPA/ONSEN-STEAM shaped highlights, closed in bliss.

Story: This golden jellyfish has found a natural hot spring pool by the sea.
It soaks in the steaming water up to its dome, tentacles floating relaxed.
A tiny towel rests on top of its dome (Japanese onsen style). Steam rises
around it. Its face is pure bliss — mouth in a contented "ahhh." A wooden
bucket and ladle sit at the pool's edge. Expression: ultimate relaxation.

Background: outdoor hot spring (onsen) by the sea at dusk. Steam rising from
the natural rock pool. Wooden fence. Bamboo water feature. Orange dusk sky
with first stars. Warm and peaceful Japanese onsen atmosphere.""" },

  'easy+_8': { 'frame': 'common', 'prompt': S + """Character: A deep indigo/navy-purple (NOT brown) crab creature — same species
but rare purple variant. Glossy deep blue-purple body with silver accents.
Large sparkling electric-blue eyes with GEAR-SHAPED highlights.

Story: This purple crab is a mad scientist inventor! It wears tiny brass
goggles pushed up on its head. One pincer holds a bubbling beaker with green
liquid, the other adjusts a small contraption made of gears and springs.
Colorful smoke puffs from the invention. Its workbench is covered with tiny
tools, springs, and blueprints. Expression: excited "eureka!" moment.

Background: a cluttered inventor's workshop on the dock. Wooden workbench with
tools. Beakers and test tubes. Small machines. Blueprints on walls. Warm lamp.
Green bubbling potion. Steam and colored smoke. Creative chaos atmosphere.""" },

  'easy+_9': { 'frame': 'uncommon', 'prompt': S + """Character: A warm golden-green/olive (NOT purple) sea dragon creature — same
species but rare golden-green variant. Glossy olive-gold body. A silver crown.
Small wings. Large sparkling gentle warm green eyes with SOFT STAR highlights
(kind, not fierce). Rosy cheeks more prominent — this is the gentle side.

Story: The terrifying storm guardian has a secret — it LOVES baking sweets.
In its underwater cave, it carefully places tiny cupcakes on a tray, each
decorated with a different sea creature design. Its tail curls around a mixing
bowl. A chef's hat sits adorably over its crown. Tiny sea creatures line up
eagerly waiting for treats. Expression: gentle motherly pride in its baking.

Background: cozy underwater cave turned bakery. Stone oven glowing warm.
Shelves of cupcakes, cookies, and sea-themed pastries. Tiny fish and seahorses
waiting in line. Warm golden light. Underwater bakery fantasy atmosphere.""" },
}

FRAME_MAP = {
    'common': 'cards/frame_common.png',
    'uncommon': 'cards/frame_uncommon.png',
    'rare': 'cards/frame_rare.png',
}

def generate_image(prompt, output_path):
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}'
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE", "TEXT"]}
    }
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    resp = urllib.request.urlopen(req, context=CTX, timeout=180)
    result = json.loads(resp.read())
    for candidate in result.get('candidates', []):
        for part in candidate.get('content', {}).get('parts', []):
            if 'inlineData' in part:
                img_data = base64.b64decode(part['inlineData']['data'])
                # Convert JPEG to PNG for consistency
                from io import BytesIO
                img = Image.open(BytesIO(img_data))
                img.save(output_path, 'PNG')
                print(f'  OK: {output_path} ({os.path.getsize(output_path)//1024}KB)')
                return True
    print(f'  FAILED: {output_path}')
    return False

def compose_card(art_path, frame_path, output_path):
    frame = Image.open(frame_path).convert('RGBA')
    art = Image.open(art_path).convert('RGBA')
    tw, th = frame.size
    pixels = frame.load()
    mask = Image.new('L', (tw, th), 0); mask_px = mask.load()
    visited = set(); queue = deque()
    cx, cy = tw // 2, th // 2
    queue.append((cx, cy)); visited.add((cx, cy))
    while queue:
        x, y = queue.popleft()
        r, g, b, a = pixels[x, y]
        if r > 220 and g > 220 and b > 220:
            mask_px[x, y] = 255
            for nx, ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0 <= nx < tw and 0 <= ny < th and (nx,ny) not in visited:
                    visited.add((nx, ny)); queue.append((nx, ny))
    art_resized = art.resize((tw, th), Image.LANCZOS)
    card = Image.new('RGBA', (tw, th), (0, 0, 0, 255))
    card.paste(art_resized, (0, 0), mask)
    fwh = frame.copy(); fp = fwh.load()
    for y in range(th):
        for x in range(tw):
            if mask_px[x, y] == 255: fp[x, y] = (0, 0, 0, 0)
    card.paste(fwh, (0, 0), fwh)
    card.convert('RGB').save(output_path, quality=95)
    print(f'  Composed: {output_path} ({os.path.getsize(output_path)//1024}KB)')

def main():
    targets = list(CARDS.keys())
    if len(sys.argv) > 1:
        targets = [k for k in targets if sys.argv[1] in k]
    os.makedirs('cards/thumb', exist_ok=True)

    for i, card_id in enumerate(targets):
        info = CARDS[card_id]
        # EASY+_0 → raw file: cards/raw_easy+_0.png, card: cards/easy+_0.png
        safe_id = card_id.replace('+', '_plus')
        raw_path = f'cards/raw_{safe_id}.png'
        final_path = f'cards/{safe_id}.png'
        thumb_path = f'cards/thumb/{safe_id}.jpg'
        frame_path = FRAME_MAP[info['frame']]

        print(f'[{i+1}/{len(targets)}] {card_id}')
        ok = generate_image(info['prompt'], raw_path)
        if not ok:
            print(f'  Retrying in 3s...')
            time.sleep(3)
            ok = generate_image(info['prompt'], raw_path)
        if ok:
            compose_card(raw_path, frame_path, final_path)
            img = Image.open(final_path).convert('RGB').resize((120, 168), Image.LANCZOS)
            img.save(thumb_path, 'JPEG', quality=80)
            print(f'  Thumb: {thumb_path}')
        if i < len(targets) - 1:
            time.sleep(2)

    print(f'\nDone! Generated {len(targets)} cards.')

if __name__ == '__main__':
    main()
