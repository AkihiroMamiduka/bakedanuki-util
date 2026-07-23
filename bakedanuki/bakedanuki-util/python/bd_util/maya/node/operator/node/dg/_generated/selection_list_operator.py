# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.typed import TypedField


class OperationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UNION = 0
    INTERSECTION = 1
    NOT_MINUS_INTERSECTION = 2
    DIFFERENCE = 3


class OperationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UNION = 0
    INTERSECTION = 1
    NOT_MINUS_INTERSECTION = 2
    DIFFERENCE = 3

    NAME_MAP = {
        UNION: "Union",
        INTERSECTION: "Intersection",
        NOT_MINUS_INTERSECTION: "Not-Intersection",
        DIFFERENCE: "Difference",
    }


class OperationEnumField(
    EnumField[OperationEnumAttrOperator, OperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OperationEnumAttrOperator
    PLUG_CLS = OperationEnumPlugOperator


class OperatorClassEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OTHER = 0
    BUILTIN = 1
    USER = 2


class OperatorClassEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OTHER = 0
    BUILTIN = 1
    USER = 2

    NAME_MAP = {
        OTHER: "other",
        BUILTIN: "builtIn",
        USER: "user",
    }


class OperatorClassEnumField(
    EnumField[OperatorClassEnumAttrOperator, OperatorClassEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OperatorClassEnumAttrOperator
    PLUG_CLS = OperatorClassEnumPlugOperator


class _GeneratedSelectionListOperator(DG):
    __slots__ = ()

    NODE_TYPE = "selectionListOperator"

    operation = OperationEnumField(default_value=0)
    op = operation

    inputListA = TypedField()
    ina = inputListA

    inputListB = TypedField()
    inb = inputListB

    outputList = TypedField()
    out = outputList

    operatorClass = OperatorClassEnumField(default_value=2)
    ocls = operatorClass
