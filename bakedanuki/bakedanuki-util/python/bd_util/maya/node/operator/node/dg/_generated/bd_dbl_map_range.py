# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedBdDblMapRange(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl_MapRange"

    input = DoubleField(default_value=0.0)
    i = input

    sourceMinimum = DoubleField(default_value=0.0)
    smin = sourceMinimum

    sourceMaximum = DoubleField(default_value=1.0)
    smax = sourceMaximum

    targetMinimum = DoubleField(default_value=0.0)
    tmin = targetMinimum

    targetMaximum = DoubleField(default_value=1.0)
    tmax = targetMaximum

    clamp = BoolField(default_value=True)
    c = clamp

    output = DoubleField(default_value=0.0, writable=False)
    o = output
