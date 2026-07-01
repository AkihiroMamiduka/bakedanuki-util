# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutPlugOperator(
    Float3CompoundBasePlugOperator["OutAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out0", "o0"),
        ("out1", "o1"),
        ("out2", "o2"),
    )

    out0 = FloatField()
    o0 = out0

    out1 = FloatField()
    o1 = out1

    out2 = FloatField()
    o2 = out2


class OutAttrOperator(
    Float3CompoundBaseAttrOperator[OutPlugOperator]
):
    __slots__ = ()

    out0 = FloatField()
    o0 = out0

    out1 = FloatField()
    o1 = out1

    out2 = FloatField()
    o2 = out2


class OutField(
    Float3CompoundBaseField[OutAttrOperator, OutPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutAttrOperator
    PLUG_CLS = OutPlugOperator

    out0 = FloatField()
    o0 = out0

    out1 = FloatField()
    o1 = out1

    out2 = FloatField()
    o2 = out2


class OriginalPlugOperator(
    Float3CompoundBasePlugOperator["OriginalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("original0", "ori0"),
        ("original1", "ori1"),
        ("original2", "ori2"),
    )

    original0 = FloatField()
    ori0 = original0

    original1 = FloatField()
    ori1 = original1

    original2 = FloatField()
    ori2 = original2


class OriginalAttrOperator(
    Float3CompoundBaseAttrOperator[OriginalPlugOperator]
):
    __slots__ = ()

    original0 = FloatField()
    ori0 = original0

    original1 = FloatField()
    ori1 = original1

    original2 = FloatField()
    ori2 = original2


class OriginalField(
    Float3CompoundBaseField[OriginalAttrOperator, OriginalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OriginalAttrOperator
    PLUG_CLS = OriginalPlugOperator

    original0 = FloatField()
    ori0 = original0

    original1 = FloatField()
    ori1 = original1

    original2 = FloatField()
    ori2 = original2


class ValuePlugOperator(
    Float3CompoundBasePlugOperator["ValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("value0", "val0"),
        ("value1", "val1"),
        ("value2", "val2"),
    )

    value0 = FloatField()
    val0 = value0

    value1 = FloatField()
    val1 = value1

    value2 = FloatField()
    val2 = value2


class ValueAttrOperator(
    Float3CompoundBaseAttrOperator[ValuePlugOperator]
):
    __slots__ = ()

    value0 = FloatField()
    val0 = value0

    value1 = FloatField()
    val1 = value1

    value2 = FloatField()
    val2 = value2


class ValueField(
    Float3CompoundBaseField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator

    value0 = FloatField()
    val0 = value0

    value1 = FloatField()
    val1 = value1

    value2 = FloatField()
    val2 = value2
