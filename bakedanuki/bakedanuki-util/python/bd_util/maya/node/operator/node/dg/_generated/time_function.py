# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.typed import TypedField


class _GeneratedTimeFunction(DG):
    __slots__ = ()

    NODE_TYPE = "timeFunction"

    input = DoubleField(default_value=0.0)
    i = input

    output = TypedField(writable=False)
    o = output
