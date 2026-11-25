-- Look: bright-warm-vivid   (starting values: tune by eye against your references)
-- Paste into the Roblox Studio command bar.
local L = game:GetService("Lighting")
local function get(class, name) local o = L:FindFirstChild(name) or Instance.new(class) o.Name = name o.Parent = L return o end
L.Technology = Enum.Technology.Future
L.Brightness = 3.0
L.ExposureCompensation = 0.2
L.Ambient = Color3.fromRGB(120, 80, 40)
L.OutdoorAmbient = Color3.fromRGB(200, 160, 110)
L.ColorShift_Top = Color3.fromRGB(255, 225, 170)
L.ColorShift_Bottom = Color3.fromRGB(120, 60, 20)
L.ClockTime = 14
L.GeographicLatitude = 35
L.GlobalShadows = true
L.ShadowSoftness = 0.25
L.EnvironmentDiffuseScale = 1
L.EnvironmentSpecularScale = 1
local cc = get("ColorCorrectionEffect", "Look_CC")
cc.Brightness, cc.Contrast, cc.Saturation, cc.TintColor = 0.05, 0.05, 0.35, Color3.fromRGB(255, 240, 210)
local b = get("BloomEffect", "Look_Bloom")
b.Intensity, b.Size, b.Threshold = 1.0, 40, 0.85
local a = L:FindFirstChildOfClass("Atmosphere") or Instance.new("Atmosphere", L)
a.Density, a.Offset, a.Color, a.Decay, a.Glare, a.Haze = 0.3, 0.1, Color3.fromRGB(255, 220, 170), Color3.fromRGB(220, 170, 110), 0.3, 1.5
local d = get("DepthOfFieldEffect", "Look_DOF")  -- close-ups: soft background (reference does this)
d.FarIntensity, d.FocusDistance, d.InFocusRadius, d.NearIntensity = 0.3, 14, 10, 0
local s = get("SunRaysEffect", "Look_SunRays")
s.Intensity, s.Spread = 0.15, 0.6
workspace.CurrentCamera.FieldOfView = 55
print("Look bright-warm-vivid applied")
