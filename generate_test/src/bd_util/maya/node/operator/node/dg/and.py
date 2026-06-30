# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class And(DG):
    __slots__ = ()

    NODE_TYPE = "and"

    input1 = BoolField()
    i1 = input1

    input2 = BoolField()
    i2 = input2

    output = BoolField()
    o = output
