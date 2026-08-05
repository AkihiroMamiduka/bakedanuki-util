# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_condition_dbl_l_extra_compose import (
    OutputField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class LogicEnumPlugOperator(EnumPlugOperator["LogicEnumAttrOperator"]):
    __slots__ = ()

    AND = 0
    OR = 1


class LogicEnumAttrOperator(EnumAttrOperator[LogicEnumPlugOperator]):
    __slots__ = ()

    AND = 0
    OR = 1

    NAME_MAP = {
        AND: "And",
        OR: "Or",
    }


class LogicEnumField(EnumField[LogicEnumAttrOperator, LogicEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = LogicEnumAttrOperator
    PLUG_CLS = LogicEnumPlugOperator


class ComparisonEnumPlugOperator(
    EnumPlugOperator["ComparisonEnumAttrOperator"]
):
    __slots__ = ()

    EQUAL = 0
    NOT_EQUAL = 1
    GREATER_THAN = 2
    GREATER_OR_EQUAL = 3
    LESS_THAN = 4
    LESS_OR_EQUAL = 5


class ComparisonEnumAttrOperator(EnumAttrOperator[ComparisonEnumPlugOperator]):
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


class ComparisonEnumField(
    EnumField[ComparisonEnumAttrOperator, ComparisonEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ComparisonEnumAttrOperator
    PLUG_CLS = ComparisonEnumPlugOperator


class GeneratedBdConditionDblLExtraCompose(DG):
    __slots__ = ()

    NODE_TYPE = "bdConditionDblLExtra_Compose"

    logic = LogicEnumField(default_value=0)
    lgc = logic

    comparison = ComparisonEnumField(default_value=0)
    cpr = comparison

    compareValue = DoubleLinearField(default_value=0.0)
    cv = compareValue

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputLogic = output.outputLogic
    olgc = outputLogic
    outputComparison = output.outputComparison
    ocpr = outputComparison
    outputCompareValue = output.outputCompareValue
    ocv = outputCompareValue
