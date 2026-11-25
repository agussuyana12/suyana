# style-toon.md: the bright-toon style (the user's target look)

Decision (the user, 2026-11-14): **"I want exactly like that style… with those facial expressions too."**
This is the default style for every Roblox-look reel from now on. It replaces the moody look of the
first six refs (dark sets, bloom, fog, one-word captions).

Source: one reference reel he gave, "In this town, when you turn eighteen, you get cracked" (152 s,
720x1280). Its numbers are in `your analysis folder`. Every REF number below is measured
on that one video (n=1). GUESS = judged by eye or by a rough measure.

**Match the style, not the video.** Copy the look, the pacing, the caption system and the kind of
faces. Never copy its characters (the white-curly-hair kid with the cat tee, the purple-cap friend…),
its story, its jokes, its sign texts or its music. Our cast, our sets and our jokes are our own.

**Where this file disagrees with another file, this file wins:**
| other file says | in the toon style |
|---|---|
| lighting-color.md mood presets, bloom, fog, palette shift at the twist | bright even light all the way; mood comes from faces, poses, sound and the set (see §1) |
| look.md: rack focus / dolly-zoom on the twist, DOF on close-ups | no depth of field, no bloom, no fog; the twist is a hold + a face |
| captions.md: one word per caption, 104 px, pop | phrases of 2–4 words, small, ALL CAPS, one coloured key word (§6) |
| script.md pause rule (2–3 designed pauses) | 1 designed pause, before the reveal word (§7) |
| audio.md: SFX 2–5 per minute | more SFX, about 6–12 per minute (§8) |
Everything else in script.md, pacing.md, upgrades.md, checklist.md and blender.md still applies.

## 1. Look (REF, per-shot means)
| measure | this style | the six older refs |
|---|---|---|
| brightness (HSV V) | **0.66** (p10 0.52, p90 0.78) | 0.46–0.64 |
| saturation | **0.21** (p10 0.12, p90 0.34); 0 % of shots over 0.6 | 0.33–0.56 |
| contrast (grey std) | 0.25 | 0.21–0.23 |
| warmth (R−B) | +0.04 (neutral white) | −0.01 to +0.16 |
- **High key and pastel.** Big light surfaces (white ceilings, cream or mint walls, pale tiled floors), with small strong colour only on props and clothes (coral lamp, yellow and blue lockers, teal clinic trim).
- **Soft, short shadows.** A hint of contact shadow under things. No black anywhere: the darkest things are hair and black shirts.
- **No bloom, no fog, no depth of field, no lens effects.** Edges are clean and everything is in focus.
- **Smooth matte plastic** with rounded edges. No textures except printed graphics (a shirt print, a poster).
- **Night scenes stay readable:** a blue room with the same soft light, never a dark frame (bedroom shots).

Targets for our renders (`tools/measure.py` on caption-free stills): brightness 0.60–0.80, saturation 0.15–0.36, p99 ≥ 230, p1 ≥ 25.
The kit's `toon_day` look measured 0.65–0.81 / 0.21–0.37 / p99 237 on `shots/example_toon.py`.

## 2. Sets
- Everyday places, clean and a little empty: kitchen, school hall with lockers, cafeteria, bedroom, a shop front, a waiting room, a treatment room. One clear colour idea per place (school = cream + yellow/blue lockers; clinic = mint + teal).
- **Signs carry the jokes and the rule.** Posters, a calendar with a circled date, a form with tick boxes, a business card, a shop sign. Short, big, readable in under a second. About 10 % of shots are inserts of a sign or prop, some full-screen (the form, the card, the calendar). (REF: ~10 of 99 shots.)
- Checker or tile floors, drop ceilings with light panels, a colour band or trim on the walls.
- Build with `k.toon_room()`, `k.sign()`, `k.text()`, `k.checker_mat()`, `k.PASTEL` (§9), then dress with free CC0 models.

## 3. Characters
- Blocky body, big head, **chunky sculpted hair** (curls, long straight hair with bangs, a bob, a cap). Hair is each character's silhouette.
- One loud, simple outfit per character, the same every episode: a coloured top or a shirt with one print, plain trousers. Each character owns one colour.
- Skin tones vary across the cast. Sleeveless arms show skin; hands are blocks.
- Kit: `k.make_hero(..., hair_style="fluffy" | "long" | "bob" | "spiky" | "block", sleeves=False)`.
- Our hero keeps his own locked design (pipeline.md / `templates/hero-cast.md`). Never rebuild the ref's cast.

## 4. Faces: the heart of this style
Flat 2D faces drawn in thick black ink: dot eyes, ring eyes, arcs, and red open mouths. The face
changes on almost every beat, and the same character shows 10+ different faces in one video (REF: the
hero shows about 14).

