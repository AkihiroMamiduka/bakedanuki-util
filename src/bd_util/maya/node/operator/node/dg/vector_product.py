# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.vector_product import (
    Input1Field,
    Input2Field,
    OutputField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class OperationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_OPERATION = 0
    DOT_PRODUCT = 1
    CROSS_PRODUCT = 2
    VECTOR_MATRIX_PRODUCT = 3
    POINT_MATRIX_PRODUCT = 4


class OperationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NO_OPERATION = 0
    DOT_PRODUCT = 1
    CROSS_PRODUCT = 2
    VECTOR_MATRIX_PRODUCT = 3
    POINT_MATRIX_PRODUCT = 4

    NAME_MAP = {
        NO_OPERATION: "No operation",
        DOT_PRODUCT: "Dot Product",
        CROSS_PRODUCT: "Cross Product",
        VECTOR_MATRIX_PRODUCT: "Vector Matrix Product",
        POINT_MATRIX_PRODUCT: "Point Matrix Product",
    }


class OperationEnumField(
    EnumField[OperationEnumAttrOperator, OperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OperationEnumAttrOperator
    PLUG_CLS = OperationEnumPlugOperator


class VectorProduct(DG):
    __slots__ = ()

    NODE_TYPE = "vectorProduct"

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

    input2 = Input2Field(default_value=(0.0, 0.0, 0.0))
    i2 = input2
    input2X = input2.input2X
    i2x = input2X
    input2Y = input2.input2Y
    i2y = input2Y
    input2Z = input2.input2Z
    i2z = input2Z

    matrix = FltMatrixField()
    m = matrix

    normalizeOutput = BoolField(default_value=False)
    no = normalizeOutput

    output = OutputField(default_value=(1.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
