# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedBdDoubleValue(DG):
    __slots__ = ()

    NODE_TYPE = "bdDoubleValue"

    value = DoubleField(default_value=0.0)
    v = value
