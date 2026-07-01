# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
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


class AnimBlendNodeAdditiveI16(DG):
    __slots__ = ()

    NODE_TYPE = "animBlendNodeAdditiveI16"

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

    interpolateMode = InterpolateModeEnumField()
    im = interpolateMode
