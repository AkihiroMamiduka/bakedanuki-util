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
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField


class Extra_logicEnumPlugOperator(
    EnumPlugOperator["Extra_logicEnumAttrOperator"]
):
    __slots__ = ()

    AND = 0
    OR = 1


class Extra_logicEnumAttrOperator(
    EnumAttrOperator[Extra_logicEnumPlugOperator]
):
    __slots__ = ()

    AND = 0
    OR = 1

    NAME_MAP = {
        AND: "And",
        OR: "Or",
    }


class Extra_logicEnumField(
    EnumField[Extra_logicEnumAttrOperator, Extra_logicEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Extra_logicEnumAttrOperator
    PLUG_CLS = Extra_logicEnumPlugOperator


class Extra_comparisonEnumPlugOperator(
    EnumPlugOperator["Extra_comparisonEnumAttrOperator"]
):
    __slots__ = ()

    EQUAL = 0
    NOT_EQUAL = 1
    GREATER_THAN = 2
    GREATER_OR_EQUAL = 3
    LESS_THAN = 4
    LESS_OR_EQUAL = 5


class Extra_comparisonEnumAttrOperator(
    EnumAttrOperator[Extra_comparisonEnumPlugOperator]
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


class Extra_comparisonEnumField(
    EnumField[
        Extra_comparisonEnumAttrOperator, Extra_comparisonEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Extra_comparisonEnumAttrOperator
    PLUG_CLS = Extra_comparisonEnumPlugOperator


class ExtraPlugOperator(CompoundPlugOperator["ExtraAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("logic", "lgc"),
        ("comparison", "cpr"),
        ("compareValue", "cv"),
    )

    logic = Extra_logicEnumField(default_value=0)
    lgc = logic

    comparison = Extra_comparisonEnumField(default_value=0)
    cpr = comparison

    compareValue = DoubleAngleField(default_value=0.0)
    cv = compareValue


class ExtraAttrOperator(CompoundAttrOperator[ExtraPlugOperator]):
    __slots__ = ()

    logic = Extra_logicEnumField(default_value=0)
    lgc = logic

    comparison = Extra_comparisonEnumField(default_value=0)
    cpr = comparison

    compareValue = DoubleAngleField(default_value=0.0)
    cv = compareValue


class ExtraField(CompoundField[ExtraAttrOperator, ExtraPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ExtraAttrOperator
    PLUG_CLS = ExtraPlugOperator
