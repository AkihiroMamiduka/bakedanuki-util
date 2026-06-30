# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_matrix_multiply_vector import (
    InputField,
    OutTransparencyField,
    OutValueField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField


class TypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    POINT = 0
    VECTOR = 1
    NORMAL = 2


class TypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    POINT = 0
    VECTOR = 1
    NORMAL = 2

    NAME_MAP = {
        POINT: "point",
        VECTOR: "vector",
        NORMAL: "normal",
    }


class TypeEnumField(
    EnumField[TypeEnumAttrOperator, TypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TypeEnumAttrOperator
    PLUG_CLS = TypeEnumPlugOperator


class AiMatrixMultiplyVector(DG):
    __slots__ = ()

    NODE_TYPE = "aiMatrixMultiplyVector"

    outValue = OutValueField()
    out = outValue
    outValueX = outValue.outValueX
    outx = outValueX
    outValueY = outValue.outValueY
    outy = outValueY
    outValueZ = outValue.outValueZ
    outz = outValueZ

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    input = InputField()
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    type = TypeEnumField()

    matrix = FltMatrixField()
