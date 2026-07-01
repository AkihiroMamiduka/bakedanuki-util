# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_standard_volume import (
    DisplacementField,
    EmissionColorField,
    OutColorField,
    OutTransparencyField,
    ScatterColorField,
    TransparentField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class EmissionModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    CHANNEL = 1
    DENSITY = 2
    BLACKBODY = 3


class EmissionModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    CHANNEL = 1
    DENSITY = 2
    BLACKBODY = 3

    NAME_MAP = {
        NONE: "none",
        CHANNEL: "channel",
        DENSITY: "density",
        BLACKBODY: "blackbody",
    }


class EmissionModeEnumField(
    EnumField[EmissionModeEnumAttrOperator, EmissionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissionModeEnumAttrOperator
    PLUG_CLS = EmissionModeEnumPlugOperator


class EmissionScalingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    OPACITY = 1
    THERMODYNAMIC = 2


class EmissionScalingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    OPACITY = 1
    THERMODYNAMIC = 2

    NAME_MAP = {
        NONE: "none",
        OPACITY: "opacity",
        THERMODYNAMIC: "thermodynamic",
    }


class EmissionScalingEnumField(
    EnumField[EmissionScalingEnumAttrOperator, EmissionScalingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissionScalingEnumAttrOperator
    PLUG_CLS = EmissionScalingEnumPlugOperator


class InterpolationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLOSEST = 0
    TRILINEAR = 1
    TRICUBIC = 2


class InterpolationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CLOSEST = 0
    TRILINEAR = 1
    TRICUBIC = 2

    NAME_MAP = {
        CLOSEST: "closest",
        TRILINEAR: "trilinear",
        TRICUBIC: "tricubic",
    }


class InterpolationEnumField(
    EnumField[InterpolationEnumAttrOperator, InterpolationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InterpolationEnumAttrOperator
    PLUG_CLS = InterpolationEnumPlugOperator


class AiStandardVolume(DG):
    __slots__ = ()

    NODE_TYPE = "aiStandardVolume"

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

    densityChannel = DataStringField()
    density_channel = densityChannel

    scatter = FloatField()

    scatterColor = ScatterColorField()
    scatter_color = scatterColor
    scatterColorR = scatterColor.scatterColorR
    scatter_colorr = scatterColorR
    scatterColorG = scatterColor.scatterColorG
    scatter_colorg = scatterColorG
    scatterColorB = scatterColor.scatterColorB
    scatter_colorb = scatterColorB

    scatterColorChannel = DataStringField()
    scatter_color_channel = scatterColorChannel

    scatterAnisotropy = FloatField()
    scatter_anisotropy = scatterAnisotropy

    scatterSecondaryAnisotropy = FloatField()
    scatter_secondary_anisotropy = scatterSecondaryAnisotropy

    scatterSecondaryAnisotropyMix = FloatField()
    scatter_secondary_anisotropy_mix = scatterSecondaryAnisotropyMix

    transparent = TransparentField()
    transparentR = transparent.transparentR
    transparentr = transparentR
    transparentG = transparent.transparentG
    transparentg = transparentG
    transparentB = transparent.transparentB
    transparentb = transparentB

    transparentDepth = FloatField()
    transparent_depth = transparentDepth

    transparentChannel = DataStringField()
    transparent_channel = transparentChannel

    emissionMode = EmissionModeEnumField()
    emission_mode = emissionMode

    emissionScaling = EmissionScalingEnumField()
    emission_scaling = emissionScaling

    emission = FloatField()

    emissionColor = EmissionColorField()
    emission_color = emissionColor
    emissionColorR = emissionColor.emissionColorR
    emission_colorr = emissionColorR
    emissionColorG = emissionColor.emissionColorG
    emission_colorg = emissionColorG
    emissionColorB = emissionColor.emissionColorB
    emission_colorb = emissionColorB

    emissionChannel = DataStringField()
    emission_channel = emissionChannel

    temperature = FloatField()

    temperatureChannel = DataStringField()
    temperature_channel = temperatureChannel

    blackbodyKelvin = FloatField()
    blackbody_kelvin = blackbodyKelvin

    blackbodyIntensity = FloatField()
    blackbody_intensity = blackbodyIntensity

    blackbodyContrast = FloatField()
    blackbody_contrast = blackbodyContrast

    displacement = DisplacementField()
    displacementX = displacement.displacementX
    displacementx = displacementX
    displacementY = displacement.displacementY
    displacementy = displacementY
    displacementZ = displacement.displacementZ
    displacementz = displacementZ

    interpolation = InterpolationEnumField()
