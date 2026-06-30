# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField


class Record(DG):
    __slots__ = ()

    NODE_TYPE = "record"

    input = DoubleField()
    i = input
