# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
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

    valueR = FloatField()
    vr = valueR

    valueG = FloatField()
    vg = valueG

    valueB = FloatField()
    vb = valueB


class ValueAttrOperator(
    Float3CompoundBaseAttrOperator[ValuePlugOperator]
):
    __slots__ = ()

    valueR = FloatField()
    vr = valueR

    valueG = FloatField()
    vg = valueG

    valueB = FloatField()
    vb = valueB


class ValueField(
    Float3CompoundBaseField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator

    valueR = FloatField()
    vr = valueR

    valueG = FloatField()
    vg = valueG

    valueB = FloatField()
    vb = valueB