**The 24 faces in the kit** (`k.set_face(rig, frame, name)`; drawn by `scripts/faces.py`):
| feeling | face | feeling | face |
|---|---|---|---|
| normal, listening | `neutral` | relief, bliss | `content` |
| friendly | `smile` | proud, teasing | `smirk`, `wink` |
| joy | `happy`, `laugh` | cute, charming | `sparkle`, `sparkle_oh` |
| surprise | `oh` → `shocked` | thinking, confused | `nerd` (glasses, eyes up) |
| fear, panic | `scared` (teeth), `stare` | bracing for pain | `squeeze` (>_<) |
| worry | `nervous` (zigzag mouth + sweat) | knocked silly | `dizzy` (swirl eyes) |
| unimpressed, tired | `sleepy` | anger, shouting | `angry` |
| sadness | `sad`, `cry` | speaking | `talk` |
| blink | `blink` | horror only | `creepy` |
Aliases: `panic` = scared, `surprised` = shocked, `unimpressed` = sleepy, `relieved` = content, `glasses` = nerd, `brace` = squeeze.

**Face rules**
1. **A new face on every shot a character is in**, and on every punchline word (±3 frames). Two shots in a row with the same face on the same character is a miss.
2. **Escalate in steps:** `neutral` → `oh` → `shocked` → `scared`. Don't jump to the biggest face first.
3. **Hold the reaction.** After a joke lands, cut to a close-up of the listener's face and hold it 0.7–1.5 s. The reaction shot is the laugh.
4. **Opposite faces in a two-shot:** one calm (`smile`, `sparkle`, `sleepy`), one losing it (`shocked`, `nervous`). The gap is the comedy.
5. `talk` mouth flaps only on quoted lines on camera, 3–4 frames per shape, and return to the feeling face, not to `neutral`.
6. Blink every 3–4 s on long holds (`k.blink`), never on a punchline word.
7. Need a face that isn't there? Add it to `faces.py` at the END of the list (a new row), re-run it, add the name to `FACES` in `rbxkit.py`. Never reorder.

## 5. Camera and pacing (REF unless marked)
- 99 shots in 152 s: **mean 1.53 s, median 1.37 s, 39 cuts per minute.** One shot over 3.5 s (4.5 s).
- **Close shots about 44 %** (GUESS, hand count of 87 shots): the face fills 50–70 % of the frame width, seen from the front or just off it, with a wide lens close to the face and the camera a little below the eyes. Kit: `k.face_cam(name, rig, dist=3.8, lens=32)`.
- Medium two-shots and wides place people in the set; an insert of a sign or prop about every 10 shots.
- Most shots drift or push in slowly (GUESS). No shake, no whip pans, no spins.
- Cut on sentence starts (pacing.md). In dialogue, cut to whoever speaks, then to the listener's face.
- Top-down or tilted angles only when the story puts someone on their back or on the floor.

