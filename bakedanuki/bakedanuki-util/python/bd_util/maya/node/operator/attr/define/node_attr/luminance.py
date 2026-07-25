# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ValuePlugOperator(
    Float3CompoundBasePlugOperator["ValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("valueR", "vr"),
        ("valueG", "vg"),
        ("valueB", "vb"),
    )

    valueR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vr = valueR

    valueG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vg = valueG

    valueB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vb = valueB


class ValueAttrOperator(
    Float3CompoundBaseAttrOperator[ValuePlugOperator]
):
    __slots__ = ()

    valueR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vr = valueR

    valueG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vg = valueG

    valueB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vb = valueB


class ValueField(
    Float3CompoundBaseField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator

    valueR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vr = valueR

    valueG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vg = valueG

    valueB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vb = valueB
