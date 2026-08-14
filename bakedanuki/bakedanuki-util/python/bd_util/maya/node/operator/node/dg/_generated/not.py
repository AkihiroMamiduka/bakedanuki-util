# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField


class GeneratedNot(DG):
    __slots__ = ()

    NODE_TYPE = "not"

    input = BoolField(default_value=False)
    i = input

    output = BoolField(default_value=False, writable=False)
    o = output
