# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_clamp import (
    InputField,
    MaxColorField,
    MinColorField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class ModeEnumPlugOperator(EnumPlugOperator["ModeEnumAttrOperator"]):
    __slots__ = ()

    SCALAR = 0
    COLOR = 1


class ModeEnumAttrOperator(EnumAttrOperator[ModeEnumPlugOperator]):
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


class GeneratedAiClamp(DG):
    __slots__ = ()

    NODE_TYPE = "aiClamp"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    input = InputField(default_value=(0.0, 0.0, 0.0))
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    mode = ModeEnumField(default_value=0)

    min = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    max = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)

    minColor = MinColorField(default_value=(0.0, 0.0, 0.0))
    min_color = minColor
    minColorR = minColor.minColorR
    min_colorr = minColorR
    minColorG = minColor.minColorG
    min_colorg = minColorG
    minColorB = minColor.minColorB
    min_colorb = minColorB

    maxColor = MaxColorField(default_value=(1.0, 1.0, 1.0))
    max_color = maxColor
    maxColorR = maxColor.maxColorR
    max_colorr = maxColorR
    maxColorG = maxColor.maxColorG
    max_colorg = maxColorG
    maxColorB = maxColor.maxColorB
    max_colorb = maxColorB
