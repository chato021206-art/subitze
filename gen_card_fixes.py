#!/usr/bin/env python3
"""Regenerate cards for color balance fix — 11 cards across EASY/NORMAL/HARD."""
import urllib.request, json, os, ssl, base64, time, sys
from PIL import Image
from collections import deque

API_KEY = os.environ.get('GOOGLE_API_KEY', '')
MODEL = 'imagen-4.0-generate-001'
CTX = ssl.create_default_context()

STYLE = """Super deformed cute chibi blob creature, anime mobile game card illustration,
extremely round soft body with tiny stubby limbs, large sparkling anime eyes
with star-shaped highlights, rosy cheeks, glossy skin with specular highlights,
digital painting, vibrant saturated colors, rich detailed background that fills
the ENTIRE image edge to edge with NO white borders or margins anywhere,
creature fills about 55-60% of the frame vertically and is centered with clear
margins from all edges so it does not touch or overlap the borders,
portrait orientation 7:10 aspect ratio, no text, no frame, no border, no UI elements.

"""

CARDS = {
    # === EASY ===
    'easy_3': {
        'prompt': STYLE + """A cute round sea turtle creature with glossy turquoise-green shell and lighter
mint-green belly. The shell has a beautiful hexagonal pattern with golden edge highlights.
Large gentle dark-green eyes with star-shaped highlights and long eyelashes. Tiny flippers.
It is on a moonlit sandy beach, shyly digging a small hole in the sand with one flipper,
looking back at the viewer with an embarrassed blush. Small flipper tracks trail behind it.
Background: a beautiful moonlit beach at night, dark blue sky full of twinkling stars,
gentle waves lapping at the shore in the distance, palm tree silhouettes on the sides,
the full moon casting silver light on the wet sand. Warm and peaceful atmosphere.""",
        'frame': 'cards/frame_common.png',
    },
    'easy_7': {
        'prompt': STYLE + """A cute round jellyfish creature with a translucent lavender-purple glossy dome cap
and delicate trailing tentacles below. The dome has subtle iridescent rainbow sheen.
Large sparkling purple anime eyes with star highlights, rosy cheeks, gentle happy smile.
The creature is SMALL relative to the frame — it floats in the upper-center of the image
with plenty of space around it, especially above. The tentacles trail down gracefully.
The creature takes up only about 50% of the image height, leaving generous margins.
Background: deep ocean blue water gradient from lighter blue at top to darker navy below.
Tiny glowing particles (bioluminescence) float around. Coral reef hints at the very bottom.
Shafts of sunlight filter down from above. Serene underwater atmosphere.""",
        'frame': 'cards/frame_common.png',
    },

    # === NORMAL ===
    'normal_2': {
        'prompt': STYLE + """A cute round firefly creature with a glowing lime-yellow translucent body.
Its round bottom glows brightly with warm yellow-green bioluminescent light, creating
a soft lantern-like radiance. Small translucent wings buzz on its back. Two tiny antennae
on top of its head with glowing tips. Large sparkling yellow-green eyes with star highlights.
It is flying through a dark nighttime forest, leaving a trail of glowing light particles
behind its tail. Its expression is cheerful and excited.
Background: a dark enchanted forest at night with tall shadowy trees. Dozens of tiny
firefly lights dot the darkness like floating stars. Soft green moss glows faintly on
tree trunks. A crescent moon peeks through the canopy. Magical and mystical atmosphere.""",
        'frame': 'cards/frame_common.png',
    },
    'normal_5': {
        'prompt': STYLE + """A cute round frog creature with glossy sky-blue body and white belly. Its body is
smooth and slightly transparent like blue glass. Large sparkling aqua-blue eyes with
star highlights. Rosy cheeks. A small golden crown sits tilted on its head. It sits on
a large green lily pad floating on a forest pond, puffing up its white throat pouch
while singing. Tiny colorful musical notes float upward from its mouth.
Background: a sunlit forest pond surrounded by lush green vegetation. Multiple lily pads
with small pink lotus flowers float on the crystal-clear water surface. Tall trees with
golden sunlight filtering through leaves. Dragonflies hover nearby. Peaceful and bright.""",
        'frame': 'cards/frame_common.png',
    },
    'normal_8': {
        'prompt': STYLE + """A cute round fox spirit creature with glossy warm amber-orange fur and a fluffy white
chest. A bushy fox tail with white tip that has small blue-white spirit flames (foxfire/
kitsunebi) flickering from the tail tip. Pointed fox ears with dark tips. Large sparkling
golden-amber eyes with star highlights. A mischievous grin showing one tiny fang.
It sits in a twilight autumn forest, one tiny paw raised as if casting a spell. Three
small blue-white spirit flames float around it in a circle.
Background: an autumn forest at dusk with trees in brilliant red, orange, and gold foliage.
A weathered red torii gate silhouette is visible in the misty background. Fallen maple
leaves carpet the ground. Warm golden-hour lighting with purple twilight sky above.
Mysterious and enchanting Japanese folklore atmosphere.""",
        'frame': 'cards/frame_common.png',
    },

    # === HARD ===
    'hard_1': {
        'prompt': STYLE + """A cute round scorpion creature with glossy sandy-beige/tan body like desert sand.
Its segmented tail curls up high above its head with a small stinger that glows faintly
orange. Two small pincers held up in a threatening but adorable pose. Dark brown markings
on its back in a natural camouflage pattern. Large sparkling amber-brown eyes with
star highlights. It emerges halfway from desert sand, tail raised high in warning.
Background: a vast desert landscape at golden sunset. Towering sand dunes stretch into
the distance under a dramatic orange-pink sky. Heat shimmer rises from the sand.
Scattered desert rocks and a lone dead tree. Warm golden light bathes everything.""",
        'frame': 'cards/frame_common.png',
    },
    'hard_2': {
        'prompt': STYLE + """A cute round falcon/hawk creature with brilliant golden-brown glossy plumage.
A white chest with golden-brown speckles. Small but fierce spread wings with darker
brown tips. A small curved golden beak. Sharp but adorable large golden eyes with
diamond-shaped highlights showing fierce determination. A tiny golden anklet on one foot.
It perches on a desert rock outcropping, body puffed up proudly, wings slightly spread.
Background: a dramatic desert canyon at sunrise. Towering sandstone cliffs in warm orange
and red layers. Distant pyramids visible on the horizon. The rising sun creates dramatic
golden rays cutting through morning haze. Eagles soar as tiny silhouettes in the sky.""",
        'frame': 'cards/frame_common.png',
    },
    'hard_5': {
        'prompt': STYLE + """A cute round crystal-scorpion creature with glossy teal/cyan body that shimmers
with an inner crystalline glow. Small crystalline segments along its back that catch
and refract light into rainbow sparkles. A curled tail with a glowing teal crystal tip.
Two small translucent pincers. Large sparkling emerald-teal eyes with gem-facet highlights.
It is inside a cavern, happily munching on a glowing teal crystal, mouth sparkling with
crystal dust. Tiny crystal shards float around its head.
Background: a spectacular crystal cavern with massive teal and cyan crystal formations
growing from walls and ceiling. Veins of glowing minerals run through the rock.
Underground pool reflects the crystal light. Magical blue-green luminescence everywhere.""",
        'frame': 'cards/frame_common.png',
    },
    'hard_6': {
        'prompt': STYLE + """A cute round bomb creature with glossy dark navy-blue body (NOT red). A metal cap
on top with a blue-tipped fuse that has bright blue-white sparks shooting from it.
The body is dark midnight blue with tiny star-like sparkle patterns on its surface.
Large panicked spiral eyes in pale blue, mouth open in a worried "oh no" expression,
a single blue sweat drop on its forehead. Tiny stubby feet.
Background: a desert landscape at night under a spectacular starry sky with the Milky Way
visible. Sand dunes in cool blue-gray moonlight. The blue sparks from the fuse illuminate
the nearby sand with blue light. A few shooting stars streak across the sky.
Dramatic nighttime atmosphere with cool blue tones throughout.""",
        'frame': 'cards/frame_common.png',
    },
    'hard_7': {
        'prompt': STYLE + """A cute round cobra creature with glossy jade-green/emerald body (NOT red). Beautiful
darker green scale pattern across its smooth round body. A lighter green belly.
A small jade-green cobra hood fans out behind its head with golden ornamental markings.
Large sparkling yellow-green slit-pupil eyes. A forked tongue flicks out playfully.
It is coiled in front of golden desert ruins, looking regal and mysterious.
Background: ancient golden desert ruins with hieroglyph-covered sandstone walls.
Sunlight streams through a crumbled doorway creating dramatic light shafts. Potted plants
with green vines creep along the ruins. Sand piles in corners. Warm golden afternoon light
contrasts beautifully with the green snake. Mysterious archaeological atmosphere.""",
        'frame': 'cards/frame_common.png',
    },
    'hard_8': {
        'prompt': STYLE + """A cute round mineral/crystal creature with glossy ice-blue/frost-blue body (NOT brown).
Its round body is covered in sparkling ice-blue and pale white crystal clusters that
grow from its surface like frozen flowers. The body has a translucent frosted glass quality.
Large sparkling diamond-blue eyes that look like cut sapphires with bright white star
highlights. A gentle peaceful smile. Tiny ice crystal feet.
Background: a mine tunnel with wooden support beams and old mining rails. But instead of
warm orange light, the tunnel glows with cool blue-white light from ice-blue crystal
formations growing along the walls. A mining lantern hangs from a beam casting warm light
that contrasts with the blue crystals. Mine cart on rails in the distance.""",
        'frame': 'cards/frame_common.png',
    },
    'hard_9': {
        'prompt': STYLE + """A majestic cute round fire demon creature with deep dark crimson body (darker and more
dramatic than typical red). Its body emanates an aura of blue-purple flames mixed with
traditional orange fire. Flame-shaped eyes that burn with inner blue-white fire at the
center, surrounded by orange flame iris. Two small dark horns. Sharp tiny fangs in a
fierce grin. The creature radiates overwhelming boss energy despite being adorably round.
Background: a volcanic arena with dark basalt pillars. Rivers of bright orange lava flow
on the ground. But dramatic tall pillars of BLUE fire rise on both sides, creating an
unusual and striking contrast with the orange lava. Dark volcanic ash clouds swirl above.
The blue and orange fire creates a spectacular dual-tone lighting effect. Epic boss arena.""",
        'frame': 'cards/frame_rare.png',
    },
}

