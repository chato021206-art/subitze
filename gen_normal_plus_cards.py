#!/usr/bin/env python3
"""Generate NORMAL+ card images using Gemini Nano Banana 2.

NORMAL+ concept: "もうひとつの季節／もうひとつの顔"
Base character's alternate-season / alternate-role moment, with a ~180deg
hue-shifted color scheme. Same species/shape, opposite mood or time-of-day.
"""
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

IMPORTANT: This is a "+" variant — an alternate color version of the base
character. Same species and silhouette, but a completely different color
scheme (~180 degree hue shift) and a completely different scene/mood.

"""

CARDS = {
  # 0. ファンガ+ — 夜の灯台きのこ
  'normal_plus_0': { 'frame': 'common', 'prompt': S + """Character: A night-variant mushroom creature — same shy round mushroom species
as the white-and-red original, but this one has a DEEP INDIGO-VIOLET CAP with
SILVER-WHITE DOTS instead of red. The cap edges and gills glow faintly with
bioluminescent cyan light. Cream-colored stubby body. Large sparkling deep
violet eyes with SOFT ROUND DEWDROP highlights.

Story: Night has fallen on the enchanted forest. This indigo mushroom turns on
its bioluminescent cap and becomes a living lantern for nocturnal forest
creatures. A small brown owl is perched on its cap edge, bats glide in the
silvery light, tiny fireflies circle around it. Its expression is quietly
confident — a proud little night watchman. One tiny arm holds a drifting
dandelion seed like a torch.

Background: deep midnight enchanted forest. Moonlight filters through the
canopy. Bioluminescent mushrooms glow in the distance. Owls and bats silhouetted.
A crescent moon high above. Mystical blue-violet atmosphere.""" },

  # 1. マンドラ+ — 誕生日ミッション
  'normal_plus_1': { 'frame': 'common', 'prompt': S + """Character: A plum-purple/violet mandragora creature — same round species as the
orange original, but with VIBRANT PLUM-PURPLE body and DEEP MAGENTA leaf-hair
instead of orange/green. Large sparkling magenta eyes with WIDE JOYFUL SPARKLE
highlights (multiple excited light dots, opposite of the shocked version).

Story: Unlike its orange cousin who was yanked out, this purple mandragora has
CHOSEN to leap out of the ground on its own. It has a tiny wrapped birthday
present held up high in one leaf-arm and a party hat tilted on its leaves.
Mission: deliver the present to its underground family's birthday party! Dirt
clumps fly upward from the fresh hole below, and a confetti trail follows its
jump. Expression: brave determination mixed with excited anticipation — tongue
slightly poking out in effort.

Background: rich forest floor at dusk, warm magenta and golden sunset light.
The freshly-jumped-from hole below. Paper streamers and confetti in the air.
Small mushroom lanterns lining a trail. Festive but cozy atmosphere.""" },

  # 2. ホタルン+ — 雨の日の虹づくり
  'normal_plus_2': { 'frame': 'common', 'prompt': S + """Character: A deep sapphire-blue firefly creature — same round firefly species
as the lime-yellow original, but with a JEWEL-BLUE body and CYAN-WHITE antenna
glow instead of yellow-green. Large sparkling sapphire eyes with GLOWING HALO
highlights — rings of cool blue light.

Story: It is pouring rain in the forest and a tiny baby rabbit is crying under
a leaf, terrified of thunder. This blue firefly flies in close and lights up
each raindrop one by one, turning them into floating prismatic rainbow beads
that hang in the air around the rabbit like a protective aurora. The rabbit's
tears have stopped, eyes wide with wonder at the floating rainbow. Tiny rainbow
refractions play across the firefly's body. Expression: calm, gentle reassurance.

Background: rainy forest during a storm. Raindrops caught mid-fall, each one
glowing with rainbow refraction from the firefly's light. A tiny brown rabbit
under a leaf watching in awe. Soft grey-blue rain atmosphere warmed by the
magical rainbow light.""" },

  # 3. モルビー+ — バレンタインの秘密手紙
  'normal_plus_3': { 'frame': 'common', 'prompt': S + """Character: A rose-pink morbol creature — same round grumpy-looking species as
the dark olive original, but with a SOFT ROSE-PINK body and CORAL-PINK flower
buds on its head instead of red/olive. Despite the pink color the face still
wears the signature grumpy morbol pout — but now it looks like bashful blushing
instead of scary. Large sparkling coral-pink eyes with HEART-SHAPED highlights.

