# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.plus_minus_average import (
    Input2DField,
    Input3DField,
    Output2DField,
    Output3DField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class OperationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_OPERATION = 0
    SUM = 1
    SUBTRACT = 2
    AVERAGE = 3


class OperationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

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


class OperationEnumField(
    EnumField[OperationEnumAttrOperator, OperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OperationEnumAttrOperator
    PLUG_CLS = OperationEnumPlugOperator


class PlusMinusAverage(DG):
    __slots__ = ()

    NODE_TYPE = "plusMinusAverage"

    operation = OperationEnumField(default_value=1)
    op = operation

    input1D = FloatField(multi=True, default_value=0.0, readable=False)
    i1 = input1D

    input2D = Input2DField(multi=True, default_value=(0.0, 0.0), readable=False)
    i2 = input2D

    input3D = Input3DField(multi=True, default_value=(0.0, 0.0, 0.0), readable=False)
    i3 = input3D

    output1D = FloatField(default_value=0.0, writable=False)
    o1 = output1D

    output2D = Output2DField(default_value=(0.0, 0.0), writable=False)
    o2 = output2D
    output2Dx = output2D.output2Dx
    o2x = output2Dx
    output2Dy = output2D.output2Dy
    o2y = output2Dy

    output3D = Output3DField(default_value=(0.0, 0.0, 0.0), writable=False)
    o3 = output3D
    output3Dx = output3D.output3Dx
    o3x = output3Dx
    output3Dy = output3D.output3Dy
    o3y = output3Dy
    output3Dz = output3D.output3Dz
    o3z = output3Dz
