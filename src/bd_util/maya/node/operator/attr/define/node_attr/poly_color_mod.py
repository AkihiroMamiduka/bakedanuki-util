# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.numeric_scalar_range.float import FloatField


class RedScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class RedScale_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class RedScale_InterpEnumField(
    EnumField[RedScale_InterpEnumAttrOperator, RedScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RedScale_InterpEnumAttrOperator
    PLUG_CLS = RedScale_InterpEnumPlugOperator


class GreenScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class GreenScale_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class GreenScale_InterpEnumField(
    EnumField[GreenScale_InterpEnumAttrOperator, GreenScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GreenScale_InterpEnumAttrOperator
    PLUG_CLS = GreenScale_InterpEnumPlugOperator


class BlueScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class BlueScale_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class BlueScale_InterpEnumField(
    EnumField[BlueScale_InterpEnumAttrOperator, BlueScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlueScale_InterpEnumAttrOperator
    PLUG_CLS = BlueScale_InterpEnumPlugOperator


class AlphaScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class AlphaScale_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class AlphaScale_InterpEnumField(
    EnumField[AlphaScale_InterpEnumAttrOperator, AlphaScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaScale_InterpEnumAttrOperator
    PLUG_CLS = AlphaScale_InterpEnumPlugOperator


class IntensityScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class IntensityScale_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class IntensityScale_InterpEnumField(
    EnumField[IntensityScale_InterpEnumAttrOperator, IntensityScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IntensityScale_InterpEnumAttrOperator
    PLUG_CLS = IntensityScale_InterpEnumPlugOperator


class RedScalePlugOperator(
    CompoundPlugOperator["RedScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("redScale_Position", "rp"),
        ("redScale_FloatValue", "rfv"),
        ("redScale_Interp", "ri"),
    )

    redScale_Position = FloatField()
    rp = redScale_Position

    redScale_FloatValue = FloatField()
    rfv = redScale_FloatValue

    redScale_Interp = RedScale_InterpEnumField()
    ri = redScale_Interp


class RedScaleAttrOperator(
    CompoundAttrOperator[RedScalePlugOperator]
):
    __slots__ = ()

    redScale_Position = FloatField()
    rp = redScale_Position

    redScale_FloatValue = FloatField()
    rfv = redScale_FloatValue

    redScale_Interp = RedScale_InterpEnumField()
    ri = redScale_Interp


class RedScaleField(
    CompoundField[RedScaleAttrOperator, RedScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RedScaleAttrOperator
    PLUG_CLS = RedScalePlugOperator


class GreenScalePlugOperator(
    CompoundPlugOperator["GreenScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("greenScale_Position", "gp"),
        ("greenScale_FloatValue", "gfv"),
        ("greenScale_Interp", "gi"),
    )

    greenScale_Position = FloatField()
    gp = greenScale_Position

    greenScale_FloatValue = FloatField()
    gfv = greenScale_FloatValue

    greenScale_Interp = GreenScale_InterpEnumField()
    gi = greenScale_Interp


class GreenScaleAttrOperator(
    CompoundAttrOperator[GreenScalePlugOperator]
):
    __slots__ = ()

    greenScale_Position = FloatField()
    gp = greenScale_Position

    greenScale_FloatValue = FloatField()
    gfv = greenScale_FloatValue

    greenScale_Interp = GreenScale_InterpEnumField()
    gi = greenScale_Interp


class GreenScaleField(
    CompoundField[GreenScaleAttrOperator, GreenScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GreenScaleAttrOperator
    PLUG_CLS = GreenScalePlugOperator


class BlueScalePlugOperator(
    CompoundPlugOperator["BlueScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("blueScale_Position", "bp"),
        ("blueScale_FloatValue", "bfv"),
        ("blueScale_Interp", "bi"),
    )

    blueScale_Position = FloatField()
    bp = blueScale_Position

    blueScale_FloatValue = FloatField()
    bfv = blueScale_FloatValue

    blueScale_Interp = BlueScale_InterpEnumField()
    bi = blueScale_Interp


class BlueScaleAttrOperator(
    CompoundAttrOperator[BlueScalePlugOperator]
):
    __slots__ = ()

    blueScale_Position = FloatField()
    bp = blueScale_Position

    blueScale_FloatValue = FloatField()
    bfv = blueScale_FloatValue

    blueScale_Interp = BlueScale_InterpEnumField()
    bi = blueScale_Interp


class BlueScaleField(
    CompoundField[BlueScaleAttrOperator, BlueScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlueScaleAttrOperator
    PLUG_CLS = BlueScalePlugOperator


class AlphaScalePlugOperator(
    CompoundPlugOperator["AlphaScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("alphaScale_Position", "ap"),
        ("alphaScale_FloatValue", "afv"),
        ("alphaScale_Interp", "ai"),
    )

    alphaScale_Position = FloatField()
    ap = alphaScale_Position

    alphaScale_FloatValue = FloatField()
    afv = alphaScale_FloatValue

    alphaScale_Interp = AlphaScale_InterpEnumField()
    ai = alphaScale_Interp


class AlphaScaleAttrOperator(
    CompoundAttrOperator[AlphaScalePlugOperator]
):
    __slots__ = ()

    alphaScale_Position = FloatField()
    ap = alphaScale_Position

    alphaScale_FloatValue = FloatField()
    afv = alphaScale_FloatValue

    alphaScale_Interp = AlphaScale_InterpEnumField()
    ai = alphaScale_Interp


class AlphaScaleField(
    CompoundField[AlphaScaleAttrOperator, AlphaScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaScaleAttrOperator
    PLUG_CLS = AlphaScalePlugOperator


class IntensityScalePlugOperator(
    CompoundPlugOperator["IntensityScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("intensityScale_Position", "np"),
        ("intensityScale_FloatValue", "nfv"),
        ("intensityScale_Interp", "ni"),
    )

    intensityScale_Position = FloatField()
    np = intensityScale_Position

    intensityScale_FloatValue = FloatField()
    nfv = intensityScale_FloatValue

    intensityScale_Interp = IntensityScale_InterpEnumField()
    ni = intensityScale_Interp


class IntensityScaleAttrOperator(
    CompoundAttrOperator[IntensityScalePlugOperator]
):
    __slots__ = ()

    intensityScale_Position = FloatField()
    np = intensityScale_Position

    intensityScale_FloatValue = FloatField()
    nfv = intensityScale_FloatValue

    intensityScale_Interp = IntensityScale_InterpEnumField()
    ni = intensityScale_Interp


class IntensityScaleField(
    CompoundField[IntensityScaleAttrOperator, IntensityScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IntensityScaleAttrOperator
    PLUG_CLS = IntensityScalePlugOperator
