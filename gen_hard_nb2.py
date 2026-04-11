#!/usr/bin/env python3
"""Regenerate HARD cards + generate HARD+/EXTREME+ using Nano Banana 2."""
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

SP = S + "IMPORTANT: This is a '+' variant — alternate color with a completely different scene.\n\n"

CARDS = {
  # ══════ HARD base (story prompts) ══════
  'hard_0': { 'frame': 'common', 'prompt': S + """Scene: A round sandy-beige camel creature with a small hump loaded with colorful
merchant goods — tiny carpets, brass lamps, spice bags. Tattered red scarf on neck.
Warm brown eyes with GENTLE OVAL highlights, half-closed with contentment. A tiny
gecko rides on the cargo. Trudging cheerfully through desert leaving hoofprints.
Background: vast golden desert, caravan trail behind, oasis with palms in distance.""" },

  'hard_1': { 'frame': 'common', 'prompt': S + """Scene: A sandy-beige scorpion waited 3 days in sand. Now bursting out in sand spray,
tail raised with orange-glowing stinger. But the lizard just escaped — expression
shifts to deflated "...three more days." Amber eyes with SHARP TRIANGULAR highlights.
Background: vast desert at golden sunset, sand exploding, tiny lizard fleeing.""" },

  'hard_2': { 'frame': 'common', 'prompt': S + """Scene: Young golden-brown falcon on cliff edge, fledging day. Wings spread wide for
first time, trembling. Below: vast desert and pyramids. Parent hawk silhouette watches
behind. "I can do this!" Golden eyes with SHARP DIAMOND highlights.
Background: desert canyon at sunrise, nest visible, pyramids, golden rays.""" },

  'hard_3': { 'frame': 'common', 'prompt': S + """Scene: Green cactus creature's head-flower blooms once per 100 years. This is THAT
moment! Dancing uncontrollably, petals scatter. Surrounding cacti bloom in solidarity.
Dark green eyes with SPARKLE-BURST highlights. Joyful beyond measure.
Background: desert cactus field at sunset, all cacti blooming, wildflowers.""" },

  'hard_4': { 'frame': 'uncommon', 'prompt': S + """Scene: Golden-amber sphinx on stone pedestal before pyramid. Pharaoh headdress in
blue and gold. "Answer: what walks on four legs at dawn, two at noon, three at dusk?"
Mysterious smile unchanged for 3000 years. Deep amber eyes with HIEROGLYPH highlights.
Ankh pendant glows. Background: pyramid at golden hour, obelisks, crescent moon.""" },

  'hard_5': { 'frame': 'common', 'prompt': S + """Scene: Teal crystal-scorpion born from cave crystal, talking to crystal siblings
by nibbling a glowing teal gem. Sparkles at mouth are crystal "words." Still half-
embedded in birth-crystal. Emerald-teal eyes with GEM-FACET highlights.
Background: spectacular crystal cavern, massive teal formations, glowing veins.""" },

  'hard_6': { 'frame': 'common', 'prompt': S + """Scene: Wine-red/maroon desert jackal on sand dune at night, head tilted up in
adorable howl at full moon. Golden-amber eyes with SHARP CANINE highlights catch
moonlight. Tiny scar across nose. Moonlight paints fur with silver edges.
Background: desert under massive full moon, silver-blue dunes, stars, solitary.""" },

  'hard_7': { 'frame': 'common', 'prompt': S + """Scene: Jade-green cobra spent 1000 years reading hieroglyphs. Just finished the
last character — walls glow gold. The ancient text says "Congratulations, you read
all this!" An ancient joke. Cobra's expression: disbelief then reluctant amusement.
Yellow-green eyes with VERTICAL SLIT highlights. Background: golden glowing ruins.""" },

  'hard_8': { 'frame': 'common', 'prompt': S + """Scene: Cream/ivory desert hedgehog pops out of sand burrow holding up a tiny ruby
triumphantly. Its treasure-hunting hobby. A collection of colorful gems (emerald,
sapphire, amber) piled by the burrow entrance. Warm brown eyes with SPARKLE highlights.
Background: warm desert at golden hour, burrow visible, scattered gems.""" },

  'hard_9': { 'frame': 'rare', 'prompt': S + """Scene: Dark crimson fire demon rises from lava throne. For the first time in centuries,
its forbidden "blue flame" awakens for a worthy challenger. Blue-purple fire erupts
alongside orange. "Come, show me everything." Eyes: BLUE-CENTER ORANGE-RING dual fire.
Dark horns, tiny fangs, fierce respectful grin. Background: volcanic arena, blue and
orange fire pillars, lava rivers, dark basalt, epic dual-tone lighting.""" },

  # ══════ HARD+ (alternate stories) ══════
  'hard+_0': { 'frame': 'common', 'prompt': SP + """Character: A silver-white (NOT beige) camel variant with frost patterns on fur.
Story: This arctic camel delivers gifts through a snowy desert oasis town at night.
Tiny wrapped presents in its saddlebags, a small bell around its neck jingling.
Silver-blue eyes with SNOWFLAKE highlights. Background: snowy oasis town, lanterns.""" },

  'hard+_1': { 'frame': 'common', 'prompt': SP + """Character: A deep purple (NOT tan) scorpion variant with bioluminescent markings.
Story: This nocturnal variant hunts by starlight. Its body glows with purple patterns
in the dark. It dances under the aurora borealis that mysteriously appeared over the
desert. Violet eyes with CONSTELLATION highlights. Background: desert aurora night.""" },

  'hard+_2': { 'frame': 'common', 'prompt': SP + """Character: A snow-white (NOT golden) falcon variant with ice-blue wing tips.
Story: This arctic falcon delivers mail across the frozen tundra. A tiny leather
mailbag on its back. It soars through falling snow with a letter in its beak.
Ice-blue eyes with WIND-STREAK highlights. Background: snowy mountain pass.""" },

  'hard+_3': { 'frame': 'common', 'prompt': SP + """Character: A cherry-blossom pink (NOT green) cactus variant with sakura flowers.
Story: In an impossible desert miracle, this pink cactus blooms sakura. Cherry
blossom petals swirl around it as it dances. Other desert plants watch in awe.
Pink eyes with PETAL-SHAPED highlights. Background: desert with sakura petals.""" },

  'hard+_4': { 'frame': 'uncommon', 'prompt': SP + """Character: A midnight-blue (NOT golden) sphinx variant with silver star markings.
Story: The night sphinx guards the dream realm. Instead of riddles, it tells
bedtime stories. Tiny sleeping desert animals curled around its pedestal. A book
of fairy tales open before it. Starry silver eyes with MOON highlights.
Background: starlit desert, sleeping animals, open storybook, peaceful night.""" },

  'hard+_5': { 'frame': 'common', 'prompt': SP + """Character: An amber/golden (NOT teal) crystal-scorpion variant made of warm topaz.
Story: This golden variant is a desert jeweler, carefully polishing gems with its
pincers. Tiny spectacles on its face. A display case of finished jewelry beside it.
Warm amber eyes with JEWEL-CUT highlights. Background: desert gem workshop, sunset.""" },

  'hard+_6': { 'frame': 'common', 'prompt': SP + """Character: A frost-blue (NOT wine-red) jackal variant with white fur accents.
Story: This ice jackal plays in the first snowfall the desert has seen in 1000
years. It catches snowflakes on its tongue, tail wagging, pure childlike joy.
Ice-blue eyes with SNOWFLAKE highlights. Background: desert with miraculous snow.""" },

  'hard+_7': { 'frame': 'common', 'prompt': SP + """Character: A royal purple (NOT jade-green) cobra variant with golden crown markings.
Story: This purple cobra is a teacher. It uses its tail to draw math equations in
the sand for tiny desert lizard students sitting in rows. A tiny chalkboard nearby.
Wise purple eyes with BOOK-PAGE highlights. Background: desert schoolhouse scene.""" },

  'hard+_8': { 'frame': 'common', 'prompt': SP + """Character: A warm rose-pink (NOT cream) hedgehog variant with flower-petal quills.
Story: This pink hedgehog is a florist! Its quills bloom with tiny flowers. It
arranges a bouquet of desert wildflowers in a tiny vase, tongue out in concentration.
Soft pink eyes with FLOWER-PETAL highlights. Background: desert flower stall.""" },

  'hard+_9': { 'frame': 'uncommon', 'prompt': SP + """Character: An ice-blue (NOT crimson) fire demon variant — an ice demon instead.
Story: The volcanic arena has frozen over. This ice demon creates beautiful ice
sculptures instead of destroying. Crystalline frost breath creates an ice palace.
Serene and artistic, the opposite of its fire twin. Deep ice-blue eyes with
CRYSTAL-FROST highlights. Background: frozen volcanic arena, ice sculptures, aurora.""" },

  # ══════ EXTREME+ (alternate stories) ══════
  'extreme+_0': { 'frame': 'common', 'prompt': SP + """Character: A bronze/copper (NOT steel-gray) armadillo-dragon variant.
Story: This bronze variant is a master chef! It rolls into a ball to knead dough,
then unrolls to check the flatbread baking in a clay oven. Flour on its face.
A bazaar food stall with "Best Naan" sign. Warm copper eyes with BREAD-ROUND highlights.
Background: bustling Near Eastern food bazaar, clay oven, steam, spice jars.""" },

  'extreme+_1': { 'frame': 'common', 'prompt': SP + """Character: A coral-pink (NOT cerulean) sea-dragon variant with rose-gold horn.
Story: This pink variant runs a bath house. It swims in a ornate temple pool
giving rides to tiny fish children on its back. Warm and nurturing.
Rose-pink eyes with BUBBLE-ROUND highlights. Background: ornate temple bath.""" },

  'extreme+_2': { 'frame': 'common', 'prompt': SP + """Character: A sunset-orange (NOT emerald-green) divine bird variant.
Story: This orange bird is a postal carrier, delivering scrolls between temple
towers. A tiny mailbag strapped on. Racing through sunset clouds with a scroll
in its beak. Orange eyes with WING-SHAPED highlights. Background: temple towers.""" },

  'extreme+_3': { 'frame': 'common', 'prompt': SP + """Character: A silver-white (NOT golden) sacred monkey variant with ice-blue accents.
Story: This white monkey is a librarian in the grand temple library. Sitting atop
a towering stack of ancient scrolls, reading with tiny spectacles. Books everywhere.
Silver eyes with SCROLL-SHAPED highlights. Background: grand temple library.""" },

  'extreme+_4': { 'frame': 'uncommon', 'prompt': SP + """Character: A jade-green (NOT brown) elephant variant with emerald jewelry.
Story: This green elephant is a garden keeper of a magnificent temple garden.
Using its trunk to water exotic flowers. Butterflies land on its ears.
Emerald eyes with LEAF-SHAPED highlights. Background: lush temple garden.""" },

  'extreme+_5': { 'frame': 'common', 'prompt': SP + """Character: A golden-yellow (NOT purple) serpent variant with sun markings.
Story: This golden naga is a treasure GIVER, not guardian. It distributes coins
to grateful tiny creatures from an overflowing treasure pot. Generous and kind.
Golden eyes with COIN-ROUND highlights. Background: temple treasury, gold coins.""" },

  'extreme+_6': { 'frame': 'common', 'prompt': SP + """Character: A midnight-blue (NOT crimson) griffin variant with silver wings.
Story: This blue griffin is a stargazer, lying on its back on a cliff at night,
using a tiny telescope. Maps of constellations spread around it.
Deep blue eyes with STAR-MAP highlights. Background: cliff at night, telescope.""" },

  'extreme+_7': { 'frame': 'common', 'prompt': SP + """Character: A mint-green (NOT rose-pink) dancer variant with silver accessories.
Story: This green variant teaches dance to tiny temple creatures. Leading a class
of baby animals in a dance pose. Patient and encouraging expression.
Mint-green eyes with MUSICAL-NOTE highlights. Background: temple dance studio.""" },

  'extreme+_8': { 'frame': 'common', 'prompt': SP + """Character: A warm amber (NOT indigo) jackal variant with golden ear tips.
Story: This golden jackal is an archaeologist! With a tiny brush and magnifying
glass, it carefully uncovers a buried golden artifact. Explorer hat on head.
Warm amber eyes with MAGNIFYING-GLASS highlights. Background: excavation site.""" },

  'extreme+_9': { 'frame': 'uncommon', 'prompt': SP + """Character: A pearl-white (NOT golden) dragon variant with rainbow scale accents.
Story: The fearsome dragon king's secret: it paints. In a hidden grotto, it holds
a tiny brush in its claw, painting a beautiful landscape on a canvas. Palette of
colors beside it. Art supplies everywhere. Gentle artistic expression.
Rainbow-tinged white eyes with PALETTE-SHAPED highlights. Background: art grotto.""" },
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
    tw, th = frame.size
    pixels = frame.load()
    mask = Image.new('L', (tw, th), 0); mask_px = mask.load()
    visited = set(); queue = deque()
    queue.append((tw//2, th//2)); visited.add((tw//2, th//2))
    while queue:
        x, y = queue.popleft()
        r, g, b, a = pixels[x, y]
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
        safe_id = card_id.replace('+', '_plus')
        raw_path = f'cards/raw_{safe_id}.png'
        final_path = f'cards/{safe_id}.png'
        thumb_path = f'cards/thumb/{safe_id}.jpg'
        frame_path = FRAME_MAP[info['frame']]
        print(f'[{i+1}/{len(targets)}] {card_id}')
        ok = generate_image(info['prompt'], raw_path)
        if not ok:
            time.sleep(3)
            ok = generate_image(info['prompt'], raw_path)
        if ok:
            compose_card(raw_path, frame_path, final_path)
            Image.open(final_path).convert('RGB').resize((120,168),Image.LANCZOS).save(thumb_path,'JPEG',quality=80)
        if i < len(targets) - 1:
            time.sleep(2)
    print(f'\nDone! {len(targets)} cards.')

if __name__ == '__main__':
    main()
