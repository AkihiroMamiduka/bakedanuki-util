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


class XPlugOperator(Float3CompoundBasePlugOperator["XAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("XX", "Xx"),
        ("XY", "Xy"),
        ("XZ", "Xz"),
    )

    XX = FloatField(default_value=1.0)
    Xx = XX

    XY = FloatField(default_value=0.0)
    Xy = XY

    XZ = FloatField(default_value=0.0)
    Xz = XZ


class XAttrOperator(Float3CompoundBaseAttrOperator[XPlugOperator]):
    __slots__ = ()

    XX = FloatField(default_value=1.0)
    Xx = XX

    XY = FloatField(default_value=0.0)
    Xy = XY

    XZ = FloatField(default_value=0.0)
    Xz = XZ


class XField(Float3CompoundBaseField[XAttrOperator, XPlugOperator]):
    __slots__ = ()

    ATTR_CLS = XAttrOperator
    PLUG_CLS = XPlugOperator

    XX = FloatField(default_value=1.0)
    Xx = XX

    XY = FloatField(default_value=0.0)
    Xy = XY

    XZ = FloatField(default_value=0.0)
    Xz = XZ


class YPlugOperator(Float3CompoundBasePlugOperator["YAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("YX", "Yx"),
        ("YY", "Yy"),
        ("YZ", "Yz"),
    )

    YX = FloatField(default_value=0.0)
    Yx = YX

    YY = FloatField(default_value=1.0)
    Yy = YY

    YZ = FloatField(default_value=0.0)
    Yz = YZ


class YAttrOperator(Float3CompoundBaseAttrOperator[YPlugOperator]):
    __slots__ = ()

    YX = FloatField(default_value=0.0)
    Yx = YX

    YY = FloatField(default_value=1.0)
    Yy = YY

    YZ = FloatField(default_value=0.0)
    Yz = YZ


class YField(Float3CompoundBaseField[YAttrOperator, YPlugOperator]):
    __slots__ = ()

    ATTR_CLS = YAttrOperator
    PLUG_CLS = YPlugOperator

    YX = FloatField(default_value=0.0)
    Yx = YX

    YY = FloatField(default_value=1.0)
    Yy = YY

    YZ = FloatField(default_value=0.0)
    Yz = YZ


class ZPlugOperator(Float3CompoundBasePlugOperator["ZAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ZX", "Zx"),
        ("ZY", "Zy"),
        ("ZZ", "Zz"),
    )

    ZX = FloatField(default_value=0.0)
    Zx = ZX

    ZY = FloatField(default_value=0.0)
    Zy = ZY

    ZZ = FloatField(default_value=1.0)
    Zz = ZZ


class ZAttrOperator(Float3CompoundBaseAttrOperator[ZPlugOperator]):
    __slots__ = ()

    ZX = FloatField(default_value=0.0)
    Zx = ZX

    ZY = FloatField(default_value=0.0)
    Zy = ZY

    ZZ = FloatField(default_value=1.0)
    Zz = ZZ


class ZField(Float3CompoundBaseField[ZAttrOperator, ZPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ZAttrOperator
    PLUG_CLS = ZPlugOperator

    ZX = FloatField(default_value=0.0)
    Zx = ZX

    ZY = FloatField(default_value=0.0)
    Zy = ZY

    ZZ = FloatField(default_value=1.0)
    Zz = ZZ
