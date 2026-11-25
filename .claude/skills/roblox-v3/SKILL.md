---
name: roblox-v3
description: Make Roblox 3D story reels/shorts (vertical, 60 s–3 min, first-person narration) in the reference look measured frame by frame: saturated sunny sets, real R6 avatars with custom expressive faces, characters walking and running, push-ins, shake, depth of field, fast ~1 s cuts, small lowercase captions with one red key word. Covers script, voice, captions, pacing, camera, lighting files, faces, movement and the Roblox Studio / Blender build. Use for ANY Roblox-look story video when the user asks for roblox v3 or the reference style.
---

# Roblox story reels (v3: reference look, 2026-11-16)

**Style = reference look** . Read `look-reference.md` FIRST. It was measured from every frame of 5 reference Shorts (34,398 frames, 660 shots; data in `your analysis folder`). **Where it disagrees with `style-toon.md`, `look.md`, `lighting-color.md`, `pacing.md` or `captions.md`, `look-reference.md` wins.** Lighting: `assets/lighting/reference/lighting-<family>.lua` (paste in the Studio command bar; starting values).
The older skill `roblox` (bright toon) stays as it was. Script shape: the `roblox-town-script` skill.

**v2.1 (2026-11-15):** read `studio.md` §8–9 first: the visible-rule story shape, grey blockout → world → light → R15 cast with real Roblox animations (`StepAnimations`) → one shot per second. **Build engine = Roblox Studio, driven by Claude (v4, the creator's call 2026-11-14)** with free Creator Store assets: read `studio.md` (picture quality, real R6 characters with clothes, hair fit, the no-clipping rule, physics). Blender (`blender.md`) is the fallback.

**Earlier build engine = Blender, free** (the creator's decision). `blender.md` replaces the Roblox Studio / Moon Animator / OBS build. Where a file still says Luau, `execute_luau`, `screen_capture`, Motor6D, `LightingStyle` or OBS, keep its intent and numbers and do it with the Blender kit.

The research behind the rules (`your analysis folder`, `team/*.md`) lives outside the skill; every number you need is inside these files.
Tags inside the files: **REF-RANGE** = measured on the refs · **HYPOTHESIS** = a beat-the-refs bet; keep it only if the user's analytics agree · **POLICY** = a platform or legal rule.
The refs are the floor. Every episode must also pass `upgrades.md` (≥10 of 14).

## Files
| file | use it for |
|---|---|
| `look-reference.md` | **the target style (v3)**: 6 look families with measured numbers, camera grammar, edit rhythm, faces, movement, captions, effects, never-do list |
| `assets/lighting/reference/` | one Studio command-bar lighting file per look family |
| `style-toon.md` | **the target style**: look numbers, sets, characters, the 24 faces and face rules, camera, captions, comedy script shape, audio, kit recipe, checks |
| `script.md` | world-rule formula and scoring, beat map by % for any 60–180 s runtime, twist families, sentence rules, **the pause rule** (§6), banned phrases, self-check |
| `look.md` | shot sizes, camera, faces and decals, posing, sets, how to show the rule on screen, ending shot |
| `lighting-color.md` | LightingStyle presets per mood, colour targets, twist palette shift, how to measure a capture |
| `audio.md` | ElevenLabs voice settings, pauses, character voices, music events, SFX, mix targets, library map, rotation |
| `pacing.md` | cut rules, shot lengths, holds, first 3 s / 10 s, pacing self-check script |
| `captions.md` | caption spec at 1080x1920, highlight rule, safe zones, `make_caps.py` (timestamps → captions) |
| `studio.md` | **the build (v4)**: Roblox Studio via its MCP, tiled 1080x1920 capture, real R6 + own clothes, hair at head scale, auto no-clipping, physics helpers; kit in `studio_kit/` |
| `blender.md` | **the fallback build**: Blender kit, hero, faces, poses, cameras, looks, render, free sets, shot checks |
| `SETUP.md` | one-time free install on the Mac (MCP for Blender, ffmpeg, alias) |
| `scripts/` `assets/` `shots/` | `rbxkit.py` (the kit), `faces.py` + `face_atlas.png` (24 faces, preview in `face_atlas_preview.jpg`), `example_toon.py` (toon-style template), `example_shot.py` (old moody look) |
| `pipeline.md` | episode folder, edit, export, disclosure, build budget. Its Roblox Studio / OBS build steps are replaced by `blender.md` |
| `upgrades.md` | the 14 upgrades over the refs + what to rotate every episode |
| `checklist.md` | QA rubric, /10 per area; anything under 8 gets fixed |
| `templates/` | script sheet, shot list, cue sheet, **rotation log** (every rotating field, one rule each), hero cast file, caption preset; `lighting-presets.lua` and `mcp-setup.md` are the old Roblox Studio route (reference only) |
| `examples/` | 2 gold scripts: a quality comparison **after** your first draft. Never open them before (they anchor: round 2 rebuilt gold-1 beat for beat) |
| `tools/` | zero-token Python: `script_check.py` (script numbers), `plan_timing.py` (sheet → planned words.json + cuts.txt), `shotlist_check.py`, `pacing_check.py`, `make_caps.py` (one-word captions), `make_caps_toon.py` (toon phrase captions), `move_check.py`, `measure.py` (colour), `assemble.py` (cut OBS takes, 60→30 fps); `sheetlib.py` is their shared parser; `patterns.txt` (voice and no-copy patterns), `skeletons.txt` (story skeletons + signature moves), `ref_lines.txt` (the refs' scripts) and `market_titles.txt` are their data (not included in this copy: `script_check.py` skips the no-copy check against ref lines when the file is missing) |
| `agents/` | the 8 research-team agents (copies of `.claude/agents/`), to rerun when new reference videos are added |
| `research/` (not included in this copy) | REPORT.md (10-bullet summary), GAPS.md (14 ways to beat the refs), TRAINING-LOG.md (3 rounds). Full data: `your analysis folder` |
| `first-test-prompt.md` | ready-to-paste prompt for the first 15 s test (written for the Roblox Studio route; adapt to `blender.md`) |

**What to read.** Planning an episode (script, shot list, cue sheet, caption plan): `script.md`, `templates/`, `checklist.md` [plan] items, the tools, `look.md` §0–3, §5, §6.1, §7.1, §9 and §16, `lighting-color.md` §1–5, all of `audio.md` (the cue sheet needs it), `pacing.md` §2–5, `captions.md` §1, and the build budget in `pipeline.md`. Paths outside the skill (`your project folder/…`, `team/…`) may not exist in your session: a log or cast file supplied in the brief replaces them. Building: `blender.md` (and `SETUP.md` once), then the rest of `look.md` and `lighting-color.md` for intent and numbers. Editing: `pipeline.md`.

**Fallbacks.** No Agent tool: the blind guess test is UNCHECKED; leave `pretwist.txt` for the orchestrating session or the user to read. No `humanizer` skill: do script.md §10 step 7's six-item pass by hand.

## Workflow (always in this order)
1. **Rule.** Write 5 one-sentence world rules and score each with the script.md rubric. Keep the best one that's outside the crowded "X is deadly" lane.
2. **Rotation.** Read the last 5 rows of `your project folder/projects/ROTATION-LOG.md` (fields and rules: `templates/rotation-log.md`). Twist family not in the last 5; reveal ≥10 points from the last episode. A field the log doesn't have yet is free: choose and log it.
3. **Script.** Rule, beat map, 10-slot skeleton and tone (script.md §0.2, §9.4), then the first draft, **all before opening `examples/`**. Only then compare with the golds for quality. Then the humanizer pass, `tools/plan_timing.py`, `tools/script_check.py` (with `--log` and `--pretwist`) and the blind guess test (script.md §3.3), in `templates/script-sheet.md`. **the user reads it and edits before any voice is generated or anything is built. Never skip his read.** A plan package may draft steps 5–6 on planned timing before his read; mark it "waiting on the user's read".
4. **Voice.** your ElevenLabs voice (or a free text-to-speech voice). **Ask before spending credits** (character count from `script_check.py`). Get word timestamps (Whisper/Parakeet), then set the designed pauses (script.md §6).
5. **Shot list + cue sheet + caption plan** from the timestamps (`templates/`). For a plan, use `plan_timing.py`'s planned words.json, then rebuild from the real one.
6. **QA the plan** with checklist.md: the plan score (a) must be ≥8 in every area, no HARD fail.
7. **Build** in Blender (`blender.md`): one shot .py per scene from the shot list and `words.json`; check framing with `-- draft still` renders first.
8. **Render** each scene on the Mac (`-- final`, PNG frames → ffmpeg mp4). Run a 15 s end-to-end test before the first full episode.
9. **Edit** (pipeline.md): cuts on sentence starts, captions from timestamps, music events, SFX, mix to −14 LUFS.
10. **QA the cut** with checklist.md: the strict score (b) must be ≥8 in every area. Then export. IG "AI info" label on when the narration is a TTS/clone. Update the episode's row in ROTATION-LOG.md.

## The 21 rules that matter most (reference look; numbers from look-reference.md)
1. The rule/premise is the first sentence, spoken at 0.0–0.2 s, 8–15 words, fully clear by about 9 % of runtime. (REF)
2. Reveal at 49–78 %, climax 69–96 %, last line at ≥92 %. No outro. (REF)
3. Rotate twist families. Never default to "secret sacrifice for a sick or dying relative". (POLICY + REF)
4. Banned outright: "for the first time", "I finally understood/knew", "Everyone thought…", emphasis-only fragments. (REF)
5. Short sentences: about 5–7 words, half of them 6 words or fewer. Every fragment adds a new fact. (REF)
6. Narration 185–240 wpm. Exactly 2–3 designed pauses (after the twist, before the last line). (REF)
7. Music changes with the story: calm bed → tension → big power/reveal hit. Duck ≥10 dB under quiet beats. (REF)
8. SFX on every action: whooshes on push-ins and runs, impacts with shake, a glow/rise sound on powers and flashes. (REF)
9. **Fast cuts:** median shot 0.9–1.1 s, 8–12 cuts per 10 s, nothing over 2.5 s except one designed hold. Cut on sentence starts. (the reference)
10. Rule/premise object in shot 1 and in ≥50 % of shots. **Big readable in-world signs** carry the facts (prices, names, "SIGN UP HERE"), text in the top third. (the reference)
11. **Faces:** real R6 avatars with custom faces: big white eyes with pupils, thick angled brows, open mouths with teeth, sweat. A new face on almost every shot; reaction faces 0.5–1 s. Characters fill the frame on close-ups. (the reference)
12. **Camera:** push in on about 40 % of shots (many are big 5–15 % punch-ins), static camera with a moving character on about 15 %, pull out on about 10 %, shake on about 25 % (impacts, runs, powers), roll on hits. Low angles, wide lens, **depth of field ON for close-ups** (soft background). (the reference)
13. **Lighting:** run `assets/lighting/reference/lighting-<family>.lua` for the scene's mood (mid-neutral-normal for normal life, mid-warm-vivid for golden/power, dark-neutral-vivid for blue tension, bright-warm-vivid for gold glory, dark-warm-vivid for lava/danger, bright-neutral-normal for heaven/flash). Video averages: brightness 0.34–0.43, saturation 0.42–0.66, near-pure blacks, slight vignette (~0.89). Bloom on gold, wings and powers. White flash frames on reveals. (the reference)
14. Custom hero with our own face decals. Never the noob or classic avatar (Creator Terms), no Roblox logo, Roblox audio muted. Never copy reference characters, outfits, names or stories. (POLICY)
15. **Captions:** 1–2 words at a time, lowercase, white, bold rounded sans, soft dark shadow, cap height about 50 px, centered at about 65 % of the height. One key word per sentence in ALL-CAPS red (about #e8452c). Mix: −14 LUFS, ≤ −1.0 dBTP, voice 6–10 dB over music. (the reference)

16. **Nothing passes through anything.** No arm inside a torso, no person inside another person, no body inside a wall, table, bed, lamp or tree, no prop sunk into a hand. Run the clip check on every shot (first, middle and last frame) before rendering; it must be empty or explained. (the user, 2026-11-14)
17. **Hair and hats never sink into or float off the head.** Scale the head the same on every axis and put accessories on their own attachment at the same scale. (the user, 2026-11-14)
18. **Real physics.** Thrown things arc and spin, dropped things fall and bounce, feet stay planted on the floor, walkers move at walking speed, nobody slides or floats. (the user, 2026-11-14)
19. **Sharp picture.** Native 1080x1920 frames (tiled capture), max quality level, never a stretched centre-crop. Compare one frame side by side with a ref before the full render. (the user, 2026-11-14)
20. **Characters look like real Roblox avatars:** R6 with real shirts and pants (collars, hoodies, prints, jeans, shoes), real hair accessories, crowd spacing ≥4.4 studs. Never plain coloured blocks. (the user, 2026-11-14)
21. **Characters move.** Something moves on its own in about 63 % of screen time; about a third of shots have someone walking or running (real R6 walk/run animations, big arm swings). Use: running straight at a low static camera until he fills the frame, walking across frame, entering and leaving frame, being grabbed, falling, flying. Feet stay on the ground with hard sun shadows. 

## Never
- Spend ElevenLabs/Higgsfield credits, buy plugins or assets, or use paid add-on features (MCP-for-Blender Premium, Meshy/Tripo/Rodin/World Labs) without the user's OK. Moon Animator is out: we animate in Blender.
- Copy a ref's story, music track, opener sound or avatar, or a line shape from the refs or golds (script.md §9.4).
- Use the refs' bad data fields as evidence (`shots.json` move labels, `audio.json` music_changes/sfx_hits).
- Hand the user a script that fails the script.md self-check (voice, logic and twist tests included), or count an unchecked item as a pass.

## Known mistakes (add here when a review note repeats)
- Never hand the user one still frame per shot with a camera zoom as "the video". Every shot must be animated in Blender (breathing, blinks, talking mouths, reactions, walks, camera move). Working pattern: `your project folder/shots/monster.py` (`animate()` + per-shot `@act` actions) and its `4 Render animation.command`. If time is short, say so before building, not after.
- Never render a centre 9:16 crop of a landscape Studio capture (about 590 px wide, then stretched). It looked blurry next to the refs. Use the tiled capture in `studio.md` §2.
- Never stretch the head unevenly (old 2.0×1.75×1.8 head). The hair sank into it. The head scales the same on every axis, and the hair uses the same k.
- Never pack people closer than R6 shoulders allow (2.6-stud crowd grid = bodies inside bodies). Use ≥4.4 studs, and let `MT.resolve` push the crowd out of the cast.
- Never build a character from plain boxes (box sleeves, box shoes, no clothes). the user: "my roblox guys are looking really bad".
- Never ship camera moves + face swaps on standing bodies (ep02 "no animation?", 2026-11-16). Our rigs are anchored parts (no Motor6Ds), so use the walk/run cycle in `your project folder/roblox/ep_anim.lua`: phase from distance travelled (feet planted, no sliding), legs ±40° walk / ±60° run, opposite arms ±44°/±72°, hip drop so the tilted leg stands on its edge. `ep_moves.lua` there shows idle life on every rig, talking hands, gestures, reactions, flailing, capes, walkers and moving bits for empty inserts. Check with analyze.py: ≥55 % of frames moving, no still shot.
- Studio can close mid-render (update or crash). Check `bridge.log` for "No studio available" and follow the recovery steps in `studio.md` §1.
