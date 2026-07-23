# coding: utf-8
from .._core import DG
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class _GeneratedAbsolute(DG):
    __slots__ = ()

    NODE_TYPE = "absolute"

    input = DoubleLinearField(default_value=0.0)
    i = input

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
