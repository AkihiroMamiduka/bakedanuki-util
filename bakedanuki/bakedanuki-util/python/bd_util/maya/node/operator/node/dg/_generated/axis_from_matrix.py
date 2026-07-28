# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.axis_from_matrix import OutputField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField


class AxisEnumPlugOperator(EnumPlugOperator["AxisEnumAttrOperator"]):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2
    MINUS_X = 3
    MINUS_Y = 4
    MINUS_Z = 5


class AxisEnumAttrOperator(EnumAttrOperator[AxisEnumPlugOperator]):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2
    MINUS_X = 3
    MINUS_Y = 4
    MINUS_Z = 5

    NAME_MAP = {
        X: "X",
        Y: "Y",
        Z: "Z",
        MINUS_X: "-X",
        MINUS_Y: "-Y",
        MINUS_Z: "-Z",
    }


class AxisEnumField(
    EnumField[AxisEnumAttrOperator, AxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisEnumAttrOperator
    PLUG_CLS = AxisEnumPlugOperator


class GeneratedAxisFromMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "axisFromMatrix"

    input = MatrixField(readable=False)
    i = input

    axis = AxisEnumField(default_value=0)
    op = axis

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
