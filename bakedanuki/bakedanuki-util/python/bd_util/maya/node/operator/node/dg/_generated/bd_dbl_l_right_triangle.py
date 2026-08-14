# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class SolveForEnumPlugOperator(EnumPlugOperator["SolveForEnumAttrOperator"]):
    __slots__ = ()

    HYPOTENUSE = 0
    LEGA = 1
    LEGB = 2


class SolveForEnumAttrOperator(EnumAttrOperator[SolveForEnumPlugOperator]):
    __slots__ = ()

    HYPOTENUSE = 0
    LEGA = 1
    LEGB = 2

    NAME_MAP = {
        HYPOTENUSE: "Hypotenuse",
        LEGA: "LegA",
        LEGB: "LegB",
    }


class SolveForEnumField(
    EnumField[SolveForEnumAttrOperator, SolveForEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SolveForEnumAttrOperator
    PLUG_CLS = SolveForEnumPlugOperator


class GeneratedBdDblLRightTriangle(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblL_RightTriangle"

    solveFor = SolveForEnumField(default_value=0)
    sf = solveFor

    legA = DoubleLinearField(default_value=0.0)
    la = legA

    legB = DoubleLinearField(default_value=0.0)
    lb = legB

    hypotenuse = DoubleLinearField(default_value=0.0)
    h = hypotenuse

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output

    isValid = BoolField(default_value=True, writable=False)
    iv = isValid
