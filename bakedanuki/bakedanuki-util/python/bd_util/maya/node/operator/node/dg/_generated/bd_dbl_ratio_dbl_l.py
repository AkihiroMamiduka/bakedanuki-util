# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class GeneratedBdDblRatioDblL(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl_RatioDblL"

    input = DoubleLinearField(default_value=0.0)
    i = input

    base = DoubleLinearField(default_value=1.0)
    b = base

    output = DoubleField(default_value=0.0, writable=False)
    o = output
