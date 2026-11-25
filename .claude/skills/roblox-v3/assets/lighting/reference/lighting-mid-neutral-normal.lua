-- Look: mid-neutral-normal   (starting values: tune by eye against your references)
-- Paste into the Roblox Studio command bar.
local L = game:GetService("Lighting")
local function get(class, name) local o = L:FindFirstChild(name) or Instance.new(class) o.Name = name o.Parent = L return o end
L.Technology = Enum.Technology.Future
L.Brightness = 2.5
L.ExposureCompensation = 0
L.Ambient = Color3.fromRGB(25, 25, 35)
L.OutdoorAmbient = Color3.fromRGB(128, 128, 135)
L.ColorShift_Top = Color3.fromRGB(255, 245, 230)
L.ColorShift_Bottom = Color3.fromRGB(0, 0, 0)
L.ClockTime = 13
L.GeographicLatitude = 35
L.GlobalShadows = true
L.ShadowSoftness = 0.2
L.EnvironmentDiffuseScale = 1
L.EnvironmentSpecularScale = 1
local cc = get("ColorCorrectionEffect", "Look_CC")
cc.Brightness, cc.Contrast, cc.Saturation, cc.TintColor = 0, 0.12, 0.05, Color3.fromRGB(255, 252, 245)
local b = get("BloomEffect", "Look_Bloom")
b.Intensity, b.Size, b.Threshold = 0.4, 24, 0.95
local a = L:FindFirstChildOfClass("Atmosphere") or Instance.new("Atmosphere", L)
a.Density, a.Offset, a.Color, a.Decay, a.Glare, a.Haze = 0.25, 0, Color3.fromRGB(199, 210, 230), Color3.fromRGB(106, 112, 125), 0, 0
local d = get("DepthOfFieldEffect", "Look_DOF")  -- close-ups: soft background (reference does this)
d.FarIntensity, d.FocusDistance, d.InFocusRadius, d.NearIntensity = 0.35, 14, 10, 0
local s = get("SunRaysEffect", "Look_SunRays")
s.Intensity, s.Spread = 0.0, 0.6
workspace.CurrentCamera.FieldOfView = 55
print("Look mid-neutral-normal applied")
