# First 15 s test: paste into Claude Code

Before you paste:
- Roblox Studio is open with a new Baseplate.
- MCP is on (Assistant → Manage MCP Servers → Enable Studio as MCP server → Quick connect → Claude Code).
- OBS is installed.
- Start Claude Code in Terminal from your project folder.

```
Read skills/roblox/SKILL.md, then pipeline.md ("First test" + Step 0) and templates/mcp-setup.md.
Run the first 15 s test from pipeline.md, steps 1-8, in your project folder/.
Use the 8-row example in templates/shot-list.md (lantern street) as the scene.
Rules:
- Use the Roblox Studio MCP for everything inside Studio.
- Free models only, and strip their scripts.
- Lighting presets from templates/lighting-presets.lua.
- Custom hero rig with my own face decals. Do the 2-minute decal test first and tell me what face PNGs to draw.
- No ElevenLabs generation and no purchases. For voice, I'll record the 53 words on my phone; tell me when and where to save the file.
- Check framing with screen_capture stills, max 15.
- Tell me exactly when to press record in OBS and with which settings.
- At the end, write the real times, viewport pixel size and the verdicts (step 8) into pipeline.md, and list what broke.
```
