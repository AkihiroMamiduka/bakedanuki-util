# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class CombinationMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MULTIPLICATION = 0
    LOWEST_WEIGHTING = 1
    SMOOTH = 2


class CombinationMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MULTIPLICATION = 0
    LOWEST_WEIGHTING = 1
    SMOOTH = 2

    NAME_MAP = {
        MULTIPLICATION: "multiplication",
        LOWEST_WEIGHTING: "lowest weighting",
        SMOOTH: "smooth",
    }


class CombinationMethodEnumField(
    EnumField[CombinationMethodEnumAttrOperator, CombinationMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CombinationMethodEnumAttrOperator
    PLUG_CLS = CombinationMethodEnumPlugOperator


class CombinationShape(DG):
    __slots__ = ()

    NODE_TYPE = "combinationShape"

    inputWeight = FloatField(multi=True, default_value=0.0)
    iw = inputWeight

    combinationMethod = CombinationMethodEnumField(default_value=0)
    cm = combinationMethod

    outputWeight = FloatField(default_value=0.0)
    ow = outputWeight