def generate_image(prompt, output_path):
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:predict?key={API_KEY}'
    payload = {
        "instances": [{"prompt": prompt}],
        "parameters": {"sampleCount": 1, "aspectRatio": "3:4", "personGeneration": "dont_allow"}
    }
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    resp = urllib.request.urlopen(req, context=CTX, timeout=180)
    result = json.loads(resp.read())
    preds = result.get('predictions', [])
    if preds and preds[0].get('bytesBase64Encoded'):
        img_data = base64.b64decode(preds[0]['bytesBase64Encoded'])
        with open(output_path, 'wb') as f:
            f.write(img_data)
        print(f'  Generated: {output_path} ({len(img_data)//1024}KB)')
        return True
    print(f'  FAILED: {output_path}')
    return False

def compose_card(art_path, frame_path, output_path):
    frame = Image.open(frame_path).convert('RGBA')
    art = Image.open(art_path).convert('RGBA')
    tw, th = frame.size
    frame = frame.resize((tw, th), Image.LANCZOS)
    pixels = frame.load()
    mask = Image.new('L', (tw, th), 0)
    mask_px = mask.load()
    visited = set()
    queue = deque()
    cx, cy = tw // 2, th // 2
    queue.append((cx, cy))
    visited.add((cx, cy))
    while queue:
        x, y = queue.popleft()
        r, g, b, a = pixels[x, y]
        if r > 220 and g > 220 and b > 220:
            mask_px[x, y] = 255
            for nx, ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0 <= nx < tw and 0 <= ny < th and (nx,ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    art_resized = art.resize((tw, th), Image.LANCZOS)
    card = Image.new('RGBA', (tw, th), (0, 0, 0, 255))
    card.paste(art_resized, (0, 0), mask)
    frame_with_hole = frame.copy()
    fh_px = frame_with_hole.load()
    for y in range(th):
        for x in range(tw):
            if mask_px[x, y] == 255:
                fh_px[x, y] = (0, 0, 0, 0)
    card.paste(frame_with_hole, (0, 0), frame_with_hole)
    card.convert('RGB').save(output_path, quality=95)
    print(f'  Composed: {output_path} ({os.path.getsize(output_path)//1024}KB)')

def make_thumb(src, dst):
    img = Image.open(src).convert('RGB')
    img = img.resize((120, 168), Image.LANCZOS)
    img.save(dst, 'JPEG', quality=80)

def main():
    targets = list(CARDS.keys())
    if len(sys.argv) > 1:
        targets = [k for k in targets if sys.argv[1] in k]

    for i, card_id in enumerate(targets):
        info = CARDS[card_id]
        raw_path = f'cards/raw_{card_id}.png'
        final_path = f'cards/{card_id}.png'
        thumb_path = f'cards/thumb/{card_id}.jpg'

        print(f'[{i+1}/{len(targets)}] {card_id}')
        ok = generate_image(info['prompt'], raw_path)
        if not ok:
            print(f'  Retrying...')
            time.sleep(5)
            ok = generate_image(info['prompt'], raw_path)

        if ok:
            compose_card(raw_path, info['frame'], final_path)
            make_thumb(final_path, thumb_path)
            print(f'  Thumb: {thumb_path}')

        if i < len(targets) - 1:
            time.sleep(2)

    print('\nAll done!')

if __name__ == '__main__':
    main()
