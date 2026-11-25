-- Look: mid-warm-vivid   (starting values: tune by eye against your references)
-- Paste into the Roblox Studio command bar.
local L = game:GetService("Lighting")
local function get(class, name) local o = L:FindFirstChild(name) or Instance.new(class) o.Name = name o.Parent = L return o end
L.Technology = Enum.Technology.Future
L.Brightness = 2.2
L.ExposureCompensation = 0
L.Ambient = Color3.fromRGB(40, 20, 10)
L.OutdoorAmbient = Color3.fromRGB(140, 100, 70)
L.ColorShift_Top = Color3.fromRGB(255, 200, 120)
L.ColorShift_Bottom = Color3.fromRGB(80, 30, 10)
L.ClockTime = 17.2
L.GeographicLatitude = 35
L.GlobalShadows = true
L.ShadowSoftness = 0.15
L.EnvironmentDiffuseScale = 1
L.EnvironmentSpecularScale = 1
local cc = get("ColorCorrectionEffect", "Look_CC")
cc.Brightness, cc.Contrast, cc.Saturation, cc.TintColor = -0.02, 0.2, 0.45, Color3.fromRGB(255, 235, 205)
local b = get("BloomEffect", "Look_Bloom")
b.Intensity, b.Size, b.Threshold = 0.8, 30, 0.9
local a = L:FindFirstChildOfClass("Atmosphere") or Instance.new("Atmosphere", L)
a.Density, a.Offset, a.Color, a.Decay, a.Glare, a.Haze = 0.3, 0.1, Color3.fromRGB(255, 200, 140), Color3.fromRGB(180, 110, 60), 0.3, 1
local d = get("DepthOfFieldEffect", "Look_DOF")  -- close-ups: soft background (reference does this)
d.FarIntensity, d.FocusDistance, d.InFocusRadius, d.NearIntensity = 0.4, 12, 8, 0
local s = get("SunRaysEffect", "Look_SunRays")
s.Intensity, s.Spread = 0.12, 0.6
workspace.CurrentCamera.FieldOfView = 55
print("Look mid-warm-vivid applied")
