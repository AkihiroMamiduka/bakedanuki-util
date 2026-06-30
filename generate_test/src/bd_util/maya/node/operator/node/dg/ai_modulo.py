# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_modulo import (
    DivisorField,
    InputField,
    OutColorField,
    OutTransparencyField,
)


class AiModulo(DG):
    __slots__ = ()

    NODE_TYPE = "aiModulo"

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

    divisor = DivisorField()
    divisorR = divisor.divisorR
    divisorr = divisorR
    divisorG = divisor.divisorG
    divisorg = divisorG
    divisorB = divisor.divisorB
    divisorb = divisorB
