# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.dt.string import DataStringField


class AccumulationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ADDITIVE = 0
    MULTIPLY = 1


class AccumulationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ADDITIVE = 0
    MULTIPLY = 1

    NAME_MAP = {
        ADDITIVE: "additive",
        MULTIPLY: "multiply",
    }


class AccumulationModeEnumField(
    EnumField[AccumulationModeEnumAttrOperator, AccumulationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AccumulationModeEnumAttrOperator
    PLUG_CLS = AccumulationModeEnumPlugOperator


class _GeneratedAnimBlendNodeAdditiveScale(DG):
    __slots__ = ()

    NODE_TYPE = "animBlendNodeAdditiveScale"

    weightA = DoubleField(default_value=1.0)
    wa = weightA

    weightB = DoubleField(default_value=1.0)
    wb = weightB

    destinationPlug = DataStringField(multi=True)
    dp = destinationPlug

    inputA = DoubleField(default_value=0.0)
    ia = inputA

    inputB = DoubleField(default_value=0.0)
    ib = inputB

    output = DoubleField(default_value=0.0)
    o = output

    accumulationMode = AccumulationModeEnumField(default_value=0)
    acm = accumulationMode
