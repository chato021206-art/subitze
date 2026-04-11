#!/usr/bin/env python3
"""Regenerate ALL EASY/NORMAL/HARD cards (30 total) with EXTREME-quality prompts."""
import urllib.request, json, os, ssl, base64, time, sys
from PIL import Image
from collections import deque

API_KEY = os.environ.get('GOOGLE_API_KEY', '')
MODEL = 'imagen-4.0-generate-001'
CTX = ssl.create_default_context()

S = """Super deformed cute chibi blob creature, anime mobile game card illustration,
extremely round soft body with tiny stubby limbs, large sparkling anime eyes,
rosy cheeks, glossy skin with specular highlights,
digital painting, vibrant saturated colors, rich detailed background that fills
the ENTIRE image edge to edge with NO white borders or margins anywhere,
creature fills about 55-60% of the frame vertically and is centered with clear
margins from all edges so it does not touch or overlap the borders,
portrait orientation 7:10 aspect ratio, no text, no frame, no border, no UI elements.

"""

CARDS = {
  # ══════════════ EASY（港・海辺 ラノシア風）══════════════
  'easy_0': { 'frame': 'common', 'prompt': S + """A cute round slime jelly creature — NOT a dog, NOT an animal — a simple featureless
pink blob of translucent glossy bubblegum-pink gelatin. No ears, no nose, no fur.
Smooth glistening surface with white bubble-like highlight spots. Large sparkling
deep blue anime eyes with HEART-SHAPED highlights (not stars). Tiny stubby pseudopod
limbs made of the same pink goo. It sits on sun-warmed wooden dock planks, a small
puddle of pink goo beneath it. A tiny pink heart bubble floats above its head.
Background: peaceful seaside wooden dock at golden hour. Calm turquoise ocean.
Fluffy clouds. Wooden barrels and coiled ropes. Lighthouse in the distance.""" },

  'easy_1': { 'frame': 'common', 'prompt': S + """A cute round snail creature with a large golden spiral shell on its back gleaming
with warm amber highlights. Soft cream-yellow glossy body. Large sparkling warm
brown eyes with TEARDROP-SHAPED highlights (like dewdrops). Tiny stubby arms — one
holds a small seashell, the other carries a tiny woven basket overflowing with shells.
Running happily along a sandy beach, leaving a faint trail. Determined smile.
Background: warm sandy beach at midday. Crystal water laps at shore. Scattered
seashells and starfish. Beach grass sways. Distant cliffs. Bright blue sky.""" },

  'easy_2': { 'frame': 'common', 'prompt': S + """A cute round pufferfish creature with glossy chartreuse/lime-green body slightly
inflated with tiny soft rounded spines. Lighter yellow-green belly. Small round
pectoral fins. A surprised flustered expression with puffed cheeks. Large sparkling
bright green eyes with CIRCULAR RING-SHAPED highlights (like ripples in water).
Tiny "o" mouth. Floats near harbor water surface, puffed up in surprise at a small
fish. Tiny bubbles rise from its mouth.
Background: calm harbor with crystal turquoise water. Wooden dock with barnacles
underwater. Colorful tropical fish. Sunlight sparkles on water. Half underwater.""" },

  'easy_3': { 'frame': 'common', 'prompt': S + """A cute round starfish creature with glossy warm coral-orange body shaped like a
chubby five-pointed starfish blob. Each arm tip has a lighter orange spot. Lighter
peach-colored belly. Large sparkling warm orange eyes with STAR-SHAPED highlights
(matching its starfish body). Big happy cheerful smile. It sits on a sun-warmed
wooden dock post, tiny arms waving cheerfully. Seashells and a hermit crab nearby.
Background: warm sunset harbor with wooden docks and colorful fishing boats on
calm golden water. Lobster traps and ropes. Seagulls. Orange-pink sunset sky.""" },

  'easy_4': { 'frame': 'uncommon', 'prompt': S + """A cute but imposing round fish-warrior creature with bright royal blue glossy body.
Small golden crown with teal jewel. Tiny golden trident in one stubby fin. Blue-green
fin ears. Large sparkling bright cyan eyes with SHARP DIAMOND-SHAPED highlights
(like cut aquamarine gems). Determined furrowed brows. White belly. It stands on a
rocky outcrop by the crashing sea, one fin raised holding the trident proudly.
Background: dramatic rocky coastline with crashing waves and white spray. Lighthouse
on distant cliff. Storm clouds with sunlight breaking through.""" },

  'easy_5': { 'frame': 'common', 'prompt': S + """A cute round ladybug creature with glossy dark navy-black body and bright red shell
with black polka dots. Small black antennae with tiny balls. Large sparkling warm
golden-amber eyes with HONEYCOMB-PATTERN hexagonal highlights. Gentle smile. Tiny
black legs. It sits on a large colorful flower, wings slightly spread, basking.
Background: vibrant flower garden overlooking the sea. Colorful flowers in bloom.
Castle tower in misty distance. Butterflies. Bright blue sky. Warm sunlight.""" },

  'easy_6': { 'frame': 'common', 'prompt': S + """A cute round anglerfish creature with glossy deep teal-green body. A bioluminescent
lure dangles from a forehead stalk, glowing warm golden-yellow. Large sparkling dark
eyes with GLOWING ROUND SPOTLIGHT highlights (like its own lure reflected). Wide
friendly grin showing tiny rounded teeth. Small fins. It floats in deep water, its
lure illuminating the area with warm light.
Background: deep ocean with dark navy water. The lure creates warm golden light circle.
Coral formations glow faintly. Small glowing jellyfish drift. Deep-sea atmosphere.""" },

  'easy_7': { 'frame': 'common', 'prompt': S + """A cute round jellyfish creature with translucent lavender-purple glossy dome cap.
Iridescent rainbow sheen. Delicate trailing tentacles. Large sparkling purple anime
eyes with CRESCENT MOON-SHAPED highlights (ethereal and dreamy). Gentle smile.
The creature is SMALL — only 50% of frame height, plenty of space around it.
Background: deep ocean blue gradient. Bioluminescent particles glow like underwater
stars. Coral reef hints at bottom. Sunlight shafts from above. Serene.""" },

  'easy_8': { 'frame': 'common', 'prompt': S + """A cute round crab creature with glossy warm chocolate-brown body and lighter tan
belly. Two small pincers held up cheerfully. Large sparkling warm honey-brown eyes
with WARM OVAL highlights (like polished pebbles). Proud grin. Tiny legs. It stands
on a wooden dock at sunset, striking a confident pose with both pincers raised
like a bodybuilder showing off its strength.
Background: warm harbor at sunset. Fishing boats at wooden docks. Golden sunset
light on calm water. Crates and fishing nets. Orange-pink sky. Seagulls.""" },

  'easy_9': { 'frame': 'rare', 'prompt': S + """A majestic yet adorable round sea dragon creature with deep purple-blue glossy body.
Golden crown with teal jewel. Small bat-like wings. Curling dragon tail. Blazing
orange-amber eyes with FLAME-SHAPED highlights (burning with inner fire, radiating
boss power). Small white claws. Satisfied regal smile. Boss-level authority despite
being round and cute. Ocean waves churn dramatically.
Background: dramatic stormy sea filling entire image. Dark thunderclouds with
lightning bolts. Massive crashing waves. Lighthouse on cliffs. Dark moody atmosphere.""" },

  # ══════════════ NORMAL（森・黒衣森風）══════════════
  'normal_0': { 'frame': 'common', 'prompt': S + """A cute round mushroom creature with large glossy red-and-white spotted toadstool
cap on its head. Cream/beige soft body. Large sparkling warm brown eyes with
SOFT ROUND DEW-DROP highlights (like morning dew on a mushroom). Shy gentle smile.
Tiny roots for feet. It stands in a mossy clearing, tiny spore particles floating up.
Background: lush enchanted forest with towering ancient trees. Dappled golden
sunlight through dense canopy. Moss-covered logs. Wildflowers. Fireflies. Peaceful.""" },

  'normal_1': { 'frame': 'common', 'prompt': S + """A cute round mandragora/root vegetable creature with glossy warm orange body like a
chubby carrot. Fresh green leaves sprout from its head. Small root feet. Large
sparkling dark brown eyes with WIDE SHOCKED SPARKLE highlights — pupils dilated
in surprise, multiple small light dots. Tiny "o" mouth. Just pulled from ground,
startled. Dirt particles cling to body.
Background: rich dark forest floor with upturned soil. Roots and fallen leaves.
Mushrooms on logs. Soft diffused forest light. Freshly dug hole. Earth tones.""" },

  'normal_2': { 'frame': 'common', 'prompt': S + """A cute round firefly creature with glowing lime-yellow translucent body. Bottom
glows with yellow-green bioluminescent light like a lantern. Small translucent wings.
Two tiny antennae with glowing tips. Large sparkling yellow-green eyes with
GLOWING RING-SHAPED highlights (like halos of light). Cheerful expression.
Flying through dark nighttime forest, trail of glowing particles behind.
Background: dark enchanted forest at night. Dozens of tiny firefly lights like
floating stars. Moss glows on tree trunks. Crescent moon. Magical atmosphere.""" },

  'normal_3': { 'frame': 'common', 'prompt': S + """A cute round morbol/plant-beast creature with glossy dark olive-green body. Small
red flower buds on its head like a crown. Slightly grumpy but cute — furrowed brows,
small pout showing one fang. Large sparkling dark red-brown eyes with CROSS-SHAPED
highlights (like thorns). Stubby vine arms. Sits on a mossy log in a dense swamp.
Background: deep dark mossy forest with thick undergrowth. Gnarled trees with
hanging moss. Blue-green fog. Ferns and bracket fungi. Dim mysterious light.""" },

  'normal_4': { 'frame': 'uncommon', 'prompt': S + """A cute but fierce round wolf creature with glossy steel-gray fur and thick fluffy
white mane. Pointed wolf ears. Bushy gray tail. Large sparkling fierce amber-golden
eyes with SHARP VERTICAL SLIT highlights (like a wolf's predatory gaze combined
with cute anime style). Furrowed eyebrows. Small scar on cheek. Tiny fangs in
confident smirk. One paw raised. Round chibi body is adorable despite fierceness.
Background: mystical misty forest clearing with towering ancient oaks. Morning fog.
Golden sunlight through canopy. Ancient standing stones with moss and runes.""" },

  'normal_5': { 'frame': 'common', 'prompt': S + """A cute round frog creature with glossy sky-blue body and white belly. Smooth slightly
transparent blue-glass skin. Large sparkling aqua-blue eyes with HORIZONTAL OVAL
highlights (like a real frog's wide pupils but sparkly and cute). Small golden crown
tilted on head. Sits on a lily pad, puffing white throat pouch while singing.
Musical notes float upward.
Background: sunlit forest pond with lush vegetation. Lily pads with pink lotus
flowers. Trees with golden sunlight. Dragonflies. Clear water. Bright peaceful.""" },

  'normal_6': { 'frame': 'common', 'prompt': S + """A cute round baby chocobo/chick with fluffy bright golden-yellow feathers. Small
orange beak. Tiny wings flapping excitedly. Large sparkling dark brown-black eyes
with LARGE INNOCENT ROUND highlights (the biggest, most innocent-looking highlights
of all — pure childlike wonder). Wide happy open-mouth smile. Single head tuft.
Tiny orange feet in mid-run. Dashing across a farm field with pure joy.
Background: peaceful pastoral ranch with green rolling hills and wooden fence.
Red barn in distance. Fluffy sheep. Blue sky with cotton-candy clouds.""" },

  'normal_7': { 'frame': 'common', 'prompt': S + """A cute round tree spirit/dryad with glossy mossy-green body covered in tiny leaves
and branches. An acorn dangles from one branch. Vine arms. Large sparkling warm
amber-orange eyes with LEAF-SHAPED highlights (organic and natural, like tiny
golden leaves reflected in the iris). Peaceful sleepy smile. Sits on a thick tree
branch high in canopy, legs dangling. Dappled sunlight warms its mossy body.
Background: high canopy of ancient forest. Massive branches as platforms. Hanging
vines and moss. Golden sunbeams. Bird's nest nearby. Forest floor far below.""" },

  'normal_8': { 'frame': 'common', 'prompt': S + """A cute round fox spirit creature with glossy warm amber-orange fur and fluffy white
chest. Bushy fox tail with blue-white spirit flames at the tip. Pointed ears with
dark tips. Large sparkling golden-amber eyes with VERTICAL FLAME-SHAPED highlights
(like dancing foxfire reflected in the iris — mystical and alluring). Mischievous
grin with one tiny fang. One paw raised casting a spell. Three foxfire flames around.
Background: autumn forest at dusk with brilliant red, orange, gold foliage.
Red torii gate silhouette in misty background. Fallen maple leaves. Purple twilight.""" },

  'normal_9': { 'frame': 'rare', 'prompt': S + """A majestic yet adorable round moogle king creature with fluffy pure white body.
Red pompom on stalk above head. Golden crown with red gem between tiny purple wings.
Large sparkling deep red-pink eyes with CROSS-STAR/ROYAL highlights (like a
royal four-pointed cross, radiating regal authority). Regal but sweet expression.
Sits on ancient tree stump in a magical fairy ring.
Background: enchanted forest clearing at twilight. Glowing mushroom fairy ring.
Magical sparkles and fireflies. Ancient trees with moss. Golden-green magical light.""" },

  # ══════════════ HARD（砂漠・ザナラーン風）══════════════
  'hard_0': { 'frame': 'common', 'prompt': S + """A cute round rock golem creature with glossy blue-gray stone body with natural cracks
and weathered texture. Small teal-blue crystal gems embedded, glowing faintly. Thick
stone eyebrow ridges. Large sparkling ice-blue eyes with CROSS/PLUS-SHAPED highlights
(like fractured crystal refractions). Small forehead crack reveals teal light inside.
Tiny stone fists. Sturdy and ancient but adorable.
Background: dramatic desert ruins at golden sunset. Crumbling sandstone pillars.
Setting sun creates orange-gold sky behind mesa formations. Sand drifts. Dig site.""" },

  'hard_1': { 'frame': 'common', 'prompt': S + """A cute round scorpion creature with glossy sandy-beige/tan body like desert sand.
Segmented tail curled high with faintly orange glowing stinger. Two small pincers
in threatening but adorable pose. Dark brown camouflage markings. Large sparkling
amber-brown eyes with SHARP ANGULAR/TRIANGULAR highlights (like desert crystals).
Emerging halfway from sand, tail raised in warning.
Background: vast desert at golden sunset. Towering sand dunes under orange-pink sky.
Heat shimmer. Desert rocks and lone dead tree. Warm golden light.""" },

  'hard_2': { 'frame': 'common', 'prompt': S + """A cute round falcon/hawk creature with brilliant golden-brown glossy plumage.
White chest with golden-brown speckles. Small fierce spread wings with darker tips.
Curved golden beak. Large sparkling golden eyes with SHARP DIAMOND/RAPTOR-SHAPED
highlights (like a hawk's piercing focused gaze). Golden anklet. Perches on desert
rock, puffed up proudly, wings slightly spread, scanning horizon.
Background: dramatic desert canyon at sunrise. Towering sandstone cliffs. Distant
pyramids. Rising sun creates golden rays through morning haze.""" },

  'hard_3': { 'frame': 'common', 'prompt': S + """A cute round cactus creature with glossy bright green body with small golden spines.
Beautiful pink flower blooming on its head. Small cactus arm-branches waving. Large
sparkling dark green eyes with SPARKLE-BURST highlights (like tiny fireworks, joyful
and energetic). Wide happy smile. Dancing in a cactus field, one foot raised,
flower petals falling from its bloom.
Background: beautiful desert cactus field at golden sunset. Saguaro cacti and prickly
pear. Mountains in purple-orange distance. Sunset sky. Desert wildflowers.""" },

  'hard_4': { 'frame': 'uncommon', 'prompt': S + """A cute but imposing round desert sphinx creature with glossy warm golden-amber body.
Pharaoh-style striped headdress (nemes) in blue and gold on its round head. Small
lion paws. Mysterious knowing smile. Large sparkling deep amber eyes with
HIEROGLYPH-SHAPED highlights (like ancient Egyptian eye-of-Horus symbols reflected
in the iris — ancient wisdom in cute form). Golden wings at sides. Ankh pendant on
golden chain. Sits regally on stone pedestal before a massive pyramid.
Background: Egyptian-inspired desert at golden hour. Massive golden pyramid behind.
Shadow stretches across sand. Obelisks with hieroglyphs. Amber light. Crescent moon.""" },

  'hard_5': { 'frame': 'common', 'prompt': S + """A cute round crystal-scorpion creature with glossy teal/cyan body shimmering with
inner crystalline glow. Crystalline segments refract rainbow sparkles. Curled tail
with teal crystal tip. Small translucent pincers. Large sparkling emerald-teal eyes
with GEM-FACET highlights (like cut emerald reflections, multifaceted). Happily
munching a teal crystal, mouth sparkling. Crystal shards float around head.
Background: spectacular crystal cavern with massive teal crystal formations.
Glowing mineral veins. Underground pool reflecting crystal light. Blue-green glow.""" },

  'hard_6': { 'frame': 'common', 'prompt': S + """A cute round bomb creature with glossy dark navy-blue body (NOT red). Metal cap on
top with blue-tipped fuse shooting blue-white sparks. Midnight blue body with tiny
star-like sparkle patterns. Large panicked eyes with SPIRAL/SWIRL highlights
(dizzied panic spirals in pale blue — classic cartoon bomb panic). Mouth open in
worry, single blue sweat drop.
Background: desert at night under spectacular starry Milky Way sky. Sand dunes in
blue-gray moonlight. Blue fuse sparks illuminate nearby sand. Shooting stars.""" },

  'hard_7': { 'frame': 'common', 'prompt': S + """A cute round cobra creature with glossy jade-green/emerald body (NOT red). Beautiful
darker green scale pattern. Lighter green belly. Small jade-green cobra hood with
golden ornamental markings. Large sparkling yellow-green eyes with VERTICAL SLIT-PUPIL
highlights (reptilian serpent pupils with golden light — wise and hypnotic). Forked
tongue flicks playfully. Regal mysterious expression. Coiled before golden ruins.
Background: ancient golden desert ruins with hieroglyph sandstone walls. Sunlight
through crumbled doorway. Green vines on ruins. Golden afternoon light.""" },

  'hard_8': { 'frame': 'common', 'prompt': S + """A cute round mineral/crystal creature with glossy ice-blue/frost-blue body (NOT brown).
Sparkling ice-blue and white crystal clusters growing from surface like frozen
flowers. Translucent frosted glass quality. Large sparkling diamond-blue eyes with
SAPPHIRE-FACET highlights (like looking into a cut sapphire — deep multifaceted
blue reflections). Gentle peaceful smile. Tiny ice crystal feet. Inner blue glow.
Background: mine tunnel with wooden beams and rails. Cool blue-white light from
ice crystal formations. Mining lantern casting warm contrast. Mine cart in distance.""" },

  'hard_9': { 'frame': 'rare', 'prompt': S + """A majestic cute round fire demon creature with deep dark crimson body. Aura of
blue-purple flames mixed with orange fire. Large eyes with BLUE-FIRE-CENTER highlights
(inner iris burns with blue-white fire, outer ring of orange flame — dual-tone fire
eyes radiating overwhelming boss power). Two small dark horns. Sharp tiny fangs in
fierce grin. Rosy cheeks for cute contrast. Boss energy despite adorable round body.
Background: volcanic arena with dark basalt pillars. Rivers of bright orange lava.
Dramatic tall pillars of BLUE fire on both sides. Volcanic ash clouds. Dual-tone
blue and orange fire lighting. Epic boss arena.""" },
}

