# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.float_angle import (
    FloatAngleField,
)
from ....attr.define.std.dt.string import DataStringField


class InterpolateModeEnumPlugOperator(
    EnumPlugOperator["InterpolateModeEnumAttrOperator"]
):
    __slots__ = ()

    ADDITIVE = 0
    MULTIPLY = 1


class InterpolateModeEnumAttrOperator(
    EnumAttrOperator[InterpolateModeEnumPlugOperator]
):
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


class GeneratedAnimBlendNodeAdditiveFA(DG):
    __slots__ = ()

    NODE_TYPE = "animBlendNodeAdditiveFA"

    weightA = DoubleField(default_value=1.0)
    wa = weightA

    weightB = DoubleField(default_value=1.0)
    wb = weightB

    destinationPlug = DataStringField(multi=True)
    dp = destinationPlug

    inputA = FloatAngleField(default_value=0.0)
    ia = inputA

    inputB = FloatAngleField(default_value=0.0)
    ib = inputB

    output = FloatAngleField(default_value=0.0)
    o = output

    interpolateMode = InterpolateModeEnumField(default_value=0)
    im = interpolateMode
