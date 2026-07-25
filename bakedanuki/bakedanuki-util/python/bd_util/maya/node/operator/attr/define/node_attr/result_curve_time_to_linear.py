# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.scalar.unit.time import TimeField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class CurveColorPlugOperator(
    Float3CompoundBasePlugOperator["CurveColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("curveColorR", "ccr"),
        ("curveColorG", "ccg"),
        ("curveColorB", "ccb"),
    )

    curveColorR = FloatField(default_value=0.0)
    ccr = curveColorR

    curveColorG = FloatField(default_value=0.0)
    ccg = curveColorG

    curveColorB = FloatField(default_value=0.0)
    ccb = curveColorB


class CurveColorAttrOperator(
    Float3CompoundBaseAttrOperator[CurveColorPlugOperator]
):
    __slots__ = ()

    curveColorR = FloatField(default_value=0.0)
    ccr = curveColorR

    curveColorG = FloatField(default_value=0.0)
    ccg = curveColorG

    curveColorB = FloatField(default_value=0.0)
    ccb = curveColorB


class CurveColorField(
    Float3CompoundBaseField[CurveColorAttrOperator, CurveColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CurveColorAttrOperator
    PLUG_CLS = CurveColorPlugOperator

    curveColorR = FloatField(default_value=0.0)
    ccr = curveColorR

    curveColorG = FloatField(default_value=0.0)
    ccg = curveColorG

    curveColorB = FloatField(default_value=0.0)
    ccb = curveColorB


class KeyTimeValuePlugOperator(
    CompoundPlugOperator["KeyTimeValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("keyTime", "kt"),
        ("keyValue", "kv"),
    )

    keyTime = TimeField(default_value=0.0)
    kt = keyTime

    keyValue = DoubleLinearField(default_value=0.0)
    kv = keyValue


class KeyTimeValueAttrOperator(
    CompoundAttrOperator[KeyTimeValuePlugOperator]
):
    __slots__ = ()

    keyTime = TimeField(default_value=0.0)
    kt = keyTime

    keyValue = DoubleLinearField(default_value=0.0)
    kv = keyValue


class KeyTimeValueField(
    CompoundField[KeyTimeValueAttrOperator, KeyTimeValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KeyTimeValueAttrOperator
    PLUG_CLS = KeyTimeValuePlugOperator
