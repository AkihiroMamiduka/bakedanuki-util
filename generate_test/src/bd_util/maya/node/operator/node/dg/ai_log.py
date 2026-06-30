# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_log import (
    BaseField,
    InputField,
    OutColorField,
    OutTransparencyField,
)


class AiLog(DG):
    __slots__ = ()

    NODE_TYPE = "aiLog"

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

    base = BaseField()
    baseR = base.baseR
    baser = baseR
    baseG = base.baseG
    baseg = baseG
    baseB = base.baseB
    baseb = baseB
