# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.cross_product import (
    Input1Field,
    Input2Field,
    OutputField,
)


class _GeneratedCrossProduct(DG):
    __slots__ = ()

    NODE_TYPE = "crossProduct"

    input1 = Input1Field(default_value=(0.0, 0.0, 0.0), readable=False)
    i1 = input1
    input1X = input1.input1X
    i1x = input1X
    input1Y = input1.input1Y
    i1y = input1Y
    input1Z = input1.input1Z
    i1z = input1Z

    input2 = Input2Field(default_value=(0.0, 0.0, 0.0), readable=False)
    i2 = input2
    input2X = input2.input2X
    i2x = input2X
    input2Y = input2.input2Y
    i2y = input2Y
    input2Z = input2.input2Z
    i2z = input2Z

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
