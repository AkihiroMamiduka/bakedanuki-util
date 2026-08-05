# coding: utf-8

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
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.typed import TypedField


class Case_extra_logicEnumPlugOperator(
    EnumPlugOperator["Case_extra_logicEnumAttrOperator"]
):
    __slots__ = ()

    AND = 0
    OR = 1


class Case_extra_logicEnumAttrOperator(
    EnumAttrOperator[Case_extra_logicEnumPlugOperator]
):
    __slots__ = ()

    AND = 0
    OR = 1

    NAME_MAP = {
        AND: "And",
        OR: "Or",
    }


class Case_extra_logicEnumField(
    EnumField[
        Case_extra_logicEnumAttrOperator, Case_extra_logicEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Case_extra_logicEnumAttrOperator
    PLUG_CLS = Case_extra_logicEnumPlugOperator


class Case_extra_comparisonEnumPlugOperator(
    EnumPlugOperator["Case_extra_comparisonEnumAttrOperator"]
):
    __slots__ = ()

    EQUAL = 0
    NOT_EQUAL = 1
    GREATER_THAN = 2
    GREATER_OR_EQUAL = 3
    LESS_THAN = 4
    LESS_OR_EQUAL = 5


class Case_extra_comparisonEnumAttrOperator(
    EnumAttrOperator[Case_extra_comparisonEnumPlugOperator]
):
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


class Case_extra_comparisonEnumField(
    EnumField[
        Case_extra_comparisonEnumAttrOperator,
        Case_extra_comparisonEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Case_extra_comparisonEnumAttrOperator
    PLUG_CLS = Case_extra_comparisonEnumPlugOperator


class Case_operationEnumPlugOperator(
    EnumPlugOperator["Case_operationEnumAttrOperator"]
):
    __slots__ = ()

    EQUAL = 0
    NOT_EQUAL = 1
    GREATER_THAN = 2
    GREATER_OR_EQUAL = 3
    LESS_THAN = 4
    LESS_OR_EQUAL = 5


class Case_operationEnumAttrOperator(
    EnumAttrOperator[Case_operationEnumPlugOperator]
):
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


class Case_operationEnumField(
    EnumField[Case_operationEnumAttrOperator, Case_operationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Case_operationEnumAttrOperator
    PLUG_CLS = Case_operationEnumPlugOperator


class Case_extraPlugOperator(CompoundPlugOperator["Case_extraAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("logic", "lgc"),
        ("comparison", "cpr"),
        ("compareValue", "cv"),
    )

    logic = Case_extra_logicEnumField(default_value=0)
    lgc = logic

    comparison = Case_extra_comparisonEnumField(default_value=0)
    cpr = comparison

    compareValue = DoubleLinearField(default_value=0.0)
    cv = compareValue


class Case_extraAttrOperator(CompoundAttrOperator[Case_extraPlugOperator]):
    __slots__ = ()

    logic = Case_extra_logicEnumField(default_value=0)
    lgc = logic

    comparison = Case_extra_comparisonEnumField(default_value=0)
    cpr = comparison

    compareValue = DoubleLinearField(default_value=0.0)
    cv = compareValue


class Case_extraField(
    CompoundField[Case_extraAttrOperator, Case_extraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Case_extraAttrOperator
    PLUG_CLS = Case_extraPlugOperator


class CasePlugOperator(CompoundPlugOperator["CaseAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("operation", "op"),
        ("compare", "cmp"),
        ("extra", "ex"),
        ("value", "v"),
    )

    operation = Case_operationEnumField(default_value=0)
    op = operation

    compare = DoubleLinearField(default_value=0.0)
    cmp = compare

    extra: Case_extraField = Case_extraField(
        multi=True, default_value=(0.0, 0.0, 0.0)
    )
    ex = extra

    value: TypedField = TypedField()
    v = value


class CaseAttrOperator(CompoundAttrOperator[CasePlugOperator]):
    __slots__ = ()

    operation = Case_operationEnumField(default_value=0)
    op = operation

    compare = DoubleLinearField(default_value=0.0)
    cmp = compare

    extra: Case_extraField = Case_extraField(
        multi=True, default_value=(0.0, 0.0, 0.0)
    )
    ex = extra

    value: TypedField = TypedField()
    v = value


class CaseField(CompoundField[CaseAttrOperator, CasePlugOperator]):
    __slots__ = ()

    ATTR_CLS = CaseAttrOperator
    PLUG_CLS = CasePlugOperator
