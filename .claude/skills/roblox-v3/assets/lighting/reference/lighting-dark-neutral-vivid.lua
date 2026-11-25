-- Look: dark-neutral-vivid   (starting values: tune by eye against your references)
-- Paste into the Roblox Studio command bar.
local L = game:GetService("Lighting")
local function get(class, name) local o = L:FindFirstChild(name) or Instance.new(class) o.Name = name o.Parent = L return o end
L.Technology = Enum.Technology.Future
L.Brightness = 1.2
L.ExposureCompensation = -0.2
L.Ambient = Color3.fromRGB(20, 22, 45)
L.OutdoorAmbient = Color3.fromRGB(70, 75, 110)
L.ColorShift_Top = Color3.fromRGB(200, 210, 255)
L.ColorShift_Bottom = Color3.fromRGB(0, 0, 20)
L.ClockTime = 19.5
L.GeographicLatitude = 35
L.GlobalShadows = true
L.ShadowSoftness = 0.2
L.EnvironmentDiffuseScale = 1
L.EnvironmentSpecularScale = 1
local cc = get("ColorCorrectionEffect", "Look_CC")
cc.Brightness, cc.Contrast, cc.Saturation, cc.TintColor = -0.05, 0.18, 0.3, Color3.fromRGB(235, 240, 255)
local b = get("BloomEffect", "Look_Bloom")
b.Intensity, b.Size, b.Threshold = 0.5, 24, 0.92
local a = L:FindFirstChildOfClass("Atmosphere") or Instance.new("Atmosphere", L)
a.Density, a.Offset, a.Color, a.Decay, a.Glare, a.Haze = 0.3, 0, Color3.fromRGB(110, 120, 170), Color3.fromRGB(40, 45, 80), 0, 0.5
local d = get("DepthOfFieldEffect", "Look_DOF")  -- close-ups: soft background (reference does this)
d.FarIntensity, d.FocusDistance, d.InFocusRadius, d.NearIntensity = 0.35, 12, 8, 0
local s = get("SunRaysEffect", "Look_SunRays")
s.Intensity, s.Spread = 0.0, 0.6
workspace.CurrentCamera.FieldOfView = 55
print("Look dark-neutral-vivid applied")
