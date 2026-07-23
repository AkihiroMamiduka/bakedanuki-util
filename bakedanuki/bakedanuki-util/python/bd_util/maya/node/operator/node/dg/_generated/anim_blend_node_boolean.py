# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAnimBlendNodeBoolean(DG):
    __slots__ = ()

    NODE_TYPE = "animBlendNodeBoolean"

    weightA = DoubleField(default_value=1.0)
    wa = weightA

    weightB = DoubleField(default_value=1.0)
    wb = weightB

    destinationPlug = DataStringField(multi=True)
    dp = destinationPlug

    inputA = BoolField(default_value=False)
    ia = inputA

    inputB = BoolField(default_value=False)
    ib = inputB

    output = BoolField(default_value=False)
    o = output
