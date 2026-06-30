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


class YPlugOperator(
    Float3CompoundBasePlugOperator["YAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("yR", "yr"),
        ("yG", "yg"),
        ("yB", "yb"),
    )

    yR = FloatField()
    yr = yR

    yG = FloatField()
    yg = yG

    yB = FloatField()
    yb = yB


class YAttrOperator(
    Float3CompoundBaseAttrOperator[YPlugOperator]
):
    __slots__ = ()

    yR = FloatField()
    yr = yR

    yG = FloatField()
    yg = yG

    yB = FloatField()
    yb = yB


class YField(
    Float3CompoundBaseField[YAttrOperator, YPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = YAttrOperator
    PLUG_CLS = YPlugOperator

    yR = FloatField()
    yr = yR

    yG = FloatField()
    yg = yG

    yB = FloatField()
    yb = yB


class XPlugOperator(
    Float3CompoundBasePlugOperator["XAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("xR", "xr"),
        ("xG", "xg"),
        ("xB", "xb"),
    )

    xR = FloatField()
    xr = xR

    xG = FloatField()
    xg = xG

    xB = FloatField()
    xb = xB


class XAttrOperator(
    Float3CompoundBaseAttrOperator[XPlugOperator]
):
    __slots__ = ()

    xR = FloatField()
    xr = xR

    xG = FloatField()
    xg = xG

    xB = FloatField()
    xb = xB


class XField(
    Float3CompoundBaseField[XAttrOperator, XPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = XAttrOperator
    PLUG_CLS = XPlugOperator

    xR = FloatField()
    xr = xR

    xG = FloatField()
    xg = xG

    xB = FloatField()
    xb = xB
