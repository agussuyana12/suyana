#!/usr/bin/env python3
# assemble.py - cut scenes out of one long OBS take by their white slates, blend 60->30 fps, join them.
# usage: python3 assemble.py take.mov 15.0,22.4,18.1 picture.mp4 [--use 1,3,4] [--noblend]
#   the list = each scene's duration in seconds, in story order (from the scene data files)
#   --use = which slates to use, in story order (after retakes: slate 2 was a bad take of scene 2, so use 1,3,4)
# Each scene starts on the first frame after a white slate (>=0.8 s of near-white frames; the runner shows a 1.0 s slate). Zero tokens.
import sys, subprocess, os, tempfile, cv2

take, durs, out = sys.argv[1], [float(x) for x in sys.argv[2].split(",")], sys.argv[3]
blend = "--noblend" not in sys.argv
cap = cv2.VideoCapture(take); fps = cap.get(cv2.CAP_PROP_FPS)
need = int(0.8 * fps); run = 0; f = 0; ins = []   # slate is 1.0 s; a short in-scene whiteout is ignored
while True:
    ok = cap.grab()
    if not ok: break
    _, im = cap.retrieve()
    small = cv2.resize(im, (36, 64))
    if small.mean() > 240 and small.min() > 200: run += 1
    else:
        if run >= need: ins.append(f)              # first frame after a slate
        run = 0
    f += 1
print(f"fps {fps:.2f}, frames {f}, slates found {len(ins)}, scenes expected {len(durs)}")
if "--use" in sys.argv:
    ins = [ins[int(x) - 1] for x in sys.argv[sys.argv.index("--use") + 1].split(",")]
if len(ins) != len(durs): sys.exit(f"{len(ins)} slates vs {len(durs)} scenes: pass --use to pick one slate per scene")
tmp = tempfile.mkdtemp(); parts = []
vf = "tmix=frames=2,fps=30" if blend else "fps=30"         # 2-frame blend = fake 180-degree shutter (HYPOTHESIS)
for k, (fin, d) in enumerate(zip(ins, durs), 1):
    p = os.path.join(tmp, f"scene{k:02d}.mp4"); parts.append(p)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{fin / fps:.4f}", "-i", take, "-t", f"{d:.4f}", "-an",
                    "-vf", vf, "-c:v", "libx264", "-crf", "14", "-preset", "medium", "-pix_fmt", "yuv420p", p], check=True)
    print(f"scene {k}: in {fin / fps:.3f} s, {d:.3f} s")
lst = os.path.join(tmp, "list.txt")
open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out], check=True)
print("wrote", out)
