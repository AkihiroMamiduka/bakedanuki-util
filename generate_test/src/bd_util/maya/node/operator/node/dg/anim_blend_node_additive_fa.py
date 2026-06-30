# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar_range.float_angle import FloatAngleField
from ...attr.define.std.dt.string import DataStringField


class InterpolateModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ADDITIVE = 0
    MULTIPLY = 1


class InterpolateModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ADDITIVE = 0
    MULTIPLY = 1

    NAME_MAP = {
        ADDITIVE: "additive",
        MULTIPLY: "multiply",
    }


class InterpolateModeEnumField(
    EnumField[InterpolateModeEnumAttrOperator, InterpolateModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InterpolateModeEnumAttrOperator
    PLUG_CLS = InterpolateModeEnumPlugOperator


class AnimBlendNodeAdditiveFA(DG):
    __slots__ = ()

    NODE_TYPE = "animBlendNodeAdditiveFA"

    weightA = DoubleField()
    wa = weightA

    weightB = DoubleField()
    wb = weightB

    destinationPlug = DataStringField(multi=True)
    dp = destinationPlug

    inputA = FloatAngleField()
    ia = inputA

    inputB = FloatAngleField()
    ib = inputB

    output = FloatAngleField()
    o = output

    interpolateMode = InterpolateModeEnumField()
    im = interpolateMode
