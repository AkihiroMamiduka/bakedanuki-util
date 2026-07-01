# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_range import (
    InputField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiRange(DG):
    __slots__ = ()

    NODE_TYPE = "aiRange"

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

    inputMin = FloatField()
    input_min = inputMin

    inputMax = FloatField()
    input_max = inputMax

    outputMin = FloatField()
    output_min = outputMin

    outputMax = FloatField()
    output_max = outputMax

    smoothstep = BoolField()

    contrast = FloatField()

    contrastPivot = FloatField()
    contrast_pivot = contrastPivot

    bias = FloatField()

    gain = FloatField()
