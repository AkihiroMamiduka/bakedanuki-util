# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl3_condition import (
    FalseValueField,
    OutputField,
    TrueValueField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class OperationEnumPlugOperator(EnumPlugOperator["OperationEnumAttrOperator"]):
    __slots__ = ()

    EQUAL = 0
    NOT_EQUAL = 1
    GREATER_THAN = 2
    GREATER_OR_EQUAL = 3
    LESS_THAN = 4
    LESS_OR_EQUAL = 5


class OperationEnumAttrOperator(EnumAttrOperator[OperationEnumPlugOperator]):
    __slots__ = ()

    EQUAL = 0
    NOT_EQUAL = 1
    GREATER_THAN = 2
    GREATER_OR_EQUAL = 3
    LESS_THAN = 4
    LESS_OR_EQUAL = 5

    NAME_MAP = {
        EQUAL: "Equal",
        NOT_EQUAL: "Not Equal",
        GREATER_THAN: "Greater Than",
        GREATER_OR_EQUAL: "Greater or Equal",
        LESS_THAN: "Less Than",
        LESS_OR_EQUAL: "Less or Equal",
    }


class OperationEnumField(
    EnumField[OperationEnumAttrOperator, OperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OperationEnumAttrOperator
    PLUG_CLS = OperationEnumPlugOperator


class GeneratedBdDbl3Condition(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl3_Condition"

    input = DoubleField(default_value=0.0)
    i = input

    operation = OperationEnumField(default_value=0)
    op = operation

    compare = DoubleField(default_value=0.0)
    cmp = compare

    trueValue = TrueValueField(default_value=(0.0, 0.0, 0.0))
    tv = trueValue
    trueValueX = trueValue.trueValueX
    tvx = trueValueX
    trueValueY = trueValue.trueValueY
    tvy = trueValueY
    trueValueZ = trueValue.trueValueZ
    tvz = trueValueZ

    falseValue = FalseValueField(default_value=(0.0, 0.0, 0.0))
    fv = falseValue
    falseValueX = falseValue.falseValueX
    fvx = falseValueX
    falseValueY = falseValue.falseValueY
    fvy = falseValueY
    falseValueZ = falseValue.falseValueZ
    fvz = falseValueZ

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
