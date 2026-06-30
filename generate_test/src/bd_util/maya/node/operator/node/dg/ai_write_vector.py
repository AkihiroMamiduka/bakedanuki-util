# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_write_vector import (
    BeautyField,
    InputField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class AiWriteVector(DG):
    __slots__ = ()

    NODE_TYPE = "aiWriteVector"

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
    inputX = input.inputX
    aov_inputx = inputX
    inputY = input.inputY
    aov_inputy = inputY
    inputZ = input.inputZ
    aov_inputz = inputZ

    aovName = DataStringField()
    aov_name = aovName

    blend = BoolField()
    blend_opacity = blend
