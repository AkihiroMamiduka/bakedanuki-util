# coding: utf-8
from .._core import DG
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class _GeneratedLog(DG):
    __slots__ = ()

    NODE_TYPE = "log"

    input = DoubleLinearField(default_value=0.0, min_value=0.0)
    i = input

    base = DoubleLinearField(default_value=2.0, min_value=0.0)
    e = base

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
