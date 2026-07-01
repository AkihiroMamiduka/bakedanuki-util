# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class CustomPlugOperator(
    Float3CompoundBasePlugOperator["CustomAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("customR", "customr"),
        ("customG", "customg"),
        ("customB", "customb"),
    )

    customR = FloatField()
    customr = customR

    customG = FloatField()
    customg = customG

    customB = FloatField()
    customb = customB


class CustomAttrOperator(
    Float3CompoundBaseAttrOperator[CustomPlugOperator]
):
    __slots__ = ()

    customR = FloatField()
    customr = customR

    customG = FloatField()
    customg = customG

    customB = FloatField()
    customb = customB


class CustomField(
    Float3CompoundBaseField[CustomAttrOperator, CustomPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CustomAttrOperator
    PLUG_CLS = CustomPlugOperator

    customR = FloatField()
    customr = customR

    customG = FloatField()
    customg = customG

    customB = FloatField()
    customb = customB
