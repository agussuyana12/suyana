# One-time setup on the Mac (all free)

Blender is already installed. Use Blender 4.2 or newer (Blender menu → About Blender).
If it's older, get the free Apple Silicon build from blender.org/download.

Paste these in Terminal one at a time:

```bash
# 1. uv (runs the Blender bridge for Claude Code)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Put the bridge add-on into Blender
uvx mcp-for-blender install-addon

# 3. Let Claude Code talk to Blender (telemetry off)
claude mcp add --env DISABLE_TELEMETRY=true blender -- uvx mcp-for-blender

# 4. ffmpeg, to join rendered frames into an mp4 (skip if `ffmpeg -version` works)
brew install ffmpeg

# 5. Short command for Blender
echo 'alias blender="/Applications/Blender.app/Contents/MacOS/Blender"' >> ~/.zshrc && source ~/.zshrc
```

Then in Blender: Edit → Preferences → Add-ons → turn on **MCP for Blender**.
In the 3D view press N → **MCP for Blender** tab → Start server. Tick **Poly Haven**.
Leave the telemetry box off. Do not sign up for Premium.

Test the kit:
```bash
cd "<your project folder>/skills/roblox-v3"
blender -b -P shots/example_shot.py -- draft still
open renders/example_shot
```
You should see 3 pictures: the hero walking in, then scared close-ups.
