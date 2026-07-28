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


class MagnitudeScale_InterpEnumPlugOperator(EnumPlugOperator["MagnitudeScale_InterpEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class MagnitudeScale_InterpEnumAttrOperator(EnumAttrOperator[MagnitudeScale_InterpEnumPlugOperator]):
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


class MagnitudeScale_InterpEnumField(
    EnumField[MagnitudeScale_InterpEnumAttrOperator, MagnitudeScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MagnitudeScale_InterpEnumAttrOperator
    PLUG_CLS = MagnitudeScale_InterpEnumPlugOperator


class MagnitudeScalePlugOperator(
    CompoundPlugOperator["MagnitudeScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("magnitudeScale_Position", "msp"),
        ("magnitudeScale_FloatValue", "msfv"),
        ("magnitudeScale_Interp", "msi"),
    )

    magnitudeScale_Position = FloatField(default_value=0.0)
    msp = magnitudeScale_Position

    magnitudeScale_FloatValue = FloatField(default_value=0.0)
    msfv = magnitudeScale_FloatValue

    magnitudeScale_Interp = MagnitudeScale_InterpEnumField(default_value=1)
    msi = magnitudeScale_Interp


class MagnitudeScaleAttrOperator(
    CompoundAttrOperator[MagnitudeScalePlugOperator]
):
    __slots__ = ()

    magnitudeScale_Position = FloatField(default_value=0.0)
    msp = magnitudeScale_Position

    magnitudeScale_FloatValue = FloatField(default_value=0.0)
    msfv = magnitudeScale_FloatValue

    magnitudeScale_Interp = MagnitudeScale_InterpEnumField(default_value=1)
    msi = magnitudeScale_Interp


class MagnitudeScaleField(
    CompoundField[MagnitudeScaleAttrOperator, MagnitudeScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MagnitudeScaleAttrOperator
    PLUG_CLS = MagnitudeScalePlugOperator


class RegionMapPlugOperator(
    Float3CompoundBasePlugOperator["RegionMapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("regionMapR", "rmpr"),
        ("regionMapG", "rmpg"),
        ("regionMapB", "rmpb"),
    )

    regionMapR = FloatField(default_value=1.0)
    rmpr = regionMapR

    regionMapG = FloatField(default_value=1.0)
    rmpg = regionMapG

    regionMapB = FloatField(default_value=1.0)
    rmpb = regionMapB


class RegionMapAttrOperator(
    Float3CompoundBaseAttrOperator[RegionMapPlugOperator]
):
    __slots__ = ()

    regionMapR = FloatField(default_value=1.0)
    rmpr = regionMapR

    regionMapG = FloatField(default_value=1.0)
    rmpg = regionMapG

    regionMapB = FloatField(default_value=1.0)
    rmpb = regionMapB


class RegionMapField(
    Float3CompoundBaseField[RegionMapAttrOperator, RegionMapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RegionMapAttrOperator
    PLUG_CLS = RegionMapPlugOperator

    regionMapR = FloatField(default_value=1.0)
    rmpr = regionMapR

    regionMapG = FloatField(default_value=1.0)
    rmpg = regionMapG

    regionMapB = FloatField(default_value=1.0)
    rmpb = regionMapB
