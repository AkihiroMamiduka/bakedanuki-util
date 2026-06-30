# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_clamp import (
    InputField,
    MaxColorField,
    MinColorField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SCALAR = 0
    COLOR = 1


class ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SCALAR = 0
    COLOR = 1

    NAME_MAP = {
        SCALAR: "scalar",
        COLOR: "color",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class AiClamp(DG):
    __slots__ = ()

    NODE_TYPE = "aiClamp"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    input = InputField()
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    mode = ModeEnumField()

    min = FloatField()

    max = FloatField()

    minColor = MinColorField()
    min_color = minColor
    minColorR = minColor.minColorR
    min_colorr = minColorR
    minColorG = minColor.minColorG
    min_colorg = minColorG
    minColorB = minColor.minColorB
    min_colorb = minColorB

    maxColor = MaxColorField()
    max_color = maxColor
    maxColorR = maxColor.maxColorR
    max_colorr = maxColorR
    maxColorG = maxColor.maxColorG
    max_colorg = maxColorG
    maxColorB = maxColor.maxColorB
    max_colorb = maxColorB
