# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAnimBlendNodeEnum(DG):
    __slots__ = ()

    NODE_TYPE = "animBlendNodeEnum"

    weightA = DoubleField(default_value=1.0)
    wa = weightA

    weightB = DoubleField(default_value=1.0)
    wb = weightB

    destinationPlug = DataStringField(multi=True)
    dp = destinationPlug

    inputA = ShortField(default_value=0)
    ia = inputA

    inputB = ShortField(default_value=0)
    ib = inputB

    output = ShortField(default_value=0)
    o = output
