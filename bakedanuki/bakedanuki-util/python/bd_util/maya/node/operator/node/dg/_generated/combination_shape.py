# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


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


class _GeneratedCombinationShape(DG):
    __slots__ = ()

    NODE_TYPE = "combinationShape"

    inputWeight = FloatField(multi=True, default_value=0.0)
    iw = inputWeight

    combinationMethod = CombinationMethodEnumField(default_value=0)
    cm = combinationMethod

    outputWeight = FloatField(default_value=0.0)
    ow = outputWeight
