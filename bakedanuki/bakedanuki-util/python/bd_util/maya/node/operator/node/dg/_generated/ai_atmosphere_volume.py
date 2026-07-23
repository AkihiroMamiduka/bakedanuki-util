# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_atmosphere_volume import (
    OutColorField,
    OutTransparencyField,
    RgbAttenuationField,
    RgbDensityField,
)
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField


class _GeneratedAiAtmosphereVolume(DG):
    __slots__ = ()

    NODE_TYPE = "aiAtmosphereVolume"

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

    density = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    samples = LongField(default_value=5, min_value=1, max_value=100, soft_max_value=64)

    eccentricity = FloatField(default_value=0.0, min_value=-0.8999999761581421, max_value=0.8999999761581421)

    attenuation = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    affectCamera = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    affect_camera = affectCamera

    affectDiffuse = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    affect_diffuse = affectDiffuse

    affectSpecular = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    affect_specular = affectSpecular

    rgbDensity = RgbDensityField(default_value=(1.0, 1.0, 1.0))
    rgb_density = rgbDensity
    rgbDensityR = rgbDensity.rgbDensityR
    rgb_densityr = rgbDensityR
    rgbDensityG = rgbDensity.rgbDensityG
    rgb_densityg = rgbDensityG
    rgbDensityB = rgbDensity.rgbDensityB
    rgb_densityb = rgbDensityB

    rgbAttenuation = RgbAttenuationField(default_value=(1.0, 1.0, 1.0))
    rgb_attenuation = rgbAttenuation
    rgbAttenuationR = rgbAttenuation.rgbAttenuationR
    rgb_attenuationr = rgbAttenuationR
    rgbAttenuationG = rgbAttenuation.rgbAttenuationG
    rgb_attenuationg = rgbAttenuationG
    rgbAttenuationB = rgbAttenuation.rgbAttenuationB
    rgb_attenuationb = rgbAttenuationB
