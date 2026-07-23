# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_multiply import (
    Input1Field,
    Input2Field,
    OutColorField,
    OutTransparencyField,
)


class _GeneratedAiMultiply(DG):
    __slots__ = ()

    NODE_TYPE = "aiMultiply"

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

    input1 = Input1Field(default_value=(1.0, 1.0, 1.0))
    input1R = input1.input1R
    input1r = input1R
    input1G = input1.input1G
    input1g = input1G
    input1B = input1.input1B
    input1b = input1B

    input2 = Input2Field(default_value=(1.0, 1.0, 1.0))
    input2R = input2.input2R
    input2r = input2R
    input2G = input2.input2G
    input2g = input2G
    input2B = input2.input2B
    input2b = input2B
