# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_write_color import (
    BeautyField,
    InputField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class AiWriteColor(DG):
    __slots__ = ()

    NODE_TYPE = "aiWriteColor"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField()
    outa = outAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    beautyA = FloatField()
    passthrougha = beautyA

    beauty = BeautyField()
    passthrough = beauty
    beautyR = beauty.beautyR
    passthroughr = beautyR
    beautyG = beauty.beautyG
    passthroughg = beautyG
    beautyB = beauty.beautyB
    passthroughb = beautyB

    input = InputField()
    aov_input = input
    inputR = input.inputR
    aov_inputr = inputR
    inputG = input.inputG
    aov_inputg = inputG
    inputB = input.inputB
    aov_inputb = inputB

    aovName = DataStringField()
    aov_name = aovName

    blend = BoolField()
    blend_opacity = blend
