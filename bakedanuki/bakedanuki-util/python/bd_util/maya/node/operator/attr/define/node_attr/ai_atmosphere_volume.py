# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
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
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
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


class RgbDensityPlugOperator(
    Float3CompoundBasePlugOperator["RgbDensityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rgbDensityR", "rgb_densityr"),
        ("rgbDensityG", "rgb_densityg"),
        ("rgbDensityB", "rgb_densityb"),
    )

    rgbDensityR = FloatField(default_value=1.0)
    rgb_densityr = rgbDensityR

    rgbDensityG = FloatField(default_value=1.0)
    rgb_densityg = rgbDensityG

    rgbDensityB = FloatField(default_value=1.0)
    rgb_densityb = rgbDensityB


class RgbDensityAttrOperator(
    Float3CompoundBaseAttrOperator[RgbDensityPlugOperator]
):
    __slots__ = ()

    rgbDensityR = FloatField(default_value=1.0)
    rgb_densityr = rgbDensityR

    rgbDensityG = FloatField(default_value=1.0)
    rgb_densityg = rgbDensityG

    rgbDensityB = FloatField(default_value=1.0)
    rgb_densityb = rgbDensityB


class RgbDensityField(
    Float3CompoundBaseField[RgbDensityAttrOperator, RgbDensityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RgbDensityAttrOperator
    PLUG_CLS = RgbDensityPlugOperator

    rgbDensityR = FloatField(default_value=1.0)
    rgb_densityr = rgbDensityR

    rgbDensityG = FloatField(default_value=1.0)
    rgb_densityg = rgbDensityG

    rgbDensityB = FloatField(default_value=1.0)
    rgb_densityb = rgbDensityB


class RgbAttenuationPlugOperator(
    Float3CompoundBasePlugOperator["RgbAttenuationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rgbAttenuationR", "rgb_attenuationr"),
        ("rgbAttenuationG", "rgb_attenuationg"),
        ("rgbAttenuationB", "rgb_attenuationb"),
    )

    rgbAttenuationR = FloatField(default_value=1.0)
    rgb_attenuationr = rgbAttenuationR

    rgbAttenuationG = FloatField(default_value=1.0)
    rgb_attenuationg = rgbAttenuationG

    rgbAttenuationB = FloatField(default_value=1.0)
    rgb_attenuationb = rgbAttenuationB


class RgbAttenuationAttrOperator(
    Float3CompoundBaseAttrOperator[RgbAttenuationPlugOperator]
):
    __slots__ = ()

    rgbAttenuationR = FloatField(default_value=1.0)
    rgb_attenuationr = rgbAttenuationR

    rgbAttenuationG = FloatField(default_value=1.0)
    rgb_attenuationg = rgbAttenuationG

    rgbAttenuationB = FloatField(default_value=1.0)
    rgb_attenuationb = rgbAttenuationB


class RgbAttenuationField(
    Float3CompoundBaseField[
        RgbAttenuationAttrOperator, RgbAttenuationPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RgbAttenuationAttrOperator
    PLUG_CLS = RgbAttenuationPlugOperator

    rgbAttenuationR = FloatField(default_value=1.0)
    rgb_attenuationr = rgbAttenuationR

    rgbAttenuationG = FloatField(default_value=1.0)
    rgb_attenuationg = rgbAttenuationG

    rgbAttenuationB = FloatField(default_value=1.0)
    rgb_attenuationb = rgbAttenuationB
