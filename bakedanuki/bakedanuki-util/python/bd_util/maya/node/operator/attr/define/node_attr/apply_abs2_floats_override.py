# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)


class OutPlugOperator(
    Float2CompoundBasePlugOperator["OutAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out0", "o0"),
        ("out1", "o1"),
    )

    out0 = FloatField(default_value=0.0, writable=False)
    o0 = out0

    out1 = FloatField(default_value=0.0, writable=False)
    o1 = out1


class OutAttrOperator(
    Float2CompoundBaseAttrOperator[OutPlugOperator]
):
    __slots__ = ()

    out0 = FloatField(default_value=0.0, writable=False)
    o0 = out0

    out1 = FloatField(default_value=0.0, writable=False)
    o1 = out1


class OutField(
    Float2CompoundBaseField[OutAttrOperator, OutPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutAttrOperator
    PLUG_CLS = OutPlugOperator

    out0 = FloatField(default_value=0.0, writable=False)
    o0 = out0

    out1 = FloatField(default_value=0.0, writable=False)
    o1 = out1


class OriginalPlugOperator(
    Float2CompoundBasePlugOperator["OriginalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("original0", "ori0"),
        ("original1", "ori1"),
    )

    original0 = FloatField(default_value=0.0, readable=False)
    ori0 = original0

    original1 = FloatField(default_value=0.0, readable=False)
    ori1 = original1


class OriginalAttrOperator(
    Float2CompoundBaseAttrOperator[OriginalPlugOperator]
):
    __slots__ = ()

    original0 = FloatField(default_value=0.0, readable=False)
    ori0 = original0

    original1 = FloatField(default_value=0.0, readable=False)
    ori1 = original1


class OriginalField(
    Float2CompoundBaseField[OriginalAttrOperator, OriginalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OriginalAttrOperator
    PLUG_CLS = OriginalPlugOperator

    original0 = FloatField(default_value=0.0, readable=False)
    ori0 = original0

    original1 = FloatField(default_value=0.0, readable=False)
    ori1 = original1


class ValuePlugOperator(
    Float2CompoundBasePlugOperator["ValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("value0", "val0"),
        ("value1", "val1"),
    )

    value0 = FloatField(default_value=0.0, readable=False)
    val0 = value0

    value1 = FloatField(default_value=0.0, readable=False)
    val1 = value1


class ValueAttrOperator(
    Float2CompoundBaseAttrOperator[ValuePlugOperator]
):
    __slots__ = ()

    value0 = FloatField(default_value=0.0, readable=False)
    val0 = value0

    value1 = FloatField(default_value=0.0, readable=False)
    val1 = value1


class ValueField(
    Float2CompoundBaseField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator

    value0 = FloatField(default_value=0.0, readable=False)
    val0 = value0

    value1 = FloatField(default_value=0.0, readable=False)
    val1 = value1
