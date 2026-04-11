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
  'easy_0': { 'frame': 'common', 'prompt': S + """Scene: A pink slime jelly blob — NOT a dog or animal — a simple featureless blob
of translucent bubblegum-pink gelatin with no ears, no nose, no fur. It has just
stepped outside its dark warehouse home for the very first time and is seeing the
ocean for the first time in its life. Its body trembles with excitement, a tiny
trail of pink goo leads from the warehouse door behind it. A small heart-shaped
bubble floats above its head expressing its overwhelming emotion. Its deep blue eyes
with HEART-SHAPED highlights are wide with wonder, reflecting the vast turquoise sea.
Background: sunlit wooden dock at golden hour. The warehouse door is slightly ajar
behind. Calm turquoise ocean stretches to the horizon. Wooden barrels, coiled ropes.
A distant lighthouse. Seagulls soar. First-time-seeing-the-world atmosphere.""" },

  'easy_1': { 'frame': 'common', 'prompt': S + """Scene: A cream-yellow snail creature with a large golden spiral shell has just found
the legendary "rainbow conch shell" after years of searching. It holds the shimmering
iridescent shell high in one tiny hand while the other clutches its worn woven basket
overflowing with ordinary shells. It is running joyfully along the beach with a single
happy tear rolling down its cheek. A trail of tiny footprints stretches behind it in
the wet sand. Its warm brown eyes have TEARDROP-SHAPED highlights — tears of joy.
Background: warm sandy beach at midday. Crystal water. Countless shells and starfish
scattered on sand. Beach grass. Distant cliffs with a coastal path. Bright blue sky.""" },

  'easy_2': { 'frame': 'common', 'prompt': S + """Scene: A chartreuse/lime-green pufferfish was peacefully floating in the harbor when
a mischievous little fish snuck up and shouted "BOO!" from behind. The pufferfish
has instantly inflated to twice its size in shock, spines popping out, eyes wide as
saucers, mouth frozen in an "O" of surprise. Tiny bubbles stream from its mouth.
But the prankster fish is now MORE scared of the inflated pufferfish and is fleeing
in the background. Its bright green eyes have RIPPLE-RING highlights like shockwaves.
Background: calm harbor half-underwater view. Wooden dock pilings with barnacles.
The fleeing small fish visible. Tropical fish below. Sunlight dances on the surface.""" },

  'easy_3': { 'frame': 'common', 'prompt': S + """Scene: Every evening at sunset, this coral-orange starfish climbs the tallest dock
post to wave goodbye to departing fishing boats — the fishermen call it "the little
lighthouse." Tonight it waves all five arms enthusiastically as a boat sails past,
its warm orange eyes with STAR-SHAPED highlights (matching its starfish body) shining
with devotion. A tiny seashell necklace bounces as it waves. The fisherman on the
boat waves back with a smile.
Background: warm sunset harbor. Colorful fishing boats on golden water. One boat
sailing away. Lobster traps and ropes. Orange-pink sunset sky. Seagulls.""" },

  'easy_4': { 'frame': 'uncommon', 'prompt': S + """Scene: A storm is approaching the harbor. The royal blue fish-warrior stands on the
tallest rock at the harbor entrance, raising its inherited golden trident toward the
darkening sky. Lightning reflects off its golden crown's teal jewel. "This harbor is
under MY protection." Its cyan eyes with DIAMOND-SHAPED highlights blaze with resolve.
Behind it, the harbor's fishing boats are safely moored, protected by this small
but determined guardian.
Background: dramatic rocky coastline. Storm clouds roll in from one side while golden
sunlight breaks through on the other. Crashing waves. Distant lighthouse.""" },

  'easy_5': { 'frame': 'common', 'prompt': S + """Scene: On a secret cliff-top garden that nobody else knows about, this navy-black
ladybug has been tending flowers alone for years. This morning, the rose it planted
last spring has finally bloomed. It spreads its red dotted shell slightly, reaching
one tiny leg gently toward the rose petal, afraid to damage it. A small watering
can sits at its feet. Its golden-amber eyes with HONEYCOMB highlights are misty
with quiet pride and tenderness.
Background: vibrant secret flower garden on a sea cliff. Roses, daisies, lavender.
Castle tower silhouette in misty distance. Butterflies. Morning sunlight.""" },

  'easy_6': { 'frame': 'common', 'prompt': S + """Scene: Deep in the dark ocean, this teal anglerfish has found a school of tiny lost
baby fish crying in the darkness. It turns its golden lure to maximum brightness and
says "Follow me, the exit is this way." The baby fish line up single-file behind it,
their little eyes reflecting the warm golden light. Its dark eyes have GLOWING ROUND
SPOTLIGHT highlights — its own light reflected within. A wide friendly grin.
Background: dark deep ocean. The lure creates a warm golden light trail. Baby fish
following in a line. Coral formations glow faintly. Glowing jellyfish. Warm and kind.""" },

  'easy_7': { 'frame': 'common', 'prompt': S + """Scene: On a full-moon night, this lavender jellyfish has floated up near the surface
for its monthly moonlight bath. The moonlight passes through its translucent dome,
making its entire body shimmer with iridescent rainbow colors. Its eyes are half-closed
in blissful ecstasy, purple eyes with CRESCENT MOON highlights reflecting the moon.
Tentacles sway gently like curtains in moonlight. The creature is SMALL, only 50%
of frame height, floating serenely with generous space around it.
Background: deep ocean blue gradient. Full moon visible above water surface. Tiny
bioluminescent particles. Coral hints below. Moonlight shafts. Peaceful and dreamy.""" },

  'easy_8': { 'frame': 'common', 'prompt': S + """Scene: This chocolate-brown crab has just won the annual Harbor Strength Competition!
Both pincers raised high in a triumphant bodybuilder pose, a shiny gold medal hanging
around its neck catching the sunset light. Tiny fish spectators cheer around it.
Its honey-brown eyes with WARM OVAL highlights blaze with the thrill of victory.
The trophy sits on the dock beside it — a golden anchor statuette.
Background: warm harbor at sunset. Fishing boats at docks. Golden light on calm
water. A small crowd of sea creatures cheering. Orange-pink sky.""" },

  'easy_9': { 'frame': 'rare', 'prompt': S + """Scene: Once every hundred years, a catastrophic storm threatens the harbor. The
ancient sea dragon awakens from the ocean depths, crown blazing as lightning strikes
its teal jewel. It rises through the parting waves, wings spread wide, facing the
storm head-on to protect the harbor. Its blazing orange-amber eyes with FLAME-SHAPED
highlights burn with ancient power. This is not anger — it is duty. The roar splits
the clouds. The lighthouse keeper watches in awe from the distant cliff.
Background: epic stormy sea. Lightning-filled thunderclouds. Massive parting waves.
Rain and sea spray. Distant lighthouse with a tiny figure watching. Dark and majestic.""" },

  # ══════════════ NORMAL（森・黒衣森風）══════════════
  'normal_0': { 'frame': 'common', 'prompt': S + """Scene: The rain has just stopped in the enchanted forest. This shy mushroom creature
peeks out from under its red-and-white spotted cap, where a few raindrops still cling
like tiny jewels catching the first ray of sunlight. It is looking up timidly,
searching for a rainbow that might appear. A small puddle at its feet reflects its
own face. Its warm brown eyes have SOFT ROUND DEWDROP highlights like the raindrops
on its cap. Tiny spore particles drift upward in the golden light.
Background: lush enchanted forest just after rain. Everything glistens with moisture.
Dappled golden sunlight through canopy. Moss-covered logs. Small puddles. Rainbow
hint in the sky. Wildflowers with water droplets. Fresh peaceful atmosphere.""" },

  'normal_1': { 'frame': 'common', 'prompt': S + """Scene: This orange mandragora had been peacefully sleeping underground for 100 years
when a curious squirrel grabbed its leaf-hair and yanked it out. Captured in the
exact moment of being uprooted — eyes bulging in absolute shock, mouth frozen in
a perfect "O," leaf-hair still messy from 100 years of bedhead. Dirt clumps cling
to its round body. The freshly dug hole is visible below. Its dark brown eyes have
WIDE SHOCKED SPARKLE highlights — multiple scattered light dots of total bewilderment.
Background: rich dark forest floor with upturned soil. The hole it was pulled from.
Roots and fallen leaves. A squirrel tail visible at the edge fleeing. Mushrooms on logs.""" },

  'normal_2': { 'frame': 'common', 'prompt': S + """Scene: In the dark nighttime forest, a baby squirrel was crying, lost and alone. This
lime-yellow firefly found it and turned its glow to maximum brightness, becoming a
living lantern. "Follow me, I know the way home!" Its glowing trail of golden light
particles creates a sparkling path through the darkness. The baby squirrel reaches
toward the warm glow, following trustingly. Its yellow-green eyes have GLOWING HALO
highlights — rings of light like a guiding beacon. Antennae tips glow bright.
Background: dark enchanted forest at night. The firefly's light creates a golden path.
A tiny crying squirrel following. Other fireflies dot the darkness. Crescent moon.""" },

  'normal_3': { 'frame': 'common', 'prompt': S + """Scene: This dark olive-green morbol LOOKS terrifying — furrowed brows, one fang
showing, grumpy pout — but it is actually babysitting. Hidden among the red flower
buds on its head, a tiny baby bird chick peeks out, completely safe and happy. The
morbol is deliberately making its scariest face to ward off predators, but if you
look closely, the corner of its mouth is fighting back a smile. Broken eggshell
pieces are scattered at its feet. Its dark red-brown eyes have CROSS/THORN highlights
— protective thorns guarding something precious.
Background: deep dark mossy forest. Gnarled trees with hanging moss. Blue-green fog.
A hawk silhouette in the distance, scared away by the scary face.""" },

  'normal_4': { 'frame': 'uncommon', 'prompt': S + """Scene: This steel-gray wolf is the last surviving member of the ancient Forest
Guardian pack. It stands before moss-covered rune stones in the morning mist,
one paw raised in challenge to an approaching adventurer. The scar on its cheek
was inherited from the previous pack leader — a mark of duty, not battle. "If you
wish to pass, you must prove your worth." Its fierce amber-golden eyes with SHARP
VERTICAL SLIT highlights burn with lonely pride. White mane bristles. Tiny fangs
gleam in a confident smirk. Adorable despite its fierce demeanor.
Background: mystical misty forest clearing. Ancient standing stones with glowing
runes. Morning fog. Golden sunlight breaking through oaks. Fallen autumn leaves.""" },

  'normal_5': { 'frame': 'common', 'prompt': S + """Scene: This sky-blue frog is convinced it is the world's greatest singer. Every
night it performs a "sold-out concert" on its lily pad stage. Tonight is the special
full-moon performance. It puffs its white throat pouch to maximum, belting out its
best song with eyes closed in rapture. Colorful musical notes float upward. Its
tilted golden crown is self-awarded — "The Singing King." The entire audience is
three dragonflies and one unimpressed fish. Its aqua eyes have HORIZONTAL OVAL
FROG-PUPIL highlights with sparkles.
Background: sunlit forest pond. Lily pads with pink lotus as stage decorations.
Three dragonflies watching. One fish peeking above water. Musical notes in the air.""" },

  'normal_6': { 'frame': 'common', 'prompt': S + """Scene: This golden-yellow baby chocobo chick just learned to run THIS MORNING and
is now racing a butterfly. Its tiny legs are tangled and it is leaning forward about
to stumble, but its face shows pure ecstatic joy — the happiest moment of its very
short life. What it does not know is that the butterfly is actually leading it toward
its sibling chicks waiting at the farm. A single head-tuft feather bounces wildly.
Its dark brown-black eyes have the LARGEST, MOST INNOCENT ROUND highlights of any
creature — pure childlike wonder in its first adventure.
Background: pastoral ranch with green hills and wooden fence. Red barn in distance.
A butterfly just ahead. Fluffy sheep watching. Blue sky with cotton-candy clouds.""" },

  'normal_7': { 'frame': 'common', 'prompt': S + """Scene: This mossy-green dryad has lived in this ancient tree for 500 years. It knows
every bird by name, every season by heart. Right now, it was singing a lullaby to the
baby birds in a nearby nest when it accidentally fell asleep mid-song. An acorn just
dropped onto its head with a soft "bonk" — one eye is half-open in sleepy confusion
while the other stays shut. Its vine arms still gently cradle the branch. Its warm
amber-orange eyes have LEAF-SHAPED highlights, as if golden autumn leaves float
inside its irises.
Background: high up in ancient forest canopy. Thick mossy branch. A bird's nest with
sleeping chicks nearby. The dropped acorn on its head. Dappled golden sunlight.""" },

  'normal_8': { 'frame': 'common', 'prompt': S + """Scene: This amber-orange fox spirit is the forest's famous trickster — it lures
travelers with foxfire, but always secretly guides them to safety. Tonight it sits
before a red torii gate, three floating blue-white foxfires dancing around it, one
paw beckoning "This way~" with a mischievous wink. What travelers do not know is that
every path the fox creates leads to the warm hot spring inn. Its golden-amber eyes
with VERTICAL FOXFIRE-FLAME highlights burn with playful mischief and hidden kindness.
One tiny fang peeks from its smirk. Bushy tail-tip flickers with blue spirit fire.
Background: autumn dusk forest. Brilliant red-orange-gold foliage. Red torii gate.
Falling maple leaves. Three blue foxfires. Purple twilight sky above.""" },

  'normal_9': { 'frame': 'rare', 'prompt': S + """Scene: The tiny king of the fairy realm sits on his tree-stump throne, about to
deliver judgment in the Great Acorn Dispute. He raises a tiny wooden gavel — "This
acorn belongs to Squirrel-kun!" The fairy ring of glowing mushrooms around his throne
pulses with golden light as he speaks. His red pompom bounces with authority. Despite
being tiny and adorably round, every creature in the forest respects his wisdom. His
deep red-pink eyes have ROYAL CROSS-STAR highlights radiating regal authority. Tiny
purple wings flutter. Golden crown gleams with a red gem.
Background: enchanted clearing at twilight. Glowing mushroom fairy ring. Magical
sparkles and fireflies. A squirrel and chipmunk waiting for the verdict. Ancient trees.""" },

  # ══════════════ HARD（砂漠・ザナラーン風）══════════════
  'hard_0': { 'frame': 'common', 'prompt': S + """Scene: For 1000 years, this blue-gray stone golem has guarded a temple that no one
visits anymore. It watches yet another sunset alone, the golden light catching the
teal crystals embedded in its cracked body. One particular crack runs down its cheek
like a tear trail — not damage, but the mark of centuries of solitary vigil. Yet
there is peace in its ice-blue eyes with CROSS/CRYSTAL highlights. It still finds
the sunset beautiful. A single desert flower has grown in a crack on its shoulder.
Background: ancient crumbling desert temple at golden sunset. Sand-worn pillars.
The setting sun paints everything amber-gold. A tiny desert flower growing in ruins.""" },

  'hard_1': { 'frame': 'common', 'prompt': S + """Scene: This sandy-beige scorpion has been buried motionless in the desert sand for
THREE DAYS, waiting for a sand lizard to come within range. Finally — the moment
arrives! It bursts from the sand in an explosive spray, tail raised high with its
orange-glowing stinger charged. But the lizard just barely escapes, and the scorpion's
expression shifts from fierce hunter to deflated "...three more days then." Its
amber-brown eyes have SHARP TRIANGULAR highlights — a hunter's precision focus.
Background: vast desert at golden sunset. Sand exploding upward from the ambush spot.
A tiny lizard fleeing in the distance. Towering dunes. Orange-pink sky.""" },

  'hard_2': { 'frame': 'common', 'prompt': S + """Scene: This golden-brown young falcon stands at the edge of its cliff nest on its
fledging day — the first flight of its life. Wings spread wide for the first time,
trembling slightly. Below stretches the vast desert it has only seen from above.
Distant pyramids. It is terrified but the excitement is winning — "I can do this!"
Behind it, the silhouette of its parent watches proudly. Its golden eyes with SHARP
DIAMOND/RAPTOR highlights are laser-focused on the horizon, gathering courage.
Background: dramatic desert canyon at sunrise. Canyon edge with nest visible. Vast
desert and pyramids below. Parent hawk silhouette behind. Golden sunrise rays.""" },

  'hard_3': { 'frame': 'common', 'prompt': S + """Scene: A cactus creature's head-flower blooms only once every 100 years. This is THAT
moment — the pink flower has just opened and the cactus is SO happy it has begun
dancing uncontrollably. Flower petals scatter with each joyful spin. The surrounding
cacti have also sprouted tiny celebratory flowers in solidarity. Even the desert
blooms with rare wildflowers for this occasion. Its dark green eyes with SPARKLE-BURST
highlights are fireworks of pure hundred-year joy.
Background: desert cactus field at golden sunset. All cacti have tiny flowers blooming
in celebration. Mountains in purple-orange. Desert wildflowers everywhere.""" },

  'hard_4': { 'frame': 'uncommon', 'prompt': S + """Scene: Another treasure seeker has arrived at the pyramid. The golden sphinx sits on
its stone pedestal, regarding the challenger with ancient eyes that have seen thousands
fail. "Answer me: what walks on four legs at dawn, two at noon, three at dusk?" Its
mysterious smile has not changed in 3000 years. The ankh pendant on its chest glows
faintly. No one has ever answered correctly. Its deep amber eyes have HIEROGLYPH-SHAPED
highlights — the Eye of Horus itself reflected in its ancient gaze. Blue-and-gold
pharaoh headdress gleams. Tiny golden wings folded at sides.
Background: Egyptian desert at golden hour. Massive pyramid behind casting shadow.
Obelisks with hieroglyphs. A tiny adventurer silhouette approaching. Crescent moon.""" },

  'hard_5': { 'frame': 'common', 'prompt': S + """Scene: This teal crystal-scorpion was literally born from a cave crystal — and
right now it is "talking" to its crystal siblings by nibbling on a glowing teal gem.
The sparkles at its mouth are not crumbs but the crystal's "words" being received.
It is still half-embedded in its birth-crystal, tail curled happily. It has never
known loneliness because every crystal in this cave is family. Its emerald-teal eyes
with GEM-FACET highlights see the world through crystal clarity.
Background: spectacular crystal cavern. Massive teal formations. The scorpion is
partially emerging from a large crystal. Glowing mineral veins. Underground pool.""" },

  'hard_6': { 'frame': 'common', 'prompt': S + """Scene: This dark navy-blue bomb creature is an amateur astronomer who loves
stargazing. Tonight it was watching the Milky Way from atop a sand dune when it got
so excited about a shooting star that it BOUNCED — and accidentally lit its own fuse.
"Wait no no NO—" Its eyes are panicked SPIRALS, mouth open in horror, a blue sweat
drop on its forehead. But the blue sparks from its fuse are mixing with the actual
stars above, and the scene is accidentally beautiful. Only the bomb is panicking.
Background: desert night under magnificent Milky Way. Sand dunes in blue moonlight.
Shooting stars. The bomb's blue sparks blend with the starry sky. Comically beautiful.""" },

  'hard_7': { 'frame': 'common', 'prompt': S + """Scene: This jade-green cobra has spent 1000 years memorizing every hieroglyph on
these ancient ruin walls. It has just finished reading the very last character — and
the walls begin to glow gold. The thousand-year mystery is revealed to be... an
ancient scholar's joke: "Congratulations, you actually read all of this!" The cobra's
expression is a mix of disbelief, exasperation, and reluctant amusement. Its forked
tongue flicks in annoyance. Its yellow-green eyes have VERTICAL SLIT-PUPIL highlights
with golden knowledge-light. The golden cobra hood has ornamental markings.
Background: golden desert ruins. Hieroglyph walls glowing gold. Dramatic light shafts
through crumbled doorway. Green vines on ancient stone. Warm golden light.""" },

  'hard_8': { 'frame': 'common', 'prompt': S + """Scene: Frozen for tens of thousands of years in the deepest mine shaft, this ice-blue
crystal creature has just been awakened by a miner's lantern. Its first sight in eons
is the warm orange glow of the lantern — so different from its own cold blue light.
Crystal flowers bloom from its body as it slowly awakens, spreading icy light through
the tunnel. It gazes at the lantern's warmth with gentle wonder and curiosity. Its
diamond-blue eyes with SAPPHIRE-FACET highlights are ancient but newly curious.
Background: mine tunnel with wooden beams and rails. The miner's dropped warm lantern
contrasts with cool blue crystal light. Ice-blue formations on walls. Mine cart.""" },

  'hard_9': { 'frame': 'rare', 'prompt': S + """Scene: The volcanic arena's ultimate guardian has been waiting for a truly worthy
challenger. Today one has finally arrived. The dark crimson fire demon rises from its
lava throne, and for the first time in centuries, its forbidden "blue flame" awakens
— a power it only unleashes against opponents who deserve its full respect. Blue-purple
fire erupts alongside the traditional orange flames, creating an unprecedented
spectacle. "Come. Show me everything you have." Its eyes burn with DUAL-TONE FIRE —
blue-white center, orange outer ring — radiating overwhelming boss majesty. Dark horns.
Tiny fangs in a fierce, respectful grin. Rosy cheeks despite the inferno.
Background: volcanic arena. Dark basalt pillars. Orange lava rivers AND dramatic blue
fire pillars rising on both sides. Volcanic ash clouds. Dual-tone fire lighting.""" },
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
