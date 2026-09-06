# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedEqual(DG):
    __slots__ = ()

    NODE_TYPE = "equal"

    input1 = DoubleField(default_value=0.0)
    i1 = input1

    input2 = DoubleField(default_value=0.0)
    i2 = input2

    epsilon = DoubleField(default_value=0.0)
    e = epsilon

    output = BoolField(default_value=False, writable=False)
    o = output
