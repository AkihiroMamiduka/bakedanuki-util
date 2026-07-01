# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.dot_product import (
    Input1Field,
    Input2Field,
)
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class DotProduct(DG):
    __slots__ = ()

    NODE_TYPE = "dotProduct"

    input1 = Input1Field()
    i1 = input1
    input1X = input1.input1X
    i1x = input1X
    input1Y = input1.input1Y
    i1y = input1Y
    input1Z = input1.input1Z
    i1z = input1Z

    input2 = Input2Field()
    i2 = input2
    input2X = input2.input2X
    i2x = input2X
    input2Y = input2.input2Y
    i2y = input2Y
    input2Z = input2.input2Z
    i2z = input2Z

    output = DoubleLinearField()
    o = output
