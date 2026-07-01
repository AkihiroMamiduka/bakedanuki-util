# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.typed import TypedField


class TimeFunction(DG):
    __slots__ = ()

    NODE_TYPE = "timeFunction"

    input = DoubleField()
    i = input

    output = TypedField()
    o = output
