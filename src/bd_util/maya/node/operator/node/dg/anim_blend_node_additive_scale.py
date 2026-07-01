# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.string import DataStringField


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


class AnimBlendNodeAdditiveScale(DG):
    __slots__ = ()

    NODE_TYPE = "animBlendNodeAdditiveScale"

    weightA = DoubleField()
    wa = weightA

    weightB = DoubleField()
    wb = weightB

    destinationPlug = DataStringField(multi=True)
    dp = destinationPlug

    inputA = DoubleField()
    ia = inputA

    inputB = DoubleField()
    ib = inputB

    output = DoubleField()
    o = output

    accumulationMode = AccumulationModeEnumField()
    acm = accumulationMode
