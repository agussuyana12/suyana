-- Look: dark-warm-vivid   (starting values: tune by eye against your references)
-- Paste into the Roblox Studio command bar.
local L = game:GetService("Lighting")
local function get(class, name) local o = L:FindFirstChild(name) or Instance.new(class) o.Name = name o.Parent = L return o end
L.Technology = Enum.Technology.Future
L.Brightness = 0.5
L.ExposureCompensation = -0.3
L.Ambient = Color3.fromRGB(30, 5, 5)
L.OutdoorAmbient = Color3.fromRGB(60, 10, 10)
L.ColorShift_Top = Color3.fromRGB(255, 90, 40)
L.ColorShift_Bottom = Color3.fromRGB(60, 0, 0)
L.ClockTime = 0
L.GeographicLatitude = 35
L.GlobalShadows = true
L.ShadowSoftness = 0.2
L.EnvironmentDiffuseScale = 1
L.EnvironmentSpecularScale = 1
local cc = get("ColorCorrectionEffect", "Look_CC")
cc.Brightness, cc.Contrast, cc.Saturation, cc.TintColor = -0.1, 0.3, 0.5, Color3.fromRGB(255, 170, 150)
local b = get("BloomEffect", "Look_Bloom")
b.Intensity, b.Size, b.Threshold = 1.2, 30, 0.8
local a = L:FindFirstChildOfClass("Atmosphere") or Instance.new("Atmosphere", L)
a.Density, a.Offset, a.Color, a.Decay, a.Glare, a.Haze = 0.45, 0, Color3.fromRGB(120, 20, 10), Color3.fromRGB(60, 10, 5), 0, 2
local d = get("DepthOfFieldEffect", "Look_DOF")  -- close-ups: soft background (reference does this)
d.FarIntensity, d.FocusDistance, d.InFocusRadius, d.NearIntensity = 0.3, 12, 8, 0
local s = get("SunRaysEffect", "Look_SunRays")
s.Intensity, s.Spread = 0.0, 0.6
workspace.CurrentCamera.FieldOfView = 55
print("Look dark-warm-vivid applied")
