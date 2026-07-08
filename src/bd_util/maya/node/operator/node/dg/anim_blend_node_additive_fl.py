# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar_range.float_linear import FloatLinearField
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


class AnimBlendNodeAdditiveFL(DG):
    __slots__ = ()

    NODE_TYPE = "animBlendNodeAdditiveFL"

    weightA = DoubleField(default_value=1.0)
    wa = weightA

    weightB = DoubleField(default_value=1.0)
    wb = weightB

    destinationPlug = DataStringField(multi=True)
    dp = destinationPlug

    inputA = FloatLinearField(default_value=0.0)
    ia = inputA

    inputB = FloatLinearField(default_value=0.0)
    ib = inputB

    output = FloatLinearField(default_value=0.0)
    o = output

    interpolateMode = InterpolateModeEnumField(default_value=0)
    im = interpolateMode
