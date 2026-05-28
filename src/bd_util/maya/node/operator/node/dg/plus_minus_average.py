# coding: utf-8
from ._core import DG
from ...attr.node_attr.plus_minus_average import (
    Input2DAttr,
    Input3DAttr,
    Output2DAttr,
    Output3DAttr,
)
from ...attr.at.enum import EnumAttr, EnumPlug
from ...attr.at.float import FloatAttr


class OperationEnumPlug(EnumPlug):
    NO_OPERATION = 0
    SUM = 1
    SUBTRACT = 2
    AVERAGE = 3


class OperationEnumAttr(EnumAttr):
    PLUG_CLS = OperationEnumPlug

    NO_OPERATION = 0
    SUM = 1
    SUBTRACT = 2
    AVERAGE = 3

    NAME_MAP = {
        NO_OPERATION: "No operation",
        SUM: "Sum",
        SUBTRACT: "Subtract",
        AVERAGE: "Average",
    }


class PlusMinusAverage(DG):
    __slots__ = ()

    NODE_TYPE = "plusMinusAverage"

    operation = OperationEnumAttr()
    op = operation

    input1D = FloatAttr(multi=True)
    i1 = input1D

    input2D = Input2DAttr(multi=True)
    i2 = input2D

    input3D = Input3DAttr(multi=True)
    i3 = input3D

    output1D = FloatAttr()
    o1 = output1D

    output2D = Output2DAttr()
    o2 = output2D
    output2Dx = output2D.output2Dx
    o2x = output2Dx
    output2Dy = output2D.output2Dy
    o2y = output2Dy

    output3D = Output3DAttr()
    o3 = output3D
    output3Dx = output3D.output3Dx
    o3x = output3Dx
    output3Dy = output3D.output3Dy
    o3y = output3Dy
    output3Dz = output3D.output3Dz
    o3z = output3Dz
