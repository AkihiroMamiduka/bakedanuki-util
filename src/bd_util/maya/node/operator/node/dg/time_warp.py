# coding: utf-8
from ._core import DG
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.double_array import DataDoubleArrayField


class TimeWarp(DG):
    __slots__ = ()

    NODE_TYPE = "timeWarp"

    input = TimeField()
    i = input

    output = TimeField()
    o = output

    origFrames = DataDoubleArrayField()
    of = origFrames

    endFrames = DataDoubleArrayField()
    ef = endFrames

    interpType = TypedField()
    it = interpType

    apply = TypedField()
    a = apply
