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


class ColorPlugOperator(
    Float3CompoundBasePlugOperator["ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "colorr"),
        ("colorG", "colorg"),
        ("colorB", "colorb"),
    )

    colorR = FloatField()
    colorr = colorR

    colorG = FloatField()
    colorg = colorG

    colorB = FloatField()
    colorb = colorB


class ColorAttrOperator(
    Float3CompoundBaseAttrOperator[ColorPlugOperator]
):
    __slots__ = ()

    colorR = FloatField()
    colorr = colorR

    colorG = FloatField()
    colorg = colorG

    colorB = FloatField()
    colorb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField()
    colorr = colorR

    colorG = FloatField()
    colorg = colorG

    colorB = FloatField()
    colorb = colorB


class PalettePlugOperator(
    Float3CompoundBasePlugOperator["PaletteAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("paletteR", "paletter"),
        ("paletteG", "paletteg"),
        ("paletteB", "paletteb"),
    )

    paletteR = FloatField()
    paletter = paletteR

    paletteG = FloatField()
    paletteg = paletteG

    paletteB = FloatField()
    paletteb = paletteB


class PaletteAttrOperator(
    Float3CompoundBaseAttrOperator[PalettePlugOperator]
):
    __slots__ = ()

    paletteR = FloatField()
    paletter = paletteR

    paletteG = FloatField()
    paletteg = paletteG

    paletteB = FloatField()
    paletteb = paletteB


class PaletteField(
    Float3CompoundBaseField[PaletteAttrOperator, PalettePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PaletteAttrOperator
    PLUG_CLS = PalettePlugOperator

    paletteR = FloatField()
    paletter = paletteR

    paletteG = FloatField()
    paletteg = paletteG

    paletteB = FloatField()
    paletteb = paletteB
