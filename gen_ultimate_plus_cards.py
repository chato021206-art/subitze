#!/usr/bin/env python3
"""Generate ULTIMATE+ card images using Gemini Nano Banana 2."""
import urllib.request, json, os, ssl, base64, time, sys
from PIL import Image
from collections import deque
from io import BytesIO

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
IMPORTANT: This is a '+' variant — alternate color with a completely different scene.

"""

CARDS = {
  'ultimate_plus_0': { 'frame': 'common', 'prompt': S + """Character: A warm coral-pink (NOT ice-blue) rabbit — the off-duty color variant.
Glossy soft coral-pink body. Long ears drooping down limply (not trailing like a
comet). Large pink eyes CLOSED in deep sleep with tiny Zzz bubbles floating up.
It is curled up asleep on Saturn's rings, using them as a hammock. A small
mailbag serves as its pillow. Drool droplet on cheek. Totally exhausted but
content expression. Background: Saturn and its magnificent rings from close up.
The rabbit nestled in the ring particles. Stars and other planets visible.
Peaceful cosmic nap time. Warm golden cosmic light.""" },

  'ultimate_plus_1': { 'frame': 'common', 'prompt': S + """Character: A golden-amber (NOT silver-white) owl — the party-mode variant.
Glossy warm golden body with sparkly feathers. NO spectacles — replaced by
cool DJ headphones on its head. Large sparkling golden eyes with MUSICAL NOTE
highlights, wide open with excitement. Small wings operating a tiny turntable/
DJ deck with a vinyl record. Colorful sound waves and music notes radiate outward.
Expression: huge grin, totally out of character — the quiet librarian going wild.
Background: a cosmic dance floor on an asteroid. Colorful disco lights and laser
beams. Tiny star creatures dancing around. A disco ball made of a small moon
reflects light everywhere. Party atmosphere in space.""" },

  'ultimate_plus_2': { 'frame': 'common', 'prompt': S + """Character: An emerald-green (NOT metallic-red) woodpecker — the gardener variant.
Glossy metallic emerald-green body. Green crest feathers. Small golden beak.
Large sparkling green eyes with SPROUT/LEAF shaped highlights, glistening with
a single happy tear. It sits beside a tiny glass dome on the Mars surface. Inside
the dome, a single small flower blooms — the first life on Mars in a billion years.
The woodpecker gazes at the flower with overwhelming emotion and tender pride.
A tiny watering can sits nearby. Expression: tearful joy, life-changing discovery.
Background: red Mars landscape, but with this one tiny glass dome containing
green life. The contrast of red desert and green sprout. Sunset on Mars.""" },

  'ultimate_plus_3': { 'frame': 'common', 'prompt': S + """Character: A sunset-orange (NOT deep blue) whale — the surfer variant.
Glossy warm orange body with golden wave patterns. Small flippers spread wide
for balance. Large sparkling orange eyes with WAVE-CREST highlights, wide open
with thrilling excitement. It rides a massive cosmic gravity wave made of
stardust, tail flipping up a spray of sparkling star particles. Mouth wide open
in a joyful shout of pure joy. Expression: ecstatic adrenaline rush.
Background: cosmic gravity waves — shimmering golden-orange energy waves rolling
through space. Stardust sprays like ocean surf. Stars streak past from the speed.
Galaxies visible in the distance. Cosmic surfing action scene.""" },

  'ultimate_plus_4': { 'frame': 'uncommon', 'prompt': S + """Character: An ice-silver (NOT amber-gold) lion — the sleeping kitten variant.
Glossy pale silver-blue body. The once-fearsome mane is now fluffy and messy
like bedhead. NO lightning — just soft fluffy fur. Tiny pink paw pads visible
as it lies on its back. Large silver eyes CLOSED peacefully, long eyelashes.
It is curled up on a soft cloud bed, kneading the cloud with tiny paws. A small
drool droplet at the corner of its smile. A tiny milk bottle nearby. Expression:
the most peaceful, vulnerable, adorable sleeping kitten face imaginable —
completely opposite to the fierce storm king.
Background: above Jupiter's clouds at night. Soft pastel clouds form a cozy bed.
Stars twinkle gently above. No storms, no lightning — just peaceful calm. A
crescent moon casts gentle light. Cozy cosmic nursery atmosphere.""" },

  'ultimate_plus_5': { 'frame': 'common', 'prompt': S + """Character: A turquoise-cyan (NOT purple-pink) octopus — the chef variant.