## 6. Captions
### 6.1 Spec (REF, scaled to 1080x1920)
| item | value |
|---|---|
| chunk | **a phrase of 2–4 words** (about 2.9 on average, 1.1 captions per second). Breaks at commas, full stops and breaths |
| case and font | ALL CAPS, heavy rounded geometric sans: **Poppins ExtraBold** (free), fallback Montserrat ExtraBold. Tight letter spacing |
| size | about **56 px** (text block about 50 px tall with its outline). Median width 42 % of the frame, never over 83 % |
| position | centred, **70.7 % down** (y 1357) |
| colour | white, black outline about 6 px, small soft shadow |
| key word | **one coloured word or name per phrase, in about half of the phrases** (REF: colour in 59 % of caption frames) |
| animation | fades in over 2 frames. No pop, no bounce, no word-by-word. Goes away in pauses |
### 6.2 Colour rule
| colour | hex | use for |
|---|---|---|
| red | `#DB5D5E` | the rule word, danger, pain, shouting ("CRACKED", "WAIT", "FIGHT") |
| yellow | `#EAD95B` | names, times, numbers, the key object of the line ("EIGHTEEN", "SATURDAY", a friend's name) |
| blue | `#75C8E2` | calm or neutral things ("WATER", "TOWEL", "SILENCE") |
Never colour function words. The rule word is always red, every time it appears.
### 6.3 Make them
`python3 tools/make_caps_toon.py words.json caps.ass --red "…" --yellow "…" --blue "…"`
(phrases, colours, fade and position are built in; it prints captions per second and the colour share).
In Studio Preview, the built-in captions with `maxWords: 3` are close enough for review; the .ass file is for the export.

## 7. Script: comedy by misdirection
This style is funny first. The ref runs one joke for 150 s: a scary-sounding rule that turns out to be
harmless.
- **REF numbers:** 468 words, 150.6 s, **186 wpm**. 96 sentences, **mean 4.9 words**, 78 % are 6 words or fewer, 30 % are 3 or fewer. About a third of the lines are spoken dialogue (GUESS).
- **The rule** is the first sentence, done by 3.4 s, and it hides one word with two meanings. The audience guesses the scary meaning.
- **Nobody explains** (0–9 s): "Nobody tells you how." Everyone who knows acts like asking is weird.
- **Three witnesses, each worse** (9–40 s): best friend, mom, a girl at school. Each gives one short, useless, worrying answer ("Drink water beforehand." "Louder than I expected.").
- **The kit** (40–48 s): a friend hands over odd objects (water, a towel, a stress ball). Each one must pay off later.
- **The place and the people** (48–96 s): every detail looks worse than it is (blacked-out windows, a form asking "gentle or firm?", a yell from the next room, then silence).
- **The moment** at about 72 %: the thing happens, and it's fine. Relief beat, the body feels great.
- **The reveal word** at about 80 %: a name or sign shows the innocent meaning. The only real pause in the voice (0.56 s) sits right before it.
- **Tag jokes** (82–99 %): pay off each planted object and each witness, then one more turn in the last 10 s, and end on a side character's one-liner. The last line starts at 98.6 %.
- **Rules for us:** every setup pays off (objects, witnesses, signs); no joke is explained; the narrator is the scared one and everyone else is calm; keep it clean, the misread is the audience's own idea. Pick our own double-meaning rule; never reuse "cracked" or a chiropractor.
- script.md still governs the rule rubric, beat windows, banned phrases, the no-copy check and the user's voice. Log tone = funny in the rotation log.

## 8. Audio (REF unless marked)
- Mix −14.2 LUFS; voice −15.8, bed −22.1, so **voice sits 6.3 dB over the bed**.
- One light, bouncy bed the whole way (about 152 bpm, GUESS: quirky and upbeat). It **dips 10 dB or more twice**: on the line "Then silence" (73–74 s) and right after the big moment (112 s). Use that: duck the music on the two quietest beats, never change the track.
- **SFX: about 31 hits, 12 per minute** (GUESS: some may be music accents; verified range for us 6–12 per minute). Only 29 % land on cuts; most land on actions and words (the crack, a door, a button, footsteps, a pop on a sign).
- Voices: every character has their own voice (pitch medians: narrator about 150–190 Hz, girls and mom 205–260 Hz, the big man about 105–140 Hz). GUESS: text-to-speech voices. For us: the user's clone narrates; side characters get separate designed voices (audio.md, pitch shift ≤ +10 st). **Ask before spending ElevenLabs credits.**
- One voice pause ≥ 0.5 s in the whole video: before the reveal word.

## 9. Build it in the kit
```python
import rbxkit as k
P = k.PASTEL
k.clean_scene()
k.toon_room(w=20, d=12, h=9, wall=P["cream"], floor=(P["tile_a"], P["tile_b"]), band=P["teal"])
k.apply_look("toon_day", subject=(0, 1, 3))        # also: toon_warm (kitchen), toon_cool (clinic), toon_night
k.sign("notice", ["TODAY:", "PIZZA DAY", "(again)"], (6.6, 5.7, 5.6), w=3.6, h=2.4,
       colors=[P["charcoal"], P["coral"], P["grey"]])
hero = k.make_hero("Hero", at=(-1.2, 1, 0), facing=-18, shirt=P["coral"], hair_style="fluffy", sleeves=False)
k.set_face(hero, 1, "smile"); k.recoil(hero, 46, face="shocked"); k.set_face(hero, 92, "nervous")
cu = k.face_cam("cam_hero", hero, dist=3.8, lens=32)   # the toon close-up
```
Full working shot: `shots/example_toon.py` (`blender -b -P shots/example_toon.py -- draft still`).
Never call `_bloom()`, fog, or a `dof_target` in this style. Old looks (`warm_interior`, `night_horror`…) stay in the kit for horror episodes only.

## 10. Checks before a shot goes to the user
- Brightness 0.60–0.80 and saturation 0.15–0.36 on stills (`tools/measure.py`). Nothing darker than hair.
- Every shot with a character: a different face from that character's last shot.
- Close shots ≥ 40 % of the shot list; an insert at least every 10 shots; a sign or prop that tells a joke in every location.
- No shot over 3.5 s except one designed hold. Mean shot 1.3–1.8 s.
- Captions: 2–4 words, ALL CAPS, one coloured key word in 40–60 % of phrases, the rule word always red.
- No character, joke, sign text or music taken from the ref.

## 11. Our own spin (be creative, keep the style)
The style is the frame; what goes in it is ours.
- **A background gag per location** that changes each time we come back (the sign's small print, a clock, a poster).
- **A signature object per character**, like a colour, that shows up in their captions (their name in yellow) and their scenes.
- **New faces when a story needs them:** draw them in the same ink language and add them to the atlas (§4 rule 7).
- **Burmese touches** in sets and names when the user wants them: his channel, his world.
