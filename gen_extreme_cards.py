#!/usr/bin/env python3
"""Generate EXTREME card images using Imagen 4 API + frame composition."""
import urllib.request, json, os, ssl, base64, time, sys
from PIL import Image

API_KEY = os.environ.get('GOOGLE_API_KEY', '')
MODEL = 'imagen-4.0-generate-001'
CTX = ssl.create_default_context()

STYLE_PREFIX = """Super deformed cute chibi blob creature, anime mobile game card illustration,
extremely round soft body with tiny stubby limbs, large sparkling anime eyes
with star-shaped highlights, rosy cheeks, glossy skin with specular highlights,
digital painting, vibrant saturated colors, rich detailed background,
portrait orientation 7:10 aspect ratio, no text, no frame, no border, no UI elements.

"""

PROMPTS = {
    1: STYLE_PREFIX + """A cute sea-dragon creature with bright cerulean blue glossy round body, small
golden crown-like horn on its forehead, tiny fin-like arms, and a short fish tail.
Its belly is lighter aqua. Deep ocean-blue eyes with concentric ripple-ring highlights.
It is floating belly-up in a sacred temple fountain, mouth wide open in a huge
contented yawn showing small rounded teeth. Eyes squeezed shut into happy crescents.
One tiny fin dangles lazily over the ornate stone edge of the fountain.
Three golden coins rest on its belly, tossed by worshippers. Floating lotus
flowers and lily pads surround it. More golden coins glimmer at the bottom of
the crystal-clear water.
Background: an octagonal sacred fountain in a Near Eastern temple courtyard.
Golden fish sculptures serve as water spouts. White marble rim entwined with
jasmine vines. Two turquoise-tiled minarets rise in the distance against a
clear blue sky. Sunlight sparkles on the water surface.""",

    2: STYLE_PREFIX + """An emerald-green baby divine bird creature with fluffy downy feathers covering
its round body. Two elegantly curling plume feathers on top of its head. Small
but proud wings. Ruby-red eyes with wind-swirl spiral highlights.
It is clinging to the golden finial atop a temple minaret spire. Strong wind
tilts its body sideways, feathers blown dramatically upward. Colorful Tibetan-
style prayer flags (red, blue, yellow, green, white) have tangled around its
body and wings. Its expression is wide-eyed bewilderment but its tiny talons
grip the finial determinedly. A few loose feathers blow away in the wind.
Background: a view from the spire top looking down over a Near Eastern coastal
city with white-walled terraced rooftops and golden domes spread below. Dramatic
sunset sky with towering cumulus clouds painted orange and pink. Prayer flag
lines stretch between towers. Visible wind streaks cross the scene.""",

    3: STYLE_PREFIX + """A golden-furred sacred monkey creature with warm amber-orange glossy round
body and cream-colored belly. A curly tail, small round ears. Honey-brown
eyes with star highlights, one eye is closed in a mischievous wink.
It sits triumphantly atop a towering pile of stolen tropical fruits — mangoes,
papayas, coconuts, and bananas heaped together. It holds a half-peeled banana
in one tiny hand, cheeks puffed out and bulging with food, giving a cheeky
wink directly at the viewer. Banana peels are scattered around.
Background: a vibrant tropical fruit market with red-and-white striped awning
overhead, wooden crates of colorful fruits displayed at a vendor's stall.
Palm trees and frangipani flowers frame the edges. Warm afternoon sunlight
bathes the scene.""",

    4: STYLE_PREFIX + """A cute but imposing round elephant creature with warm chocolate-brown glossy body.
Large floppy ears with pink inner rims, a short thick trunk raised high, two small
ivory tusks. A golden chain necklace with a jade medallion hangs around its neck.
Deep amber eyes with golden flame-shaped highlights showing brave determination.
It stands guard before a massive ornate temple gate, having just rung a golden
temple bell with the tip of its raised trunk. Visible ring-shaped shockwaves
(sound ripples) radiate outward from the bell. One foot stamps forward powerfully,
cracking the stone floor tiles in a radiating spider-web pattern. Its expression
is fierce yet adorable, eyebrows furrowed in a resolute look.
Background: the grand entrance gate of a Near Eastern temple. Towering stone
pillars carved with lotus and elephant relief motifs flank both sides. Golden
incense braziers emit curling blue smoke. A carved semicircular arch crowns the
gate above. Sunset light casts long dramatic shadows from the pillars.""",

    5: STYLE_PREFIX + """A royal-purple sacred serpent creature with iridescent scales shifting between
violet and indigo. A golden cobra hood fans out behind its head with ornate golden
patterns. Four thin snake-tails extend from below its round body. Emerald-green
slit-pupil eyes with jewel-facet-shaped highlights.
It is coiled protectively around a golden pedestal in a half-submerged underground
temple. Each of its four tail-tips holds up a different glowing gemstone — ruby red,
sapphire blue, emerald green, and topaz yellow. Its cobra hood flares wide as it
flicks its forked tongue, giving the viewer a suspicious sideways glare.
The four colored gem-lights reflect off its iridescent scales, creating rainbow
refractions across its body.
Background: a half-flooded underground temple treasure vault. Stone walls carved
with ancient serpent reliefs and glowing script. Green bioluminescent moss casts
a soft eerie glow. Stone pillars rise from the water, topped with golden offerings.
Mystical light particles drift in the air.""",

    6: STYLE_PREFIX + """A crimson-red griffin creature with an eagle head with a small golden curved beak,
lion body with a fluffy mane and tufted tail, and spread wings with brown-tipped
feathers. A small golden crown atop its head. Amber-gold eyes with sharp
diamond-shaped highlights, fierce yet adorable.
It perches proudly on a rocky cliff ledge, one eagle talon pinning down a freshly
caught shimmering silver fish. Its chest feathers puff up with unmistakable pride,
a look what I caught expression. Its lion mane streams dramatically in the sea
breeze. Behind it, a nest made of golden branches holds three gleaming golden eggs.
Background: a dramatic coastal cliff at sunset. Waves crash against rocks far
below, sending up white spray that catches the golden light. A distant Near Eastern
port city with golden minarets is silhouetted on the horizon. The sky is painted
in deep orange, crimson, and gold sunset gradients.""",

    7: STYLE_PREFIX + """A rose-pink dancer creature with an elegant glossy round body, long delicate
eyelashes, and a serene graceful presence. Tiny golden bangles on both small arms,
a small golden tiara with a ruby on its head. Deep rose-pink eyes with lotus-petal-
shaped highlights, half-closed in blissful ecstasy.
It dances atop a giant floating lotus flower on a temple pool. One tiny arm is
raised elegantly, holding a golden oil lamp (diya) with a flickering flame. The
other arm trails a long salmon-pink silk scarf that spirals outward in snake-like
curves. Rose petals flutter and fall gently all around. Its expression is one of
serene bliss with a peaceful half-smile.
Background: a nighttime temple pool. Hundreds of floating oil lamps (diyas) cover
the water surface, their orange glow reflecting and shimmering. A crescent moon
reflects in the pool. Stone railings draped with jasmine garlands line the edges.
Warm golden candlelight creates an intimate dreamlike atmosphere.""",

    8: STYLE_PREFIX + """A deep indigo-purple jackal creature with tall pointed triangular ears standing
straight up and a small black nose. The body is dark indigo with slightly lighter
purple on the ear edges and belly. Golden-amber eyes with crescent moon-shaped
highlights, mystical and solemn. EXACTLY 4 LEGS visible (standard canine anatomy:
2 front paws + 2 back paws, NOT 6, NOT 8).
It sits upright on the lid of a weathered sandstone sarcophagus. One tiny front
paw rests on a golden ankh staff (cross with a loop on top) planted beside it.
Its head tilts upward, mouth slightly open in a small adorable howl. Six or seven
pale blue-white wisps (spirit flames) float around it like ethereal fireflies.
Background: the entrance to an ancient tomb at night. A massive full moon hangs
low on the horizon directly behind the creature, creating a dramatic silhouette
halo effect. Two weathered obelisks with faded hieroglyphs stand on either side.
Desert sand drifts gently. Starry sky with the Milky Way visible. Faint blue-
violet magical mist creeps along the ground.""",

    9: STYLE_PREFIX + """A magnificent yet cute round dragon creature with brilliant golden glossy body
covered in shimmering scales that reflect warm amber and bronze light. Two
majestically curved large horns on its head. Impressive spread wings with golden
membrane unfurled wide. A thick dragon tail curls behind. Blazing deep crimson
eyes with eight-pointed starburst highlights radiating overwhelming power, yet its
perfectly round chibi body and rosy cheeks create an endearing contrast.
It rises from a throne of gold and jewels, wings fully spread. It breathes a
spectacular spiraling torrent of golden flame from its mouth, the fire twisting
upward. A floating crown of molten fire hovers above its horns. Ancient dragon-rune
symbols glow golden and orbit slowly around its body. Its expression commands
absolute authority. Golden sparks and embers fill the air.
Background: a golden palace at the summit of a volcano. Rivers of molten lava flow
through obsidian channels on either side. A massive golden throne carved with dragon
reliefs stands behind. The sky blazes in deep crimson and gold. Countless embers and
golden light particles rise through the superheated air."""
}

