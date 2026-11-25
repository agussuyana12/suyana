# Upgrades — how every episode beats the refs

The refs are the floor, not the target. Each episode must hit **at least 10 of these 14**. Score them in `checklist.md` §6.
Evidence for each gap is in `your analysis folder`. BET = hypothesis: keep it only if the user's own analytics agree.

| # | Upgrade | Pass test | Details in |
|---|---|---|---|
| U1 | New twist family (not used in the last 5 episodes; never "secret sacrifice for a dying relative" by default) | Twist log entry is different from the last 5 | script.md §4 |
| U2 | No stock lines ("for the first time", "I finally understood", "Everyone thought…") and no copied gold/ref line shapes | 0 hits in `script_check.py` (banned list + no-copy check) | script.md §9 |
| U3 | The voice breathes: 200–240 wpm with the designed pauses of script.md §6 (2–3 of 0.6–1.3 s: after the twist line and before the last line) | `pacing_check.py` on the voice file's word timestamps | script.md §6 |
| U4 | 1–2 music events at 45–90 % landing on the climax or twist line; event-1 type differs from the last episode's | Cue sheet + energy curve | audio.md §2 |
| U5 | 2–5 real SFX per minute, ≥35 % on cuts, and the rule object has its own sound motif | Cue sheet count | audio.md |
| U6 | Close shots ≥25 %; readable face on every key line | Shot list count | look.md |
| U7 | Posed or animated body on ≥35 % of shots; face-decal swap on the key word (±0.1 s); lip flaps on dialogue | Shot list + test capture | look.md |
| U8 | Real in-engine camera move on ≥70 % of shots (not just an edit zoom); one rack focus or dolly-zoom on the twist line | Shot list + capture | look.md |
| U9 | A deliberate lighting or palette shift on the twist cut | Two captures, brightness/warmth Δ ≥0.10 | lighting-color.md |
| U10 | Median saturation 0.35–0.50, ≤10 % of shots over 0.6, p99 ≥240 in ≥25 % of shots, p1 10–25 | `measure` step in lighting-color.md | lighting-color.md |
| U11 | Original custom hero avatar, 5–8 locations, 2–3 story props per set, no setup used more than twice | Shot list | look.md |
| U12 | Rule object in shot 1 and in ≥50 % of shots; every rule-state change shown within 1 shot | Shot list | look.md |
| U13 | Final shot ≥3 s on the rule object's final state; music resolves under it | Edit timeline | look.md, audio.md |
| U14 | Mix: −14 LUFS, true peak ≤ −1.0 dBTP, voice 7–10 dB over the bed; character pitch shift ≤+10 st | Loudness measurement on the export | audio.md |

## Rotate every episode (anti-template; YouTube "inauthentic content" protection)
Every rotating field and its rule (window, alternate, at most every other episode) is in `templates/rotation-log.md`. Log one row per episode in `your project folder/projects/ROTATION-LOG.md`.
