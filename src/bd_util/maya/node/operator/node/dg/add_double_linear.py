# coding: utf-8
from ._core import DG
from ...attr.at.double import DoubleAttr


class AddDoubleLinear(DG):
    NODE_TYPE = "addDoubleLinear"

    input1 = DoubleAttr()
    i1 = input1
    input2 = DoubleAttr()
    i2 = input2
    output = DoubleAttr()
    o = output
