#!/usr/bin/env python3
# move_check.py take.mp4 cuts.txt  -> zoom %/s and pan %/s per shot; caption band and top 13 % masked
import sys, cv2, numpy as np
def frame(cap, f):
    cap.set(cv2.CAP_PROP_POS_FRAMES, f); ok, im = cap.read()
    return cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) if ok else None
video, cutfile = sys.argv[1], sys.argv[2]
cap = cv2.VideoCapture(video); fps = cap.get(cv2.CAP_PROP_FPS); nf = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
starts = [float(x) for x in open(cutfile).read().split()]
bounds = list(zip(starts, starts[1:] + [nf / fps]))
orb = cv2.ORB_create(3000); bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
moved = n = 0
print("shot  start   len   zoom%/s  pan%/s   verdict")
for i, (a, b) in enumerate(bounds, 1):
    f0, f1 = int(a * fps) + 2, int(b * fps) - 3
    if f1 - f0 < 6: print(f"{i:4d} {a:6.2f}  too short"); continue
    g0, g1 = frame(cap, f0), frame(cap, f1)
    H, W = g0.shape; m = np.full((H, W), 255, np.uint8); m[int(.55 * H):int(.80 * H)] = 0; m[:int(.13 * H)] = 0
    k0, d0 = orb.detectAndCompute(g0, m); k1, d1 = orb.detectAndCompute(g1, m); n += 1
    if d0 is None or d1 is None or len(k0) < 30: print(f"{i:4d} {a:6.2f}  no texture (check by eye)"); continue
    mt = bf.match(d0, d1)
    p0 = np.float32([k0[x.queryIdx].pt for x in mt]); p1 = np.float32([k1[x.trainIdx].pt for x in mt])
    M, inl = cv2.estimateAffinePartial2D(p0, p1, ransacReprojThreshold=3)
    if M is None or inl.sum() < 40: print(f"{i:4d} {a:6.2f}  fit failed: big motion or parallax (check by eye)"); moved += 1; continue
    dur = (f1 - f0) / fps; sc = np.hypot(M[0, 0], M[1, 0])
    c = np.array([W / 2, H / 2]); shift = (M[:, :2] @ c + M[:, 2]) - c
    zoom = (sc - 1) * 100 / dur; pan = np.hypot(*shift) / W * 100 / dur
    mv = abs(zoom) >= 2 or pan >= 1.5          # HYPOTHESIS thresholds (refs: visible move >= ~3 %/s)
    moved += mv
    print(f"{i:4d} {a:6.2f} {b-a:5.2f}  {zoom:+7.1f}  {pan:6.1f}   {'moves' if mv else 'STATIC'}{'  FAST (>20 %/s)' if abs(zoom) > 20 else ''}")
print(f"\nshots that move: {moved}/{n} = {moved/max(n,1)*100:.0f}%  (target >=70%)")
