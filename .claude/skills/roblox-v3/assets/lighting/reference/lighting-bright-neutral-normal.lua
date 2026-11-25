-- Look: bright-neutral-normal   (starting values: tune by eye against your references)
-- Paste into the Roblox Studio command bar.
local L = game:GetService("Lighting")
local function get(class, name) local o = L:FindFirstChild(name) or Instance.new(class) o.Name = name o.Parent = L return o end
L.Technology = Enum.Technology.Future
L.Brightness = 4.0
L.ExposureCompensation = 0.8
L.Ambient = Color3.fromRGB(150, 155, 170)
L.OutdoorAmbient = Color3.fromRGB(200, 205, 215)
L.ColorShift_Top = Color3.fromRGB(255, 255, 250)
L.ColorShift_Bottom = Color3.fromRGB(150, 160, 180)
L.ClockTime = 12
L.GeographicLatitude = 35
L.GlobalShadows = true
L.ShadowSoftness = 0.5
L.EnvironmentDiffuseScale = 1
L.EnvironmentSpecularScale = 1
local cc = get("ColorCorrectionEffect", "Look_CC")
cc.Brightness, cc.Contrast, cc.Saturation, cc.TintColor = 0.15, -0.1, -0.25, Color3.fromRGB(250, 250, 255)
local b = get("BloomEffect", "Look_Bloom")
b.Intensity, b.Size, b.Threshold = 1.5, 56, 0.75
local a = L:FindFirstChildOfClass("Atmosphere") or Instance.new("Atmosphere", L)
a.Density, a.Offset, a.Color, a.Decay, a.Glare, a.Haze = 0.5, 0.2, Color3.fromRGB(230, 235, 245), Color3.fromRGB(200, 210, 225), 0.5, 3
local d = get("DepthOfFieldEffect", "Look_DOF")  -- close-ups: soft background (reference does this)
d.FarIntensity, d.FocusDistance, d.InFocusRadius, d.NearIntensity = 0.2, 14, 10, 0
local s = get("SunRaysEffect", "Look_SunRays")
s.Intensity, s.Spread = 0.25, 0.6
workspace.CurrentCamera.FieldOfView = 55
print("Look bright-neutral-normal applied")