Story: It is Valentine's morning in the forest. This pink morbol is secretly
a romantic at heart. It is tiptoeing up to a sleeping deer family's doorstep
to leave a tiny handmade love letter — a folded pink leaf sealed with a tree
sap heart. Its pout is extreme bashful embarrassment. Both cheeks are crimson.
One tiny tentacle-arm holds the letter out, another covers its face in shyness.
A trail of tiny heart-shaped petals follows its path, showing it has been
delivering letters all morning.

Background: dawn forest clearing. Pink cherry blossom petals drift through the
air. A hollow-tree home with a tiny wreath of pink flowers. Soft pastel pink
dawn light. Hearts drawn in the morning dew on nearby leaves. Shy romantic
atmosphere.""" },

  # 4. ガルウ+ — 冬の夜明けの遠吠え教室
  'normal_plus_4': { 'frame': 'uncommon', 'prompt': S + """Character: A snow-white wolf creature — same round wolf species as the
steel-gray original, but with GLEAMING SNOW-WHITE fur and PALE ICE-BLUE mane
tips instead of gray. Same proud scar on the cheek, now softened by age.
Large sparkling pale ice-blue eyes with SOFT CRESCENT-MOON highlights — the
fierce vertical slit is replaced by gentle warmth.

Story: Unlike its proud gray cousin standing alone at the rune stones, this
elder white wolf has become a gentle teacher. On a misty winter dawn it is
surrounded by three tiny wolf pups (fluffy gray, fluffy brown, fluffy cream)
all learning their very first howl. One pup is on the elder's back, mouth
perfectly round trying to match the tone. Another is trying to copy the elder's
pose, head tilted up. The elder's head is raised, eyes closed, leading the
lesson with a soft patient smile. A frozen stream of breath rises from its
muzzle in the cold air.

Background: snow-covered forest clearing at dawn. Rune stones dusted with
frost. Soft pink-gold sunrise light. Pine trees heavy with snow. Fresh wolf
pawprints in the snow. Tender, teaching-moment atmosphere.""" },

  # 5. フロッガ+ — 画家デビュー
  'normal_plus_5': { 'frame': 'common', 'prompt': S + """Character: A coral-salmon orange frog creature — same round frog species as
the sky-blue original, but with a WARM CORAL-SALMON body and PEACH-ORANGE
throat pouch instead of blue. Large sparkling golden-orange eyes with
HORIZONTAL OVAL FROG-PUPIL highlights — focused and serious, not rapturous.

Story: This frog has outgrown singing and discovered a new passion — painting.
It sits in front of a tiny wooden easel on its lily pad, wearing a tilted black
beret and a paint-smudged smock, holding a fine brush in one webbed hand and a
small wooden palette in the other. A dragonfly sits patiently as a model on a
nearby cattail. The frog squints at the dragonfly with intense artist focus,
tongue sticking out in concentration. Its painting-in-progress shows a
surprisingly beautiful dragonfly portrait.

Background: same sunlit forest pond but now at golden hour. Lily pads with
paint jars, brushes, and crumpled paper sketches scattered on them. The
dragonfly model in a regal pose. A few butterflies watching the painter at
work. Warm peaceful artistic atmosphere.""" },

  # 6. チョコン+ — 空を飛ぼう大作戦
  'normal_plus_6': { 'frame': 'common', 'prompt': S + """Character: A vermillion-red baby chocobo chick — same round chick species as
the golden-yellow original, but with a VIVID VERMILLION-RED body and CRIMSON
head-tuft feather instead of yellow. Large sparkling ruby-red eyes with
MASSIVE INNOCENT ROUND highlights — eyes squeezed shut in determination.

Story: After learning to run yesterday, this red chick is now convinced it can
also FLY. It has climbed up onto a tiny mushroom stool at the edge of the
ranch fence and is mid-leap, tiny useless wings flapping at maximum speed with
eyes squeezed shut in total concentration. Its little legs are tucked up. Its
head-tuft feather is pointed straight back from the wind. What it doesn't know
is that it is falling about six inches down onto soft hay. A butterfly flutters
nearby, watching in surprise. Expression: pure determined hope.

