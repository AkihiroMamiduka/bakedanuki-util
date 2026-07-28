# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_log import (
    BaseField,
    InputField,
    OutColorField,
    OutTransparencyField,
)


class GeneratedAiLog(DG):
    __slots__ = ()

    NODE_TYPE = "aiLog"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
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

    base = BaseField(
        default_value=(
            2.7182817459106445,
            2.7182817459106445,
            2.7182817459106445,
        )
    )
    baseR = base.baseR
    baser = baseR
    baseG = base.baseG
    baseg = baseG
    baseB = base.baseB
    baseb = baseB
