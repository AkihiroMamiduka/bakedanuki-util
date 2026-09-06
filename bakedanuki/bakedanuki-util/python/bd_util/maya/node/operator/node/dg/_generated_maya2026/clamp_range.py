# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedClampRange(DG):
    __slots__ = ()

    NODE_TYPE = "clampRange"

    input = DoubleField(default_value=0.0)
    i = input

    minimum = DoubleField(default_value=0.0)
    min = minimum

    maximum = DoubleField(default_value=1.0)
    max = maximum

    output = DoubleField(default_value=0.0, writable=False)
    o = output
