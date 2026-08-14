# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)


class OutPlugOperator(Float2CompoundBasePlugOperator["OutAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out0", "o0"),
        ("out1", "o1"),
    )

    out0 = FloatField(default_value=0.0, writable=False)
    o0 = out0

    out1 = FloatField(default_value=0.0, writable=False)
    o1 = out1


class OutAttrOperator(Float2CompoundBaseAttrOperator[OutPlugOperator]):
    __slots__ = ()

    out0 = FloatField(default_value=0.0, writable=False)
    o0 = out0

    out1 = FloatField(default_value=0.0, writable=False)
    o1 = out1


class OutField(Float2CompoundBaseField[OutAttrOperator, OutPlugOperator]):
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


class MultiplyPlugOperator(
    Float2CompoundBasePlugOperator["MultiplyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("multiply0", "mul0"),
        ("multiply1", "mul1"),
    )

    multiply0 = FloatField(default_value=1.0, readable=False)
    mul0 = multiply0

    multiply1 = FloatField(default_value=1.0, readable=False)
    mul1 = multiply1


class MultiplyAttrOperator(
    Float2CompoundBaseAttrOperator[MultiplyPlugOperator]
):
    __slots__ = ()

    multiply0 = FloatField(default_value=1.0, readable=False)
    mul0 = multiply0

    multiply1 = FloatField(default_value=1.0, readable=False)
    mul1 = multiply1


class MultiplyField(
    Float2CompoundBaseField[MultiplyAttrOperator, MultiplyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MultiplyAttrOperator
    PLUG_CLS = MultiplyPlugOperator

    multiply0 = FloatField(default_value=1.0, readable=False)
    mul0 = multiply0

    multiply1 = FloatField(default_value=1.0, readable=False)
    mul1 = multiply1


class OffsetPlugOperator(Float2CompoundBasePlugOperator["OffsetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offset0", "ofs0"),
        ("offset1", "ofs1"),
    )

    offset0 = FloatField(default_value=0.0, readable=False)
    ofs0 = offset0

    offset1 = FloatField(default_value=0.0, readable=False)
    ofs1 = offset1


class OffsetAttrOperator(Float2CompoundBaseAttrOperator[OffsetPlugOperator]):
    __slots__ = ()

    offset0 = FloatField(default_value=0.0, readable=False)
    ofs0 = offset0

    offset1 = FloatField(default_value=0.0, readable=False)
    ofs1 = offset1


class OffsetField(
    Float2CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offset0 = FloatField(default_value=0.0, readable=False)
    ofs0 = offset0

    offset1 = FloatField(default_value=0.0, readable=False)
    ofs1 = offset1
