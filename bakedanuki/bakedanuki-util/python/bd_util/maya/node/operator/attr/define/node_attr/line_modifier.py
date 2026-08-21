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
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class Dropoff_dropoff_InterpEnumPlugOperator(
    EnumPlugOperator["Dropoff_dropoff_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Dropoff_dropoff_InterpEnumAttrOperator(
    EnumAttrOperator[Dropoff_dropoff_InterpEnumPlugOperator]
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


class Dropoff_dropoff_InterpEnumField(
    EnumField[
        Dropoff_dropoff_InterpEnumAttrOperator,
        Dropoff_dropoff_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Dropoff_dropoff_InterpEnumAttrOperator
    PLUG_CLS = Dropoff_dropoff_InterpEnumPlugOperator


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "crr"),
        ("colorG", "crg"),
        ("colorB", "crb"),
    )

    colorR = FloatField(default_value=1.0)
    crr = colorR

    colorG = FloatField(default_value=0.0)
    crg = colorG

    colorB = FloatField(default_value=0.0)
    crb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=1.0)
    crr = colorR

    colorG = FloatField(default_value=0.0)
    crg = colorG

    colorB = FloatField(default_value=0.0)
    crb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=1.0)
    crr = colorR

    colorG = FloatField(default_value=0.0)
    crg = colorG

    colorB = FloatField(default_value=0.0)
    crb = colorB


class DropoffPlugOperator(CompoundPlugOperator["DropoffAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dropoff_Position", "drpp"),
        ("dropoff_FloatValue", "drpfv"),
        ("dropoff_Interp", "drpi"),
    )

    dropoff_Position = FloatField(default_value=0.0)
    drpp = dropoff_Position

    dropoff_FloatValue = FloatField(default_value=0.0)
    drpfv = dropoff_FloatValue

    dropoff_Interp = Dropoff_dropoff_InterpEnumField(default_value=0)
    drpi = dropoff_Interp


class DropoffAttrOperator(CompoundAttrOperator[DropoffPlugOperator]):
    __slots__ = ()

    dropoff_Position = FloatField(default_value=0.0)
    drpp = dropoff_Position

    dropoff_FloatValue = FloatField(default_value=0.0)
    drpfv = dropoff_FloatValue

    dropoff_Interp = Dropoff_dropoff_InterpEnumField(default_value=0)
    drpi = dropoff_Interp


class DropoffField(CompoundField[DropoffAttrOperator, DropoffPlugOperator]):
    __slots__ = ()

    ATTR_CLS = DropoffAttrOperator
    PLUG_CLS = DropoffPlugOperator
