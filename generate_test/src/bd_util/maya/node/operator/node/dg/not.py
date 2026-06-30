# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class Not(DG):
    __slots__ = ()

    NODE_TYPE = "not"

    input = BoolField()
    i = input

    output = BoolField()
    o = output
