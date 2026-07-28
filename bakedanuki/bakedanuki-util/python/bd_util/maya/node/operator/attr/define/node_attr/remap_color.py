# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class Red_InterpEnumPlugOperator(
    EnumPlugOperator["Red_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Red_InterpEnumAttrOperator(EnumAttrOperator[Red_InterpEnumPlugOperator]):
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


class Red_InterpEnumField(
    EnumField[Red_InterpEnumAttrOperator, Red_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Red_InterpEnumAttrOperator
    PLUG_CLS = Red_InterpEnumPlugOperator


class Green_InterpEnumPlugOperator(
    EnumPlugOperator["Green_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Green_InterpEnumAttrOperator(
    EnumAttrOperator[Green_InterpEnumPlugOperator]
):
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


class Green_InterpEnumField(
    EnumField[Green_InterpEnumAttrOperator, Green_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Green_InterpEnumAttrOperator
    PLUG_CLS = Green_InterpEnumPlugOperator


class Blue_InterpEnumPlugOperator(
    EnumPlugOperator["Blue_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Blue_InterpEnumAttrOperator(
    EnumAttrOperator[Blue_InterpEnumPlugOperator]
):
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


class Blue_InterpEnumField(
    EnumField[Blue_InterpEnumAttrOperator, Blue_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Blue_InterpEnumAttrOperator
    PLUG_CLS = Blue_InterpEnumPlugOperator


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "cr"),
        ("colorG", "cg"),
        ("colorB", "cb"),
    )

    colorR = FloatField(default_value=0.5)
    cr = colorR

    colorG = FloatField(default_value=0.5)
    cg = colorG

    colorB = FloatField(default_value=0.5)
    cb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=0.5)
    cr = colorR

    colorG = FloatField(default_value=0.5)
    cg = colorG

    colorB = FloatField(default_value=0.5)
    cb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=0.5)
    cr = colorR

    colorG = FloatField(default_value=0.5)
    cg = colorG

    colorB = FloatField(default_value=0.5)
    cb = colorB


class RedPlugOperator(CompoundPlugOperator["RedAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("red_Position", "rp"),
        ("red_FloatValue", "rfv"),
        ("red_Interp", "ri"),
    )

    red_Position = FloatField(default_value=0.0)
    rp = red_Position

    red_FloatValue = FloatField(default_value=0.0)
    rfv = red_FloatValue

    red_Interp = Red_InterpEnumField(default_value=0)
    ri = red_Interp


class RedAttrOperator(CompoundAttrOperator[RedPlugOperator]):
    __slots__ = ()

    red_Position = FloatField(default_value=0.0)
    rp = red_Position

    red_FloatValue = FloatField(default_value=0.0)
    rfv = red_FloatValue

    red_Interp = Red_InterpEnumField(default_value=0)
    ri = red_Interp


class RedField(CompoundField[RedAttrOperator, RedPlugOperator]):
    __slots__ = ()

    ATTR_CLS = RedAttrOperator
    PLUG_CLS = RedPlugOperator


class GreenPlugOperator(CompoundPlugOperator["GreenAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("green_Position", "gp"),
        ("green_FloatValue", "gfv"),
        ("green_Interp", "gi"),
    )

    green_Position = FloatField(default_value=0.0)
    gp = green_Position

    green_FloatValue = FloatField(default_value=0.0)
    gfv = green_FloatValue

    green_Interp = Green_InterpEnumField(default_value=0)
    gi = green_Interp


class GreenAttrOperator(CompoundAttrOperator[GreenPlugOperator]):
    __slots__ = ()

    green_Position = FloatField(default_value=0.0)
    gp = green_Position

    green_FloatValue = FloatField(default_value=0.0)
    gfv = green_FloatValue

    green_Interp = Green_InterpEnumField(default_value=0)
    gi = green_Interp


class GreenField(CompoundField[GreenAttrOperator, GreenPlugOperator]):
    __slots__ = ()

    ATTR_CLS = GreenAttrOperator
    PLUG_CLS = GreenPlugOperator


class BluePlugOperator(CompoundPlugOperator["BlueAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("blue_Position", "bp"),
        ("blue_FloatValue", "bfv"),
        ("blue_Interp", "bi"),
    )

    blue_Position = FloatField(default_value=0.0)
    bp = blue_Position

    blue_FloatValue = FloatField(default_value=0.0)
    bfv = blue_FloatValue

    blue_Interp = Blue_InterpEnumField(default_value=0)
    bi = blue_Interp


class BlueAttrOperator(CompoundAttrOperator[BluePlugOperator]):
    __slots__ = ()

    blue_Position = FloatField(default_value=0.0)
    bp = blue_Position

    blue_FloatValue = FloatField(default_value=0.0)
    bfv = blue_FloatValue

    blue_Interp = Blue_InterpEnumField(default_value=0)
    bi = blue_Interp


class BlueField(CompoundField[BlueAttrOperator, BluePlugOperator]):
    __slots__ = ()

    ATTR_CLS = BlueAttrOperator
    PLUG_CLS = BluePlugOperator


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
