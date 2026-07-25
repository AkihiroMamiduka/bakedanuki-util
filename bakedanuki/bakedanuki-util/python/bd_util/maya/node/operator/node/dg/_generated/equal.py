# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField


class _GeneratedEqual(DG):
    __slots__ = ()

    NODE_TYPE = "equal"

    input1 = DoubleLinearField(default_value=0.0)
    i1 = input1

    input2 = DoubleLinearField(default_value=0.0)
    i2 = input2

    epsilon = DoubleLinearField(default_value=0.0)
    e = epsilon

    output = BoolField(default_value=False, writable=False)
    o = output
