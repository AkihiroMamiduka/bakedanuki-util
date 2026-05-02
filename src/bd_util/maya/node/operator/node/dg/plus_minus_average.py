# coding: utf-8

# self
from ._core import DG
from .....attr.enum import AttributeEnum
from ...attr.at.float import FloatAttr
from ...attr.at.enum import EnumAttr
from ...attr.node_attr.plus_minus_average import (
    Input2Attr,
    Input3DAttr,
    Output2DAttr,
    Output3DAttr,
)


class OperationEnum(AttributeEnum):
    NO_OPERATION = "No operation"
    SUM = "Sum"
    SUBTRACT = "Subtract"
    AVERAGE = "Average"


class PlusMinusAverage(DG):
    NODE_TYPE = "plusMinusAverage"

    operation = EnumAttr(enum_name=OperationEnum)
    op = operation
    input1D = FloatAttr(multi=True)
    i1 = input1D
    input2D = Input2Attr(multi=True)
    i2 = input2D
    input3D = Input3DAttr(multi=True)
    i3 = input3D
    output1D = FloatAttr()
    o1 = output1D
    output2D = Output2DAttr()
    o2 = output2D
    output3D = Output3DAttr()
    o3 = output3D
