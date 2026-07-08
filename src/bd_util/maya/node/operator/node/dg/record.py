# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField


class Record(DG):
    __slots__ = ()

    NODE_TYPE = "record"

    input = DoubleField(default_value=0.0, readable=False)
    i = input