FRAME_MAP = {
    'common': 'cards/frame_common.png',
    'uncommon': 'cards/frame_uncommon.png',
    'rare': 'cards/frame_rare.png',
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
        print(f'  OK: {output_path} ({len(img_data)//1024}KB)')
        return True
    print(f'  FAILED: {output_path}')
    return False

def compose_card(art_path, frame_path, output_path):
    frame = Image.open(frame_path).convert('RGBA')
    art = Image.open(art_path).convert('RGBA')
    tw, th = frame.size
    pixels = frame.load()
    mask = Image.new('L', (tw, th), 0)
    mask_px = mask.load()
    visited = set()
    queue = deque()
    cx, cy = tw // 2, th // 2
    queue.append((cx, cy)); visited.add((cx, cy))
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

    # Allow filtering: python3 gen_all_cards.py easy / normal / hard / easy_3
    if len(sys.argv) > 1:
        filt = sys.argv[1]
        targets = [k for k in targets if filt in k]

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
            print(f'  Retrying in 5s...')
            time.sleep(5)
            ok = generate_image(info['prompt'], raw_path)

        if ok:
            compose_card(raw_path, frame_path, final_path)
            img = Image.open(final_path).convert('RGB').resize((120, 168), Image.LANCZOS)
            img.save(thumb_path, 'JPEG', quality=80)
            print(f'  Thumb: {thumb_path}')

        if i < len(targets) - 1:
            time.sleep(2)

    print(f'\nAll done! Generated {len(targets)} cards.')

if __name__ == '__main__':
    main()
