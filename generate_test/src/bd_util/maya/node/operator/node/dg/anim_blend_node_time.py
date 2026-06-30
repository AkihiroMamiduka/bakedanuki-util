# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField


class AnimBlendNodeTime(DG):
    __slots__ = ()

    NODE_TYPE = "animBlendNodeTime"

    weightA = DoubleField()
    wa = weightA

    weightB = DoubleField()
    wb = weightB

    destinationPlug = DataStringField(multi=True)
    dp = destinationPlug

    inputA = TimeField()
    ia = inputA

    inputB = TimeField()
    ib = inputB

    output = TimeField()
    o = output
