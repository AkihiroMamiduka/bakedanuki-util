# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_cross import (
    Input1Field,
    Input2Field,
    OutTransparencyField,
    OutValueField,
)


class AiCross(DG):
    __slots__ = ()

    NODE_TYPE = "aiCross"

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

    input1 = Input1Field(default_value=(1.0, 1.0, 1.0))
    input1X = input1.input1X
    input1x = input1X
    input1Y = input1.input1Y
    input1y = input1Y
    input1Z = input1.input1Z
    input1z = input1Z

    input2 = Input2Field(default_value=(1.0, 1.0, 1.0))
    input2X = input2.input2X
    input2x = input2X
    input2Y = input2.input2Y
    input2y = input2Y
    input2Z = input2.input2Z
    input2z = input2Z
