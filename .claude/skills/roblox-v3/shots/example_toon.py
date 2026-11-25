"""Example bright-toon shot (style-toon.md): 5 s in a school hallway, 3 cameras, 2 cuts.
High-key pastel light, readable sign, face swap on every beat.

Render:  blender -b -P shots/example_toon.py -- draft still   (4 framing stills)
         blender -b -P shots/example_toon.py -- draft         (fast frames)
         blender -b -P shots/example_toon.py -- final
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
import rbxkit as k  # noqa: E402

args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
quality = args[0] if args else "draft"
still = "still" in args
P = k.PASTEL

k.clean_scene()
k.toon_room(w=20, d=12, h=9, wall=P["cream"], floor=(P["tile_a"], P["tile_b"]), band=P["teal"])
k.apply_look("toon_day", subject=(0, 1, 3))

# lockers along the back wall, in two colours
for i in range(8):
    col = P["butter"] if i % 2 else P["sky"]
    x = -7 + i * 1.55
    k.box(f"locker{i}", (1.45, 0.9, 5.6), (x, 5.3, 2.8), k.mat(f"locker_m{i % 2}", col, 0.5), bevel=0.05)
    k.box(f"vent{i}", (0.9, 0.06, 0.5), (x, 4.83, 4.6), k.mat("vent", P["charcoal"], 0.6))
    k.box(f"handle{i}", (0.12, 0.1, 0.5), (x + 0.45, 4.82, 2.9), k.mat("metal", P["grey"], 0.3, 0.6))
k.sign("notice", ["TODAY:", "PIZZA DAY", "(again)"], (6.6, 5.7, 5.6), w=3.6, h=2.4, border=P["teal"],
       colors=[P["charcoal"], P["coral"], P["grey"]], sizes=[0.42, 0.5, 0.3])

hero = k.make_hero("Hero", at=(-1.2, 1.0, 0), facing=-18, skin="#F1C9A5", shirt=P["coral"], pants="#3D4A6B",
                   shoes="#F4F4F0", hair="#4A3020", hair_style="fluffy", sleeves=False)
pal = k.make_hero("Pal", at=(1.5, 1.4, 0), facing=22, skin="#D9A57E", shirt=P["lilac"], pants="#2E3138",
                  shoes="#F4F4F0", hair="#1E1A22", hair_style="long")

# beats: 1-45 pal tells him, 46 he gets it (shocked), 92 nervous, pal smirks then winks
k.set_face(hero, 1, "smile")
k.set_face(pal, 1, "sparkle")
k.idle(hero, 1, 150)
k.idle(pal, 1, 150, seed=4)
k.talk(pal, 8, 40, base="sparkle", rate=4)
k.blink(hero, 30, "smile")
k.recoil(hero, 46, face="shocked")
k.set_face(pal, 60, "smirk")
k.set_face(hero, 92, "nervous")
k.hold(hero, 96, "shrug")
k.set_face(pal, 120, "wink")

two = k.camera("cam_two", (0.4, -12.5, 3.3), (0.2, 1.2, 2.9), lens=40)
cu_hero = k.face_cam("cam_hero", hero, dist=3.8, lens=32)      # toon close-up: wide lens, close, frontal
cu_pal = k.face_cam("cam_pal", pal, dist=3.8, lens=32)
k.push_in(two, 1, 45, amount=1.2)
k.push_in(cu_hero, 46, 100, amount=0.5)
k.push_in(cu_pal, 101, 150, amount=0.4)
k.cut_to(two, 1)
k.cut_to(cu_hero, 46)
k.cut_to(cu_pal, 101)

out = os.path.join(HERE, "..", "renders", "example_toon")
sc = k.render_setup(out, 1, 150, quality=quality)
k.save(os.path.join(HERE, "..", "renders", "example_toon.blend"))

if k.bpy.app.background:
    if still:
        for f in (20, 52, 96, 125):
            sc.frame_set(f)
            sc.render.filepath = os.path.join(out, f"still_{f:04d}.png")
            k.bpy.ops.render.render(write_still=True)
    else:
        k.bpy.ops.render.render(animation=True)
