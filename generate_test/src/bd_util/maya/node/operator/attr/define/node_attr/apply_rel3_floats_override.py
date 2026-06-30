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


class MultiplyPlugOperator(
    Float3CompoundBasePlugOperator["MultiplyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("multiply0", "mul0"),
        ("multiply1", "mul1"),
        ("multiply2", "mul2"),
    )

    multiply0 = FloatField()
    mul0 = multiply0

    multiply1 = FloatField()
    mul1 = multiply1

    multiply2 = FloatField()
    mul2 = multiply2


class MultiplyAttrOperator(
    Float3CompoundBaseAttrOperator[MultiplyPlugOperator]
):
    __slots__ = ()

    multiply0 = FloatField()
    mul0 = multiply0

    multiply1 = FloatField()
    mul1 = multiply1

    multiply2 = FloatField()
    mul2 = multiply2


class MultiplyField(
    Float3CompoundBaseField[MultiplyAttrOperator, MultiplyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MultiplyAttrOperator
    PLUG_CLS = MultiplyPlugOperator

    multiply0 = FloatField()
    mul0 = multiply0

    multiply1 = FloatField()
    mul1 = multiply1

    multiply2 = FloatField()
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

    offset0 = FloatField()
    ofs0 = offset0

    offset1 = FloatField()
    ofs1 = offset1

    offset2 = FloatField()
    ofs2 = offset2


class OffsetAttrOperator(
    Float3CompoundBaseAttrOperator[OffsetPlugOperator]
):
    __slots__ = ()

    offset0 = FloatField()
    ofs0 = offset0

    offset1 = FloatField()
    ofs1 = offset1

    offset2 = FloatField()
    ofs2 = offset2


class OffsetField(
    Float3CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offset0 = FloatField()
    ofs0 = offset0

    offset1 = FloatField()
    ofs1 = offset1

    offset2 = FloatField()
    ofs2 = offset2
