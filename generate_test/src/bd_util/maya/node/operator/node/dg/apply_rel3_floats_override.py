# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.apply_rel3_floats_override import (
    MultiplyField,
    OffsetField,
    OriginalField,
    OutField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class ApplyRel3FloatsOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyRel3FloatsOverride"

    enabled = BoolField()
    en = enabled

    out = OutField()
    o = out
    out0 = out.out0
    o0 = out0
    out1 = out.out1
    o1 = out1
    out2 = out.out2
    o2 = out2

    original = OriginalField()
    ori = original
    original0 = original.original0
    ori0 = original0
    original1 = original.original1
    ori1 = original1
    original2 = original.original2
    ori2 = original2

    multiply = MultiplyField()
    mul = multiply
    multiply0 = multiply.multiply0
    mul0 = multiply0
    multiply1 = multiply.multiply1
    mul1 = multiply1
    multiply2 = multiply.multiply2
    mul2 = multiply2

    offset = OffsetField()
    ofs = offset
    offset0 = offset.offset0
    ofs0 = offset0
    offset1 = offset.offset1
    ofs1 = offset1
    offset2 = offset.offset2
    ofs2 = offset2
