# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_volume_collector import (
    AttenuationColorField,
    AttenuationField,
    EmissionColorField,
    EmissionField,
    OutColorField,
    OutTransparencyField,
    PositionOffsetField,
    ScatteringColorField,
    ScatteringField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class ScatteringSourceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PARAMETER = 0
    CHANNEL = 1


class ScatteringSourceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PARAMETER = 0
    CHANNEL = 1

    NAME_MAP = {
        PARAMETER: "parameter",
        CHANNEL: "channel",
    }


class ScatteringSourceEnumField(
    EnumField[ScatteringSourceEnumAttrOperator, ScatteringSourceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScatteringSourceEnumAttrOperator
    PLUG_CLS = ScatteringSourceEnumPlugOperator


class AttenuationSourceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PARAMETER = 0
    CHANNEL = 1
    SCATTERING = 2


class AttenuationSourceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PARAMETER = 0
    CHANNEL = 1
    SCATTERING = 2

    NAME_MAP = {
        PARAMETER: "parameter",
        CHANNEL: "channel",
        SCATTERING: "scattering",
    }


class AttenuationSourceEnumField(
    EnumField[AttenuationSourceEnumAttrOperator, AttenuationSourceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttenuationSourceEnumAttrOperator
    PLUG_CLS = AttenuationSourceEnumPlugOperator


class AttenuationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ABSORPTION = 0
    EXTINCTION = 1


class AttenuationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ABSORPTION = 0
    EXTINCTION = 1

    NAME_MAP = {
        ABSORPTION: "absorption",
        EXTINCTION: "extinction",
    }


class AttenuationModeEnumField(
    EnumField[AttenuationModeEnumAttrOperator, AttenuationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttenuationModeEnumAttrOperator
    PLUG_CLS = AttenuationModeEnumPlugOperator


class EmissionSourceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PARAMETER = 0
    CHANNEL = 1


class EmissionSourceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PARAMETER = 0
    CHANNEL = 1

    NAME_MAP = {
        PARAMETER: "parameter",
        CHANNEL: "channel",
    }


class EmissionSourceEnumField(
    EnumField[EmissionSourceEnumAttrOperator, EmissionSourceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissionSourceEnumAttrOperator
    PLUG_CLS = EmissionSourceEnumPlugOperator


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


class AiVolumeCollector(DG):
    __slots__ = ()

    NODE_TYPE = "aiVolumeCollector"

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

    scatteringSource = ScatteringSourceEnumField()
    scattering_source = scatteringSource

    scattering = ScatteringField()
    scatteringR = scattering.scatteringR
    scatteringr = scatteringR
    scatteringG = scattering.scatteringG
    scatteringg = scatteringG
    scatteringB = scattering.scatteringB
    scatteringb = scatteringB

    scatteringChannel = DataStringField()
    scattering_channel = scatteringChannel

    scatteringColor = ScatteringColorField()
    scattering_color = scatteringColor
    scatteringColorR = scatteringColor.scatteringColorR
    scattering_colorr = scatteringColorR
    scatteringColorG = scatteringColor.scatteringColorG
    scattering_colorg = scatteringColorG
    scatteringColorB = scatteringColor.scatteringColorB
    scattering_colorb = scatteringColorB

    scatteringIntensity = FloatField()
    scattering_intensity = scatteringIntensity

    anisotropy = FloatField()

    attenuationSource = AttenuationSourceEnumField()
    attenuation_source = attenuationSource

    attenuation = AttenuationField()
    attenuationR = attenuation.attenuationR
    attenuationr = attenuationR
    attenuationG = attenuation.attenuationG
    attenuationg = attenuationG
    attenuationB = attenuation.attenuationB
    attenuationb = attenuationB

    attenuationChannel = DataStringField()
    attenuation_channel = attenuationChannel

    attenuationColor = AttenuationColorField()
    attenuation_color = attenuationColor
    attenuationColorR = attenuationColor.attenuationColorR
    attenuation_colorr = attenuationColorR
    attenuationColorG = attenuationColor.attenuationColorG
    attenuation_colorg = attenuationColorG
    attenuationColorB = attenuationColor.attenuationColorB
    attenuation_colorb = attenuationColorB

    attenuationIntensity = FloatField()
    attenuation_intensity = attenuationIntensity

    attenuationMode = AttenuationModeEnumField()
    attenuation_mode = attenuationMode

    emissionSource = EmissionSourceEnumField()
    emission_source = emissionSource

    emission = EmissionField()
    emissionR = emission.emissionR
    emissionr = emissionR
    emissionG = emission.emissionG
    emissiong = emissionG
    emissionB = emission.emissionB
    emissionb = emissionB

    emissionChannel = DataStringField()
    emission_channel = emissionChannel

    emissionColor = EmissionColorField()
    emission_color = emissionColor
    emissionColorR = emissionColor.emissionColorR
    emission_colorr = emissionColorR
    emissionColorG = emissionColor.emissionColorG
    emission_colorg = emissionColorG
    emissionColorB = emissionColor.emissionColorB
    emission_colorb = emissionColorB

    emissionIntensity = FloatField()
    emission_intensity = emissionIntensity

    positionOffset = PositionOffsetField()
    position_offset = positionOffset
    positionOffsetX = positionOffset.positionOffsetX
    position_offsetx = positionOffsetX
    positionOffsetY = positionOffset.positionOffsetY
    position_offsety = positionOffsetY
    positionOffsetZ = positionOffset.positionOffsetZ
    position_offsetz = positionOffsetZ

    interpolation = InterpolationEnumField()
