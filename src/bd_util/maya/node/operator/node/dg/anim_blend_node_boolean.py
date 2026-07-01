# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.string import DataStringField


class AnimBlendNodeBoolean(DG):
    __slots__ = ()

    NODE_TYPE = "animBlendNodeBoolean"

    weightA = DoubleField()
    wa = weightA

    weightB = DoubleField()
    wb = weightB

    destinationPlug = DataStringField(multi=True)
    dp = destinationPlug

    inputA = BoolField()
    ia = inputA

    inputB = BoolField()
    ib = inputB

    output = BoolField()
    o = output
