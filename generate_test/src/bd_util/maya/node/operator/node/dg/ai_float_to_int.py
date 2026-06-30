# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_float_to_int import OutTransparencyField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ROUND = 0
    TRUNC = 1
    FLOOR = 2
    CEIL = 3


class ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ROUND = 0
    TRUNC = 1
    FLOOR = 2
    CEIL = 3

    NAME_MAP = {
        ROUND: "round",
        TRUNC: "trunc",
        FLOOR: "floor",
        CEIL: "ceil",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class AiFloatToInt(DG):
    __slots__ = ()

    NODE_TYPE = "aiFloatToInt"

    outValue = LongField()
    out = outValue

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    input = FloatField()

    mode = ModeEnumField()
