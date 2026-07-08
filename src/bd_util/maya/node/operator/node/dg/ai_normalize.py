# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_normalize import (
    InputField,
    OutTransparencyField,
    OutValueField,
)


class AiNormalize(DG):
    __slots__ = ()

    NODE_TYPE = "aiNormalize"

    outValue = OutValueField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outValue
    outValueX = outValue.outValueX
    outx = outValueX
    outValueY = outValue.outValueY
    outy = outValueY
    outValueZ = outValue.outValueZ
    outz = outValueZ

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    input = InputField(default_value=(1.0, 1.0, 1.0))
    inputX = input.inputX
    inputx = inputX
    inputY = input.inputY
    inputy = inputY
    inputZ = input.inputZ
    inputz = inputZ
