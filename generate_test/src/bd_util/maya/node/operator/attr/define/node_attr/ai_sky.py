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


class XPlugOperator(
    Float3CompoundBasePlugOperator["XAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("XX", "Xx"),
        ("XY", "Xy"),
        ("XZ", "Xz"),
    )

    XX = FloatField()
    Xx = XX

    XY = FloatField()
    Xy = XY

    XZ = FloatField()
    Xz = XZ


class XAttrOperator(
    Float3CompoundBaseAttrOperator[XPlugOperator]
):
    __slots__ = ()

    XX = FloatField()
    Xx = XX

    XY = FloatField()
    Xy = XY

    XZ = FloatField()
    Xz = XZ


class XField(
    Float3CompoundBaseField[XAttrOperator, XPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = XAttrOperator
    PLUG_CLS = XPlugOperator

    XX = FloatField()
    Xx = XX

    XY = FloatField()
    Xy = XY

    XZ = FloatField()
    Xz = XZ


class YPlugOperator(
    Float3CompoundBasePlugOperator["YAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("YX", "Yx"),
        ("YY", "Yy"),
        ("YZ", "Yz"),
    )

    YX = FloatField()
    Yx = YX

    YY = FloatField()
    Yy = YY

    YZ = FloatField()
    Yz = YZ


class YAttrOperator(
    Float3CompoundBaseAttrOperator[YPlugOperator]
):
    __slots__ = ()

    YX = FloatField()
    Yx = YX

    YY = FloatField()
    Yy = YY

    YZ = FloatField()
    Yz = YZ


class YField(
    Float3CompoundBaseField[YAttrOperator, YPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = YAttrOperator
    PLUG_CLS = YPlugOperator

    YX = FloatField()
    Yx = YX

    YY = FloatField()
    Yy = YY

    YZ = FloatField()
    Yz = YZ


class ZPlugOperator(
    Float3CompoundBasePlugOperator["ZAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ZX", "Zx"),
        ("ZY", "Zy"),
        ("ZZ", "Zz"),
    )

    ZX = FloatField()
    Zx = ZX

    ZY = FloatField()
    Zy = ZY

    ZZ = FloatField()
    Zz = ZZ


class ZAttrOperator(
    Float3CompoundBaseAttrOperator[ZPlugOperator]
):
    __slots__ = ()

    ZX = FloatField()
    Zx = ZX

    ZY = FloatField()
    Zy = ZY

    ZZ = FloatField()
    Zz = ZZ


class ZField(
    Float3CompoundBaseField[ZAttrOperator, ZPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ZAttrOperator
    PLUG_CLS = ZPlugOperator

    ZX = FloatField()
    Zx = ZX

    ZY = FloatField()
    Zy = ZY

    ZZ = FloatField()
    Zz = ZZ
