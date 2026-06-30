# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class OperationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UNION = 0
    SUBTRACT = 1
    INTERSECT = 2


class OperationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UNION = 0
    SUBTRACT = 1
    INTERSECT = 2

    NAME_MAP = {
        UNION: "Union",
        SUBTRACT: "Subtract",
        INTERSECT: "Intersect",
    }


class OperationEnumField(
    EnumField[OperationEnumAttrOperator, OperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OperationEnumAttrOperator
    PLUG_CLS = OperationEnumPlugOperator


class Boolean(DG):
    __slots__ = ()

    NODE_TYPE = "boolean"

    inputShellA = TypedField()
    isa = inputShellA

    inputShellB = TypedField()
    isb = inputShellB

    operation = OperationEnumField()
    op = operation

    tolerance = DoubleLinearField()
    tlb = tolerance

    outputShell = TypedField()
    osh = outputShell
