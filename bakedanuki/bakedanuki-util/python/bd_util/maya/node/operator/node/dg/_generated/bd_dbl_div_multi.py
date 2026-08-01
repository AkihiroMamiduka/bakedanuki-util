# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedBdDblDivMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl_DivMulti"

    input = DoubleField(multi=True, default_value=1.0)
    i = input

    output = DoubleField(default_value=1.0, writable=False)
    o = output
