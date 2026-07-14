# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_pow import (
    BaseField,
    ExponentField,
    OutColorField,
    OutTransparencyField,
)


class AiPow(DG):
    __slots__ = ()

    NODE_TYPE = "aiPow"

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

    base = BaseField(default_value=(2.7182817459106445, 2.7182817459106445, 2.7182817459106445))
    baseR = base.baseR
    baser = baseR
    baseG = base.baseG
    baseg = baseG
    baseB = base.baseB
    baseb = baseB

    exponent = ExponentField(default_value=(0.0, 0.0, 0.0))
    exponentR = exponent.exponentR
    exponentr = exponentR
    exponentG = exponent.exponentG
    exponentg = exponentG
    exponentB = exponent.exponentB
    exponentb = exponentB