FRAME_MAP = {
    0: 'cards/frame_common.png',
    1: 'cards/frame_common.png',
    2: 'cards/frame_common.png',
    3: 'cards/frame_common.png',
    4: 'cards/frame_uncommon.png',   # mid-boss silver
    5: 'cards/frame_common.png',
    6: 'cards/frame_common.png',
    7: 'cards/frame_common.png',
    8: 'cards/frame_common.png',
    9: 'cards/frame_rare.png',       # boss gold
}

def generate_image(prompt, output_path):
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:predict?key={API_KEY}'
    payload = {
        "instances": [{"prompt": prompt}],
        "parameters": {
            "sampleCount": 1,
            "aspectRatio": "3:4",
            "personGeneration": "dont_allow"
        }
    }
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    resp = urllib.request.urlopen(req, context=CTX, timeout=180)
    result = json.loads(resp.read())
    predictions = result.get('predictions', [])
    if predictions and predictions[0].get('bytesBase64Encoded'):
        img_data = base64.b64decode(predictions[0]['bytesBase64Encoded'])
        with open(output_path, 'wb') as f:
            f.write(img_data)
        print(f'  Generated: {output_path} ({len(img_data)//1024}KB)')
        return True
    else:
        print(f'  FAILED: {output_path} - no image data')
        if predictions:
            print(f'  Reason: {json.dumps(predictions[0], indent=2)[:300]}')
        return False

