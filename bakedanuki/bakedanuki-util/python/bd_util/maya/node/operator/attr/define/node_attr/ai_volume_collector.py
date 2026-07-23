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

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
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

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
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

    scatteringR = FloatField(default_value=1.0)
    scatteringr = scatteringR

    scatteringG = FloatField(default_value=1.0)
    scatteringg = scatteringG

    scatteringB = FloatField(default_value=1.0)
    scatteringb = scatteringB


class ScatteringAttrOperator(
    Float3CompoundBaseAttrOperator[ScatteringPlugOperator]
):
    __slots__ = ()

    scatteringR = FloatField(default_value=1.0)
    scatteringr = scatteringR

    scatteringG = FloatField(default_value=1.0)
    scatteringg = scatteringG

    scatteringB = FloatField(default_value=1.0)
    scatteringb = scatteringB


class ScatteringField(
    Float3CompoundBaseField[ScatteringAttrOperator, ScatteringPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScatteringAttrOperator
    PLUG_CLS = ScatteringPlugOperator

    scatteringR = FloatField(default_value=1.0)
    scatteringr = scatteringR

    scatteringG = FloatField(default_value=1.0)
    scatteringg = scatteringG

    scatteringB = FloatField(default_value=1.0)
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

    scatteringColorR = FloatField(default_value=1.0)
    scattering_colorr = scatteringColorR

    scatteringColorG = FloatField(default_value=1.0)
    scattering_colorg = scatteringColorG

    scatteringColorB = FloatField(default_value=1.0)
    scattering_colorb = scatteringColorB


class ScatteringColorAttrOperator(
    Float3CompoundBaseAttrOperator[ScatteringColorPlugOperator]
):
    __slots__ = ()

    scatteringColorR = FloatField(default_value=1.0)
    scattering_colorr = scatteringColorR

    scatteringColorG = FloatField(default_value=1.0)
    scattering_colorg = scatteringColorG

    scatteringColorB = FloatField(default_value=1.0)
    scattering_colorb = scatteringColorB


class ScatteringColorField(
    Float3CompoundBaseField[ScatteringColorAttrOperator, ScatteringColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScatteringColorAttrOperator
    PLUG_CLS = ScatteringColorPlugOperator

    scatteringColorR = FloatField(default_value=1.0)
    scattering_colorr = scatteringColorR

    scatteringColorG = FloatField(default_value=1.0)
    scattering_colorg = scatteringColorG

    scatteringColorB = FloatField(default_value=1.0)
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

    attenuationR = FloatField(default_value=1.0)
    attenuationr = attenuationR

    attenuationG = FloatField(default_value=1.0)
    attenuationg = attenuationG

    attenuationB = FloatField(default_value=1.0)
    attenuationb = attenuationB


class AttenuationAttrOperator(
    Float3CompoundBaseAttrOperator[AttenuationPlugOperator]
):
    __slots__ = ()

    attenuationR = FloatField(default_value=1.0)
    attenuationr = attenuationR

    attenuationG = FloatField(default_value=1.0)
    attenuationg = attenuationG

    attenuationB = FloatField(default_value=1.0)
    attenuationb = attenuationB


class AttenuationField(
    Float3CompoundBaseField[AttenuationAttrOperator, AttenuationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttenuationAttrOperator
    PLUG_CLS = AttenuationPlugOperator

    attenuationR = FloatField(default_value=1.0)
    attenuationr = attenuationR

    attenuationG = FloatField(default_value=1.0)
    attenuationg = attenuationG

    attenuationB = FloatField(default_value=1.0)
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

    attenuationColorR = FloatField(default_value=1.0)
    attenuation_colorr = attenuationColorR

    attenuationColorG = FloatField(default_value=1.0)
    attenuation_colorg = attenuationColorG

    attenuationColorB = FloatField(default_value=1.0)
    attenuation_colorb = attenuationColorB


class AttenuationColorAttrOperator(
    Float3CompoundBaseAttrOperator[AttenuationColorPlugOperator]
):
    __slots__ = ()

    attenuationColorR = FloatField(default_value=1.0)
    attenuation_colorr = attenuationColorR

    attenuationColorG = FloatField(default_value=1.0)
    attenuation_colorg = attenuationColorG

    attenuationColorB = FloatField(default_value=1.0)
    attenuation_colorb = attenuationColorB


class AttenuationColorField(
    Float3CompoundBaseField[AttenuationColorAttrOperator, AttenuationColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttenuationColorAttrOperator
    PLUG_CLS = AttenuationColorPlugOperator

    attenuationColorR = FloatField(default_value=1.0)
    attenuation_colorr = attenuationColorR

    attenuationColorG = FloatField(default_value=1.0)
    attenuation_colorg = attenuationColorG

    attenuationColorB = FloatField(default_value=1.0)
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

    emissionR = FloatField(default_value=0.0)
    emissionr = emissionR

    emissionG = FloatField(default_value=0.0)
    emissiong = emissionG

    emissionB = FloatField(default_value=0.0)
    emissionb = emissionB


class EmissionAttrOperator(
    Float3CompoundBaseAttrOperator[EmissionPlugOperator]
):
    __slots__ = ()

    emissionR = FloatField(default_value=0.0)
    emissionr = emissionR

    emissionG = FloatField(default_value=0.0)
    emissiong = emissionG

    emissionB = FloatField(default_value=0.0)
    emissionb = emissionB


class EmissionField(
    Float3CompoundBaseField[EmissionAttrOperator, EmissionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissionAttrOperator
    PLUG_CLS = EmissionPlugOperator

    emissionR = FloatField(default_value=0.0)
    emissionr = emissionR

    emissionG = FloatField(default_value=0.0)
    emissiong = emissionG

    emissionB = FloatField(default_value=0.0)
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

    emissionColorR = FloatField(default_value=1.0)
    emission_colorr = emissionColorR

    emissionColorG = FloatField(default_value=1.0)
    emission_colorg = emissionColorG

    emissionColorB = FloatField(default_value=1.0)
    emission_colorb = emissionColorB


class EmissionColorAttrOperator(
    Float3CompoundBaseAttrOperator[EmissionColorPlugOperator]
):
    __slots__ = ()

    emissionColorR = FloatField(default_value=1.0)
    emission_colorr = emissionColorR

    emissionColorG = FloatField(default_value=1.0)
    emission_colorg = emissionColorG

    emissionColorB = FloatField(default_value=1.0)
    emission_colorb = emissionColorB


class EmissionColorField(
    Float3CompoundBaseField[EmissionColorAttrOperator, EmissionColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissionColorAttrOperator
    PLUG_CLS = EmissionColorPlugOperator

    emissionColorR = FloatField(default_value=1.0)
    emission_colorr = emissionColorR

    emissionColorG = FloatField(default_value=1.0)
    emission_colorg = emissionColorG

    emissionColorB = FloatField(default_value=1.0)
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

    positionOffsetX = FloatField(default_value=0.0)
    position_offsetx = positionOffsetX

    positionOffsetY = FloatField(default_value=0.0)
    position_offsety = positionOffsetY

    positionOffsetZ = FloatField(default_value=0.0)
    position_offsetz = positionOffsetZ


class PositionOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[PositionOffsetPlugOperator]
):
    __slots__ = ()

    positionOffsetX = FloatField(default_value=0.0)
    position_offsetx = positionOffsetX

    positionOffsetY = FloatField(default_value=0.0)
    position_offsety = positionOffsetY

    positionOffsetZ = FloatField(default_value=0.0)
    position_offsetz = positionOffsetZ


class PositionOffsetField(
    Float3CompoundBaseField[PositionOffsetAttrOperator, PositionOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionOffsetAttrOperator
    PLUG_CLS = PositionOffsetPlugOperator

    positionOffsetX = FloatField(default_value=0.0)
    position_offsetx = positionOffsetX

    positionOffsetY = FloatField(default_value=0.0)
    position_offsety = positionOffsetY

    positionOffsetZ = FloatField(default_value=0.0)
    position_offsetz = positionOffsetZ
