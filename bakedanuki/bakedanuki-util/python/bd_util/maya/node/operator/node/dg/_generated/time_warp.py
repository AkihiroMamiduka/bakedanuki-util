# coding: utf-8
from .._core import DG
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.dt.double_array import DataDoubleArrayField


class _GeneratedTimeWarp(DG):
    __slots__ = ()

    NODE_TYPE = "timeWarp"

    input = TimeField(default_value=0.0)
    i = input

    output = TimeField(default_value=0.0, writable=False)
    o = output

    origFrames = DataDoubleArrayField()
    of = origFrames

    endFrames = DataDoubleArrayField()
    ef = endFrames

    interpType = TypedField()
    it = interpType

    apply = TypedField(writable=False)
    a = apply
