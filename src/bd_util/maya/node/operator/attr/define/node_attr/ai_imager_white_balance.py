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

    customR = FloatField(default_value=1.0)
    customr = customR

    customG = FloatField(default_value=1.0)
    customg = customG

    customB = FloatField(default_value=1.0)
    customb = customB


class CustomAttrOperator(
    Float3CompoundBaseAttrOperator[CustomPlugOperator]
):
    __slots__ = ()

    customR = FloatField(default_value=1.0)
    customr = customR

    customG = FloatField(default_value=1.0)
    customg = customG

    customB = FloatField(default_value=1.0)
    customb = customB


class CustomField(
    Float3CompoundBaseField[CustomAttrOperator, CustomPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CustomAttrOperator
    PLUG_CLS = CustomPlugOperator

    customR = FloatField(default_value=1.0)
    customr = customR

    customG = FloatField(default_value=1.0)
    customg = customG

    customB = FloatField(default_value=1.0)
    customb = customB
