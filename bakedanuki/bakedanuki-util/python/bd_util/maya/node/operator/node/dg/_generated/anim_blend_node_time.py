# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.unit_scalar.time import TimeField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAnimBlendNodeTime(DG):
    __slots__ = ()

    NODE_TYPE = "animBlendNodeTime"

    weightA = DoubleField(default_value=1.0)
    wa = weightA

    weightB = DoubleField(default_value=1.0)
    wb = weightB

    destinationPlug = DataStringField(multi=True)
    dp = destinationPlug

    inputA = TimeField(default_value=0.0)
    ia = inputA

    inputB = TimeField(default_value=0.0)
    ib = inputB

    output = TimeField(default_value=0.0, writable=False)
    o = output
