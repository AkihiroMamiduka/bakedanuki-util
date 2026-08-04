# coding: utf-8
from .._core import DG
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


class GeneratedBdDblCondition(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl_Condition"

    input = DoubleField(default_value=0.0)
    i = input

    operation = OperationEnumField(default_value=0)
    op = operation

    compare = DoubleField(default_value=0.0)
    cmp = compare

    trueValue = DoubleField(default_value=0.0)
    tv = trueValue

    falseValue = DoubleField(default_value=0.0)
    fv = falseValue

    output = DoubleField(default_value=0.0, writable=False)
    o = output
