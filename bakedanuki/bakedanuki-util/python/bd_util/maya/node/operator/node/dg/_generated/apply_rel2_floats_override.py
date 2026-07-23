# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.apply_rel2_floats_override import (
    MultiplyField,
    OffsetField,
    OriginalField,
    OutField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField


class _GeneratedApplyRel2FloatsOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyRel2FloatsOverride"

    enabled = BoolField(default_value=True, readable=False)
    en = enabled

    out = OutField(default_value=(0.0, 0.0), writable=False)
    o = out
    out0 = out.out0
    o0 = out0
    out1 = out.out1
    o1 = out1

    original = OriginalField(default_value=(0.0, 0.0), readable=False)
    ori = original
    original0 = original.original0
    ori0 = original0
    original1 = original.original1
    ori1 = original1

    multiply = MultiplyField(default_value=(1.0, 1.0), readable=False)
    mul = multiply
    multiply0 = multiply.multiply0
    mul0 = multiply0
    multiply1 = multiply.multiply1
    mul1 = multiply1

    offset = OffsetField(default_value=(0.0, 0.0), readable=False)
    ofs = offset
    offset0 = offset.offset0
    ofs0 = offset0
    offset1 = offset.offset1
    ofs1 = offset1