Glossy turquoise body. Eight tentacles each doing a different cooking task
simultaneously: stirring a pot, sprinkling star dust, tasting soup, holding a
recipe book, flipping a cosmic pancake, chopping a meteor, whisking stardust
cream, adjusting the heat. A tiny white chef hat on its head. A small apron
tied around its round body. Large sparkling cyan eyes with STAR-SPARKLE
highlights, focused in multitasking concentration. Expression: busy but loving it.
Background: a cosmic kitchen floating in space. Pots and pans made of asteroid
metal. A stove with nebula-gas flames. Shelves of cosmic ingredients in jars.
Steam and sparkles rise from the pots. Cosmic cooking atmosphere.""" },

  'ultimate_plus_6': { 'frame': 'common', 'prompt': S + """Character: A midnight-blue (NOT flame-orange) bird — the nighttime variant.
Glossy deep midnight-blue body that blends with dark space. Small wings with
tips that glow with tiny starlight points. A crest of soft blue starlight instead
of flame. Large sparkling deep blue eyes with TINY STAR highlights scattered
like a night sky. It delicately places tiny glowing stars into dark patches of
space with its beak, one by one, illuminating the darkness. A small basket of
collected starlight hangs from its wing. Expression: quiet dedication and care.
Background: a very dark corner of space with few stars. The bird is adding new
tiny stars, creating a trail of new light. Gentle blue-white starlight.""" },

  'ultimate_plus_7': { 'frame': 'common', 'prompt': S + """Character: A warm honey-amber (NOT dark navy) bear — the beekeeper variant.
Glossy warm amber-golden body that seems to glow with inner honey light. Small
round ears. NO constellation patterns — instead, body has a warm honeycomb
shimmer. Large sparkling warm amber eyes with HONEYCOMB highlights. It hugs a
large glass jar filled with glowing golden "star honey." Its mouth and paws are
sticky with honey as it tastes it with pure delight. A tiny space bee buzzes
nearby. Expression: blissful foodie happiness, honey all over its face.
Background: a cosmic apiary — tiny beehives attached to stars, connected by
golden light-threads. Space bees buzz around. Jars of golden star honey on
floating shelves. Warm golden honey-light fills the scene.""" },

  'ultimate_plus_8': { 'frame': 'common', 'prompt': S + """Character: A divine three-eyed guardian dog deity — the "Liberated Mahakara"
white-light variant. Glossy radiant white-platinum body that EMITS soft holy
light instead of absorbing it. A warm golden lotus aura halo behind its head.
Small pointed ears with golden tips. A fluffy tail curled gracefully, with
golden sparkles drifting from its tip. THREE EYES: two large sparkling warm
golden eyes in normal positions, plus a THIRD EYE vertically centered on its
forehead, larger and glowing with brilliant white-gold mystical light, marked
with a tiny golden bindi dot above it. All three eyes have RADIANT MANDALA
highlights (concentric rings of light like a sacred geometric pattern). It
sits in a peaceful meditation pose on a giant glowing golden lotus flower
floating in space. Tiny golden prayer beads float around its neck. Its small
front paws are pressed gently together as if in blessing. Expression: serene,
compassionate, deeply enlightened — the opposite of the lonely howl. A single
tear of golden joy on its cheek. Background: a sacred cosmic temple in deep
space. Golden mandala patterns of light radiate outward filling the sky.
Distant galaxies form a halo. Floating lotus petals drift through the scene.
Warm golden divine light fills everything. The atmosphere of cosmic
enlightenment and infinite compassion.""" },

  'ultimate_plus_9': { 'frame': 'rare', 'prompt': S + """Character: A soft pastel-purple (NOT dark rainbow) dragon — the playful variant.
