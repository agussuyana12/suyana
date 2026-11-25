"""Example 4-second shot: hero walks into a warm room, stops, sees something,
gets scared. Two cameras, one cut.

Render:  blender -b -P shots/example_shot.py -- draft     (fast check)
         blender -b -P shots/example_shot.py -- final
Open:    blender -P shots/example_shot.py                 (look in the viewport)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
import rbxkit as k  # noqa: E402

args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
quality = args[0] if args else "draft"
still = "still" in args                     # render one frame only

k.clean_scene()
k.room()
k.apply_look("warm_interior", subject=(0, 0, 3))

hero = k.make_hero("Hero", at=(4, 2, 0), shirt="#2E5E8C", hair_style="block")

# 1-45: walk in   45-60: stop, idle   62: sees it   63+: recoil, scared
k.set_face(hero, 1, "neutral")
k.walk(hero, 1, 44, to=(0, 0, 0))
k.turn_to(hero, 46, 0)
k.idle(hero, 50, 120)
k.blink(hero, 52)
k.talk(hero, 54, 61, base="neutral", rate=3)
k.recoil(hero, 62, face="scared")
k.shake(hero, 76, 118, bone="torso", amp=2.5)

wide = k.camera("cam_wide", (6, -16, 5.5), (1.5, 0, 3), lens=35)
close = k.camera("cam_close", (0.9, -6.5, 4.9), (0, 0, 4.5),
                 lens=60, dof_target=(0, 0, 4.6), fstop=1.8)
k.push_in(wide, 1, 60, amount=2.0)
k.push_in(close, 62, 120, amount=1.2)
k.handheld(close, strength=0.006)
k.cut_to(wide, 1)
k.cut_to(close, 62)

out = os.path.join(HERE, "..", "renders", "example_shot")
sc = k.render_setup(out, 1, 120, quality=quality)
k.save(os.path.join(HERE, "..", "renders", "example_shot.blend"))

if k.bpy.app.background:
    if still:
        for f in (30, 64, 90):
            sc.frame_set(f)
            sc.render.filepath = os.path.join(out, f"still_{f:04d}.png")
            k.bpy.ops.render.render(write_still=True)
    else:
        k.bpy.ops.render.render(animation=True)
