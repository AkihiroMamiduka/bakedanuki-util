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


class ScalePlugOperator(Float3CompoundBasePlugOperator["ScaleAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleX", "scalex"),
        ("scaleY", "scaley"),
        ("scaleZ", "scalez"),
    )

    scaleX = FloatField(default_value=1.0)
    scalex = scaleX

    scaleY = FloatField(default_value=1.0)
    scaley = scaleY

    scaleZ = FloatField(default_value=1.0)
    scalez = scaleZ


class ScaleAttrOperator(Float3CompoundBaseAttrOperator[ScalePlugOperator]):
    __slots__ = ()

    scaleX = FloatField(default_value=1.0)
    scalex = scaleX

    scaleY = FloatField(default_value=1.0)
    scaley = scaleY

    scaleZ = FloatField(default_value=1.0)
    scalez = scaleZ


class ScaleField(
    Float3CompoundBaseField[ScaleAttrOperator, ScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAttrOperator
    PLUG_CLS = ScalePlugOperator

    scaleX = FloatField(default_value=1.0)
    scalex = scaleX

    scaleY = FloatField(default_value=1.0)
    scaley = scaleY

    scaleZ = FloatField(default_value=1.0)
    scalez = scaleZ


class OffsetPlugOperator(Float3CompoundBasePlugOperator["OffsetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetX", "offsetx"),
        ("offsetY", "offsety"),
        ("offsetZ", "offsetz"),
    )

    offsetX = FloatField(default_value=0.0)
    offsetx = offsetX

    offsetY = FloatField(default_value=0.0)
    offsety = offsetY

    offsetZ = FloatField(default_value=0.0)
    offsetz = offsetZ


class OffsetAttrOperator(Float3CompoundBaseAttrOperator[OffsetPlugOperator]):
    __slots__ = ()

    offsetX = FloatField(default_value=0.0)
    offsetx = offsetX

    offsetY = FloatField(default_value=0.0)
    offsety = offsetY

    offsetZ = FloatField(default_value=0.0)
    offsetz = offsetZ


class OffsetField(
    Float3CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetX = FloatField(default_value=0.0)
    offsetx = offsetX

    offsetY = FloatField(default_value=0.0)
    offsety = offsetY

    offsetZ = FloatField(default_value=0.0)
    offsetz = offsetZ


class PPlugOperator(Float3CompoundBasePlugOperator["PAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("PX", "Px"),
        ("PY", "Py"),
        ("PZ", "Pz"),
    )

    PX = FloatField(default_value=0.0)
    Px = PX

    PY = FloatField(default_value=0.0)
    Py = PY

    PZ = FloatField(default_value=0.0)
    Pz = PZ


class PAttrOperator(Float3CompoundBaseAttrOperator[PPlugOperator]):
    __slots__ = ()

    PX = FloatField(default_value=0.0)
    Px = PX

    PY = FloatField(default_value=0.0)
    Py = PY

    PZ = FloatField(default_value=0.0)
    Pz = PZ


class PField(Float3CompoundBaseField[PAttrOperator, PPlugOperator]):
    __slots__ = ()

    ATTR_CLS = PAttrOperator
    PLUG_CLS = PPlugOperator

    PX = FloatField(default_value=0.0)
    Px = PX

    PY = FloatField(default_value=0.0)
    Py = PY

    PZ = FloatField(default_value=0.0)
    Pz = PZ


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "colorr"),
        ("colorG", "colorg"),
        ("colorB", "colorb"),
    )

    colorR = FloatField(default_value=1.0)
    colorr = colorR

    colorG = FloatField(default_value=1.0)
    colorg = colorG

    colorB = FloatField(default_value=1.0)
    colorb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=1.0)
    colorr = colorR

    colorG = FloatField(default_value=1.0)
    colorg = colorG

    colorB = FloatField(default_value=1.0)
    colorb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=1.0)
    colorr = colorR

    colorG = FloatField(default_value=1.0)
    colorg = colorG

    colorB = FloatField(default_value=1.0)
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

    paletteR = FloatField(default_value=1.0)
    paletter = paletteR

    paletteG = FloatField(default_value=1.0)
    paletteg = paletteG

    paletteB = FloatField(default_value=1.0)
    paletteb = paletteB


class PaletteAttrOperator(Float3CompoundBaseAttrOperator[PalettePlugOperator]):
    __slots__ = ()

    paletteR = FloatField(default_value=1.0)
    paletter = paletteR

    paletteG = FloatField(default_value=1.0)
    paletteg = paletteG

    paletteB = FloatField(default_value=1.0)
    paletteb = paletteB


class PaletteField(
    Float3CompoundBaseField[PaletteAttrOperator, PalettePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PaletteAttrOperator
    PLUG_CLS = PalettePlugOperator

    paletteR = FloatField(default_value=1.0)
    paletter = paletteR

    paletteG = FloatField(default_value=1.0)
    paletteg = paletteG

    paletteB = FloatField(default_value=1.0)
    paletteb = paletteB
