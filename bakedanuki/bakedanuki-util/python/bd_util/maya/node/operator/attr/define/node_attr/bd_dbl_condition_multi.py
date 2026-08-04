# coding: utf-8

from typing import TYPE_CHECKING

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.double import (
    DoubleField,
    DoublePlugOperator,
)


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


class CasePlugOperator(CompoundPlugOperator["CaseAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("operation", "op"),
        ("compare", "cmp"),
        ("value", "v"),
    )

    operation = OperationEnumField(default_value=0)
    op = operation

    compare = DoubleField(default_value=0.0)
    cmp = compare

    if TYPE_CHECKING:
        value: DoublePlugOperator
        v: DoublePlugOperator
    else:
        value = DoubleField(default_value=0.0)
        v = value


class CaseAttrOperator(CompoundAttrOperator[CasePlugOperator]):
    __slots__ = ()

    operation = OperationEnumField(default_value=0)
    op = operation

    compare = DoubleField(default_value=0.0)
    cmp = compare

    value = DoubleField(default_value=0.0)
    v = value


class CaseField(CompoundField[CaseAttrOperator, CasePlugOperator]):
    __slots__ = ()

    ATTR_CLS = CaseAttrOperator
    PLUG_CLS = CasePlugOperator
