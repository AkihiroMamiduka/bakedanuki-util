# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "cr"),
        ("colorG", "cg"),
        ("colorB", "cb"),
    )

    colorR = FloatField(default_value=0.0)
    cr = colorR

    colorG = FloatField(default_value=0.5882400274276733)
    cg = colorG

    colorB = FloatField(default_value=0.6439999938011169)
    cb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=0.0)
    cr = colorR

    colorG = FloatField(default_value=0.5882400274276733)
    cg = colorG

    colorB = FloatField(default_value=0.6439999938011169)
    cb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=0.0)
    cr = colorR

    colorG = FloatField(default_value=0.5882400274276733)
    cg = colorG

    colorB = FloatField(default_value=0.6439999938011169)
    cb = colorB


class PointWorldPlugOperator(
    Float3CompoundBasePlugOperator["PointWorldAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointWorldX", "px"),
        ("pointWorldY", "py"),
        ("pointWorldZ", "pz"),
    )

    pointWorldX = FloatField(default_value=1.0, readable=False)
    px = pointWorldX

    pointWorldY = FloatField(default_value=1.0, readable=False)
    py = pointWorldY

    pointWorldZ = FloatField(default_value=1.0, readable=False)
    pz = pointWorldZ


class PointWorldAttrOperator(
    Float3CompoundBaseAttrOperator[PointWorldPlugOperator]
):
    __slots__ = ()

    pointWorldX = FloatField(default_value=1.0, readable=False)
    px = pointWorldX

    pointWorldY = FloatField(default_value=1.0, readable=False)
    py = pointWorldY

    pointWorldZ = FloatField(default_value=1.0, readable=False)
    pz = pointWorldZ


class PointWorldField(
    Float3CompoundBaseField[PointWorldAttrOperator, PointWorldPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointWorldAttrOperator
    PLUG_CLS = PointWorldPlugOperator

    pointWorldX = FloatField(default_value=1.0, readable=False)
    px = pointWorldX

    pointWorldY = FloatField(default_value=1.0, readable=False)
    py = pointWorldY

    pointWorldZ = FloatField(default_value=1.0, readable=False)
    pz = pointWorldZ


class FarPointWorldPlugOperator(
    Float3CompoundBasePlugOperator["FarPointWorldAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("farPointWorldX", "fpx"),
        ("farPointWorldY", "fpy"),
        ("farPointWorldZ", "fpz"),
    )

    farPointWorldX = FloatField(default_value=1.0, readable=False)
    fpx = farPointWorldX

    farPointWorldY = FloatField(default_value=1.0, readable=False)
    fpy = farPointWorldY

    farPointWorldZ = FloatField(default_value=1.0, readable=False)
    fpz = farPointWorldZ


class FarPointWorldAttrOperator(
    Float3CompoundBaseAttrOperator[FarPointWorldPlugOperator]
):
    __slots__ = ()

    farPointWorldX = FloatField(default_value=1.0, readable=False)
    fpx = farPointWorldX

    farPointWorldY = FloatField(default_value=1.0, readable=False)
    fpy = farPointWorldY

    farPointWorldZ = FloatField(default_value=1.0, readable=False)
    fpz = farPointWorldZ


class FarPointWorldField(
    Float3CompoundBaseField[
        FarPointWorldAttrOperator, FarPointWorldPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FarPointWorldAttrOperator
    PLUG_CLS = FarPointWorldPlugOperator

    farPointWorldX = FloatField(default_value=1.0, readable=False)
    fpx = farPointWorldX

    farPointWorldY = FloatField(default_value=1.0, readable=False)
    fpy = farPointWorldY

    farPointWorldZ = FloatField(default_value=1.0, readable=False)
    fpz = farPointWorldZ


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


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
