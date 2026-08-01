# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedBdSubDoubleMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdSubDoubleMulti"

    input = DoubleField(multi=True, default_value=0.0)
    i = input

    output = DoubleField(default_value=0.0, writable=False)
    o = output
