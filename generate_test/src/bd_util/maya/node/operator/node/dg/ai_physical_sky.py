# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_physical_sky import (
    GroundAlbedoField,
    OutColorField,
    OutTransparencyField,
    SkyTintField,
    SunDirectionField,
    SunTintField,
    XField,
    YField,
    ZField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiPhysicalSky(DG):
    __slots__ = ()

    NODE_TYPE = "aiPhysicalSky"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField()
    outa = outAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    turbidity = FloatField()

    groundAlbedo = GroundAlbedoField()
    ground_albedo = groundAlbedo
    groundAlbedoR = groundAlbedo.groundAlbedoR
    ground_albedor = groundAlbedoR
    groundAlbedoG = groundAlbedo.groundAlbedoG
    ground_albedog = groundAlbedoG
    groundAlbedoB = groundAlbedo.groundAlbedoB
    ground_albedob = groundAlbedoB

    useDegrees = BoolField()
    use_degrees = useDegrees

    elevation = FloatField()

    azimuth = FloatField()

    sunDirection = SunDirectionField()
    sun_direction = sunDirection
    sunDirectionX = sunDirection.sunDirectionX
    sun_directionx = sunDirectionX
    sunDirectionY = sunDirection.sunDirectionY
    sun_directiony = sunDirectionY
    sunDirectionZ = sunDirection.sunDirectionZ
    sun_directionz = sunDirectionZ

    enableSun = BoolField()
    enable_sun = enableSun

    enableSky = BoolField()
    enable_sky = enableSky

    sunSize = FloatField()
    sun_size = sunSize

    sunTint = SunTintField()
    sun_tint = sunTint
    sunTintR = sunTint.sunTintR
    sun_tintr = sunTintR
    sunTintG = sunTint.sunTintG
    sun_tintg = sunTintG
    sunTintB = sunTint.sunTintB
    sun_tintb = sunTintB

    skyTint = SkyTintField()
    sky_tint = skyTint
    skyTintR = skyTint.skyTintR
    sky_tintr = skyTintR
    skyTintG = skyTint.skyTintG
    sky_tintg = skyTintG
    skyTintB = skyTint.skyTintB
    sky_tintb = skyTintB

    intensity = FloatField()

    X = XField()
    XX = X.XX
    Xx = XX
    XY = X.XY
    Xy = XY
    XZ = X.XZ
    Xz = XZ

    Y = YField()
    YX = Y.YX
    Yx = YX
    YY = Y.YY
    Yy = YY
    YZ = Y.YZ
    Yz = YZ

    Z = ZField()
    ZX = Z.ZX
    Zx = ZX
    ZY = Z.ZY
    Zy = ZY
    ZZ = Z.ZZ
    Zz = ZZ
