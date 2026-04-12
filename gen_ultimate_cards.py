#!/usr/bin/env python3
"""Generate ULTIMATE card images using Gemini Nano Banana 2."""
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

"""

CARDS = {
  'ultimate_0': { 'frame': 'common', 'prompt': S + """Scene: A cute round rabbit creature with glossy ice-blue crystalline body that
sparkles like comet ice. Long ears that trail behind like a comet's tail, glowing
with blue-white light and leaving a sparkling trail. Large sparkling ice-blue eyes
with SHOOTING-STAR shaped highlights (streaking light trails in the iris).
It races through space at incredible speed, a small letter held in its mouth.
Its feet leave a rainbow-colored trail of stardust behind. Expression: determined
and joyful — the fastest delivery in the universe.
Background: deep space with countless stars. Colorful nebulae in the distance.
A small cute planet visible ahead as the destination. Shooting stars streak past.
The rabbit's comet trail creates a brilliant arc across the starfield.""" },

  'ultimate_1': { 'frame': 'common', 'prompt': S + """Scene: A cute round owl creature with glossy silvery-white body that glows with
soft moonlight. Small silver wings folded at sides. Downy feathers shimmer with
pearlescent sheen. Round spectacles perched on its face. Large sparkling silver
eyes with CRESCENT MOON shaped highlights (the moon's phases reflected in iris).
It sits in a lunar library, carefully turning pages of an ancient star atlas with
one tiny wing. Star charts and constellation maps are spread around it. A cup of
starlight tea steams beside it. Expression: serene scholarly concentration.
Background: a magical library inside a moon crater. Bookshelves carved from lunar
rock, filled with glowing scrolls. A round window shows Earth in the distance.
Soft silver moonlight illuminates everything. Floating dust motes sparkle like stars.""" },

  'ultimate_2': { 'frame': 'common', 'prompt': S + """Scene: A cute round woodpecker creature with glossy metallic-red body like
polished Mars rock. A magnificent red crest/mohawk of metallic feathers stands
tall on its head. Small but strong beak with a golden tip. Tiny wings at sides.
Large sparkling deep red eyes with HEXAGONAL/FOSSIL-SHAPED highlights.
It has just pecked open a Mars rock and discovered a glowing ancient fossil
inside — a tiny spiral shell that shimmers with golden light. It holds up the
glowing fossil with both tiny wings, crest feathers standing straight up with
excitement. Expression: wide-eyed astonishment and pure "EUREKA!" joy.
Background: dramatic Mars canyon wall with layers of red rock. The pecked-open
hole in the rock face glows golden. Red dust particles float in amber sky.
Scattered rock chips from the pecking. Two small moons visible above.""" },

  'ultimate_3': { 'frame': 'common', 'prompt': S + """Scene: A cute round whale creature with glossy deep navy-blue body with subtle
swirling patterns like Neptune's atmosphere. Small flippers and a gentle whale
tail. Lighter blue belly. Large sparkling deep blue eyes with SWIRL/VORTEX
shaped highlights (like the Great Dark Spot storm). Its mouth is slightly open,
singing — visible sound waves ripple outward as musical notes made of starlight.
Tiny newborn stars glow and orbit around it, lulled by its lullaby.
Expression: gentle, maternal, singing softly with closed eyes and peaceful smile.
Background: a vast colorful nebula — swirling clouds of blue, purple, and pink
cosmic gas. The whale swims through the nebula like an ocean. Tiny bright baby
stars twinkle around it. Deep space visible beyond the nebula edges.""" },

  'ultimate_4': { 'frame': 'uncommon', 'prompt': S + """Scene: A cute but imposing round lion creature with glossy amber-gold body
covered in swirling band patterns like Jupiter's atmosphere. A magnificent mane
that flows and crackles with lightning bolts. Small but regal paws. Large
sparkling amber eyes with GREAT RED SPOT storm-swirl highlights (a massive
storm reflected in the iris). Tiny lightning bolts arc between the strands of
its mane. It sits on a throne of swirling clouds, one paw raised in challenge.
Expression: regal authority and fierce pride — "Can you survive my storm?"
Background: the surface of Jupiter — massive swirling cloud bands in orange,
amber, and cream. The Great Red Spot visible as a massive storm nearby.
Lightning flashes within the clouds. Awe-inspiring scale and power.""" },

  'ultimate_5': { 'frame': 'common', 'prompt': S + """Scene: A cute round octopus creature with glossy purple-pink translucent body
that shifts between purple, magenta, and pink like nebula gas. Eight short
tentacles, each glowing a different color (red, blue, purple, gold, green, pink,
cyan, orange). Large sparkling purple eyes with NEBULA-CLOUD shaped highlights
(swirling cosmic gas patterns in the iris). It floats in space, tentacles spread
wide, painting a new nebula into existence. Each tentacle leaves a different
colored trail of cosmic gas. Expression: artistic concentration with a pleased
smile. Background: deep space. The octopus is surrounded by its half-finished
nebula creation — swirling colorful gas clouds in brilliant colors. Stars
twinkle through the gas. A cosmic art studio in space.""" },

  'ultimate_6': { 'frame': 'common', 'prompt': S + """Scene: A cute round bird creature with glossy flame-orange body that radiates
warm golden light. Small wings spread wide, each feather tip burning with
solar flare fire. A crest of golden flame on its head like a solar corona.
Large sparkling golden-orange eyes with SOLAR FLARE/PROMINENCE shaped highlights
(arcing flame patterns in the iris). It spreads its wings at the horizon of a
small planet, creating a spectacular sunrise. Light rays burst from behind it.
Expression: majestic pride — "Behold, I bring the dawn!"
Background: the curved horizon of a small colorful planet. The bird is
silhouetted against the rising sun, which appears to emerge from its wings.
Golden light rays fan out dramatically. Stars still visible in the dark sky
above. A breathtaking cosmic sunrise scene.""" },

  'ultimate_7': { 'frame': 'common', 'prompt': S + """Scene: A cute round bear creature with glossy dark navy body that looks like
the night sky itself — tiny stars and constellation patterns actually glow on
its surface. The Big Dipper / Ursa Major pattern is visible on its belly,
glowing with connected star-lines. Small rounded ears. Large sparkling deep
blue eyes with NORTH STAR / POLARIS highlights (a single bright guiding point
of light in each iris). It floats in space, one tiny paw reaching up to connect
two stars with a glowing golden line, creating a new constellation.
Expression: focused and satisfied — a craftsman admiring its work.
Background: pure deep space filled with stars. Several completed constellations
glow with connected lines nearby. The bear's paw touches a star, and a golden
line extends to the next star. Magical constellation-weaving atmosphere.""" },

  'ultimate_8': { 'frame': 'common', 'prompt': S + """Scene: A cute round dog/wolf creature with glossy jet-black body so dark it
seems to absorb light. A faint purple-violet aura/glow outlines its silhouette.
Small pointed ears. A fluffy tail with a glowing purple tip — the only color.
A thick fluffy mane of soft fur around its chest and neck (like a lion's ruff
or a Pomeranian's chest fluff), extra puffy and huggable.
THREE EYES: two large sparkling eyes in normal positions, plus a THIRD EYE
vertically centered on its forehead — the third eye glows with bright purple
mystical light, slightly larger and more intense than the other two. All three
eyes have EVENT HORIZON highlights (a bright ring of light around a dark
center, like the accretion disk of a black hole). It sits at the edge of a
massive black hole, head tilted up in a small lonely howl. Gravity
distortion bends the starlight around it. Despite looking fearsome, its
expression is deeply lonely and yearning for connection. A single tear of
purple light on its cheek. Background: the edge of a black hole — an enormous
dark sphere with a brilliant glowing accretion disk of light swirling around it.
Stars are distorted by gravity lensing. Deep space. Hauntingly beautiful.""" },

  'ultimate_9': { 'frame': 'rare', 'prompt': S + """Scene: A majestic yet adorable round dragon creature whose body IS a galaxy —
glossy dark body filled with billions of tiny twinkling stars, swirling nebulae,
and spiral galaxy arms visible within its translucent form. Magnificent spread
wings that contain entire star fields. Two grand horns that curve like spiral
galaxy arms. A tail that trails stardust and cosmic gas. Large sparkling eyes
with SPIRAL GALAXY highlights (an entire galaxy rotating within each iris).
Despite its cosmic scale, it has rosy cheeks and a gentle expression. It
carefully cradles several tiny sleeping shooting stars on one wing, nurturing
them. Expression: ancient wisdom combined with tender maternal care.
Background: the vast cosmos. Other galaxies visible in the distance. A river of
stardust flows around the dragon. Golden cosmic light. Awe-inspiring majesty.""" },

  'ultimate_10': { 'frame': 'rare', 'prompt': S + """Scene: A transcendently beautiful round creature made entirely of clear crystal
— like a living diamond or prism. Its transparent body contains an entire
miniature universe inside: swirling rainbow nebulae, tiny galaxies, sparkling
stars, all visible through the crystal surface. When light hits it, rainbow
prisms scatter in all directions. No horns, no wings — just pure crystalline
perfection. Large sparkling eyes with PRISM/RAINBOW highlights (white light
splitting into all colors of the spectrum within the iris). Its expression is
the warmest, most loving smile in the entire game — a cosmic mother welcoming
its children home. "You made it." Tiny silhouettes of all the other Ultimate
creatures (rabbit, owl, woodpecker, whale, lion, octopus, bird, bear, dog, dragon)
are visible as constellations within its crystal body.
Background: a realm of pure light — not space, but a dimension of crystalline
light beyond space. Rainbow prismatic light fills everything. Crystal formations
float in the air. This is where the universe began. Transcendent beauty.""" },
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
    for c in result.get('candidates', []):
        for p in c.get('content', {}).get('parts', []):
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
    fwh = frame.copy()
    fp = fwh.load()
    for y in range(th):
        for x in range(tw):
            if mask_px[x, y] == 255:
                fp[x, y] = (0, 0, 0, 0)
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