Background: same pastoral ranch but at sunset. Golden-red sky with long
shadows. The wooden fence and red barn. Hay bales below the jump zone. Other
chocobo chicks watching from below with worried faces. A single feather floats
in the air. Heartwarming failure-in-progress atmosphere.""" },

  # 7. ドリアン+ — 冬至の霜わけ
  'normal_plus_7': { 'frame': 'uncommon', 'prompt': S + """Character: A frost silver-blue dryad creature — same round mossy species as
the original, but with a SILVERY FROST-BLUE body covered in delicate ice
crystals and PALE WINTER-WHITE vine hair instead of moss green. Large
sparkling pale blue eyes with LEAF-SHAPED highlights now formed from frosted
leaves.

Story: It is the winter solstice, the coldest night of the year. This frost
dryad sits on its ancient bare tree branch, completely covered in frost — but
it is using one of its own vine arms to gently wrap a tiny shivering robin in
a handmade scarf of woven icicles that magically keeps warmth inside. The
robin is nestled against its chest, warm and safe. The dryad's own body is
colder for it — tiny ice crystals forming on its cheeks — but its smile is
serene and selfless. A single tear of frozen starlight sits on one cheek.

Background: high up in a bare winter forest canopy. Snow falling gently. The
ancient tree silhouetted against a twilight sky full of stars. Other empty
bird nests dusted with snow. Soft aurora-like light in the distance. Quiet,
sacred winter atmosphere.""" },

  # 8. キツネビ+ — 吹雪の中の案内
  'normal_plus_8': { 'frame': 'common', 'prompt': S + """Character: A snow-white fox spirit — same round fox species as the amber
original, but with PURE SNOW-WHITE fur and PALE ICE-BLUE ear-tips and tail-tip
instead of amber/orange. Large sparkling pale-blue eyes with VERTICAL
FOXFIRE-FLAME highlights now glowing with cool white-blue light instead of
playful orange. No smirk — a gentle protective expression instead.

Story: A fierce blizzard is raging through the forest. A tiny human child
wearing a thick winter coat is lost and crying in the snow. This white fox
has found the child and is leading them safely to the warm inn, walking just
ahead with its bushy tail curled back toward the child like a guiding lantern.
Its tail-tip burns with pale blue foxfire, cutting through the snow-dark
forest. Three blue-white foxfire wisps float in formation, lighting the path.
The fox looks back over its shoulder with a reassuring expression: "This way.
Stay close." No mischief — only tender guardianship.

Background: heavy winter blizzard in the autumn forest turned white. Snow
swirling through the air. The red torii gate half-buried in snow. Warm
lantern light from a distant inn barely visible through the storm. Cold
white-blue atmosphere with warm rescue glow ahead.""" },

  # 9. キングモグ+ — 月夜の詩人王
  'normal_plus_9': { 'frame': 'rare', 'prompt': S + """Character: A deep midnight-indigo fairy king — same round tiny-king species
as the white original, but with a DEEP MIDNIGHT-INDIGO body and SILVER-WHITE
pompom and SILVER crown with a MOONSTONE gem instead of red/gold. Tiny
silver-trimmed wings. Large sparkling silver-blue eyes with CRESCENT-MOON
STAR highlights instead of royal red stars.

Story: The loud daytime courtroom is gone. Under the quiet moonlight, this
night-variant fairy king has set aside his gavel and taken up a tiny silver
quill. He sits on his tree-stump throne with a small floating candle lantern
beside him, writing poetry on a rolled parchment across his lap. His expression
is thoughtful and dreamy — a scholar-king contemplating the beauty of the
night. The fairy ring of mushrooms now glows with soft pale-blue moonlight
instead of golden fire. One tiny foot taps in quiet rhythm to the verse forming
in his mind.

Background: same enchanted clearing but transformed by moonlight. The mushroom
fairy ring glows pale silver-blue. Fireflies replaced by floating silver stars.
A beam of moonlight illuminates the king like a spotlight on a poet's stage.
Ancient tall trees silhouetted. A drowsy sleeping owl on a nearby branch.
Serene, contemplative midnight atmosphere.""" },
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
            Image.open(final_path).convert('RGB').resize((120,168), Image.LANCZOS).save(thumb_path, 'JPEG', quality=80)
            print(f'  Thumb: {thumb_path}')
        if i < len(targets) - 1:
            time.sleep(2)
    print(f'\nDone! Generated {len(targets)} cards.')

if __name__ == '__main__':
    main()
