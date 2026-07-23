# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.apply_abs2_floats_override import (
    OriginalField,
    OutField,
    ValueField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField


class _GeneratedApplyAbs2FloatsOverride(DG):
    __slots__ = ()

    NODE_TYPE = "applyAbs2FloatsOverride"

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

    value = ValueField(default_value=(0.0, 0.0), readable=False)
    val = value
    value0 = value.value0
    val0 = value0
    value1 = value.value1
    val1 = value1