def compose_card(art_path, frame_path, output_path):
    frame = Image.open(frame_path).convert('RGBA')
    art = Image.open(art_path).convert('RGBA')
    tw, th = frame.size
    frame = frame.resize((tw, th), Image.LANCZOS)
    pixels = frame.load()
    for y in range(th):
        for x in range(tw):
            r, g, b, a = pixels[x, y]
            if r > 230 and g > 230 and b > 230:
                pixels[x, y] = (r, g, b, 0)
    art_resized = art.resize((tw, th), Image.LANCZOS)
    card = Image.new('RGBA', (tw, th), (255, 255, 255, 255))
    card.paste(art_resized, (0, 0), art_resized)
    card.paste(frame, (0, 0), frame)
    card.convert('RGB').save(output_path, quality=95)
    print(f'  Composed: {output_path} ({os.path.getsize(output_path)//1024}KB)')

def main():
    # Which cards to generate (skip 0, already done)
    targets = list(range(1, 10)) if '--all' not in sys.argv else list(range(0, 10))
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        targets = [int(sys.argv[1])]

    for idx in targets:
        prompt = PROMPTS.get(idx)
        if not prompt:
            print(f'[{idx}] No prompt, skipping')
            continue

        raw_path = f'cards/raw_extreme_{idx}.png'
        final_path = f'cards/extreme_{idx}.png'
        frame_path = FRAME_MAP[idx]

        print(f'[{idx}] Generating raw image...')
        ok = generate_image(prompt, raw_path)
        if not ok:
            print(f'[{idx}] Retrying in 5s...')
            time.sleep(5)
            ok = generate_image(prompt, raw_path)

        if ok:
            print(f'[{idx}] Composing with frame ({os.path.basename(frame_path)})...')
            compose_card(raw_path, frame_path, final_path)

        # Rate limit: wait between API calls
        if idx < targets[-1]:
            time.sleep(2)

    print('\nDone!')

if __name__ == '__main__':
    main()
