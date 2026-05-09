# coding: utf-8
from ._core import DG
from ...attr.at.double_linear import DoubleLinearAttr


class AddDoubleLinear(DG):
    __slots__ = ()

    NODE_TYPE = "addDoubleLinear"

    input1 = DoubleLinearAttr()
    i1 = input1

    input2 = DoubleLinearAttr()
    i2 = input2

    output = DoubleLinearAttr()
    o = output