Glossy pale lavender-purple body with soft pastel star patterns instead of
intense galaxy swirls. Small pastel-colored wings. Cute small horns. Large
sparkling soft purple eyes with TOY-PLANET highlights (tiny colorful spheres
reflected in iris). It sits surrounded by miniature toy planets — rolling a tiny
Jupiter with one paw, wearing Saturn's ring on a claw like a bracelet, stacking
tiny moons into a tower. Expression: totally absorbed in play, tongue slightly
out in concentration. Rosy cheeks prominent. Background: a cozy cosmic playroom.
Shelves of miniature planet models. A toy box overflowing with tiny stars. Soft
pastel nebula wallpaper. Plush cosmic toys scattered around.""" },

  'ultimate_plus_10': { 'frame': 'rare', 'prompt': S + """Character: A warm rose-quartz pink (NOT clear crystal) creature — the baker variant.
Glossy soft rose-pink translucent body with a warm inner glow instead of rainbow
universe. Gentle rounded form with no sharp crystal facets — soft and warm.
A tiny white apron tied around its body. A small chef hat. Large sparkling warm
rose-pink eyes with STAR-COOKIE shaped highlights. It holds a baking tray of
perfectly baked star-shaped cookies, each cookie glowing with golden warmth.
A few cookie crumbs on its cheek. A mixing bowl and flour dust nearby. Expression:
the warmest, most nurturing proud mama smile. Background: a cozy cosmic kitchen
inside a crystal cave. A warm oven glowing. Shelves of star-shaped cookies. Tiny
cosmic creatures (baby versions of all Ultimate characters) lining up eagerly for
cookies. Warm golden baking light. The most heartwarming scene in the game.""" },
}

FRAME_MAP = {'common':'cards/frame_common.png','uncommon':'cards/frame_uncommon.png','rare':'cards/frame_rare.png'}

def generate_image(prompt, output_path):
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}'
    payload = {"contents":[{"parts":[{"text":prompt}]}],"generationConfig":{"responseModalities":["IMAGE","TEXT"]}}
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers={'Content-Type':'application/json'})
    resp = urllib.request.urlopen(req, context=CTX, timeout=180)
    result = json.loads(resp.read())
    for c in result.get('candidates',[]):
        for p in c.get('content',{}).get('parts',[]):
            if 'inlineData' in p:
                img_data = base64.b64decode(p['inlineData']['data'])
                img = Image.open(BytesIO(img_data))
                img.save(output_path, 'PNG')
                print(f'  OK: {output_path} ({os.path.getsize(output_path)//1024}KB)')
                return True
    print(f'  FAILED: {output_path}')
    return False

def compose_card(art_path, frame_path, output_path):
    frame = Image.open(frame_path).convert('RGBA')
    art = Image.open(art_path).convert('RGBA')
    tw, th = frame.size; pixels = frame.load()
    mask = Image.new('L', (tw, th), 0); mask_px = mask.load()
    visited = set(); queue = deque()
    queue.append((tw//2, th//2)); visited.add((tw//2, th//2))
    while queue:
        x, y = queue.popleft(); r, g, b, a = pixels[x, y]
        if r > 220 and g > 220 and b > 220:
            mask_px[x, y] = 255
            for nx, ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0 <= nx < tw and 0 <= ny < th and (nx,ny) not in visited:
                    visited.add((nx, ny)); queue.append((nx, ny))
    art_r = art.resize((tw, th), Image.LANCZOS)
    card = Image.new('RGBA', (tw, th), (0, 0, 0, 255))
    card.paste(art_r, (0, 0), mask)
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
        raw_path = f'cards/raw_{card_id}.png'
        final_path = f'cards/{card_id}.png'
        thumb_path = f'cards/thumb/{card_id}.jpg'
        frame_path = FRAME_MAP[info['frame']]
        print(f'[{i+1}/{len(targets)}] {card_id}')
        ok = generate_image(info['prompt'], raw_path)
        if not ok:
            time.sleep(3); ok = generate_image(info['prompt'], raw_path)
        if ok:
            compose_card(raw_path, frame_path, final_path)
            Image.open(final_path).convert('RGB').resize((120,168),Image.LANCZOS).save(thumb_path,'JPEG',quality=80)
            print(f'  Thumb: {thumb_path}')
        if i < len(targets) - 1:
            time.sleep(2)
    print(f'\nDone! Generated {len(targets)} cards.')

if __name__ == '__main__':
    main()
