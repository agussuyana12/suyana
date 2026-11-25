# blender.md: build, animate and render in Blender (replaces Roblox Studio + Moon Animator)

Decision (the user, 2026-11-14): **we build in Blender, free.** No Moon Animator, no Roblox Studio
shot runner, no OBS recording. This file replaces workflow steps 7 (Build) and 8 (Record) in
SKILL.md. Script, voice, audio, captions, pacing, upgrades and QA rules stay exactly as written
in the other files: they don't care which engine made the picture.

Where other files still talk Roblox Studio (Luau, `execute_luau`, `screen_capture`, Motor6D,
`LightingStyle`, FieldOfView, OBS), read them for the **intent and the numbers** and do it with
the Blender kit below. The banner at the top of each of those files says the same.

**Money:** everything here is free. Never use MCP-for-Blender Premium, Meshy, Tripo, Rodin,
Hunyuan, World Labs, paid asset packs or any credits without asking the user first.
**Tokens:** renders run on the user's Mac. Claude only looks at draft stills for framing checks.

## Files
```
scripts/rbxkit.py        the kit: hero rig, faces, poses, walk, talk, cameras, looks, render
scripts/faces.py         redraws assets/face_atlas.png (needs Pillow)
assets/face_atlas.png    12 expressions in a 4x3 grid, sharp lines
shots/example_toon.py    5 s toon-style test: hallway, sign, 2 characters, 3 cameras (copy THIS as a template)
shots/example_shot.py    4 s test in the old moody look
SETUP.md                 one-time install on the Mac (all free)
```
Blender command on the Mac: `/Applications/Blender.app/Contents/MacOS/Blender`
(SETUP.md adds the alias `blender`).

## 1. Look rules in Blender terms
- **Hero**: `k.make_hero(name, at, facing, skin, shirt, pants, shoes, hair, hair_style, sleeves)`.
  Blocky R6-style body, our own design. Never the classic/"noob" colours (yellow head, blue
  torso, green legs), no Roblox logo, no copied ref avatars. Lock each character's colours +
  hair once and reuse them every episode.
- **Faces** (style-toon.md §4): `k.set_face(rig, frame, "shocked")` hard-cuts the decal. Atlas of 24:
  neutral happy sad cry angry shocked scared sleepy talk smirk blink creepy smile laugh nervous
  dizzy squeeze wink oh content sparkle sparkle_oh nerd stare (aliases: panic, surprised,
  unimpressed, relieved, glasses, brace). Preview: `assets/face_atlas_preview.jpg`. New faces go
  at the END of `faces.py` and of `FACES` in `rbxkit.py` (never reorder), then re-run `faces.py`.
- **Face timing** (look.md §7.2): swap on the key word ±3 frames; hold ≥0.5 s;
  `k.blink()` = 3 frames, every 3–4 s, never on a key word; `k.talk()` mouth flaps **only**
  for quoted lines spoken on camera, never under narration.
- **Body** (look.md §8): never frozen. `k.idle()` on everyone not acting; `k.hold()` named
  poses; posed/animated on ≥35 % of shots. The ref "starter pose library" maps to:
  point → `point`, hand-to-face → `facepalm` / `think`, head-drop slump → `sad`,
  flinch → `k.recoil()`, hug/hold → `hug_self` / `reach`, hands-on-head → `hands_up`
  (lower arms a bit), kneel → `sit` + `k.move(lift=-…)`. Add new ones to `POSES`.
- **Lighting**: toon style = `k.apply_look("toon_day" | "toon_warm" | "toon_cool" | "toon_night", subject)`
  (soft sun + bright ambient, Standard colour, no fog, no bloom; targets in style-toon.md §1).
  Check stills with `tools/measure.py`. The old moody presets `warm_interior`, `school_day`,
  `night_horror`, `dreamy_train`, `sad_rain` (3-point + fog + AgX + bloom) are for horror episodes only.
- **Toon close-up**: `k.face_cam(name, rig, dist=3.8, lens=32)` puts a wide lens right in front of a face.
- **Camera** (look.md, pacing.md): real moves on ≥70 % of shots: `k.push_in()`,
  `k.handheld()`; rack focus with `dof_target` + keyed `cam.data.dof.focus_distance`;
  dolly-zoom = `push_in(..., lens_to=…)` going back while the lens zooms in.
  Lens: Roblox vertical FOV 30–40° CU ≈ 60–75 mm here, 40–55° MS ≈ 45–60 mm, 55–70° WS ≈ 30–40 mm
  (at 1080x1920, 36 mm sensor; check one still).
- **Several cameras in one scene**: `k.cut_to(cam, frame)`. Cut on sentence starts, leading the
  first word by 0–2 frames (pacing.md) — take frames from `words.json`.
- Vertical 1080x1920, 30 fps.

### Body angle controls (same meaning on both sides)
- arms/legs `(forward, across, out)`: forward + = to the front, across + = in toward the chest,
  out + = up to the side
- head/torso `(nod, turn, tilt)`: nod + = look down / lean forward, turn + = its left,
  tilt + = its right
