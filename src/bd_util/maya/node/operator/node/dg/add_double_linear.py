# coding: utf-8
from ._core import DG
from ...attr.at.double_linear import DoubleLinearAttrOperator


class AddDoubleLinear(DG):
    __slots__ = ()

    NODE_TYPE = "addDoubleLinear"

    input1 = DoubleLinearAttrOperator()
    i1 = input1

    input2 = DoubleLinearAttrOperator()
    i2 = input2

    output = DoubleLinearAttrOperator()
    o = output
