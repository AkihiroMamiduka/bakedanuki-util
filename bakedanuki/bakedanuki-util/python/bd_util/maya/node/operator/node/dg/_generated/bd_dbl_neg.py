# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedBdDblNeg(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl_Neg"

    input = DoubleField(default_value=0.0)
    i = input

    output = DoubleField(default_value=0.0, writable=False)
    o = output
