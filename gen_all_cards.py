#!/usr/bin/env python3
"""Regenerate ALL EASY/NORMAL/HARD cards (30 total) with EXTREME-quality prompts."""
import urllib.request, json, os, ssl, base64, time, sys
from PIL import Image
from collections import deque

API_KEY = os.environ.get('GOOGLE_API_KEY', '')
MODEL = 'imagen-4.0-generate-001'
CTX = ssl.create_default_context()

S = """Super deformed cute chibi blob creature, anime mobile game card illustration,
extremely round soft body with tiny stubby limbs, large sparkling anime eyes
with star-shaped highlights, rosy cheeks, glossy skin with specular highlights,
digital painting, vibrant saturated colors, rich detailed background that fills
the ENTIRE image edge to edge with NO white borders or margins anywhere,
creature fills about 55-60% of the frame vertically and is centered with clear
margins from all edges so it does not touch or overlap the borders,
portrait orientation 7:10 aspect ratio, no text, no frame, no border, no UI elements.

"""

CARDS = {
  # ══════════════ EASY（港・海辺 ラノシア風）══════════════
  'easy_0': { 'frame': 'common', 'prompt': S + """A cute round pink slime/jelly creature with translucent glossy bubblegum-pink body.
White highlight spots shimmer on its surface like soap bubbles. Large sparkling
deep blue anime eyes with star highlights. Tiny stubby pseudopod limbs. It sits
contentedly on sun-warmed wooden dock planks, a small puddle of goo beneath it.
A tiny pink heart-shaped bubble floats above its head. Rosy cheeks and a sweet smile.
Background: a peaceful seaside wooden dock at golden hour. Calm turquoise ocean
stretches to the horizon. Fluffy white clouds in a warm blue sky. Wooden barrels
and coiled ropes on the dock. A lighthouse visible in the distance. Seagulls soar.
Warm golden afternoon sunlight makes the ocean glitter.""" },

  'easy_1': { 'frame': 'common', 'prompt': S + """A cute round snail creature with a large golden spiral shell on its back, the shell
gleaming with warm amber highlights and spiral grooves. Its soft body is cream-yellow
with a glossy sheen. Large sparkling warm brown eyes with star highlights. Tiny
stubby arms — one holds a small seashell, the other carries a tiny woven basket
overflowing with collected shells. Running happily along a sandy beach, leaving
a faint trail behind. Rosy cheeks and a determined smile.
Background: a warm sandy beach at midday. Crystal-clear water laps at the shore.
Scattered seashells and starfish dot the sand. Beach grass sways in the breeze.
Distant cliffs with a coastal path. Fluffy clouds in a bright blue sky.""" },

  'easy_2': { 'frame': 'common', 'prompt': S + """A cute round pufferfish creature with glossy chartreuse/lime-green body that is
slightly inflated with tiny soft rounded spines. Lighter yellow-green belly.
Small round pectoral fins flapping. A surprised flustered expression with puffed
cheeks. Large sparkling bright green eyes with star highlights. Tiny "o" mouth.
It floats near the surface of calm harbor water, having just puffed up in surprise
at a small fish swimming by. Tiny bubbles rise from its mouth.
Background: a calm harbor scene at midday with crystal-clear turquoise water. A wooden
dock with barnacles visible underwater. Colorful tropical fish swim below. Sunlight
sparkles on the water surface. Boats in the distance. Half underwater perspective.""" },

  'easy_3': { 'frame': 'common', 'prompt': S + """A cute round starfish creature with glossy warm coral-orange body shaped like a
chubby five-pointed starfish blob. Each arm tip has a tiny lighter orange spot.
Its smooth round center has a lighter peach-colored belly. Large sparkling warm
orange eyes with star highlights. Rosy cheeks and a big happy cheerful smile.
It sits on a sun-warmed wooden dock post, tiny arms waving cheerfully at the viewer.
Small seashells and a tiny hermit crab sit nearby.
Background: a warm sunset harbor with wooden docks and colorful fishing boats
bobbing on calm golden water. Stacked lobster traps and coiled ropes. Seagulls fly
across a brilliant orange-pink sunset sky. Lighthouse in the distance.""" },

  'easy_4': { 'frame': 'uncommon', 'prompt': S + """A cute but imposing round fish-warrior creature with bright royal blue glossy body.
A small golden crown sits on its head with a teal jewel. A tiny golden trident held
in one stubby fin. Small blue-green fin ears. Large sparkling bright cyan eyes with
star highlights. Determined furrowed brows but still adorable. White belly. It stands
on a rocky outcrop by the crashing sea, one fin raised holding the trident proudly.
Background: a dramatic rocky coastline with waves crashing against dark rocks sending
up white spray. A lighthouse on a distant cliff. Storm clouds gathering on one side
but sunlight breaks through on the other. Dramatic lighting with turquoise sea.""" },

  'easy_5': { 'frame': 'common', 'prompt': S + """A cute round ladybug creature with glossy dark navy-black body and a bright red
shell/carapace with black polka dots on its back. Small black antennae with tiny
balls on the tips. Large sparkling warm golden-amber eyes with honeycomb-pattern
highlights. Rosy cheeks and a gentle smile. Tiny black legs. It sits on a large
colorful flower, wings slightly spread, basking in the sunshine.
Background: a vibrant flower garden overlooking the sea. Colorful flowers in full
bloom — roses, daisies, lavender. A castle or tower silhouette in the misty distance.
Butterflies flutter nearby. Bright blue sky with fluffy white clouds. Warm sunlight.""" },

  'easy_6': { 'frame': 'common', 'prompt': S + """A cute round anglerfish creature with glossy deep teal-green body. A bioluminescent
lure dangles from a small stalk on its forehead, glowing warm golden-yellow. Large
sparkling dark eyes with star highlights — expressive and curious despite the deep-sea
theme. Small fins on the sides. A wide friendly grin showing tiny rounded teeth.
It floats in deep blue water, its lure illuminating the area around it with warm light.
Background: a deep ocean scene with dark navy-blue water. The anglerfish's lure creates
a warm circle of golden light. Coral formations and sea anemones glow faintly below.
Small glowing jellyfish drift in the background. Mysterious deep-sea atmosphere.""" },

  'easy_7': { 'frame': 'common', 'prompt': S + """A cute round jellyfish creature with a translucent lavender-purple glossy dome cap.
Iridescent rainbow sheen on the dome surface. Delicate trailing tentacles below.
Large sparkling purple anime eyes with star highlights. Rosy cheeks, gentle smile.
The creature is SMALL — it floats in the center of the image with plenty of space
around it, taking up only 50% of frame height. Tentacles trail gracefully.
Background: deep ocean blue water gradient from lighter at top to darker navy below.
Tiny bioluminescent particles glow around it like underwater stars. Coral reef
hints at the bottom. Shafts of sunlight filter down from above. Serene atmosphere.""" },

  'easy_8': { 'frame': 'common', 'prompt': S + """A cute round crab creature with glossy warm chocolate-brown body and a lighter tan
belly. Two small pincers held up in a cheerful pose, as if showing them off. Large
sparkling warm honey-brown eyes with star highlights. Rosy cheeks and a proud grin.
Tiny legs beneath the round body. It stands on a wooden dock at sunset, striking
a confident pose with both pincers raised like a bodybuilder showing off.
Background: a warm harbor at sunset. Fishing boats moored at wooden docks. Golden
sunset light reflects off calm water. Stacked crates and fishing nets nearby. The sky
is painted in warm oranges and pinks. A few seagulls in the distance.""" },

  'easy_9': { 'frame': 'rare', 'prompt': S + """A majestic yet adorable round sea dragon creature with deep purple-blue glossy body.
A golden crown with a teal jewel on its head. Small bat-like wings. A curling dragon
tail. Blazing orange-amber eyes with fire-shaped highlights radiating power. Small
white claws on stubby feet. A satisfied regal smile. Despite being round and cute,
it radiates boss-level authority. Ocean waves churn around it dramatically.
Background: a dramatic stormy sea filling the entire image. Dark thunderclouds with
lightning bolts. Massive ocean waves crashing and swirling. Distant lighthouse on
cliffs. Sea spray catches dramatic lighting. Dark moody teal-gray storm atmosphere.""" },

  # ══════════════ NORMAL（森・黒衣森風）══════════════
  'normal_0': { 'frame': 'common', 'prompt': S + """A cute round mushroom creature with a large glossy red-and-white spotted mushroom
cap on its head. The cap has classic toadstool appearance with bright red top and
white polka dots. Its body is cream/beige and soft. Large sparkling warm brown eyes
with star highlights beneath the mushroom cap. Rosy cheeks and a shy gentle smile.
Tiny roots for feet. It stands in a mossy forest clearing, a few tiny spore particles
floating upward from under the cap.
Background: a lush enchanted forest with towering ancient trees. Dappled golden
sunlight filters through the dense green canopy. Moss-covered logs and rocks.
Small wildflowers dot the forest floor. Fireflies glow faintly. Peaceful atmosphere.""" },

  'normal_1': { 'frame': 'common', 'prompt': S + """A cute round mandragora/root vegetable creature with glossy warm orange body shaped
like a chubby carrot or turnip. Fresh green leaves sprout from the top of its head
like a natural crown. Small root-like feet. Large sparkling dark brown eyes with
star highlights, wide open in surprise — it looks like it was just pulled from the
ground and is startled. Tiny "o" shaped mouth. Dirt particles still cling to its body.
Background: a rich dark forest floor with upturned soil where it was just uprooted.
Surrounding roots and fallen leaves. Mushrooms grow on nearby logs. Soft diffused
forest light. Other small plants around the freshly dug hole. Earth-toned atmosphere.""" },

  'normal_2': { 'frame': 'common', 'prompt': S + """A cute round firefly creature with glowing lime-yellow translucent body. Its round
bottom glows brightly with warm yellow-green bioluminescent light, creating a soft
lantern-like radiance. Small translucent wings buzz on its back. Two tiny antennae
on top with glowing tips. Large sparkling yellow-green eyes with star highlights.
Cheerful excited expression. It flies through a dark nighttime forest, leaving a
trail of glowing light particles behind.
Background: a dark enchanted forest at night with tall shadowy trees. Dozens of tiny
firefly lights dot the darkness like floating stars. Soft green moss glows faintly on
tree trunks. Crescent moon through canopy. Magical mystical atmosphere.""" },

  'normal_3': { 'frame': 'common', 'prompt': S + """A cute round morbol/plant-beast creature with glossy dark olive-green body. Small
red flower buds sprout from the top of its head like a crown of roses. A slightly
grumpy but cute expression — tiny furrowed brows and a small pout showing one
fang. Large sparkling dark red-brown eyes with star highlights. Stubby vine-like
arms. It sits on a mossy log in a dense swamp-like forest, tiny vines trailing.
Background: a deep dark mossy forest with thick undergrowth. Ancient gnarled trees
with hanging moss. A misty atmosphere with blue-green fog. Ferns and bracket fungi
cover everything. Dim mysterious light filtering through. Primal swamp atmosphere.""" },

  'normal_4': { 'frame': 'uncommon', 'prompt': S + """A cute but fierce round wolf creature with glossy steel-gray fur and thick fluffy
white mane around its neck. Pointed wolf ears standing alert. A bushy gray tail.
Large sparkling fierce amber-golden eyes with sharp diamond-shaped highlights.
Furrowed eyebrows showing determination. A small scar on one cheek. Tiny sharp fangs
peek from its mouth in a confident smirk. One paw raised as if commanding respect.
Despite being fierce, its round chibi body is adorable.
Background: a mystical misty forest clearing surrounded by towering ancient oaks.
Morning fog rolls between tree trunks. Golden sunlight breaks through the canopy.
Ancient standing stones covered in moss and runes form a circle. Fallen autumn leaves.""" },

  'normal_5': { 'frame': 'common', 'prompt': S + """A cute round frog creature with glossy sky-blue body and white belly. Smooth slightly
transparent skin like blue glass. Large sparkling aqua-blue eyes with star highlights.
Rosy cheeks. A small golden crown sits tilted on its head. It sits on a large green
lily pad on a forest pond, puffing up its white throat pouch while singing joyfully.
Tiny colorful musical notes float upward from its mouth.
Background: a sunlit forest pond surrounded by lush green vegetation. Multiple lily
pads with small pink lotus flowers. Tall trees with golden sunlight through leaves.
Dragonflies hover nearby. Crystal-clear water with visible pebbles. Bright peaceful.""" },

  'normal_6': { 'frame': 'common', 'prompt': S + """A cute round baby chocobo/chick creature with fluffy bright golden-yellow feathers.
A small orange beak. Tiny wings flapping excitedly as it runs. Large sparkling dark
brown-black eyes with star highlights — round and innocent. Rosy cheeks and a wide
happy open-mouth smile. A single tuft of feather sticks up on its head. Tiny orange
bird feet in mid-run. It dashes across a farm field with pure joy.
Background: a peaceful pastoral ranch with green rolling hills and a wooden fence.
A red barn visible in the distance. Fluffy sheep grazing nearby. Blue sky with
cotton-candy clouds. Warm gentle sunlight. Country farm atmosphere.""" },

  'normal_7': { 'frame': 'common', 'prompt': S + """A cute round tree spirit/dryad creature with glossy mossy-green body covered in tiny
leaves and small branches growing from it. An acorn dangles from one small branch.
Vine arms reach outward gently. Large sparkling warm amber-orange eyes with star
highlights. A peaceful sleepy smile. It sits contentedly on a thick tree branch high
up in the canopy, legs dangling. Dappled sunlight warms its mossy body.
Background: high up in the canopy of an ancient forest. Massive tree branches form
natural platforms. Hanging vines and creeping moss everywhere. Golden sunbeams cut
through the leaves. A bird's nest nearby. Far below, the forest floor is barely
visible through the foliage. Peaceful elevated forest atmosphere.""" },

  'normal_8': { 'frame': 'common', 'prompt': S + """A cute round fox spirit creature with glossy warm amber-orange fur and fluffy white
chest. A bushy fox tail with white tip that has small blue-white spirit flames
flickering from the tip. Pointed fox ears with dark tips. Large sparkling golden-amber
eyes with star highlights. A mischievous grin showing one tiny fang. One tiny paw
raised as if casting a spell. Three small blue-white foxfire flames float around it.
Background: an autumn forest at dusk with trees in brilliant red, orange, and gold
foliage. A weathered red torii gate silhouette visible in the misty background.
Fallen maple leaves carpet the ground. Golden-hour lighting with purple twilight sky.
Mysterious Japanese folklore atmosphere.""" },

  'normal_9': { 'frame': 'rare', 'prompt': S + """A majestic yet adorable round moogle king creature with fluffy pure white body.
A small red pompom bobbles on a stalk above its head. A golden crown with a red
gem sits between tiny bat-like purple wings. Large sparkling deep red-pink eyes with
star highlights. Rosy cheeks. A regal but sweet expression — it knows it's royalty
but is still friendly. It sits on an ancient tree stump in a magical fairy ring.
Background: an enchanted forest clearing at twilight. A circle of glowing mushrooms
forms a fairy ring around the stump. Tiny magical sparkles and fireflies float
everywhere. Ancient trees with hanging moss surround the clearing. Soft golden-green
magical light emanates from the ground. Small red mushrooms dot the grass.""" },

  # ══════════════ HARD（砂漠・ザナラーン風）══════════════
  'hard_0': { 'frame': 'common', 'prompt': S + """A cute round rock golem creature with glossy blue-gray stone body covered in natural
cracks and weathered texture. Small teal-blue crystal gems embedded in its surface
glow faintly. Thick stone eyebrow ridges give it a determined look. Large sparkling
ice-blue diamond-shaped eyes with cross highlights. A small crack on its forehead
reveals a glowing teal light inside. Tiny stone fists. Sturdy and ancient but adorable.
Background: dramatic desert ruins at golden sunset. Crumbling sandstone pillars and
ancient carved doorways. The setting sun creates spectacular orange-gold sky behind
towering mesa formations. Sand drifts around ruins. Archaeological dig atmosphere.""" },

  'hard_1': { 'frame': 'common', 'prompt': S + """A cute round scorpion creature with glossy sandy-beige/tan body like desert sand.
Segmented tail curls up high above its head with a small stinger that glows faintly
orange. Two small pincers held up in a threatening but adorable pose. Dark brown
camouflage markings on its back. Large sparkling amber-brown eyes with star highlights.
It emerges halfway from desert sand, tail raised high in warning.
Background: vast desert landscape at golden sunset. Towering sand dunes stretch into
the distance under dramatic orange-pink sky. Heat shimmer rises from sand. Scattered
desert rocks and a lone dead tree. Warm golden light bathes everything.""" },

  'hard_2': { 'frame': 'common', 'prompt': S + """A cute round falcon/hawk creature with brilliant golden-brown glossy plumage. White
chest with golden-brown speckles. Small fierce spread wings with darker brown tips.
A small curved golden beak. Sharp but adorable large golden eyes with diamond-shaped
highlights. A tiny golden anklet on one foot. It perches on a desert rock, body
puffed up proudly, wings slightly spread, scanning the horizon with fierce determination.
Background: dramatic desert canyon at sunrise. Towering sandstone cliffs in warm orange
and red layers. Distant pyramids on the horizon. Rising sun creates dramatic golden
rays cutting through morning haze. Eagles soar as tiny silhouettes.""" },

  'hard_3': { 'frame': 'common', 'prompt': S + """A cute round cactus creature with glossy bright green body covered in small golden
spines. A beautiful pink flower blooms on top of its head. Small cactus arm-branches
wave cheerfully on each side. Large sparkling dark green eyes with star highlights.
Rosy cheeks and a wide happy smile. It dances joyfully in a cactus field, one foot
raised in mid-step, tiny cactus flower petals falling from its bloom.
Background: a beautiful desert cactus field at golden sunset. Tall saguaro cacti
and prickly pear surround it. Mountains in the distance painted in purple and orange.
The sky blazes with warm sunset colors. Small desert wildflowers bloom at the base
of each cactus. Warm peaceful desert evening atmosphere.""" },

  'hard_4': { 'frame': 'uncommon', 'prompt': S + """A cute but imposing round desert sphinx creature with glossy warm golden-amber body.
A pharaoh-style striped headdress (nemes) in blue and gold sits on its round head.
Small lion paws visible below. A mysterious knowing smile. Large sparkling deep amber
eyes with hieroglyph-shaped highlights — ancient wisdom in cute form. Tiny golden
wings folded at its sides. A golden ankh pendant hangs from its neck on a chain.
It sits regally on a stone pedestal in front of a massive pyramid.
Background: a dramatic Egyptian-inspired desert at golden hour. A massive golden
pyramid rises behind the creature. The Sphinx's own shadow stretches across golden
sand. Obelisks with hieroglyphs flank the scene. Warm amber light bathes everything.
A crescent moon is already visible in the darkening sky above.""" },

  'hard_5': { 'frame': 'common', 'prompt': S + """A cute round crystal-scorpion creature with glossy teal/cyan body that shimmers
with inner crystalline glow. Small crystalline segments along its back refract light
into rainbow sparkles. Curled tail with glowing teal crystal tip. Two small translucent
pincers. Large sparkling emerald-teal eyes with gem-facet highlights. It is inside
a cavern, happily munching on a glowing teal crystal, mouth sparkling with crystal
dust. Tiny crystal shards float around its head.
Background: spectacular crystal cavern with massive teal and cyan crystal formations.
Veins of glowing minerals in the rock. Underground pool reflects crystal light.
Blue-green luminescence everywhere. Magical underground atmosphere.""" },

  'hard_6': { 'frame': 'common', 'prompt': S + """A cute round bomb creature with glossy dark navy-blue body (NOT red). A metal cap
on top with a blue-tipped fuse that has bright blue-white sparks shooting from it.
Dark midnight blue body with tiny star-like sparkle patterns on surface. Large panicked
spiral eyes in pale blue, mouth open in worried expression, a single blue sweat drop.
Background: desert landscape at night under spectacular starry sky with Milky Way
visible. Sand dunes in cool blue-gray moonlight. Blue sparks from fuse illuminate
nearby sand. Shooting stars streak across sky. Cool blue nighttime atmosphere.""" },

  'hard_7': { 'frame': 'common', 'prompt': S + """A cute round cobra creature with glossy jade-green/emerald body (NOT red). Beautiful
darker green scale pattern. A lighter green belly. A small jade-green cobra hood fans
out behind its head with golden ornamental markings. Large sparkling yellow-green
slit-pupil eyes. Forked tongue flicks out playfully. Regal and mysterious expression.
It is coiled in front of golden desert ruins, looking wise and confident.
Background: ancient golden desert ruins with hieroglyph-covered sandstone walls.
Sunlight streams through crumbled doorway creating dramatic light shafts. Green vines
creep along ruins. Sand piles in corners. Warm golden afternoon light contrasts with
the green snake. Mysterious archaeological atmosphere.""" },

  'hard_8': { 'frame': 'common', 'prompt': S + """A cute round mineral/crystal creature with glossy ice-blue/frost-blue body (NOT brown).
Body covered in sparkling ice-blue and pale white crystal clusters that grow from
surface like frozen flowers. Translucent frosted glass quality. Large sparkling
diamond-blue eyes like cut sapphires with bright white star highlights. Gentle peaceful
smile. Tiny ice crystal feet. It glows softly with inner blue-white light.
Background: mine tunnel with wooden support beams and old mining rails. Cool blue-white
light from ice-blue crystal formations along walls. Mining lantern on beam casting
warm contrasting light. Mine cart on rails in distance. Underground mine atmosphere.""" },

  'hard_9': { 'frame': 'rare', 'prompt': S + """A majestic cute round fire demon creature with deep dark crimson body (darker than
typical red). Emanates an aura of blue-purple flames mixed with orange fire. Flame-
shaped eyes that burn with inner blue-white fire center, surrounded by orange flame
iris. Two small dark horns. Sharp tiny fangs in fierce grin. The creature radiates
overwhelming boss energy despite being adorably round. Rosy cheeks for cute contrast.
Background: volcanic arena with dark basalt pillars. Rivers of bright orange lava
flow on ground. Dramatic tall pillars of BLUE fire rise on both sides creating
unusual contrast with orange lava. Dark volcanic ash clouds swirl above. Blue and
orange fire creates spectacular dual-tone lighting. Epic boss arena atmosphere.""" },
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
