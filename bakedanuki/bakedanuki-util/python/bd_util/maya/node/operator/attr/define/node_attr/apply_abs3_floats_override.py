# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutPlugOperator(Float3CompoundBasePlugOperator["OutAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out0", "o0"),
        ("out1", "o1"),
        ("out2", "o2"),
    )

    out0 = FloatField(default_value=0.0, writable=False)
    o0 = out0

    out1 = FloatField(default_value=0.0, writable=False)
    o1 = out1

    out2 = FloatField(default_value=0.0, writable=False)
    o2 = out2


class OutAttrOperator(Float3CompoundBaseAttrOperator[OutPlugOperator]):
    __slots__ = ()

    out0 = FloatField(default_value=0.0, writable=False)
    o0 = out0

    out1 = FloatField(default_value=0.0, writable=False)
    o1 = out1

    out2 = FloatField(default_value=0.0, writable=False)
    o2 = out2


class OutField(Float3CompoundBaseField[OutAttrOperator, OutPlugOperator]):
    __slots__ = ()

    ATTR_CLS = OutAttrOperator
    PLUG_CLS = OutPlugOperator

    out0 = FloatField(default_value=0.0, writable=False)
    o0 = out0

    out1 = FloatField(default_value=0.0, writable=False)
    o1 = out1

    out2 = FloatField(default_value=0.0, writable=False)
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

    original0 = FloatField(default_value=0.0, readable=False)
    ori0 = original0

    original1 = FloatField(default_value=0.0, readable=False)
    ori1 = original1

    original2 = FloatField(default_value=0.0, readable=False)
    ori2 = original2


class OriginalAttrOperator(
    Float3CompoundBaseAttrOperator[OriginalPlugOperator]
):
    __slots__ = ()

    original0 = FloatField(default_value=0.0, readable=False)
    ori0 = original0

    original1 = FloatField(default_value=0.0, readable=False)
    ori1 = original1

    original2 = FloatField(default_value=0.0, readable=False)
    ori2 = original2


class OriginalField(
    Float3CompoundBaseField[OriginalAttrOperator, OriginalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OriginalAttrOperator
    PLUG_CLS = OriginalPlugOperator

    original0 = FloatField(default_value=0.0, readable=False)
    ori0 = original0

    original1 = FloatField(default_value=0.0, readable=False)
    ori1 = original1

    original2 = FloatField(default_value=0.0, readable=False)
    ori2 = original2


class ValuePlugOperator(Float3CompoundBasePlugOperator["ValueAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("value0", "val0"),
        ("value1", "val1"),
        ("value2", "val2"),
    )

    value0 = FloatField(default_value=0.0, readable=False)
    val0 = value0

    value1 = FloatField(default_value=0.0, readable=False)
    val1 = value1

    value2 = FloatField(default_value=0.0, readable=False)
    val2 = value2


class ValueAttrOperator(Float3CompoundBaseAttrOperator[ValuePlugOperator]):
    __slots__ = ()

    value0 = FloatField(default_value=0.0, readable=False)
    val0 = value0

    value1 = FloatField(default_value=0.0, readable=False)
    val1 = value1

    value2 = FloatField(default_value=0.0, readable=False)
    val2 = value2


class ValueField(
    Float3CompoundBaseField[ValueAttrOperator, ValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ValueAttrOperator
    PLUG_CLS = ValuePlugOperator

    value0 = FloatField(default_value=0.0, readable=False)
    val0 = value0

    value1 = FloatField(default_value=0.0, readable=False)
    val1 = value1

    value2 = FloatField(default_value=0.0, readable=False)
    val2 = value2
