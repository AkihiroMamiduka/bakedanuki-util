# coding: utf-8
from ._core import DG
from ...attr.at.double_linear import DoubleLinearField


class AddDoubleLinear(DG):
    __slots__ = ()

    NODE_TYPE = "addDoubleLinear"

    input1 = DoubleLinearField()
    i1 = input1

    input2 = DoubleLinearField()
    i2 = input2

    output = DoubleLinearField()
    o = output
