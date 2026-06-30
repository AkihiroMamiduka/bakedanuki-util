# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "outr"),
        ("outColorG", "outg"),
        ("outColorB", "outb"),
    )

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
    outb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
    outb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
    outb = outColorB


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class ScatteringPlugOperator(
    Float3CompoundBasePlugOperator["ScatteringAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scatteringR", "scatteringr"),
        ("scatteringG", "scatteringg"),
        ("scatteringB", "scatteringb"),
    )

    scatteringR = FloatField()
    scatteringr = scatteringR

    scatteringG = FloatField()
    scatteringg = scatteringG

    scatteringB = FloatField()
    scatteringb = scatteringB


class ScatteringAttrOperator(
    Float3CompoundBaseAttrOperator[ScatteringPlugOperator]
):
    __slots__ = ()

    scatteringR = FloatField()
    scatteringr = scatteringR

    scatteringG = FloatField()
    scatteringg = scatteringG

    scatteringB = FloatField()
    scatteringb = scatteringB


class ScatteringField(
    Float3CompoundBaseField[ScatteringAttrOperator, ScatteringPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScatteringAttrOperator
    PLUG_CLS = ScatteringPlugOperator

    scatteringR = FloatField()
    scatteringr = scatteringR

    scatteringG = FloatField()
    scatteringg = scatteringG

    scatteringB = FloatField()
    scatteringb = scatteringB


class ScatteringColorPlugOperator(
    Float3CompoundBasePlugOperator["ScatteringColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scatteringColorR", "scattering_colorr"),
        ("scatteringColorG", "scattering_colorg"),
        ("scatteringColorB", "scattering_colorb"),
    )

    scatteringColorR = FloatField()
    scattering_colorr = scatteringColorR

    scatteringColorG = FloatField()
    scattering_colorg = scatteringColorG

    scatteringColorB = FloatField()
    scattering_colorb = scatteringColorB


class ScatteringColorAttrOperator(
    Float3CompoundBaseAttrOperator[ScatteringColorPlugOperator]
):
    __slots__ = ()

    scatteringColorR = FloatField()
    scattering_colorr = scatteringColorR

    scatteringColorG = FloatField()
    scattering_colorg = scatteringColorG

    scatteringColorB = FloatField()
    scattering_colorb = scatteringColorB


class ScatteringColorField(
    Float3CompoundBaseField[ScatteringColorAttrOperator, ScatteringColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScatteringColorAttrOperator
    PLUG_CLS = ScatteringColorPlugOperator

    scatteringColorR = FloatField()
    scattering_colorr = scatteringColorR

    scatteringColorG = FloatField()
    scattering_colorg = scatteringColorG

    scatteringColorB = FloatField()
    scattering_colorb = scatteringColorB


class AttenuationPlugOperator(
    Float3CompoundBasePlugOperator["AttenuationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("attenuationR", "attenuationr"),
        ("attenuationG", "attenuationg"),
        ("attenuationB", "attenuationb"),
    )

    attenuationR = FloatField()
    attenuationr = attenuationR

    attenuationG = FloatField()
    attenuationg = attenuationG

    attenuationB = FloatField()
    attenuationb = attenuationB


class AttenuationAttrOperator(
    Float3CompoundBaseAttrOperator[AttenuationPlugOperator]
):
    __slots__ = ()

    attenuationR = FloatField()
    attenuationr = attenuationR

    attenuationG = FloatField()
    attenuationg = attenuationG

    attenuationB = FloatField()
    attenuationb = attenuationB


class AttenuationField(
    Float3CompoundBaseField[AttenuationAttrOperator, AttenuationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttenuationAttrOperator
    PLUG_CLS = AttenuationPlugOperator

    attenuationR = FloatField()
    attenuationr = attenuationR

    attenuationG = FloatField()
    attenuationg = attenuationG

    attenuationB = FloatField()
    attenuationb = attenuationB


class AttenuationColorPlugOperator(
    Float3CompoundBasePlugOperator["AttenuationColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("attenuationColorR", "attenuation_colorr"),
        ("attenuationColorG", "attenuation_colorg"),
        ("attenuationColorB", "attenuation_colorb"),
    )

    attenuationColorR = FloatField()
    attenuation_colorr = attenuationColorR

    attenuationColorG = FloatField()
    attenuation_colorg = attenuationColorG

    attenuationColorB = FloatField()
    attenuation_colorb = attenuationColorB


class AttenuationColorAttrOperator(
    Float3CompoundBaseAttrOperator[AttenuationColorPlugOperator]
):
    __slots__ = ()

    attenuationColorR = FloatField()
    attenuation_colorr = attenuationColorR

    attenuationColorG = FloatField()
    attenuation_colorg = attenuationColorG

    attenuationColorB = FloatField()
    attenuation_colorb = attenuationColorB


class AttenuationColorField(
    Float3CompoundBaseField[AttenuationColorAttrOperator, AttenuationColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttenuationColorAttrOperator
    PLUG_CLS = AttenuationColorPlugOperator

    attenuationColorR = FloatField()
    attenuation_colorr = attenuationColorR

    attenuationColorG = FloatField()
    attenuation_colorg = attenuationColorG

    attenuationColorB = FloatField()
    attenuation_colorb = attenuationColorB


class EmissionPlugOperator(
    Float3CompoundBasePlugOperator["EmissionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emissionR", "emissionr"),
        ("emissionG", "emissiong"),
        ("emissionB", "emissionb"),
    )

    emissionR = FloatField()
    emissionr = emissionR

    emissionG = FloatField()
    emissiong = emissionG

    emissionB = FloatField()
    emissionb = emissionB


class EmissionAttrOperator(
    Float3CompoundBaseAttrOperator[EmissionPlugOperator]
):
    __slots__ = ()

    emissionR = FloatField()
    emissionr = emissionR

    emissionG = FloatField()
    emissiong = emissionG

    emissionB = FloatField()
    emissionb = emissionB


class EmissionField(
    Float3CompoundBaseField[EmissionAttrOperator, EmissionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissionAttrOperator
    PLUG_CLS = EmissionPlugOperator

    emissionR = FloatField()
    emissionr = emissionR

    emissionG = FloatField()
    emissiong = emissionG

    emissionB = FloatField()
    emissionb = emissionB


class EmissionColorPlugOperator(
    Float3CompoundBasePlugOperator["EmissionColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emissionColorR", "emission_colorr"),
        ("emissionColorG", "emission_colorg"),
        ("emissionColorB", "emission_colorb"),
    )

    emissionColorR = FloatField()
    emission_colorr = emissionColorR

    emissionColorG = FloatField()
    emission_colorg = emissionColorG

    emissionColorB = FloatField()
    emission_colorb = emissionColorB


class EmissionColorAttrOperator(
    Float3CompoundBaseAttrOperator[EmissionColorPlugOperator]
):
    __slots__ = ()

    emissionColorR = FloatField()
    emission_colorr = emissionColorR

    emissionColorG = FloatField()
    emission_colorg = emissionColorG

    emissionColorB = FloatField()
    emission_colorb = emissionColorB


class EmissionColorField(
    Float3CompoundBaseField[EmissionColorAttrOperator, EmissionColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissionColorAttrOperator
    PLUG_CLS = EmissionColorPlugOperator

    emissionColorR = FloatField()
    emission_colorr = emissionColorR

    emissionColorG = FloatField()
    emission_colorg = emissionColorG

    emissionColorB = FloatField()
    emission_colorb = emissionColorB


class PositionOffsetPlugOperator(
    Float3CompoundBasePlugOperator["PositionOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionOffsetX", "position_offsetx"),
        ("positionOffsetY", "position_offsety"),
        ("positionOffsetZ", "position_offsetz"),
    )

    positionOffsetX = FloatField()
    position_offsetx = positionOffsetX

    positionOffsetY = FloatField()
    position_offsety = positionOffsetY

    positionOffsetZ = FloatField()
    position_offsetz = positionOffsetZ


class PositionOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[PositionOffsetPlugOperator]
):
    __slots__ = ()

    positionOffsetX = FloatField()
    position_offsetx = positionOffsetX

    positionOffsetY = FloatField()
    position_offsety = positionOffsetY

    positionOffsetZ = FloatField()
    position_offsetz = positionOffsetZ


class PositionOffsetField(
    Float3CompoundBaseField[PositionOffsetAttrOperator, PositionOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionOffsetAttrOperator
    PLUG_CLS = PositionOffsetPlugOperator

    positionOffsetX = FloatField()
    position_offsetx = positionOffsetX

    positionOffsetY = FloatField()
    position_offsety = positionOffsetY

    positionOffsetZ = FloatField()
    position_offsetz = positionOffsetZ
