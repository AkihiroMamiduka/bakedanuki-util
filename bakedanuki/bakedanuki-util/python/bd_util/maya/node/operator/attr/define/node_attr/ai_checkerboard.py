# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
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


class Color1PlugOperator(Float3CompoundBasePlugOperator["Color1AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color1R", "color1r"),
        ("color1G", "color1g"),
        ("color1B", "color1b"),
    )

    color1R = FloatField(default_value=1.0)
    color1r = color1R

    color1G = FloatField(default_value=1.0)
    color1g = color1G

    color1B = FloatField(default_value=1.0)
    color1b = color1B


class Color1AttrOperator(Float3CompoundBaseAttrOperator[Color1PlugOperator]):
    __slots__ = ()

    color1R = FloatField(default_value=1.0)
    color1r = color1R

    color1G = FloatField(default_value=1.0)
    color1g = color1G

    color1B = FloatField(default_value=1.0)
    color1b = color1B


class Color1Field(
    Float3CompoundBaseField[Color1AttrOperator, Color1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Color1AttrOperator
    PLUG_CLS = Color1PlugOperator

    color1R = FloatField(default_value=1.0)
    color1r = color1R

    color1G = FloatField(default_value=1.0)
    color1g = color1G

    color1B = FloatField(default_value=1.0)
    color1b = color1B


class Color2PlugOperator(Float3CompoundBasePlugOperator["Color2AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color2R", "color2r"),
        ("color2G", "color2g"),
        ("color2B", "color2b"),
    )

    color2R = FloatField(default_value=0.0)
    color2r = color2R

    color2G = FloatField(default_value=0.0)
    color2g = color2G

    color2B = FloatField(default_value=0.0)
    color2b = color2B


class Color2AttrOperator(Float3CompoundBaseAttrOperator[Color2PlugOperator]):
    __slots__ = ()

    color2R = FloatField(default_value=0.0)
    color2r = color2R

    color2G = FloatField(default_value=0.0)
    color2g = color2G

    color2B = FloatField(default_value=0.0)
    color2b = color2B


class Color2Field(
    Float3CompoundBaseField[Color2AttrOperator, Color2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Color2AttrOperator
    PLUG_CLS = Color2PlugOperator

    color2R = FloatField(default_value=0.0)
    color2r = color2R

    color2G = FloatField(default_value=0.0)
    color2g = color2G

    color2B = FloatField(default_value=0.0)
    color2b = color2B
