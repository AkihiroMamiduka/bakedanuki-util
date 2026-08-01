# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedBdDoubleDiv(DG):
    __slots__ = ()

    NODE_TYPE = "bdDoubleDiv"

    input1 = DoubleField(default_value=1.0)
    i1 = input1

    input2 = DoubleField(default_value=1.0)
    i2 = input2

    output = DoubleField(default_value=1.0, writable=False)
    o = output
