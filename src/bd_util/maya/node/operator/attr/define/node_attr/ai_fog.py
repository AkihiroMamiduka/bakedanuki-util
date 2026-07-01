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


class GroundPointPlugOperator(
    Float3CompoundBasePlugOperator["GroundPointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("groundPointX", "ground_pointx"),
        ("groundPointY", "ground_pointy"),
        ("groundPointZ", "ground_pointz"),
    )

    groundPointX = FloatField()
    ground_pointx = groundPointX

    groundPointY = FloatField()
    ground_pointy = groundPointY

    groundPointZ = FloatField()
    ground_pointz = groundPointZ


class GroundPointAttrOperator(
    Float3CompoundBaseAttrOperator[GroundPointPlugOperator]
):
    __slots__ = ()

    groundPointX = FloatField()
    ground_pointx = groundPointX

    groundPointY = FloatField()
    ground_pointy = groundPointY

    groundPointZ = FloatField()
    ground_pointz = groundPointZ


class GroundPointField(
    Float3CompoundBaseField[GroundPointAttrOperator, GroundPointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GroundPointAttrOperator
    PLUG_CLS = GroundPointPlugOperator

    groundPointX = FloatField()
    ground_pointx = groundPointX

    groundPointY = FloatField()
    ground_pointy = groundPointY

    groundPointZ = FloatField()
    ground_pointz = groundPointZ


class GroundNormalPlugOperator(
    Float3CompoundBasePlugOperator["GroundNormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("groundNormalX", "ground_normalx"),
        ("groundNormalY", "ground_normaly"),
        ("groundNormalZ", "ground_normalz"),
    )

    groundNormalX = FloatField()
    ground_normalx = groundNormalX

    groundNormalY = FloatField()
    ground_normaly = groundNormalY

    groundNormalZ = FloatField()
    ground_normalz = groundNormalZ


class GroundNormalAttrOperator(
    Float3CompoundBaseAttrOperator[GroundNormalPlugOperator]
):
    __slots__ = ()

    groundNormalX = FloatField()
    ground_normalx = groundNormalX

    groundNormalY = FloatField()
    ground_normaly = groundNormalY

    groundNormalZ = FloatField()
    ground_normalz = groundNormalZ


class GroundNormalField(
    Float3CompoundBaseField[GroundNormalAttrOperator, GroundNormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GroundNormalAttrOperator
    PLUG_CLS = GroundNormalPlugOperator

    groundNormalX = FloatField()
    ground_normalx = groundNormalX

    groundNormalY = FloatField()
    ground_normaly = groundNormalY

    groundNormalZ = FloatField()
    ground_normalz = groundNormalZ
