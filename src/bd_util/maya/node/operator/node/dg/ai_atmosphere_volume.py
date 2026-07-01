# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_atmosphere_volume import (
    OutColorField,
    OutTransparencyField,
    RgbAttenuationField,
    RgbDensityField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class AiAtmosphereVolume(DG):
    __slots__ = ()

    NODE_TYPE = "aiAtmosphereVolume"

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

    density = FloatField()

    samples = LongField()

    eccentricity = FloatField()

    attenuation = FloatField()

    affectCamera = FloatField()
    affect_camera = affectCamera

    affectDiffuse = FloatField()
    affect_diffuse = affectDiffuse

    affectSpecular = FloatField()
    affect_specular = affectSpecular

    rgbDensity = RgbDensityField()
    rgb_density = rgbDensity
    rgbDensityR = rgbDensity.rgbDensityR
    rgb_densityr = rgbDensityR
    rgbDensityG = rgbDensity.rgbDensityG
    rgb_densityg = rgbDensityG
    rgbDensityB = rgbDensity.rgbDensityB
    rgb_densityb = rgbDensityB

    rgbAttenuation = RgbAttenuationField()
    rgb_attenuation = rgbAttenuation
    rgbAttenuationR = rgbAttenuation.rgbAttenuationR
    rgb_attenuationr = rgbAttenuationR
    rgbAttenuationG = rgbAttenuation.rgbAttenuationG
    rgb_attenuationg = rgbAttenuationG
    rgbAttenuationB = rgbAttenuation.rgbAttenuationB
    rgb_attenuationb = rgbAttenuationB
