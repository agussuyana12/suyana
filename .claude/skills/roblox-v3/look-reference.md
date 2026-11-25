# reference look: STYLE.md

Measured from 5 Shorts (34,398 frames, 660 shots): The Last Guardian (4.3M), I got the Weakest Power (2.8M), Forbidden Prison Pt 2 (844K), The Boy Who Was Sold for 100 Gold (172K), He Knew My Name (151K).
All numbers are REF-RANGE unless marked. Sample frames: `_summary/family_<name>.png`. Every shot: `<video>/sheet_XX.jpg`.

## 1. The look in one paragraph
Bright, saturated, sunny Roblox with real movie-camera habits. Real R6 avatars in real clothes with custom, very expressive faces. Hard sun shadows, blue skies, gold and fire-red fantasy sets, and blurred backgrounds on close-ups. The camera lives close and low, pushes in on almost half the shots and shakes on impacts. Characters keep moving: walking, running at the camera, entering and leaving frame. Cuts are fast (about 1 per second). Captions are small, white, lowercase, 1–2 words, with one red ALL-CAPS key word.

## 2. Look families (use the matching lighting file)
| family | used for | share of time | brightness | contrast | black pt | white pt | saturation | shadow | mid | highlight | shadow warmth | highlight warmth | vignette |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mid-neutral-normal | daylight indoors (office, house, school), normal life | 28% | 0.495 | 0.326 | 0.007 | 0.969 | 0.333 | #0b0b17 | #919397 | #f8f3e4 | -12.6 | +20.2 | 1.08 |
| mid-warm-vivid | golden hour, desert, fire-lit, "power" moments | 28% | 0.326 | 0.294 | 0.004 | 0.924 | 0.706 | #0a0303 | #855623 | #f4e58f | +7.5 | +101.7 | high (bright center glow) |
| dark-neutral-vivid | blue dusk / night / dim halls, tension | 27% | 0.298 | 0.264 | 0.003 | 0.888 | 0.581 | #050517 | #515367 | #d9d9d0 | -18.2 | +9.6 | 1.32 |
| bright-warm-vivid | gold palace, kings, rewards, glory | 10% | 0.621 | 0.245 | 0.086 | 0.940 | 0.634 | #672f14 | #d6a956 | #fbf0b9 | +83.0 | +65.8 | 0.91 |
| dark-warm-vivid | lava, hell, villain throne, danger | 5% | 0.096 | 0.115 | 0.003 | 0.495 | 0.694 | #050101 | #3f1010 | #af5742 | +3.3 | +109.8 | 0.66 |
| bright-neutral-normal | heaven light, white flashes, power reveals | 2% | 0.715 | 0.182 | 0.263 | 0.962 | 0.208 | #59667e | #b6bdc0 | #f3f1e1 | -37.2 | +17.6 | 0.89 |

Palettes: mid-neutral #ebece1 #03040b #9eb4d1 #6b6580 #302952 #e1a64b · mid-warm #140705 #532212 #f7db3c #b93b0a #e4e4b1 #b48b57 · dark-neutral #130c18 #58596f #78aae1 #e9d5ad #09248a #c45b24 · bright-warm #f5e0ae #f8d14c #e09b31 #431707 #9b4a1d #c3a685 · dark-warm #0e0104 #380e10 #6b0f07 #66565e #ca240a #d9bb84 · bright-neutral #eef1f0 #8f837f #bdc5cf #4a4856 #4f9dea #eddd72

Whole videos: brightness 0.34–0.43, saturation 0.42–0.66 (much more saturated than our toon look's 0.15–0.36). Median vignette 0.89 (slightly dark corners). Blacks almost pure black (p1 ≈ 0.003–0.007) except the bright families.

## 3. Camera grammar
- Shot moves (660 shots): push in 41%, static 23%, static camera while the character moves 15%, pull out 10%, shake as the main move 6%. Shake appears on 26% of all shots (impacts, running, power moments). Roll on 6% (hits, falls).
- Push-ins are real: median +0.9% per shot, but the average push is 8.6%, so many shots have a big punch-in.
- Low angles close to the character, wide lens feel. Characters fill the frame on close-ups.
- **Depth of field ON for close-ups:** background trees, walls and crowds are soft.
- Big readable in-world signs carry facts ("100,000,000 GOLD", "SIGN UP HERE", "THE GRAND COMPETITION").

## 4. Edit rhythm
- Median shot 0.93 s, average 1.04 s. 8–12.5 cuts per 10 s (the 2.8M video is fastest: 0.67 s median).
- White/black flash frames on power and impact moments (148 in Forbidden Prison, 108 in The Last Guardian).
- First 3 s: rule/premise line with a big set (palace, lava throne) and fast cuts; see `<video>/hook_sheet.jpg`.

## 5. Characters and faces
- Real R6 Roblox avatars with real clothing. The hero of 4 videos: black suit, cyan shirt, black tie, black messy hair.
- Custom faces, not default decals: big white eyes with black pupils, thick angled brows, open mouths with teeth, sweat drops. A new face on almost every shot.
- Fantasy characters: long white anime hair, gold armor, wings, glowing marks, villains in red/black.
- Crowds fill stadiums and streets.

## 6. Movement (characters don't just stand)
- 63% of screen time has something moving on its own. 221 shots (33%) have sustained walking or running, 213 (32%) short bursts, 226 (34%) are still.
- Classic Roblox R6 walk and run animations with big arm and leg swings.
- Signature shot: character runs straight at a low static camera until he fills the frame (see `reference-3-last-guardian/motion/s019_strip.jpg`).
- Characters walk across frame, enter and leave frame, get grabbed or pushed, fall, fly. Feet stay on the ground with hard sun shadows under them.

## 7. Captions
- 1–2 words at a time, lowercase, white, bold rounded sans, soft dark shadow (no thick outline).
- Cap height about 50 px at 1080x1920 (about 2.7% of height), centered at about 65% of the height.
- One key word per sentence in ALL CAPS red (about #e8452c): KILLER, GUARDIAN, INCH.

## 8. Effects
- Bloom/glow on gold, wings, powers. Fire and lava glow. White flashes on reveals.
- Screen shake on impacts and runs. Roll on hits.
- Slight vignette. No grain.

## 9. Never do
- Grey, low-saturation scenes for normal life (that's our old toon look, not theirs).
- Long static holds: almost nothing lasts over 2.5 s.
- Plain block characters or default faces.
- ALL-CAPS captions for every word.

## Status
Lighting files in `lighting-<family>.lua` are STARTING values from these numbers. They still need the Step 7 match test in Roblox Studio (`compare.py` against `_summary/family_<family>.png`).
