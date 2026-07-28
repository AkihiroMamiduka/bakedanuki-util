# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_float_to_int import OutTransparencyField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class ModeEnumPlugOperator(EnumPlugOperator["ModeEnumAttrOperator"]):
    __slots__ = ()

    ROUND = 0
    TRUNC = 1
    FLOOR = 2
    CEIL = 3


class ModeEnumAttrOperator(EnumAttrOperator[ModeEnumPlugOperator]):
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


class GeneratedAiFloatToInt(DG):
    __slots__ = ()

    NODE_TYPE = "aiFloatToInt"

    outValue = LongField(default_value=0, writable=False)
    out = outValue

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    input = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)

    mode = ModeEnumField(default_value=0)
