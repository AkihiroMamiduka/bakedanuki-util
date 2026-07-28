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


class YPlugOperator(Float3CompoundBasePlugOperator["YAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("yR", "yr"),
        ("yG", "yg"),
        ("yB", "yb"),
    )

    yR = FloatField(default_value=0.0)
    yr = yR

    yG = FloatField(default_value=0.0)
    yg = yG

    yB = FloatField(default_value=0.0)
    yb = yB


class YAttrOperator(Float3CompoundBaseAttrOperator[YPlugOperator]):
    __slots__ = ()

    yR = FloatField(default_value=0.0)
    yr = yR

    yG = FloatField(default_value=0.0)
    yg = yG

    yB = FloatField(default_value=0.0)
    yb = yB


class YField(Float3CompoundBaseField[YAttrOperator, YPlugOperator]):
    __slots__ = ()

    ATTR_CLS = YAttrOperator
    PLUG_CLS = YPlugOperator

    yR = FloatField(default_value=0.0)
    yr = yR

    yG = FloatField(default_value=0.0)
    yg = yG

    yB = FloatField(default_value=0.0)
    yb = yB


class XPlugOperator(Float3CompoundBasePlugOperator["XAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("xR", "xr"),
        ("xG", "xg"),
        ("xB", "xb"),
    )

    xR = FloatField(default_value=0.0)
    xr = xR

    xG = FloatField(default_value=0.0)
    xg = xG

    xB = FloatField(default_value=0.0)
    xb = xB


class XAttrOperator(Float3CompoundBaseAttrOperator[XPlugOperator]):
    __slots__ = ()

    xR = FloatField(default_value=0.0)
    xr = xR

    xG = FloatField(default_value=0.0)
    xg = xG

    xB = FloatField(default_value=0.0)
    xb = xB


class XField(Float3CompoundBaseField[XAttrOperator, XPlugOperator]):
    __slots__ = ()

    ATTR_CLS = XAttrOperator
    PLUG_CLS = XPlugOperator

    xR = FloatField(default_value=0.0)
    xr = xR

    xG = FloatField(default_value=0.0)
    xg = xG

    xB = FloatField(default_value=0.0)
    xb = xB
