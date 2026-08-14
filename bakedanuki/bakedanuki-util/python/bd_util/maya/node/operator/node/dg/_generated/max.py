# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class GeneratedMax(DG):
    __slots__ = ()

    NODE_TYPE = "max"

    input = DoubleLinearField(multi=True, default_value=0.0)
    i = input

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
