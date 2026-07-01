# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class Log(DG):
    __slots__ = ()

    NODE_TYPE = "log"

    input = DoubleLinearField()
    i = input

    base = DoubleLinearField()
    e = base

    output = DoubleLinearField()
    o = output
