# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.multiply_divide import (
    Input1Field,
    Input2Field,
    OutputField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


class OperationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_OPERATION = 0
    MULTIPLY = 1
    DIVIDE = 2
    POWER = 3


class OperationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NO_OPERATION = 0
    MULTIPLY = 1
    DIVIDE = 2
    POWER = 3

    NAME_MAP = {
        NO_OPERATION: "No operation",
        MULTIPLY: "Multiply",
        DIVIDE: "Divide",
        POWER: "Power",
    }


class OperationEnumField(
    EnumField[OperationEnumAttrOperator, OperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OperationEnumAttrOperator
    PLUG_CLS = OperationEnumPlugOperator


class GeneratedMultiplyDivide(DG):
    __slots__ = ()

    NODE_TYPE = "multiplyDivide"

    operation = OperationEnumField(default_value=1)
    op = operation

    input1 = Input1Field(default_value=(0.0, 0.0, 0.0))
    i1 = input1
    input1X = input1.input1X
    i1x = input1X
    input1Y = input1.input1Y
    i1y = input1Y
    input1Z = input1.input1Z
    i1z = input1Z

    input2 = Input2Field(default_value=(1.0, 1.0, 1.0))
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
