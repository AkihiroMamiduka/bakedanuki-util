# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.dt.string import DataStringField


class AnimBlendNodeEnum(DG):
    __slots__ = ()

    NODE_TYPE = "animBlendNodeEnum"

    weightA = DoubleField()
    wa = weightA

    weightB = DoubleField()
    wb = weightB

    destinationPlug = DataStringField(multi=True)
    dp = destinationPlug

    inputA = ShortField()
    ia = inputA

    inputB = ShortField()
    ib = inputB

    output = ShortField()
    o = output
