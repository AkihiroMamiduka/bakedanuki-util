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

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    turbidity = FloatField(default_value=3.0, soft_min_value=1.0, soft_max_value=10.0)

    groundAlbedo = GroundAlbedoField(default_value=(0.10000000149011612, 0.10000000149011612, 0.10000000149011612))
    ground_albedo = groundAlbedo
    groundAlbedoR = groundAlbedo.groundAlbedoR
    ground_albedor = groundAlbedoR
    groundAlbedoG = groundAlbedo.groundAlbedoG
    ground_albedog = groundAlbedoG
    groundAlbedoB = groundAlbedo.groundAlbedoB
    ground_albedob = groundAlbedoB

    useDegrees = BoolField(default_value=True)
    use_degrees = useDegrees

    elevation = FloatField(default_value=45.0, soft_min_value=0.0, soft_max_value=90.0)

    azimuth = FloatField(default_value=90.0, soft_min_value=0.0, soft_max_value=360.0)

    sunDirection = SunDirectionField(default_value=(0.0, 1.0, 0.0))
    sun_direction = sunDirection
    sunDirectionX = sunDirection.sunDirectionX
    sun_directionx = sunDirectionX
    sunDirectionY = sunDirection.sunDirectionY
    sun_directiony = sunDirectionY
    sunDirectionZ = sunDirection.sunDirectionZ
    sun_directionz = sunDirectionZ

    enableSun = BoolField(default_value=True)
    enable_sun = enableSun

    enableSky = BoolField(default_value=True)
    enable_sky = enableSky

    sunSize = FloatField(default_value=0.5099999904632568, soft_min_value=0.10000000149011612, soft_max_value=5.0)
    sun_size = sunSize

    sunTint = SunTintField(default_value=(1.0, 1.0, 1.0))
    sun_tint = sunTint
    sunTintR = sunTint.sunTintR
    sun_tintr = sunTintR
    sunTintG = sunTint.sunTintG
    sun_tintg = sunTintG
    sunTintB = sunTint.sunTintB
    sun_tintb = sunTintB

    skyTint = SkyTintField(default_value=(1.0, 1.0, 1.0))
    sky_tint = skyTint
    skyTintR = skyTint.skyTintR
    sky_tintr = skyTintR
    skyTintG = skyTint.skyTintG
    sky_tintg = skyTintG
    skyTintB = skyTint.skyTintB
    sky_tintb = skyTintB

    intensity = FloatField(default_value=1.0, soft_min_value=0.10000000149011612, soft_max_value=10.0)

    X = XField(default_value=(1.0, 0.0, 0.0))
    XX = X.XX
    Xx = XX
    XY = X.XY
    Xy = XY
    XZ = X.XZ
    Xz = XZ

    Y = YField(default_value=(0.0, 1.0, 0.0))
    YX = Y.YX
    Yx = YX
    YY = Y.YY
    Yy = YY
    YZ = Y.YZ
    Yz = YZ

    Z = ZField(default_value=(0.0, 0.0, 1.0))
    ZX = Z.ZX
    Zx = ZX
    ZY = Z.ZY
    Zy = ZY
    ZZ = Z.ZZ
    Zz = ZZ
