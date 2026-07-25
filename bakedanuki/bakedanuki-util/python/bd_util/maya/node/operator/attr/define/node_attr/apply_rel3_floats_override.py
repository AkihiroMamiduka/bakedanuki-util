# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
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

    out0 = FloatField(default_value=0.0, writable=False)
    o0 = out0

    out1 = FloatField(default_value=0.0, writable=False)
    o1 = out1

    out2 = FloatField(default_value=0.0, writable=False)
    o2 = out2


class OutAttrOperator(
    Float3CompoundBaseAttrOperator[OutPlugOperator]
):
    __slots__ = ()

    out0 = FloatField(default_value=0.0, writable=False)
    o0 = out0

    out1 = FloatField(default_value=0.0, writable=False)
    o1 = out1

    out2 = FloatField(default_value=0.0, writable=False)
    o2 = out2


class OutField(
    Float3CompoundBaseField[OutAttrOperator, OutPlugOperator]
):
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


class MultiplyPlugOperator(
    Float3CompoundBasePlugOperator["MultiplyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("multiply0", "mul0"),
        ("multiply1", "mul1"),
        ("multiply2", "mul2"),
    )

    multiply0 = FloatField(default_value=1.0, readable=False)
    mul0 = multiply0

    multiply1 = FloatField(default_value=1.0, readable=False)
    mul1 = multiply1

    multiply2 = FloatField(default_value=1.0, readable=False)
    mul2 = multiply2


class MultiplyAttrOperator(
    Float3CompoundBaseAttrOperator[MultiplyPlugOperator]
):
    __slots__ = ()

    multiply0 = FloatField(default_value=1.0, readable=False)
    mul0 = multiply0

    multiply1 = FloatField(default_value=1.0, readable=False)
    mul1 = multiply1

    multiply2 = FloatField(default_value=1.0, readable=False)
    mul2 = multiply2


class MultiplyField(
    Float3CompoundBaseField[MultiplyAttrOperator, MultiplyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MultiplyAttrOperator
    PLUG_CLS = MultiplyPlugOperator

    multiply0 = FloatField(default_value=1.0, readable=False)
    mul0 = multiply0

    multiply1 = FloatField(default_value=1.0, readable=False)
    mul1 = multiply1

    multiply2 = FloatField(default_value=1.0, readable=False)
    mul2 = multiply2


class OffsetPlugOperator(
    Float3CompoundBasePlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offset0", "ofs0"),
        ("offset1", "ofs1"),
        ("offset2", "ofs2"),
    )

    offset0 = FloatField(default_value=0.0, readable=False)
    ofs0 = offset0

    offset1 = FloatField(default_value=0.0, readable=False)
    ofs1 = offset1

    offset2 = FloatField(default_value=0.0, readable=False)
    ofs2 = offset2


class OffsetAttrOperator(
    Float3CompoundBaseAttrOperator[OffsetPlugOperator]
):
    __slots__ = ()

    offset0 = FloatField(default_value=0.0, readable=False)
    ofs0 = offset0

    offset1 = FloatField(default_value=0.0, readable=False)
    ofs1 = offset1

    offset2 = FloatField(default_value=0.0, readable=False)
    ofs2 = offset2


class OffsetField(
    Float3CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offset0 = FloatField(default_value=0.0, readable=False)
    ofs0 = offset0

    offset1 = FloatField(default_value=0.0, readable=False)
    ofs1 = offset1

    offset2 = FloatField(default_value=0.0, readable=False)
    ofs2 = offset2
