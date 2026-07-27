# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField


class GeneratedAnd(DG):
    __slots__ = ()

    NODE_TYPE = "and"

    input1 = BoolField(default_value=False)
    i1 = input1

    input2 = BoolField(default_value=False)
    i2 = input2

    output = BoolField(default_value=False, writable=False)
    o = output
