# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_range import (
    InputField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class _GeneratedAiRange(DG):
    __slots__ = ()

    NODE_TYPE = "aiRange"

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

    inputMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    input_min = inputMin

    inputMax = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    input_max = inputMax

    outputMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    output_min = outputMin

    outputMax = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    output_max = outputMax

    smoothstep = BoolField(default_value=False)

    contrast = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)

    contrastPivot = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    contrast_pivot = contrastPivot

    bias = FloatField(default_value=0.5, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)

    gain = FloatField(default_value=0.5, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
