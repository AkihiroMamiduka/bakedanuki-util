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


class ScalePlugOperator(
    Float3CompoundBasePlugOperator["ScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleX", "scalex"),
        ("scaleY", "scaley"),
        ("scaleZ", "scalez"),
    )

    scaleX = FloatField()
    scalex = scaleX

    scaleY = FloatField()
    scaley = scaleY

    scaleZ = FloatField()
    scalez = scaleZ


class ScaleAttrOperator(
    Float3CompoundBaseAttrOperator[ScalePlugOperator]
):
    __slots__ = ()

    scaleX = FloatField()
    scalex = scaleX

    scaleY = FloatField()
    scaley = scaleY

    scaleZ = FloatField()
    scalez = scaleZ


class ScaleField(
    Float3CompoundBaseField[ScaleAttrOperator, ScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAttrOperator
    PLUG_CLS = ScalePlugOperator

    scaleX = FloatField()
    scalex = scaleX

    scaleY = FloatField()
    scaley = scaleY

    scaleZ = FloatField()
    scalez = scaleZ


class OffsetPlugOperator(
    Float3CompoundBasePlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetX", "offsetx"),
        ("offsetY", "offsety"),
        ("offsetZ", "offsetz"),
    )

    offsetX = FloatField()
    offsetx = offsetX

    offsetY = FloatField()
    offsety = offsetY

    offsetZ = FloatField()
    offsetz = offsetZ


class OffsetAttrOperator(
    Float3CompoundBaseAttrOperator[OffsetPlugOperator]
):
    __slots__ = ()

    offsetX = FloatField()
    offsetx = offsetX

    offsetY = FloatField()
    offsety = offsetY

    offsetZ = FloatField()
    offsetz = offsetZ


class OffsetField(
    Float3CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetX = FloatField()
    offsetx = offsetX

    offsetY = FloatField()
    offsety = offsetY

    offsetZ = FloatField()
    offsetz = offsetZ


class PPlugOperator(
    Float3CompoundBasePlugOperator["PAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("PX", "Px"),
        ("PY", "Py"),
        ("PZ", "Pz"),
    )

    PX = FloatField()
    Px = PX

    PY = FloatField()
    Py = PY

    PZ = FloatField()
    Pz = PZ


class PAttrOperator(
    Float3CompoundBaseAttrOperator[PPlugOperator]
):
    __slots__ = ()

    PX = FloatField()
    Px = PX

    PY = FloatField()
    Py = PY

    PZ = FloatField()
    Pz = PZ


class PField(
    Float3CompoundBaseField[PAttrOperator, PPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PAttrOperator
    PLUG_CLS = PPlugOperator

    PX = FloatField()
    Px = PX

    PY = FloatField()
    Py = PY

    PZ = FloatField()
    Pz = PZ


class Color1PlugOperator(
    Float3CompoundBasePlugOperator["Color1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color1R", "color1r"),
        ("color1G", "color1g"),
        ("color1B", "color1b"),
    )

    color1R = FloatField()
    color1r = color1R

    color1G = FloatField()
    color1g = color1G

    color1B = FloatField()
    color1b = color1B


class Color1AttrOperator(
    Float3CompoundBaseAttrOperator[Color1PlugOperator]
):
    __slots__ = ()

    color1R = FloatField()
    color1r = color1R

    color1G = FloatField()
    color1g = color1G

    color1B = FloatField()
    color1b = color1B


class Color1Field(
    Float3CompoundBaseField[Color1AttrOperator, Color1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Color1AttrOperator
    PLUG_CLS = Color1PlugOperator

    color1R = FloatField()
    color1r = color1R

    color1G = FloatField()
    color1g = color1G

    color1B = FloatField()
    color1b = color1B


class Color2PlugOperator(
    Float3CompoundBasePlugOperator["Color2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color2R", "color2r"),
        ("color2G", "color2g"),
        ("color2B", "color2b"),
    )

    color2R = FloatField()
    color2r = color2R

    color2G = FloatField()
    color2g = color2G

    color2B = FloatField()
    color2b = color2B


class Color2AttrOperator(
    Float3CompoundBaseAttrOperator[Color2PlugOperator]
):
    __slots__ = ()

    color2R = FloatField()
    color2r = color2R

    color2G = FloatField()
    color2g = color2G

    color2B = FloatField()
    color2b = color2B


class Color2Field(
    Float3CompoundBaseField[Color2AttrOperator, Color2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Color2AttrOperator
    PLUG_CLS = Color2PlugOperator

    color2R = FloatField()
    color2r = color2R

    color2G = FloatField()
    color2g = color2G

    color2B = FloatField()
    color2b = color2B