- facing 0 = looks toward -Y. Put cameras on the -Y side.

## 2. Build an episode (replaces SKILL.md steps 7–8)
Episode folder as in pipeline.md: `your project folder/projects/<episode>/`, plus
`shots/` (one .py per scene), `renders/<scene>/` (PNG frames), `blend/` (saved .blend files).

1. One Python file per scene, data from the shot list + `words.json`:
   ```python
   import os, sys
   sys.path.insert(0, os.path.expanduser(
       "skills/roblox/scripts"))
   import rbxkit as k
   FPS = 30
   def f(sec): return round(sec * FPS) + 1      # word time (s) -> frame
   k.clean_scene()
   ```
   Then: set (`k.room()` or `k.import_model()`), `k.apply_look()`, `k.make_hero()`, acting,
   cameras, `k.cut_to()`, `k.render_setup(out, start, end, quality)`, `k.save(blend_path)`.
   Copy `shots/example_shot.py`.
2. Framing check: `blender -b -P shot.py -- draft still` (3 stills, fast). Claude looks at
   those, nothing more.
3. the user can open the .blend and nudge keys by hand (Graph Editor / Dope Sheet). **If a .blend
   is newer than its .py, ask before re-running the .py** — it would wipe his edits.
4. Final: `blender -b -P shot.py -- final` → PNG frames (stops and resumes safely) →
   `ffmpeg -framerate 30 -i renders/<scene>/%04d.png -c:v libx264 -crf 16 -pix_fmt yuv420p <scene>.mp4`.
   Long renders: `caffeinate -ims`.
5. Edit exactly as pipeline.md says (sound, captions with `tools/make_caps.py`, music events,
   SFX, −14 LUFS). No slate-cutting is needed: each scene renders to its own exact length,
   so `tools/assemble.py`'s OBS slate step is skipped.

## 3. Sets and props (free only)
- Poly Haven (CC0, no credit needed): HDRIs, textures, models. Via MCP for Blender (tick Poly
  Haven in the sidebar) or download .blend/.glb by hand.
- Kenney.nl packs (CC0): furniture, interiors, city — already blocky.
- Poly Pizza (free key) and Sketchfab free downloads: CC0/CC-BY only; credits go in
  `your project folder/projects/<episode>/CREDITS.md` and the video description.
- Optional, free: Roblox Studio → Creator Store model → right-click → Export Selection (.obj/.fbx)
  → `k.import_model()`. Set pieces only; never avatars or logos. Delete any scripts — Blender
  ignores them anyway.
- Keep downloads in `your project folder/assets/<source>/`.

## 4. Claude driving Blender live (optional)
MCP for Blender (SETUP.md) lets Claude Code look at the open scene, run Blender Python and pull
Poly Haven assets. Use it for set dressing and framing. Keep acting and cameras in the shot .py
files so every shot can be rebuilt.

## 5. Checks before a shot goes to the user
- No character still for more than ~1 s (idle / blink / breath).
- Face swaps land on the beat word ±3 frames.
- A camera move or a cut at least every 2.3 s (pacing.md limits win if they differ).
- Close-ups: head ≥25 % of frame width; faces readable at phone size.
- Final quality (no draft %), motion blur on, lines sharp.
- No Roblox logo, no classic avatar, no copied characters; CREDITS.md updated.

## 6. Kit reference
| call | does |
|---|---|
| `make_hero(...)` | rigged character, returns the rig. `hair_style`: block, spiky, fluffy (curls), long, bob, none |
| `set_face(rig, f, name)` / `blink(rig, f)` / `talk(rig, a, b, base, rate)` | faces |
| `pose(rig, f, arm_R=(85,0,0), head=(10,0,0))` / `hold(rig, f, "think")` | key bones / named pose |
| named poses | rest arms_out point wave think facepalm hug_self shrug hands_up sad sit run_ready cover_face reach |
| `idle(rig, a, b)` / `shake(rig, a, b, bone, amp)` / `recoil(rig, f, face)` | breathing / crying-shiver / jump-scare |
| `walk(rig, a, b, to=(x,y,0), run=False)` / `turn_to(rig, f, deg)` / `move(rig, f, loc, turn, lift)` | travel |
| `camera(name, loc, look_at, lens, dof_target, fstop)` / `face_cam(name, rig, dist, height, side, lens)` / `push_in()` / `handheld()` / `cut_to()` | cameras |
| `apply_look(name, subject)` / `light()` / `world()` | lighting |
| `toon_room(w, d, h, wall, floor, band)` / `sign(name, lines, loc, w, h, colors, sizes)` / `text()` / `checker_mat()` / `PASTEL` | toon sets: tiled floor, trim, drop ceiling, readable signs, pastel colours |
| `room()` / `import_model(path, loc, scale, rot_z)` / `box()` / `mat()` | sets |
| `render_setup(out, start, end, quality, engine)` / `save(path)` | render (EEVEE default; CYCLES on Metal GPU) |

Tested on Blender 5.2 LTS (walk, poses, faces, cuts, looks, draft stills). Works on 4.2+.
