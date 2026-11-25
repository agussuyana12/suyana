# pipeline.md: one Roblox story reel on the user's Mac, cheapest path

> **v2 note (2026-11-14):** the build is now Blender — see `blender.md`. Steps 0.1–0.2, the shot runner, OBS recording, Luau appendix and Moon Animator here are the old Roblox Studio route, kept for reference only. Episode folder, edit, export, disclosure and budget sections still apply.


Who: the user, solo, Apple Silicon Mac, Claude Code in Terminal, $40/month total for tools (ElevenLabs already takes most of it), prefers free assets over building.
Output: vertical 1080×1920, 30 fps, 60 s–3 min, "In this world…" story in the Roblox 3D style.
Tags: **REF-RANGE** = measured in the 6 refs; **HYPOTHESIS** = not proven; **ESTIMATE** = time guess, replace with real numbers after the first test; **UNVERIFIED** = a tool behaviour nobody has checked yet on his Mac.

**Money rules (HARD):** never spend money or paid credits without asking the user first (ElevenLabs generations, Moon Animator, CapCut Pro, any asset). Stop if credits run out.
**Token rules:** Roblox renders and measuring scripts run on the Mac for free. `screen_capture` sends images to Claude, so use it for framing checks (about 10–20 per episode), never for measuring or for frame-by-frame rendering. Write the shot runner once; per episode Claude only writes scene data.

Episode folder: `your project folder/projects/<episode>/` with `script.md`, `audio/vo.wav`, `words.json`, `shotlist.md`, `cue-sheet.md`, `scenes/` (scene data), `takes/` (OBS), `stills/`, `edit/`, `QA.md`.

---

