# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_matrix_interpolate import (
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class TypeEnumPlugOperator(EnumPlugOperator["TypeEnumAttrOperator"]):
    __slots__ = ()

    TIME = 0
    VALUE = 1


class TypeEnumAttrOperator(EnumAttrOperator[TypeEnumPlugOperator]):
    __slots__ = ()

    TIME = 0
    VALUE = 1

    NAME_MAP = {
        TIME: "time",
        VALUE: "value",
    }


class TypeEnumField(EnumField[TypeEnumAttrOperator, TypeEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = TypeEnumAttrOperator
    PLUG_CLS = TypeEnumPlugOperator


class GeneratedAiMatrixInterpolate(DG):
    __slots__ = ()

    NODE_TYPE = "aiMatrixInterpolate"

    outValue = FltMatrixField(writable=False)
    out = outValue

    outTransparency = OutTransparencyField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    placementMatrix = FltMatrixField()
    matrix = placementMatrix

    type = TypeEnumField(default_value=0)

    value = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
