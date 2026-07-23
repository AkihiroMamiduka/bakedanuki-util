# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar.bool import BoolField


class _GeneratedNot(DG):
    __slots__ = ()

    NODE_TYPE = "not"

    input = BoolField(default_value=False)
    i = input

    output = BoolField(default_value=False, writable=False)
    o = output