## The idea in one line
Claude builds and lights the sets through the Roblox Studio MCP, a **shot runner** plays each scene in real time inside Studio (cuts, camera moves, face swaps and poses all timed from the voice's word timestamps, each scene starting on a 1-second white slate), OBS records it, and a script cuts the takes at the slates. **Roblox does the picture cut live**, so the "edit" is mostly sound and captions.
The live cut is HYPOTHESIS until the first test (§ First test) shows no dropped frames and cuts within 1 frame of plan.

---

## Step 0. One-time setup (ESTIMATE 5–8 h, mostly the face kit and the hero)

### 0.1 Roblox Studio (free)
- Install from the Creator Dashboard. Activity Monitor → Studio must show **Kind: Apple**. If it says Intel, reinstall from the dashboard.
- File → Studio Settings → Rendering: **Editor Quality Level 21**, **Mesh Detail Level00**.
- Make one place file per episode type (or one per set library: school, house, street, vehicle). Save with `save_place`.

### 0.2 Roblox Studio built-in MCP → local Claude Code
Exact steps and 3 test prompts: `templates/mcp-setup.md`. Summary:
- It is **built into Studio**; transport is **stdio**, so Claude Code must run **on the same Mac** (Terminal CLI or the desktop app's Code tab), never a cloud session.
- Studio: Assistant → … → Manage MCP Servers → **Enable Studio as MCP server**; Assistant Settings → MCP Servers → **Quick connect → Claude Code**. Fallback: `claude mcp add --transport stdio --scope user Roblox_Studio -- /Applications/RobloxStudio.app/Contents/MacOS/StudioMCP`. Restart Studio and Claude Code; check `claude mcp list`.

| it CAN (30 tools) | it CANNOT |
|---|---|
| `search_asset` + `insert_asset` (Creator Store models, meshes, images, audio, animations by ID) | record video (no recording tool at all) |
| `execute_luau` in Edit, Client or Server (build, light, pose, swap decals, run the shot runner during Play) | make R6 animation: `generate_animation` is **R15 only, max 10 s** (text prompt or R6→R15 conversion) |
| `screen_capture` with an optional camera position and look-at target (framing stills) | author Moon Animator files |
| `search_game_tree`, `inspect_instance`, `script_read`, `multi_edit`, `script_search`, `script_grep` | control OBS |
| `start_stop_play`, `get_console_output`, `get_studio_state`, `save_place`, `list_roblox_studios` (every call needs its `studio_id`) | |
| `upload_image` / `store_image` (face PNGs), `generate_mesh`, `generate_material`, `generate_procedural_model`, `generate_avatar`, `wait_job_finished` (quotas UNVERIFIED) | |
| `character_navigation`, `user_keyboard_input`, `user_mouse_input`, `http_get`, `skill`, `subagent`, `submit_feedback` | |

### 0.3 OBS (free)
| setting | value | tag |
|---|---|---|
| Source | macOS Screen Capture → Window → Roblox Studio; crop to the emulated device area (Alt-drag or a Crop filter); cursor off | |
| Studio viewport | Test tab → Device → custom device **1080×1920 portrait** | |
| Canvas / Output | **1080×1920** | |
| FPS | **60** (blended to 30 later) | HYPOTHESIS: a 2-frame blend fakes the motion blur Roblox lacks; test blend vs no blend in the first test |
| Encoder | Apple VT H.264 hardware (or HEVC), CBR **40,000 kbps** | Roblox staff tip says ≥20,000; 40,000 is headroom (HYPOTHESIS) |
| Format | MKV (then File → Remux Recordings to MP4/MOV) or a crash-safe MP4 option if your OBS has one | Roblox staff tip |
| Audio | **delete every audio source**: Roblox audio never reaches the file (Roblox licensed music is barred off-platform; all sound is added in the edit) | HARD |

**Check the real pixel size once** (UNVERIFIED): a MacBook screen is about 1964 physical pixels tall, so after Studio's ribbon the viewport may be only about 1700 px tall. Then the 9:16 area is about 956×1700 and gets upscaled 1.13× to 1080×1920 (slightly soft). Fixes, cheapest first: close Studio panels and use full screen; an external monitor (a 4K screen in portrait is ideal); or accept ≤1.15× upscale and keep edit zooms ≤ +5 % (look.md §3.2).

### 0.4 Free sets (Creator Store) and the script strip
- Claude: `search_asset` → pick → `insert_asset` → run the cleanup in mcp-setup.md test A: **destroy every Script, LocalScript and ModuleScript inside inserted models** (free models can carry backdoors), remove Sound objects, then `P.cleanFreeModelFx()`.
- Not the shared free school map (blue-locker hallway + bulletin-board classroom; look.md §9). Redress every map with 2–3 story props.

### 0.5 Cast: hero rig + own face decals
- R6 rig (Avatar → Rig Builder → R6, or Luau). **Never the default noob or any Classic Avatar** (Roblox Creator Terms bar Classic Avatars in off-platform "motion picture" use; critic §4d). Own face PNGs, own shirt/pants textures, one signature colour (look.md §9). Write the cast file `your project folder/cast/<name>.md`.
- Face kit: 19 PNGs per character, 512×512, transparent, layered Eyes / Brows / Mouth (look.md §7.1). **Do the 2-minute decal test (mcp-setup.md test B, 4 test PNGs) before drawing the rest.**
- Upload: `upload_image` (check in the decal test whether it takes a local file; fallback: Studio → Asset Manager → Bulk Import). Put the IDs in `ReplicatedStorage.FaceLibrary`.

### 0.6 Animation tools
- Free first: Luau C0 poses (`PoseLibrary`, below) + built-in Animation Editor + RoMixamo Lite (R6 walks/runs, free).
- **Moon Animator 2, about $30 one-time: ask the user before buying.** It can blow the month's $40 when ElevenLabs is already paid. Buy only if the free routes fail the first test's acting.

### 0.7 Shot runner + libraries (Claude writes once, in `ReplicatedStorage`)
Code in § Appendix A. In **ReplicatedStorage**: `LightingPresets` (templates/lighting-presets.lua; it must be here, not ServerStorage, so the client can use it), `FaceLibrary`, `PoseLibrary`, `ShotRunner`, a `Scenes` folder and a StringValue `PlayList`. In **StarterPlayer.StarterPlayerScripts**: the LocalScript `RunScenes`, which plays the scenes named in `PlayList` when Play starts. Set `game.Players.CharacterAutoLoads = false` (no player avatar spawns).

### 0.8 Local helper scripts (Python 3 + OpenCV + ffmpeg; `pip3 install opencv-python numpy`)
All in this skill's `tools/` folder: `script_check.py`, `plan_timing.py`, `shotlist_check.py`, `pacing_check.py`, `make_caps.py`, `move_check.py`, `measure.py`, `assemble.py` (+ `sheetlib.py`, their shared parser). Copy the folder to the Mac once.

---

## Step 1. Script → `script.md` (ESTIMATE 45 min first, 30 min later)
Follow the script rules in this skill (`script.md`, `checklist.md` §1): rule in sentence 1, first word ≤0.2 s; twist family not used in the last 5 episodes; no banned phrases; it must sound like the user talking (humanizer skill / Script Studio if he wants). Run `tools/plan_timing.py --rewrite-times` and `tools/script_check.py` on the sheet. Write the episode's row in `ROTATION-LOG.md` now (the 7 core fields of `templates/rotation-log.md` are mandatory, the rest when you can), so the shot list follows it.

## Step 2. Voice + word timestamps (ESTIMATE 20–40 min / 15 min)
- ElevenLabs, his professional voice clone, settings in audio.md §1. **Ask before generating** ("about N words, 2 takes each, OK?").
- Save `audio/vo.wav`. Set the designed pauses in the audio editor (script.md §6: the pause length is the whole silence between the two words).
- Word timestamps, free: his studio's `python3 studio/timing.py <vo.wav> --script <script.md>` (already installed; writes `words.json`), or WhisperX forced alignment (captions.md §3). Do not use paid transcription without asking.

## Step 3. Shot list (ESTIMATE 45 min / 20 min)
Claude drafts `shotlist.md` from `script.md` + `words.json` with `templates/shot-list.md` (before the voice exists, use `plan_timing.py`'s `words_planned.json` and rebuild the times from the real one later): one row per shot, cut 1 frame before each sentence start (pacing.md), sizes/angles/moves per look.md, a mood per scene and a deliberate shift on the twist cut (lighting-color.md §4). Run `python3 shotlist_check.py shotlist.md`; fix every FAIL or write why. the user reads the table (2 minutes) before anything is built.

## Step 4. Build sets + light via MCP (ESTIMATE 1.5–3 h / 30–60 min)
Per location, Claude: inserts the free map (or reuses the set library place), strips scripts, dresses 2–3 story props and the rule object, applies the scene's mood (`P.apply`), adds practicals, then takes **one** `screen_capture` per set from the main angle for the user to approve. Calibrate the mood once per set: grab a still in OBS, run `measure.py`, adjust (lighting-color.md §6). `save_place`.

## Step 5. Pose / animate (ESTIMATE 3–5 h / 1.5–3 h)
- Poses: Claude adds missing poses to `PoseLibrary`, each checked once with a `screen_capture` CU.
- Walks and runs: RoMixamo Lite clips; in Play mode only animations owned by the user load (UNVERIFIED; it's the usual Roblox ownership rule).
- Faces: Claude converts the shot list's face column into timed swaps from `words.json` (key word ±3 frames, flaps at 2–3/s on on-camera dialogue, blinks every 3–4 s).
- Target: stiff idle ≤40 %, posed/animated ≥35 % (look.md L15).

## Step 6. Camera + record (ESTIMATE 1.5–2.5 h / 45–90 min)
1. Claude writes one scene data file per scene (`scenes/S01.lua` → `ReplicatedStorage.Scenes.S01`) from the shot list: shot start times relative to the scene, camera `from`/`to` (or `path`) CFrames, FOV, ease, mood, focus, face swaps, poses, events. Format in Appendix A.
2. Framing check: one `screen_capture` per new setup with the shot's camera (cheap version: only the key and twist shots).
3. the user starts OBS recording **once** for the whole session.
4. Claude sets `ReplicatedStorage.PlayList.Value = "S01,S02,S03"` (Edit mode) and calls `start_stop_play`. `RunScenes` plays them back to back, each opening on a 1.0 s white slate; Claude stops Play when they're done (scene lengths + 1.5 s each). Bad take? Set `PlayList` to that scene and play again; note which slate was good. (A long blocking `execute_luau` call might time out, which is why the LocalScript runs the scenes; UNVERIFIED either way until the first test.)
5. the user stops OBS. Takes go in `takes/`.
6. Stills for tests only: `screen_capture` with a camera, or `ffmpeg -ss <t> -i take.mov -frames:v 1 still.png` (free).

## Step 7. Edit
1. **Cut the picture (free, about 2 min of machine time):** `python3 assemble.py takes/session1.mov 15.0,22.4,… edit/picture.mp4 [--use 1,3,4]` finds the slates, trims each scene to its exact length, blends 60→30 fps and joins them. Picture length = voice length.
2. Check: `python3 move_check.py edit/picture.mp4 cuts.txt` (cuts.txt = the shot list's start times, one per line; ≥70 % move), `python3 measure.py --video edit/picture.mp4 --times …` (colour targets), pacing check (pacing.md §7).
3. **Where to finish (captions, music, SFX, review notes):**

| | his own studio (Studio Preview 2.0) | CapCut desktop (free) | Premiere |
|---|---|---|---|
| good at | review notes → Claude fixes → "Check fixes" tour; drag-drop VOICE / MUSIC / SFX tracks with his sound pack, music ducks under the voice; word timing; swear-clean render | fast hand trimming of many clips; native 9:16 timeline; quick export | everything, if he already pays for it |
| weak for this format | built for code-drawn 16:9 scenes: overlays are `file, scene, lt, dur, x, y, w, opacity` with no source in-point (pre-cut clips); `--vertical` is cut from the middle of a 4K render, so every final renders 3840×2160 lossless frames (slow for 2–3 min); videos in scenes need light preview proxies (scene-rules §6); the video.js API was not reviewed for this skill, so one long 9:16 overlay is UNVERIFIED | captions style must be rebuilt by hand to the captions.md spec; whether auto-captions are free is unconfirmed | about $23/month (GUESS, check): does not fit the budget next to ElevenLabs. Don't buy it for this |
| use it when | the 20 s studio test below passes | the studio test fails, or a scene needs hand-trimmed cuts | only if already paid |

**Honest verdict:** the fastest path is the one with the least hand editing: the live cut in Roblox + `assemble.py` + the captions.md ASS file + the ffmpeg mix from audio.md. All scripted, re-runs cost no tokens. His studio is a good **finisher** for sound and review notes, but it is a poor tool for cutting 60–100 separate clips, and its vertical render path is slow. Use it only after a 20 s test proves a full-height 9:16 video overlay renders sharp in `--vertical`. If that test fails, CapCut desktop free is the fallback. Premiere costs money he doesn't need to spend.

**20 s studio test (do once):** `node studio/new-video.js roblox-test`; put a 20 s `picture.mp4` in `videos/roblox-test/assets/`; add it in `edit.json` `"overlays"` to fill the middle 9:16 of the frame (find out whether x/y are the corner or the centre; for a corner, x ≈ 0.342, w ≈ 0.316 of a 16:9 frame); render `--vertical`. Pass = sharp, in sync with the voice, captions at about 70 % height, and render time noted.

## Step 8. Captions (ESTIMATE 15–30 min / 10 min)
captions.md: one word per caption, Montserrat ExtraBold 104 px, centre at 70 % height, 12 px outline, pop 125 → 100 % over 4 frames, onset −2…0 frames. Generate `caps.ass` from `words.json` (captions.md §3) and burn it in with ffmpeg, or set the same style in his studio's caption panel. Colour tests always run on the caption-free picture.

## Step 9. Mix (ESTIMATE 45 min / 30 min)
audio.md §2–§4 and the cue sheet (`templates/cue-sheet.md`): voice −15.5 to −16.5 LUFS, bed −22 to −25 LUFS, voice 7–10 dB over the bed, 2–5 real SFX per minute, 1–2 music events landing on the climax or twist line. Final file **−14 LUFS integrated, ≤ −1.0 dBTP** (limiter ceiling −1.5). Measure: `ffmpeg -i final.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12`.

## Step 10. Export (one file for both IG Reels and YouTube Shorts)
| item | value |
|---|---|
| Size / fps | 1080×1920, **30 fps constant** |
| Video | H.264 High, yuv420p, BT.709 tags, VBR about 12 Mbps (max 16), keyframe every 15 frames |
| Audio | AAC-LC, 48 kHz stereo, 320 kbps |
| Loudness | −14 LUFS integrated, ≤ −1.0 dBTP |
| Container | MP4 with `+faststart` |
| Length | ≤ 2:59 (Shorts and Reels allow up to 3 min as of 2025; UNVERIFIED today, recheck if it matters) |

YouTube's own upload guide recommends about 8 Mbps for 1080p30 SDR (known guide, not re-checked today); 12 Mbps gives headroom for the platform re-encode (HYPOTHESIS).

```bash
ffmpeg -i edit/picture_caps.mp4 -i edit/mix.wav -map 0:v -map 1:a \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -r 30 -b:v 12M -maxrate 16M -bufsize 24M -g 15 \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 \
  -c:a aac -b:a 320k -ar 48000 -movflags +faststart -shortest final.mp4
```
(Faster on the Mac: `-c:v h264_videotoolbox -b:v 12M` instead of libx264.)

## Step 11. Disclosure and platform rules
- **Instagram**: turn on **"AI info"** when the narration is TTS or his voice clone (Meta asks for a label on "realistic-sounding audio" that was digitally created; penalties possible). His own recorded voice needs no label.
- **YouTube**: no AI disclosure needed: animated (non-realistic) content is exempt, and "cloning one's own voice to create voice overs" is listed as exempt. A stock, non-the user TTS voice in an animated video is probably exempt too (GUESS).
- **YouTube YPP "inauthentic content"**: don't make "characters … put in the same situation over and over again with the same outcome". The rotation log is the protection.
- **Roblox**: no Roblox logo anywhere (thumbnail, video); no implied endorsement; "Roblox" only in the description and hashtags (GUESS); no Roblox in-game music; no Classic/noob avatars. Recording Creator Store assets in Studio is a low-but-nonzero-risk grey zone every Roblox channel works in. Credit any CC-BY music in the description (audio.md §5.3).

## Step 12. QA (ESTIMATE 30 min / 20 min)
Score with `checklist.md` (every area ≥8, U1–U14 ≥10 met) and write `QA.md`. Update the episode's row in `ROTATION-LOG.md` (fields: `templates/rotation-log.md`).

---

## Time per reel (ESTIMATE, 90–120 s, 55–75 shots)

| stage | first reels | reel 5+ (libraries reused) |
|---|---|---|
| 0 one-time setup | 5–8 h once | — |
| 1 script | 45 min | 30 min |
| 2 voice + timing | 20–40 min | 15 min |
| 3 shot list | 45 min | 20 min |
| 4 sets + light | 1.5–3 h | 30–60 min |
| 5 pose/animate | 3–5 h | 1.5–3 h |
| 6 camera + record | 1.5–2.5 h | 45–90 min |
| 7 assemble + checks | 30–60 min | 15–30 min |
| 8 captions | 15–30 min | 10 min |
| 9 mix | 45 min | 30 min |
| 10–11 export + post | 20 min | 15 min |
| 12 QA | 30 min | 20 min |
| **total per reel** | **about 11–16 h** | **about 5.5–9 h** |

These times hold only inside the build budget below, and they don't include drawing new PNGs: add the drawing time for new face kits, marks and silhouettes per episode (ESTIMATE: replace with the first kit's real minutes per PNG). The round-1 plan (8 sets, about 11 rigs, about 110 face PNGs, about 35 poses) was estimated at 25–40 h by the critic, 2–3x this table.

## Build budget (per episode; HYPOTHESIS: the round-1 critic's estimate, replace with the first test's real hours)

| item | cap | how to stay under it |
|---|---|---|
| shots | soft cap 0.6 × runtime in s (about 70 at 120 s) | extra camera setups in an existing set are cheap with the ShotRunner; poses and faces are the cost |
| sets | ≤6, of which ≤2 new | the rest come from the set-library place, redressed (3 props + wall colours) |
| rigs with a full face kit (19 PNGs) | ≤5 (hero + ≤4) | everyone else shares one 8-PNG side kit |
| new face PNGs | ≤40 (about 2 new full kits) + ≤12 rule-mark states | reuse the cast's kits from FaceLibrary |
| rule-object images (marks, silhouettes, sign states, sound-proxy images) | ≤12 distinct uploaded images, counted from the shot list's props column, not from memory (round 2 planned 12 and needed about 20). TextLabel strings on one SurfaceGui template (phone texts, signs) don't count | one sheet for a group (the kids' wants on one image); reuse a sheet between shots |
| new poses | ≤15 | PoseLibrary first |
| contact poses (two rigs touching) | ≤3 | hand-holding, cheek touch, stepping on feet are the hardest R6 work (look.md §16) |
| special builds (a first-time trick: mirror POV, rendered photo on a SurfaceGui, a shadow/silhouette system, a new rig of parts, an in-shot dolly-zoom the first time) | ≤2 | a system built once (ShadowLibrary, the dolly field) is reused, not a special build, next time |
| new VFX (ParticleEmitter setups) | ≤3 | keep them in a `VfxLibrary` module for the next episode |
| outfits | 1 per character | add a jacket Part instead of a new outfit |
| crowds | cloned static posed rigs, soft in DOF, ≤3 of them moving | |
| flashbacks | shown through an object (photo, video, drawing) unless the set already exists | |

**Reuse plan.** A locked hero and 1–2 recurring side characters with cast files and kits; the set-library place grows by ≤2 sets per episode; poses, VFX and mood variants worth keeping move into PoseLibrary, VfxLibrary and the presets module. The shot list's "Build cost" block counts new vs reused against these caps; anything over a cap needs a reason and the user's OK.

Outside benchmarks (production research): about 5 h per 30 s for a Blender faceless pipeline; about 1.5 h for one short Moon Animator clip with dialogue. Replace these estimates with the first test's real numbers.

---

## First test: one 15 s scene end to end (do this before a full episode)
Scene: the 8-row example in `templates/shot-list.md` (lantern street, 15.0 s). Cost $0: the user reads the 53 words into his phone or uses an existing voice take (ask before any ElevenLabs generation).

| # | step | pass if | ESTIMATE |
|---|---|---|---|
| 1 | MCP connected; mcp-setup.md tests A–C | all three run; capture pixel size and seconds per capture noted | 30 min |
| 2 | 2-minute decal test | 3 layers render, the swap shows | 5 min |
| 3 | build the street + 2 doors, hero + neighbour rigs, 6 poses, 8 shots of scene data | `shotlist_check.py` passes (L18 info only) | 1.5–2 h |
| 4 | record with the shot runner, 60 fps, blend and no-blend versions | OBS stats: 0 dropped/lagged frames; every cut within 1 frame of plan (step through the cut frames); slate found | 30 min |
| 5 | `move_check.py` and `measure.py` on the caption-free picture | ≥70 % shots move; C1–C5 pass or the misses are understood | 15 min |
| 6 | captions + mix + export | caption onset −2…0 frames on 2 words; −14 LUFS, ≤ −1 dBTP | 30 min |
| 7 | the 20 s studio test (Step 7) | sharp and in sync, render time noted | 30 min |
| 8 | write down real times per stage, viewport pixel size, blend vs no blend, studio vs CapCut verdict | written into this file, replacing ESTIMATE / UNVERIFIED | 10 min |

If step 4 fails (frame drops or cut jitter): lower Editor Quality to 18, turn off shadows on extra lights, close other apps. Still failing: record each shot as its own take (the runner's `play` with a one-shot scene) and cut in CapCut.

---

## Appendix A. Shot runner, libraries, scene data (Luau; UNTESTED until the first test)

```lua
-- ReplicatedStorage.ShotRunner (ModuleScript). Runs in PLAY mode on the CLIENT (called by RunScenes below).
local RunService = game:GetService("RunService")
local TweenService = game:GetService("TweenService")
local StarterGui = game:GetService("StarterGui")
local Players = game:GetService("Players")
local RS = game:GetService("ReplicatedStorage")
local P = require(RS.LightingPresets)
local Faces = require(RS.FaceLibrary)   -- Faces[rigName][layer][state] = "rbxassetid://..."
local Poses = require(RS.PoseLibrary)   -- Poses[poseName][jointName] = {xDeg, yDeg, zDeg} offset on the joint's C0
local okS, Shadows = pcall(require, RS:FindFirstChild("ShadowLibrary")) -- optional: Shadows[name][state] = "rbxassetid://..." (look.md §6.1)
if not okS then Shadows = {} end

local M = {}
local orig = {} -- Motor6D -> rest C0

local function ease(a, kind)
	a = math.clamp(a, 0, 1)
	if kind == "linear" then return a end
	if kind == "out" then return 1 - (1 - a) * (1 - a) end
	return 0.5 - 0.5 * math.cos(math.pi * a) -- Sine InOut (default)
end

local function camAt(s, a)
	local path = s.cam.path or { s.cam.from, s.cam.to or s.cam.from }
	if #path == 1 then return path[1] end
	local x = a * (#path - 1)
	local seg = math.min(#path - 1, math.floor(x) + 1)
	return path[seg]:Lerp(path[seg + 1], x - (seg - 1))
end

function M.setFace(rigName, layer, state)
	local rig = workspace:FindFirstChild(rigName)
	local head = rig and rig:FindFirstChild("Head")
	local decal = head and head:FindFirstChild(layer)
	local id = Faces[rigName] and Faces[rigName][layer] and Faces[rigName][layer][state]
	if decal and id then decal.Texture = id else warn("[ShotRunner] face missing", rigName, layer, state) end
end

-- Story silhouettes / signs on walls (look.md §6.1): a part named `partName` anywhere in workspace holding a SurfaceGui
-- with an ImageLabel. Swap its image, then fade ImageTransparency to `alpha` (default 0.3) over `fade` s (0 = instant).
function M.setShadow(partName, state, fade, alpha)
	local part = workspace:FindFirstChild(partName, true)
	local img = part and part:FindFirstChildWhichIsA("ImageLabel", true)
	local id = Shadows[partName] and Shadows[partName][state]
	if not img then warn("[ShotRunner] shadow part missing", partName) return end
	if id then img.Image = id elseif state ~= "off" then warn("[ShotRunner] shadow state missing", partName, state) end
	local goal = { ImageTransparency = state == "off" and 1 or (alpha or 0.3) }
	if (fade or 0) > 0 then TweenService:Create(img, TweenInfo.new(fade), goal):Play() else img.ImageTransparency = goal.ImageTransparency end
end

function M.setPose(rigName, poseName, dur)
	local rig = workspace:FindFirstChild(rigName)
	local pose = Poses[poseName]
	if not (rig and pose) then warn("[ShotRunner] pose missing", rigName, poseName) return end
	for _, m in ipairs(rig:GetDescendants()) do
		if m:IsA("Motor6D") then
			orig[m] = orig[m] or m.C0
			local d = pose[m.Name] or { 0, 0, 0 } -- joints not named go back to rest
			local goal = orig[m] * CFrame.Angles(math.rad(d[1]), math.rad(d[2]), math.rad(d[3]))
			if (dur or 0) > 0 then
				TweenService:Create(m, TweenInfo.new(dur, Enum.EasingStyle.Sine, Enum.EasingDirection.InOut), { C0 = goal }):Play()
			else
				m.C0 = goal
			end
		end
	end
end

function M.play(scene)
	local cam = workspace.CurrentCamera
	cam.CameraType = Enum.CameraType.Scriptable
	pcall(function() StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.All, false) end)
	pcall(function() StarterGui:SetCore("TopbarEnabled", false) end) -- UNVERIFIED on the current top bar: else crop it in OBS

	local gui = Instance.new("ScreenGui")
	gui.IgnoreGuiInset = true
	gui.DisplayOrder = 100
	local slate = Instance.new("Frame")
	slate.Size = UDim2.fromScale(1, 1)
	slate.BackgroundColor3 = Color3.new(1, 1, 1)
	slate.BorderSizePixel = 0
	slate.Parent = gui
	gui.Parent = Players.LocalPlayer:WaitForChild("PlayerGui")

	local shots = scene.shots
	for _, sh in ipairs(shots) do -- retakes start clean
		if sh.rack then sh.rack.started = nil end
		if sh.dolly then sh.dolly.d0, sh.dolly.f0 = nil, nil end
	end
	local faces, poses, events, shadows = scene.faces or {}, scene.poses or {}, scene.events or {}, scene.shadows or {}
	for _, f in ipairs(scene.startFaces or {}) do M.setFace(f.rig, f.layer, f.state) end
	for _, p in ipairs(scene.startPoses or {}) do M.setPose(p.rig, p.pose, 0) end
	cam.CFrame = camAt(shots[1], 0)
	cam.FieldOfView = shots[1].fov[1]
	local mood = shots[1].mood
	if mood then P.apply(mood) end

	task.wait(1.0) -- 1.0 s white slate (assemble.py finds it)
	slate.Visible = false
	local t0 = os.clock()
	local i, fi, pidx, ei, si, done = 1, 1, 1, 1, 1, false
	local conn
	conn = RunService.RenderStepped:Connect(function()
		local t = os.clock() - t0
		if t >= scene.dur then conn:Disconnect(); done = true; return end
		while shots[i + 1] and t >= shots[i + 1].t do -- the cut: camera snaps to the next shot
			if shots[i].rack then P.restoreDof() end -- a rack shot hands DOF back to the mood on the cut
			i += 1
			local s = shots[i]
			if s.mood and s.mood ~= mood then P.apply(s.mood); mood = s.mood end -- "mood" or "mood@clock"; no tween: lands on the cut
		end
		local s = shots[i]
		local rk = s.rack -- { at = s into the shot, from = studs, to = studs, secs = 0.4-0.8 } (look.md 3.3)
		if rk and not rk.started and t >= s.t + (rk.at or 0) then rk.started = true; P.rack(rk.from, rk.to, rk.secs) end
		local t1 = shots[i + 1] and shots[i + 1].t or scene.dur
		local a = ease((t - s.t) / (t1 - s.t), s.ease)
		cam.CFrame = camAt(s, a)
		cam.FieldOfView = s.fov[1] + ((s.fov[2] or s.fov[1]) - s.fov[1]) * a
		-- dolly-zoom inside one shot (look.md 3.3): dolly = { at = 0.3, dur = 1.2, to = 10, ease = "inout" }. From `at` s into
		-- the shot the camera backs away from its look-at point (cam.look, or 8 studs ahead) from its distance there to `to`
		-- studs, and FOV follows so d * tan(FOV/2) stays constant: the face keeps its size, the background stretches.
		local dz = s.dolly
		if dz and t >= s.t + (dz.at or 0) then
			local u = ease((t - s.t - (dz.at or 0)) / (dz.dur or 1.2), dz.ease)
			local look = s.cam.look or (cam.CFrame.Position + cam.CFrame.LookVector * 8)
			dz.d0 = dz.d0 or (cam.CFrame.Position - look).Magnitude
			dz.f0 = dz.f0 or cam.FieldOfView
			local d = dz.d0 + (dz.to - dz.d0) * u
			cam.CFrame = CFrame.lookAt(look - cam.CFrame.LookVector * d, look)
			cam.FieldOfView = 2 * math.deg(math.atan(dz.d0 * math.tan(math.rad(dz.f0 / 2)) / d))
		end
		if s.camFn then s.camFn(t - s.t, cam) end -- any other in-shot override; runs after the runner's own write, so it wins
		if s.focus and not (rk and rk.started) then -- per-frame focus would overwrite a rack
			local rig = workspace:FindFirstChild(s.focus)
			if rig and rig:FindFirstChild("Head") then P.focusOn(rig.Head, cam) end
		end
		while faces[fi] and t >= faces[fi].t do local f = faces[fi]; M.setFace(f.rig, f.layer, f.state); fi += 1 end
		while poses[pidx] and t >= poses[pidx].t do local p = poses[pidx]; M.setPose(p.rig, p.pose, p.dur); pidx += 1 end
		while events[ei] and t >= events[ei].t do task.spawn(events[ei].fn); ei += 1 end
		while shadows[si] and t >= shadows[si].t do local h = shadows[si]; M.setShadow(h.part, h.state, h.fade, h.alpha); si += 1 end
	end)
	repeat task.wait() until done
	task.wait(0.5) -- 0.5 s handle on the last frame
	gui:Destroy()
end

return M
```

```lua
-- StarterPlayer.StarterPlayerScripts.RunScenes (LocalScript). Plays ReplicatedStorage.PlayList ("S01,S02") on Play.
local RS = game:GetService("ReplicatedStorage")
local list = RS:WaitForChild("PlayList").Value
if list == "" then return end
task.wait(2) -- let the place and textures load before the first slate
local R = require(RS:WaitForChild("ShotRunner"))
local em = RS:FindFirstChild("EpisodeMoods") -- optional: P.variant(...) calls for this episode (lighting-color.md 3)
if em then require(em) end
for name in string.gmatch(list, "[^,%s]+") do
	R.play(require(RS.Scenes[name]))
end
```

```lua
-- ReplicatedStorage.PoseLibrary (ModuleScript). Offsets in degrees on each R6 joint's C0:
-- "Neck", "Right Shoulder", "Left Shoulder", "Right Hip", "Left Hip", "RootJoint".
-- Each joint has its own axes: on R6 shoulders and hips the Z angle swings the limb forward/back (UNVERIFIED signs).
-- Check every new pose once with a screen_capture CU, fix the signs, then keep it.
return {
	rest = {},
	point = { ["Right Shoulder"] = { 0, 0, 90 }, Neck = { 0, 0, 0 } },
	headDrop = { Neck = { -25, 0, 0 } },
	handToFace = { ["Right Shoulder"] = { 0, 0, 150 }, Neck = { -10, 0, 0 } },
	kneel = { ["Right Hip"] = { 0, 0, 90 }, ["Left Hip"] = { 0, 0, -20 } },
}
```

```lua
-- ReplicatedStorage.FaceLibrary (ModuleScript): IDs from upload_image / Asset Manager.
return {
	Hero = {
		Eyes = { open = "rbxassetid://0", half = "rbxassetid://0", closed = "rbxassetid://0", wide = "rbxassetid://0" },
		Brows = { neutral = "rbxassetid://0", sad = "rbxassetid://0", raised = "rbxassetid://0" },
		Mouth = { closed = "rbxassetid://0", smile = "rbxassetid://0", O = "rbxassetid://0", openSmall = "rbxassetid://0" },
	},
}
```

```lua
-- ReplicatedStorage.Scenes.S01 (ModuleScript): written by Claude from shotlist.md + words.json.
-- Times are seconds from the scene start (= global voice time minus the scene's first shot time).
local V, L = Vector3.new, CFrame.lookAt
return {
	dur = 4.70,
	startFaces = { { rig = "Neighbour", layer = "Eyes", state = "half" } },
	startPoses = { { rig = "Hero", pose = "rest" } },
	shots = {
		{ t = 0.00, mood = "normalDay", fov = { 60, 58 }, ease = "out",
		  cam = { from = L(V(0, 30, 40), V(0, 4, 0)), to = L(V(0, 24, 34), V(0, 4, 0)) } },  -- crane-down + push
		{ t = 2.10, fov = { 35, 33 }, cam = { from = L(V(8, 5, 6), V(10, 9, 2)), to = L(V(8.3, 5.2, 5.5), V(10, 9, 2)) } },
		{ t = 3.10, fov = { 45, 44 }, focus = "Neighbour", mood = "normalDay@18.5",
		  cam = { from = L(V(20, 5, 10), V(22, 5, 2)), to = L(V(20.2, 5, 9.4), V(22, 5, 2)) } },
	},
	faces = { { t = 4.32, rig = "Neighbour", layer = "Eyes", state = "closed" } }, -- "dies" at 4.42 minus 3 frames
	shadows = { { t = 3.40, part = "WallShadow_Hero", state = "lanternHeld", fade = 0.2 } }, -- optional: silhouette swaps
	poses = { { t = 3.40, rig = "Neighbour", pose = "headDrop", dur = 0.4 } },
	events = { { t = 2.30, fn = function() --[[ ignite lantern: emitter burst + light tween ]] end } },
}
```

## Appendix B. `assemble.py`
Code: `tools/assemble.py` (tested on a synthetic slated take: finds both slates, trims to the frame, outputs 30 fps). Usage in Step 7.
