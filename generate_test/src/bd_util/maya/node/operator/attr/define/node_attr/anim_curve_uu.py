# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
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

    curveColorR = FloatField()
    ccr = curveColorR

    curveColorG = FloatField()
    ccg = curveColorG

    curveColorB = FloatField()
    ccb = curveColorB


class CurveColorAttrOperator(
    Float3CompoundBaseAttrOperator[CurveColorPlugOperator]
):
    __slots__ = ()

    curveColorR = FloatField()
    ccr = curveColorR

    curveColorG = FloatField()
    ccg = curveColorG

    curveColorB = FloatField()
    ccb = curveColorB


class CurveColorField(
    Float3CompoundBaseField[CurveColorAttrOperator, CurveColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CurveColorAttrOperator
    PLUG_CLS = CurveColorPlugOperator

    curveColorR = FloatField()
    ccr = curveColorR

    curveColorG = FloatField()
    ccg = curveColorG

    curveColorB = FloatField()
    ccb = curveColorB


class KeyTimeValuePlugOperator(
    CompoundPlugOperator["KeyTimeValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("keyTime", "kt"),
        ("keyValue", "kv"),
    )

    keyTime = DoubleField()
    kt = keyTime

    keyValue = DoubleField()
    kv = keyValue


class KeyTimeValueAttrOperator(
    CompoundAttrOperator[KeyTimeValuePlugOperator]
):
    __slots__ = ()

    keyTime = DoubleField()
    kt = keyTime

    keyValue = DoubleField()
    kv = keyValue


class KeyTimeValueField(
    CompoundField[KeyTimeValueAttrOperator, KeyTimeValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KeyTimeValueAttrOperator
    PLUG_CLS = KeyTimeValuePlugOperator
