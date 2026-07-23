# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_standard_volume import (
    DisplacementField,
    EmissionColorField,
    OutColorField,
    OutTransparencyField,
    ScatterColorField,
    TransparentField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


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


class _GeneratedAiStandardVolume(DG):
    __slots__ = ()

    NODE_TYPE = "aiStandardVolume"

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

    density = FloatField(default_value=1.0, min_value=0.0, soft_max_value=5.0)

    densityChannel = DataStringField()
    density_channel = densityChannel

    scatter = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    scatterColor = ScatterColorField(default_value=(0.5, 0.5, 0.5))
    scatter_color = scatterColor
    scatterColorR = scatterColor.scatterColorR
    scatter_colorr = scatterColorR
    scatterColorG = scatterColor.scatterColorG
    scatter_colorg = scatterColorG
    scatterColorB = scatterColor.scatterColorB
    scatter_colorb = scatterColorB

    scatterColorChannel = DataStringField()
    scatter_color_channel = scatterColorChannel

    scatterAnisotropy = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    scatter_anisotropy = scatterAnisotropy

    scatterSecondaryAnisotropy = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    scatter_secondary_anisotropy = scatterSecondaryAnisotropy

    scatterSecondaryAnisotropyMix = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    scatter_secondary_anisotropy_mix = scatterSecondaryAnisotropyMix

    transparent = TransparentField(default_value=(0.3678794503211975, 0.3678794503211975, 0.3678794503211975))
    transparentR = transparent.transparentR
    transparentr = transparentR
    transparentG = transparent.transparentG
    transparentg = transparentG
    transparentB = transparent.transparentB
    transparentb = transparentB

    transparentDepth = FloatField(default_value=1.0)
    transparent_depth = transparentDepth

    transparentChannel = DataStringField()
    transparent_channel = transparentChannel

    emissionMode = EmissionModeEnumField(default_value=3)
    emission_mode = emissionMode

    emissionScaling = EmissionScalingEnumField(default_value=0)
    emission_scaling = emissionScaling

    emission = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)

    emissionColor = EmissionColorField(default_value=(1.0, 1.0, 1.0))
    emission_color = emissionColor
    emissionColorR = emissionColor.emissionColorR
    emission_colorr = emissionColorR
    emissionColorG = emissionColor.emissionColorG
    emission_colorg = emissionColorG
    emissionColorB = emissionColor.emissionColorB
    emission_colorb = emissionColorB

    emissionChannel = DataStringField()
    emission_channel = emissionChannel

    temperature = FloatField(default_value=1.0)

    temperatureChannel = DataStringField()
    temperature_channel = temperatureChannel

    blackbodyKelvin = FloatField(default_value=5000.0, min_value=0.0, soft_max_value=20000.0)
    blackbody_kelvin = blackbodyKelvin

    blackbodyIntensity = FloatField(default_value=1.0, min_value=0.0, soft_max_value=100.0)
    blackbody_intensity = blackbodyIntensity

    blackbodyContrast = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    blackbody_contrast = blackbodyContrast

    displacement = DisplacementField(default_value=(0.0, 0.0, 0.0))
    displacementX = displacement.displacementX
    displacementx = displacementX
    displacementY = displacement.displacementY
    displacementy = displacementY
    displacementZ = displacement.displacementZ
    displacementz = displacementZ

    interpolation = InterpolationEnumField(default_value=1)
